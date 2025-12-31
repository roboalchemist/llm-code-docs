# Source: https://fly.io/docs/flyctl/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# flyctl - The Fly.io CLI 

flyctl, the Fly.io CLI, is one of the primary ways to interact with the Fly.io platform. You'll use the `fly` command to create and deploy apps, manage Machines and volumes, configure networking, and more.

First, [install flyctl](/docs/flyctl/install/).

Also check out [flyctl and continuous integration](/docs/flyctl/integrating/) which covers environment variables, JSON and other automation related information about flyctl.

The following list includes some important commands to get started.

## [](#using-your-fly-io-account)[Using your Fly.io Account] 

-   Signing Up: [fly auth signup](/docs/flyctl/auth-signup/)
-   Logging In: [fly auth login](/docs/flyctl/auth-login/)

## [](#working-with-apps)[Working with Apps] 

-   Create An App: [fly launch](/docs/flyctl/launch/)
-   Deploy An App: [fly deploy](/docs/flyctl/deploy/)
-   Manage Apps: [fly apps](/docs/flyctl/apps/)
-   Manage App Secrets: [fly secrets](/docs/flyctl/secrets/)

## [](#viewing-and-monitoring-an-app)[Viewing and monitoring an App] 

-   Show App Logs: [fly logs](/docs/flyctl/logs/)
-   Show App Deployment Status: [fly status](/docs/flyctl/status/)
-   Show App Releases: [fly releases](/docs/flyctl/releases/)

## [](#configuring-networking-and-certificates)[Configuring networking and certificates] 

-   Assign IP Addresses: [fly ips](/docs/flyctl/ips/)
-   Create Certificates: [fly certs](/docs/flyctl/certs/)