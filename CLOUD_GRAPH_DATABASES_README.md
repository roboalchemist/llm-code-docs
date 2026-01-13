# Cloud-Based Graph Database Services Research (2026)

Comprehensive research on managed graph database offerings from AWS, Azure, Google Cloud, and independent providers.

## Quick Links

Start here based on your needs:

- **New to graph databases?** → [CLOUD_GRAPH_DATABASES_SUMMARY.txt](./CLOUD_GRAPH_DATABASES_SUMMARY.txt) (Executive overview)
- **Need to choose a platform?** → [CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md](./CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md) (Use-case matching)
- **Want complete details?** → [CLOUD_GRAPH_DATABASES_2026.md](./CLOUD_GRAPH_DATABASES_2026.md) (Full reference)
- **Comparing 2-3 options?** → [CLOUD_GRAPH_DATABASES_QUICK_REFERENCE.csv](./CLOUD_GRAPH_DATABASES_QUICK_REFERENCE.csv) (Spreadsheet)
- **Need to navigate?** → [CLOUD_GRAPH_DATABASES_INDEX.md](./CLOUD_GRAPH_DATABASES_INDEX.md) (Navigation guide)

## What's Included

This research package contains **5 comprehensive documents** analyzing **13 major managed graph database services**:

### Documents

1. **CLOUD_GRAPH_DATABASES_2026.md** (24 KB)
   - Technical reference for all 13 platforms
   - Detailed feature comparisons
   - Pricing and entry costs
   - Selection criteria by workload
   - Market trends and emerging capabilities

2. **CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md** (13 KB)
   - Quick decision tree for platform selection
   - 8 use-case scenarios with platform recommendations
   - Cost-performance analysis by scale
   - Multi-cloud and enterprise requirements
   - PoC testing methodology
   - Implementation checklist

3. **CLOUD_GRAPH_DATABASES_QUICK_REFERENCE.csv** (2.3 KB)
   - Spreadsheet-ready comparison matrix
   - All services in single table
   - Ready for Excel/Google Sheets import

4. **CLOUD_GRAPH_DATABASES_INDEX.md** (9.2 KB)
   - Navigation guide for all documents
   - Quick links by cloud provider, use case, language, scale, pricing
   - Key takeaways and selection patterns
   - How-to guide for using the research

5. **CLOUD_GRAPH_DATABASES_SUMMARY.txt** (14 KB)
   - Executive summary
   - Comprehensive service list
   - Market statistics
   - Pricing overview
   - Next steps

## Services Covered

### Cloud Provider Offerings (3)
- **Amazon Neptune** (AWS) - Knowledge graphs, semantic reasoning
- **Azure Cosmos DB** (Gremlin API) - Multi-model, global distribution
- **Google Cloud Spanner Graph** - Relational-scale, ACID consistency

### Independent Managed Services (5)
- **Neo4j AuraDB** - Developer experience, relationship queries
- **TigerGraph Cloud** - Compute-intensive analytics at massive scale
- **NebulaGraph Cloud** - Distributed architecture, transparent pricing
- **ArangoDB Oasis** - Multi-model unified language
- **Dgraph Cloud** - Native GraphQL, real-time subscriptions

### Specialized Platforms (5)
- **Redis Enterprise Cloud** (Graphs) - Microsecond latency
- **Ontotext GraphDB** - RDF/semantic reasoning
- **RDFox** - High-performance RDF reasoning
- **FaunaDB** - Serverless multi-model
- **Google Cloud BigQuery** - Petabyte-scale analytics

## Key Comparisons

### By Cloud Provider
| Provider | Best Choice | Alternative | Budget |
|----------|-------------|-------------|--------|
| AWS | Neptune | TigerGraph | $150-300/mo |
| Azure | Cosmos DB | ArangoDB | $100-200/mo |
| GCP | Spanner Graph | BigQuery | $330+/mo |
| Multi-cloud | Neo4j AuraDB | ArangoDB | $65-150/mo |

### By Use Case
| Scenario | Best Choice | Alternative |
|----------|-------------|-------------|
| Real-time recommendations | TigerGraph (scale) / Neo4j (mid) | NebulaGraph |
| Fraud detection | TigerGraph (patterns) | Neptune (analysis) |
| Knowledge graphs | Neptune (SPARQL) | GraphDB |
| GraphQL APIs | Dgraph Cloud | FaunaDB |
| Social networks | NebulaGraph | TigerGraph |
| Supply chain | Spanner Graph | ArangoDB |

