# Source: https://render.com/docs/deploy-webdis-docker.md

# Deploy Webdis and Redis with Docker

This example helps you deploy [Webdis](https://webd.is) on Render using Docker. Webdis is a fast HTTP interface for Redis with JSON output.

In this example, you'll use a Redis server and a public Webdis server and connect the two.

## Deployment

1. Create a new Redis server using [the Redis deployment guide](key-value) and make a note of the service address which will look like `red-xxxxxxxxxxxxxxxxxxxx:6379`.

2. Fork [render-examples/webdis](https://github.com/render-examples/webdis) on GitHub.

3. Create a new *Web Service* on Render using your webdis fork. Set the service's *Language* field to `Docker` and add the following environment variables:

   | Key          | Value                                                                                                           |
   | ------------ | --------------------------------------------------------------------------------------------------------------- |
   | `REDIS_HOST` | The *host* in your Redis address. For example, `red-xxxxxxxxxxxxxxxxxxxx` in `red-xxxxxxxxxxxxxxxxxxxx:6379`. |
   | `REDIS_PORT` | The *port* in your Redis address. For example, `6379` in `red-xxxxxxxxxxxxxxxxxxxx:6379`.                     |

That's it! Your webdis instance will be live on the Render URL displayed in the dashboard as soon as the build finishes. Try a few HTTP requests against your webdis instance.

Assuming the URL is `https://webdis-wxyz.onrender.com`, run the following commands in your local terminal:

```bash
curl https://webdis-wxyz.onrender.com/SET/hello/world
curl https://webdis-wxyz.onrender.com/GET/hello
curl https://webdis-wxyz.onrender.com/LPUSH/mylist/hello/world
curl https://webdis-wxyz.onrender.com/LLEN/mylist
```