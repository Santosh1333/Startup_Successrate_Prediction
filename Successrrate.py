import streamlit as st
pickle_in=open('model.pkl','rb')
model=pickle.load(pickle_in)
e=st.number_input('ENTER EXPERIENCE')
if st.button('PREDICT'):
  r=model.predict([[e]]).squeeze()
  st.success(f'rate: {r}')




