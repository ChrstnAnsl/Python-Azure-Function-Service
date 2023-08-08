from datetime import datetime, timezone
import azure.functions as func
import logging
import requests

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

    send_notification_to_teams()

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
