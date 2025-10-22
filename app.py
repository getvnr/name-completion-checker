import streamlit as st

# Master/source list of names
source_names = [
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
st.write("Paste the names you want to check below (one per line):")

# Input names
input_names = st.text_area("Enter names").splitlines()
input_names = [name.strip() for name in input_names if name.strip()]

if st.button("Check Uncompleted Names"):
    # Find names that are not in source/master list
    uncompleted = [name for name in input_names if name not in source_names]

    st.subheader("❌ Uncompleted Names")
    if uncompleted:
        for name in uncompleted:
            st.write(name)
    else:
        st.write("All names are completed ✅")
