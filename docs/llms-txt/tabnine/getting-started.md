# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/getting-started.md

# Getting Started

### What is Tabnine CLI?

Tabnine CLI is an AI-powered coding assistant that runs directly in your terminal. It combines advanced AI models with intelligent code understanding to help you write, understand, and improve code faster.

### What Can Tabnine CLI Do?

#### 💬 Interactive Conversations

Ask questions and get intelligent answers about your code:

```
> What does this function do in @src/auth.ts?

> How can I improve the error handling in @utils/validator.js?

> Explain the authentication flow in this codebase
```

#### 📝 Code Analysis and Review

Get comprehensive code reviews with actionable feedback:

```
> Review @src/api/users.ts and suggest improvements

> Check @src/services/ for security vulnerabilities

> Analyze the performance of @database/queries.ts
```

#### ✍️ Code Generation and Editing

Generate new code or modify existing files:

```
> Create a REST API endpoint for user registration

> Add error handling to all functions in @src/utils/

> Refactor @src/payment.ts to use async/await
```

#### 🔍 Powerful Code Search

**Remote Code Search** - Search across massive codebases:

```
> Find all functions that handle authentication

> Where is the database connection configured?

> Show all API endpoints that use JWT tokens
```

#### 🎓 Learn Best Practices

**Coaching Guidelines** - Get AI-powered guidance:

```
> What are the best practices for error handling in Node.js?

> How should I structure my API endpoints?

> Review my code against security best practices
```

#### 🛠️ File Operations

Work with files naturally:

```
> Read @package.json and list the main dependencies

> Create a new file README.md with project documentation

> Search for "TODO" comments in @src/
```

### Key Features

#### Terminal-Native Experience

* **Interactive Mode**: Full-featured chat interface
* **Non-Interactive Mode**: Perfect for scripts and automation
* **Keyboard Shortcuts**: Efficient navigation
* **Rich Output**: Syntax highlighting and formatted code

#### Smart Context Understanding

Tabnine CLI automatically understands your:

* **Current working directory**
* **File structure**
* **Code conventions**
* **Project context**

#### Powerful Built-in Tools

* **File Operations** - Read, write, search files
* **Shell Commands** - Execute commands safely
* **Remote Code Search** - Search large codebases using cloud indexing
* **Coaching Guidelines** - AI-powered best practices
* **Code Analysis** - Deep understanding of your code

#### Enterprise-Ready

* **Proxy Support** - Works behind corporate firewalls
* **Custom Certificates** - Supports custom CA certificates
* **Secure Authentication** - OAuth-based authentication
* **Privacy** - Your code stays secure

### How It Works

```
┌─────────────────┐
│  You ask a      │
│  question       │
└────────┬────────┘
         ↓
┌─────────────────┐
│  Tabnine CLI    │
│  gathers context│
└────────┬────────┘
         ↓
┌─────────────────┐
│  AI analyzes    │
│  with context   │
└────────┬────────┘
         ↓
┌─────────────────┐
│  Tools execute  │
│  as needed      │
└────────┬────────┘
         ↓
┌─────────────────┐
│  Results shown  │
│  in terminal    │
└─────────────────┘
```

### Common Use Cases

#### Development Workflow

**Code Review**

```
> Review the changes in @src/auth.ts and suggest improvements
```

**Bug Fixing**

```
> I'm getting a TypeError in @src/server.ts line 45. Help me fix it
```

**Refactoring**

```
> Refactor @src/utils.ts to be more maintainable
```

**Documentation**

```
> Generate JSDoc comments for all functions in @src/api/
```

#### Learning and Exploration

**Understand Code**

```
> Explain how the authentication system works in this project
```

**Learn Patterns**

```
> Show me the best way to implement pagination in REST APIs
```

**Troubleshoot**

```
> Why am I getting a CORS error when calling the API?
```

#### Automation

**CI/CD Integration**

```bash
tabnine -p "Review the code changes" --output-format json
```

**Batch Processing**

```bash
tabnine -p "Add type annotations to all TypeScript files in src/"
```

### Interface Overview

When you start Tabnine CLI, you'll see:

```
┌─────────────────────────────────────────────┐
│  Tabnine CLI                                │  ← Header
│  Model: gpt-4o | Dir: /my/project           │
├─────────────────────────────────────────────┤
│                                             │
│  AI: How can I help you today?              │  ← Conversation
│                                             │
│  You: What files are in this directory?     │
│                                             │
│  AI: [Using list_directory tool...]         │
│  The current directory contains...          │
│                                             │
├─────────────────────────────────────────────┤
│  > █                                        │  ← Input
├─────────────────────────────────────────────┤
│  Type /help for commands                    │  ← Footer
└─────────────────────────────────────────────┘
```

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FU04i5mrHYzNrAsmDdODZ%2FTabnine%20CLI%20screen%201.png?alt=media&#x26;token=c224a586-4e4b-473f-98a3-db8f99912ae3" alt=""><figcaption><p>This screenshot shows the header, conversation area, input area, and footer</p></figcaption></figure>
