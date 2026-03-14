# Source: https://novita.ai/docs/guides/skyvern.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Skyvern

> Learn how to seamlessly connect Novita AI's powerful GPU infrastructure with Skyvern's automation capabilities.

The collaboration between Skyvern and Novita AI marks a significant advancement in AI-powered automation and development capabilities. By combining Skyvern's expertise in browser-based workflow automation with Novita AI's robust GPU infrastructure and model deployment platform, developers and businesses can now access a comprehensive solution for building and scaling AI applications.

Our comprehensive guide will walk you through Novita AI implementation on Skyvern, including setting up Docker Compose and leveraging Novita AI in Skyvern.

## Setting Up Docker Compose

Step 1: Ensure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is installed and running on your machine.

Step 2: Check for running PostgreSQL instances using `docker ps` the command.

Step 3: Navigate to the project directory after cloning the repository.

```bash  theme={"system"}
git clone <repository-url> && cd <repository-name>
```

Step 4: Add your LLM provider API Key on the [docker-compose.yml](https://github.com/Skyvern-AI/skyvern/blob/main/docker-compose.yml). (*If you want to run Skyvern on a remote server, make sure you set the correct server ip for the UI container in* [*docker-compose.yml*](https://github.com/Skyvern-AI/skyvern/blob/main/docker-compose.yml)*.)*

Step 5: Enter the following command via the command line.

```
docker compose up -d
```

Step 6: Access the application interface at`http://localhost:8080` in your browser to start using the UI.

## Leveraging Novita AI in Skyvern

Step 1: Update environment variables in docker-compose.yml before building the docker image.

Step 2:  Start Novita AI LLM service by running`docker compose up -d`.

<Frame>
    <img src="https://mintcdn.com/novitaai/OIO9nfACcX0vhcTI/images/third-party/LeveragingNovitaAIinSkyvern-editenvironmentvariables.jpeg?fit=max&auto=format&n=OIO9nfACcX0vhcTI&q=85&s=03a7b4e59209a08d7d78318f4707f8a7" alt="Leveraging Novita AI in Skyvern- edit environment variables" width="1710" height="472" data-path="images/third-party/LeveragingNovitaAIinSkyvern-editenvironmentvariables.jpeg" />
</Frame>


Built with [Mintlify](https://mintlify.com).