# Search vectors
python run.py --engines qdrant-all-in-ram --datasets glove-100-angular --skip-upload

```

### [Anchor](https://qdrant.tech/articles/memory-consumption/\#all-in-memory) All in Memory

In the first experiment, we tested how well our system performs when all vectors are stored in memory.
We tried using different amounts of memory, ranging from 1512mb to 1024mb, and measured the number of requests per second (rps) that our system was able to handle.

| Memory | Requests/s |
| --- | --- |
| 1512mb | 774.38 |
| 1256mb | 760.63 |
| 1200mb | 794.72 |
| 1152mb | out of memory |
| 1024mb | out of memory |

We found that 1152MB memory limit resulted in our system running out of memory, but using 1512mb, 1256mb, and 1200mb of memory resulted in our system being able to handle around 780 RPS.
This suggests that about 1.2GB of memory is needed to serve around 1 million vectors, and there is no speed degradation when limiting memory usage above 1.2GB.

### [Anchor](https://qdrant.tech/articles/memory-consumption/\#vectors-stored-using-mmap) Vectors stored using MMAP

Let’s go a bit further!
In the second experiment, we tested how well our system performs when **vectors are stored using the memory-mapped file** (mmap).
Create collection with:

```http
PUT /collections/benchmark
{
  "vectors": {
    ...
    "on_disk": true
  }
}

```

This configuration tells Qdrant to use mmap for vectors if the segment size is greater than 20000Kb (which is approximately 40K 128d-vectors).

Now the out-of-memory happens when we allow using **600mb** RAM only

Experiments details

| Memory | Requests/s |
| --- | --- |
| 1200mb | 759.94 |
| 1100mb | 687.00 |
| 1000mb | 10 |

— use a bit faster disk —

| Memory | Requests/s |
| --- | --- |
| 1000mb | 25 rps |
| 750mb | 5 rps |
| 625mb | 2.5 rps |
| 600mb | out of memory |

At this point we have to switch from network-mounted storage to a faster disk, as the network-based storage is too slow to handle the amount of sequential reads that our system needs to serve the queries.

But let’s first see how much RAM we need to serve 1 million vectors and then we will discuss the speed optimization as well.

### [Anchor](https://qdrant.tech/articles/memory-consumption/\#vectors-and-hnsw-graph-stored-using-mmap) Vectors and HNSW graph stored using MMAP

In the third experiment, we tested how well our system performs when vectors and [HNSW](https://qdrant.tech/articles/filtrable-hnsw/) graph are stored using the memory-mapped files.
Create collection with:

```http
PUT /collections/benchmark
{
  "vectors": {
    ...
    "on_disk": true
  },
  "hnsw_config": {
    "on_disk": true
  },
  ...
}

```

With this configuration we are able to serve 1 million vectors with **only 135mb of RAM**!

Experiments details

| Memory | Requests/s |
| --- | --- |
| 600mb | 5 rps |
| 300mb | 0.9 rps / 1.1 sec per query |
| 150mb | 0.4 rps / 2.5 sec per query |
| 135mb | 0.33 rps / 3 sec per query |
| 125mb | out of memory |

At this point the importance of the disk speed becomes critical.
We can serve the search requests with 135mb of RAM, but the speed of the requests makes it impossible to use the system in production.

Let’s see how we can improve the speed.

## [Anchor](https://qdrant.tech/articles/memory-consumption/\#how-to-speed-up-the-search) How to speed up the search

To measure the impact of disk parameters on search speed, we used the `fio` tool to test the speed of different types of disks.

```bash