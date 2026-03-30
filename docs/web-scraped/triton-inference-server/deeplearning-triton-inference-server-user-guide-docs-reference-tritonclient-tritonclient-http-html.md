# Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html

Title: tritonclient.http — NVIDIA Triton Inference Server

URL Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html

Markdown Content:
_class_ tritonclient.http.InferAsyncRequest(_greenlet_, _verbose=False_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferAsyncRequest "Link to this definition")
An object of InferAsyncRequest class is used to describe a handle to an ongoing asynchronous inference request.

Parameters:
*   **greenlet** (_gevent.Greenlet_) – The greenlet object which will provide the results. For further details about greenlets refer [http://www.gevent.org/api/gevent.greenlet.html](http://www.gevent.org/api/gevent.greenlet.html).

*   **verbose** (_bool_) – If True generate verbose output. Default value is False.

get_result(_block=True_, _timeout=None_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferAsyncRequest.get_result "Link to this definition")
Get the results of the associated asynchronous inference.

Parameters:
*   **block** (_bool_) – If block is True, the function will wait till the corresponding response is received from the server. Default value is True.

*   **timeout** (_int_) – The maximum wait time for the function. This setting is ignored if the block is set False. Default is None, which means the function will block indefinitely till the corresponding response is received.

Returns:
The object holding the result of the async inference.

Return type:
[InferResult](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferResult "tritonclient.http.InferResult")

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If server fails to perform inference or failed to respond within specified timeout.

_class_ tritonclient.http.InferInput(_name_, _shape_, _datatype_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferInput "Link to this definition")
An object of InferInput class is used to describe input tensor for an inference request.

Parameters:
*   **name** (_str_) – The name of input whose data will be described by this object

*   **shape** (_list_) – The shape of the associated input.

*   **datatype** (_str_) – The datatype of the associated input.

_get_binary_data()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferInput._get_binary_data "Link to this definition")
Returns the raw binary data if available

Returns:
The raw data for the input tensor

Return type:
bytes

_get_tensor()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferInput._get_tensor "Link to this definition")
Retrieve the underlying input as json dict.

Returns:
The underlying tensor specification as dict

Return type:
dict

datatype()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferInput.datatype "Link to this definition")
Get the datatype of input associated with this object.

Returns:
The datatype of input

Return type:
str

name()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferInput.name "Link to this definition")
Get the name of input associated with this object.

Returns:
The name of input

Return type:
str

set_data_from_numpy(_input\_tensor_, _binary\_data=True_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferInput.set_data_from_numpy "Link to this definition")
Set the tensor data from the specified numpy array for input associated with this object.

Parameters:
*   **input_tensor** (_numpy array_) – The tensor data in numpy array format

*   **binary_data** (_bool_) – Indicates whether to set data for the input in binary format or explicit tensor within JSON. The default value is True, which means the data will be delivered as binary data in the HTTP body after the JSON object.

Returns:
The updated input

Return type:
[InferInput](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferInput "tritonclient.http.InferInput")

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If failed to set data for the tensor.

set_shape(_shape_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferInput.set_shape "Link to this definition")
Set the shape of input.

Parameters:
**shape** (_list_) – The shape of the associated input.

Returns:
The updated input

Return type:
[InferInput](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferInput "tritonclient.http.InferInput")

set_shared_memory(_region\_name_, _byte\_size_, _offset=0_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferInput.set_shared_memory "Link to this definition")
Set the tensor data from the specified shared memory region.

Parameters:
*   **region_name** (_str_) – The name of the shared memory region holding tensor data.

*   **byte_size** (_int_) – The size of the shared memory region holding tensor data.

*   **offset** (_int_) – The offset, in bytes, into the region where the data for the tensor starts. The default value is 0.

Returns:
The updated input

Return type:
[InferInput](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferInput "tritonclient.http.InferInput")

shape()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferInput.shape "Link to this definition")
Get the shape of input associated with this object.

Returns:
The shape of input

Return type:
list

_class_ tritonclient.http.InferRequestedOutput(_name_, _binary\_data=True_, _class\_count=0_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferRequestedOutput "Link to this definition")
An object of [`InferRequestedOutput`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferRequestedOutput "tritonclient.http.InferRequestedOutput") class is used to describe a requested output tensor for an inference request.

Parameters:
*   **name** (_str_) – The name of output tensor to associate with this object.

