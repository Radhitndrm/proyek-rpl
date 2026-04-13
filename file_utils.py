def save_to_file(data, filename, mode, encoding, separator):
    """Menyimpan data 2D ke file teks dengan pemisah kolom tertentu."""
    with open(filename, mode, encoding=encoding) as file:
        for row in data:
            line = separator.join(str(value) for value in row)
            file.write(line + "\n")
