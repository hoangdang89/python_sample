# Created by Evcheto Novakova

import re

""" Enter text and if the text contains e-mails the program will show them as output. """

def find_email_in_text(plain_text):
    pattern = r"([\w\.-]+)(\@[\w\.-]+)(\.[\w]+)"
    match = re.findall(pattern, plain_text)
    found_emails_list = []
    if match:
        for char in match:
            char_list = list(char)
            email = "".join(char_list)
            found_emails_list.append(email)
        return found_emails_list
    else:
        return 0
        
text = input()
print(find_email_in_text(text))
