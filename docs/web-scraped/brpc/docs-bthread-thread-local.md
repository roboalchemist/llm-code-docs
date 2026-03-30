# Source: https://brpc.apache.org/docs/bthread/thread-local/

Title: thread-local

URL Source: https://brpc.apache.org/docs/bthread/thread-local/

Markdown Content:
thread-local | bRPC
===============
thread-local | bRPC
===============
[](https://brpc.apache.org/)

*   [GitHub](https://github.com/apache/brpc/)
*   [Download](https://brpc.apache.org/docs/downloadbrpc/)
*   [Docs](https://brpc.apache.org/docs/)
*   [Community](https://brpc.apache.org/docs/community/community/)
*   [ASF](https://brpc.apache.org/docs/asf/)
*   [Blog](https://brpc.apache.org/docs/blogs/)
*   [Users](https://brpc.apache.org/docs/users/)
*   [English](https://brpc.apache.org/docs/bthread/thread-local/#)[中文](https://brpc.apache.org/zh/docs/bthread/thread-local/) 

[English](https://brpc.apache.org/docs/bthread/thread-local/#)

[中文](https://brpc.apache.org/zh/docs/bthread/thread-local/)

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

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/bthread/thread-local/_index.md)[Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=thread-local)[Create project issue](https://github.com/apache/brpc/issues/new)

1.   [Docs](https://brpc.apache.org/docs/)
2.   [bthread](https://brpc.apache.org/docs/bthread/)
3.   [thread-local](https://brpc.apache.org/docs/bthread/thread-local/)

thread-local
============

The thread-local problem.

本页说明bthread下使用pthread-local可能会导致的问题。bthread-local的使用方法见[这里](https://brpc.apache.org/docs/server/basics/#bthread-local)。

thread-local问题
==============

调用阻塞的bthread函数后，所在的pthread很可能改变，这使[pthread_getspecific](http://linux.die.net/man/3/pthread_getspecific)，[gcc __thread](https://gcc.gnu.org/onlinedocs/gcc-4.2.4/gcc/Thread_002dLocal.html)和c++11 thread_local变量，pthread_self()等的值变化了，如下代码的行为是不可预计的：

```
thread_local SomeObject obj;
...
SomeObject* p = &obj;
p->bar();
bthread_usleep(1000);
p->bar();
```

bthread_usleep之后，该bthread很可能身处不同的pthread，这时p指向了之前pthread的thread_local变量，继续访问p的结果无法预计。这种使用模式往往发生在用户使用线程级变量传递业务变量的情况。为了防止这种情况，应该谨记：

*   不使用线程级变量传递业务数据。这是一种槽糕的设计模式，依赖线程级数据的函数也难以单测。判断是否滥用：如果不使用线程级变量，业务逻辑是否还能正常运行？线程级变量应只用作优化手段，使用过程中不应直接或间接调用任何可能阻塞的bthread函数。比如使用线程级变量的tcmalloc就不会和bthread有任何冲突。
*   如果一定要（在业务中）使用线程级变量，使用bthread_key_create和bthread_getspecific。

gcc4下的errno问题
=============

gcc4会优化[标记为__attribute__((**const**))](https://gcc.gnu.org/onlinedocs/gcc/Function-Attributes.html#index-g_t_0040code_007bconst_007d-function-attribute-2958)的函数，这个标记大致指只要参数不变，输出就不会变。所以当一个函数中以相同参数出现多次时，gcc4会合并为一次。比如在我们的系统中errno是内容为*__errno_location()的宏，这个函数的签名是：

```
/* Function to get address of global `errno' variable.  */
extern int *__errno_location (void) __THROW __attribute__ ((__const__));
```

由于此函数被标记为`__const__`，且没有参数，当你在一个函数中调用多次errno时，可能只有第一次才调用__errno_location()，而之后只是访问其返回的`int*`。在pthread中这没有问题，因为返回的`int*`是thread-local的，一个给定的pthread中是不会变化的。但是在bthread中，这是不成立的，因为一个bthread很可能在调用一些函数后跑到另一个pthread去，如果gcc4做了类似的优化，即一个函数内所有的errno都替换为第一次调用返回的int*，这中间bthread又切换了pthread，那么可能会访问之前pthread的errno，从而造成未定义行为。

比如下文是一种errno的使用场景：

```
Use errno ...   (original pthread)
bthread functions that may switch to another pthread.
Use errno ...   (another pthread)
```

我们期望看到的行为：

```
Use *__errno_location() ...  -  the thread-local errno of original pthread
bthread may switch another pthread ...
Use *__errno_location() ...  -  the thread-local errno of another pthread
```

使用gcc4时的实际行为：

```
int* p= __errno_location();
Use *p ...                   -  the thread-local errno of original pthread
bthread context switches ...
Use *p ...                   -  still the errno of original pthread, undefined behavior!!
```

严格地说这个问题不是gcc4导致的，而是glibc给__errno_location的签名不够准确，一个返回thread-local指针的函数依赖于段寄存器（TLS的一般实现方式），这怎么能算const呢？由于我们还未找到覆盖__errno_location的方法，所以这个问题目前实际的解决方法是：

**务必在直接或间接使用bthread的项目的gcc编译选项中添加`-D__const__=`，即把`__const__`定义为空，避免gcc4做相关优化。**

把`__const__`定义为空对程序其他部分的影响几乎为0。另外如果你没有**直接**使用errno（即你的项目中没有出现errno），或使用的是gcc 3.4，即使没有定义`-D__const__=`，程序的正确性也不会受影响，但为了防止未来可能的问题，我们强烈建议加上。

需要说明的是，和errno类似，pthread_self也有类似的问题，不过一般pthread_self除了打日志没有其他用途，影响面较小，在`-D__const__=`后pthread_self也会正常。

* * *

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

*   [](https://github.com/apache/brpc)

© 2026 The Apache Software Foundation. Apache and the Apache feather logo are trademarks of The Apache Software Foundation. All Rights Reserved

[Foundation](https://www.apache.org/) | [License](https://www.apache.org/licenses/) | [Security](https://www.apache.org/security/) | [Events](https://www.apache.org/events/current-event) | [Sponsorship](https://www.apache.org/foundation/sponsorship.html) | [Privacy](https://privacy.apache.org/policies/privacy-policy-public.html) | [Thanks](https://www.apache.org/foundation/thanks.html)
