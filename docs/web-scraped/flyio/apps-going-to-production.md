# Source: https://fly.io/docs/apps/going-to-production/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# Going to production checklist 

Use this checklist to help you set up a production environment on Fly.io.

<figure class="flex justify-center">
<img src="/static/images/outlook.png" class="max-w-lg" alt="Illustration by Annie Ruygt of Frankie the hot air balloon waving to a bird sitting on a hour roof" />
</figure>

## [](#overview)[Overview] 

Moving an app from staging to production can expose unexpected failure modes: security holes, performance and scaling issues, or data loss. This checklist is meant to catch common pitfalls for apps on Fly.io, but itâ€™s not a guarantee of production readiness. Not every item here will apply to your app, and you may have additional requirements that aren't listed. Use this as a foundation and adapt it to your needs. Think of this list as a scaffold, not a silver bullet.

**Important:** The checklist is not exhaustive and does not guarantee production-readiness for your app. Apps can have unique requirements for production depending on the framework and type of app. Some items wonâ€™t be applicable and there may be other considerations not listed here; youâ€™ll need to decide which checklist items work for your app.

## [](#security)[Security] 

[Set up single sign-on for organizations]

[Toggle Set up single sign-on for organizations description]

Enable SSO on your organization to take advantage of Google or GitHub authentication security. Learn more about [Single sign-on for organizations](/docs/security/sso/).

[Isolate staging and production environments]

[Toggle Isolate staging and production environments description]

Use organizations to limit access to your production environment. Read this guide: [Staging and production isolation](/docs/blueprints/staging-prod-isolation/).

[Enforce least privilege access]

[Toggle Enforce least privilege access description]

