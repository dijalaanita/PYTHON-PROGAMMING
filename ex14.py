from sys import argv

script, user_name = argv
prompt = '> '

print(f"hi {user_name}, i'm {script} script.")
print("i'd like to ask you some things.")
print(f"do you like me {user_name}?")
likes = input(prompt)

print(f"where do you stay {user_name}?")
lives = input(prompt)

print(f"what computer do you have {user_name}?")
comp = input(prompt)

print(f"""
      so you said {likes} to me liking me.
      you live in {lives}, no clue what that is.
      and you have a {comp} computer, cool!
      """)