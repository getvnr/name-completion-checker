import streamlit as st
import pandas as pd

# Master list of names
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

st.title("Name Completion Checker")

st.write("Paste the names you want to check below (one per line):")

# Input box for user-pasted names
input_names = st.text_area("Enter names").splitlines()

if st.button("Check Completion"):
    # Strip spaces from input
    input_names = [name.strip() for name in input_names if name.strip()]
    
    completed = [name for name in input_names if name in master_names]
    not_completed = [name for name in input_names if name not in master_names]
    
    # Make both lists the same length for table display
    max_len = max(len(completed), len(not_completed))
    completed += [""] * (max_len - len(completed))
    not_completed += [""] * (max_len - len(not_completed))
    
    # Create dataframe
    df = pd.DataFrame({
        "Completed": completed,
        "Not Completed": not_completed
    })
    
    st.subheader("✅ Result Table")
    st.dataframe(df)
