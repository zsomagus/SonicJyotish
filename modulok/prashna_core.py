import pendulum
import swisseph as swe
from modulok.astro_core import get_planet_data
import streamlit as st
from modulok.config import fill_coordinate_entries
st.subheader("📍 Prashna helyszín megadása")

with st.form("prashna_location_form"):
    prashna_city = st.text_input("Kérdés helyszíne (város)", value="Budapest")
    prashna_lat = st.text_input("Szélességi fok", value="")
    prashna_lon = st.text_input("Hosszúsági fok", value="")
    prashna_submit = st.form_submit_button("🔍 Mentés")

def fill_prashna_data_streamlit():
    now = pendulum.now("Europe/Budapest")

    # Alapadatok
    date_str = now.format("YYYY-MM-DD")
    time_str = now.format("HH:mm")
    lat = "47.4979"
    lon = "19.0402"

    # UTC idő (opcionális)
    utc_dt = now.in_timezone("UTC")
    utc_str = utc_dt.format("YYYY-MM-DD HH:mm")

    # Julián-dátum számítása
    jd = swe.julday(
        now.year,
        now.month,
        now.day,
        now.hour + now.minute / 60.0 + now.second / 3600.0,
    )

    # Csak a három elfogadott paramétert adjuk át
    chart_data = get_planet_data(
        jd=jd,
        latitude=float(lat),
        longitude=float(lon)
    )

    return {
        "date": date_str,
        "time": time_str,
        "latitude": lat,
        "longitude": lon,
        "utc": utc_str,
        "jd": jd,
        "chart_data": chart_data
    }
