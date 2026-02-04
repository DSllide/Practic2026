import requests


get_url = "https://jsonplaceholder.typicode.com/posts/1"  # відкритий тестовий API
response_get = requests.get(get_url)

print("=== GET-запит ===")
print("Статус-код:", response_get.status_code)
print("Заголовки:", response_get.headers)
print("Тіло відповіді:", response_get.json())  # якщо JSON


post_url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "Привіт",
    "body": "Це тестовий пост",
    "userId": 1
}

response_post = requests.post(post_url, json=data)

print("\n=== POST-запит ===")
print("Статус-код:", response_post.status_code)
print("Заголовки:", response_post.headers)
print("Тіло відповіді:", response_post.json())
