import React, { useState } from "react";
import api from "../services/api";

export default function ReviewForm({ onReviewSubmitted }) {
  const [reviewText, setReviewText] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post("/reviews", { review_text: reviewText });
      onReviewSubmitted(response.data); 
      setReviewText("");
    } catch (error) {
      console.error("Error submitting review:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 p-4">
      <textarea
        value={reviewText}
        onChange={(e) => setReviewText(e.target.value)}
        placeholder="Write your review..."
        className="w-full p-2 border"
        required
      ></textarea>
      <button type="submit" className="bg-green-500 text-white p-2">
        Analyze Sentiment
      </button>
    </form>
  );
}
