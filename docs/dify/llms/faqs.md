# Source: https://docs.dify.ai/en/self-host/quick-start/faqs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# FAQs

## Deployment Methods

### Install older version

Use the `--branch` flag to install a specific version:

```bash  theme={null}
git clone https://github.com/langgenius/dify.git --branch 0.15.3
```

The rest of the setup is identical to installing the latest version.

### Install using ZIP archive

For network-restricted environments or when git is unavailable:

```bash  theme={null}
# Download latest release
wget -O dify.zip "$(curl -s https://api.github.com/repos/langgenius/dify/releases/latest | jq -r '.zipball_url')"
unzip dify.zip && rm dify.zip
```

Alternatively, download the ZIP on another device and transfer it manually.

**To upgrade:**

```bash  theme={null}
wget -O dify-latest.zip "$(curl -s https://api.github.com/repos/langgenius/dify/releases/latest | jq -r '.zipball_url')"
unzip dify-latest.zip && rm dify-latest.zip
rsync -a dify-latest/ dify/
rm -rf dify-latest/
cd dify/docker
docker compose pull
docker compose up -d
```

## Backup Procedures

### Create backup before upgrading

Always backup before upgrading to prevent data loss:

```bash  theme={null}
cp -r dify "dify.bak.$(date +%Y%m%d%H%M%S)"
```

This creates a timestamped backup for easy restoration.


Built with [Mintlify](https://mintlify.com).