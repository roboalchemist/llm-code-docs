# Source: https://statamic.dev/starter-kits/updating-a-starter-kit.md

# Updating a Starter Kit

Starter Kits aren't all designed to be updatable, but when they are you'll need to know how.


## Not all starter kits are updatable

As their name implies, starter kits were originally intended to be a way to "start" a site. Once installed, you're on your own and can customize as you see fit.

However, some kits _are_ built in a way that they can be updated. Updatable kits will be noted on the Statamic Marketplace.

For example, the [Podcaster](https://statamic.com/starter-kits/statamic/podcaster) Kit is designed in an opinionated way, with settings for you to tweak brand colors. If a CSS or JavaScript bug is encountered one day, the developer of the Kit can fix it and you can simply pull down the update into your site.

## Performing updates

When initially installing an updatable Starter Kit, it will be left as a dependency in your `composer.json` file.

To update, you will need to update via Composer:

```shell
composer update
```

(Or `composer update vendor/starter-kit-name` to avoid updating everything else.)

Additionally, you may need to run additional commands to re-compile or publish assets. These should be explained in the Starter Kit's documentation, but would typically be something like this:

```shell
php artisan vendor:publish --tag=starter-kit-name
npm run dev
```
