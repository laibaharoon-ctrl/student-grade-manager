class Student:
    """Represents a single student with grades."""

    def __init__(self, student_id: str, name: str, grades: dict = None):
        self.student_id = student_id
        self.name = name
        self.grades = grades if grades else {}

    def add_grade(self, subject: str, score: float) -> None:
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100.")
        self.grades[subject] = score

    def remove_grade(self, subject: str) -> bool:
        if subject in self.grades:
            del self.grades[subject]
            return True
        return False

    def average(self) -> float:
        if not self.grades:
            return 0.0
        return round(sum(self.grades.values()) / len(self.grades), 2)

    def letter_grade(self) -> str:
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        return "F"

    def to_dict(self) -> dict:
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grades": self.grades,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        return cls(data["student_id"], data["name"], data.get("grades", {}))

    def __str__(self) -> str:
        grades_str = ", ".join(f"{k}: {v}" for k, v in self.grades.items()) or "No grades"
        return (f"[{self.student_id}] {self.name} | "
                f"Avg: {self.average()} ({self.letter_grade()}) | {grades_str}")