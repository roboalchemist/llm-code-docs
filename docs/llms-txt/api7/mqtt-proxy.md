# Source: https://docs.api7.ai/hub/mqtt-proxy.md

# mqtt-proxy

The `mqtt-proxy` plugin is an L4 plugin that supports proxying and load balancing MQTT requests to MQTT servers. It supports MQTT versions 3.1.x and 5.0. The plugin must be configured on a [stream route](https://docs.api7.ai/apisix/key-concepts/stream-routes.md), and APISIX should enable L4 traffic proxying.

## Examples[â](#examples "Direct link to Examples")

By default, APISIX only proxies L7 traffic. Before proceeding to examples, first ensure that you enable L4 traffic proxying in APISIX.

Update the [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample) as follows to enable L4 traffic proxying:

conf/config.yaml

```
apisix:
  proxy_mode: http&stream   # Enable both L4 & L7 proxies
  stream_proxy:             # Configure L4 proxy
    tcp:
      - 9100                # Set TCP proxy listening port
```

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for changes to take effect. APISIX should now start listening L4 traffic on port `9100`.

The examples below uses a MQTT client from the Mosquitto project to publish and subscribe messages. You can download it [here](https://mosquitto.org/download/) or use any other MQTT client of your choice.

### Proxy to a MQTT Broker[â](#proxy-to-a-mqtt-broker "Direct link to Proxy to a MQTT Broker")

The following example demonstrates how you can configure a stream route to proxy traffic to a hosted MQTT server and verify the APISIX can proxy MQTT messages successfully.

Create a stream route to the MQTT server and configure the `mqtt-proxy` plugin:

```
curl "http://127.0.0.1:9180/apisix/admin/stream_routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "mqtt-route",
    "plugins": {
      "mqtt-proxy": {
        "protocol_name": "MQTT",
        "protocol_level": 4
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "test.mosquitto.org:1883": 1
      }
    }
  }'
```

Open two terminal sessions. In the first one, subscribe to the test topic:

```
mosquitto_sub -h test.mosquitto.org -p 1883 -t "test/apisix"
```

In the other one, publish a sample message to the created route:

```
mosquitto_pub -h 127.0.0.1 -p 9100 -t "test/apisix" -m "Hello APISIX"
```

You should see the message `Hello APISIX` in the first terminal.

### Load Balance MQTT Traffic[â](#load-balance-mqtt-traffic "Direct link to Load Balance MQTT Traffic")

The following example demonstrates how you can configure a stream route to load balance MQTT traffic to different MQTT servers.

When the plugin is enabled, it registers a variable `mqtt_client_id` which can be used for load balancing. MQTT connections with different client ID will be forwarded to different upstream nodes based on the consistent hash algorithm. If the client ID is missing, client IP will be used instead.

Create a stream route to two MQTT servers and configure the `mqtt-proxy` plugin:

```
curl "http://127.0.0.1:9180/apisix/admin/stream_routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "mqtt-route",
    "plugins": {
      "mqtt-proxy": {
        "protocol_name": "MQTT",
        "protocol_level": 4
      }
    },
    "upstream": {
      "type": "roundrobin",
      "key": "mqtt_client_id",
      "nodes": [
        {
          "host": "test.mosquitto.org",
          "port": 1883,
          "weight": 1
        },
        {
          "host": "broker.mqtt.cool",
          "port": 1883,
          "weight": 1
        }
      ]
    }
  }'
```

Open three terminal sessions. In the first one, subscribe to the test topic in the first MQTT broker:

```
mosquitto_sub -h test.mosquitto.org -p 1883 -t "test/apisix"
```

In the second terminal, subscribe to the same topic in the second MQTT broker:

```
mosquitto_sub -h broker.mqtt.cool -p 1883 -t "test/apisix"
```

In the third terminal, run the following commands a few times to send sample messages to the route:

```
mosquitto_pub -h 127.0.0.1 -p 9100 -t "test/apisix" -m "Hello APISIX"
```

You should see the message `Hello APISIX` in both terminals, verifying the traffic was load balanced.
