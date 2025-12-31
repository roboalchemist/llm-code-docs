# OpenCode Providers

## Overview

OpenCode supports 75+ LLM providers via AI SDK and Models.dev. Supports both cloud and local models.

## Setup

1. Add credentials: `/connect` command or environment variables
2. Configure provider in `opencode.json`
3. Select model: `/models` command

Credentials stored in `~/.local/share/opencode/auth.json`.

## Provider Configuration

### Base URL

Customize endpoint for any provider:

```json
{
  "provider": {
    "anthropic": {
      "options": {
        "baseURL": "https://api.anthropic.com/v1"
      }
    }
  }
}
```

## OpenCode Zen

Recommended for beginners. Tested and verified models by OpenCode team.

```bash
# Authenticate
/connect
# Select opencode
# Visit https://opencode.ai/auth
# Copy API key
```

Optional - completely standard provider.

## Major Providers

### Anthropic Claude

Claude Pro/Max recommended:

```bash
/connect
# Select Anthropic > Claude Pro/Max
# Authenticate in browser
```

Or with API key:
- Create API Key: Get code from browser
- Manually enter API Key: Paste existing key

### OpenAI

```bash
# Get key from https://platform.openai.com/api-keys
/connect
# Select OpenAI
# Enter API key
```

### Amazon Bedrock

Requirements:
1. Request model access in Bedrock console
2. Set authentication:
   - `AWS_ACCESS_KEY_ID`: IAM access key
   - `AWS_PROFILE`: SSO profile (after `aws sso login`)
   - `AWS_BEARER_TOKEN_BEDROCK`: Long-term API key

```bash
AWS_ACCESS_KEY_ID=XXX opencode
```

Or in bash profile:
```bash
export AWS_ACCESS_KEY_ID=XXX
```

### Google Vertex AI

Requirements:
1. Enable Vertex AI API
2. Set environment:
   - `GOOGLE_CLOUD_PROJECT`: Project ID (required)
   - `VERTEX_LOCATION`: Region (default: global)
   - Authentication:
     - `GOOGLE_APPLICATION_CREDENTIALS`: Service account JSON path
     - Or: `gcloud auth application-default login`

```bash
GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json \
GOOGLE_CLOUD_PROJECT=project-id \
opencode
```

Tip: Use `global` region for better availability.

### GitHub Copilot

Requires Pro+ for some models. Enable in GitHub Copilot settings.

```bash
/connect
# Select GitHub Copilot
# Visit github.com/login/device
# Enter code
```

### DeepSeek

```bash
# Get key from https://platform.deepseek.com/
/connect
# Select DeepSeek
# Enter API key
```

### Azure OpenAI

Requirements:
1. Create Azure OpenAI resource (get resource name and API key)
2. Deploy model (deployment name must match model name)

```bash
/connect
# Select Azure
# Enter API key
```

Set resource name:
```bash
export AZURE_RESOURCE_NAME=XXX
opencode
```

Endpoint: `https://RESOURCE_NAME.openai.azure.com/`

Note: If you see "cannot assist" errors, change content filter from DefaultV2 to Default.

### Other Providers

#### Groq
```bash
# Get key from https://console.groq.com/
/connect
```

#### Cerebras
```bash
# Get key from https://inference.cerebras.ai/
/connect
```

#### Together AI
```bash
# Get key from https://api.together.ai
/connect
```

#### Fireworks AI
```bash
# Get key from https://app.fireworks.ai/
/connect
```

#### OpenRouter
```bash
# Get key from https://openrouter.ai/settings/keys
/connect
```

Customize provider routing:
```json
{
  "provider": {
    "openrouter": {
      "models": {
        "moonshotai/kimi-k2": {
          "options": {
            "provider": {
              "order": ["baseten"],
              "allow_fallbacks": false
            }
          }
        }
      }
    }
  }
}
```

## Local Models

### Ollama

```json
{
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "llama2": {
          "name": "Llama 2"
        }
      }
    }
  }
}
```

Tip: Increase `num_ctx` (16k-32k) if tool calls aren't working.

### Ollama Cloud

```bash
# Get key from https://ollama.com/ > Settings > Keys
/connect

# Pull model info locally first
ollama pull gpt-oss:20b-cloud

/models
```

### LM Studio

