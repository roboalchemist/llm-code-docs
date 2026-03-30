# optuna.storages.GrpcStorageProxy

class optuna.storages.GrpcStorageProxy(***, *host='localhost'*, *port=13000*)

gRPC client for `run_grpc_proxy_server()`.

Example

This is a simple example of using `GrpcStorageProxy` with
`run_grpc_proxy_server()`.

```
import optuna
from optuna.storages import GrpcStorageProxy

storage = GrpcStorageProxy(host="localhost", port=13000)
study = optuna.create_study(storage=storage)

```