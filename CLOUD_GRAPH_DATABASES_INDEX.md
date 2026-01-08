# Cloud-Based Graph Database Research Index

Comprehensive research on managed graph database services available as of January 2026.

## Documents in This Collection

### 1. **CLOUD_GRAPH_DATABASES_2026.md** (24 KB, 578 lines)
Complete technical reference covering all major managed graph database services.

**Contents**:
- Detailed profiles of 13+ graph database platforms
- Feature comparison matrices
- Pricing models and entry costs
- Use case alignment guidance
- Emerging trends in graph technology
- Selection criteria by workload type

**Services Covered**:
- Amazon Neptune (AWS)
- Azure Cosmos DB (Gremlin API)
- Google Cloud Spanner Graph
- Neo4j AuraDB
- TigerGraph Cloud
- NebulaGraph Cloud
- ArangoDB Oasis
- Dgraph Cloud
- Redis Enterprise Cloud (Graphs)
- Ontotext GraphDB
- RDFox
- FaunaDB

**When to Use**: Reference guide for understanding capabilities, pricing, and technical trade-offs of each platform.

---

### 2. **CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md** (13 KB, 377 lines)
Practical guide for selecting the right graph database for your specific use case.

**Contents**:
- Quick decision tree for rapid selection
- Use case matrices (real-time recommendations, fraud detection, knowledge graphs, social networks, etc.)
- Cost-performance analysis by scale (small to massive graphs)
- Query language preference guide
- Multi-cloud considerations
- SLA & enterprise requirements comparison
- Cloud integration ecosystem alignment
- PoC testing methodology
- Final checklist for implementation

**When to Use**: Use this when evaluating options for a specific project or workload. Contains practical decision trees and cost-benefit analyses.

---

### 3. **CLOUD_GRAPH_DATABASES_QUICK_REFERENCE.csv** (2.3 KB, 13 rows)
Spreadsheet-compatible comparison matrix of all platforms.

**Columns**:
- Service name
- Provider
- Supported query languages
- Deployment model
- Scalability characteristics
- Primary strength
- Pricing model
- Estimated entry cost
- Best use cases
- Multi-model support
- ACID transaction support
- Vector search capabilities

**When to Use**: Quick lookup when comparing 2-3 platforms side-by-side or creating custom analyses in spreadsheet tools.

---

## Quick Navigation

### By Cloud Provider

**AWS Users**:
- Primary: Amazon Neptune
- Alternative: TigerGraph Cloud, NebulaGraph (via Marketplace)
- See: CLOUD_GRAPH_DATABASES_2026.md → "Amazon Neptune" section

**Azure Users**:
- Primary: Azure Cosmos DB (Gremlin API)
- Alternative: ArangoDB Oasis, NebulaGraph (via Marketplace)
- See: CLOUD_GRAPH_DATABASES_2026.md → "Azure Cosmos DB" section

**Google Cloud Users**:
- Primary: Google Cloud Spanner Graph
- Secondary: BigQuery for graph analytics
- Alternative: Cloud-agnostic platforms via Kubernetes
- See: CLOUD_GRAPH_DATABASES_2026.md → "Google Cloud" sections

**Cloud-Agnostic**:
- Recommended: Neo4j AuraDB, ArangoDB, TigerGraph, NebulaGraph
- See: CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md → "Multi-Cloud Considerations"

---

### By Use Case

**Real-Time Analytics & Scoring**:
- TigerGraph Cloud or NebulaGraph
- See: CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md → "Real-Time Recommendations"

**Knowledge Graphs & Semantic Reasoning**:
- Neptune (SPARQL), GraphDB, or RDFox
- See: CLOUD_GRAPH_DATABASES_2026.md → "Specialized Graph Platforms"

**Fraud Detection**:
- TigerGraph (pattern analysis) or Neptune (network analytics)
- See: CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md → "Fraud Detection" use case

**Social Networks / Community Detection**:
- NebulaGraph (billions of users) or TigerGraph (algorithms)
- See: CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md → "Social Network" use case

**API-First Development (GraphQL)**:
- Dgraph Cloud (native) or FaunaDB (serverless)
- See: CLOUD_GRAPH_DATABASES_2026.md → "Dgraph Cloud" section

**Supply Chain & Logistics**:
- Spanner Graph (GCP) or ArangoDB (hybrid model)
- See: CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md → "Supply Chain" use case

**Master Data Management**:
- Neptune or Neo4j AuraDB
- See: CLOUD_GRAPH_DATABASES_2026.md → "Amazon Neptune" section

---

### By Query Language

**Cypher** (SQL-like, relationship-focused):
- Neo4j AuraDB (native), Redis (on Redis), Neptune (openCypher)
- See: CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md → "Team Familiar with Cypher"

**Gremlin** (traversal API):
- Neptune (native), Cosmos DB, TinkerpopJVM ecosystem
- See: CLOUD_GRAPH_DATABASES_2026.md → "Query Languages" comparison

**SPARQL** (semantic/RDF):
- Neptune (native), GraphDB, RDFox
- See: CLOUD_GRAPH_DATABASES_2026.md → "Specialized Graph Platforms"

