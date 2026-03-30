# Academic Papers & Research

Curated index of peer-reviewed papers, conference proceedings, and technical reports that study, evaluate, or use Zenoh.

---

## Table of Contents

- [Performance Benchmarks](#performance-benchmarks)
- [Robotics & ROS2](#robotics-ros2)
- [Automotive & SDV](#automotive-sdv)
- [Edge & Cloud Continuum](#edge-cloud-continuum)
- [Pub/Sub & Middleware Theory](#pubsub-middleware-theory)
- [Community Comparisons & Evaluations](#community-comparisons-evaluations)

---

## Performance Benchmarks

### A Performance Study on the Throughput and Latency of Zenoh, MQTT, Kafka, and DDS
**arXiv:2303.09419** · cs.DC · 2023 · 21 pages, 7 figures, 7 tables

The primary benchmark paper comparing Zenoh against MQTT, Kafka, and DDS across throughput and latency dimensions on 100 GbE hardware. Results show Zenoh achieves ~16 µs peer-to-peer latency and competitive throughput at scale. Widely cited in the Zenoh documentation and comparison guides.

- [Abstract](https://arxiv.org/abs/2303.09419)
- [PDF](https://arxiv.org/pdf/2303.09419)
- DOI: [10.48550/arXiv.2303.09419](https://doi.org/10.48550/arXiv.2303.09419)

---

## Robotics & ROS2

### Comparison of Middlewares in Edge-to-Edge and Edge-to-Cloud Communication for Distributed ROS2 Systems
**arXiv:2309.07496** · cs.RO · 2023 · *J Intell Robot Syst* 110, 162 (2024)

Evaluates Zenoh, DDS, MQTT, and other middlewares for distributed ROS2 deployments across edge-to-edge and edge-to-cloud scenarios. Published in the Journal of Intelligent & Robotic Systems.

- [Abstract](https://arxiv.org/abs/2309.07496)
- DOI: [10.48550/arXiv.2309.07496](https://doi.org/10.48550/arXiv.2309.07496)
- Journal DOI: [10.1007/s10846-024-02187-z](https://doi.org/10.1007/s10846-024-02187-z)

---

## Automotive & SDV

### Automotive Middleware Performance: Comparison of FastDDS, Zenoh and vSomeIP
**arXiv:2505.02734** · 2025 · AUTOtechagil project (FKZ 01IS22088x)

Analyzes FastDDS, Zenoh, and vSomeIP under automotive operating conditions. Examines end-to-end latency, scaling performance, discovery times, and kernel interaction. Presents 12 findings on best-performing middleware configurations for software-defined vehicles.

- [Full text](https://arxiv.org/html/2505.02734v2)
- [Abstract](https://arxiv.org/abs/2505.02734)

---

## Edge & Cloud Continuum

### TriCloudEdge: A Multi-Layer Cloud Continuum
**arXiv:2602.02121** · cs.NI · 2026

Proposes a multi-layer cloud continuum architecture using Zenoh as the communication fabric across edge, fog, and cloud tiers.

- [Abstract](https://arxiv.org/abs/2602.02121)

### MOSE: A Novel Orchestration Framework for Stateful Microservice Migration at the Edge
**arXiv:2506.09159** · 2025 · EC 6G-INTENSE / ADROIT6G / TRIALSNET projects

Framework for stateful microservice migration at the edge. Uses Zenoh as a key communication primitive. Supported by multiple EU 6G research projects.

- [Full text](https://arxiv.org/html/2506.09159v1)

---

## Pub/Sub & Middleware Theory

### Runtime Verification Containers for Publish/Subscribe Networks
**arXiv:2408.06380** · 2024 · Boğaziçi University

Studies containerization of runtime verification tools for pub/sub networks. Benchmarks using software-defined vehicle case study. Evaluates Zenoh-based deployments in IoT and robotics contexts.

- [Full text](https://arxiv.org/html/2408.06380v1)

---

## Community Comparisons & Evaluations

### Zenoh vs MQTT, Kafka, DDS — ZettaScale Blog
Official ZettaScale analysis and benchmarks comparing Zenoh to common alternatives.

- [Read](https://zenoh.io/blog/2023-03-21-zenoh-vs-mqtt-kafka-dds/)

### Comparison of DDS, MQTT, and Zenoh in Edge-to-Edge Cloud Co-Processing
Technical report comparing middleware options for edge computing deployments.

- [Read](https://deepai.org/publication/comparison-of-dds-mqtt-and-zenoh-in-edge-to-edge-cloud-co-processing)

### Zenoh Performance — ROS Discourse
Community thread with real-world performance measurements and discussion of Zenoh's ROS2 middleware implementation.

- [Read](https://discourse.openrobotics.org/t/zenoh-performance-30494)

### PX4 Zenoh Middleware Documentation
PX4 autopilot project's documentation on using Zenoh as their middleware layer.

- [Read](https://docs.px4.io/main/en/middleware/zenoh.html)

---

> **Contributing**: Found a paper that uses or evaluates Zenoh? The raw sources for this index are in `raw/17-arxiv-papers/` and `raw/13-research-papers/`.

## See Also

- [Comparison Guide](comparison-guide.md) — protocol-level benchmarks against MQTT, DDS, and Kafka referenced in many of these papers
- [Benchmarks](benchmarks.md) — detailed throughput and latency numbers underlying the performance claims
- [Performance Tuning Guide](performance-tuning-guide.md) — how to configure Zenoh to achieve the performance these papers measure
- [ROS2 Migration Guide](ros2-migration-guide.md) — context for the robotics/ROS2 papers on replacing DDS
- [Automotive Guide](automotive-guide.md) — deeper coverage of the SDV and automotive papers in this index
