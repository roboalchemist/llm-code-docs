# Source: https://render.com/docs/deploy-rabbitmq.md

# Deploy RabbitMQ on Render

[RabbitMQ](https://www.rabbitmq.com/) is one of the most popular open source message brokers and queues. It supports multiple messaging protocols like AMQP and MQTT, and can be deployed in clustered configurations to meet high availability and throughput needs.

Render makes it effortless to run RabbitMQ complete with RabbitMQ's management interface and [persistence](https://redis.io/topics/persistence) so your data is always protected against restarts and failures.

Render automatically discovers all available ports on your RabbitMQ service and only exposes the HTTP management port outside your private Render network. This way you can connect to RabbitMQ from any of your applications on Render but no one else will be able to connect to it. Let's set it up!

## Deployment

1. Fork [render-examples/rabbitmq](https://github.com/render-examples/rabbitmq) on GitHub or click the green 'Use this template' button.

2. Create a new *Web Service* on Render, and give Render permission to access your new repo. If you don't want to expose the HTTP management interface, you can choose to create a *Private Service* instead.

3. Make sure the *Language* field is set to `Docker`, and enter a name for the service.

4. Add the following environment variables to your service:

   | Key                      | Value                                 |
   | ------------------------ | ------------------------------------- |
   | `RABBITMQ_ERLANG_COOKIE` | `your-secret-cookie-value`            |
   | `RABBITMQ_DEFAULT_USER`  | `rabbitmq` or your preferred username |
   | `RABBITMQ_DEFAULT_PASS`  | A strong password                     |

5. Add a Disk under *Advanced* with the following values:

   |                |                                                              |
   | -------------- | ------------------------------------------------------------ |
   | *Mount Path* | `/var/lib/rabbitmq`                                          |
   | *Size*       | `10 GB` Feel free to change this to match your requirements. |

Click *Save* and you're good to go! Once deployed, the RabbitMQ management interface will be available on your `.onrender.com` URL, and you will be able to use the username and the password you added above to log in.

Separately, RabbitMQ itself will be available on its default port `5672` and you can connect to it using the internal service hostname which is simply your service slug (`xyz` in `xyz.onrender.com`).