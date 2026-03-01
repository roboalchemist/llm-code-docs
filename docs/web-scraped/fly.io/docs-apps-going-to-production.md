# Source: https://fly.io/docs/apps/going-to-production/

Title: Going to production checklist

URL Source: https://fly.io/docs/apps/going-to-production/

Markdown Content:
Going to production checklist · Fly Docs
===============

[Skip to content](https://fly.io/docs/apps/going-to-production/#main-content-start)

[](https://fly.io/)[](https://fly.io/docs/)

[**Need a Logo?** View Our Brand Assets](https://fly.io/docs/about/brand/)

Search

Open main menu[](https://fly.io/)[](https://fly.io/docs/)

[Pricing](https://fly.io/pricing/)[Support](https://fly.io/docs/about/support/)

[Sign In](https://fly.io/app/sign-in/)[Sign Up](https://fly.io/app/sign-up/)

[Docs Index](https://fly.io/docs/)[Apps on Fly.io](https://fly.io/docs/apps/)
*   [Fly Apps overview](https://fly.io/docs/apps/overview/)
*   [Get app info](https://fly.io/docs/apps/info/)
*   [Restart an app](https://fly.io/docs/apps/restart/)
*   [Delete an app](https://fly.io/docs/apps/delete/)
*   [Move an app between orgs](https://fly.io/docs/apps/move-app-org/)

[Fly Launch](https://fly.io/docs/launch/)Toggle Fly Launch section
*   [Launch a new app](https://fly.io/docs/launch/create/)
*   [Deploy an app](https://fly.io/docs/launch/deploy/)
*   [Scale Machine CPU and RAM](https://fly.io/docs/launch/scale-machine/)
*   [Scale the number of Machines](https://fly.io/docs/launch/scale-count/)
*   [Autostop/autostart Machines](https://fly.io/docs/launch/autostop-autostart/)
*   [Autoscale based on metrics](https://fly.io/docs/launch/autoscale-by-metric/)
*   [Add volume storage](https://fly.io/docs/launch/volume-storage/)
*   [Use process groups](https://fly.io/docs/launch/processes/)
*   [Deploy with GitHub Actions](https://fly.io/docs/app-guides/continuous-deployment-with-github-actions/)
*   [Deploy monorepo apps](https://fly.io/docs/launch/monorepo/)
*   [Troubleshoot when a host is down](https://fly.io/docs/apps/trouble-host-unavailable/)
*   [App config reference (fly.toml)](https://fly.io/docs/reference/configuration/)

Secrets Toggle Secrets section
*   [Set runtime secrets](https://fly.io/docs/apps/secrets/)
*   [Set build secrets](https://fly.io/docs/apps/build-secrets/)

Production Apps Toggle Production Apps section
*   [Going to production](https://fly.io/docs/apps/going-to-production/)
*   [App availability and resiliency](https://fly.io/docs/apps/app-availability/)
*   [Fine-tune and benchmark apps](https://fly.io/docs/apps/fine-tune-apps/)
*   [App handover guide](https://fly.io/docs/apps/app-handover-guide/)
*   [Concurrency settings](https://fly.io/docs/apps/concurrency/)

--- title: Going to production checklist layout: docs nav: apps redirect_from: - /docs/going-to-production/ - /docs/going-to-production/the-basics/ - /docs/going-to-production/the-basics/production-databases/ - /docs/reference/going-to-production/ --- Use this checklist to help you set up a production environment on Fly.io. <figure class="flex justify-center"><img src="/static/images/outlook.png" alt="Illustration by Annie Ruygt of Frankie the hot air balloon waving to a bird sitting on a hour roof" class="max-w-lg"></figure> ## Overview Moving an app from staging to production can expose unexpected failure modes: security holes, performance and scaling issues, or data loss. This checklist is meant to catch common pitfalls for apps on Fly.io, but it’s not a guarantee of production readiness. Not every item here will apply to your app, and you may have additional requirements that aren't listed. Use this as a foundation and adapt it to your needs. Think of this list as a scaffold, not a silver bullet. <div class="important icon"> **Important:** The checklist is not exhaustive and does not guarantee production-readiness for your app. Apps can have unique requirements for production depending on the framework and type of app. Some items won't be applicable and there may be other considerations not listed here; you'll need to decide which checklist items work for your app. </div> ## Security <%= render ChecklistComponent.new( items: [ { id: "sso", title: "Set up single sign-on for organizations", description: "Enable SSO on your organization to take advantage of Google or GitHub authentication security. Learn more about [Single sign-on for organizations](/docs/security/sso/)." }, { id: "isolation", title: "Isolate staging and production environments", description: "Use organizations to limit access to your production environment. Read this guide: [Staging and production isolation](/docs/blueprints/staging-prod-isolation/)." }, { id: "least-privilege", title: "Enforce least privilege access", description: "Use access tokens to allow only the minimum access level required by team members to your organization, apps, and Machines. Understand [access tokens](https://fly.io/docs/security/tokens/)." }, { id: "secrets", title: "Protect sensitive information", description: "Set secrets to store sensitive data and make them available as environment variables to your app. Read about [Secrets and Fly Apps](/docs/apps/secrets/)." }, { id: "exposure", title: "Make sure private services are not exposed", description: "Check that your private apps with services don't have public IP addresses. Run `fly ips list` and use `fly ips release` to release unnecessary public IPs. More detail is available in this `flyctl` reference: [`fly ips` commands](/docs/flyctl/ips/). Assign private apps a [Flycast address](https://fly.io/docs/networking/flycast/) instead." }, { id: "arcjet", title: "Use Arcjet application security for JavaScript apps", description: "Secure your app with rate limiting, bot protection, email validation, and defense against common attacks through our extension partner Arcjet. Read more about [Application Security by Arcjet](/docs/security/arcjet/)." } ], c: params[:c] || "", o: params[:o] || "", h: params[:h] || "" ) %> ## Databases <%= render ChecklistComponent.new( items: [ { id: "production-grade-postgres", title: "Use Managed Postgres", description: "We recommend using [Fly.io's Managed Postgres](/docs/mpg/), our fully-managed database service that handles all aspects of running production PostgreSQL."}, { id: "test-backups", title: "Practice your disaster recovery plan", description: "Practice restoring your managed Postgres database from a backup before you actually need to. You can do this anytime from the Managed Postgres dashboard." } ], c: params[:c] || "", o: params[:o] || "", h: params[:h] || "" ) %> ## App performance <%= render ChecklistComponent.new( items: [ { id: "machine-sizing", title: "Get Machine sizing right", description: "Most conventional production web apps require [performance CPUs](/docs/machines/cpu-performance/). Also make sure you have enough RAM for your app and/or enable [swapping to disk](/docs/reference/configuration/#swap_size_mb-option) to deal with brief spikes in memory use. Find out more details in our [Machine sizing guide](/docs/machines/guides-examples/machine-sizing/)."}, { id: "fine-tune-app", title: "Fine-tune your app", description: "Learn about optimizing your app on Fly.io. Read these tips to [fine-tune your app on Fly.io](/docs/apps/fine-tune-apps/)."} ], c: params[:c] || "", o: params[:o] || "", h: params[:h] || "" ) %> ## Availability, resiliency, and costs <%= render ChecklistComponent.new( items: [ { id: "multiple-machines", title: "Use multiple Machines for resiliency", description: "Make your app resilient to single-host failures with multiple Machines that stay stopped until you need them. Learn more in our guide: [Resilient apps use multiple Machines](/docs/blueprints/resilient-apps-multiple-machines/)."}, { id: "add-regions", title: "Scale your app into more regions", description: "Scale your app in multiple regions closest to your app's users. Find out how to [Scale an app's regions](/docs/launch/scale-count/#scale-an-apps-regions)."}, { id: "autostop-autostart", title: "Use autostop/autostart to reduce costs", description: "Autostop/autostart lets you stop or suspend Machines when there's low traffic, saving on resource usage and costs. You get autostop/autostart by default with a new app, but you can configure it to optimize for your use case. Find out more: [Autostop/autostart Machines](/docs/launch/autostop-autostart/)."}, { id: "autoscale-by-metric", title: "Set up autoscaling by metric to reduce costs", description: "For apps that aren't running web services, use the autoscaler app to scale your app's Machines based on any metric, saving on resource usage and costs. Learn how to [Autoscale based on metrics](/docs/launch/autoscale-by-metric/)."} ], c: params[:c] || "", o: params[:o] || "", h: params[:h] || "" ) %> ## Networking <%= render ChecklistComponent.new( items: [ { id: "custom-domain", title: "Set up a custom domain", description: "Configure a certificate for your domain. Learn how to [use a custom domain](/docs/networking/custom-domain/)."}, { id: "ipv4", title: "Consider using a dedicated IPv4 address", description: "Completely eliminate the chance of blacklisted spammers causing problems for your app. There is a small [added cost](/docs/about/pricing/#anycast-ip-addresses) for dedicated IPv4 addresses. Read more about [Dedicated IPv4](/docs/networking/services/#dedicated-ipv4)."}, { id: "flycast", title: "Set up Flycast for private apps", description: "If you haven't already done so, give your private apps a Flycast address to communicate with them entirely on your private network. Find out about [Flycast - Private Fly Proxy services](https://fly.io/docs/networking/flycast/)."} ], c: params[:c] || "", o: params[:o] || "", h: params[:h] || "" ) %> ## Monitoring <%= render ChecklistComponent.new( items: [ { id: "metrics", title: "Monitor your app with fully-managed metrics", description: "Use managed Prometheus and managed Grafana dashboards to monitor your app. Read about [Metrics on Fly.io](/docs/monitoring/metrics/)."}, { id: "sentry", title: "Use Sentry for Error tracking", description: "Our extension partner Sentry provides an application monitoring platform that helps you identify and fix software problems before they impact your users. Fly.io organizations get a year's worth of [Sentry Team Plan](https://fly.io/docs/monitoring/sentry/#sentry-plan-details) credits. Read how to configure [Application Monitoring by Sentry](/docs/monitoring/sentry/)."}, { id: "export-logs", title: "Export your logs", description: "Set up the Fly Log Shipper to aggregate your app’s logs to a service of your choice. Read more about [Exporting logs](/docs/monitoring/exporting-logs/)."} ], c: params[:c] || "", o: params[:o] || "", h: params[:h] || "" ) %> ## CI/CD <%= render ChecklistComponent.new( items: [ { id: "review-apps", title: "Generate review apps with GitHub Actions", description: "Automatically generate ephemeral review apps on Fly.io for each pull request (PR) using GitHub Actions. Learn more about [Git Branch Preview Environments on GitHub](/docs/blueprints/review-apps-guide/)."}, { id: "deploy-with-github-actions", title: "Deploy with GitHub Actions", description: "Set up your app for continuous deployment to Fly.io from the app’s GitHub repository. Find out how to use [Continuous Deployment with Fly.io and GitHub Actions](/docs/app-guides/continuous-deployment-with-github-actions/)."} ], c: params[:c] || "", o: params[:o] || "", h: params[:h] || "" ) %> ## Get support <%= render ChecklistComponent.new( items: [ { id: "community", title: "Get answers in our community forum", description: "Check out our [community forum](https://community.fly.io/) to talk about your project and get help."}, { id: "email-support", title: "Consider a purchasing a support plan", description: "Standard, Premium, or Enterprise support packages are available to purchase. Learn more about [Support plans](https://fly.io/support)."} ], c: params[:c] || "", o: params[:o] || "", h: params[:h] || "" ) %>

[Docs](https://fly.io/docs/)[Apps on Fly.io](https://fly.io/docs/apps)Going to production checklist
Going to production checklist
=============================

Use this checklist to help you set up a production environment on Fly.io.

![Image 2: Illustration by Annie Ruygt of Frankie the hot air balloon waving to a bird sitting on a hour roof](https://fly.io/static/images/outlook.png)
[](https://fly.io/docs/apps/going-to-production/#overview)Overview
------------------------------------------------------------------

Moving an app from staging to production can expose unexpected failure modes: security holes, performance and scaling issues, or data loss. This checklist is meant to catch common pitfalls for apps on Fly.io, but it’s not a guarantee of production readiness. Not every item here will apply to your app, and you may have additional requirements that aren’t listed. Use this as a foundation and adapt it to your needs. Think of this list as a scaffold, not a silver bullet.

**Important:** The checklist is not exhaustive and does not guarantee production-readiness for your app. Apps can have unique requirements for production depending on the framework and type of app. Some items won’t be applicable and there may be other considerations not listed here; you’ll need to decide which checklist items work for your app.

[](https://fly.io/docs/apps/going-to-production/#security)Security
------------------------------------------------------------------

- [x] Set up single sign-on for organizations

Toggle Set up single sign-on for organizations description

Enable SSO on your organization to take advantage of Google or GitHub authentication security. Learn more about [Single sign-on for organizations](https://fly.io/docs/security/sso/).

- [x] Isolate staging and production environments

Toggle Isolate staging and production environments description

Use organizations to limit access to your production environment. Read this guide: [Staging and production isolation](https://fly.io/docs/blueprints/staging-prod-isolation/).

- [x] Enforce least privilege access

Toggle Enforce least privilege access description

Use access tokens to allow only the minimum access level required by team members to your organization, apps, and Machines. Understand [access tokens](https://fly.io/docs/security/tokens/).

- [x] Protect sensitive information

Toggle Protect sensitive information description

Set secrets to store sensitive data and make them available as environment variables to your app. Read about [Secrets and Fly Apps](https://fly.io/docs/apps/secrets/).

- [x] Make sure private services are not exposed

Toggle Make sure private services are not exposed description

Check that your private apps with services don’t have public IP addresses. Run `fly ips list` and use `fly ips release` to release unnecessary public IPs. More detail is available in this `flyctl` reference: [`fly ips` commands](https://fly.io/docs/flyctl/ips/). Assign private apps a [Flycast address](https://fly.io/docs/networking/flycast/) instead.

- [x] Use Arcjet application security for JavaScript apps

Toggle Use Arcjet application security for JavaScript apps description

Secure your app with rate limiting, bot protection, email validation, and defense against common attacks through our extension partner Arcjet. Read more about [Application Security by Arcjet](https://fly.io/docs/security/arcjet/).

[](https://fly.io/docs/apps/going-to-production/#databases)Databases
--------------------------------------------------------------------

- [x] Use Managed Postgres

Toggle Use Managed Postgres description

We recommend using [Fly.io’s Managed Postgres](https://fly.io/docs/mpg/), our fully-managed database service that handles all aspects of running production PostgreSQL.

- [x] Practice your disaster recovery plan

Toggle Practice your disaster recovery plan description

Practice restoring your managed Postgres database from a backup before you actually need to. You can do this anytime from the Managed Postgres dashboard.

[](https://fly.io/docs/apps/going-to-production/#app-performance)App performance
--------------------------------------------------------------------------------

- [x] Get Machine sizing right

Toggle Get Machine sizing right description

Most conventional production web apps require [performance CPUs](https://fly.io/docs/machines/cpu-performance/). Also make sure you have enough RAM for your app and/or enable [swapping to disk](https://fly.io/docs/reference/configuration/#swap_size_mb-option) to deal with brief spikes in memory use. Find out more details in our [Machine sizing guide](https://fly.io/docs/machines/guides-examples/machine-sizing/).

- [x] Fine-tune your app

Toggle Fine-tune your app description

Learn about optimizing your app on Fly.io. Read these tips to [fine-tune your app on Fly.io](https://fly.io/docs/apps/fine-tune-apps/).

[](https://fly.io/docs/apps/going-to-production/#availability-resiliency-and-costs)Availability, resiliency, and costs
----------------------------------------------------------------------------------------------------------------------

- [x] Use multiple Machines for resiliency

Toggle Use multiple Machines for resiliency description

Make your app resilient to single-host failures with multiple Machines that stay stopped until you need them. Learn more in our guide: [Resilient apps use multiple Machines](https://fly.io/docs/blueprints/resilient-apps-multiple-machines/).

- [x] Scale your app into more regions

Toggle Scale your app into more regions description

Scale your app in multiple regions closest to your app’s users. Find out how to [Scale an app’s regions](https://fly.io/docs/launch/scale-count/#scale-an-apps-regions).

- [x] Use autostop/autostart to reduce costs

Toggle Use autostop/autostart to reduce costs description

Autostop/autostart lets you stop or suspend Machines when there’s low traffic, saving on resource usage and costs. You get autostop/autostart by default with a new app, but you can configure it to optimize for your use case. Find out more: [Autostop/autostart Machines](https://fly.io/docs/launch/autostop-autostart/).

- [x] Set up autoscaling by metric to reduce costs

Toggle Set up autoscaling by metric to reduce costs description

For apps that aren’t running web services, use the autoscaler app to scale your app’s Machines based on any metric, saving on resource usage and costs. Learn how to [Autoscale based on metrics](https://fly.io/docs/launch/autoscale-by-metric/).

[](https://fly.io/docs/apps/going-to-production/#networking)Networking
----------------------------------------------------------------------

- [x] Set up a custom domain

Toggle Set up a custom domain description

Configure a certificate for your domain. Learn how to [use a custom domain](https://fly.io/docs/networking/custom-domain/).

- [x] Consider using a dedicated IPv4 address

Toggle Consider using a dedicated IPv4 address description

Completely eliminate the chance of blacklisted spammers causing problems for your app. There is a small [added cost](https://fly.io/docs/about/pricing/#anycast-ip-addresses) for dedicated IPv4 addresses. Read more about [Dedicated IPv4](https://fly.io/docs/networking/services/#dedicated-ipv4).

- [x] Set up Flycast for private apps

Toggle Set up Flycast for private apps description

If you haven’t already done so, give your private apps a Flycast address to communicate with them entirely on your private network. Find out about [Flycast - Private Fly Proxy services](https://fly.io/docs/networking/flycast/).

[](https://fly.io/docs/apps/going-to-production/#monitoring)Monitoring
----------------------------------------------------------------------

- [x] Monitor your app with fully-managed metrics

Toggle Monitor your app with fully-managed metrics description

Use managed Prometheus and managed Grafana dashboards to monitor your app. Read about [Metrics on Fly.io](https://fly.io/docs/monitoring/metrics/).

- [x] Use Sentry for Error tracking

Toggle Use Sentry for Error tracking description

Our extension partner Sentry provides an application monitoring platform that helps you identify and fix software problems before they impact your users. Fly.io organizations get a year’s worth of [Sentry Team Plan](https://fly.io/docs/monitoring/sentry/#sentry-plan-details) credits. Read how to configure [Application Monitoring by Sentry](https://fly.io/docs/monitoring/sentry/).

- [x] Export your logs

Toggle Export your logs description

Set up the Fly Log Shipper to aggregate your app’s logs to a service of your choice. Read more about [Exporting logs](https://fly.io/docs/monitoring/exporting-logs/).

[](https://fly.io/docs/apps/going-to-production/#ci-cd)CI/CD
------------------------------------------------------------

- [x] Generate review apps with GitHub Actions

Toggle Generate review apps with GitHub Actions description

Automatically generate ephemeral review apps on Fly.io for each pull request (PR) using GitHub Actions. Learn more about [Git Branch Preview Environments on GitHub](https://fly.io/docs/blueprints/review-apps-guide/).

- [x] Deploy with GitHub Actions

Toggle Deploy with GitHub Actions description

Set up your app for continuous deployment to Fly.io from the app’s GitHub repository. Find out how to use [Continuous Deployment with Fly.io and GitHub Actions](https://fly.io/docs/app-guides/continuous-deployment-with-github-actions/).

[](https://fly.io/docs/apps/going-to-production/#get-support)Get support
------------------------------------------------------------------------

- [x] Get answers in our community forum

Toggle Get answers in our community forum description

Check out our [community forum](https://community.fly.io/) to talk about your project and get help.

- [x] Consider a purchasing a support plan

Toggle Consider a purchasing a support plan description

Standard, Premium, or Enterprise support packages are available to purchase. Learn more about [Support plans](https://fly.io/support).

Copy page as markdown or[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fapps%2Fgoing-to-production.html.markerb)

[Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Going+to+production+checklist%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fapps%2Fgoing-to-production%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fapps%2Fgoing-to-production.html.markerb%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Going+to+production+checklist%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/apps/going-to-production.html.markerb)

[On this page](https://fly.io/docs/apps/going-to-production/#)
*   [Overview](https://fly.io/docs/apps/going-to-production/#overview)
*   [Security](https://fly.io/docs/apps/going-to-production/#security)
*   [Databases](https://fly.io/docs/apps/going-to-production/#databases)
*   [App performance](https://fly.io/docs/apps/going-to-production/#app-performance)
*   [Availability, resiliency, and costs](https://fly.io/docs/apps/going-to-production/#availability-resiliency-and-costs)
*   [Networking](https://fly.io/docs/apps/going-to-production/#networking)
*   [Monitoring](https://fly.io/docs/apps/going-to-production/#monitoring)
*   [CI/CD](https://fly.io/docs/apps/going-to-production/#ci-cd)
*   [Get support](https://fly.io/docs/apps/going-to-production/#get-support)

Copy page as markdown[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fapps%2Fgoing-to-production.html.markerb)
