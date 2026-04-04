# Source: https://herd.laravel.com/docs/macos/herd-pro-services/redis.md

> ## Documentation Index
> Fetch the complete documentation index at: https://herd.laravel.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Redis

# Setting up Redis

Redis is a fast in-memory data store that is very versatile, and most Laravel applications use it for caching or as queue service. While you may go with the `sync` driver for queues and the `file` driver for caches locally, it's often useful to have the same development setup that you use in production.

<Note>
  Keep in mind that using the `dump()` function in queued jobs only works if you pair it with the [Dumps](/macos/debugging/dumps) feature, otherwise dumps happen in the background, and you won't see them.
</Note>

You can set up a new Redis instance via the services tab of the settings.

<Frame>
  <img alt="Screenshot of MySQL settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-redis.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=52dfa1ee87d018b5aec4c274e75b1efb" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/setup-redis.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-redis.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3ac25accf9a1a848417760edf3cfe8a6 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-redis.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=d27c456b7f617705362b206f95e2760f 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-redis.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3d42515395d93c6c072d99a019faa299 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-redis.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f8f4b3d9c6ccdb4a14588327a188cff9 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-redis.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0966cd58faf9c216d91e022f5f78018f 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-redis.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e0e210d343e423af6d80b3cef9b34364 2500w" />
</Frame>

## Configuration

Redis comes with a sensible default configuration, making it easy to use for local development without any changes. If you want change the port of the Redis service or decide if you want to automatically start it with Herd, you can do that in the settings of the service.

You can modify the configuration by right-clicking the service in the settings and open its data directory. In this data directory, there is a `redis.conf` that this specific Redis instance loads on startup.

Make sure to restart the service if you make changes to this configuration file.

## Accessing the Redis instance

You usually don't need dedicated Redis databases within your redis instance but if you decide to do that or want to debug the content of your Redis database, you can open TablePlus directly from the menu on the right side.

<Frame>
  <img alt="MySQL Sidebar" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_redis.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=b7c7474e06c40e073e109cfc3b8a133e" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_redis.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_redis.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=93faabe5042256a57b607213e4697cd0 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_redis.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3b7bf7d96a9723994216d19c6fbf0b6a 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_redis.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2439d204a45e4fffbb3efa7a4bd01fed 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_redis.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=52cc5a6d4127321f90f7c768a3934519 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_redis.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=5a6536a3cd4d2fd9f850b3c5a64d2df4 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_redis.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=be0ec9d0930a2630957ee2749944ef70 2500w" />
</Frame>

## Connecting from your Laravel application

To connect it within your application, you can use the credentials that are listed next to the running service in the settings, or you can use the ones below.

```env  theme={null}
# Driver configuration
CACHE_DRIVER=redis
QUEUE_CONNECTION=redis
SESSION_DRIVER=redis

# Redis setup
REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6138
```

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service | Version |
| ------- | ------- |
| Redis   | 7.0.0   |
