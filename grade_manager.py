import json
import os
from student import Student


class GradeManager:
    """Manages a collection of students and persists them to JSON."""

    def __init__(self, filename: str = "grades.json"):
        self.filename = filename
        self.students: dict[str, Student] = {}
        self.load()

    # ---------- Persistence ----------
    def load(self) -> None:
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    self.students = {
                        sid: Student.from_dict(s) for sid, s in data.items()
                    }
            except (json.JSONDecodeError, KeyError) as e:
                print(f"⚠️  Could not load data: {e}. Starting fresh.")
                self.students = {}

    def save(self) -> None:
        with open(self.filename, "w") as f:
            json.dump(
                {sid: s.to_dict() for sid, s in self.students.items()},
                f,
                indent=4,
            )

    # ---------- Core Operations ----------
    def add_student(self, student_id: str, name: str) -> bool:
        if student_id in self.students:
            return False
        self.students[student_id] = Student(student_id, name)
        self.save()
        return True

    def remove_student(self, student_id: str) -> bool:
        if student_id in self.students:
            del self.students[student_id]
            self.save()
            return True
        return False

    def get_student(self, student_id: str) -> Student | None:
        return self.students.get(student_id)

    def list_students(self) -> list[Student]:
        return list(self.students.values())

    def class_average(self) -> float:
        if not self.students:
            return 0.0
        return round(
            sum(s.average() for s in self.students.values()) / len(self.students), 2
        )

    def top_student(self) -> Student | None:
        if not self.students:
            return None
        return max(self.students.values(), key=lambda s: s.average())