```json
{
  "provider": {
    "lmstudio": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "LM Studio (local)",
      "options": {
        "baseURL": "http://127.0.0.1:1234/v1"
      },
      "models": {
        "google/gemma-3n-e4b": {
          "name": "Gemma 3n-e4b (local)"
        }
      }
    }
  }
}
```

### llama.cpp

```json
{
  "provider": {
    "llama.cpp": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "llama-server (local)",
      "options": {
        "baseURL": "http://127.0.0.1:8080/v1"
      },
      "models": {
        "qwen3-coder:a3b": {
          "name": "Qwen3-Coder: a3b-30b (local)",
          "limit": {
            "context": 128000,
            "output": 65536
          }
        }
      }
    }
  }
}
```

## Custom Providers

Add any OpenAI-compatible provider:

```bash
/connect
# Scroll to "Other"
# Enter provider ID (e.g., "myprovider")
# Enter API key
```

Configure in opencode.json:

```json
{
  "provider": {
    "myprovider": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "My Provider",
      "options": {
        "baseURL": "https://api.myprovider.com/v1",
        "apiKey": "{env:MY_API_KEY}",
        "headers": {
          "Authorization": "Bearer custom-token"
        }
      },
      "models": {
        "my-model": {
          "name": "My Model",
          "limit": {
            "context": 200000,
            "output": 65536
          }
        }
      }
    }
  }
}
```

Options:
- **npm**: AI SDK package (use `@ai-sdk/openai-compatible` for OpenAI-compatible APIs)
- **name**: Display name
- **baseURL**: API endpoint
- **apiKey**: API key (use `{env:VAR}` for environment variables)
- **headers**: Custom headers
- **models**: Available models
- **limit.context**: Max input tokens
- **limit.output**: Max output tokens

## Gateway Providers

### Cloudflare AI Gateway

Access multiple providers through unified endpoint with unified billing:

```bash
/connect
# Select Cloudflare AI Gateway
# Enter API token
```

Set account and gateway:
```bash
export CLOUDFLARE_ACCOUNT_ID=your-account-id
export CLOUDFLARE_GATEWAY_ID=your-gateway-id
```

Add models:
```json
{
  "provider": {
    "cloudflare-ai-gateway": {
      "models": {
        "openai/gpt-4o": {},
        "anthropic/claude-sonnet-4": {}
      }
    }
  }
}
```

### Helicone

Observability platform with logging and analytics:

```bash
# Get key from https://helicone.ai
/connect
# Select Helicone
```

Models auto-route to appropriate provider. For custom configs:

```json
{
  "provider": {
    "helicone": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Helicone",
      "options": {
        "baseURL": "https://ai-gateway.helicone.ai",
        "headers": {
          "Helicone-Cache-Enabled": "true",
          "Helicone-User-Id": "opencode"
        }
      },
      "models": {
        "gpt-4o": {
          "name": "GPT-4o"
        }
      }
    }
  }
}
```

Common headers:
- `Helicone-Cache-Enabled`: Enable caching
- `Helicone-User-Id`: Track by user
- `Helicone-Property-*`: Custom properties
- `Helicone-Session-Id`: Group requests
- `Helicone-Prompt-Id`: Prompt versioning

See [Helicone docs](https://docs.helicone.ai/helicone-headers/header-directory).

### ZenMux

```bash
# Get key from https://zenmux.ai/settings/keys
/connect
```

Add models:
```json
{
  "provider": {
    "zenmux": {
      "models": {
        "somecoolnewmodel": {}
      }
    }
  }
}
```

## Provider Management

### Disable Providers

```json
{
  "disabled_providers": ["openai", "gemini"]
}
```

### Enable Only Specific

```json
{
  "enabled_providers": ["anthropic", "openai"]
}
```

Note: `disabled_providers` takes priority.

## Troubleshooting

1. **Check auth**: `opencode auth list`
2. **Verify config**:
   - Provider ID matches `/connect` ID
   - Correct npm package
   - Valid baseURL
3. **Environment variables**: Check required vars are set
4. **Refresh models**: `opencode models --refresh`

## Model Format

Use `provider/model-id` format:
- `anthropic/claude-sonnet-4-5`
- `openai/gpt-4o`
- `opencode/gpt-5.1-codex` (OpenCode Zen)

List models: `opencode models [provider]`
