# Source: https://brpc.apache.org/docs/server/json2pb/

Title: json2pb

URL Source: https://brpc.apache.org/docs/server/json2pb/

Markdown Content:
json2pb | bRPC
===============
json2pb | bRPC
===============
[](https://brpc.apache.org/)

*   [GitHub](https://github.com/apache/brpc/)
*   [Download](https://brpc.apache.org/docs/downloadbrpc/)
*   [Docs](https://brpc.apache.org/docs/)
*   [Community](https://brpc.apache.org/docs/community/community/)
*   [ASF](https://brpc.apache.org/docs/asf/)
*   [Blog](https://brpc.apache.org/docs/blogs/)
*   [Users](https://brpc.apache.org/docs/users/)
*   [English](https://brpc.apache.org/docs/server/json2pb/#)[中文](https://brpc.apache.org/zh/docs/server/json2pb/) 

[English](https://brpc.apache.org/docs/server/json2pb/#)

[中文](https://brpc.apache.org/zh/docs/server/json2pb/)

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

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Server/json2pb/_index.md)[Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=json2pb)[Create project issue](https://github.com/apache/brpc/issues/new)

*   [message](https://brpc.apache.org/docs/server/json2pb/#message)
*   [repeated field](https://brpc.apache.org/docs/server/json2pb/#repeated-field)
*   [map](https://brpc.apache.org/docs/server/json2pb/#map)
*   [integers](https://brpc.apache.org/docs/server/json2pb/#integers)
*   [floating point](https://brpc.apache.org/docs/server/json2pb/#floating-point)
*   [enum](https://brpc.apache.org/docs/server/json2pb/#enum)
*   [string](https://brpc.apache.org/docs/server/json2pb/#string)
*   [bytes](https://brpc.apache.org/docs/server/json2pb/#bytes)
*   [bool](https://brpc.apache.org/docs/server/json2pb/#bool)
*   [unknown fields](https://brpc.apache.org/docs/server/json2pb/#unknown-fields)

1.   [Docs](https://brpc.apache.org/docs/)
2.   [Server](https://brpc.apache.org/docs/server/)
3.   [json2pb](https://brpc.apache.org/docs/server/json2pb/)

json2pb
=======

Learn how to transfer json to pb.

brpc支持json和protobuf间的**双向**转化，实现于[json2pb](https://github.com/brpc/brpc/tree/master/src/json2pb/)，json解析使用[rapidjson](https://github.com/miloyip/rapidjson)。此功能对pb2.x和3.x均有效。pb3内置了[转换json](https://developers.google.com/protocol-buffers/docs/proto3#json)的功能。

by design, 通过HTTP + json访问protobuf服务是对外服务的常见方式，故转化必须精准，转化规则列举如下。

message
-------

对应rapidjson Object, 以花括号包围，其中的元素会被递归地解析。

```protobuf
// protobuf
message Foo {
    required string field1 = 1;
    required int32 field2 = 2;  
}
message Bar { 
    required Foo foo = 1; 
    optional bool flag = 2;
    required string name = 3;
}

// rapidjson
{"foo":{"field1":"hello", "field2":3},"name":"Tom" }
```

repeated field
--------------

对应rapidjson Array, 以方括号包围，其中的元素会被递归地解析，和message不同，每个元素的类型相同。

```protobuf
// protobuf
repeated int32 numbers = 1;

// rapidjson
{"numbers" : [12, 17, 1, 24] }
```

特别的，针对仅有一个 `repeated` 类型成员的 `message`，序列化为 `json` 时支持直接序列化为数组，以简化包体。

```protobuf
// protobuf
message Foo {
    required int32 numbers = 1;
}
// rapidjson
[12, 17, 1, 24]
```

该特性默认为关闭状态，客户端在发送请求时，或服务端在发送回复时，可手动开启：

```c++
brpc::Controller cntl;
cntl.set_pb_single_repeated_to_array(true);
```

map
---

满足如下条件的repeated MSG被视作json map :

*   MSG包含一个名为key的字段，类型为string，tag为1。
*   MSG包含一个名为value的字段，tag为2。
*   不包含其他字段。

这种"map"的属性有：

*   自然不能确保key有序或不重复，用户视需求自行检查。
*   与protobuf 3.x中的map二进制兼容，故3.x中的map使用pb2json也会正确地转化为json map。

如果符合所有条件的repeated MSG并不需要被认为是json map，打破上面任一条件就行了: 在MSG中加入optional int32 this_message_is_not_map_entry = 3; 这个办法破坏了“不包含其他字段”这项，且不影响二进制兼容。也可以调换key和value的tag值，让前者为2后者为1，也使条件不再满足。

integers
--------

rapidjson会根据值打上对应的类型标记，比如：

*   对于3，rapidjson中的IsUInt, IsInt, IsUint64, IsInt64等函数均会返回true。
*   对于-1，则IsUInt和IsUint64会返回false。
*   对于5000000000，IsUInt和IsInt是false。

这使得我们不用特殊处理，转化代码就可以自动地把json中的UInt填入protobuf中的int64，而不是机械地认为这两个类型不匹配。相应地，转化代码自然能识别overflow和underflow，当出现时会转化失败。

```protobuf
// protobuf
int32 uint32 int64 uint64

// rapidjson
Int UInt Int64 UInt64
```

floating point
--------------

json的整数类型也可以转至pb的浮点数类型。浮点数(IEEE754)除了普通数字外还接受"NaN", “Infinity”, “-Infinity"三个字符串，分别对应Not A Number，正无穷，负无穷。

```protobuf
// protobuf
float double

// rapidjson
Float Double Int Uint Int64 Uint64
```

enum
----

enum可转化为整数或其名字对应的字符串，可由Pb2JsonOptions.enum_options控制。默认后者。

string
------

默认同名转化。但当json中出现非法C++变量名（pb的变量名规则）时，允许转化，规则是:

`illegal-char <-> **_Z**<ASCII-of-the-char>**_**`

bytes
-----

和string不同，可能包含\0的bytes默认以base64编码。

```protobuf
// protobuf
"Hello, World!"

// json
"SGVsbG8sIFdvcmxkIQo="
```

bool
----

对应json的true false

unknown fields
--------------

unknown_fields → json目前不支持，未来可能支持。json → unknown_fields目前也未支持，即protobuf无法透传json中不认识的字段。原因在于protobuf真正的key是proto文件中每个字段后的数字:

```protobuf
...
required int32 foo = 3; <-- the real key
...
```

这也是unknown_fields的key。当一个protobuf不认识某个字段时，其proto中必然不会有那个数字，所以没办法插入unknown_fields。

可行的方案有几种：

*   确保被json访问的服务的proto文件最新。这样就不需要透传了，但越前端的服务越类似proxy，可能并不现实。
*   protobuf中定义特殊透传字段。比如名为unknown_json_fields，在解析对应的protobuf时特殊处理。此方案修改面广且对性能有一定影响，有明确需求时再议。

* * *

Last modified June 13, 2022: [update getting_start and json2pb docs (#73) (b6b734ea7)](https://github.com/apache/brpc-website/commit/b6b734ea718b3e1e0480b1ef945f6228413126b4)

*   [](https://github.com/apache/brpc)

© 2026 The Apache Software Foundation. Apache and the Apache feather logo are trademarks of The Apache Software Foundation. All Rights Reserved

[Foundation](https://www.apache.org/) | [License](https://www.apache.org/licenses/) | [Security](https://www.apache.org/security/) | [Events](https://www.apache.org/events/current-event) | [Sponsorship](https://www.apache.org/foundation/sponsorship.html) | [Privacy](https://privacy.apache.org/policies/privacy-policy-public.html) | [Thanks](https://www.apache.org/foundation/thanks.html)
