# Laravel Scout guide
Source: https://www.meilisearch.com/docs/guides/laravel_scout

Learn how to use Meilisearch with Laravel Scout.

In this guide, you will see how to setup [Laravel Scout](https://laravel.com/docs/10.x/scout) to use Meilisearch in your Laravel 10 application.

## Prerequisites

Before you start, make sure you have the following installed on your machine:

* PHP
* [Composer](https://getcomposer.org/)

You will also need a Laravel application. If you don't have one, you can create a new one by running the following command:

```sh theme={null}
composer create-project laravel/laravel my-application
```

## Installing Laravel Scout

Laravel comes with out-of-the-box full-text search capabilities via Laravel Scout.

To enable it, navigate to your Laravel application directory and install Scout via the Composer package manager:

```sh theme={null}
composer require laravel/scout
```

After installing Scout, you need to publish the Scout configuration file. You can do this by running the following `artisan` command:

```sh theme={null}
php artisan vendor:publish --provider="Laravel\Scout\ScoutServiceProvider"
```

This command should create a new configuration file in your application directory: `config/scout.php`.

## Configuring the Laravel Scout driver

Now you need to configure Laravel Scout to use the Meilisearch driver. First, install the dependencies required to use Scout with Meilisearch via Composer:

```sh theme={null}
composer require meilisearch/meilisearch-php http-interop/http-factory-guzzle
```

Then, update the environment variables in your `.env` file:

```sh theme={null}
SCOUT_DRIVER=meilisearch