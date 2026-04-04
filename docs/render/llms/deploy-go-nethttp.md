# Source: https://render.com/docs/deploy-go-nethttp.md

# Deploy a Go Web Server on Render — Run a web service using Go's standard library.

You can deploy a Go `net/http` web server on Render in just a few clicks.

This quickstart uses a basic example app. You're welcome to use your own Go app instead.

1. Fork the [render-examples/go-web-server](https://github.com/render-examples/go-web-server) repo on GitHub.

> A demo instance of this app is hosted at [go-web-server-0tcz.onrender.com](https://go-web-server-0tcz.onrender.com/).

2. In the [Render Dashboard](https://dashboard.render.com), click *New > Web Service* and connect your new repo.

3. Provide the following values during creation:

   |                   |                                                |
   | ----------------- | ---------------------------------------------- |
   | *Language*      | `Go`                                           |
   | *Build Command* | `go build -tags netgo -ldflags '-s -w' -o app` |
   | *Start Command* | `./app`                                        |

> *Using your own app?*
>
>    Instead provide whatever commands you use to build and start it, if they differ from the above.

4. Click *Deploy Web Service*.

That's it! Your Go-powered web server will be live at its unique `onrender.com` URL as soon as the deploy finishes.

Going forward, every push to your linked branch automatically builds and deploys your app. If a build fails, Render cancels the deploy, and your app's existing version continues running until the next successful deploy. [Learn more about deploys.](/deploys)