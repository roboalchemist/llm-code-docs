# Source: https://render.com/docs/deploy-ghost.md

# Deploy Ghost

[Ghost](https://ghost.org) is a free and open source publishing platform for building and running modern blogs, magazines, and journals.

This guide shows how to deploy a Ghost instance on Render in just a few minutes. This version uses a SQLite database stored on a [Render SSD Disk](disks) so your data is saved across deploys and automatically backed up with daily snapshots.

> As of Ghost 5, [MySQL 8](/deploy-mysql) is the only supported database for production deploys of Ghost. SQLite is only supported by Ghost 5 in a development environment.

## Manual Deploy

1. Fork [render-examples/ghost](https://github.com/render-examples/ghost) on GitHub or click 'Use this template'.

2. Create a new *Blueprint Instance* on Render, and give Render permission to access your new repo.

3. In your Render Dashboard, navigate to the *Environment* tab for your newly created MySQL Private Service.

4. Copy the generated value of the `MYSQL_PASSWORD` environment variable.

5. Navigate to the *Environment* tab for your newly created Ghost Web Service.

6. Create a new environment variable called `database__connection__password` with the value copied from the `MYSQL_PASSWORD` environment variable of the MySQL Private Instance.

7. Use the *Manual Deploy* button to deploy the latest commit to your Ghost Web Service.

That’s it! This initial deploy will take a few minutes in which Ghost will create the needed database entries. Subsequent deploys of Ghost will not need to do that and will be much quicker as a consequence.

Your Ghost instance will be available on your `.onrender.com` URL as soon as the deploy is live.

You can then configure Ghost by going to `https://your-subdomain.onrender.com/ghost` and start creating content for your new site!

## Custom Domains for Ghost

Render makes it easy to add a custom domain to your Ghost site, with free and fully managed TLS certificates. Follow the [Render custom domains](custom-domains) guide to add a domain to your site.

After adding and verifying your domain on Render, make sure to add the following environment variable to your Ghost service on Render. You can do this under the *Environment* tab.

| Key   | Value                        |
| ----- | ---------------------------- |
| `url` | `https://www.yourdomain.com` |

> The <strong>`url`</strong> should be set to the <strong>primary</strong> domain for your site. If your custom domain is set up to redirect `www` to the apex domain, set <strong>`url`</strong> to `https://yourdomain.com`.

See [Running Ghost with config env variables](https://ghost.org/docs/concepts/config/#running-ghost-with-config-env-variables) for more information.

## Sending Mail from Ghost

You can set up Ghost to send email using an external service like [Mailgun](https://www.mailgun.com) which allows up to 10,000 emails per month for free.

See https://ghost.org/docs/concepts/config/#mail for how to get Mailgun credentials for your Ghost domain.

Once you have your credentials, set up the following environment variables under the *Environment* tab to start sending mail from Ghost.

| Key                         | Value                            |
| --------------------------- | -------------------------------- |
| `mail__transport`           | `SMTP`                           |
| `mail__options__service`    | `Mailgun`                        |
| `mail__options__auth__user` | `postmaster@example.mailgun.org` |
| `mail__options__auth__pass` | `correct horse battery staple`   |

Render will automatically restart Ghost to apply your new settings.