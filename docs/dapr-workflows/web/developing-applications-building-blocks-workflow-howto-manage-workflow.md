# Source: https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-manage-workflow/

Title: How to: Manage workflows

URL Source: https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-manage-workflow/

Markdown Content:
How to: Manage workflows | Dapr Docs
===============
[Dapr Docs](https://docs.dapr.io/)

*   [Homepage](https://dapr.io/)
*   [GitHub](https://github.com/dapr)
*   [Blog](https://blog.dapr.io/posts)
*   [Discord](https://bit.ly/dapr-discord)
*   [Community](https://dapr.io/community)
*   
[v1.17 (latest)](https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-manage-workflow/#)
    *   [v1.18 (preview)](https://v1-18.docs.dapr.io/)
    *   [v1.17 (latest)](https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-manage-workflow/#)
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
[English](https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-manage-workflow/#)
    *   [简体中文](https://docs.dapr.io/zh-hans/developing-applications/building-blocks/workflow/howto-manage-workflow/)

Search

[English](https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-manage-workflow/#)
*   [简体中文](https://docs.dapr.io/zh-hans/developing-applications/building-blocks/workflow/howto-manage-workflow/)

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

[Edit this page](https://github.com/dapr/docs/edit/v1.17//daprdocs/content/en/developing-applications/building-blocks/workflow/howto-manage-workflow.md)[Create documentation issue](https://github.com/dapr/docs/issues/new/choose)[Create project issue](https://github.com/dapr/dapr/issues/new/choose)[Print entire section](https://docs.dapr.io/developing-applications/building-blocks/workflow/_print/)

*   [Next steps](https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-manage-workflow/#next-steps)
*   [Related links](https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-manage-workflow/#related-links)

1.   [Developing applications](https://docs.dapr.io/developing-applications/)
2.   [Building blocks](https://docs.dapr.io/developing-applications/building-blocks/)
3.   [Workflow](https://docs.dapr.io/developing-applications/building-blocks/workflow/)
4.   How to: Manage workflows

How to: Manage workflows
========================

Manage and run workflows

Now that you’ve [authored the workflow and its activities in your application](https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-author-workflow/), you can start, terminate, rerun, and get information about the workflow using the CLI or API calls.

*    CLI
*    Python
*    JavaScript
*    .NET
*    Java
*    Go
*    HTTP

Managing Workflows with the Dapr CLI
------------------------------------

The Dapr CLI provides commands for managing workflow instances in both self-hosted and Kubernetes environments.

See also [Workflow Retention Policy](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-history-retention-policy/) for information on how to configure retention policies for completed workflows.

### Basic Workflow Operations

#### Start a Workflow

```bash
# Using the `orderprocessing` application, start a new workflow instance with input data
dapr workflow run OrderProcessingWorkflow \
  --app-id orderprocessing \
  --input '{"orderId": "12345", "amount": 100.50}'

# Start with a new workflow with a specific instance ID
dapr workflow run OrderProcessingWorkflow \
  --app-id orderprocessing \
  --instance-id order-12345 \
  --input '{"orderId": "12345"}'

# Schedule a new workflow to start at 10:00:00 AM on December 25, 2024, Coordinated Universal Time (UTC).
dapr workflow run OrderProcessingWorkflow \
  --app-id orderprocessing \
  --start-time "2024-12-25T10:00:00Z"
```

#### List Workflow Instances

```bash
# List all workflows for an app
dapr workflow list

# Filter by status
dapr workflow list --filter-status RUNNING

# Filter by workflow name and app ID
dapr workflow list --app-id orderprocessing --filter-name OrderProcessingWorkflow

# Filter by age (workflows started in last 24 hours)
dapr workflow list --filter-max-age 24h

# Get detailed output
dapr workflow list -o wide
```

#### View Workflow History

```bash
# Get execution history
dapr workflow history order-12345

# Get history in JSON format on a particular app ID.
dapr workflow history order-12345 --app-id orderprocessing --output json
```

#### Control Workflow Execution

```bash
# Suspend a running workflow
dapr workflow suspend order-12345 \
  --app-id orderprocessing \
  --reason "Waiting for manual approval"

# Resume a suspended workflow
dapr workflow resume order-12345 \
  --app-id orderprocessing \
  --reason "Approved by manager"

# Terminate a workflow
dapr workflow terminate order-12345 \
  --app-id orderprocessing \
  --output '{"reason": "Cancelled by customer"}'
```

#### Raise External Events

```bash
# Raise an event for a waiting workflow
dapr workflow raise-event order-12345/PaymentReceived \
  --app-id orderprocessing \
  --input '{"paymentId": "pay-67890", "amount": 100.50}'
```

#### Re-run Workflows

```bash
# Re-run from the beginning
dapr workflow rerun order-12345

# Re-run from a specific event ID, discovered via the history command
dapr workflow rerun order-12345 --event-id 5

# Re-run with a new specified instance ID
dapr workflow rerun order-12345 --new-instance-id order-12345-retry
```

#### Purge Completed Workflows

Note that purging a workflow from the CLI will also delete all associated Scheduler reminders.

#### Important

```
<p>It is required that a workflow client is running in the application to perform purge operations.</p>
```

The workflow client connection is required in order to preserve the workflow state machine integrity and prevent corruption. Errors like the following suggest that the workflow client is not running:

```
failed to purge orchestration state: rpc error: code = FailedPrecondition desc = failed to purge orchestration state: failed to lookup actor: api error: code = FailedPrecondition desc = did not find address for actor
```

It is possible to purge a workflow _without_ a workflow application running by using the `--force` flag; however, this should only be used when you are certain that no workflow instances are currently running, as it **will** otherwise corrupt the workflow state machine.

```bash
# Purge a specific instance
dapr workflow purge order-12345

# Purge all completed workflows older than 30 days
dapr workflow purge --all-older-than 720h

# Purge all terminal workflows (use with caution!)
dapr workflow purge --app-id orderprocessing --all

# Force a purge without a running workflow client (use with extreme caution!)
dapr workflow purge order-12345 --force
```

### Kubernetes Operations

All commands support the `-k` flag for Kubernetes deployments:

```bash
# List workflows in Kubernetes
dapr workflow list \
  --kubernetes \
  --namespace production \
  --app-id orderprocessing

# Suspend a workflow in Kubernetes
dapr workflow suspend order-12345 \
  --kubernetes \
  --namespace production \
  --app-id orderprocessing \
  --reason "Maintenance window"
```

### Listing Workflows

In self-hosted mode, simply run:

```bash
dapr workflow list
```

In Kubernetes mode, specify the `--kubernetes`/`-k` flag along with the namespace and app ID:

```bash
dapr workflow list -k
```

### Workflow Management Best Practices

1.   **Monitor Running Workflows**: Use filtered lists to track long-running instances

```bash
dapr workflow list --app-id orderprocessing --filter-status RUNNING --filter-max-age 24h
``` 
2.   **Use Instance IDs**: Assign meaningful instance IDs for easier tracking

```bash
dapr workflow run OrderWorkflow --app-id orderprocessing --instance-id "order-$(date +%s)"
``` 
3.   **Export for Analysis**: Export workflow data for analysis

```bash
dapr workflow list --app-id orderprocessing --output json > workflows.json
``` 

Managing Workflow Reminders with the Dapr CLI
---------------------------------------------

Workflow reminders are stored in the Scheduler and can be managed using the dapr scheduler CLI.

#### List workflow reminders

```bash
dapr scheduler list --filter workflow
NAME                                           BEGIN     COUNT  LAST TRIGGER
workflow/my-app/instance1/timer-0-ABC123       +50.0h    0
workflow/my-app/instance2/timer-0-XYZ789       +50.0h    0
```

Get reminder details

```bash
dapr scheduler get workflow/my-app/instance1/timer-0-ABC123 -o yaml
```

#### Delete workflow reminders

Delete a single reminder:

```bash
dapr scheduler delete workflow/my-app/instance1/timer-0-ABC123
```

Delete all reminders for a given workflow app"

```bash
dapr scheduler delete-all workflow/my-app
```

Delete all reminders for a specific workflow instance:

```bash
dapr scheduler delete-all workflow/my-app/instance1
```

#### Backup and restore reminders

Export all reminders:

```bash
dapr scheduler export -o workflow-reminders-backup.bin
```

Restore from a backup file:

```bash
dapr scheduler import -f workflow-reminders-backup.bin
```

Manage your workflow within your code. In the workflow example from the [Author a workflow](https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-author-workflow/#write-the-application) guide, the workflow is registered in the code using the following APIs:

*   **schedule_new_workflow**: Start an instance of a workflow
*   **get_workflow_state**: Get information on the status of the workflow
*   **pause_workflow**: Pauses or suspends a workflow instance that can later be resumed
*   **resume_workflow**: Resumes a paused workflow instance
*   **raise_workflow_event**: Raise an event on a workflow
*   **purge_workflow**: Removes all metadata related to a specific workflow instance
*   **wait_for_workflow_completion**: Complete a particular instance of a workflow

```python
from dapr.ext.workflow import WorkflowRuntime, DaprWorkflowContext, WorkflowActivityContext
from dapr.clients import DaprClient

# Sane parameters
instanceId = "exampleInstanceID"
workflowComponent = "dapr"
workflowName = "hello_world_wf"
eventName = "event1"
eventData = "eventData"

# Start the workflow
wf_client.schedule_new_workflow(
        workflow=hello_world_wf, input=input_data, instance_id=instance_id
    )

# Get info on the workflow
wf_client.get_workflow_state(instance_id=instance_id)

# Pause the workflow
wf_client.pause_workflow(instance_id=instance_id)
    metadata = wf_client.get_workflow_state(instance_id=instance_id)

# Resume the workflow
wf_client.resume_workflow(instance_id=instance_id)

# Raise an event on the workflow.
wf_client.raise_workflow_event(instance_id=instance_id, event_name=event_name, data=event_data)

# Purge the workflow
wf_client.purge_workflow(instance_id=instance_id)

# Wait for workflow completion
wf_client.wait_for_workflow_completion(instance_id, timeout_in_seconds=30)
```

Manage your workflow within your code. In the workflow example from the [Author a workflow](https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-author-workflow/#write-the-application) guide, the workflow is registered in the code using the following APIs:

*   **client.workflow.start**: Start an instance of a workflow
*   **client.workflow.get**: Get information on the status of the workflow
*   **client.workflow.pause**: Pauses or suspends a workflow instance that can later be resumed
*   **client.workflow.resume**: Resumes a paused workflow instance
*   **client.workflow.purge**: Removes all metadata related to a specific workflow instance
*   **client.workflow.terminate**: Terminate or stop a particular instance of a workflow

```javascript
import { DaprClient } from "@dapr/dapr";

async function printWorkflowStatus(client: DaprClient, instanceId: string) {
  const workflow = await client.workflow.get(instanceId);
  console.log(
    `Workflow ${workflow.workflowName}, created at ${workflow.createdAt.toUTCString()}, has status ${
      workflow.runtimeStatus
    }`,
  );
  console.log(`Additional properties: ${JSON.stringify(workflow.properties)}`);
  console.log("--------------------------------------------------\n\n");
}

async function start() {
  const client = new DaprClient();

  // Start a new workflow instance
  const instanceId = await client.workflow.start("OrderProcessingWorkflow", {
    Name: "Paperclips",
    TotalCost: 99.95,
    Quantity: 4,
  });
  console.log(`Started workflow instance ${instanceId}`);
  await printWorkflowStatus(client, instanceId);

  // Pause a workflow instance
  await client.workflow.pause(instanceId);
  console.log(`Paused workflow instance ${instanceId}`);
  await printWorkflowStatus(client, instanceId);

  // Resume a workflow instance
  await client.workflow.resume(instanceId);
  console.log(`Resumed workflow instance ${instanceId}`);
  await printWorkflowStatus(client, instanceId);

  // Terminate a workflow instance
  await client.workflow.terminate(instanceId);
  console.log(`Terminated workflow instance ${instanceId}`);
  await printWorkflowStatus(client, instanceId);

  // Wait for the workflow to complete, 30 seconds!
  await new Promise((resolve) => setTimeout(resolve, 30000));
  await printWorkflowStatus(client, instanceId);

  // Purge a workflow instance
  await client.workflow.purge(instanceId);
  console.log(`Purged workflow instance ${instanceId}`);
  // This will throw an error because the workflow instance no longer exists.
  await printWorkflowStatus(client, instanceId);
}

start().catch((e) => {
  console.error(e);
  process.exit(1);
});
```

Manage your workflow within your code. In the `OrderProcessingWorkflow` example from the [Author a workflow](https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-author-workflow/#write-the-application) guide, the workflow is registered in the code. You can now start, terminate, and get information about a running workflow:

```csharp
string orderId = "exampleOrderId";
OrderPayload input = new OrderPayload("Paperclips", 99.95);
Dictionary<string, string> workflowOptions; // This is an optional parameter

// Start the workflow using the orderId as our workflow ID. This returns a string containing the instance ID for the particular workflow instance, whether we provide it ourselves or not.
await daprWorkflowClient.ScheduleNewWorkflowAsync(nameof(OrderProcessingWorkflow), orderId, input, workflowOptions);

// Get information on the workflow. This response contains information such as the status of the workflow, when it started, and more!
WorkflowState currentState = await daprWorkflowClient.GetWorkflowStateAsync(orderId, orderId);

// Terminate the workflow
await daprWorkflowClient.TerminateWorkflowAsync(orderId);

// Raise an event (an incoming purchase order) that your workflow will wait for
await daprWorkflowClient.RaiseEventAsync(orderId, "incoming-purchase-order", input);

// Pause
await daprWorkflowClient.SuspendWorkflowAsync(orderId);

// Resume
await daprWorkflowClient.ResumeWorkflowAsync(orderId);

// Purge the workflow, removing all inbox and history information from associated instance
await daprWorkflowClient.PurgeInstanceAsync(orderId);
```

Manage your workflow within your code. [In the workflow example from the Java SDK](https://github.com/dapr/java-sdk/blob/master/examples/src/main/java/io/dapr/examples/workflows/), the workflow is registered in the code using the following APIs:

*   **scheduleNewWorkflow**: Starts a new workflow instance
*   **getInstanceState**: Get information on the status of the workflow
*   **waitForInstanceStart**: Pauses or suspends a workflow instance that can later be resumed
*   **raiseEvent**: Raises events/tasks for the running workflow instance
*   **waitForInstanceCompletion**: Waits for the workflow to complete its tasks
*   **purgeInstance**: Removes all metadata related to a specific workflow instance
*   **terminateWorkflow**: Terminates the workflow
*   **purgeInstance**: Removes all metadata related to a specific workflow

```java
package io.dapr.examples.workflows;

import io.dapr.workflows.client.DaprWorkflowClient;
import io.dapr.workflows.client.WorkflowInstanceStatus;

// ...
public class DemoWorkflowClient {

  // ...
  public static void main(String[] args) throws InterruptedException {
    DaprWorkflowClient client = new DaprWorkflowClient();

    try (client) {
      // Start a workflow
      String instanceId = client.scheduleNewWorkflow(DemoWorkflow.class, "input data");
      
      // Get status information on the workflow
      WorkflowInstanceStatus workflowMetadata = client.getInstanceState(instanceId, true);

      // Wait or pause for the workflow instance start
      try {
        WorkflowInstanceStatus waitForInstanceStartResult =
            client.waitForInstanceStart(instanceId, Duration.ofSeconds(60), true);
      }

      // Raise an event for the workflow; you can raise several events in parallel
      client.raiseEvent(instanceId, "TestEvent", "TestEventPayload");
      client.raiseEvent(instanceId, "event1", "TestEvent 1 Payload");
      client.raiseEvent(instanceId, "event2", "TestEvent 2 Payload");
      client.raiseEvent(instanceId, "event3", "TestEvent 3 Payload");

      // Wait for workflow to complete running through tasks
      try {
        WorkflowInstanceStatus waitForInstanceCompletionResult =
            client.waitForInstanceCompletion(instanceId, Duration.ofSeconds(60), true);
      } 

      // Purge the workflow instance, removing all metadata associated with it
      boolean purgeResult = client.purgeInstance(instanceId);

      // Terminate the workflow instance
      client.terminateWorkflow(instanceToTerminateId, null);

    System.exit(0);
  }
}
```

Manage your workflow within your code. [In the workflow example from the Go SDK](https://github.com/dapr/go-sdk/tree/main/examples/workflow), the workflow is registered in the code using the following APIs:

*   **StartWorkflow**: Starts a new workflow instance
*   **GetWorkflow**: Get information on the status of the workflow
*   **PauseWorkflow**: Pauses or suspends a workflow instance that can later be resumed
*   **RaiseEventWorkflow**: Raises events/tasks for the running workflow instance
*   **ResumeWorkflow**: Waits for the workflow to complete its tasks
*   **PurgeWorkflow**: Removes all metadata related to a specific workflow instance
*   **TerminateWorkflow**: Terminates the workflow

```go
// Start workflow
type StartWorkflowRequest struct {
	InstanceID        string // Optional instance identifier
	WorkflowComponent string
	WorkflowName      string
	Options           map[string]string // Optional metadata
	Input             any               // Optional input
	SendRawInput      bool              // Set to True in order to disable serialization on the input
}

type StartWorkflowResponse struct {
	InstanceID string
}

// Get the workflow status
type GetWorkflowRequest struct {
	InstanceID        string
	WorkflowComponent string
}

type GetWorkflowResponse struct {
	InstanceID    string
	WorkflowName  string
	CreatedAt     time.Time
	LastUpdatedAt time.Time
	RuntimeStatus string
	Properties    map[string]string
}

// Purge workflow
type PurgeWorkflowRequest struct {
	InstanceID        string
	WorkflowComponent string
}

// Terminate workflow
type TerminateWorkflowRequest struct {
	InstanceID        string
	WorkflowComponent string
}

// Pause workflow
type PauseWorkflowRequest struct {
	InstanceID        string
	WorkflowComponent string
}

// Resume workflow
type ResumeWorkflowRequest struct {
	InstanceID        string
	WorkflowComponent string
}

// Raise an event for the running workflow
type RaiseEventWorkflowRequest struct {
	InstanceID        string
	WorkflowComponent string
	EventName         string
	EventData         any
	SendRawData       bool // Set to True in order to disable serialization on the data
}
```

Manage your workflow using HTTP calls. The example below plugs in the properties from the [Author a workflow example](https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-author-workflow/#write-the-workflow) with a random instance ID number.

### Start workflow

To start your workflow with an ID `12345678`, run:

```shell
curl -X POST "http://localhost:3500/v1.0/workflows/dapr/OrderProcessingWorkflow/start?instanceID=12345678"
```

Note that workflow instance IDs can only contain alphanumeric characters, underscores, and dashes.

### Terminate workflow

To terminate your workflow with an ID `12345678`, run:

```shell
curl -X POST "http://localhost:3500/v1.0/workflows/dapr/12345678/terminate"
```

### Raise an event

For workflow components that support subscribing to external events, such as the Dapr Workflow engine, you can use the following “raise event” API to deliver a named event to a specific workflow instance.

```shell
curl -X POST "http://localhost:3500/v1.0/workflows/<workflowComponentName>/<instanceID>/raiseEvent/<eventName>"
```

> An `eventName` can be any function.

### Pause or resume a workflow

To plan for down-time, wait for inputs, and more, you can pause and then resume a workflow. To pause a workflow with an ID `12345678` until triggered to resume, run:

```shell
curl -X POST "http://localhost:3500/v1.0/workflows/dapr/12345678/pause"
```

To resume a workflow with an ID `12345678`, run:

```shell
curl -X POST "http://localhost:3500/v1.0/workflows/dapr/12345678/resume"
```

### Purge a workflow

The purge API can be used to permanently delete workflow metadata from the underlying state store, including any stored inputs, outputs, and workflow history records. This is often useful for implementing data retention policies and for freeing resources.

Only workflow instances in the COMPLETED, FAILED, or TERMINATED state can be purged. If the workflow is in any other state, calling purge returns an error.

```shell
curl -X POST "http://localhost:3500/v1.0/workflows/dapr/12345678/purge"
```

### Get information about a workflow

To fetch workflow information (outputs and inputs) with an ID `12345678`, run:

```shell
curl -X GET "http://localhost:3500/v1.0/workflows/dapr/12345678"
```

Next steps
----------

Now that you’ve learned how to manage workflows, learn how to execute workflows across multiple applications

[Multi Application Workflows>>](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-multi-app/)
Related links
-------------

*   [Try out the Workflow quickstart](https://docs.dapr.io/getting-started/quickstarts/workflow-quickstart/)
*   Try out the full SDK examples:
    *   [Python example](https://github.com/dapr/python-sdk/blob/master/examples/demo_workflow/app.py)
    *   [JavaScript example](https://github.com/dapr/js-sdk/tree/main/examples/workflow)
    *   [.NET example](https://github.com/dapr/dotnet-sdk/tree/master/examples/Workflow)
    *   [Java example](https://github.com/dapr/java-sdk/tree/master/examples/src/main/java/io/dapr/examples/workflows)
    *   [Go example](https://github.com/dapr/go-sdk/tree/main/examples/workflow)

Last modified March 3, 2026: [Merge pull request #5062 from JoshVanL/wf-versioning-cli-example (3b5020c)](https://github.com/dapr/docs/commit/3b5020cab259e29c3330b7215d10f7a6dd8ede4b)

*   [](https://www.youtube.com/@darpdev)
*   [](https://www.linkedin.com/company/daprdev/)
*   [](https://twitter.com/daprdev)
*   [](https://bsky.app/profile/daprdev.bsky.social)

*   [](https://github.com/dapr/)
*   [](https://bit.ly/dapr-discord)

© 2026 The Linux Foundation. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage](https://linuxfoundation.org/trademark-usage/) page.

![Image 1](https://static.scarf.sh/a.png?x-pxid=4848fb3b-3edb-4329-90a9-a9d79afff054)
