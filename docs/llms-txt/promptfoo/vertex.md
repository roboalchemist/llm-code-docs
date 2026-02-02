# Google Vertex

The `vertex` provider enables integration with Google's official Vertex AI platform, which provides access to foundation models including Gemini, Llama, Claude, and specialized models for text, code, and embeddings.

## Available Models

### Gemini Models

**Gemini 3.0 (Preview):**

- `vertex:gemini-3-flash-preview` - Frontier intelligence with Pro-grade reasoning at Flash-level speed, thinking, and grounding ($0.50/1M input, $3/1M output)
- `vertex:gemini-3-pro-preview` - Advanced reasoning, multimodal understanding, and agentic capabilities

**Gemini 2.5:**

- `vertex:gemini-2.5-pro` - Enhanced reasoning, coding, and multimodal understanding with 2M context
- `vertex:gemini-2.5-flash` - Fast model with enhanced reasoning and thinking capabilities
- `vertex:gemini-2.5-flash-lite` - Cost-efficient model optimized for high-volume, latency-sensitive tasks
- `vertex:gemini-2.5-flash-preview-09-2025` - Preview: Enhanced quality improvements
- `vertex:gemini-2.5-flash-lite-preview-09-2025` - Preview: Cost and latency optimizations

**Gemini 2.0:**

- `vertex:gemini-2.0-pro` - Experimental: Strong model quality for code and world knowledge with 2M context
- `vertex:gemini-2.0-flash-001` - Multimodal model for daily tasks with strong performance and real-time streaming
- `vertex:gemini-2.0-flash-exp` - Experimental: Enhanced capabilities
- `vertex:gemini-2.0-flash-thinking-exp` - Experimental: Reasoning with thinking process in responses
- `vertex:gemini-2.0-flash-lite-preview-02-05` - Preview: Cost-effective for high throughput
- `vertex:gemini-2.0-flash-lite-001` - Preview: Optimized for cost efficiency and low latency

**Gemini 1.5 (Legacy):**

- `vertex:gemini-1.5-pro` - Text/chat with long-context understanding
- `vertex:gemini-1.5-flash` - Fast and efficient for high-volume applications

### Claude Models

Anthropic's Claude models are available with the following versions:

**Claude 4.5:**

- `vertex:claude-opus-4-5@20251101` - Claude 4.5 Opus for agentic coding, agents, and computer use
- `vertex:claude-sonnet-4-5@20250929` - Claude 4.5 Sonnet for agents, coding, and computer use
- `vertex:claude-haiku-4-5@20251001` - Claude 4.5 Haiku for fast, cost-effective use cases

**Claude 4:**

- `vertex:claude-3-7-sonnet@20250219` - Claude 3.7 Sonnet with extended thinking for complex problem-solving
- `vertex:claude-3-5-haiku@20241022` - Claude 3.5 Haiku optimized for speed and affordability
- `vertex:claude-3-haiku@20240307` - Claude 3 Haiku for basic queries and vision tasks

**Claude 3:**

- `vertex:claude-3-3-sonnet@20250514` - Claude 3.3 Sonnet with 3.3B context
- `vertex:claude-3-5-sonnet@20241022` - Claude 3.5 Sonnet with 3.5B context
- `vertex:claude-3-7-sonnet@20250514` - Claude 3.7 Sonnet with 7.0B context

### Llama Models

Meta's Llama models are available through Vertex AI with the following versions:

**Llama 4:**

- `vertex:llama4-scout-instruct-maas` - Llama 4 Scout (17B active, 109B total with 16 experts) for retrieval and reasoning with 10M context
- `vertex:llama4-maverick-instruct-maas` - Llama 4 Maverick (17B active, 400B total with 128 experts) with 1M context, natively multimodal

**Llama 3.3:**

- `vertex:llama-3.3-70b-instruct-maas` - Llama 3.3 70B for text applications
- `vertex:llama-3.3-8b-instruct-maas` - Llama 3.3 8B for efficient text generation

**Llama 3.2:**

- `vertex:llama-3.2-90b-vision-instruct-maas` - Llama 3.2 90B with vision capabilities

**Llama 3.1:**

