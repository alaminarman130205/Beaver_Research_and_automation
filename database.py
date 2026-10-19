
import streamlit as st
import psycopg
from psycopg.rows import dict_row


def get_connection():
    """Open a secure PostgreSQL connection using Streamlit secrets."""
    config = st.secrets["database"]

    return psycopg.connect(
        host=config["host"],
        port=int(config["port"]),
        dbname=config["dbname"],
        user=config["user"],
        password=config["password"],
        sslmode=config.get("sslmode", "require"),
        connect_timeout=10,
        row_factory=dict_row,
    )


def test_connection():
    """Check whether PostgreSQL is reachable."""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT current_database() AS database_name;")
            return cur.fetchone()


def save_inquiry(
    full_name,
    email,
    phone,
    organization,
    service,
    budget_range,
    project_details,
    consent_to_contact,
):
    """Save a new inquiry into the client_inquiries table."""

    sql = """
        INSERT INTO public.client_inquiries (
            full_name,
            email,
            phone,
            organization,
            service,
            budget_range,
            project_details,
            consent_to_contact
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
    """

    values = (
        full_name,
        email,
        phone or None,
        organization or None,
        service,
        budget_range or None,
        project_details,
        consent_to_contact,
    )

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, values)
            result = cur.fetchone()

    return result["id"]
