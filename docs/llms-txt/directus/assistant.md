# Source: https://directus.io/docs/raw/guides/ai/assistant.md

# Overview

> Chat with an AI assistant directly inside Directus. Create content, manage your schema, trigger automations, and explore your data through natural conversation.

Directus AI Assistant is an embedded conversational assistant that helps you interact with your Directus instance through natural language.

<video title="AI Assistant creating a blog post" autoPlay="true" playsInline="true" muted="true" loop="true" controls="true" className="rounded-md">
<source src="/docs/video/ai-chat-blog-post.mp4" type="video/mp4" />
</video>

<callout color="info" icon="material-symbols:info">

**AI Assistant requires an API key from a supported provider.** Administrators [configure API keys](/guides/ai/assistant/setup) for OpenAI, Anthropic, Google, or an OpenAI-compatible endpoint in Settings → AI.

</callout>

## What can AI Assistant do?

- **Content Management**: Create, update, and organize items across your collections
- **Schema Operations**: Explore your data model, add new fields and collections
- **Flow Automation**: Create new Flows and trigger them manually
- **File Attachments**: Upload images, documents, audio, and video for AI analysis
- **Data Exploration**: Query your data and understand your schema structure

## Supported Models

### <icon className="align-middle,mr-1,size-5" name="i-simple-icons-openai"></icon> OpenAI

<table>
<thead>
  <tr>
    <th>
      Model
    </th>
    
    <th>
      Model ID
    </th>
    
    <th>
      Context Window Size
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      GPT-4o Mini
    </td>
    
    <td>
      <code>
        gpt-4o-mini
      </code>
    </td>
    
    <td>
      128k tokens
    </td>
  </tr>
  
  <tr>
    <td>
      GPT-4.1 Nano
    </td>
    
    <td>
      <code>
        gpt-4.1-nano
      </code>
    </td>
    
    <td>
      1M tokens
    </td>
  </tr>
  
  <tr>
    <td>
      GPT-4.1 Mini
    </td>
    
    <td>
      <code>
        gpt-4.1-mini
      </code>
    </td>
    
    <td>
      1M tokens
    </td>
  </tr>
  
  <tr>
    <td>
      GPT-4.1
    </td>
    
    <td>
      <code>
        gpt-4.1
      </code>
    </td>
    
    <td>
      1M tokens
    </td>
  </tr>
  
  <tr>
    <td>
      GPT-5 Nano
    </td>
    
    <td>
      <code>
        gpt-5-nano
      </code>
    </td>
    
    <td>
      400k tokens
    </td>
  </tr>
  
  <tr>
    <td>
      GPT-5 Mini
    </td>
    
    <td>
      <code>
        gpt-5-mini
      </code>
    </td>
    
    <td>
      400k tokens
    </td>
  </tr>
  
  <tr>
    <td>
      GPT-5
    </td>
    
    <td>
      <code>
        gpt-5
      </code>
    </td>
    
    <td>
      400k tokens
    </td>
  </tr>
  
  <tr>
    <td>
      GPT-5.2
    </td>
    
    <td>
      <code>
        gpt-5.2
      </code>
    </td>
    
    <td>
      400k tokens
    </td>
  </tr>
  
  <tr>
    <td>
      GPT-5.2 Chat
    </td>
    
    <td>
      <code>
        gpt-5.2-chat-latest
      </code>
    </td>
    
    <td>
      128k tokens
    </td>
  </tr>
  
  <tr>
    <td>
      GPT-5.2 Pro
    </td>
    
    <td>
      <code>
        gpt-5.2-pro
      </code>
    </td>
    
    <td>
      400k tokens
    </td>
  </tr>
</tbody>
</table>

### <icon className="align-middle,mr-1,size-5" name="i-simple-icons-anthropic"></icon> Anthropic

