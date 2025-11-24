# Source: https://herd.laravel.com/docs/macos/debugging/profiler.md

# Profiler

# Profiling Applications

Herd supports a customized version of the [SPX profiler](https://github.com/beyondcode/php-spx) for PHP. The profiler allows you to identify bottlenecks in your application and supports profiling web and CLI requests.

## Installing the profiler extension

You can download and install the profiler extension by running this command in your terminal:

```bash  theme={null}
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/beyondcode/php-spx/HEAD/install.sh)"
```

This command downloads the extension and moves it to your Herd application directory and also adds it to all your existing `php.ini` files. If you install a new version, please run this command again to add it to this version automatically.

The extension does not profile requests automatically and requires environment variables or specific headers to record and profile the request, so you can keep it enabled without slowing down your normal setup.

## Profiling Web Requests

You can either open the profiler dashboard from the site configuration of the Site Manager or by opening the `/herd-profiler` route of your application. This route is dynamically added to requests when you enable the profiler in the settings.

### The Profiler Dashboard

Herd uses the SPX extension for PHP to profile your application and display a customized dashboard of your requests. Please make sure to enable the profiling on the top left.

<Frame>
  <img alt="Profiler Dashboard" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_home.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8ffc773f2f36d372ad69485d657119f6" data-og-width="2780" width="2780" data-og-height="1998" height="1998" data-path="images/docs/profiler_home.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_home.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a12fc74bc7ce4ddd49a4c1a88aa63e85 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_home.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=1135b84d7dabf4a5017ecd4d493afcbb 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_home.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=e434cc64447717e866aea4e091b2b574 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_home.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=25ad2b21d6681c1bc42bdc8a1758fe37 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_home.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=2ddb2c7b9efe5e182fac51b86577f0fc 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_home.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ff194df4ea6db72de07eb958cfb5da7e 2500w" />
</Frame>

### Results

If you click on a web request in the dashboard, it loads a breakdown of the request and allows you to inspect function calls and other operations in great detail.

<Frame>
  <img alt="Profiler Settings" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_graph.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5d1beaef8cbac4c8bfbdadd652966c49" data-og-width="2780" width="2780" data-og-height="1998" height="1998" data-path="images/docs/profiler_graph.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_graph.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a77e8a04e1a3f6c6d5636827d95a7fe7 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_graph.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=eb294dbe43e8b630d9c8eb631e8edead 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_graph.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=e4b4aa989c4f80736406b37d44a774e1 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_graph.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=07046fc0bd56d82052ded457c28761ad 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_graph.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=80152cbdaf48d3ed3af8af4a0b11ff9e 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_graph.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7b9bb51896147dbf8f3e586a725d2421 2500w" />
</Frame>

## Profiling CLI scripts

While you can profile web requests via the dashboard, SPX has a profiler for CLI requests as well. When the SPX extension is active, you can run PHP scripts with `herd profile` to trigger the profiling process. As an example, you can profile artisan commands with this command:

```bash  theme={null}
herd profile artisan inspire
```

This profiles the command and displays the results directly in your terminal.

<Frame>
  <img alt="Profiler Settings" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_cli.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=419bdf862fecaac956ab213db874d9e4" data-og-width="2002" width="2002" data-og-height="1086" height="1086" data-path="images/docs/profiler_cli.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_cli.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=26370ecfe8b2742726a02512ee9e7d90 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_cli.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=003d26bb704446e783bf942d09960d5b 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_cli.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c29923905d8423ace4d80d822ba58bec 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_cli.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a8576aed16b8c335e1857d9766e28626 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_cli.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=bc3ed9066a95ef04d53a64898b347e80 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_cli.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ea5e91dcce6d2e7012c06ef36fca6405 2500w" />
</Frame>

## Profiling long-running CLI scripts

When you have long-running CLI scripts, such as daemonized processes, you might want to see profiling information regularly, instead of only seeing them once you end your PHP script.

You can do this by running:

```bash  theme={null}
herd profile --live artisan long-running-task
```

You can learn more about SPX in the [official documentation](https://github.com/NoiseByNorthwest/php-spx).
