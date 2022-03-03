import React from 'react';
import '@/styles/index.scss';
import Map from '@/components/Map';
import {AppBar, Box, Grid, ThemeProvider, Toolbar} from '@mui/material';
import Sidebar from '@/containers/Sidebar';
import SKToolbar from '@/containers/Toolbar';
import {Visualizer} from '@/containers/Visualizer';
import config from '@/config';

function App() {
  return (
    <ThemeProvider theme={config.theme}>
      <Box className={'app'}>
        <AppBar position='fixed'>
          <SKToolbar></SKToolbar>
        </AppBar>
        <Grid container spacing={0} sx={{height: '100vh', paddingTop: '64px'}}>
          <Grid item xs={3} sx={{height: '100%', padding: '12px', overflowY: 'auto'}}>
            <Sidebar></Sidebar>
          </Grid>
          <Grid item xs={9} sx={{height: '100%'}}>
            <Map></Map>
            <Grid item xs={9} alignItems={'stretch'} className={'vis-container'}>
              {/* Float Layer Component */}
              <Visualizer></Visualizer>
            </Grid>
          </Grid>
        </Grid>
      </Box>
    </ThemeProvider>
  );
}

export default App;
