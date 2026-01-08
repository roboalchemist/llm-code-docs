# Graph Processing Frameworks Complete Index

Comprehensive index of all graph processing, analytics, and database frameworks covered in the 2025 research.

---

## Quick Index

### Distributed Graph Processing (6 frameworks)
1. [Pregel](#pregel) - Google's foundational BSP model
2. [Apache Giraph](#apache-giraph) - Open-source Pregel implementation
3. [Spark GraphX](#spark-graphx) - Graph processing on Apache Spark
4. [Plato](#plato) - High-performance distributed graph ML
5. [GraphScope](#graphscope) - Unified analytics + queries + learning
6. [PowerGraph](#powergraph) - Vertex-cut pioneer (legacy)

### Analytics Libraries (4 frameworks)
7. [NetworkX](#networkx) - Pure Python graph library
8. [igraph](#igraph) - C-based high-performance graphs
9. [graph-tool](#graph-tool) - C++ graph analysis
10. [SNAP](#snap) - (Not covered in research, but popular)

### Graph Neural Networks (2 frameworks)
11. [PyTorch Geometric](#pytorch-geometric) - GNN on PyTorch
12. [Deep Graph Library (DGL)](#deep-graph-library) - GNN training framework

### Graph Databases (5 frameworks)
13. [Neo4j](#neo4j) - Market leader, property graph DB
14. [TigerGraph](#tigergraph) - Enterprise analytics at scale
15. [Memgraph](#memgraph) - In-memory real-time DB
16. [JanusGraph](#janusgraph) - Distributed, open-source DB
17. [ArangoDB](#arangodb) - Multi-model database

### Visualization Tools (3 frameworks)
18. [Gephi](#gephi) - Network visualization & analysis
19. [Cytoscape](#cytoscape) - Biological network analysis
20. [Graphviz](#graphviz) - Automatic graph drawing

---

## Framework Profiles

### Distributed Graph Processing

#### Pregel
- **Type:** Distributed graph processing (proprietary)
- **Creator:** Google
- **Language:** Proprietary (C++ backend)
- **Model:** Bulk Synchronous Parallel (BSP)
- **Graph Size:** Web-scale (billions+)
- **Status:** Industry standard foundation
- **Open Source:** No
- **Key Innovation:** Vertex-centric message-passing model
- **Use Case:** Foundation for Giraph, GraphX, other systems
- **Links:** [Pregel: A System for Large-Scale Graph Processing](http://infolab.stanford.edu/gps/)

#### Apache Giraph
- **Type:** Distributed graph processing
- **Creator:** Apache Software Foundation
- **Language:** Java
- **Model:** Pure Pregel implementation
- **Graph Size:** 50+ billion edges
- **Performance:** 2.8-8.6x faster than GraphX
- **Status:** Production-ready
- **Open Source:** Yes (Apache License)
- **Integration:** Hadoop, HDFS, HBase
- **Key Strength:** Memory efficiency at extreme scale
- **Repository:** [apache/giraph](https://github.com/apache/giraph)
- **Best For:** Production analytics on massive graphs

#### Spark GraphX
- **Type:** Distributed graph processing
- **Creator:** Apache Spark project
- **Language:** Scala (with PySpark support)
- **Model:** Pregel API on Spark RDDs
- **Graph Size:** Up to 10 billion edges
- **Performance:** Baseline for comparison
- **Status:** Production-ready
- **Open Source:** Yes (Apache License)
- **Integration:** Native Spark, Hive, SQL
- **Key Strength:** Spark ecosystem integration, ease of use
- **Documentation:** [Spark GraphX Programming Guide](https://spark.apache.org/docs/latest/graphx-programming-guide.html)
- **Best For:** Rapid prototyping, Spark-integrated workloads

#### Plato
- **Type:** Distributed graph ML framework
- **Creator:** Tencent
- **Language:** C++ (Rust improvements)
- **Model:** Block partitioning with dual-engine communication
- **Graph Size:** Massive (single-machine memory footprint on clusters)
- **Performance:** 10x faster than Giraph/GraphX
- **Memory:** 16-116x smaller than GraphX
- **Status:** Open-source, specialized for ML
- **Open Source:** Yes
- **Key Strength:** Performance and memory efficiency
- **Repository:** [Tencent/Plato](https://github.com/Tencent/plato)
- **Best For:** Large-scale graph neural network training

#### GraphScope
- **Type:** Unified graph computing platform
- **Creator:** Alibaba
- **Language:** C++ with Python (PyGraphScope)
- **Model:** Multi-engine (GRAPE analytics, GraphIR queries, Graph-Learn ML)
- **Graph Size:** Distributed clusters (massive scale)
- **Performance:** 2.6x LDBC-SNB improvement (Flex 2024)
- **Status:** Production-ready (GraphScope Flex 2024)
- **Open Source:** Yes
- **Components:**
  - GRAPE: Analytics engine (Pregel, PIE, FLASH models)
  - GraphIR/Gaia: Query optimization (Cypher/Gremlin)
  - Graph-Learn: GNN support
  - Vineyard: Shared in-memory storage
  - GART: Multi-version graphs
- **Key Strength:** Unified analytics + queries + learning in one platform
- **Repository:** [alibaba/GraphScope](https://github.com/alibaba/GraphScope)
- **Documentation:** [GraphScope.io](https://graphscope.io)
- **Best For:** Multi-workload graph platforms, cloud-native analytics

#### PowerGraph
- **Type:** Distributed graph processing (legacy)
- **Creator:** CMU (2012)
- **Language:** C++
- **Model:** Vertex-cut partitioning
- **Status:** Legacy/superseded
- **Open Source:** Yes
- **Key Innovation:** Vertex-cut partitioning for skewed graphs
- **Historical Impact:** Influenced GRAPE, GraphScope
- **Note:** Largely superseded by GraphScope and modern alternatives
- **Best For:** Historical reference, understanding vertex-cut concepts

---

### Analytics Libraries

#### NetworkX
- **Type:** General-purpose graph analytics
- **Language:** Python (pure)
- **Graph Size:** Small to medium (thousands of nodes)
- **Performance:** Baseline (slow on large graphs)
- **Status:** Stable, widely used
- **Open Source:** Yes (BSD License)
- **Key Features:**
  - Graph creation & manipulation
  - 60+ algorithms (PageRank, shortest paths, community detection)
  - Multiple graph types
  - Excellent documentation
- **Installation:** `pip install networkx`
- **Key Strength:** Ease of use, learning, flexibility
- **Documentation:** [NetworkX Documentation](https://networkx.org)
- **Best For:** Learning, prototyping, small graphs

#### igraph
- **Type:** High-performance graph analytics
- **Language:** C (with Python, R, Ruby bindings)
- **Graph Size:** Millions of nodes/edges
- **Performance:** 27x faster than NetworkX on large graphs
- **Status:** Stable, actively maintained
- **Open Source:** Yes (GPL)
- **Key Features:**
  - C core with Python bindings
  - Fast algorithms
  - Community detection
  - Network motifs
  - Isomorphism
- **Installation:** `pip install igraph` or `pip install python-igraph`
- **Key Strength:** Performance on large graphs
- **Repository:** [igraph/igraph-python](https://github.com/igraph/igraph-python)
- **Best For:** Production systems, large networks

#### graph-tool
- **Type:** Statistical graph analysis
- **Language:** C++ (with Python bindings)
- **Graph Size:** Large networks
- **Performance:** Near C++ speed with Python interface
- **Status:** Actively maintained
- **Open Source:** Yes (LGPL)
- **Key Features:**
  - C++ core
  - Graph algorithms
  - Community detection
  - Graph generation models
  - Statistical analysis
  - Visualization support
- **Installation:** `pip install graph-tool`
- **Key Strength:** C++ performance with Pythonic interface
- **Documentation:** [graph-tool.skewed.de](https://graph-tool.skewed.de)
- **Best For:** Statistical analysis, large-scale graph work

#### SNAP
- **Type:** Graph analytics library
- **Language:** C++ (Python bindings available)
- **Note:** Not covered in detailed research but widely used
- **Key Use:** Large-scale network analysis
- **Repository:** [snap-stanford](http://snap.stanford.edu/)

---

### Graph Neural Networks

#### PyTorch Geometric
- **Type:** Graph neural network library
- **Framework:** Built on PyTorch
- **Language:** Python
- **Graph Size:** Millions of nodes
- **Performance:** Training time 2,984 seconds (10k epochs, PPI dataset)
- **Status:** Active development
- **Open Source:** Yes (MIT License)
- **Key Features:**
  - Pre-built GNN architectures (GCN, GAT, GraphSAGE)
  - Graph convolution layers
  - Sampling utilities
  - Mini-batch support
  - Pure PyTorch tensors
  - Message passing API
- **Installation:** `pip install torch-geometric`
- **Key Strength:** Pythonic API, extensive models, flexibility
- **Repository:** [pyg-team/pytorch_geometric](https://github.com/pyg-team/pytorch_geometric)
- **Documentation:** [pytorch-geometric.readthedocs.io](https://pytorch-geometric.readthedocs.io)
- **Best For:** GNN research, flexible architectures

#### Deep Graph Library (DGL)
- **Type:** Graph neural network library
- **Framework:** Works with PyTorch, TensorFlow, MXNet
- **Language:** Python
- **Graph Size:** Billions of nodes
- **Performance:** Training time 1,148 seconds (10k epochs, PPI dataset) - 2.6x faster than PyG
- **Status:** Active development (2025)
- **Open Source:** Yes (Apache 2.0 License)
- **Key Features:**
  - Graph interface similar to NetworkX
  - High-performance sampling
  - Multiple backend support
  - Distributed training
  - Heterogeneous graph support
  - Sparse matrix optimization
- **Installation:** `pip install dgl`
- **Key Strength:** Training speed, memory efficiency
- **Repository:** [dmlc/dgl](https://github.com/dmlc/dgl)
- **Documentation:** [dgl.ai](https://www.dgl.ai)
- **Best For:** Large-scale GNN training, speed-critical workloads

---

### Graph Databases

#### Neo4j
- **Type:** Property graph database
- **Language:** Java (REST API, multiple drivers)
- **Graph Size:** Billions of relationships
- **Status:** Market leader
- **Open Source:** Community Edition (free), Enterprise (commercial)
- **Query Language:** Cypher
- **Key Features:**
  - Native graph storage
  - ACID transactions
  - Property graphs
  - Full-text search
  - Graph Data Science (GDS) library
  - Stored procedures
- **Deployment:** Self-hosted, Neo4j Cloud
- **Community:** Large, mature ecosystem
- **Key Strength:** Mature ecosystem, Cypher, extensive tooling
- **Website:** [neo4j.com](https://neo4j.com)
- **Documentation:** [Neo4j Documentation](https://neo4j.com/docs/)
- **Best For:** Enterprise graphs, OLTP + analytics hybrid

#### TigerGraph
- **Type:** Property graph analytics database
- **Language:** C++ backend (REST API)
- **Graph Size:** Terabytes of data
- **Status:** Enterprise-grade
- **Open Source:** Partial (free tier up to 50GB)
- **Query Language:** GSQL (proprietary)
- **Key Features:**
  - Hybrid memory-disk storage
  - Compression (2x-10x reduction)
  - Real-time deep analytics
  - Machine learning integration
  - Built-in graph algorithms
  - Multi-tenancy
- **Deployment:** Self-hosted, TigerGraph Cloud
- **Key Strength:** Enterprise analytics at scale, deep queries
- **Website:** [tigergraph.com](https://www.tigergraph.com)
- **Documentation:** [TigerGraph Docs](https://docs.tigergraph.com)
- **Best For:** Enterprise analytics, terabyte-scale graphs

#### Memgraph
- **Type:** In-memory property graph database
- **Language:** C++ backend (Cypher API)
- **Graph Size:** RAM-limited
- **Status:** Production-ready
- **Open Source:** Community Edition (full-featured), Enterprise
- **Query Language:** Cypher
- **Key Features:**
  - In-memory processing
  - ACID transactions
  - Cypher compatibility with Neo4j
  - Kafka integration
  - MAGE algorithm library
  - Optional disk persistence
  - Transparent replication
- **Deployment:** Self-hosted, Memgraph Cloud, Docker
- **Key Strength:** Lightning-fast queries, real-time analytics
- **Website:** [memgraph.com](https://memgraph.com)
- **Documentation:** [Memgraph Docs](https://memgraph.com/docs/)
- **Best For:** Real-time fraud detection, monitoring, cybersecurity

#### JanusGraph
- **Type:** Distributed property graph database
- **Language:** Java (Gremlin API)
- **Graph Size:** Hundreds of billions of edges
- **Status:** Linux Foundation project
- **Open Source:** Yes (Apache 2.0)
- **Query Language:** Gremlin (TinkerPop standard)
- **Key Features:**
  - Distributed architecture
  - Pluggable backends (Cassandra, HBase, Bigtable)
  - Horizontal scaling
  - Transactions
  - Full-text search
  - Geospatial queries
- **Deployment:** Self-managed on big data infrastructure
- **Key Strength:** Massive scale, distributed, no vendor lock-in
- **Repository:** [JanusGraph/janusgraph](https://github.com/JanusGraph/janusgraph)
- **Documentation:** [JanusGraph Docs](https://janusgraph.org)
- **Best For:** Massive scale, big data integration

#### ArangoDB
- **Type:** Multi-model database (documents + graphs + search)
- **Language:** C++ backend (REST/JavaScript API)
- **Graph Size:** Multi-model flexibility
- **Status:** Production-ready
- **Open Source:** Community Edition (free), Enterprise
- **Query Language:** AQL (graph + document)
- **Key Features:**
  - Multi-model (documents + graphs + search)
  - ACID transactions
  - AQL language
  - Full-text search
  - Geospatial queries
  - Python/JavaScript drivers
- **Deployment:** Self-hosted, ArangoDB Cloud
- **Key Strength:** Flexible multi-model approach
- **Website:** [arangodb.com](https://www.arangodb.com)
- **Documentation:** [ArangoDB Docs](https://www.arangodb.com/docs/)
- **Best For:** Applications needing document + graph combo

---

### Visualization Tools

#### Gephi
- **Type:** Network visualization & analysis (desktop)
- **Language:** Java
- **Graph Size:** Excellent for 100k+ nodes
- **Status:** Stable, actively maintained
- **Open Source:** Yes (AGPL)
- **Key Features:**
  - Force-directed layout (ForceAtlas2)
  - Community detection
  - Statistical analysis
  - Plugin architecture
  - Real-time visualization
  - Temporal network support
- **Installation:** Desktop application
- **Key Strength:** Scalable visualization, memory-efficient
- **Website:** [gephi.org](https://gephi.org)
- **Best For:** Large network visualization

#### Cytoscape
- **Type:** Network visualization & analysis (desktop + web)
- **Language:** Java (Cytoscape.js for web)
- **Graph Size:** Medium (optimized for curated networks)
- **Status:** Actively maintained
- **Open Source:** Yes (LGPL)
- **Key Features:**
  - Domain-specific for biology
  - 200+ plugins
  - Gene ontology annotations
  - Pathway analysis
  - Functional enrichment
  - Cytoscape.js web variant
- **Installation:** Desktop application or web library
- **Key Strength:** Bioinformatics specialization
- **Website:** [cytoscape.org](https://cytoscape.org)
- **Best For:** Biological networks, life sciences

#### Graphviz
- **Type:** Automatic graph layout & drawing (CLI + library)
- **Language:** C (DOT language)
- **Graph Size:** Moderate
- **Status:** Mature, stable
- **Open Source:** Yes (Common Public License)
- **Key Features:**
  - DOT language specification
  - Automatic layout algorithms
  - Multiple output formats (PNG, SVG, PDF)
  - Hierarchical layouts (excellent for DAGs)
  - Spring-embedded layouts
  - Scriptable via pygraphviz
- **Installation:** Command-line tool or Python library
- **Key Strength:** Automatic, deterministic layout
- **Website:** [graphviz.org](https://graphviz.org)
- **Best For:** Automatic layout, software architecture diagrams

---

## Framework Categories Summary

### By Scale
- **Petabyte-scale:** TigerGraph, JanusGraph
- **Terabyte-scale:** TigerGraph, GraphScope, Giraph
- **Billion-edge scale:** Giraph, Plato, GraphScope, DGL
- **Million-node scale:** igraph, graph-tool, PyG, DGL
- **Thousand-node scale:** NetworkX
- **In-memory:** Memgraph (RAM-limited)

### By Language
- **Python (pure):** NetworkX
- **Python (with bindings):** igraph, graph-tool, DGL, PyG, GraphScope
- **Java:** Giraph, Neo4j, JanusGraph
- **C/C++:** PowerGraph, Plato, graph-tool, Graphviz, TigerGraph, Memgraph, ArangoDB
- **Scala:** Spark GraphX
- **Proprietary:** Pregel, TigerGraph

### By Primary Use
- **Analytics:** NetworkX, igraph, graph-tool, Giraph, GraphX, Plato, GraphScope
- **OLTP Database:** Neo4j, Memgraph, ArangoDB
- **Analytics Database:** TigerGraph, JanusGraph
- **Machine Learning:** DGL, PyG, Plato, GraphScope
- **Visualization:** Gephi, Cytoscape, Graphviz

### By Maturity
- **Mature/Proven:** Neo4j, NetworkX, igraph, Giraph, GraphX, Graphviz, Gephi
- **Production-Ready:** TigerGraph, Memgraph, JanusGraph, DGL, PyG, graph-tool, GraphScope
- **Emerging:** Plato, newer GraphScope versions

### By Open Source Status
- **Fully Open:** NetworkX, igraph, graph-tool, Giraph, GraphX, JanusGraph, Memgraph Community, Cytoscape, Gephi, Graphviz, DGL, PyG
- **Partial Open:** Neo4j (Community free), TigerGraph (free tier), ArangoDB (Community free), Memgraph (Community free)
- **Proprietary:** Pregel, TigerGraph Enterprise

---

## Technology Stack Integration Matrix

| Framework | Spark | Hadoop | PyTorch | TensorFlow | Kafka | Docker |
|-----------|-------|--------|---------|-----------|-------|--------|
| GraphX | **Native** | Good | - | - | - | Yes |
| Giraph | Good | **Native** | - | - | - | Yes |
| Plato | - | - | - | - | - | Yes |
| GraphScope | - | - | Good | Good | - | Yes |
| Neo4j | Plugin | Good | - | - | Yes | Yes |
| Memgraph | - | - | - | - | **Native** | Yes |
| TigerGraph | Plugin | Plugin | - | - | - | Yes |
| JanusGraph | Good | **Native** | - | - | - | Yes |
| DGL | - | - | **Native** | **Native** | - | Yes |
| PyG | - | - | **Native** | - | - | Yes |

---

## Performance Comparison Benchmarks

### Graph Size Handling (Maximum Typical)
```
Pregel         →  Web-scale (50B+)
Giraph         →  50B+ edges ████████████████████
GraphX         →  10B edges ████
Plato          →  Massive ████████████████████
GraphScope     →  Distributed ████████████████████
NetworkX       →  Thousands ███
igraph         →  Millions ████████
graph-tool     →  Millions ████████
Neo4j          →  Billions ██████████
TigerGraph     →  Terabytes ████████████████████
Memgraph       →  RAM-limited ████████████
JanusGraph     →  100B+ edges ████████████████████
```

### Speed (Relative to Baseline GraphX = 1.0)
```
Plato          →  10x faster ██████████
Giraph         →  3-9x faster ███████
GraphX         →  1.0 (baseline) █
NetworkX       →  0.037x (27x slower) ▌
igraph         →  1.5-3x faster (vs NetworkX) ███
DGL (vs PyG)   →  2.6x faster (GNN training) ██
```

### Memory Efficiency (Lower is Better)
```
Plato          →  1x (reference) █
Giraph         →  1.3-4x (vs baseline) ███
GraphX         →  16-116x (vs Plato) ████████████████████
NetworkX       →  3-5x (vs igraph) ████
igraph         →  Very low █
```

---

## Decision Reference by Use Case

| Use Case | Best Choice | Alternative | Avoid |
|----------|------------|-------------|-------|
| Learning graphs | NetworkX | PyG | Giraph, TigerGraph |
| Prototyping algorithms | NetworkX, PyG | igraph | Giraph, JanusGraph |
| Production analytics (small) | igraph | graph-tool | NetworkX |
| Production analytics (large) | Giraph | Plato | GraphX |
| Real-time OLTP | Memgraph | Neo4j | Giraph, JanusGraph |
| Enterprise analytics | TigerGraph | Neo4j | Memgraph |
| Large-scale ML training | DGL | Plato, PyG | GraphX |
| GNN research | PyG | DGL | - |
| Knowledge graphs | Neo4j | JanusGraph | - |
| Recommendation engine | Neo4j | DGL | - |
| Network visualization | Gephi | Cytoscape | Graphviz |
| Biological networks | Cytoscape | Gephi | - |
| Automatic layout | Graphviz | - | - |

---

## Resources & Links

### Official Documentation
- [Pregel paper](http://infolab.stanford.edu/gps/) - Seminal paper
- [Apache Giraph](https://giraph.apache.org/)
- [Spark GraphX](https://spark.apache.org/docs/latest/graphx-programming-guide.html)
- [GraphScope](https://graphscope.io)
- [NetworkX](https://networkx.org)
- [igraph](https://igraph.org)
- [graph-tool](https://graph-tool.skewed.de)
- [PyTorch Geometric](https://pytorch-geometric.readthedocs.io)
- [DGL](https://www.dgl.ai)
- [Neo4j](https://neo4j.com)
- [TigerGraph](https://www.tigergraph.com)
- [Memgraph](https://memgraph.com)
- [JanusGraph](https://janusgraph.org)
- [ArangoDB](https://www.arangodb.com)
- [Gephi](https://gephi.org)
- [Cytoscape](https://cytoscape.org)
- [Graphviz](https://graphviz.org)

### Research Papers
- Pregel: A System for Large-Scale Graph Processing (Google, 2010)
- PowerGraph: Distributed Graph-Parallel Computation (CMU, 2012)
- GraphScope: A Unified Engine for Big Graph Processing (Alibaba, 2020)
- Benchmarking Graph Computing Frameworks (Tencent, 2019)

---

**Last Updated:** January 1, 2025
**Total Frameworks Covered:** 20 major systems
**Categories:** Distributed Processing (6), Analytics (4), GNN (2), Databases (5), Visualization (3)
