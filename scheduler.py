
import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='selam')

subject = "test"
body = "this is a test...."
recipient = "ymekeci@gmail.com"


message = {'recipient': recipient,'subject': subject, "body": body,}

# yukarıda aldığımız kanala bir iş gönderiyoruz
channel.basic_publish(exchange='',
                      routing_key='selam',
                      body=json.dumps(message))

print("Selam mesajı sıraya gönderildi.")

connection.close()