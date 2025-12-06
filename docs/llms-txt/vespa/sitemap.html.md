# Source: https://docs.vespa.ai/sitemap.html.md

# Table of contents

#### Vespa basics

- [Deploy an application](/en/basics/deploy-an-application.html)
- [Vespa applications](/en/basics/applications.html)
- [Schemas](/en/basics/schemas.html)
- [Writing](/en/basics/writing.html)
- [Querying](/en/basics/querying.html)
- [Ranking](/en/basics/ranking.html)
- [Operations](/en/basics/operations.html)
- [What's more](/en/basics/whats-more.html)

#### Learn more

- [Vespa overview](/en/learn/overview.html)
- [Getting help from LLMs](/en/llm-help.html)
- [Features](/en/learn/features.html)
- [Tutorials and use cases](/en/learn/tutorials/)
- [Frequently asked questions](/en/learn/faq.html)
- [Glossary](/en/learn/glossary.html)
- [Releases](/en/learn/releases.html)
- [Tenants, apps and instances](/en/learn/tenant-apps-instances.html)
- [Migrating to Vespa Cloud](/en/learn/migrating-to-cloud.html)
- [Migrating from ElasticSearch](/en/learn/migrating-from-elastic-search.html)
- [About this documentation](/en/learn/about-documentation.html)
- [Contributing to Vespa](/en/learn/contributing.html)

#### Applications and components

- [Developer guide](/en/applications/developer-guide.html)
- [IDE support](/en/applications/ide-support.html)
- [Deployment](/en/applications/deployment.html)
- [.vespaignore files](/en/applications/vespaignore.html)
- [Containers](/en/applications/containers.html)
- [Components](/en/applications/components.html)
- [Searchers](/en/applications/searchers.html)
- [Document processors](/en/applications/document-processors.html)
- [Request handlers](/en/applications/request-handlers.html)
- [Result renderers](/en/applications/result-renderers.html)
- [Dependency injection](/en/applications/dependency-injection.html)
- [Configuring components](/en/applications/configuring-components.html)
- [Chaining](/en/applications/chaining.html)
- [Inspecting structured data in a Searcher](/en/applications/inspecting-structured-data.html)
- [Developing web services](/en/applications/web-services.html)
- [Unit testing](/en/applications/unit-testing.html)
- [System testing](/en/applications/testing.html)
- [The config system](/en/applications/config-system.html)
- [Request-response processing](/en/applications/processing.html)
- [Bundles](/en/applications/bundles.html)
- [Using ZooKeeper](/en/applications/using-zookeeper.html)
- [Http servers and filters](/en/applications/http-servers-and-filters.html)
- [Using pluggable frameworks](/en/applications/pluggable-frameworks.html)
- [Java config API](/en/applications/configapi-dev.html)

#### Schemas and documents

- [Documents](/en/schemas/documents.html)
- [Inheritance in schemas](/en/schemas/inheritance-in-schemas.html)
- [Concrete document types](/en/schemas/concrete-documents.html)
- [Parent-child relationships](/en/schemas/parent-child.html)
- [Structs](/en/schemas/structs.html)
- [Predicate fields](/en/schemas/predicate-fields.html)
- [Exposing schema information](/en/schemas/exposing-schema-information.html)

#### Reading and writing

- [Reads and writes](/en/writing/reads-and-writes.html)
- [/document/v1](/en/writing/document-v1-api-guide.html)
- [Indexing](/en/writing/indexing.html)
- [Index bootstrap](/en/writing/initial-batch-feed.html)
- [Visiting](/en/writing/visiting.html)
- [Document API](/en/writing/document-api-guide.html)
- [Partial updates](/en/writing/partial-updates.html)
- [Batch delete](/en/writing/batch-delete.html)
- [Feed block](/en/writing/feed-block.html)
- [Document routing](/en/writing/document-routing.html)
- [Indexing paged vectors](/en/writing/indexing-paged-vectors.html)

#### Querying

- [The query api](/en/querying/query-api.html)
- [The YQL query language](/en/querying/query-language.html)
- [Grouping and aggregation](/en/querying/grouping.html)
- [Federation](/en/querying/federation.html)
- [Query profiles](/en/querying/query-profiles.html)
- [An intro to vector search](/en/querying/vector-search-intro.html)
- [Nearest neighbor search](/en/querying/nearest-neighbor-search.html)
- [Approximate nearest neighbor search](/en/querying/approximate-nn-hnsw.html)
- [Nearest neighbor search guide](/en/querying/nearest-neighbor-search-guide.html)
- [Text matching](/en/querying/text-matching.html)
- [Searching multivalue fields](/en/querying/searching-multivalue-fields.html)
- [Geo search](/en/querying/geo-search.html)
- [Document summaries](/en/querying/document-summaries.html)
- [Result diversity](/en/querying/result-diversity.html)
- [Page templates](/en/querying/page-templates.html)

#### Ranking and inference

- [Ranking introduction](/en/ranking/ranking-intro.html)
- [Ranking expressions and features](/en/ranking/ranking-expressions-features.html)
- [Multivalue query operators](/en/ranking/multivalue-query-operators.html)
- [Tensor user guide](/en/ranking/tensor-user-guide.html)
- [Tensor examples](/en/ranking/tensor-examples.html)
- [Phased ranking](/en/ranking/phased-ranking.html)
- [Using TensorFlow models](/en/ranking/tensorflow.html)
- [Using ONNX models](/en/ranking/onnx.html)
- [Using XGBoost models](/en/ranking/xgboost.html)
- [Using LightGBM models](/en/ranking/lightgbm.html)
- [Wand: Accelerated OR search](/en/ranking/wand.html)
- [The BM25 rank feature](/en/ranking/bm25.html)
- [The nativeRank rank feature](/en/ranking/nativerank.html)
- [Cross-encoder transformer ranking](/en/ranking/cross-encoders.html)
- [Searcher re-ranking](/en/ranking/reranking-in-searcher.html)
- [Significance model](/en/ranking/significance.html)
- [Stateless model evaluation](/en/ranking/stateless-model-evaluation.html)

#### RAG and embedding

- [RAG in Vespa](/en/rag/rag.html)
- [Working with chunks](/en/rag/working-with-chunks.html)
- [Embedding](/en/rag/embedding.html)
- [Binarizing vectors](/en/rag/binarizing-vectors.html)
- [LLMs in Vespa](/en/rag/llms-in-vespa.html)
- [Using local LLMs](/en/rag/local-llms.html)
- [Using external LLMs](/en/rag/external-llms.html)
- [Document enrichment with LLMs](/en/rag/document-enrichment.html)
- [Model hub](/en/rag/model-hub.html)

#### Linguistics and text processing

- [Linguistics](/en/linguistics/linguistics.html)
- [Lucene linguistics](/en/linguistics/lucene-linguistics.html)
- [Query rewriting](/en/linguistics/query-rewriting.html)
- [Troubleshooting character encoding](/en/linguistics/troubleshooting-encoding.html)

#### Content and elasticity

- [Content clusters](/en/content/proton.html)
- [Content nodes and states](/en/content/content-nodes.html)
- [Elasticity](/en/content/elasticity.html)
- [Document attributes](/en/content/attributes.html)
- [Consistency Model](/en/content/consistency.html)
- [Distribution algorithm](/en/content/idealstate.html)
- [Buckets](/en/content/buckets.html)

#### Performance

- [Performance overview](/en/performance/)
- [Practical performance guide](/en/performance/practical-search-performance-guide.html)
- [Serving sizing guide](/en/performance/sizing-search.html)
- [Feed sizing guide](/en/performance/sizing-feeding.html)
- [Node resources](/en/performance/node-resources.html)
- [Sizing examples](/en/performance/sizing-examples.html)
- [Topology and resizing](/en/performance/topology-and-resizing.html)
- [Streaming search](/en/performance/streaming-search.html)
- [Benchmarking](/en/performance/benchmarking.html)
- [Benchmarking using Vespa Cloud](/en/performance/benchmarking-cloud.html)
- [Memory visualizer](/en/performance/memory-visualizer.html)
- [Profiling](/en/performance/profiling.html)
- [Container tuning](/en/performance/container-tuning.html)
- [Rate-limiting queries](/en/performance/rate-limiting-searcher.html)
- [Graceful degradation](/en/performance/graceful-degradation.html)
- [Caches](/en/performance/caches-in-vespa.html)
- [HTTP performance testing](/en/performance/container-http.html)
- [HTTP/2](/en/performance/http2.html)
- [Feature tuning](/en/performance/feature-tuning.html)
- [Valgrind](/en/performance/valgrind.html)

#### Operations

- [Environments](/en/operations/environments.html)
- [Zones](/en/operations/zones.html)
- [Production deployment](/en/operations/production-deployment.html)
- [Deployment variants](/en/operations/deployment-variants.html)
- [Automated deployments](/en/operations/automated-deployments.html)
- [Autoscaling](/en/operations/autoscaling.html)
- Enclave: Bring your own cloud 
  - [Enclave](/en/operations/enclave/enclave.html)
  - [AWS getting started](/en/operations/enclave/aws-getting-started.html)
  - [AWS architecture](/en/operations/enclave/aws-architecture.html)
  - [Azure getting started](/en/operations/enclave/azure-getting-started.html)
  - [GCP getting started](/en/operations/enclave/gcp-getting-started.html)
  - [GCP architecture](/en/operations/enclave/gcp-architecture.html)
  - [Log archive](/en/operations/enclave/archive.html)
  - [Operations](/en/operations/enclave/operations.html)

- [Reindexing](/en/operations/reindexing.html)
- [Data management and backup](/en/operations/data-management.html)
- [Cloning applications and data](/en/operations/cloning.html)
- [Monitoring](/en/operations/monitoring.html)
- [Metrics](/en/operations/metrics.html)
- [Notifications](/en/operations/notifications.html)
- [Deployment patterns](/en/operations/deployment-patterns.html)
- [Private endpoints](/en/operations/private-endpoints.html)
- [Endpoint routing](/en/operations/endpoint-routing.html)
- [Access logging](/en/operations/access-logging.html)
- Artefact archive 
  - [Archive guide](/en/operations/archive/archive-guide.html)
  - [Archive Guide AWS](/en/operations/archive/archive-guide-aws.html)
  - [Archive Guide GCP](/en/operations/archive/archive-guide-gcp.html)

- [Deleting applications](/en/operations/deleting-applications.html)
- Self-managed 
  - [Admin procedures](/en/operations/self-managed/admin-procedures.html)
  - [Multinode Systems](/en/operations/self-managed/multinode-systems.html)
  - [Files, Processes, Ports, Environment](/en/operations/self-managed/files-processes-and-ports.html)
  - [Node Setup](/en/operations/self-managed/node-setup.html)
  - [Using Kubernetes](/en/operations/self-managed/using-kubernetes-with-vespa.html)
  - [Build and install](/en/operations/self-managed/build-install.html)
  - [Monitoring](/en/operations/self-managed/monitoring.html)
  - [Content node recovery](/en/operations/self-managed/content-node-recovery.html)
  - [Configuration Servers](/en/operations/self-managed/configuration-server.html)
  - [Live Vespa upgrade procedure](/en/operations/self-managed/live-upgrade.html)
  - [Config Sentinel](/en/operations/self-managed/config-sentinel.html)
  - [Config Proxy](/en/operations/self-managed/config-proxy.html)
  - [Docker Containers](/en/operations/self-managed/docker-containers.html)
  - [Docker Containers GPU setup](/en/operations/self-managed/vespa-gpu-container.html)
  - [CPU Support](/en/operations/self-managed/cpu-support.html)
  - [Service Location Broker](/en/operations/self-managed/slobrok.html)
  - [Change from attribute to index procedure](/en/operations/self-managed/procedure-change-attribute-index.html)
  - [Container](/en/operations/self-managed/container.html)
  - [Monitoring](/en/operations/self-managed/monitoring.html)

#### Security

- [Security overview](/en/security/security.html)
- [Security Guide](/en/security/guide.html)
- [Secret Store](/en/security/secret-store.html)
- [Cloudflare Workers](/en/security/cloudflare-workers.html)
- [Security Whitepaper](/en/security/whitepaper.html)
- [Securing a Vespa installation](/en/security/securing-your-vespa-installation.html)
- [mTLS](/en/security/mtls.html)

#### Clients

- [Command line client (Vespa CLI)](/en/clients/vespa-cli.html)
- [Python client (pyVespa)](https://vespa-engine.github.io/pyvespa/)
- [Java feed client](/en/clients/vespa-feed-client.html)
- [HTTP best practices](/en/clients/http-best-practices.html)

#### Modules

- E-commerce 
  - [Multi-currency filtering](/en/modules/e-commerce/multi-currency-filtering.html)

#### Reference

- APIs 
  - [APIs overview](/en/reference/api/api.html)
  - [The query API](/en/reference/api/query.html)
  - [/document/v1 API](/en/reference/api/document-v1.html)
  - [/state/v1 API](/en/reference/api/state-v1.html)
  - [/application/v2 API (deployment)](/en/reference/api/deploy-v2.html)
  - [/application/v2/tenant API](/en/reference/api/application-v2.html)
  - [/config/v2 API](/en/reference/api/config-v2.html)
  - [/cluster/v2 API](/en/reference/api/cluster-v2.html)
  - [/metrics/v1 API](/en/reference/api/metrics-v1.html)
  - [/metrics/v2 API](/en/reference/api/metrics-v2.html)
  - [/prometheus/v1 API](/en/reference/api/prometheus-v1.html)

- Applications and components 
  - [Application packages](/en/reference/applications/application-packages.html)
  - services.xml 
    - [services.xml](/en/reference/applications/services/services.html)
    - [services.xml - admin](/en/reference/applications/services/admin.html)
    - [services.xml - container](/en/reference/applications/services/container.html)
    - [services.xml - content](/en/reference/applications/services/content.html)
    - [services.xml - docproc](/en/reference/applications/services/docproc.html)
    - [services.xml - http](/en/reference/applications/services/http.html)
    - [services.xml - processing](/en/reference/applications/services/processing.html)
    - [services.xml - search](/en/reference/applications/services/search.html)

  - [deployment.xml](/en/reference/applications/deployment.html)
  - [hosts.xml](/en/reference/applications/hosts.html)
  - [validation-overrides.xml](/en/reference/applications/validation-overrides.html)
  - [Components](/en/reference/applications/components.html)
  - [Configuration files](/en/reference/applications/config-files.html)
  - [System test](/en/reference/applications/testing.html)
  - [System test (Java)](/en/reference/applications/testing-java.html)

- Schemas and documents 
  - [Schemas](/en/reference/schemas/schemas.html)
  - [Document JSON format](/en/reference/schemas/document-json-format.html)
  - [Document field path language](/en/reference/schemas/document-field-path.html)

- Reading and writing 
  - [Indexing language](/en/reference/writing/indexing-language.html)
  - [Document selector language](/en/reference/writing/document-selector-language.html)

- Querying 
  - [The YQL query language](/en/reference/querying/yql.html)
  - [The simple query language](/en/reference/querying/simple-query-language.html)
  - [Select](/en/reference/querying/json-query-language.html)
  - [Grouping](/en/reference/querying/grouping-language.html)
  - [Sorting](/en/reference/querying/sorting-language.html)
  - [Query profiles](/en/reference/querying/query-profiles.html)
  - [Semantic rules](/en/reference/querying/semantic-rules.html)
  - [The default result format](/en/reference/querying/default-result-format.html)
  - [The page result format](/en/reference/querying/page-result-format.html)
  - [Page templates](/en/reference/querying/page-templates.html)

- Ranking and inference 
  - [Ranking expressions](/en/reference/ranking/ranking-expressions.html)
  - [Tensor evaluation](/en/reference/ranking/tensor.html)
  - [Rank features](/en/reference/ranking/rank-features.html)
  - [nativeRank](/en/reference/ranking/nativerank.html)
  - [String segment match](/en/reference/ranking/string-segment-match.html)
  - [Rank feature configuration](/en/reference/ranking/rank-feature-configuration.html)
  - [Rank types](/en/reference/ranking/rank-types.html)
  - [Model files](/en/reference/ranking/model-files.html)
  - [Constant tensors](/en/reference/ranking/constant-tensor-json-format.html)

- RAG and embedding 
  - [Chunking](/en/reference/rag/chunking.html)
  - [Embedding](/en/reference/rag/embedding.html)

- Operations 
  - [Health checks](/en/reference/operations/health-checks.html)
  - [Log files](/en/reference/operations/log-files.html)
  - [Tools](/en/reference/operations/tools.html)
  - Metrics 
    - [Metrics](/en/reference/operations/metrics/metrics.html)
    - [Default metric set](/en/reference/operations/metrics/default-metric-set.html)
    - [Vespa metric set](/en/reference/operations/metrics/vespa-metric-set.html)
    - [Metric units](/en/reference/operations/metrics/metric-units.html)
    - [Container metrics](/en/reference/operations/metrics/container.html)
    - [Distributor metrics](/en/reference/operations/metrics/distributor.html)
    - [Search node metrics](/en/reference/operations/metrics/searchnode.html)
    - [Storage metrics](/en/reference/operations/metrics/storage.html)
    - [Configserver metrics](/en/reference/operations/metrics/configserver.html)
    - [Logd metrics](/en/reference/operations/metrics/logd.html)
    - [Node Admin metrics](/en/reference/operations/metrics/nodeadmin.html)
    - [Slobrok metrics](/en/reference/operations/metrics/slobrok.html)
    - [Cluster controller metrics](/en/reference/operations/metrics/clustercontroller.html)
    - [Sentinel metrics](/en/reference/operations/metrics/sentinel.html)

  - Self-managed 
    - [Tools](/en/reference/operations/self-managed/tools.html)

- Security 
  - [Mtls](/en/reference/security/mtls.html)

- Clients 
  - Vespa CLI 
    - [vespa](/en/reference/clients/vespa-cli/vespa.html)
    - [vespa activate](/en/reference/clients/vespa-cli/vespa_activate.html)
    - [vespa auth](/en/reference/clients/vespa-cli/vespa_auth.html)
    - [vespa clone](/en/reference/clients/vespa-cli/vespa_clone.html)
    - [vespa config](/en/reference/clients/vespa-cli/vespa_config.html)
    - [vespa curl](/en/reference/clients/vespa-cli/vespa_curl.html)
    - [vespa deploy](/en/reference/clients/vespa-cli/vespa_deploy.html)
    - [vespa destroy](/en/reference/clients/vespa-cli/vespa_destroy.html)
    - [vespa document](/en/reference/clients/vespa-cli/vespa_document.html)
    - [vespa feed](/en/reference/clients/vespa-cli/vespa_feed.html)
    - [vespa fetch](/en/reference/clients/vespa-cli/vespa_fetch.html)
    - [vespa inspect](/en/reference/clients/vespa-cli/vespa_inspect.html)
    - [vespa log](/en/reference/clients/vespa-cli/vespa_log.html)
    - [vespa prepare](/en/reference/clients/vespa-cli/vespa_prepare.html)
    - [vespa prod](/en/reference/clients/vespa-cli/vespa_prod.html)
    - [vespa query](/en/reference/clients/vespa-cli/vespa_query.html)
    - [vespa status](/en/reference/clients/vespa-cli/vespa_status.html)
    - [vespa test](/en/reference/clients/vespa-cli/vespa_test.html)
    - [vespa version](/en/reference/clients/vespa-cli/vespa_version.html)
    - [vespa visit](/en/reference/clients/vespa-cli/vespa_visit.html)

- Release notes 
  - [Vespa 7](/en/reference/release-notes/vespa7.html)
  - [Vespa 8](/en/reference/release-notes/vespa8.html)
  - [Vespa 9 (upcoming)](/en/reference/release-notes/vespa9.html)

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [Table of contents](#)

