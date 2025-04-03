import os
from io import BytesIO
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def generate_order_pdf(order):
    font_path = os.path.join(settings.BASE_DIR, settings.PDF_ORDER_FONT)
    pdfmetrics.registerFont(TTFont('DejaVu', font_path))
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)

    # оформление pdf-документа

    pdf.setFont('DejaVu', 24)
    pdf.drawString(100, 750, "Детали заказа:")
    pdf.setFont('DejaVu', 12)
    pdf.drawString(100, 700, f"№ заказа: {order.id}")
    pdf.drawString(100, 680, f"Клиент: {order.first_name} {order.last_name}")
    pdf.drawString(100, 660, f"Сумма к оплате: {order.get_total_cost():.2f} руб")
    pdf.save()
    buffer.seek(0)
    return buffer

