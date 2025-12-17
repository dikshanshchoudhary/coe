from datetime import datetime, timedelta
import pytz
import time

print("\n===== MEETING SCHEDULER & REMINDER =====\n")
meeting_title = input("Enter meeting title: ")

num = int(input("Enter number of participants: "))

participants = {}

for i in range(num):
    name = input(f"Enter participant {i+1} name/location: ")
    timezone = input(f"Enter timezone for {name} (example: Asia/Kolkata): ")
    participants[name] = timezone

preferred_date = input("Enter meeting date (YYYY-MM-DD): ")
base_time_ist = input("Enter meeting start time in IST (HH:MM): ")
meeting_duration_minutes = int(input("Enter meeting duration (in minutes): "))
print("\n Current Time in Each Time Zone:\n")

utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)

for place, zone in participants.items():
    tz = pytz.timezone(zone)
    local_time = utc_now.astimezone(tz)
    print(f"{place}: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
ist = pytz.timezone("Asia/Kolkata")

meeting_start_ist = ist.localize(
    datetime.strptime(preferred_date + " " + base_time_ist, "%Y-%m-%d %H:%M")
)

meeting_end_ist = meeting_start_ist + timedelta(minutes=meeting_duration_minutes)

print("\n Best Meeting Time for All Participants:\n")

for place, zone in participants.items():
    tz = pytz.timezone(zone)
    local_start = meeting_start_ist.astimezone(tz)
    local_end = meeting_end_ist.astimezone(tz)

    print(f"{place}: {local_start.strftime('%H:%M')} - {local_end.strftime('%H:%M')}")
print("\n MEETING AGENDA\n")
print(f"Title: {meeting_title}")
print("1. Welcome & Introductions")
print("2. Progress Updates")
print("3. Discussion & Issues")
print("4. Action Items and QnA")
print("5. Wrap-up")
reminder_time = meeting_start_ist - timedelta(minutes=15)

print("\n Reminder set for:", reminder_time.strftime("%Y-%m-%d %H:%M"), "IST")
print(" Waiting for reminder...\n")

while True:
    now = datetime.now(ist)
    if now >= reminder_time:
        print(" REMINDER: Meeting starts in 15 minutes!")
        break
    time.sleep(30)
