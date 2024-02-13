import pika 
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def on_message_recieved(self, ch, method, properties, body):
        print(f'recieved new message: {body}')

    def handle(self, *args, **kwargs):
        connection_parameters = pika.ConnectionParameters('localhost')
        connection = pika.BlockingConnection(connection_parameters) 
        channel = connection.channel()
        channel.queue_declare(queue='upload')
        channel.basic_consume(queue='upload', auto_ack=True, 
                              on_message_callback=self.on_message_recieved)
        print('Starting Consuming')
        channel.start_consuming()
