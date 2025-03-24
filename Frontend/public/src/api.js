// frontend/src/services/api.js
import axios from "axios";

const API_URL = "http://localhost:8000";

const api = axios.create({
  baseURL: API_URL,
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("");
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default api;
