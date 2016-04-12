# -*- coding: utf-8 -*-

from flask import render_template
from flask.ext.mail import Message
from html2text import html2text
from premailer import transform as email_transform
from .models import Order
from . import mail, app


def send_receipt_email(order_id, subject="Thank you for your order!"):
    """
    Sends an invoice with a PDF attached, to the order's buyer
    """
    with app.test_request_context():
        order = Order.query.get(order_id)
        msg = Message(subject=subject, recipients=[order.buyer_email], bcc=[order.organization.contact_email])
        html = email_transform(render_template('cash_receipt.html', order=order, org=order.organization))
        msg.html = html
        msg.body = html2text(html)
        mail.send(msg)


def send_participant_assignment_mail(order_id, subject="Please tell us who's coming!"):
    with app.test_request_context():
        order = Order.query.get(order_id)
        msg = Message(subject=subject, recipients=[order.buyer_email], bcc=[order.organization.contact_email])
        html = email_transform(render_template('participant_assignment_mail.html', order=order, org=order.organization))
        msg.html = html
        msg.body = html2text(html)
        mail.send(msg)
