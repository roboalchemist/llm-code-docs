# Source: https://docs.inkeep.com/deployment/gcp-compute-engine

# Deploy to GCP Compute Engine (/deployment/gcp-compute-engine)

Deploy to GCP Compute Engine with Docker Compose



## Create a VM Instance

* Go to [Compute Engine](https://console.cloud.google.com/compute/instances) in your GCP project.
* Create an instance; a recommended size is at least `e2-standard-2` (2 vCPU, 1 core, 8 GB memory).
* Use Debian GNU/Linux 12 (bookworm)
* Increase the size of the boot disk to 100 GB.
* Allow HTTP traffic.
* Allow ingress traffic from source IPv4 ranges `0.0.0.0/0` to TCP ports: `3000, 3002, 3003, 3050, 3051, 3080`. These are the ports exposed by the Inkeep services.
* Retrieve an external IP address (if applicable, set up a static IP or set up a load balancer).

## Install Docker Compose

1. [SSH into the VM](https://cloud.google.com/compute/docs/connect/standard-ssh)

2. [Set up Docker's apt repository](https://docs.docker.com/engine/install/debian/#install-using-the-repository)

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

3. Install the Docker packages

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

4. Grant permissions

```
sudo usermod -aG docker $USER
newgrp docker
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
