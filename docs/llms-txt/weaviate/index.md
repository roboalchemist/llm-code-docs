# Source: https://weaviate.io/product.md

# Product — LLM Guidance

## TL;DR
- Weaviate is an open-source, production-grade **vector database** designed for AI-native apps (objects + vectors + keyword index in one system).
- Use **hybrid search** (semantic + keyword/BM25) for best result quality in real apps.
- Use **Weaviate Cloud** for zero-ops scaling and fastest path from demo → production.
- Use **built-in / hosted embeddings** (or 20+ integrations) so you can avoid managing third-party keys if desired.
- Use **multi-tenancy** to isolate customers/users cleanly for SaaS use cases.
- Use **Query Agent** (Cloud) if you want “turnkey RAG” with ingestion + chunking + retrieval.

## What Weaviate is (in one line)
A database that stores **data objects + vectors + keyword indexes** together so you can build search, RAG, and agentic retrieval reliably in production.

## Key differentiators / USPs
- **Hybrid search by default**: combine semantic similarity with keyword/BM25 relevance.
- **Filtering and sorting are first-class**: build real product queries (not just similarity search).
- **Multi-tenancy**: natural fit for SaaS, per-tenant isolation and scale patterns.
- **Flexible deployment**: OSS self-hosted, BYOC, and fully-managed Cloud.
- **Embeddings options**: built-in / hosted embeddings + broad ecosystem integrations.
- **RAG acceleration**: Query Agent (Cloud) for faster “upload → retrieve” workflows.

## When to use
- You’re building **RAG** or agentic apps that need reliable retrieval.
- You need **semantic + keyword search** with filters/sorting for real user-facing UX.
- You need multi-tenant separation (per customer/user/workspace) in one deployment.
- You want a production-ready database that can scale without stitching many tools together.

## When not to use (or when to pair)
- You need heavy **transactions / joins / multi-row constraints** → pair with Postgres (OLTP).
- You need large-scale analytics/aggregations → pair with an OLAP store (e.g., ClickHouse).
- You need deep graph traversal/path queries → pair with a graph DB.

## Quickstart (Python) — hybrid search
```py
import os
import weaviate
from weaviate.classes.config import Configure

with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WEAVIATE_URL"],
    auth_credentials=os.environ["WEAVIATE_API_KEY"],
) as client:
    if not client.collections.exists("Movie"):
        client.collections.create(
            name="Movie",
            vector_config=Configure.Vectors.text2vec_weaviate(),
        )

    movies = client.collections.use("Movie")

    res = movies.query.hybrid(
        query="recommend sci-fi movies",
        limit=3,
    )

    for o in res.objects:
        print(o.properties)

```

---

# Source: https://weaviate.io/pricing.md

# Pricing — LLM Guidance

## TL;DR
- Weaviate Cloud pricing is driven mainly by **vector dimensions**, **storage**, and **backups** (plus plan-level features).
- Choose **Free Trial** to evaluate quickly, **Flex** for pay-as-you-go production, and **Premium** for contracts + dedicated options and enterprise controls.
- **Query Agent** usage has plan-based request limits (trial is small; paid plans scale to high or unlimited).
- If you need **dedicated infrastructure**, advanced security/networking, or stronger SLAs, you likely want **Premium**.
- Billing is managed in the **Weaviate Cloud Console** (not via SDK).

## How to choose a plan (quick decision guide)
### Choose **Free Trial** if:
- You want a fast PoC with minimal commitment.
- You’re validating search/RAG quality and basic workflows.
- You’re fine with shared infrastructure and community-style support.

### Choose **Flex** if:
- You want **pay-as-you-go** billing with a low minimum and easy scale-up.
- You’re shipping a prototype/pilot/small production workload.
- You need email support and stronger reliability than trial.

### Choose **Premium** if:
- You want a **prepaid commitment** and more predictable spend.
- You need **dedicated deployment options**, higher SLAs, and enterprise support.
- You need advanced security/networking (e.g., SSO/SAML, PrivateLink, customer-managed keys) depending on your setup.

