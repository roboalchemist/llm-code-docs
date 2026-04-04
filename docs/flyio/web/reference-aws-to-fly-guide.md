# Source: https://fly.io/docs/reference/aws-to-fly-guide/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# Migrating from AWS to Fly.io Overview 

<figure class="flex justify-center">
<img src="/static/images/migrating-from-aws.png" class="w-full max-w-lg mx-auto" alt="Illustration by Annie Ruygt of a figure jumping from one mountain to another" />
</figure>

**Fly.io runs apps close to your users, by giving you fast-starting VMs (â€œFly Machinesâ€?) in regions worldwide.** This guide is for folks moving apps from AWS. It walks through the major architectural differences youâ€™ll hit and how to adjust your deployment model.

Migrating from AWS to Fly.io means rethinking a few assumptions. The two platforms run apps differently, wire networks differently, and give you different tools to scale and persist data. This is a whirlwind tour of what changes when you leave the AWS cloud mothership.

### [](#compute)[Compute] 

First up: compute. Fly.io runs apps as virtual machines, but it doesn't use AMIs or EC2. Instead, you give us a Docker image, we unpack it, and that becomes the root filesystem for a VM we spin up for you. We call these [Fly Machines](/docs/machines/overview/). They're fast. And they're small. And they boot fast because there's no hypervisor cold-start time and no shared kernel games like you'd find in ECS or EKS.

But here's the catch: unless you mount a volume, the root filesystem is ephemeral. It disappears on restart. Any data written there is toast unless you store it somewhere else. If your app currently depends on an EBS volume or even just writes temp files it expects to survive a restart, you'll need to rethink that.

### [](#storage)[Storage] 

[Fly Volumes](/docs/volumes/overview/) are our answer to persistent storage. They're slices of NVMe mounted directly on the physical host. They're not network-attached. This means they're fast and simple, but they're tied to a specific host. If your machine dies, you can boot another and reattach the volume. Think EBS, minus the network indirection and regional abstraction. You can also store large static assets like ML models in volumes, which keeps your Docker images lean and your deploys snappy.

For object storage, we offer [Tigris](/docs/tigris/). It's S3-compatible and runs on Fly.io itself. If you're migrating from AWS S3, there's a handy [shadow bucket](/docs/tigris/#migrating-to-tigris-with-shadow-buckets) mode: Tigris can fall back to fetching from your existing S3 bucket if a file isn't yet copied over. First request pulls from S3; future requests hit local. Writes are synced, too, which makes a gradual migration painless.

### [](#networking)[Networking] 

Talking to AWS-hosted services, like RDS, takes a bit of finessing. There's no direct WireGuard bridge into your AWS VPC. If you want to connect to RDS securely, the simplest approach is to run PgBouncer as a Fly Machine with a static egress IP. Allowlist that IP in your RDS security group. Then your app machines connect to PgBouncer over Fly's private network, and it forwards to RDS.

Speaking of [networks](/docs/networking/): Fly.io apps live on an isolated private network per org, connected over WireGuard. Machines talk to each other via `.internal` hostnames (direct) or `.flycast` (load-balanced via our proxy). This setup is pretty close to private subnets and security groups in AWS. You usually only expose your edge-facing apps to the public internet.

