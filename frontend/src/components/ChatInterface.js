import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Box, Paper } from '@mui/material';
import MessageHistory from './MessageHistory';
import QueryInput from './QueryInput';

const ChatInterface = () => {
  const messages = useSelector(state => state.chat.messages);
  const dispatch = useDispatch();

  return (
    <Box sx={{ maxWidth: 800, margin: '0 auto', p: 2 }}>
      <Paper elevation={3} sx={{ p: 2, height: '80vh', display: 'flex', flexDirection: 'column' }}>
        <MessageHistory messages={messages} />
        <QueryInput />
      </Paper>
    </Box>
  );
};

export default ChatInterface;