import re

name = r"^[A-Z]['|a-z][A-Z|a-z]+($|\s[A-Z][a-z]+[-|a-z][A-Z|a-z]+)"
name_regex = re.compile(name)

phone_number = r"\W*[0-9]{3}\W*-?[0-9]{3}-?[0-9]{4}"
phone_regex = re.compile(phone_number)

email_address = r"^[a-z]+\.*[a-z|0-9]+@[a-z]+\.[a-z]+"
email_regex = re.compile(email_address)