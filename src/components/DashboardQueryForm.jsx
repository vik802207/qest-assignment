import React, { useState } from "react";

const DashboardQueryForm = () => {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!query.trim()) return;
    setLoading(true);
    setResponse("");

    try {
      const res = await fetch("https://qest-assignment.onrender.com/query/dashboard", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ query })
      });

      const data = await res.json();
      setResponse(data.response || "No response.");
    } catch (error) {
      console.error("Error:", error);
      setResponse("Error occurred.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-xl mx-auto mt-10 p-6 bg-white rounded-xl shadow-lg">
      <h1 className="text-2xl font-bold mb-4">📊 Ask Dashboard Agent</h1>

      <textarea
        className="w-full p-3 border rounded-lg mb-4"
        rows={3}
        placeholder="e.g. How much revenue this month?"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button
        onClick={handleAsk}
        disabled={loading}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        {loading ? "Asking..." : "Ask Agent"}
      </button>

      {response && (
        <div className="mt-6 p-4 border bg-gray-50 rounded">
          <strong>🧠 Response:</strong>
          <p className="mt-2 text-lg">{response}</p>
        </div>
      )}
    </div>
  );
};

export default DashboardQueryForm;
