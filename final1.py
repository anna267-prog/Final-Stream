import streamlit as st

#Introduction of "History Helper"
st.title(''':blue[ **Welcome to History Helper: Philadelphia!**]''')
st.subheader(''':blue[This app seeks to provide visitors  to Philadelphia historical sites, like you, with additional archival information that is not available at the sites themselves. History on!]''')

st.markdown("The first section of this app will request some simple demographic information to inform the City of Philadelphia and the Philadelphia Historical Commission's efforts and recognize their historical sites's vastly diverse audiences. Following this section, you will have the opportunity to learn about the historical site you are currently visiting from academic and archival sources! Lastly, your personal preferences and proximity will help us recommend to you your next historical site! Enjoy!")

#Demographic Section
st.markdown(''':blue[Demographic Details]''')
name = st.text_input('What is your name?')
age = st.text_input('How old are you?')
philly_visitor = st.selectbox("Have you visited Philadelphia before?", ("Yes","No"), index=None, placeholder="Select option...",)

#Site visit with default value 
site_visitor = None
if philly_visitor == 'Yes': 
    site_visitor = st.selectbox("Have you visited this site before?", ("Yes","No"), index=None, placeholder="Select option...",) #Prompts question about repeated site visit if they have visited Philly before  

#Archival History Data
import pandas as pd
st.markdown(''':blue[Historical Archive]''')
site = st.selectbox("Which of the following sites are you currently visiting?", ("Elfreth's Alley","Independence Hall","Liberty Bell Center"), index=None, placeholder="Select location...",)

#Create dictionary of demographic info
dem_data = {
    'Name': [name],
    'Age': [age],
    'Previous Philly Visit': [philly_visitor],
    'Previous Site Visit': [site_visitor] if [site_visitor] else 'No',
    'Site Visiting': [site]
}

#Convert dictionary to dataframe
demographics = pd.DataFrame(dem_data)

#Output dataframe to csv file 
demographics.to_csv('demographics.csv', index=False)

#Produce Information Table for Users
df_excel = pd.read_excel('/Users/annalev/Desktop/pf/week12/data_archival_history-programming2.xlsx', index_col ='Location.Name')

if site in df_excel.index:
    st.markdown(f'Historical Details for {site}:') #Labels outcoming information
    site_info = df_excel.loc[site] #defines and retrieves information from dataframe
    st.table(site_info) #displays table on streamlit
elif site == None:
    st.write('') #prevents message output when site not selected
else:
    st.write('Selected site not currently available on History Helper: Philadelphia')

#Inquire about second site visit 
st.markdown(''':blue[Next Stop]''')
nextstop_interest = st.selectbox("Are you interested in visiting another historical site?", ("Yes","No"), index=None, placeholder="Select option...")

time_frame = None
distance_frame = None
if nextstop_interest == "Yes":
    time_frame = st.selectbox("How long would you like to spend at this new site?", ("< 10 min", "10-30 min", "30-60 min", "60-90 min", "90-120 min", "> 120 min"), index=None, placeholder="Select a time...")
    distance_frame = st.selectbox("For how long are you willing to travel to your next site?", ("< 10 min", "10-20 min", "20-30 min", "30-40 min", "40-50 min", "50-60+ min"), index=None, placeholder="Select a time...")
    #OpenAI to provide suggestions for new site to visit based on time and distance constraints 
    from openai import OpenAI
    openai_api_key = "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"
    client = OpenAI(api_key=openai_api_key)

    user_input = f'I am a visitor to this Philadelphia historical site {site}. I am willing to travel for this amount of time: {distance_frame} and I would like to spend around {time_frame} at this location. Can you provide one suggestion of another historical site that I cna visit with these parameters?'
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": "You are a helpful tour guide in Philadelphia helping visitors find historical sites to visit. The user will provide you with a site they are currently visiting and parameters for the type of site they would like to visit next."},
            {"role": "user", "content": user_input}
        ]
    )
    st.write(response.choices[0].message.content)
elif nextstop_interest == "No":
    st.write(f'Thank you so much for using History Helper:Philadelphia!!! We hope you this information added to your experience at {site}! Please feel free to come back and inquire about another site any time!')

