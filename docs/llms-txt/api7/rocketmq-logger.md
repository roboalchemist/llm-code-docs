# Source: https://docs.api7.ai/hub/rocketmq-logger.md

# rocketmq-logger

The `rocketmq-logger` plugin pushes request and response logs as JSON objects to your RocketMQ clusters in batches and supports the customization of log formats.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `rocketmq-logger` plugin for different scenarios.

To follow along the examples, start a sample RocketMQ cluster using the below Docker compose file:

docker-compose.yml

```
version: "3"

services:
  rocketmq_namesrv:
    image: apacherocketmq/rocketmq:4.6.0
    container_name: rmqnamesrv
    restart: unless-stopped
    ports:
      - "9876:9876"
    command: sh mqnamesrv
    networks:
      rocketmq_net:

  rocketmq_broker:
    image: apacherocketmq/rocketmq:4.6.0
    container_name: rmqbroker
    restart: unless-stopped
    ports:
      - "10909:10909"
      - "10911:10911"
      - "10912:10912"
    depends_on:
      - rocketmq_namesrv
    command: sh mqbroker -n rmqnamesrv:9876 -c ../conf/broker.conf
    networks:
      rocketmq_net:

networks:
  rocketmq_net:
```

Start containers:

```
docker compose up -d
```

In a few seconds, the name server and broker should start.

Create the `TopicTest` topic:

```
docker exec -i rmqnamesrv rm /home/rocketmq/rocketmq-4.6.0/conf/tools.yml
docker exec -i rmqnamesrv /home/rocketmq/rocketmq-4.6.0/bin/mqadmin updateTopic -n rmqnamesrv:9876 -t TopicTest -c DefaultCluster 
```

Wait for message in the configured RockerMQ topic:

```
docker run -it --name rockemq_consumer -e NAMESRV_ADDR=localhost:9876 --net host apacherocketmq/rocketmq:4.6.0 sh tools.sh org.apache.rocketmq.example.quickstart.Consumer
```

In a few seconds, the consumer should start and listen for messages from APISIX:

```
01:32:17.823 [main] DEBUG i.n.u.i.l.InternalLoggerFactory - Using SLF4J as the default logging framework
Consumer Started.
```

Open a new terminal session for the following steps working with APISIX.

### Log in Different Meta Log Formats[â](#log-in-different-meta-log-formats "Direct link to Log in Different Meta Log Formats")

The following example demonstrates how you can enable the `rocketmq-logger` plugin on a route, which logs client requests to the route and pushes logs to RocketMQ. You will also understand the differences between the `default` and `origin` meta log formats.

Create a route with `rocketmq-logger` as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "rocketmq-logger-route",
    "uri": "/anything",
    "plugins": {
      "rocketmq-logger": {
        "nameserver_list": [ "127.0.0.1:9876" ],
        "topic": "TopicTest",
        "key": "key1",
        "timeout": 30,
        "meta_format": "default",
        "batch_max_size": 1
      }
    },
    "upstream": {
      "nodes": {
        "httpbin.org:80": 1
      },
      "type": "roundrobin"
    }
  }'
