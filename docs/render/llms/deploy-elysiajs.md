# Source: https://render.com/docs/deploy-elysiajs.md

# Deploy ElysiaJS with Bun

[ElysiaJS](https://elysiajs.com/) is a web framework for building backend servers with Bun. [Bun](https://bun.com/) is a fast JavaScript runtime that serves as a bundler, test runner, and package manager.

You can use Render to host an ElysiaJS app. Render [supports Bun](language-support) natively.

## Deploying from the Render Dashboard

1. Fork [render-examples/elysiajs-hello-world](https://github.com/render-examples/elysiajs-hello-world) on GitHub.

2. Create a new *web service* on Render, and give Render permission to access your new repo.

3. Provide the following values during service creation:

   | Setting           | Value         |
   | ----------------- | ------------- |
   | *Language*      | `Node`        |
   | *Build Command* | `bun install` |
   | *Start Command* | `bun start`   |

That's it! Your web service will be live at its `onrender.com` URL as soon as the deploy finishes.

## Deploying with a Blueprint (Infrastructure as Code)

1. Fork [render-examples/elysiajs-hello-world](https://github.com/render-examples/elysiajs-hello-world) on GitHub.

2. In the included `render.yaml` file, set the `repo` field to the URL of your fork. Commit this change.

3. Follow [these steps](infrastructure-as-code#setup) to create a new Blueprint using the `render.yaml` file.

That's it! Your web service will be live on your Render URL as soon as the deploy finishes.