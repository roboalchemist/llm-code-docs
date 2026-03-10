# Source: https://render.com/docs/private-services.md

# Private Services — Host apps that only accept traffic from your other services.

Render private services are just like web services, with one exception: *private services aren't reachable via the public internet.* They _do not_ receive an `onrender.com` subdomain:

[diagram]

However, private services _are_ reachable by your other Render services on the same private network! This means they're perfect for services that only your own infrastructure needs to talk to.

Private services can listen on _almost_ any port ([see details](private-network#port-restrictions)) and communicate using any protocol.

> *Private services must bind to at least one port.*
>
> If your service won't receive incoming traffic, instead create a background worker. See details [below](#private-service-or-background-worker).

## Examples

Here are some deployment guides for tools that make great private services:

- [Deploy an Elasticsearch server](/deploy-elasticsearch)
- [Deploy Clickhouse](/deploy-clickhouse)

## Private service or background worker?

Like private services, your background workers are unreachable via the public internet. _Unlike_ private services, *background workers aren't even reachable via their private network:*

[diagram]

- If your internal service will bind to _at least one port_ and receive private network traffic, create a private service.
- Otherwise, create a background worker.

Background workers can _initiate_ network requests but can't _receive_ them. They usually perform long-running or resource-intensive tasks, which they fetch from a job queue that's often backed by a Render Key Value instance.

## Connect to your private service

See [Private Network](private-network#how-to-connect).

---

##### Appendix: Glossary definitions

###### web service

Deploy this *service type* to host a dynamic application at a public URL.

Ideal for full-stack web apps and API servers.

Related article: https://render.com/docs/web-services.md

###### private network

Your Render services in the same *region* can reach each other without traversing the public internet, enabling faster and safer communication.

Related article: https://render.com/docs/private-network.md

###### background worker

Deploy this *service type* to continuously run code that does not receive incoming requests.

Ideal for processing jobs from a queue.

Related article: https://render.com/docs/background-workers.md

###### Render Key Value

Fully managed, Redis®-compatible storage ideal for use as a job queue or shared cache.

Related article: https://render.com/docs/key-value.md