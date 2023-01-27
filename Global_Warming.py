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

#c1.image(Image.open('Images/op-arb.JPG'))


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
     if query1 == 'Daily Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8481f651-ec83-44a4-8aa5-d79ef14de8d9/data/latest')
     elif query1 == 'ALICE Price ATH':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/392bbd12-3ba3-4fa8-844b-6bf8f81405e5/data/latest')
     elif query1 == 'New Addresses':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/90828ee6-8f67-47de-8812-29d302b22d4c/data/latest')
     elif query1 == 'Daily Transactions Value':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ea6888d0-422a-4bce-bb77-da7ec1410cbc/data/latest')
     elif query1 == 'Weekly Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/29ad802c-4267-4cc7-8458-b48f17d6898b/data/latest')
     elif query1 == 'Monthly Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8fd56cb3-9123-407b-9c95-0f215202a1a2/data/latest')
     elif query1 == 'New Addresses Weekly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ca20a9b0-a0c5-49c9-b3d3-5a16a11e6b45/data/latest')
     elif query1 == 'New Addresses Monthly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/37b83485-1817-4ca3-bf57-8157ff28addc/data/latest')
     elif query1 == 'Transaction Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/335e43c1-ebc8-4117-80be-b97f3d0945a7/data/latest')
     elif query1 == 'Arbitrum TX Status':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/cfc29701-c6f0-4a71-b102-7f119313dda9/data/latest')
     elif query1 == 'Optimism TX Status':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/880cf7d7-70ab-4cff-b926-3b6df8a28c59/data/latest')
     elif query1 == 'Arbitrum TX Status Weekly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a7c937c0-1a3f-4d47-8e9f-daece6bcab95/data/latest')
     elif query1 == 'Optimism TX Status Weekly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ef59f00d-7aff-42ea-9c8c-f7da9bf07f31/data/latest')
     elif query1 == 'Arbitrum TX Status Monthly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8007648b-997a-4647-9900-ebb983e78c23/data/latest')
     elif query1 == 'Optimism TX Status Monthly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/73494d91-353c-4d8a-aa52-d6eb9f112e10/data/latest')
     elif query1 == 'Top 20 Events Based on TXs Count Arbitrum':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/eb082222-8ccf-4e35-ae4d-238f1fa70f2d/data/latest')
     elif query1 == 'Top 20 Events Based on TXs Count Optimism':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c4cf84bd-d545-4620-ba8d-2949ac7b929b/data/latest')
     elif query1 == 'Classification of Activity of Addresses Arbitrum':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/06ff575c-8b6b-43ca-b973-21e2dd759071/data/latest')
     elif query1 == 'Classification of Activity of Addresses Optimism':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/bb5316a1-9a0e-42d2-aef9-b9e82b0dc36d/data/latest')
     elif query1 == 'Status of Total Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a2b49ba0-adb2-4834-bd8a-6d8c6fbff7ba/data/latest')
     elif query1 == 'Heat Map of Transactions Arbitrum':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/450b8565-460f-4913-a299-4a4b4fd98bee/data/latest')
     elif query1 == 'Heat Map of Transactions Optimism':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ecacbbd4-fd7f-417a-99b4-80fd0a4fef8f/data/latest')
     return None

Daily_Transactions = get_data('Daily Transactions')
ALICE_Price_ATH = get_data('ALICE Price ATH')
New_Addresses = get_data('New Addresses')
Daily_Transactions_Value = get_data('Daily Transactions Value')
Weekly_Transactions = get_data('Weekly Transactions')
Monthly_Transactions = get_data('Monthly Transactions')
New_Addresses_Weekly = get_data('New Addresses Weekly')
New_Addresses_Monthly = get_data('New Addresses Monthly')
Transaction_Overview = get_data('Transaction Overview')
Arbitrum_TX_Status = get_data('Arbitrum TX Status')
Optimism_TX_Status = get_data('Optimism TX Status')
Arbitrum_TX_Status_Weekly = get_data('Arbitrum TX Status Weekly')
Optimism_TX_Status_Weekly = get_data('Optimism TX Status Weekly')
Arbitrum_TX_Status_Monthly = get_data('Arbitrum TX Status Monthly')
Optimism_TX_Status_Monthly = get_data('Optimism TX Status Monthly')
Top_20_Events_Based_on_TXs_Count_Arbitrum = get_data('Top 20 Events Based on TXs Count Arbitrum')
Top_20_Events_Based_on_TXs_Count_Optimism = get_data('Top 20 Events Based on TXs Count Optimism')
Classification_of_Activity_of_Addresses_Arbitrum = get_data('Classification of Activity of Addresses Arbitrum')
Classification_of_Activity_of_Addresses_Optimism = get_data('Classification of Activity of Addresses Optimism')
Status_of_Total_Transactions = get_data('Status of Total Transactions')
Heat_Map_of_Transactions_Optimism = get_data('Heat Map of Transactions Optimism')
Heat_Map_of_Transactions_Arbitrum = get_data('Heat Map of Transactions Arbitrum')

	
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


