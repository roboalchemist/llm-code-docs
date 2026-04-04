Source: https://docs.slack.dev/reference/scopes/search.read.public

# search:read.public scope

Search a workspace's content in public channels

## Facts

## Supported token types

[`Bot`](/authentication/tokens#bot)

[`User`](/authentication/tokens#user)

## Compatible API methods

[`assistant.search.context`](/reference/methods/assistant.search.context)

[`assistant.search.info`](/reference/methods/assistant.search.info)

## Usage info {#usage-info}

This scope allows [apps using AI features](/ai/) to query messages and files in public channels to help them answer user queries. It allows searching for data in public channels within the workspace(s) where the app is installed AND the searching user is a member. The searching user need not be a member of the public channels, just of the workspace, for the channels to be included in the search results.
