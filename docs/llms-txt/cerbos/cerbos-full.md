# Cerbos Documentation

Source: https://docs.cerbos.dev/llms-full.txt

---



Painless access control for your software
====================
Cerbos helps you super-charge your authorization implementation by writing context-aware access control policies for your application resources. Author access rules using an intuitive YAML configuration language, use your Git-ops infrastructure to test and deploy them and, make simple API requests to the Cerbos PDP to evaluate the policies and make dynamic access decisions.

![How Cerbos works](_images/how_cerbos_works.png)

Iterate quickly

Instantly update your access policies without re-compiling or re-deploying your application. Let your product owner tweak access policies on their own while you focus on more interesting work.

Increase visibility

The traditional practice of weaving authorization logic into application code effectively obscures the logic and complicates the source code. Documentation is notoriously difficult to keep up-to-date as the system evolves — inevitably requiring a code spelunking session to answer questions or update the documentation. This is often tedious, error-prone and requires valuable developer time. The simple policy-as-configuration approach provided by Cerbos helps even non-developers easily understand the authorization logic of the system. Best of all, it is always guaranteed to be up-to-date.

Don’t repeat yourself

In modern microservice environments it is quite common to share some resources between different services developed by different teams (e.g. a bank account in a banking system). These services could even be developed using different programming languages. Cerbos provides a language-agnostic API to share common access control policies between these disparate services — ensuring instant consistency without the need to coordinate development and deployment efforts across many teams.

Use proven techniques

Cerbos provides advanced tooling to lint, compile and test policies. Native GitOps support is built in. Use the same development best practices you use day-to-day to develop and deploy authorization logic.

Comprehensive audit trails

The textual policy language of Cerbos makes it ideal for storing policies on version control systems. Follow the evolution of access rules through time and pinpoint exactly when changes were made, why, and by whom.

Cerbos Policy Decision Point (PDP) is built for modern, containerised microservice environments with support for both x86-64 and ARM64 architectures, comprehensive observability integrations (metrics, distributed tracing), REST and gRPC endpoints, and native GitOps support (CI tooling, push-to-deploy).

## [](#%5Fcerbos%5Fworkflow)Cerbos workflow

* Author Cerbos policies to define access rules for your resources. Optionally, write unit tests for the policies using the Cerbos DSL.
* Compile the policies and run tests using the Cerbos CLI.
* Follow your standard development process to push the changes to production. (E.g. create pull request, run CI tests, get approval and merge to prod branch)
* Cerbos will automatically pull the latest commits from the production branch and update the policies in place without requiring a restart. Your changes are now rolled out!

## [](#%5Fauthorization%5Fas%5Fa%5Fservice)Authorization as a Service

Cerbos is designed to be deployed as a service rather than a library compiled into an application. This design choice provides several benefits:

* Permission checks can be performed by any part of the application stack and even shared between multiple services regardless of the programming language, CPU architecture, operating system or deployment model.
* Policy updates instantly take effect without having to recompile or redeploy the applications. This reduces disruption to busy services and enables policy authors to iterate quickly and respond to events faster.
* With modern network stacks, the communication overhead is [effectively negligible](https://www.miketheman.net/2021/12/28/container-to-container-communication/) in all but the most extreme cases. Even in those exceptional cases, scaling Cerbos to handle the demand is extremely easy due to its lightweight, stateless design.
* All development and optimization efforts to Cerbos can be concentrated on a single project because we do not need to replicate the effort on multiple language-specific implementations. All our users, regardless of their programming language of choice, immediately get the benefit of the latest and greatest Cerbos features as soon they are released.

The Cerbos approach is a proven, modern, cloud native pattern for delivering language-agnostic infrastructure services. [Microsoft Dapr](https://dapr.io), [Istio](https://istio.io) and [Linkerd](https://linkerd.io) are good examples of popular products utilising similar language-agnostic service APIs to augment applications.

Because Cerbos is in the critical request path and expected to handle large volumes of requests, we are obsessive about making Cerbos as fast and as efficient as possible with every release. Cerbos exposes an efficient, low latency gRPC API and is designed to be stateless and lightweight so that it can be deployed as a sidecar right next to your application. It can even be accessed over Unix domain sockets for extra security and reduced overhead.

Quickstart
====================
Create a directory to store the policies.

```sh
mkdir -p cerbos-quickstart/policies
```

Now start the Cerbos server. We are using the container image in this guide but you can follow along using the binary as well. See [installation instructions](installation/binary.html) for more information.

```shell
docker run --rm --name cerbos -d -v $(pwd)/cerbos-quickstart/policies:/policies -p 3592:3592 -p 3593:3593  ghcr.io/cerbos/cerbos:0.51.0
```

Time to try out a simple request.

| |  If you prefer to use [Postman](https://www.postman.com), [Insomnia](https://insomnia.rest) or any other software that supports OpenAPI, you can follow this guide along on those tools by downloading the OpenAPI definitions from <http://localhost:3592/schema/swagger.json>. You can also use the built-in API browser by pointing your browser to <http://localhost:3592>. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

* cURL
* .NET
* Go
* Java
* JS
* PHP
* Python
* Ruby
* Rust

```shell
cat <<EOF | curl --silent "http://localhost:3592/api/check/resources?pretty" -d @-
{
  "requestId": "quickstart",
  "principal": {
    "id": "bugs_bunny",
    "roles": [
      "user"
    ],
    "attr": {
      "beta_tester": true
    }
  },
  "resources": [
    {
      "actions": [
        "view:public",
        "comment"
      ],
      "resource": {
        "kind": "album:object",
        "id": "BUGS001",
        "attr": {
          "owner": "bugs_bunny",
          "public": false,
          "flagged": false
        }
      }
    },
    {
      "actions": [
        "view:public",
        "comment"
      ],
      "resource": {
        "kind": "album:object",
        "id": "DAFFY002",
        "attr": {
          "owner": "daffy_duck",
          "public": true,
          "flagged": false
        }
      }
    }
  ]
}
EOF
```

```csharp
using Cerbos.Api.V1.Effect;
using Cerbos.Sdk.Response;
using Cerbos.Sdk.Builder;
using Cerbos.Sdk.Utility;

internal class Program
{
    private static void Main(string[] args)
    {
        var client = CerbosClientBuilder.ForTarget("http://localhost:3593").WithPlaintext().Build();
        var request = CheckResourcesRequest
            .NewInstance()
            .WithRequestId(RequestId.Generate())
            .WithIncludeMeta(true)
            .WithPrincipal(
                Principal
                    .NewInstance("bugs_bunny", "user")
                    .WithAttribute("beta_tester", AttributeValue.BoolValue(true))
            )
            .WithResourceEntries(
                ResourceEntry
                    .NewInstance("album:object", "BUGS001")
                    .WithAttribute("owner", AttributeValue.StringValue("bugs_bunny"))
                    .WithAttribute("public", AttributeValue.BoolValue(false))
                    .WithAttribute("flagged", AttributeValue.BoolValue(false))
                    .WithActions("comment", "view:public"),

                ResourceEntry
                    .NewInstance("album:object", "DAFFY002")
                    .WithAttribute("owner", AttributeValue.StringValue("daffy_duck"))
                    .WithAttribute("public", AttributeValue.BoolValue(true))
                    .WithAttribute("flagged", AttributeValue.BoolValue(false))
                    .WithActions("comment", "view:public")
            );

        CheckResourcesResponse result = client.CheckResources(request);
        foreach (var resourceId in new[] { "BUGS001", "DAFFY002" })
        {
            var resultEntry = result.Find(resourceId);
            Console.Write($"\nResource ID: {resourceId}\n");
            foreach (var actionEffect in resultEntry.Actions)
            {
                string action = actionEffect.Key;
                Effect effect = actionEffect.Value;
                Console.Write($"\t{action} -> {(effect == Effect.Allow ? "EFFECT_ALLOW" : "EFFECT_DENY")}\n");
            }
        }
    }
}
```

```go
package main

import (
	"context"
	"log"

	"github.com/cerbos/cerbos-sdk-go/cerbos"
)

func main() {
	c, err := cerbos.New("localhost:3593", cerbos.WithPlaintext())
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}

	principal := cerbos.NewPrincipal("bugs_bunny", "user")
	principal.WithAttr("beta_tester", true)

	kind := "album:object"
	actions := []string{"view:public", "comment"}

	r1 := cerbos.NewResource(kind, "BUGS001")
	r1.WithAttributes(map[string]any{
		"owner":   "bugs_bunny",
		"public":  false,
		"flagged": false,
	})

	r2 := cerbos.NewResource(kind, "DAFFY002")
	r2.WithAttributes(map[string]any{
		"owner":   "daffy_duck",
		"public":  true,
		"flagged": false,
	})

	batch := cerbos.NewResourceBatch()
	batch.Add(r1, actions...)
	batch.Add(r2, actions...)

	resp, err := c.CheckResources(context.Background(), principal, batch)
	if err != nil {
		log.Fatalf("Failed to check resources: %v", err)
	}
	log.Printf("%v", resp)
}
```

```java
package demo;

import static dev.cerbos.sdk.builders.AttributeValue.boolValue;
import static dev.cerbos.sdk.builders.AttributeValue.stringValue;

import java.util.Map;

import dev.cerbos.sdk.CerbosBlockingClient;
import dev.cerbos.sdk.CerbosClientBuilder;
import dev.cerbos.sdk.CheckResult;
import dev.cerbos.sdk.builders.Principal;
import dev.cerbos.sdk.builders.ResourceAction;


public class App {
    public static void main(String[] args) throws CerbosClientBuilder.InvalidClientConfigurationException {
        CerbosBlockingClient client=new CerbosClientBuilder("localhost:3593").withPlaintext().buildBlockingClient();

        for (String n : new String[]{"BUGS001", "DAFFY002"}) {
            CheckResult cr = client.batch(
                Principal.newInstance("bugs_bunny", "user")
                    .withAttribute("beta_tester", boolValue(true))
                )
                .addResources(
                    ResourceAction.newInstance("album:object","BUGS001")
                        .withAttributes(
                            Map.of(
                                "owner", stringValue("bugs_bunny"),
                                "public", boolValue(false),
                                "flagged", boolValue(false)
                            )
                        )
                        .withActions("view:public", "comment"),
                    ResourceAction.newInstance("album:object","DAFFY002")
                        .withAttributes(
                            Map.of(
                                "owner", stringValue("daffy_duck"),
                                "public", boolValue(true),
                                "flagged", boolValue(false)
                            )
                        )
                        .withActions("view:public", "comment")
                )
                .check().find(n).orElse(null);

            if (cr != null) {
                System.out.printf("\nResource: %s\n", n);
                cr.getAll().forEach((action, allowed) -> { System.out.printf("\t%s -> %s\n", action, allowed ? "EFFECT_ALLOW" : "EFFECT_DENY"); });
            }
        }
    }
}
```

```javascript
const { GRPC: Cerbos } = require("@cerbos/grpc");

const cerbos = new Cerbos("localhost:3593", { tls: false });

(async() => {
  const kind = "album:object";
  const actions = ["view:public", "comment"];

  const cerbosPayload = {
    principal: {
      id: "bugs_bunny",
      roles: ["user"],
      attributes: {
        beta_tester: true,
      },
    },
    resources: [
      {
        resource: {
          kind: kind,
          id: "BUGS001",
          attributes: {
		    owner:   "bugs_bunny",
		    public:  false,
		    flagged: false,
          },
        },
        actions: actions,
      },
      {
        resource: {
          kind: kind,
          id: "DAFFY002",
          attributes: {
		    owner:   "daffy_duck",
		    public:  true,
		    flagged: false,
          },
        },
        actions: actions,
      },
    ],
  };

  const decision = await cerbos.checkResources(cerbosPayload);
  console.log(decision.results)
})();
```

```php
<?php

require __DIR__ . '/vendor/autoload.php';

use Cerbos\Effect\V1\Effect;
use Cerbos\Sdk\Builder\AttributeValue;
use Cerbos\Sdk\Builder\CerbosClientBuilder;
use Cerbos\Sdk\Builder\CheckResourcesRequest;
use Cerbos\Sdk\Builder\Principal;
use Cerbos\Sdk\Builder\ResourceEntry;
use Cerbos\Sdk\Utility\RequestId;

$client = CerbosClientBuilder::newInstance("localhost:3593")
            ->withPlaintext(true)
            ->build();

$request = CheckResourcesRequest::newInstance()
    ->withRequestId(RequestId::generate())
    ->withPrincipal(
        Principal::newInstance("bugs_bunny")
            ->withRole("user")
            ->withAttribute("beta_tester", AttributeValue::boolValue(true))
    )
    ->withResourceEntries(
        [
            ResourceEntry::newInstance("album:object", "BUGS001")
                ->withAttribute("owner", AttributeValue::stringValue("bugs_bunny"))
                ->withAttribute("public", AttributeValue::boolValue(false))
                ->withAttribute("flagged", AttributeValue::boolValue(false))
                ->withActions(["comment", "view:public"]),

            ResourceEntry::newInstance("album:object", "DAFFY002")
                ->withAttribute("owner", AttributeValue::stringValue("daffy_duck"))
                ->withAttribute("public", AttributeValue::boolValue(true))
                ->withAttribute("flagged", AttributeValue::boolValue(false))
                ->withActions(["comment", "view:public"])
        ]
    );

$checkResourcesResponse = $client->checkResources($request);
foreach (["BUGS001", "DAFFY002"] as $resourceId) {
    $resultEntry = $checkResourcesResponse->find($resourceId);
    $actions = $resultEntry->getActions();
    foreach ($actions as $k => $v) {
        printf("%s -> %s", $k, Effect::name($v));
    }
}
?>
```

```python
import json

from cerbos.sdk.client import CerbosClient
from cerbos.sdk.model import Principal, Resource, ResourceAction, ResourceList
from fastapi import HTTPException, status

principal = Principal(
    "bugs_bunny",
    roles=["user"],
    attr={
        "beta_tester": True,
    },
)

actions = ["view:public", "comment"]
resource_list = ResourceList(
    resources=[
        ResourceAction(
            Resource(
                "BUGS001",
                "album:object",
                attr={
                    "owner": "bugs_bunny",
                    "public": False,
                    "flagged": False,
                },
            ),
            actions=actions,
        ),
        ResourceAction(
            Resource(
                "DAFFY002",
                "album:object",
                attr={
                    "owner": "daffy_duck",
                    "public": True,
                    "flagged": False,
                },
            ),
            actions=actions,
        ),
    ],
)

with CerbosClient(host="http://localhost:3592") as c:
    try:
        resp = c.check_resources(principal=principal, resources=resource_list)
        resp.raise_if_failed()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized"
        )

print(json.dumps(resp.to_dict(), sort_keys=False, indent=4))
```

```ruby
require 'cerbos'
require 'json'

client = Cerbos::Client.new("localhost:3593", tls: false)

kind = "album:object"
actions = ["view:public", "comment"]

r1 = {
  :kind => kind,
  :id => "BUGS001",
  :attributes => {
    :owner => "bugs_bunny",
    :public => false,
    :flagged => false,
  }
}

r2 = {
  :kind => kind,
  :id => "DAFFY002",
  :attributes => {
    :owner => "daffy_duck",
    :public => true,
    :flagged => false,
  }
}

decision = client.check_resources(
  principal: {
    id: "bugs_bunny",
    roles: ["user"],
    attributes: {
      beta_tester: true,
    },
  },
  resources: [
    {
      resource: r1,
      actions: actions
    },
    {
      resource: r2,
      actions: actions
    },
  ],
)

res = {
  :results => [
    {
      :resource => r1,
      :actions => {
        :comment => decision.allow?(resource: r1, action: "comment"),
        :"view:public" => decision.allow?(resource: r1, action: "view:public"),
      },
    },
    {
      :resource => r2,
      :actions => {
        :comment => decision.allow?(resource: r2, action: "comment"),
        :"view:public" => decision.allow?(resource: r2, action: "view:public"),
      },
    },
  ],
}
puts JSON.pretty_generate(res)
```

```rust
use cerbos::sdk::attr::attr;
use cerbos::sdk::model::{Principal, Resource, ResourceAction, ResourceList};
use cerbos::sdk::{CerbosAsyncClient, CerbosClientOptions, CerbosEndpoint, Result};

#[tokio::main]
async fn main() -> Result<()> {
    let opt =
        CerbosClientOptions::new(CerbosEndpoint::HostPort("localhost", 3593)).with_plaintext();
    let mut client = CerbosAsyncClient::new(opt).await?;

    let principal =
        Principal::new("bugs_bunny", ["user"]).with_attributes([attr("beta_tester", true)]);

    let actions: [&str; 2] = ["view:public", "comment"];

    let resp = client
        .check_resources(
            principal,
            ResourceList::new_from([
                ResourceAction(
                    Resource::new("BUGS001", "album:object").with_attributes([
                        attr("owner", "bugs_bunny"),
                        attr("public", false),
                        attr("flagged", false),
                    ]),
                    actions,
                ),
                ResourceAction(
                    Resource::new("DAFFY002", "album:object").with_attributes([
                        attr("owner", "daffy_duck"),
                        attr("public", true),
                        attr("flagged", false),
                    ]),
                    actions,
                ),
            ]),
            None,
        )
        .await?;

    println!("{:?}", resp.response);

    Ok(())
}
```

In this example, the `bugs_bunny` principal is trying to perform two actions (`view:public` and `comment`) on two `album:object` resources. The resource instance with the ID `BUGS001` belongs to `bugs_bunny` and is private (`public` attribute is `false`). The other resource instance with the ID `DAFFY002` belongs to `daffy_duck` and is public.

This is the response from the server:

Response

```json
{
  "requestId": "quickstart",
  "results": [
    {
      "resource": {
        "id": "BUGS001",
        "kind": "album:object"
      },
      "actions": {
        "comment": "EFFECT_DENY",
        "view:public": "EFFECT_DENY"
      }
    },
    {
      "resource": {
        "id": "DAFFY002",
        "kind": "album:object"
      },
      "actions": {
        "comment": "EFFECT_DENY",
        "view:public": "EFFECT_DENY"
      }
    }
  ]
}
```

Bugs Bunny is not allowed to view or comment on any of the album resources — even the ones that belong to him. This is because currently there are no policies defined for the `album:object` resource.

Now create a [derived roles](policies/derived%5Froles.html) definition that assigns the `owner` dynamic role to a user if the `owner` attribute of the resource they’re trying to access is equal to their ID.

```sh
cat > cerbos-quickstart/policies/derived_roles_common.yaml <<EOF
---
apiVersion: "api.cerbos.dev/v1"
derivedRoles:
  name: common_roles
  definitions:
    - name: owner
      parentRoles: ["user"]
      condition:
        match:
          expr: request.resource.attr.owner == request.principal.id
EOF
```

Also create a resource policy that gives `owner`s full access to their own albums.

```sh
cat > cerbos-quickstart/policies/resource_album.yaml <<EOF
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: "default"
  importDerivedRoles:
    - common_roles
  resource: "album:object"
  rules:
    - actions: ['*']
      effect: EFFECT_ALLOW
      derivedRoles:
        - owner
EOF
```

Try the request again. This time `bugs_bunny` should be allowed access to his own album but denied access to the album owned by `daffy_duck`.

Request 

```shell
cat <<EOF | curl --silent "http://localhost:3592/api/check/resources?pretty" -d @-
{
  "requestId": "quickstart",
  "principal": {
    "id": "bugs_bunny",
    "roles": [
      "user"
    ],
    "attr": {
      "beta_tester": true
    }
  },
  "resources": [
    {
      "actions": [
        "view:public",
        "comment"
      ],
      "resource": {
        "kind": "album:object",
        "id": "BUGS001",
        "attr": {
          "owner": "bugs_bunny",
          "public": false,
          "flagged": false
        }
      }
    },
    {
      "actions": [
        "view:public",
        "comment"
      ],
      "resource": {
        "kind": "album:object",
        "id": "DAFFY002",
        "attr": {
          "owner": "daffy_duck",
          "public": true,
          "flagged": false
        }
      }
    }
  ]
}
EOF
```

Response

```json
{
  "requestId": "quickstart",
  "results": [
    {
      "resource": {
        "id": "BUGS001",
        "kind": "album:object"
      },
      "actions": {
        "comment": "EFFECT_ALLOW",
        "view:public": "EFFECT_ALLOW"
      }
    },
    {
      "resource": {
        "id": "DAFFY002",
        "kind": "album:object"
      },
      "actions": {
        "comment": "EFFECT_DENY",
        "view:public": "EFFECT_DENY"
      }
    }
  ]
}
```

Now add a rule to the policy to allow users to view public albums.

```sh
cat > cerbos-quickstart/policies/resource_album.yaml <<EOF
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: "default"
  importDerivedRoles:
    - common_roles
  resource: "album:object"
  rules:
    - actions: ['*']
      effect: EFFECT_ALLOW
      derivedRoles:
        - owner

    - actions: ['view:public']
      effect: EFFECT_ALLOW
      roles:
        - user
      condition:
        match:
          expr: request.resource.attr.public == true
EOF
```

If you try the request again, `bugs_bunny` now has `view:public` access to the album owned by `daffy_duck` but not `comment` access. Can you figure out how to update the policy to give him `comment` access as well?

Request and response 

Request

```shell
cat <<EOF | curl --silent "http://localhost:3592/api/check/resources?pretty" -d @-
{
  "requestId": "quickstart",
  "principal": {
    "id": "bugs_bunny",
    "roles": [
      "user"
    ],
    "attr": {
      "beta_tester": true
    }
  },
  "resources": [
    {
      "actions": [
        "view:public",
        "comment"
      ],
      "resource": {
        "kind": "album:object",
        "id": "BUGS001",
        "attr": {
          "owner": "bugs_bunny",
          "public": false,
          "flagged": false
        }
      }
    },
    {
      "actions": [
        "view:public",
        "comment"
      ],
      "resource": {
        "kind": "album:object",
        "id": "DAFFY002",
        "attr": {
          "owner": "daffy_duck",
          "public": true,
          "flagged": false
        }
      }
    }
  ]
}
EOF
```

Response

```json
{
  "requestId": "quickstart",
  "results": [
    {
      "resource": {
        "id": "BUGS001",
        "kind": "album:object"
      },
      "actions": {
        "comment": "EFFECT_ALLOW",
        "view:public": "EFFECT_ALLOW"
      }
    },
    {
      "resource": {
        "id": "DAFFY002",
        "kind": "album:object"
      },
      "actions": {
        "comment": "EFFECT_DENY",
        "view:public": "EFFECT_ALLOW"
      }
    }
  ]
}
```

Once you are done experimenting, the Cerbos server can be stopped with the following command:

```shell
docker kill cerbos
```

Next steps

* [Explore the demo apps built with Cerbos](https://github.com/cerbos?q=demo&type=all&language=&sort=)
* [Read more about Cerbos policies](policies/index.html)
* [Join the Cerbos community on Slack](http://go.cerbos.io/slack)
* [Ask us anything via ](mailto:help@cerbos.dev)[help@cerbos.dev](mailto:help@cerbos.dev)
* [Visit the Cerbos website](https://cerbos.dev)

What is Cerbos?
====================
## [](#%5Fauthorization%5Fas%5Fa%5Fservice)Authorization-as-a-Service

One of the key tenets that allows many successful systems to scale is the adoption of a microservices architecture where each component can be scaled to meet the exact demands of the system.

Cerbos has been built as a standalone service which gives it several characteristics that are desirable for such an architecture

* Authorization checks can be made from any system or part of the app stack. No more complicated logic replicating rules - now it is a single call out to Cerbos which returns a simple ALLOW or DENY response for the request.
* All policy decisions are centralized in the Cerbos instances so there is a single location where audit logs can be gathered from.
* The Cerbos instances can be scaled alongside the rest of your services for example as a Kubernetes sidecar

## [](#%5Fpolicy%5Fas%5Fcode)Policy as Code

Often, as systems grow, the complexity of authorization rules require complicated logic to be translated into each language used and hardcoded into each service in the app stack. Any updates require engineering time to go and change the logic, run tests, and then cut a release of every part of the system which is affected.

Cerbos' approach is to define all policy as human-readable policy definitions held centrally and that is read by all the Cerbos instances. This way any updates or changes to authorization rules can be made once and then all services that call Cerbos for permissions checks get the updated result. No code changes or releases are needed.

## [](#%5Fbring%5Fyour%5Fown%5Fidentity)Bring your own identity

Companies often standardize on using specialised IdPs (identity providers) like [Auth0](https://auth0.com/) for authentication across their suite of applications. This contains the user profile information such as what role the user has, which department they belong to and what office they are based in.

Cerbos can consume an identity from any authentication provider be it homegrown or a managed service and can even natively support JWTs including verification.

This profile information from Auth0 is used to construct the user information (called the principal in Cerbos speak due to supporting not user identities also) which is passed in with an authorization call to make policy decisions with.

## [](#%5Fperformance)Performance

For larger systems, there are often concerns about how performant Cerbos can be given authorization checks are being made in the blocking path of every request. Several key features of Cerbos have quelled these concerns:

* The Cerbos API is exposed over a highly performant [gRPC](api/index.html) interface to keep overheads low (with an HTTP gateway on top).
* A recommended approach is a [sidecar deployment](deployment/k8s-sidecar.html) so that each service instance has its Cerbos instance to keep latency as low as possible - calls can even be made over [UNIX sockets](https://github.com/cerbos/demo-rest/blob/main/docker-compose.yaml).
* Cerbos is advocating a modern cloud-native approach to dealing with common infrastructure services such as authorization. This is a proven method - [Microsoft Dapr](https://docs.microsoft.com/en-us/dotnet/architecture/dapr-for-net-developers/dapr-at-20000-feet) is a good example at scale.

The Cerbos Admin API
====================
The Admin API is an optional component of the Cerbos PDP that must be enabled by setting the `server.adminAPI.enabled` to `true` in the configuration. (See [Admin API configuration](../configuration/server.html#admin-api) for details).

Authentication is mandatory for the Admin API. Currently only basic authentication with a single admin user is supported. If no credentials are configured using the [configuration](../configuration/server.html#admin-api), the default username and password is `cerbos` and `cerbosAdmin`.

| |  Always change the default credentials and enable TLS for the endpoint when enabling the Admin API. See [Server configuration](../configuration/server.html) for more information. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

| |  The Admin API is still under development and might include breaking changes in future releases. |
| -------------------------------------------------------------------------------------------------- |

## [](#%5Faudit%5Flogs)Audit Logs

### [](#%5Flist%5Faudit%5Flog%5Fentries)List Audit Log Entries

GET /admin/auditlog/list/{kind}

When [audit logging is enabled](../configuration/audit.html) you can view the audit log entries using this API endpoint.

There are two kinds of audit logs:

`KIND_ACCESS`

Captured Cerbos API access logs. These records are only available if `accessLogsEnabled` is set to `true` in the [configuration](../configuration/audit.html).

`KIND_DECISION`

Decision logs captured by the engine. These records are only available if `decisionLogsEnabled` is set to `true` in the [configuration](../configuration/audit.html).

Supported filters are:

`tail`

View the last N entries

`between`

View entries captured between two timestamps. The time range is specified by providing two ISO-8601 timestamps using the `between.start` and `between.end` query parameters.

`since`

View entries captured since N hours/minutes/seconds ago

`lookup`

View a specific entry by call ID

View last 5 decision log entries

```shell
curl -k -u cerbos:cerbosAdmin \
    'https://localhost:3592/admin/auditlog/list/KIND_DECISION?tail=5'
```

View decision logs from 2 hours ago up to now

```shell
curl -k -u cerbos:cerbosAdmin \
    'https://localhost:3592/admin/auditlog/list/KIND_DECISION?since=2h'
```

View access log entries between midnight 2021-07-01 and midnight 2021-07-02

```shell
curl -k -u cerbos:cerbosAdmin \
    'https://localhost:3592/admin/auditlog/list/KIND_ACCESS?between.start=2021-07-01T00:00:00Z&between.end=2021-07-02T00:00:00Z'
```

View specific access log entry

```shell
curl -k -u cerbos:cerbosAdmin \
    'https://localhost:3592/admin/auditlog/list/KIND_ACCESS?lookup=01F9VS1N77S83MTSBBX44GYSJ6'
```

## [](#policy-management)Policy Management

### [](#%5Faddupdate%5Fpolicies)Add/update policies

POST /admin/policy
PUT /admin/policy

| |  This endpoint requires a mutable storage driver such as [sqlite3](../configuration/storage.html#sqlite3) to be configured. |
| ----------------------------------------------------------------------------------------------------------------------------- |

Request

```json
{
  "policies": [ (1)
    {
      "apiVersion": "api.cerbos.dev/v1",
      "principalPolicy": {
        "principal": "donald_duck",
        "version": "20210210",
        "rules": [
          {
            "resource": "leave_request",
            "actions": [
              {
                "action": "*",
                "condition": {
                  "match": {
                    "expr": "request.resource.attr.dev_record == true"
                  }
                },
                "effect": "EFFECT_ALLOW"
              }
            ]
          },
          {
            "resource": "salary_record",
            "actions": [
              {
                "action": "*",
                "effect": "EFFECT_DENY"
              }
            ]
          }
        ]
      }
    }
  ]
}
```

| **1** | List of policy definitions |
| ----- | -------------------------- |

Response

```json
{"success":{}}
```

### [](#%5Flist%5Fpolicies)List Policies

GET /admin/policies

Issue a GET request to the endpoint to list the policies available in the store. If the policy store supports filtering, you can optionally pass filter parameters to reduce the result set.

Use `includeDisabled=true` query parameter in order to include disabled policies in the response.

Use `policyId` query parameter to provide a list of policy IDs to be included in the result.

Use `nameRegexp`, `scopeRegexp` and `versionRegexp` to filter using the policy name, scope or version with case insensitive regular expressions.

```shell
curl -k -u cerbos:cerbosAdmin \
    'https://localhost:3592/admin/policies?pretty'
```

```shell
curl -k -u cerbos:cerbosAdmin \
    'https://localhost:3592/admin/policies?pretty&includeDisabled=true&nameRegexp=%5Efoo&scopeRegexp=bar%24&versionRegexp=default'
```

### [](#%5Fget%5Fpolicies)Get Policies

GET /admin/policy?id=policy_id

Issue a GET request to the endpoint with the list of IDs (the `id` query parameter can be repeated multiple times) to retrieve. The list of IDs available in the store can be retrieved using the `ListPolicies` API call described above.

```shell
curl -k -u cerbos:cerbosAdmin \
    'https://localhost:3592/admin/policy?id=x.yaml&id=y.yaml'
```

### [](#%5Finspect%5Fpolicies)Inspect Policies

GET /admin/policies/inspect

Issue a GET request to the endpoint to list actions and variables covered by the policies in the store. If the policy store supports filtering, you can optionally pass filter parameters to reduce the result set.

Use `includeDisabled=true` query parameter in order to include disabled policies in the response.

Use `policyId` query parameter to provide a list of policy IDs to inspect.

Use `nameRegexp`, `scopeRegexp` and `versionRegexp` to filter using the policy name, scope or version with case-insensitive regular expressions.

```shell
curl -k -u cerbos:cerbosAdmin \
    'https://localhost:3592/admin/policies/inspect'
```

```shell
curl -k -u cerbos:cerbosAdmin \
    'https://localhost:3592/admin/policies/inspect?policyId=x.yaml&policyId=y.yaml
```

```shell
curl -k -u cerbos:cerbosAdmin \
    'https://localhost:3592/admin/policies/inspect?includeDisabled=true&nameRegexp=%5Efoo&scopeRegexp=bar%24&versionRegexp=default'
```

### [](#delete-policies)Delete Policies

POST   /admin/policy/delete?id=policy_id

| |  This endpoint requires a mutable storage driver such as [sqlite3](../configuration/storage.html#sqlite3) to be configured. |
| ----------------------------------------------------------------------------------------------------------------------------- |

Issue a POST request to the endpoint with the list of IDs (the `id` query parameter can be repeated multiple times) to delete. IDs follow the same format as the output of `ListPolicies` (`<kind>.<name>.v<version>/<scope>`). For example, a resource policy for `leave_request` with version `default` and scope `acme.hr` would have the ID `resource.leave_request.vdefault/acme.hr`.

curl -k -u cerbos:cerbosAdmin -X POST \
    'https://localhost:3592/admin/policy/delete?id=principal.donald_duck.vdefault&id=derived_roles.my_derived_roles'

Response

```json
{
  "deletedPolicies": 2 (1)
}
```

| **1** | Number of policies deleted |
| ----- | -------------------------- |

### [](#disable-policies)Disable Policies

POST   /admin/policy/disable?id=policy_id
PUT    /admin/policy/disable?id=policy_id
DELETE /admin/policy?id=policy_id [DEPRECATED]

| |  This endpoint requires a mutable storage driver such as [sqlite3](../configuration/storage.html#sqlite3) to be configured. |
| ----------------------------------------------------------------------------------------------------------------------------- |

Issue a POST request to the endpoint with the list of IDs (the `id` query parameter can be repeated multiple times) to disable. IDs follow the same format as the output of `ListPolicies` (`<kind>.<name>.v<version>/<scope>`). For example, a resource policy for `leave_request` with version `default` and scope `acme.hr` would have the ID `resource.leave_request.vdefault/acme.hr`.

curl -k -u cerbos:cerbosAdmin -X POST \
    'https://localhost:3592/admin/policy/disable?id=principal.donald_duck.vdefault&id=derived_roles.my_derived_roles'

Response

```json
{
  "disabledPolicies": 2 (1)
}
```

| **1** | Number of policies disabled |
| ----- | --------------------------- |

### [](#enable-policies)Enable Policies

POST /admin/policy/enable?id=policy_id
PUT  /admin/policy/enable?id=policy_id

| |  This endpoint requires a mutable storage driver such as [sqlite3](../configuration/storage.html#sqlite3) to be configured. |
| ----------------------------------------------------------------------------------------------------------------------------- |

Issue a POST request to the endpoint with the list of IDs (the `id` query parameter can be repeated multiple times) to enable. IDs follow the same format as the output of `ListPolicies` (`<kind>.<name>.v<version>/<scope>`). For example, a resource policy for `leave_request` with version `default` and scope `acme.hr` would have the ID `resource.leave_request.vdefault/acme.hr`.

curl -k -u cerbos:cerbosAdmin -X POST \
    'https://localhost:3592/admin/policy/enable?id=principal.donald_duck.vdefault&id=derived_roles.my_derived_roles'

Response

```json
{
  "enabledPolicies": 2 (1)
}
```

| **1** | Number of policies enabled |
| ----- | -------------------------- |

## [](#%5Fschema%5Fmanagement)Schema Management

### [](#%5Faddupdate%5Fschemas)Add/update schemas

POST /admin/schema
PUT /admin/schema

| |  This endpoint requires a mutable storage driver such as [sqlite3](../configuration/storage.html#sqlite3) to be configured. |
| ----------------------------------------------------------------------------------------------------------------------------- |

Request

```json
{
  "schemas": [ (1)
    {
      "id": "principal.json",
      "definition": "ewogICIkc2NoZW1hIjogImh0dHBzOi8vanNvbi1zY2hlbWEub3JnL2RyYWZ0LzIwMjAtMTIvc2NoZW1hIiwKICAidHlwZSI6ICJvYmplY3QiLAogICJwcm9wZXJ0aWVzIjogewogICAgImRlcGFydG1lbnQiOiB7CiAgICAgICJ0eXBlIjogInN0cmluZyIsCiAgICAgICJlbnVtIjogWwogICAgICAgICJtYXJrZXRpbmciLAogICAgICAgICJlbmdpbmVlcmluZyIKICAgICAgXQogICAgfSwKICAgICJnZW9ncmFwaHkiOiB7CiAgICAgICJ0eXBlIjogInN0cmluZyIKICAgIH0sCiAgICAidGVhbSI6IHsKICAgICAgInR5cGUiOiAic3RyaW5nIgogICAgfSwKICAgICJtYW5hZ2VkX2dlb2dyYXBoaWVzIjogewogICAgICAidHlwZSI6ICJzdHJpbmciCiAgICB9LAogICAgIm9yZ0lkIjogewogICAgICAidHlwZSI6ICJzdHJpbmciCiAgICB9LAogICAgImpvYlJvbGVzIjogewogICAgICAidHlwZSI6ICJhcnJheSIsCiAgICAgICJpdGVtcyI6IHsKICAgICAgICAgICJ0eXBlIjogInN0cmluZyIKICAgICAgfQogICAgfSwKICAgICJ0YWdzIjogewogICAgICAidHlwZSI6ICJvYmplY3QiLAogICAgICAicHJvcGVydGllcyI6IHsKICAgICAgICAiYnJhbmRzIjogewogICAgICAgICAgInR5cGUiOiAiYXJyYXkiLAogICAgICAgICAgIml0ZW1zIjogewogICAgICAgICAgICAgICJ0eXBlIjogInN0cmluZyIKICAgICAgICAgIH0KICAgICAgICB9LAogICAgICAgICJjbGFzc2VzIjogewogICAgICAgICAgInR5cGUiOiAiYXJyYXkiLAogICAgICAgICAgIml0ZW1zIjogewogICAgICAgICAgICAgICJ0eXBlIjogInN0cmluZyIKICAgICAgICAgIH0KICAgICAgICB9LAogICAgICAgICJyZWdpb25zIjogewogICAgICAgICAgInR5cGUiOiAiYXJyYXkiLAogICAgICAgICAgIml0ZW1zIjogewogICAgICAgICAgICAgICJ0eXBlIjogInN0cmluZyIKICAgICAgICAgIH0KICAgICAgICB9CiAgICAgIH0KICAgIH0KICB9LAogICJyZXF1aXJlZCI6IFsKICAgICJkZXBhcnRtZW50IiwKICAgICJnZW9ncmFwaHkiLAogICAgInRlYW0iCiAgXQp9Cg==" (2)
    }
  ]
}
```

| **1** | List of schema definitions                                      |
| ----- | --------------------------------------------------------------- |
| **2** | base64 encoded [JSON schema](http://json-schema.org) definition |

Response

```json
{}
```

### [](#%5Flist%5Fschemas)List schemas

GET /admin/schemas

Issue a GET request to the endpoint to list the schemas available in the store.

| |  Only the schema IDs will be returned from this request. Use the GetSchema endpoint to retrieve the full definition of a schema. |
| ---------------------------------------------------------------------------------------------------------------------------------- |

```shell
curl -k -u cerbos:cerbosAdmin \
    'https://localhost:3592/admin/schemas'
```

Response

```json
{
    "schemaIds": [ (1)
        "principal.json",
        "leave_request.json"
    ]
}
```

| **1** | List of schema ids |
| ----- | ------------------ |

### [](#%5Fget%5Fschemas)Get schema(s)

GET /admin/schema

Issue a GET request to the endpoint to get the schema(s) stated in the query parameters.

```shell
curl -k -u cerbos:cerbosAdmin \
    'https://localhost:3592/admin/schema?id=principal.json&id=leave_request.json'
```

Response

```json
{
    "schemas": [ (1)
        {
            "id": "principal.json",
            "definition": "ewogICIkc2NoZW1hIjogImh0dHBzOi8vanNvbi1zY2hlbWEub3JnL2RyYWZ0LzIwMjAtMTIvc2NoZW1hIiwKICAidHlwZSI6ICJvYmplY3QiLAogICJwcm9wZXJ0aWVzIjogewogICAgImRlcGFydG1lbnQiOiB7CiAgICAgICJ0eXBlIjogInN0cmluZyIsCiAgICAgICJlbnVtIjogWwogICAgICAgICJtYXJrZXRpbmciLAogICAgICAgICJlbmdpbmVlcmluZyIKICAgICAgXQogICAgfSwKICAgICJnZW9ncmFwaHkiOiB7CiAgICAgICJ0eXBlIjogInN0cmluZyIKICAgIH0sCiAgICAidGVhbSI6IHsKICAgICAgInR5cGUiOiAic3RyaW5nIgogICAgfSwKICAgICJtYW5hZ2VkX2dlb2dyYXBoaWVzIjogewogICAgICAidHlwZSI6ICJzdHJpbmciCiAgICB9LAogICAgIm9yZ0lkIjogewogICAgICAidHlwZSI6ICJzdHJpbmciCiAgICB9LAogICAgImpvYlJvbGVzIjogewogICAgICAidHlwZSI6ICJhcnJheSIsCiAgICAgICJpdGVtcyI6IHsKICAgICAgICAgICJ0eXBlIjogInN0cmluZyIKICAgICAgfQogICAgfSwKICAgICJ0YWdzIjogewogICAgICAidHlwZSI6ICJvYmplY3QiLAogICAgICAicHJvcGVydGllcyI6IHsKICAgICAgICAiYnJhbmRzIjogewogICAgICAgICAgInR5cGUiOiAiYXJyYXkiLAogICAgICAgICAgIml0ZW1zIjogewogICAgICAgICAgICAgICJ0eXBlIjogInN0cmluZyIKICAgICAgICAgIH0KICAgICAgICB9LAogICAgICAgICJjbGFzc2VzIjogewogICAgICAgICAgInR5cGUiOiAiYXJyYXkiLAogICAgICAgICAgIml0ZW1zIjogewogICAgICAgICAgICAgICJ0eXBlIjogInN0cmluZyIKICAgICAgICAgIH0KICAgICAgICB9LAogICAgICAgICJyZWdpb25zIjogewogICAgICAgICAgInR5cGUiOiAiYXJyYXkiLAogICAgICAgICAgIml0ZW1zIjogewogICAgICAgICAgICAgICJ0eXBlIjogInN0cmluZyIKICAgICAgICAgIH0KICAgICAgICB9CiAgICAgIH0KICAgIH0KICB9LAogICJyZXF1aXJlZCI6IFsKICAgICJkZXBhcnRtZW50IiwKICAgICJnZW9ncmFwaHkiLAogICAgInRlYW0iCiAgXQp9Cg=="
        },
        {
            "id": "leave_request.json",
            "definition": "ewogICIkc2NoZW1hIjogImh0dHBzOi8vanNvbi1zY2hlbWEub3JnL2RyYWZ0LzIwMjAtMTIvc2NoZW1hIiwKICAidHlwZSI6ICJvYmplY3QiLAogICJwcm9wZXJ0aWVzIjogewogICAgImRlcGFydG1lbnQiOiB7CiAgICAgICJ0eXBlIjogInN0cmluZyIsCiAgICAgICJlbnVtIjogWwogICAgICAgICJtYXJrZXRpbmciLAogICAgICAgICJlbmdpbmVlcmluZyIKICAgICAgXQogICAgfSwKICAgICJnZW9ncmFwaHkiOiB7CiAgICAgICJ0eXBlIjogInN0cmluZyIKICAgIH0sCiAgICAidGVhbSI6IHsKICAgICAgInR5cGUiOiAic3RyaW5nIgogICAgfSwKICAgICJpZCI6IHsKICAgICAgInR5cGUiOiAic3RyaW5nIgogICAgfSwKICAgICJvd25lciI6IHsKICAgICAgInR5cGUiOiAic3RyaW5nIgogICAgfSwKICAgICJzdGF0dXMiOiB7CiAgICAgICJ0eXBlIjogInN0cmluZyIKICAgIH0sCiAgICAiZGV2X3JlY29yZCI6IHsKICAgICAgInR5cGUiOiAiYm9vbGVhbiIKICAgIH0KICB9LAogICJyZXF1aXJlZCI6IFsKICAgICJkZXBhcnRtZW50IiwKICAgICJnZW9ncmFwaHkiLAogICAgInRlYW0iLAogICAgImlkIgogIF0KfQo="
        }
    ]
}
```

| **1** | List of schemas |
| ----- | --------------- |

### [](#%5Fdelete%5Fschemas)Delete schema(s)

DELETE /admin/schema

Issue a DELETE request to the endpoint to delete the schema(s) stated in the query parameters.

```shell
curl -k -u cerbos:cerbosAdmin -X DELETE \
    'https://localhost:3592/admin/schema?id=principal.json&id=leave_request.json'
```

Response

```json
{
  "deletedSchemas": 2 (1)
}
```

| **1** | Number of schemas deleted |
| ----- | ------------------------- |

## [](#store-management)Store Management

### [](#%5Fpurge%5Fstore%5Frevisions)Purge store revisions

DELETE /admin/store/revisions

Issue a DELETE request to the endpoint to delete rows from the `policy_revision` table.

Use `keepLast=N` query parameter to keep the last N revisions for each policy. If not specified, the entire table will be truncated.

Purge the store revisions

```shell
curl -k -u cerbos:cerbosAdmin -X DELETE \
    'https://localhost:3592/admin/store/revisions'
```

Response

```json
{}
```

| |  This endpoint requires a mutable storage driver such as [sqlite3](../configuration/storage.html#sqlite3) to be configured. |
| ----------------------------------------------------------------------------------------------------------------------------- |

### [](#%5Freload%5Fstore)Reload store

GET /admin/store/reload

Issue a GET request to the endpoint to force a reload of the store.

Reload the store

```shell
curl -k -u cerbos:cerbosAdmin -X GET \
    'https://localhost:3592/admin/store/reload'
```

Reload the store and block until it finishes

```shell
curl -k -u cerbos:cerbosAdmin -X GET \
    'https://localhost:3592/admin/store/reload?wait=true'
```

Response

```json
{}
```

| |  This endpoint requires a reloadable storage driver such as [blob](../configuration/storage.html#blob), [disk](../configuration/storage.html#disk) and [git](../configuration/storage.html#git) to be configured. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The Cerbos API
====================
The main API endpoint for making policy decisions is the [/api/check/resources REST endpoint](#check-resources) (`cerbos.svc.v1.CerbosService/CheckResources` RPC in the gRPC API). You can browse a [static version of the Cerbos OpenAPI specification on this site](%5Fattachments/cerbos-api.html). To interactively explore the API, launch a Cerbos instance and access the root directory of the HTTP endpoint using a browser.

```sh
docker run --rm --name cerbos -p 3592:3592 -p 3593:3593 ghcr.io/cerbos/cerbos:0.51.0
```

Navigate to <http://localhost:3592/> using your browser to explore the Cerbos API documentation.

Alternatively, you can explore the API using the following methods as well:

* Using an OpenAPI-compatible software like [Postman](https://www.postman.com) or [Insomnia](https://insomnia.rest) to explore the Cerbos OpenAPI spec available at <http://localhost:3592/schema/swagger.json>.
* Using [grpcurl](https://github.com/fullstorydev/grpcurl) or any other tool that supports [gRPC server reflection](https://github.com/grpc/grpc/blob/master/doc/server-reflection.md) API to explore the gRPC API exposed on port 3593.

## [](#%5Fclient%5Fsdks)Client SDKs

* [![Go](_images/go.svg)](https://pkg.go.dev/github.com/cerbos/cerbos-sdk-go/cerbos)[ Go](https://pkg.go.dev/github.com/cerbos/cerbos-sdk-go/cerbos)
* [![Java](_images/java.svg)](https://github.com/cerbos/cerbos-sdk-java)[ Java](https://github.com/cerbos/cerbos-sdk-java)
* [![JavaScript](_images/javascript.svg)](https://github.com/cerbos/cerbos-sdk-javascript)[ JavaScript](https://github.com/cerbos/cerbos-sdk-javascript)
* [![.NET](_images/dot-net.svg)](https://github.com/cerbos/cerbos-sdk-net)[ .NET](https://github.com/cerbos/cerbos-sdk-net)
* [![Laravel](_images/laravel.svg)](https://github.com/cerbos/cerbos-sdk-laravel)[ Laravel](https://github.com/cerbos/cerbos-sdk-laravel)
* [![PHP](_images/php.svg)](https://github.com/cerbos/cerbos-sdk-php)[ PHP](https://github.com/cerbos/cerbos-sdk-php)
* [![Python](_images/python.svg)](https://github.com/cerbos/cerbos-sdk-python)[ Python](https://github.com/cerbos/cerbos-sdk-python)
* [![Ruby](_images/ruby.svg)](https://github.com/cerbos/cerbos-sdk-ruby)[ Ruby](https://github.com/cerbos/cerbos-sdk-ruby)
* [![Rust](_images/rust.svg)](https://github.com/cerbos/cerbos-sdk-rust)[ Rust](https://github.com/cerbos/cerbos-sdk-rust)

Other languages coming soon

## [](#%5Fdemos)Demos

| |  Demos are constantly being added or updated by the Cerbos team. Visit <https://github.com/orgs/cerbos/repositories?language=&q=demo&sort=&type=all> for the latest list. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

* [Application (Python)](https://github.com/cerbos/demo-python)
* [GraphQL Service (NodeJS)](https://github.com/cerbos/demo-graphql)
* [REST Service (Go)](https://github.com/cerbos/demo-rest)

Get help

* [Join the Cerbos community on Slack](http://go.cerbos.io/slack)
* [Email us at ](mailto:help@cerbos.dev)[help@cerbos.dev](mailto:help@cerbos.dev)

## [](#%5Frequest%5Fand%5Fresponse%5Fformats)Request and response formats

### [](#check-resources)`CheckResources` (`/api/check/resources`)

This is the main API entrypoint for checking permissions for a set of resources.

Request

```json
{
  "requestId": "test", (1)
  "principal": {
    "id": "alice", (2)
    "policyVersion": "20210210", (3)
    "scope": "acme.corp", (4)
    "roles": [ (5)
      "employee"
    ],
    "attr": { (6)
      "department": "accounting",
      "geography": "GB",
      "team": "design"
    }
  },
  "resources": [ (7)
    {
      "resource": {
        "id": "XX125", (8)
        "kind": "leave_request", (9)
        "policyVersion": "20210210", (10)
        "scope": "acme.corp", (11)
        "attr": { (12)
          "department": "accounting",
          "geography": "GB",
          "id": "XX125",
          "owner": "john",
          "team": "design"
        }
      },
      "actions": [ (13)
        "view:public",
        "approve",
        "create"
      ]
    }
  ],
  "auxData": { (14)
    "jwt": {
        "token": "xxx.yyy.zzz", (15)
        "keySetId": "ks1" (16)
    }
  },
  "includeMeta": true (17)
}
```

| **1**  | Request ID is an optional, application-provided identifier useful for correlating logs.                                                                                                                  |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2**  | ID of the principal whose permissions are being checked. This usually comes from the identity provider (IdP).                                                                                            |
| **3**  | Principal policy version. Optional. The server falls back to the [configured default version](../configuration/engine.html) if this is not specified.                                                    |
| **4**  | Principal policy scope. Optional. See [Scoped policies](../policies/scoped%5Fpolicies.html).                                                                                                             |
| **5**  | The roles attached to this principal by the identity provider.                                                                                                                                           |
| **6**  | Free-form context data about this principal. Policy rule conditions are evaluated based on these values.                                                                                                 |
| **7**  | List of resources the principal is attempting to access. Up to 50 resources may be provided in a single request by default. This [limit can be configured](../configuration/server.html#request-limits). |
| **8**  | ID of the resource.                                                                                                                                                                                      |
| **9**  | Resource kind. This is used to determine the resource policy that applies to this resource.                                                                                                              |
| **10** | Resource policy version. Optional. The server falls back to the [configured default version](../configuration/engine.html) if this is not specified.                                                     |
| **11** | Resource policy scope. Optional. See [Scoped policies](../policies/scoped%5Fpolicies.html).                                                                                                              |
| **12** | Free-form context data about this resource. Policy rule conditions are evaluated based on these values.                                                                                                  |
| **13** | List of actions being performed on the resource. Up to 50 actions per resource may be provided by default. This [limit can be configured](../configuration/server.html#request-limits).                  |
| **14** | Optional section for providing auxiliary data.                                                                                                                                                           |
| **15** | JWT to use as an auxiliary data source.                                                                                                                                                                  |
| **16** | ID of the keyset to use to verify the JWT. Optional if only a single [keyset is configured](../configuration/auxdata.html).                                                                              |
| **17** | Optional flag to receive metadata about request evaluation.                                                                                                                                              |

Response

```json
{
  "requestId": "test", (1)
  "results": [ (2)
    {
      "resource": { (3)
        "id": "XX125",
        "kind": "leave_request",
        "policyVersion": "20210210",
        "scope": "acme.corp"
      },
      "actions": { (4)
        "view:public": "EFFECT_ALLOW",
        "approve": "EFFECT_DENY"
      },
      "outputs": [ (5)
        {
          "src": "resource.leave_request.v20210210/acme#rule-001", (6)
          "val": "create_allowed:john" (7)
        },
        {
          "src": "resource.leave_request.v20210210#public-view",
          "val": {
            "id": "john",
            "keys": ["foo", "bar", "baz"]
          }
        }
      ],
      "validationErrors": [ (8)
        {
          "path": "/department",
          "message": "value must be one of \"marketing\", \"engineering\"",
          "source": "SOURCE_PRINCIPAL"
        },
        {
          "path": "/department",
          "message": "value must be one of \"marketing\", \"engineering\"",
          "source": "SOURCE_RESOURCE"
        }
      ],
      "meta": { (9)
        "actions": {
          "view:public": {
            "matchedPolicy": "resource.leave_request.v20210210/acme.corp", (10)
            "matchedScope": "acme" (11)
          },
          "approve": {
            "matchedPolicy": "resource.leave_request.v20210210/acme.corp"
          }
        },
        "effectiveDerivedRoles": [ (12)
          "employee_that_owns_the_record",
          "any_employee"
        ]
      }
    }
  ],
  "cerbosCallId": "01HHENANTHFD5DV3HZGDKB87PJ" (13)
}
```

| **1**  | Request ID that was sent with the request.                                                                                    |
| ------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **2**  | List of results. Items are in the same order as they were sent in the request.                                                |
| **3**  | Resource identifiers.                                                                                                         |
| **4**  | Access decisions for each of the actions.                                                                                     |
| **5**  | List of outputs from policy evaluation, if there are any. See [Outputs](../policies/outputs.html).                            |
| **6**  | Name of the rule that produced the output.                                                                                    |
| **7**  | Output value produced by the rule.                                                                                            |
| **8**  | Validation errors, if [schema enforcement](../policies/schemas.html) is enabled and the request didn’t conform to the schema. |
| **9**  | Metadata (if includeMeta was true in the request)                                                                             |
| **10** | Name of the policy that produced the decision for this action.                                                                |
| **11** | Name of the scope that was active when the decision was made for the action.                                                  |
| **12** | List of derived roles that were activated.                                                                                    |
| **13** | The call ID generated by Cerbos and stored in the audit log for this request.                                                 |

### [](#resources-query-plan)`PlanResources` (`/api/plan/resources`)

Produces a query plan that can be used to obtain a list of resources that a principal is allowed to perform a particular action on.

Request

```json
{
  "requestId":  "test01", (1)
  "action":  "approve", (2)
  "actions":  ["approve", "view"], (3)
  "resource":  {
    "policyVersion": "dev", (4)
    "kind":  "leave_request", (5)
    "scope": "acme.corp", (6)
    "attr":  { (7)
      "owner":  "alicia"
    }
  },
  "principal":  {
    "id":  "alicia", (8)
    "policyVersion": "dev", (9)
    "scope": "acme.corp", (10)
    "roles":  ["user"], (11)
    "attr": { (12)
      "geography": "GB"
    }
  },
  "includeMeta": true, (13)
  "auxData": { (14)
    "jwt": {
      "token": "xxx.yyy.zzz", (15)
      "keySetId": "ks-1" (16)
    }
  }
}
```

| **1**  | Request ID can be anything that uniquely identifies a request.                                                                                                                                                                                                                                                                                                                                                   |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2**  | Action being performed on the resource instances. Either <2> or <3> is required.                                                                                                                                                                                                                                                                                                                                 |
| **3**  | Actions being performed on the resource instances. The query plan is the logical AND of individual query plans for each action. Either <2> or <3> is required.                                                                                                                                                                                                                                                   |
| **4**  | Resource policy version. Optional. The server falls back to the [configured default version](../configuration/engine.html) if this is not specified.                                                                                                                                                                                                                                                             |
| **5**  | Resource kind. Required. This value is used to determine the resource policy to evaluate.                                                                                                                                                                                                                                                                                                                        |
| **6**  | Resource scope. Optional. See [Scoped policies](../policies/scoped%5Fpolicies.html).                                                                                                                                                                                                                                                                                                                             |
| **7**  | Free-form context data about the resources under consideration. The object holds all attributes known about the resource at the time the request. Optional. Policy rule conditions will be (partially) evaluated based on these values. If an effective policy rule condition(s) requires a resource attribute not present in this object, then the response will contain the condition(s) abstract syntax tree. |
| **8**  | ID of the principal performing the actions. Required.                                                                                                                                                                                                                                                                                                                                                            |
| **9**  | Principal policy version. Optional. The server falls back to the [configured default version](../configuration/engine.html) if this is not specified.                                                                                                                                                                                                                                                            |
| **10** | Principal scope. Optional. See [Scoped policies](../policies/scoped%5Fpolicies.html).                                                                                                                                                                                                                                                                                                                            |
| **11** | Static roles that are assigned to this principal by your identity management system. Required.                                                                                                                                                                                                                                                                                                                   |
| **12** | Free-form context data about this principal. Policy rule conditions are evaluated based on these values.                                                                                                                                                                                                                                                                                                         |
| **13** | An optional flag to signal that the response should include metadata about evaluation. Useful for debugging.                                                                                                                                                                                                                                                                                                     |
| **14** | Optional section for providing auxiliary data.                                                                                                                                                                                                                                                                                                                                                                   |
| **15** | JWT to use as an auxiliary data source.                                                                                                                                                                                                                                                                                                                                                                          |
| **16** | ID of the keyset to use to verify the JWT. Optional if only a single [keyset is configured](../configuration/auxdata.html).                                                                                                                                                                                                                                                                                      |

Response

```json
{
  "requestId": "test01",
  "action": "approve",
  "resourceKind": "leave_request",
  "policyVersion": "dev",
  "filter": {
    "kind": "KIND_CONDITIONAL", (1)
    "condition": { (2)
        "expression":  {
          "operator":  "eq",
          "operands":  [
            { "variable":  "request.resource.attr.status" },
            { "value":  "PENDING_APPROVAL" }
          ]
        }
    }
  },
  "meta": {
    "filterDebug": "(request.resource.attr.status == \"PENDING_APPROVAL\")" (3)
  },
  "cerbosCallId": "01HHENANTHFD5DV3HZGDKB87PJ" (4)
}
```

| **1** | Filter kind can be KIND\_ALWAYS\_ALLOWED, KIND\_ALWAYS\_DENIED or KIND\_CONDITIONAL. See below for description of what these values mean.         |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Populated only if kind is KIND\_CONDITIONAL. Contains the abstract syntax tree (AST) of the condition that must be satisfied to allow the action. |
| **3** | Condition AST represented as a human readable string. Useful for debugging.                                                                       |
| **4** | The call ID generated by Cerbos and stored in the audit log for this request.                                                                     |

#### [](#%5Fstructure%5Fof%5Fthe%5Ffilter%5Fblock)Structure of the `filter` block

The `kind` field defines the filter kind.

`KIND_ALWAYS_ALLOWED`

The principal is unconditionally allowed to perform the action

`KIND_ALWAYS_DENIED`

The principal is unconditionally not permitted to perfrom the action

`KIND_CONDITIONAL`

The principal is allowed to perform the action if the condition is satisfied

The `condition` field holds the AST of the condition that must be satisfied. It is rooted in an expression that has an `operator` (e.g. equals, greater than) and `operands` (e.g. a constant value, a variable or another expression).

__Common Operators__
| Operator | Description                |
| -------- | -------------------------- |
| add      | Addition (+)               |
| and      | Logical AND (&&)           |
| div      | Division (/)               |
| eq       | Equality (==)              |
| ge       | Greater than or equal (>=) |
| gt       | Greater than (>)           |
| in       | List membership (in)       |
| index    | Array or map index         |
| lambda   | Anonymous function         |
| le       | Less than or equal (⇐)     |
| list     | List constructor           |
| lt       | Less than (<)              |
| mod      | Modulo (%)                 |
| mult     | Multiplication (\*)        |
| ne       | Not equal (!=)             |
| not      | Logical NOT                |
| or       | Logical OR                 |
| sub      | Subtract (-)               |

Example: `request.resource.attr.status == "PENDING_APPROVAL"`

```json
{
  "expression": {
    "operator": "eq",
    "operands": [
      {
        "variable": "request.resource.attr.status"
      },
      {
        "value": "PENDING_APPROVAL"
      }
    ]
  }
}
```

Example: `(request.resource.attr.department == "marketing") && (request.resource.attr.team != "design")`

```json
{
  "expression": {
    "operator": "and",
    "operands": [
      {
        "expression": {
          "operator": "eq",
          "operands": [
            {
              "variable": "request.resource.attr.department"
            },
            {
              "value": "marketing"
            }
          ]
        }
      },
      {
        "expression": {
          "operator": "ne",
          "operands": [
            {
              "variable": "request.resource.attr.team"
            },
            {
              "value": "design"
            }
          ]
        }
      }
    ]
  }
}
```

Example: `request.resource.attr.values.filter(t, t > 0)`

```json
{
  "expression": {
    "operator": "filter",
    "operands": [
      {
        "variable": "request.resource.attr.values"
      },
      {
        "expression": {
          "operator": "lambda",
          "operands": [
            {
              "variable": "t"
            },
            {
              "expression": {
                "operator": "gt",
                "operands": [
                  {
                    "variable": "t"
                  },
                  {
                    "value": 0
                  }
                ]
              }
            }
          ]
        }
      }
    ]
  }
}
```

#### [](#%5Fquery%5Fplan%5Fadapters)Query plan adapters

Rather than interpreting the condition AST directly, Cerbos provides reference implementations of query plan adapters that convert the `PlanResources` response into a native filter for your data layer. These adapters serve as a starting point — use them as-is or adapt them to your application’s requirements. Reference implementations are available for Prisma, Drizzle, Mongoose, Convex, LangChain/ChromaDB, and SQLAlchemy.

See [Query plan adapters](../recipes/query-plan-adapters/index.html) for installation, usage, and operator support details.

### [](#server-info)`ServerInfo` (`/api/server_info`)

Returns Cerbos server version.

Response

```json
{
  "version": "0.25.0",
  "commit": "6b5a051a160398a3c04370f742e6090fab2ed0b8",
  "buildDate": "2023-02-13T09:31:48Z"
}
```

## [](#authzen)Request and response formats (AuthZEN Authorization API)

Cerbos partially implements the [OpenID AuthZEN Authorization API specification](https://openid.github.io/authzen/), providing a standardized way to make authorization decisions. The AuthZEN API uses a simplified entity model that maps to Cerbos’s native authorization model.

### [](#authzen-entity-model)AuthZEN entity model mapping

The AuthZEN specification uses a simplified entity model with three core entities:

* **Subject**: The principal requesting access (maps to Cerbos `principal`)
* **Resource**: The target of the access request (maps to Cerbos `resource`)
* **Action**: The operation being performed (maps to Cerbos `actions`)

#### [](#%5Fmapping%5Fauthzen%5Fto%5Fcerbos)Mapping AuthZEN to Cerbos

AuthZEN entities are mapped to Cerbos CheckResources requests as follows:

**Subject → Principal**

| AuthZEN Field                           | Cerbos Field            | Notes                                                 |
| --------------------------------------- | ----------------------- | ----------------------------------------------------- |
| subject.type                            | \-                      | Informational field describing the type of subject    |
| subject.id                              | principal.id            | Unique identifier for the principal                   |
| subject.properties.cerbos.roles         | principal.roles         | Array of role names assigned by the identity provider |
| subject.properties.cerbos.policyVersion | principal.policyVersion | Policy version to use for the principal               |
| subject.properties.cerbos.scope         | principal.scope         | Policy scope for the principal                        |
| subject.properties.\*                   | principal.attr.\*       | All other properties become principal attributes      |

**Resource → Resource**

| AuthZEN Field                            | Cerbos Field           | Notes                                              |
| ---------------------------------------- | ---------------------- | -------------------------------------------------- |
| resource.type                            | resource.kind          | Type of resource (determines which policy applies) |
| resource.id                              | resource.id            | Unique identifier for the resource                 |
| resource.properties.cerbos.policyVersion | resource.policyVersion | Policy version to use for the resource             |
| resource.properties.cerbos.scope         | resource.scope         | Policy scope for the resource                      |
| resource.properties.\*                   | resource.attr.\*       | All other properties become resource attributes    |

**Action → Actions**

| AuthZEN Field     | Cerbos Field | Notes                                                    |
| ----------------- | ------------ | -------------------------------------------------------- |
| action.name       | actions\[0\] | Action name added as the first item in the actions array |
| action.properties | \-           | Reserved for future use                                  |

**Context**

| AuthZEN Field              | Cerbos Field | Notes                                                        |
| -------------------------- | ------------ | ------------------------------------------------------------ |
| context.cerbos.requestId   | requestId    | Application-provided correlation identifier                  |
| context.cerbos.auxData     | auxData      | Auxiliary data such as JWT tokens                            |
| context.cerbos.includeMeta | \-           | Controls whether full Cerbos response is included in context |

### [](#authzen-metadata)`Metadata` (`/.well-known/authzen-configuration`)

Returns metadata about the Cerbos Policy Decision Point, including endpoint URLs for accessing the AuthZEN APIs.

Request

This endpoint accepts GET requests with no body.

Response

```json
{
  "policy_decision_point": "https://localhost:3592", (1)
  "access_evaluation_endpoint": "https://localhost:3592/access/v1/evaluation", (2)
  "access_evaluations_endpoint": "https://localhost:3592/access/v1/evaluations" (3)
}
```

| **1** | Base URL of the Policy Decision Point            |
| ----- | ------------------------------------------------ |
| **2** | Full URL for single access evaluation request    |
| **3** | Full URL for multiple access evaluation requests |

### [](#authzen-access-evaluation)`Access Evaluation` (`/access/v1/evaluation`)

Evaluates whether a subject can perform a single action on a single resource according to the AuthZEN specification.

Request

```json
{
  "subject": { (1)
    "type": "user", (2)
    "id": "donald_duck", (3)
    "properties": { (4)
      "cerbos.policyVersion": "20210210",
      "cerbos.roles": ["employee"],
      "department": "marketing",
      "geography": "GB",
      "team": "design"
    }
  },
  "resource": { (5)
    "type": "leave_request", (6)
    "id": "XX125", (7)
    "properties": { (8)
      "cerbos.policyVersion": "20210210",
      "department": "marketing",
      "geography": "GB",
      "owner": "john",
      "team": "design"
    }
  },
  "action": { (9)
    "name": "view:public", (10)
    "properties": {} (11)
  },
  "context": { (12)
    "cerbos.requestId": "test",
    "cerbos.auxData": { (13)
      "jwt": {
        "token": "xxx.yyy.zzz"
      }
    },
    "cerbos.includeMeta": true (14)
  }
}
```

| **1**  | Subject requesting access (maps to Cerbos principal)                                                                       |
| ------ | -------------------------------------------------------------------------------------------------------------------------- |
| **2**  | Type of the subject (informational field)                                                                                  |
| **3**  | Unique identifier for the subject                                                                                          |
| **4**  | Properties about the subject. Special cerbos.\* properties are mapped to Cerbos-specific fields, others become attributes  |
| **5**  | Resource being accessed (maps to Cerbos resource)                                                                          |
| **6**  | Type of the resource (maps to Cerbos resource.kind)                                                                        |
| **7**  | Unique identifier for the resource                                                                                         |
| **8**  | Properties about the resource. Special cerbos.\* properties are mapped to Cerbos-specific fields, others become attributes |
| **9**  | Action being performed                                                                                                     |
| **10** | Name of the action to check                                                                                                |
| **11** | Optional properties about the action (currently unused)                                                                    |
| **12** | Environmental/contextual data                                                                                              |
| **13** | Auxiliary data such as JWT tokens. See [CheckResources (/api/check/resources)](#check-resources) for details               |
| **14** | Include metadata about evaluation in the response (Cerbos extension)                                                       |

Response

```json
{
  "decision": true, (1)
  "context": { (2)
    "cerbos.response": { (3)
      "requestId": "test",
      "results": [
        {
          "resource": {
            "id": "XX125",
            "kind": "leave_request",
            "policyVersion": "20210210"
          },
          "actions": {
            "view:public": "EFFECT_ALLOW"
          },
          "meta": {
            "actions": {
              "view:public": {
                "matchedPolicy": "resource.leave_request.v20210210"
              }
            },
            "effectiveDerivedRoles": [
              "employee_that_owns_the_record"
            ]
          }
        }
      ],
      "cerbosCallId": "01HHENANTHFD5DV3HZGDKB87PJ"
    }
  }
}
```

| **1** | Boolean decision: true for allow, false for deny                                                                                                                             |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Additional context about the evaluation                                                                                                                                      |
| **3** | Full Cerbos CheckResources response (included when cerbos.includeMeta is true). See [CheckResources (/api/check/resources)](#check-resources) for response structure details |

### [](#authzen-access-evaluation-batch)`Access Evaluations` (`/access/v1/evaluations`)

Evaluates multiple access requests in a single call. This endpoint supports default values that can be overridden for individual evaluations, and evaluation semantics that control execution behavior.

Request

```json
{
  "subject": { (1)
    "type": "user",
    "id": "donald_duck",
    "properties": {
      "cerbos.policyVersion": "20210210",
      "cerbos.roles": ["employee"],
      "department": "marketing",
      "geography": "GB",
      "team": "design"
    }
  },
  "resource": { (2)
    "type": "leave_request",
    "id": "XX125",
    "properties": {
      "cerbos.policyVersion": "20210210",
      "department": "marketing",
      "geography": "GB",
      "owner": "john",
      "team": "design"
    }
  },
  "context": { (3)
    "cerbos.requestId": "test",
    "cerbos.includeMeta": true
  },
  "evaluations": [ (4)
    {
      "action": { (5)
        "name": "view:public",
        "properties": {}
      }
    },
    {
      "action": {
        "name": "approve",
        "properties": {}
      }
    },
    {
      "resource": { (6)
        "type": "leave_request",
        "id": "XX150",
        "properties": {
          "cerbos.policyVersion": "20210210",
          "department": "marketing",
          "geography": "GB",
          "owner": "mary",
          "team": "design"
        }
      },
      "action": {
        "name": "create",
        "properties": {}
      }
    }
  ],
  "options": { (7)
    "evaluations_semantic": "execute_all" (8)
  }
}
```

| **1** | Default subject for all evaluations (can be overridden in individual evaluations)                    |
| ----- | ---------------------------------------------------------------------------------------------------- |
| **2** | Default resource for all evaluations (can be overridden in individual evaluations)                   |
| **3** | Default context for all evaluations (can be overridden in individual evaluations)                    |
| **4** | Array of evaluations to perform. Each can override the default subject, resource, action, or context |
| **5** | Evaluation using default subject and resource, specifying only the action                            |
| **6** | Evaluation overriding the default resource while using the default subject                           |
| **7** | Optional execution controls                                                                          |
| **8** | Evaluation semantic: execute\_all (default), deny\_on\_first\_deny, or permit\_on\_first\_permit     |

**Evaluation Semantics:**

`execute_all` (default)

Process all evaluations regardless of individual results

`deny_on_first_deny`

Stop processing after the first denial

`permit_on_first_permit`

Stop processing after the first permit

Response

```json
{
  "evaluations": [ (1)
    {
      "decision": true, (2)
      "context": {
        "cerbos.response": { (3)
          "requestId": "test",
          "results": [
            {
              "resource": {
                "id": "XX125",
                "kind": "leave_request",
                "policyVersion": "20210210"
              },
              "actions": {
                "view:public": "EFFECT_ALLOW"
              },
              "meta": {
                "actions": {
                  "view:public": {
                    "matchedPolicy": "resource.leave_request.v20210210"
                  }
                }
              }
            }
          ],
          "cerbosCallId": "01HHENANTHFD5DV3HZGDKB87PJ"
        }
      }
    },
    {
      "decision": false,
      "context": {
        "cerbos.response": {
          "requestId": "test",
          "results": [
            {
              "resource": {
                "id": "XX125",
                "kind": "leave_request",
                "policyVersion": "20210210"
              },
              "actions": {
                "approve": "EFFECT_DENY"
              }
            }
          ],
          "cerbosCallId": "01HHENANTHFD5DV3HZGDKB87PJ"
        }
      }
    },
    {
      "decision": false,
      "context": {
        "cerbos.response": {
          "requestId": "test",
          "results": [
            {
              "resource": {
                "id": "XX150",
                "kind": "leave_request",
                "policyVersion": "20210210"
              },
              "actions": {
                "create": "EFFECT_DENY"
              }
            }
          ],
          "cerbosCallId": "01HHENANTHFD5DV3HZGDKB87PJ"
        }
      }
    }
  ]
}
```

| **1** | Array of evaluation responses, in the same order as the request                                    |
| ----- | -------------------------------------------------------------------------------------------------- |
| **2** | Boolean decision for this evaluation                                                               |
| **3** | Full Cerbos CheckResources response for this evaluation (included when cerbos.includeMeta is true) |

## [](#%5Faccessing%5Fthe%5Fapi)Accessing the API

### [](#%5Fusing%5Fcurl%5Fto%5Faccess%5Fthe%5Frest%5Fapi)Using curl to access the REST API

#### [](#%5Fcerbos%5Fapi%5Fexamples)Cerbos API Examples

```sh
cat <<EOF | curl --silent "localhost:3592/api/check/resources?pretty" -d @-
{
  "requestId": "test",
  "principal": {
    "id": "alice",
    "roles": ["employee"],
    "attr": {
      "department": "accounting",
      "geography": "GB",
      "team": "design"
    }
  },
  "resources": [
    {
      "resource": {
        "id": "XX125",
        "kind": "leave_request",
        "attr": {
          "department": "accounting",
          "geography": "GB",
          "id": "XX125",
          "owner": "john",
          "team": "design"
        }
      },
      "actions": [
        "view:public",
        "approve",
        "create"
      ]
    }
  ]
}
EOF
```

#### [](#%5Fauthzen%5Fapi%5Fexamples)AuthZEN API Examples

**Metadata endpoint:**

```sh
curl --silent "localhost:3592/.well-known/authzen-configuration?pretty"
```

**Access Evaluation (single):**

```sh
cat <<EOF | curl --silent "localhost:3592/access/v1/evaluation?pretty" -d @-
{
  "subject": {
    "type": "user",
    "id": "alice",
    "properties": {
      "cerbos.roles": ["employee"],
      "department": "accounting",
      "geography": "GB",
      "team": "design"
    }
  },
  "resource": {
    "type": "leave_request",
    "id": "XX125",
    "properties": {
      "department": "accounting",
      "geography": "GB",
      "owner": "john",
      "team": "design"
    }
  },
  "action": {
    "name": "view:public",
    "properties": {}
  },
  "context": {
    "cerbos.requestId": "test",
    "cerbos.includeMeta": true
  }
}
EOF
```

**Access Evaluations (batch):**

```sh
cat <<EOF | curl --silent "localhost:3592/access/v1/evaluations?pretty" -d @-
{
  "subject": {
    "type": "user",
    "id": "alice",
    "properties": {
      "cerbos.roles": ["employee"],
      "department": "accounting",
      "geography": "GB",
      "team": "design"
    }
  },
  "resource": {
    "type": "leave_request",
    "id": "XX125",
    "properties": {
      "department": "accounting",
      "geography": "GB",
      "owner": "john",
      "team": "design"
    }
  },
  "context": {
    "cerbos.requestId": "test",
    "cerbos.includeMeta": true
  },
  "evaluations": [
    {
      "action": {
        "name": "view:public",
        "properties": {}
      }
    },
    {
      "action": {
        "name": "approve",
        "properties": {}
      }
    },
    {
      "action": {
        "name": "create",
        "properties": {}
      }
    }
  ]
}
EOF
```

### [](#%5Fusing%5Fgrpcurl%5Fto%5Faccess%5Fthe%5Fgrpc%5Fapi)Using grpcurl to access the gRPC API

```sh
cat <<EOF | grpcurl -plaintext -d @ localhost:3593 cerbos.svc.v1.CerbosService/CheckResources
{
  "requestId": "test",
  "principal": {
    "id": "alice",
    "roles": ["employee"],
    "attr": {
      "department": "accounting",
      "geography": "GB",
      "team": "design"
    }
  },
  "resources": [
    {
      "resource": {
        "id": "XX125",
        "kind": "leave_request",
        "attr": {
          "department": "accounting",
          "geography": "GB",
          "id": "XX125",
          "owner": "john",
          "team": "design"
        }
      },
      "actions": [
        "view:public",
        "approve",
        "create"
      ]
    }
  ]
}
EOF
```

## [](#%5Fgenerating%5Fapi%5Fclients)Generating API clients

The Cerbos OpenAPI specification can be obtained from a running Cerbos instance by accessing <http://localhost:3592/schema/swagger.json>. Cerbos gRPC API definitions are published to the [Buf schema registry (BSR)](https://buf.build/cerbos/cerbos-api) and can be easily added to your project if you use the [Buf build system for protobufs](https://docs.buf.build).

### [](#%5Frest)REST

There are many tools available to generate clients from an OpenAPI specification. <https://openapi.tools/#sdk> is a good resource for finding a tool suitable for your preferred language.

#### [](#%5Fexample%5Fgenerating%5Fa%5Fjava%5Fclient%5Fusing%5Fopenapi%5Fgenerator)Example: Generating a Java client using OpenAPI Generator

| |  [OpenAPI Generator](https://openapi-generator.tech) has [support for many popular programming languages and frameworks](https://openapi-generator.tech/docs/generators#client-generators). Please consult the documentation to find the client generation instructions for your favourite language. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

This is an example of using the popular [OpenAPI Generator](https://openapi-generator.tech) service to generate a Java client API.

* Download the Cerbos OpenAPI specification  
```sh  
curl -Lo swagger.json http://localhost:3592/schema/swagger.json  
```
* Run the OpenAPI Generator  
```sh  
docker run --rm -v $(pwd):/oas openapitools/openapi-generator-cli generate -i /oas/swagger.json -g java -o /oas/java  
```

### [](#%5Fgrpc)gRPC

**Any language**

You can access the Cerbos protobuf definitions from the [Cerbos source tree](https://github.com/cerbos/cerbos/tree/main/api). However, the easiest way to generate client code for your preferred language is to use the [Buf build tool](https://docs.buf.build) to obtain the published API definitions from the [Buf schema registry (BSR)](https://buf.build/cerbos/cerbos-api).

* Run `buf export buf.build/cerbos/cerbos-api -o proto` to download the API definitions with dependencies to the `proto` directory.
* You can now use [buf generate](https://docs.buf.build/generate-usage) or `protoc` to generate code using the protobufs available in the `proto` directory.

| |  [BSR generated SDKs](https://buf.build/cerbos/cerbos-api/sdks) feature can be used to download pre-packaged, generated code for supported languages. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- |

**Go**

The [Cerbos Go SDK](https://pkg.go.dev/github.com/cerbos/cerbos/client) uses the gRPC API to communicate with Cerbos. The generated gRPC and protobuf code is available under the `github.com/cerbos/cerbos/api/genpb` package.

```sh
go get github.com/cerbos/cerbos/api/genpb
```

You can also make use [Buf generated SDKs](https://buf.build/cerbos/cerbos-api) to pull down the Cerbos gRPC API as a Go module:

```sh
go get buf.build/gen/go/cerbos/cerbos-api/grpc/go@latest
```

API reference
====================
[API reference](%5Fattachments/cerbos-api.html)

<code>cerbos</code>
====================
See [Install from binary](../installation/binary.html) or [Run from container](../installation/container.html) for instructions on how to install the `cerbos` binary.

This binary provides the following sub commands:

`compile`

Validate, compile and run tests on a policy repo

`healthcheck`

Perform a healthcheck on a Cerbos PDP

`repl`

An interactive REPL (read-evaluate-print-loop) for CEL conditions

`run`

Start a PDP and run a command within its context

`server`

Start the PDP server

Example: Running `compile` using the binary

```sh
./cerbos compile --help
```

Example: Running `compile` using the container

```sh
docker run -i -t ghcr.io/cerbos/cerbos:0.51.0 compile --help
```

## [](#compile)`compile` Command

Runs the Cerbos compiler to validate policy definitions and run any test suites. See [Policy compilation](../policies/compile.html) for more information.

This command exits with different exit codes depending on the kind of failure.

| 0 | No compile or test failures  |
| - | ---------------------------- |
| 1 | Unknown failure              |
| 2 | Invalid arguments to command |
| 3 | Compilation failed           |
| 4 | Tests failed                 |

```none
Usage: cerbos compile <dir>

Compile and test policies

Examples:

# Compile and run tests found in /path/to/policy/repo

cerbos compile /path/to/policy/repo

# Compile but skip tests

cerbos compile --skip-tests /path/to/policy/repo

# Compile and run tests matching a filter (globs for suite, test, principal, resource, action)

cerbos compile --test-filter='suite=MySuite;test=album*;principal=alice;resource=my_album;action=view' /path/to/policy/repo

# Multiple filters can be combined (all filter dimensions are merged)

cerbos compile --test-filter='principal=alice,bob' --test-filter='action=view,edit' /path/to/policy/repo

Arguments:
  <dir>    Policy directory

Flags:
  -h, --help                       Show context-sensitive help.
      --version                    Show cerbos version

      --ignore-schemas             Ignore schemas during compilation
      --test-filter=TEST-FILTER    Filter tests by dimensions (suite, test, principal, resource, action).
                                   Format: 'dimension=glob1,glob2;...'. Can be specified multiple times.
      --skip-tests                 Skip tests
      --skip-batching              Skip batching tests
  -o, --output="tree"              Output format (tree,list,json)
      --test-output=TEST-OUTPUT    Test output format. If unspecified matches the value of the output flag. (tree,list,json,junit)
      --color=COLOR                Output color level (auto,never,always,256,16m). Defaults to auto.
      --no-color                   Disable colored output
      --verbose                    Verbose output on test failure
```

## [](#healthcheck)`healthcheck` Command

Utility to perform healthchecks on a Cerbos PDP. Can be used as a [Docker HEALTHCHECK](https://docs.docker.com/engine/reference/builder/#healthcheck) command.

You can share the configuration between Cerbos PDP and the healthcheck by using the `CERBOS_CONFIG` environment variable to define the path to the config file.

Example: Docker healthcheck based on mounted config file

```sh
docker run -i -t -p 3592:3592 -p 3593:3593 \
    -v /path/to/conf/dir:/config \
    -e CERBOS_CONFIG=/config/.cerbos.yaml \
    ghcr.io/cerbos/cerbos:0.51.0
```

```none
Usage: cerbos healthcheck (hc)

Healthcheck utility

Performs a healthcheck on a Cerbos PDP. This can be used as a Docker HEALTHCHECK command. When the path to the Cerbos config file is provided via the '--config' flag or the CERBOS_CONFIG environment variable, the
healthcheck will be automatically configured based on the settings from the file. By default, the gRPC endpoint will be checked using the gRPC healthcheck protocol. This is usually sufficient for most cases as the Cerbos
REST API is built on top of the gRPC API as well.

Examples:

# Check gRPC endpoint

cerbos healthcheck --config=/path/to/.cerbos.yaml

# Check HTTP endpoint and ignore server certificate verification

cerbos healthcheck --config=/path/to/.cerbos.yaml --kind=http --insecure

# Check the HTTP endpoint of a specific host with no TLS.

cerbos healthcheck --kind=http --host-port=10.0.1.5:3592 --no-tls

Flags:
  -h, --help           Show context-sensitive help.
      --version        Show cerbos version

      --kind="grpc"    Healthcheck kind (grpc,http) ($CERBOS_HC_KIND)
      --insecure       Do not verify server certificate ($CERBOS_HC_INSECURE)
      --timeout=10s    Healthcheck timeout ($CERBOS_HC_TIMEOUT)

config
  --config=STRING    Cerbos config file ($CERBOS_CONFIG)

manual
  --host-port=STRING    Host and port to connect to ($CERBOS_HC_HOSTPORT)
  --ca-cert=STRING      Path to CA cert for validating server cert ($CERBOS_HC_CACERT)
  --no-tls              Don't use TLS ($CERBOS_HC_NOTLS)
```

## [](#repl)`repl` Command

The REPL is an interactive utility to experiment with [CEL conditions](../policies/conditions.html) used in Cerbos policy rules. All Cerbos library functions and special variables (`request`, `R`, `P` and so on) are available in this environment.

Example: Running the REPL using the binary

```sh
./cerbos repl
```

Example: Running the REPL using the container

```sh
docker run -i -t ghcr.io/cerbos/cerbos:0.51.0 repl
```

You can type in valid CEL expressions at the prompt to instantly evaluate them.

-> 5 + 1
_ = 6

-> "test".charAt(1)
_ = "e"

The special variable `_` holds the result of the last expression evaluated.

-> 5 + 5
_ = 10

-> _ * 10
_ = 100

You can define variables using the `:let` directive.

-> :let x = hierarchy("a.b.c")
x = [
  "a",
  "b",
  "c"
]

-> :let y = hierarchy("a.b")
y = [
  "a",
  "b"
]

-> x.immediateChildOf(y)
_ = true

You can also set special variables used in Cerbos policies (`request`, `variables`, `R`, `P`, `V`) and try out CEL expressions using them.

-> :let request = {
>   "principal":{"id":"john","roles":["employee"],"attr":{"scope":"foo.bar.baz.qux"}},
>   "resource":{"id":"x1","kind":"leave_request","attr":{"scope":"foo.bar"}}
> }

-> hierarchy(R.attr.scope).ancestorOf(hierarchy(P.attr.scope))
_ = true

Type `:vars` to display the values of all the variables currently defined in the environment.

You can load a Cerbos policy into the REPL by typing `:load path/to/policy_file.yaml`. This will read the policy and load any rules that have conditions attached. These can be viewed by typing `:rules`. Execute any rule by providing its number to the `:exec` directive (for example, `:exec #2`). Rules are executed using the variables defined in the current REPL session. You can set or update them using the `:let` directive and re-execute the rules to see the effects.

-> :load store/leave_request.yaml
Loaded resource.leave_request.v20210210

Policy variables:
{
  "pending_approval": "(\"PENDING_APPROVAL\")",
  "principal_location": "(P.attr.ip_address.inIPAddrRange(\"10.20.0.0/16\") ? \"GB\" : \"\")"
}

Conditional rules in 'resource.leave_request.v20210210'

[#0]
    actions:
    - approve
    condition:
      match:
        expr: request.resource.attr.status == V.pending_approval
    derivedRoles:
    - direct_manager
    effect: EFFECT_ALLOW


-> :exec #0
└──request.resource.attr.status == V.pending_approval [false]

Type `:help` or `:h` to display help. Type `:quit`, `:q` or `:exit` to exit the REPL.

| |  Use the up/down arrow keys (or Ctrl+P/Ctrl+N) to navigate command history. Most of the standard line-editing commands such as Ctrl+a, Ctrl+h, Ctrl+r are supported as well. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#run)`run` Command

This provides a quick way to try out Cerbos. It launches a Cerbos PDP instance and then invokes a command of your choice that can then use the PDP to make access decisions. A good use case for this command is as an integration test runner. If you have written some tests that make use of Cerbos, you can run them within the context of an actual PDP instance as follows:

```sh
cerbos run -- python -m unittest
```

By default, the policies are loaded from the `policies` directory in the current working directory and HTTP and gRPC endpoints will be exposed on `127.0.0.1:3592` and `127.0.0.1:3593` respectively. Your application can obtain the actual endpoint addresses by inspecting the `CERBOS_HTTP` or `CERBOS_GRPC` environment variables.

If a file named `.cerbos.yaml` exists in the current working directory, that file will be used as the Cerbos [configuration file](../configuration/index.html). You can use a different config file or override specific config values using the same flags as the `server` command above.

```none
Usage: cerbos run <command> ...

Run a command in the context of a Cerbos PDP

Launches a command within the context of a Cerbos PDP. The policies are loaded by default from a directory named "policies" in the current working directory. The launched application can access Cerbos endpoints using the
values from CERBOS_HTTP or CERBOS_GRPC environment variables.

If a file named ".cerbos.yaml" exists in the current working directory, it will be used as the configuration file for the PDP. You can override the config file and/or other configuration options using the flags described
below.

Examples:

# Launch Go tests within a Cerbos context

cerbos run -- go test ./...

# Start Cerbos with a custom configuration file and run Python tests within the context

cerbos run --config=myconf.yaml -- python -m unittest

# Silence Cerbos log output

cerbos run --log-level=error -- curl -I http://127.0.0.1:3592/_cerbos/health

Arguments:
  <command> ...    Command to run

Flags:
  -h, --help                                    Show context-sensitive help.
      --version                                 Show cerbos version

      --log-level="info"                        Log level (debug,info,warn,error)
      --config=.cerbos.yaml                     Path to config file
      --set=server.adminAPI.enabled=true,...    Config overrides
      --timeout=30s                             Cerbos startup timeout
```

## [](#server)`server` Command

Starts the Cerbos PDP.

```none
Usage: cerbos server --config=.cerbos.yaml

Start Cerbos server (PDP)

Examples:

# Start the server

cerbos server --config=/path/to/.cerbos.yaml

# Start the server with the Admin API enabled and the 'sqlite' storage driver

cerbos server --config=/path/to/.cerbos.yaml --set=server.adminAPI.enabled=true --set=storage.driver=sqlite3 --set=storage.sqlite3.dsn=':memory:'

Flags:
  -h, --help                                    Show context-sensitive help.
      --version                                 Show cerbos version

      --debug-listen-addr=:6666                 Address to start the gops listener
      --log-level="info"                        Log level (debug,info,warn,error)
      --config=.cerbos.yaml                     Path to config file
      --set=server.adminAPI.enabled=true,...    Config overrides
```

<code>cerbosctl</code>
====================
This utility can be downloaded as a separate container, tar archive, or [npm package](https://www.npmjs.com/package/cerbosctl). It is automatically installed when installing Cerbos through [Linux packages or the Homebrew tap](../installation/binary.html#linux-packages).

Run from the container

```sh
docker run -it ghcr.io/cerbos/cerbosctl:0.51.0 \
    --server=192.168.1.10:3593 \
    --username=user \
    --password=password \
    get rp
```

__Download and run the appropriate binary from <https://github.com/cerbos/cerbos/releases/tag/v0.51.0>__
| OS    | Arch      | Bundle                                    |
| ----- | --------- | ----------------------------------------- |
| Linux | x86-64    | cerbosctl\_0.51.0\_Linux\_x86\_64.tar.gz  |
| Linux | arm64     | cerbosctl\_0.51.0\_Linux\_arm64.tar.gz    |
| MacOS | universal | cerbosctl\_0.51.0\_Darwin\_all.tar.gz     |
| MacOS | x86-64    | cerbosctl\_0.51.0\_Darwin\_x86\_64.tar.gz |
| MacOS | arm64     | cerbosctl\_0.51.0\_Darwin\_arm64.tar.gz   |

Cerbosctl requires the [Admin API to be enabled](../configuration/server.html#admin-api) on the Cerbos server.

The server address to connect to and the credentials to authenticate can be provided through environment variables or as arguments to the command.

```none
Usage: cerbosctl <command>

A CLI for managing Cerbos

The Cerbos Admin API must be enabled in order for these commands to work.
The Admin API requires credentials. They can be provided using a netrc file,
environment variables or command-line arguments.

Environment variables

  - CERBOS_SERVER: gRPC address of the Cerbos server
  - CERBOS_USERNAME: Admin username
  - CERBOS_PASSWORD: Admin password

When more than one method is used to provide credentials, the precedence from
lowest to highest is: netrc < environment < command line.

Examples

    # Connect to a TLS enabled server while skipping certificate verification and launch the decisions viewer
    cerbosctl --server=localhost:3593 --username=user --password=password --insecure decisions

    # Connect to a non-TLS server and launch the decisions viewer
    cerbosctl --server=localhost:3593 --username=user --password=password --plaintext decisions

Flags:
  -h, --help                       Show context-sensitive help.
      --server="localhost:3593"    Address of the Cerbos server ($CERBOS_SERVER)
      --username=STRING            Admin username ($CERBOS_USERNAME)
      --password=STRING            Admin password ($CERBOS_PASSWORD)
      --ca-cert=STRING             Path to the CA certificate for verifying server identity
      --client-cert=STRING         Path to the TLS client certificate
      --client-key=STRING          Path to the TLS client key
      --insecure                   Skip validating server certificate
      --plaintext                  Use plaintext protocol without TLS

Commands:
  get derived_roles (derived_role,dr) [<id> ...]

  get export_constants (ec) [<id> ...]

  get export_variables (ev) [<id> ...]

  get principal_policies (principal_policy,pp) [<id> ...]

  get resource_policies (resource_policy,rp) [<id> ...]

  get role_policies (role_policy,rlp) [<id> ...]

  get schemas (schema,s) [<id> ...]

  inspect policies (p) [<id> ...]
    Inspect policies in the store

  store export (e) <path>

  store reload (r)

  delete policy (policies,p) <id> ...

  delete schema (schemas,s) <id> ...

  disable policy (policies,p) <id> ...

  enable policy (policies,p) <id> ...

  put policy (policies,p) <paths> ...

  put schema (schemas,s) <paths> ...

  decisions
    Interactive decision log viewer

  audit
    View audit logs

  version
    Show cerbosctl and PDP version

Run "cerbosctl <command> --help" for more information on a command.
```

## [](#audit)`audit`

This command allows you to view the audit logs captured by the Cerbos server. [Audit logging](../configuration/audit.html) must be enabled on the server to obtain the data through this command.

Filters

tail

Get the last N records (e.g. `--tail=10`)

between

Get records between two ISO-8601 timestamps. If the last timestamp is left out, get records from the first timestamp up to now.

* `--between=2021-07-01T00:00:00Z,2021-07-02T00:00:00Z`: From midnight of 2021-07-01 to midnight of 2021-07-02.
* `--between=2021-07-01T00:00:00Z`: From midnight of 2021-07-01 to now.

since

Get records from N hours/minutes/second ago to now. (e.g. `--since=3h`)

lookup

Get a specific record by ID. (e.g. `--lookup=01F9Y5MFYTX7Y87A30CTJ2FB0S`)

View the last 10 access logs

```sh
cerbosctl audit --kind=access --tail=10
```

View the decision logs from midnight 2021-07-01 to midnight 2021-07-02

```sh
cerbosctl audit --kind=decision --between=2021-07-01T00:00:00Z,2021-07-02T00:00:00Z
```

View the decision logs from midnight 2021-07-01 to now

```sh
cerbosctl audit --kind=decision --between=2021-07-01T00:00:00Z
```

View the access logs from 3 hours ago to now as newline-delimited JSON

```sh
cerbosctl audit --kind=access --since=3h --raw
```

View a specific access log entry by call ID

```sh
cerbosctl audit --kind=access --lookup=01F9Y5MFYTX7Y87A30CTJ2FB0S
```

## [](#decisions)`decisions`

This command starts an interactive text user interface to view and analyze the decision records captured by the Cerbos server. It accepts the same [filter flags](#audit-filters) as the `audit` command.

![Decisions](_images/decisions-tui.png)

* tab Switch focus to different panes in the UI
* esc Close window (or exit if you are in the main screen)
* q Exit

Use the arrow keys (or Vim keys h, j, k, l) to scroll horizontally or vertically. Press enter to select/open an item.

Start analyzing the last 20 decision records

```sh
cerbosctl decisions --tail=20
```

## [](#delete)`delete`

This command deletes the polices and the schemas with the specified ids.

Delete policies

cerbosctl delete policies derived_roles.my_derived_roles
cerbosctl delete policy derived_roles.my_derived_roles
cerbosctl delete p derived_roles.my_derived_roles

Delete multiple policies

cerbosctl delete policies derived_roles.my_derived_roles resource.leave_request.default
cerbosctl delete policy derived_roles.my_derived_roles resource.leave_request.default
cerbosctl delete p derived_roles.my_derived_roles resource.leave_request.default

Delete schemas

cerbosctl delete schemas principal.json
cerbosctl delete schema principal.json
cerbosctl delete s principal.json

Delete multiple schemas

cerbosctl delete schemas principal.json leave_request.json
cerbosctl delete schema principal.json leave_request.json
cerbosctl delete s principal.json leave_request.json

## [](#disable)`disable`

This command disables the policies with the specified ids.

Disable policies

cerbosctl disable policies derived_roles.my_derived_roles
cerbosctl disable policy derived_roles.my_derived_roles
cerbosctl disable p derived_roles.my_derived_roles

Disable multiple policies

cerbosctl disable policies derived_roles.my_derived_roles resource.leave_request.default
cerbosctl disable policy derived_roles.my_derived_roles resource.leave_request.default
cerbosctl disable p derived_roles.my_derived_roles resource.leave_request.default

| |  Scoped policies must have unbroken scope chains. If you’re disabling a scoped policy, make sure that its descendant policies are disabled as well. |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#enable)`enable`

This command enables the policies with the specified ids.

Enable policies

cerbosctl enable policies derived_roles.my_derived_roles
cerbosctl enable policy derived_roles.my_derived_roles
cerbosctl enable p derived_roles.my_derived_roles

Enable multiple policies

cerbosctl enable policies derived_roles.my_derived_roles resource.leave_request.default
cerbosctl enable policy derived_roles.my_derived_roles resource.leave_request.default
cerbosctl enable p derived_roles.my_derived_roles resource.leave_request.default

## [](#get)`get`

This command lists the policies available in the configured policy repository. You can also retrieve individual policies or schemas by their identifiers and view their definitions as YAML or JSON.

You can filter the output using the `name` and `version` flags. Each flag accepts multiple comma-separated values which are OR’ed together. For example, `--name=a.yaml,b.yaml` matches policies that are either named `a.yaml` or `b.yaml`.

Separately, you can filter the output using the `name-regexp`, `version-regexp` and `scope-regexp` flags. Each flag accepts a regular expression string. These are separate from the `name` and `version` flags above, and cannot be used with their respective counterparts.

You can include disabled policies in the results by adding `--include-disabled` flag.

You can optionally restrict the list to a specific set of policies by supplying their IDs as trailing arguments.

List derived roles

cerbosctl get derived_roles
cerbosctl get derived_role
cerbosctl get dr

List principal policies

cerbosctl get principal_policies
cerbosctl get principal_policy
cerbosctl get pp

List resource policies

cerbosctl get resource_policies
cerbosctl get resource_policy
cerbosctl get rp

List derived\_roles where `name` is `my_policy` or `a_policy`

cerbosctl get derived_roles --name my_policy,a_policy
cerbosctl get dr --name my_policy,a_policy

List derived\_roles where `name` is `my_policy` or `a_policy`, using regular expression

cerbosctl get derived_roles --name-regexp "^(my|a)_policy\$"
cerbosctl get dr --name-regexp "^(my|a)_policy\$"

Get derived roles policies having the ID `common_roles.yaml` and `other_roles.yaml`

cerbosctl get derived_roles common_roles.yaml other_roles.yaml
cerbosctl get dr common_roles.yaml other_roles.yaml

List principal\_policies where `version` is `default` or `v1`

cerbosctl get principal_policies --version default,v1
cerbosctl get pp --version default,v1

List principal\_policies where `version` is `default` or `v1`, using regular expression

cerbosctl get principal_policies --version-regexp "(default|v1)"
cerbosctl get pp --version-regexp "(default|v1)"

Get principal\_policies having the ID `alex.yaml` and `john.yaml`

cerbosctl get principal_policies alex.yaml john.yaml
cerbosctl get pp alex.yaml john.yaml

List resource\_policies where `scope` includes the substring `foo`, using regular expression

cerbosctl get resource_policies --scope-regexp foo
cerbosctl get rp --scope-regexp foo

Get resource\_policies having the ID `leave_request.yaml` and `purchase_order.yaml`

cerbosctl get resource_policies leave_request.yaml purchase_order.yaml
cerbosctl get rp leave_request.yaml purchase_order.yaml

List derived\_roles and sort by column `policyId` or `name`

cerbosctl get derived_roles --sort-by policyId
cerbosctl get dr --sort-by policyId

cerbosctl get derived_roles --sort-by name
cerbosctl get dr --sort-by name

List principal\_policies and sort by column `policyId`, `name` or `version`

cerbosctl get principal_policies --sort-by policyId
cerbosctl get pp --sort-by policyId

cerbosctl get principal_policies --sort-by name
cerbosctl get pp --sort-by name

cerbosctl get principal_policies --sort-by version
cerbosctl get pp --sort-by version

List resource\_policies and sort by column `policyId`, `name` or `version`

cerbosctl get resource_policies --sort-by policyId
cerbosctl get rp --sort-by policyId

cerbosctl get resource_policies --sort-by name
cerbosctl get rp --sort-by name

cerbosctl get resource_policies --sort-by version
cerbosctl get rp --sort-by version

Get JSON

cerbosctl get derived_roles my_derived_roles --output=json

Get YAML

cerbosctl get derived_roles my_derived_roles --output=yaml

## [](#hub)`hub`

Operations related to Cerbos Hub.

### [](#epdp)`epdp`

Operations related to embedded PDPs.

#### [](#list-candidates)`list-candidates`

This command lists policies that are candidates for inclusion in the ePDP bundle. A policy is marked for inclusion if it is annotated with `hub.cerbos.cloud/embedded-pdp: "true"` in the `metadata.annotations` section of the policy. If a policy has the correct annotation, that policy and its ancestors (if it’s a scoped policy) are included the Cerbos Hub embedded PDP bundle. If none of the policies in the repo are annotated, they are all included in the bundle by default.

List candidates

cerbosctl hub epdp list-candidates ./path/to/repository

## [](#inspect-policies)`inspect policies`

This command is to inspect policies in the store. Currently, it lists actions and variables defined in the policies.

Inspect policies

cerbosctl inspect policies

## [](#put)`put`

This command puts the given policies or schemas to the configured policy repository.

Put policies

cerbosctl put policies ./path/to/policy.yaml
cerbosctl put policy ./path/to/policy.yaml
cerbosctl put p ./path/to/policy.yaml

Put multiple policies

cerbosctl put policy ./path/to/policy.yaml ./path/to/other/policy.yaml

Put policies under a directory

cerbosctl put policy ./dir/to/policies ./other/dir/to/policies

Put policies under a directory recursively

cerbosctl put policy --recursive ./dir/to/policies
cerbosctl put policy -R ./dir/to/policies

Put policies from a zip file

cerbosctl put policy ./dir/to/policies.zip

Put schemas

cerbosctl put schemas ./path/to/schema.json
cerbosctl put schema ./path/to/schema.json
cerbosctl put s ./path/to/schema.json

Put multiple schemas

cerbosctl put schema ./path/to/schema.json ./path/to/other/schema.json

Put schemas under a directory

cerbosctl put schema ./dir/to/schemas ./other/dir/to/schemas

Put schemas under a directory recursively

cerbosctl put schema --recursive ./dir/to/schemas
cerbosctl put schema -R ./dir/to/schemas

Put schemas from a zip file

cerbosctl put schema ./dir/to/schemas.zip

## [](#store)`store`

Trigger operations on the policy store of the PDP

### [](#export)`export`

Exports the policies and schemas from the store into a directory.

Export policies and schemas from the store into a directory

cerbosctl store export path/to/dir

Export policies and schemas from the store into a zip archive

cerbosctl store export path/to/archive.zip

Export policies and schemas from the store into a gzip archive

cerbosctl store export path/to/archive.gzip
cerbosctl store export path/to/archive.tar.gz

### [](#reload)`reload`

Reloads the store.

Reload the store

cerbosctl store reload

Reload the store and wait until it finishes

cerbosctl store reload --wait`

### [](#revisions)`revisions`

Trigger operations on the policy store revisions

#### [](#purge)`purge`

Deletes revisions from the `policy_revision` table

Purge all revisions

cerbosctl store revisions purge

Purge all revisions but keep last 2 revisions of each policy.

cerbosctl store revisions purge --keep-last=2

Cerbos CLI
====================
Every [Cerbos release](https://github.com/cerbos/cerbos/releases/tag/v0.51.0) ships with two binaries:

[cerbos](cerbos.html)

The Cerbos server (PDP) and the compiler/test runner

[cerbosctl](cerbosctl.html)

Command line utility to interact with Cerbos PDP instances that have the [Admin API enabled](../configuration/server.html#admin-api)

Audit block
====================
The `audit` block configures the audit logging settings for the Cerbos instance. Audit logs capture access records and decisions made by the engine along with the associated context data.

Cerbos API responses include a `cerbosCallId` field that contains the unique identifier under which the request was logged to the audit log (if enabled) and the Cerbos activity log. It is recommended that applications log this ID as part of their activity logs too so that those log entries can be joined together with Cerbos logs during log analysis to build a complete picture of the authorization decisions.

| |  Audit logging has some overhead in terms of resource usage (disk IO, CPU and memory). This overhead is usually negligible unless Cerbos is running in a resource-constrained environment. If resources are scarce or if you are expecting heavy traffic, disabling audit logging might have a positive impact on performance. |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

```yaml
audit:
  accessLogsEnabled: false # AccessLogsEnabled defines whether access logging is enabled.
  backend: local # Backend states which backend to use for Audits.
  decisionLogFilters: # DecisionLogFilters define the filters to apply while producing decision logs.
    checkResources: # CheckResources defines the filters that apply to CheckResources calls.
      ignoreAllowAll: false # IgnoreAllowAll ignores responses that don't contain an EFFECT_DENY.
    planResources: # PlanResources defines the filters that apply to PlanResources calls.
      ignoreAll: false # IgnoreAll prevents any plan responses from being logged. Takes precedence over other filters.
      ignoreAlwaysAllow: false # IgnoreAlwaysAllow ignores ALWAYS_ALLOWED plans.
  decisionLogsEnabled: false # DecisionLogsEnabled defines whether logging of policy decisions is enabled.
  enabled: false # Enabled defines whether audit logging is enabled.
  excludeMetadataKeys: ['authorization'] # ExcludeMetadataKeys defines which gRPC request metadata keys should be excluded from the audit logs. Takes precedence over includeMetadataKeys.
  includeMetadataKeys: ['content-type'] # IncludeMetadataKeys defines which gRPC request metadata keys should be included in the audit logs.
  file:
    additionalPaths: [stdout] # AdditionalPaths to mirror the log output. Has performance implications. Use with caution.
    logRotation: # LogRotation settings (optional).
      maxFileAgeDays: 10 # MaxFileAgeDays sets the maximum age in days of old log files before they are deleted.
      maxFileCount: 10 # MaxFileCount sets the maximum number of files to retain.
      maxFileSizeMB: 100 # MaxFileSizeMB sets the maximum size of individual log files in megabytes.
    path: /path/to/file.log # Required. Path to the log file to use as output. The special values stdout and stderr can be used to write to stdout or stderr respectively.
  hub:
    advanced:
      bufferSize: 256
      flushInterval: 1s
      gcInterval: 60s
      maxBatchSize: 32
    mask: # Mask defines a list of attributes to exclude from the audit logs, specified as lists of JSONPaths
      checkResources:
        - inputs[*].principal.attr.foo
        - inputs[*].auxData
        - outputs
      metadata: ['authorization']
      peer:
        - address
        - forwarded_for
      planResources: ['input.principal.attr.nestedMap.foo']
    retentionPeriod: 168h # How long to keep records for
    storagePath: /path/to/dir # Path to store the data
    pipeOutput: # Secondary backend to send logs to.
      backend: file
      enabled: false
  kafka:
    ack: all # Ack mode for producing messages. Valid values are "none", "leader" or "all" (default). Idempotency is disabled when mode is not "all".
    authentication: # Authentication
      tls:
        caPath: /path/to/ca.crt # Required. CAPath is the path to the CA certificate.
        certPath: /path/to/tls.cert # CertPath is the path to the client certificate.
        insecureSkipVerify: true # InsecureSkipVerify controls whether the server's certificate chain and host name are verified. Default is false.
        keyPath: /path/to/tls.key # KeyPath is the path to the client key.
        reloadInterval: 5m # ReloadInterval is the interval at which the TLS certificates are reloaded. The default is 0 (no reload).
    brokers: ['localhost:9092'] # Required. Brokers list to seed the Kafka client.
    clientID: cerbos # ClientID reported in Kafka connections.
    closeTimeout: 30s # CloseTimeout sets how long when closing the client to wait for any remaining messages to be flushed.
    compression: ['snappy'] # Compression sets the compression algorithm to use in order of priority. Valid values are "none", "gzip", "snappy","lz4", "zstd". Default is ["snappy", "none"].
    encoding: json # Encoding format. Valid values are "json" (default) or "protobuf".
    maxBufferedRecords: 1000 # MaxBufferedRecords sets the maximum number of records the client should buffer in memory in async mode.
    produceSync: false # ProduceSync forces the client to produce messages to Kafka synchronously. This can have a significant impact on performance.
    topic: cerbos.audit.log # Required. Topic to write audit entries to.
  local:
    advanced:
      bufferSize: 256
      flushInterval: 1s
      gcInterval: 60s
      maxBatchSize: 32
    retentionPeriod: 168h # How long to keep records for
    storagePath: /path/to/dir # Path to store the data
```

Including or excluding request metadata in log entries

To tune how request metadata (headers) is logged to access and decision log entries, configure `includeMetadataKeys` and `excludeMetadataKeys` as follows:

* Both `includeMetadataKeys` and `excludeMetadataKeys` are empty: no metadata will be logged
* Only `includeMetadataKeys` is defined: only the metadata keys in the list will be logged
* Only `excludeMetadataKeys` is defined: everything except the keys defined in the list will be logged
* Both `includeMetadataKeys` and `excludeMetadataKeys` are defined: Only the keys in the include list will be logged if, and only if, they are not in the exclude list

| |  If requests contain sensitive data such as authorization tokens, they will be captured by the audit logs and visible to anyone with access to the log files. Cerbos automatically excludes the authorization header. However, if you use other header keys to store sensitive data, always exclude them using the excludeMetadataKeys configuration setting. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#file)File backend

The `file` backend writes audit records as newline-delimited JSON to a file or stdout/stderr. With this backend you can use your existing log aggregation system (Datadog agent, Elastic agent, Fluentd, Graylog — to name a few) to collect, process and archive the audit data from all Cerbos instances.

| |  This backend cannot be queried using the Admin API, cerbosctl audit or cerbosctl decisions. |
| ---------------------------------------------------------------------------------------------- |

Minimal configuration with file output and no log rotation

```yaml
audit:
  enabled: true
  accessLogsEnabled: true
  decisionLogsEnabled: true
  backend: file
  file:
    path: /path/to/audit.log
```

Configuration with log rotation and output to both stdout and a file

```yaml
audit:
  enabled: true
  accessLogsEnabled: true
  decisionLogsEnabled: true
  backend: file
  file:
    path: /path/to/file.log
    additionalPaths:
      - stdout
    logRotation:
      maxFileAgeDays: 10 # Maximum age in days of old log files before they are deleted.
      maxFileCount: 10 # Maximum number of old log files to retain.
      maxFileSizeMB: 100 # Maximum size of individual log files in megabytes.
```

The `path` field can be set to special names `stdout` or `stderr` to log to stdout or stderr. Note that this would result in audit logs being mixed up with normal Cerbos operational logs. It is recommended to use an actual file for audit log output if your container orchestrator has support for collecting logs from files in addition to stdout/stderr.

Audit log entries can be selected by setting a filter on `log.logger == "cerbos.audit"`. Access log entries have `log.kind == "access"` and decision log entries have `log.kind == "decision"`.

If log rotation is enabled, `maxFileSizeMB` is the only required setting. If `maxFileCount` and `maxFileAgeDays` settings are not defined, files are never deleted by the Cerbos process.

## [](#hub)Hub backend

| |  Requires a [Cerbos Hub](https://www.cerbos.dev/product-cerbos-hub) account. [![Try Cerbos Hub](../_images/try_cerbos_hub.png)](https://hub.cerbos.cloud) |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- |

Securely sends audit logs to Cerbos Hub for aggregation and analysis. This vastly simplifies the work that would otherwise be required to configure and deploy a log aggregation solution to securely collect, store and query audit logs from across your fleet.

If you are new to Cerbos Hub, follow the [getting started guide](../../../cerbos-hub/getting-started.html). For more information about configuring the PDP to send audit logs to Cerbos Hub, refer to the [audit log collection documentation](../../../cerbos-hub/audit-log-collection.html).

## [](#kafka)Kafka backend

The `kafka` backend writes audit records to a Kafka topic. By default, the messages are published asynchronously to the specified topic in JSON format. The message header named `cerbos.audit.kind` would have the value `access` for access log entries and `decision` for decision log entries.

You can configure the audit logger to produce data in the Protocol Buffers binary encoding format as well. The schema for messages is available at <https://buf.build/cerbos/cerbos-api/docs/main:cerbos.audit.v1>.

Minimal configuration

```yaml
audit:
  enabled: true
  accessLogsEnabled: true
  decisionLogsEnabled: true
  backend: kafka
  kafka:
    brokers: ['broker1.kafka:9092', 'broker2.kafka:9092']
    topic: cerbos.audit.log
```

Full configuration

```yaml
audit:
  enabled: true
  accessLogsEnabled: true
  decisionLogsEnabled: true
  backend: kafka
  kafka:
    ack: all # Ack mode for producing messages. Valid values are "none", "leader" or "all" (default). Idempotency is disabled when mode is not "all".
    authentication: # Authentication
      tls:
        caPath: /path/to/ca.crt # Required. CAPath is the path to the CA certificate.
        certPath: /path/to/tls.cert # CertPath is the path to the client certificate.
        insecureSkipVerify: true # InsecureSkipVerify controls whether the server's certificate chain and host name are verified. Default is false.
        keyPath: /path/to/tls.key # KeyPath is the path to the client key.
        reloadInterval: 5m # ReloadInterval is the interval at which the TLS certificates are reloaded. The default is 0 (no reload).
    brokers: ['localhost:9092'] # Required. Brokers list to seed the Kafka client.
    clientID: cerbos # ClientID reported in Kafka connections.
    closeTimeout: 30s # CloseTimeout sets how long when closing the client to wait for any remaining messages to be flushed.
    encoding: json # Encoding format. Valid values are "json" (default) or "protobuf".
    maxBufferedRecords: 1000 # MaxBufferedRecords sets the maximum number of records the client should buffer in memory in async mode.
    produceSync: false # ProduceSync forces the client to produce messages to Kafka synchronously. This can have a significant impact on performance.
    topic: cerbos.audit.log # Required. Topic to write audit entries to.
    compression: ['snappy'] # Compression sets the compression algorithm to use in order of priority. Valid values are "none", "gzip", "snappy","lz4", "zstd". Default is ["snappy", "none"].
```

## [](#local)Local backend

The `local` backend uses an embedded key-value store to save audit records. Records are preserved for seven days by default and can be queried using the [Admin API](../api/admin%5Fapi.html), the [cerbosctl audit](../cli/cerbosctl.html#audit) command or the [cerbosctl decisions](../cli/cerbosctl.html#decisions) text interface (TUI).

The only required setting for the `local` backend is the `storagePath` field which specifies the path on disk where the logs should be stored.

```yaml
audit:
  enabled: true
  accessLogsEnabled: true
  decisionLogsEnabled: true
  backend: local
  local:
    storagePath: /path/to/dir
    retentionPeriod: 168h
    advanced:
      bufferSize: 16 # Size of the memory buffer. Increasing this will use more memory and the chances of losing data during a crash.
      maxBatchSize: 16 # Write batch size. If your records are small, increasing this will reduce disk IO.
      flushInterval: 30s # Time to keep records in memory before committing.
      gcInterval: 15m # How often the garbage collector runs to remove old entries from the log.
```

AuxData block
====================
The `auxData` block configures the auxiliary data sources that can be referenced in policy conditions.

## [](#%5Fjwt)JWT

Cerbos supports reading claims from a JWT issued by an authentication system. This helps reduce the boilerplate on the client side to extract the claims from a JWT and add them as attributes to the Cerbos API request. (See [The Cerbos API](../api/index.html) and [Auxiliary Data](../policies/conditions.html#auxdata) for more information on how to craft the API request and access the JWT claims in policies.)

In order to verify the JWT, the Cerbos instance must have access to the appropriate keysets. They can be fetched from a URL or read from the local file system. Verification involves checking that the signature is valid and that the token has not expired.

Using multiple keysets

```yaml
auxData:
  jwt:
    keySets:
      - id: ks1 # Unique ID that can be used in API requests to indicate the keyset to use to verify a particular token.
        remote: # Fetch from a JWKS URL.
          url: https://domain.tld/.well-known/keys.jwks
      - id: ks2
        remote:
          url: https://other-domain.tld/.well-known/keys.jwks
          refreshInterval: 1h # Explicitly set the refresh interval.
      - id: ks3
        local: # Load from a local file
          file: /path/to/keys.jwks
      - id: ks4
        local: # Load from a base64-encoded key data defined inline.
          data: BASE64-ENCODED-KEY-DATA
      - id: ks5
        local:
          file: /path/to/keys.pem
          pem: true # Treat the file (or data) as PEM.
```

| |  When multiple keysets are defined in the configuration file, all API requests _must_ include the keyset ID along with the JWT. When only a single keyset is defined in the configuration, then the keyset ID can be dropped from the API requests. |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

When keysets are fetched from a `remote` source, if the `refreshInterval` is not defined in the configuration, Cerbos will respect the `Cache-Control` and `Expiry` headers returned from the remote source when determining the refresh interval. If none of these data points are available, then the default refresh interval is one hour.

You can disable JWT verification by setting `disableVerification` to `true`. When verification is disabled, Cerbos will not perform cryptographic verification of the JWT but the `exp` and `nbf` claims are still checked to ensure that the token is valid. You can configure the acceptable time skew for those claims by setting `acceptableTimeSkew` to a positive time duration.

| |  Disabling JWT verification is not recommended because it makes the system insecure by forcing Cerbos to evaluate policies using potentially tampered data. Similarly, it’s not recommended to set acceptableTimeSkew to more than a few seconds. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

```yaml
auxData:
  jwt:
    disableVerification: true
    acceptableTimeSkew: 2s
```

Cerbos maintains an in-memory cache of verified JWTs to avoid repeating the cryptographic verification step on each request. Cached tokens are still validated on each request to make sure they are still valid for use. You can increase the size of the cache by setting `cacheSize`.

```yaml
auxData:
  jwt:
    cacheSize: 256
    keySets:
      - id: default
        remote:
          url: https://domain.tld/.well-known/keys.jwks
```

Some legacy authentication systems have key sets that do not contain `alg` or `kid` fields. Not having these fields defined is a security risk and the default behaviour of Cerbos is to fail the parsing of JWT. If you are aware of the risks and still want to enable those tokens to be parsed, set the `optionalAlg` and `optionalKid` options.

```yaml
auxData:
  jwt:
    keySets:
      - id: default
        remote:
          url: https://domain.tld/.well-known/keys.jwks
        insecure:
          optionalAlg: true # Set to true only if the keyset doesn't have an alg field
          optionalKid: true # Set to true only if the keyset doesn't have a kid field
```

Engine block
====================
## [](#default%5Fpolicy%5Fversion)Default policy version

[Cerbos policies](../policies/index.html) have a `version` field to support use cases such as having different policies for different environments (production, staging etc.) or for gradual rollout of a new version of an application. By default, when a request does not explicitly specify the policy version, the Cerbos engine attempts to find a matching policy that has its version set to `default`. You can change this fallback value by setting the `defaultPolicyVersion`. For example, if you have a Cerbos deployment for your staging environment, you may want to set `defaultPolicyVersion: staging` to ensure that the default policies in effect are the ones versioned as `staging`.

```yaml
engine:
  defaultPolicyVersion: "default"
```

## [](#default%5Fscope)Default scope

[Cerbos policies](../policies/index.html) have a `scope` field to support a way to model hierarchical relationships that regularly occur in many situations. By default, when a request does not explicitly specify the scope, the Cerbos engine attempts to find a matching policy that has its scope set to `""`. You can change this fallback value by setting the `defaultScope`. For example, you may set the default scope to `acme` with `defaultScope: acme` which will take effect when the request does not explicitly specify `scope` field.

```yaml
engine:
  defaultScope: "acme"
```

## [](#globals)Globals

Global variables are a way to pass environment-specific information to [policy conditions](../policies/conditions.html). For example, you might want to grant additional permissions to a role in your staging environment, without creating separate policy versions for different environments.

```yaml
engine:
  globals:
    environment: "staging"
```

Values set in `globals` can then be referenced in policy conditions:

```yaml
rules:
  - actions:
      - view
    effect: EFFECT_ALLOW
    roles:
      - developer
    condition:
      match:
        expr: globals.environment != "production"
```

As with other configuration settings, environment variables can be used to set global values.

```yaml
engine:
  globals:
    environment: ${CERBOS_ENVIRONMENT:development}
```

## [](#lenient%5Fscopes)Lenient scope search

When working with [scopes](../policies/scoped%5Fpolicies.html), the default behaviour of the Cerbos engine is to expect that a policy file exists for the requested scope. For example, if the API request defines `a.b.c` as the `scope`, a policy file _must exist_ in the policy repository with the `a.b.c` scope. This behaviour can be overridden by setting `lenientScopeSearch` configuration to `true`. When lenient scope search is enabled, if a policy with scope `a.b.c` does not exist in the store, Cerbos will attempt to find scopes `a.b`, `a` and \`\` in that order.

| |  This setting only affects how Cerbos treats missing leaf scopes when searching for policies. The policies stored in your policy store _must_ have unbroken scope chains (for example, if you have a scoped policy a.b.c in the store, the policy files for scopes a.b, a and \`\` must also exist). |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

```yaml
engine:
  lenientScopeSearch: true
```

Configuration
====================
The Cerbos server is configured with a YAML file, conventionally named `.cerbos.yaml`. Start the server by passing the configuration file using the `--config` flag. The values defined in the file can be overridden from the command-line by using the `--set` flag. The `--set` flag can be used multiple times. For example, to override `server.httpListenAddr` and `engine.defaultPolicyVersion`, the `--set` flag can be used as follows:

```sh
./cerbos server --config=/path/to/.cerbos.yaml --set=server.httpListenAddr=:3592 --set=engine.defaultPolicyVersion=staging
```

| |  Config values can reference environment variables by enclosing them between ${}, for example ${HOME}. Defaults can be set using ${VAR:default}. |
| -------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#minimal-configuration)Minimal Configuration

At a minimum, Cerbos requires a storage driver to be configured. If no explicit configuration is provided using the `--config` flag, Cerbos defaults to a `disk` driver configured to look for policies in a directory named `policies` in the current working directory.

Default configuration

```yaml
---
server:
  httpListenAddr: ":3592"
  grpcListenAddr: ":3593"

engine:
  defaultPolicyVersion: "default"

auxData:
  jwt:
    disableVerification: true

storage:
  driver: "disk"
  disk:
    directory: "${PWD}/policies"
    watchForChanges: true
```

## [](#full-configuration)Full Configuration

Cerbos has many configuration options that are either optional or has reasonable defaults built-in. The following section describes all user-configurable options and their defaults.

Cerbos configuration file

```yaml
---
audit:
  accessLogsEnabled: false # AccessLogsEnabled defines whether access logging is enabled.
  backend: local # Backend states which backend to use for Audits.
  decisionLogFilters: # DecisionLogFilters define the filters to apply while producing decision logs.
    checkResources: # CheckResources defines the filters that apply to CheckResources calls.
      ignoreAllowAll: false # IgnoreAllowAll ignores responses that don't contain an EFFECT_DENY.
    planResources: # PlanResources defines the filters that apply to PlanResources calls.
      ignoreAll: false # IgnoreAll prevents any plan responses from being logged. Takes precedence over other filters.
      ignoreAlwaysAllow: false # IgnoreAlwaysAllow ignores ALWAYS_ALLOWED plans.
  decisionLogsEnabled: false # DecisionLogsEnabled defines whether logging of policy decisions is enabled.
  enabled: false # Enabled defines whether audit logging is enabled.
  excludeMetadataKeys: ['authorization'] # ExcludeMetadataKeys defines which gRPC request metadata keys should be excluded from the audit logs. Takes precedence over includeMetadataKeys.
  includeMetadataKeys: ['content-type'] # IncludeMetadataKeys defines which gRPC request metadata keys should be included in the audit logs.
  file:
    additionalPaths: [stdout] # AdditionalPaths to mirror the log output. Has performance implications. Use with caution.
    logRotation: # LogRotation settings (optional).
      maxFileAgeDays: 10 # MaxFileAgeDays sets the maximum age in days of old log files before they are deleted.
      maxFileCount: 10 # MaxFileCount sets the maximum number of files to retain.
      maxFileSizeMB: 100 # MaxFileSizeMB sets the maximum size of individual log files in megabytes.
    path: /path/to/file.log # Required. Path to the log file to use as output. The special values stdout and stderr can be used to write to stdout or stderr respectively.
  hub:
    advanced:
      bufferSize: 256
      flushInterval: 1s
      gcInterval: 60s
      maxBatchSize: 32
    mask: # Mask defines a list of attributes to exclude from the audit logs, specified as lists of JSONPaths
      checkResources:
        - inputs[*].principal.attr.foo
        - inputs[*].auxData
        - outputs
      metadata: ['authorization']
      peer:
        - address
        - forwarded_for
      planResources: ['input.principal.attr.nestedMap.foo']
    pipeOutput:
      backend: file
      enabled: false
    retentionPeriod: 168h # How long to keep records for
    storagePath: /path/to/dir # Path to store the data
  kafka:
    ack: all # Ack mode for producing messages. Valid values are "none", "leader" or "all" (default). Idempotency is disabled when mode is not "all".
    authentication: # Authentication
      tls:
        caPath: /path/to/ca.crt # Required. CAPath is the path to the CA certificate.
        certPath: /path/to/tls.cert # CertPath is the path to the client certificate.
        insecureSkipVerify: true # InsecureSkipVerify controls whether the server's certificate chain and host name are verified. Default is false.
        keyPath: /path/to/tls.key # KeyPath is the path to the client key.
        reloadInterval: 5m # ReloadInterval is the interval at which the TLS certificates are reloaded. The default is 0 (no reload).
    brokers: ['localhost:9092'] # Required. Brokers list to seed the Kafka client.
    clientID: cerbos # ClientID reported in Kafka connections.
    closeTimeout: 30s # CloseTimeout sets how long when closing the client to wait for any remaining messages to be flushed.
    compression: ['snappy', 'none'] # Compression sets the compression algorithm to use in order of priority. Valid values are "none", "gzip", "snappy","lz4", "zstd". Default is ["snappy", "none"].
    encoding: json # Encoding format. Valid values are "json" (default) or "protobuf".
    maxBufferedRecords: 1000 # MaxBufferedRecords sets the maximum number of records the client should buffer in memory in async mode.
    produceSync: false # ProduceSync forces the client to produce messages to Kafka synchronously. This can have a significant impact on performance.
    topic: cerbos.audit.log # Required. Topic to write audit entries to.
  local:
    advanced:
      bufferSize: 256
      flushInterval: 1s
      gcInterval: 60s
      maxBatchSize: 32
    retentionPeriod: 168h # How long to keep records for
    storagePath: /path/to/dir # Path to store the data
auxData:
  jwt: # JWT holds the configuration for JWTs used as an auxiliary data source for the engine.
    acceptableTimeSkew: 2s # AcceptableTimeSkew sets the acceptable skew when checking exp and nbf claims.
    cacheSize: 256 # CacheSize sets the number of verified tokens cached in memory. Set to negative value to disable caching.
    disableVerification: false # DisableVerification disables JWT verification.
    keySets: # KeySets is the list of keysets to be used to verify tokens.
      -
        id: ks1 # Required. ID is the unique reference to this keyset.
        insecure: # Insecure options for relaxing security. Not recommended for production use. Use with caution.
          optionalAlg: false # OptionalAlg configures Cerbos to not require the alg field to be set in the key set.
          optionalKid: false # OptionalKid configures Cerbos to not require the kid field to be set in the key set.
        local: # Local defines a local keyset. Mutually exclusive with Remote.
          data: base64encodedJWK # Data is the encoded JWK data for this keyset. Mutually exclusive with File.
          file: /path/to/keys.jwk # File is the path to file containing JWK data. Mutually exclusive with Data.
          pem: true # PEM indicates that the data is PEM encoded.
        remote: # Remote defines a remote keyset. Mutually exclusive with Local.
          refreshInterval: 1h # RefreshInterval is the refresh interval for the keyset.
          url: https://domain.tld/.well-known/keys.jwks # Required. URL is the JWKS URL to fetch the keyset from.
engine:
  defaultPolicyVersion: "default" # DefaultPolicyVersion defines what version to assume if the request does not specify one.
  defaultScope: "" # DefaultScope defines what scope to assume if the request does not specify one.
  globals: {"environment": "staging"} # Globals are environment-specific variables to be made available to policy conditions.
  lenientScopeSearch: false # LenientScopeSearch configures the engine to ignore missing scopes and search upwards through the scope tree until it finds a usable policy.
  policyLoaderTimeout: 2s # PolicyLoaderTimeout is the timeout for loading policies from the policy store.
hub:
  credentials: # Credentials holds Cerbos Hub client credentials.
    clientID: 92B0K05B6HOF # ClientID of the Cerbos Hub credential. Defaults to the value of the CERBOS_HUB_CLIENT_ID environment variable.
    clientSecret: ${CERBOS_HUB_CLIENT_SECRET} # ClientSecret of the Cerbos Hub credential. Defaults to the value of the CERBOS_HUB_CLIENT_SECRET environment variable.
    pdpID: crb-004 # PDPID is the unique identifier for this Cerbos instance. Defaults to the value of the CERBOS_HUB_PDP_ID environment variable.
    workspaceSecret: ${CERBOS_HUB_WORKSPACE_SECRET} # WorkspaceSecret used to decrypt the bundles. Defaults to the value of the CERBOS_HUB_WORKSPACE_SECRET environment variable.
schema:
  cacheSize: 1024 # CacheSize defines the number of schemas to cache in memory.
  enforcement: reject # Enforcement defines level of the validations. Possible values are none, warn, reject.
server:
  apiExplorerEnabled: true # APIExplorerEnabled defines whether the API explorer UI is enabled.
  adminAPI: # AdminAPI defines the admin API configuration.
    adminCredentials: # AdminCredentials defines the admin user credentials.
      passwordHash: JDJ5JDEwJEdEOVFzZDE2VVhoVkR0N2VkUFBVM09nalc0QnNZaC9xc2E4bS9mcUJJcEZXenp5OUpjMi91Cgo= # PasswordHash is the base64-encoded bcrypt hash of the password to use for authentication.
      username: cerbos # Username is the hardcoded username to use for authentication.
    enabled: true # Enabled defines whether the admin API is enabled.
  advanced: # Advanced server settings.
    grpc: # GRPC server settings.
      connectionTimeout: 60s # ConnectionTimeout sets the timeout for establishing a new connection.
      maxConcurrentStreams: 1024 # MaxConcurrentStreams sets the maximum concurrent streams per connection. Defaults to 1024. Set to 0 to allow the maximum possible number of streams.
      maxConnectionAge: 600s # MaxConnectionAge sets the maximum age of a connection.
      maxRecvMsgSizeBytes: 4194304 # MaxRecvMsgSizeBytes sets the maximum size of a single request message. Defaults to 4MiB. Affects performance and resource utilisation.
    http: # HTTP server settings.
      idleTimeout: 120s # IdleTimeout sets the keepalive timeout.
      readHeaderTimeout: 15s # ReadHeaderTimeout sets the timeout for reading request headers.
      readTimeout: 30s # ReadTimeout sets the timeout for reading a request.
      writeTimeout: 30s # WriteTimeout sets the timeout for writing a response.
  cors: # CORS defines the CORS configuration for the server.
    allowedHeaders: ['content-type'] # AllowedHeaders is the contents of the allowed-headers header.
    allowedOrigins: ['*'] # AllowedOrigins is the contents of the allowed-origins header.
    disabled: false # Disabled sets whether CORS is disabled.
    maxAge: 10s # MaxAge is the max age of the CORS preflight check.
  grpcListenAddr: ":3593" # Required. GRPCListenAddr is the dedicated GRPC address.
  httpListenAddr: ":3592" # Required. HTTPListenAddr is the dedicated HTTP address.
  logRequestPayloads: false # LogRequestPayloads defines whether the request payloads should be logged.
  metricsEnabled: true # MetricsEnabled defines whether the metrics endpoint is enabled.
  requestLimits: # RequestLimits defines the limits for requests.
    maxActionsPerResource: 50 # MaxActionsPerResource sets the maximum number of actions that could be checked for a resource in a single request.
    maxResourcesPerRequest: 50 # MaxResourcesPerBatch sets the maximum number of resources that could be sent in a single request.
  tls: # TLS defines the TLS configuration for the server.
    caCert: /path/to/CA_certificate # CACert is the path to the optional CA certificate for verifying client requests.
    cert: /path/to/certificate # Cert is the path to the TLS certificate file.
    key: /path/to/private_key # Key is the path to the TLS private key file.
  udsFileMode: 0o766 # UDSFileMode sets the file mode of the unix domain sockets created by the server.
storage:
  # This section is required. The field driver must be set to indicate which driver to use.
  driver: "disk" # Required. Driver defines which storage driver to use.
  blob:
    # This section is required only if storage.driver is blob.
    bucket: "s3://my-bucket-name?region=us-east-2" # Required. Bucket URL (Examples: s3://my-bucket?region=us-west-1 gs://my-bucket).
    downloadTimeout: 30s # DownloadTimeout specifies the timeout for downloading from cloud storage.
    prefix: policies # Prefix specifies a subdirectory to download.
    requestTimeout: 10s # RequestTimeout specifies the timeout for an HTTP request.
    updatePollInterval: 15s # UpdatePollInterval specifies the interval to poll the cloud storage. Set to 0 to disable.
    workDir: ${HOME}/tmp/cerbos/work # WorkDir is the local path to check out policies to.
  disk:
    # This section is required only if storage.driver is disk.
    directory: pkg/test/testdata/store # Required. Directory is the path on disk where policies are stored.
    watchForChanges: false # Required. WatchForChanges enables watching the directory for changes.
  git:
    # This section is required only if storage.driver is git.
    branch: policies # Branch is the branch to checkout.
    checkoutDir: ${HOME}/tmp/cerbos/work # CheckoutDir is the local path to checkout the Git repo to.
    https: # HTTPS holds auth details for the HTTPS protocol.
      password: ${GITHUB_TOKEN} # The password (or token) to use for authentication.
      username: cerbos # The username to use for authentication.
    operationTimeout: 60s # OperationTimeout specifies the timeout for git operations.
    protocol: file # Required. Protocol is the Git protocol to use. Valid values are https, ssh, and file.
    ssh: # SSH holds auth details for the SSH protocol.
      password: pw # The password to the SSH private key.
      privateKeyFile: ${HOME}/.ssh/id_rsa # The path to the SSH private key file.
      user: git # The git user. Defaults to git.
    subDir: policies # SubDir is the path under the checked-out Git repo where the policies are stored.
    url: file://${HOME}/tmp/cerbos/policies # Required. URL is the URL to the Git repo.
    updatePollInterval: 60s # UpdatePollInterval specifies the interval to poll the Git repository for changes. Set to 0 to disable.
  hub:
    # This section is required only if storage.driver is hub.
    cacheSize: 1024 # CacheSize defines the number of policies to cache in memory.
    local: # Local holds configuration for local bundle source.
      bundlePath: /path/to/bundle.crbp # Required. BundlePath is the full path to the local bundle file.
      tempDir: ${TEMP} # TempDir is the directory to use for temporary files.
    remote: # Remote holds configuration for remote bundle source. Takes precedence over local if both are defined.
      bundleLabel: latest # Required. BundleLabel to fetch from the server.
      cacheDir: ${XDG_CACHE_DIR} # CacheDir is the directory to use for caching downloaded bundles.
      disableAutoUpdate: false # DisableAutoUpdate sets whether new bundles should be automatically downloaded and applied.
      tempDir: ${TEMP} # TempDir is the directory to use for temporary files.
  mysql:
    # This section is required only if storage.driver is mysql.
    connPool:
      maxLifeTime: 60m
      maxIdleTime: 45s
      maxOpen: 4
      maxIdle: 1
    connRetry:
      maxAttempts: 3
      initialInterval: 0.5s
      maxInterval: 60s
    dsn: "user:password@tcp(localhost:3306)/db?interpolateParams=true" # Required. DSN is the data source connection string.
    serverPubKey:
      mykey: testdata/server_public_key.pem
    skipSchemaCheck: false # SkipSchemaCheck skips checking for required database tables on startup.
    tls:
      mytls:
        cert: /path/to/certificate
        key: /path/to/private_key
        caCert: /path/to/CA_certificate
  overlay:
    # This section is required only if storage.driver is overlay.
    baseDriver: blob # Required. BaseDriver is the default storage driver
    fallbackDriver: disk # Required. FallbackDriver is the secondary or fallback storage driver
    fallbackErrorThreshold: 5 # FallbackErrorThreshold is the max number of errors we allow within the fallbackErrorWindow period
    fallbackErrorWindow: 5m # FallbackErrorWindow is the cyclic period within which we aggregate failures
  postgres:
    # This section is required only if storage.driver is postgres.
    connPool:
      maxLifeTime: 60m
      maxIdleTime: 45s
      maxOpen: 4
      maxIdle: 1
    connRetry:
      maxAttempts: 3
      initialInterval: 0.5s
      maxInterval: 60s
    skipSchemaCheck: false # SkipSchemaCheck skips checking for required database tables on startup.
    url: "postgres://user:password@localhost:port/db" # Required. URL is the Postgres connection URL. See https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
  sqlite3:
    # This section is required only if storage.driver is sqlite3.
    dsn: ":memory:?_fk=true" # Required. Data source name
telemetry:
  disabled: false # Disabled sets whether telemetry collection is disabled or not.
  reportInterval: 1h # ReportInterval is the interval between telemetry pings.
  stateDir: ${HOME}/.config/cerbos # StateDir is used to persist state to avoid repeatedly sending the data over and over again.
```

Observability
====================
Cerbos is designed from the ground up to be cloud native and has first-class support for observability via OpenTelemetry metrics and distributed traces.

## [](#metrics)Metrics

By default, Cerbos exposes a metrics endpoint at `/_cerbos/metrics` that can be scraped by Prometheus or other metrics scrapers that support the Prometheus metrics format. This endpoint can be disabled by setting `server.metricsEnabled` configuration value to `false` (see [Server block](server.html)).

Cerbos also has support for OpenTelemetry protocol (OTLP) push metrics. It can be configured using [OpenTelemetry environment variables](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/). The following environment variables are supported.

| Environment variable                                                                            | Description                                                                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| OTEL\_EXPORTER\_OTLP\_METRICS\_ENDPOINT or OTEL\_EXPORTER\_OTLP\_ENDPOINT                       | Address of the OTLP metrics receiver (for example: <https://localhost:9090/api/v1/otlp/v1/metrics>). If not defined, OTLP metrics are disabled. |
| OTEL\_EXPORTER\_OTLP\_METRICS\_INSECURE or OTEL\_EXPORTER\_OTLP\_INSECURE                       | Skip validating the TLS certificate of the endpoint                                                                                             |
| OTEL\_EXPORTER\_OTLP\_METRICS\_CERTIFICATE or OTEL\_EXPORTER\_OTLP\_CERTIFICATE                 | Path to the certificate to use for validating the server’s TLS credentials.                                                                     |
| OTEL\_EXPORTER\_OTLP\_METRICS\_CLIENT\_CERTIFICATE or OTEL\_EXPORTER\_OTLP\_CLIENT\_CERTIFICATE | Path to the client certificate to use for mTLS                                                                                                  |
| OTEL\_EXPORTER\_OTLP\_METRICS\_CLIENT\_KEY or OTEL\_EXPORTER\_OTLP\_CLIENT\_KEY                 | Path to the client key to use for mTLS                                                                                                          |
| OTEL\_EXPORTER\_OTLP\_METRICS\_PROTOCOL or OTEL\_EXPORTER\_OTLP\_PROTOCOL                       | OTLP protocol. Supported values are grpc and http/protobuf. Defaults to grpc.                                                                   |
| OTEL\_METRIC\_EXPORT\_INTERVAL                                                                  | The export interval in milliseconds. Defaults to 60000.                                                                                         |
| OTEL\_METRIC\_EXPORT\_TIMEOUT                                                                   | Timeout for exporting the data in milliseconds. Defaults to 30000.                                                                              |
| OTEL\_METRICS\_EXPORTER                                                                         | Set to otlp to enable the OTLP exporter. Defaults to prometheus.                                                                                |

Refer to <https://opentelemetry.io/docs/specs/otel/protocol/exporter/> for more information about exporter configuration through environment variables. Note that the OpenTelemetry Go SDK used by Cerbos might not have full support for some of the environment variables listed on the OpenTelemetry specification.

| |  OTEL\_METRICS\_EXPORTER and OTEL\_EXPORTER\_OTLP\_METRICS\_ENDPOINT are the only required environment variables to enable OTLP metrics. |
| ------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#traces)Traces

Cerbos supports distributed tracing to provide insights into application performance and request lifecycle. Traces from Cerbos can be exported to any compatible collector that supports the OpenTelemetry protocol (OTLP).

Trace configuration should be done using [OpenTelemetry environment variables](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/). The following environment variables are supported.

| |  If you are upgrading from a Cerbos version older than 0.33.0, refer to [migration instructions](tracing.html#migration) for information about mapping file-based configuration to environment variables. |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| Environment variable                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OTEL\_SERVICE\_NAME                                                                            | Service name reported in the traces. Defaults to cerbos.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| OTEL\_TRACES\_SAMPLER                                                                          | [Trace sampler](https://opentelemetry.io/docs/specs/otel/trace/sdk/#sampling). Defaults to parentbased\_always\_off. Supported values: always\_on Record every trace. always\_off Don’t record any traces. traceidratio Record a fraction of traces based on ID. Set OTEL\_TRACES\_SAMPLER\_ARG to a value between 0 and 1 to define the fraction. parentbased\_always\_on Record all traces except those where the parent span is not sampled. parentbased\_always\_off Don’t record any traces unless the parent span is sampled. parentbased\_traceidratio Record a fraction of traces where the parent span is sampled. Set OTEL\_TRACES\_SAMPLER\_ARG to a value between 0 and 1 to define the fraction. |
| OTEL\_TRACES\_SAMPLER\_ARG                                                                     | Set the sampling ratio when OTEL\_TRACES\_SAMPLER is a ratio-based sampler. Defaults to 0.1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| OTEL\_EXPORTER\_OTLP\_TRACES\_ENDPOINT or OTEL\_EXPORTER\_OTLP\_ENDPOINT                       | Address of the OTLP collector (for example: <https://localhost:4317>). If not defined, traces are disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| OTEL\_EXPORTER\_OTLP\_TRACES\_INSECURE or OTEL\_EXPORTER\_OTLP\_INSECURE                       | Skip validating the TLS certificate of the endpoint                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| OTEL\_EXPORTER\_OTLP\_TRACES\_CERTIFICATE or OTEL\_EXPORTER\_OTLP\_CERTIFICATE                 | Path to the certificate to use for validating the server’s TLS credentials.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| OTEL\_EXPORTER\_OTLP\_TRACES\_CLIENT\_CERTIFICATE or OTEL\_EXPORTER\_OTLP\_CLIENT\_CERTIFICATE | Path to the client certificate to use for mTLS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| OTEL\_EXPORTER\_OTLP\_TRACES\_CLIENT\_KEY or OTEL\_EXPORTER\_OTLP\_CLIENT\_KEY                 | Path to the client key to use for mTLS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| OTEL\_EXPORTER\_OTLP\_TRACES\_PROTOCOL or OTEL\_EXPORTER\_OTLP\_PROTOCOL                       | OTLP protocol. Supported values are grpc and http/protobuf. Defaults to grpc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

Refer to <https://opentelemetry.io/docs/specs/otel/protocol/exporter/> for more information about exporter configuration through environment variables. Note that the OpenTelemetry Go SDK used by Cerbos might not have full support for some of the environment variables listed on the OpenTelemetry specification.

| |  OTEL\_EXPORTER\_OTLP\_TRACES\_ENDPOINT is the only required environment variable to enable OTLP trace exports. |
| ----------------------------------------------------------------------------------------------------------------- |

Schema block
====================
See [Schemas](../policies/schemas.html) for more information about schemas.

## [](#%5Fenforcement)Enforcement

`enforcement` can be set to one of the following three values:

* `none` (default): Do not validate requests using schemas
* `warn`: Validate requests and log warnings when there are validation failures
* `reject`: Deny the request if it fails validation

```yaml
schema:
  enforcement: reject
```

Server block
====================
## [](#%5Flisten%5Faddresses)Listen addresses

By default the server will start an HTTP server on port `3592` and a gRPC server on `3593` that will listen on all available interfaces.

Listen on all available interfaces (default)

```yaml
server:
  httpListenAddr: ":3592"
  grpcListenAddr: ":3593"
```

Listen on a specific interface

```yaml
server:
  httpListenAddr: "192.168.0.17:3592"
  grpcListenAddr: "192.168.0.17:3593"
```

Listen on a Unix domain socket

```yaml
server:
  httpListenAddr: "unix:/var/sock/cerbos.http"
  grpcListenAddr: "unix:/var/sock/cerbos.grpc"
```

Listen on a Unix domain socket with specific file mode

```yaml
server:
  httpListenAddr: "unix:/var/sock/cerbos.http"
  grpcListenAddr: "unix:/var/sock/cerbos.grpc"
  udsFileMode: 0o776
```

## [](#%5Fmetrics)Metrics

By default, Prometheus metrics are available to scrape from the `/_cerbos/metrics` HTTP endpoint. If you want to disable metrics reporting, set `metricsEnabled` to `false`.

```yaml
server:
  metricsEnabled: false
```

## [](#%5Fpayload%5Flogging)Payload logging

For debugging or auditing purposes, you can enable request and response payload logging for each request.

| |  Enabling this setting affects server performance and could expose potentially sensitive data contained in the requests to anyone with access to the server logs. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

```yaml
server:
  logRequestPayloads: true
```

## [](#%5Ftransport%5Flayer%5Fsecurity%5Ftls)Transport layer security (TLS)

You can enable transport layer security (TLS) by defining the paths to the certificate and key file in the `TLS` section.

```yaml
server:
  tls:
    cert: /path/to/certificate
    key: /path/to/private_key
```

| |  For production use cases that require automatic certificate reloading, workload identities and other advanced features, we recommend running a proxy server such as [Envoy](https://www.envoyproxy.io), [Ghostunnel](https://github.com/ghostunnel/ghostunnel) or [Traefik](https://traefik.io) in front of the Cerbos server. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#%5Fcors)CORS

By default, [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is enabled on the HTTP service with all origins allowed. The default allowed headers are `accept`, `content-type`, `user-agent` and `x-requested-with`. You can disable CORS by setting `server.cors.disabled` to `true`. You can also restrict the list of allowed origins and headers by setting `server.cors.allowedOrigins` and `server.cors.allowedHeaders` respectively.

```yaml
server:
  cors:
    allowedOrigins:
      - example.com
      - example.org
    allowedHeaders:
      - accept
      - content-type
      - user-agent
      - x-custom-header
      - x-requested-with
```

## [](#request-limits)Request limits

By default, each Cerbos API request can include a batch of 50 resources with up to 50 actions to be checked for each resource. This limit is in place to prevent the server from being overloaded by very large requests — which affects throughput and CPU,memory,I/O usage.

| |  Changing these settings could have a large impact on the performance and resource utilisation of Cerbos instances. |
| --------------------------------------------------------------------------------------------------------------------- |

```yaml
server:
  requestLimits:
    maxActionsPerResource: 50
    maxResourcesPerRequest: 50
```

## [](#admin-api)Enable Admin API

The [Cerbos Admin API](../api/admin%5Fapi.html) provides administration functions such as adding or updating policies (if the underlying storage engine supports it) to the running Cerbos instance. It is disabled by default.

Authentication is mandatory for the Admin API. See [Cerbos Admin API documentation](../api/admin%5Fapi.html) for more details.

| |  TLS should be enabled to ensure that credentials are transmitted securely over the network. We also highly recommend changing the default username and password when deploying Cerbos. |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

```yaml
server:
  adminAPI:
    enabled: true
    adminCredentials:
      username: cerbos
      passwordHash: JDJ5JDEwJE5HYnk4cTY3VTE1bFV1NlR2bmp3ME9QOXdXQXFROGtBb2lWREdEY2xXbzR6WnoxYWtSNWNDCgo=
```

### [](#password-hash)Generating a password hash

Cerbos expects the password to be hashed with bcrypt and encoded with base64\. This can be achieved using the `htpasswd` and `base64` utilities available on most operating systems.

```sh
echo "cerbosAdmin" | htpasswd -niBC 10 cerbos | cut -d ':' -f 2 | base64 -w0
```

| |  On MacOS, the base64 utility does not require the \-w0 argument. echo "cerbosAdmin" \| htpasswd -niBC 10 cerbos | cut -d ':' -f 2 | base64 |
| ------------------------------------------------------------------------------------------------------------------ | --------------- | ------ |

| |  The output of the above command for a given password value is not deterministic. It will vary between invocations or between different machines. This is because the bcrypt algorithm uses a salt (random noise) to make password cracking harder. |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Storage block
====================
Cerbos supports multiple backends for storing policies. Which storage driver to use is defined by the `driver` setting.

## [](#blob-driver)Blob driver

Cerbos policies can be stored in AWS S3, Google Cloud Storage, or any other S3-compatible storage systems such as [Minio](https://www.minio.io).

Configuration keys

* `bucket`: Required. A URL specifying the service (e.g. S3, GCS), the storage bucket and any other configuration parameters required by the provider.  
   * AWS S3: `s3://my-bucket?region=us-west-1`. Must specify region in the URL.  
   * Google Cloud Storage: `gs://my-bucket`  
   * S3-compatible (e.g. Minio): `s3://my-bucket?endpoint=http://my.minio.local:8080&hostname_immutable=true&region=local`. Must specify region in the URL.
* `prefix`: Optional. Look for policies only under this key prefix.
* `workDir`: Optional. Path to the local directory to download the policies to. Defaults to the system cache directory if not specified.
* `updatePollInterval`: Optional. How frequently the blob store should be checked to discover new or updated policies. Defaults to 0 — which disables polling.
* `requestTimeout`: Optional. HTTP request timeout. It takes an HTTP request to download a policy file. Defaults to 5s.
* `downloadTimeout`: Optional. Timeout to download all policies from the the storage provider. Must be greater than the `requestTimeout`. Defaults to 60s.

| |  Setting the updatePollInterval to a low value could increase resource consumption in both the client and the server systems. Some managed service providers may even impose rate limits or temporary suspensions on your account if the number of requests is too high. |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Credentials for accessing the storage buckets are retrieved from the environment. The method of specifying credentials in the environment vary by cloud provider and security configuration. Usually, it involves defining environment variables such as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` for S3 and `GOOGLE_APPLICATION_CREDENTIALS` for GCS. Refer to the relevant cloud provider documentation for more details.

* AWS: <https://docs.aws.amazon.com/sdk-for-go/api/aws/session/>
* Google: <https://cloud.google.com/docs/authentication/provide-credentials-adc>

AWS S3

```yaml
storage:
  driver: "blob"
  blob:
    bucket: "s3://my-bucket-name?region=us-east-2"
    prefix: policies
    workDir: ${HOME}/tmp/cerbos/work
    updatePollInterval: 15s
    downloadTimeout: 30s
    requestTimeout: 10s
```

Google Cloud Storage

```yaml
storage:
  driver: "blob"
  blob:
    bucket: "gs://my-bucket-name"
    workDir: ${HOME}/tmp/cerbos/work
    updatePollInterval: 10s
```

Minio local container

```yaml
storage:
  driver: "blob"
  blob:
    bucket: "s3://my-bucket-name?endpoint=http://localhost:9000&hostname_immutable=true&region=local"
    workDir: ${HOME}/tmp/cerbos/work
    updatePollInterval: 10s
```

## [](#disk-driver)Disk driver

The disk driver is a way to serve the policies from a directory on the filesystem. Any `.yaml`, `.yml` or `.json` files in the directory tree rooted at the given path will be read and parsed as policies.

Static fileset with no change detection

```yaml
storage:
  driver: disk
  disk:
    directory: /etc/cerbos/policies
```

Dynamic fileset with change detection

```yaml
storage:
  driver: disk
  disk:
    directory: /etc/cerbos/policies
    watchForChanges: true
```

| |  On some platforms the automatic change detection feature can be inefficient and resource-intensive if the watched directory contains many files or gets updated frequently. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### [](#disk-driver-archives)Archive files

Alternatively, you can opt to archive and/or compress your policies directory into a Zip (`.zip`), Tar (`.tar`) or Gzip file (`.tgz` or `.tar.gz`). The archive is assumed to be laid out like a standard policy directory. It must contain no non-policy YAML files.

You specify the file in your config like so:

Archived fileset using a Zip file

```yaml
storage:
  driver: disk
  disk:
    directory: /etc/cerbos/policies.zip
```

| |  Change detection will be disabled when using archive files. |
| -------------------------------------------------------------- |

## [](#git-driver)Git driver

Git is the preferred method of storing Cerbos policies. The server is smart enough to detect when new commits are made to the git repository and refresh its state based on the changes.

| |  Azure DevOps repositories use a newer protocol that is currently not supported by the Git library used by Cerbos. We are working to address this issue. In the mean time, please consider using the Cerbos disk storage in conjunction with an external Git sync implementation such as <https://github.com/kubernetes/git-sync> or using a CI pipeline to publish your policies to another storage implementation supported by Cerbos. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

* Git repositories can be local (`file` protocol) or remote (`ssh` or `https`). Please note that the local `file` protocol requires `git` to be available and cannot be used with the Cerbos container.
* If no `branch` is specified, the default branch would be the `master` branch.
* If no `subDir` is specified, the entire repository would be scanned for policies (`.yaml`, `.yml` or `.json`).
* The `checkoutDir` is the working directory of the server and must be writable by the server process.
* If `updatePollInterval` is set to 0, the source repository will not be polled to pick up any new commits.
* If `operationTimeout` is not specified, the default timeout for git operations is 60 seconds.

| |  If the git repository is remote, setting the updatePollInterval to a low value could increase resource consumption in both the client and the server systems. Some managed service providers may even impose rate limits or temporary suspensions on your account if the number of requests is too high. |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Local git repository

```yaml
storage:
  driver: "git"
  git:
    protocol: file
    url: file://${HOME}/tmp/cerbos/policies
    checkoutDir: ${HOME}/tmp/cerbos/work
    updatePollInterval: 10s
```

Remote git repository accessed over HTTPS

```yaml
storage:
  driver: "git"
  git:
    protocol: https
    url: https://github.com/cerbos/policy-test.git
    branch: main
    subDir: policies
    checkoutDir: ${HOME}/tmp/work/policies
    updatePollInterval: 60s
    operationTimeout: 30s
    https:
      username: cerbos
      password: ${GITHUB_TOKEN}
```

Remote git repository accessed over SSH

```yaml
storage:
  driver: "git"
  git:
    protocol: ssh
    url: github.com:cerbos/policy-test.git
    branch: main
    subDir: policies
    checkoutDir: ${HOME}/tmp/cerbos/work
    updatePollInterval: 60s
    ssh:
      user: git
      privateKeyFile: ${HOME}/.ssh/id_rsa
```

## [](#hub)Hub driver

| |  Requires a [Cerbos Hub](https://www.cerbos.dev/product-cerbos-hub) account. [![Try Cerbos Hub](../_images/try_cerbos_hub.png)](https://hub.cerbos.cloud) |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- |

Connects the PDP to a Cerbos Hub [Deployment](../../../cerbos-hub/deployments.html). A Cerbos Hub Deployment tracks a connected Git repository or a [managed Cerbos Hub store](../../../cerbos-hub/policy-stores.html) and automatically compiles, tests and pushes an optimized policy bundle to the PDP whenever a policy change is committed.

If you are new to Cerbos Hub, follow the [getting started guide](../../../cerbos-hub/getting-started.html). For more information about configuring a PDP to connect to Cerbos Hub, refer to the [Deployments documentation](../../../cerbos-hub/deployments.html).

## [](#mysql)MySQL driver

The MySQL storage backend is one of the dynamic stores that supports adding or updating policies at runtime through the [Admin API](server.html#admin-api).

| |  The [cerbosctl utility](../cli/cerbosctl.html) is a handy way to interact with the Admin API and supports loading policies through the [built-in put command](../cli/cerbosctl.html#put). |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| |  Cerbos has an in-memory cache for holding compiled policy definitions to speed up the evaluation process. When a policy is removed or updated using the [Admin API](../api/admin%5Fapi.html#policy-management) this cache is updated by the instance that handles the request. However, if you share the database with multiple Cerbos instances, the other instances won’t be aware of the change and might still have the old policy definition cached in memory. There are two ways to handle this situation. By default, the cache entries are stored indefinitely until there’s memory pressure. You can set a maximum cache duration for entries by setting the compile.cacheDuration configuration value. This could help make all the Cerbos instances to become eventually consistent within a time frame that’s acceptable to you. Setting the compile.cacheDuration to a low value helps to reach in an eventually consistent state quicker. Invoke the [/admin/store/reload API endpoint](../api/admin%5Fapi.html#store-management) on all the Cerbos instances whenever you make a change to your policies. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| |  Unlike the SQLite3 driver, the tables and other database objects are not created automatically by the Cerbos MySQL driver. This is to minimize the privileges the Cerbos instance has on the MySQL installation. You must create the required tables using the provided script before configuring Cerbos to connect to the database. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The driver configuration expects the connection details to be provided as a DSN in the following form:

[username[:password]@][protocol[(address)]]/dbname[?param1=value1&...&paramN=valueN]

See <https://github.com/go-sql-driver/mysql#dsn-data-source-name> for the list of supported parameters.

You can use environment variable references in the URL to avoid storing credentials as part of the Cerbos configuration file.

Using MySQL as a storage backend for Cerbos

```yaml
storage:
  driver: "mysql"
  mysql:
    dsn: "${MYSQL_USER}:${MYSQL_PASSWORD}@tcp(localhost:3306)/cerbos"
```

### [](#%5Fsecure%5Fconnections)Secure connections

If your MySQL server requires TLS or if you want to use RSA key pair-based password exchange, you can configure those settings as follows:

TLS certificates

```yaml
storage:
  driver: "mysql"
  mysql:
    dsn: "${MYSQL_USER}:${MYSQL_PASSWORD}@tcp(localhost:3306)/cerbos?tls=mysecuretls"
    tls:
      mysecuretls:
        caCert: /path/to/ca_certificate.crt
        cert: /path/to/certificate.crt
        key: /path/to/private.key
```

Server public key

```yaml
storage:
  driver: "mysql"
  mysql:
    dsn: "${MYSQL_USER}:${MYSQL_PASSWORD}@tcp(localhost:3306)/cerbos?serverPubKey=mypubkey"
    serverPubKey:
      mypubkey: /path/to/server_public_key.pem
```

### [](#%5Fconnection%5Fpool)Connection pool

Cerbos uses a connection pool when connecting to a database. You can configure the connection pool settings by adding a `connPool` section to the driver configuration.

Available options are:

`maxLifeTime`

The maximum length of time a connection can be reused for. This is useful when your database enforces a maximum lifetime on connections or if you have a load balancer in front of your database to spread the load.

`maxIdleTime`

How long a connection should be idle for before it is closed. Useful if you want to cleanup idle connections quickly.

`maxOpen`

Maximum number of connections that can be open at any given time (including idle connections).

`maxIdle`

Maximum number of idle connections that can be open at any given time.

| |  Connection pool settings can have a significant impact on the performance of Cerbos and your database server. Make sure you fully understand the implications of updating these settings before making any changes. |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

```yaml
storage:
  driver: "mysql"
  mysql:
    dsn: "${MYSQL_USER}:${MYSQL_PASSWORD}@tcp(localhost:3306)/cerbos"
    connPool:
      maxLifeTime: 5m
      maxIdleTime: 3m
      maxOpen: 10
      maxIdle: 5
```

### [](#%5Fconnection%5Fretries)Connection retries

Cerbos attempts to connect to the database on startup and exits if connection cannot be established after three attempts. You can configure the connection retry settings using the `connRetry` options.

`maxAttempts`

Maximum number of connection attempts before giving up

`initialInterval`

The time to wait before the second connection attempt. Subsequent attempts have increasing wait times (exponential backoff) derived from a combination of this value and the retry attempt number

`maxInterval`

Maximum amount of time to wait between retries. This affects the maximum value produced by the exponential backoff algorithm.

| |  Changing the retry settings affect the availability of Cerbos and the time it takes to detect and recover from a failure. For example, if the database connection details are incorrect or have changed, it will take longer for a Cerbos PDP to fail on startup because of retries. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#mysql-schema)Database object definitions

You can customise the script below to suit your environment. Make sure to specify a strong password for the `cerbos_user` user.

```sql
CREATE DATABASE IF NOT EXISTS cerbos CHARACTER SET utf8mb4;

USE cerbos;

CREATE TABLE IF NOT EXISTS policy (
    id BIGINT PRIMARY KEY,
    kind VARCHAR(128) NOT NULL,
    name VARCHAR(1024) NOT NULL,
    version VARCHAR(128) NOT NULL,
    scope VARCHAR(512),
    description TEXT,
    disabled BOOLEAN default false,
    definition BLOB);

CREATE TABLE IF NOT EXISTS policy_dependency (
    policy_id BIGINT NOT NULL,
    dependency_id BIGINT NOT NULL,
    PRIMARY KEY (policy_id, dependency_id),
    FOREIGN KEY (policy_id) REFERENCES policy(id) ON DELETE CASCADE);

CREATE TABLE IF NOT EXISTS policy_ancestor (
    policy_id BIGINT NOT NULL,
    ancestor_id BIGINT NOT NULL,
    PRIMARY KEY (policy_id, ancestor_id),
    FOREIGN KEY (policy_id) REFERENCES policy(id) ON DELETE CASCADE);

CREATE TABLE IF NOT EXISTS policy_revision (
    revision_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    action ENUM('INSERT', 'UPDATE', 'DELETE'),
    id BIGINT NOT NULL,
    kind VARCHAR(128),
    name VARCHAR(1024),
    version VARCHAR(128),
    scope VARCHAR(512),
    description TEXT,
    disabled BOOLEAN,
    definition BLOB,
    update_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

CREATE TABLE IF NOT EXISTS attr_schema_defs (
    id VARCHAR(255) PRIMARY KEY,
    definition JSON);

DROP TRIGGER IF EXISTS policy_on_insert;

CREATE TRIGGER policy_on_insert AFTER INSERT ON policy
FOR EACH ROW
INSERT INTO policy_revision(action, id, kind, name, version, scope, description, disabled, definition)
VALUES('INSERT', NEW.id, NEW.kind, NEW.name, NEW.version, NEW.scope, NEW.description, NEW.disabled, NEW.definition);

DROP TRIGGER IF EXISTS policy_on_update;

CREATE TRIGGER policy_on_update AFTER UPDATE ON policy
FOR EACH ROW
INSERT INTO policy_revision(action, id, kind, name, version, scope, description, disabled, definition)
VALUES('UPDATE', NEW.id, NEW.kind, NEW.name, NEW.version, NEW.scope, NEW.description, NEW.disabled, NEW.definition);

DROP TRIGGER IF EXISTS policy_on_delete;

CREATE TRIGGER policy_on_delete AFTER DELETE ON policy
FOR EACH ROW
INSERT INTO policy_revision(action, id, kind, name, version, scope, description, disabled, definition)
VALUES('DELETE', OLD.id, OLD.kind, OLD.name, OLD.version, OLD.scope, OLD.description, OLD.disabled, OLD.definition);

CREATE USER IF NOT EXISTS cerbos_user IDENTIFIED BY 'changeme';
GRANT SELECT,INSERT,UPDATE,DELETE ON cerbos.policy TO cerbos_user;
GRANT SELECT,INSERT,UPDATE,DELETE ON cerbos.attr_schema_defs TO cerbos_user;
GRANT SELECT,INSERT,UPDATE,DELETE ON cerbos.policy_dependency TO cerbos_user;
GRANT SELECT,INSERT,UPDATE,DELETE ON cerbos.policy_ancestor TO cerbos_user;
GRANT SELECT,INSERT,DELETE ON cerbos.policy_revision TO cerbos_user;
```

## [](#overlay)Overlay driver

You can provide redundancy by configuring an `overlay` driver, which wraps a `base` and a `fallback` driver. Under normal operation, the base driver will be targeted as usual. However, if the driver consistently errors, the PDP will start targeting the fallback driver instead. The fallback is determined by a configurable [circuit breaker pattern](https://learn.microsoft.com/en-us/previous-versions/msp-n-p/dn589784%28v=pandp.10%29).

You can configure the fallback error threshold and the fallback error window to determine how many errors can occur within a rolling window before the circuit breaker is tripped.

```yaml
storage:
  driver: "overlay"
  overlay:
    baseDriver: postgres
    fallbackDriver: disk
    fallbackErrorThreshold: 5 # number of errors that occur within the fallbackErrorWindow to trigger failover
    fallbackErrorWindow: 5s # the rolling window in which errors are aggregated
  disk:
    directory: policies
    watchForChanges: true
  postgres:
    url: "postgres://${PG_USER}:${PG_PASSWORD}@localhost:5432/postgres?sslmode=disable&search_path=cerbos"
```

| |  The overlay driver assumes the same interface as the base driver. Any operations that are available on the base driver but not the fallback driver will error if the circuit breaker is open and the fallback driver is being targeted. Likewise, even if the fallback driver supports additional operations compared to the base driver, these will still not be available should failover occur. |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#postgres)Postgres driver

The Postgres storage backend is one of the dynamic stores that supports adding or updating policies at runtime through the [Admin API](server.html#admin-api).

| |  The [cerbosctl utility](../cli/cerbosctl.html) is a handy way to interact with the Admin API and supports loading policies through the [built-in put command](../cli/cerbosctl.html#put). |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| |  Cerbos has an in-memory cache for holding compiled policy definitions to speed up the evaluation process. When a policy is removed or updated using the [Admin API](../api/admin%5Fapi.html#policy-management) this cache is updated by the instance that handles the request. However, if you share the database with multiple Cerbos instances, the other instances won’t be aware of the change and might still have the old policy definition cached in memory. There are two ways to handle this situation. By default, the cache entries are stored indefinitely until there’s memory pressure. You can set a maximum cache duration for entries by setting the compile.cacheDuration configuration value. This could help make all the Cerbos instances to become eventually consistent within a time frame that’s acceptable to you. Setting the compile.cacheDuration to a low value helps to reach in an eventually consistent state quicker. Invoke the [/admin/store/reload API endpoint](../api/admin%5Fapi.html#store-management) on all the Cerbos instances whenever you make a change to your policies. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| |  Unlike the SQLite3 driver, the tables and other database objects are not created automatically by the Cerbos Postgres driver. This is to minimize the privileges the Cerbos instance has on the Postgres installation. You must create the required tables using the provided script before configuring Cerbos to connect to the database. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The driver configuration expects the connection details to be provided as connection URL. See [Postgres connstring documentation](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING) for more information. Use the `search_path` parameter to point to the schema containing the Cerbos tables.

You can use environment variable references in the URL to avoid storing credentials as part of the Cerbos configuration file.

Using Postgres as a storage backend for Cerbos

```yaml
storage:
  driver: "postgres"
  postgres:
    url: "postgres://${PG_USER}:${PG_PASSWORD}@localhost:5432/postgres?sslmode=disable&search_path=cerbos"
```

### [](#%5Fconnection%5Fpool%5F2)Connection pool

Cerbos uses a connection pool when connecting to a database. You can configure the connection pool settings by adding a `connPool` section to the driver configuration.

Available options are:

`maxLifeTime`

The maximum length of time a connection can be reused for. This is useful when your database enforces a maximum lifetime on connections or if you have a load balancer in front of your database to spread the load.

`maxIdleTime`

How long a connection should be idle for before it is closed. Useful if you want to cleanup idle connections quickly.

`maxOpen`

Maximum number of connections that can be open at any given time (including idle connections).

`maxIdle`

Maximum number of idle connections that can be open at any given time.

| |  Connection pool settings can have a significant impact on the performance of Cerbos and your database server. Make sure you fully understand the implications of updating these settings before making any changes. |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

```yaml
storage:
  driver: "postgres"
  postgres:
    url: "postgres://${PG_USER}:${PG_PASSWORD}@localhost:5432/postgres?sslmode=disable&search_path=cerbos"
    connPool:
      maxLifeTime: 5m
      maxIdleTime: 3m
      maxOpen: 10
      maxIdle: 5
```

### [](#%5Fconnection%5Fretries%5F2)Connection retries

Cerbos attempts to connect to the database on startup and exits if connection cannot be established after three attempts. You can configure the connection retry settings using the `connRetry` options.

`maxAttempts`

Maximum number of connection attempts before giving up

`initialInterval`

The time to wait before the second connection attempt. Subsequent attempts have increasing wait times (exponential backoff) derived from a combination of this value and the retry attempt number

`maxInterval`

Maximum amount of time to wait between retries. This affects the maximum value produced by the exponential backoff algorithm.

| |  Changing the retry settings affect the availability of Cerbos and the time it takes to detect and recover from a failure. For example, if the database connection details are incorrect or have changed, it will take longer for a Cerbos PDP to fail on startup because of retries. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#postgres-schema)Database object definitions

You can customise the script below to suit your environment. Make sure to specify a strong password for the `cerbos_user` user.

```sql
CREATE SCHEMA IF NOT EXISTS cerbos;

SET search_path TO cerbos;

CREATE TABLE IF NOT EXISTS policy (
    id bigint NOT NULL PRIMARY KEY, 
    kind VARCHAR(128) NOT NULL,
    name VARCHAR(1024) NOT NULL,
    version VARCHAR(128) NOT NULL,
    scope VARCHAR(512),
    description TEXT,
    disabled BOOLEAN default false,
    definition BYTEA
);

CREATE TABLE IF NOT EXISTS policy_dependency (
    policy_id BIGINT,
    dependency_id BIGINT,
    PRIMARY KEY (policy_id, dependency_id),
    FOREIGN KEY (policy_id) REFERENCES cerbos.policy(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS policy_ancestor (
    policy_id BIGINT,
    ancestor_id BIGINT,
    PRIMARY KEY (policy_id, ancestor_id),
    FOREIGN KEY (policy_id) REFERENCES cerbos.policy(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS policy_revision (
    revision_id SERIAL PRIMARY KEY,
    action VARCHAR(64),
    id BIGINT,
    kind VARCHAR(128),
    name VARCHAR(1024),
    version VARCHAR(128),
    scope VARCHAR(512),
    description TEXT,
    disabled BOOLEAN, 
    definition BYTEA,
    update_timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS attr_schema_defs (
    id VARCHAR(255) PRIMARY KEY,
    definition JSON
);

CREATE OR REPLACE FUNCTION process_policy_audit() RETURNS TRIGGER AS $policy_audit$
    BEGIN
        IF (TG_OP = 'DELETE') THEN
            INSERT INTO policy_revision(action, id, kind, name, version, scope, description, disabled, definition)
            VALUES('DELETE', OLD.id, OLD.kind, OLD.name, OLD.version, OLD.scope, OLD.description, OLD.disabled, OLD.definition);
        ELSIF (TG_OP = 'UPDATE') THEN
            INSERT INTO policy_revision(action, id, kind, name, version, scope, description, disabled, definition)
            VALUES('UPDATE', NEW.id, NEW.kind, NEW.name, NEW.version, NEW.scope, NEW.description, NEW.disabled, NEW.definition);
        ELSIF (TG_OP = 'INSERT') THEN
            INSERT INTO policy_revision(action, id, kind, name, version, scope, description, disabled, definition)
            VALUES('INSERT', NEW.id, NEW.kind, NEW.name, NEW.version, NEW.scope, NEW.description, NEW.disabled, NEW.definition);
        END IF;
        RETURN NULL; 
    END;
$policy_audit$ LANGUAGE plpgsql;

CREATE TRIGGER policy_audit
AFTER INSERT OR UPDATE OR DELETE ON policy 
FOR EACH ROW EXECUTE PROCEDURE process_policy_audit();

CREATE USER cerbos_user WITH PASSWORD 'changeme';
GRANT CONNECT ON DATABASE postgres TO cerbos_user;
GRANT USAGE ON SCHEMA cerbos TO cerbos_user;
GRANT SELECT,INSERT,UPDATE,DELETE ON cerbos.policy, cerbos.policy_dependency, cerbos.policy_ancestor, cerbos.attr_schema_defs TO cerbos_user; 
GRANT SELECT,INSERT,DELETE ON cerbos.policy_revision TO cerbos_user;
GRANT USAGE,SELECT ON cerbos.policy_revision_revision_id_seq TO cerbos_user;
```

## [](#sqlite3)SQLite3 driver

The SQLite3 storage backend is one of the dynamic stores that supports adding or updating policies at runtime through the [Admin API](server.html#admin-api).

| |  The [cerbosctl utility](../cli/cerbosctl.html) is a handy way to interact with the Admin API and supports loading policies through the [built-in put command](../cli/cerbosctl.html#put). |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

In-memory ephemeral database

```yaml
storage:
  driver: "sqlite3"
  sqlite3:
    dsn: "file::memory:?cache=shared"
```

| |  Cerbos uses a database connection pool which would result in unexpected behaviour when using the SQLite:memory: database. Use file::memory:?cache=shared instead. See <https://www.sqlite.org/draft/inmemorydb.html> for details. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

On-disk persistent database

```yaml
storage:
  driver: "sqlite3"
  sqlite3:
    dsn: "file:/tmp/cerbos.sqlite?mode=rwc&cache=shared&_fk=true"
```

Telemetry
====================
Cerbos developers rely on anonymous usage data to help prioritise new features and improve the product. The information collected is completely anonymous, never shared with external entities, and you can opt out at any time.

## [](#%5Fwhat%5Fkind%5Fof%5Fdata%5Fis%5Fcollected)What kind of data is collected?

* Cerbos build information like version, commit and build date
* Operating system type and architecture
* Enabled Cerbos features (storage backend type and schema enforcement level are some examples of this information)
* Aggregated statistics about the policies like the total number of policies and average number of rules in a policy
* Aggregated statistics about Cerbos API calls and the gRPC user agents.

You can view the full schema of the telemetry data on [GitHub](https://github.com/cerbos/cerbos/tree/main/api/public/cerbos/telemetry/v1/telemetry.proto) or on the [Buf schema registry](https://buf.build/cerbos/cerbos-api/docs/main/cerbos.telemetry.v1).

We use [Rudderstack](https://www.rudderstack.com) to collect the data. Only a small number of Zenauth (the company leading the development of Cerbos) employees have access to the data.

## [](#%5Fhow%5Fto%5Fdisable%5Ftelemetry%5Fcollection)How to disable telemetry collection

There are multiple ways in which you can disable telemetry collection.

### [](#%5Fuse%5Fthe%5Fconfiguration%5Ffile)Use the configuration file

Set `telemetry.disabled: true` in the [Cerbos configuration file](index.html).

```yaml
telemetry:
  disabled: true
```

### [](#%5Fset%5Fan%5Fenvironment%5Fvariable)Set an environment variable

Set `CERBOS_NO_TELEMETRY=1` or `CERBOS_NO_TELEMETRY=true` in your environment. We also honour the `DO_NOT_TRACK` environment variable if it exists.

With the binary

```sh
CERBOS_NO_TELEMETRY=1 ./cerbos server --config=/path/to/.cerbos.yaml
```

With the container

```sh
docker run -i -t -p 3592:3592 \
    -e CERBOS_NO_TELEMETRY=true \
    ghcr.io/cerbos/cerbos:0.51.0
```

### [](#%5Fthrough%5Fthe%5Fcommand%5Fline)Through the command line

Start Cerbos with `--set=telemetry.disabled=true` command line flag.

With the binary

```sh
./cerbos server --config=/path/to/.cerbos.yaml --set=telemetry.disabled=true
```

With the container

```sh
docker run -i -t -p 3592:3592 \
    ghcr.io/cerbos/cerbos:0.51.0 \
    server --set=telemetry.disabled=true
```

Tracing block
====================
| |  The tracing block was deprecated in Cerbos 0.32.0 and removed in Cerbos 0.33.0\. Refer to [observability configuration](observability.html#traces) for information about configuring traces. |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#migration)Migrating tracing configuration from previous Cerbos versions

From Cerbos 0.32.0, the preferred method of trace configuration is through the OpenTelemetry environment variables described in [observability configuration](observability.html#traces). The `tracing` section is no longer supported by Cerbos versions starting from 0.33.0\. Native Jaeger protocol is superseded by OTLP as well and no longer supported. Follow the instructions below to migrate your existing configuration.

| Configuration setting                                            | New configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| tracing.serviceName                                              | Set OTEL\_SERVICE\_NAME environment variable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| tracing.sampleProbability                                        | Set OTEL\_TRACES\_SAMPLER to parentbased\_traceidratio and OTEL\_TRACES\_SAMPLER\_ARG to the probability value                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| tracing.jaeger.agentEndpoint or tracing.jaeger.collectorEndpoint | Jaeger now has [stable support for OTLP](https://www.jaegertracing.io/docs/1.51/apis/#opentelemetry-protocol-stable) and is the recommended way to send traces. Set OTEL\_EXPORTER\_OTLP\_TRACES\_ENDPOINT to the address of your Jaeger instance (for example: <https://your.jaeger.instance:4317>) and, optionally, set OTEL\_EXPORTER\_OTLP\_TRACES\_INSECURE=true if Jaeger is using a self-signed certificate. If you want to use the HTTP API or customize other aspects, refer to the documentation above for other supported environment variables. |
| tracing.otlp.collectorEndpoint                                   | Set OTEL\_EXPORTER\_OTLP\_TRACES\_ENDPOINT to the value of the collector endpoint and OTEL\_EXPORTER\_OTLP\_INSECURE=true to emulate the behaviour of Cerbos OTLP exporter before version 0.32.0.                                                                                                                                                                                                                                                                                                                                                           |

Deploy Cerbos to Cloud platforms
====================
## [](#%5Faws%5Fmarketplace)AWS Marketplace

Cerbos is avaliable via the [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-6kkahbtwv3gtq) and can be deployed in either [Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/) or [Elastic Container Service (ECS)](https://aws.amazon.com/ecs/). When deploying Cerbos via the Marketplace, your Cerbos Hub account is included with the purchase via AWS and no additional paid account is required.

### [](#%5Felastic%5Fkubernetes%5Fservice%5Feks)Elastic Kubernetes Service (EKS)

#### [](#%5Fstep%5F1%5Fcreate%5Fan%5Fiam%5Fpolicy)Step 1: Create an IAM policy

To deploy Cerbos from AWS Marketplace, you need to assign an IAM policy with appropriate IAM permission to a Kubernetes service account before starting the deployment. You can either use AWS managed policy `arn:aws:iam::aws:policy/AWSMarketplaceMeteringRegisterUsage` or create your own IAM policy.

Here’s an example IAM policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "aws-marketplace:RegisterUsage"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

#### [](#%5Fstep%5F2%5Fcreate%5Fan%5Fiam%5Frole%5Ffor%5Fthe%5Fkubernetes%5Fservice%5Faccount%5Firsa)Step 2: Create an IAM role for the Kubernetes service account (IRSA)

Once the IAM role has been created, a Kubernetes service account needs to be created and assicated with the role. We recommend doing this via [eksctl](https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html). The command below automates the process to:

1. Create an IAM role with AWS-managed IAM policy (or you can provide your own ARN).
2. Create a Kubernetes service account name `cerbos-serviceaccount` in the cluster.
3. Set up a trust relationship between the IAM role and the service account.
4. Modify `cerbos-serviceaccount` annotation to associate it with the created IAM role

Remember to replace `CLUSTER_NAME` with your actual Amazon EKS cluster name and optionally set the namespace.

```sh
eksctl create iamserviceaccount \
    --name cerbos-serviceaccount \
    --attach-policy-arn arn:aws:iam::aws:policy/AWSMarketplaceMeteringRegisterUsage \
    --namespace default \
    --cluster CLUSTER_NAME \
    --approve \
    --override-existing-serviceaccounts
```

#### [](#%5Fstep%5F4%5Fdeploy%5Fcerbos%5Fwith%5Fthe%5Fservice%5Faccount)Step 4: Deploy Cerbos with the service account

| |  Requires a [Cerbos Hub](https://www.cerbos.dev/product-cerbos-hub) account. [![Try Cerbos Hub](../_images/try_cerbos_hub.png)](https://hub.cerbos.cloud) |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- |

For the following steps, you need a Cerbos Hub account with a workspace connected to your policy repository and a set of client credentials. See the [Cerbos Hub getting started guide](../../../cerbos-hub/getting-started.html) for details.

* Create a new Kubernetes secret to hold the Cerbos Hub credentials. See the [Cerbos Hub guide](../../../cerbos-hub/getting-started.html) for details.  
```sh  
kubectl create secret generic cerbos-hub-credentials \  
   --from-literal=CERBOS_HUB_CLIENT_ID=YOUR_CLIENT_ID \ (1)  
   --from-literal=CERBOS_HUB_CLIENT_SECRET=YOUR_CLIENT_SECRET \ (2)  
   --from-literal=CERBOS_HUB_DEPLOYMENT_ID=YOUR_DEPLOYMENT_ID (3)  
```  
| **1** | Client ID from the Cerbos Hub credential                         |  
| ----- | ---------------------------------------------------------------- |  
| **2** | Client secret from the Cerbos Hub credential                     |  
| **3** | Cerbos Hub [Deployment ID](../../../cerbos-hub/deployments.html) |
* Create a new values file named `hub-values.yaml` with the following contents:  
```yaml  
# Assign the service account  
serviceAccount:  
  name: cerbos-serviceaccount  
# Set Cerbos configuration  
cerbos:  
  config:  
    # Configure the Hub audit backend  
    audit:  
      enabled: true <1>  
      backend: "hub"  
      hub:  
        storagePath: /audit_logs  
# Create environment variables from the secret.  
envFrom:  
  - secretRef:  
      name: cerbos-hub-credentials  
# Mount volume for locally buffering the audit logs. A persistent volume is recommended for production use cases.  
volumes:  
  - name: cerbos-audit-logs  
    emptyDir: {}  
volumeMounts:  
  - name: cerbos-audit-logs  
    mountPath: /audit_logs  
```  
| **1** | Enables audit log collection. See [Hub audit log collection documentation](../../../cerbos-hub/audit-log-collection.html) for information about masking sensitive fields and other advanced settings. |  
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
* Deploy Cerbos using the AWS Helm chart  
```sh  
aws ecr get-login-password \  
     --region us-west-1 | helm registry login \  
     --username AWS \  
     --password-stdin 709825985650.dkr.ecr.us-west-1.amazonaws.com  
helm install cerbos oci://709825985650.dkr.ecr.us-east-1.amazonaws.com/cerbos/cerbos-aws-helm  --values=hub-values.yaml  
```

### [](#%5Felastic%5Fcontainer%5Fservice%5Fecs)Elastic Container Service (ECS)

#### [](#%5Fstep%5F1%5Fcreate%5Fecs%5Ftask%5Frole%5Fpolicy)Step 1: Create ECS Task Role policy

To deploy Cerbos from AWS Marketplace, you need to create an ECS Task AIM Role with appropriate IAM permission before starting the deployment. You can either use AWS managed policy `arn:aws:iam::aws:policy/AWSMarketplaceMeteringRegisterUsage` or create your own IAM policy.

Here’s an example IAM policy required - you will need the ARN for this role when defining the task.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
          "aws-marketplace:RegisterUsage"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

#### [](#%5Fstep%5F2%5Fcreate%5Fthe%5Ftask%5Fdefinition)Step 2: Create the task definition

In the AWS console or the CLI, create the task using the following JSON definition, subsituting the values noted:

```json
{
  "family": "cerbos",
  "containerDefinitions": [
    {
      "name": "cerbos",
      "image": "709825985650.dkr.ecr.us-east-1.amazonaws.com/cerbos/cerbos:0.51.0",
      "cpu": 0,
      "portMappings": [
        {
          "name": "cerbos-3592-tcp",
          "containerPort": 3592,
          "hostPort": 3592,
          "protocol": "tcp",
          "appProtocol": "http"
        },
        {
          "name": "cerbos-3593-tcp",
          "containerPort": 3593,
          "hostPort": 3593,
          "protocol": "tcp"
        }
      ],
      "essential": true,
      "environment": [
        {
          "name": "CERBOS_HUB_CLIENT_ID",
          "value": "YOUR_CLIENT_ID" <1>
        },
        {
          "name": "CERBOS_HUB_CLIENT_SECRET",
          "value": "YOUR_CLIENT_SECRET" <2>
        },
        {
          "name": "CERBOS_HUB_WORKSPACE_SECRET",
          "value": "YOUR_WORKSPACE_SECRET" <3>
        },
        {
          "name": "CERBOS_HUB_BUNDLE",
          "value": "YOUR_LABEL" <4>
        }
      ],
      "command": [
        "server",
        "--set=audit.enabled=true", <5>
        "--set=audit.backend=hub",
        "--set=audit.hub.storagePath=/tmp"
      ],
      "environmentFiles": [],
      "mountPoints": [],
      "volumesFrom": [],
      "ulimits": [],
      "healthCheck": {
        "command": [
            "CMD",
            "/cerbos",
            "healthcheck"
        ],
        "interval": 30,
        "timeout": 5,
        "retries": 3,
        "startPeriod": 5
      },
      "systemControls": []
    }
  ],
  "taskRoleArn": "TASK_ROLE_ARN", <6>
  "executionRoleArn": "TASK_EXECUTION_ROLE_ARN", <7>
  "networkMode": "awsvpc",
  "requiresCompatibilities": [
    "FARGATE"
  ],
  "cpu": "1024",
  "memory": "3072",
  "runtimePlatform": {
    "cpuArchitecture": "X86_64",
    "operatingSystemFamily": "LINUX"
  }
}
```

| **1** | Client ID from the Cerbos Hub credential                                                                                                                                                              |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Client secret from the Cerbos Hub credential                                                                                                                                                          |
| **3** | Cerbos Hub workspace secret                                                                                                                                                                           |
| **4** | The label to watch for bundle updates. See [deployment labels documentation](#cerbos-hub:ROOT:deployment-labels.adoc) for details.                                                                    |
| **5** | Enables audit log collection. See [Hub audit log collection documentation](../../../cerbos-hub/audit-log-collection.html) for information about masking sensitive fields and other advanced settings. |
| **6** | The ARN for the custom ECS Task Role defined in Step 1.                                                                                                                                               |
| **7** | The ARN for the ECS Task Execution. The default is arn:aws:iam::<AWS\_ACCOUNT\_ID>:role/ecsTaskExecutionRole                                                                                          |

#### [](#%5Fstep%5F4%5Flaunch%5Fa%5Fservice)Step 4: Launch a service

Using the above task defintion, launch a service in your ECS Cluster. Take note to ensure the service is running attached to the security groups which your applications will be calling Cerbos from.

## [](#%5Ffly%5Fio)Fly.io

You can deploy Cerbos on Fly.io as a [Fly Launch](https://fly.io/docs/apps) app. The following `fly.toml` file shows how to deploy Cerbos with healthchecks and metrics:

```toml
app = '<APPLICATION_NAME>' (1)
primary_region = '<REGION>' (2)

[build]
  image = 'ghcr.io/cerbos/cerbos:0.51.0'

[[mounts]]
  source = 'policies'
  destination = '/policies'
  initial_size = '1GB'

[[services]]
  protocol = ''
  internal_port = 3592

[[services.ports]]
    port = 3592
    handlers = ['tls', 'http']

[[services.http_checks]]
    interval = '5s'
    timeout = '2s'
    grace_period = '5s'
    method = 'get'
    path = '/_cerbos/health'
    protocol = 'http'

[[services]]
  protocol = ''
  internal_port = 3593

[[services.ports]]
    port = 3593
    handlers = ['tls']

    [services.ports.tls_options]
      alpn = ['h2']

[[vm]]
  memory = '1gb'
  cpu_kind = 'shared'
  cpus = 1

[metrics]
  port = 3592
  path = "/_cerbos/metrics"
```

| **1** | The name of the [Fly App](https://fly.io/docs/apps)                           |
| ----- | ----------------------------------------------------------------------------- |
| **2** | Pick a Fly.io [region](https://fly.io/docs/reference/regions/#fly-io-regions) |

The example above launches a Cerbos instance with the [minimal configuration](../configuration/index.html#minimal-configuration) using an empty [Fly volume](https://fly.io/docs/reference/volumes/) mounted as the policy directory. For production use cases, consider using one of the following methods for policy storage.

| |  Your host or service for an application should be listening on the right address within the VM: Fly Proxy reaches services through a private IPv4 address on each VM, so the process should listen on 0.0.0.0:<port> ([but see A note on IPv4 and IPv6 wildcards](https://fly.io/docs/networking/app-services/#a-note-on-ipv4-and-ipv6-wildcards)). |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

* Cerbos [git driver](../configuration/storage.html#git-driver) with a Git provider such as GitHub or GitLab
* Cerbos [blob driver](../configuration/storage.html#blob-driver) with [Tigris](https://fly.io/docs/reference/tigris/#create-and-manage-a-tigris-storage-bucket)
* Cerbos [sqlite3 driver](../configuration/storage.html#sqlite3) with a standalone SQLite database or [LiteFS](https://fly.io/docs/litefs/#litefs-cloud)
* Cerbos [postgres driver](../configuration/storage.html#postgres) with [Fly Postgres](https://fly.io/docs/postgres/)
* [Cerbos Hub](https://www.cerbos.dev/product-cerbos-hub)

| |  Cerbos can be [configured entirely from the command line](../configuration/index.html) using \--set flags. On the Fly.io platform, they can be set by overriding the cmd setting in the [experimental section](https://fly.io/docs/reference/configuration/#the-experimental-section) of the fly.toml file. |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#%5Fusing%5Ftigris%5Fas%5Fa%5Fpolicy%5Frepository)Using Tigris as a policy repository

Cerbos `blob` driver can be used with any S3-compatible blob storage backend such as [Tigris](https://fly.io/docs/reference/tigris).

Create a storage bucket on Tigris. Refer to <https://fly.io/docs/reference/tigris/#create-and-manage-a-tigris-storage-bucket> for more information about creating storage buckets.

```bash
flyctl storage create
```

Note down the credentials for accessing the bucket and save them as application secrets.

```bash
flyctl apps create <APPLICATION_NAME> (1)
flyctl secrets set --app=<APPLICATION_NAME> AWS_ACCESS_KEY_ID=tid_XXXXXX (2)
flyctl secrets set --app=<APPLICATION_NAME> AWS_SECRET_ACCESS_KEY=tsec_XXXXXX (3)
```

| **1** | Your application name on Fly.io |
| ----- | ------------------------------- |
| **2** | Tigris key ID                   |
| **3** | Tigris secret access key        |

Create a `fly.toml` file.

```toml
app = '<APPLICATION_NAME>' (1)
primary_region = '<REGION>' (2)

[build]
  image = 'ghcr.io/cerbos/cerbos:0.51.0'

[experimental]
  cmd = [
    'server',
    '--set', 'storage.driver=blob',
    '--set', 'storage.blob.bucket=s3://<BUCKET_NAME>?endpoint=fly.storage.tigris.dev&region=auto', (3)
    '--set', 'storage.blob.downloadTimeout=30s',
    '--set', 'storage.blob.prefix=policies',
    '--set', 'storage.blob.updatePollInterval=15s',
    '--set', 'storage.blob.workDir=/policies'
  ]

[[mounts]]
  source = 'policies'
  destination = '/policies'
  initial_size = '1GB'

[[services]]
  protocol = ''
  internal_port = 3592
  auto_stop_machines = true

[[services.ports]]
    port = 3592
    handlers = ['tls', 'http']

[[services.http_checks]]
    interval = '5s'
    timeout = '2s'
    grace_period = '5s'
    method = 'get'
    path = '/_cerbos/health'
    protocol = 'http'

[[services]]
  protocol = ''
  internal_port = 3593
  auto_stop_machines = true

[[services.ports]]
    port = 3593
    handlers = ['tls']

    [services.ports.tls_options]
      alpn = ['h2']

[[vm]]
  memory = '1gb'
  cpu_kind = 'shared'
  cpus = 1

[metrics]
  port = 3592
  path = "/_cerbos/metrics"
```

| **1** | The name of the [Fly App](https://fly.io/docs/apps)                           |
| ----- | ----------------------------------------------------------------------------- |
| **2** | Pick a Fly.io [region](https://fly.io/docs/reference/regions/#fly-io-regions) |
| **3** | Storage bucket name                                                           |

Deploy the app.

```bash
flyctl deploy
```

### [](#%5Fusing%5Flitefs%5Fas%5Fa%5Fpolicy%5Frepository)Using LiteFS as a policy repository

Fly.io’s distributed SQLite storage layer [LiteFS](https://fly.io/docs/litefs) can be used for policy storage using Cerbos' `sqlite3` driver.

Start by creating an app on Fly.io.

```bash
flyctl apps create <APPLICATION_NAME>
```

Create a LiteFS configuration file named `litefs.yml`.

```yaml
data:
  dir: "/var/lib/litefs"

exec:
  - cmd: "/cerbos server --set=storage.driver=sqlite3 --set=storage.sqlite3.dsn=file:/litefs/db --set=server.adminAPI.enabled=true --set=server.adminAPI.adminCredentials.username=$CERBOS_ADMIN_USER --set=server.adminAPI.adminCredentials.passwordHash=$CERBOS_ADMIN_PASSWORD_HASH"

exit-on-error: false

fuse:
  dir: "/litefs"

lease:
  advertise-url: "http://${FLY_ALLOC_ID}.vm.${FLY_APP_NAME}.internal:20202"
  candidate: ${FLY_REGION == PRIMARY_REGION}
  consul:
    url: "${FLY_CONSUL_URL}"
    key: "${FLY_APP_NAME}/primary"
  promote: true
  type: "consul"
```

| |  Refer to [Configuring LiteFS](https://fly.io/docs/litefs/getting-started-docker/#configuring-litefs) documentation for other available configuration parameters. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Create a Dockerfile.

```Dockerfile
FROM flyio/litefs:0.5 AS litefs

FROM ghcr.io/cerbos/cerbos:0.51.0 AS cerbos

FROM alpine:3.16 AS base
RUN apk add fuse3 sqlite
ADD litefs.yml /etc/litefs.yml
COPY --from=cerbos /cerbos /cerbos
COPY --from=litefs /usr/local/bin/litefs /usr/local/bin/litefs

ENTRYPOINT ["litefs"]
CMD ["mount"]
```

Create a `fly.toml` file to launch Cerbos.

```toml
app = '<APPLICATION_NAME>' (1)
primary_region = '<REGION>' (2)

[build]
  dockerfile = "Dockerfile"

[mounts]
  source = "litefs"
  destination = "/var/lib/litefs" (3)

[[services]]
  protocol = ''
  internal_port = 3592

[[services.ports]]
    port = 3592
    handlers = ['tls', 'http']

[[services.http_checks]]
    interval = '5s'
    timeout = '2s'
    grace_period = '5s'
    method = 'get'
    path = '/_cerbos/health'
    protocol = 'http'

[[services]]
  protocol = ''
  internal_port = 3593

[[services.ports]]
    port = 3593
    handlers = ['tls']

    [services.ports.tls_options]
      alpn = ['h2']

[[vm]]
  memory = '1gb'
  cpu_kind = 'shared'
  cpus = 1

[metrics]
  port = 3592
  path = "/_cerbos/metrics"
```

| **1** | The name of the [Fly App](https://fly.io/docs/apps)                    |
| ----- | ---------------------------------------------------------------------- |
| **2** | Pick a [region](https://fly.io/docs/reference/regions/#fly-io-regions) |
| **3** | Destination must be equal to the one specified in the litefs.yaml      |

Create secrets to hold Cerbos Admin API credentials. Refer to [password hash generation instructions](../configuration/server.html#password-hash) to learn how to generate the password hash.

```bash
flyctl secrets set CERBOS_ADMIN_USER=<ADMIN_USER_NAME>
flyctl secrets set CERBOS_ADMIN_PASSWORD_HASH=<ADMIN_PASSWORD_HASH>
```

Attach to Consul to manage LiteFS leases.

```bash
flyctl consul attach
```

| |  See [lease configuration](https://fly.io/docs/litefs/getting-started-fly/#lease-configuration) for more information about Consul leases on Fly.io. |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- |

Finally, deploy Cerbos.

```bash
flyctl deploy
```

You can interact with the Cerbos [Admin API](../api/admin%5Fapi.html) using one of the Cerbos SDKs or the [cerbosctl](../cli/cerbosctl.html) utility to manage the policies stored on LiteFS.

List policies with cerbosctl

```bash
cerbosctl \
  --server=<APPLICATION_NAME>.fly.dev:3593 \
  --username=<ADMIN_USER_NAME> \
  --password=<ADMIN_PASSWORD> \
  get rp
```

Put a policy or a directory consisting of multiple policies with cerbosctl

```bash
cerbosctl \
  --server=<APPLICATION_NAME>.fly.dev:3593 \
  --username=<ADMIN_USER_NAME> \
  --password=<ADMIN_PASSWORD> \
  put policies -R \
  policy_dir
```

Cerbos deployment patterns
====================
Cerbos can be deployed as a service or as a sidecar. Which mode to choose depends on your requirements.

## [](#service)Service model

![Service model](_images/service_deployment.png)

* Central policy decision point shared by a group of applications.
* Cerbos can be upgraded independently from the applications — reducing maintenance overhead.
* In a busy environment, careful capacity planning would be required to ensure that the central Cerbos endpoint does not become a bottleneck.

## [](#sidecar)Sidecar model

![Sidecar model](_images/sidecar_deployment.png)

* Each application instance gets its own Cerbos instance — ensuring high performance and availability.
* Upgrades to Cerbos would require a rolling update to all the application instances.
* Policy updates could take slightly longer to propagate to all the individual application instances — resulting in a period where both the old and new policies are in effect at the same time.

## [](#daemonset)DaemonSet model

![DaemonSet model](_images/daemonset_deployment.png)

* Each cluster node gets its own Cerbos instance — ensuring high performance and efficient resource usage.
* Policy updates must roll out to nodes individually — resulting in a period where both the old and new policies are in effect at the same time.
* When deployed as a daemonset the service `internalTrafficPolicy` defaults to `Local`. This causes all requests to the service to be forced to the local node for minimum latency. Upgrades to Cerbos could result in application seeing a short outage to the cerbos instance on their own node, client retries may be neccessary. If this is unacceptable you can set `service.internalTrafficPolicy` to `Cluster`. You may be able to improve availability via the `service.kubernetes.io/topology-mode: Auto` annotation.

Deploy Cerbos as DaemonSet
====================
You can use the [Cerbos Helm chart](../installation/helm.html) to deploy Cerbos as a daemonset inside your Kubernetes cluster by setting the Helm `type` value to `daemonset`. By default, the [internal traffic policy](#https://kubernetes.io/docs/concepts/services-networking/service-traffic-policy/) is set to `Local`. You can change this by setting `service.internalTrafficPolicy` explicitly.

Refer to the [Helm chart instructions](../installation/helm.html) to learn more about using the Cerbos Helm chart.

Deploy Cerbos as a service
====================
You can use the [Cerbos Helm chart](../installation/helm.html) to deploy Cerbos as a service inside your Kubernetes cluster. Refer to the [Helm chart instructions](../installation/helm.html) for more details.

Deploy Cerbos as a sidecar
====================
The sidecar deployment model might be a preferrable option under the following circumstances:

* You have a self-contained application that does not need to share policies with other applications in your environment.
* You prefer to ship policy changes as application updates by bundling the two together.
* You are concerned about network latency.

Cerbos supports serving the API over a Unix domain socket. This allows your application container to securely communicate with the Cerbos service with no network overhead. Because the Cerbos server is only listening over a Unix domain socket, no other applications in your network will be able to communicate with it — thus providing secrecy as a bonus side effect.

The following example illustrates a Kubernetes deployment with Cerbos as a sidecar.

| |  We are using [ghostunnel](https://github.com/ghostunnel/ghostunnel) as the application container for demonstration purposes only. In a real production deployment the Cerbos endpoint should not be exposed to the network. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

```yaml
---
# Config map used to configure Cerbos.
apiVersion: v1
kind: ConfigMap
metadata:
  name: cerbos-sidecar-demo
  labels:
    app.kubernetes.io/name: cerbos-sidecar-demo
    app.kubernetes.io/component: cerbos
    app.kubernetes.io/version: "0.0.1"
data:
  ".cerbos.yaml": |-
      server:
        # Configure Cerbos to listen on a Unix domain socket.
        httpListenAddr: "unix:/sock/cerbos.sock"
      storage:
        driver: disk
        disk:
          directory: /policies
          watchForChanges: false
---
# Application deployment with Cerbos as a sidecar.
# Note that in this example we are simply proxying requests received
# by the main application (application container) to the Cerbos
# sidecar (`cerbos` container) for demonstration purposes. In a real
# production deployment the main application would not expose Cerbos
# to the outside world at all. It would communicate with the Cerbos
# sidecar privately to make policy decisions about the actions that
# it is performing.
#
# Bonus: You can re-purpose this example to deploy Cerbos in an
# environment that requires SPIFFE workload identities and/or
# regular certificate rotation and access restrictions. See the
# ghostunnel documentation at https://github.com/ghostunnel/ghostunnel
# for more information.
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cerbos-sidecar-demo
  labels:
    app.kubernetes.io/name: cerbos-sidecar-demo
    app.kubernetes.io/component: cerbos-sidecar-demo
    app.kubernetes.io/version: "0.0.1"
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: cerbos-sidecar-demo
      app.kubernetes.io/component: cerbos-sidecar-demo
  template:
    metadata:
      labels:
        app.kubernetes.io/name: cerbos-sidecar-demo
        app.kubernetes.io/component: cerbos-sidecar-demo
    spec:
      containers:
        ########################################################################
        # Application container. Replace with your own application definition. #
        ########################################################################
        - name: application
          image: "ghostunnel/ghostunnel"
          imagePullPolicy: IfNotPresent
          args:
            - "server"
            - "--listen=:3592"
            - "--target=unix:/sock/cerbos.sock"
            - "--cert=/certs/tls.crt"
            - "--key=/certs/tls.key"
            - "--disable-authentication"
          ports:
            - name: http
              containerPort: 3592
          livenessProbe:
            httpGet:
              path: /_cerbos/health
              port: http
              scheme: HTTPS
          readinessProbe:
            httpGet:
              path: /_cerbos/health
              port: http
              scheme: HTTPS
          volumeMounts:
            # Mount the shared volume containing the socket
            - name: sock
              mountPath: /sock
            - name: certs
              mountPath: /certs
        ##################
        # Cerbos sidecar #
        ##################
        - name: cerbos
          image: "ghcr.io/cerbos/cerbos:0.51.0"
          imagePullPolicy: IfNotPresent
          args:
            - "server"
            - "--config=/config/.cerbos.yaml"
            - "--log-level=INFO"
          volumeMounts:
            # Mount the shared volume containing the socket
            - name: sock
              mountPath: /sock
            - name: config
              mountPath: /config
              readOnly: true
            - name: policies
              mountPath: /policies
      volumes:
        # Shared volume containing the socket.
        - name: sock
          emptyDir: {}
        - name: config
          configMap:
            name: cerbos-sidecar-demo
        - name: certs
          secret:
            secretName: cerbos-sidecar-demo
        - name: policies
          emptyDir: {}
---
# Use cert-manager to issue a certificate to the application.
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: cerbos-sidecar-demo
  labels:
    app.kubernetes.io/name: cerbos-sidecar-demo
    app.kubernetes.io/component: cerbos-sidecar-demo
    app.kubernetes.io/version: "0.0.1"
spec:
  isCA: true
  secretName: cerbos-sidecar-demo
  dnsNames:
    - cerbos-sidecar-demo.default.svc.cluster.local
    - cerbos-sidecar-demo.default.svc
    - cerbos-sidecar-demo.default
    - cerbos-sidecar-demo
  issuerRef:
    name: selfsigned-cluster-issuer
    kind: ClusterIssuer
    group: cert-manager.io
```

Deploy Cerbos to Serverless/FaaS environments
====================
## [](#aws-lambda)AWS Lambda

| |  Cerbos is a CPU-bound application. On AWS Lambda environments CPU is not individually configurable and is determined as a function of allocated memory (see [Configure Lambda function memory](https://docs.aws.amazon.com/lambda/latest/dg/configuration-memory.html)). If you’re experiencing slow response times from Cerbos, increase the memory allocation. Even though neither Cerbos nor your code requires a lot of memory, the architecture of AWS Lambda forces this counter-intuitive tuning advice. Because each application is different, we can’t provide any recommendations. Monitor your application and tune the memory allocation until the performance is satisfactory for your needs. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Cerbos provides two deployment options for AWS Lambda:

### [](#%5Fcerbos%5Flambda%5Ffunction)Cerbos Lambda Function

Deploy Cerbos as a standalone AWS Lambda function that handles authorization requests directly. This deployment pattern is suitable for centralized authorization services.

Download the appropriate `cerbos_aws_lambda_func` tarball from the [releases page](https://github.com/cerbos/cerbos/releases/tag/v0.51.0). It contains a specially-built binary named `bootstrap` that can be deployed as either a Zip package or a container image.

Deploying it as a zip package requires creating a zip file with the `bootstrap` binary at the root. See [Deploy Go Lambda functions with .zip file archives](https://docs.aws.amazon.com/lambda/latest/dg/golang-package.html) for more information.

Lambda Function deployment with a zip package

```shell
mkdir -p dist
sam deploy --template sam.yml --stack-name ${CERBOS_STACK_NAME:-Cerbos} --resolve-s3 \
    --capabilities CAPABILITY_IAM --no-confirm-changeset --no-fail-on-empty-changeset
```

SAM template for Lambda Function deployment with a zip package

```yaml
---

AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: Cerbos Lambda Function

Globals:
  Function:
    Timeout: 5

Resources:
  CerbosFunction:
    Type: AWS::Serverless::Function
    Properties:
      Runtime: provided.al2
      CodeUri: dist/
      Handler: bootstrap
      Architectures:
        - arm64
      MemorySize: 1024
      Events:
        CheckResources:
          Type: HttpApi
          Properties:
            Path: /api/check/resources
            Method: POST
        PlanResources:
          Type: HttpApi
          Properties:
            Path: /api/plan/resources
            Method: POST
        HealthCheck:
          Type: HttpApi
          Properties:
            Path: /
            Method: GET
      Environment:
        Variables:
          CERBOS_LOG_LEVEL: debug
          XDG_CACHE_HOME: /tmp
          CERBOS_CONFIG: /.cerbos.yaml

Outputs:
  CerbosFunctionAPI:
    Description: "API Gateway endpoint URL for Cerbos Function"
    Value: !Sub "https://${ServerlessHttpApi}.execute-api.${AWS::Region}.amazonaws.com"
  CerbosFunction:
    Description: "Cerbos Lambda Function ARN"
    Value: !GetAtt CerbosFunction.Arn
  CerbosFunctionIamRole:
    Description: "IAM Role created for the Cerbos Lambda function"
    Value: !GetAtt CerbosFunctionRole.Arn
```

To deploy as a container, build an image using a Dockerfile similar to the following:

```dockerfile
FROM public.ecr.aws/lambda/provided:al2023
COPY bootstrap /bootstrap
ENTRYPOINT [ "/bootstrap" ]
```

See [Deploy Go Lambda functions with container images](https://docs.aws.amazon.com/lambda/latest/dg/go-image.html) for more information.

### [](#%5Fcerbos%5Flambda%5Fextension%5Flayer)Cerbos Lambda Extension (Layer)

Lambda function deployed as a Zip package can have up to five layers. Primary use case for [layers](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html) is managing dependencies and configurations. Additionally, a layer can be used to deploy a Lambda function [extension](https://docs.aws.amazon.com/lambda/latest/dg/lambda-extensions.html). Deploying Cerbos PDP as a Lambda extension allows it to run on the same host with your application function. This deployment pattern is similar to a sidecar deployment.

Download the appropriate `cerbos_aws_lamba_ext` tarball from the [releases page](https://github.com/cerbos/cerbos/releases/tag/v0.51.0). It contains a specially-built `cerbosext` binary that can be deployed as a Zip layer. The (extension) layer then can be attached to your AWS Lambda function, if it is deployed as a Zip package. See [adding layers](https://docs.aws.amazon.com/lambda/latest/dg/adding-layers.html) for more information.

Lambda Extension deployment

```shell
mkdir -p layer/extensions
mv cerbosext layer/extensions/
sam deploy --template sam.yml --stack-name ${CERBOS_STACK_NAME:-Cerbos} --resolve-s3 \
    --capabilities CAPABILITY_IAM --no-confirm-changeset --no-fail-on-empty-changeset
```

SAM template for Lambda Extension deployment

```yaml
---

AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: Cerbos server

Globals:
  Function:
    Timeout: 5

Resources:
  CerbosExtensionLayer:
    Type: AWS::Serverless::LayerVersion
    Properties:
      LayerName: cerbos-extension
      Description: Cerbos extension layer
      ContentUri: ./layer (1)
      CompatibleRuntimes:
        - provided.al2
        - provided.al2023
      CompatibleArchitectures:
        - arm64

Outputs:
  CerbosExtensionLayerArn:
    Description: "Cerbos Extension Layer ARN"
    Value: !Ref CerbosExtensionLayer
```

| **1** | Layer is a directory containing the cerbosext binary |
| ----- | ---------------------------------------------------- |

### [](#%5Fconfiguration)Configuration

| |  Cerbos Lambda extension overrides server.httpListenAddr and server.grpcListenAddr to "unix:/tmp/cerbos.http.sock" and "unix:/tmp/cerbos.grpc.sock" respectively. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The Cerbos function/extension can be configured with environment variables.

```yaml
CERBOS_LOG_LEVEL: info
XDG_CACHE_HOME: /tmp
CERBOS_CONFIG: "..." (1)
```

| **1** | Path to the Cerbos configuration file |
| ----- | ------------------------------------- |

Set the following environment variables to connect to [Cerbos Hub](https://www.cerbos.dev/product-cerbos-hub).

```yaml
CERBOS_HUB_DEPLOYMENT_ID: "..."
CERBOS_HUB_CLIENT_ID: "..."
CERBOS_HUB_CLIENT_SECRET: ".."
```

### [](#%5Fcomparison%5Ffunction%5Fvs%5Fextension)Comparison: Function vs Extension

| Aspect                 | Lambda Function               | Lambda Extension                              |
| ---------------------- | ----------------------------- | --------------------------------------------- |
| **Deployment Pattern** | Centralized service           | Sidecar pattern                               |
| **Resource Sharing**   | Dedicated Lambda execution    | Shares execution with application function    |
| **Cold Start**         | Independent cold start        | Shared cold start with application            |
| **Network Overhead**   | API Gateway + Lambda runtime  | Direct process communication                  |
| **Use Case**           | Central authorization service | Embedded authorization for specific functions |
| **Scaling**            | Independent scaling           | Scales with application function              |

Both deployment options use AWS SAM (Serverless Application Model) templates for easy deployment and include example configurations for policies, logging, and API Gateway integration.

Deploy Cerbos as a systemd service
====================
The [Cerbos Linux packages](../installation/binary.html#linux-packages) will automatically create a systemd service during installation. If you are using the tarballs to create a custom installation, you can modify the following sample systemd service definition to match your requirements.

```toml
[Unit]
Description=Cerbos Policy Decision Point

[Service]
ExecStart=/usr/local/bin/cerbos server --config=/etc/cerbos.yaml
ProtectSystem=full
ProtectHome=true
PrivateUsers=true
PrivateTmp=true
DynamicUser=yes

[Install]
WantedBy=multi-user.target
```

Refer to [systemd documentation](https://www.freedesktop.org/software/systemd/man/systemd.exec.html) for more information about available configuration options.

Why we built Cerbos this way
====================
Welcome! The purpose of this section is to give some insight into how decisions were made when designing and building Cerbos, for the more _curious_ of our users.

* [Why Cerbos runs as a separate process](why%5Fcerbos%5Fruns%5Fas%5Fa%5Fseparate%5Fprocess.html)

Why Cerbos runs as a separate process
====================
If you’re used to traditional authorization approaches, you’d be surprised to find that Cerbos is not a library that you can embed into your application. Instead, Cerbos is designed to be run as a sidecar or a service alongside your application. There are several reasons why we have chosen this approach. To provide a bit of background, let’s consider how modern software development works in the era of cloud native computing.

Nowadays, the trend is towards microservice architectures where system functionality is split between multiple services that are fairly independent of each other. They are probably owned by different teams within the organization and even developed using different programming languages and tools. Automated CI/CD pipelines deploy new versions of these services many times a day.

![organization](_images/organisation.png)

In these dynamic, polyglot environments, the emergent pattern for providing cross-cutting concerns such as service discovery, resiliency, observability and security in a standardized way is through the use of sidecars or other microservices. Frameworks such as [Dapr](https://dapr.io) and service meshes such as [Istio](https://istio.io) and [Linkerd](https://linkerd.io) are examples of software that employ this pattern.

Authorization is one of those cross-cutting concerns that needs to be standardized and centrally managed across the organization. If authorization rules for the same resource are even slightly different between two services, then that creates a security issue. In a polyglot environment, the implementation of access rules would be duplicated between each programming language. This is a waste of effort and an inevitable source of inconsistencies and bugs due to how programmers interpret the specifications or how the particular programming language deals with certain data types or special cases.

Changing access rules for the whole organization requires coordinated effort to develop, test and roll out those changes across the whole fleet. Debugging authorization problems in such an environment is quite difficult because no one has overall visibility of the whole system. The access logic is hidden away in code in multiple repositories. Unless the developers have been extremely disciplined, the quality of debugging aids such as traces, audit trails and tests would vary wildly as well.

## [](#%5Fenter%5Fcerbos)Enter Cerbos…​

Cerbos is designed to address most of the above problems:

* Access policies are human-readable and stored in a central repository so that all stakeholders have visibility over the security rules implemented in their organization.
* Logs, traces, metrics and audit trails are available out of the box and there are supplementary tools such as a policy testing framework, linter and a REPL for debugging issues.
* Cerbos automatically detects changes to policies and updates itself on the fly. This makes rollout of access policy changes easy and almost instantaneous. For most changes, this means that the dependent services don’t need to have their code updated and rolled out to production. It saves development time and deployment headaches.
* Offering Cerbos as a decoupled API allows it to be used by any application or service written in any language while providing a consistent experience across the board. Cerbos facilitates sharing access control logic across different services and applications and gets rid of inherent code duplication, inconsistent implementations, version drift and maintenance burden.

By not having to worry about wrapping and shipping Cerbos features into language specific, embeddable libraries, we can focus our time and energy into optimizing the product and building new features using a smaller set of libraries and utilities provided by the language of our choice. We can test these features much more thoroughly because we have full control over all the integration points. We don’t have to be concerned about integrating or being compatible with an almost unlimited set of libraries and frameworks available for every programming language. And we don’t have to expend effort figuring out how to share common code across different languages, fight with language quirks and performance hotspots like foreign function interfaces and concurrency primitives.

Glossary of Cerbos terms
====================
ACTION

Any application-defined operation that could be performed on a `**RESOURCE**`. Actions could be coarse-grained like `create`, `update`, `delete`, `view` or fine-grained like `view:public`, `update:invoice_amt`. What actions are possible is determined by the application developers and they can use [Cerbos policies](../policies/index.html) to define the rules that must be satisfied in order for a given `**PRINCIPAL**` to perform one of those actions on a `**RESOURCE INSTANCE**`.

ATTRIBUTE

A piece of information about a `**PRINCIPAL**` or a `**RESOURCE INSTANCE**` that is useful for making an access decision. Cerbos is stateless and has no access to your application data. In order to make access decisions, Cerbos needs to know relevant information about the users and the objects they are trying to access. This information is sent as `attributes` in the Cerbos API request. For example, if you want to restrict users from a particular geography to access only objects from that same geography, you might define a Cerbos rule condition like `request.resource.attr.geography == request.principal.attr.geography`. Then, in the Cerbos API request, you must send the `geography` attribute (as determined by your application) for both the principal and the resource instance.

CONDITION

Cerbos policy rules can make dynamic, context-aware decisions by evaluating conditional logic against the `**ATTRIBUTES**` sent through the API request. See [Conditions](../policies/conditions.html) for details.

DERIVED ROLE

Most applications have a statically defined set of roles such as `admin`, `writer`, `employee` and so on. Cerbos derived roles are a feature in which these static roles can be dynamically augmented with context-awareness. For example, someone with the `employee` role can be augmented to `us_employee` by checking whether their location is in the USA. Cerbos policies can then be written to target the `us_employee` derived role instead of the `employee` role — which removes repetition of logic across policy files. See [Derived roles](../policies/derived%5Froles.html) for details.

PDP

Policy decision point. Essentially, where policies are executed and decisions are made. When you start a Cerbos server through one of the distribution artefacts (binary, container, Helm chart), you start a PDP.

PRINCIPAL

A human or an automated process that wants to perform one or more `**ACTIONS**` on one or more `**RESOURCE INSTANCES**`. Typically called a "user" in most settings but Cerbos uses the term `Principal` to avoid any ambiguity about whether the user is human or not. You can create [principal policies](../policies/principal%5Fpolicies.html) to create exceptions for particular users.

RESOURCE

A kind or a category of application objects with similar characteristics. The concept is very similar to a `class` in object-oriented programming. For example, in an inventory system, `Invoice` is a resource. Your system might have thousands or millions of invoices (`**RESOURCE INSTANCES**`: similar to `objects` in object-oriented programming) but there would only be a single Cerbos [resource policy](../policies/resource%5Fpolicies.html) for `Invoice` which encodes all the access rules.

| |  Sometimes the term resource is used to refer to a **RESOURCE INSTANCE** when the meaning is obvious from the context (the [API request fields](../api/index.html) are a good example of this). |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

RESOURCE INSTANCE

A specific item of a `**RESOURCE**` kind. If a `**RESOURCE**` is a `class`, a `**RESOURCE INSTANCE**` is an `object` of that class. For example, an invoice that was issued to "Acme Corp." with ID "I23456" is a `**RESOURCE INSTANCE**`. When making access decisions using Cerbos, you need to send information about the _resource instances_ to the Cerbos `CheckResources` API endpoint. The Cerbos `**PDP**` would then use the appropriate resource policy (determined by the `kind` specified in the resource instance) to process the information and make an access decision.

Policy authoring
====================
## [](#%5Ftips%5Ffor%5Fworking%5Fwith%5Fpolicies)Tips for working with policies

* Policies can be in either YAML or JSON formats. Accepted file extensions are `.yml`, `.yaml` or `.json`. All other extensions are ignored.
* The JSON schemas for Cerbos files are available at:  
   * Policy  
         * `<https://api.cerbos.dev/v0.51.0/cerbos/policy/v1/Policy.schema.json>`  
   * [Test suite](compile.html#testing)  
         * `<https://api.cerbos.dev/v0.51.0/cerbos/policy/v1/TestSuite.schema.json>`  
   * [Principal test fixtures](compile.html#fixtures)  
         * `<https://api.cerbos.dev/v0.51.0/cerbos/policy/v1/TestFixture/Principals.schema.json>`  
   * [Resources test fixtures](compile.html#fixtures)  
         * `<https://api.cerbos.dev/v0.51.0/cerbos/policy/v1/TestFixture/Resources.schema.json>`  
   * [Auxiliary data test fixtures](compile.html#fixtures)  
         * `<https://api.cerbos.dev/v0.51.0/cerbos/policy/v1/TestFixture/AuxData.schema.json>`
* If you prefer to always use the latest version, they can be accessed at:  
   * `<https://api.cerbos.dev/latest/cerbos/policy/v1/Policy.schema.json>`  
   * `<https://api.cerbos.dev/latest/cerbos/policy/v1/TestSuite.schema.json>`  
   * `<https://api.cerbos.dev/latest/cerbos/policy/v1/TestFixture/Principals.schema.json>`  
   * `<https://api.cerbos.dev/latest/cerbos/policy/v1/TestFixture/Resources.schema.json>`  
   * `<https://api.cerbos.dev/latest/cerbos/policy/v1/TestFixture/AuxData.schema.json>`

## [](#%5Fpolicy%5Fstructure)Policy structure

* The policy header is common for all policy types:  
   * `apiVersion`: Required. Must be `api.cerbos.dev/v1`.  
   * `description`: Optional. Description of the policy.  
   * `disabled`: Optional. Set to `true` to make the Cerbos engine ignore this policy file.  
   * `metadata.sourceFile`: Optional. Set to the source of the policy data for auditing purposes.  
   * `metadata.annotations`: Optional. Key-value pairs of strings holding free-form data for auditing purposes.
* Resource names, actions, and principal names can be hierarchical. Use `:` as the delimiter. For example: `app:component:resource`.
* Wildcard matches are allowed on certain fields. Wildcards respect the hierarchy delimiter `:`.
* [Scoped policies](scoped%5Fpolicies.html) (optional) are handy for use cases like multi-tenancy where you may want to override particular rules for some tenants.
* See [Conditions](conditions.html) to learn how to write conditions in policy rules.
* See [Schemas](schemas.html) to learn how you can define schemas for validating requests.
* See [Best practices](best%5Fpractices.html) to check out a growing collection of snippets detailing the optimal way to write policies.

## [](#%5Fediting%5Fpolicies)Editing policies

The quickest and the easiest way to get familiar with Cerbos policies is to use the [online playground](https://play.cerbos.dev). It provides an IDE-like experience with an interactive editor, examples, code snippets, test cases and other useful utilities to help you design policies.

### [](#%5Feditor%5Fconfigurations)Editor configurations

Editors with support for the [Language Server Protocol (LSP)](https://microsoft.github.io/language-server-protocol/) can make use of the [YAML language server](https://github.com/redhat-developer/yaml-language-server) implementation when working with Cerbos policies. Simply add the following line at the beginning of your policy file to get context-sensitive code suggestions and validation messages from the editor.

```yaml
# yaml-language-server: $schema=https://api.cerbos.dev/latest/cerbos/policy/v1/Policy.schema.json
```

The same method can be used for [tests](compile.html#testing):

```yaml
# yaml-language-server: $schema=https://api.cerbos.dev/latest/cerbos/policy/v1/TestSuite.schema.json
```

[Resource fixtures](compile.html#fixtures) for tests:

```yaml
# yaml-language-server: $schema=https://api.cerbos.dev/latest/cerbos/policy/v1/TestFixture/Resources.schema.json
```

[Principal fixtures](compile.html#fixtures) for tests:

```yaml
# yaml-language-server: $schema=https://api.cerbos.dev/latest/cerbos/policy/v1/TestFixture/Principals.schema.json
```

[Auxiliary data fixtures](compile.html#fixtures) for tests:

```yaml
# yaml-language-server: $schema=https://api.cerbos.dev/latest/cerbos/policy/v1/TestFixture/AuxData.schema.json
```

YAML language server also supports per-directory settings. If all your Cerbos policies are contained in a specific directory, you can configure the editor to always use the correct schema for the YAML files in that directory. Refer to the [YAML language server documentation](https://github.com/redhat-developer/yaml-language-server#language-server-settings=) for more information.

Example: Apply the schema to all files in the /cerbos directory

```yaml
yaml.schemas: {
    "https://api.cerbos.dev/latest/cerbos/policy/v1/Policy.schema.json": "/cerbos/*",
    "https://api.cerbos.dev/latest/cerbos/policy/v1/TestSuite.schema.json": "/cerbos/**/*_test.yaml",
    "https://api.cerbos.dev/latest/cerbos/policy/v1/TestFixture/Resources.schema.json": "/cerbos/**/testdata/resources.yaml",
    "https://api.cerbos.dev/latest/cerbos/policy/v1/TestFixture/Principals.schema.json": "/cerbos/**/testdata/principals.yaml",
    "https://api.cerbos.dev/latest/cerbos/policy/v1/TestFixture/AuxData.schema.json": "/cerbos/**/testdata/auxdata.yaml"
}
```

JSON files can specify the schema using the `$schema` top-level property.

```json
"$schema": "https://api.cerbos.dev/latest/cerbos/policy/v1/Policy.schema.json",
```

#### [](#%5Fneovim)Neovim

Refer to your plugin manager documentation to figure out how to install [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig/tree/master) and [configure the yaml-language-server](https://github.com/neovim/nvim-lspconfig/blob/master/doc/server%5Fconfigurations.md#yamlls). Plugins such as [mason-lspconfig](https://github.com/williamboman/mason-lspconfig.nvim) can automatically download and install language servers as well.

The following is an example of using [lazy.nvim](https://github.com/folke/lazy.nvim) and [mason.nvim](https://github.com/williamboman/mason.nvim) to install and configure yaml-language-server. It follows the [recommended way of configuring lazy plugins](https://github.com/folke/lazy.nvim#-structuring-your-plugins).

\~/.config/nvim/lua/plugins/lspconfig.lua

```lua
return {
    {
        "neovim/nvim-lspconfig",
        dependencies = {
            {
                "williamboman/mason.nvim",
            },
            {
                "williamboman/mason-lspconfig.nvim",
                opts = {
                    ensure_installed = { "yamlls" },
                },
            },
        },
        opts = {
            servers = {
                yamlls = {
                    settings = {
                        yaml = {
                            schemas = {
                                "https://api.cerbos.dev/latest/cerbos/policy/v1/Policy.schema.json": "/cerbos/*",
                                "https://api.cerbos.dev/latest/cerbos/policy/v1/TestSuite.schema.json": "/cerbos/**/*_test.yaml",
                                "https://api.cerbos.dev/latest/cerbos/policy/v1/TestFixture/Resources.schema.json": "/cerbos/**/testdata/resources.yaml",
                                "https://api.cerbos.dev/latest/cerbos/policy/v1/TestFixture/Principals.schema.json": "/cerbos/**/testdata/principals.yaml",
                                "https://api.cerbos.dev/latest/cerbos/policy/v1/TestFixture/AuxData.schema.json": "/cerbos/**/testdata/auxdata.yaml"
                            },
                        },
                    },
                },
            },
        },
    }
}
```

#### [](#%5Fjetbrains%5Fides)JetBrains IDEs

Navigate to the **Preferences** **Languages & Frameworks** **Schemas and DTDs** **JSON Schema Mappings** in JetBrains IDE of your choice.

Add an entry with the following configuration:

Name: Cerbos
Schema file or URL: https://api.cerbos.dev/latest/cerbos/policy/v1/Policy.schema.json
Schema version: JSON Schema Version 7
File path pattern: cerbos/*

![JetBrains JSON Schema Mappings menu](_images/jetbrains-menu.png)

| |  In the example above, the schema is applied to all files in the cerbos directory. |
| ------------------------------------------------------------------------------------ |

#### [](#%5Fvisual%5Fstudio%5Fcode)Visual Studio Code

If you are new to Visual Studio Code, refer to the[documentation](https://code.visualstudio.com/docs/getstarted/settings) for more information about how to change settings.

Install the YAML language server extension from <https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml>

After the extension is installed, hit Ctrl+, or **File** **Preferences** **Settings** to edit settings. Expand **Extensions** **YAML**, click `Edit in settings.json` under `Yaml: Schemas`. and add the following snippet:

```json
{
  "yaml.schemas": {
    "https://api.cerbos.dev/latest/cerbos/policy/v1/Policy.schema.json": "cerbos/*",
    "https://api.cerbos.dev/latest/cerbos/policy/v1/TestSuite.schema.json": "/cerbos/**/*_test.yaml",
    "https://api.cerbos.dev/latest/cerbos/policy/v1/TestFixture/Resources.schema.json": "/cerbos/**/testdata/resources.yaml",
    "https://api.cerbos.dev/latest/cerbos/policy/v1/TestFixture/Principals.schema.json": "/cerbos/**/testdata/principals.yaml",
    "https://api.cerbos.dev/latest/cerbos/policy/v1/TestFixture/AuxData.schema.json": "/cerbos/**/testdata/auxdata.yaml"
  }
}
```

| |  In the example above, the schema is applied to all files in the cerbos directory. |
| ------------------------------------------------------------------------------------ |

Best practices and recipes
====================
A collection of tips and code snippets designed to help you write cleaner, more optimised Cerbos policies.

## [](#%5Fmodelling%5Fpolicies)Modelling policies

With Cerbos, access rules are always resource-oriented and the policies you write map to these resources within your system. A _resource_ can be anything, and the way you model your policies is up you — you can achieve the same logical outcome in numerous ways; action-led, role-led, attribute-led, or with combinations thereof.

That said, some patterns will lend themselves more naturally to certain scenarios — let’s take a look at some different approaches. Consider this business model:

| _Actions_ | _Roles_     |             |      |     |   |
| --------- | ----------- | ----------- | ---- | --- | - |
| IT\_ADMIN | JR\_MANAGER | SR\_MANAGER | USER | CFO |   |
| run       | x           | x           | x    |     |   |
| view      | x           | x           | x    | x   | x |
| edit      | x           | x           |      |     |   |
| save      | x           | x           |      |     |   |
| share     | x           | x           | x    |     |   |

Representing this as a resource policy could be achieved in a variety of ways. Let’s take a look at each:

### [](#%5Faction%5Fled)Action-led

Here, we focus on an action, and list all the roles that can perform that action:

```yaml
# Principals in the following three roles can perform the `run` action
  - actions:
      - "run"
    effect: EFFECT_ALLOW
    roles:
      - JR_MANAGER
      - SR_MANAGER
      - CFO

# All principals can perform the `view` action
  - actions:
      - "view"
    effect: EFFECT_ALLOW
    roles:
      - ["*"]
```

This approach might be suitable if any of the following apply to your system:

* Your roles are "similar" in what they can do like `JR_MANAGER` and `SR_MANAGER`; it’s likely that `JR_MANAGER` will have a subset of the permissions of `SR_MANAGER`. There will of course be duplication in either direction, but it’s often easier to reason about this from an action perspective.
* You have "high-risk" actions — you want to be able to tell at a glance which roles have access to a particular action. The act of explicitly listing roles per action makes it much more difficult to accidentally give unwanted permissions to the wrong user.
* You have a relatively high number of roles to a low number of actions.

### [](#%5Frole%5Fled)Role-led

Alternatively, we can focus on a role, and list all the actions the role can perform:

```yaml
# These three actions can be performed by principals in the `JR_MANAGER` role
  - actions:
      - "run"
      - "view"
      - "share"
    effect: EFFECT_ALLOW
    roles:
      - JR_MANAGER
```

You might opt for a role-led approach if:

* You have distinct roles where it’s rare for your roles to share common actions.
* You have a relatively low number of roles to a high number of actions.

### [](#%5Fhybrid)Hybrid

Perhaps we want to use a combination of the two:

```yaml
# Principals in the `SR_MANAGER` or `CFO` roles can perform all actions
  - actions:
      - "*"
    effect: EFFECT_ALLOW
    roles:
      - SR_MANAGER
      - CFO
```

This might apply if your scenario doesn’t strictly fall into one of the previous two sections; individually, or at all.

### [](#%5Fblanket%5Fallow%5Fgranular%5Fdeny)Blanket allow, granular deny

We can opt to explicitly state which actions a user **cannot** do:

```yaml
# Principals in the `JR_MANAGER` role can perform all actions, other than `edit` and `save`
  - actions:
      - "*"
    effect: EFFECT_ALLOW
    roles:
      - "JR_MANAGER"

  - actions:
      - "edit"
      - "save"
    effect: EFFECT_DENY
    roles:
      - "JR_MANAGER"
```

This would suit scenarios where a principal can perform _nearly_ every action, and you want to explicitly list disallowed actions.

### [](#%5Fattribute%5Fled)Attribute-led

Consider the following hypothetical scenario:

An organization models its resources as specific _data sets_. Each data set is unique, as are the principals trying to access them. The organization uses JWTs extensively to manage and transmit identity/contextual information. The resource policies map 1:1 to each data set, and access is governed by arbitrary information (in this case, passed within the JWT).

Given the dynamic nature of audiences, it’s not practical to enumerate all roles that have access. What we could do instead is to globally allow all roles and actions and then determine access based on attributes passed in the JWT. Take a look at the following example policy:

```yaml
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  resource: "data_set"
  version: default
  rules:
    - actions: ["*"]
      roles: ["*"]
      effect: EFFECT_ALLOW
      condition:
        match:
          all:
            of:
              - expr: has(request.aux_data.jwt.aud)
              - expr: >
                  "my.custom.audience" in request.aux_data.jwt.aud
```

In the above, we blanket-allow all actions and roles, but specifically rely on the `aud` key parsed from the JWT to determine access.

## [](#%5Fadding%5Fself%5Fservice%5Fcustom%5Froles)Adding self-service custom roles

Imagine this scenario: you’re an admin in a multi-tenant system, and you want a method by which you can copy an existing role, and then select which permissions/actions to enable or disable for each.

There are two ways of approaching this:

### [](#%5Fstatic%5Fpolicies%5Fdynamic%5Fcontext)Static Policies / Dynamic Context

This is the _idiomatic_ way of solving this use-case in Cerbos. In the vast majority of cases, it is possible to have the policies statically defined and to pass in dynamic context as attributes of a principal. This dynamic context can be any arbitrary data such as the principal’s location, age, or specific roles it has within the context of an organizational unit (a department, a tenant or a project, for example). This contextual data would be retrieved at request time from another service or a data store. Let’s look at an example.

Here is a resource policy for a resource of type `"workspace"`:

workspace.yaml

```yaml
apiVersion: "api.cerbos.dev/v1"
resourcePolicy:
  version: "default"
  resource: "workspace"
  rules:
    - actions:
        - workspace:view
        - pii:view
      effect: EFFECT_ALLOW
      roles:
        - USER
      condition:
        match:
          expr: P.attr.workspaces[R.id].role == "OWNER"
```

Notice how the condition relies on context passed in within the `P.attr.workspaces` map, with the key being the resource ID, and the value being a predefined value `"OWNER"`. We can grant access to a principal with the `USER` role, by constructing the following request payload:

* cURL
* .NET
* Go
* Java
* JS
* PHP
* Python
* Ruby
* Rust

```shell
cat <<EOF | curl --silent "http://localhost:3592/api/check/resources?pretty" -d @-
{
  "requestId": "quickstart",
  "principal": {
    "id": "123",
    "roles": [
      "USER"
    ],
    "attr": {
      "workspaces": {
        "workspaceA": {
          "role": "OWNER"
        },
        "workspaceB": {
          "role": "MEMBER"
        }
      }
    }
  },
  "resources": [
    {
      "actions": [
        "workspace:view",
        "pii:view"
      ],
      "resource": {
        "id": "workspaceA",
        "kind": "workspace"
      }
    },
    {
      "actions": [
        "workspace:view",
        "pii:view"
      ],
      "resource": {
        "id": "workspaceB",
        "kind": "workspace"
      }
    }
  ]
}
EOF
```

```csharp
using Cerbos.Sdk.Builders;
using Cerbos.Sdk;

internal class Program
{
    private static void Main(string[] args)
    {
        var client = new CerbosClientBuilder("http://localhost:3593").WithPlaintext().BuildBlockingClient();
        string[] actions = { "workspace:view", "pii:view" };

        CheckResourcesResult result = client
            .CheckResources(
                Principal.NewInstance("123", "USER")
                    .WithAttribute("workspaces", AttributeValue.MapValue(new Dictionary<string, AttributeValue>()
                    {
                        {
                            "workspaceA", AttributeValue.MapValue(new Dictionary<string, AttributeValue>()
                            {
                                {"role", AttributeValue.StringValue("OWNER")}
                            })
                        },
                        {
                            "workspaceB", AttributeValue.MapValue(new Dictionary<string, AttributeValue>()
                            {
                                {"role", AttributeValue.StringValue("MEMBER")}
                            })
                        }
                    })),

                ResourceAction.NewInstance("workspace", "workspaceA")
                    .WithActions(actions),

                ResourceAction.NewInstance("workspace", "workspaceB")
                    .WithActions(actions)
            );

        foreach (string n in new string[] { "workspaceA", "workspaceB" })
        {
            var r = result.Find(n);
            Console.Write(String.Format("\nResource: {0}\n", n));
            foreach (var i in r.GetAll())
            {
                String action = i.Key;
                Boolean isAllowed = i.Value;
                Console.Write(String.Format("\t{0} -> {1}\n", action, isAllowed ? "EFFECT_ALLOW" : "EFFECT_DENY"));
            }
        }
    }
}
```

```go
package main

import (
	"context"
	"log"

	"github.com/cerbos/cerbos-sdk-go/cerbos"
)

func main() {
	c, err := cerbos.New("localhost:3593", cerbos.WithPlaintext())
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}

	principal := cerbos.NewPrincipal("123", "USER")
	// We use map[string]any as strictly typed nested maps aren't supported
	principal.WithAttr("workspaces", map[string]map[string]any{
		"workspaceA": {
			"role": "OWNER",
		},
		"workspaceB": {
			"role": "MEMBER",
		},
	})

	kind := "workspace"
	actions := []string{"workspace:view", "pii:view"}

	batch := cerbos.NewResourceBatch()
	batch.Add(cerbos.NewResource(kind, "workspaceA"), actions...)
	batch.Add(cerbos.NewResource(kind, "workspaceB"), actions...)

	resp, err := c.CheckResources(context.Background(), principal, batch)
	if err != nil {
		log.Fatalf("Failed to check resources: %v", err)
	}
	log.Printf("%v", resp)
}
```

```java
package demo;

import static dev.cerbos.sdk.builders.AttributeValue.mapValue;
import static dev.cerbos.sdk.builders.AttributeValue.stringValue;

import java.util.Map;

import dev.cerbos.sdk.CerbosBlockingClient;
import dev.cerbos.sdk.CerbosClientBuilder;
import dev.cerbos.sdk.CheckResult;
import dev.cerbos.sdk.builders.Principal;
import dev.cerbos.sdk.builders.ResourceAction;


public class App {
    public static void main(String[] args) throws CerbosClientBuilder.InvalidClientConfigurationException {
        CerbosBlockingClient client=new CerbosClientBuilder("localhost:3593").withPlaintext().buildBlockingClient();

        for (String n : new String[]{"workspaceA", "workspaceB"}) {
            CheckResult cr = client.batch(
                Principal.newInstance("123", "USER")
                    .withAttribute("workspaces", mapValue(Map.of(
                        "workspaceA", mapValue(Map.of(
                                "role", stringValue("OWNER")
                        )),
                        "workspaceB", mapValue(Map.of(
                                "role", stringValue("MEMBER")
                        ))
                    )))
                )
                .addResources(
                    ResourceAction.newInstance("workspace","workspaceA")
                        .withActions("workspace:view", "pii:view"),
                    ResourceAction.newInstance("workspace","workspaceB")
                        .withActions("workspace:view", "pii:view")
                )
                .check().find(n).orElse(null);

            if (cr != null) {
                System.out.printf("\nResource: %s\n", n);
                cr.getAll().forEach((action, allowed) -> { System.out.printf("\t%s -> %s\n", action, allowed ? "EFFECT_ALLOW" : "EFFECT_DENY"); });
            }
        }
    }
}
```

```javascript
const { GRPC: Cerbos } = require("@cerbos/grpc");

const cerbos = new Cerbos("localhost:3593", { tls: false });

(async() => {
  const kind = "workspace";
  const actions = ["workspace:view", "pii:view"];

  const cerbosPayload = {
    principal: {
      id: "123",
      roles: ["USER"],
      attributes: {
        workspaces: {
          workspaceA: {
            role: "OWNER",
          },
          workspaceB: {
            role: "MEMBER",
          }
        },
      },
    },
    resources: [
      {
        resource: {
          kind: kind,
          id: "workspaceA",
        },
        actions: actions,
      },
      {
        resource: {
          kind: kind,
          id: "workspaceB",
        },
        actions: actions,
      },
    ],
  };

  const decision = await cerbos.checkResources(cerbosPayload);
  console.log(decision.results)
})();
```

```php
<?php

require __DIR__ . '/vendor/autoload.php';

use Cerbos\Sdk\Builder\CerbosClientBuilder;
use Cerbos\Sdk\Builder\Principal;
use Cerbos\Sdk\Builder\ResourceAction;
use Symfony\Component\HttpClient\HttplugClient;

$clientBuilder = new CerbosClientBuilder("http://localhost:3592", new HttplugClient(), null, null, null);
$client = $clientBuilder->build();

$principal = Principal::newInstance("123")
              ->withRole("USER")
              ->withAttribute("workspaces", [
                  "workspaceA" => [
                      "role" => "OWNER"
                  ],
                  "workspaceB" => [
                      "role" => "MEMBER"
                  ]
              ]);

$type = "workspace";

$resourceAction1 = ResourceAction::newInstance($type, "workspaceA")
                    ->withAction("workspace:view")
                    ->withAction("pii:view");

$resourceAction2 = ResourceAction::newInstance($type, "workspaceB")
                    ->withAction("workspace:view")
                    ->withAction("pii:view");

$checkResourcesResult = $client->checkResources($principal, array($resourceAction1, $resourceAction2), null, null);

echo json_encode($checkResourcesResult, JSON_PRETTY_PRINT);

?>
```

```python
import json

from cerbos.sdk.client import CerbosClient
from cerbos.sdk.model import Principal, Resource, ResourceAction, ResourceList
from fastapi import HTTPException, status

principal = Principal(
    "123",
    roles=["USER"],
    attr={
        "workspaces": {
            "workspaceA": {
                "role": "OWNER",
            },
            "workspaceB": {
                "role": "MEMBER",
            }
        }
    }
)

actions = ["workspace:view", "pii:view"]
resource_list = ResourceList(
    resources=[
        ResourceAction(
            Resource(
                "workspaceA",
                "workspace",
            ),
            actions=actions,
        ),
        ResourceAction(
            Resource(
                "workspaceB",
                "workspace",
            ),
            actions=actions,
        ),
    ],
)

with CerbosClient(host="http://localhost:3592") as c:
    try:
        resp = c.check_resources(principal=principal, resources=resource_list)
        resp.raise_if_failed()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized"
        )

print(json.dumps(resp.to_dict(), sort_keys=False, indent=4))
```

```ruby
# frozen_string_literal: true

require "cerbos"
require "json"

client = Cerbos::Client.new("localhost:3593", tls: false)

kind = "workspace"
actions = ["workspace:view", "pii:view"]

r1 = {
  kind: kind,
  id: "workspaceA"
}

r2 = {
  kind: kind,
  id: "workspaceB"
}

decision = client.check_resources(
  principal: {
    id: "123",
    roles: ["USER"],
    attributes: {
      workspaces: {
        workspaceA: {
          role: "OWNER"
        },
        workspaceB: {
          role: "MEMBER"
        }
      }
    }
  },
  resources: [
    {
      resource: r1,
      actions: actions
    },
    {
      resource: r2,
      actions: actions
    }
  ]
)

puts JSON.pretty_generate({
  results: [
    {
      resource: r1,
      actions: {
        "workspace:view": decision.allow?(resource: r1, action: "workspace:view"),
        "pii:view": decision.allow?(resource: r1, action: "pii:view")
      }
    },
    {
      resource: r2,
      actions: {
        "workspace:view": decision.allow?(resource: r2, action: "workspace:view"),
        "pii:view": decision.allow?(resource: r2, action: "pii:view")
      }
    }
  ]
})
```

```rust
use cerbos::sdk::attr::{attr, StructVal};
use cerbos::sdk::model::{Principal, Resource, ResourceAction, ResourceList};
use cerbos::sdk::{CerbosAsyncClient, CerbosClientOptions, CerbosEndpoint, Result};

#[tokio::main]
async fn main() -> Result<()> {
    let opt =
        CerbosClientOptions::new(CerbosEndpoint::HostPort("localhost", 3593)).with_plaintext();
    let mut client = CerbosAsyncClient::new(opt).await?;

    let principal = Principal::new("123", ["USER"]).with_attributes([attr(
        "workspaces",
        StructVal([
            ("workspaceA", StructVal([("role", "OWNER")])),
            ("workspaceB", StructVal([("role", "MEMBER")])),
        ]),
    )]);

    let actions: [&str; 2] = ["workspace:view", "pii:view"];

    let kind = "workspace";
    let resp = client
        .check_resources(
            principal,
            ResourceList::new_from([
                ResourceAction(Resource::new("workspaceA", kind), actions),
                ResourceAction(Resource::new("workspaceB", kind), actions),
            ]),
            None,
        )
        .await?;

    println!("{:?}", resp.response);

    Ok(())
}
```

You can find a full (and extended) example of the above in our [SaaS Workspace Policy playground example](https://play.cerbos.dev/p/IJxlK6131f642ND65F1EhPmiT18Ap1A5).

### [](#%5Fdynamic%5Fpolicies)Dynamic Policies

There might be circumstances where you want to create or update resources and actions on the fly; an example of this might be a multi-tenant platform that provides tenants the ability to manage their own policies.

If this is the case, then you can use the [Admin API](../api/admin%5Fapi.html) configured alongside a mutable [database storage engine](../configuration/storage.html#sqlite3) to provide this functionality. This would be handled within your application layer, with the desired policy contents provided to the PDP via the API.

For a full example implementation, check out [this demo](https://github.com/cerbos/demo-admin-api).

## [](#%5Fpolicy%5Frepository%5Flayout)Policy repository layout

Cerbos expects the policy repository to have a particular directory layout.

* The directory must only contain Cerbos policy files, policy test files and schemas. Any other YAML or JSON files will cause Cerbos to consider the policy repository as invalid.
* If you use [schemas](schemas.html), the `_schemas` directory must be a top-level directory at the root of the policy repo.
* All policy tests must have a file name ending in `_test` and a `.yaml`, `.yml` or `.json` extension.
* Directories named `testdata` can be used to store test data for policy tests. Cerbos will not attempt to locate any policy files inside those directories.
* Hidden files and directories (names starting with `.`) are ignored.

A typical policy repository might resemble the following:

.
├── _schemas
│   ├── principal.json
│   └── resources
│       ├── leave_request.json
│       ├── purchase_order.json
│       └── salary_record.json
├── derived_roles
│   ├── backoffice_roles.yaml
│   └── common_roles.yaml
├── principal_policies
│   └── auditor_audrey.yaml
└── resource_policies
    ├── finance
    │   ├── purchase_order.yaml
    │   └── purchase_order_test.yaml
    └── hr
        ├── leave_request.yaml
        ├── leave_request_test.yaml
        ├── salary_record.yaml
        ├── salary_record_test.yaml
        └── testdata
            ├── auxdata.yaml
            ├── principals.yaml
            └── resources.yaml

Validating and testing policies
====================
## [](#%5Fvalidating%5Fpolicies)Validating policies

You can use the Cerbos compiler to make sure that your policies are valid before pushing them to a production Cerbos instance. We recommend setting up a git hook or a CI step to run the Cerbos compiler before you push any policy changes to production.

```sh
docker run -i -t -v /path/to/policy/dir:/policies ghcr.io/cerbos/cerbos:0.51.0 compile /policies
```

## [](#testing)Testing policies

You can write optional tests for policies and run them as part of the compilation stage to make sure that the policies do exactly what you expect.

Tests are defined using the familiar YAML format as well. A test file must have `_test` suffix in the name and one of the following file extensions: `yaml`, `yml`, or `json`. For example, `album_test.yml`, `album_test.yaml` or `album_test.json`.

Test suite definition

```yaml
---
name: AlbumObjectTestSuite (1)
description: Tests for verifying the album:object resource policy (2)
options:
  now: "2022-08-02T15:00:00Z" (3)
  defaultPolicyVersion: staging (4)
  defaultScope: "" (5)
  lenientScopeSearch: true (6)
  globals: (7)
    my_global_var: foo

principals: (8)
  alicia:
    id: aliciaID
    roles:
      - user

  bradley:
    id: bradleyID
    roles:
      - user

principalGroups: (9)
  everyone:
    principals:
      - alicia
      - bradley

resources: (10)
  alicia_album:
    id: XX125
    kind: album:object
    policyVersion: default
    attr:
      owner: aliciaID
      public: false
      flagged: false

  bradley_album:
    id: XX250
    kind: album:object
    policyVersion: staging
    attr:
      owner: bradleyID
      public: false
      flagged: false

resourceGroups: (11)
  all_albums:
    resources:
      - alicia_album
      - bradley_album

auxData: (12)
  validJWT:
    jwt:
      iss: my.domain
      aud: ["x", "y"]
      myField: value

tests: (13)
  - name: Accessing an album (14)
    options: (15)
      now: "2022-08-03T15:00:00Z" (16)
      defaultPolicyVersion: production (17)
      defaultScope: "" (18)
      lenientScopeSearch: false (19)
      globals: (20)
        my_global_var: bar

    input: (21)
      principals: (22)
        - alicia
        - bradley
      resources: (23)
        - alicia_album
        - bradley_album
      actions: (24)
        - view
        - delete
      auxData: validJWT (25)

    expected: (26)
      - principal: alicia (27)
        resource: alicia_album (28)
        actions: (29)
          view: EFFECT_ALLOW
          delete: EFFECT_ALLOW
        outputs: (30)
          - action: view (31)
            expected: (32)
              - src: resource.album.vdefault#view-rule
                val:
                  key1: value1
                  key2: ["value2", "value3"]
              - src: resource.album.vdefault#token-lifetime
                val: 1h

      - principal: bradley
        resource: bradley_album
        actions:
          view: EFFECT_ALLOW
          delete: EFFECT_ALLOW

  - name: Using groups
    input:
      principalGroups: (33)
        - everyone
      resourceGroups: (34)
        - all_albums
      actions:
        - download

    expected:
      - principalGroups: (35)
          - everyone
        resourceGroups: (36)
          - all_albums
        actions:
          download: EFFECT_DENY
```

| **1**  | Name of the test suite.                                                                                                                                                                            |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2**  | Description of the test suite.                                                                                                                                                                     |
| **3**  | Optional RFC3339 timestamp to be used as the return value of the now function. Applies to all tests in the suite unless overridden locally.                                                        |
| **4**  | Optionally set [default policy version](../configuration/engine.html#default%5Fpolicy%5Fversion) for this test suite.                                                                              |
| **5**  | Optionally set [default scope](../configuration/engine.html#default%5Fscope) for this test suite.                                                                                                  |
| **6**  | Optionally set [lenient scope search](../configuration/engine.html#lenient%5Fscopes) for this test suite.                                                                                          |
| **7**  | Optionally set [globals](../configuration/engine.html#globals) for this test suite.                                                                                                                |
| **8**  | Map of principal fixtures. The key is a string that can be used to refer to the associated principal.                                                                                              |
| **9**  | Map of principal groups. The key is a string that can be used to refer to the associated group of principal fixtures.                                                                              |
| **10** | Map of resource fixtures. The key is a string that can be used to refer to the associated resource.                                                                                                |
| **11** | Map of resource groups. The key is a string that can be used to refer to the associated group of resource fixtures.                                                                                |
| **12** | Map of (optional) auxiliary data fixtures required to evaluate some requests. The key is a string that can be used to refer to the associated auxData.                                             |
| **13** | List of tests in this suite.                                                                                                                                                                       |
| **14** | Name of the test.                                                                                                                                                                                  |
| **15** | Optionally set options that apply to just this test. Test-specific options are not merged with suite-wide options, so any unspecified values revert to the default.                                |
| **16** | Optional RFC3339 timestamp to be used as the return value of the now function.                                                                                                                     |
| **17** | Optionally set [default policy version](../configuration/engine.html#default%5Fpolicy%5Fversion) for this test.                                                                                    |
| **18** | Optionally set [default scope](../configuration/engine.html#default%5Fscope) for this test suite.                                                                                                  |
| **19** | Optionally set [lenient scope search](../configuration/engine.html#lenient%5Fscopes) for this test.                                                                                                |
| **20** | Optionally set [globals](../configuration/engine.html#globals) for this test.                                                                                                                      |
| **21** | Input to the policy engine.                                                                                                                                                                        |
| **22** | List of keys of principal fixtures to test.                                                                                                                                                        |
| **23** | List of keys of resource fixtures to test.                                                                                                                                                         |
| **24** | List of actions to test.                                                                                                                                                                           |
| **25** | Key of auxiliary data fixture to test (optional).                                                                                                                                                  |
| **26** | List of outcomes expected for each principal and resource. If a principal+resource pair specified in input is not listed in expected, then EFFECT\_DENY is expected for all actions for that pair. |
| **27** | Key of the principal fixture under test. Use principals instead of principal if you want to specify identical expectations for multiple principals.                                                |
| **28** | Key of the resource fixture under test. Use resources instead of resource if you want to specify identical expectations for multiple resources.                                                    |
| **29** | Expected outcomes for each action for each principal+resource pair. If an action specified in input is not listed, then EFFECT\_DENY is expected for that action.                                  |
| **30** | Optional list of [output values](outputs.html) to match.                                                                                                                                           |
| **31** | Name of the action that would produce the output.                                                                                                                                                  |
| **32** | List of expected output values.                                                                                                                                                                    |
| **33** | List of keys of principal groups to test. You can provide this instead of, or as well as, principals.                                                                                              |
| **34** | List of keys of resource groups to test. You can provide this instead of, or as well as, resources.                                                                                                |
| **35** | Key of the principal group under test. You can provide this instead of, or as well as, principal or principals.                                                                                    |
| **36** | Key of the resource group under test. You can provide this instead of, or as well as, resource or resources.                                                                                       |

### [](#fixtures)Sharing test fixtures

It is possible to share principals, resources and auxData blocks between test suites stored in the same directory. Create a `testdata` directory in the directory containing your test suite files, then define shared resources, principals and auxData in `testdata/resources.yml`, `testdata/principals.yml`, `testdata/auxdata.yml` respectively (`yaml` and `json` extensions are also supported).

tests
├── album_object_test.yaml
├── gallery_object_test.yaml
├── slideshow_object_test.yaml
└── testdata
   ├── auxdata.yaml
   ├── principals.yaml
   └── resources.yaml

An example of `testdata/principals.yml`

```yaml
---
principals: # required
  john:
    id: johnID
    roles:
      - user
      - moderator

principalGroups: # optional
  moderators:
    principals:
      - john
```

An example of `testdata/resources.yml`

```yaml
---
resources: # required
  alicia_album:
    id: XX125
    kind: "album:object"
    attr:
      owner: aliciaID
      public: false
      flagged: false

resourceGroups: # optional
  all_albums:
    resources:
      - alicia_album
```

An example of `testdata/auxdata.yml`

```yaml
---
auxData: # required
  validJWT:
    jwt:
      iss: my.domain
      aud: ["x", "y"]
      myField: value
```

| |  [YAML anchors and overrides](https://www.educative.io/blog/advanced-yaml-syntax-cheatsheet#anchors) are a great way to reduce repetition and reuse definitions in test cases. For example, the following definitions are equivalent: Without anchors and overrides With anchors and overrides resources:   alicias\_album1:     id: "XX125"     kind: "album:object"     attr:       owner: "alicia"       public: false       flagged: false   alicias\_album2:     id: "XX525"     kind: "album:object"     attr:       owner: "alicia"       public: false       flagged: false   alicias\_album3:     id: "XX925"     kind: "album:object"     attr:       owner: "alicia"       public: false       flagged: false resources:   alicias\_album1:     id: "XX125"     kind: "album:object"     attr: &alicia\_album\_attr       owner: "alicia"       public: false       flagged: false   alicias\_album2:     id: "XX525"     kind: "album:object"     attr:       <<: \*alicia\_album\_attr   alicias\_album3:     id: "XX925"     kind: "album:object"     attr:       <<: \*alicia\_album\_attr |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#%5Frunning%5Ftests)Running tests

The `compile` command automatically discovers test files in the policy repository.

```sh
docker run -i -t \
    -v /path/to/policy/dir:/policies \
    ghcr.io/cerbos/cerbos:0.51.0 compile /policies
```

The output format can be controlled using the `--output` flag, which accepts the values `tree` (default), `list` and `json`. The `--color` flag controls the coloring of the output. To produce machine readable output from the tests, pass `--output=json --color=never` to the command.

By default, all discovered tests are run. Use the `--skip-tests` flag to skip all tests or use `--test-filter` to run only tests matching specific criteria.

The `--test-filter` flag accepts a filter expression with the following dimensions:

* `suite` \- filter by test suite name,
* `test` \- filter by test name,
* `principal` \- filter by principal key,
* `resource` \- filter by resource key,
* `action` \- filter by action name.

Each dimension accepts one or more glob patterns. Multiple dimensions are separated by semicolons, and multiple values within a dimension are separated by commas.

Example: Running tests for a specific suite and principal

```sh
docker run -i -t \
    -v /path/to/policy/dir:/policies \
    ghcr.io/cerbos/cerbos:0.51.0 compile --test-filter='suite=AlbumObjectTestSuite;principal=alicia' /policies
```

Example: Running tests matching glob patterns

```sh
docker run -i -t \
    -v /path/to/policy/dir:/policies \
    ghcr.io/cerbos/cerbos:0.51.0 compile --test-filter='test=*Delete*;action=view,edit' /policies
```

Multiple `--test-filter` flags can be combined. All filter dimensions are merged together.

```sh
docker run -i -t \
    -v /path/to/policy/dir:/policies \
    ghcr.io/cerbos/cerbos:0.51.0 compile --test-filter='principal=alice,bob' --test-filter='action=view' /policies
```

You can mark entire suites or individual tests in a suite with `skip: true` to skip them during test runs.

Example: Skipping a test

```yaml
---
name: AlbumObjectTestSuite
description: Tests for verifying the album:object resource policy
tests:
  - name: View private album
    skip: true
    skipReason: "Policy under review"
    input:
      principals: ["alicia"]
      resources: ["alicia_private_album"]
      actions: ["view"]
    expected:
      - principal: alicia
        resource: alicia_private_album
        actions:
          view: EFFECT_ALLOW
```

## [](#ci-environments)Validating and testing policies in CI environments

Because Cerbos artefacts are distributed as self-contained containers and binaries, you should be able to easily integrate Cerbos into any CI environment. Simply configure your workflow to execute the commands described in the sections above using either the Cerbos container (you may need to configure mount points to suit your repo structure) or the binary.

### [](#%5Fgithub%5Factions)GitHub Actions

* [cerbos-setup-action](https://github.com/cerbos/cerbos-setup-action): Install `cerbos` and `cerbosctl` binaries into your workflow tools cache
* [cerbos-compile-action](https://github.com/cerbos/cerbos-compile-action): Compile and (optionally) test Cerbos policies

Example workflow

```yaml
---
name: PR Check
on:
  pull_request:
    branches:
      - main
jobs:
  cerbosCheck:
    name: Check Cerbos policies
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Setup Cerbos
        uses: cerbos/cerbos-setup-action@v1
        with:
          version: latest

      - name: Compile and test policies
        uses: cerbos/cerbos-compile-action@v1
        with:
          policyDir: policies
```

See <https://github.com/cerbos/photo-share-tutorial> for an example of Cerbos GitHub Actions being used in a workflow.

### [](#%5Fgitlab%5Fci)GitLab CI

Example pipeline

```yaml
---
stages:
  - prepare
  - compile

download-cerbos:
  stage: prepare
  script:
    - curl https://github.com/cerbos/cerbos/releases/download/v0.51.0/cerbos_0.51.0_Linux_x86_64.tar.gz -L --output /tmp/cerbos.tar.gz
    - tar -xf /tmp/cerbos.tar.gz -C ./
    - chmod +x ./cerbos
  artifacts:
    paths:
      - cerbos

compile-job:
  stage: compile
  dependencies: ["download-cerbos"]
  script:
    - ./cerbos compile ./policies
```

### [](#%5Fdagger)Dagger

The [Dagger](https://dagger.io) Cerbos module can be installed by running `dagger install github.com/cerbos/dagger-cerbos`. This module provides a `compile` function for compiling and testing Cerbos policy repositories and a `server` service for starting a Cerbos server.

```yaml
# Compile and run tests on a policy repository
dagger -m github.com/cerbos/dagger-cerbos call compile --policy-dir=./cerbos

# Start a Cerbos server with the default disk driver
dagger -m github.com/cerbos/dagger-cerbos call server --policy-dir=./cerbos up

# Start a Cerbos server instance configured to use an in-memory SQLite policy repository
dagger -m github.com/cerbos/dagger-cerbos call server --config=storage.driver=sqlite3,storage.sqlite3.dsn=:memory:,server.adminAPI.enabled=true up

# View usage information
dagger -m github.com/cerbos/dagger-cerbos call compile --help
dagger -m github.com/cerbos/dagger-cerbos call server --help
```

Conditions
====================
A powerful feature of Cerbos policies is the ability to define conditions that are evaluated against the data provided in the request. Conditions are written using the [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md).

| |  Cerbos ships with an interactive REPL that can be used to experiment with writing CEL conditions. It can be started by running cerbos repl. See [the REPL documentation](../cli/cerbos.html#repl) for more information. |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Every condition expression must evaluate to a boolean true/false value. A condition block in a policy can contain either a single condition expression, or multiple expressions combined using the `all`, `any`, or `none` operators. These logical operators may be nested.

Condition block

```yaml
condition:
  match:
    all:
      of:
        - expr: request.resource.attr.status == "PENDING_APPROVAL"
        - expr: >
            "GB" in request.resource.attr.geographies
```

## [](#top%5Flevel%5Fidentifiers)Top-level identifiers

Within a condition expression, you have access to several top-level identifiers:

`request`

Data provided in the check or plan request (principal, resource, and auxiliary data).

`runtime`

Additional data computed while evaluating the policy.

`variables`

Variables declared in the [variables section of the policy](variables.html#variables).

`constants`

Variables declared in the [constants section of the policy](variables.html#constants).

`globals`

Global variables declared in the [policy engine configuration](../configuration/engine.html#globals).

There are also single-letter aliases available to allow you to write terser expressions:

`P`

`request.principal`

`R`

`request.resource`

`V`

`variables`

`C`

`constants`

`G`

`globals`

The `request` object

```yaml
request:
  principal: (1)
    id: alice (2)
    roles: (3)
      - employee
    attr: (4)
      geography: GB

  resource: (5)
    kind: leave_request (6)
    id: XX125 (7)
    attr: (8)
      owner: alice

  auxData: (9)
    jwt: (10)
      iss: acme.corp
```

| **1**  | The principal whose permissions are being checked.                                  |
| ------ | ----------------------------------------------------------------------------------- |
| **2**  | ID of the principal.                                                                |
| **3**  | Static roles that are assigned to the principal by your identity management system. |
| **4**  | Free-form context data about the principal.                                         |
| **5**  | The resource on which the principal is performing actions.                          |
| **6**  | Resource kind.                                                                      |
| **7**  | ID of the resource instance.                                                        |
| **8**  | Free-form context data about the resource instance.                                 |
| **9**  | [Auxiliary data sources](../configuration/auxdata.html).                            |
| **10** | JWT claims.                                                                         |

The `runtime` object

```yaml
runtime:
  effectiveDerivedRoles: (1)
    - owner
    - gb_employee
```

| **1** | [Derived roles](derived%5Froles.html) that were assigned to to the principal by Cerbos while evaluating the policy. This is only populated in expressions in resource policies, and only includes derived roles that are referenced in at least one policy rule. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#%5Fexpressions%5Fand%5Fblocks)Expressions and blocks

Single boolean expression

```yaml
condition:
  match:
    expr: P.id.matches("^dev_.*")
```

`all` operator: all expressions must evaluate to true (logical AND)

```yaml
condition:
  match:
    all:
      of:
        - expr: R.attr.status == "PENDING_APPROVAL"
        - expr: >
            "GB" in R.attr.geographies
        - expr: P.attr.geography == "GB"
```

`any` operator: only one of the expressions has to evaluate to true (logical OR)

```yaml
condition:
  match:
    any:
      of:
        - expr: R.attr.status == "PENDING_APPROVAL"
        - expr: >
            "GB" in R.attr.geographies
        - expr: P.attr.geography == "GB"
```

`none` operator: none of the expressions should evaluate to true (logical negation)

```yaml
condition:
  match:
    none:
      of:
        - expr: R.attr.status == "PENDING_APPROVAL"
        - expr: >
            "GB" in R.attr.geographies
        - expr: P.attr.geography == "GB"
```

Nesting operators

```yaml
condition:
  match:
    all:
      of:
        - expr: R.attr.status == "DRAFT"
        - any:
            of:
              - expr: R.attr.dev == true
              - expr: R.attr.id.matches("^[98][0-9]+")
        - none:
            of:
              - expr: R.attr.qa == true
              - expr: R.attr.canary == true
```

The above nested block is equivalent to the following:

```yaml
condition:
  match:
    expr: >
      (R.attr.status == "DRAFT" &&
        (R.attr.dev == true || R.attr.id.matches("^[98][0-9]+")) &&
        !(R.attr.qa == true || R.attr.canary == true))
```

Quotes in expressions

Single and double quotes have special meanings in YAML. To avoid parsing errors when your expression contains quotes, use the YAML block scalar syntax or wrap the expression in parentheses.

```yaml
expr: >
  "GB" in R.attr.geographies
```

```yaml
expr: ("GB" in R.attr.geographies)
```

## [](#%5Fpolicy%5Fvariables)Policy variables

To avoid duplication in condition expressions, you can define [variables and constants in policies](variables.html).

## [](#auxdata)Auxiliary data

If you have [auxiliary data sources configured](../configuration/auxdata.html), they can be accessed using `request.auxData`.

Accessing JWT claims

```yaml
"cerbie" in request.auxData.jwt.aud && request.auxData.jwt.iss == "cerbos"
```

## [](#%5Foperators)Operators

| |  CEL has many builtin functions and operators. The fully up-to-date list can be found at <https://github.com/google/cel-spec/blob/master/doc/langdef.md#list-of-standard-definitions>. |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| Operator | Description                      |
| -------- | -------------------------------- |
| !        | Logical negation (NOT)           |
| \-       | Subtraction/numeric negation     |
| !=       | Unequals                         |
| %        | Modulo                           |
| &&       | Logical AND                      |
| \||      | Logical OR                       |
| \*       | Multiplication                   |
| +        | Addition/concatenation           |
| /        | Division                         |
| <=       | Less than or equal to            |
| <        | Less than                        |
| \==      | Equals                           |
| \>=      | Greater than or equal to         |
| \>       | Greater than                     |
| in       | Membership in lists or maps      |
| ? :      | Ternary condition (if-then-else) |

## [](#%5Fdurations)Durations

| |  Duration values must be specified in one of the following units. Larger units like days, weeks or years are not supported because of ambiguity around their meaning due to factors such as daylight saving time transitions. Suffix Unit ns Nanoseconds us Microseconds ms Milliseconds s Seconds m Minutes h Hours |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Test data

```json
...
"resource": {
  "kind": "leave_request",
  "attr": {
    "cooldownPeriod": "3750s",
    "lastAccessed": "2021-04-20T10:00:20.021-05:00"
  }
}
...
```

| Function        | Description                                                                                                                   | Example                                                      |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| duration        | Convert a string to a duration. The string must contain a valid duration suffixed by one of ns, us, ms, s, m or h. E.g. 3750s | duration(R.attr.cooldownPeriod).getSeconds() == 3750         |
| getHours        | Get hours from a duration                                                                                                     | duration(R.attr.cooldownPeriod).getHours() == 1              |
| getMilliseconds | Get milliseconds from a duration                                                                                              | duration(R.attr.cooldownPeriod).getMilliseconds() == 3750000 |
| getMinutes      | Get minutes from a duration                                                                                                   | duration(R.attr.cooldownPeriod).getMinutes() == 62           |
| getSeconds      | Get seconds from a duration                                                                                                   | duration(R.attr.cooldownPeriod).getSeconds() == 3750         |
| timeSince       | Time elapsed since the given timestamp to current time on the server. This is a Cerbos extension to CEL                       | timestamp(R.attr.lastAccessed).timeSince() > duration("1h")  |

## [](#hierarchies)Hierarchies

| |  The hierarchy functions are Cerbos-specific extensions to CEL. |
| ----------------------------------------------------------------- |

Test data

```json
...
"principal": {
  "id": "john",
  "roles": ["employee"],
  "attr": {
    "scope": "foo.bar.baz.qux",
  }
},
"resource": {
  "kind": "leave_request",
  "attr": {
    "scope": "foo.bar",
  }
}
...
```

| Function          | Description                                                                          | Example                                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| hierarchy         | Convert a dotted string or a string list to a hierarchy                              | hierarchy("a.b.c") == hierarchy(\["a","b","c"\])                                                                                    |
| hierarchy         | Convert a delimited string representation to a hierarchy                             | hierarchy("a:b:c", ":").size() == 3                                                                                                 |
| ancestorOf        | Returns true if the first hierarchy shares a common prefix with the second hierarchy | hierarchy("a.b").ancestorOf(hierarchy("a.b.c.d")) == true                                                                           |
| commonAncestors   | Returns the common ancestor hierarchy                                                | hierarchy(R.attr.scope).commonAncestors(hierarchy(P.attr.scope)) == hierarchy("foo.bar")                                            |
| descendentOf      | Mirror function of ancestorOf                                                        | hierarchy("a.b.c.d").descendentOf(hierarchy("a.b")) == true                                                                         |
| immediateChildOf  | Returns true if the first hierarchy is a first-level child of the second hierarchy   | hierarchy("a.b.c").immediateChildOf(hierarchy("a.b")) == true && hierarchy("a.b.c.d").immediateChildOf(hierarchy("a.b")) == false   |
| immediateParentOf | Mirror function of immediateChildOf                                                  | hierarchy("a.b").immediateParentOf(hierarchy("a.b.c")) == true && hierarchy("a.b").immediateParentOf(hierarchy("a.b.c.d")) == false |
| overlaps          | Returns true if one of the hierarchies is a prefix of the other                      | hierarchy("a.b.c").overlaps(hierarchy("a.b.c.d.e")) == true && hierarchy("a.b.x").overlaps(hierarchy("a.b.c.d.e")) == false         |
| siblingOf         | Returns true if both hierarchies share the same parent                               | hierarchy("a.b.c").siblingOf(hierarchy("a.b.d")) == true                                                                            |
| size              | Returns the number of levels in the hierarchy                                        | hierarchy("a.b.c").size() == 3                                                                                                      |
| \[\]              | Access a level in the hierarchy                                                      | hierarchy("a.b.c.d")\[1\] == "b"                                                                                                    |

## [](#%5Fip%5Faddresses)IP addresses

| |  The IP address functions are Cerbos-specific extensions to CEL. |
| ------------------------------------------------------------------ |

Test data

```json
...
"principal": {
  "id": "elmer_fudd",
  "attr": {
    "ipv4Address": "192.168.0.10",
    "ipv6Address": "2001:0db8:0000:0000:0000:0000:1000:0000"
  }
}
...
```

| Function      | Description                                                      | Example                                                                                                 |
| ------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| inIPAddrRange | Check whether the IP address is in the range defined by the CIDR | P.attr.ipv4Address.inIPAddrRange("192.168.0.0/24") && P.attr.ipv6Address.inIPAddrRange("2001:db8::/48") |

## [](#%5Flists%5Fand%5Fmaps)Lists and maps

Test data

```json
...
"principal": {
  "id": "elmer_fudd",
  "attr": {
    "id": "125",
    "teams": ["design", "communications", "product", "commercial"],
    "limits": {
        "design": 10,
        "product": 25
    },
    "clients": {
      "acme": {"active": true},
      "bb inc": {"active": true}
    }
  }
}
...
```

| Operator/Function | Description                                                                                                                                                      | Example                                                                                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| +                 | Concatenates lists                                                                                                                                               | P.attr.teams + \["design", "engineering"\]                                                                                                                      |
| \[\]              | Index into a list or a map                                                                                                                                       | P.attr.teams\[0\] == "design" && P.attr.clients\["acme"\]\["active"\] == true                                                                                   |
| all               | Check whether all elements in a list match the predicate.                                                                                                        | P.attr.teams.all(t, size(t) > 3) && \[1, 2, 3\].all(i, j, i < j)                                                                                                |
| distinct          | Returns the distinct elements of a list                                                                                                                          | \[1, 2, 2, 3, 3, 3\].distinct() == \[1, 2, 3\]                                                                                                                  |
| except            | Produces the set difference of two lists                                                                                                                         | P.attr.teams.except(\["design", "engineering"\]) == \["communications", "product", "commercial"\]                                                               |
| exists            | Check whether at least one element matching the predicate exists in a list or map.                                                                               | P.attr.teams.exists(t, t.startsWith("comm")) && P.attr.limits.exists(k, v, k == "design" && v > 0)                                                              |
| exists\_one       | Check that only one element matching the predicate exists.                                                                                                       | P.attr.teams.exists\_one(t, t.startsWith("comm")) == false && P.attr.limits.exists\_one(k, v, k == "design" && v > 0) == false                                  |
| filter            | Filter a list using the predicate.                                                                                                                               | size(P.attr.teams.filter(t, t.matches("^comm"))) == 2                                                                                                           |
| flatten           | Flattens a list. If an optional depth is provided, the list is flattened to the specified level                                                                  | \[1,2,\[\],\[\],\[3,4\]\].flatten() == \[1, 2, 3, 4\] && \[1,\[2,\[3,\[4\]\]\]\].flatten(2) == \[1, 2, 3, \[4\]\]                                               |
| hasIntersection   | Checks whether the lists have at least one common element                                                                                                        | hasIntersection(\["design", "engineering"\], P.attr.teams)                                                                                                      |
| in                | Check whether the given element is contained in the list or map                                                                                                  | ("design" in P.attr.teams) && ("acme" in P.attr.clients)                                                                                                        |
| intersect         | Produces the set intersection of two lists                                                                                                                       | intersect(\["design", "engineering"\], P.attr.teams) == \["design"\]                                                                                            |
| isSubset          | Checks whether the list is a subset of another list                                                                                                              | \["design", "engineering"\].isSubset(P.attr.teams) == false                                                                                                     |
| lists.range       | Returns a list of integers from 0 to n-1                                                                                                                         | lists.range(5) == \[0, 1, 2, 3, 4\]                                                                                                                             |
| map               | Transform each element in a list                                                                                                                                 | "DESIGN" in P.attr.teams.map(t, t.upperAscii())                                                                                                                 |
| reverse           | Returns the elements of a list in reverse order                                                                                                                  | \[5, 3, 1, 2\].reverse() == \[2, 1, 3, 5\]                                                                                                                      |
| size              | Number of elements in a list or map                                                                                                                              | size(P.attr.teams) == 4 && size(P.attr.clients) == 2                                                                                                            |
| slice             | Returns a new sub-list using the indexes provided                                                                                                                | \[1,2,3,4\].slice(1, 3) == \[2, 3\]                                                                                                                             |
| sort              | Sorts a list with comparable elements                                                                                                                            | \[3, 2, 1\].sort() == \[1, 2, 3\]                                                                                                                               |
| sortBy            | Sorts a list by a key value, i.e., the order is determined by the result of an expression applied to each element of the list                                    | \[{ "name": "foo", "score": 0 },{ "name": "bar", "score": -10 },{ "name": "baz", "score": 1000 }\].sortBy(e, e.score).map(e, e.name) == \["bar", "foo", "baz"\] |
| transformList     | Converts a map or a list into a list value. The output expression determines the contents of the output list. Elements in the list may optionally be filtered    | \[1, 2, 3\].transformList(i, v, i > 0, 2 \* v) == \[4, 6\] &&\[1, 2, 3\].transformList(i, v, 2 \* v) == \[2, 4, 6\]                                             |
| transformMap      | Converts a map or a list into a map value. The key remains unchanged and only the value is changed.                                                              | \[1, 2, 3\].transformMap(i, v, i > 0, 2 \* v) == {1: 4, 2: 6}                                                                                                   |
| transformMapEntry | Converts a map or a list into a map value; however, this transform expects the entry expression be a map literal. Elements in the map may optionally be filtered | {'greeting': 'hello'}.transformMapEntry(k, v, {v: k}) == {'hello': 'greeting'}                                                                                  |

## [](#%5Fmath)Math

| Function           | Description                                                                                                                                                                                        | Example                                                                                                                              |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| math.abs           | Returns the absolute value of the numeric type provided as input                                                                                                                                   | math.abs(1.2) == 1.2 && math.abs(-2) == 2                                                                                            |
| math.bitAnd        | Performs a bitwise-AND operation over two int or uint values                                                                                                                                       | math.bitAnd(3u, 2u) == 2u && math.bitAnd(3, 5) == 1 && math.bitAnd(-3, -5) == -7                                                     |
| math.bitNot        | Function which accepts a single int or uint and performs a bitwise-NOT ones-complement of the given binary value                                                                                   | math.bitNot(1) == -1 && math.bitNot(-1) == 0 && math.bitNot(0u) == 18446744073709551615u                                             |
| math.bitOr         | Performs a bitwise-OR operation over two int or uint values                                                                                                                                        | math.bitOr(1u, 2u) == 3u && math.bitOr(-2, -4) == -2                                                                                 |
| math.bitShiftLeft  | Perform a left shift of bits on the first parameter, by the amount of bits specified in the second parameter. The first parameter is either a uint or an int. The second parameter must be an int  | math.bitShiftLeft(1, 2) == 4 && math.bitShiftLeft(-1, 2) == -4 && math.bitShiftLeft(1u, 2) == 4u && math.bitShiftLeft(1u, 200) == 0u |
| math.bitShiftRight | Perform a right shift of bits on the first parameter, by the amount of bits specified in the second parameter. The first parameter is either a uint or an int. The second parameter must be an int | math.bitShiftRight(1024, 2) == 256 && math.bitShiftRight(1024u, 2) == 256u && math.bitShiftLeft(1024u, 64) == 0u                     |
| math.bitXor        | Performs a bitwise-XOR operation over two int or uint values                                                                                                                                       | math.bitXor(3u, 5u) == 6u && math.bitXor(1, 3) == 2                                                                                  |
| math.ceil          | Compute the ceiling of a double value                                                                                                                                                              | math.ceil(1.2) == 2.0 && math.ceil(-1.2) == -1.0                                                                                     |
| math.floor         | Compute the floor of a double value                                                                                                                                                                | math.floor(1.2) == 1.0 && math.floor(-1.2) == -2.0                                                                                   |
| math.greatest      | Get the greatest valued number present in the arguments                                                                                                                                            | math.greatest(\[1, 3, 5\]) == 5 && math.greatest(1, 3, 5) == 5                                                                       |
| math.isFinite      | Returns true if the value is a finite number                                                                                                                                                       | !math.isFinite(0.0/0.0) && math.isFinite(1.2)                                                                                        |
| math.isInf         | Returns true if the input double value is -Inf or +Inf                                                                                                                                             | math.isInf(1.0/0.0) && !math.isInf(1.2)                                                                                              |
| math.isNaN         | Returns true if the input double value is NaN, false otherwise                                                                                                                                     | math.isNaN(0.0/0.0) && !math.isNaN(1.2)                                                                                              |
| math.least         | Get the least valued number present in the arguments                                                                                                                                               | math.least(\[1, 3, 5\]) == 1 && math.least(1, 3, 5) == 1                                                                             |
| math.round         | Rounds the double value to the nearest whole number with ties rounding away from zero, e.g. 1.5 → 2.0, -1.5 → -2.0                                                                                 | math.round(1.2) == 1.0 && math.round(1.5) == 2.0 && math.round(-1.5) == -2.0                                                         |
| math.sign          | Returns the sign of the numeric type, either -1, 0, 1                                                                                                                                              | math.sign(1.2) == 1.0 && math.sign(-2) == -1 && math.sign(0) == 0                                                                    |
| math.trunc         | Truncates the fractional portion of the double value                                                                                                                                               | math.trunc(1.2) == 1.0 && math.trunc(-1.2) == -1.0                                                                                   |

## [](#spiffe)SPIFFE

| |  The SPIFFE functions are Cerbos-specific extensions to CEL. |
| -------------------------------------------------------------- |

Test data

```json
...
"principal": {
  "id": "spiffe://cerbos.dev/ns/privileged/sa/curl",
  "roles": ["api"],
}
...
```

| Function               | Description                                        | Example                                                                                                                                         |
| ---------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| spiffeID.isMemberOf    | Check whether the ID belongs to given trust domain | spiffeID(P.id).isMemberOf(spiffeTrustDomain("spiffe://cerbos.dev"))                                                                             |
| spiffeID.path          | Get the path element of ID                         | spiffeID(P.id).path() == "/ns/privileged/sa/curl"                                                                                               |
| spiffeID.trustDomain   | Get the trust domain of ID                         | spiffeID(P.id).trustDomain() == spiffeTrustDomain("spiffe://cerbos.dev")                                                                        |
| spiffeMatchAny         | Match any SPIFFE ID                                | spiffeMatchAny().matchesID(spiffeID(P.id)) == true                                                                                              |
| spiffeMatchExact       | Match a single SPIFFE ID                           | spiffeMatchExact(spiffeID("spiffe://cerbos.dev/ns/privileged/sa/curl")).matchesID(spiffeID(P.id)) == true                                       |
| spiffeMatchOneOf       | Match any one of SPIFFE IDs                        | spiffeMatchOneOf(\["spiffe://cerbos.dev/ns/privileged/sa/curl", "spiffe://cerbos.dev/ns/privileged/sa/foo"\]).matchesID(spiffeID(P.id)) == true |
| spiffeMatchTrustDomain | Match any ID from the trust domain                 | spiffeMatchTrustDomain(spiffeTrustDomain("spiffe://cerbos.dev")).matchesID(spiffeID(P.id)) == true                                              |
| spiffeTrustDomain.id   | Fully qualified trust domain ID                    | spiffeTrustDomain("cerbos.dev").id() == "spiffe://cerbos.dev"                                                                                   |
| spiffeTrustDomain.name | Name of trust domain                               | spiffeTrustDomain("spiffe://cerbos.dev").name() == "cerbos.dev"                                                                                 |

## [](#%5Fstrings)Strings

Test data

```json
...
"resource": {
  "kind": "leave_request",
  "attr": {
    "id": "125",
    "department": "marketing"
  }
}
...
```

| Function      | Description                                                                                                 | Example                                                                                                     |
| ------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| base64.encode | Encode as base64                                                                                            | base64.encode(bytes("hello")) == "aGVsbG8="                                                                 |
| base64.decode | Decode base64                                                                                               | base64.decode("aGVsbG8=") == bytes("hello")                                                                 |
| charAt        | Get the character at given index                                                                            | R.attr.department.charAt(1) == 'a'                                                                          |
| contains      | Check whether a string contains the given substring                                                         | R.attr.department.contains("arket")                                                                         |
| endsWith      | Check whether a string has the given suffix                                                                 | R.attr.department.endsWith("ing")                                                                           |
| format        | Format a string with the given arguments                                                                    | "department\_%s\_%d".format(\["marketing", 1\])                                                             |
| indexOf       | Index of the first occurrence of the given character                                                        | R.attr.department.indexOf('a') == 1                                                                         |
| lastIndexOf   | Index of the last occurrence of the given character                                                         | R.attr.department.lastIndexOf('g') == 8                                                                     |
| lowerAscii    | Convert ASCII characters to lowercase                                                                       | "MARKETING".lowerAscii() == R.attr.department                                                               |
| matches       | Check whether a string matches a [RE2](https://github.com/google/re2/wiki/Syntax) regular expression        | R.attr.department.matches("^\[mM\].\*g$")                                                                   |
| replace       | Replace all occurrences of a substring                                                                      | R.attr.department.replace("market", "engineer") == "engineering"                                            |
| replace       | Replace with limits. Limit 0 replaces nothing, -1 replaces all.                                             | "engineering".replace("e", "a", 1) == "angineering" && "engineering".replace("e", "a", -1) == "anginaaring" |
| size          | Get the length of the string                                                                                | size(R.attr.department) == 9                                                                                |
| split         | Split a string using a delimiter                                                                            | "a,b,c,d".split(",")\[1\] == "b"                                                                            |
| split         | Split a string with limits. Limit 0 returns an empty list, 1 returns a list containing the original string. | "a,b,c,d".split(",", 2)\[1\] == "b,c,d"                                                                     |
| startsWith    | Check whether a string has the given prefix                                                                 | R.attr.department.startsWith("mark")                                                                        |
| substring     | Selects a substring from the string                                                                         | R.attr.department.substring(4) == "eting" && R.attr.department.substring(4, 6) == "et"                      |
| trim          | Remove whitespace from beginning and end                                                                    | " marketing ".trim() == "marketing"                                                                         |
| upperAscii    | Convert ASCII characters to uppercase                                                                       | R.attr.department.upperAscii() == "MARKETING"                                                               |

## [](#%5Ftimestamps)Timestamps

| |  All timestamp getters (getHours, getMinutes, getDayOfWeek, and similar) take a time zone parameter. If omitted, the 'UTC' time zone is used by default. |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |

Test data

```json
...
"resource": {
  "kind": "leave_request",
  "attr": {
    "lastAccessed": "2021-04-20T10:00:20.021-05:00",
    "lastUpdateTime": "2021-05-01T13:34:12.024Z",
  }
}
...
```

| Function        | Description                                                                                             | Example                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| timestamp       | Convert an RFC3339 formatted string to a timestamp                                                      | timestamp(R.attr.lastAccessed).getFullYear() == 2021        |
| getDate         | Get day of month from a timestamp                                                                       | timestamp(R.attr.lastAccessed).getDate() == 20              |
| getDayOfMonth   | Get day of month from a timestamp. Returns a zero-based value                                           | timestamp(R.attr.lastAccessed).getDayOfMonth() == 19        |
| getDayOfWeek    | Get day of week from a timestamp. Returns a zero-based value where Sunday is 0                          | timestamp(R.attr.lastAccessed).getDayOfWeek() == 2          |
| getDayOfYear    | Get day of year from a timestamp. Returns a zero-based value                                            | timestamp(R.attr.lastAccessed).getDayOfYear() == 109        |
| getFullYear     | Get full year from a timestamp                                                                          | timestamp(R.attr.lastAccessed).getFullYear() == 2021        |
| getHours        | Get hours from a timestamp                                                                              | timestamp(R.attr.lastAccessed).getHours("-05:00") == 10     |
| getMilliseconds | Get milliseconds from a timestamp                                                                       | timestamp(R.attr.lastAccessed).getMilliseconds() == 21      |
| getMinutes      | Get minutes from a timestamp                                                                            | timestamp(R.attr.lastAccessed).getMinutes("UTC") == 5       |
| getMonth        | Get month from a timestamp. Returns a zero-based value where January is 0                               | timestamp(R.attr.lastAccessed).getMonth("NZ") == 3          |
| getSeconds      | Get seconds from a timestamp                                                                            | timestamp(R.attr.lastAccessed).getSeconds() == 20           |
| now             | Current time on the server. This is a Cerbos extension to CEL                                           | now() > timestamp(R.attr.lastAccessed)                      |
| timeSince       | Time elapsed since the given timestamp to current time on the server. This is a Cerbos extension to CEL | timestamp(R.attr.lastAccessed).timeSince() > duration("1h") |

Example: Assert that more than 36 hours has elapsed between last access time and last update time

```yaml
timestamp(R.attr.lastUpdateTime) - timestamp(R.attr.lastAccessed) > duration("36h")
```

Example: Add a duration to a timestamp

```yaml
timestamp(R.attr.lastUpdateTime) + duration("24h") == timestamp("2021-05-02T13:34:12.024Z")
```

Derived roles
====================
Traditional RBAC roles are usually broad groupings with no context awareness. They are static and they are provided by the Identity Provider(IDP), not by Cerbos. Cerbos provides derived roles as a way of augmenting those broad roles with contextual data to provide more fine-grained control at runtime. For example, a person with the broad `manager` role can be augmented to `manager_of_scranton_branch` by taking into account the geographic location (or another factor) and giving that derived role bearer extra privileges on resources that belong to the Scranton branch.

| |  Derived roles are dynamically determined at runtime by matching the principal’s roles sent in the [API request](../api/index.html#check-resources) to the parentRoles specified in the derived roles definitions. Don’t use the derived role names as roles in the API request as Cerbos only expects that field to contain "normal" roles. |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

```yaml
---
apiVersion: "api.cerbos.dev/v1"
description: |-
  Common dynamic roles used within the Apatr app
derivedRoles:
  name: apatr_common_roles (1)
  constants:
    import: (2)
      - apatr_common_constants
    local: (3)
      corporate_network_ip_range: 10.20.0.0/16
  variables:
    import: (4)
      - apatr_common_variables
    local: (5)
      flagged_resource: request.resource.attr.flagged
  definitions:
    - name: owner (6)
      parentRoles: ["user"] (7)
      condition: (8)
        match:
          expr: request.resource.attr.owner == request.principal.id

    - name: abuse_moderator
      parentRoles: ["moderator"]
      condition:
        match:
          expr: variables.flagged_resource

    - name: corporate_user
      parentRoles: ["user"]
      condition:
        match:
          expr: request.principal.attr.ip_address.inIPAddrRange(constants.corporate_network_ip_range)
```

| **1** | Name to use when importing this set of derived roles.                                                                                    |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [Constant definitions](variables.html#export-constants) to import (optional).                                                            |
| **3** | [Local constant definitions](variables.html#local-constants) (optional).                                                                 |
| **4** | [Variable definitions](variables.html#export) to import (optional).                                                                      |
| **5** | [Local variable definitions](variables.html#local) (optional).                                                                           |
| **6** | Descriptive name for this derived role.                                                                                                  |
| **7** | The static roles (from the identity provider) to which this derived role applies to. The special value \* can be used to match any role. |
| **8** | An (optional) set of expressions that should evaluate to true for this role to activate.                                                 |

Understanding derived roles

To explain the concept of derived roles, consider this example from the DC Comics universe: when billionaire playboy Bruce Wayne wears the bat costume he becomes Batman, the caped crusader. Becoming Batman gives Bruce extra privileges like being able to beat up criminals without any consequences and driving a tank through the streets of Gotham. In Cerbos terms, Batman is the `derived role` and Bruce Wayne is the `parentRole`. The `condition` for activating the Batman derived role is: `Bruce Wayne is wearing the bat costume`.

Cerbos only ever deals with Bruce Wayne because he’s the only real person in this scenario. However, Cerbos is smart enough to treat him as Batman whenever he’s wearing his costume.

```yaml
---
apiVersion: "api.cerbos.dev/v1"
derivedRoles:
  name: gotham_city
  definitions:
    - name: batman
      parentRoles: ["bruce_wayne"]
      condition:
        match:
          expr: P.attr.isWearingBatCostume
```

Cerbos policies
====================
There are six kinds of Cerbos policies:

[Derived roles](derived%5Froles.html)

Traditional RBAC roles are usually broad groupings with no context awareness. Derived roles are a way of augmenting those broad roles with contextual data to provide more fine-grained control at runtime. For example, a person with the broad `manager` role can be augmented to `manager_of_scranton_branch` by taking into account the geographic location (or another factor) and giving that derived role bearer extra privileges on resources that belong to the Scranton branch.

[Resource policies](resource%5Fpolicies.html)

Defines rules for actions that can be performed on a given resource. A resource is an application-specific concept that applies to anything that requires access rules. For example, in an HR application, a resource can be as coarse-grained as a full employee record or as fine-grained as a single field in the record.

[Principal policies](principal%5Fpolicies.html)

Defines overrides for a specific user.

[Role policies](role%5Fpolicies.html)

Define rules specific to a given role. Rules are defined as a list of allowable actions that apply to a particular resource.

[Exported variables](variables.html#export)

Defines variables to be reused in condition expressions in other policies.

[Exported constants](variables.html#export-constants)

Defines constants to be reused in condition expressions in other policies.

Policies are evaluated based on the metadata passed in the request to the Cerbos PDP. See [Cerbos API](../api/index.html) for more information.

| |  View the latest documentation and example requests by accessing a running Cerbos instance using a browser (<http://localhost:3592/>). The OpenAPI (Swagger) schema can be obtained by accessing /schema/swagger.json as well. |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Outputs
====================
You can define an optional expression to be evaluated when a policy rule is fully activated (`action`, `roles` and`derivedRoles` match and `condition` is satisfied) or partially activated (`condition` is not satisfied). The collected outputs from all the rules are included in the Cerbos API response.

Output expressions are useful if you want to take specific actions in your application based on the triggered rules. For example, if your policy contains a rule that denies access if the request is issued outside working hours, it could output a string that explains the restriction. Your application could then display that back to the user so that they know the specific reason why the request was denied.

Consider the following policy definition:

```yaml
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: "default"
  resource: "system_access"
  rules:
    - name: working-hours-only
      actions: ['*']
      effect: EFFECT_DENY
      roles: ['*']
      condition:
        match:
          expr: now().getHours() > 18 || now().getHours() < 8
      output:
        when:
          ruleActivated: |-
            {"principal": P.id, "resource": R.id, "timestamp": now(), "message": "System can only be accessed between 0800 and 1800"}
          conditionNotMet: |-
            {"principal": P.id, "resource": R.id, "timestamp": now(), "message": "System can be accessed at this time"}
```

If a request is made outside working hours, the response from Cerbos would resemble the following:

```json
{
  "requestId": "xx-010023-23459",
  "results": [
    {
      "resource": {
        "id": "bastion_002",
        "kind": "system_access"
      },
      "actions": {
        "login": "EFFECT_DENY"
      },
      "meta": {
        "actions": {
          "login": {
            "matchedPolicy": "resource.system_access.vdefault"
          }
        }
      },
      "outputs": [
        {
          "src": "resource.system_access.vdefault#working-hours-only",
          "val": {
            "message": "System can only be accessed between 0800 and 1800",
            "principal": "john",
            "resource": "bastion_002",
            "timestamp": "2023-06-02T21:53:58.319506543+01:00"
          }
        }
      ]
    }
  ]
}
```

If a request is made inside working hours, the response would resemble the following:

```json
{
  "requestId": "xx-010023-23459",
  "results": [
    {
      "resource": {
        "id": "bastion_002",
        "kind": "system_access"
      },
      "actions": {
        "login": "EFFECT_ALLOW"
      },
      "meta": {
        "actions": {
          "login": {
            "matchedPolicy": "resource.system_access.vdefault"
          }
        }
      },
      "outputs": [
        {
          "src": "resource.system_access.vdefault#working-hours-only",
          "val": {
            "message": "System can be accessed at this time",
            "principal": "john",
            "resource": "bastion_002",
            "timestamp": "2023-06-02T21:53:58.319506543+01:00"
          }
        }
      ]
    }
  ]
}
```

| |  Depending on the evaluation result of the expression(s) under the condition.match, the result of the expressionoutput.when.ruleActivated or output.when.conditionNotMet will be rendered in the output. |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Output expressions can be any valid CEL expression. You can return simple values such as strings, numbers and booleans or complex values such as maps and lists.

| |  Excessive use of output expressions could affect policy evaluation performance. If you use them for debugging purposes, remember to remove them before going to production. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

Principal policies
====================
Principal policies define overrides for a specific user.

```yaml
---
apiVersion: "api.cerbos.dev/v1"
principalPolicy:
  principal: daffy_duck (1)
  version: "dev" (2)
  scope: "acme.corp" (3)
  scopePermissions: SCOPE_PERMISSIONS_REQUIRE_PARENTAL_CONSENT_FOR_ALLOWS (4)
  constants:
    import: (5)
      - apatr_common_constants
    local: (6)
      test_department_id: 12345
  variables:
    import: (7)
      - apatr_common_variables
    local: (8)
      is_dev_record: |-
        request.resource.attr.dev_record == true || request.resource.attr.department_id == constants.test_department_id
  rules:
    - resource: leave_request (9)
      actions:
        - name: dev_record_wildcard (10)
          action: "*" (11)
          condition: (12)
            match:
              expr: variables.is_dev_record
          effect: EFFECT_ALLOW
          output: (13)
            when:
              ruleActivated: |-
                "wildcard_override:%s".format([request.principal.id])
              conditionNotMet: |-
                "wildcard_condition_not_met:%s".format([request.principal.id])

    - resource: employee_profile
      actions:
        - name: view_employee_profile
          action: "*"
          condition:
            match:
              all:
                of:
                  - expr: variables.is_dev_record
                  - expr: request.resource.attr.public == true
          effect: EFFECT_ALLOW

    - resource: salary_record
      actions:
        - action: "*"
          effect: EFFECT_DENY
```

| **1**  | Principal to whom this policy applies.                                                                                                                                                                                                                                                                       |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2**  | Version of this policy. Policies are uniquely identified by the principal name and version pair. You can have multiple policy versions for the same principal (e.g. production vs. staging). The version value default is special as it is the default fallback when no version is specified in the request. |
| **3**  | Optional [scope](scoped%5Fpolicies.html) for this policy.                                                                                                                                                                                                                                                    |
| **4**  | Optional [scope permission](scope%5Fpermissions.html) for this policy, defaults to SCOPE\_PERMISSIONS\_OVERRIDE\_PARENT.                                                                                                                                                                                     |
| **5**  | [Constant definitions](variables.html#export-constants) to import (optional).                                                                                                                                                                                                                                |
| **6**  | [Local constant definitions](variables.html#local-constants) (optional).                                                                                                                                                                                                                                     |
| **7**  | [Variable definitions](variables.html#export) to import (optional).                                                                                                                                                                                                                                          |
| **8**  | [Local variable definitions](variables.html#local) (optional).                                                                                                                                                                                                                                               |
| **9**  | Resource to which this override applies. Wildcards are supported here.                                                                                                                                                                                                                                       |
| **10** | Optional name for the rule.                                                                                                                                                                                                                                                                                  |
| **11** | Actions that can be performed on the resource. Wildcards are supported here.                                                                                                                                                                                                                                 |
| **12** | Optional conditions required to match this rule.                                                                                                                                                                                                                                                             |
| **13** | Optional output for the action rule. You can define optional expressions to be evaluated as output depending on whether the rule is activated or not activated because of a condition failure.                                                                                                               |

Resource policies
====================
Resource policies define rules for actions that can be performed on a given resource. A resource is an application-specific concept that applies to anything that requires access rules. For example, in an HR application, a resource can be as coarse-grained as a full employee record or as fine-grained as a single field in the record.

Multiple rules can be defined for the same action on a resource for different roles and/or with different conditions. If more than one rule matches a given input, then a rule specifying `EFFECT_DENY` will take precedence over one specifying `EFFECT_ALLOW`.

```yaml
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  resource: "album:object" (1)
  version: "default" (2)
  scope: "acme.corp" (3)
  scopePermissions: SCOPE_PERMISSIONS_REQUIRE_PARENTAL_CONSENT_FOR_ALLOWS (4)
  importDerivedRoles:
    - apatr_common_roles (5)
  constants:
    import: (6)
      - apatr_common_constants
    local: (7)
      corporate_network_ip_range: 10.20.0.0/16
  variables:
    import: (8)
      - apatr_common_variables
    local: (9)
      is_corporate_network: |-
        request.principal.attr.ip_address.inIPAddrRange(constants.corporate_network_ip_range)
  rules:
    - actions: ['*'] (10)
      effect: EFFECT_ALLOW
      derivedRoles:
        - owner (11)

    - actions: ['view']
      effect: EFFECT_ALLOW
      roles:
        - user (12)
      condition:
        match:
          expr: request.resource.attr.public == true
      output: (13)
        when:
          ruleActivated: |-
            "view_allowed:%s".format([request.principal.id])
          conditionNotMet: |-
            "view_not_allowed:%s".format([request.principal.id])

    - name: moderator_rule (14)
      actions: ['view', 'delete']
      effect: EFFECT_ALLOW
      condition:
        match:
          expr: variables.is_corporate_network
      derivedRoles:
        - abuse_moderator
  schemas: (15)
    principalSchema:
      ref: cerbos:///principal.json (16)
    resourceSchema:
      ref: cerbos:///album/object.json (17)
```

| **1**  | Kind of resource to which this policy applies.                                                                                                                                                                                                                                                             |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2**  | Version of this policy. Policies are uniquely identified by the resource name and version pair. You can have multiple policy versions for the same resource (e.g. production vs. staging). The version value default is special as it is the default fallback when no version is specified in the request. |
| **3**  | Optional [scope](scoped%5Fpolicies.html) for this policy.                                                                                                                                                                                                                                                  |
| **4**  | Optional [scope permission](scope%5Fpermissions.html) for this policy, defaults to SCOPE\_PERMISSIONS\_OVERRIDE\_PARENT.                                                                                                                                                                                   |
| **5**  | Import a set of [derived roles](derived%5Froles.html) (optional).                                                                                                                                                                                                                                          |
| **6**  | [Constant definitions](variables.html#export-constants) to import (optional).                                                                                                                                                                                                                              |
| **7**  | [Local constant definitions](variables.html#local-constants) (optional).                                                                                                                                                                                                                                   |
| **8**  | [Variable definitions](variables.html#export) to import (optional).                                                                                                                                                                                                                                        |
| **9**  | [Local variable definitions](variables.html#local) (optional).                                                                                                                                                                                                                                             |
| **10** | Actions can contain wildcards. Wildcards honour the : delimiter. E.g. a:\*:d would match a:x:d but not a:x.                                                                                                                                                                                                |
| **11** | This rule applies to a derived role.                                                                                                                                                                                                                                                                       |
| **12** | Rules can also refer directly to static roles. The special value \* can be used to disregard roles when evaluating the rule.                                                                                                                                                                               |
| **13** | Optional output for the action rule. You can define optional expressions to be evaluated as output depending on whether the rule is activated or not activated because of a condition failure.                                                                                                             |
| **14** | Optional name for the rule.                                                                                                                                                                                                                                                                                |
| **15** | Optional section for defining schemas that apply to this resource kind.                                                                                                                                                                                                                                    |
| **16** | Optional schema for validating the principal attributes.                                                                                                                                                                                                                                                   |
| **17** | Optional schema for validating the resource attributes.                                                                                                                                                                                                                                                    |

Role policies
====================
Role policies are ABAC policies in which you specify a number of resources, each with a set of allowable actions that the role can carry out on the resource. Optionally, a condition can also be specified for each set of allowable actions. In the simple case, they allow you to author permissions from the view of an IdP role, rather than for a given resource.

Unlike resource and principal policies, role policies do not define explicit `ALLOW` or `DENY` effects. Instead, the **allowable actions** act as an exhaustive list of actions allowed on each resource. Any resource and action pair not defined in this list is immediately denied for that role.

The name of a role policy is effectively a custom role within the context of Cerbos. A role policy (custom role) can optionally define `parentRoles`, inheriting and narrowing their permissions by default. The policy can only define rules that are a strict subset of the parent role’s permissions and cannot introduce any extra rules beyond what the parent roles allow. They can immediately DENY an action but if they ALLOW an action, a parent policy higher up the scope chain must also ALLOW the same action.

A parent role can be either an arbitrary IdP role or the name of another role policy within the system. Parent role resolution is recursive—if a custom role inherits from another custom role that also has parent roles, it inherits and narrows their permissions as well.

```yaml
---
apiVersion: api.cerbos.dev/v1
rolePolicy:
  role: "acme_admin" (1)
  version: "default" (2)
  scope: "acme.hr.uk" (3)
  parentRoles: (4)
    - admin
  rules:
    - resource: leave_request (5)
      allowActions: (6)
        - view:* (7)
        - deny

    - resource: salary_record
      allowActions:
        - edit
      condition: (8)
        match:
          expr: R.attr.owner == P.id

    - resource: "*" (9)
      allowActions: ["create"]
```

| **1** | The role to which this policy applies.                                                                                                                                                                                                                                                             |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Version of this policy. Policies are uniquely identified by the role name and version pair. You can have multiple policy versions for the same role (e.g. production vs. staging). The version value default is special as it is the default fallback when no version is specified in the request. |
| **3** | Optional principal [scope](scoped%5Fpolicies.html) for this policy.                                                                                                                                                                                                                                |
| **4** | The list of parent roles that the custom role inherits.                                                                                                                                                                                                                                            |
| **5** | The resource to which the following rule applies.                                                                                                                                                                                                                                                  |
| **6** | The list of allowable actions that the role can carry out on the given resource.                                                                                                                                                                                                                   |
| **7** | Wildcard actions are supported.                                                                                                                                                                                                                                                                    |
| **8** | A condition that must be met for the action to be allowed.                                                                                                                                                                                                                                         |
| **9** | Wildcard resources are also supported.                                                                                                                                                                                                                                                             |

Schemas
====================
Cerbos policies rely on context data about the principal and the resource(s) that are submitted through the `attr` fields of the [API request](../api/index.html). While the free-form nature of these fields gives you maximum flexibility to author policies that work on data of any shape or form, they can become difficult to reason about and make it harder to enforce system-wide standards and conventions.

Using the [JSON Schema](http://json-schema.org) support built into Cerbos, you can define schemas for all your principal and resource attributes on a per-resource basis by specifying them in the resource policy. The Cerbos PDP will validate the incoming requests and either log warnings or completely reject them based on the schema enforcement configuration in effect.

## [](#%5Fdefine%5Fschemas)Define schemas

Cerbos schemas are standard [JSON Schemas](http://json-schema.org/specification.html) (draft 2020-12). If you are using any of `disk`, `git` or `blob` [storage drivers](../configuration/storage.html) the schemas are expected to be in a special directory named `_schemas` located at the root of the storage directory or bucket. Use the [Admin API](../api/admin%5Fapi.html) to add or update schemas if you are using one of the database drivers.

To avoid repetition, you can define common schema fragments inline using `$defs` or refer to other schemas using `$ref` (see <https://json-schema.org/understanding-json-schema/structuring.html>). When using `$ref` to refer to another schema stored in Cerbos storage, make sure to use an absolute URL with `cerbos` as the scheme. For example, use `cerbos:///common/address.json` to refer to a schema file stored in `_schemas/common/address.json` (if using one of the disk-based stores). This ensures that policies remain portable between different environments.

customer.json: a schema that references another schema to avoid repetition

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "first_name": { "type": "string" },
    "last_name": { "type": "string" },
    "shipping_address": { "$ref": "cerbos:///address.json" },
    "billing_address": { "$ref": "cerbos:///address.json" }
  },
  "required": ["first_name", "last_name", "shipping_address", "billing_address"]
}
```

address.json: the schema referenced by customer.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "street_address": { "type": "string" },
    "city": { "type": "string" },
    "state": { "type": "string" }
  },
  "required": ["street_address", "city", "state"]
}
```

## [](#%5Fvalidate%5Frequests%5Fusing%5Fschemas)Validate requests using schemas

First, update your resource policy to point to the schemas that should be used to validate requests for that resource kind. For example, the following resource policy requires all requests for `album:object` resource kind to be validated using `principal.json` for the principal attributes and `album/object.json` for the resource attributes respectively.

Example

```yaml
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  importDerivedRoles:
    - apatr_common_roles
  resource: "album:object"
  rules:
    - actions: ['create']
      effect: EFFECT_ALLOW
      derivedRoles:
        - owner

    - actions: ['view']
      effect: EFFECT_ALLOW
      roles:
        - user
      condition:
        match:
          expr: request.resource.attr.public == true

  schemas: (1)
    principalSchema: (2)
      ref: cerbos:///principal.json
    resourceSchema: (3)
      ref: cerbos:///album/object.json
      ignoreWhen: (4)
        actions: ['create', 'delete:*']
```

| **1** | Schema definition block. Optional. Leave this out if you do not want to use schema validation for this resource type.                                                                                                            |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Schema for validating the principal attributes. Optional. Leave this out if you do not want to validate the principal.                                                                                                           |
| **3** | Schema for validating the resource attributes. Optional. Leave this out if you do not want to validate the resource.                                                                                                             |
| **4** | Ignore block. Optional. Define the actions for which schema validation should be ignored. This is useful for special cases like CREATE where your resource might not have all the required attributes to pass schema validation. |

Finally, [configure the schema enforcement level](../configuration/schema.html) of the Cerbos PDP to either `warn` or `reject` and restart it. Now the PDP will validate any requests where the matching resource policy has schemas specified.

| |  If enforcement level is reject and the request is invalid according to the schema, the effect for all actions will be set to EFFECT\_DENY. If enforcement level is warn, then Cerbos will still evaluate the policies and return the effects determined by the policy. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Example: CheckResourceSet API response containing validation errors

```json
{
  "requestId": "test",
  "resourceInstances": {
    "XX125": {
      "actions": {
        "approve": "EFFECT_DENY",
        "create": "EFFECT_DENY",
        "defer": "EFFECT_ALLOW",
        "view:public": "EFFECT_ALLOW"
      },
      "validationErrors": [
        {
          "path": "/department",
          "message": "value must be one of \"marketing\", \"engineering\"",
          "source": "SOURCE_PRINCIPAL"
        },
        {
          "path": "/department",
          "message": "value must be one of \"marketing\", \"engineering\"",
          "source": "SOURCE_RESOURCE"
        }
      ]
    }
  }
}
```

Scope Permissions
====================
`scopePermissions` is a setting applied to resource and principal policies that impacts how rules are evaluated within a scope hierarchy. It defines whether policies in a given scope can **override** parent scope rules or whether they can only **restrict** the permissions granted by parent scopes.

All resource or principal policies within the same scope **must** use the same `scopePermissions` setting. If conflicting settings are detected within a shared scope, a build-time error will occur.

There are two available settings:

* `SCOPE_PERMISSIONS_OVERRIDE_PARENT`
* `SCOPE_PERMISSIONS_REQUIRE_PARENTAL_CONSENT_FOR_ALLOWS`

| |  By default, resource and principal policies use SCOPE\_PERMISSIONS\_OVERRIDE\_PARENT unless explicitly set otherwise. |
| ------------------------------------------------------------------------------------------------------------------------ |

### [](#%5Fscope%5Fpermissions%5Foverride%5Fparent)SCOPE\_PERMISSIONS\_OVERRIDE\_PARENT

This is the default evaluation strategy for scoped policies. Cerbos starts evaluating policies from the bottom of the scope chain and moves up. The first policy to produce a decision for a given action is the winner. Any policies further up the chain cannot influence that decision.

* If an input matches a rule and its condition is met, the specified effect is applied (no need to check parents).
* If a rule is matched but its condition is not met, or if a rule is not matched, evaluation continues up the hierarchy.

### [](#%5Fscope%5Fpermissions%5Frequire%5Fparental%5Fconsent%5Ffor%5Fallows)SCOPE\_PERMISSIONS\_REQUIRE\_PARENTAL\_CONSENT\_FOR\_ALLOWS

When a policy is configured with `scopePermissions: SCOPE_PERMISSIONS_REQUIRE_PARENTAL_CONSENT_FOR_ALLOWS`, it **inherits and restricts** the permissions of parent scopes. Policies at this level must define rules within the maximum set of permissions allowed by parent policies—they cannot introduce new permissions that exceed what a parent scope already permits.

In this mode, an `ALLOW` rule that matches an action doesn’t immediately generate an `ALLOW` decision. A parent policy higher up in the scope chain must also `ALLOW` that same action in order to produce a definitive decision. However, if a rule is matched but its condition is not met, the request is implicitly denied.

* If an input is not matched, evaluation continues up the scope hierarchy.
* If a rule is matched but its condition is not met, an implicit DENY is issued.
* If a rule matches and the condition is met, evaluation continues to parent policies to verify that the action is also allowed at a higher level.

Scoped policies
====================
| |  Scoped Policies are optional and are only evaluated if a "scope" is passed in the request, and there are matching "scope" attributes defined in the policies. |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| |  Empty scope can also be represented by setting the "scope" to value "." in the request. |
| ------------------------------------------------------------------------------------------ |

| |  Resource and principal policies can define "scopePermissions", which affects how rules are applied across scopes. See the [scope permissions documentation](scope%5Fpermissions.html) for more details. |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Scoped policies offer a way to model hierarchical relationships that regularly occur in many situations. Typically, the requirement is to have a base set of policies that can then be overridden for specific cases. For example, a multi-tenant SaaS system could have a standard set of access rules that can then be customised to suit the requirements of different tenants. Another example is a large organization that might want to have regional or departmental customisations to their global access rules.

![hierarchy](_images/hierarchy.png) 

Cerbos resource and principal policies have an optional `scope` field that can be used to indicate that they are part of a set of policies that must be evaluated together. Additionally, resource and principal policies within the same scope must use the same `scopePermissions` setting to define how rules interact across scope levels.

```yaml
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: "default"
  scope: "acme.corp" (1)
  scopePermissions: SCOPE_PERMISSIONS_OVERRIDE_PARENT (2)
  resource: "album:object"
  rules:
    - actions: ['*']
      effect: EFFECT_ALLOW
      roles: ["admin"]
```

| **1** | Scope definition          |
| ----- | ------------------------- |
| **2** | Scope permissions setting |

The value of `scope` is a dot-separated string where each dotted segment defines an ancestor. During policy evaluation, the Cerbos engine starts with the most specific scoped policy and moves up the hierarchy. NOTE: The value of the `scopePermissions` field affects the policy evaluation behaviour. See [scope permissions](scope%5Fpermissions.html) for more information. For example, consider a policy with the scope `a.b.c`. The Cerbos engine could process up to four policies to arrive at the final decision:

* scope `a.b.c`
* scope `a.b`
* scope `a`
* scope \`\` (no scope)

To illustrate, consider the following Check request:

```json
{
  "requestId":  "test01",
  "actions":  ["view", "comment"],
  "resource":  {
    "kind":  "album:object",
    "policyVersion": "default",
    "scope": "customer.abc", (1)
    "instances": {
      "XX125": {
        "attr":  {
          "owner":  "alicia",
          "public": false,
          "tags": ["x", "y"],
        }
      }
    }
  },
  "principal":  {
    "id":  "alicia",
    "policyVersion": "default",
    "scope": "customer", (2)
    "roles":  ["user"],
    "attr": {
      "geography": "GB"
    }
  }
}
```

| **1** | Optional resource scope  |
| ----- | ------------------------ |
| **2** | Optional principal scope |

When processing the above request, the decision flow chart for the Cerbos engine would look like the following:

![decision flow](_images/decision_flow.png) 

## [](#%5Fworking%5Fwith%5Fscoped%5Fpolicies)Working with scoped policies

* The policy without any scope defined is always the base policy. It is used by default if a request does not specify any scope.
* Scope permissions must be consistent within the same scope. If conflicting `scopePermissions` settings are detected in policies within a shared scope, a build-time error will occur.
* Scope traversal behaviour depends on `scopePermissions`:  
   * With `SCOPE_PERMISSIONS_OVERRIDE_PARENT`, the first policy to return a decision wins for each action.  
   * With `SCOPE_PERMISSIONS_REQUIRE_PARENTAL_CONSENT_FOR_ALLOWS`, leaf nodes can only **restrict** access and must conform to parent permissions.
* There must be no gaps in the policy chain. For example, if you define a policy with scope `a.b.c`, then policies with scopes `a.b`, `a`, and no-scope should also exist in the policy repository.
* [Schemas](schemas.html) must be the same among all the policies in the chain. The schemas used to validate the request are taken from the base policy (policy without a scope). Schemas defined in other policies of the chain will be ignored.
* First match wins (when using `SCOPE_PERMISSIONS_OVERRIDE_PARENT`): Scoped policies are evaluated from the most specific to the least specific. The first policy to produce a decision (ALLOW/DENY) for an action is the winner. The remaining policies cannot override the decision for that particular action.
* Parent constraints apply (when using `SCOPE_PERMISSIONS_REQUIRE_PARENTAL_CONSENT_FOR_ALLOWS`): The most specific policies can only **restrict permissions** further, not grant new ones.
* **Explicit imports for derived roles and variables**: Variables and derived roles imports are not inherited between policies. Explicitly import any derived roles and re-define any variables in each policy that requires them.
* Unless [lenient scope search](../configuration/engine.html#lenient%5Fscopes) is enabled, a policy file matching the exact scope requested in the API request must exist in the store.

Variables and constants
====================
## [](#variables)Variables

You can use variables to reduce duplication in [policy condition expressions](conditions.html). Variables may either be defined locally within a policy, or in a standalone `exportVariables` policy file that can be imported by other policies.

### [](#local)Defining local variables

Local variables are only accessible from the policy they are defined. In particular, local variables defined for derived roles can’t be used in resource policies that import the derived roles.

```yaml
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  variables:
    local: (1)
      flagged_resource: request.resource.attr.flagged
      label: '"latest"' # assigning a string literal
      teams: '["red", "blue"]' # assigning an array literal
      lookup: '{"red": 9001, "blue": 0}' # assigning a map literal
  # ...
```

| **1** | Map of variable name to expression. |
| ----- | ----------------------------------- |

### [](#export)Defining and importing exported variables

To reuse variables between policies, they can be exported from a separate file.

```yaml
---
apiVersion: api.cerbos.dev/v1
description: Common variables used within the Apatr app
exportVariables:
  name: apatr_common_variables (1)
  definitions: (2)
    flagged_resource: request.resource.attr.flagged
    label: '"latest"' # assigning a string literal
    teams: '["red", "blue"]' # assigning an array literal
    lookup: '{"red": 9001, "blue": 0}' # assigning a map literal
```

| **1** | Name to use when importing this set of variables. |
| ----- | ------------------------------------------------- |
| **2** | Map of variable name to expression.               |

Other policies can then import the variables by name.

```yaml
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  variables:
    import: (1)
      - apatr_common_variables
  # ...
```

| **1** | List of names of variable sets to import. |
| ----- | ----------------------------------------- |

### [](#%5Fusing%5Fvariables%5Fin%5Fpolicy%5Fconditions)Using variables in policy conditions

Variables can be referenced via the `variables` (aliased to `V`) special variable in policy condition expressions.

```yaml
---
condition:
  match:
    expr: variables.flagged_resource
```

Local and imported variable definitions are merged, and each variable is evaluated before any rule condition. If a variable is defined in more than one location, the policy will fail to compile.

### [](#%5Ftop%5Flevel%5Fvariables%5Ffield)Top-level variables field

In earlier versions of Cerbos, local variables were defined in a top-level `variables` field in the policy file. This field is deprecated in favour of the `variables.local` section within the policy body. For backwards compatibility, the deprecated top-level field is merged with the `variables.local` section in derived roles, resource, and principal policies.

## [](#constants)Constants

Variables are expressions that are evaluated at runtime. That makes them slightly awkward to use with literal values, because you have to quote the value to make it a valid [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md) expression.

Constants are an alternative to defining variables with literal values, which allow the values to be written using standard YAML or JSON syntax.

### [](#local-constants)Defining local constants

Local constants are only accessible from the policy they are defined. In particular, local constants defined for derived roles can’t be used in resource policies that import the derived roles.

```yaml
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  constants:
    local: (1)
      label: latest
      teams:
        - red
        - blue
      lookup:
        red: 9001
        blue: 0
  # ...
```

| **1** | Map of constant name to value. |
| ----- | ------------------------------ |

### [](#export-constants)Defining and importing exported constants

To reuse constants between policies, they can be exported from a separate file.

```yaml
---
apiVersion: api.cerbos.dev/v1
description: Common constants used within the Apatr app
exportConstants:
  name: apatr_common_constants (1)
  definitions: (2)
    label: latest
    teams:
      - red
      - blue
    lookup:
      red: 9001
      blue: 0
```

| **1** | Name to use when importing this set of constants. |
| ----- | ------------------------------------------------- |
| **2** | Map of constant name to value.                    |

Other policies can then import the constants by name.

```yaml
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  constants:
    import: (1)
      - apatr_common_constants
  # ...
```

| **1** | List of names of constant sets to import. |
| ----- | ----------------------------------------- |

### [](#%5Fusing%5Fconstants%5Fin%5Fpolicy%5Fconditions)Using constants in policy conditions

Constants can be referenced via the `constants` (aliased to `C`) special variable in policy condition expressions.

```yaml
---
condition:
  match:
    expr: constants.lookup[request.principal.attr.team] > 9000
```

Local and imported constant definitions are merged. If a constant is defined in more than one location, the policy will fail to compile.

Integrating permission checks into your user interface
====================
It’s a common requirement to make permission checks in the user interface layer of your application. For example, you might want to hide the "Edit" button if the current user isn’t allowed to edit the corresponding resource.

You can tackle this by checking the user’s permissions in the back end of your application and including the results in your API responses, by calling the Cerbos PDP directly from the browser, or by evaluating your policies in the browser.

| |  Checking permissions in the user interface is not a substitute for performing checks in the back end. |
| -------------------------------------------------------------------------------------------------------- |

## [](#%5Fincluding%5Fpermissions%5Fin%5Fapi%5Fresponses)Including permissions in API responses

You can add a `permissions` field to relevant API responses, and populate it by calling the Cerbos PDP’s [CheckResources](../api/index.html#check-resources) API with multiple actions. For example, an API response from a blog application might look like this:

```json
{
  "blog_post": {
    "title": "Why are we building Cerbos?",
    "author": "Emre Baran & Charith Ellawala",
    "permissions": {
      "edit": true,
      "delete": false
    }
  }
}
```

This pattern can be readily tailored to your requirements. It’s a great way to ensure that the front and back ends of your application agree on your policy rules.

## [](#%5Fcalling%5Fthe%5Fcerbos%5Fpdp%5Ffrom%5Fthe%5Fbrowser)Calling the Cerbos PDP from the browser

The Cerbos PDP API is available via REST, so you can perform permissions checks directly from the browser. The [@cerbos/http JavaScript SDK](https://www.npmjs.com/package/@cerbos/http) wraps the REST API to make it easier to integrate into your application.

| |  Exposing the PDP to the internet has security and performance implications. An attacker could use the API to probe your authorization policies much more easily than through your user interface. You could mitigate this to some extent by keeping the PDP behind a reverse proxy that authenticates and rate-limits API calls. You might also want to use a separate deployment with only a subset of your policies. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#%5Fevaluating%5Fpolicies%5Fin%5Fthe%5Fbrowser)Evaluating policies in the browser

You can use [Cerbos Hub’s embedded PDPs](https://docs.cerbos.dev/cerbos-hub/decision-points-embedded) to evaluate your authorization policies directly in the browser. This allows you to perform permission checks on the front end without changing the back end.

Install from binary
====================
Cerbos binaries are available for multiple operating systems and architectures. See the [releases page](https://github.com/cerbos/cerbos/releases/tag/v0.51.0) for all available downloads.

| OS    | Arch      | Bundle                                 |
| ----- | --------- | -------------------------------------- |
| Linux | x86-64    | cerbos\_0.51.0\_Linux\_x86\_64.tar.gz  |
| Linux | arm64     | cerbos\_0.51.0\_Linux\_arm64.tar.gz    |
| MacOS | universal | cerbos\_0.51.0\_Darwin\_all.tar.gz     |
| MacOS | x86-64    | cerbos\_0.51.0\_Darwin\_x86\_64.tar.gz |
| MacOS | arm64     | cerbos\_0.51.0\_Darwin\_arm64.tar.gz   |

You can download the binaries by running the following command. Substitute `<BUNDLE>` with the appropriate value from the above table.

```sh
curl -L -o cerbos.tar.gz "https://github.com/cerbos/cerbos/releases/download/v0.51.0/<BUNDLE>"
tar xvf cerbos.tar.gz
chmod +x cerbos
```

| |  Cerbos binaries are signed using [sigstore](https://www.sigstore.dev) tools during the automated build process and the verification bundle is published along with the binary as <BUNDLE>.sigstore.json. The following example demonstrates how to verify the Linux X86\_64 bundle archive. \# Download the bundle archive curl -L \\   \-o cerbos\_0.51.0\_Linux\_x86\_64.tar.gz \\   "https://github.com/cerbos/cerbos/releases/download/v0.51.0/cerbos\_0.51.0\_Linux\_x86\_64.tar.gz" \# Download the verification bundle curl -L \\   \-o cerbos\_0.51.0\_Linux\_x86\_64.tar.gz.sigstore.json \\   "https://github.com/cerbos/cerbos/releases/download/v0.51.0/cerbos\_0.51.0\_Linux\_x86\_64.tar.gz.sigstore.json" \# Verify the signature cosign verify-blob \\   \--certificate-oidc-issuer="https://token.actions.githubusercontent.com" \\   \--certificate-identity="https://github.com/cerbos/cerbos/.github/workflows/release.yaml@refs/tags/v0.51.0" \\   \--bundle="cerbos\_0.51.0\_Linux\_x86\_64.tar.gz.sigstore.json" \\   "cerbos\_0.51.0\_Linux\_x86\_64.tar.gz" |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#linux-packages)Linux packages

Cerbos DEB and RPM packages can be installed on any Linux distribution that supports one of those package formats. You can download the appropriate package for your system from the [releases page](https://github.com/cerbos/cerbos/releases/tag/v0.51.0).

| |  Cerbos packages are currently only designed to work with systems where systemd is the init system. If you use a different init system, consider installing cerbos from the tarballs instead. |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The packages install the `cerbos` and `cerbosctl` binaries to `/usr/local/bin` and create a systemd service to automatically start the Cerbos server. The default configuration is setup to look for policies in `/var/cerbos/policies` but you can change this by editing `/etc/cerbos/yaml` and reloading the service with `sudo systemctl restart cerbos`.

```sh
# Show status of the service
sudo systemctl status cerbos

# Restart the service
sudo systemctl restart cerbos

# View logs
sudo journalctl -xeu cerbos.service
```

## [](#homebrew)Homebrew

You can install Cerbos binaries using Homebrew as well.

```sh
brew tap cerbos/tap
brew install cerbos
```

## [](#npm)npm

You can install Cerbos binaries from the npm registry. This removes a separate setup step for JavaScript projects and allows you to lock Cerbos to a specific version to ensure a consistent development environment.

[cerbos](https://www.npmjs.com/package/cerbos) and [cerbosctl](https://www.npmjs.com/package/cerbosctl) are available as separate packages.

```sh
npm install --save-dev cerbos cerbosctl
```

Note that the npm packages rely on platform-specific optional dependencies, so make sure you don’t omit these when installing dependencies (for example, don’t pass the `--no-optional` flag to `npm`).

## [](#nix)Nix flake

A [Nix flake](https://nixos.wiki/wiki/Flakes) is available at <https://github.com/cerbos/cerbos-flake>.

```none
# Launch a Cerbos server
nix run github:cerbos/cerbos-flake#cerbos -- server --set=storage.disk.directory=/path/to/policy_directory

# Launch a REPL
nix run github:cerbos/cerbos-flake#cerbos -- repl

# Launch cerbosctl
nix run github:cerbos/cerbos-flake#cerbosctl

# Start a Nix shell session with cerbos and cerbosctl installed
nix shell github:cerbos/cerbos-flake
```

Run from container
====================
```sh
docker run --rm --name cerbos -p 3592:3592 ghcr.io/cerbos/cerbos:0.51.0
```

| |  Cerbos images can be verified using [sigstore](https://www.sigstore.dev) tools as follows: cosign verify \\   \--certificate-oidc-issuer="https://token.actions.githubusercontent.com" \\   \--certificate-identity="https://github.com/cerbos/cerbos/.github/workflows/release.yaml@refs/tags/v0.51.0" \\   ghcr.io/cerbos/cerbos:0.51.0 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

By default, the container is configured to listen on ports 3592 (HTTP) and 3593 (gRPC) and watch for policy files on the volume mounted at `/policies`. You can override these by creating a new [configuration file](../configuration/index.html).

Create a directory to hold the config file and policies.

```sh
mkdir -p cerbos-quickstart/policies
```

Create a config file.

```sh
cat > cerbos-quickstart/.cerbos.yaml <<EOF
server:
  httpListenAddr: ":3592"

storage:
  driver: "disk"
  disk:
    directory: /quickstart/policies
    watchForChanges: true
EOF
```

Launch the container with the new config file.

```sh
docker run --rm --name cerbos -d -v $(pwd)/cerbos-quickstart:/quickstart -p 3592:3592 ghcr.io/cerbos/cerbos:0.51.0 server --config=/quickstart/.cerbos.yaml
```

| |  Cerbos container images are mirrored to Docker Hub and the latest version is available at docker.io/cerbos/cerbos:0.51.0 as well. |
| ------------------------------------------------------------------------------------------------------------------------------------ |

Install from Helm chart
====================
Add the Cerbos Helm repository:

```sh
helm repo add cerbos https://download.cerbos.dev/helm-charts
helm repo update
```

You can view all the available configuration values for the chart by running the following command:

```sh
helm show values cerbos/cerbos --version=0.51.0
```

| |  Cerbos Helm chart is also available from an [OCI registry](https://helm.sh/docs/topics/registries/). HELM\_EXPERIMENTAL\_OCI=1 helm install cerbos oci://ghcr.io/cerbos/helm-charts/cerbos --version=0.51.0 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Securing Cerbos with TLS

Cerbos endpoints can be secured with TLS by providing a secret containing the certificate and its private key in the [cert-manager](https://cert-manager.io) format:

`tls.crt`

Certificate chain. Required.

`tls.key`

Private key. Required.

`ca.crt`

Trust chain. Optional.

During installation, provide the name of the Kubernetes secret containing the certificates by using the `cerbos.tlsSecretName` value.

```sh
helm install cerbos cerbos/cerbos --version=0.51.0 --set=cerbos.tlsSecretName=my-certificate-secret
```

If you require advanced features such as automatic certificate reloading, workload identities or mTLS, we recommend deploying a proxy server like [Envoy](https://www.envoyproxy.io), [Ghostunnel](https://github.com/ghostunnel/ghostunnel) or [Traefik](https://traefik.io) as a frontend to the Cerbos server. See the [Kubernetes sidecar](../deployment/k8s-sidecar.html) documentation for an example of deploying Cerbos as a sidecar to Ghostunnel.

## [](#%5Fcustomizing%5Fthe%5Fmanifests)Customizing the manifests

For the sake of simplicity, the Cerbos Helm chart only exposes settings that are most likely to be changed in a typical deployment scenario. If you want to customize the manifests further, use the post-renderer functionality in Helm to patch the generated manifests before they are applied.

For example, if you want to set `loadBalancerSourceRanges` of the service generated by the Cerbos Helm chart, you can use Kustomize to patch the service as follows:

Create a file named `kustomization.yaml` with the patches you want to apply:

```yaml
---
resources:
  - base.yaml
patches:
  - patch: |-
      - op: add
        path: /spec/loadBalancerSourceRanges
        values: ["10.0.0.0/16"]
    target:
      version: v1
      kind: Service
```

Create a file named `kustomize.sh` with the following contents and make it executable:

```sh
#!/usr/bin/env bash

cat > base.yaml
exec kubectl kustomize
```

Test that the patch works as expected:

```sh
helm template cerbos/cerbos --post-renderer ./kustomize.sh
```

Now you can install Cerbos with your patches:

```sh
helm install cerbos cerbos/cerbos --version=0.51.0 --post-renderer=./kustomize.sh
```

## [](#%5Fdeploy%5Fcerbos%5Fconfigured%5Fto%5Fread%5Fpolicies%5Ffrom%5Fa%5Fgithub%5Frepository)Deploy Cerbos configured to read policies from a GitHub repository

* Follow the instructions at <https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token> to create a personal access token (PAT) with `repo` permissions.
* Create a new Kubernetes secret to hold the PAT  
```sh  
PAT=YOUR_GITHUB_PAT kubectl create secret generic cerbos-github-token --from-literal=GITHUB_TOKEN=$PAT  
```
* Create a new values file named `git-values.yaml` with the following contents:  
```yaml  
envFrom:  
  - secretRef:  
      name: cerbos-github-token (1)  
cerbos:  
  config:  
    # Configure the git storage driver  
    storage:  
      driver: "git"  
      git:  
        protocol: https  
        # Replace with the URL of your GitHub repo.  
        url: https://github.com/cerbos/sample-policies.git  
        # Replace with the branch name of your repo.  
        branch: main  
        # Remove or leave empty if the policies are not stored in a subdirectory.  
        subDir: hr  
        # Path to checkout. By default, /work is a Kubernetes emptyDir volume that is only available for the lifetime of the pod.  
        # If you want the work directory to persist between pod restarts, specify the mount path of a persistent volume here.  
        checkoutDir: /work  
        # How often the remote repo should be checked for updates.  
        updatePollInterval: 60s  
        # Credentials used to login to the remote GitHub repo. We are using an environment variable mounted from the secret we created earlier.  
        https:  
          username: "cerbos" (2)  
          password: "${GITHUB_TOKEN}" (3)  
```  
| **1** | Create an environment variable from the secret we created                          |  
| ----- | ---------------------------------------------------------------------------------- |  
| **2** | Username should be set to a string value (can be any value if using GitHub)        |  
| **3** | Use the environment variable containing the PAT as the password to login to GitHub |
* Deploy Cerbos using the Helm chart  
```sh  
helm install cerbos cerbos/cerbos --version=0.51.0 --values=git-values.yaml  
```

## [](#%5Fdeploy%5Fcerbos%5Fconfigured%5Fto%5Fread%5Fpolicies%5Ffrom%5Fa%5Fmounted%5Fvolume)Deploy Cerbos configured to read policies from a mounted volume

Here we demonstrate how to use a `hostPath` volume to feed policies to a Cerbos deployment. You can easily substitute the `hostPath` volume type with any other type of volumes supported by Kubernetes. See <https://kubernetes.io/docs/concepts/storage/volumes/>.

* Create a new values file named `pv-values.yaml` with the following contents:  
```yaml  
volumes: (1)  
  - name: cerbos-policies  
    hostPath:  
      path: /data/cerbos-policies  
volumeMounts: (2)  
  - name: cerbos-policies  
    mountPath: /policies  
    readOnly: true  
cerbos:  
  config:  
    storage:  
      driver: "disk"  
      disk:  
        directory: /policies (3)  
        watchForChanges: true  
```  
| **1** | Define a hostPath volume type                                          |  
| ----- | ---------------------------------------------------------------------- |  
| **2** | Mount the volume to the container at the path /policies                |  
| **3** | Configure Cerbos to read policies from the mounted /policies directory |
* Deploy Cerbos using the Helm chart  
```sh  
helm install cerbos cerbos/cerbos --version=0.51.0 --values=pv-values.yaml  
```

## [](#%5Fdeploy%5Fa%5Fpdp%5Fconnected%5Fto%5Fcerbos%5Fhub)Deploy a PDP connected to Cerbos Hub

| |  Requires a [Cerbos Hub](https://www.cerbos.dev/product-cerbos-hub) account. [![Try Cerbos Hub](../_images/try_cerbos_hub.png)](https://hub.cerbos.cloud) |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- |

* Create a new Kubernetes secret to hold the Cerbos Hub credentials  
```sh  
kubectl create secret generic cerbos-hub-credentials \  
   --from-literal=CERBOS_HUB_CLIENT_ID=YOUR_CLIENT_ID \ (1)  
   --from-literal=CERBOS_HUB_CLIENT_SECRET=YOUR_CLIENT_SECRET \ (2)  
   --from-literal=CERBOS_HUB_DEPLOYMENT_ID=CERBOS_HUB_DEPLOYMENT_ID (3)  
```  
| **1** | Client ID from the Cerbos Hub credential                         |  
| ----- | ---------------------------------------------------------------- |  
| **2** | Client secret from the Cerbos Hub credential                     |  
| **3** | Cerbos Hub [Deployment ID](../../../cerbos-hub/deployments.html) |
* Create a new values file named `hub-values.yaml` with the following contents:  
```yaml  
cerbos:  
  config:  
    # Configure the Hub audit backend  
    audit:  
      enabled: true (1)  
      backend: "hub"  
      hub:  
        storagePath: /audit_logs  
# Create environment variables from the secret.  
envFrom:  
  - secretRef:  
      name: cerbos-hub-credentials  
# Mount volume for locally buffering the audit logs. A persistent volume is recommended for production use cases.  
volumes:  
  - name: cerbos-audit-logs  
    emptyDir: {}  
volumeMounts:  
  - name: cerbos-audit-logs  
    mountPath: /audit_logs  
```  
| **1** | Enables audit log collection. See [Hub audit log collection documentation](../../../cerbos-hub/audit-log-collection.html) for information about masking sensitive fields and other advanced settings. |  
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
* Deploy Cerbos using the Helm chart  
```sh  
helm install cerbos cerbos/cerbos --version=0.51.0 --values=hub-values.yaml  
```

Tutorial
====================
## [](#%5Fcerbforce)Cerbforce

'Cerbforce' is the new killer CRM system that is taking the world by storm. It began as a small SaaS app that has grown into an enterprise-scale, multi-tenant, global powerhouse.

It is now at the point where the existing basic permission model created at the start of development is no longer fit for purpose and [Cerbos](https://cerbos.dev/) has been selected as the system to implement.

This tutorial walks through the decision-making process for implementing [Cerbos](https://cerbos.dev/). It covers setting up, defining the various resources and policies for the different objects and users in the system, and evolve them to make use of all of Cerbos' features.

Running locally
====================
As the developers of Cerbforce began their investigation of the system, the first step was getting a Cerbos instance up and running locally.

## [](#%5Fcontainer)Container

If you have Docker, you can simply use the published images. The container already ships with a default configuration that has a `disk` driver configured to look for policies mounted at `/policies`. Create an empty policy folder at `policies/`, and then run the following:

```sh
docker run --rm --name cerbos -t \
  -v $(pwd)/policies:/policies \
  -p 3592:3592 \
  ghcr.io/cerbos/cerbos:latest server
```

## [](#%5Fbinary)Binary

Alternatively, if you don’t have Docker running, you can opt to use the release binary directly which you can download from [here](../installation/binary.html).

### [](#%5Fconfig%5Ffile)Config file

In order to run the binary, you’ll need to create a minimal server configuration file. The simplest configuration to get up and running (using a local folder for storage of policies) requires only the port and location to be set:

```yaml
---
server:
  httpListenAddr: ":3592"
storage:
  driver: "disk"
  disk:
    directory: policies
```

| |  You can find the full configuration schema in the [Cerbos docs](../configuration/index.html). |
| ------------------------------------------------------------------------------------------------ |

Save this configuration to a file named `.cerbos.yaml`. You’ll also need to create an empty policy folder `policies/`.

Now, extract the binary and run:

```sh
./cerbos server --config=.cerbos.yaml
```

Once started you can open `<http://localhost:3592>` to see the API documentation.

Resource definition
====================
| |  The policies for this section can be found [on GitHub](https://github.com/cerbos/cerbos/tree/main/docs/modules/ROOT/examples/tutorial/03-resource-definition/cerbos). |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#%5Fauthentication%5Froles)Authentication roles

To begin with Cerbos needs to know about the basic roles which are provided by your authentication provider. In the case of Cerbforce, [Auth0](https://cerbos.dev/ecosystem/cerbos-auth0) provides a role of either `ADMIN` or `USER` for all profiles. This is important when starting to define access to resources below - for now just make a note of them.

## [](#%5Fresources)Resources

The best place to start with defining [policies](../policies/index.html) is listing out all the resources and their actions that exist in the system. A resource is an entity type that users are authorized to access.

In the case of Cerbforce some of the resources and actions are as follows:

| Resource | Actions                      |
| -------- | ---------------------------- |
| User     | Create, Read, Update, Delete |
| Company  | Create, Read, Update, Delete |
| Contact  | Create, Read, Update, Delete |

With this as a start, you can begin creating your first Cerbos policy - a [resource policy](../policies/resource%5Fpolicies.html).

## [](#%5Fresource%5Fpolicies)Resource policies

Taking the user resource as an example, the most basic resource policy can be defined like below:

```yaml
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: "default"
  resource: "user"
  rules:
    - actions:
        - create
        - read
      effect: EFFECT_ALLOW
      roles:
        - user

    - actions:
        - create
        - read
        - update
        - delete
      effect: EFFECT_ALLOW
      roles:
        - admin
```

The structure of a resource policy requires a name to be set on the `resource` key and then a list of rules is defined. A rule defines a list of actions on the resource, the effect of the rule (`EFFECT_ALLOW` or `EFFECT_DENY`) and then fields to state who this applies to - in this simple case a list of `roles` which is checked for in the roles of the user making the request.

In this case, a request made for a principal with a role of `user` is granted only `create` and `read` actions whilst an `admin` role can also perform `update`, `delete` actions.

The full documentation for resource policies can be found [here](../policies/resource%5Fpolicies.html).

## [](#%5Fwildcard%5Faction)Wildcard action

To simplify things further, admins might need to be able to do every action. We can use a special `*` wildcard action to specify this succinctly:

```yaml
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: "default"
  resource: "user"
  rules:
    - actions:
        - create
        - read
        - update
      effect: EFFECT_ALLOW
      roles:
        - user

    - actions:
        - "*"
      effect: EFFECT_ALLOW
      roles:
        - admin
```

The `contact` and `company` resources have a similar structure at this stage and can be modeled as so:

```yaml
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: "default"
  resource: "contact"
  rules:
    - actions:
        - create
        - read
        - update
      effect: EFFECT_ALLOW
      roles:
        - user

    - actions:
        - "*"
      effect: EFFECT_ALLOW
      roles:
        - admin
```

```yaml
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: "default"
  resource: "company"
  rules:
    - actions:
        - create
        - read
        - update
      effect: EFFECT_ALLOW
      roles:
        - user

    - actions:
        - "*"
      effect: EFFECT_ALLOW
      roles:
        - admin
```

## [](#%5Fvalidating%5Fpolicies)Validating policies

Now with the initial policies in place, you can run Cerbos in compile mode which validates the content of the policy files to ensure they are correct.

If you are running Cerbos in a container then mount the folder containing your policies and run the `compile` command pointing to the folder of your policies.

```sh
# Using Container
docker run --rm --name cerbos -t \
  -v /tutorial:/tutorial \
  ghcr.io/cerbos/cerbos:latest compile /tutorial/policies

# Using Binary
./cerbos compile /tutorial/policies
```

If the policies are valid then the process exits with no errors. If there is an issue, the error message points you to where you need to look and the specific problem to fix.

## [](#%5Fconclusion)Conclusion

At this stage, a simple Roles-based Access Control (RBAC) model has been designed and the policies have been validated - next up is making an authorization call to Cerbos.

Calling Cerbos
====================
| |  The policies for this section can be found [on GitHub](https://github.com/cerbos/cerbos/tree/main/docs/modules/ROOT/examples/tutorial/04-calling-cerbos/cerbos). |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Now that you know the policies are valid, it is time to make your first call to Cerbos to make an authorization check.

## [](#%5Fstarting%5Fcerbos)Starting Cerbos

To start you need to launch the server:

```sh
# Using Container
docker run --rm --name cerbos -t \
  -v /tutorial:/tutorial \
  -p 3592:3592 ghcr.io/cerbos/cerbos:latest server --config=/tutorial/.cerbos.yaml

# Using Binary
./cerbos server --config=/tutorial/.cerbos.yaml
```

Once Cerbos has started up you should see an output confirming that there are 3 policies loaded and ready to start processing authorization checks:

```sh
2024-12-28T13:55:57.043+0600    INFO    cerbos.server   maxprocs: Leaving GOMAXPROCS=8: CPU quota undefined
2024-12-28T13:55:57.044+0600    INFO    cerbos.server   Loading configuration from .cerbos.yaml
2024-12-28T13:55:57.045+0600    WARN    cerbos.otel     Disabling OTLP traces because neither OTEL_EXPORTER_OTLP_ENDPOINT nor OTEL_EXPORTER_OTLP_TRACES_ENDPOINT is defined
2024-12-28T13:55:57.046+0600    INFO    cerbos.disk.store       Initializing disk store from /Users/username/tutorial/policies
2024-12-28T13:55:57.048+0600    INFO    cerbos.index    Found 3 executable policies
2024-12-28T13:55:57.048+0600    INFO    cerbos.telemetry        Telemetry disabled
2024-12-28T13:55:57.048+0600    INFO    cerbos.grpc     Starting gRPC server at :3593
2024-12-28T13:55:57.050+0600    INFO    cerbos.http     Starting HTTP server at :3592
```

At this point how you make a request to the Cerbos instance is down to your preference - a simple cURL command or using a GUI such as Postman also works.

## [](#%5Fcerbos%5Fcheck%5Fcall)Cerbos check call

A call to Cerbos contains 3 key bits of information:

1. The Principal - who is making the request
2. The Resources - a map of entities of a resource kind that are they requesting access too
3. The Actions - what actions are they trying to perform on the entities

The request payload to the `/api/check/resources` endpoint takes these 3 bits of information as JSON:

```json
{
  "principal": {
    "id": "user_1",     // the user ID
    "roles": ["user"],  // list of roles from user's profile
    "attr": {}          // a map of attributes about the user - not used yet
  },
  "resources": [        // an array of resources being accessed
    {
      "actions": ["read"],  // the list of actions to be performed on the resource
      "resource": {         // details about the resource
        "kind": "contact",  // the type of the resource
        "id": "contact_1",  // the ID of the specific resource instance
        "attr": {}          // a map of attributes about the resource - not used yet
      }
    }
  ]
}
```

To make the actual call as a cURL with the default server config:

```sh
curl --location --request POST 'http://localhost:3592/api/check/resources' \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "principal": {
        "id": "user_1",
        "roles": ["user"],
        "attr": {}
      },
      "resources": [
          {
              "actions": ["read"],
              "resource": {
                  "kind": "contact",
                  "id": "contact_1",
                  "attr": {}
              }
          }
      ]
    }'
```

The response object looks as follows where for each instance of the resource the authorization decision for each action is either `EFFECT_ALLOW` or `EFFECT_DENY` depending on the policies:

```json
{
    "results": [
        {
            "resource": {
                "id": "contact_1",
                "kind": "contact"
            },
            "actions": {
                "read": "EFFECT_ALLOW"
            }
        }
    ],
    "cerbosCallId": "49KQ6456PRBLWYMXYDBKZM1F6H"
}
```

You can find the Swagger definition of the Cerbos API via going to the root of the Cerbos instance - for example <http://localhost:3592> if running on the default port.

## [](#%5Fconclusion)Conclusion

Now that you have made the first call to Cerbos you can move on to a way of checking policy logic without having to make individual calls each time by writing unit tests.

Testing policies
====================
| |  The policies for this section can be found [on GitHub](https://github.com/cerbos/cerbos/tree/main/docs/modules/ROOT/examples/tutorial/05-testing-policies/cerbos). |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Cerbos allows you to write [tests for policies](../policies/compile.html) and run them as part of the compilation stage to make sure that the policies do exactly what you expect. This saves the manual effort of running example requests over and over to ensure the policy logic is as you expect.

A test suite defines a number of resources and principals and the expected result of actions for any combination of them.

To define a test suite, create a `tests` folder inside your policy folder. In this folder, any number of tests can be defined as YAML but the file must end with `_test`.

As an example, the `contact` policy states that a `user` can create, read and update a contact, but only an `admin` can delete them - therefore you can create a test suite for this like the below:

```yaml
---
name: ContactTestSuite
description: Tests for verifying the contact resource policy

principals:
  admin:
    id: admin
    roles:
      - admin

  user:
    id: user
    roles:
      - user

resources:
  contact:
    kind: contact
    id: contact

tests:
  - name: Contact CRUD Actions
    input:
      principals:
        - admin
        - user

      resources:
        - contact

      actions:
        - create
        - read
        - update
        - delete

    expected:
      - principal: admin
        resource: contact
        actions:
          create: EFFECT_ALLOW
          read: EFFECT_ALLOW
          update: EFFECT_ALLOW
          delete: EFFECT_ALLOW

      - principal: user
        resource: contact
        actions:
          create: EFFECT_ALLOW
          read: EFFECT_ALLOW
          update: EFFECT_ALLOW
          delete: EFFECT_DENY
```

With this defined, you can now extend the compile command to also run the tests for example:

```sh
# Using Container
docker run --rm --name cerbos -t \
  -v /tutorial:/tutorial \
  -p 3592:3592 \
  ghcr.io/cerbos/cerbos:latest compile /tutorial/policies

# Using Binary
./cerbos compile /tutorial/policies
```

If everything is as expected the output of the tests should be green:

```none
Test results
= ContactTestSuite (contact_test.yaml)
== 'Contact CRUD Actions' for resource 'contact_test' by principal 'user' [OK]
== 'Contact CRUD Actions' for resource 'contact_test' by principal 'admin' [OK]
```

Full testing documentation can be found [here](../policies/compile.html).

Adding conditions
====================
| |  The policies for this section can be found [on GitHub](https://github.com/cerbos/cerbos/tree/main/docs/modules/ROOT/examples/tutorial/06-adding-conditions/cerbos). |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

In the previous section, an RBAC policy was created that allowed anyone with a `user` role to update a user resource - this isn’t what is intended as it would allow users to update other users' profiles.

```yaml
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: "default"
  resource: "user"
  rules:
    - actions:
        - create
        - read
        - update
      effect: EFFECT_ALLOW
      roles:
        - user
# ....other conditions
```

This blanket approach is where using pure role-based access controls falls down as there is more nuanced required to meet the requirements.

## [](#%5Fconditions)Conditions

Cerbos is a powerful Attribute-based Access Control system that can make contextual decisions at request time whether an action can be taken.

In this scenario, Cerbforce’s business logic states that a user can only update their own user profile. To implement this a check needs to be made to ensure the ID of the user making the request matches the ID of the user resource being updated.

[Conditions](../policies/conditions.html) in Cerbos are written in [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md) which is a simple way of defining boolean logic of conditions. In this environment, there are two main bits of data provided that are of interest `request.principal` which is the information about the user making the request and `request.resource` which is the information about the resource being accessed.

The data model for each of these is as follows:

```json
// request.principal
{
  "id": "somePrinicpalId", // the prinicpal ID
  "roles": ["user"], // the list of roles from the auth provider
  "attr": {
    // a map of attributes about the prinicpal
  }
}

// request.resource
{
  "id": "someResourceId", // the resource ID
  "attr": {
    // a map of attributes about the resourece
  }
}
```

Using this information a check to see if the principal ID is the same as the ID of the user resource being accessed can be defined as

```none
request.resource.id == request.principal.id
```

Adding this to the policy request a new rule to be created that is just for the `update` and `delete` actions which are for the `user` role and has a single condition.

```json
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: "default"
  resource: "user"
  rules:
    - actions:
        - create
        - read
      effect: EFFECT_ALLOW
      roles:
        - user

    - actions:
        - update
        - delete
      effect: EFFECT_ALLOW
      roles:
        - user
      condition:
        match:
          expr: request.resource.id == request.principal.id

# ....other conditions
```

Complex logic can be defined in conditions (or sets of conditions) which you can read more about in [the docs](https://docs.cerbos.dev/cerbos/latest/policies/conditions.html).

## [](#%5Fextending%5Ftests)Extending tests

Now that you have a conditional policy, you can add these as test cases in the user tests. You can now define multiple `user` resources and principals and create test cases for ensuring the `update` action is allowed when the ID of the principal matches the ID of the resource, as well as checking that it isn’t allowed if the condition is not met.

```yaml
---
name: UserTestSuite
description: Tests for verifying the user resource policy

principals:
  admin:
    id: admin
    roles:
      - admin

  user1:
    id: user1
    roles:
      - user

  user2:
    id: user2
    roles:
      - user

resources:
  admin:
    kind: user
    id: admin

  user1:
    kind: user
    id: user1

  user2:
    kind: user
    id: user2

tests:
  - name: User CRUD Actions
    input:
      principals:
        - admin
        - user1
        - user2

      resources:
        - admin
        - user1
        - user2

      actions:
        - create
        - read
        - update
        - delete

    expected:
      - principal: admin
        resource: admin
        actions:
          create: EFFECT_ALLOW
          read: EFFECT_ALLOW
          update: EFFECT_ALLOW
          delete: EFFECT_ALLOW

      - principal: admin
        resource: user1
        actions:
          create: EFFECT_ALLOW
          read: EFFECT_ALLOW
          update: EFFECT_ALLOW
          delete: EFFECT_ALLOW

      - principal: admin
        resource: user2
        actions:
          create: EFFECT_ALLOW
          read: EFFECT_ALLOW
          update: EFFECT_ALLOW
          delete: EFFECT_ALLOW

      - principal: user1
        resource: admin
        actions:
          create: EFFECT_ALLOW
          read: EFFECT_ALLOW
          update: EFFECT_DENY
          delete: EFFECT_DENY

      - principal: user1
        resource: user1
        actions:
          create: EFFECT_ALLOW
          read: EFFECT_ALLOW
          update: EFFECT_ALLOW
          delete: EFFECT_ALLOW

      - principal: user1
        resource: user2
        actions:
          create: EFFECT_ALLOW
          read: EFFECT_ALLOW
          update: EFFECT_DENY
          delete: EFFECT_DENY

      - principal: user2
        resource: admin
        actions:
          create: EFFECT_ALLOW
          read: EFFECT_ALLOW
          update: EFFECT_DENY
          delete: EFFECT_DENY

      - principal: user2
        resource: user1
        actions:
          create: EFFECT_ALLOW
          read: EFFECT_ALLOW
          update: EFFECT_DENY
          delete: EFFECT_DENY

      - principal: user2
        resource: user2
        actions:
          create: EFFECT_ALLOW
          read: EFFECT_ALLOW
          update: EFFECT_ALLOW
          delete: EFFECT_ALLOW
```

Derived roles
====================
| |  The policies for this section can be found [on GitHub](https://github.com/cerbos/cerbos/tree/main/docs/modules/ROOT/examples/tutorial/07-derived-roles/cerbos). |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

The business requirements for Cerbforce state that only an owner of Contacts and Companies are allowed to delete them from the system. With Cerbos, the aim is to keep policies as simple as possible and not repeat logic across different resources, so in this situation, a [Derived Role](../policies/derived%5Froles.html) can enable help.

Derived roles are a way of augmenting the broad roles with are attached to the user in the directory of the authentication system with contextual data to provide more fine-grained control at runtime. On every request, all the relevant derived role policies are evaluated and those matching roles are 'attached' to the user as Cerbos computes access.

## [](#%5Fowner%5Fderived%5Frole)Owner derived role

In the Cerbforce data model, the `contact` and `company` both have an attribute called `ownerId` which is the ID of the user that created the record. Rather than adding a condition to both of these resource policies, you are going to create a derived role that gives the principal an additional `owner` role within the context of the request. The policy for this is as follows:

```yaml
---
apiVersion: "api.cerbos.dev/v1"
description: |-
  Common dynamic roles used within the Cerbforce app
derivedRoles:
  name: cerbforce_derived_roles
  definitions:
    - name: owner
      parentRoles: ["user"]
      condition:
        match:
          expr: request.resource.attr.ownerId == request.principal.id
```

The structure is similar to a resource policy but rather than defining actions with conditions, it defines roles that are an extension of the listed `parentRoles` and can have any number of conditions as with resources.

With this derived role policy setup a resource can import them and then make use of them in rules eg:

```yaml
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: "default"
  resource: "contact"
  importDerivedRoles:
    - cerbforce_derived_roles
  rules:
    - actions:
        - create
        - read
      effect: EFFECT_ALLOW
      roles:
        - user

    - actions:
        - update
        - delete
      effect: EFFECT_ALLOW
      derivedRoles:
        - owner

    - actions:
        - "*"
      effect: EFFECT_ALLOW
      roles:
        - admin
```

Full documentation can be found [here](../policies/derived%5Froles.html).

Principal policies
====================
| |  The policies for this section can be found [on GitHub](https://github.com/cerbos/cerbos/tree/main/docs/modules/ROOT/examples/tutorial/08-principal-policies/cerbos). |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The final type of policy that Cerbos supports is a [principal policy](../policies/principal%5Fpolicies.html) which is a special type that allows user-specific overrides to be defined.

In the case of Cerbforce there is a Data Protection Officer (DPO) that handles any data deletion requests. By default, they would not have any delete access to contacts unless they were the owner of the record or have the `admin` role. To overcome this a principal policy has been created which targets their userId and overrides this for the delete action on a contact resource:

```yaml
---
apiVersion: "api.cerbos.dev/v1"
principalPolicy:
  version: "default"
  principal: "dpo1"
  rules:
    - resource: contact
      actions:
        - name: contact_delete
          action: "delete"
          effect: EFFECT_ALLOW
```

With this policy in place, when an authorization check is made with the principal ID of `dpo1` the delete action on a `contact` resource is overridden to be allowed.

Full documentation can be found [here](../policies/principal%5Fpolicies.html).

Attribute schema
====================
| |  The policies for this section can be found [on GitHub](https://github.com/cerbos/cerbos/tree/main/docs/modules/ROOT/examples/tutorial/09-attribute-schema/cerbos). |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

An additional check bit of business logic has been introduced for the `contact` resource which requires the `active` attribute of a contact to be set to `True` to be able to `update` or `delete` it. This is so that old contacts are kept for reporting purposes and can’t be accidentally deleted or updated.

This now means there are two attributes of a `contact` resource that are now required for the policies to be computed - `ownerId` and `active`. If either of these is not included in the request to check permissions the result would not be as expected (defaulting to `EFFECT_DENY`).

To prevent this mistake, it is possible to define a [schema](../policies/schemas.html) for the attributes of a principal and resources which Cerbos validates against at request time to ensure all fields are provided as expected.

## [](#%5Fdefining%5Fschema)Defining schema

[Attribute schema](../policies/schemas.html) are defined in [JSON Schema (draft 2020-12)](https://json-schema.org/specification.html) and stored in a special `_schemas` sub-directory along side the policies

For the contact resource the schema looks like the following:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "ownerId": { "type": "string" },
    "active": { "type": "boolean" }
  },
  "required": ["ownerId", "active"]
}
```

Once defined, it is then linked to the resource via adding a reference in the policy:

```yaml
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: "default"
  resource: "contact"
  importDerivedRoles:
    - cerbforce_derived_roles
  rules:
    - actions:
        - create
        - read
      effect: EFFECT_ALLOW
      roles:
        - user

    - actions:
        - update
        - delete
      effect: EFFECT_ALLOW
      derivedRoles:
        - owner
      condition:
        match:
          expr: request.resource.attr.active == true

    - actions:
        - "*"
      effect: EFFECT_ALLOW
      roles:
        - admin
  schemas:
    resourceSchema:
      ref: cerbos:///contact.json
```

The same can be done with attributes of a principal - you can find out more in [the documentation](../policies/schemas.html).

## [](#%5Fenforcing%5Fschema)Enforcing schema

Validating the request against the schema is done at request time by the server - to enable this a [new schema configuration block](../configuration/schema.html) needs adding to the `.cerbos.yaml`.

```yaml
schema:
  enforcement: reject
```

With this now in place, any request that is made to check authorization of a `contact` resource is rejected if the attributes are not provided or of the wrong type:

_Request_

```json
{
  "principal": {
    "id": "user_1",
    "roles": ["user"],
    "attr": {}
  },
  "resource": {
    "kind": "contact",
    "instances": {
      "contact_1": {
        "attr": {
          "ownerId": "user1"
        }
      }
    }
  },
  "actions": ["read"]
}
```

_Response_

```json
{
  "resourceInstances": {
    "contact_1": {
      "actions": {
        "read": "EFFECT_DENY"
      },
      "validationErrors": [
        {
          "message": "missing properties: 'active'",
          "source": "SOURCE_RESOURCE"
        }
      ]
    }
  }
}
```

Integrating Cerbos
====================
With the policies now defined the authorization logic inside the app can be replaced with a call out to a running Cerbos instance.

Cerbos has SDKs available for Go, Java, .NET, Node, PHP, Python, Ruby, and Rust. Documentation for these and other examples can be found [here](../api/index.html).

Tutorial: Writing policies for a simple photo-sharing service
====================
Getting started

* We will use Docker to run the server and the compiler.

```shell
docker pull ghcr.io/cerbos/cerbos:0.51.0
```

* Create a file named `.cerbos.yaml` with the following contents:

```yaml
---
server:
  httpListenAddr: ":3592"

storage:
  driver: "disk"
  disk:
    directory: /photo-share/policies
```

* Create a directory named `policies` to hold the policies.

| |  You can find all the policies and tests used in this tutorial at <https://github.com/cerbos/photo-share-tutorial>. |
| --------------------------------------------------------------------------------------------------------------------- |

## [](#%5Fthe%5Fapatr%5Fapplication)The Apatr application

Apatr is a simple photo-sharing service that allows users to upload their photos and optionally share them with the rest of the world. Users sign-up to the service either by creating their own user account on the website or by signing-in with an identity provider (IDP) like Google or Facebook. Apatr uses a third-party identity management tool to manage these accounts and authenticating users to the site. Once they are logged-in, users can do the following:

* Create albums to organize their photos
* Upload photos to albums
* Share albums or individual photos with other Apatr users
* Share albums or individual photos with the internet

Apatr also employs a team of moderators to investigate complaints and remove any illegal or offensive items from the site. To respect users privacy, moderators are only allowed to view photos or albums that are public or those that have been flagged as inappropriate by another user.

Apatr’s identity provider allows defining roles for users. The roles currently defined in this system are:

* `moderator`: Member of the moderator team
* `user`: Authenticated users

## [](#%5Fresources%5Fand%5Factions)Resources and actions

In the Apatr application, the most obvious resource hierarchy is the following:

* Album  
   * Photo  
         * Caption  
         * Comment  
   * Description
* User Profile

__Album permissions matrix__
| Resource         | Action                                                          | Allowed role                                  | Condition |
| ---------------- | --------------------------------------------------------------- | --------------------------------------------- | --------- |
| **album:object** | create                                                          | user                                          |           |
| delete           | user                                                            | If user owns the album                        |           |
| moderator        | If the album is flagged as inappropriate                        |                                               |           |
| share            | user                                                            | If user owns the album                        |           |
| unshare          | user                                                            | If user owns the album                        |           |
| view             | user                                                            | If user owns the album If the album is public |           |
| moderator        | If the album is flagged as inappropriate If the album is public |                                               |           |
| flag             | user                                                            | If the album is public                        |           |

## [](#%5Fderived%5Froles)Derived roles

There are some recurring themes in the above permissions matrix.

* People who have the `user` role can be either owners or viewers depending on the resource they are trying to access
* Moderators get extra capabilities when the content is flagged as inappropriate

These capabilities are determined based on contextual information. Let’s codify them so that they can be reused.

```yaml
---
apiVersion: "api.cerbos.dev/v1"
description: |-
  Common dynamic roles used within the Apatr app
derivedRoles:
  name: apatr_common_roles (1)
  definitions:
    - name: owner (2)
      parentRoles: ["user"] (3)
      condition:
        match:
          expr: request.resource.attr.owner == request.principal.id (4)

    - name: abuse_moderator
      parentRoles: ["moderator"]
      condition:
        match:
          expr: request.resource.attr.flagged == true
```

| **1** | Name that we will use to import this set of roles                                          |
| ----- | ------------------------------------------------------------------------------------------ |
| **2** | Descriptive name for this derived role                                                     |
| **3** | The static roles (from the identity provider) to which this derived role applies to        |
| **4** | An expression that is applied to the request to determine when this role becomes activated |

Save the above definition as `apatr_common_roles.yaml` in the `policies` directory.

Run the compiler to make sure that the contents of the file are valid.

```shell
docker run -it -v $(pwd):/photo-share ghcr.io/cerbos/cerbos:0.51.0 \
    compile /photo-share/policies
```

## [](#%5Fresource%5Fpolicies)Resource policies

Let’s write a resource policy for the `album:object` resource.

```yaml
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: "default" (1)
  importDerivedRoles:
    - apatr_common_roles (2)
  resource: "album:object"
  rules:
    - actions: ['*']
      effect: EFFECT_ALLOW
      derivedRoles:
        - owner

    - actions: ['view', 'flag']
      effect: EFFECT_ALLOW
      roles:
        - user
      condition:
        match:
          expr: request.resource.attr.public == true

    - actions: ['view', 'delete']
      effect: EFFECT_ALLOW
      derivedRoles:
        - abuse_moderator
```

| **1** | You can have multiple policy versions for the same resource (e.g. production vs. staging). If the request does not explicitly specify the version, the default policy takes effect. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Import the roles we defined earlier                                                                                                                                                 |

Save the above policy definition as `resource_album_object.yaml` inside the `policies` directory.

Run the compiler to make sure that the contents of the policies directory are valid.

```shell
docker run -it -v $(pwd):/photo-share ghcr.io/cerbos/cerbos:0.51.0 compile /photo-share/policies
```

Let’s start the server and try out a request.

```shell
docker run -it -v $(pwd):/photo-share -p 3592:3592 ghcr.io/cerbos/cerbos:0.51.0 \
    server --config=/photo-share/.cerbos.yaml
```

| |  If you like to use [Postman](https://www.postman.com), [Insomnia](https://insomnia.rest) or any other software that supports OpenAPI, the Cerbos OpenAPI definitions can be downloaded by accessing <http://localhost:3592/schema/swagger.json>. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Alicia trying to view her own album

```shell
cat <<EOF | curl --silent "http://localhost:3592/api/check/resources?pretty" -d @-
{
  "requestId": "test01",
  "includeMeta": true,
  "principal": {
    "id": "alicia",
    "policyVersion": "default",
    "roles": [
      "user"
    ]
  },
  "resources": [
    {
      "actions": [
        "view"
      ],
      "resource": {
        "id": "XX125",
        "policyVersion": "default",
        "kind": "album:object",
        "attr": {
          "owner": "alicia",
          "public": false,
          "flagged": false
        }
      }
    }
  ]
}
EOF
```

{
  "requestId": "test01",
  "results": [
    {
      "resource": {
        "id": "XX125",
        "kind": "album:object",
        "policyVersion": "default"
      },
      "actions": {
        "view": "EFFECT_ALLOW"
      },
      "meta": {
        "actions": {
          "view": {
            "matchedPolicy": "resource.album_object.vdefault"
          }
        },
        "effectiveDerivedRoles": [
          "owner"
        ]
      }
    }
  ]
}

## [](#%5Fwriting%5Ftests%5Fto%5Fverify%5Fbehaviour)Writing tests to verify behaviour

It’s not practical to start the server and manually make requests every time a policy is updated. So let’s write some tests instead.

Create a new directory named `tests` and create a file named `album_object_test.yaml` with the following contents.

```yaml
---
name: AlbumObjectTestSuite
description: Tests for verifying the album:object resource policy
resources:
  alicia_private_album:
    id: "XX125"
    kind: "album:object"
    attr:
      owner: "alicia"
      public: false
      flagged: false

  alicia_public_album:
    id: "XX525"
    kind: "album:object"
    attr:
      owner: "alicia"
      public: true
      flagged: false

  alicia_flagged_album:
    id: "XX666"
    kind: "album:object"
    attr:
      owner: "alicia"
      public: true
      flagged: true

principals:
  alicia:
    id: "alicia"
    roles: ["user"]

  bradley:
    id: "bradley"
    roles: ["user"]

  maria:
    id: "maria"
    roles: ["moderator", "user"]

tests:
  - name: View album
    input: &testInput
      principals:
        - alicia
        - bradley
        - maria
      actions:
        - view
      resources:
        - alicia_private_album
        - alicia_public_album
        - alicia_flagged_album
    expected:
      - &viewExp
        principal: alicia
        resource: alicia_private_album
        actions:
          view: EFFECT_ALLOW

      - <<: *viewExp
        resource: alicia_public_album

      - <<: *viewExp
        resource: alicia_flagged_album

      - <<: *viewExp
        principal: bradley
        resource: alicia_public_album

      - <<: *viewExp
        principal: bradley
        resource: alicia_flagged_album

      - <<: *viewExp
        principal: maria
        resource: alicia_public_album

      - <<: *viewExp
        principal: maria
        resource: alicia_flagged_album

  - name: Delete album
    input:
      <<: *testInput
      actions:
        - delete
    expected:
      - &deleteExp
        principal: alicia
        resource: alicia_private_album
        actions:
          delete: EFFECT_ALLOW

      - <<: *deleteExp
        resource: alicia_public_album

      - <<: *deleteExp
        resource: alicia_flagged_album

      - <<: *deleteExp
        principal: maria
        resource: alicia_flagged_album
```

Now run the compiler.

```shell
docker run -it -v $(pwd):/photo-share ghcr.io/cerbos/cerbos:0.51.0 \
    compile /photo-share/policies
```

Test results
└──AlbumObjectTestSuite (album_object_test.yaml) [18 OK]

18 tests executed [18 OK]

| |  See <https://github.com/cerbos/photo-share-tutorial> for an example of using Cerbos GitHub Actions in a CI workflow to compile and test policies. |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#%5Fusing%5Fschemas%5Fto%5Fenforce%5Ftype%5Fsafety%5Foptional)Using schemas to enforce type safety \[Optional\]

The derived roles and resource policy rules we defined above rely on certain attributes being present in the `attr` sections of the incoming request. To ensure that API requests are strictly-typed and contain required attributes, we can define schemas for the principal and resource attributes sections.

Create a new directory named `_schemas` inside the `policies` directory.

```sh
mkdir policies/_schemas
```

Let’s add a JSON schema defining the data types and required fields for `album:object` resources. Create a file named `album_object.json` inside the `policies/_schemas` directory with the following contents:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "owner": {
      "type": "string"
    },
    "public": {
      "type": "boolean"
    },
    "flagged": {
      "type": "boolean"
    }
  },
  "required": [
    "owner"
  ]
}
```

Now update `policies/resource_album_object.yaml` to add the reference to the schema:

```yaml
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: "default"
  importDerivedRoles:
    - apatr_common_roles
  resource: "album:object"
  rules:
    - actions: ['*']
      effect: EFFECT_ALLOW
      derivedRoles:
        - owner

    - actions: ['view', 'flag']
      effect: EFFECT_ALLOW
      roles:
        - user
      condition:
        match:
          expr: request.resource.attr.public == true

    - actions: ['view', 'delete']
      effect: EFFECT_ALLOW
      derivedRoles:
        - abuse_moderator

  schemas:
    resourceSchema:
      ref: cerbos:///album_object.json (1)
```

| **1** | Defines the schema to use for validating resource attributes |
| ----- | ------------------------------------------------------------ |

Update `.cerbos.yaml` to enable schema enforcement.

```yaml
---
server:
  httpListenAddr: ":3592"

storage:
  driver: "disk"
  disk:
    directory: /photo-share/policies

schema:
  enforcement: reject
```

Now start the server again and send a request that does not conform to the schema. The server response should contain a list of validation errors.

```shell
docker run -it -v $(pwd):/photo-share -p 3592:3592 ghcr.io/cerbos/cerbos:0.51.0 \
    server --config=/photo-share/.cerbos.yaml
```

Invalid request

```shell
cat <<EOF | curl --silent "http://localhost:3592/api/check/resources?pretty" -d @-
{
  "requestId": "test02",
  "includeMeta": true,
  "principal": {
    "id": "alicia",
    "policyVersion": "default",
    "roles": [
      "user"
    ]
  },
  "resources": [
    {
      "actions": [
        "view"
      ],
      "resource": {
        "id": "XX125",
        "policyVersion": "default",
        "kind": "album:object",
        "attr": {
          "public": "false",
          "flagged": "false"
        }
      }
    }
  ]
}
EOF
```

{
  "requestId": "test02",
  "results": [
    {
      "resource": {
        "id": "XX125",
        "kind": "album:object",
        "policyVersion": "default"
      },
      "actions": {
        "view": "EFFECT_DENY"
      },
      "validationErrors": [
        {
          "message": "missing properties: 'owner'",
          "source": "SOURCE_RESOURCE"
        },
        {
          "path": "/public",
          "message": "expected boolean, but got string",
          "source": "SOURCE_RESOURCE"
        },
        {
          "path": "/flagged",
          "message": "expected boolean, but got string",
          "source": "SOURCE_RESOURCE"
        }
      ],
      "meta": {
        "actions": {
          "view": {
            "matchedPolicy": "resource.album_object.vdefault"
          }
        }
      }
    }
  ]
}

Convex adapter
====================
The `@cerbos/orm-convex` package converts a Cerbos [PlanResources](../../api/index.html#resources-query-plan) response into a [Convex](https://convex.dev/) filter function. Authorization conditions are split between a database-level filter and an optional JavaScript post-filter for operators that Convex cannot express natively.

## [](#%5Frequirements)Requirements

* Cerbos >= v0.16
* `@cerbos/http` or `@cerbos/grpc` client
* Convex 1.x
* Node.js >= 20.0.0

## [](#%5Finstallation)Installation

```bash
npm install @cerbos/orm-convex
```

## [](#%5Fsupported%5Foperators)Supported operators

### [](#%5Fdatabase%5Flevel%5Foperators)Database-level operators

| Category   | Operators                                                      |
| ---------- | -------------------------------------------------------------- |
| Logical    | and, or, not — q.and(…​), q.or(…​), q.not(…​)                  |
| Comparison | eq, ne, lt, le, gt, ge — q.eq, q.neq, q.lt, q.lte, q.gt, q.gte |
| Membership | in — composed as q.or(q.eq(field, v1), q.eq(field, v2), …​)    |
| Existence  | isSet — q.neq(field, undefined) or q.eq(field, undefined)      |

### [](#%5Fpost%5Ffilter%5Foperators)Post-filter operators

The following operators cannot be expressed as Convex database filters. When encountered, the adapter returns a `postFilter` function that evaluates them in JavaScript:

| Category   | Operators                                                      |
| ---------- | -------------------------------------------------------------- |
| String     | contains, startsWith, endsWith                                 |
| Collection | hasIntersection, exists, exists\_one, all, filter, map, lambda |

For `and(…​)` expressions with mixed operator types, the adapter splits the tree: database-pushable children go to `filter`, the rest go to `postFilter`. For `or(…​)` with any unsupported child, the entire expression goes to `postFilter` to avoid missing results.

### [](#%5Fallowpostfilter%5Fopt%5Fin)`allowPostFilter` opt-in

By default, `queryPlanToConvex` throws when the query plan requires a `postFilter`. This is because post-filter operators cause data to be fetched before authorization filtering is fully applied. To opt in:

```typescript
const { kind, filter, postFilter } = queryPlanToConvex({
  queryPlan,
  mapper,
  allowPostFilter: true,
});
```

If your policies only use operators that Convex supports natively, `filter` alone enforces the full policy at the database level and this flag is not needed.

## [](#%5Fusage)Usage

```typescript
import { queryPlanToConvex, PlanKind } from "@cerbos/orm-convex";

const queryPlan = await cerbos.planResources({
  principal: { id: "user1", roles: ["USER"] },
  resource: { kind: "document" },
  action: "view",
});

const { kind, filter, postFilter } = queryPlanToConvex({
  queryPlan,
  mapper,
  allowPostFilter: true,
});

if (kind === PlanKind.ALWAYS_DENIED) return [];

if (kind === PlanKind.ALWAYS_ALLOWED && !postFilter) {
  return await ctx.db.query("documents").collect();
}

let query = ctx.db.query("documents");
if (filter) query = query.filter(filter);
let results = await query.collect();
if (postFilter) results = results.filter(postFilter);
return results;
```

## [](#%5Ffield%5Fmapper)Field mapper

```typescript
const mapper = {
  "request.resource.attr.title": { field: "title" },
  "request.resource.attr.status": { field: "status" },
};

// Or as a function:
const mapper = (path) => ({
  field: path.replace("request.resource.attr.", ""),
});
```

The `field` property rewrites a Cerbos path to a Convex document field. Dot notation is supported for nested fields. If the mapper is omitted, the adapter uses query plan paths as-is.

## [](#%5Flimitations)Limitations

* String and collection operators are evaluated as a JavaScript `postFilter` after the database query returns. These conditions do not reduce the number of documents read from the database.
* For `or(…​)` expressions where any child uses an unsupported operator, the entire OR is evaluated via `postFilter`.
* The `in` operator is composed as multiple `eq` comparisons joined with `or`, which may be less efficient for large value lists.

## [](#%5Fsource%5Fcode)Source code

[cerbos/query-plan-adapters/convex](https://github.com/cerbos/query-plan-adapters/tree/main/convex)

Drizzle adapter
====================
The `@cerbos/orm-drizzle` package converts a Cerbos [PlanResources](../../api/index.html#resources-query-plan) response into a Drizzle ORM SQL expression. The resulting filter can be composed with your existing query builder chain.

## [](#%5Frequirements)Requirements

* Cerbos >= v0.16
* `@cerbos/http` or `@cerbos/grpc` client
* Drizzle ORM (SQLite, PostgreSQL, MySQL, PlanetScale)
* Node.js >= 20.0.0

## [](#%5Finstallation)Installation

```bash
npm install @cerbos/orm-drizzle
```

## [](#%5Fsupported%5Foperators)Supported operators

* Logical: `and`, `or`, `not`
* Comparison: `eq`, `ne`, `lt`, `gt`, `le`, `ge`, `in`
* String: `contains`, `startsWith`, `endsWith`
* Existence: `isSet`
* Collection: `hasIntersection`, `exists`, `exists_one`, `all`, `filter`
* Relation-aware mappings with `EXISTS` subqueries

## [](#%5Fusage)Usage

```typescript
import { queryPlanToDrizzle, PlanKind } from "@cerbos/orm-drizzle";
import { eq, and } from "drizzle-orm";
import { resources } from "./schema";

const plan = await cerbos.planResources({
  principal,
  resource: { kind: "document" },
  action: "view",
});

const result = queryPlanToDrizzle({
  queryPlan: plan,
  mapper: {
    "request.resource.attr.status": resources.status,
    "request.resource.attr.owner": resources.ownerId,
  },
});

switch (result.kind) {
  case PlanKind.ALWAYS_DENIED:
    return [];
  case PlanKind.ALWAYS_ALLOWED:
    return await db.select().from(resources);
  case PlanKind.CONDITIONAL:
    return await db
      .select()
      .from(resources)
      .where(result.filter);
}
```

## [](#%5Ffield%5Fmapper)Field mapper

The mapper associates Cerbos attribute references with Drizzle columns. It accepts:

* A plain object with keys as Cerbos attribute references and values as Drizzle columns or SQL expressions
* A function receiving the attribute reference and returning the column or expression
* An object with a `column` property and an optional `transform` function for custom SQL translation

```typescript
const result = queryPlanToDrizzle({
  queryPlan,
  mapper: {
    "request.resource.attr.custom": {
      column: sql`lower(${resources.title})`,
      transform: ({ operator, value }) => {
        if (operator !== "eq") throw new Error("Unsupported");
        return eq(sql`lower(${resources.title})`, value.toLowerCase());
      },
    },
  },
});
```

## [](#%5Frelation%5Fmapping)Relation mapping

The adapter wraps relation comparisons in `EXISTS` subqueries, automatically inferring relation fields when they match column names on the related table.

```typescript
const result = queryPlanToDrizzle({
  queryPlan,
  mapper: {
    "request.resource.attr.owner": {
      relation: {
        type: "one",
        table: owners,
        sourceColumn: resources.ownerId,
        targetColumn: owners.id,
        fields: {
          email: owners.email,
        },
      },
    },
    "request.resource.attr.tags": {
      relation: {
        type: "many",
        table: resourceTags,
        sourceColumn: resources.id,
        targetColumn: resourceTags.resourceId,
        fields: {
          name: {
            relation: {
              type: "one",
              table: tags,
              sourceColumn: resourceTags.tagId,
              targetColumn: tags.id,
              field: tags.name,
            },
          },
        },
      },
    },
  },
});
```

## [](#%5Fcollection%5Foperators)Collection operators

* `hasIntersection` — translates to `column IN (…​)` for multi-valued attributes mapped as nested relations
* `exists`, `exists_one`, `all` — generate correlated `EXISTS` subqueries with the lambda variable scoped to the relation
* `filter` — Cerbos uses this during plan construction; the adapter discards the lambda since the filter is applied in Drizzle

## [](#%5Fsource%5Fcode)Source code

[cerbos/query-plan-adapters/drizzle](https://github.com/cerbos/query-plan-adapters/tree/main/drizzle)

Query plan adapters
====================
The Cerbos [PlanResources API](../../api/index.html#resources-query-plan) returns a query plan describing which resources a principal can access for a given action. Cerbos provides reference implementations of query plan adapters that convert that response into native query filters for your data layer, so authorization conditions are evaluated at the database level rather than in application code. Use these adapters as-is or as a starting point to build your own.

## [](#%5Favailable%5Fadapters)Available adapters

| Adapter                                         | Language   | Target                                                      |
| ----------------------------------------------- | ---------- | ----------------------------------------------------------- |
| [Prisma](prisma.html)                           | TypeScript | Prisma ORM (PostgreSQL, MySQL, SQLite, SQL Server, MongoDB) |
| [Drizzle](drizzle.html)                         | TypeScript | Drizzle ORM (PostgreSQL, MySQL, SQLite)                     |
| [Mongoose](mongoose.html)                       | TypeScript | MongoDB via Mongoose                                        |
| [Convex](convex.html)                           | TypeScript | Convex reactive database                                    |
| [LangChain / ChromaDB](langchain-chromadb.html) | TypeScript | ChromaDB vector store via LangChain.js                      |
| [SQLAlchemy](sqlalchemy.html)                   | Python     | SQLAlchemy (PostgreSQL, MySQL, SQLite, Oracle, SQL Server)  |

LangChain / ChromaDB adapter
====================
The `@cerbos/langchain-chromadb` package converts a Cerbos [PlanResources](../../api/index.html#resources-query-plan) response into a [ChromaDB](https://www.trychroma.com/) `Where` filter object compatible with the LangChain.js Chroma vector store. This enables authorization-aware similarity searches where Cerbos policy conditions are pushed down as metadata filters.

## [](#%5Frequirements)Requirements

* Cerbos >= v0.16
* `@cerbos/http` or `@cerbos/grpc` client
* ChromaDB 3.x
* Node.js >= 20.0.0

## [](#%5Finstallation)Installation

```bash
npm install @cerbos/langchain-chromadb
```

## [](#%5Fsupported%5Foperators)Supported operators

| Category   | Operators                                                |
| ---------- | -------------------------------------------------------- |
| Logical    | and, or — $and, $or                                      |
| Negation   | not — operator inversion via De Morgan’s law (see below) |
| Comparison | eq, ne, lt, le, gt, ge — $eq, $ne, $lt, $lte, $gt, $gte  |
| Membership | in — $in                                                 |

### [](#%5Fnegation%5Fhandling)Negation handling

ChromaDB has no `$not` or `$nor` filter. The adapter handles `not` expressions by inverting the inner operator:

* `not(eq)` becomes `$ne`; `not(ne)` becomes `$eq`
* `not(lt)` becomes `$gte`; `not(gt)` becomes `$lte`; `not(le)` becomes `$gt`; `not(ge)` becomes `$lt`
* `not(in)` becomes `$nin`
* `not(and(A, B))` becomes `$or[not(A), not(B)]` (De Morgan’s law)
* `not(or(A, B))` becomes `$and[not(A), not(B)]` (De Morgan’s law)
* `not(not(X))` becomes `X` (double negation elimination)

### [](#%5Funsupported%5Foperators)Unsupported operators

ChromaDB stores flat scalar metadata. The following operators cannot be mapped and cause `queryPlanToChromaDB` to throw an error:

* String: `contains`, `startsWith`, `endsWith`
* Existence: `isSet`
* Collection: `hasIntersection`, `exists`, `exists_one`, `all`, `filter`, `map`, `lambda`, `size`

## [](#%5Fusage)Usage

```typescript
import { queryPlanToChromaDB, PlanKind } from "@cerbos/langchain-chromadb";
import { Chroma } from "@langchain/community/vectorstores/chroma";
import { OpenAIEmbeddings } from "@langchain/openai";

const queryPlan = await cerbos.planResources({
  principal: { id: "user1", roles: ["USER"] },
  resource: { kind: "document" },
  action: "view",
});

const result = queryPlanToChromaDB({
  queryPlan,
  fieldNameMapper: {
    "request.resource.attr.department": "department",
    "request.resource.attr.public": "public",
  },
});

if (result.kind === PlanKind.ALWAYS_DENIED) {
  return [];
}

const chroma = await Chroma.fromExistingCollection(
  new OpenAIEmbeddings(),
  { collectionName: "my_collection" },
);

const filters =
  result.kind === PlanKind.CONDITIONAL ? result.filters : undefined;
const matches = await chroma.similaritySearch("query", 10, filters);
```

## [](#%5Ffield%5Fname%5Fmapper)Field name mapper

The mapper translates Cerbos attribute references to ChromaDB metadata field names. It accepts an object or a function.

```typescript
// Object mapper
const result = queryPlanToChromaDB({
  queryPlan,
  fieldNameMapper: {
    "request.resource.attr.aBool": "aBool",
    "request.resource.attr.aString": "title",
  },
});

// Function mapper
const result = queryPlanToChromaDB({
  queryPlan,
  fieldNameMapper: (fieldName) =>
    fieldName.replace("request.resource.attr.", ""),
});
```

If a field is not found in the object mapper, the original Cerbos path is used as-is.

## [](#%5Fsource%5Fcode)Source code

[cerbos/query-plan-adapters/langchain-chromadb](https://github.com/cerbos/query-plan-adapters/tree/main/langchain-chromadb)

Mongoose adapter
====================
The `@cerbos/orm-mongoose` package converts a Cerbos [PlanResources](../../api/index.html#resources-query-plan) response into a MongoDB filter compatible with Mongoose’s `find()` method.

## [](#%5Frequirements)Requirements

* Cerbos >= v0.16
* `@cerbos/http` or `@cerbos/grpc` client
* Mongoose 8.x or 9.x
* MongoDB 5.0+
* Node.js >= 20.0.0

## [](#%5Finstallation)Installation

```bash
npm install @cerbos/orm-mongoose
```

## [](#%5Fsupported%5Foperators)Supported operators

| Category   | Operators                                                                              |
| ---------- | -------------------------------------------------------------------------------------- |
| Logical    | and, or, not — mapped to $and, $or, $nor                                               |
| Comparison | eq, ne, lt, le, gt, ge — mapped to $eq, $ne, $lt, $lte, $gt, $gte                      |
| Membership | in, hasIntersection — $in for simple lists, $elemMatch for array relations             |
| String     | contains, startsWith, endsWith — escaped regular expressions                           |
| Existence  | isSet, exists, exists\_one — $exists/$ne: null for scalars, $elemMatch for collections |
| Collection | filter, lambda, map, all — scoped $elemMatch filters with lambda variable resolution   |

| |  exists\_one behaves as "at least one element matches". Enforcing "exactly one" requires an aggregation pipeline, which is outside the scope of this adapter. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#%5Fusage)Usage

```typescript
import { queryPlanToMongoose, PlanKind } from "@cerbos/orm-mongoose";

const queryPlan = await cerbos.planResources({
  principal: { id: "user1", roles: ["USER"] },
  resource: { kind: "document" },
  action: "view",
});

const result = queryPlanToMongoose({ queryPlan, mapper });

if (result.kind === PlanKind.ALWAYS_DENIED) {
  return [];
}

const filters = result.kind === PlanKind.CONDITIONAL ? result.filters : {};
const records = await MyModel.find(filters);
```

Combine with existing application filters using `$and`:

```typescript
await MyModel.find({ $and: [filters ?? {}, { archived: false }] });
```

## [](#%5Ffield%5Fmapper)Field mapper

```typescript
const mapper = {
  "request.resource.attr.title": { field: "title" },
  "request.resource.attr.owner": {
    relation: { name: "owner", type: "one", field: "id" },
  },
  "request.resource.attr.tags": {
    relation: {
      name: "tags",
      type: "many",
      fields: { name: { field: "name" } },
    },
  },
};
```

* `field` — rewrites a Cerbos path to a different field name in MongoDB
* `valueParser` — transforms leaf values during filter construction (for example, converting strings to `ObjectId`)
* `relation` — describes embedded documents (`type: "one"`) or arrays (`type: "many"`)
* `fields` — nested overrides for lambda expressions such as `tag.name`

### [](#%5Fvalue%5Fparsing)Value parsing

Use `valueParser` to convert values from the query plan into types MongoDB expects:

```typescript
import { Types } from "mongoose";

const mapper = {
  "request.resource.attr.id": {
    field: "_id",
    valueParser: (value) => new Types.ObjectId(value),
  },
};
```

## [](#%5Fcollection%5Foperators)Collection operators

Collection-aware operators (`filter`, `exists`, `exists_one`, `hasIntersection`, `map`, `all`) require the mapper to declare the relation with `type: "many"`. The adapter scopes lambda variables and uses the `fields` map when translating expressions:

* `exists`, `exists_one`, `filter` — wrap the condition in `$elemMatch`
* `hasIntersection` — supports both scalar arrays and arrays of objects; projects nested paths via `$elemMatch`
* `all` — converts the lambda condition into a negated `$elemMatch` so all elements must satisfy the predicate

## [](#%5Fsource%5Fcode)Source code

[cerbos/query-plan-adapters/mongoose](https://github.com/cerbos/query-plan-adapters/tree/main/mongoose)

Prisma adapter
====================
The `@cerbos/orm-prisma` package converts a Cerbos [PlanResources](../../api/index.html#resources-query-plan) response into a Prisma `where` clause. The resulting filter object can be passed directly to `findMany`, `count`, or any Prisma method that accepts a `where` argument.

## [](#%5Frequirements)Requirements

* Cerbos >= v0.40
* `@cerbos/http` or `@cerbos/grpc` client
* Prisma >= 6.0 (v7 supported)
* Node.js >= 20.0.0

## [](#%5Finstallation)Installation

```bash
npm install @cerbos/orm-prisma
```

## [](#%5Fsupported%5Foperators)Supported operators

### [](#%5Fscalar%5Foperators)Scalar operators

`and`, `or`, `not`, `eq`, `ne`, `lt`, `gt`, `lte`, `gte`, `in`, `startsWith`, `endsWith`, `contains`, `isSet`

### [](#%5Frelation%5Foperators)Relation operators

`is`, `isNot`, `some`, `none`, `every`, `exists`, `exists_one`, `all`, `filter`, `except`, `hasIntersection`

### [](#%5Fadvanced%5Ffeatures)Advanced features

* Deep nested relation support
* Automatic field inference from attribute paths
* Collection mapping and filtering
* Lambda expression handling

## [](#%5Fusage)Usage

```typescript
import { queryPlanToPrisma, PlanKind } from "@cerbos/orm-prisma";

const queryPlan = await cerbos.planResources({
  principal: { id: "user1", roles: ["USER"] },
  resource: { kind: "contact" },
  action: "read",
});

const result = queryPlanToPrisma({
  queryPlan,
  mapper: {
    "request.resource.attr.ownerId": { field: "ownerId" },
    "request.resource.attr.status": { field: "status" },
  },
});

switch (result.kind) {
  case PlanKind.ALWAYS_DENIED:
    return [];
  case PlanKind.ALWAYS_ALLOWED:
    return await prisma.contact.findMany();
  case PlanKind.CONDITIONAL:
    return await prisma.contact.findMany({
      where: result.filters,
    });
}
```

## [](#%5Ffield%5Fmapper)Field mapper

The mapper translates Cerbos attribute references to Prisma field names. It accepts either an object or a function.

```typescript
// Object mapper
const result = queryPlanToPrisma({
  queryPlan,
  mapper: {
    "request.resource.attr.status": { field: "status" },
  },
});

// Function mapper
const result = queryPlanToPrisma({
  queryPlan,
  mapper: (attr) => ({
    field: attr.replace("request.resource.attr.", ""),
  }),
});
```

## [](#%5Frelation%5Fmapping)Relation mapping

Relations are declared with their type and optional field configuration. Fields not explicitly mapped are inferred from the attribute path.

```typescript
const result = queryPlanToPrisma({
  queryPlan,
  mapper: {
    "request.resource.attr.owner": {
      relation: {
        name: "owner",
        type: "one",
      },
    },
    "request.resource.attr.tags": {
      relation: {
        name: "tags",
        type: "many",
        field: "name",
      },
    },
  },
});
```

### [](#%5Fnested%5Frelations)Nested relations

Relations can be nested to arbitrary depth:

```typescript
const result = queryPlanToPrisma({
  queryPlan,
  mapper: {
    "request.resource.attr.categories": {
      relation: {
        name: "categories",
        type: "many",
        fields: {
          subCategories: {
            relation: {
              name: "subCategories",
              type: "many",
              fields: {
                name: { field: "name" },
              },
            },
          },
        },
      },
    },
  },
});
```

The adapter generates the nested `NOT`, `some`, `every`, and `none` structures that Prisma requires for the full relation chain.

### [](#%5Flambda%5Fexpressions)Lambda expressions

Collection operators such as `exists` and `all` produce lambda expressions in the query plan. The adapter translates these into the corresponding Prisma relation filters:

```typescript
const result = queryPlanToPrisma({
  queryPlan,
  mapper: {
    "request.resource.attr.comments": {
      relation: {
        name: "comments",
        type: "many",
        fields: {
          author: {
            relation: {
              name: "author",
              type: "one",
            },
          },
          status: { field: "status" },
        },
      },
    },
  },
});
```

## [](#%5Fin%5Foperator%5Fnormalization)`in` operator normalization

The adapter normalizes `in` expressions to match Prisma conventions:

* Single values become equality comparisons: `{ field: "value" }`
* Arrays remain `{ field: { in: […​] } }`
* Relation-backed fields retain their relation structure while applying the appropriate operator at the leaf

## [](#%5Ftypes)Types

```typescript
import { PlanKind, QueryPlanToPrismaResult } from "@cerbos/orm-prisma";

type QueryPlanToPrismaResult =
  | { kind: PlanKind.ALWAYS_ALLOWED | PlanKind.ALWAYS_DENIED }
  | { kind: PlanKind.CONDITIONAL; filters: Record<string, any> };

type MapperConfig = {
  field?: string;
  relation?: {
    name: string;
    type: "one" | "many";
    field?: string;
    fields?: { [key: string]: MapperConfig };
  };
};

type Mapper =
  | { [key: string]: MapperConfig }
  | ((key: string) => MapperConfig);
```

## [](#%5Fsource%5Fcode)Source code

[cerbos/query-plan-adapters/prisma](https://github.com/cerbos/query-plan-adapters/tree/main/prisma)

## [](#%5Ftutorial%5Fexpress%5Fprisma%5Fcerbos)Tutorial: Express + Prisma + Cerbos

This walkthrough builds a CRM API using Express, Prisma, and Cerbos. The business rules:

* Admins can perform all actions
* Users in the Sales department can read and create contacts
* Only the user who created the contact can update and delete it

The full source code is available at [github.com/cerbos/express-prisma-cerbos](https://github.com/cerbos/express-prisma-cerbos/).

### [](#%5Fprisma%5Fschema)Prisma schema

```bash
mkdir express-prisma-cerbos
cd express-prisma-cerbos

npm i express @cerbos/grpc @prisma/client @cerbos/orm-prisma &&
npm i --save-dev @types/express ts-node
```

Create `prisma/schema.prisma`:

```prisma
datasource db {
  provider = "sqlite"
  url      = "file:./dev.db"
}

generator client {
  provider = "prisma-client-js"
}

model Contact {
  id             String   @id @default(cuid())
  createdAt      DateTime @default(now())
  updatedAt      DateTime @updatedAt
  firstName      String
  lastName       String
  ownerId        String
  active         Boolean  @default(false)
  marketingOptIn Boolean  @default(false)
}
```

Initialize the database:

```bash
npx prisma migrate dev --name init
```

### [](#%5Fcerbos%5Fpolicy)Cerbos policy

Create `cerbos/policies/contacts.yaml`:

```yaml
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: default
  resource: contact
  rules:
  - actions: ["*"]
    effect: EFFECT_ALLOW
    roles:
      - admin

  - actions: ["read", "create"]
    effect: EFFECT_ALLOW
    roles:
      - user
    condition:
      match:
        expr: request.principal.attr.department == "Sales"

  - actions: ["update", "delete"]
    effect: EFFECT_ALLOW
    roles:
      - user
    condition:
      match:
        expr: request.resource.attr.ownerId == request.principal.id
```

Start the Cerbos PDP:

```bash
docker run -i -t -p 3592:3592 \
  -v $(pwd)/cerbos/policies:/policies \
  ghcr.io/cerbos/cerbos:0.51.0 \
  server
```

### [](#%5Fauthorizing%5Findividual%5Fresources)Authorizing individual resources

Use `checkResource` to authorize access to a single contact:

```typescript
import { PrismaClient } from "@prisma/client";
import express from "express";
import { GRPC as Cerbos } from "@cerbos/grpc";

const prisma = new PrismaClient();
const cerbos = new Cerbos("localhost:3592", { tls: false });

const user = {
  id: "1",
  role: "user",
  department: "Sales",
};

app.get("/contacts/:id", async ({ params }, res) => {
  const contact = await prisma.contact.findUnique({
    where: { id: params.id },
  });
  if (!contact) return res.status(404).json({ error: "Contact not found" });

  const decision = await cerbos.checkResource({
    principal: {
      id: `${user.id}`,
      roles: [user.role],
      attributes: { department: user.department },
    },
    resource: {
      kind: "contact",
      id: contact.id + "",
      attributes: JSON.parse(JSON.stringify(contact)),
    },
    actions: ["read"],
  });

  if (decision.isAllowed("read")) {
    return res.json(contact);
  } else {
    return res.status(403).json({ error: "Unauthorized" });
  }
});
```

### [](#%5Ffiltering%5Fwith%5Fthe%5Fquery%5Fplan%5Fadapter)Filtering with the query plan adapter

Use `planResources` with the Prisma adapter to retrieve only the contacts the principal is authorized to access:

```typescript
import { queryPlanToPrisma, PlanKind } from "@cerbos/orm-prisma";

app.get("/contacts", async (req, res) => {
  const contactQueryPlan = await cerbos.planResources({
    principal: {
      id: `${user.id}`,
      roles: [user.role],
      attributes: { department: user.department },
    },
    resource: { kind: "contact" },
    action: "read",
  });

  const queryPlanResult = queryPlanToPrisma({
    queryPlan: contactQueryPlan,
    mapper: {
      "request.resource.attr.ownerId": { field: "ownerId" },
      "request.resource.attr.department": { field: "department" },
      "request.resource.attr.active": { field: "active" },
      "request.resource.attr.marketingOptIn": { field: "marketingOptIn" },
    },
  });

  let contacts;

  if (queryPlanResult.kind === PlanKind.ALWAYS_DENIED) {
    contacts = [];
  } else if (queryPlanResult.kind === PlanKind.ALWAYS_ALLOWED) {
    contacts = await prisma.contact.findMany({
      select: {
        firstName: true,
        lastName: true,
        active: true,
        marketingOptIn: true,
      },
    });
  } else if (queryPlanResult.kind === PlanKind.CONDITIONAL) {
    contacts = await prisma.contact.findMany({
      where: {
        AND: [{ ...queryPlanResult.filters }],
      },
      select: {
        firstName: true,
        lastName: true,
        active: true,
        marketingOptIn: true,
      },
    });
  }

  return res.json({ contacts });
});
```

### [](#%5Frunning%5Fthe%5Fexample)Running the example

Start the Cerbos PDP as described above, then start the Express server:

```bash
npx ts-node src/index.ts
```

Test the endpoints:

```bash
curl -i http://localhost:3000/contacts/1
curl -i http://localhost:3000/contacts
```

SQLAlchemy adapter
====================
The `cerbos-sqlalchemy` package converts a Cerbos [PlanResources](../../api/index.html#resources-query-plan) response into a SQLAlchemy `Select` instance. The resulting query object can be extended with additional `where` clauses or column selections before execution.

## [](#%5Frequirements)Requirements

* Cerbos >= v0.16
* [Cerbos Python SDK](https://github.com/cerbos/cerbos-sdk-python)
* SQLAlchemy >= 1.4 / 2.0

## [](#%5Finstallation)Installation

```bash
pip install cerbos-sqlalchemy
```

## [](#%5Fsupported%5Foperators)Supported operators

`and`, `or`, `not`, `eq`, `ne`, `lt`, `gt`, `le` (`lte`), `ge` (`gte`), `in`

Other operators (for example, math operators) can be handled programmatically and attached to the query via `query.where(…​)`.

## [](#%5Fusage)Usage

```python
from cerbos.sdk.client import CerbosClient
from cerbos.sdk.model import Principal, ResourceDesc
from cerbos_sqlalchemy import get_query
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class LeaveRequest(Base):
    __tablename__ = "leave_request"
    id = Column(Integer, primary_key=True)
    department = Column(String(225))
    geography = Column(String(225))
    team = Column(String(225))
    priority = Column(Integer)

with CerbosClient(host="http://localhost:3592") as c:
    p = Principal(
        "john",
        roles={"employee"},
        policy_version="20210210",
        attr={
            "department": "marketing",
            "geography": "GB",
            "team": "design",
        },
    )
    rd = ResourceDesc("leave_request", policy_version="20210210")
    plan = c.plan_resources("view", p, rd)

attr_map = {
    "request.resource.attr.department": LeaveRequest.department,
    "request.resource.attr.geography": LeaveRequest.geography,
    "request.resource.attr.team": LeaveRequest.team,
    "request.resource.attr.priority": LeaveRequest.priority,
}

query = get_query(plan, LeaveRequest, attr_map)
```

### [](#%5Fmulti%5Ftable%5Fjoins)Multi-table joins

When the `attr_map` references columns from more than one table, pass the join mapping as the fourth positional argument:

```python
query = get_query(
    plan,
    Table1,
    {
        "request.resource.attr.foo": Table1.foo,
        "request.resource.attr.bar": Table2.bar,
        "request.resource.attr.bosh": Table3.bosh,
    },
    [
        (Table2, Table1.table2_id == Table2.id),
        (Table3, Table1.table3_id == Table3.id),
    ],
)
```

### [](#%5Fextending%5Fthe%5Fquery)Extending the query

```python
query = query.where(LeaveRequest.priority < 5)

query = query.with_only_columns(
    LeaveRequest.department,
    LeaveRequest.geography,
)
```

## [](#%5Foverriding%5Fdefault%5Foperators)Overriding default operators

Override specific operator implementations for database-specific alternatives:

```python
from sqlalchemy.sql.expression import any_

query = get_query(
    plan,
    some_table,
    attr_map={"request.resource.attr.foo": Table1.foo},
    operator_override_fns={
        "in": lambda c, v: c == any_(v),
    },
)
```

## [](#%5Fsource%5Fcode)Source code

[cerbos/query-plan-adapters/sqlalchemy](https://github.com/cerbos/query-plan-adapters/tree/main/sqlalchemy)

## [](#%5Ftutorial%5Ffastapi%5Fsqlalchemy%5Fcerbos)Tutorial: FastAPI + SQLAlchemy + Cerbos

This walkthrough builds a contact directory API using FastAPI, SQLAlchemy, and Cerbos. The application demonstrates both `CheckResources` for individual resource authorization and `PlanResources` for query-level filtering.

The full source code is available at [github.com/cerbos/python-sqlalchemy-cerbos](https://github.com/cerbos/python-sqlalchemy-cerbos).

### [](#%5Fprerequisites)Prerequisites

* Python 3.10
* [SQLAlchemy](https://docs.sqlalchemy.org/en/14/) 1.4 / 2.0
* [Docker](https://www.docker.com/products/docker-desktop/)

### [](#%5Fdata%5Fmodel)Data model

The application has three entities:

* `User` — the person interacting with the application
* `Contact` — a person within a user’s directory (a user can have many contacts)
* `Company` — the company a contact is employed with (a company can have many contacts)

SQLAlchemy represents these as classes with column attributes and relationship declarations:

```python
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True)
    username = Column(String(255))
    email = Column(String(255))
    contacts = relationship("Contact", back_populates="owner")

class Contact(Base):
    __tablename__ = "contact"

    id = Column(String, primary_key=True)
    owner_id = Column(String, ForeignKey("user.id"))
    owner = relationship("User", back_populates="contacts", lazy="joined")
```

The `ForeignKey` on the child table establishes the many-to-one side. `lazy="joined"` loads the related object at attribute access time. The full table definitions are in [app/models.py](https://github.com/cerbos/python-sqlalchemy-cerbos/blob/main/app/models.py).

### [](#%5Fdependency%5Finjection)Dependency injection

FastAPI dependables retrieve the Cerbos `Principal` and database `Contact` from request context:

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

def get_principal(credentials: HTTPBasicCredentials = Depends(security)) -> Principal:
    username = credentials.username
    with Session() as s:
        user = s.scalars(select(User).where(User.username == username)).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
    return Principal(user.id, roles={user.role}, attr={"department": user.department})

def get_db_contact(contact_id: str) -> Contact:
    with Session() as s:
        contact = s.scalars(select(Contact).where(Contact.id == contact_id)).first()
        if contact is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Contact not found",
            )
    return contact
```

### [](#%5Fauthorizing%5Findividual%5Fresources)Authorizing individual resources

Use `CheckResources` via the `is_allowed` method for single-resource authorization:

```python
@app.get("/contacts/{contact_id}")
def get_contact(
    db_contact: Contact = Depends(get_db_contact),
    p: Principal = Depends(get_principal),
):
    r = get_resource_from_contact(db_contact)

    with CerbosClient(host="http://localhost:3592") as c:
        if not c.is_allowed("read", p, r):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized"
            )

    return db_contact
```

### [](#%5Ffiltering%5Fwith%5Fthe%5Fquery%5Fplan%5Fadapter)Filtering with the query plan adapter

Use `PlanResources` with the SQLAlchemy adapter to retrieve only the contacts the principal is authorized to access:

```python
@app.get("/contacts")
def get_contacts(p: Principal = Depends(get_principal)):
    with CerbosClient(host="http://localhost:3592") as c:
        rd = ResourceDesc("contact")
        plan = c.plan_resources("read", p, rd)

    query = get_query(
        plan,
        Contact,
        {
            "request.resource.attr.owner_id": User.id,
            "request.resource.attr.department": User.department,
            "request.resource.attr.is_active": Contact.is_active,
            "request.resource.attr.marketing_opt_in": Contact.marketing_opt_in,
        },
        [(User, Contact.owner_id == User.id)],
    )

    query = query.with_only_columns(
        Contact.id,
        Contact.first_name,
        Contact.last_name,
        Contact.is_active,
        Contact.marketing_opt_in,
    )

    with Session() as s:
        rows = s.execute(query).fetchall()

    return rows
```

The `get_query` function accepts:

1. The query plan response
2. A primary SQLAlchemy `Table` or ORM entity (the `FROM` table)
3. The attribute map — Cerbos resource attribute strings mapped to SQLAlchemy columns
4. (Optional) Explicit table joins — required when the attribute map references columns from multiple tables

### [](#%5Frunning%5Fthe%5Fexample)Running the example

Clone and start:

```bash
git clone git@github.com:cerbos/python-sqlalchemy-cerbos.git
cd python-sqlalchemy-cerbos

cd cerbos && ./start.sh && cd ..

pdm install
pdm run demo
```

Test the endpoints:

```bash
# Get all permitted contacts
curl http://john@localhost:8000/contacts

# Get a single contact (Sales user, owned contact)
curl -i http://john@localhost:8000/contacts/1

# Delete a contact (owner)
curl -i http://john@localhost:8000/contacts/1 -X DELETE

# Create a contact (Sales user)
curl -i http://john@localhost:8000/contacts/new \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"first_name": "frodo", "last_name": "baggins", "owner_id": "2", "company_id": "2"}'
```

Implementing authorization in RAG-based AI systems
====================
As companies implement AI applications, a Retrieval Augmented Generation (RAG) architecture is often used to give an LLM context from internal data. The challenge that consequently arises is how to provide the LLM with sufficient context without violating privacy and authorization policies. Companies need to ensure that AI agents can’t inappropriately access sensitive data or expose it to unauthorized users.

## [](#%5Fhow%5Fthe%5Fcerbos%5Fquery%5Fplan%5Fworks%5Fwith%5Frag)How the Cerbos query plan works with RAG

RAG architecture can leverage large data sets of internal knowledge: documents, meeting notes, and resources to provide business-specific context to the LLM. This business data first has to be extracted from the system of record (ERP, CRM, HRIS, etc), go through an embedding process, and then be loaded into a vector store — which is a specialized database that can find similar items based on their vector embeddings. Vector stores also support storing metadata such as what the source system was, which department it belongs to and which region it’s associated with. These can all be leveraged for making authorization decisions.

With the business data stored along with its associated metadata, a typical workflow would be to put a chatbot-style interface in front. The workflow that processes user input and produces results can use Cerbos to apply authorization logic to data retrieval.

1. The access filters applicable to the user in the current context are generated by the Cerbos Policy Decision Point (PDP).
2. The user input is vectorized using an embedding model and used to query the vector data store. A metadata filter is applied to the query using the Cerbos query plan to restrict the results.
3. The retrieved documents are injected into the prompt and fed to the LLM to generate the answer.

## [](#%5Fleveraging%5Fcerbos%5Fquery%5Fplan%5Ffor%5Fauthorization)Leveraging Cerbos Query Plan for authorization

Cerbos can be used to enforce authorization policies on the data retrieval step in the RAG architecture. The Cerbos Query Plan can be used to generate filters based on the user’s identity and the metadata associated with the data. This ensures that the LLM only uses data that the user is authorized to access.

As an example, consider a scenario where a LLM is used to provide information about work projects. A project is associated with a department and a region and only those users in the same department or region should be able to access it. The Cerbos policy for this could be defined as follows:

```yaml
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: "default"
  resource: "project"

  rules:
    - actions: ["read"]
      effect: EFFECT_ALLOW
      condition:
        all:
          of:
            - expr: R.attr.department == P.attr.department
            - expr: R.attr.region == P.attr.region

    # ... other rules
```

When a user issues a query using the chat interface, their authorization context is passed to the Cerbos PDP in a [PlanResources](../../../api/index.html#plan-resources) request to produce a plan for performing the `read` action on the `project` resource kind.`` ` ``

```json
{
  "principal": {
    "id": "alice",
    "roles": [
      "USER",
      "MANAGER"
    ],
    "attr": {
      "department": "FINANCE",
      "region": "EMEA"
    }
  },
  "resource": {
    "kind": "project",
  },
  "action": "read",
}
```

The Query Plan generated by Cerbos would then include the following conditions - note that the actual response is completely dynamic and depends on the user’s identity and the policy defined in Cerbos:

```json
{
  "action": "read",
  "resourceKind": "project",
  "filter": {
    "kind": "KIND_CONDITIONAL",
    "condition": {
      "expression": {
        "operator": "and",
        "operands": [
          {
            "expression": {
              "operator": "eq",
              "operands": [
                {
                  "variable": "request.resource.attr.department"
                },
                {
                  "value": "FINANCE"
                }
              ]
            }
          },
          {
            "expression": {
              "operator": "eq",
              "operands": [
                {
                  "variable": "request.resource.attr.region"
                },
                {
                  "value": "EMEA"
                }
              ]
            }
          }
        ]
      }
    }
  }
}
```

This set of conditions then can be converted into a metadata filter that can be applied to the vector store query to ensure that only the data that the user is authorized to access is retrieved. Each vector store has its own syntax for defining filters. With the popular [Chroma](https://www.trychroma.com/) database system, a filter looks as follows.

```json
{
  "$and": [
    {"department": "FINANCE"},
    {"region": "EMEA"}
  ]
}
```

With this filter in place, any documents retired from the vector store would be limited to those that match the user’s department and region, ensuring that the LLM only receives data that the user is authorized to access.

Implementing authorization in RAG-based AI systems is crucial to ensure that sensitive data is not exposed to unauthorized users. By leveraging Cerbos query plan, companies can ensure that their LLM use cases don’t inadvertently violate privacy and data security requirements.

Tutorial: Using Cerbos with Auth0
====================
An example application of integrating [Cerbos](https://cerbos.dev) with an [Express](https://expressjs.com/) server using [Auth0](https://auth0.com/) for authentication.

## [](#%5Fdependencies)Dependencies

* Node.js
* Docker for running the [Cerbos Policy Decision Point (PDP)](../../../installation/container.html)
* An [Auth0](https://auth0.com/) account if you want to use your own

## [](#%5Fgetting%5Fstarted)Getting started

1. Clone the repo  
```bash  
git clone git@github.com:cerbos/express-auth0-cerbos.git  
```
2. Start up the Cerbos PDP instance docker container. This will be called by the express app to check authorization.  
```bash  
cd cerbos  
./start.sh  
```
3. Install node dependencies  
```bash  
npm install  
```
4. Start the express server  
```bash  
node index.js  
```

## [](#%5Fauth0%5Frule%5Fto%5Fadd%5Froles%5Fto%5Ftoken)Auth0 Rule to add roles to token

By default any roles set up in the Auth0 console are not passed through in the authentication token. To enable this, add the following rule to the Auth Pipeline in your Auth0 account.

```js
function (user, context, callback) {
  const namespace = 'https://cerbos.cloud';
  const assignedRoles = (context.authorization || {}).roles;

  let idTokenClaims = context.idToken || {};
  let accessTokenClaims = context.accessToken || {};

  idTokenClaims[`${namespace}/roles`] = assignedRoles;
  accessTokenClaims[`${namespace}/roles`] = assignedRoles;

  context.idToken = idTokenClaims;
  context.accessToken = accessTokenClaims;

  callback(null, user, context);
}
```

## [](#%5Fpolicies)Policies

This example has a simple CRUD policy in place for a resource kind of`contact` \- like a CRM system would have. The policy file can be found in the `cerbos/policies` folder[here](https://github.com/cerbos/express-auth0-cerbos/blob/main/cerbos/policies/contact.yaml).

Should you wish to experiment with this policy, you can try it in the[Cerbos Playground](https://play.cerbos.dev/p/g561543292ospj7w0zOrFx7H5DzhmLu2).

The policy expects one of two roles to be set on the principal - `admin`and `user`. These roles are authorized as follows:

| Action | User     | Admin |
| ------ | -------- | ----- |
| list   | Y        | Y     |
| read   | Y        | Y     |
| create | Y        | Y     |
| update | If owner | Y     |
| delete | If owner | Y     |

This business logic is represented in Cerbos as a resource policy.

```yaml
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: default
  resource: contact
  rules:
    - actions: ["read", "create"]
      effect: EFFECT_ALLOW
      roles:
        - admin
        - user

    - actions: ["update", "delete"]
      effect: EFFECT_ALLOW
      roles:
        - admin

    - actions: ["update", "delete"]
      effect: EFFECT_ALLOW
      roles:
        - user
      condition:
        match:
          expr: request.resource.attr.owner == request.principal.id
```

Tutorial: Using Cerbos with AWS Cognito
====================
An example application of integrating [Cerbos](https://cerbos.dev) with a [FastAPI](https://fastapi.tiangolo.com/) server using [AWS Cognito](https://aws.amazon.com/cognito/) for authentication.

## [](#%5Fdependencies)Dependencies

* Python 3.10
* Docker for running the [Cerbos Policy Decision Point (PDP)](https://docs.cerbos.dev/cerbos/latest/installation/container.html)
* A configured AWS Cognito User Pool ([set-up guide](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-with-cognito-user-pools.html))

## [](#%5Fgetting%5Fstarted)Getting started

1. Clone the repo  
```bash  
git clone git@github.com:cerbos/python-cognito-cerbos.git  
```
2. Start up the Cerbos PDP instance docker container. This will be called by the FastAPI app to check authorization.  
```bash  
cd cerbos  
./start.sh  
```
3. Install python dependencies  
```bash  
# from project root  
./pw install  
```
4. Set the appropriate environment variables  
```bash  
AWS_COGNITO_POOL_ID  
AWS_COGNITO_CLIENT_ID  
AWS_DEFAULT_REGION  
AWS_COGNITO_POOL_NAME  
# if you've configured your user pool with a client secret  
AWS_COGNITO_CLIENT_SECRET  
# optionally, to enable the hosted UI:  
AWS_COGNITO_HOSTED_UI_CALLBACK_URL # this needs to match the callback URL configured for the hosted UI  
AWS_COGNITO_HOSTED_UI_LOGOUT_URL  
```
5. Start the FastAPI dev server  
```bash  
./pw demo  
```

## [](#%5Fcognito%5Fconfiguration)Cognito Configuration

### [](#%5Fgroups)Groups

This demo maps Cognito User Pool groups to Cerbos roles. The app will retrieve the groups from the access token, and use them to determine authorization.

Any test users in your pool should be added to one or both of `admin` and/or `user` groups to demonstrate different access to the demo resources.

## [](#%5Fpolicies)Policies

This example has a simple CRUD policy in place for a resource kind of`contact` \- like a CRM system would have. The policy file can be found in the `cerbos/policies` folder[here](https://github.com/cerbos/python-cognito-cerbos/blob/main/cerbos/policies/contact.yaml).

Should you wish to experiment with this policy, you can try it in the[Cerbos Playground](https://play.cerbos.dev/p/g561543292ospj7w0zOrFx7H5DzhmLu2).

The policy expects one of two roles to be set on the principal - `admin`and `user`. These roles are authorized as follows:

| Action | User     | Admin |
| ------ | -------- | ----- |
| list   | Y        | Y     |
| read   | Y        | Y     |
| create | Y        | Y     |
| update | If owner | Y     |
| delete | If owner | Y     |

This business logic is represented in Cerbos as a resource policy.

```yaml
---
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: default
  resource: contact
  rules:
    - actions: ["read", "create"]
      effect: EFFECT_ALLOW
      roles:
        - admin
        - user

    - actions: ["update", "delete"]
      effect: EFFECT_ALLOW
      roles:
        - admin

    - actions: ["update", "delete"]
      effect: EFFECT_ALLOW
      roles:
        - user
      condition:
        match:
          expr: request.resource.attr.owner == request.principal.id
```

Tutorial: Using Cerbos with FusionAuth
====================
An example stack of integrating [Cerbos](https://cerbos.dev) with an [Express](https://expressjs.com/) server using [FusionAuth](https://fusionauth.com/) for authentication.

This example is based off the [FusionAuth/fusionauth-example-node](https://github.com/fusionauth/fusionauth-example-node) repo.

## [](#%5Fdependencies)Dependencies

* docker-compose

## [](#%5Fgetting%5Fstarted)Getting started

1. Clone the repo  
```bash  
git clone git@github.com:cerbos/express-fusionauth-cerbos.git  
```

### [](#%5Fstart%5Fstack)Start Stack

Start up the stack `docker compose up` \- this will take some time to pull down all the images and launch them, but once started the following services will be running.

* FusionAuth <http://localhost:9011>
* Cerbos <http://localhost:3592/>
* Node App <http://localhost:8080/>
* Postgres DB for FustionAuth on port `5432`

### [](#%5Fconfigure%5Ffusionauth)Configure FusionAuth

This example is based off the[FusionAuth 5 Minute Guide](https://fusionauth.io/docs/v1/tech/5-minute-setup-guide/) \- and most of the steps have bee handled by the`docker compose` setup.

The only manual steps required are creating the application. To do this, open up <http://localhost:9011> and complete the setup wizard, then:

Once we arrive in the FusionAuth admin UI, the first thing we need to do is create an Application. An Application is something that a user can log into. This is the application we are building or that we are migrating to use FusionAuth. We’ll click the Application menu option on the left side of the page or the Setup button in the box at the top of the page.

![fusionauth dashboard applications](../../_images/fusionauth-dashboard-applications.png)

This will take us to the listing page for Applications. Next, we’ll click the green plus button (the add button) at the top of the page:

![fusionauth application listing](../../_images/fusionauth-application-listing.png)

On the Application form, we’ll need to provide a name for our Application (only used for display purposes) and a couple of items on the OAuth tab. We’ll start with a simple setup that allows existing users to log into your application. Therefore, we won’t need to define any roles or registration configuration. If we click on the OAuth tab, we’ll see these options:

![fusionauth application form](../../_images/fusionauth-application-form.png)

Most of the defaults will work, but we also need to provide these items:

* An authorized redirect URL. This is the route/controller in our application’s backend that will complete the OAuth workflow. This is also known as the 'Backend for Frontend' or BFF pattern, and is a lightweight proxy. In our example, we set this to`<http://localhost:8080/auth/callback>`. We’ll show some Node.js example code below for this route.
* Optionally, we can specify a valid Logout URL. This is where the user will be redirected to after they are logged out of FusionAuth’s OAuth front-end: our application.
* We need to ensure that the Authorization Code grant is selected in the Enabled Grants.

Next we need to add the roles that will be used by our policies. Back on the application listing page press the 'Manage Roles' button next to our application and add roles for `user` and `editor` (admin should already exist). These roles will be passed back with the user information to our application, and then passed onto Cerbos for use in authorization decisions.

![fusionauth add roles](../../_images/fusionauth-add-roles.png)

Once we have all of this configured, we can then copy the Client ID and Client Secret and move to the next step.

### [](#%5Fconfigure%5Fnode%5Fapp)Configure Node App

Now that our application has been created, we need to add the Client ID and Client Secret from FusionAuth into the top of `app/index.js` (line 12 & 13). These will be used to identify the app through the login flow.

### [](#%5Ftest%5Fthe%5Fapp)Test the app

Now that everything is wired up you should be able to goto<http://localhost:8080> and press the login link to authenticate with your FusionAuth account.

## [](#%5Fpolicies)Policies

This example has a simple CRUD policy in place for a resource kind of`contact` \- like a CRM system would have. The policy file can be found in the `cerbos/policies` folder[here](https://github.com/cerbos/express-fusionauth-cerbos/blob/main/cerbos/policies/contact.yaml).

Should you wish to experiment with this policy, you can try it in the[Cerbos Playground](https://play.cerbos.dev/p/g561543292ospj7w0zOrFx7H5DzhmLu2).

The policy expects one of two roles to be set on the principal - `admin`and `user`. These roles are authorized as follows:

| Action | User     | Admin |
| ------ | -------- | ----- |
| list   | Y        | Y     |
| read   | Y        | Y     |
| create | Y        | Y     |
| update | If owner | Y     |
| delete | If owner | Y     |

## [](#%5Frequest%5Fflow)Request Flow

1. User access the application and clicks `Login`
2. User is directed to the FusionAuth UI and authenticates
3. A token is returned back in the redirect URL to the application
4. That token is then exchanged for the user profile information
5. The user profile from FusionAuth being stored (user Id, email, roles etc).
6. Any requests to the `/contacts` endpoints fetch the data required about the resource being accessed from the data store
7. Call the Cerbos PDP with the principal, resource and action to check the authorization and then return an error if the user is not authorized. The [Cerbos package](https://www.npmjs.com/package/cerbos) is used for this.  
```javascript  
---  
const allowed = await cerbos.check({  
  principal: { //pass in the Okta user ID and groups  
    id: req.userContext.userinfo.sub,  
    roles: req.userContext.userinfo.groups,  
  },  
  resource: {  
    kind: "contact",  
    instances: {  
      //a map of the resource(s) being accessed  
      [contact.id]: {  
        attr: contact,  
      },  
    },  
  },  
  actions: ["read"], //the list of actions being performed  
});  
```

if (!allowed.isAuthorized(contact.id, "read")) { return res.status(403).json({ error: "Unauthorized" }); } --- Implementation at this stage will be dependant on your business requirements.

Tutorial: Using Cerbos with JWT
====================
An example application of integrating [Cerbos](https://cerbos.dev) with an[Express](https://expressjs.com/) server using [JSON Web Tokens](https://jwt.io/) \- via [express-jwt](https://github.com/auth0/express-jwt) \- for authentication.

## [](#%5Fdependencies)Dependencies

* Node.js
* Docker for running the [Cerbos Policy Decision Point (PDP)](../../../installation/container.html)

## [](#%5Fgetting%5Fstarted)Getting started

1. Clone the repo  
```bash  
git clone git@github.com:cerbos/express-jwt-cerbos.git  
```
2. Start up the Cerbos PDP instance docker container. This will be called by the express app to check authorization.  
```bash  
cd cerbos  
./start.sh  
```
3. Install node dependencies  
```bash  
npm install  
```
4. Start the express server  
```bash  
npm run start  
```

## [](#%5Fpolicies)Policies

This example has a simple CRUD policy in place for a resource kind of`contact` \- like a CRM system would have. The policy file can be found in the `cerbos/policies` folder[here](https://github.com/cerbos/express-jwt-cerbos/blob/main/cerbos/policies/contact.yaml).

Should you wish to experiment with this policy, you can try it in the[Cerbos Playground](https://play.cerbos.dev/p/sZC611cf06deexP0q8CTcVufTVau1SA3).

The policy expects one of two roles to be set on the principal - `admin`and `user`. These roles are authorized as follows:

| Action | User | Admin |
| ------ | ---- | ----- |
| list   | Y    | Y     |
| read   | Y    | Y     |
| create | N    | Y     |
| update | N    | Y     |
| delete | N    | Y     |

This business logic is represented in Cerbos as a resource policy.

```yaml
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  version: default
  resource: contact
  rules:
  - actions: ["read", "list"]
    roles:
      - admin
      - user
    effect: EFFECT_ALLOW

  - actions: ["create", "update", "delete"]
    roles:
      - admin
    effect: EFFECT_ALLOW
```

## [](#%5Fjwt%5Fstructure)JWT Structure

For this example a JWT needs to be generated to be passed in the authorization header. The payload of the token contains an array of roles which are passed into Cerbos to use for authorization - the structure is as follows:

{
  sub: string,
  name: string,
  iat: number,
  roles: string[] // "user" and "admin" supported in this demo
}

[JWT.io](https://jwt.io) can be used generate a token for testing purposes - an[example is here](https://jwt.io/#debugger-io?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwicm9sZXMiOlsiYWRtaW4iXSwiaWF0IjoxNTE2MjM5MDIyfQ.CQEEaSdswE2tou7MUeSe4-6kfe1imJXnbqhiMFsF13A).

**Note:** The secret is hardcoded in this example to `yoursecret` and the algorithm is `HS256` \- you will need to set these for the signature to be valid.

![JWT](../../_images/jwt-token.png)

## [](#%5Frequest%5Fflow)Request Flow

1. HTTP request comes in and the `express-jwt` library validates the token and adds the payload to `req.user`.
2. The contents of the JWT token is mapped to the structure of the principal object required by Cerbos

```js
// Extract data from the JWT (check DB etc) and create the principal object to be sent to Cerbos
const jwtToPrincipal = ({ sub, iat, roles = [], ...rest }) => {
  return {
    id: sub,
    roles,
    attr: rest,
  };
};
```

1. Fetch the data required about the resource being accessed from the data store
2. Call the Cerbos PDP with the principal, resource and action to check the authorization and then return an error if the user is not authorized. The [Cerbos package](https://www.npmjs.com/package/cerbos) is used for this.

```js
const allowed = await cerbos.check({
  principal: jwtToPrincipal(req.user),
  resource: {
    kind: "contact",
    instances: {
      //a map of the resource(s) being accessed
      [contact.id]: {
        attr: contact,
      },
    },
  },
  actions: ["read"], //the list of actions being performed
});

// not authorized for read action
if (!allowed.isAuthorized(contact.id, "read")) {
  return res.status(403).json({ error: "Unauthorized" });
}
```

1. Serve the response if authorized

## [](#%5Fexample%5Frequests)Example Requests

Once a JWT token has been generated requests can be made to the express server.

### [](#%5Flist%5Fcontacts)List contacts

Allowed for `user` and `admin` roles

```bash
curl -X GET 'http://localhost:3000/contacts' \
--header 'Authorization: Bearer <token here>'
```

### [](#%5Fget%5Fa%5Fcontact)Get a contact

Allowed for `user` and `admin` roles

```bash
curl -X GET 'http://localhost:3000/contacts/abc123' \
--header 'Authorization: Bearer <token here>'
```

### [](#%5Fcreate%5Fa%5Fcontact)Create a contact

Allowed for `admin` role only

```bash
curl -X POST 'http://localhost:3000/contacts/new' \
--header 'Authorization: Bearer <token here>'
```

Should this request be made with the JWT roles set to `["admin"]` the response will be"

```json
{ "result": "Created contact" }
```

Should this request be made with the JWT roles set to `["user"]` the response will be:

```json
{ "error": "Unauthorized" }
```

### [](#%5Fupdate%5Fa%5Fcontact)Update a contact

Allowed for `admin` role only

```bash
curl -X PATCH 'http://localhost:3000/contacts/abc123' \
--header 'Authorization: Bearer <token here>'
```

Should this request be made with the JWT roles set to `["admin"]` the response will be"

```json
{ "result": "Contact updated" }
```

Should this request be made with the JWT roles set to `["user"]` the response will be:

```json
{ "error": "Unauthorized" }
```

### [](#%5Fdelete%5Fa%5Fcontact)Delete a contact

Allowed for `admin` role only

```bash
curl -X DELETE 'http://localhost:3000/contacts/abc123' \
--header 'Authorization: Bearer <token here>'
```

Should this request be made with the JWT roles set to `["admin"]` the response will be"

```json
{ "result": "Contact deleted" }
```

Should this request be made with the JWT roles set to `["user"]` the response will be:

```json
{ "error": "Unauthorized" }
```

Tutorial: Using Cerbos with Magic
====================
The demise of passwords has [long been predicted](https://www.forbes.com/sites/forbestechcouncil/2020/03/06/the-inevitable-death-of-passwords/) due to the ongoing leaks, hacks and breaches in recent years.

There has been a lot of innovation in this space and [Magic](https://magic.link) has become a leader with their novel approach to eradicating the need to store passwords at all by making use of ‘magic links’ which are sent via the provided email address and log you in to the site once clicked.

> Magic provides a key-based identity solution built on top of the Decentralized Identity (DID) standard, where users’ identities are self-sovereign by leveraging blockchain public-private key pairs. These keypairs are used to generate zero-knowledge proofs to authenticate users instead of having to rely on users providing passwords to Magic or any identity provider

— Magic Whitepaper  
https://www.dropbox.com/s/3flqaszoigwis5b/Magic%20Whitepaper.pdf 

This approach is a great way to securely establish a user’s identity without running authentication infrastructure.

At this point, you can use this identity to fetch extra data such as roles and group memberships about the user from your directory, profile store or other database system to further add context about the user. The exact mechanism for this is out of the scope of this article, but Active Directory, LDAP or just a plain old DB are all good places to store this extra user information.

Once a user has authenticated (and the profile enriched with profile information) the next step is to establish what the user has permissions to do in the application - this is where Cerbos steps in and through it’s policy based approach can do context-aware authorization using the user (or principal in Cerbos speak) from Magic.

## [](#%5Fexample%5Fimplementation%5Fwith%5Fcerbos)Example Implementation with Cerbos

Implementing this requires passing the token provided from the Magic Client SDK to your backend code and then verifying it with the Magic Admin SDK.

As an example, we have forked Magic’s Node/Express/Passport demo repo and added in calls to Cerbos to demonstrate how the two systems can work together - you can find a live [demo here](https://demo-magiclink.cerbos.cloud/) and [view source code on GitHub](https://github.com/cerbos/express-magiclink-cerbos).

The logical data flow for how this is implemented is as follows:

1. User visits site and and enters their email address
2. Magic send an email to that address with a link which authenticates the user
3. The website gets a call back when a user clicks the link from the email with the authenticated identity and token client side
4. Calls to the authenticated endpoint can now be made with the token passed as a Bearer token which is parsed by Passport.js’s Magic integration
5. App code fetches the resource being accessed from the data store
6. App sends the user information from the verified Magic token along with the resource and desired actions to the Cerbos PDP instance
7. Cerbos PDP evaluates the policies and returns an ALLOW or DENY
8. App conditionally returns based on the authorization response

The key part of this are Steps #4-7 where the context about the principal and the resource is gathered and sent to Cerbos to determine the authorization. In this stage all the attributes about the resource and the user can now be used to make a decision.

## [](#%5Fconclusion)Conclusion

Magic’s approach to passwordless authentication and identity is a game changer in how to secure your application, and when paired with Cerbos for authorization, it is possible to deploy context-aware access controls without complex rules or token-bloat.

Tutorial: Using Cerbos with Okta
====================
An example application of integrating [Cerbos](https://cerbos.dev) with an [Express](https://expressjs.com/) server using [Okta](https://okta.com/) for authentication.

## [](#%5Fdependencies)Dependencies

* Node.js
* An [Okta](https://okta.com/) account

---

For simplicity this demo is using the hosted Cerbos Demo PDP avaliable in the Playground so running the Cerbos container locally isn’t required. For production use cases a deployed Cerbos PDP is required and the code updated to point to your instance. You can read more about the deployment options [here](https://docs.cerbos.dev/cerbos/latest/deployment/index.html). ---

## [](#%5Fsetup)Setup

### [](#%5Finstall%5Fdeps)Install Deps

1. Clone the repo  
```bash  
git clone git@github.com:cerbos/express-okta-cerbos.git  
```

### [](#%5Fcreate%5Fan%5Fokta%5Fapplication)Create an Okta Application

In your Okta instance you need to create a new application. For this example we will be making use of Okta’s ExpressOIDC package so the application’s sign-in method needs to be `OIDC - OpenID Connect` and the application type is `Web Application`.

![Okta Create App](../../_images/okta-create-app.png)

### [](#%5Fset%5Fredirect%5Furls)Set Redirect URLs

The default redirect URLs for sign-in and sign-out are correct if you are running this demo app on the default 8080 port. If you have chanaged this in your `.env` file then you will need to update accordingly.

![Okta App Settings](../../_images/okta-app-settings.png)

### [](#%5Fenabling%5Fgroups%5Fin%5Fthe%5Fokta%5Ftoken)Enabling Groups in the Okta Token

By default the groups the user belongs to are not passed to the application in the Okta token - this needs enabling as these groups will be passed from Okta to Cerbos for use in authorization decisions.

To do this, goto _Security > API_ in the sidebar, and edit the default_Authorization Server_.

On this page, got the _Claims_ tab and press _Add Claim_. Add a new claim called groups which includes the groups of the user in the ID token.

![Okta Groups Claim](../../_images/okta-groups-claim.png)

> In production you will likely want to filter this down, but for this example we are enabling all groups to be added to the token.

### [](#%5Fcreate%5Fan%5Fexample%5Fadmin%5Fgroup)Create an example `admin` group.

In a new Okta account the only group that exists is the _Everyone_group. For our demo application policies we expect users to be in`admin` or `user` group as this is what is checked.

Under _Directory > Groups_ press _Add Group_ and create the two groups and add your example users to them.

### [](#%5Fsetup%5Fenvironment%5Fvariables)Setup Environment Variables

Make a copy of the `.env.sample` file and call it `.env`. You will then need to populate the feilds that begin with `OKTA_` with the information provided in the new application you created.

PORT=8080
CERBOS_HOSTNAME=https://demo-pdp.cerbos.cloud
CERBOS_PLAYGROUND=ygW612cc9c9xXOsOZjI40ovY2LZvXf43
OKTA_DOMAIN=
OKTA_CLIENTID=
OKTA_CLIENTSECRET=
OKTA_APP_BASE_URL=http://localhost:8080

> This example is using the hosted Demo PDP of Cerbos and an example Playground instance. If you are running your own Cerbos PDP then update the `CERBOS_HOSTNAME` feild to your own instance and remove the`CERBOS_PLAYGROUND` feild.

### [](#%5Ftest%5Fthe%5Fapp)Test the app

Now that everything is wired up you should be able to goto<http://localhost:8080> and press the login link to authenticate with your Okta account.

## [](#%5Fpolicies)Policies

This example has a simple CRUD policy in place for a resource kind of`contact` \- like a CRM system would have. Should you wish to experiment with this policy, you can try it in the[Cerbos Playground](https://play.cerbos.dev/p/g561543292ospj7w0zOrFx7H5DzhmLu2).

The policy expects one of two roles to be set on the principal - `admin`and `user`. These roles are authorized as follows:

| Action | User | Admin |
| ------ | ---- | ----- |
| list   | Y    | Y     |
| read   | Y    | Y     |
| create | N    | Y     |
| update | N    | Y     |
| delete | N    | Y     |

## [](#%5Frequest%5Fflow)Request Flow

1. User access the application and clicks Login
2. User is directed to the Okta UI and authenticates
3. A token is returned back in the redirect URL to the application
4. That token is then exchanged for the user profile information
5. The user profile from Okta being stored (user Id, roles etc).
6. Any requests to the /contacts endpoints fetch the data required about the resource being accessed from the data store
7. Call the Cerbos PDP with the principal, resource and action to check the authorization and then return an error if the user is not authorized. The Cerbos package is used for this.  
```javascript  
---  
const allowed = await cerbos.check({  
  principal: { //pass in the Okta user ID and groups  
    id: req.userContext.userinfo.sub,  
    roles: req.userContext.userinfo.groups,  
  },  
  resource: {  
    kind: "contact",  
    instances: {  
      //a map of the resource(s) being accessed  
      [contact.id]: {  
        attr: contact,  
      },  
    },  
  },  
  actions: ["read"], //the list of actions being performed  
});  
```

if (!allowed.isAuthorized(contact.id, "read")) { return res.status(403).json({ error: "Unauthorized" }); } --- Implementation at this stage will be dependant on your business requirements.

Administration
====================
* [User management](user-management.html)

Audit log collection
====================
With a simple configuration change, you can configure your PDPs to securely send audit logs to Cerbos Hub. This vastly simplifies the work that would otherwise be required to configure and deploy a log aggregation solution to securely collect, store and query audit logs from across your fleet.

For embedded PDPs, decision logs can be captured locally using the SDK’s `onDecision` callback. See [ePDP SDK options](deployments-epdp-rules.html#%5Fsdk%5Foptions) for details.

## [](#%5Fenabling%5Fcollection)Enabling collection

To get started, you need to obtain a set of client credentials. Navigate to the **Settings** → **Client credentials** tab of the deployment, click on **Generate a client credential** and generate a **Read & write** credential. Make sure to save the client secret in a safe place as it cannot be recovered.

The client credentials can be provided to the PDP using environment variables or the configuration file. The environment variables to set are:

| CERBOS\_HUB\_CLIENT\_ID     | Client ID                                                                     |
| --------------------------- | ----------------------------------------------------------------------------- |
| CERBOS\_HUB\_CLIENT\_SECRET | Client secret                                                                 |
| CERBOS\_HUB\_PDP\_ID        | Optional. A unique name for the PDP. If not provided, a random value is used. |

Alternatively, you can define these values in the Cerbos configuration file as follows:

```yaml
hub:
  credentials:
    pdpID: "..." # Optional. Identifier for this Cerbos instance.
    clientID: "..." # ClientID
    clientSecret: "..." # ClientSecret
```

To enable audit log collection, configure the `hub` audit log backend with a local storage path. This local storage path is important for preserving the audit logs until they are safely saved to Cerbos Hub. If there are any network interruptions or if the PDP process crashes, the audit logs generated up to that point are saved on disk and will be sent to Cerbos Hub the next time the PDP starts. If you’re using a container orchestrator or a cloud-based solution to deploy Cerbos, attach a persistent storage volume at this path to ensure that the data does not get lost.

```yaml
server:
  httpListenAddr: ":3592" # The port the HTTP server will listen on
  grpcListenAddr: ":3593" # The port the gRPC server will listen on

hub:
  credentials:
    pdpID: "..." # Optional. Identifier for this Cerbos instance.
    clientID: "..." # ClientID
    clientSecret: "..." # ClientSecret

audit:
  enabled: true
  backend: hub
  hub:
    storagePath: "..." # Local storage path for buffering the audit logs.
```

Refer to [Cerbos documentation](../cerbos/latest/configuration/audit.html) for details about common audit configurations that apply to all backends. You can configure an optional secondary output for the audit logs. This is useful for cases where you want to aggregate Cerbos audit logs into an existing silo for compliance and monitoring purposes while still taking advantage of the powerful features provided by Cerbos Hub to view and analyze log entries.

The following snippet demonstrates how to configure a secondary output that writes audit entries to standard output of the container.

```yaml
audit:
  enabled: true
  backend: hub
  hub:
    storagePath: "..." # Local storage path for buffering the audit logs.
    pipeOutput: # Secondary output configuration
      enabled: true
      backend: file # Any supported audit backend can be used here.
  file: # Configuration for the file backend which is used by the pipeOutput configuration above.
    path: stdout
```

| |  To quickly try out the Cerbos Hub audit logs feature, you can use the following command. mkdir -p /tmp/cerbos && docker run --rm --name cerbos \\  \-p 3592:3592 -p 3593:3593 \\  \-e CERBOS\_HUB\_CLIENT\_ID="..." \\  \-e CERBOS\_HUB\_CLIENT\_SECRET="..." \\  \-v /tmp/cerbos:/audit\_logs \\  ghcr.io/cerbos/cerbos:latest server \\ \--set=audit.enabled=true \\ \--set=audit.backend=hub \\ \--set=audit.hub.storagePath=/audit\_logs |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#%5Faccessing%5Fthe%5Flogs)Accessing the logs

Once collection is enabled, the logs can accessed via the _Audit logs_ tab in Cerbos Hub. From here you can select which logs to view:

### [](#%5Fdecision%5Flogs)Decision logs

The decision logs are records of the authorization decisions made by the Cerbos PDP. These logs provide detailed information about each decision, including the inputs, Cerbos policies evaluated, and the `ALLOW/DENY` decisions along with any outputs from rule evaluation. Besides providing a comprehensive audit trail, these records can be used for troubleshooting purposes and to understand how Cerbos policies are used within your organization.

The log list displays each entry with the timestamp, call ID, request kind (`CheckResources` or `PlanResources`), principal ID, resource kind, resource ID, and action decision. Toggle between the **Decision** view for a compact summary or **JSON** view for raw log data.

#### [](#%5Flog%5Fentry%5Fdetails)Log entry details

Click on any log entry to open the details panel, which shows:

* **Principal**: The user or service that made the request, including their ID, roles, effective derived roles, and any attributes.
* **Resource**: The resource being accessed, including kind, ID, scope, and attributes.
* **Decisions**: The authorization outcome for each action, showing the effect (`ALLOW` or `DENY`) and which policy produced the decision.
* **Outputs**: Any output values returned by policy rules.
* **Raw JSON**: The complete log entry in JSON format.

#### [](#%5Fdeep%5Flinking%5Fto%5Fpolicies)Deep linking to policies

Policy names in audit log entries are clickable links. Click any policy name in the Decisions section to navigate directly to that policy in your policy store. This makes it easy to investigate authorization decisions and understand the policy logic behind each outcome without manually searching for the relevant policy file.

#### [](#%5Ffiltering)Filtering

Filter the logs by time range, PDP ID, principal, resource kind, action, or policy decision to find specific entries.

### [](#%5Faccess%5Flogs)Access logs

![Access logs](_images/audit_log_access.png)

The access logs are records of all the API requests received by the Cerbos PDP. The valid `CheckResources` and `PlanResources` API calls would have a corresponding decision log entry with the the same call ID. API requests that are invalid or unauthenticated are logged as well and can be used for identifying misconfigured clients or unauthorized access attempts.

You can filter the logs by a particular PDP and a time range.

## [](#%5Fmasking%5Fsensitive%5Ffields)Masking sensitive fields

You can define masks to filter out sensitive or personally identifiable information (PII) that might be included in the audit log entries. Masked fields are removed locally at the PDP and are never transmitted to Cerbos Hub.

Masks are defined using a subset of JSONPath syntax.

```yaml
hub:
  credentials:
    pdpID: "..." # Optional. Identifier for this Cerbos instance.
    clientID: "..." # ClientID
    clientSecret: "..." # ClientSecret

audit:
  enabled: true
  backend: hub
  hub:
    storagePath: "..." # Local storage path for buffering the audit logs.
    mask:
      # Fields to mask from CheckResources requests
      checkResources:
        - inputs[*].principal.attr.foo
        - inputs[*].auxData
        - outputs
      # Fields to mask from the metadata
      metadata:
        - authorization
      # Fields to mask from the peer information
      peer:
        - address
        - forwarded_for
      # Fields to mask from the PlanResources requests.
      planResources:
        - input.principal.attr.nestedMap.foo
```

| |  Use the [local audit backend](../cerbos/latest/configuration/audit.html#local) along with [cerbosctl audit commands](../cerbos/latest/cli/cerbosctl.html#audit) to inspect your audit logs locally and determine the paths that need to be masked. |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| |  In order to avoid slowing down request processing and to avoid any data losses, raw log entries are stored locally on disk at the storage path. The masks are applied later by the background process that syncs the on-disk log entries to Cerbos Hub. To avoid storing authentication tokens and other sensitive request parameters locally, use the top-level includeMetadataKeys and excludeMetadataKeys settings. Refer to [Cerbos audit configuration](../cerbos/latest/configuration/audit.html) for more details. |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#%5Fadvanced%5Fconfiguration)Advanced configuration

Advanced users can tune the local log retention period and other buffering settings. We generally do not recommend changing the default values unless absolutely necessary.

```yaml
audit:
  enabled: true
  backend: hub
  hub:
    storagePath: "..." # Local storage path for buffering the audit logs.
    retentionPeriod: 168h # How long to keep buffered records on disk.
    advanced:
      bufferSize: 16 # Size of the memory buffer. Increasing this will use more memory and the chances of losing data during a crash.
      maxBatchSize: 16 # Write batch size. If your records are small, increasing this will reduce disk IO.
      flushInterval: 30s # Time to keep records in memory before committing.
      gcInterval: 15m # How often the garbage collector runs to remove old entries from the log.
```

Concepts
====================
Client credentials

Used to establish an authenticated connection to Cerbos Hub using a client ID and a secret. Client credentials are scoped to either a deployment or a policy store, and can be read-only or read and write. They can be created from the **Client credentials** tab on any deployment or policy store detail page.

Deployment

A deployment is a specific configuration of policy stores (such as ‘production’ or ‘staging’) that can be connected to a set of PDPs. Each new change to the underlying store(s) results in a new policy build that’s automatically delivered to the PDPs if the tests are successful.

Organization

An Organization serves as the top-level entity in Cerbos Hub and provides centralized control over billing, access control, and Workspace management. Typically a business would have one Organization and a number of Workspaces underneath it.

Policy bundle

An encrypted file containing optimized binary representations of policies. When policies change in a policy store, Cerbos Hub validates the policies, runs any tests, and produces a policy bundle that is pushed to all connected PDPs assigned to that deployment. Bundles are versioned, allowing you to track exactly which policies were in effect at any point in time.

Policy Decision Point (PDP)

A component that evaluates authorization requests against policies. Cerbos Hub supports two types of PDPs:

Service PDP

The open source Cerbos PDP instances that you run in your own infrastructure. Cerbos Hub pushes pre-compiled policy bundles to service PDPs, ensuring all your data remains within your network perimeter while reducing the overhead of policy updates. See [Service PDPs](decision-points.html).

Embedded PDP

A WebAssembly module that executes authorization logic locally within an application, without network calls to a Cerbos server. Embedded PDPs are suited for browser applications, edge functions, mobile apps, and other environments where latency or connectivity constraints make server-side authorization impractical. Each deployment can define multiple ePDP rules with independent policy filtering, authentication requirements, and IP allowlists. See [Embedded PDPs](deployments-epdp-rules.html).

Policy playground

A browser-based policy editor to quickly prototype, test, and collaborate on Cerbos policies. Features include execution traces for debugging, a permissions matrix view for visualizing access patterns, and real-time collaborative editing. You can create playgrounds from scratch, from templates, or from existing policy stores. See [Playgrounds](playground.html).

Policy store

A versioned, cloud-based storage container for Cerbos policies. A policy store can be either linked to a supported git provider for automatic mirroring or managed manually using the Cerbos Hub user interface, Cerbos Hub SDKs or the [cerbosctl](../cerbos/latest/cli/cerbosctl.html) utility. Multiple stores can be connected to a single deployment, making it easy to manage policies by teams or tenants or any other desired level of organization and combine them all at deployment time to distribute to PDPs.

Workspace

A Workspace encompasses a set of users, policy stores, deployments, and playgrounds to help organize your work by teams, departments, tenants, or any other desired form of separating responsibilities.

ePDP rule

A configuration within a deployment that defines how embedded PDP bundles are built and served. Each rule specifies policy filtering criteria (resources, actions, scopes, roles, versions), authentication requirements, and IP allowlists. A deployment can have multiple ePDP rules for different clients or use cases. See [ePDP rules](deployments-epdp-rules.html).

Service Policy Decision Points
====================
Service policy decision points (PDPs) are open source Cerbos instances running in your infrastructure, managed by Cerbos Hub. Cerbos Hub acts as a control plane for your PDP fleet, handling policy compilation, testing, and distribution so your PDPs can focus on serving authorization requests.

### [](#%5Fwhy%5Fuse%5Fcerbos%5Fhub%5Ffor%5Fpdps)Why use Cerbos Hub for PDPs?

Without Cerbos Hub, each PDP must independently detect policy changes, fetch source files, parse, compile, and load them. This creates operational overhead and can lead to version drift across your fleet.

With Cerbos Hub:

| Pre-compiled bundles        | Policies are compiled once by Cerbos Hub and pushed as optimized bundles. PDPs skip parsing and compilation entirely, reducing startup time and memory usage.                           |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Instant fleet-wide updates  | Push-based distribution means all PDPs receive updates within seconds—no polling delays or staggered rollouts.                                                                          |
| Validated before deployment | Policies are tested automatically before distribution. Failed tests block deployment, preventing broken policies from reaching production.                                              |
| Centralized visibility      | Monitor all connected PDPs from a single dashboard. See which version each instance is running, when it last connected, and access its audit logs.                                      |
| Built-in resilience         | PDPs cache bundles locally and continue operating if Cerbos Hub is temporarily unavailable. New instances can start from cached bundles served by a high-availability fallback service. |

For environments where running a Cerbos server is impractical, such as browser applications or edge functions, see [Embedded PDPs](deployments-epdp-rules.html).

## [](#%5Fwhen%5Fto%5Fuse%5Fservice%5Fpdps)When to use service PDPs

Service PDPs are the standard deployment model for server-side authorization. Use them when:

### [](#%5Fbackend%5Fservices)Backend services

API servers, microservices, and backend applications that need to authorize requests. The PDP runs alongside your application and responds to authorization checks with sub-millisecond latency.

### [](#%5Fcentralized%5Fauthorization)Centralized authorization

Organizations that want a dedicated authorization service that multiple applications can query. Deploy one or more PDPs and have all services send authorization requests to them.

### [](#%5Fhigh%5Fvolume%5Fworkloads)High-volume workloads

Service PDPs handle thousands of authorization checks per second. The compiled policy format and in-memory evaluation ensure consistent performance under load.

### [](#%5Fdata%5Fsensitive%5Fenvironments)Data-sensitive environments

All authorization data stays within your network. Cerbos Hub only pushes policy bundles—your request data, principal attributes, and resource attributes never leave your infrastructure.

## [](#%5Fhow%5Fit%5Fworks)How it works

When a PDP connects to Cerbos Hub, it establishes a two-way communication channel:

1. The PDP authenticates using client credentials scoped to a deployment
2. Cerbos Hub pushes the current policy bundle to the PDP
3. The PDP loads the bundle and begins serving authorization requests
4. When policies change, Cerbos Hub pushes a notification to all connected PDPs
5. Each PDP downloads and activates the new bundle

Because there is no polling, all PDPs converge on the same policy version within seconds of a change.

## [](#%5Fdeployment%5Fpatterns)Deployment patterns

Cerbos supports multiple deployment patterns depending on your requirements.

### [](#%5Fservice%5Fmodel)Service model

A central Cerbos deployment shared by multiple applications.

* Cerbos can be upgraded independently from applications
* Simpler policy management with a single point of control
* Requires capacity planning to avoid bottlenecks

### [](#%5Fsidecar%5Fmodel)Sidecar model

Each application instance gets its own Cerbos container.

* High performance with no network overhead between application and PDP
* Upgrades require rolling updates to all application instances
* Policy updates propagate to each sidecar independently

Cerbos supports serving the API over a Unix domain socket, allowing secure communication with no network overhead. See [Kubernetes sidecar deployment](../cerbos/latest/deployment/k8s-sidecar.html) for details.

### [](#%5Fdaemonset%5Fmodel)DaemonSet model

Each Kubernetes node gets one Cerbos instance, shared by all pods on that node.

* Efficient resource usage compared to sidecars
* Lower latency than centralized service
* Policy updates roll out node by node

See [Kubernetes DaemonSet deployment](../cerbos/latest/deployment/k8s-daemonset.html) for configuration details.

## [](#%5Fdeploying%5Fa%5Fpdp)Deploying a PDP

A PDP requires three pieces of configuration to connect to Cerbos Hub:

| Deployment ID | Identifies which deployment’s policies to load |
| ------------- | ---------------------------------------------- |
| Client ID     | Authentication credential                      |
| Client secret | Authentication credential                      |

These can be configured via environment variables or a configuration file.

### [](#%5Fenvironment%5Fvariables)Environment variables

The simplest method to get a connected PDP running:

```shell
docker run --rm --name cerbos \
  -p 3592:3592 -p 3593:3593 \
  -e CERBOS_HUB_DEPLOYMENT_ID="..." \
  -e CERBOS_HUB_CLIENT_ID="..." \
  -e CERBOS_HUB_CLIENT_SECRET="..." \
  -e CERBOS_HUB_PDP_ID="..." \
  ghcr.io/cerbos/cerbos:latest server
```

| CERBOS\_HUB\_DEPLOYMENT\_ID | The deployment ID to load policies from. Find this on the deployment page in Cerbos Hub.                                  |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| CERBOS\_HUB\_CLIENT\_ID     | Client ID from the deployment’s **Client credentials** tab.                                                               |
| CERBOS\_HUB\_CLIENT\_SECRET | Client secret from the deployment’s **Client credentials** tab.                                                           |
| CERBOS\_HUB\_PDP\_ID        | Optional. A name for this PDP instance, shown in the Cerbos Hub monitoring page. If not provided, a random value is used. |

### [](#%5Fconfiguration%5Ffile)Configuration file

For production deployments, use a configuration file:

```yaml
server:
  httpListenAddr: ":3592"
  grpcListenAddr: ":3593"

hub:
  credentials:
    pdpID: "payments-service-1" # Optional. Identifier for this PDP instance.
    clientID: "..."
    clientSecret: "..."

storage:
  driver: hub
  hub:
    remote:
      deploymentID: "..." # The deployment ID to load policies from
```

Start the PDP with the configuration file:

```shell
docker run --rm --name cerbos \
  -v $(pwd):/conf \
  -p 3592:3592 -p 3593:3593 \
  ghcr.io/cerbos/cerbos:latest server --config=/conf/.cerbos.yaml
```

See [Configuration](../cerbos/latest/configuration/index.html) for the full configuration reference.

### [](#%5Fobtaining%5Fcredentials)Obtaining credentials

To generate client credentials:

1. Navigate to the deployment in Cerbos Hub
2. Select the **Client credentials** tab
3. Click **Generate a client credential**
4. Choose **Read only** for PDPs that only need to receive bundles
5. Save the client secret—it cannot be recovered after creation

## [](#%5Fproduction%5Fdeployment)Production deployment

Cerbos runs anywhere containers run: Kubernetes, Docker Compose, Amazon ECS, systemd, or directly as a binary. The examples below focus on Kubernetes as the most common deployment target.

For other platforms, see [Cloud platform deployment](../cerbos/latest/deployment/cloud-platforms.html) (AWS Marketplace, Fly.io) and [systemd deployment](../cerbos/latest/deployment/systemd.html).

### [](#%5Fkubernetes)Kubernetes

#### [](#%5Fhelm)Helm

Create a secret for the Hub credentials:

```shell
kubectl create secret generic cerbos-hub-credentials \
  --from-literal=CERBOS_HUB_CLIENT_ID="..." \
  --from-literal=CERBOS_HUB_CLIENT_SECRET="..." \
  --from-literal=CERBOS_HUB_DEPLOYMENT_ID="..."
```

Create a values file (`hub-values.yaml`):

```yaml
cerbos:
  config:
    audit:
      enabled: true
      backend: hub
      hub:
        storagePath: /audit_logs

envFrom:
  - secretRef:
      name: cerbos-hub-credentials

volumes:
  - name: cerbos-audit-logs
    emptyDir: {}

volumeMounts:
  - name: cerbos-audit-logs
    mountPath: /audit_logs
```

Deploy with Helm:

```shell
helm repo add cerbos https://download.cerbos.dev/helm-charts
helm install cerbos cerbos/cerbos --values=hub-values.yaml
```

| |  For AWS Marketplace (EKS/ECS), the Helm chart handles metering automatically. See [Cloud platform deployment](../cerbos/latest/deployment/cloud-platforms.html) for setup instructions. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#%5Freliability)Reliability

Cerbos Hub is designed for high availability. However, if Cerbos Hub becomes temporarily unavailable:

* **Running PDPs** continue serving requests using the last downloaded bundle while attempting to reconnect in the background
* **New PDPs** can start with the last successfully built bundle, served from a separate high-availability service

### [](#%5Flocal%5Fbundle%5Fcaching)Local bundle caching

For additional resilience, configure a cache directory to persist bundles to disk:

```yaml
storage:
  driver: hub
  hub:
    remote:
      deploymentID: "..."
      cacheDir: /var/cerbos/hub # Directory to cache downloaded bundles
```

Mount a persistent volume at this path when running in containers or Kubernetes.

### [](#%5Foffline%5Fmode)Offline mode

In disaster recovery scenarios, start the PDP with the cached bundle:

```shell
docker run --rm --name cerbos \
  -p 3592:3592 -p 3593:3593 \
  -e CERBOS_HUB_OFFLINE=true \
  -v /var/cerbos/hub:/var/cerbos/hub \
  ghcr.io/cerbos/cerbos:latest server --config=/conf/.cerbos.yaml
```

The PDP loads the cached bundle and serves requests without connecting to Cerbos Hub.

### [](#%5Ffallback%5Fto%5Fgit)Fallback to git

As a last resort, switch the PDP to use the git storage driver and read policies directly from your policy repository:

```yaml
storage:
  driver: git
  git:
    protocol: https
    url: https://github.com/your-org/policies.git
    branch: main
    checkoutDir: /tmp/cerbos/policies
    updatePollInterval: 60s
```

## [](#%5Fhealth%5Fchecks)Health checks

Cerbos exposes health check endpoints for container orchestrators and load balancers.

### [](#%5Fhttp%5Fhealth%5Fendpoint)HTTP health endpoint

```none
GET /_cerbos/health
```

Returns HTTP 200 when the PDP is healthy and ready to serve requests.

### [](#%5Fgrpc%5Fhealth)gRPC health

Cerbos implements the standard gRPC health checking protocol on port 3593.

### [](#%5Fkubernetes%5Fprobes)Kubernetes probes

Configure liveness and readiness probes:

```yaml
livenessProbe:
  httpGet:
    path: /_cerbos/health
    port: 3592
  initialDelaySeconds: 5
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /_cerbos/health
    port: 3592
  initialDelaySeconds: 5
  periodSeconds: 10
```

## [](#%5Fmonitoring)Monitoring

### [](#%5Fconnected%5Fpdps)Connected PDPs

The **Decision points** tab on each deployment page shows all recently connected PDP instances:

* **PDP ID**: The identifier for the instance
* **Build**: Which policy bundle version is active
* **Sessions**: Number of active connections
* **Cerbos version**: The PDP software version
* **Last seen**: When the PDP last communicated with Cerbos Hub
* **Audit logs**: Link to view audit logs from this PDP

### [](#%5Fprometheus%5Fmetrics)Prometheus metrics

Cerbos exposes metrics at `/_cerbos/metrics` in Prometheus format.

Monitor PDP connectivity using the `cerbos_dev_hub_connected` gauge:

| 1 | PDP is connected to Cerbos Hub            |
| - | ----------------------------------------- |
| 0 | PDP is disconnected (using cached bundle) |

Additional metrics for Hub connectivity:

| cerbos\_dev\_store\_bundle\_updates\_count | Number of bundle updates received from Cerbos Hub |
| ------------------------------------------ | ------------------------------------------------- |
| cerbos\_dev\_store\_bundle\_op\_latency    | Time to perform bundle operations                 |

See [Observability](../cerbos/latest/configuration/observability.html) for the full list of available metrics.

## [](#%5Frelated%5Ffeatures)Related features

| [Audit log collection](audit-log-collection.html)                    | Send authorization decision logs from PDPs to Cerbos Hub for analysis and compliance. |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| [Deployments](deployments.html)                                      | Configure which policy stores contribute to a deployment and view build history.      |
| [Policy stores](policy-stores.html)                                  | Manage the policy repositories that feed into deployments.                            |
| [Cerbos deployment patterns](../cerbos/latest/deployment/index.html) | Detailed guides for service, sidecar, and DaemonSet deployment models.                |

Embedded Policy Decision Points
====================
Embedded policy decision points (ePDPs) execute authorization logic locally using WebAssembly, without requiring network calls to a Cerbos PDP. Policy bundles are downloaded from Cerbos Hub and evaluated in-process by a WASM runtime.

For server-side authorization using the open source Cerbos PDP, see [Service PDPs](decision-points.html).

## [](#%5Fwhen%5Fto%5Fuse%5Fembedded%5Fpdps)When to use embedded PDPs

ePDPs address scenarios where server-side authorization is impractical due to latency, connectivity, or architectural constraints.

### [](#%5Fbrowser%5Fapplications)Browser applications

Web applications often need to make authorization decisions to determine which UI elements to render. A document editor might show or hide the "Delete" button based on whether the current user has permission to delete the document. Making a network request for each visibility check introduces latency and creates a dependency on backend availability.

With an ePDP, the browser downloads a policy bundle once and evaluates all permission checks locally. The bundle updates automatically when policies change, and the application continues to function if the network is temporarily unavailable.

### [](#%5Fedge%5Fcomputing)Edge computing

Edge functions and CDN workers operate in environments where round-trips to origin servers are expensive. An edge function that needs to authorize a request before proxying it to the backend can evaluate policies locally, reducing total request latency.

### [](#%5Fmobile%5Fapplications)Mobile applications

Mobile applications operate with intermittent connectivity. An ePDP allows the application to make authorization decisions while offline, using the most recently downloaded policy bundle. When connectivity is restored, the bundle updates automatically.

React Native applications can use the JavaScript SDK today. Native iOS and Android SDK support is planned.

### [](#%5Fserverless%5Ffunctions)Serverless functions

Serverless functions incur cold start latency when loading external dependencies. An ePDP embedded in the function bundle eliminates the need for network calls to an authorization service during function execution.

## [](#%5Fepdp%5Frules)ePDP rules

An ePDP rule defines:

* Which subset of policies to include in the bundle
* Under what conditions the bundle can be accessed
* What security controls apply to bundle downloads

Each deployment can have multiple ePDP rules. This allows different bundle configurations for different clients or environments. For example:

* A rule serving a minimal bundle for browser clients, containing only UI-relevant policies
* A rule serving a full bundle for edge workers, containing all policies
* A rule per tenant in a multi-tenant application, each filtered to that tenant’s scope

### [](#%5Fcreating%5Fa%5Frule)Creating a rule

To create an ePDP rule:

1. Navigate to the [deployment](deployments.html) in Cerbos Hub
2. Select the **Embedded PDP rules** tab
3. Click **Create rule**
4. Enter a unique name for the rule
5. Configure access control and policy bundle filtering options
6. Click **Save rule**

After saving, the rule appears in the list with its rule ID displayed. Click **Copy** next to the rule ID to copy it for use in your client application.

### [](#%5Fenabling%5Fand%5Fdisabling%5Frules)Enabling and disabling rules

Each rule has an enabled/disabled toggle. Disabled rules cannot serve bundles. Requests for a disabled rule’s bundle return an error.

To disable a rule, toggle the switch on the rule card. A confirmation dialog appears before the rule is disabled.

Use this to:

* Temporarily suspend access to a bundle without deleting the rule configuration
* Prepare a rule configuration before making it available to clients
* Revoke access in response to a security concern

### [](#%5Fmanaging%5Frules)Managing rules

Each rule card provides actions:

| Edit      | Modify the rule configuration.                                                                     |
| --------- | -------------------------------------------------------------------------------------------------- |
| Duplicate | Create a new rule with the same configuration. Useful for creating variations of an existing rule. |
| Delete    | Permanently remove the rule. A confirmation dialog appears before deletion.                        |

## [](#%5Ffiltering%5Fpolicies)Filtering policies

By default, an ePDP bundle contains all policies from the deployment. Filters reduce the bundle to only the policies required by the client application.

Filtering serves two purposes:

| Performance | Smaller bundles download faster and consume less memory. A browser application checking permissions on three resource types does not need policies for the fifty other resource types in the system. |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Security    | Bundles may be served to environments you do not fully control, such as end-user browsers. Filtering prevents exposure of server-side authorization logic that clients do not need.                  |

Filters are applied when the bundle is requested. The source policies in the deployment are not modified.

### [](#%5Fresources%5Fand%5Factions)Resources and actions

The **Resources and actions** setting specifies which authorization rules to include based on the resource types and actions they govern.

If no filter entries are defined, all resources and actions are included.

Click **Add filter entry** to create a filter. Each entry can specify:

* Resources only: Include all rules for the specified resource types, regardless of action
* Actions only: Include all rules for the specified actions, regardless of resource type
* Both: Include only rules matching both the specified resources and actions

Multiple filter entries can be defined. The resulting bundle includes rules matching any of the entries.

Example: Browser application

A browser application checks three permissions:

* `document:view`
* `document:edit`
* `folder:view`

Configure two filter entries:

1. Resources: `document`, Actions: `view`, `edit`
2. Resources: `folder`, Actions: `view`

The bundle includes only the rules necessary for these checks. Rules governing `document:delete`, `folder:create`, or other resource types are excluded.

Example: Action-based filter

An application checks the `view` action across many resource types but never checks `delete` or `admin` actions.

Configure one filter entry:

* Actions: `view`

The bundle includes `view` rules for all resource types, excluding rules for other actions.

### [](#%5Fscopes)Scopes

Scope filtering supports multi-tenant architectures and hierarchical permission structures.

Cerbos policies can be scoped to specific contexts. A policy with scope `acme.eu` applies only when requests specify that scope or a descendant scope like `acme.eu.prod`. Scope filtering determines which scoped policies appear in the bundle.

The **Scopes** setting offers three options:

| All                                  | Include policies for all scopes. No filtering is applied.                                                                        |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| Specific                             | Include policies matching specified scope patterns. Configure this in the rule definition.                                       |
| Require specific scope at fetch time | Require clients to specify scopes when downloading the bundle. The bundle is filtered dynamically based on the requested scopes. |

#### [](#%5Fstatic%5Fscopes%5Fspecific)Static scopes (Specific)

Select **Specific** and enter scope patterns in the rule definition. The bundle includes policies matching those patterns.

Use static scopes when:

* The set of scopes is small and known in advance
* All clients using this rule need the same scopes
* Scopes do not change frequently

Example

A rule serving bundles for European customers specifies scope pattern `acme.eu`. The bundle includes:

* Policies with scope `acme.eu`
* Policies with scope `acme` (ancestor)
* Policies with no scope (root)

Policies scoped to `acme.us` or `acme.ap` are excluded.

#### [](#%5Fdynamic%5Fscopes)Dynamic scopes

Select **Require specific scope at fetch time** to require clients to specify scopes when downloading the bundle. The bundle is filtered to the requested scopes on each request.

| |  If the rule has scope patterns configured, the scopes requested by clients must match one of those patterns. Requests for scopes outside the allowed patterns are rejected. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

Use dynamic scopes when:

* The set of scopes is large, such as one scope per customer tenant
* Scopes change frequently as tenants are added or removed
* Different clients need different scopes from the same rule

Example

A multi-tenant application has thousands of customer tenants, each with a unique scope like `tenant-a`, `tenant-b`, etc. Rather than creating thousands of ePDP rules, create one rule with dynamic scopes enabled.

When client code initializes:

```typescript
const cerbos = new Embedded({
  policies: {
    ruleId: "<RULE_ID>",
    scopes: [currentTenant.scopeId],
  },
  wasm,
});
```

The bundle returned contains only policies applicable to that tenant’s scope.

#### [](#%5Fscope%5Fhierarchy)Scope hierarchy

When a scope is requested, ancestor scopes are included automatically.

Requesting scope `acme.eu.prod` includes policies for:

* `acme.eu.prod` (exact match)
* `acme.eu` (parent)
* `acme` (grandparent)
* Root scope (no scope specified)

This ensures that inherited policies from parent scopes are available for evaluation.

### [](#%5Froles)Roles

The **Roles** setting specifies which roles to include. Select **Specific** and enter role names to filter. Only rules referencing the specified roles are included in the bundle.

If set to **All**, all roles are included.

Example

A browser application is used only by users with `viewer` or `editor` roles. Administrative actions are performed through a separate interface.

Configure role filter: `viewer`, `editor`

The bundle excludes rules that apply only to `admin` or other roles, reducing bundle size and avoiding exposure of administrative authorization logic.

### [](#%5Fversions)Versions

The **Versions** setting specifies which policy versions to include. Select **Specific** and enter version identifiers to filter.

Cerbos policies support versioning, allowing different rule sets for different API versions or feature flags. If your policies use versions, you can filter the bundle to include only the versions relevant to the client.

If set to **All**, all versions are included.

Example

An application has migrated from policy version `v1` to `v2`, but some legacy clients still use `v1`.

* Rule for modern clients: version filter `v2`
* Rule for legacy clients: version filter `v1`

## [](#%5Fsecurity%5Fcontrols)Security controls

ePDP bundles contain compiled authorization logic. Depending on your security requirements, this logic may need protection from unauthorized access.

### [](#%5Fthreat%5Fmodel)Threat model

Consider what is exposed if an ePDP bundle is obtained by an unauthorized party:

* **Policy structure**: Which resource types and actions exist in the system
* **Authorization rules**: The conditions under which access is granted or denied
* **Role definitions**: Which roles exist and what permissions they grant
* **Attribute checks**: Which principal and resource attributes influence decisions

For some applications, this information is not sensitive. A publicly documented API with straightforward role-based access control may have no authorization logic worth protecting.

For other applications, authorization rules are proprietary or security-sensitive. An attacker studying the rules might identify edge cases to exploit or gain insight into system architecture.

Evaluate your requirements and apply controls accordingly.

### [](#%5Fauthentication)Authentication

The **Authentication** setting controls whether credentials are required to download bundles.

| Public access     | Bundles are served without authentication. Any client with the rule ID can download the bundle.                                                                                                                                                                                                         |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Client credential | Clients must provide valid credentials to download bundles. Credentials are a [client ID and client secret](concepts.html#%5Fclient%5Fcredentials), issued from the deployment’s **Client credentials** tab in Cerbos Hub. These are the same credentials used by [service PDPs](decision-points.html). |

#### [](#%5Fbrowser%5Fapplications%5F2)Browser applications

Client credentials must not be exposed to end users. Browser JavaScript is readable by users, and credentials embedded in client-side code are not secret.

For browser applications requiring authenticated bundles:

| Backend-for-frontend  | Your server fetches the bundle using credentials and serves it to the browser. The browser never sees the credentials.         |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Server-side rendering | Evaluate permissions on the server and send only the results to the browser. The browser does not load the ePDP bundle at all. |
| Accept public bundles | If the authorization logic is not sensitive, disable authentication and serve bundles directly to browsers.                    |

#### [](#%5Fserver%5Fside%5Fapplications)Server-side applications

Node.js servers, edge workers with secret storage, and other server-side environments can safely use credentials. Store credentials in environment variables or a secrets manager, not in source code.

### [](#%5Fip%5Fallowlist)IP allowlist

The **IP allowlist** specifies CIDR ranges permitted to download bundles. Requests from IP addresses outside these ranges are rejected, regardless of authentication status.

Both IPv4 and IPv6 ranges are supported.

__Table 1\. Examples__
| CIDR            | Description                                             |
| --------------- | ------------------------------------------------------- |
| 203.0.113.0/24  | Single IPv4 /24 block                                   |
| 203.0.113.42/32 | Single IPv4 address                                     |
| 2001:db8::/32   | IPv6 block                                              |
| 0.0.0.0/0       | All IPv4 addresses (effectively disables the allowlist) |

Use the IP allowlist to:

* Limit bundle access to your corporate network
* Restrict access to known CDN or edge provider IP ranges
* Add defense-in-depth alongside authentication

The IP allowlist applies to the bundle download request, not to subsequent policy evaluations. Once a client has downloaded a bundle, it can evaluate policies from any network location.

## [](#%5Fjavascript%5Fsdk)JavaScript SDK

The [@cerbos/embedded-client](https://www.npmjs.com/package/@cerbos/embedded-client) package provides a client for loading and evaluating ePDP bundles in JavaScript environments.

### [](#%5Finstallation)Installation

```bash
npm install @cerbos/embedded-client @cerbos/embedded-server
```

The `@cerbos/embedded-server` package contains the WebAssembly module that executes policy evaluation.

### [](#%5Finitializing%5Fthe%5Fclient)Initializing the client

The client requires two inputs:

| policies | Source of the policy bundle, typically a rule ID pointing to Cerbos Hub |
| -------- | ----------------------------------------------------------------------- |
| wasm     | Source of the WebAssembly module                                        |

```typescript
import { Embedded } from "@cerbos/embedded-client";
import wasm from "@cerbos/embedded-server/server.wasm?init";

const cerbos = new Embedded({
  policies: { ruleId: "<RULE_ID>" },
  wasm,
});
```

Replace `<RULE_ID>` with the rule ID from the Embedded PDP rules tab in Cerbos Hub.

The client begins downloading the policy bundle immediately upon construction. The first authorization check waits for the download to complete.

### [](#%5Fchecking%5Fpermissions)Checking permissions

The client provides several methods for authorization checks.

#### [](#%5Fisallowed)isAllowed

Check if a single action is allowed:

```typescript
const allowed = await cerbos.isAllowed({
  principal: {
    id: "user-123",
    roles: ["editor"],
    attr: {
      department: "engineering",
      clearanceLevel: 3,
    },
  },
  resource: {
    kind: "document",
    id: "doc-456",
    attr: {
      owner: "user-789",
      confidential: false,
    },
  },
  action: "edit",
});

if (allowed) {
  // Show edit button
}
```

#### [](#%5Fcheckresource)checkResource

Check multiple actions on a single resource:

```typescript
const result = await cerbos.checkResource({
  principal: {
    id: "user-123",
    roles: ["editor"],
  },
  resource: {
    kind: "document",
    id: "doc-456",
  },
  actions: ["view", "edit", "delete", "share"],
});

const canView = result.isAllowed("view");
const canEdit = result.isAllowed("edit");
const canDelete = result.isAllowed("delete");
const canShare = result.isAllowed("share");
```

#### [](#%5Fcheckresources)checkResources

Check actions across multiple resources:

```typescript
const result = await cerbos.checkResources({
  principal: {
    id: "user-123",
    roles: ["editor"],
  },
  resources: [
    {
      resource: { kind: "document", id: "doc-1" },
      actions: ["view", "edit"],
    },
    {
      resource: { kind: "document", id: "doc-2" },
      actions: ["view", "edit"],
    },
    {
      resource: { kind: "folder", id: "folder-1" },
      actions: ["view"],
    },
  ],
});

const canEditDoc1 = result.isAllowed({
  resource: { kind: "document", id: "doc-1" },
  action: "edit",
});
```

#### [](#%5Fplanresources)planResources

Generate a query plan for filtering resources:

```typescript
const plan = await cerbos.planResources({
  principal: {
    id: "user-123",
    roles: ["editor"],
  },
  resource: { kind: "document" },
  action: "view",
});

switch (plan.kind) {
  case "KIND_ALWAYS_ALLOWED":
    // User can view all documents
    break;
  case "KIND_ALWAYS_DENIED":
    // User cannot view any documents
    break;
  case "KIND_CONDITIONAL":
    // User can view documents matching plan.condition
    break;
}
```

### [](#%5Fauthenticated%5Faccess)Authenticated access

When the rule uses **Client credential** authentication, provide credentials:

```typescript
import { Embedded } from "@cerbos/embedded-client";
import wasm from "@cerbos/embedded-server/server.wasm?init";

const cerbos = new Embedded({
  policies: {
    ruleId: "<RULE_ID>",
    credentials: {
      clientId: process.env.CERBOS_HUB_CLIENT_ID,
      clientSecret: process.env.CERBOS_HUB_CLIENT_SECRET,
    },
  },
  wasm,
});
```

The `credentialsFromEnv` helper reads credentials from standard environment variables:

```typescript
import { Embedded } from "@cerbos/embedded-client";
import { credentialsFromEnv } from "@cerbos/hub";
import wasm from "@cerbos/embedded-server/server.wasm?init";

const cerbos = new Embedded({
  policies: {
    ruleId: "<RULE_ID>",
    credentials: credentialsFromEnv(),
  },
  wasm,
});
```

This reads `CERBOS_HUB_CLIENT_ID` and `CERBOS_HUB_CLIENT_SECRET` from `process.env`.

### [](#%5Fdynamic%5Fscopes%5F2)Dynamic scopes

When the rule uses **Require specific scope at fetch time**, specify scopes when creating the client:

```typescript
const cerbos = new Embedded({
  policies: {
    ruleId: "<RULE_ID>",
    scopes: ["tenant-acme.department-eng", "tenant-acme.department-sales"],
  },
  wasm,
});
```

The bundle returned includes only policies applicable to the specified scopes and their ancestors. In this example, the bundle includes policies for `tenant-acme.department-eng`, `tenant-acme.department-sales`, `tenant-acme` (shared ancestor), and the root scope.

To change scopes, create a new client instance. Scopes cannot be changed on an existing client.

### [](#%5Fautomatic%5Fbundle%5Fupdates)Automatic bundle updates

The SDK polls Cerbos Hub for bundle updates. When policies change and a new bundle is available, it is downloaded and activated automatically.

The default polling interval is 60 seconds. Configure a different interval:

```typescript
const cerbos = new Embedded({
  policies: {
    ruleId: "<RULE_ID>",
    interval: 300, // Poll every 5 minutes
  },
  wasm,
});
```

The minimum interval is 10 seconds. Values below 10 are increased to 10.

To disable automatic updates, set `interval: 0`. The client uses the bundle downloaded at initialization and never checks for updates.

#### [](#%5Fupdate%5Fnotifications)Update notifications

Register a callback to be notified when updates complete:

```typescript
const cerbos = new Embedded({
  policies: {
    ruleId: "<RULE_ID>",
    onUpdate: (error) => {
      if (error) {
        console.error("Policy update failed:", error);
      } else {
        console.info("Policies updated");
      }
    },
  },
  wasm,
});
```

The callback receives an error object if the update failed, or `undefined` if it succeeded.

Update failures are silent by default. The client continues using the previously loaded bundle. Use the `onUpdate` callback to log failures or trigger alerts.

#### [](#%5Fdeferred%5Factivation)Deferred activation

By default, downloaded updates are activated immediately. To control when updates take effect, use the `PolicyLoader` class directly:

```typescript
import { Embedded, PolicyLoader } from "@cerbos/embedded-client";
import wasm from "@cerbos/embedded-server/server.wasm?init";

const loader = new PolicyLoader({
  ruleId: "<RULE_ID>",
  activateOnLoad: false,
  onUpdate: (error) => {
    if (!error) {
      console.info("New policy bundle ready for activation");
    }
  },
});

const cerbos = new Embedded({
  policies: loader,
  wasm,
});

// Later, when ready to apply the update:
loader.activate();
```

This is useful for:

* Activating updates only on page navigation to avoid layout shifts
* Batching updates with other application state changes
* Implementing user-facing "Refresh policies" functionality

#### [](#%5Fstopping%5Fupdates)Stopping updates

To stop polling for updates:

```typescript
loader.stop();
```

Call this when the client is no longer needed, such as during application shutdown or when navigating away from a page.

### [](#%5Floading%5Fthe%5Fwebassembly%5Fmodule)Loading the WebAssembly module

The WebAssembly module must be loaded and provided to the client. The loading mechanism depends on your build tooling and runtime environment.

#### [](#%5Fvite)Vite

Vite supports WebAssembly imports with the `?init` suffix:

```typescript
import wasm from "@cerbos/embedded-server/server.wasm?init";

const cerbos = new Embedded({
  policies: { ruleId: "<RULE_ID>" },
  wasm,
});
```

#### [](#%5Fwebpack)Webpack

Configure Webpack to handle `.wasm` files as assets, then import:

```typescript
import wasmUrl from "@cerbos/embedded-server/server.wasm";

const cerbos = new Embedded({
  policies: { ruleId: "<RULE_ID>" },
  wasm: wasmUrl,
});
```

Webpack configuration varies by version. Consult the Webpack documentation for WebAssembly handling.

#### [](#%5Frspack)Rspack

Configure Rspack to handle `.wasm` files as `asset/resource`:

```typescript
// rspack.config.ts
export default defineConfig({
  module: {
    rules: [
      {
        test: /\.wasm$/,
        type: "asset/resource",
      },
    ],
  },
});
```

Then import and use the WASM URL:

```typescript
import wasmUrl from "@cerbos/embedded-server/server.wasm";

const cerbos = new Embedded({
  policies: { ruleId: "<RULE_ID>" },
  wasm: wasmUrl,
});
```

#### [](#%5Fnext%5Fjs%5Fturbopack)Next.js (Turbopack)

Next.js with Turbopack does not support direct `.wasm` imports. Copy the WASM binary to the `public/` directory and reference it by URL.

Create a copy script at `scripts/copy-cerbos-wasm.mjs`:

```javascript
import { copyFile, mkdir } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const source = fileURLToPath(
  import.meta.resolve("@cerbos/embedded-server/server.wasm"),
);
const destination = join(
  process.cwd(),
  "public",
  "wasm",
  "cerbos-epdp-server.wasm",
);

await mkdir(dirname(destination), { recursive: true });
await copyFile(source, destination);
```

Add `postinstall` and `prebuild` hooks to `package.json` to run the script automatically:

```json
{
  "scripts": {
    "postinstall": "node scripts/copy-cerbos-wasm.mjs",
    "prebuild": "node scripts/copy-cerbos-wasm.mjs"
  }
}
```

Then pass the public URL to the client:

```typescript
import { Embedded } from "@cerbos/embedded-client";

const cerbos = new Embedded({
  policies: { ruleId: "<RULE_ID>" },
  wasm: "/wasm/cerbos-epdp-server.wasm",
});
```

When `@cerbos/embedded-server` is upgraded, re-run `npm install` (or your package manager’s install command) so the copied WASM binary matches the installed version.

#### [](#%5Fnode%5Fjs)Node.js

Read the module from the filesystem:

```typescript
import { readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import { Embedded } from "@cerbos/embedded-client";

const cerbos = new Embedded({
  policies: { ruleId: "<RULE_ID>" },
  wasm: readFile(
    fileURLToPath(import.meta.resolve("@cerbos/embedded-server/server.wasm")),
  ),
});
```

#### [](#%5Furl)URL

Fetch the module from a URL:

```typescript
const cerbos = new Embedded({
  policies: { ruleId: "<RULE_ID>" },
  wasm: "https://cdn.example.com/cerbos-server.wasm",
});
```

The module is fetched using the Fetch API and compiled using `WebAssembly.instantiateStreaming`.

#### [](#%5Fprecompiled%5Fmodule)Precompiled module

If you have a precompiled `WebAssembly.Module`:

```typescript
const cerbos = new Embedded({
  policies: { ruleId: "<RULE_ID>" },
  wasm: precompiledModule,
});
```

### [](#%5Fconfiguration%5Foptions)Configuration options

| Option               | Default   | Description                                                                                                                                                                      |
| -------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| defaultPolicyVersion | "default" | Policy version applied to requests that do not specify one. Requests can override this per-call.                                                                                 |
| defaultScope         | ""        | Scope applied to requests that do not specify one. Requests can override this per-call.                                                                                          |
| globals              | {}        | Global variables passed to policy conditions. Use this for environment-specific values like feature flags or deployment region.                                                  |
| lenientScopeSearch   | false     | When enabled, if a policy with the exact requested scope is not found, the engine tries ancestor scopes in order. When disabled, the exact scope must exist.                     |
| schemaEnforcement    | NONE      | Validation level for input schemas defined in policies. NONE skips validation. WARN validates and includes errors in the response. REJECT denies the action if validation fails. |
| onDecision           | (none)    | Callback invoked after each authorization decision. Receives a decision log entry containing the request, response, and evaluation metadata. Use for local logging or analytics. |
| decodeJWTPayload     | (throws)  | Function to verify and decode JWTs passed as auxiliary data. Required if your policies reference JWT claims. See the SDK documentation for implementation examples.              |

### [](#%5Ferror%5Fhandling)Error handling

The client throws errors for initialization failures and unrecoverable conditions:

```typescript
import { NotOK, Status } from "@cerbos/core";

try {
  const cerbos = new Embedded({
    policies: { ruleId: "<RULE_ID>" },
    wasm,
  });
  await cerbos.isAllowed({ /* ... */ });
} catch (error) {
  if (error instanceof NotOK) {
    switch (error.code) {
      case Status.UNAUTHENTICATED:
        // Credentials required but not provided, or invalid
        break;
      case Status.PERMISSION_DENIED:
        // IP address not in allowed list
        break;
      case Status.NOT_FOUND:
        // Rule ID does not exist
        break;
      case Status.FAILED_PRECONDITION:
        // Rule is disabled
        break;
      case Status.INVALID_ARGUMENT:
        // Scope parameter required but not provided
        break;
    }
  }
}
```

Authorization check methods (`isAllowed`, `checkResource`, etc.) do not throw for denied permissions. A denied permission is a valid result, not an error.

## [](#%5Fconstraints%5Fand%5Flimitations)Constraints and limitations

### [](#%5Fbundle%5Fupdates)Bundle updates

ePDP bundles are point-in-time snapshots of compiled policies. Changes to policies in Cerbos Hub do not affect already-downloaded bundles until the client downloads an update.

The SDK’s automatic update mechanism handles this for long-running applications. For short-lived processes like serverless functions, each invocation downloads the current bundle.

### [](#%5Ffeature%5Fsupport)Feature support

The WebAssembly runtime supports core Cerbos policy evaluation. Some features available in service PDPs are not supported:

* **Audit logging to external sinks**: Decision logs can be captured via the `onDecision` callback but are not automatically sent to Cerbos Hub or other destinations.
* **Admin API**: The embedded runtime does not expose administrative endpoints.
* **Runtime configuration changes**: Options like `globals` and `schemaEnforcement` are fixed at client initialization.

### [](#%5Fbundle%5Fsize)Bundle size

Bundle size depends on policy complexity:

* Number of resource types, actions, and roles
* Complexity of conditions (CEL expressions)
* Number of scopes
* Schema definitions

For browser applications, monitor bundle size as policies grow. Large bundles increase initial page load time. Use filtering to include only necessary policies.

### [](#%5Fplatform%5Fsupport)Platform support

The JavaScript SDK supports browsers, Node.js, edge runtimes, and React Native. The WebAssembly module executes in any JavaScript host environment.

Native iOS and Android SDK support is planned. For other platforms (Go, Python, etc.), use [service PDPs](decision-points.html).

### [](#%5Fconcurrent%5Faccess)Concurrent access

The `Embedded` client is safe to use concurrently. Multiple authorization checks can be in flight simultaneously.

Creating multiple `Embedded` clients with the same `PolicyLoader` shares the underlying bundle. Updates are applied to all clients sharing the loader.

Deployments
====================
A deployment is a specific configuration of [policy stores](policy-stores.html) (such as 'production' or 'staging') that can be connected to a set of PDPs. Each new change to the underlying store(s) results in a new policy build that’s automatically delivered to the [policy decision points (PDPs)](decision-points.html) if the tests are successful.

Source agnostic inputs

Populate a policy store from any Git provider, CI system, API, CLI, or direct upload, so your existing workflows remain intact.

Multi-store composition

Reference multiple stores in a deployment to separate ownership, for example security team versus product team, or to blend static Git-managed policies with dynamic API-driven rules.

End-to-end automation

Building, testing, and distribution of policies is fully managed by Cerbos Hub, giving you a consistent CI/CD style pipeline for authorization without the need for extra infrastructure.

Strong versioning

Every deployment attempt is attached to a set of immutable policy store versions, making it easy to audit exactly which policies were in effect at any given point in time and to revert any changes if needed.

## [](#%5Fdeployment%5Foverview)Deployment overview

Each deployment page provides several tabs to manage and monitor your policy pipeline:

Builds

View the history of deployed versions, showing which policy bundles have been active and when. Each build shows the contributing policy stores and their versions.

Policies

Browse the current policies included in this deployment and view their contents.

Decision points

See the PDPs currently connected to this deployment. Each PDP shows its ID, the build it’s running, active sessions, Cerbos version, when it was last seen, and a link to its audit logs.

Embedded PDP rules

Configure [embedded policy decision points](deployments-epdp-rules.html) for this deployment. Each rule defines policy filtering criteria (resources, actions, scopes, roles, versions), authentication requirements, and IP allowlists. Multiple rules can serve different clients or environments from the same deployment.

Client credentials

Manage API credentials scoped to this deployment for PDP connections, audit log collection, and authenticated ePDP bundle access.

Settings

Configure deployment options including which policy stores contribute to builds.

## [](#%5Fdeployed%5Fversions)Deployed versions

The Builds tab displays the history of policy bundles that have been deployed. Each row in the table shows:

Build reference

A unique identifier for the build. Click to view detailed information about the build including test results and bundle contents.

Active from

The timestamp when this build was activated and pushed to connected PDPs.

Active to

The timestamp when this build was replaced by a newer version, or a dash if it is the currently active build.

Included policies

The policy stores and specific versions that contributed to this build. This makes it easy to trace exactly which policies were in effect at any point in time.

## [](#%5Fbuild%5Flife%5Fcycle)Build life cycle

Whenever Cerbos Hub detects a change in any policy store connected to a deployment, it launches a new policy build.

1. **In progress**: The policy build is queued and begins processing.
2. **Compilation**: Policies from all contributing stores are compiled together. If compilation fails, the error is surfaced so you can diagnose it quickly.
3. **Test execution**: After successful compilation, Cerbos Hub runs all policy tests found across the contributing stores. Failures are displayed with full logs for debugging.
4. **Bundle generation**: When compilation and tests pass, the bundle is generated and all PDPs assigned to this deployment receive a push notification to download and activate the new bundle immediately.

## [](#%5Fbuild%5Fdetails)Build details

Click on any build reference to view detailed information about that specific build.

### [](#%5Fbuild%5Fsummary)Build summary

The top of the page displays key metrics at a glance:

* **Status**: Whether the build succeeded or failed
* **Build completed**: When the build finished
* **Build time**: How long the build took to complete
* **Test results**: Total tests run, passed, skipped, and failed

### [](#%5Fcompile%5Fand%5Ftest%5Fstages)Compile and test stages

Expandable sections show the results of each build stage:

* **Compile**: Shows whether policy compilation succeeded. Expand to see any compilation errors or warnings.
* **Test**: Shows whether all policy tests passed. Expand to see detailed test results, including any failures with full output for debugging.

### [](#%5Fbundle%5Ffile%5Fexplorer)Bundle file explorer

The file explorer displays the contents of the generated policy bundle. Browse the directory structure organized by contributing policy store, and click any file to view its contents. This lets you verify exactly which policies were included in the bundle and inspect their contents without leaving Cerbos Hub.

Use the file explorer to:

* Confirm the correct policy versions were bundled
* Debug unexpected authorization behavior by examining the active policies
* Audit which policies contributed to a specific deployment

For details on creating policy stores and connecting PDPs to receive bundles, see the related guides:

* [Policy stores](policy-stores.html)
* [PDP configuration](decision-points.html)

## [](#%5Fbest%5Fpractices)Best practices

Use meaningful names

Name deployments after their purpose such as application, environment, or team, for example payments-service-production.

Automate testing

Include comprehensive test cases with each policy store to catch regressions before they reach production PDPs.

Validate in staging

Use staging deployments to verify policy changes in a pre-production environment before promoting to production.

Getting started
====================
## [](#%5Fprerequisites)Prerequisites

* A set of Cerbos policies. An example set of policies are avaliable at <https://github.com/cerbos/example-cerbos-policy-repository>.
* Cerbos version 0.45.1 or higher.
* Outbound internet access from your Cerbos instances so that they can connect to Cerbos Hub to fetch bundle updates and, if enabled, upload audit logs.

## [](#%5Fcreate%5Fa%5Fpolicy%5Fstore)Create a policy store

Cerbos Hub uses policy stores to manage your policies. A policy store is a collection of policies and tests that can be built into a deployment and distributed to Cerbos PDPs.

For the quick start, you can create a policy store using the browser and upload a ZIP file containing policies ([example](https://github.com/cerbos/example-cerbos-policy-repository/archive/refs/heads/main.zip)) or fork the GitHub [example repository](https://github.com/cerbos/example-cerbos-policy-repository) and connect it to Cerbos Hub.

### [](#%5Fupload%5Fpolicies%5Fvia%5Fbrowser)Upload policies via browser

1. Sign in to Cerbos Hub at <https://hub.cerbos.cloud> and follow the on-boarding wizard to create an Organization and its first Workspace.
2. Inside the Workspace, select **Policy stores** then **New store**.
3. Give the store a clear name, for example `orders-service`, choose **Browser upload** as the source, and click **Create**.
4. In the store detail page, click **Upload files** and select a ZIP file containing your policies. The ZIP file should contain the policies in the root directory, not in a subdirectory.
5. Cerbos Hub immediately ingests the ZIP file, compiles the policies, and shows the first successful build.

### [](#%5Fgithub%5Frepository)GitHub repository

1. Sign in to Cerbos Hub at <https://hub.cerbos.cloud> and follow the on-boarding wizard to create an Organization and its first Workspace.
2. Inside the Workspace, select **Policy stores** then **New store**.
3. Give the store a clear name, for example `orders-service`, choose **GitHub repository** as the source and connect to your GitHub account.
4. Pick the branch you want Hub to track, usually `main`, and save. Cerbos Hub immediately ingests the repository, compiles the policies, and shows the first successful build.

| |  You can create additional stores for other branches, teams or projects. |
| -------------------------------------------------------------------------- |

## [](#%5Fcreate%5Fa%5Fdeployment)Create a Deployment

Deployments package policies from one or more policy stores into versioned bundles that are automatically distributed to connected Cerbos PDPs.

1. Open **Deployments** then click **New deployment**.
2. Select the store you just created.
3. Click **Create**. Hub starts the initial build. When it finishes, note the deployment ID shown on the detail page. You will need this ID to configure the PDP.

## [](#%5Fgenerate%5Fclient%5Fcredentials)Generate client credentials

Navigate to **Settings** → **Client credentials** and click **Generate a client credential**, giving it a name and select **Read & Write** so that policies can be pulled down and Audit Logs pushed back. Copy both the Client ID and Client secret. The secret is shown only once.

## [](#%5Fconfigure%5Fand%5Frun%5Fa%5Fcerbos%5Fpdp)Configure and run a Cerbos PDP

You can pass the Hub connection settings as environment variables or in a YAML configuration file. The example below uses environment variables for a quick start:

```shell
docker run --rm --name cerbos \
  -p 3592:3592 -p 3593:3593 \
  -e CERBOS_HUB_DEPLOYMENT_ID="..." \
  -e CERBOS_HUB_CLIENT_ID="..." \
  -e CERBOS_HUB_CLIENT_SECRET="..." \
  ghcr.io/cerbos/cerbos:latest server
```

| CERBOS\_HUB\_DEPLOYMENT\_ID | Deployment ID from the deployment detail page in Cerbos Hub.                                                                            |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| CERBOS\_HUB\_CLIENT\_ID     | Client ID from **Deployment → Client credentials**.                                                                                     |
| CERBOS\_HUB\_CLIENT\_SECRET | Client secret from **Deployment → Client credentials**.                                                                                 |
| CERBOS\_HUB\_PDP\_ID        | Optional. A friendly name for this PDP instance, shown on the Cerbos Hub monitoring page. If omitted, a random identifier is generated. |

### [](#%5Fyaml%5Falternative)YAML alternative

```yaml
server:
  httpListenAddr: ":3592"
  grpcListenAddr: ":3593"

hub:
  credentials:
    pdpID: "orders-pdp-01" # Optional
    clientID: "..."
    clientSecret: "..."

storage:
  driver: hub
  hub:
    remote:
      deploymentID: "..." # Deployment ID from Hub
```

Assuming you saved the file as .cerbos.yaml in the current directory, start Cerbos with:

```shell
docker run --rm --name cerbos \
  -v $(pwd):/conf \
  -p 3592:3592 -p 3593:3593 \
  ghcr.io/cerbos/cerbos:latest server --config=/conf/.cerbos.yaml
```

See [Configuration](../cerbos/latest/configuration/index.html) for advanced configuration options.

## [](#%5Fenable%5Faudit%5Flog%5Fcollection%5Foptional)Enable audit log collection (optional)

Add the Hub audit backend to stream decision logs to Cerbos Hub:

```yaml
audit:
  backend: hub
  hub:
    storagePath: "/var/cerbos/audit-buffer" # Local buffer used when the network is unavailable
```

Refer to [Audit log collection](audit-log-collection.html) for details on filtering sensitive fields and other advanced options.

With a policy store connected, a deployment created, and at least one PDP running, you are ready to iterate on your policies. Push a change to the repository, watch Cerbos Hub build a new deployment version, and see the PDP update itself automatically within seconds.

## [](#%5Fnext%5Fsteps)Next steps

| [Service PDPs](decision-points.html)              | Production deployment patterns, Kubernetes setup, reliability features, and monitoring. |
| ------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [Embedded PDPs](deployments-epdp-rules.html)      | Run authorization in browsers, edge functions, and mobile apps using WebAssembly.       |
| [Audit log collection](audit-log-collection.html) | Stream decision logs to Cerbos Hub for analysis and compliance.                         |
| [Policy stores](policy-stores.html)               | Connect Git repositories, upload via CLI, or use the SDKs to manage policies.           |

Cerbos Hub
====================
Cerbos Hub simplifies the process of authoring authorization policies, testing changes, rolling out updates to production, and aggregating audit logs about authorization decisions. It is a scalable solution for developers who want to save time, streamline their workflows, and confidently roll out authorization updates, freeing you to focus on delivering great products to your customers.

## [](#%5Ffeatures)Features

Collaborative policy editing

Cerbos Hub playgrounds provide private, collaborative, IDE-like development environments to help author and test policies with ease. Drag and drop policy and test files directly into the playground editor for fast loading and testing.

Managed build and release pipeline

Cerbos Hub automatically validates, tests, signs, and distributes every policy change, giving you a turnkey CI/CD pipeline without extra infrastructure. Policy execution traces are available for debugging complex authorization logic, showing a step-by-step view of how requests are evaluated.

Source agnostic policy stores

Populate policy stores from any source using any of the many integration methods available.

Coordinated rollout of policy changes

Cerbos Hub pushes new policy bundles to every connected PDP instance, ensuring fleet-wide consistency and eliminating manual polling or reload logic.

PDP monitoring

Cerbos Hub shows which policies each PDP is serving, the exact bundle version, and when the instance was last seen.

Embedded policy decision points

Evaluate policies locally in browsers, edge functions, and other JavaScript environments using WebAssembly. Configure multiple ePDP rules per deployment, each with independent policy filtering (by resource, action, scope, role, or version), authentication requirements, and IP allowlists. Dynamic scopes enable per-tenant bundles in multi-tenant applications.

Audit log aggregation

With one line of configuration you can stream PDP decision logs to Cerbos Hub, filter sensitive fields locally, and retain searchable history without running a separate log stack.

Organization usage dashboard

The organization-level usage dashboard aggregates metrics from all your workspaces, providing a unified view of request volumes, policy distribution, and usage trends across your organization.

## [](#%5Fhow%5Fit%5Fworks)How it works

Cerbos Hub is a cloud-hosted management control plane, while Cerbos instances and the data they process remain strictly inside your network perimeter. Switching to Cerbos Hub requires only a minor configuration change to your existing Cerbos deployment. After the switch, PDPs receive optimized policy bundles from Cerbos Hub instead of compiling policies locally.

![How Cerbos Hub works](_images/how_cerbos_hub_works.png)

1. Make a change to policies and submit it to a policy store through Git, a CI pipeline, an API call, a CLI upload, or a direct drag and drop in the browser.
2. Cerbos Hub detects the update and starts a new build.
3. Validate and compile the policies.
4. Run all policy tests found in the store.
5. Generate a compact encrypted policy bundle.
6. Increment the deployment version and notify every PDP that is assigned to this deployment that a new bundle is available.
7. PDP instances download the new bundle and start serving it immediately.

Optionally, configure Cerbos Hub as an audit backend for the PDPs. Logs are streamed securely, with sensitive data removed locally before leaving your network perimeter.

## [](#%5Fget%5Fstarted)Get started

* [Quick start guide](getting-started.html) — Create a policy store, deployment, and connect your first PDP.
* [Service PDPs](decision-points.html) — Production deployment patterns for server-side authorization.
* [Embedded PDPs](deployments-epdp-rules.html) — Client-side authorization for browsers and edge functions.

Aperture by Tailscale
====================
Aperture is Tailscale’s AI gateway. It sits between AI agents and LLM providers, routing requests through the tailnet with visibility into agent activity. The Cerbos integration adds fine-grained, policy-driven authorization to every tool call that passes through Aperture.

When an agent makes a tool call, Aperture intercepts the request before it reaches the LLM. It extracts the user identity, tool name, and tool parameters and forwards them to a Cerbos PDP running on the tailnet. Cerbos evaluates the request against authorization policies and returns an allow or deny decision. Aperture enforces that decision: permitted tool calls proceed, denied tool calls are blocked before execution.

## [](#%5Farchitecture)Architecture

User -> AI Agent -> Tailscale Aperture -> LLM
                          |         ^
                     Cerbos PDP  Allow/Deny

| Aperture   | AI gateway and enforcement point. Intercepts tool calls, forwards metadata to Cerbos, and enforces the authorization decision.                                                          |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cerbos PDP | Evaluates tool calls against authorization policies. Enriches requests with context from external systems (identity providers, HR platforms, on-call systems) before making a decision. |
| Cerbos Hub | Manages the policy lifecycle: authoring, version control, testing, distribution, and audit logging. Every decision is logged back to Hub as audit evidence.                             |

## [](#%5Fwhat%5Fis%5Fevaluated)What is evaluated

Every tool call produces an authorization request containing:

| Principal attributes | The identity of whoever or whatever initiated the tool call, sourced from Tailscale. This can be enriched at decision time with real-time context from external systems such as Okta, Workday, ServiceNow, or PagerDuty: department, cost center, on-call status, project assignments. |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Resource attributes  | The tool name and its parameters (the database being queried, the CRM object being accessed, the API endpoint being called), along with metadata about the model and provider.                                                                                                         |
| Request context      | Runtime signals such as time of day, device posture, and Tailscale app capabilities.                                                                                                                                                                                                   |

The policy engine evaluates all inputs together. A decision reflects who or what is making the call, what they are attempting, and what the organization knows about both at that moment.

## [](#%5Fprerequisites)Prerequisites

* A [Tailscale](https://tailscale.com) account with an [Aperture](https://tailscale.com/aperture) instance set up
* Docker installed on a machine connected to your tailnet

## [](#%5Fsetup)Setup

### [](#%5Fconfigure%5Ftailscale%5Facls)Configure Tailscale ACLs

Define a tag and service for the Cerbos container in your tailnet access controls:

1. Create a tag (e.g. `tag:tainaron-host`)
2. Create a service named `cerbos-tainaron` on port 443 with that tag
3. Add the following ACL grants:  
```json  
{  
    "tagOwners": {  
        "tag:tainaron-host": ["autogroup:member"]  
    },  
    "autoApprovers": {  
        "services": {  
            "svc:cerbos-tainaron": ["tag:tainaron-host"]  
        }  
    },  
    "grants": [{  
        "src": ["*"],  
        "dst": ["svc:cerbos-tainaron"],  
        "ip": ["*"]  
    }]  
}  
```
4. Generate a Tailscale auth key with the tag assigned. Ephemeral mode is recommended.

### [](#%5Fconnect%5Fcerbos%5Fhub%5Ffrom%5Faperture)Connect Cerbos Hub from Aperture

1. In your Aperture instance, select the Cerbos integration. This redirects you to Cerbos Hub to create a workspace linked to your Aperture instance.
2. Complete the Cerbos Hub sign-up. The workspace is automatically provisioned with a deployment and credentials for your Aperture instance.

### [](#%5Fdownload%5Fthe%5Fconfiguration%5Ffile)Download the configuration file

After the workspace is provisioned, the Cerbos Hub dashboard provides a configuration file with your credentials pre-filled.

1. Navigate to the Aperture configuration page in your workspace
2. Click **Generate and download config file**
3. Open the downloaded `aperture.yaml` in a text editor
4. Replace `<paste-your-tailscale-auth-key-here>` with the Tailscale auth key generated in the previous step

The configuration file contains the Cerbos Hub credentials, PDP settings, and the Aperture extension configuration:

```yaml
server:
  tailscale:
    authKey: <paste-your-tailscale-auth-key-here>
    serviceName: cerbos-tainaron

pdp:
  inProcess:
    audit:
      enabled: true
      backend: "hub"
      hub:
        storagePath: /tmp/hub_auditlog

    hub:
      credentials:
        clientID: <your-client-id>
        clientSecret: <your-client-secret>

    storage:
      driver: "hub"
      hub:
        remote:
          deploymentID: <aperture-deployment-id>

extensions:
  routeExtensions:
    aperture:
      extension:
        extensionURL: /extensions/tailscale/aperture.star
      routes:
        "/aperture": ["GET", "POST"]
```

Alternatively, all credentials can be passed as environment variables instead of embedding them in the configuration file:

| TS\_AUTHKEY                 | The Tailscale auth key that was generated above.                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| CERBOS\_HUB\_DEPLOYMENT\_ID | The deployment ID to load policies from. Find this on the deployment page in Cerbos Hub.                                  |
| CERBOS\_HUB\_CLIENT\_ID     | Client ID from the deployment’s **Client credentials** tab.                                                               |
| CERBOS\_HUB\_CLIENT\_SECRET | Client secret from the deployment’s **Client credentials** tab.                                                           |
| CERBOS\_HUB\_PDP\_ID        | Optional. A name for this PDP instance, shown in the Cerbos Hub monitoring page. If not provided, a random value is used. |

When using environment variables, the configuration file reduces to:

```yaml
pdp:
  inProcess:
    audit:
      enabled: true
      backend: "hub"
      hub:
        storagePath: /tmp/hub_auditlog

    storage:
      driver: "hub"

extensions:
  routeExtensions:
    aperture:
      extension:
        extensionURL: /extensions/tailscale/aperture.star
      routes:
        "/aperture": ["GET", "POST"]
```

### [](#%5Frun%5Fthe%5Fcerbos%5Fcontainer)Run the Cerbos container

From the directory where you saved `aperture.yaml`, start the Cerbos service:

```shell
docker run \
  --rm \
  --tmpfs /tmp \
  -v $(pwd)/aperture.yaml:/config/aperture.yaml \
  cerbos/tainaron:latest server --conf.path=/config/aperture.yaml
```

The container joins your tailnet automatically and begins accepting authorization requests.

### [](#%5Fconfigure%5Faperture)Configure Aperture

Open the Aperture settings page at <http://ai/ui> from a device on your tailnet.

Add a hook named `cerbos` pointing to your Cerbos service:

```json
{
    "hooks": {
        "cerbos": {
            "url": "https://cerbos-tainaron/ext/aperture"
        }
    }
}
```

Add a grant to route tool calls to Cerbos for authorization. Set the `src` array to the users whose traffic should be evaluated, or use `*` to apply to all users:

```json
{
    "src": ["*"],
    "grants": [
        {
            "hook": {
                "match": {
                    "providers": ["*"],
                    "models": ["*"],
                    "events": ["tool_call_entire_request"]
                },
                "hook": "cerbos",
                "fields": ["tools"]
            }
        }
    ]
}
```

### [](#%5Fverify%5Fthe%5Fconnection)Verify the connection

After starting the container, check the Cerbos Hub dashboard to confirm the PDP has connected. The **Decision points** tab on your deployment page shows all connected PDP instances.

## [](#%5Frecommended%5Frollout)Recommended rollout

| Observe         | Start with a default allow-all policy. All tool calls are evaluated and logged, but nothing is blocked. Use the [audit data](audit-log-collection.html) to build an evidence base of what agents are doing. |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Author policies | Write rules that reflect the organization’s requirements. Start narrow: restrict a single tool or constrain a specific parameter. Expand coverage incrementally.                                            |
| Enforce         | Push policies through Cerbos Hub. They take effect immediately across all connected PDPs. No agent modifications required.                                                                                  |

## [](#%5Fpolicy%5Fexamples)Policy examples

Cerbos policies are declarative and version-controlled. Each rule targets a set of actions (tool names), applies to specific roles, and specifies conditions under which the rule takes effect. Conditions can reference any attribute of the principal, the resource, or the request context.

A single policy can express requirements such as the following:

1. **Read-only tools are always permitted.** File reads, searches, and documentation lookups are allowed unconditionally for all authenticated users.
2. **CRM access is scoped by team and operation.** An agent can read account metadata from Salesforce via an MCP tool, but only for users in the sales org. Updating deal stages or exporting contact lists requires a more privileged role.
3. **Production database access is restricted.** An agent calling a database tool against a production connection string is denied unless the user is currently on call, verified in real time against PagerDuty. The same query against a staging environment is permitted for any engineer.
4. **HR and compensation data require explicit authorization.** Tools that access BambooHR, Workday, or any system containing employee PII are denied by default. Access is granted only to users in HR or People Ops, and only from managed devices.
5. **Different rules apply to different clients.** A tool call from a sanctioned coding agent (Claude Code) is permitted, while the same call from an unsanctioned client is denied. The user-agent is an input to the policy.

These rules compose. A single tool call can be evaluated against multiple conditions simultaneously. The policy engine resolves the outcome deterministically.

## [](#%5Faudit%5Flogging)Audit logging

Every authorization decision creates a log entry in Cerbos Hub recording:

* The principal: who or what triggered the tool call
* The resource: which tool, with what parameters
* The decision: allow or deny
* The policy: which version, which rule matched
* The context: all attributes that were evaluated

This is a per-decision record that traces from a specific tool call to a specific policy evaluation. See [Audit log collection](audit-log-collection.html) for details on accessing and exporting audit data.

## [](#%5Ffurther%5Freading)Further reading

* [Aperture documentation](https://tailscale.com/aperture)
* [Service PDPs](decision-points.html)
* [Audit log collection](audit-log-collection.html)
* [Deployments](deployments.html)

Migrating from legacy workspaces
====================
This guide covers migrating from the legacy Cerbos Hub workspace architecture to the current system based on policy stores and deployments. It applies to both service PDPs and embedded PDPs.

| |  If you would prefer a guided migration, contact [support@cerbos.dev](mailto:support@cerbos.dev). We are happy to walk you through the process. |
| ------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#%5Fwhat%5Fthe%5Fnew%5Farchitecture%5Fprovides)What the new architecture provides

The legacy system coupled a single Git repository to a single workspace, with deployment labels defined in `.cerbos-hub.yaml` and a workspace secret for bundle encryption. The current architecture removes these constraints.

Multi-store composition

[Deployments](deployments.html) can combine policies from multiple independent [policy stores](policy-stores.html). Teams, services, or tenants can own their policies separately while Cerbos Hub merges them at build time. The legacy system was limited to a single repository per workspace.

Source-agnostic ingestion

Policy stores accept input from Git repositories, CI/CD pipelines, the Cerbos Hub API, SDKs, the `cerbosctl` CLI, or browser upload. The legacy system required a GitHub repository. See [supported ingestion methods](policy-stores.html#%5Fsupported%5Fingestion%5Fmethods).

No workspace secret

Bundle encryption is managed entirely by Cerbos Hub. There is no secret to generate, distribute, rotate, or lose. PDP configuration requires only a client ID, client secret, and deployment ID. See [deploying a PDP](decision-points.html#%5Fdeploying%5Fa%5Fpdp).

Deployment-scoped credentials

Credentials are scoped to individual deployments rather than an entire workspace. This provides a narrower blast radius when credentials are rotated or revoked. See [obtaining credentials](decision-points.html#%5Fobtaining%5Fcredentials).

Embedded PDP rules

Each deployment can define multiple [ePDP rules](deployments-epdp-rules.html#%5Fepdp%5Frules) with independent policy filtering (by resource, action, scope, role, and version), [authentication requirements, and IP allowlists](deployments-epdp-rules.html#%5Fsecurity%5Fcontrols). The legacy system included all annotated policies in a single bundle with no access controls.

Automatic build pipeline

Every change to a policy store triggers compilation, test execution, and bundle distribution. The legacy system required `.cerbos-hub.yaml` label mappings to control which Git references produced builds. See [build life cycle](deployments.html#%5Fbuild%5Flife%5Fcycle).

## [](#%5Fmigration%5Foverview)Migration overview

Migration involves five phases:

1. [Create a new workspace](#create-workspace) in Cerbos Hub
2. [Create a policy store](#create-policy-store) and connect it to your Git repository
3. [Create a deployment](#create-deployment) using that policy store
4. [Update service PDP configuration](#update-service-pdps) to use the new credentials and deployment ID
5. [Update embedded PDP integration](#update-embedded-pdps) (if applicable)

Each phase can be completed independently. Legacy and current PDPs can run in parallel during the transition.

## [](#%5Farchitecture%5Fchanges)Architecture changes

| Aspect                         | Legacy                                                              | Current                                                                            |
| ------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Policy source                  | Workspace (single Git repository, single policy source)             | One or more [policy stores](policy-stores.html) per [deployment](deployments.html) |
| Bundle versioning              | Deployment labels in .cerbos-hub.yaml (branch, tag, or commit hash) | Deployment ID; each policy store change triggers a new build automatically         |
| Bundle encryption              | Workspace secret (asymmetric key pair)                              | Managed by Cerbos Hub; no workspace secret required                                |
| Credentials                    | Workspace-scoped client ID, client secret, and workspace secret     | Deployment-scoped client ID and client secret                                      |
| Embedded PDP bundle addressing | URL with workspace and label query parameters                       | Opaque ePDP rule ID                                                                |
| Embedded PDP policy filtering  | Per-policy YAML annotation (hub.cerbos.cloud/embedded-pdp)          | Per-rule configuration in Hub UI (resources, actions, scopes, roles, versions)     |
| Audit log collection           | Same credentials as bundle distribution                             | Same credentials as bundle distribution (no workspace secret)                      |

## [](#create-workspace)Phase 1: Create a new workspace

Policy stores and deployments are only available in new workspaces. Your legacy workspace cannot be upgraded in place, so you need to create a new one.

1. Sign in to [Cerbos Hub](https://hub.cerbos.cloud)
2. Create a new workspace

## [](#create-policy-store)Phase 2: Create a policy store

A policy store replaces the workspace as the container for your policies. If your legacy workspace was connected to a GitHub repository, the policy store connects to the same repository.

1. In the new workspace, navigate to **Policy stores** and click **New store**
2. Enter a name for the store (e.g. the same name as your legacy workspace)
3. Select **GitHub repository** as the source and authorize access if prompted
4. Select the same repository your legacy workspace used
5. Configure the branch to track

If your legacy `.cerbos-hub.yaml` defined a label pointing to a specific branch (e.g. `main`), use that branch as the policy store’s tracked branch.

Legacy label mapping

```yaml
# .cerbos-hub.yaml (legacy)
apiVersion: api.cerbos.cloud/v1
labels:
  latest:
    branch: main
```

In this example, create a policy store tracking the `main` branch. The label abstraction is no longer needed — the policy store tracks the branch directly.

If your legacy setup used multiple labels pointing to different branches (e.g. `production` on `main` and `staging` on `develop`), create a separate policy store for each branch, then reference each in the appropriate deployment.

See [Policy stores](policy-stores.html) and [GitHub integration](policy-stores-git-github.html) for details.

### [](#%5Fsubdirectory%5Fconfiguration)Subdirectory configuration

If your policies are in a subdirectory of the repository, specify the path when configuring the GitHub connection. The policy store syncs only that directory and its children.

### [](#%5Fnon%5Fgithub%5Fsources)Non-GitHub sources

If your policies are not in GitHub, other ingestion methods are available: CI/CD pipelines, Cerbos Hub SDKs, the `cerbosctl` CLI, or browser upload. See [Supported ingestion methods](policy-stores.html#%5Fsupported%5Fingestion%5Fmethods).

## [](#create-deployment)Phase 3: Create a deployment

A deployment replaces the combination of workspace + deployment label. It packages policies from one or more policy stores into versioned bundles and distributes them to connected PDPs.

1. Navigate to **Deployments** and click **New deployment**
2. Select the policy store created in Phase 2
3. Click **Create**

Cerbos Hub runs an initial build. When it completes, note the **deployment ID** from the deployment detail page.

### [](#%5Fgenerate%5Fclient%5Fcredentials)Generate client credentials

1. On the deployment page, select the **Client credentials** tab
2. Click **Generate a client credential**
3. Choose **Read & Write** if you need audit log collection, or **Read only** for bundle distribution only
4. Save the client ID and client secret — the secret is shown only once

These credentials replace the legacy workspace-scoped credentials and workspace secret.

## [](#update-service-pdps)Phase 4: Update service PDP configuration

The PDP configuration changes in two ways:

* `CERBOS_HUB_BUNDLE` (label name) is replaced by `CERBOS_HUB_DEPLOYMENT_ID`
* `CERBOS_HUB_WORKSPACE_SECRET` is no longer required

### [](#%5Flegacy%5Fconfiguration)Legacy configuration

```shell
docker run --rm --name cerbos \
  -p 3592:3592 -p 3593:3593 \
  -e CERBOS_HUB_BUNDLE="latest" \
  -e CERBOS_HUB_WORKSPACE_SECRET="..." \
  -e CERBOS_HUB_CLIENT_ID="..." \
  -e CERBOS_HUB_CLIENT_SECRET="..." \
  ghcr.io/cerbos/cerbos:latest server
```

### [](#%5Fupdated%5Fconfiguration)Updated configuration

```shell
docker run --rm --name cerbos \
  -p 3592:3592 -p 3593:3593 \
  -e CERBOS_HUB_DEPLOYMENT_ID="..." \
  -e CERBOS_HUB_CLIENT_ID="..." \
  -e CERBOS_HUB_CLIENT_SECRET="..." \
  ghcr.io/cerbos/cerbos:latest server
```

Use the deployment ID and credentials from Phase 3.

### [](#%5Fyaml%5Fconfiguration%5Ffile)YAML configuration file

Legacy

```yaml
hub:
  credentials:
    clientID: "..."
    clientSecret: "..."
    workspaceSecret: "..."

storage:
  driver: hub
  hub:
    remote:
      bundleLabel: latest
```

Updated

```yaml
hub:
  credentials:
    clientID: "..."
    clientSecret: "..."

storage:
  driver: hub
  hub:
    remote:
      deploymentID: "..."
```

The `workspaceSecret` and `bundleLabel` fields are removed. The `deploymentID` field replaces `bundleLabel`.

### [](#%5Faudit%5Flog%5Fcollection)Audit log collection

If audit log collection was enabled, the `audit` configuration block is unchanged:

```yaml
audit:
  backend: hub
  hub:
    storagePath: "/var/cerbos/audit-buffer"
```

The audit backend uses the same deployment-scoped credentials configured in the `hub.credentials` block. No additional credential changes are needed.

| |  Existing audit log data stored under your legacy workspace is not automatically migrated to the new deployment. Contact the Cerbos team at [support@cerbos.dev](mailto:support@cerbos.dev) to arrange migration of your historical audit logs. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#%5Fcerbos%5Fversion%5Frequirement)Cerbos version requirement

The current deployment system requires Cerbos version 0.51.0 or later. If your PDPs are running an older version, upgrade before switching to the new credentials.

### [](#%5Frolling%5Fmigration)Rolling migration

Legacy and current PDPs can run in parallel. To migrate a fleet incrementally:

1. Deploy updated configuration to a subset of instances
2. Verify those instances connect to Cerbos Hub and receive the correct bundle (check the **Decision points** tab on the deployment page)
3. Roll out to the remaining instances

## [](#update-embedded-pdps)Phase 5: Update embedded PDP integration

This phase applies only if you use the embedded PDP (WebAssembly-based authorization in browsers, edge functions, or other JavaScript environments). If you only use service PDPs, skip to [Cleanup](#cleanup).

The embedded PDP requires new SDK packages and a different bundle addressing model.

### [](#%5Fcreate%5Fan%5Fepdp%5Frule)Create an ePDP rule

Before updating client code, create an ePDP rule on the deployment:

1. Navigate to the deployment in Cerbos Hub
2. Select the **Embedded PDP rules** tab
3. Click **Create rule**
4. Configure policy filtering (see [Policy filtering](#epdp-policy-filtering) below)
5. Configure access controls (see [Access controls](#epdp-access-controls) below)
6. Click **Save rule**
7. Copy the **rule ID** from the rule card

### [](#epdp-policy-filtering)Policy filtering

The legacy system used a YAML annotation on individual policies to control inclusion in the bundle:

```yaml
apiVersion: api.cerbos.dev/v1
metadata:
  annotations:
    hub.cerbos.cloud/embedded-pdp: "true"
resourcePolicy:
  version: default
  resource: purchase_order
```

The current system filters policies through the ePDP rule configuration in Cerbos Hub. The annotation is no longer used.

To replicate your existing filtering:

1. Identify which policies had the `hub.cerbos.cloud/embedded-pdp: "true"` annotation
2. Note the resource types, actions, roles, and scopes those policies cover
3. Configure equivalent filters on the ePDP rule using the **Resources and actions**, **Scopes**, **Roles**, and **Versions** settings

If no policies in your legacy setup were annotated (all policies were included), leave all filters set to **All** on the new rule.

| |  The hub.cerbos.cloud/embedded-pdp annotation can be removed from your policy files after migration is complete. It has no effect in the current system. |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |

See [Filtering policies](deployments-epdp-rules.html#%5Ffiltering%5Fpolicies) for details on each filter type.

### [](#epdp-access-controls)Access controls

The legacy embedded PDP did not support authentication or IP restrictions on bundle downloads. The current system supports both.

| Authentication | If the bundle is served to end-user browsers and the authorization logic is not sensitive, **Public access** is appropriate. If the bundle is fetched server-side (Node.js, edge workers), use **Client credential** and store credentials in environment variables or a secrets manager. |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IP allowlist   | If bundle access should be restricted to specific network ranges, configure CIDR entries on the rule.                                                                                                                                                                                     |

See [Security controls](deployments-epdp-rules.html#%5Fsecurity%5Fcontrols) for details.

### [](#%5Fupdate%5Fsdk%5Fpackages)Update SDK packages

Remove the legacy package and install the replacements:

```bash
npm uninstall @cerbos/embedded
npm install @cerbos/embedded-client @cerbos/embedded-server
```

If the rule uses client credential authentication, also install the `@cerbos/hub` package:

```bash
npm install @cerbos/hub
```

### [](#%5Fupdate%5Fclient%5Finitialization)Update client initialization

Legacy

```typescript
import { AutoUpdatingLoader, Embedded } from "@cerbos/embedded";

const cerbos = new Embedded(
  new AutoUpdatingLoader(
    "https://lite.cerbos.cloud/bundle?workspace=...&label=...",
  ),
);
```

Updated

```typescript
import { Embedded } from "@cerbos/embedded-client";
import wasm from "@cerbos/embedded-server/server.wasm?init"; (1)

const cerbos = new Embedded({
  policies: { ruleId: "<RULE_ID>" },
  wasm,
});
```

| **1** | The ?init import suffix is Vite-specific. See [WebAssembly module loading](#epdp-wasm-loading) below for other environments. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------- |

Replace `<RULE_ID>` with the rule ID from Cerbos Hub.

The `AutoUpdatingLoader` and the bundle URL are no longer used. The SDK fetches bundles and polls for updates based on the rule ID.

### [](#epdp-wasm-loading)WebAssembly module loading

The legacy SDK bundled the WebAssembly runtime internally. The current SDK requires explicit loading of the WASM module. The mechanism depends on your build tooling:

| Environment         | Import                                                                                                                                                                                        |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Vite                | import wasm from "@cerbos/embedded-server/server.wasm?init";                                                                                                                                  |
| Webpack             | import wasmUrl from "@cerbos/embedded-server/server.wasm";                                                                                                                                    |
| Rspack              | import wasmUrl from "@cerbos/embedded-server/server.wasm";                                                                                                                                    |
| Next.js (Turbopack) | Copy WASM to public/ and pass the URL string (see [WebAssembly module loading](#epdp-wasm-loading) below)                                                                                     |
| Node.js             | import { readFile } from "node:fs/promises"; import { fileURLToPath } from "node:url"; const wasm = readFile(   fileURLToPath(import.meta.resolve("@cerbos/embedded-server/server.wasm")), ); |

See [Loading the WebAssembly module](deployments-epdp-rules.html#%5Floading%5Fthe%5Fwebassembly%5Fmodule) for all options.

### [](#%5Fauthenticated%5Faccess)Authenticated access

If the rule requires client credentials:

```typescript
import { Embedded } from "@cerbos/embedded-client";
import { credentialsFromEnv } from "@cerbos/hub";
import wasm from "@cerbos/embedded-server/server.wasm?init";

const cerbos = new Embedded({
  policies: {
    ruleId: "<RULE_ID>",
    credentials: credentialsFromEnv(),
  },
  wasm,
});
```

This reads `CERBOS_HUB_CLIENT_ID` and `CERBOS_HUB_CLIENT_SECRET` from `process.env`.

### [](#%5Fauthorization%5Fcheck%5Fapi)Authorization check API

The authorization check methods (`isAllowed`, `checkResource`, `checkResources`) are unchanged between the legacy and current SDKs. Existing check calls do not require modification. Run your test suite to confirm authorization decisions match the legacy behavior.

The current SDK also supports `planResources`, which was not available in the legacy embedded PDP.

### [](#%5Fnew%5Fcapabilities)New capabilities

The current ePDP SDK adds several capabilities not present in the legacy version:

| Dynamic scopes                | Clients specify scopes at fetch time, so each tenant gets only its applicable policies without a dedicated rule. See [Dynamic scopes](deployments-epdp-rules.html#%5Fdynamic%5Fscopes). |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deferred activation           | Download bundle updates without applying them immediately. See [Deferred activation](deployments-epdp-rules.html#%5Fdeferred%5Factivation).                                             |
| Update notifications          | Register callbacks for bundle update success or failure. See [Update notifications](deployments-epdp-rules.html#%5Fupdate%5Fnotifications).                                             |
| Decision callbacks            | Capture authorization decisions locally via onDecision. See [Configuration options](deployments-epdp-rules.html#%5Fconfiguration%5Foptions).                                            |
| Query planning                | Use planResources to generate query plans. See [planResources](deployments-epdp-rules.html#%5Fplanresources).                                                                           |
| Multiple rules per deployment | Serve different bundle configurations to different clients. See [ePDP rules](deployments-epdp-rules.html#%5Fepdp%5Frules).                                                              |

## [](#cleanup)Cleanup

After confirming all PDPs are running on the new configuration:

1. Remove the `.cerbos-hub.yaml` deployment labels file from your repository (this was only used by the legacy workspace system)
2. Remove the `hub.cerbos.cloud/embedded-pdp` annotations from policy files, if present
3. Verify that the `@cerbos/embedded` package is no longer referenced in your codebase (embedded PDP only)
4. Revoke the legacy workspace client credentials
5. Delete or archive the legacy workspace

On-premises deployment
====================
Cerbos Hub can be deployed on-premises in your own infrastructure, giving you full control over your authorization management platform while maintaining all the features of the cloud-hosted service.

## [](#%5Foverview)Overview

On-premises deployment is suitable for organizations that:

* Require data residency within their own infrastructure
* Have regulatory or compliance requirements that prevent use of cloud services
* Need to integrate Hub deeply with internal systems
* Want to operate Hub in air-gapped or restricted network environments

The on-premises deployment includes all core Cerbos Hub features:

* Policy stores and deployments
* Policy validation and testing
* Bundle generation and distribution to PDPs
* Audit log collection and analysis
* User management and access control

## [](#%5Fgetting%5Fstarted)Getting started

On-premises deployment of Cerbos Hub is available for enterprise customers. To learn more about deploying Cerbos Hub in your own infrastructure, please [contact us](https://cerbos.dev/contact). Our team will work with you to understand your requirements and help you get set up.

Collaborative policy playgrounds
====================
Cerbos Hub playgrounds are fully-interactive, private development environments that provide an IDE-like experience for authoring policies. You can quickly create or edit policies and test fixtures with instant feedback on syntax issues and test failures. Take advantage of the powerful collaborative editing features to pair with colleagues to develop new authorization rules or use it as a sandbox to train new team members on Cerbos policies.

## [](#%5Fimporting%5Ffiles)Importing files

Drag and drop files directly into the playground editor:

* **Individual files**: Drop policy files (`.yaml`, `.yml`) or test files directly into the file tree
* **Zip archives**: Drop a zip file containing an entire policy directory structure to load multiple files at once
* **Folders**: Drop entire folders to import complete policy sets

This makes it easy to quickly load local policies for testing, share examples with colleagues, or migrate existing policies into the playground environment.

## [](#%5Fcreating%5Fa%5Fplayground)Creating a playground

Login to Cerbos Hub and select one of the organizations you’re a member of. Click on the **Playgrounds** tab to view existing playgrounds or to create a new one.

When creating a new playground, you have a number of options:

* Create an empty playground to start from scratch
* Generate a starter RBAC policy by answering a few questions about your user roles, resources and actions
* Start with an example template set of policies covering common use cases
* Create from an existing policy store to experiment with production policies in a safe environment

### [](#%5Fcreate%5Ffrom%5Fa%5Fpolicy%5Fstore)Create from a policy store

You can create a playground directly from an existing policy store, making it easy to experiment with production policies without affecting live authorization decisions. This is useful for:

* Testing policy changes before deploying them
* Debugging authorization issues with real policy configurations
* Training team members using actual policies as examples

To create a playground from a store, navigate to the policy store and click **Create playground**. The playground is pre-populated with all policies and tests from the store.

After creating a playground, click on the **Video tutorial** button on the top right corner of the screen to learn the basics.

## [](#%5Freadme%5Ffiles)README files

Playgrounds support README.md files that display as rendered markdown when opened. When you open a playground containing a README and no file is selected, the README displays automatically.

README files can include:

* Relative links to other files in the playground (click to open in the editor)
* External links (opens with a confirmation dialog)
* Standard markdown formatting

Use README files to document your playground examples, explain policy structure, or provide onboarding instructions for team members.

## [](#%5Fplayground%5Fengine%5Fsettings)Playground engine settings

The playground engine settings in the Settings tab allow you to configure the [Cerbos PDP engine](../cerbos/latest/configuration/engine.html) used when evaluating policy during development. Policy execution traces are available, providing a detailed, step-by-step view of how Cerbos evaluates a request, including every rule, condition, and variable evaluation. This helps you debug complex authorization logic and understand exactly why a specific decision was made.

* **Default policy version**: When a request does not explicitly specify the policy version, the Cerbos engine attempts to find a matching policy that has its version set to `default`. You can change this fallback value by setting the default policy version.
* **Lenient scope search**: When lenient scope search is enabled, if a policy with scope `a.b.c` does not exist in the store, Cerbos will attempt to find scopes `a.b`, `a` and ``` `` ``` in that order.
* **Globals**: Global variables are a way to pass environment-specific information to policy conditions. Values defined here are exposed to policy conditions via the `globals` object.

You can find full details of these settings in the [Cerbos configuration reference](../cerbos/latest/configuration/engine.html).

## [](#%5Fexplore%5Ftab)Explore tab

The Explore tab lets you interactively test authorization decisions against your policies. Select a fixtures folder containing test data, then choose a principal and resource to evaluate.

The panel displays:

* **Actions and effects**: Each action shows its authorization result (`ALLOW` or `DENY`). Click **Trace** next to any action to see the detailed evaluation path.
* **Effective derived roles**: Shows which derived roles were activated for the selected principal, helping you understand role-based access decisions.

Click **\+ Add action** to test additional actions, or **Create auxiliary data fixtures** to add test data for your evaluations.

### [](#%5Fpermissions%5Fmatrix%5Fview)Permissions matrix view

The matrix view displays permission evaluation results in a comprehensive grid format, showing how policies affect different principal and resource combinations at a glance. This is useful for:

* Visualizing access patterns across multiple principals and resources
* Demonstrating authorization behavior during policy reviews or demos
* Quickly identifying unexpected permission gaps or grants

Toggle between the standard explore view and the matrix view using the view selector in the Explore tab.

## [](#%5Ftest%5Fresults)Test results

The bottom panel shows test execution results with two tabs:

* **Problems**: Displays any syntax errors or validation issues in your policies.
* **Test results**: Shows the outcome of all policy tests. Filter by **Passed**, **Failed**, **Skipped**, or **Errored** to focus on specific results.

Click on any test file to see detailed results. For failed tests, a side-by-side diff view highlights the differences between expected and actual outputs.

## [](#%5Fexecution%5Ftraces)Execution traces

When debugging complex authorization logic, execution traces provide a detailed, step-by-step view of how Cerbos evaluates a request. Traces show every rule, condition, and variable evaluation, helping you understand exactly why a specific decision was made.

To view execution traces, click the **Trace** button next to any action in the Explore tab. Expand individual trace entries to see the evaluation path, including which rules matched and how conditions were evaluated.

## [](#%5Ftry%5Fthe%5Fapi)Try the API

One of the key features of the playground is the ability to try out authorization checks against your policies without having to run a local Policy Decision Point (PDP). In the Implement tab of the sidebar, you can experiment with both the Check API and the Plan API. This section allows you to select from your test fixtures and view the request structure needed to call the PDP, as well as the expected response. When evaluating policies, the effective derived roles for a user are displayed, helping you understand which derived roles were activated for that user during the request.

![Try the API](_images/playground_try_api.png)

## [](#%5Fconnect%5Fa%5Fpdp%5Fto%5Fa%5Fplayground)Connect a PDP to a playground

For developers looking to test the integration of their application, Cerbos Hub offers a Playground PDP connection. This feature allows you to start up a PDP locally in your development environment and connect it to your current playground instance. Any changes you make in the playground are immediately reflected in your local PDP, enabling fast iteration and providing a real-time feedback loop for your integration efforts.

Instructions for starting up a local PDP can be found in the Implement tab under "Connect a PDP"

![Connect a PDP](_images/playground_connect_pdp.png)

| |  Note that while the Playground PDP connection is an excellent tool for rapid development and testing, it’s not intended for production use. When you’re ready to release your application to production environments, you should [create a workspace](getting-started.html) with a policy store and configure the PDPs to receive bundle updates via Cerbos Hub’s fully managed CI/CD pipeline. It also allows you to take advantage of Cerbos Hub audit log collection to effortlessly store and analyze all the decisions made by your PDPs. |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Policy stores: CLI upload (binary)
====================
## [](#%5Finstallation)Installation

`cerbosctl` binaries are available for multiple operating systems and architectures. See the [releases page](https://github.com/cerbos/cerbos/releases/tag/v0.45.1) for all available downloads.

| OS    | Arch      | Bundle                                    |
| ----- | --------- | ----------------------------------------- |
| Linux | x86-64    | cerbosctl\_0.45.1\_Linux\_x86\_64.tar.gz  |
| Linux | arm64     | cerbosctl\_0.45.1\_Linux\_arm64.tar.gz    |
| MacOS | universal | cerbosctl\_0.45.1\_Darwin\_all.tar.gz     |
| MacOS | x86-64    | cerbosctl\_0.45.1\_Darwin\_x86\_64.tar.gz |
| MacOS | arm64     | cerbosctl\_0.45.1\_Darwin\_arm64.tar.gz   |

You can download the binaries by running the following command. Substitute `<BUNDLE>` with the appropriate value from the above table.

```sh
curl -L -o cerbosctl.tar.gz "https://github.com/cerbos/cerbos/releases/download/v0.45.1/<BUNDLE>"
tar xvf cerbosctl.tar.gz
chmod +x cerbosctl
mv cerbosctl /usr/local/bin/ # or somewhere on your PATH
```

| |  Cerbos binaries are signed using [sigstore](https://www.sigstore.dev) tools during the automated build process and the verification bundle is published along with the binary as <BUNDLE>.bundle. The following example demonstrates how to verify the Linux X86\_64 bundle archive. \# Download the bundle archive curl -L \\   \-o cerbosctl\_0.45.1\_Linux\_x86\_64.tar.gz \\   "https://github.com/cerbos/cerbos/releases/download/v0.45.1/cerbosctl\_0.45.1\_Linux\_x86\_64.tar.gz" \# Download the verification bundle curl -L \\   \-o cerbosctl\_0.45.1\_Linux\_x86\_64.tar.gz.bundle \\   "https://github.com/cerbos/cerbos/releases/download/v0.45.1/cerbosctl\_0.45.1\_Linux\_x86\_64.tar.gz.bundle" \# Verify the signature cosign verify-blob \\   \--certificate-oidc-issuer="https://token.actions.githubusercontent.com" \\   \--certificate-identity="https://github.com/cerbos/cerbos/.github/workflows/release.yaml@refs/tags/v0.45.1" \\   \--bundle="cerbosctl\_0.45.1\_Linux\_x86\_64.tar.gz.bundle" \\   "cerbosctl\_0.45.1\_Linux\_x86\_64.tar.gz" |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#%5Fusage)Usage

The `cerbosctl` CLI tool can be used to upload policies to a policy store in Cerbos Hub.

First generate a set of client credentials for the policy store in Cerbos Hub - you can do this in the **Client credentials** section in the UI. Make sure to select the `Read & Write` option when creating the credentials to allow uploading policies.

Then export the following environment variables with the values from the generated client credentials and the store ID:

```sh
export CERBOS_HUB_CLIENT_ID=...
export CERBOS_HUB_CLIENT_SECRET=...
export CERBOS_HUB_STORE_ID=...
```

The following command uploads policy files from the current directory and replaces all the files in the store.

```sh
cerbosctl hub store replace-files .
```

## [](#%5Ffull%5Fcli%5Freference)Full CLI Reference

```none
Usage: cerbosctl hub store --store-id=STRING --client-id=STRING --client-secret=STRING <command> [flags]

Interact with Cerbos Hub managed stores.

Requires an existing managed store and the API credentials to access it. The store ID and credentials can be provided using either command-line flags or
environment variables.

Flags:
  -h, --help                    Show context-sensitive help.

      --store-id=STRING         ID of the store to operate on ($CERBOS_HUB_STORE_ID)
      --client-id=STRING        Client ID of the access credential ($CERBOS_HUB_CLIENT_ID)
      --client-secret=STRING    Client secret of the access credential ($CERBOS_HUB_CLIENT_SECRET)

Commands:
  hub store list-files --store-id=STRING --client-id=STRING --client-secret=STRING [flags]
    List store files

  hub store get-files --store-id=STRING --client-id=STRING --client-secret=STRING --output-path=STRING <files> ... [flags]
    Download files from the store

  hub store download --store-id=STRING --client-id=STRING --client-secret=STRING <output-path> [flags]
    Download the entire store

  hub store replace-files --store-id=STRING --client-id=STRING --client-secret=STRING <path> [flags]
    Overwrite the store with the given set of files

  hub store add-files --store-id=STRING --client-id=STRING --client-secret=STRING <paths> ... [flags]
    Add files to the store

  hub store delete-files --store-id=STRING --client-id=STRING --client-secret=STRING <paths> ... [flags]
    Delete files from the store
```

Policy stores: CLI upload (Container)
====================
The `cerbosctl` CLI tool is also available as a Docker container image:

Via ghcr.io

```sh
docker run --rm -it ghcr.io/cerbos/cerbosctl:latest hub store
```

Via docker.io

```sh
docker run --rm -it docker.io/cerbos/cerbosctl:latest hub store
```

## [](#%5Fusage)Usage

The `cerbosctl` container can be used to upload policies to a policy store in Cerbos Hub.

First generate a set of client credentials for the policy store in Cerbos Hub - you can do this in the **Client credentials** section in the UI. Make sure to select the `Read & Write` option when creating the credentials to allow uploading policies.

Then export the following environment variables with the values from the generated client credentials and the store ID:

```sh
export CERBOS_HUB_CLIENT_ID=...
export CERBOS_HUB_CLIENT_SECRET=...
export CERBOS_HUB_STORE_ID=...
```

The following command uploads policy files from the policies directory and replaces all the files in the store.

```sh
docker run -it {cerbosctl-docker-img} \
    -e CERBOS_HUB_CLIENT_ID=$CERBOS_HUB_CLIENT_ID \
    -e CERBOS_HUB_CLIENT_SECRET=$CERBOS_HUB_CLIENT_SECRET \
    -e CERBOS_HUB_STORE_ID=$CERBOS_HUB_STORE_ID \
    -v $(pwd):/policies \
    hub store replace-files /policies .
```

## [](#%5Ffull%5Fcli%5Freference)Full CLI Reference

```none
Usage: cerbosctl hub store --store-id=STRING --client-id=STRING --client-secret=STRING <command> [flags]

Interact with Cerbos Hub managed stores.

Requires an existing managed store and the API credentials to access it. The store ID and credentials can be provided using either command-line flags or
environment variables.

Flags:
  -h, --help                    Show context-sensitive help.

      --store-id=STRING         ID of the store to operate on ($CERBOS_HUB_STORE_ID)
      --client-id=STRING        Client ID of the access credential ($CERBOS_HUB_CLIENT_ID)
      --client-secret=STRING    Client secret of the access credential ($CERBOS_HUB_CLIENT_SECRET)

Commands:
  hub store list-files --store-id=STRING --client-id=STRING --client-secret=STRING [flags]
    List store files

  hub store get-files --store-id=STRING --client-id=STRING --client-secret=STRING --output-path=STRING <files> ... [flags]
    Download files from the store

  hub store download --store-id=STRING --client-id=STRING --client-secret=STRING <output-path> [flags]
    Download the entire store

  hub store replace-files --store-id=STRING --client-id=STRING --client-secret=STRING <path> [flags]
    Overwrite the store with the given set of files

  hub store add-files --store-id=STRING --client-id=STRING --client-secret=STRING <paths> ... [flags]
    Add files to the store

  hub store delete-files --store-id=STRING --client-id=STRING --client-secret=STRING <paths> ... [flags]
    Delete files from the store
```

Policy stores: CLI upload (Homebrew)
====================
## [](#%5Finstallation)Installation

`cerbosctl` binaries are available via Homebrew for simple installation on macOS. To install the `cerbosctl` CLI tool, run the following command:

```sh
brew tap cerbos/tap
brew install cerbos
```

## [](#%5Fusage)Usage

The `cerbosctl` CLI tool can be used to upload policies to a policy store in Cerbos Hub.

First generate a set of client credentials for the policy store in Cerbos Hub - you can do this in the **Client credentials** section in the UI. Make sure to select the `Read & Write` option when creating the credentials to allow uploading policies.

Then export the following environment variables with the values from the generated client credentials and the store ID:

```sh
export CERBOS_HUB_CLIENT_ID=...
export CERBOS_HUB_CLIENT_SECRET=...
export CERBOS_HUB_STORE_ID=...
```

The following command uploads policy files from the current directory and replaces all the files in the store.

```sh
cerbosctl hub store replace-files .
```

## [](#%5Ffull%5Fcli%5Freference)Full CLI Reference

```none
Usage: cerbosctl hub store --store-id=STRING --client-id=STRING --client-secret=STRING <command> [flags]

Interact with Cerbos Hub managed stores.

Requires an existing managed store and the API credentials to access it. The store ID and credentials can be provided using either command-line flags or
environment variables.

Flags:
  -h, --help                    Show context-sensitive help.

      --store-id=STRING         ID of the store to operate on ($CERBOS_HUB_STORE_ID)
      --client-id=STRING        Client ID of the access credential ($CERBOS_HUB_CLIENT_ID)
      --client-secret=STRING    Client secret of the access credential ($CERBOS_HUB_CLIENT_SECRET)

Commands:
  hub store list-files --store-id=STRING --client-id=STRING --client-secret=STRING [flags]
    List store files

  hub store get-files --store-id=STRING --client-id=STRING --client-secret=STRING --output-path=STRING <files> ... [flags]
    Download files from the store

  hub store download --store-id=STRING --client-id=STRING --client-secret=STRING <output-path> [flags]
    Download the entire store

  hub store replace-files --store-id=STRING --client-id=STRING --client-secret=STRING <path> [flags]
    Overwrite the store with the given set of files

  hub store add-files --store-id=STRING --client-id=STRING --client-secret=STRING <paths> ... [flags]
    Add files to the store

  hub store delete-files --store-id=STRING --client-id=STRING --client-secret=STRING <paths> ... [flags]
    Delete files from the store
```

Policy stores: CLI upload (npx)
====================
## [](#%5Finstallation)Installation

`cerbosctl` binaries are published to npm for easy installation. To install the `cerbosctl` CLI tool, run the following command:

```sh
npm install -g cerbosctl
```

Alternatively, you can use `npx` to run the CLI without installing it globally.

## [](#%5Fusage)Usage

The `cerbosctl` CLI tool can be used to upload policies to a policy store in Cerbos Hub.

First generate a set of client credentials for the policy store in Cerbos Hub - you can do this in the **Client credentials** section in the UI. Make sure to select the `Read & Write` option when creating the credentials to allow uploading policies.

Then export the following environment variables with the values from the generated client credentials and the store ID:

```sh
export CERBOS_HUB_CLIENT_ID=...
export CERBOS_HUB_CLIENT_SECRET=...
export CERBOS_HUB_STORE_ID=...
```

The following command uploads policy files from the current directory and replaces all the files in the store.

### [](#%5Fvia%5Fglobal%5Fnpm%5Finstallation)via global NPM installation

```sh
cerbosctl hub store replace-files .
```

### [](#%5Fvia%5Fnpx)via npx

```sh
npx cerbosctl hub store replace-files .
```

## [](#%5Ffull%5Fcli%5Freference)Full CLI Reference

```none
Usage: cerbosctl hub store --store-id=STRING --client-id=STRING --client-secret=STRING <command> [flags]

Interact with Cerbos Hub managed stores.

Requires an existing managed store and the API credentials to access it. The store ID and credentials can be provided using either command-line flags or
environment variables.

Flags:
  -h, --help                    Show context-sensitive help.

      --store-id=STRING         ID of the store to operate on ($CERBOS_HUB_STORE_ID)
      --client-id=STRING        Client ID of the access credential ($CERBOS_HUB_CLIENT_ID)
      --client-secret=STRING    Client secret of the access credential ($CERBOS_HUB_CLIENT_SECRET)

Commands:
  hub store list-files --store-id=STRING --client-id=STRING --client-secret=STRING [flags]
    List store files

  hub store get-files --store-id=STRING --client-id=STRING --client-secret=STRING --output-path=STRING <files> ... [flags]
    Download files from the store

  hub store download --store-id=STRING --client-id=STRING --client-secret=STRING <output-path> [flags]
    Download the entire store

  hub store replace-files --store-id=STRING --client-id=STRING --client-secret=STRING <path> [flags]
    Overwrite the store with the given set of files

  hub store add-files --store-id=STRING --client-id=STRING --client-secret=STRING <paths> ... [flags]
    Add files to the store

  hub store delete-files --store-id=STRING --client-id=STRING --client-secret=STRING <paths> ... [flags]
    Delete files from the store
```

Cerbos Hub GitHub Integration
====================
The Cerbos Hub GitHub integration allows you to manage your policies in a GitHub repository. This integration supports both public and private repositories, enabling you to store your policies securely and manage them using Git workflows.

## [](#%5Fprerequisites)Prerequisites

Before you can use the Cerbos Hub GitHub integration, you need to have the following:

* A GitHub account.
* A GitHub repository where you want to store your policies.
* Permission to add a GitHub App to your repository.

## [](#%5Fsetting%5Fup%5Fthe%5Fgithub%5Fintegration)Setting Up the GitHub Integration

To set up the GitHub integration, follow these steps:

1. Go to [Cerbos Hub](https://hub.cerbos.cloud) and sign in.
2. Inside a workspace, create a new policy store by clicking on "Policy Stores" in the sidebar.
3. In the Import tab, select "GitHub" as the source for your policy store.
4. Follow the prompts to authorize the Cerbos Hub to access your GitHub account.
5. Select the repository you want to use for storing your policies.
6. Configure the branch or tag for the integration to track, and optionally a directory where your policies will be stored.![GitHub connection setup](_images/policy_store_github_connection_setup.png)
7. Click "Save" to complete the setup.

## [](#%5Fsyncing%5Fa%5Fsubdirectory)Syncing a subdirectory

If your policies are stored in a subdirectory of your repository, you can configure the store to sync only that path. This is useful when your authorization policies are part of a larger monorepo or when you want to organize policies into separate directories.

When configuring the GitHub connection, specify the path to the directory containing your policies in the directory field. Cerbos Hub will only sync files from that directory and its subdirectories. You can also sync hidden directories (those starting with a dot) if needed.

For example, if your repository structure looks like this:

my-repo/
├── src/
├── docs/
└── policies/
    └── cerbos/
        ├── resource_policies/
        └── derived_roles/

You would set the directory to `policies/cerbos` to sync only the Cerbos policy files.

## [](#%5Fusing%5Fthe%5Fgithub%5Fintegration)Using the GitHub Integration

Once the GitHub integration is set up, you can monitor and manage your policies directly in the GitHub connection tab. The integration will automatically sync changes made to the policies in your GitHub repository.

![GitHub connection status](_images/policy_store_github_connection.png)

To reconfigure the GitHub integration, you can click on the "Update configuration" button in the GitHub connection tab. This allows you to change the repository, branch, or directory settings.

Policy stores: .NET SDK
====================
The .NET SDK for policy stores allows you to interact with policy stores programmatically using .NET. This SDK provides a set of functions and types that make it easy to upload, manage, and retrieve policies from a policy store.

Find the .NET SDK on GitHub: <https://github.com/cerbos/cerbos-sdk-net>

Policy stores: Go SDK
====================
The Go SDK for policy stores allows you to interact with policy stores programmatically using Go. This SDK provides a set of functions and types that make it easy to upload, manage, and retrieve policies from a policy store.

Find the Go SDK on GitHub: <https://github.com/cerbos/cerbos-sdk-go>

Policy stores: Java SDK
====================
The Java SDK for policy stores allows you to interact with policy stores programmatically using Java. This SDK provides a set of functions and types that make it easy to upload, manage, and retrieve policies from a policy store.

Find the Java SDK on GitHub: <https://github.com/cerbos/cerbos-sdk-java>

Policy stores: JavaScript <code>@cerbos/hub</code> SDK
====================
The `@cerbos/hub` JavaScript SDK for policy stores allows you to interact with policy stores programmatically using JavaScript/TypeScript. This SDK provides a set of functions and types that make it easy to upload, manage, and retrieve policies from a policy store.

Find the JavaScript SDK on GitHub: <https://github.com/cerbos/cerbos-sdk-javascript/blob/main/packages/hub/README.md>

Policy stores: PHP SDK
====================
The PHP SDK for policy stores allows you to interact with policy stores programmatically using PHP. This SDK provides a set of functions and types that make it easy to upload, manage, and retrieve policies from a policy store.

Find the PHP SDK on GitHub: <https://github.com/cerbos/cerbos-sdk-php>

Policy stores: Python SDK
====================
The Python SDK for policy stores allows you to interact with policy stores programmatically using Python. This SDK provides a set of functions and types that make it easy to upload, manage, and retrieve policies from a policy store.

Find the Python SDK on GitHub: <https://github.com/cerbos/cerbos-sdk-python>

Policy stores: Rust SDK
====================
The Rust SDK for policy stores allows you to interact with policy stores programmatically using Rust. This SDK provides a set of functions and types that make it easy to upload, manage, and retrieve policies from a policy store.

Find the Rust SDK on GitHub: <https://github.com/cerbos/cerbos-sdk-rust>

Policy stores: Browser Upload
====================
The browser upload feature allows you to manually upload policy files directly to a policy store using the Cerbos Hub web interface. You can quickly add policies by selecting a ZIP file or by dragging and dropping the file into the designated area, without using a Git repository or CI/CD pipeline.

## [](#%5Fuploading%5Fpolicies)Uploading Policies

![Browser upload](_images/policy_store_upload.png)

To upload policies using the browser, follow these steps:

1. Go to [Cerbos Hub](https://hub.cerbos.cloud) and sign in.
2. Inside a workspace, create a new policy store by clicking on "Policy Stores" in the sidebar.
3. In the Import tab, select "Browser upload" as the source for your policy store.
4. Click on the "Upload files" button to select a ZIP file of your policies or drag and drop the ZIP file into the designated area.
5. Once the file is uploaded, the policies will be processed and added to the policy store.
6. You can then view and manage the uploaded policies in the policy store Policies tab.

| |  Uploading policies via the browser does a full replace of the existing policies in the store. If you want to append or update specific policies, consider using a Git repository or CI/CD pipeline instead. |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Policy stores
====================
Policy stores are flexible containers for Cerbos policy files managed inside Cerbos Hub. A store decouples policy storage from any specific source control system, letting each team choose the workflow that best fits its needs while Cerbos Hub guarantees validation, versioning, and secure delivery to [deployments](deployments.html).

## [](#%5Fwhy%5Fuse%5Fpolicy%5Fstores)Why use policy stores

Clear boundaries and ownership

Create one store per team, product, tenant, or environment so each group owns just the policies that matter to them, reducing cognitive load.

Independent update cadence

Teams can update their store at any time without blocking others, a new deployment is built only when you choose to combine the stores.

Layered policy logic

Combine multiple stores in a single deployment to apply global guard rails, platform defaults, application-level rules, and tenant overrides in a predictable hierarchy.

Source agnostic workflows

Populate a store from Git, a CI pipeline, the Cerbos Hub API, the [cerbosctl CLI](../cerbos/latest/cli/cerbosctl.html), or a direct UI upload, no GitHub lock-in.

Full visibility and auditability

View every policy file in Hub, see which store and commit contributed to a deployment, and trace any PDP decision back to the exact policy version.

## [](#%5Fsupported%5Fingestion%5Fmethods)Supported ingestion methods

| Method            | Typical use case                                                                                                                                                     |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Git repository    | Structured policy as code managed with pull requests and reviews. If you are using GitHub, you can connect your repository directly to a policy store in Cerbos Hub. |
| CI or CD pipeline | Push the policies produced by a build job, for example when generating service-specific policies or promoting between environments.                                  |
| Cerbos Hub SDKs   | Programmatic updates such as per-tenant roles, user-defined permissions, or event-driven changes.                                                                    |
| cerbosctl CLI     | Local scripting, quick one-off uploads, or integration into existing tooling.                                                                                        |
| Browser upload    | Ad hoc tweaks, demos, or importing legacy policy files.                                                                                                              |

## [](#%5Flife%5Fcycle%5Finside%5Fcerbos%5Fhub)Life-cycle inside Cerbos Hub

1. Create a store in **Cerbos Hub** workspace.
2. Add or update policy files using any supported ingestion method.
3. Automatic validation ensures policies are correctly formatted.
4. Reference the store in one or more deployments to build a versioned bundle.

## [](#%5Fstore%5Fdetail%5Fpage)Store detail page

Each policy store has a detail page with the following tabs:

Import

Add policies to the store by uploading files, connecting to a Git repository, or using other ingestion methods.

Policies

Browse the current contents of the store in a file tree. Select a version from the dropdown to view historical snapshots. Click **Create playground** to experiment with the policies in an isolated environment—this creates a playground pre-populated with all policies and tests from the store.

Version history

View a chronological list of all versions, showing when each was created and what changed.

Client credentials

Manage API credentials scoped to this store for programmatic access via SDKs or the CLI. Each credential shows its type (read-only or read and write), usage statistics, and when it was last used.

Settings

Configure store options and manage connections to external sources like GitHub.

## [](#%5Fbest%5Fpractices)Best practices

Use meaningful names

Name stores after their responsibility, for example security-global, platform-core, payments-service, or tenant-alpha.

Keep tests with policies

store-specific tests catch regressions early and run automatically on every change.

Protect production stores

Restrict write access and require review for stores that feed your production deployment.

Isolate dynamic inputs

Create a dedicated store for API-driven or user-defined policies to avoid mixing static and dynamic files.

Review store composition

Periodically confirm that each deployment references only the stores it needs and in the correct order.

Release notes
====================
## [](#%5F2026%5F01%5F28)2026-01-28

### [](#%5Frbac%5Fpolicy%5Fgenerator%5Fimprovements)RBAC policy generator improvements

The RBAC policy generator now displays role names more clearly by rotating the rule matrix headers, accommodating longer role names. Fixed a navigation issue in the wizard form that prevented users from going back to previous steps.

### [](#%5Fvariable%5Fexpression%5Fstability)Variable expression stability

Fixed an issue where invalid variable expressions could cause unexpected errors. The system now handles malformed expressions gracefully, improving reliability when authoring policies.

## [](#%5F2026%5F01%5F27)2026-01-27

### [](#%5Fembedded%5Fpdp%5Fdeploy%5Fhelper)Embedded PDP deploy helper

A new deployment helper modal guides you through deploying embedded PDPs. The helper dynamically shows scope filters and client credentials based on your rule requirements. Rules requiring authentication cannot run in-browser, so the helper clearly indicates when server-side deployment is necessary.

### [](#%5Fplayground%5Freadme%5Fimprovements)Playground README improvements

Enhanced the markdown viewer styling in the Playground. README content now updates in real-time when collaborators edit the file. Drag-and-drop file uploads now correctly handle markdown files.

## [](#%5F2026%5F01%5F26)2026-01-26

### [](#%5Fnew%5Fembedded%5Fpdp%5Farchitecture)New embedded PDP architecture

A completely redesigned [embedded policy decision point (ePDP)](deployments-epdp-rules.html) system replaces the previous implementation. The new architecture introduces ePDP rules, which provide fine-grained control over policy bundles served to client applications.

Key capabilities:

* **Per-deployment rules**: Each deployment can define multiple ePDP rules, allowing different bundle configurations for different clients or environments
* **Policy filtering**: Specify which resources, actions, scopes, roles, and versions to include, reducing bundle size and limiting exposure of server-side authorization logic
* **Dynamic scope filtering**: Require clients to specify scopes at fetch time, enabling multi-tenant architectures where each tenant receives only their applicable policies
* **Access controls**: Configure authentication requirements (public access or client credential) and IP allowlists per rule

A new JavaScript SDK (`@cerbos/embedded-client`) replaces the previous `@cerbos/embedded` package, with support for automatic bundle updates, deferred activation, and improved error handling. See the [SDK documentation](deployments-epdp-rules.html#%5Fjavascript%5Fsdk) for migration details.

The previous ePDP implementation remains available for existing users. See [legacy documentation](legacy/decision-points-embedded.html) for reference.

## [](#%5F2026%5F01%5F21)2026-01-21

### [](#%5Fpermissions%5Fmatrix%5Fview)Permissions matrix view

The playground now includes a matrix check view that displays permission evaluation results in a comprehensive grid format. This makes it easier to visualize how policies affect different principal and resource combinations during demos and policy development.

### [](#%5Fplayground%5Freadme%5Fsupport)Playground README support

Playgrounds now support README.md files that display as rendered markdown when opened. READMEs can include relative links to other files in the playground and external links (with a confirmation dialog). When opening a playground with a README and no file selected, the README displays automatically, making it easier to document and share playground examples. == 2026-01-05

### [](#%5Fcreate%5Fplayground%5Ffrom%5Fa%5Fstore)Create playground from a store

You can now create a playground directly from an existing policy store, making it easy to experiment with production policies in a safe, isolated environment. This feature streamlines the workflow for testing policy changes before deploying them, allowing you to iterate quickly without affecting live authorization decisions. You can also use a store’s policies as a starting point for developing new authorization rules, reducing the time needed to build and validate complex policy structures.

## [](#%5F2025%5F12%5F23)2025-12-23

### [](#%5Faudit%5Flog%5Fdeep%5Flinking)Audit log deep linking

Click on a policy referenced in an audit log entry to navigate directly to that policy in your policy store. This makes it easier to investigate authorization decisions and understand the policy logic that led to a specific outcome.

### [](#%5Fplayground%5Fzip%5Ffile%5Fsupport)Playground zip file support

You can now drag and drop zip files containing policies and tests directly into the playground. This simplifies loading entire policy sets for testing and collaboration.

## [](#%5F2025%5F12%5F01)2025-12-01

### [](#%5Ftest%5Fcase%5Foutput%5Fdiff%5Fview)Test case output diff view

When a test case fails, you can now view a side-by-side diff comparing the expected output with the actual output. This visual comparison makes it significantly easier to identify exactly what went wrong—whether it’s a missing permission, an unexpected denial, or an incorrect output value. By highlighting the specific differences, you can quickly understand the root cause and fix failing tests with confidence.

### [](#%5Fexecution%5Ftraces%5Fin%5Fplayground%5Fexplore%5Ftab)Execution traces in playground explore tab

Execution traces are now available directly in the playground’s explore tab, providing real-time visibility into how Cerbos evaluates your authorization requests. As you experiment with different principals, resources, and actions, you can inspect the complete policy evaluation path to understand exactly how decisions are made. This makes it easier to debug complex policy logic and verify that your authorization rules behave as expected before deploying them.

### [](#%5Faccessibility%5Fimprovements)Accessibility improvements

Icon-only buttons throughout the interface now have proper accessibility labels, ensuring screen reader users can navigate and interact with all controls effectively. Additionally, identifiers such as policy names, resource kinds, and action names are now displayed using a fixed-width font, improving readability and making it easier to scan lists of technical values.

## [](#%5F2025%5F11%5F06)2025-11-06

### [](#%5Fcombobox%5Finput%5Fimprovements)Combobox input improvements

Fixed an issue with combobox components when using multiselect and free-input modes together. This resolves problems that could occur when selecting multiple values while also entering custom text, ensuring a smoother form input experience throughout the Hub interface.

## [](#%5F2025%5F10%5F27)2025-10-27

### [](#%5Fstore%5Fimport%5Fwizard%5Ffix)Store import wizard fix

Fixed an issue that prevented the store import wizard from completing successfully in certain scenarios. The wizard now reliably guides you through importing policies from external sources, ensuring a smooth onboarding experience when migrating existing authorization rules into Cerbos Hub.

## [](#%5F2025%5F10%5F21)2025-10-21

### [](#%5Fexpired%5Finvitation%5Fhandling)Expired invitation handling

The system now properly handles expired invitations, displaying clear messages when users attempt to accept an invitation that is no longer valid. This prevents confusion and guides users to request a new invitation from their organization administrator, streamlining the team onboarding process.

## [](#%5F2025%5F10%5F08)2025-10-08

### [](#%5Fon%5Fpremises%5Fdeployment)On-premises deployment

Cerbos Hub is now available for on-premises deployment, giving you full control over your authorization management platform while maintaining all the features of the cloud-hosted service. On-premises deployment is available for enterprise customers. [Contact us](https://cerbos.dev/contact) to learn more.

### [](#%5Fworkspace%5Fname%5Fvalidation)Workspace name validation

Workspace names now require a minimum length, with immediate validation feedback in the creation form. This prevents issues that could arise from very short or ambiguous workspace names, helping teams maintain clear and consistent naming conventions across their organization.

### [](#%5Finvitation%5Fmanagement%5Fimprovements)Invitation management improvements

Improved handling when inviting users who are already members of an organization. The system now prevents duplicate invitations and provides clearer error messages explaining why an invitation cannot be sent. This reduces confusion for administrators managing team access and ensures invitation workflows remain straightforward.

### [](#%5Fbuild%5Fstatus%5Ffix)Build status fix

Fixed an issue where the wrong build status was displayed in the UI for certain policy stores. Build indicators now accurately reflect the current state of your policy compilation, giving you reliable feedback on whether your latest changes have been successfully processed.

## [](#%5F2025%5F09%5F09)2025-09-09

### [](#%5Fplayground%5Fdrag%5Fand%5Fdrop%5Fsupport)Playground drag-and-drop support

You can now drag-and-drop policy and test files from your local machine directly into the playground editor. This makes it easier to quickly load and test local policy files without needing to copy and paste.

## [](#%5F2025%5F09%5F01)2025-09-01

### [](#%5Fpolicy%5Fexecution%5Ftraces)Policy execution traces

Debugging complex authorization logic is now easier with policy execution traces. This feature provides a detailed, step-by-step view of how Cerbos evaluates a request, showing every rule, condition, and variable evaluation. Traces are available in the playground for real-time testing and in your deployment builds to provide production-level visibility, helping you quickly pinpoint why a specific decision was made.

### [](#%5Forganization%5Fusage%5Fdashboard)Organization usage dashboard

A new organization-level usage dashboard is now available, aggregating authorization metrics from all your workspaces into a single view. This dashboard provides a complete picture of request volumes, policy distribution, and usage trends across your entire organization. It helps platform owners and engineering leaders understand adoption patterns, identify which teams might need support, and discover optimization opportunities.

## [](#%5F2025%5F08%5F04)2025-08-04

### [](#%5Fusage%5Fdashboard)Usage dashboard

The new [Usage Dashboard](usage-dashboard.html) provides comprehensive observability into your authorization service. It allows you to monitor key metrics, view trends, and gain insights into how your Cerbos Hub workspace is utilized.

### [](#%5Fapi%5Fkey%5Flifecycle)API key lifecycle

Should an API key become blocked due to misconfiguration, you can now unblock it directly from the API key list.

## [](#%5F2025%5F07%5F17)2025-07-17

A major launch of the [Policy Stores](policy-stores.html) feature in Cerbos Hub, which allows you to store and manage your authorization policies more effectively. You can read more in the announcement blog post: [Updated Cerbos Hub](https://www.cerbos.dev/blog/updated-cerbos-hub-complete-authorization-solution-for-your-identity-fabrics).

## [](#%5F2025%5F07%5F09)2025-07-09

### [](#%5Faudit%5Flogs%5Fgeneral%5Favailability)Audit logs general availability

The audit logs feature is now generally available. The beta badge has been removed and the feature is ready for production use.

## [](#%5F2025%5F06%5F24)2025-06-24

### [](#%5Fgithub%5Fbacked%5Fpolicy%5Fstores)GitHub-backed policy stores

Policy stores can now be connected directly to GitHub repositories. Changes pushed to your repository are automatically synced to the store, and you can configure which branch and subdirectory to track. See [GitHub integration](policy-stores-git-github.html) for details.

## [](#%5F2025%5F06%5F03)2025-06-03

### [](#%5Fimport%5Fpolicies%5Fwizard)Import policies wizard

A new guided wizard helps you import existing policies into a managed policy store. Upload a zip file or connect to a Git repository to quickly populate a new store.

## [](#%5F2025%5F05%5F16)2025-05-16

### [](#%5Fbundle%5Ffile%5Fexplorer)Bundle file explorer

View the contents of policy bundles directly in Cerbos Hub. The build details page now includes a file explorer showing all policies included in the bundle and the ability to inspect individual files.

## [](#%5F2025%5F04%5F28)2025-04-28

### [](#%5Forganization%5Fdeletion)Organization deletion

You can now delete an organization in Cerbos Hub. To delete an organization, navigate to the organization settings page and click on the "Delete organization" button. Please note that this action is irreversible and will permanently delete all data associated with the organization.

## [](#%5F2025%5F03%5F19)2025-03-19

### [](#%5Frole%5Fpolicy%5Fand%5Fconstants%5Ftemplates)Role policy and constants templates

The playground template picker now includes examples for role policies and policy constants, making it easier to get started with these advanced policy features.

## [](#%5F2025%5F03%5F12)2025-03-12

### [](#%5Fplayground)Playground

The effective derived roles for a user are now displayed in the playground when evaluating policies. This feature helps you understand which derived roles were activated for that user during that request.

### [](#%5Fembedded%5Fpolicy%5Fdecision%5Fpoint)Embedded Policy Decision Point

Time-based functions used in condition expressions such as `getHours` and `getMinutes` default to UTC unless the time zone is explicitly provided as an argument to the function. It’s recommended to review your policies to make sure that time calculations use the correct time zone. Refer to [timestamps documentation](../cerbos/latest/policies/conditions.html#%5Ftimestamps) to identify the affected functions.

## [](#%5F2025%5F02%5F26)2025-02-26

### [](#%5Fembedded%5Fpolicy%5Fdecision%5Fpoint%5F2)Embedded Policy Decision Point

We’ve introduced support for capturing audit decision logs from the Cerbos Hub Embedded Policy Decision Points (ePDP) using the latest version of the [Cerbos Javascript SDK](https://github.com/cerbos/cerbos-sdk-javascript). This feature enables organizations to track and analyze authorization decisions made locally in embedded environments, ensuring complete visibility and auditability, without relying on a centralized PDP or Cerbos Hub.

## [](#%5F2025%5F02%5F01)2025-02-01

The Builds section of Cerbos Hub has been renamed Policies. The Policies section now includes all the features previously available in Builds, such as policy versioning, policy history, and policy deployment. The Builds section has been removed from the Cerbos Hub navigation.

## [](#%5F2025%5F01%5F28)2025-01-28

### [](#%5Fplayground%5F2)Playground

Added support for [globals](../cerbos/latest/configuration/engine.html#%5Fglobals) in playground engine settings. Global variables defined in the [playground settings](playground.html) are exposed to policy conditions via the `globals` object.

Reliability
====================
Cerbos Hub is designed for high availability. All PDPs continue to operate independently even when Cerbos Hub experiences disruptions.

## [](#%5Fpush%5Fbased%5Fupdates)Push-based updates

When a PDP connects to Cerbos Hub, it establishes a two-way communication channel used to receive the initial policy bundle and subsequent update notifications. Because there is no polling, all PDPs converge on the same policy version within seconds of a change.

## [](#%5Fdisconnection%5Fhandling)Disconnection handling

If Cerbos Hub becomes temporarily unavailable:

| Running PDPs | Continue serving requests using the last downloaded bundle while attempting to reconnect in the background. Authorization decisions are unaffected. |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| New PDPs     | Can start with the last successfully built bundle, served from a separate high-availability fallback service.                                       |

## [](#%5Flocal%5Fbundle%5Fcaching)Local bundle caching

For additional resilience, configure a cache directory to persist bundles to disk:

```yaml
storage:
  driver: hub
  hub:
    remote:
      deploymentID: "..."
      cacheDir: /var/cerbos/hub # Directory to cache downloaded bundles
```

Mount a persistent volume at this path when running in containers or Kubernetes. Cached bundles allow PDPs to restart without network access to Cerbos Hub.

## [](#%5Foffline%5Fmode)Offline mode

In disaster recovery scenarios, start the PDP with only the cached bundle:

```shell
docker run --rm --name cerbos \
  -p 3592:3592 -p 3593:3593 \
  -e CERBOS_HUB_OFFLINE=true \
  -v /var/cerbos/hub:/var/cerbos/hub \
  ghcr.io/cerbos/cerbos:latest server --config=/conf/.cerbos.yaml
```

The PDP loads the cached bundle and serves requests without connecting to Cerbos Hub.

## [](#%5Ffallback%5Fto%5Fgit)Fallback to git

As a last resort, switch the PDP to read policies directly from your Git repository:

```yaml
storage:
  driver: git
  git:
    protocol: https
    url: https://github.com/your-org/policies.git
    branch: main
    checkoutDir: /tmp/cerbos/policies
    updatePollInterval: 60s
```

This bypasses Cerbos Hub entirely, though you lose pre-compilation, testing, and centralized management.

## [](#%5Fmonitoring%5Fconnectivity)Monitoring connectivity

Monitor PDP connectivity using the `cerbos_dev_hub_connected` Prometheus metric:

| 1 | PDP is connected to Cerbos Hub            |
| - | ----------------------------------------- |
| 0 | PDP is disconnected (using cached bundle) |

Additional metrics for bundle operations:

| cerbos\_dev\_store\_bundle\_updates\_count       | Number of bundle updates received from Cerbos Hub |
| ------------------------------------------------ | ------------------------------------------------- |
| cerbos\_dev\_store\_bundle\_op\_latency          | Time to perform bundle operations                 |
| cerbos\_dev\_store\_bundle\_fetch\_errors\_count | Count of errors during bundle downloads           |

See [Observability](../cerbos/latest/configuration/observability.html) for the full list of available metrics.

Troubleshooting
====================
## [](#%5Fpdp%5Fconnection%5Fissues)PDP connection issues

### [](#%5Fpdp%5Ffails%5Fto%5Fconnect%5Fto%5Fcerbos%5Fhub)PDP fails to connect to Cerbos Hub

**Symptoms**: PDP logs show connection errors or timeouts when starting.

**Causes and solutions**:

| Invalid credentials  | Verify the client ID and client secret are correct. Generate new credentials from the deployment’s **Client credentials** tab if needed. |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Wrong deployment ID  | Confirm the deployment ID matches the deployment you want to connect to. Find the ID on the deployment detail page.                      |
| Network restrictions | Ensure outbound HTTPS (port 443) is allowed to Cerbos Hub endpoints. Check firewalls, security groups, and network policies.             |
| Expired credentials  | Client credentials do not expire, but they can be revoked. Check the credential status in Cerbos Hub.                                    |

### [](#%5Fpdp%5Fshows%5Fas%5Fdisconnected%5Fin%5Fcerbos%5Fhub)PDP shows as disconnected in Cerbos Hub

**Symptoms**: The PDP appears in the Decision points tab but shows as disconnected or has a stale "Last seen" timestamp.

**Causes and solutions**:

| Network interruption  | The PDP will automatically reconnect when network access is restored. Check for intermittent connectivity issues.            |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| PDP process crashed   | Verify the PDP container or process is running. Check logs for crash reasons.                                                |
| Load balancer timeout | Some load balancers close idle connections. The PDP maintains a heartbeat, but aggressive timeouts may cause disconnections. |

## [](#%5Fpolicy%5Fcompilation%5Ferrors)Policy compilation errors

### [](#%5Fbuild%5Ffails%5Fwith%5Fcompilation%5Ferrors)Build fails with compilation errors

**Symptoms**: The deployment build fails and shows compilation errors in the build details.

**Causes and solutions**:

| Invalid YAML syntax          | Check for indentation errors, missing colons, or invalid characters. Use a YAML linter locally before pushing.                                             |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Invalid policy structure     | Ensure policies follow the [Cerbos policy schema](../cerbos/latest/policies/index.html). Common issues include misspelled keys or missing required fields. |
| Duplicate policy definitions | Each resource/action combination must be unique within a scope. Check for conflicting policies across stores.                                              |
| Invalid CEL expressions      | Condition expressions must be valid CEL syntax. Test expressions in the playground before deploying.                                                       |

### [](#%5Ftests%5Ffail%5Fduring%5Fbuild)Tests fail during build

**Symptoms**: Compilation succeeds but tests fail, blocking deployment.

**Causes and solutions**:

| Policy behavior changed     | Review the test diff in the build details to understand what changed. Update tests if the new behavior is intentional. |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Missing test fixtures       | Ensure all principals, resources, and auxiliary data referenced in tests exist in the test fixtures.                   |
| Incorrect expected outcomes | Verify the expected actions and effects in your test cases match the policy logic.                                     |

## [](#%5Fembedded%5Fpdp%5Fissues)Embedded PDP issues

### [](#%5Fbundle%5Ffetch%5Ffails%5Fin%5Fbrowser)Bundle fetch fails in browser

**Symptoms**: The ePDP client throws errors when fetching the policy bundle.

**Causes and solutions**:

| CORS blocking requests  | Browser security prevents cross-origin requests. ePDP bundles are served with appropriate CORS headers, but ensure you’re using the correct endpoint. |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication required | If the ePDP rule requires authentication, provide credentials when initializing the client. Check the rule’s access control settings.                 |
| IP not in allowlist     | If the rule has an IP allowlist, ensure the client’s IP address is included. For browser clients, this is the end user’s IP.                          |
| Rule disabled           | Verify the ePDP rule is enabled in the deployment settings.                                                                                           |
| Invalid rule ID         | Confirm the rule ID matches an existing rule in the deployment.                                                                                       |

### [](#%5Fscope%5Fparameter%5Frequired)Scope parameter required

**Symptoms**: Bundle fetch fails with "scope parameter required" error.

**Causes and solutions**:

The ePDP rule has **Require scopes at fetch time** enabled. You must provide scope parameters when initializing the client:

```typescript
const cerbos = new Embedded({
  policies: {
    ruleId: "<RULE_ID>",
    scopes: ["tenant-acme"],
  },
  wasm,
});
```

### [](#%5Fauthorization%5Freturns%5Funexpected%5Fresults)Authorization returns unexpected results

**Symptoms**: The ePDP allows or denies actions differently than expected.

**Causes and solutions**:

| Filtered policies | The ePDP bundle may not contain all policies. Check the rule’s filtering settings (resources, actions, scopes, roles, versions) to ensure required policies are included.                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Stale bundle      | If policies were recently updated, the client may still have an old bundle. For long-running applications, enable automatic updates. For serverless, each invocation fetches the current bundle. |
| Missing globals   | If policies reference global variables, ensure they are passed in the client configuration.                                                                                                      |
| Scope mismatch    | If using scopes, verify the request scope matches policies in the filtered bundle.                                                                                                               |

## [](#%5Faudit%5Flog%5Fcollection%5Fissues)Audit log collection issues

### [](#%5Faudit%5Flogs%5Fnot%5Fappearing%5Fin%5Fcerbos%5Fhub)Audit logs not appearing in Cerbos Hub

**Symptoms**: The PDP is connected but no audit logs appear in the Audit logs tab.

**Causes and solutions**:

| Audit backend not configured      | Ensure audit.backend is set to hub in the PDP configuration.                                          |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Audit disabled                    | Verify audit.enabled is true.                                                                         |
| Storage path missing              | The audit.hub.storagePath must be set to a writable directory. Without this, logs cannot be buffered. |
| Credentials lack write permission | Audit log upload requires **Read & write** credentials. Read-only credentials cannot upload logs.     |

### [](#%5Flogs%5Fdelayed%5For%5Fmissing%5Fentries)Logs delayed or missing entries

**Symptoms**: Audit logs appear with significant delay or some entries are missing.

**Causes and solutions**:

| Network issues          | Logs are buffered locally and uploaded when connectivity is available. Check for intermittent network problems.                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Storage volume full     | If the local storage path runs out of space, new logs cannot be buffered. Monitor disk usage on the storage volume.                                                          |
| PDP crashed before sync | Logs are periodically synced to Cerbos Hub. If the PDP crashes between syncs, recent entries may be lost. Use a persistent volume to preserve buffered logs across restarts. |

## [](#%5Fgithub%5Fintegration%5Fissues)GitHub integration issues

### [](#%5Fbuilds%5Farent%5Ftriggered%5Fwhen%5Fmultiple%5Ftags%5Fare%5Fpushed)Builds aren’t triggered when multiple tags are pushed

GitHub has a [known limitation](https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads#push) where connected apps like Cerbos Hub won’t receive notifications for repository changes if more than three tags are pushed simultaneously. To avoid this issue, limit the maximum number of references pushed at once to three. See the [GitHub documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-push-policy-for-your-repository#limiting-how-many-branches-and-tags-can-be-updated-in-a-single-push) for configuration details.

### [](#%5Frepository%5Fchanges%5Fnot%5Fdetected)Repository changes not detected

**Symptoms**: Pushing to the connected repository doesn’t trigger a new build.

**Causes and solutions**:

| Wrong branch            | Verify you’re pushing to the branch configured in the policy store settings.                    |
| ----------------------- | ----------------------------------------------------------------------------------------------- |
| Webhook disabled        | Check that the GitHub webhook for Cerbos Hub is active in your repository settings.             |
| No policy files changed | Builds only trigger when policy files (.yaml, .yml) change. Changes to other files are ignored. |

Usage dashboard
====================
The Usage Dashboard provides comprehensive observability into your authorization service, allowing you to monitor key metrics, view trends, and gain insights into how your Cerbos Hub workspace is utilized. At the organization level, the dashboard aggregates authorization metrics from all your workspaces into a single view, giving platform owners and engineering leaders a complete picture of request volumes, policy distribution, and usage trends across the entire organization.

## [](#%5Fsummary%5Fmetrics)Summary metrics

The top of the dashboard displays three key metrics for the current month, each showing the change from the previous month:

Active principals

The number of unique principals (users, services, or applications) making authorization requests. Track this to understand adoption and identify unexpected usage patterns.

Decisions

The total number of authorization decisions made via the Check API. A single API call can check multiple actions, so this count may exceed the number of calls.

Query plans

The total number of Plan API calls used to generate query filters for data access.

## [](#%5Ftrend%5Fcharts)Trend charts

### [](#%5Factive%5Fprincipals)Active principals

A line chart showing the number of unique principals over time. Use this to identify growth trends, seasonal patterns, or unexpected drops in usage.

### [](#%5Fcheck%5Fcalls)Check calls

A stacked bar chart showing Check API activity by month, broken down by outcome:

* **Check calls**: Total number of Check API requests
* **Allowed actions**: Decisions that granted access
* **Denied actions**: Decisions that rejected access

A sudden spike in denied actions could indicate policy changes that are stricter than intended, requests for policies that don’t exist, or application issues such as typos in resource or action names.

### [](#%5Fplan%5Fcalls)Plan calls

A stacked bar chart showing Plan API activity by month, broken down by outcome:

* **Plan calls**: Total number of Plan API requests
* **Allowed actions**: Plans that grant unconditional access
* **Denied actions**: Plans that deny access unconditionally
* **Conditional actions**: Plans that include conditions to filter data

This breakdown helps you understand how query planning is being used to generate database filters and conditional access patterns.

## [](#%5Fusage%5Fdetails)Usage details

The table at the bottom provides month-by-month metrics with the following columns:

| Column            | Description                                                                         |
| ----------------- | ----------------------------------------------------------------------------------- |
| Month             | The calendar month for this row of data                                             |
| Call type         | Whether the row represents Check or Plan API calls                                  |
| Unique principals | Count of distinct principals making requests of this type                           |
| Total calls       | Number of API calls made                                                            |
| Call breakdown    | Visual breakdown showing allowed, denied, and (for Plan calls) conditional outcomes |

User management
====================
A Cerbos Hub user can have a role at the organization level and an optional set of roles for each workspace. All of these roles are considered when determining the permissions for any particular user.

## [](#%5Forganization%5Froles)Organization roles

Organization roles, except for the `Member` role, apply to all workspaces within the organization. Users with organizational role of `Member` must be explicitly granted workspace roles in order to access a workspace.

| Action                        | Owner | Developer | Analyst | Viewer | Member |
| ----------------------------- | ----- | --------- | ------- | ------ | ------ |
| View organization             | ✅     | ✅         | ✅       | ✅      | ✅      |
| Modify organization           | ✅     | ❌         | ❌       | ❌      | ❌      |
| Manage members                | ✅     | ❌         | ❌       | ❌      | ❌      |
| Invite a member               | ✅     | ❌         | ❌       | ❌      | ❌      |
| Create a workspace            | ✅     | ✅         | ✅       | ✅      | ✅      |
| Create a playground           | ✅     | ✅         | ✅       | ✅      | ✅      |
| Update a playground           | ✅     | ✅         | ✅       | ✅      | ✅      |
| Delete a playground           | ✅     | ✅         | ✅       | ✅      | ✅      |
| Export a playground           | ✅     | ✅         | ✅       | ✅      | ✅      |
| Connect a PDP to a playground | ✅     | ✅         | ✅       | ✅      | ✅      |

## [](#%5Fworkspace%5Froles)Workspace Roles

Permissions assigned at the organization level are inherited by all workspaces. Additionally, a user can be assigned specific roles within a workspace, potentially granting more permissions for that particular workspace only.

| Action                   | Owner | Developer | Analyst | Viewer |
| ------------------------ | ----- | --------- | ------- | ------ |
| View a workspace         | ✅     | ✅         | ✅       | ✅      |
| View builds              | ✅     | ✅         | ✅       | ✅      |
| View decision points     | ✅     | ✅         | ✅       | ✅      |
| View issues              | ✅     | ✅         | ✅       | ✅      |
| View audit logs          | ✅     | ❌         | ✅       | ❌      |
| Manage API keys          | ✅     | ✅         | ❌       | ❌      |
| Reset encryption key     | ✅     | ❌         | ❌       | ❌      |
| Manage workspace members | ✅     | ❌         | ❌       | ❌      |
| Modify workspace         | ✅     | ❌         | ❌       | ❌      |
| Delete a workspace       | ✅     | ❌         | ❌       | ❌      |

## [](#%5Fdeleting%5Fan%5Forganization)Deleting an organization

Organizations can be deleted by navigating to the organization settings page and clicking **Delete organization**. This action is irreversible and permanently deletes all data associated with the organization, including all workspaces, policy stores, deployments, and audit logs.