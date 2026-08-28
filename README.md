# Intelligent Resume Analyzer

A Python-based resume screening system that extracts candidate information, matches resumes against job requirements, calculates match scores, and generates structured analysis reports.

## Features

- Resume text parsing
- PDF resume text extraction
- Candidate name extraction
- Email extraction and normalization
- Skills extraction
- Experience extraction
- Case-insensitive skill matching
- Skill match scoring
- Experience scoring
- Overall candidate match score
- Hiring recommendation
- JSON report generation
- Error handling for invalid input
- Automated unit tests

## Project Structure

```text
Intelligent-Resume-Analyzer_HiDevs/
│
├── data/
│   ├── sample_resume.pdf
│   └── resume_report.json
│
├── src/
│   ├── main.py
│   ├── parser.py
│   ├── pdf_parser.py
│   ├── matcher.py
│   └── report.py
│
├── tests/
│   └── test_system.py
│
├── .gitignore
├── README.md
└── requirements.txt