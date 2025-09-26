
# Exam Agentic

An AI-powered exam generator and grader. Upload your topics, generate MCQs using LLMs, take the exam, and get instant feedback and results.

## Features
- Upload a list of topics (as a .txt file)
- Automatic MCQ generation using LLM (Gemini API)
- Take the generated exam in the browser
- Instant grading and feedback
- Results dashboard with score and detailed answers

## Project Structure

- `backend/` — FastAPI server, LLM integration, MCQ generation, grading
- `frontend/` — React app for uploading topics, taking exams, and viewing results

## Setup & Running Instructions

### 1. Backend (FastAPI)

1. Go to the backend directory:
	```sh
	cd backend
	```
2. (Recommended) Create a virtual environment:
	```sh
	python -m venv venv
	venv\Scripts\activate  # On Windows
	# or
	source venv/bin/activate  # On Mac/Linux
	```
3. Install dependencies:
	```sh
	pip install fastapi uvicorn requests python-dotenv
	```
4. Create a `.env` file in the backend directory and add your Gemini API key:
	```env
	API_KEY=your_gemini_api_key_here
	```
5. Start the backend server:
	```sh
	uvicorn main:app --reload
	```

### 2. Frontend (React)

1. Go to the frontend directory:
	```sh
	cd frontend
	```
2. Install dependencies:
	```sh
	npm install
	```
3. Start the React app:
	```sh
	npm start
	```
4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Usage
1. Upload a `.txt` file with your exam topics (one topic per line).
2. Wait for MCQs to be generated (loading indicator will show).
3. Take the exam and submit your answers.
4. View your score, feedback, and detailed results.

## Notes
- The `.env` file is required for backend LLM access and is excluded from version control.
- Make sure the backend is running on port 8000 and frontend on 3000 (default settings).

---
Made with ❤️ for learning and experimentation!