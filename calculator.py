import streamlit as st
from mortgage_classes import FixedMortgageProduct

st.title("Maja's mortgage calculator")

st.write(f'Calculate your mortgageeeee :chart_with_upwards_trend::chart_with_upwards_trend::chart_with_upwards_trend::muscle::muscle::muscle::muscle::muscle::weight_lifter::weight_lifter::weight_lifter::weight_lifter:')

loan = st.slider("How much are you borrowing?", 10000, 500000,20000,1000)
rate = st.slider("What is your interest rate?", 0.01, 0.1,0.03,0.01)
years = st.slider("How many years will it take to pay back your mortgage?", 5, 40,10)


params = {'pv': loan, 'rate': rate, 'nper': years}

mp = FixedMortgageProduct(**params)

st.write(f'You have taken out a loan of £{loan} at an interest rate of {round(rate*100)}% over {years} years.')

st.write(f'	:moneybag::moneybag: Your monthly payment is £{round(mp.get_pmt()):,}. :money_with_wings::money_with_wings::money_with_wings::money_with_wings:')

params2 = {'pv': loan, 'rate': rate+0.03, 'nper': years}

mp2 = FixedMortgageProduct(**params2)

st.write(f'If your interest rate increased by 3%, your new monthly payment would be £{round(mp2.get_pmt()):,}.:chart_with_downwards_trend::pensive:	:point_down:')

st.write**(f'Alternatively, if you are unsure of how much you should borrow, please refer below.')**

payment = st.slider("How much is your monthly payment?", 100,10000,int(mp.get_pmt()),100)
rate2 = st.slider("What is your current interest rate?", 0.01,0.1,rate,0.01)
years2 = st.slider("In how many years will you be able to pay back your mortgage?", 5,40,years)

params3 = {'pmt': payment, 'rate': rate2, 'nper': years2}

mp3 = FixedMortgageProduct(**params3)

st.write(f'You can make a monthly payment of £{payment} at an interest rate of {round(rate2*100)}% over {years2} years.')
st.write(f'Your loan is £{round(mp3.get_pv()):,}.')