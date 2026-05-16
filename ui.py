
import streamlit as st


def metric_card(title, value):
    st.markdown(
        f'''
        <div class="metric-card">
            <div class="metric-label">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
        ''',
        unsafe_allow_html=True,
    )



def glass_container_start():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)



def glass_container_end():
    st.markdown('</div>', unsafe_allow_html=True)


