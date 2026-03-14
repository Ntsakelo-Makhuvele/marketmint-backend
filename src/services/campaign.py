import os
from dotenv import load_dotenv
from google import genai
from src.schemas.campaign import CampaignCreateRequest, CampaignAssets
from google.genai import types
import time
import json
load_dotenv()

MARKETMINT_SYSTEM_INSTRUCTIONS = """
You are MarketMint, an intuitive creative director and campaign orchestrator.
Your goal is to transform a single campaign intent into a cohesive suite of assets.

Rules for Analysis:
1. Prioritize Authenticity: Avoid generic, corporate, or overly "AI-generated" phrasing. 
2. Content Cohesion: Ensure the email, SMS, and video prompt share a unified brand voice.
3. Creative Prompts: The video and image prompts must be detailed, cinematic, and optimized for models like Google Veo and Nano Banana.
4. Strict Output: Your response MUST be a JSON object that strictly adheres to the provided schema. No markdown backticks or preamble.
"""

class CampaignService:
    def __init__(self):
            self.client = genai.Client(
             
                vertexai=True, 
                project="marketmint-489521", 
                location="us-central1",
                http_options=types.HttpOptions(api_version="v1")
            )

    def create_email_campaign(self, campaign_data: CampaignCreateRequest):
        # In 2026, we use Gemini 2.5 Flash for the best speed/cost
        response = self.client.models.generate_content(
            
            model="gemini-2.5-flash",
            contents=f"Create a campaign for: {campaign_data}",
            config=types.GenerateContentConfig(
                system_instruction="""
You are MarketMint, an intuitive creative director and campaign orchestrator.
Your goal is to transform a single campaign intent into a cohesive suite of assets.

Rules for Analysis:
1. Prioritize Authenticity: Avoid generic, corporate, or overly "AI-generated" phrasing. 
2. Content Cohesion: Ensure the email, SMS, and video prompt share a unified brand voice.
3. Creative Prompts: The video and image prompts must be detailed, cinematic, and optimized for models like Google Veo and Nano Banana.
4. Strict Output: Your response MUST be a JSON object that strictly adheres to the provided schema. No markdown backticks or preamble.
""",
                response_mime_type="application/json",
                response_schema=CampaignAssets,
                temperature=0.4
            )
            
        )
    
        return response.parsed# This is your structured output ready to be parsed and used for asset generation.
    
    
    def create_video(self, video_prompt: str):
        operation = self.client.models.generate_videos(
            model="veo-3.1-generate-preview",
            prompt=video_prompt,
            config=types.GenerateVideosConfig(
                 duration_seconds=6,
                 aspect_ratio="9:16"
            )
        )
        
        print("marketmint is filming your video....")
        
        while not operation.done:
            time.sleep(5)
            operation = self.client.operations.get(operation)

        generated_video = operation.result.generated_videos[0]  

        video_path = "marketmint_promo.mp4"
        generated_video.video.save(video_path)

        return video_path