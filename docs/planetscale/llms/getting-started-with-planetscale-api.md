# Source: https://planetscale.com/docs/api/reference/getting-started-with-planetscale-api.md

# Getting started with PlanetScale API

> Learn how to start using the PlanetScale API.

## Overview

You can use the PlanetScale API to manage your PlanetScale databases programmatically.

The PlanetScale API does **not** include direct access to the data in the database. Some endpoints will consist of database schema information or connection information.

## Authentication

Before making your first API call, set up the proper authentication for the PlanetScale API using the `Authorization` header. There are two API authentication types: **Service tokens** and **OAuth**.

### Service tokens

Most endpoints only need a service token for authentication, but some organization-specific endpoints also need OAuth. Each endpoint will state what types of authentication are allowed. See the [Service tokens documentation](/docs/api/reference/service-tokens) for creating a service token and making your first API call with the PlanetScale API.

### OAuth applications

All OAuth applications have a comprehensive list of scopes that the application can request from the PlanetScale user. See the [OAuth documentation](/docs/api/reference/oauth) for more info.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt