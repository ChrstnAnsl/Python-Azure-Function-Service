from datetime import datetime
import azure.functions as func
import logging
import requests
import pytz

log_file = "logfile.log"
est_timezone = pytz.timezone('America/New_York')

def send_notification_to_teams():
    try:
        # Your code to send the notification to Teams here
        teams_webhook_url = "https://notificatione096ed.azurewebsites.net/api/notification"
        requests.post(teams_webhook_url)
        
        # For now, this function will log a message to a file.
        with open(log_file, "a") as file:
            file.write(f"Sending notification to Teams at {datetime.now()}. Please submit your time card\n")
    except Exception as e:
        # Log the exception details
        with open(log_file, "a") as file:
            file.write(f"Error while sending notification to Teams: {str(e)}\n")

# def main(mytimer: func.TimerRequest) -> None:
#     utc_timestamp = datetime.datetime.utcnow().replace(
#         tzinfo=datetime.timezone.utc).isoformat()

#     if mytimer.past_due:
#         logging.info('The timer is past due!')
#         print('The timer is past due!')

send_notification_to_teams()  # This is where you are calling the function

#     logging.info('Python timer trigger function ran at %s', utc_timestamp)
#     print('Python timer trigger function ran at %s', utc_timestamp)
