import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='selam')


def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
       """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print("successfully sent the mail")
    except Error as e:
        print("failed to send mail", e)

def callback_handler(ch, method, properties, body):

    print(body)
    email_body =json.loads(body)
    from_email = "dimag.kahta@gmail.com"
    from_password = "11232018"

    send_email(from_email, from_password,email_body['recipient'],email_body['subject'],email_body['body'])

if __name__ == "__main__":

    print('Sıraya bir mesaj gelmesi bekleniyor...')

    # parametreler vererek kanal üzerindeki işleri işlemeye başlıyoruz
    channel.basic_consume(callback_handler,
                          queue='selam',
                          no_ack=True)
    channel.start_consuming()