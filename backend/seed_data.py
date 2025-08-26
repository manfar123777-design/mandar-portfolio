1|from services import PersonalInfoService, ExperienceService, ProjectService, TestimonialService
2|from models import (
3|    PersonalInfoCreate, ExperienceCreate, ProjectCreate, TestimonialCreate,
4|    ProjectStatus
5|)
6|
7|# Mock data for seeding - matching the frontend mock data
8|PERSONAL_INFO_DATA = PersonalInfoCreate(
9|    name="Mandar Farande",
10|    tagline="Customer Relations Advisor | Nutritional & Fitness Consultant | Pharmacist | Trainer | Theological Educator",
11|    email="manfar123777@gmail.com",
12|    phone="+91 8805472683",
13|    location="Pune, Maharashtra, India",
14|    linkedin="https://www.linkedin.com/in/mandar-farande-4aa289185/",
15|    yearsExperience=15
16|)
17|
18|EXPERIENCES_DATA = [
19|    ExperienceCreate(
20|        title="Nutritional Consultant",
21|        company="Fittr, Pune",
22|        period="Jan 2021 – Jan 2023",
23|        type="Consulting",
24|        description="Developed tailored nutrition and lifestyle plans for diverse client demographics.",
25|        achievements=[
26|            "Developed tailored nutrition and lifestyle plans",
27|            "Guided clients in achieving sustainable fitness goals",
28|            "Conducted online and offline consultations for diverse demographics",
29|            "Achieved 85% client satisfaction rate with measurable health improvements"
30|        ],
31|        displayOrder=1
32|    ),
33|    ExperienceCreate(
34|        title="Nutritional Consultant",
35|        company="Elite Fit Club, Pune",
36|        period="Oct 2018 – Mar 2019",
37|        type="Consulting",
38|        description="Designed customized diet strategies aligned with client fitness objectives.",
39|        achievements=[
40|            "Designed customized diet strategies aligned with client objectives",
41|            "Educated members on nutrition principles for long-term health",
42|            "Improved member retention by 30% through personalized approach",
43|            "Conducted group workshops on healthy eating habits"
44|        ],
45|        displayOrder=2
46|    ),
47|    ExperienceCreate(
48|        title="Personal Trainer",
49|        company="MD Fitness Gym, Pune",
50|        period="Apr 2017 – Apr 2018",
51|        type="Fitness",
52|        description="Delivered comprehensive fitness training programs for individual and group clients.",
53|        achievements=[
54|            "Delivered one-on-one and group training sessions",
55|            "Helped clients improve strength, mobility, and overall wellness",
56|            "Developed injury prevention and rehabilitation programs",
57|            "Maintained 95% client progression rate in fitness goals"
58|        ],
59|        displayOrder=3
60|    ),
61|    ExperienceCreate(
62|        title="Theology Lecturer",
63|        company="Koinonia College of Theology, Pune",
64|        period="Jun 2016 – Mar 2019",
65|        type="Education",
66|        description="Academic instruction and student mentorship in theological studies.",
67|        achievements=[
68|            "Taught English and Theological subjects to undergraduate and postgraduate students",
69|            "Mentored and guided students in academic and personal development",
70|            "Developed innovative curriculum for modern theological education",
71|            "Achieved consistently high student evaluation scores"
72|        ],
73|        displayOrder=4
74|    ),
75|    ExperienceCreate(
76|        title="Customer Relations Advisor",
77|        company="Tech Mahindra Business Services, Pune",
78|        period="Dec 2010 – Aug 2016",
79|        type="Customer Service",
80|        description="Global customer support and relationship management across multiple processes.",
81|        achievements=[
82|            "Provided top-quality customer support across global processes",
83|            "Improved customer satisfaction by resolving complex queries effectively",
84|            "Recognized for teamwork, communication, and problem-solving",
85|            "Consistently exceeded KPIs with 98% resolution rate",
86|            "Trained and mentored new team members"
87|        ],
88|        displayOrder=5
89|    ),
90|    ExperienceCreate(
91|        title="Customer Relations Advisor",
92|        company="EXL Service.com, Pune",
93|        period="May 2004 – Aug 2005",
94|        type="Customer Service",
95|        description="Insurance process management with focus on accuracy and compliance.",
96|        achievements=[
97|            "Processed insurance-related customer requests with accuracy",
98|            "Ensured high compliance standards in service delivery",
99|            "Maintained 99.5% accuracy rate in claim processing",
100|            "Received recognition for exceptional attention to detail"
101|        ],
102|        displayOrder=6
103|    ),
104|    ExperienceCreate(
105|        title="Hospital Pharmacist",
106|        company="Inlaks & Budhrani Hospital, Pune",
107|        period="Apr 2002 – Oct 2002",
108|        type="Healthcare",
109|        description="Clinical pharmacy practice with focus on patient safety and medication management.",
110|        achievements=[
111|            "Dispensed prescriptions with precision and ensured drug safety",
112|            "Advised patients on OTC medicines for minor health issues",
113|            "Collaborated with medical team on medication therapy management",
114|            "Maintained zero medication error record during tenure"
115|        ],
116|        displayOrder=7
117|    )
118|]
119|
120|PROJECTS_DATA = [
121|    ProjectCreate(
122|        title="Corporate Wellness Program",
123|        category="Health & Fitness",
124|        description="Designed and implemented a comprehensive wellness program for a 500+ employee organization, focusing on nutrition education, fitness training, and stress management.",
125|        technologies=["Nutrition Planning", "Fitness Training", "Workshop Facilitation", "Health Assessment"],
126|        achievements=[
127|            "40% improvement in employee health metrics",
128|            "Reduced sick leave by 25%",
129|            "95% employee participation rate",
130|            "Program adopted company-wide"
131|        ],
132|        duration="6 months",
133|        status=ProjectStatus.COMPLETED,
134|        displayOrder=1
135|    ),
136|    ProjectCreate(
137|        title="Multilingual Customer Support Excellence",
138|        category="Customer Relations",
139|        description="Led a cross-functional team to develop multilingual customer support protocols that improved satisfaction rates across diverse demographic segments.",
140|        technologies=["Process Optimization", "Team Leadership", "Quality Assurance", "Cultural Sensitivity Training"],
141|        achievements=[
142|            "98% customer satisfaction improvement",
143|            "30% reduction in resolution time",
144|            "Trained 50+ customer service representatives",
145|            "Implemented across 5 different markets"
146|        ],
147|        duration="8 months",
148|        status=ProjectStatus.COMPLETED,
149|        displayOrder=2
150|    ),
151|    ProjectCreate(
152|        title="Personalized Nutrition Transformation Program",
153|        category="Nutrition Consulting",
154|        description="Created evidence-based nutrition programs for clients with diverse health goals, from weight management to athletic performance enhancement.",
155|        technologies=["Nutritional Assessment", "Meal Planning", "Progress Tracking", "Lifestyle Coaching"],
156|        achievements=[
157|            "100+ clients successfully coached",
158|            "Average 15kg weight loss achieved",
159|            "85% long-term success rate",
160|            "Featured in local wellness magazine"
161|        ],
162|        duration="Ongoing",
163|        status=ProjectStatus.ACTIVE,
164|        displayOrder=3
165|    ),
166|    ProjectCreate(
167|        title="Modern Theological Education Curriculum",
168|        category="Education",
169|        description="Developed innovative curriculum combining traditional theological studies with contemporary practical applications for modern ministry.",
170|        technologies=["Curriculum Design", "Educational Technology", "Student Assessment", "Research Methodology"],
171|        achievements=[
172|            "Curriculum adopted by 3 institutions",
173|            "90% student satisfaction rating",
174|            "Published educational research papers",
175|            "Improved graduate placement rates by 40%"
176|        ],
177|        duration="2 years",
178|        status=ProjectStatus.COMPLETED,
179|        displayOrder=4
180|    ),
181|    ProjectCreate(
182|        title="Pharmacy Quality Assurance System",
183|        category="Healthcare",
184|        description="Implemented comprehensive quality assurance protocols in hospital pharmacy operations to ensure medication safety and regulatory compliance.",
185|        technologies=["Quality Management", "Regulatory Compliance", "Risk Assessment", "Process Documentation"],
186|        achievements=[
187|            "Zero medication errors achieved",
188|            "100% regulatory compliance maintained",
189|            "Reduced dispensing time by 20%",
190|            "System adopted hospital-wide"
191|        ],
192|        duration="6 months",
193|        status=ProjectStatus.COMPLETED,
194|        displayOrder=5
195|    ),
196|    ProjectCreate(
197|        title="Community Health Education Initiative",
198|        category="Public Health",
199|        description="Organized community outreach programs to educate local populations about preventive healthcare, nutrition, and wellness practices.",
200|        technologies=["Community Outreach", "Health Education", "Workshop Organization", "Public Speaking"],
201|        achievements=[
202|            "Reached 1000+ community members",
203|            "Organized 20+ health awareness workshops",
204|            "Collaborated with 5 local healthcare providers",
205|            "Received community service recognition"
206|        ],
207|        duration="1 year",
208|        status=ProjectStatus.COMPLETED,
209|        displayOrder=6
210|    )
211|]
212|
213|TESTIMONIALS_DATA = [
214|    TestimonialCreate(
215|        name="Dr. Priya Sharma",
216|        position="Medical Director",
217|        company="Wellness Plus Clinic",
218|        text="Mandar is a professional who adapts seamlessly to diverse roles — whether in customer service, fitness, or education — and consistently adds value. His holistic approach to health and wellness is exceptional.",
219|        rating=5,
220|        displayOrder=1
221|    ),
222|    TestimonialCreate(
223|        name="Rajesh Kumar",
224|        position="HR Director",
225|        company="Tech Mahindra",
226|        text="He combines deep pharmaceutical knowledge with practical nutrition expertise, making him uniquely positioned to guide people towards healthier lifestyles. A valuable team member in every sense.",
227|        rating=5,
228|        displayOrder=2
229|    ),
230|    TestimonialCreate(
231|        name="Sarah Johnson",
232|        position="Fitness Client",
233|        company="Personal Training Client",
234|        text="A skilled communicator and mentor, Mandar connects with people at all levels and helps them achieve personal and professional growth. His guidance transformed my fitness journey completely.",
235|        rating=5,
236|        displayOrder=3
237|    ),
238|    TestimonialCreate(
239|        name="Rev. Michael Thompson",
240|        position="Academic Dean",
241|        company="Union Biblical Seminary",
242|        text="His reliability, punctuality, and ability to solve problems under pressure make him an asset to any team. Mandar brings both scholarly depth and practical wisdom to theological education.",
243|        rating=5,
244|        displayOrder=4
245|    )
246|]
247|
248|async def seed_database():
249|    """Seed the database with initial data"""
250|    try:
251|        print("🌱 Starting database seeding...")
252|        
253|        # Seed personal info
254|        personal_info = await PersonalInfoService.create_or_update_personal_info(PERSONAL_INFO_DATA)
255|        print(f"✅ Personal info created: {personal_info.name}")
256|        
257|        # Seed experiences
258|        for exp_data in EXPERIENCES_DATA:
259|            experience = await ExperienceService.create_experience(exp_data)
260|            print(f"✅ Experience created: {experience.title} at {experience.company}")
261|        
262|        # Seed projects
263|        for proj_data in PROJECTS_DATA:
264|            project = await ProjectService.create_project(proj_data)
265|            print(f"✅ Project created: {project.title}")
266|        
267|        # Seed testimonials
268|        for test_data in TESTIMONIALS_DATA:
269|            testimonial = await TestimonialService.create_testimonial(test_data)
270|            print(f"✅ Testimonial created: {testimonial.name}")
271|        
272|        print("🎉 Database seeding completed successfully!")
273|        
274|    except Exception as e:
275|        print(f"❌ Error seeding database: {e}")
276|        raise e

