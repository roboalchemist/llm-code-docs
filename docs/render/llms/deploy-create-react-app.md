# Source: https://render.com/docs/deploy-create-react-app.md

# Deploy a Create React App Static Site

You can deploy a [Create React App](https://github.com/facebook/create-react-app) static site on Render in under a minute. Your site is served over a *lightning-fast global CDN*, comes with *fully managed TLS* certificates, and supports *custom domains* out of the box.

The sample app for this quick start is deployed at https://cra.onrender.com.

1. Use your existing React repository, or fork our sample React repo on [GitHub](https://github.com/render-examples/create-react-app) or [GitLab](https://gitlab.com/render-examples/create-react-app).
2. Create a new *Static Site* on Render, and give Render permission to access your new repo.
3. Use the following values during creation:

   |                       |                    |
   | --------------------- | ------------------ |
   | *Build Command*     | `yarn; yarn build` |
   | *Publish Directory* | `build`            |

That's it! Your app will be live on your Render URL as soon as the build finishes.

## Using Client-Side Routing

If you use [Reach Router](https://github.com/reach/router) or [React Router](https://github.com/ReactTraining/react-router) for [client-side routing](https://facebook.github.io/create-react-app/docs/deployment#serving-apps-with-client-side-routing), you will need to direct all routing requests to `index.html` so they can be handled by your routing library.

You can do this easily by defining a *Rewrite Rule* for your static site. Go to the *Redirects/Rewrites* tab for your service and add a rule with the following values:

|                  |               |
| ---------------- | ------------- |
| Source Path      | `/*`          |
| Destination Path | `/index.html` |
| Action           | `Rewrite`     |

The result should look like this:

[image: React Router Rewrite]

See [Specifying a Node Version](node-version) if you need to customize the version of Node.js used for your site.

## Environment Variables

React can consume environment variables that are exposed via `REACT_APP_` prefix.

Sometimes you may want to use [environment variables](environment-variables) we expose to your service.

> Do not store secrets in your React app - see https://create-react-app.dev/docs/adding-custom-environment-variables/ for more details.

You can do this by updating your build command to expose the variables you require, for example to access `RENDER_GIT_COMMIT` you would change your Build Command to be `REACT_APP_RENDER_GIT_COMMTL=$RENDER_GIT_COMMIT yarn build`

Alternatively, changing your Build Command to use a script, eg `render-build.sh` you could achieve similar as well as being able to version control the file with:

```bash
#!/usr/bin/env bash
# exit on error
set -o errexit

export REACT_APP_RENDER_GIT_COMMIT=$RENDER_GIT_COMMIT

yarn build
```