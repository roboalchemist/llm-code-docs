# Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html

Title: tritonclient.grpc — NVIDIA Triton Inference Server

URL Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html

Markdown Content:
_class_ tritonclient.grpc.InferInput(_name_, _shape_, _datatype_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferInput "Link to this definition")
An object of InferInput class is used to describe input tensor for an inference request.

Parameters:
*   **name** (_str_) – The name of input whose data will be described by this object

*   **shape** (_list_) – The shape of the associated input.

*   **datatype** (_str_) – The datatype of the associated input.

_get_content()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferInput._get_content "Link to this definition")
Retrieve the contents for this tensor in raw bytes. :returns: The associated contents for this tensor in raw bytes. :rtype: bytes

_get_tensor()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferInput._get_tensor "Link to this definition")
Retrieve the underlying InferInputTensor message. :returns: The underlying InferInputTensor protobuf message. :rtype: protobuf message

datatype()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferInput.datatype "Link to this definition")
Get the datatype of input associated with this object.

Returns:
The datatype of input

Return type:
str

name()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferInput.name "Link to this definition")
Get the name of input associated with this object.

Returns:
The name of input

Return type:
str

set_data_from_numpy(_input\_tensor_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferInput.set_data_from_numpy "Link to this definition")
Set the tensor data from the specified numpy array for input associated with this object.

Parameters:
**input_tensor** (_numpy array_) – The tensor data in numpy array format

Returns:
The updated input

Return type:
[InferInput](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferInput "tritonclient.grpc.InferInput")

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If failed to set data for the tensor.

set_shape(_shape_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferInput.set_shape "Link to this definition")
Set the shape of input.

Parameters:
**shape** (_list_) – The shape of the associated input.

Returns:
The updated input

Return type:
[InferInput](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferInput "tritonclient.grpc.InferInput")

set_shared_memory(_region\_name_, _byte\_size_, _offset=0_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferInput.set_shared_memory "Link to this definition")
Set the tensor data from the specified shared memory region.

Parameters:
*   **region_name** (_str_) – The name of the shared memory region holding tensor data.

*   **byte_size** (_int_) – The size of the shared memory region holding tensor data.

*   **offset** (_int_) – The offset, in bytes, into the region where the data for the tensor starts. The default value is 0.

Returns:
The updated input

Return type:
[InferInput](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferInput "tritonclient.grpc.InferInput")

shape()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferInput.shape "Link to this definition")
Get the shape of input associated with this object.

Returns:
The shape of input

Return type:
list

_class_ tritonclient.grpc.InferRequestedOutput(_name_, _class\_count=0_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferRequestedOutput "Link to this definition")
An object of [`InferRequestedOutput`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferRequestedOutput "tritonclient.grpc.InferRequestedOutput") class is used to describe a requested output tensor for an inference request.

Parameters:
*   **name** (_str_) – The name of output tensor to associate with this object

*   **class_count** (_int_) – The number of classifications to be requested. The default value is 0 which means the classification results are not requested.

_get_tensor()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferRequestedOutput._get_tensor "Link to this definition")
Retrieve the underlying InferRequestedOutputTensor message. :returns: The underlying InferRequestedOutputTensor protobuf message. :rtype: protobuf message

name()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferRequestedOutput.name "Link to this definition")
Get the name of output associated with this object.

Returns:
The name of output

Return type:
str

set_shared_memory(_region\_name_,_byte\_size_,_offset=0_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferRequestedOutput.set_shared_memory "Link to this definition")
Marks the output to return the inference result in specified shared memory region.

Parameters:
*   **region_name** (_str_) – The name of the shared memory region to hold tensor data.

*   **byte_size** (_int_) – The size of the shared memory region to hold tensor data.

*   **offset** (_int_) – The offset, in bytes, into the region where the data for the tensor starts. The default value is 0.

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If failed to set shared memory for the tensor.

