# Source: https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/publishing/platform-api.md

# Source: https://www.apollographql.com/docs/graphos/platform/platform-api.md

# The GraphOS Platform API

The *GraphOS Platform API* enables you to perform GraphOS actions from your own custom application. Currently, these actions include:

* Fetching details about your organization's graphs
* Publishing schemas to new or existing variants (limited to 400 requests per minute, per graph)
* Running [schema checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks) and obtaining their results
* Creating and editing [schema proposals](https://www.apollographql.com/docs/graphos/platform/schema-management/proposals), including adding reviewers
* Removing variants from a graph
* Removing subgraphs from a supergraph
* Managing API keys
* CRUD operations on persisted query lists, including linking them to variants and publishing operations to them
* [Changing GraphOS Studio session length](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#change-studio-session-length) for an organization's users
* Viewing operation and field insights

We'll continue to expand the Platform API with additional GraphOS functionality over time.

## API docs

The Platform API is itself represented as a public graph in GraphOS! Documentation for the API (which includes a README and collections of example operations) is available in GraphOS Studio.

Open Platform API docs
