# Source: https://fly.io/docs/about/healthcare/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# Healthcare apps on Fly 

![Illustration by Annie Ruygt of Frankie the hot air balloon examining a green box with A written on it](/static/images/healthcare.png)

Fly.io is a great place to develop and host healthcare applications! You can get started for free and be up and running with a fully secure solution in minutes.

We recognize that healthcare apps and data are different beasts and we're here to protect your patients' data (and keep your auditors happy). We're SOC2 (Type 2) audited, we'll sign BAAs, and we're available to answer questions you might have about how our platform meets your compliance needs [(just ask!)](mailto:sales@fly.io).

Nailing the security for a HIPAA-compliant application can be a big task, and no hosting provider can do it all for you. But Fly.io has a security-first design and a number of features that make HIPAA simpler:

## [](#access-control)[Access Control] 

### [](#database-endpoint-security)[Database Endpoint Security] 

Whether youâ€™re running Fly.io Postgres or your own database, thereâ€™s no network ACLs required to ensure that only your application can talk to the database server; databases on Fly.io talk to app servers over 6PN and WireGuard, and never to the public Internet.

### [](#anti-spoofing-controls)[Anti-Spoofing Controls] 

Attackers that boot up evil Fly.io apps canâ€™t spoof packets to other Fly.io instances; we use both Linux kernel controls, IP routing, and eBPF programs to make sure of that. Itâ€™s kind of a 1998 sort of attack to worry about, but in case your auditor cares, we took care of it.

## [](#audit)[Audit] 

### [](#centralizing-logging-and-metrics)[Centralizing Logging and Metrics] 

Fly.io collects logs and metrics from your apps, and can send them wherever you need them to go; you can get a single feed of logs from all your instances into an ELK cluster or a Splunk instance, or aim Grafana at our metrics, so you have visibility and an audit trail of whatâ€™s going on with your app.

## [](#integrity)[Integrity] 

### [](#hardened-hosting)[Hardened Hosting] 

Apps running on Fly.io run inside Firecracker, a Rust-based, memory-safe KVM hypervisor designed at Amazon as the engine for Fargate. At Fly.io, we take container images from our users and transmogrify them into VMs, for full, no-shared-kernel isolation between applications. Firecracker VMs run as userland processes on our hosts, and are further locked down with modern Linux security tools, including cgroups, file and network namespaces, resource limits, and privilege separation.

### [](#kernel-vulnerability-response)[Kernel Vulnerability Response] 

Fly.io is responsible for the security both of our host kernels (of course) and of the guest kernels our apps run in; one less thing for you worry about.

## [](#authentication)[Authentication] 

### [](#multi-factor-authentication)[Multi-Factor Authentication] 

Fly.io supports standard multifactor authentication apps, because of course we do. We feel a little miffed you had to ask.

### [](#secrets-management)[Secrets Management] 

Itâ€™s easy to expose secrets to your running apps without leaking them in configurations: we provide a â€œwrite-onlyâ€? secrets management scheme that keeps app secrets encrypted, exposing them only to running instances of your app, using a token-based system that ensures your plaintext secrets never hit machines not running your apps.

## [](#confidentiality)[Confidentiality] 

### [](#wireguard-everywhere)[WireGuard Everywhere] 

The Fly.io platform is knitted together out of hosts connected via a WireGuard mesh. Everything talks to everything else over WireGuard. WireGuard is a next-generation in-kernel (and userland) VPN designed by vulnerability researchers for simplicity, auditability, and modern cryptography. The Linux kernel implementation of WireGuard runs in steady state without requiring dynamic memory allocation! WireGuard is great, and is the gold standard for secure network transports. We run a full mesh of WireGuard. That means that once a request arrives at our edge from the Internet, when we proxy it to a host running your app, that communication occurs over a WireGuard virtual network.

We also use WireGuard in our API. Need to SSH to an instance of your app? Thatâ€™ll happen over WireGuard. Need to open a Postgres shell? WireGuard. Deploy a new instance using a remote builder running in Fly.io? You guessed it: the Docker protocol stuff is running over WireGuard, from your machine to our hosts.

### [](#encryption-in-transit)[Encryption In Transit] 

See above! WireGuard runs 256-bit ChaCha20-Poly1305 with an authenticated Curve25519 key exchange.

