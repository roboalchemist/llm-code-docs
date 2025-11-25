# Source: https://www.activepieces.com/docs/install/options/docker.md

# Docker

> Single docker image deployment with SQLite3 and Memory Queue

<Warning>
  This setup is only meant for personal use or testing. It runs on SQLite3 and an in-memory Redis queue, which supports only a single instance on a single machine. For production or multi-instance setups, you must use Docker Compose with PostgreSQL and Redis.
</Warning>

To get up and running quickly with Activepieces, we will use the Activepieces Docker image. Follow these steps:

## Prerequisites

You need to have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker](https://docs.docker.com/get-docker/) installed on your machine in order to set up Activepieces via Docker Compose.

## Install

### Pull Image and Run Docker image

Pull the Activepieces Docker image and run the container with the following command:

```bash  theme={null}
docker run -d -p 8080:80 -v ~/.activepieces:/root/.activepieces -e AP_REDIS_TYPE=MEMORY -e AP_DB_TYPE=SQLITE3 -e AP_FRONTEND_URL="http://localhost:8080" activepieces/activepieces:latest
```

### Configure Webhook URL (Important for Triggers, Optional If you have public IP)

**Note:** By default, Activepieces will try to use your public IP for webhooks. If you are self-hosting on a personal machine, you must configure the frontend URL so that the webhook is accessible from the internet.

**Optional:** The easiest way to expose your webhook URL on localhost is by using a service like ngrok. However, it is not suitable for production use.

1. Install ngrok
2. Run the following command:

```bash  theme={null}
ngrok http 8080
```

3. Replace `AP_FRONTEND_URL` environment variable in the command line above.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=85cc8d40c4ad2ede8e8ad83fcb6e6b42" alt="Ngrok" data-og-width="961" width="961" data-og-height="509" height="509" data-path="resources/screenshots/docker-ngrok.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3c787f690f4700e8d2ac0115b86554e5 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=ce675bfcc849cfe97d79fe6defdb69bc 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=d5f1a1530820f43048b1d6110bb88d50 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0d917892d782b38aaabcd94d2d3b0c09 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=ff5dfdbbed7b1b24ec65fe48e826ad20 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=09c2e4f0aacdcc60602ed8f3137e908d 2500w" />

## Upgrade

Please follow the steps below:

### Step 1: Back Up Your Data (Recommended)

Before proceeding with the upgrade, it is always a good practice to back up your Activepieces data to avoid any potential data loss during the update process.

1. **Stop the Current Activepieces Container:** If your Activepieces container is running, stop it using the following command:
   ```bash  theme={null}
   docker stop activepieces_container_name
   ```

2. **Backup Activepieces Data Directory:** By default, Activepieces data is stored in the `~/.activepieces` directory on your host machine. Create a backup of this directory to a safe location using the following command:
   ```bash  theme={null}
   cp -r ~/.activepieces ~/.activepieces_backup
   ```

### Step 2: Update the Docker Image

1. **Pull the Latest Activepieces Docker Image:** Run the following command to pull the latest Activepieces Docker image from Docker Hub:
   ```bash  theme={null}
   docker pull activepieces/activepieces:latest
   ```

### Step 3: Remove the Existing Activepieces Container

1. **Stop and Remove the Current Activepieces Container:** If your Activepieces container is running, stop and remove it using the following commands:
   ```bash  theme={null}
   docker stop activepieces_container_name
   docker rm activepieces_container_name
   ```

### Step 4: Run the Updated Activepieces Container

Now, run the updated Activepieces container with the latest image using the same command you used during the initial setup. Be sure to replace `activepieces_container_name` with the desired name for your new container.

```bash  theme={null}
docker run -d -p 8080:80 -v ~/.activepieces:/root/.activepieces -e AP_REDIS_TYPE=MEMORY -e AP_DB_TYPE=SQLITE3 -e AP_FRONTEND_URL="http://localhost:8080" --name activepieces_container_name activepieces/activepieces:latest
```

Congratulations! You have successfully upgraded your Activepieces Docker deployment
