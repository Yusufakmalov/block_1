user1 = input("Enter your name: ")
user2 = input("Enter your name: ")
print(user1, "- is user 1,", "he chooses first")
print(user2, "- is user 2,", "he chooses second")
user_1 = input("Please enter paper, stone or scissor:")
user_2 = input("Please enter paper, stone or scissor:")


if user_1 == user_2:
  print("draw")
elif user_1 == "stone" and user_2 == "paper":
  print(user2, "won")
elif user_1 == "stone" and user_2 == "scissor":
  print(user1, "won")
elif user_1 == "scissor" and user_2 == "paper":
  print(user1, "won")
elif user_1 == "scissor" and user_2 == "stone":
  print(user2, "won")
elif user_1 == "paper" and user_2 == "stone":
  print(user1, "won")
elif user_1 == "paper" and user_2 == "scissor":
  print(user2, "won")
else:
  print(" Please write correctly: ")




