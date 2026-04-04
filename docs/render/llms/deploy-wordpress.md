# Source: https://render.com/docs/deploy-wordpress.md

# Deploy WordPress

[WordPress](https://wordpress.org) is an open source publishing platform that powers 34% of the web, from hobby blogs to the biggest online news sites. It has a robust [themes](https://wordpress.org/themes/) and [plugins](https://wordpress.org/plugins/) ecosystem and a worldwide community that continues to work towards making it one of the most flexible options for online publishing.

This guide shows how to deploy a WordPress instance on Render in just a few minutes. It uses [MySQL 8](/deploy-mysql) and a [Render disk](disks) for fast persistent storage for all your files. Render manages TLS certificates and custom domains for you, and you can easily add additional security and backups using the official [Jetpack](https://wordpress.org/plugins/jetpack/) plugin.

## One-Click Deploy

Click *Deploy to Render* below and follow the prompts to set up Wordpress on Render.

<deploy-to-render repo="https://github.com/render-examples/wordpress">
</deploy-to-render>

## Manual Deploy

1. [Set up a MySQL 8 instance](/deploy-mysql) on Render and make a note of the connection details. Make sure to select the `master` branch when you create your database. The database should be up in a few minutes. Wait for it to go live before moving to the next step.

2. Fork [render-examples/wordpress](https://github.com/render-examples/wordpress) on GitHub or click 'Use this template'.

3. Create a new *Web Service* on Render and give Render permission to access your new repo. Make sure the *Language* field is set to `Docker` and pick a name for your service.

4. Add the following environment variables to your web service:

   | Key                     | Value                                         |
   | ----------------------- | --------------------------------------------- |
   | `WORDPRESS_DB_HOST`     | MySQL hostname from above (e.g. `mysql-xyz0`) |
   | `WORDPRESS_DB_NAME`     | MySQL database name                           |
   | `WORDPRESS_DB_USER`     | MySQL database user                           |
   | `WORDPRESS_DB_PASSWORD` | MySQL database password                       |

5. Add a Disk under *Advanced* with the following values:

   |                |                                                      |
   | -------------- | ---------------------------------------------------- |
   | *Mount Path* | `/var/www/html`                                      |
   | *Size*       | `10 GB` Feel free to change this to suit your needs. |

That’s it! Save your web service to bring up WordPress. It will take a couple of minutes to start, but future deploys will be much faster.

Your WordPress instance will be available on your `.onrender.com` URL as soon as the deploy is live.

You can then configure WordPress by going to `https://your-subdomain.onrender.com` and start creating content for your new site!

[image: WordPress Welcome Screen]

## Backups

> Relying on a [disk snapshot](disks#disk-snapshots) to restore a database is not recommended. Restoring a disk snapshot will likely result in corrupted or lost database data.

Using a database’s recommended backup tool (for example: [mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html)) is the recommended way to backup and restore a database without corrupted or lost data.

## Custom Domains for WordPress

Render makes it easy to add a custom domain to your WordPress site, with free and fully managed TLS certificates. Follow the [Render custom domains](custom-domains) guide to add a domain to your site.

If you add a custom domain, make sure to add the *primary domain* under the *General Settings* tab in your WordPress Admin Panel.

[image: WordPress Domain]

## WordPress Plugins

Use your WordPress admin dashboard to install plugins. As a starting point, we recommend the following plugins:

- [Jetpack](https://wordpress.org/plugins/jetpack/) for added security and performance.
- [Akismet Anti-Spam](https://wordpress.org/plugins/akismet/) to manage comment spam.
- [Yoast SEO](https://wordpress.org/plugins/wordpress-seo/) for optimizing your site for search engines.

## Sending Mail from WordPress

Install the free [WPMail SMTP](https://wordpress.org/plugins/wp-mail-smtp/) plugin and configure it with a service like [Mailgun](https://www.mailgun.com) which allows up to 10,000 emails per month for free.

[image: Mailgun for WordPress]