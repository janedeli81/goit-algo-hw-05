import requests

# Змініть цю частину на ваш прямий URL для завантаження
download_url = "https://drive.google.com/uc?export=download&id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"

# Назва файлу, під якою ви хочете зберегти завантажений файл
output_file = "downloaded_file.txt"  # Замініть .ext на відповідне розширення файлу

# Виконуємо запит на завантаження
response = requests.get(download_url)

# Перевіряємо, що запит був успішним
if response.status_code == 200:
    # Записуємо вміст в файл
    with open(output_file, 'wb') as file:
        file.write(response.content)
    print(f"Файл успішно завантажено та збережено як {output_file}")
else:
    print("Помилка при завантаженні файлу")

