# Cloud Graph Database Decision Guide

A practical guide to selecting the right managed graph database for your use case.

## Quick Decision Tree

```
START
  ↓
[Using AWS?] ──Yes→ [Need SPARQL/Semantic?] ──Yes→ Neptune
  ↓ No                    ↓ No
  ↓                       └→ Neptune (Gremlin preferred)
[Using Azure?] ──Yes→ [Need multi-model?] ──Yes→ Cosmos DB
  ↓ No                    ↓ No
  ↓                       └→ Cosmos DB (Gremlin) or Neptune via partner
[Using GCP?] ──Yes→ [Petabyte scale + SQL compatibility?] ──Yes→ Spanner Graph
  ↓ No                    ↓ No
  ↓                       └→ BigQuery Graph Analytics
[Cloud agnostic] ──Yes→ [GraphQL-first?] ──Yes→ Dgraph Cloud
                          ↓ No
                          ↓
                    [Query type?] ──Analytics on billions edges→ TigerGraph
                          ↓
                          ├→ Relationship queries (OLAP) → Neo4j AuraDB
                          │
                          ├→ Large distributed graphs → NebulaGraph
                          │
                          ├→ Mixed model (docs+graphs) → ArangoDB
                          │
                          ├→ Microsecond latency → Redis
                          │
                          └→ RDF/Semantic → GraphDB or RDFox
```

## Use Case Matrix

### Use Case: Real-Time Recommendations & Personalization

| Requirement | Best Choice | Alternative | Avoid |
|-------------|-------------|-------------|-------|
| **Scale** | <100M users | Neo4j AuraDB | TigerGraph (if budget conscious) | FaunaDB |
| **Scale** | >100M users | TigerGraph | NebulaGraph | Neptune (write bottleneck) |
| **Latency** | Sub-second critical | TigerGraph, Redis | NebulaGraph | - |
| **Cloud** | AWS | Neptune with custom scoring | TigerGraph | - |
| **Cloud** | Azure | Cosmos DB | TigerGraph on Azure | - |
| **Cloud** | GCP | Spanner Graph + Vertex AI | BigQuery Graph | - |

**Rationale**: Personalization requires fast graph traversal (TigerGraph excels), but can also use Neo4j for medium scale, or Redis for ultra-low latency if dataset fits in RAM.

---

### Use Case: Fraud Detection

| Requirement | Best Choice | Alternative | Avoid |
|-------------|-------------|-------------|-------|
| **Ring Analysis** | TigerGraph | NebulaGraph | Cosmos DB |
| **Money Laundering Patterns** | TigerGraph (pattern matching) | Neptune (SPARQL) | Redis |
| **Real-Time Scoring** | TigerGraph + Redis | NebulaGraph | Neo4j (slower for complex patterns) |
| **Compliance Reporting** | Neptune (SPARQL inference) | Spanner Graph | - |
| **AWS Native** | Neptune (edge ingestion) | TigerGraph on AWS | - |

**Rationale**: Fraud detection benefits from GSQL pattern matching (TigerGraph) for complex rings, or SPARQL inference (Neptune) for regulatory reasoning. Real-time scoring favors TigerGraph's MPP engine.

---

### Use Case: Knowledge Graphs & Master Data Management

| Requirement | Best Choice | Alternative | Avoid |
|-------------|-------------|-------------|-------|
| **Semantic Inference** | GraphDB (RDFox if speed critical) | Neptune (SPARQL) | Dgraph |
| **Entity Consolidation** | Neptune or Neo4j | ArangoDB | Cosmos DB |
| **Large Scale (1B+ entities)** | NebulaGraph | Neptune | - |
| **Multi-Tenant Isolation** | Neptune (IAM per graph) | Neo4j Aura (Enterprise) | Cosmos DB (shared RUs) |
| **RDF/OWL Ontologies** | GraphDB, RDFox | Neptune | All others |

**Rationale**: Knowledge graphs typically require inference (RDF platforms) or entity-centric queries (Neptune/Neo4j). Large-scale MDM favors distributed platforms like NebulaGraph.

---

### Use Case: Social Network / Community Detection

| Requirement | Best Choice | Alternative | Avoid |
|-------------|-------------|-------------|-------|
| **Billions of Users** | NebulaGraph | TigerGraph | Neptune |
| **Community Detection Algorithms** | TigerGraph (pre-built) | Neo4j (GDS library) | - |
| **Real-Time Friend Feeds** | Redis or Neo4j | NebulaGraph | - |
| **Analytics on User Graph** | TigerGraph, NebulaGraph | Neo4j | - |
| **AWS Native** | Neptune | NebulaGraph | - |

**Rationale**: Social networks require massive distribution (NebulaGraph) for billions of users, combined with algorithm libraries (TigerGraph, Neo4j) for community analysis.

---

### Use Case: Supply Chain & Logistics Networks

