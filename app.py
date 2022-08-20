# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)




def main():
    st.title("hello world")
    path = 'AirPassengers.csv'

    df = pd.read_csv(path)   
    df.columns = ['Date','Number of Passengers']
    df['Date']=pd.to_datetime(df['Date'])
    df['Year']=df['Date'].apply(lambda x: x.year)
    year=st.selectbox('Select',df['Year'].unique())
    button=st.button('show result')
    if button:
        subset=df[df['Year']==year]
        st.table(subset)
        
    
        
    
if __name__ == '__main__':
    main()