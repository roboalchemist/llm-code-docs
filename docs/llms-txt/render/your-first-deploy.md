# Source: https://render.com/docs/your-first-deploy.md

# Your First Render Deploy — Run your web app in minutes.

Welcome! Let's get up and running on Render.

*This tutorial uses free Render resources. No payment is required.* All you need is a GitHub repo with the web app you want to deploy (GitLab and Bitbucket work too).

> *Want to deploy an example app using a particular language or framework?*
>
> Check out our [quickstarts](#quickstarts).

## 1. Sign up

Signing up is fast and free:

## 2. Choose a service type

To deploy to Render, you create a *service* that pulls, builds, and runs your code.

1. Open the [Render Dashboard](https://dashboard.render.com).

2. In the top-right corner, open the *+ New* dropdown:

[image: The "New" dropdown in the Render dashboard]

Here you select a *service type*.

For this tutorial, choose *Web Service* or *Static Site*:

| Service type | Description | Common frameworks |
| --- | --- | --- |
| *Web Service* | Choose this if your web app runs any server-side code. The app also needs to listen for HTTP requests on a port. Full-stack web apps, API servers, and mobile backends are all web services. | Express, Next.js, Fastify, Django, FastAPI, Flask, Rails, Phoenix |
| *Static Site* | Choose this if your web app consists entirely of static content (mostly HTML/CSS/JS). Blogs, portfolios, and documentation sets are often (but not _always_) static sites. | Create React App, Vue.js, Hugo, Docusaurus, Next.js [static exports](https://nextjs.org/docs/pages/building-your-application/deploying/static-exports) |

You can deploy either of these service types for free on Render.

> *Free web services "spin down" after 15 minutes of inactivity.*
>
> They spin back up when they next receive an incoming HTTP request or new WebSocket connection. Learn more about [free instance limitations.](free)

## 3. Link your repo

After you select a service type, the service creation form appears.

1. First, connect your GitHub/GitLab/Bitbucket account to Render:

   [image: Options for connecting your Git provider to Render]

   After you connect, the form shows a list of all the repos you have access to:

   [image: List of available repos to use for a new service]

2. Select the repo that contains your web app and click *Connect*.

   The rest of the creation form appears.

## 4. Configure deployment

Complete the service creation form to define how Render will build and run your app.

*Click the tab for your service type to view important field details:*

**Web Service**

#### Important web service fields

------

###### Field

*Branch*

###### Description

Your service only deploys commits on the Git branch you specify, such as `main`. Render can automatically redeploy your app whenever you push changes to this branch.

---

###### Field

*Root Directory*

###### Description

Deploying from a monorepo? Specify the subdirectory that represents your application root. Your build and start commands will run from this directory.

---

###### Field

*Language*

###### Description

If your app's programming language isn't listed in this dropdown, you can still deploy using the `Docker` runtime if you build your app from a `Dockerfile`.

---

###### Field

*Build Command*

###### Description

This is the command that Render will use to build your app from source and install dependencies. Common examples include:

**Node.js**

```bash
npm install
``` You can also use `bun` or `yarn`.

**Python**

```bash
pip install -r requirements.txt
``` You can also use `uv` or `poetry`. To use `uv`, your project must include a `uv.lock` file.

**Ruby**

```bash
bundle install
``` This usually resembles the command you run locally to install dependencies and perform any necessary compilation.

---

###### Field

*Start Command*

###### Description

This is the command that Render will use to start your app. Common examples include:

**Node.js**

```bash
npm start
``` You can also use `bun` or `yarn`.

**Python**

```bash
gunicorn your_application.wsgi
```

**Ruby**

```bash
./bin/rails server
``` For some frameworks, this might differ from the command you run locally to start your app. For example, a Flask app might use `flask run` locally but `gunicorn` for production.

---

###### Field

*Instance Type*

###### Description

This determines your service's RAM and CPU, along with its cost. Choose the *Free* instance type to deploy for free:  [image: Selecting the Free instance type] 

---

###### Field

*Environment Variables*

###### Description

These will be available to your service at both build time and runtime. If you forget any, you can always add them later and redeploy.

------

**Static Site**

#### Important static site fields

------

###### Field

*Branch*

###### Description

Your site only deploys commits on the branch you specify, such as `main`. Render can automatically redeploy whenever you push changes to this branch.

---

###### Field

*Root Directory*

###### Description

Deploying from a monorepo? Specify the subdirectory that represents your application root. Your build command will run from this directory.

---

###### Field

*Build Command*

###### Description

This is the command that Render will use to install dependencies and then build your site's static assets. Common examples include:

**Next.js / Create React App / Vue.js**

```bash
npm install && npm run build
``` For Next.js, make sure you've set [`output: 'export'`](https://nextjs.org/docs/pages/building-your-application/deploying/static-exports#configuration) in your `next.config.js` file.

**Jekyll**

```bash
bundle install && bundle exec jekyll build
```

---

###### Field

*Publish Directory*

###### Description

This is the directory containing your site's static assets, which are usually generated by your build command. Common examples include:

- `build` (Create React App, Vue.js, etc.)
- `out` (Next.js static export)
- `_site` (Jekyll)

---

###### Field

*Environment Variables*

###### Description

These will be available to your service at build time. Additionally, some static site generators substitute environment variable values into your generated static assets. For example:

- Create React App performs environment variable substitution for variables prefixed with `REACT_APP_`.
- Next.js does the same for variables prefixed with `NEXT_PUBLIC_`.

If you forget any, you can always add them later and redeploy.

------

When you're done, click the *Deploy* button at the bottom of the form. Render kicks off your first deploy.

## 5. Monitor your deploy

Render automatically opens a log explorer that shows your deploy's progress:

[image: Logs for a service deploy]

Follow along as the deploy proceeds through your build and start commands.

- *If the deploy completes successfully,* the deploy's status updates to *Live* and you'll see log lines like these:

  ```bash
  # Web service
  ==> Deploying...
  ==> Running 'npm start' # (or your start command)
  ==> Your service is live 🎉

  # Static site
  ==> Uploading build...
  ==> Your site is live 🎉
  ```

- *If the deploy fails,* the deploy's status updates to *Failed*. Review the log feed to help identify the issue.
  - Also see [Troubleshooting Your Deploy](troubleshooting-deploys) for common solutions.
  - After you identify the issue, push a new commit to your linked branch. Render will automatically start a new deploy.

## 6. Open your app

After your app deploys successfully, you're ready to view it live.

Every Render web service and static site receives a unique `onrender.com` URL. Find this URL on your service's page in the Render Dashboard:

[image: A service's onrender.com URL]

Click the URL to open it in your browser. Your service will serve the content for its root path.

*Congratulations!* You've deployed your first app on Render 🎉

When you're ready, check out recommended [next steps](#next-steps).

## Next steps

### Connect a datastore

Render provides fully managed Postgres and Key Value instances for your data needs. Both provide a Free instance type to help you get started.

> *Free Render Postgres databases expire 30 days after creation.*
>
> You can upgrade to a paid instance at any time to keep your data. Learn more about [free instance limitations.](free)

Learn how to create datastores and connect them to your app:

- [Render Postgres databases](postgresql-creating-connecting#create-your-database)
- [Render Key Value instances](key-value#create-your-key-value-instance)

Paid services can also attach a [disk](disks) for persistence of local filesystem data (by default, local filesystem changes are [lost with each deploy](/deploys#ephemeral-filesystem)).

### Install the Render CLI

The Render CLI helps you manage your Render services right from your terminal. Trigger deploys, view logs, initiate psql sessions, and more.

[video]

[Get started with the Render CLI.](cli)

### Add a custom domain

Each Render web service and static site receives its own `onrender.com` URL. You can also add your own custom domains to these service types. [Learn how.](custom-domains)

### Learn about operational controls

Deploying your app is just the beginning. Check out a few of the ways you can manage and monitor your running services on Render:

- [Scaling your instance count](scaling)
- [Analyzing service metrics](service-metrics)
- [Rolling back a deploy](rollbacks)
- [Enabling maintenance mode](maintenance-mode)

Note that some of these capabilities require running your service on a paid instance type.

### Explore other service types

In addition to supporting web services and static sites, Render offers a variety of other service types to support any use case:

| Service type                                  | Description                                                                     |
| --------------------------------------------- | ------------------------------------------------------------------------------- |
| [*Private services*](private-services)     | Run servers that aren't reachable from the public internet.                     |
| [*Background Workers*](background-workers) | Offload long-running and computationally expensive tasks from your web servers. |
| [*Cron Jobs*](cronjobs)                    | Run periodic tasks on a schedule you define.                                    |

Note that free instances are not available for these service types.

Use this flowchart to help determine which service type is right for your use case:

[diagram]