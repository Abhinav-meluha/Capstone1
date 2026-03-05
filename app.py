import os
import json
import base64
import asyncio
from typing import List, Optional, Dict, Any
from fastapi import FastAPI, WebSocket, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai import types

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

app = FastAPI(title="Cultural AI Backend")

# --- DATA FROM constants.tsx ---
DESTINATIONS = [
    {"city": "Kyoto", "country": "Japan", "culture": 9.9, "cost": "High", "season": "Spring"},
    {"city": "Paris", "country": "France", "culture": 9.5, "cost": "High", "season": "Spring"},
    {"city": "Cusco", "country": "Peru", "culture": 9.8, "cost": "Medium", "season": "Spring"},
    {"city": "Cairo", "country": "Egypt", "culture": 9.7, "cost": "Low", "season": "Winter"},
    {"city": "Rome", "country": "Italy", "culture": 9.6, "cost": "High", "season": "Autumn"},
    {"city": "Jaipur", "country": "India", "culture": 9.4, "cost": "Low", "season": "Winter"},
    {"city": "New York", "country": "USA", "culture": 8.5, "cost": "V. High", "season": "Autumn"},
    {"city": "Sydney", "country": "Australia", "culture": 8.0, "cost": "High", "season": "Summer"},
    {"city": "Cape Town", "country": "South Africa", "culture": 8.8, "cost": "Medium", "season": "Summer"}
]

# --- MODELS & SCHEMAS ---
class ItineraryConfig(BaseModel):
    city: str
    days: int
    season: str
    budget: str
    pace: str
    interests: List[str]
    customNotes: Optional[str] = None

# --- CORE SERVICES FROM geminiService.ts ---

@app.post("/api/itinerary")
async def get_itinerary(config: ItineraryConfig):
    """High-reasoning itinerary generation with Google Search grounding."""
    model = genai.GenerativeModel('gemini-3.1-pro-preview')
    
    prompt = f"""Perform a high-reasoning spatial and cultural analysis for a {config.days}-day trip to {config.city}.
    CRITICAL PARAMETERS:
    - Season: {config.season} | Budget: {config.budget} | Pace: {config.pace}
    - Interests: {", ".join(config.interests) if config.interests else 'Balanced mix'}
    - Directives: {config.customNotes or 'None'}
    
    Grounding Requirement: Use Google Search for 2024/2025 trending venues and cultural events.
    Output Style: Sophisticated travel document with 'Insider Secrets' for each day."""

    response = model.generate_content(
        prompt,
        tools=[{"google_search": {}}],
        generation_config=types.GenerationConfig(
            thinking_config={"thinking_level": "HIGH"}
        )
    )
    
    # Extract grounding sources
    sources = []
    if response.candidates[0].grounding_metadata.search_entry_point:
        chunks = response.candidates[0].grounding_metadata.grounding_chunks
        sources = [{"title": c.web.title, "uri": c.web.uri} for c in chunks if c.web]

    return {"text": response.text, "sources": sources}

@app.get("/api/cultural-pulse")
async def get_cultural_pulse():
    """Real-time global cultural scan with JSON output."""
    model = genai.GenerativeModel('gemini-3.1-pro-preview')
    
    # Define response schema
    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "location": {"type": "string"},
                "insight": {"type": "string"},
                "category": {"type": "string"},
                "sourceUrl": {"type": "string"}
            },
            "required": ["title", "location", "insight", "category"]
        }
    }

    response = model.generate_content(
        "Identify 6 significant cultural shifts or festivals happening globally in February 2026.",
        tools=[{"google_search": {}}],
        generation_config=types.GenerationConfig(
            response_mime_type="application/json",
            response_schema=schema,
            thinking_config={"thinking_level": "HIGH"}
        )
    )
    return json.loads(response.text)

@app.post("/api/generate-image")
async def generate_image(prompt: str):
    """Image generation using gemini-2.5-flash-image."""
    model = genai.GenerativeModel('gemini-2.5-flash-image')
    response = model.generate_content(
        f"High-fidelity cultural visualization: {prompt}",
        generation_config={"aspect_ratio": "16:9"}
    )
    # Binary image data is returned in parts[0].inline_data.data
    img_part = response.candidates[0].content.parts[0]
    b64_data = base64.b64encode(img_part.inline_data.data).decode()
    return {"image_url": f"data:{img_part.inline_data.mime_type};base64,{b64_data}"}

@app.post("/api/generate-speech")
async def generate_speech(text: str):
    """Speech synthesis using gemini-2.5-flash-preview-tts."""
    model = genai.GenerativeModel('gemini-2.5-flash-preview-tts')
    response = model.generate_content(
        f"Read this with a sophisticated, professional cultural guide voice: {text}",
        generation_config=types.GenerationConfig(
            response_modalities=["AUDIO"],
            speech_config={"voice_config": {"prebuilt_voice_config": {"voice_name": "Kore"}}}
        )
    )
    audio_part = response.candidates[0].content.parts[0]
    b64_audio = base64.b64encode(audio_part.inline_data.data).decode()
    return {"audio_url": f"data:audio/wav;base64,{b64_audio}"}

# --- LIVE SENTINEL WEBSOCKET FROM liveService.ts ---

@app.websocket("/ws/live-sentinel")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket bridge for the Multimodal Live API."""
    await websocket.accept()
    
    # Multimodal Live connection using the Python SDK
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    async with model.aio.live_connect(
        config=types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            system_instruction="You are a supreme travel AI sentinel. Be helpful and insightful."
        )
    ) as session:
        
        async def receive_from_client():
            while True:
                data = await websocket.receive_json()
                # Sending text or audio to the Gemini Live session
                if "text" in data:
                    await session.send(data["text"], end_of_turn=True)
                elif "audio" in data:
                    await session.send({"mime_type": "audio/pcm", "data": data["audio"]})

        async def send_to_client():
            async for message in session:
                if message.server_content:
                    # Forward Gemini's audio/text back to the UI
                    resp = {}
                    if message.server_content.model_turn:
                        parts = message.server_content.model_turn.parts
                        for part in parts:
                            if part.text: resp["text"] = part.text
                            if part.inline_data: 
                                resp["audio"] = base64.b64encode(part.inline_data.data).decode()
                    await websocket.send_json(resp)

        await asyncio.gather(receive_from_client(), send_to_client())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
