import tracker
def show_menu():
    print("\nWelcome to Workout Log!")
    print("1 Add Workouts")
    print("2 View All Workouts")
    print("3 View Summary")
    print("4 Exit")
def main():
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()
        if choice=="1":
            tracker.add_workout()
        elif choice=="2":
             tracker.view_all_workouts()
        elif choice=="3":
             tracker.summary_report()
        elif choice=="4":
                print("Goodbye!")
                break
        else:
                print("Invalid choice - Please enter 1-4.")
main()


