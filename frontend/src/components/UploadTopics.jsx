import React, { useState } from "react";
import { uploadTopics } from "../api";

const UploadTopics = ({ onUploadComplete }) => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Please select a file!");
    setLoading(true);
    try {
      await uploadTopics(file);
      // call parent callback to proceed to exam
      if (onUploadComplete) onUploadComplete();
    } catch (err) {
      console.error(err);
      alert("Upload failed!");
    }
    setLoading(false);
  };

  return (
    <div>
      <h2>Upload Your Topics</h2>
      <input type="file" accept=".txt" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Uploading..." : "Upload & Generate MCQs"}
      </button>
    </div>
  );
};

export default UploadTopics;
