def get_letter_grade(score):
    """Mengembalikan nilai huruf (A–E) berdasarkan skor."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"


def is_passing(score):
    """Menentukan apakah skor termasuk lulus (>= 70) atau tidak."""
    return score >= 70
