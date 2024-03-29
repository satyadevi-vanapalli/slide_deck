import streamlit as st
import streamlit_authenticator as stauth
# from dependancies import fetch_users, sign_up
import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re
import mysql.connector
import time
import bcrypt
from sqlalchemy.sql import text

st.set_page_config(page_title='Streamlit', page_icon='🐍', initial_sidebar_state='collapsed')
conn = st.connection('mysql', type='sql')

def validate_email(email):
    """
    Check Email Validity
    :param email:
    :return True if email is valid else False:
    """
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$" #tesQQ12@gmail.com

    if re.match(pattern, email):
        print(pattern)
        return True
    return False

def fetch_users():
    st.cache_data.clear()
    df = conn.query('SELECT * from users;', ttl=600)
    st.write(df)

def get_user_emails():
    st.cache_data.clear()
    df = conn.query('SELECT * from users;', ttl=600)
    # st.write(df.to_dict(),"KKK")
    emails = []
    for row in df.itertuples():
        # st.write(row,"JJJ")
        emails.append(row.email)
    print(emails,df)
    return emails
def validate_username(username):
    pattern = "^[a-zA-Z0-9 ]*$"
    if re.match(pattern, username):
        return True
    return False

def get_usernames():
    st.cache_data.clear()
    df = conn.query('SELECT * from users;', ttl=600)
    # st.write(df.to_dict())
    usernames = []
    for row in df.itertuples():
        usernames.append(row.userName)
    return usernames
def main():
    fetch_users()
    try:
        signUpForm = st.empty()
        with signUpForm.form('signup'):
            
            signUptext = st.empty()
            emailText = st.empty()
            usernameText = st.empty()
            password1Text = st.empty()
            password2Text = st.empty()
            signUpbutton = st.empty()
            signUptext.subheader('Sign Up')
            email = emailText.text_input('Email', placeholder='Enter Your Email')
            username = usernameText.text_input('Username', placeholder='Enter Your Username')
            password1 = password1Text.text_input('Password', placeholder='Enter Your Password', type='password')
            password2 = password2Text.text_input('Confirm Password', placeholder='Confirm Your Password', type='password')
            # btn1= st.columns(1)
            # showError = False
            # with btn1:
            accountCreated = False
            if signUpbutton.form_submit_button('Sign Up'):
                # st.write("LL")
                if email:
                    if validate_email(email):
                        if email not in get_user_emails():
                            if username and validate_username(username):
                                if username not in get_usernames():
                                    if len(username) >= 2:
                                        if len(password1) >= 6:
                                            if password1 == password2:
                                                # Add User to DB
                                                hashed_password = stauth.Hasher([password2]).generate()
                                                # insert_user(email, username, hashed_password[0])
                                                # with conn.session as s:

                                                insert_stmt = (
                                                    "INSERT INTO users(username, email, password)" "VALUES (%s, %s, %s)")
                                                data = (username, email, hashed_password[0])
                                                print(data,"?????????????????/",insert_stmt)
                                                # conn.query(insert_stmt, data)
                                                    # cu.execute(insert_stmt, data)
                                                    # s.commit()
                                                st.cache_data.clear()
                                                conn1 = st.connection('mysql', type='sql')

                                                with conn1.session as s:
                                                    a = 'INSERT INTO users (username, email, password) VALUES ("{username}","{email}","{password}");'.format(username=username, email=email, password=hashed_password[0])
                                                    s.execute(
                                                        text(a)
                                                    )
                                                    s.commit()
                                                    accountCreated = True
                                                with emailText.container():
                                                    st.success('Account created successfully!!')
                                                    st.balloons()
                                                with usernameText.container():
                                                    pass
                                                with password1Text.container():
                                                    pass
                                                with password2Text.container():
                                                    pass
                                                with signUptext.container():
                                                    pass
                                                with signUpForm.container():
                                                    pass
                                                st.markdown("""
    <style>

        .st-emotion-cache-u9xbm8 {
                                                            visibility:hidden;
                                                            height:0px !important
        }
                                                            .st-emotion-cache-17ypgft {
                                                            height:10px !important;
                                                            }


    </style>""", unsafe_allow_html=True)
                                                st.write('<a href="/" target="_self" style="color:white;margin-left:35%">Please click here to login</a>', unsafe_allow_html=True)
                                            else:
                                                st.warning('Passwords Do Not Match')
                                        else:
                                            st.warning('Password is too Short')
                                    else:
                                        st.warning('Username Too short')
                                else:
                                    st.warning('Username Already Exists')

                            else:
                                st.warning('Invalid Username')
                        else:
                            st.warning('Email Already exists!!')
                    else:
                        st.warning('Invalid Email')
                else:
                    # showError = True
                    st.warning("Please add all details")
            if not accountCreated:
                st.write('<a href="/" target="_self" style="color:white">Already have account?</a>', unsafe_allow_html=True)
    except Exception as e:
        st.write(e)

if __name__ == '__main__':
    main()
