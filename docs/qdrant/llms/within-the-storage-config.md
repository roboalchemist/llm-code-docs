# within the storage config
storage:
	# enable the async scorer which uses io_uring
	async_scorer: true

```

You can return to the mmap based backend by either deleting the `async_scorer`
entry or setting the value to `false`.

## [Anchor](https://qdrant.tech/articles/io_uring/\#benchmarks) Benchmarks

To run the benchmark, use a test instance of Qdrant. If necessary spin up a
docker container and load a snapshot of the collection you want to benchmark
with. You can copy and edit our [benchmark script](https://qdrant.tech/articles_data/io_uring/rescore-benchmark.sh)
to run the benchmark. Run the script with and without enabling
`storage.async_scorer` and once. You can measure IO usage with `iostat` from
another console.

For our benchmark, we chose the laion dataset picking 5 million 768d entries.
We enabled scalar quantization + HNSW with m=16 and ef\_construct=512.
We do the quantization in RAM, HNSW in RAM but keep the original vectors on
disk (which was a network drive rented from Hetzner for the benchmark).

If you want to reproduce the benchmarks, you can get snapshots containing the
datasets:

- [mmap only](https://storage.googleapis.com/common-datasets-snapshots/laion-768-6m-mmap.snapshot)
- [with scalar quantization](https://storage.googleapis.com/common-datasets-snapshots/laion-768-6m-sq-m16-mmap.shapshot)

Running the benchmark, we get the following IOPS, CPU loads and wall clock times:

|  | oversampling | parallel | ~max IOPS | CPU% (of 4 cores) | time (s) (avg of 3) |
| --- | --- | --- | --- | --- | --- |
| io\_uring | 1 | 4 | 4000 | 200 | 12 |
| mmap | 1 | 4 | 2000 | 93 | 43 |
| io\_uring | 1 | 8 | 4000 | 200 | 12 |
| mmap | 1 | 8 | 2000 | 90 | 43 |
| io\_uring | 4 | 8 | 7000 | 100 | 30 |
| mmap | 4 | 8 | 2300 | 50 | 145 |

Note that in this case, the IO operations have relatively high latency due to
using a network disk. Thus, the kernel takes more time to fulfil the mmap
requests, and application threads need to wait, which is reflected in the CPU
percentage. On the other hand, with the io\_uring backend, the application
threads can better use available cores for the rescore operation without any
IO-induced delays.

Oversampling is a new feature to improve accuracy at the cost of some
performance. It allows setting a factor, which is multiplied with the `limit`
while doing the search. The results are then re-scored using the original vector
and only then the top results up to the limit are selected.

## [Anchor](https://qdrant.tech/articles/io_uring/\#discussion) Discussion

Looking back, disk IO used to be very serialized; re-positioning read-write
heads on moving platter was a slow and messy business. So the system overhead
didn’t matter as much, but nowadays with SSDs that can often even parallelize
operations while offering near-perfect random access, the overhead starts to
become quite visible. While memory-mapped IO gives us a fair deal in terms of
ease of use and performance, we can improve on the latter in exchange for
some modest complexity increase.

io\_uring is still quite young, having only been introduced in 2019 with kernel
5.1, so some administrators will be wary of introducing it. Of course, as with
performance, the right answer is usually “it depends”, so please review your
personal risk profile and act accordingly.

## [Anchor](https://qdrant.tech/articles/io_uring/\#best-practices) Best Practices

If your on-disk collection’s query performance is of sufficiently high
priority to you, enable the io\_uring-based async\_scorer to greatly reduce
operating system overhead from disk IO. On the other hand, if your
collections are in memory only, activating it will be ineffective. Also note
that many queries are not IO bound, so the overhead may or may not become
measurable in your workload. Finally, on-device disks typically carry lower
latency than network drives, which may also affect mmap overhead.

Therefore before you roll out io\_uring, perform the above or a similar
benchmark with both mmap and io\_uring and measure both wall time and IOps).
Benchmarks are always highly use-case dependent, so your mileage may vary.
Still, doing that benchmark once is a small price for the possible performance
wins. Also please
[tell us](https://discord.com/channels/907569970500743200/907569971079569410)
about your benchmark results!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/io_uring.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/io_uring.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-118-lllmstxt|>
## dataset-quality
- [Articles](https://qdrant.tech/articles/)
- Finding errors in datasets with Similarity Search

[Back to Data Exploration](https://qdrant.tech/articles/data-exploration/)