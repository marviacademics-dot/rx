from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens. import datetime
import csv
import os

file_name = "attendance.csv"

employees = {"101": {"name": "Ali", "rate": 10}, "102": {"name": "Sara", "rate": 12}}
attendance = {}  # emp_id -> {"in": datetime, "out": datetime}

# Create file with header if it doesn't exist
if not os.path.exists(file_name):
  with open(file_name, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Employee ID", "Name", "Check-In", "Check-Out", "Hours Worked", "Pay"])

def check_in(emp_id):
  if emp_id not in employees:
    print(f"Unknown employee ID: {emp_id}")
    return
  attendance[emp_id] = {"in": datetime.datetime.now()}
  print(f"{employees[emp_id]['name']} checked in at {attendance[emp_id]['in']}")

def check_out(emp_id):
  if emp_id not in employees:
    print(f"Unknown employee ID: {emp_id}")
    return
  if emp_id not in attendance or "in" not in attendance[emp_id]:
    print(f"{employees[emp_id]['name'] if emp_id in employees else emp_id} has not checked in.")
    return

  attendance[emp_id]["out"] = datetime.datetime.now()

  check_in_time = attendance[emp_id]["in"]
  check_out_time = attendance[emp_id]["out"]
  hours = (check_out_time - check_in_time).total_seconds() / 3600  # use total_seconds
  pay = hours * employees[emp_id]["rate"]

  print(f"{employees[emp_id]['name']} worked {hours:.2f} hours → Pay: ${pay:.2f}")

  # Append the completed record to CSV at check-out time
  with open(file_name, mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([emp_id, employees[emp_id]["name"], check_in_time.isoformat(timespec="seconds"), check_out_time.isoformat(timespec="seconds"), f"{hours:.2f}", f"{pay:.2f}", ])
if __name__ == "__main__":
  check_in("102")
  import time; time.sleep(3)  # simulate 3 seconds of work
  check_out("102")

if __name__ == "__main__":
  check_in("101")
  import time; time.sleep(3)  # simulate 3 seconds of work
  check_out("101")


# Example usage:
# check_in("101")
# ... time passes ...
# check_out("101")

