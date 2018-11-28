import pika
import json
import smtplib


def send_email(user, pwd, recipient, subject, body):
    from_email = user
    to_email = recipient if isinstance(recipient, list) else [recipient]
    print("Sending email to ", to_email)

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
       """ % (from_email, ", ".join(to_email), subject, body)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(from_email, to_email, message)
        server.close()
        print("successfully sent the mail")
    except Error as e:
        print("failed to send mail", e)

def callback_handler(ch, method, properties, body):
    print("Message received: ", body)
    email_body =json.loads(body)
    from_email = "dimag.kahta@gmail.com"
    from_password = "11232018"
    print("Sending email to:", email_body['recipient'])
    send_email(from_email, from_password,email_body['recipient'], email_body['subject'], email_body['body'])

def create_channel(host, queue):
    print("Creating channel...")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    channel = connection.channel()
    channel.basic_consume(callback_handler, queue=queue, no_ack=True)
    return channel

def start(host, queue):
    channel = create_channel(host, queue)
    channel.start_consuming()



if __name__ == "__main__":
    print('Starting email email sender')
    start("localhost", "selam")

