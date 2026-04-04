# Source: https://electric-sql.com/docs/integrations/netlify.md

---
url: /docs/integrations/netlify.md
description: How to deploy Electric apps on Netlify.
---

# Netlify

[Netlify](https://www.netlify.com/) is an [application deployment platform](https://www.netlify.com/platform/).

## Electric and Netlify

Netlify is a great choice for deploying client-side web apps that use Electric.

> \[!Tip] Need context?
> See the [Deployment guide](/docs/guides/deployment) for more details.

### Deploy your app

[Create your app](https://docs.netlify.com/welcome/add-new-site/), connect it to Netlify and [deploy via `git push`](https://docs.netlify.com/site-deploys/create-deploys/#deploy-with-git).

### Connect to Electric

> \[!Warning] You need Electric (and Postgres) running somewhere else
> The easiest way is to use the [Electric Cloud](/cloud). Or see the [Deployment guide](/docs/guides/deployment).

Copy the URL to your Electric instance and use it when [syncing data](/docs/api/clients/typescript#shape) into your app. E.g.: by [setting an environment variable](https://docs.netlify.com/environment-variables/get-started/#site-environment-variables) and using it in your code:

```tsx
const ELECTRIC_URL = process.env.ELECTRIC_URL

const stream = new ShapeStream({
  url: `${ELECTRIC_URL}/v1/shape`,
  params: {
    table: 'items',
  },
})
```

See the [Client docs](/docs/api/clients/typescript) for more information.

## Example

### Deploy example app

Deploy our [standalone-basic-example](https://github.com/electric-sql/standalone-basic-example) app using the form below:
