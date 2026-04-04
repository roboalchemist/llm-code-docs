# Source: https://render.com/docs/private-network.md

# Private Network — Communicate securely between services without traversing the public internet.

Your Render services in the same region can communicate over their shared private network, _without_ traversing the public internet:

[image: A diagram of Render services on the same private network]

- Each web service and private service has a unique hostname on the private network.
  - These services can listen for private network traffic on _almost_ any port ([see below](#port-restrictions)) and use any protocol.
  - [Free web services](free#free-web-services) can _send_ private network requests, but they can't _receive_ them.
- Each Render Postgres and Key Value instance has an internal URL specifically for private network connections.
- Background workers and cron jobs can _send_ private network requests, but they can't _receive_ them.

Private network communication is fast, safe, and reliable. It uses stable internal hostnames and IPs that dynamically map to individual instance addresses (which can change between deploys).

[Direct IP-based communication](#direct-ip-communication-advanced) is also supported for advanced use cases.

> *Need a private connection to a non-Render system?*
>
> See [Integrating with AWS PrivateLink](#integrating-with-aws-privatelink).

## Port restrictions

Each service is limited to a maximum of 75 open ports.

The following ports _cannot_ be used for private network communication:

- `10000`
- `18012`
- `18013`
- `19099`

## What's on my private network?

Static sites are _not_ on a private network.

Other Render services are on the same private network if they're deployed in the same region _and_ they belong to the same workspace.

> With a [*Professional* workspace](professional-features) or higher, you can [block private network traffic](projects#blocking-cross-environment-traffic) from entering or leaving a particular environment.

## How to connect

These service types each have an internal address or URL:

- Web services
- Private services
- Render Postgres databases
- Render Key Value instances

This value is available from each service's *Connect* menu in the [Render Dashboard](https://dashboard.render.com) (see the *Internal* tab):

[image: Viewing service internal address]

Private services also display this value as their *Service Address*:

[image: The service address for a private service in the Render Dashboard]

The private service above has the internal address `elasticsearch-2j3e:9200`. Other services _on the private network_ can communicate with it at this address.

> *You might need to specify a service's expected protocol in its internal address string when you connect.*
>
> For example, you might need to specify `http://elastic-qeqj:10000` instead of just `elastic-qeqj:10000`.

Background workers and cron jobs _don't_ have an internal address, so they can't receive inbound private network traffic. However, they can _send_ requests to other service types on their private network.

## Integrating with AWS PrivateLink

With a *Professional* workspace or higher, you can create secure, low-latency connections from your private network to compatible non-Render systems hosted on AWS:

[image: A diagram of a PrivateLink connection between a Render private network and MongoDB Atlas]

Use a private link to connect to Snowflake, MongoDB Atlas, or resources in your own AWS VPC.

For details, see [Private Link Connections](private-link).

## Direct IP communication (advanced)

> *Use this method _only_ if [*hostname-based communication*](#how-to-connect) does not serve your use case.*

For advanced use cases, you can send private network requests directly to the IP of a specific service instance. This is most commonly useful for [scaled](scaling) services in the following cases:

- You need to message each running instance of your service individually (such as to pull metrics with a monitoring tool like Prometheus).
- You want to implement custom load balancing logic for your service, instead of relying on Render's built-in load balancing.

Each web service and private service has an associated *discovery hostname* that resolves to _all_ of its active instance IPs. By convention, this hostname has the format `[INTERNAL_HOSTNAME]-discovery` (e.g., `myapp-ne5j-discovery`). To find your service's internal hostname, see [How to connect](#how-to-connect).

Each service exposes its discovery hostname to its own environment via the `RENDER_DISCOVERY_SERVICE` environment variable. If you manage your services via [Blueprints](infrastructure-as-code), you can also access _another_ service's discovery hostname (see [Referencing values from other services](blueprint-spec#referencing-values-from-other-services)).

### Example: Obtaining instance IPs

The snippet below shows a JavaScript function that fetches all of a service's instance IP addresses via DNS lookup and prints them to the console. For other languages, use a supported DNS lookup library.

> *Use a lookup API that relies on the underlying system's DNS resolver.*
>
> This ensures that your lookup applies necessary DNS configuration (such as rules defined in `/etc/resolv.conf`).

```js
const dns = require('dns')

// Obtain discovery hostname from environment variable
const discoveryHostname = process.env.RENDER_DISCOVERY_SERVICE

function fetchAndPrintIPs() {
  // Perform DNS lookup
  // all: true returns all IP addresses for the given hostname
  // family: 4 returns IPv4 addresses
  dns.lookup(discoveryHostname, { all: true, family: 4 }, (err, addresses) => {
    if (err) {
      console.error('Error resolving DNS:', err)
      return
    }
    // Map over results to extract just the IP addresses
    const ips = addresses.map((a) => a.address)
    console.log(`IP addresses for ${discoveryHostname}: ${ips.join(', ')}`)
  })
}
```

---

##### Appendix: Glossary definitions

###### web service

Deploy this *service type* to host a dynamic application at a public URL.

Ideal for full-stack web apps and API servers.

Related article: https://render.com/docs/web-services.md

###### private service

Deploy this *service type* to host a dynamic application that is not internet-reachable.

Ideal for internal apps that only your other Render services can access.

Related article: https://render.com/docs/private-services.md

###### Render Postgres

Fully managed PostgreSQL databases that support point-in-time recovery, read replicas, high availability, and more.

Related article: https://render.com/docs/postgresql.md

###### Render Key Value

Fully managed, Redis®-compatible storage ideal for use as a job queue or shared cache.

Related article: https://render.com/docs/key-value.md

###### background worker

Deploy this *service type* to continuously run code that does not receive incoming requests.

Ideal for processing jobs from a queue.

Related article: https://render.com/docs/background-workers.md

###### cron job

Deploy this *service type* to execute a command or script on a predefined schedule.

Ideal for intermittent tasks like sending email digests or generating reports.

Related article: https://render.com/docs/cronjobs.md

###### static site

Deploy this *service type* to host a static website (HTML/CSS/JS) over a global CDN at a public URL.

Related article: https://render.com/docs/static-sites.md

###### region

Each Render service runs in one of the following regions: *Oregon*, *Ohio*, *Virginia*, *Frankfurt*, or *Singapore*.

Services in the same region can communicate over their *private network*.

Related article: https://render.com/docs/regions.md

###### instance

A virtual machine that runs your service's code on Render.

You can select from a range of *instance types* with different compute specs.