### By Budget
| Budget | Options |
|--------|---------|
| Free | Neo4j Free, Dgraph Free, TigerGraph Free |
| Entry-level ($0-50/mo) | NebulaGraph, ArangoDB, Redis |
| Mid-range ($50-300/mo) | Neo4j Professional, Cosmos DB |
| Enterprise (Custom) | Neptune Multi-AZ, TigerGraph at scale |

## How to Use This Research

### Option 1: Quick Start (30 minutes)
1. Read CLOUD_GRAPH_DATABASES_SUMMARY.txt
2. Scan CLOUD_GRAPH_DATABASES_QUICK_REFERENCE.csv
3. Identify 2-3 candidates for your cloud provider

### Option 2: Structured Selection (2-3 hours)
1. Read CLOUD_GRAPH_DATABASES_2026.md introduction
2. Complete the checklist in CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md
3. Review the use case section matching your workload
4. Deep dive on top 2-3 candidates

### Option 3: Comprehensive Evaluation (4-6 hours)
1. Start with CLOUD_GRAPH_DATABASES_INDEX.md
2. Read relevant sections of CLOUD_GRAPH_DATABASES_2026.md
3. Work through CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md
4. Plan PoC testing using provided methodology

## Research Quality

- **Coverage**: 13 major platforms analyzed
- **Detail Level**: 4+ pages per major service
- **Data Sources**: Official documentation, cloud marketplaces, web search (Perplexity, Tavily), industry reports
- **Freshness**: January 2026
- **Verification**: Web-searched with citations, cross-referenced

## Key Findings

### Market Leaders (2026)
1. **Neo4j AuraDB** - Best developer experience, largest ecosystem
2. **Amazon Neptune** - AWS integration, mature platform
3. **TigerGraph Cloud** - Analytics at massive scale
4. **Azure Cosmos DB** - Multi-model, global distribution
5. **NebulaGraph** - Rapidly growing, transparent pricing

### Emerging Trends
- Vector search integration across all platforms
- Native GraphQL support (Dgraph, others)
- Serverless and consumption-based pricing growing
- Real-time analytics (sub-second) becoming standard
- Multi-region distribution as default feature

### Technology Trade-offs
- **Cypher vs. Gremlin vs. GraphQL**: Different strengths for different teams
- **Scale vs. Simplicity**: TigerGraph for massive analytics, Neo4j for balanced
- **Cost vs. Features**: Transparent pricing (NebulaGraph) vs. integrated ecosystems
- **OLTP vs. OLAP**: Different optimization priorities
- **Vendor Lock-in**: Cloud-native vs. cloud-agnostic options

## Next Steps

1. **Define Requirements**
   - Current graph size and growth projections
   - Query patterns and latency requirements
   - Budget constraints
   - Cloud provider preferences
   - Team expertise and language preferences

2. **Narrow Candidates**
   - Use decision guide for initial filtering
   - Review detailed profiles for top 2-3
   - Check integration with existing systems

3. **Proof of Concept**
   - Use free trials (available for most)
   - Load sample data (or 10-100x your actual data)
   - Run representative queries
   - Measure performance and costs

4. **Evaluate Holistically**
   - SLA and support requirements
   - Compliance and security certifications
   - Ecosystem and community support
   - Long-term roadmap alignment

## File Organization

```
/Users/joe/github/llm-code-docs/

CLOUD_GRAPH_DATABASES_*.* (5 files)
├── CLOUD_GRAPH_DATABASES_2026.md              (Technical reference)
├── CLOUD_GRAPH_DATABASES_DECISION_GUIDE.md    (Selection guide)
├── CLOUD_GRAPH_DATABASES_QUICK_REFERENCE.csv  (Comparison matrix)
├── CLOUD_GRAPH_DATABASES_INDEX.md             (Navigation)
├── CLOUD_GRAPH_DATABASES_SUMMARY.txt          (Executive summary)
└── CLOUD_GRAPH_DATABASES_README.md            (This file)
```

## Contact & Updates

Research compiled: January 1, 2026

For the most current pricing and feature information, always consult:
- [Amazon Neptune Documentation](https://docs.aws.amazon.com/neptune/)
- [Azure Cosmos DB Documentation](https://docs.microsoft.com/en-us/azure/cosmos-db/)
- [Google Cloud Spanner Documentation](https://cloud.google.com/spanner/docs/)
- [Neo4j AuraDB Documentation](https://neo4j.com/docs/aura/)
- [TigerGraph Cloud Documentation](https://www.tigergraph.com/docs/)
- [NebulaGraph Documentation](https://docs.nebula-graph.io/)

---

**Start Reading**: [CLOUD_GRAPH_DATABASES_SUMMARY.txt](./CLOUD_GRAPH_DATABASES_SUMMARY.txt)

Last Updated: January 1, 2026
