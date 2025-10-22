import streamlit as st

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

st.write("Paste the names you want to check below:")

# Input box for user-pasted names
input_names = st.text_area("Enter names (one per line)").splitlines()

if st.button("Check Completion"):
    completed = [name for name in input_names if name.strip() in master_names]
    not_completed = [name for name in input_names if name.strip() not in master_names]
    
    st.subheader("✅ Completed Names")
    st.write(completed if completed else "None")
    
    st.subheader("❌ Not Completed Names")
    st.write(not_completed if not_completed else "None")
