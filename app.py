import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import random
# Custom CSS for styling
languages = ["Assamese", "Bengali", "Gujarati", "Hindi", "Kannada", "Kashmiri", "Konkani", "Malayalam", "Manipuri", "Marathi", "Odia", "Punjabi", "Sanskrit", "Tamil", "Telugu"]
dataset_strength = [random.randint(1000, 10000) for _ in range(len(languages))]
progress = [random.randint(0, 100) for _ in range(len(languages))]
managers = ["Join us", "Manager Name", "Join us", "Manager Name", "Join us", "Join us", "Manager Name", "Join us", "Join us", "Join us", "Join us", "Join us", "Join us", "Manager Name", "Join us"]
df = pd.DataFrame({
    "Language": languages,
    "Dataset Strength": dataset_strength,
    "Progress": progress,
    "Program Managers": managers
})

st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
        }
        .header {
            font-size: 2.5em;
            font-weight: bold;
            text-align: center;
            color: #2e4053;
        }
        .subheader {
            font-size: 1.5em;
            font-weight: bold;
            color: #2874a6;
        }
        .text {
            font-size: 1.2em;
            color: #2e4053;
        }
        .contact {
            font-size: 1.2em;
            color: #2874a6;
            text-align: center;
        }
        .partner-logo {
            max-width: 150px;
            max-height: 100px;
        }
    </style>
""", unsafe_allow_html=True)

# Setting the title of the web page
st.markdown('<div class="header">SanskritiBench:Bridging NLP and Indian Cultural Richness</div>', unsafe_allow_html=True)

# Abstract section
st.markdown('<div class="subheader">Abstract</div>', unsafe_allow_html=True)
st.markdown("""
        <div class="text">
        The aim of the project is to develop a state-of-the-art Indian Cultural benchmark that can test these models for their cultural accuracies, especially in a country like India which is rich in diversity. With Hugging Face support, our aim is to expand the benchmark into an alignment dataset and release it.<br>
        We will be covering the 15 official languages of India: Assamese, Bengali, Gujarati, Hindi, Kannada, Kashmiri, Konkani, Malayalam, Manipuri, Marathi, Odia, Punjabi, Sanskrit, Tamil, Telugu and their corresponding dialects. This is a community-driven project and your support and collaboration can make this initiative a success.
        </div>
    """, unsafe_allow_html=True)

# Goals and Milestones section
st.markdown('<div class="subheader">Goals and Milestones</div>', unsafe_allow_html=True)
st.markdown("""
        <div class="text">
        <strong>Goals:</strong>
        <ul>
            <li>Develop state of the art Indian Culture Benchmark.</li>
            <li>Enhance NLP models with cultural and social awareness by working on cultural alignment datasets.</li>
            <li>Extend the research into deeper levels for each Indian Language.</li>
        </ul>
        <strong>Milestones:</strong>
        <ul>
            <li>Milestone 1: Initial research and dataset collection.</li>
            <li>Milestone 2: Model benchmarking and preliminary testing.</li>
            <li>Milestone 3: Dataset Release and Feedback</li>
            <li>Milestone 4: Final evaluation and publication.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)

# PI and Advisor section
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="subheader">Principal Investigator (PI)</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Guneet Singh Kohli<br>Research Lead and NLP Engineer</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="subheader">Research Advisors</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="text">
        <strong>Industry:</strong><br>
        - Dr. Shantipriya Parida, Silo AI<br>
        - Anindya Sannigarhi, Prem AI<br>
        <br>
        <strong>Academia:</strong><br>
        - Dr. Sathya Ranjan , Assistant Professor, KIIT<br>
        - Dr. Prashant Singh Rana, Assistant Professor, Thapar University<br>
        - Aseem Srivastava, PhD, IIIT Delhi<br>
        <br>
        </div>
    """, unsafe_allow_html=True)

# Language project and progress section
st.dataframe(
    df,
    column_config={
        "Language": "Language",
        "Dataset Strength": st.column_config.NumberColumn(
            "Dataset Strength",
            help="Number of data points in the dataset",
            format="%d"
        ),
        "Progress": st.column_config.ProgressColumn(
            "Progress",
            help="Progress in percentage",
            format="%d%%",
            min_value=0,
            max_value=1000,
        ),
        "Program Managers": "Program Managers"
    },
    hide_index=True,
)

# Create a table to display the data in a more detailed manner
st.markdown('<div class="subheader">Language Progress and Managers</div>', unsafe_allow_html=True)

# Display the data in a tabular format with progress bars
for i in range(len(df)):
    col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
    with col1:
        st.write(df.loc[i, "Language"])
    with col2:
        st.write(df.loc[i, "Dataset Strength"])
    with col3:
        st.progress(df.loc[i, "Progress"])
    with col4:
        st.write(df.loc[i, "Program Managers"])

# Project partner section
st.markdown('<div class="subheader">Project Partners</div>', unsafe_allow_html=True)
st.markdown('<div class="text">Our Partners:</div>', unsafe_allow_html=True)
partners = ["img/huggingFace.png"]
cols = st.columns(len(partners))
for col, partner in zip(cols, partners):
    col.image(partner, use_column_width=True, caption="Partner Logo")

# Contact us or join us section
st.markdown('<div class="subheader">Contact Us or Join Us</div>', unsafe_allow_html=True)
st.markdown('<div class="contact">If you are interested in joining our project or want to know more about our research, please contact us at:<br>Email: research@project.com<br>Phone: +1 234 567 890</div>', unsafe_allow_html=True)
