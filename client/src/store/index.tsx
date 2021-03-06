import {configureStore} from '@reduxjs/toolkit';
import {siteSlice} from '@/store/siteSlice';
import {uiSlice} from '@/store/uiSlice';

export const store = configureStore({
  reducer: {
    site: siteSlice.reducer,
    ui: uiSlice.reducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
