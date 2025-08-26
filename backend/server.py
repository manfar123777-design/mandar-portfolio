Excellent! 🎉 Great job adding the `backend/requirements.txt` file. Now let's add the next essential file.

## 📄 **Next: Add backend/server.py (Main API File)**

This is the core of your backend API. Let me show you the content:
Action: file_editor view /app/backend/server.py
Observation: /app/backend/server.py:
1|from fastapi import FastAPI, APIRouter, HTTPException, Query
2|from fastapi.responses import JSONResponse
3|from dotenv import load_dotenv
4|from starlette.middleware.cors import CORSMiddleware
5|import os
6|import logging
7|from pathlib import Path
8|from typing import List, Optional
9|
10|# Import our models and services
11|from models import (
12|    PersonalInfo, PersonalInfoCreate, PersonalInfoUpdate,
13|    Experience, ExperienceCreate, ExperienceUpdate,
14|    Project, ProjectCreate, ProjectUpdate,
15|    Testimonial, TestimonialCreate, TestimonialUpdate,
16|    ContactMessage, ContactMessageCreate, ContactMessageUpdate,
17|    MessageResponse, ListResponse, ContactStatus
18|)
19|from services import (
20|    PersonalInfoService, ExperienceService, ProjectService, 
21|    TestimonialService, ContactService
22|)
23|from database import connect_to_mongo, close_mongo_connection
24|from seed_data import seed_database
25|
26|ROOT_DIR = Path(__file__).parent
27|load_dotenv(ROOT_DIR / '.env')
28|
29|# Create the main app without a prefix
30|app = FastAPI(title="Portfolio API", version="1.0.0")
31|
32|# Create a router with the /api prefix
33|api_router = APIRouter(prefix="/api")
34|
35|# Health check endpoint
36|@api_router.get("/")
37|async def root():
38|    return {"message": "Portfolio API is running!", "status": "healthy"}
39|
40|# Personal Information Endpoints
41|@api_router.get("/personal-info", response_model=PersonalInfo)
42|async def get_personal_info():
43|    """Get personal information"""
44|    try:
45|        personal_info = await PersonalInfoService.get_personal_info()
46|        if not personal_info:
47|            raise HTTPException(status_code=404, detail="Personal information not found")
48|        return personal_info
49|    except Exception as e:
50|        raise HTTPException(status_code=500, detail=str(e))
51|
52|@api_router.put("/personal-info", response_model=PersonalInfo)
53|async def update_personal_info(data: PersonalInfoCreate):
54|    """Update personal information (admin only)"""
55|    try:
56|        personal_info = await PersonalInfoService.create_or_update_personal_info(data)
57|        return personal_info
58|    except Exception as e:
59|        raise HTTPException(status_code=500, detail=str(e))
60|
61|# Experience Endpoints
62|@api_router.get("/experiences", response_model=List[Experience])
63|async def get_experiences():
64|    """Get all active experiences"""
65|    try:
66|        experiences = await ExperienceService.get_experiences()
67|        return experiences
68|    except Exception as e:
69|        raise HTTPException(status_code=500, detail=str(e))
70|
71|@api_router.post("/experiences", response_model=Experience)
72|async def create_experience(data: ExperienceCreate):
73|    """Create new experience (admin only)"""
74|    try:
75|        experience = await ExperienceService.create_experience(data)
76|        return experience
77|    except Exception as e:
78|        raise HTTPException(status_code=500, detail=str(e))
79|
80|@api_router.put("/experiences/{experience_id}", response_model=Experience)
81|async def update_experience(experience_id: str, data: ExperienceUpdate):
82|    """Update experience (admin only)"""
83|    try:
84|        experience = await ExperienceService.update_experience(experience_id, data)
85|        if not experience:
86|            raise HTTPException(status_code=404, detail="Experience not found")
87|        return experience
88|    except Exception as e:
89|        raise HTTPException(status_code=500, detail=str(e))
90|
91|@api_router.delete("/experiences/{experience_id}", response_model=MessageResponse)
92|async def delete_experience(experience_id: str):
93|    """Delete experience (admin only)"""
94|    try:
95|        success = await ExperienceService.delete_experience(experience_id)
96|        if not success:
97|            raise HTTPException(status_code=404, detail="Experience not found")
98|        return MessageResponse(message="Experience deleted successfully")
99|    except Exception as e:
100|        raise HTTPException(status_code=500, detail=str(e))
101|
102|# Project Endpoints
103|@api_router.get("/projects", response_model=List[Project])
104|async def get_projects(category: Optional[str] = Query(None, description="Filter by category")):
105|    """Get all active projects, optionally filtered by category"""
106|    try:
107|        projects = await ProjectService.get_projects(category=category)
108|        return projects
109|    except Exception as e:
110|        raise HTTPException(status_code=500, detail=str(e))
111|
112|@api_router.post("/projects", response_model=Project)
113|async def create_project(data: ProjectCreate):
114|    """Create new project (admin only)"""
115|    try:
116|        project = await ProjectService.create_project(data)
117|        return project
118|    except Exception as e:
119|        raise HTTPException(status_code=500, detail=str(e))
120|
121|@api_router.put("/projects/{project_id}", response_model=Project)
122|async def update_project(project_id: str, data: ProjectUpdate):
123|    """Update project (admin only)"""
124|    try:
125|        project = await ProjectService.update_project(project_id, data)
126|        if not project:
127|            raise HTTPException(status_code=404, detail="Project not found")
128|        return project
129|    except Exception as e:
130|        raise HTTPException(status_code=500, detail=str(e))
131|
132|@api_router.delete("/projects/{project_id}", response_model=MessageResponse)
133|async def delete_project(project_id: str):
134|    """Delete project (admin only)"""
135|    try:
136|        success = await ProjectService.delete_project(project_id)
137|        if not success:
138|            raise HTTPException(status_code=404, detail="Project not found")
139|        return MessageResponse(message="Project deleted successfully")
140|    except Exception as e:
141|        raise HTTPException(status_code=500, detail=str(e))
142|
143|# Testimonial Endpoints
144|@api_router.get("/testimonials", response_model=List[Testimonial])
145|async def get_testimonials():
146|    """Get all active testimonials"""
147|    try:
148|        testimonials = await TestimonialService.get_testimonials()
149|        return testimonials
150|    except Exception as e:
151|        raise HTTPException(status_code=500, detail=str(e))
152|
153|@api_router.post("/testimonials", response_model=Testimonial)
154|async def create_testimonial(data: TestimonialCreate):
155|    """Create new testimonial (admin only)"""
156|    try:
157|        testimonial = await TestimonialService.create_testimonial(data)
158|        return testimonial
159|    except Exception as e:
160|        raise HTTPException(status_code=500, detail=str(e))
161|
162|# Contact Endpoints
163|@api_router.post("/contact", response_model=MessageResponse)
164|async def submit_contact_form(data: ContactMessageCreate):
165|    """Submit contact form"""
166|    try:
167|        message = await ContactService.create_contact_message(data)
168|        return MessageResponse(
169|            message="Thank you for your message! I'll get back to you within 24 hours.",
170|            data={"messageId": message.id}
171|        )
172|    except Exception as e:
173|        raise HTTPException(status_code=500, detail=str(e))
174|
175|@api_router.get("/contact-messages", response_model=List[ContactMessage])
176|async def get_contact_messages():
177|    """Get all contact messages (admin only)"""
178|    try:
179|        messages = await ContactService.get_contact_messages()
180|        return messages
181|    except Exception as e:
182|        raise HTTPException(status_code=500, detail=str(e))
183|
184|@api_router.put("/contact-messages/{message_id}/status", response_model=ContactMessage)
185|async def update_message_status(message_id: str, data: ContactMessageUpdate):
186|    """Update contact message status (admin only)"""
187|    try:
188|        message = await ContactService.update_message_status(message_id, data.status)
189|        if not message:
190|            raise HTTPException(status_code=404, detail="Message not found")
191|        return message
192|    except Exception as e:
193|        raise HTTPException(status_code=500, detail=str(e))
194|
195|# Seed database endpoint (for development)
196|@api_router.post("/seed-database", response_model=MessageResponse)
197|async def seed_database_endpoint():
198|    """Seed database with initial data (development only)"""
199|    try:
200|        await seed_database()
201|        return MessageResponse(message="Database seeded successfully!")
202|    except Exception as e:
203|        raise HTTPException(status_code=500, detail=f"Error seeding database: {str(e)}")
204|
205|# Include the router in the main app
206|app.include_router(api_router)
207|
208|app.add_middleware(
209|    CORSMiddleware,
210|    allow_credentials=True,
211|    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
212|    allow_methods=["*"],
213|    allow_headers=["*"],
214|)
215|
216|# Configure logging
217|logging.basicConfig(
218|    level=logging.INFO,
219|    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
220|)
221|logger = logging.getLogger(__name__)
222|
223|@app.on_event("startup")
224|async def startup_db_client():
225|    await connect_to_mongo()
226|
227|@app.on_event("shutdown")
228|async def shutdown_db_client():
229|    await close_mongo_connection()
230|

