import pandas as pd
import numpy as np

def down_sample_data():
    """ This function reads 3 csv files and reduce the sampling rate from
    1 sample/second to 1 sample/minute and create 3 corresponding downsampled file """

    #downsampling can be done with a function taking filename as arguements
    #but the all csv files doesn't have same columns, so I performed downsampling separately

    #downsampling "detail.csv"
    df_detailmin = pd.read_csv('detail.csv')
    df_detailmin['Absolute Time'] = pd.to_datetime(df_detailmin['Absolute Time'])   #set column to datetime type
    df_detailmin = df_detailmin.set_index('Absolute Time').resample('60S').\
        agg({'Record Index':'last','Status':'last','JumpTo':'last','Cycle':'last','Step':'last',\
            'Cur(mA)':np.mean,'Voltage(V)':np.mean,'CapaCity(mAh)':np.mean,\
                'Energy(mWh)':np.mean,'Relative Time(h:min:s.ms)':'last'})   #Resampling data

    df_detailmin.to_csv('detailDownsampled.csv', index=True, header=True)   #create a downsampled csv for 'detail.csv'

    #downsampling "detailVol.csv"
    df_detvolmin = pd.read_csv('detailVol.csv')
    df_detvolmin['Realtime'] = pd.to_datetime(df_detvolmin['Realtime'])     #set column to datetime type
    df_detvolmin = df_detvolmin.set_index('Realtime').resample('60S').\
        agg({'Record ID':'last','Step Name':'last','Relative Time(h:min:s.ms)':'last',\
            'Auxiliary channel TU1 U(V)':np.mean, 'Gap of Voltage':np.mean,})   #Resampling data

    df_detvolmin.to_csv('detailVolDownsampled.csv', index=True, header=True)    #create a downsampled csv for 'detailVol.csv'

    #downsampling "detailTemp.csv"
    df_dettempmin = pd.read_csv('detailTemp.csv')
    df_dettempmin['Realtime'] = pd.to_datetime(df_dettempmin['Realtime'])     #set column to datetime type
    df_dettempmin = df_dettempmin.set_index('Realtime').resample('60S').\
        agg({'Record ID':'last','Step Name':'last','Relative Time(h:min:s.ms)':'last',\
            'Auxiliary channel TU1 T(°C)':np.mean, 'Gap of Temperature':np.mean,})   #Resampling data

    df_dettempmin.to_csv('detailTempDownsampled.csv', index=True, header=True)    #create a downsampled csv for 'detailTemp.csv'

down_sample_data()