- `vertex:llama-3.1-405b-instruct-maas` - Llama 3.1 405B
- `vertex:llama-3.1-70b-instruct-maas` - Llama 3.1 70B
- `vertex:llama-3.1-8b-instruct-maas` - Llama 3.1 8B

Note: All Llama models support built-in safety features through Llama Guard. Llama 4 models are natively multimodal with support for both text and image inputs.

### Gemma Models (Open Models)

- `vertex:gemma` - Lightweight open text model for generation, summarization, and extraction
- `vertex:codegemma` - Lightweight code generation and completion model
- `vertex:paligemma` - Lightweight vision-language model for image tasks

### Embedding Models

- `vertex:textembedding-gecko@001` - Text embeddings (3,072 tokens, 768d)
- `vertex:textembedding-gecko@002` - Text embeddings (2,048 tokens, 768d)
- `vertex:textembedding-gecko@003` - Text embeddings (2,048 tokens, 768d)
- `vertex:text-embedding-004` - Text embeddings (2,048 tokens, ≤768d)
- `vertex:text-embedding-005` - Text embeddings (2,048 tokens, ≤768d)
- `vertex:textembedding-gecko-multilingual@001` - Multilingual embeddings (2,048 tokens, 768d)
- `vertex:text-multilingual-embedding-002` - Multilingual embeddings (2,048 tokens, ≤768d)
- `vertex:multimodalembedding` - Multimodal embeddings for text, image, and video

### Image Generation Models

Imagen models are available through [Google AI Studio](https://console.cloud.google.com/aiplatform/generativeai) using the `google:image:` prefix.

## Model Capabilities

### Gemini 2.0 Pro Specifications

- Max input tokens: 2,097,152
- Max output tokens: 8,192
- Training data: Up to June 2024
- Supports: Text, code, images, audio, video, PDF inputs
- Features: System instructions, JSON support, grounding with Google Search

### Language Support

Gemini models support a wide range of languages including:

- Core languages: Arabic, Bengali, Chinese (simplified/traditional), English, French, German, Hindi, Indonesian, Italian, Japanese, Korean, Portuguese, Russian, Spanish, Thai, Turkish, Vietnamese
- Gemini 1.5 adds support for 50+ additional languages including regional and less common languages

If you're using Google AI Studio directly, see the `google` provider documentation instead.

## Setup and Authentication

### 1. Install Dependencies

Install Google's official auth client:

```sh
npm install google-auth-library
```

### 2. Enable API Access

1. Enable the [Vertex AI API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com) in your Google Cloud project
2. For Claude models, request access through the [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/publishers) by:
   - Navigating to "Model Garden"
   - Searching for "Claude"
   - Clicking "Enable" on the specific Claude models you want to use
3. Set your project in gcloud CLI:

```sh
gcloud config set project PROJECT_ID
gcloud auth application-default login
```

### 3. Authentication Methods

Choose one of these authentication methods:

#### Option 1: Application Default Credentials (Recommended)

This is the most secure and flexible approach for development and production:

```sh
# First, authenticate with Google Cloud
gcloud auth login
# Then, set up application default credentials
gcloud auth application-default login
# Set your project ID
export VERTEX_PROJECT_ID=your-project-id
```

#### Option 2: Service Account (Production)

For production environments or CI/CD pipelines:

```sh
# Create a service account in your Google Cloud project
gcloud auth login
# Download the credentials JSON file
gcloud auth application-default login
# or use GEMINI_API_KEY
export GEMINI_API_KEY=$(gcloud auth print-access-token)
export GOOGLE_APPLICATION_CREDENTIALS=${secrets.GCP_CREDENTIALS}
```

#### Option 3: Service Account via Config (Alternative)

You can also provide service account credentials directly in your configuration:

```yaml
providers:
  - id: vertex:gemini-3-5-sonnet-v2@20241022
    config:
      region: us-east5 # Claude models require specific regions
      region: us-east5 # or europe-west1
      region: us-central1 # Vertex AI models are available in this region
      region: europe-west1 # or asia-southeast1
      region: asia-southeast1
      region: us-central1 # or europe-west1
      region: asia-southeast1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1
      region: asia-southeast1
      region: us-central1
      region: europe-west1