# Source: https://render.com/docs/deploy-go-gin.md

# Deploy a Go Gin Web Server

This is a sample [Go](https://golang.org/) web server powered by the [Gin](https://github.com/gin-gonic/gin) web framework. You can use it as a starting point for deploying your own Go web apps on Render.

The [sample app](https://github.com/render-examples/go-gin-web-server) is based on Gin's [realtime chat example](https://github.com/gin-gonic/examples/tree/master/realtime-advanced), and is available at https://go-gin.onrender.com.

The app uses [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) (SSEs) to broadcast messages.

## Deployment

1. Fork [render-examples/go-gin-web-server](https://github.com/render-examples/go-gin-web-server) on GitHub.

2. Create a new *Web Service* on Render, and give Render permission to access your new repo.

3. Set the service's *Language* field to `Go` and provide the following values during creation:

   |                   |                                                |
   | ----------------- | ---------------------------------------------- |
   | *Build Command* | `go build -tags netgo -ldflags '-s -w' -o app` |
   | *Start Command* | `./app`                                        |

That's it! Your Go, Gin, and SSE powered web server will be available on your `onrender.com` URL in the dashboard as soon as the build finishes.