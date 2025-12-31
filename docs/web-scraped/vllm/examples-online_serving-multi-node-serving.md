# Source: https://docs.vllm.ai/en/stable/examples/online_serving/multi-node-serving/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/multi-node-serving.md "Edit this page")

# Multi-Node-Serving[¶](#multi-node-serving "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/multi-node-serving.sh>.

    #!/bin/bash
    #
    # Helper script to manually start or join a Ray cluster for online serving of vLLM models.
    # This script is first executed on the head node, and then on each worker node with the IP address
    # of the head node.
    #
    # Subcommands:
    #   leader: Launches a Ray head node and blocks until the cluster reaches the expected size (head + workers).
    #   worker: Starts a worker node that connects to an existing Ray head node.
    #
    # Example usage:
    # On the head node machine, start the Ray head node process and run a vLLM server.
    #   ./multi-node-serving.sh leader --ray_port=6379 --ray_cluster_size=<SIZE> [<extra ray args>]  && \
    #   vllm serve meta-llama/Meta-Llama-3.1-405B-Instruct --port 8080 --tensor-parallel-size 8 --pipeline_parallel_size 2
    # 
    # On each worker node, start the Ray worker node process.
    #   ./multi-node-serving.sh worker --ray_address=<HEAD_NODE_IP> --ray_port=6379 [<extra ray args>]
    #
    # About Ray:
    # Ray is an open-source distributed execution framework that simplifies
    # distributed computing. Learn more:
    # https://ray.io/

    subcommand=$1  # Either "leader" or "worker".
    shift          # Remove the subcommand from the argument list.

    ray_port=6379              # Port used by the Ray head node.
    ray_init_timeout=300       # Seconds to wait before timing out.
    declare -a start_params    # Parameters forwarded to the underlying 'ray start' command.

    # Handle the worker subcommand.
    case "$subcommand" in
      worker)
        ray_address=""
        while [ $# -gt 0 ]; do
          case "$1" in
            --ray_address=*)
              ray_address="$"
              ;;
            --ray_port=*)
              ray_port="$"
              ;;
            --ray_init_timeout=*)
              ray_init_timeout="$"
              ;;
            *)
              start_params+=("$1")
          esac
          shift
        done

        if [ -z "$ray_address" ]; then
          echo "Error: Missing argument --ray_address"
          exit 1
        fi

        # Retry until the worker node connects to the head node or the timeout expires.
        for (( i=0; i < $ray_init_timeout; i+=5 )); do
          ray start --address=$ray_address:$ray_port --block "$"
          if [ $? -eq 0 ]; then
            echo "Worker: Ray runtime started with head address $ray_address:$ray_port"
            exit 0
          fi
          echo "Waiting until the ray worker is active..."
          sleep 5s;
        done
        echo "Ray worker starts timeout, head address: $ray_address:$ray_port"
        exit 1
        ;;

      # Handle the leader subcommand.
      leader)
        ray_cluster_size=""
        while [ $# -gt 0 ]; do
              case "$1" in
                --ray_port=*)
                  ray_port="$"
                  ;;
                --ray_cluster_size=*)
                  ray_cluster_size="$"
                  ;;
                --ray_init_timeout=*)
                  ray_init_timeout="$"
                  ;;
                *)
                  start_params+=("$1")
              esac
              shift
        done

        if [ -z "$ray_cluster_size" ]; then
          echo "Error: Missing argument --ray_cluster_size"
          exit 1
        fi

        # Start the Ray head node.
        ray start --head --port=$ray_port "$"

        # Poll Ray until every worker node is active.
        for (( i=0; i < $ray_init_timeout; i+=5 )); do
            active_nodes=`python3 -c 'import ray; ray.init(); print(sum(node["Alive"] for node in ray.nodes()))'`
            if [ $active_nodes -eq $ray_cluster_size ]; then
              echo "All ray workers are active and the ray cluster is initialized successfully."
              exit 0
            fi
            echo "Wait for all ray workers to be active. $active_nodes/$ray_cluster_size is active"
            sleep 5s;
        done

        echo "Waiting for all ray workers to be active timed out."
        exit 1
        ;;

      *)
        echo "unknown subcommand: $subcommand"
        exit 1
        ;;
    esac