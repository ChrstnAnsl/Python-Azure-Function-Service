import requests, pytz
from datetime import datetime, timedelta

log_file = "logfile.log"
est_timezone = pytz.timezone('America/New_York')

# Function to send notification to Microsoft Teams
def send_notification_to_teams():
    # Your code to send the notification to Teams here
    teams_webhook_url = "https://my-bot.azurewebsites.net/api/notification"
    requests.post(teams_webhook_url)
    
    # For now, this function will log a message to a file.
    with open(log_file, "a") as file:
        file.write(f"Sending notification to Teams at {datetime.now()}. Please submit your time card\n")

# Get the current time in 24-hour format
current_time = datetime.now(est_timezone).strftime("%H")

# Check if it's 8:00 AM EST to send the notification to Teams
if current_time == "08":
    # Get the current day of the week (0 = Monday, 1 = Tuesday, ..., 4 = Friday)
    current_day = datetime.now(est_timezone).weekday()

    # Check if it's the last weekday of the month
    if (datetime.now(est_timezone) + timedelta(days=1)).month != datetime.now(est_timezone).month and current_day < 5:
        with open(log_file, "a") as file:
            file.write(f"{datetime.now(est_timezone)}: log for this timesheet as End of Month\n")
        send_notification_to_teams()

    # Check if it's Friday (0 = Monday, ..., 4 = Friday)
    if current_day == 4:
        with open(log_file, "a") as file:
            file.write(f"{datetime.now(est_timezone)}: log for this timesheet as end of Week\n")
        send_notification_to_teams()