# Source: https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/

Title: Workflow architecture

URL Source: https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/

Markdown Content:
Workflow architecture | Dapr Docs
===============
[Dapr Docs](https://docs.dapr.io/)

*   [Homepage](https://dapr.io/)
*   [GitHub](https://github.com/dapr)
*   [Blog](https://blog.dapr.io/posts)
*   [Discord](https://bit.ly/dapr-discord)
*   [Community](https://dapr.io/community)
*   
[v1.17 (latest)](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#)
    *   [v1.18 (preview)](https://v1-18.docs.dapr.io/)
    *   [v1.17 (latest)](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#)
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
[English](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#)
    *   [简体中文](https://docs.dapr.io/zh-hans/developing-applications/building-blocks/workflow/workflow-architecture/)

Search

[English](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#)
*   [简体中文](https://docs.dapr.io/zh-hans/developing-applications/building-blocks/workflow/workflow-architecture/)

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

[Edit this page](https://github.com/dapr/docs/edit/v1.17//daprdocs/content/en/developing-applications/building-blocks/workflow/workflow-architecture.md)[Create documentation issue](https://github.com/dapr/docs/issues/new/choose)[Create project issue](https://github.com/dapr/dapr/issues/new/choose)[Print entire section](https://docs.dapr.io/developing-applications/building-blocks/workflow/_print/)

*   [Sidecar interactions](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#sidecar-interactions)
    *   [Differences between workflow and application actor interactions](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#differences-between-workflow-and-application-actor-interactions)

*   [Workflow distributed tracing](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#workflow-distributed-tracing)
*   [Workflow actors](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#workflow-actors)

    *   [Supported State Stores](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#supported-state-stores)

*   [Workflow scalability](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#workflow-scalability)
*   [Workflow latency](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#workflow-latency)
*   [Increasing scheduling throughput](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#increasing-scheduling-throughput)
*   [Workflows cluster deployment when using Dapr Shared with workflow](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#workflows-cluster-deployment-when-using-dapr-shared-with-workflow)
*   [Next steps](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#next-steps)
*   [Related links](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#related-links)

1.   [Developing applications](https://docs.dapr.io/developing-applications/)
2.   [Building blocks](https://docs.dapr.io/developing-applications/building-blocks/)
3.   [Workflow](https://docs.dapr.io/developing-applications/building-blocks/workflow/)
4.   Workflow architecture

Workflow architecture
=====================

The Dapr Workflow engine architecture

[Dapr Workflows](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-overview/) allow developers to define workflows using ordinary code in a variety of programming languages. The workflow engine runs inside of the Dapr sidecar and orchestrates workflow code deployed as part of your application. Dapr Workflows are built on top of Dapr Actors providing durability and scalability for workflow execution.

This article describes:

*   The architecture of the Dapr Workflow engine
*   How the workflow engine interacts with application code
*   How the workflow engine fits into the overall Dapr architecture
*   How different workflow backends can work with workflow engine

For more information on how to author Dapr Workflows in your application, see [How to: Author a workflow](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-overview/).

The Dapr Workflow engine is internally powered by Dapr’s actor runtime. The following diagram illustrates the Dapr Workflow architecture in Kubernetes mode:

![Image 6: Diagram showing how the workflow architecture works in Kubernetes mode](https://docs.dapr.io/images/workflow-overview/workflows-architecture-k8s.png)
To use the Dapr Workflow building block, you write workflow code in your application using the Dapr Workflow SDK, which internally connects to the sidecar using a gRPC stream. This registers the workflow and any workflow activities, or tasks that workflows can schedule.

The engine is embedded directly into the sidecar and implemented using the [`durabletask-go`](https://github.com/dapr/durabletask-go) framework library. This framework allows you to swap out different storage providers, including a storage provider created for Dapr that leverages internal actors behind the scenes. Since Dapr Workflows use actors, you can store workflow state in state stores.

Sidecar interactions
--------------------

When a workflow application starts up, it uses a workflow authoring SDK to send a gRPC request to the Dapr sidecar and get back a stream of workflow work items, following the [server streaming RPC pattern](https://grpc.io/docs/what-is-grpc/core-concepts/#server-streaming-rpc). These work items can be anything from “start a new X workflow” (where X is the type of a workflow) to “schedule activity Y with input Z to run on behalf of workflow X”.

The workflow app executes the appropriate workflow code and then sends a gRPC request back to the sidecar with the execution results.

![Image 7: Dapr Workflow Engine Protocol](https://docs.dapr.io/images/workflow-overview/workflow-engine-protocol.png)
All interactions happen over a single gRPC channel and are initiated by the application, which means the application doesn’t need to open any inbound ports. The details of these interactions are internally handled by the language-specific Dapr Workflow authoring SDK.

### Differences between workflow and application actor interactions

If you’re familiar with Dapr actors, you may notice a few differences in terms of how sidecar interactions works for workflows compared to application defined actors.

| Actors | Workflows |
| --- | --- |
| Actors created by the application can interact with the sidecar using either HTTP or gRPC. | Workflows only use gRPC. Due to the workflow gRPC protocol’s complexity, an SDK is _required_ when implementing workflows. |
| Actor operations are pushed to application code from the sidecar. This requires the application to listen on a particular _app port_. | For workflows, operations are _pulled_ from the sidecar by the application using a streaming protocol. The application doesn’t need to listen on any ports to run workflows. |
| Actors explicitly register themselves with the sidecar. | Workflows do not register themselves with the sidecar. The embedded engine doesn’t keep track of workflow types. This responsibility is instead delegated to the workflow application and its SDK. |

Workflow distributed tracing
----------------------------

The [`durabletask-go`](https://github.com/dapr/durabletask-go) core used by the workflow engine writes distributed traces using Open Telemetry SDKs. These traces are captured automatically by the Dapr sidecar and exported to the configured Open Telemetry provider, such as Zipkin.

Each workflow instance managed by the engine is represented as one or more spans. There is a single parent span representing the full workflow execution and child spans for the various tasks, including spans for activity task execution and durable timers.

> Workflow activity code currently **does not** have access to the trace context.

Workflow actors
---------------

Upon the workflow client connecting to the sidecar, there are two types of actors that are registered in support of the workflow engine:

*   `dapr.internal.{namespace}.{appID}.workflow`
*   `dapr.internal.{namespace}.{appID}.activity`

The `{namespace}` value is the Dapr namespace and defaults to `default` if no namespace is configured. The `{appID}` value is the app’s ID. For example, if you have a workflow app named “wfapp”, then the type of the workflow actor would be `dapr.internal.default.wfapp.workflow` and the type of the activity actor would be `dapr.internal.default.wfapp.activity`.

The following diagram demonstrates how workflow actors operate in a Kubernetes scenario:

![Image 8: Diagram demonstrating internally registered actors across a cluster](https://docs.dapr.io/images/workflow-overview/workflow-execution.png)
Just like user-defined actors, workflow actors are distributed across the cluster by the hashing lookup table provided by the actor placement service. They also maintain their own state and make use of reminders. However, unlike actors that live in application code, these workflow actors are embedded into the Dapr sidecar. Application code is completely unaware that these actors exist.

#### Note

The workflow actor types are only registered after an app has registered a workflow using a Dapr Workflow SDK. If an app never registers a workflow, then the internal workflow actors are never registered.

### Workflow actors

There are 2 different types of actors used with workflows: workflow actors and activity actors. Workflow actors are responsible for managing the state and placement of all workflows running in the app. A new instance of the workflow actor is activated for every workflow instance that gets scheduled. The ID of the workflow actor is the ID of the workflow. This workflow actor stores the state of the workflow as it progresses, and determines the node on which the workflow code executes via the actor lookup table.

As workflows are based on actors, all workflow and activity work is randomly distributed across all replicas of the application implementing workflows. There is no locality or relationship between where a workflow is started and where each work item is executed.

Each workflow actor saves its state using the following keys in the configured actor state store:

| Key | Description |
| --- | --- |
| `inbox-NNNNNN` | A workflow’s inbox is effectively a FIFO queue of _messages_ that drive a workflow’s execution. Example messages include workflow creation messages, activity task completion messages, etc. Each message is stored in its own key in the state store with the name `inbox-NNNNNN` where `NNNNNN` is a 6-digit number indicating the ordering of the messages. These state keys are removed once the corresponding messages are consumed by the workflow. |
| `history-NNNNNN` | A workflow’s history is an ordered list of events that represent a workflow’s execution history. Each key in the history holds the data for a single history event. Like an append-only log, workflow history events are only added and never removed (except when a workflow performs a “continue as new” operation, which purges all history and restarts a workflow with a new input). |
| `customStatus` | Contains a user-defined workflow status value. There is exactly one `customStatus` key for each workflow actor instance. |
| `metadata` | Contains meta information about the workflow as a JSON blob and includes details such as the length of the inbox, the length of the history, and a 64-bit integer representing the workflow generation (for cases where the instance ID gets reused). The length information is used to determine which keys need to be read or written to when loading or saving workflow state updates. |

#### Warning

```
Workflow actor state remains in the state store even after a workflow has completed.
```

Creating a large number of workflows could result in unbounded storage usage. To address this either purge workflows using their ID or directly delete entries in the workflow DB store.

The following diagram illustrates the typical lifecycle of a workflow actor.

![Image 9: Dapr Workflow Actor Flowchart](https://docs.dapr.io/images/workflow-overview/workflow-actor-flowchart.png)
To summarize:

1.   A workflow actor is activated when it receives a new message.
2.   New messages then trigger the associated workflow code (in your application) to run and return an execution result back to the workflow actor.
3.   Once the result is received, the actor schedules any tasks as necessary.
4.   After scheduling, the actor updates its state in the state store.
5.   Finally, the actor goes idle until it receives another message. During this idle time, the sidecar may decide to unload the workflow actor from memory.

### Activity actors

Activity actors are responsible for managing the state and placement of all workflow activity invocations. A new instance of the activity actor is activated for every activity task that gets scheduled by a workflow. The ID of the activity actor is the ID of the workflow combined with a sequence number (sequence numbers start with 0), as well as the “generation” (incremented during instances of rerunning from using `continue as new`). For example, if a workflow has an ID of `876bf371` and is the third activity to be scheduled by the workflow, it’s ID will be `876bf371::2::1` where `2` is the sequence number, and `1` is the generation. If the activity is scheduled again after a `continue as new`, the ID will be `876bf371::2::2`.

No state is stored by activity actors, and instead all resulting data is sent back to the parent workflow actor.

The following diagram illustrates the typical lifecycle of an activity actor.

![Image 10: Workflow Activity Actor Flowchart](https://docs.dapr.io/images/workflow-overview/workflow-activity-actor-flowchart.png)
Activity actors are short-lived:

1.   Activity actors are activated when a workflow actor schedules an activity task.
2.   Activity actors then immediately call into the workflow application to invoke the associated activity code.
3.   Once the activity code has finished running and has returned its result, the activity actor sends a message to the parent workflow actor with the execution results.
4.   The activity actor then deactivates itself.
5.   Once the results are sent, the workflow is triggered to move forward to its next step.

### Reminder usage and execution guarantees

The Dapr Workflow ensures workflow fault-tolerance by using [actor reminders](https://docs.dapr.io/developing-applications/building-blocks/actors/actors-timers-reminders/#%23actor-reminders) to recover from transient system failures. Prior to invoking application workflow code, the workflow or activity actor will create a new reminder. These reminders are made “one shot”, meaning that they will expire after successful triggering. If the application code executes without interruption, the reminder is triggered and expired. However, if the node or the sidecar hosting the associated workflow or activity crashes, the reminder will reactivate the corresponding actor and the execution will be retried, forever.

![Image 11: Diagram showing the process of invoking workflow actors](https://docs.dapr.io/images/workflow-overview/workflow-actor-reminder-flow.png)
### State store usage

Dapr Workflows use actors internally to drive the execution of workflows. Like any actors, these workflow actors store their state in the configured actor state store. This is done by specifying a state store component in your Dapr configuration and then referencing that state store in the `actorStateStore` property of the configuration’s `actors` section. Read the [state API reference](https://docs.dapr.io/reference/api/state_api/) and the [actors API reference](https://docs.dapr.io/reference/api/actors_api/) to learn more about state stores for actors.

Any state store that supports actors implicitly supports Dapr Workflow.
As discussed in the [workflow actors](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#workflow-actors) section, workflows save their state incrementally by appending to a history log. The history log for a workflow is distributed across multiple state store keys so that each “checkpoint” only needs to append the newest entries.

The size of each checkpoint is determined by the number of concurrent actions scheduled by the workflow before it goes into an idle state. [Sequential workflows](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-overview/#task-chaining) will therefore make smaller batch updates to the state store, while [fan-out/fan-in workflows](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-overview/#fan-outfan-in) will require larger batches. The size of the batch is also impacted by the size of inputs and outputs when workflows [invoke activities](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#workflow-activities) or [child workflows](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#child-workflows).

![Image 12: Diagram of workflow actor state store interactions](https://docs.dapr.io/images/workflow-overview/workflow-state-store-interactions.png)
Different state store implementations may implicitly put restrictions on the types of workflows you can author. For example, the Azure Cosmos DB state store limits item sizes to 2 MB of UTF-8 encoded JSON ([source](https://learn.microsoft.com/azure/cosmos-db/concepts-limits#per-item-limits)). The input or output payload of an activity or child workflow is stored as a single record in the state store, so a item limit of 2 MB means that workflow and activity inputs and outputs can’t exceed 2 MB of JSON-serialized data.

Similarly, if a state store imposes restrictions on the size of a batch transaction, that may limit the number of parallel actions that can be scheduled by a workflow.

Workflow state can be purged from a state store, including all its history. Each Dapr SDK exposes APIs for purging all metadata related to specific workflow instances.

#### State store record count

The number of records which are saved as history in the state store per workflow run is determined by its complexity or “shape”. In other words, the number of activities, timers, sub-workflows etc. The following table shows a general guide to the number of records that are saved by different workflow tasks. This number may be larger or smaller depending on retries or concurrency.

| Task type | Number of records saved |
| --- | --- |
| Start workflow | 5 records |
| Call activity | 3 records |
| Timer | 3 records |
| Raise event | 3 records |
| Start child workflow | 8 records |

#### Query Workflow History

```bash
dapr workflow --app-id myapp list
dapr workflow --app-id myapp history <instance-id>
```

### Supported State Stores

The workflow engine supports these state stores:

*   PostgreSQL
*   MySQL
*   SQL Server
*   SQLite
*   Oracle Database
*   CockroachDB
*   MongoDB
*   Redis

Workflow scalability
--------------------

Because Dapr Workflows are internally implemented using actors, Dapr Workflows have the same scalability characteristics as actors. The placement service:

*   Doesn’t distinguish between workflow actors and actors you define in your application
*   Will load balance workflows using the same algorithms that it uses for actors

The expected scalability of a workflow is determined by the following factors:

*   The number of machines used to host your workflow application
*   The CPU and memory resources available on the machines running workflows
*   The scalability of the state store configured for actors
*   The scalability of the actor placement service and the reminder subsystem

The implementation details of the workflow code in the target application also plays a role in the scalability of individual workflow instances. Each workflow instance executes on a single node at a time, but a workflow can schedule activities and child workflows which run on other nodes.

Workflows can also schedule these activities and child workflows to run in parallel, allowing a single workflow to potentially distribute compute tasks across all available nodes in the cluster.

You can configure the maximum concurrency of workflows and activities using the [Dapr configuration](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-concurrency/) as described in the next section.

#### Important

By default, there are no global limits imposed on workflow and activity concurrency. A runaway workflow could therefore potentially consume all resources in a cluster if it attempts to schedule too many tasks in parallel. Use care when authoring Dapr Workflows that schedule large batches of work in parallel.

#### Important

The Dapr Workflow engine requires that all instances of a workflow app register the exact same set of workflows and activities. In other words, it’s not possible to scale certain workflows or activities independently. All workflows and activities within an app must be scaled together.

Workflows don’t control the specifics of how load is distributed across the cluster. For example, if a workflow schedules 10 activity tasks to run in parallel, all 10 tasks may run on as many as 10 different compute nodes or as few as a single compute node. The actual scale behavior is determined by the actor placement service, which manages the distribution of the actors that represent each of the workflow’s tasks.

![Image 13: Diagram of workflow and activity actors scaled out across multiple Dapr instances](https://docs.dapr.io/images/workflow-overview/workflow-actor-scale-out.png)
Workflow latency
----------------

In order to provide guarantees around durability and resiliency, Dapr Workflows frequently write to the state store and rely on reminders to drive execution. Dapr Workflows therefore may not be appropriate for latency-sensitive workloads. Expected sources of high latency include:

*   Latency from the state store when persisting workflow state.
*   Latency from the state store when rehydrating workflows with large histories.
*   Latency caused by too many active reminders in the cluster.
*   Latency caused by high CPU usage in the cluster.

See the [Reminder usage and execution guarantees section](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#reminder-usage-and-execution-guarantees) for more details on how the design of workflow actors may impact execution latency.

Increasing scheduling throughput
--------------------------------

By default, when a client schedules a workflow, the workflow engine waits for the workflow to be fully started before returning a response to the client. Waiting for the workflow to start before returning can decrease the scheduling throughput of workflows. When scheduling a workflow with a start time, the workflow engine does not wait for the workflow to start before returning a response to the client. To increase scheduling throughput, consider adding a start time of “now” when scheduling a workflow. An example of scheduling a workflow with a start time of “now” in the Go SDK is shown below:

```go
client.ScheduleNewWorkflow(ctx, "MyCoolWorkflow", workflow.WithStartTime(time.Now()))
```

Workflows cluster deployment when using Dapr Shared with workflow
-----------------------------------------------------------------

#### Note

The following feature is only available when the [Workflows Clustered Deployment preview feature is enabled](https://docs.dapr.io/operations/configuration/preview-features/).

When using [Dapr Shared](https://docs.dapr.io/operations/hosting/kubernetes/kubernetes-dapr-shared/), it can be the case that there are multiple daprd sidecars running behind a single load balancer or service. As such, the instance to which a worker receiving work, may not be the same instance that receives the work result. Dapr creates a third actor type to handle this scenario: `dapr.internal.{namespace}.{appID}.executor` to handle routing of the worker results back to the correct workflow actor to ensure correct operation.

Next steps
----------

[Author workflows >>](https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-author-workflow/)
Related links
-------------

*   [Workflow overview](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-overview/)
*   [Workflow API reference](https://docs.dapr.io/reference/api/workflow_api/)
*   [Try out the Workflow quickstart](https://docs.dapr.io/getting-started/quickstarts/workflow-quickstart/)
*   Try out the following examples:
    *   [Python](https://github.com/dapr/python-sdk/tree/master/examples/demo_workflow)
    *   [JavaScript example](https://github.com/dapr/js-sdk/tree/main/examples/workflow)
    *   [.NET](https://github.com/dapr/dotnet-sdk/tree/master/examples/Workflow)
    *   [Java](https://github.com/dapr/java-sdk/tree/master/examples/src/main/java/io/dapr/examples/workflows)
    *   [Go example](https://github.com/dapr/go-sdk/tree/main/examples/workflow/README.md)

Last modified March 3, 2026: [Merge pull request #5062 from JoshVanL/wf-versioning-cli-example (3b5020c)](https://github.com/dapr/docs/commit/3b5020cab259e29c3330b7215d10f7a6dd8ede4b)

*   [](https://www.youtube.com/@darpdev)
*   [](https://www.linkedin.com/company/daprdev/)
*   [](https://twitter.com/daprdev)
*   [](https://bsky.app/profile/daprdev.bsky.social)

*   [](https://github.com/dapr/)
*   [](https://bit.ly/dapr-discord)

© 2026 The Linux Foundation. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage](https://linuxfoundation.org/trademark-usage/) page.

![Image 14](https://static.scarf.sh/a.png?x-pxid=4848fb3b-3edb-4329-90a9-a9d79afff054)
