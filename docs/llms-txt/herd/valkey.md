# Source: https://herd.laravel.com/docs/macos/herd-pro-services/valkey.md

> ## Documentation Index
> Fetch the complete documentation index at: https://herd.laravel.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Valkey

# Setting up Valkey

Valkey is an alternative to Redis that is API compatible and can be used as a cache and queue driver in Laravel
applications. It's free and open source, making it a great choice for local development since Redis pivoted to a less
developer friendly license.

<Note>
  Keep in mind that using the `dump()` function in queued jobs only works if you pair it with the [Dumps](/macos/debugging/dumps) feature, otherwise dumps happen in the background, and you won't see them.
</Note>

You can set up a new Valkey instance via the services tab of the settings.

<Frame>
  <img alt="Screenshot of Valkey settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-valkey.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=d694ba29d47fd0cda010e0125f47cd6e" data-og-width="1800" width="1800" data-og-height="1236" height="1236" data-path="images/docs/setup-valkey.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-valkey.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=239a73dad8cce80a3c8c79f41261993b 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-valkey.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=443278dd6194c8fb18402f8618187ace 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-valkey.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=b4f4e2f3457d9771d7ee75c214430da3 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-valkey.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=94c8ce6aee0064ddf702a6275e4ab99c 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-valkey.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=8148996ae2442fefee53c1447e20ef99 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-valkey.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=107986a8a0193573fc8da9c6706e0aa0 2500w" />
</Frame>

## Configuration

Valkey comes with a sensible default configuration, making it easy to use for local development without any changes. If you want to change the port of the Valkey service or decide if you want to automatically start it with Herd, you can do that in the settings of the service.

You can modify the configuration by right-clicking the service in the settings and opening its data directory. In this data directory, there is a `valkey.conf` that this specific Valkey instance loads on startup.

Make sure to restart the service if you make changes to this configuration file.

## Accessing the Valkey instance

You usually don't need dedicated databases within your Valkey instance, but if you decide to do that or want to debug the content of your database, you can open TablePlus directly from the menu on the right side.

<Frame>
  <img alt="Valkey Sidebar" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_valkey.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=d7fa29ca04ac0263d6b673dfbe78ba35" data-og-width="1800" width="1800" data-og-height="1236" height="1236" data-path="images/docs/settings_services_valkey.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_valkey.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a8e031afd3f4b0d3ff036afba38dfa24 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_valkey.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=609a0884d693bbcdf598dfd2566c5e20 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_valkey.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=7380e2d2382436b178ff07b71cf84a23 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_valkey.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=9155b73d1920f88227aab55c975fbc87 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_valkey.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=7c9646c583e1b645753cee5a7ea83ffa 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_valkey.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f00b407df69e97a3efaffcd8163ffa44 2500w" />
</Frame>

## Connecting from your Laravel application

To connect it within your application, you can use the credentials that are listed next to the running service in the
settings, or you can use the ones below. Since Valkey is API compatible with Redis, the configuration is the same.

```env  theme={null}
# Driver configuration
CACHE_DRIVER=redis
QUEUE_CONNECTION=redis
SESSION_DRIVER=redis

# Redis setup
REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379
```

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service | Version |
| ------- | ------- |
| Valkey  | 7.2.x   |
| Valkey  | 8.0.x   |
| Valkey  | 8.1.x   |
