# Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html

Title: tritonclient.http.aio — NVIDIA Triton Inference Server

URL Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html

Markdown Content:
Classes

_class_ tritonclient.http.aio.InferenceServerClient(_url_,_verbose=False_,_conn\_limit=100_,_conn\_timeout=60.0_,_ssl=False_,_ssl\_context=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient "Link to this definition")
This feature is currently in beta and may be subject to change.

An analogy of the [`tritonclient.http.InferenceServerClient`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient "tritonclient.http.InferenceServerClient") to enable calling via asyncio syntax. The object is intended to be used by a single thread and simultaneously calling methods with different threads is not supported and can cause undefined behavior.

Returns a header that is valid for aiohttp.

Parameters:
**headers** (_dict_ _(or_ _None_ _)_) – HTTP headers to fix before processing the request.

_async_ _get(_request\_uri_, _headers_, _query\_params_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient._get "Link to this definition")
Issues the GET request to the server

Parameters:
*   **request_uri** (_str_) – The request URI to be used in GET request.

*   **headers** (_dict_) – Additional HTTP headers to include in the request.

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction.

Returns:
The response from server.

Return type:
aiohttp.ClientResponse

_async_ _post(_request\_uri_,_request\_body_,_headers_,_query\_params_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient._post "Link to this definition")
Issues the POST request to the server

Parameters:
*   **request_uri** (_str_) – The request URI to be used in POST request.

*   **request_body** (_str_) – The body of the request

*   **headers** (_dict_) – Additional HTTP headers to include in the request.

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction.

Returns:
The response from server.

Return type:
aiohttp.ClientResponse

Checks for any unsupported HTTP headers before processing a request.

Parameters:
**headers** (_dict_) – HTTP headers to validate before processing the request.

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If an unsupported HTTP header is included in a request.

_async_ close()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.close "Link to this definition")
Close the client. Any future calls to server will result in an Error.

_static_ generate_request_body(_inputs_,_outputs=None_,_request\_id=''_,_sequence\_id=0_,_sequence\_start=False_,_sequence\_end=False_,_priority=0_,_timeout=None_,_parameters=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.generate_request_body "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.generate_request_body()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.generate_request_body "tritonclient.http.InferenceServerClient.generate_request_body")

_async_ get_cuda_shared_memory_status(_region\_name=''_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.get_cuda_shared_memory_status "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.get_cuda_shared_memory_status()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_cuda_shared_memory_status "tritonclient.http.InferenceServerClient.get_cuda_shared_memory_status")

_async_ get_inference_statistics(_model\_name=''_,_model\_version=''_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.get_inference_statistics "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.get_inference_statistics()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_inference_statistics "tritonclient.http.InferenceServerClient.get_inference_statistics")

_async_ get_log_settings(_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.get_log_settings "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.get_log_settings()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_log_settings "tritonclient.http.InferenceServerClient.get_log_settings")

_async_ get_model_config(_model\_name_,_model\_version=''_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.get_model_config "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.get_model_config()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_model_config "tritonclient.http.InferenceServerClient.get_model_config")

_async_ get_model_metadata(_model\_name_,_model\_version=''_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.get_model_metadata "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.get_model_metadata()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_model_metadata "tritonclient.http.InferenceServerClient.get_model_metadata")

_async_ get_model_repository_index(_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.get_model_repository_index "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.get_model_repository_index()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_model_repository_index "tritonclient.http.InferenceServerClient.get_model_repository_index")

_async_ get_server_metadata(_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.get_server_metadata "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.get_server_metadata()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_server_metadata "tritonclient.http.InferenceServerClient.get_server_metadata")

_async_ get_system_shared_memory_status(_region\_name=''_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.get_system_shared_memory_status "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.get_system_shared_memory_status()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_system_shared_memory_status "tritonclient.http.InferenceServerClient.get_system_shared_memory_status")

_async_ get_trace_settings(_model\_name=None_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.get_trace_settings "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.get_trace_settings()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_trace_settings "tritonclient.http.InferenceServerClient.get_trace_settings")

_async_ infer(_model\_name_,_inputs_,_model\_version=''_,_outputs=None_,_request\_id=''_,_sequence\_id=0_,_sequence\_start=False_,_sequence\_end=False_,_priority=0_,_timeout=None_,_headers=None_,_query\_params=None_,_request\_compression\_algorithm=None_,_response\_compression\_algorithm=None_,_parameters=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.infer "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.infer()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.infer "tritonclient.http.InferenceServerClient.infer")

_async_ is_model_ready(_model\_name_,_model\_version=''_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.is_model_ready "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.is_model_ready()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.is_model_ready "tritonclient.http.InferenceServerClient.is_model_ready")

_async_ is_server_live(_headers=None_, _query\_params=None_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.is_server_live "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.is_server_live()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.is_server_live "tritonclient.http.InferenceServerClient.is_server_live")

_async_ is_server_ready(_headers=None_, _query\_params=None_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.is_server_ready "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.is_server_ready()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.is_server_ready "tritonclient.http.InferenceServerClient.is_server_ready")

_async_ load_model(_model\_name_,_headers=None_,_query\_params=None_,_config=None_,_files=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.load_model "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.load_model()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.load_model "tritonclient.http.InferenceServerClient.load_model")

_static_ parse_response_body(_response\_body_,_verbose=False_,_header\_length=None_,_content\_encoding=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.parse_response_body "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.parse_response_body()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.parse_response_body "tritonclient.http.InferenceServerClient.parse_response_body")

_async_ register_cuda_shared_memory(_name_,_raw\_handle_,_device\_id_,_byte\_size_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.register_cuda_shared_memory "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.register_cuda_shared_memory()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.register_cuda_shared_memory "tritonclient.http.InferenceServerClient.register_cuda_shared_memory")

_async_ register_system_shared_memory(_name_,_key_,_byte\_size_,_offset=0_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.register_system_shared_memory "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.register_system_shared_memory()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.register_system_shared_memory "tritonclient.http.InferenceServerClient.register_system_shared_memory")

_async_ unload_model(_model\_name_,_headers=None_,_query\_params=None_,_unload\_dependents=False_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.unload_model "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.unload_model()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.unload_model "tritonclient.http.InferenceServerClient.unload_model")

_async_ unregister_cuda_shared_memory(_name=''_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.unregister_cuda_shared_memory "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.unregister_cuda_shared_memory()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.unregister_cuda_shared_memory "tritonclient.http.InferenceServerClient.unregister_cuda_shared_memory")

_async_ unregister_system_shared_memory(_name=''_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.unregister_system_shared_memory "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.unregister_system_shared_memory()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.unregister_system_shared_memory "tritonclient.http.InferenceServerClient.unregister_system_shared_memory")

_async_ update_log_settings(_settings_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.update_log_settings "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.update_log_settings()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.update_log_settings "tritonclient.http.InferenceServerClient.update_log_settings")

_async_ update_trace_settings(_model\_name=None_,_settings={}_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio.InferenceServerClient.update_trace_settings "Link to this definition")
Refer to [`tritonclient.http.InferenceServerClient.update_trace_settings()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.update_trace_settings "tritonclient.http.InferenceServerClient.update_trace_settings")

_async_ tritonclient.http.aio._get_error(_response_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio._get_error "Link to this definition")
Returns the `InferenceServerException` object if response indicates the error. If no error then return None

_async_ tritonclient.http.aio._raise_if_error(_response_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html#tritonclient.http.aio._raise_if_error "Link to this definition")
Raise `InferenceServerException` if received non-Success response from the server

Modules
