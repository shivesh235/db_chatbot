import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { chatApi } from '../services/api';

export const sendMessage = createAsyncThunk(
  'chat/sendMessage',
  async (message) => {
    const response = await chatApi.sendMessage(message);
    return response.data;
  }
);

const chatSlice = createSlice({
  name: 'chat',
  initialState: {
    messages: [],
    loading: false,
    error: null
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(sendMessage.pending, (state) => {
        state.loading = true;
      })
      .addCase(sendMessage.fulfilled, (state, action) => {
        state.messages.push(
          { text: action.meta.arg, isUser: true },
          { text: action.payload.response, isUser: false }
        );
        state.loading = false;
      })
      .addCase(sendMessage.rejected, (state, action) => {
        state.error = action.error.message;
        state.loading = false;
      });
  }
});

export default chatSlice.reducer;