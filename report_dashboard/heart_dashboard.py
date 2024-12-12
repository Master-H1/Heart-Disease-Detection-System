import requests
import plotly.express as px
import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'axes.facecolor': '#fad4'}, style='darkgrid')
st.set_page_config(page_title="Heart Disease Detection", page_icon="report_dashboard/Heart.png",
                   layout="wide", initial_sidebar_state="expanded")

st.markdown(
    """
    <style> 
    div.block-container{padding-top:2rem;padding-left:1rem;padding-right:1rem;}
    span.st-emotion-cache-10trblm{color:salmon;}
    </style""", unsafe_allow_html=True)


# Load Database data
api_url = 'http://127.0.0.1:8000/api/heart-medical-history/'

df = pd.read_json(api_url)
# df = pd.DataFrame(data, )
df.dropna(inplace=True)
for col in df.columns:
    if col != 'oldpeak' and col != 'date_recorded':
        df[col] = df[col].astype('int')
    if col == 'date_recorded':
        df[col] = pd.to_datetime(df[col])
        df[col] = df[col].dt.date
df.rename(columns={'patient': 'patient_id'}, inplace=True)


# ====================== system title ===============
with st.container(border=True):
    st.subheader(":heart: Heart Disease Detection System")
    st.write("This system will help you to generate a good report based the heart disease patient treated within a specific time.")

# ======================== 0 Row ============================================================================
row0_col1, row0_col2 = st.columns((2, 1))
with row0_col1:
    row0_col11, row0_col12 = st.columns((2))
    with row0_col11:
        start_date = st.date_input("Start Date")

    with row0_col12:
        end_date = st.date_input("End Date")

    # Display data based on date filtered
    if start_date <= end_date:
        pass
    else:
        st.error("Start Date should be less than End Date")

    mask = (df["date_recorded"] >= start_date) & (
        df["date_recorded"] <= end_date)
    df = df.loc[mask]
    if not df.empty:
        pass
    else:
        st.error("No values available for specified date!")


# Let's visualize some data ====== Bar plot =============
    if not df.empty:
        # =========== Figure 1 ===================
        patient_count = df.groupby(['date_recorded', 'sex'])[
            'patient_id'].count()
        patient_count = patient_count.to_frame().sort_values(by='date_recorded')
        plt.figure(figsize=(15, 4))
        fig = patient_count.plot(kind='barh', width=0.4)
        plt.title(
            f"Total Patients per Sex, for each day from {start_date} to {end_date}", fontdict={"fontweight": "bold"})
        plt.xlabel('Number of Patients')
        plt.ylabel("Date_recorded,  Sex=[1: Male, 0:Female]", labelpad=1)
        plt.tight_layout()

        # Add mean values to the barplot
        for cont in fig.containers:
            fig.bar_label(cont, fmt='%.3g')
        st.pyplot(plt, use_container_width=True)

        # ========== Figure 2 ===================
        patient_count = df.groupby(['date_recorded', 'sex', 'heartdisease'])[
            'patient_id'].count()
        patient_count = patient_count.to_frame().sort_values(by='date_recorded')
        fig = plt.figure(figsize=(1, 4))
        graph = patient_count.plot(kind='barh')
        plt.title(
            f"Total Patients per Sex, for each day from {start_date} to {end_date}", fontdict={"fontweight": "bold"})
        plt.xlabel('Number of Patients')
        plt.ylabel(
            "Date_recorded,Sex,HeartDisease")
        fig.suptitle(
            f"Total Patients per Sex, for each day from {start_date} to {end_date}", fontweight="bold")
        fig.tight_layout()

        # Add mean values to the barplot
        for cont in graph.containers:
            graph.bar_label(cont, fmt='%.3g')

        st.pyplot(plt, use_container_width=True)
        # st.download_button(label="Download", file=graph,
        #                    file_name="report.png", mime="image/png")
        # st.button("Download This graph", onclick=graph.download)
        # if st.button("Download This graph"):
        #     plt.savefig("/home/merabu/Downloads/Total_patients_per_sex.png")
    else:
        st.error("No values available for specified date!")

# ===================== Visualize Pie plots = ==========
with row0_col2:

    #  ========= Figure 1 ================
    with st.container(border=True):
        if not df.empty:
            fig = plt.figure(figsize=(6, 4))
            values = df['sex'].value_counts()
            values.plot(kind='bar', color=['salmon', 'lightblue'])
            plt.ylabel("Number of Patients")
            plt.xticks(rotation=0)
            fig.suptitle(
                f"Number of Patients per Sex value, from {start_date} to {end_date}", fontweight='bold')
            st.pyplot(plt, use_container_width=True)

            # Display count dataframe
            st.write(values)

    #  ========= Figure 2 ================
    with st.container(border=True):
        if not df.empty:
            values = df['sex'].value_counts()
            fig = plt.figure(figsize=(4, 4))
            plt.pie(values, labels=values.index, colors=[
                    'salmon', 'lightblue'], autopct="%1.1f%%")
            plt.legend(title="Sex", labels=[
                       'Male', 'Female'], loc="upper right")
            plt.title(
                f"Percentage of Male vs Female for all Days, from {start_date} to {end_date}", fontdict={"fontweight": 'bold'})

            st.pyplot(fig, use_container_width=True)

    # ========== Figure 3 ================
    with st.container(border=True):
        if not df.empty:
            values = df['heartdisease'].value_counts()
            fig = plt.figure(figsize=(4, 5))
            plt.pie(values, labels=values.index, colors=[
                    "green", "blue"], autopct="%1.1f%%")
            plt.legend(title="Heart Disease", labels=[
                       'Has Disease', 'No Disease'], loc="upper right")
            plt.title(
                f"Percentage of Heart Disease for all Patients from {start_date} to {end_date}", fontdict={'fontweight': 'bold'})
            st.pyplot(fig, use_container_width=True)

    # ========== Figure 4 ================
    with st.container(border=True):
        if not df.empty:
            pd.crosstab(df['sex'], df['heartdisease']).plot(
                kind='bar', figsize=(6, 4), color=['blue', 'green'])
            plt.title(
                f"Sex vs HeartDisease from {start_date} to {end_date}", fontdict={'fontweight': 'bold'})
            plt.legend(title="Heart Disease", labels=[
                       'No Disease', 'Has Disease'], loc="upper right")
            plt.xticks(rotation=0)
            plt.ylabel("Number of patients")
            plt.xlabel("Sex = [0:Female,  1:Male]")
            st.pyplot(plt, use_container_width=True)


# ================================== First Row =============================================================
row1_col1, row1_col2 = st.columns((4, 1))


# We can display the dataframe
st.subheader("Patient Records.")
st.dataframe(df)

# ===============sidebar ========
if not df.empty:
    with st.sidebar:
        st.image("report_dashboard/Heart.png")
        with st.container(border=True):
            st.subheader("Model Accuracy:")
            st.metric("Recall Test Score:",
                      value="92%", delta="92%")
        st.subheader("System Report Service:", anchor="blue")
        with st.container(border=True):
            st.write('Total Patients:')
            st.write(df['patient_id'].count())
