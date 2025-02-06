import React from 'react';
import { Box, Typography } from '@mui/material';

const MessageHistory = ({ messages }) => {
  return (
    <Box sx={{ flexGrow: 1, overflow: 'auto', mb: 2 }}>
      {messages.map((message, index) => (
        <Box
          key={index}
          sx={{
            p: 1,
            mb: 1,
            bgcolor: message.isUser ? 'primary.light' : 'grey.100',
            borderRadius: 1,
            maxWidth: '80%',
            ml: message.isUser ? 'auto' : 0
          }}
        >
          <Typography>{message.text}</Typography>
        </Box>
      ))}
    </Box>
  );
};

export default MessageHistory;