Use access tokens to allow only the minimum access level required by team members to your organization, apps, and Machines. Understand [access tokens](https://fly.io/docs/security/tokens/).

[Protect sensitive information]

[Toggle Protect sensitive information description]

Set secrets to store sensitive data and make them available as environment variables to your app. Read about [Secrets and Fly Apps](/docs/apps/secrets/).

[Make sure private services are not exposed]

[Toggle Make sure private services are not exposed description]

Check that your private apps with services don't have public IP addresses. Run `fly ips list` and use `fly ips release` to release unnecessary public IPs. More detail is available in this `flyctl` reference: [`fly ips` commands](/docs/flyctl/ips/). Assign private apps a [Flycast address](https://fly.io/docs/networking/flycast/) instead.

[Use Arcjet application security for JavaScript apps]

[Toggle Use Arcjet application security for JavaScript apps description]

Secure your app with rate limiting, bot protection, email validation, and defense against common attacks through our extension partner Arcjet. Read more about [Application Security by Arcjet](/docs/security/arcjet/).

## [](#databases)[Databases] 

[Use Managed Postgres]

[Toggle Use Managed Postgres description]

We recommend using [Fly.io's Managed Postgres](/docs/mpg/), our fully-managed database service that handles all aspects of running production PostgreSQL.

[Practice your disaster recovery plan]

[Toggle Practice your disaster recovery plan description]

Practice restoring your managed Postgres database from a backup before you actually need to. You can do this anytime from the Managed Postgres dashboard.

## [](#app-performance)[App performance] 

[Get Machine sizing right]

[Toggle Get Machine sizing right description]

Most conventional production web apps require [performance CPUs](/docs/machines/cpu-performance/). Also make sure you have enough RAM for your app and/or enable [swapping to disk](/docs/reference/configuration/#swap_size_mb-option) to deal with brief spikes in memory use. Find out more details in our [Machine sizing guide](/docs/machines/guides-examples/machine-sizing/).

[Fine-tune your app]

[Toggle Fine-tune your app description]

Learn about optimizing your app on Fly.io. Read these tips to [fine-tune your app on Fly.io](/docs/apps/fine-tune-apps/).

## [](#availability-resiliency-and-costs)[Availability, resiliency, and costs] 

[Use multiple Machines for resiliency]

[Toggle Use multiple Machines for resiliency description]

Make your app resilient to single-host failures with multiple Machines that stay stopped until you need them. Learn more in our guide: [Resilient apps use multiple Machines](/docs/blueprints/resilient-apps-multiple-machines/).

[Scale your app into more regions]

[Toggle Scale your app into more regions description]

Scale your app in multiple regions closest to your app's users. Find out how to [Scale an app's regions](/docs/launch/scale-count/#scale-an-apps-regions).

[Use autostop/autostart to reduce costs]

[Toggle Use autostop/autostart to reduce costs description]

Autostop/autostart lets you stop or suspend Machines when there's low traffic, saving on resource usage and costs. You get autostop/autostart by default with a new app, but you can configure it to optimize for your use case. Find out more: [Autostop/autostart Machines](/docs/launch/autostop-autostart/).

[Set up autoscaling by metric to reduce costs]

[Toggle Set up autoscaling by metric to reduce costs description]

For apps that aren't running web services, use the autoscaler app to scale your app's Machines based on any metric, saving on resource usage and costs. Learn how to [Autoscale based on metrics](/docs/launch/autoscale-by-metric/).

## [](#networking)[Networking] 

[Set up a custom domain]

[Toggle Set up a custom domain description]

Configure a certificate for your domain. Learn how to [use a custom domain](/docs/networking/custom-domain/).

[Consider using a dedicated IPv4 address]

[Toggle Consider using a dedicated IPv4 address description]

Completely eliminate the chance of blacklisted spammers causing problems for your app. There is a small [added cost](/docs/about/pricing/#anycast-ip-addresses) for dedicated IPv4 addresses. Read more about [Dedicated IPv4](/docs/networking/services/#dedicated-ipv4).

[Set up Flycast for private apps]

[Toggle Set up Flycast for private apps description]

If you haven't already done so, give your private apps a Flycast address to communicate with them entirely on your private network. Find out about [Flycast - Private Fly Proxy services](https://fly.io/docs/networking/flycast/).

## [](#monitoring)[Monitoring] 

[Monitor your app with fully-managed metrics]

[Toggle Monitor your app with fully-managed metrics description]

Use managed Prometheus and managed Grafana dashboards to monitor your app. Read about [Metrics on Fly.io](/docs/monitoring/metrics/).

[Use Sentry for Error tracking]

[Toggle Use Sentry for Error tracking description]

Our extension partner Sentry provides an application monitoring platform that helps you identify and fix software problems before they impact your users. Fly.io organizations get a year's worth of [Sentry Team Plan](https://fly.io/docs/monitoring/sentry/#sentry-plan-details) credits. Read how to configure [Application Monitoring by Sentry](/docs/monitoring/sentry/).

[Export your logs]

[Toggle Export your logs description]

Set up the Fly Log Shipper to aggregate your appâ€™s logs to a service of your choice. Read more about [Exporting logs](/docs/monitoring/exporting-logs/).

## [](#ci-cd)[CI/CD] 

[Generate review apps with GitHub Actions]

[Toggle Generate review apps with GitHub Actions description]

Automatically generate ephemeral review apps on Fly.io for each pull request (PR) using GitHub Actions. Learn more about [Git Branch Preview Environments on GitHub](/docs/blueprints/review-apps-guide/).

[Deploy with GitHub Actions]

[Toggle Deploy with GitHub Actions description]

Set up your app for continuous deployment to Fly.io from the appâ€™s GitHub repository. Find out how to use [Continuous Deployment with Fly.io and GitHub Actions](/docs/app-guides/continuous-deployment-with-github-actions/).

## [](#get-support)[Get support] 

[Get answers in our community forum]

[Toggle Get answers in our community forum description]

Check out our [community forum](https://community.fly.io/) to talk about your project and get help.

[Consider a purchasing a support plan]

[Toggle Consider a purchasing a support plan description]

Standard, Premium, or Enterprise support packages are available to purchase. Learn more about [Support plans](https://fly.io/support).

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSIgc3R5bGU9IndpZHRoOiAxNnB4OyBoZWlnaHQ6IDE2cHg7IHBvaW50ZXItZXZlbnRzOiBub25lOyIgdmlld2JveD0iMCAwIDIwOCAxMjgiIGZpbGw9ImN1cnJlbnRDb2xvciI+CiAgPHJlY3Qgd2lkdGg9IjE5OCIgaGVpZ2h0PSIxMTgiIHg9IjUiIHk9IjUiIHJ5PSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMTAiIGZpbGw9Im5vbmUiPjwvcmVjdD4KICA8cGF0aCBkPSJNMzAgOThWMzBoMjBsMjAgMjUgMjAtMjVoMjB2NjhIOTBWNTlMNzAgODQgNTAgNTl2Mzl6bTEyNSAwbC0zMC0zM2gyMFYzMGgyMHYzNWgyMHoiPjwvcGF0aD4KPC9zdmc+) [Copy page as markdown]

[or] [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE2cHg7IGhlaWdodDogMTZweDsiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8cGF0aCBkPSJNMjIuMjgyIDkuODIxYTUuOTg1IDUuOTg1IDAgMCAwLS41MTYtNC45MSA2LjA0NiA2LjA0NiAwIDAgMC02LjUxLTIuOUE2LjA2NSA2LjA2NSAwIDAgMCA0Ljk4MSA0LjE4YTUuOTg1IDUuOTg1IDAgMCAwLTMuOTk4IDIuOSA2LjA0NiA2LjA0NiAwIDAgMCAuNzQzIDcuMDk3IDUuOTggNS45OCAwIDAgMCAuNTEgNC45MTEgNi4wNTEgNi4wNTEgMCAwIDAgNi41MTUgMi45QTUuOTg1IDUuOTg1IDAgMCAwIDEzLjI2IDI0YTYuMDU2IDYuMDU2IDAgMCAwIDUuNzcyLTQuMjA2IDUuOTkgNS45OSAwIDAgMCAzLjk5Ny0yLjkgNi4wNTYgNi4wNTYgMCAwIDAtLjc0Ny03LjA3M3pNMTMuMjYgMjIuNDNhNC40NzYgNC40NzYgMCAwIDEtMi44NzYtMS4wNGwuMTQxLS4wODEgNC43NzktMi43NThhLjc5NS43OTUgMCAwIDAgLjM5Mi0uNjgxdi02LjczN2wyLjAyIDEuMTY4YS4wNzEuMDcxIDAgMCAxIC4wMzguMDUydjUuNTgzYTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0IDQuNDk0ek0zLjYgMTguMzA0YTQuNDcgNC40NyAwIDAgMS0uNTM1LTMuMDE0bC4xNDIuMDg1IDQuNzgzIDIuNzU5YS43NzEuNzcxIDAgMCAwIC43OCAwbDUuODQzLTMuMzY5djIuMzMyYS4wOC4wOCAwIDAgMS0uMDMzLjA2Mkw5Ljc0IDE5Ljk1YTQuNSA0LjUgMCAwIDEtNi4xNC0xLjY0NnpNMi4zNCA3Ljg5NmE0LjQ4NSA0LjQ4NSAwIDAgMSAyLjM2Ni0xLjk3M1YxMS42YS43NjYuNzY2IDAgMCAwIC4zODguNjc2bDUuODE1IDMuMzU1LTIuMDIgMS4xNjhhLjA3Ni4wNzYgMCAwIDEtLjA3MSAwbC00LjgzLTIuNzg2QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQgNy44NzJ6bTE2LjU5NyAzLjg1NWwtNS44MzMtMy4zODdMMTUuMTE5IDcuMmEuMDc2LjA3NiAwIDAgMSAuMDcxIDBsNC44MyAyLjc5MWE0LjQ5NCA0LjQ5NCAwIDAgMS0uNjc2IDguMTA1di01LjY3OGEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxLTMuMDIzbC0uMTQxLS4wODUtNC43NzQtMi43ODJhLjc3Ni43NzYgMCAwIDAtLjc4NSAwTDkuNDA5IDkuMjNWNi44OTdhLjA2Ni4wNjYgMCAwIDEgLjAyOC0uMDYxbDQuODMtMi43ODdhNC41IDQuNSAwIDAgMSA2LjY4IDQuNjZ6bS0xMi42NCA0LjEzNWwtMi4wMi0xLjE2NGEuMDguMDggMCAwIDEtLjAzOC0uMDU3VjYuMDc1YTQuNSA0LjUgMCAwIDEgNy4zNzUtMy40NTNsLS4xNDIuMDhMOC43MDQgNS40NmEuNzk1Ljc5NSAwIDAgMC0uMzkzLjY4MXptMS4wOTctMi4zNjVsMi42MDItMS41IDIuNjA3IDEuNXYyLjk5OWwtMi41OTcgMS41LTIuNjA3LTEuNXoiPjwvcGF0aD4KPC9zdmc+) Open in ChatGPT ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1sLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE0cHg7IGhlaWdodDogMTRweDsiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSI+CiAgPHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iY3VycmVudENvbG9yIiBvcGFjaXR5PSIwLjEiPjwvcmVjdD4KICA8cGF0aCBkPSJNNiA1aDV2NU0xMSA1bC01IDUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg+Cjwvc3ZnPg==)](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fapps%2Fgoing-to-production.html.markerb)

[![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIGNsYXNzPSJtci0xLjUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InBvaW50ZXItZXZlbnRzOiBub25lOyB3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+CiAgICA8cGF0aCBkPSJNMTEuOTk5IDEuMjcxQzUuOTI1IDEuMjcxIDEgNi4xOTYgMSAxMi4yNzNjMCA0Ljg1OSAzLjE1MiA4Ljk4MiA3LjUyMyAxMC40MzcuNTUuMS43NTEtLjIzOS43NTEtLjUzbC0uMDE1LTEuODcyYy0zLjA2LjY2Ni0zLjcwNi0xLjQ3NC0zLjcwNi0xLjQ3NC0uNS0xLjI3MS0xLjIyMS0xLjYwOS0xLjIyMS0xLjYwOS0uOTk5LS42ODMuMDc1LS42NjguMDc1LS42NjggMS4xMDUuMDc3IDEuNjg1IDEuMTMzIDEuNjg1IDEuMTMzLjk4MSAxLjY4MSAyLjU3NSAxLjE5NiAzLjIwMi45MTQuMS0uNzExLjM4NC0xLjE5Ni42OTgtMS40NzEtMi40NDItLjI3Ny01LjAxMS0xLjIyMS01LjAxMS01LjQzNiAwLTEuMjAxLjQyOS0yLjE4MyAxLjEzMy0yLjk1Mi0uMTE0LS4yNzgtLjQ5MS0xLjM5Ny4xMDgtMi45MTEgMCAwIC45MjMtLjI5NiAzLjAyNSAxLjEyN0ExMC41NiAxMC41NiAwIDAgMSAxMiA2LjU5MWMuOTM1LjAwNCAxLjg3Ni4xMjcgMi43NTQuMzcgMi4xLTEuNDIzIDMuMDIyLTEuMTI3IDMuMDIyLTEuMTI3LjYgMS41MTQuMjIzIDIuNjMzLjExIDIuOTExLjcwNS43NjkgMS4xMzEgMS43NTEgMS4xMzEgMi45NTIgMCA0LjIyNS0yLjU3MyA1LjE1NS01LjAyMyA1LjQyNy4zOTUuMzQuNzQ3IDEuMDExLjc0NyAyLjAzOCAwIDEuNDcxLS4wMTQgMi42NTctLjAxNCAzLjAxOCAwIC4yOTMuMTk5LjYzNi43NTYuNTI4QzE5Ljg1MSAyMS4yNTEgMjMgMTcuMTMgMjMgMTIuMjczYzAtNi4wNzctNC45MjYtMTEuMDAyLTExLjAwMS0xMS4wMDJ6Ij48L3BhdGg+CiAgPC9nPgo8L3N2Zz4=) Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Going+to+production+checklist%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fapps%2Fgoing-to-production%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fapps%2Fgoing-to-production.html.markerb%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Going+to+production+checklist%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/apps/going-to-production.html.markerb)