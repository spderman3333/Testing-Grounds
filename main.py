from Greeting import Greetings
import time, os

def logo():
  print("Secure Login system")
  print()
  print("-------------------")
  print()

logo()
new_acc = input("""Do you want a new account? ⚠ (This will delete your old account!) ⚠ (Y or N): """).lower()
if new_acc == "y":
  confirm = ("Are you sure? (Y or N): ").lower()
  if confirm == "y":
    pass
  elif confirm == "n":
    pass
  else:
    print("Error: unknown command")
elif new_acc == "n":
  pass
else:
  print("Error: unknown command")