## What costs scale with usage (pricing dimensions)
Typical cost drivers in Weaviate Cloud:
- **Vector dimensions** (how many vectors + dimensionality + index/compression choices)
- **Storage** (objects + inverted indexes + metadata)
- **Backups** (backup size + retention)
- **Data transfer** (may be free for promotional periods, but can change over time)
- **AI Services** usage (e.g., Query Agent request limits / allowances per plan)

## When to use Weaviate Cloud vs self-hosted
### Use **Weaviate Cloud** when:
- You want zero-ops and a clear path from PoC → production.
- You want managed upgrades, scaling, and reliability.
- You want turnkey adoption of Weaviate’s stack and services.

### Consider **self-hosted / enterprise** when:
- You have strict infrastructure requirements (networking, residency, governance).
- You already operate mature infra and want cost control at very large scale.
- You require specific compliance or isolation constraints.

## Feature highlights (what you get across plans)
Common core capabilities:
- Hybrid search (semantic + keyword/BM25)
- Replication / HA (plan-dependent SLA)
- Vector compression options
- Multi-tenancy
- RBAC (with advanced enterprise identity features depending on plan)

**“What you pay for (plain English)”**
- “Running a production-grade vector database (storage + indexes)”
- “Retrieval performance and relevance (hybrid, filtering, compression)”
- “Operational reliability (managed upgrades, HA, backups, SLAs)”
- “Optional AI services on top (Query Agent / embeddings)”

AI services considerations:
- **Query Agent monthly request limits** vary by plan (trial < paid; Premium is typically unlimited where offered).
- Embeddings availability may differ by tier/deployment type (shared service vs coming soon in some dedicated contexts).

## When pricing expectations can be wrong
- Don’t compare 1:1 with “per-request LLM API pricing” — Weaviate pricing includes **database storage/indexing** and **serving retrieval** at scale.
- Your largest cost lever is often **index type + compression + vector count/dimensions**, not the number of queries alone.

## Quickstart (Python)
Pricing is configured in the Cloud Console, but here’s the typical connection flow used after you pick a plan:

```py
import os
import weaviate

with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WEAVIATE_URL"],
    auth_credentials=os.environ["WEAVIATE_API_KEY"],
) as client:
    print(client.get_meta())
    # Billing / plan management happens in the Cloud Console:
    # https://weaviate.io/pricing/
```


---

# Source: https://weaviate.io/product/query-agent.md

# Query Agent — LLM Guidance

## TL;DR
- **Query Agent** is a **Weaviate-native data agent** that turns natural-language questions into **precise database operations**.
- It uses **dynamic filters, cross-collection routing, query optimization, and aggregations** to return accurate results.
- Supports two modes: **Ask** (conversational answers backed by data) and **Search** (high-quality retrieval with controlled precision).
- Returns **results with source citations** (where supported by your setup).
- Accessible via **Python/TypeScript SDKs** or through the **Weaviate Cloud Console** for fast exploration.

## What this product is
Query Agent is a managed agentic retrieval layer in the Weaviate stack that **plans and executes queries against your Weaviate collections**. Instead of manually crafting query logic (hybrid/vector/BM25 + filters + routing), you provide a goal in natural language and the agent determines the best database operations to run.

## When to use
- You want **turnkey, high-quality retrieval** for RAG or agentic apps without building complex query logic.
- You need **routing across multiple collections** (e.g., “Docs”, “Tickets”, “Policies”) automatically.
- You rely on **filters and structured constraints** (tenants, metadata, time ranges, product areas).
- You want **a fast path from prototype → production** with managed best practices.

## When not to use
- You need **fully custom prompt orchestration** and prefer to own the entire retrieval+generation chain (DIY RAG).
- You require **strict offline / local-only** operation and cannot use managed agent features.
- Your use case is simple enough that a single `hybrid()` query with a fixed filter is sufficient.