```

â¶ `meta_format`: set to the `default` log format.

â· `batch_max_size`: set to 1 to send the log entry immediately.

Send a request to the route to generate a log entry:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should see a log entry in the other terminal running the consumer:

```
ConsumeMessageThread_1 Receive New Messages: [MessageExt [queueId=0, storeSize=857, queueOffset=0, sysFlag=0, bornTimestamp=1703661585406, bornHost=/172.18.0.1:38362, storeTimestamp=1703661585486, storeHost=/172.18.0.3:10911, msgId=AC12000300002A9F0000000000000000, commitLogOffset=0, bodyCRC=1383911373, reconsumeTimes=0, preparedTransactionOffset=0, toString()=Message{topic='TopicTest', flag=0, properties={MIN_OFFSET=0, MAX_OFFSET=1, KEYS=key1, CONSUME_START_TIME=1703661585635, UNIQ_KEY=7F000001A7045E46ABB3892F67FD0002, CLUSTER=DefaultCluster, WAIT=true}, body=[123, 34, 99, 108, 105, 101, 110, 116, 95, 105, 112, 34, 58, 34, 49, 50, 55, 46, 48, 46, 48, 46, 49, 34, 44, 34, 117, 112, 115, 116, 114, 101, 97, 109, 34, 58, 34, 49, 57, 56, 46, 49, 56, 46, 49, 46, 57, 50, 58, 56, 48, 34, 44, 34, 115, 116, 97, 114, 116, 95, 116, 105, 109, 101, 34, 58, 49, 55, 48, 51, 54, 54, 49, 53, 56, 52, 56, 57, 52, 44, 34, 114, 101, 113, 117, 101, 115, 116, 34, 58, 123, 34, 104, 101, 97, 100, 101, 114, 115, 34, 58, 123, 34, 104, 111, 115, 116, 34, 58, 34, 49, 50, 55, 46, 48, 46, 48, 46, 49, 58, 57, 48, 56, 48, 34, 44, 34, 97, 99, 99, 101, 112, 116, 34, 58, 34, 42, 47, 42, 34, 44, 34, 117, 115, 101, 114, 45, 97, 103, 101, 110, 116, 34, 58, 34, 99, 117, 114, 108, 47, 55, 46, 56, 49, 46, 48, 34, 125, 44, 34, 113, 117, 101, 114, 121, 115, 116, 114, 105, 110, 103, 34, 58, 123, 125, 44, 34, 115, 105, 122, 101, 34, 58, 56, 54, 44, 34, 117, 114, 105, 34, 58, 34, 47, 97, 110, 121, 116, 104, 105, 110, 103, 34, 44, 34, 117, 114, 108, 34, 58, 34, 104, 116, 116, 112, 58, 47, 47, 49, 50, 55, 46, 48, 46, 48, 46, 49, 58, 57, 48, 56, 48, 47, 97, 110, 121, 116, 104, 105, 110, 103, 34, 44, 34, 109, 101, 116, 104, 111, 100, 34, 58, 34, 71, 69, 84, 34, 125, 44, 34, 114, 111, 117, 116, 101, 95, 105, 100, 34, 58, 34, 114, 111, 99, 107, 101, 116, 109, 113, 45, 108, 111, 103, 103, 101, 114, 45, 114, 111, 117, 116, 101, 34, 44, 34, 97, 112, 105, 115, 105, 120, 95, 108, 97, 116, 101, 110, 99, 121, 34, 58, 56, 46, 57, 57, 57, 56, 52, 53, 53, 48, 52, 55, 54, 48, 55, 44, 34, 117, 112, 115, 116, 114, 101, 97, 109, 95, 108, 97, 116, 101, 110, 99, 121, 34, 58, 53, 48, 51, 44, 34, 108, 97, 116, 101, 110, 99, 121, 34, 58, 53, 49, 49, 46, 57, 57, 57, 56, 52, 53, 53, 48, 52, 55, 54, 44, 34, 114, 101, 115, 112, 111, 110, 115, 101, 34, 58, 123, 34, 115, 105, 122, 101, 34, 58, 51, 51, 50, 44, 34, 104, 101, 97, 100, 101, 114, 115, 34, 58, 123, 34, 99, 111, 110, 116, 101, 110, 116, 45, 108, 101, 110, 103, 116, 104, 34, 58, 34, 49, 54, 50, 34, 44, 34, 99, 111, 110, 110, 101, 99, 116, 105, 111, 110, 34, 58, 34, 99, 108, 111, 115, 101, 34, 44, 34, 100, 97, 116, 101, 34, 58, 34, 87, 101, 100, 44, 32, 50, 55, 32, 68, 101, 99, 32, 50, 48, 50, 51, 32, 48, 55, 58, 49, 57, 58, 52, 53, 32, 71, 77, 84, 34, 44, 34, 115, 101, 114, 118, 101, 114, 34, 58, 34, 65, 80, 73, 83, 73, 88, 47, 51, 46, 55, 46, 48, 34, 44, 34, 99, 111, 110, 116, 101, 110, 116, 45, 116, 121, 112, 101, 34, 58, 34, 116, 101, 120, 116, 47, 104, 116, 109, 108, 59, 32, 99, 104, 97, 114, 115, 101, 116, 61, 117, 116, 102, 45, 56, 34, 125, 44, 34, 115, 116, 97, 116, 117, 115, 34, 58, 52, 48, 52, 125, 44, 34, 115, 101, 114, 118, 101, 114, 34, 58, 123, 34, 104, 111, 115, 116, 110, 97, 109, 101, 34, 58, 34, 117, 98, 117, 110, 116, 117, 45, 108, 105, 110, 117, 120, 45, 50, 50, 45, 48, 52, 45, 48, 50, 45, 100, 101, 115, 107, 116, 111, 112, 34, 44, 34, 118, 101, 114, 115, 105, 111, 110, 34, 58, 34, 51, 46, 55, 46, 48, 34, 125, 44, 34, 115, 101, 114, 118, 105, 99, 101, 95, 105, 100, 34, 58, 34, 34, 125], transactionId='null'}]]
```

You can use JavaScript to translate the body:

```
const data = [123, 34, 99, 108, 105, 101, 110, 116, 95, 105, 112, 34, 58, 34, 49, 50, 55, 46, 48, 46, 48, 46, 49, 34, 44, 34, 117, 112, 115, 116, 114, 101, 97, 109, 34, 58, 34, 49, 57, 56, 46, 49, 56, 46, 49, 46, 57, 50, 58, 56, 48, 34, 44, 34, 115, 116, 97, 114, 116, 95, 116, 105, 109, 101, 34, 58, 49, 55, 48, 51, 54, 54, 49, 53, 56, 52, 56, 57, 52, 44, 34, 114, 101, 113, 117, 101, 115, 116, 34, 58, 123, 34, 104, 101, 97, 100, 101, 114, 115, 34, 58, 123, 34, 104, 111, 115, 116, 34, 58, 34, 49, 50, 55, 46, 48, 46, 48, 46, 49, 58, 57, 48, 56, 48, 34, 44, 34, 97, 99, 99, 101, 112, 116, 34, 58, 34, 42, 47, 42, 34, 44, 34, 117, 115, 101, 114, 45, 97, 103, 101, 110, 116, 34, 58, 34, 99, 117, 114, 108, 47, 55, 46, 56, 49, 46, 48, 34, 125, 44, 34, 113, 117, 101, 114, 121, 115, 116, 114, 105, 110, 103, 34, 58, 123, 125, 44, 34, 115, 105, 122, 101, 34, 58, 56, 54, 44, 34, 117, 114, 105, 34, 58, 34, 47, 97, 110, 121, 116, 104, 105, 110, 103, 34, 44, 34, 117, 114, 108, 34, 58, 34, 104, 116, 116, 112, 58, 47, 47, 49, 50, 55, 46, 48, 46, 48, 46, 49, 58, 57, 48, 56, 48, 47, 97, 110, 121, 116, 104, 105, 110, 103, 34, 44, 34, 109, 101, 116, 104, 111, 100, 34, 58, 34, 71, 69, 84, 34, 125, 44, 34, 114, 111, 117, 116, 101, 95, 105, 100, 34, 58, 34, 114, 111, 99, 107, 101, 116, 109, 113, 45, 108, 111, 103, 103, 101, 114, 45, 114, 111, 117, 116, 101, 34, 44, 34, 97, 112, 105, 115, 105, 120, 95, 108, 97, 116, 101, 110, 99, 121, 34, 58, 56, 46, 57, 57, 57, 56, 52, 53, 53, 48, 52, 55, 54, 48, 55, 44, 34, 117, 112, 115, 116, 114, 101, 97, 109, 95, 108, 97, 116, 101, 110, 99, 121, 34, 58, 53, 48, 51, 44, 34, 108, 97, 116, 101, 110, 99, 121, 34, 58, 53, 49, 49, 46, 57, 57, 57, 56, 52, 53, 53, 48, 52, 55, 54, 44, 34, 114, 101, 115, 112, 111, 110, 115, 101, 34, 58, 123, 34, 115, 105, 122, 101, 34, 58, 51, 51, 50, 44, 34, 104, 101, 97, 100, 101, 114, 115, 34, 58, 123, 34, 99, 111, 110, 116, 101, 110, 116, 45, 108, 101, 110, 103, 116, 104, 34, 58, 34, 49, 54, 50, 34, 44, 34, 99, 111, 110, 110, 101, 99, 116, 105, 111, 110, 34, 58, 34, 99, 108, 111, 115, 101, 34, 44, 34, 100, 97, 116, 101, 34, 58, 34, 87, 101, 100, 44, 32, 50, 55, 32, 68, 101, 99, 32, 50, 48, 50, 51, 32, 48, 55, 58, 49, 57, 58, 52, 53, 32, 71, 77, 84, 34, 44, 34, 115, 101, 114, 118, 101, 114, 34, 58, 34, 65, 80, 73, 83, 73, 88, 47, 51, 46, 55, 46, 48, 34, 44, 34, 99, 111, 110, 116, 101, 110, 116, 45, 116, 121, 112, 101, 34, 58, 34, 116, 101, 120, 116, 47, 104, 116, 109, 108, 59, 32, 99, 104, 97, 114, 115, 101, 116, 61, 117, 116, 102, 45, 56, 34, 125, 44, 34, 115, 116, 97, 116, 117, 115, 34, 58, 52, 48, 52, 125, 44, 34, 115, 101, 114, 118, 101, 114, 34, 58, 123, 34, 104, 111, 115, 116, 110, 97, 109, 101, 34, 58, 34, 117, 98, 117, 110, 116, 117, 45, 108, 105, 110, 117, 120, 45, 50, 50, 45, 48, 52, 45, 48, 50, 45, 100, 101, 115, 107, 116, 111, 112, 34, 44, 34, 118, 101, 114, 115, 105, 111, 110, 34, 58, 34, 51, 46, 55, 46, 48, 34, 125, 44, 34, 115, 101, 114, 118, 105, 99, 101, 95, 105, 100, 34, 58, 34, 34, 125]
const charArray = data.map(code => String.fromCharCode(code))
const resultString = charArray.join('')

