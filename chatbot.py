import streamlit as st

# ===========================
#   DATA SECTION
# ===========================

doctor_schedule = {
    "Dr. Meredith Grey": {
        "specialty": "Gynecologist",
        "available_days": ["Monday", "Wednesday", "Friday"]
    },
    "Dr. Mark Sloan": {
        "specialty": "Dermatologist",
        "available_days": ["Tuesday", "Thursday"]
    },
    "Dr. Derek Shepherd": {
        "specialty": "General Physician",
        "available_days": ["Monday", "Tuesday", "Friday"]
    }
}

symptom_advice = {
    "fever": "A mild fever is usually nothing serious—rest, stay hydrated, and keep an eye on it. If it sticks around for more than a few days, it’s worth getting checked.",
    "cough": "A simple cough can come from a cold or dry throat. Warm fluids and rest help a lot. If it gets worse or lasts over a week, you may want to see a doctor.",
    "headache": "Headaches can come from stress, dehydration, or lack of sleep. Try drinking water and resting. If headaches happen often or feel severe, it might need a medical visit.",
    "rash": "Skin rashes can be from allergies, irritation, or infections. Try avoiding anything that might have triggered it. If it spreads or becomes painful, a dermatologist should take a look."
}

clinic_hours = "🕒 Clinic Operating Hours: **8 AM – 6 PM (Monday to Friday)**"
emergency_message = "🚨 If this is a medical emergency, call your local emergency number immediately."


# ===========================
#   FUNCTION SECTION
# ===========================

def display_doctors():
    """Returns a formatted list of doctors."""
    info_lines = []
    for doctor, details in doctor_schedule.items():
        days = ", ".join(details["available_days"])
        info_lines.append(
            f"**{doctor}** — {details['specialty']}  \nAvailable: *{days}*"
        )
    return "\n\n".join(info_lines)


def book_appointment(doctor, day):
    """Validates and books appointment."""
    if doctor not in doctor_schedule:
        return "❌ Doctor not found."

    if day not in doctor_schedule[doctor]["available_days"]:
        return f"❌ {doctor} is not available on {day}."

    return f"✅ **Appointment booked with {doctor} on {day}!**"


def get_symptom_advice(symptom):
    """Provides advice based on symptom."""
    symptom = symptom.lower().strip()
    return symptom_advice.get(symptom, "❓ Symptom not recognized. Try another.")


# ===========================
#   STREAMLIT UI SECTION
# ===========================

st.set_page_config(page_title="Clinic Chatbot", page_icon="🏥", layout="centered")

st.title("🏥 Clinic Appointment & Symptom Checker Chatbot")
st.write("Welcome! Choose a service from the menu on the left.")

menu = st.sidebar.radio(
    "📌 Navigation",
    ["Home", "Check Doctors", "Book Appointment", "Symptom Checker", "Clinic Hours", "Emergency Help"]
)

# ========== HOME PAGE ==========
if menu == "Home":
    st.header("🏠 Home")
    st.write("This chatbot helps you:")
    st.markdown("""
    - 📅 Book appointments  
    - 👨‍⚕️ Check available doctors  
    - 🤒 Get basic symptom guidance  
    - 🕒 View clinic hours  
    - 🚨 Access emergency help  
    """)

# ========== CHECK DOCTORS PAGE ==========
elif menu == "Check Doctors":
    st.header("👨‍⚕️ Available Doctors")
    st.markdown(display_doctors())

# ========== BOOK APPOINTMENT PAGE ==========
elif menu == "Book Appointment":
    st.header("📅 Book an Appointment")

    doctor = st.selectbox("Select a doctor", list(doctor_schedule.keys()))
    day = st.selectbox("Select a day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])

    if st.button("Book Appointment"):
        result = book_appointment(doctor, day)
        st.success(result)

# ========== SYMPTOM CHECKER PAGE ==========
elif menu == "Symptom Checker":
    st.header("🤒 Symptom Checker")

    symptom = st.text_input("Enter your symptom (e.g., fever, cough, rash)")

    if st.button("Get Advice"):
        advice = get_symptom_advice(symptom)
        st.info(advice)

# ========== CLINIC HOURS ==========
elif menu == "Clinic Hours":
    st.header("🕒 Clinic Operating Hours")
    st.info(clinic_hours)

# ========== EMERGENCY SECTION ==========
elif menu == "Emergency Help":
    st.header("🚨 Emergency Assistance")

    st.error("If you believe this is a serious or life-threatening situation, contact emergency services or go to the nearest hospital immediately.")

    st.subheader("🚑 Nearby Emergency Hospitals (Kenya)")

    st.markdown("""
    **M.P. Shah Hospital**  
    📞 Emergency: +254 20 4291 500  
    Address: Shivachi Road, Parklands, Nairobi  

    **The Nairobi Hospital**  
    📞 Emergency: +254 703 082 000  
    Address: Argwings Kodhek Rd, Nairobi  

    **Aga Khan University Hospital**  
    📞 Emergency: +254 20 366 2000  
    Address: 3rd Parklands Ave, Nairobi  
    """)

    st.info("If transportation is needed, consider using an ambulance service or local emergency number.")

