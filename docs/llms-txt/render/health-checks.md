# Source: https://render.com/docs/health-checks.md

# Health Checks — Monitor the availability of your web services.


> Health checks are currently available only for web services.

You can (and should!) define a *health check endpoint* for every web service to help Render determine whether it's ready to receive traffic. Render sends an HTTP request to this endpoint as part of [zero-downtime deploys](/deploys#zero-downtime-deploys), and also every few seconds to verify the health of running services.

Set your health check endpoint path in the [Render Dashboard](https://dashboard.render.com) from your web service's *Settings* page:

[image: Setting health check path in the Render Dashboard]

If you manage your service with a Blueprint, instead set the [`healthCheckPath`](blueprint-spec#healthcheckpath) field in your `render.yaml` file.

## Health check protocol

With every health check, Render sends an HTTP `GET` request to each service instance's health check endpoint. If your service has at least one [custom domain](custom-domains), Render sets one of those domains as the value of the `Host` header for the request. Otherwise, Render uses the service's `onrender.com` subdomain.

- *The check succeeds* if your health check endpoint responds with a `2xx` or `3xx` status code. Render considers the instance healthy.
- *The check fails* in all other cases (including after a 5-second response timeout). Render considers the instance _potentially_ unhealthy.

If a potentially unhealthy instance continues to fail its health checks, Render takes the following actions:

- During a [zero-downtime deploy](/deploys#zero-downtime-deploys):
  - If a new instance fails all of its health checks for 15 consecutive minutes, Render cancels the deploy and continues routing traffic to existing instances.
- For an actively running service:
  - If an instance fails all of its health checks for 15 consecutive seconds, Render stops routing traffic to it to give it an opportunity to recover.
  - After 60 consecutive seconds of failed health checks, Render automatically [restarts the service](/deploys#restarting-a-service).

In the event of a canceled deploy or a service restart, Render [notifies you](notifications) according to your settings.

> *The actions your endpoint should take to verify service health depend on your service's details.*
>
> We recommend performing operation-critical checks, such as executing a simple database query to confirm connectivity.


---

##### Appendix: Glossary definitions

###### web service

Deploy this *service type* to host a dynamic application at a public URL.

Ideal for full-stack web apps and API servers.

Related article: https://render.com/docs/web-services.md