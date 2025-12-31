# Source: https://playwright.dev/docs/docker

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Integrations]
-   [Docker]

On this page

<div>

# Docker

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

[Dockerfile.noble](https://github.com/microsoft/playwright/blob/main/utils/docker/Dockerfile.noble "Dockerfile.noble") can be used to run Playwright scripts in Docker environment. This image includes the [Playwright browsers](/docs/browsers#install-browsers) and [browser system dependencies](/docs/browsers#install-system-dependencies). The Playwright package/dependency is not included in the image and should be installed separately.

## Usage[​](#usage "Direct link to Usage") 

This Docker image is published to [Microsoft Artifact Registry](https://mcr.microsoft.com/en-us/product/playwright/about "Microsoft Artifact Registry").

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

This Docker image is intended to be used for testing and development purposes only. It is not recommended to use this Docker image to visit untrusted websites.

### Pull the image[​](#pull-the-image "Direct link to Pull the image") 

``` 
docker pull mcr.microsoft.com/playwright:v1.57.0-noble
```

### Run the image[​](#run-the-image "Direct link to Run the image") 

By default, the Docker image will use the `root` user to run the browsers. This will disable the Chromium sandbox which is not available with root. If you run trusted code (e.g. End-to-end tests) and want to avoid the hassle of managing separate user then the root user may be fine. For web scraping or crawling, we recommend to create a separate user inside the Docker container and use the seccomp profile.

#### End-to-end tests[​](#end-to-end-tests "Direct link to End-to-end tests") 

On trusted websites, you can avoid creating a separate user and use root for it since you trust the code which will run on the browsers.

``` 
docker run -it --rm --ipc=host mcr.microsoft.com/playwright:v1.57.0-noble /bin/bash
```

#### Crawling and scraping[​](#crawling-and-scraping "Direct link to Crawling and scraping") 

On untrusted websites, it\'s recommended to use a separate user for launching the browsers in combination with the seccomp profile. Inside the container or if you are using the Docker image as a base image you have to use `adduser` for it.

``` 
docker run -it --rm --ipc=host --user pwuser --security-opt seccomp=seccomp_profile.json mcr.microsoft.com/playwright:v1.57.0-noble /bin/bash
```

[`seccomp_profile.json`](https://github.com/microsoft/playwright/blob/main/utils/docker/seccomp_profile.json) is needed to run Chromium with sandbox. This is a [default Docker seccomp profile](https://github.com/docker/engine/blob/d0d99b04cf6e00ed3fc27e81fc3d94e7eda70af3/profiles/seccomp/default.json) with extra user namespace cloning permissions:

``` 
,
  "excludes": 
}
```

### Recommended Docker Configuration[​](#recommended-docker-configuration "Direct link to Recommended Docker Configuration") 

When running Playwright in Docker, the following configuration is recommended:

1.  **Using [`--init`](https://docs.docker.com/reference/cli/docker/container/run/#init)** Docker flag is recommended to avoid special treatment for processes with PID=1. This is a common reason for zombie processes.
2.  **Using `--ipc=host`** is recommended when using Chromium. Without it, Chromium can run out of memory and crash. Learn more about this option in [Docker docs](https://docs.docker.com/reference/cli/docker/container/run/#ipc).
3.  **If seeing weird errors when launching Chromium**, try running your container with `docker run --cap-add=SYS_ADMIN` when developing locally.

### Using on CI[​](#using-on-ci "Direct link to Using on CI") 

See our [Continuous Integration guides](/docs/ci) for sample configs.

### Remote Connection[​](#remote-connection "Direct link to Remote Connection") 

You can run Playwright Server in Docker while keeping your tests running on the host system or another machine. This is useful for running tests on unsupported Linux distributions or remote execution scenarios.

#### Running the Playwright Server[​](#running-the-playwright-server "Direct link to Running the Playwright Server") 

Start the Playwright Server in Docker:

``` 
docker run -p 3000:3000 --rm --init -it --workdir /home/pwuser --user pwuser mcr.microsoft.com/playwright:v1.57.0-noble /bin/sh -c "npx -y playwright@1.57.0 run-server --port 3000 --host 0.0.0.0"
```

#### Connecting to the Server[​](#connecting-to-the-server "Direct link to Connecting to the Server") 

There are two ways to connect to the remote Playwright server:

1.  Using environment variable with `@playwright/test`:

``` 
PW_TEST_CONNECT_WS_ENDPOINT=ws://127.0.0.1:3000/ npx playwright test
```

2.  Using the [browserType.connect()](/docs/api/class-browsertype#browser-type-connect) API for other applications:

``` 
const browser = await playwright['chromium'].connect('ws://127.0.0.1:3000/');
```

#### Network Configuration[​](#network-configuration "Direct link to Network Configuration") 

If you need to access local servers from within the Docker container:

``` 
docker run --add-host=hostmachine:host-gateway -p 3000:3000 --rm --init -it --workdir /home/pwuser --user pwuser mcr.microsoft.com/playwright:v1.57.0-noble /bin/sh -c "npx -y playwright@1.57.0 run-server --port 3000 --host 0.0.0.0"
```

This makes `hostmachine` point to the host\'s localhost. Your tests should use `hostmachine` instead of `localhost` when accessing local servers.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

When running tests remotely, ensure the Playwright version in your tests matches the version running in the Docker container.

## Image tags[​](#image-tags "Direct link to Image tags") 

See [all available image tags](https://mcr.microsoft.com/en-us/product/playwright/about "all available image tags").

We currently publish images with the following tags:

-   `:v1.57.0` - Playwright v1.57.0 release docker image based on Ubuntu 24.04 LTS (Noble Numbat).
-   `:v1.57.0-noble` - Playwright v1.57.0 release docker image based on Ubuntu 24.04 LTS (Noble Numbat).
-   `:v1.57.0-jammy` - Playwright v1.57.0 release docker image based on Ubuntu 22.04 LTS (Jammy Jellyfish).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

It is recommended to always pin your Docker image to a specific version if possible. If the Playwright version in your Docker image does not match the version in your project/tests, Playwright will be unable to locate browser executables.

### Base images[​](#base-images "Direct link to Base images") 

We currently publish images based on the following [Ubuntu](https://hub.docker.com/_/ubuntu) versions:

-   **Ubuntu 24.04 LTS** (Noble Numbat), image tags include `noble`
-   **Ubuntu 22.04 LTS** (Jammy Jellyfish), image tags include `jammy`

#### Alpine[​](#alpine "Direct link to Alpine") 

Browser builds for Firefox and WebKit are built for the [glibc](https://en.wikipedia.org/wiki/Glibc) library. Alpine Linux and other distributions that are based on the [musl](https://en.wikipedia.org/wiki/Musl) standard library are not supported.

## Build your own image[​](#build-your-own-image "Direct link to Build your own image") 

To run Playwright inside Docker, you need to have Node.js, [Playwright browsers](/docs/browsers#install-browsers) and [browser system dependencies](/docs/browsers#install-system-dependencies) installed. See the following Dockerfile:

``` 
FROM node:20-bookworm

RUN npx -y playwright@1.57.0 install --with-deps
```