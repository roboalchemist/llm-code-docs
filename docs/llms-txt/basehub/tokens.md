# Tokens

> Learn which tokens exist in BaseHub and what they are for.

## Read Token

The most commonly used token in BaseHub, has unrestricted read access scoped to a repository. **By default, you should be using this token.**

Unrestricted read access means the token can retrieve all content, metadata, and structure within its assigned repository, including drafts and published content across all collections. However, it cannot perform any write operations or access content from other repositories.

Read more on how to use this toke in the [Query](https://docs.basehub.com/api-reference/javascript-sdk/basehub-client/query) documentation.

warning:

### Hidden blocks

Blocks that are hidden don’t pass through commit validation (e.g: required blocks won’t fail if they’re empty) and won’t be exposed in the API.

## Admin Token

Handle this token with greater care as it includes all _Read Token_ permissions plus write access to the repository. This token can be used by a team member or by the AI agents to make updates via the [Mutation API](https://docs.basehub.com/api-reference/javascript-sdk/basehub-client/mutation).

## MCP Token

This token has a very specific purpose and it’s to give permissions to the [BaseHub MCP Server](https://docs.basehub.com/ai/mcp) to read and write into your repository. This token, in comparison to the read and admin tokens, isn’t one per repo, rather it’s one per repo and user. So each team member will have a different MCP Token.

## Where can I find my tokens?

Here you go:

![](https://assets.basehub.com/7b31fb4b/40d2463fb34580ff8aeeaf9a5d6a93d3/cleanshot-2025-08-02-at-19.31.392x.png?width=3840&quality=90&format=auto)

## Help

[My tokens were exposed, what do I do?](https://help.basehub.com/dashboard/my-api-keys-were-exposed-what-do-i-do)