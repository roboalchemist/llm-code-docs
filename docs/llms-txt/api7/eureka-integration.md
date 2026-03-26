# Source: https://docs.api7.ai/apisix/how-to-guide/service-discovery/eureka-integration.md

# Integrate with Netflix Eureka

[Netflix Eureka](https://github.com/Netflix/eureka) is an open-source registry service written in Java by Netflix, and it is essential to Netflix's infrastructure. Netflix Eureka provides a lightweight and reliable solution for [service discovery](https://docs.api7.ai/apisix/key-concepts/upstreams.md#service-discovery). It utilizes a client-server model where microservices register themselves with the server and other services can dynamically locate them through service resolutions.

This guide will walk you through the process of setting up Netflix Eureka for service discovery, and demonstrate how to integrate it with APISIX to dynamically route and load balance traffic across your microservices.

note

If you are running APISIX and the Ingress Controller in Kubernetes, this guide simulates a hybrid environment where APISIX routes traffic to services outside the cluster through an external Eureka registry.

In a setup where all services already run inside Kubernetes, you typically do not need Eureka, as Kubernetes provides its own built-in service discovery through the Kubernetes Service registry and DNS.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started Tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Start Eureka Instance[â](#start-eureka-instance "Direct link to Start Eureka Instance")

Start a Eureka Docker instance named `eureka` in the same network as the APISIX instance and expose port `8761` to the same port on the host machine:

```
docker run \
  --name eureka \
  -d -p 8761:8761 \
  --network=apisix-quickstart-net \
  -e ENVIRONMENT=apisix \
  -e spring.application.name=apisix-eureka \
  -e server.port=8761 \
  -e eureka.instance.ip-address=127.0.0.1 \
  -e eureka.client.registerWithEureka=true \
  -e eureka.client.fetchRegistry=false \
  -e eureka.client.serviceUrl.defaultZone=http://127.0.0.1:8761/eureka/ \
  bitinit/eureka
```

## Start Sample Web Services[â](#start-sample-web-services "Direct link to Start Sample Web Services")

In this section, you will start two sample web services based on NGINX.

Create two configuration files, `web1.conf` and `web2.conf`, which instruct NGINX to serve static text responses at root:

```
echo 'worker_processes 1;
error_log stderr notice;
events {
    worker_connections 1024;
}

http {
    variables_hash_max_size 1024;
    access_log off;
    real_ip_header X-Real-IP;
    charset utf-8;

    server {
        listen 80;

        location / {
            return 200 "Application 1 is running";
        }

        location /static/ {
            alias static/;
        }
    }
}' > web1.conf
```

```
echo 'worker_processes 1;
error_log stderr notice;
events {
    worker_connections 1024;
}

http {
    variables_hash_max_size 1024;
    access_log off;
    real_ip_header X-Real-IP;
    charset utf-8;

    server {
        listen 80;

        location / {
            return 200 "Application 2 is running";
        }

        location /static/ {
            alias static/;
        }
    }
}' > web2.conf
```

Start the web services `web1` and `web2`:

```
docker run -d \
  --name web1 \
  --restart always \
  -v $(pwd)/web1.conf:/etc/nginx/nginx.conf \
  -p 9081:80 \
  --network=apisix-quickstart-net \
  nginx:1.25-alpine
```

```
docker run -d \
  --name web2 \
  --restart always \
  -v $(pwd)/web2.conf:/etc/nginx/nginx.conf \
  -p 9082:80 \
  --network=apisix-quickstart-net \
  nginx:1.25-alpine
```

â¶ Mount `web1.conf` and `web2.conf` from the host machine to `/etc/nginx/nginx.conf` inside the containers.

â· Map port `80` of the containers to port `9081` and `9082` on the host.

## Register Services in Eureka[â](#register-services-in-eureka "Direct link to Register Services in Eureka")

Save the IP address of your host to an environment variable:

```
HOST_IP=192.168.31.89   # replace with your host IP
```

Register two services in Eureka:

```
curl "http://127.0.0.1:8761/eureka/apps/web" -X POST \
  -H "Content-Type: application/json" \
  -d '{
"instance":{
  "instanceId": "'"$HOST_IP"':9081",
  "hostName": "'"$HOST_IP"'",
  "ipAddr": "'"$HOST_IP"'",
  "port":{
    "$":9081,
    "@enabled":true
    },
  "status": "UP",
  "app": "web",
  "dataCenterInfo": {
    "name": "MyOwn",
    "@class":"com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo"
    }
  }
}'
```

```
curl "http://127.0.0.1:8761/eureka/apps/web" -X POST \
  -H "Content-Type: application/json" \
  -d '{
"instance":{
  "instanceId": "'"$HOST_IP"':9082",
  "hostName": "'"$HOST_IP"'",
  "ipAddr": "'"$HOST_IP"'",
  "port":{
    "$":9082,
    "@enabled":true
    },
  "status": "UP",
  "app": "web",
  "dataCenterInfo": {
    "name": "MyOwn",
    "@class":"com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo"
    }
  }
}'
```

Verify if the services are registered successfully:

```
curl "http://127.0.0.1:8761/eureka/apps/web"
```

You should see an XML response including information of your services.

## Connect Eureka to APISIX[â](#connect-eureka-to-apisix "Direct link to Connect Eureka to APISIX")

Add Eureka discovery configurations to APISIX's `config.yaml` [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample):

```
docker exec apisix-quickstart /bin/sh -c "echo '
discovery:
  eureka:
    host:
      - "http://eureka:8761"
    prefix: /eureka/
    fetch_interval: 30
    weight: 100
    timeout:
      connect: 2000
      send: 2000
      read: 5000
' >> /usr/local/apisix/conf/config.yaml"
```

â¶ `host`: address of the Eureka server.

â· `prefix`: the base API path used by the Eureka server for service registration and discovery requests.

Reload APISIX for configuration changes to take effect:

```
docker exec apisix-quickstart apisix reload
```

## Create a Route in APISIX[â](#create-a-route-in-apisix "Direct link to Create a Route in APISIX")

Create a route and configure the upstream to use Eureka for service discovery of `WEB`:

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "eureka-web-route",
  "uri": "/eureka/web/*",
  "upstream": {
    "service_name": "WEB",
    "discovery_type": "eureka",
    "type": "roundrobin"
  }
}'
```

An `HTTP/1.1 200 OK` response verifies that the route is created successfully.

adc.yaml

```
services:
  - name: Eureka Service
    routes:
      - uris:
        - /eureka/web/*
        name: eureka-web-route
    upstream:
      service_name: WEB
      discovery_type: eureka
      type: roundrobin
```

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

## Validate[â](#validate "Direct link to Validate")

Generate a few requests to the previously created route:

```
curl "http://127.0.0.1:9080/eureka/web/"
```

You should see the responses alternating between the following:

```
Application 1 is running%
```

```
Application 2 is running%
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

In addition to Eureka, APISIX also supports the integration with [HashiCorp Consul](https://docs.api7.ai/apisix/how-to-guide/service-discovery/consul-integration.md), Nacos, and other service discovery platforms (coming soon).
