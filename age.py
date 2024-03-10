from datetime import datetime

birth_date_input = input(
    "please enter your birth date in the form DD-MM-YYYY ")

birth_date = datetime.strptime(birth_date_input, "%d-%m-%Y")

print(datetime.now().year - birth_date.year -
      (datetime.now().month < birth_date.month))
