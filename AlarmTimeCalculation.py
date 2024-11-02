# Ask the user for the current time in hours (0-23)
current_time = int(input("Enter the current time (0-23): "))

# Validate the input
while current_time < 0 or current_time > 23:
    print("Invalid input. Please enter a number between 0 and 23.")
    current_time = int(input("Enter the current time (0-23): "))

# Ask the user for the number of hours to wait
wait_time = int(input("Enter the number of hours to wait: "))

# Calculate the alarm time
alarm_time = (current_time + wait_time) % 24

# Display the result
print(f"The alarm will go off at {alarm_time:02d}:00 on the 24-hour clock.")
