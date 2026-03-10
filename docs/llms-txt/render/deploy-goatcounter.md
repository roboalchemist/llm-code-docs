# Source: https://render.com/docs/deploy-goatcounter.md

# Deploy GoatCounter

[GoatCounter](https://www.goatcounter.com/) is an open-source web analytics platform that is *free for non-commercial use* and available as a hosted service or self-hosted app. It respects the user's privacy and has a simple, easy-to-use interface. In order to deploy GoatCounter on Render, you can either use the [One-Click Deploy](#one-click-deploy) button or follow the [Manual Deploy](#manual-deploy) steps.

## One-Click Deploy

Click *Deploy to Render* below to set up GoatCounter in your Render workspace.

<deploy-to-render repo="https://github.com/render-examples/goatcounter">
</deploy-to-render>

Then, on the deployment dashboard, enter values for the `GC_USER_EMAIL` and `GC_PASSWORD` environment variables to create your GoatCounter account.

That's it! Once the service is deployed, you can find the access URL on top of your service dashboard. Go to your `https://goatcounter-xyz.onrender.com` address, log in using the credentials you just provided and start using GoatCounter on Render!

## Manual Deploy

### Create a Database

Create a new [managed PostgreSQL](postgresql-creating-connecting) instance on Render. The database should be up in a few minutes; wait for it to go live before moving to the next step.

Note your database *internal database URL*; you will need it later.

### Deploy GoatCounter

1. Fork [render-examples/goatcounter](https://github.com/render-examples/goatcounter) on GitHub or click `Use this template`. Then, give Render's GitHub app permission to access your new repository.

2. Create a new *Web Service* on Render with your new repo. Make sure the *Language* field is set to `Docker` and pick a name for your service.

3. Add the following environment variables to your web service and click *Create Web Service* at the bottom of the page.

   | Key                    | Value                                                   |
   | ---------------------- | ------------------------------------------------------- |
   | `DB_CONNECTION_STRING` | *Internal Database URL* from your PostgreSQL database |
   | `DB_PASSWORD`          | *Password* from your PostgreSQL database              |
   | `DB_USER`              | *Username* from your PostgreSQL database              |
   | `DB_NAME`              | *Database* name from your PostgreSQL database         |
   | `GC_USER_EMAIL`        | your email (use for logging into GoatCounter)           |
   | `GC_PASSWORD`          | your password (use for logging into GoatCounter)        |

That's it! Your GoatCounter instance will be available on your `.onrender.com` URL as soon as your first deploy is live. Visit that address and start using GoatCounter.

[image: GoatCounter Welcome Screen]