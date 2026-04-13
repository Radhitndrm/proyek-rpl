from math_utils import fibonacci, bubble_sort, sum_values
from stats_utils import calculate_statistics
from grade_utils import get_letter_grade, is_passing


def main():
    angka = int(input("Masukkan angka: "))
    print(fibonacci(angka))

    numbers = [5, 3, 8, 1, 9, 2, 7, 4, 6]
    print(bubble_sort(numbers))

    total, average, maximum, minimum = calculate_statistics(numbers)
    print(f"total: {total}")
    print(f"rata-rata: {average}")
    print(f"maks: {maximum}")
    print(f"mins: {minimum}")

    score = 75
    grade = get_letter_grade(score)
    status = "lulus" if is_passing(score) else "tidak lulus"
    print(f"{grade} - {status}")

    print(sum_values([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()
