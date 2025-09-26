import axios from "axios";

const API_BASE = "http://localhost:8000";

export const uploadTopics = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  const res = await axios.post(`${API_BASE}/upload-topics`, formData);
  return res.data;
};

export const getMCQs = async () => {
  const res = await axios.get(`${API_BASE}/generate-mcqs`);
  return res.data.mcqs;
};

export const submitExam = async (answers) => {
  // Convert answers to FormData
  const formData = new FormData();
  Object.keys(answers).forEach((key) => formData.append(key, answers[key]));
  const res = await axios.post(`${API_BASE}/submit-exam`, formData);
  return res.data.report;
};
