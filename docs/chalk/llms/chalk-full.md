# Chalk Documentation

Source: https://docs.chalk.ai/llms-full.txt

---

# What is Chalk?
source: https://docs.chalk.ai/docs/what-is-chalk

Build, deploy, and iterate faster with Chalk — a programmable feature engine that powers low-latency inference, rapid model iteration, and observability across your model lifecycle.
Chalk eliminates the core pain points that slow down teams building enterprise AI and ML systems, providing an end-to-end platform for:

- Deploying and scaling enterprise-grade infrastructure
- Authoring feature pipelines in pure Python — No DSLs! No rewrites!
- Building training datasets with high throughput batch offline queries and point-in-time correctness
- Integrating unstructured data into production ML pipelines with LLMs
- Serving fresh features on-the-fly with versioning, branching, and full observabilityGradually rollout, easily rollback, and feature flag models with version controlCollaborate across teams with branch-based QAA/B testing models and LLM prompts with historical production traffic

Chalk is the first platform to unify feature and prompt engineering, LLM evals, and real-time low-latency inference into a unified platform.

### How does Chalk make feature engineering easier?

Define features using Pythonic classes — no DSLs required.
Every feature is:

- Typed and validated
- Versioned and testable
- Composable and reusable in both training and online inference

Describe relationships between entities (e.g., users and transactions) with simple type annotations, and Chalk takes care of joins, lineage, and query planning automatically.

```
import chalk.functions as F
from chalk.features import features
from chalk import DataFrame, Windowed, windowed, _

@features
class Transaction:
    id: int
    amount: float
    discount_percentage: float
    at: datetime

    # create new features inline with Chalk Expressions
    is_expensive_purchase: bool = _.amount > 100

    # instead of declaring user_id as a string type (user_id: str)
    # reference a feature from another class to create a join key
    user_id: "User.id"

    # "User.id" now enables you to reference the
    # User class associated with this transaction!
    user: "User"

@features
class User:
    # id, name, email are pulled from underlying data sources like
    # Postgres, Kafka, Iceberg, Athena, Snowflake, Databricks, etc.
    # with a SQL resolver
    id: int
    name: str
    email: str

    # computed with the Python resolver (function) `get_username`
    username: str

    # Chalk's SDK provides common functions that run in C++
    name_match: float = F.levenshtein_distance(_.name, _.email)

    # create an intermediate DataFrame of another feature class.
    # Chalk infers how to resolve the DataFrame
    # by leveraging the "User.id" type annotation
    # from the Transaction class as a join key
    txns: DataFrame[Transaction]

    # reference DataFrames to run aggregations
    transaction_count: int = _.txns.count()

    # easily filter DataFrames before running an aggregation
    average_discount_percentage: float = _.txns[
        _.amount,
        _.discount_percentage > 0,
    ].mean()

    # run aggregations across time intervals
    total_transaction_amount: Windowed[float] = windowed(
        "1d",
        "7d",
        "30d",
        expression=_.txns[
            _.amount,
            _.at > _.chalk_window,
        ].sum(),
    )
```

Chalk queries allow you to explicitly express the features you want returned:

```
chalk query --in user.id=241 --out name_match --out transactions
```

```
Results
https://chalk.ai/environments/devx/query-runs/4712089747
Branch: elvis
Environment: devx

 Name                       Hit?  Value
────────────────────────────────────────
 user.name_match        41.0


user.txns

 id    transaction_status  user_id  session_id  item_count  cheapest_line_item_price  most_expensively_valued_product_id  created_at                          updated_at
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 17    "failed"            27       16281       2           34                        20364                               "2024-12-06T00:36:07.348750+00:00"  "2024-12-06T19:53:21.575073+00:00"
 18    "failed"            27       16282       1           71.41                     20362                               "2024-11-26T11:29:03.684327+00:00"  "2024-11-27T01:50:03.002378+00:00"
 5440  "pending"           27       16357       1           62.64                     20180                               "2024-11-16T17:29:43.540722+00:00"  null
 67    "cleared"           27       16358       1           86.31                     20179                               "2024-11-28T04:11:31.857431+00:00"  "2024-11-29T04:08:29.746079+00:00"
 68    "cleared"           27       16359       1           138.38                    20178                               "2024-11-11T01:19:53.140456+00:00"  "2024-11-11T11:35:40.673632+00:00"



(5 rows)
```

When running this query, Chalk only fetches exactly the base features needed to return name_match and txns.

Chalk analyzes type annotations to build a directed acyclic graph (DAG) of feature dependencies.
At inference time, query plans tailored to your input/output schema are generated dynamically by slicing this DAG into sub-graphs.
This ensures that only the features needed are fetched — optimizing for speed, precision, and cost.

Each node in the DAG is a Chalk expression or resolver (SQL / Python):

- An expression e.g. is_expensive_purchase: bool = _.amount > 100
- A SQL file ending in .chalk.sql that connects to an underlying data store like Athena
- A Python function that explicitly inputs and outputs featuresUse the Python packages you're familiar with e.g. Polars, httpx, OpenAI, etc.

Here's an example of a generated query plan:

Chalk query plan

### How does Chalk resolve features? What are Chalk resolvers?

Chalk connects directly to your existing infrastructure and underlying data stores (Athena, BigQuery, Postgres, Iceberg catalog, etc.) with SQL resolvers and to APIs (microservices, 3rd-party clients, LLMs) with Python resolvers.
Resolvers make it easy to integrate a wide variety of data sources, join them together, and use them in inference.

Decoupling feature logic from ETL pipelines unlocks:

- Faster iteration cycles
- On-demand just-in-time inference
- Reproducible and testable features (with point-in-time accuracy)

### How does Chalk orchestrate and manage features?

Chalk has built-in support for feature engineering workflows — there's no need to manage Airflow or orchestrate complicated streaming flows.
Once you've defined features and resolvers, Chalk orchestrates them into flexible pipelines (slicing the DAG) that make both training and model execution easy.

The get_username Python resolver below explicitly defines input dependencies as User.email and specifies the output feature type as User.username:

```
@online
def get_username(
    # the input type annotation specifies the input feature
    email: User.email,
    # the resulting feature is saved as username unto User class
) -> User.username:
    username = email.split("@")[0]
    if "gmail.com" in email:
        username = username.split("+")[0].replace(".", "")

    return username.lower()
```

### How do you cache features with Chalk?

Some data sources, like LLMs or 3rd party APIs, are expensive or slow to call at inference time.
Chalk supports caching features to optimize for latency and cost:

- Define cache TTLs inline with your features
- Override staleness at query-time when fresh data is critical
- Pre-warm caches and backfill pipelines for performance

Add a caching policy with one line of code in our feature definition:

### How do you deploy and query features with Chalk?

After defining pipelines, deploy features to a branch in < 100ms with:

```
chalk apply --branch
```

Chalk scans through resolvers, lints features, and deploys them to this separate branch.

```
✓ Found resolvers
✓ Deployed to branch 'fraud-model-v2'
```

Chalk automatically detects and uses your current Git branch name without requiring you to explicitly specify it.
Query for features against this branch to test changes independently before merging them into the production environment.

```
chalk query --branch --in user.id=47
```

This command returns the user's features from your branch deployment, showing all computed fields for the specified user.id.

```
Using '--out=user'
Results
https://chalk.ai/environments/devx/query-runs/4701020347
Branch: elvis
Environment: devx

 Name                                             Hit?  Value
─────────────────────────────────────────────────────────────────────────────────────────────────────
 user.average_rating_given                  4.3125
 user.birthday                              "1987-12-28"
 user.created_at                            "2024-08-07T20:54:42.942294+00:00"
 user.email                                 "98178ad58fe8481db74996996d6e8de7@google.ru"
 user.first_name                            "Marseda"
 user.id                                    47
 user.last_name                             "Karkaletsis"
 user.review_count                          32
 user.total_orders_placed                   48
 user.unique_products_inquired_about        203
```

Once you validate the deployment, promote it to production with a single CLI command and no downtime (blue-green deployments).

```
chalk apply
```

These features are now available for low-latency online inference and offline training.

### Why Chalk?

Features are computed at inference time with an execution engine called Velox — we maintain a fork that's been heavily optimized for low-latency (< 3 ms).
Chalk's low-latency execution enables us to bridge the gap between experimentation and production by unifying offline and online inference.
With this unified approach, teams can easily:

- Establish a single source of truth for feature definitions and transformations
- Consolidate training and serving into a single version controlled environment
- Reduce time-to-production for new models from months to days
- Standardize and share features across the entire organization

Chalk offers the developer-friendly experience of Python while achieving high performance by transpiling functions like get_username into optimized Velox expressions by parsing the Abstract Syntax Tree (AST) of the Python code.

```
lower(
    if_then_else(
        !=(
            strpos(str(email), str(gmail.com)),
            int(0)
        ),
        replace(
            element_at(
                split(
                    element_at(split(str(email), str(@)), int(1)),
                    str(+)
                ),
                int(1)
            ),
            str(.),
            str()
        ),
        element_at(split(str(email), str(@)), int(1))
    )
)
```

We wrote an engineering blog post on our Symbolic Python interpreter if you want to learn more!

### Observability

Traditional ML systems often operate as opaque black boxes, especially when transformation logic gets embedded across disparate data pipelines, obscuring the connection between inputs and predictions.
Chalk brings comprehensive observability to every aspect of your ML systems, making it easy to:

- Trace every model feature back to its original data sources with detailed lineage tracking, showing exactly where the data originated
- Troubleshoot and optimize your ML pipelines with end-to-end tracing that tracks the inputs and outputs of every step in any run
- Monitor feature drift, access patterns, and performance metrics in real-time across all your model deployments

Deploy faster and confidently, knowing exactly how your systems behave at each step of the machine learning lifecycle.

### Chalk for MLOps

Let Chalk handle orchestrating, caching, and serving features at scale, freeing you and your team to focus on building models, not plumbing.

Chalk brings modern software engineering to data workflows:

- Features are discoverable and auditable across all environments
- Experimental changes are isolated to branches and safely promoted via CLI with gradual rollouts
- Models are versioned and can be easily rolled-back the same way you would an API

Easily serve features across your entire tech stack with SDKs in Python, JavaScript, Java and more - making inference accessible to any team whether for internal tools or customer-facing applications.

With Chalk, MLOps teams confidently deploy and serve low-latency ML systems, benefiting from comprehensive observability while supporting gradual rollouts and seamless rollbacks.

### Chalk for AI Engineers

Build enterprise-grade AI applications without stitching together LLMs, prompts, vector DBs, and retrieval logic.

- Call chat completion APIs out-of-the-box
- Cache expensive computations to avoid redundant processing and reduce latency
- Retrieve real-time context into LLMs
- Generate embeddings and vectors within pipelines
- Run large-scale evaluations using historical traffic
- Reuse and manage prompts with named prompts

```
import chalk.functions as F
import chalk.prompts as P
from chalk.features import DataFrame, Primary, Vector, embed, features, has_many, _
from pydantic import BaseModel

# Use structured output to easily incorporate unstructured data in our ML pipelines
class AnalyzedReceiptStruct(BaseModel):
    expense_category: ExpenseCategoryEnum
    business_expense: bool
    loyalty_program: str
    return_policy: int

@features
class Transaction:
    id: int
    merchant_id: Merchant.id
    merchant: Merchant
    receipt: Receipt

    llm: P.PromptResponse = P.completion(
        model="gpt-5.1-2025-11-13",
        messages=[P.message(
                role="user",
                content=F.jinja(
            """Analyze the following receipt:
            Line items: {{Transaction.receipt.line_items}}
            Merchant: {{Transaction.merchant.name}} {{Transaction.merchant.description}}""")
        )],
        output_structure=AnalyzedReceiptStruct,
    )

    # cache forever since transaction is finalized
    expense_category: str = features(
        max_staleness="infinity",
        expression=F.json_value(
            _.llm.response, # from LLM
            "$.expense_category",
        ),
    )
    # or configure the chat completion from your Chalk dashboard
    llm_call_with_named_prompt: P.run_prompt("analyze_receipt-v1")

@features
class ProductRec:
    user_id: Primary[User.id]
    user: User

    # generate embeddings
    user_vector: Vector = embed(
        input=F.array_join(F.array_agg(
            _.user.products[
                _.name,
                _.type == "liked"
            ]),
            delimiter=" || ",
        ),
        provider="vertexai",
        model="text-embedding-005",
    )

    # do a vector search with the generated embedding
    similar_users: DataFrame[User] = has_many(
      lambda: ProductRec.user_vector.is_near(
            User.liked_products_vector
        )
    )
```

With Chalk, AI engineers easily integrate unstructured data, build context-aware prompts, and run LLM evaluations at scale — all without managing vector databases, embedding providers, and complex retrieval systems.

### Chalk for Data Scientists

Test new features, run experiments, and ship production models — all from a Jupyter notebook.

- Catch regressions and A/B test features on development branches
- Import features from production into Jupyter notebooks with a single line of code
- Export features to catalogs like Iceberg for downstream analytics and usage
- Trace data lineage all the way down to source tables

```
from chalk.client import ChalkClient

client = ChalkClient(branch=True)
client.load_features() # load prod features with one line

User.name_exclaimed = _.name + "!" # add new features

chalk_dataset = client.offline_query(
    input={
        User.id: list(range(1000)),
    },
    output={
        User.id,
        User.name,
        User.name_exclaimed,
    },
    recompute_features=True, # A/B test against historical model runs
    dataset_name="fraud_model",
)

df = chalk_dataset.to_pandas() # convert to pandas dataframe

# write to Glue or Iceberg
catalog = GlueCatalog(
    name="aws_glue_catalog",
    aws_region="us-west-2",
    catalog_id="123",
    aws_role_arn="arn:aws:iam::123456789012:role/OurCatalogueAccessRole",
)
chalk_dataset.write_to(destination="database.table_name", catalog=catalog)
```

Chalk evaluates features with point-in-time lookups, guaranteeing evaluation only with data that would have been seen in the past.
You can provide labels with different past timestamps to easily get historical features that represent what your application would have retrieved online at those past times.

With Chalk, data scientists easily integrate new data sources, test new features with point-in-time correctness, and collaborate with Git-like branches and flexible data exports (to data catalogs like Iceberg and Parquet).

### Chalk for Data Engineers

Manage features declaratively without the complexity of orchestrating ETL jobs, feature stores, and offline/online datastores.
Chalk makes it easy to:

- Cache expensive computations with configurable staleness
- Manage model versions and A/B test features
- Create complex joins and relationships between data entities
- Configure time-window aggregations with flexible materialization options

```
from chalk.features import DataFrame,
  feature,
  features,
  _
from chalk.streams import Windowed, windowed

@features
class Transaction:
    id: int
    created_at: datetime
    amount: float

    user_id: "User.id"
    user: "User"

@features
class User:
    id: int
    domain: str

    # composite keys that can be used as join keys
    workspace_id: str = _.domain + "-" + _.id
    expensive_api_call: str = feature(max_staleness="30d") # cache values

    # maintain different resolvers to A/B test function calls e.g. gemini vs openai
    llm_response: str = feature(version=3)

    # multi-attribute joins
    txns: DataFrame[Transaction]

    count_txns: Windowed[int] = windowed(
        "1d", "365d",
        expression=_.txns[_.created_at > _.chalk_window].count(),
        # https://docs.chalk.ai/docs/materialized_aggregations
        materialization=True,
    )
```

Chalk also integrates natively into your existing data infrastructure by deploying directly into your virtual private cloud (VPC) providing seamless resource access while maintaining strict security and compliance controls with full data isolation:

- Customizable compute layer enabling the use of different memory stores (Redis, etc.) tailored to access patterns and performance requirements
- Inherit existing security groups, policies, and ACLs
- Co-located resources and full-control over data residency to meet compliance requirements

With Chalk, Data Engineers easily manage features programmatically and maintain production systems without the overhead of configuring YAML, custom scripts, or infrastructure.

### A full-stack solution for building and deploying enterprise AI

Chalk gives teams the building blocks to prototype and deploy production AI and ML systems quickly and reliably.
Whether you're delivering hyperpersonalized product recommendations, dynamically reranking search results, or detecting sophisticated fraud patterns, Chalk is the go-to platform for inference.

Schedule a demo to see how Chalk fits with your team.

# Platform Architecture
source: https://docs.chalk.ai/docs/architecture

## How it all fits together.

Chalk’s online query serving platform is architected to

- retrieve fresh features across heterogeneous sources with the minimum possible latency
- orchestrate and execute complex transformations on structured and unstructured data
- uphold enterprise-grade guarantees for security, observability, and reliability

In short, Chalk was built to get the right data from the right place at the right time.

### Online serving architecture

Let's examine how the pieces work together to compute and serve features.

Suppose that you want to compute a set of features for making a decision about a request from a user:

- Your application sends an HTTP request to Chalk's serving API for features
- Chalk's query planner generates an optimized execution plan by analyzing feature dependencies and available data sources.
- Chalk's compute engineretrieves fresh values from underlying sources with Resolverspulls from Chalk’s low-latency online storage e.g. tiled / materialized features or cached featuresexecutes the generated query plan
- Returns computed features in response
- Newly computed features values are logged for reuse and auditability

Chalk architecture diagram

This entire pipeline—from SQL queries and API calls to response—runs in less than 5ms, even with heterogeneous data sources and complex logic.
Chalk uses many techniques to reduce latency, such as:

- Automatic parallelism across pipeline stages
- Vectorization of pipeline stages that are written using scalar syntax
- Statistics-informed join planning
- Low-latency key/value stores (like Redis, BigTable, or DynamoDB)
- Transpilation of Python code into native code with Chalk's symbolic Python interpreter

### Data orchestration

Chalk eliminates the complexity of orchestrating data and ETL pipelines by building a dependency graph (DAG) of your features, which are defined using Python.
At inference time, Chalk dynamically builds query plans (subgraphs of your feature DAG) without manual configuration, based on the features you request.

Write feature definitions in Python, and Chalk automatically

- Determines optimal computation and query planning strategies
- Handles caching, incremental updates, and backfills
- Provides built-in observability and data lineage without additional tooling

As a result, Chalk can serve as a drop-in replacement for orchestration tools like Dagster, Airflow, and Prefect while simultaneously providing purpose-built features for production ML workloads.

Chalk query plan

Declaratively defining features frees up data teams to focus on designing features instead of writing plumbing code.
There's no need to write custom glue code because Chalk interfaces directly with underlying data sources, managing all the connections and transformations behind the scenes.

Note: Features can also be computed on a recurring basis with scheduled queries.

### Data persistence and storage

Chalk uses different storage technologies to support online and offline use cases.

The online store is optimized for serving the latest version of any given feature for any given entity with the minimum possible latency.
Chalk can be configured to use Redis or Cloud Memory Store for smaller resident data sets with high latency requirements, or DynamoDB when horizontal scalability is required.

The offline store is optimized for storing all historical feature values, serving point-in-time correct queries, and tracking provenance of features.
Chalk supports a variety of storage backends depending on data scale and latency requirements.
Typically, Chalk uses Snowflake, Delta Lake, BigQuery, Iceberg, or Athena.

### Offline computation and serving

Chalk's architecture also supports efficient batch point-in-time queries to construct model training sets or perform batch offline inference.

- Submit a training data request from a notebook client like Jupyter using Chalk's Python SDK
- The query planner builds a point-in-time correct plan
- The compute engine pulls point-in-time correct feature values from offline storage
- Chalk returns a DataFrame of features to you.

Chalk integrates with your existing data providers (Snowflake, Delta Lake, or BigQuery) to ingest massive amounts of data from a variety of data sources and query it efficiently.
Note that data ingested into the offline store can be trivially made available for use in an online querying context with Chalk's Reverse ETL.

There's an exhaustive list of supported ingestion sources in the Integrations section.

### High-performance execution engine

Under the hood, Chalk uses Velox, an open source unified execution engine, to deliver high-throughput feature computation.
We maintain a fork that's been optimized for low-latency online inference.

You can think of Velox as a backend for query engine's like Presto (AWS Athena) and Spark i.e. you can't point Velox at a database and pass in a SQL expression.
Rather than forcing users to work directly with low-level execution primitives, Chalk provides an ergonomic interface (Chalk Python SDK) for defining features, transformations, and pipelines.

Velox architecture diagram

This architecture allows us to expose the power of vectorized computation with clean APIs that feel natural (like writing Pandas and Polars) to data scientists and engineers.
Users write simple Python decorators and SQL queries, while Velox handles the complex optimizations that make these computations blazingly fast.

- Velox's columnar memory layout and vectorized expression evaluation deliver significant performance improvements, with benchmarks showing 6-7x speedups on real analytical workloads
- Native support for structs, maps, arrays, and nested data types makes it ideal for feature engineering workflows
- Features like filter reordering, dynamic filter pushdown, and adaptive column prefetching optimize query execution based on runtime statistics

### Service architecture

We offer both a hosted model (“Chalk Cloud”) and a customer-hosted model (“Customer Cloud”).

Most companies choose to run Chalk in their own cloud (VPC) for data residency and compliance.
Chalk is traditionally deployed as a Platform As a Service into an isolated account under the managent of the customer, with the core components (VPC, Kubernetes Cluster, Message Queues, etc) managed by Chalk.

Compute nodes run on Kubernetes (typically EKS on AWS, GKE on GCP, and AKS on Azure).
If you have custom needs, we are happy to customize the deployment to fit with your service architecture.

### Metadata Plane

The Metadata Plane is responsible for storing and serving non-customer data (like alert and RBAC configurations).
It can control many Data Planes, which it manages through the Kubernetes API,
enabling tasks such as scaling deployments and running batch jobs.

In short, the Metadata Plane handles:

- Deployment orchestration
- Access control
- Monitoring and alerting
- Feature discovery

It does not have access to customer data.

### Data Plane

The Data Plane encompasses the execution environment for feature pipelines along with the storage and serving
infrastructure for both online and offline feature stores.

A single Data Plane can run many Chalk Environments.
Often, companies will have 2-3 environments (like qa, stage, and prod.)
If running in a single data plane, these environments share resources, which helps with cost and ease of setup.

However, if you prefer to have stronger isolation between Chalk Environments,
each Chalk Environment can run in a separate Data Plane.
You would typically run only one Metadata Plane to orchestrate all Data Planes,
and deploy the Metadata Plane to the most sensitive of the environments.

### Deployment Models

Chalk offers several deployment options
to provide you with the right level of infrastructure
control.

### Chalk-Hosted Deployment

In the Chalk-Hosted Deployment, both the Metadata Plane and Data Plane
run in Chalk's cloud account. Deployed in this manner, Chalk runs
as a SaaS application. There is no infrastructure to manage,
and no ability to see inside the cloud account running Chalk.

### Customer Cloud Deployment

The Customer Cloud Deployment is Chalk's most common deployment.

Most customers choose our Customer Cloud Deployment.
In this model, the customer runs the Data Plane in its own cloud account,
and Chalk runs the Metadata Plane in its cloud account.

This deployment model strikes a good balance between security and ease of maintenance.
No one at Chalk will be able to access your data, but the Chalk team
can handle upgrades to the underlying resources without your team's involvement.

### Air-Gapped Deployment

Chalk offers the option to self-host both the Data Plane and Metadata Plane.
In the Customer Cloud Deployment, only the Data Plane runs in your cloud account,
whereas in the Air-Gapped Deployment, the Metadata Plane
joins the Data Plane in your cloud account.

There are two primary reasons that customers will choose to host the Metadata Plane:

- Regulatory requirements: highly regulated environments (like FedRAMP) may require additional security control.
- Disaster recovery: deploying both the Metadata Plane and Data Plane into your cloud account means that Chalk will continue to run independent of any Chalk uptime.

In this configuration, no service hosted by Chalk needs to talk to your instance.
Telemetry can be exported for billing purposes (over topics), but is non-essential
to uptime of your instance.
In the event of a complete outage in Chalk's cloud accounts,
your instance service would continue running indefinitely without disruption.

### Data Plane Architecture

Chalk has a few tiers of concepts within the Data Plane that are important to understand when thinking
about how to structure your deployment, such as how many environments you should set up. Each customer
is associated with a team. Each team is tied to one or more projects, and each project
can have one or more environments. The team, project, and environment concepts are all logical groupings
for the underlying Kubernetes resources of Data Plane components.
Each environment has at least one resource group, which is one set of Data Plane components, as well as a
metrics database deployment. Then, each resource group is deployed to a Kubernetes cluster, and every
Chalk-managed Kubernetes cluster has a set of background processes that can be shared across environments
deployed to that cluster. These background processes include load balancers, background persistence workers,
a Clickhouse deployment for tracing, and a cluster manager.

Most customers have a team, a project, and one or more environments deployed across one or more Kubernetes clusters,
however the exact structure of your deployment is flexible within the constraints outlined in the previous
paragraph.

### Monitoring

Native integrations with PagerDuty and Slack ensure teams are immediately alerted to any issues
in their feature pipelines.

Beyond alerting, every Chalk query is fully instrumented with traces and detailed logs, enabling
both broad system-wide monitoring and deep request-level debugging across every stage of
computation—down to the root data source.
With Chalk, data teams get

- Comprehensive logging & debuggingResolver execution detailsFeature computationsCache missesData source failuresFeature stalenessFeature ownership tracking
- Metrics and performance monitoringFeatures: request volumes, computation times, and error ratesModels: inference latency, prediction accuracy, and resource utilizationSystem: query throughput, system latency, and pipeline health
- End-to-end request tracingTrack the inputs and outputs of every step in any runLineage tracking from data source to final predictions

Easily, build your own views and set up custom dashboards to visualize your metrics and configure smart alerts with custom formulas that notify you instantly when thresholds are crossed or anomalies are detected.

Metrics and chart creation

This flexibility to configure and define your own metrics makes it easy to answer common questions such as how often certain features are computed, how long individual computations take, and what the average value for a feature is.

### Architecting maintainable and scalable systems for enterprise success

By both connecting to your data stores directly and computing features post-fetch, Chalk makes it
trivial to integrate new data sources from other teams, dramatically increasing predictive
accuracy and the context available to your models.

Your systems can also bidirectionally integrate with Chalk's underlying infrastructure, which
is built on widely-adopted technologies like Redis or DynamoDB, and leverages open
standards like Arrow, Parquet, and Iceberg—ultimately maximizing compatibility and unlocking
downstream analytical workflows

Together, these architectural choices enable enterprises to build future-proof ML and AI systems
that scale with their needs, maintain interoperability, and seamlessly integrate with their
existing technology stack.

# How do I use Chalk?
source: https://docs.chalk.ai/docs/setup-guide

## Customizing your Chalk solution.

Chalk is a feature store that enables data engineers and data scientists on production machine learning teams to
collaborate efficiently and effectively.

In this tutorial, we will guide you step by step through customizing your Chalk solution to help you achieve all of
your data goals.

### Creating your Chalk project

- If you don't already have a GitHub repository where you will store your Chalk code, create one. Then, pick a
local directory in which to work on Chalk code, and clone the GitHub repository there. Then cd inside of the
directory.
- If you haven't already, install Python. You can do this through Homebrew as follows:

```
# Install Homebrew
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# Use Homebrew to install python3.11
$ brew install python@3.11
```

- Install the Chalk command line tool. The Chalk CLI allows you to create, update, and
manage your feature pipelines directly from your terminal

```
curl -s -L https://api.chalk.ai/install.sh | sh
```

- Create a Python virtual environment within your repository root directory and activate it

```
$ python3.11 -m venv .venv
$ source .venv/bin/activate
```

You can run source .venv/bin/activate to activate the virtual environment, and deactivate to deactivate.

- Log in by typing chalk login. If you're using a dedicated environment, make sure you use the
--api-host flag. Type y when prompted and log in through the browser.
- Run chalk init to initialize your project files. This will initialize a directory structure with an
empty src directory and three files: chalk.yaml, README.md, and requirements.txt.

```
root_directory/
├── src/
├── chalk.yaml
├── README.md
└── requirements.txt
```

The first file, chalk.yaml, stores configuration information about your project. You can edit this so it
contains the following

```
project: {YOUR_PROJECT_NAME}
environments:
  default:
    requirements: requirements.txt
    runtime: python312
```

The second file, README.md, contains some basic commands you can use with the Chalk CLI.
The third file, requirements.txt should look something like this:

```
requests
chalkpy[runtime]
```

This contains your project dependencies.
You can add a file .chalkignore which will act just like a .gitignore file, and exclude the specified files from
deploys when you run chalk apply (more on this later).

- Within your virtual environment, install the project requirements.

```
$ pip3 install -r requirements.txt
```

Now, you should have a virtual environment with all project dependencies installed and a basic project structure upon
which we will build in the next step.

### Configure data sources

Having set up a basic project directory, next we'll want to configure the data sources from which we will load data to
compute our features. We can do so in the Chalk dashboard.

- In the same directory from before, log in or sign up with Chalk directly from the command line. The
chalk login command will open your browser and create an
API token for your local development, as well as redirect you to your dashboard. If you are not
redirected you can also find the dashboard at https://chalk.ai/projects
or run the chalk dashboard command.
You will automatically see all the environments in which the email you used to log in has been
provisioned as a user.
- Within the dashboard, navigate to Data Sources in the sidebar and add all data sources that you will
be working with here. After you have saved a data source, you can use the Test Data Source button
in the upper right hand corner of the Data Source configuration view to verify that your connection is
valid.
- Within the working directory, we'll add a datasources.py file under our src folder to reference the
data sources that we've added in the dashboard.

```
root_directory/
├── src/
│  ├── __init__.py
│  └── datasources.py
├── chalk.yaml
├── README.md
└── requirements.txt
```

Say we added a PostgreSQL data source, then our datasources.py might look something like this:

```
pg = PostgreSQLSource(name='PG')
```

For more details on setting up data sources, see here.

### Define feature classes and resolvers

Next, we'll define our feature classes and resolvers. Each feature class is a Python class of features, and each resolver
tells Chalk how to compute the values for different features. Each feature that we write should correspond to a
resolver output.

We recommend starting with a minimal feature class and building up iteratively to easily test your code along the way.
After writing some feature classes, resolvers, and tests, we would expect to see a directory structure like this:

```
root_directory/
├── src/
│  ├── resolvers/
│  │  ├── .../
│  │  ├── __init__.py
│  │  └── pipelines.py
│  ├── __init__.py
│  ├── datasources.py
│  └── feature_sets.py
├── tests/
│  └── ...
├── .chalkignore
├── chalk.yaml
├── README.md
└── requirements.txt
```

You can read more in our docs about the different kinds of features and the
different kinds of resolvers that you can write. If you would like
guidance on how to structure your feature classes and resolvers, please reach out in your support channel!

### Deploy and query

Now, you can deploy the features and resolvers that you wrote! You can deploy to production by
using the chalk apply command. During development, we recommend that you use
chalk apply --branch {BRANCH_NAME} to deploy to the branch server, which allows
multiple people to work concurrently in one environment, and also enables more performant deploys.

Once you have deployed your code, then you can query your features directly from the command line using the
chalk query command, or by calling one of our Chalk Clients in code.
Chalk has a Python client, Go client,
Java client, and a Typescript client.

This is the primary workflow for iterating on features and resolvers! Write, deploy, and query to verify whether the
feature values that you receive are the values you expect. Once you have finalized your feature class and resolver
definitions, the final step is frequently orchestration.

### Orchestration

Having verified that your feature and resolver definitions are correct, the next step is to determine how
you want to use the corresponding feature values within your larger machine learning platform. Some users trigger
resolvers and run queries from within other orchestrated pipelines, such as Airflow.
Some users define cron schedulesfor their resolvers,
and set staleness values on different features to
ensure that the data they query falls within their requirements for freshness. The data world is your oyster!

But, as always, if you would like guidance on how to configure that oyster, please reach out in your support channel!

### Further resources

For a detailed tutorial on how to build a fraud model using Chalk, see here.

# File Structure
source: https://docs.chalk.ai/docs/configuration

## Configure your Chalk project and organize your features and resolvers.

### Overview

Your Chalk project's configuration is shared across the following files:

- chalk.yaml (or chalk.yml): Configuration for your project's deployment
- .chalkignore: Files to exclude from your project's deployment
- A requirements file: Default Python requirements for Chalk to install via pip (can be overridden in chalk.yaml).
This can either be requirements.txt or a pyproject.toml
(via Poetry or uv).

Here's our recommended repository structure:

```
company_chalk/
├── src/
│  ├── resolvers/
│  │  ├── ...
│  │  ├── __init__.py
│  │  └── pipelines.py
│  ├── __init__.py
│  ├── datasources.py
│  └── feature_sets.py
├── tests/
│  └── ...
├── notebooks/
│  └── ...
├── .chalkignore
├── chalk.yaml
├── README.md
└── requirements.txt
```

When you're first getting started, we recommend putting all your features in a single
file. Keeping the features in a single file makes circular references easier to reason
about, as they can just be quoted.

If you do want to split your features across multiple files,
you'll need to use the if TYPE_CHECKING block from the typing module.

### Organizing Feature Definitions Across Files

In large projects, it's common to split feature definitions across multiple Python modules.
For unidirectional dependencies, this is straightforward. For example, if src/models/user.py imports
src/models/profile.py, you can define the User and Profile features in separate files without
issues. However, if you have circular dependencies, you may run into problems.

Chalk supports this, but circular imports can arise when features reference each other across files.
To avoid these issues, use the if TYPE_CHECKING block from the typing module and quote your forward references.

Here's an example of how to do this cleanly:

```
# Imports `User` directly, because `src/models/user.py`
# doesn't import `src/models/profile.py`
from chalk.features import features
from src.models.user import User

@features
class Profile:
    id: Primary[User.id]
    username: str
```

```
from chalk.features import features
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Imports `Profile` only when type checking
    # to avoid circular imports
    from src.models.profile import Profile

@features
class User:
    id: str
    # Profile must be quoted because it is imported
    # only when type checking
    profile: "Profile"
```

By quoting imports inside if TYPE_CHECKING,
you avoid circular dependency errors while still
maintaining type safety and feature linkage.

If the relationship to Profile is optional, you can use typing.Optional or the | None syntax,
but the entire annotation should be quoted:

```
from chalk.features import features
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.profile import Profile

@features
class User:
    id: str
    # All of `"Profile | None"` must be quoted, not just the `Profile` part
    profile: "Profile | None"
```

A similar pattern should be used for DataFrame annotations:

```
from chalk.features import features
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.profile import Profile

@features
class User:
    id: str
    # All of `"DataFrame[Transaction]"` must be quoted, not just the `Transaction` part
    transactions: "DataFrame[Transaction]"
```

In a project with features living in different files, we recommend that the schema definition
all live in a single folder, separate from the resolvers. In this case, your folder structure
will look something like:

```
company_chalk/
├── src/
│  ├── models/
│  │  ├── user.py
│  │  ├── profile.py
│  │  ├── __init__.py
│  │  └── ...
│  ├── resolvers/
│  │  ├── ...
│  │  ├── __init__.py
│  │  └── pipelines.py
│  ├── __init__.py
│  ├── datasources.py
│  └── feature_sets.py
├── tests/
│  └── ...
├── notebooks/
│  └── ...
├── .chalkignore
├── chalk.yaml
├── README.md
└── requirements.txt
```

Keeping the schema definition all in one place (as you might with something like Protobuf or Avro files)
helps you keep your schema definitions organized and makes importing them in your resolvers straightforward.

### chalk.yaml

Use chalk.yaml to configure your project's Docker environment, Python configuration, and metadata validation for your
features and resolvers.

### Schema

The name of this Chalk project, which must match your project's name in the dashboard (case-sensitive).

Per-environment overrides. See our Docker documentation for more details.

The name of this environment, such as prod or qa. Find available environment names in
your dashboard. Use default to configure default values to apply to all of this project's
environments.

The Python version for the Chalk project.

Python requirements file to install with pip. This can either be a requirements.txt file or
a pyproject.toml file.

Path to an alternative Dockerfile that will be used to build a base image for your Chalk deploys.

Reference a version of the Chalk runtime that you want to use for this environment. Can be either a version
tag, like v3.0.0, or a release stream like stable. If not specified, defaults to stable.
Releases are documented in the Platform Release Notes.

Path to a custom ignore file for this environment. If not specified, defaults to .chalkignore in
the project root. Use this to exclude different files from deployment in different environments.

Configuration for metadata validation for features and resolvers. See our validation
documentation for more details.

Validations for all features.

A list of dictionaries of metadata attributes and error severity levels when this metadata property is
missing.

The name of the metadata property.

The level of severity to use when a feature is missing this metadata property. Deploys are permitted for
info and warning levels, but disallowed for error level.

Validations for all resolvers.

A list of dictionaries of metadata attributes and error severity levels when this metadata property is
missing.

The name of the metadata property.

The level of severity to use when a feature is missing this metadata property. Deploys are permitted for
info and warning levels, but disallowed for error level.

### Sample file

Here is a sample chalk.yaml file. In this file, we use a different Dockerfile in production and different chalkignore files per environment.

```
project: my-project-id

environments:
  default:
    runtime: python312
    requirements: requirements.txt
  dev:
    chalkignore: .chalkignore.dev
  prod:
    dockerfile: ./DockerfileProd
    chalkignore: .chalkignore.prod

validation:
  feature:
    metadata:
      - name: owner
        missing: error
      - name: description
        missing: warning
      - name: tags
        missing: info
  resolver:
    metadata:
      - name: owner
        missing: error
```

### .chalkignore

Your .chalkignore file should include your scripts, notebooks, and tests. Anything that you are not actively using in
your deployment should be added so that non-deployment code does not clutter or interfere with your deployment.

### Per-Environment Chalkignore Files

You can specify different chalkignore files for each environment in your chalk.yaml file. This is useful when you want to exclude different files from deployment in different environments. For example, you might want to include experimental features in dev but exclude them from production.

```
project: my-project
environments:
  dev:
    runtime: python312
    chalkignore: .chalkignore.dev  # Custom ignore file for dev
  prod:
    runtime: python312
    chalkignore: .chalkignore.prod  # Custom ignore file for prod
  staging:
    runtime: python312
    # No chalkignore specified - defaults to .chalkignore
```

If no chalkignore field is specified for an environment, Chalk will use the default .chalkignore file in your project root.

### Python Requirements

Chalk will install the Python requirements for your project as specified in the requirements
parameter of your chalk.yaml file. This can either be a requirements.txt file or a pyproject.toml.
Chalk supports both Poetry and uv for managing your Python dependencies.
You can specify this file's location and type in your chalk.yaml file like below:

```
project: my-project-id

environments:
  dev:
    runtime: python312
    requirements: requirements-dev.txt
  prod:
    requirements: pyproject.yaml
```

### Python Requirement Overrides

The requirements file specified in your chalk.yaml file will serve as the default dependency set for
your environment. However, if you have different requirements for specific resolvers, you can also
define alternative virtual environments under the venvs key in your chalk.yaml file.

```
project: features

environments:
    default:
        runtime: python311
        requirements: ./requirements.txt
        platform_version: v3.26.8

venvs:
    model-1:
      dependencies:
        - numpy==2.3.2
        - pandas==2.3.2
        - scikit-learn==1.7.2
        - tensorflow==2.20.0
        - torch
        - transformers
    model-2:
      requirements: ./requirements-model-2.txt
```

For each virtual environment, you can specify the associated dependencies either by passing in a list of Python
requirements under the dependencies key, or by providing a filepath to a requirements.txt or pyproject.toml
file under the requirements key.

Then, to run a specific resolver in one of these virtual environments, you can reference your virtual environment
using the name specified in your chalk.yaml file in the @before_all, @online, and @offline decorators.
For your @before_all functions, if there is no venv specified, the function will run in every
virtual environment. Otherwise, if there is a venv specified, the function will only run in the specified
virtual environment. Otherwise, @online and @offline resolvers will default to run using the default virtual
environment, unless a different venv is specified.

```
from chalk import before_all, online, offline, Features
from src.models import User

# this will run in all venvs
@before_all()
def before_all_hook():
    from services import msvc

    msvc_client = msvc.Client()

# runs **only** in specified venv
@before_all(venv="model-1")
def before_all_model_1():
    from models import Model1

    model_1 = Model1.load()

# runs **only** in specified venv
@before_all(venv="model-2")
def before_all_model_2():
    from models import Model2

    model_2 = Model2.load()

# runs using default venv
@online
def get_user_email_domain(
    email: User.email
) -> Features[User.email_handle, User.email_domain]:
    handle, domain = email.split("@")
    return User(email_handle=handle, email_domain=domain)

# runs using model-1 venv
@online(venv="model-1")
def get_user_risk_score_1(
    id: User.id,
    email_domain: User.email_domain,
    recent_activity_count: User.recent_activity_count["7d"]
) ->User.is_fraud_1:
    threshold = msvc_client.get_model_threshold("model-1")
    return model_1.predict(id, email_domain, recent_activity_count).sum() > threshold

# runs using model-2 venv
@online(venv="model-2")
def get_user_risk_score_2(
    id: User.id,
    email_domain: User.email_domain,
    recent_activity_count: User.recent_activity_count["7d"]
) -> User.is_fraud_2:
    threshold = msvc_client.get_model_threshold("model-2")
    return model_2.predict(id, email_domain, recent_activity_count).sum() > threshold
```

### Pinning Chalk Platform Versions

By default, when you deploy in your Chalk environment, Chalk will pull the latest version of the Chalk platform.
You can choose to pin a Chalk platform version  for each environment such that your deployments
will only update your Chalk code, and will use the same platform image until you deploy a new pinned platform
version.

```
project: my-project-id
environments:
  dev:
    runtime: python312
    requirements: requirements-dev.txt
    platform_version: v3.27.30
  staging:
    runtime: python312
    requirements: requirements-staging.txt
    platform_version: v3.27.30
  prod:
    runtime: python312
    requirements: requirements.txt
    platform_version: v3.27.30
```

# Best Practices
source: https://docs.chalk.ai/docs/best-practices

## Learn our best practices for building and maintaining your Chalk solution

With Chalk, the same solution can be implemented in a number of different ways. Below are some guidelines
and recommended patterns for building and maintaining your Chalk solution!

### Data Sources/Integrations

### Test your data source connections

Define integrations through the Chalk dashboard and check that they're connecting properly using the Test Data Source button.
Test Data Source

### Avoid naming your data sources by their "type", e.g. don't call your Postgres data source "postgres"

Though this works, it can lead to ambiguity in SQL resolvers when you add multiple data sources of the same type. This occurs
because Chalk lets you refer to data sources by their type if you've only linked one data source of that type to Chalk. In
general, to future-proof your resolvers, you should refer to them by their name.

### Features

### Start by defining your features

Features fully specify what you want your data to look like. Once you have an understanding of the inner relations, writing resolvers for your features becomes easier.

### Avoid dataclass feature types, instead use separate feature classes or unpack the data

While Chalk allows for dataclass feature types, they should be avoided. They don't always play nicely with serialization and can cause tough-to-debug errors. We recommend
either unpacking the nested class into basic types or defining and joining an additional Chalk feature class if the nested component is truly a separate entity. Defining a
separate feature class also makes the underlying data easier to monitor and test.

### Tag and annotate your features

We strongly recommend annotating your features as you are developing them. Your feature annotations show up in the Chalk
dashboard and are a good way of documenting your code. You can also add tags and owners to your features, which can
be used for aggregation and filtering in the Chalk Dashboard.

```
from chalk.features import features
from datetime import datetime

@features
class User:
  id: str

  # the user's fullname
  # :owner: mary.shelley@aol.com
  # :tags: team:identity, priority:high
  name: str

  # the user's birthdate
  # :owner: mary.shelley@aol.com
  # :tags: team:identity, priority:high
  birthday: datetime
```

If you want to apply a tag or owner to all features in a feature class, this
should be done in the feature decorator, like so:

```
from chalk.features import features

@features(owner="ada.lovelace@aol.com", tags=['group:risk'])
class User:
  id: str

  # the user's fullname.
  name: str
```

You can also apply restrictions or enforce feature annotation for your entire project.
For instance, you can block deployment if features are not tagged or described.

### Keep feature definitions separated from resolvers

Features should be defined in separate files from resolvers (except underscore features).

### When starting your Chalk implementation, define all your feature classes in the same file

Although it can get a bit lengthy, we recommend starting by defining your features in a single file.
This makes expressing joins between features easier and prevents circular dependencies.

### Add Validations For Your Features

Validations for your features can prevent incorrect
data from being written to your offline store. They can provide an even stricter
complement to monitoring, ensuring that nothing
is going wrong with the feature you are calculating.

### Use implicit join syntax

Joins between feature classes can be specified in a number of different ways.
We recommend using an implicit join syntax, which
we cover in the join section of the docs.

### Resolvers

### Use SQL resolvers to read data from your raw datasets

While Python resolvers can be used to read data from your data sources, SQL resolvers are preferred. SQL resolvers
allow for direct execution against your data sources and additional optimizations, making them more efficient.

### Explicitly list columns in a select statement for SQL file resolvers

Select statements in SQL resolvers should be explicit. Avoid using the * syntax.

### Give Python resolvers and SQL filenames clear names

Resolver names are used in the Chalk dashboard to identify resolvers. They should be clear and concise.

### Make sure your resolvers operate inside a single feature space

Resolver inputs and outputs must belong to the same feature class, but joins can allow resolvers to connect data between feature classes.

### Transform your Chalk DataFrame to Pandas or Polars

Don't worry about converting Chalk DataFrames to Pandas or Polars in a Python resolver—the transformation is cheap. We use arrow (and so do Pandas and Polars) so moving data from a Chalk DataFrame to either is close to free

### Querying

### Run simple queries with the Chalk CLI, for more flexibility use one of Chalk's API clients

The Chalk CLI should be used to run simple online queries. For more complex use cases, you should use one of Chalk's API clients.

### Run large queries asynchronously

When sending large or long-running queries, use
run_asynchronously to set up one Kubernetes pod per input,
separate from your production and branch servers. You can configure resources for asynchronous offline queries in your
dashboard settings. You can also terminate asynchronous queries through the dashboard by terminating the pod or
canceling the query within the dashboard, which is not possible for synchronous queries.

### Create named queries for your commonly executed queries

With Chalk, you can alias your complex queries using a NamedQuery. Named queries help simplify and document your
query patterns.

To define a named query, add a NamedQuery object to your Chalk deployment:

```
from chalk import NamedQuery
from src.models import User

NamedQuery(
    name="fraud",
    input=[User.id],
    output=[
        User.email_age_days,
        User.denylisted,
        User.credit_report.flags,
    ],
    tags=["team:fraud"],
    staleness={
        User.credit_report.flags: "30d"
    },
    owner="jodie@chalk.ai",
    description="Primary fraud model for signup",
)
```

Running chalk apply makes the query name available as an alias for executing your more complex queries.

For instance, running:

```
chalk query --in user.id=1 --query-name fraud
```

is equivalent to running the more complicated:

```
chalk query \
  --in user.id=1 \
  --out user.email_age_days \
  --out user.denylisted \
  --out user.credit_report.flags \
  --staleness user.credit_report.flags=30d \
  --tag team:fraud
```

This feature is also accessible in all of our API clients through the query_name parameter.
For instance, in python, you can run:

```
from chalk.client import ChalkClient

ChalkClient().query(
    input={"user.id": 1},
    query_name="fraud",
)
```

To see all the named queries you've defined in your current active deployment, you can run:

```
chalk named-query list
```

If you want to create multiple versions of a similar queries, you can use the version parameter of the NamedQuery object
and the query_name_version parameter of our various clients.

### Deployment

### Customize your Chalk project with configuration files

Chalk expects to find a chalk.yaml file in your project's root repository. This file stores configuration for your
deployment (such as your Dockerfile and Python requirements). You can find a sample Chalk project repository
structure and more details in our configuration documentation. You'll also find details on how to
exclude files from your deployment with .chalkignore.

### Code changes should be tested and queried on the branch server.

Use the branch server to test that your deployments and new features are behaving as expected.

### Use the @before_all decorator to configure global variables for your resolvers

Global setup for resolvers should be done through a function decorated with the @before_all decorator. This also allows for unique setups for different environments.

### Custom files such as machine learning models are accessed with the TARGET_ROOT environment variable

To access files packaged in your chalk deployments, use the TARGET_ROOT environment variable to fully specify the path to your files.

For instance, if you have the following directory which you are deploying to Chalk:

```
example/
├── chalk.yaml
├── features.py
├── model.joblib
└── resolvers.py
```

You would access the model.joblib file as follows:

```
import os
model_file_path=f"{os.environ['TARGET_ROOT']}/model.joblib"
```

### Observability / Testing

### Set up monitoring on your most important features and resolvers early

Monitoring helps you catch tricky bugs early and gives you guarantees about the data you are generating and serving. You should configure monitoring for your
important features and resolvers early in your implementation.

### Unit test your resolvers to make sure they're functioning as expected

Chalk makes it easy to set up unit tests for your resolvers using Pytest or any other python testing framework.

### Improve CI/CD in your Chalk repository using our GitHub Actions workflow

Chalk has a GitHub Actions integration—you can use it to create branch deployments or run queries
as part of your code development cycle.

### Security

### Generate and use access tokens to set and restrict the permissions for your different users

Scope your Chalk user permissions with access tokens.
These can be programmatically generated through
Chalk clients or in the dashboard. Give your users only the permissions they need.

# Common Errors
source: https://docs.chalk.ai/docs/debugging-errors

## Learn techniques for debugging different elements of Chalk.

We've compiled some common errors that people come across, as well as some approaches to debug these errors
and their most common root causes. If you are still struggling to debug, please reach out in your support channel!

### Query Errors

These are errors you would encounter when running queries, either manual or orchestrated.

### Unexpected query results

If you're receiving either 0 rows when you expect a non-zero query result, or if the feature values that you're seeing
in your query results do not match what you're expecting, we recommend that you follow the steps in
our guide for debugging queries. This includes some common tips and
tricks, such as using store_plan_stages and stepping through the query plan.

### Unexpected Chalk server error with status code 401

The 401 status code means unauthenticated. We'd recommend verifying that the token you're using to run the query is
correct. To refresh your token, you can run chalk login from the terminal using our CLI and then chalk config
to verify that your token has been provisioned for the right environment.

### Unexpected Chalk server error with status code 500

The 500 status code means internal server error. This should usually come with another message with more details on
the root cause of the error. If you are struggling to debug this, please reach out to us!

### Unexpected Chalk server error with status code 502

The 502 status code means bad gateway, which usually indicates timeout or not enough servers. We'd recommend
looking at CPU utilization on your cluster to determine if you need to modify the cloud resource configurations. You
can do so in the Settings > Resources page in the Chalk dashboard by modifying and applying resource configuration JSON
changes under Advanced Resource Configuration. However, we'd also encourage reaching out to us for discussion on how
to optimize resource configuration for your environment!

### Query Timeout / Unclear Failure

If you are executing a long-running query from a notebook or somewhere locally, the client's polling for query status
might have a timeout shorter than the query's runtime. If the query times out before completion, we'd recommend
verifying whether the query is still running in the dashboard by looking at the query run page and validating that there
is a pod in the cluster running the query. It's possible that your query may also complete after the polling timeout,
in which case you can view the query status in the dashboard.

### Please double check that all features have resolvers and resolvers do not have circular dependencies.

The first thing to validate is that every feature can be mapped to a resolver output.
If all features have resolvers, then you might see this error message if Chalk is unable to construct a dependency
graph for resolving the features that you are querying. This is usually a result of a join that cannot be processed.
Please reduce the number of output features in your query until you have identified a minimal set that reproduces the
circular dependency error and reach out to us with this context!

### Duplicate Resolver Shortname

The first thing to check is whether there actually are duplicate resolvers by the same name. If there are not, this
error message can also sometimes be an indicator of a missing import. If you are unable to determine if your recent
changes required an import, you can use a linting tool to find out, such as pylint.

### chalk apply Errors

These are errors you would encounter when running chalk apply or chalk apply --branch.

### Branch server might still be starting

You would usually encounter this error when running chalk apply --branch. In the Chalk dashboard under Branches, you
can check the status of the branch server. You can also kill lingering processes on branches, such as long-running
queries, by stopping and restarting the branch server in the dashboard.

### Could not connect to server when running chalk apply

If you've verified that you have a token and are properly authenticated, then you should also verify what role you
have within the Chalk environment. The developer role can only run chalk apply --branch rather than chalk apply.

### Deployed Errors

These are errors that you might observe through metrics monitors on deployed and orchestrated features and resolvers,
as opposed to errors you would encounter in local development.

### Elevated number of errors (e.g. 502/504's)

Typically, these errors are an indication of a misalignment in load and resource configuration. Please reach out to us
in your support channels with context on data scale and current resource configurations and we can help you identify
mitigation strategies to avoid these errors!

### Returning stale features

If you're seeing stale features, we'd recommend ensuring that you have
max_staleness set for the features to configure the maximum staleness
allowed for the features, so that Chalk will know to recompute fresh values as specified.

# Debugging Queries
source: https://docs.chalk.ai/docs/debugging-queries

## Learn techniques for debugging online and offline queries

Online and offline queries can fuse data from multiple sources, and the structure of how data flows
through queries can be complex. Chalk has a number of tools to help you debug queries. In this section, we'll
explore how to use these tools on a few simple features and resolvers.

First, we'll define our feature classes. We'll work with a User and a Transaction object, representing
users performing financial transactions. In this scenario, we'll write a simple aggregation that has a bug
in its definition, and explore various ways to debug that issue.

```
from datetime import datetime
from chalk.features import features, DataFrame

@features
class Transaction:
    id: int
    user_id: "User.id"
    amount: float
    ts: datetime

@features
class User:
    id: int
    sum_transaction_amount: float
    transactions: DataFrame[Transaction]
```

Then, we'll define simple online resolvers to ingest user and transaction data from a Postgres database:

```
-- resolves: User
-- source: postgres

select id from users
```

```
-- resolves: Transaction
-- source: postgres

select id, user_id, amount, ts from transactions
```

Next, we'll write a simple (buggy) aggregation resolver to compute the sum of a user's transactions:

```
from chalk import online

@online
def sum_transaction_amount(txns: User.transactions[Transaction.amount]) -> User.sum_transaction_amount:
    return txns[Transaction.amount].count() # this 'count' is a bug! we'll debug it shortly.
```

Notice that we've defined this aggregation with a bug! We're actually computing the count of the User's
Transactions, rather than the sum of their amounts.

Let's run a query --

```
data = ChalkClient().query(input={User.id: 1}, output=[User.sum_transaction_amount])

print(data.get_value(User.sum_transaction_amount))

# Outputs 100!!
```

Whoops! Because we have prior knowledge of our data, we know that 100 is the wrong value for User 1s transaction sum.
Let's debug this issue.

### Query Plan Visualizer

The query plan visualizer is a tool that allows you to see the structure of a query, and also inspect the data that
flows through it.

To make full use of the query plan visualizer, we can re-execute the previous query with the store_plan_stages=True kwarg.
This stores all of the data that passes through each stage of the query plan.

```
ChalkClient.query(input={User.id: 1}, output=[User.sum_transactions], store_plan_stages=True)

# -or to debug multiple users at once-
ChalkClient.offline_query(input={User.id: [1,2,3]}, output=[User.sum_transactions], store_plan_stages=True)
```

Then, we navigate to the 'Queries' tab in the web dashboard. Our query appear under the
'Online' or 'Offline' tab depending on which kind of query. Here we'll take a look at the online query, and we
can see the structure of the query:

Query Plan Visualizer

The query plan visualizer shows us the structure of the query. Note that the transaction resolver is executed
to fetch the transactions for each user, and then the sum_transaction_amount resolver is executed to compute
the sum.

We can also see the data that flows through the query. Clicking on the transaction resolver shows us the output
of the resolver:

Transaction Output

Notice that the sum of the transaction amounts is definitely not 100! By inspecting the transaction.amount column
we notice that the sum should be much larger. If we were paying attention, we'd probably notice that our (incorrect) output
100 happens to be identical to the count summary of the transaction resolver, which would be a good hint that
our aggregation is actually computing the count of the transactions, rather than the sum of their amounts.

However, if we're having a slow day and don't notice that the aggregation happens to match the count, we have more
tools we can use to debug. The next section will walk through how to execute the aggregation locally using
the raw input data, so we can use a debugger.

(Note: the query plan visualizer UI displays the first 20 rows of each stage of the query plan in the preview areas.
If you want to see more, click "Download data" to download the raw parquet file.)

### Resolver Replay

Resolver execution can be examined using the Query Plan Visualizer, but Chalk also allows you to directly
execute your resolver on your local computer using the same arguments that were used in your query.

To use the resolver_replay functionality:

- Run an offline_query with store_plan_stages=True to store the query plan stages, and recompute_features=True to allow resolver execution.
- On the returned dataset, call resolver_replay with your resolver function.

Example:

```
from chalk.client import ChalkClient

ChalkClient().offline_query(
    input={User.id: [1]},
    output=[User.sum_transactions],
    store_plan_stages=True,
    recompute_features=True
).resolver_replay(sum_transaction_amount)
```

This will execute the resolver locally, using the same input data that was used in the query. This allows you to debug
using your IDE (VS Code, PyCharm, or even pdb):

Debugger

You can edit the definition of the resolver locally, and re-run resolver_replay to see the results of your changes
in your terminal or by stepping through with a debugger.

### Using logs to debug

If you're not able to use the query plan visualizer or resolver replay, you can also use the logs to debug your query.
Use the chalk_logger from the chalk.clogging just like a standard python logger. This logger will output
to the web interface, and to configured log sinks (for example, a DataDog instance).

```
from chalk.clogging import chalk_logger

@online
def sum_transaction_amount(txns: User.transaction[Transaction.amount]) -> User.sum_transaction_amount:
    chalk_logger.info(f"Transactions: {txns}")
    return txns[Transaction.amount].count() # this 'count' is a bug! we'll debug it shortly.
```

You can also view these logs using resolver_replay, where they will be emitted to your terminal:

Logs output example

### Query Error Categories

In using the debugging techniques above, you may encounter a few different categories of errors
that have common root causes:

### Request error

Request errors are raised before your resolver code executes.
They are often caused by invalid feature names in the input or by requests that
cannot be satisfied by the resolvers you have defined.

### Feature error

Feature errors are raised when a specific resolver that maps to a feature fails.
For this type of error, you'll find a feature and resolver
attribute in the error type.

When a resolver crashes, you will receive null value in the response.
To differentiate from a resolver returning a null value and
a failure in the resolver, you need to check the error schema.

### Network error

Network errors are thrown outside your resolvers.
They can be caused by unauthenticated requests or other connection failures.

### Error schema

The online query interface for resolvers returns the following schema:

### Response Schema

The outputs features and any query metadata (discussed in detail at
Query Basics.)

Errors encountered while running the resolvers. Each element in the list is a
ChalkError. If no errors were encountered, this field is empty.

###  ChalkError

The type of error, matching one of the error codes.

The category of the error, given in the type field for the
error codes. This will be one of
"REQUEST", "NETWORK", and
"FIELD".

A readable description of the error message.

The exception that caused the failure, if applicable.

The name of the class of the exception.

The message taken from the exception.

The stacktrace produced by the code.

The fully qualified name of the failing feature, eg.
user.identity.has_voip_phone.

The fully qualified name of the failing resolver, eg.
my.project.get_fraud_score.

### Error codes

The query contained features that do not exist.

A resolver was required as part of running the dependency graph that could not be found.

The query is invalid. All supplied features need to be rooted in the same top-level entity.

A feature value did not match the expected schema (eg. incompatible type "int"; expected "str")

The resolver for a feature errored.

The resolver for a feature timed out.

A crash in a resolver that was to produce an input for the resolver crashed, and so the resolver
could not run crashed, and so the resolver could not run.

The request was submitted with an invalid authentication header.

The request has credentials that do not provide the required authorization to execute an operation.

An unspecified error occurred.

# Development with LLMs
source: https://docs.chalk.ai/docs/development-with-llms

## Use LLMs to write Chalk code with specialized prompts.

Chalk provides specialized prompts to help Large Language Models (LLMs) write effective Chalk code.
These prompts are designed to guide AI assistants in understanding Chalk's patterns, best practices,
and API conventions.

### Getting Started

- Run the chalk init agent-prompt command to add the prompt to your local repository.
- Provide specific context about your feature requirements
- Review generated code for adherence to your team's conventions
- Test the generated features in your development environment

By using these specialized prompts, you can leverage AI assistance to write more consistent
and idiomatic Chalk code while reducing development time and improving code quality.

### Agent Prompts Repository

The Chalk team maintains the public repository chalk-ai/agent-prompts
with prompts specifically designed for LLM-assisted Chalk development:

This repository contains prompts that are tested against LLM providers to help them understand:

- Chalk's feature definition patterns
- Built-in LLM integration capabilities
- Resolver implementation best practices
- Data source integration patterns
- Template interpolation syntax
- Model selection and configuration
# Frequently Asked Questions
source: https://docs.chalk.ai/docs/faq

## A collection of questions frequently asked by customers

### Getting support

The questions are sorted by category. Don't see your question answered? Please reach out via your support channel
and we will be happy to help!

### Data Sources and Infrastructure

### What is the difference between the online store and the offline store?

The online store is intended to store features for low-latency retrieval in online query.
Typically, the online store is implemented using Redis or DynamoDB.

The offline store is intended to store historical logs of all previously ingested or computed
features. It is used to compute large historical training sets. It is typically implemented using
BigQuery, Snowflake, Iceberg, or other data warehouses.

### Can we do RBAC (Role Based Access Control) within Chalk?

Yes! Within the dashboard you can assign roles with different permissions to different users. The default roles
available are shown below.

### What are the necessary steps for us to get Chalk in our system?

Please reach out via your support channel and we'd be happy to walk you through how to get Chalk setup running
on your cloud infrastructure!

### We use Okta SCIM provisioning. Can we import these roles to be used in Chalk?

Yes! You can set up Okta to automatically provision and deprovision Chalk users. For more information on how,
see here.

### How should I set up secrets to be accessible in our deployed environments?

You can configure secrets as environment variables in the Secrets tab of Settings in your Chalk dashboard, and
these secrets would then be available on the next deploy in the environments that you've specified, and on all
branches in those environments!

### Features

### Does Chalk have a feature catalog?

Yes! You can view all the features for all namespaces deployed in your environments, along with some metadata
on recent activity and updates.

### How should I use feature versioning?

You can define versions for features if, for example, you are iterating on feature definitions. We'd recommend
setting a default feature version for ensuring consistency across feature references. For more information, please
see this tutorial on feature versions

### How does FeatureTime work? Should I override FeatureTime with timestamps from existing data sources?

Feature time is the time at which a feature was observed. By default, feature time is set to the feature's resolver
execution time. You can override feature time and may want to do so if you're ingesting historical data.
For more information on how feature times work, see our time documentation.

### How should I structure my windowed features? What kind of windows can I use?

We recommend writing windowed features for aggregated computations over
different time periods. You can define the different windows in terms of weeks, days, hours, minutes,
or even seconds (weeks="w", days="d", hours="h", minutes="m", seconds="s"). Under the hood, we normalize the
time representations into durations in seconds, so you would have multiple syntactical options for accessing
different windows for features. We recommend setting default values for windowed features in case there are
windows with no events during the specified time period. Otherwise, you can write resolvers defining how
your windowed features should be computed and pass windowed features as inputs into resolvers just like normal
features!

### Can I upload features into the online store with an API endpoint?

Yes! In addition to streaming and scheduled bulk ingests of features, you can submit requests using
the upload_features SDK endpoints to synchronously ingest features into the online or offline stores
using API clients.

### Resolvers

### What is the difference between an online and offline resolver?

Not much! The only difference is in which contexts the resolvers are executed.
A few key scenarios:

- in "online query" (i.e. queries submitted via .query, .query_bulk, multi_query), offline resolvers never execute.
- in "offline query" (i.e. queries submitted via .offline_query), offline resolvers are preferred, taking precedence over online resolvers that compute the same features.
- in offline query, online resolvers are permitted to execute

@offline is intended to be used for resolvers whose backing data sources are too slow or expensive
to fulfill online query requests -- i.e. data warehouses or certain API sources, but
if your query requests can tolerate the latency of one of these slow sources, you can mark resolvers
using those datasources @online to query them on-the-fly.

On the other hand, if your query requests can't tolerate the latency of the underlying data store,
evaluate using scheduled ingestion or streaming resolvers in order to ensure that fresh
data is available in the online store.

### How do I force certain resolvers to execute in my query?

Make use of tags=[...]. If a resolver is marked with a tag, it is only eligible to execute in
queries that have a matching tag. An even stricter variant of this concept is available with the
required_resolver_tags argument to query and offline_query which allows you to force all
resolvers to have a particular tag.

### How do I know when my resolver will run and when it will time out?

You can set cron schedules for your resolvers, which will be parsed in
your local system's timezone. You can also set customized timeouts for resolvers.
Chalk currently has a max timeout of 18 hours for resolvers, but if this does not suit your needs, please reach out
to us in your support channel with a description of your compute needs for your resolver!

### How do I know if my resolver is still running?

The best way to check if your resolver is still running is to see if there are still resources provisioned to run
your resolver. For scheduled resolver runs, you can view an overview of Run History as well as a view of Cloud
Resources dedicated to scheduled resolver runs under the Runs tab on the menu sidebar. For triggered resolver
runs, you can also find which pod is running your resolver on the run page. Finally, if you navigate to
Settings > Resources you can view all pods currently running in your cluster, whether for resolver runs or
queries.

### How should I work with dataframes in my resolvers?

You can define resolvers with DataFrame inputs or outputs, which uses the
Chalk DataFrame structure. You can do some aggregations and projections
using the Chalk DataFrame, but you can also convert the Chalk DataFrames into Pandas or Polars using .to_pandas()
and .to_polars() for more data manipulation.

### Querying

### Can I query for two different feature classes in a single query?

We recommend creating a "root" feature class that models the interaction between the two entities -- i.e.
if need "customer" and "business" features for a transaction fraud model, you might create a class like this:

```
@features
class AuthQuery:
    # A unique ID that represents this interaction; may be randomly generated if you have
    # no natural ID in your system.
    id: str

    # A reference to the relevant customer.
    customer_id: "Customer.id"
    customer: Customer
    # A reference to the relevant business.
    business_id: "Business.id"
    business: Business
```

Then, queries can be submitted using:

```
ChalkClient().query(
    input={
        AuthQuery.id: ...,
        AuthQuery.customer_id: ...,
        AuthQuery.business_id: ...,
    },
    output=[
        AuthQuery.customer, 
        AuthQuery.business,
    ]
)
```

### How do I query for multiple entities at the same time?

Use the .query_bulk SDK method instead of .query. For example, to query features for multiple Hospital entities, you might use:

```
result = ChalkClient().query_bulk(
    input={Hospital.id: [1,2,3,4,5]}
    output=[Hospital.current_waiting_time, Hospital.has_trauma_bay, Hospital.has_er, Hospital.has_mri]
)

df = result[0].to_pandas()
```

### How do I tell if my offline query is still running if it shows as In Progress in the UI?

The first thing to check is whether there is a pod in your cluster running your offline query. You can verify this
by viewing the pods running under Settings > Resources. If you're running an offline query from a notebook, then
the polling may timeout even if the offline query is still running, so the best way to verify the status of your
offline query is a combination of checking the query run in dashboard and the status of pods in the cluster. For more
visibility, you can also add the run_asynchronously=True argument to ChalkClient.offline_query to explicitly run
your offline query on an isolated worker so you can use the worker status as a query status.

### How do I sample instances of a feature class?

You can query for random instances of a feature class by running an offline query and specifying the max_samples
parameter. For instance, running the example query below will sample ten random users from the User feature class,
returning the features specified by the output parameters: [User.id, User.name, User.age].

```
from chalk.client import ChalkClient
from datetime import datetime

from src.feature_sets import User

client = ChalkClient()

dataset = client.offline_query(
  output=[User.id, User.name, User.age],
  max_samples=10,
  recompute_features=True
)
df = dataset.get_data_as_pandas()
```

### Deployment

### How are resources provisioned for my Chalk cluster, and can I modify the configuration?

We have default resource configurations for general environments.
You can modify the configuration for your project's cloud resources by modifying the specs under
Settings > Resources  > Advanced Resource Configuration. You must hit Save and Apply Changes in order for
your configuration changes to go through. If you are not sure how you should configure your cloud resources,
please reach out to us in your support channel!

### Can I suspend or delete branches when they are not in use?

You cannot currently suspend or delete branches, but stale branches do not consume resources, so there is no cost
or performance impact from old branches.

### Observability and Testing

### Is my (resolver / query) running?

See answers above under Resolvers and Querying respectively!

### How do I setup a sensor so that I can run something else after a resolver run?

If you are triggering a resolver run as part of an orchestrated pipeline, we usually see customers using the
built-in sensors from the orchestrators (e.g. Airflow or Dagster) to poll for resolver completion. You can
also customize this polling using an API to query run status.
See here for an example
of how to set up Airflow orchestration to trigger and poll a resolver run.

### Roadmap

### What have the people at Chalk been working on?

To get a glimpse of recently released features, take a look at our changelog!

### I want to request a feature!

Feel free to reach out to us with feature requests or questions about feature requests in your support channel!

# Features Overview
source: https://docs.chalk.ai/docs/features

## Define features for training and inference.

Chalk lets you spell out your features directly in Python.
Features are namespaced to a FeatureSet.
To create a new FeatureSet, apply the @features
decorator to a Python class with typed attributes.
A FeatureSet is constructed and functions much like
Python's own
dataclass.

### Example

```
from datetime import datetime
from typing import Optional
from chalk.features import features

@features
class User:
    id: int
    full_name: str
    nickname: Optional[str]
    email: Optional[str]
    birthday: datetime
    fraud_score: float
```

### Namespacing

Features are namespaced by their containing FeatureSet,
and then by the name of the variable.

In the above example, our features, when rendered as strings, are:

| Feature Name     | Type                                                                                                             |
| ---------------- | ---------------------------------------------------------------------------------------------------------------- |
| user.id          |  Integer         |
| user.full_name   |  String          |
| user.nickname    |  String | None  |
| user.email       |  String | None  |
| user.birthday    |  Datetime        |
| user.fraud_score |  Decimal         |

(FeatureSet names are stripped of the suffix "Features",
if it exists).

### Overrides

Feature names and feature classes can be overridden by supplying
the name keyword argument to the feature function or the @features decorator.
This practice allows us to evolve our variable names without
losing the past history of this feature.

```
- @features
+ @features(name="prince")
- class Prince:
+ class TheArtistFormerlyKnownAsPrince:
-   birthday: datetime
+   date_of_birth: datetime = feature(name="**birthday**")
```

### Primary keys

Feature sets must all have a primary key.
This primary key is used to index storage for features you later resolve
in this feature class. Your primary key can have type int or str,
given by the type annotation on the field.

By default, if you have a feature with the name id,
that feature will be the primary key.
However, you can override this behavior:

```
from chalk.features import features, Primary

@features
class User:
    user_id: Primary[str]
    ...
```

If you mark an explicit primary key, it will override the default behavior:

```
@features
class User:
    user_id: Primary[str]
    # Not really the primary key!
    id: str
```

Alternatively, you can use the feature function
to set a feature to primary:

```
from chalk.features import features, feature

@features
class User:
    user_id: str = feature(primary=True)
```

### Versions

Chalk versions all of your features with every deployment.
However, you can also choose explicit versions for your
features.

```
@features
class User:
    ...
    email_domain: str = feature(version=2)
```

### Feature time

By default, Chalk marks the time a feature was created as the time that
its resolver was run.
However, you may want to provide a custom value for this time
for data sources like events tables.

You can inspect the time a feature was created and set the time
for when a feature was created by creating a feature of type
FeatureTime.

To set the time a feature was created, assign the feature
when you resolve it:

```
@offline
def fn(uid: User.uuid) -> Features[User.name, User.ts]:
    return User(
        name="Anousheh Ansari",
        ts=datetime(month=9, day=12, year=1966)
    )
```

Then, when you sample offline data,
the name feature will be treated as having been created at
the provided date.

### Constructing feature classes

To construct a User instance, supply the feature values
to the __init__() method

```
User(full_name="Grace Hopper", nickname="Amazing Grace")
User(email="grace.hopper@yale.edu")
```

The @features decorator adds a custom __init__():

```
def __init__(
    self,
    uid: int | MISSING = MISSING,
    full_name: str | MISSING = MISSING,
    email: Optional[str] | MISSING = MISSING,
    ...
):
    self.uid = uid
    self.full_name = full_name
    self.email = email
    ...
```

Note that all fields have a default MISSING value.
Therefore, you can construct feature classes with any subset
of the fields you would like to use.

### Refactoring

After going to production, you may find that you want to change
the name of a property on the feature class.
You can change the name of a feature property without changing
the underlying data using the name override.
From the example in the namespacing section,
if you initially called a feature birthday,
and decided to rename it date_of_birth,
you can keep the underlying data the same and rename the property
on the class as follows:

Here, we also rename the feature class originally named Prince
to TheArtistFormerlyKnownAsPrince.

### Interplay with auto-id

Where the name of the Python property
and the name provided to feature(name=...) differ,
IDs are auto-assigned based
on the name provided to feature(name=...).

### Default feature values

For features that can't always be computed, you can pass default to
feature or assign a default directly:

```
from chalk.features import features
@features
class User:
    id: int
+   num_purchases: int = 0
+   count_logins: int = feature(default=0)
```

# Feature Types
source: https://docs.chalk.ai/docs/feature-types

## Define features for training and inference.

### Scalars

Features can be any primitive Python type:

```
from enum import Enum

class Genre(Enum):
    FICTION = "FICTION"
    NONFICTION = "NONFICTION"
    DRAMA = "DRAMA"
    POETRY = "POETRY"

@features
class Book:
    id: int
    name: str
    publish_date: date
    copyright_ended_at: datetime | None
    genre: Genre

```

In addition to the primitive Python types (int, float, str, bool), Chalk also supports
date, datetime, and the Chalk FeatureTime as
scalar feature types.

### Lists and Sets

Features can be a list or set of scalar or struct types.

```
@dataclass
class Chapter:
    start_page: int
    end_page: int

@features
class Book:
    authors: list[str]
    categories: set[str]
    chapters: list[Chapter]
```

### Structs

Features can be a struct, which is a collection that maps a fixed set of keys to sub-fields. You can use
dataclasses, Pydantic models, and
attrs classes to represent struct features. Struct features can be used recursively
within list features or other struct features.

Struct types should be used for objects that don't have ids. If an object has an id, consider using has-one.

### Dataclass

You can use any dataclass as a struct feature.

```
@dataclass
class JacketInfo:
    title: str
    subtitle: str
    body: str

@features
class Book:
    id: int
    jacket_info: JacketInfo
```

### Pydantic models

Pydantic models can also be used for structs.

```
from pydantic import BaseModel, constr

class TitleInfo(BaseModel):
    heading: constr(min_length=2)
    subheading: Optional[str]

@features
class Book:
    title: TitleInfo
    ...
```

### Attrs

Alternatively, you can use attrs.

```
import attrs

@attrs.define
class TableOfContentsItem:
    foo: str
    bar: int

@features
class Book:
    table_of_contents: list[TableOfContentsItem]
    ...
```

### Document

Both dataclass and Pydantic
structs are implemented using the PyArrow
serialization format, a high-performance schema for data serialization.
This data is stored "value only", i.e. without keys, so any change to these structs over time will invalidate historical data.
To support feature values where the schema changes over time, we introduced the Document struct type.
Documents are serialized as JSON and supports changes to schema over time, at the cost of a small performance penalty.

```
from pydantic import BaseModel
from chalk import Document

class AuthorInfo(BaseModel):
    first_name: str
    last_name: str

@features
class Book:
    title: Document[AuthorInfo]
    ...
```

### Vectors

Features can be vectors (fixed sized arrays of floats), such as the output from an embedding model.
Unlike list or set features, vector features are compatible with embedding functions
and nearest neighbor similarity search.

```
from chalk.features import features, Vector

@features
class Document:
    embedding: Vector[1536]  # Defines a vector with 1536 dimensions
```

When using the built-in embedding functions, then the vector dimensions don't need to be specified, as Chalk will automatically infer it
from the embedding model.

```
from chalk.features import embed, features, Vector

@features
class Document:
    content: str
    # Chalk knows that text-embedding-ada-002 has 1536 dimensions
    embedding: Vector = embed(
        input=lambda: Document.content,
        provider="openai",
        model="text-embedding-ada-002"
    )
```

By default, vectors are persisted as 16 bit floats for efficiency. However, Chalk also supports persisting vectors as 32-bit or 64-bit floats via the keywords
"f32" and "f64", respectively.

```
from chalk.features import Vector

@features
class Document:
    # Defines a vector with 1536 dimensions that will be persisted with 32 bit precision
    embedding: Vector["fp32", 1536]
```

### Custom serializers

Finally, if you have an object that you want to serialize that isn't
from dataclass, attrs, or pydantic, you can write a custom codec.
This custom codec must target a type that can be serialized to a PyArrow
data type, which
is the underlying serialization format for all features.

Consider the custom class below:

```
class CustomStruct:
    def __init__(self, foo: str, bar: int) -> None:
        self.foo = foo
        self.bar = bar

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, CustomStruct)
            and self.foo == other.bar
            and self.bar == other.bar
        )

    def __hash__(self) -> int:
        return hash((self.foo, self.bar))
```

Here, we use the custom class as a feature, and provide an encoder and decoder.
The encoder takes an instance of the custom type and outputs a Python object, and
the decoder takes output of the encoder and creates an instance of the custom type

```
@features
class Book:
    custom_field: CustomStruct = feature(
        encoder=lambda x: dict(foo=x.foo, bar=x.bar),
        decoder=lambda x: CustomStruct(**x),
    )
```

# Discovery
source: https://docs.chalk.ai/docs/feature-discovery

## Declare owners and metadata for features.

Features can capture metadata to inform
alerting, monitoring, and discovery.
By default, features are created as any type-annotated
variable of a class decorated with @features.
However, you may also assign these variables to the
result of the chalk.features.feature(...) function
to provide metadata.

### Description

Descriptions are parsed from the comments preceding
the feature definition. For example, you can document a
fraud_score feature with information about the values
as follows:

```
@features
class User:
    # **0 to 100 score indicating an identity match.**
    # **Low scores indicate safer users**
    fraud_score: float
    ...
```

You can alternatively provide a description of a feature
directly in the code. The following example is equivalent to
explicitly providing the description as above:

```
@features
class User:
    fraud_score: float = feature(description="""
           **0 to 100 score indicating an identity match.**
           **Low scores indicate safer users**
        """)
    ...
```

If both an explicit description and a comment are present,
the description will be set to the explicit value from
feature(description=...).

You can programmatically access the description for a feature
with the description(...) function:

```
from chalk.feature import description
print(description(User.fraud_score))
```

### Owner

You may also specify which person or group is responsible for an individual feature.
The owner tag will be available in Chalk's web portal.
Alerts that do not otherwise have an owner will be assigned
to the owner of the monitored feature.
Owners are parsed from the source code. For example:

```
@features
class User:
    full_name: str
    # :owner: **katherine.johnson@nasa.gov**
    fraud_score: float
    ...
```

You may instead choose to specify an owner via a keyword argument to
feature().
For example:

```
@features
class User:
    full_name: str
    fraud_score: float = feature(owner="**katherine.johnson@nasa.gov**")
    ...
```

An owner can also be assigned to every feature in a namespace via a keyword argument to @features:

```
@features(owner="**katherine.johnson@nasa.gov**")
class User:
    full_name: str
    fraud_score: float
    # :owner: **annie.easley@nasa.gov**
    email: str
    ...
```

Here, User.full_name and User.fraud_score
assume the owner katherine.johnson@nasa.gov.
However, User.email, which specifies an owner at the feature level,
assumes the owner annie.easley@nasa.gov.

You can programmatically access the owner of a feature
with the owner(...) function:

```
from chalk.feature import owner
assert owner(User.email) == "annie.easley@nasa.gov"
```

### Tags

Tags are a way of adding metadata to features for use in
filtering, aggregations, and visualizations.
For example, you can use tags to assign features to a team
and find all features for a given team.

```
@features
class User:
    # :tags: **team:identity**, **priority:high**
    fraud_score: float
    ...
```

Alternatively, you may specify tags via explicit construction:

```
@features
class User:
    fraud_score: float = feature(tags=[
        "**team:identity**",
        "**priority:high**",
    ])
    ...
```

As with the owner property, tags can be assigned to all features in a namespace:

```
@features(tags="**group:risk**")
class User:
    fraud_score: float
    # :tags: pii
    email: str
    ...
```

Here, User.fraud_score inherits the tag group:risk.
The feature User.email will also inherit this tag
in addition to the tag pii.

You can programmatically access the tags for a feature
with the tags(...) function:

```
from chalk.feature import tags
assert tags(User.email) == ["pii", "group:risk"]
```

### Semantic search

Chalk provides powerful semantic search capabilities to help you quickly find features across your entire feature catalog. You can access semantic search in two ways:

- Keyboard shortcut: Press Cmd+K (Mac) or Ctrl+K (Windows/Linux) from anywhere in the Chalk web interface
- Search button: Click the search icon in the header navigation bar

The semantic search understands natural language queries and searches across:

- Feature names and namespaces
- Feature descriptions and documentation
- Owner information
- Tags and metadata
- Resolver implementations

This makes it easy to find features even when you don't know their exact names. For example, you can search for "user risk features" or "features updated last week" or "features owned by data team".

Feature Search

### Data lineage

Understanding how features are computed and what data they depend on is critical for debugging, compliance, and impact analysis. Chalk automatically tracks and visualizes the complete data lineage for every feature.

The data lineage view shows:

- Upstream dependencies: Data sources, SQL queries, and other features that this feature depends on
- Downstream consumers: Features, models, and queries that depend on this feature
- Resolver chain: The sequence of resolvers that compute this feature
- Data sources: External databases, APIs, and streaming sources that provide raw data

You can access the lineage view by clicking on any feature in the web interface and selecting the "Lineage" tab. The interactive graph allows you to explore dependencies, trace data flow, and understand the full context of how a feature is computed.

Data Lineage

This visualization is particularly useful for:

- Impact analysis: Before modifying a feature, see what downstream features and models would be affected
- Debugging: Trace back through the computation graph to identify where issues may be occurring
- Compliance: Document data provenance for regulatory requirements
- Optimization: Identify redundant computations or opportunities to consolidate resolvers
# Feature Caching
source: https://docs.chalk.ai/docs/feature-caching

## Cache pre-computed features values in the online store

When a feature is expensive or slow to compute, you may wish to cache its value in the online store.
Chalk uses the terminology "maximum staleness" to describe how recently a feature value needs to
have been computed for the value in the online store to be returned rather than recomputing a fresh
feature value by running a resolver. The online store is typically best suited for low-latency reads
on a smaller amount of data relative to the offline store.

You can specify the maximum staleness for a feature as follows:

```
from chalk.features import feature, features
from datetime import timedelta

@features
class User:
    id: int
    # Using text descriptors:
    expensive_fraud_score: float = feature(
        max_staleness="**1m 30s**"
    )

    # Alternatively, using timedelta:
    expensive_fraud_score: float = feature(
        max_staleness=timedelta(minutes=1, seconds=30)
    )
```

Max staleness durations can be given in natural language, or specified using
datetime.timedelta.
You can specify a max staleness of "infinity" to indicate that Chalk should cache computed feature
values forever. This makes sense for data that never becomes invalid, or for data that you wish
to explicitly update using Streaming Updates or Reverse ETL.

Staleness can also be assigned to all features in a namespace:

```
from chalk.features import features, feature

@features(max_staleness="**1d**")
class User:
    id: int
    fraud_score: float
    full_name: str
    email: str = feature(max_staleness="0s")
    ...

@features(max_staleness="infinity")
class UserReport:
    user_id: Primary[User.id]
    report_data: str
    created_at: datetime
    ...
```

Here, User.fraud_score and User.full_name
assume the max-staleness of 1d.
However, User.email, which specifies max-staleness at the feature level,
assumes the max-staleness of 0s, forcing it to be recomputed on every request.

By default, features are not cached, and instead are recomputed for every online request.
In effect, you can think of max_staleness as being 0 except where otherwise specified.

### Caching indefinitely

If you want to cache a feature indefinitely, you can set the max_staleness to "infinity":

```
from chalk.features import feature, features

@features
class User:
    id: int
    fraud_score: float = feature(max_staleness="**infinity**")
```

In this example, the latest computed value for User.fraud_score will be cached indefinitely in the online store.
When a new value is computed, it will replace the old value in the online store.

### Populating the Online Store

Once you have set the max staleness for a feature, there are several ways to populate the online
store, depending on whether you want to just cache recently computed feature values or if you want
to ensure that your queries utilize the low-latency path of online store lookup.

- Online Queries: When you run an online query,
the Chalk engine will check the online store for feature values that fall within the max staleness duration
for a feature. If a feature value is found then the engine will return that value. Else, the engine will
run the associated resolver to compute a fresh feature value and store the newly computed feature value in
the online store.
- Offline Queries: When you run an offline query with the parameter
store_online=True, the feature values computed in the offline query output will be loaded into the online
store.
- Triggered Resolver Run: You can trigger a resolver run with the parameter store_online=True
to populate the online store with the feature values computed in the resolver run.
- Scheduled Queries: You can create a ScheduledQuery with the parameter
store_online=True to populate the online store with the feature values computed in the scheduled query.
- Dataset Ingest: You can ingest a Dataset to the online store using the method
dataset.ingest(store_online=True).
- ETL Offline to Online: You can set the etl_offline_to_online parameter to True in an @online or
@offline scheduled resolver to populate the online store with the feature values computed in the resolver for
features with max_staleness != 0.
- Stream: You can stream feature values to the online store for features with max_staleness != 0.

### Handling null and default values

For features with max_staleness != 0, you can also specify how you want to handle null and default feature
values. By default, Chalk will cache the computed feature value, even if it is null or the default value,
however if you set the cache_null or cache_default parameter to False, Chalk will not cache the
null/default computed feature value. Furthermore, if your online store is Redis or DynamoDB, you can also
set cache_nulls="evict_nulls" to evict cached null feature values from the online store, and
cache_defaults="evict_defaults" to evict cached default feature values from the online store.
Read more about how to handle null and default value caching here.

### Caching Cookbook

Given all of these options, which recipe should you follow for what data to cache in the online store
and how to load that data into the online store?

First, there are a few general principles to keep in mind:

- The online store is optimized for low-latency reads, so you should cache data that you want to query
quickly, usually for real-time use cases.
- The online store is not optimized for huge amounts of data, so you should cache only the data that
you need to query quickly.
- When you run an online query, if the output feature values are not found in the online store, the online
resolver will run. When you run an offline query, if the output feature values are not found in the
offline store, an offline resolver will run, or if there is no offline resolver then the online
resolver will run.

Keeping these principles in mind, here are some common use cases and how to handle them:

- If you know the specific primary keys for the data that you would like to query quickly, you canRun offline queries or dataset ingest to load data ad-hoc: Given the set of feature values that
you would like to load into the online store, you can run offline queries with store_online=True
or ingest a dataset to the online store using dataset.ingest(store_online=True).Schedule or orchestrate queries and ingests: If you would like to regularly update the
feature values in the online store, you can also orchestrate the offline queries
and dataset ingests to run at specific intervals, or use a ScheduledQuery.
- If you would like to cache all possible values for a feature in the online store, you canTrigger a resolver run: A resolver run with store_online=True will populate the online store
with all possible feature values for the resolver's output features.
- If you would like to cache recently computed data, but do not have a specific concept in mind of what
data you would like to cache, you canRun online queries: Running online queries will populate the online store with the feature values
that fall within the max staleness duration for the feature.Set etl_offline_to_online in your resolvers: If you have resolvers that
compute features with max_staleness != 0, you can set etl_offline_to_online=True to populate the
online store with the feature values computed in the resolver run.
- If you have a streaming data sourceStream feature values to the online store: You can stream feature values to the online store for
features with max_staleness != 0.

### Overriding default caching

The max_staleness values provided to the feature function
may be overridden at the time of querying for features.
See Overriding Default Caching for a detailed discussion.

### Specifying Online and Offline Storage

Chalk enables granular configuration about whether and how to store feature values in the online and offline stores.
For each feature class, the @features decorator can be used to specify whether the scalar features in the feature
class should be cached in the online store based on the max_staleness parameter. However, the feature function
enables per-feature specification of whether values computed for that feature within a feature class should be stored
in the online and offline stores using the store_online and store_offline parameters. The following example
showcases how these parameters can be used in combination to express different storage behavior.

```
from chalk.features import features, feature, DataFrame
from datetime import datetime

# due to the max_staleness parameter, all scalar features in the Driver feature class will be cached in the online
# store with a max staleness of 30 days. In addition--all of the computed feature values will be stored offline by
# default.
@features(max_staleness="30d")
class Driver:
    id: int

    # with no overrides, this feature will be stored online with max staleness of 30 days, and stored offline
    name: str

    # with an override on store_offline, this feature will be stored online with a max staleness of 30 days, but
    # will not be stored offline
    age: int = feature(store_offline=False)

    # with overrides for store_online and store_offline, computed feature values for location will not be persisted
    # in either the online or offline store
    location: str = feature(store_online=False, store_offline=False)

    # joined features are not scalar features, and hence do not inherit the storage behavior of the feature class.
    # because neither the Job feature class nor the
    jobs: "DataFrame[Job]"

    # because the Record feature class has a max staleness of 30 days, and so does the join, this join
    # would be cached on the Driver feature class
    records: "DataFrame[Record]" = has_many(lambda: Record.driver_id == Driver.id, max_staleness="30d")

# with no max_staleness set, features in the Job feature class will by default by stored offline, but not online
@features
class Job:
    id: int

    # with no overrides, this feature will be stored offline, but not online
    driver_id: Driver.id

    # with an override for store_offline, computed feature values for start_time will not be persisted
    start_time: datetime = feature(store_offline=False)

    # with overrides for store_online and store_offline, computed feature values for end_time will be persisted
    # in the online store, but not the offline store
    end_time: datetime = feature(store_online=True, store_offline=False)

# with max_staleness set, all scalar features in the Record feature class will be cached in the online store with a
# max staleness of 30 days and stored offline by default.
@features(max_staleness="30d")
class Record:
    id: int

    # with an override on max_staleness, all other features in the feature class would be cached with a max
    # staleness of 30 days, but driver_id would be cached with a max staleness of 1 day.
    driver_id: Driver.id = feature(max_staleness="1d")
    timestamp: datetime
    record_details: str
```

### Removing Cached Feature Values

There are two ways to remove cached feature values from the online store. If you would like to remove all cached
values for a specific feature or set of features, then you can use chalk drop to remove all cached
values such that none of those values would be eligible to be served from the online store. If you would like to remove
a specific cached value for a specific primary key, then you can use [chalk delete](cli/delete).

For example, if you have the feature class User.risk_score_1 and you want to remove an incorrectly computed
cached value for the user with primary key 123, you can run the following command:

```
chalk delete --keys=123 --features user.risk_score_1
```

If you have updated how risk_score_1 is computed and want to remove all cached values for the feature, you can
then run the following:

```
chalk drop --features user.risk_score_1
chalk apply
```

### LRU Caching

Chalk also supports tiered caching using an LRU cache in front of the online store. To enable LRU caching, you can
create an OnlineStoreConfig with an lru_cache, and then pass that configuration to the feature classes that you
want to cache:

```
from chalk.features import features
from chalk.stores import LRUCache, OnlineStoreConfig

lru_cache_config = OnlineStoreConfig(
    lru_cache=LRUCache(
        max_size=10000,
        ttl="60s",
        store_cache_misses=True,
    )
)

@features(online_store_config=lru_cache_config)
class User:
    id: int
    risk_score: float = feature(max_staleness="1h")
```

In this example, the User feature class is configured to use an LRU cache with a maximum size of 10,000 entries. Every worker process will maintain its own LRU cache. If a feature value is found in the LRU cache, it will be returned directly.

If it is not found in the LRU cache, the online store will be queried. If it is not found in the online store, the resolver will be run to compute a fresh value. If the store_cache_misses parameter is set to true, then a cache miss against the online store is stored in the LRU cache: subsequent requests for the same primary key will not hit the online store until the TTL of the LRU cache for the pkey expires.

# Has One
source: https://docs.chalk.ai/docs/has-one

## Define one-to-one relationships between feature classes.

Has-one relationships link a feature to a single instance of another feature.

### Recommended Implementation

The simplest way to specify a join for a has-one relationship is implicitly. In the example below,
a User is linked to their Profile.

```
from chalk.features import features

@features
class Profile:
    id: str
    user_id: "User.id"
    email_age_years: float

@features
class User:
    id: str
    profile: Profile
```

With a has-one relationship established, you can reference features on Profile through
User. For example:

```
user_email_age = User.profile.email_age_years
```

### Explicit Join

In the following snippet, the has-one join is explicitly defined. This is functionally
equivalent to the recommended implementation:

```
from chalk.features import features, has_one, ...

@features
class Profile:
    id: str
    user_id: str
    email_age_years: float

@features
class User:
    id: str
    uid: str
    profile: Profile = has_one(lambda: Profile.user_id == User.uid)
```

The lambda solves forward references, letting you reference User before it is defined.

### Composite Join Keys

You can also specify a composite join key for a has-one relationship. For example, if a User is linked to a
Profile by org and email, you can define the join as follows:

```
from chalk.features import features, has_one
from datetime import datetime

@features
class User:
    id: str
    email: str = _.alias + "-" + _.org + _.domain
    org_domain: str = _.org + _.domain
    org: str
    domain: str
    alias: str

    # join with composite key
    posts: DataFrame[Posts] = has_many(lambda: User.email == Post.email)
    # multi-feature join
    org_profile: Profile = has_one(lambda: (User.alias == Profile.email) & (User.org == Profile.org))

@features
class Workspace:
    id: str
    # join with child-class's composite key
    users: DataFrame[Users] = has_many(lambda: Workspace.id == User.org_domain)
```

### Back-references

### One-to-one

You can also add a back-reference to User from Profile.
However, you don't have to explicitly set the join on Profile.
Instead, the join condition is assumed to be symmetric and copied over.
To complete the one-to-one relationship from our example, add a User
to the Profile class:

Here you need to use quotes around User to use a forward reference.

### Optional relationships

When a has-one relationship is specified, the default behavior is to treat the linked Feature
as required. Following the example above, specifying a User without a Profile and
querying for a User's profile or using the User.profile in a resolver raises an
error.

To define optional relationships, use the typing.Optional[...] keyword:

Note, resolvers that take optional features as inputs need to handle the None case. This is
covered in more detail in the resolver's section of the docs.

### Chained Has-One Joins

You can chain has-one joins to traverse multiple relationships. For example, you could define
the following features to represent a user's profile and preferences in an application.

```
from chalk.features import features, Primary

@features
class User:
    id: str
    email: str

@features
class Profile:
    id: Primary[User.id]
    username: str

@features
class Preferences:
    id: Primary[Profile.id]
    dark_mode: bool


```

### Organizing Feature Definitions Across Files

In large projects, it's common to split feature definitions across multiple Python modules.
For unidirectional dependencies, this is straightforward. For example, if src/models/user.py imports
src/models/profile.py, you can define the User and Profile features in separate files without
issues. However, if you have circular dependencies, you may run into problems.

Chalk supports this, but circular imports can arise when features reference each other across files.
To avoid these issues, use the if TYPE_CHECKING block from the typing module and quote your forward references.

Here's an example of how to do this cleanly:

```
# Imports `User` directly, because `src/models/user.py`
# doesn't import `src/models/profile.py`
from chalk.features import features
from src.models.user import User

@features
class Profile:
    id: Primary[User.id]
    username: str
```

```
from chalk.features import features
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Imports `Profile` only when type checking
    # to avoid circular imports
    from src.models.profile import Profile

@features
class User:
    id: str
    # Profile must be quoted because it is imported
    # only when type checking
    profile: "Profile"
```

By quoting imports inside if TYPE_CHECKING,
you avoid circular dependency errors while still
maintaining type safety and feature linkage.

If the relationship to Profile is optional, you can use typing.Optional or the | None syntax,
but the entire annotation should be quoted:

```
from chalk.features import features
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.profile import Profile

@features
class User:
    id: str
    # All of `"Profile | None"` must be quoted, not just the `Profile` part
    profile: "Profile | None"
```

### Querying for Has-One Relationships

You can also query for a feature that is joined through a has-one relationship by
referencing the root namespace. For example, to query for the Profile features
associated with a User continuing from the example above, you can write:

```
from chalk.client import ChalkClient
from src.features import User

client = ChalkClient()
client.query(
    input={User.id: "1"},
    output=[User.profile.id, User.profile.email_age_years]
)
```

# Has Many
source: https://docs.chalk.ai/docs/has-many

## Define one-to-many and many-to-many relationships between feature classes.

Has-many relationships link a feature to many instances of another feature.

### Foreign Keys

The recommended way to specify a join for a has-many relationship is implicitly. In the
example below, a User is linked to potentially multiple Transfers.

```
from chalk.features import features, DataFrame

@features
class Transfer:
    id: str
    # note, the annotation must be a string reference because User is
    # defined after Transfer.
    user_id: "User.id"
    amount: float

@features
class User:
    id: str
    transfers: DataFrame[Transfer]
```

### Explicit Join

The following example, which explicitly sets the join, is equivalent to the above:

```
from chalk.features import has_many, DataFrame

@features
class Transfer:
    id: str
    user_id: str
    amount: float

@features
class User:
    id: str
    transfers: DataFrame[Transfer] = has_many(lambda: Transfer.user_id == User.id)

```

### Composite Join Keys

You can also specify multiple join keys for a has-many relationship. For example, say hospitals wants to
compute aggregations over visit to each of their departments. We could write the following feature classes.

```
from chalk import _
from chalk.features import features, DataFrame, has_many
import chalk.functions as F
from datetime import datetime


@features
class HospitalVisit:
    id: str = _.user_id + _.hospital + _.department + F.cast(_.date, str)
    composite_key: str = _.hospital + "-" + _.department
    department: str
    hospital: str
    user_id: str
    date: datetime

@features
class HospitalDepartment:
    id: int
    name: str
    hospital_name: str
    composite_key_match: str = _.hospital_name + "-" + _.name
    # multi-feature join
    visits: DataFrame[HospitalVisit] = has_many(
      lambda:
       (HospitalDepartment.hospital_name == HospitalVisit.hospital) &
       (HospitalDepartment.name == HospitalVisit.department)
    )
    # composite key join
    visits_with_composite_key: DataFrame[HospitalVisit] = has_many(
      lambda: HospitalDepartment.composite_key_match == HospitalVisit.composite_key
    )
```

You can also join in Has-Many relationships for features that have primary composite keys.

```
from chalk.features import features, DataFrame, has_many

@features
class SoftwareEngineer:
    id: int = _.first_name + " " + _.last_name
    first_name: str
    last_name: str

    manager_id: str

@features
class Manager:
    id: int
    direct_reports: DataFrame[SoftwareEngineer] = has_many(
      lambda: Manager.id == SoftwareEngineer.manager_id
    )
```

### Aggregations on References

Having established a has-many relationship, you can now reference the transfers for
a user through the user namespace. The has_many feature returns a chalk.DataFrame,
which supports many helpful aggregation operations:

```
# Number of transfers made by a user
User.transfers.count()

# Total amount of transfers made by the user
User.transfers[Transfer.amount].sum()

# Total amount of the transfers made by the user that were returned
User.transfers[
    Transfer.status == "returned",
    Transfer.amount
].sum()
```

To compute an aggregation over one or more time windows, see our docs on windowed aggregations.

### Back-references

### One-to-many

In the reverse direction, a one-to-many relation is defined by a has_one
relation (following the above example, a user has many transfers but a transfer has a
single user). However, you don't have to explicitly set the join a second time. Instead,
the join condition is assumed to be symmetric and copied over. To complete the one-to-many
relationship from our example, add a User to the Transfer class:

Here, you need to use quotes around User to use a forward reference.

### Many-to-many

The recommended way to define a many-to-many relationship is through a joining feature class.
For instance, to define a many-many relationship between Actors and Movies, you
could write the following feature classes:

```
from chalk.features import features, DataFrame

@features
class Actor:
    id: int
    appearances: "DataFrame[MovieRole]"
    full_name: str

    # this will be used to demonstrate one of the
    # ways the joining feature can be populated
    movie_ids: list[int]

@features
class Movie:
    id: int
    title: str

@features
class MovieRole:
    id: str
    actor_id: Actor.id
    movie_id: Movie.id
    movie: Movie
```

Here you need to use quotes around DataFrame[MovieRole] to use a forward reference.

This joining feature class can be populated by a SQL file resolver:

```
-- resolves: MovieRole
-- source: PG
SELECT id, actor_id, movie_id FROM movie_roles;
```

Alternatively, by a DataFrame-returning Python resolver (namespaced to one of the joined feature sets):

```
@online
def get_actor_in_movie(
  a_id: Actor.id,
  movie_ids: Actor.movie_ids,
) -> Actor.appearances:
  return DataFrame([
    MovieRole(
      id=f"{a_id}_{m_id}",
      actor_id=a_id,
      movie_id=m_id
    )
    for m_id in movie_ids
  ])
```

The joining feature class lets you:

- query for movie features from the Actor namespace, and
- use movie features in downstream Actor resolvers.

For example, to get the titles for all the movies that an actor has appeared in, you can run the following query:

```
$ chalk query --in actor.id=1 --out actor.appearances.movie.title
Results

 Name                           Hit?  Value
───────────────────────────────────────────────────────────────────────────────
 actor.appearances.movie.title        ["The Bad Sleep Well","High and Low",...]
```

# Chalk DataFrame
source: https://docs.chalk.ai/docs/dataframe

## Describe and fetch rows of features.

A Chalk DataFrame is a 2-dimensional data structure
similar to pandas.DataFrame, but with richer underlying optimizations.
In a Chalk DataFrame, the column headers are instances of chalk.feature.
The Chalk DataFrame can be used to describe rows of data
and as a wrapper for returning that data.

The Chalk DataFrame is parameterized by the feature values it contains.
For example:

```
DataFrame[User.name, User.email]
```

The DataFrame type is commutative on its type parameters.
This property allows you to write the type parameters of
a DataFrame in any order:

```
DataFrame[User.name, User.email] == DataFrame[User.email, User.name]
```

Note: The Chalk DataFrame is used as a feature type for defining has-many relationships
between feature classes, but the functions, filters, and aggregations described in this document are meant
to be used in Python resolvers or notebooks--not in Chalk Expressions. For information about the functions
and aggregations that you can use in Chalk Expressions, see here.

### Constructing a DataFrame

You're likely to use the Chalk DataFrame primarily as a type,
or to handle one as the result of a SQL query.
However, you can also construct a DataFrame directly.

### From a dictionary

Much like a pandas.DataFrame, a chalk.DataFrame can be constructed from a dictionary.
The keys of the dictionary are the headers and the values are the rows under each header.
The keys can be specified as either strings
("taco.price")
or as their Python types
(Taco.price).
You can convert from a feature's Python definition to a string with a cast:
str(Taco.price) == "taco.price".

```
chalk_df = DataFrame(
    {
        Taco.id: ["t_1", "t_2", "t_3"],
        "taco.price": [1, 2, 10],
        str(Taco.contains_meat): [True, True, False],
    }
)
```

In the above example, we use all forms of referencing a feature's name.

### From a list

You can create the same chalk.DataFrame by passing a list of feature classes:

```
chalk_df = DataFrame([
    Taco(id="t_1", price=1, contains_meat=True),
    Taco(id="t_2", price=2, contains_meat=True),
    Taco(id="t_3", price=10, contains_meat=False),
])
```

### From a pandas.DataFrame

You can also convert to and from a pandas.DataFrame.

```
import pandas as pd

DataFrame(
    pd.DataFrame({
        "taco.id": ["t_1", "t_2", "t_3"],  # Taco.id or "taco.id" are accepted
        "taco.price": [1, 2, 10],
    })
)
```

The Chalk DataFrame can be converted to a pandas.DataFrame
via the method .to_pandas():

```
df = DataFrame(...)
df.to_pandas()
```

### From a SQL query

Chalk's SQL integrations output the type DataFrame.
For more information, see the SQL Integration section.

```
pg = PostgreSQLSource()

@offline
def fn() -> DataFrame[Login.ts, Login.user_id, Login.status]:
    return pg.query(
        Login(
            status=LoginHistorySQL.status,
            ts=LoginHistorySQL.created_at,
            user_id=LoginHistorySQL.user_id,
        )
    ).all()
```

### Aggregations

| Method                                                                                                                                     | Description                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| DataFrame.count() | The number of rows in a DataFrame                                     |
| DataFrame.mean()  | The average for each column in the DataFrame†       |
| DataFrame.sum()   | The sum of each column in the DataFrame†            |
| DataFrame.max()   | The maximum value for each column in the DataFrame† |
| DataFrame.min()   | The minimum value for each column in the DataFrame† |

† There will be only one row in the DataFrame after this operation, one for each
value. If the DataFrame contained only a single column to start,
then the value returned is a scalar.

### Projections

You can select columns out of a DataFrame from the set
of columns already present to produce a new DataFrame
scoped down to those columns. For example:

```
df: DataFrame[User.name, User.email, User.age] = ...
projected = df[User.email, User.age]
# type(projected) == DataFrame[User.email, User.age]
```

### Filters

In addition to selecting columns, you can
filter the rows
of a DataFrame.
The example below restricts the rows of a DataFrame to only rows where
the User is over 21 years old:

```
df: DataFrame[User.name, User.email, User.age]
f = df[User.age >= 21]
# type(f) == DataFrame[User.name, User.email, User.age]
```

Filtering a DataFrame keeps all the existing columns,
but drops rows where the predicate is not met.

The Chalk DataFrame supports the standard comparison
functions
(<, <=, >, >=, in, is, is not, ==, and !=)
for features and their matching scalars values.
You can compose these filters with the boolean operations
and, or, and not.

| Operation(s)                                                                                                         | Example                                                                                                                                                         | Comment                   |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| >, <, >=, <= | User.age > 21                                                   |                           |
| ==, !=             | User.age is NoneUser.age is not None                      | AST-only feature.† |
| is, is not         | User.age is NoneUser.age is not None                      | AST-only feature.† |
| in, not in         | User.age in User.age not in [17, 18]              | AST-only feature.† |
| or, and            | (User.state == "AL" and User.age >= 17) or User.age >= 18 | AST-only feature.† |
| not                | not (User.state == "AL" and User.age >= 17)                     | AST-only feature.† |

† The marked operations must be provided as direct arguments.
They cannot first be assigned to a variable, and later provided as an argument.
For example, DataFrame[User.age in {17, 18}] is valid, but
defining x = User.age in {17, 18} and then running DataFrame[x] is not valid.
The reason for this is that Python does not allow overriding these operations.
However, Chalk's aim is to allow developers to inspect and support natural Python syntax.
To that end, Chalk parses the AST to override these operations, with the restriction
that they are provided as arguments directly.

### Composing Filters

To filter on multiple columns, separate your filters by
a comma:

```
df[User.age > 21, User.email == "joe@chalk.ai"]
```

Alternatively, use the and keyword between filters:

```
df[User.age > 21 and User.email == "joe@chalk.ai"]
```

Similarly, you can perform or queries with Python's
or keyword:

```
df[User.age > 21 or User.email == "joe@chalk.ai"]
```

All of these can be composed:

```
df[
  User.age > 21 and (
    User.email == "joe@chalk.ai" or
    User.full_name is None
  )
]
```

### Composing projections and filters

Filtering may be combined with projection.
For example, you can select all the values for User.email
where the user is at least 21 years old as follows:

```
df: DataFrame[User.name, User.email, User.age]
projected = df[User.email, User.age > 21]
# type(projected) == DataFrame[User.email]
```

If you'd like to filter on a value and also return the value,
you need to explicitly select it. You can amend the
above example to include the User.age feature like so:

```
df: DataFrame[User.name, User.email, User.age]
projected = df[User.email, User.age, User.age > 21]
# type(projected) == DataFrame[User.email, User.age]
```

### Performance (Vectorization, Laziness)

Chalk's DataFrame is designed to support efficient operations
across a variety of underlying data sources. DataFrame
vectorizes scalar operations on data that is kept resident in memory. Chalk
calls operations on data that is loaded into memory "strict execution".

In coordination with Chalk's Execution Engine, DataFrame is capable of
pushing down filtering, projection, and aggregation operations to
underlying data sources. Chalk calls this style of execution "lazy execution".

Suppose that we use a DataFrame to query a SQL source:

```
@online
def get_return_count(
    transfers: User.transfers[Transfer.status == "returned", after(days_ago=60)]
) -> User.returned_transactions_last_60:
    return transfers.count()
```

This ultimately results in (approximately) the following SQL query being executed:

```
SELECT COUNT(*) from transfers
WHERE status = 'returned' and
transfers.ts > current_date - interval '60' day;
```

This "push down" mechanism in lazy computation helps make
computationally expensive operations execute quickly, since Chalk only needs to load
a single integer from the underlying data source, instead of potentially all Transfer rows.

# Validation
source: https://docs.chalk.ai/docs/validation

## Validate features and resolvers

### Feature Values

Chalk can enforce requirements on your feature values.
You can validate the values and length of many primitive types
through the keyword arguments min, max, min_length, and max_length.

To prevent 'invalid' features from being written
to the offline or online store, set strict=True.
In this case an error will be thrown when an invalid
feature is observed.
The validations keyword argument can be used when there are
multiple validations, only some of which are strict.

```
from chalk import Validation
from chalk.features import feature, features

@features
class Office:
    size_sqft: int = feature(min=0, max=100_000_000)
    street: str = feature(validations=[
        Validation(min_length=1, max_length=256, strict=True),
        Validation(min_length=20, max_length=100)
    ])
```

### Feature validation requirements

For some features, it is important to specify metadata
such as owner and description.
Chalk allows you to enforce metadata requirement easily.
In addition, you can specify for each feature the severity
at which to raise a missing metadata issue.

In chalk.yml, the validation > feature > metadata
section specifies settings for metadata validation.
In the following example, users will be blocked from
deploying features (chalk apply) with
an unspecified owner. They are allowed to deploy
features with missing description and tags.

```
project: Predict Q2 Spending

validation:
  feature:
    metadata:
      - name: owner
        missing: error
      - name: description
        missing: warning
      - name: tags
        missing: info

environments:
  default:
    runtimes: 'python310'
    requirements: requirements.txt
```

# Versioning
source: https://docs.chalk.ai/docs/feature-versions

## Rigorously update your features as their meaning changes.

### What are feature versions

Feature versions allow you to manage a feature as its
definition changes over time. You can reference versions
of a feature when querying, in resolvers, in migrations,
and anywhere you use features!

The ability to maintain multiple versions of a feature is
especially useful as your use cases evolve and the definition
of a feature changes. This might be because your old feature
had a bug, or maybe you want to improve the feature to be
even more useful.

Changing the definition of a feature can have unexpected
side effects, especially when there might be many consumers
of a feature, some of which you may be unaware of.
Feature versions allow you to update the feature definition
without worrying that you might affect these consumers
unknowingly.

Try it out yourself with this tutorial.

### Definition

To define a versioned feature, supply the version keyword
argument to the feature function. This allows you to
continue adding versions without affecting past versions.

```
from chalk.features import features, feature

@features
class Trial:
    id: int
    code: str = feature(version=2)
```

### Querying

You can refer to a specific version of a feature using the
@ operator. You can query versioned features from any client,
including the CLI, Python, etc.

```
$ chalk query --in trial.id=1 --out trial.code@2
```

```
from chalk.client import ChalkClient
from src.models import Trial

client = ChalkClient()
result = client.query(
    input={Trial.id: 1},
    output=[Trial.code@2]
)
```

### Default versions

When you define a versioned feature, that feature always
has a default version. When you reference a versioned feature
without the @ operator, you reference the default version.
The default version can be controlled by adding the
default_version keyword argument to the feature function.
If no default_version is provided, the default version is 1.
It is best practice to leave the default as 1 until all
consumers have been updated to use a newer version.

```
from chalk.features import features, feature

@features
class Trial:
    id: int
    code: str = feature(version=2, default_version=2)
```

### Deprecating features

As you migrate to newer feature versions or phase out old features,
you can mark them as deprecated to signal that they should no longer be used.
This helps teams understand which features to avoid and provides a clear migration path.

You can deprecate features that aren't versioned to indicate they should be phased out:

```
from chalk.features import features, feature

@features
class User:
    id: str
    # Mark the old feature as deprecated
    legacy_risk_score: float = feature(
        deprecated=True,
        description="Use risk_score_v2 instead"
    )

    # The new feature that should be used instead
    risk_score_v2: float
```

### Deprecating specific versions

When using multiple versions of a feature, you can mark specific versions as deprecated:

```
from chalk.features import features, feature
from chalk import _

@features
class User:
    id: str
    score: int
    banned: bool = feature(versions={
        1: feature(
            deprecated=True,
            description="Prior thresholds we used",
            expression=_.score > 900,
        ),
        2: feature(
            description="New cutoff released by Monica's team",
            expression=_.score > 300 | (_.score < 100 & _.id == "admin"),
        ),
    })
```

When a deprecated feature is used in queries or resolvers, Chalk will log warnings to help you track and eliminate usage of deprecated features across your codebase. This is particularly useful during gradual migrations when you need to maintain backward compatibility while encouraging adoption of new features.

To monitor the migration progress and identify which deprecated features can be safely removed, you can use the Chalk web interface to sort features by usage and see when each feature was last queried. This helps you make data-driven decisions about when it's safe to fully retire deprecated features.

### Resolvers

Resolvers also reference versioned features with @.
Resolvers can take versions of a feature as input, return
them as output, or both. Chalk will always generate the
right version of a feature when chaining resolvers that
require versioned features.

### Requesting versioned features

```
from chalk.features import online

@online
def detect_trial_failure(code: Trial.code) -> Trial.failed:
    # Default version is 1.
    return code in {'failed', 'err'}

@online
def detect_trial_failure_v2(code: Trial.code@2) -> Trial.failed:
    # Version 2 is specifically requested.
    return code in {'FAILED', 'ERR'}
```

### Producing versioned features

```
@online
def extract_trial_code_v1(d: Trial.raw_data) -> Trial.code @ 1:
    return d['code']

@online
def extract_trial_code_v2(d: Trial.raw_data) -> Trial.code @ 2:
    return d['data']['code']
```

```
-- resolves: Trial@2
-- source: pg_trial

select id, code from trial_table;
```

### Limitations

Only scalar features can be versioned. Other kinds of
features cannot be versioned. These include:

- has_one and has_many
- FeatureTime
- Windowed
- Primary
# Embeddings
source: https://docs.chalk.ai/docs/embeddings

## Automatically calculate embeddings from existing features

Embedding models are generally used to calculate a vector feature. Chalk includes
built-in support for common embedding models, or can define your own embedding model through a resolver.

### Built-In Embedding Functions

Chalk includes built-in support for both open-source and hosted embedding models via the embedding function.
We recommend using this function when possible, as Chalk will automatically handle batching and retries,
and you don't need to specify the vector size. The main arguments for this function are:

- input (required): A lambda that returns the feature that will be embedded. If the embedding model takes multiple
inputs (such as with INSTRUCTOR, which requires the instruction along with the content), then this lambda should
return a tuple of the feature references (or a string and a feature reference, if the instruction is constant).
See the INSTRUCTOR example below.If you would like to use multiple features as input, you can define a resolver to combine
these features into one. Then, reference this combined feature as input.
- provider (required): The embedding model provider. The currently supported providers are sentence-transformers,
instructor, openai, or cohere. Chalk may add more providers in the future.
- model (required): The name of the model to use. Each provider has a different set of models that are supported.
- max_staleness (optional): The duration for which the embedding will be cached. By default, the embedding vector
will be cached for the same duration as the feature. If you would like different behavior, you can specify this
argument explicitly.

For the complete signature, please see the api docs.

### Sentence Transformers

Chalk supports all models that are part of the sentence-transformers framework.
It is recommended to use the all-MiniLM-L6-v model, though all
pre-trained models are supported.

```
from chalk.features import embed, features, Vector

@features
class Document:
    content: str
    embedding: Vector = embed(
        input=lambda: Document.content,
        provider="sentence-transformers",
        model="all-MiniLM-L6-v",
    )
```

### Instructor

Chalk supports INSTRUCTOR embedding models. When using this
provider, the input lambda should return a tuple of the instruction and feature to encode.
See the available models here.

If the instruction is the same for every row, you can use a literal (constant) string.

```
from chalk.features import embed, features, Vector

@features
class Document:
    content: str
    embedding: Vector = embed(
        input=lambda: ("Represent the Legal document: ", Document.content),
        provider="instructor",
        model="hkunlp/instructor-base",
    )
```

However, if we have multiple types of documents, then you can use another feature to represent the instruction
and define a resolver to compute the instruction.

```
from chalk.features import embed, features, online, Vector

@features
class Document:
    content: str
    document_type: str
    instruction: str
    embedding: Vector = embed(
        input=lambda: (Document.instruction, Document.content),
        provider="instructor",
        model="hkunlp/instructor-base",
    )

@online
def generate_instruction(document_type: Document.document_type) -> Document.instruction:
    return f"Represent the {document_type} document: "
```

### OpenAI

Chalk can proxy calls to the OpenAI Embeddings API.
It is recommended to use the text-embedding-ada-002 model, though all OpenAI models are supported.
If you don't already have an OpenAI account, sign up here, and then create an
OpenAI Integration in Chalk. All OpenAI requests will be attributed to your API key.
To minimize usage, we highly recommend specifying an appropriate max staleness in Chalk, which will ensure that
embeddings are cached.

```
from chalk.features import embed, features, Vector

@features
class Document:
    content: str
    embedding: Vector = embed(
        input=lambda: Document.content,
        provider="openai",
        model="text-embedding-ada-002",
        max_staleness="infinity",
    )
```

### Cohere

Chalk can proxy calls to Cohere Embed. To use this integration, first sign up for an
Cohere Account, and then create an Cohere Integration
in Chalk. All Cohere requests will be attributed to your API key. To minimize usage, we highly recommend specifying an
appropriate max staleness in Chalk, which will ensure that embeddings are cached.

```
from chalk.features import embed, features, Vector

@features
class Document:
    content: str
    embedding: Vector = embed(
        input=lambda: Document.content,
        provider="cohere",
        model="embed-english-v2.0",
        max_staleness="infinity",
    )
```

### Custom embedding functions

If you would like to run your own embedding model, you can define a custom resolver to compute the embedding
from existing features in the feature class. For performance, we recommend to store the model weights in an
object store (such as AWS S3 or GCS) rather than including them your source code and to load the model
using a boot hook.

```
from chalk.features import before_all, DataFrame, embed, features, online, Vector

my_model = MyModel()

@before_all
def load_my_model():
    my_model.initialize("s3://my-bucket/my-checkpoint.pt")


@features
class Document:
    content: str
    # When using a custom embedding function, the size of the vector must be specified.
    embedding: Vector[1536]

@online
def my_embedding_function(content: DataFrame[Document.content]) -> DataFrame[Document.embedding]:
    return my_model.embed(content.to_arrow()['document.content'])
```

Chalk will then call my_embedding_function whenever an embedding is needed.

# Nearest Neighbors (Vector Search)
source: https://docs.chalk.ai/docs/vector-search

## Find the nearest neighbors across a vector relationship

A feature class can be linked to the closest examples of another feature class. This functionality can be useful for search
and retrieval applications.

Nearest neighbor relationships are only supported for vector features.

We recommend to first take a look through Chalk's support for vector
features and embedding functions.

To illustrate how to use nearest neighbor relationships, we'll walk through an example for Chalk can power FAQ search.
In this example, the SearchQuery feature class represents an incoming request, and the FAQDocument
feature class represents our collection of frequently asked questions and answers. Our goal is to return the five most
relevant FAQ entries for the given search query.

### Defining nearest neighbor relationships

Using the has_many function and the is_near method, we can express a relationship where we want the nearest
documents for each query.

```
from chalk.features import DataFrame, embed, features, has_many, Vector

@features
class SearchQuery:
  query: str
  product_version: int
  embedding: Vector = embed(...)
  nearest_documents: DataFrame[FAQDocument] = has_many(
      lambda: SearchQuery.embedding.is_near(
          FAQDocument.embedding
      )
  )
  response: str

@features
class FAQDocument:
  question: str
  product_version: int
  question_embedding: Vector = embed(...)
  link: str
```

The lambda solves forward references, letting you reference SearchQuery and
FAQDocument before they are defined.

### Distance Measure

Nearest neighbor relationships use a distance function to measure closeness. By default, Chalk uses L2 distance, though
inner product and cosine similarity are also supported. To change the distance function, use the metric argument:

```
from chalk.features import DataFrame, features, has_many

@features
class SearchQuery:
  nearest_documents: DataFrame[Document] = has_many(
    lambda: SearchQuery.embedding.is_near(
      FAQDocument.embedding,
      metric="cos",  # or "l2", "ip"
    )
  )
```

### Nearest neighbors as resolver inputs

It's possible to use this relationship as a has-many resolver input. The resulting
documents will be returned as a Chalk DataFrame. Because the search is approximate, the number of
documents to return must be specified via a slice expression.

```
from chalk import online

@online
def generate_response(
  # Query for the five most relevant documents, and select their links
  nearest_documents: SearchQuery.nearest_documents[FAQDocument.link, :5],
) -> SearchQuery.response:
  return "\n".join(nearest_documents[FAQDocument.link])
```

### Filtering

Inside the input argument signature, we can include filters for more accurate results. The filters will be applied
before the limit is applied.

When using a nearest neighbor relationship, do not filter within the resolver.

Filtering inside the resolver will be performed after the limit is applied, which may filter out all returned neighbors
if none of them match the filter expression.

Don't filter like this

```
from chalk import online

@online
def generate_response(
  version: SearchQuery.product_version,
  nearest_documents: SearchQuery.nearest_documents[
    FAQDocument.link,
    FAQDocument.product_version,
    :5,
  ],
) -> SearchQuery.response:
  # Don't do this! If the nearest five documents are all for a different product version,
  # then filtered_nearest_documents will be empty
  filtered_nearest_documents = nearest_documents[FAQDocument.product_version == version]
  return "\n".join(filtered_nearest_documents[FAQDocument.link])
```

Instead, specify the filter conditions in the resolver signature. This will ensure that the filter is applied before
the limit, meaning that the nearest five documents that match all of the filters will be returned.

Filter like this

```
from chalk import online

@online
def generate_response(
  filtered_nearest_documents: SearchQuery.nearest_documents[
    FAQDocument.link,
    FAQDocument.product_version == SearchQuery.product_version,
    :5,
  ],
) -> SearchQuery.response:
  return "\n".join(filtered_nearest_documents[FAQDocument.link])
```

# Named Prompts
source: https://docs.chalk.ai/docs/prompts

## Define templated LLM interactions as microservices

You can define named prompts in Chalk to help maintain consistency in your LLM workflows by making prompts more
maintainable and reusable across your application. You can parameterize prompts using Jinja templating to inject
feature values.

### Prompt Definition Approaches

Chalk supports two primary methods for defining and managing prompts: direct prompt definitions and named prompts.
Each approach offers different benefits depending on your use case and deployment requirements.

### Direct Prompts

Direct prompt definitions provide immediate, inline configuration of LLM completions.
This approach is useful for rapid prototyping, one-off implementations, or when prompt logic is tightly coupled to specific features.
To define a direct prompt to perform sentiment analysis on a comment, you could define the following Chalk features utilizing the chalk.prompts library.

```
import chalk.functions as F
import chalk.prompts as P
from chalk.features import features
from pydantic import BaseModel

system_message = """You are a sentiment analysis expert. Analyze the user's comment and determine if it's positive, negative, or neutral.
Rules:
- Be objective and focus on the text's emotional tone
- Consider context and nuance
- Provide a confidence score based on clarity of sentiment"""

user_message = "Analyze this comment: {{User.comment}}"

class UserSentiment(BaseModel):
    sentiment: str = Field(description="positive, negative, or neutral")
    confidence: float = Field(description="on a 1-100 scale")

@features
class User:
    id: str
    comment: str
    actual_sentiment: str
    response: P.PromptResponse = P.completion(
        model="gpt-5.1",
        messages=[
            P.message(role="system", content=system_message),
            P.message(role="user", content=F.jinja(user_message)),
        ],
        output_structure=UserSentiment,
    )
    predicted_sentiment: str = F.json_value(_.response.response, "sentiment")
```

In the example above, we see how direct prompts integrate with Chalk's feature system.
The prompt uses Jinja templating
to dynamically inject the user's comment into the prompt through {{User.comment}}, allowing the LLM to analyze the
specific content at runtime.
The UserSentiment Pydantic model defines a structured output format, ensuring consistent response parsing across all completions.
While this approach provides fine-grained control over the prompt configuration, it tightly couples the prompt template, model settings, and output structure to your deployment code.  Any changes to the prompt template or model parameters require a new deployment.

### Multimodal Prompts

Chalk's chat completion API extends beyond text-only interactions by supporting multimodal inputs, enabling you to process images alongside text in your LLM workflows.
This capability opens up new possibilities for visual content analysis, allowing you to pass images directly to vision-capable models like GPT-5.1, combine text and image inputs in a single prompt, and extract structured information from visual content. Here's how you can process a receipt image to extract structured data:

```
@features
class Receipt:
    image_url: str
    image_response: P.MultimodalPromptResponse = P.completion(
        model="gpt-5.1",
        messages=[
            P.message(
                "user",
                [
                    {"type": "input_text", "text": "Extract all items, prices, and total from this receipt"},
                    {"type": "input_image", "image_url": _.image_url},
                ],
            ),
        ],
    )
```

This multimodal approach seamlessly integrates with Chalk's feature system, treating visual inputs as first-class citizens alongside text.
The same structured output capabilities available for text-only prompts apply here, allowing you to define Pydantic models for consistent parsing of visual information extraction tasks.

### Named Prompts

Named prompts abstract prompt definitions into standalone, reusable components that can be managed independently of
your feature code. This separation of concerns enables centralized prompt management across your application and
provides robust version control of your prompt templates. Named prompts allow you to conduct A/B testing between
different prompt variants and make runtime modifications through the web interface without code changes. You can define
a named prompt in the Web UI and implement the same Chalk feature with more concise code.

```
import chalk.functions as F
import chalk.prompts as P
from chalk.features import features

@features
class User:
    id: str
    comment: str
    actual_sentiment: str
    response: P.PromptResponse = P.run_prompt("analyze_sentiment")
    predicted_sentiment: str = F.json_value(_.response.response, "sentiment")
```

Named prompts function as microservices within your ML pipeline, allowing you to modify prompt behavior without
requiring code deployments. This architecture is particularly valuable for teams that need to iterate rapidly on prompt
engineering or maintain multiple prompt variants.

### Prompt Evaluation

The Chalk evaluation platform provides comprehensive tooling for testing and comparing prompt performance. This
framework enables data-driven prompt engineering through systematic testing of prompt variants.

### Dataset Preparation

Evaluation begins with creating a labeled dataset that serves as your ground truth. This dataset should contain input
examples and their expected outputs, enabling automated assessment of prompt performance:

```
import pandas as pd

sentiment_df = pd.read_csv("sentiment.csv")
sentiment_ds = chalk_client.create_dataset(
    input=sentiment_df,
    dataset_name="sentiment_gt",
)
sentiment_ds.to_pandas()
```

### Evaluation Execution

The evaluation framework allows you to test variations in prompt templates, assess the impact of different models and
parameters, and validate changes to output structures. Built-in evaluators like "exact_match" offer immediate insights
into prompt performance, while custom evaluation expressions enable more nuanced analysis specific to your use case.

```
eval_run = chalk_client.prompt_evaluation(
    dataset_name="sentiment_gt",
    evaluators=["exact_match"],
    reference_output="user.actual_sentiment",
    prompts=[
        "analyze_sentiment-v1",
        "analyze_sentiment-v2",
        P.completion(
            model="gpt-5.1",
            messages=[
                P.message(role="system", content=system_message),
                P.message(role="user", content=user_message),
            ],
        ),
    ]
)
eval_run.to_pandas()
```

The results of every evaluation are stored and available for viewing in the Web UI.

# Windowed Aggregations
source: https://docs.chalk.ai/docs/aggregations

## Define features as aggregations of data over sliding time ranges.

Given a has-many relationship between two feature classes, Chalk can compute aggregations over the joined data either
for all possible values or filtered by specific windows of time. Create an Aggregation Feature using a
Chalk Expression or a Windowed Aggregation Feature using the windowed function.
For example, use windowed features to count the number of login attempts made by a user over the past 10 minutes, or
to track the largest purchase amount a cardholder has made in the past 30 days.

### Define an Aggregation

Chalk supports a number of aggregations out of box. Chalk builtins are very performant as they're optimized and also
run natively in C++ and Rust.
Aggregations automatically skip null or None values.
The following table lists the supported aggregations along with some notes.

| Function | Notes |
| ---  | --- |
| sum | Support for vector and scalar feature aggregations. |
| min | |
| max | |
| min_by_n | Returns a list of the n values for the minimum by values. |
| max_by_n | Returns a list of the n values for the maximum by values. |
| mean | Feature type must be Vector, float or float | None. None values are skipped, meaning they are not included in the mean calculation.  |
|count | |
|std | Standard deviation. Requires at least 2 values. |
|var | Variance. Same requirements as std. |
|approx_count_distinct | An approximation of the cardinality of non-null data. |
|approx_top_k | An approximation of the most common values in a field. Takes in a required k parameter, such as approx_top_k(k=5) for the five approximately-most common values. Up to k values will be returned, sometimes fewer. |
|approx_percentile | An approximation of the value a given percentage of your data falls below. Accepts quantile parameter, between 0 and 1, such as approx_percentile(quantile=.5). |

For example, say you want to compute some aggregations over a document's revisions. You could define the features
and aggregations below.

```
from chalk.features import features, DataFrame, _
from datetime import datetime

@features
class Document:
    id: int
    revisions: DataFrame[Revision]

    # these are aggregations over the revisions DataFrame
    num_revisions: int = _.revisions[_.id].count()
    max_revision_size: float = _.revisions[_.size_bytes].max()

    # you can also filter the rows being aggregated
    earliest_large_revision_ts: datetime = _.revisions[_.size_bytes > 100,000,000, _.timestamp].min()

    # some aggregations return a list
    most_common_sizes: list[float] = _.revisions[_.size_bytes].approx_top_k(k=5)


@features
class Revision:
    id: int
    # this is a foreign key join between Document and Revision
    document_id: Document.id
    size_bytes: float
    timestamp: datetime

```

### Define a Windowed Aggregation

In an aggregation, you can filter and sort by datetime features. Chalk enables you to define Windowed Aggregations,
such that you can compute the same aggregation over multiple time windows in a single feature definition.
Windowed features are typically computed using either raw data or pre-aggregated data. For larger datasets, some systems
may pre-aggregate batch data to optimize performance at the cost of real-time accuracy. Chalk supports both modes of
operation to achieve low latency and accuracy for real time aggregations over large datasets through
materialized windowed aggregations.

Otherwise, for smaller datasets or lower throughput use cases, Chalk can compute windowed aggregations directly
on the raw data.

### Set up a data aggregation using windowed features

A windowed feature takes in a series of window durations, and an aggregation expression
for how to compute the feature outputs. Within the expression, you can reference the timestamp feature on the
feature class over which you are aggregating and compare to _.chalk_window and _.chalk_now to filter against
the current window's time range. The _.chalk_now keyword references the query time which
will default to timestamp.now() but can be overridden when a different input time is specified at query time. This
allows you to query for an aggregation for any window duration at any point in time.

Here is an example of a windowed feature representing the number of
failed logins in the last 10 minutes, 30 minutes, and 1 day:

```
from chalk import Windowed, windowed
from chalk.features import DataFrame, _
from datetime import datetime

@features
class LoginAttempt:
    id: int
    user: "User.id"
    status: str
    at: datetime

@features
class User:
    id: int
    login_attempts: DataFrame[LoginAttempt]
    num_failed_logins: Windowed[int] = windowed(
        "10m", "30m", "1d",
        max_staleness="10m",
        expression=_.login_attempts[
            _.status=="failed",
            _.at > _.chalk_window,
            _.at < _.chalk_now,
        ].count(),
        default=0,
    )
    most_common_statuses: Windowed[list[str]] = windowed(
        "1h",
        max_staleness="15m",
        expression=_.login_attempts[
            _.status,
            _.at > _.chalk_window,
            _.at < _.chalk_now,
        ].approx_top_k(k=5)
    )
```

Windowed features support much of the same functionality as normal features. They are most often used alongside
max_staleness and
etl_offline_to_online.

Windowed features are typically resolved, either:

- inline by expressions,
- by stream resolvers, or
- by materialized aggregates.

### Querying by windowed time range

Windowed features resolved via expressions can reference the current windowed time range
using the _.chalk_window operator:

```
from chalk import Windowed, windowed
from chalk.features import DataFrame, _
from datetime import datetime

@features
class Transaction:
    id: int
    user_id: "User.id"
    amount: float
    at: datetime

@features
class User:
    id: int
    transactions: DataFrame[Transaction]
    total_spend: Windowed[float] = windowed(
        "30d", "60d", "90d",
        default=0,
        expression=_.transactions[
            _.amount,
            _.at > _.chalk_window,
            _.at < _.chalk_now,
        ].sum(),
        materialization={"bucket_duration": "1d"},
    )
```

In this code, the windowed feature will return the sum of transaction amounts for the given user over the last 30, 60,
and 90 days. _.at > _.chalk_window is a boolean condition checking that the current transaction's timestamp is greater
than the start of the current window duration.

For aggregating across all features for all time, Chalk offers "all" and "infinity" as keywords for
window durations. As a default, Chalk will look back 100 years for the "all" window. If your team requires
a larger window duration, please reach out to the Chalk team.

```
from chalk.features import features, DataFrame, _
from chalk.streams import windowed, Windowed

@features
class TennisPlayer:
    id: int

    games: DataFrame[Game]
    lifetime_wins: Windowed[int] = windowed(
        "all",
        expression=_.games[_.winner_id == _.id].count(),
        default=0,
    )
```

### Nested windowed feature references

Windowed features can also be referenced by other windowed features in the same feature class using
expressions and the _.chalk_window operator. For example, we can compute the average
transaction amount over different time windows:

```
@features
class Transaction:
    id: int
    user_id: "User.id"
    amount: float
    at: datetime

@features
class User:
    id: int
    transactions: DataFrame[Transaction]
    sum_transactions: Windowed[float] = windowed(
        "30d", "60d", "90d",
        expression=_.transactions[
            _.amount,
            _.at > _.chalk_window,
            _.at < _.chalk_now,
        ].sum(),
    )
    count_transactions: Windowed[float] = windowed(
        "30d", "60d", "90d",
        expression=_.transactions[
            _.at > _.chalk_window,
            _.at < _.chalk_now,
        ].count(),
    )
    avg_transaction_amount: Windowed[float] = windowed(
        "30d", "60d", "90d",
        expression=(
            _.sum_transactions[_.chalk_window] /
            _.count_transactions[_.chalk_window]
        )
    )
```

### Referencing windowed features

A windowed feature can be referenced in a query or a resolver in Python using the window as defined in the feature
definition, but Chalk will convert every windowed feature to a FQN (fully qualified name) that defines the window
duration in seconds. So, when referencing the feature for a resolver, you can use the Python syntax. However, when
referencing a feature in a query, you can use the Python syntax when querying with the Chalk Python SDK, otherwise
the CLI will require the FQN syntax. If you do not specify a window when referencing a windowed feature, Chalk will
return all windows.

Given the feature definition below, the following showcase the ways to reference the respective windows in either
Python syntax or using the FQN.

```
from chalk.features import features
from chalk.streams import windowed, Windowed

@features
class User:
    id: int
    ...
    num_failed_logins: Windowed[int] = windowed(
        "10m",
        "1h30m",
        "1d",
        expression=...,
    )
```

|  Feature Definition Window | Python Syntax                   | Fully Qualified Name            |
| ---------------------------|---------------------------------|---------------------------------|
| "10m"                      | User.num_failed_logins["10m"]   | User.num_failed_logins__600__   |
| "1h30m"                    | User.num_failed_logins["1h30m"] | User.num_failed_logins__5400__  |
| "1d"                       | User.num_failed_logins["1d"]    | User.num_failed_logins__86400__ |

Windowed features can be inputs to resolvers:

```
@online
def account_under_attack(
    failed_logins_30m: User.num_failed_logins["30m"],
    failed_logins_1d: User.num_failed_logins["1d"]
) -> ...:
    return failed_logins_30m > 10 or failed_logins_1d > 100
```

# Materialized Windowed Aggregations
source: https://docs.chalk.ai/docs/materialized_aggregations

## Cache and materialize feature aggregations

Machine learning teams often build and maintain separate pre-aggregation pipelines that relay data--as standalone
features--into a feature store to reduce the latency of computing expensive features.

With Chalk, teams don’t need to spin up separate pipelines. Developers can materialize aggregations to improve
performance, without compromising on flexibility, with just a single line of code:

```
from chalk.features import features, Vector, _
from chalk import DataFrame, Windowed, windowed
from datetime import datetime

@features
class Transaction:
    id: int
    amount: float
    category: int
    user_id: "User.id"
    timestamp: datetime
    embedding: Vector[384]

@features
class User:
    id: int
    transactions: DataFrame[Transaction]
    total_transaction_amount: Windowed[float] = windowed(
        "1d", "7d", "30d",
        materialization={"bucket_duration": "1d"},
        expression=_.transactions[
            _.amount,
            _.timestamp <= _.chalk_now,
            _.timestamp > _.chalk_window
        ].sum(),
    )
    most_active_categories: Windowed[list[int]] = windowed(
        "30d", "60d", "all",
        materialization={"bucket_duration": "1h"},
        # The approximate top 10 categories that the user has
        # spent at in each of the windowed buckets.
        expression=_.transactions[
            _.category,
            _.timestamp <= _.chalk_now,
            _.timestamp > _.chalk_window
        ].approx_top_k(k=10)
    )
    avg_embedding: Windowed[Vector[384]] = windowed(
        "30d", "60d", "all",
        materialization={"bucket_duration": "1h"},
        # Vector mean will be computed as the element-wise
        # mean for each component of the vector
        expression=_.transactions[
            _.embedding,
            _.timestamp <= _.chalk_now,
            _.timestamp > _.chalk_window
        ].mean(),
        default=[0.0] * 384
    )
```

### Why are materialized aggregations useful?

Windowed features are typically computed using either raw data or pre-aggregated data.
Raw data is the ground truth, but aggregating it can be slow if you request long time windows or large volumes of data.
Some systems improve performance by serving features from pre-aggregated batch data.
Pre-aggregated data mitigates high latency with the trade-off of not having access to the freshest data.

Chalk balances accuracy and performance by combining both approaches.
Chalk aggregates historical data while continuously updating your features as new data arrives.
Chalk automatically rolls new data into the appropriate buckets and reconstructs the aggregations.
Buckets that become stale i.e. no longer relevant to any of your active time windows, are automatically cleaned up.
For each bucket, Chalk stores the minimal required data to compute the aggregation, and at query time, the aggregation
is computed by merging the partial aggregate states for all buckets within the requested time window.

Chalk aligns buckets on Unix epoch (ignoring leap seconds) by default. However, if you would like to customize
the bucket starts, you can use the bucket_start field on the MaterializationWindowConfig in your definition.
When serving windowed queries, Chalk uses all buckets containing any overlap with the requested time window.

Materialized Windowed Aggregations

### What types of aggregations does Chalk support?

Chalk supports a number of aggregations out of box. Chalk builtins are very performant as they're optimized and also run natively in C++ and Rust.
Aggregations automatically skip null or None values.
The following table lists the supported aggregations along with some notes.

| Function | Notes |
| ---  | --- |
| sum | Support for vector and scalar feature aggregations. |
| min | |
| max | |
| min_by_n | Returns a list of the n values for the minimum by values. |
| max_by_n | Returns a list of the n values for the maximum by values. |
| mean | Feature type must be Vector, float or float | None. None values are skipped, meaning they are not included in the mean calculation.  |
|count | |
|std | Standard deviation. Requires at least 2 values. |
|var | Variance. Same requirements as std. |
|approx_count_distinct | An approximation of the cardinality of non-null data. Uses Apache DataSketches CPC. |
|approx_top_k | An approximation of the most common values in a field. Takes in a required k parameter, such as approx_top_k(k=5) for the five approximately-most common values. Up to k values will be returned, sometimes fewer. For a weighted count of the most common values, you can use the parameter by, and set return_total_weight to True or False, which will return the top k values based on the by parameter, optionally with the total weight as well. |
|approx_percentile | An approximation of the value a given percentage of your data falls below. Accepts quantile parameter, between 0 and 1, such as approx_percentile(quantile=.5). |

These aggregations can be applied to DataFrame features that represent a has-many join relationship
between two feature classes. Typically, these joins can be defined using a join key, like in our previous example:

```
from chalk.features import features, _
from chalk import DataFrame, Windowed, windowed
from datetime import datetime

@features
class Transaction:
    id: int
    amount: float
    timestamp: datetime
    user_id: "User.id"

@features
class User:
    id: int
    transactions: DataFrame[Transaction]
    total_transaction_amount: Windowed[float] = windowed(
        "1d", "7d", "30d",
        # materialize your features in a single line
        materialization={"bucket_duration": "1d"},
        expression=_.transactions[
            _.amount,
            _.timestamp <= _.chalk_now,
            _.timestamp > _.chalk_window
        ].sum(),
    )

```

Materialized aggregations can also be applied to DataFrame features that are defined using a composite join key.

```
from chalk.features import features, has_many, _
from chalk import DataFrame, Windowed, windowed
from datetime import datetime

@features
class Transaction:
    id: int
    bank: str
    user_id: str
    timestamp: datetime

    amount: float

@features
class User:
    id: int
    bank: str
    transactions: DataFrame[Transaction] = has_many(lambda: (Transaction.user_id == User.id) & (Transaction.bank == User.bank))
    total_transaction_amount: Windowed[float] = windowed(
        "1d", "7d", "30d",
        # materialize your features in a single line
        materialization={"bucket_duration": "1d"},
        expression=_.transactions[
            _.amount,
            _.timestamp <= _.chalk_now,
            _.timestamp > _.chalk_window
        ].sum(),
    )

    top_5_bank_amounts: Windowed[list[str]] = windowed(
        "7d", "14d",
        materialization={"bucket_duration": "1d"},
        expression=_.transactions[
            _.bank,
            _.timestamp <= _.chalk_now,
            _.timestamp > _.chalk_window
        ].max_by_n(_.amount, 5),
    )

    lowest_5_bank_amounts: Windowed[list[str]] = windowed(
        "7d", "14d",
        materialization={"bucket_duration": "1d"},
        expression=_.transactions[
            _.bank,
            _.timestamp <= _.chalk_now,
            _.timestamp > _.chalk_window
        ].min_by_n(_.amount, 5),
    )


```

### Approximate Count Distinct

The approx_count_distinct aggregation provides an efficient way to estimate the number of unique values in your data
using the Compressed Probability Counting (CPC) sketch
algorithm from Apache DataSketches.

### Why use approximate count distinct?

Computing exact distinct counts for large datasets can be memory-intensive and slow, especially for materialized
aggregations where you need to track uniqueness across many time buckets. The CPC sketch algorithm provides:

- Memory efficiency: Uses significantly less memory than storing all unique values
- Mergeable sketches: Partial aggregates from different buckets can be efficiently combined
- High accuracy: Provides estimates with low relative error (typically < 2% for reasonable sketch sizes)

### How do I use materialized aggregations with Chalk?

Users can materialize a feature aggregation in Chalk by supplying the materialization
parameter of the windowed function on the feature you want to aggregate.
In the example above, we specify a bucket_duration of "1d".

The materialization parameter takes in a dictionary that adheres to the schema outlined by MaterializationWindowConfig:

The Duration of each bucket in the window e.g. "1h"

A dictionary that specifically maps bucket durations to your window intervals e.g.
if you wanted to use "10m" bucket durations for your
"1d" window interval and
"3d" bucket durations for your "30d" window interval.
We recommend explicitly mapping bucket durations to each window if your window intervals have a wide discrepancy e.g.
ten minute bucket duration with a one year window interval.
Any window intervals not explicitly included in the "bucket_durations"
dictionary will use your supplied "bucket_duration" by default.

The schedule on which to automatically backfill the aggregation.
For example, "* * * * *"
or "1h".
See CronTab for more details.

The minimum period of time for which to sample data directly via online query, rather than from the backfilled aggregations.

If you want to use one bucket size for all of your window intervals, you can just use the bucket_duration parameter.
If your window intervals have a wide discrepancy (say, 1d and 365d), you can use the bucket_durations parameter to
explicitly map bucket durations to each window interval. Selecting the right bucket duration is a tradeoff between
accuracy and storage. Shorter bucket durations will yield more accurate results, but will also require more storage.
To optimize for accuracy given a storage constraint, you can compute the approximate storage costs by computing the
number of buckets needed for your materialized aggregation (for a materialized aggregation, buckets of the same size
will be reused across all relevant window interval calculations, but each distinct bucket duration requires a distinct
set of buckets), and then computing the storage per bucket. The storage used per bucket is the sum of the size of the online
storage key representation for the primary key, as well as the size of the bucket state (which ranges from approximately
9 bytes for simple aggregations such as sum, min, and max, 18 bytes for mean, and then approximately 50-200 bytes for
more complex aggregations like approx_count_distinct). For more details on determining the tradeoff between accuracy
and storage space, please reach out to the Chalk team.

When you query for a specific window_interval, Chalk will aggregate over all buckets that intersect with the window interval
If you are backfilling the materialized buckets on a schedule, and would like to directly query for the leading edge of data
from a different source, then you can set a continuous buffer duration, which will run online resolvers to compute the aggregation
for the buffer duration time window. If the continuous
buffer duration intersects with a filled bucket that starts at time t, then Chalk will run online resolvers to
compute the aggregation from t to the current time. Chalk will only ever include filled buckets in the aggregation
computation.

### Backfilling data and managing aggregation

Chalk provides multiple ways to backfill and update your windowed aggregations.

You can control how your aggregations are backfilled by:

- Supplying a cron expression (CronTab) to the backfill_schedule keyword parameter.
- Supplying a Duration to continuous_buffer_duration.
- Triggering a backfill job using the Chalk CLI with chalk aggregate backfill.

### Cron Schedule Expression

```
from chalk.features import features, _
from chalk import DataFrame, Windowed, windowed
from datetime import datetime

@features
class Transaction:
    id: int
    amount: float
    timestamp: datetime
    user_id: "User.id"

@features
class User:
    id: int
    transactions: DataFrame[Transaction]
    total_transaction_amount: Windowed[int] = windowed(
        "10d", "90d",
        materialization={
            "bucket_duration": "1d",
            "backfill_schedule": "0 0 * * *",
            "continuous_buffer_duration": "36h",
        },
        expression=_.transactions[
            _.amount,
            _.timestamp <= _.chalk_now,
            _.timestamp > _.chalk_window
        ].sum(),
    )
```

In the example above, we supply a cron expression that's set to run daily at midnight ("0 0 * * *") into the
backfill_schedule parameter of the materialization config.
Now backfill_schedule has been set, the total_transaction_amount feature will be backfilled every day.

### Continuous Buffer

In addition to backfilling your aggregation with the recurring batch job, you can also integrate fresh data into your
windowed aggregation with continuous backfills.
Continuous backfills can be configured by supplying a Duration to the continuous_buffer_duration e.g. "36h".
Chalk will compute data within your continuous_buffer_duration directly from your online resolvers.

Note: Chalk includes all the data contained in overlapping buckets.
We suggest shortening the bucket duration, if the time delta between the end of your window interval and the boundary
of the last overlapping bucket exceeds the constraints of your use case.

If continuous_buffer_duration is not set, then Chalk will only serve data from the backfilled aggregations.

no continuous buffer duration

If continuous_buffer_duration is set, and its value is less than the duration between the end of the last bucket
and the current time, Chalk will run online resolvers to compute the data for thistime window.

12h continuous buffer duration

If the continuous_buffer_duration is longer than the duration between the end of the last bucket and the current time,
Chalk will run online resolvers to compute the data from the start of the most recently filled bucket to now.

20h continuous buffer duration

### Triggering a backfill through the Chalk CLI

Use chalk aggregate backfill to trigger a backfill aggregation for a windowed feature.
This command is useful if you change your feature's time windows or bucket_duration values.

To view existing aggregations, use chalk aggregate list.

```
 Series  Namespace    Group                Agg     Bucket  Retention  Aggregation  Dependent Features
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 1       transaction  user_id merchant_id  amount  1d      30d        sum          user.txn_sum_by_merchant merchant.txn_sum_by_user
 1       transaction  user_id merchant_id  amount  1d      30d        count        user.txn_count_by_merchant
 2       transaction  user_id              amount  1d      30d        sum          user.txn_sum
```

The series column shows the unique ID of the timeseries data underlying our aggregation system.
Each unique combination of the Namespace,
Group (see group_by_windowed), and Agg (the aggregated feature) columns represents a separate timeseries.
When possible, Chalk will use the same timeseries data to serve multiple features.

Other useful information here is the Bucket column, which shows the current bucket size.
The Retention column shows the maximum time window of any feature that depends on the given timeseries.
The Dependent Features column lists the features that are served by the given timeseries.

### Materialized aggregations with streaming data

For information on updating materialized aggregations with streaming data, see the example in the streaming
documentation here.

### Materialization with Offline Queries

The aggregated buckets in the online store can currently only be accessed via an online query.
By default, if you specify a materialized windowed aggregation as output in an offline query, the engine will run resolvers,
with a preference for offline resolvers over online resolvers, to compute the expression in the materialized windowed
aggregation. There are also a few configurations that you can use to optimize your offline queries, or reproduce the
results of online queries for materialized aggregations. If you set align_offline_chalk_window_with_materialization,
this means that the lower bound of each query will round down to the next bucket boundary, to perfectly simulate the
results of the online query. To optimize offline queries for the materialized aggregation features, you can set
use_materialized_offline_query which will bucket the input times and events, and aggregate across all complete buckets
that intersect with the window interval.

# Streaming with Materialized Aggregations
source: https://docs.chalk.ai/docs/windowed-streaming

## Computing aggregate functions on streams.

Windowed features represent aggregated data pertaining to discrete time buckets.
Using materialized aggregations in concert with streams,
you can update aggregations on the fly as new streaming data arrives.

Materialized aggregations are a powerful tool
to compute aggregations over time windows, combining representations of historical data
with incoming real-time data to produce accurate and fresh results quickly.
If you have a stream resolver that outputs a feature that is related to a feature that uses
a materialized aggregation (more on this later), the materialized aggregations will be updated
as new messages arrive.

### Setting up a materialized aggregation

Setting up features for materialized aggregation with streaming is almost identical to the method described in the
materialized_aggregations docs.

```
from datetime import datetime
from chalk import features, has_many, DataFrame, _
from chalk.streams import Windowed, windowed

@features
class Transaction:
    id: str
    user_id: 'User.id'
    amount: float
    ts: datetime

@features
class User:
    id: str
    name: str
    transactions: DataFrame[Transaction]
    sum_transaction_amount: Windowed[float] = windowed(
        "30d",
        expression=_.transactions[_.amount].sum(),
        materialization=True,
        default=0.0,
    )
    mean_transaction_amount: Windowed[float] = windowed(
        "30d",
        expression=_.transactions[_.amount].mean(),
        materialization=True,
        default=0.0,
    )
```

Now, set up your streaming resolvers referencing these features using a native streaming resolver:

```
from pydantic import BaseModel
from chalk.features import _
from chalk.features.resolver import make_stream_resolver
from chalk.streams import KafkaSource

class TransactionMsg(BaseModel):
    id: str
    user_id: str
    amount: float

process_transaction_topic = make_stream_resolver(
    name="process_transaction_topic",
    source=KafkaSource(name="transactions"),
    message_type=TransactionMsg,
    output_features={
        Transaction.id: _.id,
        Transaction.user_id: _.user_id,
        Transaction.amount: _.amount,
    },
)
```

That's it! Now, when messages are received on the streams, Chalk will infer whether the output features
of the stream resolver are relevant to materialized aggregations, and if so, will update and store the data
in the existing materialized aggregations.

The resolver process_transaction_topic returns Transaction.id, Transaction.user_id, and Transaction.amount.
These features impact the materialized aggregate features User.sum_transaction_amount and
User.mean_transaction_amount. Both require two features on transaction:
Transaction.user_id (referenced through the join from _.transactions) and
Transaction.amount (referenced by _.amount in the aggregation expression).
When a streaming message comes through, the resolver process_transaction_topic will update
the materialized aggregations with the new values for User.sum_transaction_amount and
User.mean_transaction_amount.

To opt out of updating materialized aggregations, set updates_materialized_aggregations=False on the stream resolver.

### Online Storage

Similar to materialized aggregations that are backfilled from a non-streaming
data source, when the Chalk streaming server receives a message on a stream, if the streaming resolver is used
to compute a materialized aggregation, then the relevant data will be used to update the correct bucket for the
materialized aggregation. When a stream resolver is used to compute a materialized aggregation, the minimum amount of
data required to compute the aggregation will be stored for each bucket. For example, for a sum aggregation, the
sum of all values in the bucket will be stored. Then when new messages arrive, the appropriate bucket based on the
timestamp of the message will be updated with the new value. Because this data is stored online, you can access the
values through both online and offline queries.

# Streams
source: https://docs.chalk.ai/docs/streams

## Integrate with streaming data sources.

Chalk enables users to convert and aggregate streaming messages into Chalk features in realtime.

The first step towards building a streaming environment with Chalk
is creating a streaming source from one of Chalk's integrations.
Chalk supports Kafka, Kinesis,
and PubSub for streaming.
Like other integration sources, source parameters and credentials
may be specified in either the dashboard or the source instantiation in code.
See more information on KafkaSource,
KinesisSource, and PubSubSource in the API docs.

```
from chalk.streams import KafkaSource, KinesisSource, PubSubSource

kafka_topic = KafkaSource(name="transactions")
kinesis_topic = KinesisSource(name="transactions")
pubsub_topic = PubSubSource(name="transactions")
```

Now, let's set up the Chalk features you'd like to materialize upon stream message ingestion.

```
from chalk.features import features, Features

@features(max_staleness="1d")
class Transaction:
    id: str
    amount: float
```

Streaming resolvers produce feature values that are persisted to the offline store. Similar
to other resolvers, streaming resolvers can also persist computed feature values to the online
store by setting etl_offline_to_online=True or max_staleness in the @features decorator.

Chalk supports two kinds of streaming resolvers: mapping and windowed.
This page focuses on mapping resolvers, which create one Chalk feature instance per message.
Windowed streaming is covered in the windowed streaming page.

This is an example of a mapping resolver that maps from a bytes message to an instance of Transaction.

```
from chalk.streams import stream
from chalk.features import Features

@stream(source=source)
def stream_resolver(message: bytes) -> Features[Transaction.id, Transaction.value]:
    id, value = some_bytes_processing_step(message)
    return Transaction(id=id, value=value)
```

In this resolver, we pass in the raw bytes from the stream.
If you're using JSON as the encoding for messages on your topic,
you can optionally specify a
Pydantic Model
as a wrapper for messages on the topic.
Chalk will validate the encoding against the model.

```
from chalk.streams import KafkaSource
from chalk.features import features, Features
from pydantic import BaseModel

@features(max_staleness="1d")
class Transaction:
    id: str
    amount: float

kafka_topic = KafkaSource(name="transactions")

class TransactionTopicMessage(BaseModel):
    id: str
    amount: float

@stream(source=kafka_topic)
def stream_resolver(
    message: TransactionTopicMessage,
) -> Features[Transaction.id, Transaction.value]:
    return Transaction(id=message.id, value=message.value)
```

### Late arrivals

Chalk lets you configure whether resolvers should accept late-arriving stream messages.
By default, Chalk attempts to consider any late arriving in stream resolvers.
However, you can tune this behavior with the late_arrival_deadline argument
to you stream source:

```
from chalk.streams import KafkaSource

# By default, the late_arrival_deadline is set to "**infinity**".
source = KafkaSource(late_arrival_deadline="**30m**")
```

If a message is older than the late_arrival_deadline when it is consumed,
its resolver will not run.

### Parsing

Sometimes, messages must be processed before resolver execution.
Streaming resolvers can optionally support a parse function that preprocesses messages.
Possible use cases include

- Ingesting bytes and preprocessing before inputting data into a BaseModel.
- Optionally skipping resolver execution for certain messages.
- Re-keying for windowed stream aggregations.

The parse function runs before the resolver, and can transform the message into a format that the
stream resolver understands. If the parse function returns None, the resolver will be skipped.

A simple parse function can ingest bytes into a BaseModel, which will be used as input for the streaming resolver.

```
from pydantic import BaseModel

class TransactionMessage(BaseModel):
    id: str
    value: str

def parse_bytes(data: bytes) -> TransactionMessage:
    id, amount = some_bytes_processing_step(data)
    return TransactionMessage(id=id, amount=amount)

@stream(source=source, parse=parse_bytes)
def stream_resolver(message: TransactionMessage) -> Features[Transaction.id, Transaction.amount]:
    return Transaction(id=message.id, amount=message.amount)
```

In the below example, only UserEventMessages which have a click_event property will be processed by resolve_clicks.
Those where it is equal to None will not be processed, and skipped entirely.

```
from pydantic import BaseModel

# Child messages
class UserLoginEvent(BaseModel):
    ...

class UserClickEvent(BaseModel):
    ...

# Parent message contains one of the child message types
class UserEventMessage(BaseModel):
    login_event: UserLoginEvent | None = None
    click_event: UserClickEvent | None = None

def get_click_event(event: UserEventMessage) -> UserClickEvent | None:
    return event.click_event # can be None

@stream(source=str_source, parse=get_click_event)
def resolve_clicks(message: UserClickEvent) -> Features[...]:
    ...
```

### Full example

In this example, each of the messages from our Kafka source will be converted to a StreamFeature instance.
Our streaming message, embodied by KafkaMessage, contains a string representation of a naive datetime
we would like to convert to a timezoned datetime.

Upon message arrival, the bytes are first parsed into KafkaMessage,
then run through the parse function parse_message.
The intermediate output ParsedMessage is fed to the stream_resolver, which produces Chalk features.
Because we have specified max staleness and etl_offline_to_online,
we can expect StreamFeature to be queryable in both online and offline contexts.

```
from datetime import datetime, timezone
from dateutil import parser
from pydantic import BaseModel
from chalk.features import features, Features
from chalk.streams import stream, KafkaSource


source = KafkaSource(name="...")

class KafkaMessage(BaseModel):
    id: str
    value: str
    naive_timestamp_str: str

class ParsedMessage(BaseModel):
    id: str
    value: str
    event_timestamp: datetime


@features(max_staleness="1d", etl_offline_to_online=True)
class StreamFeature:
    id: str
    value: str
    event_timestamp: datetime

def parse_message(kafka_message: KafkaMessage) -> ParsedMessage:
    parsed_timestamp: datetime = parser.parse(kafka_message.naive_timestamp_str)
    timezoned_timestamp = parsed_timestamp.replace(tzinfo=timezone.utc)
    return ParsedMessage(
        id=kafka_message.id,
        value=kafka_message.value,
        event_timestamp=timezoned_timestamp
    )

@stream(source=source, parse=parse_message)
def kafka_stream_resolver(message: ParsedMessage) -> Features[StreamFeature.id, StreamFeature.value]:
    return StreamFeature(id=message.id, value=message.value, event_timestamp=message.event_timestamp)
```

### Testing Stream Resolvers

Testing stream resolvers can be difficult:
streaming is a complex paradigm that involves multiple services that can be difficult to replicate.

If your streaming resolvers error in production,
the errors will be logged and displayed on the dashboard for the resolver.
But if you're looking to unit test your stream resolvers, you have a few options.

One option is to feed dummy data into the resolver locally.
Like regular resolvers, stream resolvers should be unit-testable as regular Python functions.

```
from pydantic import BaseModel
from chalk.features import features, Features
from chalk.streams import stream, KinesisSource

kinesis_source = KinesisSource(name="...")

class KinesisMessage(BaseModel):
    payment_id: str
    amount: int

@features(max_staleness="1d", etl_offline_to_online=True)
class KinesisPaymentFeatures:
    id: str
    amount: int

@stream(source=kinesis_source)
def kinesis_stream_resolver(
    message: KinesisMessage,
) -> Features[KinesisPaymentFeatures.id, KinesisPaymentFeatures.amount]:
    return KinesisPaymentFeatures(id=message.payment_id, amount=message.amount)


model_example = KinesisMessage(id="1", amount=5)
result = kinesis_stream_resolver(model_example)
assert result.id == "1"
```

However, if you have a parse function,
custom timestamps, or other advanced functionality you want to test,
you may have to send messages to the streaming server.
Streaming resolver updates require a full chalk apply to update the
streaming server for testing.
Read more on how to use the ChalkClient to test streaming resolvers
here). This will pass messages
through your resolvers without persistence, and will return you a Polars DataFrame
with your output data for inspection.

```
from pydantic import BaseModel
from chalk.features import features, Features
from chalk.streams import stream, KinesisSource
from chalk.client import ChalkClient

kinesis_source = KinesisSource(name="...")

class KinesisMessage(BaseModel):
    payment_id: str
    amount: int

@features(max_staleness="1d", etl_offline_to_online=True)
class KinesisPaymentFeatures:
    id: str
    amount: int

# Note the use of a parse function here.
def parse_bytes(b: bytes) -> KinesisMessage:
    return KinesisMessage.parse_raw(b)

@stream(source=kinesis_source, parse=parse_bytes)
def kinesis_stream_resolver_with_parse(
    message: KinesisMessage,
) -> Features[KinesisPaymentFeatures.id, KinesisPaymentFeatures.amount]:
    return KinesisPaymentFeatures(id=message.payment_id, amount=message.amount)

client = ChalkClient()
messages = [KinesisMessage(payment_id=str(i), amount=i * 10).json().encode('utf-8') for i in range(10)]
resp = client.test_streaming_resolver(
    resolver="kinesis_stream_resolver_with_parse",
    message_bodies=messages,
)
print(resp.features)
```

### Online / Offline Storage

With mapping streaming resolvers, as with Python and SQL resolvers, Chalk will persist values to the
offline store if there is an offline store deployed in the environment. You would be able to access
these values with an offline query or through the SQL Interface.
If you would like to query features as resolved by a stream resolver, then the feature must have
etl_offline_to_online=True and max_staleness set in the feature definition. With these two settings, the
Chalk streaming server will also persist feature values to the online store, such that you can access recent
feature values through the online query pathway.

Note: if you would like
to resolve features in a feature class with a materialized aggregation defined as part of the feature class,
you should apply the max_staleness specifically to the features for which you would like to online query.
Otherwise, the aggregation will return the last observed value based on the max_staleness, rather than the actual
computed aggregation value.

# Stream Sources
source: https://docs.chalk.ai/docs/stream-sources

## Consuming Kafka streams.

Chalk supports Kafka, Kinesis, and PubSub as streaming sources
for @stream resolvers.

### Configuration options

You can configure the Kafka-, Kinesis-, or PubSub-specific options
either explicitly or through the Chalk dashboard.

### Named integration

If configuring through the dashboard, your Kafka/Kinesis integration
must be given a name. You can then reference this name in your
stream configuration.

The name of the integration as configured in your Chalk dashboard.

### Explicit configuration

You can instead choose to configure the source in your code directly for the following source types.

The Kafka broker's host name without the security protocol. You can specify multiple brokers by
passing a list of strings. Example: "localhost:9092" or ["localhost:9092", "localhost:9093"]

The topic or topics to subscribe to.

An S3 or GCS URI that points to the keystore file that should be used for brokers. You must
configure the appropriate AWS or GCP integration in order for Chalk to be able to access these
files.

Optionally, you may specify a prefix that will be used for client ids generated by @stream
resolvers that consume this source.

Optionally, you may specify a prefix that will be used for group ids generated by @stream
resolvers that consume this source.

Security protocol passed directly to Kafka. Defaults to 'PLAINTEXT'.

Authentication mechanism when security_protocol is configured for SASL_PLAINTEXT or SASL_SSL.
Defaults to 'PLAIN'.

Username for SASL PLAIN, SCRAM-SHA-256, or SCRAM-SHA-512 authentication. Defaults to null.

Password for SASL PLAIN, SCRAM-SHA-256, or SCRAM-SHA-512 authentication. Defaults to null.

The name of your stream. Either this or the stream_arn must be specified.

The ARN of your stream. Either this or the stream_name must be specified.

The AWS region, e.g. "us-east-2".

The AWS access key id credential, if not already set in the environment.

The AWS secret access key credential, if not already set in the environment.

The AWS session token credential, if not already set in the environment.

An optional endpoint to hit the Kinesis server.

An optional role ARN for the consumer to assume.

The project id that your pubsub source resides in.

The subscription id of your pubsub source.

### Example

```
from pydantic import BaseModel
from chalk import stream, feature
from chalk.streams import KafkaSource
from chalk.features import features, Features

@features
class User:
    id: str
    favorite_color: str = feature(max_staleness='30m')

class UserUpdateBody(BaseModel):
    user_id: str
    favorite_color: str

kafka_source = KafkaSource(name="user_favorite_color_updates")

@stream(source=kafka_source)
def fn(message: UserUpdateBody) -> Features[User.uid, User.favorite_color]:
    return User(
        id=message.value.user_id,
        favorite_color=message.value.favorite_color
    )
```

### Additional Configurations

For Kafka data sources, Chalk supports the following Kafka configuration values
for your integration. You can set these configurations within your Kafka Data Source either by constructing a dict of
{"your.kafka.config": "config_value"} and setting that under the ADDITIONAL_ENGINE_ARGUMENTS field, or by passing in
KafkaSource(additional_kafka_args=...) in your code-based data source configuration.

### Supported Kafka Configurations

Fetch & Polling Configuration

- fetch.min.bytes - Minimum amount of data the server should return for a fetch request
- fetch.max.bytes - Maximum amount of data the server should return for a fetch request
- fetch.max.wait.ms - Maximum time the server will block before answering the fetch request
- max.partition.fetch.bytes - Maximum amount of data per-partition the server will return
- max.poll.records - Maximum number of records returned in a single call to poll()
- max.poll.interval.ms - Maximum delay between invocations of poll()

Timeout Configuration

- session.timeout.ms - Timeout used to detect consumer failures
- heartbeat.interval.ms - Expected time between heartbeats to the consumer coordinator
- request.timeout.ms - Maximum amount of time the client will wait for the response of a request
- consumer.timeout.ms - Timeout for consumer operations
- poll.timeout - User-friendly alias for consumer.timeout.ms
- connections.max.idle.ms - Close idle connections after this many milliseconds

Retry & Reliability

- retry.backoff.ms - Time to wait before attempting to retry a failed request
- reconnect.backoff.ms - Base amount of time to wait before attempting to reconnect
- reconnect.backoff.max.ms - Maximum amount of time to wait when reconnecting

Metadata & Discovery

- metadata.max.age.ms - Period of time before forcing a refresh of metadata

Message Processing

- check.crcs - Automatically check the CRC32 of the records consumed
- isolation.level - Controls how to read messages written transactionally
- exclude.internal.topics - Whether internal topics should be exposed to the consumer

Protocol Settings

- receive.buffer.bytes - Size of the TCP receive buffer (SO_RCVBUF)
- send.buffer.bytes - Size of the TCP send buffer (SO_SNDBUF)
# Webhook Sources
source: https://docs.chalk.ai/docs/webhook-sources

## Handling webhooks with Chalk.

Webhook resolvers function almost exactly like stream resolvers.

The first step is to create a webhook source:

```
from chalk.webhooks import WebhookSource

source = WebhookSource(id="my_webhook_id")
```

You can optionally also specify a
Pydantic Model
for any of the body, headers, and query parameters.
Chalk will validate the parameters against the model.
If the model doesn't validate, Chalk will return a 400
with the Pydantic error message to the user.

```
from pydantic import BaseModel

class WebhookBody(BaseModel):
    username: str
    friends: list[int]
    ...

class QueryParameters(BaseModel):
    environment: str
    ...

class Headers(BaseModel):
    ...

source = WebhookSource(
    id="my_webhook_id",
    body=WebhookBody,
    query=QueryParameters,
    headers=Headers
)
```

Once you create the source and deploy your change,
Chalk will host a URL for your third-party service
to hit.

Webhooks will be exposed at the url

```
https://webhooks.chalk.ai/<client_id>/<environment>/<id>
```

After creating your webhook source,
you can start processing messages and creating feature values.
The webhook object above named source has an attribute
named Message that gives a type you can use in your resolver,
described below:

### webhook.Message

The body of the webhook. If you provided a Pydantic model in describing the webhook, this will be
a model. Otherwise, it will be the string contents of the body.

The query parameters attached to the URL. If the same query arg is used more than once, the value
in the dict will be a list of strings.

Request headers from the webhook.

Once you've defined your webhook source,
you can write a resolver for processing
webhook updates with the @webhook decorator:

```
from chalk.webhooks import webhook

@webhook
def fn(message: webhook.Message):
    ...
```

### Full example

```
from pydantic import BaseModel, Field
from chalk.webhooks import webhook, WebhookSource

class WebhookBody(BaseModel):
    webhook_type: str
    item_id: str


class Headers(BaseModel):
    plaid_verification: str = Field(alias="plaid-verification")

source = WebhookSource(
    id="plaid_transactions",
    body=WebhookBody,
    headers=Headers
)

@online
def get_transactions(account: Account.item_id) -> DataFrame[PlaidTransaction]:
    ...

@webhook
def fn(message: source.Message):
    verify_webhook(message.headers.plaid_verification)

    if message.body.webhook_type == "TRANSACTIONS":
        return get_transactions(message.body.item_id)
```

# Native Streaming Resolvers
source: https://docs.chalk.ai/docs/native-streaming

## Using Chalk expressions to define streaming resolvers

Native streaming resolvers provide a way to process streaming data using statically-defined expressions instead of Python functions. Similar to Chalk's expression-based feature definitions, these expressions are compiled and executed as vectorized C++, enabling high-throughput processing of stream messages.

### Overview

Native streaming resolvers can be defined using the make_stream_resolver() function. The definition takes a message type and a mapping from Chalk features to expressions. In production, raw streaming messages are first converted into the given message type. Then, the output features of the resolver are computed based on the given expressions.

### Basic Example

Let's start with a simple example that processes user data from a Kafka stream:

```
from chalk import Features, Primary, features
from chalk.features import _
from chalk.features.resolver import make_stream_resolver
from chalk import functions as F
from pydantic import BaseModel
import pyarrow as pa
import datetime as dt

# Define the Kafka stream source
kafka_source = KafkaSource(name="user_updates")

# Define the feature class
@features(max_staleness="30d", etl_offline_to_online=True)
class User:
    user_id: Primary[int]
    full_name: str
    email_address: str | None
    updated_at: dt.datetime | None

# Define the message schema
class ContactInfo(BaseModel):
    phone_number: str
    email_address: str | None

class UserMessage(BaseModel):
    id: int  # maps to user_id
    name: str
    updated_at: int  # epoch microseconds
    contact_info: ContactInfo


# Create a native streaming resolver
users_streaming_resolver = make_stream_resolver(
    name="get_users_stream", # The resolver name
    source=kafka_source,  # Your Kafka stream source
    message_type=UsersMessage,
    output_features={
        User.user_id: _.id,
        User.full_name: _.name,
        User.email_address: _.contact_info.email_address,
        User.updated_at: F.from_unix_seconds(_.updated_at / 1_000_000),
    },
)
```

Here, stream messages will come in as JSON strings whose structure matches the definition of the UserMessage model. The output features are defined as simple field accesses into the JSON struct. Note that nested access, such as _.contact_info.email_address, works as expected. Similar to feature definitions, scalar functions can be used to process the raw message fields. Here, we convert a raw integer timestamp in microseconds into a UTC datetime.

Note that the expressions here are are essentially the same as those used in feature definitions. However, the semantics are slightly different: The "root" here (), refers not to a namespace of features, but rather a table column whose datatype is based on the stream resolver's message_type. Thus, .amount does not mean "get me Chalk feature amount in the current namespace" but rather "access struct field amount on this column." In addition, since these expressions represent projections on single columns, dataframe operations such as .transactions[.amount, _.amount > 100].sum() don't apply here.

### Example Stream Messages

Here's what an incoming message might look like:

```
{
  "id": 123,
  "name": "John Smith",
  "updated_at": 1700000000000000,
  "contact_info": {
    "phone_number": "555-555-5555",
    "email_address": "john.smith@gmail.com",
  }
}
```

This message will get parsed into the following data:

```
User(
    id=123,
    full_name="John Smith",
    email_address="john.smith@gmail.com",
    updated_at=datetime.datetime(2023, 11, 14, 22, 13, 20, tzinfo=datetime.timezone.utc)
)
```

### Supported message types

The following message types are supported:

- Pydantic BaseModels or python @dataclasses: Incoming string messages will be deserialized from JSON into structs.
- Protocol buffer messages:  The incoming binary messages will be deserialized into structs with the various fields.
- str or bytes: The incoming messages can also be treated as simple strings or bytes. In this case, your feature expressions can't access struct fields on the message, but they can use scalar string/binary functions:

```
{
    Event.timestamp: _.timestamp #  INVALID -- strings don't have an 'age' field
    Event.raw_data_cleaned:  F.trim(F.lower(_)) # Here, `_` refers to the string message as whole.
    Event.timestamp: F.json_value(_, "$.metadata.timestamp") # This parses the input string as JSON and extracts a single field.
}
```

Note: Not all pydantic or protobuf types are supported. The message type needs to be converted into a well-defined PyArrow schema. Types that are recursive and can be arbitrarily nested will fail to be parsed. Similarly, Pydantic types with type annotations such as Any or complex union types are also not supported. To process these types in a native streaming resolver, use a custom parse function to only extract specific fields with well-known datatypes.

```

class PhoneInfo(BaseModel):
    number: str
    area_code: str

class EmailInfo(BaseModel):
    address: str

class Parent(BaseModel):
    id: int
    parent: Parent | None

class UsersMessage(BaseModel):
    id: int
    account_id: int | str # INVALID -- 'account_id' field's datatype is not well-defined
    card_id: int | None # Nullable types OK
    contact: PhoneInfo | EmailInfo # INVALID -- complex union types not supported
    parent: Parent | None # INVALID -- even if finitely nested in practice, the schema of this can't be determined ahead of time since it contains arbitrarily many sub-columns.

```

### Custom Parse Functions

By default, the message parsing logic is inferred automatically from the message_type. For Pydantic types or dataclasses, JSON parsing is used. For protobuf message classes,
these are parsed from the protobuf's binary representation. However, it is also possible to provide customer parsing logic. In addition to handling custom message formats, this also allows the stream resolver to skip a subset of messages. For instance, one might have multiple message types on the same kafka topic, or perhaps a stream of events where only events of type "CREATE" are relevant.

The make_stream_resolver() function has an optional parse argument that takes an expression. If provided, this expression will be used to convert raw message bytes into the expected message type. If the expression returns None, that message will be skipped.

For example, consider the following protobuf definition:

```
message User {
  enum UserType {
    USER_TYPE_UNSPECIFIED = 0;
    USER_TYPE_GUEST = 1;
    USER_TYPE_MEMBER = 2;
  }

  message ContactInfo {
    optional string phone_number = 1;
    optional string email_address = 1;
  }

  uint32 id = 1;
  string name = 2;
  UserType user_type = 3;
  optional ContactInfo contact_info = 4;
  uint64 updated_at = 5;
}
```

Let's say our system produces protobuf messages w/ an unusual format (a 6-byte prefix is added). We would like to strip the prefix before parsing and also ignore messages
for users of type "GUEST". We can use a custom parse expression to do this:

```
from messages.user_pb2 import UserMessage # Import the generated protobuf classes
from chalk import functions as F 
from chalk.features.resolver import make_stream_resolver


# Strip first 6 bytes, then parse the protobuf message
parsed_message = F.proto_deserialize(F.substr(_, 6, None), UserMessage)
# Exclude any UserMessages whose user_type == GUEST
parse_expression = F.if_then_else(
    parsed_message.user_type == UserMessage.UserType.GUEST, None, parsed_message
)

users_streaming_resolver = make_stream_resolver(
    name="get_users_stream",
    source=kafka_source,
    message_type=UserMessage,
    parse=parse_expression, # Custom parse expression provided here
    output_features={
        User.user_id: _.id,
        User.full_name: _.name,
        User.email_address: _.contact_info.email_address,
        User.updated_at: F.from_unix_seconds(_.updated_at / 1_000_000),
    },
)
```

### Testing Native Streaming Resolvers

Running native streaming resolvers locally is currently not supported. However, native streaming resolvers can be tested with sample messages from a notebook or client against the branch server or a production streaming server. In addition, native streaming resolvers defined in notebooks can be uploaded to Chalk servers for testing, without affecting the production deployment.

```
from chalk.client import ChalkClient

sample_messages = [
    '{"id": 123, "name": "John Smith"}',
    '{"id": 456, "name": "Alice Liddell"}',
]

client = ChalkClient()

# 1. Test messages against production resolver:
result = client.test_streaming_resolver(resolver="get_users_streaming", message_bodies=sample_messages)
# 'test_streaming_resolver' returns a signed URL to a parquet file in cloud storage -- `result.features` downloads this and extracts the table.
print(result.features)

# 2. Test messages against a stream resolver on a branch:
result = client.test_streaming_resolver(resolver="get_users_streaming", message_bodies=sample_messages, branch="new_users_stream_logic")
print(result.features)

# 3. Create a new resolver and test it:
new_users_resolver = make_stream_resolver(
    source=...,
    name="get_users_streaming_new",
    message_type=...,
    output_features={...},
)
result = client.test_streaming_resolver(resolver=new_users_resolver, message_bodies=sample_messages)
print(result.features)
```

### Performance Considerations

### Benefits of Native Streaming

- High Throughput: Process thousands of messages per second per CPU core
- Low Latency: Rust-based processing eliminates Python GIL overhead
- Parallel Processing: Automatic parallelization across CPU cores
- Type Safety: Compile-time validation of expressions

### When to Use Native Streaming

Native streaming is ideal for:

- High-volume data ingestion (>1000 messages/second)
- Low-latency feature computation (<10ms)
- Simple to moderate transformations
- Stateless processing

Consider traditional Python resolvers for:

- Complex business logic requiring external API calls
- Complex error handling and recovery logic

### Migration from Traditional Streaming

If you have an existing Python streaming resolver, you can create an equivalent native version:

```
from chalk.features.resolver import make_stream_resolver
from chalk import stream, Features



# Traditional Python resolver
@stream(source=user_stream)
def process_users(message: UsersMessage) -> Features[Users]:
    return Users(
        user_id=message.id,
        has_been_evicted_bool=message.qualification.has_been_evicted,
        monthly_income_min=message.qualification.monthly_income.min,
        # ... more processing
    )

# Equivalent native streaming resolver
process_users_native = make_stream_resolver(
    name="process_users_native",
    message_type=UsersMessage,
    output_features={
        Users.user_id: _.id,
        Users.has_been_evicted_bool: _.qualification.has_been_evicted,
        Users.monthly_income_min: _.qualification.monthly_income.min,
        # ... same mappings using underscore expressions
    },
    source=user_stream,
)
```

Both resolvers produce identical results, but the native version offers significantly better performance for high-throughput scenarios.

### Writing to a Sink

Native streaming resolvers can write computed features to downstream Kafka topics using the Sink parameter. This enables chaining of stream processing stages, where one resolver's output becomes another resolver's input. This pattern is particularly useful for:

- Multi-stage processing pipelines: Break complex transformations into discrete stages
- Feature routing: Direct specific features to specialized processing streams
- Model inference workflows: Send features to GPU-accelerated resolvers for heavy computation

The sink specifies which output features should be written to the destination stream. These features are computed by the resolver or by downstream resolvers that depend on the initial resolver's outputs.

### Example: Item Embedding Pipeline

This example demonstrates a two-stage pipeline where items are first processed through a native streaming resolver, then routed to a GPU-accelerated resolver for embedding generation:

```
from chalk.streams import KafkaSource
from chalk.features.resolver import Sink, make_stream_resolver
from chalk.features import _
from chalk import online
from pydantic import BaseModel
from src.models import Item
import numpy as np


class ItemMessage(BaseModel):
    id: int
    name: str
    price: float
    description: str
    image_url: str


new_items = KafkaSource(
    name="new_items",
)

embedding_stream = KafkaSource(
    name="item_embeddings",
)

make_stream_resolver(
    name="process_new_items",
    source=new_items,
    message_type=ItemMessage,
    output_features={
        Item.id: _.id,
        Item.name: _.name,
        Item.price: _.price,
        Item.description: _.description,
        Item.image_url: _.image_url,
    },
    sink=Sink(
        send_to=embedding_stream,
        output_features=[Item.id, Item.embedding],
    ),
)

@online(resource_hint="gpu")
def run_item_embedding_model(
    price: Item.price,
    description: Item.description,
    state: Item.state,
    image_url: Item.image_url,
) -> Item.embedding:
    """Mock generate item embedding using a pre-trained model."""
    # In a real implementation, this function would load a pre-trained model
    # and generate an embedding based on the input features or make an API
    # call to an external service.
    return np.random.rand(128).tolist()
```

In this example:

- The process_new_items resolver consumes messages from the new_items Kafka source and extracts basic item features
- The sink configuration specifies that Item.id and Item.embedding should be written to the item_embeddings stream
- When a message is processed, Chalk computes Item.item_embedding by calling the run_item_embedding_model resolver, which runs on a GPU-enabled instance
- The computed features are then written to the item_embeddings topic

This pattern allows the lightweight native streaming resolver to handle high-throughput message parsing while delegating compute-intensive embedding generation to specialized GPU resources. The sink acts as a bridge, automatically triggering the downstream computation and routing results to the appropriate stream.

Messages can be encoded as either arrow IPC streams or as JSON. The fully qualified feature names are used as the column names in the output stream or as the JSON keys.

### Skip Writing to the Offline Store

If you already store a historical log of your stream messages in a data warehouse, you can disable stream persistence to the Chalk offline store. This can be done by setting the skip_offline parameter of make_stream_resolver:

```
users_streaming_resolver = make_stream_resolver(
    name="get_users_stream",
    source=kafka_source,
    message_type=UsersMessage,
    output_features={
        User.user_id: _.id,
        User.full_name: _.name,
        User.email_address: _.contact_info.email_address,
        User.updated_at: F.from_unix_seconds(_.updated_at / 1_000_000),
    },
    skip_offline=True, # don't write resolved events from stream to offline store
)
```

### Environment-specific Stream Resolvers

A stream resolver can be restricted to a specific environment through the environment parameter of make_stream_resolver:

```

@features(max_staleness="30d", etl_offline_to_online=True)
class Transaction:
    transaction_id: Primary[int]
    submitted: dt.datetime
    amount: int

class TransactionMessage(BaseModel):
    id: int # maps to transaction_id
    submitted: int # epoch microseconds
    amount: int

# new resolver to experiment with new Transaction class
experimental_streaming_resolver = make_stream_resolver(
    name="new_transaction_stream_resolver",
    source=kafka_source,
    message_type=UsersMessage,
    output_features={
        Transaction.transaction_id: _.id,
        Transaction.timestamp: F.from_unix_seconds(_.submitted / 1_000_000),
        Transaction.amount: int
    },
    environments=["dev"], # only deploy resolver in "dev" environment
)
```

# Resolvers Overview
source: https://docs.chalk.ai/docs/resolver-overview

## Create resolvers to compute feature values.

While feature classes define what your data looks like (e.g. the types of your features,
their relationships, and their properties), resolvers define how your feature values
are computed.

If you haven't read the section on feature classes, you are strongly encouraged to do so.
Understanding feature classes will help you understand resolvers.

Resolvers have four main components: inputs, outputs, code, and run conditions.

The first three of these are rather straightforward. The inputs to a resolver
are the features it uses to compute its output. The outputs of a resolver
are the features that it computes. The code of the resolver is the logic that
transforms your input features into your output features.

The last component, run conditions, is a little more nuanced. At a high level,
Chalk is optimized for two different access patterns: online and offline. In online
access, information about a single entity is being requested and features must be
computed quickly and cached. In offline access, a large chunk of historical
feature data is being requested (you can think of this as creating a dataset for model
training or running an analytic query).

Resolvers are always specified as either online or offline. We go into more detail
about what this means in the next section where we talk about run conditions,
but for now it is important to note that: 1). every resolver is either online or offline, and 2). different
resolvers run depending on how you are requesting data from Chalk.

### Writing Resolvers

Chalk allows you to write resolvers in three different ways:

- as SQL queries, with comments specifying data sources and output features.
- as python functions, with type annotations specifying the input and output features.
- as an expression, inline in your feature definitions.

Below is an example of how to write the three kinds of resolvers in Chalk
for a User feature class. In this example, we assume that a Postgres data source
called pg_users has been configured and connected to Chalk.

First, let's define our User feature class:

```
from chalk.features import features

@features
class User:
  id: str
  name: str
  age: int
  hobbies: list[str]

  is_runner: bool  # computed feature
  athleticism_score: float # computed feature
```

Now we define our resolvers:

We resolve the id, name, age, and hobbies features for our users from the
users table of our pg_users data source. When reading data from your data
sources, you should use a SQL resolver:

```
-- The features given to us by the user.
-- resolves: user
-- type: online
-- source: pg_users
select id, name, age, hobbies
from users;
```

To compute the is_runner feature for users, we simply check whether running is in
the list of hobbies, which we can do with an expression. Chalk expressions utilize low-latency
C++ for efficient execution. Chalk expressions can use any of the chalk.functions to express
a variety of computations.

```
import chalk.functions as F
from chalk.features import features, _

@features
class User:
  id: str
  name: str
  age: int
  hobbies: list[str]

  is_runner: bool = F.contains(_.hobbies, "running")
  athleticism_score: float # computed feature
```

We now use a python resolver to compute the athleticism_score feature for our users.
Python resolvers are useful for integrating existing libraries, and executing more complex
logic, such as API calls.

```
from chalk import online
from src.user import User
from utils.athleticism import is_athletic

@online
def get_is_runner(
    hobbies: User.hobbies
) -> User.athleticism_score:
    num_athletic_hobbies = sum([is_athletic(hobby) for hobby in hobbies])
    return num_athletic_hobbies / len(hobbies)
```

### When Do Resolvers Run

A question that often crops up at this point is, "I have defined a resolver, but how do
I make it run?"

Just like features, the idea behind resolvers is that they are declarative. Resolvers
don't run when you define them, and they don't run exhaustively over your data. They run
only in response to a request for the features that they are responsible for computing. In
practice, this means that they run in response to "queries".

Resolvers can also be run on a schedule or triggered. Either approach causes them to 1). execute,
in batch-job fashion, across all data they find in your upstream data sources, and 2). write
computed features to your offline store.

A query is just a request for data. Chalk takes a query and determines which resolvers it
needs to run, optimizes the execution order, and provides you with a response. For now, we'll
hold off on discussing queries further, but feel free to skip ahead and
get a sense of what Chalk queries are and how they work before diving
deeper into resolvers.

# Online / Offline
source: https://docs.chalk.ai/docs/resolver-online-offline

## Eliminate train-serve skew with shared logic.

Chalk supports two primary execution contexts: online (for inference) and offline (for training).
Online contexts handle real-time prediction requests with millisecond latency requirements, while
offline contexts process historical data for model training and analysis.

Chalk enables you to write resolvers that can run in either or both contexts,
helping eliminate train-serve skew while optimizing for the different performance
characteristics of each environment.

### Online and Offline Resolvers

Online resolvers are eligible to run in online and offline queries.
However, in an offline context, Chalk will prefer to run an offline resolver
to an online resolver if both are available for the same feature.

Offline resolvers can run only in offline queries, and can never
be used as part of an online query.

There are three types of resolvers: expressions, Python resolvers, and SQL resolvers.
Expressions are online resolvers, while Python and SQL resolvers can be specified as
either offline or online.

### Expressions

Chalk expressions are online resolvers.
However, an expression can operate on data that is fetched from either an online or offline resolver.
Expressions are written in terms of the data model, and thus are portable between online and offline contexts.

For example, consider the following feature definition:

```
from chalk import _
from chalk.features import features

@features
class User:
    id: int
    first_name: str
    last_name: str
    full_name: str = _.first_name + " " + _.last_name
```

The full_name feature is defined as an expression that concatenates the first_name and last_name features.
No matter how we compute first_name and last_name, the expression for full_name remains the same.
If we have a PostgreSQL online resolver that computes first_name and last_name from a low-latency database,
we can use that resolver in an online query.
If we have a Snowflake offline resolver that computes first_name and last_name
from a data warehouse, we can use that resolver in an offline query.

Scalar expressions like this one are also time-independent. So long as the underlying features
are temporally consistent, the expression will be as well.
If your expression depends on time-varying data, such as a DataFrame aggregation,
you can use _.chalk_now or _.chalk_window (in the case of a windowed aggregation)
to ensure temporal consistency.

```
from datetime import timedelta, datetime
from chalk import _
from chalk.features import features, DataFrame, windowed, Windowed

@features
class Transaction:
    id: int
    user_id: "User.id"
    amount: float
    at: datetime

@features
class User:
    id: int
    transactions: DataFrame[Transaction]
    total_amount_last_30d: float = _.transactions[
        _.at >= _.chalk_now - timedelta(days=30),
        _.amount
    ].sum()
    average_transaction_amount: Windowed[float] = windowed(
        "1d", "30d", "365d",
        expression=_.transactions[_.amount, _.at > _.chalk_window].mean(),
    )
```

Now, total_amount_last_30d and average_transaction_amount will compute
the same values in both online and offline contexts,
regardless of how the transactions for the User are fetched.

At inference time, _.chalk_now will be the current time,
and _.chalk_window will be the time of the query less the window size.
At training time, _.chalk_now will be the point-in-time of the query,
and _.chalk_window will be the point-in-time of the query less the window size.

### Python

To define a Python resolver as online or offline,
use the @online or @offline decorator.

```
from chalk.features import online, offline, DataFrame
from src.features import User, Transaction

@online
def get_email_username(email: User.email) -> User.email_username:
    username = email.split("@")[0]
    if "gmail.com" in email:
        username = username.split("+")[0].replace(".", "")
    return username.lower()

@offline
def get_transactions() -> DataFrame[
    Transaction.id,
    Transaction.amount,
    Transaction.date,
]:
    return DataFrame.read_parquet(...)
```

Online Python resolvers can run in both online and offline queries,
while offline Python resolvers can run only in offline queries.
Typically, almost all Python resolvers will be online.
The most common use-case for offline Python resolvers
is to load parquet files or other data files that represent historical data.

If your online Python resolver is time-dependent,
you can pull in the point-in-time of the query
to ensure temporal consistency.

```
from chalk import Now, online

@online
def get_age(birthdate: User.birthdate, now: Now) -> User.age:
    return (now.date() - birthdate).days // 365
```

At inference time, chalk.Now will be the current time,
and at training time, chalk.Now will be the point-in-time of the query.

### SQL

To define a SQL resolver as online or offline, use the type field in the resolver comment.

```
  -- resolves: User
  -- source: postgres
+ -- type: online
  select
    id,
    name,
    age
  from users
```

With SQL resolvers, you're likely to want to define an online and offline variant.
You would never want to run a query against, for example,
Snowflake in an online context. Snowflake, and other data warehouses
like BigQuery, Databricks, and Redshift, are not designed for low-latency queries.
Instead, you would want to run a query against a low-latency
database like Postgres or MySQL in an online context.

In contrast, with an offline query, you might want to run a query against
Snowflake to get a large amount of data, and you might not have a Postgres
instance that contains all the data you need or can handle unloading terabytes of data.

```
  -- resolves: User
+ -- source: snowflake
+ -- type: offline
  select
    id,
    name,
    first_name,
    last_name,
    age
  from users
```

```
  -- resolves: User
+ -- source: postgres
+ -- type: online
  select
    id,
    name,
    age
  from users
```

Note that these two resolvers can have different schemas.
The offline Snowflake resolver above returns first_name and last_name in addition to name,
while the online Postgres resolver returns only name.

### Eliminating train-serve skew

Introducing different online and offline resolvers leads to an opportunity
to introduce different means of computing a feature.
Online and offline SQL resolvers are a necessary source of skew.
Data warehouses cannot stand up to production traffic request volumes,
and transactional databases cannot store the nearly unlimited data volumes
where warehouses excel.

However, we should aim to minimize this skew as much as possible.
For example, consider these aggregation features for user transaction statistics:

```
@features
class User:
    id: int
    count: int
    avg_amount: float
    amount_stddev: float
```

Implementing the same feature logic twice in different SQL dialects invites subtle bugs and inconsistencies.

These SQL resolvers look nearly identical, but they produce subtly different results due to differences in how Postgres and Snowflake handle standard deviation calculations and rounding. The STDDEV_POP() in Postgres computes population standard deviation, while Snowflake's STDDEV() defaults to sample standard deviation. Additionally, the rounding methods (::DECIMAL vs ROUND()) can produce different results for edge cases. These small numerical differences can compound and degrade model performance in production.

Implementation for Postgres online context

```
-- resolves: User
-- source: postgres
-- type: online
select
    user_id as id,
    count(*) as count,
    avg(amount)::decimal(10,2) as avg_amount,
    stddev_pop(amount)::decimal(10,2) as amount_stddev
from transactions
where created_at >= current_date - interval '30 days'
group by user_id
```

Now you need to implement the same logic again for the offline context, but adapted for Snowflake's SQL dialect.
Notice how even though the intent is identical, the implementation details differ—different function names,
different date arithmetic syntax, and different rounding behavior.

Separate implementation for Snowflake offline context

```
-- resolves: User
-- source: snowflake
-- type: offline
select
    user_id as id,
    count(*) as count,
    round(avg(amount), 2) as avg_amount,
    round(stddev(amount), 2) as amount_stddev
from transactions
where created_at >= dateadd('day', -30, current_date())
group by user_id
```

Write the aggregation logic once using Chalk expressions, and it runs identically in both online and offline contexts.

Instead of computing these aggregations differently in each database, you can fetch the raw transaction data and compute the statistics using Chalk expressions. This ensures the exact same computation logic runs in both online and offline contexts, completely eliminating this source of train-serve skew. The expression syntax is simple and declarative—you just specify what you want to compute, and Chalk handles the execution optimally for each environment.

Using expressions to compute derived features consistently

```
from chalk import _
from chalk.features import features, DataFrame

@features
class User:
    id: int
    transactions: DataFrame[Transaction]

    count: int = _.transactions.count()
    avg_amount: float = _.transactions[_.amount].mean()
    amount_stddev: float = _.transactions[_.amount].std()
```

### Storage

Chalk includes an online and an offline store. The online store is used to cache data to make
realtime data requests extremely fast, while the offline store is a data warehouse that stores
all the features that you've computed—enabling monitoring and dataset generation for training.

Your online store holds data that you want to cache
according to the cache policies you set on your features or
on your queries.
At inference time, you need exceptionally fast reads to serve data at low latency.
However, it's not important to keep every value of every historical feature value
around for low-latency access.
This access pattern aligns with the performance characteristics of
Redis or DynamoDB,
which Chalk uses to store your online data.

The offline store holds far more data than the online store.
It keeps a record of all online runs
and indexes all data brought in from your offline data sources.
Chalk integrates with a number of different data warehouse systems for our large-scale
offline storage depending on customer needs and deployment type,
including BigQuery, Snowflake, and Redshift.

In addition, offline queries write their output to a parquet file
in cloud storage (S3/GCS), whereas online queries write their results to database.

| writes to the offline store                                                                       | writes to the online store                                                                                                      |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| an online query writes all freshly computed features (those not read from the online store)       | an online query writes all freshly computed features with max_staleness != 0                                                  |
| A triggered resolver run with store_offline=True (default behavior)                             | A triggered resolver run with store_online=True (default behavior)                                                            |
| scheduled queries with recompute_features=True and store_offline=True (default behavior)      | scheduled query with store_online=True (default behavior)                                                                     |
| Ingesting a dataset to the offline store: dataset.ingest(store_offline=True)                    | Ingesting a dataset to the online store: dataset.ingest(store_online=True)                                                    |
| offline queries with ChalkClient.offline_query(store_offline=True)                              | offline queries with ChalkClient.offline_query(store_online=True)                                                             |
| An @online or @offline scheduled resolver                                                     | An @online or @offline scheduled resolver that computes features with max_staleness!=0 and etl_offline_to_online=True  |
| A streaming resolver: @stream                                                                   | A streaming resolver: @stream                                                                                                 |

### Querying

Every request you make to Chalk for data is done through a query, and every query
you make is either an online or an offline query.

Online queries are used to receive information about a single entity.
For example, you might be looking to compute the features of a
credit model for a single user, or decide what products to suggest
to a customer. Thus, online queries are designed to be as quick as possible—
within milliseconds. You can use our API client to run
queries.

Offline queries are used to sample historical data about many entities
at specific points in time for model training or investigation.
When you execute an offline query, Chalk will kick off a job that acquires the requested data for
every primary key/timestamp combination presented. This could take a few seconds!
Since offline queries often lookup data for thousands of
rows, they are not designed to be used to make millisecond-level decisions.
See our guide on offline queries
for a more in-depth treatment.

|                  | online query                      | offline query                                                                                        |
|------------------|-----------------------------------|------------------------------------------------------------------------------------------------------|
| online resolver  | @online resolver will run       | @online resolver will run if there is no @offline resolver with the same definition             |
| offline resolver | @offline resolver will never run | @offline resolver will run                                                                        |

### Online/Offline Interaction

### Online-to-Offline

After an online resolver runs, its values are copied into the offline store.
When you query the offline store,
you will receive data from both records of online runs and offline-specific resolvers.
Which data you receive depends on which data was closest to the point-in-time
that you queried.
For more information, see temporal consistency.

### Offline-to-online

In contrast, data from the offline store does not
reach the online store by default.
However, you can choose to ETL the data from an offline
resolver into the online store.
This can be helpful, for example,
when you tolerate stale data in online inference and
have a data source in the offline store that doesn't
have a direct replacement in the online store.
More details are provided in the section Reverse ETL.

### Summary

| Online query                                                               | Offline query                                                                                                                                                                           |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Runs only @online resolvers                                              | Runs both @online and @offline resolvers                                                                                                                                            |
| Returns one row of data about one entity                                   | Returns a DataFrame of many rows of historical data corresponding to multiple entities at historical time points                                                                        |
| Designed to return data in milliseconds                                    | Blocks until computation is complete, not designed for millisecond-level computation                                                                                                    |
| Queries the online store and calls @online resolvers for quick retrieval | Queries the offline store which stores all data from online queries, unless recompute_features=True, in which case @offline and @online resolvers are used to resolve the outputs |
| Writes output data to online store database and offline store database     | Writes output to a parquet file containing results to cloud storage. Only writes to online store or offline store if specified.                                                         |

# SQL Resolvers
source: https://docs.chalk.ai/docs/sql-resolvers

## Define feature resolvers as a SQL query.

SQL resolvers enable you to load and transform data from your data sources as feature values.

### Defining SQL Resolvers

There are two ways to define SQL resolvers. The first is to write a SQL query in a file with the
.chalk.sql extension, and the second is to use the make_sql_file_resolver
function, which will generate a SQL file resolver based on the function arguments at build time.

### SQL File Resolvers

To define a SQL resolver in a file, create a file with the .chalk.sql extension, add comments to specify
the data source the SQL query will run on and the feature class whose features it will resolve, and write
the SQL query.

```
-- source: pg_users
-- resolves: User
select id, name, age, hobbies from users
```

The output column names in the SQL query must match the feature names in the feature class specified in the
resolves comment. The data source specified in the source comment must also match the name of the data
source configured in the Chalk dashboard. Each SQL file resolver must only resolve features within the
same feature class, but a resolver does not have to resolve all features within the feature class.

### Generating SQL File Resolvers

To generate SQL file resolvers at build time, use the make_sql_file_resolver
function. This function enables you to define one or many SQL file resolvers at a time that may have slight
variations, for example querying a different data source in a different environment. The following code
would generate an equivalent SQL file resolver to the one above:

```
from chalk import make_sql_file_resolver

make_sql_file_resolver(
    name="get_user",
    source="pg_users",
    resolves="User",
    query="select id, name, age, hobbies from users"
)
```

### SQL Resolver Configurations

As with Python resolvers, SQL resolvers can be configured through many optional parameters. For generating SQL
file resolvers, these parameters are passed as arguments to the make_sql_file_resolver
function. For SQL file resolvers, these parameters are specified in the comments at the top of the file.

```
-- These parameters are required in all SQL file resolvers
-- source: pg
-- resolves: User

-- These parameters are optional in all SQL file resolvers
-- type: online <-- default is "online," but can also be "offline" or "streaming"
-- incremental: <-- read more about incremental resolvers here: https://docs.chalk.ai/docs/sql#incremental-queries
--   mode: row
--   lookback_period: 60m
--   incremental_column: updated_at
-- count: 1 <-- the number of rows the resolver should return. This can be set to 1, 'one', 'one_or_none', or 'all'
-- timeout: 5m <-- the maximum time the resolver should run before timing out
-- cron: 0 0 * * * <-- a cron expression to schedule the resolver to run at a specific time
-- owner: 'helly@lumonindustries.com' <-- the email of the owner of the resolver. Alerts can be routed to owners.
-- tags: ['user', 'profile'] <-- tags to help organize resolvers in the Chalk dashboard
-- environment: 'production' <-- the environment in which the resolver should run
-- total: True <-- whether this resolver returns all ID's of a given namespace.

select id, name, age, hobbies, updated_at from users
```

For the full list of configurations, see here.

### Testing

To test your SQL resolvers, we recommend setting up integration tests
or iterating on a branch.

# Expressions
source: https://docs.chalk.ai/docs/expression

## Using Chalk expressions to define features

### Overview

Chalk Expressions let you define features declaratively, using symbolic computation over your data.
While you write expressions in idiomatic Python, they are compiled and executed as vectorized C++,
enabling low-latency computation at serve time and high-throughput processing at train time.

Expressions support a wide range of operations, including arithmetic, filtering, aggregations,
and built-in functions like .

For example, in a Transaction feature class, we can compute the subtotal of a transaction as the
difference between its total and sales tax:

```
from chalk.features import features, Primary
from chalk import _

@features
class Transaction:
    id: int
    total: float
    sales_tax: float
    subtotal: float = _.total - _.sales_tax
```

The _ symbol refers to the current scope (here, the feature class Transaction)
and is used to reference other fields on the same instance.
Expressions like _.total - _.sales_tax are compiled into native execution
plans that run efficiently in production.

In addition to referencing fields on the same object, you can traverse relationships.
If each Transaction is associated with a User, for example, you can compute a
string similarity between the user’s name and the transaction memo:

```
  from chalk.features import _, features
+ import chalk.functions as F

  @features
  class Transaction:
      ...
      amount: float
      memo: str
      user: "User"
+     name_match_score: float = F.jaccard_similarity(
+       _.user.name, _.memo
+     )
```

Here, _.user.name follows the foreign key relationship from Transaction to User.
The function F.jaccard_similarity is one of many built-in Chalk functions that
operate on symbolic expressions.

Expressions can also perform aggregations over related records.
In a User feature class, we can compute aggregates like the
number of large transactions or the total amount spent:

```
from chalk import _
from chalk.features import DataFrame, features

@features
class User:
    id: int
    name: str
    transactions: DataFrame[Transaction]

    # Total spend is nullable because the sum of an empty DataFrame is null
    total_spend: float | None = _.transactions[_.total].sum()

    # The count is never null, because an empty DataFrame has count 0
    num_large_txns: int = _.transactions[_.total > 1000].count()
```

In this context, _ refers to the User instance when referring to _.transactions.
But when you apply a filter, like _.transactions[_.total > 1000],
the expression inside the brackets is evaluated in the context of each individual Transaction.
That means _.total refers to the total field on each Transaction, not on the User.
This scoped evaluation makes it easy to filter, project, and aggregate over related data.

All expressions are statically analyzed, optimized to eliminate redundant computation,
and executed as high-performance C++ at runtime.

### Scalar Functions

Chalk expressions support a wide range of built-in functions for manipulating data, performing calculations,
and transforming features. These functions can be used in expressions to operate on feature values, DataFrames, and other data types.

```
- from chalk import features, online
+ from chalk.features import _, features

@features
class Transaction:
    id: int
    total: float
    sales_tax: float
+   subtotal: float = _.total - _.sales_tax

- @online
- def get_subtotal(total: Transaction.total, sales_tax: Transaction.sales_tax) -> Transaction.subtotal:
-     return total - sales_tax
```

### Infix Operators

Chalk expressions support a variety of infix operators for arithmetic, conditions, and boolean logic.

| Operator        | Description              | Example                                      |
|-----------------|--------------------------|----------------------------------------------|
| +             | Addition                 | _.total + _.sales_tax                      |
| -             | Subtraction              | _.total - _.sales_tax                      |
| *             | Multiplication           | _.quantity * _.price                       |
| /             | Division                 | _.total / _.quantity                       |
| >             | Greater than             | _.total > 1000                             |
| >=            | Greater than or equal    | _.total >= 1000                            |
| <             | Less than                | _.total < 1000                             |
| <=            | Less than or equal       | _.total <= 1000                            |
| ==            | Equal                    | _.status == "completed"                    |
| !=            | Not equal                | _.status != "completed"                    |
| &             | Boolean and              | _.is_active & _.is_verified                |
| | | Boolean or               | _.is_active | _.is_verified |
| ~             | Boolean not              | ~_.is_active                               |

Python does not allow these operators to be overridden, so they will not work with Chalk's expressions.
Instead, use the infix operators &, |, and ~ for boolean logic,
and use == and != for equality comparisons.

### Builtin Functions

The chalk.functions module exposes several helpful functions that can be used in
combination with expression references to transform features. These functions are meant
to be used in expressions and are not available as standalone functions. To view all
available functions, see our SDK docs.

### Structs

Expressions can be used to access nested attributes from other features in a feature class, whether these
other features are struct dataclasses, features, or DataFrames.

```
import chalk.functions as F
from chalk.features import features
from dataclasses import dataclass

@dataclass
class LatLon:
    lat: float | None
    lon: int | None

@features
class User:
    id: int
    home: LatLon
    work: LatLon
    commute_distance: float = F.haversine(
        lat1=_.home.lat,
        lon1=_.home.lon,
        lat2=_.work.lat,
        lon2=_.work.lon,
    )
```

### Custom Functions

You can create custom functions to encapsulate complex logic or reusable computations in your expressions.
For example, if you wanted to apply consistent windows across many features, you could define a custom function
like this:

Use helper functions to create expressions

```
from chalk import _
from chalk.features import features, DataFrame

def count_where(*filters):
    return _.transactions[_.created_at > _.chalk_window, *filters].count()

@features
class User:
    id: int
    transactions: DataFrame[Transaction]
    num_large_transactions: int = count_where(_.total > 1000)
    num_small_transactions: int = count_where(_.total < 100)
```

Expressions are not supported in Python resolvers, so you cannot use Chalk functions like F.jaccard_similarity
in a Python resolver.

Don't use expressions in Python resolvers

```
@features
class User:
    id: int
    name: str
    email: str
    name_email_match_score: float

@online
def get_score(
    name: User.name,
    email: User.email,
) -> User.name_email_match_score:
    # Don't do this!! Expressions don't run in Python resolvers
    return F.jaccard_similarity(name, email)
```

Instead, use expressions to define the feature directly in the feature class:

Use expressions in feature classes

```
@features
class User:
    id: int
    name: str
    email: str
    name_email_match_score: float = F.jaccard_similarity(
        _.name, _.email
    )
```

### DataFrame Functions

### Conditions and filters

DataFrame features can be filtered with expressions.

Extending our Transaction example, we can create a User feature class with a has-many relationship
to Transaction. Then, we can define a feature representing the number of large purchases by referencing the existing
User.transactions feature:

```
  from chalk.features import _, features, DataFrame

  @features
  class Transaction:
      id: int
+     user_id: "User.id"
      total: float
      sales_tax: float
      subtotal: float = _.total - _.sales_tax

+ @features
+ class User:
+    id: int
+    # implicit has-many relationship with Transaction due to `user_id` above
+    transactions: DataFrame[Transaction]
+    num_large_transactions: int = _.transactions[_.total > 1000].count()
```

The object referenced by _ changes depending on its current scope. In this code, the _ in _.transactions
references the User object.
Within the DataFrame filter, the _ in _.total references each Transaction object as each one is evaluated.
The count aggregation is covered in the next section.

### Projections and aggregations

DataFrame features support projection with expressions, which produce a new
DataFrame scoped down to the referenced columns. DataFrames can be aggregated after eligible columns are selected.

With our Transaction example, we already saw a count aggregation for counting the number of large transactions. We
can add another aggregation for computing the user's total spend:

```
from chalk.features import _, features, DataFrame

@features
class Transaction:
    id: int
    user_id: "User.id"
    sales_tax: float
    subtotal: float
    total: float = _.subtotal + _.sales_tax

@features
class User:
    id: int
    transactions: DataFrame[Transaction]
    num_large_transactions: int = _.transactions[_.total > 1000].count()
+   total_spend: float = _.transactions[_.total].sum()
```

To compute User.total_spend, we needed to create a projection of the User.transactions
DataFrame limited to only the Transaction.total column so that the sum aggregation could work.
In contrast, no projection was needed for the num_large_transactions aggregation because count
works on DataFrames with any number of columns.

For computing low-latency aggregations over high volumes of data, Chalk also offers
materialized windowed aggregations
that uses materialization of buckets of data to compute large aggregations efficiently.

### Aggregation functions

Aggregation functions have varying behavior when handling None values and empty DataFrames.
If an aggregation function says None values are skipped in the table below,
it will consider a DataFrame with only None values as empty.

| Function                 | None values | Empty DataFrame   | Notes                                                                                                                                                                                                                        |
|--------------------------|-------------- |-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| sum                    | Skipped       | Returns 0       |                                                                                                                                                                                                                              |
| min                    | Skipped       | Returns None    |                                                                                                                                                                                                                              |
| max                    | Skipped       | Returns None    |                                                                                                                                                                                                                              |
| mean                   | Skipped       | Returns None    | Feature type must be float or float \| None. None values are skipped, meaning they are not included in the mean calculation.                                                                                           |
| count                  | Included      | Returns 0       |                                                                                                                                                                                                                              |
| any                    | Skipped       | Returns False   |                                                                                                                                                                                                                              |
| all                    | Skipped       | Returns True    |                                                                                                                                                                                                                              |
| std                    | Skipped       | See notes         | Standard deviation. Requires at least 2 values. For DataFrames with less than 2 values, returns None.  Aliases: stddev, stddev_sample, std_sample.                                                              |
| var                    | Skipped       | See notes         | Variance. Same requirements as std.  Alias: var_sample.                                                                                                                                                             |
| approx_count_distinct  | Skipped       | Returns 0       |                                                                                                                                                                                                                              |
| approx_percentile      | Skipped       | Returns None    | Takes one argument, quantile, expected to be a float in the range [0, 1].  Example: approx_percentile(0.75) returns a value approximately equal to the 75th percentile of the not-None values in the DataFrame. |
| approx_top_k           | Skipped       | Returns None      | Takes one argument, k, expected to be a positive integer, as a keyword argument.  Example: approx_top_k(k=25) returns the 25 or fewer approximately-most common values.

For aggregations that can return None, either mark the feature as optional
(for example, by setting the feature type to float | None) or use coalesce
to fall back to a default value.

### Run conditions and Execution

To specify run conditions such as environment, tags, and versions for a feature
that is resolved through an expression,
you can use the feature function and pass in the expression as an argument.

```
from chalk.features import Primary, features, feature

@features
class User:
    id: int

    purchases: DataFrame[Purchase]
    # Uses a default value of 0 when one cannot be computed.
    num_purchases: int = feature(
        expression=_.purchases.count(),
        default=0,
        environment=["staging", "dev"],
        tags=["fraud", "credit"],
        version=1,
    )
```

You may also want to define expressions that are only meant to be used for the offline pathway, say
if you would like to compute values or aggregations dependent on offline resolvers. To do so, you can
specify a distinct offline_expression as an offline resolver for your feature.

```
from chalk.features import features, feature 

@features 
class Merchant: 
    id: int 
    
    transactions: DataFrame[Transaction]

    merchant_risk_score: float = feature(
        expression=_.transactions[_.status=="approved"].count() / _.transactions.count(),
        offline_expression=(0.50*_.transactions[_.is_chargeback==True].count()+0.25*_.transactions[_.is_refund==True].count()+0.25*_.transactions[_.status=="approved"].count())/_.transactions.count()
    )
```

### Testing

To test your expressions, we recommend setting up integration tests or
iterating on a branch.

### Dynamic Expressions

In some cases, you may want to build expressions dynamically.
For example, if you have a rules engine that generates expressions
and stores them in a database, you can load those expressions at runtime
and ask Chalk to compute their values.

Consider this User and Transaction model, which would be checked in to the code:

```
from chalk.features import features, DataFrame

@features
class 
Transaction:
    id: int
    user_id: "User.id"
    user: "User"
    total: float
    sales_tax: float

@features
class User:
    id: int
    transactions: DataFrame[Transaction]
    name: str
    email: str
```

Using the Golang
or Python
SDKs, you can compute both scalar and aggregate features on demand.

For example, in Golang, if we wanted to compare the lowercased name and email
by their Jaccard similarity, we could build the expression dynamically and ask
Chalk to compute it:

```
package main

import (
	"testing"
	"github.com/zeebo/assert"
	"github.com/chalk-ai/chalk-go/expr"
	"github.com/chalk-ai/chalk-go"
)

func TestQueryingExpressions(t *testing.T) {
	// Picks up the ambient credentials from the `chalk login` run on the CLI.
	client, err := chalk.NewGRPCClient(t.Context())
	assert.NoError(t, err)
	result, err := client.OnlineQueryBulk(
		t.Context(),
		chalk.OnlineQueryParams{}.
			WithInput("user.id", []int{1}).
			WithOutputs("user.name").
			WithOutputs("user.email").
			WithOutputExprs(
				expr.FunctionCall(
					"jaccard_similarity",
					expr.FunctionCall("lower", expr.Col("name")),
					expr.FunctionCall("lower", expr.Col("email")),
				).
					As("user.name_email_sim"),
			),
	)
	assert.NoError(t, err)
	row, err := result.GetRow(0)
	assert.NoError(t, err)
	for feature, value := range row.Features {
		t.Logf("Feature: %s, Value: %+v", feature, value.Value)
	}
}
```

This program produces output like this:

```
=== RUN   TestChalkClient
    chalk_test.go:46: Feature: user.name, Value: Nicole Mann
    chalk_test.go:46: Feature: user.email, Value: nicoleam@nasa.gov
    chalk_test.go:46: Feature: user.name_email_sim, Value: 0.5714285714285714
--- PASS: TestChalkClient (0.43s)
```

The feature user.name_email_sim was computed using the expression
jaccard_similarity(lower(name), lower(email)), which was built dynamically
using the expr package.

For a complete list of functions, see our SDK docs.
All the functions available in expressions are also available in the expr package.

You can also compute aggregations dynamically.
Using the Golang SDK, we can compute the number of large transactions for a user:

```
result, err := client.OnlineQueryBulk(
    t.Context(),
    chalk.OnlineQueryParams{}.
        WithInput("user.id", []int{1}).
        WithOutputExprs(
            expr.DataFrame("transactions").
                Filter(expr.Col("amount").Gt(expr.Float(0.))).
                Agg("count").
                As("user.positive_transaction_count"),
        ),
)
```

For this program, the output would look like this:

```
=== RUN   TestChalkClient
    chalk_test.go:42: Feature: user.positive_transaction_count, Value: 33
--- PASS: TestChalkClient (0.45s)
```

In a Python expression, the above SDK call is equivalent to:

```
User.positive_transaction_count = _.transactions[_.amount > 0].count()
```

Both the scalar functions and aggregations can be computed in Python SDK.
See this guide for more details.

# Python Resolvers
source: https://docs.chalk.ai/docs/python-resolvers

## Specify dependencies and results of feature resolvers.

Python resolvers are Python functions marked with either an @online or @offline decorator,
with Python type annotations
declaring the dependencies on other features, as well as the output feature(s).

### Inputs

### Scalar dependencies

To depend on features from a feature class,
label your resolver arguments with your features as the types.
You can then use those arguments in the body of your resolver to
compute your output features.
If you're running our editor plugin,
your editor will see the type of each variable as the type
of the underlying scalar.

```
from chalk.features import features, online

@features
class User:
    id: str
    email: str
    email_domain: str

@online
def get_domain(email: User.email) -> User.email_domain:
    # type(email) == str
    return email.split('@')[1].lower()
```

You can require multiple features in a resolver.
However, all feature dependencies in a single resolver
need to originate in the same root namespace:

Requiring features from the same root namespace

```
@online
def get_name_sim(a: User.email, b: User.name) -> User.email_name_match:
    return len(set(a) & set(b)) / len(set(a) | set(b))
```

Here, we incorrectly request features from the root namespaces
of Transfer and User:

Requiring features from different root namespaces

```
@online
def txn_email_sim(
    email: User.email,
    memo: Transfer.memo,
) -> Transfer.email_in_memo:
    return email in memo
```

If you want to require features from namespaces,
you can use has-one or
has-many relationships.

Requiring features from different root namespaces using a relationship

```
@online
def txn_email_sim(
    email: Transfer.user.email,
    memo: Transfer.memo,
) -> Transfer.email_in_memo:
    return email in memo
```

### Has-one dependencies

### Scalar has-one

You can also require features joined to a
feature class through
has-one relationships.
For example, if users in your system have bank accounts,
and you wanted to compare the name on the user's bank account
to the user's name, you could require the user's name and
the account's title through the user:

```
@online
def name_sim(title: User.account.title, name: User.full_name) -> User.name_sim:
    return len(set(title) & set(name)) / len(set(title) | set(name))
```

You can also require all scalars on the user:

```
from chalk import online, Now

@online
def get_txn_name_match(
    memo: Transaction.memo,
    user: Transaction.user,
) -> User.profile.age:
    return (
        len(set(memo) & set(user.full_name)) /
        len(set(memo) | set(user.full_name)
    )
```

Chalk will materialize all scalar features on the user
before calling this function.
If you want to pull only a few features of the user,
require each directly:

```
@online
def get_txn_name_match(
    memo: Transaction.memo,
    full_name: Transaction.user.full_name,
) -> User.profile.age:
    return (
        len(set(memo) & set(full_name)) /
        len(set(memo) | set(full_name)
    )
```

### Optional has-one

Has-one relationships can also be
declared as optional.
You may also require feature through optional relationships,
but the types for all of those optional features will become
optional. Consider the below example:

```
from chalk.features import features, online

@features
class Account:
    id: int
    user_id: "User.id"
    balance: float  # Non-optional balance

@features
class User:
    id: int
    account: Account | None
    has_high_balance: bool

@online
def has_high_bal(balance: User.account.balance) -> User.has_high_balance:
    # Balance will be "float | None", because User.account is optional
    if balance is None:
        return False
    return balance > 1000
```

The resolver in this example receives an optional float,
even though balance is not an optional field on Account.
The optional is added because the user may not have an account,
in which case the resolver will receive None for the balance.

### Nested has-one

You can also traverse nested has-one
relationships in the same manner as
requiring a single has-one.

Consider a schema where users have a feature class of profile information,
and the user's profile has an identity feature class, which in turn
has the age of the user's email.
You can require the email age feature as below:

```
@online
def email_score(
    email_age: User.profile.identity.email_age
) -> User.email_score:
    return (
        1 if email_age < 30 else
        0.5 if email_age < 60 else
        0
    )
```

However, you cannot access nested relationships without
explicit asking for them.

Accessing a transitive relationship from a dependency.

```
@online
def fn(acct: User.account) -> ...:
    acct.balance           # Ok
    acct.institution.name  # Error!
```

Instead, you can require the nested relationship directly
and access any of its scalar features.

Directly requiring the transitive relationship.

```
@online
def fn(ins: User.account.institution, acct: User.account) -> ...:
    acct.balance  # Ok
    ins.name      # Ok
```

The semantics of
optional has-one dependencies
carry over to nested has-one dependencies.
If you traverse an optional relationship,
then all downstream attributes will become optional.

### Has-many dependencies

### Scalar has-many

You can also require has-many relationships
as inputs to your resolver:

```
@online
def txn_count(transfers: User.transfers) -> User.count_transfers:
    return len(transfers)
```

You receive a Chalk DataFrame,
which supports
projections,
filtering, and
aggregations,
among other operations.

### Projections

By default, Chalk will materialize all scalar features
on the Transfer feature class before calling your resolver.
As an optimization hint, you can specify which features from
the transfers that you'd like Chalk to materialize before calling
the function. For example, if there were expensive features
to compute on the transfer, you could scope the features
to only the set you need:

```
@online
def fn(transfers: User.transfers[Transfer.amount, Transfer.memo]) -> ...:
    transfers[Transfer.amount].sum()      # Ok
    transfers[Transfer.from_institution]  # Error: filtered out above
```

The error above is surfaced statically
by our editor plugin.

### Filtering

You can apply filters to the has-many inputs of resolvers:

```
@online
def fn(transfers: User.transfers[Transfer.amount > 100]) -> ...:
```

Filters can be composed with
projections following the semantics
of the Chalk DataFrame.

```
@online
def fn(transfers: User.transfers[Transfer.amount > 100, Transfer.memo]) -> ...:
```

Filters can also be used on features through has-one relationships.

```
@online
def fn(transfers: User.transfers[Transfer.amount, Transfer.bank.location == "USA"]) -> ...:
```

More on projection and filtering here

### Has-many through has-one

Has-many relationships can be required through has-one relationships:

```
@online
def fn(transfers: User.account.transfers) -> ...:
```

As with scalar has-many dependencies,
you can scope down the scalar features on the transfer
to only those required:

```
@online
def fn(transfers: User.account.transfers[Transfer.amount]) -> ...:
    transfers[Transfer.amount].sum()      # Ok
    transfers[Transfer.from_institution]  # Error: filtered out above
```

### Has-many through optional-has-one

If the has-one relationship that you're traversing is
optional,
then the transfers argument in the example above will
either be None or a Chalk DataFrame.

### Has-one through has-many

You can also select columns through nested has-one relationships that would not normally materialize.

```
@online
def fn(transfers: User.transfers[Transfer.amount, Transfer.bank.name]) -> ...:
```

In the above example, if there was a has-one relationship between Transfer and Bank,
we can fetch any scalar feature from Bank as well for the DataFrame.
Note that the Bank.name column would not materialize with the simple transfers: User.transfers typing,
since this typing only materializes scalar features in the root namespace.

### Has-many through has-many

Has-many relationships can be required through other has-many relationships.

For example, consider the following feature definitions for User, Account, and Transaction,
where a user can have many accounts, each with many transactions.

```
from chalk.features import features, has_many, DataFrame

@features
class Transaction:
    id: str
    account_id: "Account.id"
    amount: float

@features
class Account:
    id: str
    user_id: "User.id"
    transactions: DataFrame[Transaction]

@features
class User:
    id: str
    total_spent: float
    accounts: DataFrame[Account]
```

We can resolve the total_spent feature on User by computing the sum of transaction
amounts across all of a user's accounts, as shown below.

```
@online
def get_total_spent(
    txns: User.accounts.transactions[Transaction.amount]
) -> User.total_spent:
    return txns.sum()
```

### Time dependencies

To set a time-based dependency in your resolver, you can use the Now keyword. Resolvers with a dependency on Now
can use the input times passed in at query-time to compute either scalar or DataFrame outputs.

```
from chalk import online, DataFrame, Now
from chalk.features import features
from datetime import datetime

@features
class Account:
    id: str
    balance: float
    updated: datetime

@online
def get_daily_balance(now: Now) -> DataFrame[Account]:
    return DataFrame([
        Account(id="1", balance=100, updated=now),
        Account(id="2", balance=200, updated=now),
    ])
```

Read more about time-based dependencies here.

### Outputs

Python resolvers can output either scalar features or a DataFrame of features.

### Scalar output

### Single output

To return a single feature from a resolver,
set the return type annotation to the feature you
want to resolve:

```
from chalk.features import features

@features
class User:
    id: int
    name: str
    employer: str

@online
def resolve(u: User.id) -> User.name:
    return "Jennifer Doudna"
```

Equivalently, you can wrap the return value in the User class:

```
@online
def resolve(u: User.id) -> User.name:
-   return "Jennifer Doudna"
+   return User(name="Jennifer Doudna")
```

### Multiple outputs

To return multiple features, return an
instance of the feature class.
In the type signature, specify
the Features[...] class, parameterized
by the features that you pass to the feature class.

```
@online
def resolve(u: User.id) -> Features[User.name, User.employer]:
    return User(
        name="Jennifer Doudna",
        employer="University of California, Berkeley"
    )
```

You only need to pass
a subset of the features
to the constructor for the feature class.

The editor plugin will check
that the type annotation you assign to the resolver
matches subset of features passed to the constructor
of the feature class.

### All features

To return all features of a class,
use Features[...] around the feature class.

```
@online
def get_user(u: User.id) -> Features[User]:
    return User(
        name="Jennifer Doudna",
        employer="University of California, Berkeley"
    )
```

If your resolver takes input features, those features are not
considered as part of the output features.

Note that the id feature is not returned from the function.

This definition is equivalent to:

```
@online
- def get_user(u: User.id) -> Features[User]:
+ def get_user(u: User.id) -> Features[User.name, User.employer]:
    return User(
        name="Jennifer Doudna",
        employer="University of California, Berkeley"
    )
```

However, you may want to return almost all features of a class.
Writing out all the features can be tedious and error-prone.
You can subtract features from a feature class
using the - operator:

```
from chalk.features import Features, ...

@online
def get_all_users(id: User.id) -> Features[User] - User.name:
    return User(employer="University of California, Berkeley")
```

Here, both the id feature and the name feature are not returned,
which leaves only the employer feature.

### DataFrame output

You can also output many instances of a feature class from a resolver
by specifying a DataFrame as the return type of
the function:

```
@offline
def get_events() -> DataFrame[Transfer.uuid, Transfer.amount, Transfer.ts]:
    return DataFrame.read_csv(...)
```

Say you wanted to return many instances of a feature class, including nested features,
from a resolver, then you can the DataFrame class for your return type and in your
resolver definition.

```
@online
def get_user_employer_information(id: User.id) -> DataFrame[
    User.id,
    User.name,
    User.employer.name,
    User.employer.category
]:
    return DataFrame([
        User(
            id="1",
            name="Jennifer Doudna",
            employer=Employer(
                name="University of California, Berkeley",
                category="Education"
            )
        )
    ])
```

For more info on how to load batch data,
see the Data Sources sections.
DataFrame-returning resolvers don't need inputs.

### All features

To return all features of a class in a DataFrame,
use DataFrame[...] class around the feature class:

```
@online
def get_all_users() -> DataFrame[User]:
    return DataFrame([
        User(
            name="Jennifer Doudna",
            employer="University of California, Berkeley"
        )
    ])
```

### Other DataFrame-returning resolvers

Imagine a scalar feature you'd like to backfill over many thousands of primary keys and historical
times. DataFrame-returning resolvers can dramatically reduce the computation time due to its
vectorized handling.

```
@offline
def get_new_feature_as_dataframe(
    df: DataFrame[Transaction.id, Transaction.amount]
) -> DataFrame[Transaction.id, Transaction.is_large]:
    return df.with_column(...)
```

The above resolver runs faster on a thousand rows
than the equivalent scalar resolver ran a thousand times.

Chalk also supports relationship-returning resolvers that enable users to
return a DataFrame belonging to a has-many relationship.

```
@offline
def relationship_returning_resolver(
    df: User.transactions[Transaction.id, Transaction.amount, Transaction.description],
    user_type: User.type
) -> User.transactions[Transaction.id, Transaction.transaction_type]:
    return ...
```

Just make sure that the return DataFrames do not have duplicate rows.
That means no two rows should have the same primary key, or primary key & timestamp combinations if the
feature time is also returned.

### Testing

To test your Python resolvers, you can set up unit tests, construct
integration tests or iterate on a branch.

### Examples

### ML Flow

Python resolvers can also be used to load and run ML models. An example using ML Flow is shown below.
This example loads a model from the ML Flow registry and uses it to make predictions. Using the @before_all
decorator, the model is loaded once before any online requests are made. The model is then used in the
get_prediction function to make predictions based on the input features.

```
import mlflow
from chalk import online
from chalk.features import before_all

from src.models import FeatureClass
import ExampleModelClass

model: ExampleModelClass | None = None

@before_all
def load_model():
    mlflow.set_registry_uri("EXAMPLE_REGISTRY_URI")
    mlflow.set_tracking_uri("EXAMPLE_TRACKING_URI")

    global model
    model = mlflow.load_model("models:/mymodel@production")

@online
def get_prediction(
  model_input: FeatureClass.model_input,
) -> FeatureClass.model_output:
    x_in = [model_input]
    return model.predict(x_in)
```

# Environments
source: https://docs.chalk.ai/docs/resolver-environments

## Change resolver behavior by deployment.

Environments are used to trigger behavior in different deployments
such as staging, production, and local development.
For example, you may wish to interact with a vendor via an API call
in the production environment, and opt to return a constant value
in a staging environment.

### Specifying environments

You can choose to scope resolvers to a restricted set of environments.
Resolvers optionally take a keyword argument named environment
that can take one of three types:

- Unassigned (default) - The resolver will be a candidate to run in every environment.
- String value - The resolver will run only in this environment.
- List of strings - The resolver will run in any of the specified environments and no other environments.

### Example

Say your fraud models needed to interact with a fraud vendor that you wanted
to mock out in staging. We can scope the environments as follows:

```
@online(environment="**production**")
def fraud_score_prod(email: User.email, phone: User.phone) -> User.fraud_score:
    return api_vendor.fraud_score(email)

@online(environment=["**staging**", "**dev**"])
def fraud_score_staging(email: User.email) -> User.fraud_score:
    if email == "fraud_user@chalk.ai":
        return 10
    return 90
```

Resolvers in different environments don't need to take the same arguments.
In the above example, the production version of the resolver takes a phone
number and an email, while the staging version of the resolver takes only
the email.

# Tags
source: https://docs.chalk.ai/docs/resolver-tags

## Change resolver behavior within an environment.

Tags allow you to scope requests within an environment.
Both tags and environment need to match for a resolver to
be a candidate to execute.

You might consider using tags, for example, to change out
whether you want to use a sandbox environment for a vendor,
or to bypass the vendor and return constant values in a
staging environment.

### Specifying tags

Tags can be either a string value, or a key-value pair.
As a best practice
(and fitting with recommendations from other services like
Datadog),
we recommend using key-value pairs, but the choice is yours.

There are two ways to specify tags on resolvers:

- "key" -
As a single scalar string.
- "key:value" -
As a string value representing a key-value pair.

### Python resolver tags

Resolvers take one or many tags, all of which need to match for the
resolver to run. For example, you may want to test with
a sandboxed vendor, and also be able to set a constant value
for a particular feature.

```
@online(tags=["**api:mock**", "**fraud**"])
def simulate_fraud(id: User.id) -> User.fraud_score:
    return 100

@online(tags="**api:mock**")
def simulate_no_fraud(id: User.id) -> User.fraud_score:
    return 10

@online(tags="**api:sandbox**")
def sandbox_score(
    name: User.name,
    email: User.email,
) -> User.fraud_score:
    return sandbox.fraud_score(name, email).score

@online
def real_score(
    name: User.name,
    email: User.email,
) -> Features[User.fraud_score, User.fraud_tags]:
    r = prod.fraud_score(name, email).score
    return User(fraud_score=r.score, fraud_tags=r.tags)
```

In the above example, the resolver that is chosen to compute
the User.fraud_score feature will depend on the tags provided
at query time. The table below shows which resolver will be
chosen for a given set of tags.

| Query tags                                                              | Resolver                                                             |
| ----------------------------------------------------------------------- | -------------------------------------------------------------------- |
|  [api:mock, fraud]  |  simulate_fraud     |
|  api:mock           |  simulate_no_fraud  |
|  api:sandbox        |  sandbox_score      |
|  <otherwise>        |  real_score         |

Note that these resolvers don't need to take the same set of inputs,
and don't need to return the same types.

### SQL resolver tags

SQL resolvers can also specify flags via the tags comment.
For example, if you wanted to use Snowflake for User features
in a fraud context and use Redshift for the same features in a signup
context, you could write two different SQL file resolvers with different tags:

```
-- type: offline
-- resolves: User
-- source: snowflake
-- tags: ["fraud"]
select id, name, fraud_status from users
```

```
-- type: offline
-- resolves: User
-- source: redshift
-- tags: ["signup"]
select id, name, fraud_status from users
```

### When tagged resolvers run

Like Environments, tags control when resolvers run
based on the
Online Context or Training Context
matching the tags provided to the resolver decorator.
Resolvers optionally take a keyword argument named tags
that can take one of three types:

- Unassigned (default) - The resolver will be a candidate to run for every set of tags.
- String value - The resolver will run only if this tag is provided.
- List of strings - The resolver will run only if all the specified tags match.

If your resolver is tagged only by a key (not a key-value pair),
and the request context contains a key-value pair such that the resolver's
tag (a key only) matches they key of a key-value pair in the context,
the resolver will be eligible to run. For example:

| Resolver Tag                                                                 | Request Context                                                           | Matches? |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------- | -------- |
|  api                     |  api                     | Yes      |
|  api                     |  api:live                | Yes      |
|  [api:live, mock-phone]  |  [api:live, mock-phone]  | Yes      |
|  [api:live, mock-phone]  |  api:live                | No       |
|  api:live                |  api                     | No       |
|  api:fixture             |  api:live                | No       |

### Example

Frequently, you'll want to combine tags and Environments,
as below.
This span uses a constant value in staging when the tag api takes the value fixture,
uses the sandboxed fraud vendor in staging when the tag api takes the value live,
and uses the production fraud vendor in production.

```
@online(environment="staging", tags="**api:fixture**")
def fraud_score_fixture(email: UserFeatures.email) -> UserFeatures.fraud_score:
    if email == "elliot@chalk.ai":
        return 100
    return 50

@online(environment="staging", tags="**api:live**")
def fraud_score_sandbox(email: UserFeatures.email) -> UserFeatures.fraud_score:
    return api_vendor_sandbox.fraud_score(email, profile="dev")

@online(environment="production")
def fraud_score_prod(email: UserFeatures.email) -> UserFeatures.fraud_score:
    return api_vendor_live.fraud_score(email)
```

# Errors
source: https://docs.chalk.ai/docs/resolver-errors

## Surface and handle failed feature values.

Resolvers can raise errors in the course of executing,
and handle errors in resolving other feature values.

### Raising errors

If your resolver fails by raising an exception,
the error will be surfaced as a
ChalkError
in query responses.
Clients will receive a null value for the feature,
and by default,
downstream resolvers won't run.

### Handling errors

By default, if there was an error in computing one of the inputs
to a resolver, that resolver will also fail with the error code
UPSTREAM_FAILED.
To handle failures in the input features, take as input the feature
value, but wrapped in typing.Optional:

```
from typing import Optional

@online
def fn(score: Optional[User.fraud_score]) -> ...:
```

The argument score will receive the value None in the case of a failure.

If you'd like to provide a default value to use in the case of a failure, you can use Python's syntax for assigning
a default value to an argument:

```
@online
def fn(score: Optional[User.fraud_score] = -1) -> ...:
```

# Scheduling
source: https://docs.chalk.ai/docs/resolver-cron

## Automate resolver runs.

You can schedule resolvers to run on a pre-determined schedule
via the cron argument to resolver decorators.

```
@online(cron="**90d**")
def fn() -> DataFrame[User.id, User.name]:
    return ...
```

The cron keyword arguments takes a duration
to determine the schedule on which to run.  For more fine-grained control,
you can alternatively specify a crontab in the UTC timezone.

```
@online(cron="***/5 * * * ***")
def region_average(
    houses: DataFrame[
        House.city, House.rent_price
    ]
) -> DataFrame[Region.name, Region.average_price]:
    return houses.group_by(
        group={Region.name: House.city},
        agg={
            Region.average_price: op.mean(House.rent_price),
        },
    )
```

In SQL resolvers you can also use the cron keyword in the comments.

```
-- type: offline
-- resolves: user_seller_features
-- source: snowflake
-- owner: disco
-- tags: ["team:discoml","type:simulated"]
-- cron: "0 0 * * *"
```

### Scheduling with arguments

Scheduled resolvers can also take arguments.
Chalk gives you control over which arguments should be
provided for each run of the schedule.

### All examples (default)

Chalk calls the resolver with
all unique argument names that could have called the function.
Consider a scheduled resolver that takes in
Feature 1 and Feature 2:

In this example, we compute two points to sample:
(1, 5) and (1, 7). These two values will be given
to the resolver on the specified cron schedule.

### Filtering examples

You can choose to filter down the set of all examples to run.
The cron keyword argument alternatively takes a Cron class.
By specifying a function from features to boolean,
you can tell Chalk which of the default examples
to run, and which to skip:

```
def filter_examples(bank_id: User.bank_account.balance) -> bool:
    return balance > 100

@online(cron=Cron(schedule="1d", filter=filter_examples))
def fn(balance: User.bank_account.balance) -> ...:
```

The arguments to the filter function all need to be rooted in the
same entity as the features in the scheduled resolver,
but there is no requirement that the filter function take a subset
of the scheduled resolver's arguments:

```
def filter_examples(status: User.bank_account.status) -> bool:
    return status == "opened"

@online(cron=Cron(schedule="1d", filter=filter_examples))
def fn(balance: User.bank_account.balance) -> ...:
```

### Custom examples

Finally, you can pick exactly the examples that you'd like to run.

```
def pull_examples() -> DataFrame[User.id]:
    return DataFrame.read_csv(...)

@online(cron=Cron(schedule="1d", samples=pull_examples))
def fn(uid: User.id) -> ...:
```

In the above example, we provide all arguments to the resolver function.
However, you may also choose to provide only a subset of the arguments,
and Chalk will sample the other arguments.

```
def pull_examples() -> DataFrame[User.id]:
    return DataFrame.read_csv(...)

@online(cron=Cron(schedule="1d", samples=pull_examples))
def fn(uid: User.id, balance: User.account.balance) -> ...:
```

# Reverse ETL
source: https://docs.chalk.ai/docs/reverse-etl

## Move data from offline to online.

Reverse ETL is the process of moving data from a data warehouse into
operational systems. In the context of
Chalk's architecture,
our data warehouse is the offline data store
(Timescale or BigQuery)
and our operational system is the online data store
(Redis, Cloud Memorystore, or DynamoDB).
Chalk's API client can be used to query the online data store and the offline data store.
one our API clients,
while the offline data store can be queried by
our bulk API.

Data from online resolvers is always loaded into the offline store
and made available for training.
In contrast,
data from offline resolvers is not loaded into online stores by default.
To enable offline data to reach the online environment,
use the keyword argument etl_offline_to_online on the feature you wish to ETL.

```
from chalk.features import features, feature, offline
from chalk import DataFrame

@features
class User:
    ...
    favorite_color: str = feature(etl_offline_to_online=True)

@offline
def fn(...) -> DataFrame[User.favorite_color, ...]:
    ...
```

When this argument is present in the feature declaration,
Chalk copies this feature into the online environment.

Reverse ETL can also be assigned to all features in a namespace:

```
from chalk.features import features, feature

@features(etl_offline_to_online=True)
class User:
    fraud_score: float
    full_name: str
    email: str = feature(etl_offline_to_online=False)
    ...
```

Here, User.fraud_score and User.full_name
will be reverse ETL'd into the online environment.
However, User.email, which specifies the ETL parameter at the feature level,
will not be reverse ETL'd.

### Interplay with max staleness

When data from an offline store reaches an online store,
it is necessarily somewhat stale.
The data may have come from an events table,
where it could be arbitrarily old,
or it could be a snapshot that was live when the
snapshot was taken, but takes non-zero time to
migrate online.
Therefore, you will only receive offline data
from queries in the online environment when you
your queries tolerate
maximum staleness via features
or maximum staleness via queries.

# Triggered Runs
source: https://docs.chalk.ai/docs/runs

## Execute resolver runs via API

In addition to scheduling resolver executions,
Chalk allows you to trigger resolver executions programmatically via the Chalk Client, CLI and REST API.

### Trigger a Run via Chalk Client

Using the Chalk Client, you can trigger a resolver run using the trigger_resolver_run command.

```
from chalk.client import ChalkClient

ChalkClient().trigger_resolver_run(resolver_fqn="load_user_data", store_online=True)
```

To read more about how to specify parameters like upper_bound, lower_bound, store_online, store_offline,
and idempotency_key, check out our API documentation.

### Trigger a Run via CLI

The chalk trigger command allows you to trigger a resolver execution via the CLI.

```
$ chalk trigger --resolver my.module.fn
ID:     j-2qtwuxpskm2pbg
Status: Received
URL:    https://chalk.ai/runs/j-2qtwuxpskm2pbg
```

To read more about how to specify flags like deployment, persist-online, persist-offline, and
idempotency-key, check out our CLI documentation.

### Trigger a Run via API

Using the trigger API endpoint allows you to build custom integrations with other
data orchestration tools like Airflow.

The trigger endpoint will return within 300 seconds, even if the
triggered run takes longer to execute. If the returned status is received,
you should poll the v1/runs/{id} endpoint until status transitions to succeeded or failed.

It is also possible to manually trigger resolver executions via the Chalk dashboard, on the
details page for the resolver you would like to run. The same input parameters are available in the dashboard.

Note: if you use a user-scoped token (i.e. one that's derived from chalk login) you will need to
specify the environment in which to trigger your resolver via the X-Chalk-Env-id header.

### Trigger a run

The fully qualified name of the resolver to trigger. Example: 'neobank.resolvers.offline_get_transactions'.

The lower bound timestamp to use when sampling input features to run this resolver on. Example: '2021-01-01T00:00:00Z'.

The upper bound

The maximum number of samples to pull from the offline store when running this resolver. Example: 1000.

### Response

ID of the relevant run.

One of 'received', 'succeeded', or 'failed'

### Example

```
curl -XPOST -H "Authorization: Bearer $(chalk token)" \
     -H "X-Chalk-Env-Id: <your-environment-id>" \
     -H "Content-Type: application/json" \
     https://api.chalk.ai/v1/runs/trigger \
     -d '{ "resolver_fqn": "neobank.resolvers.offline_get_transactions" }'

# Returns

{
  "id": "<run-id>",
  "status": "succeeded"
}
```

### Query run status

URL Param. ID of the relevant run.

### Response

ID of the relevant run.

One of 'received', 'succeeded', or 'failed'

### Example

```
curl -H "Authorization: Bearer $(chalk token)" \
     -H "X-Chalk-Env-Id: <your-environment-id>" \
     https://api.chalk.ai/v1/runs/{run_id}
```

# Timeout
source: https://docs.chalk.ai/docs/timeout

## Maximum execution time for resolvers

Computing features associated with third-party services can be unpredictably slow.
Chalk helps you manage such uncertainty by specifying a resolver timeout duration.

Chalk will instantaneously (±1ms) cease waiting for a resolver whose
runtime has exceeded the specified timeout duration. Simultaneously,
via parallel execution, Chalk will return other crucial features whose
resolvers did not time out.

To specify a timeout, use the timeout keyword argument to either
@online or @offline:

### Example

```
from chalk.features import online, offline

@online(timeout="200ms")
def resolve_australian_credit_score(
    driver_id: User.driver_id_aus,
) -> User.credit_score_aus:
    return experian_client.get_score(driver_id)

@offline(timeout=timedelta(milliseconds=50))
def resolve_canadian_credit_score(
    user_si_number: User.social_insurance_number,
) -> User.credit_score_can:
    return equifax_client.get_score(user_si_number)
```

See Duration for supported durations.

### Behavior upon timeout

### Direct timeout

If a query's output feature is directly resolved by a resolver that
timed out, Chalk will return an error with the error code RESOLVER_TIMED_OUT,
and its message will contain the name of the timed-out resolver.

### Upstream timeout

If a query's output feature is resolved by a resolver whose upstream
resolver has timed out, Chalk will return an error with the error
code UPSTREAM_FAILED.

The resolver that directly outputs the requested feature will not be
run (unless it marks its inputs as optional).

### Multiple output features

If your query contains multiple output features, Chalk will still
return the other features whose resolver did not time out.

# Integrations Overview
source: https://docs.chalk.ai/docs/integrations

## Integrate any API, 3rd-party client or data source without needing to orchestrate data pipelines

Chalk integrates seamlessly with your underlying systems--querying your data sources directly, eliminating the need
for ETL!

This unlocks several key benefits:

- alleviates the need to move data across multiple systemssingle source of truth (define once and use everywhere)prevents data drift (same feature logic for offline and online workloads)reduces data duplication and storage costs
- optimizes compute by only ever fetching exactly what you need when you need it (dynamic query planning)
- enables real-time data delivery by satisfying strict (under 5ms) latency requirements

### Cloud Platforms

Anywhere that you can run Kubernetes, you can run Chalk--Chalk is cloud-agnostic.

Chalk deploys into your VPC co-located with your data sources for the lowest latency and cost.
Multi-cloud deployments for high availability and disaster recovery.

- AWS (Amazon Web Services)
- GCP (Google Cloud Platform)
- Azure Cloud (Microsoft)

### SQL data sources and data warehouses

Chalk has native drivers and integrations with a variety of SQL data sources and query engines, and
provide a unified interface for adding new data sources.
Adding a new SQL source is as simple as providing a connection string and a few configuration options through your
Chalk dashboard.
Once it's been added to your Chalk deployment, you can start querying it right away with SQL Resolvers.

```
-- resolves: User
-- source: postgres
select
    id,
    name,
from users
```

The features in a feature class can be hydrated from multiple SQL sources--we can pull a user's social security number
from a different database that has stricter access controls.

```
-- resolves: User
-- source: restricted_postgres
select
    id,
    ssn
from sensitive_user_data
```

In addition, Chalk can reverse ETL features from your data warehouses into Chalk's online store for low-latency access.
Chalk integrates natively (C++ integration) with the following data sources and pushes down filters and projections
into SQL queries for more efficient data fetching.

Data Warehouses

- Snowflake
- Databricks

Native:

- MySQL
- PostgreSQL
- Clickhouse
- Presto / Trino
- DuckDB

AWS:

- Redshift
- Athena
- DynamoDB

GCP:

- BigQuery
- Spanner
- Alloy

Azure:

- Microsoft SQL Server (MSSQL) / Azure SQL Database
- Database for PostgreSQL
- Database for MySQL

### Streaming / Real-Time Data Systems

We provide stream resolvers for integrating Kafka compatible systems data sources.

- Kafka compatibleConfluentRedpanda
- Kinesis (AWS)
- Pub/Sub (GCP)
- Event Hubs (Azure)

Streams can also be filtered, processed, and materialized as a step in Chalk's feature computation pipelines.

```
@stream(source=KafkaSource(name='transactions_stream'))
def process_transaction_topic(
    value: TransactionMsg,
) -> Features[Transaction.id, Transaction.user_id, Transaction.amount]:
    return Transaction(
        id=value.id,
        user_id=value.user_id,
        amount=value.amount,
    )
```

### Feature caching with expensive features with Redis/Valkey, Memcached, DynamoDB, and more

Chalk makes it easy to cache features for low-latency access with the max_staleness keyword
argument. These features skip expensive API calls and are fetched from the online store.

```
@feature
class User:
    id: int
    name: str
    ssn: int
    credit_score: int = feature(max_staleness="30d")
```

We support a variety of caching backends:

- Redis / Valkey
- Memcached
- DynamoDB
- Amazon ElastiCache
- Google Cloud Memorystore
- Azure Cache for Redis
- Azure Cosmos DB

### APIs & Microservices

Call internal APIs, third-party services, and microservices with built-in retry logic and circuit breakers:

```
@online
def get_credit_score(ssn: User.ssn) -> User.credit_score:
    response = requests.get(
        f"https://api.creditbureau.com/score/{ssn}",
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=2.0
    )
    return response.json()["score"]
```

Chalk's Symbolic Python Interpreter supports accelerating libraries like requests,
and so this function gets run in C++.

### Object Storage and Iceberg Catalogs

AWS (Amazon Web Services)

- S3 (Amazon Simple Storage Service)
- Glue Catalog

GCP (Google Cloud)

- Google Cloud Storage
- Cloud Data Catalog
- BigLake

Microsoft

- Azure Blob Storage
- Microsoft Purview
- Azure Data Lake

Chalk is Iceberg native and can write to your underlying object storage and catalog directly from offline queries.

```
from chalk.integrations import GlueCatalog

catalog = GlueCatalog(
    name="aws_glue_catalog",
    aws_region="us-west-2",
    catalog_id="123",
    aws_role_arn="arn:aws:iam::123456789012:role/YourCatalogueAccessRole",
)
results.write_to(destination="database.table_name", catalog=catalog)
```

### AI & ML Services

Access traditional machine learning functions like Scikit, XGBoost, and your own models directly within feature definitions using Chalk Expressions:

- Sci-kit functions
- ONNX Models (Open Neural Network Exchange) through Chalk's model registry

Integrating unstructured data with LLMS (large language models) or computing embeddings is straightforward with Chalk's built-in integrations.
Easily conduct Evals, switch out different models and providers, and reference the features you need in your prompts without having to configure complex pipelines.

- OpenAI
- Anthropic
- AWS Bedrock
- Azure OpenAI
- Google Vertex
- Any OpenAI compatible chat completion modelCerebrasGroqOllama CloudTogether.ai

You can override the base url and API key to connect to any OpenAI compatible endpoint.

```
@features
class Item:
    id: int
    title: str
    description: str
    llm: P.PromptResponse = P.completion(
        model="gpt-5.1-2025-11-13",
        messages=[
            P.message(
                role="user",
                content=F.jinja(
                    """
                    Classify the following item category using its title and description:
                    Item title: {{ Item.title }}
                    Item description: {{ Item.description }}
                    """,
                ),
            ),
        ],
        output_structure=StructuredOutput,
    )
```

You can just as easily compute embeddings for items, users, or any other entity using built-in integrations:

```
@features
class VectorSearch:
    q: Primary[str]
    # from chalk.features import embed
    vector: Vector = embed(
        input=lambda: VectorSearch.q,
        provider="vertexai",
        model="text-embedding-005",
    )
    query_type: str = "vector"

    results: "DataFrame[ItemDocument]"
```

### Get started today

With dozens of native integrations across cloud platforms, databases, streaming systems, caching layers, and AI services,
Chalk eliminates the complexity of building and maintaining production machine learning systems.

Whether you're pulling user data from PostgreSQL, processing real-time events from Kafka, caching expensive feature
computations in Redis, or extracting features from unstructured data with LLM's-—Chalk's unified platform handles it all.

The result? Faster time to production, lower operational overhead, and consistent feature logic across your
entire ML stack.

# Docker
source: https://docs.chalk.ai/docs/docker

## Customize the base image for your pipelines.

Chalk runs your feature pipelines on Docker images.
If your code relies only on your resolvers and data source definitions, you may
use Chalk's base image with no modification. If you require additional
dependencies, you can specify installation and management instructions.

You can specify build options on a per-environment basis,
and you can provide a default set of configuration for
environments that do not have explicit configuration values.

### Extra pip dependencies

Chalk can install extra dependencies with pip.
By default, Chalk looks for a file named requirements.txt in the base
of your project.

However, you can override this location or specify requirements
files per-environment in the chalk.yaml file located at the base
of your repo.

```
project: my-project-id
environments:
  default:
    runtime: python312
    requirements: ./requirements.txt
    dockerfile: Dockerfile
  prod:
    requirements: ./requirements-prod.txt
```

### Building your own image

You may have dependencies that cannot be expressed through pip.
For those dependencies, you need to customize the base image Chalk uses
to run your pipelines.
Chalk allows you to specify a custom Dockerfile
that will be used to build a base image for your deploys.

```
project: my-project-id
environments:
  default:
    dockerfile: ./Dockerfile
  prod:
    dockerfile: ./DockerfileProd
```

You build any Debian-based
image that you like, with a few requirements:

- python must be on the path
- pip must be on the path
- The Python version can be python310, python311, or python312
- There should be no folder or file at /app

Chalk is responsible for mounting your code into
the image, and for installing your requirements with pip.

### Python Version

The Python version for a Chalk project is set at the project level.
The version is set with the chalk.yml file in your project repo.
Chalk supports both python310, python311, and python312 as values for runtime:

```
project: my-project-id
environments:
  default:
    runtime: python312
  prod:
    runtime: python311
```

# Amazon Web Services
source: https://docs.chalk.ai/docs/aws

## Setup your AWS integration

You can provide Chalk with an AWS Access Key to use AWS-specific integrations (like Redshift) and S3 Cloud Storage.

In the settings page, you'll find a form for adding your credentials:

You are encouraged to use different access keys for different environments, although they can be shared.

### Creating an access key

Access keys are created directly in the AWS console, via the AWS CLI, or via the AWS API. Make sure that the IAM user you create the access key for has access to the appropriate IAM permissions for your intended integration use case.

# S3 / Object Storage
source: https://docs.chalk.ai/docs/s3

## Integrate with S3 compatible data sources.

### Reading .csv files

Chalk parses .csv files from s3 or the local file system
with the function DataFrame.read_csv(...).

If your .csv has headers, you can tell Chalk which
columns to parse into which features by providing
a mapping in the columns keyword argument:

```
DataFrame.read_csv(
    path="s3://your-bucket/path/to/file.csv",
    columns={"uid": User.uid, "fraud score": User.socure_score},
)
```

The first line of the file is taken to be the header
row, and subsequent lines are parsed into the provided
features.

The returned value matches the type:

```
DataFrame[User.uid, User.socure_score]
```

Alternatively, you can map the file into features by
column number in the .csv, and optionally skip rows
that might contain header fields or summary stats:

```
DataFrame.read_csv(
    path="s3://your-bucket/path/to/file.csv",
    columns={0: User.uid, 1: User.socure_score},
    skip_rows=1
)
```

### Reading .parquet files

Reading .parquet files works just like reading .csv files.
As with .csv, Chalk parses .parquet files from s3 or the
local file system, this time with the function
DataFrame.read_parquet(...).
Otherwise, the functionality provided is the same as provided
above for reading .csv files.

### Authentication

Chalk can connect to AWS S3 or GCP Cloud Storage
for reading .csv and .parquet files.
Chalk will use the application credentials that you
set up in the AWS and GCP integrations sections.

# Google Cloud Platform
source: https://docs.chalk.ai/docs/gcp

You can provide Chalk with a GCP application credentials
to use integrations with GCP (like BigQuery and Cloud Storage).

On your dashboard, you'll find a form for adding your credentials:

You are encouraged to use different service accounts for different environments,
although they can be shared.

### Creating credentials

Credentials are created through GCP directly.
You'll want to make a new service key for Chalk
with the permissions you require.
Credentials are created through GCP's dashboard.
You can create a key and download it from your console
here.

### BigQuery permissions

If you plan to add a BigQuery data source to your Chalk deployment, then you should ensure
that the permissions set includes bigquery.tables.create and bigquery.jobs.create.

When querying your BigQuery data source, Chalk will push down filters on top of your
queries to optimize the amount of data read from your tables. For larger queries, rather than
interpolating values directly in the SQL string for the query, which has length limits in
BigQuery, Chalk will use a table to temporarily hold the values against which to query.

# SQL Integration
source: https://docs.chalk.ai/docs/sql

## Integrate with SQL-like sources.

Chalk can ingest data using a SQL interface from any of our supported SQL data source integrations. The full list of
supported SQL data sources can be found in our API reference.

### Basic queries

Chalk supports running SQL from files or from strings. When you run queries that invoke your SQL resolver, Chalk
automatically pushes your input parameters into the WHERE clause of your query. For more details, see our section on
push-down filters.

The examples on this page use our PostgreSQL data source, but can be generalized to any of our other
SQL data sources.

### SQL file resolvers

SQL file resolvers are Chalk's recommended method for writing SQL resolvers.

```
-- type: online
-- resolves: user
-- source: PG
select id, email, full_name from users
```

Here, we define an online resolver that returns some features for the User feature class
from the users table in the PostgreSQL source PG. The comments are yaml-parsed
to provide other metadata for Chalk to decide how to design the resolver. SQL file resolvers
can return multiple rows for aggregation operations, offline queries, and more.

It's also possible to use SELECT * in a SQL file resolver, but be careful!

```
-- type: online
-- resolves: user
-- source: PG
select * from users
```

Implicitly, this query tries to align every scalar feature from the User feature class to a column name in
users. If a feature name is misnamed or absent from the table, you'll get a "missing columns" error.

To programmatically generate SQL file resolvers, check out Generated SQL file
resolvers.

### Parameterized feature inputs

Like other resolvers, SQL file resolvers can take features as input. In this example, we want our resolver to require
EmailUser.id as input:

```
-- type: online
-- resolves: user
-- source: PG
select id, email, full_name
from users
where id = ${user.id}
```

Use ${} with snake case to reference the desired feature.

Use ${now} in your query as a special argument representing the time of the query. For more details, see our
time documentation.

### SQL strings

You can run SQL queries either as Python strings or from .sql files.

When the name of the column matches the name of the feature
with non-alphanumeric characters removed, the mapping from
column to feature is automatic.

```
pg = PostgreSQLSource(name='PG')

@online
def get_user(uid: User.id) -> Features[User.full_name, User.email]:
    return (
        pg.query_string("select full_name, email from users where id=1")
        .first()
    )
```

get_user's return type indicates that it expects features named full_name and email, which are returned as
columns from the SQL query.

If the column names don't align exactly, you can
include the parameter fields to specify the mapping from
the query to the fields.

```
pg = PostgreSQLSource(name='PG')

@online
def get_user(uid: User.id) -> Features[User.full_name, User.email]:
    return (
        pg.query_string(
            "select name, email from users where id=1",
            fields=dict(name=User.full_name),
        )
        .first()
    )
```

Here, the email column of the query automatically aligns with the
expected User.email feature, but the name column of the query
is explicitly mapped to the User.full_name feature.

### Parameterizing string queries

You can parameterize queries to pass variables.
Parameterize names with a colon,
and pass a dictionary from parameter name to parameter value:

```
pg.query_string(
    query="select * from users where user_id=**:user_id**",
    args=dict(user_id="**uid123**"),
)
```

Use a backslash to escape any literal : characters you need to use in your query:

```
pg.query_string(
    query="select * from users where user_id=**:user_id** and name=**'\:colon'**",
    args=dict(user_id="uid123"),
)
```

### SQL string files

Instead of passing a string directly into your Python code, you can load the SQL content from a file.
you can use the query_sql_file function.

For example, here is a query.sql file containing the same query from above:

```
select * from users where user_id=:user_id
```

You can reference this file in a Python resolver, either
using the absolute path from the root of your project or
relative to the resolver's file.

For example, if the snippet below lived in the same directory
as query.sql, we could refer to it as follows:

```
pg = PostgreSQLSource(name='PG')

@online
def get_user(uid: User.id) -> Features[User.full_name, User.email]:
    return (
        pg.query_sql_file(
            path="query.sql",
            args=dict(user_id=uid)
        )
        .first()
    )
```

Auto-mapping of column name to feature name also applies for
the query_sql_file method. Parameterization also works the same way.

### Push-down filtering

Chalk automatically adds query inputs to the WHERE clause of your SQL
queries. We recommend relying on our push-down filtering logic rather than
parameterizing your queries by hand.

The following example will show a transaction feature and how we use push-down
filtering to retrieve transactions belonging to a specific category.

Here's the feature class:

```
pg = PostgreSQLSource(name='PG')

@features
class Transaction:
    id: int
    category: string
    amount: float
```

And the SQL file resolver:

```
-- type: online
-- resolves: transaction
-- source: PG
SELECT
    id, merchant_category AS category, amount
FROM
    txn_table;
```

Finally, here is our query for grocery transactions:

```
client = ChalkClient()
client.query(
    input={
        Transaction.id: [1, 2, 3, 4],
        Transaction.category: "Groceries",
    },
    output=[
        Transaction.id,
        Transaction.amount,
    ],
)
```

When this query is run, Chalk adds each input parameter to the WHERE clause,
effectively running this query against your database:

```
SELECT
    id, merchant_category AS category, amount
FROM
    txn_table
+ WHERE
+     id IN (1, 2, 3, 4)
+     AND merchant_category = "Groceries";
```

If your database column names differ from your feature names, the column name must be aliased in the SELECT clause of
your query, as shown above with the merchant_category column.

### Configuration

### Supported SQL file resolver comment keys

The following are supported keys that may be included in .chalk.sql file comments.

Describes the namespace to which the outputs belong.
In the above example, user.email
and user.full_name are the outputs.

Describes the database by name, as in the above example, or
the type if there is only one database of that type. Thus, if you have
one PostgreSQL source, you can also write source: postgresql.

The type of resolver. If not specified, online is the default.

Parameters for incremental queries. For more information, see the 
below section on incremental queries.

The incrementalization mode decides how to ingest new data. Defaults to 
"row".

The length of the window from the last observed row that Chalk will re-ingest, e.g. 
1h. Defaults to 0.

The timestamp column in the underlying table to use as the basis for incrementalization.
Must be supplied in row and 
group modes.

The timestamp used for timedelta calculations. Defaults to 
feature_time.

Returns one. Equivalent to the common query finalizer .one().

The maximum time to wait before timing out the query.
See Duration for more details.

The user tags associated with this resolver. For online and offline resolvers.

The environments associated with this resolver.

The schedule for a cron run, e.g. 1h.

The max staleness for the resolver, e.g. 24h.

The owner of the resolver.

An optional mapping from SQL column to Chalk feature.
For example, with SELECT name AS arbitrary_column_name,
we can map the arbitrary_column_name to a Chalk feature belonging to
the
namespace described by the resolves field with the mapping
arbitrary_column_name: chalk_feature_name.

A list of features that must be unique for each row of the output.
This enables unique optimizations in the resolver execution.
Only applicable to resolvers that return a DataFrame.

A list of features that correspond to partition keys in the data source.
This field indicates that this resolver executes its query against a data storage system that is
partitioned by a particular set of columns.
This is most common with data-warehouse sources like Snowflake, BigQuery, Databricks, or Iceberg.

Whether this resolver returns all ids of a given namespace.
To have this annotation, the resolver must take no arguments and return a DataFrame.

### Proper comment formatting

All comments must be inserted before the body of the sql query. Each comment line is parsed as
either a yaml-formatted line describing the resolver or a docstring. Below, the last comment
will appear as a docstring since it is not in key:value format.

```
-- type: online
-- resolves: user
-- source: PG
-- This comment is not in yaml format, so it will be parsed as a docstring
select * from users
```

For field values that can be lists or dictionaries,
such as tags or incremental settings,
we can either enumerate the values inline or with an extra indentation.
Remember, if your values include a colon, you must use quotes around your value in order for
the line to have valid YAML format.

Both of the following formats are valid and equivalent.

```
-- type: online
-- resolves: user
-- source: PG
-- tags: ["single:1", "double:2"]
select * from users
```

```
-- type: online
-- resolves: user
-- source: PG
-- tags:
--    - single:1
--    - double:2
select * from users
```

### Streaming SQL file resolvers

Chalk supports streaming with SQL file resolvers:

```
-- source: kafka
-- resolves: store_features
-- type: streaming
select store_id as id, sum(amount) as purchases
from topic
group by 1
```

### SQL linting configuration

If you are using SQLFluff or another SQL Linter,
you may need to set configurations to accept the variable pattern.
For SQLFluff, set the templater to placeholder and add the following to your config file.

```
# Allows sqlfluff to correctly parse
# ${arbitrary_placeholder_name}

[sqlfluff:templater:placeholder]
param_regex =\$\{[^}]*\}
1 = 'arbitrary_placeholder_name'
```

### Generated SQL file resolvers

You can programmatically generate SQL resolvers with make_sql_file_resolver. This
function is useful if you have many SQL tables and want to automate management of their resolvers.

```
from chalk import make_sql_file_resolver
from chalk.sql import PostgreSQLSource

pg = PostgreSQLSource(name='PG')

definitions = [
    {
        resolver_name: "get_user_features",
        entity_name: "User",
        table: "users",
        pkey_column: "id",
        features: ["feature1", "feature2"],
    },
    ...
]

for definition in definitions:
    targets = ", ".join(definition.features)

    make_sql_file_resolver(
        name=definition.resolver_name,
        sql=f"select {definition.pkey_column}, {targets} from {definition.table}",
        source=pg, # "PG" is also acceptable
        resolves=definition.entity_name,
    )
```

make_sql_file_resolver adds this resolver to your registry as if it were a SQL file
resolver, but without creating the .chalk.sql file.

All SQL file resolvers require source and resolves. These values can be provided as SQL comments within your sql
value or as parameters. If comments and parameters are both provided, parameters will take precedence. This function
call is equivalent to the previous example:

```
make_sql_file_resolver(
    name=definition.resolver_name,
    sql=f"""
        -- source: PG
        -- resolves: {definition.entity_name}
        select {definition.pkey_column}, {targets} from {definition.table}
    """,
)
```

### Incremental queries

### Overview

The first time that a resolver with an incremental
query is executed, Chalk ingests all data from the source.
On subsequent runs of the resolver, Chalk only looks for
new rows in the table to ingest.
Using incremental queries limits the amount of data that
Chalk needs to ingest, lowering latency for updates
and reducing costs.

Incremental queries are useful for ingesting immutable tables
or queries, like event tables or logs.
This type of data is frequently found in the offline
context, as it represents logs of real-time events.

Incremental queries use the incremental_column parameter to
page over the underlying table.

### Incremental queries with SQL file resolvers

Imagine you have a login events table, where you keep track of login attempts to your website. You can ingest this table
with a SQL file resolver as follows:

```
-- type: offline
-- resolves: login
-- source: PG
-- incremental:
--   mode: row
--   lookback_period: 60m
--   incremental_column: attempted_at
select attempted_at, status, user_id from logins
```

Configuration for incremental resolvers can be passed in the incremental dictionary of the file's comments. For more
details, see the configuration reference above.

### Incremental queries with SQL strings

To use incremental mode with SQL string resolvers, use .incremental along with the incremental_column parameter.

```
pg = PostgreSQLSource(name='PG')

@offline
def fn() -> DataFrame[Login.attempted_at, Login.user_id, Login.status]:
    return (
        pg.query_string("select attempted_at, status, user_id from logins")
          .incremental(incremental_column="attempted_at")
    )
```

### Handling late-arriving messages

If your underlying data source has "late arriving records", you may need to use the lookback_period argument to
incremental. When lookback_period is specified, Chalk subtracts the lookback_period from the
"maximum observed timestamp" that it uses as a lower-bound for ingestion.

Concretely, if your resolver body looks like this:

```
db.query_string("SELECT * FROM payments")
    .incremental(incremental_column="updated_at", lookback_period="30m")
```

then Chalk will rewrite your SQL query to:

```
SELECT * FROM payments
WHERE updated_at >= (<previous_max_updated_at> - <lookback_period>)
```

This means that rows that arrive up to 30 minutes late will be properly ingested. The trade-off
is that Chalk will re-ingest some redundant data.

### Managing incremental resolvers

Each incremental resolver tracks the timestamp of its latest ingested row in an internal property called
chalk_incremental_timestamp. This property can be referenced within your SQL query when using parameter as your
incrementalization mode.

The Chalk CLI provides several commands for managing your incremental resolvers:

- chalk incremental status shows the status and latest timestamp of the given resolver.
- chalk incremental set allows you to directly modify the internal timestamps the resolver
uses to track its state.
- chalk incremental drop clears the resolver's tracking state so that it will restart data
ingestion on its next run.

### Incrementalization modes

The default incrementalization mode for .incremental is mode='row'. Three modes are supported:

- row: Chalk ingests features from all rows whose incremental_column is newer than the previously observed max timestamp.
- group: Chalk ingests features from all groups who are aggregating a row that has been added or changed since the previously observed max timestamp.
- parameter: Chalk passes the chalk_incremental_timestamp value (including lookback_period) to your query, and leaves your query unchanged.

### "Group" incremental mode

Group mode incremental ingestion is appropriate when you are aggregating rows in a table in order to compute
features.

For example, if you are running the following query:

```
SELECT
    business_id,
    SUM(amount) as sum_payments_amount,
    COUNT(*) as count_payments,
    max(updated_at) as ts
FROM
    payments
GROUP BY
    1
```

to ingest features for this feature class:

```
@features
class Business:
    id: int
    sum_payments_amount: float
    count_payments: int
    ts: FeatureTime
```

then you can specify the following resolver:

```
@offline(...)
def resolve_aggregate_payment_features() -> DataFrame[Business]:
    query = """
        SELECT
            business_id,
            SUM(amount) as sum_payments_amount,
            COUNT(*) as count_payments,
            max(updated_at) as ts
        FROM
            payments
        GROUP BY
            1
    """

    return db.query_string(query, fields={"business_id": Business.id}) \
                .incremental(incremental_column="updated_at", mode="group")
```

and Chalk will automatically rewrite your query into this form:

```
SELECT
    business_id,
    SUM(amount) as sum_payments_amount,
    COUNT(*) as count_payments,
    max(updated_at) as ts
FROM payments
WHERE business_id IN (
    SELECT DISTINCT(business_id) FROM payments
    WHERE updated_at >= :chalk_incremental_timestamp
)
GROUP BY 1
```

This means that if you have a payments table like this:

```
| id | business_id | amount | updated_at               |
| 1  | 1           | 10     | 2022-11-01T00:00:00.000Z |
| 2  | 1           | 5      | 2022-11-15T00:00:00.000Z |
| 3  | 2           | 7      | 2022-11-15T00:00:00.000Z |
| 4  | 3           | 17     | 2022-10-01T00:00:00.000Z |
```

and your query had previously run on 2022-11-07, then Chalk would return the following aggregate values:

```
| business_id | sum_payments_amount | count_payments | ts                       |
| 1           | 15                  | 2              | 2022-11-01T00:00:00.000Z |
| 2           | 7                   | 1              | 2022-11-15T00:00:00.000Z |
```

Both business 1 and 2 are present, because they have at least one payment after 2022-11-07.
Business 3 is excluded, since it has no payments that after 2022-11-07.

### "Parameter" incremental mode

In parameter incremental mode, Chalk leaves your query untouched. Chalk will simply pass the max incremental timestamp
to your query as a bind parameter named chalk_incremental_timestamp.

Concretely, if you write:

```
@offline(...)
def parameter_incremental_mode_resolver() -> DataFrame[...]:
    return (
        db.query_string("SELECT * FROM payments WHERE updated_at >= :chalk_incremental_timestamp")
           .incremental(mode="parameter")
    )
```

Then Chalk will execute your query verbatim, and will keep track of the appropriate value for chalk_incremental_timestamp
between executions of your resolver.

### Incremental interaction with FeatureTime

When Chalk executes an incremental query, it has to update the "max timestamp" value that it will use as the
lower bound for the next query. By default, Chalk sets this value to the time at the start of the query.

If your resolver returns a FeatureTime feature, Chalk will update the "max timestamp" value
to the "max" FeatureTime value that is returned instead. This allows you to control the incremental
behavior more precisely.

### Tagged SQL sources

Chalk supports applying tags to SQL sources. This allows you to define a single resolver that routes traffic
to multiple different backing databases depending on tags supplied at query time. This is useful for limiting
the blast-radius of traffic from different use-cases.

First, define a SQL source group:

```
from chalk.sql import SQLSourceGroup, PostgreSQLSource

sql_group = SQLSourceGroup(
    name='primary_group',
    default=PostgreSQLSource(name="default_replica"),
    tagged_sources={
        'risk': PostgreSQLSource(name='risk_replica'),
        'analytics': PostgreSQLSource(name='analytics_replica'),
    }
)
```

Then, define a resolver that uses the group:

```
@online
def users() -> DataFrame[User]:
    return sql_group.query_string("select id, name from users").all()
```

Then, when you submit queries, the query tags will control which data source is used to execute the
query:

```
client = ChalkClient()

# This query uses the risk datasource
client.query(input={User.id: 1}, output=[User.name], tags=['risk'])

# This query uses the analytics data source

client.query(input={User.id: 1}, output=[User.name], tags=['analytics'])

# This query uses the default datasource
client.query(input={User.id: 1}, output=[User.name])
```

### Additional query options

### SQLAlchemy

Chalk supports SQLAlchemy:

```
pg = PostgreSQLSource(name='PG')

@online
def get_user(uid: User.id) -> Features[User.email, User.full_name]:
    return (
        pg.query(User(email=UserSQL.email, full_name=UserSQL.name))
        .filter_by(id=uid)
        .first()
    )
```

In the .query(...) call, you map the target columns of the
SQL statement to the feature namespace.
Here, we assign User.email to UserSQL.email and
User.full_name to UserSQL.name.

### Incremental queries with SQLAlchemy

To create an incremental SQLAlchemy query, use .incremental. Chalk will page over the underlying table using the
column mapped to FeatureTime.

```
pg = PostgreSQLSource(name='PG')

@offline
def fn() -> DataFrame[Login.ts, Login.attempted_at, Login.user_id, Login.status]:
    return pg.query(
        Login(
            ts=LoginHistorySQL.created_at,
            attempted_at=LoginHistorySQL.attempted_at,
            user_id=LoginHistorySQL.user_id,
            status=LoginHistorySQL.status,
        )
    ).incremental()
```

# Custom Data Source
source: https://docs.chalk.ai/docs/generic

## Integrate with any data source you use.

Chalk doesn't need to officially support a data source
or API vendor for you to include it in your feature pipelines.
Chalk has a mechanism for initializing objects at boot time,
and then you can use those objects within your resolver.

### Initializing

To initialize your custom data source, use the @before_all
decorator. The decorated function will run before any of your
resolvers are called:

```
import os
from chalk.features import before_all

vendor_client: VendorClient = VendorClient(...)

@before_all
def initialize():
    key = os.getenv("MY_VENDOR_KEY")
    vendor_client.api_key = key
```

This function has access to all
environment variables
configured for your environment.
Then, in your resolver,
you can use the vendor_client
knowing it has been correctly initialized.

```
@online
def get_vendor_score(...) -> ...:
    vendor_client.do_something(...)
```

You can alternatively supply environment-specific
initialization functions. The before_all decorator
takes an optional keyword argument environment that
accepts a single environment name or a list of applicable
environment names:

```
@before_all(environment="**production**")
def initialize():
    ...

@before_all(environment=["**staging**", "**development**"])
def initialize():
    ...
```

### Initialization order

The order in which setup hooks run is not guaranteed and may differ across instances of your service. Your setup hooks
should not rely on being called in a specific order.

### Scopes

You should be careful when trying to assign a variable outside the local
scope. In the below example, the vendor_client isn't initialized as it may
appear to be. Instead, a new local variable that shadows the name in the
outer scope is initialized, and the outer variable doesn't receive a value.

Careful with assigning outside of the local scope.

```
vendor_client: VendorClient

@before_all
def initialize():
    vendor_client = VendorClient(...)
```

Instead, try modifying the client inside the initialization function:

Modify the outer scope from the inner scope.

```
vendor_client: VendorClient = VendorClient(...)

@before_all
def initialize():
    vendor_client.api_key = os.getenv("MY_VENDOR_KEY")
```

If you really want to assign a variable in the outer scope, you can
use Python's global keyword.

Use the global to modify outside of local scope (not recommended, but correct)

```
vendor_client: VendorClient

@before_all
def initialize():
    global vendor_client
    vendor_client = VendorClient(...)
```

However, if you do this,
you need to make sure that access to vendor_client
happens through the module.
Global is discouraged
because of this footgun.

```
import myproject
from myproject import vendor_client

@online
def fn(...) -> ...:
    vendor_client.api_call(...)            # Error! vendor_client is None
    myproject.vendor_client.api_call(...)  # Correct!
```

### Cleaning up

If there is clean up work you need to do when Chalk
suspends your runtime, you can specify that work in
a function decorated with @after_all.

```
from chalk.features import after_all

@after_all
def tear_down():
    ...
```

As with before_all, you can
optionally supply a filter on the environment:

```
@after_all(environment=["**production**"])
def tear_down():
    ...

@after_all(environment=["**staging**"])
def tear_down():
    ...
```

# Test Integrations Locally
source: https://docs.chalk.ai/docs/local-development

## Execute resolvers that connect to external systems

### Introduction

Many resolvers generate features by connecting to external, production-like systems (e.g. databases and APIs).
It can be challenging to validate these resolvers since they involve communication between several systems.
This guide will help you execute resolvers that communicate with those external systems on your local environment.

### Setup Environment Variables

Chalk's datasource integrations operate by assuming certain environment variables exist which provide integration information (such as urls, passwords, etc.) to the python code.
When executing these resolvers locally, you'll need to replicate those environment variables.  For the following guide lets assume a single Postgres datasource named "PG".

- The first env var lists all your datasources by name.

```
_CHALK_AVAILABLE_INTEGRATIONS=["PG"]
```

- Then you should set environment variables for datasource.  These environment variables should be pre-fixed with the datasource name.  You should have a env var for each field in

```
PG_PGHOST=database-1.myproject.us-west-1.rds.amazon.com 
PG_PGPORT=5432
PG_PGDATABASE=db
PG_PGUSER=postgres
PG_PGPASSWORD=password
```

### Exercise your resolvers

Once the environment variables are setup correctly, you can execute your resolver like any python code.
For example if the file chalkproject/resolvers.py includes a resolver like get_transactions_from_snowflake, you can execute it any python environment.

```
$ source .venv/bin/activate
$ (.venv) python
>>> from chalkproject.resolvers import get_transactions_from_snowflake
>>> get_transactions_from_snowflake()
```

# Environment Variables
source: https://docs.chalk.ai/docs/env-vars

## Access environment variables in your resolvers.

Chalk lets you inject environment variables into the
runtime for your resolvers.
You can add an environment variable through the dashboard,
where you'll find a form that looks like this:

Here, you can provide any environment variable you need.
The value will be available in all the environments you
check on the right side of the pane.

Environment variables can include secrets or configuration.
All environment variables are securely stored using a
Key Management Service.

Then, in your resolver
or in a setup hook,
you can access these environment variables as you would
normally:

```
import os

value = os.getenv("my_variable")
```

### Chalk environment variables

Chalk also provides a few environment variables that you
can use in your resolvers.

| Name                       | Description                                                                                           |
| -------------------------- | ----------------------------------------------------------------------------------------------------- |
| TARGET_ROOT              | The root directory of the application. This variable is set for both branch and standard deployments. |
| CHALK_DEPLOYMENT_ID      | The ID of the deployment                                                                              |
| CHALK_TEAM_ID            | The ID of the team                                                                                    |
| CHALK_PROJECT_ID         | The ID of the project                                                                                 |
| CHALK_ACTIVE_ENVIRONMENT | The id of the active environment (e.g. "9d0oj902")                                                   |
| CHALK_ENVIRONMENT_NAME   | The name of the active environment (e.g. "prod")                                                     |

# Unit Tests
source: https://docs.chalk.ai/docs/unit-tests

## Unit tests for Chalk resolvers

Chalk lets you specify your feature pipelines using idiomatic Python.
You can unit test individual resolvers and combinations of resolvers as you would normal Python
functions.

Read more about how to write integration tests for resolvers here.

### Testing resolvers

Consider the following features and resolvers:

```
from chalk.features import features, Features
from chalk import online

@features
class Home:
    id: str
    address: str
    price: int
    sq_ft: int

@online
def get_address(hid: Home.id) -> Home.address:
    return "Bridge Street" if hid == 1 else "Filbert Street"

@online
def get_home_data(
    hid: Home.id,
) -> Features[Home.price, Home.sq_ft]:
    return Home(
        price=200_000,
        sq_ft=2_000,
    )
```

You can test them just like normal Python functions
using any unit testing framework:

```
def test_single_output(self):
    assert get_address(2) == "Filbert Street"

def test_multiple_output(self):
    result = get_home_data(2)
    assert result.price == 200_000
    assert result.sq_ft == 2_000
    assert result == Home(
        price=200_000,
        sq_ft=2_000,
    )
```

### DataFrame inputs

If you specify projections or filters in
DataFrame arguments of resolvers, Chalk will
automatically project out columns and filter rows in
the input data.

### Filters

Consider if we extend the Home class to include
a rooms field:

```
+ @features
+ class Room:
+     id: str
+     home_id: "Home.id"
+     name: str

@features
class Home:
    id: str
    address: str
    price: int
    sq_ft: int
+   rooms: DataFrame[Room]
+   num_bedrooms: int
+
+ @online
+ def get_num_bedrooms(
+     rooms: Home.rooms[Room.name == 'bedroom']
+ ) -> Home.num_bedrooms:
+     return len(rooms)
```

The get_num_bedrooms resolver filters the rooms
argument to only include bedrooms. We can test this
by passing in a list of rooms, some of which are
bedrooms and some of which are not:

```
def test_get_num_rooms():
    # Rooms is automatically converted to a `DataFrame`
    rooms = [
        Room(id=1, name="bedroom"),
        Room(id=2, name="kitchen"),
        Room(id=3, name="bedroom"),
    ]

    # The kitchen room is filtered out
    assert get_num_bedrooms(rooms) == 2

    # `get_num_bedrooms` also works with a `DataFrame`
    assert get_num_bedrooms(DataFrame(rooms)) == 2
```

Note that although we passed in a list of three rooms,
only two of them were bedrooms, so the resolver
returns 2.

Furthermore, we didn't need to convert the list of
rooms to a DataFrame. In this case, we passed in a
list of Room objects, but Chalk automatically
converts it to a DataFrame for us. We also could
have passed in a polars.DataFrame or any other
valid constructor for DataFrame.

### Projections

Chalk will also automatically project the input data
as specified by the DataFrame argument. So, if you
specify which columns you need in the resolver body,
but accidentally use an extra column in your resolver
body, your unit tests will fail.

For example, if we wrote a resolver for summing
the square footage of all rooms in a home
using the Room.sq_ft feature, but accidentally
excluded the Room.sq_ft column in the DataFrame
argument:

```
@online
def get_sqft(
    rooms: Home.rooms[Room.name]
) -> Home.sq_ft:
    # This will fail because we used `Room.sq_ft`
    return rooms[Room.sq_ft].sum()
```

Then our unit tests will fail:

```
def test_get_sqft():
    rooms = [
        Room(id=1, name="bedroom", sq_ft=100),
        Room(id=2, name="kitchen", sq_ft=200),
        Room(id=3, name="bedroom", sq_ft=300),
    ]

    # This will fail because we used `Room.sq_ft`,
    # which is excluded by the `Home.rooms[Room.name]`
    # argument
    assert get_sqft(rooms) == 400
```

### after(...)/before(...) and time filtering

Some DataFrame filters are implicitly resolved relative to "now". In offline_query and online_query, this value
is controlled by input_times= and now= parameters, respectively. In unit tests, the value defaults to
datetime.now(), but can be explicitly set with the chalk.freeze_time context manager:

```
from chalk import freeze_time

@online
def get_p30d_transactions_count(txns: User.transactions[after(days_ago=30)]) -> User.recent_txn_count_30d:
    """
    Count the number of transactions that have occurred in the past 30 days
    """
    return txns.count()

NOW = datetime.now(tz=timezone.utc)

transactions = DataFrame([
    Transaction(id=1, created_at=NOW),
    Transaction(id=2, created_at=NOW - timedelta(days_ago=30)),
    Transaction(id=3, created_at=NOW - timedelta(days_ago=32))
])

# There is a single transaction in the range (30, 0] days ago
assert get_p30d_transactions_count(transactions) == 1

# There are two transactions in the range (45, 15] days ago
with freeze_time(at=NOW - timedelta(days_ago=15)):
    assert get_p30d_transactions_count(transactions) == 2
```

Note that the at= parameter must be timezone-aware.

# Integration Tests
source: https://docs.chalk.ai/docs/integration-tests

## Integration tests for Chalk resolvers

A Chalk resolver is a callable Python function that you can unit test like any other Python function,
making assertions on the expected output. Chalk also provides two features that make integration testing really easy.

- branch deployments,
- the check method of the python Chalk client.

With branch deployments, you can test your changes in an isolated environment before
shipping your code into production.

With Chalk check, you can set up simple integration tests that assert on the expected outputs of your queries.

### Branch deployments

Chalk allows you to create an unlimited number of branch deployments.
Branch deployments run all of your resolvers in the same way
that they run in production. However, branch deployments don't impact
the offline store.

### Creating a branch deployment

You can create a branch deployment in the same
way that you create a full deployment by passing
the flag --branch <branch_name>.

```
# --branch creates a branch deployment
> chalk apply --force --await --branch <branch_name>
```

The --await flag means that the deployment will
be live by the time that the command returns.

### Querying a branch deployment from CLI

You can quickly check your branch deployment using
chalk query --branch on the command line to
pull feature values:

```
# Example of making a query directly
> chalk query --branch <branch_name> \
              --in user.id=1 \
              --out user.id \
              --out user.email
```

The flag --branch tells this query to target the branch set during chalk apply.

### Querying a branch deployment using ChalkClient

You can also target a branch from the
Chalk API client.
Using this client, you can write integration tests:

Branch deployments are a great way to quickly test whether the changes you have made to features
or resolvers are behaving as expected when they are composed and executed in response to Chalk
queries.

However, if you want to write concrete integration tests, we recommend using the check method of
the Chalk Python client.

### Writing Integration Tests using ChalkClient.check()

Suppose you have the following features defined in chalk:

```
from chalk.features import DataFrame, features, FeatureTime, _
from chalk.streams import Windowed, windowed

@features
class Transaction:
    id: int
    user_id: "User.id"
    amount: float
    ts: FeatureTime

@features
class User:
    id: int
    name: str
    transactions: DataFrame[Transaction]
    transaction_count: Windowed[int] =  windowed(
        "1d", "3d",
        expression=_.transactions[_.ts > _.chalk_window].count(),
    )
    transaction_mean: Windowed[float] =  windowed(
        "1d", "3d",
        expression=_.transactions[_.amount, _.ts > _.chalk_window].mean(),
    )
```

You can write integration tests with the ChalkClient by leveraging the check method. The check method allows assertion on values, errors, and cache hits. Mismatches between expected
and resolved data will be printed in a table.

Note that the service token being used by the ChalkClient must have permission to Query online features to be able to use the check method.

```
from chalk.client import ChalkClient
from chalk.features import DataFrame
from src.feature_sets import Transaction, User
import datetime as dt
import pytest


@pytest.fixture(scope="session")
def client():
    return ChalkClient(local=True) # this will deploy your local changes to a branch using the name of your current git branch
    # return ChalkClient(branch=True) # Uses your current git branch


def test_transaction_aggregations(client):
    now = dt.datetime.now()

    result = client.check(
        input={
            User.id: 1,
            User.transactions: DataFrame([
                Transaction(id=1, amount=10, ts=now - dt.timedelta(days=1)),
                Transaction(id=2, amount=20, ts=now - dt.timedelta(days=2)),
                Transaction(id=3, amount=30, ts=now - dt.timedelta(days=3)),
                Transaction(id=4, amount=40, ts=now - dt.timedelta(days=4)),
                Transaction(id=5, amount=50, ts=now - dt.timedelta(days=5)),
                Transaction(id=6, amount=60, ts=now - dt.timedelta(days=6)),
                Transaction(id=7, amount=70, ts=now - dt.timedelta(days=7)),
                Transaction(id=8, amount=80, ts=now - dt.timedelta(days=8)),
                Transaction(id=9, amount=90, ts=now - dt.timedelta(days=9)),
            ])
        },
        assertions={
            User.transaction_sum["3d"]: 60,
            User.transaction_sum["1d"]: 10,
            User.transaction_mean["1d"]: 10,
            User.transaction_mean["3d"]: 21,   # This test will fail because this value is incorrect!
        }
    )
```

You can then run pytest -s tests/test_transaction_aggregations.py, where you will see a result like this:

```
$ pytest tests/test_transaction_aggs.py -s
==================================================== test session starts =====================================================================
platform darwin -- Python 3.10.14, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/chalk/deployment/
configfile: pyproject.toml
plugins: anyio-4.4.0
collected 1 item

tests/test_transaction_aggs.py

Chalk Feature Value Check Table
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Kind   ┃ Name                       ┃ Value ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ Match  │ user.transaction_count[1d] │ 1     │
│ Match  │ user.transaction_count[3d] │ 3     │
│ Match  │ user.transaction_mean[1d]  │ 10.0  │
│ Expect │ user.transaction_mean[3d]  │ 21.0  │
│ Actual │ user.transaction_mean[3d]  │ 20.0  │
└────────┴────────────────────────────┴───────┘
{'user.transaction_count__259200__': 3, 'user.transaction_count__86400__': 1, 'user.transaction_mean__86400__': 10.0, 'user.transaction_mean__259200__': 20.0}
F
```

### Testing for errors

You can also use the check method to test for errors. This might look like the following:

```
from chalk.client import ChalkClient
from chalk.features import DataFrame
from chalk.client import ChalkClient, ErrorCode, ErrorCodeCategory, ChalkError
from src.feature_sets import Transaction, User

import pytest


@pytest.fixture(scope="session")
def client():
    return ChalkClient(local=True) # this will deploy your local changes to a branch using the name of your current git branch
    # return ChalkClient(branch=True) # Uses your current git branch


def test_user_null_error(client):
    result = client.check(
        input={
            User.id: 1,
            User.name: None,
        },
        query_errors=[
            ChalkError(
                code=ErrorCode.PARSE_FAILED,
                category=ErrorCodeCategory.REQUEST,
                message="Received a null input for feature 'user.name', which is non-nullable (with type 'str').",
            )
        ],
        assertions={
            User.name: ...
        },
    )
```

### Integration Testing Using Tagged Resolvers

In addition to the check method, you can also use tagged resolvers to test changes to resolvers.
If you have a resolver that you want to update and then test, you could add resolver tags
to two versions of the resolver--one tagged "v1.0.0" and one tagged "v1.0.1", for example. Then, you
can run two queries with the same input data but the different tags and compare the query outputs
to ensure that the new resolver is working as expected.

### GitHub Action

You can also run integration tests as part of your CI/CD pipeline using the Chalk
GitHub Action.
You will need to create a Chalk token from the settings
page of your dashboard with the necessary permissions and store the resulting client
id and secret as
GitHub Secrets.

```
name: Chalk Integration Test

on: push

jobs:
  chalk-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          cache: 'pip'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - uses: chalk-ai/deploy-action@v2
        with:
          client-id: ${{secrets.CHALK_CLIENT_ID}}
          client-secret: ${{secrets.CHALK_CLIENT_SECRET}}
          # Deploys Chalk to a branch environment
          branch: ${{ GITHUB_REF_NAME }}
          # Waits for the deployment to succeed (Optional, default false)
          await: true

      - name: Runs a test query against the branch
        run: |
          # Example of making a query directly against a branch
          chalk query --branch ${{ GITHUB_REF_NAME }} \
                      --in user.id=1 \
                      --out user.id \
                      --out user.email \
                      --json \
                      --include-meta

          # Alternatively, run the integration test suite, which should make queries with the branch parameter.
          pytest -s ./tests
```

# Snapshot Tests
source: https://docs.chalk.ai/docs/snapshot-tests

## Snapshot testing with Chalk

Snapshot testing is an effective way of ensuring that your features are not dramatically changing
between deployments. You can set up snapshot testing in Chalk by leveraging Datasets.

Typically, snapshot testing will be part of a CI (continuous integration) workflow. Pull requests will automatically
trigger tests which verify that code changes have not caused feature distribution shifts.

In this section, we'll walk through the process of creating snapshot tests using Pytest and GitHub Actions.

### Overview

To set up snapshot testing, we'll write a couple Pytest fixtures, a test, and a helper script. The fixtures will pull
your current snapshot data and create a new snapshot based on your current code. The test will then compare the distributions of
the features in your old and new datasets. The helper script will update the main snapshot and will be run when a PR is
merged.

In this example we'll be snapshot testing the features on the following feature class:

```
from chalk.features import features
import datetime as dt

@features
class User:
    id: int
    full_name: str
    birthday: dt.datetime
    age: int
```

In this example, we resolve the full_name and birthday of our User's from a Postgres database. The age feature is calculated using an online resolver:

```
from chalk import online
from chalk.features import Now

@online
def get_age_in_years(bday: User.birthday, now: Now) -> User.age:
    return now.year - bday.year - ((now.month, now.day) < (bday.month, bday.day))
```

Though this is a rather trivial example, lets set some expectations for our feature distribution shifts between snapshots:

- We expect a User's birthday to never change,
- We expect a User's full_name to change in a maximum of 0.001% of our users (1/100,000),
- We expect a User's age to change by a maximum amount of 2 years (in reality, average age will increase by precisely the amount of time between invocations of our snapshot test).

### Writing the Test and Helper Script

First we'll write two fixtures: the first sets up a Chalk Client and the second creates your new snapshot (using
the previous snapshot to make sure that the exact same User ids are being pulled).

```
from chalk.client import ChalkClient
from chalk.features import DataFrame
from src.feature_sets import Transaction, User
import datetime as dt
import pytest
import pandas as pd


@pytest.fixture(scope="session")
def client():
    return ChalkClient(branch=True) # Uses your current git branch


@pytest.fixture(scope="session")
def snapshots(client: ChalkClient):
    # The dataset name will be set to the latest commit on the branch
    main_snapshot = client.get_dataset(dataset_name="user_snapshot")
    main_snapshot_df = snapshot.to_pandas().set_index(User.id)

    branch_snapshot = client.offline_query(
        input={User.id: main_snapshot_df.index.to_list()},
        recompute_features=True,
        wait=True,
        run_asynchronously=True
    )
    branch_snapshot_df = branch_snapshot.to_pandas().set_index(User.id)

    return active_snapshot_df, branch_snapshot_df
```

These fixtures serve to output two Pandas DataFrames: the main_snapshot_df (which is stored in
a dataset called user_snapshot) and the branch_snapshot_df (which is generated
on the fly with an offline query).

Next, we will use those snapshots in a test:

```
# Note, we skip this test locally since we only want to run it in CI
@pytest.mark.skipif(os.getenv("CI") is None, reason="Skipping on local machine")
def test_snapshot__user_feature_drift(snapshot_dfs: tuple[pd.DataFrame, pd.DataFrame]):
    main_snapshot, branch_snapshot = snapshot_dfs

    # Birthdays should not change
    assert main_snapshot[User.birthday].equals(branch_snapshot[User.birthday])

    # Full names should not change in more than 0.001% of users
    assert (main_snapshot[User.full_name] != branch_snapshot[User.full_name]).mean() < 0.00001

    # Age should not change by more than 2 years between runs
    assert (main_snapshot[User.age] - branch_snapshot[User.age]).max() <= 2
```

In addition to the tests, we'll create a script which will run when we merge pull requests—this
script will update the user_snapshot dataset with the one generated with our latest code.

```
import os
from chalk.client import ChalkClient

branch = os.environ["GITHUB_REF_NAME"]
client = ChalkClient(branch=branch)

dataset = client.get_dataset(dataset_name="user_snapshot")

dataset.recompute_features(branch=branch, wait=True, run_asynchronously=True)
```

### Writing the GitHub Action

We will write two GitHub actions: one will run when we create a pull requests, the other
will run when we merge code into our main branch.

The first GitHub Action sets up the environment and then runs pytest. The
GitHub Action is set to run on pull, which means it will run when we open a
pull request against main:

```
name: Chalk Integration Test

on:
  pull_request:
    branches: [main]

jobs:
  chalk-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          cache: 'pip'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - uses: chalk-ai/deploy-action@v2
        with:
          client-id: ${{secrets.CHALK_CLIENT_ID}}
          client-secret: ${{secrets.CHALK_CLIENT_SECRET}}
          # Deploys Chalk to a branch environment
          branch: ${{ GITHUB_REF_NAME }}
          # Waits for the deployment to succeed (Optional, default false)
          await: true

      - name: Runs the Snapshot Test
        run: |
          pytest -s ./tests
```

The second GitHub Action runs our update script to update the user_snapshot dataset with our latest snapshot. It runs whenever we push code to the main branch.

```
on:
  push:
    branches: [main]
jobs:
  update-snapshot:
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          cache: 'pip'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - uses: chalk-ai/cli-action@main
        with:
          client-id: ${{ secrets.CHALK_CLIENT_ID }}
          client-secret: ${{ secrets.CHALK_CLIENT_SECRET }}
          environment: ${{ secrets.CHALK_ENVIRONMENT }}

      - name: Update snapshot
        run: python3 scripts/update_user_snapshot.py
```

### Bootstrapping the GitHub Action

Before this works fully, we need to bootstrap the snapshot test. If you tried
to run the action above, you'd get an error when running client.get_dataset(...):
the error would indicate that the dataset was not found. To bootstrap your snapshot,
you'll want to run an offline_query to create a dataset named user_snapshot.

```
from src.feature_sets import User

client.offline_query(
    output=[User],
     # This can be however many you want to include in your snapshot
    max_samples=200_000,
    recompute_features=True,
    run_asynchronously=True,
    dataset_name="user_snapshot"
)
```

With your initial snapshot created, future pull requests will be able to automatically execute a snapshot test
against your main deployment.

# Time Overview
source: https://docs.chalk.ai/docs/time

## Manage feature timestamps and point-in-time query timestamps.

### Overview

Chalk uses two main timestamps you should be aware of as you build your Chalk project:

- Feature time (FeatureTime): The time at which a feature was observed, which is used in query time filters and
aggregation time windows.
- Query time (Now): The time a query should assume is "now" when retrieving data. Features whose feature time comes
after a given query time will never be returned for those queries, in online or offline contexts.

Feature time is returned in the __observed_at__ column in Chalk query results. Query time is returned in the __ts__
column.

### Feature time

Feature time is the time at which a feature was observed. By default, Chalk sets a feature's time to the feature's
resolver execution time. The feature time can be overridden for a feature class, accessed from resolver parameters, and
requested in query inputs and outputs.

You may have multiple timestamps associated with your data. It's important to set the feature time to the value that
most closely represents when your system would have accessed the data in production.

For example, in an asynchronous streaming system, you may have one timestamp for when an event was added to your task
queue and another timestamp for when the event was removed from the queue and processed. We recommend using the
latter timestamp as your feature time to make your training most closely resemble production. If you use the timestamp
for when an event was added to your task queue, you would be training your system with data it would not have been able
to access in production.

### Setting feature time for a feature class

Each individual feature has its own feature time, which is used to retrieve point-in-time correct data for temporal
consistency.

To access the latest time associated with any feature in a feature class, use the special FeatureTime feature
throughout Chalk.

By default, if it is present, Chalk will treat a feature named ts with datetime.datetime type as the FeatureTime
value. Otherwise, you can use the FeatureTime type annotation to set a different name:

```
from chalk.features import features, FeatureTime

@features
class User:
    id: int
    name: str
    timestamp: FeatureTime  # datetime.datetime under the hood
```

Using your FeatureTime feature, you can access and override feature time for the whole feature class.

You can directly set the FeatureTime value by returning it from a resolver:

```
@offline
def fn(...) -> Features[User.name, User.timestamp]:
    return User(
        name="Maryam Mirzakhani",
        ts=datetime(2014, 8, 12, tzinfo=timezone.utc)
    )
```

You can include the FeatureTime feature in query output. Its value
will be set to the maximum timestamp across all features in its feature class.

### Time filtering in resolvers

has-many features create DataFrames. These DataFrames can be filtered with
before and after.

Regardless of which time filters you use, Chalk will never return features where the feature time is strictly greater
than the current query time (Now), in order to maintain temporal consistency.

### Examples

To compute the number of transfers a user made in the last seven days, use after:

```
from chalk.features import after, ...

@online
def fn(transfers: User.transfers[after(days_ago=7)]) -> ...:
    return transfers.count()
```

To compute the number of transfers a user made more than seven days ago, use before:

```
from chalk.features import before, ...

@online
def fn(transfers: User.transfers[before(days_ago=7)]) -> ...:
    return transfers.count()
```

Combine before and after to retrieve transfers made 1-2 weeks ago:

```
from chalk.features import before, after, ...

@online
def fn(transfers: User.transfers[after(days_ago=14), before(days_ago=7)]) -> ...:
    return transfers.count()
```

All of these examples can be used in combination with other DataFrame projections and
filters. You may also find windowed
aggregations useful.

### Interaction with the online store

Features with overridden observation timestamps are treated specially when inserted into the online store.
In particular, Chalk will always check for existing "newer" feature values in the online store
before inserting historically dated feature values. This means that you can safely ingest large quantities
of backdated features without accidentally ingesting stale data into the online store.

Additionally, once features are inserted into the online store, Chalk tracks the source observation timestamps
when these feature values are returned as part of online queries. Chalk uses these source timestamps
to compute the "feature staleness" metric. Staleness in this context is defined as "query time - observation time".

### Interaction with the offline store

Features with overridden observation timestamps are inserted into the offline store with the timestamp that you
specify. The observation timestamp works like an "effective as of" timestamp, so if you insert something like this:

```
| id | feature | value | timestamp            |
|---------------------------------------------|
| 1  | age     | 7     | 2022-02-01T00:00:00Z |
```

into an offline store that already contained these observations:

```
| id | feature | value | timestamp            |
|---------------------------------------------|
| 1  | age     | 6     | 2022-01-01T00:00:00Z |
| 1  | age     | 8     | 2022-03-01T00:00:00Z |
```

then the observation will be interleaved "in between" the existing observations, and you would see the following query
results:

```
id, age, <= 2022-02-01
output: 7

id, age, <= 2022-03-02
output: 8

id, age, <= 2022-01-02
output: 6
```

### Enforcing a TTL

Features in the offline store have an optional TTL (time to live). When a feature has a TTL value, it will never be
returned at any time later than FeatureTime + TTL. For example, you may not want to consider credit scores which were
retrieved more than a year ago. Setting offline_ttl will make credit_score return
None if last observed credit score is more than one year old in comparison to the current query time.

```
@features
class User:
    id: str
    credit_score: int = feature(offline_ttl=timedelta(years=1))
```

### Query time

Query time is the time treated as "now" within a query context. For online queries, Now is equal to datetime.now().
For offline queries, you can pass one or more timestamps that will be used as the query time for each input row. In
Chalk Expressions, you can reference the query time with _.chalk_now.

### Setting query time

In training, you will likely want to retrieve data as if you are at a point in the past to create the most accurate
predictions. We cover this idea in greater detail in our temporal consistency
documentation.

To set the query's "now" time, pass input_times as either a single
timestamp or as a list corresponding to the Now times to use for each entry in input:

```
from datetime import timezone

ChalkClient().offline_query(
    # Pass id 1 multiple times because we want to
    # request it with multiple input_times
    input={User.id: [1, 1, 1]},  
    input_times=[
        datetime.now(tz=timezone.utc) - timedelta(days=365 * 10),
        datetime.now(tz=timezone.utc) - timedelta(days=365),
        datetime.now(tz=timezone.utc) - timedelta(days=0),
    ],
    output=[User.age_in_years],
)

## Output:

# | id | age_in_years |
# | 1  | <age> - 10   |
# | 1  | <age> - 1    |
# | 1  | <age> - 0    |
```

### Accessing query time in resolvers

To access the query time in your resolvers, you can reference a special feature called Now, which is a
datetime.datetime object.

You can pass Now in Python resolvers:

```
from chalk import Now

@online
def get_age_in_years(birthday: User.birthday, now: Now) -> User.age_in_years:
    return (now - birthday).years
```

Now can be used in DataFrame resolvers as well in order to compute bulk values:

```
@online
def batch_get_age_in_years(df: DataFrame[User.id, User.birthday, Now]) -> DataFrame[User.id, User.age_in_years]:
    return (
        df.to_polars()
            .select(
                pl.col(User.id),
                pl.col(str(User.birthday) - pl.col(str(Now))).alias(str(User.age_in_years))
            )
    )
```

You can also reference ${now} in SQL file resolvers.

```
-- source: sql_file_resolver_temp_db
-- resolves: tv_episode
select id,
       name,
       season_no,
       episode_no,
       show_name,
       air_date
from tv_episodes
where air_date < ${now}
  and id = ${tv_episode.id}
```

You can also reference _.chalk_now in Chalk Expressions, particularly in
windowed aggregations:

```
from chalk import features, _
from chalk.streams import windowed, Windowed

@features
class Store:
    id: int
    visits: DataFrame[Visit]

    num_recent_visits: Windowed[int] = windowed(
        "1d", "7d", "30d",
        expression=_.visits[
            _.ts <  _.chalk_now,
            _.ts > _.chalk_window
        ].count(),
        default=0,
    )
```

### Accessing query time in query results

Chalk Datasets return the query time in the __ts__ column.

When converting Chalk Datasets to Polars or Pandas DataFrames, you may want to include the query time column. To do so,
pass output_ts to your to_polars or to_pandas calls.
You may pass a column name to output_ts to set the name of the query time column. If you pass True, the query time
column name will be __chalk__.CHALK_TS.

Be careful to not mix up ts and ts. ts represents the query time, or the
time the query treats as "now" during query execution. ts is a common name for the feature representing
FeatureTime, the time at which a feature was observed.

### Timezone handling for naive datetimes

Chalk stores UTC as the timezone for naive datetime objects. Additionally, Chalk assumes UTC if retrieving naive
datetimes from data stores.

We recommend that you include timezone information on all datetime objects you work with to avoid ambiguity.

### When to use FeatureTime vs Now

Chalk enables different levels of temporal consistency, which also have different impacts on performance.
When a resolver does not have a FeatureTime or Now as an input or output, there is no temporal pushdown
filtering, so the resolver will be fully time independent, which will also be more performant. If the
resolver has a FeatureTime as an input, then Chalk will apply a temporal pushdown filter. Then, if a resolver
takes Now as an input, the resolvers can fully interact with time, which will provide the most accuracy for
point-in-time feature resolution but also be the least performant.

# Temporal Consistency
source: https://docs.chalk.ai/docs/temporal-consistency

## Point-in-time queries for training data sets.

### Introduction

Temporal consistency is crucial for ensuring your model's training performance is reflective of production. When
creating datasets for model training, your system must consistently retrieve data as it would appear at a specific point
in time. If your model trains on data that was retrieved after the point where it would have made a prediction, it will
not perform consistently in production.

Chalk performs point-in-time lookups on your training data so you can train your models knowing they won't receive data
from the future, even across complex relationships.

### Scenario 1: Historical loan decisions

In this scenario, we will consider a machine learning model for determining whether to issue loans to businesses based
on their financial performance.

For each business, we track sales and COGS (cost of goods sold) over time in millions of dollars. We define a Business
feature class with sales and cogs features:

```
from chalk.features import features, FeatureTime

@features
class Business:
    id: int
    sales: float
    cogs: float
    ts: FeatureTime
```

After collecting historical data on the performance of businesses we previously considered, we want to retrain our
model.

For a business with id=123, we gave loans at t1 and t2:

In training, you want to know the observed gross profit and COGS for the business at the time you made the loan without
knowing the future values of those features.

For example, at t1, when we issued the loan, we had observed sales of $1.3M. It would be inconsistent for this model to
train with the $1M data point because this data would not have existed at t1.

At t1 and t2, the temporally consistent values of sales and cogs would be as follows:

| Feature          | Value at t1                                            | Value at t2                                             |
| ---------------- | -------------------------------------------------------- | --------------------------------------------------------- |
| Business.sales |  1.3  |  1    |
| Business.cogs    |  0.5  |  0.4  |

Each of these values occurred at or before the sample time and is valid to use in training.

### Sample code

Chalk allows you to control the time your query considers to be "now", which is covered in greater detail in our
time documentation.

To set the query's "now" time, pass input_times to
your offline queries:

```
from chalk.client import ChalkClient

t1 = datetime.now() - timedelta(days=365)
t2 = datetime.now() - timedelta(days=30)

dataset = ChalkClient().offline_query(
     input={
         # Sample business 123 twice because we have two input_times
         Business.id: [123, 123],
     },
     # Each element of `input_times` corresponds to the element
     # with the same index in `input`
     input_times=[t1, t2],
     # Sample all features of business.
     # Alternatively, sample only the features you need:
     #   output=[Business.sales, Business.cogs]
     output=[Business],
)
```

This query will return a Dataset with temporally consistent values for each input time.

### Scenario 2: Backfilling new features

Temporal consistency is especially difficult when you want to build new features. Building on the first scenario,
imagine you've observed Business.sales and Business.cogs many times in the past, and for each of the businesses that
you track, these values have changed over time.

Now, you want to compute a new feature, Business.gross_profit, which is the difference between Business.sales and
Business.cogs. We can add an expression to compute this new feature:

```
- from chalk.features import features, FeatureTime
+ from chalk.features import _, features, FeatureTime

@features
class Business:
    id: int
    sales: float
    cogs: float
    ts: FeatureTime
+   gross_profit: float = _.sales - _.cogs
```

With the same historical data from the previous scenario, we can determine the correct inputs for computing
Business.gross_profit:

Business.gross_profit at t1 and t2 would be computed with the following values:

| Query time | Business.sales | Business.cogs | Business.gross_profit |
| --- | --- | --- | --- |
| t1 |  1.3  |  0.5  |  0.8  |
| t2 |  1.0  |  0.4  |  0.6  |

In your code, you can compute historical values for updated features by running an offline query with
recompute_features=True. You may also consider one of our
other backfill options for other use cases.

As you start layering more resolvers or using has-many relationships, temporal consistency becomes even
more difficult to reason about. Chalk manages the complexity under the hood so that you can write any query and expect
temporally consistent results.

# Batch Backfilling
source: https://docs.chalk.ai/docs/backfilling-data

## Chalk makes it easy to batch ingest historical feature data from datasets and bulk data sources.

### Backfilling from datasets

The most common way to backfill features is to ingest them from a dataset. This is useful when you have historical
data ready or when you want to compute and backfill new features based on existing data.

Run an offline query to obtain a Dataset of the feature values you want
to ingest and then call .ingest to store online or offline:

```
from chalk.client import ChalkClient

# Query for historical data
dataset = ChalkClient().offline_query(
    input={
        User.id: [i for i in range(1000)],
    },
    output=[
        User.favorite_color,
        User.purchase_count,
        User.last_active
    ],
)

# Ingest into the offline store for training
dataset.ingest(store_offline=True)

# Or ingest into the online store for serving
# dataset.ingest(store_online=True)
```

### Backfills from bulk sources

When ingesting historical feature data from external bulk data sources (such as a data warehouse or S3), you can override
feature time with timestamps from the data source. Chalk uses feature time to determine when a feature
should be included in your point-in-time queries for consistency with production.

First, define a FeatureTime feature for the relevant feature class:

```
@features
class User:
    id: int
    ...
    backfilled_feature: str
    ...
    ts: FeatureTime
```

Next, define a resolver to ingest data from your data source. Here's an example of a SQL file resolver for
ingesting data from Snowflake:

```
-- type: offline
-- resolves: User
-- source: snowflake

SELECT id, backfilled_feature, updated_at AS ts FROM users
```

Chalk assumes your timestamp column is in UTC. You may return many values of backfilled_feature for the same id, but
they should have different FeatureTime values.

Then, after running chalk apply, you can trigger this resolver to run once using the Chalk Dashboard or
the chalk trigger command:

```
chalk trigger --resolver your.module.path.ingest_historical_data
```

You must manually trigger the resolver because it has no cron schedule specified.

Once your resolver run completes, your data will be available in the offline store with effective times specified by the
values returned for the FeatureTime (in this example, updated_at from users). If the feature tolerates
staleness and etl_offline_to_online=True, then Chalk will also insert feature values into the
online store if they are newer than existing values.

### Re-ingesting incremental resolvers

Resolvers that use incremental ingestion don't re-process data from before their "max observed timestamp"
by default, even if the query is changed.

Chalk lets you reset the maximum observed timestamp of incremental resolvers to a specific timestamp,
or re-ingest all historical data.

Chalk uses offline queries to perform this operation. Suppose you want to add a new column,
favorite_color, to this existing batch SQL resolver:

```
-- type: offline
-- resolves: User
-- source: snowflake
-- cron: "0 * * * *"
-- incremental:
--   incremental_column: updated_at
SELECT id, favorite_food, favorite_color, updated_at FROM preferences
```

If you have been running this resolver in production for a long time, then simply adding favorite_color and
running chalk apply will not ingest historical color preferences because the incremental timestamp
lower bound will prevent the query from returning "old" rows which include these historical favorite_color observations.

Instead, run an offline query to obtain a Dataset of the feature values you want
to ingest and then call .ingest to either store online or
offline.

```
from chalk.client import ChalkClient

dataset = ChalkClient().offline_query(
    input={
        User.id: [i for i in range(1000)],
    },
    output=[
        User.favorite_color
    ],
)

dataset.recompute(features=['user.favorite_color'])
dataset.ingest(store_offline=True)
```

### Backfilling Python resolvers

Chalk can also backfill feature data for resolvers that take arguments to compute feature values. This
is useful for generating historically accurate training datasets using new resolvers that are derived from
features where we have historical observations.

Suppose we have the following feature class:

```
@features
class User:
    id: int
    name: str

    reversed_name: str # a feature we want to backfill
```

with the following newly added resolver:

```
@online
def reverse_name(name: User.name) -> User.reversed_name:
    return name[::-1]
```

Chalk can automatically compute this feature using historically observed values of User.name.  To do so, you can
either use an offline query with recompute_features=True and
ingest the computed feature values as we did above. Alternatively, you can use chalk trigger to
trigger a resolver run:

```
chalk trigger --resolver your.module.path.reverse_name --lower-bound 2024-05-05T12:00:00+00:00 --persist-offline=True
```

In this example, Chalk will query the offline store to sample all combinations of user.id, user.name, and the
corresponding FeatureTime for which FeatureTime is later than the ISO8601 timestamp passed in as the lower_bound.
For each sample, Chalk will invoke your resolver and write the results back to the offline store. Chalk will also update
the online store if the new feature is marked with non-zero max_staleness and etl_offline_to_online=True.

# Feature Development Lifecycle
source: https://docs.chalk.ai/docs/lifecycle

## Developing, testing, deploying, and backfilling a new feature

Chalk is the fastest way to deploy new features and feature
pipelines to production.
This demo covers creating a new feature.
You'll develop, unit test, integration test,
and deploy a resolver for this feature.
Then you'll see how to backfill that feature
to Chalk's offline store so that data scientists
can use it in historical training sets.

### Develop

The first step is to write a new feature and resolver for that feature.
Imagine you wanted to create a new feature called user.name_email_match_score.
This feature should capture the similarity between a user's name and email.
Put another way:
andy and andy@gmail.com should produce a high score, and
emily and andy@gmail.com should produce a low score.

The first step is to add the new feature, and a resolver for that feature.

Our new resolver name_email_match_scorer takes a dependency on
the user's email and fullname in the argument list.
Then, it declares that it returns the User.name_email_match_score
in the return type signature.

In the body of the function, we compute the
Jaccard index
between the email without the domain and the full name.

### Test

Now that you've written the new feature and resolver, it's time
to validate your change.
Chalk supports both unit testing and integration testing of your
feature pipelines.

### Unit test

You can unit test resolvers just like normal
Python functions using any unit testing framework:

```
from pytest import approx

def test_name_email_match_scorer():
    assert approx(0.60) == name_email_match_scorer(
        "katherine.johnson@nasa.gov",
        "Katherine Johnson",
    )
    assert approx(0.39) == name_email_match_scorer(
        "katherine.johnson@nasa.gov",
        "Eleanor Roosevelt",
    )
```

Here, the
Jaccard index
for katherine.johnson@nasa.gov is higher with the name
Katherine Johnson than with the name Eleanor Roosevelt,
as expected.

### Deploy branch

Now that the unit tests have passed,
you can create a Branch Deploy
with the new changes.

Chalk allows you to create an unlimited number of branch deployments.
Branch deployments run all of your resolvers in the same way
that they run in production. However, branch deployments don't impact
the offline store. You can create a branch
deployment with the following command:

```
chalk apply --branch test
```

### Integration test

With the branch deployment created, you can run integration tests
on your changes.

Here, the
Chalk API client
is configured to use the preview deployment id returned
in the previous step.

### Deploy

Once you've tested your changes, it's time to deploy!
This step looks much like the preview deployment,
but this time without the --branch flag:

```
chalk apply
```

Now, your production environments can request the new
user.name_email_match_score feature.

```
chalk query --in user.id=1 --out user.name_email_match_score
```

### Backfill

The user.name_email_match_score feature is live!
But historically, this feature did not exist,
and you won't be able to sample its values at previous times
until you backfill the values, which you can do with the 'chalk trigger' command.

```
chalk trigger --resolver example.name_email_match_scorer --lower-bound 2020-05-05T12:00:00+00:00 --persist-offline=True
```

This command will backfill historical values for the user.name_email_match_score feature.

### Offline training

With the feature backfilled, you can query
the historical value:

That's how you deploy a new feature with Chalk!
Let a member of our technical team know if we can be helpful.

### Delete

Mistakes are inevitable, but Chalk provides the tools you need to quickly and easily recover and keep going.

### Drop a feature

If you need to change a feature's type (for example from string to int), or if you want to drop all the data for a feature value, the Chalk CLI has you covered with chalk drop.  Simply execute the command from the CLI and you'll have a fresh start to recreate the feature and its data as necessary.

### Delete a row

Sometimes you just need to fully remove a record from your systems, whether because of a GDPR mandated "right to forget" request or due to a business requirement. Chalk provides the chalk delete command to meet this need.

# Working With Branches
source: https://docs.chalk.ai/docs/branches

## Make rapid changes and explore features with branches.

Branch deployments allow users to quickly iterate on features and datasets.When working in a branch users have a number of useful capabilities, including:

- Chalk can automatically watch your files and deploy any changes
- Updates to your project are deployed in seconds
- Adjust and create features and resolvers inside a Jupyter notebook
- Quickly recompute datasets to see the effects of changes
- Branches have a consistent name across deployments

However, branch deployments do not pick up changes to environment variables or secrets,
so these changes would require a new non-branch deployment to take effect.

### Create a Branch Deployment

To create a branch, simply run chalk apply --branch <branch_name>. Chalk will create a new branch in the environment that you can interact with. Now, you can make queries against your branch with chalk query --branch.If you're using the Python API, you can set the branch when creating your client, and all subsequent commands will execute against your branch.

### Continuously Deploy Changes

You can ask the Chalk CLI to continuously deploy changes to your branch using the watch flag.
Chalk will automatically keep the branch up to date as you make changes locally.

### Develop in a Notebook

One of the major advantages of branch deployments is the flexibility they offer when working in notebooks.Once you've deployed a branch, you can iteratively edit features and resolvers and see the effects of these updates in a dataset.
Create a chalk client and set the branch parameter equal to your branch. Then, any time you execute a cell that contains a class annotated with @features it will automatically be updated in your branch.
Similarly, executing cells that contain a function annotated with @online or @offline will automatically deploy the resolver to your branch.

```
@features
class NewFeatures:
    id: int
    name: str
    greeting: str

@online
def new_resolver(name: NewFeatures.name) -> NewFeatures.greeting:
    return f"Hello {name}!"
```

### Recompute Datasets

As you adjust features and resolvers, you can iteratively see how your changes affect your feature values with the Dataset.recompute method. Just pass any features you want to be re-computed as arguments to the features parameter, and Chalk will generate a new Dataset revision using the latest definitions of features and resolvers.

When used in conjunction with the ability to adjust your features and resolvers in the notebook, this tool allows developers and data scientists to rapidly experiment and productionize their work.

### Example

In the following example we add an oversize feature to an existing dataset of loans.

We start out with a dataset. We may have produced this dataset manually, by calling an external API, or by executing offline_query.

```
dataset
shape: (786, 3)
┌───────────────┬──────────────┬─────────────────────────┐
│ loan.amount   ┆ loan.id      ┆ loan.event_time         │
│ ---           ┆ ---          ┆ ---                     │
│ f64           ┆ str          ┆ datetime[μs, UTC]       │
╞═══════════════╪══════════════╪═════════════════════════╡
│ 165435.647396 ┆ l_G3Mc6bi9y4 ┆ 2023-04-08 10:03:09 UTC │
│ 405006.796909 ┆ l_O9OK3us7t2 ┆ 2022-02-07 20:46:08 UTC │
│ 680377.427817 ┆ l_L0Gg0Bd1v3 ┆ 2023-02-16 16:48:29 UTC │
│ 562678.545344 ┆ l_D1Rb5Jq4U5 ┆ 2022-06-21 06:15:19 UTC │
│ …             ┆ …            ┆ …                       │
│ 750583.279013 ┆ l_W4ZY9OK5N7 ┆ 2021-12-16 21:40:27 UTC │
│ 71698.15609   ┆ l_H9tG2yJ5B6 ┆ 2023-01-04 11:33:54 UTC │
│ 488697.890372 ┆ l_L4fd4xu4w2 ┆ 2022-08-22 03:55:16 UTC │
│ 769665.198436 ┆ l_k4Dq8bl7b3 ┆ 2022-10-31 07:15:52 UTC │
└───────────────┴──────────────┴─────────────────────────┘
```

In our Jupyter notebook, we can execute this in a cell to set up our notebook to point to our branch, then update our branch with the new feature and resolver.

```
client = ChalkClient(branch="<our_branch>")

# We want to introduce an `oversize` detection feature
@features
class Loan:
    id: str
    event_time: datetime
    status: str
    amount: float
    oversize: bool

# Detect any loans bigger than $250,000
@online
def is_oversize(amt: Loan.amount) -> Loan.oversize:
    return amt > 250000
```

Finally, we can recompute our dataset, telling it to calculate Loan.oversize, to get a dataset back with our new feature values.

```
# Recomputing the dataset will add the oversize column to our result
dataset.recompute(features=[Loan.oversize])
shape: (786, 4)
┌───────────────┬───────────────┬──────────────┬─────────────────────────┐
│ loan.oversize ┆ loan.amount   ┆ loan.id      ┆ loan.event_time         │
│ ---           ┆ ---           ┆ ---          ┆ ---                     │
│ bool          ┆ f64           ┆ str          ┆ datetime[μs, UTC]       │
╞═══════════════╪═══════════════╪══════════════╪═════════════════════════╡
│ true          ┆ 165435.647396 ┆ l_G3Mc6bi9y4 ┆ 2023-04-08 10:03:09 UTC │
│ true          ┆ 405006.796909 ┆ l_O9OK3us7t2 ┆ 2022-02-07 20:46:08 UTC │
│ true          ┆ 680377.427817 ┆ l_L0Gg0Bd1v3 ┆ 2023-02-16 16:48:29 UTC │
│ true          ┆ 562678.545344 ┆ l_D1Rb5Jq4U5 ┆ 2022-06-21 06:15:19 UTC │
│ …             ┆ …             ┆ …            ┆ …                       │
│ true          ┆ 750583.279013 ┆ l_W4ZY9OK5N7 ┆ 2021-12-16 21:40:27 UTC │
│ true          ┆ 71698.15609   ┆ l_H9tG2yJ5B6 ┆ 2023-01-04 11:33:54 UTC │
│ true          ┆ 488697.890372 ┆ l_L4fd4xu4w2 ┆ 2022-08-22 03:55:16 UTC │
│ true          ┆ 769665.198436 ┆ l_k4Dq8bl7b3 ┆ 2022-10-31 07:15:52 UTC │
└───────────────┴───────────────┴──────────────┴─────────────────────────┘
```

# Static Resolver Optimization
source: https://docs.chalk.ai/docs/static-resolver-optimization

## Accelerate Python resolvers using Chalk's symbolic interpreter for columnar execution.

Chalk's static resolver optimization transforms Python resolvers into high-performance columnar operations through
symbolic execution, eliminating Python's runtime overhead while maintaining its developer-friendly syntax.

### The Performance Challenge

Python resolvers provide flexibility and ease of use for feature engineering, but traditional Python execution
introduces significant performance bottlenecks in real-time ML workloads:

- Row-by-row processing: Traditional Python resolvers process data one row at a time
- Global Interpreter Lock (GIL): Prevents true parallel execution across multiple CPU cores
- Dynamic typing overhead: Runtime type checking adds computational cost
- Limited vectorization: Cannot leverage SIMD operations for numerical computations

These limitations can make Python resolvers unsuitable for latency-sensitive applications requiring sub-millisecond
response times.

### Symbolic Execution Approach

Chalk addresses these performance challenges by converting Python resolver functions into optimized
Velox-native expressions at query-plan time. This transformation
happens automatically without requiring changes to your resolver code.

### How It Works

- Symbolic Analysis: At query planning stage, Chalk analyzes your Python resolver function
- Type Tracking: Maintains both Python and Velox types during symbolic interpretation
- Expression Tree Building: Executes the function symbolically with "symbolic values" that represent computation trees
- Columnar Translation: Transforms Python logic into efficient columnar operations
- Automatic Fallback: Gracefully falls back to subprocess execution for unsupported functions

For more details on the implementation, check out our blog post.

Static optimization is automatically applied to compatible Python resolvers. No code changes or special decorators are required.

### Supported Operations

The symbolic interpreter supports a wide range of Python operations commonly used in feature engineering:

### Basic Operations

- Arithmetic operations (+, -, *, /, //, %, **)
- Comparison operations (<, >, <=, >=, ==, !=)
- Logical operations (and, or, not)
- String operations (basic manipulation and formatting)

### Data Types

- Numeric types (int, float)
- Strings (str)
- Booleans (bool)
- None values and null handling

### Control Flow

- Conditional expressions (if/else)
- Simple list comprehensions
- Basic function calls

### Performance Benefits

Static resolver optimization delivers significant performance improvements:

### Parallel Execution

- Eliminates Python's GIL restrictions
- Enables true multithreaded processing
- Scales linearly with available CPU cores

### Vectorized Operations

- Leverages SIMD (Single Instruction, Multiple Data) instructions
- Processes multiple data points simultaneously
- Optimizes memory access patterns

### Reduced Overhead

- Removes dynamic typing checks at runtime
- Eliminates Python interpreter overhead
- Minimizes memory allocations

### Example Performance Impact

```
@online
def compute_risk_score(
    transaction_amount: Transaction.amount,
    user_avg_transaction: Transaction.user.avg_transaction_amount,
    merchant_risk_factor: Transaction.merchant.risk_factor
) -> Transaction.risk_score:
    if transaction_amount > user_avg_transaction * 10:
        return merchant_risk_factor * 2.5
    else:
        return merchant_risk_factor * 0.5
```

This resolver, when optimized, can process millions of transactions per second compared to thousands with traditional Python execution.

### Best Practices

To maximize the benefits of static resolver optimization:

### Keep Resolvers Simple

Focus on computational logic rather than complex control flow:

```
# Good: Simple mathematical computation
@online
def calculate_ratio(numerator: Feature.a, denominator: Feature.b) -> Feature.ratio:
    return numerator / denominator if denominator != 0 else 0

# Less optimal: Complex nested logic
@online
def complex_calculation(a: Feature.a, b: Feature.b, c: Feature.c) -> Feature.result:
    result = a
    for i in range(10):  # Loops may not optimize
        if b > i:
            result = custom_function(result, c)  # External functions may not optimize
    return result
```

### Use Native Operations

Stick to Python's built-in operations when possible:

```
# Good: Uses native operations
@online
def normalize_value(value: Feature.value, mean: Feature.mean, std: Feature.std) -> Feature.normalized:
    return (value - mean) / std if std > 0 else 0

# Less optimal: External library calls
@online
def normalize_with_library(value: Feature.value) -> Feature.normalized:
    import numpy as np  # External libraries may not optimize
    return np.log1p(value)
```

### Leverage Type Annotations

Ensure all inputs and outputs have proper type annotations:

```
@online
def typed_resolver(
    amount: Transaction.amount,  # Explicit feature type
    rate: Transaction.currency.exchange_rate  # Explicit feature type
) -> Transaction.converted_amount:  # Explicit return type
    return amount * rate
```

### Monitoring Optimization

You can verify whether your resolvers are being optimized by checking the query execution logs or by viewing the
query plan in the dashboard. Optimized resolvers will be marked as accelerated, and if your Python resolver is not
optimized the query plan node will also provide information about why it was not optimized. Optimized resolvers will
show significantly lower execution times and higher throughput.

### Limitations

While powerful, static optimization has some limitations:

- Complex control flow: Deeply nested loops or recursive functions may not optimize
- Dynamic code: eval(), exec(), or dynamic attribute access patterns

When the optimizer encounters unsupported operations, it automatically falls back to standard Python execution, ensuring
your resolvers always work correctly.

### Summary

Static resolver optimization in Chalk bridges the gap between Python's ease of use and the performance requirements of
real-time ML systems. By automatically converting Python resolvers into optimized columnar operations, Chalk enables you
to write maintainable feature engineering code that runs at production scale without sacrificing performance.

# Tasks
source: https://docs.chalk.ai/docs/tasks

## Run arbitrary Python scripts in your Chalk deployment

Tasks let you run arbitrary Python code in your Chalk deployment environment with full access to your resolvers, dependencies, and infrastructure.

Tasks execute in the same environment as your resolvers, making them ideal for:

- Data backfills: Recompute historical features or migrate data
- One-off computations: Run ad-hoc analyses, reports, or maintenance tasks
- ML training: Execute training scripts with access to your feature infrastructure
- Testing and validation: Run data quality checks or integration tests

All tasks are tracked and monitored through the Chalk dashboard with full logs, metrics, and status tracking.

### Quick Start

The fastest way to run a task is using the Chalk CLI.

First, create a simple Python script:

```
echo 'print("Hello from Chalk tasks!")' > script.py
```

Then, run it with the Chalk CLI:

```
chalk task run script.py
```

The CLI will output a link to view your task in the dashboard:

```
✓ View task at: https://chalk.ai/projects/my-project/environments/prod/tasks/550e8400...
```

Click the link to see your script's output, status, and execution metrics.

### CLI Reference

### Basic Usage

The chalk task run command executes Python scripts in your deployment:

```
chalk task run [target] [flags]
```

### Target Formats

The target supports multiple formats:

### Running a File

Execute an entire Python script:

```
chalk task run scripts/data_migration.py
```

### Running a Function

Execute a specific function from a file:

```
chalk task run scripts/backfill.py::process_batch
```

### Running a Module

For installed Python modules, use the -m / --module flag. Modules require --branch for access to your deployment. See Branch Execution for details.

```
# Module execution
chalk task run -m mypackage.scripts.backfill --branch my-branch

# Module function
chalk task run -m mypackage.scripts.backfill::main --branch my-branch
```

### Passing Arguments

CLI arguments are always passed as strings. Your function should handle type conversion as needed.

### Arguments for Functions

When running a specific function (with ::function), arguments are passed directly to your function as *args and **kwargs:

```
chalk task run script.py::backfill --arg 2024-01-01 --arg 2024-12-31 --arg dry_run=true
```

```
def backfill(start_date: str, end_date: str, dry_run: str = "false"):
    """
    Positional arguments: start_date, end_date
    Keyword arguments: dry_run
    """
    is_dry_run = dry_run == "true"
    print(f"Backfilling from {start_date} to {end_date} (dry_run={is_dry_run})")

    if not is_dry_run:
        # Perform actual backfill
        pass
```

### Arguments for Whole Files

When running a whole file (without ::function), arguments are passed as command-line arguments. You can use sys.argv or an argument parser to access them:

Using sys.argv:

Direct access to raw command-line arguments as a list:

```
chalk task run script.py --arg 2024-01-01 --arg 2024-12-31
```

```
#!/usr/bin/env python3
import sys

if len(sys.argv) >= 3:
    start_date = sys.argv[1]
    end_date = sys.argv[2]
    print(f"Processing data from {start_date} to {end_date}")
```

Using argparse:

Provides automatic parsing, help messages, and type handling:

```
chalk task run process.py --arg users.csv --arg --dry-run --arg output_dir=./results
```

```
#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='Input CSV file')
parser.add_argument('--dry-run', action='store_true', help='Run without making changes')
parser.add_argument('--output_dir', default='./output', help='Output directory')
args = parser.parse_args()

print(f"Processing {args.input_file}")
print(f"Dry run: {args.dry_run}")
print(f"Output directory: {args.output_dir}")
```

### Batch Execution

Execute the same script multiple times with different parameters using a JSONL file. This is useful for hyperparameter sweeps, batch processing, or running experiments across different data segments.

### JSONL Format

Each line is a JSON object with kwargs (and optionally args):

```
{"kwargs": {"learning_rate": "0.001", "batch_size": "32", "epochs": "10"}}
{"kwargs": {"learning_rate": "0.005", "batch_size": "64", "epochs": "10"}}
{"kwargs": {"learning_rate": "0.01", "batch_size": "128", "epochs": "5"}}
```

### Running Batch Tasks

```
chalk task run scripts/train_model.py::train --args-file hyperparams.jsonl
```

This creates a separate task for each line in the file. The CLI will show progress and provide a link to view all tasks in the dashboard.

### Generating JSONL Files

From Python:

```
import json

params = [
    {"kwargs": {"user_id": i, "region": "us-west"}}
    for i in range(1000, 2000)
]

with open("batch_params.jsonl", "w") as f:
    for param in params:
        f.write(json.dumps(param) + "\n")
```

From a database query:

```
import json
import psycopg2

conn = psycopg2.connect(...)
cursor = conn.cursor()
cursor.execute("SELECT user_id, region FROM users WHERE needs_backfill = true")

with open("users_to_backfill.jsonl", "w") as f:
    for user_id, region in cursor:
        f.write(json.dumps({
            "kwargs": {"user_id": user_id, "region": region}
        }) + "\n")
```

### Branch Execution

When you're making changes across multiple files, updating dependencies, or modifying resolvers that your script uses, it's important to test everything together before merging to production. Branch deployments let you run tasks in an isolated environment that includes all your changes:

```
chalk task run scripts.py --branch feature/new-algorithm
```

This automatically:

- Runs chalk apply --branch feature/new-algorithm
- Waits for the branch deployment to be ready
- Submits the task to the branch environment

You can skip the automatic apply if the branch is already deployed:

```
chalk task run scripts/hello.py --branch feature/new-algorithm --skip-apply
```

See Working with Branches for more information.

### CLI Flags Reference

### Module flag

-m, --module - Treat the target as a module import path instead of a file path.

```
chalk task run -m mypackage.analytics.report
```

### Branch flags

--branch BRANCH_NAME - Execute code from a specific git branch. See Branch Execution.

--skip-apply - Skip the automatic chalk apply when running with --branch. Use this if the branch is already deployed.

### Argument flags

--arg KEY=VALUE or --arg VALUE - Pass arguments to your script. Can be specified multiple times. See Passing Arguments.

--args-file FILE.jsonl - Execute script multiple times with different arguments from a JSONL file. See Batch Execution.

### Execution flags

--max-retries N - Set number of retry attempts on failure. Defaults to 0 (no retries).

```
chalk task run flaky_api_call.py --max-retries 3
```

### Monitoring and Dashboard

Tasks appear in the Chalk dashboard where you can monitor their execution and debug failures.

### Accessing the Dashboard

After submitting a task, the CLI outputs a link to the dashboard:

```
$ chalk task run scripts/hello.py

✓ View task at: https://chalk.ai/projects/my-project/environments/prod/tasks/550e8400...
```

You can also view all tasks at the tasks overview page, which shows aggregate CPU and memory utilization charts across all running tasks.

### Task Details

The task detail page displays:

- Execution timeline - Visual timeline showing queue time, execution attempts, and retries
- Status - Current state (QUEUED, WORKING, COMPLETED, FAILED, CANCELED)
- Logs - Full stdout and stderr output with search and filtering
- Metrics - CPU and memory utilization for the task
- Source code - View and download the uploaded script
- Task metadata - Branch, deployment ID, resource group, start/end times, and author

### Task Statuses

- QUEUED - Task is waiting to execute
- WORKING - Task is currently running
- COMPLETED - Task finished successfully
- FAILED - Task encountered an error or non-zero exit code
- CANCELED - Task was manually canceled

### Additional Usage

### Logging in Tasks

Task logs are captured and displayed in the Chalk dashboard. You can use standard print() statements which will appear in your task logs. You can also use chalk_logger in your script for structured logging:

```
from chalk import chalk_logger

def process_data(batch_size: str):
    batch_size_int = int(batch_size)

    chalk_logger.info(f"Starting data processing with batch_size={batch_size_int}")

    # Your processing logic
    for i in range(batch_size_int):
        chalk_logger.debug(f"Processing batch {i+1}/{batch_size_int}")
        # ... process data ...

    chalk_logger.info("Data processing completed successfully")
```

chalk_logger provides:

- Structured log levels (debug, info, warning, error)
- Better integration with Chalk's logging infrastructure
- Consistent formatting with resolver logs

### Running Class Methods

You can execute class methods using the double-colon syntax:

```
# File-based class method
chalk task run scripts/processor.py::DataProcessor::run

# Module-based class method
chalk task run mypackage.processors::ETLProcessor::execute --module
```

### Troubleshooting

### Task Stuck in QUEUED

If a task remains in QUEUED status:

- Verify Kubernetes pods are running
- Check for image pull errors or pod crashloops
- Ensure the job queue is processing tasks

### Import Errors

```
ModuleNotFoundError: No module named 'mypackage'
```

Solutions:

- Ensure the package is in requirements.txt or pyproject.toml
- Verify the package is installed in your active deployment
- For modules, ensure the module path is correct

### Argument Issues

If arguments aren't being passed correctly:

- Remember CLI args are always strings - convert types in your function
- Use key=value format for kwargs, plain values for positional args
- Test locally first with the same argument format

### Next Steps

- Learn about Working with Branches for development workflows
- Explore Model Training for ML-specific tasks
# GitHub Actions
source: https://docs.chalk.ai/docs/github-actions

## Deploy feature pipelines in GitHub Actions

Chalk provides official support for GitHub Actions.
You can install the Chalk CLI and create deployments
(preview and production) from pre-built GitHub Actions.

### Installing the Chalk CLI

You will need to create a Chalk token from the settings
page of your dashboard and store the resulting client
id and secret as
GitHub Secrets.

This step supports the following inputs:

- client-id: The Chalk Client ID from the tokens page in your settings.
- client-secret: The Chalk Client Secret from the tokens page in your settings.
- version (optional): The version of chalk to install, defaulting to latest.
- api-host (optional): If you're using a self-hosted deployment, the API host where Chalk is hosted.
- environment (optional): The Chalk environment to use. Your token is typically scoped to a single environment, and you won't need to use this parameter.

### Example

```
- uses: chalk-ai/cli-action@v2
  with:
    client-id: ${{secrets.CHALK_CLIENT_ID}}
    client-secret: ${{secrets.CHALK_CLIENT_SECRET}}
    # Optional: Version of the Chalk CLI to install. Defaults to `latest`
    version: latest
    # Optional: Environment to use. Optional for environment-scoped tokens.
    environment: <environment id>
    # Optional: Used for Hybrid Cloud deployments
    api-host: https://custom.deployment.com/
```

For more information, see the chalk-ai/cli-action
on the GitHub Marketplace,
or see a complete example at chalk-ai/examples.

### Deploying to Chalk

You can deploy to Chalk by first installing the CLI, as in the section above.
Or, you can use the chalk-ai/deploy-action step.
This step supports the following inputs:

- client-id: The Chalk Client ID from the tokens page in your settings.
- client-secret: The Chalk Client Secret from the tokens page in your settings.
- branch (optional): By default, Chalk will deploy to your production environment. With branch, your pipelines will deploy to a Chalk branch.
- await (optional): Should this step block until it completes? Defaults to true.
- version (optional): The version of chalk to install, defaulting to latest.
- api-host (optional): If you're using a self-hosted deployment, the API host where Chalk is hosted.
- environment (optional): The Chalk environment to use. Your token is typically scoped to a single environment, and you won't need to use this parameter.

### Example

```
- uses: chalk-ai/deploy-action@v2
  with:
    client-id: ${{secrets.CHALK_CLIENT_ID}}
    client-secret: ${{secrets.CHALK_CLIENT_SECRET}}
    # Optional: Version of the Chalk CLI to install. Defaults to `latest`
    version: latest
    # Optional: Environment to use. Optional for environment-scoped tokens.
    environment: <environment id>
    # Optional: Used for Hybrid Cloud deployments
    api-host: https://custom.deployment.com/
```

# GitLab CI/CD
source: https://docs.chalk.ai/docs/gitlab-cicd

## Deploy feature pipelines in GitLab CI/CD

Chalk provides official support for GitLab CI/CD.
You can install the Chalk CLI and create deployments
(preview and production) using GitLab CI/CD jobs.

### Installing the Chalk CLI

You will need to create a Chalk token from the settings
page of your dashboard and store the resulting client
id and secret as
GitLab CI/CD Variables.

Create a job that supports the following variables:

- CHALK_CLIENT_ID: The Chalk Client ID from the tokens page in your settings (stored as CI/CD variable).
- CHALK_CLIENT_SECRET: The Chalk Client Secret from the tokens page in your settings (stored as masked CI/CD variable).
- CHALK_VERSION (optional): The version of chalk to install, defaulting to latest.
- CHALK_API_HOST (optional): If you're using a self-hosted deployment, the API host where Chalk is hosted.
- CHALK_ENVIRONMENT (optional): The Chalk environment to use. Your token is typically scoped to a single environment, and you won't need to use this parameter.

### Example

```
install-chalk:
  stage: setup
  image: ubuntu:latest
  before_script:
    - apt-get update && apt-get install -y curl
  script:
    - |
      # Download and install Chalk CLI
      CHALK_VERSION=${CHALK_VERSION:-latest}
      curl -L "https://github.com/chalk-ai/chalk/releases/${CHALK_VERSION}/download/chalk-linux" -o chalk
      chmod +x chalk
      mv chalk /usr/local/bin/chalk
    - |
      # Configure Chalk with credentials
      chalk auth --client-id "$CHALK_CLIENT_ID" --client-secret "$CHALK_CLIENT_SECRET"
      if [ -n "$CHALK_ENVIRONMENT" ]; then
        chalk config set environment "$CHALK_ENVIRONMENT"
      fi
      if [ -n "$CHALK_API_HOST" ]; then
        chalk config set api-host "$CHALK_API_HOST"
      fi
  variables:
    CHALK_CLIENT_ID: $CHALK_CLIENT_ID
    CHALK_CLIENT_SECRET: $CHALK_CLIENT_SECRET
    # Optional: Version of the Chalk CLI to install. Defaults to `latest`
    CHALK_VERSION: latest
    # Optional: Environment to use. Optional for environment-scoped tokens.
    CHALK_ENVIRONMENT: <environment id>
    # Optional: Used for Hybrid Cloud deployments
    CHALK_API_HOST: https://custom.deployment.com/
  artifacts:
    paths:
      - /usr/local/bin/chalk
    expire_in: 1 hour
```

For more information, see the Chalk CLI documentation or complete examples in your GitLab repository.

### Deploying to Chalk

You can deploy to Chalk by first installing the CLI, as in the section above, then creating a deployment job.
This job supports the following variables:

- CHALK_CLIENT_ID: The Chalk Client ID from the tokens page in your settings (stored as CI/CD variable).
- CHALK_CLIENT_SECRET: The Chalk Client Secret from the tokens page in your settings (stored as masked CI/CD variable).
- CHALK_BRANCH (optional): By default, Chalk will deploy to your production environment. With this variable, your pipelines will deploy to a Chalk branch.
- CHALK_AWAIT (optional): Should this job block until deployment completes? Defaults to true.
- CHALK_VERSION (optional): The version of chalk to install, defaulting to latest.
- CHALK_API_HOST (optional): If you're using a self-hosted deployment, the API host where Chalk is hosted.
- CHALK_ENVIRONMENT (optional): The Chalk environment to use. Your token is typically scoped to a single environment, and you won't need to use this parameter.

### Example

```
stages:
  - setup
  - deploy

install-chalk:
  stage: setup
  image: ubuntu:latest
  before_script:
    - apt-get update && apt-get install -y curl
  script:
    - |
      CHALK_VERSION=${CHALK_VERSION:-latest}
      curl -L "https://github.com/chalk-ai/chalk/releases/${CHALK_VERSION}/download/chalk-linux" -o chalk
      chmod +x chalk
      mv chalk /usr/local/bin/chalk
  artifacts:
    paths:
      - /usr/local/bin/chalk
    expire_in: 1 hour

deploy-chalk:
  stage: deploy
  image: ubuntu:latest
  dependencies:
    - install-chalk
  before_script:
    - cp chalk /usr/local/bin/chalk || echo "Using pre-installed chalk"
  script:
    - |
      # Configure Chalk with credentials
      chalk auth --client-id "$CHALK_CLIENT_ID" --client-secret "$CHALK_CLIENT_SECRET"
      if [ -n "$CHALK_ENVIRONMENT" ]; then
        chalk config set environment "$CHALK_ENVIRONMENT"
      fi
      if [ -n "$CHALK_API_HOST" ]; then
        chalk config set api-host "$CHALK_API_HOST"
      fi
    - |
      # Deploy to Chalk
      DEPLOY_CMD="chalk apply"
      if [ -n "$CHALK_BRANCH" ]; then
        DEPLOY_CMD="$DEPLOY_CMD --branch $CHALK_BRANCH"
      fi
      if [ "$CHALK_AWAIT" = "false" ]; then
        DEPLOY_CMD="$DEPLOY_CMD --no-wait"
      fi
      $DEPLOY_CMD
  variables:
    CHALK_CLIENT_ID: $CHALK_CLIENT_ID
    CHALK_CLIENT_SECRET: $CHALK_CLIENT_SECRET
    # Optional: Version of the Chalk CLI to install. Defaults to `latest`
    CHALK_VERSION: latest
    # Optional: Environment to use. Optional for environment-scoped tokens.
    CHALK_ENVIRONMENT: <environment id>
    # Optional: Used for Hybrid Cloud deployments
    CHALK_API_HOST: https://custom.deployment.com/
    # Optional: Deploy to a specific branch instead of production
    # CHALK_BRANCH: feature-branch
    # Optional: Wait for deployment to complete (default: true)
    # CHALK_AWAIT: "false"
```

# Queries Overview
source: https://docs.chalk.ai/docs/query-overview

## Fetch feature values via queries.

To request or compute data with Chalk, you'll use queries. In general,
when you run a Chalk query, you are either requesting the most up-to-date
values for your feature classes, requesting a set of historical data
for your feature classes, or running a backfill or batch job.

The first use case is accomplished through online queries, which try to
return values for a single feature class as quickly as possible, taking
advantage of caching and distributed execution.

The latter use cases are accomplished through offline queries which use
the offline store and can return multiple instances of a feature class
for multiple primary keys or timepoints.

### Running queries

At a high level, a query specifies input features and output features. Inputs differ slightly for online queries and
offline queries, but in both cases the input must contain the primary key of your requested feature class.

### Running online queries

Online queries can be run using query:

```
chalk query --in user.id=1 --out user.name
```

or one of our API Clients:

```
from chalk.client import ChalkClient

client = ChalkClient()
client.query(
  input={'user.id': 1},
  output=['user.name'],
  # branch='test', # run against a branch
)
```

### Running offline queries

Offline queries can be run with one of our API Clients:

```
from chalk.client import ChalkClient
from datetime import datetime

client = ChalkClient()
client.offline_query(
  input={'user.id': [1,2,3,4]},
  output=['user.name']
  # branch='test',                      # run against a branch
  # recompute_features=True,            # recompute features
  # run_asynchronously=True,            # run in separate pod from active deployment
  # max_samples = 10,                   # max of 10 samples
  # lower_bound=datetime(2024, 10, 12), # sample computed after 10.12.2024
  # upper_bound=datetime(2024, 10, 20), # sample computed before 10.20.2024
)
```

### Running queries using gRPC

If you have a gRPC query server active in your environment, you can also run queries using the
gRPC client:

```
from chalk.client.client_grpc import ChalkGRPCClient

grpc_client = ChalkGRPCClient()
grpc_client.query(
  input={'user.id': 1},
  output=['user.name']
)
```

### Scheduled and triggered resolver runs

Specific resolvers can also be scheduled or triggered (for instance, as part of
pipelines like Airflow). Specific queries can also be scheduled with
ScheduledQuery. Triggers and schedules are useful for pulling data from "slow" data
sources into your offline and online store.

### Query side effects

Chalk queries can also write data. This is an essential part of
Chalk: every time you compute a feature through an online query, the
output is written down in the offline store. This makes it easy to:

- create datasets from your previously computed features,
- monitor and track your computed features over time.

Though not the default, offline queries can write data to both the offline store and the online store using
etl_offline_to_online. This can be useful when backfilling data from slow
data sources or when performing expensive feature computation that would otherwise significantly impact the latency of
your online queries.

### Online and offline query differences

| Online query                                                                                                                  | Offline query                                                                                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Runs only  @online  resolvers | Runs both  @online  and  @offline  resolvers |
| Returns one row of data about one entity                                                                                      | Returns a DataFrame of many rows of historical data corresponding to multiple entities point-in-time                                                                                                                                         |
| Designed to return data in milliseconds                                                                                       | Blocks until computation is complete, not designed for millisecond-level computation                                                                                                                                                         |
| Queries the online store and calls @online resolvers for quick retrieval                                                    | Queries the offline store which stores all data from online queries, unless recompute_features=True, in which case @offline and @online resolvers are used to resolve the outputs                                                      |
| Writes output data to online store database and offline store database                                                        | Writes output to a parquet file containing results to cloud storage. Only writes to online store or offline store if specified.                                                                                                              |

# Online Queries
source: https://docs.chalk.ai/docs/query-online

## Fetch feature values via online queries

Online queries access or compute feature values for a single feature
set in real time. The term "real time" means that responses should seem
practically instantaneous, even if they need to compute features on new data.

However, online queries don't only perform data retrieval, they also store
the results of the features that they compute. This provides visibility and
long-term tracking into the features you are generating. In this section,
we provide a high level overview of how online queries compute and record
their outputs.

### How Do Online Queries Work?

Chalk responds to online queries by getting and executing a query plan.

### Getting a Query Plan

A query plan is a sequence of tasks, some of which can be executed in parallel,
that will produce a target output. Although a simplification, your resolvers
are a subset of these tasks. Consider the following feature class and resolvers:

```
from chalk.features import features, online

@features
class User:
  id: int
  name: str
  is_palindrome: str
  is_short: bool
  palindrome_and_short: bool

@online
def get_is_palindrome(name: User.name) -> User.is_palindrome:
  return name == name[::-1]

@online
def get_is_short(name: User.name) -> User.is_short:
  return len(name) < 3

@online
def get_is_short_palindrome(is_short: User.is_short, is_palindrome: User.is_palindrome) -> User.is_short_palindrome:
  return is_short and is_palindrome
```

If you were to begin assembling a dependency graph for the features. You would wind up with something
like the following:

```
┌───────────┐
│name       │
└┬─────────┬┘
┌▽───────┐┌▽────────────┐
│is_short││is_palindrome│
└┬───────┘└┬────────────┘
┌▽─────────▽────────┐
│is_short_palindrome│
└───────────────────┘
```

When you run an online query, such as:

```
chalk query --in user.id=1 --in user.name=bob --out is_short_palindrome
```

Chalk constructs a plan for how to "solve" this query. This query plan is viable
for other queries with the same input and output features.

 Running chalk query with the --explain flag outputs your query plan. 

The following query can reuse the plan generated by the one above:

```
chalk query --in user.id --in user.name=bartholomew --out is_short_palindrome
```

Even though both the input name and the output of the query are different, the query plan
remains valid.

### Executing a Query Plan

As illustrated above, a query plan is not a linear sequence of tasks that must
be executed one after another: a lot of work can often be performed in
parallel.

After getting a query plan, Chalk distributes subtasks to workers, applies
a number of optimizations on your resolvers/datasource connections, and
computes the target outputs of your query. These outputs are then returned.

There are multiple ways to run an online query. You can use the
Chalk API Client,
the Chalk CLI, or the REST API. For
example the following calls all trigger the same online query:

With the Chalk Python API Client:

```
from chalk.client import ChalkClient
from src.models import User


client = ChalkClient()
results = client.query(
    inputs={
        User.id: 1,
    },
    outputs=[User.organization, User.name],
)
```

With the Chalk CLI:

```
chalk query --in user.id=1 --out user.organization --out user.name
```

With the REST API:

```
curl -X POST {YOUR_ENGINE_URL}/v1/query/online \
  -H "Authorization: Bearer $access_token" \
  -H 'x-chalk-env-id: {YOUR_ENV_ID}' \
  -H 'x-chalk-deployment-type: engine' \
  -H 'content-type:application/json' \
  -d '{"inputs": {"user.id": 1}, "outputs":["user.organization", "user.name""]}'
```

### Caching and Writing

Online queries write computed values to two places: the offline store
and the online store. However, computed features are only written to
the online store if they have a caching policy.
The online store is used to circumvent recomputation of expensive features
that are either unlikely to have changed or can tolerate slightly stale
values. Properly configuring the caching policies for your features
can make your online queries significantly more efficient.

If you haven't specified a caching policy, Chalk recomputes the
values for a feature each time it is requested. We go into more depth
on query caching here.

# Scheduled Query
source: https://docs.chalk.ai/docs/scheduled-query

## Run feature pipelines on a schedule

When features are coming from a single SQL file, or a single resolver,
you can use resolver crons to keep your online
and offline stores up to date.

However, when features are chained together, or when you need to run
a feature pipeline on a schedule, you can use scheduled queries.

Scheduled queries let you run an offline query on a schedule,
and persist the results in the online and/or offline feature stores.

### Create a Scheduled Query

To create a scheduled query, make a ScheduledQuery
object somewhere in your code. Crontabs can be used to specify the
schedule in the UTC timezone.

```
from chalk import ScheduledQuery

ScheduledQuery(
    name="enrich-transactions",
    schedule="0 0 * * *",
    output=[Transaction.clean_name, Transaction.category],
    store_online=True,
    store_offline=True,
)
```

At the time of chalk apply, the scheduled query will be
created.

In the web, you can see the list of scheduled queries in Scheduled Runs tab.
Each run will show the status of the last execution, and you can click into
each run to see the logs.

Scheduled queries

### Incrementalization

By default, scheduled queries use incrementalization to only ingest data which
has been updated since the last run. You can also set a resolver to use as the
source of the incrementalization. For example, if you were enriching financial
transaction data, you might use the transactions.chalk.sql resolver as the
source of incrementalization.

```
from chalk import ScheduledQuery

ScheduledQuery(
    name="enrich-transactions",
    schedule="0 0 * * *",
    output=[Transaction.clean_name, Transaction.category],
    store_online=True,
    store_offline=True,
    incremental_resolvers="transactions",
)
```

### Monitoring

You can monitor the status of scheduled queries in the Scheduled Runs tab.
From there, you can set up alerts to notify you when a scheduled query fails.
To set up an alert, click on the Add Alert button in the top right corner of the
page.

Cron Alerts

All alerts integrate with your other Chalk alerting integrations, including
email, PagerDuty, Slack, and incident.io.

Additionally, you can export metrics about scheduled query executions to your observability tools.
The cron_run_request metric (see metrics export documentation) tracks the number of times a scheduled
query was executed, with tags for success/failure status. This allows you to monitor scheduled query reliability
and alert when executions fall below expected thresholds in your preferred monitoring system.

### Resources

By default, scheduled query runs are picked up by the Job Queue Server. To see your
Job Queue Server resource configurations, check the Job Queue Server service under
Resources in the dashboard. To customize the resources allocated to runs for a specific
scheduled query, you can set the resource configuration under the Scheduled Query Configuration
tab in the dashboard.

# Named Queries
source: https://docs.chalk.ai/docs/named-query

## Track and manage named queries in Chalk

With Chalk NamedQuery objects, you can define and version
your common query patterns in code.

This provides several advantages:

- queries are preplanned on engine boot, reducing first-query latency,
- query outputs and parameters don't need to be hardcoded, reducing boilerplate code and ensuring consistency between your queries,
- queries are grouped together on the web, making them easier to track, monitor, and debug.

### Relationship to models

Named queries typically map to specific models that you're running in production.
While feature classes model your domain objects (users, transactions, accounts) and may contain hundreds of features
for reuse across different models, a named query selects only the specific subset of features needed for a particular model.

For example, you might have a User feature class with 100+ features capturing everything about a user: their
profile, behavior metrics, transaction history aggregations, and risk signals. However, your fraud detection model
might only need 15 specific features, while your recommendation model needs a different set of 30 features.
Named queries let you define these model-specific feature sets, ensuring each model gets exactly what it needs
without unnecessary computation.

This separation allows different models to access the same domain objects through feature classes while only
requesting the features they need, improving performance and making it easier to track which features each model depends on.

### Defining Named Queries

To define a named query, add a NamedQuery object to your Chalk deployment:

```
from chalk import NamedQuery
from src.models import User

NamedQuery(
    name="fraud",
    input=[User.id],
    output=[
        User.email_age_days,
        User.denylisted,
        User.credit_report.flags,
    ],
    tags=["team:fraud"],
    owner="jodie@chalk.ai",
    description="Primary fraud model for signup"
)
```

Running chalk apply makes the named query available in your deployment.

### Using Named Queries

Named queries can then be leveraged through any of our clients by specifying the query_name parameter.

Using the Chalk CLI tool, this looks something like:

```
chalk query --in user.id=1 --query-name fraud
```

Because a named query has been specified, you don't need to explicitly pass in the tags and outputs
for your query. The above command is equivalent to running the more complicated:

```
chalk query \
  --in user.id=1 \
  --out user.email_age_days \
  --out user.denylisted \
  --out user.credit_report.flags \
  --tag team:fraud
```

This feature is also accessible in all of our API clients through the query_name parameter.
For instance, in Python, you can run:

```
from chalk.client import ChalkClient

ChalkClient().query(
    input={"user.id": 1},
    query_name="fraud",
)
```

You can also run a named query offline, provided that all outputs have offline resolvers.

```
from chalk.client import ChalkClient

ChalkClient().offline_query(
    input={"user.id": 1},
    query_name="fraud",
    recompute_features=True,
)
df = dataset.get_data_as_pandas()
```

To see all the named queries you've defined in your current active deployment, you can run:

```
$ chalk named-query list
<example output>
```

### Versioning Named Queries

If you want to create multiple versions of a similar query, you can use the version
parameter of the NamedQuery object
and the query_name_version parameter of our various clients.

Note, when executing a named query both the query name and the query version must match.
This means that if you've defined two named queries in your codebase:

```
from chalk import NamedQuery
from src.models import User

NamedQuery(
    name="fraud",
    input=[User.id],
    output=[User.denylisted],
)

NamedQuery(
    name="fraud",
    version="1.1.0",
    input=[User.id],
    output=[
        User.email_age_days,
        User.denylisted,
        User.credit_report.flags,
    ],
)
```

And you run the following query:

```
chalk query --in user.id=1 --query-name fraud
```

We will return User.denylisted since the first named query has no version and no version was passed
through query-name-version. To access a version named query, the version must be
explicitly passed. For example:

```
chalk query --in user.id=1 --query-name fraud --query-name-version 1.1.0
```

### Caching ad-hoc query plans

Defining NamedQuery objects is the recommended way to ensure that your queries will be
pre-planned, and that planning time will not impact your query latency. By default, the environment variable
CHALK_PRE_PLAN_NAMED_QUERIES=1 should be set to enable this. However, sometimes
defining NamedQuery objects is not ergonomic or possible. For example, if you are
a platform team serving multiple teams, you may not want to define a NamedQuery object for every
query that your users run.

In this case, you cache ad-hoc query plans by setting the following environment variables:

```
CHALK_STORE_ADHOC_QUERIES=true
CHALK_PLAN_ADHOC_QUERIES=3
```

The first environment variable will cache the ad-hoc query requests in the database. The second
environment variable will plan up to 3 of the most recent ad-hoc queries. These Ad-hoc queries
are re-planned at boot so that code or platform changes can be reflected in the query plan. With
ad-hoc query caching enabled, you can cache the sketch of your most frequent queries without defining
the queries in code.

To fully cache query plans, you can use the Durable Plan Cache. With the Durable Plan Cache, your query plans
are serialized and stored in a cache that persists across pods and deployments. Then, whenever a new pod
spins up, you can configure the number of entries to pre-load into the pod cache from the Durable Plan Cache.
You can configure the Durable Plan Cache with the following environment variables:

```
CHALK_PERSIST_DURABLE_PLAN_CACHE=true
CHALK_PREPOPULATE_DURABLE_PLAN_CACHE=10
CHALK_PREPOPULATE_DURABLE_PLAN_CACHE_DURATION=259200
```

CHALK_PERSIST_DURABLE_PLAN_CACHE enables the Durable Plan Cache. Then, you can choose how to load query plans on new
pods using either CHALK_PREPOPULATE_DURABLE_PLAN_CACHE=k which will load the top k most recent query plans, or
CHALK_PREPOPULATE_DURABLE_PLAN_CACHE_DURATION={DURATION_IN_SECONDS} which will load all query plans created within the
duration of now - timedelta. Generally, the plans will stay consistent across pods and deployments, but if
there are any changes in serialization / deserialization schemes between platform versions, then Chalk will still
plan the named and ad-hoc queries and cache the new plans.

# Authentication
source: https://docs.chalk.ai/docs/online-authentication

## Access the Chalk API.

Chalk implements OAuth for authentication to the online query interface.
Two kinds of credentials can be used to access Chalk resources:

- Personal Credentials: Full access to all resources on your account. This allows a client to act as you.
- Service Credentials: Access scoped to a specific project and environment. Used for computers to talk to Chalk. Generated via the web dashboard.

Both personal and service credentials can be used to query Chalk, and potentially to modify your Chalk deployment's
settings. This means that these credentials are sensitive and must be kept secret.

You can create and manage service credentials in the Chalk dashboard or using the Chalk CLI.
When you use the CLI to create credentials, you will be asked to authenticate yourself on Chalk's web dashboard.
Then, you will receive a client_id and client_secret. Once generated, client_id cannot be changed. However,
client_secret can be rotated if your security practices require this or if you suspect that client_secret has
been compromised.

Once you have generated your client_id and client_secret, you can make authenticated requests to Chalk.

### Authenticating an API client

Chalk has published API client libraries for several languages. These libraries handle exchanging a client_id
and client_secret for an access_token which can be used to access Chalk.

### Authenticating CURL

We recommend using the chalk cli tool to authenticate a curl request. You can use chalk token to acquire an
access_token that is suitable for use as a Bearer token:

```
curl -H "Authorization: Bearer $(chalk token)" \
  https://api.chalk.ai/v1/who-am-i
```

### Fetching an Access Token

If you're implementing a custom API client for a language that Chalk hasn't published a library for, you may need to
fetch an access_token using the OAuth Client Credentials
grant flow. You can use the token endpoint in Chalk's API to execute this flow:

### Request

Your client_id

Your client_secret

The grant_type field must always be "client_credentials".

### Response

The access_token that you should use in the Authorization header for authenticated requests.

Number of seconds until the access_token expires.

This field will always be "Bearer"

### Creating a Service Token in the Dashboard

You can create a service token in the Chalk dashboard by navigating to the "Service Tokens" tab in the "Settings" page.
You can then specify permissions for the token, as well as datasource and feature tags for datasource-based and
feature-based RBAC (Role-Based Access Control), respectively.

Service Token Creation

### Authenticating a Request Using an Access Token

Use the token obtained from the Client Credentials grant flow in the Authorization: Bearer <ACCESS_TOKEN> header
that your client sends along all authenticated requests. For example:

```
curl -H "Authorization: Bearer <ACCESS_TOKEN>" https://api.chalk.ai/v1/who-am-i
```

will return a 200 response and a JSON object containing a short description of the requesting user. This is
convenient for verifying that you are using a valid access_token.

### Role-based access control (RBAC)

Use service credentials to limit your application's access to specific data sources and features.

### Data sources

For data sources, you can provide an allowlist of tags when creating the service credential. Your service credential
will only be allowed to access data sources whose tags match your allowlist.

### Features

For features, Chalk expects a blocklist or allowlist of tags. Features that are not permissible will be excluded from computation. We
make a distinction between features solely used to compute other features and features which are returned as query
output. You can maintain separate permissions for each of these types of features.

### Examples

If we created a service token blocking the tag allow1, then the following features with said tag would not be
computable. If we ran a query with this service token fetching feature feature1 with tag allow1, we would get an
error back indicating that the feature was not accessible:

Feature Definition:

```
@features(tags=["generic"])
class AllowedEvents:
  id: int
  feature1: str = feature(tags=["allow1"])
```

Query:

```
$ chalk query --in allowed_events.id=1 --out allowed_events.feature1

Results:
<query url>

No scalar features

Errors:
Unauthorized allowed_events.feature1

Feature 'allowed_events.feature1' is not authorized for this environment for tag allow1
```

# Query Caching
source: https://docs.chalk.ai/docs/query-caching

## Override default max-staleness for individual requests.

Features may specify a default caching strategy through
the maximum staleness parameter
(see Feature Caching for a more in-depth discussion).

However, a request may have freshness requirements that differ from
the default caching period specified at the feature level.

You can specify maximum staleness requirements for any set of features,
even features you do not wish to return.
This facility may be useful if a feature value is
used as an intermediate result for an explicitly requested feature.

### Example

Consider the following feature definition:

```
@features
class User:
    fico_score: int = feature(max_staleness="**30d**")
    ...
```

For most models, it may be acceptable to use a thirty-day old
version of the FICO score. However, if you were running a
model for issuing a new line of credit,
you may require a more updated version of the feature.

By default, our models will receive a FICO score computed
in the last 30 days, but we can override this behavior
at the time of requesting features for the credit model:

### Handling null and default values in the cache

You can specify whether to cache null or default feature values using the
cache_nulls and cache_defaults
parameters in the feature definition. Additionally, customers with a DynamoDB or
Redis online store can specify feature(cache_nulls="evict_nulls") to evict
any entry that would have been null from the cache, and similarly feature(cache_defaults="evict_defaults") to evict
any entry that would have been a default value from the cache if it exists. For more
information on how to configure these parameters for your use case, check out our
API documentation.

### Cache busting

Cache busting is a special case of overriding the maximum
staleness at the time of making a query.
To bypass the cache, simply provide "0s" as the max-staleness.

# Offline Queries
source: https://docs.chalk.ai/docs/query-offline

## Fetch offline feature values.

Offline queries can pull data from the offline store, or run offline and online
resolvers to compute feature datasets, that can be used for model training, backfilling,
and experimentation.

Offline queries are highly configurable, and can be used for most offline workflows.
In an offline query, you can guarantee temporal consistency by providing input_times,
to fetch the latest values for each feature observed before the input time. You can also
set recompute_features to compute the freshest feature values for some or all output
features, running offline and online resolvers. For offline queries, the query planner
will preference an offline resolver if present, but otherwise will still run online resolvers
to compute feature values.

Offline queries can be used directly for computing feature values to be stored in the online
or offline store, as well as creating datasets that can be used for model training. Providing
a dataset_name in an offline query creates versioned revisions of Datasets, including
metadata about each offline query used to create each revision of a dataset. If an offline
query should be run on a schedule, then the same query can be defined and deployed in code
as a Scheduled Query.

Chalk supports a number of clients for offline queries. In this section, our examples
use our Python client, which integrates with Jupyter notebooks.

### Making offline queries

As mentioned earlier, offline queries can be made through one of Chalk's API clients.

```
from chalk.client import ChalkClient
from datetime import datetime

client = ChalkClient()
dataset = client.offline_query(
  input={'user.id': [1,2,3,4]},         # Input
  output=['user.name'],                 # Output
  # tags=['test'],                      # Environment
  # branch='branch',
  # recompute_features=True,            # Run Resolvers
  # run_asynchronously=True,            # Run Configuration
  # max_samples = 10,
  # lower_bound=datetime(2024, 10, 12), # Bounds
  # upper_bound=datetime(2024, 10, 20),
)
df = dataset.get_data_as_pandas()
```

Offline queries return Chalk Datasets, which we cover in more detail in the
next section. At a high level, Chalk Datasets are flexible wrappers
for the results of your offline query. They can be converted to pandas or polars DataFrames for ease of use
in downstream ML tasks.

### Input

Offline queries can receive input from a DataFrame, mapping, or SQL query.
Regardless of the format, the primary key feature of the feature class must be included in the input.

### DataFrames and mappings as input

The input parameter accepts chalk.DataFrame,
pandas.DataFrame, or a mapping (like a Python dictionary).
DataFrames should include one column for each known feature in the input.
Mappings should map from each feature to a list of its values:

```
input={
    User.id: ['id1', 'id2'],
    User.age: [23, 40]
}
```

### Input times

Timestamps can be passed in the input_times argument.
If none are provided, Chalk will use the current time.

```
input={
    User.id: ['id1', 'id1'],
}
input_times=[datetime.now() - timedelta(days=1), datetime.now() - timedelta(days=2)]
```

### SQL queries as input

offline_query can also take spine_sql_query as an alternative
input parameter for retrieving feature values from your offline data store.

Spine SQL queries are recommended in the following scenarios:

- You want to retrieve data for multiple rows at once. Chalk will compute an efficient query plan for loading multiple
rows of data at once. Chalk will also reuse data between rows where appropriate.
- You want to query from Chalk as your offline data store. You can reduce unnecessary back-and-forth requests by having
Chalk execute the SQL query and handle the result rows directly.
- You want to request features from multiple feature namespaces for each row of output.

Spine SQL queries accept features from multiple feature namespaces as columns of the result. Each column must either
correspond to an existing feature or be included in the output list. For
each referenced feature namespace, the feature namespace's primary key must be included as a column.

The "ts" column is always interpreted as the query execution time for the row. See our documentation on temporal
consistency for more details.

```
# This spine_sql_query queries the table `transactions` in the Snowflake offline store instance.
output = chalk_client.offline_query(
    spine_sql_query=f"""
        SELECT
            t.txn_time AS ts,
            t.seller_id AS "seller.id",
            t.buyer_id AS "buyer.id",
            t.amount AS "txn.amount",
            t.payment_type AS "txn.payment_type"
        FROM transactions AS t
        WHERE t.update_at >= {now - timedelta(days=30)}
    """,
    output=[
        Seller.id,
        Buyer.id,
        Buyer.account_created_date,
        Txn.payment_type,
        # Computed in the seller namespace from the 'seller.id' spine feature.
        Seller.recent_transactions_volume,
        # Computed in the buyer namespace from the 'buyer.id' spine feature.
        Buyer.total_spent_last_30d,
        # Passed through from the SQL query
        Txn.amount,
    ],
)

```

### Output

This argument describes a list of features to sample.

```
output=[
    User.returned_transactions_last_60,
    User.user_account_name_match_score,
    User.socure_score,
    User.identity.has_verified_phone,
    User.identity.is_voip_phone,
    User.identity.account_age_days,
    User.identity.email_age,
]
```

### Recompute features

Users can request that features (or a subset of features) be recomputed by resolvers
at query time instead of sampled from the offline store.
For more information, see recompute_features.

### Timebounds

In some cases, users may not have a list of primary keys to sample with,
and instead would like to see results within a period of time.
The user can then leave the inputs argument empty and supply a
lower bound and an
upper bound along with the requested output features.
The parameter max_samples can also be used to limit the number of rows returned.

```
dataset: Dataset = ChalkClient().offline_query(
     output=[
         User.id,
         User.fullname,
         User.email,
         User.name_email_match_score,
     ],
     lower_bound=datetime.now() - timedelta(days=7),
     upper_bound=datetime.now(),
)
```

### Environment

The user can specify
tags,
environment,
or branch
as parameters to offline_query in the same fashion
as online query.

### Debugging offline queries

Like online queries,
offline queries can be debugged using the explain flag, which logs the query execution plan, and
the store_plan_stages flag, which stores the inputs and outputs of each of the plan stages,
which will be visible in the web dashboard's query detail view.

In addition, the offline query output is a Dataset object that you can inspect
within the dashboard using the Output Explorer. With the Output Explorer you can run SQL queries
on the output to do more testing and validation. More on these and other tips here.

### Running large offline queries

Offline queries that run on a large number of rows require their own compute resources and infrastructure
to ensure they complete and do not contend with resources from other workloads like the engine or branch server.
Chalk handles this by launching a Kubernetes job that runs asynchronously on dedicated compute nodes.
To do so, set the run_asynchronously flag to True in the offline_query method.

```
from chalk.client import ChalkClient

client = ChalkClient()
client.offline_query(
  input={'user.id': range(1_000_000)},
  output=['user.name'],
  run_asynchronously=True,
)
```

If you'd like to adjust the compute or memory resources for the job,
set the resources parameter to a custom ResourceRequests object.
Ensure that the request values are compatible with the resources available on Kubernetes cluster.
By default, asynchronous offline queries will be picked up by a Job Queue Server worker, so the
resource requests can override the Job Queue server configurations.

Another option to consider is to parallelize the computation of the offline query by dividing the input into shards.
If the num_shards parameter is set,
Chalk will split the input into num_shards shards and run each shard in a separate pod.
The num_workers parameter sets the maximum number of pods that can run concurrently.
If the number of shards is large compared to the size of the Kubernetes cluster,
set the num_workers parameter to a smaller number to ensure that Chalk can launch enough pods to run the query.

```
from chalk.client import ChalkClient

client = ChalkClient()
client.offline_query(
  input={'user.id': range(1_000_000)},
  output=['user.name'],
  run_asynchronously=True,
  num_shards=50,
  num_workers=10,
)
```

For the above example, Chalk will split the input spine into 50 shards of 20,000 rows each.
It will then launch jobs for each shard, while not exceeding 10 concurrent pods at once.

If you lose track of the state of a long-running offline query, you'll always be able to retrieve the outputs later.
First, check the offline query dashboard: you'll be able to download all shards of the output,
individually or as a group, there.
You can also retrieve the outputs via Python with the ChalkClient.get_dataset method.
If you pass in a dataset_name when running the offline query, then you can use the dataset name,
otherwise the revision_id for your dataset will use the Query Id from the offline query dashboard
which you can also use to retrieve the dataset in your function call.

```
from chalk.client import ChalkClient

client = ChalkClient()
dataset = client.get_dataset(revision_id="21d9ceb7-c1ef-4c08-a39c-f8381e825a66") # your query id
df = dataset.get_data_as_pandas()
```

### Disk spilling for memory-intensive queries

When an offline query processes more data than can fit in memory, the execution engine
automatically spills intermediate results to local disk rather than failing with an
out-of-memory error. The engine reads the data back as needed to complete the query,
trading some I/O overhead for the ability to handle larger workloads.

Spilling works best when the underlying compute nodes have local NVMe SSDs, which
provide the high throughput needed for fast spill I/O. When you provision your offline
query workers on instance types with local storage, Chalk automatically mounts the SSD
and configures the engine to use it — no manual configuration is required.

Recommended instance types:

| Cloud | Instance families with local NVMe SSDs |
|-------|---------------------------------------|
| AWS | i3, i4i, m5d, m6id, r5d, r6id, c5d, c6id |
| GCP |z3 |
| Azure | Lsv2, Lsv3 |

If you are not using instance types with local SSDs, spilling falls back to the node's
ephemeral storage (the root filesystem). In this case, you should increase the
ephemeral storage request on your offline query workers to ensure there is enough
disk space for spill files. Set this in your resource group configuration:

```
client.offline_query(
  input={'user.id': range(1_000_000)},
  output=['user.name'],
  run_asynchronously=True,
  resources=ResourceRequests(
    cpu="4",
    memory="16Gi",
    ephemeral_storage="50Gi",
  ),
)
```

Without a sufficient ephemeral storage request, Kubernetes may evict the pod if spill
files exceed the default allocation, causing the query to fail.

Spilling only applies to offline queries. Online queries always run entirely in memory
to preserve low-latency serving.

### Optimizing aggregations in offline queries

When computing aggregations over large datasets in offline queries, your offline query may have to perform
computationally expensive joins. To optimize these joins, Chalk provides a planner option use_materialized_offline_query
that you can specify that follows similar bucketing logic to Materialized Windowed Aggregations
used in online queries. When this option is specified, the Chalk engine will bin the events over which you
are aggregating into appropriately sized buckets based on timestamps and feature groupings, compute the
bucket-level aggregations, and then merge the bucket-level aggregations to produce the final result. This
approach can significantly reduce the amount of data that needs to be processed during joins, leading to faster
offline query execution times, but the performance gain is a tradeoff with some loss of precision in the
calculation of the aggregation.

```
from chalk.client import ChalkClient

client = ChalkClient()

ds = client.offline_query(
    inputs={'user.id': big_input_list},
    input_times=big_input_time_list,
    output=[
        User.recent_transactions,
        User.total_spent_last_30d,
        User.recent_spending_score
    ],
    planner_options={
        'use_materialized_offline_query': '1'
    },
)
```

# Datasets
source: https://docs.chalk.ai/docs/datasets

## Persist and evolve offline queries over time

The Chalk Dataset class governs metadata related to offline queries,
supports revisions to queries over time, and enables the easy retrieval
of data from the cloud.

### Datasets from offline query

Dataset instances are obtained by calling ChalkClient.offline_query()
which computes feature values from the offline store.
If inputs are given, the method returns the values corresponding to those inputs.
Otherwise, the method returns a random sample according to the parameter max_samples,
or features from within timebounds specified by lower_bound and upper_bound.

```
from chalk.client import ChalkClient, Dataset
uids = [1, 2, 3, 4]
at = datetime.now()
dataset: Dataset = ChalkClient().offline_query(
     input={
         User.id: uids,
     },
     input_times=[at] * len(uids),
     output=[
         User.id,
         User.fullname,
         User.email,
         User.name_email_match_score,
     ],
     dataset_name='my_dataset'
)

sample_dataset: Dataset = ChalkClient().offline_query(
     output=[
         User.id,
         User.fullname,
         User.email,
         User.name_email_match_score,
     ],
     max_samples=10,
     lower_bound=datetime.now() - timedelta(days=7),
     upper_bound=datetime.now(),
     dataset_name='my_sample'
)
```

Here, we attach a unique name to the Dataset. Whenever we send additional
queries with the same name, a new DatasetRevision instance will be created
and attached to the existing dataset.
If a dataset_name is not given, the output data won't be retrievable beyond the current session.

A Dataset's revisions can be inspected in Dataset.revisions:
they hold useful metadata relating to the offline query job and the data itself.
Be sure to check out Dataset.errors for any errors upon submitting the query.

### Retrieving output data

Since offline queries are not realtime, the Dataset instance returned
is not guaranteed to have the outputs of the query instantaneously.
Thus, loading the data may take some time.

The data can be accessed programmatically by calling
Dataset.get_data_as_pandas(),  Dataset.get_data_as_polars(), or Dataset.get_data_as_dataframe().
If the offline query job is still running, the Dataset will poll the engine until the
results are completed.

```
from chalk.client import ChalkClient, Dataset
uids = [1, 2, 3, 4]
at = datetime.now()
dataset: Dataset = ChalkClient().offline_query(
     input={
         User.id: uids,
     },
     input_times=[at] * len(uids),
     output=[
         User.id,
         User.fullname,
         User.email,
         User.name_email_match_score,
     ],
     dataset_name='my_dataset'
)

pandas_df: pd.DataFrame = dataset.get_data_as_pandas()
polars_df: pl.LazyFrame = dataset.get_data_as_polars()
chalk_df: chalk.features.DataFrame = dataset.get_data_as_dataframe()
```

The file outputs of the query themselves can also be downloaded to a specified directory.

```
from chalk.client import ChalkClient, Dataset
uids = [1, 2, 3, 4]
at = datetime.now()
dataset: Dataset = ChalkClient().offline_query(
     input={
         User.id: uids,
     },
     input_times=[at] * len(uids),
     output=[
         User.id,
         User.fullname,
         User.email,
         User.name_email_match_score,
     ],
     dataset_name='my_dataset'
)
dataset.download_data('my_directory')
```

By default, Dataset instances fetch the output data from their most recent revision.
A specific DatasetRevision's output data can be fetched using the same methods.

```
from chalk.client import ChalkClient, Dataset
uids = [1, 2, 3, 4]
at = datetime.now()
dataset: Dataset = ChalkClient().offline_query(
     input={
         User.id: uids,
     },
     input_times=[at] * len(uids),
     output=[
         User.id,
         User.fullname,
         User.email,
         User.name_email_match_score,
     ],
     dataset_name='my_dataset'
)
for revision in dataset.revisions:
    print(revision.get_data_as_pandas())
```

### Dataset Inputs

Dataset objects also store the inputs for each revision.

```
from chalk.client import ChalkClient, Dataset
uids = [1, 2, 3, 4]
at = datetime.now()
dataset: Dataset = ChalkClient().offline_query(
     input={
         User.id: uids,
     },
     input_times=[at] * len(uids),
     output=[
         User.id,
         User.fullname,
         User.email,
         User.name_email_match_score,
     ],
     dataset_name='my_dataset'
)
df = dataset.get_input_dataframe()
```

### Managing Datasets

### Renaming Datasets

You can rename a dataset from the Chalk dashboard to better organize your datasets or reflect changes in your workflow.

To rename a dataset:

- From the Datasets page under the Offline section in the sidebar, click on a dataset to open its detail page
- Click the Edit button in the page header next to the dataset name
- Enter the new name and click Save, or press Enter

The dataset name is used when retrieving datasets via the API, so update any references in your code after renaming.

### Archiving Dataset Revisions

Archiving a revision cannot be undone. Archived revisions will no longer be accessible via the API.

As datasets accumulate revisions over time, you can archive older or buggy revisions to keep your dataset history organized. Some metadata about your revision will still be accessible through the dashboard but revisions will be permanently inaccessible after archiving.

To archive a revision:

- From the Datasets page under the Offline section in the sidebar, click on a dataset to open its detail page
- Select the Revisions tab
- Select the checkboxes next to all revisions you want to archive
- An Archive button will appear in the actions bar at the top of the page. Click this button and confirm the action in the dialog.

To view archived revisions, check the Include archived revisions checkbox above the revisions table.

Datasets are stored as parquet files in the storage buckets in your cloud. Archiving a revision does not delete the data there—to conserve storage, you can set an expiration policy directly on those buckets.

### Recompute a Dataset

Datasets expose a recompute method
that enables users to see the results of updates to resolvers/features in the context of this dataset.
recompute takes a list of features as an argument to be recomputed,
and any other required input features are sampled from the offline store.

### Integrate Datases into PyTorch

Datasets expose methods create_torch_map_dataset and
create_torch_iter_dataset, which create
PyTorch datasets from the results of the
Chalk dataset.

To learn more, see Chalk's PyTorch Integration with Datasets.

# Pytorch Integration with Datasets
source: https://docs.chalk.ai/docs/pytorch-datasets

## Create PyTorch Datasets from Chalk Datasets

Chalk Datasets expose the following methods, which create
PyTorch datasets from the Chalk dataset's
contents.

- Dataset.create_torch_map_dataset(...), which creates a
map-based PyTorch dataset.
- Dataset.create_torch_iter_dataset(...), which creates an
iterable Pytorch dataset.

These functions can be used to integrate the results of your Chalk query directly with your PyTorch workflows.
Check out the MNIST Dataset Example for example
code that can do this.

These functions will create datasets that return values in pydict format: {"column_name": torch_tensor}. These column
names will by default be the column names of the dataset, but can be mapped by specifying the columns= kwarg in the
above function calls. Note that when using a data loader with a batch_size >= 1, each batch when iterating over the
data loader will give a mapping from column names to tensors of size batch_size.

### Map-based vs Iterable Datasets

In PyTorch, the map-based torch.utils.data.Dataset
and iterable torch.utils.data.IterableDataset
are the two different types of datasets that can be used in DataLoaders.

Map-based datasets are optimized for random access on any given row. In Chalk, Dataset.create_torch_map_dataset(...)
will materialize the entire dataset upon the underlying operation's completion. However, if you do not need random
access on your dataset, it may be more appropriate to use Dataset.create_torch_iter_dataset(...), which will
only materialize one row group of the Chalk dataset at a time by default.

# Metaplanning
source: https://docs.chalk.ai/docs/metaplanning

## Automatic parallelization of scheduled offline queries

Metaplanning is an environment-level feature that automatically parallelizes scheduled offline queries by splitting them into multiple shards that run concurrently.

Contact our support team to enable metaplanning in your environments.

### How It Works

When metaplanning is enabled for your environment, all scheduled offline queries go through a metaplanning workflow:

Example: A query with 100,000 rows and the default target of 10,000 rows per shard creates 10 parallel shard jobs.

### Configuration

Metaplanning is configured at the environment level. Once enabled, all scheduled offline queries in that environment use metaplanning automatically.

The shard size can be controlled via the CHALK_AUTOSHARDER_TARGET_ROWS_PER_SHARD environment variable (default: 10,000 rows per shard).

### Example

```
ScheduledQuery(
    name="daily_user_scores",
    outputs=[User.id, User.score],
    schedule="0 0 * * *",
)
```

With metaplanning enabled, this query will:

- Compute shard keys to find all User IDs (since no input is specified)
- Autoshard the IDs based on the configured target
- Execute all shards in parallel

### See Also

- Query Scheduling - Creating scheduled queries
- ScheduledQuery - API reference
# SQL Interface
source: https://docs.chalk.ai/docs/sql-interface

## Querying Chalk with SQL.

Chalk is testing a direct SQL query interface for your feature values and
data sources in your environment. In the dashboard, under Data Explorer,
you can find several interfaces that you can use to query your data. The
Online Query Explorer and Offline Query Explorer enable you to execute
online queries and offline queries,
respectively, from the dashboard. In addition, you can use the SQL Query
Interface to query against previously computed feature values from your
offline store as well as data sources in your environment.

Additionally, you can use the GRPC client's run_sql() endpoint.

### Query Syntax

Chalk's SQL interface uses a standard SQL dialect, and all queries are processed through a parser that expects
familiar SQL syntax.

Currently, Chalk SQL only supports making SELECT queries, with the following restrictions:

- SELECT list:Column references cannot be qualified yet. If a column in a table has a . delimiter, you may reference it with
double quotes, e.g. SELECT "column.with.dot" FROM table.A subset of Chalk's expressions are automatically exposed as top-level functions in the SQL
interface.
- FROM clause:You can query tables that are exposed by the Chalk catalog. See SQL Interface Sources for more details.You can also query against the following table-valued functionsread_parquet(path: str): Reads a Parquet file from the given path and returns a table. Path must be a literal string.query_values_from_operation_ids(operation_id: str, ...): Returns a table consisting of the values queried in the
given operation id(s). The operation id(s) provided must correspond to queries that have the same output schema.
- WHERE clause:Column references cannot be qualified yet. As such, JOINs are not possible yet.You can use any of the supported expressions available in ChalkSQL as part of your WHERE clause.A best-effort attempt of pushdown is made for the expressions used in the WHERE clause, but not all expressions
are guaranteed to be pushed down to the underlying data source.
- GROUP BY clause:At present, you may only use direct column references in the GROUP BY clause.
- LIMIT clause:You may use the LIMIT clause to limit the number of rows returned by your query. The value must be a literal integer.
- ORDER BY clause:At present, you may only use direct column references in the ORDER BY clause.

### SQL Interface Sources

In the SQL Interface, there exist various schema providers, which all exist under the chalk catalog:

- chalk.datasources: directly query against the data sources configured in your
environment (e.g. Postgres, Snowflake, BigQuery, Iceberg, etc.). Table names are tables within the data sources themselves.Schema: Exactly that of the table in the data source.
- chalk.historical_values: query against historically observed feature values with table names of the form
feature_namespace.feature_name from your offline store, or query for the freshest values for each primary key
for a specific feature namespace with table names feature_namespaceSchema for feature_namespace.feature_name:observation_id, string, non-nullable: The unique identifier for the observation of the feature value.pkey, (type of feature namespace's pkey), non-nullable: The value of the primary feature associated with this
observationvalue, (type of feature namespace's value): The observed value of the feature.value_json, string, DEPRECATED: The observed value of the feature, as JSON, for backwards compatibility.observed_at, timestamp, non-nullable: The time at which the feature value was observed.inserted_at, timestamp, non-nullable: The time at which the feature value was inserted into the offline store.resolver_fqn, string, nullable: The resolver that computed this feature.deployment_id, string, nullable: The deployment id where the observation was madeSchema for feature_namespace:__pkey__: (type of feature namespace's pkey), non-nullable: The value of the primary feature associated with this row<feature-name>, (type of feature), for each feature: The freshest observed value of the feature for the primary key.<feature-name>.__observed_at__, timestamp, for each feature: The time at which the freshest value was observed.
- chalk.query_log:  A schema provider consisting of one table, data, which is the query log table.
This table provides a list of query metadata for each operation id, including which tables in the offline store
correspond to values queried in that operation id.
Schema for data:operation_id, string, non-nullable: The unique identifier for the operation.environment_id, string, non-nullable: The environment id where the operation was run.deployment_id, string: The deployment id where the operation was run.operation_kind, string, The kind of operation that was run (inference, streaming, etc.).query_timestamp, timestamp: The value of now() that was used by the query.execution_started_at, timestamp: The time at which the operation started executing. Null if there were errors during planning.execution_finished_at, timestamp: The time at which the operation finished executing. Null if there were errors during execution.query_status, string: The status of the query (success, error, running, etc.).query_name, string: The query name for named queries, null otherwise.query_name_version, string: The version of the query for named queries, null otherwise.branch_name: string: The branch the query was run on, null if the query was not run on a branch.correlation_id, string: The correlation id for the query, null if the query was not run with a correlation id.value_tables: array of strings: The list of tables in the offline store that correspond to result values from this query.
- chalk.resolvers: Trigger a resolver run and return the outputs of a specific resolver, with additional filtering
based on the SQL query provided. A table exists for every eligible resolver. To run a resolver this way, it must not
take any inputs and return a dataframe consisting of only scalar outputs.
Schema: Exactly that of the resolver.

Chalk also offers a chalk.information_schema that you can query (similar to many other database offerings), and queries such as SHOW TABLES and SHOW SCHEMAS can also be used.

### Examples

If you had the following feature class:

```
@features
class User:
    id: int
    name: str
```

You could query observed feature values for User.name with user.id = 1 by running the following query:

```
SELECT value FROM "chalk.historical_values.user.name" WHERE pkey = 1
```

# Chalk Clients
source: https://docs.chalk.ai/docs/query-basics

## Fetch feature values via online query.

Chalk maintains several client libraries (gRPC) and a REST API for fetching feature values.

### Library support

Chalk maintains libraries in several major languages
for fetching online feature values. If you need support
for a language that we don't support, let us know!
We also support a rest API if you'd like to build your
own.

### REST API

Chalk supports a REST API for querying online features
and exposes this endpoint in several API clients.
When you execute an online query, resolvers
will execute to produce the requested data.
Online query will prioritize running online resolvers over offline resolvers to compute features
if both are possible.

The following endpoint can also be hit with the python ChalkClient by using its query method.
For information on how to authenticate the ChalkClient, check out the section on
authentication.
Read more about the parameters to this method here.

### Request

Input features and values are provided at the time of request.
For example, primary key-value pairs often designate the subset of data returned. Feature inputs
are provided by fully qualified path.  Has many features
are input as lists, and struct features are input as JSON.

An example of passing a user with two credit cards as input:


Outputs are the features that you'd like to compute from the inputs.

Maximum staleness overrides for any output features or intermediate features. See
query caching for more information.

The context object controls the environment and tags
under which a request should execute resolvers:

The environment in which to run the resolvers.
Like resolvers, API tokens can be scoped to an environment.
If no environment is specified in the query,
but the token supports only a single environment,
then that environment will be taken as the scope for executing
the request.

The tags used to scope the resolvers.

The preview deployment id. See
Preview Deployments for more
information.

The query name. See NamedQuery for more details.

If specified, routes to the relevant branch. See
Branches for more
information.

More information on parameters is available here

### Response

The outputs features and any query metadata

The name of the feature requested, eg.

user.identity.has_voip_phone

.

The value of the requested feature. If an error was encountered in resolving this feature, this
field will be empty.

The error code encountered in resolving this feature. If no error occurred, this field is empty.

Metadata pertaining to the feature, including the resolver run and whether the result was a cache hit.

Errors encountered while running the resolvers. Each element in the list is a
ChalkError. If no errors were encountered, this field
is empty.

Metadata related to the query. Returned if 

include_meta
 or 

explain
 is set to 

True
.

The time, expressed in seconds, that Chalk spent executing this query.

The id of the deployment that served this query.

The id of the environment that served this query.

The short name of the environment that served this query. For example: "dev" or "prod".

A unique ID generated and persisted by Chalk for this query. All computed features, metrics, and logs are
associated with this ID. Your system can store this ID for audit and debugging workflows.

At the start of query execution, Chalk computes 'datetime.now()'.
This value is used to timestamp computed features.

Deterministic hash of the 'structure' of the query. Queries that have the same input/output features will
typically have the same hash; changes may be observed over time as we adjust implementation details.

An unstructured string containing diagnostic information about the query execution.
Only included if

explain
 is set to

True
.

### Query Explanation

Chalk offers support for the user for when queries don't work.
The first step is always to check to see the response contains any errors.
Often, the error message will directly point to the failure.

In the case of more complicated queries, queries can be sent with explain=True.
This will return a representation of the query plan in the meta return attribute.
The user can use this information to verify the resolvers and operators ran during execution.
Beware, this will result in slower execution times.

Some queries that involve multiple operations might need additional tracking.
Users can supply store_plan_stages=True to store intermediate outputs at all operations of the query.
This will dramatically slow things down, so use wisely!
These results are visible in the dashboard under the "Queries" page.

For more information, read the ChalkClient docs here.

### Online Query Bulk

Compute feature values for many rows of inputs using online resolvers. This endpoint is similar to the
online query endpoint, but takes in lists of inputs and produces one output per row of inputs.
This is appropriate when you want to fetch the same set of features for many different input primary keys.

The following endpoint can be accessed with the Python ChalkClient by using its query_bulk method.

### Request

The request body should be a binary payload containing:

- A magic string identifier
- Serialized query metadata
- Feature data in Apache Feather format

When using the ChalkClient, this serialization is handled automatically. For direct HTTP usage, the structure is:

- Request inputs are provided as mappings of feature names to lists of values
- Each list should have the same length, representing multiple rows of data

Input features and lists of values. Each key is a feature name (e.g., "user.id") and
each value is a list of values for that feature. All lists must have the same length, where
each element represents one row.

Has-many features are input as lists within each row element,
and struct features (has-one) are input as JSON objects within each row element.

Example with simple, has-one, and has-many features:

```
{
  "user.id": [1, 2],
  "user.name": ["Alice", "Bob"],
  "user.profile": [
    {"age": 30, "city": "NYC"},
    {"age": 25, "city": "SF"}
  ],
  "user.cards": [
    [{"id": "card1"}, {"id": "card2"}],
    [{"id": "card3"}]
  ]
}
```

The features that you'd like to compute from the inputs. Same as online query.

List of timestamps (ISO format) for each row. If provided, the list must match the length
of the input value lists. Each timestamp represents the query time for the corresponding row.

Maximum staleness overrides for any output features or intermediate features.
See query caching for more information.

The context object controls the environment and tags under which requests execute:

The environment in which to run the resolvers.

The tags used to scope the resolvers.

If specified, all required_resolver_tags must be present on a resolver for it to be eligible to execute.

The semantic name for the query, e.g., "loan_application_model". See NamedQuery.

The version of the named query to execute.

A globally unique ID for the query, used in logs and web interfaces.

If specified, routes to the relevant branch.

If specified, routes to the relevant preview deployment.

If true, returns query execution plan in the response metadata. Makes the query slower.

If true, stores intermediate outputs at all query plan stages. Dramatically impacts performance.

Arbitrary key-value pairs to associate with the query.

An immutable context accessible from Python resolvers. See ChalkContext.

### Response

The response is a binary payload in Apache Feather format containing the results.

A list of query results, where each result contains:

A DataFrame containing the scalar feature values for all rows. Each row corresponds to an input row.
Columns are feature names, and values are the computed feature values.

A map of feature names to DataFrames for has-many features.

Errors encountered while running the resolvers.

Metadata about query execution including execution duration, deployment ID, query ID, etc.
See the online query response documentation for QueryMeta details.

### Offline Query

Submit an offline query to compute feature values from the offline store or by running offline/online resolvers.
Offline queries are typically used for generating training datasets and run asynchronously.

The following endpoint can be accessed with the Python ChalkClient by using its offline_query method.
See the offline query documentation for more information.

### Request

The request body is a binary payload containing:

- Serialized query plan (protobuf)
- Query metadata (JSON)
- Input data (Apache Feather format)

When using the ChalkClient, this serialization is handled automatically.

The features for which there are known values. Can be:

- A mapping of feature names to lists of values (similar to bulk query format)
- A DataFrame with input data
- A URI pointing to input data in cloud storage

When using a mapping, has-many features are input as lists within each row,
and struct features (has-one) are input as JSON objects within each row.
See the bulk query input format above for examples.

Timestamps for point-in-time correctness. If a list, must match the length of input rows.
See temporal consistency.

The features to compute or sample. If a feature was never computed for a sample, its value will be null.

Features that must exist in each row. Rows where a required output was never stored will be skipped.

Controls whether resolvers run to compute features:

- If true, all output features are recomputed by resolvers
- If false, all output features are sampled from the offline store
- If a list, features in the list are recomputed, others are sampled

The environment in which to run resolvers.

A unique name for the dataset. If provided, the dataset will be saved and can be retrieved later.

Maximum number of samples to include in the result. If not specified, all samples are returned.

Only query data observed after this timestamp. Accepts ISO 8601 format strings.

Only query data observed before this timestamp. Accepts ISO 8601 format strings.

The tags used to scope the resolvers.

If specified, routes to the relevant branch.

A globally unique ID for the query, used in logs and web interfaces.

The name of the query. If provided, creates a named query or fills in missing parameters from a preexisting execution.

If true, runs the query in separate Kubernetes pods. Useful for large datasets and long-running jobs.

If true, stores the query output in the online store.

If true, stores the query output in the offline store.

If specified, splits the input across this many shards for parallel processing.

Override resource requests (CPU, memory) for the offline query job.

### Response

The response contains information about the submitted offline query job.

A unique identifier for the offline query job. Use this to check the job status.

If a dataset_name was provided, this is the ID of the created dataset.

### Check Offline Query Status

Check the status of an offline query job. Offline queries run asynchronously, so you need to poll
this endpoint to determine when the job is complete and the results are ready.

### Request

The job ID returned from the offline query request (also called revision_id).

The name of the dataset, if one was provided in the offline query request.

The ID of the dataset.

If true, returns results even if some errors occurred during execution. Default is false.

If true, skips failed shards and returns results from successful shards only. Default is false.

You must provide at least one of: job_id, dataset_name, or dataset_id.

### Response

Whether the offline query job has completed. Poll this endpoint until this field is true.

A list of short-lived, authenticated URLs to download the query results. These URLs point to
data files in cloud storage (S3 or GCS) containing the feature values in a columnar format.
Only populated when is_finished is true.

Errors encountered during query execution, if any.

Version number representing the format of the data. The client uses this to properly decode
and load the query results into DataFrames. Current version is 1.

Once is_finished is true, you can download the data from the provided URLs and load it into a DataFrame.
The ChalkClient's Dataset object handles this automatically.

# Model Registry
source: https://docs.chalk.ai/docs/model_registry

## Learn how to track, version, and run ML models in Chalk

With Chalk you can easily register and load machine learning models into your deployments. You can then run inference on these models. This guide covers how to integrate models into your Chalk applications, including loading existing models and running inference.

Chalk has a few key model concepts:

- Model Name: A namespace for a model (which might have multiple implementations).
- Model Version: A model that has been registered with a specific version number—these are models that can be loaded into Chalk deployments.
- Model Artifact: The actual files that make up a model, such as weights, configuration files, and tokenizers.
- Model Reference: A reference to a specific model version. Used to load models into deployments and track model performance and feature distributions for a deployed model.

Generally running inference on models in Chalk involves three steps:

- Registering models in Chalk
- Including models in Chalk deployments
- Connecting your models to features for inference

### Registering Models in Chalk

To add a model to the Chalk model registry, you can either register an existing model or run training code to create a new model. Once registered, models can be versioned and tracked over time. Registering models through training jobs is covered in the Chalk model training docs.

To add a new model namespace to the registry, you can use the client.register_model_namespace method. This namespace can then be used when registering a model version to assign it to this namespace.

```
from chalk.client import ChalkClient

client = ChalkClient()

client.register_model_namespace(
    name="RiskScoreModel",
    description="Risk score model developed in pytorch"
)
```

### Registering Existing Models

Existing machine learning models can be registered in Chalk using the ChalkClient class. You can register models from local files, cloud storage, or directly from Python objects. All of these are supported through the client.register_model_version method.

### Registering From Local Files

To register a model from local files, provide the path to the model files and any additional files needed for inference, such as tokenizers or configuration files.
You'll also want to specify the input and output schema for the model, which helps with validation and integration in your Chalk deployment.

When registering a new model, you can specify a description which will be shown for the Model object in the Chalk dashboard. To register a new
model, you should use the client.register_model_version method. This will create a new model in the registry and add a new model version.

```
from chalk.client import ChalkClient

client = ChalkClient()

client.register_model_version(
    name="RiskScoreModel",
    aliases=["v1.0"],
    model_paths=["./risk_score_model.pth"],
    additional_files=[
        "./tokenizer.json"
    ],
    metadata={
        "framework": "pytorch",
        "training_date": "2025-07-29",
        "performance_metrics": {
            "accuracy": 0.95,
            "f1_score": 0.92
        }
    }
)
```

### Registering From Python Model Objects

Models can also be registered directly from Python objects, such as Scikit-learn or PyTorch models. This allows you to register models directly from your
code without needing to save them to disk first.

```
from chalk.client import ChalkClient
from sklearn.ensemble import RandomForestClassifier

client = ChalkClient()

rfc = RandomForestClassifier()

rfc.fit(X_train, y_train)


# Since the model has already been registered, we can create a new version by calling register_model_version
client.register_model_version(
    name="RiskScoreModel",
    aliases=["v1.0.0"],
    model=rfc,  # Directly pass the model object
    metadata={
        "framework": "sklearn",
        "training_date": "2025-07-29",
        "accuracy": 0.89,
        "precision": 0.91
    },
    input_features=[User.age, User.income],
    output_features=[User.churn_risk],
)
```

### Retrieving Model Information

Registered models are tracked in the Chalk Model Registry. They can be loaded through the client and queried for metadata such as versions and performance metrics.
They can also be viewed in the Chalk Dashboard. If they've been included in a deployment, you will also see feature distributions and model performance over time.

```
# Get model metadata
model = client.get_model(name="RiskScoreModel")
print(f"Latest version: {model.latest_version}")
print(f"Available versions: {model.versions}")

# Get specific version details
model_v1 = client.get_model(name="RiskScoreModel", version=1)
print(f"Performance: {model_v1.metadata['training_metrics']}")
```

### Including Models in Chalk Deployments

To include models in your Chalk deployment, use ModelReference objects. ModelReferences are code-defined objects which should be included in your Chalk code: they are used to connect model versions to model deployments.

```
from chalk.features import features, _
from chalk.ml import ModelReference
from chalk import functions as F
from chalk import make_model_resolver

# Load a model into the deployment
churn_risk = ModelReference.from_version(
    name="ChurnModel",
    version=2,
)

@features
class User:
    id: int
    age: int
    income: float

    churn_risk: float # define the prediction feature

resolver = make_model_resolver(
    name="churn_model_prediction",
    model=churn_risk,
    input=[User.age, User.income],
    output=[User.churn_risk],
)
```

Once the model is deployed, metrics for the model will be tracked in the Chalk dashboard, including feature distributions and
performance over time.

### Running Inference on Models

Once models are registered and loaded into your deployment, you can run inference on your models:

```
from chalk.features import feature, features, _
from chalk.ml import ModelReference
from chalk import functions as F
from chalk import make_model_resolver

# Load a model into the deployment using alias
risk_model_latest = ModelReference.from_alias(
    name="RiskScoreModel",
    alias="latest",
)

# Load a model into the deployment using version
risk_model_v1_0_0 = ModelReference.from_version(
    name="RiskScoreModel",
    version=1,
)

# Reference the loaded model(s) in inference
@features
class User:
    id: int
    age: int
    income: float
    risk_score: float = feature(versions=2) 

make_model_resolver(
    name="user_risk_score_v1_prediction",
    input=[User.age, User.income],
    output=[User.risk_score@1]
)

make_model_resolver(
    name="user_risk_score_v2_prediction",
    input=[User.age, User.income],
    output=[User.risk_score@2]
)
```

# Model Training
source: https://docs.chalk.ai/docs/model_training

## Learn how to train ML models in Chalk

Chalk provides single node and distributed training capabilities that leverage your existing feature infrastructure
and generate Model Artifacts. These Model Artifacts can be registered into the Model Registry

### Training Overview

Chalk supports two primary training approaches:

- Single-Node Training: For smaller datasets that fit in memory on a single machine
- Distributed Training: For large-scale datasets that require distributed processing across multiple workers

Both approaches integrate seamlessly with your existing Chalk feature infrastructure and automatically register trained models in the Model Registry
and can be run from a Jupyter notebook or as part of a CI/CD pipeline. In this tutorial, we cover both training methods run through a jupyter notebook:

### Single-Node Training

Single-node training is ideal for smaller datasets that can fit comfortably in memory. This approach is simpler to set up and debug, making it perfect for experimentation and smaller production workloads.

### Basic Training Setup

Here's a complete example of single-node training with PyTorch. Use thechalk_train module for checkpointing and
accessing Chalk datasets.

```
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.feature_extraction.text import TfidfVectorizer

import chalk.ml.train as chalk_train


class SpamClassifier(nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.fc = nn.Sequential(nn.Linear(input_size, 32), nn.ReLU(), nn.Linear(32, 2))

    def forward(self, x):
        return self.fc(x)


# Define the preprocessing and data loading code
def preprocess_data(dataset_name: str, config: dict):
    # Use Chalk Train to Load Dataset for Training
    df = chalk_train.load_dataset(dataset_name=dataset_name).to_pandas()

    data = df[['sms_spam.content']]
    labels = df['sms_spam.label'].map({'ham': 1, 'spam': 0}).values

    tfidf = TfidfVectorizer(max_features=50)

    X = torch.tensor(tfidf.fit_transform(data).toarray(), dtype=torch.float32)
    y = torch.tensor(labels, dtype=torch.long)

    dataset = TensorDataset(X, y)
    dataloader = DataLoader(dataset, batch_size=config["batch_size"], shuffle=True)
    return dataloader, X.shape[1]


# Define the training code for the model
def train(config: dict):
    dataloader, input_size = preprocess_data(dataset_name=config['dataset_name'], config=config)
    model = SpamClassifier(input_size)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=config["lr"])

    for epoch in range(config["num_epochs"]):
        total_loss = 0
        correct = 0
        total = 0

        for batch_X, batch_y in dataloader:
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == batch_y).sum().item()
            total += batch_y.size(0)

        if epoch % 5 == 0:
            accuracy = correct / total

            print(f"Epoch {epoch}: Loss={total_loss/len(dataloader):.3f}, Acc={accuracy:.3f}")

            chalk_train.checkpoint(
                model,
                metadata=dict(
                    accuracy=accuracy,
                    epoch=epoch,
                )
            )
```

Once your train model is defined, you can run a training job using the client.train_model method:

```
from chalk import ResourceRequests

# Create a training run
training_run = client.train_model(
    experiment_name="spam_model",
    train_fn=train,
    config=dict(
        lr=0.01,
        num_epochs=50,
        batch_size=32,
        dataset_name="sms_spam_dataset"
    ),
    resources=ResourceRequests(
        cpu=15,
        memory="15Gi",
        resource_group="gpu"
    )
)
```

If you've defined a resource group with GPU access, you can also leverage this for training by specifying the appropriate resource group.

### Next Steps

After training your models, you can:

- Register Models: Use the Model Registry to version and track your trained models
- Deploy Models: Load models into Chalk deployments for inference
- Monitor Performance: Track model performance and feature distributions over time
- Iterate: Use the training infrastructure to experiment with new architectures and hyperparameters
# LLM Toolchain
source: https://docs.chalk.ai/docs/chalk-for-ai-engineers

## Easily integrate unstructured data, build context-aware prompts, and run LLM evaluations at scale with Chalk.

Chalk's LLM toolchain enables you to build enterprise-grade AI applications without stitching together LLMs, prompts, vector DBs, and retrieval logic:

- Call chat completion APIs out-of-the-box
- Cache expensive computations to avoid redundant processing and reduce latency
- Retrieve real-time context into LLMs
- Generate embeddings and vectors within pipelines
- Reuse and manage prompts with named prompts
- Run large-scale evaluations using historical traffic to compare prompt variants

Chalk provides a full-stack solution but can also integrate seamlessly with your current infrastructure.
For instance, you can use an existing vector DB to store and retrieve your embeddings, while leveraging Chalk to evaluate new models and prompts.
Chalk lets you integrate only the pieces you need:

```
import chalk.functions as F
import chalk.prompts as P
from chalk.features import DataFrame, Primary, Vector, embed, features, has_many, _
from pydantic import BaseModel

# Use structured output to easily incorporate unstructured data in our ML pipelines
class AnalyzedReceiptStruct(BaseModel):
    expense_category: ExpenseCategoryEnum
    business_expense: bool
    loyalty_program: str
    return_policy: int

@features
class Transaction:
    id: int
    merchant_id: Merchant.id
    merchant: Merchant
    receipt: Receipt

    llm: P.PromptResponse = P.completion(
        model="gpt-5.1-2025-11-13",
        messages=[P.message(
                role="user",
                content=F.jinja(
            """Analyze the following receipt:
            Line items: {{Transaction.receipt.line_items}}
            Merchant: {{Transaction.merchant.name}} {{Transaction.merchant.description}}""")
        )],
        output_structure=AnalyzedReceiptStruct,
    )

    # cache forever since transaction is finalized
    expense_category: str = features(
        max_staleness="infinity",
        expression=F.json_value(
            _.llm.response, # from LLM
            "$.expense_category",
        ),
    )
    # or configure the chat completion from your Chalk dashboard
    llm_call_with_named_prompt: P.run_prompt("analyze_receipt-v1")

@features
class ProductRec:
    user_id: Primary[User.id]
    user: User

    # generate embeddings
    user_vector: Vector = embed(
        input=F.array_join(F.array_agg(
            _.user.products[
                _.name,
                _.type == "liked"
            ]),
            delimiter=" || ",
        ),
        provider="vertexai",
        model="text-embedding-005",
    )

    # do a vector search with the generated embedding
    similar_users: DataFrame[User] = has_many(
      lambda: ProductRec.user_vector.is_near(
            User.liked_products_vector
        )
    )
```

Chalk eliminates the complexity of orchestrating data and ETL pipelines by building a dependency graph (DAG) of your features, which are defined using Python.
At inference time, Chalk dynamically builds query plans (subgraphs of your feature DAG) without manual configuration, based on the features you request.
The (structured) outputs of chat completions are treated as just newly computed features and can feed into other feature computations until all of the features requested are computed.

Chalk for AI engineers

### Call chat completion APIs out-of-the-box with Chalk's Completion function

Use Chalk’s P.completion function to call LLMs from within your feature classes.
Easily create structured LLM responses with full control over model selection, prompt construction, and output formatting.

Combined with F.jinja templates, you can dynamically inject relevant feature values into your prompts for context-aware responses.

```
@features
class Transaction:
    llm: P.PromptResponse = P.completion(
        model="gpt-5.1-2025-11-13",
        messages=[...],
    )
```

P.completion accepts a range of parameters for fine-tuning your LLM interactions, including:

- Model selection
- Temperature control for output randomness
- Token limits
- Structured output formatting via Pydantic models
- Various provider-specific settings

You can also set timeout values, retry logic, and custom stop sequences to build the exact experience your application requires.
Visit our API documentation for a complete reference of all available parameters.

After executing a completion, Chalk returns a P.PromptResponse object that encapsulates the complete interaction, including:

- response: the model's generated text
- prompt: the original prompt for context
- usage: token usage and cost metrics
- runtime_stats: execution timing data to help you monitor and optimize your model interactions

```
class PromptResponse(BaseModel):
    response: Optional[str] = Field(
        description="Response from the model. Raw string if no output structure specified, json encoded string otherwise. `None` if the response was not received or incorrectly formatted."
    )
    prompt: Prompt
    usage: Usage
    runtime_stats: RuntimeStats
```

After receiving a response from an LLM via Chalk's completion function, you can easily extract specific fields from the structured response using F.json_value.
The extracted LLM-generated values become referenceable like ordinary features:

```
@features
class Transaction:
    id: int
    llm: P.PromptResponse
    expense_category: str = F.json_value(
        _.llm.response, # from LLM
        "$.expense_category",
    )
```

You can also compose multimodal prompts — combining image and text in a single call using P.completion(...).
This unlocks image analysis workflows like receipt or PDF parsing with minimal code.

```
@features
class Receipt:
   image_url: str
   image_response: P.MultimodalPromptResponse = P.completion(
       model="gpt-5.1",
       messages=[
           P.message(
               "user",
               [
                   {"type": "input_text", "text": "describe this image"},
                   {"type": "input_image", "image_url": _.image_url},
               ],
           ),
       ],
   )
```

Chalk's LLM toolchain streamlines the entire experience of working with language models by providing:

- Direct access to LLM providers without managing API keys, request formatting, or response parsing
- A consistent API interface regardless of which LLM provider you're using
- Automatic tracking of token usage, costs, and performance metrics
- Built-in error handling with automatic retries without additional code
- Easy extraction of fields from LLM responses for direct use as features
- Seamless integration with Chalk's feature system for dynamic data incorporation through F.jinja

### Cache expensive computations to avoid redundant processing and reduce latency with Chalk's max_staleness setting

Chalk makes it easy to cache features.
This is done by setting the max_staleness of a feature, which lets you specify how old a cached feature value can be before it must be recomputed.
This gives you full control in balancing freshness and performance requirements.

You can specify cache duration in multiple ways:

| Value | Description |
|-------------------|-------------|
| "30d" "1h" "15m" | Natural language strings |
| timedelta(hours=1) | Python timedelta objects |
| "infinity" | Permanent caching for immutable data |

These settings can be overridden at query time for additional flexibility.

```
@features
class User:
    id: int
    # from API or 3rd-party client
    credit_score: int = features(
        max_staleness="30d",
    )

@features
class Transaction:
    id: int
    llm: P.PromptResponse

    # cache forever since transaction is finalized
    expense_category: str = features(
        max_staleness="infinity",
        expression=F.json_value(
            _.llm.response, # from LLM
            "$.expense_category",
        ),
    )
```

### Retrieve real-time context to give LLMs with Chalk's Jinja function

Chalk's F.jinja function lets you build prompts with live data.
Feature values are accessed with the jinja double curly brace sytanx: {{ feature_name }}.

```
F.jinja(
    """Analyze the following receipt:
    Line items: {{Transaction.receipt.line_items}}
    Merchant: {{Transaction.merchant.name}} {{Transaction.merchant.description}}"""
)
```

Benefits of using Jinja for LLM prompting:

- Improve performance by dynamically incorporating real-time data from Chalk features
- Reduce token usage by only including relevant context in your prompts
- Iterate on prompts faster with a structured template system that allows quick experimentation while maintaining consistency across team workflows

### Generate embeddings and vectors within pipelines with Chalk's embed function

Convert structured or unstructured data into embeddings with one line.

Chalk's embedding function automatically converts your features into vector embeddings for similarity search, etc. with built-in support for popular embedding models.
Running in your VPC gives you quick and secure access to models like Bedrock and Gemini with minimal overhead and configuration, as Chalk abstracts away connecting to model providers.

```
@features
class ProductRec:
    user_id: Primary[User.id]
    user: User

    bio_embeddings: Vector = embed(
        input=lambda: ProductRec.user.bio,
        provider="vertexai",
        model="text-embedding-005",
    )
```

When using Chalk's built-in embedding functions, the vector dimensions don't need to be specified, as Chalk will automatically infer it from the embedding model.

### Reuse and manage prompts with Chalk's named prompts

You can define named prompts directly from your Chalk dashboard to help maintain consistency in your LLM workflows.
This centralized approach makes prompts more maintainable and reusable across your application, while also allowing you to change your prompts and model providers without needing to redeploy Chalk.

```
@features
class Transaction:
    id: int
    merchant_id: Merchant.id
    merchant: Merchant
    receipt: Receipt

    # or configure the chat completion from your Chalk dashboard
    llm_call_with_named_prompt: P.PromptResponse = P.run_prompt("analyze_receipt-v1")
```

The P.run_prompt() function provides a clean syntax for connecting your feature classes to a named prompt.

You can edit prompt templates directly from your Chalk dashboard and test features with different prompts without changing any code, making iteration and refinement much faster.

### Run large-scale evaluations using historical traffic with Chalk's feature store for realistic offline testing

Chalk prompt evaluations provide systematic comparison of prompt variants against historical datasets, supporting customizable metrics, reference outputs, and distributed processing for large-scale prompt experimentation.
Built-in evaluators like "exact_match" measure accuracy against reference outputs, while custom evaluation expressions allow for domain-specific metrics tailored to your application needs.

```
eval_run = chalk_client.prompt_evaluation(
    dataset_name="sentiment_gt",
    evaluators=["exact_match"],
    reference_output="user.actual_sentiment",
    prompts=[
        "analyze_sentiment-v1",
        "analyze_sentiment-v2",
        P.completion(
            model="gpt-5.1",
            messages=[
                P.message(role="system", content=system_message),
                P.message(role="user", content=user_message),
            ],
        ),
    ]
)
eval_run.to_pandas()
```

Benefits of leveraging a feature store for evaluation:

- Test against historical traffic and usage patterns from your production environment
- Identify edge cases and failure modes before they affect real users
- Run thousands of evaluations in parallel without impacting live systems

View your eval results from the Chalk dashboard to track important metrics such as accuracy, average tokens, P50 latency, and P99 latency.

# Getting Started
source: https://docs.chalk.ai/docs/chalkdf/getting-started

## Install and run your first chalkdf commands

This guide will walk you through installing chalkdf and performing some basic operations.
If you are new to chalkdf or DataFrame libraries, this is a great place to start. If you
are already familiar with DataFrame libraries you can skip ahead to the full
Reference Library or the installation guide

### Installation

Given Python 3.10-3.13 and Linux/macOS 15+, you can install chalkdf via pip:

```
uv pip install "chalkdf[chalkpy]"
```

### Reading Data

chalkdf supports reading data from several formats and sources, including JSON, CSV, and Parquet files,
Arrow objects and tables, as well as AWS Glue Iceberg tables, and SQL sources defined via
chalkpy.

Below we can initialize a chalkdf.DataFrame from a Python dictionary.

```
from chalkdf import DataFrame

df = DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "city": ["New York", "Los Angeles", "Chicago"],
    }
)

df.run()
```

```
DataFrame(materialized 3 rows x 3 columns)
┌─────────┬───────┬─────────────┐
│ name    ┆ age   ┆ city        │
│ ─────── ┆ ───── ┆ ─────────── │
│ string  ┆ int64 ┆ string      │
╞═════════╪═══════╪═════════════╡
│ Alice   ┆ 25    ┆ New York    │
│ Bob     ┆ 30    ┆ Los Angeles │
│ Charlie ┆ 35    ┆ Chicago     │
└─────────┴───────┴─────────────┘
```

You can also scan files directly into a DataFrame. Below, we scan a CSV file:

```
from chalkdf import DataFrame
import pyarrow as pa

df = DataFrame.scan(
    "people",
    ['people.csv'],
    schema=pa.schema([
        ('name', pa.string()),
        ('birthday', pa.date32()),
        ('occupation', pa.string())
    ])
)
df.run()
```

```
DataFrame(materialized 3 rows x 3 columns)
┌───────────────┬─────────────┬───────────────────┐
│ name          ┆ birthday    ┆ occupation        │
│ ───────────── ┆ ─────────── ┆ ───────────────── │
│ string        ┆ date32[day] ┆ string            │
╞═══════════════╪═════════════╪═══════════════════╡
│ Alice Chen    ┆ 1990-03-15  ┆ Software Engineer │
│ Bob Smith     ┆ 1985-07-22  ┆ Teacher           │
│ Carol Johnson ┆ 1992-11-08  ┆ Data Analyst      │
└───────────────┴─────────────┴───────────────────┘
```

### DataFrame Expressions

DataFrame expressions allow you to transform and explore your data through a variety of operations.
For example, given a DataFrame of values with id's, you could group the values by id and compute the
aggregate sum. We use the underscore notation _ to reference the current DataFrame, to easily
access columns without any additional wrappers. You can import _ from the chalk module.

```
>>> from chalk import _
>>> df.run()

DataFrame(materialized 5 rows x 2 columns)
┌───────┬───────┐
│ id    ┆ value │
│ ───── ┆ ───── │
│ int64 ┆ int64 │
╞═══════╪═══════╡
│ 1     ┆ 10    │
│ 1     ┆ 20    │
│ 2     ┆ 1     │
│ 2     ┆ 2     │
│ 2     ┆ 3     │
└───────┴───────┘
```

```
>>> from chalk.features import _
>>> grouped = df.agg(["id"], _.value.sum().alias("value_sum_by_id"))
>>> grouped.run()

DataFrame(materialized 2 rows x 2 columns)
┌───────┬─────────────────┐
│ id    ┆ value_sum_by_id │
│ ───── ┆ ─────────────── │
│ int64 ┆ int64           │
╞═══════╪═════════════════╡
│ 1     ┆ 30              │
│ 2     ┆ 6               │
└───────┴─────────────────┘
```

Below are some common operations you can use to construct DataFrame expressions.

### select

DataFrame.select allows you to extract specific columns from a DataFrame.

```
>>> interactions = df.select("user_id", "item_id", "interaction_type", "timestamp")
>>> interactions.run()

DataFrame(materialized 5 rows x 4 columns)
┌──────────┬───────────┬──────────────────┬─────────────────────┐
│ user_id  ┆ item_id   ┆ interaction_type ┆ timestamp           │
│ ──────── ┆ ───────── ┆ ──────────────── ┆ ─────────────────── │
│ string   ┆ string    ┆ string           ┆ timestamp[us]       │
╞══════════╪═══════════╪══════════════════╪═════════════════════╡
│ user_001 ┆ item_4521 ┆ click            ┆ 2024-11-08 14:23:15 │
│ user_002 ┆ item_8832 ┆ purchase         ┆ 2024-11-08 15:10:42 │
│ user_003 ┆ item_1203 ┆ view             ┆ 2024-11-08 16:05:30 │
│ user_004 ┆ item_4521 ┆ add_to_cart      ┆ 2024-11-08 17:45:12 │
│ user_005 ┆ item_9944 ┆ click            ┆ 2024-11-08 18:20:05 │
└──────────┴───────────┴──────────────────┴─────────────────────┘
```

### with_columns

To add new columns or modify existing columns in your DataFrame while retaining all original
columns, you can use DataFrame.with_columns.

```
>>> from chalk import _
>>> processed_interactions = df.with_columns({"user_id": _.user_id, "long_session": _.session_duration_sec > 180})
>>> processed_interactions.select("user_id", "session_duration_sec", "long_session").run()

DataFrame(materialized 5 rows x 3 columns)
┌──────────┬──────────────────────┬──────────────┐
│ user_id  ┆ session_duration_sec ┆ long_session │
│ ──────── ┆ ──────────────────── ┆ ──────────── │
│ string   ┆ int64                ┆ bool         │
╞══════════╪══════════════════════╪══════════════╡
│ user_001 ┆ 145                  ┆ False        │
│ user_002 ┆ 320                  ┆ True         │
│ user_003 ┆ 78                   ┆ False        │
│ user_004 ┆ 210                  ┆ True         │
│ user_005 ┆ 167                  ┆ False        │
└──────────┴──────────────────────┴──────────────┘
```

### project

To define more complex transformations without retaining all original columns, you can use DataFrame.project to take
in a DataFrame as input and project to new columns based on provided expressions. In these expressions, you can use the
underscore notation _ to reference columns within your source DataFrame, and utilize the chalk.functions
library (typically imported as F) for a variety of operations.

```
from chalk import functions as F, _
from chalkdf import DataFrame
import pyarrow as pa

tbl = pa.table(
  {
    "txns_last_hour": [[1, 2, 3, 4, 5], [100], [200, 201]],
    "max_txns_allowed": [3, 5, 4],
  }
)

df = DataFrame.from_arrow(tbl)

out = df.project(
  {
    "velocity_score": _.txns_last_hour
      .cardinality()
      .cast(float)
      .least(_.max_txns_allowed + 0.5)
      .ceil()
      .cast(int),
    "velocity_score_2": F.cast(
      F.ceil(
        F.least(
          F.cast(F.cardinality(_.txns_last_hour), float),
          _.max_txns_allowed + 0.5
        )
      ),
      int,
    ),
  }
)
out.run()
```

```
DataFrame(materialized 3 rows x 2 columns)
┌────────────────┬──────────────────┐
│ velocity_score ┆ velocity_score_2 │
│ ────────────── ┆ ──────────────── │
│ int64          ┆ int64            │
╞════════════════╪══════════════════╡
│ 4              ┆ 4                │
│ 1              ┆ 1                │
│ 2              ┆ 2                │
└────────────────┴──────────────────┘
```

### filter

You can filter rows in a DataFrame using DataFrame.filter, which takes in a boolean expression.

```
>>> from chalk import _
>>> df.run()

DataFrame(materialized 5 rows x 7 columns)
┌──────────┬───────────┬──────────────────┬─────────────────────┬────────┬─────────────┬──────────────────────┐
│ user_id  ┆ item_id   ┆ interaction_type ┆ timestamp           ┆ score  ┆ category    ┆ session_duration_sec │
│ ──────── ┆ ───────── ┆ ──────────────── ┆ ─────────────────── ┆ ────── ┆ ─────────── ┆ ──────────────────── │
│ string   ┆ string    ┆ string           ┆ timestamp[us]       ┆ double ┆ string      ┆ int64                │
╞══════════╪═══════════╪══════════════════╪═════════════════════╪════════╪═════════════╪══════════════════════╡
│ user_001 ┆ item_4521 ┆ click            ┆ 2024-11-08 14:23:15 ┆ 0.85   ┆ electronics ┆ 145                  │
│ user_002 ┆ item_8832 ┆ purchase         ┆ 2024-11-08 15:10:42 ┆ 0.92   ┆ fashion     ┆ 320                  │
│ user_003 ┆ item_1203 ┆ view             ┆ 2024-11-08 16:05:30 ┆ 0.67   ┆ home        ┆ 78                   │
│ user_004 ┆ item_4521 ┆ add_to_cart      ┆ 2024-11-08 17:45:12 ┆ 0.78   ┆ electronics ┆ 210                  │
│ user_005 ┆ item_9944 ┆ click            ┆ 2024-11-08 18:20:05 ┆ 0.81   ┆ sports      ┆ 167                  │
└──────────┴───────────┴──────────────────┴─────────────────────┴────────┴─────────────┴──────────────────────┘
```

```
>>> df.filter(_.score > 0.8).run()

DataFrame(materialized 3 rows x 7 columns)
┌──────────┬───────────┬──────────────────┬─────────────────────┬────────┬─────────────┬──────────────────────┐
│ user_id  ┆ item_id   ┆ interaction_type ┆ timestamp           ┆ score  ┆ category    ┆ session_duration_sec │
│ ──────── ┆ ───────── ┆ ──────────────── ┆ ─────────────────── ┆ ────── ┆ ─────────── ┆ ──────────────────── │
│ string   ┆ string    ┆ string           ┆ timestamp[us]       ┆ double ┆ string      ┆ int64                │
╞══════════╪═══════════╪══════════════════╪═════════════════════╪════════╪═════════════╪══════════════════════╡
│ user_001 ┆ item_4521 ┆ click            ┆ 2024-11-08 14:23:15 ┆ 0.85   ┆ electronics ┆ 145                  │
│ user_002 ┆ item_8832 ┆ purchase         ┆ 2024-11-08 15:10:42 ┆ 0.92   ┆ fashion     ┆ 320                  │
│ user_005 ┆ item_9944 ┆ click            ┆ 2024-11-08 18:20:05 ┆ 0.81   ┆ sports      ┆ 167                  │
└──────────┴───────────┴──────────────────┴─────────────────────┴────────┴─────────────┴──────────────────────┘
```

### agg

To compute aggregations over groups of data, you can use DataFrame.agg.

```
>>> processed_interactions.agg(
...    ["long_session"],
...    processed_interactions.column("score").mean().alias("avg_score")
... ).run()

DataFrame(materialized 2 rows x 2 columns)
┌──────────────┬───────────┐
│ long_session ┆ avg_score │
│ ──────────── ┆ ───────── │
│ bool         ┆ double    │
╞══════════════╪═══════════╡
│ False        ┆ 0.776667  │
│ True         ┆ 0.85      │
└──────────────┴───────────┘
```

### join

You can combine data from multiple DataFrames using DataFrame.join. Below is an example of joining two
DataFrames using an inner join on the user_id column. You can also specify right and left joins.

```
>>> txns_df.join(
...    users_df,
...    on=["user_id"],
...    how="inner"
... ).select(
...    "transaction_id",
...    "user_id",
...    "name",
...    "amount",
...    "tier",
...    "status"
... ).run()

DataFrame(materialized 5 rows x 6 columns)
┌────────────────┬──────────┬─────────┬────────┬─────────┬───────────┐
│ transaction_id ┆ user_id  ┆ name    ┆ amount ┆ tier    ┆ status    │
│ ────────────── ┆ ──────── ┆ ─────── ┆ ────── ┆ ─────── ┆ ───────── │
│ string         ┆ string   ┆ string  ┆ double ┆ string  ┆ string    │
╞════════════════╪══════════╪═════════╪════════╪═════════╪═══════════╡
│ txn_101        ┆ user_001 ┆ Alice   ┆ 49.99  ┆ premium ┆ completed │
│ txn_102        ┆ user_002 ┆ Bob     ┆ 19.99  ┆ basic   ┆ completed │
│ txn_103        ┆ user_001 ┆ Alice   ┆ 89.5   ┆ premium ┆ pending   │
│ txn_104        ┆ user_003 ┆ Charlie ┆ 120    ┆ premium ┆ completed │
│ txn_105        ┆ user_001 ┆ Alice   ┆ 15.75  ┆ premium ┆ completed │
└────────────────┴──────────┴─────────┴────────┴─────────┴───────────┘
```

# Installation
source: https://docs.chalk.ai/docs/chalkdf/installation

## Install chalkdf to access DataFrame utilities.

chalkdf is a DataFrame library that provides utilities for building fast, portable data pipelines
on top of Apache Arrow--powered by Chalk's libchalk execution engine.

### Installation

To install chalkdf, check the following requirements:

- Python 3.10-3.13
- Linux/macOS 15+

Install from PyPI:

```
pip install "chalkdf[chalkpy]"
```

Alternatively, download platform-specific wheels directly from PyPI.

# Chalk SQL
source: https://docs.chalk.ai/docs/chalksql/what-is-chalk-sql

Chalk SQL is dialect of SQL developed within Chalk built to create federated queries across a
Chalk environment. Chalk SQL is a highly efficient, easy-to-write, and expressive language that enable:

- Querying across multiple SQL sources seamlessly
- Introspecting the online and offline store, datasets from
offline queries, and many other entities across the Chalk ecosystem
- Applying functions from the Chalk Function registry in ad-hoc contexts.
- Integrating with existing online and offline query paths
as a new form of input.

```
WITH total_spending AS (
    SELECT
        u.user_id AS user_id,
        SUM(t.amount) AS user_spending,
    FROM "my_postgres.public.user" u  -- Query against a data source named "my_postgres"
    LEFT JOIN "my_bigquery.my_dataset.transactions" t -- Query against a data source named "my_bigquery"
    ON u.user_id = t.user_id
    GROUP BY u.user_id
)
SELECT
    u.user_id AS user_id,
    u.embedding AS user_embedding,
    array_normalize(u.embedding, 2) AS l2_normalized_embedding,
    json_extract(ts.random_transaction_data, '$.timestamp') AS txn_timestamp,
    json_extract(ts.random_transaction_data, '$.metadata.country') AS country,
    ts.user_spending AS user_spending,
FROM "my_postgres.public.users" u
LEFT JOIN total_spending ts
ON u.user_id = ts.user_id
```

### The Basics

Chalk SQL comprises three main components to both plan and run queries:

- A custom-built transpiler from a dialect of SQL to Chalk's internal planning system.
- Chalk's existing infrastructure to execute plans at blazing speeds, which allows Chalk SQL to benefit from
as Native SQL drivers, static compilation of expressions, and integration with Velox,
the open-source low-latency execution engine.
- The Chalk Catalog, which is a culmination of various objects within a Chalk deployment. This includes
features, resolvers,
datasets, the online and offline store,
and registered SQL sources.

A Chalk Catalog exists per deployment, meaning that as an environment changes over time through feature engineering,
the Chalk Catalog will also update to reflect the newest changes. This means there's no additional work to sync the
catalog to pick up changes: if an additional resolver is added to a deployment, the Chalk Catalog will automatically
know about it, and Chalk SQL can make queries against it.

### Referencing the Chalk Catalog

The Chalk Catalog is organized much like a traditional relational database. Primarily, objects are classified
under the three-level namespacing of CATALOG.SCHEMA.TABLE. Chalk Catalog tables are primarily views, meaning
that they are not materialized in memory like a conventional database table. These views exist over the various
components of the Chalk Catalog

When referencing these tables in your queries to Chalk SQL, you must fully qualify their name.
For example, if you wish to query the keys table in the online_store schema within the chalk catalog,
you should make queries like the following.

```
SELECT * FROM "chalk.online_store.keys";
```

You can learn more about available catalogs, schemas, and tables via the
Database Explorer,
or by making queries to Chalk's INFORMATION_SCHEMA.

```
-- Example query to find all schemas available in the "chalk" catalog
SELECT * FROM chalk.information_schema.schemas WHERE catalog_name = 'chalk';
```

### Running Chalk SQL

Chalk SQL is automatically enabled and available for use in any environment that has at least one
gRPC query server running. Both new and existing environments can start running Chalk SQL queries with no additional
setup.

Chalk SQL is primarily run in two different contexts:

- Ad-hoc Chalk SQL queries stand alone and are useful for introspection or workflows that aren't directly adjacent
to the main query path. These can be run via the CLI, via the Python
SDK's GRPC Client, or via the SQL Explorer, Chalk's
built-in SQL console on the dashboard.
- Chalk SQL can be used as a replacement to the inputs field in online and offline query. Learn more about using
Chalk SQL as inputs to traditional chalk queries here.

### Further Readings

- Example workflows
- Chalk Catalog Components
- Chalk SQL as query inputs
# Example Chalk SQL Workflows
source: https://docs.chalk.ai/docs/chalksql/example-workflows

This page summarizes some workflows that are commonly used in Chalk SQL.

### Introspecting datasets

In Chalk SQL, you can query named datasets within the chalk.datasets schema. Note that only datasets created within
the last 60 days will be available to Chalk SQL.

```
from chalk.client import ChalkClient
client = ChalkClient()
client.offline_query(
    input={
        "user.id": [i for i in range(1, 10)]
    },
    output=["user.name", "user.sum_amt_txns", "user.cnt_txns"],
    recompute_features=True,
    dataset_name="my_users_dataset"
).get_data_as_polars()
```

```
SELECT
    "user.id" AS id,
    "user.sum_txns" / "user.cnt_txns" AS avg_txn_amt,
    "__ts__" AS created_at
FROM chalk.datasets.my_user_dataset
WHERE "user.id" >= 5 AND "user.id" <= 8;
```

### Federating SQL over multiple data sources

If you define named data sources in your Chalk environment, you can reference schemas and tables within them in Chalk
SQL queries. This means Chalk SQL can be used to create queries that join across these data sources.

```
# In your Chalk project
from chalk.sql import PostgreSQLSource, BigquerySource

pg = PostgreSQLSource(name="my_postgres")
bq = PostgreSQLSource(name="my_bigquery")
```

```
WITH txn_sum AS (
    SELECT
        user_id,
        SUM(amount) AS total
    FROM my_bigquery.my_dataset.transactions  -- Table "transactions" in dataset "my_dataset"
    GROUP BY user_id
)
SELECT
    u.id AS user_id,
    u.name AS user_name,
    t.total AS user_spending
FROM my_postgres.my_schema.users u -- Table "users" in schema "my_schema"
JOIN txn_sum t
ON u.id = t.user_id;
```

### Views into online and offline query results

When making queries to Chalk with persistence turned on, these values will be ingested into the offline store, where
they can be re-used for analytical queries. Chalk SQL provides many useful views into the offline store.

The query log, which is accessible via the chalk.query_log.data table, consists of information about each query

It can be hard to determine the table in the table within in the offline store that corresponds
to the results of the query. Chalk SQL provides a table-valued function query_values_from_operation_ids()
that performs this resolution in-house.

```
from chalk.client import ChalkClient
client = ChalkClient()
result = client.query_bulk(
    input={
        "user.id": [i for i in range(1, 100)]
    },
    output=["user.name", "user.favorite_color"],
)
# In the UI or in the query meta information, an operation id will be set.
```

```
SELECT *
FROM query_values_from_operation_ids('c012345678901234567890123')
WHERE "user.id" = 1
```

You can also directly query the offline store via the offline_store catalog.

```
SELECT *
FROM offline_store.schema_name.feat_0123456789;
```

# The SQL Explorer
source: https://docs.chalk.ai/docs/chalksql/sql-explorer

## Chalk's built-in console for Chalk SQL

The SQL Explorer is an interface built into Chalk's web dashboard, which provides an easy-to-use interface for
making exploratory and experimental queries.

SQL Explorer Example

### Database Explorer

The Database Explorer is a direct overview of the various catalogs, schemas, and tables that Chalk SQL can integrate with.
This catalog of items is determined by your deployment, meaning that it will change as you make deployments to your
environment.

### Worksheets

Chalk SQL worksheets can be created in the SQL explorer via the Worksheets tab. You can create a "New Sheet" or choose
to use "Save Sheet" on an existing worksheet. Worksheets are tied to users and will be persisted across sessions,
providing an easy way to revisit queries within the explorer.

### Synchronous vs. Asynchronous Queries

Chalk SQL can be run in synchronous and asynchronous modes, which are tailored for transactional and
analytical workloads, respectively. Synchronous queries will hit the GRPC query servers directly, whereas async
queries will create an isolated environment but will take some time to provision.

Running synchronous Chalk SQL queries that are larger in nature can cause gRPC query servers to
go out-of-memory, which can impact any production traffic running on that engine.
Clients provide the ability to set memory limits for queries to mitigate this.

# SQL as Input
source: https://docs.chalk.ai/docs/chalksql/sql-as-input

If you need to compute the inputs to a query dynamically, you can use ChalkSQL.
This can improve performance and reduce cost by avoiding extra round trips across the network.

- This feature works in:ChalkGRPCClient.online_query_bulk()ChalkClient.offline_query()
- You can pass input_sql= as a SQL string, instead of input=.It uses the ChalkSQL dialect.It has access to the usual ChalkSQL catalog, which includes Data Sources and zero-argument Resolvers. You can see what's available in the SQL Data Explorer.
- Each column that the SQL query returns specifies an input feature.The SQL can return a __ts__ column to specify a query time.

### In online queries

For comparison, let's start with a simple query that does not use SQL:

```
grpc_client = ChalkGRPCClient(...)

grpc_client.online_query_bulk(
    input={
        User.id: [1, 2],
        User.email: ["alice@example.com", "bob@example.com"],
    },
    output=[
        User.id,
        User.email,
        User.is_fraud,
    ],
)
```

This query says we know the User.id and email, and we want to know is_fraud.
The known values (inputs) are passed as literal data: 1 or "alice@example.com".
Because we're using the _bulk method, we can pass many input examples in one query.

Conceptually the input is a table, where each column is a feature, and each row is a different example:

```
┌─────────┬───────────────────┐
│ user.id │    user.email     │
│  int32  │      varchar      │
├─────────┼───────────────────┤
│       1 │ alice@example.com │
│       2 │ bob@example.com   │
└─────────┴───────────────────┘
```

In any SQL implementation (not only ChalkSQL), you can build the same table
with VALUES:

```
select *
from (values (1, 'alice@example.com'), (2, 'bob@example.com'))
as t("user.id", "user.email");
```

Note the as t(...) alias, which renames the columns to match our features' fully-qualified names (FQNs).

You can plug this SQL query into the Chalk query by replacing
the input argument with input_sql:

```
grpc_client = ChalkGRPCClient(...)

grpc_client.online_query_bulk(
    input_sql="""
        select *
        from (values (1, 'alice@example.com'), (2, 'bob@example.com'))
        as t("user.id", "user.email");
    """,
    output=[
        User.id,
        User.email,
        User.is_fraud,
    ],
)
```

This returns the same result as the original query with hardcoded inputs.
But now we can replace the SQL with something more dynamic, such as a data source.

For example, to get the IDs of all users whose last name starts with "S":

```
select
    id as "user.id",
    email_address as "user.email"
from my_postgres.users
where last_name like "S%"
```

(Note the as aliases, which rename each column to exactly match the feature FQN.)

The overall Chalk query, using this SQL as its input, would look like this:

```
grpc_client = ChalkGRPCClient(...)

grpc_client.online_query_bulk(
    input_sql="""
        select
            id as "user.id",
            email_address as "user.email"
        from my_postgres.users
        where last_name like "S%"
    """,
    output=[
        User.id,
        User.email,
        User.is_fraud,
    ],
)
```

### In offline queries

This is the same as the previous example: the only difference is that it uses ChalkClient.offline_query instead of ChalkGRPCClient.online_query_bulk.

```
client = ChalkClient(...)

client.offline_query(
    input_sql="""
        select
            id as "user.id",
            email_address as "user.email"
        from my_postgres.users
        where last_name like "S%"
    """,
    output=[
        User.id,
        User.email,
        User.is_fraud,
    ],
    recompute_features=True,
)
```

### Setting a query time

Normally, online and offline queries let you specify a query time
by passing an input_times or now argument.
This time value is not a feature value, but is part of the overall input to the query.

For example, this query specifies values for one input feature, and also a query time:

```
grpc_client = ChalkGRPCClient(...)
grpc_client.online_query_bulk(
    input={
        Thermometer.id: [2, 3],
    },
    now=[datetime(2025, 1, 2, 12, 0, 0), datetime(2025, 1, 2, 12, 0, 0)],

    output=[
        Thermometer.id,
        Thermometer.measured_at,
        Thermometer.degrees_fahrenheit,
    ],
)
```

Conceptually, the overall input to the query is this table:

```
┌────────────────┬─────────────────────┐
│ thermometer.id │       __ts__        │
│     int32      │      timestamp      │
├────────────────┼─────────────────────┤
│              2 │ 2025-01-02 00:00:00 │
│              3 │ 2025-01-02 00:00:00 │
└────────────────┴─────────────────────┘
```

So to get the same behavior with SQL as the input, you would write a SQL query that outputs
two columns: thermometer.id and __ts__:

```
grpc_client = ChalkGRPCClient(...)
grpc_client.online_query_bulk(
    input_sql=f"""
        select *
        from (values
            (2, '2025-1-2 12:00:00'::datetime),
            (3, '2025-1-2 12:00:00'::datetime)
        )
        as t("thermometer.id", "__ts__")
    """,
    output=[
        Thermometer.id,
        Thermometer.measured_at,
        Thermometer.degrees_fahrenheit,
    ],
)
```

And the syntax for offline query follows the same pattern:

```
client = ChalkClient(...)
client.offline_query(
    input_sql=f"""
        select *
        from (values
            (2, '2025-1-2 12:00:00'::datetime),
            (3, '2025-1-2 12:00:00'::datetime)
        )
        as t("thermometer.id", "__ts__")
    """,
    output=[
        Thermometer.id,
        Thermometer.measured_at,
        Thermometer.degrees_fahrenheit,
    ],
    recompute_features=True,
)
```

### Using versioned features

Versioned features work as usual by appending a "@N" suffix to the fully-qualified name:

```
grpc_client.online_query_bulk(
    input_sql="""
        select
            id as "user.id",
            email_address as "user.email@2"
        from my_postgres.users
        where last_name like "S%"
    """,
    output=[
        User.id,
        User.email @ 2,
        User.is_fraud,
    ],
)
```

You may also find it convenient to use str() to access the fully-qualified name instead
of hardcoding it:

```
input_sql=f"""
    select
        id as "{str(User.id)}",
        email_address as "{str(User.email @ 2)}",
    from ...
""",
```

# Chalk Catalog Components
source: https://docs.chalk.ai/docs/chalksql/chalk-catalog-components

The Chalk Catalog is an umbrella term encompassing all things Chalk. This page describes how various concepts within
Chalk are translated into the Catalog and made available to Chalk SQL.

Like traditional relational databases, the Catalog is organized under a three-tiered namespace system of
catalogs, schemas, and tables.

### The chalk catalog

Most concepts in Chalk will be exposed as tables under the chalk database catalog.

### chalk.datasets schema

The chalk.datasets schema contains a view for each named dataset created within the last 60 days,
and the view's name is the dataset's name. Note that if two offline queries reference the same named dataset,
only the latest dataset revision is available in this schema.

To reference dataset revisions that are not the most
recent or were created without a name, consider using the get_dataset_revision() table-valued function.

This schema is available in all Chalk deployments.

### chalk.historical_values schema

The chalk.historical_values schema contains a view for each feature, as well as a view for each feature namespace
within the deployment.

- For each feature, a view with the same name as the feature's fully-qualified name is available in the Catalog
(i.e. chalk.historical_values.user.name). This view contains information about all observations of the feature, with
the following schema:observation_id, string, non-nullable: The unique identifier for the observation of the feature value.pkey, (type of feature namespace's pkey), non-nullable: The value of the primary feature associated with this
observationvalue, (type of feature namespace's value): The observed value of the feature.value_json, string, DEPRECATED: The observed value of the feature, as JSON, for backwards compatibility.observed_at, timestamp, non-nullable: The time at which the feature value was observed.inserted_at, timestamp, non-nullable: The time at which the feature value was inserted into the offline store.resolver_fqn, string, nullable: The resolver that computed this feature.deployment_id, string, nullable: The deployment id where the observation was made
- For each feature namespace, a view with the same name as the namespace is available in the Catalog
(i.e. chalk.historical_values). This view contains the freshest values of each feature for each primary key
at the current point in time, and has the following schema:__pkey__: (type of feature namespace's pkey), non-nullable: The value of the primary feature associated with this row<feature-name>, (type of feature), for each feature in the namespace: The freshest observed value of the feature for the primary key.<feature-name>.__observed_at__, timestamp, for each feature in the namespace: The time at which the freshest value was observed.

This schema is available in Chalk deployments with an
offline store
configured.

### chalk.query_log schema

The chalk.query_log schema consists of exactly one table, data, which is the query log table.
This table provides a list of query metadata for each operation id, including which tables in the offline store
correspond to values queried in that operation id. The data table has the following schema:

- operation_id, string, non-nullable: The unique identifier for the operation.
- environment_id, string, non-nullable: The environment id where the operation was run.
- deployment_id, string: The deployment id where the operation was run.
- operation_kind, string, The kind of operation that was run (inference, streaming, etc.).
- query_timestamp, timestamp: The value of now() that was used by the query.
- execution_started_at, timestamp: The time at which the operation started executing. Null if there were errors during planning.
- execution_finished_at, timestamp: The time at which the operation finished executing. Null if there were errors during execution.
- query_status, string: The status of the query (success, error, running, etc.).
- query_name, string: The query name for named queries, null otherwise.
- query_name_version, string: The version of the query for named queries, null otherwise.
- branch_name: string: The branch the query was run on, null if the query was not run on a branch.
- correlation_id, string: The correlation id for the query, null if the query was not run with a correlation id.
- value_tables: array of strings: The list of tables in the offline store that correspond to result values from this query.

This schema is available in Chalk deployments with an
offline store
configured.

### chalk.resolvers schema

The chalk.resolvers schema contains a view for each dataframe-returning resolver that
takes in no inputs. When querying this view, a resolver run will be triggered and have the resolver's outputs as the
view's contents.

This schema is available in all Chalk deployments.

### chalk.online_store schema

The chalk.online_store schema contains a fixed view keys, which contains different information depending on which
online store is configured for your environment.

- For Redis online stores, information about the keys' type (Scalar, HasMany, TimeSeries, etc.),
memory usage, TTL, and feature fqn are available in this view.
- For DynamoDB online stores, information about the keys' namespace and value are available in this view.

Additionally, for each feature namespace, a view with the same name (i.e. chalk.online_store.user) is available,
consisting of the following schema:

- __id__
- <feature_namespace>.<feature> for each feature
- <feature_namespace>.<feature>_ts for each feature

This schema is available in Chalk deployments with a Redis or DynamoDB online store configured.

### The offline_store catalog

The offline store is available as a catalog. Similar to data sources as catalogs, this catalog works as a direct
interface to querying the underlying database that powers it.

### Data Sources as Catalogs

Each data source that you register with Chalk will be automatically registered in the Chalk Catalog as
a database catalog. The catalog shares the same name as the data source and provides a more direct interface
into querying that data source.

Data sources that are not named will not be registered in the Chalk Catalog.

As an example, if you define a Postgres source and a BigQuery source in your code:

```
from chalk.sql import PostgresSource
from chalk.sql import BigquerySource
pg = PostgresSource(name='pg_source')
bq = BigquerySource(name='bq_source')
```

You can write a federated query in Chalk SQL to join a transactions table in pg with a users table in bq:

```
SELECT
  bq_users.user_id AS user_id,
  bq_users.full_name AS full_name,
  pg_transactions.transaction_id AS transaction_id,
  pg_transactions.amount AS transaction_amount
FROM bq_source.my_dataset.users AS bq_users
OUTER JOIN pg.public.transactions AS pg_transactions
ON user_id = pg_transactions.user_id
/* pg_source and bq_source are the name of the datasources
 and therefore also the name of their respective catalogs */
```

The following data source types will be registered to the Chalk Catalog, and will be able to be queried in Chalk SQL:

- PostgreSQL
- Spanner
- MySQL
- Clickhouse
- BigQuery
- Redshift
- Snowflake
- Databricks
# Notebook Development
source: https://docs.chalk.ai/docs/notebook-development

## Use Chalk in your notebook of choice.

Chalk makes it really easy to write and test out new features from a notebook.

To get started, you'll want to install and connect Chalk to your notebook environment. Generally
this involves two steps:

- Installing the chalkpy[runtime] package,
- Authenticating to Chalk (using the chalk cli or by setting environment variables)

We provide specific setup instructions for Deepnote, Hex and Vertex, but the process should be similar for other notebook environments.

### Installing the Chalk Python Dependency

To install dependencies, run the !pip install "chalkpy[runtime]" bash command directly in a cell. Alternatively,
you can add and install the chalkpy[runtime] dependency in your kernel's virtual environment.

### Connecting Your Notebook to Chalk

To authenticate, we recommend generating a client ID and client secret pair.

To do this, open the Chalk Dashboard. Go to Settings > Access Tokens and click on New Token, selecting all necessary permissions (generally, you'll want: online query, offline query, and preview deployment permissions).

You can now use these access credentials to connect Chalk to any Jupyter notebook environment—we walk through
this process for a few different notebook environments in our notebook setup docs.

```
from chalk.client import ChalkClient
import os

CHALK_CLIENT_ID = os.environ.get("CHALK_CLIENT_ID")
CHALK_CLIENT_SECRET = os.environ.get("CHALK_CLIENT_SECRET")

client = ChalkClient(
  client_id=CHALK_CLIENT_ID,
  client_secret=CHALK_CLIENT_SECRET,
  branch='notebook',
)
```

### Verifying the Setup

To verify that everything is properly set up, you can run the following code in a cell:

```
client.whoami()
```

If everything is properly configured, you should see your user_id, team_id and environment_id come back:

```
WhoAmIResponse(user='<user_id>', environment_id=<environment_id>, team_id='<team_id>')
```

### Loading Features

Now we can start building some new features!

To load your Chalk features into your notebook, you'll want to run:

```
from chalk.client import ChalkClient

client = ChalkClient()

client.load_features()
```

This will print out your available features and load them into your notebook:

```
Director
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Feature            ┃ Type                  ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ id                 │ str                   │
│ name               │ str                   │
│ birth_year         │ int                   │
│ active             │ bool                  │
│ favorite_numbers   │ list[int]             │
│ death_year         │ int | None            │
│ known_for_titles   │ list[str]             │
│ known_for_genres   │ list[str]             │
│ movies             │ DataFrame[Movie]      │
│ num_movies         │ int                   │
└────────────────────┴───────────────────────┘
Movie
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Feature                ┃ Type              ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ id                     │ str               │
│ director_id            │ str               │
│ release_number         │ int               │
│ type_                  │ str               │
│ title                  │ str               │
│ original_title         │ str               │
│ release_date           │ dt.datetime       │
│ runtime_m              │ float             │
│ primary_genre          │ str               │
│ secondary_genre        │ str               │
└────────────────────────┴───────────────────┘
```

We'll use the data schema above for the rest of this tutorial.

Before we get started writing features, you'll want to import _ from
Chalk _ (underscore) allows you to build out features on your feature classes.

```
from chalk.features import _
```

Additionally, if you want to create and work from a new branch (which is recommended), run the following command:

```
client.get_or_create_branch(branch_name="<your-branch-name>")
```

This command will:

- create a new Chalk branch deployment that has the same features defined as your main chalk deployment,
- point your client to that new branch.

If the branch already exists, your client will just be updated to point to that branch (no new branch deployment will be created).

### Building New Features

Lets say we want to write a new "exclaimed name" feature, which is a director's name with an exclamation mark tacked on.
To do this, run the following code in a cell:

```
Director.name_exclaimed = _.name + "!"
```

In this example, the underscore acts as a reference to the Director feature class`.

We have now created a new feature in our notebook and can query for it in either an online or offline context.

### Querying for features

To query for your new features, pass them as outputs to the ChalkClient query methods. For instance, to run an
online query for your new Director.name_exclaimed feature, you can run the following:

```
new_features = client.query(
    input={
        Director.id: 113,
    },
    output={
        Director.name,
        Director.name_exclaimed,
    }
)

new_features
```

Running an offline query is equally straight forward:

```
chalk_dataset = client.offline_query(
    input={
        Director.id: list(range(1000)),
    },
    output={
        Director.id,
        Director.name,
        Director.name_exclaimed,
    },
    recompute_features=True,
    run_asynchronously=True,
    dataset_name="<dataset_name>",
)

df = chalk_dataset.to_pandas()
```

Running the offline query above creates a Pandas DataFrame with the columns Director.id, Director.name, and Director.name_exclaimed (alongside
some metadata columns). This DataFrame will have one row for every Directors with an id between 0 and 999.

By providing a dataset_name to the offline_query, we've created a named dataset. Named datasets can easily be shared with other team members.

Any historical dataset can be accessed using the ChalkClient. Named datasets can be accessed as follows:

```
client = ChalkClient()

dataset = client.get_dataset(name="<dataset_name>")
```

### Building Out More Complex Features

You can use expressions to build out more complex features. Generally these more complex features are composed of: has-one relationships, has-many relationships, and chalk functions.

### Using Has-one Relationships

In the schema we've defined above, a Movie is in a has-one relationship with its Director (even if this is not necessarily true in practice).

When building new features on the Movie class, features from joined classes can be directly accessed. For instance, lets say we want to define Movie.is_latest_release.
We can accomplish this by defining a feature that reaches through the has_one join:

```
Movie.is_latest_release= _.director.num_movies == _.release_number
```

The expression above defines a boolean feature which tests whether the release number for a movie (_.release_number) is equal to the number of movies a director
has released (_.director.num_movies).

### Using Has-Many Relationships

In the schema we've defined above, a Director is in a has-many relationship with their Movies.

When building new features on the Director class, features from joined classes can be directly accessed. For instance, lets say we want to define Director.average_movie_runtime. We can accomplish this by defining an aggregation feature:

```
Director.average_movie_runtime = _.movies[_.runtime].mean()
```

In the above example, the two different _'s refer to two different feature class namespaces:

- _.movies can be thought of as Director.movies,
- _.runtime can be thought of as Movie.runtime.

The expression above gets a directors movies (_.movies), specifies that the aggregation is happening on the
runtime field of those movies (_.movies[_.runtime]) and then calculates the mean (.mean()).

Filters can also be passed to these expressions. For instance, say we want to filter out any movie
that has a primary or secondary genre of short from the average runtime. This can be done as follows:

```
Director.average_movie_runtime_filtered = _.movies[
    _.runtime,                      # aggregation column
    _.primary_genre != "short",     # filter
    _.secondary_genre != "short"    # additional filter
].mean()
```

### Using Chalk Functions

Chalk exposes a number of functions that can be called and composed as part of expressions—a full list of these functions
can be found in our expressions docs.

Below, we provide a few examples of how these functions can be used to create new features:

Identify whether a movie belongs to a Director's typical genres:

```
Movie.is_directors_usual_genre = F.contains(_.director.genres, _.primary_genre)
```

Identify whether a movie was released on a US federal holiday:

```
Movie.released_on_holiday = F.is_us_federal_holiday(_.release_daate)
```

Get release_date of Director's last movie:

```
Director.latest_movie_release = F.max_by(_.movies[_.release_date], _.release_date)
```

### Composing New Features

The features you've defined in your notebook can also be composed—they can be used to define new features.
For instance, you can define the Director.makes_movies_that_are_too_long feature:

```
Director.makes_movies_that_are_too_long = _.average_movie_runtime > 150
```

### Translating this Code into Production Code

Defining features as these expressions provides a couple really significant advantages:

- You build out really modular and granular features that can be composed.
- Your features translate directly into performant code—everything we've written in this tutorial can be directly translated to your Chalk feature store and run efficiently.
# Notebook Setup
source: https://docs.chalk.ai/docs/notebook-setup

## Set up Chalk in your notebook of choice.

In this section, we walk through authentication: how to connect to Chalk from a
notebook.

To authenticate, we recommend generating a client ID and secret key pair.

This can be done in the Chalk Dashboard. Go to Settings > Access Tokens,
and generate a client ID/secret key pair by clicking on New Token and selecting
all necessary permissions—(typically, online query, offline query, and preview
deployment permissions should be sufficient).

You can then use your access credentials to connect Chalk to any Jupyter notebook
environment. In the following section, we show the process of authenticating
to a local notebook. We then show the process for Hex, Deepnote, and Vertex.

### Local

If you are working with a local notebook, Chalk will pick up your credentials
generated from running chalk login in your terminal.

All you need to do is initialize the client:

```
from chalk.client import ChalkClient

client = ChalkClient()
```

### Hex

On Hex, you can store the client ID and secret key using secrets

Hex Secrets

Select Python 3.10 as the image under Environment > Compute Profile.

Hex Python Image

The Chalk client can then be initialized referencing the variables directly.

```
from chalk.client import ChalkClient

client = ChalkClient(
  client_id=CHALK_CLIENT_ID,
  client_secret=CHALK_CLIENT_SECRET,
  branch='notebook'
)
```

### Deepnote

On Deepnote, you can set environment variables by going to the
integrations tab and clicking on the "Environment Variables" button.

Deepnote Environment Variables

Set the CHALK_CLIENT_ID and CHALK_CLIENT_SECRET variables to the values you generated in the previous step.
You can then initialize Chalk by running the following code in a cell:

```
import os
from chalk.client import ChalkClient

client = ChalkClient()
```

### Vertex and Google Colab Enterprise

On Google Colab Enterprise, you can set up secrets with the Google Secret Manager.
Add two secrets named chalk-client-id and chalk-client-secret to Google Secret Manager
that correspond to your Chalk client id and client secret.

Google Colab Secret

Add three dependencies to your notebook environment: google-cloud-secret-manager,
google-cloud-resource-manager, and chalkpy.

You can now read your credentials securely from the Google Secret Manager and
initialize your Chalk client!

```
# !pip install google-cloud-secret-manager
# !pip install google-cloud-resource-manager
# !pip install chalkpy
import os

from google.cloud import secretmanager as sm
from google.cloud import resourcemanager_v3 as rm

from chalk.client import ChalkClient

# Create the Secret Manager client.
PROJECT_NAME = os.environ['GOOGLE_CLOUD_PROJECT']

# These should match the names given to your secrets in Google Secret Manager
client_id_name = "chalk-client-id"
client_secret_name  = "chalk-client-secret"

# Get the project ID from google resources
project_id = rm.ProjectsClient().get_project(
    request=rm.GetProjectRequest(
      name=f"projects/{PROJECT_NAME}"
    )
).name

# Get CHALK_CLIENT_ID and CHALK_CLIENT_SECRET using the secret manager
secret_client = sm.SecretManagerServiceClient()

CHALK_CLIENT_ID = secret_client.access_secret_version(
    name=f"{project_id}/secrets/{client_id_name}/versions/1"
).payload.data.decode("utf-8")

CHALK_CLIENT_SECRET = secret_client.access_secret_version(
    name=f"{project_id}/secrets/{client_secret_name}/versions/1"
).payload.data.decode("utf-8")


# Instantiate your Chalk Client
chalk_client = ChalkClient(
    client_id=CHALK_CLIENT_ID,
    client_secret=CHALK_CLIENT_SECRET,
    branch="new-feature"
)
```

# Observability Overview
source: https://docs.chalk.ai/docs/observability

## Monitor the execution of your feature pipelines & alert you when problems arise.

It’s inevitable — production data drifts from historical baselines,
pipelines break, and partners change data formats. Chalk monitors
the execution of your feature pipelines and to alert when problems
arise.

### What to read next

Resolvers support many workflows and common orchestration patterns:

- Metrics Monitor -
Define critical metrics for monitoring and alerting.
- Metrics Export -
Export Chalk metrics to other monitoring systems.
- Alert Configuration -
Configure which alerts get sent where and to whom.
- Logs Export -
Export Chalk logs to other monitoring systems.
- Datadog Integration -
Ingest Chalk metrics into Datadog.
- PagerDuty -
Integrate PagerDuty alerts into you feature pipelines.
- Slack -
Consume Chalk alerts in your Slack channels.
- incident.io -
Integrate Chalk alerts with your IncidentIo workflow
# Metrics Monitor
source: https://docs.chalk.ai/docs/metricmonitor

## Define and monitor metrics

Chalk's online dashboard provides a simple way to view
metrics about performance of your queries resolvers.
By default, the resolver and query detail pages show request count and latency for each 30 minute interval over the last 2 days, but you may wish to customize this to make it more useful.

### Resolver Details

In addition to the default charts, the resolver details page tells you the input and output features of the resolver, plus the implementation code of the resolver.

Metric Dashboard

### Query Details

The query details page shows you much of the same information as the resolver details page, including the input and output features. You can also see which resolvers executed on the right hand sidebar.

Query Dashboard

### Customize Your Metrics Dashboard

Customize your monitoring view with additional charts, combine metrics into complex formulas, and configure alerting thresholds.
Clicking "Add Metric" brings up the metric editor which you can use to add a new chart to your page.
Edit or remove a chart using the ellipsis menu.

Create a metric

### Add Series

By default, when you click add metric the editor is pre-populated with a new series called Request Count.
Use the drop down fields to change the metric kind, window, grouping function, and conditions. Add additional series to the chart by clicking "Add Series" below.

### Add Formula

Aggregate multiple series together into one chart using a formula. Chalk supports aggregating by sum, total ratio, ratio, product, and abs

### Add Alert Trigger

Alerts can be triggered on any series or formula. To set up an alert, you should first configure at least one of
a Pagerduty integration or a Slack integration. Then you can set up
Alert Configurations to define which channels to use to alert different users or teams.
Then, in your metrics chart, you can select the series, the threshold logic, and the severity, and route the
alert appropriately with the alert owner dropdown. You can select from users in the Chalk environment or free type
an owner name corresponding to one of your alert configurations.

# Charts with Code
source: https://docs.chalk.ai/docs/charts

## Define charts and alerts with code.

You can also create charts using Python, just as you would your features and resolvers.

### Charts and Series

The heart of the Chart paradigm is the Series,
a single collection of data points over time.
They must be instantiated with a metric and name,
and can accumulate filters and group-bys to
support advanced calculations.
Some Series metrics require a window function parameter
to decide how to calculate values.
Window functions often include aggregates such as
count and mean and percentiles such as 95% and 99%.
Methods and options will auto-complete in your text
editor based on the type of series.

Series objects must be attached to a Chart,
which can have multiple series and up to one trigger.

Let's say you have a resolver get_fraud_profile and you want to make sure it goes fast.
The following chart will track the p95 latency of your resolver,
and attach it to its resolver page on the dashboard.

```
from chalk.monitoring import Chart, Series

Chart(
    name="my_chart_1",
    window_period="30m"
).with_series(
    Series.resolver_latency_metric(
        name="p95 latency for `get_fraud_profile`",
        window_function="95%"
    ).where(resolver=get_fraud_profile)
).with_resolver_link(get_fraud_profile)
```

This is all that's necessary to ship a chart to your online dashboard upon chalk apply!

Using this builder pattern, we're able to generate charts
quickly and by reusing intermediate instances if necessary
since every instance is deep-copied from the previous instance.

By default, only non-copied charts will be registered to the server.
Consider the following example:

```
from chalk.monitoring import Chart, Series

base = Chart(
    name="my_chart_1",
    window_period="30m",
).with_series(
    Series.resolver_latency_metric(window_function="99%")
)

modified = base.with_series(
    Series.resolver_latency_metric(
        window_function="99%",
    ).where(resolver_type='online')
)
```

Since modified has not been copied,
it will be the only one of the three to be shipped to the server.
However, base has been copied, and will not create a chart.
To force-register charts to the server, use .keep(),
which will be applied to the chart itself and all its descendants.

In the above example, we also added a filter to our Series object.
Here, we restrict the series to only calculate latencies for online resolvers.
The filters enabled differ depending on the series metric,
and the appropriate options should be available through
auto-complete in your text editor.

### Triggers

Triggers can also be added to charts. The following error trigger will
alert myemail@chalk.ai when the resolver get_fraud_profile takes more
than 200ms to execute.

```
from chalk.monitoring import Chart, Series

Chart(name="my_chart_1", window_period="30m").with_trigger(
    Series.resolver_latency_metric(
        window_function="95%"
    ).where(resolver=get_fraud_profile) > 0.2,
    trigger_name=f"High latency alert",
    severity="error",
    channel_name="myemail@chalk.ai",
    description="""
        *Debugging*
        When this alert is triggered, we're parsing null values from
        a lot of our FICO reports. It's likely that Experian is
        having an outage. Check the <dashboard|https://internal.dashboard.com>.
    """
).with_resolver_link(get_fraud_profile)
```

### Advanced Chart Building

We can also easily create charts in bulk.
Let's say we have a feature class Transaction with four scalar features.

```
from chalk.monitoring import Chart, Series

for feature in Transaction:
    Chart(
        name=f"{feature} request count chart",
        window_period="5m"
    ).with_trigger(
        Series.feature_request_count_metric().where(feature=feature) < 10,
        trigger_name=f"Low volume requests for {feature}",
        severity="error",
        channel_name="myemail@chalk.ai",
    ).with_feature_link(feature)
```

Upon chalk apply, four charts will be registered to the server filtering
on feature requests for each of the four features.
These charts will be available on the relevant feature pages on the dashboard.

# Feature Drift
source: https://docs.chalk.ai/docs/featuredrift

## Detect and setup alerting for drift in feature values

Chalk provides a simple way to monitor feature drift by running
the Kolmogorov-Smirnov test for
features values over a given time period.

### Kolmogorov–Smirnov test

The K-S test is a statistical test that can be used to determine if two samples
are drawn from the same distribution. Chalk runs the test on
samples from the online store and data from a given dataset to determine if the
feature values are drawn from the same distribution.

Note that the K-S test can not be used if the feature values in the dataset are all null, if they are
not numeric or if there is only one unique value.

### Charts and Alerts

To setup a chart and alert for the Kolmogorov-Smirnov test, start by creating a
named dataset for the features you want to monitor.

Then under Settings > Global Charts, create a new chart and click on Add Formula, choosing KS TEST as the function.
Next select the dataset you created and the feature you want to monitor.

The y-axis of the chart displays the difference between the Kolmogorov-Smirnov test statistic and the critical value at
significance level 0.05. When the value is greater than 0, the feature values are considered to be drawn from different
distributions.

KS Test Chart

To create an Alert, click on Add Alert Trigger and configure the alert to trigger when the KS Test value is greater than 0.

# Metrics Export
source: https://docs.chalk.ai/docs/metricexport

## Export Chalk metrics to other monitoring systems.

Chalk's online dashboard provides a simple way to view
metrics about performance of your feature pipelines.
However, you may wish to export these metrics from Chalk
into other observability tools so that you can view
your Chalk-related data alongside data from other
systems you maintain.

### Exporting metrics

Chalk tracks various time series metrics that measure the latency and throughput of resolvers and
streaming pipelines.

Chalk uses TimescaleDB to store these metrics. You can use any
OpenMetrics-compatible collector to collect metrics about the execution of your feature pipelines
from Chalk. Examples include:

- Prometheus
- OpenMetrics (Datadog)
- NewRelic
- Stackdriver Prometheus

### Available metrics

The table below summarizes the metrics that are available for export.
The headers in the table are the exported metric name followed by the
OpenMetrics metric type
(gauge,
histogram,
summary, or
counter).

Provides information about the time it takes to compute a resolver.

The name of the resolver, for example, my.company.get_user

Whether this latency represents the median, 75th percentile, 95th percentile, or 99th percentile
of the latency

The type of the resolver - online, offline, or stream.

Provides information about the time it takes to execute an online query.

The name of the query, for example, eligibility_query_v2. Queries without names are
labeled "Unnamed"

Whether this latency represents the median, 75th percentile, 95th percentile, or 99th percentile
of the latency

Provides information about the time it takes to execute a cron run.

The name of the resolver executed by the cron run, for example, my.company.get_user

Whether this latency represents the median, 75th percentile, 95th percentile, or 99th percentile
of the latency

Provides information about the number of times a feature was computed.

The name of the feature, for example, user.age

The status of the computed feature (success or failure)

The context in which the feature was generated

Provides information about the number of times a resolver was computed. This metric informs the number of
times that resolvers are being called and the context in which they are called, for example in a cron
run as part of a scheduled job or in inference as part of a query plan.

The name of the resolver, for example, my.company.get_user

The status of the resolver run (success or failure)

The context in which the resolver ran

The type of the resolver - online, offline, or stream.

Provides information about the number of times a cron run was executed. This metric is useful for
monitoring the status of resolver runs that are scheduled or triggered via API to load data into
the online and/or offline store.

The name of the resolver executed by the cron run, for example, my.company.get_user

The status of the cron run (success or failure)

Provides information about the number of features computed by cron written to online / offline store. This
metric is useful for monitoring resolver runs that are scheduled or triggered via API to
load data into the online and/or offline store.

The name of the resolver executed by the cron run, for example, my.company.get_user

Whether the features were written to online or offline store.

Provides statistical information about the value of features.

The name of the feature, for example, user.age

Whether this value represents the median, 75th percentile, 95th percentile, or 99th percentile
of the feature value

Provides information about the number of times an online query was executed.

The name of the query, for example, eligibility_query_v2. Queries without names are
labeled "Unnamed"

The status of the query (success or failure)

The active deployment version. This gauge will always have a value of 1 for active deployments.
A gauge of this kind is sometimes called an Info metric.

The ID of the deployment.

The response counts by HTTP response code.

The ID of the environment.

The current max_ingested_timestamp in UNIX epoch time for resolvers.

The ID of the resolver.

# Alert Configuration
source: https://docs.chalk.ai/docs/alertconfig

## Configure Alerts

Connect your Alert Thresholds
to external alerting tools like PagerDuty,
Slack, and incident.io.

### Configure your alerts

Chalk enables you to set up alert configurations to route alerts to different channels based on the owner
of the alert. In the dashboard, visit Settings > Alert Configuration to define an owner (the dropdown will list
all users in the environment, but the owner can be any string, so you can use a team name or other identifier).
For each owner, you can select one or more channels to send alerts to. The channels can be Slack channels,
Pagerduty services, and IncidentIo integrations, depending on which integrations you have set up in your
Chalk environment. All alerts that belong to an owner (as configured on the alert trigger) will be sent to
the channels associated with that owner.
Edit or remove the alert configuration, or send a test message, using the buttons on the right hand side.

Alert Configuration

# Log Export
source: https://docs.chalk.ai/docs/logexport

## Export Chalk logs to other monitoring systems.

Chalk's online dashboard provides a simple way to view logs
from resolver execution. However, you may wish to
export these logs into other observability
tools so that you can view your Chalk-related data alongside
data from other systems you maintain.

### Exporting logs

Chalk can export your logs to a sink of your choosing.
You can configure sinks for log export from your settings page.
Exported logs will contain the following fields:

ISO8601 timestamp.

The log line format version. Currently constant "1".

The log message.

Name of the logger, if relevant.

The log level as a string: "INFO", "WARN", "ERROR", "DEBUG".

Stack trace of the associated exception, if relevant.

A trace id in OpenCensus format. Used for correlating logs corresponding to a single query.

Chalk Project ID.

Chalk Deployment ID. Can be used to understand log patterns as code evolves.

Your commit SHA, if available for the deployment.

"online" or "offline".

The name of the resolver that produced this log line, if available.

Environment name.

Environment id.

An array of the tags that were provided for the associated query.

The id of the agent that made the request (a service token or Chalk user).

### Custom logs

Chalk provides an implementation of the standard Python Logger interface that supports
emitting logs to the web UI and your metrics export sink. You can use this logger like this:

```
from chalk.clogging import chalk_logger

@online
def your_resolver(...):
    chalk_logger.info("Hello world!")
```

# Tracing
source: https://docs.chalk.ai/docs/tracing

## Use tracing to debug and optimize query performance.

Chalk provides traces for online queries, enabling customers to identify performance bottlenecks and effectively
optimize their low-latency queries. Chalk's traces break down every function call--from feature computation to data
retrieval--showing where time is spent and why. Easily write, deploy, and tune high-performance ML applications
with Chalk.

Chalk's tracing is built on OpenTelemetry standards, ensuring compatibility with existing telemetry systems and
future extensibility. Traces are stored in a ClickHouse database deployed within your Kubernetes cluster and
viewable via the query pages in the Chalk dashboard. Chalk, by default, sets a TTL of 7 days for trace data, but
will adjust this automatically as storage limits are approached.

### Enabling Traces

Tracing is typically enabled by default in Chalk environments. In order to fetch a trace for an online query,
you can either add a flag at query time or set environment variables for environment-wide configurations.

### Requirements

To use tracing features, please ensure that you add the following Python dependency

- chalkpy[tracing]

This links required peer dependencies for OpenTelemetry tracing:

- opentelemetry-api
- opentelemetry-sdk

Please note that tracing is not fully supported in the python client until version chalkpy>=2.95.9

### Query-time traces

To fetch a trace for a specific online query, you can use the --trace flag in the Chalk CLI:

```
chalk query --in customer.id=123 --out customer.num_recent_transactions --trace
```

You can also specify a trace flag in your ChalkClient call:

```
from chalk import ChalkClient

ChalkClient().query(
    input={"customer.id": 123},
    output=["customer.avg_recent_transactions_amt"],
    trace=True
)
```

Once you have run a traced query, you can view the trace in the Trace tab of the Online Query page.

Trace Tab

### Environment Configuration

Following OpenTelemetry standards,
you can also configure tracing via environment variables. Tracing across your environment can be configured using the
environment variables OTEL_TRACES_SAMPLER and OTEL_TRACES_SAMPLER_ARG, which you can set in your dashboard under
Settings > Variables. The default values of OTEL_TRACES_SAMPLER=parentbased_traceidratio
and OTEL_TRACES_SAMPLER_ARG=0.01 will be used, unless an explicit value is set

The supported sampling strategies are detailed below:

| Environment Variable Configuration | Description                                               |
|------------------------------------|-----------------------------------------------------------|
| OTEL_TRACES_SAMPLER=always_on          | Trace 100% of online queries--no query-time overrides                              |
| OTEL_TRACES_SAMPLER=always_off         | Disable tracing for all online queries--no query-time overrides                       |
| OTEL_TRACES_SAMPLER=traceidratio OTEL_TRACES_SAMPLER_ARG=0.005 | Sample a percentage of online queries based on OTEL_TRACES_SAMPLER_ARG (e.g., 0.005 for 0.5%)--no query-time overrides |
| OTEL_TRACES_SAMPLER=parentbased_traceidratio OTEL_TRACES_SAMPLER_ARG=0.01 | Sample a percentage of online queries based on OTEL_TRACES_SAMPLER_ARG (e.g., 0.01 for 1%) if there is no parent span--accepts query-time overrides |
| OTEL_TRACES_SAMPLER=parentbased_always_on     | Trace 100% of online queries if there is no parent span--accepts query-time overrides               |
| OTEL_TRACES_SAMPLER=parentbased_always_off    | Disable tracing for all online queries if there is no parent span--accepts query-time overrides          |

When configuring tracing via environment variables, you can either enforce tracing settings for all queries
("always_on" or "always_off") or enable query-time overrides ("parentbased_*" samplers). For example, if you set
OTEL_TRACES_SAMPLER=parentbased_traceidratio with OTEL_TRACES_SAMPLER_ARG=0.01, then 1% of online queries
will be traced by default, but you can still enable tracing for specific queries using the --trace flag or
the trace=True argument in ChalkClient. However, if you set OTEL_TRACES_SAMPLER=always_on, then all
online queries will be traced, and the query-time flags will be ignored.

# Introspection
source: https://docs.chalk.ai/docs/introspection

## View metadata about your deployed Chalk features and resolvers.

Occasionally, you may need to inspect a running Chalk environment to review metadata about your configured Chalk
pipelines. You can use the provided Rest API to query for this metadata as part of your admin dashboards,
monitoring tooling, or team knowledge management.

Note: if you use a user-scoped token (i.e. one that’s derived from chalk login),
you will need to specify the environment in which to trigger your resolver via the X-Chalk-Env-id header.

### View an environment's live feature and resolver graph

The auth token that should be used for the request, such as
Authorization: Bearer $(chalk token)

The environment ID for which this request should be executed, if the provided Authorization token was not created with an implicit environment

### Response

Pipelines object

### Example

```
curl -XGET -H "Authorization: Bearer $(chalk token)" \
     -H "X-Chalk-Env-Id: <your-environment-id>" \
     https://api.chalk.ai/v1/environment/graph

# Returns

{
  "deployment_id": "<deployment-id>",
  "features": […],
  "resolvers": […]
}
```

### View a deployment's feature and resolver graph

The machine-generated ID for your deployment, usually a 25-character string that begins with c
and looks something like cl789789aoa002chalkexample. The deployment can be associated with a
preview or production environment.

The auth token that should be used for the request, such as
Authorization: Bearer $(chalk token)

The environment ID for which this request should be executed, if the provided Authorization token
was not created with an implicit environment

### Response

Pipelines object

### Example

```
curl -XGET -H "Authorization: Bearer $(chalk token)" \
     -H "X-Chalk-Env-Id: <your-environment-id>" \
     https://api.chalk.ai/v1/deployments/<your-deployment-id>/graph

# Returns
{
  "deployment_id": "<deployment-id>",
  "features": […],
  "resolvers": […]
}
```

### Pipelines

The deployment ID that is being described by this graph

Array of FeatureInfo objects, one for each Feature in your deployment.
Most of the metadata in each FeatureInfo is defined in your Feature() declaration

The fully-qualified name of this feature, like user.id

The name of this feature, like "User first name"

Additional metadata about this feature's value type, including its underlying raw type, whether
it's a primary key, and feature version metadata.

The user tags associated with this feature

An ISO-8601 datetime string describing when this feature was first introduced to your deployment

An ISO-8601 datetime string describing when this feature was last modified by a deployment

Whether this feature has Offline-to-Online Chalk ETL integration

Array of ResolverInfo objects, one for each Resolver in your deployment.

The fully-qualified name of this resolver, like example.resolvers.get_user

Whether this resolver is configured to run as an

online or offline resolver, or a stream or sink resolver

The user tags associated with this resolver

The declared feature input fqns to this resolver, as a string array

The declared feature output fqns of this resolver, as a string array

If the resolver is configured to run with a schedule, this field
will describe that schedule

The last time this resolver was modified by a deployment, including its declaration or its
implementation, as an ISO-8601 datetime string

# Scaling Groups
source: https://docs.chalk.ai/docs/scaling-groups

## Run long-lived services with replicas, GPU support, and automatic DNS routing in your Chalk environment.

Scaling groups let you run long-lived, replicated services inside your Chalk environment's
Kubernetes cluster. Each scaling group is backed by a Kubernetes Deployment, so you get
rolling updates, replica management, and automatic service discovery out of the box.

Common use cases include hosting ML inference servers, running sidecar services that your
resolvers depend on, and deploying internal APIs that need to scale independently from
your feature pipelines.

### Creating a scaling group

Use the chalk scaling-group create command to launch a new scaling group. At a minimum
you need an image, a name, and a port:

```
$ chalk scaling-group create \
    --image=my-registry/my-inference-server:v1 \
    --name=inference \
    --port=8080
```

This creates a Kubernetes Deployment with a single replica running your image, a headless
Service, and an HTTPRoute that exposes the service over HTTPS.

You can tune replicas and resource limits at creation time:

```
$ chalk scaling-group create \
    --image=my-registry/my-inference-server:v1 \
    --name=inference \
    --port=8080 \
    --replicas=3 \
    --cpu=4 \
    --memory=8Gi
```

### GPU support

Scaling groups support GPU-accelerated workloads. Use the --gpu flag with a
type:count value to request GPU resources:

```
$ chalk scaling-group create \
    --image=my-registry/my-gpu-model:v1 \
    --name=gpu-inference \
    --port=8080 \
    --gpu=nvidia-tesla-t4:1 \
    --cpu=4 \
    --memory=16Gi
```

The type portion (e.g. nvidia-tesla-t4) is used to select the right node pool via
a Kubernetes node selector (cloud.google.com/gke-accelerator), while the count
sets the nvidia.com/gpu resource request and limit on the container. A toleration for
nvidia.com/gpu is also applied so the pods can schedule onto GPU-tainted nodes.

If you don't need to target a specific GPU type (for example on EKS where node selection
is handled differently), you can pass just the count:

```
$ chalk scaling-group create \
    --image=my-registry/my-gpu-model:v1 \
    --name=gpu-inference \
    --port=8080 \
    --gpu=1 \
    --cpu=4 \
    --memory=16Gi
```

This sets the nvidia.com/gpu resource request without adding a GPU-type node selector.

Available GPU types depend on what node pools are configured in your cluster. Common
GKE values include:

| GPU type | Description |
|---|---|
| nvidia-tesla-t4 | NVIDIA T4 (cost-effective inference) |
| nvidia-tesla-a100 | NVIDIA A100 (high-performance training and inference) |
| nvidia-l4 | NVIDIA L4 (balanced inference) |
| nvidia-tesla-v100 | NVIDIA V100 (training) |

To request multiple GPUs, increase the count:

```
$ chalk scaling-group create \
    --image=my-registry/my-training-server:v1 \
    --name=multi-gpu \
    --port=8080 \
    --gpu=nvidia-tesla-a100:4
```

### CPU and memory resources

The --cpu and --memory flags control the resource requests and limits for each
replica. When specified, both the Kubernetes request and limit are set to the same
value, guaranteeing your workload the resources it asks for.

```
$ chalk scaling-group create \
    --image=my-registry/my-app:v1 \
    --name=my-service \
    --port=8080 \
    --cpu=2 \
    --memory=4Gi
```

If you omit these flags, the following defaults are applied:

| Resource | Request | Limit |
|---|---|---|
| CPU | 100m | 1 |
| Memory | 256Mi | 1Gi |

CPU values follow Kubernetes conventions: 1 means one full core, 500m means half a
core. Memory values use standard suffixes: Mi (mebibytes) and Gi (gibibytes).

### DNS and routing

Every scaling group is automatically assigned a DNS hostname and exposed over HTTPS
through your cluster's gateway. The hostname follows this pattern:

```
<environment-id>-<scaling-group-name>.<gateway-domain>
```

For example, a scaling group named inference in environment abc123 with gateway
domain gw.chalk.ai would be reachable at:

```
https://abc123-inference.gw.chalk.ai
```

This hostname is shown as the Web URL in the output of chalk scaling-group get
and chalk scaling-group list. Traffic arriving at this hostname is routed to the
port you specified with --port.

Because the hostname includes the scaling group name, you can reference it by a
stable, human-readable URL rather than an opaque UUID.

### Managing scaling groups

### Listing scaling groups

```
$ chalk scaling-group list
```

This displays a table of all scaling groups in your environment with their ID, name,
image, status, replica counts, URL, and creation time.

### Inspecting a scaling group

```
$ chalk scaling-group get --name=inference
```

This shows detailed information about the scaling group including its spec, replica
status (desired, ready, available), tags, and URL.

### Deleting a scaling group

```
$ chalk scaling-group delete --name=inference
```

This removes the Kubernetes Deployment, Service, and HTTPRoute associated with the
scaling group. The database record is soft-deleted so it still appears in history.

### Tags

You can attach arbitrary key-value tags to a scaling group for organization and
filtering:

```
$ chalk scaling-group create \
    --image=my-registry/my-app:v1 \
    --name=my-service \
    --port=8080 \
    --tags="team=ml,version=2.1"
```

Tags are applied as Kubernetes labels with the prefix chalk.ai/tag-, making them
visible in standard Kubernetes tooling.

### Entrypoint override

If you need to override the Docker image's default entrypoint, use the --entrypoint
flag with comma-separated arguments:

```
$ chalk scaling-group create \
    --image=python:3.12 \
    --name=custom-server \
    --port=8000 \
    --entrypoint="python,-m,uvicorn,main:app,--host,0.0.0.0,--port,8000"
```

### Full example

Here is a complete example that provisions a GPU-accelerated inference service with
custom resource limits, multiple replicas, and tags:

```
$ chalk scaling-group create \
    --image=my-registry/llm-serving:v3 \
    --name=llm-inference \
    --port=8080 \
    --replicas=2 \
    --gpu=nvidia-l4:1 \
    --cpu=8 \
    --memory=32Gi \
    --tags="model=llama3,team=ml-platform" \
    --entrypoint="python,-m,vllm.entrypoints.openai.api_server,--model,/models/llama3"
```

After creation, the service is reachable at its assigned DNS name and can be referenced
by resolvers or other services running in the same Chalk environment.

# Performance Profiling
source: https://docs.chalk.ai/docs/profiling

## Collect CPU profiles and system traces from engine nodes and upload them to cloud storage for performance analysis.

Chalk supports two profiling tools to help diagnose performance bottlenecks in your deployment:

- Perf profiling — samples CPU activity using Linux perf and uploads gzip-compressed perf script output to your bucket.
- Perfetto tracing — captures system-wide traces using Perfetto and uploads them in Perfetto's native proto format.

Both are configured as observability daemons in your
background persistence configuration. Once enabled,
a daemon runs on each Kubernetes node and periodically uploads results to your bucket.

### Choosing which tool to use

Perfetto offers a superset of the features that perf offers, but at the cost of some performance. With Perfetto, you can collect not
only CPU profile information about the nodes that Chalk runs on, but also correlate those with traces emitted by the Chalk Engine.

It is recommended to start with Perf profiling only, and move over to using Perfetto if Perf does not provide enough information.

For Perfetto to work, in addition to configuring the profiling in the background persistence (as is outlined in this guide), you also need
to enable trace outputs from your engine by setting the environment variable LIBCHALK_ENABLE_PERFETTO_TRACING=true.

### Prerequisites

- A running Chalk deployment with background persistence configured. To install, please follow this guide
- An S3 or GCS bucket for storing profiles and traces
- Write access from the background persistence service account to that bucket

### Cloud storage permissions

GCP: The service account used by background persistence
(configured via service_account_name in common_persistence_specs) needs write
access to the target GCS bucket. You also need google_cloud_project set
in common_persistence_specs.

AWS: Background persistence pods obtain AWS credentials through
IAM Roles for Service Accounts (IRSA).
The default IAM role is provisioned with broad S3 access within your account,
so any same-account bucket will work without additional configuration.
To write to a bucket in a different AWS account, add a bucket policy on the
destination bucket granting access to the background persistence IAM role ARN.

### Perf profiling

The perf collector samples CPU activity for Chalk-related processes on each node and
periodically uploads gzip-compressed perf script output to your bucket.

### Enabling perf profiling

There are two ways to enable perf profiling—through the Chalk dashboard if you manage your
background persistence deployments there, or using the Chalk CLI.

### Using the Chalk dashboard

- Navigate to Settings > Shared Resources > Background Persistence.
- Click Edit JSON.
- Add an observability_daemons array at the top level of the JSON,
alongside the existing common_persistence_specs and writers:

```
"observability_daemons": [
  {
    "keep_running_when_suspended": true,
    "perf_collector": {
      "perf_polling_frequency_hz": 99,
      "call_graph": true,
      "max_dumps_retained": 3,
      "dump_duration_seconds": 120,
      "bucket_subdirectory": "perf-data",
      "export_to": "s3://your-bucket-name"
    }
  }
]
```

- Replace s3://your-bucket-name with your bucket URI. Use gs:// for GCS.
The subdirectory name can be anything you like.
- Save and apply.

### Using the Chalk CLI

With the Chalk CLI, you can export your current configuration, edit it, and re-apply to your background persistence deployment.

```
chalk infra describe persistence --json > persistence.json
```

Open persistence.json and add an observability_daemons array at the top level,
alongside the existing common_persistence_specs and writers:

```
"observability_daemons": [
  {
    "keep_running_when_suspended": true,
    "perf_collector": {
      "perf_polling_frequency_hz": 99,
      "call_graph": true,
      "max_dumps_retained": 3,
      "dump_duration_seconds": 120,
      "bucket_subdirectory": "perf-data",
      "export_to": "s3://your-bucket-name"
    }
  }
]
```

Replace s3://your-bucket-name with your bucket URI. Use gs:// for GCS.
Then apply:

```
chalk infra apply persistence -f persistence.json
```

The CLI will show a diff of the changes and prompt for confirmation.

### Configuration reference

Sampling frequency in Hz. 99 is a standard default that avoids aliasing with timer interrupts.

Capture full call stacks with each sample. Required for flame graph generation. Defaults to true.

Maximum number of profile files to keep on disk per node. Older files are uploaded and deleted.

How often, in seconds, perf record rotates its output file and the cleanup loop runs. Defaults to 60.

Bucket URI for uploads. Use s3://bucket-name for AWS, or gs://bucket-name for GCS.

Path prefix within the bucket. Files are organized as .

### Where to find profiles

Profiles appear in your bucket organized by node name:

```
BUCKET_SUBDIRECTORY/NODE_NAME/TIMESTAMP-perf-data.gz
```

For example, with bucket_subdirectory set to "perf-data" and a node named
ip-10-0-1-42.ec2.internal:

```
s3://your-bucket-name/perf-data/ip-10-0-1-42.ec2.internal/20260220T153012-perf-data.gz
```

Each file contains gzip-compressed perf script output, filtered to Chalk-related processes.

### Tuning overhead

Perf profiling adds CPU and I/O overhead to your nodes. You can adjust
the following settings to find the right balance:

- Lower the sampling frequency: Reduce perf_polling_frequency_hz (e.g., from
99 to 49).
- Increase dump duration: A larger dump_duration_seconds produces fewer, larger
files and reduces I/O frequency.

### Perfetto tracing

The Perfetto daemon captures system-wide traces on each node. Traces can be triggered
on a fixed time interval or on-demand via an HTTP endpoint that the Chalk CLI can call.
Trace files are in Perfetto's native proto format and can be opened directly in the
Perfetto UI.

### Enabling Perfetto tracing

There are two ways to enable Perfetto tracing—through the Chalk dashboard if you manage
your background persistence deployments there, or using the Chalk CLI.

### Using the Chalk dashboard

- Navigate to Settings > Shared Resources > Background Persistence.
- Click Edit JSON.
- Add an observability_daemons array at the top level of the JSON,
alongside the existing common_persistence_specs and writers:

```
"observability_daemons": [
  {
    "keep_running_when_suspended": true,
    "perfetto_daemon": {
      "trigger": "PERFETTO_TRIGGER_TIME_INTERVAL",
      "interval": 60000,
      "max_retained_runs": 3,
      "bucket_subdirectory": "perfetto-traces",
      "export_to": "s3://your-bucket-name",
      "trigger_name": "chalk_traces",
      "config_text": "buffers: {\n  size_kb: 102400\n  fill_policy: RING_BUFFER\n}\n\ndata_sources: {\n  config {\n    name: \"linux.perf\"\n    perf_event_config {\n      all_cpus: true\n      sampling_frequency: 100\n    }\n  }\n}\n\ntrigger_config {\n  trigger_mode: CLONE_SNAPSHOT\n  triggers {\n    name: \"chalk_traces\"\n    stop_delay_ms: 1000\n  }\n}\n"
    }
  }
]
```

- Replace s3://your-bucket-name with your bucket URI. Use gs:// for GCS.
Replace the config_text value with a valid Perfetto text proto config.
- Save and apply.

### Using the Chalk CLI

With the Chalk CLI, you can export your current configuration, edit it, and re-apply to your
background persistence deployment.

```
chalk infra describe persistence --json > persistence.json
```

Open persistence.json and add an observability_daemons array at the top level,
alongside the existing common_persistence_specs and writers:

```
"observability_daemons": [
  {
    "keep_running_when_suspended": true,
    "perfetto_daemon": {
      "trigger": "PERFETTO_TRIGGER_TIME_INTERVAL",
      "interval": 60000,
      "max_retained_runs": 3,
      "bucket_subdirectory": "perfetto-traces",
      "export_to": "s3://your-bucket-name",
      "trigger_name": "chalk_traces",
      "config_text": "buffers: {\n  size_kb: 102400\n  fill_policy: RING_BUFFER\n}\n\ndata_sources: {\n  config {\n    name: \"linux.perf\"\n    perf_event_config {\n      all_cpus: true\n      sampling_frequency: 100\n    }\n  }\n}\n\ntrigger_config {\n  trigger_mode: CLONE_SNAPSHOT\n  triggers {\n    name: \"chalk_traces\"\n    stop_delay_ms: 1000\n  }\n}\n"
    }
  }
]
```

Replace s3://your-bucket-name with your bucket URI. Use gs:// for GCS.
Then apply:

```
chalk infra apply persistence -f persistence.json
```

The CLI will show a diff of the changes and prompt for confirmation.

### Generating Perfetto text proto config

The config_text field must contain a valid Perfetto text proto config.

Regardless of which trigger mode you use, the config must include a trigger_config block with
trigger_mode: CLONE_SNAPSHOT and a trigger whose name exactly matches the trigger_name field
in your daemon config. This is how Perfetto knows when to snapshot the ring buffer and emit a trace.

Write your config in a .pbtxt file. For example, a config that samples CPU at 99 Hz and snapshots
on the trigger "chalk_traces" would look like:

```
buffers: {
  size_kb: 102400
  fill_policy: RING_BUFFER
}

data_sources: {
  config {
    name: "linux.perf"
    perf_event_config {
      all_cpus: true
      sampling_frequency: 99
    }
  }
}

trigger_config {
  trigger_mode: CLONE_SNAPSHOT
  triggers {
    name: "chalk_traces"
    stop_delay_ms: 1000
  }
}
```

Because config_text is embedded as a JSON string, newlines and quotes must be escaped.
Use jq to produce the correctly escaped value from your .pbtxt file:

```
jq -Rs '.' < perfetto.pbtxt
```

This prints the file contents as a quoted, escaped JSON string. Copy the output (including
the surrounding quotes) and use it as the config_text value in your persistence config.

### Trigger modes

The Perfetto daemon supports two ways to initiate a trace capture:

- PERFETTO_TRIGGER_TIME_INTERVAL — Traces are collected automatically on a fixed interval
(controlled by the interval field). Use this for continuous background profiling.
- PERFETTO_TRIGGER_HTTP — An HTTP endpoint is exposed on port 3565. The cluster manager
can call this endpoint to trigger a trace on demand. Use this when you want to capture a trace
at a specific moment, such as during a known slow request. At most one HTTP-triggered Perfetto
daemon may be configured per environment.

When PERFETTO_TRIGGER_HTTP is used, the cluster manager is automatically configured with the
CHALK_PERFETTO_DAEMON_PORT and CHALK_PERFETTO_DAEMON_NAMESPACE environment variables.
You can then trigger a snapshot with:

```
chalk profiling perfetto-snapshot
```

Regardless of the trigger mode you use for the daemon, the underlying Perfetto config needs to use trigger_mode: CLONE_SNAPSHOT for
the system to work properly.

### On-demand tracing (HTTP trigger)

To enable on-demand tracing via chalk profiling perfetto-snapshot, use
PERFETTO_TRIGGER_HTTP as the trigger mode and set a trigger_name:

```
"observability_daemons": [
  {
    "keep_running_when_suspended": true,
    "perfetto_daemon": {
      "trigger": "PERFETTO_TRIGGER_HTTP",
      "trigger_name": "chalk_snapshot",
      "max_retained_runs": 5,
      "bucket_subdirectory": "perfetto-traces",
      "export_to": "gs://your-bucket-name",
      "config_text": "buffers: {\n  size_kb: 102400\n  fill_policy: RING_BUFFER\n}\n\ndata_sources: {\n  config {\n    name: \"linux.perf\"\n    perf_event_config {\n      all_cpus: true\n      sampling_frequency: 100\n    }\n  }\n}\n\ntrigger_config {\n  trigger_mode: CLONE_SNAPSHOT\n  triggers {\n    name: \"chalk_snapshot\"\n    stop_delay_ms: 1000\n  }\n}\n"
    }
  }
]
```

Once deployed, trigger a trace capture with:

```
chalk profiling perfetto-snapshot
```

### Configuration reference

Perfetto tracing configuration in text proto format (.pbtxt). This is required. See the
Perfetto config documentation for available
data sources and options.

How traces are initiated. Use PERFETTO_TRIGGER_TIME_INTERVAL for automatic periodic
collection, or PERFETTO_TRIGGER_HTTP for on-demand collection via
chalk profiling perfetto-snapshot.

Interval between traces in milliseconds. This is also how frequently the system will be scanned for new
trace files to upload.

Perfetto trigger name. Required. Must exactly match the trigger name in the
trigger_config block of config_text.

Maximum number of trace files to keep on disk per node. Older files are uploaded and deleted. Recommended
to set this to 0 to start uploading immediately.

Bucket URI for uploads. Use s3://bucket-name for AWS, or gs://bucket-name for GCS.

Path prefix within the bucket. Files are organized as .

### Where to find traces

Traces appear in your bucket organized by node name:

```
BUCKET_SUBDIRECTORY/NODE_NAME/TIMESTAMP-perfetto-trace.pb
```

For example, with bucket_subdirectory set to "perfetto-traces" and a node named
ip-10-0-1-42.ec2.internal:

```
s3://{your-bucket-name}/perfetto-traces/ip-10-0-1-42.ec2.internal/20260220T153012-perfetto-trace.pb
```

### Common configuration

The following fields apply to both the perf_collector and perfetto_daemon daemon objects.

Keep the daemon running when background persistence is suspended.

Kubernetes resource requests (cpu, memory). Defaults to 25m CPU and 64Mi memory.

Kubernetes resource limits (cpu, memory).

Custom container image. Omit to use the default.

### Sending data to Chalk

Once data has been collected, download it from your bucket, compress it into an archive,
and send it to your Chalk support contact.

### Perf profiles

For AWS:

```
aws s3 sync s3://your-bucket-name/perf-data/ ./perf-data/
tar czf perf-profiles.tar.gz perf-data/
```

For GCS:

```
gcloud storage rsync -r gs://your-bucket-name/perf-data/ ./perf-data/
tar czf perf-profiles.tar.gz perf-data/
```

### Perfetto traces

For AWS:

```
aws s3 sync s3://your-bucket-name/perfetto-traces/ ./perfetto-traces/
tar czf perfetto-traces.tar.gz perfetto-traces/
```

For GCS:

```
gcloud storage rsync -r gs://your-bucket-name/perfetto-traces/ ./perfetto-traces/
tar czf perfetto-traces.tar.gz perfetto-traces/
```

### Disabling profiling

When profiling is no longer needed, remove the observability_daemons entry from
your background persistence configuration and re-apply. The profiling daemonset will
be removed automatically.

In the dashboard, navigate to Settings > Shared Resources > Background Persistence,
click Edit JSON, delete the observability_daemons block, and save.

With the CLI:

```
chalk infra describe persistence --json > persistence.json
# Remove the observability_daemons array from persistence.json
chalk infra apply persistence -f persistence.json
```

# Blue-Green Deployments
source: https://docs.chalk.ai/docs/blue-green-deployment

## Set up blue-green deployments for reliability.

Chalk offers a variety of tools and strategies for testing your features, resolvers, and
queries in the process of deploying them to production. Testing through writing unit tests
and integration tests can ensure that your code is working as expected.
Chalk also offers blue-green deployments for a release strategy that can further minimize downtime
and risk when deploying changes. If your team is interested in using blue-green deployments in your
production environment, please reach out to the Chalk team.

### Blue-Green Deployments with Chalk

Chalk offers blue-green deployments as a way to minimize downtime when deploying new code by
running two deployments, one "blue" and one "green", in parallel. The blue deployment is the current
production deployment, while the green deployment is the new version of the code that is being
released. Using deployment tags, Chalk can route a specified percentage of traffic to the blue
or green deployment, allowing for a gradual rollout of the new code, as well as an easy path to
rollback if any issues arise.

### Releasing using Blue-Green Deployments

Once you have confirmed with the Chalk team that blue-green deployments are enabled in your Chalk environment,
there are a few ways that you can start to use blue-green deployments.

### Full rollouts using Blue-Green Deployments

The simplest way to start to use blue-green deployments is to use the --bluegreen tag when deploying your code.
When you run chalk apply --bluegreen, that will automatically tag your latest deployment with either blue
if the latest deployment was tagged green, or green if the latest deployment was tagged blue. Then, when you're
ready to migrate traffic to your new deployment, you can run chalk traffic promote, which will migrate traffic from
the deployment currently in use to the other tagged deployment. The following example demonstrates how to use
these blue-green deployments.

Suppose you have made changes that you now want to release. You can then run

```
$ chalk apply --deployment-tag blue # or `green` depending on the current deployment
```

This will create a new deployment tagged with blue or green. Then, you can choose to migrate traffic to the
new deployment by running:

```
$ chalk traffic promote
```

If previous deployment was tagged blue and the latest deployment was tagged green, this command migrates 100%
of the traffic from the blue deployment to the green deployment. You can then monitor the green deployment
traffic. If you encounter any errors with your new deployment, then you can once again run chalk traffic promote and
it will migrate traffic from the green deployment back to the blue deployment. This allows you to easily rollback
during releases.

### Gradual rollouts using Blue-Green Deployments

If you would like to gradually roll out your new deployment with staged increments of traffic, you can
use the --deployment-tag flag to specify a new deployment towards which to direct traffic.
To get started with blue-green deployments, you can tag the current deployment with blue. To do so you can
run the following Chalk CLI commands:

```
$ chalk apply --deployment-tag blue
$ chalk traffic set --tags blue=100
```

This will tag the current deployment with blue and direct 100% of traffic to the blue deployment. Then, when you
are ready to begin rolling out the next deployment, you can deploy the new version of code with the tag green.

```
$ chalk apply --deployment-tag green
$ chalk traffic set --tags blue=90,green=10
```

This will direct 90% of traffic to the blue deployment and 10% of traffic to the green deployment. You can
verify the traffic distribution by running chalk traffic get.

```
$ chalk traffic get

tags:
     - deployment_id: cm9n46thy000bwe6y784y4j0l
       tag: blue
       weight: 90
     - deployment_id: cm9n3vx7c0004we6yefnsw8kg
       tag: green
       weight: 10
```

Then, you can gradually increase traffic to the green deployment until it is at 100%, and for the next time
you release, you can tag the latest deployment with blue and migrate traffic from the green deployment to the
even newer blue deployment. This workflow enables you to have fine-tuned control over the traffic distribution
between your deployments. Furthermore, Chalk will automatically scale down unused deployments to minimize unnecessary
resource usage. If you run the command chalk traffic set and do not specify some amount of traffic for a
tagged deployment, then Chalk will recognize that the deployment is no longer in use and will scale it down.

### Managing your Blue-Green Deployments

In order to create a new tagged deployment in Chalk, you can either specify a --deployment-tag when
running chalk apply, or you can use the --blue-green flag to automatically target the inactive
tag for the new deployment. In addition to creating new tagged deployments, you can also use the
Chalk CLI command chalk traffic to manage your blue-green deployments. To view all available
commands, you can run chalk traffic --help.

To view the current traffic distribution between your blue and green deployments, you can run:

```
 $ chalk traffic get
 tags:
     - deployment_id: cm9n46thy000bwe6y784y4j0l
       tag: blue
       weight: 50
       mirror_weight: 10
     - deployment_id: cm9n3vx7c0004we6yefnsw8kg
       tag: green
       weight: 50
       mirror_weight: 0
```

To mirror a percentage of traffic to a tagged deployment, you can use the chalk traffic mirror command:

```
$ chalk traffic --mirror blue=15,green=5   
  tags:                                           
      - deployment_id: cm9n46thy000bwe6y784y4j0l  
        tag: blue                                 
        mirror_weight: 15                         
      - deployment_id: cm9n3vx7c0004we6yefnsw8kg  
        tag: green                                
        mirror_weight: 5    
```

As shown above, you can you chalk traffic promote and chalk traffic set to configure the
distribution of traffic between your blue and green deployments.

Once you roll out your new deployment, by default we would still keep pods up for your inactive
deployment to enable a fast rollback. However, if you would like to spin down pods for any
inactive deployment, you can also use chalk traffic suspend to essentially set the
traffic weight to nil, which will scale down the pods for that deployment.

```
$ chalk traffic suspend --deployment-tag blue
```

### Should I use Blue-Green Deployments?

Blue-green deployments are a powerful tool for minimizing downtime through a gradual rollout deployment. However,
running two deployments in parallel also has resource implications and may not be necessary for all teams. We
would recommend blue-green deployments for teams that have a high volume of traffic in their production environments
where the benefit of minimizing downtime risk is worth the cost of additional resources required.

If you are interested in using blue-green deployments, please reach out to the Chalk team and we can help you
determine what configurations are best suited for your release strategy.

### Mirror Traffic

Chalk also offers a mirror traffic feature that allows you to mirror traffic from your production deployment to a
new deployment. This is useful for testing new features in a production-like environment without affecting the
production traffic. To use mirror traffic, you can run the following command:

```
# Mirror 5% of traffic to the green deployment.
$ chalk traffic set --tags blue=100,green=0 --mirror green=5
```

Note: mirror traffic does not block responses for existing production traffic. It simply mirrors the traffic to the
new deployment without waiting to receive a response from the new deployment.

Metrics, logs, and traces from the mirrored traffic will be available in the new deployment. Queries will not
impact the online store, but will impact the offline store if the new deployment is configured to write to
the offline store. This permits statistical analysis of the new deployment using tooling like the query log
or the offline store.

### Light-weight Cookbook

You can make use of only mirroring with minimal reference to blue-green by:

- Deploying your new code with the --deployment-tag flag to tag the deployment.
- Mirroring traffic to the new deployment using the --weight flag to specify the percentage of traffic to mirror.
- Monitoring the new deployment for any issues.

Example commands:

```
# Make the new deployment -- it won't receive any traffic yet
$ chalk apply --deployment-tag green

# Mirror 5% of traffic to the green deployment
$ chalk traffic set --tags blue=100,green=0 --mirror green=5

# Monitor the new deployment for any issues. Once you're satisfied, you can promote it to production with:
$ chalk traffic promote
```

A key point is that the mirrored deployment does need to have 0% weight specified, which indicates to Chalk that
the deployment should have pods running to handle the mirrored traffic, but not to handle any production traffic.

Failing to specify the --weight flag will result in Chalk not running any pods for the off-color deployment.

# Multi-Region Failover
source: https://docs.chalk.ai/docs/multi-region-failover

## Configure multi-region failover for high availability on AWS.

Chalk supports multi-region failover on AWS so that your feature serving infrastructure
remains available even if an entire region goes down. This guide covers how to set up
active-passive failover using multiple EKS clusters, resource groups, and Route 53
failover routing.

### Architecture overview

Multi-region failover works by deploying Chalk into EKS clusters in two or more AWS
regions. Each region runs an independent set of Chalk services behind its own ALB.
Route 53 failover routing directs traffic to the healthy region based on health checks
against each ALB.

The key components are:

- Multiple EKS clusters -- one per region, each running a full Chalk data plane.
- Resource groups -- each region's Chalk deployment is assigned to a distinct resource group with a unique hostname.
- Route 53 failover routing -- a single DNS name resolves to the healthy region's ALB, with automatic failover when health checks fail.

### Setting up multi-region failover

### 1. Create EKS clusters in each region

Work with the Chalk team to provision EKS clusters in your target regions (for example,
us-east-1 and us-west-2). Each cluster runs a complete Chalk data plane with its
own query servers, online store, and background persistence workers.

### 2. Configure resource groups

Each regional deployment is assigned to its own resource group.
Resource groups provide workload isolation and give each region a unique hostname for
its query servers.

For example, you might have:

| Region | Resource group | Hostname |
|---|---|---|
| us-east-1 | prod-east | prod-east.query.example.com |
| us-west-2 | prod-west | prod-west.query.example.com |

Each resource group's query server exposes a /healthz endpoint that the ALB uses for
health checking. When the query server is healthy, /healthz returns a 200 response.

### 3. Configure Route 53 failover routing

Create a Route 53 hosted zone with failover routing records that point to the ALB in
each region:

- Primary record -- points to the ALB in your primary region (e.g. us-east-1),
with a health check against the /healthz endpoint.
- Secondary record -- points to the ALB in your secondary region (e.g. us-west-2),
with its own health check.

Both records share the same DNS name (e.g. chalk-failover.example.com). Route 53
resolves this name to the primary ALB when it is healthy, and automatically switches to
the secondary ALB when the primary's health check fails.

Route 53 health checks poll the /healthz endpoint on each ALB. The default health check
interval is 30 seconds. You can configure the failure threshold (number of consecutive
failures before failover) and request interval to tune failover speed vs. sensitivity.

### 4. Point clients at the failover hostname

Configure your application to send queries through the failover DNS name using the
query_server parameter on ChalkClient:

```
from chalk.client import ChalkClient

client = ChalkClient(
    query_server="https://chalk-failover.example.com",
)

result = client.query(
    input={"user.id": 123},
    output=["user.name", "user.risk_score"],
)
```

The client does not need any awareness of which region is active. DNS resolution
handles routing transparently.

### How failover works

Under normal operation, Route 53 resolves the failover hostname to the primary region's
ALB. All client traffic flows to the primary EKS cluster.

When the primary region becomes unhealthy:

- The ALB health check against /healthz begins failing.
- Route 53 detects consecutive health check failures (typically within 1-2 minutes).
- Route 53 updates DNS to resolve the failover hostname to the secondary region's ALB.
- Client traffic is routed to the secondary EKS cluster.

When the primary region recovers:

- The /healthz endpoint starts returning 200 again.
- Route 53 detects the recovery and switches DNS back to the primary region.

Failover is DNS-based, so clients must respect DNS TTLs. Set a low TTL (e.g. 60 seconds)
on the failover record to minimize the window during which clients may still resolve to
the unhealthy region.

### Data replication

Each region's Chalk deployment operates independently, but the underlying data stores
must be replicated across regions so the passive region can serve traffic with current
feature values.

### Online store -- DynamoDB Global Tables

Chalk uses DynamoDB Global Tables
to replicate online feature values across regions. Global Tables provide automatic,
asynchronous replication so that the passive region's online store stays up to date
with writes from the active region. No application-level changes are required -- both
regions read and write to the same logical table.

### Persistence coordination -- MSK Replicator

Chalk uses Amazon MSK (Managed Streaming for Apache Kafka)
to coordinate background persistence operations such as writing computed features to the
online and offline stores. In a multi-region deployment, MSK must be configured for
cross-region replication using
MSK Replicator.

MSK Replicator continuously replicates topics from the active region's MSK cluster to
the passive region's MSK cluster. This ensures that persistence operations initiated by
the active region -- such as online store writes and offline store ingestion -- are also
applied in the passive region. When failover occurs, the passive region's persistence
workers pick up from the replicated topic offsets.

### Metadata plane -- RDS Aurora

The Chalk metadata plane uses
Amazon Aurora as its sole state store. Because
Aurora is the only stateful component, multi-region metadata plane availability maps
directly to Aurora's cross-region capabilities:

- Active-passive -- use an
Aurora Global Database
with a read replica in the secondary region. Aurora handles asynchronous replication
and supports managed failover to promote the secondary cluster when the primary
region is unavailable.
- Active-active -- use
Aurora Global Database write forwarding
or an Aurora multi-master configuration so that both regions can accept writes.

The choice between active-passive and active-active for the metadata plane should match
the routing strategy you choose for the data plane (see
Active-active vs. active-passive below).

### Offline store

Offline stores are typically regional. Training data queries and dataset generation should
target a specific region rather than the failover hostname.

### Deployments

chalk apply should target both regions to keep feature definitions and resolver code in
sync. You can automate this in CI/CD by deploying to each resource group.

### Recovery point objective (RPO)

RPO -- the maximum acceptable amount of data loss measured in time -- depends on the
failure scenario:

| Failure scenario | RPO | Notes |
|---|---|---|
| Single AZ failure | 0 | EKS and DynamoDB span multiple AZs within a region. No data is lost. |
| Full region failure (recoverable) | Replication lag | Determined by DynamoDB Global Tables replication lag and MSK Replicator lag, typically seconds. Once the primary region recovers, any in-flight writes that had not yet replicated are recovered from the primary. |
| Full region failure (permanent loss) | Replication lag | If the primary region is permanently lost, any writes that had not yet replicated to the passive region are lost. RPO equals the replication lag at the time of failure. |

You can monitor DynamoDB Global Tables replication lag via the ReplicationLatency
CloudWatch metric, and MSK Replicator lag via the ReplicationLatency metric on your
replicator. Under normal conditions both are single-digit seconds.

### Active-active vs. active-passive

The architecture described above is active-passive: only one region serves live
traffic at a time. Chalk also supports active-active configurations using Route 53
weighted or latency-based routing, where both regions serve traffic simultaneously.
Contact the Chalk team to discuss which approach is best for your availability and
latency requirements.

# Tutorial: Fraud Detection Pipeline
source: https://docs.chalk.ai/docs/fraud-tutorial

## Build a feature pipeline for fraud detection.

### Introduction

Chalk helps you build out feature pipelines for training and serving machine learning models.

The building blocks of Chalk are features and resolvers.
Features specify what you want your data to look like and resolvers tell Chalk where to find your "data".

In Chalk, features are defined as Python classes with annotated attributes.
Note how the User class is annotated with the @features decorator that's imported from chalk.features.

```
from chalk.features import features
import datetime as dt

@features
class User:
    id: int
    birthday: dt.datetime
    name: str
    email: str

    # computed features
    username: str
    age: int
    is_adult: bool
```

Features are the abstract underlying attributes of your data.
In the example above id, birthday, name, email, username, age, and is_adult are all features.
Features are grouped together (namespaced) in what are called feature
classes.
For instance, the User class is a feature class (also sometimes referred to as a feature set).
Specific instances of a feature class are feature class instances.

Note, you define your features before defining how they will be computed.
Some of these features might come directly from a database table: for instance, the id, birthday, and name fields that
we've defined above. Some might be calculated in real time based on the current timestamp (like the age feature) or a
different upstream feature (like the is_adult feature, which will depend on the age feature).

You could deploy the code above to Chalk and it would be considered valid.
However, if you tried to query for a field (for example, if you asked chalk to return the name of a user with id 1)
then you'd get an error.

In particular, you would get the following error:

```
$ chalk query --in user.id=1 --out user.name
Results

No scalar features


Errors

Resolver Not Found user.age

Failed to find any valid resolver for feature: 'user.name' and no `default` value or
`max_staleness` was specified for 'user.name', so the feature cannot be defaulted or
resolved from the online store.
```

We'll talk more about deploying code to Chalk later, but, if you'd like to, you're welcome to
skip ahead to get a better sense of deploying code to Chalk and running queries.

This should not be surprising.
Chalk has no connection to your underlying data.
So it doesn't know how to get the name of the user with an id of 1 (or any id for that matter).

In particular, the error message tells us that a "Resolver" was not found.
A resolver is a function that takes in features and outputs features.
Broadly, there are two types of resolvers: root and non-root.
Root resolvers don't take any features (or take only a primary key) as their input and are used to
fetch data from external sources.

In the User example we sketched out above, you could think of a root resolver as a SQL query that reads from a
users table in an external database.

While there are exceptions, this is what the majority of root resolvers look like.
For example, to read from the users table in your PostgreSQL database, you might write a get_users.chalk.sql file,
with the following contents:

```
-- source: postgres
-- resolves: User

select id, birthday, email, name from users
```

By writing this file, you've defined a SQL resolver, named get_users, which knows how to resolve birthday, name,
or email for any given id in the users table.
At this point, you might have noticed that the SQL query above doesn't explicitly know how to get the birthday or name
of a given id, it just returns all users.
Chalk gets around this by pushing filters into your SQL queries.

Let's say you've defined the SQL resolver above and deployed it to Chalk.
You rerun the query that failed above:

```
$ chalk query --in user.id=1 --out user.name
```

Chalk will look at the resolvers you've defined and ask "given a User.id, can I calculate a User.name".
It will see the SQL resolver defined above and realize that it can be used to get User.name from a User.id.
It will push the id filter into the SQL query, running.

```
select name from users
where id=1
```

In addition to the filter a projection will be pushed into your SQL query: only the name column
is requested.
When running a query, Chalk processes the minimum amount of data required to calculate a desired output features.

Getting this to work fully, will involve setting up a database connector to Chalk and deploying code, both of which
we will cover later.
For now, it is important to note that the process of defining resolvers is incredibly modular.

Now lets look into defining a non-root resolver, which computes a User's email username.

In Chalk, non-root resolvers take one of two forms:

- Python functions with feature annotations,
- inline expressions.

We will look at both variants, but functionally they are similar.
Both take input features
and generate output features.

```
from chalk import online
from chalk.features import features
import datetime as dt

@features
class User:
    id: int
    birthday: dt.datetime
    name: str
    email: str

    # computed features
    username: str
    age: int
    is_adult: bool

@online
def get_email_username(email: User.email) -> User.username:
    return email.split('@')[0]
```

As mentioned above, this could also be written as an inline expression, like so:

```
from chalk import online
from chalk.features import features
import datetime as dt

@features
class User:
    id: int
    birthday: dt.datetime
    name: str
    email: str

    # computed features
    username: str = F.split_part(_.email, delimiter="@", index=0)
    age: int
    is_adult: bool
```

The advantage of inline expressions is that they are statically compiled into the execution engine, which often
provides performance advantages.
Chalk also tries to statically compile Python resolvers by parsing the AST of the function!

By writing the get_email_username Python function, we've defined another resolver.
If we deploy this new code to Chalk, we can now query for the username of a user with a given id.

```
$ chalk query --in user.id=1 --out user.username
```

When running the above query, Chalk will identify that it knows how to determine an email
from a given id using the get_user resolver.
It will also determine that it knows how to calculate a username for an email using the get_email_username resolver.
Chalk will execute both these resolvers and return the result.

The focus on data instead of pipelines may be unfamiliar at first.
Traditional orchestration platforms like Airflow or Dagster
explicitly compose functions which produce data into a DAG of tasks.
With Chalk, the DAG of resolvers is defined implicitly by the features they produce.
This architecture makes it easy to build out feature pipelines that are reusable and composable.
Chalk handles tracking your features for temporal consistency, running your resolvers in parallel, and horizontally
scaling your feature pipelines.

Alright, enough with the intro. Let's get started building!

### Fraud Detection Pipeline

This tutorial walks through the process of building a feature pipeline for fraud detection.
We'll cover the full feature development lifecycle:

- Data Modeling - Creating feature classes for the data we want to compute.
- SQL Resolvers - Mapping data from SQL sources to feature classes.
- Python Resolvers - Defining resolvers in Python that compute derived features and call external APIs.
- Inference - Integrating Chalk into production decisioning systems.
- Backtesting - Experimenting with new features

In this tutorial, we'll assume the following existing data architecture:

- a PostgreSQL database with three tables: users, accounts, and transactions.
- a Snowflake analytics database with the same three tables: users, accounts, and transactions,
which is periodically updated in response to changes in the PostgreSQL database.

Before you get started, make sure you have the Chalk CLI installed.

If you want to skip ahead, you can find the full source code for this tutorial on GitHub.

### Define features

We'll start by modeling out the Users feature class.

We'll start simple with three scalar features: User.id, User.name, and User.email.
First, we'll create a new file called feature_sets.py where we'll define a User class decorated with @features.

```
from chalk.features import features

@features
class User:
    id: int

    # The name the user provided to us at signup.
    # :owner: identity@chalk.ai
    # :tags: pii
    name: str

    # :tags: pii
    email: str
```

Note that at this point we haven't defined how to compute these features.
We are only thinking about the data that we would like to have.

### Primary keys

There are a few things to note here. First, all our feature classes need to have a unique id field.
By default, this is the field named id.
However, if you want to use a different feature name as the primary key, you can specify it by annotating the primary key feature with the Primary type.

```
from chalk.features import features, Primary

@features
class User:
-   id: int
+   user_id: Primary[int]
    name: str
    email: str
```

### Tags, Descriptions, and Owners

In our features above, we've added some comments and annotations. These are optional, but can be useful for documentation and for setting alerting policies.
For example, you may wish to send Pagerduty alerts to different teams based on the owner of the related feature.

All of the comments and tags from the code also show up in the Chalk dashboard, and are indexed for search.

For example, we've added a pii tag to the name and email fields.
This means that these fields will be treated as personally identifiable information and will be subject to additional restrictions.

### Has-One Relationships

Next up, we'll define a feature class related to our User.
We'll call this class Account and it will represent a user's bank account.

```
from chalk.features import features

@features
class Account:
    id: int

    # The name of the owner of the account.
    title: str

    # The id of the user that owns this account.
    user_id: int

    # The balance of the account, in dollars.
    balance: float
```

This should look much like what we did for the User class.
However, we may want to link these two classes together.
We can do this by adding a user field to the Account class.

```
@features
class Account:
    id: int
-   user_id: int
+   user_id: User.id
    balance: float

+   # The user that owns this account.
+   user: User
```

This denotes that each account has one user, and that the Account.user_id and the User.id are equal and of type int,
as described by User.id.

Once we've defined the relationship on one side of the join, we can define the inverse relationship on the other side without
needing to specify the foreign key again.

```
@features
class User:
    id: int
    name: str
    email: str

+   # The account that this user owns.
+   account: "Account"
```

Note that the account annotation in the User feature class is in quotes.
Because the Account class is defined later in the file, Chalk will recognize this as a valid feature reference
and process it correctly.

### Has-Many Relationships

The final feature entity that we'll define in this tutorial is for transactions.
Each account has many transactions and each transaction is linked to a single account.
We'll define the Transaction class and link it to our Account class as follows:

```
+ from enum import Enum
- from chalk.features import features
+ from chalk.features import features, DataFrame, FeatureTime

+ class TransactionStatus(str, Enum):
+     PENDING = "pending"
+     CLEARED = "cleared"
+     FAILED = "failed"
+
+ @features
+ class Transaction:
+    id: int
+
+    # The id of the account that this transaction belongs to, set to a join.
+    # We refer to features and feature classes defined further down in the file
+    # using quotation marks, so Chalk will recognize that it is a valid
+    # feature reference to be processed later.
+    account_id: "Account.id"
+
+    # The amount of the transaction, in dollars.
+    amount: float
+
+    # The status of the transaction, defined as an enum above.
+    status: TransactionStatus
+
+    # When the transaction occurred
+    created_at: FeatureTime
+
+    # Because we define the join condition between
+    # `Transaction` and `Account` below, we don't
+    # need to repeat it here.
+    account: "Account"

@features
class User:
    id: int
    name: str
    email: str

    # The account that this user owns.
    account: "Account"

@features
class Account:
    id: int
    user_id: User.id
    balance: float
    user: User
+   transactions: DataFrame[Transaction]
```

This is the first time we're seeing the DataFrame type.

A Chalk DataFrame models tabular data in much the same way that Pandas does. However, there are some key
differences that allow the Chalk DataFrame to increase type safety and performance.

Like pandas, Chalk's DataFrame is a two-dimensional data structure with rows and columns.
You can perform operations like filtering, grouping, and aggregating on a DataFrame.
However, there are two main differences.

- Lazy implementation - Chalk's DataFrame is lazy and can be backed by multiple data sources, where a pandas.DataFrame executes eagerly in memory.
- Usable as a type - Chalk's DataFrame[...] can be used to represent a type of data with pre-defined filters.

You might also notice that we used an Enum feature.
Chalk supports many feature types, including Enums, lists/sets, and dataclasses.

We also added a created_at field to the Transaction class of type FeatureTime.
FeatureTime is a special annotation that can only be assigned to a single feature in a feature class.
This feature specifies the logical time of a feature instance—it is used for point in time correctness and incremental updating.
We'll cover both later in this tutorial.

### Configuring SQL sources

The primary source of data for most companies are SQL databases (note, by SQL database we don't mean relational databases:
we mean any database that can be queried with SQL—in practice this means pretty much any of them).
Chalk can automatically ingest data from SQL databases and map results into feature classes.

In our example application, we have two databases: PostgreSQL and Snowflake.
Our PostgreSQL database is the primary database used in our codebase, and our Snowflake database is used for analytics,
with tables populated from DBT views and batch jobs.

To configure your SQL sources in Chalk, we'll:
1). Add your data sources to the Chalk dashboard
2). Define the data sources in your Chalk code.

### Adding Data Sources in the Chalk Dashboard

To add your data sources to the Chalk dashboard, go to the Data Sources tab of the dashboard and click on the
Add a data source button.
You can then select the type of data source you want to add.

Select PostgreSQL and fill in the required information.
Repeat the same process with a Snowflake data source.
Keep track of the names that you've given to each of your data sources: these will be used in the next step. We recommend
naming your PostgreSQL data source postgres and your Snowflake data source snowflake.

Note, the data source connection information you add in the dashboard will be stored securely using the secrets manager
of your cloud provider.

### Define Your Data Sources in Your Chalk Code

To define your data sources, you'll need to create a datasources.py file that contains a SnowflakeSource
and a PostgreSQLSource:

```
from chalk.sql import SnowflakeSource, PostgreSQLSource

# if you named your postgres or snowflake resolvers something other than `postgres`
# and `snowflake`, you'll have to update the code accordingly.
snowflake = SnowflakeSource(name="postgres")
postgres = PostgreSQLSource(name="snowflake")
```

Now that we've defined our data sources, we can use them to create root SQL resolvers.

### Online data

Chalk's preferred way to ingest data from SQL databases is to use SQL file resolvers.

With SQL file resolvers, you can write your root resolvers in SQL, and use whatever database tooling you're familiar with to test, lint, and debug your code.

To create a SQL resolver, add a file to your project directory with the extension .chalk.sql.
You can now write a SQL query in this file.
You will also need to add metadata to the top of the file to tell Chalk how to ingest the data.

For example, say that we want to resolve the name and email features of our User feature class from a PostgreSQL table.

To do this, we can write the following SQL file resolver:

```
-- get users from postgres.
-- resolves: User
-- source: postgres
select
    id,
    full_name as name,
    email
from users
```

The resolves key (--resolves: User) tells Chalk which feature class the columns in the select statement should be mapped into.
Then, the target names of the query are compared against the names of the features on the specified feature class.
If the names match after stripping underscores and lower-casing, the select target is mapped to the feature.

In the example above, we aliased the full_name column to name, so it will be mapped to the name attribute on the User feature class.

Chalk validates your SQL file resolvers when you run chalk apply.
If you want to validate your code without deploying, you can run the chalk lint command.

The source key (-- source: postgres) tells Chalk which integration to use to connect to the database.

Other comments in the SQL file resolver are indexed by Chalk and can be searched in the Chalk dashboard.
In the example resolver above, the comment get users from postgres becomes the description of the resolver in the dashboard.

Let's also add our get_accounts  and get_transactions SQL file resolvers:

```
-- get accounts from postgres.
-- resolves: Account
-- source: postgres
select
    id,
    user_id,
    balance,
from accounts
```

```
-- get transactions from postgres.
-- resolves: Transaction
-- source: postgres
select
    id,
    account_id,
    amount,
    status,
    created_at
from transactions
```

### Deploying!

Now that we've written a few resolvers, we can deploy our feature pipeline and query our data in realtime.
To deploy you'll want to run chalk apply.
You will be shown the changes that you've made since your last deployment and prompted for confirmation

```
chalk apply
✓ Found resolvers
✓ Successfully validated features and resolvers!
✓ Checked against live resolvers
Added Features

    Name
───────────────────────────
 +  transaction.id
 +  transaction.account_id
 +  transaction.amount
 +  transaction.status
 +  transaction.created_at
 +  transaction.account
 +  user.id
 +  user.name
 +  user.email
 +  user.account
 +  account.id
 +  account.user_id
 +  account.balance
 +  account.user
 +  account.transactions


  Would you like to deploy?  [y/n]
```

If you accept, chalk will build and deploy your new code. Once that's done, you can start querying your data in realtime!

### Querying

Now that we've deployed our feature pipeline, we can query our data in realtime.
One of the easiest ways to do this is from the Chalk CLI.

```
$ chalk query --in user.id=1 --out user.name --out user.email

user.name     "John Doe"
email         "john@doe.com"
```

This query will fetch the name and email attributes from the User feature class for the user with id=1, hitting the PostgreSQL database directly.

### Push-down filters

Note that in SQL file resolver that we wrote, we didn't include a where clause.
However, Chalk automatically pushes down filters to the database when querying features.
The SQL query that executes against our PostgreSQL database is:

```
select
    id,
    full_name as name,
    email
from users
+ where id = 1;
```

Chalk can also push down non-primary key filters to SQL databases.
For example, to fetch all transactions for a user, Chalk will modify the get_transaction resolver to include a where clause for the user's account_id:

```
select
    id,
    account_id,
    amount,
    status,
    date
from txns
+ where account_id = 38;
```

You can see this in action, by querying for a user's transactions:

```
$ chalk query --in user.id=1 --out user.account.transactions
Results

No scalar features

user.account.transactions

 id      account_id   amount    status     created_at
─────────────────────────────────────────────────────────────────────────────────────
 197524  38           12.00     "cleared"  "2023-12-02T21:05:54.057868+00:00"
 198604  38           27.51     "cleared"  "2023-04-29T22:27:12.058023+00:00"
 210326  38           93.27     "cleared"  "2023-02-17T21:49:27.058144+00:00"
 228363  38           1.05      "cleared"  "2023-04-20T21:46:33.058240+00:00"
 230225  38           23.91     "cleared"  "2023-06-09T03:07:44.058314+00:00"
 235551  38           12.20     "failed"   "2022-12-26T15:45:07.058416+00:00"
```

### Derived Features

We've noticed that some fraudsters try to link stolen accounts to our platform and attempt to transfer money through our system.
To detect this behavior, we want to compute a similarity score between the user's name and the account's title.

We'll start by adding this new feature, account_name_match, to our User feature class.

```
@features
class User:
    id: int
    name: str
    email: str
    account: "Account"

+   # The similarity between the user's name and the account's title.
+   account_name_match: float
```

Next, we'll define a resolver that computes this feature.
We'll use Jaccard similarity to compute the similarity score.

```
from src.feature_sets import User
from chalk import online

@online
def account_name_match(
    title: User.account.title,
    name: User.name,
) -> User.account_name_match:
    """Docstrings show up in the Chalk dashboard"""
    intersection = set(title) & set(name)
    union = set(title) | set(name)
    return len(intersection) / len(union)
```

The @online decorator tells Chalk that this resolver should be called
in realtime when the User.account_name_match feature is requested.
Our feature dependencies are declared in the function signature as User.account.title and User.name.
Chalk will automatically retrieve User.account_id and User.name with our get_user.chalk.sql resolver.
Then, using this account_id, Chalk will retrieve Account.title from the get_account.chalk.sql resolver.  Lets deploy our code.

```
$ chalk apply --branch tutorial
✓ Found resolvers
✓ Deployed branch
```

Note, this time we are using a branch (by specifying the --branch <name> flag).
In testing, new features, we recommend deploying your feature pipeline to a branch, which allows you to test your changes without affecting your production feature pipelines.
An additional benefit of branches is that they are incredibly lightweight—they should deploy pretty much instantly.

### Testing

Resolvers are callable functions, so we can also test them like any other Python function.
Let's test our new resolver by writing a unit test:

This is one of the only times when you'll explicitly call your resolver functions.
We covered this idea already in the intro, but since its one of the central concepts behind Chalk it is worth reiterating.
Most of the time, Chalk will determine which resolvers it needs to run to compute the features you've requested in a query.
This is just like how a SQL database decides how to compute the output features you've requested.

```
from src.resolvers import account_name_match

def test_names_match():
    """Resolvers can be unit tested exactly as you would expect.

    Here, the `account_name_match` resolver should return 1.0
    because the `title` and `name` are identical.
    """
    assert 1 == account_name_match(
        title="John Coltrane",
        name="John Coltrane",
    )

def test_names_completely_different():
    """The `account_name_match` resolver should return 0
    because the `title` and `name` don't share any characters.
    """
    assert 0 == account_name_match(
        title="John Coltrane",
        name="Zyx",
    )
```

If you want to learn more, we also provide additional docs on testing resolvers.

### Reverse ETL

Let's say we have a rather complex feature that we can't serve in realtime because it increases the latency of a query
too much for a particular production use case.
For instance, lets say we want to add a new feature to our users that indicates the average time between their transactions.
Maybe we believe that we can use this to detect whether a new transaction is fraudulent.

To add this feature, we'd add it to the User feature class:

```
@features
class User:
    id: int
    name: str
    email: str
    account: "Account"

    # The similarity between the user's name and the account's title.
    account_name_match: float

    # The average time between each of a user's transactions, from the last
    # 30 days, in ms.
+   average_time_between_transactions_30d: float
```

We would then write a resolver to calculate this feature:

```
from chalk import online
from chalk.features import after

@online
def get_average_time_between_transactions(
    transactions: User.account.transactions[
      Transaction.created_at,
      after(days_ago=30)
    ]
) -> User.average_time_between_transactions:
  """Computes the average time between transactions for a user"""

  # conversion to polars is cheap since both Chalk and Polars DataFrames
  # Use Arrow as their memory representation.
  df = transactions.to_polars()

  # Get the date column, convert to milliseconds timestamps, and sort
  date_col = df.collect().get_column(
    str(Transaction.created_at)
  ).dt.timestamp("ms").sort()

  return (date_col - date_col.shift(1)).mean()
```

For good measure, lets also add this to our tests and make sure that it is running as expected:

```
import datetime as dt

from chalk.features import DataFrame

from src.resolvers import get_average_time_between_transactions

def test_get_average_time_between_transactions():
    """To unit test Dataframe taking resolvers, you can construct and
    pass in a Chalk DataFrame:
    """
    now = dt.now(tzinfo=dt.timezone.utc),
    transactions = DataFrame({
      Transaction.created_at: [
        # will be filtered out since it did not occur in last 30d
        dt.datetime(1990, 1, 1, tzinfo=dt.timezone.utc),
        now,
        now - dt.timedelta(seconds=1), # diff = 1000
        now - dt.timedelta(seconds=2), # diff = 1000
        now - dt.timedelta(seconds=3), # diff = 1000
        now - dt.timedelta(seconds=4), # diff = 1000
        now - dt.timedelta(seconds=6), # diff = 2000
      ]                                # -----------
    })                                 #        6000 / 5 = 1200

    assert 1200 == get_average_time_between_transactions(
      transactions
    )
```

Lets deploy this new feature to a branch and run a couple test queries:

```
chalk apply --branch new-fraud-feature
```

```
chalk query \
  --in user.id=1 \
  --out user.average_time_between_transactions_30d \
  --branch new-fraud-feature
```

After some testing, we realize a couple of things:
1). This feature is too slow to compute in real time (for our use case),
2). This feature doesn't change very often.

In practice, even executing the above resolver in realtime should be really fast.
When building new features, do some testing.
You may not even need to reverse-ETL features into the online store to achieve your target latency.
Reverse-ETL-ing features into the online store adds state and complexity to your feature pipeline.
We recommend only doing this if you are unable to achieve your latency targets.

We decide to reverse-ETL this computed feature from our snowflake data store into our Chalk online store. At a high level,
this means that periodically (maybe once a day), we'll:

- Look for all users with new transactions in our snowflake data source,
- Recompute the average_time_between_transactions_30d for these users,
- Load the new average_time_between_transactions_30d values into the Chalk online store.

Of note, we don't want to use our PostgreSQL database for this, we want to use Snowflake, which is optimized for bulk data
loads unlike Postgres.
As a result, we'll need to define some offline resolvers.

So far we've only written online resolvers.
You can think of offline resolvers as overrides for online resolvers that are run in bulk data request scenarios.
At a high level offline resolvers let you pull your feature data from data stores that are optimized for bulk data
loading—this is exactly what we want for our reverse-ETL process.

To set up a reverse-ETL process, we'll need to do three things:

- set a staleness policy on your target feature,
- add offline resolvers (technically optional, but strongly recommended),
- create a scheduled query.

### Setting a Max Staleness on Our Feature

We can have Chalk reverse-ETL our offline data into our online store by setting the max_staleness
on a feature and using scheduled queries.

```
from chalk.features import feature
@features
class User:
    id: int
    name: str
    email: str
    account: "Account"

    # The similarity between the user's name and the account's title.
    account_name_match: float

    # The average time between each of a user's transactions, from the last
    # 30 days, in ms.
-   average_time_between_transactions_30d: float
+   average_time_between_transactions_30d: float = feature(max_staleness="infinity")
```

The max_staleness keyword argument tells Chalk how stale a feature value can get before it should be refreshed.
In this case, we're telling Chalk that we'll tolerate arbitrarily old feature values.
However, we could also specify a max_staleness of 1h or 1d to tell Chalk not to serve feature values that are older than 1 hour or 1 day.

To take advantage of our max_staleness, we need to get computed feature into the online store.
Feature are only written to the online store if they (or their feature class) have been given a max_staleness value.

Features with a max_staleness are written to the online store in two ways:

- Passively, when a feature value is computed in response to an online query,
- Actively, in response to an ETL or scheduled query.

The first time average_time_between_transactions_30d is queried for any given user it will be computed by the get_average_time_between_transactions resolver.
All subsequent times that the feature is requested it will be read from the online store (until the feature is evicted from the cache).

### Adding Offline Resolvers

By setting up offline SQL resolvers, we are telling Chalk that there are times when we don't want to pull data from our Postgres data source and instead want to get our data from a bulk data store.
There are a couple reasons why we might want to do this:
1). We don't want to overwhelm our Postgres data source with requests that
don't require real time data,
2). We want to query for large chunks of data (which is the purpose of a database like snowflake).

In the case of reverse-ETLing data, we have decided that we are tolerating some degree of staleness in our average_time_between_transactions_30d feature in exchange for being able to serve the feature faster.
As a result, it makes sense to read the new data from snowflake.

To connect our feature classes to Snowflake, we'll write three more SQL resolvers, this time labeling them with type: offline and source: snowflake.

```
-- get users from snowflake.
-- resolves: User
-- source: snowflake
-- type: offline
select
    id,
    full_name as name,
    email
from users
```

```
-- get accounts from snowflake.
-- resolves: Account
-- source: snowflake
-- type: offline
select
    id,
    user_id,
    balance,
from accounts
```

```
-- get transactions from snowflake.
-- resolves: Transaction
-- source: snowflake
-- type: offline
select
    id,
    account_id,
    amount,
    status,
    created_at
from transactions
```

### Creating a Scheduled Query

With our offline SQL resolvers defined, we can now write a ScheduledQuery which will periodically run and write updated average_time_between_transactions_30d features to the online store.

```
from chalk import ScheduledQuery

ScheduledQuery(
    name="user-transaction-reverse-etl-features",
    schedule="0 * * * *",
    output=[User.average_time_between_transactions_30d],
    online=True,
    offline=True,
    incremental_resolvers="get_transactions_offline",
)
```

Our schedule "0 * * * *",  means that we will run this query and update the online store every hour.
This means our features will be one hour fresh (disregarding the snowflake data source lag).
Note, this allows really precise and granular trade-offs between staleness, latency, and compute.

In addition, by specifying an incremental resolver, we are telling Chalk to remember the high ingest time from the previous run and only pull data that is fresher than that high water mark.
Again Chalk is processing the minimum amount of information it requires to calculate the average_time_between_transactions_30d.

### API Calls

Any Python function can be used as a resolver.
This means that we can call APIs to compute features.
Let's add a feature that computes the user's FICO score from our credit scoring vendor, Experian.

As we did earlier, we'll first add the features that we want to compute:

```
+ from chalk.features import feature

@features
class User:
    id: int
    name: str
    email: str
    account_name_match: float

+   # The fraud score, as provided by a third-party vendor.
+   fico_score: int = feature(min=300, max=850, strict=True)
+
+   # Tags from our credit scoring vendor.
+   credit_score_tags: list[str]
```

We are adding strict validation to our fico_score feature to ensure that we only store and utilize valid FICO scores.

Now, we can write a resolver to fetch the user's FICO score from Experian.

```
from src.feature_sets import User
from src.mocks import experian
from chalk.features import online, Features

@online
def get_fraud_score(
    name: User.name,
    email: User.email,
) -> Features[User.fico_score, User.credit_score_tags]:
    response = experian.get_credit_score(name, email)

    # We don't need to provide all the features for
    # the `User` class, only the ones that we want to update.
    return User(
        fico_score=response['fico_score'],
        credit_score_tags=response['tags'],
    )
```

Here, we are returning two features of the user, User.fico_score and User.credit_score_tags.
We use the Features type to indicate which feature we expect to return.
Also note that we are initializing the User class with only the features that we want to update.
This partial initialization is the primary difference between Python's @dataclass and Chalk's @features.

### Setting up a Materialized Windowed Aggregation

When defining aggregations, it is often useful to compute a windowed aggregation to define the
same aggregation over different time windows. When defining a windowed aggregation over high-cardinality datasets like
transactions, it can be more performant to materialize these aggregations in the online store by defining a
materialized windowed aggregation. In a materialized windowed aggregation, you can
define time buckets, and Chalk will pre-aggregate the minimum data required over all the data in each time bucket
necessary to compute the aggregation for all time windows in the feature definition. For example, say we want to
compute the count of transactions associated with an Account over the past 7 days, 30 days, and 90 days. Then we can
define the materialized windowed aggregation below:

```
from chalk.features import feature
@features
class Account:
    id: int
    user_id: User.id
    balance: float
    user: User
    transactions: DataFrame[Transaction]
+
+   num_transactions: Windowed[int] = windowed(
        "7d",
        "30d",
        "60d",
        materialization={
            "bucket_durations": {"1d": ["7d"], "3d": ["30d", "60d"]},
        },
        expression=_.transactions[
            _.created_at > _.chalk_window,
            _.created_at < _.chalk_now
        ].count(),
    )
```

This defines a materialized windowed aggregation over the Account.transactions DataFrame, which counts the number of
transactions associated over the past 7, 30, and 60 days. The materialization argument tells Chalk to pre-aggregate the
data in buckets in the online store, such that the 7-day aggregation is pre-aggregated in 1-day buckets, and the
30-day and 60-day aggregations are pre-aggregated in 3-day buckets. Because this aggregation .count() only requires the
count of transactions that fall within each bucket, we would store the count of transactions for each bucket, and at
query time sum the counts for the buckets that fall within the requested time window. This configuration allows you
to define more performant aggregations over high-cardinality datasets, such as transactions, where recomputing the
aggregation could be computationally expensive by materializing the aggregations in buckets.

Because the materialized windowed aggregation relies on the materialized buckets in the online store, and branch
deployments do not persist data to the online store, we would need to run a full deploy with chalk apply to use
this new feature. After running a chalk apply, we can run chalk aggregate backfill --feature account.num_transactions
to populate the buckets, and then we can query the feature as normal.

In production, you could also set up a schedule to periodically backfill the buckets, or stream the data into the
online store, to keep the buckets up to date.

### Deploying

Finally, we'll want to deploy our new resolvers.
As we did earlier, we can check our work by using a branch deployment:

```
$ chalk apply --branch tutorial
✓ Found resolvers
✓ Deployed branch
```

We can then query our new features:

```
$ chalk query --branch tutorial  \
              --in     user.id=1 \
              --out    user.name_match_score
```

### CLI Query

Now that we've written some features and resolvers and deployed them to Chalk, we're ready to integrate Chalk into our production decisioning systems.

As a sanity check, it can be helpful to use the Chalk CLI to query a well-known input and ensure that we get the expected output.

We can use the chalk query command, passing in the id of a user, and the names of the features we want to resolve:

```
$ chalk query --in  user.id=1  \
              --out user.name  \
              --out user.email \
              --out user.account.balance
Results
user.name             "John Doe"
email                 "john@doe.com"
user.account.balance  2032.91
```

### API Client Query

Once we're satisfied that our features and resolvers are working as expected, we can use a client library to query Chalk from our application.

In this first example, we'll use the
ChalkClient in the
chalkpy package
to query Chalk from our application:

```
from src.feature_sets import User
from chalk.client import ChalkClient

# Create a new Chalk client. By default, this will
# pick up the login credentials generated after running
# `chalk login`.
client = ChalkClient()

client.query(
    input=User(id=1234),
    output=[
        User.id,
        User.name,
        User.fico_score,
        User.account.balance,
    ],
)
```

We use the same feature definitions for querying our data as we used for defining our features and resolvers.

Chalk has API client libraries in several languages, including
Python,
Go,
Java,
Typescript, and
Elixir.

### Code Generation (Optional)

All API clients can operate on the string names of features.
However, in a production system, you may have many hundreds or thousands of features, and want to avoid hard-coding the names of each feature in your code.

To help with this, Chalk can codegen a library of strongly-typed feature names for you.

For example, say the service that calls into Chalk is written in Go.
We can generate a Go library of feature names with the following command:

```
$ chalk codegen go --out ./clients/go/client.go --package=client
✓ Found resolvers
✓    Wrote features to file './clients/go/client.go'
✓    Please do not change the generated code.
```

This generates a file
clients/go/client.go
that looks like this:

```
package client

/**************************************
 Code generated by Chalk. DO NOT EDIT.
 > chalk codegen go --out ./clients/go/client.go --package client
**************************************/

import (
	"github.com/chalk-ai/chalk-go"
	"time"
)

var InitFeaturesErr error

type Account struct {
	Id *int64
	Title *string
	UserId *int64
	Balance *float64
	User *User
	UpdatedAt *time.Time
}

type User struct {
	Id *int64
	Name *string
	Email *string
	Account *Account
	AccountNameMatch *float64
	FicoScore *int64
	CreditScoreTags *[]any
}

var Features struct {
	Account *Account
	User *User
}

func init() {
	InitFeaturesErr = chalk.InitFeatures(&Features)
}
```

We can then use this library to query Chalk:

```
import (
    "github.com/chalk-ai/chalk-go"
)

// Create a new Chalk client.
client := chalk.NewClient()

// Create an empty struct to hold the results.
user := User{}

// Query Chalk, and add the results to the struct.
_, err = client.OnlineQuery(
  chalk.OnlineQueryParams{}.
  WithInput(Features.User.Id, 1234).
  WithOutputs(
    Features.User.Id,
    Features.User.LastName,
    Features.User.FicoScore,
    Features.User.Account.Balance,
  ),
  &user,
)

// Now, you can access the properties of the
// user for which there was a matching `output`.
fmt.Println(user.Account.Balance)
```

If your calling service is written in Python, but you don't want to take a dependency on the repository that contains your Chalk features, you can generate your Python features into a separate repository:

```
$ chalk codegen python --out ./clients/python/client.py
```

You can see the generated code in clients/python/client.py.

If you are generating Python into a subdirectory of your Chalk project, be sure to add an entry to your .chalkignore containing the directory of your generated code (in the above example, clients/).
Otherwise, Chalk will find duplicate definitions of your features.

# Tutorial: Feature Versions
source: https://docs.chalk.ai/docs/feature-version-tutorial

## Learn how to create and interact with versioned features

### Introduction

With Feature Versioning on the Chalk
platform, you can manage multiple versions of a feature.
In this guide, you'll add versioning to a feature in an existing
Chalk project.

The following example shows you how to add versions to a feature,
manage resolvers for different versions, query versioned features,
and generally interact with versioned features.

### Creating your first versioned feature

- Create a versioned_feature.py file in your Chalk project.
- Copy the following Python contents into the versioned_feature.py file.

```
from chalk.features import feature, features, online

@features
class Animal:
    id: str
    sound: str = feature(version=2)

@online
def resolver_1(id: Animal.id) -> Animal.sound@1:
    return "Hello"

@online
def resolver_2(id: Animal.id) -> Animal.sound@2:
    match id:
        case "Cow": return "Moo"
        case "Dog": return "Woof"
        case _: return "Hello"
```

- Deploy your new feature with chalk apply --branch test.
- Now try a basic query for animal.sound. When no explicit version is provided, and no default_version is set, version 1 will be requested, so this function will return "Hello".

```
$ chalk query --in animal.id=Cow --out animal.sound --branch test
```

- To query a specific version, use the @ syntax

```
$ chalk query --in animal.id=Cow --out animal.sound@2 --branch test
```

### Changing default versions

When you create a versioned feature, the default version is 1.
You can control this default version and change the behavior of querying and resolvers.

- Replace the contents of versioned_feature.py with the following Python code. Note that we didn't specify @2 in resolver_2. We can do that because 2 is the default version of Animal.sound.

```
from chalk.features import feature, features, online

@features
class Animal:
    id: str
    sound: str = feature(version=2, default_version=2)

@online
def resolver_1(id: Animal.id) -> Animal.sound@1:
    return "Hello"

@online
def resolver_2(id: Animal.id) -> Animal.sound:
    match id:
        case "Cow": return "Moo"
        case "Dog": return "Woof"
        case _: return "Hello"
```

- chalk apply --branch test to deploy.
- Now try querying without a version, and resolver_2 will get executed.

```
$ chalk query --in animal.id=Cow --out animal.sound --branch test
```

### Using versioned features in resolvers

Versioned features can also be used as the inputs for resolvers,
which lets you do some clever things!
Let's check it out.

- Replace the contents of versioned_features.py with this code.

```
from chalk.features import feature, features, online

@features
class Animal:
    id: str
    sound: str = feature(version=2)

@online
def resolver_1(id: Animal.id) -> Animal.sound@1:
    return "Hello"

@online
def resolver_2(id: Animal.id, sound: Animal.sound@1) -> Animal.sound@2:
    sounds = {"Cow" : "Moo", "Dog": "Woof"}
    return f"The {id} says {sounds.get(id, 'Hello')}, but its trying to say {sound}"
```

- Now query for an Cow.sound@2 and notice how Chalk automatically generates the dependent Cow.sound@1 feature!

```
$ chalk query --in animal.id=Cow --out animal.sound@2 --branch test
```

# Tutorial: Jupyter Notebook
source: https://docs.chalk.ai/docs/notebook-tutorial

## Work through an example using Chalk in a Jupyter notebook

Chalk enables data science and machine learning teams to build and
deploy feature pipelines for machine learning.
For data science workflows, Chalk can be used in entirely in a notebook
to iteratively build features and generate training data.

In this tutorial, we will use Chalk in a Jupyter notebook to explore
a dataset of credit card authorizations and build out some features and resolvers.

### Table of Contents

- Configure Data Sources
- Defining Features
- Defining Resolvers
- Computed Features
- Troubleshooting
- Summary

### Configure data sources

The dataset we will be using for this tutorial is stored in tables in
our Snowflake warehouse.

Chalk has built-in support for a number of SQL-like sources
and can ingest data using SQL strings.

### Adding a Snowflake source

Chalk provides a native integration with Snowflake as
a SQL Source.

Before we can start ingesting data, we will initialize
a SnowflakeSource.
If you're working on an existing project, it's likely that this
step has already been done for you.

```
from chalk.sql import SnowflakeSource

snowflake = SnowflakeSource()
```

If you have multiple sources, you can initialize a
SnowflakeSource by passing in the name of your Snowflake integration which can be
defined in the Chalk Dashboard.

```
from chalk.sql import SnowflakeSource

snowflake = SnowflakeSource(name="snowflake-integration")
```

### Defining Features

Once we have our data source setup, we can start defining features. We will start by defining the
features we will ingest from our data source. In further sections, we will define derived features
that we will use to train a fraud classification model.

Our dataset consists of the following tables:

- cards
- merchants
- authorizations
- cardholders

Chalk lets you define your features in Python by decorating classes
with the @feature decorator.

Chalk lets you define features directly in Python. To create a new FeatureSet,
apply the @features decorator to a Python class with typed attributes.

In our notebook, we will now define the following feature classes:

```
from datetime import datetime

from chalk.features import features, has_many, DataFrame, FeatureTime

@features
class Merchant:
    id: int
    name: str
    category: str
    country_code: str

@features
class Authorization:
    id: int
    amount_in_cents: int
    card_id: int
    merchant_id: int
    country_code: str
    status: str
    authorized_at: FeatureTime

    # Relationships
    card: "Card"

@features
class Card:
    id: int
    cardholder_id: int
    issued_at: datetime

    # Relationships
    authorizations: DataFrame[Authorization] = has_many(
        lambda: Authorization.card_id == Card.id
    )

@features
class CardHolder:
    id: int
    name: str
    address: str
    created_at: datetime

    # Relationships
    cards: DataFrame[Card] = has_many(lambda: CardHolder.id == Card.cardholder_id)
```

Here we have defined four feature classes: Merchant, Authorization, Card,
and CardHolder.
In the features sets, we have defined the root features which are the
features that are directly fetched from the datasource as well as derived features.
In the next section, we will look at how to resolve these features.

### Primary Keys

Feature classes in Chalk need to have a unique id field. By default,
Chalk will use the id field as the primary key for the feature class.
However, if you want to use a different field as the primary key, you can
specify it using the Primary argument as shown below.

```
from chalk.features import Primary

@features
class Merchant:
-   id: int
+   merchant_id: Primary[int]
    name: str
    category: str
    country_code: str
```

### Namespacing

Features are namespaced by their containing FeatureSet and by the
name of the variable.

For example, as defined above Authorization would be the containing
FeatureSet and its corresponding features would be named as follows:

| Feature Name                  | Type                                                                                                          |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------- |
| authorization.id              |  Integer      |
| authorization.amount_in_cents |  Integer      |
| authorization.card_id         |  Integer      |
| authorization.merchant_id     |  Integer      |
| authorization.country_code    |  String       |
| authorization.status          |  String       |
| authorization.authorized_at   |  FeatureTime  |

### Relationships

We can also define relationships between features using the has_one
or has_many functions, where the first argument specifies a function
returning how to join the tables.

In the feature definitions above, we have defined a one-to-many relationship between Card
and Authorization using the has_many function.

```
@features
class Authorization:
    id: int
    amount_in_cents: int
    card_id: int
    merchant_id: int
    country_code: str
    status: str
    authorized_at: FeatureTime

    # Relationships
+   # We defined the join condition between `Card` and `Authorization` below,
+   # we don't need to repeat it here
+   card: "Card"

@features
class Card:
    id: int
    cardholder_id: int
    issued_at: datetime

    # Relationships
+   # The has-many relationship between `Card` and `Authorization`
+   # specifying the join condition
+   authorizations: DataFrame[Authorization] = has_many(
+       lambda: Authorization.card_id == Card.id
+   )
```

### Feature Types

Chalk supports a number of different feature types including scalars,
collections, dataclasses, Pydantic models and custom types.
For a complete list of features, refer to Feature Types.

### Using feature time

By default, our features are timestamped with the execution time of their resolvers.
Since we want to be able to run point-in-time correct backfills, we will need
to use the FeatureTime type to override the default behavior and explicitly
use the authorized_at field.

To learn more about how to use FeatureTime, refer to our time documentation.

```
from chalk.features import FeatureTime

@features
class Authorization:
    # Root features
    id: int
    amount_in_cents: int
    card_id: int
-   authorized_at: datetime
+   authorized_at: FeatureTime

    # Relationships
    card: "Card"

```

### Defining Resolvers

Next we will define the resolvers for the features we have defined above.
A resolver is a function that defines how features
are fetched or derived.

To ingest data from Snowflake for the features we defined above, we will define
resolvers using SQL strings.
Specifically we will use the query_string
function on our Snowflake source defined above.

It is important to make sure the names of the features we are resolving match the
names of the features we defined above.
For example, in the resolver definition below,
we alias created_at to authorized_at for Authorization

### SQL Resolvers

We will use the %%resolver magic to define SQL resolvers in our notebook.

```
%%resolver get_merchant_features
-- resolves: Merchant
-- source: snowflake
SELECT id,
       name,
       category,
       country_code
FROM merchant
```

```
%%resolver get_cardholder_features
-- resolves: CardHolder
-- source: snowflake
SELECT id,
       name,
       address,
       created_at
FROM cardholder
```

```
%%resolver get_authorization_features
-- resolves: Authorization
-- source: snowflake
SELECT id,
       amount_in_cents,
       card_id,
       merchant_id,
       status,
       country_code,
       created_at as authorized_at
FROM authorization
```

```
%%resolver get_card_features
-- resolves: Card
-- source: snowflake
SELECT id,
       cardholder_id,
       issued_at
FROM card
```

### Python resolvers

Alternatively, you can define resolvers using Python functions using the @offline decorator

A note on namespaces

Resolvers can take in multiple features as input, however, all feature dependencies in a
single resolver must be from the same namespace.

Requiring features from the same root namespace

```
@offline
def fn(
    authorization_amount: Authorization.amount_in_cents,
    card_id: Authorization.card_id,
) -> Authorization.some_feature:
    return ...
```

Here, we incorrectly request features from the root namespaces
of Authorization and Card:

Requiring features from different root namespaces

```
@online
def fn(
    authorization_amount: Authorization.amount_in_cents,
    card_id: Card.id
) -> Authorization.some_feature:
    return ...
```

### Computed Features

The ChalkClient provides the offline_query
method to compute features from the offline store.

To validate that we are able to resolve features from our offline store, we can run an
offline query to resolve the features defined on Merchant.

If inputs are given, the query will return rows corresponding to those inputs, otherwise it
will return a random sample according to the max_samples parameter.

Offline queries return a Dataset instance which can be converted to a
Pandas DataFrame using the get_data_as_pandas method.

```
dataset = client.offline_query(
    input={
        Merchant.id: [1, 2, 3]
    },
    output=[
        Merchant.id,
        Merchant.name,
        Merchant.category
    ],
    recompute_features=True,
).get_data_as_dataframe()
```

We get back the following DataFrame, validating that our resolvers are working as expected

```
┌───────────────────────┬───────────────────────────┬─────────────────┐
│ merchant.category     ┆ merchant.name             ┆ merchant.id     │
│ ---                   ┆ ---                       ┆ ---             │
│ str                   ┆ str                       ┆ i64             │
╞═══════════════════════╪═══════════════════════════╪═════════════════╡
│ Gas Station           ┆ Tucker, Hull and Gallegos ┆ 1               │
│ E-commerce            ┆ Silva-Odonnell            ┆ 2               │
│ Grocery               ┆ Taylor-Davis              ┆ 3               │
└───────────────────────┴───────────────────────────┴─────────────────┘
```

Note that we specified the recompute_features
parameter to True to ensure that the features are recomputed by the resolvers.
When set to False, output features are sampled from the offline store.

### Feature Definitions

Let's expand on the feature classes we have defined and add the following computed features:

```
@features
class Authorization:
    id: int
    amount_in_cents: int
    card_id: int
    merchant_id: int
    country_code: str
    status: str
    authorized_at: FeatureTime

+   # The authorization amount (in cents) of the previous transaction
+   previous_auth_amount_in_cents: int

    # Relationships
    card: "Card"

@features
class Card:
    id: int
    cardholder_id: int
    issued_at: datetime

+   # The total number of transactions
+   count_transactions_total: int
+
+   # The total number of transactions in the last 7 days
+   count_transactions_7d: int
+
+   # The number of days since the card was created
+   days_since_card_created: int
+
+   # Days since first transaction
+   days_since_first_transaction: int
+
+   # Days since last transaction
+   days_since_last_transaction: int

    # Relationships
    authorizations: DataFrame[Authorization] = has_many(
        lambda: Authorization.card_id == Card.id
    )
```

Next, we will define resolvers for these features.

```
%%resolver get_prev_auth_amounts
-- resolves: Authorization
-- source: snowflake
WITH ordered AS (
	SELECT
		id,
		card_id,
		amount_in_cents,
		LAG(amount_in_cents,
			1) OVER (PARTITION BY card_id ORDER BY created_at) AS previous_auth_amount_in_cents
	FROM
		AUTHORIZATION
)
SELECT
	id,
	previous_auth_amount_in_cents
FROM
	ordered
WHERE
	previous_auth_amount_in_cents IS NOT NULL
```

```
from chalk.features import after

@offline
def get_count_all_txns(
    txns: Card.authorizations[Authorization.id],
) -> Card.count_transactions_total:
    return txns.count()


@offline
def get_count_7d_txns(
    txns: Card.authorizations[Authorization.id, after(days_ago=7)]
) -> Card.count_transactions_7d:
    return txns.count()
```

### Projections & Filters

Chalk has support for time windows
using the before and after functions.
In the resolvers above, we use the after operator to
filter the transactions by the created_at field.

Additionally, since we don't need to resolve all the features on Authorization
to compute the counts, we can specify the features we need for this resolver using a projection.
Projections allow us to scope down a DataFrame
to only include the features we need.
In this instance, we are using projections to only fetch the id field from Authorization.

In the resolvers above, we have combined filtering with a projection on the authorizations DataFrame.
Refer to the section on
composing projections and filters
for more details.

```
from datetime import datetime
from chalk import Now

@offline
def get_days_since_card_created(
    card_id: Card.id,
    issued_at: Card.issued_at,
    now: Now,
) -> Card.days_since_card_created:
    return (now - issued_at).days

@offline
def get_days_since_first_last_txn(
    txns: Card.authorizations[Authorization.created_at],
    now: Now,
) -> Features[
    Card.days_since_first_transaction,
    Card.days_since_last_transaction,
]:
    # Sort transactions by created_at
    sorted_txns = txns.sort(by=Authorization.created_at, descending=False)

    # Get first and last transaction dates
    first_txn_date = sorted_txns.first(col=Authorization.created_at)
    last_txn_date = sorted_txns.last(col=Authorization.created_at)

    return Card(
        days_since_first_transaction=(now - first_txn_date).days,
        days_since_last_transaction=(now - last_txn_date).days,
    )
```

### Time-dependent resolvers

In the resolvers above, we made use of the Chalk feature Now which
allows us to express time-dependency in our resolvers.
This is useful for performing backfills which compute values that depend
on values that are semantically similar to datetime.now().

In online queries, Now represents datetime.now(). In offline queries,
we can use the input_times parameter
to specify the times Now should resolve to allowing us to run backfills for many different
historical points in time.

```
# Example of running an offline query for multiple historical points in time
client.offline_query(
    input={Card.id: [1, 1, 1]},
    output=[Card.get_days_since_card_created],
    input_times=[
        datetime.now(),
        datetime.now() - timedelta(days=10),
        datetime.now() - timedelta(days=50),
    ],
)


# Output:
# ┌─────────┬──────────────────────────────┐
# │ card.id ┆ card.days_since_card_created │
# │ ---     ┆ ---                          │
# ╞═════════╪══════════════════════════════╡
# │ 1       ┆ 90                           │
# │ 1       ┆ 80                           │
# │ 1       ┆ 40                           │
# └─────────┴──────────────────────────────┘
```

### Troubleshooting

Some queries that involve multiple operations might need additional tracking.
Users can supply store_plan_stages=True to store
intermediate outputs at all operations of the query.
This will dramatically slow things down, so use wisely!
These results are visible in the dashboard under the "Queries" page as shown below.

### Query Plan

The Query Plan shows the operations that were executed to compute the query as well as the
intermediate results at each stage.
The numbers on the edges represent the number of rows of data that
were passed from one stage to the next.

Chalk Query Plan

### Intermediate Results

You can examine the intermediate results at each stage of the query plan by clicking on
a specific stage and download the results as a parquet file.

Chalk Query Intermediate Results

### Summary

In this tutorial, we learned how to use Chalk in a notebook to define features, resolvers and
run offline queries.

To dive deeper into Chalk, check out our documentation on the topics listed below

- DataFrame
- Offline Queries
- SQL Integrations
- Backfills
- Temporal Consistency
# Tutorial: AWS SageMaker with Chalk
source: https://docs.chalk.ai/docs/sagemaker-tutorial

## Build a Chalk feature pipeline for training and serving models with AWS SageMaker.

### Introduction

Chalk enables you to build feature pipelines for machine learning models. AWS
SageMaker is a popular service for building, training, and deploying models. Chalk
and SageMaker fit together naturally to create a streamlined machine learning architecture that uses the best aspects of
each system.

### Why use Chalk?

There are several advantages to using Chalk in your ML architecture alongside SageMaker.

- Use the same Python codebase for notebook iteration, training, and serving. Chalk enables you to maintain a
single Python codebase that integrates with many data sources, including Postgres, Databricks, Snowflake, Kafka, and
others. As you tweak your feature definitions, you can deploy your updates to separate
branches to try your new features without needing to wait for a long build step.
- Generate features when they're needed. Chalk computes features in response to queries. Other systems such as
SageMaker Feature Store require you to precompute features from batch data. We believe the precomputation style is
limiting because this style prevents users from relying on real-time data. For example, precomputation prevents users
from writing features reliant on recency (such as the number of failed logins in the past minute) or third-party APIs
(which may be costly to exhaustively pre-fetch).

### What you'll learn

In this tutorial, we'll take a deep dive into how you can use Chalk to serve features combined with SageMaker for model
training and serving. You will:

- Set up your feature pipeline with Chalk:Connect your data sources (in this tutorial, DynamoDB)Write feature definitions in PythonWrite resolvers defining how to generate those features from your data source
- Set up your SageMaker pipeline:Run Chalk offline queries and prepare datasets for training and evaluationTrain your modelEvaluate your model
- Deploy your model with SageMaker

We'll go through each of these steps using fraud detection as our example use case. The full code for this tutorial can
be found in GitHub.

### Set up Chalk

In this section, we'll set up your Chalk feature pipeline.

### Connect your data source

Chalk integrates with AWS, GCP, various SQL databases, Databricks, and more.
For this tutorial, we'll pull transaction data from AWS DynamoDB, but you can add as many data sources as you need.

To connect DynamoDB, enter your AWS access key into the Chalk dashboard. After adding AWS, define your DynamoDB data
source in Python and give it a name:

```
from chalk.sql import DynamoDBSource

DynamoDBSource(name="our_dynamo")
```

### Define features

Features are structured data you can use as inputs to your model. With Chalk, you define your features
in one place as Pydantic-style Python classes:

```
from datetime import date

from chalk import DataFrame, FeatureTime
from chalk.features import features, feature


@features
class Transaction:
    id: int
    amount: float
    confirmed_fraud: bool
    # Use strings to reference Customer because Customer is defined beneath this class
    customer_id: "Customer.id"
    customer: "Customer"
    transacted_at: FeatureTime


@features
class Customer:
    id: int
    name: str
    email: str
    dob: date
    income: int
    # :tags: pii
    ssn: str
    # Set max_staleness on fico because fico relies on a third-party API call.
    # We will read this value from a cache (as long as it was computed
    # sometime in the last day).
    fico: int = feature(max_staleness="1d")
    # The transactions, linked by the Customer.id type on the Transaction.customer_id field
    transactions: DataFrame[Transaction]
```

In this code, Transaction is the feature class and each of its properties is a feature.

### Define resolvers

Resolvers are Chalk's way of defining how to retrieve data and convert them into features.

Most of our features will be loaded from DynamoDB using SQL file resolvers. Here's how we retrieve basic
Transaction and Customer data:

```
-- type: online
-- resolves: transaction
-- source: our_dynamo
SELECT
  id,
  amount,
  confirmed_fraud,
  customer_id,
  created_at AS transacted_at
FROM
  txns;
```

```
-- type: online
-- resolves: customer
-- source: our_dynamo
SELECT
  id,
  name,
  email,
  dob,
  income,
  ssn
FROM
  customers;
```

Each column in the result must match the name of a feature. Use AS to rename columns as needed.

For features requiring computation, we use Python resolvers. Here's a resolver
for retrieving a customer's FICO score from an API:

```
from chalk import online

@online
def get_fico(name: Customer.name, ssn: Customer.ssn) -> Customer.fico:
    # Replace with your preferred provider.
    fico_score = FICOApi().get_score(name, ssn)
    return Customer(fico=fico_score)
```

This resolver depends on Customer.name and Customer.ssn and returns Customer.fico. When you deploy, Chalk uses
your resolver inputs and outputs to create a dependency graph to confirm your features can be generated safely.

The get_fico resolver will be invoked in response to Chalk queries. Resolvers do not run
exhaustively over your customer dataset, which helps you reduce costs related to unnecessary computation and API usage.
Our resolver documentation goes into greater detail about how you can schedule
resolvers and set up batch offline jobs. We also set max_staleness to 1 day on the fico
feature, so this feature will be read from the online store's cache if the value has already been computed in the past
day.

With a combination of Python and SQL resolvers, we have now told Chalk how to retrieve each of our features.

### Deploy Chalk

At this point, you can deploy Chalk to a local branch and start writing queries.

To deploy to a non-production branch, pass --branch to chalk apply:

```
$ chalk apply --branch sagemaker_tutorial
✓ Found resolvers
✓ Deployed branch
```

You can run ad hoc queries on this branch from the CLI:

```
$ chalk query --branch sagemaker_tutorial  \
              --in     transaction.id=1 \
              --out    transaction.confirmed_fraud
```

Once you're satisfied with your feature pipeline, you can move on to setting up SageMaker.

### Set up SageMaker

There are many ways to set up SageMaker. In this tutorial, we'll use SageMaker
steps to compose our model training
pipeline. Steps allow us to modularize the code and we find them easier to work with than some alternatives, such as
running the pipeline directly from one super long Jupyter notebook.

In this section, we'll write steps for creating the dataset, training a candidate model, and evaluating the model.

### Create the dataset

In this step, we'll use Chalk to generate a random sample of features from our dataset, split the dataset for training
and testing using
scikit-learn, write
the results to S3, and return the S3 paths to be used in the next step.

Writing the split datasets to S3 provides a clear history of the data you used to train and evaluate your
model. Additionally, it allows you re-run later steps in your pipeline without re-executing the dataset generation
step.

In the previous section, we set up our features and resolvers without going into great detail about how the code would
be executed. Here, we'll finally show how the code gets executed through a Chalk offline query:

```
from sagemaker.workflow.function_step import step
from src.feature_sets import Transaction

@step(name="create_dataset")
def create_dataset(
    test_size: float, run_bucket: str, model_name: str
) -> tuple[str, str, str, str]:
    from chalk.client import ChalkClient
    from sklearn.model_selection import train_test_split

+    client = ChalkClient(branch="sagemaker_tutorial")
+
+    chalk_dataset = ChalkClient().offline_query(
+        recompute_features=True,
+        output=[
+            Transaction.amount,
+            Transaction.customer.fico,
+            # ... and more features
+        ],
+        # By giving this dataset a name, we will be able to view it in the Chalk
+        # dashboard, download it locally, or share it with collaborators.
+        name=model_name,
+    )
+
+    # Converting a chalk_dataset to a pandas (or polars) dataframe is
+    # efficient because both are backed by Apache Arrow.
+    dataset = chalk_dataset.to_pandas()

    # Create training data by removing the target column.
    X = dataset.drop(columns=[Transaction.confirmed_fraud])

    # Pull target from dataset.
    y = dataset[Transaction.confirmed_fraud]

    # Split data into train and test set. We will use k-fold cross-validation
    # for hyperparameter tuning
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,test_size=test_size
    )

    xtrain_path = f"{run_bucket}/input/X_train.parquet"
    xtest_path = f"{run_bucket}/input/X_test.parquet"
    ytrain_path = f"{run_bucket}/input/y_train.parquet"
    ytest_path = f"{run_bucket}/input/y_test.parquet"

    dataset.to_parquet(f"{run_bucket}/raw_data/data.parquet")
    X_train.to_parquet(xtrain_path)
    y_train.to_parquet(ytrain_path)
    X_test.to_parquet(xtest_path)
    y_test.to_parquet(ytest_path)
    return xtrain_path, xtest_path, ytrain_path, ytest_path
```

The full code for this step can be found in
steps/dataset.py.

### Train and evaluate

Our last two steps will retrieve our features from S3 and train and evaluate our model. These steps don't depend on
Chalk or any other data sources, so you can rapidly iterate here without being blocked on feature engineering if your
training data does not require changes.

In steps/training.py, we load the training data from S3 and train a model using
scikit-learn:

```
from sagemaker.workflow.function_step import step

PARAM_GRID = {
    'xgb__n_estimators': [20, 50, 100, 200],
    'xgb__learning_rate': [0.01, 0.1, 0.2],
    'xgb__max_depth': [3, 5, 7, 9],
}

@step(
    name="model-training",
    instance_type="ml.m5.xlarge",
    keep_alive_period_in_seconds=300,
)
def train(
    xtrain_path: str,
    ytrain_path: str,
    num_rounds: int
):
    from sklearn.pipeline import Pipeline
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    from sklearn.impute import SimpleImputer
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.model_selection import RandomizedSearchCV

    # Read data files from S3.
    X_train = pd.read_parquet(xtrain_path)
    y_train = pd.read_parquet(ytrain_path)

    pipeline = Pipeline(
        steps=[
            ("impute", (SimpleImputer())),
            ("scaler", StandardScaler()),
            ("xgb", GradientBoostingClassifier()),
        ]
    )
    # Note: Fraud detection commonly experiences the imbalanced learning problem.
    # In other words, fraud may be over or underrepresented in the dataset, leading
    # to unreliable results in production. When training a model for production,
    # the imbalance should be addressed, for example, by upsampling, downsampling,
    # or model choice.
    rsc = RandomizedSearchCV(
        pipeline,
        param_distributions=PARAM_GRID,
        n_iter=num_rounds,
        cv=3,
        scoring="f1",
        n_jobs=-1,
    )
    rsc.fit(X_train, y_train)

    return rsc.best_estimator_
```

In
steps/evaluate.py,
we load our newly trained model and evaluate it against our test dataset:

```
from sagemaker.workflow.function_step import step

@step(
    name="model-evaluation",
    instance_type='ml.t3.medium',
    keep_alive_period_in_seconds=300,
)
def evaluate(model, xtest_path: str, ytest_path: str, run_bucket: str) -> str:
    import pandas as pd
    from sklearn.metrics import (
        accuracy_score,
        f1_score,
        precision_score,
        recall_score,
    )
    import s3fs
    import json

    X_test = pd.read_parquet(xtest_path)
    y_test = pd.read_parquet(ytest_path)

    predictions = model.predict(X_test)

    results = {
        "accuracy": accuracy_score(y_test, predictions),
        "f1": f1_score(y_test, predictions),
        "precision": precision_score(y_test, predictions),
        "recall": recall_score(y_test, predictions),
    }

    # Upload evaluation report to s3
    s3_fs = s3fs.S3FileSystem()
    eval_src_s3 = f"{run_bucket}/evaluation/evaluation.json"

    with s3_fs.open(eval_src_s3, "wb") as file:
        file.write(json.dumps(results))

    return eval_src_s3
```

### Assemble the steps into a SageMaker pipeline

Finally, let's assemble our three steps into a SageMaker pipeline in
chalk_sagemaker_pipeline.py:

```
from sagemaker.workflow.pipeline import Pipeline
from steps.dataset import create_dataset
from steps.training import train
from steps.evaluate import evaluate
from sagemaker.workflow.parameters import (
    ParameterInteger,
    ParameterString,
    ParameterFloat,
)
from uuid import uuid4

BUCKET_PREFIX = "s3://chalk-sagemaker-models/"

if __name__ == "__main__":
    # Create Run Parameters
    model_package_group = "chalk-sagemaker-xgb"
    run_bucket = f"s3://chalk-sagemaker-models/{model_package_group}/{uuid4()}/"

    # Required F1 Threshold for model registration
    f1_threshold = ParameterFloat(name="F1Threshold", default_value=0.8)

    # Size of test split
    test_size = ParameterFloat(name="TestSize", default_value=0.2)

    # Number of estimators to evaluate
    num_rounds = ParameterInteger(name="NumRounds", default_value=50)
    run_bucket = ParameterString(name="RunBucket", default_value=run_bucket)
    model_package_group = ParameterString(name="ModelPackageGroup", default_value="chalk-sagemaker-xgb")

+    delayed_data = create_dataset(test_size=test_size, run_bucket=run_bucket)
+    delayed_model = train(xtrain_path=delayed_data[0], ytrain_path=delayed_data[2], num_rounds=num_rounds)
+    delayed_evaluation = evaluate(model=delayed_model, xtest_path=delayed_data[1], ytest_path=delayed_data[3], run_bucket=run_bucket)
+
+    pipeline = Pipeline(
+        name="ChalkaiSagemakerPipeline",
+        steps=[delayed_evaluation],
+        parameters=[
+            f1_threshold,
+            test_size,
+            run_bucket,
+            model_package_group,
+            num_rounds,
+        ]
+    )
```

### Deploy your model with SageMaker

There are a number of different ways to deploy the model that you trained on SageMaker. We recommend deploying your
model to an endpoint, which is documented
here.

### Efficient SageMaker inference with Chalk underscores

Once you've defined your SageMaker endpoint, you can run predictions against SageMaker from Chalk. This
can be accomplished by encoding your input features and then using the F.sagemaker_predict underscore.
function. You can specify your target SageMaker endpoint in the underscore function's parameters.

```
import chalk.functions as F

@features
class Transaction:
    id: int
    amount: float
    confirmed_fraud: bool
    # Use strings to reference Customer because Customer is defined beneath this class
    customer_id: "Customer.id"
    customer: "Customer"
    transacted_at: FeatureTime

    encoded_features: str
    transaction_fraud_prediction_raw: bytes = F.sagemaker_predict(
      F.string_to_bytes(_.encoded_features),
      endpoint="chalk-sagemaker-xgb-endpoint",
    )

@online
def get_encoded_features(amount: Transaction.amount, customer_fico: Transaction.customer.fico, ...) -> Transaction.encoded_features:
    return f"{amount},{customer_fico},..."
```

### Conclusion

In this tutorial, you got a look at how Chalk accelerates your feature engineering workflows by making it easy to
connect your data sources and unifying your feature code into a single Python codebase. Chalk fits naturally into a
SageMaker step for dataset generation and hands feature data off to the rest of your SageMaker pipeline for model
training, evaluation, and serving.

# End-to-End Model Tutorial
source: https://docs.chalk.ai/docs/model-tutorial

## Build a complete ML pipeline from features to inference

This tutorial walks through a complete machine learning workflow in Chalk: defining features, connecting to Snowflake data sources, creating point-in-time correct training datasets, training a model, registering it, and deploying it for inference.

We'll build an event engagement prediction model that predicts whether a user is likely to engage with a notification.

### Step 1: Define Your Features

First, define feature classes that represent the entities in your domain. Feature classes use the @features decorator and define typed attributes for each feature.

```
from datetime import datetime

from chalk import windowed, Windowed
from chalk.features import features, DataFrame, _
import chalk.functions as F


@features
class User:
    id: int

    # Account features
    email: str
    signup_date: datetime
    account_type: str  # one of: "free", "basic", "premium"

    # Windowed activity features - automatically creates versions for each window
    total_logins: Windowed[int] = windowed(
        "1d",
        "7d",
        "30d",
        expression=_.events[
            _.type == "login",
            _.ts > _.chalk_window,
            _.ts <= _.chalk_now
        ].count(),
        default=0
    )
    first_login_unix_seconds: Windowed[int | None] = windowed(
        "1d",
        "7d",
        "30d",
        "all",
        expression=_.events[
            _.ts_unix_seconds,
            _.type == "login",
            _.ts > _.chalk_window,
            _.ts <= _.chalk_now
        ].min(),
        default=None
    )

    # Non-windowed activity feature
    days_since_last_login: int | None = (
        (F.unix_seconds(_.chalk_now) - _.first_login_unix_seconds["all"]) / 86400
    )

    # Windowed billing features
    monthly_spend: float

    # Computed features
    account_age_days: int
    engagement_score: float

    # Has-many relationship to events
    events: "DataFrame[Event]"

    # Timestamp for feature time
    ts: datetime


@features
class Event:
    id: int
    user_id: User.id
    user: User
    type: str
    ts: datetime
    ts_unix_seconds: int = F.unix_seconds(_.ts)
    event_clicked: "EventClicked | None"
    event_was_clicked: bool = F.is_not_null(_.event_clicked.ts)

    # Model prediction
    interaction_probability: float


@features
class EventClicked:
    id: Event.id
    ts: datetime
```

The windowed() function creates multiple versions of a feature, one for each time window. You can reference specific windows using bracket notation:

- User.total_logins["1d"] - logins in the last day
- User.total_logins["7d"] - logins in the last 7 days
- User.total_logins["30d"] - logins in the last 30 days

### Step 2: Configure Snowflake Data Sources

Connect Chalk to your Snowflake data warehouse. First, configure the integration in the Chalk dashboard, then reference it in your code.

### Dashboard Configuration

In the Chalk dashboard, navigate to Settings > Data Sources and add a Snowflake integration with your credentials (account, warehouse, database, schema, role).

### Define Sources in Code

```
from chalk.sql import SnowflakeSource

# Reference the integration configured in the dashboard
snowflake = SnowflakeSource(name="sf")
```

### Create SQL File Resolvers

Create SQL files that map your Snowflake tables to Chalk features.

```
-- type: offline
-- resolves: User
-- source: sf

SELECT
    id,
    email,
    signup_date,
    account_type,
    monthly_spend
FROM users
```

```
-- type: offline
-- resolves: Event
-- source: sf

SELECT
    id,
    user_id,
    ts,
    type
FROM events
```

```
-- type: offline
-- resolves: EventClicked
-- source: sf

SELECT
    id,
    ts
FROM events_clicked
```

### Create Python Resolvers

Create python resolvers to computed some simple derived features:

```
from datetime import datetime

from chalk import online, Now
from src.features import User


@online
def compute_account_age(
    signup_date: User.signup_date,
    now: Now
) -> User.account_age_days:
    return (now - signup_date).days


@online
def compute_engagement_score(
    logins: User.total_logins["30d"],      # Reference 30-day window
    days_inactive: User.days_since_last_login,
) -> User.engagement_score:
    # Simple engagement formula using 30-day windowed features
    activity_score = min(logins / 30, 1.0) * 0.6
    recency_score = max(0, 1 - (days_inactive / 30)) * 0.4

    score = (activity_score + recency_score) * 100
    return score
```

### Step 3: Create a Point-in-Time Correct Training Dataset

Use offline_query to create a training dataset with point-in-time correctness. This ensures that feature values reflect what was known at each historical point, preventing data leakage.

```
from datetime import datetime, timedelta
from chalk.client import ChalkClient
from src.features import Event

client = ChalkClient()

# Create the dataset with point-in-time correctness
# Use bracket notation to select specific windows for windowed features
dataset = client.offline_query(
    input_sql="""
    SELECT 
        id as "event.id", 
        ts  as "__ts__"
    FROM "sf.prod.events"
    WHERE type='recommendation';
    """,
    output=[
        Event.id,
        Event.user.id,
        Event.user.account_type,
        Event.user.total_logins["1d"],      # 1-day window
        Event.user.total_logins["7d"],      # 7-day window
        Event.user.total_logins["30d"],     # 30-day window
        Event.user.days_since_last_login,
        Event.user.monthly_spend,
        Event.user.account_age_days,
        Event.user.engagement_score,
        Event.event_was_clicked
    ],
    dataset_name="event_recommendation_dataset",
    run_asynchronously=True,  # For large datasets
)

# Retrieve the data as a pandas DataFrame
df = dataset.get_data_as_pandas()
print(f"Dataset shape: {df.shape}")
print(df.head())
```

### Step 4: Train Your Model

With your point-in-time correct dataset, train a model. Here's an example using scikit-learn:

```
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, precision_score, recall_score

# Prepare features and labels
# Windowed feature columns include the window in the column name
feature_columns = [
    'event.user.total_logins__30d__',        # 30-day login count
    'event.user.days_since_last_login',
    'event.user.monthly_spend',
    'event.user.account_age_days',
    'event.user.engagement_score',
]

X = df[feature_columns]
y = df['event.event_was_clicked']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train the model
model = GradientBoostingClassifier(
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1,
    random_state=42
)
model.fit(X_train, y_train)

# Evaluate
y_pred_proba = model.predict_proba(X_test)[:, 1]
y_pred = model.predict(X_test)

metrics = {
    "auc_roc": roc_auc_score(y_test, y_pred_proba),
    "precision": precision_score(y_test, y_pred),
    "recall": recall_score(y_test, y_pred),
}
print(f"Model metrics: {metrics}")
```

### Step 5: Register the Model

Register your trained model in the Chalk Model Registry. This versions your model and makes it available for deployment.

```
from datetime import datetime
from chalk.client import ChalkClient

client = ChalkClient()

# Register the trained model version
client.register_model_version(
    name="InteractionModel",
    aliases=["production", "v1.0"],
    model=model,  # Pass the sklearn model directly
    metadata={
        "framework": "sklearn",
        "algorithm": "GradientBoostingClassifier",
        "training_date": datetime.now().isoformat(),
        "training_dataset": "event_recommendation_dataset",
        "feature_columns": feature_columns,
        "metrics": metrics,
    },
    input_features=[
        Event.user.total_logins["30d"],
        Event.user.days_since_last_login,
        Event.user.monthly_spend,
        Event.user.account_age_days,
        Event.user.engagement_score,
    ],
    output_features=[
        Event.interaction_probability
    ]


print("Model registered successfully!")
```

### Step 6: Deploy the Model for Inference

Create a model resolver that connects your registered model to your feature class for real-time inference.

```
from chalk.ml import ModelReference
from chalk import make_model_resolver
from src.features import Event

# Reference the registered model
interaction_model = ModelReference.from_alias(
    name="InteractionModel",
    alias="production",
)

# Or reference by specific version:
# interaction_model = ModelReference.from_version(
#     name="InteractionModel",
#     version=1,
# )

# Create a resolver that runs inference
# Use bracket notation to specify which window to use for each windowed feature
interaction_resolver = make_model_resolver(
    name="get_interaction_prediction",
    model=interaction_model,
    inputs=[
        Event.user.total_logins["30d"],
        Event.user.days_since_last_login,
        Event.user.monthly_spend,
        Event.user.account_age_days,
        Event.user.engagement_score,
    ],
    output=[Event.interaction_probability],
)
```

Deploy your Chalk project to make the model available:

```
chalk apply
```

### Step 7: Query Predictions

Now you can query interaction predictions in real-time through the Chalk API:

 To get good performance, you'll want to add an online source for your features (like a postgres
or a stream). 

```
from chalk.client import ChalkClient
from src.features import Event

client = ChalkClient()

# Get interaction probability for a single event
# You can query multiple windows of the same feature
result = client.query(
    input={Event.id: 12345},
    output=[
        Event.interaction_probability,
    ],
)

print(f"Interaction probability: {result.get_feature_value(Event.interaction_probability)}")
print(f"Logins (1d): {result.get_feature_value(Event.user.total_logins['1d'])}")
print(f"Logins (7d): {result.get_feature_value(Event.user.total_logins['7d'])}")
print(f"Logins (30d): {result.get_feature_value(Event.user.total_logins['30d'])}")
```

### Batch Predictions

For batch inference, use query_bulk:

```
event_ids = [1, 2, 3, 4, 5]

results = client.query_bulk(
    input={Event.id: event_ids},
    output=[Event.id, Event.interaction_probability, Event.user.total_logins["30d"]],
)

predictions_df = results.get_data_as_pandas()
print(predictions_df)
```

### Next Steps

- Monitor your model: View model performance metrics and feature distributions in the Chalk dashboard
- A/B test models: Use feature versions to run multiple model versions simultaneously
- Retrain on schedule: Set up periodic retraining using scheduled queries to refresh your training data
- Add more features: Expand your feature set with windowed aggregations and has-many relationships

For more details on specific topics:

- Model Registry - Managing model versions and aliases
- Datasets - Working with offline query results
- Temporal Consistency - Understanding point-in-time correctness
- Snowflake Integration - Configuring Snowflake data sources
# TypeScript Client
source: https://docs.chalk.ai/docs/client-typescript

## Query features with Chalk's TypeScript client library

The Chalk TypeScript client library provides a convenient way to query features from your TypeScript and
JavaScript applications.

- chalk-ts GitHub Repository
- NPM Package

### Installation

Install the Chalk TypeScript client using npm or yarn:

```
npm install @chalk-ai/client
```

or

```
yarn add @chalk-ai/client
```

### Basic Usage

Here's a quick example of how to use the Chalk TypeScript client:

```
import { ChalkClient } from '@chalk-ai/client';

// Initialize the client
const client = new ChalkClient({
  clientId: 'your-client-id',
  clientSecret: 'your-client-secret',
  environmentId: 'your-environment-id'
});

// Query features
const result = await client.query({
  inputs: {
    'user.id': 'user123'
  },
  outputs: [
    'user.credit_score',
    'user.account_age_days'
  ]
});

console.log(result);
```

### Next Steps

- Query Basics - Learn how to query features
- Authentication - Set up authentication for your client
- Online Query API - Explore the online query API
# Python Client
source: https://docs.chalk.ai/docs/client-python

## Query features with Chalk's Python client library

The Chalk Python client library (chalkpy) provides a convenient way to query features from your Python applications.

- PyPI Package
- Python SDK Reference - Complete API documentation

### Installation

Install chalkpy using pip:

```
pip install chalkpy
```

### Basic Usage

Here's a quick example of how to use the Chalk Python client:

```
from chalk import ChalkClient

# Initialize the client
client = ChalkClient(
    client_id='your-client-id',
    client_secret='your-client-secret',
    environment='your-environment-id'
)

# Query features
result = client.query(
    input={
        'user.id': 'user123'
    },
    output=[
        'user.credit_score',
        'user.account_age_days'
    ]
)

print(result)
```

### Next Steps

- Query Basics - Learn how to query features
- Authentication - Set up authentication for your client
- Online Query API - Explore the online query API
- Python SDK Reference - Full API documentation
# Go Client
source: https://docs.chalk.ai/docs/client-go

## Query features with Chalk's Go client library

The Chalk Go client library provides a convenient way to query features from your Go applications.

- chalk-go GitHub Repository
- pkg.go.dev Documentation

### Installation

Install the Chalk Go client using go get:

```
go get github.com/chalk-ai/chalk-go
```

### Basic Usage

Here's a quick example of how to use the Chalk Go client:

```
package main

import (
    "context"
    "fmt"
    "log"

    "github.com/chalk-ai/chalk-go"
)

func main() {
    // Initialize the client
    client, err := chalk.NewClient(
        chalk.WithClientID("your-client-id"),
        chalk.WithClientSecret("your-client-secret"),
        chalk.WithEnvironment("your-environment-id"),
    )
    if err != nil {
        log.Fatal(err)
    }

    // Query features
    result, err := client.Query(context.Background(), chalk.QueryParams{
        Inputs: map[string]interface{}{
            "user.id": "user123",
        },
        Outputs: []string{
            "user.credit_score",
            "user.account_age_days",
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(result)
}
```

### Next Steps

- Query Basics - Learn how to query features
- Authentication - Set up authentication for your client
- Online Query API - Explore the online query API
# Rust Client
source: https://docs.chalk.ai/docs/client-rust

## Query features with Chalk's Rust client library

The Chalk Rust client library provides a convenient way to query features from your Rust applications.

- chalk-rust GitHub Repository
- crates.io Package

### Installation

Add the Chalk Rust client to your Cargo.toml:

```
[dependencies]
chalk-client = "*"
```

Or install using cargo:

```
cargo add chalk-client
```

### Basic Usage

Here's a quick example of how to use the Chalk Rust client:

```
use chalk_client::{ChalkClient, QueryParams};
use std::collections::HashMap;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Initialize the client
    let client = ChalkClient::builder()
        .client_id("your-client-id")
        .client_secret("your-client-secret")
        .environment("your-environment-id")
        .build()?;

    // Query features
    let mut inputs = HashMap::new();
    inputs.insert("user.id".to_string(), "user123".into());

    let result = client.query(QueryParams {
        inputs,
        outputs: vec![
            "user.credit_score".to_string(),
            "user.account_age_days".to_string(),
        ],
    }).await?;

    println!("{:?}", result);
    Ok(())
}
```

### Next Steps

- Query Basics - Learn how to query features
- Authentication - Set up authentication for your client
- Online Query API - Explore the online query API
# Java Client
source: https://docs.chalk.ai/docs/client-java

## Query features with Chalk's Java client library

The Chalk Java client library provides a convenient way to query features from your Java applications.

- chalk-java GitHub Repository

### Installation

Add the Chalk Java client to your project using Maven or Gradle:

### Maven

```
<dependency>
    <groupId>ai.chalk</groupId>
    <artifactId>chalk-java</artifactId>
    <version>latest</version>
</dependency>
```

### Gradle

```
dependencies {
    implementation 'ai.chalk:chalk-java:latest'
}
```

### Basic Usage

Here's a quick example of how to use the Chalk Java client:

```
import ai.chalk.ChalkClient;
import ai.chalk.models.QueryParams;
import ai.chalk.models.QueryResult;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        // Initialize the client
        ChalkClient client = ChalkClient.builder()
            .clientId("your-client-id")
            .clientSecret("your-client-secret")
            .environmentId("your-environment-id")
            .build();

        // Query features
        Map<String, Object> inputs = new HashMap<>();
        inputs.put("user.id", "user123");

        QueryParams params = QueryParams.builder()
            .inputs(inputs)
            .outputs(List.of(
                "user.credit_score",
                "user.account_age_days"
            ))
            .build();

        QueryResult result = client.query(params);
        System.out.println(result);
    }
}
```

### Next Steps

- Query Basics - Learn how to query features
- Authentication - Set up authentication for your client
- Online Query API - Explore the online query API
# C# Client
source: https://docs.chalk.ai/docs/client-csharp

## Query features with Chalk's C# client library

The Chalk C# client library provides a convenient way to query features from your C# and .NET applications.

- chalk-csharp GitHub Repository
- NuGet Package

### Installation

Install the Chalk C# client using the .NET CLI:

```
dotnet add package Chalk.Client
```

Or using the Package Manager Console:

```
Install-Package Chalk.Client
```

### Basic Usage

Here's a quick example of how to use the Chalk C# client:

```
using Chalk.Client;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        // Initialize the client
        var client = new ChalkClient(new ChalkClientOptions
        {
            ClientId = "your-client-id",
            ClientSecret = "your-client-secret",
            Environment = "your-environment-id"
        });

        // Query features
        var result = await client.QueryAsync(new QueryParams
        {
            Inputs = new Dictionary<string, object>
            {
                { "user.id", "user123" }
            },
            Outputs = new List<string>
            {
                "user.credit_score",
                "user.account_age_days"
            }
        });

        Console.WriteLine(result);
    }
}
```

### Next Steps

- Query Basics - Learn how to query features
- Authentication - Set up authentication for your client
- Online Query API - Explore the online query API
# Elixir Client
source: https://docs.chalk.ai/docs/client-elixir

## Query features with Chalk's Elixir client library

The Chalk Elixir client library provides a convenient way to query features from your Elixir applications.

- chalk-elixir Github Repository
- Hex Package

### Installation

Add chalk_elixir to your list of dependencies in mix.exs:

```
def deps do
  [
    {:chalk_elixir, "~> 0.1.0"}
  ]
end
```

Then run:

```
mix deps.get
```

### Basic Usage

Here's a quick example of how to use the Chalk Elixir client:

```
# Configure the client
config :chalk_elixir,
  client_id: "your-client-id",
  client_secret: "your-client-secret",
  environment_id: "your-environment-id"

# Query features
defmodule MyApp do
  alias ChalkElixir.Client

  def query_features do
    {:ok, result} = Client.query(
      %{
        inputs: %{
          "user.id" => "user123"
        },
        outputs: [
          "user.credit_score",
          "user.account_age_days"
        ]
      }
    )

    IO.inspect(result)
  end
end
```

### Next Steps

- Query Basics - Learn how to query features
- Authentication - Set up authentication for your client
- Online Query API - Explore the online query API
# Ruby Client
source: https://docs.chalk.ai/docs/client-ruby

## Query features with Chalk's Ruby client library

The Chalk Ruby client library provides a convenient way to query features from your Ruby applications.

- chalk-ruby GitHub Repository
- RubyGems Package

### Installation

Add chalk_ruby to your Gemfile:

```
gem 'chalk_ruby'
```

Then run:

```
bundle install
```

Or install it directly:

```
gem install chalk_ruby
```

### Basic Usage

Here's a quick example of how to use the Chalk Ruby client:

```
require 'chalk_ruby'

# Initialize the client
client = ChalkRuby::Client.new(
  client_id: 'your-client-id',
  client_secret: 'your-client-secret',
  environment_id: 'your-environment-id'
)

# Query features
result = client.query(
  inputs: {
    'user.id' => 'user123'
  },
  outputs: [
    'user.credit_score',
    'user.account_age_days'
  ]
)

puts result
```

### Next Steps

- Query Basics - Learn how to query features
- Authentication - Set up authentication for your client
- Online Query API - Explore the online query API
# Changelog
source: https://docs.chalk.ai/docs/changelog

## Updates to Chalk!

### February 26, 2026

### Materialized Aggregations - weighted approximate Top K

Chalk now supports a weighted version of approximate Top K
as a materialized aggregation.

Instead of ranking values purely by frequency, you can rank them by weight, such as transaction amount.

This enables questions like:

- Which category accounted for the most revenue last month
- Which segment contributed the highest weighted score

The aggregation maintains constant memory usage and supports streaming updates.

### PyTorch dataset integration

Offline query results can now be converted directly into
PyTorch Dataset objects via the Python client.

This creates a direct path from feature computation to model training, eliminating custom data conversion steps in ML pipelines.

### Trigger Perfetto profiling on demand

Perfetto profiling can now be triggered via HTTP instead of running continuously.

You can deploy the profiling daemon and use chalk profiling perfetto-snapshot to capture traces only when needed. This reduces storage overhead while improving debugging workflows for performance issues.

### February 23, 2026

### Search source code from anywhere

You can now search your deployment source code directly from the global command menu.

Press Command+K or pull up the search bar, select Source Code, and jump straight to matching resolvers or SQL definitions.

This significantly improves debugging workflows that require inspecting feature definitions or resolver logic.

Global search for cod example

### Offline queries support numWorkers

The numWorkers parameter is now supported for offline queries when the Job Queue Manager is enabled.

This allows teams to rate-limit shard execution at the query level instead of modifying cluster-wide configuration. It improves predictability and resource control for large backfills and scheduled jobs.

Read more: https://docs.chalk.ai/docs/job-queue

### Combined Aggs

We recently shipped an optimization to the Chalk query planner that combines aggregations in the query plan by default,
which should dramatically improve performance especially for large offline queries computing multiple aggregations
over high-cardinality datasets.

We have previously exposed this optimization through the environment variable
CHALK_PLANNER_COMBINE_AGGREGATION_OPTIMIZATION as well as the planner option
enable_combine_aggregation_optimization, but this is now defaulted to true in all platform versions v3.31.5 and onwards.

### January 26, 2026

### Faster Query Planning

Query planning is now even faster due to optimization work on the planner.
Planning time improved by an average of 58%, reducing time-to-results and preventing online query timeouts for larger feature graphs.

### ClickHouse for logs and tracing

Logs and tracing now run on ClickHouse, improving search performance. Facets—indexed attributes like service,
environment, status, region, and user_id—help narrow searches and surface the most common values for easier production debugging.

Log Explorer Page with New Facets

### Enhanced query plan visualization

The query plan visualizer now supports
node-by-node navigation through query DAGs. View associations between plan nodes and see how data flows through
each query. Async batch UDFs and conditional nodes display in the data flow, making query plans easier to read and understand.

Log Explorer Page with New Facets

### Store plan stages for scheduled queries

Scheduled queries now include a "Store plan stages" feature.
This allows for improved query debugging.

### December 22, 2025

### Node monitoring improvements

The Nodes tab on the Kubernetes page in the dashboard now supports filtering and sorting by node type, node pool, and CPU utilization.

### Expanded materialized aggregations

Although previously supported as windowed aggregations, approx_percentile aggregations are now supported as materialized aggregations as well. Teams can compute windowed percentile statistics efficiently, improving latency for percentile-based monitoring and modeling.

### Native SQL driver for MS SQL

Chalk now provides a native drive for Microsoft SQL Server, enabling users to write SQL resolvers against their MS SQL data sources, and Chalk compiles and executes the queries using Rust and C++ for performance optimization. This expands Chalk's coverage across data ecosystems, allowing teams that store features or raw data in MS SQL to integrate directly without custom pipelines or data exports.

### December 12, 2025

### Preview messages when setting up stream sources

You can now preview sample messages while configuring a new stream source. This makes it easier to verify that data is flowing correctly and that message formats (like JSON) are being parsed as expected before saving the connection.

Example of stream message preview interface

### Updated navigation pane for faster workflows

We refreshed the left-hand navigation pane to make Chalk easier to move through. Related concepts are now grouped more clearly, visual noise has been reduced, and high-frequency actions are easier to access. The result is a more predictable, friction-free workflow, especially in larger projects.

Optional new navigation pane layout example

### November 25, 2025

### Tracing for query performance diagnosis

Tracing now provides full visibility into how queries execute inside Chalk.

Each resolver and model call is instrumented and timed, allowing teams to pinpoint slow spans, identify inefficient SQL,
and understand query behavior end to end.

Trace data is surfaced directly in the dashboard, so engineers can drill into individual spans to view execution time,
rows returned, and linked data source details.

Traces can be enabled per query using CLI, ChalkClient(), or configured to
sample automatically in production for continuous monitoring.

Example Query Trace

### October 27, 2025

### Stream consumption analytics

Stream incidents now record failure events at one-minute granularity, up from five minutes previously.

This provides finer visibility into where and when stream consumption fails, improving incident analysis and recovery time.
Read more about Chalk’s metrics monitoring.

Stream Monitoring Incident Graph

### Method chaining for Chalk DataFrame

The Chalk DataFrame library now supports method chaining, allowing expressions like

```
tbl = pa.table(
  {
    "txns_last_hour": [[1, 2, 3, 4, 5], [100], [200, 201]],
    "max_txns_allowed": [3, 5, 4],
  }
)
df = DataFrame.from_arrow(tbl)
out = df.project(
  {
    "velocity_score": _.txns_last_hour
      .cardinality()
      .cast(float)
      .least(_.max_txns_allowed + 0.5)
      .ceil()
      .cast(int),
    "velocity_score_2": F.cast(
      F.ceil(
        F.least(
          F.cast(F.cardinality(_.txns_last_hour), float),
          _.max_txns_allowed + 0.5
        )
      ),
      int,
    ),
  }
)
```

The underscore interface is now the recommended API — it’s cleaner, type-safe, and validated by the Chalk function registry.
Discover more about Chalk DataFrame aggregations and filters.

### Cron query tracking

Scheduled (cron) queries now include detailed job-level status tracking, mirroring the system used for backfills.

Teams can now see when jobs start, skip, or fail — and identify the exact cause directly in the UI.
Learn more about scheduling queries for automated runs.

Stream Monitoring Incident Graph

### Vector aggregates

Chalk now supports materialized vector aggregates such as sum and mean.
These precomputed embeddings accelerate workloads involving vector math and high-dimensional similarity features.

### Velox integration in Query Plan Viewer

The query plan viewer now links Velox physical execution data to individual plan nodes.
This lets teams analyze operator-level performance, data flow, and throughput directly from plan output —
helping diagnose slow or memory-heavy offline queries.

### October 23, 2025

### Environment Visibility

Pods now display their Kubernetes service account, namespace, and role ARN.
This makes deployment and debugging more transparent for engineers from within Chalk.

Check the pod view in your Chalk environment to confirm service account mappings.
Learn more about environment visibility in our docs.

Kubernetes Service Accounts

### October 14, 2025

### New Chalk expressions for retrieving the top and bottom N records

Added new (materialize-able) aggregations (min_by_n/max_by_n) for computing the smallest/largest n elements based on any specified ordering column.

Easily compute features like the 5 most recent transactions or the top 3 highest value purchases; combine them with windowed aggregations to compute these at various intervals – e.g., past day, week, month, etc.

```
@features
class Transaction:
    id: int
    user_id: "User.id"
    timestamp: datetime
    amount: float


@features
class User:
    id: int

    transactions: DataFrame[Transaction]
    recent_transaction_amounts: list[int] | None = F.max_by_n(_.transactions[_.amount], _.timestamp, 3)
```

### October 1, 2025

### Chalk Dashboard Improvements

- Custom role creation and assignment functionality, enabling specialized roles like "Machine Learning Scientist" and "Platform Engineer"
- You can now search and filter environment variables in your Chalk dashboard
- Added a connections pane to the overview section of Chalk dashboard that shows the health status of each underlying service in your Chalk deployment

Connections pane

### September 26, 2025

### Derive features at query time with Chalk's Dynamic Expressions

Dynamic expressions enable you to compute new features on-the-fly during online queries without needing to define them in advance.
Leverage Chalk's extensive function library directly in an online query to build adaptive systems that respond to changing requirements without code changes or deployments; this enables:

- Rapid experimentation, A/B testing, and hotfixes to feature logic
- Customization and conditional logic based on user context, business rules, etc.
- Seasonal or time-sensitive feature adjustments (e.g., holiday promotions)

### Added new filtering options to Chalk's log explorer

The log explorer now supports escaped quotes and also negation--making it easier to filter out unwanted results.
Clicking on a log operator toggles it to negation to filter out logs e.g. from a particular service.

### Improvements to Chalk's diff viewer

Enhanced Chalk's diff viewer to show the entire file contents for added/removed files instead of just file names; helps track feature and resolver changes between deployments and branches.

### New Chalk expression for computing the top most common values for a field

Added a new windowed aggregation (approx_top_k), for computing an approximation of the most common values in a field.
Takes in a required k parameter, such as approx_top_k(k=5) for the five approximately-most common values.

```
@feature
class User:
    id: int
    transactions: DataFrame[Transaction]
    most_common_transaction_category: Windowed[list[str]] = windowed(
        "1h",
        max_staleness="15m",
        expression=_.transactions[
            _.category,
            _.at > _.chalk_window,
        ].approx_top_k(k=5)
    )
```

### Chalk developer experience improvements

- Re-running an offline query from the Chalk Dashboard auto-fills the input parameters with the previous values for easier experimentation
- Added support for aggregations over Vector types (sum, mean)
- Pod metrics e.g. request count, etc. are now easily exportable from the Chalk Dashboard (as a CSV)

Re-running Offline Queries

### July 30, 2025

### Chalk diff viewer

New chalk diff command for visualizing code differences across deployments and branches.
The diff viewer highlights additions, deletions, and modifications in a color-coded format, making it easy to spot changes at a glance.

Compare any two branches

chalk diff --branch=<branch_name> --other-branch=<other_branch_name>

Compare a branch with main (default)

chalk diff --branch=<branch_name>

Compare two specific deployments

chalk diff --deployment-id=<deployment_id> --other-deployment-id=<other_deployment_id>

Compare a deployment with main branch

chalk diff --deployment-id=<deployment_id>

### Chalk's Online Query Explorer now supports viewing has-one and has-many relationships

Chalk's Online Query Explorer now supports querying has-one and has-many relationship joins directly in the dashboard.
When exploring a feature like User, you can now run online queries that include data from related features such as Profile (has-one) and Transfers (has-many) without leaving the dashboard interface.

Output explorer with has-one and has-many features

### Chalk dashboard improvements

- Aggregation backfills, which can be viewed from Chalk's Offline Query page now also include a table of the features that have been persisted with the backfill into your online store
- Errors encountered while deploying a branch now bubble up to the branch deployment page in the Chalk Dashboard
- Deactivated users are now visible in UI for more efficient management of inactive accounts

### June 23, 2025

### Process images with Chalk's builtin chat completion API

Chalk's chat completion API now supports multimodal inputs, enabling you to process images alongside text in your LLM workflows. This enhancement allows you to:

- Pass images directly to vision-capable models like GPT-4o
- Combine text and image inputs in a single prompt
- Extract structured information from visual content

```
@features
class Receipt:
   image_url: str
   image_response: P.MultimodalPromptResponse = P.completion(
       model="gpt-5.1",
       messages=[
           P.message(
               "system",
               [
                   {"type": "input_text", "text": "describe this image"},
                   {"type": "input_image", "image_url": _.image_url},
               ],
           ),
       ],
   )
```

### Workspace audit logs and monitoring

The audit log page provides comprehensive tracking of workspace changes, helping you maintain security compliance, troubleshoot issues, and understand your team's activity. Navigate to the audit logs page from the Chalk dashboard by going to Settings → Audit Logs.

The audit log captures:

- Timestamps
- Users or service accounts that made changes
- API endpoints accessed
- Descriptions of the operation
- Success/failure status
- IP addresses
- Trace IDs for debugging

### Enhanced metadata export for online queries

Added a "Full Export" option that includes both query metadata and the actual input/output data (query_values.parquet) to the online queries page. Each export includes query execution details, configurations, query plans, data values, and GraphQL information.

### Added an offline query input explorer

Chalk's offline query explorer makes it easy to inspect, debug, and validate your offline query results through interactive SQL queries and data visualization.

We've introduced an Inputs Explorer that makes it easier to see the inputs of the offline queries that you're running. Having visibility into both inputs and outputs provides a complete picture of your offline query lifecycle, making it easier to troubleshoot issues and optimize query performance.

Inputs explorer for offline queries

### June 6, 2025

### New documentation on optimizing and verifying static Python resolvers

We've added a new page to our docs that serves as a primer on how Chalk optimizes static Python resolvers.
You can verify if your resolvers are being accelerated by checking the query plan page—optimized resolvers are highlighted in yellow and marked as "accelerated".
Python resolvers that cannot be optimized will show an error explaining why.
We've extended support for accelerating Python expressions that

- cast from strings to integers
- contain enums that are inherited from other enums
- use zip and enumerate built-ins
- returns a list of another feature class

```
@online
def get_search_results_documents(
    query_text: SearchQuery.text,
) -> SearchQuery.documents:
    # requests gets accelerated
    docs = requests.get(f"{BASE_URL}/vector_search/{query_text}"
        headers=HEADERS,
    )
    # returning a list of another feature class is also accelerated
    return  [
            Document(
                query_id=query_text,
                content=doc.content,
                title=doc.title,
                similarity_score=doc.similarity_score,
                metadata=doc.metadata,
                rank=rank,
            )
            # enumerate built-in is accelerated
            for rank, doc in enumerate(docs)
        ]
```

Accelerated Python function

### Easily view all of your charts from the Settings page of Chalk Dashboard

We have added a new "All Charts" tab under the "Metric Charts" section of your Settings that displays all charts available in Chalk.
The new tab shows:

- A complete list of all the charts in your environment
- Chart types and categories
- The entities or features that each chart is attached to (for example, a link to view the chart)
- Any associated alerts

All charts page

### May 30, 2025

### Export user permissions as a CSV

You can export information about all users across all environments as a CSV file for easy auditing and compliance reporting.
This export, available from the User Permissions section in your Chalk Dashboard, generates a CSV containing each user's name, email address, unique Chalk ID, and their assigned roles for every project-environment combination in your workspace.

### Chalk resource configuration and dashboard improvements

- Service isolation, which ensures your workloads run on dedicated infrastructure with 1:1 pod-to-node isolation, is now easily toggle-able using a checkbox in the configuration options.
- The instance type selector is now a searchable dropdown that displays machine specifications and validates your resource requests in real-time. If you request more CPUs than the selected instance can provide, you'll see an immediate warning preventing deployment failures and reducing troubleshooting time.
- Added a dropdown for selecting which node pools services should run on.
When selected, services will be directed to the specified node pools with automatic toleration handling. This prevents services from being assigned to incompatible node types and ensures pods are scheduled correctly on tainted nodes.

Resource configuration

### May 23, 2025

### Embed Chalk expressions in versioned features

Feature versions support Chalk expressions, allowing you to define different computation logic for each version of a feature.
This makes it easy to experiment with new feature definitions—you can create multiple versions with different expressions and test them side-by-side to compare their accuracy, performance, and business impact.

```
@features
class Merchant:
    id: str
    fulfilled_orders: int
    total_orders: int
    customer_rating: float
    max_rating: float

    trust_score: float = feature(
        default_version=2,
        versions={
            1: feature(
                description="Trust score based on orders",
                expression=_.fulfilled_orders / _.total_orders,
            ),
            2: feature(
                description="Trust score based on CSAT",
                expression=(_.customer_rating / _.max_rating),
            ),
        }
    )
```

### gRPC support for TypeScript SDK

Our gRPC clients are faster than their HTTP counterparts, offering reduced latency and improved query response times.
We've published a migration guide for transitioning from the HTTP client to the new gRPC implementation in TypeScript.
The function signatures are identical, making for a seamless transition with minimal code changes.
Currently, the gRPC client supports query(), queryBulk(), and multiQuery() operations, covering the most common query use cases.

```
import { ChalkGRPCClient } from "@chalk-ai/client"
import { FeaturesType } from "local/generated_types";

interface FeaturesType {
  "user.id": string;
  "user.fraud_score": number;
}

const client = new ChalkGRPCClient<FeaturesType>();
const result = await client.query({
  inputs: {
    "user.id": "1",
  },
  outputs: ["user.fraud_score"],
});
console.log(result.data["user.fraud_score"].value);
```

### May 16, 2025

### We now support ClickHouse as a Chalk data source

Chalk can connect to your ClickHouse database and other data sources with standard SQL syntax.
Here's an example of a SQL resolver for pulling transaction data:

```
-- type: online
-- resolves: Transaction
-- source: clickhouse
select
  transaction_id,
  transaction_timestamp,
  transaction_amount,
  user_id,
  product_category,
  transaction_channel,
  payment_method_type,
  transaction_status,
  store_location_region
from
  transactions
```

### Refreshed our "What is Chalk?" overview and documentation page

We've refreshed our introductory documentation with more comprehensive examples and new sections that showcase how Chalk serves different roles (AI Engineers, Data Scientists, and Data Engineers).

### Case study with MoneyLion—a leading fintech for banking, investing, and credit building

With Chalk, MoneyLion replaced fragmented Java microservices and manual rewrites with a unified Python-first feature platform.
MoneyLion now iterates in hours instead of weeks, replacing their "slow and disjointed" prototype-to-production cycle with a central feature catalog that makes starting "every use case from scratch" a thing of the past.

### May 2, 2025

### Retrieve historical feature values with SQL

Feature values can now be retrieved from historical storage with SQL enabling direct access to previously computed values with the option to fall back to on-demand re-computation when needed.

### Manage traffic spikes with per-pod rate limiting

Rate limiting now supports per-pod controls through rate-per-second and concurrency parameters, enabling customers to maintain performance targets even during high traffic periods.
The configurable limits help prevent resource exhaustion and ensure consistent application behavior under varying loads.

### Quarterly product update Spring 2025

We've published our quarterly product update, which summarizes improvements and updates from this past Spring, including expanded Python-to-C++ compilation, selective feature persistence controls, and enhanced observability tools.

### April Events Roundup

We've published a recap of the various AI and data conferences our team attended in April 2025.
The blog post covers our participation at NexGen Banking Summit, VeloxCon, Agents & GenAI Infrastructure Summit, OptimizedAI Conference, and Data Council, including key talks and insights we shared about building infra for real-time ML at scale.

### April 21, 2025

### Presented at VeloxCon 25 (April 15-16 at Meta HQ)

Nathan Fenner presented how Chalk leverages Velox as a common compute engine for both online and offline queries:

- Improvements to Velox's expression analysis for low-latency applications
- Custom enhancements for avoiding redundant computations and a specialized online hash join
- Our symbolic Python interpreter that automatically converts Python feature transformations into efficient Velox expressions

Check out the talk (18 mins) on our YouTube page!

### Faster HTTP requests using Chalk Expressions

Chalk functions now support direct HTTP requests via the chalk.functions.http module, enabling you to call external APIs with high performance and without the overhead of Python.
The HttpResponse type provides access to response data including status codes, bodies, headers, and the final URL after redirects.

```
import chalk.functions as F
from chalk import Primary, _
from chalk.features import features
from chalk.functions.http import HttpResponse

@features
class ExternalAPI:
    id: int
    api_endpoint: str

    # GET request returning string response
    api_response: HttpResponse[str] = F.http_get(_.api_endpoint)
    status_code: int = _.api_response.status_code
    response_body: str = _.api_response.body
    headers: dict[str, str] = _.api_response.headers
    final_url: str = _.api_response.final_url
```

### Chalk accelerated Python resolvers are colored as yellow

Symbolic Python resolvers accelerated by Chalk are now highlighted in yellow in the query plan viewer (standard Python resolvers remain purple), making it easier to differentiate resolvers that are accelerated or candidates for symbolic execution.

### New offline query explorer added to the Chalk dashboard

The offline query explorer includes a new grid/table view for entering multiple input features in a single query, with support for adding, editing, and deleting rows and the option to recompute outputs as needed.
The updated interface enhances visibility into these query results through interactive preview panels, comprehensive statistics displays, and detailed metadata exploration.

Offline query explorer

### April 4, 2025

### Chalk developer experience improvements and engineering blog post

We've expanded the coverage for the types of Python resolvers that Chalk can statically compile into C++, speeding up computation.
Check out our new engineering blog post for a deep dive into how our Symbolic Python Interpreter works.

### Chalk dashboard improvements

- Improved how we render stack bar charts within the Chalk dashboard
- Can now filter out and explicitly view Scheduled Queries from the Offline Queries page
- New "Resolved by" column in the features page clearly displays the source resolver for each feature improving traceability
- The Offline Queries page now includes a "Request" button in the details section that displays the parameters used when the query was processed
- Added a "Performance" tab when viewing an Online Query that enables inspecting each resolver referenced e.g. SQL query, code, input and output params, and why it may have not been statically accelerated

Resolved by column

Online Query Performance

### March 26, 2025

### Case study with Apartment List—a thriving apartment rental marketplace transforming search with real-time personalization

With Chalk, Apartment List delivers instant apartment recommendations with real-time price and location flexing, dynamically adapting to user behavior while making low-latency calls to third-party services for the most current pricing information.

### Chalk developer experience improvements

Added store_offline and store_online overrides for features with max staleness, making it easy to exclude features from being persisted, particularly helpful for intermediate features that do not need to be saved e.g. very long text.

```
@features(max_staleness="infinity")
class Document:
    id: str
    file_type: str
    corpus_text: str = feature(store_offline=False, store_online=False)
    extracted_feature_from_corpus_text: str
```

### Chalk dashboard improvements

Chalk's Data Explorer now displays the source of each feature e.g. "Live Resolver"

Sources in Chalk Data Explorer

### March 14, 2025

### Breaking changes to Chalk Client's Go SDK (1.2.0)

Released v1.2.0 of the Chalk Go Client which introduces some breaking changes, most notably:

- The gRPC implementation of Client is removed and replaced with a consolidated NewGRPCClient constructor--configuration remains mostly unchanged.
- OnlineQueryBulk removed to prevent inefficient data conversions, migrate to OnlineQueryBulk`.Use GRPCOnlineQueryBulkResult.UnmarshalInto for structured responses.
- Most GRPCClient methods now return user-friendly wrappers around proto responses, exposing raw responses via RawResponse. Errors are now lifted properly.

### Chalk developer experience improvements

- Singletons can be used to filter DataFrames and has-many relationships.
- New Chalk functions: max_by_n and min_by_n Chalk functions: retrieve the top n rows with the maximum and minimum values from a specified column in a DataFrame or has-many relationship, equivalent to sort_by(sort_col, DESC or ASC).head(n)[result_col]
- New Chalk functions: array_median, array_average, array_sum, array_stddev
- Expanded Python resolver acceleration to support strings manipulation e.g. slices, substrings, and reverses

### Chalk dashboard improvements

- Chalk deployments running on AWS now support manually creating and editing node pools via the dashboard, making it easier to organize and manage different groups of worker nodes in a cluster. This helps distribute workloads more efficiently and scale specific groups as needed.
- The query plan viewer now displays the static expressions generated to accelerate Python resolvers

Static expressions

### February 27, 2025

### Case study with Verisoul--a leading provider of real-time fake account detection

With Chalk, Verisoul iterates on fraud signals, deploys new updates in hours, and increases detection accuracy.

### Easily import feature classes with Chalk Client when experimenting locally

We have implemented two new functions for Chalk Client to aid in local experimentation: client.load_features() and client.get_or_create_branch().

- client.load_features() imports your environment's feature classes into the global namespace, making it easier to reference features when running queries with Chalk Client in a Jupyter notebook.
- client.get_or_create_branch() enables programmatically creating branches or fetching branches for local experimentation.

We've also updated our guide for developing with Jupyter Notebooks.

### Breaking changes to Chalk Client's Go SDK

Released v1.0.0 of the Chalk Go Client which introduces some breaking changes, most notably:

- Removed custom error structs which helps us standardize how Client errors are bubbled up
- Added context.Context to all Client methods enabling us to specify timeouts and custom loggers

### Chalk dashboard improvements

- The deployment metrics chart can now be filtered by named (custom) tags
- The Chalk dashboard has a new errors page for viewing exceptions and issues with Chalk queries

Errors page

### February 20, 2025

### Persist Datasets to your AWS Glue Catalog

ML teams often use offline queries to build training sets by pulling historical data and loading multiple features at specific points in time.
We call the results returned from these offline queries Datasets.
Chalk supports exporting Datasets back into your AWS Glue catalog, letting other teams discover them and enabling downstream analytical workflows.

```
from chalk.integrations import GlueCatalog

dataset = client.offline_query(...)
catalog = GlueCatalog(
    name="aws_glue_catalog",
    aws_region="us-west-2",
    catalog_id="123",
    aws_role_arn="arn:aws:iam::123456789012:role/YourCatalogueAccessRole",
)
dataset.write_to(destination="database.table_name", catalog=catalog)
```

### Chalk dashboard improvements

- The Resolvers page in the Chalk dashboard now has a Request Count column; quickly sort and see which resolvers are being called the most
- The pages for Named Queries and Resolvers now also include errors, use the "Logs and Errors" tab to switch to this filtered viewClick and drag your mouse within the time series graph to zoom in into a time interval and filter down the errors table

Logs and Errors

### February 13, 2025

### Expressive filtering: DataFrames & Has-Manys now support Chalk Expressions!

Has-many (DataFrame) features can now be filtered using any Chalk Expression, unlocking new design patterns and improving DevX!

```
high_cash_flow_merchants: int = _.df[_.id].where(_.total_deposit_amount + F.abs(_.total_withdrawn_amount) > 10**7).count()
average_revenue_from_amazon_retailers: float = _.df[_.revenue].where(F.starts_with(_.merchant_code, "amazon-")).mean()
publicly_traded_not_tech: int = _.df.where((_.industry != "tech") & (_.is_public == True)).count()
holiday_shifts: int = _.df.where(F.is_us_federal_holiday(_.timestamp)).count()
expenses_past_month_with_three_day_lag: float = _.expenses[_.amount].where(_.timestamp - timedelta(days=3) > _.chalk_now - timedelta(days=31)).sum()
```

### Has-many joins using composite keys (Chalk Expressions)

A composite key is a combination of two or more attributes that together uniquely identify an entity.
Link feature classes with composite keys created by a Chalk Expression or through referencing multiple features in a has-one or has-many join.
Here's a has-one relationship between User and Profile classes using both user_id and email as composite join keys.

```
@features
class User:
    id: str = _.alias + "-" + _.org + _.domain
    org_domain: str = _.org + _.domain
    org: str
    domain: str
    alias: str

	# join with composite key
    posts: DataFrame[Posts] = has_many(lambda: User.id == Post.email)
    # multi-feature join
    org_profile: Profile = has_one(lambda: (User.alias == Profile.email) & (User.org == Profile.org))

@features
class Workspace:
    id: str
    # join with child-class's composite key
    users: DataFrame[Users] = has_many(lambda: Workspace.id == User.org_domain)
```

### Chalk runtime improvements

- Chalk attempts to convert each Python resolver into a chain of static expressions that can be accelerated using the function's AST. We've expanded the parser with preliminary support for accelerating Python for loops.
- Improved how we incorporate traffic from Kafka Streams into our (KEDA) autoscaler

### Chalk dashboard improvements

- Reduced the chart load times of large offline queries and queries run through the Data Explorer page of the Chalk dashboard
- Added support for configuring Chalk query contexts and planner options in the Data Explorer page

Data Explorer

### February 06, 2025

### Chalk dashboard improvements

- Added a configuration page for modifying Chalk's connection to your artifact registry e.g. AWS CodeArtifact and Google Artifact Registry
- The deployments overview page now includes hyperlinks to the source code associated with each deployment
- Added a unified page for viewing scheduled resolvers, queries, and pending backfills
- The detailed performance metrics now displays metrics from a query's physical plan e.g. peak memory, input bytes, output rows

Scheduled queries

### January 30, 2025

### Support for embedding models from Vertex AI (GCP)

Chalk can automatically create embeddings for vector feature types through Open AI.
We've expanded our native embed function to support Vertex, Google Cloud's AI platform.

### Extended support for Now--a Chalk primitive for referencing the current time

Now is a Chalk built-in that enables us to incorporate the current time as a filter.
Extending the support for Now unlocks new design patterns; build resolvers and queries that take in

- multiple ids at a single point in time
- a single id at various points in time
- multiple ids at various points in time

Easily sample historical state like all the transactions for 3 users from a particular date or include the current time when calling out to a microservice.

```
sample_some_transactions = offline_query(
    input={Transaction.user_id: [103, 150, 170]},
    input_times=[datetime(2024, 1, 1, tzinfo=timezone.utc)] * 3,
    output=[Transaction],
    recompute_features=True,
)
```

### Chalk branches can be deployed without requiring a local Chalkpy installation

Chalk checks your features for errors locally before deploying them to a remote branch.
Normally, if chalkpy (Chalk’s Python SDK) isn’t installed locally, running chalk apply would fail.
However, we can now lint branches remotely and show your validation errors in the CLI as usual.

### Breaking change in the 1.0.0 major release of Chalk's Java client

This release introduces performance improvements to OnlineQueryResult.unmarshal, but with a few breaking changes:

- Unrequested features are now left as null instead of being initialized as empty objects, similarly so for unrequested dataclass features (subclasses of StructFeaturesClass).
- OnlineQueryResult.unmarshal now consumes scalarsTable, resulting in getScalarsTable() returning an empty table post unmarshaling.
Please create a copy of your results if they need to be retained with .copy().

### Chalk dashboard improvements

- Drag to zoom: Click and drag within a chart or online query to zoom into the selected timeframe; this helps drill down into your charts.
- Faster chart loads: We've improved the load times of charts in the Chalk dashboard!
- Offline queries that run with explain=True now have a performance summary tab that helps trace query performance. Identify operations with their memory consumption, input size, output size, and whether the operation was blocked before executing.
- The Chalk dashboard now supports directly exporting (as Parquet) any view that uses our output explorer: feature previews, datasets, offline queries, and online queries that get persisted to the offline store.

Profiling an offline query

### January 22, 2025

### Chalk's C++ SQL Driver for Spanner now supports inputs (parameterized queries)

Chalk’s C++ driver now supports Spanner queries that explicitly accept input parameters.
These resolvers now run faster, with some query latencies dropping from 24ms to 10ms.

### Enhanced visibility into your Chalk deployment

The Chalk query plan viewer now highlights nodes for Chalk expressions and SQL resolvers using Chalk's C++ driver in orange.
Differentiate between various node types at a glance to debug Chalk queries in less time.

The Kubernetes resource page in the Chalk dashboard has been enhanced to include data from the Kubernetes events API, increasing visibility into nodes, pods, and more objects to come.
Expanding the types of events and their granularity provides better insights into jobs.
These include events like node removal, pod scheduling, and deployment failures.

The query plan viewer in the Chalk dashboard now supports breadcrumbs to hyperlink to a feature’s parent in the query plan viewer, enabling quicker traversal through a feature’s lineage.

Colored nodes in Chalk's query plan viewer

### January 15, 2025

### Improved the granularity at which Chalk services can be rolled back

We improved our CI/CD to support releasing new Chalk images in parallel.
We also extended both the quantity and types of builds (across various Chalk microservices) that we cache, improving the speed and flexibility of Chalk rollbacks!

### Kubernetes node UI enhanced for readability

We improved the Kubernetes Node UI to display additional data about the nodes in your cluster and polished the UI for compactness and readability.

### Chalk dashboard bubbles up feature value metrics

The feature section of the Chalk dashboard will now show salient metrics for your top feature values.
The number of observations, when features were observed, the most observed features, and more.
Metrics can be sliced and grouped by filters like deployment ID, resolver, and operation type, which helps in debugging (at a glance insight into) deployments.

### Query plan viewer now supports node lookups

The Chalk dashboard now also supports query plan node look ups via resolver name, node type, and the input/output features associated with the node.
This makes it easier to trace the behavior of a resolver in complex query plans.

Feature metrics view

### January 6, 2025

### Optimized resource usage with KEDA

We've implemented KEDA (Kubernetes-based Event Driven Autoscaler) and are rolling it out to all customer clusters over the next few weeks.
With KEDA, we've expanded the types of resources that can be dynamically scaled up and down during periods of reduced or no workload.
We look forward to potential improvements both in the elasticity and efficiency of your deployments.

### View and query logs using the CLI

Inspect your log stream the same way you would from the Chalk dashboard but with the command line:

chalk logs [--query="the same string you can put in the web ui"]

Read more about how to view logs using the Chalk CLI in our docs.

### Visualize and trace your feature's data lineage with a Graph View

The Data Lineage page in the Chalk dashboard lets you track your features, specifically how they are derived, when they are referenced (Named Queries), etc.
In addition to the default list view, we have implemented a graph view, making it easier than ever to trace how your features are created and connected.

Graph view for a data lineage

### December 23, 2024

### Search and filter logs by query name, log message, deployment, and more!

You can now search logs in the Logs Explorer in the dashboard using a key-value pair query format:
key1:value1 key2:value2 .... This allows you to combine multiple filters at once. The Logs Explorer
displays the available keywords for filtering, shown below.

Updated log explorer

### Search by file name in the source code viewer

The Source Code Viewer on the Deployments page of the dashboard has been extended!
In addition to searching for keywords in your source code, you can now also search for your files by name.

Source code viewer with file search

### Include query context in Chalk Client queries

The Chalk Client now offers a query_context field that can be accessed
by Python resolvers, allowing you to pass additional information in your queries. The query_context is available
for online queries, bulk online queries, and offline queries for both ChalkClient and
ChalkGRPCClient, and can be tested using ChalkClient.check.

### Expressions support more string, encoding, and date functions

The chalk.functions library now supports more string, encoding, and date functions that can be used in
Chalk expressions. You can now use jaro_winkler_distance
to compute the Jaro-Winkler distance between two strings, partial_ratio to compute
the fuzzywuzzy partial ratio between two strings, and
length to compute the length of a string. We've also added
struct_pack to construct a struct from a mapping, year to extract
the year from a date, and last_day_of_month to return the last date in the month
given a date. To read more about all of the chalk.functions available for writing expressions, check
out our API docs.

### December 16, 2024

### Source code viewer in dashboard supports text search

The source code viewer in the Deployments page of the dashboard now supports fuzzy text search across the source code
for the linked deployment.

Source code viewer with text search

### Dataset revision metadata get and set

DatasetRevision objects now have get_metadata and set_metadata methods to get and
set metadata as a dictionary. This can be useful for storing information such as whether a dataset has been ingested
to the online or offline store, or for tagging and labeling datasets. Read more about all of the DatasetRevision
methods in our API documentation.

### Expressions support more array functions

The chalk.functions library now supports more array functions that can be used in expressions.
array_max and array_min return the maximum and minimum values in an array, respectively. array_distinct returns
a list of the distinct elements in an array, and array_sort sorts the elements of an array by ascending or descending
order. Read more about all of the chalk.functions available for writing expressions in our API docs.

### December 9, 2024

### Expressions support struct field access and more functions

You can now reference dataclass struct fields with expressions.
We've also added more functions to chalk.functions that can be used in expressions,
including is_us_federal_holiday for determining if a date is a federal holiday in the United States,
array_sort for sorting the elements of an array by ascending or descending order, and element_at for
retrieving the element at a specified index in an array. To read more about all of the chalk.functions
in your toolbox for writing expressions, check out our API docs.

### New overview page and dashboard updates for viewing stack traces and recent feature values

We've updated the overview page in the dashboard to show an overview of query activity and cluster health for
your environment. You can now view graphs and metrics for online and offline queries, resolver runs, query latency,
online store activity, deployments, incidents, errors, and connections. Please reach out to the Chalk team if you have
any questions about any of these metrics

Overview page in dashboard

In addition, you can now view the latest stack trace for a pod in your cluster under Settings > Kubernetes, which can
be helpful for debugging offline queries or scheduled runs.

Stack trace for pods in the cluster

Customers with a gRPC engine can also use the new Values Preview tab on the Features page to view recently observed
feature values as loaded from the offline store.

Values preview for features in dashboard

### Postgres Native SQL driver improvements

The Postgres Native SQL driver now supports parameters, as well as returning relationships and scalar aggregations,
expanding the kinds of SQL resolvers querying Postgres sources that we can support with performant C++ execution.

### Read our updated documentation on windowed aggregations

We've updated our documentation on windowed aggregations to include more information on how to
fuse real-time aggregations with materialized pre-aggregations for windowed features.

### December 2, 2024

### We now support Poetry for managing Python dependencies

You can now use Poetry to manage Python dependencies in your Chalk project. Simply
set the requirements field in your chalk.yaml file to pyproject.toml to use Poetry for dependency management.
Read more about how to use configuration files here.

```
project: no-fun-project-names
environments:
  default:
    runtime: 'python310'
    requirements: pyproject.toml
```

### Expressions now support more datetime, JSON, string, and math functions

We've added more functions to chalk.functions that can be used in expressions.
You can now use json_extract_array to extract arrays of strings, bools, numbers, or
nulls from a JSON feature, safe_divide to divide two numbers safely, returning None if the
denominator is zero, to_iso8601 to convert a datetime feature to an ISO 8601 string,
from_unix_seconds and from_unix_milliseconds to
convert a Unix timestamp in seconds or milliseconds to a datetime feature, and finally
regexp_replace to replace substrings in a string using a regular expression. To read more
about all of the chalk.functions in your toolbox for writing expressions, check out our
API docs.

### Warning banners in dashboard for deployments

We've added warning banners in the dashboard to alert you to potential issues in your deployments, such as when
pods fail to start up cleanly. These banners will help with monitoring and observability for deployment health.

Warning banners in dashboard

### November 25, 2024

### Offline query now accepts parquet inputs and relative input times

Offline queries can now accept parquet files as input by passing in a ”s3://“ or ”gs://“
URL as the offline_query(input=“…”) parameter. In addition, you can now define upper and lower bounds for offline
queries with a timedelta that is set relative to the min/max input times per shard. For example, you can now
set offline_query(lower_bound=timedelta(days=-30) to set the lower bound to be 30 days before the earliest input_time
or offline_query(upper_bound=timedelta(days=30) to set the upper bound to be 30 days after the latest input_time.
To read more about offline query parameters, see our API docs.

### Backfill materialized window aggregations over computed features

You can now define a materialized aggregate backfill over features that are returned by multiple resolvers
rather than just one resolver. Read more about the chalk aggregate backfill command in our
CLI docs.

### Expressions now support more array and encoding functions

We've added more functions to chalk.functions that can be used in expressions.
You can now use array_join to concatenate array elements into a string,
cardinality to count the number of elements in an array, as well as
max and min to find the maximum and minimum values, respectively, in an array.
You can also use max_by and min_by to find the row with the maximum and
minimum values in a given column in a DataFrame. For mathematical operations, you can now round
numbers and use from_base for base conversion. For encoding, you can now compute
the sha1, sha256, and sha512 hashes of strings.
Finally, you can use format_datetime to format datetime features using a format string
and strpos to find the first position of a substring in a string. To read more about all of the
chalk.functions in your toolbox for writing expressions, check out our
API docs.

### Optionally cache nulls or default feature values in the online store

Where you could previously choose whether to cache null feature values in the online store,
you can now use the cache_defaults parameter to optionally cache default feature
values in the online store. Customers with DynamoDB or Redis online stores can also choose to
evict_defaults from the online store, evicting the entry that would have been a default value from the online
store if it exists. Read more about how to use cache_defaults and cache_nulls in our
API docs.

### Define features as map types

You can now define features as map types and reference these map features in expressions.

```
from chalk.features import features

@features
class User:
    id: str
    user_preferences: dict[str, bool] = {"Advertising cookies": True, "Functional cookies": True}
```

### Retrieve map types from DynamoDB data sources as either dicts or strings

You can now retrieve Map document types
from DynamoDB data sources as either dicts or strings, using the new map feature type.

### Dashboard updates for viewing Kubernetes logs

We’ve exposed much more granularity for Kubernetes logs in the dashboard. You can now filter logs by pod name,
component, resource group, and deployment. These filters are set in the page query params, which means that you can
send a link to pre-filtered log views. The links that are newly exposed in the Kubernetes pod view now directs to a
pre-filtered logs viewer page. Finally, you can now view pod conditions in the Kubernetes pod view, which can include
useful information for debugging failed or pending pods.

Detailed Kubernetes logs in dashboard

### Improved stacktrace rendering in Chalk CLI

We've drastically improved the rendering of stacktraces in the Chalk CLI with improved syntax highlighting
and clearer formatting to make debugging easier.

### November 18, 2024

### View Kubernetes resources created by each deployment in the dashboard

You can now view the Kubernetes pods created by each deployment in the dashboard along with additional
details like the pod states and the resources requested by each pod.

Pod Resources in Deployment Page

### Resolve list features with expressions

We've added the array_agg function to chalk.functions to help you resolve list features with underscore
expressions. For example, you can now express the following features to aggregate
all categories of videos watched for a user.

```
import chalk.functions as F
from chalk import DataFrame
from chalk.features import _, features

@features
class VideoInteraction:
    id: str
    video_url: str
    video_category: str
    user_id: "User.id"

@features
class User:
    id: str
    videos_watched: DataFrame[VideoInteraction]
    all_watched_video_categories: list[str] = F.array_agg(_.videos[_.category])
```

To see all of the chalk.functions that you can use in expressions, see
our API documentation.

### View usage information through the Chalk CLI

Users can now use the chalk usage commands to view usage information for their
projects and environments. If you have any questions, please reach out to the Chalk team.

### November 11, 2024

### Idempotency in triggered resolver runs

We now provide an idempotency key parameter for triggering resolver runs
so that you can ensure that only one job will be kicked off per idempotency key provided.

### ChalkClient.check() function for easy integration testing

The ChalkClient now has a check function that enables you to run a query and
check whether the query outputs match your expected outputs. This function should be used with
pytest for integration testing. To read more about different
methods and best practices for integration testing, see our integration test docs.

### Expressions support more mathematical and logical functions

This week, we've added mathematical functions floor, ceil, and abs to chalk.functions, along with
the logical functions when, then, otherwise, and is_null. We've also added the haversine function
for computing the Haversine distance between two points on Earth given their latitude and longitude. These
points can be used in expressions to define features with code that can be
statically compiled in C++ for faster execution. See the full list of functions you can use in underscore
expressions in our API docs.

### Dashboard improvements for providing more insights into resolver performance and execution

In the dashboard, users can now view the P50, P75, P95, and P99 latencies for resolvers in the table under
the Resolver tab of the menu. You can also customize which columns are displayed in the table by clicking
the gear icon in the top left corner of the table.

In addition, we've added a SQL Explorer for examining resolver output for queries that are run with the
store_plan_stages=True parameter.

### chalk healthcheck in CLI

You can now use the chalk healthcheck command in the CLI to view information on the health of Chalk's API
server and its services. The healthcheck provides information for the API server based on the active
environment and project. To read more about the healthcheck command, see
the CLI documentation.

### November 4, 2024

### Offline Query Specifications for shards and workers

When running an asynchronous offline query, you can now specify the inputs num_shards and num_workers as
parameters to allow for more granular control over the parallelization of your query execution. To see all of the
offline query options, check out the offline query documentation.

In addition, offline query progress reporting now specifies progress by shard, giving developers more insight
into where their offline query is in the execution progress.

### ChalkClient can now use the default Git branch

You can now default to using the name of your current Git branch when developing using the ChalkClient.
For example, if you have checked out a branch named my-very-own-branch you can now set ChalkClient(branch=True)
and all of your client calls will be directed at my-very-own-branch. To read more about how to use ChalkClient, see
our API documentation.

### Expressions support functions for URL parsing, regular expressions, and more

We've added more functions to chalk.functions that can be used in expressions.
You can now use regexp_like, regexp_extract, split_part, and regexp_extract_all to do regular expression matching and
use url_extract_host, url_extract_path, and url_extract_prtocol to parse URL's. In addition, we've added
helpful logical functions like if_then_else, map_dict, and cast to broaden the span of features that you can
define using expressions. To read more about all of our functions, check out our
API documentation.

### Deployment build logs for AWS environments

We now provide more detailed build logs for deployments in AWS environments in the dashboard!

### October 28, 2024

### Run predictions against SageMaker from Chalk, and do so much more in expressions

We've added a new function chalk.functions.sagemaker_predict that allows
you to run predictions against a SageMaker endpoint to resolve features. Read more about how to define
a SageMaker endpoint, encode your input data, and run predictions in our SageMaker tutorial.

In addition to being able to make SageMaker calls, expressions now support a
variety of new functions. With these functions imported from chalk.functions, you can perform encoding,
decoding, math, datetime manipulation, string manipulation, and more! For example, say you have a Transaction
feature, where you make a SageMaker call to enrich the transaction data and provide a label for the transaction,
and you parse this label for other features. You can now define all of these features related to transaction
enrichment using expressions and Chalk functions in the feature definition:

```
from datetime import date
import chalk.functions as F
from chalk.features import _, features, Primary

@features
class Transaction:
    id: str
    amount: float
    date: date
    day: int = F.day_of_year(_.date)
    month: int = F.month_of_year(_.date)

    sagemaker_input_data: bytes = F.string_to_bytes(_.id, encoding="utf-8")
    transaction_enrichment_label: bytes = F.sagemaker_predict(
        _.sagemaker_input_data,
        endpoint="transaction-enrichment-model_2.0.2024_10_28",
        target_model="model_v2.tar.gz",
        target_variant="production_variant_3"
    )
    transaction_enrichment_label_str: str = F.bytes_to_string(_.transaction_enrichment_label, encoding="utf-8")
    is_rent: bool = F.like(_.transaction_enrichment_label_str, "%rent%")
    is_purchase: bool = F.like(_.transaction_enrichment_label_str, "%purchase%")

```

### Nested materialized windowed aggregation references!

You can now reference other windowed aggregations in your windowed aggregation expressions. To read more about
how to define your windowed aggregations, see our example here.

### Updated usage dashboard to view CPU and storage requests grouped by pod and namespace

We've updated the Usage Dashboard with a new view under the Pod Resources tab that allows you to view CPU and storage
requests by pod as grouped by cluster, environment, namespace, and service! If you have any questions about the usage
dashboard, please reach out to the Chalk team.

### Dropping support for Python 3.8

From chalkpy==2.55.0, Chalk is dropping support for Python 3.8,
which has reached end-of-life.
If you are still using Python 3.8, please upgrade to Python 3.9 or higher.

### October 21, 2024

### Pub/Sub streaming source

We've enabled support for using Pub/Sub as a streaming source.
Read more about how to use Pub/Sub as a streaming source here.

### Online/Offline Storage for Offline Queries

You can automatically load offline query outputs to the online and offline store using the boolean parameters
store_online and
store_offline. Below is an example of how to
use these parameters.

```
from chalk.client import ChalkClient

client = ChalkClient()
ds = client.offline_query(
    input={"user.id": [1, 2, 3, 4, 5]},
    output=["user.num_interactions_l7d", "user.num_interactions_l30d", "user.num_interactions_l90d"],
    store_online=True,
    store_offline=True
)
```

### SQL explorer for query outputs in the dashboard

Customers running gRPC servers can now run SQL queries on the dataset
outputs of online and offline queries in the dashboard. To enable this feature for your deployment,
please reach out to the team.

SQL Explorer for Query Outputs

### Color updates in the dashboard

We've updated our color scheme in the dashboard to more clearly differentiate between successes and failures
in metrics graphs!

Red for failures and green for successes

### October 14, 2024

### SQL explorer in dashboard for datasets

Customers can now run SQL queries on dataset outputs
in the dashboard. To use this feature, navigate to the Datasets page in the menu, select a dataset,
and click on the Output Explorer tab.

SQL Explorer for Datasets

### Optionally evict nulls from your DynamoDB online store

Last week we enabled the option to decide whether to persist null values for features in Redis lightning
online stores, and this week we have enabled this feature in DynamoDB online stores. By default, null
values are persisted in the online store for features defined as Optional, but you can set cache_nulls=False
in the feature method to evict null values. Read more about how to use the cache_nulls parameter
here.

### Set environment variables and more in the Advanced section of the Cloud Resource Configurations page in the dashboard

You can set cloud resource configurations for your environment by navigating to Settings > Resources in the
dashboard. In addition to specifying resource configurations for resource groups like instance counts and CPU,
you can now also set environment variables and other settings like Kubernetes Node Selectors. The Kubernetes Node
Selector enables you to specify the machine family you would like to use for your deployment. For example,
this would map to EC2 Instance Types
for AWS deployments or Compute Engine Machine Families
for GCP deployments. If you have any questions about how to use any of these settings in the configuration page,
please reach out to the team.

Cloud Resource Configurations Advanced Settings

### October 7, 2024

### Expressions support datetime subtraction and total_seconds

Expressions now support datetime subtraction and the use of a new
library function chalk.functions.total_seconds. This allows you to compute the number of seconds
in a time duration and define more complex time interval calculations using performant underscore
expressions.

For example, to define a feature that computes the difference between two date features in days and weeks,
we can use chalk.functions.total_seconds and underscore date expressions together.

```
from chalk.functions as F
from chalk.features import _, features, Primary
from datetime import date
@features
class User:
    id: str
    created_at: date
    last_activity: date
    days_since_last_activity: float = F.total_seconds(date.today() - _.last_activity) / (60 * 60 * 24)
    num_weeks_active: float = F.total_seconds(_.last_activity - _.created_at) / (60 * 60 * 24 * 7)
```

### Optionally evict nulls from your Redis lightning online store

You can now select whether to persist null values for features in the Redis lightning online store
using the cache_nulls parameter in the feature method. By default, null values are persisted in the
online store for features defined as Optional. If you set cache_nulls=False, null values will
not be persisted in the online store.

```
from chalk import feature
from chalk.features import features, Primary, Optional

@features
class RestaurantRating:
    id: str
    cleanliness_score: Optional[float] = feature(cache_nulls=False) # null values will not be persisted
    service_score: Optional[float] = feature(cache_nulls=True) # null values will be persisted. This is the default behavior.
    overall_score: float # null values are not persisted for required features
```

### Feature value metrics from gRPC server and feature table updates

Customers running the gRPC server can now reach out to enable feature value metrics. Feature value metrics include
the number of observations, number of unique values, and percentage of null values over all queries, as well as the
running average and maximum of features observed. Please reach out if you'd like to enable feature value metrics.

Feature value metrics

Additionally, the feature table in the dashboard has been updated to allow for customization of columns displayed,
which enables viewing request counts over multiple time ranges in the same view.

### September 30, 2024

### Compute cosine similarity between two vector features

chalk.functions now offers a cosine_similarity function:

```
import chalk.functions as F
from chalk.features import _, embedding, features

@features
class Shopper:
      id: str
      preferences_embedding: Vector[1536]

@features
class Product:
      id: str
      description_embedding: Vector[1536]

@features
class ShopperProduct:
      id: str
      shopper_id: Shopper.id
      shopper: Shopper
      product_id: Product.id
      product: Product
+     similarity: float = F.cosine_similarity(_.shopper.preferences_embedding, _.product.description_embedding)
```

Cosine similarity is useful when handling vector embeddings, which are often used when analyzing unstructured text. You
can also use embedding to compute vector embeddings with Chalk.

### Dashboard now shows metrics for offline query runs

When looking at an offline query run in the dashboard, you'll now find a new Metrics tab showing query metadata, CPU utilization,
and memory utilization.

### Configuration option for recomputing features on cache misses

We have a new offline query configuration option for recomputing features only when they are not already available in
the offline store. This option is useful for workloads with computationally expensive features that cannot easily be
recomputed. Please reach out if you'd like to try this feature.

### September 23, 2024

### Configurable retry policy for SQL resolvers

Sometimes, a SQL resolver may fail to retrieve data due to temporary unavailability. We've added new options for
configuring the number of retry attempts a resolver may make (and how long it should wait between attempts). If you're
interested in trying out this new functionality early, please let the team know.

### Has-one join keys can be chained

When creating has-one relationships, you can set the primary key of the child feature class to the
primary key of the parent feature class. For example, you may model an InsurancePolicy feature class as belonging to
exactly one user by setting InsurancePolicy.id's type to Primary[User.id].

Now, we've updated Chalk so that you can chain more of these relationships together. For example, an InsurancePolicy
feature class may have an associated InsuranceApplication. The InsuranceApplication may also have an associated
CreditReport. Chalk now allows chaining an arbitrary number of has-one relationships. Chalk will also validate these
relationships to ensure there are no circular dependencies.

Here's an example where we have features describing a system where user has one insurance policy, each policy has one
submitted application, and each application has one credit report:

```
from chalk import Primary
from chalk.features import features

@features
class User:
      id: str
      # :tags: pii
      ssn: str
      policy: "InsurancePolicy"

@features
class InsurancePolicy:
      id: Primary[User.id]
      user: User
+     application: "InsuranceApplication"

+ @features
+ class InsuranceApplication:
+     id: Primary[InsurancePolicy.id]
+     stated_income: float
+     # For the sake of illustrating has-one relationships,
+     # we're assuming exactly one credit report per
+     # application, which may not be realistic. A has-many
+     # relationship may be more accurate here.
+     credit_report: "CreditReport"
+
+ @features
+ class CreditReport:
+     id: Primary[InsuranceApplication.id]
+     fico_score: int
+     application: InsuranceApplication
```

To query for a user's credit report, you would write:

```
client.query(
    inputs={User.id: "123"},
    output=[User.policy.application.credit_report],
)
```

To write a resolver for one of the dependent feature classes here, such as CreditReport.fico_score, you would still
reference the relevant feature class by itself:

```
@online
def get_fico_score(id: CreditReport.id) -> CreditReport.fico_score:
    ...
```

As an aside, if your resolver depends on features from other feature classes, such as User.ssn, we instead recommend
joining those two feature classes directly for clarity (which was possible prior to this changelog entry):

```
from chalk import Primary
- from chalk.features import features
+ from chalk.features import features, has_one

@features
class User:
      id: str
      # :tags: pii
      ssn: str
      policy: "InsurancePolicy"
+     credit_report: "CreditReport" = has_one(lambda: User.id == CreditReport.id)

# ... the rest of the feature classes

+ @online
+ def get_fico_score(id: User.id, ssn: User.ssn) -> User.credit_report.fico_score:
+     ...
```

### User permissions page shows roles per user

When you view Users in the Chalk settings page, you will now find a menu for viewing the roles associated with each
user, whether those roles are granted directly or via SCIM.

An example user with admin and owner roles

### September 16, 2024

### New feature and resolver UI in the dashboard

We have shipped a new UI for the Features and Resolvers sections of the dashboard!

The new UI has tables with compact filtering and expanded functionality. You can now filter
and sort by various resolver and feature attributes! The tables also provide column resizing
for convenient exploration of the feature catalog.

Resolver table with compact filtering and sorting

The features table now includes request counts from the last 5 minutes up to the last 180 days,
has built-in sorting, and has a Features as CSV button to download all the feature attributes
in your table as a CSV for further analysis.

Feature table with request count and csv export button

### New helper functions for feature computation

The new chalk.functions module contains several helper functions for feature computation. For example, if you have a
feature representing a raw value in GZIP-compressed value, you can use gunzip with an underscore
reference to create an unzipped feature. The full list of available functions
can be found in our
expression documentation.

### JSON feature type

You can now define features with JSON as the type after importing JSON from the chalk module. You can then
reference the JSON feature in resolver and query definitions. You can also retrieve scalar values from JSON features
using the json_value function.

### September 9, 2024

### Configure Chalk to not cache null feature values

By default, Chalk caches all feature values, including null. To prevent Chalk from caching null values, use the
feature method and set cache_nulls to False.

### More static execution of certain Python resolvers

We built a way to statically interpret Python resolvers to identify ones that are eligible for C++ execution, which has
faster performance. For now, resolvers are eligible if they do simple arithmetic and logical expressions. If you're
interested in learning more and seeing whether these new query planner options would apply to your codebase, please
reach out!

### New tutorial for using Chalk with SageMaker

We have a new tutorial for using Chalk with SageMaker available now. In the tutorial, we
show how to use Chalk to generate training datasets from within a SageMaker pipeline for model training and evaluation.

### September 3, 2024

### Feature catalog shows associated named queries

In the August 19 changelog entry, we announced
NamedQuery, a tool for naming your queries so that you can execute them without writing out
the full query definition.

This week, we've updated the dashboard's feature catalog so that it shows which named queries
reference a given feature as input or output.

Feature catalog showing links to named queries a feature is an input or output of

### August 26, 2024

### View aggregation backfills in the dashboard

We added a new Aggregations page to the dashboard where you can see the results of aggregate backfill commands. Check it out to see what resolvers were run for a backfill, the backfill's
status, and other details that will help you drill down to investigate performance.

For more details on aggregate backfills, see our documentation on managing windowed
aggregations.

### August 19, 2024

### Execute queries by name

Instead of writing out the full definition of your query each time you want to run it, you can now register a name for
your query and reference it by the name!

Here's an example of a NamedQuery:

```
from chalk import NamedQuery
from src.feature_sets import Book, Author

NamedQuery(
    name="book_key_information",
    input=[Book.id],
    output=[
        Book.id,
        Book.title,
        Book.author.name,
        Book.year,
        Book.short_description
    ],
    tags=["team:analytics"],
    staleness={
        Book.short_description: "0s"
    },
    owner="mary.shelley@aol.com",
    description=(
        "Return a condensed view of a book, including its title, author, "
        "year, and short description."
    )
)
```

After applying this code, you can execute this query by its name:

```
chalk query --in book.id=1 --query-name book_key_information
```

To see all named queries defined in your current active deployment, use chalk named-query list.

As Shakespeare once wrote, "What's in a named query? That which we call a query
by any other name would execute just as quickly."

### Miscellaneous improvements

- The offline query page of the dashboard now shows which table in your offline store contains the query's output values.

### August 12, 2024

### Queries can reference multiple feature namespaces

Previously, you could only reference one feature namespace in your queries. Now you can request features from multiple
feature namespaces. For example, here's a query for a specific customer and merchant:

```
client.query(
    input={
        Customer.id: 12345,
        Merchant.id: 98765,
    },
    output=[Customer, Merchant],
)
```

### Dashboard resources view shows allocatable CPU and memory

The resources page of the dashboard now shows the allocatable and total CPU and memory for each of your Kubernetes
nodes. Kubernetes reserves some of each machine's resources for internal usage, so you cannot allocate 100% of a
machine's stated resources to your system. Now, you can use the allocatable CPU and memory numbers to tune your resource
usage with more accuracy.

### Performance improvements

We identified an improvement for our query planner’s handling of temporal joins! Our logic
for finding the most recent observation for a requested timestamp is now more efficient. Happy time traveling!

### August 5, 2024

### DynamoDB with PartiQL

We now support DynamoDB as a native accelerated data source! After connecting your AWS credentials,
Chalk automatically has access to your DynamoDB instance, which you can query with PartiQL.

### Expressions support references to the target window duration

Expressions on windowed features can now include the special
expression _.chalk_window to reference the target window duration. Use _.chalk_window in windowed aggregation
expressions to define aggregations across multiple window sizes
at once:

```
@features
class Transaction:
    id: int
    user_id: "User.id"
    amount: float

@features
class User:
    id: int
    transactions: DataFrame[Transaction]
    total_spend: Windowed[float] = windowed(
        "30d", "60d", "90d",
        default=0,
        expression=_.transactions[_.amount, _.ts > _.chalk_window].sum(),
        materialization={"bucket_duration": "1d"},
    )
```

### Offline queries allow resource overriding

- offline_query now supports the resources parameter. resources
allows you to override the default resource requests associated with offline queries and cron jobs so that you can
control CPU, memory, ephemeral volume size, and ephemeral storage.

### July 26, 2024

### Dashboard improvements

- The offline query page of the dashboard now shows live query progress. After query completion, the query page will
also show how long each resolver took to run."
- The Kubernetes resource page in the dashboard shows which kinds of hardware resources are currently running. It also
allows you to group resources by application, component, and other common groupings.

### July 19, 2024

### Datasets and dataset revisions now support previews and summaries

Datasets and DatasetRevisions have two new methods:
preview and summary. preview shows the first few rows of the
query output. summary shows summary statistics of the query output. Here's an example of summary output:

```
     describe  user.id  ...  __index__ shard_id batch_id
0       count      1.0  ...        1.0        0        0
1  null_count      0.0  ...        0.0        0        0
2        mean      1.0  ...        0.0        0        0
3         std      0.0  ...        0.0        0        0
4         min      1.0  ...        0.0        0        0
5         max      1.0  ...        0.0        0        0
6      median      1.0  ...        0.0        0        0

[7 rows x 14 columns]
```

### Create isolated node pools for your resource groups (in AWS)

Chalk resource groups create separate independent deployments of the query server to prevent resource contention. For
example, one team may want to make long-running analytics queries and another may want to make low-latency queries in
line with customer requests.

We have updated the Cloud Resource Configuration page! You can now configure resource groups to use completely independent
node pools to ensure your workflows run on separate computer hardware. The configuration page also allows you to specify
exactly what kind of hardware will be available in each resource group so you can optimize the balance between cost and
performance.

This feature is currently available for customers running Chalk in EKS, but will be available soon for customers using
GKE.

### Performance improvements

- We've significantly improved SQL runtime in our query planner by executing eligible queries in C++ instead of
SQLAlchemy. Chat with our support team if you'd like to update your query planner options.
- We improved the performance of some expressions by executing count() operations as native dataframe
operations.

### Miscellaneous improvements

- Our feature catalog now lets you filter features by their context (online or offline). Additionally, you can now search
features by their name, description, and owner.
- We fixed an issue where some underscore expressions had incorrect typechecking.

### July 10, 2024

### Feature catalog

You can now view and filter features in the feature catalog by their tags and owners.

Feature catalog filtering by tag and owner

### July 1, 2024

### Chalk gRPC

We shipped a gRPC engine for Chalk that improved performance by at least 2x through improved data serialization,
efficient data transfer, and a migration to our C++ server. You can now use ChalkGRPCClient to run queries with the
gRPC engine and fetch enriched metadata about your feature classes and resolvers through the get_graph method.

### Spine SQL query

With ChalkPy v2.38.8 or later, you can now pass spine_sql_query
to offline queries. The resulting rows of the SQL query will be used as input to the offline query. Chalk will compute
an efficient query plan to retrieve your SQL data without requiring you to load the data and transform it into input
before sending it back to Chalk. For more details, check out our
documentation.

### Static planning of expressions

We shipped static planning of expressions. expressions
enable you to define and resolve features from operations on other features. When you use expressions, we
now do static analysis of your feature definition to transform it into performant C++ code.

Expressions currently support basic arithmetic and logical operations, and we continue to build out more
functionality! See the code snippet below for some examples of how to use expressions:

```
@features
class SampleFeatureSet:
    id: int
    feature_1: int
    feature_2: int
    feature_1_2_sum: int = _.feature_1 + _.feature_2
    feature_1_2_diff: int = _.feature_1 - _.feature_2
    feature_1_2_equality: bool = _.feature_1 == _.feature_2
```

### June 28, 2024

### Chalk deployment tags

You can now add tags to your deployments. Tags must be unique to each of your environments. If you add an already existing tag to a new deployment, Chalk will remove the tag from your old deployment.

Tags can be added with the --deployment-tag flag in the Chalk CLI:

```
chalk apply --deployment-tag=latest --deployment-tag=v1.0.4
```

### Resource configuration management in dashboard

We updated our UI for resource configuration management in the dashboard! You can now toggle your view between
a GUI or a JSON editor. The GUI exposes all the configuration options available in the JSON editor, including
values that aren't set, and allows you to easily adjust your cluster's resources to fit your needs.

resource configuration management

### June 19, 2024

### New data sources and native drivers

We added integrations for Trino and Spanner as new data sources. We've also added native drivers for Postgres and
Spanner, which drastically improves performance for these data sources.

### May 29, 2024

### Heartbeating

We now have heartbeating to poll the status of long-running queries and resolvers, which will now mark any hanging
runs that are no longer detected as "failed" after a certain period of time.

### May 14, 2024

### Data source and feature-level RBAC

We expanded the functionality of our service tokens to enable role-based access control (RBAC) at both the
data source and feature level. On the datasource level, you can now restrict a token to only access data sources
with matching tags to resolve features. On the feature level, you can restrict a token's access to tagged features
either by blocking the token from returning tagged features in any queries but allowing the feature values to be
used in the computation of other features, or by blocking the token from accessing tagged features entirely.

datasource and feature level rbac

### May 8, 2024

### Incremental Status

We shipped statuses during incremental runs such that users can get a signal of the current high water mark of
data being updated.

```
chalk incremental status  --scheduled_query get_some_data__daily
✓ Fetched resolver progress state
Resolver:                 N/A
Query:                    run_this_query_daily
Environment:              chalk12345
Max Ingested Timestamp:   2024-07-01T16:01:46+00:00
Last Execution Timestamp: 2024-07-01T00:01:27.421873+00:00
```

### April 18, 2024

### Miscellaneous improvements

- Windowed resolvers have expanded to allow for hourly cadences.

### April 9, 2024

### Miscellaneous improvements

- SQL resolvers have improved error reporting for failures related to type conversion (e.g., if your resolver selects
an int column, but the feature's type is string)

### March 29, 2024

### Miscellaneous improvements

- SQL file resolvers have spellcheck (based on Levenshtein distance)
- Failed annotation parsing raises a type error with a more helpful error message

### March 19, 2024

### Scheduled Queries

Chalk now supports executing an offline_query on a schedule. Effectively, this extends the existing "scheduled resolver"
functionality and allows you to execute more complicated data ingestion or caching workflows without needing to
use Airflow or other external schedulers to orchestrate resolver execution.

Here's an example of a scheduled query that caches the number of transactions a user has made in the last 24 hours into
the online store:

```
from chalk import ScheduledQuery

ScheduledQuery(
    name="num_transactions_last_24h",
    output=[User.num_transactions_last_24h],
    schedule="0 0 * * *", # every day at midnight
    store_online=True,    # store the result in the online store
    store_offline=False,  # don't store this value in the offline store
)
```

### Bugfixes and improvements

- offline_query(...) now accepts sample_features: list[Feature] as an argument. This works in conjunction
with recompute_features, and allows you to write something like:

```
ChalkClient().offline_query(
    input={User.id: [...]},
    output=[User.full_name],
    recompute_features=True,                          # means "recompute all features
    sample_features=[User.first_name, User.last_name] # but sample these features from the offline store
)
```

This is useful when you have a large number of features that you want to recompute, but only a few that you want to sample.

- ChalkClient.offline_query now accepts run_asynchronously: bool to explicitly opt a query into running on an isolated worker.
- DataSet.to_polars()/.to_pandas() now accept output_ts: str and output_id: str to customize the name of the timestamp and id columns in the output dataframe.
- Feature and resolver discovery during chalk apply is roughly twice as fast as of chalkpy v2.33.9.
- Dataset downloads no longer have any dependency on locally registered features, which resolves crashes for certain dataset management workflows.
- ChalkClient.query now supports request_timeout: float, which is passed to the underlying requests.request call.

### March 8, 2024

### Bugfixes and improvements

- A persistent issue with chalk drop has been resolved. Now, chalk drop will allow you to reset a feature whose
deletion has been deployed to the active deployment, which will allow you to re-deploy the feature. Previously,
it was possible to get into a state that was impossible to recover from without support.
- tags(...) allows you to extract the tags of a @features class or a property (Feature) of that class.
- DataSet.to_polars()/to_pandas() now raises an error if the dataset computation had errors. This
prevents the user from accidentally using a dataset that was not computed correctly. If you wish to use the dataset
anyway, you can use DataSet.to_polars(ignore_errors=True).

### March 1, 2024

### Support for custom SQL sampling in offline query

You can now specify a custom SQL sampling query for offline queries. This allows you to use a native SQL query
to compute the query's entity spine for offline queries. This is useful when you have a complicated sampling policy
(i.e. class-based sampling). Additional non-primary key features can be provided as well.

### January 22, 2024

### required_resolver_tags for queries

You can now specify required_resolver_tags when querying. This allows you to ensure that a query only considers a
resolver if it has a certain tag. This is useful for guaranteeing that a query only uses resolvers that are
cost-efficient, or for enforcing certain compliance workflows.

In this example:

```
@offline()
def fetch_credit_scores() -> DataFrame[User.id, User.credit_score]:
    """
    Call bureaus to get credit scores; costs money for each record retrieved.
    """

    return requests.post(...)

@offline(tags=["low-cost"])
def fetch_previously_ingested_credit_scores() -> DataFrame[User.id, User.credit_score]:
    """
    Pull previously retrieved credit scores from Snowflake only
    """

    return snowflake.query_string("select user_id as id, credit_score from ...").all()
```

querying with required_resolver_tags can be used to enforce that only 'low-cost' resolvers are executed --

```
# This query is guaranteed to /never/ run any resolver that isn't tagged "low-cost".

dataset = ChalkClient().offline_query(
    input={User.id:[1,2,3]},
    output=[
        User.credit_score
    ],
    recompute_features=True,
    required_resolver_tags=["low-cost"]
)
```

### October 24, 2023

### Support for Python 3.11

You can now use either of Python 3.11 or 3.10 on a per-environment basis.

```
project: my-project-id
environments:
  default:
    runtime: python310
  develop:
    runtime: python311
```

See Python Version for more information.

### October 23, 2023

### Quality of Life Improvements

- ChalkClient.query_bulk(...) and multi_query no longer require that references features
be defined as Python classes, and string names for inputs and outputs can now be used instead.

### October 11, 2023

### Alert descriptions

Alerts now support descriptions, which can be used to provide more context about the alert.

```
from chalk.monitoring import Chart, Series
Chart(name="Request count").with_trigger(
    Series
        .feature_null_ratio_metric()
        .where(feature=User.fico_score) > 0.2,
+   description="""*Debugging*
+
+   When this alert is triggered, we're parsing null values from
+   a lot of our FICO reports. It's likely that Experian is
+   having an outage. Check the <dashboard|https://internal.dashboard.com>.
+   """
)
```

These descriptions can also be set in the Chalk dashboard via the metric alerts interface.

Alert description interface:

### October 5, 2023

### query_bulk support for notebooks

The query_bulk method is now available in the ChalkClient class. This method allows you to query for multiple rows of
features at once.

This method uses Apache Arrow's Feather format
to encode data. This allows the endpoint to transmit data (particularly numeric-heavy data) using roughly 1/10th the bandwidth
that is required for the JSON format used by query.

This method has been available in beta for a few months, but is now available for general use, and as part of this
release is now supported when querying using notebooks without access to feature schemas.

### September 26, 2023

### Improve scheduled resolver runs list

The list of scheduled resolvers now shows which resolvers are actually scheduled to
run in the current environment, based on the environment argument to @online and @offline.

Scheduled Resolvers List:

Resolvers that are annotated with an environment other than the current environment are labeled with the
environment in which they are configured to run.

### August 23, 2023

### Improved chalk query output

The chalk query command now has
improved output for errors. Previously, errors
were displayed in a table, which meant that
stacktraces were truncated:

```
> chalk query --in email.normalized=nice@chalk.ai --out email

Errors

Code             Feature  Resolver                        Message
─────────────────────────────────────────────────────────────────────────────
RESOLVER_FAILED           src.resolvers.get_fraud_tags    KeyError: 'tags'
```

Now, errors are displayed in a more readable format,
and stacktraces are not truncated:

```
> chalk query --in email.normalized=nice@chalk.ai --out email

Errors

Resolver Failed src.resolvers.get_fraud_tags

KeyError: 'tags'
  File "src/resolvers.py", line 30, in get_fraud_tags
      return parsed["tags"]

KeyError('tags')
```

### August 19, 2023

### Query plan trace viewer

The query plan viewer now includes a flame graph visualization of the query plan's execution, called the Trace View. Precise trace
data is stored for every offline query by default and for online queries when the query is made with the --explain flag.

Trace View:

### August 11, 2023

### Override now in online query

- Support now= for .query, --now, etc.

### Query plan viewer improvements

- Redesigned query plan viewer
- Support viewing execution time per operator
- Support viewing data processing metrics per operator
- Query plans saved for all queries by default

### No-input online and offline query improvements

- offline_query now supports running downstream resolvers when no input is provided. Query primary keys will be sampled or computed, depending on the value of recompute_features.
- online_query now support running a query without any input. Query primary keys will be computed using an appropriate no-argument resolver that returns a DataFrame[...]

### Misc

- --local for chalk query, combines chalk apply --branch and chalk query --branch
- The progress indicator in the chalk command line tool is no longer an off-brand magenta.

### August 5, 2023

### Chalk Python SDK Improvements

Added: .to_polars(), to_pandas(), and .to_pyarrow() accept prefixed: bool as an argument. prefixed=True is the
default behavior, and will prefix all column names with the feature namespace. prefixed=False will not prefix column names.

```
DataFrame({User.name: ["Andy"]}).to_polars(prefixed=False)
# output:
# polars DataFrame with `name` as the sole column.

DataFrame({User.name: ["Andy"]}).to_polars(prefixed=True)
# output:
# polars DataFrame with `user.name` as the sole column.
```

Added: include_meta on ChalkClient.query(...), which includes .meta on the response object. This metadata object
includes useful information about the query execution, at the cost of increased network payload size and a small
increase in latency.

### July 25, 2023

### Freezing time in unit tests

Chalk now supports freezing time in unit tests. This is useful for testing time-dependent resolvers.

```
from datetime import timezone, datetime
from chalk.features import DataFrame, after
from chalk.features.filter import freeze_time

df = DataFrame([...])
with freeze_time(at=datetime(2020, 2, 3, tzinfo=timezone.utc)):
    df[after(days_ago=1)] # Get items after february 2nd
```

freeze_time also works with resolvers that declare specific time bounds for their aggregation inputs:

```
@online
def get_num_transactions(txs: Card.transactions[before(days_ago=1)]) -> Card.num_txs:
  return len(txs)

with freeze_time(at=datetime(2020, 9, 14)):
    num_txs = get_num_transactions(txs) # num transactions before september 13th
```

### July 11, 2023

### Explicitly time-dependent resolvers

Chalk now supports resolvers that are explicitly time-dependent. This is useful for performing backfills which
compute values that depend on values that are semantically similar to datetime.now().

You can express time-dependency by declaring a dependency on a special feature called Now:

```
@online
def get_age_in_years(birthday: User.birthday, now: Now) -> User.age_in_years:
    return (now - birthday).years
```

In online query, (i.e. with ChalkClient().query), Now is datetime.now(). In offline query contexts,
now will be set to the appropriate input_time value for the calculation. This allows you to backfill
a feature for a single entity at many different historical time points:

```
ChalkClient().offline_query(input={User.id: [1,1,1]}, output=[User.age_in_years], input_times=[
    datetime.now() - timedelta(days_ago=100),
    datetime.now() - timedelta(days_ago=50),
    datetime.now() - timedelta(days_ago=0),
])
...
```

Now can be used in batch resolvers as well:

```
@online
def batch_get_age_in_years(df: DataFrame[User.id, User.birthday, Now]) -> DataFrame[User.id, User.age_in_years]:
    ...
```

### June 21, 2023

### Testing your SQL File Resolvers

SQL file resolvers are Chalk's preferred method of resolving
features with SQL queries.
Now, you can get your SQL file resolvers in Python by the name of the SQL file resolver.
For example, if you have the following SQL file resolver:

```
-- source: postgres
-- cron: 1h
-- resolves: Person
select id, name, email, building_id from table where id=${person.id}
```

you can test out your resolver with the following code.

```
from chalk import get_resolver

resolver = get_resolver('person') # get_resolver('person.chalk.sql') will also work
result = resolver('my_id')
```

### June 15, 2023

### Metrics Export Updates

Now, Chalk supports exporting metrics about "named query" execution. These metrics (count, latency) join
similar metrics about feature and resolver execution. Contact your Chalk Support representative to configure
metrics export if you would like to view metrics about Chalk system execution in your existing metrics dashboards.

Additional updates:

- synthetic cache resolvers are now excluded
- query_name is a tag on many metrics

### June 14, 2023

### Branch deployment performance

Chalk Branch Deployments provide an excellent experience for quick iteration cycles on new features and resolvers.
Now, Chalk Branch Deployments automatically use a pool of "standby" workers, so there is less delay before
queries can be served against a new deployment. This reduces the time it takes to run query or offline query against
a new deployment from ~10-15 seconds to ~1-3 seconds. This impacts customers with more complex feature graphs the most.

### June 13, 2023

### Expanded support for logical keying in streaming contexts

Stream resolvers support a keys= parameter. This parameter allows you to re-key a stream by a property of the message,
rather than relaying on the protocol layer key. This is appropriate if a stream is keyed randomly, or by an entity key like "user",
but you want to aggregate along a different axis, e.g. "organization".

Now, keys= supports passing a "dotted string" (e.g. foo.bar) to indicate that Chalk should use a sub-field of your
message model. Previously, only root-level fields of the model were supported.

### DataFrame unit tests

If you specify projections or filters in
DataFrame arguments of resolvers, Chalk will
automatically project out columns and filter rows in
the input data.

Below, we test a resolver that filters rooms in
a house to only the bedrooms:

```
@features
class Room:
    id: str
    home_id: "Home.id"
    name: str

@features
class Home:
    id: str
    rooms: DataFrame[Room]
    num_bedrooms: int

@online
def get_num_bedrooms(
    rooms: Home.rooms[Room.name == 'bedroom']
) -> Home.num_bedrooms:
    return len(rooms)
```

Now, we may want to write a unit test
for this resolver.

```
def test_get_num_rooms():
    # Rooms is automatically converted to a `DataFrame`
    rooms = [
        Room(id=1, name="bedroom"),
        Room(id=2, name="kitchen"),
        Room(id=3, name="bedroom"),
    ]

    # The kitchen room is filtered out
    assert get_num_bedrooms(rooms) == 2

    # `get_num_bedrooms` also works with a `DataFrame`
    assert get_num_bedrooms(DataFrame(rooms)) == 2
```

While we could have written this test before, we would
have had to manually filter the input data to only
include bedrooms.
Also note that Chalk will automatically convert our argument
to a DataFrame if it is not already one.

### June 12, 2023

### Query Run Page

Chalk's dashboard shows aggregated logs and metrics about the execution of queries and resolvers. Now, it can also
show detailed metrics for a single query. This is useful for debugging and performance tuning.

You can access this page from the "runs" tab on an individual named query page, or from the "all query runs" link
on the "queries" page.

You can search the list of previously executed queries by date range, or by "query id". The query id is returned
in the "online query" API response object.

### May 15, 2023

### BigTable Online Storage

Chalk now supports BigTable as an online-storage implementation. BigTable is appropriate for customers with large
working sets of online features, as is common with recommendation systems. We have successfully configured
BigTable to serve 700,000 feature vectors per second at ~30ms p90 e2e latency.

### May 10, 2023

### Enhancements to Offline Query

The Offline Query has been enhanced with a new recompute_features parameter. Users can control which features are sampled from the offline store, and which features are recomputed.

- The default value False will maintain current behavior, returning only samples from the offline store.
- True will ignore the offline store, and execute @online and @offline resolvers to produce the requested output.
- If, instead, the user passes in a list of features to recompute_features, those features will be recomputed by running @online and @offline resolvers, and all other feature values - including those needed to recompute the requested features - will be sampled from the offline store.

### Recompute Dataset

The 'recompute' capability is also exposed on Dataset. When passed a list of features to recompute, a new Dataset Revision will be generated, and the existing dataset will be used as inputs to recompute the requested features.

### Developing in Jupyter

Chalk has introduced a new workflow when working with branches, allowing full iterations to take place directly in any IPython notebook. When a user creates a Chalk Client with a branch in a notebook, subsequent features and resolvers in the notebook will be deployed to that branch.
When combined with Recompute Dataset and the enhancements to Offline Query, users have a new development loop available for feature exploration and development:

- Take advantage af existing data in chalk
- Explore that data using familiar tools in a notebook
- Enrich the data by developing new features and resolvers
- Immediately view the results of adjusting features in the dataset
- When exploration is complete, features and resolvers can be directly added back to the Chalk project

### May 5, 2023

### View Deployment Source Code

Deployments now offer the ability to view their source code. By clicking the "View Source" button on the Deployment Detail page, users can view all files included in the deployed code.

### April 21, 2023

### Improved Deployment Utilities

Users can now "redeploy" any historical deployment with a UI button on the deployment details page. This enables useful workflows including rollbacks.
The "download source" button downloads a tarball containing the deployed source to your local machine.
Deploy UI Enhancements

### April 18, 2023

### Resolver error messages for incorrect types include primary keys

When writing resolvers, incorrect typing can be a difficult to track.
Now, if a resolver instantiates a feature of an incorrect type, the resolver error message
will include the primary key value(s) of the query itself.

### April 11, 2023

### Online query improvements

The Online Query API can now be used to query DataFrame-typed features. For instance, you can query all of a user's
transaction level features in a single query:

```
chalk query --in user.id --out user.transactions

{
  "columns": ["transaction.id", "transaction.user_id", ...],
  "values": [[1, 2, 3, ...], ["user_1", "user_2", "user_3", ...]
}
```

More functionality will be added to Online and Offline query APIs to support more advanced query patterns.

### April 6, 2023

### Branch deployments

When deploying with chalk apply a new flag --branch <branch_name> has been introduced which creates a branch deployment.
Users can interact with their branch deployment using a consistent name by passing the branch name to query, upload_features, etc.
Chalk clients can also be scoped to a branch by passing the branch in the constructor.
Branch deployments are many times faster than other flavors of chalk apply, frequently taking only a few seconds from beginning to end.
Branch deployments replace preview deploys, which have been deprecated.

### March 31, 2023

### Speed improvements for deployments

Deployments via chalk apply are now up to 50% faster in certain cases. If your project's PIP dependencies haven't changed, new deployments will build & become active significantly faster than before.

Deploy Time Comparison:

### March 17, 2023

### Offline TTL

Introduces a new "offline_ttl" property to features decorator . Now you can control for how long data is valid in the offline_store. Any feature older than the ttl value will not be returned in an offline query.

```
@features
class MaxOfflineTTLFeatures:
    id: int
    ts: datetime = feature_time()

    no_offline_ttl_feature: int = feature(offline_ttl=timedelta(0))
    one_day_offline_ttl_feature: int = feature(offline_ttl=timedelta(days=1))
    infinite_ttl_feature: int
```

### Strict Feature Validation

Adds the strict property to features decorator, indicating that any failed validation will throw an error. Invalid features will never be written to the online or offline store is strict is True. Also introduces the validations array to allow differentiated strict and soft validations on the same feature.

```
@features
class ClassWithValidations:
    id: int
    name: int = feature(max=100, min=0, strict=True)
    feature_with_two_validations: int = feature(
        validations=[
            Validation(min=70, max=100),
            Validation(min=0, max=100, strict=True),
        ]
    )
```

### March 7, 2023

### Datasets in Offline Query

The Dataset class is now live!
Using the new ChalkClient.offline_query method,
we can inspect important metadata about the query and
retrieve its output data in a variety of ways.

Simply attach a dataset_name to the query to persist the results.

```
from chalk.client import ChalkClient, Dataset
uids = [1, 2, 3, 4]
at = datetime.now()
dataset: Dataset = ChalkClient().offline_query(
     input={
         User.id: uids,
     },
     input_times=[at] * len(uids),
     output=[
         User.id,
         User.fullname,
         User.email,
         User.name_email_match_score,
     ],
     dataset_name='my_dataset'
)
pandas_df: pd.DataFrame = dataset.data_as_pandas
```

Check out the documentation  here.

### February 28, 2023

### Deployment Build Logs

Chalk now provides access to build and boot logs through the Deployments page in the dashboard.

Build Logs

### February 16, 2023

### Resolver timeouts

Computing features associated with third-party services can be unpredictably slow.
Chalk helps you manage such uncertainty by specifying a resolver timeout duration.

Now you can set timeouts for resolvers!

```
@online(timeout="200ms")
def resolve_australian_credit_score(driver_id: User.driver_id_aus) -> User.credit_score_aus:
    return experian_client.get_score(driver_id)
```

### January 26, 2023

### SQL File Resolvers

SQL-integrated resolvers can be completely written in SQL files: no Python required!
If you have a SQL source like as follows:

```
pg = PostgreSQLSource(name='PG')
```

You can define a resolver in a .chalk.sql file, with comments that detail important
metadata. Chalk will process it upon chalk apply as it would any other Python resolver.

```
-- type: online
-- resolves: user
-- source: PG
-- count: 1
select email, full_name from user_table where id=${user.id}
```

Check out the documentation  here.

### January 12, 2023

### Improved Logging

Logging on your dashboard has been improved. You can now scroll through more logs, and the formatting is cleaner and easier to use.
This view is available for resolvers and resolver runs.

Logs Viewer

### January 9, 2023

### Pretty Print Online Query Results

Online Query Response objects now support pretty-print in any iPython environment.

Pretty Print Query Response

### January 8, 2023

### Linux docker containers on M1 Macs

chalkpy has always supported running in docker images using M1's native arm64 architecture, and now
chalkpy==1.12.0 supports most functionality on M1 Macs when run with AMD64 (64 bit Linux) architecture docker images.
This is helpful when testing images built for Linux servers that include chalkpy.

### January 6, 2023

### Docs Search

Chalk has lots of documentation, and finding content is now difficult.

We've added docs search!

Documentation search

Try it out by typing cmd-K, or clicking the search button at the top of the
table of contents.

### September 27, 2022

### Tags & Owners as Comments

This update makes several improvements to feature discovery.

Tags and owners are now parsed from the comments preceding
the feature definition.

```
@features
class RocketShip:
    # :tags: **team:identity**, **priority:high**
    # :owner: **katherine.johnson@nasa.gov**
    velocity: float
    ...
```

Prior to this update, owners and tags needed to be set in the feature(...) function:

```
@features
class RocketShip:
    velocity: float = feature(
        tags=["**team:identity**", "**priority:high**"],
        owner="**katherine.johnson@nasa.gov**"
    )
    ...
```

Feel free to choose either mechanism!

### July 28, 2022

### Auto Id Features

It's natural to name the primary feature of a feature class
id. So why do you always have to specify it?
Until now, you needed to write:

```
@features
class User:
    id: str = feature(primary=True)
    ...
```

Now you don't have to! If you have a feature class that does
not have a feature with the primary field set, but has a feature
called id, it will be assigned primary automatically:

```
@features
class User:
    id: str
    ...
```

The functionality from before sticks around:
if you use a field as a primary key with a name other than
id, you can keep using it as your primary feature:

```
@features
class User:
    user_id: str = feature(primary=True)
    # Not really the primary key!
    id: str
```

### July 25, 2022

### DataFrame Expressions

The Chalk DataFrame now supports boolean expressions!
The Chalk team has worked hard to let you express your
DataFrame transformations in natural, idiomatic Python:

```
DataFrame[
  User.first_name == "Eleanor" or (
    User.email == "eleanor@whitehouse.gov" and
    User.email_status not in {"deactivated", "unverified"}
  ) and User.birthdate is not None
]
```

Python experts will note that or, and, is, is not, not in, and not
aren't overload-able.
So how did we do this?
The answer is AST parsing! A more detailed blog post to follow.

### July 22, 2022

### Descriptions as Comments

This update makes several improvements to feature discovery.

Descriptions are now parsed from the comments preceding
the feature definition. For example, we can document the feature
User.fraud_score with a comment above the attribute definition:

```
@features
class User:
    # **0 to 100 score indicating an identity match.**
    # **Low scores indicate safer users**
    fraud_score: float
    ...
```

Prior to this update, descriptions needed to be set in the feature(...) function:

```
@features
class User:
    fraud_score: float = feature(description="""
           **0 to 100 score indicating an identity match.**
           **Low scores indicate safer users**
        """)
    ...
```

The description passed to feature(...) takes precedence over the
implicit comment description.

### Namespace Metadata

You can now set attributes for all features in a namespace!

Here, we assign the tag group:risk and the owner ravi@chalk.ai
to all features on the feature class.
Owners specified at the feature level take precedence
(so the owner of User.email is the default ravi@chalk.ai whereas the
owner of User.flaky_api_result is devops@chalk.ai).
Tags aggregate, so email has the tags pii and group:risk.

```
@features(tags="group:risk", owner="ravi@chalk.ai")
class User:
    email: str = feature(tags="pii")
    flaky_api_result: str = feature(owner="devops@chalk.ai")
```

### July 14, 2022

### Self-Serve Slack Integration

You can configure Chalk to post message to your Slack workspace!
You can find the Slack integration tab in the settings page of your dashboard.

Slack integration

Slack can be used as an alert channel or for build notifications.

### July 13, 2022

### Python 3.8 Support

Chalk's pip package now supports Python 3.8!
With this change, you can use the Chalk package to run
online and offline queries in a Python environment
with version >= 3.8.
Note that your features will still be computed on a runtime
with Python version 3.10.

### July 8, 2022

### Named Integrations

Chalk's injects environment variables to support data integrations.
But what happens when you have two data sources of the same kind?
Historically, our recommendation was to create one set of environment
variables through an official data source integration,
and one set of prefixed environment variables yourself using
the generic environment variable support.

With the release of named integrations, you can connect to as many
of the same data source as you need!
Provide a name at the time of configuring your data source,
and reference it in the code directly.
Named integrations inject environment variables with the standard names
prefixed by the integration name (ie. RISK_PGPORT).
The first integration of a given kind will also create the un-prefixed environment
variable (ie. both PGPORT and RISK_PGPORT).

### June 29, 2022

### SOC 2 Report

Chalk is excited to announce the availability of our SOC 2 Type 1 report from Prescient Assurance. Chalk
has instituted rigorous controls to ensure the security of customer data and earn the trust of our customers,
but we're always looking for more ways to improve our security posture, and to communicate these steps to our customers.
This report is one step along our ongoing path of trust and security.

If you're interested in reviewing this report, please contact support@chalk.ai to request a copy.

### June 3, 2022

### Pandas Integration

You can now convert Chalk's DataFrame to a pandas.DataFrame and back!
Use the methods chalk_df.to_pandas() and .from_pandas(pandas_df).

### Migration Sampling

The 1.4.1 release of the CLI added a parameter --sample to chalk migrate.
This flag allows migrations to be run targeting specific sample sets.

### Feature/Resolver Health

Added spark lines to the feature and resolver tables which show a quick summary of request counts over the past 24 hours.
Added status to feature and resolver tables which show any failing checks related to a feature or resolver.

# Offline Queries
source: https://docs.chalk.ai/docs/training-client

## Fetch offline feature values.

Offline queries pull data from the offline store or calculate features through
resolvers that are marked as offline.

Offline queries can also execute online resolvers if no offline resolver is available for a
requested feature.

In an offline query you can request features for multiple entities at distinct time points.
By default, an offline query returns a row for each primary key containing the most recent
computed value for each requested output feature. The main use case for offline queries is
creating datasets.

Chalk supports a number of clients that can run offline queries. In this section, our examples
focus on our python client, which integrates nicely with jupyter notebooks.

### Making Offline Queries

As mentioned earlier, offline queries can be made through one of Chalk's API clients.

```
from chalk.client import ChalkClient
from datetime import datetime

client = ChalkClient()
client.offline_query(
  input={'user.id': [1,2,3,4]},         # Input
  output=['user.name'],                 # Output
  # tags=['test'],                      # Environment
  # branch='branch',
  # recompute_features=True,            # Run Resolvers
  # run_asynchronously=True,            # Run Configuration
  # max_samples = 10,
  # lower_bound=datetime(2024, 10, 12), # Bounds
  # upper_bound=datetime(2024, 10, 20),
)
```

In the Python client, offline queries return Chalk Datasets, which we cover, in detail, in the
next section. However, at a high level, Chalk Datasets are flexible wrappers
around the results of your offline query that can be converted to pandas or polars—this makes them
easy to use for downstream ML tasks.

### Input

As input, offline_query takes a
chalk.DataFrame or pandas.DataFrame
with one column for each known feature in the input.
The primary key feature must be included among the inputs.

Alternatively, instead of a DataFrame, users can pass a mapping from features to a list of values for each feature.

```
input={
    User.id: ['id1', 'id2'],
    User.age: [23, 40]
}
```

### Input Times

Timestamps can be also be passed in the input_times argument instead.

```
input={
    User.id: ['id1', 'id1'],
}
input_times=[datetime.now() - timedelta(days=1), datetime.now() - timedelta(days=2)]
```

### Output

This argument describes a list of features to sample.

```
output=[
    User.returned_transactions_last_60,
    User.user_account_name_match_score,
    User.socure_score,
    User.identity.has_verified_phone,
    User.identity.is_voip_phone,
    User.identity.account_age_days,
    User.identity.email_age,
]
```

### Recompute Features

Users can request that certain features be recomputed by resolvers
at query time instead of sampled from the offline store.
For more information, read here.

### Time Bounds

In some cases, users may not have a list of primary keys to sample with,
and instead would like to see results within a period of time.
The user can then leave the inputs argument empty and supply a
lower bound and an
upper bound along with the requested output features.

```
dataset: Dataset = ChalkClient().offline_query(
     output=[
         User.id,
         User.fullname,
         User.email,
         User.name_email_match_score,
     ],
     lower_bound=datetime.now() - timedelta(days=7),
     upper_bound=datetime.now(),
)
```

### Environment

The user can specify
tags,
environment,
or branch
as parameters to offline_query in the same fashion
as online query.

### Training Client

# Snowflake Offline Store Overview
source: https://docs.chalk.ai/docs/snowflake-offline-store

## Understanding Snowflake offline store architecture and multi-environment deployments.

Chalk supports Snowflake as an offline store for persisting feature values, enabling historical data access
for training set generation and batch inference. This guide explains the architecture, component hierarchy,
and how to plan your Snowflake offline store setup—especially for deployments with multiple environments.

### Architecture Overview

When using Snowflake as your offline store, components are organized at two levels: cluster-level (shared)
and environment-level (per environment). Understanding this hierarchy is essential for planning your setup.

Snowflake Offline Store Architecture

Chalk uses fully-qualified names (FQNs) to route data through the shared storage integration,
ensuring data isolation between environments without contamination.

### Component Sharing Rules

### Must Be Unique Per Environment

| Component | Notes |
|-----------|-------|
| Schema | Each environment must have its own schema (e.g., OFFLINE_STORE_DEV, OFFLINE_STORE_PROD) |
| Role | Recommended: separate roles for security isolation |
| User | Recommended: separate users with separate credentials |

### Must Be Shared (Cluster-Level)

| Component | Notes |
|-----------|-------|
| Storage Integration | One per cluster—all environments share it |
| Storage Bucket | One per cluster (S3 or GCS) |
| IAM Policy/Role | Tied to storage integration |

### Your Choice: Share or Separate

| Component | Shared | Separated | When to Separate |
|-----------|--------|-----------|------------------|
| Database | CHALK for all envs | CHALK_DEV, CHALK_PROD | Regulatory requirements, separate billing |
| Warehouse | CHALK_WAREHOUSE for all | CHALK_WH_DEV, CHALK_WH_PROD | Independent scaling, separate cost tracking |
| Snowflake Account | One account for cluster | Separate accounts | Cannot have multiple per cluster |

### Key Takeaways

- Schema is the critical isolation boundary—each environment must have its own unique schema
- Storage integration is cluster-wide—you create it once and all environments use it
- Database and Warehouse are flexible—share them for simplicity, or separate them for independent scaling/billing
- Chalk handles routing—data flows through the shared storage integration but is isolated by environment using fully-qualified paths

### Multi-Environment Deployment Options

When setting up multiple Chalk environments (e.g., dev, staging, production), you have two approaches:

### Option 1: Full Separation (Recommended for Strict Isolation)

Create completely separate resources for each environment:

| Resource | Dev | Stage | Prod |
|----------|-----|-------|------|
| Database | CHALK_DEV | CHALK_STAGE | CHALK_PROD |
| Schema | OFFLINE_STORE | OFFLINE_STORE | OFFLINE_STORE |
| Role | CHALK_ROLE_DEV | CHALK_ROLE_STAGE | CHALK_ROLE_PROD |
| User | CHALK_USER_DEV | CHALK_USER_STAGE | CHALK_USER_PROD |
| Warehouse | CHALK_WH_DEV | CHALK_WH_STAGE | CHALK_WH_PROD |

Benefits:

- Maximum isolation between environments
- Independent resource management and billing
- Easier audit trails

### Option 2: Minimal Separation (Simpler Setup)

Share what you can, separate only what you must:

| Resource | Dev | Stage | Prod |
|----------|-----|-------|------|
| Database | CHALK (shared) | CHALK (shared) | CHALK (shared) |
| Schema | OFFLINE_STORE_DEV | OFFLINE_STORE_STAGE | OFFLINE_STORE_PROD |
| Role | CHALK_ROLE_DEV | CHALK_ROLE_STAGE | CHALK_ROLE_PROD |
| User | CHALK_USER_DEV | CHALK_USER_STAGE | CHALK_USER_PROD |
| Warehouse | CHALK_WAREHOUSE (shared) | CHALK_WAREHOUSE (shared) | CHALK_WAREHOUSE (shared) |

Benefits:

- Fewer resources to manage
- Simpler credential management
- Lower administrative overhead

### Recommendation

Use Option 2 (Minimal Separation) for most deployments. The schema-level isolation provides
sufficient separation for feature data, and Chalk's FQN-based routing ensures data integrity.

Use Option 1 (Full Separation) when:

- Regulatory requirements mandate complete resource isolation
- Different environments need different warehouse sizes or configurations
- You need separate billing or resource quotas per environment

### Setup Checklist

Before starting your Snowflake offline store setup, gather the following:

### From Your Cloud Environment

- [ ] AWS Account ID (where Chalk is deployed) or GCP Project ID
- [ ] S3 bucket name or GCS bucket name (typically chalk-{organization}-data-bucket)

### From Snowflake

- [ ] Snowflake account name (SELECT CURRENT_ACCOUNT_NAME();)
- [ ] Snowflake organization name (SELECT CURRENT_ORGANIZATION_NAME();)

### Permissions Required

- [ ] AWS: Permissions to create IAM policies, roles, and update trust relationships
- [ ] GCP: Permissions to create IAM custom roles and assign roles to service accounts
- [ ] Snowflake: ACCOUNTADMIN role or equivalent with CREATE DATABASE, CREATE WAREHOUSE, CREATE INTEGRATION, and SECURITYADMIN privileges

### Cloud-Specific Setup Guides

Choose the guide that matches your cloud provider:

- Snowflake Setup for AWS — S3 storage integration with IAM roles
- Snowflake Setup for GCP — GCS storage integration with service accounts

### What to Share with Chalk

After completing the setup, securely share the following with Chalk:

### Credentials

Share the following via GPG encryption:

- RSA private key for Snowflake authentication
- Snowflake user name

### Configuration Details

- Snowflake account name and organization name
- Database name, schema name(s), warehouse name
- Role name(s)
- Storage integration name
- AWS Account ID or GCP Project ID
- S3/GCS bucket name

For multi-environment setups, provide these details for each environment, clearly labeled
(e.g., "Dev Environment", "Stage Environment", "Prod Environment").

# GPUs and Resource Hints
source: https://docs.chalk.ai/docs/resource-hints

## Schedule workloads on differentiated hardware & execution pools

Different workloads have different requirements. Some workloads are compute-intensive, while others are memory-intensive.
Some workloads require GPUs, some perform blocking IO, and some are purely CPU-bound.and

Chalk allows you to specify the hardware and execution pool requirements for your queries,
so that they can be scheduled on the most appropriate resources.

### Executing on Hardware with GPUs

Chalk allows you to execute specific resolvers on hardware with GPUs. To do this, you can use the "gpu" resource
hint in your resolver definition. This will ensure that the resolver is scheduled on a machine with a GPU.

```
import torch
from chalk.features import online

@online(resource_hint="gpu")
def my_gpu_resolver(Transaction.memo) -> Transaction.cleaned_memo:
    """
    Run a torch model to process data using a GPU.
    """
    ...
```

Then, specify the Resource Group that has the GPU resources available:

```
CHALK_GPU_RESOURCE_GROUP_NAME=gpu-resolvers
```

This resource group should:

- have a UDF Invoker Service deployed
- this service should have a node selector that matches nodes with GPUs, e.g.:

```
cloud.google.com/machine-family: a2-highgpu
```

Chalk's query planner will execute the primary query plan on your Query Server service, and will transmit
row data to the GPU resolver service for processing in compressed Arrow format. Response data will be
transmitted back to the Query Server service, which will then return the final result to the client.

### CPU vs IO Pools

Chalk allows you to specify whether a resolver is CPU-bound or IO-bound. This is useful for scheduling
resolvers on the most appropriate resources. To do this, you can use the "cpu" or "io" resource hints in your resolver definition.

```
from chalk.features import online

@online(resource_hint="cpu")
def my_cpu_bound_resolver(Transaction.memo) -> Transaction.cleaned_memo:
    """
    Run a CPU-bound operation.
    """
    fibbonaci = [0, 1]
    for i in range(2, 100):
        fibbonaci.append(fibbonaci[i - 1] + fibbonaci[i - 2])
    return fibbonaci

@online(resource_hint="io")
def my_io_bound_resolver(Transaction.memo) -> Transaction.cleaned_memo:
    """
    Run an IO-bound operation.
    """
    return requests.get("https://example.com/api/data").json()
```

Chalk uses CPU-count thread pools for CPU-bound resolvers, because additional threads do not help with CPU-bound workloads.
Chalk uses variable sized thread pools for IO-bound resolvers, because additional threads can help with IO-bound workloads.

Note: if you use async resolvers, Chalk will execute them on an asyncio event loop that is shared across all resolvers.
This means that you should not use blocking IO operations in async resolvers, as they will block the event loop and
prevent other resolvers from executing.

# Error Handling
source: https://docs.chalk.ai/docs/query-errors

## Run resolvers in the presence of upstream failures.

Chalk returns an error channel in addition the requested feature values.

There are several types of errors one could expect:

### Error categories

### Request error

Request errors are raised before execution of your resolver code.
They may occur due to invalid feature names in the
input or a request that cannot be satisfied by the resolvers you
have defined.

### Field error

Field errors are raised while running a feature resolver
for a particular field.
For this type of error, you'll find a feature and resolver
attribute in the error type.

When a feature resolver crashes, you will receive null value
in the response.
To differentiate from a resolver returning a null value and
a failure in the resolver, you need to check the error schema.

### Network error

Network errors are thrown outside your resolvers.
For example, your request was unauthenticated,
connection failed, or an error occurred within Chalk.

### Error schema

The online query interface for resolvers returns the following schema:

### Response Schema

The outputs features and any query metadata (discussed in detail at
Query Basics.)

Errors encountered while running the resolvers. Each element in the list is a
ChalkError. If no errors were encountered, this field is empty.

### ChalkError

The type of error, matching one of the error codes.

The category of the error, given in the type field for the
error codes. This will be one of
"REQUEST", "NETWORK", and
"FIELD".

A readable description of the error message.

The exception that caused the failure, if applicable.

The name of the class of the exception.

The message taken from the exception.

The stacktrace produced by the code.

The fully qualified name of the failing feature, eg.
user.identity.has_voip_phone.

The fully qualified name of the failing resolver, eg.
my.project.get_fraud_score.

### Error code

The query contained features that do not exist.

A resolver was required as part of running the dependency graph that could not be found.

The query is invalid. All supplied features need to be rooted in the same top-level entity.

A feature value did not match the expected schema (eg. incompatible type "int"; expected "str")

The resolver for a feature errored.

The resolver for a feature timed out.

A crash in a resolver that was to produce an input for the resolver crashed, and so the resolver
could not run crashed, and so the resolver could not run.

The request was submitted with an invalid authentication header.

The request has credentials that do not provide the required authorization to execute an operation.

An unspecified error occurred.

# Query Scheduling
source: https://docs.chalk.ai/docs/query-cron

## Create and ingest datasets on a schedule

Once you have defined features and resolvers in Chalk, you can schedule queries to run at regular intervals. This is
useful for ingesting data from external sources, or for precomputing features that are expensive to compute in real-time.

### Scheduling a Query

Query scheduling looks very similar to offline_query's usage. Imagine that we want to precompute the average
temperature for each city in the world every day. First, we define a feature class for the temperature readings, and a
feature class for the cities:

```
@features
class TemperatureReading:
    id: int
    city: City.id
    temperature: float
    ts: datetime

@features(max_staleness="1d", etl_offline_to_online=True)
class City:
    id: str
    name: str
    average_temperature: float

    temperature_readings: DataFrame[TemperatureReading]
```

Then, we define a resolver that fetches the temperature readings for each city:

```
-- resolves: TemperatureReading
-- source: snowflake
SELECT
    id,
    city,
    temperature,
    ts
FROM
    temperature_readings
```

Then, we define a resolver to compute the average temperature for each city:

```
@offline
def compute_average_temperature(temps: City.temperature_readings[TemperatureReading.temperature, after(days_ago=1)]) -> City.average_temperature:
    return temps.mean()
```

Finally, we schedule the query to run every day at midnight:

```
ScheduledQuery(
    name="average_temperature",
    outputs=[City.average_temperature],
    schedule="0 0 * * *",
    store_online=True
)
```

Each day, this query will execute and cache the average temperature for each city in the world. This data will be
available for real-time queries:

```
client.query(input={City.id: 713}, output=[City.average_temperature])

# 58
```

# Sharing sensitive data with Chalk
source: https://docs.chalk.ai/docs/public-key

### Overview

If you need to send sensitive material to Chalk, you can use
asymmetric encryption
to transmit your data securely. Only Chalk will be able to view the data
that you encrypt with Chalk's public key.

### Using GnuPG

To begin, ensure that you've installed GnuPG (Mac, Ubuntu). GnuPG provides the gpg utility, which you will use to encrypt your data using Chalk's public key.

Next, download and import Chalk's public key:

```
curl -s https://docs.chalk.ai/chalk-public-key.key > chalk-public-key.key
gpg --import chalk-public-key.key
```

Next, encrypt your plaintext using Chalk's public key:

```
cat <plaintext_file> | gpg -e -r Chalk > ciphertext.gpg
```

Now you can transmit ciphertext.gpg via email or Slack to Chalk. Only
Chalk's support staff will be able to decrypt and view the contents of ciphertext.gpg.

# OpenAI
source: https://docs.chalk.ai/docs/openai

## Integrate with OpenAI for embedding models.

Chalk supports OpenAI as an embeddings provider.

### Adding OpenAI

On the dashboard, you can provide your OpenAI API key.

# Online Store Survey
source: https://docs.chalk.ai/docs/online-store-survey

## Use SQL Explorer to analyze online store key distribution and memory utilization

Chalk SQL provides a virtual table that lets you survey the contents of your Redis or Valkey online store.
This is useful for capacity planning, identifying deprecated features that haven't been cleaned up,
and understanding which feature namespaces consume the most memory.

### Prerequisites

To run online store survey queries, you need:

- A Redis or Valkey online store configured and operational
- Access to the SQL Explorer in the Chalk dashboard
- Queries can run in either synchronous or asynchronous mode—the online store schema is available in both execution paths

For background on these tools, see:

- SQL Explorer — the query interface
- Online and Offline Stores — store configuration options
- Chalk Catalog Components — full schema reference

### The chalk.online_store.keys table

The chalk.online_store.keys view exposes metadata about every key in your Redis or Valkey online store.
The table has the following schema:

- key (binary) — The raw key stored in the online store.
- key_type (string) — The type of key: Scalar, HasMany, TimeSeries, etc.
- cache_prefix (string) — The configured cache prefix for this key.
- fqn (string) — The fully qualified feature name (e.g. user.fraud_score).
- memory_usage (uint64) — Bytes consumed in the store by this key.
- ttl_seconds (uint64) — Time-to-live remaining in seconds.

### Safety warning

Querying chalk.online_store.keys without a LIMIT performs a full
Redis/Valkey SCAN, which can significantly impact production performance. Always use a
LIMIT clause in the inner subquery to cap the number of keys scanned.
Because keys are proportionally distributed across the scan space, a limited sample provides
a representative picture of your online store's contents.

Redis/Valkey are key-value stores and as such do not support indexing on different
"columns" out-of-the-box. A "select-from-where" query with a filter will still scan the
online store, yielding only rows that match the filter. This means that a filter that
doesn't match any keys might perform a full scan -- e.g. SELECT * FROM
	"chalk.online_store.keys" WHERE fqn='nonexistent_feature'. Support for filtering by
primary key (i.e. performing a direct redis GET instead of a SCAN for a certain id) is
not currently supported for this SQL interface but is coming soon!

### Survey queries

In the SQL Explorer settings sidebar, enable Persist Results to save query output to cloud
storage. This makes results available in the dashboard for later review. Asynchronous queries always persist
results automatically, but for synchronous queries you must enable this toggle explicitly. This is recommended
for larger survey queries where you want to revisit or share results.

### Sampling keys

Start with a small sample to see what's in your online store:

```
SELECT * FROM chalk.online_store.keys LIMIT 100;
```

### Key distribution and memory by feature namespace

Aggregate over a sample to see how keys and memory are distributed across feature namespaces:

```
SELECT key_type, fqn, count(*), sum(memory_usage)
FROM (SELECT * FROM chalk.online_store.keys LIMIT 20000)
GROUP BY key_type, fqn;
```

### Ordered by memory usage

Find the largest consumers by sorting on total memory:

```
SELECT key_type, fqn, count(*), sum(memory_usage)
FROM (SELECT * FROM chalk.online_store.keys LIMIT 100000)
GROUP BY key_type, fqn
ORDER BY sum(memory_usage) DESC;
```

### Checking for a specific feature namespace

Verify whether a particular namespace still has keys in the store — useful after removing a feature class:

```
SELECT * FROM (
  SELECT * FROM chalk.online_store.keys LIMIT 100
) WHERE fqn = 'my_feature_namespace';
```

### Interpreting results

- Representative sampling — Because keys are proportionally distributed across the Redis/Valkey scan space,
a limited sample gives an accurate picture of the overall distribution. Derive percentages by dividing
the count for each fqn by the total count in your sample.
- Memory usage — The memory_usage column reports bytes per key. Sum these values per namespace
to estimate how much of the store each feature class occupies.
- Key types — The key_type column indicates the kind of feature data stored:
Scalar for single values, HasMany for relationship data, TimeSeries for time-indexed features, etc.
- TTL — The ttl_seconds column shows how long until a key expires. Keys with no expiration
will show a large or zero value depending on your store configuration.

### Common use cases

### Capacity planning

Use the memory-ordered query to identify which namespaces dominate your online store.
This informs scaling decisions and helps you decide whether to tune
max_staleness to reduce retention for features that don't need long cache lifetimes.

### Verifying deprecated feature cleanup

After removing a feature class from your Chalk project, keys may still exist in the online store.
Chalk runs a nightly cleanup job that removes keys for features no longer in active deployments.
Use the namespace-specific query above to confirm that the cleanup has completed.

### Reducing online store size

If your online store is growing large, consider:

- Lowering max_staleness on features that don't need long retention — see Feature Caching
- Removing feature classes that are no longer used and waiting for the nightly cleanup
- Reviewing HasMany and TimeSeries key types, which tend to consume more memory per entity

### Related resources

- Feature Caching — Configure max_staleness for online store retention
- SQL Explorer — The SQL Explorer interface
- Chalk Catalog Components — Full catalog and schema reference
- Online and Offline Stores — Store configuration options
# Offline Query Heartbeat Timeout
source: https://docs.chalk.ai/docs/offline-query-timeout

## Learn more about debugging offline query timeouts.

Offline queries can consume significant amounts of system resources. Chalk's management plane checks each
running offline query every 60 seconds to verify that the query is still running. If the query has not
updated its heartbeat within the last 60 seconds, the query is considered to have timed out and is killed.

Typically, this is due to the query being too resource-intensive for the system to handle. If you are experiencing
offline query timeouts, you may want to consider the following:

- Check for out-of-memory errors: Check the 'metrics' tab of your query, and look at the reported memory utilization.
If you are running out of memory, you may want to increase the memory requests for your
offline query pods. You can do this by navigating to the "Resources" page in the Chalk UI and increasing the memory
requests for offline query workers.
- Use run_asynchronously: Add run_asynchronously=True to isolate your query to its own Kubernetes pod. This
lowers the chance that your query will contend with other workloads on a single machine and may help prevent timeouts.
- Adjust node selectors: If you are using node selectors to run your offline queries on specific nodes, ensure that
the nodes you are selecting have enough resources to handle the query. Make sure that your workloads are not co-scheduled
with other intense tasks.
- Shard your query: If you are running a large query, consider breaking it into smaller pieces using num_shards.
This can help prevent timeouts and improve the overall performance of your query.
- Optimize your query: Look at the operations the query is processing. Check for Python resolvers that
use heavy libraries, or that perform memory-intensive operations like Pandas transformations.

If you are still experiencing timeouts, contact Chalk Support for further assistance. Please provide an example
failed query and context on how to reproduce the issue.

# Magics
source: https://docs.chalk.ai/docs/notebook-magics

## Chalk cell magics for notebooks

Chalk provides a set of IPython magics to improve the experience of defining resolvers in notebooks.

### Cell Magics

### %%resolver

You can define a SQL resolver in a notebook cell using the %%resolver magic. The magic will parse the cell contents
and upload your resolver to your current working branch.

%%resolver needs to be followed by a resolver name, e.g. root_authorization_resolver as shown below.

Refer to the section on SQL Resolvers to learn more about how to define resolvers.

```
%%resolver root_authorization_resolver
-- resolves: Authorization
-- source: snowflake
SELECT
    id,
    amount_in_cents,
    card_id,
    merchant_id,
    created_at as authorized_at
FROM authorizations
```

Chalk lines up the names of your target SQL columns with the names of your features.
In this case, we have an Authorization feature class that contains a features called authorized_at.
However, our Snowflake table has a column called created_at that we want to use to populate the authorized_at feature.
So, we use the as keyword to rename the column in our resolver.

# Inline Syntax
source: https://docs.chalk.ai/docs/notebook-inline

## Defining features inline in notebooks

In notebooks, you can define features inline using the syntax shown below.

Consider the following feature class definition for RocketEngine

```
from chalk.features import features

@features
class RocketEngine:
    id: int
    mass: float
    volume: float
    thrust: float
```

If we wanted to define a feature inline in a notebook cell, we could do so using the underscore syntax below:

```
RocketEngine.density: float = _.mass / _.volume
```

# Job Queue
source: https://docs.chalk.ai/docs/job-queue

## Understanding Chalk's job queue and resource groups

### Overview

The job queue in Chalk, together with resource groups, functions similarly to warehouses in analytical data platforms - they provide dedicated, configurable compute resources for processing workloads.

A job queue server is a persistent worker process that consumes jobs from a queue and executes them one at a time. By configuring multiple resource groups with different job queue servers, you can create isolated compute environments optimized for different workload types.

### What does the job queue process?

The job queue handles two primary types of workloads:

- Scheduled queries - Feature pipelines that run on a cron schedule (see ScheduledQuery)
- Async offline queries - Large offline queries that run asynchronously when run_asynchronously=True is set

```
# This runs on the job queue
client.offline_query(
    input={'user.id': range(1_000_000)},
    output=['user.name'],
    run_asynchronously=True,  # Runs as a task on job queue
)

# This runs on the query server (NOT the job queue)
client.offline_query(
    input={'user.id': [1, 2, 3]},
    output=['user.name'],
    # run_asynchronously=False by default - runs as synchronous RPC
)
```

### How job queues work

### FIFO Processing

Jobs are processed in first-in, first-out (FIFO) order. Each job queue server processes one job at a time sequentially.

### Fixed Resources

Each job queue server has a single, pre-configured resource allocation (CPU and memory).

### Automatic Fallback

If a job requests resources larger than the job queue server can handle, Chalk automatically skips the queue and runs the job as a standalone Kubernetes pod with the requested resources.

### Resource Groups

Resource groups allow you to create multiple job queue servers with different resource configurations. This is useful for:

- Isolating large scheduled queries from smaller workloads
- Optimizing costs by right-sizing compute for different job types
- Preventing resource contention between different teams or use cases

### Configuring Job Queue Servers

In the Chalk dashboard under Settings > Resources, you can configure the "Job Queue Server" for each resource group:

- Set the CPU and memory allocation
- Configure autoscaling (min/max instances)
- Select the nodepool to use

All Chalk environments start with a Default resource group.

### Targeting Specific Resource Groups

### For Scheduled Queries

```
from chalk import ScheduledQuery

ScheduledQuery(
    name="large-batch-job",
    schedule="0 0 * * *",
    output=[User.features],
    resource_group="large-jobs",  # Runs on the "large-jobs" resource group
)
```

### For Async Offline Queries

```
from chalk.client import ChalkClient, ResourceRequests

client.offline_query(
    input={'user.id': range(1_000_000)},
    output=['user.name'],
    run_asynchronously=True,
    resources=ResourceRequests(
        resource_group="large-jobs"  # Runs on the "large-jobs" resource group
    ),
)
```

### Job Queue vs Query Server

| Aspect | Job Queue Server | Query Server |
|--------|------------------|--------------|
| Processes | Scheduled queries, async offline queries | Synchronous offline queries, online queries |
| Execution | One job at a time (FIFO) | Multiple concurrent requests |
| Resources | Fixed per resource group | Requested per query |
| Scaling | Horizontal (more instances) | Vertical (larger pods) |
| Workload Isolation | Jobs run sequentially without resource contention | Multiple concurrent queries may compete for resources on the same server |
| Timeout Behavior | Can run indefinitely beyond load balancer timeout | Will report an error if execution exceeds load balancer timeout |

### Best Practices

- Create separate resource groups for jobs with significantly different resource requirementsExample: Small daily scheduled queries vs. large weekly batch jobs
- Right-size your default job queue to handle typical workloadsConsider your most common scheduled query needsRemember that oversized requests will automatically get their own pods
- Use resource groups for isolationPrevent one team's large jobs from blocking another team's scheduled queriesGuarantee resources for critical scheduled pipelines
- Monitor queue depth and adjust max instances if jobs are waiting too longJobs will timeout and fail if they can't obtain resources within ~4 hours

### Example Configuration

Here's a common setup with two resource groups:

```
# Default resource group: moderate sizing for typical scheduled queries
# Configured in dashboard: 8 CPU, 16 GB memory

ScheduledQuery(
    name="daily-features",
    schedule="0 1 * * *",
    output=[User.daily_features],
    # Uses default resource group
)

# Large jobs resource group: high-memory machines for big batch processing
# Configured in dashboard: 32 CPU, 450 GB memory

ScheduledQuery(
    name="weekly-aggregations",
    schedule="0 0 * * 0",
    output=[User.historical_aggregates],
    resource_group="large-jobs",  # Uses dedicated high-memory queue
)
```

# Getting Started
source: https://docs.chalk.ai/docs/getting-started

## Your first time with Chalk

### Introduction

Chalk's platform is a powerful tool that allows data engineers
and data scientists to collaborate efficiently and effectively.

In this project we'll create features related to Usersand their credit scores. We'll combine data from an
API and a database to help us decide whether we should issue
new loans.

You will learn how to create a new Chalk project,
create features and resolvers, deploy them to the Chalk
environment, and query the environment using the
Chalk CLI and a Jupyter Notebook.

This tutorial will take about 45 minutes to complete
end-to-end.

### Installing the Required Software

- If you don't have a favorite IDE, install VS Code by
visiting the download site
and running the appropriate installer.
- You'll also want to install
the code CLI command.
- If you haven't already, install Python. You can do
this through Homebrew as follows:

```
# Install Homebrew
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# Use Homebrew to install python3
$ brew install python
```

If you're having trouble installing Python, follow the
instructions in Python's docs.

- Install the Chalk CLI by running

```
$ curl -s -L https://api.chalk.ai/install.sh | sh
```

### Creating your Chalk project

Now that all of your software is installed, let's create
a Chalk project where you will add your features and
resolvers.

- Create a folder and call it chalk-tutorial.
- Run chalk init from inside the chalk-tutorial
to initialize your project files.
This will create two files for you: chalk.yaml and .chalkignore.
The first file, chalk.yaml, contains configuration information about
your project. The second file, .chalkignore, tells your
Chalk CLI tool which files to ignore when deploying
to your Chalk environment. You can edit this file and use it
just like a .gitignore file.

```
$ mkdir chalk-tutorial
$ cd chalk-tutorial
$ chalk init
Created project config file chalk.yaml
Created .chalkignore file
```

- Now edit the chalk.yaml file and set the project field to the
name of your Chalk project. This might be chalk-tutorial, but check
by visiting the Projects page.
- Login by typing chalk login.
If you're using a dedicated environment,
make sure you use the --api-host flag.
Type y when prompted and login in the browser.

Now you're ready to deploy code and query the environment!

### Create a virtual environment

We're going to create a virtual environment
so that you can download and use Python libraries
in your Chalk project.

- Run the following command from inside your Chalk project
to create and activate your virtual environment.
When you want to deactivate your virtual environment,
type deactivate.

```
$ python3 -m venv chalk-tutorial-venv
$ source chalk-tutorial-venv/bin/activate
```

- Your requirements.txt file tells your virtual environment
(and Chalk) which libraries to install. We'll use a few
libraries for this tutorial, so add the following to the
requirements.txt. Feel free to add more libraries later.

```
chalkpy
pydantic
requests
```

- Install the requirements.

```
$ pip3 install -r requirements.txt
```

- Check that the libraries are installed by importing
requests in Python. If there's no error message, it
worked. Exit by typing exit() and hitting enter.

```
$ python3
>>> import requests
>>> exit()
```

### Use Curl and Jupyter to call APIs.

Now that all the software is installed and ready to use,
you're ready to start integrating an API.

- First, lets test the API we're going to use.
Run this command to hit the API from your command line.
Here we're asking "give me the credit score for user 12"
and the API gives us back a JSON object with a credit score.

```
$ curl https://credit-report.chalk.dev/rutter_score/12
{"score":98}
```

Now you should try to hit this API from Python using a
Jupyter Notebook.

- Open VS Code, and create a new file File -> New File.
Select Jupyter Notebook.
- Jupyter will probably ask you which interpreter to use.
If it does, select the virtual environment you created before
(chalk-tutorial-venv).
- If not, you can select it manually.
Select Jupyter virtual environment
- Finally, let's query the API from Jupyter. Enter the following
code and run it with shift+enter.

```
import requests
requests.get(
    "https://credit-report.chalk.dev/rutter_score/12"
).json()["score"]
```

If you see 98, congratulations! You're all setup and ready
to start developing your Chalk project.

### Building a Chalk project

With all the pre-requisites completed, let's jump right
into building your Chalk project.

### Creating your first Chalk feature

We'll create a feature called User with a "Rutter score"
property. The resolver will call the "Rutter" API we tested
earlier, passing the User ID, and return the score.
After you deploy the feature, you will test it in
Jupyter.

- Create a credit.py file and copy in the feature and
resolver definitions below:

```
import requests
from chalk.features import online, features, Features

@features
class User:
    id: str
    credit_score: int

@online
def get_credit_score(
    id: User.id,
) -> Features[User.credit_score]:
    return requests.get(
        f"https://credit-report.chalk.dev/rutter_score/{id}"
    ).json()["score"]
```

- Deploy your code. Pass the --branch flag with a name
so that you don't affect the "actual" environment

```
chalk apply --branch test
```

- Now lets query for your feature from your Jupyter Notebook.
Enter and execute the following code in your notebook.

```
from credit import User
from chalk.client import ChalkClient
ChalkClient().query(
   input={User.id: 'u_F6zY0tE4w8'},
   output=[User.credit_score],
   branch="test"
)
```

You can also query for this feature in your terminal:

```
$ chalk query --in user.id=u_F6zY0tE4w8 \
              --out user.credit_score \
              --branch test
```

Congratulations! You've written your first Chalk feature,
connected it to an external API, and queried it from a
Jupyter Notebook. This is a big achievement!

### Adding a database to Chalk

We have a database containing more information about users,
and it would be good to combine that information together
on our user feature.

- If you have psql
or similar tool installed, you can preview the database from the command line.
When prompted, the password is postgres.

```
psql -U postgres -p 5432 -h 35.188.7.252 -d postgres
postgres=> select * from users limit 10;
```

Notice that we know name, surname, email, birthday, and
is_fraud, a flag that tells us whether we know this user
has committed fraud in the past.

- To use this in your Chalk project, we'll add the database
through the UI. Navigate to your environment, and find
"Data Sources" on the left hand navigation.
- If you see the database already, great, you can skip the
next step of adding the database. Otherwise, continue.
- Click Add a Data Source and choose PostgreSQL.
- Fill out the fields as shown here. The password is postgres.
Postgres

### Write a resolver that resolves a database

- Add the fields from the database to the User feature class
you created before. The properties name, surname, and
email are strings. Birthday is a date, and is_fraud
is a boolean. (Hint: you may have to add from datetime import date to your credit.py file)
- Add the datasource to your Python context. Add the below
code to your credit.py file. This tells Python about
your datasource.

```
from chalk.sql import PostgreSQLSource
user_pg = PostgreSQLSource(name="User_PG")
```

- You can use a SQL File Resolver
to pull this information. Create a new file called
users.chalk.sql and copy the below contents:

```
-- type: online
-- resolves: user
-- source: postgres
-- count: 1
select name, surname, email, birthday, is_fraud from users where id=${user.id}
```

- After deploying (remember to use --branch with the name you specified, for example "test"),
query your feature. Supplying User as the output
tells Chalk to give you back ALL the features of User.

```
res = client.query(
    input={User.id: 'u_F6zY0tE4w8'},
    output=[User],
    branch="test"
)
```

You can also query for this feature in your terminal:

```
$ chalk query --in user.id=u_F6zY0tE4w8 \
              --out user \
              --deployment test
```

# Tutorial: Backtesting
source: https://docs.chalk.ai/docs/fraud-6

## Try out new feature values on historical data.

If you want to skip ahead, you can find the full source code for this tutorial on
GitHub.

After you've created some features and resolvers,
you can use them to generate values for training.

Chalk tracks all the values of the features you
compute, and times at which those values were
computed.

First, we need to sample some user ids on which to
build a dataset.

```
from datetime import datetime, timezone, timedelta
from chalk.client import ChalkClient
from src.models import User

client = ChalkClient()

now = datetime.now(tz=timezone.utc)
ds = client.offline_query(
    output=[User.id],
    lower_bound=now - timedelta(hours=12),
    upper_bound=now,
)

```

```
from chalk.client import ChalkClient

client = ChalkClient()
dataset = client.offline_query(
    input={
        User.id: [],
    },
    output=[],
    recompute_features=True,
)


ds = client.offline_query(
    input={
    "fraud_model.id": spine["fraud_model.id"].to_list()
    },
    input_times=spine['__chalk__.CHALK_TS'].to_list(),
    output=[
        "fraud_model.id",
        "fraud_model.card_created_at",
    ],
    recompute_features=True
)
```

# Tutorial: Inference
source: https://docs.chalk.ai/docs/fraud-5

## Integrate Chalk into your production decisioning systems.

If you want to skip ahead, you can find the full source code for this tutorial on
GitHub.

Now that we've written some features and resolvers
and deployed them to Chalk, we're ready to integrate
Chalk into our production decisioning systems.

### CLI Query

As a sanity check, it can be helpful to use the Chalk CLI
to query a well-known input and ensure that we get the expected output.

We can use the chalk query command,
passing in the id of a user, and the names of the features
we want to resolve:

```
$ chalk query --in  user.id=1  \
              --out user.name  \
              --out user.email \
              --out user.account.balance
Results
user.name             "John Doe"
email                 "john@doe.com"
user.account.balance  2032.91
```

### API Client Query

Once we're satisfied that our features and resolvers are working as expected,
we can use a client library to query Chalk from our application.

In this first example, we'll use the
ChalkClient in the
chalkpy package
to query Chalk from our application:

```
from src.models import User
from chalk.client import ChalkClient

# Create a new Chalk client. By default, this will
# pick up the login credentials generated after running
# `chalk login`.
client = ChalkClient()

client.query(
    input=User(id=1234),
    output=[
        User.id,
        User.name,
        User.fico_score,
        User.account.balance,
    ],
)
```

We use the same feature definitions for querying our data
as we used for defining our features and resolvers.

Chalk has API client libraries in several languages, including
Python,
Go,
Typescript, and
Elixir.

### Code Generation (Optional)

All API clients can operate on the string names of features.
However, in a production system, you may have many hundreds or thousands
of features, and want to avoid hard-coding the names of each feature
in your code.

To help with this, Chalk can codegen a library of
strongly-typed feature names for you.

For example, say the service that calls into Chalk is written in Go.
We can generate a Go library of feature names with the following command:

```
$ chalk codegen go --out ./clients/go/client.go --package=client
✓ Found resolvers
✓    Wrote features to file './clients/go/client.go'
✓    Please do not change the generated code.
```

This generates a file
clients/go/client.go
that looks like this:

```
package client

/**************************************
 Code generated by Chalk. DO NOT EDIT.
 > chalk codegen go --out ./clients/go/client.go --package client
**************************************/

import (
	"github.com/chalk-ai/chalk-go"
	"time"
)

var InitFeaturesErr error

type Account struct {
	Id *int64
	Title *string
	UserId *int64
	Balance *float64
	User *User
	UpdatedAt *time.Time
}

type User struct {
	Id *int64
	Name *string
	Email *string
	Account *Account
	AccountNameMatch *float64
	FicoScore *int64
	CreditScoreTags *[]any
}

var Features struct {
	Account *Account
	User *User
}

func init() {
	InitFeaturesErr = chalk.InitFeatures(&Features)
}
```

We can then use this library to query Chalk:

```
import (
    "github.com/chalk-ai/chalk-go"
)

// Create a new Chalk client.
client := chalk.NewClient()

// Create an empty struct to hold the results.
user := User{}

// Query Chalk, and add the results to the struct.
_, err = client.OnlineQuery(
    chalk.OnlineQueryParams{}.
        WithInput(Features.User.Id, 1234).
        WithOutputs(
			Features.User.Id,
			Features.User.LastName,
			Features.User.FicoScore,
			Features.User.Account.Balance,
        ),
    &user,
)

// Now, you can access the properties of the
// user for which there was a matching `output`.
fmt.Println(user.Account.Balance)
```

If your calling service is written in Python,
but you don't want to take a dependency on the
repository that contains your Chalk features,
you can generate your Python features into a separate
repository:

```
$ chalk codegen python --out ./clients/python/client.py
```

You can see the generated code in
clients/python/client.py.

If you are generating Python into a subdirectory of your
Chalk project, be sure to add an entry to your
.chalkignore
containing the directory of your generated code
(in the above example, clients/).
Otherwise, Chalk will find duplicate definitions
of your features.

# Tutorial: Python Resolvers
source: https://docs.chalk.ai/docs/fraud-4

## Define resolvers in Python that call APIs and compute derived features.

If you want to skip ahead, you can find the full source code for this tutorial on
GitHub.

So far, we've mapped SQL tables into feature classes. But there's a lot more we can do with
Chalk. In this step, we'll add features to our Account and User feature classes
that are gathered from API calls and computed downstream of other features.

### Derived Features

We've noticed that some fraudsters try to link
stolen accounts to our platform and attempt to
transfer money through our system.
To detect this behavior, we want to compute a
similarity score between the user's name and the
account's title.

We'll start by adding this new feature, account_name_match,
to our User feature class.

```
@features
class User:
    id: int
    name: str
    email: str
    account: "Account"

+   # The similarity between the user's name and the account's title.
+   account_name_match: float
```

Next, we'll define a resolver that computes this feature.
We'll use
Jaccard similarity
to compute the similarity score.

```
from src.models import User
from chalk import online

@online
def account_name_match(
    title: User.account.title,
    name: User.name,
) -> User.account_name_match:
    """Docstrings show up in the Chalk dashboard"""
    intersection = set(title) & set(name)
    union = set(title) | set(name)
    return len(intersection) / len(union)
```

The @online decorator tells Chalk that this resolver should be called
in realtime when the User.account_name_match feature is requested.
Our feature dependencies are declared in the function signature
as User.account.title and User.name.
Chalk will automatically retrieve
User.account_id and User.name
from our
user.chalk.sql
resolver. Then, using this account id,
Chalk will retrieve Account.title
from the online store, where it has been cached from our cron run of the
balance.chalk.sql
resolver.

### Testing

Resolvers are callable functions, so we can test them like any other Python function.
Let's test our new resolver by writing a
unit test:

```
from src.resolvers import account_name_match

def test_names_match():
    """Resolvers can be unit tested exactly as you would expect.

    Here, the `account_name_match` resolver should return 1.0
    because the `title` and `name` are identical.
    """
    assert 1 == account_name_match(
        title="John Coltrane",
        name="John Coltrane",
    )

def test_names_completely_different():
    """The `account_name_match` resolver should return 0
    because the `title` and `name` don't share any characters.
    """
    assert 0 == account_name_match(
        title="John Coltrane",
        name="Zyx",
    )
```

You can read more about testing resolvers in the
API docs.

### API Calls

Any Python function can be used as a resolver.
This means that we can call APIs to compute features.
Let's add a feature that computes the user's FICO score
from our credit scoring vendor,
Experian.

As before, we'll first add the features that we want to compute:

```
+ from chalk.features import features

@features
class User:
    id: int
    name: str
    email: str
    account_name_match: float

+   # The fraud score, as provided by a third-party vendor.
+   fico_score: int = feature(min=300, max=850, strict=True)
+
+   # Tags from our credit scoring vendor.
+   credit_score_tags: list[str]
```

We are adding
strict validation
to our fico_score feature
to ensure that we only store and utilize valid FICO scores.

Now, we can write a resolver to fetch the user's FICO score from Experian.

```
from src.models import User
from src.mocks import experian
from chalk.features import online, Features

@online
def get_fraud_score(
    name: User.name,
    email: User.email,
) -> Features[User.fico_score, User.credit_score_tags]:
    response = experian.get_credit_score(name, email)

    # We don't need to provide all the features for
    # the `User` class, only the ones that we want to update.
    return User(
        fico_score=response['fico_score'],
        credit_score_tags=response['tags'],
    )
```

Here, we are returning two features of the user,
User.fico_score and User.credit_score_tags.
We use the Features type to indicate
which feature we expect to return.
Also note that we are initializing the User class with
only the features that we want to update.
This partial initialization is the primary difference
between Python's
@dataclass
and Chalk's
@features.

### Deploying

Finally, we'll want to deploy our new resolvers.
As before, we can check our work by using a branch
deployment:

```
$ chalk apply --branch tutorial
✓ Found resolvers
✓ Deployed branch
```

We can then query our new features:

```
$ chalk query --branch tutorial  \
              --in     user.id=1 \
              --out    user.name_match_score
```

# Tutorial: SQL Resolvers
source: https://docs.chalk.ai/docs/fraud-3

## Mapping data from SQL sources to feature classes.

If you want to skip ahead, you can find the full source code for this tutorial on
GitHub.

A primary source of data for many companies is a SQL database. Chalk can
automatically ingest data from SQL databases and map it to feature classes.

### Configuring SQL sources

In our example application, we have two databases: PostgreSQL and Snowflake.
Our PostgreSQL database is the primary database used elsewhere in our
codebase, and our Snowflake database is used for analytics, with tables
populated from DBT views and batch jobs.

To configure our SQL sources in Chalk, we'll create a
datasources.py
file that contains a
SnowflakeSource
and a
PostgreSQLSource:

```
from chalk.sql import SnowflakeSource, PostgreSQLSource

snowflake = SnowflakeSource()
postgres = PostgreSQLSource()
```

These singleton variables can be used to query data in
Python SQL resolvers.
They're also necessary before we can write any
.chalk.sql
files, as we'll do below.

### Online data

Chalk's preferred way to ingest data from SQL databases is to use
SQL file resolvers. This allows us to write
queries in the same language as our database, and to use the same tooling to
test and debug them.

To create a SQL file resolver, we create a file in our project directory with
the extension .chalk.sql. We can then write a SQL query in this file, and
add metadata
to the top of the file to tell Chalk how to ingest the data.

From our User feature class, we may want to resolve the
name and email attributes from a PostgreSQL table.
To do this, we can write the following SQL file resolver:

```
-- The features given to us by the user.
-- resolves: user
-- source: postgres
select
    id,
    full_name as name,
    email
from users;
```

The resolves key tells Chalk which feature class the columns
in the select statement should be mapped to.
Then, the target names of the query are
compared against the names of the attributes on the feature class.
If the names match after stripping underscores and lower-casing,
the select target is mapped to the feature.
In the example above, we aliased the full_name column to name,
so it will be mapped to the name attribute on the User feature class.
Chalk validates your SQL file resolvers when you run
chalk apply.

The source key tells Chalk which integration
to use to connect to the database. Since we have only one PostgreSQL
database, we can reference the source as postgres. If we had
multiple PostgreSQL databases, we can use named integrations to
reference different databases.

Other comments in the SQL file resolver are indexed by Chalk and can be
searched in the Chalk dashboard.

### Deploying!

Now that we've written a resolver, we can deploy our feature pipeline and
query our data in realtime.

In testing, it can be helpful to deploy your feature pipeline to a
branch, which allows you to test your changes without
affecting the production feature pipeline. Branch deployments
take only a few seconds to deploy.

```
$ chalk apply --branch tutorial
✓ Found resolvers
✓ Deployed branch
```

### Querying

Now that we've deployed our feature pipeline, we can query our data in realtime.
One of the easiest ways to do this is from the Chalk CLI.

```
$ chalk query --in user.id=1 --out user.name --out user.email

user.name     "John Doe"
email         "john@doe.com"
```

This query will fetch the name and email attributes from the User feature
class for the user with id=1, hitting the PostgreSQL database directly.

### Push-down filters

Note that in SQL file resolver that we wrote,
we didn't include a where clause.
However, Chalk automatically pushes down filters to the database
when querying features.
So, the SQL that will execute against our PostgreSQL database
will be:

```
select
    id,
    full_name as name,
    email
from users
+ where id = 1;
```

Chalk can also push down non-primary key filters to SQL databases.
For example, to fetch all transactions for a user, Chalk will
modify the
SQL-resolver query
to include a where clause:

```
select
    id,
    account_id,
    amount,
    status,
    date
from txns
+ where account_id = 38;
```

### Offline data

In addition to online data, we can also ingest data from SQL databases
into Chalk's offline store. Offline data won't be queried in realtime,
but can be used to train models and generate features.

For our Account feature class, we may want to ingest data from a
Snowflake table. We can write a
SQL file resolver
to do this:

```
-- Incrementally ingest account data from Snowflake.
-- This comment will be searchable in the Chalk dashboard.
--
-- resolves: account
-- source: snowflake
-- type: offline
-- cron: 5m
-- incremental:
--   mode: row
--   lookback: 1h
select
    id,
    user_id,
    amount,
    updated_at
from accounts;
```

There are a few differences between this SQL file resolver and the one
we wrote for the User feature class.

First, we've added a type key to the header. This tells Chalk
that this resolver should be used to ingest data into the offline store.
If we didn't include this key, Chalk would assume that this resolver
could be queried in realtime.

Second, we've added a cron key to the header. This tells Chalk
to run this resolver on a schedule. In this case, we're telling Chalk
to run this resolver every 5 minutes.

Finally, we've added an
incremental
key to the header.
This tells Chalk to only ingest new data from the database, and is helpful
when you have an immutable events table. Also, notice the new
updated_at column in the select statement. We'll map that column
to a FeatureTime attribute in our feature class:

```
from chalk.features import feature, features, FeatureTime

@features
class Account:
    id: int
    user_id: int
    amount: float
+   updated_at: FeatureTime
```

Features with overridden observation timestamps are inserted into
the offline store with the timestamp that you
specify. The observation timestamp works like an "effective as of" timestamp.
When you sample historical data, you can specify the observation timestamp
at which you want to sample a feature value. Then, Chalk will return the
most-recent feature value that was observed before that timestamp.
This method of sampling ensures temporal consistency
in your feature values.

### Reverse ETL

While our offline data is useful for training models and generating features,
we may also want to use these values for serving production queries.

However, data warehouses like Snowflake
and BigQuery are optimized for analytics
and are not well-suited for transactional queries.

We can have Chalk
reverse-ETL
our offline data into our online store
by setting the
max_staleness
and
etl_offline_to_online
keyword arguments on our
@features
decorator:

```
- @features
+ @features(max_staleness="infinity", etl_offline_to_online=True)
class Account:
    id: int
    user_id: int
    amount: float
    updated_at: FeatureTime
```

The max_staleness keyword argument tells
Chalk how stale a feature value can be before it should be refreshed.
In this case, we're telling Chalk that we'll tolerate arbitrarily old
feature values. However, we could also specify a max_staleness of
1h or 1d to tell Chalk not to serve feature values that are older
than 1 hour or 1 day.

The etl_offline_to_online keyword argument
tells Chalk to reverse-ETL our offline data into our online store.
By default, data only enters the online store when it's queried in
realtime. However, by setting this keyword argument, we're telling
Chalk to reverse-ETL our offline data into our online store.

# Tutorial: Data Modeling
source: https://docs.chalk.ai/docs/fraud-2

## Defining the features that we want to compute.

If you want to skip ahead, you can find the full source code for this tutorial on
GitHub.

In this example, we'll consider a fintech use-case
where we want to detect fraudulent credit card purchases.
Our data consists of a list of credit card transactions,
each with a timestamp, a location, and a purchase amount.
We also have information about the cardholder and the
accounts that the card is linked to.

### Define features

We'll start by modeling the features we want for our
the users in our system.
We'll start simple with three
scalar features:
user.id, user.name, and user.email.
First, we'll create a new file called models.py
where we'll define a User class decorated with
@features.

```
from chalk.features import features

@features
class User:
    id: int

    # The name the user provided to us at signup.
    # :owner: identity@chalk.ai
    # :tags: pii
    name: str

    # :tags: pii
    email: str
```

Note that at this point,
we haven't defined how to compute these
features. We are only thinking about the data
that we would like to have.

### Primary keys

There are a few things to note here. First, all our feature
classes need to have a unique id field. By default, this
is the field named id. However, if you want to use a
different field as the primary key, you can specify it
using the Primary argument to @features.

```
from chalk.features import features

@features
class User:
-   id: int
+   user_id: Primary[int]
    name: str
    email: str
```

### Tags, Descriptions, & Owners

In our features below, we've added some comments and
annotations to our features. These are optional, but
can be useful for documentation and for setting alerting
policies. For example, you may wish to send PagerDuty alerts
to different teams based on
the owner of the related feature.

Any of the comments and tags from the code also show up
in the Chalk dashboard,
and are indexed for search.

For example, we've added a pii tag
to the name and email fields. This means that
these fields will be treated as personally identifiable
information and will be subject to additional
restrictions.

### Has-One Relationships

Next up, we'll define a related feature class to our users.
We'll call this class Account and it will represent
a bank account that a user owns.

```
from chalk.features import features

@features
class Account:
    id: int

    # The name of the owner of the account.
    title: str

    # The id of the user that owns this account.
    user_id: int

    # The balance of the account, in dollars.
    balance: float
```

This should look much like what we did for the User class.
However, we may want to link these two classes together.
We can do this by adding a user field to the Account class.

```
@features
class Account:
    id: int
-   user_id: int
+   user_id: User.id
    balance: float

+   # The user that owns this account.
+   user: User
```

This denotes that each account has one user, and that the
Account.user_id and the User.id are equal and of type int, as described by Account.user_id.

Once we've defined the relationship on one side of the
join, we can define the inverse relationship on the
other side without needing to specify the predicate
again.

```
@features
class User:
    id: int
    name: str
    email: str

+   # The account that this user owns.
+   account: "Account"
```

### Has-Many Relationships

The final feature entity that we'll define in this tutorial is
for transactions. Each account has many transactions, and each
transaction is linked to a single account. We'll define the
Transaction class and link it to our Account class as follows:

```
- from chalk.features import features
+ from chalk.features import features, DataFrame

+ class TransactionStatus(str, Enum):
+     PENDING = "pending"
+     CLEARED = "cleared"
+     FAILED = "failed"
+
+ @features
+ class Transaction:
+    id: int
+
+    # The id of the account that this transaction belongs to, set to a join.
+    account_id: "Account.id"
+
+    # The amount of the transaction, in dollars.
+    amount: float
+
+    # The status of the transaction, defined as an enum above.
+    status: TransactionStatus
+
+    # Because we define the join condition between
+    # `Transaction` and `Account` below, we don't
+    # need to repeat it here.
+    account: "Account"

@features
class User:
    id: int
    name: str
    email: str

    # The account that this user owns.
    account: "Account"

@features
class Account:
    id: int
    user_id: User.id
    balance: float
    user: User
+   transactions: DataFrame[Transaction]
```

This is the first time we're seeing the DataFrame type.

A Chalk DataFrame models tabular data in much the same
way that pandas does. However, there are some key differences that
allow the Chalk DataFrame to increase type safety and performance.

Like pandas, Chalk's DataFrame is a two-dimensional data structure with
rows and columns. You can perform operations like filtering, grouping,
and aggregating on a DataFrame. However, there are two main differences.

- Lazy implementation - Chalk's DataFrame is lazy and can be backed by multiple data sources, where a pandas.DataFrame executes eagerly in memory.
- Use as a type - Chalk's DataFrame[...] can be used to represent a type of data with pre-defined filters.

You can read more about the Chalk DataFrame
in the docs and
API Reference.

You might also notice that we've used an Enum feature here.
Chalk supports many feature types, including
Enum,
lists and sets,
and @dataclasses.

# Feature Studio
source: https://docs.chalk.ai/docs/feature-studio

## Define, deploy, and manage features and resolvers with Chalk's Feature Studio.

Chalk's Feature Studio provides a no-code interface within the web dashboard for users to
define, deploy, and manage features and resolvers. The Feature Studio provides intuitive forms
and visualizations to help users create and edit features in collaboration either entirely
independently or in conjunction with Chalk's traditional Python-based interface.

After defining features and resolvers in the Feature Studio, users can deploy their changes either
to branches for testing, or directly as mainline deployments. From there, users can use the
Online and Offline Data Explorers in the dashboard to trigger online and offline queries to validate
their new feature pipelines, and create datasets for machine learning workflows.

This workflow is still in alpha--please reach out to the Chalk team if you would like to try it out.

### Getting Started

To access the Feature Studio, navigate to the Feature Studio tab in the Chalk dashboard.
The studio currently loads the graph of all features and resolvers defined in the current active
deployment in the environment. All features are editable, and show their current definitions, types,
and metadata (including description, owner, tags, and max_staleness). All resolvers show their
definitions, metadata, and links to upstream and downstream features.

Feature Studio Home Page

### Developing in the Feature Studio

In the dashboard, users can click the Add New button to define a new feature namespace, feature
within an existing namespace, or resolver. Similar to the Pydantic-style definitions in Chalk's
Python-based interface, users can define typed features with additional metadata.

Feature Studio: Add New Feature

In addition to creating new features, users can also edit their features upon creation, or
modify existing features in the current deployment.

Feature Studio: Edit Feature

After defining the feature schema, users can define resolvers that indicate to the Chalk engine
how feature values should be computed. SQL resolvers enable users to write
SQL queries to load and transform data from their integrated data sources.
Python resolvers provide the flexibility to call API's, execute models,
and perform arbitrary computations to generate feature values. Chalk Expressions
enable users to write simple, intuitive computations referencing other features.

Feature Studio: Add SQL Resolver

The Feature Studio supports the definition of more complex features as well, such as
Windowed Aggregations. Through the feature definition modal, users can define time-based
aggregations with custom filters based on has-many relationships between feature classes.

Feature Studio: Add Windowed Agg

After defining the necessary features and resolvers for a new use case, users can preview all
of the changes made in their current studio session, including all new, modified, and deleted
components.

Feature Studio: Preview Changes

Once satisfied with the changes, users can deploy their new graph either to the branch server
for testing, or directly as a mainline deployment for use in production.

Feature Studio: Deploy Changes

### Collaboration in the Feature Studio

The Feature Studio is designed to enable concurrent collaboration between multiple users, the same
way that multiple users can work on branches in Chalk's Python-based interface. In addition, many
teams have some users who prefer to work in the Feature Studio, while others prefer the code-based
interface. The Feature Studio supports this hybrid workflow as well, enabling imports of graphs as
defined in code, as well as code exports of changes deployed from the Feature Studio.

# Support
source: https://docs.chalk.ai/docs/enterprise-support

## Get in touch with our support team!

Our documentation is designed to be as comprehensive and easy to understand as possible. In addition, we have a
team of Support Engineers and Forward Deployed Engineers who are available to answer customer questions and
help to troubleshoot any issues that arise. All Chalk customers have channels of communication available with
them to get in touch with our production support team and file tickets. Finally, the Chalk on-call engineering team
does have a 24/7 paging system and alerting configured for customer environments to ensure that we are able to
respond and resolve outages in a timely manner. We ask that customers also configure alerting and paging accordingly
such that the Chalk team can be most effective in responding to and mitigating these potential issues.

There are two levels of support available to customers: Standard Support and Enterprise Support. All customers
have access to Standard Support, which enables customers to contact the Chalk team, and create support tickets.
The Chalk team is distributed across multiple time zones, and so strives to respond to all tickets and messages
in a timely fashion.

### Standard Support

Customers can create support tickets by starting a new thread and adding the 🎫 ticket reaction. Our
production support team monitors all tickets and will respond in a timely manner. If you have an urgent issue or need
support with an outage, please ensure to highlight the urgency
of the issue in the ticket and our team will prioritize accordingly. All customers can also view the status of their
tickets through the Pylon Customer Portal.

### Enterprise Support

In addition to our timely and friendly support provided for all customers, we also have an Enterprise Support plan
that customers can choose to include in their bundles. This allows for a 24/7 Pagerduty line to page our on-call engineer
for urgent issues that require immediate attention.

Enterprise support customers are provided with three ways to page our on-call engineering team, outlined below.
Our on-call rotation is staffed 24/7 year-round. We ask that customers provide context about the issue or incident
when paging our on-call team so that we can respond as effectively as possible, especially in case of outages.

### 1. Paging via the dashboard

To page via the dashboard, click your username at the bottom left hand corner of the dashboard in the menu bar,
then click Escalate Issue. This will lead to a modal that enables you to provide more information about the incident.

### 2. Paging via Slack

Enteprise support customers can also page our on-call engineering team via Slack by adding the 🎫 ticket reaction
to a message, marking the ticket as urgent, and then selecting the option to page our on-call team.

The urgency option looks like this:

This option to page our on-call will open another modal that allows you to provide more information about the incident:

### 3. Paging via email

Enterprise support customers are given an emergency email address. Each message sent to this address immediately
pages our on-call engineering team.

# Enterprise Deployment
source: https://docs.chalk.ai/docs/deployment

## Enterprise Deployment Model

Chalk integrates with your data sources, transform this data with feature pipelines,
store this data in online and offline storage, and provide monitoring on feature computation and distributions.

### Enterprise Service Architecture

Chalk offers a hosted model ("Chalk Cloud"), or a customer-hosted model ("Customer Cloud").

There are a few main components of a Chalk deployment:

- Management - serves non-customer data (like alert configuration and RBAC configuration).
- Builder - builds containers that run your feature pipelines.
- Compute - machines that run your feature pipelines. In both AWS and GCP, the compute runs on
Kubernetes with Knative.
- Customer Data - the online and offline stores for your features.
- Secrets - environment variables and configuration for your data sources.

These components are organized as follows:

### Data Isolation

In the enterprise deployment, your API clients talk directly to the compute engine deployed into your cloud.
Feature values, historical and online, do not escape your cloud project.

### Storage

Chalk uses different storage technologies to support online and offline use-cases.

The online store is optimized for serving the latest version of any given feature for any given entity with the minimum possible latency.
Behind the scenes, Chalk uses a key-value store for this purpose.
Chalk can be configured to use Redis or Cloud Memory Store for smaller resident data sets with high latency requirements,
or DynamoDB when horizontal scalability is required.

The offline store is optimized for storing all historical feature values, serving point-in-time correct queries,
and tracking provenance of features.
Chalk supports a variety of storage backends depending on data scale and latency requirements.
Typically, Chalk uses TimescaleDB, Redshift, or BigQuery.

# Online and Offline Stores
source: https://docs.chalk.ai/docs/choosing-online-offline-stores

## Selecting an online and offline store for your environment

When setting up a new environment, Chalk provides several options for choosing a storage provider
for your online and offline store. The DBMS (Database Management System) that you choose will depend on your
specific requirements, as well as your cloud deployment provider.

### Online Store Options

The Chalk online store is used for low-latency serving of real-time feature values. Although Chalk's query engine
is optimized for efficient computation of feature values by compiling Python and SQL resolvers into Rust and C++,
caching computed values in the online store can further improve performance.

### GCP Online Store Options

There are two options for online stores for customers on GCP (Google Cloud Platform):

| Store                  | Description                               | Performance  | Scaling    |
|------------------------|-------------------------------------------|--------------|------------|
| Memorystore for Valkey | Valkey (in-memory key-value NoSQL store)  | microseconds | vertical   |
| Bigtable               | Distributed wide-column NoSQL database    | milliseconds | horizontal |

Generally, customers will choose the data store that they already use within their data platform.
However, we would generally recommend Memorystore for Valkey, as it is optimized for low-latency and high
throughput, and Bigtable for huge storage needs.

### AWS

There are two options for customers on AWS (Amazon Web Services):

| Store                  | Description                    | Performance  | Scaling     |
|------------------------|--------------------------------|--------------|-------------|
| ElastiCache for Valkey | Redis (in-memory store)        | microseconds | vertical    |
| DynamoDB               | Key-Value NoSQL database       | milliseconds | auto-scales |

We generally recommend DynamoDB for its performance optimizations and ElastiCache for Valkey for its low-latency and greater
storage capacity for large rows. However, some customers may choose to use RDS depending on their existing
data platform.

### Azure

For customers on Azure, we offer Azure Cache for Redis for the online store.

| Store                          | Description                       | Performance  | Scaling     |
|--------------------------------|-----------------------------------|--------------|-------------|
| Azure Cache for Redis          | Redis (key-value in-memory store) | microseconds | horizontal  |

We generally recommend the Azure Cache for Redis to customers on Azure for a low-latency and scalable database with storage based
pricing.

### Offline Store Options

The Chalk offline store is used for storing historical feature values. The offline store also serves
data for offline queries, which can be used for analytics, batch processing, and other use cases.
We offer four options for offline stores:

| Store                 | Storage                     |
|-----------------------|-----------------------------|
| Google BigQuery       | Columnar (Bigtable-based)   |
| Amazon Redshift       | Columnar (Parquet)          |
| Snowflake             | Columnar (Micro-partitions) |
| Databricks Delta Lake | Columnar (Parquet)          |
| Iceberg               | Columnar (Parquet)          |

For customers with GCP cloud deployments, we generally recommend Google Big Query for its performance with
analytical queries. However, generally, customers will choose the data store that they already use within
their data platform.

# Chalk Billing
source: https://docs.chalk.ai/docs/billing

## Learn about Chalk's billing model and how to optimize costs.

Chalk charges for machine uptime of nodes labeled as Chalk Managed. We calculate this by
multiplying:

- The instance type
- Chalk’s credit utilization rate/hour for that instance type
- The number of hours (i.e., uptime) that the node remains active.
Rather than rounding to the nearest hour, Chalk meters usage in 10-second increments.

Regardless of the load placed on a Chalk-managed node, credit usage remains the same.
We charge for the node’s uptime, not based on the level of activity within the node.
You can run unlimited queries or create multiple branches without incurring extra charges.
Billing is based solely on the node’s active hours, not on how many features or branches are used.

### Finding Chalk Credit Rates

You can see the full list of credit utilization rates per hour for all machine types in the Chalk
dashboard under Settings > Usage > Utilization Rates.

To view the full list of credit utilization rates in your terminal, log into Chalk in the
terminal and use the Chalk CLI command to view usage rates.

```
$ chalk login
$ chalk usage rates
```

### Cost Optimization Tips

There are two primary ways to optimize your resource configurations for cost optimization.

### Configure Auto-Shutdown Periods

The branch server can be configured to automatically shut down after a window of inactivity. To set this
window of inactivity, go to Settings > Resources > Branch Server Configurations in the dashboard.
After the specified window of inactivity, the server automatically shuts down, halting costs. If the
branch server is shut down and activity is detected, including branch deployments and queries, then the
branch server will automatically spin back up.

### Configure Resource Configurations

For the other nodes in your cluster, you can configure the resource configurations according to your needs
in the dashboard under Settings > Resources > Resource Configurations. You can select the instance type
for each server that is right for you, and set a scaling policy that ensures that you scale up when traffic
is high, but notably that your nodes scale down when traffic is low. The instance type selected should have
enough capacity to support the resource request multiplied by the number of max instances, plus additional overhead.

### Frequently Asked Questions

### Do I get charged for pods or for nodes?

You are charged per node. Multiple Chalk pods on a single node does not change the amount of the credit
utilization.

### What if we are running non-Chalk workloads on the same cluster?

Chalk only applies charges to nodes labeled “Chalk Managed.” Other workloads on different nodes do not
incur Chalk charges. You can also configure your cluster to have isolated nodepools to ensure that
unrelated workloads are completely isolated from your Chalk Managed nodes.

### What do these labels in the nodepool configuration pane mean?

You may notice labels like Chalk, Restricted, and Isolated in the nodepools settings pane.

Different nodepool labels

- Chalk: This label indicates that the nodepool makes Chalk-managed nodes, whose uptime contributes to credit usage. All nodepools
created through the Chalk dashboard automatically have this label, although the dashboard will also display nodepools without it.
- Isolated: This label indicates that the nodepool will not allow any workloads to schedule on its nodes
unless they are explicitly configured to do so by setting the Nodepool field in the Resources settings pane. Controlled by the checkbox
"Isolate this nodepool".
- Restricted: This label indicates that the nodepool makes nodes that only allow Chalk workloads to schedule on them. This is
useful in the case where Chalk is running in your cluster alongside other unrelated workloads, and it prevents those workloads from
inadvertently consuming Chalk credits. Controlled by the checkbox "Restrict to Chalk workloads only".

Chalk workloads are only allowed to schedule on nodes from nodepools with the Chalk label. They will not schedule on an Isolated nodepool
unless configured to do so, and the Restricted label has no effect on whether Chalk workloads can schedule on the nodepool, but only affects
unrelated non-Chalk workloads.

### Do more branches cost more money?

No. Because one pod runs all branches, there is no extra cost for having multiple branches.

### Do I get charged if nobody is running queries but the node is still up?

Yes, if the node is up, you are accumulating costs. You can mitigate this by setting the auto-shutdown
period for the branch server for periods of inactivity, as well as by configuring a scaling policy for
your other workloads.

### Does Chalk charge for storage or staging environments?

Chalk only charges for compute resources (i.e., running nodes). If a staging environment is idle or shut
down, it won’t incur costs.

### Chalk Marketplace Billing

Chalk supports marketplace billing through both AWS and GCP. With this setup, your Chalk usage is billed directly to
your cloud infrastructure provider, appearing as a line item on your existing bill and simplifying your payment process.

If you’re interested in enabling marketplace billing, reach out to your Chalk representative. Our finance team will guide
you through the required steps and coordinate a private offer. Once finalized, you’ll be able to receive and pay
your Chalk charges directly through
AWS Marketplace or
GCP Marketplace.

Depending on your Chalk agreement, we can accommodate:

- Prepaid bundles, invoiced up front.
- Standard usage-based billing, invoiced monthly in arrears. For example, your April Chalk usage will appear on
your April cloud provider bill.

The benefits of marketplace billing include:

- No extra invoices to manage
- Chalk charges consolidated with your existing infrastructure spend
- Available on both AWS and GCP
# Benchmarking
source: https://docs.chalk.ai/docs/benchmark

## Time to put Chalk to the test

After setting up your features, resolvers, etc., you'll want to see if your queries meet your speed requirements! We have a tool in alpha to make this process easier. To explore the most up-to-date options available, run chalk benchmark --help in the terminal using the CLI tool.

### Scale

It's important to isolate and scale your resources with the level of benchmark you are performing. The larger the QPS, the larger and/or more machines you'll need. With more cached features, you may need to increase your online store's capabilities as well. In the case of Valkey/Redis, this could be increasing your cluster size and/or node capacity. You can read more about how to update these resources on our Resource Configuration Page

# Ambiguous Resolvers
source: https://docs.chalk.ai/docs/ambiguous-resolvers

## Ambiguous Resolvers

### Resolving Ambiguous Resolver Errors

In standard operation, Chalk assumes that each feature is un-ambiguously
resolved by a single "in-scope" resolver. If this assumption
is violated, Chalk's planner will raise an "ambiguous resolver" error that looks like --

```
Chalk was unable to determine which resolvers to run for feature 'user.id'.
There were multiple candidates ....
```

This error typically indicates that there is a mistake in resolver definitions,
but it may arise in other situations as well.
This document describes common causes of ambiguous resolver errors and how to resolve them.

### Multiple DataFrame-Returning Resolvers

Often, ambiguous resolver errors arise when there are multiple resolvers that return dataframes that include the
same feature. This occurs most often when multiple offline resolvers return the "primary feature" for a given
feature class.

For example:

```
@online
def get_users() -> DataFrame[User.id, User.name]:
    ...

@online
def get_user_registration_dates() -> DataFrame[User.id, user.registration_date]:
    ...
```

This tends to arise when some of the features for a particular entity are resolved from one data source,
and other features for the same entity are resolved from another data source (i.e. a different SQL table).

This causes ambiguity because the query planner cannot determine which resolver returns "all" of the user rows.
To resolve this ambiguity, you can define a single "primary" resolver that returns all the features for the
entity in question by adding the total=True keyword argument --

```
from chalk import online

+ @online(total=True)
def get_users() -> DataFrame[User.id, User.name]:
    ...
```

or for SQL resolvers:

```
-- resolves: User
-- source: snowflake
-- type: offline
+ -- total: true
select
    id,
    name
from users
```

The total keyword argument indicates to the Chalk query planner that all primary keys for the entity are returned by this resolver.
Other resolvers which return subsets of the entity's features can still be defined, but they will be combined with
the "total" resolver to ensure that all rows are returned via a left-outer-join operation.

### Multiple Implementations of Resolvers

Sometimes, overlaps in resolver definitions arise when multiple implementations of the same feature are defined. Common
scenarios include:

- if an A/B test is being run
- a new version of a feature is being rolled out
- offline query workloads with multiple different source parquet/csv datasets
- switching between a production or sandbox version of a service call

In these cases, you can resolve the ambiguity by adding tags to resolvers in order to break scoping ties --

```
@online(tags="**api:mock**")
def simulate_no_fraud(id: User.id) -> User.fraud_score:
    return 10

@online(tags="**api:sandbox**")
def sandbox_score(
    name: User.name,
    email: User.email,
) -> User.fraud_score:
    return sandbox.fraud_score(name, email).score

@online
def real_score(
    name: User.name,
    email: User.email,
) -> Features[User.fraud_score, User.fraud_tags]:
    r = prod.fraud_score(name, email).score
    return User(fraud_score=r.score, fraud_tags=r.tags)
```

In this example, the simulate_no_fraud and sandbox_score
resolvers can be selected by specifying the appropriate tag when making a feature request.
The real_score resolver will be used when no tags are specified.

For more information, see resolver tags.

### Online and Offline Resolvers with Overlapping Features

Often, a single feature may have a natural "online" source (i.e. PostgreSQL, or a microservice API),
and a natural "offline" source (i.e. Snowflake, or another bulk warehouse system).
This case is handled automatically by Chalk's planner,
which will prioritize @online resolvers over @offline resolvers when both are available.





