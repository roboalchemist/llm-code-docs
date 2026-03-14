# Source: https://brpc.apache.org/docs/rpc-in-depth/bthread_id/

Title: bthread_id

URL Source: https://brpc.apache.org/docs/rpc-in-depth/bthread_id/

Markdown Content:
bthread_id | bRPC
===============
bthread_id | bRPC
===============
[](https://brpc.apache.org/)

*   [GitHub](https://github.com/apache/brpc/)
*   [Download](https://brpc.apache.org/docs/downloadbrpc/)
*   [Docs](https://brpc.apache.org/docs/)
*   [Community](https://brpc.apache.org/docs/community/community/)
*   [ASF](https://brpc.apache.org/docs/asf/)
*   [Blog](https://brpc.apache.org/docs/blogs/)
*   [Users](https://brpc.apache.org/docs/users/)
*   [English](https://brpc.apache.org/docs/rpc-in-depth/bthread_id/#)[中文](https://brpc.apache.org/zh/) 

[English](https://brpc.apache.org/docs/rpc-in-depth/bthread_id/#)

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

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/RPC%20in%20depth/bthread_id/_index.md)[Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=bthread_id)[Create project issue](https://github.com/apache/brpc/issues/new)

1.   [Docs](https://brpc.apache.org/docs/)
2.   [RPC in depth](https://brpc.apache.org/docs/rpc-in-depth/)
3.   [bthread_id](https://brpc.apache.org/docs/rpc-in-depth/bthread_id/)

bthread_id
==========

Learn about bRPC bthread_id.

bthread_id是一个特殊的同步结构，它可以互斥RPC过程中的不同环节，也可以O(1)时间内找到RPC上下文(即Controller)。注意，这里我们谈论的是bthread_id_t，不是bthread_t（bthread的tid），这个名字起的确实不太好，容易混淆。

具体来说，bthread_id解决的问题有：

*   在发送RPC过程中response回来了，处理response的代码和发送代码产生竞争。
*   设置timer后很快触发了，超时处理代码和发送代码产生竞争。
*   重试产生的多个response同时回来产生的竞争。
*   通过correlation_id在O(1)时间内找到对应的RPC上下文，而无需建立从correlation_id到RPC上下文的全局哈希表。
*   取消RPC。

上文提到的bug在其他rpc框架中广泛存在，下面我们来看下brpc是如何通过bthread_id解决这些问题的。

bthread_id包括两部分，一个是用户可见的64位id，另一个是对应的不可见的bthread::Id结构体。用户接口都是操作id的。从id映射到结构体的方式和brpc中的[其他结构](https://brpc.apache.org/docs/rpc-in-depth/memory-management/)类似：32位是内存池的位移，32位是version。前者O(1)时间定位，后者防止ABA问题。

bthread_id的接口不太简洁，有不少API：

*   create
*   lock
*   unlock
*   unlock_and_destroy
*   join
*   error

这么多接口是为了满足不同的使用流程。

*   发送request的流程：bthread_id_create -> bthread_id_lock -> … register timer and send RPC … -> bthread_id_unlock
*   接收response的流程：bthread_id_lock -> ..process response -> bthread_id_unlock_and_destroy
*   异常处理流程：timeout/socket fail -> bthread_id_error -> 执行on_error回调(这里会加锁)，分两种情况
    *   请求重试/backup request： 重新register timer and send RPC -> bthread_id_unlock
    *   无法重试，最终失败：bthread_id_unlock_and_destroy

*   同步等待RPC结束：bthread_id_join

为了减少等待，bthread_id做了一些优化的机制：

*   error发生的时候，如果bthread_id已经被锁住，会把error信息放到一个pending queue中，bthread_id_error函数立即返回。当bthread_id_unlock的时候，如果pending queue里面有任务就取出来执行。
*   RPC结束的时候，如果存在用户回调，先执行一个bthread_id_about_to_destroy，让正在等待的bthread_id_lock操作立即失败，再执行用户回调（这个可能耗时较长，不可控），最后再执行bthread_id_unlock_and_destroy

* * *

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

*   [](https://github.com/apache/brpc)

© 2026 The Apache Software Foundation. Apache and the Apache feather logo are trademarks of The Apache Software Foundation. All Rights Reserved

[Foundation](https://www.apache.org/) | [License](https://www.apache.org/licenses/) | [Security](https://www.apache.org/security/) | [Events](https://www.apache.org/events/current-event) | [Sponsorship](https://www.apache.org/foundation/sponsorship.html) | [Privacy](https://privacy.apache.org/policies/privacy-policy-public.html) | [Thanks](https://www.apache.org/foundation/thanks.html)