<table>
<thead>
  <tr>
    <th>
      Model
    </th>
    
    <th>
      Model ID
    </th>
    
    <th>
      Context Window Size
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Claude Haiku 4.5
    </td>
    
    <td>
      <code>
        claude-haiku-4-5
      </code>
    </td>
    
    <td>
      200k tokens
    </td>
  </tr>
  
  <tr>
    <td>
      Claude Sonnet 4.5
    </td>
    
    <td>
      <code>
        claude-sonnet-4-5
      </code>
    </td>
    
    <td>
      200k tokens
    </td>
  </tr>
  
  <tr>
    <td>
      Claude Opus 4.5
    </td>
    
    <td>
      <code>
        claude-opus-4-5
      </code>
    </td>
    
    <td>
      200k tokens
    </td>
  </tr>
</tbody>
</table>

### <icon className="align-middle,mr-1,size-5" name="i-simple-icons-googlegemini"></icon> Google

<table>
<thead>
  <tr>
    <th>
      Model
    </th>
    
    <th>
      Model ID
    </th>
    
    <th>
      Context Window Size
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Gemini 2.5 Flash
    </td>
    
    <td>
      <code>
        gemini-2.5-flash
      </code>
    </td>
    
    <td>
      1M tokens
    </td>
  </tr>
  
  <tr>
    <td>
      Gemini 2.5 Pro
    </td>
    
    <td>
      <code>
        gemini-2.5-pro
      </code>
    </td>
    
    <td>
      1M tokens
    </td>
  </tr>
  
  <tr>
    <td>
      Gemini 3 Flash Preview
    </td>
    
    <td>
      <code>
        gemini-3-flash-preview
      </code>
    </td>
    
    <td>
      1M tokens
    </td>
  </tr>
  
  <tr>
    <td>
      Gemini 3 Pro Preview
    </td>
    
    <td>
      <code>
        gemini-3-pro-preview
      </code>
    </td>
    
    <td>
      1M tokens
    </td>
  </tr>
</tbody>
</table>

### <icon className="align-middle,mr-1,size-5" name="material-symbols:cloud"></icon> OpenAI-Compatible

Use any OpenAI-compatible API endpoint including self-hosted models (Ollama, LM Studio), Azure OpenAI, DeepSeek, Mistral, and more. Configure custom models in [Settings → AI](/guides/ai/assistant/setup#openai-compatible-providers).

Have feedback or feature requests? [Submit on our roadmap](https://roadmap.directus.io/).

## Key Features

- **Tool Approval**: All tools require approval by default. [Configure per-tool settings](/guides/ai/assistant/tools#tool-behavior).
- **Uses Your Permissions**: The AI operates with your existing Directus role and access policies.
- **File Attachments**: Upload files or select from your library. Supports images, PDFs, text, audio, and video up to 50MB.
- **Streaming Responses**: Responses stream in real-time. Stop or retry at any time.

<callout color="warning" icon="material-symbols:warning">

**Conversations are stored in your browser only.** They are not saved to the server or shared between devices. Closing your browser or clearing localStorage will delete your conversation history.

</callout>

---

## Get Started

<card-group>
<card icon="material-symbols:settings" title="Admin Setup" to="/guides/ai/assistant/setup">

Configure API keys and customize the AI assistant behavior.

</card>

<card icon="material-symbols:chat" title="User Guide" to="/guides/ai/assistant/usage">

Learn how to use AI Assistant effectively in your daily workflow.

</card>

<card icon="material-symbols:construction" title="Available Tools" to="/guides/ai/assistant/tools">

Reference of all tools the AI can use to interact with Directus.

</card>

<card icon="material-symbols:lightbulb" title="Tips & Best Practices" to="/guides/ai/assistant/tips">

Get the most out of AI Assistant with practical tips and example prompts.

</card>

<card icon="material-symbols:security" title="Security" to="/guides/ai/assistant/security">

Access control, data protection, and security considerations.

</card>
</card-group>
