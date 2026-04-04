# Source: https://render.com/docs/deploy-adminer.md

# Deploy Adminer on Render

[Adminer](https://www.adminer.org/) is a lightweight database management tool for MySQL, MariaDB, PostgreSQL, SQLite, Elasticsearch, and more.

You can deploy Adminer on Render to easily manage your [PostgreSQL](postgresql), [MySQL](/deploy-mysql), and [Elasticsearch](/deploy-elasticsearch) instances.

## Deployment

1. Fork [render-examples/adminer](https://github.com/render-examples/adminer) on GitHub (or click the green 'Use this template' button).

2. Create a new *Web Service* on Render, and give Render permission to access your new repo.

3. Make sure the *Language* field is set to `Docker`, and enter a name for the service.

Click Save and you're good to go! When it's ready, your Adminer instance will be available at its unique `onrender.com` URL, and you can use it to connect to your private services on Render.

As an example, if your [MySQL database](/deploy-mysql) is set up as a private service with url `mysql-demo:3306` and username and database `mysql`, you can log in to it using the values below:

[image: Adminer Login Screen]

You will see your database in Adminer once you're logged in:

[image: Adminer UI]

You can also use Adminer to connect to other databases in your Render account. See [Adminer docs](https://www.adminer.org/en/) for details.

## Plugins

Adminer has a robust [plugin](https://www.adminer.org/en/plugins/) ecosystem. Render's Dockerfile includes the following plugins by default:

- [dump-alter](https://github.com/vrana/adminer/blob/master/plugins/dump-alter.php)
- [dump-json](https://github.com/vrana/adminer/blob/master/plugins/dump-json.php)
- [dump-zip](https://github.com/vrana/adminer/blob/master/plugins/dump-zip.php)
- [dump-bz2](https://github.com/vrana/adminer/blob/master/plugins/dump-bz2.php)
- [tables-filter](https://github.com/vrana/adminer/blob/master/plugins/tables-filter.php)

Add more plugins by changing the value of `ADMINER_PLUGINS` in your version of the Dockerfile. You can also override the default set of plugins by setting the `ADMINER_PLUGINS` environment variable for your Render service.

## Security

Because your Adminer URL is accessible over the internet, make sure to secure it with one of the following plugins:

- [Login IP](https://github.com/vrana/adminer/blob/master/plugins/login-ip.php)
- [Login OTP](https://github.com/vrana/adminer/blob/master/plugins/login-otp.php)
- [Login Table](https://github.com/vrana/adminer/blob/master/plugins/login-table.php)

These plugins need additional configuration described in [loading plugins](https://hub.docker.com/_/adminer/#loading-plugins) in the official Adminer Docker guide.