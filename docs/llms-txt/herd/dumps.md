# Source: https://herd.laravel.com/docs/macos/debugging/dumps.md

> ## Documentation Index
> Fetch the complete documentation index at: https://herd.laravel.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Dumps

# Debugging with Dumps

The Dumps feature can automatically intercept all `dump()` calls in your code and display them in a separate window instead of rendering them in the browser or CLI. But that's not all, it can also show HTTP requests, logs, Eloquent queries, dispatched jobs and Blade views to give you all the integrations that you need when debugging your app.

## Using Dump features

You may open the Dumps Window via the Herd system tray menu or open it with a globally configurable shortcut that you can define in the [shortcut settings](/macos/advanced-usage/shortcuts).

In order to enable dump interception and record debug information, click on the antenna icon in the title bar of the window. The icon will flash to indicate that dump interception is enabled.
Once enabled, you may use the `dump()` function as usual. Instead of printing the dump to your browser or terminal, Herd will open a window when a new dump becomes available.

<Frame>
  <img alt="Empty state of the dump interceptor window" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_empty.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7973a904c46a0dc312a1ee2725f8fe8f" data-og-width="1654" width="1654" data-og-height="1166" height="1166" data-path="images/docs/dumps_empty.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_empty.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=705d5dd6a54bc84ba928330f4bcdc197 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_empty.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=38bd222ca3acba2d0dbb39ef3b39eb2a 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_empty.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=79853ad0b4e11a170da6df6cc97221eb 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_empty.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=06c21aa6b1cddcf9732796e00335ff41 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_empty.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a7b92ce7836403291bab73a169bdedc4 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_empty.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=588c2aa98ba24efc6b6405bafb6eb45e 2500w" />
</Frame>

New dumps are automatically added to the top of the window, and you can clear the window by pressing the icon in the title bar of the dump window. All dumps are searchable so you can easily find what you are looking for.

By default, Herd only displays the output of the latest request, but you can enable persistent storage between requests in the settings. This keeps a history until you close the Dumps Window.

## Settings

You can select which features you need when you start debugging, so that your requests stay as fast as usual and there's no bloat when digging into a problem.

<Frame>
  <img alt="Dump Window" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=3b975ef5a985eb2051d8015d73d64a92" data-og-width="1844" width="1844" data-og-height="1342" height="1342" data-path="images/docs/dumps_settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a3ce4cef8e7af2c5bd71f8cc549e1cb0 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=29cbe8f9f64e084d45280079f41e6d28 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=19c8014aa53e82cd33f2387469eb2e80 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b452cc108274a1006e4821ab70fe3bf6 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d940a060b7211ef941f030dc71e416fc 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7ac8ec169b70cdad36a87080fd8028a1 2500w" />
</Frame>

## Dumps

When enabled, all dumps that you run via Laravels' `dump()` or `dd()` methods automatically go to the Dumps Windows instead of your browser. This has the advantage that the dump doesn't break your layout and SPAs still work.

This also sends `dump()` calls from queued jobs to the dump window that you wouldn't see in your browser when working with real queues.

<Frame>
  <img alt="Dump Window" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_dumps.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=dbb2744e5da4680251b9cc53470a58d8" data-og-width="1654" width="1654" data-og-height="1166" height="1166" data-path="images/docs/dumps_dumps.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_dumps.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c5d347e21953a8c71401645852a84f52 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_dumps.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=19ccdbef3cc55bdc058875a1b4b843f2 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_dumps.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=da11d625775e0c89fb00ee76e0c98590 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_dumps.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=94c896c42dcd7112e4abfee68c24e8d2 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_dumps.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7b9a36da2a35b803d5ba58eb2b48d045 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_dumps.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=435d785ec47d592fc6550101fd0f40d3 2500w" />
</Frame>

## Queries

You can display and debug Eloquent queries by enabling the query feature in the settings. If you want to debug specific queries, you can select the duration for these queries and skip fast ones which are good to go.

