# Source: https://render.com/docs/deploy-bun-docker.md

# Deploy a Bun HTTP Server with Docker


> Render now supports Bun natively, so you can use Bun without Docker.
>
> Learn more in our [language support docs](language-support).

[Bun](https://bun.com/) is a fast JavaScript runtime that serves as a bundler, test runner, and package manager.

You can use Render to host a simple [Bun HTTP server](https://bun.com/docs/api/http) using Docker.

1. Fork [render-examples/bun-docker](https://github.com/render-examples/bun-docker) on GitHub or click *Use this template*.

2. Create a new *web service* on Render, and give Render permission to access your new repo.

3. Set the web service's *Language* field to `Docker`.

That's it! Your web service will be live on your Render URL as soon as the build finishes.

## One-click deploy

<deploy-to-render repo="https://github.com/render-examples/bun-docker">
</deploy-to-render>