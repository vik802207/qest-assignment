import ChatBox from "../components/ChatBox";

const DashboardAgentPage = () => {
  return (
    <div>
      <h1 className="text-center text-2xl font-semibold my-4">Dashboard Agent Interface</h1>
      <ChatBox agentType="dashboard" />
    </div>
  );
};

export default DashboardAgentPage;