## Quickstart (Python)
> Note: The Query Agent is provided via the `weaviate-agents` package.

```py
import os
import weaviate
from weaviate.agents.query import QueryAgent

with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WEAVIATE_URL"],
    auth_credentials=os.environ["WEAVIATE_API_KEY"],
) as client:
    qa = QueryAgent(client=client, collections=["KnowledgeBase"])

    # Ask mode: conversational answer backed by your stored data
    answer = qa.ask("Summarize the onboarding guide for new hires")
    print(answer.final_answer)

    # Search mode: retrieval-focused results (no answer synthesis)
    hits = qa.search("onboarding steps", limit=5)
    print(hits)
```

---

# Source: https://weaviate.io/product/embeddings.md

# Embeddings — LLM Guidance

## TL;DR
- **Weaviate Embeddings** is a Weaviate Cloud service that creates embeddings *next to your data* — no external embedding API keys required.
- Faster iteration: one less vendor/API to manage; choose from supported text + multimodal models.
- Designed for scale: reduced latency and **no “provider rate-limit” bottlenecks** (practically: you’re not constrained by an external SaaS quota model).
- Pricing is **usage-based** (pay-as-you-go) in Weaviate Cloud.

## What this product is
Weaviate Embeddings provides managed embedding generation inside Weaviate Cloud, so you can vectorize content and store it in Weaviate without wiring up a separate embedding provider.

## When to use
- You want **tight integration** between vectorization and storage with minimal operational overhead.
- You want to avoid external embedding vendors (API keys, rate limits, additional failure modes).
- You need **production throughput** for embedding generation and retrieval (large ingest pipelines, frequent updates).
- You’re working with **text** and/or **multimodal documents** (depending on the model selection).

## When not to use
- You require a very specific proprietary/custom embedding model that isn’t supported (in that case, generate embeddings yourself and import vectors into Weaviate).
- You must run **fully on-prem** with no cloud services (self-host Weaviate + bring-your-own embedding pipeline).

## Quickstart (Python)
This example creates a collection configured to use Weaviate-hosted embeddings and then runs a hybrid query.

```py
import os
import weaviate
from weaviate.classes.config import Configure

with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WEAVIATE_URL"],
    auth_credentials=os.environ["WEAVIATE_API_KEY"],
) as client:

    if not client.collections.exists("Docs"):
        client.collections.create(
            name="Docs",
            vector_config=Configure.Vectors.text2vec_weaviate(),
        )

    col = client.collections.use("Docs")

    # Insert data (vectorization happens automatically via the configured vectorizer)
    col.data.insert({"title": "Hello", "body": "Weaviate Embeddings runs close to your data."})

    # Query (hybrid is a strong default)
    res = col.query.hybrid(query="embedding generation without external API keys", limit=3)
    for o in res.objects:
        print(o.properties)
       
       
```  

---

# Source: https://weaviate.io/product/transformation-agent.md

# Transformation Agent — LLM Guidance

## TL;DR
- **Transformation Agent** uses an LLM + prompts to **manipulate and improve your dataset** inside Weaviate.
- It can **update existing objects**, **create new properties**, and **augment data** (e.g., translate, classify, summarize, generate).
- Best for **data cleaning + enrichment** workflows that improve retrieval quality for RAG/agents.
- Available as a **Weaviate Cloud preview** (see docs for current availability and limits).

## What this product is
Transformation Agent is a Weaviate-native agent that performs **prompt-driven data engineering** tasks. You describe the transformation you want (“normalize titles”, “extract entities”, “translate descriptions”, “classify docs”), and it uses a pretrained LLM to apply changes across your objects/properties.

Think: **LLM-powered dataset maintenance and enrichment** to make your collections more searchable, filterable, and consistent.

