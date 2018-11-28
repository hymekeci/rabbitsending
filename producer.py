import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='selam')


message  = {"subject": " Merhaba","body":" Bu mesajdir."}
print(json.dumps(message))
# yukarıda aldığımız kanala bir iş gönderiyoruz
channel.basic_publish(exchange='',
                      routing_key='selam',
                      body=json.dumps(message))

print("Selam mesajı sıraya gönderildi.")

connection.close()
