import os
from io import BytesIO
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def generate_order_pdf(order):
    pass