unset_shared_memory()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferRequestedOutput.unset_shared_memory "Link to this definition")
Clears the shared memory option set by the last call to [`InferRequestedOutput.set_shared_memory()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferRequestedOutput.set_shared_memory "tritonclient.grpc.InferRequestedOutput.set_shared_memory"). After call to this function requested output will no longer be returned in a shared memory region.

_class_ tritonclient.grpc.InferResult(_result_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferResult "Link to this definition")
An object of [`InferResult`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferResult "tritonclient.grpc.InferResult") class holds the response of an inference request and provide methods to retrieve inference results.

Parameters:
**result** (_protobuf message_) – The ModelInferResponse returned by the server

as_numpy(_name_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferResult.as_numpy "Link to this definition")
Get the tensor data for output associated with this object in numpy format

Parameters:
**name** (_str_) – The name of the output tensor whose result is to be retrieved.

Returns:
The numpy array containing the response data for the tensor or None if the data for specified tensor name is not found.

Return type:
numpy array

get_output(_name_, _as\_json=False_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferResult.get_output "Link to this definition")
Retrieves the InferOutputTensor corresponding to the named output.

Parameters:
*   **name** (_str_) – The name of the tensor for which Output is to be retrieved.

*   **as_json** (_bool_) – If True then returns response as a json dict, otherwise as a protobuf message. Default value is False. The returned json is generated from the protobuf message using MessageToJson and as a result int64 values are represented as string. It is the caller’s responsibility to convert these strings back to int64 values as necessary.

Returns:
If a InferOutputTensor with specified name is present in ModelInferResponse then returns it as a protobuf message or dict, otherwise returns None.

Return type:
protobuf message or dict

get_response(_as\_json=False_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferResult.get_response "Link to this definition")
Retrieves the complete ModelInferResponse as a json dict object or protobuf message

Parameters:
**as_json** (_bool_) – If True then returns response as a json dict, otherwise as a protobuf message. Default value is False. The returned json is generated from the protobuf message using MessageToJson and as a result int64 values are represented as string. It is the caller’s responsibility to convert these strings back to int64 values as necessary.

Returns:
The underlying ModelInferResponse as a protobuf message or dict.

Return type:
protobuf message or dict

_class_ tritonclient.grpc.InferenceServerClient(_url_,_verbose=False_,_ssl=False_,_root\_certificates=None_,_private\_key=None_,_certificate\_chain=None_,_creds=None_,_keepalive\_options=None_,_channel\_args=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient "Link to this definition")
An InferenceServerClient object is used to perform any kind of communication with the InferenceServer using gRPC protocol. Most of the methods are thread-safe except start_stream, stop_stream and async_stream_infer. Accessing a client stream with different threads will cause undefined behavior.

Parameters:
*   **url** (_str_) – The inference server URL, e.g. ‘localhost:8001’.

*   **verbose** (_bool_) – If True generate verbose output. Default value is False.

*   **ssl** (_bool_) – If True use SSL encrypted secure channel. Default is False.

*   **root_certificates** (_str_) – File holding the PEM-encoded root certificates as a byte string, or None to retrieve them from a default location chosen by gRPC runtime. The option is ignored if ssl is False. Default is None.

*   **private_key** (_str_) – File holding the PEM-encoded private key as a byte string, or None if no private key should be used. The option is ignored if ssl is False. Default is None.

*   **certificate_chain** (_str_) – File holding PEM-encoded certificate chain as a byte string to use or None if no certificate chain should be used. The option is ignored if ssl is False. Default is None.

*   **creds** (_grpc.ChannelCredentials_) – A grpc.ChannelCredentials object to use for the connection. The ssl, root_certificates, private_key and certificate_chain options will be ignored when using this option. Default is None.

*   **keepalive_options** ([_KeepAliveOptions_](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.KeepAliveOptions "tritonclient.grpc.KeepAliveOptions")) – Object encapsulating various GRPC KeepAlive options. See the class definition for more information. Default is None.

*   **channel_args** (_List_ _[_ _Tuple_ _]_) – List of Tuple pairs (“key”, value) to be passed directly to the GRPC channel as the channel_arguments. If this argument is provided, it is expected the channel arguments are correct and complete, and the keepalive_options parameter will be ignored since the corresponding keepalive channel arguments can be set directly in this parameter. See [https://grpc.github.io/grpc/python/glossary.html#term-channel_arguments](https://grpc.github.io/grpc/python/glossary.html#term-channel_arguments) for more details. Default is None.

Raises:
**Exception** – If unable to create a client.

_get_metadata(_headers_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient._get_metadata "Link to this definition")async_infer(_model\_name_,_inputs_,_callback_,_model\_version=''_,_outputs=None_,_request\_id=''_,_sequence\_id=0_,_sequence\_start=False_,_sequence\_end=False_,_priority=0_,_timeout=None_,_client\_timeout=None_,_headers=None_,_compression\_algorithm=None_,_parameters=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.async_infer "Link to this definition")
Run asynchronous inference using the supplied ‘inputs’ requesting the outputs specified by ‘outputs’.

Parameters:
*   **model_name** (_str_) – The name of the model to run inference.

*   **inputs** (_list_) – A list of [`InferInput`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferInput "tritonclient.grpc.InferInput") objects, each describing data for a input tensor required by the model.

*   **callback** (_function_) – Python function that is invoked once the request is completed. The function must reserve the last two arguments (result, error) to hold [`InferResult`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferResult "tritonclient.grpc.InferResult") and [`InferenceServerException`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") objects respectively which will be provided to the function when executing the callback. The ownership of these objects will be given to the user. The ‘error’ would be None for a successful inference.

*   **model_version** (_str_) – The version of the model to run inference. The default value is an empty string which means then the server will choose a version based on the model and internal policy.

*   **outputs** (_list_) – A list of [`InferRequestedOutput`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferRequestedOutput "tritonclient.grpc.InferRequestedOutput") objects, each describing how the output data must be returned. If not specified all outputs produced by the model will be returned using default settings.

*   **request_id** (_str_) – Optional identifier for the request. If specified will be returned in the response. Default value is an empty string which means no request_id will be used.

*   **sequence_id** (_int_) – The unique identifier for the sequence being represented by the object. Default value is 0 which means that the request does not belong to a sequence.

*   **sequence_start** (_bool_) – Indicates whether the request being added marks the start of the sequence. Default value is False. This argument is ignored if ‘sequence_id’ is 0.

*   **sequence_end** (_bool_) – Indicates whether the request being added marks the end of the sequence. Default value is False. This argument is ignored if ‘sequence_id’ is 0.

*   **priority** (_int_) – Indicates the priority of the request. Priority value zero indicates that the default priority level should be used (i.e. same behavior as not specifying the priority parameter). Lower value priorities indicate higher priority levels. Thus the highest priority level is indicated by setting the parameter to 1, the next highest is 2, etc. If not provided, the server will handle the request using default setting for the model.

*   **timeout** (_int_) – The timeout value for the request, in microseconds. If the request cannot be completed within the time the server can take a model-specific action such as terminating the request. If not provided, the server will handle the request using default setting for the model. This option is only respected by the model that is configured with dynamic batching. See here for more details: [triton-inference-server/server](https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_configuration.md#dynamic-batcher) The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and provide error with message “Deadline Exceeded” in the callback when the specified time elapses. The default value is None which means client will wait for the response from the server.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **compression_algorithm** (_str_) – Optional grpc compression algorithm to be used on client side. Currently supports “deflate”, “gzip” and None. By default, no compression is used.

*   **parameters** (_dict_) – Optional custom parameters to be included in the inference request.

Returns:
A representation of a computation in another control flow. Computations represented by a Future may be yet to be begun, ongoing, or have already completed.

Note

This object can be used to cancel the inference request like below:

>>> future = async_infer(...)
>>> ret = future.cancel()

Return type:
CallContext

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If server fails to issue inference.

async_stream_infer(_model\_name_,_inputs_,_model\_version=''_,_outputs=None_,_request\_id=''_,_sequence\_id=0_,_sequence\_start=False_,_sequence\_end=False_,_enable\_empty\_final\_response=False_,_priority=0_,_timeout=None_,_parameters=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.async_stream_infer "Link to this definition")
Runs an asynchronous inference over gRPC bi-directional streaming API. A stream must be established with a call to start_stream() before calling this function. All the results will be provided to the callback function associated with the stream.

Parameters:
*   **model_name** (_str_) – The name of the model to run inference.

*   **inputs** (_list_) – A list of [`InferInput`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferInput "tritonclient.grpc.InferInput") objects, each describing data for a input tensor required by the model.

*   **model_version** (_str_) – The version of the model to run inference. The default value is an empty string which means then the server will choose a version based on the model and internal policy.

*   **outputs** (_list_) – A list of [`InferRequestedOutput`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferRequestedOutput "tritonclient.grpc.InferRequestedOutput") objects, each describing how the output data must be returned. If not specified all outputs produced by the model will be returned using default settings.

*   **request_id** (_str_) – Optional identifier for the request. If specified will be returned in the response. Default value is an empty string which means no request_id will be used.

*   **sequence_id** (_int_ _or_ _str_) – The unique identifier for the sequence being represented by the object. A value of 0 or “” means that the request does not belong to a sequence. Default is 0.

*   **sequence_start** (_bool_) – Indicates whether the request being added marks the start of the sequence. Default value is False. This argument is ignored if ‘sequence_id’ is 0 or “”.

*   **sequence_end** (_bool_) – Indicates whether the request being added marks the end of the sequence. Default value is False. This argument is ignored if ‘sequence_id’ is 0 or “”.

*   **enable_empty_final_response** (_bool_) – Indicates whether “empty” responses should be generated and sent back to the client from the server during streaming inference when they contain the TRITONSERVER_RESPONSE_COMPLETE_FINAL flag. This strictly relates to the case of models/backends that send flags-only responses (use TRITONBACKEND_ResponseFactorySendFlags(TRITONSERVER_RESPONSE_COMPLETE_FINAL) or InferenceResponseSender.send(flags=TRITONSERVER_RESPONSE_COMPLETE_FINAL)) Currently, this only occurs for decoupled models, and can be used to communicate to the client when a request has received its final response from the model. If the backend sends the final flag along with a non-empty response, this arg is not needed. Default value is False.

*   **priority** (_int_) – Indicates the priority of the request. Priority value zero indicates that the default priority level should be used (i.e. same behavior as not specifying the priority parameter). Lower value priorities indicate higher priority levels. Thus the highest priority level is indicated by setting the parameter to 1, the next highest is 2, etc. If not provided, the server will handle the request using default setting for the model.

*   **timeout** (_int_) – The timeout value for the request, in microseconds. If the request cannot be completed within the time the server can take a model-specific action such as terminating the request. If not provided, the server will handle the request using default setting for the model. This does not stop the grpc stream itself and is only respected by the model that is configured with dynamic batching. See here for more details: [triton-inference-server/server](https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_configuration.md#dynamic-batcher)

*   **parameters** (_dict_) – Optional custom parameters to be included in the inference request.

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If server fails to issue inference.

close()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.close "Link to this definition")
Close the client. Any future calls to server will result in an Error.

get_cuda_shared_memory_status(_region\_name=''_,_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_cuda_shared_memory_status "Link to this definition")
Request cuda shared memory status from the server.

Parameters:
*   **region_name** (_str_) – The name of the region to query status. The default value is an empty string, which means that the status of all active cuda shared memory will be returned.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **as_json** (_bool_) – If True then returns cuda shared memory status as a json dict, otherwise as a protobuf message. Default value is False. The returned json is generated from the protobuf message using MessageToJson and as a result int64 values are represented as string. It is the caller’s responsibility to convert these strings back to int64 values as necessary.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Returns:
The JSON dict or CudaSharedMemoryStatusResponse message holding the cuda shared memory status.

Return type:
dict or protobuf message

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to get the status of specified shared memory or has timed out.

get_inference_statistics(_model\_name=''_,_model\_version=''_,_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_inference_statistics "Link to this definition")
Get the inference statistics for the specified model name and version.

Parameters:
*   **model_name** (_str_) – The name of the model to get statistics. The default value is an empty string, which means statistics of all models will be returned.

*   **model_version** (_str_) – The version of the model to get inference statistics. The default value is an empty string which means then the server will return the statistics of all available model versions.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **as_json** (_bool_) – If True then returns inference statistics as a json dict, otherwise as a protobuf message. Default value is False. The returned json is generated from the protobuf message using MessageToJson and as a result int64 values are represented as string. It is the caller’s responsibility to convert these strings back to int64 values as necessary.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to get the model inference statistics or has timed out.

get_log_settings(_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_log_settings "Link to this definition")
Get the global log settings.

Parameters:
*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **as_json** (_bool_) – If True then returns log settings as a json dict, otherwise as a protobuf message. Default value is False. The returned json is generated from the protobuf message using MessageToJson and as a result int64 values are represented as string. It is the caller’s responsibility to convert these strings back to int64 values as necessary.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Returns:
The JSON dict or LogSettingsResponse message holding the log settings.

Return type:
dict or protobuf message

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to get the log settings or has timed out.

get_model_config(_model\_name_,_model\_version=''_,_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_model_config "Link to this definition")
Contact the inference server and get the configuration for specified model.

Parameters:
*   **model_name** (_str_) – The name of the model

*   **model_version** (_str_) – The version of the model to get configuration. The default value is an empty string which means then the server will choose a version based on the model and internal policy.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **as_json** (_bool_) – If True then returns configuration as a json dict, otherwise as a protobuf message. Default value is False. The returned json is generated from the protobuf message using MessageToJson and as a result int64 values are represented as string. It is the caller’s responsibility to convert these strings back to int64 values as necessary.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Returns:
The JSON dict or ModelConfigResponse message holding the metadata.

Return type:
dict or protobuf message

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to get model configuration or has timed out.

get_model_metadata(_model\_name_,_model\_version=''_,_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_model_metadata "Link to this definition")
Contact the inference server and get the metadata for specified model.

Parameters:
*   **model_name** (_str_) – The name of the model

*   **model_version** (_str_) – The version of the model to get metadata. The default value is an empty string which means then the server will choose a version based on the model and internal policy.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **as_json** (_bool_) – If True then returns model metadata as a json dict, otherwise as a protobuf message. Default value is False. The returned json is generated from the protobuf message using MessageToJson and as a result int64 values are represented as string. It is the caller’s responsibility to convert these strings back to int64 values as necessary.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Returns:
The JSON dict or ModelMetadataResponse message holding the metadata.

Return type:
dict or protobuf message

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to get model metadata or has timed out.

get_model_repository_index(_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_model_repository_index "Link to this definition")
Get the index of model repository contents

Parameters:
*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **as_json** (_bool_) – If True then returns model repository index as a json dict, otherwise as a protobuf message. Default value is False. The returned json is generated from the protobuf message using MessageToJson and as a result int64 values are represented as string. It is the caller’s responsibility to convert these strings back to int64 values as necessary.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Returns:
The JSON dict or RepositoryIndexResponse message holding the model repository index.

Return type:
dict or protobuf message

get_server_metadata(_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_server_metadata "Link to this definition")
Contact the inference server and get its metadata.

Parameters:
*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **as_json** (_bool_) – If True then returns server metadata as a json dict, otherwise as a protobuf message. Default value is False. The returned json is generated from the protobuf message using MessageToJson and as a result int64 values are represented as string. It is the caller’s responsibility to convert these strings back to int64 values as necessary.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Returns:
The JSON dict or ServerMetadataResponse message holding the metadata.

Return type:
dict or protobuf message

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to get server metadata or has timed out.

get_system_shared_memory_status(_region\_name=''_,_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_system_shared_memory_status "Link to this definition")
Request system shared memory status from the server.

Parameters:
*   **region_name** (_str_) – The name of the region to query status. The default value is an empty string, which means that the status of all active system shared memory will be returned.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **as_json** (_bool_) – If True then returns system shared memory status as a json dict, otherwise as a protobuf message. Default value is False. The returned json is generated from the protobuf message using MessageToJson and as a result int64 values are represented as string. It is the caller’s responsibility to convert these strings back to int64 values as necessary.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Returns:
The JSON dict or SystemSharedMemoryStatusResponse message holding the system shared memory status.

Return type:
dict or protobuf message

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to get the status of specified shared memory or has timed out.

get_trace_settings(_model\_name=None_,_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.get_trace_settings "Link to this definition")
Get the trace settings for the specified model name, or global trace settings if model name is not given

Parameters:
*   **model_name** (_str_) – The name of the model to get trace settings. Specifying None or empty string will return the global trace settings. The default value is None.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **as_json** (_bool_) – If True then returns trace settings as a json dict, otherwise as a protobuf message. Default value is False. The returned json is generated from the protobuf message using MessageToJson and as a result int64 values are represented as string. It is the caller’s responsibility to convert these strings back to int64 values as necessary.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Returns:
The JSON dict or TraceSettingResponse message holding the trace settings.

Return type:
dict or protobuf message

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to get the trace settings or has timed out.

infer(_model\_name_,_inputs_,_model\_version=''_,_outputs=None_,_request\_id=''_,_sequence\_id=0_,_sequence\_start=False_,_sequence\_end=False_,_priority=0_,_timeout=None_,_client\_timeout=None_,_headers=None_,_compression\_algorithm=None_,_parameters=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.infer "Link to this definition")
Run synchronous inference using the supplied ‘inputs’ requesting the outputs specified by ‘outputs’.

Parameters:
*   **model_name** (_str_) – The name of the model to run inference.

*   **inputs** (_list_) – A list of [`InferInput`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferInput "tritonclient.grpc.InferInput") objects, each describing data for a input tensor required by the model.

*   **model_version** (_str_) – The version of the model to run inference. The default value is an empty string which means then the server will choose a version based on the model and internal policy.

*   **outputs** (_list_) – A list of [`InferRequestedOutput`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferRequestedOutput "tritonclient.grpc.InferRequestedOutput") objects, each describing how the output data must be returned. If not specified all outputs produced by the model will be returned using default settings.

*   **request_id** (_str_) – Optional identifier for the request. If specified will be returned in the response. Default value is an empty string which means no request_id will be used.

*   **sequence_id** (_int_) – The unique identifier for the sequence being represented by the object. Default value is 0 which means that the request does not belong to a sequence.

*   **sequence_start** (_bool_) – Indicates whether the request being added marks the start of the sequence. Default value is False. This argument is ignored if ‘sequence_id’ is 0.

*   **sequence_end** (_bool_) – Indicates whether the request being added marks the end of the sequence. Default value is False. This argument is ignored if ‘sequence_id’ is 0.

*   **priority** (_int_) – Indicates the priority of the request. Priority value zero indicates that the default priority level should be used (i.e. same behavior as not specifying the priority parameter). Lower value priorities indicate higher priority levels. Thus the highest priority level is indicated by setting the parameter to 1, the next highest is 2, etc. If not provided, the server will handle the request using default setting for the model.

*   **timeout** (_int_) – The timeout value for the request, in microseconds. If the request cannot be completed within the time the server can take a model-specific action such as terminating the request. If not provided, the server will handle the request using default setting for the model. This option is only respected by the model that is configured with dynamic batching. See here for more details: [triton-inference-server/server](https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_configuration.md#dynamic-batcher)

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **compression_algorithm** (_str_) – Optional grpc compression algorithm to be used on client side. Currently supports “deflate”, “gzip” and None. By default, no compression is used.

*   **parameters** (_dict_) – Optional custom parameters to be included in the inference request.

Returns:
The object holding the result of the inference.

Return type:
[InferResult](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferResult "tritonclient.grpc.InferResult")

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If server fails to perform inference.

is_model_ready(_model\_name_,_model\_version=''_,_headers=None_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.is_model_ready "Link to this definition")
Contact the inference server and get the readiness of specified model.

Parameters:
*   **model_name** (_str_) – The name of the model to check for readiness.

*   **model_version** (_str_) – The version of the model to check for readiness. The default value is an empty string which means then the server will choose a version based on the model and internal policy.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Returns:
True if the model is ready, False if not ready.

Return type:
bool

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to get model readiness or has timed out.

is_server_live(_headers=None_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.is_server_live "Link to this definition")
Contact the inference server and get liveness.

Parameters:
*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Returns:
True if server is live, False if server is not live.

Return type:
bool

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to get liveness or has timed out.

is_server_ready(_headers=None_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.is_server_ready "Link to this definition")
Contact the inference server and get readiness.

Parameters:
*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Returns:
True if server is ready, False if server is not ready.

Return type:
bool

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to get readiness or has timed out.

load_model(_model\_name_,_headers=None_,_config=None_,_files=None_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.load_model "Link to this definition")
Request the inference server to load or reload specified model.

Parameters:
*   **model_name** (_str_) – The name of the model to be loaded.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **config** (_str_) – Optional JSON representation of a model config provided for the load request, if provided, this config will be used for loading the model.

*   **files** (_dict_) – Optional dictionary specifying file path (with “file:” prefix) in the override model directory to the file content as bytes. The files will form the model directory that the model will be loaded from. If specified, ‘config’ must be provided to be the model configuration of the override model directory.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to load the model or has timed out.

register_cuda_shared_memory(_name_,_raw\_handle_,_device\_id_,_byte\_size_,_headers=None_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.register_cuda_shared_memory "Link to this definition")
Request the server to register a system shared memory with the following specification.

Parameters:
*   **name** (_str_) – The name of the region to register.

*   **raw_handle** (_bytes_) – The raw serialized cudaIPC handle in base64 encoding.

*   **device_id** (_int_) – The GPU device ID on which the cudaIPC handle was created.

*   **byte_size** (_int_) – The size of the cuda shared memory region, in bytes.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to register the specified cuda shared memory or has timed out.

register_system_shared_memory(_name_,_key_,_byte\_size_,_offset=0_,_headers=None_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.register_system_shared_memory "Link to this definition")
Request the server to register a system shared memory with the following specification.

Parameters:
*   **name** (_str_) – The name of the region to register.

*   **key** (_str_) – The key of the underlying memory object that contains the system shared memory region.

*   **byte_size** (_int_) – The size of the system shared memory region, in bytes.

*   **offset** (_int_) – Offset, in bytes, within the underlying memory object to the start of the system shared memory region. The default value is zero.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to register the specified system shared memory or has timed out.

start_stream(_callback_,_stream\_timeout=None_,_headers=None_,_compression\_algorithm=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.start_stream "Link to this definition")
Starts a grpc bi-directional stream to send streaming inferences. Note: When using stream, user must ensure the InferenceServerClient.close() gets called at exit.

Parameters:
*   **callback** (_function_) – Python function that is invoked upon receiving response from the underlying stream. The function must reserve the last two arguments (result, error) to hold [`InferResult`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferResult "tritonclient.grpc.InferResult") and [`InferenceServerException`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") objects respectively which will be provided to the function when executing the callback. The ownership of these objects will be given to the user. The ‘error’ would be None for a successful inference.

*   **stream_timeout** (_float_) – Optional stream timeout (in seconds). The stream will be closed once the specified timeout expires.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **compression_algorithm** (_str_) – Optional grpc compression algorithm to be used on client side. Currently supports “deflate”, “gzip” and None. By default, no compression is used.

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to start a stream or a stream was already running for this client or has timed out.

stop_stream(_cancel\_requests=False_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.stop_stream "Link to this definition")
Stops a stream if one available.

Parameters:
**cancel_requests** (_bool_) – If set True, then client cancels all the pending requests and closes the stream. If set False, the call blocks till all the pending requests on the stream are processed.

unload_model(_model\_name_,_headers=None_,_unload\_dependents=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.unload_model "Link to this definition")
Request the inference server to unload specified model.

Parameters:
*   **model_name** (_str_) – The name of the model to be unloaded.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **unload_dependents** (_bool_) – Whether the dependents of the model should also be unloaded.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to unload the model or has timed out.

unregister_cuda_shared_memory(_name=''_,_headers=None_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.unregister_cuda_shared_memory "Link to this definition")
Request the server to unregister a cuda shared memory with the specified name.

Parameters:
*   **name** (_str_) – The name of the region to unregister. The default value is empty string which means all the cuda shared memory regions will be unregistered.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to unregister the specified cuda shared memory region or has timed out.

unregister_system_shared_memory(_name=''_,_headers=None_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.unregister_system_shared_memory "Link to this definition")
Request the server to unregister a system shared memory with the specified name.

Parameters:
*   **name** (_str_) – The name of the region to unregister. The default value is empty string which means all the system shared memory regions will be unregistered.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to unregister the specified system shared memory region or has timed out.

update_log_settings(_settings_,_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.update_log_settings "Link to this definition")
Update the global log settings. Returns the log settings after the update.

Parameters:
*   **settings** (_dict_) – The new log setting values. Only the settings listed will be updated.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **as_json** (_bool_) – If True then returns trace settings as a json dict, otherwise as a protobuf message. Default value is False. The returned json is generated from the protobuf message using MessageToJson and as a result int64 values are represented as string. It is the caller’s responsibility to convert these strings back to int64 values as necessary.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Returns:
The JSON dict or LogSettingsResponse message holding the updated log settings.

Return type:
dict or protobuf message

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to update the log settings or has timed out.

update_trace_settings(_model\_name=None_,_settings={}_,_headers=None_,_as\_json=False_,_client\_timeout=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClient.update_trace_settings "Link to this definition")
Update the trace settings for the specified model name, or global trace settings if model name is not given. Returns the trace settings after the update.

Parameters:
*   **model_name** (_str_) – The name of the model to update trace settings. Specifying None or empty string will update the global trace settings. The default value is None.

*   **settings** (_dict_) – The new trace setting values. Only the settings listed will be updated. If a trace setting is listed in the dictionary with a value of ‘None’, that setting will be cleared.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **as_json** (_bool_) – If True then returns trace settings as a json dict, otherwise as a protobuf message. Default value is False. The returned json is generated from the protobuf message using MessageToJson and as a result int64 values are represented as string. It is the caller’s responsibility to convert these strings back to int64 values as necessary.

*   **client_timeout** (_float_) – The maximum end-to-end time, in seconds, the request is allowed to take. The client will abort request and raise InferenceServerExeption with message “Deadline Exceeded” when the specified time elapses. The default value is None which means client will wait for the response from the server.

Returns:
The JSON dict or TraceSettingResponse message holding the updated trace settings.

Return type:
dict or protobuf message

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "tritonclient.grpc.InferenceServerException") – If unable to update the trace settings or has timed out.

_class_ tritonclient.grpc.InferenceServerClientPlugin[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClientPlugin "Link to this definition")
Every Triton Client Plugin should extend this class. Each plugin needs to implement the [`__call__()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClientPlugin.__call__ "tritonclient.grpc.InferenceServerClientPlugin.__call__") method.

