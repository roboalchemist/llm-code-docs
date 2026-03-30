# Source: https://www.cosmicjs.com/docs/agent-skills.md

# Agent Skills

AI coding assistant skills for building applications with Cosmic headless CMS. Agent skills provide AI coding assistants with context about the Cosmic SDK and API, enabling them to generate accurate code for your content-powered applications.

## Installation

Install skills for your AI coding assistant using the skills CLI:
```bash
npx skills add cosmicjs/skills

```
This will add the Cosmic skill to your local project, giving your AI assistant context about the Cosmic SDK and API.

## What the Skill Covers

The Cosmic agent skill provides comprehensive guidance on:

### SDK-first Development

- Setting up the `@cosmicjs/sdk` package
- Configuring bucket clients with proper authentication
- Type-safe methods and error handling

### Objects API

Create, read, update, and delete content with the Objects API:
```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY',
  writeKey: 'BUCKET_WRITE_KEY'
})

// Get multiple Objects
const { objects: posts } = await cosmic.objects
  .find({ type: 'posts' })
  .props(['id', 'title', 'slug', 'metadata'])
  .limit(10)

// Get single Object by slug
const post = await cosmic.objects
  .findOne({ type: 'posts', slug: 'hello-world' })
  .props(['title', 'slug', 'metadata'])

// Create an Object
await cosmic.objects.insertOne({
  title: 'My Post',
  type: 'posts',
  metadata: {
    content: 'Post content here...',
    author: 'author-object-id'
  }
})

```
### Object Types & Metafields

Content modeling with Object types and all available Metafield types:

- Text, textarea, markdown, HTML
- Number, date, switch, color
- Dropdown, radio buttons, checkboxes
- Single and multiple file uploads
- Object relationships (single and multiple)
- JSON, repeater, and parent (nested) fields

### Media API

Upload and manage files and images:
```js
// Upload media
const uploaded = await cosmic.media.insertOne({
  media: { originalname: 'photo.jpg', buffer: fileBuffer },
  folder: 'uploads',
  alt_text: 'Description of image'
})

// Use imgix for image transformations
const optimized = `${media.imgix_url}?w=800&auto=format,compress`

```
### Queries

MongoDB-style filtering and search:
```js
// Comparison operators
await cosmic.objects.find({
  type: 'products',
  'metadata.price': { $lt: 100 }
})

// Array matching
await cosmic.objects.find({
  type: 'products',
  'metadata.tags': { $in: ['sale', 'featured'] }
})

// Text search
await cosmic.objects.find({
  type: 'posts',
  title: { $regex: 'hello', $options: 'i' }
})

```
### AI Generation

Built-in AI capabilities for text, images, and video:
```js
// Generate text
const text = await cosmic.ai.generateText({
  prompt: 'Write a product description',
  model: 'claude-sonnet-4-5-20250929'
})

// Generate image
const image = await cosmic.ai.generateImage({
  prompt: 'Mountain landscape at sunset',
  size: '1024x1024',
  folder: 'ai-generated'
})

// Generate video
const video = await cosmic.ai.generateVideo({
  prompt: 'A kitten playing with yarn',
  duration: 8,
  resolution: '720p'
})

```
### Framework Patterns

Integration patterns for popular frameworks:

- **Next.js App Router** - Server Components and Server Actions
- **React** - Client-side data fetching
- **Astro** - Static and server-rendered pages
- **And more** - Remix, Nuxt, Svelte, etc.

## Quick Example

Here's a complete Next.js App Router example:
```tsx
// app/posts/page.tsx
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: process.env.COSMIC_BUCKET_SLUG!,
  readKey: process.env.COSMIC_READ_KEY!
})

export default async function Posts() {
  const { objects: posts } = await cosmic.objects
    .find({ type: 'posts' })
    .props(['title', 'slug', 'metadata.excerpt'])
    .limit(10)

  return (
    <ul>
      {posts.map(post => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}

```
## Supported AI Agents

The Cosmic agent skill works with:

- **Cursor** - AI-first code editor
- **Claude Code** - Anthropic's coding assistant
- **GitHub Copilot** - AI pair programmer
- **Windsurf** - AI coding assistant
- **Gemini** - Google's AI assistant
- And 16+ other AI coding agents

## Key Reminders

The skill teaches your AI assistant these important patterns:

1. **Object type is the SLUG** - Use `type: 'blog-posts'`, not `type: 'Blog Posts'`
2. **Media uses `name`** - Reference media by `name` property, not URL
3. **Relations use `id`** - Reference related Objects by `id`, not slug
4. **Never expose `writeKey`** - Keep it server-side only
5. **Use `props()`** - Always specify needed properties for performance
6. **imgix for images** - Use `imgix_url` with query params for optimizations

## Resources

- [Cosmic Documentation](/docs)
- [API Reference](/docs/api)
- [Discord Community](https://discord.com/invite/MSCwQ7D6Mg)