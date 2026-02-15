# Source: https://developers.cloudflare.com/workers/examples/respond-with-another-site/index.md

---

title: Respond with another site · Cloudflare Workers docs
description: Respond to the Worker request with the response from another
  website (example.com in this example).
lastUpdated: 2026-01-27T21:11:25.000Z
chatbotDeprioritize: false
tags: Middleware,JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/respond-with-another-site/
  md: https://developers.cloudflare.com/workers/examples/respond-with-another-site/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/respond-with-another-site)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

* JavaScript

  ```js
  export default {
    async fetch(request) {
      function MethodNotAllowed(request) {
        return new Response(`Method ${request.method} not allowed.`, {
          status: 405,
          headers: {
            Allow: "GET",
          },
        });
      }
      // Only GET requests work with this proxy.
      if (request.method !== "GET") return MethodNotAllowed(request);
      return fetch(`https://example.com`);
    },
  };
  ```

  [Run Worker in Playground](https://workers.cloudflare.com/playground#LYVwNgLglgDghgJwgegGYHsHALQBM4RwDcABAEbogB2+CAngLzbPYZb6HbW5QDGU2AAwAWAIwAmAOzCAHKIBsI4QC4WLNsA5wuNPgJETpcxcOEBYAFABhdFQgBTO9gAiUAM4x0bqNFvKSGngExCRUcMD2DABEUDT2AB4AdABWblGkqFBgjuGRMXFJqVGWNnaOENgAKnQw9v5wMDBgfARQtsjJcABucG68CLAQANTA6Ljg9paWCZ5IJLj2qHDgECQA3hYkJL10VLwB9hC8ABYAFAj2AI4g9m4QAJTrm1sB1Ly+VCQAsofHYwBy6AgAEEwGB0AB3ey4c5XG53R4bF4vC4QEAIT5UewQkgAJVuniobnspwABj8IH9cCQACRrC7XW4QRIRSljAC+oSB2zBkOhiVJABonsjkXcCCA3P5hIIAKyC56ikjHexwBYIKUipUvUHgiH+KIAcQAopUogrtSR2RbRez7kRFVbHchkCQAPJUMB0EgmyokBnwiBuEgQzAAaxDPmOJEp7hIMAQ6HidESjqgqBIsMZdxZvzGJAAhAwGCQjaaoo9UejPhSqYCQbyoTCA0z7Y6qxiDkczqTjhAIDApS6EuEmvZErx0MBSW2ttaLOyiJY1MwNFodDx+EIxFJZAolCVbA4nK4PF4fG0qP5AlpSGEItFWWrgukAlkcg+omRwWRitYj+UVQ1HU2yNM0vCtO0qS2FMFhrFEwBwLEAD6ozjNkUTKPkCyFGk7LLiua7BBuejboYe4mMIzCWEAA)

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      function MethodNotAllowed(request) {
        return new Response(`Method ${request.method} not allowed.`, {
          status: 405,
          headers: {
            Allow: "GET",
          },
        });
      }
      // Only GET requests work with this proxy.
      if (request.method !== "GET") return MethodNotAllowed(request);
      return fetch(`https://example.com`);
    },
  } satisfies ExportedHandler;
  ```

* Python

  ```py
  from workers import WorkerEntrypoint, Response, fetch


  class Default(WorkerEntrypoint):
      def fetch(self, request):
          def method_not_allowed(request):
              msg = f'Method {request.method} not allowed.'
              headers = {"Allow": "GET"}
              return Response(msg, headers=headers, status=405)


          # Only GET requests work with this proxy.
          if request.method != "GET":
              return method_not_allowed(request)


          return fetch("https://example.com")
  ```
