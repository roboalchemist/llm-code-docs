# Source: https://www.aptible.com/docs/how-to-guides/app-guides/serve-static-assets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to serve static assets

> 📘 This article is about static assets served by your app such as CSS or JavaScript files. If you're looking for strategies for storing files uploaded by or generated for your customers, see [How do I accept file uploads when using Aptible?](/how-to-guides/app-guides/use-s3-to-accept-file-uploads) instead.

Broadly speaking, there are two ways to serve static assets from an Aptible web app:

## Serving static assets from a web container running on Aptible

> ❗️ This approach is typically only appropriate for development and staging apps. See [Serving static assets from a third-party object store or CDN](/how-to-guides/app-guides/serve-static-assets#serving-static-assets-from-a-third-party-object-store-or-cdn) to understand why and review a production-ready approach. Note that using a third-party object store is often simpler to maintain as well.

Using this method, you'll serve assets from the same web container that is serving application requests on Aptible.

Many web frameworks (such as Django or Rails) have asset serving mechanisms that you can use to build assets, and will automatically serve assets for you after you've done so.

Typically, you'll have to run an asset pre-compilation step ahead of time for this to work. Ideally, you want do so in your `Dockerfile` to ensure the assets are built once and are available in your web containers.

Unfortunately, in many frameworks, building assets requires access to at least a subset of your app's configuration (e.g., for Rails, at the very least, you'll need `RAILS_ENV` to be set, perhaps more depending on your app), but building Docker images is normally done **without configuration**.

Here are a few solutions you can use to work around this problem:

## Use Aptible's `.aptible.env`

If you are building on Aptible using [Dockerfile Deploy](/how-to-guides/app-guides/deploy-from-git), you can access your app's configuration variables during the build. This means you can load those variables, then build your assets.

To do so with a Rails app, you'd want to add this block toward the end of your `Dockerfile`:

```bash  theme={null}
RUN set -a \
 && . ./.aptible.env \
 && bundle exec rake assets:precompile
```

For a Django app, you might use something like this:

```bash  theme={null}
RUN set -a \
 && . ./.aptible.env \
 && python manage.py collectstatic
```

> 📘 Review [Accessing Configuration variables during the Docker build](/how-to-guides/app-guides/access-config-vars-during-docker-build) for more information about `.aptible.env` and important caveats.

## Build assets upon container startup

An alternative is to build assets when your web container starts. If your app has a [Procfile](/how-to-guides/app-guides/define-services), you can do so like this, for example (adjust as needed):

```bash  theme={null}
# Rails example:
web: bundle exec rake assets:precompile && exec bundle exec rails s -b 0.0.0.0 -p 3000

# Django example:
web: python manage.py collectstatic && exec gunicorn --access-logfile=- --error-logfile=- --bind=0.0.0.0:8000 --workers=3 mysite.wsgi
```

Alternatively, you could add an `ENTRYPOINT` in your image to do the same thing.

An upside of this approach is that all your configuration variables will be available when the container starts, so this approach is largely guaranteed to work as long as there is no bug in your app.

However, an important downside of this approach is that it will slow down the startup of your containers: instead of building assets once and for all when building your image, your app will rebuild them every time it starts. This includes restarts triggered by [Container Recovery](/core-concepts/architecture/containers/container-recovery) should your app crash.

Overall, this approach is only suitable if your asset build is fairly quick and/or you can tolerate a slower startup.

## Minimize environment requirements and provide them in the Dockerfile

Alternatively, you can refactor your App not to require environment variables to build assets.

For a Django app, you'd typically do that by creating a minimal settings module dedicated to building assets and settings, e.g., `DJANGO_SETTINGS_MODULE=myapp.static_settings` prior to running `collectstatic`

For a Rails app, you'd do that by creating a minimal `RAILS_ENV` dedicated to building assets and settings e.g. `RAILS_ENV=assets` prior to running `assets:precompile`.

If you can take the time to refactor your App slightly, this approach is by far the best one if you are going to serve assets from your container.

## Serving static assets from a third-party object store or CDN

## Reasons to use a third-party object store

There are two major problems with serving assets from your web containers:

### Performance

If you serve your assets from your web containers, you'll typically do so from your application server (e.g. Unicorn for Ruby, Gunicorn for Python, etc.).

However, application servers are optimized for serving application code, not assets. Serving assets is a comparatively dumb task that simpler web servers are better suited for.

For example, when it comes to serving assets, a Unicorn Ruby server serving assets from Ruby code is going to be very inefficient compared to an Nginx or Apache web server.

Likewise, an object store will be a lot more efficient at serving assets than your application server, which is one reason why you should favor using one.

### Interaction with Zero-Downtime Deploys

When you deploy your app, [Zero-Downtime Deployment](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview#zero-downtime-deployment) requires that there will be a period when containers from both your old code release and new code release are serving traffic at the same time.

If you are serving assets from a web container, this means the following interaction could happen:

1. A client requests a page.

2. That request is routed to a container running your new code, which responds with a page that links to assets.

3. The client requests a linked asset.

4. That request is routed to a container running your old code.

When this interaction happens, if you change your assets, the asset served by your Container running the old code may not be the one you expect. And, if you fingerprint your assets, it may not be found at all.

For your client, both cases will result in a broken page

Using an object store solves this problem: as long as you fingerprint assets, you can ensure your object store is able to serve assets from *all* your code releases.

To do so, simply upload all assets to the object store of your choice for a release prior to deploying it, and never remove assets from past releases until you're absolutely certain they're no longer referenced anywhere.

This is another reason why you should be using an object store to serve static assets.

> 📘 Considering the low pricing of object stores and the relatively small size of most application assets, you might not need to bother with cleaning up older assets: keeping them around may cost you only a few cents per month.

## How to use a third-party object store

To push assets to an object store from an app on Aptible, you'll need to:

* Identify and incorporate a library that integrates with your framework of choice to push assets to the object store of your choice. There are many of those for the most popular frameworks.

* Add credentials for the object store in your App's [Configuration](/core-concepts/apps/deploying-apps/configuration).

* Build and push assets to the object store as part of your release on Aptible. The easiest and best way to do this is to run your asset build and push as part of [`before_release`](/core-concepts/apps/deploying-apps/releases/aptible-yml#before-release) commands on Aptible.

For example, if you're running a Rails app and using [the Asset Sync gem](https://github.com/rumblelabs/asset_sync) to automatically sync your assets to S3 at the end of the Rails assets pipeline, you might use the following [`.aptible.yml`](/core-concepts/apps/deploying-apps/releases/aptible-yml) file:

```bash  theme={null}
before_release:
  - bundle exec rake assets:precompile
```
