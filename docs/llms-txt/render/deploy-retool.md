# Source: https://render.com/docs/deploy-retool.md

# Deploy Retool

[Retool](https://retool.com) lets you build internal tools quickly. You can use building blocks like [Tables](https://retool.com/components#Table), [TextInputs](https://retool.com/components#TextInput), and [Dropdowns](https://retool.com/components#Select), read [data from PostgreSQL](https://docs.retool.com/docs/sql-queries), write back [via an API](https://docs.retool.com/docs/apis), read some more [data from Google Sheets](https://docs.retool.com/docs/google-sheets), query it via SQL, and [join it to data from Stripe](https://docs.retool.com/docs/google-sheets).

Retool supports multiple databases and any HTTP API. Follow their [quickstart](https://docs.retool.com/docs/quickstart) or learn more at [retool.com/docs](https://docs.retool.com/)

You can deploy Retool on Render in a single click using the button below.

<deploy-to-render repo="https://github.com/render-examples/retool">
</deploy-to-render>

This will install the latest stable version of Retool's [Docker image](https://github.com/tryretool/retool-onpremise) and a PostgreSQL database which is used to store Retool metadata.

> The database created in this step is <strong>not</strong> your application database. You will configure connections to your backend database and APIs after installation.

## Customizing Retool

The single-click deploy uses the [render-examples/retool](https://github.com/render-examples/retool) repository and a default [`render.yaml`](infrastructure-as-code) spec.

To customize Retool, fork the GitHub repository to your own account. If you choose to make your new repo is private, grant [Render's GitHub app](https://github.com/apps/render) access to it.

The Dockerfile in this repo uses the latest stable version of Retool by default:

```dockerfile
FROM tryretool/backend:latest
```

You can pin your Retool version by simply replacing `latest` with the desired version:

```dockerfile
FROM tryretool/backend:2.57.1
```

Commit and push your changes and Render will automatically upgrade and deploy your Retool instance.

### Getting a License Key

You will need a license key to run Retool on Render. You can get one by [registering for the Retool self-hosted beta](https://retool.com/self-hosted).

Once you have registered with Retool, you'll need to provide your Retool license key as the value of the `LICENSE_KEY` environment variable for your Retool Render instance, which then must be redeployed.

### Adding Google Login

1. Follow Retool's [instructions for creating a Google OAuth Client](https://github.com/tryretool/retool-onpremise#adding-google-login).

2. Add the environment variables below to `render.yaml` in your repo.

```yaml
- key: CLIENT_ID
  value: YOUR_GOOGLE_CLIENT_ID
- key: CLIENT_SECRET
  sync: false # update the value in your Render Dashboard
- key: RESTRICTED_DOMAIN
  value: yourcompany.com
```

> Make sure to never add your Google Client Secret (or any other secrets) to Git. In the snippet above you're instructing Render to create the `CLIENT_SECRET` environment variable with an empty value so you can update it in the Render Dashboard.
