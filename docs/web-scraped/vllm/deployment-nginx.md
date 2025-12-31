# Source: https://docs.vllm.ai/en/stable/deployment/nginx/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/deployment/nginx.md "Edit this page")

# Using Nginx[¶](#using-nginx "Permanent link")

This document shows how to launch multiple vLLM serving containers and use Nginx to act as a load balancer between the servers.

## Build Nginx Container[¶](#build-nginx-container "Permanent link")

This guide assumes that you have just cloned the vLLM project and you\'re currently in the vllm root directory.

    export vllm_root=`pwd`

Create a file named `Dockerfile.nginx`:

    FROM nginx:latest
    RUN rm /etc/nginx/conf.d/default.conf
    EXPOSE 80
    CMD ["nginx", "-g", "daemon off;"]

Build the container:

    docker build . -f Dockerfile.nginx --tag nginx-lb

## Create Simple Nginx Config file[¶](#create-simple-nginx-config-file "Permanent link")

Create a file named `nginx_conf/nginx.conf`. Note that you can add as many servers as you\'d like. In the below example we\'ll start with two. To add more, add another `server vllmN:8000 max_fails=3 fail_timeout=10000s;` entry to `upstream backend`.

Config

    upstream backend 
    server 
    }

## Build vLLM Container[¶](#build-vllm-container "Permanent link")

    cd $vllm_root
    docker build -f docker/Dockerfile . --tag vllm

If you are behind proxy, you can pass the proxy settings to the docker build command as shown below:

    cd $vllm_root
    docker build \
        -f docker/Dockerfile . \
        --tag vllm \
        --build-arg http_proxy=$http_proxy \
        --build-arg https_proxy=$https_proxy

## Create Docker Network[¶](#create-docker-network "Permanent link")

    docker network create vllm_nginx

## Launch vLLM Containers[¶](#launch-vllm-containers "Permanent link")

Notes:

-   If you have your HuggingFace models cached somewhere else, update `hf_cache_dir` below.
-   If you don\'t have an existing HuggingFace cache you will want to start `vllm0` and wait for the model to complete downloading and the server to be ready. This will ensure that `vllm1` can leverage the model you just downloaded and it won\'t have to be downloaded again.
-   The below example assumes GPU backend used. If you are using CPU backend, remove `--gpus device=ID`, add `VLLM_CPU_KVCACHE_SPACE` and `VLLM_CPU_OMP_THREADS_BIND` environment variables to the docker run command.
-   Adjust the model name that you want to use in your vLLM servers if you don\'t want to use `Llama-2-7b-chat-hf`.

Commands

    mkdir -p ~/.cache/huggingface/hub/
    hf_cache_dir=~/.cache/huggingface/
    docker run \
        -itd \
        --ipc host \
        --network vllm_nginx \
        --gpus device=0 \
        --shm-size=10.24gb \
        -v $hf_cache_dir:/root/.cache/huggingface/ \
        -p 8081:8000 \
        --name vllm0 vllm \
        --model meta-llama/Llama-2-7b-chat-hf
    docker run \
        -itd \
        --ipc host \
        --network vllm_nginx \
        --gpus device=1 \
        --shm-size=10.24gb \
        -v $hf_cache_dir:/root/.cache/huggingface/ \
        -p 8082:8000 \
        --name vllm1 vllm \
        --model meta-llama/Llama-2-7b-chat-hf

Note

If you are behind proxy, you can pass the proxy settings to the docker run command via `-e http_proxy=$http_proxy -e https_proxy=$https_proxy`.

## Launch Nginx[¶](#launch-nginx "Permanent link")

    docker run \
        -itd \
        -p 8000:80 \
        --network vllm_nginx \
        -v ./nginx_conf/:/etc/nginx/conf.d/ \
        --name nginx-lb nginx-lb:latest

## Verify That vLLM Servers Are Ready[¶](#verify-that-vllm-servers-are-ready "Permanent link")

    docker logs vllm0 | grep Uvicorn
    docker logs vllm1 | grep Uvicorn

Both outputs should look like this:

    INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 17, 2025] ]