# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

path = "D:\Learn\GB\Разработчик\Python\Homework\HW5"

with open(path+"/text.txt", "r", encoding="utf-8") as data:
    dataText = data.read()

print("Получен следующий текст:\n" +
      "__________________________________________________\n")
print(dataText + "\n" + "__________________________________________________\n")

dataText = dataText.split()

#findText = str.lower(input("Введите текст для поиска: "))
findText = "абв"

resultTxt = []
for word in dataText:
    if str.lower(findText) not in str.lower(word):  # ищем независимо от регистра
        resultTxt.append(word)

resultTxt = " ".join(resultTxt)  # склеиваем обратно в текст

print("Текст после очистки: " + "\n" +
      "__________________________________________________\n")
print(resultTxt + "\n" + "__________________________________________________\n")

with open(path+"/ClearText.txt", "w", encoding="utf-8") as file:
    file.write(resultTxt)