console.log(resultString)
```

The result will be:

```
{
  "client_ip": "127.0.0.1",
  "upstream": "198.18.1.92:80",
  "start_time": 1703661584894,
  "request": {
    "headers": {
      "host": "127.0.0.1:9080",
      "accept": "*/*",
      "user-agent": "curl/7.81.0"
    },
    "querystring": {},
    "size": 86,
    "uri": "/anything",
    "url": "http://127.0.0.1:9080/anything",
    "method": "GET"
  },
  "route_id": "rocketmq-logger-route",
  "apisix_latency": 8.9998455047607,
  "upstream_latency": 503,
  "latency": 511.99984550476,
  "response": {
    "size": 332,
    "headers": {
      "content-length": "162",
      "connection": "close",
      "date": "Wed, 27 Dec 2023 07:19:45 GMT",
      "server": "APISIX/3.8.0",
      "content-type": "text/html; charset=utf-8"
    },
    "status": 404
  },
  "server": {
    "hostname": "ubuntu-linux-22-04-02-desktop",
    "version": "3.8.0"
  },
  "service_id": ""
}
```

Update the `rocketmq-logger` meta log format to `origin`:

```
curl "http://127.0.0.1:9180/apisix/admin/routes/rocketmq-logger-route" -X PATCH \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "plugins": {
      "rocketmq-logger": {
        "meta_format": "origin"
      }
    }
  }'