*   **binary_data** (_bool_) – Indicates whether to return result data for the output in binary format or explicit tensor within JSON. The default value is True, which means the data will be delivered as binary data in the HTTP body after JSON object. This field will be unset if shared memory is set for the output.

*   **class_count** (_int_) – The number of classifications to be requested. The default value is 0 which means the classification results are not requested.

_get_tensor()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferRequestedOutput._get_tensor "Link to this definition")
Retrieve the underlying input as json dict.

Returns:
The underlying tensor as a dict

Return type:
dict

name()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferRequestedOutput.name "Link to this definition")
Get the name of output associated with this object.

Returns:
The name of output

Return type:
str

set_shared_memory(_region\_name_,_byte\_size_,_offset=0_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferRequestedOutput.set_shared_memory "Link to this definition")
Marks the output to return the inference result in specified shared memory region.

Parameters:
*   **region_name** (_str_) – The name of the shared memory region to hold tensor data.

*   **byte_size** (_int_) – The size of the shared memory region to hold tensor data.

*   **offset** (_int_) – The offset, in bytes, into the region where the data for the tensor starts. The default value is 0.

unset_shared_memory()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferRequestedOutput.unset_shared_memory "Link to this definition")
Clears the shared memory option set by the last call to [`InferRequestedOutput.set_shared_memory()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferRequestedOutput.set_shared_memory "tritonclient.http.InferRequestedOutput.set_shared_memory"). After call to this function requested output will no longer be returned in a shared memory region.

_class_ tritonclient.http.InferResult(_response_, _verbose_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferResult "Link to this definition")
An object of [`InferResult`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferResult "tritonclient.http.InferResult") class holds the response of an inference request and provide methods to retrieve inference results.

Parameters:
*   **response** (_geventhttpclient.response.HTTPSocketPoolResponse_) – The inference response from the server

*   **verbose** (_bool_) – If True generate verbose output. Default value is False.

as_numpy(_name_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferResult.as_numpy "Link to this definition")
Get the tensor data for output associated with this object in numpy format

Parameters:
**name** (_str_) – The name of the output tensor whose result is to be retrieved.

Returns:
The numpy array containing the response data for the tensor or None if the data for specified tensor name is not found.

Return type:
numpy array

_classmethod_ from_response_body(_response\_body_,_verbose=False_,_header\_length=None_,_content\_encoding=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferResult.from_response_body "Link to this definition")
A class method to construct [`InferResult`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferResult "tritonclient.http.InferResult") object from a given ‘response_body’.

Parameters:
*   **response_body** (_bytes_) – The inference response from the server

*   **verbose** (_bool_) – If True generate verbose output. Default value is False.

*   **header_length** (_int_) – The length of the inference header if the header does not occupy the whole response body. Default value is None.

*   **content_encoding** (_string_) – The encoding of the response body if it is compressed. Default value is None.

Returns:
The InferResult object generated from the response body

Return type:
[InferResult](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferResult "tritonclient.http.InferResult")

get_output(_name_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferResult.get_output "Link to this definition")
Retrieves the output tensor corresponding to the named output.

Parameters:
**name** (_str_) – The name of the tensor for which Output is to be retrieved.

Returns:
If an output tensor with specified name is present in the infer response then returns it as a json dict, otherwise returns None.

Return type:
Dict

get_response()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferResult.get_response "Link to this definition")
Retrieves the complete response

Returns:
The underlying response dict.

Return type:
dict

_class_ tritonclient.http.InferenceServerClient(_url_,_verbose=False_,_concurrency=1_,_connection\_timeout=60.0_,_network\_timeout=60.0_,_max\_greenlets=None_,_ssl=False_,_ssl\_options=None_,_ssl\_context\_factory=None_,_insecure=False_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient "Link to this definition")
An InferenceServerClient object is used to perform any kind of communication with the InferenceServer using http protocol. None of the methods are thread safe. The object is intended to be used by a single thread and simultaneously calling different methods with different threads is not supported and will cause undefined behavior.

Parameters:
*   **url** (_str_) – The inference server name, port and optional base path in the following format: host:port/<base-path>, e.g. ‘localhost:8000’.

*   **verbose** (_bool_) – If True generate verbose output. Default value is False.

*   **concurrency** (_int_) – The number of connections to create for this client. Default value is 1.

*   **connection_timeout** (_float_) – The timeout value for the connection. Default value is 60.0 sec.

*   **network_timeout** (_float_) – The timeout value for the network. Default value is 60.0 sec

*   **max_greenlets** (_int_) – Determines the maximum allowed number of worker greenlets for handling asynchronous inference requests. Default value is None, which means there will be no restriction on the number of greenlets created.

*   **ssl** (_bool_) – If True, channels the requests to encrypted https scheme. Some improper settings may cause connection to prematurely terminate with an unsuccessful handshake. See ssl_context_factory option for using secure default settings. Default value for this option is False.

*   **ssl_options** (_dict_) – Any options supported by ssl.wrap_socket specified as dictionary. The argument is ignored if ‘ssl’ is specified False.

*   **ssl_context_factory** (_SSLContext callable_) – It must be a callbable that returns a SSLContext. Set to gevent.ssl.create_default_context to use contexts with secure default settings. This should most likely resolve connection issues in a secure way. The default value for this option is None which directly wraps the socket with the options provided via ssl_options. The argument is ignored if ‘ssl’ is specified False.

*   **insecure** (_bool_) – If True, then does not match the host name with the certificate. Default value is False. The argument is ignored if ‘ssl’ is specified False.

Raises:
**Exception** – If unable to create a client.

_get(_request\_uri_, _headers_, _query\_params_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient._get "Link to this definition")
Issues the GET request to the server

Parameters:
*   **request_uri** (_str_) – The request URI to be used in GET request.

*   **headers** (_dict_) – Additional HTTP headers to include in the request.

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction.

Returns:
The response from server.

Return type:
geventhttpclient.response.HTTPSocketPoolResponse

_post(_request\_uri_,_request\_body_,_headers_,_query\_params_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient._post "Link to this definition")
Issues the POST request to the server

Parameters:
*   **request_uri** (_str_) – The request URI to be used in POST request.

*   **request_body** (_str_) – The body of the request

*   **headers** (_dict_) – Additional HTTP headers to include in the request.

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction.

Returns:
The response from server.

Return type:
geventhttpclient.response.HTTPSocketPoolResponse

Checks for any unsupported HTTP headers before processing a request.

Parameters:
**headers** (_dict_) – HTTP headers to validate before processing the request.

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If an unsupported HTTP header is included in a request.

async_infer(_model\_name_,_inputs_,_model\_version=''_,_outputs=None_,_request\_id=''_,_sequence\_id=0_,_sequence\_start=False_,_sequence\_end=False_,_priority=0_,_timeout=None_,_headers=None_,_query\_params=None_,_request\_compression\_algorithm=None_,_response\_compression\_algorithm=None_,_parameters=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.async_infer "Link to this definition")
Run asynchronous inference using the supplied ‘inputs’ requesting the outputs specified by ‘outputs’. Even though this call is non-blocking, however, the actual number of concurrent requests to the server will be limited by the ‘concurrency’ parameter specified while creating this client. In other words, if the inflight async_infer exceeds the specified ‘concurrency’, the delivery of the exceeding request(s) to server will be blocked till the slot is made available by retrieving the results of previously issued requests.

Parameters:
*   **model_name** (_str_) – The name of the model to run inference.

*   **inputs** (_list_) – A list of [`InferInput`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferInput "tritonclient.http.InferInput") objects, each describing data for a input tensor required by the model.

*   **model_version** (_str_) – The version of the model to run inference. The default value is an empty string which means then the server will choose a version based on the model and internal policy.

*   **outputs** (_list_) – A list of [`InferRequestedOutput`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferRequestedOutput "tritonclient.http.InferRequestedOutput") objects, each describing how the output data must be returned. If not specified all outputs produced by the model will be returned using default settings.

*   **request_id** (_str_) – Optional identifier for the request. If specified will be returned in the response. Default value is ‘None’ which means no request_id will be used.

*   **sequence_id** (_int_) – The unique identifier for the sequence being represented by the object. Default value is 0 which means that the request does not belong to a sequence.

*   **sequence_start** (_bool_) – Indicates whether the request being added marks the start of the sequence. Default value is False. This argument is ignored if ‘sequence_id’ is 0.

*   **sequence_end** (_bool_) – Indicates whether the request being added marks the end of the sequence. Default value is False. This argument is ignored if ‘sequence_id’ is 0.

*   **priority** (_int_) – Indicates the priority of the request. Priority value zero indicates that the default priority level should be used (i.e. same behavior as not specifying the priority parameter). Lower value priorities indicate higher priority levels. Thus the highest priority level is indicated by setting the parameter to 1, the next highest is 2, etc. If not provided, the server will handle the request using default setting for the model.

*   **timeout** (_int_) – The timeout value for the request, in microseconds. If the request cannot be completed within the time the server can take a model-specific action such as terminating the request. If not provided, the server will handle the request using default setting for the model. This option is only respected by the model that is configured with dynamic batching. See here for more details: [triton-inference-server/server](https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_configuration.md#dynamic-batcher)

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction.

*   **request_compression_algorithm** (_str_) – Optional HTTP compression algorithm to use for the request body on client side. Currently supports “deflate”, “gzip” and None. By default, no compression is used.

*   **response_compression_algorithm** (_str_) – Optional HTTP compression algorithm to request for the response body. Note that the response may not be compressed if the server does not support the specified algorithm. Currently supports “deflate”, “gzip” and None. By default, no compression is requested.

*   **parameters** (_dict_) – Optional custom parameters to be included in the inference request.

Returns:
The handle to the asynchronous inference request.

Return type:
[InferAsyncRequest](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferAsyncRequest "tritonclient.http.InferAsyncRequest")

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If server fails to issue inference.

close()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.close "Link to this definition")
Close the client. Any future calls to server will result in an Error.

_static_ generate_request_body(_inputs_,_outputs=None_,_request\_id=''_,_sequence\_id=0_,_sequence\_start=False_,_sequence\_end=False_,_priority=0_,_timeout=None_,_parameters=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.generate_request_body "Link to this definition")
Generate a request body for inference using the supplied ‘inputs’ requesting the outputs specified by ‘outputs’.

Parameters:
*   **inputs** (_list_) – A list of [`InferInput`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferInput "tritonclient.http.InferInput") objects, each describing data for a input tensor required by the model.

*   **outputs** (_list_) – A list of [`InferRequestedOutput`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferRequestedOutput "tritonclient.http.InferRequestedOutput") objects, each describing how the output data must be returned. If not specified all outputs produced by the model will be returned using default settings.

*   **request_id** (_str_) – Optional identifier for the request. If specified will be returned in the response. Default value is an empty string which means no request_id will be used.

*   **sequence_id** (_int_ _or_ _str_) – The unique identifier for the sequence being represented by the object. A value of 0 or “” means that the request does not belong to a sequence. Default is 0.

*   **sequence_start** (_bool_) – Indicates whether the request being added marks the start of the sequence. Default value is False. This argument is ignored if ‘sequence_id’ is 0.

*   **sequence_end** (_bool_) – Indicates whether the request being added marks the end of the sequence. Default value is False. This argument is ignored if ‘sequence_id’ is 0.

*   **priority** (_int_) – Indicates the priority of the request. Priority value zero indicates that the default priority level should be used (i.e. same behavior as not specifying the priority parameter). Lower value priorities indicate higher priority levels. Thus the highest priority level is indicated by setting the parameter to 1, the next highest is 2, etc. If not provided, the server will handle the request using default setting for the model.

*   **timeout** (_int_) – The timeout value for the request, in microseconds. If the request cannot be completed within the time the server can take a model-specific action such as terminating the request. If not provided, the server will handle the request using default setting for the model. This option is only respected by the model that is configured with dynamic batching. See here for more details: [triton-inference-server/server](https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_configuration.md#dynamic-batcher)

*   **parameters** (_dict_) – Optional fields to be included in the ‘parameters’ fields.

Returns:
*   _Bytes_ – The request body of the inference.

*   _Int_ – The byte size of the inference request header in the request body. Returns None if the whole request body constitutes the request header.

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If server fails to perform inference.

get_cuda_shared_memory_status(_region\_name=''_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_cuda_shared_memory_status "Link to this definition")
Request cuda shared memory status from the server.

Parameters:
*   **region_name** (_str_) – The name of the region to query status. The default value is an empty string, which means that the status of all active cuda shared memory will be returned.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction

Returns:
The JSON dict holding cuda shared memory status.

Return type:
dict

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to get the status of specified shared memory.

get_inference_statistics(_model\_name=''_,_model\_version=''_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_inference_statistics "Link to this definition")
Get the inference statistics for the specified model name and version.

Parameters:
*   **model_name** (_str_) – The name of the model to get statistics. The default value is an empty string, which means statistics of all models will be returned.

*   **model_version** (_str_) – The version of the model to get inference statistics. The default value is an empty string which means then the server will return the statistics of all available model versions.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction

Returns:
The JSON dict holding the model inference statistics.

Return type:
dict

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to get the model inference statistics.

get_log_settings(_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_log_settings "Link to this definition")
Get the global log settings for the Triton server

Parameters:
*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction

Returns:
The JSON dict holding the log settings.

Return type:
dict

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to get the log settings.

get_model_config(_model\_name_,_model\_version=''_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_model_config "Link to this definition")
Contact the inference server and get the configuration for specified model.

Parameters:
*   **model_name** (_str_) – The name of the model

*   **model_version** (_str_) – The version of the model to get configuration. The default value is an empty string which means then the server will choose a version based on the model and internal policy.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction

Returns:
The JSON dict holding the model config.

Return type:
dict

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to get model configuration.

get_model_metadata(_model\_name_,_model\_version=''_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_model_metadata "Link to this definition")
Contact the inference server and get the metadata for specified model.

Parameters:
*   **model_name** (_str_) – The name of the model

*   **model_version** (_str_) – The version of the model to get metadata. The default value is an empty string which means then the server will choose a version based on the model and internal policy.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction

Returns:
The JSON dict holding the metadata.

Return type:
dict

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to get model metadata.

get_model_repository_index(_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_model_repository_index "Link to this definition")
Get the index of model repository contents

Parameters:
*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction

Returns:
The JSON dict holding the model repository index.

Return type:
dict

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to get the repository index.

get_server_metadata(_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_server_metadata "Link to this definition")
Contact the inference server and get its metadata.

Parameters:
*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction.

Returns:
The JSON dict holding the metadata.

Return type:
dict

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to get server metadata.

get_system_shared_memory_status(_region\_name=''_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_system_shared_memory_status "Link to this definition")
Request system shared memory status from the server.

Parameters:
*   **region_name** (_str_) – The name of the region to query status. The default value is an empty string, which means that the status of all active system shared memory will be returned.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction

Returns:
The JSON dict holding system shared memory status.

Return type:
dict

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to get the status of specified shared memory.

get_trace_settings(_model\_name=None_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.get_trace_settings "Link to this definition")
Get the trace settings for the specified model name, or global trace settings if model name is not given

Parameters:
*   **model_name** (_str_) – The name of the model to get trace settings. Specifying None or empty string will return the global trace settings. The default value is None.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction

Returns:
The JSON dict holding the trace settings.

Return type:
dict

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to get the trace settings.

infer(_model\_name_,_inputs_,_model\_version=''_,_outputs=None_,_request\_id=''_,_sequence\_id=0_,_sequence\_start=False_,_sequence\_end=False_,_priority=0_,_timeout=None_,_headers=None_,_query\_params=None_,_request\_compression\_algorithm=None_,_response\_compression\_algorithm=None_,_parameters=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.infer "Link to this definition")
Run synchronous inference using the supplied ‘inputs’ requesting the outputs specified by ‘outputs’.

Parameters:
*   **model_name** (_str_) – The name of the model to run inference.

*   **inputs** (_list_) – A list of [`InferInput`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferInput "tritonclient.http.InferInput") objects, each describing data for a input tensor required by the model.

*   **model_version** (_str_) – The version of the model to run inference. The default value is an empty string which means then the server will choose a version based on the model and internal policy.

*   **outputs** (_list_) – A list of [`InferRequestedOutput`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferRequestedOutput "tritonclient.http.InferRequestedOutput") objects, each describing how the output data must be returned. If not specified all outputs produced by the model will be returned using default settings.

*   **request_id** (_str_) – Optional identifier for the request. If specified will be returned in the response. Default value is an empty string which means no request_id will be used.

*   **sequence_id** (_int_) – The unique identifier for the sequence being represented by the object. Default value is 0 which means that the request does not belong to a sequence.

*   **sequence_start** (_bool_) – Indicates whether the request being added marks the start of the sequence. Default value is False. This argument is ignored if ‘sequence_id’ is 0.

*   **sequence_end** (_bool_) – Indicates whether the request being added marks the end of the sequence. Default value is False. This argument is ignored if ‘sequence_id’ is 0.

*   **priority** (_int_) – Indicates the priority of the request. Priority value zero indicates that the default priority level should be used (i.e. same behavior as not specifying the priority parameter). Lower value priorities indicate higher priority levels. Thus the highest priority level is indicated by setting the parameter to 1, the next highest is 2, etc. If not provided, the server will handle the request using default setting for the model.

*   **timeout** (_int_) – The timeout value for the request, in microseconds. If the request cannot be completed within the time the server can take a model-specific action such as terminating the request. If not provided, the server will handle the request using default setting for the model. This option is only respected by the model that is configured with dynamic batching. See here for more details: [triton-inference-server/server](https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_configuration.md#dynamic-batcher)

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction.

*   **request_compression_algorithm** (_str_) – Optional HTTP compression algorithm to use for the request body on client side. Currently supports “deflate”, “gzip” and None. By default, no compression is used.

*   **response_compression_algorithm** (_str_) – Optional HTTP compression algorithm to request for the response body. Note that the response may not be compressed if the server does not support the specified algorithm. Currently supports “deflate”, “gzip” and None. By default, no compression is requested.

*   **parameters** (_dict_) – Optional fields to be included in the ‘parameters’ fields.

Returns:
The object holding the result of the inference.

Return type:
[InferResult](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferResult "tritonclient.http.InferResult")

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If server fails to perform inference.

is_model_ready(_model\_name_,_model\_version=''_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.is_model_ready "Link to this definition")
Contact the inference server and get the readiness of specified model.

Parameters:
*   **model_name** (_str_) – The name of the model to check for readiness.

*   **model_version** (_str_) – The version of the model to check for readiness. The default value is an empty string which means then the server will choose a version based on the model and internal policy.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction.

Returns:
True if the model is ready, False if not ready.

Return type:
bool

Raises:
**Exception** – If unable to get model readiness.

is_server_live(_headers=None_, _query\_params=None_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.is_server_live "Link to this definition")
Contact the inference server and get liveness.

Parameters:
*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction.

Returns:
True if server is live, False if server is not live.

Return type:
bool

Raises:
**Exception** – If unable to get liveness.

is_server_ready(_headers=None_, _query\_params=None_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.is_server_ready "Link to this definition")
Contact the inference server and get readiness.

Parameters:
*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction.

Returns:
True if server is ready, False if server is not ready.

Return type:
bool

Raises:
**Exception** – If unable to get readiness.

load_model(_model\_name_,_headers=None_,_query\_params=None_,_config=None_,_files=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.load_model "Link to this definition")
Request the inference server to load or reload specified model.

Parameters:
*   **model_name** (_str_) – The name of the model to be loaded.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction.

*   **config** (_str_) – Optional JSON representation of a model config provided for the load request, if provided, this config will be used for loading the model.

*   **files** (_dict_) – Optional dictionary specifying file path (with “file:” prefix) in the override model directory to the file content as bytes. The files will form the model directory that the model will be loaded from. If specified, ‘config’ must be provided to be the model configuration of the override model directory.

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to load the model.

_static_ parse_response_body(_response\_body_,_verbose=False_,_header\_length=None_,_content\_encoding=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.parse_response_body "Link to this definition")
Generate a [`InferResult`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferResult "tritonclient.http.InferResult") object from the given ‘response_body’

Parameters:
*   **response_body** (_bytes_) – The inference response from the server

*   **verbose** (_bool_) – If True generate verbose output. Default value is False.

*   **header_length** (_int_) – The length of the inference header if the header does not occupy the whole response body. Default value is None.

*   **content_encoding** (_string_) – The encoding of the response body if it is compressed. Default value is None.

Returns:
The InferResult object generated from the response body

Return type:
[InferResult](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferResult "tritonclient.http.InferResult")

register_cuda_shared_memory(_name_,_raw\_handle_,_device\_id_,_byte\_size_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.register_cuda_shared_memory "Link to this definition")
Request the server to register a system shared memory with the following specification.

Parameters:
*   **name** (_str_) – The name of the region to register.

*   **raw_handle** (_bytes_) – The raw serialized cudaIPC handle in base64 encoding.

*   **device_id** (_int_) – The GPU device ID on which the cudaIPC handle was created.

*   **byte_size** (_int_) – The size of the cuda shared memory region, in bytes.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to register the specified cuda shared memory.

register_system_shared_memory(_name_,_key_,_byte\_size_,_offset=0_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.register_system_shared_memory "Link to this definition")
Request the server to register a system shared memory with the following specification.

Parameters:
*   **name** (_str_) – The name of the region to register.

*   **key** (_str_) – The key of the underlying memory object that contains the system shared memory region.

*   **byte_size** (_int_) – The size of the system shared memory region, in bytes.

*   **offset** (_int_) – Offset, in bytes, within the underlying memory object to the start of the system shared memory region. The default value is zero.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to register the specified system shared memory.

unload_model(_model\_name_,_headers=None_,_query\_params=None_,_unload\_dependents=False_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.unload_model "Link to this definition")
Request the inference server to unload specified model.

Parameters:
*   **model_name** (_str_) – The name of the model to be unloaded.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction

*   **unload_dependents** (_bool_) – Whether the dependents of the model should also be unloaded.

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to unload the model.

unregister_cuda_shared_memory(_name=''_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.unregister_cuda_shared_memory "Link to this definition")
Request the server to unregister a cuda shared memory with the specified name.

Parameters:
*   **name** (_str_) – The name of the region to unregister. The default value is empty string which means all the cuda shared memory regions will be unregistered.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to unregister the specified cuda shared memory region.

unregister_system_shared_memory(_name=''_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.unregister_system_shared_memory "Link to this definition")
Request the server to unregister a system shared memory with the specified name.

Parameters:
*   **name** (_str_) – The name of the region to unregister. The default value is empty string which means all the system shared memory regions will be unregistered.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to unregister the specified system shared memory region.

update_log_settings(_settings_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.update_log_settings "Link to this definition")
Update the global log settings of the Triton server.

Parameters:
*   **settings** (_dict_) – The new log setting values. Only the settings listed will be updated.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction

Returns:
The JSON dict holding the updated log settings.

Return type:
dict

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to update the log settings.

update_trace_settings(_model\_name=None_,_settings={}_,_headers=None_,_query\_params=None_,)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClient.update_trace_settings "Link to this definition")
Update the trace settings for the specified model name, or global trace settings if model name is not given. Returns the trace settings after the update.

Parameters:
*   **model_name** (_str_) – The name of the model to update trace settings. Specifying None or empty string will update the global trace settings. The default value is None.

*   **settings** (_dict_) – The new trace setting values. Only the settings listed will be updated. If a trace setting is listed in the dictionary with a value of ‘None’, that setting will be cleared.

*   **headers** (_dict_) – Optional dictionary specifying additional HTTP headers to include in the request.

*   **query_params** (_dict_) – Optional url query parameters to use in network transaction

Returns:
The JSON dict holding the updated trace settings.

Return type:
dict

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "tritonclient.http.InferenceServerException") – If unable to update the trace settings.

_class_ tritonclient.http.InferenceServerClientPlugin[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClientPlugin "Link to this definition")
Every Triton Client Plugin should extend this class. Each plugin needs to implement the [`__call__()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClientPlugin.__call__ "tritonclient.http.InferenceServerClientPlugin.__call__") method.

