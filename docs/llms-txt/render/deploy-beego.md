# Source: https://render.com/docs/deploy-beego.md

# Deploy a Beego Web App

This is a sample Go web app built with [Beego](https://github.com/astaxie/beego) and [gorilla/websocket](https://github.com/gorilla/websocket). It is based on [Beego's chat example](https://beego.me/docs/examples/chat.md).

It uses [Go modules](https://github.com/golang/go/wiki/Modules) which are supported natively on Render.

## Deployment

1. Fork [render-examples/beego-WebIM](https://github.com/render-examples/beego-WebIM) on GitHub.

2. Create a new *Web Service* on Render, and give Render permission to access your new repo.

3. Set the service's *Language* field to `Go` and use the following values during creation:

   ###### *Build Command*: `go build -o app`

   ###### *Start Command*: `./app`

   This will start the `app` executable compiled during build.

That's it! Your Go, Beego, and Gorilla powered IM server will be available on your `onrender.com` URL as soon as the build finishes.