# Source: https://render.com/docs/deploy-matomo.md

# Deploy Matomo

[Matomo](https://matomo.org/) (formerly Piwik) is an open-source analytics platform that focuses on user privacy and data ownership. It is a free alternative to Google Analytics and is already used on more than a million websites.

You can host your own Matomo instance on Render in just a few minutes. Once it's live you will be able to log in and get your JavaScript snippet that you can add to any website to get instant access to detailed, real-time analytics.

## One-Click Deploy

Click *Deploy to Render* below to deploy Matomo on Render.

<deploy-to-render repo="https://github.com/render-examples/matomo">
</deploy-to-render>

## Manual Deploy

The rest of this document explains how to set up Matomo on Render manually.

### Create a MySQL Database

[Set up a new MySQL 8 instance](/deploy-mysql) on Render. Make sure to select the `master` branch when you create your database so it uses MySQL 8. The database should be up in a few minutes; wait for it to go live before moving to the next step.

You'll need details from your MySQL private database service before you can deploy the Matomo web app.

### Deploy Matomo Server

1. Fork [render-examples/matomo](https://github.com/render-examples/matomo) on GitHub or click `Use this template`.

2. Create a new *Web Service* on Render and give Render's GitHub app permission to access your new repository. Make sure the *Language* field is set to `Docker` and pick a name for your service.

3. Add the following environment variables to your web service:

   | Key                        | Value                                         |
   | -------------------------- | --------------------------------------------- |
   | `MATOMO_DATABASE_HOST`     | MySQL hostname from above (e.g. `mysql-xyz1`) |
   | `MATOMO_DATABASE_DBNAME`   | MySQL database name                           |
   | `MATOMO_DATABASE_USERNAME` | MySQL database username                       |
   | `MATOMO_DATABASE_PASSWORD` | MySQL database password                       |

4. Add a Disk under *Advanced*:

   |                |                                                      |
   | -------------- | ---------------------------------------------------- |
   | *Mount Path* | `/var/www/html`                                      |
   | *Size*       | `20 GB` Feel free to change this to suit your needs. |

That’s it! Save your web service to deploy Matomo on Render. It will take a couple of minutes to start but future deploys will be much faster.

Your Matomo instance will be available on your `.onrender.com` URL as soon as your first deploy is live. You can configure it by going to `https://your-subdomain.onrender.com` and start using Matomo!

[image: Matomo Welcome Screen]