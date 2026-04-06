# beach_report.py
# MVP Beach Report System
# Author: JJ
# Date: 2026-04-05

import json
import requests

# Load beaches
with open("data/Beaches.json", "r") as f:
    beaches = json.load(f)["beaches"]

print("Checking today's weather...\n")

# Prepare Open-Meteo endpoint
BASE_URL = "https://api.open-meteo.com/v1/forecast"

results = []  # store each beach's weather

for beach in beaches:
    name = beach["name"]
    lat = beach["lat"]
    lon = beach["lon"]

    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": ["temperature_2m_max", "cloudcover_mean"],
        "timezone": "Pacific/Honolulu"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # Extract today's values (index 0)
    temp_c = data["daily"]["temperature_2m_max"][0]
    cloud = data["daily"]["cloudcover_mean"][0]

    # Convert Celsius → Fahrenheit
    temp_f = (temp_c * 9/5) + 32

    results.append({
        "name": name,
        "temp_f": round(temp_f, 1),
        "cloud": cloud
    })

# Print results
for r in results:
    print(f"{r['name']}: {r['temp_f']}°F, Cloudiness {r['cloud']}%")
# Apply beach-day rules
good_beaches = []

for r in results:
    temp = r["temp_f"]
    cloud = r["cloud"]

    if temp > 75 and cloud < 50:
        good_beaches.append(r["name"])

print("\nBeach Day Evaluation:")
if good_beaches:
    print("Good beach day! 🌞")
    print("Recommended beaches:")
    for b in good_beaches:
        print(f"- {b}")
else:
    print("Not a good beach day. 🌥️")
# Build email body
email_body = "Today's Beach Report:\n\n"

for r in results:
    email_body += f"{r['name']}: {r['temp_f']}°F, Cloudiness {r['cloud']}%\n"

email_body += "\nBeach Day Result:\n"

if good_beaches:
    email_body += "Good beach day! 🌞\n"
    email_body += "Recommended beaches:\n"
    for b in good_beaches:
        email_body += f"- {b}\n"
else:
    email_body += "Not a good beach day. 🌥️\n"
# Send email
import smtplib
from email.mime.text import MIMEText

sender = "jj4tajunk@gmail.com"
password = "ilby ujlv qdif hpfg"
recipient = "jj4tajunk@gmail.com"

msg = MIMEText(email_body)
msg["Subject"] = "Daily Beach Report"
msg["From"] = sender
msg["To"] = recipient

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.send_message(msg)

print("\nEmail sent successfully!")
# Write to log file
from datetime import datetime

log_path = "logs/beach_report.log"

with open(log_path, "a") as log:
    log.write("\n==============================\n")
    log.write(f"Run Date: {datetime.now()}\n")
    log.write("Weather Results:\n")

    for r in results:
        log.write(f"{r['name']}: {r['temp_f']}°F, Cloudiness {r['cloud']}%\n")

    log.write("\nBeach Day Result:\n")
    if good_beaches:
        log.write("Good beach day! Recommended beaches:\n")
        for b in good_beaches:
            log.write(f"- {b}\n")
    else:
        log.write("Not a good beach day.\n")

    log.write("Email sent successfully.\n")