```

Send a request to the route again to generate a new log entry:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should see a log entry in the other terminal running the consumer:

```
ConsumeMessageThread_1 Receive New Messages: [MessageExt [queueId=0, storeSize=857, queueOffset=0, sysFlag=0, bornTimestamp=1703661585406, bornHost=/172.18.0.1:38362, storeTimestamp=1703661585486, storeHost=/172.18.0.3:10911, msgId=AC12000300002A9F0000000000000000, commitLogOffset=0, bodyCRC=1383911373, reconsumeTimes=0, preparedTransactionOffset=0, toString()=Message{topic='TopicTest', flag=0, properties={MIN_OFFSET=0, MAX_OFFSET=1, KEYS=key1, CONSUME_START_TIME=1703661585635, UNIQ_KEY=7F000001A7045E46ABB3892F67FD0002, CLUSTER=DefaultCluster, WAIT=true}, body=[123, 34, 99, 108, 105, 101, 110, 116, 95, 105, 112, 34, 58, 34, 49, 50, 55, 46, 48, 46, 48, 46, 49, 34, 44, 34, 117, 112, 115, 116, 114, 101, 97, 109, 34, 58, 34, 49, 57, 56, 46, 49, 56, 46, 49, 46, 57, 50, 58, 56, 48, 34, 44, 34, 115, 116, 97, 114, 116, 95, 116, 105, 109, 101, 34, 58, 49, 55, 48, 51, 54, 54, 49, 53, 56, 52, 56, 57, 52, 44, 34, 114, 101, 113, 117, 101, 115, 116, 34, 58, 123, 34, 104, 101, 97, 100, 101, 114, 115, 34, 58, 123, 34, 104, 111, 115, 116, 34, 58, 34, 49, 50, 55, 46, 48, 46, 48, 46, 49, 58, 57, 48, 56, 48, 34, 44, 34, 97, 99, 99, 101, 112, 116, 34, 58, 34, 42, 47, 42, 34, 44, 34, 117, 115, 101, 114, 45, 97, 103, 101, 110, 116, 34, 58, 34, 99, 117, 114, 108, 47, 55, 46, 56, 49, 46, 48, 34, 125, 44, 34, 113, 117, 101, 114, 121, 115, 116, 114, 105, 110, 103, 34, 58, 123, 125, 44, 34, 115, 105, 122, 101, 34, 58, 56, 54, 44, 34, 117, 114, 105, 34, 58, 34, 47, 97, 110, 121, 116, 104, 105, 110, 103, 34, 44, 34, 117, 114, 108, 34, 58, 34, 104, 116, 116, 112, 58, 47, 47, 49, 50, 55, 46, 48, 46, 48, 46, 49, 58, 57, 48, 56, 48, 47, 97, 110, 121, 116, 104, 105, 110, 103, 34, 44, 34, 109, 101, 116, 104, 111, 100, 34, 58, 34, 71, 69, 84, 34, 125, 44, 34, 114, 111, 117, 116, 101, 95, 105, 100, 34, 58, 34, 114, 111, 99, 107, 101, 116, 109, 113, 45, 108, 111, 103, 103, 101, 114, 45, 114, 111, 117, 116, 101, 34, 44, 34, 97, 112, 105, 115, 105, 120, 95, 108, 97, 116, 101, 110, 99, 121, 34, 58, 56, 46, 57, 57, 57, 56, 52, 53, 53, 48, 52, 55, 54, 48, 55, 44, 34, 117, 112, 115, 116, 114, 101, 97, 109, 95, 108, 97, 116, 101, 110, 99, 121, 34, 58, 53, 48, 51, 44, 34, 108, 97, 116, 101, 110, 99, 121, 34, 58, 53, 49, 49, 46, 57, 57, 57, 56, 52, 53, 53, 48, 52, 55, 54, 44, 34, 114, 101, 115, 112, 111, 110, 115, 101, 34, 58, 123, 34, 115, 105, 122, 101, 34, 58, 51, 51, 50, 44, 34, 104, 101, 97, 100, 101, 114, 115, 34, 58, 123, 34, 99, 111, 110, 116, 101, 110, 116, 45, 108, 101, 110, 103, 116, 104, 34, 58, 34, 49, 54, 50, 34, 44, 34, 99, 111, 110, 110, 101, 99, 116, 105, 111, 110, 34, 58, 34, 99, 108, 111, 115, 101, 34, 44, 34, 100, 97, 116, 101, 34, 58, 34, 87, 101, 100, 44, 32, 50, 55, 32, 68, 101, 99, 32, 50, 48, 50, 51, 32, 48, 55, 58, 49, 57, 58, 52, 53, 32, 71, 77, 84, 34, 44, 34, 115, 101, 114, 118, 101, 114, 34, 58, 34, 65, 80, 73, 83, 73, 88, 47, 51, 46, 55, 46, 48, 34, 44, 34, 99, 111, 110, 116, 101, 110, 116, 45, 116, 121, 112, 101, 34, 58, 34, 116, 101, 120, 116, 47, 104, 116, 109, 108, 59, 32, 99, 104, 97, 114, 115, 101, 116, 61, 117, 116, 102, 45, 56, 34, 125, 44, 34, 115, 116, 97, 116, 117, 115, 34, 58, 52, 48, 52, 125, 44, 34, 115, 101, 114, 118, 101, 114, 34, 58, 123, 34, 104, 111, 115, 116, 110, 97, 109, 101, 34, 58, 34, 117, 98, 117, 110, 116, 117, 45, 108, 105, 110, 117, 120, 45, 50, 50, 45, 48, 52, 45, 48, 50, 45, 100, 101, 115, 107, 116, 111, 112, 34, 44, 34, 118, 101, 114, 115, 105, 111, 110, 34, 58, 34, 51, 46, 55, 46, 48, 34, 125, 44, 34, 115, 101, 114, 118, 105, 99, 101, 95, 105, 100, 34, 58, 34, 34, 125], transactionId='null'}]]
```

You can use JavaScript to translate the body:

```
const data = [71, 69, 84, 32, 47, 97, 110, 121, 116, 104, 105, 110, 103, 32, 72, 84, 84, 80, 47, 49, 46, 49, 13, 10, 104, 111, 115, 116, 58, 32, 49, 50, 55, 46, 48, 46, 48, 46, 49, 58, 57, 48, 56, 48, 13, 10, 117, 115, 101, 114, 45, 97, 103, 101, 110, 116, 58, 32, 99, 117, 114, 108, 47, 55, 46, 56, 49, 46, 48, 13, 10, 97, 99, 99, 101, 112, 116, 58, 32, 42, 47, 42, 13, 10, 13, 10]
const charArray = data.map(code => String.fromCharCode(code))
const resultString = charArray.join('')

