# Source: https://render.com/docs/deploy-php-laravel-docker.md

# Deploy a PHP Web App with Laravel and Docker

[Laravel](https://laravel.com) is one of the most popular web frameworks for PHP and for good reason. It comes bundled with most common web app needs, including authentication, authorization, localization, and support for multiple database backends including PostgreSQL.

In this guide, we're going to deploy a simple [Laravel 11](https://laravel.com/docs/11.x/releases) web app using Render's native [PostgreSQL](postgresql) and Docker support.

Let's get started!

1. [Create](https://dashboard.render.com/new/database) a new PostgreSQL database on Render and copy the internal DB URL to use below.

2. Fork [render-examples/php-laravel-docker](https://github.com/render-examples/php-laravel-docker) and create a new *Web Service* on Render, giving Render permission to access your forked repo.

3. Select `Docker` for the runtime, and add the following environment variables under the _Advanced_ section:

   | Key             | Value                                                             |
   | --------------- | ----------------------------------------------------------------- |
   | `DATABASE_URL`  | The *internal database URL* for the database you created above. |
   | `DB_CONNECTION` | `pgsql`                                                           |
   | `APP_KEY`       | Copy the output of `php artisan key:generate --show`              |

That's it! Your Laravel web app will be live on your Render URL as soon as the build finishes. You can test it out by registering and logging in.

## Modifying an Existing Laravel App for Render

The [commit history](https://github.com/render-examples/php-laravel-docker/commits/master) of our sample repo is useful in understanding the modifications needed for an existing Laravel app.

1. Force HTTPS on all assets served by Laravel to avoid mixed content warnings in the browser. Render already manages and terminates TLS certificates for you, but Laravel's [asset helper](https://laravel.com/docs/11.x/helpers#method-asset) needs to be configured to serve everything over TLS.

   You can do this in one of two ways:

   A. Set the [`ASSET_URL`](https://laravel.com/docs/11.x/vite#custom-base-urls) environment variable, _OR_

   B. Follow the changes in [Force HTTPS for Laravel](https://github.com/render-examples/php-laravel-docker/commit/27a895df86bc8604c7985af4649bcac8cd2ad1e8). In the end, the contents of `app/Providers/AppServiceProvider.php` would look something like this:

   ```php{3,24-29}
   namespace App\Providers;

   use Illuminate\Routing\UrlGenerator;
   use Illuminate\Support\ServiceProvider;

   class AppServiceProvider extends ServiceProvider
   {
       // ...

       public function boot(UrlGenerator $url)
       {
           if (env('APP_ENV') == 'production') {
               $url->forceScheme('https');
           }
       }
   }
   ```

2. Configure your repo to deploy Laravel using Docker and NGINX. We're building on the [nginx-php-fpm](https://gitlab.com/ric_harvey/nginx-php-fpm) Docker image as [shown here](https://github.com/render-examples/php-laravel-docker/commit/c4bc0ccc7b72554135fed30eb676c37e86a40e87#diff-3254677a7917c6c01f55212f86c57fbf), and adding [php-fpm configuration for NGINX](https://github.com/render-examples/php-laravel-docker/commit/c4bc0ccc7b72554135fed30eb676c37e86a40e87#diff-d3c89d8b2729af3493db888f6617630d) to tie everything together.

> Make sure to add the <a href=https://github.com/render-examples/php-laravel-docker/commit/c4bc0ccc7b72554135fed30eb676c37e86a40e87#diff-f7c5b4068637e2def526f9bbc7200c4e target="blank" rel="noopener noreferrer"> .dockerignore </a> file to your repo to avoid adding unnecessary or confidential information to your Docker image.

3. Finally, add [a deploy script](https://github.com/render-examples/php-laravel-docker/commit/c4bc0ccc7b72554135fed30eb676c37e86a40e87#diff-65731ecc61eedfe1b36a04ef6db2d866) that will be run when your PHP app starts up.

   ```bash
   #!/usr/bin/env bash
   echo "Running composer"
   composer install --no-dev --working-dir=/var/www/html

   echo "Caching config..."
   php artisan config:cache

   echo "Caching routes..."
   php artisan route:cache

   echo "Running migrations..."
   php artisan migrate --force
   ```

You should now be able to deploy your existing Laravel app on Render. If you need help, feel free to email as at <support@render.com>.