_abstract_ __call__ (_request_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClientPlugin.__call__ "Link to this definition")
This method will be called when any of the client functions are invoked. Note that the request object must be modified in-place.

Parameters:
**request** ([_Request_](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.Request "tritonclient.grpc.Request")) – The request object.

_abc_impl _=<\_abc.\_abc\_data object>_[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerClientPlugin._abc_impl "Link to this definition")_exception_ tritonclient.grpc.InferenceServerException(_msg_, _status=None_, _debug\_details=None_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException "Link to this definition")
Exception indicating non-Success status.

Parameters:
*   **msg** (_str_) – A brief description of error

*   **status** (_str_) – The error code

*   **debug_details** (_str_) – The additional details on the error

debug_details()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException.debug_details "Link to this definition")
Get the detailed information about the exception for debugging purposes

Returns:
Returns the exception details

Return type:
str

message()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException.message "Link to this definition")
Get the exception message.

Returns:
The message associated with this exception, or None if no message.

Return type:
str

status()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.InferenceServerException.status "Link to this definition")
Get the status of the exception.

Returns:
Returns the status of the exception

Return type:
str

_class_ tritonclient.grpc.KeepAliveOptions(_keepalive\_time\_ms=2147483647_,_keepalive\_timeout\_ms=20000_,_keepalive\_permit\_without\_calls=False_,_http2\_max\_pings\_without\_data=2_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.KeepAliveOptions "Link to this definition")
A KeepAliveOptions object is used to encapsulate GRPC KeepAlive related parameters for initiating an InferenceServerclient object.

See the [grpc/grpc](https://github.com/grpc/grpc/blob/master/doc/keepalive.md) documentation for more information.

Parameters:
*   **keepalive_time_ms** (_int_) – The period (in milliseconds) after which a keepalive ping is sent on the transport. Default is INT32_MAX.

*   **keepalive_timeout_ms** (_int_) – The period (in milliseconds) the sender of the keepalive ping waits for an acknowledgement. If it does not receive an acknowledgment within this time, it will close the connection. Default is 20000 (20 seconds).

*   **keepalive_permit_without_calls** (_bool_) – Allows keepalive pings to be sent even if there are no calls in flight. Default is False.

*   **http2_max_pings_without_data** (_int_) – The maximum number of pings that can be sent when there is no data/header frame to be sent. gRPC Core will not continue sending pings if we run over the limit. Setting it to 0 allows sending pings without such a restriction. Default is 2.

_class_ tritonclient.grpc.Request(_headers_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html#tritonclient.grpc.Request "Link to this definition")
A request object.

Parameters:
**headers** (_dict_) – A dictionary containing the request headers.

Modules
