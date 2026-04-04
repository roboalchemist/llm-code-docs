# Source: https://render.com/docs/deploy-gotify.md

# Deploy Gotify on Render

[Gotify](https://gotify.net) is an open source push notifications server that lets you send messages via a REST API and create clients that subscribe to them using web sockets. You can deploy your own Gotify server on Render using the steps below.

1. Create a new [PostgreSQL database](postgresql) on Render. Set the *Name*, *Database*, and *User* to `gotify`.

2. Fork [render-examples/gotify-server](https://github.com/render-examples/gotify-server) and create a new *Web Service* on Render, giving Render permission to access your forked repo.

3. On the service creation page, add the following environment variable. Use the internal database hostname and password from the database you created earlier.

   | Key                          | Value                                                                                 |
   | ---------------------------- | ------------------------------------------------------------------------------------- |
   | `GOTIFY_DATABASE_CONNECTION` | `host=your-db-hostname port=5432 user=gotify dbname=gotify password=your-db-password` |

That's it! Your Gotify server will be available on your `onrender.com` URL in less than a minute. Don't forget to log in and change the admin password.

You can also add a [custom domain](custom-domains) to your service and Render will automatically issue and manage TLS certificates for your domain. Make sure to add the domain to the list of allowed origins in your [Gotify configuration file](https://gotify.net/docs/config#config-file).