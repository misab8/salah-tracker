import streamlit as st
import datetime

st.set_page_config(page_title="Salah Tracker", layout="centered")

st.title("🕌 Salah Tracker")
st.write("Track your daily prayers and build consistency in your worship.")

# Today's date
today = datetime.date.today()
st.subheader(f"Date: {today.strftime('%A, %d %B %Y')}")

# Initialize session state
if "salah_status" not in st.session_state:
    st.session_state.salah_status = {
        "Fajr": False,
        "Dhuhr": False,
        "Asr": False,
        "Maghrib": False,
        "Isha": False
    }

# Show checkboxes for 5 prayers
st.markdown("### ✅ Mark your prayers:")
for prayer in st.session_state.salah_status:
    st.session_state.salah_status[prayer] = st.checkbox(prayer, value=st.session_state.salah_status[prayer])

# Summary
completed = sum(1 for done in st.session_state.salah_status.values() if done)
st.markdown("---")
st.success(f"**You've completed {completed}/5 prayers today.** Keep going!")

# Tip
st.info("Try to come back every day and track your prayers for long-term consistency.")
