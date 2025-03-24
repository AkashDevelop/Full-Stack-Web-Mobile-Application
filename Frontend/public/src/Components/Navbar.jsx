// frontend/src/components/Navbar.jsx
import React from "react";
import { Link, useNavigate } from "react-router-dom";

export default function Navbar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    navigate("/login");
  };

  return (
    <nav className="bg-gray-800 text-white p-4 flex justify-between items-center">
      <div>
        <Link to="/dashboard" className="mr-4">Dashboard</Link>
        <Link to="/login" className="mr-4">Login</Link>
        <Link to="/register" className="mr-4">Register</Link>
      </div>
      <button onClick={handleLogout} className="bg-red-500 p-2 rounded">
        Logout
      </button>
    </nav>
  );
}
