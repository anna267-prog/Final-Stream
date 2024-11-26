import streamlit as st

#Introduction of "History Helper"
st.title(''':blue[ **Welcome to History Helper: Philadelphia!**]''')
st.subheader(''':blue[This app seeks to provide visitors  to Philadelphia historical sites, like you, with additional archival information that is not available at the sites themselves. History on!]''')

st.markdown("The first section of this app will request some simple demographic information to inform the City of Philadelphia and the Philadelphia Historical Commission's efforts and recognize their historical sites's vastly diverse audiences. Following this section, you will have the opportunity to learn about the historical site you are currently visiting from academic and archival sources! Lastly, your personal preferences and proximity will help us recommend to you your next historical site! Enjoy!")

#Demographic Section
st.markdown('Demographic Details')
name = st.text_input('What is your name?')
age = st.text_input('How old are you?')
philly_visitor = st.text_input('Have you visited Philadelphia before? (Yes or No)')
casecheck = philly_visitor.capitalize()
if casecheck == 'Yes': 
    site_visitor = st.text_input('Have you visited this site before? (Yes or No)')

#Archival History Data
import pandas as pd
st.markdown('Historical Archive')
site = st.selectbox("Which of the following sites are you currently visiting?", ("Elfreth's Alley","Independence Hall","Liberty Bell Center"), index=None, placeholder="Select location...",)

df_excel = pd.read_excel('/Users/annalev/Desktop/pf/week12/data_archival_history-programming2.xlsx', index_col ='Location.Name')

if site in df_excel.index:
    st.markdown(f'Historical Details for {site}:') #Labels outcoming information
    site_info = df_excel.loc[site] #defines and retrieves information from dataframe
    st.table(site_info) #displays table on streamlit
elif site == None:
    st.write('')
else:
    st.write('Selected site not currently available on History Helper: Philadelphia')