from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_number: str) -> str:
    """
    Возвращает информацию о картах или счете с замаскированными номерами
    """
    if "счет" in type_number.lower():
        number_account = type_number[-20:]
        return f"Счет {get_mask_account(number_account)}"
    else:
        number_card = type_number[-16:]
        return f"{type_number[:-16]}{get_mask_card_number(number_card)}"


def get_date(date: str) -> str:
    """
    Функция возвращает дату в формате 'ДД.ММ.ГГГГ'
    """
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
