# Source: https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/

Title: Import - Operations Manual

URL Source: https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/

Markdown Content:
Import - Operations Manual
===============

This website uses cookies

We use cookies to offer you a better browsing experience, analyze site traffic, personalize content and serve targeted ads. Learn about how we use cookies and how you can control them in [Cookie Settings](https://neo4j.com/neo4j-cookie-and-tracking-policy/). By using our site. you consent to our use of cookies.

[Accept Cookies](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#)[Use necessary cookies only](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#)

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

[Search](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#search)

[Skip to content](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#skip-to-content "Skip to content")

Operations Manual

Product Version

*       *   [The Neo4j Operations Manual](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/)
    *   [Introduction](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/introduction/)
    *   [Installation](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/installation/)
        *   [System requirements](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/installation/requirements/)
        *   [Linux installation](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/installation/linux/)
            *   [Debian-based distributions (.deb)](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/installation/linux/debian/)
            *   [Red Hat, CentOS, Fedora, and Amazon Linux (.rpm)](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/installation/linux/rpm/)
            *   [Linux executable (.tar)](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/installation/linux/tarball/)
            *   [Neo4j system service](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/installation/linux/systemd/)

        *   [macOS installation](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/installation/osx/)
        *   [Windows installation](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/installation/windows/)
        *   [Neo4j Desktop](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/installation/neo4j-desktop/)

    *   [Cloud deployments](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/cloud-deployments/)
        *   [Neo4j on AWS](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/cloud-deployments/neo4j-aws/)
        *   [Neo4j on GCP](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/cloud-deployments/neo4j-gcp/)

    *   [Docker](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/docker/)
        *   [Getting started with Neo4j in Docker](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/docker/introduction/)
        *   [Persisting data with Docker volumes](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/docker/mounting-volumes/)
        *   [Modify the default configuration](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/docker/configuration/)
        *   [Plugins](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/docker/plugins/)
        *   [Deploy a Neo4j standalone server using Docker Compose](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/docker/docker-compose-standalone/)
        *   [Deploy a Neo4j cluster on multiple Docker hosts](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/docker/clustering/)
        *   [Access Neo4j](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/docker/accessing-neo4j/)
        *   [Docker-specific operations](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/docker/operations/)
        *   [Dump and load a Neo4j database (offline)](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/docker/dump-load/)
        *   [Back up and restore a Neo4j database (online)](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/docker/backup-restore/)
        *   [SSL encryption in a Neo4j Docker container](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/docker/security/)
        *   [Docker-specific configuration settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/docker/ref-settings/)

    *   [Kubernetes](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/)
        *   [Introduction](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/introduction/)
        *   [Configuring the Neo4j Helm chart repository](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/helm-charts-setup/)
        *   [Quickstart: Deploy a standalone instance](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-standalone/)
            *   [Neo4j Helm chart for standalone server deployments](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-standalone/server-setup/)
            *   [Prerequisites](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-standalone/prerequisites/)
            *   [Create a Helm deployment _values.yaml_ file](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-standalone/create-value-file/)
            *   [Install a Neo4j standalone instance](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-standalone/install-neo4j/)
            *   [Verify the installation](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-standalone/verify-installation/)
            *   [Uninstall Neo4j and clean up the created resources](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-standalone/uninstall-cleanup/)

        *   [Quickstart: Deploy a cluster](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-cluster/)
            *   [Neo4j Helm chart for cluster deployments](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-cluster/server-setup/)
            *   [Prerequisites](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-cluster/prerequisites/)
            *   [Create Helm deployment values files](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-cluster/create-value-file/)
            *   [Install Neo4j cluster servers](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-cluster/install-servers/)
            *   [Verify the Neo4j cluster formation](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-cluster/verify-cluster-formation/)
            *   [Access the Neo4j cluster from inside Kubernetes](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-cluster/access-inside-k8s/)
            *   [Access the Neo4j cluster from outside Kubernetes](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-cluster/access-outside-k8s/)
            *   [Uninstall Neo4j cluster and clean up resources](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-cluster/uninstall-cleanup/)

        *   [Quickstart: Deploy a Neo4j cluster for analytic queries](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/quickstart-analytics-cluster/)
        *   [Volume mounts and persistent volumes](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/persistent-volumes/)
        *   [Customizing a Neo4j Helm chart](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/configuration/)
        *   [Configuring SSL](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/security/)
        *   [Authentication and authorization](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/authentication-authorization/)
        *   [Plugins](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/plugins/)
        *   [Accessing Neo4j](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/accessing-neo4j/)
        *   [Accessing Neo4j using Kubernetes Ingress](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/accessing-neo4j-ingress/)
        *   [Importing data](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/import-data/)
        *   [Monitoring](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/monitoring/)
        *   [Operations](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/operations/)
            *   [Maintenance modes](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/operations/maintenance-mode/)
            *   [Reset the `neo4j` user password](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/operations/reset-password/)
            *   [Restart a Neo4j pod after configuration change](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/operations/restart-pod/)
            *   [Dump and load databases (offline)](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/operations/dump-load/)
            *   [Back up, aggregate, and restore (online)](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/operations/backup-restore/)
            *   [Upgrade Neo4j on Kubernetes](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/operations/upgrade/)
            *   [Migrate Neo4j from Labs Helm to Neo4j Helm charts](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/operations/migrate-from-labs/)
            *   [Scale a Neo4j deployment](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/operations/scaling/)
            *   [Use custom images from private registries](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/operations/image-pull-secret/)
            *   [Assign Neo4j pods to specific nodes](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/operations/assign-neo4j-pods/)

        *   [Troubleshooting](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/kubernetes/troubleshooting/)

    *   [Configuration](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/)
        *   [The neo4j.conf file](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/neo4j-conf/)
        *   [Command expansion](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/command-expansion/)
        *   [Default file locations](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/file-locations/)
        *   [Ports](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/ports/)
        *   [Configure the Cypher default version](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/cypher-version-configuration/)
        *   [Configure network connectors](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/connectors/)
        *   [Set an initial password](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/set-initial-password/)
        *   [Get initial memory recommendations](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/neo4j-admin-memrec/)
        *   [Plugins](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/plugins/)
        *   [Update dynamic settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/dynamic-settings/)
        *   [Migrate configurations](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/migrate-configuration/)
        *   [Validate configurations](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/validate-config/)
        *   [Configuration settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/)
            *   [Checkpoint settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_checkpoint_settings)
            *   [Cloud storage integration settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_cloud_storage_integration_settings)
            *   [Cluster settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_cluster_settings)
            *   [Connection settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_connection_settings)
            *   [Cypher settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_cypher_settings)
            *   [Database settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_database_settings)
            *   [DBMS settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_dbms_settings)
            *   [Import settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_import_settings)
            *   [Index settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_index_settings)
            *   [Logging settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_logging_settings)
            *   [Memory settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_memory_settings)
            *   [Metrics settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_metrics_settings)
            *   [Neo4j Browser and client settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_neo4j_browser_and_client_settings)
            *   [Kubernetes settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_kubernetes_settings)
            *   [Security settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_security_settings)
            *   [Server directories settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_server_directories_settings)
            *   [Server settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_server_settings)
            *   [Transaction settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_transaction_settings)
            *   [Transaction log settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_transaction_log_settings)

    *   [Import](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/)
    *   [Database administration](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/)
        *   [Database management command syntax](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/syntax/)
        *   Standard databases
            *   [Naming rules for databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/standard-databases/naming-databases/)
            *   [Create databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/standard-databases/create-databases/)
            *   [Create a database from a URI](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/standard-databases/seed-from-uri/)
            *   [List databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/standard-databases/listing-databases/)
            *   [Alter databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/standard-databases/alter-databases/)
            *   [Start and stop databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/standard-databases/start-stop-databases/)
            *   [Recreate a database](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/standard-databases/recreate-database/)
            *   [Delete databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/standard-databases/delete-databases/)
            *   [Migrate a database](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/standard-databases/migrate-database/)
            *   [Upload to Neo4j Aura](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/standard-databases/upload-to-aura/)
            *   [`WAIT` options](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/standard-databases/wait-options/)
            *   [Configuration parameters](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/standard-databases/configuration-parameters/)
            *   [Error handling](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/standard-databases/errors/)

        *   Database aliases
            *   [Naming rules for database aliases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/aliases/naming-aliases/)
            *   [Managing database aliases for standard databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/aliases/manage-aliases-standard-databases/)
            *   [Managing database aliases in composite databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/aliases/manage-aliases-composite-databases/)
            *   [Configuring remote database aliases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/aliases/remote-database-alias-configuration/)

        *   [Query routing decisions](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/routing-decisions/)

    *   [Clustering](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/)
        *   [Introduction: Neo4j clustering architecture](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/introduction/)
        *   Setting up a cluster
            *   [Deploy a basic cluster](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/setup/deploy/)
            *   [Deploy an analytics cluster](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/setup/analytics-cluster/)
            *   [Move from a standalone deployment to a cluster](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/setup/single-to-cluster/)
            *   [Reconciler](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/setup/reconciler/)
            *   [Cluster server discovery](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/setup/discovery/)
            *   [Leadership, routing, and load balancing](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/setup/routing/)
            *   [Intra-cluster encryption](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/setup/encryption/)

        *   [Managing servers in a cluster](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/servers/)
        *   [Unbind a server](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/unbind/)
        *   [Managing databases in a cluster](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/databases/)
        *   [Unbind the `system` database](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/unbind-system-database/)
        *   Monitoring
            *   [Monitor servers](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/monitoring/show-servers-monitoring/)
            *   [Monitor databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/monitoring/show-databases-monitoring/)
            *   [Monitor cluster endpoints for status information](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/monitoring/endpoints/)
            *   [Monitor replication status](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/monitoring/status-check/)

        *   Resilient multi-region cluster deployment
            *   [Designing a resilient multi-data center cluster](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/multi-region-deployment/geo-redundant-deployment/)
            *   [Multi-data center routing](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/multi-region-deployment/multi-data-center-routing/)
            *   [Disaster recovery](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/multi-region-deployment/disaster-recovery/)

        *   [Settings reference](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/settings/)
        *   [Server management command syntax](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/server-syntax/)
        *   [Clustering glossary](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/glossary/)

    *   Scalability
        *   [Concepts](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/concepts/)
        *   [Scaling with Neo4j](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/scaling-with-neo4j/)
        *   Composite databases
            *   [Concepts](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/composite-databases/concepts/)
            *   [Create composite databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/composite-databases/create-composite-databases/)
            *   [List composite databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/composite-databases/list-composite-databases/)
            *   [Alter composite databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/composite-databases/alter-composite-databases/)
            *   [Start and stop composite databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/composite-databases/start-stop-composite-databases/)
            *   [Delete composite databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/composite-databases/delete-composite-databases/)
            *   [Set up and query composite databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/composite-databases/querying-composite-databases/)
            *   [Role-based access control (RBAC)](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/composite-databases/role-based-access-control-composite-databases/)
            *   [Sharding data with the `copy` command](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/composite-databases/sharding-with-copy/)

        *   Property sharding (Infinigraph)
            *   [Overview](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/sharded-property-databases/overview/)
            *   [Planning and sizing](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/sharded-property-databases/planning-and-sizing/)
            *   [System requirements and configuration](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/sharded-property-databases/configuration/)
            *   [Data ingestion](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/sharded-property-databases/data-ingestion/)
            *   [Creating sharded property databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/sharded-property-databases/creating-sharded-databases/)
            *   [Starting and stopping sharded property databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/sharded-property-databases/starting-stopping-sharded-databases/)
            *   [Listing sharded property databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/sharded-property-databases/listing-sharded-databases/)
            *   [Altering sharded property databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/sharded-property-databases/altering-sharded-databases/)
            *   [Deleting sharded property databases](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/sharded-property-databases/deleting-sharded-databases/)
            *   [Role-based access control (RBAC)](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/sharded-property-databases/role-based-access-control/)
            *   [Admin operations](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/sharded-property-databases/admin-operations/)
            *   [Security](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/sharded-property-databases/security/)
            *   [Limitations and considerations](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/sharded-property-databases/limitations-and-considerations/)

    *   [Database internals and transactional behavior](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-internals/)
        *   [Transaction management](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-internals/transaction-management/)
        *   [Concurrent data access](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-internals/concurrent-data-access/)
        *   [Transaction logging](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-internals/transaction-logs/)
        *   [Checkpointing and log pruning](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-internals/checkpointing/)
        *   [Store formats](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-internals/store-formats/)
        *   [Display store information](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-internals/neo4j-admin-store-info/)

    *   [Backup and restore](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/backup-restore/)
        *   [Backup and restore planning](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/backup-restore/planning/)
        *   [Backup modes](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/backup-restore/modes/)
        *   [Back up an online database](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/backup-restore/online-backup/)
        *   [Aggregate a database backup chain](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/backup-restore/aggregate/)
        *   [Inspect the metadata of a backup file](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/backup-restore/inspect/)
        *   [Validate a sharded property database backup](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/backup-restore/validate/)
        *   [Check database consistency](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/backup-restore/consistency-checker/)
        *   [Restore a database backup](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/backup-restore/restore-backup/)
        *   [Back up an offline database](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/backup-restore/offline-backup/)
        *   [Restore a database dump](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/backup-restore/restore-dump/)
        *   [Copy a database store](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/backup-restore/copy-database/)

    *   [Authentication and authorization](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/)
        *   [Manage users](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/manage-users/)
        *   [Manage roles](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/manage-roles/)
        *   [Recover admin user and password](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/password-and-user-recovery/)
        *   Manage privileges
            *   [Role-based access control](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/manage-privileges/)
            *   [Read privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/privileges-reads/)
            *   [Property-based access control](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/property-based-access-control/)
            *   [Write privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/privileges-writes/)
            *   [Database privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/database-administration/)
            *   [DBMS privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/dbms-administration/)
                *   [Administrator role privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/dbms-administration/dbms-admin-role/)
                *   [The DBMS `ROLE MANAGEMENT` privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/dbms-administration/dbms-role-management-privileges/)
                *   [The DBMS `USER MANAGEMENT` privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/dbms-administration/dbms-user-management-privileges/)
                *   [The DBMS `IMPERSONATE` privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/dbms-administration/dbms-impersonate-privileges/)
                *   [The DBMS `DATABASE MANAGEMENT` privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/dbms-administration/dbms-database-management-privileges/)
                *   [The DBMS `ALIAS MANAGEMENT` privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/dbms-administration/dbms-alias-management-privileges/)
                *   [The DBMS `SERVER MANAGEMENT` privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/dbms-administration/dbms-server-management-privileges/)
                *   [The DBMS `PRIVILEGE MANAGEMENT` privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/dbms-administration/dbms-privilege-management-privileges/)
                *   [The DBMS `EXECUTE` privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/dbms-administration/dbms-execute-privileges/)
                *   [The DBMS `SETTING` privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/dbms-administration/dbms-setting-privileges/)

            *   [Load privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/load-privileges/)
            *   [Limitations](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/limitations/)
            *   [Procedure and user-defined function privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/manage-execute-permissions/)

        *   [Built-in roles and privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/built-in-roles/)
        *   [Immutable roles and privileges](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/immutable-roles-privileges/)
        *   Integration with auth systems
            *   [User auth providers](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/auth-providers/)
            *   [LDAP integration](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/ldap-integration/)
            *   [Single sign-on integration](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/authentication-authorization/sso-integration/)

    *   [Security](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/security/)
        *   [Securing extensions](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/security/securing-extensions/)
        *   [SSL framework](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/security/ssl-framework/)
            *   [Configuring SSL for FIPS 140-2 compatibility](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/security/ssl-fips-compatibility/)

        *   [Browser credentials handling](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/security/browser/)
        *   [Security checklist](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/security/checklist/)

    *   [Performance](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/performance/)
        *   [Memory configuration](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/performance/memory-configuration/)
        *   [Vector index memory configuration](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/performance/vector-index-memory-configuration/)
        *   [Index configuration](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/performance/index-configuration/)
        *   [Tuning of the garbage collector](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/performance/gc-tuning/)
        *   [Bolt thread pool configuration](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/performance/bolt-thread-pool-configuration/)
        *   [Linux file system tuning](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/performance/linux-file-system-tuning/)
        *   [Disks, RAM and other tips](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/performance/disks-ram-and-other-tips/)
        *   [Statistics and execution plans](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/performance/statistics-execution-plans/)
        *   [Space reuse](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/performance/space-reuse/)

    *   [Monitoring](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/monitoring/)
        *   [Logging](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/monitoring/logging/)
        *   [Metrics](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/monitoring/metrics/)
            *   [Essential metrics](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/monitoring/metrics/essential/)
            *   [Enable metrics logging](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/monitoring/metrics/enable/)
            *   [Expose metrics](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/monitoring/metrics/expose/)
            *   [Metrics reference](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/monitoring/metrics/reference/)

        *   [Manage queries](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/monitoring/query-management/)
        *   [Manage connections](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/monitoring/connection-management/)
        *   [Manage background jobs](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/monitoring/background-jobs/)
        *   [Generate a report about the system](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/monitoring/neo4j-admin-report/)

    *   [Neo4j Admin and Neo4j CLI](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-neo4j-cli/)
    *   [Cypher Shell](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/cypher-shell/)
    *   [Procedures](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/procedures/)
    *   Changes, deprecations, and removals
        *   [Changes in Neo4j 2025-2026 series](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/changes-2025-2026/)
        *   [Current deprecations](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/deprecations/)
        *   [Breaking changes in Neo4j 2025.01](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/breaking-changes/)

    *   [Tutorials](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/tutorial/)
        *   [Importing data](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/tutorial/neo4j-admin-import/)
        *   [Setting up and using a composite database](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/tutorial/tutorial-composite-database/)
        *   [Fine-grained access control](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/tutorial/access-control/)
        *   [Configuring Neo4j Single Sign-On (SSO)](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/tutorial/tutorial-sso-configuration/)
        *   [Deploying a Neo4j cluster in a Docker container](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/tutorial/tutorial-clustering-docker/)

**Is this page helpful?**

[](https://neo4j.com/docs)
*   [Operations Manual](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/)
*   [Import](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/)

[Raise an issue](https://github.com/neo4j/docs-operations/issues/new/?title=Docs%20Feedback%20modules/ROOT/pages/import.adoc%20(ref:%20main)&body=%3E%20Do%20not%20include%20confidential%20information,%20personal%20data,%20sensitive%20data,%20or%20other%20regulated%20data.)

Import
======

`neo4j-admin database import` writes CSV data into Neo4j’s native file format as fast as possible.

 It also provides support for the Parquet file format.

You should use this tool when:

*   Import performance is important because you have a large amount of data (millions/billions of entities).

*   The database can be taken offline and you have direct access to one of the servers hosting your Neo4j DBMS.

*   The database is non-existent or empty and you need to perform the initial data load.

*   You need to update your graph with a large amount of data. In this case, importing data incrementally can be more performant than transactional insertion.

The incremental import can be done either within a single command or in stages. For details, see [Incremental import in a single command](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_incremental_import_in_a_single_command) and [Incremental import in stages](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#incremental-import-stages). 
*   The CSV data is clean/fault-free (nodes are not duplicated and relationships' start and end nodes exist). This tool can handle data faults but performance is not optimized. If your data has a lot of faults, it is recommended to clean it using a dedicated tool before import.

Other methods of importing data into Neo4j might be better suited to non-admin users:

*   Cypher® - CSV data can be bulk loaded via the Cypher command `LOAD CSV`. See [Cypher Manual → `LOAD CSV`](https://neo4j.com/docs/cypher-manual/current/clauses/load-csv/).

*   Graphical Tools - [Neo4j AuraDB → Importing data](https://neo4j.com/docs/aura/import/introduction).

Change Data Capture does **not** capture any data changes resulting from the use of `neo4j-admin database import`. See [Change Data Capture → Key considerations](https://neo4j.com/docs/cdc/current/get-started/self-managed/#non-tx-log-changes) for more information.

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_overview)Overview
------------------------------------------------------------------------------------------------------------

The `neo4j-admin database import` command has two modes both used for initial data import:

*   _full_ — used to import data into a non-existent empty database.

*   _incremental_ — used when import cannot be completed in a single _full_ import, by allowing the import to be a series of smaller imports.

The user running `neo4j-admin database import` must have `WRITE` capabilities into `server.directories.data` and `server.directories.log`.

This section describes the `neo4j-admin database import` option.

For information on `LOAD CSV`, see the [Cypher Manual → `LOAD CSV`](https://neo4j.com/docs/cypher-manual/current/clauses/load-csv). For in-depth examples of using the command `neo4j-admin database import`, refer to the [Tutorials → Importing data](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/tutorial/neo4j-admin-import/).

These are some things you need to keep in mind when creating your input files:

*   Fields are comma-separated by default but a different delimiter can be specified.

*   All files must use the same delimiter.

*   Multiple data sources can be used for both nodes and relationships.

*   A data source can optionally be provided using multiple files.

*   A separate file with a header that provides information on the data fields, must be the first specified file of each data source.

*   Fields without corresponding information in the header are not read.

*   UTF-8 encoding is used.

*   By default, the importer trims extra whitespace at the beginning and end of strings. Quote your data to preserve leading and trailing whitespaces.

Indexes and constraints

Indexes and constraints are not created during the import. Instead, you have to add these afterward (see [Cypher Manual → Indexes](https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/full-text-indexes/)).

You can use the `--schema` option to create and populate indexes and constraints during the import process. The option is available in the Enterprise Edition and works only for the block format. See [Provide indexes and constraints during import](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#indexes-constraints-import) for more information.

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-full)Full import
----------------------------------------------------------------------------------------------------------------------

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-syntax)Syntax

The syntax for importing a set of CSV files is:

```syntax
neo4j-admin database import full [-h] [--expand-commands] [--verbose] [--auto-skip-subsequent-headers[=true|false]]
                                 [--dry-run[=true|false]] [--ignore-empty-strings[=true|false]] [--ignore-extra-columns
                                 [=true|false]] [--legacy-style-quoting[=true|false]] [--normalize-types[=true|false]]
                                 [--overwrite-destination[=true|false]] [--profile[=true|false]]
                                 [--skip-bad-entries-logging[=true|false]] [--skip-bad-relationships[=true|false]]
                                 [--skip-duplicate-nodes[=true|false]] [--strict[=true|false]] [--trim-strings
                                 [=true|false]] [--additional-config=<file>] [--array-delimiter=<char>]
                                 [--bad-tolerance=<num>] [--delimiter=<char>] [--format=<format>]
                                 [--high-parallel-io=on|off|auto] [--id-type=string|integer|actual]
                                 [--input-encoding=<character-set>] [--input-type=csv|parquet]
                                 [--max-off-heap-memory=<size>] [--path-pattern-style=regex|glob|none]
                                 [--profile-results-path=<path>] [--property-shard-count=<propertyShardCount>]
                                 [--quote=<char>] [--read-buffer-size=<size>] [--report-file=<path>] [--schema=<path>]
                                 [--target-format=<format>] [--target-location=<path>] [--temp-path=<path>]
                                 [--threads=<num>] [--vector-delimiter=<char>] [--nodes=[<label>[:<label>]...=]
                                 <files>...]... [--relationships=[<type>=]<files>...]...
                                 [--multiline-fields=true|false|<path>[,<path>] [--multiline-fields-format=v1|v2]]
                                 <database>
```

[View all (3 more lines)](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/)

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_description)Description

High-speed initial import of fault-free data from CSV files into a non-existent or empty database.

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_parameters)Parameters

Table 1. `neo4j-admin database import full` parameters| Parameter | Description | Default |
| --- | --- | --- |
| `<database>` | Name of the database to import. If the database into which you import does not exist prior to importing, you must create it subsequently using `CREATE DATABASE`. | `neo4j` |

Some of the options below are marked as **Advanced**. These options should not be used for experimentation.

For more information, please contact Neo4j Professional Services.

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_options)Options

`neo4j-admin import` also supports the Parquet file format. You can use the parameter `--input-type=csv|parquet` to explicitly specify whether to use CSV or Parquet for the importer. If not defined, it defaults to CSV. The [examples](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-examples) for CSV can also be used with Parquet.

Table 2. `neo4j-admin database import full` options| Option | Description | Default | CSV | Parquet |
| --- | --- | --- | --- | --- |
| `--additional-config=<file>[1]` | Configuration file with additional configuration. |  |  |  |
| `--array-delimiter=<char>` | Delimiter character between array elements within a value in CSV data. Also accepts `TAB` and e.g. `U+20AC` for specifying a character using Unicode. * ASCII character — e.g. `--array-delimiter=";"`. * `\ID` — Unicode character with ID, e.g. `--array-delimiter="\59"`. * `U+XXXX` — Unicode character specified with 4 HEX characters, e.g. `--array-delimiter="U+20AC"`. * `\t` — horizontal tabulation (HT), e.g. `--array-delimiter="\t"`. For horizontal tabulation (HT), use `\t` or the Unicode character ID `\9`. Unicode character ID can be used if prepended by `\`. | `;` |  |  |
| `--auto-skip-subsequent-headers[=true|false]` | Automatically skip accidental header lines in subsequent files in file groups with more than one file. | `false` |  |  |
| `--bad-tolerance=<num>` | Number of bad entries before the import is aborted. The import process is optimized for error-free data. Therefore, cleaning the data before importing it is highly recommended. If you encounter any bad entries during the import process, you can set the number of bad entries to a specific value that suits your needs. However, setting a high value may affect the performance of the tool. | `-1 Changed in 2025.12` |  |  |
| `--delimiter=<char>` | Delimiter character between values in CSV data. Also accepts `TAB` and e.g. `U+20AC` for specifying a character using Unicode. * ASCII character — e.g. `--delimiter=","`. * `\ID` — Unicode character with ID, e.g. `--delimiter="\44"`. * `U+XXXX` — Unicode character specified with 4 HEX characters, e.g. `--delimiter="U+20AC"`. * `\t` — horizontal tabulation (HT), e.g. `--delimiter="\t"`. For horizontal tabulation (HT), use `\t` or the Unicode character ID `\9`. Unicode character ID can be used if prepended by `\`. | `,` |  |  |
| `--dry-run[=true|false][2]` | Introduced in 2026.02 Flag used to indicate that a dry run of the import should be performed, i.e. no data will actually be imported, only the validation of the various arguments and estimation of size of the import will be performed and reported. | `false` |  |  |
| `--expand-commands` | Allow command expansion in config value evaluation. |  |  |  |
| `--format=<format>` | Name of database format. The imported database will be created in the specified format or use the format set in the configuration. Valid formats are `standard`, `aligned`, `high_limit`, and `block`. |  |  |  |
| `-h, --help` | Show this help message and exit. |  |  |  |
| `--high-parallel-io=on|off|auto` | Ignore environment-based heuristics and indicate if the target storage subsystem can support parallel IO with high throughput or auto detect. Typically this is `on` for SSDs, large raid arrays, and network-attached storage. | `auto` |  |  |
| `--id-type=string|integer|actual` | Each node must provide a unique ID. This is used to find the correct nodes when creating relationships. Possible values are: * `string` — arbitrary strings for identifying nodes. * `integer` — arbitrary integer values for identifying nodes. * `actual` — (advanced) actual node IDs. | `string` |  |  |
| `--ignore-empty-strings[=true|false]` | Whether or not empty string fields, i.e. "" from input source are ignored, i.e. treated as null. | `false` |  |  |
| `--ignore-extra-columns[=true|false]` | If unspecified columns should be ignored during the import. | `false` |  |  |
| `--input-encoding=<character-set>` | Character set that input data is encoded in. | `UTF-8` |  |  |
| `--input-type=csv|parquet` | File type to import from. Can be csv or parquet. Defaults to csv. |  |  |  |
| `--legacy-style-quoting[=true|false]` | Whether or not a backslash-escaped quote e.g. \" is interpreted as an inner quote. | `false` |  |  |
| `--max-off-heap-memory=<size>` | Maximum memory that the command can use for page cache and various caching data structures to improve performance. Values can be plain numbers, such as 10000000, or, for example, 20G for 20 gigabytes, or 70%, which will amount to 70% of currently free memory on the machine. | `90%` |  |  |
| `--multiline-fields=true|false|<path>[,<path>]` | In v1, whether or not fields from an input source can span multiple lines, i.e. contain newline characters. Setting `--multiline-fields=true` can severely degrade the performance of the importer. Therefore, use it with care, especially with large imports. In v2, this option will specify the list of files that contain multiline fields. Files can also be specified using regular expressions. | `null` |  |  |
| `--multiline-fields-format=v1|v2` | Controls the parsing of input source that can span multiple lines, i.e. contain newline characters. When set to v1, the value for `--multiline-fields` can only be true or false. When set to v2, the value for `--multiline-fields` should be the list of files that contain multiline fields. | `null` |  |  |
| `--nodes=[<label>[:<label>]…​=]<files>…​` | Node CSV header and data. * Multiple files will be logically seen as one big file from the perspective of the importer. * The first line must contain the header. * Multiple data sources like these can be specified in one import, where each data source has its own header. * Files can also be specified using regular expressions. It is possible to import files from AWS S3 buckets, Google Cloud storage buckets, and Azure buckets using the appropriate URI as the path. For an example, see [Import data from CSV files using regular expression](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-multiple-input-files-regex-example). |  |  |  |
| `--normalize-types[=true|false]` | When `true`, non-array property values are converted to their equivalent Cypher types. For example, all integer values will be converted to 64-bit long integers. | `true` |  |  |
| `--overwrite-destination[=true|false]` | Delete any existing database files prior to the import. | `false` |  |  |
| `--path-pattern-style=regex|glob|none[3]` | Introduced in 2026.01 Pattern style to use for matching `--nodes` and `--relationships` files. Possible values are: * `glob` — allows you to write patterns like `/some/**/deep/**/nested/structure.*`. * `regex` — allows you to write regular expressions, i.e. `/some/nested/structure.*`. * `none` — you have to enumerate all the file paths exactly, i.e. `/some/content/structure1.csv,/some/content/structure2.csv`. | `regex` |  |  |
| `--profile[=true|false]` | Introduced in 2026.02 Capture a java flight recording for the entire duration of the import. | `false` |  |  |
| `--profile-results-path=<path>` | Introduced in 2026.02 Provide a path where to store java flight recordings captured with the `--profile` option. Requires `--profile` or `--profile=true` to be set to have an effect. |  |  |  |
| `--property-shard-count=<propertyShardCount>[4]` | Introduced in 2025.12 Enterprise edition Number of shards of property data that will be created, each shard will be its own database. When this value is `0`, it is the equivalent of running just a `FULL` import. | `0` |  |  |
| `--quote=<char> [5]` | Character to treat as a quotation mark for values in CSV data. For example, quotes can be escaped as per [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180) by doubling them. Thus `""` would be interpreted as a literal `"`. You cannot escape using `\`. | `"` |  |  |
| `--read-buffer-size=<size>` | Size of each buffer for reading input data. It has to be at least large enough to hold the biggest single value in the input data. The value can be a plain number or a byte units string, e.g. `128k`, `1m`. | `4194304` |  |  |
| `--relationships=[<type>=]<files>…​` | Relationship CSV header and data. * Multiple files will be logically seen as one big file from the perspective of the importer. * The first line must contain the header. * Multiple data sources like these can be specified in one import, where each data source has its own header. * Files can also be specified using regular expressions. It is possible to import files from AWS S3 buckets, Google Cloud storage buckets, and Azure buckets using the appropriate URI as the path. For an example, see [Import data from CSV files using regular expression](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-multiple-input-files-regex-example). |  |  |  |
| `--report-file=<path>` | File in which to store the report of the csv-import. The location of the import log file can be controlled using the `--report-file` option. If you run large imports of CSV files that have low data quality, the import log file can grow very large. For example, CSV files that contain duplicate node IDs, or that attempt to create relationships between non-existent nodes, could be classed as having low data quality. In these cases, you may wish to direct the output to a location that can handle the large log file. If you are running on a UNIX-like system and you are not interested in the output, you can get rid of it altogether by directing the report file to `/dev/null`. If you need to debug the import, it might be useful to collect the stack trace. This is done by using the `--verbose` option. | `import.report` |  |  |
| `--schema=<path>` | Enterprise edition Path to the file containing the Cypher commands for creating indexes and constraints during data import. It is possible to load commands from AWS S3 buckets, Google Cloud storage buckets, and Azure buckets using the appropriate URI as the path. |  |  |  |
| `--skip-bad-entries-logging[=true|false]` | When set to `true`, the details of bad entries are not written in the log. Disabling logging can improve performance when the data contains lots of faults. Cleaning the data before importing it is highly recommended because faults dramatically affect the tool’s performance even without logging. | `false` |  |  |
| `--skip-bad-relationships[=true|false]` | Whether or not to skip importing relationships that refer to missing node IDs, i.e. either start or end node ID/group referring to a node that was not specified by the node input data. Skipped relationships will be logged if they are within the limit of entities specified by `--bad-tolerance` and the `--skip-bad-entries-logging` option is disabled. | `false` |  |  |
| `--skip-duplicate-nodes[=true|false]` | Whether or not to skip importing nodes that have the same ID/group. In the event of multiple nodes within the same group having the same ID, the first encountered will be imported, whereas consecutive such nodes will be skipped. Skipped nodes will be logged if they are within the limit of entities specified by `--bad-tolerance` and the `--skip-bad-entries-logging` option is disabled. | `false` |  |  |
| `--strict[=true|false]` | Whether or not the lookup of nodes referred to from relationships needs to be checked strict. If disabled, most but not all relationships referring to non-existent nodes will be detected. If enabled all those relationships will be found but at the cost of lower performance. | `false` |  |  |
| `--target-format=<format>[4]` | Introduced in 2025.12 Enterprise edition Target format can be either a plain database directory/files structure (`database`) or a backup artifact (`backup`). Uses the `--temp-path` location to keep any intermediate state. | `database` |  |  |
| `--target-location=<path>[4]` | Introduced in 2025.12 Enterprise edition Location for target backup artifact data. Used together with `--target-format=backup`. |  |  |  |
| `--temp-path=<path>` | Introduced in 2025.04 Provide a path where to store temporary files that are created and deleted during import. If not specifically provided, the default temp path will be created inside the database directory of the imported database. |  |  |  |
| `--threads=<num>` | (advanced) Max number of worker threads used by the importer. Defaults to the number of available processors reported by the JVM. There is a certain amount of minimum threads needed so for that reason there is no lower bound for this value. For optimal performance, this value should not be greater than the number of available processors. |  |  |  |
| `--trim-strings[=true|false]` | Whether or not strings should be trimmed for whitespaces. | `false` |  |  |
| `--vector-delimiter=<char>` | Introduced in 2025.10 Delimiter character between vector coordinates within a value in CSV data. Also accepts `TAB` and e.g. `U+20AC` for specifying a character using Unicode. | `;` |  |  |
| `--verbose` | Enable verbose output. |  |  |  |
| [1](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_footnoteref_1). See [Neo4j Admin and Neo4j CLI → Configuration](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-neo4j-cli/#_configuration) for details. [2](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_footnoteref_2). See [Perform a dry run before importing data](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-full-dry-run) for details. [3](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_footnoteref_3). See [Using pattern style for matching `--nodes` and `--relationships` files](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-path-pattern-style) for details. [4](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_footnoteref_4). See [Property Sharding → Data ingestion](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/sharded-property-databases/data-ingestion/) for details. [5](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_footnoteref_5). To escape quotation marks in the CSV data, you should double the configured character. |

Heap size for the import

You want to set the maximum heap size to a relevant value for the import. This is done by defining the `HEAP_SIZE` environment parameter before starting the import. For example, 2G is an appropriate value for smaller imports.

If doing imports in the order of magnitude of 100 billion entities, 20G will be an appropriate value.

Record format

If your import data results in a graph that is larger than 34 billion nodes, 34 billion relationships, or 68 billion properties, you will need to configure the importer to use the `block` format. This is achieved by using the `format` option of the import command and setting the value to `block`:

Copied!

```shell
bin/neo4j-admin database import full --format=block
```

The `block` format is available in Enterprise Edition only.

Providing arguments in a file

All options can be provided in a file and passed to the command using the `@` prefix. This is useful when the command line becomes too long to manage. For example, the following command:

Copied!

```shell
bin/neo4j-admin database import full @/path/to/your/<args-filename> mydb
```

For more information, see [Picocli → AtFiles](https://picocli.info/#AtFiles) official documentation.

Using both a multi-value option and a positional parameter

When using both a multi-value option, such as `--nodes` and `--relationships`, and a positional parameter (for example, in `--additional-config neo4j.properties --nodes 0-nodes.csv mydatabase`), the `--nodes` option acts "greedy" and the next option, in this case, `mydatabase`, is pulled in via the nodes convertor.

This is a limitation of the underlying library, Picocli, and is not specific to Neo4j Admin. For more information, see [Picocli → Variable Arity Options and Positional Parameters](https://picocli.info/#_variable_arity_options_and_positional_parameters) official documentation.

To resolve the problem, use one of the following solutions:

*   Put the positional parameters first. For example, `mydatabase --nodes 0-nodes.csv`.

*   Put the positional parameters last, after `--` and the final value of the last multi-value option. For example, `nodes 0-nodes.csv — mydatabase`.

Importing from a cloud storage

The `--nodes` and `--relationships` options can also import files from AWS S3 buckets, Google Cloud storage buckets, and Azure buckets. For more information, see [Importing files from a cloud storage](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-files-from-cloud-storage).

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-examples)Examples

If importing to a database that has not explicitly been created before the import, it must be created subsequently in order to be used.

Assume that you have formatted your data as per [CSV header format](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-header-format) so that you have it in six different files:

1.   `movies_header.csv`

2.   `movies.csv`

3.   `actors_header.csv`

4.   `actors.csv`

5.   `roles_header.csv`

6.   `roles.csv`

#### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-full-dry-run)Perform a dry run before importing data

Introduced in 2026.02

Before performing the actual import, you can run a dry run to validate the input files and estimate the size of the import. The command does not write any data to the database.

Copied!

```shell
bin/neo4j-admin database import full --dry-run=true --nodes import/movies_header.csv,import/movies.csv \
--nodes import/actors_header.csv,import/actors.csv \
--relationships import/roles_header.csv,import/roles.csv
```

Example output

Neo4j version: 2026.02.2
Checking the contents of the following files:
Nodes:
  /path/to/neo4j-enterprise-2026.02.2/import/movies_header.csv
  /path/to/neo4j-enterprise-2026.02.2/import/movies.csv
  /path/to/neo4j-enterprise-2026.02.2/import/actors_header.csv
  /path/to/neo4j-enterprise-2026.02.2/import/actors.csv

Relationships:
  null:
  /path/to/neo4j-enterprise-2026.02.2/import/roles_header.csv
  /path/to/neo4j-enterprise-2026.02.2/import/roles.csv

Available resources:
  Total machine memory: 32.00GiB
  Free machine memory: 81.34MiB
  Max heap memory : 7.111GiB
  Max worker threads: 10
  Configured max memory: 88.11MiB
  High parallel IO: true

Cypher type normalization is enabled (disable with --normalize-types=false):
  Property type of 'year' normalized from 'int' --> 'long' in /path/to/neo4j-enterprise-2026.02.2/import/movies_header.csv
Estimated entity counts / sizes:
  Nodes: 6
    Labels: 8
    Total property count: 15
    Total properties size: 237B
  Relationships: 9
    Total property count: 9
    Total properties size: 108B

#### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_import_data_from_multiple_csv_files)Import data from multiple CSV files

The following command imports the three datasets:

Copied!

```shell
bin/neo4j-admin database import full --nodes import/movies_header.csv,import/movies.csv \
--nodes import/actors_header.csv,import/actors.csv \
--relationships import/roles_header.csv,import/roles.csv
```

#### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-multiple-input-files-regex-example)Import data from CSV files using regular expression

Assume that you want to include a header and then multiple files that match a pattern, e.g. containing numbers. In this case, a regular expression can be used. It is guaranteed that groups of digits will be sorted in numerical order, as opposed to lexicographic order.

For example:

Copied!

```shell
bin/neo4j-admin database import full --nodes import/node_header.csv,import/node_data_\d+\.csv
```

In many scripting languages, you must use double backslashes (`\\`) when defining regular expression patterns inside string literals. This is because a single backslash (`\`) is treated as an escape character.

#### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_import_data_from_csv_files_using_a_more_complex_regular_expression)Import data from CSV files using a more complex regular expression

For regular expression patterns containing commas, which is also the delimiter between files in a group, the pattern can be quoted to preserve the pattern.

For example:

Copied!

```shell
bin/neo4j-admin database import full --nodes import/node_header.csv,'import/node_data_\d{1,5}.csv' databasename
```

#### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-files-from-cloud-storage)Importing files from a cloud storage

In Neo4j 2025.03, new cloud integration settings are introduced to provide better support for deployment and management in cloud ecosystems. For details, refer to [Configuration settings → Cloud storage integration settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#_cloud_storage_integration_settings).

The following examples show how to import data stored in a cloud storage bucket using the `--nodes` and `--relationships` options.

AWS S3

Google cloud storage

Azure cloud storage

Neo4j uses the AWS SDK v2 to call the APIs on AWS using AWS URLs. Alternatively, you can override the endpoints so that the AWS SDK can communicate with alternative storage systems, such as Ceph, Minio, or LocalStack, using the system variables `aws.endpointUrls3`, `aws.endpointUrlS3`, or `aws.endpointUrl`, or the environments variables `AWS_ENDPOINT_URL_S3` or `AWS_ENDPOINT_URL`.

1.   Install the AWS CLI by following the instructions in the AWS official documentation — [Install the AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

2.   Create an S3 bucket and a directory to store the backup files using the AWS CLI:

Copied!   
```shell
aws s3 mb --region=us-east-1 s3://myBucket
aws s3api put-object --bucket myBucket --key myDirectory/
```  For more information on how to create a bucket and use the AWS CLI, see the AWS official documentation — [Use Amazon S3 with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-prereqs) and [Use high-level (s3) commands with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3.html). 
3.   Verify that the `~/.aws/config` file is correct by running the following command:

Copied!   
```shell
cat ~/.aws/config
```  The output should look like this: [default]
region=us-east-1  
4.   Configure the access to your AWS S3 bucket by setting the `aws_access_key_id` and `aws_secret_access_key` in the `~/.aws/credentials` file and, if needed, using a bucket policy. For example:

    1.   Use `aws configure set aws_access_key_id aws_secret_access_key` command to set your IAM credentials from AWS and verify that the `~/.aws/credentials` is correct:

Copied!   
```shell
cat ~/.aws/credentials
```  The output should look like this: [default]
aws_access_key_id=this.is.secret
aws_secret_access_key=this.is.super.secret  
    2.   Additionally, you can use a resource-based policy to grant access permissions to your S3 bucket and the objects in it. Create a policy document with the following content and attach it to the bucket. Note that both resource entries are important to be able to download and upload files.

Copied!   
```json
{
    "Version": "2012-10-17",
    "Id": "Neo4jBackupAggregatePolicy",
    "Statement": [
        {
            "Sid": "Neo4jBackupAggregateStatement",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::myBucket/*",
                "arn:aws:s3:::myBucket"
            ]
        }
    ]
}
```
[View all (5 more lines)](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/)   

5.   Run the `neo4j-admin database import` command to import your data from your AWS S3 storage bucket. The example assumes that you have data stored in the `myBucket/data` folder in your bucket.

Copied!   
```shell
bin/neo4j-admin database import full --nodes s3://myBucket/data/nodes.csv --relationships s3://myBucket/data/relationships.csv newdb
```  

1.   Ensure you have a Google account and a project created in the Google Cloud Platform (GCP).

    1.   Install the `gcloud` CLI by following the instructions in the Google official documentation — [Install the gcloud CLI](https://cloud.google.com/sdk/docs/install).

    2.   Create a service account and a service account key using Google official documentation — [Create service accounts](https://cloud.google.com/iam/docs/service-accounts-create) and [Creating and managing service account keys](https://cloud.google.com/iam/docs/keys-create-delete).

    3.   Download the JSON key file for the service account.

    4.   Set the `GOOGLE_APPLICATION_CREDENTIALS` and `GOOGLE_CLOUD_PROJECT` environment variables to the path of the JSON key file and the project ID, respectively:

Copied!   
```shell
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/keyfile.json"
export GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID
```  
    5.   Authenticate the `gcloud` CLI with the e-mail address of the service account you have created, the path to the JSON key file, and the project ID:

Copied!   
```shell
gcloud auth activate-service-account service-account@example.com --key-file=$GOOGLE_APPLICATION_CREDENTIALS --project=$GOOGLE_CLOUD_PROJECT
```  For more information, see the Google official documentation — [gcloud auth activate-service-account](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account). 
    6.   Create a bucket in the Google Cloud Storage using Google official documentation — [Create buckets](https://cloud.google.com/storage/docs/creating-buckets).

    7.   Verify that the bucket is created by running the following command:

Copied!   
```shell
gcloud storage ls
```  The output should list the created bucket. 

2.   Run the `neo4j-admin database import` command to import your data from your Google storage bucket. The example assumes that you have data stored in the `myBucket/data` folder in your bucket.

Copied!   
```shell
bin/neo4j-admin database import full --nodes gs://myBucket/data/nodes.csv --relationships gs://myBucket/data/relationships.csv newdb
```  

1.   Ensure you have an Azure account, an Azure storage account, and a blob container.

    1.   You can create a storage account using the Azure portal.

 For more information, see the Azure official documentation on [Create a storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal).

    2.   Create a blob container in the Azure portal.

 For more information, see the Azure official documentation on [Quickstart: Upload, download, and list blobs with the Azure portal](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal).

2.   Install the Azure CLI by following the instructions in the Azure official documentation — [Azure official documentation](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).

3.   Authenticate the neo4j or neo4j-admin process against Azure using the default Azure credentials.

 See the Azure official documentation on [default Azure credentials](https://learn.microsoft.com/en-us/java/api/com.azure.identity.defaultazurecredential?view=azure-java-stable) for more information.

Copied!   
```shell
az login
```  Then you should be ready to use Azure URLs in either neo4j or neo4j-admin. 
4.   To validate that you have access to the container with your login credentials, run the following commands:

Copied!   
```shell
# Upload a file:
az storage blob upload --file someLocalFile  --account-name accountName - --container someContainer --name remoteFileName  --auth-mode login

# Download the file
az storage blob download  --account-name accountName --container someContainer --name remoteFileName --file downloadedFile --auth-mode login

# List container files
az storage blob list  --account-name someContainer --container someContainer  --auth-mode login
```  
5.   Run the `neo4j-admin database import` command to import your data from your Azure blob storage container. The example assumes that you have data stored in the `myStorageAccount/myContainer/data` folder in your container.

Copied!   
```shell
bin/neo4j-admin database import full --nodes azb://myStorageAccount/myContainer/data/nodes.csv --relationships azb://myStorageAccount/myContainer/data/relationships.csv newdb
```  

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-incremental)Incremental import

Enterprise Edition
--------------------------------------------------------------------------------------------------------------------------------------------------------

Incremental import supports `block` format.

Incremental import allows you to incorporate large amounts of data in batches into the graph. You can run this operation as part of the initial data load when it cannot be completed in a single full import. Besides, you can update your graph by importing data incrementally, which is more performant than transactional insertion of such data.

Incremental import requires the use of `--force` and can be run on an existing database only.

You must stop your database, if you want to perform the incremental import within one command.

If you cannot afford a full downtime of your database, split the operation into several stages:

*   _prepare_ stage (offline)

*   _build_ stage (offline or read-only)

*   _merge_ stage (offline)

The database must be stopped for the `prepare` and `merge` stages. During the `build` stage, the database can be left online but put into read-only mode. For a detailed example, see [Incremental import in stages](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#incremental-import-stages).

It is highly recommended to back up your database before running the incremental import, as if the _merge_ stage fails, is aborted, or crashes, it may corrupt the database.

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-incremental-syntax)Syntax

The syntax for importing a set of CSV files incrementally is:

```syntax
neo4j-admin database import incremental [-h] [--expand-commands] [--force] [--update-all-matching-relationships]
                                        [--verbose] [--auto-skip-subsequent-headers[=true|false]] [--dry-run
                                        [=true|false]] [--ignore-empty-strings[=true|false]] [--ignore-extra-columns
                                        [=true|false]] [--legacy-style-quoting[=true|false]] [--normalize-types
                                        [=true|false]] [--profile[=true|false]] [--skip-bad-entries-logging
                                        [=true|false]] [--skip-bad-relationships[=true|false]] [--skip-duplicate-nodes
                                        [=true|false]] [--strict[=true|false]] [--trim-strings[=true|false]]
                                        [--additional-config=<file>] [--array-delimiter=<char>] [--bad-tolerance=<num>]
                                        [--delimiter=<char>] [--high-parallel-io=on|off|auto]
                                        [--id-type=string|integer|actual] [--input-encoding=<character-set>]
                                        [--input-type=csv|parquet] [--max-off-heap-memory=<size>]
                                        [--path-pattern-style=regex|glob|none] [--profile-results-path=<path>]
                                        [--property-shard-count=<propertyShardCount>] [--quote=<char>]
                                        [--read-buffer-size=<size>] [--report-file=<path>] [--schema=<path>]
                                        [--stage=all|prepare|build|merge] [--target-format=<format>]
                                        [--target-location=<path>] [--temp-path=<path>] [--threads=<num>]
                                        [--vector-delimiter=<char>] [--nodes=[<label>[:<label>]...=]<files>...]...
                                        [--relationships=[<type>=]<files>...]... [--multiline-fields=true|false|<path>[,
                                        <path>] [--multiline-fields-format=v1|v2]] <database>
```

[View all (4 more lines)](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/)

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_description_2)Description

Incremental import into an existing database.

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_usage_and_limitations)Usage and limitations

The importer works well on standalone servers.

To safely perform an incremental import in a clustered environment, follow these steps:

1.   Run the incremental import command on a single server in the cluster. This server can then be used as the [designated seeder](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/clustering/databases/#cluster-designated-seeder) from which other cluster members can copy the database.

2.   Reconfigure the database topology to a single primary by running the [`dbms.recreateDatabase()`](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/procedures/#procedure_dbms_recreateDatabase) procedure.

3.   Then stop the database using [STOP DATABASE](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/standard-databases/start-stop-databases/#manage-databases-stop).

4.   Perform the incremental import on the server that hosts the database.

5.   Then start the database with [START DATABASE](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/standard-databases/start-stop-databases/#manage-databases-start).

6.   Lastly, restore the desired database topology using [ALTER DATABASE](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/standard-databases/alter-databases/).

The incremental import command can be used to add:

*   New nodes with labels and properties.

Note that you must have node property uniqueness constraints in place for the property key and label combinations that form the primary key, or the uniquely identifiable nodes. Otherwise, the command will throw an error and exit. For more information, see [CSV header format](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-header-format). 
*   New relationships between existing or new nodes.

Starting from 2025.01, the incremental import command can also be used for:

*   Adding new properties to existing nodes or relationships.

*   Updating or deleting properties in nodes or relationships.

*   Updating or deleting labels in nodes.

*   Deleting existing nodes and relationships.

This is supported only by `block` format. See [Applying changes to data via CSV files](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_applying_changes_to_data_via_csv_files) for more information.

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_parameters_2)Parameters

Table 3. `neo4j-admin database import incremental` parameters| Parameter | Description | Default |
| --- | --- | --- |
| `<database>` | Name of the database to import. If the database into which you import does not exist prior to importing, you must create it subsequently using `CREATE DATABASE`. | `neo4j` |

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_options_2)Options

Table 4. `neo4j-admin database import incremental` options| Option | Description | Default | CSV | Parquet |
| --- | --- | --- | --- | --- |
| `--additional-config=<file>[6]` | Configuration file with additional configuration. |  |  |  |
| `--array-delimiter=<char>` | Delimiter character between array elements within a value in CSV data. Also accepts `TAB` and e.g. `U+20AC` for specifying a character using Unicode. * ASCII character — e.g. `--array-delimiter=";"`. * `\ID` — Unicode character with ID, e.g. `--array-delimiter="\59"`. * `U+XXXX` — Unicode character specified with 4 HEX characters, e.g. `--array-delimiter="U+20AC"`. * `\t` — horizontal tabulation (HT), e.g. `--array-delimiter="\t"`. For horizontal tabulation (HT), use `\t` or the Unicode character ID `\9`. Unicode character ID can be used if prepended by `\`. | `;` |  |  |
| `--auto-skip-subsequent-headers[=true|false]` | Automatically skip accidental header lines in subsequent files in file groups with more than one file. | `false` |  |  |
| `--bad-tolerance=<num>` | Number of bad entries before the import is aborted. The import process is optimized for error-free data. Therefore, cleaning the data before importing it is highly recommended. If you encounter any bad entries during the import process, you can set the number of bad entries to a specific value that suits your needs. However, setting a high value may affect the performance of the tool. | `-1 Changed in 2025.12` |  |  |
| `--delimiter=<char>` | Delimiter character between values in CSV data. Also accepts `TAB` and e.g. `U+20AC` for specifying a character using Unicode. * ASCII character — e.g. `--delimiter=","`. * `\ID` — Unicode character with ID, e.g. `--delimiter="\44"`. * `U+XXXX` — Unicode character specified with 4 HEX characters, e.g. `--delimiter="U+20AC"`. * `\t` — horizontal tabulation (HT), e.g. `--delimiter="\t"`. For horizontal tabulation (HT), use `\t` or the Unicode character ID `\9`. Unicode character ID can be used if prepended by `\`. | `,` |  |  |
| `--dry-run[=true|false][7]` | Introduced in 2026.02 Flag used to indicate that a dry run of the import should be performed, i.e. no data will actually be imported, only the validation of the various arguments and estimation of size of the import will be performed and reported. | `false` |  |  |
| `--expand-commands` | Allow command expansion in config value evaluation. |  |  |  |
| `--force` | Confirm incremental import by setting this flag. |  |  |  |
| `-h, --help` | Show this help message and exit. |  |  |  |
| `--high-parallel-io=on|off|auto` | Ignore environment-based heuristics and indicate if the target storage subsystem can support parallel IO with high throughput or auto detect. Typically this is `on` for SSDs, large raid arrays, and network-attached storage. | `auto` |  |  |
| `--id-type=string|integer|actual` | Each node must provide a unique ID. This is used to find the correct nodes when creating relationships. Possible values are: * `string` — arbitrary strings for identifying nodes. * `integer` — arbitrary integer values for identifying nodes. * `actual` — (advanced) actual node IDs. | `string` |  |  |
| `--ignore-empty-strings[=true|false]` | Whether or not empty string fields, i.e. "" from input source are ignored, i.e. treated as null. | `false` |  |  |
| `--ignore-extra-columns[=true|false]` | If unspecified columns should be ignored during the import. | `false` |  |  |
| `--input-encoding=<character-set>` | Character set that input data is encoded in. | `UTF-8` |  |  |
| `--input-type=csv|parquet` | File type to import from. Can be csv or parquet. Defaults to csv. |  |  |  |
| `--legacy-style-quoting[=true|false]` | Whether or not a backslash-escaped quote e.g. \" is interpreted as an inner quote. | `false` |  |  |
| `--max-off-heap-memory=<size>` | Maximum memory that the command can use for page cache and various caching data structures to improve performance. Values can be plain numbers, such as 10000000, or, for example, 20G for 20 gigabytes, or 70%, which will amount to 70% of currently free memory on the machine. | `90%` |  |  |
| `--multiline-fields=true|false|<path>[,<path>]` | In v1, whether or not fields from an input source can span multiple lines, i.e. contain newline characters. Setting `--multiline-fields=true` can severely degrade the performance of the importer. Therefore, use it with care, especially with large imports. In v2, this option will specify the list of files that contain multiline fields. Files can also be specified using regular expressions. | `null` |  |  |
| `--multiline-fields-format=v1|v2` | Controls the parsing of input source that can span multiple lines, i.e. contain newline characters. When set to v1, the value for `--multiline-fields` can only be true or false. When set to v2, the value for `--multiline-fields` should be the list of files that contain multiline fields. | `null` |  |  |
| `--nodes=[<label>[:<label>]…​=]<files>…​` | Node CSV header and data. * Multiple files will be logically seen as one big file from the perspective of the importer. * The first line must contain the header. * Multiple data sources like these can be specified in one import, where each data source has its own header. * Files can also be specified using regular expressions. It is possible to import files from AWS S3 buckets, Google Cloud storage buckets, and Azure buckets using the appropriate URI as the path. For an example, see [Import data from CSV files using regular expression](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-multiple-input-files-regex-example). |  |  |  |
| `--normalize-types[=true|false]` | When `true`, non-array property values are converted to their equivalent Cypher types. For example, all integer values will be converted to 64-bit long integers. | `true` |  |  |
| `--path-pattern-style=regex|glob|none[8]` | Introduced in 2026.01 Pattern style to use for matching `--nodes` and `--relationships` files. Possible values are: * `glob` — allows you to write patterns like `/some/**/deep/**/nested/structure.*`. * `regex` — allows you to write regular expressions, i.e. `/some/nested/structure.*`. * `none` — you have to enumerate all the file paths exactly, i.e. `/some/content/structure1.csv,/some/content/structure2.csv`. | `regex` |  |  |
| `--profile[=true|false]` | Introduced in 2026.02 Capture a java flight recording for the entire duration of the import. | `false` |  |  |
| `--profile-results-path=<path>` | Introduced in 2026.02 Provide a path where to store java flight recordings captured with the `--profile` option. Requires `--profile` or `--profile=true` to be set to have an effect. |  |  |  |
| `--property-shard-count=<propertyShardCount>[9]` | Introduced in 2025.12 Enterprise edition (advanced) Number of shards of property data that will be created, each shard will be its own database. Typically this option doesn’t need to be set at all, since the number of shards has already been decided during initial import. | `0` |  |  |
| `--quote=<char> [10]` | Character to treat as a quotation mark for values in CSV data. For example, quotes can be escaped as per [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180) by doubling them. Thus `""` would be interpreted as a literal `"`. You cannot escape using `\`. | `"` |  |  |
| `--read-buffer-size=<size>` | Size of each buffer for reading input data. It has to be at least large enough to hold the biggest single value in the input data. The value can be a plain number or a byte units string, e.g. `128k`, `1m`. | `4194304` |  |  |
| `--relationships=[<type>=]<files>…​` | Relationship CSV header and data. * Multiple files will be logically seen as one big file from the perspective of the importer. * The first line must contain the header. * Multiple data sources like these can be specified in one import, where each data source has its own header. * Files can also be specified using regular expressions. It is possible to import files from AWS S3 buckets, Google Cloud storage buckets, and Azure buckets using the appropriate URI as the path. For an example, see [Import data from CSV files using regular expression](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-multiple-input-files-regex-example). |  |  |  |
| `--report-file=<path>` | File in which to store the report of the csv-import. The location of the import log file can be controlled using the `--report-file` option. If you run large imports of CSV files that have low data quality, the import log file can grow very large. For example, CSV files that contain duplicate node IDs, or that attempt to create relationships between non-existent nodes, could be classed as having low data quality. In these cases, you may wish to direct the output to a location that can handle the large log file. If you are running on a UNIX-like system and you are not interested in the output, you can get rid of it altogether by directing the report file to `/dev/null`. If you need to debug the import, it might be useful to collect the stack trace. This is done by using the `--verbose` option. | `import.report` |  |  |
| `--schema=<path>` | Available from 2025.02 Path to the file containing the Cypher commands for creating indexes and constraints during data import. It is possible to load commands from AWS S3 buckets, Google Cloud storage buckets, and Azure buckets using the appropriate URI as the path. |  |  |  |
| `--skip-bad-entries-logging[=true|false]` | When set to `true`, the details of bad entries are not written in the log. Disabling logging can improve performance when the data contains lots of faults. Cleaning the data before importing it is highly recommended because faults dramatically affect the tool’s performance even without logging. | `false` |  |  |
| `--skip-bad-relationships[=true|false]` | Whether or not to skip importing relationships that refer to missing node IDs, i.e. either start or end node ID/group referring to a node that was not specified by the node input data. Skipped relationships will be logged if they are within the limit of entities specified by `--bad-tolerance` and the `--skip-bad-entries-logging` option is disabled. | `false` |  |  |
| `--skip-duplicate-nodes[=true|false]` | Whether or not to skip importing nodes that have the same ID/group. In the event of multiple nodes within the same group having the same ID, the first encountered will be imported, whereas consecutive such nodes will be skipped. Skipped nodes will be logged if they are within the limit of entities specified by `--bad-tolerance` and the `--skip-bad-entries-logging` option is disabled. | `false` |  |  |
| `--stage=all|prepare|build|merge` | Stage of incremental import. For incremental import into an existing database use `all` (which requires the database to be stopped). For semi-online incremental import run `prepare` (on a stopped database) followed by `build` (on a potentially running database) and finally `merge` (on a stopped database). | `all` |  |  |
| `--strict[=true|false]` | Whether or not the lookup of nodes referred to from relationships needs to be checked strict. If disabled, most but not all relationships referring to non-existent nodes will be detected. If enabled all those relationships will be found but at the cost of lower performance. | `false` |  |  |
| `--target-format=<format>[9]` | Introduced in 2025.12 Enterprise edition Target format can be either a plain database directory/files structure (`database`) or a backup artifact (`backup`). Uses the `--temp-path` location to keep any intermediate state. | `database` |  |  |
| `--target-location=<path>[9]` | Introduced in 2025.12 Enterprise edition Location for target backup artifact data. Used together with `--target-format=backup`. |  |  |  |
| `--temp-path=<path>` | Introduced in 2025.04 Provide a path where to store temporary files that are created and deleted during import. If not specifically provided, the default temp path will be created inside the database directory of the imported database. |  |  |  |
| `--threads=<num>` | (advanced) Max number of worker threads used by the importer. Defaults to the number of available processors reported by the JVM. There is a certain amount of minimum threads needed so for that reason there is no lower bound for this value. For optimal performance, this value should not be greater than the number of available processors. |  |  |  |
| `--trim-strings[=true|false]` | Whether or not strings should be trimmed for whitespaces. | `false` |  |  |
| `--vector-delimiter=<char>` | Introduced in 2025.10 Delimiter character between vector coordinates within a value in CSV data. Also accepts `TAB` and e.g. `U+20AC` for specifying a character using Unicode. | `;` |  |  |
| `--update-all-matching-relationships` | Introduced in 2025.01 Whether or not to update all existing relationships that match a relationship data entry. If disabled, the relationship data entry will be logged if it is within the limit of entities specified by `--bad-tolerance` and the `--skip-bad-entries-logging` option is disabled. | `false` |  |  |
| `--verbose` | Enable verbose output. |  |  |  |
| [6](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_footnoteref_6). See [Neo4j Admin and Neo4j CLI → Configuration](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-neo4j-cli/#_configuration) for details. [7](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_footnoteref_7). See [Perform a dry run before importing data](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-incremental-dry-run) for details. [8](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_footnoteref_8). See [Using pattern style for matching `--nodes` and `--relationships` files](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-path-pattern-style) for details. [9](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_footnoteref_9). See [Property Sharding → Data ingestion](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/scalability/sharded-property-databases/data-ingestion/) for details. [10](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_footnoteref_10). To escape quotation marks in the CSV data, you should double the configured character. |

Using both a multi-value option and a positional parameter

When using both a multi-value option, such as `--nodes` and `--relationships`, and a positional parameter (for example, in `--additional-config neo4j.properties --nodes 0-nodes.csv mydatabase`), the `--nodes` option acts "greedy" and the next option, in this case, `mydatabase`, is pulled in via the nodes convertor.

This is a limitation of the underlying library, Picocli, and is not specific to Neo4j Admin. For more information, see [Picocli → Variable Arity Options and Positional Parameters](https://picocli.info/#_variable_arity_options_and_positional_parameters) official documentation.

To resolve the problem, use one of the following solutions:

*   Put the positional parameters first. For example, `mydatabase --nodes 0-nodes.csv`.

*   Put the positional parameters last, after `--` and the final value of the last multi-value option. For example, `nodes 0-nodes.csv — mydatabase`.

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-incremental-examples)Examples

#### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-incremental-dry-run)Perform a dry run before importing data

Introduced in 2026.02

Before performing the actual import, you can run a dry run to validate the input files and estimate the size of the import. The command does not write any data to the database.

Copied!

```shell
neo4j@system> STOP DATABASE neo4j WAIT;
...
bin/neo4j-admin database import incremental --dry-run=true --nodes=N1=../../raw-data/incremental-import/nodes.csv --relationships=R1=../../raw-data/incremental-import/relationships.csv neo4j
```

Example output

Neo4j version: 2026.02.2
Checking the contents of the following files:
Nodes:
  /path/to/neo4j-enterprise-2026.02.2/raw-data/incremental-import/nodes.csv
Relationships:
  /path/to/neo4j-enterprise-2026.02.2/raw-data/incremental-import/relationships.csv

Available resources:
  Total machine memory: 64.00GiB
  Free machine memory: 9.997GiB
  Max heap memory : 14.22GiB
  Max worker threads: 10
  Configured max memory: 40.00GiB
  High parallel IO: true

Schema commands:
  Indexes to be created: 3
  Indexes to be dropped: 1
  Constraints to be created: 2
  Constraints to be dropped: 3

Estimated entity counts / sizes:
  Nodes: 2702496410
    Includes updates: true
    Labels: 2702496410
    Property count: 16348903762
    Property size: 253.6GiB
  Relationships: 18094004256
    Includes updates: false
    Property count: 6076138797
    Property size: 96.14GiB

There are two ways of importing data incrementally.

#### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_incremental_import_in_a_single_command)Incremental import in a single command

If downtime is not a concern, you can run a single command with the option `--stage=all`. This option requires the database to be stopped.

Copied!

```shell
neo4j@system> STOP DATABASE neo4j WAIT;
...
bin/neo4j-admin database import incremental --stage=all --nodes=N1=../../raw-data/incremental-import/nodes.csv --relationships=R1=../../raw-data/incremental-import/relationships.csv neo4j
```

#### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#incremental-import-stages)Incremental import in stages

If you cannot afford a full downtime of your database, you can run the import in three stages.

1.   `prepare` stage:

During this stage, the import tool analyzes the CSV headers and copies the relevant data over to the new increment database path. The import command is run with the option `--stage=prepare` and the database must be stopped. 

    1.   Using the `system` database, stop the database `neo4j` with the `WAIT` option to ensure a checkpoint happens before you run the incremental import command. The database must be stopped to run `--stage=prepare`.

Copied!   
```shell
STOP DATABASE neo4j WAIT
```  
    2.   Run the incremental import command with the `--stage=prepare` option:

Copied!   
```shell
bin/neo4j-admin database import incremental --stage=prepare --nodes=N1=../../raw-data/incremental-import/nodes.csv --relationships=R1=../../raw-data/incremental-import/relationships.csv neo4j
```  

2.   `build` stage:

During this stage, the import tool imports the data, deduplicates it, and validates it in the new increment database path. This is the longest stage and you can put the database in read-only mode to allow read access. The import command is run with the option `--stage=build`. 

    1.   Put the database in read-only mode:

Copied!   
```shell
ALTER DATABASE neo4j SET ACCESS READ ONLY
```  
    2.   Run the incremental import command with the `--stage=build` option:

Copied!   
```shell
bin/neo4j-admin database import incremental --stage=build --nodes=N1=../../raw-data/incremental-import/nodes.csv --relationships=R1=../../raw-data/incremental-import/relationships.csv neo4j
```  

3.   `merge` stage:

During this stage, the import tool merges the new with the existing data in the database. It also updates the affected indexes and upholds the affected property uniqueness constraints and property existence constraints. The import command is run with the option `--stage=merge` and the database must be stopped. It is not necessary to include the `--nodes` or `--relationships` options when using `--stage=merge`. 

    1.   Using the `system` database, stop the database `neo4j` with the `WAIT` option to ensure a checkpoint happens before you run the incremental import command.

Copied!   
```shell
STOP DATABASE neo4j WAIT
```  
    2.   Run the incremental import command with the `--stage=merge` option:

Copied!   
```shell
bin/neo4j-admin database import incremental --stage=merge neo4j
```  

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-header-format)CSV header format
-------------------------------------------------------------------------------------------------------------------------------------

The header file of each data source specifies how the data fields should be interpreted. You must use the same delimiter for the header file and the data files.

The header contains information for each field, with the format `<name>:<field_type>`. The `<name>` is used for properties and node IDs. In all other cases, the `<name>` part of the field is ignored.

Incremental import

When using [incremental import](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-incremental), you must have node property uniqueness constraints in place for the property key and label combinations that form the primary key, or the uniquely identifiable nodes. For example, importing nodes with a `Person` label that are uniquely identified with a `uuid` property key, the format of the header should be `uuid:ID{label:Person}`.

This is also true when working with multiple groups. For example, you can use `uuid:ID(Person){label:Person}`, where the relationship CSV data can refer to different groups for its `:START_ID` and `:END_ID`, just like the full import method.

*   For more information on constraints, see [Cypher Manual → Constraints](https://neo4j.com/docs/cypher-manual/current/constraints).

*   For examples of creating property uniqueness constraints, see [Cypher Manual → Create property uniqueness constraints](https://neo4j.com/docs/cypher-manual/current/constraints/managing-constraints/#create-property-uniqueness-constraints).

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_extended_header_support_for_parquet)Extended header support for Parquet

Introduced in 2025.04

In addition to the header format supported by the CSV import, the Parquet import supports name-mapping header files. Those files contain two rows of entries, where the first row represents the name (incl. optional type, id group, etc.), and the second row references the name of the original columns in the data files.

movie_header.csv

movie_header.csv

Copied!

```csv
movieId:ID,title,year:int,:LABEL
id,movie_title,year,label
```

If a header file is provided for a set of labels or a relationship type, the importer will ignore columns not mentioned in the headers.

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-header-format-nodes)Node files
------------------------------------------------------------------------------------------------------------------------------------

Files containing node data can have an `ID` field, a `LABEL` field, and properties.

ID
Each node must have a unique ID if it is to be connected by any relationships created in the import. Neo4j uses the IDs to find the correct nodes when creating relationships. Note that the ID has to be unique across all nodes within the group, regardless of their labels. The unique ID is persisted in a property whose name is defined by the `<name>` part of the field definition `<name>:ID`. If no such property `name` is defined, the unique ID will be used for the import but not be available for reference later. If no ID is specified, the node will be imported, but it will not be connected to other nodes during the import. When a property `name` is provided, that property type can be configured globally via the `--id-type` option (as for [Property data types](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-header-format-properties)).

 You can specify a different value ID type to be stored for a node property in its group using the option `id-type` in the header, e.g: `id:ID(MyGroup){label:MyLabel, id-type: int}`. This ID type overrides the global `--id-type` option. For example, the global `id-type` can be a string, but the nodes will have their IDs stored as `int` type in their ID properties. For more information, see [Storing a different value type for IDs in a group](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-id-types-header).

 A node header can also contain multiple `ID` columns, where the relationship data references the composite value of all those columns. This also implies using `string` as `id-type`. For each `ID` column, you can specify to store its values as different node properties. However, the composite value cannot be stored as a node property. For more information, see [Using multiple node IDs](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-multiple-ids).

LABEL
Read one or more labels from this field. Like array values, multiple labels are separated by `;`, or by the character specified with `--array-delimiter`. The max length of label names for block format is 16,383 characters.

Example 1. Define node files

You define the headers for movies in the _movies\_header.csv_ file. Movies have the properties `movieId`, `year`, and `title`. You also specify a field for labels.

Copied!

```csv
movieId:ID,title,year:int,:LABEL
```

You define three movies in the _movies.csv_ file. They contain all the properties defined in the header file. All the movies are given the label `Movie`. Two of them are also given the label `Sequel`.

Copied!

```csv
tt0133093,"The Matrix",1999,Movie
tt0234215,"The Matrix Reloaded",2003,Movie;Sequel
tt0242653,"The Matrix Revolutions",2003,Movie;Sequel
```

Similarly, you also define three actors in the _actors\_header.csv_ and _actors.csv_ files. They all have the properties `personId` and `name`, and the label `Actor`.

Copied!

```csv
personId:ID,name,:LABEL
```

Copied!

```csv
keanu,"Keanu Reeves",Actor
laurence,"Laurence Fishburne",Actor
carrieanne,"Carrie-Anne Moss",Actor
```

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-header-format-rels)Relationship files
-------------------------------------------------------------------------------------------------------------------------------------------

Files containing relationship data have three mandatory fields and can also have properties. The mandatory fields are:

TYPE
The relationship type to use for this relationship. The max length of relationship type names for block format is 16,383 characters.

START_ID
The ID of the start node for this relationship.

END_ID
The ID of the end node for this relationship.

The `START_ID` and `END_ID` refer to the unique node ID defined in one of the node data sources, as explained in the previous section. None of these take a name, e.g. if `<name>:START_ID` or `<name>:END_ID` is defined, the `<name>` part will be ignored. Nor do they take a `<field_type>`, e.g. if `:START_ID:int` or `:END_ID:int` is defined, the `:int` part does not have any meaning in the context of type information.

Example 2. Define relationships files

In this example, you assume that the two node files from the previous example are used together with the following relationships file.

You define relationships between actors and movies in the files _roles\_header.csv_ and _roles.csv_. Each row connects a start node and an end node with a relationship of relationship type `ACTED_IN`. Notice how you use the unique identifiers `personId` and `movieId` from the nodes files above. The name of the character that the actor is playing in this movie is stored as a `role` property on the relationship.

Copied!

```csv
:START_ID,role,:END_ID,:TYPE
```

Copied!

```csv
keanu,"Neo",tt0133093,ACTED_IN
keanu,"Neo",tt0234215,ACTED_IN
keanu,"Neo",tt0242653,ACTED_IN
laurence,"Morpheus",tt0133093,ACTED_IN
laurence,"Morpheus",tt0234215,ACTED_IN
laurence,"Morpheus",tt0242653,ACTED_IN
carrieanne,"Trinity",tt0133093,ACTED_IN
carrieanne,"Trinity",tt0234215,ACTED_IN
carrieanne,"Trinity",tt0242653,ACTED_IN
```

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-header-format-properties)Property data types
--------------------------------------------------------------------------------------------------------------------------------------------------

For properties, the `<name>` part of the field designates the property key, while the `<field_type>` part assigns a data type. You can have properties in both node data files and relationship data files. The max length of property keys for block format is 16,383 characters.

Use one of `int`, `long`, `float`, `double`, `boolean`, `byte`, `short`, `char`, `string`, `point`, `date`, `localtime`, `time`, `localdatetime`, `datetime`, `duration`, and `vector` (introduced in 2025.10) to designate the data type for properties. By default, types (except arrays) are converted to Cypher types. See [Cypher Manual → Property, structural, and constructed values](https://neo4j.com/docs/cypher-manual/current/values-and-types/property-structural-constructed).

This behavior can be disabled using the option `--normalize-types=false`. Normalizing types can require more space on disk, but avoids Cypher converting the type during queries. If no data type is given, this defaults to `string`.

To define an array type, append `[]` to the type. By default, array values are separated by `;`. A different delimiter can be specified with `--array-delimiter`. Arrays are not affected by the `--normalize-types` flag. For example, if you want a byte array to be stored as a Cypher long array, you must explicitly declare the property as `long[]`.

CSV-based import does not import empty arrays, because they cannot be distinguished from arrays that are set to `null`. However, the Parquet import distinguishes between them and will import empty arrays as empty arrays and `null` as `null`.

Boolean values are _true_ if they match exactly the text `true`. All other values are _false_. Values that contain the delimiter character need to be escaped by enclosing in double quotation marks, or by using a different delimiter character with the `--delimiter` option.

Example 3. Header format with data types

This example illustrates several different data types specified in the CSV header.

Copied!

```csv
:ID,name,joined:date,active:boolean,points:int
user01,Joe Soap,2017-05-05,true,10
user02,Jane Doe,2017-08-21,true,15
user03,Moe Know,2018-02-17,false,7
```

Special considerations for the `point` data type
A point is specified using the Cypher syntax for maps. The map allows the same keys as the input to the [Cypher Manual → Point function](https://neo4j.com/docs/cypher-manual/current/functions/spatial/). The point data type in the header can be amended with a map of default values used for all values of that column, e.g. `point{crs: 'WGS-84'}`. Specifying the header this way allows you to have an incomplete map in the value position in the data file. Optionally, a value in a data file may override default values from the header.

Example 4. Property format for `point` data type

This example illustrates various ways of using the `point` data type in the import header and the data files.

You are going to import the name and location coordinates for cities. First, you define the header as:

Copied!

```csv
:ID,name,location:point{crs:WGS-84}
```

You then define cities in the data file.

*   The first city’s location is defined using `latitude` and `longitude`, as expected when using the coordinate system defined in the header.

*   The second city uses `x` and `y` instead. This would normally lead to a point using the coordinate reference system `cartesian`. Since the header defines `crs:WGS-84`, that coordinate reference system will be used.

*   The third city overrides the coordinate reference system defined in the header and sets it explicitly to `WGS-84-3D`.

Copied!

```csv
:ID,name,location:point{crs:WGS-84}
city01,"Malmö","{latitude:55.6121514, longitude:12.9950357}"
city02,"London","{y:51.507222, x:-0.1275}"
city03,"San Mateo","{latitude:37.554167, longitude:-122.313056, height: 100, crs:'WGS-84-3D'}"
```

Note that all point maps are within double quotation marks `"` in order to prevent the enclosed `,` character from being interpreted as a column separator. An alternative approach would be to use `--delimiter='\t'` and reformat the file with tab separators, in which case the `"` characters are not required.

Copied!

```csv
:ID name    location:point{crs:WGS-84}
city01  Malmö   {latitude:55.6121514, longitude:12.9950357}
city02  London  {y:51.507222, x:-0.1275}
city03  San Mateo   {latitude:37.554167, longitude:-122.313056, height: 100, crs:'WGS-84-3D'}
```

Special considerations for temporal data types
The format for all temporal data types must be defined as described in [Cypher Manual → Temporal instants syntax](https://neo4j.com/docs/cypher-manual/current/values-and-types/temporal/#cypher-temporal-instants) and [Cypher Manual → Durations syntax](https://neo4j.com/docs/cypher-manual/current/values-and-types/temporal/#cypher-temporal-durations). Two of the temporal types, _Time_ and _DateTime_, take a time zone parameter that might be common between all or many of the values in the data file. It is therefore possible to specify a default time zone for _Time_ and _DateTime_ values in the header, for example: `time{timezone:+02:00}` and: `datetime{timezone:Europe/Stockholm}`. If no default time zone is specified, the default timezone is determined by the [`db.temporal.timezone`](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/#config_db.temporal.timezone) configuration setting. The default time zone can be explicitly overridden in the values in the data file.

Example 5. Property format for temporal data types

This example illustrates various ways of using the `datetime` data type in the import header and the data files.

First, you define the header with two _DateTime_ columns. The first one defines a time zone, but the second one does not:

Copied!

```csv
:ID,date1:datetime{timezone:Europe/Stockholm},date2:datetime
```

You then define dates in the data file.

*   The first row has two values that do not specify an explicit timezone. The value for `date1` will use the `Europe/Stockholm` time zone that was specified for that field in the header. The value for `date2` will use the configured default time zone of the database.

*   In the second row, both `date1` and `date2` set the time zone explicitly to be `Europe/Berlin`. This overrides the header definition for `date1`, as well as the configured default time zone of the database.

Copied!

```csv
1,2018-05-10T10:30,2018-05-10T12:30
2,2018-05-10T10:30[Europe/Berlin],2018-05-10T12:30[Europe/Berlin]
```

Special considerations for vector data types introduced in 2025.10

A vector is specified using the Cypher syntax for maps. The map must specify both the `coordinateType` and the `dimensions` of the vector. The `coordinateType` can be one of `byte`, `short`, `int`, `long`, `float`, or `double`. The `dimensions` must be between 1 and 4096, inclusive.

By default, vector values are separated by `;`. A different delimiter can be specified with `--vector-delimiter`.

The dimensions of each vector in the data must match what is specified in the header.

A vector in a header could for example look like this:

Copied!

```csv
:ID,"vector1:vector{coordinateType:byte,dimensions:4096}"
```

Note that quotation marks are necessary, since the `,` inside the map would otherwise be interpreted as a column delimiter.

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-id-spaces)Using ID spaces
-------------------------------------------------------------------------------------------------------------------------------

By default, the import tool assumes that node identifiers are unique across node files. In many cases, the ID is unique only across each entity file, for example, when your CSV files contain data extracted from a relational database and the ID field is pulled from the primary key column in the corresponding table. To handle this situation you define _ID spaces_. ID spaces are defined in the `ID` field of node files using the syntax `ID(<ID space identifier>)`. To reference an ID of an ID space in a relationship file, you use the syntax `START_ID(<ID space identifier>)` and `END_ID(<ID space identifier>)`.

Example 6. Define and use ID spaces

Define a `Movie-ID` ID space in the _movies\_header.csv_ file.

Copied!

```csv
movieId:ID(Movie-ID),title,year:int,:LABEL
```

Copied!

```csv
1,"The Matrix",1999,Movie
2,"The Matrix Reloaded",2003,Movie;Sequel
3,"The Matrix Revolutions",2003,Movie;Sequel
```

Define an `Actor-ID` ID space in the header of the _actors\_header.csv_ file.

Copied!

```csv
personId:ID(Actor-ID),name,:LABEL
```

Copied!

```csv
1,"Keanu Reeves",Actor
2,"Laurence Fishburne",Actor
3,"Carrie-Anne Moss",Actor
```

Now use the previously defined ID spaces when connecting the actors to movies.

Copied!

```csv
:START_ID(Actor-ID),role,:END_ID(Movie-ID),:TYPE
```

Copied!

```csv
1,"Neo",1,ACTED_IN
1,"Neo",2,ACTED_IN
1,"Neo",3,ACTED_IN
2,"Morpheus",1,ACTED_IN
2,"Morpheus",2,ACTED_IN
2,"Morpheus",3,ACTED_IN
3,"Trinity",1,ACTED_IN
3,"Trinity",2,ACTED_IN
3,"Trinity",3,ACTED_IN
```

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-multiple-ids)Using multiple node IDs
------------------------------------------------------------------------------------------------------------------------------------------

A node header can contain multiple `ID` columns.

Starting from 2025.07, the relationship data must then use a matching number of `START_ID` / `END_ID` columns as references to the composite value of those ID columns. This implies using `string` as `id-type`.

For each `ID` column, you can specify to store its values as different node properties. However, the composite value cannot be stored as a node property.

Incremental import doesn’t support the use of multiple node identifiers. This functionality is only available with a full import.

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_define_multiple_ids_as_node_properties)Define multiple IDs as node properties

1.   Define multiple `ID` columns in the node header.

nodes_header.csv nodes_header.csv Copied!   
```csv
:ID,:ID,name
```  nodes.csv nodes.csv Copied!   
```csv
aa,11,John
bb,22,Paul
```  
2.   Define the relationship between two established nodes.

relationships_header.csv Multiple ID columns Single ID column  Starting from 2025.07, you can use a matching number of `START_ID` and `END_ID` columns when defining the relationship. However, do not mix how to refer to composite IDs. Either all references must use a single `START_ID` and `END_ID` column or all references must use a matching number of them. relationships_header.csv Copied!   
```csv
:START_ID,:START_ID,:TYPE,:END_ID,:END_ID
```  relationships.csv relationships.csv Copied!   
```csv
aa,11,WORKS_WITH,bb,22
```    Now use both IDs when defining the relationship: relationships_header.csv relationships_header.csv Copied!   
```csv
:START_ID,:TYPE,:END_ID
```  relationships.csv relationships.csv Copied!   
```csv
aa11,WORKS_WITH,bb22
```      

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#multiple-IDs-Id-spaces)Define multiple IDs stored in ID spaces

1.   Define a `MyGroup` ID space in the _nodes\_header.csv_ file.

nodes_header.csv nodes_header.csv Copied!   
```csv
personId:ID(MyGroup),memberId:ID(MyGroup),name
```  nodes.csv nodes.csv Copied!   
```csv
aa,11,John
bb,22,Paul
```  
2.   Now use the defined ID space when connecting John with Paul, and use both IDs in the relationship.

relationships_header.csv Multiple ID columns Single ID column  Starting from 2025.07, you have to use a matching number of `START_ID` and `END_ID` columns when defining the relationship: relationships_header.csv Copied!   
```csv
:START_ID(MyGroup),:START_ID(MyGroup),:TYPE,:END_ID(MyGroup),:END_ID(MyGroup)
```  relationships.csv relationships.csv Copied!   
```csv
aa,11,WORKS_WITH,bb,22
```    relationships_header.csv relationships_header.csv Copied!   
```csv
:START_ID(MyGroup),:TYPE,:END_ID(MyGroup)
```  relationships.csv relationships.csv Copied!   
```csv
aa11,WORKS_WITH,bb22
```      

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-id-types-header)Storing a different value type for IDs in a group
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can control the ID type of the node property that will be stored by defining the `id-type` option in the header, for example, `:ID{id-type:long}`. The `id-type` option in the header overrides the global `--id-type` value provided to the command. This way, you can have property values of different types for different groups of nodes. For example, the global `id-type` can be a string, but some nodes can have their IDs stored as `long` type in their ID properties.

Example 7. Import nodes with different ID value types

persons_header.csv

persons_header.csv

Copied!

```csv
id:ID(GroupOne){id-type:long},name,:LABEL
```

persons.csv

persons.csv

Copied!

```csv
123,P1,Person
456,P2,Person
```

games_header.csv

games_header.csv

Copied!

```csv
id:ID(GroupTwo),name,:LABEL
```

games.csv

games.csv

Copied!

```csv
ABC,G1,Game
DEF,G2,Game
```

Import the nodes

Import the nodes

Copied!

```shell
neo4j_home$ --nodes persons.csv --nodes games.csv --id-type string
```

The `id` property of the nodes in the `persons` group will be stored as `long` type, while the `id` property of the nodes in the `games` group will be stored as `string` type, as the global `id-type` is a string.

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-path-pattern-style)Using pattern style for matching `--nodes` and `--relationships` files

Introduced in 2026.01
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The import tool supports three different pattern styles for matching `--nodes` and `--relationships` files using the `--path-pattern-style` argument of the import command. Pattern styles are `glob`, `regex`, and `none`. The default pattern style is `regex`.

`glob`
Use `glob` style pattern matching when you have a lot of data organized into a more nested folder structure, for example, data grouped together by years:

Copied!

```none
/data/invoices/2024/invoices_jan.csv
...
/data/invoices/2024/invoices_dec.csv
/data/invoices/2025/invoices_jan.csv
...
/data/invoices/2025/invoices_dec.csv
/data/invoices/2026/invoices_jan.csv
```

It allows you to import all the files via something like `/data/invoices/**/invoices_{jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec}.csv`.

`regex`
Use `regex` style pattern matching when you have a lot of data organized inside one folder. For example:

Copied!

```none
/data/invoices/invoices_2024_1.csv
/data/invoices/invoices_2024_2.csv
...
/data/invoices/invoices_2026_1.csv
```

It allows you to import all the files via something like `/data/invoices/invoices_\d+_\d.csv`.

`none`
Use `none` when you know the files and want to avoid pattern matching. For example, this is especially useful when your files are in the cloud, and using the other two options may incur unnecessary performance and financial cost.

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_applying_changes_to_data_via_csv_files)Applying changes to data via CSV files

Introduced in 2025.01.0
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can use CSV files to update existing nodes, relationships, labels, or properties during incremental import.

This feature is supported only by `block` format.

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_set_an_explicit_action_for_each_row)Set an explicit action for each row

You can set an explicit action for each row in the CSV file by using the `:ACTION` keyword in the header file. If no action is specified, the import tool works as in full import mode, creating new data.

The following actions are supported:

*   `empty` = `CREATE` (default)

*   `C`, `CREATE` - Creates new nodes and relationships, with or without properties, as well as labels.

*   `U`, `UPDATE` - Updates existing nodes, relationships, labels, and properties.

*   `D`, `DELETE` - Deletes existing nodes or relationships. Deleting a node also deletes its relationships (`DETACH DELETE`).

Using actions in CSV files to update nodes

Using actions in CSV files to update nodes

```cypher
:ACTION,uid:ID(label:Person),name,:LABEL
CREATE,person1,"Keanu Reeves",Actor
UPDATE,person2,"Laurence Fishburne",Actor
DELETE,person4,,
```

Nodes are identified by their unique property value for the key/label combination that the header specifies.

Using actions in CSV files to update relationships

Using actions in CSV files to update relationships

```cypher
:ACTION,:START_ID,:END_ID,:TYPE,role
CREATE,person1,movie1,ACTED_IN,"Neo"
UPDATE,person2,movie1,ACTED_IN,"Morpheus"
DELETE,person3,movie1,ACTED_IN
```

Relationships are identified non-uniquely by their start and end node IDs, and their type.

To further narrow down selection you can tag a property column as an identifier to help out in selecting relationships uniquely (or at least more uniquely).

Using actions in CSV files to update relationships with identifier properties

Using actions in CSV files to update relationships with identifier properties

```cypher
:ACTION,:START_ID,:TYPE,:END_ID,p1{identifier:true},name,p4
U,person1,KNOWS,person2,abc,"Keanu Reeves","Hello Morpheus"
U,person2,KNOWS,person1,def,"Laurence Fishburne","Hello Neo"
```

The data in the `p1` column for these relationships helps select relationships "more uniquely" if a multiple of `1,KNOWS,2` exists. There can also be multiple identifier properties defined in the header. Identifier properties match the selected relationships and will not be set on the relationships that already have them.

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_update_existing_labels)Update existing labels

You can add or remove one or more labels from an existing node by prepending the clause `LABEL` in the header with a `+` (default) or `-`:

*   `:+LABEL` - Add one or more labels to an existing node.

*   `:-LABEL` - Remove one or more labels (if they exist) from an existing node.

For example, a file could have the following format:

Copied!

```csv
uid:ID(label:Person),:+LABEL,:-LABEL,name,age
person1,Actor,Producer,"Keanu Reeves",55
person2,Actor;Director,,"Laurence Fishburne",60
```

In this case, all labels in the second column are added and all the labels in the third column are removed (if they exist).

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_remove_existing_properties)Remove existing properties

You can remove properties from existing nodes or relationships by a `:-PROPERTY` column in the header. In the contents of this field you can add zero or more property names to remove from the entity. For example:

Remove nodes' properties

Remove nodes' properties

```cypher
:ACTION,uid:ID(label:Person),:-PROPERTY
U,person1,age;hometown
```

Properties `age` and `hometown` are removed from the node with the `uid:ID``person1`.

Remove relationships' properties

Remove relationships' properties

```cypher
:ACTION,:START_ID,:END_ID,:TYPE,:-PROPERTY
U,person1,movie1,ACTED_IN,role;description
```

Properties `role` and `description` are removed from the relationship with the `:START_ID``person1`, `:END_ID``movie1`, and `:TYPE``ACTED_IN`.

Using actions in CSV files to update labels and properties

Using actions in CSV files to update labels and properties

```cypher
:ACTION,uid:ID(label:Person),:LABEL,:-LABEL,:-PROPERTY,name,height:int
U,person1,Actor,Producer,age;hometown,Henry",185
```

One CSV entry can specify all types of updates to one entity at the same time. In this example, the node `person1` is updated with:

*   added `Actor` label

*   removed `Producer` label

*   removed `age` and `hometown` properties

*   set `name="Henry"` property

*   set `height=185` property

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_importing_data_that_spans_multiple_lines)Importing data that spans multiple lines
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `--multiline-fields` option allows fields from an input source to span multiple lines, i.e. contain newline characters. For example:

Copied!

```shell
bin/neo4j-admin database import full --nodes import/node_header.csv,import/node_data.csv --multiline-fields=true databasename
```

Where `import/node_data.csv` contains multiline fields, such as:

```csv
id,name,birthDate,birthYear,birthLocation,description
1,John,October 1st,2000,New York,This is a multiline
description
```

Setting `--multiline-fields=true` can severely degrade the performance of the importer. Therefore, use it with care, especially with large imports.

Optionally, you can specify the format of the `--multiline-fields` to control the parsing of the input source by setting the `--multiline-fields-format` option. Possible values are:

*   `v1` - the default format, which uses the current processing method for multiline fields.

*   `v2` - a more efficient processing method that requires text fields to be quoted. For `v2`, the `--multiline-fields` option must be set to a list of files (regular expressions are allowed) that contain multiline fields.

Both formats have the restriction that the entirety of every row must be able to fit into the buffer (default is 4m). The `--multiline-fields-format` option is available in the `full` and `incremental` import modes.

For example:

Multiline fields format v1

Multiline fields format v2

Copied!

```shell
bin/neo4j-admin database import full --nodes import/node_header.csv,import/node_data.csv --multiline-fields=true --multiline-fields-format=v1 databasename
```

Where `import/node_data.csv` contains multiline fields, such as:

```csv
id,name,birthDate,birthYear,birthLocation,description
1,John,October 1st,2000,New York,This is a multiline
description
```

Copied!

```shell
bin/neo4j-admin database import full --nodes import/node_header.csv,import/node_data.csv --multiline-fields=import/node_data.csv --multiline-fields-format=v2 databasename
```

Where `import/node_data.csv` contains multiline fields, such as:

```csv
id,name,birthDate,birthYear,birthLocation,description
1,"John","October 1st",2000,"New York","This is a multiline
description"
```

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-header-format-skip-columns)Skipping columns
-------------------------------------------------------------------------------------------------------------------------------------------------

IGNORE
If there are fields in the data that you wish to ignore completely, this can be done using the `IGNORE` keyword in the header file. `IGNORE` must be prepended with a `:`.

Example 8. Skip a column

In this example, you are not interested in the data in the third column of the nodes file and wish to skip over it. Note that the `IGNORE` keyword is prepended by a `:`.

Copied!

```csv
personId:ID,name,:IGNORE,:LABEL
```

Copied!

```csv
keanu,"Keanu Reeves","male",Actor
laurence,"Laurence Fishburne","male",Actor
carrieanne,"Carrie-Anne Moss","female",Actor
```

If all your superfluous data is placed in columns located to the right of all the columns that you wish to import, you can instead use the command line option `--ignore-extra-columns`.

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-header-format-compressed-files)Importing compressed files
---------------------------------------------------------------------------------------------------------------------------------------------------------------

The import tool can handle files compressed with `zip` or `gzip`. Each compressed file must contain a single file.

Example 9. Perform an import using compressed files

Copied!

```sh
neo4j_home$ ls import
actors-header.csv  actors.csv.zip  movies-header.csv  movies.csv.gz  roles-header.csv  roles.csv.gz
```

Copied!

```sh
bin/neo4j-admin database import --nodes import/movies-header.csv,import/movies.csv.gz --nodes import/actors-header.csv,import/actors.csv.zip --relationships import/roles-header.csv,import/roles.csv.gz
```

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#indexes-constraints-import)Create/Drop indexes and constraints during import

Enterprise Edition
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can use the `--schema` option to create and populate indexes/constraints during full and incremental import by providing a Cypher script containing `CREATE INDEX|CONSTRAINT` commands. During an incremental import, you can also use the same option to drop indexes/constraints, provided that the Cypher script contains `DROP INDEX|CONSTRAINT` commands.

The `--schema` option works only for `block` store format. For incremental import, creating and dropping indexes and constraints are available from 2025.02.

The import tool supports the following indexes and constraints:

*   RANGE

*   LOOKUP

*   POINT

*   TEXT

*   FULL-TEXT

*   VECTOR

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_create_indexes_and_constraints_during_full_import)Create indexes and constraints during full import

You can use the `--schema` option to create and populate indexes/constraints during full import by providing a Cypher script containing `CREATE INDEX|CONSTRAINT` commands to be parsed and executed.

Full import does not support dropping indexes and constraints.

For example:

_schema.cypher_ script

_schema.cypher_ script

```cypher
CREATE INDEX PersonNameIndex IF NOT EXISTS FOR (p:Person) ON (p.name);
CREATE CONSTRAINT PersonAgeConstraint IF NOT EXISTS FOR (c:Person) REQUIRE c.age IS :: INTEGER;
```

This file uses ';' as a separator.

Then use the following example commands to run the import:

Copied!

```shell
bin/neo4j-admin database import full neo4j --nodes=import/movies.csv --nodes=import/actors.csv --relationships=import/roles.csv --schema=import/schema.cypher
```

### [](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_create_and_drop_indexes_and_constraints_during_incremental_import)Create and drop indexes and constraints during incremental import

Introduced in 2025.02

You can use the `--schema` option to create and populate, and drop indexes/constraints during an incremental import by providing a Cypher script containing `CREATE INDEX|CONSTRAINT` and `DROP INDEX|CONSTRAINT` commands to be parsed and executed. Note that you cannot drop indexes that are backing constraints. You must drop the constraints themselves, which will also drop the underlying indexes.

You must stop your database before performing an incremental import with a single command. If you cannot afford a full downtime of your database, split the operation into several stages. See [Incremental import in stages](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#incremental-import-stages) for details.

For example:

_schema.cypher_ script

_schema.cypher_ script

```cypher
DROP INDEX PersonNameIndex IF EXISTS;
CREATE CONSTRAINT person_name IF NOT EXISTS FOR (p:Person) REQUIRE p.name IS UNIQUE;
DROP CONSTRAINT PersonAgeConstraint IF EXISTS;
CREATE CONSTRAINT movie_title IF NOT EXISTS FOR (m:Movie) REQUIRE m.title IS UNIQUE;
```

This file uses ';' as a separator.

Then use the following example commands to run the import:

Copied!

```shell
bin/neo4j-admin database import incremental --stage=all --nodes=import/movies.csv --nodes=import/actors.csv --relationships=import/roles.csv --schema=import/schema.cypher
```

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-resume)Resuming a stopped or canceled import

Enterprise Edition
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

An import that is stopped or fails before completing can be resumed from a point closer to where it was stopped. An import can be resumed from the following points:

*   Linking of relationships

*   Post-processing

[](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-diagnose-performance-issues)Diagnosing performance issues with Java Flight Recorder (JFR)

Introduced in 2026.02
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `--profile` option runs a JFR recording for the entire duration of the import and captures JVM performance data for analysis. This option can be especially useful for long running and resource intensive imports.

To use this option, add `--profile` or `--profile=true` to your import command. For example:

Run a full import with JFR recording

Run a full import with JFR recording

Copied!

```shell
bin/neo4j-admin database import full --nodes import/movies_header.csv,import/movies.csv \
--nodes import/actors_header.csv,import/actors.csv \
--relationships import/roles_header.csv,import/roles.csv \
--profile=true
```

Optionally, you can specify a path where to store the generated Java flight recording using the `--profile-results-path` option. If not specified, the recording will be stored in the _logs_ folder.

[Configuration settings](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/configuration/configuration-settings/)[Database administration](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/database-administration/)

Contents
--------

*   [Overview](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_overview)
*   [Full import](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-full)
*   [Syntax](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-syntax)
*   [Description](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_description)
*   [Parameters](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_parameters)
*   [Options](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_options)
*   [Examples](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-examples)
*   [Incremental import](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-incremental)
*   [Syntax](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-incremental-syntax)
*   [Description](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_description_2)
*   [Usage and limitations](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_usage_and_limitations)
*   [Parameters](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_parameters_2)
*   [Options](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_options_2)
*   [Examples](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-incremental-examples)
*   [CSV header format](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-header-format)
*   [Extended header support for Parquet](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_extended_header_support_for_parquet)
*   [Node files](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-header-format-nodes)
*   [Relationship files](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-header-format-rels)
*   [Property data types](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-header-format-properties)
*   [Using ID spaces](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-id-spaces)
*   [Using multiple node IDs](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-multiple-ids)
*   [Define multiple IDs as node properties](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_define_multiple_ids_as_node_properties)
*   [Define multiple IDs stored in ID spaces](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#multiple-IDs-Id-spaces)
*   [Storing a different value type for IDs in a group](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-id-types-header)
*   [Using pattern style for matching `--nodes` and `--relationships` files](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-path-pattern-style)
*   [Applying changes to data via CSV files](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_applying_changes_to_data_via_csv_files)
*   [Set an explicit action for each row](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_set_an_explicit_action_for_each_row)
*   [Update existing labels](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_update_existing_labels)
*   [Remove existing properties](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_remove_existing_properties)
*   [Importing data that spans multiple lines](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_importing_data_that_spans_multiple_lines)
*   [Skipping columns](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-header-format-skip-columns)
*   [Importing compressed files](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-header-format-compressed-files)
*   [Create/Drop indexes and constraints during import](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#indexes-constraints-import)
*   [Create indexes and constraints during full import](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_create_indexes_and_constraints_during_full_import)
*   [Create and drop indexes and constraints during incremental import](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#_create_and_drop_indexes_and_constraints_during_incremental_import)
*   [Resuming a stopped or canceled import](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-resume)
*   [Diagnosing performance issues with Java Flight Recorder (JFR)](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/neo4j-admin-import/#import-tool-diagnose-performance-issues)

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

![Image 3](blob:https://neo4j.com/77c6d16b-1017-4d3c-8bcc-edd622b670c0)