<Frame>
  <img alt="Dump Window" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_queries.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=3c9b2df17fdb07f514b8b629062a6d1e" data-og-width="1654" width="1654" data-og-height="1166" height="1166" data-path="images/docs/dumps_queries.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_queries.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c7912a761607e4aca0b3e802699643fd 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_queries.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=cfeded8e039d7122631c7e84dd416dae 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_queries.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ee62c16030165b595438c187b392f648 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_queries.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=be56d44a0d3bc98dfc7f0be301c9397c 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_queries.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=e6a1b4ff5ddd0173749b3c5984a06450 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_queries.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8384c5202acdb3b9780a929dd3b023ee 2500w" />
</Frame>

## Jobs

Enable job logging to get a list of all jobs that your application runs. This is super useful when you work with the sync driver and are not sure if all jobs are properly triggered.

<Frame>
  <img alt="Dump Window" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_jobs.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=17edcb26c0209c8a4d0b50acb973c6cc" data-og-width="1654" width="1654" data-og-height="1166" height="1166" data-path="images/docs/dumps_jobs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_jobs.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b2e459d4c4bbd40006720761c16e3b4b 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_jobs.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ca4e266c8534dab594ae9734f1edb37a 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_jobs.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=1806e609efa993ba3fe6c548cb441943 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_jobs.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=29a615d5299abc81c934c3fea72b17c2 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_jobs.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=4ea40ea5c84f17c4a4baaa2848094604 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_jobs.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=dfe63cfeb97d12226f28db4b825aeaa9 2500w" />
</Frame>

## Views

Sometimes, you want to know which data gets passed to a view and which views your application loads on a specific site. This tab lists all views that Laravel renders during a request.

<Frame>
  <img alt="Dump Window" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_views.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=2b641e70287d56f352a5a27ecd8a5f9c" data-og-width="1654" width="1654" data-og-height="1166" height="1166" data-path="images/docs/dumps_views.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_views.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a5b68586ae7337563b474523df5828c1 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_views.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8332c987ef604a504e9ea553ee3e2b33 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_views.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=0234bab3984288b0cee382c286d6dbb6 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_views.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=233c9ca7832780c8f3e5cc14dbb6777d 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_views.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=6fe6eb6cc4be00a4235f81d5e800ac56 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_views.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=f742cd71c26c2b8f3bce1e41f4324705 2500w" />
</Frame>

## HTTP

The request tab displays all outgoing HTTP requests of your application, so if you're working with an API, these calls show up in the Dumps Window and allow you to inspect them without searching through logs etc.

<Frame>
  <img alt="Dump Window" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_http.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=cf803e7594d260eccaaf4bb9e9151ca7" data-og-width="1654" width="1654" data-og-height="1166" height="1166" data-path="images/docs/dumps_http.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_http.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8d806c654a54b9d11b8db71d951e47da 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_http.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ecd25ff0b48b031b23db8d659fb03e52 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_http.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7412fad1f05b0f4975ae826a2d00def7 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_http.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=770a51ce159b362d553b80418acae88a 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_http.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=943226cfbc27468c4543952fed47c43f 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_http.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=058a95a0e66a4aa1700c52f16d68afd5 2500w" />
</Frame>

## Logs

You can get all logs of a request without using Herd's Log Viewer or digging through log files.

<Frame>
  <img alt="Dump Window" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_logs.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=dc2835c70da47ce8a5fb14dc25302f54" data-og-width="1654" width="1654" data-og-height="1166" height="1166" data-path="images/docs/dumps_logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_logs.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7b0ce7dba9cc5c25b7c5effa5a268fe2 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_logs.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7e1505019d523af2c05e74f9c5dc9611 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_logs.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=44dc4e886f2fc5cafc500d66d4a1b770 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_logs.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ce6fbf79d665071f43d7b51e38de511f 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_logs.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b87bf6fb54b1d4085db859f3c5974cbd 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_logs.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5865ff7ae4d6062b85fe03a2d2048549 2500w" />
</Frame>

## Troubleshooting

The dumps feature uses Herds' own PHP extension so make sure it is present in your `php.ini` and the path to the extension is correct. If you think that there is a problem with the path, simply quit Herd, remove the extension from the ini file and start Herd again. This will add the extension to the configuration file with the correct path.

```ini  theme={null}
extension=/Applications/Herd.app/Contents/Resources/herd-ext/herd-83-arm64.so
```

Technically, Herd uses this extension to inject code into your codebase in very early stages of the bootstrapping process. So if you're facing issues within your application, you might want to disable some or all of the features in the [settings](#settings).
