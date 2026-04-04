# Source: https://docs.carv.io/d.a.t.a.-ai-framework/quick-start-guide.md

# Quick Start Guide

This guide will help you set up and run your first D.A.T.A framework agent. Follow these steps to get started quickly.

### Prerequisites

* Go 1.19 or higher
* SQLite3
* Git
* Discord/Twitter/Telegram API credentials (optional)
* CARV API key

### Installation

1. Clone the repository:

```bash
git clone https://github.com/carv-protocol/d.a.t.a
cd d.a.t.a
```

2. Install dependencies:

```bash
go mod download
```

### Basic Configuration

1. Create a `.env` file in the project root:

```env
# LLM Configuration
LLM_API_KEY=your_api_key
LLM_PROVIDER=openai

# CARV Configuration
CARV_DATA_BASE_URL=https://api.carv.io
CARV_DATA_API_KEY=your_carv_api_key

# Optional Social Media Configuration
DISCORD_API_TOKEN=your_discord_token
TWITTER_API_KEY=your_twitter_key
TWITTER_API_KEY_SECRET=your_twitter_secret
TWITTER_ACCESS_TOKEN=your_twitter_access
TWITTER_TOKEN_SECRET=your_twitter_token
TELEGRAM_BOT_TOKEN=your_telegram_token
```

2. Create a basic character configuration (`src/config/character.json`):

```json
{
  "name": "DataAgent",
  "system": "An AI agent for Web3 data analysis",
  "bio": [
    "Specialized in blockchain data analysis",
    "Expert in token-based interactions"
  ],
  "style": {
    "tone": ["professional", "helpful", "precise"],
    "constraints": []
  },
  "goals": [
    {
      "name": "Data Analysis",
      "description": "Provide accurate blockchain data analysis",
      "priority": 0.8
    }
  ],
  "priority_accounts": [
    {
      "platform": "discord",
      "id": "your_priority_account_id"
    }
  ]
}
```

3. Update the config file (`src/config/config.yaml`)

> Config will be override by the env vars.

```
character:
  # Path to character configuration file
  path: "./src/config/character_data_agent.json"

database:
  # Database type: "sqlite" or "postgres"
  type: "sqlite"
  # Database path (for SQLite) or connection string (for Postgres)
  path: "./data/agent.db"

llm_config:
  # LLM provider: "openai", "deepseek", etc.
  provider: "deepseek"
  # API key for the LLM provider
  api_key: ""
  # Base URL for API calls
  base_url: "https://api.deepseek.com"
  # Model name
  model: "deepseek-chat"

data:
  carvid:
    # CarvID API endpoint
    url: "https://api.carv.io/v1"
    # API key for CarvID
    api_key: "your-carvid-api-key-here"

token:
  network: "base"
  ticker: "carv"
```

### Running Your First Agent

1. Build the project:

```bash
go build -o data-agent ./src/cmd/agent
```

2. Run the agent:

```bash
./data-agent
```

### Basic Usage Examples

#### 1. Implementing a Custom Tool

```go
package tools

import (
    "context"
    "github.com/carv-protocol/d.a.t.a/src/internal/core"
)

type CustomTool struct{}

func (t *CustomTool) Initialize(ctx context.Context) error {
    return nil
}

func (t *CustomTool) Name() string {
    return "custom tool"
}

func (t *CustomTool) Description() string {
    return "A custom tool for specific functionality"
}

func (t *CustomTool) AvailableActions() []core.Action {
    return nil
}
```

#### 2. Adding a New Social Platform Integration

```go
package social

import (
    "context"
    "github.com/carv-protocol/d.a.t.a/src/internal/core"
)

type CustomPlatform struct {
    // Your platform-specific fields
}

func (p *CustomPlatform) SendMessage(ctx context.Context, msg core.SocialMessage) error {
    // Implementation
    return nil
}

func (p *CustomPlatform) GetMessageChannel() <-chan core.SocialMessage {
    // Implementation
    return nil
}
```

### Common Operations

#### Checking Token Balance

```go
balance, err := tokenManager.FetchNativeTokenBalance(
    context.Background(),
    "user_id",
    "platform",
)
if err != nil {
    log.Printf("Error fetching balance: %v", err)
    return
}
log.Printf("User balance: %f", balance.Balance)
```

#### Processing Social Messages

```go
msg := &core.SocialMessage
    Type:     "message",
    Content:  "Hello, agent!",
    Platform: "discord",
    FromUser: "user123",
}

processedMsg, err := agent.ProcessMessage(context.Background(), msg)
if err != nil {
    log.Printf("Error processing message: %v", err)
    return
}
```

### Common Issues and Solutions

1. **Database Connection Issues**
   * Ensure SQLite3 is installed
   * Check database path permissions
   * Verify database file exists
2. **API Authentication Errors**
   * Validate API keys in .env file
   * Check API endpoint availability
   * Confirm network connectivity
3. **Memory Management**
   * Monitor memory usage
   * Adjust batch sizes if needed
   * Check for memory leaks

### Next Steps

1. Explore the [full documentati](https://docs.carv.io/d.a.t.a.-ai-framework)
2. Join D.A.T.A [Discord community](https://discord.gg/AYyfmhMn5K)
3. Check out example implementations in the `/examples` directory
4. Learn about advanced features in the Architecture Guide
