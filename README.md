Log File Analyzer (Streamlit Web App)

This project is a browser-based log analyzer built using Streamlit. It scans server log files (in Apache-style format) and flags suspicious IP addresses that have made multiple failed login attempts — ideal for SOC analysts and cybersecurity learners.

Live App:
Access the app here: https://log-analyzer-web-ubslepkydzqxwa8vfjhanu.streamlit.app/

Features:
- Upload .txt log files via browser
- Detect brute-force login attempts using IP and 401 error patterns
- Displays flagged IPs in real time
- Download report as detected_ips.txt
- Mobile and desktop friendly

Built With:
- Python 3.x
- Streamlit
- Regular Expressions (re)
- GitHub for deployment

Files Included:
- streamlit_app.py — main Streamlit web app
- requirements.txt — dependencies for deployment

Deployment:
Hosted for free using Streamlit Cloud.
To run locally:

pip install streamlit
streamlit run streamlit_app.py

Developed By:
Akarsh Gautam
GitHub: https://github.com/Akarsh-gautam24

Educational Use Only:
This tool is intended for ethical learning, training, and demonstration purposes only.
