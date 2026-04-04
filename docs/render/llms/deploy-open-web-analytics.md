# Source: https://render.com/docs/deploy-open-web-analytics.md

# Deploy Open Web Analytics

[Open Web Analytics](http://www.openwebanalytics.com/) is an open-source web analytics framework that can be used as an alternative to commercial tools such as Google Analytics.

- Stay in control of the data you collect about your users.
- Run Open Web Analytics under your own domain or as part of your web application.
- Customize and extend Open Web Analytics to meet your needs.
- Track WordPress and MediaWiki based websites and admin events.
- Monitor your application with dozens of standard metrics, dimensions and reports.
- Integrate with external data sources using the extensive data access API.
- Remain compliant with GDPR and other privacy frameworks.

You can host an Open Web Analytics instance on Render in just a few minutes. Once it's live, you will be able to access your JavaScript snippet that can be added to any website to instantly record detailed, real-time analytics.

## One-Click Deploy

Click *Deploy to Render* below to deploy Open Web Analytics on Render.

<deploy-to-render repo="https://github.com/render-examples/open-web-analytics">
</deploy-to-render>

## Manual Deploy

Follow these steps to manually deploy Open Web Analytics on Render.

### Create a MySQL Database

[Set up a new MySQL 8 instance](/deploy-mysql) on Render. Make sure to deploy MySQL 8 by selecting the `master` branch. The database should be up in a few minutes. You'll need details from your MySQL database in order to deploy the Open Web Analytics app.

### Deploy Open Web Analytics

1. Fork [render-examples/open-web-analytics](https://github.com/render-examples/open-web-analytics) on GitHub or click `Use this template`.

2. Create a new *Web Service* on Render and give Render permission to access your new GitHub repository. Make sure the *Language* field is set to `Docker` and pick a name for your service.

3. Add the following environment variables to your web service:

   | Key               | Value                                         |
   | ----------------- | --------------------------------------------- |
   | `OWA_DB_HOST`     | The hostname from the MySQL database          |
   | `OWA_DB_NAME`     | The database name from the MySQL database     |
   | `OWA_DB_USER`     | The username from the MySQL database          |
   | `OWA_DB_PASSWORD` | The password from the MySQL database          |
   | `OWA_DB_PORT`     | '3306'                                        |
   | `OWA_AUTH_KEY`    | Click `Generate` to get a secure random value |
   | `OWA_AUTH_SALT`   | Click `Generate` to get a secure random value |
   | `OWA_NONCE_KEY`   | Click `Generate` to get a secure random value |
   | `OWA_NONCE_SALT`  | Click `Generate` to get a secure random value |

That’s it! Save your web service to deploy Open Web Analytics on Render. You can start using your Open Web Analytics service by going to `https://your-subdomain.onrender.com` as soon as your first deploy is live.

[image: Open Web Analytics Welcome Screen]