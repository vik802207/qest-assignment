import { useState } from "react";
import axios from "axios";

const ChatBox = ({ agentType }) => {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async () => {
    const res = await axios.post(`http://127.0.0.1:8000/agent-query`, {
      agent: agentType,
      message: query,
    });
    setResponse(res.data.answer);
  };

  return (
    <div className="p-4 max-w-lg mx-auto">
      <h2 className="text-xl font-bold">{agentType} Query</h2>
      <textarea
        className="w-full border p-2 mt-2"
        rows={3}
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask your question..."
      />
      <button onClick={handleSubmit} className="mt-2 px-4 py-2 bg-blue-600 text-white">
        Submit
      </button>
      {response && <p className="mt-4 bg-gray-100 p-3">{response}</p>}
    </div>
  );
};

export default ChatBox;
