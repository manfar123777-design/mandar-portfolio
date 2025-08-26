1|from typing import List, Optional
2|from database import get_database, COLLECTIONS
3|from models import (
4|    PersonalInfo, PersonalInfoCreate, PersonalInfoUpdate,
5|    Experience, ExperienceCreate, ExperienceUpdate,
6|    Project, ProjectCreate, ProjectUpdate,
7|    Testimonial, TestimonialCreate, TestimonialUpdate,
8|    ContactMessage, ContactMessageCreate, ContactMessageUpdate,
9|    ContactStatus, ProjectStatus
10|)
11|from datetime import datetime
12|import uuid
13|
14|class PersonalInfoService:
15|    @staticmethod
16|    async def get_personal_info() -> Optional[PersonalInfo]:
17|        """Get personal information (should be only one record)"""
18|        db = await get_database()
19|        doc = await db[COLLECTIONS["personal_info"]].find_one()
20|        if doc:
21|            doc["_id"] = str(doc["_id"])
22|            return PersonalInfo(**doc)
23|        return None
24|    
25|    @staticmethod
26|    async def create_or_update_personal_info(data: PersonalInfoCreate) -> PersonalInfo:
27|        """Create or update personal information"""
28|        db = await get_database()
29|        
30|        # Check if record exists
31|        existing = await db[COLLECTIONS["personal_info"]].find_one()
32|        
33|        if existing:
34|            # Update existing record
35|            update_data = data.dict()
36|            update_data["updatedAt"] = datetime.utcnow()
37|            
38|            await db[COLLECTIONS["personal_info"]].update_one(
39|                {"_id": existing["_id"]}, 
40|                {"$set": update_data}
41|            )
42|            
43|            updated_doc = await db[COLLECTIONS["personal_info"]].find_one({"_id": existing["_id"]})
44|            updated_doc["_id"] = str(updated_doc["_id"])
45|            return PersonalInfo(**updated_doc)
46|        else:
47|            # Create new record
48|            personal_info = PersonalInfo(**data.dict())
49|            doc_dict = personal_info.dict(by_alias=True)
50|            
51|            await db[COLLECTIONS["personal_info"]].insert_one(doc_dict)
52|            return personal_info
53|
54|class ExperienceService:
55|    @staticmethod
56|    async def get_experiences(active_only: bool = True) -> List[Experience]:
57|        """Get all experiences sorted by display order"""
58|        db = await get_database()
59|        
60|        filter_dict = {"isActive": True} if active_only else {}
61|        cursor = db[COLLECTIONS["experiences"]].find(filter_dict).sort("displayOrder", 1)
62|        
63|        experiences = []
64|        async for doc in cursor:
65|            doc["_id"] = str(doc["_id"])
66|            experiences.append(Experience(**doc))
67|        
68|        return experiences
69|    
70|    @staticmethod
71|    async def create_experience(data: ExperienceCreate) -> Experience:
72|        """Create new experience"""
73|        db = await get_database()
74|        
75|        experience = Experience(**data.dict())
76|        doc_dict = experience.dict(by_alias=True)
77|        
78|        await db[COLLECTIONS["experiences"]].insert_one(doc_dict)
79|        return experience
80|    
81|    @staticmethod
82|    async def update_experience(experience_id: str, data: ExperienceUpdate) -> Optional[Experience]:
83|        """Update experience by ID"""
84|        db = await get_database()
85|        
86|        update_data = {k: v for k, v in data.dict().items() if v is not None}
87|        if not update_data:
88|            return None
89|        
90|        update_data["updatedAt"] = datetime.utcnow()
91|        
92|        result = await db[COLLECTIONS["experiences"]].update_one(
93|            {"_id": experience_id},
94|            {"$set": update_data}
95|        )
96|        
97|        if result.modified_count:
98|            doc = await db[COLLECTIONS["experiences"]].find_one({"_id": experience_id})
99|            if doc:
100|                doc["_id"] = str(doc["_id"])
101|                return Experience(**doc)
102|        
103|        return None
104|    
105|    @staticmethod
106|    async def delete_experience(experience_id: str) -> bool:
107|        """Soft delete experience by setting isActive to False"""
108|        db = await get_database()
109|        
110|        result = await db[COLLECTIONS["experiences"]].update_one(
111|            {"_id": experience_id},
112|            {"$set": {"isActive": False, "updatedAt": datetime.utcnow()}}
113|        )
114|        
115|        return result.modified_count > 0
116|
117|class ProjectService:
118|    @staticmethod
119|    async def get_projects(category: Optional[str] = None, active_only: bool = True) -> List[Project]:
120|        """Get projects, optionally filtered by category"""
121|        db = await get_database()
122|        
123|        filter_dict = {"isActive": True} if active_only else {}
124|        if category:
125|            filter_dict["category"] = category
126|        
127|        cursor = db[COLLECTIONS["projects"]].find(filter_dict).sort("displayOrder", 1)
128|        
129|        projects = []
130|        async for doc in cursor:
131|            doc["_id"] = str(doc["_id"])
132|            projects.append(Project(**doc))
133|        
134|        return projects
135|    
136|    @staticmethod
137|    async def create_project(data: ProjectCreate) -> Project:
138|        """Create new project"""
139|        db = await get_database()
140|        
141|        project = Project(**data.dict())
142|        doc_dict = project.dict(by_alias=True)
143|        
144|        await db[COLLECTIONS["projects"]].insert_one(doc_dict)
145|        return project
146|    
147|    @staticmethod
148|    async def update_project(project_id: str, data: ProjectUpdate) -> Optional[Project]:
149|        """Update project by ID"""
150|        db = await get_database()
151|        
152|        update_data = {k: v for k, v in data.dict().items() if v is not None}
153|        if not update_data:
154|            return None
155|        
156|        update_data["updatedAt"] = datetime.utcnow()
157|        
158|        result = await db[COLLECTIONS["projects"]].update_one(
159|            {"_id": project_id},
160|            {"$set": update_data}
161|        )
162|        
163|        if result.modified_count:
164|            doc = await db[COLLECTIONS["projects"]].find_one({"_id": project_id})
165|            if doc:
166|                doc["_id"] = str(doc["_id"])
167|                return Project(**doc)
168|        
169|        return None
170|    
171|    @staticmethod
172|    async def delete_project(project_id: str) -> bool:
173|        """Soft delete project"""
174|        db = await get_database()
175|        
176|        result = await db[COLLECTIONS["projects"]].update_one(
177|            {"_id": project_id},
178|            {"$set": {"isActive": False, "updatedAt": datetime.utcnow()}}
179|        )
180|        
181|        return result.modified_count > 0
182|
183|class TestimonialService:
184|    @staticmethod
185|    async def get_testimonials(active_only: bool = True) -> List[Testimonial]:
186|        """Get all testimonials sorted by display order"""
187|        db = await get_database()
188|        
189|        filter_dict = {"isActive": True} if active_only else {}
190|        cursor = db[COLLECTIONS["testimonials"]].find(filter_dict).sort("displayOrder", 1)
191|        
192|        testimonials = []
193|        async for doc in cursor:
194|            doc["_id"] = str(doc["_id"])
195|            testimonials.append(Testimonial(**doc))
196|        
197|        return testimonials
198|    
199|    @staticmethod
200|    async def create_testimonial(data: TestimonialCreate) -> Testimonial:
201|        """Create new testimonial"""
202|        db = await get_database()
203|        
204|        testimonial = Testimonial(**data.dict())
205|        doc_dict = testimonial.dict(by_alias=True)
206|        
207|        await db[COLLECTIONS["testimonials"]].insert_one(doc_dict)
208|        return testimonial
209|
210|class ContactService:
211|    @staticmethod
212|    async def create_contact_message(data: ContactMessageCreate) -> ContactMessage:
213|        """Create new contact message"""
214|        db = await get_database()
215|        
216|        message = ContactMessage(**data.dict())
217|        doc_dict = message.dict(by_alias=True)
218|        
219|        await db[COLLECTIONS["contact_messages"]].insert_one(doc_dict)
220|        return message
221|    
222|    @staticmethod
223|    async def get_contact_messages() -> List[ContactMessage]:
224|        """Get all contact messages (admin only)"""
225|        db = await get_database()
226|        
227|        cursor = db[COLLECTIONS["contact_messages"]].find().sort("createdAt", -1)
228|        
229|        messages = []
230|        async for doc in cursor:
231|            doc["_id"] = str(doc["_id"])
232|            messages.append(ContactMessage(**doc))
233|        
234|        return messages
235|    
236|    @staticmethod
237|    async def update_message_status(message_id: str, status: ContactStatus) -> Optional[ContactMessage]:
238|        """Update contact message status"""
239|        db = await get_database()
240|        
241|        result = await db[COLLECTIONS["contact_messages"]].update_one(
242|            {"_id": message_id},
243|            {"$set": {"status": status, "updatedAt": datetime.utcnow()}}
244|        )
245|        
246|        if result.modified_count:
247|            doc = await db[COLLECTIONS["contact_messages"]].find_one({"_id": message_id})
248|            if doc:
249|                doc["_id"] = str(doc["_id"])
250|                return ContactMessage(**doc)
251|        
252|        return None

