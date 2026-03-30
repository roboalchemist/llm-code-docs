# optuna.storages.run_grpc_proxy_server

optuna.storages.run_grpc_proxy_server(*storage*, ***, *host='localhost'*, *port=13000*, *thread_pool=None*)

Run a gRPC server for the given storage URL, host, and port.

Example

Run this server with the following way:

```
from optuna.storages import run_grpc_proxy_server
from optuna.storages import get_storage

storage = get_storage("mysql+pymysql://<user>:<pass>@<host>/<dbname>[?<options>]")
run_grpc_proxy_server(storage, host="localhost", port=13000)

```