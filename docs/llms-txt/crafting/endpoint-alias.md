# Source: https://docs.sandboxes.cloud/docs/endpoint-alias.md

# Endpoint alias and endpoint routing

An `endpoint` defined in a sandbox is exposed to the Internet using a DNS name derived from the endpoint name and the sandbox name. It's sometimes inconvenient when the endpoint is used for demo or third party integration for callbacks, because the client must know the new DNS every time to target a different sandbox.

With `Endpoint Alias`, a fixed DNS name can be defined to target an endpoint from any sandbox at any time without changes on the client side. For example `demo-myorg.sandboxes.run` can always be used on the client while the target can be changed from `app--sandbox-foo-myorg.sandboxes.run` to `app--sandbox-bar-myorg.sandboxes.run` at any time.

### Common use cases

#### Callbacks and webhooks from third party API

For example I'm integrating a payment API which needs to callback to my service for posting the results. The callback URL must be specified on the partner side and changing it would require a long turn-around, which makes testing my API integration very tricky. With *Endpoint Alias*, I can create a fixed test callback URL and save it on my partner's side, and just by switching which sandbox it points to, developers can easily test the integration on their sandboxes.

#### Shared Demo URL

For example, I want to share a demo URL with my design partners so they can access our experimental features instantly and provide feedback. I created an *Endpoint Alias* once and share the fixed DNS with design partners. When a certain feature needs review, I pointed this Endpoint Alias to the endpoint of the sandbox with the work-in-progress change.

### Create endpoint alias

An *Endpoint Alias* can be created from Web Console (on the left, select `Resources` and `Endpoints`). Click *Create Endpoint Alias* card, provide a name and select an endpoint from a sandbox.

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/1ecee9e-CreateEndpointAlias.png" />

It can also be created using the CLI:$

```shell
$ cs endpoint-alias create demo sandbox-foo app
```

Please checkout the [CLI Document](https://docs.sandboxes.cloud/docs/command-line-tool#endpoint-alias) for more details.

### Common questions regarding endpoint alias

#### What happens if a sandbox is deleted?

The *Endpoint Alias* becomes *Unassigned*. Click the *Assign* button on the card to assign a different endpoint.

<Image align="center" className="border" width="50% " border={true} src="https://files.readme.io/5528778-EndpointAliasUnassigned.png" />

#### What happens if an endpoint is deleted or renamed?

Same as the sandbox deletion, the *Endpoint Alias* becomes *Unassigned*.

#### Does Endpoint Alias Support Authentication?

An *Endpoint Alias* is a name only, all features come from the actual endpoint. If the target endpoint is authenticated, then the *Endpoint Alias* supports authentication.