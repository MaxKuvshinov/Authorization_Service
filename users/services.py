import string
import random
from smsaero import SmsAero
from config.settings import SMSAERO_API_KEY, SMSAERO_EMAIL


def generate_invite_code():
    """Функция генерации инвайт кода"""
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=6))


def send_sms(phone: int, message: str) -> dict:
    """Интеграция сервиса по отправке СМС кода."""
    api = SmsAero(SMSAERO_EMAIL, SMSAERO_API_KEY)
    return api.send_sms(phone, message)
