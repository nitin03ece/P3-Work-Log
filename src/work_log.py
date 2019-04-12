import write
import inputStr
import addEntries
import searchEntries

# Main function to start the work log program
def start():
    while True:
        inputStr.clear_screen()
        print("WORK LOG")
        prompt = input(inputStr.prompt).strip().lower()
        if prompt == 'a':
            addEntries.add_new_entries()
        elif prompt == 'b':
            searchEntries.search_old_entries()
        elif prompt == 'c':
            inputStr.clear_screen()
            print("Thank You for using the work log program!")
            print("Come again soon.")
            break


if __name__ == "__main__":
    start()
