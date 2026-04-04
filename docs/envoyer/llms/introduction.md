# Source: https://docs.envoyer.io/introduction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.envoyer.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction

> Welcome to Envoyer, a zero downtime deployment service for PHP.

<CardGroup cols={2}>
  <Card title="Create An Account" icon="user-plus" href="https://envoyer.io/auth/register">
    Create your Envoyer account today
  </Card>

  <Card title="Watch More" icon="circle-play" href="https://laracasts.com/series/envoyer">
    Watch the free Envoyer series on Laracasts
  </Card>
</CardGroup>

## What Is Envoyer?

[Envoyer](https://envoyer.io) is a zero downtime deployment service for PHP. Some highlights of Envoyer's features include:

* GitHub, GitLab & Bitbucket Integration

* GitLab Self-Hosted Integration

* Seamless Deployment Rollbacks

* Application Health Checks

* Integrated Chat Notifications

* Tuned for Laravel Apps

* Deploy any PHP Project

* Unlimited Deployments

* Deploy to Multiple Servers

* Cron Job Monitoring

* Unlimited Team Members

* Customize Your Deployments

* Import Your [Laravel Forge](https://forge.laravel.com) Servers

#### Requirements

* Envoyer supports Ubuntu and FreeBSD servers.

* The server must have `scp` installed.

## Forge Integration

[Laravel Forge](https://forge.laravel.com) now offers a first-party integration with Envoyer. [Learn more](https://blog.laravel.com/forge-zero-downtime-deployments).

<Frame>
    <img src="https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/forge-envoyer-integration-header.png?fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=dbd13839cb1d1075169a79bfef643bf6" alt="Laravel Forge x Envoyer" data-og-width="4000" width="4000" data-og-height="2250" height="2250" data-path="images/forge-envoyer-integration-header.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/forge-envoyer-integration-header.png?w=280&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=7810704a7d6ade168376cad4439c3451 280w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/forge-envoyer-integration-header.png?w=560&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=5bfef3dc206e168222106dd11a62f31f 560w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/forge-envoyer-integration-header.png?w=840&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=410d4e4682810c8fa0ed92658dcd897c 840w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/forge-envoyer-integration-header.png?w=1100&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=c9766b44d0e6bfcf0ca624e483b8263b 1100w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/forge-envoyer-integration-header.png?w=1650&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=bfcfa5f19762feae02fe670e8a91860b 1650w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/forge-envoyer-integration-header.png?w=2500&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=2211294ca639f38c62b2e8746d4ab469 2500w" />
</Frame>

## Envoyer IP Addresses

If you are restricting SSH access to your server using IP whitelisting, you **must** whitelist the following IP addresses:

* `159.65.47.205`

* `157.245.120.132`

* `134.122.14.47`

* `144.126.248.121`

You may also need to whitelist the [Health Check IP addresses](/projects/management#health-check-ip-addresses).

## Envoyer API

Envoyer provides a powerful API that allows you to manage your servers programmatically, providing access to the vast majority of Envoyer features. You can find the Envoyer API documentation [here](https://envoyer.io/api-documentation).

## Limitations

Envoyer is not necessary for applications running [Laravel Octane](https://github.com/laravel/octane), as Octane already includes zero-downtime deployments out of the box.

## Legal and Compliance

Our [Terms of Service](https://envoyer.io/terms) and [Privacy Policy](https://envoyer.io/privacy) provide details on the terms, conditions, and privacy practices for using Envoyer.
