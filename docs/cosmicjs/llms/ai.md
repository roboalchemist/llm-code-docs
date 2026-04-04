# Source: https://www.cosmicjs.com/docs/api/ai.md

# Source: https://www.cosmicjs.com/docs/dashboard/ai.md

# AI

Cosmic offers a suite of features in the dashboard powered by AI to help you build your Cosmic projects faster.

## AI Studio

### Content Model Generation

The AI Studio generates complete content structures from natural language descriptions. Instead of manually configuring fields, relationships, and validation rules, you can describe what you need and receive a fully functional content model with multiple content types, relationships, and demo content to get started fast.

**Content model capabilities:**

- Generate content models for any type of website or application
- Add new content types that integrate with existing structures
- Configure relationships between content types automatically
- Create complex multi-language structures with custom validation

**Working examples:**

- "Create a content model for an e-commerce store with products, collections, and customer reviews"
- "Add an Events content model that relates to my existing blog posts and authors"
- "Set up a portfolio website with projects, skills, and testimonials"

### Content Management

Beyond structure creation, the AI handles content generation and management at scale.

**Content operations:**

- Generate realistic sample content for testing and development
- Bulk update existing content with new fields and metadata
- Maintain consistency across large content datasets
- Apply SEO optimization and structured data automatically

**Practical applications:**

- "Create 10 sample blog posts with realistic content for my existing blog model"
- "Update all product entries to include pricing and availability status"

## Application Development and Deployment

### AI-Powered Code Generation

The Cosmic AI Platform generates production-ready applications using your existing
content structure. Applications are built with modern frameworks and include proper
TypeScript definitions, responsive design, and performance optimizations.

**Supported frameworks:**

- Next.js applications with server-side rendering
- React dashboards and single-page applications
- Astro static sites with modern tooling
- Vue.js progressive web applications

## AI assisted development

Click the "AI chat" button in the top right corner of the Cosmic dashboard to open the AI chat drawer. Use AI chat to learn how to integrate your content into your apps. Available for the admin and developer role.

## Get insights from media

Click the "AI chat" button on any media asset to get summaries and insights from PDFs, spreadsheets, documents, and more. Available for all roles.

## Generate alt text

To generate alt text for an image, go to any image, find the alt text area, and click the "Generate" button. You can also generate alt text for a group of images at once. Available for all roles.

## Generate images

To generate images, open the Media modal, click the "Create" button, and describe the image you want to generate. Available for all roles.

## Generate videos

Create compelling video content using natural language, powered by Google's Veo 3.1 models. Available for all roles.

> Prompt: "Cinematic close-up of raindrops falling on a window at night, city lights blurred in background"

**Key features:**

- **Native audio generation** - Videos include automatically generated audio that matches your scene
- **Two quality tiers** - Fast (30-90s) or Standard (60-180s, premium cinematic quality)
- **Flexible options** - Generate 4, 6, or 8-second videos at 720p or 1080p
- **Image-to-video mode** - Use a reference image as the starting frame for precise control
- **Video extension** - Extend any Veo-generated video to create longer sequences

**How to use:**

1. Navigate to **Media** in your project
2. Click **"Create"** and select **"Video Generation"**
3. Choose **"Veo 3.1 Fast"** or **"Veo 3.1 Standard"**
4. Enter your video prompt
5. (Optional) Add a reference image for image-to-video mode
6. Choose duration and resolution, then click **"Generate"**

