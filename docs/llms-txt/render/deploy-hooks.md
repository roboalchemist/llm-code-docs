# Source: https://render.com/docs/deploy-hooks.md

# Deploy Hooks — Trigger a deploy with a single HTTP request.

*Deploy hooks* enable you to trigger an on-demand deploy of your Render service with a single HTTP request. Use deploy hooks with:

- CI/CD environments like GitHub Actions ([see an example](#using-with-github-actions))
- [Image-backed services](#deploying-from-an-image-registry) (to trigger a deploy when a new image is available)
- Headless CMS systems like [Contentful](https://www.contentful.com/developers/docs/concepts/webhooks/) (to trigger a deploy when content changes)

> *Looking for webhooks?* See [this article](webhooks).

## Triggering a deploy

Each service has a secret *deploy hook URL*, available from its *Settings* tab in the [Render Dashboard](https://dashboard.render.com):

[image: A service's deploy hook URL in the Render Dashboard]

> *Your deploy hook URL is a secret!*
>
> Provide the URL only to people and systems you trust to trigger deploys. If you believe a deploy hook URL has been compromised, replace it by clicking *Regenerate Hook*.

To trigger a deploy, send a basic `GET` or `POST` request to your service's deploy hook URL—no special headers required.

```bash
curl https://api.render.com/deploy/srv-xyz…
```

## Deploying from an image registry

[Image-backed services](/deploying-an-image) on Render pull and deploy a prebuilt Docker image from an external registry. These services do _not_ automatically redeploy if a new image is pushed to the registry. You can use a deploy hook to trigger a deploy whenever an updated image is available.

To deploy a specific tag or digest, append the `imgURL` query parameter to your deploy hook URL:

```bash
# Append a string with this format to your deploy hook URL.
# This example deploys the image `nginx:1.26` from Docker Hub.
# Note the URL-encoding.
&imgURL=docker.io%2Flibrary%2Fnginx%401.26
```

If you _don't_ provide this parameter, Render uses whichever tag or digest you've specified in the service's settings.

> All components of `imgURL` _besides_ the tag or digest must match your service's default image URL. Otherwise, Render rejects the deploy request.

## Using with GitHub Actions

You might want to trigger a service deploy from your CI/CD environment whenever certain conditions are met (such as when all of your tests pass). Let's set this up using deploy hooks and [GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions).

### 1. Create a repository secret

Deploy hook URLs are secret values, so we need to make sure to [store ours as a secret](https://docs.github.com/en/actions/reference/encrypted-secrets) in our GitHub repo:

1. Go to your GitHub repo's *Settings* page.
2. Click *Secrets and variables > Actions*.
3. Click *New repository secret*. Create a secret with the name `RENDER_DEPLOY_HOOK_URL` and provide your deploy hook URL as the value:

   [image: Repository secret for a GitHub action]

### 2. Add a GitHub workflow

Now that we've added our deploy hook URL, let's create a GitHub workflow that uses it:

1. Create a `.github/workflows` directory in your repo if it doesn't already exist. GitHub Actions automatically detects and runs any workflows defined in this folder.
2. Add a YAML file to this directory to represent your new workflow. The [example below](#example-workflow) uses the file path `.github/workflows/ci.yml`.
3. Define logic in your workflow to trigger a deploy after any prerequisite steps succeed. [See the example.](#example-workflow)
4. Commit all of your changes.

#### Example workflow

This example workflow defines a job named `ci` that includes two steps (`Test` and `Deploy`). The workflow runs whenever any pull request is opened against `main`, or when commits are pushed to `main`.

1. The `Test` step runs the repo's defined unit tests.
2. The `Deploy` step executes a `curl` request to our deploy hook URL _only if_ the current branch is `main` _and_ the `Test` step succeeded.

```yaml
# .github/workflows/ci.yml

on:
  pull_request:
  push:
    branches: [main]

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - name: Test
        run: |
          npm install
          npm run test

      - name: Deploy
        # Only run this step if the branch is main
        if: github.ref == 'refs/heads/main'
        env:
          deploy_url: ${{ secrets.RENDER_DEPLOY_HOOK_URL }}
        run: |
          curl "$deploy_url"
```