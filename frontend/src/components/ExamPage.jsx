import React, { useState } from "react";
import { submitExam } from "../api";

const ExamPage = ({ questions, onExamFinished }) => {
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);

  const handleChange = (qid, value) => {
    setAnswers({ ...answers, [qid]: value });
  };

  const handleSubmit = async () => {
    const report = await submitExam(answers);
    if (onExamFinished) onExamFinished(report);
    setSubmitted(true);
  };

  if (!questions || questions.length === 0) return <p>No questions available.</p>;
  if (submitted) return <p>Exam submitted! See results below.</p>;

  return (
    <div>
      <h2>Exam</h2>
      {questions.map((mcq) => (
        <div key={mcq.id} style={{ marginBottom: "20px" }}>
          <p>{mcq.id}. {mcq.question}</p>
          {mcq.options.map((opt, idx) => (
            <label key={idx} style={{ display: "block" }}>
              <input
                type="radio"
                name={`q${mcq.id}`}
                value={opt}
                checked={answers[mcq.id] === opt}
                onChange={() => handleChange(mcq.id, opt)}
              />
              {opt}
            </label>
          ))}
        </div>
      ))}
      <button onClick={handleSubmit}>Submit Exam</button>
    </div>
  );
};

export default ExamPage;
