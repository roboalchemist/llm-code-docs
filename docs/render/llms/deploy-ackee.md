# Source: https://render.com/docs/deploy-ackee.md

# Deploy Ackee

[Ackee](https://ackee.electerious.com/) is a self-hosted Node.js based analytics tool for users who care about privacy. It is easy to set up and features an intuitive and minimal interface.

[image: Ackee Dashboard Screenshot]

You can host your own Ackee instance on Render in just a few minutes. Once it's live you will be able to log in and get a JavaScript snippet that you can add to any website to get instant access to detailed, real-time analytics.

## One-Click Deploy

Click *Deploy to Render* below and follow the prompts to set up Ackee on Render.

<deploy-to-render repo="https://github.com/render-examples/ackee">
</deploy-to-render>

Once your deploy is finished, visit the URL for your service to login to Ackee. You can get your login credentials from the `ACKEE_USERNAME` and `ACKEE_PASSWORD` environment variables in the *Environment* tab of your service. By default, your username will be `render` and your password will be a randomly generated string.

## Manual Deploy

### Create a MongoDB Instance

Set up a new [MongoDB instance](/deploy-mongodb) on Render. The database should be up in a few minutes; wait for it to go live before deploying Ackee.

### Deploy Ackee

1. Fork [render-examples/ackee](https://github.com/render-examples/ackee) on GitHub or click `Use this template`.

2. Create a new *Web Service* on Render and give Render's GitHub app permission to access your new repository. Make sure the *Language* field is set to `Docker` and pick a name for your Ackee instance.

3. Add the following environment variables to your web service:

   | Key                  | Value                                                                                  |
   | -------------------- | -------------------------------------------------------------------------------------- |
   | `MONGODB_HOSTPORT`   | MongoDB hostname and port, for example: `mongodb-123c:27107`                           |
   | `MONGODB_DATABASE`   | `ackee`                                                                                |
   | `ACKEE_USERNAME`     | the username for logging in to Ackee (the one-click deploy uses `render` as a default) |
   | `ACKEE_PASSWORD`     | your Ackee password (auto-generated in one-click deploys)                              |
   | `ACKEE_PORT`         | `80`                                                                                   |
   | `ACKEE_ALLOW_ORIGIN` | `*`                                                                                    |

> Ackee uses the `Access-Control-Allow-Origin` header to restrict the sites that can send data to your Ackee instance. We're using a wildcard (`*`) in this example but recommend updating the value of `ACKEE_ALLOW_ORIGIN` once you know the domains you're tracking with Ackee. See [Ackee docs](https://docs.ackee.electerious.com/#/docs/CORS%20headers#heroku-or-platforms-as-a-service-configuration) for details.

That’s it! Save your web service to bring up Ackee. It will take a couple of minutes to start but future deploys will be much faster.

Your Ackee instance will be available on your `.onrender.com` URL as soon as the first deploy is live. Go to `https://your-subdomain.onrender.com`, log in using the values for `ACKEE_USERNAME` and `ACKEE_PASSWORD` above and start using Ackee!