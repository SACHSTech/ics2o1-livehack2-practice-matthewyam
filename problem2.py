
print("What will I be doing during the summer")
print(" ")

mark = int(input("What your average?(Number only): "))
earnings_before_the_summer = int(input("How much money have you saved?: $"))

if mark >= 80 and earnings_before_the_summer >= 500:
  print("You can go to Europe!"")

elif mark >= 80  and earnings_before_the_summer < 500:
  print("You can go to California")

else:
  print("You cannot go anywhere")