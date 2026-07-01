🚀 Redrob AI Candidate Ranker

A semantic AI-powered hiring system that ranks candidates using embeddings, career signals, and retrieval-based scoring — going beyond traditional keyword-based ATS systems.

🧠 Overview

Traditional resume screening systems rely heavily on keyword matching, which often fails to capture real candidate capability.

This project builds a hybrid AI ranking engine that evaluates candidates based on:

Semantic similarity (meaning, not keywords)
Career progression signals
Technical depth and specialization
Production AI/ML experience
Retrieval & ranking system expertise
Leadership and ownership indicators
Behavioral hiring signals

👉 The goal is to rank candidates based on real-world impact and experience, not just resume keywords.


⚡ How It Works
Parse Data
Load and structure candidate profiles
Extract job description requirements
Feature Engineering
Experience, skills, career history
Behavioral and hiring signals
Semantic Matching
Use Sentence Transformers to understand meaning
Specialized Detectors
Production AI experience
Retrieval / ranking systems
Leadership & ownership signals
Company type analysis
Hybrid Scoring Engine
Combine semantic + rule-based + behavioral signals
Final Ranking
Generate ranked list of candidates

Candidate Dataset
        │
        ▼
Data Loader & Parsing
        │
        ▼
Feature Engineering
        │
        ▼
Job Description Analyzer
        │
        ▼
Semantic Embedding Model
        │
        ▼
Specialized Signal Detectors
   ├── Leadership Detector
   ├── Production AI Detector
   ├── Retrieval System Detector
   └── Company Analyzer
        │
        ▼
Hybrid Scoring Engine
        │
        ▼
Final Candidate Ranking


redrob-ai-ranker/

├── data/
│   ├── sample_candidates.json
│   ├── candidate_schema.json
│   ├── job_description.docx
│   └── sample_submission.csv
│
├── src/
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── jd_parser.py
│   ├── jd_analyzer.py
│   ├── embedder.py
│   ├── scorer.py
│   ├── ranker.py
│   ├── profile_builder.py
│   ├── company_analyzer.py
│   ├── production_detector.py
│   ├── retrieval_detector.py
│   ├── leadership_detector.py
│   └── explore_data.py
│
├── requirements.txt
└── README.md


✨ Key Features
🧠 Semantic Understanding
Uses sentence-transformers (all-MiniLM-L6-v2)
Matches candidates to job descriptions based on meaning
📊 Feature Engineering

Extracts:

Experience level
Skills & technologies
Career progression
GitHub & behavioral signals
Hiring readiness indicators
🏢 Company Intelligence
Product vs service company detection
Consulting vs engineering experience classification
⚙️ AI/ML Production Detection
Identifies real-world ML system experience
Filters academic-only profiles
🔍 Retrieval System Expertise

Detects experience in:

Search systems
Recommendation engines
Ranking pipelines
Vector databases & embeddings
👥 Leadership Detection

Identifies:

Ownership of systems
Mentoring experience
Architecture design roles


| Signal               | Description                             |
| -------------------- | --------------------------------------- |
| Semantic Similarity  | Resume ↔ Job Description meaning match  |
| Skills Match         | Required technical skills alignment     |
| Experience Score     | Total and relevant experience           |
| Production AI Signal | Real-world ML system experience         |
| Retrieval Expertise  | Search & ranking systems experience     |
| Leadership Signal    | Ownership & mentoring roles             |
| Behavioral Signals   | GitHub, responsiveness, profile quality |
| Hiring Readiness     | Notice period, availability             |


🛠️ Tech Stack
Python 
Sentence Transformers (Hugging Face)
NLP & Feature Engineering
JSON / Data Processing
Modular ML Pipeline Design


🚀 Getting Started
1. Clone Repository
git clone https://github.com/YOUR_USERNAME/redrob-ai-ranker.git
cd redrob-ai-ranker

2. Create Virtual Environment
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt


4. Add Dataset

Place dataset files inside:

data/

Note: Large dataset files are excluded due to GitHub size limits.


5. Run Pipeline
python src/explore_data.py
python src/feature_engineering.py
python src/jd_parser.py
python src/scorer.py
python src/ranker.py


📈 Results (Example Output)
Top Ranked Candidates:

1. Candidate_1023 → Score: 0.91
2. Candidate_889  → Score: 0.87
3. Candidate_445  → Score: 0.84
4. Candidate_778  → Score: 0.81
5. Candidate_301  → Score: 0.79


🔮 Future Improvements
Learning-to-Rank (LTR) models
LLM-based candidate reasoning
FastAPI deployment
Web dashboard for recruiters
Vector database integration (FAISS / Pinecone)
Explainable AI ranking reports
Dockerized production pipeline

🏆 Challenge Context

Built for the Redrob AI Intelligent Candidate Discovery & Ranking Challenge.

This system is designed to improve hiring decisions by focusing on:

Real experience
System design capability
Semantic understanding
Production readiness


👨‍💻 Author

Benny

B.Tech Computer Science Student
Aspiring Software Developer & AI Engineer

Focused on:

Machine Learning
NLP Systems
Retrieval-Augmented Intelligence
Real-world AI applications