from datetime import datetime, timezone, timedelta
import azure.functions as func
import logging
import requests
import pytz

log_file = "logfile.log"
est_timezone = pytz.timezone('America/New_York')

def send_notification_to_teams() -> None:
    try:
        teams_webhook_url = "https://notificatione096ed.azurewebsites.net/api/notification"
        response = requests.post(teams_webhook_url)
        
        if response.status_code == 200:
            logging.info("Notification sent successfully to Teams.")
        else:
            logging.error("Failed to send notification to Teams. Status code: %d", response.status_code)
    except Exception as e:
        logging.error("Error while sending notification to Teams: %s", str(e))

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.now(timezone.utc).isoformat()

    if mytimer.past_due:
        logging.warning('The timer is past due!')

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

    logging.info('Python timer trigger function ran at %s', utc_timestamp)