### [](#tls-everywhere)[TLS Everywhere] 

Fly.io terminates TLS for our users at our edge. We run a fleet of memory-safe, Rust-based proxies that use the Hyper and Rustls libraries to implement HTTPS, in a tight configuration that scores an A grade from Qualys SSL Labs, without you needing to lift a finger.

You can terminate TLS in your application instead of at our edge, if you really want to. But you wonâ€™t want to.

### [](#automatic-certificate-management-with-letsencrypt)[Automatic Certificate Management with LetsEncrypt] 

Fly.io manages the ACME protocol to securely provision LetsEncrypt TLS certificates, so thatâ€™s another thing youâ€™re just not going to have to think much about.

### [](#http-strict-transport-security-and-https-only)[HTTP Strict Transport Security and HTTPS-Only] 

Itâ€™s easy (a single configuration line) to lock your apps to HTTPS-only, using the HSTS protocol to direct browsers exclusively to the secure endpoint of your application and defeating SSL-stripping attacks.

### [](#default-deny-public-networking)[Default-Deny Public Networking] 

Apps running on Fly.io get routable IPv6 addresses and shared IPv4 addresses. But when your users hit those addresses, theyâ€™re not bouncing directly off your app instances; instead, theyâ€™re routed to our edge, where we use our memory-safe Rust proxy to direct traffic. What that means for you is that nothing on your app is exposed unless you ask us to expose it. No security group rules or network ACLs required! Youâ€™re locked down by default.

### [](#6pn-private-networking)[6PN Private Networking] 

Modern applications are often composed of ensembles of services. Some of those services are fit for talking to random users on the Internet. Others are best kept under wraps. Fly.io makes it easy to deploy complicated applications built out of multiple services: all Fly.io apps live in a private IPv6 network exclusive to your organization. We use eBPF in the Linux kernel to ensure that private networks canâ€™t talk to each other; theyâ€™re completely private, without any extra configuration. We call this feature 6PN (for â€œIPv6 Private Networkâ€?), and it means thereâ€™s zero security lockdown work required to deploy a database, Redis cache, or background job scheduler. Your app server will be able to talk to them right away. Nobody outside your organization will be able to talk to them at all.

### [](#network-segregation)[Network Segregation] 

â€œNetwork Segregationâ€? is the term an enterprise IT administrator at a big bank would describe 6PN. Yup, your networks are segregated.

### [](#secure-network-architecture)[Secure Network Architecture] 

Sure, you could call 6PN that, too. Did we mention there are no security group rules to review? There are no security group rules to review.

### [](#encryption-at-rest)[Encryption At Rest] 

Databases like Fly.io Postgres are built on Fly.io Volumes, our persistent storage feature. It works like a drive plugged in and mounted in your app instance. And those drives are block-level encrypted with AES-XTS. We manage the keys for the drives for you, using a token-based orchestration system that ensures the keys are only accessible from privileged processes on hosts actually running your app. Check off another HITRUST CSF requirement from your list!

## [](#availability)[Availability] 

### [](#high-availability)[High Availability] 

Scaling apps across geographic regions is, like, the whole point of the service? I think itâ€™s the whole point? At any rate: itâ€™s definitely a thing we do.

### [](#ddos-protection)[DDoS Protection] 

Fly.io isnâ€™t a DDoS Protection provider. But our upstreams have sophisticated DDoS tools, including blackhole routing and traffic scrubbing, which get regular workouts.

### [](#rolling-deployments)[Rolling Deployments] 

Confidently deploy your Fly.io apps without worrying that youâ€™re going to break everything: weâ€™ll do rolling deploys, with canaries and health-checks, so a known-good version of your app is always running.

### [](#advanced-app-instance-recovery-space-modulator)[Advanced App Instance Recovery Space Modulator] 

If your app crashes or exits, weâ€™ll relaunch the VM. We have the technology.

### [](#off-site-backups)[Off-Site Backups] 

Anything stored persistently in a Fly.io volume is backed up on a regular schedule.

## [](#more-info)[More info] 

Our blueprint for [Going to production with healthcare apps](/docs/blueprints/going-to-production-with-healthcare-apps/) runs a developer or operations engineer through the process of evaluating Fly.ioâ€™s security for HIPAA healthcare apps, launching a pilot application, signing a BAA, and deploying to production.

