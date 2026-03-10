import data

def add_workout():

    workout = input("Enter workout type: ")
    if workout == "":
        print("Workout type cannot be empty.")
        return

    try:
        duration = int(input("Enter duration (minutes): "))

        if duration <= 0:
            print("Duration must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    data.workout_types.append(workout)
    data.duration.append(duration)    
            
            
def view_all_workouts():
    """Prints each entry in a formatted list."""
    print("\n--- All Workouts ---")
    
    # Check if the list is empty first
    if len(data.workout_types) == 0:
        print("No workouts recorded yet.")
        return

    # Loop through the parallel lists and print each entry
    for i in range(len(data.workout_types)):
        # Notice this now uses data.workout_minutes to match your summary function!
        print(f"{i + 1}. {data.workout_types[i]} - {data.workout_minutes[i]} mins")


def summary_report():
    """Shows total time, number of workouts, average, longest, and shortest duration."""
    # Check if the list is empty first
    if not data.workout_minutes:
        print("No workouts recorded yet.")
        return

    # Calculate all required statistics
    count = len(data.workout_minutes)
    total_minutes = sum(data.workout_minutes)
    average = total_minutes / count
    longest = max(data.workout_minutes)
    shortest = min(data.workout_minutes)

    # Output the formatted report
    print("\n--- Workout Summary ---")
    print(f"Total Workouts: {count}")
    print(f"Total Time Spent: {total_minutes} minutes")
    print(f"Average Duration: {average:.2f} minutes")
    print(f"Longest Workout: {longest} minutes")
    print(f"Shortest Workout: {shortest} minutes")