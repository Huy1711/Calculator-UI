import streamlit as st

st.title("A Simple Calculator")

left_side, _ = st.columns(2)

with left_side:

    col1, col2, col3, col4 = st.columns([1,1,1,1])

    if "display_value" not in st.session_state:
        st.session_state["display_value"] = ""

    with col1:
        if st.button('7'):
            st.session_state["display_value"] += '7'
        if st.button('4'):
            st.session_state["display_value"] += '4'
        if st.button('1'):
            st.session_state["display_value"] += '1'
        if st.button('0'):
            st.session_state["display_value"] += '0'

    with col2:
        if st.button('8'):
            st.session_state["display_value"] += '8'
        if st.button('5'):
            st.session_state["display_value"] += '5'
        if st.button('2'):
            st.session_state["display_value"] += '2'
        if st.button('.'):
            st.session_state["display_value"] += '.'

    with col3:
        if st.button('9'):
            st.session_state["display_value"] += '9'
        if st.button('6'):
            st.session_state["display_value"] += '6'
        if st.button('3'):
            st.session_state["display_value"] += '3'
        if st.button('='):
            try:
                st.session_state["display_value"] = str(eval(st.session_state["display_value"]))
            except ZeroDivisionError:
                st.session_state["display_value"] = "INF"
            except Exception as e:
                st.session_state["display_value"] = "Error"

    with col4:
        if st.button('/'):
            st.session_state["display_value"] += '/'    
        if st.button('\*'):
            st.session_state["display_value"] += '*'
        if st.button('\-'):
            st.session_state["display_value"] += '-'
        if st.button('\+'):
            st.session_state["display_value"] += '+'
            
    long_col, short_col = st.columns([3, 1])
    with short_col:
        if st.button('AC'):
            st.session_state["display_value"] = ""
    with long_col:
        tile = long_col.container(border=True)
        display_value = st.session_state["display_value"] if st.session_state["display_value"] != "" else "0"
        tile.text(display_value)