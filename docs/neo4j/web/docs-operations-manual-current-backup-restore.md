# Source: https://neo4j.com/docs/operations-manual/current/backup-restore/

Title: Backup and restore - Operations Manual

URL Source: https://neo4j.com/docs/operations-manual/current/backup-restore/

Markdown Content:
Backup and restore - Operations Manual
===============

This website uses cookies

We use cookies to offer you a better browsing experience, analyze site traffic, personalize content and serve targeted ads. Learn about how we use cookies and how you can control them in [Cookie Settings](https://neo4j.com/neo4j-cookie-and-tracking-policy/). By using our site. you consent to our use of cookies.

[Accept Cookies](https://neo4j.com/docs/operations-manual/current/backup-restore/#)[Use necessary cookies only](https://neo4j.com/docs/operations-manual/current/backup-restore/#)

[![Image 1: Neo4j Operations manual](https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg)](https://neo4j.com/)[Docs](https://neo4j.com/docs/)

[Docs](https://neo4j.com/docs/)

Neo4j DBMS
*   [Getting Started](https://neo4j.com/docs/getting-started/current/)
*   [Operations](https://neo4j.com/docs/operations-manual/current/)
*   [Migration and Upgrade](https://neo4j.com/docs/migration-guide/current/)
*   [Status Codes](https://neo4j.com/docs/status-codes/current/)
*   [Java Reference](https://neo4j.com/docs/java-reference/current/)
*   [Kerberos Add-on](https://neo4j.com/docs/kerberos-add-on/current/)

[Neo4j Aura](https://neo4j.com/docs/aura/)

Neo4j Tools
*   [Neo4j Bloom](https://neo4j.com/docs/bloom-user-guide/current/)
*   [Neo4j Browser](https://neo4j.com/docs/browser/)
*   [Neo4j Data Importer](https://neo4j.com/docs/data-importer/current/)
*   [Neo4j Desktop](https://neo4j.com/docs/desktop-manual/current/)
*   [Neo4j Ops Manager](https://neo4j.com/docs/ops-manager/current/)
*   [Neodash commercial](https://neo4j.com/docs/neodash-commercial/current/)

Neo4j Graph Data Science
*   [Neo4j Graph Data Science Library](https://neo4j.com/docs/graph-data-science/current/)
*   [Neo4j Graph Data Science Client](https://neo4j.com/docs/graph-data-science-client/current/)

Cypher Query Language
*   [Cypher](https://neo4j.com/docs/cypher-manual/current/)
*   [Cypher Cheat Sheet](https://neo4j.com/docs/cypher-cheat-sheet/current/)
*   [APOC Library](https://neo4j.com/docs/apoc/current/)

Generative AI
*   [Neo4j GraphRAG for Python](https://neo4j.com/docs/neo4j-graphrag-python/current/)
*   [Embeddings and vector indexes tutorial](https://neo4j.com/docs/genai/tutorials/embeddings-vector-indexes/)
*   [GenAI integrations](https://neo4j.com/docs/cypher-manual/current/genai-integrations/)
*   [Vector search indexes](https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/)
*   [Vector search functions](https://neo4j.com/docs/cypher-manual/current/functions/vector/)
*   [GraphQL vector index search documentation](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_vector_index_search)

Create applications
*   [Python Driver](https://neo4j.com/docs/python-manual/current/)
*   [Go Driver](https://neo4j.com/docs/go-manual/current/)
*   [Java Driver](https://neo4j.com/docs/java-manual/current/)
*   [JDBC Driver](https://neo4j.com/docs/jdbc-manual/current/)
*   [JavaScript Driver](https://neo4j.com/docs/javascript-manual/current/)
*   [.Net Driver](https://neo4j.com/docs/dotnet-manual/current/)
*   [Neo4j GraphQL Library](https://neo4j.com/docs/graphql-manual/current/)
*   [Neo4j Visualization Library](https://neo4j.com/docs/nvl/current/)
*   [OGM Library](https://neo4j.com/docs/ogm-manual/current/)
*   [Spring Data Neo4j](https://docs.spring.io/spring-data/neo4j/docs/current/reference/html/#reference)
*   [HTTP API](https://neo4j.com/docs/http-api/current/)
*   [Neo4j Query API](https://neo4j.com/docs/query-api/current/)
*   [Bolt](https://neo4j.com/docs/bolt/current/)

Connect data sources
*   [Neo4j Connector for Apache Spark](https://neo4j.com/docs/spark/current/)
*   [Neo4j Connector for Apache Kafka](https://neo4j.com/docs/kafka/)
*   [Change Data Capture (CDC)](https://neo4j.com/docs/cdc/)
*   [BigQuery to Neo4j](https://neo4j.com/docs/dataflow-bigquery/)
*   [Google Cloud to Neo4j](https://neo4j.com/docs/dataflow-google-cloud/)

[Labs](https://neo4j.com/labs/)

[GenAI Ecosystem](https://neo4j.com/labs/genai-ecosystem/)
*   [LLM Knowledge Graph Builder](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/)
*   [Vector Index & Search](https://neo4j.com/labs/genai-ecosystem/vector-search/)
*   [LangChain](https://neo4j.com/labs/genai-ecosystem/langchain/)
*   [LangChain.js](https://neo4j.com/labs/genai-ecosystem/langchain-js/)
*   [LlamaIndex](https://neo4j.com/labs/genai-ecosystem/llamaindex/)
*   [Haystack](https://neo4j.com/labs/genai-ecosystem/haystack/)
*   [DSPy](https://neo4j.com/labs/genai-ecosystem/dspy/)

**Developer Tools**
*   [APOC Extended](https://neo4j.com/labs/apoc/)
*   [Aura CLI](https://neo4j.com/labs/aura-cli/)
*   [arrows.app](https://neo4j.com/labs/arrows/)
*   [Cypher Workbench](https://neo4j.com/labs/cypher-workbench/)
*   [ETL Tool](https://neo4j.com/labs/etl-tool/)
*   [NeoDash](https://neo4j.com/labs/neodash/)

**Frameworks & Integrations**
*   [Needle Starter Kit](https://neo4j.com/labs/neo4j-needle-starterkit/)
*   [Neo4j Plugin for Liquibase](https://neo4j.com/labs/liquibase/)
*   [Neo4j Migrations](https://neo4j.com/labs/neo4j-migrations/)
*   [neomodel](https://neo4j.com/labs/neomodel/)

[RDF & Linked Data](https://neo4j.com/labs/neosemantics/)
*   [Neosemantics (Java)](https://neo4j.com/labs/neosemantics/)
*   [RDFLib-Neo4j (Python)](https://neo4j.com/labs/rdflib-neo4j/)

[Get Help](https://neo4j.com/developer/resources/)

[Community Forum](https://dev.neo4j.com/forum)

[Discord Chat](https://dev.neo4j.com/chat)

[Product Support](http://support.neo4j.com/)

[Neo4j Developer Blog](https://neo4j.com/blog/developer/)

[Neo4j Videos](https://neo4j.com/videos/)

[GraphAcademy](https://graphacademy.neo4j.com/?ref=docs-nav)

[Beginners Courses](https://graphacademy.neo4j.com/categories/beginners/?ref=docs-nav)
*   [Neo4j Fundamentals](https://graphacademy.neo4j.com/courses/neo4j-fundamentals/?ref=docs-nav)
*   [Cypher Fundamentals](https://graphacademy.neo4j.com/courses/cypher-fundamentals/?ref=docs-nav)
*   [Importing Data Fundamentals](https://graphacademy.neo4j.com/courses/importing-fundamentals/?ref=docs-nav)
*   [Importing CSV Data](https://graphacademy.neo4j.com/courses/importing-csv-data/?ref=docs-nav)
*   [Graph Data Modeling](https://graphacademy.neo4j.com/courses/modeling-fundamentals/?ref=docs-nav)

[Data Scientist Courses](https://graphacademy.neo4j.com/categories/data-scientist/?ref=docs-nav)
*   [Into to Graph Data Science](https://graphacademy.neo4j.com/courses/gds-product-introduction/?ref=docs-nav)
*   [Graph Data Science Fundamentals](https://graphacademy.neo4j.com/courses/graph-data-science-fundamentals/?ref=docs-nav)
*   [Path Finding](https://graphacademy.neo4j.com/courses/gds-shortest-paths/?ref=docs-nav)

[Generative AI Courses](https://graphacademy.neo4j.com/categories/llms/?ref=docs-nav)
*   [Neo4j & LLM Fundamentals](https://graphacademy.neo4j.com/courses/llm-fundamentals/?ref=docs-nav)
*   [Vector Indexes & Unstructured Data](https://graphacademy.neo4j.com/courses/llm-vectors-unstructured/?ref=docs-nav)
*   [Build a Chatbot with Python](https://graphacademy.neo4j.com/courses/llm-chatbot-python/?ref=docs-nav)
*   [Build a Chatbot with TypeScript](https://graphacademy.neo4j.com/courses/llm-chatbot-typescript/?ref=docs-nav)

[Neo4j Certification](https://graphacademy.neo4j.com/certification/?ref=docs-nav)
*   [Neo4j Certified Professional](https://graphacademy.neo4j.com/certifications/neo4j-certification/?ref=docs-nav)
*   [Neo4j Graph Data Science Certification](https://graphacademy.neo4j.com/certifications/gds-certification/?ref=docs-nav)

[Get Started Free](https://console.neo4j.io/?ref=docs-nav-get-started)

[Search](https://neo4j.com/docs/operations-manual/current/backup-restore/#search)

[Skip to content](https://neo4j.com/docs/operations-manual/current/backup-restore/#skip-to-content "Skip to content")

Operations Manual

Product Version

*       *   [The Neo4j Operations Manual](https://neo4j.com/docs/operations-manual/current/)
    *   [Introduction](https://neo4j.com/docs/operations-manual/current/introduction/)
    *   [Installation](https://neo4j.com/docs/operations-manual/current/installation/)
        *   [System requirements](https://neo4j.com/docs/operations-manual/current/installation/requirements/)
        *   [Linux installation](https://neo4j.com/docs/operations-manual/current/installation/linux/)
            *   [Debian-based distributions (.deb)](https://neo4j.com/docs/operations-manual/current/installation/linux/debian/)
            *   [Red Hat, CentOS, Fedora, and Amazon Linux (.rpm)](https://neo4j.com/docs/operations-manual/current/installation/linux/rpm/)
            *   [Linux executable (.tar)](https://neo4j.com/docs/operations-manual/current/installation/linux/tarball/)
            *   [Neo4j system service](https://neo4j.com/docs/operations-manual/current/installation/linux/systemd/)

        *   [macOS installation](https://neo4j.com/docs/operations-manual/current/installation/osx/)
        *   [Windows installation](https://neo4j.com/docs/operations-manual/current/installation/windows/)
        *   [Neo4j Desktop](https://neo4j.com/docs/operations-manual/current/installation/neo4j-desktop/)

    *   [Cloud deployments](https://neo4j.com/docs/operations-manual/current/cloud-deployments/)
        *   [Neo4j on AWS](https://neo4j.com/docs/operations-manual/current/cloud-deployments/neo4j-aws/)
        *   [Neo4j on GCP](https://neo4j.com/docs/operations-manual/current/cloud-deployments/neo4j-gcp/)

    *   [Docker](https://neo4j.com/docs/operations-manual/current/docker/)
        *   [Getting started with Neo4j in Docker](https://neo4j.com/docs/operations-manual/current/docker/introduction/)
        *   [Persisting data with Docker volumes](https://neo4j.com/docs/operations-manual/current/docker/mounting-volumes/)
        *   [Modify the default configuration](https://neo4j.com/docs/operations-manual/current/docker/configuration/)
        *   [Plugins](https://neo4j.com/docs/operations-manual/current/docker/plugins/)
        *   [Deploy a Neo4j standalone server using Docker Compose](https://neo4j.com/docs/operations-manual/current/docker/docker-compose-standalone/)
        *   [Deploy a Neo4j cluster on multiple Docker hosts](https://neo4j.com/docs/operations-manual/current/docker/clustering/)
        *   [Access Neo4j](https://neo4j.com/docs/operations-manual/current/docker/accessing-neo4j/)
        *   [Docker-specific operations](https://neo4j.com/docs/operations-manual/current/docker/operations/)
        *   [Dump and load a Neo4j database (offline)](https://neo4j.com/docs/operations-manual/current/docker/dump-load/)
        *   [Back up and restore a Neo4j database (online)](https://neo4j.com/docs/operations-manual/current/docker/backup-restore/)
        *   [SSL encryption in a Neo4j Docker container](https://neo4j.com/docs/operations-manual/current/docker/security/)
        *   [Docker-specific configuration settings](https://neo4j.com/docs/operations-manual/current/docker/ref-settings/)

    *   [Kubernetes](https://neo4j.com/docs/operations-manual/current/kubernetes/)
        *   [Introduction](https://neo4j.com/docs/operations-manual/current/kubernetes/introduction/)
        *   [Configuring the Neo4j Helm chart repository](https://neo4j.com/docs/operations-manual/current/kubernetes/helm-charts-setup/)
        *   [Quickstart: Deploy a standalone instance](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-standalone/)
            *   [Neo4j Helm chart for standalone server deployments](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-standalone/server-setup/)
            *   [Prerequisites](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-standalone/prerequisites/)
            *   [Create a Helm deployment _values.yaml_ file](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-standalone/create-value-file/)
            *   [Install a Neo4j standalone instance](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-standalone/install-neo4j/)
            *   [Verify the installation](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-standalone/verify-installation/)
            *   [Uninstall Neo4j and clean up the created resources](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-standalone/uninstall-cleanup/)

        *   [Quickstart: Deploy a cluster](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-cluster/)
            *   [Neo4j Helm chart for cluster deployments](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-cluster/server-setup/)
            *   [Prerequisites](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-cluster/prerequisites/)
            *   [Create Helm deployment values files](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-cluster/create-value-file/)
            *   [Install Neo4j cluster servers](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-cluster/install-servers/)
            *   [Verify the Neo4j cluster formation](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-cluster/verify-cluster-formation/)
            *   [Access the Neo4j cluster from inside Kubernetes](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-cluster/access-inside-k8s/)
            *   [Access the Neo4j cluster from outside Kubernetes](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-cluster/access-outside-k8s/)
            *   [Uninstall Neo4j cluster and clean up resources](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-cluster/uninstall-cleanup/)

        *   [Quickstart: Deploy a Neo4j cluster for analytic queries](https://neo4j.com/docs/operations-manual/current/kubernetes/quickstart-analytics-cluster/)
        *   [Volume mounts and persistent volumes](https://neo4j.com/docs/operations-manual/current/kubernetes/persistent-volumes/)
        *   [Customizing a Neo4j Helm chart](https://neo4j.com/docs/operations-manual/current/kubernetes/configuration/)
        *   [Configuring SSL](https://neo4j.com/docs/operations-manual/current/kubernetes/security/)
        *   [Authentication and authorization](https://neo4j.com/docs/operations-manual/current/kubernetes/authentication-authorization/)
        *   [Plugins](https://neo4j.com/docs/operations-manual/current/kubernetes/plugins/)
        *   [Accessing Neo4j](https://neo4j.com/docs/operations-manual/current/kubernetes/accessing-neo4j/)
        *   [Accessing Neo4j using Kubernetes Ingress](https://neo4j.com/docs/operations-manual/current/kubernetes/accessing-neo4j-ingress/)
        *   [Importing data](https://neo4j.com/docs/operations-manual/current/kubernetes/import-data/)
        *   [Monitoring](https://neo4j.com/docs/operations-manual/current/kubernetes/monitoring/)
        *   [Operations](https://neo4j.com/docs/operations-manual/current/kubernetes/operations/)
            *   [Maintenance modes](https://neo4j.com/docs/operations-manual/current/kubernetes/operations/maintenance-mode/)
            *   [Reset the `neo4j` user password](https://neo4j.com/docs/operations-manual/current/kubernetes/operations/reset-password/)
            *   [Restart a Neo4j pod after configuration change](https://neo4j.com/docs/operations-manual/current/kubernetes/operations/restart-pod/)
            *   [Dump and load databases (offline)](https://neo4j.com/docs/operations-manual/current/kubernetes/operations/dump-load/)
            *   [Back up, aggregate, and restore (online)](https://neo4j.com/docs/operations-manual/current/kubernetes/operations/backup-restore/)
            *   [Upgrade Neo4j on Kubernetes](https://neo4j.com/docs/operations-manual/current/kubernetes/operations/upgrade/)
            *   [Migrate Neo4j from Labs Helm to Neo4j Helm charts](https://neo4j.com/docs/operations-manual/current/kubernetes/operations/migrate-from-labs/)
            *   [Scale a Neo4j deployment](https://neo4j.com/docs/operations-manual/current/kubernetes/operations/scaling/)
            *   [Use custom images from private registries](https://neo4j.com/docs/operations-manual/current/kubernetes/operations/image-pull-secret/)
            *   [Assign Neo4j pods to specific nodes](https://neo4j.com/docs/operations-manual/current/kubernetes/operations/assign-neo4j-pods/)

        *   [Troubleshooting](https://neo4j.com/docs/operations-manual/current/kubernetes/troubleshooting/)

    *   [Configuration](https://neo4j.com/docs/operations-manual/current/configuration/)
        *   [The neo4j.conf file](https://neo4j.com/docs/operations-manual/current/configuration/neo4j-conf/)
        *   [Command expansion](https://neo4j.com/docs/operations-manual/current/configuration/command-expansion/)
        *   [Default file locations](https://neo4j.com/docs/operations-manual/current/configuration/file-locations/)
        *   [Ports](https://neo4j.com/docs/operations-manual/current/configuration/ports/)
        *   [Configure the Cypher default version](https://neo4j.com/docs/operations-manual/current/configuration/cypher-version-configuration/)
        *   [Configure network connectors](https://neo4j.com/docs/operations-manual/current/configuration/connectors/)
        *   [Set an initial password](https://neo4j.com/docs/operations-manual/current/configuration/set-initial-password/)
        *   [Get initial memory recommendations](https://neo4j.com/docs/operations-manual/current/configuration/neo4j-admin-memrec/)
        *   [Plugins](https://neo4j.com/docs/operations-manual/current/configuration/plugins/)
        *   [Update dynamic settings](https://neo4j.com/docs/operations-manual/current/configuration/dynamic-settings/)
        *   [Migrate configurations](https://neo4j.com/docs/operations-manual/current/configuration/migrate-configuration/)
        *   [Validate configurations](https://neo4j.com/docs/operations-manual/current/configuration/validate-config/)
        *   [Configuration settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/)
            *   [Checkpoint settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_checkpoint_settings)
            *   [Cloud storage integration settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_cloud_storage_integration_settings)
            *   [Cluster settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_cluster_settings)
            *   [Connection settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_connection_settings)
            *   [Cypher settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_cypher_settings)
            *   [Database settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_database_settings)
            *   [DBMS settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_dbms_settings)
            *   [Import settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_import_settings)
            *   [Index settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_index_settings)
            *   [Logging settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_logging_settings)
            *   [Memory settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_memory_settings)
            *   [Metrics settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_metrics_settings)
            *   [Neo4j Browser and client settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_neo4j_browser_and_client_settings)
            *   [Kubernetes settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_kubernetes_settings)
            *   [Security settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_security_settings)
            *   [Server directories settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_server_directories_settings)
            *   [Server settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_server_settings)
            *   [Transaction settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_transaction_settings)
            *   [Transaction log settings](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#_transaction_log_settings)

    *   [Import](https://neo4j.com/docs/operations-manual/current/import/)
    *   [Database administration](https://neo4j.com/docs/operations-manual/current/database-administration/)
        *   [Database management command syntax](https://neo4j.com/docs/operations-manual/current/database-administration/syntax/)
        *   Standard databases
            *   [Naming rules for databases](https://neo4j.com/docs/operations-manual/current/database-administration/standard-databases/naming-databases/)
            *   [Create databases](https://neo4j.com/docs/operations-manual/current/database-administration/standard-databases/create-databases/)
            *   [Create a database from a URI](https://neo4j.com/docs/operations-manual/current/database-administration/standard-databases/seed-from-uri/)
            *   [List databases](https://neo4j.com/docs/operations-manual/current/database-administration/standard-databases/listing-databases/)
            *   [Alter databases](https://neo4j.com/docs/operations-manual/current/database-administration/standard-databases/alter-databases/)
            *   [Start and stop databases](https://neo4j.com/docs/operations-manual/current/database-administration/standard-databases/start-stop-databases/)
            *   [Recreate a database](https://neo4j.com/docs/operations-manual/current/database-administration/standard-databases/recreate-database/)
            *   [Delete databases](https://neo4j.com/docs/operations-manual/current/database-administration/standard-databases/delete-databases/)
            *   [Migrate a database](https://neo4j.com/docs/operations-manual/current/database-administration/standard-databases/migrate-database/)
            *   [Upload to Neo4j Aura](https://neo4j.com/docs/operations-manual/current/database-administration/standard-databases/upload-to-aura/)
            *   [`WAIT` options](https://neo4j.com/docs/operations-manual/current/database-administration/standard-databases/wait-options/)
            *   [Configuration parameters](https://neo4j.com/docs/operations-manual/current/database-administration/standard-databases/configuration-parameters/)
            *   [Error handling](https://neo4j.com/docs/operations-manual/current/database-administration/standard-databases/errors/)

        *   Database aliases
            *   [Naming rules for database aliases](https://neo4j.com/docs/operations-manual/current/database-administration/aliases/naming-aliases/)
            *   [Managing database aliases for standard databases](https://neo4j.com/docs/operations-manual/current/database-administration/aliases/manage-aliases-standard-databases/)
            *   [Managing database aliases in composite databases](https://neo4j.com/docs/operations-manual/current/database-administration/aliases/manage-aliases-composite-databases/)
            *   [Configuring remote database aliases](https://neo4j.com/docs/operations-manual/current/database-administration/aliases/remote-database-alias-configuration/)

        *   [Query routing decisions](https://neo4j.com/docs/operations-manual/current/database-administration/routing-decisions/)

    *   [Clustering](https://neo4j.com/docs/operations-manual/current/clustering/)
        *   [Introduction: Neo4j clustering architecture](https://neo4j.com/docs/operations-manual/current/clustering/introduction/)
        *   Setting up a cluster
            *   [Deploy a basic cluster](https://neo4j.com/docs/operations-manual/current/clustering/setup/deploy/)
            *   [Deploy an analytics cluster](https://neo4j.com/docs/operations-manual/current/clustering/setup/analytics-cluster/)
            *   [Move from a standalone deployment to a cluster](https://neo4j.com/docs/operations-manual/current/clustering/setup/single-to-cluster/)
            *   [Reconciler](https://neo4j.com/docs/operations-manual/current/clustering/setup/reconciler/)
            *   [Cluster server discovery](https://neo4j.com/docs/operations-manual/current/clustering/setup/discovery/)
            *   [Leadership, routing, and load balancing](https://neo4j.com/docs/operations-manual/current/clustering/setup/routing/)
            *   [Intra-cluster encryption](https://neo4j.com/docs/operations-manual/current/clustering/setup/encryption/)

        *   [Managing servers in a cluster](https://neo4j.com/docs/operations-manual/current/clustering/servers/)
        *   [Unbind a server](https://neo4j.com/docs/operations-manual/current/clustering/unbind/)
        *   [Managing databases in a cluster](https://neo4j.com/docs/operations-manual/current/clustering/databases/)
        *   [Unbind the `system` database](https://neo4j.com/docs/operations-manual/current/clustering/unbind-system-database/)
        *   Monitoring
            *   [Monitor servers](https://neo4j.com/docs/operations-manual/current/clustering/monitoring/show-servers-monitoring/)
            *   [Monitor databases](https://neo4j.com/docs/operations-manual/current/clustering/monitoring/show-databases-monitoring/)
            *   [Monitor cluster endpoints for status information](https://neo4j.com/docs/operations-manual/current/clustering/monitoring/endpoints/)
            *   [Monitor replication status](https://neo4j.com/docs/operations-manual/current/clustering/monitoring/status-check/)

        *   Resilient multi-region cluster deployment
            *   [Designing a resilient multi-data center cluster](https://neo4j.com/docs/operations-manual/current/clustering/multi-region-deployment/geo-redundant-deployment/)
            *   [Multi-data center routing](https://neo4j.com/docs/operations-manual/current/clustering/multi-region-deployment/multi-data-center-routing/)
            *   [Disaster recovery](https://neo4j.com/docs/operations-manual/current/clustering/multi-region-deployment/disaster-recovery/)

        *   [Settings reference](https://neo4j.com/docs/operations-manual/current/clustering/settings/)
        *   [Server management command syntax](https://neo4j.com/docs/operations-manual/current/clustering/server-syntax/)
        *   [Clustering glossary](https://neo4j.com/docs/operations-manual/current/clustering/glossary/)

    *   Scalability
        *   [Concepts](https://neo4j.com/docs/operations-manual/current/scalability/concepts/)
        *   [Scaling with Neo4j](https://neo4j.com/docs/operations-manual/current/scalability/scaling-with-neo4j/)
        *   Composite databases
            *   [Concepts](https://neo4j.com/docs/operations-manual/current/scalability/composite-databases/concepts/)
            *   [Create composite databases](https://neo4j.com/docs/operations-manual/current/scalability/composite-databases/create-composite-databases/)
            *   [List composite databases](https://neo4j.com/docs/operations-manual/current/scalability/composite-databases/list-composite-databases/)
            *   [Alter composite databases](https://neo4j.com/docs/operations-manual/current/scalability/composite-databases/alter-composite-databases/)
            *   [Start and stop composite databases](https://neo4j.com/docs/operations-manual/current/scalability/composite-databases/start-stop-composite-databases/)
            *   [Delete composite databases](https://neo4j.com/docs/operations-manual/current/scalability/composite-databases/delete-composite-databases/)
            *   [Set up and query composite databases](https://neo4j.com/docs/operations-manual/current/scalability/composite-databases/querying-composite-databases/)
            *   [Role-based access control (RBAC)](https://neo4j.com/docs/operations-manual/current/scalability/composite-databases/role-based-access-control-composite-databases/)
            *   [Sharding data with the `copy` command](https://neo4j.com/docs/operations-manual/current/scalability/composite-databases/sharding-with-copy/)

        *   Property sharding (Infinigraph)
            *   [Overview](https://neo4j.com/docs/operations-manual/current/scalability/sharded-property-databases/overview/)
            *   [Planning and sizing](https://neo4j.com/docs/operations-manual/current/scalability/sharded-property-databases/planning-and-sizing/)
            *   [System requirements and configuration](https://neo4j.com/docs/operations-manual/current/scalability/sharded-property-databases/configuration/)
            *   [Data ingestion](https://neo4j.com/docs/operations-manual/current/scalability/sharded-property-databases/data-ingestion/)
            *   [Creating sharded property databases](https://neo4j.com/docs/operations-manual/current/scalability/sharded-property-databases/creating-sharded-databases/)
            *   [Starting and stopping sharded property databases](https://neo4j.com/docs/operations-manual/current/scalability/sharded-property-databases/starting-stopping-sharded-databases/)
            *   [Listing sharded property databases](https://neo4j.com/docs/operations-manual/current/scalability/sharded-property-databases/listing-sharded-databases/)
            *   [Altering sharded property databases](https://neo4j.com/docs/operations-manual/current/scalability/sharded-property-databases/altering-sharded-databases/)
            *   [Deleting sharded property databases](https://neo4j.com/docs/operations-manual/current/scalability/sharded-property-databases/deleting-sharded-databases/)
            *   [Role-based access control (RBAC)](https://neo4j.com/docs/operations-manual/current/scalability/sharded-property-databases/role-based-access-control/)
            *   [Admin operations](https://neo4j.com/docs/operations-manual/current/scalability/sharded-property-databases/admin-operations/)
            *   [Security](https://neo4j.com/docs/operations-manual/current/scalability/sharded-property-databases/security/)
            *   [Limitations and considerations](https://neo4j.com/docs/operations-manual/current/scalability/sharded-property-databases/limitations-and-considerations/)

    *   [Database internals and transactional behavior](https://neo4j.com/docs/operations-manual/current/database-internals/)
        *   [Transaction management](https://neo4j.com/docs/operations-manual/current/database-internals/transaction-management/)
        *   [Concurrent data access](https://neo4j.com/docs/operations-manual/current/database-internals/concurrent-data-access/)
        *   [Transaction logging](https://neo4j.com/docs/operations-manual/current/database-internals/transaction-logs/)
        *   [Checkpointing and log pruning](https://neo4j.com/docs/operations-manual/current/database-internals/checkpointing/)
        *   [Store formats](https://neo4j.com/docs/operations-manual/current/database-internals/store-formats/)
        *   [Display store information](https://neo4j.com/docs/operations-manual/current/database-internals/neo4j-admin-store-info/)

    *   [Backup and restore](https://neo4j.com/docs/operations-manual/current/backup-restore/)
        *   [Backup and restore planning](https://neo4j.com/docs/operations-manual/current/backup-restore/planning/)
        *   [Backup modes](https://neo4j.com/docs/operations-manual/current/backup-restore/modes/)
        *   [Back up an online database](https://neo4j.com/docs/operations-manual/current/backup-restore/online-backup/)
        *   [Aggregate a database backup chain](https://neo4j.com/docs/operations-manual/current/backup-restore/aggregate/)
        *   [Inspect the metadata of a backup file](https://neo4j.com/docs/operations-manual/current/backup-restore/inspect/)
        *   [Validate a sharded property database backup](https://neo4j.com/docs/operations-manual/current/backup-restore/validate/)
        *   [Check database consistency](https://neo4j.com/docs/operations-manual/current/backup-restore/consistency-checker/)
        *   [Restore a database backup](https://neo4j.com/docs/operations-manual/current/backup-restore/restore-backup/)
        *   [Back up an offline database](https://neo4j.com/docs/operations-manual/current/backup-restore/offline-backup/)
        *   [Restore a database dump](https://neo4j.com/docs/operations-manual/current/backup-restore/restore-dump/)
        *   [Copy a database store](https://neo4j.com/docs/operations-manual/current/backup-restore/copy-database/)

    *   [Authentication and authorization](https://neo4j.com/docs/operations-manual/current/authentication-authorization/)
        *   [Manage users](https://neo4j.com/docs/operations-manual/current/authentication-authorization/manage-users/)
        *   [Manage roles](https://neo4j.com/docs/operations-manual/current/authentication-authorization/manage-roles/)
        *   [Recover admin user and password](https://neo4j.com/docs/operations-manual/current/authentication-authorization/password-and-user-recovery/)
        *   Manage privileges
            *   [Role-based access control](https://neo4j.com/docs/operations-manual/current/authentication-authorization/manage-privileges/)
            *   [Read privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/privileges-reads/)
            *   [Property-based access control](https://neo4j.com/docs/operations-manual/current/authentication-authorization/property-based-access-control/)
            *   [Write privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/privileges-writes/)
            *   [Database privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/database-administration/)
            *   [DBMS privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/dbms-administration/)
                *   [Administrator role privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/dbms-administration/dbms-admin-role/)
                *   [The DBMS `ROLE MANAGEMENT` privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/dbms-administration/dbms-role-management-privileges/)
                *   [The DBMS `USER MANAGEMENT` privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/dbms-administration/dbms-user-management-privileges/)
                *   [The DBMS `IMPERSONATE` privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/dbms-administration/dbms-impersonate-privileges/)
                *   [The DBMS `DATABASE MANAGEMENT` privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/dbms-administration/dbms-database-management-privileges/)
                *   [The DBMS `ALIAS MANAGEMENT` privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/dbms-administration/dbms-alias-management-privileges/)
                *   [The DBMS `SERVER MANAGEMENT` privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/dbms-administration/dbms-server-management-privileges/)
                *   [The DBMS `PRIVILEGE MANAGEMENT` privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/dbms-administration/dbms-privilege-management-privileges/)
                *   [The DBMS `EXECUTE` privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/dbms-administration/dbms-execute-privileges/)
                *   [The DBMS `SETTING` privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/dbms-administration/dbms-setting-privileges/)

            *   [Load privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/load-privileges/)
            *   [Limitations](https://neo4j.com/docs/operations-manual/current/authentication-authorization/limitations/)
            *   [Procedure and user-defined function privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/manage-execute-permissions/)

        *   [Built-in roles and privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/built-in-roles/)
        *   [Immutable roles and privileges](https://neo4j.com/docs/operations-manual/current/authentication-authorization/immutable-roles-privileges/)
        *   Integration with auth systems
            *   [User auth providers](https://neo4j.com/docs/operations-manual/current/authentication-authorization/auth-providers/)
            *   [LDAP integration](https://neo4j.com/docs/operations-manual/current/authentication-authorization/ldap-integration/)
            *   [Single sign-on integration](https://neo4j.com/docs/operations-manual/current/authentication-authorization/sso-integration/)

    *   [Security](https://neo4j.com/docs/operations-manual/current/security/)
        *   [Securing extensions](https://neo4j.com/docs/operations-manual/current/security/securing-extensions/)
        *   [SSL framework](https://neo4j.com/docs/operations-manual/current/security/ssl-framework/)
            *   [Configuring SSL for FIPS 140-2 compatibility](https://neo4j.com/docs/operations-manual/current/security/ssl-fips-compatibility/)

        *   [Browser credentials handling](https://neo4j.com/docs/operations-manual/current/security/browser/)
        *   [Security checklist](https://neo4j.com/docs/operations-manual/current/security/checklist/)

    *   [Performance](https://neo4j.com/docs/operations-manual/current/performance/)
        *   [Memory configuration](https://neo4j.com/docs/operations-manual/current/performance/memory-configuration/)
        *   [Vector index memory configuration](https://neo4j.com/docs/operations-manual/current/performance/vector-index-memory-configuration/)
        *   [Index configuration](https://neo4j.com/docs/operations-manual/current/performance/index-configuration/)
        *   [Tuning of the garbage collector](https://neo4j.com/docs/operations-manual/current/performance/gc-tuning/)
        *   [Bolt thread pool configuration](https://neo4j.com/docs/operations-manual/current/performance/bolt-thread-pool-configuration/)
        *   [Linux file system tuning](https://neo4j.com/docs/operations-manual/current/performance/linux-file-system-tuning/)
        *   [Disks, RAM and other tips](https://neo4j.com/docs/operations-manual/current/performance/disks-ram-and-other-tips/)
        *   [Statistics and execution plans](https://neo4j.com/docs/operations-manual/current/performance/statistics-execution-plans/)
        *   [Space reuse](https://neo4j.com/docs/operations-manual/current/performance/space-reuse/)

    *   [Monitoring](https://neo4j.com/docs/operations-manual/current/monitoring/)
        *   [Logging](https://neo4j.com/docs/operations-manual/current/monitoring/logging/)
        *   [Metrics](https://neo4j.com/docs/operations-manual/current/monitoring/metrics/)
            *   [Essential metrics](https://neo4j.com/docs/operations-manual/current/monitoring/metrics/essential/)
            *   [Enable metrics logging](https://neo4j.com/docs/operations-manual/current/monitoring/metrics/enable/)
            *   [Expose metrics](https://neo4j.com/docs/operations-manual/current/monitoring/metrics/expose/)
            *   [Metrics reference](https://neo4j.com/docs/operations-manual/current/monitoring/metrics/reference/)

        *   [Manage queries](https://neo4j.com/docs/operations-manual/current/monitoring/query-management/)
        *   [Manage connections](https://neo4j.com/docs/operations-manual/current/monitoring/connection-management/)
        *   [Manage background jobs](https://neo4j.com/docs/operations-manual/current/monitoring/background-jobs/)
        *   [Generate a report about the system](https://neo4j.com/docs/operations-manual/current/monitoring/neo4j-admin-report/)

    *   [Neo4j Admin and Neo4j CLI](https://neo4j.com/docs/operations-manual/current/neo4j-admin-neo4j-cli/)
    *   [Cypher Shell](https://neo4j.com/docs/operations-manual/current/cypher-shell/)
    *   [Procedures](https://neo4j.com/docs/operations-manual/current/procedures/)
    *   Changes, deprecations, and removals
        *   [Changes in Neo4j 2025-2026 series](https://neo4j.com/docs/operations-manual/current/changes-2025-2026/)
        *   [Current deprecations](https://neo4j.com/docs/operations-manual/current/deprecations/)
        *   [Breaking changes in Neo4j 2025.01](https://neo4j.com/docs/operations-manual/current/breaking-changes/)

    *   [Tutorials](https://neo4j.com/docs/operations-manual/current/tutorial/)
        *   [Importing data](https://neo4j.com/docs/operations-manual/current/tutorial/neo4j-admin-import/)
        *   [Setting up and using a composite database](https://neo4j.com/docs/operations-manual/current/tutorial/tutorial-composite-database/)
        *   [Fine-grained access control](https://neo4j.com/docs/operations-manual/current/tutorial/access-control/)
        *   [Configuring Neo4j Single Sign-On (SSO)](https://neo4j.com/docs/operations-manual/current/tutorial/tutorial-sso-configuration/)
        *   [Deploying a Neo4j cluster in a Docker container](https://neo4j.com/docs/operations-manual/current/tutorial/tutorial-clustering-docker/)

**Is this page helpful?**

[](https://neo4j.com/docs)
*   [Operations Manual](https://neo4j.com/docs/operations-manual/current/)
*   [Backup and restore](https://neo4j.com/docs/operations-manual/current/backup-restore/)

[Raise an issue](https://github.com/neo4j/docs-operations/issues/new/?title=Docs%20Feedback%20modules/ROOT/pages/backup-restore/index.adoc%20(ref:%20main)&body=%3E%20Do%20not%20include%20confidential%20information,%20personal%20data,%20sensitive%20data,%20or%20other%20regulated%20data.)

Backup and restore
==================

This chapter describes the following:

*   [Backup and restore planning](https://neo4j.com/docs/operations-manual/current/backup-restore/planning/) — What to consider when designing your backup and restore strategy.

*   [Backup modes](https://neo4j.com/docs/operations-manual/current/backup-restore/modes/) — The supported backup modes.

*   Enterprise Edition[Back up an online database](https://neo4j.com/docs/operations-manual/current/backup-restore/online-backup/) — How to back up an online database.

*   Enterprise Edition[Aggregate a database backup chain](https://neo4j.com/docs/operations-manual/current/backup-restore/aggregate/) - How to aggregate a backup chain into a single backup.

*   Enterprise Edition[Inspect the metadata of a database backup file](https://neo4j.com/docs/operations-manual/current/backup-restore/inspect/) — How to inspect the metadata of a database backup file.

*   Enterprise Edition[Validate a sharded property database backup](https://neo4j.com/docs/operations-manual/current/backup-restore/validate/) — How to validate a sharded property database backup using the `neo4j-admin backup validate` command.

*   [Check database consistency](https://neo4j.com/docs/operations-manual/current/backup-restore/consistency-checker/) — How to check the consistency of a database, backup, or a dump.

*   Enterprise Edition[Restore a database backup](https://neo4j.com/docs/operations-manual/current/backup-restore/restore-backup/) — How to restore a database backup in a live Neo4j deployment.

*   [Back up an offline database](https://neo4j.com/docs/operations-manual/current/backup-restore/offline-backup/) — How to back up an offline database.

*   [Restore a database dump](https://neo4j.com/docs/operations-manual/current/backup-restore/restore-dump/) — How to restore a database dump in a live Neo4j deployment.

*   Enterprise Edition[Copy a database store](https://neo4j.com/docs/operations-manual/current/backup-restore/copy-database/) — How to copy data store from an existing database to a new database.

[Display store information](https://neo4j.com/docs/operations-manual/current/database-internals/neo4j-admin-store-info/)[Backup and restore planning](https://neo4j.com/docs/operations-manual/current/backup-restore/planning/)

[![Image 2](https://neo4j.com/docs/assets/img/Nodes-AI-Color.png) One Day of AI and Graphs on April 15, 2026 ------------------------------------------ The Call for Papers is now open. Submit your talk by December 12, 2025 Submit your talk](https://sessionize.com/nodesai2026/)

Learn
-----

*   [Sandbox](https://neo4j.com/sandbox/?ref=developer-footer)
*   [Neo4j Community Site](https://community.neo4j.com/?ref=developer-footer)
*   [Neo4j Developer Blog](https://medium.com/neo4j)
*   [Neo4j Videos](https://www.youtube.com/neo4j)
*   [GraphAcademy](https://neo4j.com/graphacademy/?ref=developer-footer)
*   [Neo4j Labs](https://neo4j.com/labs/?ref=developer-footer)

Social
------

*   [Twitter](https://twitter.com/neo4j)
*   [Meetups](https://www.meetup.com/Neo4j-Online-Meetup/)
*   [Github](https://github.com/neo4j/neo4j)
*   [Stack Overflow](https://stackoverflow.com/questions/tagged/neo4j)
*   [Want to Speak?](https://docs.google.com/forms/d/e/1FAIpQLSdEcNnMruES5iwvOVYovmS1D_P1ZL_HdUOitFrwrvruv5PZvA/viewform)

[Contact Us →](https://neo4j.com/contact-us/?ref=footer)
--------------------------------------------------------

*   US: 1-855-636-4532
*   Sweden +46 171 480 113
*   UK: +44 20 3868 3223
*   France: +33 (0) 1 88 46 13 20

© 2026 Neo4j, Inc.

[Terms](https://neo4j.com/terms/) | [Privacy](https://neo4j.com/privacy-policy/) | [Sitemap](https://neo4j.com/sitemap/)

Neo4j®, Neo Technology®, Cypher®, Neo4j® Bloom™ and Neo4j® Aura™ are registered trademarks of Neo4j, Inc. All other marks are owned by their respective companies.

AI search

###### AI SEARCH

Ask Neo4j anything or try one of the following questions

How do I model data for a graph database?How do I use the MATCH clause in Cypher?How do I use Neo4j with Python?How do I get started with graph algorithms? 

This is an experimental AI chatbot. All information should be verified.

![Image 3](blob:https://neo4j.com/43289042-9ae4-4218-9279-a60228a4bb60)
