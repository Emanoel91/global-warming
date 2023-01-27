# 📚 Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import PIL
from PIL import Image

theme_plotly = None # None or streamlit

# Title
st.set_page_config(page_title='Global Warming', page_icon=':bar_chart:', layout='wide')
st.title('🌍 Global Warming')

# Content
c1, c2 = st.columns(2)

c1.image(Image.open('Images/gw.JPG'))


st.subheader('📃 Introduction')


st.write(
    """
111
    """
)

st.subheader('🎯 Purposes of Dashboard')
st.write(
    """
111
    """
)


#---------------------------------------------------------------------------------------------------------
# dash_style
with open('style.css')as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
	
# flipside API
@st.cache(ttl=600)
def get_data(query1):
     if query1 == 'Global temperature anomalies':
        return pd.read_json('https://pkgstore.datahub.io/core/global-temp/monthly_json/data/4c7af7363a20648a68b8f2038a6765d6/monthly_json.json')
     elif query1 == 'Annual Global temperature anomalies':
        return pd.read_json('https://pkgstore.datahub.io/core/global-temp/annual_json/data/529e69dbd597709e36ce11a5d0bb7243/annual_json.json')

     return None

Global_temperature_anomalies = get_data('Global temperature anomalies')
Annual_Global_temperature_anomalies = get_data('Annual Global temperature anomalies')

df = Global_temperature_anomalies
fig = px.line(df, x='Date', y='Mean', color='Source', title='MonthlyGlobal temperature anomalies from year 1 to present', log_y=False)
fig.update_layout(showlegend=True, xaxis_title=None, legend_title='', yaxis_title='Celsius', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Annual_Global_temperature_anomalies
fig = px.line(df, x='Year', y='Mean', color='Source', title='Yearly Global temperature anomalies from year 1 to present', log_y=False)
fig.update_layout(showlegend=True, xaxis_title=None, legend_title='', yaxis_title='Celsius', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Analyst: [Emanoel](https://twitter.com/Astiran91)**', icon="📌")
    #c1.image(Image.open('Images/analyst2.JPG'))
with c2:
    st.info('**Database: [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="📚")
    #c2.image(Image.open('Images/flipside.JPG'))
with c3:
    st.info('**Provided for: [MetricsDao](https://metricsdao.xyz/)**', icon="💡")
    #c3.image(Image.open('Images/metricsdao.JPG'))


