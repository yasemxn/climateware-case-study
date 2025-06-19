# Climateware – Junior AI Engineer Case Study

For the position Junior AI Engineer case study. A system was developed to simulate an AI-based system that analyses carbon-emitting activities and provides customised emission reduction strategies using static JSON data and Azure OpenAI GPT-4o.

## 🚀 Project Overview

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


### 2. Create and activate virtual environment

python -m venv venv
source venv/bin/activate        # Mac/Linux
.\venv\Scripts\activate         # Windows

### 3. Install dependencies

pip install -r requirements.txt

### 4. Create .env file

AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_DEPLOYMENT_NAME=carbondeck-ai-candidate
AZURE_API_VERSION=2025-01-01-preview

### 5. Start server

uvicorn app.main:app --reload

##  API Reference
 POST /multi-activity-recommendations
 # Request Body:
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

# Response:

- A list of up to N recommendations
- A GPT summary of emission strategies

 POST /single-activity-recommendation
 # Request Body:
 {
  "id": "uuid-2",
  "name": "Diesel",
  "recommendationHistory": ["Replace diesel generators with solar PV"]
}
 # Response: 
 - A new recommendation not included in history
 - A GPT-generated explanation

### GPT-4o Integration
- The GPT model is used to:
    * Enrich recommendations with insights
    * Generate new suggestions
    * Provide strategy summaries
    * OpenAI SDK is integrated via Azure endpoint and authenticated using .env config.

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
