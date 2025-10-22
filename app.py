import streamlit as st
import pandas as pd

# Master list with emails
master_dict = {
    "Lakshmi Narayana Rao .": "lakshmi-narayana-rao.vullapu@dxc.com",
    "Ramesh Polisetty": "ramesh.polisetty@dxc.com",
    "Gayatri Ruttala": "gayatri.ruttala@dxc.com",
    "Namithananda D": "namithananda.d@dxc.com",
    "Kalpana Edagotti": "kalpana.edagotti@dxc.com",
    "Gangavarapu suneetha": "suneetha.gangavarapu@dxc.com",
    "Yaswanth Chinthalapudi": "y.chinthalapudi@dxc.com",
    "Balachander Sammeta": "balachander.sammeta@dxc.com",
    "Abdul Mukthiyar Basha": "abdul.mukthiyarbasha@dxc.com",
    "Kaustubh Chaudhari": "kaustubh.chaudhari@dxc.com",
    "MADHURUSHA BOOPATHI": "madhurusha.b@dxc.com",
    "chidipothu Ajay kumar": "chidipothu.ajaykumar@dxc.com",
    "Thorat Yashwant": "thorat.yashwant@dxc.com",
    "Vivek Kushwaha": "vivek.kushwaha@dxc.com",
    "Panneer Selvam Murugesan": "panneerselvam@dxc.com",
    "Shejal Gawade": "shejal.gawade@dxc.com",
    "Gopalakrishnan Selvaraj": "gopalakrishnan.selvaraj@dxc.com",
    "Imran Khan": "imran.khan26@dxc.com",
    "Naveen M": "naveen.m3@dxc.com",
    "Vaibhav Kishore Khati": "vaibhav.kishorekhati@dxc.com",
    "Anil kumar Athkuri": "anil.kum.athkuri@dxc.com",
    "Divya Muppa": "divya.muppa@dxc.com",
    "Nitin Srivastav": "nitin.srivastav@dxc.com",
    "SRINIVASU CHEEDALLA": "srinivasu.cheedalla@dxc.com",
    "POUSALI CHAKRABORTY": "pousalichakraborty@dxc.com",
    "RAJESH JAYAPALAN": "rajesh.jayapalan@dxc.com",
    "Anandha Rupan Venkatesan": "a.rupanvenkatesan@dxc.com"
}

st.title("Completed vs Not Completed Names with Emails")
st.write("Paste the names you have completed below (one per line):")

# Input names
completed_input = st.text_area("Enter completed names").splitlines()
completed_input = [name.strip() for name in completed_input if name.strip()]

if st.button("Show Table"):
    # Completed names (present in master)
    completed_names = [name for name in completed_input if name in master_dict]
    completed_emails = [master_dict[name] for name in completed_names]

    # Not completed names (in master but not in completed_input)
    not_completed_names = [name for name in master_dict if name not in completed_names]
    not_completed_emails = [master_dict[name] for name in not_completed_names]

    # Make both lists same length for table display
    max_len = max(len(completed_names), len(not_completed_names))
    completed_names += [""] * (max_len - len(completed_names))
    completed_emails += [""] * (max_len - len(completed_emails))
    not_completed_names += [""] * (max_len - len(not_completed_names))
    not_completed_emails += [""] * (max_len - len(not_completed_emails))

    # Create dataframe
    df = pd.DataFrame({
        "✅ Completed Name": completed_names,
        "✅ Completed Email": completed_emails,
        "❌ Not Completed Name": not_completed_names,
        "❌ Not Completed Email": not_completed_emails
    })

    st.subheader("Result Table")
    st.dataframe(df)
