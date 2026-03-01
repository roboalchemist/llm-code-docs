# Source: https://fly.io/docs/laravel/

Title: Laravel on Fly.io

URL Source: https://fly.io/docs/laravel/

Markdown Content:
[Docs](https://fly.io/docs/)Laravel on Fly.io
![Image 1](https://fly.io/static/images/laravel-intro.webp)

Getting an application running on Fly.io is essentially working out how to package it as a deployable image. Once packaged, it can be deployed to the Fly.io platform.

In this guide we’ll learn how to deploy a [Laravel](https://laravel.com/) application on Fly.io.

For an overview of how to configure your application with services like caching, databases, and queues, reading through our [Full Stack Laravel](https://fly.io/laravel-bytes/full-stack-laravel/) post is the best place to start.

[](https://fly.io/docs/laravel/#prepare-a-laravel-app)Prepare a Laravel app
---------------------------------------------------------------------------

Bring your own Laravel app, or create a new one!

If you want to start fresh, here’s how to set up a new application. You’ll need PHP 8+ and [composer](https://getcomposer.org/) installed locally. You can check your PHP version using `php --version`.

```
composer create-project laravel/laravel fly-laravel
cd fly-laravel
php artisan serve
```

You should be able to visit `http://localhost:8000` and see the home page.

[](https://fly.io/docs/laravel/#deploy-to-fly-io)Deploy to Fly.io
-----------------------------------------------------------------

### [](https://fly.io/docs/laravel/#install-fly)Install Fly

First, [install flyctl](https://fly.io/docs/flyctl/install/), the Fly.io CLI, and [sign up to Fly.io](https://fly.io/docs/getting-started/sign-up-sign-in/#first-time-or-no-fly-account-sign-up-for-fly) if you haven’t already.

### [](https://fly.io/docs/laravel/#launch)Launch

Next, we’ll use the `launch` command to automagically configure your app for Fly and deploy it to the Fly cloud. This will add a few files to your code base–but, don’t worry, it will ask before overwriting anything.

**If you haven’t already, go ahead and run `fly launch`!**

```
fly launch
```

This would detect that your project is built with Laravel. Afterwhich it would provide a summary of the default configuration that would be given to your app.

```
We're about to launch your Laravel app on Fly.io. Here's what you're getting:

Organization: Personal                                                   (fly launch defaults to the personal org)
Name:         fly-lara-app                                               (derived from your directory name)
Region:       Paris, France                                              (this is the fastest region for you)
App Machines: shared-cpu-1x, 1GB RAM                                     (most apps need about 1GB of RAM)
Postgres:     <none>                                                     (not requested)
Redis:        Pay-as-you-go Plan: 10 GB Max Data Size, eviction disabled (determined from app source)
Tigris:       <none>                                                     (not requested)

? Do you want to tweak these settings before proceeding? (y/N)
```

Extensions like [Postgres](https://fly.io/docs/mpg/overview/) ( database ), [Redis](https://fly.io/docs/upstash/redis/) ( cache ), and [Tigris](https://fly.io/docs/tigris/#main-content-start) ( storage ) can also be added by default based on whether there’s an existing, similar connection found for your Laravel project.

**Please note** that these extension apps will also incur their own **usage costs**! You can select “y” in order to adjust the default settings and remove any extension you don’t need.

#### [](https://fly.io/docs/laravel/#launch-configuration)Launch Configuration

Once you accept the configuration, this would proceed with **adding [default secrets](https://github.com/superfly/flyctl/blob/master/scanner/laravel.go#L41-L50)**, **deploying the accepted extensions**, and **generating files** on your project:

1.   `.github/workflows/fly-deploy.yml`, `fly.toml` - Configurations specific to hosting on Fly 
2.   [.fly directory](https://github.com/fly-apps/dockerfile-laravel/tree/main/resources/views/fly) - A directory containing configuration files for running Nginx/PHP in a container 
3.   [Dockerfile](https://github.com/fly-apps/dockerfile-laravel/blob/main/resources/views/dockerfile.blade.php) - Used to build a container image that is run in fly 
4.   [.dockerignore](https://github.com/fly-apps/dockerfile-laravel/blob/main/resources/views/fly/dockerignore.blade.php) - Used to ensure certain files don’t make its way into your image 

With the configuration files and extenstion apps in place, an image is built for your app using your project and the Dockerfile generated for it. This image is then finally used to deploy your app.

#### [](https://fly.io/docs/laravel/#success)Success!

You should be able to visit `https://your-app-name.fly.dev` and see the Laravel demo home page.

That’s it! Run `fly apps open` to see your deployed app in action.

Try a few other commands:

*   [`fly logs`](https://fly.io/docs/flyctl/logs/) - Tail your application logs 
*   [`fly status`](https://fly.io/docs/flyctl/status/) - View your app’s current deployment status 
*   [`fly ssh console`](https://fly.io/docs/flyctl/ssh-console/) - Open a terminal on your VM 
*   [`fly deploy`](https://fly.io/docs/flyctl/deploy/) - Deploy the application after making changes 

[](https://fly.io/docs/laravel/#customizing-your-app)Customizing your app
-------------------------------------------------------------------------

If you have other environment variables to set, you can edit the `fly.toml` file and add them.

```
[env]
# Set any env vars you want here
# Caution: Don't add secrets here
APP_URL = "https://fly-hello-laravel.fly.dev"
```

Replace this with the URL your app will be served on (by default, `"https://<your-app-name>.fly.dev"`).

For sensitive data, you can set **secrets** with the [`fly secrets set`](https://fly.io/docs/flyctl/secrets-set/) command:

```
fly secrets set SOME_SECRET_KEY=<the-value-from-your-env-file>
```

### [](https://fly.io/docs/laravel/#deploy)Deploy

Once you’ve made changes for your app locally, you can run `fly deploy` to deploy your changes.

### [](https://fly.io/docs/laravel/#some-notes)Some Notes

Running `fly launch` (and later `fly deploy`) uses the `Dockerfile` to build a container image, copying your application files into the resulting image.

Fly doesn’t care about the state of your git repository - it copies whatever files are present (except for files ignored by `.dockerignore`).
