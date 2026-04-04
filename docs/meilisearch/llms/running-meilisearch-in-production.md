# Running Meilisearch in production
Source: https://www.meilisearch.com/docs/guides/running_production

Deploy Meilisearch in a Digital Ocean droplet. Covers installation,  server configuration, and securing your instance.

This tutorial will guide you through setting up a production-ready Meilisearch instance. These instructions use a DigitalOcean droplet running Debian, but should be compatible with any hosting service running a Linux distro.

<Note>
  [Meilisearch Cloud](https://www.meilisearch.com/cloud?utm_campaign=oss\&utm_source=docs\&utm_medium=running-production-oss) is the recommended way to run Meilisearch in production environments.
</Note>

## Requirements

* A DigitalOcean droplet running Debian 12
* An SSH key pair to connect to that machine

<Tip>
  DigitalOcean has extensive documentation on [how to use SSH to connect to a droplet](https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/).
</Tip>

## Step 1: Install Meilisearch

Log into your server via SSH, update the list of available packages, and install `curl`:

```sh theme={null}
apt update
apt install curl -y
```

Using the latest version of a package is good security practice, especially in production environments.

Next, use `curl` to download and run the Meilisearch command-line installer:

```sh theme={null}