Videos are automatically saved to your Media Library with global CDN delivery. See the [AI API documentation](/docs/api/ai#generate-video) for programmatic access.

## Generate audio

Convert any text to natural-sounding speech using OpenAI's text-to-speech models. Perfect for creating audio versions of articles, podcast intros, product descriptions, and more. Available for all roles.

**Key features:**

- **9 natural-sounding voices** - Feminine (nova, shimmer, coral, sage, alloy) and masculine (echo, onyx, fable, ash)
- **Two quality tiers** - Standard (fast, low-latency) or HD (higher quality, 2x cost)
- **Long text support** - Texts over 4,096 characters are automatically chunked and concatenated
- **Instant media library** - Generated audio is saved as MP3 and available via CDN

**How to use:**

1. Navigate to **Media** in your project
2. Click **"Create"** and select **"Audio"**
3. Select a **voice** from the dropdown (default: Nova)
4. Paste or type the text you want to convert to speech
5. Click **"Generate"** to create the audio file

Audio files are automatically saved to your Media Library in MP3 format. See the [AI API documentation](/docs/api/ai#generate-audio) for programmatic access.

## Auto translate content with AI

You can use Cosmic AI to auto translate content from one language to another. Available for all roles.

## Content generation

You can use Cosmic AI to generate content for your projects. Create summaries, SEO optimized content, translations, and more. Available for all roles.

## Agents 

AI Agents are autonomous assistants that work on tasks independently. Agents help you automate content management, application development, and browser-based workflows. For recurring or scheduled execution, use [Workflows](#workflows) to run agents on a schedule.

**Access Requirements**: AI Agents are available to users with **Admin** or **Developer** bucket roles only. Editor and Contributor roles do not have access to these features.

### Agent Types

Cosmic provides three specialized agent types, each designed for specific automation tasks:

#### Content Agent

The Content Agent works directly with your Cosmic CMS to create, update, and manage content at scale. It understands your existing content structure, researches topics via progressive web discovery, and generates perfectly formatted objects that match your schema.

**Capabilities:**
- Generate blog posts, landing pages, and product catalogs
- Create and modify object types with custom metafields
- Progressive web discovery for research-backed content
- Batch operations for bulk content creation
- Auto-publish or human review workflow
- Email notifications on task completion

**Example prompts:**
- "Research the latest AI trends from Hacker News and TechCrunch, then create a 5-part blog series covering each major development"
- "Create a complete product catalog for our new summer collection with 20 products, descriptions, and pricing"

#### Code Agent

The Code Agent connects to your GitHub repository and writes production-ready code autonomously. It discovers relevant files, understands your codebase structure, creates feature branches, commits changes, and opens pull requests.

**Capabilities:**
- Progressive file discovery to understand codebases
- Automatic branch creation and PR submission
- Conflict detection and auto-resolution
- Multi-iteration development with checkpoints
- CMS integration for content-aware features
- Email notifications with commit summaries

**Example prompts:**
- "Build a user notification system with real-time updates, API endpoints, and React components with TypeScript"
- "Create a dynamic landing page that pulls content from our Cosmic CMS with hero section, feature grid, and testimonials"

#### Computer Use Agent

The Computer Use Agent sees and controls browsers exactly like a human. It can fill out forms, record demo videos, download and upload media across platforms, and automate any workflow you can do manually.

**Capabilities:**
- Professional demo video recording with animated cursors
- Cross-platform media transfer and downloads
- AI-powered content extraction from web pages
- Visual navigation with stealth mode
- Screenshot and file operations
- Authenticated browser sessions

**Execution Limits:**
- Each Computer Use Agent execution is limited to **100 steps** (actions) by default
- This limit helps prevent runaway costs and ensures efficient task completion
- The agent automatically stops when the goal is achieved, typically well before reaching the limit
- If your task doesn't complete within 100 steps, consider breaking it into smaller, more focused tasks

**Example prompts:**
- "Record a 2-minute demo video of our new dashboard feature, navigate through the analytics section, and export a report"
- "Download our top-performing video from TikTok, then upload it to YouTube Shorts and Instagram Reels with optimized captions"

### Creating an Agent

1. Navigate to the **AI Agents** page in your bucket
2. Click **"Create Agent"**
3. Choose your agent type (Content, Code, or Computer Use)
4. Describe the task you want the agent to complete
5. (Optional) For content agents, enable Progressive Discovery to crawl web content

**Note**: To run agents on a recurring schedule, create a [Workflow](#workflows) with one or more agent steps and configure a schedule. Workflows support hourly, daily, weekly, and monthly scheduling.

### Event Triggers

Agents can be triggered automatically when content events occur. When enabled, your agent runs automatically whenever selected events happen on matching object types.

**Available Events:**
- **Object Created**: Triggers when a new object is added
- **Object Edited**: Triggers when an existing object is modified
- **Object Deleted**: Triggers when an object is removed
- **Object Published**: Triggers when an object's status changes to published
- **Object Unpublished**: Triggers when a published object is unpublished

**Event Context Data:**

When an event triggers your agent, the following data is automatically included in the prompt context:
- **Event Type**: The action that triggered the agent (created, edited, published, etc.)
- **Object Type**: The content type that was affected
- **Object ID**: The unique identifier of the object
- **Object Title**: The title of the triggered object
- **Object Slug**: The slug of the triggered object
- **Object Status**: Current status (draft, published, etc.)
- **Object Metadata**: All field values from the object

**Using Event Data for Conditional Logic:**

You can reference this event data in your prompt to implement conditional behavior:
```
If the object status is "draft", generate SEO metadata for the content.
If the object is already "published", complete early without changes.
If the object type is "blog-posts" and the title contains "urgent",
prioritize this task and notify the team.

```
**Example Use Cases:**
- Auto-generate social media posts when a blog is published
- Create translations when new content is added
- Update related content when a product price changes
- Send notifications based on specific field values

### Key Features

- **Parallel Execution**: Run multiple agents simultaneously (limits based on your plan)
- **Branch Isolation**: Code agents work on separate Git branches to prevent conflicts
- **Progress Tracking**: Monitor commits, files changed, and real-time status updates
- **Email Notifications**: Receive updates when agents complete their work
- **Pull Request Management**: Agents can create PRs for code review before merging
- **Progressive Discovery**: Content agents can crawl web content to inform their work

### Plan Limits

**Plan-Based Limits** (varies by plan):
- **Free Plan**: 2 agents at a time
- **Paid Plans**: More agents based on your plan (check your plan details)

### Agent Limits by Plan

Agent limits apply at the project level (for standalone projects) or workspace level (for workspace projects):

- **Free Plan**: 3 agents per project (manual only)
- **Builder Plan**: 5 agents per project (with scheduling)
- **Team Plan**: 15 agents per project (with scheduling)
- **Business Plan**: 25 agents per project (with scheduling)
- **Enterprise Plan**: Custom agent limits

**Note**: Scheduled execution is available through [Workflows](#workflows) on paid plans.

### Progressive Discovery

Content Agents can use Progressive Discovery to crawl and analyze web content before generating or updating CMS content. This feature allows agents to:

- Research current trends and topics from specified websites
- Gather real-world examples and data
- Reference actual sources with accurate URLs
- Create content informed by the latest information

To use Progressive Discovery, enable it when creating a content agent and specify the URLs or topics you want the agent to explore.

---

## Workflows 

AI Workflows allow you to chain multiple AI agents together to complete complex operations that previously required entire teams. Define a workflow once, and run it on-demand or on a schedule.

### What Are Workflows?

Workflows orchestrate multiple AI agents (Content, Code, and Computer Use) to execute complex, multi-step operations autonomously. Each step in a workflow passes context to the next—content feeds into code, code deploys, and Computer Use tests and records demos.

### How Workflows Work

1. **Define Your Workflow**: Choose a template or build custom. Chain Content, Code, and Computer Use agents in any sequence. Set triggers—manual, scheduled, or event-driven.

2. **Execute Automatically**: Agents work sequentially or in parallel. Each step passes context to the next, maintaining continuity throughout the workflow.

3. **Monitor in Real-Time**: Watch progress live with step-by-step updates. See token usage, costs, and duration. Pause for approval gates when human review is needed.

4. **Review & Iterate**: Get complete execution summaries. View all created content, code changes, and recordings. Clone successful workflows for future projects.

5. **Rerun Anytime**: Run workflows on-demand or schedule them to run automatically. Your automation runs 24/7 without intervention.

### Workflow Use Cases

#### Full-Stack Product Launch

**Time: 20 minutes vs 2-3 weeks**

Content Agent creates your product catalog, Code Agent builds the storefront, Computer Use Agent tests and records a demo video. Complete e-commerce site, deployed.

**Workflow steps:** Content Generation → Code Development → Deploy & Test

#### Automated Content Optimization

**Schedule: Runs every Monday at 2 AM**

Automatically analyze 500+ articles for outdated content, validate links, capture fresh screenshots, and update flagged articles. Always-fresh content, zero manual work.

**Workflow steps:** Analyze Content → Validate Links → Auto-Update

#### Multi-Market Launch

**Time: 90 minutes vs 16 weeks**

Launch in 12+ markets simultaneously. Localized content, market-specific websites, compliance validation, and demo videos—all running in parallel.

**Workflow steps:** Localize Content → Deploy Sites → Validate Compliance

#### Auto-Documentation

**Trigger: On every deploy**

Code deploys to production, agents analyze changes, test new features, capture demo videos, write documentation, and create sales materials. Docs ship with features.

**Workflow steps:** Analyze Code → Test Features → Generate Docs

### Creating a Workflow

1. Navigate to the **AI Workflows** page in your bucket
2. Click **"Create Workflow"**
3. Add steps by selecting agent types (Content, Code, or Computer Use)
4. Configure each step with specific instructions
5. Set execution order (sequential or parallel)
6. (Optional) Add approval gates for human review
7. (Optional) Set a schedule or trigger for automatic execution

### Workflow Features

- **Sequential or Parallel Execution**: Run steps one after another or simultaneously
- **Context Passing**: Each step receives output from previous steps
- **Approval Gates**: Pause workflow for human review when needed
- **Scheduling**: Run workflows on a schedule (hourly, daily, weekly, monthly)
- **Event Triggers**: Automatically trigger workflows on specific events
- **Real-Time Monitoring**: Watch progress with live updates
- **Execution History**: Review past runs with complete logs and outputs
- **Templates**: Start with pre-built workflow templates for common use cases

### Event-Triggered Workflows

Workflows can be configured to run automatically when content events occur, enabling powerful automation scenarios.

**Available Events:**
- **Object Created**: Run workflow when new content is added
- **Object Edited**: Run workflow when content is modified
- **Object Deleted**: Run workflow when content is removed
- **Object Published**: Run workflow when content goes live
- **Object Unpublished**: Run workflow when content is taken offline

**Event Context Data:**

When an event triggers your workflow, the following data is automatically included in the prompt context for all workflow steps:
- **Event Type**: The action that triggered the workflow
- **Object Type**: The content type that was affected
- **Object ID**: The unique identifier of the object
- **Object Data**: Title, slug, status, locale, and all metadata fields

**Using Event Data for Conditional Logic:**

Each step in your workflow can reference the event data to make decisions:
```
Step 1 (Content Agent):
"If the triggered object's status is 'draft', generate SEO metadata.
 If the object is 'published', create social media posts instead."

Step 2 (Code Agent):
"If the object type is 'products' and the price field changed,
 update the pricing display component."

```
**Example Event-Triggered Workflows:**

**Auto-SEO on Publish:**
```
Trigger: Object Published (blog-posts)
Step 1: Generate meta description and keywords from content
Step 2: Create Open Graph image using AI image generation
Step 3: Update object with SEO metadata

```
**Content Localization Pipeline:**
```
Trigger: Object Created (articles)
Step 1: If locale is 'en-US', translate to Spanish, French, German
Step 2: Create localized versions as new objects
Step 3: Send notification with translation summary

```
**Product Update Automation:**
```
Trigger: Object Edited (products)
Step 1: If price changed, update all related promotional content
Step 2: Regenerate product comparison charts
Step 3: Notify sales team via email

```
### Workflow Examples

**Research-to-Publication Pipeline:**
```
Step 1 (Content Agent): Research topic from specified sources
Step 2 (Content Agent): Write article draft with citations
Step 3 (Code Agent): Create landing page for article
Step 4 (Computer Use Agent): Record demo video and screenshots
Step 5 (Content Agent): Publish with all media assets

```
**Code Review and Documentation:**
```
Step 1 (Code Agent): Implement feature from requirements
Step 2 (Code Agent): Write unit tests
Step 3 (Computer Use Agent): Test in browser and record demo
Step 4 (Content Agent): Generate documentation from code changes
Step 5 (Code Agent): Open PR with docs and demo video

```
### Best Practices

- **Start Simple**: Begin with 2-3 step workflows and add complexity as needed
- **Use Approval Gates**: Add human review steps for critical operations
- **Test First**: Run workflows manually before scheduling
- **Monitor Costs**: Watch token usage across workflow steps
- **Clone Successful Workflows**: Reuse working workflows as templates for new projects

---

## Execution Retention 

Agent and workflow executions are automatically cleaned up after a retention period to manage storage and keep your dashboard performant.

### Retention Policy

- **Retention Period**: 90 days
- **Affected Executions**: Completed, failed, and cancelled executions
- **Protected Executions**: Running and active executions are never automatically deleted

### What Gets Deleted

When an execution exceeds the retention period, the following data is removed:
- Execution logs and message history
- Step-by-step results and outputs
- Token usage records for that execution
- Associated metadata (commits, file changes for code agents)

### What's Preserved

- **Agent and Workflow configurations** are never deleted by retention policies
- **Running executions** remain until they complete
- **Content created by agents** (CMS objects, media) persists independently
- **Code changes** committed to your repository remain in Git history
- **Pull requests** created by code agents remain in GitHub

### Best Practices

- Export important execution logs before the 90-day retention period if you need long-term records
- Use the execution detail view to review results while they're available
- Agent configurations store your prompts and settings permanently—only execution history expires

## Usage and limits

Cosmic AI is available on all Cosmic plans with varying limits. You can add more tokens to your account by upgrading your plan or adding the AI tokens add-on. Go to the [pricing page](https://www.cosmicjs.com/pricing) to learn more.

### Tokens

Tokens are the unit of usage for Cosmic AI. In general, 1 token equals 1 word or 4 characters. You can view your AI usage from the Usage section of your projects.

**Input tokens** are the number of tokens used in your request. These are typically lower cost and represent the content you send to the AI (prompts, context, etc.). For text generation, this includes your messages and conversation history.

**Output tokens** are the number of tokens generated by the AI. These are higher cost (typically 5x more than input tokens) and represent what the AI creates:
- **Text generation**: Varies by response length
- **Image generation**: Fixed cost per image (4,800 - 57,600 tokens depending on model and size)
- **Video generation**: Fixed cost per video (144,000 - 768,000 tokens depending on model and duration)

Media generation (images and videos) costs are counted as **output tokens** to reflect the computational requirements of generating visual content.

## Getting started

[Log in](https://app.cosmicjs.com/login) to your Cosmic account and start using Cosmic AI today.