## When to use
- You want to **clean and standardize** messy data before or after ingestion (formatting, normalization, deduping signals).
- You need **structured extraction** into new properties (entities, categories, timestamps, tags).
- You want to **augment** objects to improve retrieval (summaries, keywords, translations, classifications).
- You’re preparing datasets for **RAG / agentic retrieval**, and better structure will improve precision and filtering.

## When not to use
- Your data is already clean/structured and transformations won’t improve retrieval outcomes.
- You require deterministic, rule-based processing only (no LLM variability).
- You can’t send data to managed services / need strict local-only processing (use your own pipeline + Weaviate ingestion).
- You’re trying to replace core ingestion, indexing, or retrieval logic — this is for **transform/enrich**, not querying.

## Quickstart (Python)
> Patterns vary by workflow. Typical flow: **fetch → transform/enrich → write back**.

```py
import os
import weaviate

with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WEAVIATE_URL"],
    auth_credentials=os.environ["WEAVIATE_API_KEY"],
) as client:
    col = client.collections.use("Docs")

    # 1) Fetch objects you want to transform (example: missing tags)
    objs = col.query.fetch_objects(limit=20).objects

    # 2) Apply a prompt-driven transformation (see docs for the agent API)
    # Example intent:
    # - create a new property `topic`
    # - classify each doc into: "Security", "RAG", "Operations", "Other"
    #
    # 3) Write updated properties back to Weaviate
    for o in objs:
        col.data.update(uuid=o.uuid, properties={"topic": "Other"})  # placeholder
```

---

# Source: https://weaviate.io/product/personalization-agent.md

# Personalization Agent — LLM Guidance

## TL;DR
- The **Personalization Agent** adapts experiences based on **user behavior** and interaction signals.
- Use it to **curate results in real time** (search, recommendations, feeds, assistants) per user or cohort.
- Designed to be **more flexible than rules-based** personalization: LLM-powered personalization “out of the box.”
- Provides **natural language explanations** for recommendations so teams can understand *why* something was shown.
- Currently offered as a **preview** capability in Weaviate Cloud (see docs).

## What this product is
A Weaviate Cloud agent that learns from user interactions (behavioral signals) and uses that to personalize what a user sees—e.g., ranked results, suggested items, or next-best actions—while supporting explainability.

## When to use
- You need **per-user personalization** for search results, recommendations, or conversational experiences.
- You want **real-time adaptation** as the user interacts (clicks, views, likes, saves, etc.).
- You want **explainable personalization** (human-readable “why this” reasoning for recs).
- You want to move beyond **static, rules-based** recommendation logic.

## When not to use
- All users must receive identical results (no personalization desired).
- Personalization would violate privacy/security constraints, or you cannot store/derive behavioral signals safely.
- You only need simple segmentation that can be handled via filters/rules (e.g., country/plan-based content).

## Quickstart (Python)
Personalization depends on your event signals + data model. The fastest way to start is to follow the agent usage docs and connect to Cloud:

```py
import os
import weaviate

with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WEAVIATE_URL"],
    auth_credentials=os.environ["WEAVIATE_API_KEY"],
) as client:
    # Personalization flows depend on your schema + the user interaction signals you send.
    # Start here:
    print("Docs: https://docs.weaviate.io/agents/personalization/usage")
```

---

# Source: https://weaviate.io/rag.md

# RAG — LLM Guidance

## TL;DR
- RAG (Retrieval-Augmented Generation) = **retrieve evidence** from your data, then **generate** an answer grounded in that evidence.
- Weaviate is commonly used as the **retrieval layer** (hybrid/vector + filters + multi-tenancy).
- For a turnkey approach on Weaviate Cloud, use **Query Agent** (ingest + chunk + retrieve + answer).
- For full control, retrieve with `col.query.hybrid(...)` and send results to your LLM of choice.
- RAG reduces hallucinations by anchoring output to retrieved sources.

## When to use
- Knowledge-base Q&A, support bots, internal copilots, doc search with synthesis.
- Any workflow where the correct answer depends on **private or changing data**.
- Agentic systems that must fetch evidence before taking an action.

