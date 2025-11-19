# Source: https://www.aptible.com/docs/how-to-guides/app-guides/getting-started-with-docker.md

# Getting Started with Docker

On Aptible, we offer two application deployment strategies - [Dockerfile Deploy](/how-to-guides/app-guides/deploy-from-git) and [Direct Docker Image Deploy](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy). You’ll notice that both options involve Docker, a popular container runtime platform. Aptible uses Docker to help deploy your applications in containers, allowing you to easily scale, manage, and deploy applications in isolation. In this guide, we’ll review the basics of using Docker to deploy on Aptible. 

## Writing a Dockerfile

For both deployment options offered on Aptible, you’ll need to know how to write a Dockerfile. A Dockerfile contains all the instructions to describe how a Docker Image should be built. Docker has a great guide on [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/), which we recommend checking out before starting. You can also use the Dockerfiles included in our [Starter Templates](/getting-started/deploy-starter-template/overview) as a reference to kickstart your own. Below is an example taken from our [Ruby on Rails Starter Template](/getting-started/deploy-starter-template/ruby-on-rails):

```ruby  theme={null}
# syntax = docker / dockerfile: 1

#[1] Choose a parent image to base your image on
FROM ruby: latest

#[2] Do things that are necessary for your Application to run
RUN apt - get update \
 && apt - get - y install build - essential libpq - dev \
 && rm - rf /var/lib/apt / lists/*

ADD Gemfile /app/
ADD Gemfile.lock /app/
WORKDIR /app
RUN bundle install

ADD . /app

EXPOSE 3000

# [3] Configure the default process to run when running the container
CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0", "-p", "3000"]
```

You can typically break down a basic Dockerfile into three main sections - we’ve marked them as \[1], \[2], and \[3] in the example. 

1. Choose a parent image:

   * This is the starting point for most users. A parent image provides a foundation for your own image - every subsequent line in your Dockerfile modifies the parent image. 

   * You can find parent images to use from container registries like [Docker Hub](https://hub.docker.com/search?q=\&type=image). 
2. Build your image

   * The instructions in this section help build your image. In the example, we use `RUN`, which executes and commits a command before moving on to the next instruction, `ADD`, which adds a file or directory from your source to a destination, `WORKDIR`, which changes the working directory for subsequent instructions, and `EXPOSE`, which instructs the container to listen on the specified port at runtime. 

   * You can find detailed information for each instruction on Docker’s Dockerfile reference page.
3. Configure the default container process

   * The CMD instruction provides defaults for running a container. 

   * We’ve included the executable command bundle in the example, but you don’t necessarily need to. If you don’t include an executable command, you must provide an `ENTRYPOINT` instead.

> 📘 On Aptible, you can optionally include a [Procfile](/how-to-guides/app-guides/define-services) in the root directory to define explicit services. How we interpret the commands in your Procfile depends on whether or not you have an ENTRYPOINT defined.

## Building a Docker Image

A Docker image is the packaged version of your application - it contains the instructions necessary to build a container on the Docker platform. Once you have a Dockerfile, you can have Aptible build and deploy your image via [Dockerfile Deploy](/how-to-guides/app-guides/deploy-from-git) or build it yourself and provide us the Docker Image via [Direct Docker Image Deploy](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy). 

The steps below, which require the [Aptible CLI](/reference/aptible-cli/cli-commands/overview) and [Docker CLI](https://docs.docker.com/get-docker/), provide a general outline on building and deploying a Docker image to Aptible. 

1. docker build with your Dockerfile and context to build your image.

2. docker push to push your image to a container registry, like Docker Hub. 

3. `aptible deploy --docker-image “$DOCKER_IMAGE” --app “$APP”` to deploy your image to an App on Aptible
