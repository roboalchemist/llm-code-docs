# Source: https://herd.laravel.com/docs/macos/getting-started/sites.md

# Sites

# Sites

Herd uses the concept of *parked* paths and *linked* directories for serving sites. You can access every site in a parked path via `<directory-name>.test`. By default, Herd parks the `~/Herd` directory for you. Any PHP application in this directory is available via its `.test` domain automatically. If you have other locations for your projects, you can add them as parked paths in the general settings or link individual projects as a linked directory.

<Frame>
  <img alt="General Settings" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/general.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c19852d44fecabeb5bc19eedc5e8e453" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/general.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/general.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=22afd9e1fa032bb21b9155850730ce93 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/general.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=4869478d1f5a4152914c4a7d2167a8f0 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/general.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=e1e778bc29630e44d5f9198cd41497a1 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/general.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=097afd2821b2723239b6e5aa63923d92 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/general.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=3bff520c6616897ce59adf0038dd5449 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/general.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=68f07df21797b6c7ada48ed577906c1a 2500w" />
</Frame>

Aside from Laravel, Herd [supports many frameworks](/macos/extending-herd/supported-frameworks) and applications out-of-the-box. If your framework is not in the list, you can create a [custom driver](/macos/extending-herd/custom-drivers) to run it with Herd.

## Creating your first site

The fastest way to manage your sites and to create new applications is the command line.

```shell  theme={null}
cd ~/Herd
laravel new my-new-site
cd my-new-site
herd open
herd edit
```

These commands go into your Herd directory, create a brand new Laravel application and open it in your browser. The `herd edit` command even opens your favorite IDE.

## Linking an existing site

You can link an existing site with a specific domain via the `link` command from any directory on your machine. The `link` command uses the directory name as domain name if you don't set additional parameters.

```shell  theme={null}
cd ~/Sites/your-project
herd link
herd link custom-domain
```

These commands create Herd configurations, and you can now access the application via `your-project.test` and `custom-domain.test`. This is useful if you want to use an application from multiple domains, for example in multi-tenancy environments or if you don't store all your projects in a single code directory.

## Via the GUI

If you prefer creating and linking sites via a graphical user interface, you can use Herd's site wizard to create new Laravel applications or link existing projects.

You can start the site wizard by opening the [Site Manager](/macos/sites/managing-sites) from the Herd menu bar icon and selecting the plus icon at the top left.

<Frame>
  <img src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_wizard.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e036cb8184e43e2c20e61521982d4545" data-og-width="1868" width="1868" data-og-height="1122" height="1122" data-path="images/docs/sites_wizard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_wizard.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=71559417801774d79796d3a538c151e7 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_wizard.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a19b9c7e83e2ba48fe3862fcf88331cb 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_wizard.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=83160e018710fe921d71987ae9befa3a 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_wizard.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e8da1ee4e77c6e49645f7eacd4f7654b 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_wizard.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4eeb18e2fc28519972ee9125eb85f520 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_wizard.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a8819615eb8f41d422b946d121e2e837 2500w" />
</Frame>

## Unlinking an existing site

You may remove a previously created link, by using the `unlink` command from any directory on your machine. The `unlink` command uses the directory name as domain name if you don't set additional parameters.

```shell  theme={null}
cd ~/Sites/your-project
herd unlink
herd unlink custom-domain
```

These commands remove any previous created links to your site.

## Application Information

The "Information" tab gives you a brief overview of the application. Laravel apps display the content of the `php artisan about` command, but you can customize the overview by using a [custom driver](/macos/extending-herd/custom-drivers) for your site.

## Integrations

Herd allows linking your local site with first-party Laravel cloud services and makes triggering common tasks like deployments super easy. At the moment, Herd supports connecting to sites on Laravel Forge with the [Forge integration](/macos/integrations/laravel-forge).
