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
st.write("Paste the names you want to check below (one per line):")

# Input box
input_names = st.text_area("Enter names").splitlines()
input_names = [name.strip() for name in input_names if name.strip()]

if st.button("Check Completion"):
    completed = [name for name in input_names if name in master_names]
    not_completed = [name for name in input_names if name not in master_names]

    st.subheader("✅ Completed Names")
    if completed:
        for name in completed:
            st.write(name)
    else:
        st.write("None")
    
    st.subheader("❌ Not Completed Names")
    if not_completed:
        for name in not_completed:
            st.write(name)
    else:
        st.write("None")
