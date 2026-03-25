# Source: https://zipkin.io/pages/tracers_instrumentation

Title: Tracers and Instrumentation · OpenZipkin

URL Source: https://zipkin.io/pages/tracers_instrumentation

Markdown Content:
Tracing information is collected on each host using the instrumented libraries and sent to Zipkin. When the host makes a request to another application, it passes a few tracing identifiers along with the request to Zipkin so we can later tie the data together into spans.

The following libraries exist to provide instrumentation on various platforms. Please refer to their individual documentation for setup and configuration guides.

### Supported

The following libraries are supported by the Zipkin team. You can reach out to the team on [Gitter](https://gitter.im/openzipkin/zipkin/) chat.

| Language | Library | Framework | Propagation Supported | Transports Supported | Sampling Supported? | Other notes |
| --- | --- | --- | --- | --- | --- | --- |
| C# | [Zipkin4net](https://github.com/openzipkin/zipkin4net) | Asp.net core, Owin | Http (B3) | Any | Yes |  |
| Go | [zipkin-go](https://github.com/openzipkin/zipkin-go) | standard Go middlewares | Http (B3), gRPC (B3) | Http (v2), Kafka (v2), Log | Yes | Uses Zipkin V2 API |
| Java | [brave](https://github.com/openzipkin/brave) | Jersey, gRPC, JAXRS2, Apache HttpClient, Kafka, JMS, Mysql, and many more! | Http (B3), RPC (B3), Messaging (B3) | Same as [zipkin-reporter-brave](https://github.com/openzipkin/zipkin-reporter-java/tree/master/brave) | Yes | Java 6 or higher |
| JavaScript | [zipkin-js](https://github.com/openzipkin/zipkin-js) | [cujoJS](http://cujojs.com/), [express](http://expressjs.com/), [restify](http://restify.com/) | Http (B3) | [Http, Kafka, Scribe](https://github.com/openzipkin/zipkin-js#transports) | Yes | Uses continuation-local-storage under to hood, so you don’t have to pass around an explicit context |
| Ruby | [zipkin-ruby](https://github.com/openzipkin/zipkin-ruby) | [Rack](http://rack.github.io/) | Http (B3) | Http, Kafka, Scribe | Yes | lc support. Ruby 2.0 or higher |
| Scala | [zipkin-finagle](https://github.com/openzipkin/zipkin-finagle) | [Finagle](https://github.com/twitter/finagle) | Http (B3), Thrift | Http, Kafka, Scribe | Yes | Library is written in Java. Propagation is defined in Finagle itself. |
| PHP | [zipkin-php](https://github.com/openzipkin/zipkin-php) | Any | B3 | http, log file | Yes | V2 native based on brave’s model, compatible with PHP 5.6 and PHP 7.x. Check [this](https://github.com/openzipkin/zipkin-php-example) out for an example. |
| Java | [brave-cassandra](https://github.com/openzipkin/brave-cassandra) | [Apache Cassandra](https://cassandra.apache.org/) | CQL (B3) | Same as [zipkin-reporter-brave](https://github.com/openzipkin/zipkin-reporter-java/tree/master/brave) | Yes | Java 8+ |

| Language | Library | Framework | Propagation Supported | Transports Supported | Sampling Supported? | Other notes |
| --- | --- | --- | --- | --- | --- | --- |
| Go | [zipkin-go-opentracing](https://github.com/openzipkin-contrib/zipkin-go-opentracing) | [Go kit](https://gokit.io/), or roll your own with [OpenTracing](http://opentracing.io/) | Http (B3), gRPC (B3) | Http, Kafka, Scribe | Yes |  |
| Go | [zipkintracing](https://github.com/labstack/echo-contrib/tree/master/zipkintracing) | [Echo](https://echo.labstack.com/) | Http (B3), easy to add others | Http | Yes |  |
| Java | [cassandra-zipkin-tracing](https://github.com/thelastpickle/cassandra-zipkin-tracing) | [Apache Cassandra](https://cassandra.apache.org/) | CQL (B3) | Http, Kafka, Scribe | Yes | Java 8+ |
| Java | [Spring Cloud Sleuth](https://github.com/spring-cloud/spring-cloud-sleuth) | Spring, Spring Cloud (e.g. Stream, Netflix) | Http (B3), Messaging (B3) | Http, Spring Cloud Stream Compatible (e.g. RabbitMQ, Kafka, Redis or anything with a custom Binder) | Yes | Java 7 or higher |
| Java | [Micrometer Tracing](https://github.com/micrometer-metrics/tracing) | Spring Boot 3+ | B3, W3C | Http | Yes | Java 8+ |
| Java | [Wingtips](https://github.com/Nike-Inc/wingtips) | [Any Servlet API framework](https://github.com/Nike-Inc/wingtips/tree/master/wingtips-servlet-api), [roll-your-own](https://github.com/Nike-Inc/wingtips#generic-application-pseudo-code), [async framework support](https://github.com/Nike-Inc/wingtips#usage-in-reactive-asynchronous-nonblocking-scenarios) | Http (B3) | Http | Yes | Java 7 or higher, [SLF4J MDC support](https://github.com/Nike-Inc/wingtips#mdc_info) for auto-tagging all log messages with tracing info |
| Lua | [Apache APISIX-plugin-zipkin](https://github.com/apache/apisix/tree/master/apisix/plugins/zipkin) | [Apache APISIX](https://apisix.apache.org/) | Http (B3) | Http | Yes | An [Apache APISIX](https://apisix.apache.org/) plugin to enable tracing to a zipkin server. |
| Python | [py_zipkin](https://github.com/Yelp/py_zipkin) | Any | Http (B3) | Pluggable | [Yes](https://github.com/Yelp/py_zipkin/blob/2b1218ea6438fa7fd35946092de58496f4f759dd/py_zipkin/zipkin.py#L97) | Generic python tracer, used in pyramid-zipkin; py2, py3 support. |
| Python | [pyramid_zipkin](https://github.com/Yelp/pyramid_zipkin) | [Pyramid](http://docs.pylonsproject.org/projects/pyramid/en/latest/) | Http (B3) | [Kafka | Scribe](http://pyramid-zipkin.readthedocs.org/en/latest/configuring_zipkin.html#zipkin-transport-handler) | [Yes](http://pyramid-zipkin.readthedocs.org/en/latest/configuring_zipkin.html#zipkin-tracing-percent) | py2, py3 support. |
| Python | [swagger_zipkin](https://github.com/Yelp/swagger_zipkin) | Swagger ([Bravado](http://bravado.readthedocs.io/en/latest/)), to be used with [py_zipkin](https://github.com/Yelp/py_zipkin) | Http (B3) | [Kafka | Scribe](http://pyramid-zipkin.readthedocs.org/en/latest/configuring_zipkin.html#zipkin-transport-handler) | [Yes](http://pyramid-zipkin.readthedocs.org/en/latest/configuring_zipkin.html#zipkin-tracing-percent) | Uses py_zipkin; py2, py3 support. |
| Python | [aiozipkin](https://github.com/aio-libs/aiozipkin) | [asyncio](https://docs.python.org/3/library/asyncio.html) | Http (B3) | Http | [Yes](https://github.com/aio-libs/aiozipkin/blob/a1a239d6f5a42fce35ecc9810c09eb4ac1d89780/aiozipkin/tracer.py#L9-L10) | Supported python 3.5+ and native coroutines. |
| Scala | [kamon-zipkin](https://kamon.io/docs/latest/reporters/zipkin/) | [akka](https://doc.akka.io/docs/akka/current/index.html), [akka-http](https://doc.akka.io/docs/akka-http/current/index.html), | Http (B3) | Http | Yes | Toolkit for tracing and monitoring for jvm based applications |
| Scala | [sttp](https://github.com/softwaremill/sttp) | [akka-http](https://doc.akka.io/docs/akka-http/current/index.html), [async-http-client](https://github.com/AsyncHttpClient/async-http-client) | Http (B3) | Http | Yes | Brave-based wrapper for any http backend implemented using sttp’s interface |
| PHP | [zipkin-php-opentracing](https://github.com/jcchavezs/zipkin-php-opentracing) | Any | B3 | http, log file | Yes | Zipkin V2 client with OpenTracing API |
| Java | [kafka-interceptor-zipkin](https://github.com/openzipkin-contrib/kafka-interceptor-zipkin) | [Apache Kafka](https://kafka.apache.org/) | B3 | Http, Kafka | Yes | Java 8+, meant to be used for off-the-shelf components like Kafka Connectors, KSQL or Kafka REST Proxy. Instrumentation for Kafka Clients and Kafka Streams are included as Brave instrumentation. |
| Go | [zipkin-go-sql](https://github.com/openzipkin-contrib/zipkin-go-sql) | Any |  |  |  | SQL instrumentation for Go database/sql |
| PHP | [zipkin-instrumentation-symfony](https://github.com/jcchavezs/zipkin-instrumentation-symfony) | [Symfony](https://symfony.com/) | B3 | http, log file | Yes | A Zipkin integration for Symfony applications |
| Several | [opentelemetry](https://opentelemetry.io/) | Any | B3, W3C | Http | Yes | Toolkit for observability, with prebuilt instrumentation for many libraries in several languages. |

Did we miss a library? Please open a pull-request to [openzipkin.github.io](https://github.com/openzipkin/openzipkin.github.io).

Want to create instrumentation for another framework or platform? We have documentation on [instrumenting a library](https://zipkin.io/pages/instrumenting).
