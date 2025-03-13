import re
import streamlit as st
#page styling

st.set_page_config(page_title="Password Checker", page_icon="🔒", layout="centered")
st.markdown(""""
<style>
     .main {text-align: center;}
     .stTextInput {width:60% !important; margin:  auto;}
     .stButton button {width:50%; background-color: #4CAF50; text-align: center; color: white; font-size: 18px; padding: 10px 20px; margin: 10px 0px;} 
     .stButton button:hover {background-color: #45a049;} 
</style>            
""", unsafe_allow_html=True)

#page title
st.title("🔒 Password Checker")
st.write("Enter your password to check its strength")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at **least 8 characters long**.")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain **uppercase and lowercase letters**.")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should include **at least one numbers**.")
    
    #specail characters
    if re.search(r"[!@#$%&*^]", password):
        score += 1
    else:
        feedback.append("❌ include **at least one special character (!@#$%&*^)**.")

    #display password strength
    if score == 4:
    
        st.success("✔ Your password is **strong**.")
    elif score >= 3:
        st.info("⚠ Your password is **medium**.")
    else:
        st.error("❌ Your password is **weak**.")
    
    #feedback
    if feedback:
          with st.expander("improve your password"):
               for item in feedback:
                    st.write(item)
password = st.text_input("Enter your password", type="password" ,  help="Enter your password is strong")
if st.button("Check"):
    if password:
         check_password_strength(password)
    else:
        st.warning(" ⚠ Please enter your password to check its strength.")



    
    
