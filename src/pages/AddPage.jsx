import React, { useState } from "react";
import AddModal from "../components/AddModal";

const forms = ["client", "order", "payment", "course", "class"];

export default function AddPage() {
  const [openModal, setOpenModal] = useState("");

  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-2xl font-bold mb-4 text-purple-700">Add Data</h1>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
        {forms.map((item) => (
          <button
            key={item}
            onClick={() => setOpenModal(item)}
            className="bg-purple-500 hover:bg-purple-600 text-white py-2 px-4 rounded shadow"
          >
            Add {item.charAt(0).toUpperCase() + item.slice(1)}
          </button>
        ))}
      </div>

      {openModal && (
        <AddModal type={openModal} onClose={() => setOpenModal("")} />
      )}
    </div>
  );
}
