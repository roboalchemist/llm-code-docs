# Single node benchmarks (2022)

August 23, 2022

Dataset:deep-image-96-angulargist-960-euclideanglove-100-angular

Search threads:1008421

Plot values:

RPS

Latency

p95 latency

Index time

| Engine | Setup | Dataset | Upload Time(m) | Upload + Index Time(m) | Latency(ms) | P95(ms) | P99(ms) | RPS | Precision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| qdrant | qdrant-rps-m-64-ef-512 | deep-image-96-angular | 14.096 | 149.32 | 24.73 | 55.75 | 63.73 | 1541.86 | 0.96 |
| weaviate | weaviate-m-16-ef-128 | deep-image-96-angular | 148.70 | 148.70 | 190.94 | 351.75 | 414.16 | 507.33 | 0.94 |
| milvus | milvus-m-16-ef-128 | deep-image-96-angular | 6.074 | 35.28 | 171.50 | 220.26 | 236.97 | 339.44 | 0.97 |
| elastic | elastic-m-16-ef-128 | deep-image-96-angular | 87.54 | 101.16 | 923.031 | 1116.83 | 1671.31 | 95.90 | 0.97 |

_Download raw data: [here](https://qdrant.tech/benchmarks/result-2022-08-10.json)_

This is an archived version of Single node benchmarks. Please refer to the new version [here](https://qdrant.tech/benchmarks/single-node-speed-benchmark/).

Share this article

[x](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fsingle-node-speed-benchmark-2022%2F&text=Single%20node%20benchmarks%20%282022%29 "x")[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fsingle-node-speed-benchmark-2022%2F "LinkedIn")

Up!

<|page-10-lllmstxt|>
## using-multivector-representations
- [Documentation](https://qdrant.tech/documentation/)
- [Advanced tutorials](https://qdrant.tech/documentation/advanced-tutorials/)
- How to Use Multivector Representations with Qdrant Effectively