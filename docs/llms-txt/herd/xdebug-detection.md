# Source: https://herd.laravel.com/docs/macos/debugging/xdebug-detection.md

# Xdebug Detection

# Automatically use Xdebug

Herd Pro is able to detect Xdebug headers in HTTP requests or breakpoints in PHPStorm and routes these requests to a PHP process with Xdebug automatically. This keeps your site super fast on all normal requests but provides advanced debugging capabilities with Xdebug when needed.

<Note>
  If Xdebug is too much for you and you prefer debugging via dumps, check out the Herd take on [Dumps](/macos/debugging/dumps).
</Note>

## Setup with PhpStorm

Go to the debugging settings of Herd Pro and select the configuration to detect breakpoints within PhpStorm automatically.

<Frame>
  <img alt="Debugger Settings" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_debugger.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=9e81ce721ccbd7124acd16ecf232c32e" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/settings_debugger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_debugger.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=f39f377cfcdc9ac9ed31d3459fc1aeb1 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_debugger.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=95fd49cf07c14b424b079300a116bdce 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_debugger.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=2bfc5b2510618d692a172a31561d9d98 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_debugger.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=3eb9e2aba8386d23b4d8bc7c6ef227f6 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_debugger.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=80a3c8e802ecad468d4b49cd685b0fb9 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_debugger.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=576e90a1deb0117c8ab10d5ac3233718 2500w" />
</Frame>

When you set or remove a breakpoint in PhpStorm and save the file, this creates a temporary file within the `.idea` folder of your project. Herd parses these files to detect breakpoints.

<Note>
  Please make sure to listen for PHP Debug Connections in PhpStorm after setting the breakpoint so that Xdebug can connect to PhpStorm properly.
</Note>

### Configure PhpStorm to ignore the dump loader

Herd serves sites via a PHP script and if you've dumps enabled, it also uses a `dump-loader.php` file for custom bootstrapping of your application. If you want to debug with Xdebug, it makes sense to configure PHPStorm to ignore this dump loader. You can do that in the settings of PhpStorm by unchecking the boxes for:

* Force break at first line when no path mapping specified
* Force break at first line when a script is outside the project

<Frame>
  <img alt="PHPStorm settings for Xdebug" src="https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/docs/xdebug_phpstorm_dump_loader.png?fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=80f7cb10a141eb4059fd44407fa086ed" data-og-width="1964" width="1964" data-og-height="1444" height="1444" data-path="images/docs/xdebug_phpstorm_dump_loader.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/docs/xdebug_phpstorm_dump_loader.png?w=280&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=657609fc2d28245dec793ac50fdde033 280w, https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/docs/xdebug_phpstorm_dump_loader.png?w=560&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=e3a42e8a3d4f060fdf72332ed39052ca 560w, https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/docs/xdebug_phpstorm_dump_loader.png?w=840&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=8ec4e40a69e3957fd1d65f322175fdb7 840w, https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/docs/xdebug_phpstorm_dump_loader.png?w=1100&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=cc1fae3ab352abf5222510f03c368dad 1100w, https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/docs/xdebug_phpstorm_dump_loader.png?w=1650&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=1231909ebd7cb89186693cbb7c8d58bc 1650w, https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/docs/xdebug_phpstorm_dump_loader.png?w=2500&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=692b17622a8d3377628f736b7e10570c 2500w" />
</Frame>

If you do not use PHPStorm, you can use browser extensions for Xdebug to automatically load Xdebug.

## Setup with browser extensions

Herd uses the headers of Xdebug browser extensions that you can install via the [Chrome Web Store](https://chromewebstore.google.com/detail/xdebug-extension/aoelhdemabeimdhedkidlnbkfhnhgnhm) or [Firefox Addons](https://addons.mozilla.org/firefox/addon/xdebug-helper-for-firefox).

Once you enable the Xdebug feature in the browser extension, Herd serves the request via a PHP process with an enabled Xdebug extensions.

## Using Xdebug on the command line

You can run CLI commands via `herd debug ..` instead of using `php ...` to use the php binary with Xdebug enabled. For example, if you are debugging an artisan command, you can run `herd debug artisan your:command` to trigger your breakpoint.

## Code Coverage

Herd has a `coverage` command that allows you to run Xdebug's coverage mode on your test suite:

```bash  theme={null}
herd coverage ./vendor/bin/pest --coverage
```

## Troubleshooting

If the detection does not work, please make sure to save the file with the breakpoint after setting or removing the breakpoint.
