from datetime import datetime


def get_day_of_year():
    while True:
        # Step 1: Prompt the user for a date input
        date_str = input("Enter a date (e.g., February 14, 2025 or YYYY-MM-DD): ")

        try:
            # Step 2: Try parsing the input into a datetime object
            try:
                # - First, attempt to parse format "Month Day, Year"
                date_obj = datetime.strptime(date_str, "%B %d, %Y")
            except ValueError:
                # - If that fails, try "YYYY-MM-DD"
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")

            # Step 3: Extracting the day of the year
            day_number = date_obj.timetuple().tm_yday

            # Step 4: Get the weekday name
            weekday_name = date_obj.strftime("%A") # Example: Sunday

            # Step 5: Display the formatted result
            print(f"{weekday_name}, {date_obj.strftime('%B %d, %Y')} is day number {day_number} in the year.")
            break # Exit loop when a valid date is entered
            
        except ValueError:
            print("Invalid date format. Please enter a valid date.")

try:
    # Run the function
    get_day_of_year()
except KeyboardInterrupt: # Handle Ctrl+C
    # Print a friendly message
    print("\nGoodbye! Exiting the program.") 
