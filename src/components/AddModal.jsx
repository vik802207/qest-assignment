import React, { useState } from "react";
import axios from "axios";

export default function AddModal({ type, onClose }) {
  const [formData, setFormData] = useState({});
  const apiUrl = `http://127.0.0.1:8000/add/${type}`;

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post(apiUrl, formData);
      alert(`${type} added successfully!`);
      onClose();
    } catch (err) {
      alert("Error: " + err.message);
    }
  };

  const fields = {
    client: ["name", "email", "phone"],
    order: ["client_id", "service", "amount"],
    payment: ["order_id", "amount", "date"],
    course: ["title", "description"],
    class: ["course_id", "instructor", "date"]
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50">
      <div className="bg-white p-6 rounded shadow w-full max-w-md">
        <h2 className="text-xl font-bold mb-4">Add {type}</h2>
        <form className="flex flex-col gap-3" onSubmit={handleSubmit}>
          {fields[type].map((field) => (
            <input
              key={field}
              placeholder={field}
              value={formData[field] || ""}
              onChange={(e) => setFormData({ ...formData, [field]: e.target.value })}
              className="p-2 border rounded"
              required
            />
          ))}
          <div className="flex justify-end gap-2 mt-4">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 bg-gray-300 rounded hover:bg-gray-400"
            >
              Cancel
            </button>
            <button type="submit" className="px-4 py-2 bg-purple-600 text-white rounded hover:bg-purple-700">
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
