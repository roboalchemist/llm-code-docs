# Source: https://help.cloudsmith.io/docs/integrating-with-docker-hub.md

# Docker Hub

Retrieve Container Images from Docker Hub using Cloudsmith

<Image align="center" src="https://files.readme.io/62b0548-cloudsmith-docker-partner-banner.png" />

[Docker Hub](https://hub.docker.com/) is the official registry (provided by [Docker, Inc.](https://www.docker.com/)) that allows you to find and share Docker-format container images.

> It's the world’s largest repository of container images with an array of content sources including container community developers, open source projects, and independent software vendors (ISV) building and distributing their code in containers.

You can retrieve these images through Cloudsmith by enabling an upstream to Docker Hub to proxy and cache images.

## Adding Docker Hub as an Upstream

Here's how you can integrate the Docker Hub Registry into your Cloudsmith account to begin proxying and caching images from Docker Hub:

1. **Add a new Upstream Proxy**\
   In your Cloudsmith repository, go to "Upstreams" and select "Add Upstream Proxy".

<Image align="center" src="https://files.readme.io/a43b766735fe0608006ff0b0a31102dfd479c401a5b9db57e19e67f5b6db3a1b-app.cloudsmith.com_demo_examples-repo_upstreams_1.png" />

2. **Configure the Upstream URL and mode**\
   Provide a descriptive name for the upstream, e.g., Docker Hub, and specify the URL for Docker Hub: [https://index.docker.io](https://index.docker.io).\
   Set the desired priority.\
   Select Cache and Proxy.
3. **Provide authentication credentials**\
   Docker Hub requires authentication. Please select a Method of "Username and Password" and add your Docker Hub account credentials.\
   If you need help creating a Docker Hub account, see [here](https://docs.docker.com/docker-id/).

<Image align="center" src="https://files.readme.io/a168960f3724e369c2591180e70a321ac94e2366f028912ba1c874f9ddb5c2a4-app.cloudsmith.com_demo_examples-repo_upstreams.png" />

**Note:** For Docker Hub, Username & Password are currently required, not optional.

3. **Configure SSL Certificate Verification**\
   Ensure SSL certificates are verified for added security, especially for public sources.

Once configured, your account is now set up to proxy and cache images from Docker Hub through Cloudsmith.