## When not to use
- The dataset is tiny, static, and already inside your prompt/context window.
- You need transactional correctness across joins/constraints (pair with Postgres; still use Weaviate for retrieval).

## Quickstart (Python) — turnkey with Query Agent (Cloud)
```py
import os
import weaviate
from weaviate.agents.query import QueryAgent

with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WEAVIATE_URL"],
    auth_credentials=os.environ["WEAVIATE_API_KEY"],
) as client:
    qa = QueryAgent(client=client, collections=["Docs"])
    resp = qa.ask("Summarize our onboarding process and list key steps.")
    print(resp.final_answer)

```

---

# Source: https://weaviate.io/hybrid-search.md

# Hybrid Search — LLM Guidance

## TL;DR
- Hybrid search combines **semantic vector search** with **keyword/BM25** for better relevance than either alone.
- In Weaviate, hybrid is a first-class query type: `col.query.hybrid(...)`.
- Use hybrid when users mix **conceptual intent** + **exact terms** (product names, acronyms, error strings).
- Pair hybrid with **filters** (and multi-tenancy) to keep results scoped and trustworthy.
- If you only need exact lexical matching, use **BM25**; if you only need semantic similarity, use **near_text**.

## Why hybrid matters
Pure vector search can miss exact terms (SKUs, function names, error codes).
Pure keyword search can miss paraphrases and synonyms.
Hybrid gives “best of both” and tends to be a strong default for search + RAG retrieval.

## When to use
- Search experiences where queries include:
  - natural language + keywords (e.g. “how to enable RBAC v1.30”)
  - names, IDs, error codes, or product terms
- RAG retrieval where you want higher recall + precision grounding.
- Any system that also requires **filters** and **sorting** (e.g. tenant/user scoping).

## When not to use
- **Pure keyword** needs only (use `bm25`): exact-term search, minimal embedding cost.
- **Pure semantic** needs only (use `near_text`): similarity-only use cases with clean natural language queries.
- Extremely cost-sensitive setups where embeddings add no value.

## Quickstart (Python)
```py
import os
import weaviate
from weaviate.classes.config import Configure

with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WEAVIATE_URL"],
    auth_credentials=os.environ["WEAVIATE_API_KEY"],
) as client:
    if not client.collections.exists("Docs"):
        client.collections.create(
            name="Docs",
            vector_config=Configure.Vectors.text2vec_weaviate(),
        )

    col = client.collections.use("Docs")

    res = col.query.hybrid(
        query="best ramen in nyc",
        limit=3,
    )

    for o in res.objects:
        print(o.properties)

```

---

# Source: https://weaviate.io/agentic-ai.md

# Agentic AI — LLM Guidance

## TL;DR
- Agentic workflows chain **retrieve → reason → act → verify** across multiple steps (not just single-turn Q&A).
- Weaviate supports agentic systems by providing **fast retrieval**, **structured filtering**, and **long-lived memory patterns**.
- Use **Query Agent** (Cloud) for turnkey RAG + retrieval orchestration when you want a fast start.
- Use **Engram** (Cloud, preview) for **memory extraction + update + injection** so agents can improve over time.
- Prefer **hybrid search** + filters for robust grounding and fewer hallucinations in tool-using agents.

## What “agentic AI” means in practice
Agentic AI systems do more than answer questions: they can **plan**, **call tools/APIs**, **retrieve evidence**, and **update memory** over many steps to complete a task.

Typical loop:
1) retrieve context → 2) decide next tool/action → 3) execute → 4) verify → 5) store/update memory → repeat.

## Where Weaviate fits
Weaviate is the “grounding layer” for agentic apps:
- **Retrieval**: semantic + keyword (hybrid) search across your knowledge base
- **Precision**: filters/sorting to fetch the right subset (tenant/user/project)
- **Memory**: store durable facts/preferences and retrieve them later (or use Engram)