console.log(resultString)
```

The result will be:

```
GET /anything HTTP/1.1
host: 127.0.0.1:9080
user-agent: curl/7.81.0
accept: */*
```

### Log Request and Response Headers With Plugin Metadata[â](#log-request-and-response-headers-with-plugin-metadata "Direct link to Log Request and Response Headers With Plugin Metadata")

The following example demonstrates how you can customize log format using [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) and [built-in variables](https://docs.api7.ai/apisix/reference/built-in-variables.md) to log specific headers from request and response.

In APISIX, [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) is used to configure the common metadata fields of all plugin instances of the same plugin. It is useful when a plugin is enabled across multiple resources and requires a universal update to their metadata fields.

First, create a route with `rocketmq-logger` as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "rocketmq-logger-route",
    "uri": "/anything",
    "plugins": {
      "rocketmq-logger": {
        "nameserver_list": [ "127.0.0.1:9876" ],
        "topic": "TopicTest",
        "key": "key1",
        "timeout": 30,
        "meta_format": "default",
        "batch_max_size": 1
      }
    },
    "upstream": {
      "nodes": {
        "httpbin.org:80": 1
      },
      "type": "roundrobin"
    }
  }'
```

â¶ `meta_format`: set to the `default` log format. It is important to note that this is mandatory if you would like to customize log format with plugin metadata. If `meta_format` is set to `origin`, the log entries will remain in `origin` format.

â· `batch_max_size`: set to 1 to send the log entry immediately.

Next, configure the plugin metadata for `rocketmq-logger`:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/rocketmq-logger" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "log_format": {
      "host": "$host",
      "@timestamp": "$time_iso8601",
      "client_ip": "$remote_addr",
      "env": "$http_env",
      "resp_content_type": "$sent_http_Content_Type"
    }
  }'
```

â¶ log the custom request header `env`.

â· log the response header `Content-Type`.

Send a request to the route with the `env` header:

```
curl -i "http://127.0.0.1:9080/anything" -H "env: dev"
```

You should see a log entry in the other terminal running the consumer:

```
ConsumeMessageThread_1 Receive New Messages: [MessageExt [queueId=0, storeSize=364, queueOffset=3, sysFlag=0, bornTimestamp=1703662284683, bornHost=/172.18.0.1:34628, storeTimestamp=1703662284755, storeHost=/172.18.0.3:10911, msgId=AC12000300002A9F0000000000000577, commitLogOffset=1399, bodyCRC=39663622, reconsumeTimes=0, preparedTransactionOffset=0, toString()=Message{topic='TopicTest', flag=0, properties={MIN_OFFSET=0, MAX_OFFSET=4, KEYS=key1, CONSUME_START_TIME=1703662284829, UNIQ_KEY=7F000001A703880B19C0893A138B0002, CLUSTER=DefaultCluster, WAIT=true}, body=[123, 34, 104, 111, 115, 116, 34, 58, 34, 49, 50, 55, 46, 48, 46, 48, 46, 49, 34, 44, 34, 99, 108, 105, 101, 110, 116, 95, 105, 112, 34, 58, 34, 49, 50, 55, 46, 48, 46, 48, 46, 49, 34, 44, 34, 114, 101, 115, 112, 95, 99, 111, 110, 116, 101, 110, 116, 95, 116, 121, 112, 101, 34, 58, 34, 116, 101, 120, 116, 47, 104, 116, 109, 108, 59, 32, 99, 104, 97, 114, 115, 101, 116, 61, 117, 116, 102, 45, 56, 34, 44, 34, 114, 111, 117, 116, 101, 95, 105, 100, 34, 58, 34, 114, 111, 99, 107, 101, 116, 109, 113, 45, 108, 111, 103, 103, 101, 114, 45, 114, 111, 117, 116, 101, 34, 44, 34, 101, 110, 118, 34, 58, 34, 100, 101, 118, 34, 44, 34, 64, 116, 105, 109, 101, 115, 116, 97, 109, 112, 34, 58, 34, 50, 48, 50, 51, 45, 49, 50, 45, 50, 55, 84, 49, 53, 58, 51, 49, 58, 50, 52, 43, 48, 56, 58, 48, 48, 34, 125], transactionId='null'}]]
```

You can use JavaScript to translate the body:

```
const data = [123, 34, 104, 111, 115, 116, 34, 58, 34, 49, 50, 55, 46, 48, 46, 48, 46, 49, 34, 44, 34, 99, 108, 105, 101, 110, 116, 95, 105, 112, 34, 58, 34, 49, 50, 55, 46, 48, 46, 48, 46, 49, 34, 44, 34, 114, 101, 115, 112, 95, 99, 111, 110, 116, 101, 110, 116, 95, 116, 121, 112, 101, 34, 58, 34, 116, 101, 120, 116, 47, 104, 116, 109, 108, 59, 32, 99, 104, 97, 114, 115, 101, 116, 61, 117, 116, 102, 45, 56, 34, 44, 34, 114, 111, 117, 116, 101, 95, 105, 100, 34, 58, 34, 114, 111, 99, 107, 101, 116, 109, 113, 45, 108, 111, 103, 103, 101, 114, 45, 114, 111, 117, 116, 101, 34, 44, 34, 101, 110, 118, 34, 58, 34, 100, 101, 118, 34, 44, 34, 64, 116, 105, 109, 101, 115, 116, 97, 109, 112, 34, 58, 34, 50, 48, 50, 51, 45, 49, 50, 45, 50, 55, 84, 49, 53, 58, 51, 49, 58, 50, 52, 43, 48, 56, 58, 48, 48, 34, 125]
const charArray = data.map(code => String.fromCharCode(code))
const resultString = charArray.join('')

console.log(resultString)
```

The result will be:

```
{
  "host": "127.0.0.1",
  "client_ip": "127.0.0.1",
  "resp_content_type": "text/html; charset=utf-8",
  "route_id": "rocketmq-logger-route",
  "env": "dev",
  "@timestamp": "2023-12-27T15:31:24+08:00"
}
```

### Log Request Bodies Conditionally[â](#log-request-bodies-conditionally "Direct link to Log Request Bodies Conditionally")

The following example demonstrates how you can conditionally log request body.

Create a route with `rocketmq-logger` as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "plugins": {
      "rocketmq-logger": {
        "nameserver_list": [ "127.0.0.1:9876" ],
        "topic": "TopicTest",
        "key": "key1",
        "timeout": 30,
        "meta_format": "default",
        "batch_max_size": 1,
        "include_req_body": true,
        "include_req_body_expr": [["arg_log_body", "==", "yes"]]
      }
    },
    "upstream": {
      "nodes": {
        "httpbin.org:80": 1
      },
      "type": "roundrobin"
    },
  "uri": "/anything",
  "id": "rocketmq-logger-route"
}'
```

â¶ `include_req_body`: set to true to include request body.

â· `include_req_body_expr`: only include request body if the URL query string `log_body` is `yes`.

Send a request to the route with an URL query string satisfying the condition:

```
curl -i "http://127.0.0.1:9080/anything?log_body=yes" -X POST -d '{"env": "dev"}'
```

You should see a log entry in the other terminal running the consumer:

```
ConsumeMessageThread_1 Receive New Messages: [MessageExt [queueId=0, storeSize=1002, queueOffset=5, sysFlag=0, bornTimestamp=1703662942878, bornHost=/172.18.0.1:36804, storeTimestamp=1703662942946, storeHost=/172.18.0.3:10911, msgId=AC12000300002A9F0000000000000843, commitLogOffset=2115, bodyCRC=441488425, reconsumeTimes=0, preparedTransactionOffset=0, toString()=Message{topic='TopicTest', flag=0, properties={MIN_OFFSET=0, MAX_OFFSET=6, KEYS=key1, CONSUME_START_TIME=1703662942961, UNIQ_KEY=7F000001A702F30B5FB389441E9E0003, CLUSTER=DefaultCluster, WAIT=true}, body=[123, 34, 99, 108, 105, 101, 110, 116, 95, 105, 112, 34, 58, 34, 49, 50, 55, 46, 48, 46, 48, 46, 49, 34, 44, 34, 117, 112, 115, 116, 114, 101, 97, 109, 34, 58, 34, 49, 57, 56, 46, 49, 56, 46, 49, 46, 57, 50, 58, 56, 48, 34, 44, 34, 115, 116, 97, 114, 116, 95, 116, 105, 109, 101, 34, 58, 49, 55, 48, 51, 54, 54, 50, 57, 52, 50, 52, 55, 53, 44, 34, 114, 101, 113, 117, 101, 115, 116, 34, 58, 123, 34, 98, 111, 100, 121, 34, 58, 34, 123, 92, 34, 101, 110, 118, 92, 34, 58, 32, 92, 34, 100, 101, 118, 92, 34, 125, 34, 44, 34, 104, 101, 97, 100, 101, 114, 115, 34, 58, 123, 34, 104, 111, 115, 116, 34, 58, 34, 49, 50, 55, 46, 48, 46, 48, 46, 49, 58, 57, 48, 56, 48, 34, 44, 34, 117, 115, 101, 114, 45, 97, 103, 101, 110, 116, 34, 58, 34, 99, 117, 114, 108, 47, 55, 46, 56, 49, 46, 48, 34, 44, 34, 97, 99, 99, 101, 112, 116, 34, 58, 34, 42, 47, 42, 34, 44, 34, 99, 111, 110, 116, 101, 110, 116, 45, 108, 101, 110, 103, 116, 104, 34, 58, 34, 49, 52, 34, 44, 34, 99, 111, 110, 116, 101, 110, 116, 45, 116, 121, 112, 101, 34, 58, 34, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110, 47, 120, 45, 119, 119, 119, 45, 102, 111, 114, 109, 45, 117, 114, 108, 101, 110, 99, 111, 100, 101, 100, 34, 125, 44, 34, 113, 117, 101, 114, 121, 115, 116, 114, 105, 110, 103, 34, 58, 123, 34, 108, 111, 103, 95, 98, 111, 100, 121, 34, 58, 34, 121, 101, 115, 34, 125, 44, 34, 115, 105, 122, 101, 34, 58, 49, 56, 51, 44, 34, 117, 114, 105, 34, 58, 34, 47, 97, 110, 121, 116, 104, 105, 110, 103, 63, 108, 111, 103, 95, 98, 111, 100, 121, 61, 121, 101, 115, 34, 44, 34, 117, 114, 108, 34, 58, 34, 104, 116, 116, 112, 58, 47, 47, 49, 50, 55, 46, 48, 46, 48, 46, 49, 58, 57, 48, 56, 48, 47, 97, 110, 121, 116, 104, 105, 110, 103, 63, 108, 111, 103, 95, 98, 111, 100, 121, 61, 121, 101, 115, 34, 44, 34, 109, 101, 116, 104, 111, 100, 34, 58, 34, 80, 79, 83, 84, 34, 125, 44, 34, 114, 111, 117, 116, 101, 95, 105, 100, 34, 58, 34, 114, 111, 99, 107, 101, 116, 109, 113, 45, 108, 111, 103, 103, 101, 114, 45, 114, 111, 117, 116, 101, 34, 44, 34, 97, 112, 105, 115, 105, 120, 95, 108, 97, 116, 101, 110, 99, 121, 34, 58, 53, 46, 48, 48, 48, 49, 49, 54, 51, 52, 56, 50, 54, 54, 54, 44, 34, 117, 112, 115, 116, 114, 101, 97, 109, 95, 108, 97, 116, 101, 110, 99, 121, 34, 58, 51, 57, 56, 44, 34, 108, 97, 116, 101, 110, 99, 121, 34, 58, 52, 48, 51, 46, 48, 48, 48, 49, 49, 54, 51, 52, 56, 50, 55, 44, 34, 114, 101, 115, 112, 111, 110, 115, 101, 34, 58, 123, 34, 115, 105, 122, 101, 34, 58, 51, 51, 50, 44, 34, 104, 101, 97, 100, 101, 114, 115, 34, 58, 123, 34, 99, 111, 110, 116, 101, 110, 116, 45, 108, 101, 110, 103, 116, 104, 34, 58, 34, 49, 54, 50, 34, 44, 34, 99, 111, 110, 110, 101, 99, 116, 105, 111, 110, 34, 58, 34, 99, 108, 111, 115, 101, 34, 44, 34, 100, 97, 116, 101, 34, 58, 34, 87, 101, 100, 44, 32, 50, 55, 32, 68, 101, 99, 32, 50, 48, 50, 51, 32, 48, 55, 58, 52, 50, 58, 50, 50, 32, 71, 77, 84, 34, 44, 34, 115, 101, 114, 118, 101, 114, 34, 58, 34, 65, 80, 73, 83, 73, 88, 47, 51, 46, 55, 46, 48, 34, 44, 34, 99, 111, 110, 116, 101, 110, 116, 45, 116, 121, 112, 101, 34, 58, 34, 116, 101, 120, 116, 47, 104, 116, 109, 108, 59, 32, 99, 104, 97, 114, 115, 101, 116, 61, 117, 116, 102, 45, 56, 34, 125, 44, 34, 115, 116, 97, 116, 117, 115, 34, 58, 52, 48, 52, 125, 44, 34, 115, 101, 114, 118, 101, 114, 34, 58, 123, 34, 104, 111, 115, 116, 110, 97, 109, 101, 34, 58, 34, 117, 98, 117, 110, 116, 117, 45, 108, 105, 110, 117, 120, 45, 50, 50, 45, 48, 52, 45, 48, 50, 45, 100, 101, 115, 107, 116, 111, 112, 34, 44, 34, 118, 101, 114, 115, 105, 111, 110, 34, 58, 34, 51, 46, 55, 46, 48, 34, 125, 44, 34, 115, 101, 114, 118, 105, 99, 101, 95, 105, 100, 34, 58, 34, 34, 125], transactionId='null'}]]
```

You can use JavaScript to translate the body:

```
const data = [123, 34, 99, 108, 105, 101, 110, 116, 95, 105, 112, 34, 58, 34, 49, 50, 55, 46, 48, 46, 48, 46, 49, 34, 44, 34, 117, 112, 115, 116, 114, 101, 97, 109, 34, 58, 34, 49, 57, 56, 46, 49, 56, 46, 49, 46, 57, 50, 58, 56, 48, 34, 44, 34, 115, 116, 97, 114, 116, 95, 116, 105, 109, 101, 34, 58, 49, 55, 48, 51, 54, 54, 50, 57, 52, 50, 52, 55, 53, 44, 34, 114, 101, 113, 117, 101, 115, 116, 34, 58, 123, 34, 98, 111, 100, 121, 34, 58, 34, 123, 92, 34, 101, 110, 118, 92, 34, 58, 32, 92, 34, 100, 101, 118, 92, 34, 125, 34, 44, 34, 104, 101, 97, 100, 101, 114, 115, 34, 58, 123, 34, 104, 111, 115, 116, 34, 58, 34, 49, 50, 55, 46, 48, 46, 48, 46, 49, 58, 57, 48, 56, 48, 34, 44, 34, 117, 115, 101, 114, 45, 97, 103, 101, 110, 116, 34, 58, 34, 99, 117, 114, 108, 47, 55, 46, 56, 49, 46, 48, 34, 44, 34, 97, 99, 99, 101, 112, 116, 34, 58, 34, 42, 47, 42, 34, 44, 34, 99, 111, 110, 116, 101, 110, 116, 45, 108, 101, 110, 103, 116, 104, 34, 58, 34, 49, 52, 34, 44, 34, 99, 111, 110, 116, 101, 110, 116, 45, 116, 121, 112, 101, 34, 58, 34, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110, 47, 120, 45, 119, 119, 119, 45, 102, 111, 114, 109, 45, 117, 114, 108, 101, 110, 99, 111, 100, 101, 100, 34, 125, 44, 34, 113, 117, 101, 114, 121, 115, 116, 114, 105, 110, 103, 34, 58, 123, 34, 108, 111, 103, 95, 98, 111, 100, 121, 34, 58, 34, 121, 101, 115, 34, 125, 44, 34, 115, 105, 122, 101, 34, 58, 49, 56, 51, 44, 34, 117, 114, 105, 34, 58, 34, 47, 97, 110, 121, 116, 104, 105, 110, 103, 63, 108, 111, 103, 95, 98, 111, 100, 121, 61, 121, 101, 115, 34, 44, 34, 117, 114, 108, 34, 58, 34, 104, 116, 116, 112, 58, 47, 47, 49, 50, 55, 46, 48, 46, 48, 46, 49, 58, 57, 48, 56, 48, 47, 97, 110, 121, 116, 104, 105, 110, 103, 63, 108, 111, 103, 95, 98, 111, 100, 121, 61, 121, 101, 115, 34, 44, 34, 109, 101, 116, 104, 111, 100, 34, 58, 34, 80, 79, 83, 84, 34, 125, 44, 34, 114, 111, 117, 116, 101, 95, 105, 100, 34, 58, 34, 114, 111, 99, 107, 101, 116, 109, 113, 45, 108, 111, 103, 103, 101, 114, 45, 114, 111, 117, 116, 101, 34, 44, 34, 97, 112, 105, 115, 105, 120, 95, 108, 97, 116, 101, 110, 99, 121, 34, 58, 53, 46, 48, 48, 48, 49, 49, 54, 51, 52, 56, 50, 54, 54, 54, 44, 34, 117, 112, 115, 116, 114, 101, 97, 109, 95, 108, 97, 116, 101, 110, 99, 121, 34, 58, 51, 57, 56, 44, 34, 108, 97, 116, 101, 110, 99, 121, 34, 58, 52, 48, 51, 46, 48, 48, 48, 49, 49, 54, 51, 52, 56, 50, 55, 44, 34, 114, 101, 115, 112, 111, 110, 115, 101, 34, 58, 123, 34, 115, 105, 122, 101, 34, 58, 51, 51, 50, 44, 34, 104, 101, 97, 100, 101, 114, 115, 34, 58, 123, 34, 99, 111, 110, 116, 101, 110, 116, 45, 108, 101, 110, 103, 116, 104, 34, 58, 34, 49, 54, 50, 34, 44, 34, 99, 111, 110, 110, 101, 99, 116, 105, 111, 110, 34, 58, 34, 99, 108, 111, 115, 101, 34, 44, 34, 100, 97, 116, 101, 34, 58, 34, 87, 101, 100, 44, 32, 50, 55, 32, 68, 101, 99, 32, 50, 48, 50, 51, 32, 48, 55, 58, 52, 50, 58, 50, 50, 32, 71, 77, 84, 34, 44, 34, 115, 101, 114, 118, 101, 114, 34, 58, 34, 65, 80, 73, 83, 73, 88, 47, 51, 46, 55, 46, 48, 34, 44, 34, 99, 111, 110, 116, 101, 110, 116, 45, 116, 121, 112, 101, 34, 58, 34, 116, 101, 120, 116, 47, 104, 116, 109, 108, 59, 32, 99, 104, 97, 114, 115, 101, 116, 61, 117, 116, 102, 45, 56, 34, 125, 44, 34, 115, 116, 97, 116, 117, 115, 34, 58, 52, 48, 52, 125, 44, 34, 115, 101, 114, 118, 101, 114, 34, 58, 123, 34, 104, 111, 115, 116, 110, 97, 109, 101, 34, 58, 34, 117, 98, 117, 110, 116, 117, 45, 108, 105, 110, 117, 120, 45, 50, 50, 45, 48, 52, 45, 48, 50, 45, 100, 101, 115, 107, 116, 111, 112, 34, 44, 34, 118, 101, 114, 115, 105, 111, 110, 34, 58, 34, 51, 46, 55, 46, 48, 34, 125, 44, 34, 115, 101, 114, 118, 105, 99, 101, 95, 105, 100, 34, 58, 34, 34, 125]
const charArray = data.map(code => String.fromCharCode(code))
const resultString = charArray.join('')

console.log(resultString)
```

The result will be:

```
{
  ...,
    "method": "POST",
    "body": "{\"env\": \"dev\"}",
    "size": 183
  }
}
```

Send a request to the route without any URL query string:

```
curl -i "http://127.0.0.1:9080/anything" -X POST -d '{"env": "dev"}'
```

You should not observe the request body in the log.

info

If you have customized the `log_format` in addition to setting `include_req_body` or `include_resp_body` to `true`, the plugin would not include the bodies in the logs.

As a workaround, you may be able to use the NGINX variable `$request_body` in the log format, such as:

```
{
  "rocketmq-logger": {
    ...,
    "log_format": {"body": "$request_body"}
  }
}
```
