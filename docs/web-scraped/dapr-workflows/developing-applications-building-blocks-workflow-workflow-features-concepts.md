# Source: https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/

Title: Features and concepts

URL Source: https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/

Markdown Content:
Features and concepts | Dapr Docs
===============
[Dapr Docs](https://docs.dapr.io/)

*   [Homepage](https://dapr.io/)
*   [GitHub](https://github.com/dapr)
*   [Blog](https://blog.dapr.io/posts)
*   [Discord](https://bit.ly/dapr-discord)
*   [Community](https://dapr.io/community)
*   
[v1.17 (latest)](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#)
    *   [v1.18 (preview)](https://v1-18.docs.dapr.io/)
    *   [v1.17 (latest)](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#)
    *   [v1.16 (latest)](https://v1-16.docs.dapr.io/)
    *   [v1.15](https://v1-15.docs.dapr.io/)
    *   [v1.14](https://v1-14.docs.dapr.io/)
    *   [v1.13](https://v1-13.docs.dapr.io/)
    *   [v1.12](https://v1-12.docs.dapr.io/)
    *   [v1.11](https://v1-11.docs.dapr.io/)
    *   [v1.10](https://v1-10.docs.dapr.io/)
    *   [v1.9](https://v1-9.docs.dapr.io/)
    *   [v1.8](https://v1-8.docs.dapr.io/)
    *   [v1.7](https://v1-7.docs.dapr.io/)

*   
[English](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#)
    *   [简体中文](https://docs.dapr.io/zh-hans/developing-applications/building-blocks/workflow/workflow-features-concepts/)

Search

[English](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#)
*   [简体中文](https://docs.dapr.io/zh-hans/developing-applications/building-blocks/workflow/workflow-features-concepts/)

*   [](https://docs.dapr.io/)
    *   [Concepts](https://docs.dapr.io/concepts/ "Dapr concepts")
        *   [Overview](https://docs.dapr.io/concepts/overview/)
        *   [Building blocks](https://docs.dapr.io/concepts/building-blocks-concept/)
        *   [Components](https://docs.dapr.io/concepts/components-concept/)
        *   [Configuration](https://docs.dapr.io/concepts/configuration-concept/ "Application and control plane configuration")
        *   [Resiliency](https://docs.dapr.io/concepts/resiliency-concept/)
        *   [Observability](https://docs.dapr.io/concepts/observability-concept/)
        *   [Security](https://docs.dapr.io/concepts/security-concept/)
        *   [Isolation](https://docs.dapr.io/concepts/isolation-concept/)
        *   [Dapr services](https://docs.dapr.io/concepts/dapr-services/ "Overview of the Dapr services")
            *   [Sidecar](https://docs.dapr.io/concepts/dapr-services/sidecar/ "Dapr sidecar (daprd) overview")
            *   [Operator](https://docs.dapr.io/concepts/dapr-services/operator/ "Dapr Operator control plane service overview")
            *   [Placement](https://docs.dapr.io/concepts/dapr-services/placement/ "Dapr Placement control plane service overview")
            *   [Scheduler](https://docs.dapr.io/concepts/dapr-services/scheduler/ "Dapr Scheduler control plane service overview")
            *   [Sentry](https://docs.dapr.io/concepts/dapr-services/sentry/ "Dapr Sentry control plane service overview")
            *   [Sidecar injector](https://docs.dapr.io/concepts/dapr-services/sidecar-injector/ "Dapr Sidecar Injector control plane service overview")

        *   [Terminology](https://docs.dapr.io/concepts/terminology/ "Dapr terminology and definitions")
        *   [FAQs](https://docs.dapr.io/concepts/faq/ "Frequently asked questions and answers")
            *   [General questions](https://docs.dapr.io/concepts/faq/faq/ "General Dapr questions and answers")
            *   [Service meshes](https://docs.dapr.io/concepts/faq/service-mesh/ "Dapr and service meshes")

    *   [Getting started](https://docs.dapr.io/getting-started/ "Getting started with Dapr")
        *   [Install Dapr CLI](https://docs.dapr.io/getting-started/install-dapr-cli/ "Install the Dapr CLI")
        *   [Init Dapr locally](https://docs.dapr.io/getting-started/install-dapr-selfhost/ "Initialize Dapr in your local environment")
        *   [Use the Dapr API](https://docs.dapr.io/getting-started/get-started-api/)
        *   [Dapr Quickstarts](https://docs.dapr.io/getting-started/quickstarts/)
            *   [Service Invocation](https://docs.dapr.io/getting-started/quickstarts/serviceinvocation-quickstart/ "Quickstart: Service Invocation")
            *   [Publish and Subscribe](https://docs.dapr.io/getting-started/quickstarts/pubsub-quickstart/ "Quickstart: Publish and Subscribe")
            *   [Workflow](https://docs.dapr.io/getting-started/quickstarts/workflow-quickstart/ "Quickstart: Workflow")
            *   [State Management](https://docs.dapr.io/getting-started/quickstarts/statemanagement-quickstart/ "Quickstart: State Management")
            *   [Bindings](https://docs.dapr.io/getting-started/quickstarts/bindings-quickstart/ "Quickstart: Input & Output Bindings")
            *   [Actors](https://docs.dapr.io/getting-started/quickstarts/actors-quickstart/ "Quickstart: Actors")
            *   [Secrets Management](https://docs.dapr.io/getting-started/quickstarts/secrets-quickstart/ "Quickstart: Secrets Management")
            *   [Configuration](https://docs.dapr.io/getting-started/quickstarts/configuration-quickstart/ "Quickstart: Configuration")
            *   [Cryptography](https://docs.dapr.io/getting-started/quickstarts/cryptography-quickstart/ "Quickstart: Cryptography")
            *   [Jobs](https://docs.dapr.io/getting-started/quickstarts/jobs-quickstart/ "Quickstart: Jobs")
            *   [Conversation](https://docs.dapr.io/getting-started/quickstarts/conversation-quickstart/ "Quickstart: Conversation")
            *   [Resiliency](https://docs.dapr.io/getting-started/quickstarts/resiliency/ "Resiliency Quickstarts")
                *   [Resiliency: Service-to-component](https://docs.dapr.io/getting-started/quickstarts/resiliency/resiliency-state-quickstart/ "Quickstart: Service-to-component resiliency")
                *   [Resiliency: Service-to-service](https://docs.dapr.io/getting-started/quickstarts/resiliency/resiliency-serviceinvo-quickstart/ "Quickstart: Service-to-service resiliency")

        *   [Dapr Tutorials](https://docs.dapr.io/getting-started/tutorials/)
            *   [Define a component](https://docs.dapr.io/getting-started/tutorials/get-started-component/)
            *   [Configure state & pub/sub](https://docs.dapr.io/getting-started/tutorials/configure-state-pubsub/ "Tutorial: Configure state store and pub/sub message broker")

    *   [Developing applications](https://docs.dapr.io/developing-applications/ "Developing applications with Dapr")
        *   [Building blocks](https://docs.dapr.io/developing-applications/building-blocks/)
            *   [Service invocation](https://docs.dapr.io/developing-applications/building-blocks/service-invocation/)
                *   [Overview](https://docs.dapr.io/developing-applications/building-blocks/service-invocation/service-invocation-overview/ "Service invocation overview")
                *   [How-To: Invoke with HTTP](https://docs.dapr.io/developing-applications/building-blocks/service-invocation/howto-invoke-discover-services/ "How-To: Invoke services using HTTP")
                *   [How-To: Invoke with gRPC](https://docs.dapr.io/developing-applications/building-blocks/service-invocation/howto-invoke-services-grpc/ "How-To: Invoke services using gRPC")
                *   [How-To: Invoke Non-Dapr Endpoints](https://docs.dapr.io/developing-applications/building-blocks/service-invocation/howto-invoke-non-dapr-endpoints/ "How-To: Invoke Non-Dapr Endpoints using HTTP")
                *   [How to: Service invocation namespaces](https://docs.dapr.io/developing-applications/building-blocks/service-invocation/service-invocation-namespaces/ "How to: Service invocation across namespaces")

            *   [Publish & subscribe](https://docs.dapr.io/developing-applications/building-blocks/pubsub/ "Publish & subscribe messaging")
                *   [Overview](https://docs.dapr.io/developing-applications/building-blocks/pubsub/pubsub-overview/ "Publish and subscribe overview")
                *   [How to: Publish & subscribe to topics](https://docs.dapr.io/developing-applications/building-blocks/pubsub/howto-publish-subscribe/ "How to: Publish a message and subscribe to a topic")
                *   [Messages with Cloudevents](https://docs.dapr.io/developing-applications/building-blocks/pubsub/pubsub-cloudevents/ "Publishing & subscribing messages with Cloudevents")
                *   [Messages without CloudEvents](https://docs.dapr.io/developing-applications/building-blocks/pubsub/pubsub-raw/ "Publishing & subscribing messages without CloudEvents")
                *   [How-To: Route events](https://docs.dapr.io/developing-applications/building-blocks/pubsub/howto-route-messages/ "How-To: Route messages to different event handlers")
                *   [Subscription types](https://docs.dapr.io/developing-applications/building-blocks/pubsub/subscription-methods/ "Declarative, streaming, and programmatic subscription types")
                *   [Dead Letter Topics](https://docs.dapr.io/developing-applications/building-blocks/pubsub/pubsub-deadletter/)
                *   [How to: Namespace consumer groups](https://docs.dapr.io/developing-applications/building-blocks/pubsub/howto-namespace/ "How to: Set up pub/sub namespace consumer groups")
                *   [How to: Horizontally scale subscribers with StatefulSets](https://docs.dapr.io/developing-applications/building-blocks/pubsub/howto-subscribe-statefulset/)
                *   [Scope topic access](https://docs.dapr.io/developing-applications/building-blocks/pubsub/pubsub-scopes/ "Scope Pub/sub topic access")
                *   [Message TTL](https://docs.dapr.io/developing-applications/building-blocks/pubsub/pubsub-message-ttl/ "Message Time-to-Live (TTL)")
                *   [Publish and subscribe to bulk messages](https://docs.dapr.io/developing-applications/building-blocks/pubsub/pubsub-bulk/)

            *   [Workflow](https://docs.dapr.io/developing-applications/building-blocks/workflow/)
                *   [Overview](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-overview/ "Workflow overview")
                *   [Features and concepts](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/)
                *   [Workflow versioning](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-versioning/)
                *   [Workflow patterns](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-patterns/)
                *   [Workflow architecture](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/)
                *   [How to: Author workflows](https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-author-workflow/ "How to: Author a workflow")
                *   [How to: Manage workflows](https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-manage-workflow/)
                *   [Multi Application Workflows](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-multi-app/)
                *   [History Retention Policy](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-history-retention-policy/)
                *   [Workflow Execution Concurrency](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-concurrency/)

            *   [State management](https://docs.dapr.io/developing-applications/building-blocks/state-management/)
                *   [Overview](https://docs.dapr.io/developing-applications/building-blocks/state-management/state-management-overview/ "State management overview")
                *   [How-To: Save & get state](https://docs.dapr.io/developing-applications/building-blocks/state-management/howto-get-save-state/ "How-To: Save and get state")
                *   [How-To: Query state](https://docs.dapr.io/developing-applications/building-blocks/state-management/howto-state-query-api/)
                *   [How-To: Build a stateful service](https://docs.dapr.io/developing-applications/building-blocks/state-management/howto-stateful-service/)
                *   [How-To: Enable the transactional outbox pattern](https://docs.dapr.io/developing-applications/building-blocks/state-management/howto-outbox/)
                *   [How-To: Share state between applications](https://docs.dapr.io/developing-applications/building-blocks/state-management/howto-share-state/)
                *   [How-To: Encrypt state](https://docs.dapr.io/developing-applications/building-blocks/state-management/howto-encrypt-state/ "How-To: Encrypt application state")
                *   [Backend stores](https://docs.dapr.io/developing-applications/building-blocks/state-management/query-state-store/ "Work with backend state stores")
                    *   [Azure Cosmos DB](https://docs.dapr.io/developing-applications/building-blocks/state-management/query-state-store/query-cosmosdb-store/)
                    *   [Redis](https://docs.dapr.io/developing-applications/building-blocks/state-management/query-state-store/query-redis-store/)
                    *   [SQL server](https://docs.dapr.io/developing-applications/building-blocks/state-management/query-state-store/query-sqlserver-store/)

                *   [State TTL](https://docs.dapr.io/developing-applications/building-blocks/state-management/state-store-ttl/ "State Time-to-Live (TTL)")

            *   [Bindings](https://docs.dapr.io/developing-applications/building-blocks/bindings/)
                *   [Overview](https://docs.dapr.io/developing-applications/building-blocks/bindings/bindings-overview/ "Bindings overview")
                *   [How-To: Input bindings](https://docs.dapr.io/developing-applications/building-blocks/bindings/howto-triggers/ "How-To: Trigger your application with input bindings")
                *   [How-To: Output bindings](https://docs.dapr.io/developing-applications/building-blocks/bindings/howto-bindings/ "How-To: Use output bindings to interface with external resources")

            *   [Actors](https://docs.dapr.io/developing-applications/building-blocks/actors/)
                *   [Overview](https://docs.dapr.io/developing-applications/building-blocks/actors/actors-overview/ "Actors overview")
                *   [Runtime features](https://docs.dapr.io/developing-applications/building-blocks/actors/actors-features-concepts/ "Actor runtime features")
                *   [Runtime configuration](https://docs.dapr.io/developing-applications/building-blocks/actors/actors-runtime-config/ "Actor runtime configuration parameters")
                *   [Namespaced actors](https://docs.dapr.io/developing-applications/building-blocks/actors/namespaced-actors/)
                *   [Timers and reminders](https://docs.dapr.io/developing-applications/building-blocks/actors/actors-timers-reminders/ "Actors timers and reminders")
                *   [How-To: Interact with virtual actors](https://docs.dapr.io/developing-applications/building-blocks/actors/howto-actors/ "How-to: Interact with virtual actors using scripting")
                *   [How-To: Actor reentrancy](https://docs.dapr.io/developing-applications/building-blocks/actors/actor-reentrancy/ "How-to: Enable and use actor reentrancy in Dapr")

            *   [Secrets management](https://docs.dapr.io/developing-applications/building-blocks/secrets/)
                *   [Overview](https://docs.dapr.io/developing-applications/building-blocks/secrets/secrets-overview/ "Secrets management overview")
                *   [How To: Retrieve a secret](https://docs.dapr.io/developing-applications/building-blocks/secrets/howto-secrets/)
                *   [How To: Use secret scoping](https://docs.dapr.io/developing-applications/building-blocks/secrets/secrets-scopes/)

            *   [Configuration](https://docs.dapr.io/developing-applications/building-blocks/configuration/)
                *   [Overview](https://docs.dapr.io/developing-applications/building-blocks/configuration/configuration-api-overview/ "Configuration overview")
                *   [How-To: Manage configuration from a store](https://docs.dapr.io/developing-applications/building-blocks/configuration/howto-manage-configuration/)

            *   [Distributed lock](https://docs.dapr.io/developing-applications/building-blocks/distributed-lock/)
                *   [Overview](https://docs.dapr.io/developing-applications/building-blocks/distributed-lock/distributed-lock-api-overview/ "Distributed lock overview")
                *   [How-To: Use a lock](https://docs.dapr.io/developing-applications/building-blocks/distributed-lock/howto-use-distributed-lock/)

            *   [Cryptography](https://docs.dapr.io/developing-applications/building-blocks/cryptography/)
                *   [Overview](https://docs.dapr.io/developing-applications/building-blocks/cryptography/cryptography-overview/ "Cryptography overview")
                *   [How to: Use cryptography](https://docs.dapr.io/developing-applications/building-blocks/cryptography/howto-cryptography/ "How to: Use the cryptography APIs")

            *   [Jobs](https://docs.dapr.io/developing-applications/building-blocks/jobs/)
                *   [Overview](https://docs.dapr.io/developing-applications/building-blocks/jobs/jobs-overview/ "Jobs overview")
                *   [Features and concepts](https://docs.dapr.io/developing-applications/building-blocks/jobs/jobs-features-concepts/)
                *   [How-To: Schedule and handle triggered jobs](https://docs.dapr.io/developing-applications/building-blocks/jobs/howto-schedule-and-handle-triggered-jobs/)

            *   [Conversation](https://docs.dapr.io/developing-applications/building-blocks/conversation/)
                *   [Overview](https://docs.dapr.io/developing-applications/building-blocks/conversation/conversation-overview/ "Conversation overview")
                *   [How-To: Converse](https://docs.dapr.io/developing-applications/building-blocks/conversation/howto-conversation-layer/ "How-To: Converse with an LLM using the conversation API")

        *   [SDKs](https://docs.dapr.io/developing-applications/sdks/ "Dapr Software Development Kits (SDKs)")
            *   [.NET](https://docs.dapr.io/developing-applications/sdks/dotnet/ "Dapr .NET SDK")
                *   [Client](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-client/ "Getting started with the Dapr client .NET SDK")
                    *   [DaprClient usage](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-client/dotnet-daprclient-usage/)

                *   [Workflow](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-workflow/ "Dapr Workflow .NET SDK")
                    *   [DaprWorkflowClient registration](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-workflow/dotnet-workflowclient-usage/ "DaprWorkflowClient lifetime management and registration")
                    *   [Workflow serialization](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-workflow/dotnet-workflow-serialization/ "Workflow serialization in the .NET SDK")
                    *   [Multi-app workflows](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-workflow/dotnet-workflow-multi-app/ "Multi-application workflows in the .NET SDK")
                    *   [Workflow management operations](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-workflow/dotnet-workflow-management-methods/ "Workflow management operations with DaprWorkflowClient")
                    *   [Workflow versioning](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-workflow/dotnet-workflow-versioning/ "Workflow versioning in the .NET SDK")
                    *   [Workflow examples on GitHub](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-workflow/dotnet-workflow-examples/ ".NET Workflow Examples")

                *   [Actors](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-actors/ "Dapr actors .NET SDK")
                    *   [Actors client](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-actors/dotnet-actors-client/ "The IActorProxyFactory interface")
                    *   [Authoring actors](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-actors/dotnet-actors-usage/ "Author & run actors")
                    *   [Actor serialization](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-actors/dotnet-actors-serialization/ "Actor serialization in the .NET SDK")
                    *   [How to: Run & use virtual actors](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-actors/dotnet-actors-howto/ "How to: Run and use virtual actors in the .NET SDK")

                *   [AI](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-ai/ "Dapr AI .NET SDK")
                    *   [AI client](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-ai/dotnet-ai-conversation-usage/ "Dapr AI Client")
                    *   [How to: Use the AI Conversations client](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-ai/dotnet-ai-conversation-howto/ "How to: Create and use Dapr AI Conversations in the .NET SDK")
                    *   [How to: Use Microsoft's AI extensions with Dapr](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-ai/dotnet-ai-extensions-howto/ "How to: Using Microsoft's AI extensions with Dapr's .NET Conversation SDK")

                *   [Jobs](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-jobs/ "Dapr Jobs .NET SDK")
                    *   [How to: Author & manage jobs](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-jobs/dotnet-jobs-howto/ "How to: Author and manage Dapr Jobs in the .NET SDK")
                    *   [DaprJobsClient usage](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-jobs/dotnet-jobsclient-usage/)

                *   [Cryptography](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-cryptography/ "Dapr Cryptography .NET SDK")
                    *   [Cryptography client](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-cryptography/dotnet-cryptography-usage/ "Dapr Cryptography Client")
                    *   [How to: Use the Cryptography client](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-cryptography/dotnet-cryptography-howto/ "How to: Create and use Dapr Cryptography in the .NET SDK")

                *   [Messaging](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-messaging/ "Dapr Messaging .NET SDK")
                    *   [How to: Author & manage streaming subscriptions](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-messaging/dotnet-messaging-pubsub-howto/ "How to: Author and manage Dapr streaming subscriptions in the .NET SDK")
                    *   [DaprPublishSubscribeClient usage](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-messaging/dotnet-messaging-pubsub-usage/)

                *   [Distributed Lock](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-distributed-lock/ "Dapr Distributed Lock .NET SDK")
                    *   [How to: Use the Distributed Lock client](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-distributed-lock/dotnet-distributedlock-howto/ "How to: Create and use Dapr Distributed Lock in the .NET SDK")

                *   [Best Practices](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-guidance/ "Best Practices for the Dapr .NET SDK")
                    *   [Error Model](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-guidance/dotnet-guidance-error-model/ "Error Model in the Dapr .NET SDK")
                    *   [Experimental Attributes](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-guidance/dotnet-guidance-experimental-attributes/)
                    *   [Testcontainers](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-guidance/dotnet-guidance-testcontainers/ "Integration testing with Dapr.Testcontainers")
                    *   [Roslyn Analyzers/Generators](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-guidance/dotnet-guidance-source-generators/ "Dapr source code analyzers and generators")

                *   [Deployment Integrations](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-integrations/ "Developing applications with the Dapr .NET SDK")
                    *   [Dapr CLI](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-integrations/dotnet-development-dapr-cli/ "Dapr .NET SDK Development with Dapr CLI")
                    *   [Docker Compose](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-integrations/dotnet-development-docker-compose/ "Dapr .NET SDK Development with Docker-Compose")
                    *   [.NET Aspire](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-integrations/dotnet-development-dapr-aspire/ "Dapr .NET SDK Development with .NET Aspire")

                *   [Troubleshooting](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-troubleshooting/ "How to troubleshoot and debug with the Dapr .NET SDK")
                    *   [Troubleshoot pub/sub](https://docs.dapr.io/developing-applications/sdks/dotnet/dotnet-troubleshooting/dotnet-troubleshooting-pubsub/ "Troubleshoot Pub/Sub with the .NET SDK")

            *   [Go](https://docs.dapr.io/developing-applications/sdks/go/ "Dapr Go SDK")
                *   [Client](https://docs.dapr.io/developing-applications/sdks/go/go-client/ "Getting started with the Dapr client Go SDK")
                *   [Service](https://docs.dapr.io/developing-applications/sdks/go/go-service/ "Getting started with the Dapr Service (Callback) SDK for Go")
                    *   [HTTP Service](https://docs.dapr.io/developing-applications/sdks/go/go-service/http-service/ "Getting started with the Dapr HTTP Service SDK for Go")
                    *   [gRPC Service](https://docs.dapr.io/developing-applications/sdks/go/go-service/grpc-service/ "Getting started with the Dapr Service (Callback) SDK for Go")

            *   [Java](https://docs.dapr.io/developing-applications/sdks/java/ "Dapr Java SDK")
                *   [AI](https://docs.dapr.io/developing-applications/sdks/java/java-ai/)
                    *   [How to: Author and manage Conversation AI](https://docs.dapr.io/developing-applications/sdks/java/java-ai/java-ai-howto/ "How to: Author and manage Dapr Conversation AI in the Java SDK")

                *   [Client](https://docs.dapr.io/developing-applications/sdks/java/java-client/ "Getting started with the Dapr client Java SDK")
                    *   [Properties](https://docs.dapr.io/developing-applications/sdks/java/java-client/properties/)

                *   [Jobs](https://docs.dapr.io/developing-applications/sdks/java/java-jobs/)
                    *   [How to: Author and manage Jobs](https://docs.dapr.io/developing-applications/sdks/java/java-jobs/java-jobs-howto/ "How to: Author and manage Dapr Jobs in the Java SDK")

                *   [Workflow](https://docs.dapr.io/developing-applications/sdks/java/java-workflow/)
                    *   [How to: Author and manage workflows](https://docs.dapr.io/developing-applications/sdks/java/java-workflow/java-workflow-howto/ "How to: Author and manage Dapr Workflow in the Java SDK")

                *   [Spring Boot Integration](https://docs.dapr.io/developing-applications/sdks/java/spring-boot/ "Getting started with the Dapr and Spring Boot")
                    *   [How to: Author and manage workflows with Spring Boot](https://docs.dapr.io/developing-applications/sdks/java/spring-boot/sb-workflows-howto/ "How to: Author and manage Dapr Workflow with Spring Boot")

            *   [JavaScript](https://docs.dapr.io/developing-applications/sdks/js/ "JavaScript SDK")
                *   [Client](https://docs.dapr.io/developing-applications/sdks/js/js-client/ "JavaScript Client SDK")
                *   [Server](https://docs.dapr.io/developing-applications/sdks/js/js-server/ "JavaScript Server SDK")
                *   [Actors](https://docs.dapr.io/developing-applications/sdks/js/js-actors/ "JavaScript SDK for Actors")
                *   [Logging](https://docs.dapr.io/developing-applications/sdks/js/js-logger/ "Logging in JavaScript SDK")
                *   [Examples](https://docs.dapr.io/developing-applications/sdks/js/js-examples/ "JavaScript Examples")
                *   [How to: Author and manage workflows](https://docs.dapr.io/developing-applications/sdks/js/js-workflow/ "How to: Author and manage Dapr Workflow in the JavaScript SDK")

            *   [PHP](https://docs.dapr.io/developing-applications/sdks/php/ "Dapr PHP SDK")
                *   [Actors](https://docs.dapr.io/developing-applications/sdks/php/php-actors/ "Virtual Actors")
                    *   [Production Reference](https://docs.dapr.io/developing-applications/sdks/php/php-actors/php-actor-reference/ "Production Reference: Actors")

                *   [App](https://docs.dapr.io/developing-applications/sdks/php/php-app/ "The App")
                    *   [Unit Testing](https://docs.dapr.io/developing-applications/sdks/php/php-app/php-unit-testing/)

                *   [Custom Serializers](https://docs.dapr.io/developing-applications/sdks/php/php-serialization/ "Custom Serialization")
                *   [Publish and Subscribe](https://docs.dapr.io/developing-applications/sdks/php/php-pubsub/ "Publish and Subscribe with PHP")
                *   [State management](https://docs.dapr.io/developing-applications/sdks/php/php-state/ "State Management with PHP")

            *   [Python](https://docs.dapr.io/developing-applications/sdks/python/ "Dapr Python SDK")
                *   [Client](https://docs.dapr.io/developing-applications/sdks/python/python-client/ "Getting started with the Dapr client Python SDK")
                *   [Actor](https://docs.dapr.io/developing-applications/sdks/python/python-actor/ "Getting started with the Dapr actor Python SDK")
                *   [Extensions](https://docs.dapr.io/developing-applications/sdks/python/python-sdk-extensions/ "Dapr Python SDK extensions")
                    *   [gRPC](https://docs.dapr.io/developing-applications/sdks/python/python-sdk-extensions/python-grpc/ "Getting started with the Dapr Python gRPC service extension")
                    *   [FastAPI](https://docs.dapr.io/developing-applications/sdks/python/python-sdk-extensions/python-fastapi/ "Dapr Python SDK integration with FastAPI")
                    *   [Flask](https://docs.dapr.io/developing-applications/sdks/python/python-sdk-extensions/python-flask/ "Dapr Python SDK integration with Flask")
                    *   [Dapr Workflow](https://docs.dapr.io/developing-applications/sdks/python/python-sdk-extensions/python-workflow-ext/ "Dapr Python SDK integration with Dapr Workflow extension")
                        *   [Workflow](https://docs.dapr.io/developing-applications/sdks/python/python-sdk-extensions/python-workflow-ext/python-workflow/ "Getting started with the Dapr Workflow Python SDK")

                *   [](https://docs.dapr.io/developing-applications/sdks/python/conversation/)

            *   [Rust](https://docs.dapr.io/developing-applications/sdks/rust/ "Dapr Rust SDK")
                *   [Client](https://docs.dapr.io/developing-applications/sdks/rust/rust-client/ "Getting started with the Dapr client Rust SDK")

        *   [Error codes](https://docs.dapr.io/developing-applications/error-codes/)
            *   [Overview](https://docs.dapr.io/developing-applications/error-codes/errors-overview/ "Errors overview")
            *   [Reference](https://docs.dapr.io/developing-applications/error-codes/error-codes-reference/ "Error codes reference guide")
            *   [HTTP](https://docs.dapr.io/developing-applications/error-codes/http-error-codes/ "Handling HTTP error codes")
            *   [gRPC](https://docs.dapr.io/developing-applications/error-codes/grpc-error-codes/ "Handling gRPC error codes")

        *   [Local development](https://docs.dapr.io/developing-applications/local-development/)
            *   [IDE support](https://docs.dapr.io/developing-applications/local-development/ides/)
                *   [Visual Studio Code](https://docs.dapr.io/developing-applications/local-development/ides/vscode/ "Visual Studio Code integration with Dapr")
                    *   [Dapr extension](https://docs.dapr.io/developing-applications/local-development/ides/vscode/vscode-dapr-extension/ "Dapr Visual Studio Code extension overview")
                    *   [How-To: Debug with VSCode](https://docs.dapr.io/developing-applications/local-development/ides/vscode/vscode-how-to-debug-multiple-dapr-apps/ "How-To: Debug Dapr applications with Visual Studio Code")
                    *   [Dev Containers](https://docs.dapr.io/developing-applications/local-development/ides/vscode/vscode-remote-dev-containers/ "Developing Dapr applications with Dev Containers")

                *   [IntelliJ](https://docs.dapr.io/developing-applications/local-development/ides/intellij/)

            *   [Multi-App Run](https://docs.dapr.io/developing-applications/local-development/multi-app-dapr-run/)
                *   [Multi-App Run overview](https://docs.dapr.io/developing-applications/local-development/multi-app-dapr-run/multi-app-overview/)
                *   [How to: Use the Multi-App Run template](https://docs.dapr.io/developing-applications/local-development/multi-app-dapr-run/multi-app-template/ "How to: Use the Multi-App Run template file")

            *   [gRPC interface](https://docs.dapr.io/developing-applications/local-development/grpc-integration/ "How to: Use the gRPC interface in your Dapr application")
            *   [SDK Serialization](https://docs.dapr.io/developing-applications/local-development/sdk-serialization/ "Serialization in Dapr's SDKs")

        *   [Debugging](https://docs.dapr.io/developing-applications/debugging/ "Debugging Dapr applications and the Dapr control plane")
            *   [Kubernetes](https://docs.dapr.io/developing-applications/debugging/debug-k8s/ "Debug Dapr in Kubernetes mode")
                *   [Dapr control plane](https://docs.dapr.io/developing-applications/debugging/debug-k8s/debug-dapr-services/ "Debug Dapr control plane on Kubernetes")
                *   [Dapr sidecar](https://docs.dapr.io/developing-applications/debugging/debug-k8s/debug-daprd/ "Debug daprd on Kubernetes")

            *   [Debugging Docker Compose](https://docs.dapr.io/developing-applications/debugging/debugging-docker-compose/ "Debugging Dapr Apps running in Docker Compose")

        *   [Integrations](https://docs.dapr.io/developing-applications/integrations/)
            *   [AWS](https://docs.dapr.io/developing-applications/integrations/aws/ "Integrations with AWS")
                *   [Authenticating to AWS](https://docs.dapr.io/developing-applications/integrations/aws/authenticating-aws/)

            *   [Azure](https://docs.dapr.io/developing-applications/integrations/azure/ "Integrations with Azure")
                *   [Authenticate to Azure](https://docs.dapr.io/developing-applications/integrations/azure/azure-authentication/)
                    *   [Overview](https://docs.dapr.io/developing-applications/integrations/azure/azure-authentication/authenticating-azure/ "Authenticating to Azure")
                    *   [How to: Use workload identity federation](https://docs.dapr.io/developing-applications/integrations/azure/azure-authentication/howto-wif/)
                    *   [How to: Generate Microsoft Entra ID and Service Principal](https://docs.dapr.io/developing-applications/integrations/azure/azure-authentication/howto-aad/ "How to: Generate a new Microsoft Entra ID application and Service Principal")
                    *   [How to: Use managed identities](https://docs.dapr.io/developing-applications/integrations/azure/azure-authentication/howto-mi/)

                *   [Azure API Management](https://docs.dapr.io/developing-applications/integrations/azure/azure-api-management/ "Dapr integration policies for Azure API Management")
                *   [Azure Functions extension](https://docs.dapr.io/developing-applications/integrations/azure/azure-functions/ "Dapr extension for Azure Functions runtime")
                *   [Dapr extension for Azure Kubernetes Service (AKS)](https://docs.dapr.io/developing-applications/integrations/azure/azure-kubernetes-service-extension/)

            *   [Diagrid](https://docs.dapr.io/developing-applications/integrations/diagrid/ "Integrations with Diagrid")
                *   [Diagrid Conductor](https://docs.dapr.io/developing-applications/integrations/diagrid/diagrid-conductor/ "Conductor: Enterprise Dapr for Kubernetes")

            *   [KEDA](https://docs.dapr.io/developing-applications/integrations/autoscale-keda/ "How to: Autoscale a Dapr app with KEDA")
            *   [GitHub Actions](https://docs.dapr.io/developing-applications/integrations/github_actions/ "How to: Use the Dapr CLI in a GitHub Actions workflow")
            *   [Dapr Kubernetes Operator](https://docs.dapr.io/developing-applications/integrations/kubernetes-operator/ "How to: Use the Dapr Kubernetes Operator")
            *   [Kratix Marketplace](https://docs.dapr.io/developing-applications/integrations/kratix-marketplace/ "How to: Integrate with Kratix")
            *   [Argo CD](https://docs.dapr.io/developing-applications/integrations/argo-cd/ "How to: Integrate with Argo CD")

        *   [Components](https://docs.dapr.io/developing-applications/develop-components/)
            *   [Pluggable components](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/)
                *   [Overview](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/pluggable-components-overview/ "Pluggable components overview")
                *   [Implement pluggable components](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/develop-pluggable/ "How to: Implement pluggable components")
                *   [SDKs](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/pluggable-components-sdks/ "Pluggable components SDKs")
                    *   [.NET](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/pluggable-components-sdks/pluggable-components-dotnet/ "Getting started with the Dapr pluggable components .NET SDK")
                        *   [Bindings](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/pluggable-components-sdks/pluggable-components-dotnet/dotnet-bindings/ "Implementing a .NET input/output binding component")
                        *   [Pub/sub](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/pluggable-components-sdks/pluggable-components-dotnet/dotnet-pub-sub/ "Implementing a .NET pub/sub component")
                        *   [State Store](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/pluggable-components-sdks/pluggable-components-dotnet/dotnet-state-store/ "Implementing a .NET state store component")
                        *   [Advanced](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/pluggable-components-sdks/pluggable-components-dotnet/dotnet-advanced/ "Advanced uses of the Dapr pluggable components .NET SDK")
                            *   [Application environment](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/pluggable-components-sdks/pluggable-components-dotnet/dotnet-advanced/dotnet-application-environment/ "Application Environment of a .NET Dapr pluggable component")
                            *   [Component lifetime](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/pluggable-components-sdks/pluggable-components-dotnet/dotnet-advanced/dotnet-component-lifetime/ "Lifetimes of .NET Dapr pluggable components")
                            *   [Multiple services](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/pluggable-components-sdks/pluggable-components-dotnet/dotnet-advanced/dotnet-multiple-services/ "Multiple services in a .NET Dapr pluggable component")

                    *   [Go](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/pluggable-components-sdks/pluggable-components-go/ "Getting started with the Dapr pluggable components Go SDK")
                        *   [Bindings](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/pluggable-components-sdks/pluggable-components-go/go-bindings/ "Implementing a Go input/output binding component")
                        *   [Pub/sub](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/pluggable-components-sdks/pluggable-components-go/go-pub-sub/ "Implementing a Go pub/sub component")
                        *   [State Store](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/pluggable-components-sdks/pluggable-components-go/go-state-store/ "Implementing a Go state store component")
                        *   [Advanced](https://docs.dapr.io/developing-applications/develop-components/pluggable-components/pluggable-components-sdks/pluggable-components-go/go-advanced/ "Advanced uses of the Dapr pluggable components .Go SDK")

            *   [Middleware components](https://docs.dapr.io/developing-applications/develop-components/develop-middleware/ "How to: Author middleware components")

    *   [Developing AI](https://docs.dapr.io/developing-ai/ "Developing AI with Dapr")
        *   [Agent Integrations](https://docs.dapr.io/developing-ai/agent-integrations/)
            *   [CrewAI](https://docs.dapr.io/developing-ai/agent-integrations/crewai/)
                *   [CrewAI Workflows](https://docs.dapr.io/developing-ai/agent-integrations/crewai/crewai-workflows/)

            *   [LangGraph](https://docs.dapr.io/developing-ai/agent-integrations/langgraph/)
                *   [Agent Sessions](https://docs.dapr.io/developing-ai/agent-integrations/langgraph/langgraph-agents-sessions/)

            *   [OpenAI](https://docs.dapr.io/developing-ai/agent-integrations/openai-agents/)
                *   [Agent Sessions](https://docs.dapr.io/developing-ai/agent-integrations/openai-agents/openai-agents-sessions/)

        *   [Dapr Agents](https://docs.dapr.io/developing-ai/dapr-agents/)
            *   [Introduction](https://docs.dapr.io/developing-ai/dapr-agents/dapr-agents-introduction/)
            *   [Getting Started](https://docs.dapr.io/developing-ai/dapr-agents/dapr-agents-getting-started/)
            *   [Why Dapr Agents](https://docs.dapr.io/developing-ai/dapr-agents/dapr-agents-why/)
            *   [Core Concepts](https://docs.dapr.io/developing-ai/dapr-agents/dapr-agents-core-concepts/)
            *   [Agentic Patterns](https://docs.dapr.io/developing-ai/dapr-agents/dapr-agents-patterns/)
            *   [Integrations](https://docs.dapr.io/developing-ai/dapr-agents/dapr-agents-integrations/)
            *   [Quickstarts](https://docs.dapr.io/developing-ai/dapr-agents/dapr-agents-quickstarts/)

        *   [MCP](https://docs.dapr.io/developing-ai/mcp/)
            *   [Getting Started](https://docs.dapr.io/developing-ai/mcp/mcp-authentication/ "Authenticating an MCP server")

    *   [Operations](https://docs.dapr.io/operations/ "Deploying and configuring Dapr in your environment")
        *   [Observability](https://docs.dapr.io/operations/observability/)
            *   [Tracing](https://docs.dapr.io/operations/observability/tracing/)
                *   [Overview](https://docs.dapr.io/operations/observability/tracing/tracing-overview/ "Distributed tracing overview")
                *   [W3C trace context](https://docs.dapr.io/operations/observability/tracing/w3c-tracing-overview/ "W3C trace context overview")
                *   [Configure tracing](https://docs.dapr.io/operations/observability/tracing/setup-tracing/ "Configure Dapr to send distributed tracing data")
                *   [Open Telemetry Collector](https://docs.dapr.io/operations/observability/tracing/otel-collector/)
                    *   [Using the OpenTelemetry Collector](https://docs.dapr.io/operations/observability/tracing/otel-collector/open-telemetry-collector/ "Using OpenTelemetry Collector to collect traces")
                    *   [Using the Dynatrace OpenTelemetry Collector](https://docs.dapr.io/operations/observability/tracing/otel-collector/open-telemetry-collector-dynatrace/ "Using Dynatrace OpenTelemetry Collector to collect traces to send to Dynatrace")
                    *   [Using the OpenTelemetry for Azure App Insights](https://docs.dapr.io/operations/observability/tracing/otel-collector/open-telemetry-collector-appinsights/ "Using OpenTelemetry Collector to collect traces to send to App Insights")
                    *   [Using OpenTelemetry for Jaeger V2](https://docs.dapr.io/operations/observability/tracing/otel-collector/open-telemetry-collector-jaeger/ "Using OpenTelemetry to send traces to Jaeger V2")

                *   [New Relic](https://docs.dapr.io/operations/observability/tracing/newrelic/ "How-To: Set-up New Relic for distributed tracing")
                *   [Zipkin](https://docs.dapr.io/operations/observability/tracing/zipkin/ "How-To: Set up Zipkin for distributed tracing")
                *   [Dash0](https://docs.dapr.io/operations/observability/tracing/dash0/ "How-To: Set up Dash0 for distributed tracing")
                *   [Datadog](https://docs.dapr.io/operations/observability/tracing/datadog/ "How-To: Set up Datadog for distributed tracing")

            *   [Metrics](https://docs.dapr.io/operations/observability/metrics/)
                *   [Overview](https://docs.dapr.io/operations/observability/metrics/metrics-overview/ "Configure metrics")
                *   [Prometheus](https://docs.dapr.io/operations/observability/metrics/prometheus/ "How-To: Observe metrics with Prometheus")
                *   [Grafana dashboards](https://docs.dapr.io/operations/observability/metrics/grafana/ "How-To: Observe metrics with Grafana")
                *   [New Relic](https://docs.dapr.io/operations/observability/metrics/newrelic/ "How-To: Set-up New Relic to collect and analyze metrics")
                *   [Azure Monitor](https://docs.dapr.io/operations/observability/metrics/azure-monitor/ "How-To: Set up Azure Monitor to search logs and collect metrics")

            *   [Logging](https://docs.dapr.io/operations/observability/logging/)
                *   [Overview](https://docs.dapr.io/operations/observability/logging/logs/ "Logs")
                *   [FluentD](https://docs.dapr.io/operations/observability/logging/fluentd/ "How-To: Set up Fluentd, Elastic search and Kibana in Kubernetes")
                *   [New Relic](https://docs.dapr.io/operations/observability/logging/newrelic/ "How-To: Set-up New Relic for Dapr logging")

        *   [Hosting options](https://docs.dapr.io/operations/hosting/ "Hosting options for Dapr")
            *   [Self-Hosted](https://docs.dapr.io/operations/hosting/self-hosted/ "Run Dapr in self-hosted mode")
                *   [Overview](https://docs.dapr.io/operations/hosting/self-hosted/self-hosted-overview/ "Overview of Dapr in self-hosted mode")
                *   [Run with Docker](https://docs.dapr.io/operations/hosting/self-hosted/self-hosted-with-docker/ "How-To: Run Dapr in self-hosted mode with Docker")
                *   [Run with Podman](https://docs.dapr.io/operations/hosting/self-hosted/self-hosted-with-podman/ "How-To: Run Dapr in self-hosted mode with Podman")
                *   [Run in offline or airgap](https://docs.dapr.io/operations/hosting/self-hosted/self-hosted-airgap/ "How-To: Run Dapr in an offline or airgap environment")
                *   [Run without Docker](https://docs.dapr.io/operations/hosting/self-hosted/self-hosted-no-docker/ "How-To: Run Dapr in self-hosted mode without Docker")
                *   [How-to: Persist Scheduler Jobs](https://docs.dapr.io/operations/hosting/self-hosted/self-hosted-persisting-scheduler/)
                *   [Upgrade Dapr](https://docs.dapr.io/operations/hosting/self-hosted/self-hosted-upgrade/ "Steps to upgrade Dapr in a self-hosted environment")
                *   [Uninstall Dapr](https://docs.dapr.io/operations/hosting/self-hosted/self-hosted-uninstall/ "Uninstall Dapr in a self-hosted environment")

            *   [Kubernetes](https://docs.dapr.io/operations/hosting/kubernetes/ "Deploy and run Dapr in Kubernetes mode")
                *   [Overview](https://docs.dapr.io/operations/hosting/kubernetes/kubernetes-overview/ "Overview of Dapr on Kubernetes")
                *   [How-to: Setup clusters](https://docs.dapr.io/operations/hosting/kubernetes/cluster/ "Kubernetes cluster setup")
                    *   [Minikube](https://docs.dapr.io/operations/hosting/kubernetes/cluster/setup-minikube/ "Set up a Minikube cluster")
                    *   [KiND](https://docs.dapr.io/operations/hosting/kubernetes/cluster/setup-kind/ "Set up a KiND cluster")
                    *   [Azure Kubernetes Service (AKS)](https://docs.dapr.io/operations/hosting/kubernetes/cluster/setup-aks/ "Set up an Azure Kubernetes Service (AKS) cluster")
                    *   [Google Kubernetes Engine (GKE)](https://docs.dapr.io/operations/hosting/kubernetes/cluster/setup-gke/ "Set up a Google Kubernetes Engine (GKE) cluster")
                    *   [Elastic Kubernetes Service (EKS)](https://docs.dapr.io/operations/hosting/kubernetes/cluster/setup-eks/ "Set up an Elastic Kubernetes Service (EKS) cluster")

                *   [Deploy Dapr](https://docs.dapr.io/operations/hosting/kubernetes/kubernetes-deploy/ "Deploy Dapr on a Kubernetes cluster")
                *   [Upgrade Dapr](https://docs.dapr.io/operations/hosting/kubernetes/kubernetes-upgrade/ "Upgrade Dapr on a Kubernetes cluster")
                *   [Production guidelines](https://docs.dapr.io/operations/hosting/kubernetes/kubernetes-production/ "Production guidelines on Kubernetes")
                *   [Dapr Shared](https://docs.dapr.io/operations/hosting/kubernetes/kubernetes-dapr-shared/ "Deploy Dapr per-node or per-cluster with Dapr Shared")
                *   [How-to: Persist Scheduler Jobs](https://docs.dapr.io/operations/hosting/kubernetes/kubernetes-persisting-scheduler/)
                *   [Hybrid clusters](https://docs.dapr.io/operations/hosting/kubernetes/kubernetes-hybrid-clusters/ "Deploy to hybrid Linux/Windows Kubernetes clusters")
                *   [Kubernetes Jobs](https://docs.dapr.io/operations/hosting/kubernetes/kubernetes-job/ "Running Dapr with a Kubernetes Job")
                *   [How-to: Mount Pod volumes](https://docs.dapr.io/operations/hosting/kubernetes/kubernetes-volume-mounts/ "How-to: Mount Pod volumes to the Dapr sidecar")

            *   [Serverless](https://docs.dapr.io/operations/hosting/serverless/ "Run Dapr in a serverless offering")
                *   [Azure Container Apps](https://docs.dapr.io/operations/hosting/serverless/azure-container-apps/)

        *   [Configuration](https://docs.dapr.io/operations/configuration/ "Manage Dapr configuration")
            *   [Overview](https://docs.dapr.io/operations/configuration/configuration-overview/ "Dapr configuration")
            *   [Concurrency & rate limits](https://docs.dapr.io/operations/configuration/control-concurrency/ "How-To: Control concurrency and rate limit applications")
            *   [Limit secret store access](https://docs.dapr.io/operations/configuration/secret-scope/ "How-To: Limit the secrets that can be read from secret stores")
            *   [Service Invocation access control](https://docs.dapr.io/operations/configuration/invoke-allowlist/ "How-To: Apply access control list configuration for service invocation")
            *   [Dapr APIs allow list](https://docs.dapr.io/operations/configuration/api-allowlist/ "How-To: Selectively enable Dapr APIs on the Dapr sidecar")
            *   [Use gRPC interface](https://docs.dapr.io/operations/configuration/grpc/ "How-To: Configure Dapr to use gRPC")
            *   [HTTP header size](https://docs.dapr.io/operations/configuration/increase-read-buffer-size/ "How-To: Handle large HTTP header size")
            *   [Request body size](https://docs.dapr.io/operations/configuration/increase-request-size/ "How-To: Handle larger body requests")
            *   [Install sidecar certificates](https://docs.dapr.io/operations/configuration/install-certificates/ "How-To: Install certificates in the Dapr sidecar")
            *   [Preview features](https://docs.dapr.io/operations/configuration/preview-features/ "How-To: Enable preview features")
            *   [Environment Variables from Secrets](https://docs.dapr.io/operations/configuration/environment-variables-secrets/ "How-To: Configure Environment Variables from Secrets for Dapr sidecar")
            *   [Sidecar Service Annotations](https://docs.dapr.io/operations/configuration/sidecar-service-annotations/ "How-To: Add custom annotations to the Dapr sidecar service")

        *   [Components](https://docs.dapr.io/operations/components/ "Managing components in Dapr")
            *   [Certification lifecycle](https://docs.dapr.io/operations/components/certification-lifecycle/)
            *   [Updating components](https://docs.dapr.io/operations/components/component-updates/)
            *   [Scope access to components](https://docs.dapr.io/operations/components/component-scopes/ "How-To: Scope components to one or more applications")
            *   [Reference secrets in components](https://docs.dapr.io/operations/components/component-secrets/ "How-To: Reference secrets in components")
            *   [State stores](https://docs.dapr.io/operations/components/setup-state-store/ "State stores components")
            *   [Pub/sub brokers](https://docs.dapr.io/operations/components/setup-pubsub/ "Pub/Sub brokers")
                *   [Multiple namespaces](https://docs.dapr.io/operations/components/setup-pubsub/pubsub-namespaces/ "HowTo: Configure Pub/Sub components with multiple namespaces")

            *   [Secret stores](https://docs.dapr.io/operations/components/setup-secret-store/ "Secret store components")
            *   [Bindings](https://docs.dapr.io/operations/components/setup-bindings/ "Bindings components")
            *   [Register a pluggable component](https://docs.dapr.io/operations/components/pluggable-components-registration/ "How-To: Register a pluggable component")
            *   [Configure middleware](https://docs.dapr.io/operations/components/middleware/ "Configure middleware components")

        *   [Security](https://docs.dapr.io/operations/security/ "Securing Dapr deployments")
            *   [Setup & configure mTLS certificates](https://docs.dapr.io/operations/security/mtls/)
            *   [Configure endpoint authorization with OAuth](https://docs.dapr.io/operations/security/oauth/)
            *   [Dapr API token authentication](https://docs.dapr.io/operations/security/api-token/ "Enable API token authentication in Dapr")
            *   [App API token authentication](https://docs.dapr.io/operations/security/app-api-token/ "Authenticate requests from Dapr using token authentication")

        *   [Resiliency](https://docs.dapr.io/operations/resiliency/ "Error recovery using resiliency policies")
            *   [Overview](https://docs.dapr.io/operations/resiliency/resiliency-overview/)
            *   [Policies](https://docs.dapr.io/operations/resiliency/policies/ "Resiliency policies")
                *   [Timeouts](https://docs.dapr.io/operations/resiliency/policies/timeouts/ "Timeout resiliency policies")
                *   [Retries](https://docs.dapr.io/operations/resiliency/policies/retries/ "Retry and back-off resiliency policies")
                    *   [Overview](https://docs.dapr.io/operations/resiliency/policies/retries/retries-overview/ "Retry resiliency policies")
                    *   [Override default retries](https://docs.dapr.io/operations/resiliency/policies/retries/override-default-retries/ "Override default retry resiliency policies")

                *   [Circuit breakers](https://docs.dapr.io/operations/resiliency/policies/circuit-breakers/ "Circuit breaker resiliency policies")
                *   [Default policies](https://docs.dapr.io/operations/resiliency/policies/default-policies/ "Default resiliency policies")

            *   [Targets](https://docs.dapr.io/operations/resiliency/targets/)
            *   [Health checks](https://docs.dapr.io/operations/resiliency/health-checks/)
                *   [App health checks](https://docs.dapr.io/operations/resiliency/health-checks/app-health/)
                *   [Sidecar health](https://docs.dapr.io/operations/resiliency/health-checks/sidecar-health/)

        *   [Support](https://docs.dapr.io/operations/support/ "Support and versioning")
            *   [Versioning](https://docs.dapr.io/operations/support/support-versioning/ "Versioning policy")
            *   [Supported releases](https://docs.dapr.io/operations/support/support-release-policy/ "Supported runtime and SDK releases")
            *   [Breaking changes and deprecations](https://docs.dapr.io/operations/support/breaking-changes-and-deprecations/)
            *   [Reporting security issues](https://docs.dapr.io/operations/support/support-security-issues/ "Reporting security issues")
            *   [Preview features](https://docs.dapr.io/operations/support/support-preview-features/)
            *   [Alpha & Beta APIs](https://docs.dapr.io/operations/support/alpha-beta-apis/ "Alpha and Beta APIs")

        *   [Performance and scalability](https://docs.dapr.io/operations/performance-and-scalability/ "Performance and scalability statistics of Dapr")
            *   [Longhaul performance and stability](https://docs.dapr.io/operations/performance-and-scalability/perf-longhaul/)
            *   [Performance results](https://docs.dapr.io/operations/performance-and-scalability/perf-results/)

        *   [Troubleshooting](https://docs.dapr.io/operations/troubleshooting/ "Debugging and Troubleshooting")
            *   [Common Issues](https://docs.dapr.io/operations/troubleshooting/common_issues/ "Common issues when running Dapr")
            *   [Logs](https://docs.dapr.io/operations/troubleshooting/logs-troubleshooting/ "Configure and view Dapr Logs")
            *   [API Logs](https://docs.dapr.io/operations/troubleshooting/api-logs-troubleshooting/ "Dapr API Logs")
            *   [Debugging](https://docs.dapr.io/operations/troubleshooting/profiling-debugging/ "Profiling & Debugging")

    *   [Reference](https://docs.dapr.io/reference/ "Dapr Reference Docs")
        *   [Dapr API](https://docs.dapr.io/reference/api/ "Dapr API reference")
            *   [Actors API](https://docs.dapr.io/reference/api/actors_api/ "Actors API reference")
            *   [Bindings API](https://docs.dapr.io/reference/api/bindings_api/ "Bindings API reference")
            *   [Configuration API](https://docs.dapr.io/reference/api/configuration_api/ "Configuration API reference")
            *   [Conversation API](https://docs.dapr.io/reference/api/conversation_api/ "Conversation API reference")
            *   [Cryptography API](https://docs.dapr.io/reference/api/cryptography_api/ "Cryptography API reference")
            *   [Distributed lock API](https://docs.dapr.io/reference/api/distributed_lock_api/ "Distributed lock API reference")
            *   [Health API](https://docs.dapr.io/reference/api/health_api/ "Health API reference")
            *   [Jobs API](https://docs.dapr.io/reference/api/jobs_api/ "Jobs API reference")
            *   [Metadata API](https://docs.dapr.io/reference/api/metadata_api/ "Metadata API reference")
            *   [Placement API](https://docs.dapr.io/reference/api/placement_api/ "Placement API reference")
            *   [Pub/Sub API](https://docs.dapr.io/reference/api/pubsub_api/ "Pub/sub API reference")
            *   [Secrets API](https://docs.dapr.io/reference/api/secrets_api/ "Secrets API reference")
            *   [Service invocation API](https://docs.dapr.io/reference/api/service_invocation_api/ "Service invocation API reference")
            *   [State management API](https://docs.dapr.io/reference/api/state_api/ "State management API reference")
            *   [Workflow API](https://docs.dapr.io/reference/api/workflow_api/ "Workflow API reference")

        *   [Dapr CLI](https://docs.dapr.io/reference/cli/ "Dapr CLI reference")
            *   [Overview](https://docs.dapr.io/reference/cli/cli-overview/ "Dapr command line interface (CLI) reference")
            *   [scheduler](https://docs.dapr.io/reference/cli/dapr-scheduler/ "dapr scheduler")
            *   [annotate](https://docs.dapr.io/reference/cli/dapr-annotate/ "annotate CLI command reference")
            *   [build-info](https://docs.dapr.io/reference/cli/dapr-build-info/ "build-info CLI command reference")
            *   [completion](https://docs.dapr.io/reference/cli/dapr-completion/ "completion CLI command reference")
            *   [components](https://docs.dapr.io/reference/cli/dapr-components/ "components CLI command reference")
            *   [configurations](https://docs.dapr.io/reference/cli/dapr-configurations/ "configurations CLI command reference")
            *   [dashboard](https://docs.dapr.io/reference/cli/dapr-dashboard/ "dashboard CLI command reference")
            *   [help](https://docs.dapr.io/reference/cli/dapr-help/ "help CLI command reference")
            *   [init](https://docs.dapr.io/reference/cli/dapr-init/ "init CLI command reference")
            *   [invoke](https://docs.dapr.io/reference/cli/dapr-invoke/ "invoke CLI command reference")
            *   [list](https://docs.dapr.io/reference/cli/dapr-list/ "list CLI command reference")
            *   [logs](https://docs.dapr.io/reference/cli/dapr-logs/ "logs CLI command reference")
            *   [mtls](https://docs.dapr.io/reference/cli/dapr-mtls/ "mtls CLI command reference")
                *   [mtls export](https://docs.dapr.io/reference/cli/dapr-mtls/dapr-mtls-export/ "mtls export CLI command reference")
                *   [mtls expiry](https://docs.dapr.io/reference/cli/dapr-mtls/dapr-mtls-expiry/ "mtls expiry CLI command reference")
                *   [mtls renew certificate](https://docs.dapr.io/reference/cli/dapr-mtls/dapr-mtls-renew-certificate/ "mtls renew certificate CLI command reference")

            *   [publish](https://docs.dapr.io/reference/cli/dapr-publish/ "publish CLI command reference")
            *   [run](https://docs.dapr.io/reference/cli/dapr-run/ "run CLI command reference")
            *   [status](https://docs.dapr.io/reference/cli/dapr-status/ "status CLI command reference")
            *   [stop](https://docs.dapr.io/reference/cli/dapr-stop/ "stop CLI command reference")
            *   [uninstall](https://docs.dapr.io/reference/cli/dapr-uninstall/ "uninstall CLI command reference")
            *   [upgrade](https://docs.dapr.io/reference/cli/dapr-upgrade/ "upgrade CLI command reference")
            *   [version](https://docs.dapr.io/reference/cli/dapr-version/ "version CLI command reference")
            *   [workflow](https://docs.dapr.io/reference/cli/dapr-workflow/ "workflow CLI command")

        *   [Arguments and annotations](https://docs.dapr.io/reference/arguments-annotations-overview/ "Dapr arguments and annotations for daprd, CLI, and Kubernetes")
        *   [Environment variables](https://docs.dapr.io/reference/environment/ "Environment variable reference")
        *   [Component specs](https://docs.dapr.io/reference/components-reference/ "Dapr components reference")
            *   [Bindings](https://docs.dapr.io/reference/components-reference/supported-bindings/ "Bindings component specs")
                *   [Alibaba Cloud DingTalk](https://docs.dapr.io/reference/components-reference/supported-bindings/alicloud-dingtalk/ "Alibaba Cloud DingTalk binding spec")
                *   [Alibaba Cloud Log Storage](https://docs.dapr.io/reference/components-reference/supported-bindings/alicloudsls/ "Alibaba Cloud Log Storage Service binding spec")
                *   [Alibaba Cloud Object Storage](https://docs.dapr.io/reference/components-reference/supported-bindings/alicloudoss/ "Alibaba Cloud Object Storage Service binding spec")
                *   [Alibaba Cloud Tablestore](https://docs.dapr.io/reference/components-reference/supported-bindings/alicloudtablestore/ "Alibaba Cloud Tablestore binding spec")
                *   [Apple Push Notification Service](https://docs.dapr.io/reference/components-reference/supported-bindings/apns/ "Apple Push Notification Service binding spec")
                *   [AWS DynamoDB](https://docs.dapr.io/reference/components-reference/supported-bindings/dynamodb/ "AWS DynamoDB binding spec")
                *   [AWS Kinesis](https://docs.dapr.io/reference/components-reference/supported-bindings/kinesis/ "AWS Kinesis binding spec")
                *   [AWS S3](https://docs.dapr.io/reference/components-reference/supported-bindings/s3/ "AWS S3 binding spec")
                *   [AWS SES](https://docs.dapr.io/reference/components-reference/supported-bindings/ses/ "AWS SES binding spec")
                *   [AWS SNS](https://docs.dapr.io/reference/components-reference/supported-bindings/sns/ "AWS SNS binding spec")
                *   [AWS SQS](https://docs.dapr.io/reference/components-reference/supported-bindings/sqs/ "AWS SQS binding spec")
                *   [Azure Blob Storage](https://docs.dapr.io/reference/components-reference/supported-bindings/blobstorage/ "Azure Blob Storage binding spec")
                *   [Azure Cosmos DB (Gremlin API)](https://docs.dapr.io/reference/components-reference/supported-bindings/cosmosdbgremlinapi/ "Azure Cosmos DB (Gremlin API) binding spec")
                *   [Azure Cosmos DB (SQL API)](https://docs.dapr.io/reference/components-reference/supported-bindings/cosmosdb/ "Azure Cosmos DB (SQL API) binding spec")
                *   [Azure Event Grid](https://docs.dapr.io/reference/components-reference/supported-bindings/eventgrid/ "Azure Event Grid binding spec")
                *   [Azure Event Hubs](https://docs.dapr.io/reference/components-reference/supported-bindings/eventhubs/ "Azure Event Hubs binding spec")
                *   [Azure OpenAI](https://docs.dapr.io/reference/components-reference/supported-bindings/openai/ "Azure OpenAI binding spec")
                *   [Azure Service Bus Queues](https://docs.dapr.io/reference/components-reference/supported-bindings/servicebusqueues/ "Azure Service Bus Queues binding spec")
                *   [Azure SignalR](https://docs.dapr.io/reference/components-reference/supported-bindings/signalr/ "Azure SignalR binding spec")
                *   [Azure Storage Queues](https://docs.dapr.io/reference/components-reference/supported-bindings/storagequeues/ "Azure Storage Queues binding spec")
                *   [Cloudflare Queues](https://docs.dapr.io/reference/components-reference/supported-bindings/cloudflare-queues/ "Cloudflare Queues bindings spec")
                *   [commercetools GraphQL](https://docs.dapr.io/reference/components-reference/supported-bindings/commercetools/ "commercetools GraphQL binding spec")
                *   [Cron](https://docs.dapr.io/reference/components-reference/supported-bindings/cron/ "Cron binding spec")
                *   [Dubbo](https://docs.dapr.io/reference/components-reference/supported-bindings/dubbo/ "Apache Dubbo binding spec")
                *   [GCP Pub/Sub](https://docs.dapr.io/reference/components-reference/supported-bindings/gcppubsub/ "GCP Pub/Sub binding spec")
                *   [GCP Storage Bucket](https://docs.dapr.io/reference/components-reference/supported-bindings/gcpbucket/ "GCP Storage Bucket binding spec")
                *   [GraphQL](https://docs.dapr.io/reference/components-reference/supported-bindings/graghql/ "GraphQL binding spec")
                *   [HTTP](https://docs.dapr.io/reference/components-reference/supported-bindings/http/ "HTTP binding spec")
                *   [Huawei OBS](https://docs.dapr.io/reference/components-reference/supported-bindings/huawei-obs/ "Huawei OBS binding spec")
                *   [InfluxDB](https://docs.dapr.io/reference/components-reference/supported-bindings/influxdb/ "InfluxDB binding spec")
                *   [Kafka](https://docs.dapr.io/reference/components-reference/supported-bindings/kafka/ "Kafka binding spec")
                *   [Kitex](https://docs.dapr.io/reference/components-reference/supported-bindings/kitex/)
                *   [KubeMQ](https://docs.dapr.io/reference/components-reference/supported-bindings/kubemq/ "KubeMQ binding spec")
                *   [Kubernetes Events](https://docs.dapr.io/reference/components-reference/supported-bindings/kubernetes-binding/ "Kubernetes Events binding spec")
                *   [Local Storage](https://docs.dapr.io/reference/components-reference/supported-bindings/localstorage/ "Local Storage binding spec")
                *   [MQTT3](https://docs.dapr.io/reference/components-reference/supported-bindings/mqtt3/ "MQTT3 binding spec")
                *   [MySQL & MariaDB](https://docs.dapr.io/reference/components-reference/supported-bindings/mysql/ "MySQL & MariaDB binding spec")
                *   [PostgreSQL](https://docs.dapr.io/reference/components-reference/supported-bindings/postgresql/ "PostgreSQL binding spec")
                *   [Postmark](https://docs.dapr.io/reference/components-reference/supported-bindings/postmark/ "Postmark binding spec")
                *   [RabbitMQ](https://docs.dapr.io/reference/components-reference/supported-bindings/rabbitmq/ "RabbitMQ binding spec")
                *   [Redis](https://docs.dapr.io/reference/components-reference/supported-bindings/redis/ "Redis binding spec")
                *   [RethinkDB](https://docs.dapr.io/reference/components-reference/supported-bindings/rethinkdb/ "RethinkDB binding spec")
                *   [RocketMQ](https://docs.dapr.io/reference/components-reference/supported-bindings/rocketmq/ "Apache RocketMQ binding spec")
                *   [SFTP](https://docs.dapr.io/reference/components-reference/supported-bindings/sftp/ "SFTP binding spec")
                *   [SMTP](https://docs.dapr.io/reference/components-reference/supported-bindings/smtp/ "SMTP binding spec")
                *   [Twilio SendGrid](https://docs.dapr.io/reference/components-reference/supported-bindings/sendgrid/ "Twilio SendGrid binding spec")
                *   [Twilio SMS](https://docs.dapr.io/reference/components-reference/supported-bindings/twilio/ "Twilio SMS binding spec")
                *   [Wasm](https://docs.dapr.io/reference/components-reference/supported-bindings/wasm/)
                *   [Zeebe command](https://docs.dapr.io/reference/components-reference/supported-bindings/zeebe-command/ "Zeebe command binding spec")
                *   [Zeebe JobWorker](https://docs.dapr.io/reference/components-reference/supported-bindings/zeebe-jobworker/ "Zeebe JobWorker binding spec")

            *   [Configuration stores](https://docs.dapr.io/reference/components-reference/supported-configuration-stores/ "Configuration store component specs")
                *   [Azure App Configuration](https://docs.dapr.io/reference/components-reference/supported-configuration-stores/azure-appconfig-configuration-store/)
                *   [PostgreSQL](https://docs.dapr.io/reference/components-reference/supported-configuration-stores/postgresql-configuration-store/)
                *   [Redis](https://docs.dapr.io/reference/components-reference/supported-configuration-stores/redis-configuration-store/)

            *   [Conversation](https://docs.dapr.io/reference/components-reference/supported-conversation/ "Conversation component specs")
                *   [Anthropic](https://docs.dapr.io/reference/components-reference/supported-conversation/anthropic/)
                *   [AWS Bedrock](https://docs.dapr.io/reference/components-reference/supported-conversation/aws-bedrock/)
                *   [DeepSeek](https://docs.dapr.io/reference/components-reference/supported-conversation/deepseek/)
                *   [Echo](https://docs.dapr.io/reference/components-reference/supported-conversation/local-echo/ "Local Testing")
                *   [GoogleAI](https://docs.dapr.io/reference/components-reference/supported-conversation/googleai/)
                *   [Huggingface](https://docs.dapr.io/reference/components-reference/supported-conversation/hugging-face/)
                *   [Mistral](https://docs.dapr.io/reference/components-reference/supported-conversation/mistral/)
                *   [Ollama](https://docs.dapr.io/reference/components-reference/supported-conversation/ollama/)
                *   [OpenAI](https://docs.dapr.io/reference/components-reference/supported-conversation/openai/)

            *   [Cryptography](https://docs.dapr.io/reference/components-reference/supported-cryptography/ "Cryptography component specs")
                *   [Azure Key Vault](https://docs.dapr.io/reference/components-reference/supported-cryptography/azure-key-vault/)
                *   [JSON Web Key Sets (JWKS)](https://docs.dapr.io/reference/components-reference/supported-cryptography/json-web-key-sets/)
                *   [Kubernetes Secrets](https://docs.dapr.io/reference/components-reference/supported-cryptography/kubernetes-secrets/)
                *   [Local storage](https://docs.dapr.io/reference/components-reference/supported-cryptography/local-storage/)

            *   [Locks](https://docs.dapr.io/reference/components-reference/supported-locks/ "Lock component specs")
                *   [Redis](https://docs.dapr.io/reference/components-reference/supported-locks/redis-lock/)

            *   [Middleware](https://docs.dapr.io/reference/components-reference/supported-middleware/ "Middleware component specs")
                *   [Bearer](https://docs.dapr.io/reference/components-reference/supported-middleware/middleware-bearer/)
                *   [OAuth2](https://docs.dapr.io/reference/components-reference/supported-middleware/middleware-oauth2/)
                *   [OAuth2 client credentials](https://docs.dapr.io/reference/components-reference/supported-middleware/middleware-oauth2clientcredentials/)
                *   [Open Policy Agent (OPA)](https://docs.dapr.io/reference/components-reference/supported-middleware/middleware-opa/ "Apply Open Policy Agent (OPA) policies")
                *   [Rate limiting](https://docs.dapr.io/reference/components-reference/supported-middleware/middleware-rate-limit/)
                *   [Router Alias](https://docs.dapr.io/reference/components-reference/supported-middleware/middleware-routeralias/ "Router alias http request routing")
                *   [RouterChecker](https://docs.dapr.io/reference/components-reference/supported-middleware/middleware-routerchecker/ "RouterChecker http request routing")
                *   [Sentinel](https://docs.dapr.io/reference/components-reference/supported-middleware/middleware-sentinel/ "Sentinel fault-tolerance middleware component")
                *   [Uppercase](https://docs.dapr.io/reference/components-reference/supported-middleware/middleware-uppercase/ "Uppercase request body")
                *   [Wasm](https://docs.dapr.io/reference/components-reference/supported-middleware/middleware-wasm/)

            *   [Name resolution](https://docs.dapr.io/reference/components-reference/supported-name-resolution/ "Name resolution provider component specs")
                *   [AWS Cloudmap](https://docs.dapr.io/reference/components-reference/supported-name-resolution/nr-awscloudmap/)
                *   [HashiCorp Consul](https://docs.dapr.io/reference/components-reference/supported-name-resolution/setup-nr-consul/)
                *   [Kubernetes DNS](https://docs.dapr.io/reference/components-reference/supported-name-resolution/nr-kubernetes/)
                *   [mDNS](https://docs.dapr.io/reference/components-reference/supported-name-resolution/nr-mdns/)
                *   [NameFormat](https://docs.dapr.io/reference/components-reference/supported-name-resolution/nr-nameformat/ "Nameformat")
                *   [SQLite](https://docs.dapr.io/reference/components-reference/supported-name-resolution/nr-sqlite/)

            *   [Pub/sub brokers](https://docs.dapr.io/reference/components-reference/supported-pubsub/ "Pub/sub brokers component specs")
                *   [Apache Kafka](https://docs.dapr.io/reference/components-reference/supported-pubsub/setup-apache-kafka/)
                *   [AWS SNS/SQS](https://docs.dapr.io/reference/components-reference/supported-pubsub/setup-aws-snssqs/)
                *   [Azure Event Hubs](https://docs.dapr.io/reference/components-reference/supported-pubsub/setup-azure-eventhubs/)
                *   [Azure Service Bus Queues](https://docs.dapr.io/reference/components-reference/supported-pubsub/setup-azure-servicebus-queues/)
                *   [Azure Service Bus Topics](https://docs.dapr.io/reference/components-reference/supported-pubsub/setup-azure-servicebus-topics/)
                *   [GCP](https://docs.dapr.io/reference/components-reference/supported-pubsub/setup-gcp-pubsub/)
                *   [In-memory](https://docs.dapr.io/reference/components-reference/supported-pubsub/setup-inmemory/)
                *   [JetStream](https://docs.dapr.io/reference/components-reference/supported-pubsub/setup-jetstream/)
                *   [KubeMQ](https://docs.dapr.io/reference/components-reference/supported-pubsub/setup-kubemq/)
                *   [MQTT](https://docs.dapr.io/reference/components-reference/supported-pubsub/setup-mqtt/)
                *   [MQTT3](https://docs.dapr.io/reference/components-reference/supported-pubsub/setup-mqtt3/)
                *   [Pulsar](https://docs.dapr.io/reference/components-reference/supported-pubsub/setup-pulsar/)
                *   [RabbitMQ](https://docs.dapr.io/reference/components-reference/supported-pubsub/setup-rabbitmq/)
                *   [Redis Streams](https://docs.dapr.io/reference/components-reference/supported-pubsub/setup-redis-pubsub/)
                *   [RocketMQ](https://docs.dapr.io/reference/components-reference/supported-pubsub/setup-rocketmq/)
                *   [Solace-AMQP](https://docs.dapr.io/reference/components-reference/supported-pubsub/setup-solace-amqp/)

            *   [Secret stores](https://docs.dapr.io/reference/components-reference/supported-secret-stores/ "Secret store component specs")
                *   [AlibabaCloud OOS Parameter Store](https://docs.dapr.io/reference/components-reference/supported-secret-stores/alicloud-oos-parameter-store/)
                *   [AWS Secrets Manager](https://docs.dapr.io/reference/components-reference/supported-secret-stores/aws-secret-manager/)
                *   [AWS SSM Parameter Store](https://docs.dapr.io/reference/components-reference/supported-secret-stores/aws-parameter-store/)
                *   [Azure Key Vault](https://docs.dapr.io/reference/components-reference/supported-secret-stores/azure-keyvault/ "Azure Key Vault secret store")
                *   [GCP Secret Manager](https://docs.dapr.io/reference/components-reference/supported-secret-stores/gcp-secret-manager/)
                *   [HashiCorp Vault](https://docs.dapr.io/reference/components-reference/supported-secret-stores/hashicorp-vault/)
                *   [HuaweiCloud Cloud Secret Management Service (CSMS)](https://docs.dapr.io/reference/components-reference/supported-secret-stores/huaweicloud-csms/)
                *   [Kubernetes secrets](https://docs.dapr.io/reference/components-reference/supported-secret-stores/kubernetes-secret-store/)
                *   [Local environment variables](https://docs.dapr.io/reference/components-reference/supported-secret-stores/envvar-secret-store/ "Local environment variables (for Development)")
                *   [Local file](https://docs.dapr.io/reference/components-reference/supported-secret-stores/file-secret-store/ "Local file (for Development)")
                *   [OpenBao](https://docs.dapr.io/reference/components-reference/supported-secret-stores/openbao/)
                *   [Tencent Cloud Secrets Manager (SSM)](https://docs.dapr.io/reference/components-reference/supported-secret-stores/tencentcloud-ssm/)

            *   [State stores](https://docs.dapr.io/reference/components-reference/supported-state-stores/ "State store component specs")
                *   [Aerospike](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-aerospike/)
                *   [Alibaba Cloud TableStore](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-alicloud-tablestore/)
                *   [AWS DynamoDB](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-dynamodb/)
                *   [Azure Blob Storage](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-azure-blobstorage/)
                *   [Azure Cosmos DB (SQL API)](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-azure-cosmosdb/)
                *   [Azure Table Storage](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-azure-tablestorage/)
                *   [Cassandra](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-cassandra/)
                *   [Cloudflare Workers KV](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-cloudflare-workerskv/)
                *   [CockroachDB](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-cockroachdb/)
                *   [Coherence](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-coherence/)
                *   [Couchbase](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-couchbase/)
                *   [Etcd](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-etcd/)
                *   [GCP Firestore](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-firestore/ "GCP Firestore (Datastore mode)")
                *   [HashiCorp Consul](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-consul/)
                *   [Hazelcast](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-hazelcast/)
                *   [In-memory](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-inmemory/)
                *   [JetStream KV](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-jetstream-kv/)
                *   [Memcached](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-memcached/)
                *   [Microsoft SQL Server & Azure SQL](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-sqlserver-v2/)
                *   [Microsoft SQL Server & Azure SQL](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-sqlserver/)
                *   [MongoDB](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-mongodb/)
                *   [MySQL & MariaDB](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-mysql/)
                *   [OCI Object Storage](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-oci-objectstorage/)
                *   [Oracle Database](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-oracledatabase/)
                *   [PostgreSQL](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-postgresql-v2/)
                *   [PostgreSQL v1](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-postgresql-v1/)
                *   [RavenDB](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-ravendb/)
                *   [Redis](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-redis/)
                *   [RethinkDB](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-rethinkdb/)
                *   [SQLite](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-sqlite/)
                *   [Zookeeper](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-zookeeper/)

        *   [Resource specs](https://docs.dapr.io/reference/resource-specs/ "Dapr resource specs")
            *   [Component](https://docs.dapr.io/reference/resource-specs/component-schema/ "Component spec")
            *   [Subscription](https://docs.dapr.io/reference/resource-specs/subscription-schema/ "Subscription spec")
            *   [Resiliency](https://docs.dapr.io/reference/resource-specs/resiliency-schema/ "Resiliency spec")
            *   [HTTPEndpoint](https://docs.dapr.io/reference/resource-specs/httpendpoints-schema/ "HTTPEndpoint spec")
            *   [Configuration](https://docs.dapr.io/reference/resource-specs/configuration-schema/ "Configuration spec")

    *   [Contributing](https://docs.dapr.io/contributing/ "Contributing to Dapr")
        *   [Overview](https://docs.dapr.io/contributing/contributing-overview/ "Contribution overview")
        *   [Presentations](https://docs.dapr.io/contributing/presentations/ "Giving a presentation on Dapr")
        *   [Roadmap](https://docs.dapr.io/contributing/roadmap/ "Dapr Roadmap")
        *   [GitHub Codespaces](https://docs.dapr.io/contributing/codespaces/ "Contributing with GitHub Codespaces")
        *   [Dapr bot](https://docs.dapr.io/contributing/daprbot/ "Dapr bot reference")
        *   [Docs](https://docs.dapr.io/contributing/docs-contrib/ "Docs contributing guide")
            *   [Contributors guide](https://docs.dapr.io/contributing/docs-contrib/contributing-docs/)
            *   [Maintainer guide](https://docs.dapr.io/contributing/docs-contrib/maintainer-guide/)
            *   [Docs templates](https://docs.dapr.io/contributing/docs-contrib/docs-templates/ "Suggested Dapr docs templates")
                *   [Conceptual template](https://docs.dapr.io/contributing/docs-contrib/docs-templates/concept-template/ "Conceptual article template")
                *   [Quickstart template](https://docs.dapr.io/contributing/docs-contrib/docs-templates/quickstart-template/ "Quickstart guide template")
                *   [How-to template](https://docs.dapr.io/contributing/docs-contrib/docs-templates/howto-template/ "How-to guide template")

        *   [SDKs](https://docs.dapr.io/contributing/sdk-contrib/ "SDK contributing guide")
            *   [.NET SDK](https://docs.dapr.io/contributing/sdk-contrib/dotnet-contributing/ "Contributing to the .NET SDK")
            *   [Go SDK](https://docs.dapr.io/contributing/sdk-contrib/go-contributing/ "Contributing to the Go SDK")
            *   [Java SDK](https://docs.dapr.io/contributing/sdk-contrib/java-contributing/ "Contributing to the Java SDK")
            *   [JavaScript SDK](https://docs.dapr.io/contributing/sdk-contrib/js-contributing/ "Contributing to the JavaScript SDK")
            *   [Python SDK](https://docs.dapr.io/contributing/sdk-contrib/python-contributing/ "Contributing to the Python SDK")
            *   [Rust SDK](https://docs.dapr.io/contributing/sdk-contrib/rust-contributing/ "Contributing to the Rust SDK")

        *   [Dapr Agents](https://docs.dapr.io/contributing/dapr-agents/ "Contributing to Dapr Agents")
        *   [Protocol Reference](https://docs.dapr.io/contributing/protocol-reference/)
            *   [Workflow](https://docs.dapr.io/contributing/protocol-reference/workflow-protocol/ "Workflow Protocol")
                *   [Management API](https://docs.dapr.io/contributing/protocol-reference/workflow-protocol/workflow-protocol-management-api/ "Workflow Protocol - Management API")
                *   [Execution API](https://docs.dapr.io/contributing/protocol-reference/workflow-protocol/workflow-protocol-execution-api/ "Workflow Protocol - Execution API")
                *   [Orchestration Lifecycle](https://docs.dapr.io/contributing/protocol-reference/workflow-protocol/workflow-protocol-orchestration-lifecycle/ "Workflow Protocol - Orchestration Lifecycle")
                *   [Activity Lifecycle](https://docs.dapr.io/contributing/protocol-reference/workflow-protocol/workflow-protocol-activity-lifecycle/ "Workflow Protocol - Activity Lifecycle")
                *   [State & History](https://docs.dapr.io/contributing/protocol-reference/workflow-protocol/workflow-protocol-state-and-history/ "Workflow Protocol - State & History")
                *   [Versioning](https://docs.dapr.io/contributing/protocol-reference/workflow-protocol/workflow-protocol-versioning/ "Workflow Protocol - Versioning")

[Edit this page](https://github.com/dapr/docs/edit/v1.17//daprdocs/content/en/developing-applications/building-blocks/workflow/workflow-features-concepts.md)[Create documentation issue](https://github.com/dapr/docs/issues/new/choose)[Create project issue](https://github.com/dapr/dapr/issues/new/choose)[Print entire section](https://docs.dapr.io/developing-applications/building-blocks/workflow/_print/)

*   [Workflows](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#workflows)
*   [Workflow Instance Management](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#workflow-instance-management)
    *   [Querying Workflow State](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#querying-workflow-state)
    *   [Workflow History](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#workflow-history)

*   [External Events](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#external-events)
    *   [Raising Events via CLI](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#raising-events-via-cli)

*   [Workflow Suspension and Resumption](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#workflow-suspension-and-resumption)
    *   [Using the CLI](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#using-the-cli)
    *   [Workflow identity](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#workflow-identity)
    *   [Workflow replay](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#workflow-replay)
    *   [Infinite loops and eternal workflows](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#infinite-loops-and-eternal-workflows)
    *   [Updating workflow code](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#updating-workflow-code)

*   [Workflow activities](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#workflow-activities)
*   [Child workflows](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#child-workflows)
*   [Durable timers](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#durable-timers)
*   [Retry policies](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#retry-policies)
*   [External events](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#external-events-1)
*   [Purging](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#purging)
*   [Versioning](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#versioning)
*   [Limitations](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#limitations)
    *   [Workflow determinism and code restraints](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#workflow-determinism-and-code-restraints)
    *   [Updating workflow code](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#updating-workflow-code-1)

*   [Next steps](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#next-steps)
*   [Related links](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#related-links)

1.   [Developing applications](https://docs.dapr.io/developing-applications/)
2.   [Building blocks](https://docs.dapr.io/developing-applications/building-blocks/)
3.   [Workflow](https://docs.dapr.io/developing-applications/building-blocks/workflow/)
4.   Features and concepts

Features and concepts
=====================

Learn more about the Dapr Workflow features and concepts

Now that you’ve learned about the [workflow building block](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-overview/) at a high level, let’s deep dive into the features and concepts included with the Dapr Workflow engine and SDKs. Dapr Workflow exposes several core features and concepts which are common across all supported languages.

#### Note

For more information on how workflow state is managed, see the [workflow architecture guide](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/).

Workflows
---------

Dapr Workflows are functions you write that define a series of tasks to be executed in a particular order. The Dapr Workflow engine takes care of scheduling and execution of the tasks, including managing failures and retries. If the app hosting your workflows is scaled out across multiple machines, the workflow engine load balances the execution of workflows and their tasks across multiple machines.

There are several different kinds of tasks that a workflow can schedule, including

*   [Activities](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#workflow-activities) for executing custom logic
*   [Durable timers](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#durable-timers) for putting the workflow to sleep for arbitrary lengths of time
*   [Child workflows](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#child-workflows) for breaking larger workflows into smaller pieces
*   [External event waiters](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#external-events) for blocking workflows until they receive external event signals. These tasks are described in more details in their corresponding sections.

Workflow Instance Management
----------------------------

### Querying Workflow State

You can query workflow instances using the CLI:

```bash
# Find all running workflows
dapr workflow list --app-id myapp --filter-status RUNNING

# Find workflows by name
dapr workflow list --app-id myapp --filter-name OrderProcessing

# Find recent workflows (last 2 hours)
dapr workflow list --app-id myapp --filter-max-age 2h

# Get detailed JSON output
dapr workflow list --app-id myapp --output json
```

### Workflow History

View the complete execution history:

```bash
dapr workflow history wf-12345 --app-id myapp --output json
```

This shows all events, activities, and state transitions.

External Events
---------------

### Raising Events via CLI

```bash
dapr workflow raise-event wf-12345/ApprovalReceived \
  --app-id myapp \
  --input '{"approved": true, "comments": "Approved by manager"}'
```

Workflow Suspension and Resumption
----------------------------------

### Using the CLI

```bash
# Suspend for manual intervention
dapr workflow suspend wf-12345 \
  --app-id myapp \
  --reason "Awaiting customer response"

# Resume when ready
dapr workflow resume wf-12345 \
  --app-id myapp \
  --reason "Customer responded"
```

### Workflow identity

Each workflow you define has a type name, and individual executions of a workflow require a unique _instance ID_. Workflow instance IDs can be generated by your app code, which is useful when workflows correspond to business entities like documents or jobs, or can be auto-generated UUIDs. A workflow’s instance ID is useful for debugging and also for managing workflows using the [Workflow APIs](https://docs.dapr.io/reference/api/workflow_api/).

Only one workflow instance with a given ID can exist at any given time. However, if a workflow instance completes or fails, its ID can be reused by a new workflow instance. Note, however, that the new workflow instance effectively replaces the old one in the configured state store.

### Workflow replay

Dapr Workflows maintain their execution state by using a technique known as [event sourcing](https://learn.microsoft.com/azure/architecture/patterns/event-sourcing). Instead of storing the current state of a workflow as a snapshot, the workflow engine manages an append-only log of history events that describe the various steps that a workflow has taken. When using the workflow SDK, these history events are stored automatically whenever the workflow “awaits” for the result of a scheduled task.

When a workflow “awaits” a scheduled task, it unloads itself from memory until the task completes. Once the task completes, the workflow engine schedules the workflow function to run again. This second workflow function execution is known as a _replay_.

When a workflow function is replayed, it runs again from the beginning. However, when it encounters a task that already completed, instead of scheduling that task again, the workflow engine:

1.   Returns the stored result of the completed task to the workflow.
2.   Continues execution until the next “await” point.

This “replay” behavior continues until the workflow function completes or fails with an error.

Using this replay technique, a workflow is able to resume execution from any “await” point as if it had never been unloaded from memory. Even the values of local variables from previous runs can be restored without the workflow engine knowing anything about what data they stored. This ability to restore state makes Dapr Workflows _durable_ and _fault tolerant_.

#### Note

The workflow replay behavior described here requires that workflow function code be _deterministic_. Deterministic workflow functions take the exact same actions when provided the exact same inputs. [Learn more about the limitations around deterministic workflow code.](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#workflow-determinism-and-code-restraints)

### Infinite loops and eternal workflows

As discussed in the [workflow replay](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#workflow-replay) section, workflows maintain a write-only event-sourced history log of all its operations. To avoid runaway resource usage, workflows must limit the number of operations they schedule. For example, ensure your workflow doesn’t:

*   Use infinite loops in its implementation
*   Schedule thousands of tasks.

You can use the following two techniques to write workflows that may need to schedule extreme numbers of tasks:

1.   **Use the _continue-as-new_ API**: Each workflow SDK exposes a _continue-as-new_ API that workflows can invoke to restart themselves with a new input and history. The _continue-as-new_ API is especially ideal for implementing “eternal workflows”, like monitoring agents, which would otherwise be implemented using a `while (true)`-like construct. Using _continue-as-new_ is a great way to keep the workflow history size small.

> The _continue-as-new_ API truncates the existing history, replacing it with a new history.

2.   **Use child workflows**: Each workflow SDK exposes an API for creating child workflows. A child workflow behaves like any other workflow, except that it’s scheduled by a parent workflow. Child workflows have:

    *   Their own history
    *   The benefit of distributing workflow function execution across multiple machines.

If a workflow needs to schedule thousands of tasks or more, it’s recommended that those tasks be distributed across child workflows so that no single workflow’s history size grows too large.

### Updating workflow code

Because workflows are long-running and durable, updating workflow code must be done with extreme care. As discussed in the [workflow determinism](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#workflow-determinism-and-code-restraints) limitation section, workflow code must be deterministic. Updates to workflow code must preserve this determinism if there are any non-completed workflow instances in the system. Otherwise, updates to workflow code can result in runtime failures the next time those workflows execute.

[See known limitations](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#limitations)

Workflow activities
-------------------

Workflow activities are the basic unit of work in a workflow and are the tasks that get orchestrated in the business process. For example, you might create a workflow to process an order. The tasks may involve checking the inventory, charging the customer, and creating a shipment. Each task would be a separate activity. These activities may be executed serially, in parallel, or some combination of both.

Unlike workflows, activities aren’t restricted in the type of work you can do in them. Activities are frequently used to make network calls or run CPU intensive operations. An activity can also return data back to the workflow.

The Dapr Workflow engine guarantees that each called activity is executed **at least once** as part of a workflow’s execution. Because activities only guarantee at-least-once execution, it’s recommended that activity logic be implemented as idempotent whenever possible.

Child workflows
---------------

In addition to activities, workflows can schedule other workflows as _child workflows_. A child workflow has its own instance ID, history, and status that is independent of the parent workflow that started it.

Child workflows have many benefits:

*   You can split large workflows into a series of smaller child workflows, making your code more maintainable.
*   You can distribute workflow logic across multiple compute nodes concurrently, which is useful if your workflow logic otherwise needs to coordinate a lot of tasks.
*   You can reduce memory usage and CPU overhead by keeping the history of parent workflow smaller.

The return value of a child workflow is its output. If a child workflow fails with an exception, then that exception is surfaced to the parent workflow, just like it is when an activity task fails with an exception. Child workflows also support automatic retry policies.

Terminating a parent workflow terminates all of the child workflows created by the workflow instance. See [the terminate workflow api](https://docs.dapr.io/reference/api/workflow_api/#terminate-workflow-request) for more information.

Durable timers
--------------

Dapr Workflows allow you to schedule reminder-like durable delays for any time range, including minutes, days, or even years. These _durable timers_ can be scheduled by workflows to implement simple delays or to set up ad-hoc timeouts on other async tasks. More specifically, a durable timer can be set to trigger on a particular date or after a specified duration. There are no limits to the maximum duration of durable timers, which are internally backed by internal actor reminders. For example, a workflow that tracks a 30-day free subscription to a service could be implemented using a durable timer that fires 30-days after the workflow is created. Workflows can be safely unloaded from memory while waiting for a durable timer to fire.

#### Note

Some APIs in the workflow authoring SDK may internally schedule durable timers to implement internal timeout behavior.

Retry policies
--------------

Workflows support durable retry policies for activities and child workflows. Workflow retry policies are separate and distinct from [Dapr resiliency policies](https://docs.dapr.io/operations/resiliency/resiliency-overview/) in the following ways.

*   Workflow retry policies are configured by the workflow author in code, whereas Dapr Resiliency policies are configured by the application operator in YAML.
*   Workflow retry policies are durable and maintain their state across application restarts, whereas Dapr Resiliency policies are not durable and must be re-applied after application restarts.
*   Workflow retry policies are triggered by unhandled errors/exceptions in activities and child workflows, whereas Dapr Resiliency policies are triggered by operation timeouts and connectivity faults.

Retries are internally implemented using durable timers. This means that workflows can be safely unloaded from memory while waiting for a retry to fire, conserving system resources. This also means that delays between retries can be arbitrarily long, including minutes, hours, or even days.

#### Note

The actions performed by a retry policy are saved into a workflow’s history. Care must be taken not to change the behavior of a retry policy after a workflow has already been executed. Otherwise, the workflow may behave unexpectedly when replayed. See the notes on [updating workflow code](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#updating-workflow-code) for more information.

It’s possible to use both workflow retry policies and Dapr Resiliency policies together. For example, if a workflow activity uses a Dapr client to invoke a service, the Dapr client uses the configured resiliency policy. See [Quickstart: Service-to-service resiliency](https://docs.dapr.io/getting-started/quickstarts/resiliency/resiliency-serviceinvo-quickstart/) for more information with an example. However, if the activity itself fails for any reason, including exhausting the retries on the resiliency policy, then the workflow’s resiliency policy kicks in.

#### Note

Using workflow retry policies and resiliency policies together can result in unexpected behavior. For example, if a workflow activity exhausts its configured retry policy, the workflow engine will still retry the activity according to the workflow retry policy. This can result in the activity being retried more times than expected.

Because workflow retry policies are configured in code, the exact developer experience may vary depending on the version of the workflow SDK. In general, workflow retry policies can be configured with the following parameters.

| Parameter | Description |
| --- | --- |
| **Maximum number of attempts** | The maximum number of times to execute the activity or child workflow. If set to 0, no attempts will be made. |
| **First retry interval** | The amount of time to wait before the first retry. |
| **Backoff coefficient** | The coefficient used to determine the rate of increase of back-off. For example a coefficient of 2 doubles the wait of each subsequent retry. |
| **Maximum retry interval** | The maximum amount of time to wait before each subsequent retry. If set to 0, no retries will happen. |
| **Retry timeout** | The global timeout for retries, regardless of any configured max number of attempts. No further attempts are made executing activities after this timeout expires. |

External events
---------------

Sometimes workflows will need to wait for events that are raised by external systems. For example, an approval workflow may require a human to explicitly approve an order request within an order processing workflow if the total cost exceeds some threshold. Another example is a trivia game orchestration workflow that pauses while waiting for all participants to submit their answers to trivia questions. These mid-execution inputs are referred to as _external events_.

External events have a _name_ and a _payload_ and are delivered to a single workflow instance. Workflows can create “_wait for external event_” tasks that subscribe to external events and _await_ those tasks to block execution until the event is received. The workflow can then read the payload of these events and make decisions about which next steps to take. External events can be processed serially or in parallel. External events can be raised by other workflows or by workflow code.

Workflows can also wait for multiple external event signals of the same name, in which case they are dispatched to the corresponding workflow tasks in a first-in, first-out (FIFO) manner. If a workflow receives an external event signal but has not yet created a “wait for external event” task, the event will be saved into the workflow’s history and consumed immediately after the workflow requests the event.

Learn more about [external system interaction.](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-patterns/#external-system-interaction)

Purging
-------

Workflow state can be purged from a state store, purging all its history and removing all metadata related to a specific workflow instance. The purge capability is used for workflows that have run to a `COMPLETED`, `FAILED`, or `TERMINATED` state.

Learn more in [the workflow API reference guide](https://docs.dapr.io/reference/api/workflow_api/).

Versioning
----------

Workflow code is long-running and must remain deterministic during updates. For details on patching and named workflow versioning, see [Workflow versioning](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-versioning/).

Limitations
-----------

### Workflow determinism and code restraints

To take advantage of the workflow replay technique, your workflow code needs to be deterministic. For your workflow code to be deterministic, you may need to work around some limitations.

#### Workflow functions must call deterministic APIs

APIs that generate random numbers, random UUIDs, or the current date are _non-deterministic_. To work around this limitation, you can:

*   Use these APIs in activity functions, or
*   (Preferred) Use built-in equivalent APIs offered by the SDK. For example, each authoring SDK provides an API for retrieving the current time in a deterministic manner.

For example, instead of this:

*    .NET
*    Java
*    JavaScript
*    Go

```csharp
// DON'T DO THIS!
DateTime currentTime = DateTime.UtcNow;
Guid newIdentifier = Guid.NewGuid();
string randomString = GetRandomString();
```

```java
// DON'T DO THIS!
Instant currentTime = Instant.now();
UUID newIdentifier = UUID.randomUUID();
String randomString = getRandomString();
```

```javascript
// DON'T DO THIS!
const currentTime = new Date();
const newIdentifier = uuidv4();
const randomString = getRandomString();
```

```go
// DON'T DO THIS!
const currentTime = time.Now()
```

Do this:

*    .NET
*    Java
*    JavaScript
*    Go

```csharp
// Do this!!
DateTime currentTime = context.CurrentUtcDateTime;
Guid newIdentifier = context.NewGuid();
string randomString = await context.CallActivityAsync<string>(nameof("GetRandomString")); //Use "nameof" to prevent specifying an activity name that does not exist in your application
```

```java
// Do this!!
Instant currentTime = context.getCurrentInstant();
Guid newIdentifier = context.newGuid();
String randomString = context.callActivity(GetRandomString.class.getName(), String.class).await();
```

```javascript
// Do this!!
const currentTime = context.getCurrentUtcDateTime();
const randomString = yield context.callActivity(getRandomString);
```

```go
const currentTime = ctx.CurrentUTCDateTime()
```

#### Workflow functions must only interact _indirectly_ with external state.

External data includes any data that isn’t stored in the workflow state. Workflows must not interact with global variables, environment variables, the file system, or make network calls.

Instead, workflows should interact with external state _indirectly_ using workflow inputs, activity tasks, and through external event handling.

For example, instead of this:

*    .NET
*    Java
*    JavaScript
*    Go

```csharp
// DON'T DO THIS!
string configuration = Environment.GetEnvironmentVariable("MY_CONFIGURATION")!;
string data = await new HttpClient().GetStringAsync("https://example.com/api/data");
```

```java
// DON'T DO THIS!
String configuration = System.getenv("MY_CONFIGURATION");

HttpRequest request = HttpRequest.newBuilder().uri(new URI("https://postman-echo.com/post")).GET().build();
HttpResponse<String> response = HttpClient.newBuilder().build().send(request, HttpResponse.BodyHandlers.ofString());
```

```javascript
// DON'T DO THIS!
// Accessing an Environment Variable (Node.js)
const configuration = process.env.MY_CONFIGURATION;

fetch('https://postman-echo.com/get')
  .then(response => response.text())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Error:', error);
  });
```

```go
// DON'T DO THIS!
resp, err := http.Get("http://example.com/api/data")
```

Do this:

*    .NET
*    Java
*    JavaScript
*    Go

```csharp
// Do this!!
string configuration = workflowInput.Configuration; // imaginary workflow input argument
string data = await context.CallActivityAsync<string>(nameof("MakeHttpCall"), "https://example.com/api/data");
```

```java
// Do this!!
String configuration = ctx.getInput(InputType.class).getConfiguration(); // imaginary workflow input argument
String data = ctx.callActivity(MakeHttpCall.class, "https://example.com/api/data", String.class).await();
```

```javascript
// Do this!!
const configuration = workflowInput.getConfiguration(); // imaginary workflow input argument
const data = yield ctx.callActivity(makeHttpCall, "https://example.com/api/data");
```

```go
// Do this!!
err := ctx.CallActivity(MakeHttpCallActivity, workflow.ActivityInput("https://example.com/api/data")).Await(&output)
```

#### Workflow functions must execute only on the workflow dispatch thread.

The implementation of each language SDK requires that all workflow function operations operate on the same thread (goroutine, etc.) that the function was scheduled on. Workflow functions must never:

*   Schedule background threads, or
*   Use APIs that schedule a callback function to run on another thread.

Failure to follow this rule could result in undefined behavior. Any background processing should instead be delegated to activity tasks, which can be scheduled to run serially or concurrently.

For example, instead of this:

*    .NET
*    Java
*    JavaScript
*    Go

```csharp
// DON'T DO THIS!
Task t = Task.Run(() => context.CallActivityAsync("DoSomething"));
await context.CreateTimer(5000).ConfigureAwait(false);
```

```java
// DON'T DO THIS!
new Thread(() -> {
    ctx.callActivity(DoSomethingActivity.class.getName()).await();
}).start();
ctx.createTimer(Duration.ofSeconds(5)).await();
```

Don’t declare JavaScript workflow as `async`. The Node.js runtime doesn’t guarantee that asynchronous functions are deterministic.

```go
// DON'T DO THIS!
go func() {
  err := ctx.CallActivity(DoSomething).Await(nil)
}()
err := ctx.CreateTimer(time.Second).Await(nil)
```

Do this:

*    .NET
*    Java
*    JavaScript
*    Go

```csharp
// Do this!!
Task t = context.CallActivityAsync(nameof("DoSomething"));
await context.CreateTimer(5000).ConfigureAwait(true);
```

```java
// Do this!!
ctx.callActivity(DoSomethingActivity.class.getName()).await();
ctx.createTimer(Duration.ofSeconds(5)).await();
```

Since the Node.js runtime doesn’t guarantee that asynchronous functions are deterministic, always declare JavaScript workflow as synchronous generator functions.

```go
// Do this!
task := ctx.CallActivity(DoSomething)
task.Await(nil)
```

### Updating workflow code

Make sure updates you make to the workflow code maintain its determinism. Here are a few example of code updates that can break workflow determinism:

*   **Changing the workflow function signature**: Changing the name, input, or output of a workflow or activity is considered a breaking change and must be avoided.
*   **Changing the number or order of workflow tasks**: Changing the number or order of workflow tasks causes a workflow’s history to no longer match the workflow code and may result in runtime errors or other unexpected behavior.

To work around these constraints, use the workflow [versioning](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-versioning/) concepts described in the versioning guide to patch and introduce new named workflow versions to incorporate changes to your workflows deterministically.

Next steps
----------

[Workflow patterns >>](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-patterns/)
Related links
-------------

*   [Try out Dapr Workflow using the quickstart](https://docs.dapr.io/getting-started/quickstarts/workflow-quickstart/)
*   [Workflow overview](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-overview/)
*   [Workflow API reference](https://docs.dapr.io/reference/api/workflow_api/)
*   Try out the following examples:
    *   [Python](https://github.com/dapr/python-sdk/tree/master/examples/demo_workflow)
    *   [JavaScript](https://github.com/dapr/js-sdk/tree/main/examples/workflow)
    *   [.NET](https://github.com/dapr/dotnet-sdk/tree/master/examples/Workflow)
    *   [Java](https://github.com/dapr/java-sdk/tree/master/examples/src/main/java/io/dapr/examples/workflows)
    *   [Go](https://github.com/dapr/go-sdk/tree/main/examples/workflow/README.md)

Last modified March 3, 2026: [Merge pull request #5062 from JoshVanL/wf-versioning-cli-example (3b5020c)](https://github.com/dapr/docs/commit/3b5020cab259e29c3330b7215d10f7a6dd8ede4b)

*   [](https://www.youtube.com/@darpdev)
*   [](https://www.linkedin.com/company/daprdev/)
*   [](https://twitter.com/daprdev)
*   [](https://bsky.app/profile/daprdev.bsky.social)

*   [](https://github.com/dapr/)
*   [](https://bit.ly/dapr-discord)

© 2026 The Linux Foundation. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage](https://linuxfoundation.org/trademark-usage/) page.

![Image 1](https://static.scarf.sh/a.png?x-pxid=4848fb3b-3edb-4329-90a9-a9d79afff054)
