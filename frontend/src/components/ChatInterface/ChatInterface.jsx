import { useState } from "react";

import {
  useDispatch,
  useSelector
} from "react-redux";

import "./ChatInterface.css"

import {
  setCurrentInteractionId,
  setExtractedData
} from "../../features/interactionSlice";

import {
  chatInteraction,
  updateInteraction
} from "../../api/interactionApi";

export const ChatInterface = () => {

  const [message, setMessage] = useState("");

  const [chatMessages, setChatMessages] = useState([]);

  const dispatch = useDispatch();

  const currentInteractionId =
    useSelector(

      (state) =>
        state.interaction
          .currentInteractionId

    );

  const handleSend = async () => {

    if (!message) return;

    const userMessage = {
      type: "user",
      text: message,
    };

    setChatMessages((prev) => [
      ...prev,
      userMessage,
    ]);

    try {

      const isEditMessage =

        message.toLowerCase()
          .includes("change")

        ||

        message.toLowerCase()
          .includes("update");


      let response;


      if (
        isEditMessage &&
        currentInteractionId
      ) {

        response =
          await updateInteraction(

            currentInteractionId,
            message

          );

      } else {

        response =
          await chatInteraction(
            message
          );

      }


      dispatch(
        setExtractedData(
          response.extracted_data
        )
      );

      dispatch(
        setCurrentInteractionId(
          response.logged_response
            .interaction_id
        )
      );


      const botMessage = {
        type: "bot",
        text: response.summary,
      };

      setChatMessages((prev) => [
        ...prev,
        botMessage,
      ]);

      setMessage("");

    } catch (error) {

      console.log(error);

    }
  };

  return (

    <div className="chat-container">

      <div className="chat-header">

        <p className="ai-heding-text aitext">
          🤖 AI Assistant
        </p>

        <p className="ai-heding-text aidis">
          Log interaction details via chat
        </p>

      </div>


      <div className="chat-body">

        <div className="info-box">

          Log interaction details here
          (e.g. Met Dr. Sharma,
          discussed diabetes medicine,
          positive sentiment).

        </div>


        {chatMessages.map((msg, index) => (

          <div
            key={index}
            className={
              msg.type === "user"
                ? "user-message"
                : "bot-message"
            }
          >

            {msg.text}

          </div>

        ))}

      </div>


      <div className="chat-input-area">

        <input
          type="text"
          placeholder="Describe Interaction..."
          value={message}
          onChange={(e) =>
            setMessage(e.target.value)
          }
        />

        <button onClick={handleSend}>
          AI Log
        </button>

      </div>

    </div>

  );
};