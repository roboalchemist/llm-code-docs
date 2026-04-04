# Source: https://nitro.build/deploy/providers/gitlab-pages

-   [](/guide "Getting Started")

    ::: 
    []
    :::

    [Getting Started]
-   [](/deploy "Overview")

    ::: 
    []
    :::

    [Overview]
-   [](/config "Config")

    ::: 
    []
    :::

    [Config]

-   [[][Overview]](/deploy)
-   [[][Edge Workers]](/deploy/workers)
-   [Runtimes]

    ::: 
    -   [[][Node.js]](/deploy/runtimes/node)
    -   [[][WinterJS]](/deploy/runtimes/_winterjs)
    -   [[][Bun]](/deploy/runtimes/bun)
    -   [[][Deno]](/deploy/runtimes/deno)
    :::
-   [[][Custom Preset]](/deploy/custom-presets)
-   [Providers]

    ::: 
    -   [[Alwaysdata]](/deploy/providers/alwaysdata)
    -   [[AWS Lambda]](/deploy/providers/aws)
    -   [[AWS Amplify]](/deploy/providers/aws-amplify)
    -   [[Azure]](/deploy/providers/azure)
    -   [[Cleavr]](/deploy/providers/cleavr)
    -   [[Cloudflare]](/deploy/providers/cloudflare)
    -   [[Deno Deploy]](/deploy/providers/deno-deploy)
    -   [[DigitalOcean]](/deploy/providers/digitalocean)
    -   [[Edgio]](/deploy/providers/edgio)
    -   [[Firebase]](/deploy/providers/firebase)
    -   [[Flightcontrol]](/deploy/providers/flightcontrol)
    -   [[Genezio]](/deploy/providers/genezio)
    -   [[GitHub Pages]](/deploy/providers/github-pages)
    -   [[GitLab Pages]](/deploy/providers/gitlab-pages)
    -   [[Heroku]](/deploy/providers/heroku)
    -   [[IIS]](/deploy/providers/iis)
    -   [[Koyeb]](/deploy/providers/koyeb)
    -   [[Netlify]](/deploy/providers/netlify)
    -   [[Platform.sh]](/deploy/providers/platform-sh)
    -   [[Render.com]](/deploy/providers/render)
    -   [[StormKit]](/deploy/providers/stormkit)
    -   [[Vercel]](/deploy/providers/vercel)
    -   [[Zeabur]](/deploy/providers/zeabur)
    -   [[Zerops]](/deploy/providers/zerops)
    :::

1.  [[Providers]]

<div>

# GitLab Pages 

Deploy Nitro apps to GitLab Pages.

</div>

<div>

**Preset:** `gitlab_pages`

[[]](https://pages.github.com/)[][] Read more in [GitLab Pages].

## [[[]]Setup](#setup) 

Follow the steps to [create a GitLab Pages site](https://docs.gitlab.com/ee/user/project/pages/#getting-started).

## [[[]]Deployment](#deployment) 

1.  Here is an example GitLab Pages workflow to deploy your site to GitLab Pages:

[][.gitlab-ci.yml]

[]

``` 
image: node:lts
before_script:
  - npx nypm install
pages:
  cache:
    paths:
      - node_modules/
  variables:
    NITRO_PRESET: gitlab_pages
  script:
    - npm run build
  artifacts:
    paths:
      - .output/public
  publish: .output/public
  rules:
    # This ensures that only pushes to the default branch
    # will trigger a pages deploy
    - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
```

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/gitlab-pages.md)

[](/deploy/providers/github-pages)

[]

GitHub Pages

Deploy Nitro apps to GitHub Pages.

[](/deploy/providers/heroku)

[]

Heroku

Deploy Nitro apps to Heroku.

[On this page][[]]

[On this page][[]]

-   [[Setup]](#setup)
-   [[Deployment]](#deployment)