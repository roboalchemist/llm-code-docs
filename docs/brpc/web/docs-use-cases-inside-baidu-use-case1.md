# Source: https://brpc.apache.org/docs/use-cases-inside-baidu/use-case1/

Title: 百度地图api入口

URL Source: https://brpc.apache.org/docs/use-cases-inside-baidu/use-case1/

Markdown Content:
百度地图api入口 | bRPC
===============
百度地图api入口 | bRPC
===============
[](https://brpc.apache.org/)

*   [GitHub](https://github.com/apache/brpc/)
*   [Download](https://brpc.apache.org/docs/downloadbrpc/)
*   [Docs](https://brpc.apache.org/docs/)
*   [Community](https://brpc.apache.org/docs/community/community/)
*   [ASF](https://brpc.apache.org/docs/asf/)
*   [Blog](https://brpc.apache.org/docs/blogs/)
*   [Users](https://brpc.apache.org/docs/users/)
*   [English](https://brpc.apache.org/docs/use-cases-inside-baidu/use-case1/#)[中文](https://brpc.apache.org/zh/) 

[English](https://brpc.apache.org/docs/use-cases-inside-baidu/use-case1/#)

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

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Use%20cases%20inside%20Baidu/Use%20case1/_index.md)[Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=%e7%99%be%e5%ba%a6%e5%9c%b0%e5%9b%beapi%e5%85%a5%e5%8f%a3)[Create project issue](https://github.com/apache/brpc/issues/new)

1.   [Docs](https://brpc.apache.org/docs/)
2.   [Use cases inside Baidu](https://brpc.apache.org/docs/use-cases-inside-baidu/)
3.   [百度地图api入口](https://brpc.apache.org/docs/use-cases-inside-baidu/use-case1/)

百度地图api入口
=========

Use case1：百度地图api入口。

进展
==

| 时间 | 内容 | 说明 |
| --- | --- | --- |
| 8.11 - 8.28 | 调研 + 研发 + 自测 | 自测性能报告见附件 |
| 9.8 - 9.22 | QA测试 | QA测试报告见附件 |
| 10.8 | 北京机房1台机器上线 |  |
| 10.14 | 北京机房1台机器上线 | 修复URL编码问题 |
| 10.19 | 北京机房7/35机器上线杭州和南京各2台机器上线 | 开始小流量上线 |
| 10.22 | 北京机房10/35机器上线杭州机房5/26机器上线南京机房5/19机器上线 | 修复http响应数据压缩问题 |
| 11.3 | 北京机房10/35机器上线 | 修复RPC内存泄露问题 |
| 11.6 | 杭州机房5/26机器上线南京机房5/19机器上线 | 同北京机房版本 |
| 11.9 | 北京机房全流量上线 |  |

截止目前，线上服务表现稳定。

QA测试结论
======

1.   【性能测试】单机支持最大QPS：**9000+**。可以有效解决原来hulu_pbrpc中一个慢服务拖垮所有服务的问题。性能很好。
2.   【稳定性测试】长时间压测没问题。

QA测试结论：通过

性能提升实时统计
========

统计时间2015.11.3 15:00 – 2015.11.9 14:30，共**143.5**小时（近6天）不间断运行。北京机房升级前和升级后同机房各6台机器，共**12**台线上机器的Noah监控数据。

| 指标 | 升级**前**均值hulu_pbrpc | 升级**后**均值brpc | 收益对比 | 说明 |
| --- | --- | --- | --- | --- |
| CPU占用率 | 67.35% | 29.28% | 降低**56.53**% |  |
| 内存占用 | 327.81MB | 336.91MB | 基本持平 |  |
| 鉴权平响(ms) | 0.605 | 0.208 | 降低**65.62**% |  |
| 转发平响(ms) | 22.49 | 23.18 | 基本持平 | 依赖后端各个服务的性能 |
| 总线程数 | 193 | 132 | 降低**31.61**% | Baidu RPC版本线程数使用率较低，还可降低 |
| 极限QPS | 3000 | 9000 | 提升**3**倍 | 线下使用Geoconv和Geocoder服务测试 |

**CPU使用率(%)**（红色为升级前，蓝色为升级后） ![Image 6: img](https://brpc.apache.org/images/docs/apicontrol_compare_1.png)

**内存使用量(KB)**（红色为升级前，蓝色为升级后） ![Image 7: img](https://brpc.apache.org/images/docs/apicontrol_compare_2.png)

**鉴权平响(ms)**（红色为升级前，蓝色为升级后） ![Image 8: img](https://brpc.apache.org/images/docs/apicontrol_compare_3.png)

**转发平响(ms)**（红色为升级前，蓝色为升级后） ![Image 9: img](https://brpc.apache.org/images/docs/apicontrol_compare_4.png)

**总线程数(个)**（红色为升级前，蓝色为升级后） ![Image 10: img](https://brpc.apache.org/images/docs/apicontrol_compare_5.png)

* * *

Last modified January 30, 2022: [bRPC website 1.0 (92b925e8f)](https://github.com/apache/brpc-website/commit/92b925e8fd3d8cd6c4fa35c4952566725017b914)

*   [](https://github.com/apache/brpc)

© 2026 The Apache Software Foundation. Apache and the Apache feather logo are trademarks of The Apache Software Foundation. All Rights Reserved

[Foundation](https://www.apache.org/) | [License](https://www.apache.org/licenses/) | [Security](https://www.apache.org/security/) | [Events](https://www.apache.org/events/current-event) | [Sponsorship](https://www.apache.org/foundation/sponsorship.html) | [Privacy](https://privacy.apache.org/policies/privacy-policy-public.html) | [Thanks](https://www.apache.org/foundation/thanks.html)
