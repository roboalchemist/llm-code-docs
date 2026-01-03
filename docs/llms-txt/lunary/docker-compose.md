# Source: https://docs.lunary.ai/docs/more/self-hosting/docker-compose.md

# Docker Compose

Lunary is designed to be simple to self-host using Docker Compose, which makes managing all components easier.

<Note>
  Note: The Docker Compose setup is **available** only with [Lunary Enterprise
  Edition](https://lunary.ai/pricing)
</Note>

## Steps

<Steps>
  <Step title="Set up a PostgreSQL database">
    First, set up a PostgreSQL database (version 15 or higher). This can be on the same host or a separate server.

    You'll need the following information for your database:

    * Host address and port
    * Database name
    * Username and password with appropriate permissions

    For production use, we recommend using a managed PostgreSQL service or properly configuring your self-hosted PostgreSQL instance with backups and security.
  </Step>

  <Step title="Log in to the private Docker Repository">
    Make sure Docker is installed on your host machine before running the following command:

    ```bash  theme={null}
    docker login -u lunarycustomer
    ```

    Then, paste your organization's access token, which will be provided by Lunary when your subscription is activated.
  </Step>

  <Step title="Create the Docker Compose file">
    Create a new directory for your Lunary installation and create a `docker-compose.yml` file with the following content:

    ```yaml  theme={null}
    services:
      backend:
        container_name: lunary-backend
        image: lunary/backend:latest # or specific version (lunary/backend:1.9.8 - contact Lunary support for available versions)
        ports:
          - "3333:3333"
        restart: unless-stopped
        environment:
          DATABASE_URL: ${DATABASE_URL}
          API_URL: ${API_URL:-http://localhost:3333}
          APP_URL: ${APP_URL:-http://localhost:8080}
          JWT_SECRET: ${JWT_SECRET}
          LICENSE_KEY: ${LICENSE_KEY}
          IS_SELF_HOSTED: "true"
          # Optional environment variables for playground
          OPENAI_API_KEY: ${OPENAI_API_KEY:-}
          AZURE_OPENAI_API_KEY: ${AZURE_OPENAI_API_KEY:-}
          AZURE_OPENAI_RESOURCE_NAME: ${AZURE_OPENAI_RESOURCE_NAME:-}
          AZURE_OPENAI_DEPLOYMENT_ID: ${AZURE_OPENAI_DEPLOYMENT_ID:-}
          ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY:-}
          OPENROUTER_API_KEY: ${OPENROUTER_API_KEY:-}
          PALM_API_KEY: ${PALM_API_KEY:-}
          # Email configuration
          EMAIL_SENDER_ADDRESS: ${EMAIL_SENDER_ADDRESS:-}
          SMTP_HOST: ${SMTP_HOST:-}
          SMTP_PORT: ${SMTP_PORT:-}
          SMTP_USER: ${SMTP_USER:-}
          SMTP_PASSWORD: ${SMTP_PASSWORD:-}
        networks:
          - lunary-network
        depends_on:
          - ml
          - enrichers
        healthcheck:
          test: ["CMD", "curl", "-f", "http://localhost:3333/v1/health"]
          interval: 10s
          start_period: 20s
          timeout: 10s
          retries: 3

      frontend:
        container_name: lunary-frontend
        image: lunary/frontend:latest
        ports:
          - "8080:8080"
        restart: unless-stopped
        environment:
          API_URL: ${API_URL:-http://localhost:3333}
          APP_URL: ${APP_URL:-http://localhost:8080}
        networks:
          - lunary-network
        depends_on:
          - backend
        healthcheck:
          test: ["CMD", "curl", "-f", "http://localhost:8080"]
          interval: 10s
          start_period: 20s
          timeout: 10s
          retries: 3

      enrichers:
        container_name: lunary-enrichers
        image: lunary/realtime-evaluators:latest
        ports:
          - "3334:3333"
        restart: unless-stopped
        environment:
          DATABASE_URL: ${DATABASE_URL}
          ML_URL: http://ml:4242
        networks:
          - lunary-network
        depends_on:
          - ml

      ml:
        container_name: lunary-ml
        image: lunary/ml:latest
        ports:
          - "4242:4242"
        restart: unless-stopped
        environment:
          DATABASE_URL: ${DATABASE_URL}
        networks:
          - lunary-network
        healthcheck:
          test: ["CMD", "curl", "-f", "http://localhost:4242/health"]
          interval: 20s
          start_period: 80s
          timeout: 10s
          retries: 5

      autoheal:
        restart: always
        image: willfarrell/autoheal
        environment:
          AUTOHEAL_CONTAINER_LABEL: all
        volumes:
          - /var/run/docker.sock:/var/run/docker.sock

    networks:
      lunary-network:
    ```

    This configuration includes:

    * `backend`: The Lunary API server
    * `frontend`: The Lunary web interface
    * `enrichers`: Enriches your data by communicating with the ml service
    * `ml`: The machine learning service for advanced features
    * `autoheal`: A service to automatically restart unhealthy containers

    Each service is configured with health checks to ensure reliability.
  </Step>

  <Step title="Create the environment file">
    In the same directory, create a `.env` file with the following variables:

    ```env  theme={null}
    # Required configuration
    DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<dbname>
    API_URL=http://localhost:3333
    APP_URL=http://localhost:8080
    JWT_SECRET=<your_jwt_secret>
    LICENSE_KEY=<your_license_key>

    # Optional: API keys for AI services (needed for playground)
    OPENAI_API_KEY=
    ANTHROPIC_API_KEY=
    OPENROUTER_API_KEY=
    PALM_API_KEY=

    # Optional: Azure OpenAI configuration
    AZURE_OPENAI_API_KEY=
    AZURE_OPENAI_RESOURCE_NAME=
    AZURE_OPENAI_DEPLOYMENT_ID=

    # Optional: Email configuration (if not provided, no emails will be sent)
    EMAIL_SENDER_ADDRESS=
    SMTP_HOST=
    SMTP_PORT=
    SMTP_USER=
    SMTP_PASSWORD=
    ```

    Replace the placeholder values with your actual configuration:

    * `<username>, <password>, <host>, <port>, <dbname>`: Your PostgreSQL database credentials
    * `<your-backend-ip-or-url>`, `<your-frontend-ip-or-url>`: Your server's IP address or domain name
    * `<your_jwt_secret>`: A secure random string for JWT token generation
    * `<your_license_key>`: Your Lunary Enterprise Edition license key

    The other environment variables are optional and enable specific features:

    * API keys for various AI services enable the playground
    * Email configuration allows Lunary to send invitation emails to organization members

    ````
    </Step>


    <Step title="Start the services" >
    Run the following command to start all services:

    ```bash
    docker compose up -d
    ````

    This will pull the necessary images and start all services in detached mode. You can check the status of your services with:

    ```bash  theme={null}
    docker compose ps
    ```

    And view logs with:

    ```bash  theme={null}
    docker compose logs -f
    ```

    Or for a specific service:

    ```bash  theme={null}
    docker compose logs -f backend
    ```
  </Step>

  <Step title="🎉 Done!">
    You're all set! Open `http://<your-frontend-ip-or-url>:8080` to access the app. <br />
    Make sure to export the environment variable `LUNARY_API_URL=http://<your-backend-ip-or-url>:3333` when using the SDK to send queries to your server.
  </Step>
</Steps>

## Troubleshooting

### Requested access to the resource is denied

You need to log in to the private Docker repository before running the containers. Make sure you have the correct access token and that you are logged in:

```bash  theme={null}
docker login -u lunarycustomer
```

### Cannot connect to the database

Verify that your `DATABASE_URL` is correct and that the database is accessible from the Docker containers. If your PostgreSQL server is on the same host, make sure it's configured to accept connections from Docker containers.

### Container health checks are failing

Check the container logs for specific error messages:

```bash  theme={null}
docker compose logs backend
docker compose logs ml
docker compose logs enrichers
docker compose logs frontend
```

### Error: Client network socket disconnected before secure TLS connection was established

This means the database's SSL certificate is not properly set. Either fix the SSL certificate or disable SSL by adding `?sslmode=disable` to the `DATABASE_URL` environment variable (not recommended if the database is exposed to the internet):

```
DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<dbname>?sslmode=disable
```

### Services are not communicating with each other

If services can't communicate with each other despite being on the same Docker network, check that the service names match the hostnames used in environment variables (e.g., `ML_URL` should be `http://ml:3333` to properly resolve the ML service).

### Frontend showing "Failed to connect to the API"

This typically happens when:

1. The backend service is not running or healthy
2. The `API_URL` is not correctly set in the frontend service
3. There's a network issue preventing the frontend from reaching the backend

Check the backend logs and verify that the `API_URL` is correctly set in both the frontend container and your browser's environment.

## Upgrading

To upgrade to a newer version of Lunary:

1. Pull the latest images:

   ```bash  theme={null}
   docker compose pull
   ```

2. Restart the services:
   ```bash  theme={null}
   docker compose down
   docker compose up -d
   ```

This will update all services to the latest available versions while preserving your configuration.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt