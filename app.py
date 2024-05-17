import streamlit as st
import pandas as pd

# Custom CSS for styling

df = pd.read_csv("data.csv")

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
        .contact {
            font-size: 18px;
            line-height: 1.6;
            color: #1C2833;
            margin-bottom: 20px;
            text-align: left;
        }
        .contact-info {
            font-weight: bold;
            color: #2874A6;
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
        - Anindyadeep Sannigrahi, Prem AI<br>
        <br>
        <strong>Academia:</strong><br>
        - Dr. Sathya Ranjan , Assistant Professor, KIIT University<br>
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
    use_container_width=True,
    height=600
)

# Project partner section
st.markdown('<div class="subheader">Project Partners</div>', unsafe_allow_html=True)
st.markdown('<div class="text">Our Partners:</div>', unsafe_allow_html=True)
partners = ["img/supporters.png"]
cols = st.columns(len(partners))
for col, partner in zip(cols, partners):
    col.image(partner, use_column_width=True, caption="Partner Logo")

st.markdown('<div class="center-content">', unsafe_allow_html=True)
st.markdown('<div class="subheader">Contact Us or Join Us</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="contact">
        If you are interested in joining our project or want to know more about our research, please contact us at:<br>
        <span class="contact-info">Email:</span> guneetfateh07@gmail.com<br>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# Embedding the Google Form
st.markdown(
    """
    <div class="center-content">
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSf69DLv-dsKwVjAN1Z8xzexk0MjMMwmh6cd3y9BkEPfqVYnAQ/viewform?embedded=true" width="640" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    </div>
    """,
    unsafe_allow_html=True
)
