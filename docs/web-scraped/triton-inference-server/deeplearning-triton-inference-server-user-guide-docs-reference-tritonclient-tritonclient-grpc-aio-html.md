# Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html

Title: tritonclient.grpc.aio — NVIDIA Triton Inference Server

URL Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html

Markdown Content:
Classes

_class_ tritonclient.grpc.aio.InferenceServerClient(_url_,_verbose=False_,_ssl=False_,_root\_certificates=None_,_private\_key=None_,_certificate\_chain=None_,_creds=None_,_keepalive\_options=None_,_channel\_args=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient "Link to this definition")
This feature is currently in beta and may be subject to change.

An analogy of the [`tritonclient.grpc.InferenceServerClient`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient "tritonclient.grpc.InferenceServerClient") to enable calling via asyncio syntax. The object is intended to be used by a single thread and simultaneously calling methods with different threads is not supported and can cause undefined behavior.

_get_metadata(_headers_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient._get_metadata "Link to this definition")_return_response(_response_, _as\_json_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient._return_response "Link to this definition")_async_ close()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.close "Link to this definition")
Close the client. Any future calls to server will result in an Error.

_async_ get_cuda_shared_memory_status(_region\_name=''_,_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.get_cuda_shared_memory_status "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.get_cuda_shared_memory_status()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_cuda_shared_memory_status "tritonclient.grpc.InferenceServerClient.get_cuda_shared_memory_status")

_async_ get_inference_statistics(_model\_name=''_,_model\_version=''_,_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.get_inference_statistics "Link to this definition")
Refer to :[`tritonclient.grpc.InferenceServerClient.get_inference_statistics()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_inference_statistics "tritonclient.grpc.InferenceServerClient.get_inference_statistics")

_async_ get_log_settings(_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.get_log_settings "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.get_log_settings()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_log_settings "tritonclient.grpc.InferenceServerClient.get_log_settings")

_async_ get_model_config(_model\_name_,_model\_version=''_,_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.get_model_config "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.get_model_config()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_model_config "tritonclient.grpc.InferenceServerClient.get_model_config")

_async_ get_model_metadata(_model\_name_,_model\_version=''_,_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.get_model_metadata "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.get_model_metadata()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_model_metadata "tritonclient.grpc.InferenceServerClient.get_model_metadata")

_async_ get_model_repository_index(_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.get_model_repository_index "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.get_model_repository_index()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_model_repository_index "tritonclient.grpc.InferenceServerClient.get_model_repository_index")

_async_ get_server_metadata(_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.get_server_metadata "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.get_server_metadata()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_server_metadata "tritonclient.grpc.InferenceServerClient.get_server_metadata")

_async_ get_system_shared_memory_status(_region\_name=''_,_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.get_system_shared_memory_status "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.get_system_shared_memory_status()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_system_shared_memory_status "tritonclient.grpc.InferenceServerClient.get_system_shared_memory_status")

_async_ get_trace_settings(_model\_name=None_,_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.get_trace_settings "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.get_trace_settings()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_trace_settings "tritonclient.grpc.InferenceServerClient.get_trace_settings")

_async_ infer(_model\_name_,_inputs_,_model\_version=''_,_outputs=None_,_request\_id=''_,_sequence\_id=0_,_sequence\_start=False_,_sequence\_end=False_,_priority=0_,_timeout=None_,_client\_timeout=None_,_headers=None_,_compression\_algorithm=None_,_parameters=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.infer "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.infer()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.infer "tritonclient.grpc.InferenceServerClient.infer")

_async_ is_model_ready(_model\_name_,_model\_version=''_,_headers=None_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.is_model_ready "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.is_model_ready()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.is_model_ready "tritonclient.grpc.InferenceServerClient.is_model_ready")

_async_ is_server_live(_headers=None_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.is_server_live "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.is_server_live()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.is_server_live "tritonclient.grpc.InferenceServerClient.is_server_live")

_async_ is_server_ready(_headers=None_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.is_server_ready "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.is_server_ready()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.is_server_ready "tritonclient.grpc.InferenceServerClient.is_server_ready")

_async_ load_model(_model\_name_,_headers=None_,_config=None_,_files=None_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.load_model "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.load_model()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.load_model "tritonclient.grpc.InferenceServerClient.load_model")

_async_ register_cuda_shared_memory(_name_,_raw\_handle_,_device\_id_,_byte\_size_,_headers=None_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.register_cuda_shared_memory "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.register_cuda_shared_memory()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.register_cuda_shared_memory "tritonclient.grpc.InferenceServerClient.register_cuda_shared_memory")

_async_ register_system_shared_memory(_name_,_key_,_byte\_size_,_offset=0_,_headers=None_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.register_system_shared_memory "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.register_system_shared_memory()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.register_system_shared_memory "tritonclient.grpc.InferenceServerClient.register_system_shared_memory")

stream_infer(_inputs\_iterator_,_stream\_timeout=None_,_headers=None_,_compression\_algorithm=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.stream_infer "Link to this definition")
Runs an asynchronous inference over gRPC bi-directional streaming API.

Parameters:
*   **inputs_iterator** (_asynchronous iterator_) – Async iterator that yields a dict(s) consists of the input parameters to the [`tritonclient.grpc.InferenceServerClient.async_stream_infer()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.async_stream_infer "tritonclient.grpc.InferenceServerClient.async_stream_infer") function defined in [`tritonclient.grpc.InferenceServerClient`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient "tritonclient.grpc.InferenceServerClient").

*   **stream_timeout** (_float_) – Optional stream timeout. The stream will be closed once the specified timeout expires.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **compression_algorithm** (_str_) – Optional grpc compression algorithm to be used on client side. Currently supports “deflate”, “gzip” and None. By default, no compression is used.

Returns:
Yield tuple holding ([`tritonclient.grpc.InferResult`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferResult "tritonclient.grpc.InferResult"), [`tritonclient.grpc.InferenceServerException`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException")) objects.

Note

This object can be used to cancel the inference request like below:

>>> it = stream_infer(...)
>>> ret = it.cancel()

Return type:
asynchronous iterator

Raises:
[**tritonclient.grpc.InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If inputs_iterator does not yield the correct input.

_async_ unload_model(_model\_name_,_headers=None_,_unload\_dependents=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.unload_model "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.unload_model()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.unload_model "tritonclient.grpc.InferenceServerClient.unload_model")

_async_ unregister_cuda_shared_memory(_name=''_,_headers=None_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.unregister_cuda_shared_memory "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.unregister_cuda_shared_memory()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.unregister_cuda_shared_memory "tritonclient.grpc.InferenceServerClient.unregister_cuda_shared_memory")

_async_ unregister_system_shared_memory(_name=''_,_headers=None_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.unregister_system_shared_memory "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.unregister_system_shared_memory()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.unregister_system_shared_memory "tritonclient.grpc.InferenceServerClient.unregister_system_shared_memory")

_async_ update_log_settings(_settings_,_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.update_log_settings "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.update_log_settings()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.update_log_settings "tritonclient.grpc.InferenceServerClient.update_log_settings")

_async_ update_trace_settings(_model\_name=None_,_settings={}_,_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html#tritonclient.grpc.aio.InferenceServerClient.update_trace_settings "Link to this definition")
Refer to [`tritonclient.grpc.InferenceServerClient.update_trace_settings()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.update_trace_settings "tritonclient.grpc.InferenceServerClient.update_trace_settings")

Modules
