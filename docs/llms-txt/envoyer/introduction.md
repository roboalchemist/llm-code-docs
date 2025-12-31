# Source: https://docs.envoyer.io/introduction.md

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
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/envoyer/images/forge-envoyer-integration-header.png" alt="Laravel Forge x Envoyer" />
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
