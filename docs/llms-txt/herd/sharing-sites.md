# Source: https://herd.laravel.com/docs/macos/sites/sharing-sites.md

# Sharing Sites

# How to share a site

Herd makes it easy to share your local sites with the world. This is great for testing your sites on different devices, receiving webhooks, or sharing them with clients and colleagues.
Herd uses [Expose](https://expose.dev) to share your sites.

## Sharing sites via Expose

<Note>
  Expose may not be available in all geographical regions due to regulatory reasons. If Expose isn't available in your country, try [ngrok](#sharing-sites-via-ngrok).
</Note>

To share your site using Expose, you first need to [create a free Expose account](https://expose.dev/register).
Once you have obtained your authentication token, you can configure it in the "Expose" tab of the preferences window.

<Frame>
  <img alt="Expose Settings" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_expose.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=1b64103b11b8a97ba9558f491afaebd9" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/settings_expose.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_expose.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=03719af3085a3faeb0375acb50261671 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_expose.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ba384558581c053ca6132a5436ee1c79 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_expose.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=862297472aaa2c584bb16f2753b56435 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_expose.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=dfb47f6bede5a6dd3a6a7fd7eec529c8 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_expose.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=16ade982d6e26e08dacb0fcb0d8d5e54 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_expose.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=863f1683c617b7e2493d059f8291c07b 2500w" />
</Frame>

Or you can use the CLI:

```shell  theme={null}
expose token YOUR_TOKEN_HERE
```

Once you configured your authentication token, you can share your sites by running `herd share` or `expose share` in the site directory that you want to share.

```shell  theme={null}
cd ~/Herd/example-site

herd share

# Share a linked site:
herd share http://your-local-site.test

# You can share a secured site with:
herd share https://your-secured-local-site.test
```

You can specify a subdomain or server region for best performance and by adding parameters for them to the `share` command.

```shell  theme={null}
herd share https://example-site.test --subdomain=my-project-name --server=us-1
```

## Sharing with basic authentication

You may protect your share links with basic authentication by using the `--basicAuth` argument when sharing your site.

```shell  theme={null}
herd share https://example-site.test --basicAuth="user:password"
```

## Sharing sites via ngrok

If you want to use ngrok, install it according to their instructions. After that, you can share Herd sites via the terminal:

```shell  theme={null}
ngrok http --host-header=rewrite unsecured-site.test
ngrok http --host-header=rewrite secured-site.test:443
```
