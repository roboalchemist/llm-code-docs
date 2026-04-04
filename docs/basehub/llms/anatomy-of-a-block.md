# Anatomy of a Block

> You can think of your Repository as a tree of Blocks. Let's explore how this works.

Similar to [Notion’s data model](https://www.notion.so/blog/data-model-behind-notion), every piece of content in BaseHub is a Block. You can think of your Repository as a tree of Blocks. It all starts with the [Root Block](https://docs.basehub.com/blocks/layout/root)—although you won’t see it—, which has nested Blocks within.

We conceptually split Blocks into two categories: Layout, and Primitive Blocks. In the next sections, you’ll read more about them.

Blocks contain schema and content. In contrast to other CMSs, where developers define a schema and then add the content, in BaseHub, this can happen at the same time due to how flexible our data model is.

As you add new Blocks and nest and reorder them, you’ll be altering your Repo’s Schema. That is, the structure that will be then distributed via GraphQL and into your website. Schemas become composable with a special Block called “Component”. Read more about it [here](https://docs.basehub.com/blocks/layout/component).

## UI

This is how Blocks get rendered.

![](https://assets.basehub.com/7b31fb4b/Pa5PZW7gHoOJ3T8Wn6AF3/image.png?width=3840&quality=90&format=auto)

### Zoom into a specific Block

In this case, a [Text Block](https://docs.basehub.com/blocks/primitives/text).

![](https://assets.basehub.com/7b31fb4b/AleUyM7NuRdyzE0LAoDxH/image.png?width=3840&quality=90&format=auto)

### Slash command

To add new blocks.

![](https://assets.basehub.com/7b31fb4b/HshqidfyEVLbPWEjSyTRw/image.png?width=3840&quality=90&format=auto)

### Sidebar

Makes it easy to get around your Repo.

![](https://assets.basehub.com/7b31fb4b/7fsFldGRzzrluJNlW8fQ2/image.png?width=3840&quality=90&format=auto)

### Tabs

Shows active Blocks.

![](https://assets.basehub.com/7b31fb4b/rUXuDVyBoigYmINICI6Dh/image.png?width=3840&quality=90&format=auto)