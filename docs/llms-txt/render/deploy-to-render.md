# Source: https://render.com/docs/deploy-to-render.md

# Deploy to Render Button

You can make it easy for others to deploy your services to Render using the Deploy to Render button.

[image: Deploy to Render button]

Once you add the Deploy to Render button to a `README` in your repo, your users can simply click the button, review the
services to be deployed on their Render account and click approve to set everything up instantly and without any
additional work.

Follow these steps to add the button for your repo.

1. Create a [render.yaml](infrastructure-as-code) file describing the services you want to deploy from your
   repository.

2. Make sure your repository is accessible to your users.

   - Public repos are supported out of the box.
   - For private GitHub repos install [Render's GitHub App](https://github.com/apps/render) on your repo.
   - For private GitLab and Bitbucket repos, grant your users clone access to the repo.

3. Add the Deploy to Render button to your GitHub/GitLab/Bitbucket `README.md`.

   ```markdown
   [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
   ```

   If you're not using Markdown for the `README` add an image from
   https://render.com/images/deploy-to-render-button.svg linking to https://render.com/deploy.

   By default, Render uses the *referrer of the page* containing the Deploy to Render button to detect the repository
   to deploy. You can also explicitly specify a repository as shown below.

## Specifying a Repository

It's strongly recommended that you append a `repo` query string parameter to the button's target URL. Without it, the
Git repository URL is determined from the [`Referer`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer)
header, however many browsers no longer include the full URL in the `Referer` header due
to [privacy and security concerns](https://developer.mozilla.org/en-US/docs/Web/Security/Referer_header:_privacy_and_security_concerns)
.

Set the value of `repo` to the full `https://` URL for your Git repo. Here's an example.

```html
<a
  href="https://render.com/deploy?repo=https://github.com/render-examples/mattermost"
>
  <img
    src="https://render.com/images/deploy-to-render-button.svg"
    alt="Deploy to Render"
  />
</a>
```

### Specifying a Branch

By default the repo's default branch (normally `main` or `master`) is deployed. You can deploy a different branch by
appending `/tree/branch_name` to the end of the `repo` query parameter. As an example, the link below will deploy a
branch named `bugfix-123`.

```html
<a
  href="https://render.com/deploy?repo=https://github.com/render-examples/mattermost/tree/bugfix-123"
>
  <img
    src="https://render.com/images/deploy-to-render-button.svg"
    alt="Deploy to Render"
  />
</a>
```

## Configuring Auto-Deploys

When using the Deploy to Render button to deploy via a `render.yaml` Blueprint Spec contained in the service's
repo, special consideration must be taken with regard to the
service's [Auto-Deploy](/deploys#automatic-git-deploys) settings. For a service that is meant to be
deployed via a Deploy to Render button, it is strongly advised to set `autoDeploy: false` via
the `render.yaml` [Blueprint Spec](blueprint-spec). This ensures that code pushes
to the repo that contains the Deploy to Render button don't trigger an automatic deploy of every instance deployed via
the Deploy to Render button.

## Button Generator

Paste your GitHub/GitLab/Bitbucket repo URL to generate a Deploy to Render button as Markdown or HTML.

<deploy-to-render-generator>

> It's recommended to specify a repo URL. Without it, the URL is
> determined from the [Referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer)
> header; many browsers no longer include the full URL in the Referer
> header due
> to [privacy and security concerns](https://developer.mozilla.org/en-US/docs/Web/Security/Referer_header:_privacy_and_security_concerns)
> .

</deploy-to-render-generator>