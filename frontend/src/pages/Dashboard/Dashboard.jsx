import "./Dashboard.css"
import { ChatInterface } from "../../components/ChatInterface/ChatInterface";
import { InteractionForm } from "../../components/InteractionForm/InteractionForm";

const Dashboard = () => {

  return (
    <div className="dashboard-container inter-regular">
      <div className="left-panel">
        <InteractionForm />
      </div>
      <div className="right-panel">
        <ChatInterface />
      </div>

    </div>
  );
};

export default Dashboard;