import streamlit as st
from mortgage_classes import FixedMortgageProduct

st.title("Maja's mortgage calculator")

loan = st.slider("How much are you borrowing?", 10000, 500000,20000,1000)
rate = st.slider("What is your interest rate?", 0.01, 0.1,0.03,0.01)
years = st.slider("How many years will it take to pay back your mortgage?", 5, 40,10)


params = {'pv': loan, 'rate': rate, 'nper': years}

mp = FixedMortgageProduct(**params)

st.write(f'You have taken out a loan of £{loan} at an interest rate of {round(rate*100)}% over {years} years.')

st.write(f'Your monthly payment is £{round(mp.get_pmt()):,}.')

params2 = {'pv': loan, 'rate': rate+0.03, 'nper': years}

mp2 = FixedMortgageProduct(**params2)

st.write(f'If your interest rate increased by 3%, your new monthly payment would be £{round(mp2.get_pmt()):,}.')