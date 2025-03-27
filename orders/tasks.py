from django.conf import settings
from django.core.mail import EmailMessage
from orders.models import Order
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def sent_email_after_order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Заказ №{order_id} от {order.created_at.strftime("%d.%m.%Y %H:%M")}'
    message = (f'Уважаемый(ая), {order.first_name}!\n'
               f'Ваш эаказ №{order_id} успешно оформлен!\n!'
               f' На сумму {order.get_total_cost()}')
    mail_sent = send_mail(subject, message, settings.EMAIL_HOST_USER, [order.email])
    return mail_sent