Instead of regional load balancers, we use [Anycast](/docs/networking/services/#anycast-ip-addresses). Your DNS points to one global IP. The Fly Proxy routes requests to the nearest edge server, which forwards traffic to a healthy app instance based on load and latency. That means no more manually balancing between `us-east-1` and `us-west-2`.

### [](#scaling)[Scaling] 

Scaling works differently too. Machines are not created on-demand based on request traffic. You provision them up front, and we start/stop them as needed. That means your max spend is predictable. Want [autoscaling](/docs/reference/autoscaling/)? Monitor metrics via Prometheus, and scale using flyctl or an API client. You own the automation.

### [](#deployments-and-secrets)[Deployments and Secrets] 

Which brings us to Infrastructure-as-code (IaC). Most users glue things together with Bash scripts and `flyctl`, and manage state by convention. It's low-friction but low-abstraction. And itâ€™s still less of a headache than CloudFormation. More infrastructure automation ideas are [available here](/docs/blueprints/infra-automation-without-terraform/).

On the plus side, deployments can be [zero-downtime](/docs/blueprints/seamless-deployments/) if you use [health checks](/docs/reference/health-checks/) and run multiple machines. Define those health checks in `fly.toml`, and the proxy will route around unhealthy nodes. You can even run DB migrations with a `release_command` before a deploy, and roll back by pushing a previous image tag.

Secrets? Use [Fly Secrets](/docs/apps/secrets/). They get mounted as env vars at runtime and stay encrypted at rest. Similar to AWS Secrets Manager or Parameter Store, but simpler. We also have a new Secrets API that works like AWS KMS to allow apps to encrypt/decrypt data with centrally-managed keys.

### [](#databases)[Databases] 

Databases? We offer [Managed Postgres](/docs/mpg/), our fully-managed database service that handles all aspects of running production PostgreSQL databases, similar to RDS. We take care of automatic backups/recovery, high availability with automatic failover, performance monitoring and metrics, resource scaling, 24/7 support, and automatic data encryption.

Other database options include managed Redis from our partner Upstash, running your own Redis or Valkey, distributed SQLite via LiteFS, or vector DBs like LanceDB with Tigris.

### [](#monitoring)[Monitoring] 

For [monitoring](/docs/monitoring/metrics/), you get Prometheus metrics and Grafana dashboards. There's no native alerting yet, but many folks run their own Prometheus with Alertmanager, or use Grafana to set up alerts. This involves more user setup compared to AWS CloudWatch alarms, but you gain a wealth of resources from the Grafana and Prometheus communities.

### [](#in-a-nutshell)[In a nutshell] 

AWS is a sprawling platform with deep abstractions. Fly.io strips a lot of that away. You get rawer access to your infra and better latency for your users, but you might trade some convenience. Migration is generally less about translating concepts and more about rethinking how your app is built and deployed.

### [](#related-reading)[Related Reading] 

-   [Fly Apps](/docs/apps/overview/)
-   [Fly Volumes](/docs/volumes/overview/)
-   [Managed Postgres](/docs/mpg/)
-   [Going to Production Checklist](/docs/apps/going-to-production/)

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSIgc3R5bGU9IndpZHRoOiAxNnB4OyBoZWlnaHQ6IDE2cHg7IHBvaW50ZXItZXZlbnRzOiBub25lOyIgdmlld2JveD0iMCAwIDIwOCAxMjgiIGZpbGw9ImN1cnJlbnRDb2xvciI+CiAgPHJlY3Qgd2lkdGg9IjE5OCIgaGVpZ2h0PSIxMTgiIHg9IjUiIHk9IjUiIHJ5PSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMTAiIGZpbGw9Im5vbmUiPjwvcmVjdD4KICA8cGF0aCBkPSJNMzAgOThWMzBoMjBsMjAgMjUgMjAtMjVoMjB2NjhIOTBWNTlMNzAgODQgNTAgNTl2Mzl6bTEyNSAwbC0zMC0zM2gyMFYzMGgyMHYzNWgyMHoiPjwvcGF0aD4KPC9zdmc+) [Copy page as markdown]

[or] [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE2cHg7IGhlaWdodDogMTZweDsiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8cGF0aCBkPSJNMjIuMjgyIDkuODIxYTUuOTg1IDUuOTg1IDAgMCAwLS41MTYtNC45MSA2LjA0NiA2LjA0NiAwIDAgMC02LjUxLTIuOUE2LjA2NSA2LjA2NSAwIDAgMCA0Ljk4MSA0LjE4YTUuOTg1IDUuOTg1IDAgMCAwLTMuOTk4IDIuOSA2LjA0NiA2LjA0NiAwIDAgMCAuNzQzIDcuMDk3IDUuOTggNS45OCAwIDAgMCAuNTEgNC45MTEgNi4wNTEgNi4wNTEgMCAwIDAgNi41MTUgMi45QTUuOTg1IDUuOTg1IDAgMCAwIDEzLjI2IDI0YTYuMDU2IDYuMDU2IDAgMCAwIDUuNzcyLTQuMjA2IDUuOTkgNS45OSAwIDAgMCAzLjk5Ny0yLjkgNi4wNTYgNi4wNTYgMCAwIDAtLjc0Ny03LjA3M3pNMTMuMjYgMjIuNDNhNC40NzYgNC40NzYgMCAwIDEtMi44NzYtMS4wNGwuMTQxLS4wODEgNC43NzktMi43NThhLjc5NS43OTUgMCAwIDAgLjM5Mi0uNjgxdi02LjczN2wyLjAyIDEuMTY4YS4wNzEuMDcxIDAgMCAxIC4wMzguMDUydjUuNTgzYTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0IDQuNDk0ek0zLjYgMTguMzA0YTQuNDcgNC40NyAwIDAgMS0uNTM1LTMuMDE0bC4xNDIuMDg1IDQuNzgzIDIuNzU5YS43NzEuNzcxIDAgMCAwIC43OCAwbDUuODQzLTMuMzY5djIuMzMyYS4wOC4wOCAwIDAgMS0uMDMzLjA2Mkw5Ljc0IDE5Ljk1YTQuNSA0LjUgMCAwIDEtNi4xNC0xLjY0NnpNMi4zNCA3Ljg5NmE0LjQ4NSA0LjQ4NSAwIDAgMSAyLjM2Ni0xLjk3M1YxMS42YS43NjYuNzY2IDAgMCAwIC4zODguNjc2bDUuODE1IDMuMzU1LTIuMDIgMS4xNjhhLjA3Ni4wNzYgMCAwIDEtLjA3MSAwbC00LjgzLTIuNzg2QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQgNy44NzJ6bTE2LjU5NyAzLjg1NWwtNS44MzMtMy4zODdMMTUuMTE5IDcuMmEuMDc2LjA3NiAwIDAgMSAuMDcxIDBsNC44MyAyLjc5MWE0LjQ5NCA0LjQ5NCAwIDAgMS0uNjc2IDguMTA1di01LjY3OGEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxLTMuMDIzbC0uMTQxLS4wODUtNC43NzQtMi43ODJhLjc3Ni43NzYgMCAwIDAtLjc4NSAwTDkuNDA5IDkuMjNWNi44OTdhLjA2Ni4wNjYgMCAwIDEgLjAyOC0uMDYxbDQuODMtMi43ODdhNC41IDQuNSAwIDAgMSA2LjY4IDQuNjZ6bS0xMi42NCA0LjEzNWwtMi4wMi0xLjE2NGEuMDguMDggMCAwIDEtLjAzOC0uMDU3VjYuMDc1YTQuNSA0LjUgMCAwIDEgNy4zNzUtMy40NTNsLS4xNDIuMDhMOC43MDQgNS40NmEuNzk1Ljc5NSAwIDAgMC0uMzkzLjY4MXptMS4wOTctMi4zNjVsMi42MDItMS41IDIuNjA3IDEuNXYyLjk5OWwtMi41OTcgMS41LTIuNjA3LTEuNXoiPjwvcGF0aD4KPC9zdmc+) Open in ChatGPT ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1sLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE0cHg7IGhlaWdodDogMTRweDsiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSI+CiAgPHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iY3VycmVudENvbG9yIiBvcGFjaXR5PSIwLjEiPjwvcmVjdD4KICA8cGF0aCBkPSJNNiA1aDV2NU0xMSA1bC01IDUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg+Cjwvc3ZnPg==)](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Freference%2Faws-to-fly-guide.html.md)

