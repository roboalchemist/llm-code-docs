# Source: https://herd.laravel.com/docs/macos/technology/php-versions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://herd.laravel.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage PHP

# Using different PHP versions

Herd ships with the latest stable PHP version by default. Currently, that's PHP 8.3.
However, you may install and use different PHP versions for your sites and configure Herd that every project uses the version that it needs.

## Using different PHP versions via the GUI

You can manage your PHP versions in the "PHP" tab of the preferences window. This window allows you to install and update PHP versions with a single click.

<Frame>
  <img alt="PÜHP Settings" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_php.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=01e2b296bcf1083c067a64448fb3a59e" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/settings_php.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_php.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=814d5205dcab367927c8c4f5857c397f 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_php.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=56305abf49727320292bc7f9723cd94d 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_php.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=caea1f2fd4438b6d5a51e1d4a3da4f7b 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_php.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c1f32ae6a2b783271955312bde4ab462 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_php.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=e3b2351c2a3656ff51aead67c1b50b6a 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_php.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=1805d75e46bb7f0207e95237a9dd543c 2500w" />
</Frame>

In order to change the global PHP version that Herd uses by default, select it in the dropdown menu in the menu bar.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dropdown_php.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=cf9561d5a37eaa389c670e0244a08ec8" data-og-width="828" width="828" data-og-height="796" height="796" data-path="images/docs/dropdown_php.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dropdown_php.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=1a443bd6c891dabad1d20cbdf79e2614 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dropdown_php.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=09a171194bad039dbf92514e328a412e 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dropdown_php.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8f832bb23eb99419c2dfb7cc57581632 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dropdown_php.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=625332547196638116df0914971417ed 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dropdown_php.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=35fae0d81c6e69a95b6f3ef2df518ef6 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dropdown_php.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8a097a32c55bb66fb3788fc4a42d4038 2500w" />
</Frame>

Herd uses the global PHP version for all sites that are not [isolated](#per-site-php-versions).

## Using different PHP versions via the CLI

If you prefer to use the CLI, you can use the `herd use` command to set the global PHP version.

```shell  theme={null}
herd use 8.2
```

# Per-site PHP versions

By default, Herd uses the global PHP version to serve all your sites. However, if you need to support different PHP versions for different sites, you may use the isolate function.  This configures Herd to use a specific PHP version for a site, regardless of the global PHP version.

## Per site PHP versions via the GUI

You can configure the PHP version per site in the [Site Manager](/macos/sites/managing-sites). This gives you a list of all your sites and allows you to configure the PHP version that each site uses.

Just select the PHP version that you want to use for the site in the dropdown menu.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=43d575bfeec38ade48f0b1069ca3323a" data-og-width="1800" width="1800" data-og-height="1196" height="1196" data-path="images/docs/sites.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ac0f52cb86238074a2b66b04dc09615c 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=dbab61657028c779f437b463c73941ce 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=9448dd15ca3cffb589862c0e5eb4b3d6 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a6a9911ecd770528c2b357f6593f1ace 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=06807e86f4ea012969518118d31df970 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c75c44b14e5267d073ecb0c5ea7b6788 2500w" />
</Frame>

## Per site PHP versions via the CLI

If you prefer to use the CLI, you can use the `herd isolate` command to specify which PHP version a particular site should use.
The `isolate` command configures Herd to use the specified PHP version for the site located in your current working directory:

```shell  theme={null}
cd ~/Herd/example-site

herd isolate 8.0
```

If your site name does not match the name of the directory that contains it, you may specify the name using the `--site` option:

```shell  theme={null}
herd isolate 8.0 --site="site-name"
```

For convenience, you may use the `herd php`, `composer`, and `which-php` commands to proxy calls to the appropriate PHP CLI or tool based on the configured PHP version for the current directly and site:

```shell  theme={null}
herd php
herd composer
herd which-php
```

You may execute the `isolated` command to display a list of all of your isolated sites and their PHP and Node.js versions:

```shell  theme={null}
herd isolated
```

To revert a site back to Herd's globally installed PHP version, you may invoke the `unisolate` command from the root directory of the site:

```shell  theme={null}
herd unisolate
```

## Uninstalling PHP versions

You can uninstall PHP versions from the PHP settings. Simply right-click on a version and delete it via the context menu.

<Frame>
  <img alt="Delete PHP from Settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_delete.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=7e71c4f9cb248234d1f43127df5300ed" data-og-width="1460" width="1460" data-og-height="1226" height="1226" data-path="images/docs/settings_php_delete.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_delete.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=10f64d8605134efe0b4143f9e0d82b85 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_delete.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ebf73d931912bd79bca61a241d404c34 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_delete.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4bad7c030b785e88ac80d5a150554f39 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_delete.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=b589088c9de724583f888d76cd375ff5 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_delete.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=858ee29f74a2a98cf49cd2c51ff15d48 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_delete.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=5f0465ab0c6da0a2622f616f0e3b1b30 2500w" />
</Frame>

If you prefer deleting a PHP version manually, you can go into the Herd application directory and delete the files from your system. Once you reopen the settings, you can reinstall them.

```
~/Library/Application Support/Herd/bin
```
