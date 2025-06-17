from fastapi import FastAPI, UploadFile, Form       #  Creates the API Server 
from fastapi.middleware.cors import CORSMiddleware    # Allows frontend websites to access your backend 
from pydantic import BaseModel                        # Used for request/response schemas 
from backend.scraper import WebScraperAgent  

from backend.ai_processor import process_with_gemini
from backend.models import DeeplearningCourseList

     # Imports the custom logic from other files in the backend/ folders 
 


app = FastAPI() # This creates the server 

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], # In production, restrict to specific domain
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"]   # it means to allow all the fronts ends, but later we want to restrict this in prod
)

scraper = WebScraperAgent()

class ScrapperRequest(BaseModel): 
    url: str 
    instructions: str

@app.get("/")
def root():
    return {"message": "Backend running"}

# Defining the actual routing process 
@app.post("/process")
def run_processing():
    return process_with_gemini("https://example.com")

@app.post("/scrape")
async def scrape_and_process(data: ScrapperRequest): 
    try: 
        html_content = await scraper.scrape_content(data.url)

        result = process_with_gemini(
            html=html_content, 
            instructions=data.instructions
        )
        await scraper.close()

        return { 
            "success": True, 
            "data": result
        }

    except Exception as e: 
        return {"success": False, "error": str(e)}