# Source: https://infisical.com/docs/integrations/frameworks/laravel.md

# Laravel

> How to use Infisical to inject environment variables and secrets into a Laravel app.

Prerequisites:

* Set up and add envars to [Infisical Cloud](https://app.infisical.com)
* [Install the CLI](/cli/overview)

## Initialize Infisical for your [Laravel](https://laravel.com/) app

```bash  theme={"dark"}
# navigate to the root of your of your project 
cd /path/to/project

# then initialize Infisical
infisical init
```

## Start your application as usual but with Infisical

```bash  theme={"dark"}
infisical run -- <your application start command>

# Example 
infisical run -- php artisan serve
```
