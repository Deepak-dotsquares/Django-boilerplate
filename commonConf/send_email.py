from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def send_email(to, context, template_name):
    """
    Sends an email using the provided template, subject, and context.

    Args:
        to (str): The recipient email address.
        context (dict): The context data to render the template.
        template_name (str): The name of the template to render.
    """
    html_content = render_to_string(template_name, context)
    msg = EmailMultiAlternatives(context['subject'], "", settings.DEFAULT_FROM_EMAIL, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def send_forgot_password_mail(to, context):
    template = 'email/forgot_password.html'
    send_email(to, context, template)


def send_welcome_mail(to, context):
    template = 'email/welcome_mail.html'
    send_email(to, context, template)


def send_welcome_mail_with_password(to, context):
    template = 'email/welcome_mail_with_password.html'
    send_email(to, context, template)
