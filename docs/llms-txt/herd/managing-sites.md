# Source: https://herd.laravel.com/docs/macos/sites/managing-sites.md

# Managing Sites

# Manage Sites in Herd

If you've read the [Sites](/macos/getting-started/sites) introduction of the [Getting Started](/macos/getting-started/about-herd) section, you are already familiar with the concept of parked paths and linked directories – but how do you use them if you have many sites and use different technologies for them?

## Folder structure

We recommend to put all PHP based sites in your Herd directory until you reach a point where it makes sense to split them into a folder structure that makes sense for you. This could be sites per client, or if you run different technologies like Next.js, you can serve them from a different folder via `npm run dev`.

This setup keeps the [Site Manager](/macos/sites/managing-sites) clean and easy to use because you can simply unpark a directory in case that you don't work on these sites for a few weeks.

If you don't mind a long list in the Site Manager, you can also [mark your most important sites as favorites](#favorites) to display them at the beginning of the list.

## Site Manager

You can manage your sites via the CLI or open the Site Manager via the menu bar icon. This section of the docs explains all features of the Site Manager.

<Frame>
  <img alt="Open the Site Manager" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_sites.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0458732c0a855679a6cc050665efefc0" data-og-width="880" width="880" data-og-height="460" height="460" data-path="images/docs/sites_sites.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_sites.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e68ca7cc5fe19a5f3a683a9552f55844 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_sites.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a56a27ff92df79149aa6597b88ae08dd 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_sites.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=110c91c27d4beb69446fc5c23095389d 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_sites.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=300f13f6813c3a31df8a8adce9a9fb1a 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_sites.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ec22fa89c25e6f2ce409b13b49948607 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_sites.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=9d35ba43c8a9253a716ba7cdf66c115f 2500w" />
</Frame>

The Site Manager window is divided into the list of all your sites on the left side and a site management panel for the selected site on the right side.

You can hide the site list if you are working with mainly one site but also refresh the list in case that you are making changes to your parked or linked directories via the CLI and while the Site Manager is open.

Clicking on the plus button opens the site wizard that allows you to create Laravel applications or link existing ones that are not in a parked directory.

<Frame>
  <img alt="Open the Site Manager" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_overview.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=67cd996dd8522976d07ddadb486d7e9d" data-og-width="1868" width="1868" data-og-height="1122" height="1122" data-path="images/docs/sites_overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_overview.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e3a6a4af25b22ccea7b8ee07a7a0c844 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_overview.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=132cdc66df6ab564d4ce14c7d3eb7a56 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_overview.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=711915b2bd7f05c1085c49a084e65e2a 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_overview.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=05a75f433634d45a891b89ad2584556c 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_overview.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2020a2940b6b8da3227f2b308db49a6d 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_overview.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=97425c316e095b4565be7bf69d36c53b 2500w" />
</Frame>

The right side of the Sites Manager is dedicated to the selected site and always shows a general tab where you can isolate this site to a specific PHP version. This tells Herd to serve this site with a specific PHP version and not to use the [global configuration](/macos/technology/php-versions#using-different-php-versions-via-the-gui) that you apply in the settings.

If you select a specific Node.js version, Herd creates an `.nvmrc` file in your project directory. This tells your terminal to switch to the selected Node and NPM version automatically.

### Information

The information tab shows driver specific information about the application. For Laravel applications, that's the content of the `php artisan about` command, but you can customize this with a [custom driver](/macos/extending-herd/custom-drivers).

### Integrations

You can connect a Herd site with one or more sites on Laravel Forge. You can learn more about this feature in [Forge Integration](/macos/integrations/laravel-forge) docs.

## Site Actions

Site Actions are like shortcuts from the site manager. They allow you to open your favorite terminal directly in the project directory, start a [Tinker(-well)](/macos/debugging/tinker) session or launch your IDE.

If you open the database, Herd tries to open the application database with its tables in TablePlus but uses AdminerEvo in case that you don't use TablePlus. This gives you quick access to the database on the basis of your `.env` file.

The log action is available for Herd Pro users and opens the [Log Viewer](/macos/debugging/logs) that ships with [Herd Pro](https://herd.laravel.com/checkout). The Profiler action enables and disables the [profiling feature](/macos/debugging/profiler).

<Frame>
  <img alt="" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c85b423e650939b18e736ac0efac14c0" data-og-width="1872" width="1872" data-og-height="1122" height="1122" data-path="images/docs/sites_actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=024b530396e76dba91b8552f77e9df03 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c9628e2f385aa9aa3617666328fe1510 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3c2f53539036439c3bc10e0faaba7b87 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0c180a34f0ec88c005905555121f8ec6 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=516b3674d903000cbb231464e6995cab 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=8928f5ee21b006cf80fbdc3131fcc5b2 2500w" />
</Frame>

### Securing Sites

You can serve sites via HTTPS instead of HTTP if your application requires this via [Securing Sites](/macos/sites/securing-sites).

### Groups

If you are working with many sites at the same time and don't want to use multiple parked directories that you add and remove when you need them, you can group sites and they automatically appear in your own site structure on the left side.

<Frame>
  <img alt="Groups in the Site Manager" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_groups.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=222167ecf7ba32d8919a5d40e188fc3e" data-og-width="1868" width="1868" data-og-height="1122" height="1122" data-path="images/docs/sites_groups.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_groups.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=eb378047e22eb00860e71ad21a6c3497 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_groups.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e9eb17b206b351f5a2394ae2b8d761a8 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_groups.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=64a28161b9a2142698608832aea1c2ee 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_groups.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f18af9a02a71e5ab6d5edc9f130ead0b 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_groups.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=302ff9c4ef829030fe44cdfeaf299e9b 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_groups.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=71906e3253edd1feb45da92697a2dfff 2500w" />
</Frame>

### Deleting Sites

You can fully delete parked sites from your Herd directory with the trash icon. This is identical to deleting their folder with all files, so use this carefully.

## Best Practices

It's a good practice to name your local sites like your domains and subdomains to easily access them in your browser. As an example, the Herd website usually lives in the directory `~/Code/herd.laravel.com` so that it's accessible via `http://herd.laravel.com.test`. The Laravel website is in the directory `~/Code/laravel.com`, etc.

<Note>
  Directory names must not start with `www.`. Herd strips this part to allow you to access your local site via `www.laravel.com` and `laravel.com`.
</Note>
