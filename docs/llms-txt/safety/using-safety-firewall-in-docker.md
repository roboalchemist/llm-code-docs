# Source: https://docs.safetycli.com/safety-docs/firewall/installation-and-configuration/using-safety-firewall-in-docker.md

# Using Safety Firewall in Docker

### Overview

Safety Firewall wraps your package manager (e.g. pip and uv) to automatically scan packages for vulnerabilities and block malicious packages before they're installed. In Docker, you install Safety first, then use it to protect your package installations.

### Prerequisites

* A Safety API key (available from your [Safety dashboard](https://docs.safetycli.com/safety-docs/firewall/installation-and-configuration/using-safety-firewall-in-docker))
* Docker with BuildKit support (recommended for secure secret handling)

### Basic Setup

The simplest approach is to install Safety and then use it to wrap your pip install command:

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install safety
RUN safety --key "YOUR_API_KEY" pip install --no-cache-dir -r requirements.txt
```

{% hint style="warning" %}
This example includes the API key directly in the Dockerfile, which is not recommended for production use. The key will be visible in your image history and any systems that have access to your Dockerfile. Use this approach only for initial testing.
{% endhint %}

### Recommended: Using Docker BuildKit Secrets

Docker BuildKit secrets allow you to pass sensitive values to your build without embedding them in the image or Dockerfile.

#### Option 1: Environment Variable

Pass your API key as an environment variable at build time.

**Dockerfile:**

```dockerfile
# syntax=docker/dockerfile:1.4
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install safety
RUN --mount=type=secret,id=safety_api_key \
    SAFETY_API_KEY="$(cat /run/secrets/safety_api_key)" && \
    safety --key "$SAFETY_API_KEY" pip install --no-cache-dir -r requirements.txt
```

**Build command:**

```bash
export SAFETY_API_KEY="your-api-key-here"

DOCKER_BUILDKIT=1 docker build \
    --secret id=safety_api_key,env=SAFETY_API_KEY \
    -t my-app .
```

#### Option 2: Using a .env File

If you prefer to store your API key in a file (useful for local development or when using .env files), you can source it directly.

**Dockerfile:**

```dockerfile
# syntax=docker/dockerfile:1.4
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install safety
RUN --mount=type=secret,id=safety_api_key \
    . /run/secrets/safety_api_key && \
    safety --key "$SAFETY_API_KEY" pip install --no-cache-dir -r requirements.txt
```

**Create a secrets file** (e.g., `safety-api-key.env`):

```bash
SAFETY_API_KEY="your-api-key-here"
```

{% hint style="info" %}
Make sure to add this file to your `.gitignore` to avoid accidentally committing your API key.
{% endhint %}

**Build command:**

```bash
DOCKER_BUILDKIT=1 docker build \
    --secret id=safety_api_key,src=./safety-api-key.env \
    -t my-app .
```

### CI/CD Integration

In CI/CD pipelines, store your Safety API key as a secret in your CI platform (GitHub Actions, GitLab CI, etc.) and pass it to the Docker build using the environment variable approach shown above.

For example, in GitHub Actions:

```yaml
- name: Build Docker image
  env:
    SAFETY_API_KEY: ${{ secrets.SAFETY_API_KEY }}
  run: |
    DOCKER_BUILDKIT=1 docker build \
        --secret id=safety_api_key,env=SAFETY_API_KEY \
        -t my-app .
```

### Troubleshooting

| Issue                       | Solution                                                               |
| --------------------------- | ---------------------------------------------------------------------- |
| `safety: command not found` | Ensure `pip install safety` runs before the Safety Firewall command    |
| Authentication errors       | Verify your API key is valid and properly passed to the build          |
| BuildKit not enabled        | Set `DOCKER_BUILDKIT=1` or configure Docker to use BuildKit by default |
