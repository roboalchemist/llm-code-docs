# Source: https://www.activepieces.com/docs/install/options/docker-compose.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Docker Compose

To get up and running quickly with Activepieces, we will use the Activepieces Docker image. Follow these steps:

## Prerequisites

You need to have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker](https://docs.docker.com/get-docker/) installed on your machine in order to set up Activepieces via Docker Compose.

## Installing

**1. Clone Activepieces repository.**

Use the command line to clone Activepieces repository:

```bash  theme={null}
git clone https://github.com/activepieces/activepieces.git
```

**2. Go to the repository folder.**

```bash  theme={null}
cd activepieces
```

**3.Generate Environment variable**

Run the following command from the command prompt / terminal

```bash  theme={null}
sh tools/deploy.sh
```

<Tip>
  If none of the above methods work, you can rename the .env.example file in the root directory to .env and fill in the necessary information within the file.
</Tip>

**4. Run Activepieces.**

<Warning>
  Please note that "docker-compose" (with a dash) is an outdated version of Docker Compose and it will not work properly. We strongly recommend downloading and installing version 2 from the [here](https://docs.docker.com/compose/install/) to use Docker Compose.
</Warning>

```bash  theme={null}
docker compose -p activepieces up
```

## 4. Configure Webhook URL (Important for Triggers, Optional If you have public IP)

**Note:** By default, Activepieces will try to use your public IP for webhooks. If you are self-hosting on a personal machine, you must configure the frontend URL so that the webhook is accessible from the internet.

**Optional:** The easiest way to expose your webhook URL on localhost is by using a service like ngrok. However, it is not suitable for production use.

1. Install ngrok
2. Run the following command:

```bash  theme={null}
ngrok http 8080
```

3. Replace `AP_FRONTEND_URL` environment variable in `.env` with the ngrok url.

<img src="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/docker-ngrok.png?fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=582a33f970c20feee557523172997ad0" alt="Ngrok" data-og-width="961" width="961" data-og-height="509" height="509" data-path="resources/screenshots/docker-ngrok.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/docker-ngrok.png?w=280&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=bdf46af25beb6a2e92fceabbf9755f46 280w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/docker-ngrok.png?w=560&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=872495f39fcbed2420805f17c7f5edc6 560w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/docker-ngrok.png?w=840&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=4468c89583767ece2a35dc51eabd8d3f 840w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/docker-ngrok.png?w=1100&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=d512cbfe2c0689fcbf870ba7a3142fb4 1100w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/docker-ngrok.png?w=1650&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=ad59f73684040aa3f81488e50d5f6989 1650w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/docker-ngrok.png?w=2500&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=ddeb3188719649c6456e2d6efda05b7a 2500w" />

<Warning>
  When deploying for production, ensure that you update the database credentials and properly set the environment variables.

  Review the [configurations guide](/install/configuration/environment-variables) to make any necessary adjustments.
</Warning>

## Upgrading

To upgrade to new versions, which are installed using docker compose, perform the following steps. First, open a terminal in the activepieces repository directory and run the following commands.

### Automatic Pull

**1. Run the update script**

```bash  theme={null}
sh tools/update.sh
```

### Manually Pull

**1. Pull the new docker compose file**

```bash  theme={null}
git pull
```

**2. Pull the new images**

```bash  theme={null}
docker compose pull
```

**3. Review changelog for breaking changes**

<Warning>
  Please review breaking changes in the [changelog](../configuration/breaking-changes).
</Warning>

**4. Run the updated docker images**

```
docker compose up -d --remove-orphans
```

Congratulations! You have now successfully updated the version.

## Deleting

The following command is capable of deleting all Docker containers and associated data, and therefore should be used with caution:

```
sh tools/reset.sh
```

<Warning>
  Executing this command will result in the removal of all Docker containers and the data stored within them. It is important to be aware of the potentially hazardous nature of this command before proceeding.
</Warning>
