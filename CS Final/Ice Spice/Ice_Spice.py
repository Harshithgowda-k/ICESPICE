# --- Importing Modules ---
import pickle
import pip._vendor.requests
import streamlit as st
import mysql.connector as mc
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu


update = True
in_log = False
wrong_user = True
wrong_pass = True



if 'not_login' not in st.session_state:
    st.session_state['not_login'] = update
    
if 'login' not in st.session_state:
    st.session_state['login'] = in_log




if st.session_state['not_login'] == True:
    #---- Page Design ----
    st.set_page_config(page_title="Ice Spice", page_icon=":olive:", layout="wide")

    selected = option_menu(menu_title=None, default_index=0,
                options=["Home", "About Us", "Login","Register","Feedback"],
                # --- ICONS WEBISTE https://icons.getbootstrap.com/ ---font
                icons=["grid-fill","layout-text-window","fingerprint","person-plus-fill","envelope-paper-fill"],
                orientation="horizontal",
                styles={
                    "container": {"padding": "0!important", "background-color": "#0A2F51"},
                    "icon": {"color":"#ffffff", "font-size": "20px"},
                    "nav-link": {
                        "font-size": "20px",
                        "text-align": "center",
                        "margin": "0px",
                        "--hover-color": "#224362 ",
                        },
                    "nav-link-selected": {"background-color": "#1977CC"},
                        },)


    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_home = load_lottieurl("https://lottie.host/bb604c6a-914f-4938-95c5-a2171cf0a0f0/W3bPcF2miq.json")
    lottie_login = load_lottieurl("https://lottie.host/8e46ff97-82e0-48af-aae5-00d53310a2e8/O3S1lFyzsf.json")
    lottie_abu = load_lottieurl("https://lottie.host/a7e721ef-cf46-46f9-b72d-28329286f29a/dY91hIB3NR.json")
    lottie_regsiter = load_lottieurl("https://lottie.host/05c2003e-fddf-408f-b394-443227cac701/7KBNTgAZlg.json")








    # --- Home Page ---
    if selected == "Home":
        # ---- HEADER SECTION ----
        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.subheader("Freshness of farm on your table!")
                st.title("ice Spice")
                st.subheader("Discover a vibrant array of fresh vegetables and fruits on our online marketplace. Enjoy farm-fresh goodness delivered to your doorstep, ensuring quality and convenience for your daily needs.")
            with right_column:
                st_lottie(lottie_home, height=300, key="coding")






    # --- About Us Page ---
    elif selected == "About Us":
        colr, coll = st.columns(2)
        with coll:
            st_lottie(lottie_abu, height=300, key="coding")
        with colr:
            st.header ("What is Ice Spice?")
            st.write("Ice Spice is an open source food and grocery store where you will find everything you are looking for, right from Fruits and Vegetable,Rice and Dals,Spices and Seasonings to packaged products, Beverages and many more-we have it all. We are fresh that stands out. Choose from a wide range of options in every category, exclusively handpicked to help you find the best quality available at the lowest prices. Select a time slot for delivery and your order will be delivered right to your doorstep, anywhere in Bangalore.We guarantee on time delivery, and the best quality!\nDid you know the average person makes 221 food related decisions every day? As a grocer, we believe that everyone deserves to have access to fresh, affordable and delicious food, no matter who you are, how you shop or what you like to eat. At the heart of it, food can and SHOULD be fresh, so our new brand has been designed to stand out by being optimistic, bright, welcoming and above all fresh.")
        st.subheader("\nWhy should I use Ice Spice?")
        st.write("\nIce Spice allows you to walk away from the drudgery of grocery shopping and welcome an easy relaxed way of browsing and shopping for groceries. Discover new products and shop for all your food and grocery needs from the comfort of your home or office. No more getting stuck in traffic jams, paying for parking , standing in long queues and carrying heavy bags – get everything you need, when you need, right at your doorstep. Food shopping online is now easy as every product on your monthly shopping list.")
        st.subheader("\n\nWhere do we operate?")
        st.write("\nWe currently offer our services in Bangalore")






                


    # --- Registering Page ---
    if selected == "Register":

        left_column, right_column = st.columns(2)

        with right_column:
            st_lottie(lottie_regsiter, height=300, key="coding") 


        with left_column:
            st.title("Registration Page")
            st.subheader("Tell us about yourself!")
            user_name = st.text_input("User Name", max_chars=None)
            user_password = st.text_input("Password",type = "password", max_chars=None)
            user_type = st.radio("Who are you?" , ('Customer', 'Seller'))
            user_type= str(user_type)


            if user_type == "Seller":
                col1, col2, = st.columns(2)
                with col1:
                    seller_location = st.text_input("From where do you export?", max_chars=None)
                    print("\n\n\nLocation:",seller_location,"\n\n\n")
                with col2:
                    seller_location_pin = st.text_input("Enter your city PIN", max_chars=None)
                seller_options = st.multiselect("What would like to sell?",['Fruits', 'Vegitables', 'Meat/Dairy'])
               



                submit = st.button("Submit")

                if submit == True:
                    
                    #---- Saving User Data----
                    with open ("login.dat","ab") as datafile1:
                        register = [user_name,user_password,user_type]        
                        pickle.dump(register, datafile1)

                    con = mc.connect(host = "localhost",user = "root", password = "password", auth_plugin = "mysql_native_password",database = "Website_Data")

                    if con.is_connected():
                        cur = con.cursor()
                        try:
                            cur.execute("CREATE TABLE SELLER_INFO(SELLER_NAME char(50),SELLER_TYPE char(50),SELLER_LOCATION char(50),SELLER_LOCATION_PIN int)")
                        except:
                            print("Table exists!")
                        
                        cur.execute("INSERT INTO SELLER_INFO VALUES('{}','{}','{}',{})".format(user_name,user_type,seller_location,seller_location_pin))
                    
                        con.commit()
                    con.close()

                    



                    st.success("Your Data Has Be Submitted")


            if user_type == "Customer":
                col1, col2, = st.columns(2)
                with col1:
                    custo_location = st.text_input("Enter city name", value="", max_chars=None)
                with col2:
                    custo_location_pin = st.text_input("Enter your city PIN", value="", max_chars=None)
                custo_options = st.multiselect("What is your die style?",['Vegan','Non-Vegan'])

                
                submit = st.button("Submit")

                if submit == True:
        
                    #---- Saving User Data----
                    with open ("login.dat","ab") as datafile2:
                        register = [user_name,user_password,user_type]         
                        pickle.dump(register,datafile2)

                    con = mc.connect(host = "localhost",user = "root", password = "root", auth_plugin = "mysql_native_password",database = "Website_Data")

                    if con.is_connected():
                        cur = con.cursor()
                        try:
                            cur.execute("CREATE TABLE CONSUMER_INFO(CONSUMER_NAME char(50),CONSUMER_TYPE char(50),CONSUMER_LOCATION char(50),CONSUMER_LOCATION_PIN int)")
                        except:
                            print("Table exists!")
                        
                    cur.execute("INSERT INTO CONSUMER_INFO VALUES('{}','{}','{}',{})".format(user_name,user_type,custo_location,custo_location_pin))
                    con.commit()
                    con.close()
                    st.success("Your Data Has Be Submitted")





    if selected == "Login":
        # --- USER AUTHENTICATION ---

            left_column, right_column = st.columns(2)

            with right_column:
                st_lottie(lottie_login, height=300, key="coding")

            with left_column:
                user_name_login = st.text_input("User Name", max_chars=None)
                user_password_login = st.text_input("Password", type = "password",max_chars=None)
                st.warning("Please enter your username and password")

                
                
                log_in = st.button("Login")

                if log_in == True:
                    with open ("login.dat","rb") as file:
                        try:
                            while True:
                                data = pickle.load(file)
                                if data[0] == user_name_login:
                                    wrong_user = False
                                    if data[1]==user_password_login:
                                        wrong_pass = False
                                        st.success("Loging In!")
                                        update = False
                                        in_log = True

                        



                            
                        except EOFError:               
                                if wrong_pass == True:        
                                        st.error("Password Incorrect!")

                                
                                if wrong_user == True:
                                    st.error("Username Incorrect!")


                                if user_name_login not in data:
                                    st.error("User Data not found! Please register to login!")
                            


                                
                            
                                  



    # --- Feedback Page ---
    if selected == "Feedback":
        # ---- CONTACT ----
        with st.container():
            st.write("---")
            st.header("Give us ur feedback!!")
            st.write("##")

            contact_form = """
            <form action="https://formsubmit.co/harshithgowda.k007@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
            st.markdown(contact_form, unsafe_allow_html=True)



if update == False:
    st.session_state['not_login'] = False
    st.session_state['login'] = True




# Use local CSS
file_name = "style/style.css"
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
