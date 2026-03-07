# tracker.py
import data

def view_all_workouts():
    """Prints each entry in a formatted list."""
    print("\n--- All Workouts ---")
    
    # Check if the list is empty first
    if len(data.workout_types) == 0:
        print("No workouts recorded yet.")
        return

    # Loop through the parallel lists and print each entry [cite: 37]
    for i in range(len(data.workout_types)):
        print(f"{i + 1}. {data.workout_types[i]} - {data.workout_durations[i]} mins")


def summary_report():
    """Shows total time, number of workouts, average, longest, and shortest duration."""
    print("\n--- Workout Summary ---")
    
    # Check if there is data to summarize to prevent division by zero errors
    if len(data.workout_durations) == 0:
        print("No data available for a summary.")
        return

    # Perform the required calculations [cite: 38, 72]
    num_workouts = len(data.workout_durations)
    total_time = sum(data.workout_durations)
    avg_duration = total_time / num_workouts
    longest = max(data.workout_durations)
    shortest = min(data.workout_durations)

    # Output the formatted statistics [cite: 38, 72]
    print(f"Total Workouts: {num_workouts}")
    print(f"Total Time Spent: {total_time} minutes")
    print(f"Average Duration: {avg_duration:.2f} minutes")
    print(f"Longest Workout: {longest} minutes")
    print(f"Shortest Workout: {shortest} minutes")