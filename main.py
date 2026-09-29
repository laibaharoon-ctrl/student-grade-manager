from grade_manager import GradeManager


MENU = """
╔══════════════════════════════════════╗
║     STUDENT GRADE MANAGER            ║
╠══════════════════════════════════════╣
║  1. Add student                      ║
║  2. Remove student                   ║
║  3. List all students                ║
║  4. Add grade to student             ║
║  5. Show student report              ║
║  6. Class statistics                 ║
║  7. Exit                             ║
╚══════════════════════════════════════╝
"""


def safe_float(prompt: str) -> float | None:
    try:
        return float(input(prompt))
    except ValueError:
        print("❌ Invalid number.")
        return None


def main() -> None:
    manager = GradeManager()

    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            sid = input("Student ID: ").strip()
            name = input("Student name: ").strip()
            if manager.add_student(sid, name):
                print(f"✅ Added {name}.")
            else:
                print("❌ Student ID already exists.")

        elif choice == "2":
            sid = input("Student ID to remove: ").strip()
            print("✅ Removed." if manager.remove_student(sid) else "❌ Not found.")

        elif choice == "3":
            students = manager.list_students()
            if not students:
                print("📭 No students yet.")
            for s in students:
                print("  " + str(s))

        elif choice == "4":
            sid = input("Student ID: ").strip()
            student = manager.get_student(sid)
            if not student:
                print("❌ Student not found.")
                continue
            subject = input("Subject: ").strip()
            score = safe_float("Score (0-100): ")
            if score is None:
                continue
            try:
                student.add_grade(subject, score)
                manager.save()
                print(f"✅ Added {subject}: {score}.")
            except ValueError as e:
                print(f"❌ {e}")

        elif choice == "5":
            sid = input("Student ID: ").strip()
            student = manager.get_student(sid)
            if student:
                print("\n" + "=" * 40)
                print(f"  Report for {student.name} ({student.student_id})")
                print("=" * 40)
                for subj, score in student.grades.items():
                    print(f"  {subj:<15} {score}")
                print("-" * 40)
                print(f"  Average: {student.average()}  |  Grade: {student.letter_grade()}")
                print("=" * 40 + "\n")
            else:
                print("❌ Student not found.")

        elif choice == "6":
            if not manager.students:
                print("📭 No data.")
                continue
            print(f"\n📊 Class average: {manager.class_average()}")
            top = manager.top_student()
            print(f"🏆 Top student: {top.name} ({top.average()})\n")

        elif choice == "7":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()