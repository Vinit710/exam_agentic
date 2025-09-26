import React from "react";

const ResultsDashboard = ({ results }) => {
  if (!results) return null;

  return (
    <div>
      <h2>Results</h2>
      <p><strong>Score:</strong> {results.score}%</p>
      <h3>Feedback:</h3>
      <p>{results.feedback}</p>
      <h3>Details:</h3>
      {results.details.map((item, idx) => (
        <div key={idx} style={{ marginBottom: "10px" }}>
          <p><strong>Q:</strong> {item.question}</p>
          <p><strong>Your Answer:</strong> {item.your_answer}</p>
          <p><strong>Correct Answer:</strong> {item.correct_answer}</p>
          <p>{item.is_correct ? "✅ Correct" : "❌ Incorrect"}</p>
        </div>
      ))}
    </div>
  );
};

export default ResultsDashboard;
