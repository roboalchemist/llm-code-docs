# Source: https://docs.tabnine.com/main/getting-started/context-engine.md

# Context Engine

The Tabnine Context Engine extends your agents’ awareness beyond the local workspace by generating structured context from connected remote repositories.

This guide walks you through setup, configuration, and usage.

## Step 1: Connect Your Repositories

Before using the Context Engine, ensure your repositories are connected to your team.

Once connected:

* Repositories are automatically indexed
* The agent can search, navigate, and list the following: remote repositories, folders, files, and code elements
* Basic context becomes available within a few hours

No additional configuration is required for this initial indexing layer.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FOrzaP2YqdBhNc0ihjfD7%2Funknown.png?alt=media&#x26;token=dbfdd189-6dbf-4594-aa72-b4bc0a5f13f0" alt=""><figcaption></figcaption></figure>

The following IP addresses allow listing should our indexer service on EMT needs to contact a git host in an enterprise environment:

```
35.238.67.206
```

```
34.123.150.41
```

Depending on the port, you’ll have two options:

SSH: `22`\
HTTPS: `443`

***

## Step 2: Enable the Context Engine (Admin Setup)

Navigate to: Admin UI > Context Engine > <mark style="background-color:$tint;">**Settings**</mark>

This step has two required parts: enablement configuration and enabling Context Engine tools

### Configure Context Engine Enablement

In the Context Engine Enablement section:

1. Select the Context Engine Model\
   Choose the model that will be used for repository pre-processing.
2. Select the Context Engine User
3. Must be an admin
4. Must belong to a team with agents enabled
5. The Context Engine runs on behalf of this user (permissions and quota apply)
6. Configure the Pre-Processing Schedule (optional)
7. Any time (default)\
   Controlled (recommended only for organizations using private model endpoints to manage load)<br>

Click <mark style="background-color:$tint;">**Edit Configuration**</mark> (or the relevant save action) to apply changes:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FHiC3s6osbY0cOWdqkFeQ%2Funknown.png?alt=media&#x26;token=69071a45-b789-4ffa-bc2d-2ce057fceb07" alt=""><figcaption></figcaption></figure>

### Enable Context Engine Tools for End Users (Required)

Expand the second tab titled Context Engine Tools Configuration

Next, toggle “Enable Context Engine tools to end users”.

This step is mandatory. Without enabling tools, end users will not be able to access Context Engine capabilities in the IDE or CLI, even if repositories were processed successfully.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FVmp7pSY7Ei5LKhamaduD%2Funknown.png?alt=media&#x26;token=736eee83-7b40-461d-ac8b-e079b890bf3f" alt=""><figcaption></figcaption></figure>

## Step 3: Enable Agentic Pre-Processing Per Repository

Advanced (agentic) context layers are not generated automatically for all repositories.

For each repository:

1. Go to the Personalization page
2. Locate the connected repository
3. Enable agentic context processing using the repository action icon

Repeat for every repository you want processed.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FUPpjhYBlaCHf6OQu4Sa8%2Funknown.png?alt=media&#x26;token=bd7c42d8-34c7-46b9-b6ef-29c80e4584e7" alt=""><figcaption></figcaption></figure>

## Step 4: Review Generated Context Layers

Once advanced processing completes, generated assets can be reviewed.

Navigate to:

Context Engine > Assets

From there, admins can:

* Filter assets by repository, team, or type
* Open and inspect generated context layers

These assets include higher-level summaries, services, dependencies, and structured architectural insights.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FQEishbZY6Rd9jz0J89tg%2Funknown.png?alt=media&#x26;token=32066039-aac6-4617-a58d-c9c517fae08b" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FCHb9YK8FMnE3UEJWQqMk%2Funknown.png?alt=media&#x26;token=c7093fcf-920f-4b83-ae87-3fa44ddd07b1" alt=""><figcaption></figcaption></figure>

## Step 5: Use Remote Context in the Tabnine Agent (IDE or CLI)

When using the Tabnine Agent, remote repository context is accessible through native MCP tools.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FYyulFoqV6gzHZogOA4or%2Funknown.png?alt=media&#x26;token=a60b27d3-2fef-4bf1-88b5-c22a4d4764dd" alt=""><figcaption></figcaption></figure>

#### Example prompts:

```
“List the remote assets for connected repositories”
```

```
“List the connected repositories”
```

By default, the agent prioritizes local workspace context. If you want the agent to explicitly use remote repositories, specify it in your prompt.

For example, instead of:

```
“Do we have an API for managing users?”
```

Use:

```
“Do we have an API for managing users in the remote codebase?”
```

Adding phrases such as “in remote repositories” or “in the remote codebase” directs the agent to use the generated remote context layers.

<br>
