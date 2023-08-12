import streamlit as st
import numpy as np
import pandas as pd
import data as db
import matplotlib.pyplot as plt


st.set_page_config(layout='wide',page_title='Startup Analysis')
st.sidebar.title('Stratup Funding Analysis')
selection = st.sidebar.selectbox('Select one',['Overall Analysis','Startup','Investor'])
if selection == 'Startup':
    st.title('Startup')
    selection1 = st.sidebar.selectbox('Select Startup',db.startup_list)
    btn1 = st.sidebar.button('Find Startup Details')
    if btn1:
        st.title(selection1)
        st.dataframe(db.investor_detail(selection1))
        st.balloons()
        #print(db.investor_detail(selection2))
    st.balloons()
if selection == 'Investor':
    st.title('Investor')
    selection2 = st.sidebar.selectbox('Select Startup',db.investor_list)
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        st.title(selection2)
        (df1,df2,df3,df4,df5,df6) = db.investor_detail(selection2)
        st.subheader('Recent Investment')
        st.dataframe(df1)
        c1,c2 = st.columns(2)

        with c1:
            st.subheader('Biggest Investments')
            fg,ax = plt.subplots()

            ax.bar(df2.index,df2.values)
            st.pyplot(fg)
        
        with c2:
            st.subheader('Sector Investments')
            fg1,ax1 = plt.subplots()

            ax1.pie(df3, labels=df3.index)
            st.pyplot(fg1)

        c3,c4 = st.columns(2)

        with c3:
            st.subheader('Stage Investments')
            fg2,ax2 = plt.subplots()

            ax2.pie(df4,labels = df4.index)
            st.pyplot(fg2)

        with c4:
            st.subheader('City Investments')
            fg3,ax3 = plt.subplots()

            ax3.pie(df5,labels = df5.index)
            st.pyplot(fg3)

        st.subheader('YOY Investment')
        fg4,ax4 = plt.subplots()

        ax4.plot(df6.index,df6.values)
        st.pyplot(fg4)

        st.balloons()
        #print(db.investor_detail(selection2))


    
else:
    st.title('Overall Analysis')
    st.balloons()




