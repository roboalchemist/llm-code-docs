# Source: https://nitro.build/deploy/providers/koyeb

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

# Koyeb 

Deploy Nitro apps to Koyeb.

</div>

<div>

**Preset:** `koyeb`

[[]](https://www.koyeb.com)[][] Read more in [www.koyeb.com].

## [[[]]Using the control panel](#using-the-control-panel) 

#### In the [Koyeb control panel](https://app.koyeb.com/), click **Create App**. 

#### Choose **GitHub** as your deployment method. 

#### Choose the GitHub **repository** and **branch** containing your application code. 

#### Name your Service. 

#### If you did not add a `start` command to your `package.json` file, under the **Build and deployment settings**, toggle the override switch associated with the run command field. In the **Run command** field, enter: 

[]

``` 
node .output/server/index.mjs`
```

#### In the **Advanced** section, click **Add Variable** and add a `NITRO_PRESET` variable set to `koyeb`. 

#### Name the App. 

#### Click the **Deploy** button. 

## [[[]]Using the Koyeb CLI](#using-the-koyeb-cli) 

#### Follow the instructions targeting your operating system to [install the Koyeb CLI client](https://www.koyeb.com/docs/cli/installation) with an installer. Alternatively, visit the [releases page on GitHub](https://github.com/koyeb/koyeb-cli/releases) to directly download required files. 

#### Create a Koyeb API access token by visiting the [API settings for your organization](https://app.koyeb.com/settings/api) in the Koyeb control panel. 

#### Log into your account with the Koyeb CLI by typing: 

[]

``` 
koyeb login
```

\
Paste your API credentials when prompted.

#### Deploy your Nitro application from a GitHub repository with the following command. Be sure to substitute your own values for `<APPLICATION_NAME>`, `<YOUR_GITHUB_USERNAME>`, and `<YOUR_REPOSITORY_NAME>`: 

[]

``` 
koyeb app init <APPLICATION_NAME> \
   --git github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPOSITORY_NAME> \
   --git-branch main \
   --git-run-command "node .output/server/index.mjs" \
   --ports 3000:http \
   --routes /:3000 \
   --env PORT=3000 \
   --env NITRO_PRESET=koyeb
```

## [[[]]Using a docker container](#using-a-docker-container) 

#### Create a `.dockerignore` file in the root of your project and add the following lines: 

[]

``` 
Dockerfile
.dockerignore
node_modules
npm-debug.log
.nitro
.output
.git
dist
README.md
```

#### Add a `Dockerfile` to the root of your project: 

[]

``` 
FROM node:18-alpine AS base

FROM base AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build && npm cache clean --force

FROM base AS runner
WORKDIR /app
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nitro
COPY --from=builder /app .
USER nitro
EXPOSE 3000
ENV PORT 3000
CMD ["npm", "run", "start"]
```

The Dockerfile above provides the minimum requirements to run the Nitro application. You can easily extend it depending on your needs. You will then need to push your Docker image to a registry. You can use [Docker Hub](https://hub.docker.com/) or [GitHub Container Registry](https://docs.github.com/en/packages/guides/about-github-container-registry) for example. In the Koyeb control panel, use the image and the tag field to specify the image you want to deploy. You can also use the [Koyeb CLI](https://www.koyeb.com/docs/build-and-deploy/cli/installation) Refer to the Koyeb [Docker documentation](https://www.koyeb.com/docs/build-and-deploy/prebuilt-docker-images) for more information.

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/koyeb.md)

[](/deploy/providers/iis)

[]

IIS

Deploy Nitro apps to IIS.

[](/deploy/providers/netlify)

[]

Netlify

Deploy Nitro apps to Netlify functions or edge.

[On this page][[]]

[On this page][[]]

-   [[Using the control panel]](#using-the-control-panel)
-   [[Using the Koyeb CLI]](#using-the-koyeb-cli)
-   [[Using a docker container]](#using-a-docker-container)