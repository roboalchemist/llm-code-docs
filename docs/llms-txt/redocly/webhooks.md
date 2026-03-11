# Source: https://redocly.com/learn/openapi/openapi-visual-reference/webhooks.md

# Webhooks

> The incoming webhooks that MAY be received as part of this API and that the API consumer MAY choose to implement. Closely related to the callbacks feature, this section describes requests initiated other than by an API call, for example by an out of band registration. The key name is a unique string to refer to each webhook, while the (optionally referenced) [Path Item Object](/learn/openapi/openapi-visual-reference/path-item) describes a request that may be initiated by the API provider and the expected responses. An example is available.


## Visuals


```yaml

webhooks:
  resultPosted:
    $ref: ./webhooks/chess-result-posted.yaml
```

Redocly renders the webhook in the sidebar navigation with a badge named "Event" by default.
Redocly renders the badge with the full word "Webhook" with the operation summary.

The following image shows how Redocly renders webhooks in the sidebar navigation.

![webhooks in sidebar](/assets/webhooks-sidebar.a7caffbc80b8ed2ed3b817ac12266febb93afa5c25d6b6459e59e30e87e16e4f.6f948c6e.png)

The following image shows how Redocly renders the summary heading.

![webookssummary](/assets/webhooks-summary.481b8932448a203e94c28836529cdc08e583ed7f90de26df081685d678ed3cd4.6f948c6e.png)

The following image shows how Redocly renders the entire webhook operation.

![webhooks](/assets/webhooks.2bb56151c1c7be751f015f7fa6a6c4431ec31465d9a6cbcfbcffe9d2b52c34b8.6f948c6e.png)

## Types

- `WebhooksMap`
- [`PathItem`](/learn/openapi/openapi-visual-reference/path-item)


![webhooks map](/assets/webhooks-map-path-item-relationship.0cfdc422ac3ac349697d737665fe747ea29a1eee0427fb525e87f276b9b081ed.6f948c6e.png)


```mermaid
erDiagram
          WebhookMap }|..|{ PathItem : has
```