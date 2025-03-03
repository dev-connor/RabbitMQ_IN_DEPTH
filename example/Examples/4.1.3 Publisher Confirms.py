import rabbitpy


# Create a new queue object, passing in the channel to use
with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        exchange = rabbitpy.Exchange(channel, 'chapter4-example')
        exchange.declare()
        queue = rabbitpy.Queue(channel, 'example')

        # Declare the queue on the RabbitMQ server
        queue.declare()
        routing_key = 'important.message'
        queue.bind(exchange, routing_key)
        channel.enable_publisher_confirms()
        message = rabbitpy.Message(channel,
                                   'This is an important message',
                                   {'content_type': 'text/plain',
                                    'message_type': 'very important'})
        if message.publish('chapter4-example', routing_key):
            print('The message was confirmed')
