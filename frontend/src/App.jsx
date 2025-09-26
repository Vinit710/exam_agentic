import React, { useState } from "react";
import UploadTopics from "./components/UploadTopics";
import ExamPage from "./components/ExamPage";
import ResultsDashboard from "./components/ResultsDashboard";
import { getMCQs } from "./api";

function App() {
  const [stage, setStage] = useState("upload"); // stages: upload -> loading -> exam -> results
  const [examQuestions, setExamQuestions] = useState([]);
  const [examResults, setExamResults] = useState(null);

  const handleExamReady = async () => {
    setStage("loading");
    try {
      const mcqs = await getMCQs();
      if (mcqs && mcqs.length > 0) {
        setExamQuestions(mcqs);
        setStage("exam");
      } else {
        alert("No questions generated. Please upload topics again.");
        setStage("upload");
      }
    } catch (err) {
      console.error(err);
      alert("Failed to generate MCQs.");
      setStage("upload");
    }
  };

  const handleExamFinished = (results) => {
    setExamResults(results);
    setStage("results");
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <h1 style={{ textAlign: "center" }}>Agentic Exam AI</h1>

      {stage === "upload" && (
        <UploadTopics
          onUploadComplete={handleExamReady}
        />
      )}

      {stage === "loading" && (
        <div style={{ textAlign: "center", marginTop: "2rem" }}>
          <div className="loader" style={{ fontSize: 24, marginBottom: 16 }}>Generating questions, please wait...</div>
          <div style={{ fontSize: 48 }}>⏳</div>
        </div>
      )}

      {stage === "exam" && (
        <ExamPage
          questions={examQuestions}
          onExamFinished={handleExamFinished}
        />
      )}

      {stage === "results" && <ResultsDashboard results={examResults} />}
    </div>
  );
}

export default App;
