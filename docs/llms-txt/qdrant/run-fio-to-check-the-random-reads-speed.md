# Run fio to check the random reads speed
fio --randrepeat=1 \
    --ioengine=libaio \
    --direct=1 \
    --gtod_reduce=1 \
    --name=fiotest \
    --filename=testfio \
    --bs=4k \
    --iodepth=64 \
    --size=8G \
    --readwrite=randread

```

Initially, we tested on a network-mounted disk, but its performance was too slow, with a read IOPS of 6366 and a bandwidth of 24.9 MiB/s:

```text
read: IOPS=6366, BW=24.9MiB/s (26.1MB/s)(8192MiB/329424msec)

```

To improve performance, we switched to a local disk, which showed much faster results, with a read IOPS of 63.2k and a bandwidth of 247 MiB/s:

```text
read: IOPS=63.2k, BW=247MiB/s (259MB/s)(8192MiB/33207msec)

```

That gave us a significant speed boost, but we wanted to see if we could improve performance even further.
To do that, we switched to a machine with a local SSD, which showed even better results, with a read IOPS of 183k and a bandwidth of 716 MiB/s:

```text
read: IOPS=183k, BW=716MiB/s (751MB/s)(8192MiB/11438msec)

```

Let’s see how these results translate into search speed:

| Memory | RPS with IOPS=63.2k | RPS with IOPS=183k |
| --- | --- | --- |
| 600mb | 5 | 50 |
| 300mb | 0.9 | 13 |
| 200mb | 0.5 | 8 |
| 150mb | 0.4 | 7 |

As you can see, the speed of the disk has a significant impact on the search speed.
With a local SSD, we were able to increase the search speed by 10x!

With the production-grade disk, the search speed could be even higher.
Some configurations of the SSDs can reach 1M IOPS and more.

Which might be an interesting option to serve large datasets with low search latency in Qdrant.

## [Anchor](https://qdrant.tech/articles/memory-consumption/\#conclusion) Conclusion

In this article, we showed that Qdrant has flexibility in terms of RAM usage and can be used to serve large datasets. It provides configurable trade-offs between RAM usage and search speed. If you’re interested to learn more about Qdrant, [book a demo today](https://qdrant.tech/contact-us/)!

We are eager to learn more about how you use Qdrant in your projects, what challenges you face, and how we can help you solve them.
Please feel free to join our [Discord](https://qdrant.to/discord) and share your experience with us!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/memory-consumption.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/memory-consumption.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-141-lllmstxt|>
## distance-based-exploration
- [Articles](https://qdrant.tech/articles/)
- Distance-based data exploration

[Back to Data Exploration](https://qdrant.tech/articles/data-exploration/)