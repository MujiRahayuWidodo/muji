# import altair as alt
# import numpy as np
# import pandas as pd
# import streamlit as st

# """
# # Welcome to Streamlit!

# Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
# If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
# forums](https://discuss.streamlit.io).

# In the meantime, below is an example of what you can do with just a few lines of code:
# """

# num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
# num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

# indices = np.linspace(0, 1, num_points)
# theta = 2 * np.pi * num_turns * indices
# radius = indices

# x = radius * np.cos(theta)
# y = radius * np.sin(theta)

# df = pd.DataFrame({
#     "x": x,
#     "y": y,
#     "idx": indices,
#     "rand": np.random.randn(num_points),
# })

# st.altair_chart(alt.Chart(df, height=700, width=700)
#     .mark_point(filled=True)
#     .encode(
#         x=alt.X("x", axis=None),
#         y=alt.Y("y", axis=None),
#         color=alt.Color("idx", legend=None, scale=alt.Scale()),
#         size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
#     ))


import streamlit as st 
import pandas as pd
import plotly.express as px 
import matplotlib.pyplot as plt

df = pd.read_csv('house_clean.csv')

def main() : 
    st.sidebar.title("Menu")
    menu = st.sidebar.selectbox("Pilih halaman:", ["Home", "Profile"])

    if menu == "Home":
        show_home()
    elif menu == "Profile":
        show_profile()

def data():
    st.title("Home")
    st.write("Selamat datang di halaman Home!")
    st.write("Di sini Anda dapat menambahkan konten untuk halaman Home Anda.")
    # Tambahkan konten halaman Home di sini

def profile():
    st.title("Data Overview")
    st.write("Ini adalah halaman Profile.")
    st.write("Di sini Anda dapat menambahkan konten untuk halaman Profile Anda.")
    # Tambahkan konten halaman Profile di sini
        
    st.write('Minimal Example')
    
    st.header('This is Header')
    st.subheader('This is SubHeader')
    st.markdown('# Rendering Markdown ')
    st.write('Some Phytagorean Equation : ')
    st.latex('c^2 = a^2+b^2')
    
    st.write('Contoh dataframe')
    st.dataframe(df)
    # st.write('Menampilkan Dataframe dengan St AgGrid')
    # AgGrid(df)

    col1, col2, col3 = st.columns(3)
    with col1:
        jml_row = len(df)
        st.metric(label="Jumlah kolom", value=f"{jml_row} rows")
    with col2:    
        jml_col = len(df.columns)
        st.metric(label="Jumlah row", value=f"{jml_col} rows")
    with col3:    
        st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

    col1, col2 = st.columns(2)
    with col1:
        st.write('bedrooms vs price')
        fig,ax = plt.subplots()
        plt.scatter(df['bedrooms'],df['price'])
        st.pyplot(fig)
    with col2:    
        plotly_fig = px.scatter(df['bedrooms'],df['price'])
        st.plotly_chart(plotly_fig)

    click_me_btn = st.button('Click Me')
    st.write(click_me_btn) #Return True kalo di Click 
    check_btn = st.checkbox('Klik Jika Setuju')
    if check_btn :
        st.write('Anda Setuju')    
    
    radio_button= st.radio('Choose below',[x for x in range(1,3)])
    st.write('Anda Memilih',radio_button)
    
    #slider 
    age_slider = st.slider('Berapa Usia Anda',0,100)
    st.write('Usia Anda',age_slider)
    
    #Input (Typing)
    num_input = st.number_input('Input Berapapun')
    st.write('Kuadrat dari {} adalah {}'.format(num_input,num_input**2))

    #sidebar 
    sidebar_checkbox = st.sidebar.checkbox('Checkbox di Sidebar')
    sidebar_radio_button = st.sidebar.radio('Pilih Menu',options=['A','B','C'])

    #sidebar 
    with st.form("Data Diri"):
       st.write("Inside the form")
       slider_val = st.slider('Berapa Usia Anda',0,100)
       st.write('Anda Memilih',slider_val)
        
       checkbox_val = st.checkbox('Klik Jika Setuju')
       if check_btn :
           st.write('Anda Setuju')    

       # Every form must have a submit button.
       submitted = st.form_submit_button("Submit")
       if submitted:
           st.write("slider", slider_val, "checkbox", checkbox_val)

    st.write("Outside the form")
    
    #columns :
    col1, col2, col3 = st.columns(3)

    with col1:
       st.header("A cat")
       st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
       st.header("A dog")
       st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
       st.header("An owl")
       st.image("https://static.streamlit.io/examples/owl.jpg")
    #expander 
    #dengan with atau dengan assignment 
    expander = st.expander("Klik Untuk Detail ")
    expander.write('Anda Telah Membuka Detail')
    

if __name__ == '__main__' : 
  main()

















