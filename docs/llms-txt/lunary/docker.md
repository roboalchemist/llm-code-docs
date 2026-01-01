# Source: https://docs.lunary.ai/docs/more/self-hosting/docker.md

# Docker

Lunary is designed to be simple to self-host using Docker images for the backend and frontend components.

<Note>Note: The Docker setup is available only with [Lunary Enterprise Edition](https://lunary.ai/pricing)</Note>

<Steps>
  <Step title="Set up a PostgreSQL database">
    ta (version 15 or higher).
  </Step>

  <Step title="Log in to the private Docker Repository">
    Make sure Docker is installed on your host machine before running the following command:

    ```bash  theme={null}
    docker login -u lunarycustomer
    ```

    Then, paste your organization's access token, which will be provided by Lunary when your subscription is activated.
  </Step>

  <Step title="Run the Docker images">
    Run the following commands to start the Lunary Docker images:

    For the backend:

    ```bash  theme={null}
    docker run -d \
      -e DATABASE_URL="postgresql://<username>:<password>@<host>:<port>/<dbname>" \
      -e API_URL="http://<your-backend-ip>:3333" \
      -e APP_URL="http://<your-frontend-ip>:8080" \
      -e JWT_SECRET="<jwt_secret>" \
      -e LICENSE_KEY="<your_license_key>" \
      -p "3333:3333" \
      lunary/backend:1.4.8
    ```

    For the frontend:

    ```bash  theme={null}
    docker run -d \
      -e API_URL="http://<your-backend-ip>:3333" \
      -e APP_URL="http://<your-frontend-ip>:8080" \
      -p "8080:8080" \
      lunary/frontend:1.4.8
    ```

    Note: Replace `<your-backend-ip>` and `<your-frontend-ip>` with your actual IP addresses or domain names.
  </Step>

  <Step title="Configure optional environment variables">
    The following environment variables are optional and can be used to enable the playground, evaluation, and radar features:

    ```bash  theme={null}
    OPENAI_API_KEY=sk-...
    # Or if using Azure OpenAI:
    AZURE_OPENAI_API_KEY=...
    AZURE_OPENAI_RESOURCE_NAME=...
    AZURE_OPENAI_DEPLOYMENT_ID=...

    ANTHROPIC_API_KEY=sk-...
    OPENROUTER_API_KEY=sk-...
    PALM_API_KEY=AI...
    ```

    You can also use your custom email server for sending invite members to your organization:

    ```bash  theme={null}
    EMAIL_SENDER_ADDRESS=...
    SMTP_HOST=...
    SMTP_PORT=...
    SMTP_USER=...
    SMTP_PASSWORD=...
    ```

    If those values are not provided, no email will be send and you will need to send the invitation links manually.
  </Step>

  <Step title="🎉 Done!">
    You're all set! Open `http://<your-frontend-ip-or-url>:8080` to access the app. <br />
    Make sure to export the environment variable `LUNARY_API_URL=http://<your-backend-ip-or-url>:3333` when using the SDK to send queries to your server.
  </Step>
</Steps>

## Troubleshooting

### Requested access to the resource is denied.

You need to log in to the private Docker repository before running the image. Make sure you have the correct access token and that you are logged in.

### Error: connect ECONNREFUSED 127.0.0.1:5432

If you are running the database on the same machine, you can use `--network=host` when running the Docker images.

```bash  theme={null}
docker run -d \
  -e DATABASE_URL="postgresql://postgres:mysecretpassword@localhost:5432/lunary" \
  --network=host \
  -e API_URL="http://localhost:3333" \
  -e JWT_SECRET="replace_with_your_secret_string" \
  lunary/backend:1.4.8
```

### Error: Client network socket disconnected before secure TLS connection was established

This means the database's SSL certificate is not properly set. Either fix the SSL certificate or disable SSL by removing `?sslmode=require` from the `DATABASE_URL` environment variable (not recommended if the database is exposed to the internet).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt