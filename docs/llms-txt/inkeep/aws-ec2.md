# Source: https://docs.inkeep.com/deployment/aws-ec2

# Deploy to AWS EC2 (/deployment/aws-ec2)

Deploy to AWS EC2 with Docker Compose



## Create a VM Instance

* Go to [Compute Engine](https://console.aws.amazon.com/ec2/v2/home).
* Launch an instance
* Select Amazon Machine Image (AMI)
* Recommended size is at least `t2.large` (2 vCPU, 8 GiB Memory).
* Click "Edit" in the "Network settings" section. Set up an Inbound Security Group Rules for (TCP, 3000, 0.0.0.0/0), (TCP, 3002-3003, 0.0.0.0/0), (TCP, 3050-3051, 0.0.0.0/0), and (TCP, 3080, 0.0.0.0/0). These are the ports exposed by the Inkeep services.
* Auto-assign public IP
* Increase the size of storage to at least 100 GiB.

## Install Docker Compose

1. SSH into the EC2 Instance

2. Install packages

```bash
sudo dnf update
sudo dnf install -y git
sudo dnf install -y docker
```

```bash
sudo mkdir -p /usr/libexec/docker/cli-plugins
sudo curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-$(uname -m) -o /usr/libexec/docker/cli-plugins/docker-compose
sudo chmod +x /usr/libexec/docker/cli-plugins/docker-compose
```

## Deploy SigNoz and Nango

<>
  Clone this repo, which includes Docker files with SigNoz and Nango:

  ```bash
  git clone https://github.com/inkeep/agents-optional-local-dev inkeep-external-services
  cd inkeep-external-services
  ```

  Run this command to autogenerate a `.env` file:

  ```bash
  cp .env.docker.example .env && \
    nango_encryption_key=$(openssl rand -base64 32) && \
    nango_dashboard_password=$(openssl rand -base64 8) && \
    tmp_file=$(mktemp) && \
    sed \
      -e "s|<REPLACE_WITH_NANGO_ENCRYPTION_KEY>|$nango_encryption_key|" \
      -e "s|<REPLACE_WITH_NANGO_DASHBOARD_PASSWORD>|$nango_dashboard_password|" \
      .env > "$tmp_file" && \
    mv "$tmp_file" .env && \
    echo "Docker environment file created with auto-generated NANGO_ENCRYPTION_KEY and NANGO_DASHBOARD_PASSWORD"
  ```

  Nango requires a `NANGO_ENCRYPTION_KEY`. Once you create this, it cannot be edited.

  Here's an overview of the important environment variables when deploying to production. Make sure to review all of these in your `.env` file.

  ```bash
  NANGO_ENCRYPTION_KEY=<nango_encryption_key>

  # Replace these with your <vm_ip> in production!
  NANGO_SERVER_URL=http://<vm_ip>:3050
  NANGO_PUBLIC_CONNECT_URL=http://<vm_ip>:3051

  # Modify these in production environments!
  NANGO_DASHBOARD_USERNAME=admin@example.com
  NANGO_DASHBOARD_PASSWORD=adminADMIN!@12
  ```

  Build and deploy SigNoz, Nango, OTEL Collector, and Jaeger:

  ```bash
  docker compose up -d
  ```

  This may take up to 5 minutes to start.

  ### Retrieve your SigNoz and Nango API Keys

  To get your SigNoz API key `SIGNOZ_API_KEY`:

  * Open SigNoz in a browser at `http://<vm_ip>:3080`
  * On first login, you will be prompted to create an admin account.
  * Navigate to Settings → Account Settings → API Keys → New Key
  * Choose a role, Viewer is sufficient for observability
  * Set the expiration field to "No Expiry" to prevent the key from expiring

  <Note>
    By default, the retention period for conversation data and traces is set to **15 days**. To set a longer retention period, navigate to the **General** tab on the **Settings** page in SigNoz.
  </Note>

  To get your Nango secret key `NANGO_SECRET_KEY`:

  * Open Nango in a browser at `http://<vm_ip>:3050`
  * Nango auto-creates two environments, Prod and Dev. Select the one you will use.
  * Navigate to Environment Settings to find the secret key
</>

## Deploy the Inkeep Agent Framework

<>
  From the root directory, create a new project directory for the Docker Compose setup for the Inkeep Agent Framework

  ```bash
  mkdir inkeep && cd inkeep
  wget https://raw.githubusercontent.com/inkeep/agents/refs/heads/main/docker-compose.yml
  wget https://raw.githubusercontent.com/inkeep/agents/refs/heads/main/.env.docker.example
  ```

  Generate a `.env` file from the example:

  ```bash
  cp .env.docker.example .env && \
  \
    # Core secrets
    inkeep_agents_manage_ui_password=$(openssl rand -base64 8) && \
    inkeep_agents_run_api_bypass_secret=$(openssl rand -base64 32) && \
    inkeep_agents_jwt_signing_secret=$(openssl rand -base64 32) && \
    better_auth_secret=$(openssl rand -base64 32) && \
    spicedb_preshared_key=$(openssl rand -base64 32) && \
    jwt_tmp_priv=$(mktemp) && \
    jwt_tmp_pub=$(mktemp) && \
    openssl genrsa -out "$jwt_tmp_priv" 2048 2>/dev/null && \
    openssl rsa -in "$jwt_tmp_priv" -pubout -out "$jwt_tmp_pub" 2>/dev/null && \
    inkeep_agents_temp_jwt_private_key=$(base64 -i "$jwt_tmp_priv" | tr -d '\n') && \
    inkeep_agents_temp_jwt_public_key=$(base64 -i "$jwt_tmp_pub" | tr -d '\n') && \
    rm -f "$jwt_tmp_priv" "$jwt_tmp_pub" && \
    tmp_file=$(mktemp) && \
    sed \
      -e "s|<REPLACE_WITH_INKEEP_AGENTS_MANAGE_UI_PASSWORD>|$inkeep_agents_manage_ui_password|" \
      -e "s|<REPLACE_WITH_INKEEP_AGENTS_RUN_API_BYPASS_SECRET>|$inkeep_agents_run_api_bypass_secret|" \
      -e "s|<REPLACE_WITH_INKEEP_AGENTS_JWT_SIGNING_SECRET>|$inkeep_agents_jwt_signing_secret|" \
      -e "s|<REPLACE_WITH_BETTER_AUTH_SECRET>|$better_auth_secret|" \
      -e "s|<REPLACE_WITH_SPICEDB_PRESHARED_KEY>|$spicedb_preshared_key|" \
      -e "s|<REPLACE_WITH_INKEEP_AGENTS_TEMP_JWT_PRIVATE_KEY>|$inkeep_agents_temp_jwt_private_key|" \
      -e "s|<REPLACE_WITH_INKEEP_AGENTS_TEMP_JWT_PUBLIC_KEY>|$inkeep_agents_temp_jwt_public_key|" \
      .env > "$tmp_file" && \
    mv "$tmp_file" .env && \
    echo "✅ Docker .env created with autogenerated secrets."
  ```

  Here's an overview of the important environment variables when deploying to production. Make sure to review all of these in your `.env` file.

  ```bash
  ENVIRONMENT=production

  # (1) AI Provider Keys (you need at least one)
  ANTHROPIC_API_KEY=
  OPENAI_API_KEY=
  GOOGLE_GENERATIVE_AI_API_KEY=
  AZURE_API_KEY=

  # (2) From Nango dashboard at http://<vm_ip>:3050
  NANGO_SECRET_KEY=

  # (3) From SigNoz dashboard at http://<vm_ip>:3080
  SIGNOZ_API_KEY=

  # (4) Set these for the Manage UI at http://<vm_ip>:3000
  PUBLIC_INKEEP_AGENTS_API_URL=http://<vm_ip>:3002
  PUBLIC_NANGO_SERVER_URL=http://<vm_ip>:3050
  PUBLIC_NANGO_CONNECT_BASE_URL=http://<vm_ip>:3051
  PUBLIC_SIGNOZ_URL=http://<vm_ip>:3080

  # (5) Set these for Agents API
  INKEEP_AGENTS_MANAGE_UI_URL=http://<vm_ip>:3000
  INKEEP_AGENTS_API_URL=http://<vm_ip>:3002
  INKEEP_AGENTS_RUN_API_BYPASS_SECRET=<REPLACE_WITH_INKEEP_AGENTS_RUN_API_BYPASS_SECRET>
  ```

  <Tip>
    For long-running agents or custom deployment requirements, you can override runtime limits like execution timeouts, maximum transfers, and generation steps. See [Configure Runtime Limits](/typescript-sdk/configure-runtime-limits) for examples and the complete list of overridable settings.
  </Tip>

  Run with Docker:

  ```bash
  docker compose up -d
  ```

  Then open `http://<vm_ip>:3000` in a browser!
</>