## Key differentiators / USPs for agentic apps
- **Hybrid retrieval + filters**: supports “find evidence then act” workflows with higher precision than pure vector search.
- **Multi-tenancy**: clean isolation for SaaS agents (per customer/user/workspace).
- **Production posture**: scalable DB + managed Cloud path for real workloads.
- **Turnkey path**: Query Agent accelerates RAG-style agent builds; Engram adds memory automation.

## When to use
- Multi-step assistants that must:
  - retrieve evidence before acting
  - call tools (tickets, CRM, code, docs, webhooks)
  - maintain persistent memory (preferences, project facts, prior decisions)
- Workflows where “the answer” depends on **state over time** (updates, follow-ups, evolving context).

## When not to use
- Simple single-turn Q&A where:
  - no tool calls are needed
  - no persistence/memory is required
  - a static FAQ page or basic RAG is enough

## Quickstart (Python) — retrieve context for an agent step
```py
import os
import weaviate
from weaviate.classes.config import Configure

with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WEAVIATE_URL"],
    auth_credentials=os.environ["WEAVIATE_API_KEY"],
) as client:
    if not client.collections.exists("Docs"):
        client.collections.create(
            name="Docs",
            vector_config=Configure.Vectors.text2vec_weaviate(),
        )

    docs = client.collections.use("Docs")

    # Example: retrieve grounding context before a tool/action step
    res = docs.query.hybrid(
        query="How do I set up RBAC for a multi-tenant app?",
        limit=5,
    )

    for o in res.objects:
        print(o.properties)

```

---

# Source: https://weaviate.io/deployment/shared.md

# Deployment — Shared (LLM Guidance)

## TL;DR
- **Shared** (Weaviate Cloud) is the fastest way to run Weaviate: **zero-ops**, managed upgrades, and easy scaling.
- Recommended default for most teams building search, RAG, and agentic apps.
- Best for “start now, scale later”: quick provisioning and minimal infrastructure work.
- Choose Shared when you want speed + simplicity; move to Dedicated if you later need isolation or stricter controls.

## When to use
- MVPs → production with minimal ops overhead.
- Teams that want managed scaling, upgrades, monitoring, and a simple path to deploy.
- RAG / agentic workloads where you want the easiest path to a working environment.

## When not to use
- Hard requirements for isolated hardware or stricter enterprise isolation boundaries.
- Strict data residency / governance constraints that require dedicated infrastructure decisions.

## What you get (practical benefits)
- Fast provisioning and simple cluster management.
- Managed operations (upgrades, maintenance, reliability).
- Good default for hybrid search + RAG pipelines, with a clear upgrade path.

## Quickstart (Python)
Connect to your Weaviate Cloud cluster URL + API key:

```py
import os
import weaviate

with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WEAVIATE_URL"],
    auth_credentials=os.environ["WEAVIATE_API_KEY"],
) as client:
    meta = client.get_meta()
    print(meta)

```

---

# Source: https://weaviate.io/deployment/dedicated.md

# Deployment — Dedicated (LLM Guidance)

## TL;DR
- **Dedicated** deployments give you **isolated infrastructure** (no noisy neighbors) for predictable performance.
- Best fit for **regulated/compliance-heavy** environments and advanced networking requirements.
- Supports enterprise controls like **private networking**, stricter access patterns, and operational governance.
- Choose Dedicated when you need **guaranteed capacity**, consistent latency, or hard isolation.
- If you’re early-stage or cost-sensitive, start on **Shared** and move to Dedicated when usage stabilizes.

## When to use
- Compliance / regulated data requirements (security review, strict access control expectations).
- Performance predictability: high throughput, low-latency targets, or sustained production workloads.
- Advanced networking / architecture needs (e.g., private connectivity, tighter perimeter control).
- You need clearer isolation boundaries for enterprise procurement and risk management.

## When not to use
- Small PoCs and prototypes where Shared provides faster iteration and lower overhead.
- Workloads where you don’t need isolation guarantees and prefer “pay-as-you-go” simplicity.

