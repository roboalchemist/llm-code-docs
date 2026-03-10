# Source: https://render.com/docs/deploy-astro.md

# Deploy Astro on Render — Host your site for free in minutes.

You can deploy your Astro site on Render for free.

How you deploy depends on whether your site includes server-side logic (SSR, API routes, etc.):

[diagram]

See instructions for each service type below.

> *Not sure if you have a server-side component?*
>
> Check your project's `astro.config.mjs` file. If it sets `output: 'server'` or `output: 'hybrid'` (removed in Astro v5), deploy as a [web service](#web-service).

## Static site (no server-side logic)

Sites without a server-side component use Render's *static site* service type.

Static sites are served over a global CDN. They include fully managed TLS certificates and support custom domains out of the box.

1. In the [Render Dashboard](https://dashboard.render.com), click *New > Static Site*:

    [image: Selecting Static Site from the New menu]

2. In the creation form, connect your Astro project's GitHub repository.
    - (GitLab and Bitbucket work too.)

3. For your site's *Build Command* and *Publish Directory*, set the following:

| Setting | Value |
| --- | --- |
| *Build Command* | `npm install && npm run build` If you use a different package manager (such as `bun`, `pnpm`, or `yarn`), use its equivalent command instead. |
| *Publish Directory* | `dist` |

4. Click *Deploy Static Site*. Render kicks off your site's first build and deploy.

That's it! Your site will be live at its `onrender.com` URL as soon as the deploy finishes:

[image: An Astro static site's URL in the Render Dashboard]

As next steps, you can [add a custom domain](custom-domains) to your site and set up [pull request previews](service-previews#pull-request-previews-git-backed).

## Web service

Astro sites with a server-side component use Render's *web service* service type.

Web services support both [horizontal and vertical scaling](scaling). They include fully managed TLS certificates and support custom domains out of the box.

1. If necessary, update your Astro project to use the `@astrojs/node` adapter if you currently use a different adapter:

    ```shell
    npx astro add node
    ```

    After making this change, push it to your repository.

2. In the [Render Dashboard](https://dashboard.render.com), click *New > Web Service*:

    [image: Selecting Web Service from the New menu]

3. In the creation form, connect your Astro project's GitHub repository.
    - (GitLab and Bitbucket work too.)

4. For your web service's *Build Command* and *Start Command*, set the following:

| Setting | Value |
| --- | --- |
| *Build Command* | `npm install && npm run build` If you use a different package manager (such as `bun`, `pnpm`, or `yarn`), use its equivalent command instead. |
| *Start Command* | `node dist/server/entry.mjs` If you've customized your site's builds, confirm this path by building your site locally and checking the output of the `build` command. |

5. Set your service's *Instance Type* to *Free*.

    - You can upgrade to a paid instance type at any time.
    - Learn more about [free instance types](free).

6. Under *Environment Variables*, add the following variables:

| Name | Value |
| --- | --- |
| `HOST` | `0.0.0.0` (By default, dynamic Astro sites bind to `127.0.0.1` (i.e., `localhost`). Render web services must bind to `0.0.0.0` instead.) |
| `NODE_VERSION` (optional) | Optionally set this to the version of Node.js you want to use for your site. Newly created services use Node.js `22.22.0` by default. |

7. Click *Deploy Web Service*. Render kicks off your service's first build and deploy.

That's it! Your site will be live at its `onrender.com` URL as soon as the deploy finishes:

[image: An Astro web service's URL in the Render Dashboard]

As next steps, you can [add a custom domain](custom-domains) to your site and set up [pull request previews](service-previews#pull-request-previews-git-backed).

---

##### Appendix: Glossary definitions

###### build command

The command that Render runs to build your service from source.

Common examples include `npm install` for Node.js and `pip install -r requirements.txt` for Python.

Related article: https://render.com/docs/deploys.md#build-command

###### start command

The command that Render runs to start your built service in a newly deployed *instance*.

Common examples include `npm start` for Node.js and `gunicorn your_application.wsgi` for Python.

Related article: https://render.com/docs/deploys.md#start-command