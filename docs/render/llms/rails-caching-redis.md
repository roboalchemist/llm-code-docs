# Source: https://render.com/docs/rails-caching-redis.md

# Rails caching with Redis

This guide will show how you can set up caching using [Redis](https://redis.io/) with an existing [Rails](https://rubyonrails.org/) app on Render. [Caching](<https://en.wikipedia.org/wiki/Cache_(computing)>) is a technique that allows you to reuse a previous result from a computation or call to speed up the latency of most uses. For example, if you're making requests against an external API and you can tolerate stale results, you can cache the result - reducing the amount of time to retrieve the data from hundreds of milliseconds to just a couple of milliseconds.

Rails gives you the ability to use [different cache stores](https://guides.rubyonrails.org/caching_with_rails.html#cache-stores). While `MemoryStore` and `FileStore` can be sufficient in many use cases, using an external component for your cache like Redis has a couple of advantages:

- Redis allows all you to share data between processes and instances. This is especially handy when you're using a threaded server like Puma or if you have multiple server instances.
- Redis is more persistent. On new deploys, new instances of your web service will be able to access cached results from your old instances.

The rest of the guide assumes you already have an existing Rails app. Follow our [Rails quickstart](/deploy-rails-8) to create one if you don't.

## Deploy to Render

We will first deploy a Redis instance on Render that is connected to your Rails app. There are 2 ways to deploy, either by [declaring your services within your repository](infrastructure-as-code) in a `render.yaml` file, or by manually setting up your services using the dashboard.

### Use `render.yaml` to deploy

In your existing render.yaml , add the following:

```yaml{2-6,19-23}
services:
 - type: redis
   name: cache
   ipAllowList: [] # only allow internal connections
   plan: free # optional (defaults to starter)
   maxmemoryPolicy: allkeys-lfu # optional (defaults to allkeys-lru). Rails recommends allkeys-lfu as a default.
 - type: web # this example Rails service comes from https://render.com/docs/deploy-rails
   name: mysite
   runtime: ruby
   buildCommand: "./bin/render-build.sh"
   startCommand: "bundle exec puma -C config/puma.rb"
   envVars:
     - key: DATABASE_URL
       fromDatabase:
         name: mysite
         property: connectionString
     - key: RAILS_MASTER_KEY
       sync: false
     - key: REDIS_URL # this must match the name of the environment variable used in production.rb
       fromService:
         type: redis
         name: cache
         property: connectionString
```

This will create a new free Redis instance called `cache` with a `maxmemory-policy` set to `allkeys-lfu`. It also provides the connection string of the Redis instance to the Rails app as an environment variable called `REDIS_URL`.

### Deploy Manually

If you don't want to deploy your Rails app through a Blueprint, you can follow these steps for a manual deploy.

1. Create a new [Redis instance](key-value#create-your-key-value-instance) on Render. Note your Redis *Internal Redis URL*; you will need it later.

2. Navigate to your Rails app service page. Select the `Environment` tab. Add the following environment variable:

   | Key         | Value                                                      |
   | ----------- | ---------------------------------------------------------- |
   | `REDIS_URL` | The *Internal Redis URL* for the Redis you created above |

## Add `RedisCacheStore` to your Rails app

Now that you've deployed a Redis instance that is connected to your Rails app, we will configure the cache store used in production to be `RedisCacheStore` with the correct connection url.

1. Add the following lines to your Gemfile. You may already have the redis gem installed.

   ```ruby
   gem 'redis'

   # Use hiredis to get better performance than the "redis" gem
   gem 'hiredis'
   ```

2. Edit the following lines in config/environments/production.rb:

   ```ruby{2-4}
   # Use a different cache store in production.
   config.cache_store = :redis_cache_store, {
     url: ENV['REDIS_URL']
   }
   ```

3. Commit all changes and push them to your GitHub repository.

That's it! Render will redeploy the Rails app so that Rails will use the Redis instance created as its cache store. The official [Caching with Rails](https://guides.rubyonrails.org/caching_with_rails.html) guide is a great resource to check out next to figure out how to make the most use of your new Redis cache!