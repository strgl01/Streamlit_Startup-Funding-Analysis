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
    selection2 = st.sidebar.selectbox('Select Investor',db.investor_list)
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
    sum,max,avg,Total_fund_startup,MOM_count,MOM_total = db.overall_detail()
    c5,c6,c7,c8 = st.columns(4)
    with c5:
        st.metric('Total Investment',sum)
    
    with c6:
        st.metric('Maximum Investment',max)
    
    with c7:
        st.metric('Average Investment',round(avg))

    with c8:
        st.metric('Total Funded Startup',Total_fund_startup)

    selection3 = st.selectbox('Option',['Count','Amount'])

    st.subheader('MOM Investment on basis of ' + selection3)

    if selection3 == 'Count':
        fg5,ax5 = plt.subplots()

        ax5.plot(MOM_count['x-axis'],MOM_count['amount'])
        st.pyplot(fg5)

    if selection3 == 'Amount':
        fg5,ax5 = plt.subplots()

        ax5.plot(MOM_total['x-axis'],MOM_total['amount'])
        st.pyplot(fg5)

    
    st.balloons()




