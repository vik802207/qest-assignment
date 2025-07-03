import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import SupportQueryForm from "./components/SupportQueryForm";
import DashboardQueryForm from "./components/DashboardQueryForm";
import AddPage from "./pages/AddPage";

function App() {
  const [active, setActive] = useState("support");

  return (
    <Router>
      <div className="min-h-screen bg-gray-50 p-6">
        <div className="flex justify-between items-center mb-6">
          <div className="flex gap-3">
            <button
              className={`px-4 py-2 rounded ${active === "support" ? "bg-blue-600 text-white" : "bg-white border"}`}
              onClick={() => setActive("support")}
            >
              Support Agent
            </button>
            <button
              className={`px-4 py-2 rounded ${active === "dashboard" ? "bg-green-600 text-white" : "bg-white border"}`}
              onClick={() => setActive("dashboard")}
            >
              Dashboard Agent
            </button>
          </div>
          <Link
            to="/add"
            className="bg-purple-600 text-white px-4 py-2 rounded hover:bg-purple-700"
          >
            ➕ Add Data
          </Link>
        </div>

        <Routes>
          <Route
            path="/"
            element={active === "support" ? <SupportQueryForm /> : <DashboardQueryForm />}
          />
          <Route path="/add" element={<AddPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
