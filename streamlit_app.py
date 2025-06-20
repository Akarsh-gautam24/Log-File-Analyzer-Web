import streamlit as st
import re
from collections import defaultdict

st.set_page_config(page_title="Log File Analyzer", layout="centered")
st.title("🔍 Log File Analyzer for Intrusion Detection")

st.markdown("Upload a log file to analyze for suspicious IPs with multiple failed login attempts.")

uploaded_file = st.file_uploader("Choose a log file (.txt)", type="txt")

if uploaded_file is not None:
    suspicious_ips = defaultdict(int)
    log_lines = uploaded_file.read().decode("utf-8").splitlines()
    
    for line in log_lines:
        match = re.search(r'(\d+\.\d+\.\d+\.\d+).*POST /login.*401', line)
        if match:
            ip = match.group(1)
            suspicious_ips[ip] += 1

    flagged = {ip: count for ip, count in suspicious_ips.items() if count >= 3}

    if flagged:
        st.success("Suspicious IPs found:")
        for ip, count in flagged.items():
            st.write(f"• {ip} — {count} failed login attempts")
        
        if st.button("Download Results"):
            output = "\n".join([f"{ip} — {count} failed login attempts" for ip, count in flagged.items()])
            st.download_button("Download", data=output, file_name="detected_ips.txt", mime="text/plain")
    else:
        st.info("No suspicious activity detected in this file.")