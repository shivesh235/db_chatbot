import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { TextField, IconButton, Box } from '@mui/material';
import { Send } from '@mui/icons-material';
import { sendMessage } from '../store/chatSlice';

const QueryInput = () => {
  const [query, setQuery] = useState('');
  const dispatch = useDispatch();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim()) {
      dispatch(sendMessage(query));
      setQuery('');
    }
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ display: 'flex', gap: 1 }}>
      <TextField
        fullWidth
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Type your question..."
        variant="outlined"
        size="small"
      />
      <IconButton type="submit" color="primary">
        <Send />
      </IconButton>
    </Box>
  );
};

export default QueryInput;