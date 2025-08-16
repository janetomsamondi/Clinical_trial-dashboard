import streamlit as st
import pandas as pd
import plotly.express as px

#load dataset
df = pd.read_excel(r"C:\Users\Administrator\Desktop\VISUALIZATION\clinical_trial_dummy_data.xlsx")

st.set_page_config(page_title="Clinical Trial Dashboard", layout='wide')
st.title("Cliical Trail Dashboard")
st.markdown("Interactive dashboard built with Streamlit + Plotly")

#sidebar filters
st.sidebar.header("Filters")
country = st.sidebar.multiselect(
    "Select Country:",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

treatment = st.sidebar.multiselect(
    "Select Treatment Arm:",
    options=df["Treatment_Arm"].unique(),
    default=df["Treatment_Arm"].unique()
)

outcome = st.sidebar.multiselect(
    "Select Outcome:",
    options=df["Outcome"].unique(),
    default=df["Outcome"].unique()
)

#Filter dataset
filtered_df = df[
    (df["Country"].isin(country)) &
    (df["Treatment_Arm"].isin(treatment)) &
    (df["Outcome"].isin(outcome))

     ]

#layout: Two colums
col1, col2 = st.columns(2)

#patients by country
with col1:
    st.subheader("Patients by Country")
    fig1 = px.histogram(filtered_df, x="Country", color="Treatment_Arm",
                        barmode="group", text_auto=True)
    st.plotly_chart(fig1, use_container_width=True)

#Age distribution
with col2:
    st.subheader("Age distribution by Treatment Arm")
    fig2 = px.box(filtered_df, x="Treatment_Arm",y="Age", color="Treatment_Arm",)
    st.plotly_chart(fig2, use_container_width=True)

#Outcome trends
st.subheader("Patient Outcomes Over Time")
fig3 = px.histogram(filtered_df, x="Visit_Date", color="Outcome",
                    barmode="stack", text_auto=True)
st.plotly_chart(fig3, use_container_width=True)

#Compliance vs Age scatter
st.subheader("Compliance vs Age")
fig4 = px.scatter(filtered_df, x="Age", y="Compliance_%", color="Treatment_Arm",
                  hover_data=["Subject_ID", "Country", "Outcome"],
                  size="Compliance_%", trendline="ols")
st.plotly_chart(fig4, use_container_width=True)

#Data table
st.subheader("Filtered Patient Data")
st.dataframe(filtered_df)