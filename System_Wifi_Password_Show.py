import subprocess
import re
import streamlit as st
def get_saved_wifi_passwords():
    wifi_list = subprocess.check_output("netsh wlan show profiles", shell=True).decode()
    profiles = re.findall(r"All User Profile\s*:\s(.*)", wifi_list)

    wifi_data = []

    for profile in profiles:
        profile = profile.strip()
        try:
            result = subprocess.check_output(f'netsh wlan show profile name="{profile}" key=clear', shell=True).decode()
            password = re.search(r"Key Content\s*:\s(.*)", result)
            if password:
                wifi_data.append((profile, password.group(1)))
            else:
                wifi_data.append((profile, "No Password Found"))
        except subprocess.CalledProcessError:
            wifi_data.append((profile, "Error Fetching Details"))

    return wifi_data

# Streamlit App UI
st.title("🔐 Saved Wi-Fi Password Viewer")
st.write("This app shows saved Wi-Fi profiles and their passwords on your system.")

if st.button("Show Wi-Fi Passwords"):
    wifi_info = get_saved_wifi_passwords()

    if wifi_info:
        for name, pwd in wifi_info:
            st.markdown(f"**Wi-Fi Name:** {name}")
            st.code(pwd, language='text')
    else:
        st.warning("No Wi-Fi profiles found.")


