from imgurpython import ImgurClient

client_id = '9a0dd52375bff8d'
client_secret = '8716b26491ad56c579bd204c26553d6d8258d9f2'

client = ImgurClient(client_id, client_secret)

# Example request
items = client.get_album_images('sY44H')
for item in items:
    print(item.link)
