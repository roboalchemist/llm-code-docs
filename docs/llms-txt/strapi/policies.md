# Policies

Policies are functions that execute specific logic on each request before it reaches the [controller](/cms/backend-customization/controllers). They are mostly used for securing business logic.

Each [route](/cms/backend-customization/routes) of a Strapi project can be associated to an array of policies. For example, a policy named `is-admin` could check that the request is sent by an admin user, and restrict access to critical routes.

Policies can be global or scoped. [Global policies](#global-policies) can be associated to any route in the project. Scoped policies only apply to a specific [API](#api-policies) or [plugin](#plugin-policies) and should live under the corresponding `./src/api/<api-name>/policies/` or `./src/plugins/<plugin-name>/policies/` folder.

<figure style={{width: '100%', margin: '0'}}>
  <img src="/img/assets/backend-customization/diagram-routes.png" alt="Simplified Strapi backend diagram with routes and policies highlighted" />
  <em><figcaption style={{fontSize: '12px'}}>The diagram represents a simplified version of how a request travels through the Strapi back end, with policies and routes highlighted. The backend customization introduction page includes a complete, <a href="/cms/backend-customization#interactive-diagram">interactive diagram</a>.</figcaption></em>
</figure>

## Implementation

A new policy can be implemented:

- with the [interactive CLI command `strapi generate`](/cms/cli#strapi-generate) 
- or manually by creating a JavaScript file in the appropriate folder (see [project structure](/cms/project-structure)):
  - `./src/policies/` for global policies
  - `./src/api/[api-name]/policies/` for API policies
  - `./src/plugins/[plugin-name]/policies/` for plugin policies

<br/>

Global policy implementation example:

</Tabs>

`policyContext` is a wrapper around the [controller](/cms/backend-customization/controllers) context. It adds some logic that can be useful to implement a policy for both REST and GraphQL.

<br/>

Policies can be configured using a `config` object:

</Tabs>

## Usage

To apply policies to a route, add them to its configuration object (see [routes documentation](/cms/backend-customization/routes#policies)).

Policies are called different ways depending on their scope:

- use `global::policy-name` for [global policies](#global-policies)
- use `api::api-name.policy-name` for [API policies](#api-policies)
- use `plugin::plugin-name.policy-name` for [plugin policies](#plugin-policies)

:::tip
To list all the available policies, run `yarn strapi policies:list`.
:::

### Global policies

Global policies can be associated to any route in a project.

</Tabs>

### Plugin policies

Plugins can add and expose policies to an application. For example, the [Users & Permissions feature](/cms/features/users-permissions) comes with policies to ensure that the user is authenticated or has the rights to perform an action:

</Tabs>

### API policies

API policies are associated to the routes defined in the API where they have been declared.

</Tabs>

To use a policy in another API, reference it with the following syntax: `api::[apiName].[policyName]`:

</Tabs>