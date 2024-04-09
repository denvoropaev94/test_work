def sort_strings(strings):
    strings.sort(key=len)  # Сортировка по возрастанию
    print("По возрастанию: ", strings)
    strings.sort(key=len, reverse=True)  # Сортировка по убыванию
    print("По убыванию: ", strings)

# Пример использования:
strings = ["Ден", "Никитка", "Александр", "Олег", "Сергей"]
sort_strings(strings)