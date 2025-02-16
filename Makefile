# v3.8.34
rabbitmq2:
	docker run -d -p 15672:15672 -p 5672:5672 --name rabbitmq rabbitmq:3.8-management
	# docker exec rabbitmq rabbitmq-plugins enable rabbitmq_management
