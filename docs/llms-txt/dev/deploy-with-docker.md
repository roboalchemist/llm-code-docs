# Source: https://dev.writer.com/framework/deploy-with-docker.md

# Source: https://dev.writer.com/agent-builder/deploy-with-docker.md

# Source: https://dev.writer.com/framework/deploy-with-docker.md

# Source: https://dev.writer.com/agent-builder/deploy-with-docker.md

# Source: https://dev.writer.com/framework/deploy-with-docker.md

# Source: https://dev.writer.com/agent-builder/deploy-with-docker.md

# Source: https://dev.writer.com/framework/deploy-with-docker.md

# Source: https://dev.writer.com/agent-builder/deploy-with-docker.md

# Deploy with Docker

> Deploy Agent Builder agents with Docker containers. Run agents on cloud platforms, on-premises servers, or local development machines.

This guide shows you how to deploy your Agent Builder agents using [Docker containers](https://www.docker.com/). After completing these steps, you can run your agents in any environment that supports Docker, including cloud platforms, on-premises servers, or local development machines.

<Tip>
  To deploy a local agent to the Writer cloud, see [Sync agents between local and cloud](/agent-builder/sync-agent).
</Tip>

## Prerequisites

Before getting started, ensure you have:

* [A local Agent Builder project](/agent-builder/local-development)
* [Docker installed on your system](https://docs.docker.com/get-docker/)
* [A Writer API key](/api-reference/api-keys)

## Overview

Below are the main steps to deploying your agent with Docker:

1. Create and build a Docker image for your agent
2. Publish the Docker image to a container registry and deploy it to your target environment

## Create a Docker image

A `Dockerfile` contains instructions that tell Docker how to build your agent's container image. The `Dockerfile` must be named `Dockerfile` and placed in your agent's project directory alongside `main.py` and `.wf/`.

### Create the Dockerfile

Create a `Dockerfile` in your agent's project directory with the following content:

```docker  theme={null}
FROM python:3.13-slim

# Install system dependencies
RUN apt-get update -y && \
    apt-get install -y build-essential cmake python3-dev curl && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /app

# Workdir
WORKDIR /app
# Copy only requirements first for better caching, then install
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the project
COPY . /app

# Set up the agent
ENTRYPOINT [ "writer", "run" ]
EXPOSE 8080
CMD [ ".", "--port", "8080", "--host", "0.0.0.0" ]
```

<Note>
  This Dockerfile uses an official Python base image and installs dependencies from the `requirements.txt` file that's automatically generated in your Agent Builder project. If you're familiar with Docker, you can customize this `Dockerfile` for your specific needs. Agent Builder agents are standard Python applications that work with the Writer Framework package.

  The `--port 8080` flag overrides Writer Framework's default port range (3005-3099 for run mode) to use port 8080, which is commonly used for web applications and works well with most cloud platforms.
</Note>

### Build the Docker image

Build your Docker image using the following command:

```bash  theme={null}
docker build . -t my-agent-app
```

Replace `my-agent-app` with a descriptive name for your agent.

<Warning>
  By default, Docker builds images for the architecture it's running on. If you're using an ARM-based computer (like a Mac with M1/M2 chip or Raspberry Pi), Docker builds an ARM image. Most cloud platforms require x86 images. Use [Docker buildx](https://docs.docker.com/build/building/multi-platform/) to build multi-platform images, or build on an x86 machine.
</Warning>

## Run the container

Your agent needs access to your Writer API key to perform actions with the Writer API and Writer LLMs. The Docker image doesn't include your API key for security reasons, so you need to provide it when running the container.

### Set up your environment

Create a `.env` file in your project directory with your API key:

```bash  theme={null}
WRITER_API_KEY=your_api_key_here
```

Then source the environment file in your shell:

```bash  theme={null}
source .env
```

Now you can run your container using either `docker run` or `docker compose`.

### Using `docker run`

```bash  theme={null}
docker run -e WRITER_API_KEY -p 8080:8080 my-agent-app

# Or load environment variables from a file:
docker run --env-file .env -p 8080:8080 my-agent-app
```

### Using `docker compose`

Create a `docker-compose.yml` file for easier management:

```yaml  theme={null}
services:
  agent:
    build: .
    ports:
      - "8080:8080"
    environment:
      - WRITER_API_KEY
    # Or load environment variables from a file
    # env_file:
    #   - .env
```

Then run with:

```bash  theme={null}
docker compose up
```

## Test your agent locally

After setting up your environment and building your Docker image, test your agent locally using either `docker run` or `docker compose`.

Open your browser to [http://localhost:8080](http://localhost:8080) to verify your agent is running correctly.

## Publish your Docker image

To deploy your agent to cloud platforms, publish your Docker image to a container registry such as Docker Hub, Google Container Registry, or Amazon Elastic Container Registry.

The following example shows how to publish your image to Docker Hub:

```bash  theme={null}
docker tag my-agent-app <DOCKERHUB_USERNAME>/my-agent-app:latest
docker login
docker push <DOCKERHUB_USERNAME>/my-agent-app:latest
```

Once your image is in a registry, deploy it to services such as AWS ECS, Azure Container Instances, or Kubernetes.

## Troubleshoot issues

### Common issues

**Agent fails to start**

* Verify your `WRITER_API_KEY` is set correctly
* Check that all required dependencies are installed
* Review container logs for specific error messages

**Port binding errors**

* Ensure the port in your `Dockerfile` matches the port you're trying to access
* Check that the port isn't already in use by another service

**Memory or CPU issues**

* Increase resource allocation in your cloud platform
* Optimize your agent's code for better performance
* Consider using a more powerful instance type

### Debug locally

Run your container with verbose logging to debug issues:

```bash  theme={null}
docker run -e WRITER_LOG_LEVEL=DEBUG -p 8080:8080 my-agent-app
```

## Next steps

* Learn how to [sync your local agent with cloud agents](/agent-builder/sync-agent) for easier deployment
* Explore [custom Python code](/agent-builder/python-code) to extend your agent's capabilities
* Set up [secrets management](/agent-builder/secrets) for production deployments in the Writer cloud

<feedback />
