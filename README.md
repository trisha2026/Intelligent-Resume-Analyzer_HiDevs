# Intelligent Resume Analyzer

A Python-based resume screening system that parses resume text, extracts candidate information, matches candidate skills with job requirements, calculates a match score, and generates a hiring recommendation.

## Features

- Resume parsing
- Extracts candidate name, email, skills, and experience
- Case-insensitive skill matching
- Skill match scoring
- Experience-based scoring
- Overall candidate match score from 0–100
- Hiring recommendations
- JSON report generation
- Save and load reports
- Error handling for invalid or empty resumes
- Automated unit testing

## Project Structure

```text
Intelligent-Resume-Analyzer_HiDevs/
│
├── data/
│   └── resume_report.json
│
├── src/
│   ├── main.py
│   ├── parser.py
│   ├── matcher.py
│   └── report.py
│
├── tests/
│   └── test_system.py
│
├── .gitignore
├── README.md
└── requirements.txt