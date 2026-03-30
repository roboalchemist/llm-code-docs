# Source: https://render.com/docs/deploy-shynet.md

# Deploy Shynet

[Shynet](https://github.com/milesmcc/shynet) is an open-source cookie-free analytics tool that you can easily deploy on Render. Created with Django and a17t, it's intended for personal projects and small to medium size websites.

[image: Shynet Screenshot]

You can host your own Shynet instance on Render in just a few minutes. Once it's live you will be able to log in and get your JavaScript snippet. You can add it to any website to get instant access to detailed, real-time analytics.

## One-Click Deploy

Click *Deploy to Render* below to set up Shynet on Render.

<deploy-to-render repo="https://github.com/render-examples/shynet">
</deploy-to-render>

After deployment, use Render *Shell* to set up your account with those 3 commands:

1. Set your email with `./manage.py registeradmin your-email@example.com`. You will be prompted with a temporary password. Save it.
2. Set your whitelabel with `./manage.py whitelabel "Header for your Shynet site"`. It will be shown at the top of your Shynet site.
3. Update the `CSRF_TRUSTED_ORIGINS` environment variable to your deployed Render service domain.

You can now open your Shynet instance. You'll find your unique URL, that looks something like `https://your-shynet-domain.onrender.com`, at the top of your service dashboard. Log in with your email, and previously saved password and start using Shynet!

## Manual Deploy

Follow these steps to manually deploy Shynet on Render.

### Create a Database

Create a new [managed PostgreSQL](postgresql-creating-connecting) instance on Render. The database should be up in a few minutes; wait for it to go live before moving to the next step.

You'll need details from your database before you can deploy Shynet web service.

### Deploy Shynet

1. Fork [render-examples/shynet](https://github.com/render-examples/shynet) on GitHub or click `Use this template`.

2. Create a new *Web Service* on Render and give Render's GitHub app permission to access your new repository. Make sure the *Language* field is set to `Docker` and pick a name for your service.

3. Add the following environment variables to your web service:

   | Key                    | Value                                                |
   | ---------------------- | ---------------------------------------------------- |
   | `DB_NAME`              | `Database` variable from your newly created database |
   | `DB_HOST`              | `Hostname` variable from your newly created database |
   | `DB_PORT`              | `Port` variable from your newly created database     |
   | `DB_USER`              | `Username` variable from your newly created database |
   | `DB_PASSWORD`          | `Password` variable from your newly created database |
   | `CSRF_TRUSTED_ORIGINS` | Render service domain including scheme (`https://`)  |

   Save your web service to deploy Shynet on Render and wait for it to go live before continuing with the next step.

4. After deployment, use Render *Shell* to set up your account with the following commands:
   - Set your email with `./manage.py registeradmin your-email@example.com`. You will be prompted with a temporary password. Save it.
   - Set your whitelabel with `./manage.py whitelabel "Header for your Shynet site"`. It will be shown at the top of your Shynet site.

You can now open your Shynet instance. You'll find your unique URL, that looks something like `https://your-shynet-domain.onrender.com`, at the top of your service dashboard. Log in with your email, and previously saved password and start using Shynet!

[image: Shynet Welcome Screen]