# Source: https://docs.convex.dev/deployment-api.md

# Deployment API

The public interface of a Convex deployment is defined by the functions defined in files in a convex folder.

The public HTTP endpoints of every Convex deployment consist of custom HTTP endpoints defined by [HTTP Actions](/functions/http-actions.md) and a static [public HTTP API](/http-api/.md).

Deployments also provide private endpoints only for the administrators of that deployment:

* [Streaming export API](/streaming-export-api.md)
* [Streaming import API](/streaming-import-api.md)
* [Platform APIs](/deployment-platform-api.md)