You can also check our [community](https://community.fly.io) for answers to your questions.

If you can't find what you're looking for or want to know more, [get in touch](mailto:sales@fly.io).

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSIgc3R5bGU9IndpZHRoOiAxNnB4OyBoZWlnaHQ6IDE2cHg7IHBvaW50ZXItZXZlbnRzOiBub25lOyIgdmlld2JveD0iMCAwIDIwOCAxMjgiIGZpbGw9ImN1cnJlbnRDb2xvciI+CiAgPHJlY3Qgd2lkdGg9IjE5OCIgaGVpZ2h0PSIxMTgiIHg9IjUiIHk9IjUiIHJ5PSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMTAiIGZpbGw9Im5vbmUiPjwvcmVjdD4KICA8cGF0aCBkPSJNMzAgOThWMzBoMjBsMjAgMjUgMjAtMjVoMjB2NjhIOTBWNTlMNzAgODQgNTAgNTl2Mzl6bTEyNSAwbC0zMC0zM2gyMFYzMGgyMHYzNWgyMHoiPjwvcGF0aD4KPC9zdmc+) [Copy page as markdown]

[or] [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE2cHg7IGhlaWdodDogMTZweDsiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8cGF0aCBkPSJNMjIuMjgyIDkuODIxYTUuOTg1IDUuOTg1IDAgMCAwLS41MTYtNC45MSA2LjA0NiA2LjA0NiAwIDAgMC02LjUxLTIuOUE2LjA2NSA2LjA2NSAwIDAgMCA0Ljk4MSA0LjE4YTUuOTg1IDUuOTg1IDAgMCAwLTMuOTk4IDIuOSA2LjA0NiA2LjA0NiAwIDAgMCAuNzQzIDcuMDk3IDUuOTggNS45OCAwIDAgMCAuNTEgNC45MTEgNi4wNTEgNi4wNTEgMCAwIDAgNi41MTUgMi45QTUuOTg1IDUuOTg1IDAgMCAwIDEzLjI2IDI0YTYuMDU2IDYuMDU2IDAgMCAwIDUuNzcyLTQuMjA2IDUuOTkgNS45OSAwIDAgMCAzLjk5Ny0yLjkgNi4wNTYgNi4wNTYgMCAwIDAtLjc0Ny03LjA3M3pNMTMuMjYgMjIuNDNhNC40NzYgNC40NzYgMCAwIDEtMi44NzYtMS4wNGwuMTQxLS4wODEgNC43NzktMi43NThhLjc5NS43OTUgMCAwIDAgLjM5Mi0uNjgxdi02LjczN2wyLjAyIDEuMTY4YS4wNzEuMDcxIDAgMCAxIC4wMzguMDUydjUuNTgzYTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0IDQuNDk0ek0zLjYgMTguMzA0YTQuNDcgNC40NyAwIDAgMS0uNTM1LTMuMDE0bC4xNDIuMDg1IDQuNzgzIDIuNzU5YS43NzEuNzcxIDAgMCAwIC43OCAwbDUuODQzLTMuMzY5djIuMzMyYS4wOC4wOCAwIDAgMS0uMDMzLjA2Mkw5Ljc0IDE5Ljk1YTQuNSA0LjUgMCAwIDEtNi4xNC0xLjY0NnpNMi4zNCA3Ljg5NmE0LjQ4NSA0LjQ4NSAwIDAgMSAyLjM2Ni0xLjk3M1YxMS42YS43NjYuNzY2IDAgMCAwIC4zODguNjc2bDUuODE1IDMuMzU1LTIuMDIgMS4xNjhhLjA3Ni4wNzYgMCAwIDEtLjA3MSAwbC00LjgzLTIuNzg2QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQgNy44NzJ6bTE2LjU5NyAzLjg1NWwtNS44MzMtMy4zODdMMTUuMTE5IDcuMmEuMDc2LjA3NiAwIDAgMSAuMDcxIDBsNC44MyAyLjc5MWE0LjQ5NCA0LjQ5NCAwIDAgMS0uNjc2IDguMTA1di01LjY3OGEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxLTMuMDIzbC0uMTQxLS4wODUtNC43NzQtMi43ODJhLjc3Ni43NzYgMCAwIDAtLjc4NSAwTDkuNDA5IDkuMjNWNi44OTdhLjA2Ni4wNjYgMCAwIDEgLjAyOC0uMDYxbDQuODMtMi43ODdhNC41IDQuNSAwIDAgMSA2LjY4IDQuNjZ6bS0xMi42NCA0LjEzNWwtMi4wMi0xLjE2NGEuMDguMDggMCAwIDEtLjAzOC0uMDU3VjYuMDc1YTQuNSA0LjUgMCAwIDEgNy4zNzUtMy40NTNsLS4xNDIuMDhMOC43MDQgNS40NmEuNzk1Ljc5NSAwIDAgMC0uMzkzLjY4MXptMS4wOTctMi4zNjVsMi42MDItMS41IDIuNjA3IDEuNXYyLjk5OWwtMi41OTcgMS41LTIuNjA3LTEuNXoiPjwvcGF0aD4KPC9zdmc+) Open in ChatGPT ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1sLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE0cHg7IGhlaWdodDogMTRweDsiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSI+CiAgPHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iY3VycmVudENvbG9yIiBvcGFjaXR5PSIwLjEiPjwvcmVjdD4KICA8cGF0aCBkPSJNNiA1aDV2NU0xMSA1bC01IDUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg+Cjwvc3ZnPg==)](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fabout%2Fhealthcare.html.markerb)

