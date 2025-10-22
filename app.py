import streamlit as st
import pandas as pd

# Master/source list of names
master_names = [
    "Lakshmi Narayana Rao",
    "Ramesh Polisetty",
    "Gayatri Ruttala",
    "Namithananda D",
    "Kalpana Edagotti",
    "Gangavarapu suneetha",
    "Yaswanth Chinthalapudi",
    "Balachander Sammeta",
    "Abdul Mukthiyar Basha",
    "Kaustubh Chaudhari",
    "MADHURUSHA BOOPATHI",
    "chidipothu Ajay kumar",
    "Thorat Yashwant",
    "Vivek Kushwaha",
    "Panneer Selvam Murugesan",
    "Shejal Gawade",
    "Gopalakrishnan Selvaraj",
    "Imran Khan",
    "Naveen M",
    "Vaibhav Kishore Khati",
    "Anil kumar Athkuri",
    "Divya Muppa",
    "Nitin Srivastav",
    "SRINIVASU CHEEDALLA",
    "POUSALI CHAKRABORTY",
    "RAJESH JAYAPALAN",
    "Anandha Rupan Venkatesan"
]

st.title("Completed vs Not Completed Names")
st.write("Paste the names you have completed below (one per line):")

# Input names from user
completed_input = st.text_area("Enter completed names").splitlines()
completed_input = [name.strip() for name in completed_input if name.strip()]

if st.button("Show Table"):
    # Names that are actually completed (present in master list)
    completed_names = [name for name in completed_input if name in master_names]

    # Names not completed (in master list but not in completed_input)
    not_completed_names = [name for name in master_names if name not in completed_names]

    # Make both lists same length for display
    max_len = max(len(completed_names), len(not_completed_names))
    completed_names += [""] * (max_len - len(completed_names))
    not_completed_names += [""] * (max_len - len(not_completed_names))

    # Create a dataframe for table display
    df = pd.DataFrame({
        "✅ Completed": completed_names,
        "❌ Not Completed": not_completed_names
    })

    st.subheader("Result Table")
    st.dataframe(df)
