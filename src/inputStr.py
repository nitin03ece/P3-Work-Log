import os


prompt = """What would you like to do?
a) Add new entry
b) Search in existing entries
c) Quit Program
> """

taskDate = """Date of the task
Please use DD/MM/YYYY : """

taskTitle = "Title of the task: "

taskTime = "Time spent(rounded minutes): "

taskNotes = "Notes (Optional, you can leave this empty): "

searchEntry = """Do you want to search by:
a) Exact Date
b) Range of Dates
c) Exact Search
d) Regex Pattern
e) Return to menu
> """

search_by_date = """Search by Exact Date
Enter the date
Please use DD/MM/YYYY: """

search_by_date_range_start = """Search by Range of Dates
Enter the start date(DD/MM/YYYY): """

search_by_date_range_end = """Search by Range of Dates
Enter the end date(DD/MM/YYYY): """

search_by_date_option = """[N]ext, [P]revious, [E]dit, [D]elete, [R]eturn to search menu
> """

search_by_exactSearch = """Enter the search String: """

edit_data = """\nWhat would you like to edit?
a) Date
b) Title
c) Time Spent
d) Notes
e) exit
> """

datePrompt = """Edit Date
Enter Correct Date: """

titlePrompt = """Edit Title
Enter Correct Title: """

timePrompt = """Edit Time Spent
Enter Correct Time Spent: """

notesPrompt = """Edit Notes
Enter Correct Notes: """

nextEntries = """No Entries Further available!
Press Enter to start from Beginning"""

prevEntries = """No Entries Further available!
Press Enter to start from End"""


def clear_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.name("clear")
    pass
