# Minimal RAM you need to serve a million vectors

Andrei Vasnetsov

·

December 07, 2022

![Minimal RAM you need to serve a million vectors](https://qdrant.tech/articles_data/memory-consumption/preview/title.jpg)

When it comes to measuring the memory consumption of our processes, we often rely on tools such as `htop` to give us an indication of how much RAM is being used. However, this method can be misleading and doesn’t always accurately reflect the true memory usage of a process.

There are many different ways in which `htop` may not be a reliable indicator of memory usage.
For instance, a process may allocate memory in advance but not use it, or it may not free deallocated memory, leading to overstated memory consumption.
A process may be forked, which means that it will have a separate memory space, but it will share the same code and data with the parent process.
This means that the memory consumption of the child process will be counted twice.
Additionally, a process may utilize disk cache, which is also accounted as resident memory in the `htop` measurements.

As a result, even if `htop` shows that a process is using 10GB of memory, it doesn’t necessarily mean that the process actually requires 10GB of RAM to operate efficiently.
In this article, we will explore how to properly measure RAM usage and optimize [Qdrant](https://qdrant.tech/) for optimal memory consumption.

## [Anchor](https://qdrant.tech/articles/memory-consumption/\#how-to-measure-actual-ram-requirements) How to measure actual RAM requirements

We need to know memory consumption in order to estimate how much RAM is required to run the program.
So in order to determine that, we can conduct a simple experiment.
Let’s limit the allowed memory of the process and observe at which point it stops functioning.
In this way we can determine the minimum amount of RAM the program needs to operate.

One way to do this is by conducting a grid search, but a more efficient method is to use binary search to quickly find the minimum required amount of RAM.
We can use docker to limit the memory usage of the process.

Before running each benchmark, it is important to clear the page cache with the following command:

```bash
sudo bash -c 'sync; echo 1 > /proc/sys/vm/drop_caches'

```

This ensures that the process doesn’t utilize any data from previous runs, providing more accurate and consistent results.

We can use the following command to run Qdrant with a memory limit of 1GB:

```bash
docker run -it --rm \
    --memory 1024mb \
    --network=host \
    -v "$(pwd)/data/storage:/qdrant/storage" \
    qdrant/qdrant:latest

```

## [Anchor](https://qdrant.tech/articles/memory-consumption/\#lets-run-some-benchmarks) Let’s run some benchmarks

Let’s run some benchmarks to see how much RAM Qdrant needs to serve 1 million vectors.

We can use the `glove-100-angular` and scripts from the [vector-db-benchmark](https://github.com/qdrant/vector-db-benchmark) project to upload and query the vectors.
With the first run we will use the default configuration of Qdrant with all data stored in RAM.

```bash