# Source: https://herd.laravel.com/docs/macos/herd-pro-services/laravel-reverb.md

# Laravel Reverb

# Setting up a Laravel Reverb instance

[Laravel Reverb](https://reverb.laravel.com/) is a first-party WebSocket server for Laravel applications. It's open source and uses the Pusher protocol, making it the first choice for real-time communication between client and server in Laravel applications. If you want to learn more about Reverb, check out [Real-time games with Laravel](https://laracasts.com/series/real-time-games-with-laravel) on Laracasts.

While you can install it as a package into your existing application, it often makes sense to have a dedicated WebSocket server for all your applications.

Herd provides a convenient way to set up a dedicated Reverb instance on your machine with a few clicks. It even comes secured with an optional TLS certificate.

<Frame>
  <img alt="Screenshot of MySQL settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-reverb.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0f679516cc6864c6f0347ccc279c627a" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/setup-reverb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-reverb.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4f17e3e4f12f353ea2b91cf5c2ebb876 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-reverb.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=58d11542936fa9864ca43c925941fe8e 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-reverb.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=587e72ee734b04a4a873fc5d45174fbf 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-reverb.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1be3c57db1fac350e33a9372273e396e 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-reverb.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=13794e486f54d70f19025c4098e9f28b 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-reverb.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ae81d8d6613af803277a74bac277337b 2500w" />
</Frame>

## Connecting from your Laravel application

Laravel Reverb starts the WebSocket server on port `8080` but you can change it when creating a new service in case you're already running a different service on that port or want to run multiple instances in parallel.
After installing Reverb, you can use the following environment variables to configure the service for your application.

```bash  theme={null}
REVERB_APP_ID=1001
REVERB_APP_KEY=laravel-herd
REVERB_APP_SECRET=secret
REVERB_HOST="0.0.0.0"
REVERB_PORT=8080
```

Check out the [Laravel Echo documentation](https://laravel.com/docs/11.x/broadcasting#client-reverb) to learn how to connect your application frontend to the Laravel Reverb server.

## Logs

Reverb constantly logs information to the running process, so if you are debugging Reverb connection,s you can open the output of the Reverb process by pressing the Open button in the logs area on the right side.

<Frame>
  <img alt="Reverb Logs" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_reverb.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=8b98984c650ba9734012936c12c8e43d" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_reverb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_reverb.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4c5c4c2447c5d14e2638afcd972fd857 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_reverb.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=aba09bf84e670e8e0fc84738bded0879 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_reverb.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2668b432dddddb1e557b5165bbec3599 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_reverb.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f736a01e31b9cf1a6797bc06400952a3 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_reverb.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=70ae09a2c8680390801784714fe771f2 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_reverb.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2a57106d85e23ecc5c17c041382b6f07 2500w" />
</Frame>

## Updates

Reverb uses composer and Herd supports updating Reverb to it's latest version via the Herd UI. Simply right click to open the context menu and select "update".

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service | Version |
| ------- | ------- |
| Reverb  | 1.x     |
