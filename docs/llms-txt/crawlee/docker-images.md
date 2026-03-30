# Source: https://crawlee.dev/js/docs/guides/docker-images.md

# Running in Docker

Copy for LLM

Running headless browsers in Docker requires a lot of setup to do it right. But there's no need to worry about that, because we already created base images that you can freely use. We use them every day on the [Apify Platform](https://crawlee.dev/js/docs/deployment/apify-platform.md).

All images can be found in their [GitHub repo](https://github.com/apify/apify-actor-docker) and in our [DockerHub](https://hub.docker.com/orgs/apify).

## Overview[​](#overview "Direct link to Overview")

Browsers are pretty big, so we try to provide a wide variety of images to suit the specific needs. Here's a full list of our Docker images.

* [`apify/actor-node`](#actor-node)
* [`apify/actor-node-puppeteer-chrome`](#actor-node-puppeteer-chrome)
* [`apify/actor-node-playwright`](#actor-node-playwright)
* [`apify/actor-node-playwright-chrome`](#actor-node-playwright-chrome)
* [`apify/actor-node-playwright-firefox`](#actor-node-playwright-firefox)
* [`apify/actor-node-playwright-webkit`](#actor-node-playwright-webkit)

## Versioning[​](#versioning "Direct link to Versioning")

Each image is tagged with up to 2 version tags, depending on the type of the image. One for Node.js version and second for pre-installed web automation library version. If you use the image name without a version tag, you'll always get the latest available version.

> We recommend always using at least the Node.js version tag in production Dockerfiles. It will ensure that a future update of Node.js will not break our automations.

### Node.js versioning[​](#nodejs-versioning "Direct link to Node.js versioning")

Our images are built with multiple Node.js versions to ensure backwards compatibility. Currently, Node.js **versions 16 and 18 are supported** (legacy versions still exist, see DockerHub). To select the preferred version, use the appropriate number as the image tag.

```
# Use Node.js 20
FROM apify/actor-node:20
```

### Automation library versioning[​](#automation-library-versioning "Direct link to Automation library versioning")

Images that include a pre-installed automation library, which means all images that include `puppeteer` or `playwright` in their name, are also tagged with the pre-installed version of the library. For example, `apify/actor-node-puppeteer-chrome:20-22.1.0` comes with Node.js 20 and Puppeteer v22.1.0. If you try to install a different version of Puppeteer into this image, you may run into compatibility issues, because the Chromium version bundled with `puppeteer` will not match the version of Chromium that's pre-installed.

Similarly `apify/actor-node-playwright-firefox:14-1.21.1` runs on Node.js 14 and is pre-installed with the Firefox version that comes with v1.21.1.

Installing `apify/actor-node-puppeteer-chrome` (without a tag) will install the latest available version of Node.js and `puppeteer`.

### Pre-release tags[​](#pre-release-tags "Direct link to Pre-release tags")

We also build pre-release versions of the images to test the changes we make. Those are typically denoted by a `beta` suffix, but it can vary depending on our needs. If you need to try a pre-release version, you can do it like this:

```
# Without library version.
FROM apify/actor-node:20-beta
```

```
# With library version.
FROM apify/actor-node-playwright-chrome:20-1.10.0-beta
```

## Best practices[​](#best-practices "Direct link to Best practices")

For production crawlers, we recommend pinning both the Node.js version **and** the automation library version in your Dockerfile tag. This ensures reproducible builds and prevents unexpected behavior when new versions are released.

### Recommended approach: Pin both versions[​](#recommended-approach-pin-both-versions "Direct link to Recommended approach: Pin both versions")

Match the automation library version in your `package.json` with the version in your Docker image tag:

```
FROM apify/actor-node-playwright-chrome:22-1.52.0
```

```
{
    "dependencies": {
        "crawlee": "^3.0.0",
        "playwright": "1.52.0"
    }
}
```

Why version matching matters

If you pin the Docker image to `22-1.52.0` but install a different Playwright version via `package.json`, you may encounter browser compatibility issues. The browsers pre-installed in the image are specifically built for that Playwright version.

### Alternative approach: Using asterisk `*`[​](#alternative-approach-using-asterisk- "Direct link to alternative-approach-using-asterisk-")

You can also use asterisk `*` as the automation library version in your `package.json`:

```
FROM apify/actor-node-playwright-chrome:22
```

```
{
    "dependencies": {
        "crawlee": "^3.0.0",
        "playwright": "*"
    }
}
```

This makes sure the pre-installed version of Puppeteer or Playwright is not re-installed on build. However, this approach is less predictable because you'll get whatever version was latest when the Docker image was built.

## Finding available tags[​](#finding-available-tags "Direct link to Finding available tags")

To see all available tags for each image, you can visit Docker Hub directly:

* [apify/actor-node](https://hub.docker.com/r/apify/actor-node/tags)
* [apify/actor-node-puppeteer-chrome](https://hub.docker.com/r/apify/actor-node-puppeteer-chrome/tags)
* [apify/actor-node-playwright](https://hub.docker.com/r/apify/actor-node-playwright/tags)
* [apify/actor-node-playwright-chrome](https://hub.docker.com/r/apify/actor-node-playwright-chrome/tags)
* [apify/actor-node-playwright-firefox](https://hub.docker.com/r/apify/actor-node-playwright-firefox/tags)
* [apify/actor-node-playwright-webkit](https://hub.docker.com/r/apify/actor-node-playwright-webkit/tags)

You can also query available tags programmatically:

```
curl -s "https://registry.hub.docker.com/v2/repositories/apify/actor-node-playwright-chrome/tags?page_size=50" | jq '.results[].name'
```

### Warning about image size[​](#warning-about-image-size "Direct link to Warning about image size")

Browsers are huge. If you don't need them all in your image, it's better to use a smaller image with only the one browser you need.

You should also be careful when installing new dependencies. Nothing prevents you from installing Playwright into the`actor-node-puppeteer-chrome` image, but the resulting image will be about 3 times larger and extremely slow to download and build.

When you use only what you need, you'll be rewarded with reasonable build and start times.

## Apify Docker Images[​](#apify-docker-images "Direct link to Apify Docker Images")

### actor-node[​](#actor-node "Direct link to actor-node")

This is the smallest image we have based on Alpine Linux. It does not include any browsers, and it's therefore best used with [`CheerioCrawler`](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md). It benefits from lightning fast builds and container startups.

​[`PuppeteerCrawler`](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md), [`PlaywrightCrawler`](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md) and other browser based features will **NOT** work with this image.

```
FROM apify/actor-node:20
```

### actor-node-puppeteer-chrome[​](#actor-node-puppeteer-chrome "Direct link to actor-node-puppeteer-chrome")

This image includes Puppeteer (Chromium) and the Chrome browser. It can be used with [`CheerioCrawler`](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md) and [`PuppeteerCrawler`](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md), but **NOT** with [`PlaywrightCrawler`](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md).

The image supports XVFB by default, so you can run both `headless` and `headful` browsers with it.

```
FROM apify/actor-node-puppeteer-chrome:20
```

### actor-node-playwright[​](#actor-node-playwright "Direct link to actor-node-playwright")

A very large and slow image that can run all Playwright browsers: Chromium, Chrome, Firefox, WebKit. Everything is installed. If you need to develop or test with multiple browsers, this is the image to choose, but in most cases, it's better to use the specialized images below.

```
FROM apify/actor-node-playwright:20
```

### actor-node-playwright-chrome[​](#actor-node-playwright-chrome "Direct link to actor-node-playwright-chrome")

Similar to [`actor-node-puppeteer-chrome`](#actor-node-puppeteer-chrome), but for Playwright. You can run [`CheerioCrawler`](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md) and [`PlaywrightCrawler`](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md), but **NOT** [`PuppeteerCrawler`](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md).

It uses the [`PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD`](https://playwright.dev/docs/api/environment-variables/) environment variable to block installation of more browsers into the image to keep it small. If you want more browsers, either use the [`actor-node-playwright`](#actor-node-playwright) image override this env var.

The image supports XVFB by default, so we can run both `headless` and `headful` browsers with it.

```
FROM apify/actor-node-playwright-chrome:20
```

### actor-node-playwright-firefox[​](#actor-node-playwright-firefox "Direct link to actor-node-playwright-firefox")

Same idea as [`actor-node-playwright-chrome`](#actor-node-playwright-chrome), but with Firefox pre-installed.

```
FROM apify/actor-node-playwright-firefox:20
```

### actor-node-playwright-webkit[​](#actor-node-playwright-webkit "Direct link to actor-node-playwright-webkit")

Same idea as [`actor-node-playwright-chrome`](#actor-node-playwright-chrome), but with WebKit pre-installed.

```
FROM apify/actor-node-playwright-webkit:20
```

## Example Dockerfile[​](#example-dockerfile "Direct link to Example Dockerfile")

To use the above images, it's necessary to have a [`Dockerfile`](https://docs.docker.com/engine/reference/builder/). You can either use this example, or bootstrap your projects with the [Crawlee CLI](https://crawlee.dev/js/docs/introduction/setting-up.md) which automatically adds the correct Dockerfile into our project folder.

* Node+JavaScript
* Node+TypeScript
* Browser+JavaScript
* Browser+TypeScript

```
# Specify the base Docker image. You can read more about
# the available images at https://crawlee.dev/js/docs/guides/docker-images
# You can also use any other image from Docker Hub.
FROM apify/actor-node:20

# Copy just package.json and package-lock.json
# to speed up the build using Docker layer cache.
COPY package*.json ./

# Install NPM packages, skip optional and development dependencies to
# keep the image small. Avoid logging too much and print the dependency
# tree for debugging
RUN npm --quiet set progress=false \
    && npm install --omit=dev --omit=optional \
    && echo "Installed NPM packages:" \
    && (npm list --omit=dev --all || true) \
    && echo "Node.js version:" \
    && node --version \
    && echo "NPM version:" \
    && npm --version

# Next, copy the remaining files and directories with the source code.
# Since we do this after NPM install, quick build will be really fast
# for most source file changes.
COPY . ./


# Run the image.
CMD npm start --silent
```

```
# Specify the base Docker image. You can read more about
# the available images at https://crawlee.dev/js/docs/guides/docker-images
# You can also use any other image from Docker Hub.
FROM apify/actor-node:20 AS builder

# Copy just package.json and package-lock.json
# to speed up the build using Docker layer cache.
COPY package*.json ./

# Install all dependencies. Don't audit to speed up the installation.
RUN npm install --include=dev --audit=false

# Next, copy the source files using the user set
# in the base image.
COPY . ./

# Install all dependencies and build the project.
# Don't audit to speed up the installation.
RUN npm run build

# Create final image
FROM apify/actor-node:20

# Copy only built JS files from builder image
COPY --from=builder /usr/src/app/dist ./dist

# Copy just package.json and package-lock.json
# to speed up the build using Docker layer cache.
COPY package*.json ./

# Install NPM packages, skip optional and development dependencies to
# keep the image small. Avoid logging too much and print the dependency
# tree for debugging
RUN npm --quiet set progress=false \
    && npm install --omit=dev --omit=optional \
    && echo "Installed NPM packages:" \
    && (npm list --omit=dev --all || true) \
    && echo "Node.js version:" \
    && node --version \
    && echo "NPM version:" \
    && npm --version

# Next, copy the remaining files and directories with the source code.
# Since we do this after NPM install, quick build will be really fast
# for most source file changes.
COPY . ./


# Run the image.
CMD npm run start:prod --silent
```

This example is for Playwright. If you want to use Puppeteer, simply replace **playwright** with **puppeteer** in the `FROM` declaration.

```
# Specify the base Docker image. You can read more about
# the available images at https://crawlee.dev/js/docs/guides/docker-images
# You can also use any other image from Docker Hub.
FROM apify/actor-node-playwright-chrome:20

# Copy just package.json and package-lock.json
# to speed up the build using Docker layer cache.
COPY --chown=myuser package*.json ./

# Install NPM packages, skip optional and development dependencies to
# keep the image small. Avoid logging too much and print the dependency
# tree for debugging
RUN npm --quiet set progress=false \
    && npm install --omit=dev --omit=optional \
    && echo "Installed NPM packages:" \
    && (npm list --omit=dev --all || true) \
    && echo "Node.js version:" \
    && node --version \
    && echo "NPM version:" \
    && npm --version

# Next, copy the remaining files and directories with the source code.
# Since we do this after NPM install, quick build will be really fast
# for most source file changes.
COPY --chown=myuser . ./


# Run the image.
CMD npm start --silent
```

This example is for Playwright. If you want to use Puppeteer, simply replace **playwright** with **puppeteer** in both `FROM` declarations.

```
# Specify the base Docker image. You can read more about
# the available images at https://crawlee.dev/js/docs/guides/docker-images
# You can also use any other image from Docker Hub.
FROM apify/actor-node-playwright-chrome:20 AS builder

# Copy just package.json and package-lock.json
# to speed up the build using Docker layer cache.
COPY --chown=myuser package*.json ./

# Install all dependencies. Don't audit to speed up the installation.
RUN npm install --include=dev --audit=false

# Next, copy the source files using the user set
# in the base image.
COPY --chown=myuser . ./

# Install all dependencies and build the project.
# Don't audit to speed up the installation.
RUN npm run build

# Create final image
FROM apify/actor-node-playwright-chrome:20

# Copy only built JS files from builder image
COPY --from=builder --chown=myuser /home/myuser/dist ./dist

# Copy just package.json and package-lock.json
# to speed up the build using Docker layer cache.
COPY --chown=myuser package*.json ./

# Install NPM packages, skip optional and development dependencies to
# keep the image small. Avoid logging too much and print the dependency
# tree for debugging
RUN npm --quiet set progress=false \
    && npm install --omit=dev --omit=optional \
    && echo "Installed NPM packages:" \
    && (npm list --omit=dev --all || true) \
    && echo "Node.js version:" \
    && node --version \
    && echo "NPM version:" \
    && npm --version

# Next, copy the remaining files and directories with the source code.
# Since we do this after NPM install, quick build will be really fast
# for most source file changes.
COPY --chown=myuser . ./


# Run the image. If you know you won't need headful browsers,
# you can remove the XVFB start script for a micro perf gain.
CMD ./start_xvfb_and_run_cmd.sh && npm run start:prod --silent
```
