# Source: https://render.com/docs/deploy-rails-sidekiq.md

# Deploy Rails with Sidekiq on Render

In this guide, we will show you how to configure your existing [Rails](/deploy-rails-8) and Sidekiq application on Render.

While processing web requests, you may have to offload tasks to an asynchronous, background process (typically called a worker). [Sidekiq](https://github.com/mperham/sidekiq) is a popular task processing framework for Ruby. Render makes it easy to use Sidekiq with Rails.

At the end, you'll have 3 services:

1. Rails *[Web Service](web-services)* to handle web requests
2. Sidekiq *[Background Worker](background-workers)* to process tasks
3. *[Render Key Value](key-value)* instance for the persistence and communication of Sidekiq tasks

## Deploy to Render

There are 2 ways to deploy.
We will first walk through manually setting up your services using the dashboard.
We will then walk through declaring your services within your repository with [Blueprints](infrastructure-as-code).

## Deploy Manually

### Render Key Value

Create a new *[Render Key Value](key-value)* instance with the following settings using [the Key Value deployment guide](key-value#create-your-key-value-instance).

|                      |                                                   |
| -------------------- | ------------------------------------------------- |
| *Maxmemory Policy* | `noeviction (recommended for queues/persistence)` |
| *Plan*             | `Starter`                                         |

We choose the `noeviction` maxmemory policy to ensure the Key Value instance does not delete tasks when its memory is full. Instead, it will prevent the creation of new tasks.

We choose the `Starter` instance type as it is the smallest instance type with persistence. This means that the tasks will be written out to disk and will be retained even if the Key Value instance restarts.

Copy the Internal URL, which looks like `redis://red-xxxxxxxxxxxxxxxxxxxx:6379`

### Rails Web Service

Create a new *[Web Service](web-services)* for your Rails application. You may need to adjust the Build Command and Start Command for your service.

If you already have a Rails app deployed and are just adding Sidekiq, you can configure the `REDIS_URL` environment variable and skip the rest of this step.

|                   |                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------ |
| *Language*      | `Ruby`                                                                               |
| *Build Command* | `bundle install; bundle exec rake assets:precompile; bundle exec rake assets:clean;` |
| *Start Command* | `bundle exec puma -t 5:5 -p ${PORT:-3000} -e ${RACK_ENV:-development}`               |

Add the following environment variables to your web service (along with any other environment variables you need):

| Key                | Value                                                                                                            |
| ------------------ | ---------------------------------------------------------------------------------------------------------------- |
| `REDIS_URL`        | `<Internal URL>`, the internal Key Value URL from step 1.                                                        |
| `RAILS_MASTER_KEY` | Your Rails application's [RAILS_MASTER_KEY](https://edgeguides.rubyonrails.org/security.html#custom-credentials) |

### Sidekiq Background Worker

Create a new *[Background Worker](background-workers)* to process Sidekiq tasks.

|                   |                       |
| ----------------- | --------------------- |
| *Language*      | `Ruby`                |
| *Build Command* | `bundle install`      |
| *Start Command* | `bundle exec sidekiq` |

Add the following environment variables to your background worker (along with any other environment variables you need):

| Key                | Value                                                                                                            |
| ------------------ | ---------------------------------------------------------------------------------------------------------------- |
| `REDIS_URL`        | `<Internal URL>`, the internal Key Value URL from step 1.                                                        |
| `RAILS_MASTER_KEY` | Your Rails application's [RAILS_MASTER_KEY](https://edgeguides.rubyonrails.org/security.html#custom-credentials) |

If your Sidekiq worker needs access to a shared database or other service, [environment groups](configure-environment-variables#environment-groups) are useful for sharing environment variables across services on Render.

### Test it out!

Wait for these three services to finish deploying and then visit your Rails `.onrender.com` URL and trigger some tasks.

You should be able to see the Sidekiq Background Worker processing tasks in its logs.
<img src="../assets/images/docs/sidekiq/worker-logs.png" alt="Background Worker start and done Logs in Render Dashboard" />

On the Redis metrics page, you should be able to see Active Connections in use.
<img src="../assets/images/docs/sidekiq/active-connections.png" alt="Graph of Active Connections against time where Active Connections increase from 0 to 12" />

## Blueprints

Render enables users to deploy their services as code in a `render.yaml` file with [Blueprints](infrastructure-as-code).

The following is an example `render.yaml` to configure and deploy all 3 services.

```yaml
services:
  - type: keyvalue
    name: sidekiq-keyvalue
    region: ohio
    maxmemoryPolicy: noeviction
    ipAllowList: [] # only allow internal connections

  - type: worker
    name: sidekiq-worker
    runtime: ruby
    region: ohio
    buildCommand: bundle install
    startCommand: bundle exec sidekiq
    envVars:
      - key: REDIS_URL
        fromService:
          type: keyvalue
          name: sidekiq-keyvalue
          property: connectionString
      - key: RAILS_MASTER_KEY
        sync: false
  - type: web
    name: rails-web
    runtime: ruby
    region: ohio
    buildCommand: bundle install; bundle exec rake assets:precompile; bundle exec rake assets:clean;
    startCommand: bundle exec puma -t 5:5 -p ${PORT:-3000} -e ${RACK_ENV:-development}
    envVars:
      - key: REDIS_URL
        fromService:
          type: keyvalue
          name: sidekiq-keyvalue
          property: connectionString
      - key: RAILS_MASTER_KEY
        sync: false
```

1. Copy the above code into `render.yaml` in the top level of your repository.

2. Modify the `render.yaml` to suit your application. Remember, if you change a service name you need to update the corresponding reference in the `.envVars` that access variables from the service with the new name.

3. Change the region fields to your chosen [region](regions).

4. Commit and push your changes.

5. On the Render Dashboard, go to the Blueprint page and click the `New Blueprint Instance` button. Select your repository (after giving Render the permission to access it, if you haven’t already).

6. Enter your Rails application's [RAILS_MASTER_KEY](https://edgeguides.rubyonrails.org/security.html#custom-credentials) for the background worker and web service.

7. In the deploy window, click `Approve`.

8. Test it out with the steps in the previous section.