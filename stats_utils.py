def calculate_statistics(numbers):
    """Menghitung total, rata-rata, maksimum, dan minimum dari list angka."""
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum


def square_each(numbers):
    """Mengkuadratkan setiap elemen dalam list."""
    return [n * n for n in numbers]


def filter_even(numbers):
    """Mengembalikan hanya elemen genap dari list."""
    return [n for n in numbers if n % 2 == 0]
