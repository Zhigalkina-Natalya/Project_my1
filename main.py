from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

print(get_mask_card_number("1111222233334444"))
print(get_mask_account("11112222333344441234"))

print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Счет 73654108430135874305"))

print(get_date("2024-03-11T02:26:18.671407"))
print(get_date("2025-06-20T14:00:28.671407"))
