import React, { useState } from "react";
import axios from "axios";

export default function SupportQueryForm() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState(null);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setResponse(null);

    try {
      const res = await axios.post("https://qest-assignment.onrender.com/query/support", { query });

      let parsed;
      try {
        parsed = typeof res.data.response === "string"
          ? JSON.parse(res.data.response)
          : res.data.response;
      } catch {
        parsed = res.data.response;
      }

      setResponse(parsed);
    } catch (err) {
      setError("Error: " + err.message);
    }
  };

  const renderCard = (item, index) => (
    <div
      key={index}
      className="border rounded-lg p-4 bg-white shadow-md hover:shadow-lg transition"
    >
      {Object.entries(item).map(([key, value]) => (
        <div key={key} className="text-sm mb-1">
          <span className="font-semibold capitalize">{key}:</span>{" "}
          <span className="text-gray-800">{String(value)}</span>
        </div>
      ))}
    </div>
  );

  return (
    <div className="bg-white shadow p-4 rounded w-full max-w-xl mx-auto mt-6">
      <h2 className="text-lg font-bold mb-2 text-blue-600">Support Agent</h2>

      <form onSubmit={handleSubmit} className="flex flex-col gap-3">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="e.g. Show payment for order #12345"
          className="p-2 border border-gray-300 rounded"
        />
        <button
          type="submit"
          className="bg-blue-500 text-white py-2 rounded hover:bg-blue-600"
        >
          Ask
        </button>
      </form>

      {error && (
        <div className="mt-4 text-red-600 font-semibold">{error}</div>
      )}

      {response && (
        <div className="mt-4">
          <h4 className="font-semibold mb-2">Response:</h4>

          {Array.isArray(response) ? (
            <div className="grid gap-4">
              {response.map((item, i) => renderCard(item, i))}
            </div>
          ) : typeof response === "object" ? (
            renderCard(response)
          ) : (
            <div className="p-3 bg-gray-100 rounded text-sm text-gray-800 whitespace-pre-wrap">
              {String(response)}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