**GraphQL** (schema-first):
- Dgraph Cloud (native), FaunaDB
- See: CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md → "Team Familiar with GraphQL"

**SQL Extensions**:
- Spanner Graph, ArangoDB (AQL)
- See: CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md → "Team Familiar with SQL"

---

### By Scale

**Small Scale (< 1M nodes)**:
- Neo4j AuraDB Free/Professional
- Dgraph Free
- Redis Enterprise ($7-15)
- See: CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md → "Small Graphs"

**Medium Scale (1M - 1B nodes)**:
- Neo4j AuraDB Professional
- NebulaGraph Standard
- Cosmos DB Provisioned
- See: CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md → "Medium Graphs"

**Large Scale (1B - 100B nodes)**:
- TigerGraph Cloud
- NebulaGraph Professional
- Neptune Multi-AZ
- See: CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md → "Large Graphs"

**Massive Scale (100B+ nodes, Trillion+ edges)**:
- TigerGraph (MPP)
- NebulaGraph (distributed)
- Spanner Graph (petabyte)
- See: CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md → "Massive Graphs"

---

### By Pricing Model

**Free/Freemium Options**:
- Dgraph Cloud (free tier)
- Neo4j AuraDB Free
- TigerGraph Cloud (limited free cluster)
- See: CLOUD_GRAPH_DATABASES_2026.md → "Pricing Model" for each

**Monthly Subscriptions** ($65-500):
- Neo4j AuraDB Professional
- NebulaGraph Standard ($36-50)
- ArangoDB Oasis ($35-50)
- See: CLOUD_GRAPH_DATABASES_QUICK_REFERENCE.csv → "Entry Cost" column

**Serverless/Pay-Per-Request**:
- Azure Cosmos DB Serverless
- Neptune Serverless
- FaunaDB
- See: CLOUD_GRAPH_DATABASES_2026.md → individual service pricing sections

**Usage-Based**:
- TigerGraph Cloud
- Dgraph Cloud
- NebulaGraph (hourly)
- See: CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md → "Cost-Performance Comparison"

---

## Key Takeaways

### Most Popular Options (2026)
1. **Neo4j AuraDB** - Developer experience, relationship queries, multi-cloud
2. **Amazon Neptune** - AWS integration, semantic reasoning, established
3. **Azure Cosmos DB** - Global distribution, multi-model, enterprise SLAs
4. **TigerGraph Cloud** - Analytics at massive scale, compute-intensive workloads
5. **NebulaGraph** - Transparent pricing, distributed architecture, rapid growth

### Fastest Growing Categories
- **Vector Search Integration**: All platforms adding embedding support
- **GraphQL Native Support**: Emerging standard (Dgraph, Fauna, others)
- **Real-Time Analytics**: Sub-millisecond latencies becoming standard
- **Serverless Options**: Consumption-based pricing gaining adoption

### Common Selection Patterns
- **AWS teams** → Neptune (established) or TigerGraph (analytics)
- **Azure teams** → Cosmos DB (integrated ecosystem)
- **GCP teams** → Spanner Graph (relational scale) or BigQuery
- **Multi-cloud teams** → Neo4j AuraDB or ArangoDB
- **Performance-first** → TigerGraph (analytics) or Redis (latency)
- **Developer-first** → Neo4j AuraDB or Dgraph
- **Cost-conscious** → NebulaGraph (transparent) or free tiers

---

## How to Use This Research

### Phase 1: Initial Exploration (30 minutes)
1. Read CLOUD_GRAPH_DATABASES_2026.md → "Overview" section
2. Scan CLOUD_GRAPH_DATABASES_QUICK_REFERENCE.csv for quick comparison
3. Identify 2-3 promising platforms based on your cloud provider

### Phase 2: Requirements Matching (1-2 hours)
1. Complete checklist in CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md
2. Review relevant use case section in decision guide
3. Narrow to 2-3 final candidates

### Phase 3: Deep Dive (2-4 hours)
1. Read detailed profiles for final candidates in CLOUD_GRAPH_DATABASES_2026.md
2. Review pricing models and entry costs
3. Check multi-cloud and SLA requirements sections
4. Validate integration ecosystem alignment

### Phase 4: PoC Planning (1-2 days)
1. Reference PoC testing guide in decision guide
2. Set up trial accounts (most have free trials)
3. Load sample data, run test queries
4. Calculate projected costs for your workload

---

## Research Methodology

Data collected from:
- Official product documentation (2026)
- Cloud marketplace listings (AWS, Azure, Google Cloud)
- Perplexity AI web search with citations
- Tavily AI-powered search for current information
- Comparative analysis from industry sources (Solutions Review, DevOpsSchool, Cambridge Intelligence)
- GitHub market overviews and technical benchmarks

**Research Date**: January 2026
**Currency**: Pricing and features accurate as of January 2026
**Updates**: Recommended to verify pricing and feature details directly with vendors

---

## Related Documentation

For broader context on graph databases, see also:
- [`docs/github-scraped/`](../docs/github-scraped/) - Neo4j, TigerGraph, and other open-source graph DB docs
- [`docs/llms-txt/`](../docs/llms-txt/) - Official documentation for various platforms

---

**Questions or Updates?**
Contact: [Your organization contact info]
Last Updated: January 1, 2026
