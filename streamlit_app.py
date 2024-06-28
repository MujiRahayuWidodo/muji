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

def main() : 
    st.write('Minimal Example')
    
    st.header('This is Header')
    st.subheader('This is SubHeader')
    st.markdown('# Rendering Markdown ')
    st.write('Some Phytagorean Equation : ')
    st.latex('c^2 = a^2+b^2')
    
    df = pd.read_csv('house_clean.csv')
    st.write('Contoh dataframe')
    st.dataframe(df)
    # st.write('Menampilkan Dataframe dengan St AgGrid')
    # AgGrid(df)
    jml_row = len(df)
    jml_col = len(df.columns)
    st.metric(label="Jumlah kolom", value=f"{jml_row} rows")
    st.metric(label="Jumlah row", value=f"{jml_col} rows")
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

if __name__ == '__main__' : 
  main()

