| Requirement | Best Choice | Alternative | Avoid |
|-------------|-------------|-------------|-------|
| **Hierarchical Data (multi-level)** | Spanner Graph | ArangoDB | Dgraph |
| **Real-Time Route Optimization** | TigerGraph, NebulaGraph | Neo4j | - |
| **GCP Native with BigQuery** | Spanner Graph | - | - |
| **Cross-Border Compliance** | Cosmos DB (multi-region) | Spanner Graph | - |
| **Hybrid Documents + Graphs** | ArangoDB | Cosmos DB | - |

**Rationale**: Supply chains benefit from strong consistency (Spanner Graph) and hierarchical queries, combined with routing optimization (TigerGraph for compute-intensive algorithms).

---

### Use Case: API-First Development (GraphQL)

| Requirement | Best Choice | Alternative | Avoid |
|-------------|-------------|-------------|-------|
| **Native GraphQL** | Dgraph Cloud | FaunaDB | All others |
| **Rapid Schema Development** | Dgraph | FaunaDB | - |
| **Real-Time Subscriptions** | Dgraph | None | - |
| **Serverless GraphQL API** | FaunaDB | - | - |
| **GraphQL-over-REST** | Neo4j (Apollo integration) | ArangoDB | - |

**Rationale**: Pure GraphQL-first applications choose Dgraph for native support. Serverless teams prefer FaunaDB. Teams with existing REST APIs often retrofit Neo4j with Apollo.

---

### Use Case: Real-Time Analytics Dashboard

| Requirement | Best Choice | Alternative | Avoid |
|-------------|-------------|-------------|-------|
| **Sub-second response** | TigerGraph, NebulaGraph | Redis | Neptune |
| **Billions of events** | TigerGraph, BigQuery Graph | - | - |
| **GCP + Visualization** | Spanner Graph + Data Studio | BigQuery Graph | - |
| **AWS + Visualization** | Neptune + QuickSight | NebulaGraph | - |
| **Custom Dashboards** | TigerGraph + Grafana | NebulaGraph | - |

**Rationale**: Real-time analytics favors compute-optimized platforms (TigerGraph, NebulaGraph) with cloud-native visualization tools.

---

## Cost-Performance Comparison by Scale

### Small Graphs (<1M nodes)

**Best Options**:
1. Neo4j AuraDB Free ($0) → Professional ($65-150)
2. Dgraph Free → Paid
3. Redis Enterprise ($7-15)

**Why**: Entry costs are critical; free tiers and small monthly commitments preferred.

---

### Medium Graphs (1M - 1B nodes)

**Best Options**:
1. Neo4j AuraDB Professional ($150-500)
2. NebulaGraph Standard ($100-500)
3. Cosmos DB Provisioned (variable, typically $200-1000)

**Why**: Balanced cost and features. Transparent pricing (NebulaGraph) vs. RU-based (Cosmos DB) trade-offs.

---

### Large Graphs (1B - 100B nodes)

**Best Options**:
1. TigerGraph Cloud (usage-based, typically $1000+)
2. NebulaGraph Professional ($500-2000)
3. Neptune Multi-AZ ($1000+)

**Why**: Specialized engines (TigerGraph) or distributed platforms (NebulaGraph) justify higher costs through performance at scale.

---

### Massive Graphs (100B+ nodes / Trillion+ edges)

**Only Viable Options**:
1. TigerGraph (MPP optimization for analytics)
2. NebulaGraph (distributed architecture)
3. Spanner Graph (petabyte-scale relational)

**Why**: Only these platforms designed for true massive scale. Others hit write/consistency bottlenecks.

---

## Language & Developer Experience Preference

### Team Familiar with SQL

**Best Fit**:
1. Spanner Graph (SQL + graph extensions)
2. ArangoDB (AQL, SQL-like)
3. Neptune (SPARQL for semantic)

---

### Team Familiar with Gremlin

**Best Fit**:
1. Neptune (native Gremlin)
2. Cosmos DB (Gremlin API)
3. TinkerpopJVM users → TigerGraph (GSQL as natural extension)

---

### Team Familiar with Cypher

**Best Fit**:
1. Neo4j AuraDB (native Cypher)
2. Redis (Cypher on Redis)
3. Dgraph (DQL as alternative)

---

### Team Familiar with GraphQL

**Best Fit**:
1. Dgraph Cloud (native GraphQL)
2. FaunaDB (GraphQL API generation)
3. Neo4j (Apollo federation integration)

---

### Team Prefers Proprietary Language (Performance Over Learning)

**Best Fit**:
1. TigerGraph (GSQL with procedural logic)
2. NebulaGraph (nGQL SQL-like)
3. ArangoDB (AQL unified)

---

## Multi-Cloud & Vendor Lock-in Considerations

### Cloud-Agnostic Platforms

| Platform | AWS | Azure | GCP | On-Prem |
|----------|-----|-------|-----|---------|
| Neo4j AuraDB | ✓ | ✓ | ✓ | ✓ (Enterprise) |
| TigerGraph Cloud | ✓ | ✓ | ✗ (Kubernetes) | ✓ |
| NebulaGraph Cloud | ✓ | ✓ | ✗ | ✓ |
| ArangoDB Oasis | ✓ | ✓ | ✓ | ✓ |
| Dgraph Cloud | ✓ | ✓ | ✗ (Limited) | ✓ |
| FaunaDB | ✓ | ✗ | ✗ | ✗ |

