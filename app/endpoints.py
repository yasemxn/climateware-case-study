from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import json
from .utils import ask_gpt

router = APIRouter()

# load the dummy data
with open("app/dummy_data.json", "r") as f:
    RECOMMENDATIONS = json.load(f)

# models

class Activity(BaseModel):
    id: str
    name: str
    metadata: Dict

class MultiActivityRequest(BaseModel):
    activities: List[Activity]
    maxRecommendationAmount: int = 3

class SingleActivityRequest(BaseModel):
    id: str
    name: str
    recommendationHistory: List[str]

# First Endpoint: Multi Activity
@router.post("/multi-activity-recommendations")
def multi_activity_recommendations(request: MultiActivityRequest):
    results = []

    for activity in request.activities:
        matches = [
            rec for rec in RECOMMENDATIONS
            if rec["activityId"] == activity.id or rec["activityName"].lower() == activity.name.lower()
        ]
        results.extend(matches)

    if not results:
        raise HTTPException(status_code=404, detail="ERR_NO_ACTIVITY")

    seen = set()
    unique_results = []
    for item in results:
        key = (item["activityId"], item["recommendation"])
        if key not in seen:
            seen.add(key)
            unique_results.append(item)
        if len(unique_results) >= request.maxRecommendationAmount:
            break

    prompt = f"Given these activities: {[a.name for a in request.activities]}, suggest actions to reduce carbon emissions."
    gpt_reply = ask_gpt(prompt)

    return {
        "recommendations": unique_results,
        "gpt_summary": gpt_reply
    }

# Second Endpoint: Single Activity
@router.post("/single-activity-recommendation")
def single_activity_recommendation(request: SingleActivityRequest):
    matches = [
        rec for rec in RECOMMENDATIONS
        if rec["activityId"] == request.id or rec["activityName"].lower() == request.name.lower()
    ]

    new_recs = [
        rec for rec in matches
        if rec["recommendation"] not in request.recommendationHistory
    ]

    if not new_recs:
        raise HTTPException(status_code=404, detail="No new recommendations available.")

    prompt = f"Give a unique recommendation for reducing carbon emissions for activity '{request.name}' excluding: {request.recommendationHistory}"
    gpt_reply = ask_gpt(prompt)

    return {
        "newRecommendations": new_recs,
        "gpt_summary": gpt_reply
    }
