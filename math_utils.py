def sum_values(numbers):
    """Menjumlahkan semua elemen dalam list angka."""
    return sum(numbers)


def fibonacci(n):
    """Mengembalikan bilangan fibonacci ke-n."""
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def bubble_sort(numbers):
    """Mengurutkan list secara ascending menggunakan algoritma bubble sort."""
    numbers = numbers.copy()
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers
