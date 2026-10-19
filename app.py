
import streamlit as st
from email_validator import validate_email, EmailNotValidError

from database import save_inquiry
from email_notifications import send_inquiry_notification


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Beaver Research & Automation",
    page_icon="🦫",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------
st.markdown(
    """
    <style>
    @import url(
        'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap'
    );

    :root {
        --navy: #10233f;
        --blue: #2563eb;
        --teal: #0f766e;
        --ink: #172b46;
        --muted: #64748b;
        --paper: #f6f8fc;
    }

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .stApp {
        background: var(--paper);
    }

    .block-container {
        max-width: 1180px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    .brand {
        font-family: 'Manrope', sans-serif;
        color: var(--navy);
        font-size: 1.35rem;
        font-weight: 800;
        letter-spacing: -0.5px;
    }

    .hero {
        background: linear-gradient(135deg, #10233f, #174c76);
        padding: 4rem 3rem;
        border-radius: 24px;
        color: white;
        margin: 1.5rem 0 2rem 0;
    }

    .hero h1 {
        font-family: 'Manrope', sans-serif;
        font-size: clamp(2.2rem, 5vw, 3.8rem);
        font-weight: 800;
        line-height: 1.12;
        color: white;
        margin-bottom: 1rem;
    }

    .hero p {
        color: #e2eaf5;
        font-size: 1.1rem;
        line-height: 1.8;
        max-width: 720px;
    }

    .eyebrow {
        color: #93c5fd;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .section-title {
        color: var(--navy);
        font-family: 'Manrope', sans-serif;
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 0.4rem;
    }

    .section-subtitle {
        color: var(--muted);
        line-height: 1.8;
        margin-bottom: 1.5rem;
    }

    .service-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 1.4rem;
        min-height: 185px;
        margin-bottom: 1rem;
    }

    .service-card h3 {
        color: var(--navy);
        font-size: 1.12rem;
        font-weight: 700;
    }

    .service-card p {
        color: var(--muted);
        line-height: 1.7;
    }

    .about-panel {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 1.7rem;
        line-height: 1.8;
    }

    .contact-panel {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 1.5rem;
    }

    .footer {
        text-align: center;
        color: #64748b;
        padding: 2rem 0 0.5rem 0;
        font-size: 0.9rem;
    }

    div.stButton > button[kind="primary"],
    div.stFormSubmitButton > button[kind="primary"] {
        background: var(--blue);
        border: 0;
        border-radius: 10px;
        font-weight: 700;
        min-height: 45px;
    }

    @media (max-width: 640px) {
        .hero {
            padding: 2.2rem 1.3rem;
            border-radius: 16px;
        }

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# HEADER AND NAVIGATION
# --------------------------------------------------
header_left, header_right = st.columns([2, 3])

with header_left:
    st.markdown(
        '<div class="brand">🦫 Beaver Research & Automation</div>',
        unsafe_allow_html=True,
    )

with header_right:
    nav1, nav2, nav3, nav4 = st.columns(4)

    with nav1:
        st.markdown("[Home](#home)")

    with nav2:
        st.markdown("[Services](#services)")

    with nav3:
        st.markdown("[About](#about)")

    with nav4:
        st.markdown("[Contact](#contact)")


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.markdown(
    """
    <div class="hero" id="home">
        <div class="eyebrow">Research · Technology · Automation</div>
        <h1>Smarter Research.<br>Better Automation.</h1>
        <p>
            Beaver Research & Automation helps organizations streamline
            workflows, turn information into insights, and use technology
            to solve practical business problems.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

hero_button_left, hero_button_right = st.columns([1, 5])

with hero_button_left:
    if st.button("Discuss a Project", type="primary"):
        st.session_state["show_contact"] = True

if st.session_state.get("show_contact", False):
    st.info("Scroll down to the contact form to tell us about your project.")


# --------------------------------------------------
# SERVICES
# --------------------------------------------------
st.markdown(
    '<div id="services" class="section-title">Our Services</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-subtitle">'
    'Practical research and automation solutions tailored to your goals.'
    '</div>',
    unsafe_allow_html=True,
)

service_columns = st.columns(3)

services = [
    (
        "🔬",
        "Research & Analysis",
        "Research support, data gathering, structured analysis, "
        "and clear reporting to support better decisions.",
    ),
    (
        "⚙️",
        "Workflow Automation",
        "Reduce repetitive tasks and improve operational efficiency "
        "with practical automation solutions.",
    ),
    (
        "📊",
        "Data & Insights",
        "Organize data, identify meaningful patterns, and turn "
        "complex information into useful insights.",
    ),
    (
        "💻",
        "Web & Digital Solutions",
        "Build practical digital tools and web-based workflows "
        "that support your business processes.",
    ),
    (
        "🧩",
        "Process Improvement",
        "Identify workflow bottlenecks and design more consistent, "
        "efficient ways of working.",
    ),
    (
        "🤝",
        "Custom Projects",
        "Discuss your specific requirements and explore a solution "
        "built around your organization's needs.",
    ),
]

for index, (emoji, title, description) in enumerate(services):
    with service_columns[index % 3]:
        st.markdown(
            f"""
            <div class="service-card">
                <div style="font-size:1.8rem">{emoji}</div>
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# --------------------------------------------------
# ABOUT
# --------------------------------------------------
st.markdown(
    '<div id="about" class="section-title">About Beaver</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="about-panel">
        <p>
            Beaver Research & Automation focuses on combining thoughtful
            research, structured problem-solving, and practical technology.
        </p>
        <p>
            Our goal is to help clients reduce manual effort, understand
            their information more clearly, and develop solutions that
            fit their real-world requirements.
        </p>
        <p>
            Every project starts with understanding the problem, defining
            the desired outcome, and identifying a sensible path forward.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")


# --------------------------------------------------
# CONTACT FORM
# --------------------------------------------------
st.markdown(
    '<div id="contact" class="section-title">Let’s Talk About Your Project</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-subtitle">
        Tell us what you are working on. Your inquiry will be saved
        securely to our database, and we will be notified by email
        when notification delivery is configured correctly.
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container(border=True):
    with st.form("client_inquiry_form", clear_on_submit=False):
        st.subheader("Project Inquiry")

        col1, col2 = st.columns(2)

        with col1:
            full_name = st.text_input(
                "Full name *",
                placeholder="Your name",
                max_chars=150,
            )

            email = st.text_input(
                "Email address *",
                placeholder="you@example.com",
                max_chars=254,
            )

            phone = st.text_input(
                "Phone number",
                placeholder="Optional",
                max_chars=50,
            )

        with col2:
            organization = st.text_input(
                "Organization",
                placeholder="Company or organization",
                max_chars=200,
            )

            service = st.selectbox(
                "Service required *",
                options=[
                    "Research & Analysis",
                    "Workflow Automation",
                    "Data & Insights",
                    "Web & Digital Solutions",
                    "Process Improvement",
                    "Custom Project",
                ],
            )

            budget_range = st.selectbox(
                "Estimated budget",
                options=[
                    "Not decided",
                    "Under $500",
                    "$500–$1,000",
                    "$1,000–$5,000",
                    "$5,000+",
                ],
            )

        project_details = st.text_area(
            "Tell us about your project *",
            placeholder=(
                "What are you trying to achieve? "
                "What problem would you like us to solve?"
            ),
            height=160,
            max_chars=10000,
        )

        consent_to_contact = st.checkbox(
            "I agree that Beaver Research & Automation may contact me "
            "about this inquiry."
        )

        submitted = st.form_submit_button(
            "Submit Inquiry",
            type="primary",
            use_container_width=True,
        )

    if submitted:
        # ------------------------------------------
        # VALIDATION
        # ------------------------------------------
        if not full_name.strip():
            st.error("Please enter your full name.")

        elif not email.strip():
            st.error("Please enter your email address.")

        elif not service:
            st.error("Please select a service.")

        elif not project_details.strip():
            st.error("Please describe your project.")

        elif not consent_to_contact:
            st.error(
                "Please agree to be contacted about your inquiry."
            )

        else:
            try:
                validated_email = validate_email(
                    email.strip(),
                    check_deliverability=False,
                )
                clean_email = validated_email.normalized

            except EmailNotValidError:
                st.error("Please enter a valid email address.")

            else:
                # ----------------------------------
                # SAVE TO POSTGRESQL FIRST
                # ----------------------------------
                try:
                    save_inquiry(
                        full_name=full_name.strip(),
                        email=clean_email,
                        phone=phone.strip() or None,
                        organization=organization.strip() or None,
                        service=service,
                        budget_range=budget_range,
                        project_details=project_details.strip(),
                        consent_to_contact=consent_to_contact,
                    )

                except Exception:
                    st.error(
                        "We couldn't save your inquiry. "
                        "Please try again later."
                    )
                    st.info(
                        "If the problem continues, check the "
                        "application logs for the database error."
                    )

                else:
                    # ----------------------------------
                    # EMAIL NOTIFICATION
                    # ----------------------------------
                    try:
                        send_inquiry_notification(
                            full_name=full_name.strip(),
                            email=clean_email,
                            phone=phone.strip(),
                            organization=organization.strip(),
                            service=service,
                            budget_range=budget_range,
                            project_details=project_details.strip(),
                        )

                    except Exception:
                        # Database save succeeded, even though
                        # notification delivery may have failed.
                        st.success(
                            "Thank you! Your inquiry has been "
                            "submitted successfully."
                        )
                        st.warning(
                            "Your inquiry is saved, but the email "
                            "notification could not be sent. "
                            "Please check the email configuration "
                            "and application logs."
                        )

                    else:
                        st.success(
                            "Thank you! Your inquiry has been "
                            "submitted successfully."
                        )
                        st.info(
                            "Your message has been saved, and "
                            "the notification was accepted by "
                            "the email service."
                        )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown(
    """
    <div class="footer">
        <p><strong>Beaver Research & Automation</strong></p>
        <p>Research, technology, and automation for better work.</p>
        <p>© 2026 Beaver Research & Automation. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True,
)