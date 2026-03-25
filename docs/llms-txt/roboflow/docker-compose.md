# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/enterprise-deployment/docker-compose.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/enterprise-deployment/docker-compose.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/enterprise-deployment/docker-compose.md

# Source: https://docs.roboflow.com/deploy/enterprise-deployment/docker-compose.md

# Docker Compose

If you want to run other docker containers alongside the Roboflow inference container you can do so using [Docker Compose](https://docs.docker.com/compose/). We illustrate this via an example docker-compose.yaml file:

```yaml
# Run the roboflow Inference Service as a Docker compose service"
services:
  roboflow-inference-service:
    image: roboflow/inference-server:cpu
    ports:
      - "9001:9001"

# Optionally, add any other containers or services you need here, 
# illustrated via this example below;
# so you can "compose" multiple services with the roboflow inference 
# service  as needed by your application

  another-container-service:
    image:  curlimages/curl:8.00.1
    entrypoint:
      - /bin/ash
      - -c
      - |
        while true; do 
        curl -s -X GET http://roboflow-inference-service:9001 
        sleep 5; 
        done
      
    depends_on:
      - roboflow-inference-service
  
```

After saving the file, type `docker-compose up` in your terminal. Two docker containers will spin up - the roboflow inference server and another container that `curls` the inference server every 5 seconds.

You can extend this example to add more containers to compose your stack as needed by your application.
