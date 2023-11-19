import streamlit as st

with st.form(key='profile_form'):
    # text box
    name = st.text_input('name')
    address = st.text_input('address')

    # select box
    age_category = st.radio(
        'age group',
        ('Children(under 18 years old)', 'Adult(18 years or older)'))

    # Multiple Selection
    hobby = st.multiselect(
        'hobby',
        ('sports', 'reading', 'programming', 'anime and movie', 'fishing', 'cooking'))

    # button
    submit_btn = st.form_submit_button('send')
    cancel_btn = st.form_submit_button('cancel')

    if submit_btn:
        st.text(f'Welcome! {name}! I sent the book to {address}!')
        st.text(f'age group: {age_category}')
        st.text(f'hobby: {", ".join(hobby)}')