[![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIGNsYXNzPSJtci0xLjUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InBvaW50ZXItZXZlbnRzOiBub25lOyB3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+CiAgICA8cGF0aCBkPSJNMTEuOTk5IDEuMjcxQzUuOTI1IDEuMjcxIDEgNi4xOTYgMSAxMi4yNzNjMCA0Ljg1OSAzLjE1MiA4Ljk4MiA3LjUyMyAxMC40MzcuNTUuMS43NTEtLjIzOS43NTEtLjUzbC0uMDE1LTEuODcyYy0zLjA2LjY2Ni0zLjcwNi0xLjQ3NC0zLjcwNi0xLjQ3NC0uNS0xLjI3MS0xLjIyMS0xLjYwOS0xLjIyMS0xLjYwOS0uOTk5LS42ODMuMDc1LS42NjguMDc1LS42NjggMS4xMDUuMDc3IDEuNjg1IDEuMTMzIDEuNjg1IDEuMTMzLjk4MSAxLjY4MSAyLjU3NSAxLjE5NiAzLjIwMi45MTQuMS0uNzExLjM4NC0xLjE5Ni42OTgtMS40NzEtMi40NDItLjI3Ny01LjAxMS0xLjIyMS01LjAxMS01LjQzNiAwLTEuMjAxLjQyOS0yLjE4MyAxLjEzMy0yLjk1Mi0uMTE0LS4yNzgtLjQ5MS0xLjM5Ny4xMDgtMi45MTEgMCAwIC45MjMtLjI5NiAzLjAyNSAxLjEyN0ExMC41NiAxMC41NiAwIDAgMSAxMiA2LjU5MWMuOTM1LjAwNCAxLjg3Ni4xMjcgMi43NTQuMzcgMi4xLTEuNDIzIDMuMDIyLTEuMTI3IDMuMDIyLTEuMTI3LjYgMS41MTQuMjIzIDIuNjMzLjExIDIuOTExLjcwNS43NjkgMS4xMzEgMS43NTEgMS4xMzEgMi45NTIgMCA0LjIyNS0yLjU3MyA1LjE1NS01LjAyMyA1LjQyNy4zOTUuMzQuNzQ3IDEuMDExLjc0NyAyLjAzOCAwIDEuNDcxLS4wMTQgMi42NTctLjAxNCAzLjAxOCAwIC4yOTMuMTk5LjYzNi43NTYuNTI4QzE5Ljg1MSAyMS4yNTEgMjMgMTcuMTMgMjMgMTIuMjczYzAtNi4wNzctNC45MjYtMTEuMDAyLTExLjAwMS0xMS4wMDJ6Ij48L3BhdGg+CiAgPC9nPgo8L3N2Zz4=) Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Healthcare+apps+on+Fly%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fabout%2Fhealthcare%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fabout%2Fhealthcare.html.markerb%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Healthcare+apps+on+Fly%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/about/healthcare.html.markerb)