# Source: https://brpc.apache.org/docs/rpc-in-depth/consistent-hashing/

Title: Consistent Hashing

URL Source: https://brpc.apache.org/docs/rpc-in-depth/consistent-hashing/

Markdown Content:
Consistent Hashing | bRPC
===============
Consistent Hashing | bRPC
===============
[](https://brpc.apache.org/)

*   [GitHub](https://github.com/apache/brpc/)
*   [Download](https://brpc.apache.org/docs/downloadbrpc/)
*   [Docs](https://brpc.apache.org/docs/)
*   [Community](https://brpc.apache.org/docs/community/community/)
*   [ASF](https://brpc.apache.org/docs/asf/)
*   [Blog](https://brpc.apache.org/docs/blogs/)
*   [Users](https://brpc.apache.org/docs/users/)
*   [English](https://brpc.apache.org/docs/rpc-in-depth/consistent-hashing/#)[中文](https://brpc.apache.org/zh/) 

[English](https://brpc.apache.org/docs/rpc-in-depth/consistent-hashing/#)

[中文](https://brpc.apache.org/zh/)

*   [Docs](https://brpc.apache.org/docs/)

    *   [Overview](https://brpc.apache.org/docs/overview/)[Download](https://brpc.apache.org/docs/downloadbrpc/)[Getting started](https://brpc.apache.org/docs/getting_started/)[Performance benchmark](https://brpc.apache.org/docs/benchmark/)
        *   [bvar](https://brpc.apache.org/docs/bvar/)

        
            *                   *   [bvar](https://brpc.apache.org/docs/bvar/bvar/)

                

                *   [bvar c++](https://brpc.apache.org/docs/bvar/bvar-c++/)

                

        *   [bthread](https://brpc.apache.org/docs/bthread/)

        
            *                   *   [bthread](https://brpc.apache.org/docs/bthread/bthread/)

                

                *   [bthread or not](https://brpc.apache.org/docs/bthread/bthread-or-not/)

                

                *   [Execution Queue](https://brpc.apache.org/docs/bthread/execution-queue/)

                

                *   [thread-local](https://brpc.apache.org/docs/bthread/thread-local/)

                

        *   [C++ Base](https://brpc.apache.org/docs/c++-base/)

        
            *                   *   [IOBuf](https://brpc.apache.org/docs/c++-base/iobuf/)

                

                *   [Streaming Log](https://brpc.apache.org/docs/c++-base/streaming-log/)

                

                *   [FlatMap](https://brpc.apache.org/docs/c++-base/flatmap/)

                

                *   [bRPC Training Materials](https://brpc.apache.org/docs/c++-base/brpc-training-materials/)

                

        *   [Client](https://brpc.apache.org/docs/client/)

        
            *                   *   [Basics](https://brpc.apache.org/docs/client/basics/)

                

                *   [Error code](https://brpc.apache.org/docs/client/error-code/)

                

                *   [Combo channels](https://brpc.apache.org/docs/client/combo-channels/)

                

                *   [Access http:h2](https://brpc.apache.org/docs/client/access-httph2/)

                

                *   [Access gRPC](https://brpc.apache.org/docs/client/access-grpc/)

                

                *   [Access thrift](https://brpc.apache.org/docs/client/access-thrift/)

                

                *   [Access UB](https://brpc.apache.org/docs/client/access-ub/)

                

                *   [Access redis](https://brpc.apache.org/docs/client/access-redis/)

                

                *   [Access memcached](https://brpc.apache.org/docs/client/access-memcached/)

                

                *   [Streaming RPC](https://brpc.apache.org/docs/client/streaming-rpc/)

                

                *   [Backup request](https://brpc.apache.org/docs/client/backup-request/)

                

                *   [Dummy server](https://brpc.apache.org/docs/client/dummy-server/)

                

        *   [Server](https://brpc.apache.org/docs/server/)

        
            *                   *   [Basics](https://brpc.apache.org/docs/server/basics/)

                

                *   [Serve http:h2](https://brpc.apache.org/docs/server/serve-httph2/)

                

                *   [Serve gRPC](https://brpc.apache.org/docs/server/serve-grpc/)

                

                *   [Serve thrift](https://brpc.apache.org/docs/server/serve-thrift/)

                

                *   [Serve Nshead](https://brpc.apache.org/docs/server/serve-nshead/)

                

                *   [Server push](https://brpc.apache.org/docs/server/server-push/)

                

                *   [Avalanche](https://brpc.apache.org/docs/server/avalanche/)

                

                *   [Debug server issues](https://brpc.apache.org/docs/server/debug-server-issues/)

                

                *   [Auto ConcurrencyLimiter](https://brpc.apache.org/docs/server/auto-concurrencylimiter/)

                

                *   [Media Server](https://brpc.apache.org/docs/server/media-server/)

                

                *   [json2pb](https://brpc.apache.org/docs/server/json2pb/)

                

        *   [Builtin Services](https://brpc.apache.org/docs/builtin-services/)

        
            *                   *   [builtin services](https://brpc.apache.org/docs/builtin-services/buildin_services/)

                

                *   [status](https://brpc.apache.org/docs/builtin-services/status/)

                

                *   [vars](https://brpc.apache.org/docs/builtin-services/vars/)

                

                *   [connections](https://brpc.apache.org/docs/builtin-services/connections/)

                

                *   [flags](https://brpc.apache.org/docs/builtin-services/flags/)

                

                *   [rpcz](https://brpc.apache.org/docs/builtin-services/rpcz/)

                

                *   [cpu profiler](https://brpc.apache.org/docs/builtin-services/cpu_profiler/)

                

                *   [heap profiler](https://brpc.apache.org/docs/builtin-services/heap_profiler/)

                

                *   [contention profiler](https://brpc.apache.org/docs/builtin-services/contention_profiler/)

                

        *   [Tools](https://brpc.apache.org/docs/tools/)

        
            *                   *   [rpc_press](https://brpc.apache.org/docs/tools/rpc_press/)

                

                *   [rpc_replay](https://brpc.apache.org/docs/tools/rpc_replay/)

                

                *   [rpc_view](https://brpc.apache.org/docs/tools/rpc_view/)

                

                *   [benchmark_http](https://brpc.apache.org/docs/tools/benchmark_http/)

                

                *   [parallel_http](https://brpc.apache.org/docs/tools/parallel_http/)

                

        *   [RPC in depth](https://brpc.apache.org/docs/rpc-in-depth/)

        
            *                   *   [New Protocol](https://brpc.apache.org/docs/rpc-in-depth/new-protocol/)

                

                *   [Atomic instructions](https://brpc.apache.org/docs/rpc-in-depth/atomic-instructions/)

                

                *   [IO](https://brpc.apache.org/docs/rpc-in-depth/io/)

                

                *   [Threading Overview](https://brpc.apache.org/docs/rpc-in-depth/threading-overview/)

                

                *   [Load Balancing](https://brpc.apache.org/docs/rpc-in-depth/load-balancing/)

                

                *   [Locality-aware](https://brpc.apache.org/docs/rpc-in-depth/locality-aware/)

                

                *   [Consistent Hashing](https://brpc.apache.org/docs/rpc-in-depth/consistent-hashing/)

                

                *   [Memory Management](https://brpc.apache.org/docs/rpc-in-depth/memory-management/)

                

                *   [Timer keeping](https://brpc.apache.org/docs/rpc-in-depth/timer-keeping/)

                

                *   [bthread_id](https://brpc.apache.org/docs/rpc-in-depth/bthread_id/)

                

        *   [Community](https://brpc.apache.org/docs/community/)

        
            *   [Community](https://brpc.apache.org/docs/community/community/)[Mailing List](https://brpc.apache.org/docs/community/mailing_list/)[Contribute Guide](https://brpc.apache.org/docs/community/contributing/)[Committer Guide](https://brpc.apache.org/docs/community/committer/)[Release Guide](https://brpc.apache.org/docs/community/release/)[Committers](https://brpc.apache.org/docs/community/committers/)
                *   [Security](https://brpc.apache.org/docs/community/security/)

                
                    *   [CVE-2023-31039](https://brpc.apache.org/docs/community/security/cve-2023-31039-bugfix/)

[Monthly Meeting](https://brpc.apache.org/docs/community/monthly-meeting/)[On Call](https://brpc.apache.org/docs/community/on-call/)

[ASF](https://brpc.apache.org/docs/asf/)[Users](https://brpc.apache.org/docs/users/)
        *   [Use cases inside Baidu](https://brpc.apache.org/docs/use-cases-inside-baidu/)

        
            *                   *   [百度地图api入口](https://brpc.apache.org/docs/use-cases-inside-baidu/use-case1/)

                

                *   [联盟DSP](https://brpc.apache.org/docs/use-cases-inside-baidu/use-case2/)

                

                *   [ELF学习框架](https://brpc.apache.org/docs/use-cases-inside-baidu/use-case3/)

                

                *   [云平台代理服务](https://brpc.apache.org/docs/use-cases-inside-baidu/use-case4/)

                

[FAQ](https://brpc.apache.org/docs/faq/)
        *   [Blog](https://brpc.apache.org/docs/blogs/)

        
            *                   *   [Release](https://brpc.apache.org/docs/blogs/releases/)

                
                    *   [bRPC 1.5.0](https://brpc.apache.org/docs/blogs/releases/1.5.0/)[bRPC 1.4.0](https://brpc.apache.org/docs/blogs/releases/1.4.0/)[bRPC 1.3.0](https://brpc.apache.org/docs/blogs/releases/1.3.0/)[bRPC 1.2.0](https://brpc.apache.org/docs/blogs/releases/1.2.0/)[bRPC 1.1.0](https://brpc.apache.org/docs/blogs/releases/1.1.0/)[bRPC 1.0.0](https://brpc.apache.org/docs/blogs/releases/1.0.0/)

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/RPC%20in%20depth/Consistent%20Hashing/_index.md)[Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Consistent%20Hashing)[Create project issue](https://github.com/apache/brpc/issues/new)

1.   [Docs](https://brpc.apache.org/docs/)
2.   [RPC in depth](https://brpc.apache.org/docs/rpc-in-depth/)
3.   [Consistent Hashing](https://brpc.apache.org/docs/rpc-in-depth/consistent-hashing/)

Consistent Hashing
==================

Learn about bRPC consistent hashing.

概述
==

一些场景希望同样的请求尽量落到一台机器上，比如访问缓存集群时，我们往往希望同一种请求能落到同一个后端上，以充分利用其上已有的缓存，不同的机器承载不同的稳定working set。而不是随机地散落到所有机器上，那样的话会迫使所有机器缓存所有的内容，最终由于存不下形成颠簸而表现糟糕。 我们都知道hash能满足这个要求，比如当有n台服务器时，输入x总是会发送到第hash(x) % n台服务器上。但当服务器变为m台时，hash(x) % n和hash(x) % m很可能都不相等，这会使得几乎所有请求的发送目的地都发生变化，如果目的地是缓存服务，所有缓存将失效，继而对原本被缓存遮挡的数据库或计算服务造成请求风暴，触发雪崩。一致性哈希是一种特殊的哈希算法，在增加服务器时，发向每个老节点的请求中只会有一部分转向新节点，从而实现平滑的迁移。[这篇论文](http://blog.phpdr.net/wp-content/uploads/2012/08/Consistent-Hashing-and-Random-Trees.pdf)中提出了一致性hash的概念。

一致性hash满足以下四个性质：

*   平衡性 (Balance) : 每个节点被选到的概率是O(1/n)。
*   单调性 (Monotonicity) : 当新节点加入时， 不会有请求在老节点间移动， 只会从老节点移动到新节点。当有节点被删除时，也不会影响落在别的节点上的请求。
*   分散性 (Spread) : 当上游的机器看到不同的下游列表时(在上线时及不稳定的网络中比较常见), 同一个请求尽量映射到少量的节点中。
*   负载 (Load) : 当上游的机器看到不同的下游列表的时候， 保证每台下游分到的请求数量尽量一致。

实现方式
====

所有server的32位hash值在32位整数值域上构成一个环(Hash Ring)，环上的每个区间和一个server唯一对应，如果一个key落在某个区间内， 它就被分流到对应的server上。

![Image 2: img](https://brpc.apache.org/images/docs/chash.png)

当删除一个server的，它对应的区间会归属于相邻的server，所有的请求都会跑过去。当增加一个server时，它会分割某个server的区间并承载落在这个区间上的所有请求。单纯使用Hash Ring很难满足我们上节提到的属性，主要两个问题：

*   在机器数量较少的时候， 区间大小会不平衡。
*   当一台机器故障的时候， 它的压力会完全转移到另外一台机器， 可能无法承载。

为了解决这个问题，我们为每个server计算m个hash值，从而把32位整数值域划分为n*m个区间，当key落到某个区间时，分流到对应的server上。那些额外的hash值使得区间划分更加均匀，被称为虚拟节点（Virtual Node）。当删除一个server时，它对应的m个区间会分别合入相邻的区间中，那个server上的请求会较为平均地转移到其他server上。当增加server时，它会分割m个现有区间，从对应server上分别转移一些请求过来。

由于节点故障和变化不常发生，我们选择了修改复杂度为O(n)的有序数组来存储hash ring，每次分流使用二分查找来选择对应的机器，由于存储是连续的，查找效率比基于平衡二叉树的实现高。线程安全性请参照[Double Buffered Data](https://brpc.apache.org/docs/rpc-in-depth/locality-aware/#doublybuffereddata)章节.

使用方式
====

我们内置了分别基于murmurhash3和md5两种hash算法的实现，使用要做两件事：

*   在Channel.Init 时指定 _load\_balancer\_name_ 为 “c_murmurhash” 或 “c_md5”。
*   发起rpc时通过Controller::set_request_code(uint64_t)填入请求的hash code。

> request的hash算法并不需要和lb的hash算法保持一致，只需要hash的值域是32位无符号整数。由于memcache默认使用md5，访问memcached集群时请选择c_md5保证兼容性，其他场景可以选择c_murmurhash以获得更高的性能和更均匀的分布。

虚拟节点个数
======

通过-chash_num_replicas可设置默认的虚拟节点个数，默认值为100。对于某些特殊场合，对虚拟节点个数有自定义的需求，可以通过将 _load\_balancer\_name_ 加上参数replicas=配置，如：

```c++
channel.Init("http://...", "c_murmurhash:replicas=150", &options);
```

* * *

Last modified February 26, 2022: [brpc website 1.0 fix links jump problem in overview page (14eec1ac1)](https://github.com/apache/brpc-website/commit/14eec1ac1805c1dde9f10d0353984bde2127294c)

*   [](https://github.com/apache/brpc)

© 2026 The Apache Software Foundation. Apache and the Apache feather logo are trademarks of The Apache Software Foundation. All Rights Reserved

[Foundation](https://www.apache.org/) | [License](https://www.apache.org/licenses/) | [Security](https://www.apache.org/security/) | [Events](https://www.apache.org/events/current-event) | [Sponsorship](https://www.apache.org/foundation/sponsorship.html) | [Privacy](https://privacy.apache.org/policies/privacy-policy-public.html) | [Thanks](https://www.apache.org/foundation/thanks.html)
