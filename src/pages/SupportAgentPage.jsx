import ChatBox from "../components/ChatBox";

const SupportAgentPage = () => {
  return (
    <div>
      <h1 className="text-center text-2xl font-semibold my-4">Support Agent Interface</h1>
      <ChatBox agentType="support" />
    </div>
  );
};

export default SupportAgentPage;
