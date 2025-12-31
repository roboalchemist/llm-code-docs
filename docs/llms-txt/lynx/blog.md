# Source: https://lynxjs.org/help/blog.md

# Writing Blog Posts

The Lynx website hosts a blog to share updates, tutorials, and announcements.

## Location

All blog posts are located in `docs/en/blog/`.

## Creating a New Post

1. Create a new `.mdx` file in `docs/en/blog/`. The filename will be part of the URL.
2. Add the necessary frontmatter.

```yaml
---
title: My New Blog Post
date: 2024-01-01
author: Your Name
description: A short summary of the post.
---
```

3. Write your content using standard Markdown and MDX components.

## Blog Components

We provide specialized components for blog listings and author avatars.

### `<BlogList>`

Renders the list of blog posts automatically.

```tsx
import { BlogList } from '@lynx';

<BlogList limit={1} />;
```

[Lynx 3.5: Main Thread Script, React Compiler, HarmonyOS ImprovementsNovember 10, 2025

![](https://github.com/loongliu.png)Leron LiuPerformance Lead @ Lynx![](https://github.com/huxpro.png)Xuan HuangArchitect @ Lynx![](https://github.com/lynx-family.png)The Lynx Teamlynxjs.org](/next/blog/lynx-3-5)
### `<BlogAvatar>`

Renders avatars for blog authors.

You can add new authors in `src/components/blog-avatar/authors.json`.

```tsx
import { BlogAvatar } from '@lynx';

<BlogAvatar list={['lynx']} />;
```

<BlogAvatar list={['lynx']} />

## Blog Index

The blog index is automatically generated. Ensure your `date` field is correct so posts are ordered chronologically.

## Images

Place images in the `public/` directory or relative to the blog post if configured.
