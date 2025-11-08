"""Character Limit
In this challenge, you are given a string and need to determine if it fits in a social media post. Return the following strings based on the rules given:

"short post" if it fits within a 40-character limit.
"long post" if it's greater than 40 characters and fits within an 80-character limit.
"invalid post" if it's too long to fit within either limit.
"""

# ** start of main.py **

def can_post(message):
    count = 0
    for char in message:
        count += 1
    
    if count < 40:
        message = "short post"
    elif count > 40 and count < 80:
        message = "long post"
    else:
        message = "invalid post"

    return message

# ** end of main.py **


# Tests
# 1. can_post("Hello world") should return "short post".
# 2. can_post("This is a longer message but still under eighty characters.") should return "long post".
# 3. can_post("This message is too long to fit into either of the character limits for a social media post.") should return "invalid post".


# Printing result
print(can_post("hello world"))
print(can_post("This is a longer message but still under eighty characters."))
print(can_post("This message is too long to fit into either of the character limits for a social media post."))