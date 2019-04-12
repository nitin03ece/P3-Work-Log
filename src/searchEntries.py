import entry
import datetime
import inputStr
import json
import read
import write
import copy
import re


# For displaying current log on the screen
def display_log(data):
    inputStr.clear_screen()
    for key, val in data.items():
        if key != 'Notes':
            if key == 'Time Spent':
                print(key + ": " + str(val) + " minutes,")
            else:
                print(key + ": " + str(val) + ",")
        else:
            print(key + ": " + str(val) + ".")

# The function displays various log entries matching the input
# provide by the user. Also provides option to navigate through
# the different log along with edit and delete option.
def main_Search(list_value):
    index = 0
    prompt_option = ""
    while True:
        if len(list_value):
            data = list_value[index]
            display_log(data)
            print("\nResult " +
                str(list_value.index(data)+1) +
                " of " + str(len(list_value)) +
                "\n")

            prompt_option = input(inputStr.search_by_date_option).strip().lower()
            if prompt_option == 'n':
                index += 1
                if index >= len(list_value):
                    index = 0
            elif prompt_option == 'p':
                index -= 1
                if index < 0:
                    index = len(list_value)-1
            elif prompt_option == 'e':
                edit = delete_edit(data, 'edit')
                if edit == 'exit':
                    return "exit"
                print("Editing Complete!")
                if input("Press Enter to go back ").strip() == "":
                    return "edit"
            elif prompt_option == 'd':
                delete_edit(data, 'delete')
                print("Successfully deleted!")
                if input("Press Enter to go back ").strip() == "":
                    return "delete"
            elif prompt_option == 'r':
                return "exit"
            else:
                pass
        else:
            input("No logs found. Press enter to continue ")
            break
            

# This function edit or delete a specific record.
def delete_edit(data, option):
    rows = read.csvRead()
    temp = copy.copy(data)
    if option == 'delete':
        rows.remove(data)
        write.csvWrite(rows)
    elif option == 'edit':
        flag = True
        while flag:
            display_log(data)
            prompt = input(inputStr.edit_data)
            if prompt == 'a':
                while True:
                    try:
                        datePrompt = str(datetime.datetime.strptime(
                            input(inputStr.datePrompt),
                            "%d/%m/%Y").date())
                    except ValueError as val:
                        value = str(val).split(" ")
                        print("Error: {} is not a valid date".format(value[2]))
                        if "" == input("Press Enter to Try Again ").strip():
                            pass
                    else:
                        data['Date'] = datePrompt
                        flag = False
                        break

            elif prompt == 'b':
                titlePrompt = input(inputStr.titlePrompt)
                data['Title'] = titlePrompt
                flag = False

            elif prompt == 'c':
                timePrompt = input(inputStr.timePrompt)
                data['Time Spent'] = timePrompt
                flag = False

            elif prompt == 'd':
                notesPrompt = input(inputStr.notesPrompt)
                data['Notes'] = notesPrompt
                flag = False

            elif prompt == 'e':
                flag = False
                return "exit"

        # Update the edited data back into the file
        index = rows.index(temp)
        rows[index] = data
        write.csvWrite(rows)

# This Function takes the date as an input and 
# provides the log(s) relevant to the date provided
def search_by_date():
    while True:
        inputStr.clear_screen()
        try:
            prompt = str(datetime.datetime.strptime(input(
                inputStr.search_by_date),
                "%d/%m/%Y").date())
        except ValueError as val:
            value = str(val).split(" ")
            print("Error: {} is not a valid date".format(value[2]))
            if "" == input("Press Enter to Try Again ").strip():
                pass
        else:
            rows = read.csvRead()
            list_value = []
            for row in rows:
                if row['Date'] == prompt:
                    list_value.append(row)

            option = main_Search(list_value)
            if option == 'exit':
                return
            elif option == 'edit':
                return
            elif option == 'delete':
                return

# This Function takes the start date and end date as an input and 
# provides the log(s) relevant to the date range provided
def search_by_date_range():
    while True:
        inputStr.clear_screen()
        try:
            start_date = datetime.datetime.strptime(input(
                inputStr.search_by_date_range_start),
                "%d/%m/%Y").date()
            end_date = datetime.datetime.strptime(input(
                inputStr.search_by_date_range_end),
                "%d/%m/%Y").date()
        except ValueError as val:
            value = str(val).split(" ")
            print("Error: {} is not a valid date".format(value[2]))
            if "" == input("Press Enter to Try Again ").strip():
                pass
        else:
            rows = read.csvRead()
            list_value = []
            for row in rows:
                row_date = datetime.datetime.strptime(
                    row['Date'],
                    "%Y-%m-%d").date()
                if (row_date >= start_date and row_date <= end_date):
                    list_value.append(row)

            option = main_Search(list_value)
            if option == 'exit':
                return
            elif option == 'edit':
                return
            elif option == 'delete':
                return

# This Function takes the string and provide the log with matched string
def search_by_exactSearch():
    inputStr.clear_screen()
    prompt = input(inputStr.search_by_exactSearch).strip().lower()
    rows = read.csvRead()
    list_value = []
    for row in rows:
        data_title = str(row["Title"])
        data_notes = str(row["Notes"])

        if data_title.lower().find(prompt) != -1:
            list_value.append(row)
        elif data_notes.lower().find(prompt) != -1:
            list_value.append(row)
        else:
            pass

    option = main_Search(list_value)
    if option == 'exit':
        return
    elif option == 'edit':
        return
    elif option == 'delete':
        return

# This Function takes the regex string and provide the log with matched string
def search_by_Regex():
    inputStr.clear_screen()
    prompt = input(inputStr.search_by_exactSearch).strip().lower()
    rows = read.csvRead()
    list_value = []
    for row in rows:
        data_title = str(row["Title"])
        data_notes = str(row["Notes"])
        match_title = re.search(prompt, data_title)
        match_notes = re.search(prompt, data_notes)

        if match_title:
            list_value.append(row)
        elif match_notes:
            list_value.append(row)
        else:
            pass

    option = main_Search(list_value)
    if option == 'exit':
        return
    elif option == 'edit':
        return
    elif option == 'delete':
        return

# Main function for searching the old entries.
def search_old_entries():
    while True:
        inputStr.clear_screen()
        prompt = input(inputStr.searchEntry).strip()
        if prompt == 'a':
            inputStr.clear_screen()
            search_by_date()

        elif prompt == 'b':
            inputStr.clear_screen()
            search_by_date_range()

        elif prompt == 'c':
            inputStr.clear_screen()
            search_by_exactSearch()

        elif prompt == 'd':
            inputStr.clear_screen()
            search_by_Regex()

        elif prompt == 'e':
            return