_abstract_ __call__ (_request_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClientPlugin.__call__ "Link to this definition")
This method will be called when any of the client functions are invoked. Note that the request object must be modified in-place.

Parameters:
**request** ([_Request_](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.Request "tritonclient.http.Request")) – The request object.

_abc_impl _=<\_abc.\_abc\_data object>_[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerClientPlugin._abc_impl "Link to this definition")_exception_ tritonclient.http.InferenceServerException(_msg_, _status=None_, _debug\_details=None_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException "Link to this definition")
Exception indicating non-Success status.

Parameters:
*   **msg** (_str_) – A brief description of error

*   **status** (_str_) – The error code

*   **debug_details** (_str_) – The additional details on the error

debug_details()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException.debug_details "Link to this definition")
Get the detailed information about the exception for debugging purposes

Returns:
Returns the exception details

Return type:
str

message()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException.message "Link to this definition")
Get the exception message.

Returns:
The message associated with this exception, or None if no message.

Return type:
str

status()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.InferenceServerException.status "Link to this definition")
Get the status of the exception.

Returns:
Returns the status of the exception

Return type:
str

_class_ tritonclient.http.Request(_headers_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html#tritonclient.http.Request "Link to this definition")
A request object.

Parameters:
**headers** (_dict_) – A dictionary containing the request headers.

Modules
