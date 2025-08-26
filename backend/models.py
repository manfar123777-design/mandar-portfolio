Perfect! Here's the `backend/models.py` file - this defines all your data structures:
Action: file_editor view /app/backend/models.py
Observation: /app/backend/models.py:
1|from pydantic import BaseModel, Field, EmailStr
2|from typing import List, Optional
3|from datetime import datetime
4|from enum import Enum
5|import uuid
6|
7|class ContactStatus(str, Enum):
8|    NEW = "new"
9|    READ = "read"
10|    REPLIED = "replied"
11|
12|class ProjectStatus(str, Enum):
13|    ACTIVE = "Active"
14|    COMPLETED = "Completed"
15|
16|# Personal Information Models
17|class PersonalInfo(BaseModel):
18|    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
19|    name: str
20|    tagline: str
21|    email: EmailStr
22|    phone: str
23|    location: str
24|    linkedin: str
25|    yearsExperience: int
26|    createdAt: datetime = Field(default_factory=datetime.utcnow)
27|    updatedAt: datetime = Field(default_factory=datetime.utcnow)
28|
29|    class Config:
30|        populate_by_name = True
31|
32|class PersonalInfoCreate(BaseModel):
33|    name: str
34|    tagline: str
35|    email: EmailStr
36|    phone: str
37|    location: str
38|    linkedin: str
39|    yearsExperience: int
40|
41|class PersonalInfoUpdate(BaseModel):
42|    name: Optional[str] = None
43|    tagline: Optional[str] = None
44|    email: Optional[EmailStr] = None
45|    phone: Optional[str] = None
46|    location: Optional[str] = None
47|    linkedin: Optional[str] = None
48|    yearsExperience: Optional[int] = None
49|    updatedAt: datetime = Field(default_factory=datetime.utcnow)
50|
51|# Experience Models
52|class Experience(BaseModel):
53|    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
54|    title: str
55|    company: str
56|    period: str
57|    type: str
58|    description: str
59|    achievements: List[str]
60|    displayOrder: int = 0
61|    isActive: bool = True
62|    createdAt: datetime = Field(default_factory=datetime.utcnow)
63|    updatedAt: datetime = Field(default_factory=datetime.utcnow)
64|
65|    class Config:
66|        populate_by_name = True
67|
68|class ExperienceCreate(BaseModel):
69|    title: str
70|    company: str
71|    period: str
72|    type: str
73|    description: str
74|    achievements: List[str]
75|    displayOrder: int = 0
76|
77|class ExperienceUpdate(BaseModel):
78|    title: Optional[str] = None
79|    company: Optional[str] = None
80|    period: Optional[str] = None
81|    type: Optional[str] = None
82|    description: Optional[str] = None
83|    achievements: Optional[List[str]] = None
84|    displayOrder: Optional[int] = None
85|    isActive: Optional[bool] = None
86|    updatedAt: datetime = Field(default_factory=datetime.utcnow)
87|
88|# Project Models
89|class Project(BaseModel):
90|    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
91|    title: str
92|    category: str
93|    description: str
94|    technologies: List[str]
95|    achievements: List[str]
96|    duration: str
97|    status: ProjectStatus
98|    displayOrder: int = 0
99|    isActive: bool = True
100|    createdAt: datetime = Field(default_factory=datetime.utcnow)
101|    updatedAt: datetime = Field(default_factory=datetime.utcnow)
102|
103|    class Config:
104|        populate_by_name = True
105|
106|class ProjectCreate(BaseModel):
107|    title: str
108|    category: str
109|    description: str
110|    technologies: List[str]
111|    achievements: List[str]
112|    duration: str
113|    status: ProjectStatus
114|    displayOrder: int = 0
115|
116|class ProjectUpdate(BaseModel):
117|    title: Optional[str] = None
118|    category: Optional[str] = None
119|    description: Optional[str] = None
120|    technologies: Optional[List[str]] = None
121|    achievements: Optional[List[str]] = None
122|    duration: Optional[str] = None
123|    status: Optional[ProjectStatus] = None
124|    displayOrder: Optional[int] = None
125|    isActive: Optional[bool] = None
126|    updatedAt: datetime = Field(default_factory=datetime.utcnow)
127|
128|# Testimonial Models
129|class Testimonial(BaseModel):
130|    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
131|    name: str
132|    position: str
133|    company: str
134|    text: str
135|    rating: int = Field(ge=1, le=5)
136|    displayOrder: int = 0
137|    isActive: bool = True
138|    createdAt: datetime = Field(default_factory=datetime.utcnow)
139|    updatedAt: datetime = Field(default_factory=datetime.utcnow)
140|
141|    class Config:
142|        populate_by_name = True
143|
144|class TestimonialCreate(BaseModel):
145|    name: str
146|    position: str
147|    company: str
148|    text: str
149|    rating: int = Field(ge=1, le=5)
150|    displayOrder: int = 0
151|
152|class TestimonialUpdate(BaseModel):
153|    name: Optional[str] = None
154|    position: Optional[str] = None
155|    company: Optional[str] = None
156|    text: Optional[str] = None
157|    rating: Optional[int] = Field(None, ge=1, le=5)
158|    displayOrder: Optional[int] = None
159|    isActive: Optional[bool] = None
160|    updatedAt: datetime = Field(default_factory=datetime.utcnow)
161|
162|# Contact Models
163|class ContactMessage(BaseModel):
164|    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
165|    name: str
166|    email: EmailStr
167|    subject: str
168|    message: str
169|    status: ContactStatus = ContactStatus.NEW
170|    createdAt: datetime = Field(default_factory=datetime.utcnow)
171|    updatedAt: datetime = Field(default_factory=datetime.utcnow)
172|
173|    class Config:
174|        populate_by_name = True
175|
176|class ContactMessageCreate(BaseModel):
177|    name: str
178|    email: EmailStr
179|    subject: str
180|    message: str
181|
182|class ContactMessageUpdate(BaseModel):
183|    status: ContactStatus
184|    updatedAt: datetime = Field(default_factory=datetime.utcnow)
185|
186|# Response Models
187|class MessageResponse(BaseModel):
188|    message: str
189|    data: Optional[dict] = None
190|
191|class ListResponse(BaseModel):
192|    items: List[dict]
193|    count: int
194|    message: str = "Success"

