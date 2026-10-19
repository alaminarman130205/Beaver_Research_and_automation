
import streamlit as st
import resend


def send_inquiry_notification(
    full_name,
    email,
    phone,
    organization,
    service,
    budget_range,
    project_details,
):
    """Send an email notification when a client submits an inquiry."""

    config = st.secrets["resend"]

    resend.api_key = config["api_key"]

    message = f"""
A new client inquiry has been submitted.

Client name: {full_name}
Client email: {email}
Phone: {phone or "Not provided"}
Organization: {organization or "Not provided"}
Service: {service}
Budget: {budget_range or "Not decided"}

Project details:
{project_details}
"""

    return resend.Emails.send(
        {
            "from": config["from_email"],
            "to": [config["notification_email"]],
            "subject": f"New client inquiry from {full_name}",
            "text": message,
            "reply_to": email,
        }
    )
