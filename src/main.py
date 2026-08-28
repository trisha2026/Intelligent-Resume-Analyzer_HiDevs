import json

from src.parser import parse_resume
from src.matcher import calculate_match
from src.report import generate_report
from src.pdf_parser import extract_text_from_pdf


def main():
    print("=== Intelligent Resume Analyzer ===")
    print()
    print("Choose resume input method:")
    print("1. Enter resume text manually")
    print("2. Load resume from PDF")
    print()

    choice = input("Enter choice (1 or 2): ").strip()

    try:
        if choice == "1":
            print("\nEnter resume text.")
            print("Type END on a new line when finished:")

            resume_lines = []

            while True:
                line = input()
                if line.strip() == "END":
                    break
                resume_lines.append(line)

            resume_text = "\n".join(resume_lines)

        elif choice == "2":
            pdf_path = input(
                "\nEnter PDF path "
                "(example: data/sample_resume.pdf): "
            ).strip()

            resume_text = extract_text_from_pdf(pdf_path)

            print("\nPDF text extracted successfully.")

        else:
            print("Error: Invalid choice. Please enter 1 or 2.")
            return

        print("\nEnter required skills (comma-separated):")
        required_skills = input().split(",")

        job_requirements = {
            "skills": [
                skill.strip()
                for skill in required_skills
                if skill.strip()
            ]
        }

        resume = parse_resume(resume_text)

        match_result = calculate_match(
            resume,
            job_requirements
        )

        report = generate_report(
            resume,
            match_result
        )

        print("\nResume Analysis")
        print(json.dumps(report, indent=2))

        with open("data/resume_report.json", "w") as file:
            json.dump(report, file, indent=2)

        print("\nReport saved successfully.")

    except ValueError as error:
        print(f"Error: {error}")

    except FileNotFoundError:
        print("Error: PDF file was not found.")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()