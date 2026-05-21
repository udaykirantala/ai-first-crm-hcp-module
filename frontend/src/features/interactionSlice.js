import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  extractedData: null,
  interactions: [],
};

const interactionSlice = createSlice({
  name: "interaction",

  initialState,

  reducers: {

    setExtractedData: (state, action) => {
      state.extractedData = action.payload;
    },

    setInteractions: (state, action) => {
      state.interactions = action.payload;
    },
    setCurrentInteractionId: (state,action) => {
      state.currentInteractionId =
      action.payload;
    },
  },
});

export const {
  setExtractedData,
  setInteractions,
  setCurrentInteractionId
} = interactionSlice.actions;

export default interactionSlice.reducer;