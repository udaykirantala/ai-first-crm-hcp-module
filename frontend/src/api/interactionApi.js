import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export const chatInteraction = async (message) => {

  const response = await axios.post(
    `${BASE_URL}/interaction/chat`,
    { message }
  );

  return response.data;
};

export const getInteractions = async () => {

  const response = await axios.get(
    `${BASE_URL}/interactions`
  );

  return response.data;
};

export const updateInteraction =
    async (
        interactionId,
        message
    ) => {

    const response =
        await axios.put(

        `${BASE_URL}/interaction/${interactionId}`,

        {
            message
        }

    );

    return response.data;
};