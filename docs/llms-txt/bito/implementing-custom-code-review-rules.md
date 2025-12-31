# Source: https://docs.bito.ai/ai-code-reviews-in-git/implementing-custom-code-review-rules.md

# Implementing custom code review rules

Bito’s [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) offers a flexible solution for teams looking to enforce custom code review rules, standards, and guidelines tailored to their unique development practices. Whether your team follows specific coding conventions or industry best practices, you can customize the Agent to suite your needs.

We support three ways to customize AI Code Review Agent’s suggestions:&#x20;

1. [**Provide feedback on Bito-reported issues in pull requests**](#id-1-provide-feedback-on-bito-reported-issues), and the AI Code Review Agent automatically adapts by creating code review rules to prevent similar suggestions in the future.
2. [**Create custom code review guidelines via the dashboard**](#id-2-create-custom-code-review-guidelines). Define rules through the [**Custom Guidelines**](https://alpha.bito.ai/home/ai-agents/custom-guidelines) dashboard in Bito Cloud and apply them to agent instances in your workspace.
3. [**Use project-specific guideline files**](#id-3-use-project-specific-guideline-files). Add guideline files (like `.cursor/rules/*.mdc`, `.windsurf/rules/*.md`, `CLAUDE.md`, `GEMINI.md`, or `AGENTS.md`) to your repository, and the AI Code Review Agent automatically uses them during pull request reviews to provide feedback aligned with your project's standards.

## 1- Provide feedback on Bito-reported issues

AI Code Review Agent refines its suggestions based on your feedback. When you **provide negative feedback on Bito-reported issues in pull requests**, the Agent automatically adapts by creating **custom code review rules** to prevent similar suggestions in the future.

Depending on your Git platform, you can provide negative feedback in the following ways:

* **GitHub:** Select the checkbox given in feedback question at the end of each Bito suggestion or leave a negative comment explaining the issue with the suggestion.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FREsLjCbSETT4ng9V2urf%2Fscrnli_uijoVDl73Faal3.png?alt=media&#x26;token=b3f6ab0e-d06f-435c-9411-2784fe3b4eb8" alt=""><figcaption></figcaption></figure>

* **GitLab:** React with negative emojis (e.g., thumbs down) or leave a negative comment explaining the issue with the suggestion.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FIwUQHSeKUQoOMG2Hkuc5%2Fscrnli_T3dqxb73IGQCQX.png?alt=media&#x26;token=55faaf4d-8257-45c5-9a9e-a58598d438a4" alt=""><figcaption></figcaption></figure>

* **Bitbucket:** Provide manual review feedback by leaving a negative comment explaining the issue with the suggestion.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FRagYwO9GOvrNWOkcvAAY%2Fscrnli_1JWWOjCcvIVHRc.png?alt=media&#x26;token=83cd24a6-32eb-4b83-8b6e-3fcc704f0c86" alt="" width="563"><figcaption></figcaption></figure>

The **custom code review rules** are displayed on the [**Learned Rules**](https://alpha.bito.ai/home/ai-agents/review-rules) dashboard in Bito Cloud.

These rules are applied at the repository level for the specific programming language.

By default, newly generated custom code review rules are disabled. Once negative feedback for a specific rule reaches a threshold of 3, the rule is automatically enabled. You can also manually enable or disable these rules at any time using the toggle button in the **Status** column.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F5nhsxVcDUiGQB7BG2ubh%2Fscrnli_RSAeHezIwIR9Ja.png?alt=media&#x26;token=c026270e-d340-4feb-b648-7fed0e090aa8" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** Providing a positive reaction emoji or comment has no effect and will not generate a new code review rule.
{% endhint %}

After you provide negative feedback, Bito generates a new code review rule in your workspace. The next time the AI Code Review Agent reviews your pull requests, it will automatically filter out the unwanted suggestions.

## 2- **Create custom code review guidelines**

We understand that different development teams have unique needs. To accommodate these needs, we offer the ability to implement **custom code review guidelines** in Bito’s [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git).

Once you add guidelines, the agent will follow them when reviewing pull requests. You can manage guidelines (create, apply, and edit) entirely in the dashboard.

By enabling custom code review guidelines, Bito helps your team maintain consistency and improve code quality.

{% hint style="info" %}
**Note:** Custom review guidelines are available only on the [**Enterprise Plan**](https://bito.ai/pricing/). Enabling them also upgrades your workspace to the **Enterprise Plan**.
\
[**Visit pricing page**](https://bito.ai/pricing/)
{% endhint %}

### How to add a guideline

#### Step 1: Open the **Custom Guidelines** tab

* Sign in to [Bito Cloud](https://alpha.bito.ai/).
* Click [Custom Guidelines](https://alpha.bito.ai/home/ai-agents/custom-guidelines) in the sidebar.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FWyaHHs2jeqqtciaNwnlf%2Fscrnli_89a02mkxIZwF1j.png?alt=media&#x26;token=2b3ecd82-91b4-44ac-874a-be700e4c5a61" alt=""><figcaption></figcaption></figure>

#### Step 2: Fill the form

**A. Manual setup**

1. Click **Add guidelines** button from the top right.
2. Fill out:
   * **Guideline name**
   * **Language** (select a specific programming language or select **General** if the guideline applies to all languages)
   * **Custom Guidelines and Rules** (enter your guidelines here)
3. Click **Create guideline**.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fkf8i8x3CAOFr0DDxkoLY%2Fscrnli_pL9L6X0q4ZzoQu.png?alt=media&#x26;token=e6542c5b-c121-422e-b9a5-6c2fd1ecbb35" alt="" width="563"><figcaption></figcaption></figure>

**B. Use a Template**

1. Click **Add guidelines** button from the top right.
2. Choose a template from the **Use template** dropdown menu.
3. Review/edit fields as needed.
4. Click **Create guideline**.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FuXpSbSVzVbvHpME4HQJT%2Fscrnli_VbfcVt9RI01jRh.png?alt=media&#x26;token=a2997a4e-22d7-4c16-9c37-54548aff0416" alt="" width="563"><figcaption></figcaption></figure>

#### Step 3: Apply to an Agent

* After creating a guideline, you’ll see an **Apply review guideline** dropdown.
* Select the **Agent instance**, then click **Manage review guidelines** to open its settings.

{% hint style="info" %}
**To apply the guideline later:** go to [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent), find the Agent instance, click **Settings**, and manage guidelines there.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FikJjSQFsqVVgbk1X4lrF%2Fscrnli_Hrlv93i7v03AvS.png?alt=media&#x26;token=48612ba8-2db3-485e-ba91-7b52182746fb" alt="" width="563"><figcaption></figcaption></figure>

#### Step 4: Save configuration

On the Agent settings page, hit **Save** (top-right) to apply guideline changes.

{% hint style="info" %}
**Note:** Visit the [**Custom Guidelines**](https://alpha.bito.ai/home/ai-agents/custom-guidelines) tab to edit or delete any guideline.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fnn3bFOYEfxzxUJxoDwRA%2Fscrnli_K7jwJZpHs15W6R.png?alt=media&#x26;token=ec0ade53-1f64-4128-8008-263a7e765479" alt=""><figcaption></figcaption></figure>

### Managing review guidelines from agent settings

Efficiently control which custom guidelines apply to your AI Code Review Agent through the Agent settings interface.

1. Go to [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) dashboard from the Bito Cloud sidebar.
2. Click **Settings** next to the target agent instance.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FNpRzcdMJCARZJGr6zsfu%2Fscrnli_7EzY56dyc0u017.png?alt=media&#x26;token=3a96a9b3-695f-4662-8e2e-dce3731020c9" alt=""><figcaption></figcaption></figure>

3. Navigate to the **Custom Guidelines** section. Here you can either create a new guideline or select from existing guidelines.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FjMyWG2I1k48LEV9gjqjr%2Fscrnli_oktJf4u3e0VkU0.png?alt=media&#x26;token=ccb1a18f-1d77-463c-8996-a6e1bb611f9d" alt=""><figcaption></figcaption></figure>

3. **Create a new guideline**
   * If you click **Create a new guideline** button, you will see the same form as mentioned earlier where you can enter the details to create a review guideline.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FvTHf5T3XDheW0tEU8iM4%2Fscrnli_IOT11izz4107ka.png?alt=media&#x26;token=19f2da6f-f7e5-4fd9-a274-bf7ee6d1671d" alt=""><figcaption></figcaption></figure>

4. **Or select an existing guideline**
   * If you click **Select from existing guidelines** button, you will get a popup screen from where you can select from a list review guidelines you already created. Use checkboxes to enable or disable each guideline for the selected agent and then click **Add selected**.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FpSCt7YJ81pd4W7n4H5Od%2Fscrnli_3JcRnxBHQ135wD.png?alt=media&#x26;token=aa2a8893-4e2f-44ff-9a66-5f960e8ec202" alt=""><figcaption></figcaption></figure>

5. Once you’ve applied or adjusted guidelines, click the **Save** button in the top-right corner to confirm changes.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Ftm0jWnSPBLc49zA8FhGL%2Fscrnli_K7jwJZpHs15W6R.png?alt=media&#x26;token=4c5a3503-71a0-48ab-9bad-f805f39bd43a" alt=""><figcaption></figcaption></figure>

### FAQs

#### What types of custom code review guidelines can be implemented?

You can implement a wide range of custom code review guidelines, including:&#x20;

* Style and formatting guidelines&#x20;
* Security best practices&#x20;
* Performance optimization checks&#x20;
* Code complexity and maintainability standards
* etc.

#### Is "custom code review guidelines" feature available in Team Plan?

No, this feature is available exclusively on the [**Enterprise Plan**](https://bito.ai/pricing/). Enabling the **"custom code review guidelines"** feature also upgrades your workspace to the **Enterprise Plan**.

For more details on **Enterprise Plan**, visit our [**Pricing Page**](https://bito.ai/pricing/).

## 3- Use project-specific guideline files

The AI Code Review Agent can read guideline files directly from your repository and use them during code reviews. These are the same guideline files that AI coding assistants (like Cursor, Windsurf, and Claude Code) use to help developers write code.

By adding these files to your repository, the agent automatically follows your project's specific coding standards, architecture patterns, and best practices when reviewing pull requests.

### Supported guideline files

The AI Code Review Agent currently supports analyzing the following guideline files that are commonly used by different AI coding agents:

CRA currently supports analyzing the following guideline files that are commonly used by different AI coding agents:

| `.cursor/rules/*.mdc`  | Cursor IDE               |
| ---------------------- | ------------------------ |
| `.windsurf/rules/*.md` | Windsurf IDE             |
| `CLAUDE.md`            | Claude Code              |
| `GEMINI.md`            | Gemini CLI               |
| `AGENTS.md`            | OpenAI CodeX, Cursor IDE |

### How to organize your guideline files

**Multiple files in one directory**

You can split your guidelines across multiple files:

```
.cursor/rules/project-overview.mdc
.cursor/rules/architecture-principles.mdc
.cursor/rules/security-standards.mdc
```

For Windsurf, use the `.md` extension:

```
.windsurf/rules/coding-standards.md
.windsurf/rules/api-patterns.md
```

**Module-specific guidelines:**

Place guideline files in subdirectories to create rules for specific parts of your codebase:

```
.cursor/rules/global-standards.mdc
providers/.cursor/rules/provider-implementation.mdc
auth/.cursor/rules/authentication-rules.mdc
```

The agent finds all relevant guideline files based on which files changed in your pull request.

{% hint style="info" %}
**Note:** Rule precedence (where subdirectory rules override parent-level rules) will be added in a future release. Currently, the agent considers all applicable guideline files equally.
{% endhint %}

### How citations work

Every relevant Bito comment includes a **Citations** section that links to the specific guideline that triggered the comment. The link takes you directly to the relevant line in your guideline file, making it easy to verify the feedback and understand why it was given.

### Example scenario

Let's say you're building an application that integrates multiple LLM providers. Your guideline file specifies:

* All providers must extend the `BaseLLMProvider` class
* All providers must implement standard methods like `generateResponse()` and `streamResponse()`
* New providers must be registered in the `config/providers.json` file

When someone submits a pull request to add a new provider, the agent can catch issues like:

* The new provider doesn't extend the base class
* Required methods are missing
* The provider wasn't added to the configuration file

Each comment links back to the specific guideline, so the developer knows exactly what needs to be fixed.

### Sample guideline file

Here's an example `AGENT.md` file to help you get started:

{% code expandable="true" %}

````markdown
# LLM Proxy Architecture & Design Document

## Document Overview

### Purpose
This document serves as a coding guideline and technical reference for AI agents working with this codebase. It provides comprehensive information about the current architecture, design patterns, implementation details, and the rationale behind design decisions. AI agents should use this document to understand the existing code structure, maintain consistency when making modifications, and follow established patterns when extending functionality.

### What This Document Covers
- **System Architecture**: High-level overview of components and their interactions
- **Design Patterns**: Detailed explanation of the Factory Pattern implementation
- **Component Design**: In-depth analysis of each system component
- **Data Flow**: Request/response lifecycle through the system
- **Design Decisions**: Rationale behind current architectural choices
- **Implementation Details**: Code structure, conventions, and patterns in use

---

## Table of Contents
1. [System Architecture](#system-architecture)
2. [Design Patterns](#design-patterns)
3. [Component Design](#component-design)
4. [Data Flow](#data-flow)
5. [Design Decisions](#design-decisions)
6. [Error Handling Strategy](#error-handling-strategy)
7. [Security Considerations](#security-considerations)
8. [Coding Conventions](#coding-conventions)

---

## System Architecture

### High-Level Overview

The LLM Proxy application follows a layered architecture with clear separation between the presentation layer (FastAPI), business logic layer (Provider implementations), and integration layer (external LLM APIs).

```
┌─────────────────────────────────────────────┐
│           FastAPI Application               │
│         (Presentation Layer)                │
│   - Request validation (Pydantic)           │
│   - Route handling (/chat endpoint)         │
│   - Response formatting                     │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│          Provider Factory                   │
│        (Abstraction Layer)                  │
│   - Provider selection logic                │
│   - Instance creation                       │
└────────────────┬────────────────────────────┘
                 │
        ┌────────┴────────┐
        ▼                 ▼
┌──────────────┐   ┌──────────────┐
│   OpenAI     │   │  Anthropic   │
│   Provider   │   │   Provider   │
│              │   │              │
│ (Concrete    │   │ (Concrete    │
│  Impl.)      │   │  Impl.)      │
└──────┬───────┘   └──────┬───────┘
       │                  │
       ▼                  ▼
┌──────────────┐   ┌──────────────┐
│  OpenAI API  │   │ Anthropic API│
└──────────────┘   └──────────────┘
```

### Component Layers

1. **Presentation Layer** (`main.py`)
   - Handles HTTP requests/responses
   - Validates input using Pydantic models
   - Manages API endpoints

2. **Abstraction Layer** (`providers/factory.py`)
   - Implements Factory Pattern
   - Routes requests to appropriate providers
   - Decouples client code from concrete implementations

3. **Business Logic Layer** (`providers/*.py`)
   - Abstract base class defines contract
   - Concrete providers implement LLM-specific logic
   - Handles API communication and response parsing

4. **Integration Layer**
   - External API calls via httpx
   - Authentication management
   - Network error handling

---

## Design Patterns

### Factory Design Pattern

The application implements the **Factory Design Pattern** to create provider instances without exposing creation logic to the client.

#### Pattern Components

1. **Abstract Product** (`LLMProvider`)
```python
class LLMProvider(ABC):
    def __init__(self, model: str):
        self.model = model
    
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass
```

**Purpose**: Defines the contract that all concrete providers must implement.

2. **Concrete Products** (`OpenAIProvider`, `AnthropicProvider`)
```python
class OpenAIProvider(LLMProvider):
    def generate_response(self, prompt: str) -> str:
        # OpenAI-specific implementation
        pass
```

**Purpose**: Implement provider-specific logic while adhering to the base contract.

3. **Factory** (`ProviderFactory`)
```python
class ProviderFactory:
    @staticmethod
    def get_provider(provider_name: str, model: str) -> LLMProvider:
        providers = {
            "openai": OpenAIProvider,
            "anthropic": AnthropicProvider
        }
        return providers[provider_name.lower()](model)
```

**Purpose**: Encapsulates provider instantiation logic.

#### Benefits of This Pattern

- **Loose Coupling**: Client code depends on abstractions, not concrete classes
- **Open/Closed Principle**: Open for extension (new providers), closed for modification
- **Single Responsibility**: Each provider handles only its specific implementation
- **Testability**: Easy to mock providers for testing
- **Scalability**: Adding new providers requires minimal changes

---

## Component Design

### 1. Base Provider (`providers/base.py`)

**Responsibility**: Define the contract for all LLM providers

**Key Design Decisions**:
- Uses ABC (Abstract Base Class) to enforce implementation
- Stores model name as instance variable for reuse
- Single abstract method keeps interface simple

**Design Rationale**:
- Python's ABC ensures compile-time checking of implementations
- Simple interface reduces cognitive load for implementers
- Storing model allows for provider-specific model validation in future

### 2. OpenAI Provider (`providers/openai_provider.py`)

**Responsibility**: Implement OpenAI Chat Completions API integration

**Key Features**:
- Environment-based API key management
- Message format conversion (user prompt → OpenAI format)
- Response parsing (extract content from choices)
- Timeout handling (30 seconds)

**API Contract**:
```
POST https://api.openai.com/v1/chat/completions
Headers: Authorization: Bearer <key>
Body: {
  "model": "gpt-4",
  "messages": [{"role": "user", "content": "prompt"}]
}
```

**Error Handling**:
- Validates API key presence on initialization
- Catches HTTP errors and wraps with descriptive messages
- Re-raises exceptions for upstream handling

### 3. Anthropic Provider (`providers/anthropic_provider.py`)

**Responsibility**: Implement Anthropic Messages API integration

**Key Features**:
- Custom header format (x-api-key, anthropic-version)
- Max tokens configuration (1024)
- Content array response parsing

**API Contract**:
```
POST https://api.anthropic.com/v1/messages
Headers: 
  x-api-key: <key>
  anthropic-version: 2023-06-01
Body: {
  "model": "claude-3-sonnet",
  "max_tokens": 1024,
  "messages": [{"role": "user", "content": "prompt"}]
}
```

**Design Choices**:
- Hard-coded max_tokens provides consistent behavior
- Version header ensures API stability
- Array access for content assumes single response

### 4. Provider Factory (`providers/factory.py`)

**Responsibility**: Create provider instances based on string identifiers

**Implementation Strategy**:
- Dictionary-based mapping for O(1) lookup
- Case-insensitive provider names
- Descriptive error messages for invalid providers

**Extensibility**:
```python
# Adding new provider:
providers = {
    "openai": OpenAIProvider,
    "anthropic": AnthropicProvider,
    "deepseek": DeepseekProvider,  # Just add here
}
```

### 5. FastAPI Application (`main.py`)

**Responsibility**: HTTP interface and request orchestration

**Key Components**:

1. **Request Model**:
```python
class ChatRequest(BaseModel):
    provider: str
    model: str
    prompt: str
```
- Leverages Pydantic for automatic validation
- Clear field names match user expectations

2. **Response Model**:
```python
class ChatResponse(BaseModel):
    provider: str
    model: str
    response: str
```
- Echoes input parameters for traceability
- Returns plain text response

3. **Endpoint Handler**:
```python
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    provider = ProviderFactory.get_provider(request.provider, request.model)
    response_text = provider.generate_response(request.prompt)
    return ChatResponse(...)
```

**Error Mapping**:
- `ValueError` (invalid provider) → HTTP 400
- Generic `Exception` (API errors) → HTTP 500

---

## Data Flow

### Request Lifecycle

```
1. Client sends POST /chat
   ↓
2. FastAPI receives request
   ↓
3. Pydantic validates request body
   ↓
4. ProviderFactory.get_provider() called
   ↓
5. Factory returns concrete provider instance
   ↓
6. provider.generate_response() called
   ↓
7. Provider makes HTTP call to LLM API
   ↓
8. Provider parses response
   ↓
9. Response wrapped in ChatResponse model
   ↓
10. JSON response sent to client
```

### Detailed Flow Example (OpenAI)

```python
# Client Request
POST /chat
{
  "provider": "openai",
  "model": "gpt-4",
  "prompt": "Tell me a joke"
}

# Internal Processing
1. Pydantic validates: ChatRequest object created
2. Factory called: ProviderFactory.get_provider("openai", "gpt-4")
3. OpenAIProvider instantiated with model="gpt-4"
4. generate_response("Tell me a joke") called
5. HTTP POST to OpenAI API:
   {
     "model": "gpt-4",
     "messages": [{"role": "user", "content": "Tell me a joke"}]
   }
6. OpenAI responds with completion
7. Extract: data["choices"][0]["message"]["content"]
8. Return text to endpoint
9. Wrap in ChatResponse

# Client Response
{
  "provider": "openai",
  "model": "gpt-4",
  "response": "Why did the chicken cross the road?..."
}
```

---

## Design Decisions

### 1. Why Factory Pattern?

**Decision**: Use Factory Pattern instead of simple if/else logic

**Rationale**:
- **Scalability**: Adding providers doesn't require modifying existing code
- **Testability**: Easy to mock factory for unit tests
- **Maintainability**: Provider logic isolated in separate classes
- **Professional Standard**: Industry-recognized pattern for this use case

**Alternative Considered**: Direct instantiation with if/else
```python
# Rejected approach
if provider == "openai":
    result = OpenAIProvider(model).generate_response(prompt)
elif provider == "anthropic":
    result = AnthropicProvider(model).generate_response(prompt)
```
**Why Rejected**: Violates Open/Closed Principle, harder to extend

### 2. Why httpx Over Official SDKs?

**Decision**: Use httpx for HTTP calls instead of official provider SDKs

**Rationale**:
- **Minimal Dependencies**: Keeps requirements.txt small
- **Unified Interface**: Single HTTP client for all providers
- **Transparency**: Direct API calls are easier to debug
- **Control**: Full control over request/response handling

**Trade-offs**:
- Less abstraction (must handle response parsing)
- No built-in retry logic
- Manual API version management

### 3. Synchronous vs Asynchronous

**Decision**: Use synchronous HTTP calls with httpx.Client

**Rationale**:
- **Simplicity**: Easier to understand and debug
- **Current Scale**: Single request doesn't benefit from async
- **API Constraints**: LLM APIs are inherently blocking

**Future Consideration**: Switch to async if supporting streaming responses

### 4. Error Handling Strategy

**Decision**: Simple try/except with HTTP status code mapping

**Rationale**:
- **Simplicity**: Requirements specified basic error handling
- **Client Clarity**: HTTP status codes are standard
- **Debugging**: Error messages preserved in exceptions

**Not Included** (but recommended for production):
- Structured logging
- Retry logic
- Rate limiting
- Circuit breakers

### 5. Environment Variables for API Keys

**Decision**: Use environment variables instead of configuration files

**Rationale**:
- **Security**: Prevents accidental commit of credentials
- **12-Factor App**: Follows best practices for configuration
- **Flexibility**: Easy to change without code modification
- **Cloud-Ready**: Works seamlessly with container orchestration


---

## Error Handling Strategy

### Current Implementation

```python
try:
    provider = ProviderFactory.get_provider(request.provider, request.model)
    response_text = provider.generate_response(request.prompt)
    return ChatResponse(...)
except ValueError as e:
    # Invalid provider name
    raise HTTPException(status_code=400, detail=str(e))
except Exception as e:
    # API errors, network issues, etc.
    raise HTTPException(status_code=500, detail=str(e))
```

### Error Categories

1. **Client Errors (400)**:
   - Invalid provider name
   - Unsupported model
   - Malformed request

2. **Server Errors (500)**:
   - Missing API keys
   - Network timeouts
   - API errors (rate limits, service unavailable)
   - Response parsing failures


---

## Security Considerations

### Current Implementation

1. **API Key Management**:
   - Stored in environment variables
   - Never logged or returned in responses
   - Validated on provider initialization

2. **Request Validation**:
   - Pydantic models enforce type safety
   - No SQL injection risk (no database)
   - No command injection (no shell execution)

### Current Limitations

1. **No Rate Limiting**: The application does not implement rate limiting
2. **No Authentication**: Endpoints are publicly accessible
3. **No Input Sanitization**: Prompt length and content are not validated beyond Pydantic type checking
4. **No Retry Logic**: Failed API calls are not automatically retried

---

## Coding Conventions

### File Organization

**Current Structure**:
```
llm-proxy/
├── main.py                      # FastAPI application entry point
├── providers/                   # Provider package
│   ├── __init__.py             # Package exports
│   ├── base.py                 # Abstract base class
│   ├── openai_provider.py      # OpenAI implementation
│   ├── anthropic_provider.py   # Anthropic implementation
│   └── factory.py              # Factory implementation
├── requirements.txt             # Python dependencies
├── .env.example                # Environment variable template
└── README.md                   # User documentation
```

### Naming Conventions

1. **Classes**: PascalCase (e.g., `LLMProvider`, `OpenAIProvider`)
2. **Functions/Methods**: snake_case (e.g., `generate_response`, `get_provider`)
3. **Constants**: UPPER_SNAKE_CASE (e.g., `OPENAI_API_KEY`)
4. **Files**: snake_case (e.g., `openai_provider.py`)

### Code Patterns

1. **Provider Implementation**:
   - Inherit from `LLMProvider`
   - Validate API key in `__init__`
   - Implement `generate_response(prompt: str) -> str`
   - Use httpx.Client with 30-second timeout
   - Wrap errors with descriptive messages

2. **Error Handling**:
   - Use `try/except` blocks in provider implementations
   - Raise `ValueError` for missing API keys
   - Raise generic `Exception` with descriptive messages for API errors
   - Let FastAPI endpoint handle HTTP status code mapping

3. **Environment Variables**:
   - Load with `os.getenv()`
   - Validate presence in provider `__init__`
   - Use pattern: `{PROVIDER}_API_KEY`

4. **Type Hints**:
   - All methods should include type hints
   - Use Pydantic models for request/response validation
   - Return type explicitly stated

### Documentation Standards

1. **Docstrings**: All classes and methods include docstrings
2. **Comments**: Inline comments explain non-obvious logic
3. **README**: User-facing documentation with examples

### Dependencies

**Current Dependencies**:
- `fastapi==0.109.0`: Web framework
- `uvicorn[standard]==0.27.0`: ASGI server
- `pydantic==2.5.3`: Data validation
- `httpx==0.26.0`: HTTP client
- `python-dotenv==1.0.0`: Environment variable management

**Rationale**: Minimal, well-maintained dependencies that serve specific purposes.

---

## Summary

This document captures the current state of the LLM Proxy application. When working with this codebase, AI agents should:

1. **Follow the Factory Pattern**: All new providers must inherit from `LLMProvider` and be registered in `ProviderFactory`
2. **Maintain Consistency**: Use the same error handling, timeout values, and code structure as existing providers
3. **Respect Abstractions**: Keep provider-specific logic within provider classes
4. **Update Documentation**: Any changes to architecture should be reflected in this document
5. **Preserve Simplicity**: The design prioritizes simplicity and clarity over advanced features

The architecture demonstrates clean separation of concerns through the Factory Design Pattern, making the codebase maintainable and understandable for both human developers and AI agents.

````

{% endcode %}