**Recommendation**: If multi-cloud is priority, choose Neo4j AuraDB or ArangoDB for maximum platform coverage.

---

## SLA & Enterprise Requirements

| Requirement | Neptune | Cosmos DB | Spanner | Neo4j Enterprise | TigerGraph Enterprise |
|-------------|---------|-----------|---------|------------------|----------------------|
| **99.99% SLA** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **99.999% SLA** | With Multi-AZ | With Multi-region | ✓ | Enterprise | Enterprise |
| **SOC 2 Compliance** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **HIPAA Compliance** | ✓ | ✓ | ✓ | ✓ | Limited |
| **FedRAMP** | ✓ (AWS GovCloud) | ✓ (Azure Gov) | ✓ (GCP FedRAMP) | Limited | Limited |
| **Private Endpoint** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **BYOK (Bring Your Own Key)** | ✓ | ✓ | ✓ | Enterprise | Limited |

**Recommendation**: Heavily regulated industries (finance, healthcare) should choose cloud provider's native offerings (Neptune, Cosmos DB, Spanner) or Neo4j Enterprise.

---

## Integration Ecosystem

### AWS Integration

**Best**: Neptune
- CloudWatch integration
- Lambda for custom processing
- Kinesis for streaming
- SageMaker for ML
- Glue for ETL
- EventBridge for events

**Second**: TigerGraph on AWS or NebulaGraph via AWS Marketplace

---

### Azure Integration

**Best**: Cosmos DB
- Azure Synapse Link
- Azure OpenAI integration
- Copilot integration
- Azure Cognitive Search
- Logic Apps for workflows
- Power BI for visualization

**Second**: ArangoDB or NebulaGraph via Azure Marketplace

---

### GCP Integration

**Best**: Spanner Graph
- Vertex AI for ML
- BigQuery for analytics
- Dataflow for ETL
- Cloud Run for serverless
- Looker for visualization

**Second**: NebulaGraph (limited GCP integration)

---

## Testing & Proof of Concept (PoC) Guide

### Phase 1: Feature Validation (1-2 weeks)

1. **Clone production data** (sample or anonymized)
2. **Test query language** feasibility
3. **Verify scaling** assumptions (test with 10x-100x data)
4. **Measure latency** and throughput

**Tools**:
- Load generators (custom scripts)
- Query profilers (built-in to all platforms)
- Monitoring tools (cloud-native dashboards)

### Phase 2: Cost Estimation (2-4 weeks)

1. **Estimate node/edge count** with realistic growth projections
2. **Model query patterns** (read/write ratio, complexity)
3. **Calculate projected costs** for 1, 3, and 5-year horizons
4. **Compare with current spend** (legacy databases, infrastructure)

**Common Cost Drivers**:
- Storage size
- Query throughput (QPS)
- Write throughput (ingestion rate)
- Data replication/distribution
- Data transfer/egress

### Phase 3: Operational Readiness (4-8 weeks)

1. **Test disaster recovery** (backup/restore, failover)
2. **Security validation** (authentication, encryption, audit logs)
3. **Performance under load** (sustained 24/7 operations)
4. **Integration testing** with existing systems

---

## Final Checklist

- [ ] **Workload Type** identified (OLTP/OLAP/Hybrid/Streaming)
- [ ] **Scale Requirements** documented (current + 5-year projections)
- [ ] **Query Patterns** defined (traversal depth, complexity, frequency)
- [ ] **Consistency Needs** clear (strong, eventual, or configurable)
- [ ] **Cloud Provider** selected (AWS/Azure/GCP/Multi-cloud)
- [ ] **Query Language** team familiar with or willing to learn
- [ ] **Budget** estimated for 1-3 year TCO
- [ ] **Integration Ecosystem** validated with existing systems
- [ ] **SLA Requirements** met by shortlisted platforms
- [ ] **PoC Plan** established with success criteria
- [ ] **Governance & Compliance** requirements aligned
- [ ] **Vendor Support** and community resources evaluated

---

## Additional Resources

**Official Documentation**:
- [Amazon Neptune Docs](https://docs.aws.amazon.com/neptune/)
- [Azure Cosmos DB Docs](https://docs.microsoft.com/en-us/azure/cosmos-db/)
- [Google Cloud Spanner Graph Docs](https://cloud.google.com/spanner/docs/graph)
- [Neo4j AuraDB Docs](https://neo4j.com/docs/aura/)
- [TigerGraph Cloud Docs](https://www.tigergraph.com/docs/)
- [NebulaGraph Cloud Docs](https://docs.nebula-graph.io/3.0/)

**Comparative Resources**:
- Solutions Review: Best Graph Databases
- Cambridge Intelligence: Choosing a Graph Database
- PuppyGraph: Graph Database Comparisons
- G2: Graph Database Reviews

---

**Last Updated**: January 2026
