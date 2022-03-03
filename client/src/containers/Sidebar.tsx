import * as React from 'react';
import {Typography} from '@mui/material';
import {DataMetaInfo} from '@/components/meta/DataMetaInfo';

export interface ISidebarProps {
}

const Sidebar = (props: ISidebarProps) => {
  const demoMetaData = {
    'Instrument': '201283',
    'Sensors': 'Serial K175067, Channel 1',
    'Sampling Period': '10000',
    'Longitude': '122˚13\'5.60"',
    'Latitude': '31˚04\'4.00"',
  };

  return (
    <div>
      <Typography mb={'12px'} variant={'h5'} component={'div'}>
          Dataset Name
      </Typography>
      <DataMetaInfo meta={demoMetaData}></DataMetaInfo>
    </div>
  );
};

export default Sidebar;