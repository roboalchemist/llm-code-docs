# Platform Overview

> Understand the basics of the BaseHub Platform.

BaseHub has three main properties:

1.  The Dashboard, `basehub.com`, where you create teams, repositories, collaborate on content, etc
    
2.  The GraphQ: API, `api.basehub.com`, where you interact with your repository programmatically, either to query data in your repo, or to mutate data in your repo
    
3.  The SDK, which you install and run within your website: `pnpm i basehub`
    

As you use BaseHub, you—or your team as a whole—will interact with all of these parts, and that’s why having a good understanding of the whole is important.

![](https://assets.basehub.com/7b31fb4b/wj_i1gS0peoNRJ_wze9ig/cleanshot-2024-05-24-at-16.56.032x.png?width=3840&quality=90&format=auto)

## Creating a Block

Every piece of content you create in BaseHub is a Block. Similar to Lego, Blocks can have different types and functions. You can nest Blocks, reference Blocks, and more.

In the Editor, you’ll create Blocks by typing `/` and choosing one Block type from the Block selector.

Read more about Blocks in our Blocks Reference:

[Blocks Reference(Deep dive into all of the different Blocks that are available in BaseHub.)](https://docs.basehub.com/blocks-reference)

## Committing

A Commit stores a snapshot of your Repo at that specific point in time. Inspired by Git, each commit is immutable, and it’s a core of how version control works in BaseHub.

Once you’re happy with your changes, you can create a Commit. The API will now use the latest commit (the Head Commit) to resolve your queries.

## Exploring the GraphQL API

A great way to explore the GraphQL API is to use the Explorer. You can find it in the Developers Tab:

![](https://assets.basehub.com/7b31fb4b/5abd4deb5171f8df9b4bb848dcc4c20b/cleanshot-2025-01-20-at-19.23.462x.png?width=3840&quality=90&format=auto)