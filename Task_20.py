# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. Напишите программу, которая
# вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое
# содержит либо только английские, либо только русские буквы.

word = input('Input a word: ').strip().upper()
count = 0

dict_lists = {1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
              2: ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'], 3: ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'],
              4: ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'], 5: ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'], 8: ['J', 'X', 'Ш', 'Э', 'Ю'],
              10: ['Q', 'Z', 'Ф', 'Щ', 'Ъ']}

for a in word:
    for b in dict_lists:
        for c in dict_lists[b]:
            if a == c:
                count += b
print(f'Value of the word: {count}')