import re


def valid_name(name):
    return re.findall(r'^[+\s()\d-]*$', name)


print(valid_name("+7 499 456-45-78"))
print(valid_name("+74994564578"))
print(valid_name("7 (499) 456 45 78"))
print(valid_name("7 (499) 456-45-78"))
