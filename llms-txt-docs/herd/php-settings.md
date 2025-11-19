# Source: https://herd.laravel.com/docs/macos/technology/php-settings.md

# PHP Settings

# Changing PHP settings

The values that most developers change are the memory limit and the max upload size. You can modify them in the settings and don't need to go deep into configuration files.

<Frame>
  <img alt="Screenshot of settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_config.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=280cf026f25d384aad7b5a9e71639ef0" data-og-width="1460" width="1460" data-og-height="1226" height="1226" data-path="images/docs/settings_php_config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_config.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0755d54cb22be60d2ade51f4f283ca72 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_config.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2a1e4c980d8efffed9b0180f3c1d1877 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_config.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f1a325853ccd6c1f2879894b51586c9d 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_config.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0836c3a7cd78ebe20b4296da5f1a8261 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_config.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4d1f82e13c30a3e32472ac0d7a38a8e0 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_config.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=69c049d38cf53ab1bdb080ee81c89c5c 2500w" />
</Frame>

Herd gives you easy access to the PHP configuration files on your machine, the easiest way to get to the file is to select the php.ini directory from the context menu of the settings.

<Frame>
  <img alt="Screenshot of context menu" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_ini.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=842bf0e50500c9dbe0aae22afaba86af" data-og-width="1460" width="1460" data-og-height="1226" height="1226" data-path="images/docs/settings_php_ini.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_ini.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c9ef495bdf25217bd3dbdc6152e47733 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_ini.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1c79b81c17b5de14bc6a584f2a71c795 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_ini.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ee6081b74ebb4f5fc489afbd1d6ced7d 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_ini.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e5e7599b87da4f1e0d07dbeb2e2a29fb 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_ini.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=849ee1978e7c198c71c55c10d15a05cb 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_ini.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=39a98ffb3ca0b3c0afa16b351dd266a7 2500w" />
</Frame>

Each PHP version has its own `php.ini` file at `~/Library/Application Support/Herd/config/php/<version>/php.ini`.
You can edit this file to change or add PHP settings for a specific PHP version.

<Note>
  If you want to quickly access your php.ini file via the CLI, you may use the `herd ini` command.
</Note>

All saved changes are immediately available in the CLI, but you need to restart all Herd services to apply the changes to HTTP requests via nginx.

You can restart all services by clicking "Stop all" and then "Start all" in the Herd dropdown menu in the menu bar – it just takes 1-2 seconds. If a service does not restart properly, or you believe that there is a stale process still running with old settings, you can press the `Option` key when the menu is open and select `Force stop all`.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/stop-all.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f33cb90c9526a4545cf88e815b726db6" data-og-width="1030" width="1030" data-og-height="522" height="522" data-path="images/docs/stop-all.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/stop-all.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=6a73e3438bc6146966481d14c79752f1 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/stop-all.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=50daf5112c710f525b6ceea0995487b2 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/stop-all.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1558ddccb3ae9a28e944ec3ecfd49ba7 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/stop-all.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=fee9f4b1a90a75d818998923ca0fd41c 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/stop-all.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ab9d0051cf3634c8c3813c153892e3c8 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/stop-all.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=482edfa477152444f206c5258a5a2f48 2500w" />
</Frame>

Alternatively, you can use the `herd restart` command in the terminal.

```shell  theme={null}
herd restart
```