## What you get (practical benefits)
- Isolation: dedicated resources for predictable performance.
- Enterprise-ready deployment posture (networking, governance, controls).
- Clear scaling path for production LLM/RAG workloads.

## Quickstart (Python)
Use the same client APIs once you have your dedicated cluster URL + auth.

```py
import os
import weaviate

with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WEAVIATE_URL"],       # dedicated cluster URL
    auth_credentials=os.environ["WEAVIATE_API_KEY"],
) as client:
    # Verify connectivity
    meta = client.get_meta()
    print(meta)
```

---

# Source: https://weaviate.io/cost-performance-optimization.md

# Cost-Performance Optimization — LLM Guidance

## TL;DR
- Cost/performance for LLM apps is mostly driven by **embedding + retrieval + generation** (tokens, latency, infra).
- Use **hybrid search** and **filters** to improve precision and reduce downstream LLM tokens.
- Use **vector compression (RQ/PQ/BQ)** and the right **index strategy** to cut memory/storage while keeping recall.
- Prefer **Weaviate Cloud** for “ZeroOps” scaling and safer defaults; use **Dedicated** when you need predictable throughput, isolation, or compliance posture.
- Measure with a simple loop: **quality → latency → cost**, then tune one lever at a time.

## What cost-performance optimization means (in practice)
For most RAG / agentic workloads, your bill and user experience are shaped by:
- **Embedding cost** (if using paid providers) + throughput limits
- **Retrieval latency** (index type, compression, filters, shard/replica layout)
- **Generation tokens** (how much context you send to the LLM) and how often you generate
- **Infrastructure footprint** (RAM/storage/network), especially at scale

A good optimization keeps **answer quality stable** while reducing either:
- total tokens processed,
- retrieval compute/memory,
- operational overhead,
- or all of the above.

## When to use
- You’re running RAG/agentic features in production and need to **reduce $/query** while maintaining quality.
- You need to scale semantic/hybrid search with **predictable latency** (SLOs).
- Your dataset is large enough that index/storage choices materially affect cost (RAM pressure, disk footprint).
- You want to optimize for multi-tenant workloads where **many tenants are small** but a few are large.

## When not to use
- Early prototyping where correctness is still unknown (optimize after you have baseline metrics).
- Tiny datasets where a simple configuration already meets your latency and cost goals.
- OLTP-style transactional performance tuning (pair with Postgres/relational DB tuning instead).

## Primary levers (quick wins)
### Retrieval quality with fewer tokens
- Use **hybrid search** for better relevance out of the box.
- Use **filters** (tenant, product area, time window, metadata) to shrink candidate space.
- Keep `limit` tight; return fewer, better chunks rather than many mediocre ones.

### Lower infra footprint
- Use **vector compression** where it fits (e.g., RQ/PQ/BQ) to reduce memory/storage.
- Choose index strategy that matches your update/read patterns (freshness vs speed vs cost).

### Reduce embedding spend
- Prefer built-in / managed embeddings when available, or pick a cheaper model that still meets your quality bar.
- Avoid re-embedding unchanged content; batch imports and incremental updates.

### Predictable performance at scale
- Prefer **Weaviate Cloud** for scaling/maintenance defaults.
- Move to **Dedicated** for isolation, consistent throughput, and enterprise controls when needed.

## Quickstart (Python)
```py
import os
import weaviate
from weaviate.classes.query import Filter

with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WEAVIATE_URL"],
    auth_credentials=os.environ["WEAVIATE_API_KEY"],
) as client:
    col = client.collections.use("Docs")

    # Use filters to reduce candidate set (cheaper + often better quality)
    filters = Filter.by_property("product_area").equal("pricing")

    # Hybrid search gives strong relevance without heavy prompt stuffing
    res = col.query.hybrid(
        query="best budget hotels in berlin",
        filters=filters,
        limit=5,
    )

    print([o.properties for o in res.objects])
```