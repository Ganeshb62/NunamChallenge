import pandas as pd
import numpy as np

def downsample_detail():
    #downsampling "detail.csv"
    df_detailmin = pd.read_csv('detail.csv')
    df_detailmin['Absolute Time'] = pd.to_datetime(df_detailmin['Absolute Time'])   #set column to datetime type
    df_detailmin = df_detailmin.set_index('Absolute Time').resample('60S').\
        agg({'Record Index':'last','Status':'last','JumpTo':'last','Cycle':'last','Step':'last',\
            'Cur(mA)':np.mean,'Voltage(V)':np.mean,'CapaCity(mAh)':np.mean,\
                'Energy(mWh)':np.mean,'Relative Time(h:min:s.ms)':'last'})   #Resampling data

    df_detailmin.to_csv('detailDownsampled.csv', index=True, header=True)   #create a downsampled csv for 'detail.csv'

def downsample_detail_vol():
    #downsampling "detailVol.csv"
    df_detvolmin = pd.read_csv('detailVol.csv')
    df_detvolmin['Realtime'] = pd.to_datetime(df_detvolmin['Realtime'])     #set column to datetime type
    df_detvolmin = df_detvolmin.set_index('Realtime').resample('60S').\
        agg({'Record ID':'last','Step Name':'last','Relative Time(h:min:s.ms)':'last',\
            'Auxiliary channel TU1 U(V)':np.mean, 'Gap of Voltage':np.mean,})   #Resampling data

    df_detvolmin.to_csv('detailVolDownsampled.csv', index=True, header=True)    #create a downsampled csv for 'detailVol.csv'

def downsample_detail_temp():
    #downsampling "detailTemp.csv"
    df_dettempmin = pd.read_csv('detailTemp.csv')
    df_dettempmin['Realtime'] = pd.to_datetime(df_dettempmin['Realtime'])     #set column to datetime type
    df_dettempmin = df_dettempmin.set_index('Realtime').resample('60S').\
        agg({'Record ID':'last','Step Name':'last','Relative Time(h:min:s.ms)':'last',\
            'Auxiliary channel TU1 T(°C)':np.mean, 'Gap of Temperature':np.mean,})   #Resampling data

    df_dettempmin.to_csv('detailTempDownsampled.csv', index=True, header=True)    #create a downsampled csv for 'detailTemp.csv'

# NOTE: used np.mean to resample as a collection of 60 entries had minimu or no difference, so mean gives the same value after resampling for 60S
# NOTE: used last to resample in few comlumns as these had some states as data, so last gives the latest state at any time doesn't change after resampling 


downsample_detail()
downsample_detail_vol()
downsample_detail_temp()