// frontend/src/components/Dashboard.jsx
import React, { useEffect, useState } from "react";
import api from "../services/api";
import { Line } from "react-chartjs-2";

export default function Dashboard() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    async function fetchReviews() {
      try {
        const res = await api.get("/reviews");
        setReviews(res.data);
      } catch (error) {
        console.error("Failed to fetch reviews:", error);
      }
    }
    fetchReviews();
  }, []);

  const chartData = {
    labels: reviews.map((r) => new Date(r.timestamp).toLocaleDateString()),
    datasets: [
      {
        label: "Sentiment Confidence",
        data: reviews.map((r) => r.confidence),
        backgroundColor: "rgba(75,192,192,0.4)",
      },
    ],
  };

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">Dashboard</h2>
      <div className="mb-6">
        <Line data={chartData} />
      </div>
      <h3 className="text-xl mb-2">Recent Reviews</h3>
      <ul>
        {reviews.map((review, index) => (
          <li key={index} className="mb-2 border-b pb-2">
            <p>{review.review_text}</p>
            <small>
              {review.sentiment} ({Math.round(review.confidence * 100)}% confidence)
            </small>
          </li>
        ))}
      </ul>
    </div>
  );
}
