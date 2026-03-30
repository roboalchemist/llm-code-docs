# Source: https://render.com/docs/deploy-sidekiq-worker.md

# Deploy a Sidekiq Worker

In the course of processing web requests, you might want to offload tasks to an asynchronous, background process (typically called a worker). Render makes this easy to do via the [background worker](background-workers) service type.

For this quick start, we'll use [Sidekiq](https://sidekiq.org/), a popular task processing framework for Ruby, and the [Sinatra](https://github.com/sinatra/sinatra) example in Sidekiq's [official repo](https://github.com/mperham/sidekiq/blob/v5.2.7/examples/sinkiq.rb).

Sidekiq [uses Redis](https://github.com/mperham/sidekiq/wiki/Using-Redis) for its processing backend, so we'll set up a Redis service first.

## Deploy to Render

There are two ways to deploy your application on Render, either by [declaring your services within your repository](infrastructure-as-code) in a `render.yaml` file, or by manually setting up your services using the dashboard. In the following steps, we will walk you through both options.

## Use `render.yaml` to Deploy

1. You can fork our [render-examples/sidekiq](https://github.com/render-examples/sidekiq) on GitHub which contains a `render.yaml` file that sets up a background worker alongside a Redis instance and a web service.
2. On the Render Dashboard, go to the [Blueprint page](https://dashboard.render.com/blueprints) and click the [New Blueprint Instance](https://dashboard.render.com/select-repo?type=blueprint) button. Select your repository (after giving Render the permission to access it, if you haven’t already). Or alternatively, you can click the Deploy To Render button in the Readme of the forked repo.
3. In the deploy window, click *Approve*.

That's it! Your app will be live on your `.onrender.com` URL as soon as the build finishes. Try out the web service using the web service Render URL and play around with the small application.

## Deploy manually

1. [Create](https://dashboard.render.com/new/redis) a new Redis instance on Render and copy the internal Redis URL to use below. The internal Redis URL will look like `red-xxxxxxxxxxxxxxxxxxxx:6379`.

2. Fork [render-examples/sidekiq](https://github.com/render-examples/sidekiq) on GitHub and create a new *Background Worker* using your repo and the following values:

   |                   |                                    |
   | ----------------- | ---------------------------------- |
   | *Language*      | `Ruby`                             |
   | *Build Command* | `bundle install`                   |
   | *Start Command* | `bundle exec sidekiq -r ./main.rb` |

   Also add the following environment variable to your background worker:

   | Key         | Value                                                                                     |
   | ----------- | ----------------------------------------------------------------------------------------- |
   | `REDIS_URL` | `<redis-connection-string>`, where `<redis-connection-string>` is the string from step 1. |

3. Create a new *Web Service* using the same repo you created in Step 2, and the following values:

   |                   |                            |
   | ----------------- | -------------------------- |
   | *Language*      | `Ruby`                     |
   | *Build Command* | `bundle install`           |
   | *Start Command* | `bundle exec ruby main.rb` |

   Also add the following environment variable to your web service:

   | Key         | Value                                                                                     |
   | ----------- | ----------------------------------------------------------------------------------------- |
   | `REDIS_URL` | `<redis-connection-string>`, where `<redis-connection-string>` is the string from step 1. |

   This will spin up a new Sinatra web service which you can use to test background message sending. The code uses Sidekiq's API to send the message to your Redis instance, which is the same instance your background worker is listening on. As a result, the worker picks up and processes any messages you send from the frontend.

You can also use a Sidekiq background worker from Rails. See Sidekiq's [getting started page](https://github.com/mperham/sidekiq/wiki/Getting-Started) for more information.