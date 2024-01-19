import streamlit as st
import pandas as pd
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
import streamlit_antd_components as sac 


b = BtcConverter()
c=CurrencyRates()


#setting page configurations
st.set_page_config(page_title='HERMES',page_icon='🧭',layout='wide',initial_sidebar_state="collapsed")
#currency converter
st.image('https://github.com/joyall2812/HERMES-CONVERTER/blob/main/images/HERMES%20CONVERTER-logos_white_cropped.png?raw=true',use_column_width=True)

#setting up menu
#selected=option_menu(menu_title='main menu',menu_icon='Bank',options=['home','currency converter','exchange rates'],orientation='horizontal',icons=['home','arrow-repeat','arrow-up-right-circle-fill'])
tab= sac.tabs([
    sac.TabsItem(label='currency converter',icon='arrow-repeat'),
    sac.TabsItem(label='exchange rates',icon='arrow-up-right-circle-fill'),
    sac.TabsItem(label='about',icon='chat-left-heart-fill'),
], variant='outline', use_container_width=True, return_index=True)
# List of currency codes
currency_codes = ['EUR', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF',
                  'ISK', 'NOK', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'INR', 'KRW',
                  'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR', 'USD']

# Mapping of currency codes to full names
currency_names = {
    'EUR': 'Euro',
    'JPY': 'Japanese Yen',
    'BGN': 'Bulgarian Lev',
    'CZK': 'Czech Koruna',
    'DKK': 'Danish Krone',
    'GBP': 'British Pound Sterling',
    'HUF': 'Hungarian Forint',
    'PLN': 'Polish Złoty',
    'RON': 'Romanian Leu',
    'SEK': 'Swedish Krona',
    'CHF': 'Swiss Franc',
    'ISK': 'Icelandic Króna',
    'NOK': 'Norwegian Krone',
    'TRY': 'Turkish Lira',
    'AUD': 'Australian Dollar',
    'BRL': 'Brazilian Real',
    'CAD': 'Canadian Dollar',
    'CNY': 'Chinese Yuan Renminbi',
    'HKD': 'Hong Kong Dollar',
    'IDR': 'Indonesian Rupiah',
    'INR': 'Indian Rupee',
    'KRW': 'South Korean Won',
    'MXN': 'Mexican Peso',
    'MYR': 'Malaysian Ringgit',
    'NZD': 'New Zealand Dollar',
    'PHP': 'Philippine Peso',
    'SGD': 'Singapore Dollar',
    'THB': 'Thai Baht',
    'ZAR': 'South African Rand',
    'USD': 'United States Dollar'
}

# Create a small box in the sidebar and display the list of currencies
st.sidebar.markdown("### Currency Codes and Full Names:")
for code in currency_codes:
    st.sidebar.text(f"{code} - {currency_names.get(code, 'Unknown')}")
if tab==0:
    with st.form(key='currencyform'):
        st.header('CURRENCY :red[CONVERTER]')
        st.caption('Convert the value of one currency to another with real-time exchange rates. Enter the amount and select the currencies to see the equivalent amount instantly.')

        box1,box2,box3=st.columns([3,2,2])
        with box1:
           amount=st.number_input('amount',step=1)
        with box2:
           From=st.selectbox('From',currency_codes,key='currency1')
        with box3:
           To=st.selectbox('To',currency_codes,key='currency2')
        submit=st.form_submit_button(label='convert')
    if submit:
       a=round(c.convert(From,To,amount),ndigits=2)
       output=(f':red[{amount}] {currency_names[From]}s is equal to :red[{a}] {currency_names[To]}s')
       st.info(output)
    
    sac.divider(label='H E R M E S', align='center', color='gray',key='dv1')
#bitcoin converter
    with st.form(key='btconv'):
            st.header('BITCOIN :red[CONVERTER]')
            btbox1,btbox2=st.columns(2)
            with btbox1:
                amnt=st.number_input(b.get_symbol())
            with btbox2:
                bcr=st.selectbox('To',currency_codes,key='btsb')
            submit=st.form_submit_button(label='convert')

#converting the entered value to selected currenc
    if submit:
       ab=round(b.convert_btc_to_cur(amnt,bcr),ndigits=3)
       output=(f':red[{amnt}] bitcoins are equal to :red[{ab}]{currency_names[bcr]}')
       st.info(output)

if tab==1:
    with st.form(key='rateform2'):
        st.header('CURRENCY :red[RATES] FROM-TO')
        st.caption(' Instantly view the current exchange rate between two specific currencies.')
        boxr1,boxr2=st.columns(2)
        with boxr1:
                Fromr=st.selectbox('From',currency_codes,key='currency1r')
        with boxr2:
            tor=st.selectbox('To',currency_codes,key='currency2r')
        submit=st.form_submit_button(label='submit')
        if submit:
                rr=c.get_rate(Fromr,tor)
                outputrte=(f'the exchange rate between {currency_names[Fromr]} and {currency_names[tor]} is {rr}')
                st.info(outputrte)
    
            
    sac.divider(label='H E R M E S', align='center', color='gray',key='dv2')
    with st.form(key='rateform',clear_on_submit=True):
        st.header('CURRENCY :red[RATES]')
        st.caption('Explore real-time exchange rates for various currencies against a base currency. Stay informed about the latest market values to make informed decisions.')
        crncy=st.selectbox('select currency',currency_codes)
        submit=st.form_submit_button(label='submit')
    if submit:
        r=c.get_rates(crncy)
        rdf=pd.DataFrame(list(r.items()),columns=['Currency Code', 'Exchange Rate'])
    #st.download_button(label='download data as CSV',data=csv_file)
        st.dataframe(rdf,use_container_width=True,hide_index=True)
        #AgGrid(rdf)

if tab==2:
    st.markdown(""" # Welcome to Hermes: Your Simple Currency Converter

Hermes is a straightforward currency converter designed for quick and accurate currency conversions. Whether you're dealing with traditional currencies or cryptocurrencies like Bitcoin, Hermes has you covered. With real-time exchange rates and a minimalist design, currency conversion has never been easier.

## Features:

- **Bitcoin Conversion:**
  Easily convert Bitcoin to any other currency or vice versa. Hermes ensures accurate and up-to-date conversion rates.

- **Real-Time Exchange Rates:**
  Access the latest exchange rates at your fingertips. Hermes provides real-time information for precise currency conversions.

## How to Use:

1. **Select Currencies:**
   Choose the currencies you want to convert from and to.

2. **Enter Amount:**
   Input the amount you wish to convert.

3. **Get Results:**
   View the converted amount instantly.

## Connect with us:

- [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/joyall2812/HERMES-CONVERTER)

- [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:joyalvs380@gmail.com)
 
    """ )


    def getrating():
        a=sac.rate(label='rate my app', value=0.0, align='start')
        
        if a>0:
            st.write('Thank you for your rating')
    getrating()
