import streamlit as st

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

st.title("Uncompleted Names Checker")
st.write("Paste the names you have completed below (one per line):")

# Input names from user
completed_names = st.text_area("Enter completed names").splitlines()
completed_names = [name.strip() for name in completed_names if name.strip()]

if st.button("Show Uncompleted Names"):
    # Names in master list that are NOT in the pasted completed names
    uncompleted_names = [name for name in master_names if name not in completed_names]

    st.subheader("❌ Uncompleted Names")
    if uncompleted_names:
        for name in uncompleted_names:
            st.write(name)
    else:
        st.write("All names are completed ✅")