[![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIGNsYXNzPSJtci0xLjUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InBvaW50ZXItZXZlbnRzOiBub25lOyB3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+CiAgICA8cGF0aCBkPSJNMTEuOTk5IDEuMjcxQzUuOTI1IDEuMjcxIDEgNi4xOTYgMSAxMi4yNzNjMCA0Ljg1OSAzLjE1MiA4Ljk4MiA3LjUyMyAxMC40MzcuNTUuMS43NTEtLjIzOS43NTEtLjUzbC0uMDE1LTEuODcyYy0zLjA2LjY2Ni0zLjcwNi0xLjQ3NC0zLjcwNi0xLjQ3NC0uNS0xLjI3MS0xLjIyMS0xLjYwOS0xLjIyMS0xLjYwOS0uOTk5LS42ODMuMDc1LS42NjguMDc1LS42NjggMS4xMDUuMDc3IDEuNjg1IDEuMTMzIDEuNjg1IDEuMTMzLjk4MSAxLjY4MSAyLjU3NSAxLjE5NiAzLjIwMi45MTQuMS0uNzExLjM4NC0xLjE5Ni42OTgtMS40NzEtMi40NDItLjI3Ny01LjAxMS0xLjIyMS01LjAxMS01LjQzNiAwLTEuMjAxLjQyOS0yLjE4MyAxLjEzMy0yLjk1Mi0uMTE0LS4yNzgtLjQ5MS0xLjM5Ny4xMDgtMi45MTEgMCAwIC45MjMtLjI5NiAzLjAyNSAxLjEyN0ExMC41NiAxMC41NiAwIDAgMSAxMiA2LjU5MWMuOTM1LjAwNCAxLjg3Ni4xMjcgMi43NTQuMzcgMi4xLTEuNDIzIDMuMDIyLTEuMTI3IDMuMDIyLTEuMTI3LjYgMS41MTQuMjIzIDIuNjMzLjExIDIuOTExLjcwNS43NjkgMS4xMzEgMS43NTEgMS4xMzEgMi45NTIgMCA0LjIyNS0yLjU3MyA1LjE1NS01LjAyMyA1LjQyNy4zOTUuMzQuNzQ3IDEuMDExLjc0NyAyLjAzOCAwIDEuNDcxLS4wMTQgMi42NTctLjAxNCAzLjAxOCAwIC4yOTMuMTk5LjYzNi43NTYuNTI4QzE5Ljg1MSAyMS4yNTEgMjMgMTcuMTMgMjMgMTIuMjczYzAtNi4wNzctNC45MjYtMTEuMDAyLTExLjAwMS0xMS4wMDJ6Ij48L3BhdGg+CiAgPC9nPgo8L3N2Zz4=) Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Migrating+from+AWS+to+Fly.io+Overview%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Freference%2Faws-to-fly-guide%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Freference%2Faws-to-fly-guide.html.md%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Migrating+from+AWS+to+Fly.io+Overview%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/reference/aws-to-fly-guide.html.md)