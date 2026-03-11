# Source: https://brpc.apache.org/docs/rpc-in-depth/load-balancing/

Title: Load Balancing

URL Source: https://brpc.apache.org/docs/rpc-in-depth/load-balancing/

Markdown Content:
Load Balancing | bRPC
===============
Load Balancing | bRPC
===============
[](https://brpc.apache.org/)

*   [GitHub](https://github.com/apache/brpc/)
*   [Download](https://brpc.apache.org/docs/downloadbrpc/)
*   [Docs](https://brpc.apache.org/docs/)
*   [Community](https://brpc.apache.org/docs/community/community/)
*   [ASF](https://brpc.apache.org/docs/asf/)
*   [Blog](https://brpc.apache.org/docs/blogs/)
*   [Users](https://brpc.apache.org/docs/users/)
*   [English](https://brpc.apache.org/docs/rpc-in-depth/load-balancing/#)[中文](https://brpc.apache.org/zh/) 

[English](https://brpc.apache.org/docs/rpc-in-depth/load-balancing/#)

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

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/RPC%20in%20depth/Load%20Balancing/_index.md)[Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Load%20Balancing)[Create project issue](https://github.com/apache/brpc/issues/new)

1.   [Docs](https://brpc.apache.org/docs/)
2.   [RPC in depth](https://brpc.apache.org/docs/rpc-in-depth/)
3.   [Load Balancing](https://brpc.apache.org/docs/rpc-in-depth/load-balancing/)

Load Balancing
==============

Learn about bRPC load balancing.

上游一般通过命名服务发现所有的下游节点，并通过多种负载均衡方法把流量分配给下游节点。当下游节点出现问题时，它可能会被隔离以提高负载均衡的效率。被隔离的节点定期被健康检查，成功后重新加入正常节点。

命名服务
====

在brpc中，[NamingService](https://github.com/brpc/brpc/blob/master/src/brpc/naming_service.h)用于获得服务名对应的所有节点。一个直观的做法是定期调用一个函数以获取最新的节点列表。但这会带来一定的延时（定期调用的周期一般在若干秒左右），作为通用接口不太合适。特别当命名服务提供事件通知时(比如zk)，这个特性没有被利用。所以我们反转了控制权：不是我们调用用户函数，而是用户在获得列表后调用我们的接口，对应[NamingServiceActions](https://github.com/brpc/brpc/blob/master/src/brpc/naming_service.h)。当然我们还是得启动进行这一过程的函数，对应NamingService::RunNamingService。下面以三个实现解释这套方式：

*   bns：没有事件通知，所以我们只能定期去获得最新列表，默认间隔是[5秒](http://brpc.baidu.com:8765/flags/ns_access_interval)。为了简化这类定期获取的逻辑，brpc提供了[PeriodicNamingService](https://github.com/brpc/brpc/blob/master/src/brpc/periodic_naming_service.h) 供用户继承，用户只需要实现单次如何获取（GetServers）。获取后调用NamingServiceActions::ResetServers告诉框架。框架会对列表去重，和之前的列表比较，通知对列表有兴趣的观察者(NamingServiceWatcher)。这套逻辑会运行在独立的bthread中，即NamingServiceThread。一个NamingServiceThread可能被多个Channel共享，通过intrusive_ptr管理ownership。
*   file：列表即文件。合理的方式是在文件更新后重新读取。[该实现](https://github.com/brpc/brpc/blob/master/src/brpc/policy/file_naming_service.cpp)使用[FileWatcher](https://github.com/brpc/brpc/blob/master/src/butil/files/file_watcher.h)关注文件的修改时间，当文件修改后，读取并调用NamingServiceActions::ResetServers告诉框架。
*   list：列表就在服务名里（逗号分隔）。在读取完一次并调用NamingServiceActions::ResetServers后就退出了，因为列表再不会改变了。

如果用户需要建立这些对象仍然是不够方便的，因为总是需要一些工厂代码根据配置项建立不同的对象，鉴于此，我们把工厂类做进了框架，并且是非常方便的形式：

```
"protocol://service-name"
 
e.g.
bns://<node-name>            # baidu naming service
file://<file-path>           # load addresses from the file
list://addr1,addr2,...       # use the addresses separated by comma
http://<url>                 # Domain Naming Service, aka DNS.
```

这套方式是可扩展的，实现了新的NamingService后在[global.cpp](https://github.com/brpc/brpc/blob/master/src/brpc/global.cpp)中依葫芦画瓢注册下就行了，如下图所示：

![Image 3: img](https://brpc.apache.org/images/docs/register_ns.png)

看到这些熟悉的字符串格式，容易联想到ftp:// zk:// galileo://等等都是可以支持的。用户在新建Channel时传入这类NamingService描述，并能把这些描述写在各类配置文件中。

负载均衡
====

brpc中[LoadBalancer](https://github.com/brpc/brpc/blob/master/src/brpc/load_balancer.h)从多个服务节点中选择一个节点，目前的实现见[负载均衡](https://brpc.apache.org/docs/client/basics/#load-balancer)。

Load balancer最重要的是如何让不同线程中的负载均衡不互斥，解决这个问题的技术是[DoublyBufferedData](https://brpc.apache.org/docs/rpc-in-depth/locality-aware/#doublybuffereddata)。

和NamingService类似，我们使用字符串来指代一个load balancer，在global.cpp中注册：

![Image 4: img](https://brpc.apache.org/images/docs/register_lb.png)

健康检查
====

对于那些无法连接却仍在NamingService的节点，brpc会定期连接它们，成功后对应的Socket将被”复活“，并可能被LoadBalancer选择上，这个过程就是健康检查。注意：被健康检查或在LoadBalancer中的节点一定在NamingService中。换句话说，只要一个节点不从NamingService删除，它要么是正常的（会被LoadBalancer选上），要么在做健康检查。

传统的做法是使用一个线程做所有连接的健康检查，brpc简化了这个过程：为需要的连接动态创建一个bthread专门做健康检查（Socket::HealthCheckThread）。这个线程的生命周期被对应连接管理。具体来说，当Socket被SetFailed后，健康检查线程就可能启动（如果SocketOptions.health_check_interval为正数的话）：

*   健康检查线程先在确保没有其他人在使用Socket了后关闭连接。目前是通过对Socket的引用计数判断的。这个方法之所以有效在于Socket被SetFailed后就不能被Address了，所以引用计数只减不增。
*   定期连接直到远端机器被连接上，在这个过程中，如果Socket析构了，那么该线程也就随之退出了。
*   连上后复活Socket(Socket::Revive)，这样Socket就又能被其他地方，包括LoadBalancer访问到了（通过Socket::Address）。

* * *

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

*   [](https://github.com/apache/brpc)

© 2026 The Apache Software Foundation. Apache and the Apache feather logo are trademarks of The Apache Software Foundation. All Rights Reserved

[Foundation](https://www.apache.org/) | [License](https://www.apache.org/licenses/) | [Security](https://www.apache.org/security/) | [Events](https://www.apache.org/events/current-event) | [Sponsorship](https://www.apache.org/foundation/sponsorship.html) | [Privacy](https://privacy.apache.org/policies/privacy-policy-public.html) | [Thanks](https://www.apache.org/foundation/thanks.html)
