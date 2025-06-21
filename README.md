# Climateware – Junior AI Engineer Case Study

For the position Junior AI Engineer case study. A system was developed to simulate an AI-based system that analyses carbon-emitting activities and provides customised emission reduction strategies using static JSON data and Azure OpenAI GPT-4o.

## Project Overview

The system exposes two FastAPI endpoints:

1. **`/multi-activity-recommendations`**  
   > Takes a list of activities and returns the most relevant carbon reduction strategies from static data + GPT-powered summary.

2. **`/single-activity-recommendation`**  
   > Takes one activity and its recommendation history, returning only new, unique suggestions + GPT-powered insight.

All responses include structured recommendations and a GPT-4o-generated expert explanation.

---

## How to Run

### 1. Clone this repo
```bash
git clone https://github.com/your-username/climateware-case.git
cd climateware-case

```

### 2. Create and activate virtual environment

python -m venv venv
source venv/bin/activate        # For Mac/Linux
.\venv\Scripts\activate         # For Windows

### 3. Install dependencies

pip install -r requirements.txt

### 4. Create an .env file

AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_DEPLOYMENT_NAME=carbondeck-ai-candidate
AZURE_API_VERSION=2025-01-01-preview

### 5. Start server

uvicorn app.main:app --reload

##  API Reference
 POST /multi-activity-recommendations
 #### Request Body:
 {
  "activities": [
    {
      "id": "uuid-2",
      "name": "Diesel",
      "metadata": {}
    }
  ],
  "maxRecommendationAmount": 2
}

 #### Response:

- A list of up to N recommendations
- A GPT summary of emission strategies

 POST /single-activity-recommendation
 #### Request Body:
 {
  "id": "uuid-2",
  "name": "Diesel",
  "recommendationHistory": ["Replace diesel generators with solar PV"]
}
  #### Response: 
 - A new recommendation not included in history
 - A GPT-generated explanation

### GPT-4o Integration
- The GPT model is used to enrich recommendations with insights, generate new suggestions, provide strategy summaries and OpenAI SDK is integrated via Azure endpoint and authenticated using .env config.


# Revision Notes

As per the feedback received from Climateware, the following enhancements and fixes were applied:

 ### 1. Improved GPT Summary Structure
    Replaced generic GPT responses with structured, ranked, and reasoned summaries.

The smart_summary now highlights priority, impact, feasibility, and justification for each recommendation in markdown format.

 ### 2. Ranking Logic Added
 Implemented a custom ranking algorithm based on:
 * estimatedReductionPercentage (impact), feasibilityScore (feasibility), and cost (inverted).
 Summary now presents recommendations in ranked order with clearly stated rationale.

### Single Activity Summary Enhancements

If only one recommendation is returned, the GPT output presents a detailed evaluation, listing:
- strengths,
- - weaknesses,
  - and improvement opportunities.

### Error Handling & API Fixes

Resolved previous internal server error due to build_reasoning_prompt not being defined. Implemented proper 404 and 500 response messages for edge cases.

# NOTES:
- The system uses static data from dummy_data.json — no live API or DB.
- GPT logic is isolated in utils.py and can be easily swapped with other LLMs or backends.
- To use the latest OpenAI SDK, refer to the migration notes in utils.py.

# DELIVERABLES:

 Fully working FastAPI backend
 Two structured endpoints
 GPT-4o integration via Azure OpenAI
 Static dummy data usage

 Full README documentation
