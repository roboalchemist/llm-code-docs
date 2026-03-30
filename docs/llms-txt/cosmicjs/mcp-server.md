# Source: https://www.cosmicjs.com/docs/mcp-server.md

# MCP Server

MCP (Model Context Protocol) server that exposes Cosmic CMS functionality as tools for AI assistants. Manage your content, media, object types, and generate AI content directly through Claude, Cursor, or any MCP-compatible client.

## Installation

### Using npx (recommended)
```bash
npx @cosmicjs/mcp

```
### Global installation
```bash
npm install -g @cosmicjs/mcp

```
### From source
```bash
git clone https://github.com/cosmicjs/mcp.git
cd mcp
npm install
npm run build

```
## Configuration

The server requires the following environment variables:

| Variable | Required | Description |
|----------|----------|-------------|
| `COSMIC_BUCKET_SLUG` | Yes | Your Cosmic bucket slug |
| `COSMIC_READ_KEY` | Yes | Bucket read key for read operations |
| `COSMIC_WRITE_KEY` | No | Bucket write key for write operations |

### Getting your credentials

1. Log in to your [Cosmic dashboard](https://app.cosmicjs.com)
2. Navigate to your bucket
3. Go to **Settings** → **API Access**
4. Copy your bucket slug, read key, and write key

### Claude Desktop

Add the following to your Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
```json
{
  "mcpServers": {
    "cosmic": {
      "command": "npx",
      "args": ["@cosmicjs/mcp"],
      "env": {
        "COSMIC_BUCKET_SLUG": "your-bucket-slug",
        "COSMIC_READ_KEY": "your-read-key",
        "COSMIC_WRITE_KEY": "your-write-key"
      }
    }
  }
}

```
### Cursor

Add the following to your Cursor MCP settings (`.cursor/mcp.json` in your project or `~/.cursor/mcp.json` globally):
```json
{
  "mcpServers": {
    "cosmic": {
      "command": "npx",
      "args": ["@cosmicjs/mcp"],
      "env": {
        "COSMIC_BUCKET_SLUG": "your-bucket-slug",
        "COSMIC_READ_KEY": "your-read-key",
        "COSMIC_WRITE_KEY": "your-write-key"
      }
    }
  }
}

```
## Available Tools

The MCP server provides 17 tools for managing your Cosmic content:

### Objects

| Tool | Description |
|------|-------------|
| `cosmic_objects_list` | List objects with optional type filter, status, and pagination |
| `cosmic_objects_get` | Get a single object by ID or slug |
| `cosmic_objects_create` | Create a new object (requires write key) |
| `cosmic_objects_update` | Update an existing object (requires write key) |
| `cosmic_objects_delete` | Delete an object (requires write key) |

### Media

| Tool | Description |
|------|-------------|
| `cosmic_media_list` | List media files with optional folder filter |
| `cosmic_media_get` | Get media details by ID |
| `cosmic_media_upload` | Upload media from URL or base64 (requires write key) |
| `cosmic_media_delete` | Delete a media file (requires write key) |

### Object Types

| Tool | Description |
|------|-------------|
| `cosmic_types_list` | List all object types in the bucket |
| `cosmic_types_get` | Get object type schema by slug |
| `cosmic_types_create` | Create a new object type (requires write key) |
| `cosmic_types_update` | Update object type schema (requires write key) |
| `cosmic_types_delete` | Delete an object type (requires write key) |

### AI Generation

| Tool | Description |
|------|-------------|
| `cosmic_ai_generate_text` | Generate text content using AI |
| `cosmic_ai_generate_image` | Generate and upload an AI image (requires write key) |
| `cosmic_ai_generate_video` | Generate and upload an AI video (requires write key) |

## Usage Examples

Once configured, you can interact with your Cosmic bucket using natural language:

### Content Management
```
List all blog posts in my Cosmic bucket

```
```
Create a new blog post titled "Getting Started with MCP" 
with the content "This is an introduction to the Model Context Protocol..."
```

```
Update the blog post with ID "abc123" to change its status to published
```
### Media

```
Show me all images in the "blog-images" folder
```
```
Upload this image URL to my media library: https://example.com/image.jpg
```

### Schema Management

```
Show me all object types in my bucket
```
```
Create a new object type called "Products" with fields for 
name, price, description, and image
```

### AI Generation

```
Generate a product description for a wireless bluetooth headphone
```
```
Generate an image of a futuristic city skyline at sunset 
and upload it to my media library

```

## MCP Server vs Agent Skills

The MCP server and Agent Skills serve different but complementary purposes:

| Feature | MCP Server | Agent Skills |
|---------|------------|--------------|
| **Purpose** | Direct content management | Code generation guidance |
| **Use case** | "List my blog posts" | "Build a blog with Cosmic" |
| **How it works** | AI calls tools to interact with your bucket | AI writes code using the SDK |
| **Best for** | Managing content while developing | Building applications |

**Use both together** for the best experience:
- **Agent Skills** helps your AI write application code that uses the Cosmic SDK
- **MCP Server** lets your AI directly manage content in your bucket

## Resources

- [Cosmic Documentation](/docs)
- [API Reference](/docs/api)
- [Agent Skills](/docs/agent-skills)
- [Discord Community](https://discord.com/invite/MSCwQ7D6Mg)