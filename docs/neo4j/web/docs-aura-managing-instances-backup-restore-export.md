# Source: https://neo4j.com/docs/aura/managing-instances/backup-restore-export/

Title: Backup, export, restore, and upload - Neo4j Aura

URL Source: https://neo4j.com/docs/aura/managing-instances/backup-restore-export/

Markdown Content:
Backup, export, restore, and upload - Neo4j Aura
===============

This website uses cookies

We use cookies to offer you a better browsing experience, analyze site traffic, personalize content and serve targeted ads. Learn about how we use cookies and how you can control them in [Cookie Settings](https://neo4j.com/neo4j-cookie-and-tracking-policy/). By using our site. you consent to our use of cookies.

[Accept Cookies](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#)[Use necessary cookies only](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#)

[![Image 1: Neo4j Docs](https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg)](https://neo4j.com/)[Docs](https://neo4j.com/docs/)

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

[Search](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#search)

[Skip to content](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#skip-to-content "Skip to content")

Neo4j Aura

*       *    Neo4j Aura 
    *   Introduction
        *   [About Aura](https://neo4j.com/docs/aura/)
        *   [New Neo4j Aura console](https://neo4j.com/docs/aura/new-console/)
        *   [Visual tour](https://neo4j.com/docs/aura/visual-tour/)

    *   Quick start
        *   [Create an account](https://neo4j.com/docs/aura/getting-started/create-account/)
        *   [Create a project](https://neo4j.com/docs/aura/getting-started/create-project/)
        *   [Create an instance](https://neo4j.com/docs/aura/getting-started/create-instance/)
        *   [Connect to an instance](https://neo4j.com/docs/aura/getting-started/connect-instance/)
        *   [Migrate metadata](https://neo4j.com/docs/aura/getting-started/migrate-metadata/)

    *   [Cloud provider marketplaces](https://neo4j.com/docs/aura/cloud-providers/)
    *   Manage instances
        *   [Instance actions](https://neo4j.com/docs/aura/managing-instances/instance-actions/)
        *   [Instance details](https://neo4j.com/docs/aura/managing-instances/instance-details/)
        *   [Self-managed instances](https://neo4j.com/docs/aura/managing-instances/self-managed/)
        *   [Secondaries](https://neo4j.com/docs/aura/managing-instances/secondaries/)
        *   [Resources](https://neo4j.com/docs/aura/managing-instances/instance-resources/)
        *   [Custom endpoints](https://neo4j.com/docs/aura/managing-instances/custom-endpoints/)
        *   [Migration Readiness Report](https://neo4j.com/docs/aura/managing-instances/migration-readiness/)
        *   [Develop](https://neo4j.com/docs/aura/managing-instances/develop/)
        *   [Regions](https://neo4j.com/docs/aura/managing-instances/regions/)
        *   [Backup, export, and restore](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/)
        *   [Vector optimization](https://neo4j.com/docs/aura/managing-instances/vector-optimization/)
        *   [Cypher version](https://neo4j.com/docs/aura/managing-instances/cypher-version/)

    *   Import data
        *   [What is Import?](https://neo4j.com/docs/aura/import/introduction/)
        *   [Quick start](https://neo4j.com/docs/aura/import/quick-start/)
        *   [Visual tour](https://neo4j.com/docs/aura/import/visual-tour/)
        *   [Data provision](https://neo4j.com/docs/aura/import/file-provision/)
        *   [Model data](https://neo4j.com/docs/aura/import/modeling/)
        *   [Map data](https://neo4j.com/docs/aura/import/mapping/)
        *   [Indexes and constraints](https://neo4j.com/docs/aura/import/indexes-and-constraints/)
        *   [Run the import](https://neo4j.com/docs/aura/import/import/)

    *   Graph analytics in Aura
        *   [Overview](https://neo4j.com/docs/aura/graph-analytics/)
        *   [Aura Graph Analytics](https://neo4j.com/docs/aura/graph-analytics/aga/)
        *   [Alternative deployment options](https://neo4j.com/docs/aura/graph-analytics/alternative-deployments/)

    *   [Aura Agent](https://neo4j.com/docs/aura/aura-agent/)
    *   Explore data
        *   [What is Explore?](https://neo4j.com/docs/aura/explore/introduction/)
        *   [Quick start](https://neo4j.com/docs/aura/explore/explore-quick-start/)
        *   Visual tour
            *   [Explore overview](https://neo4j.com/docs/aura/explore/explore-visual-tour/explore-overview/)
            *   [Perspective drawer](https://neo4j.com/docs/aura/explore/explore-visual-tour/perspective-drawer/)
            *   [Legend panel](https://neo4j.com/docs/aura/explore/explore-visual-tour/legend-panel/)
            *   [Search bar](https://neo4j.com/docs/aura/explore/explore-visual-tour/search-bar/)
            *   [Card list](https://neo4j.com/docs/aura/explore/explore-visual-tour/card-list/)
            *   [Scene interactions](https://neo4j.com/docs/aura/explore/explore-visual-tour/scene-interactions/)

        *   Perspectives
            *   [Perspectives - A business view of the graph](https://neo4j.com/docs/aura/explore/explore-perspectives/perspectives/)
            *   [Creation and use](https://neo4j.com/docs/aura/explore/explore-perspectives/perspective-creation/)
            *   [Refresh Perspectives](https://neo4j.com/docs/aura/explore/explore-perspectives/refresh-perspectives/)
            *   [Database scans](https://neo4j.com/docs/aura/explore/explore-perspectives/database-scans/)

        *   Explore features in detail
            *   [Graph pattern search](https://neo4j.com/docs/aura/explore/explore-features/graph-pattern-search/)
            *   [Search phrases for advanced queries](https://neo4j.com/docs/aura/explore/explore-features/search-phrases-advanced/)
            *   [Scene actions](https://neo4j.com/docs/aura/explore/explore-features/scene-actions/)
            *   [Full-text search](https://neo4j.com/docs/aura/explore/explore-features/full-text-search/)
            *   [Edit graph data](https://neo4j.com/docs/aura/explore/explore-features/edit-graph-data/)
            *   [Graph Data Science integration](https://neo4j.com/docs/aura/explore/explore-features/gds-integration/)
            *   [Slicer](https://neo4j.com/docs/aura/explore/explore-features/slicer/)

        *   [Default actions and shortcuts](https://neo4j.com/docs/aura/explore/explore-default-actions/)

    *   Query data
        *   [What is Query?](https://neo4j.com/docs/aura/query/introduction/)
        *   [Visual tour](https://neo4j.com/docs/aura/query/visual-tour/)
        *   [Query operations](https://neo4j.com/docs/aura/query/operations/)
        *   [Command reference](https://neo4j.com/docs/aura/query/command-reference/)

    *   Fleet management
        *   [Overview](https://neo4j.com/docs/aura/fleet-management/overview/)
        *   [Add a deployment](https://neo4j.com/docs/aura/fleet-management/setup/)
        *   [Inspect deployment](https://neo4j.com/docs/aura/fleet-management/inspect-deployment/)
        *   [Deployment details](https://neo4j.com/docs/aura/fleet-management/deployment-details/)
        *   [Plugin procedures](https://neo4j.com/docs/aura/fleet-management/procedures/)
        *   [Data transparency](https://neo4j.com/docs/aura/fleet-management/data/)
        *   [Aura API](https://neo4j.com/docs/aura/fleet-management/aura-api/)
        *   [Aura CLI](https://neo4j.com/docs/aura/fleet-management/aura-cli/)

    *   [APOC support](https://neo4j.com/docs/aura/apoc/)
    *   Aura CLI
        *   [Introduction](https://neo4j.com/docs/aura/aura-cli/)
        *   [Installation](https://neo4j.com/docs/aura/aura-cli/installation/)
        *   [Initial configuration](https://neo4j.com/docs/aura/aura-cli/initial-configuration/)
        *   [Working with AuraDB tenants](https://neo4j.com/docs/aura/aura-cli/auradb-tenants/)
        *   [Managing AuraDB instances](https://neo4j.com/docs/aura/aura-cli/auradb-instances/)
        *   [Configuration](https://neo4j.com/docs/aura/aura-cli/configuration/)
        *   [Migration](https://neo4j.com/docs/aura/aura-cli/migration/)

    *   Dashboards
        *   [Overview](https://neo4j.com/docs/aura/dashboards/)
        *   [Create dashboards with AI](https://neo4j.com/docs/aura/dashboards/create-dashboards-with-ai/)
        *   [Create dashboards with Cypher](https://neo4j.com/docs/aura/dashboards/create-dashboards-manually/)
        *   [Managing dashboards](https://neo4j.com/docs/aura/dashboards/managing-dashboards/)
        *   [Import and export](https://neo4j.com/docs/aura/dashboards/import/)
        *   [Parameters and filters](https://neo4j.com/docs/aura/dashboards/parameters-and-filters/)
        *   [Filter types](https://neo4j.com/docs/aura/dashboards/filter-types/)
        *   [Sharing dashboards](https://neo4j.com/docs/aura/dashboards/sharing-dashboards/)
        *   [Visualizations](https://neo4j.com/docs/aura/dashboards/visualizations/)
            *   [Graph](https://neo4j.com/docs/aura/dashboards/visualizations/graph/)
            *   [Table](https://neo4j.com/docs/aura/dashboards/visualizations/table/)
            *   [Line chart](https://neo4j.com/docs/aura/dashboards/visualizations/linechart/)
            *   [Bar chart](https://neo4j.com/docs/aura/dashboards/visualizations/barchart/)
            *   [Pie chart](https://neo4j.com/docs/aura/dashboards/visualizations/piechart/)
            *   [Single value](https://neo4j.com/docs/aura/dashboards/visualizations/single-value/)
            *   [Text](https://neo4j.com/docs/aura/dashboards/visualizations/text/)
            *   [Map](https://neo4j.com/docs/aura/dashboards/visualizations/map/)

        *   [FAQ and resources](https://neo4j.com/docs/aura/dashboards/faq-and-resources/)

    *   Metrics
        *   [View metrics](https://neo4j.com/docs/aura/metrics/view-metrics/)
        *   Metrics integration
            *   [Introduction](https://neo4j.com/docs/aura/metrics/metrics-integration/introduction/)
            *   [Integration Process](https://neo4j.com/docs/aura/metrics/metrics-integration/process/)
            *   [Endpoint Status](https://neo4j.com/docs/aura/metrics/metrics-integration/status/)
            *   [Examples](https://neo4j.com/docs/aura/metrics/metrics-integration/examples/)
            *   [Reference](https://neo4j.com/docs/aura/metrics/metrics-integration/reference/)

    *   Logs
        *   [Query log analyzer](https://neo4j.com/docs/aura/logging/query-log-analyzer/)
        *   [Security log analyzer](https://neo4j.com/docs/aura/logging/security-log-analyzer/)
        *   [Log forwarding](https://neo4j.com/docs/aura/logging/log-forwarding/)
        *   [Download logs](https://neo4j.com/docs/aura/logging/log-downloads/)
        *   [Activity feed](https://neo4j.com/docs/aura/logging/activity-feed/)

    *   Security
        *   [Multi-factor authentication](https://neo4j.com/docs/aura/security/mfa/)
        *   [Single sign-on](https://neo4j.com/docs/aura/security/single-sign-on/)
        *   [IP filtering](https://neo4j.com/docs/aura/security/ip-filtering/)
        *   [Aura IP addresses and ports](https://neo4j.com/docs/aura/security/ip-addresses/)
        *   [Secure connections](https://neo4j.com/docs/aura/security/secure-connections/)
        *   [Encryption](https://neo4j.com/docs/aura/security/encryption/)
        *   [Tool authentication with Aura user](https://neo4j.com/docs/aura/security/tool-auth/)

    *   [User management](https://neo4j.com/docs/aura/user-management/)
    *   Billing and usage
        *   [Billing and usage report](https://neo4j.com/docs/aura/billing/usage-report/)
        *   [Billing dimensions](https://neo4j.com/docs/aura/billing/billing-dimensions/)
        *   [Payment options](https://neo4j.com/docs/aura/billing/payment-options/)

    *   Connecting applications
        *   [Drivers and libraries](https://neo4j.com/docs/aura/connecting-applications/overview/)
        *   [Using Query API](https://neo4j.com/docs/aura/connecting-applications/query-api/)

    *   Neo4j Connectors
        *   [Neo4j Connector for Apache Spark](https://neo4j.com/docs/aura/connectors/spark/)
        *   [Neo4j Connector for Apache Kafka](https://neo4j.com/docs/aura/connectors/kafka/)
        *   [Neo4j Connector for BI](https://neo4j.com/docs/aura/connectors/bi/)

    *   Aura API
        *   [Overview](https://neo4j.com/docs/aura/api/overview/)
        *   [Authentication](https://neo4j.com/docs/aura/api/authentication/)
        *   [API Specification](https://neo4j.com/docs/aura/platform/api/specification/)

    *   **Tutorials**
    *   Upgrade and migration
        *   [Migrate a version 4 instance to the latest version](https://neo4j.com/docs/aura/tutorials/upgrade/)
        *   [Migrate from self-managed Neo4j to Aura](https://neo4j.com/docs/aura/tutorials/migration/)
        *   [Migrating your AuraDB Free instance to another AuraDB tier](https://neo4j.com/docs/aura/tutorials/migration-free/)

    *   Integrating with Neo4j Connectors
        *   [Using the Neo4j Connector for Apache Spark](https://neo4j.com/docs/aura/tutorials/spark/)
        *   [Using the Neo4j BI Connector](https://neo4j.com/docs/aura/tutorials/bi/)

    *   [Improving Cypher performance](https://neo4j.com/docs/aura/tutorials/performance-improvements/)
    *   [Troubleshooting](https://neo4j.com/docs/aura/tutorials/troubleshooting/)
    *   [Create an AuraDB instance in the terminal](https://neo4j.com/docs/aura/tutorials/create-auradb-instance-from-terminal/)

**Is this page helpful?**

[](https://neo4j.com/docs)
*   [Neo4j Aura](https://neo4j.com/docs/aura/)
*    Manage instances 
*   [Backup, export, and restore](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/)

[Raise an issue](https://github.com/neo4j/docs-aura/issues/new/?title=Docs%20Feedback%20modules/ROOT/pages/managing-instances/backup-restore-export.adoc%20(ref:%20console)&body=%3E%20Do%20not%20include%20confidential%20information,%20personal%20data,%20sensitive%20data,%20or%20other%20regulated%20data.)

Backup, export, restore, and upload
===================================

The data in your Aura instance can be backed up, exported, and restored using snapshots.

A snapshot is a copy of the data in an instance at a specific point in time.

The **Snapshots** tab within an Aura instance card shows a list of available snapshots. You can find the **Snapshots** tab via **Inspect** in the more menu (**…​**) on the instance card.

There are different kinds of snapshots taken at different intervals with different lifecycles depending on your tier. See [Snapshot details](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#snapshot-details) for more information.

Aura stores the data securely in encrypted cloud storage buckets. Backups are stored in the same Cloud Service Provider and region as the instance they are associated with.

[](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_snapshot_types)Snapshot types
-------------------------------------------------------------------------------------------------------

### [](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_scheduled)Scheduled

AuraDB Business Critical AuraDB Virtual Dedicated Cloud AuraDB Professional AuraDS Enterprise AuraDS Professional

A **Scheduled** snapshot is a snapshot that is automatically triggered at a cadence depending on your tier.

For Professional instances running the latest version, scheduled snapshots are run automatically once a day, same for both AuraDS Professional and for AuraDS Enterprise instances, For Business Critical and Virtual Dedicated Cloud instances, they run once an hour. See [Snapshot details](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#snapshot-details) further on for information about frequency, restorability, and exportability of scheduled snapshots, as well snapshots on instances running version 4.x.

### [](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_on_demand)On Demand

An **On Demand** snapshot is a snapshot that you manually trigger with the **Take snapshot** button. This type of snapshot is the only snapshot available for Free instances.

[](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_snapshot_actions)Snapshot actions
-----------------------------------------------------------------------------------------------------------

![Image 2: snapshot actions](https://neo4j.com/docs/aura/_images/snapshot-actions.png)

### [](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#export-create)Export / Create

From the more menu (…​) next to an existing snapshot, you can:

*   **Export** - Download an AuraDB instance as a .backup file (latest version) or .dump file (version 4.x) to store a local copy and work on data offline. AuraDB instances with the Graph Analytics plugin are also exported as a .backup file. Download an AuraDS instance as a .tar file.

*   **Create instance from snapshot** - Create a new instance using the data from the snapshot.

Any backups exported from Aura may be unrecovered. For more information on how to recover a backup, see [Operations Manual → Aggregating an unrecovered full backup](https://neo4j.com/docs/operations-manual/current/backup-restore/aggregate/#aggregate-unrecovered-full-backup).

Note that the ability to **Export or Create** an instance from a scheduled **Virtual Dedicated Cloud** snapshot is **limited to 14 days for 4.x instances**. For latest version instances, this is limited to 60 days for full scheduled backups. Differential backups are not restorable/exportable and cannot be used to create a new instances from.

Additionally, for Virtual Dedicated Cloud instances running Neo4j latest version, the ability to export or create an instance from a scheduled snapshot is limited to one (full) snapshot per day.

Use the toggle **Show exportable only** on top of the list of snapshots to filter by whether a snapshot is exportable or not.

### [](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#restore-snapshot)Restore

Restoring from a snapshot overwrites the data in your instance, replacing it with the data contained in the snapshot.

You can restore data in your instance to a previous snapshot. Use the arrow next to the (**…​**) menu on the snapshot you want to restore from. This action overwrites the data currently in your instance and you will be asked to confirm that this is indeed desired. If not, you can create a new instance from the snapshot instead, as described in [Export / Create](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#export-create).

[](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#snapshot-details)Snapshot details
----------------------------------------------------------------------------------------------------------

| Tier | Aura version | Frequency of snapshots | Scheduled snapshots | On-demand snapshot [[1](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_footnotedef_1 "View footnote.")] |
| --- | --- | --- | --- | --- |
|  |  | **Full snapshot**[[2](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_footnotedef_2 "View footnote.")] | **Differential snapshot** | **Restorable days** | **Exportable days** | **Restorable and exportable days** |
| AuraDB Free | 4, latest | N/A | N/A | N/A | N/A | N/A |
| AuraDB Professional | 4, latest | Daily | N/A | 7 | 7 | 7 |
| AuraDB Business Critical | latest | Daily | Hourly | 30 | 30 full [[3](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_footnotedef_3 "View footnote.")] | 30 |
| AuraDB Virtual Dedicated Cloud | 4 | Every 6 hours [[4](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_footnotedef_4 "View footnote.")] |  | 60 (long), 7 (short) | 14 (long), 7 (short) | 90 |
| latest | Daily | Hourly | 60 | 60 full [[3](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_footnotedef_3 "View footnote.")] | 90 |
| AuraDS Professional | latest | Daily | N/A | 7 | 7 | 30 |
| AuraDS Enterprise | latest | Daily | N/A | 14 | 7 | 90 |
| [2](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_footnoteref_2). The full snapshot captures the entire database, while differential snapshots record changes since the last full snapshot. [3](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_footnoteref_3). The differential snapshot is not exportable. [4](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_footnoteref_4). One snapshot per day has a long retention period and remaining three a shorter period. |

[](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#restore-backup)Restore from backup file
----------------------------------------------------------------------------------------------------------------

From the **Restore from backup file** tab, next to the **Snapshots** tab on the instance card, drag and drop your _.backup_, _.dump_, or _.tar_ file or browse for it. This action also overwrites the data currently in your instance. If this is not desired, you can create a new instance from the snapshot instead, as described in [Export / Create](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#export-create).

[](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#neo4j-admin-upload)Upload an existing Neo4j database
-----------------------------------------------------------------------------------------------------------------------------

If you have a local copy of a Neo4j database and Neo4j installed locally, you can use this installation of Neo4j to upload this to your Aura instance.

This command does not work if you have a network access configuration setup that prevents public traffic to the region your instance is hosted in. See [Public traffic](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_public_traffic) below for more information.

`database upload` is a `neo4j-admin` command that you can run to upload the contents of a Neo4j database into an Aura instance, regardless of the database’s size, as long as it fits your Aura instance. Keep in mind that the database you want to upload may run a different version of Neo4j than your Aura instance. Additionally, your Neo4j Aura instance must be accessible from the machine running `neo4j-admin`. Otherwise, the upload will fail with SSL errors.

For details on how to use the `neo4j-admin database upload` command, along with a full list of options and version compatibility, see [Operations Manual → Upload to Neo4j Aura](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/upload-to-aura/).

The `database upload` command, introduced in Neo4j 5, replaces the `push-to-cloud` command in Neo4j 4.4 and 4.3. If the database you want to upload is running an earlier version of Neo4j, please see [the Neo4j Admin push-to-cloud documentation](https://neo4j.com/docs/operations-manual/4.4/tools/neo4j-admin/push-to-cloud/).

The `neo4j-admin push-to-cloud` command in Neo4j 4.4 and earlier is not compatible with instances encrypted with Customer Managed Keys. Use `neo4j-admin database upload` in Neo4j 5 to upload data to instances encrypted with Customer Managed Keys.

For Neo4j 4.x instances in Azure encrypted with Customer Managed Keys, use the Import data service to load data, as `neo4j-admin database upload` is not supported. See [Import](https://neo4j.com/docs/aura/import/introduction/) for more information.

### [](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_public_traffic)Public traffic

If you have created a network access configuration from the **Network Access** page, accessed through the sidebar menu of the Console, **Public traffic** must be enabled for the region your instance is hosted in before you can use the `database upload` command on that instance.

To enable **Public traffic** on a network access configuration:

1.   Select **Configure** next to the region that has Public traffic disabled.

2.   Select **Next** until you reach step 4 of 4 in the resulting **Edit network access configuration** modal.

3.   Clear the **Disable public traffic** checkbox and **Save**.

You can now use the `database upload` command on the instances within that region. Once the command has completed, you can disable **Public traffic** again by following the same steps and re-selecting the **Disable public** traffic checkbox.

* * *

[1](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_footnoteref_1). On-demand snapshots are restorable and exportable for the same period. 

[Regions](https://neo4j.com/docs/aura/managing-instances/regions/)[Vector optimization](https://neo4j.com/docs/aura/managing-instances/vector-optimization/)

Contents
--------

*   [Snapshot types](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_snapshot_types)
*   [Scheduled](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_scheduled)
*   [On Demand](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_on_demand)
*   [Snapshot actions](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_snapshot_actions)
*   [Export / Create](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#export-create)
*   [Restore](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#restore-snapshot)
*   [Snapshot details](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#snapshot-details)
*   [Restore from backup file](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#restore-backup)
*   [Upload an existing Neo4j database](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#neo4j-admin-upload)
*   [Public traffic](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/#_public_traffic)

[Join the User Research panel ---------------------------- Influence the future of Neo4j products by sharing your experiences with a researcher. Learn more](https://neo4j.com/docs/user-research/?ref=aura-docs)

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

![Image 3](blob:https://neo4j.com/5b947db6-e72f-400c-bf85-d864b3f3f522)
