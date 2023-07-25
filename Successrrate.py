import pickle
import streamlit as st

try:
    pickle_in = open('model.pkl', 'rb')
    model = pickle.load(pickle_in)
except FileNotFoundError:
    st.error("Model file not found. Please make sure 'model.pkl' is present.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    st.stop()

e = st.number_input('ENTER EXPERIENCE')
if st.button('PREDICT'):
    try:
        r = model.predict([[e]]).squeeze()
        st.success(f'rate: {r}')
    except AttributeError:
        st.error("The model does not have a 'predict' method.")
    except Exception as e:
        st.error(f"An error occurred while making the prediction: {e}")




