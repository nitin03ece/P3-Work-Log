import entry
import datetime
import inputStr
import json
import write


# Write the new entries inside the log.
def log_new_entries(new_entry):
    entry = {
        'Date': str(new_entry.Date),
        'Title': new_entry.Title,
        'Time Spent': new_entry.Time_Spent,
        'Notes': new_entry.Notes
    }
    write.csvwriteReload(entry)

# This function takes details of a single entry and store it, 
# later to be logged.
def add_new_entries():
    # Collect the 'Date' of the task
    while True:
        inputStr.clear_screen()
        try:
            taskDate = str(datetime.datetime.strptime(
                input(inputStr.taskDate),
                "%d/%m/%Y").date()
            )
        except ValueError as val1:
            value = str(val1).split(" ")
            print("Error: {} is not a valid date".format(value[2]))
            if "" == input("Press Enter to Try Again ").strip():
                pass
        else:
            break

    # Collect the 'Title' of the task
    inputStr.clear_screen()
    taskTitle = input(inputStr.taskTitle)

    # Collect the 'Time' of the task
    while True:
        inputStr.clear_screen()
        try:
            taskTime = round(int(input(inputStr.taskTime)))
        except ValueError as val2:
            value2 = str(val2).split(" ")
            print("Error: {} is not the time value ".format(value2[-1]))
            if "" == input("Press Enter to Try Again ").strip():
                pass
        else:
            break

    # Collect the 'Notes' of the task
    inputStr.clear_screen()
    taskNotes = input(inputStr.taskNotes)

    inputStr.clear_screen()
    new_entry = entry.Entry(taskDate, taskTitle, taskTime, taskNotes)
    log_new_entries(new_entry)
    print("The entry has been added. Press enter to return to the menu.\n")
    return
