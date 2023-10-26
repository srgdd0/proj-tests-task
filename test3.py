import requests

# Список URL-адресов страниц, которые вы хотите протестировать
pages_to_test = [
    "https://webrpc.tech/",
    "https://webrpc.tech/share-app/",
]

# Пройдите по списку и проверьте каждую страницу
for page in pages_to_test:
    response = requests.get(page)
    if response.status_code == 200:
        print(f"Page {page} is accessible and returns status code 200.")
    else:
        print(f"Page {page} is not accessible. Received status code {response.status_code}.")
