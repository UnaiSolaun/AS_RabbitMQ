import pika

def callback(ch, method, properties, body):
    print(" [x] Received %s" %body)
    connection.close()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
channel.start_consuming()

