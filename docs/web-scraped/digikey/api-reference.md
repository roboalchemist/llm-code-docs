# DigiKey API Python Client Reference

# Source: https://github.com/peeter123/digikey-api.git

## API Endpoints

### `strtobool()`

Convert a string representation of truth to true (1) or false (0).
    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.

	Copy from distutils.utils, which was removed in Python 3.12

### `wrap_exception_in()`

Wraps raised exception in another exception type, and only includes
    the original exception type name in the new exception message.
    Args:
        exc_type: Exception type
        catch: optional, Exception type to catch

### `retry()`

Applies exponential backoff and exception wrapper decorators to expose
    a single decorator, to wrap functions that make HTTP requests.

### `logger_file()`

The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str

### `logger_file()`

The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str

### `debug()`

Debug status

        :param value: The debug status, True or False.
        :type: bool

### `debug()`

Debug status

        :param value: The debug status, True or False.
        :type: bool

### `logger_format()`

The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str

### `logger_format()`

The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str

### `get_api_key_with_prefix()`

Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :return: The token for api key authentication.

### `get_basic_auth_token()`

Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.

### `auth_settings()`

Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.

### `to_debug_report()`

Gets the essential information for debugging.

        :return: The report for debugging.

### `getheaders()`

Returns a dictionary of the response headers.

### `getheader()`

Returns a given response header.

### `request()`

Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.

### `user_agent()`

User agent for this API client

### `sanitize_for_serialization()`

Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.

### `deserialize()`

Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.

### `call_api()`

Makes the HTTP request (synchronous) and returns deserialized data.

        To make an async request, set the async_req parameter.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response: Response data type.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return:
            If async_req parameter is True,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter async_req is False or missing,
            then the method will return the response directly.

### `request()`

Makes the HTTP request using RESTClient.

### `parameters_to_tuples()`

Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted

### `prepare_post_parameters()`

Builds form parameters.

        :param post_params: Normal form parameters.
        :param files: File parameters.
        :return: Form parameters with files.

### `select_header_accept()`

Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).

### `select_header_content_type()`

Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).

### `update_params_for_auth()`

Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.

### `logger_file()`

The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str

### `logger_file()`

The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str

### `debug()`

Debug status

        :param value: The debug status, True or False.
        :type: bool

### `debug()`

Debug status

        :param value: The debug status, True or False.
        :type: bool

### `logger_format()`

The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str

### `logger_format()`

The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str

### `get_api_key_with_prefix()`

Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :return: The token for api key authentication.

### `get_basic_auth_token()`

Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.

### `auth_settings()`

Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.

### `to_debug_report()`

Gets the essential information for debugging.

        :return: The report for debugging.

### `getheaders()`

Returns a dictionary of the response headers.

### `getheader()`

Returns a given response header.

### `request()`

Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.

### `user_agent()`

User agent for this API client

### `sanitize_for_serialization()`

Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.

### `deserialize()`

Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.

### `call_api()`

Makes the HTTP request (synchronous) and returns deserialized data.

        To make an async request, set the async_req parameter.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response: Response data type.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return:
            If async_req parameter is True,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter async_req is False or missing,
            then the method will return the response directly.

### `request()`

Makes the HTTP request using RESTClient.

### `parameters_to_tuples()`

Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted

### `prepare_post_parameters()`

Builds form parameters.

        :param post_params: Normal form parameters.
        :param files: File parameters.
        :return: Form parameters with files.

### `select_header_accept()`

Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).

### `select_header_content_type()`

Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).

### `update_params_for_auth()`

Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.

### `logger_file()`

The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str

### `logger_file()`

The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str

### `debug()`

Debug status

        :param value: The debug status, True or False.
        :type: bool

### `debug()`

Debug status

        :param value: The debug status, True or False.
        :type: bool

### `logger_format()`

The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str

### `logger_format()`

The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str

### `get_api_key_with_prefix()`

Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :return: The token for api key authentication.

### `get_basic_auth_token()`

Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.

### `auth_settings()`

Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.

### `to_debug_report()`

Gets the essential information for debugging.

        :return: The report for debugging.

### `getheaders()`

Returns a dictionary of the response headers.

### `getheader()`

Returns a given response header.

### `request()`

Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.

### `user_agent()`

User agent for this API client

### `sanitize_for_serialization()`

Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.

### `deserialize()`

Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.

### `call_api()`

Makes the HTTP request (synchronous) and returns deserialized data.

        To make an async request, set the async_req parameter.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response: Response data type.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return:
            If async_req parameter is True,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter async_req is False or missing,
            then the method will return the response directly.

### `request()`

Makes the HTTP request using RESTClient.

### `parameters_to_tuples()`

Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted

### `prepare_post_parameters()`

Builds form parameters.

        :param post_params: Normal form parameters.
        :param files: File parameters.
        :return: Form parameters with files.

### `select_header_accept()`

Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).

### `select_header_content_type()`

Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).

### `update_params_for_auth()`

Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.

### `po_line_item_number()`

Gets the po_line_item_number of this LineItem.  # noqa: E501

        Line item number provided on purchase order  # noqa: E501

        :return: The po_line_item_number of this LineItem.  # noqa: E501
        :rtype: str

### `po_line_item_number()`

Sets the po_line_item_number of this LineItem.

        Line item number provided on purchase order  # noqa: E501

        :param po_line_item_number: The po_line_item_number of this LineItem.  # noqa: E501
        :type: str

### `digi_key_part_number()`

Gets the digi_key_part_number of this LineItem.  # noqa: E501

        The Digi-Key part number.  # noqa: E501

        :return: The digi_key_part_number of this LineItem.  # noqa: E501
        :rtype: str

### `digi_key_part_number()`

Sets the digi_key_part_number of this LineItem.

        The Digi-Key part number.  # noqa: E501

        :param digi_key_part_number: The digi_key_part_number of this LineItem.  # noqa: E501
        :type: str

### `manufacturer_part_number()`

Gets the manufacturer_part_number of this LineItem.  # noqa: E501

        The Manufacturer Part Number.  # noqa: E501

        :return: The manufacturer_part_number of this LineItem.  # noqa: E501
        :rtype: str

### `manufacturer_part_number()`

Sets the manufacturer_part_number of this LineItem.

        The Manufacturer Part Number.  # noqa: E501

        :param manufacturer_part_number: The manufacturer_part_number of this LineItem.  # noqa: E501
        :type: str

### `product_description()`

Gets the product_description of this LineItem.  # noqa: E501

        Catalog description of the product.  # noqa: E501

        :return: The product_description of this LineItem.  # noqa: E501
        :rtype: str

### `product_description()`

Sets the product_description of this LineItem.

        Catalog description of the product.  # noqa: E501

        :param product_description: The product_description of this LineItem.  # noqa: E501
        :type: str

### `manufacturer()`

Gets the manufacturer of this LineItem.  # noqa: E501

        The Manufacturer of the product.  # noqa: E501

        :return: The manufacturer of this LineItem.  # noqa: E501
        :rtype: str

### `manufacturer()`

Sets the manufacturer of this LineItem.

        The Manufacturer of the product.  # noqa: E501

        :param manufacturer: The manufacturer of this LineItem.  # noqa: E501
        :type: str

### `country_of_origin()`

Gets the country_of_origin of this LineItem.  # noqa: E501

        The Country Of Origin of the product  # noqa: E501

        :return: The country_of_origin of this LineItem.  # noqa: E501
        :rtype: str

### `country_of_origin()`

Sets the country_of_origin of this LineItem.

        The Country Of Origin of the product  # noqa: E501

        :param country_of_origin: The country_of_origin of this LineItem.  # noqa: E501
        :type: str

### `quantity()`

Gets the quantity of this LineItem.  # noqa: E501

        The total quantity for the order.  # noqa: E501

        :return: The quantity of this LineItem.  # noqa: E501
        :rtype: int

### `quantity()`

Sets the quantity of this LineItem.

        The total quantity for the order.  # noqa: E501

        :param quantity: The quantity of this LineItem.  # noqa: E501
        :type: int

### `customer_reference()`

Gets the customer_reference of this LineItem.  # noqa: E501

        Freeform customer reference  # noqa: E501

        :return: The customer_reference of this LineItem.  # noqa: E501
        :rtype: str

### `customer_reference()`

Sets the customer_reference of this LineItem.

        Freeform customer reference  # noqa: E501

        :param customer_reference: The customer_reference of this LineItem.  # noqa: E501
        :type: str

### `unit_price()`

Gets the unit_price of this LineItem.  # noqa: E501

        The price for a single unit of this product.  # noqa: E501

        :return: The unit_price of this LineItem.  # noqa: E501
        :rtype: float

### `unit_price()`

Sets the unit_price of this LineItem.

        The price for a single unit of this product.  # noqa: E501

        :param unit_price: The unit_price of this LineItem.  # noqa: E501
        :type: float

### `total_price()`

Gets the total_price of this LineItem.  # noqa: E501

        Price of ordered quantity of the product.  # noqa: E501

        :return: The total_price of this LineItem.  # noqa: E501
        :rtype: float

### `total_price()`

Sets the total_price of this LineItem.

        Price of ordered quantity of the product.  # noqa: E501

        :param total_price: The total_price of this LineItem.  # noqa: E501
        :type: float

### `quantity_backorder()`

Gets the quantity_backorder of this LineItem.  # noqa: E501

        The quantity on backorder  # noqa: E501

        :return: The quantity_backorder of this LineItem.  # noqa: E501
        :rtype: int

### `quantity_backorder()`

Sets the quantity_backorder of this LineItem.

        The quantity on backorder  # noqa: E501

        :param quantity_backorder: The quantity_backorder of this LineItem.  # noqa: E501
        :type: int

### `back_order_details()`

Gets the back_order_details of this LineItem.  # noqa: E501


        :return: The back_order_details of this LineItem.  # noqa: E501
        :rtype: BackOrderDetails

### `back_order_details()`

Sets the back_order_details of this LineItem.


        :param back_order_details: The back_order_details of this LineItem.  # noqa: E501
        :type: BackOrderDetails

### `quantity_shipped()`

Gets the quantity_shipped of this LineItem.  # noqa: E501

        The quantity shipped  # noqa: E501

        :return: The quantity_shipped of this LineItem.  # noqa: E501
        :rtype: int

### `quantity_shipped()`

Sets the quantity_shipped of this LineItem.

        The quantity shipped  # noqa: E501

        :param quantity_shipped: The quantity_shipped of this LineItem.  # noqa: E501
        :type: int

### `invoice_id()`

Gets the invoice_id of this LineItem.  # noqa: E501

        The Invoice Id for this shipment  # noqa: E501

        :return: The invoice_id of this LineItem.  # noqa: E501
        :rtype: int

### `invoice_id()`

Sets the invoice_id of this LineItem.

        The Invoice Id for this shipment  # noqa: E501

        :param invoice_id: The invoice_id of this LineItem.  # noqa: E501
        :type: int

### `default_shipping()`

Gets the default_shipping of this LineItem.  # noqa: E501


        :return: The default_shipping of this LineItem.  # noqa: E501
        :rtype: DefaultShipping

### `default_shipping()`

Sets the default_shipping of this LineItem.


        :param default_shipping: The default_shipping of this LineItem.  # noqa: E501
        :type: DefaultShipping

### `schedule()`

Gets the schedule of this LineItem.  # noqa: E501

        The Scheduled shipment  # noqa: E501

        :return: The schedule of this LineItem.  # noqa: E501
        :rtype: list[Schedule]

### `schedule()`

Sets the schedule of this LineItem.

        The Scheduled shipment  # noqa: E501

        :param schedule: The schedule of this LineItem.  # noqa: E501
        :type: list[Schedule]

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `field()`

Gets the field of this ApiValidationError.  # noqa: E501


        :return: The field of this ApiValidationError.  # noqa: E501
        :rtype: str

### `field()`

Sets the field of this ApiValidationError.


        :param field: The field of this ApiValidationError.  # noqa: E501
        :type: str

### `message()`

Gets the message of this ApiValidationError.  # noqa: E501


        :return: The message of this ApiValidationError.  # noqa: E501
        :rtype: str

### `message()`

Sets the message of this ApiValidationError.


        :param message: The message of this ApiValidationError.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `company()`

Gets the company of this Address.  # noqa: E501

        Company or Organization name  # noqa: E501

        :return: The company of this Address.  # noqa: E501
        :rtype: str

### `company()`

Sets the company of this Address.

        Company or Organization name  # noqa: E501

        :param company: The company of this Address.  # noqa: E501
        :type: str

### `first_name()`

Gets the first_name of this Address.  # noqa: E501

        First Name  # noqa: E501

        :return: The first_name of this Address.  # noqa: E501
        :rtype: str

### `first_name()`

Sets the first_name of this Address.

        First Name  # noqa: E501

        :param first_name: The first_name of this Address.  # noqa: E501
        :type: str

### `last_name()`

Gets the last_name of this Address.  # noqa: E501

        Last Name  # noqa: E501

        :return: The last_name of this Address.  # noqa: E501
        :rtype: str

### `last_name()`

Sets the last_name of this Address.

        Last Name  # noqa: E501

        :param last_name: The last_name of this Address.  # noqa: E501
        :type: str

### `address_line_one()`

Gets the address_line_one of this Address.  # noqa: E501

        First line of address  # noqa: E501

        :return: The address_line_one of this Address.  # noqa: E501
        :rtype: str

### `address_line_one()`

Sets the address_line_one of this Address.

        First line of address  # noqa: E501

        :param address_line_one: The address_line_one of this Address.  # noqa: E501
        :type: str

### `address_line_two()`

Gets the address_line_two of this Address.  # noqa: E501

        Second line of address  # noqa: E501

        :return: The address_line_two of this Address.  # noqa: E501
        :rtype: str

### `address_line_two()`

Sets the address_line_two of this Address.

        Second line of address  # noqa: E501

        :param address_line_two: The address_line_two of this Address.  # noqa: E501
        :type: str

### `address_line_three()`

Gets the address_line_three of this Address.  # noqa: E501

        Third line of address  # noqa: E501

        :return: The address_line_three of this Address.  # noqa: E501
        :rtype: str

### `address_line_three()`

Sets the address_line_three of this Address.

        Third line of address  # noqa: E501

        :param address_line_three: The address_line_three of this Address.  # noqa: E501
        :type: str

### `city()`

Gets the city of this Address.  # noqa: E501

        City  # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str

### `city()`

Sets the city of this Address.

        City  # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type: str

### `province()`

Gets the province of this Address.  # noqa: E501

        Province or State  # noqa: E501

        :return: The province of this Address.  # noqa: E501
        :rtype: str

### `province()`

Sets the province of this Address.

        Province or State  # noqa: E501

        :param province: The province of this Address.  # noqa: E501
        :type: str

### `postal_code()`

Gets the postal_code of this Address.  # noqa: E501

        Postal Code or Zip Code  # noqa: E501

        :return: The postal_code of this Address.  # noqa: E501
        :rtype: str

### `postal_code()`

Sets the postal_code of this Address.

        Postal Code or Zip Code  # noqa: E501

        :param postal_code: The postal_code of this Address.  # noqa: E501
        :type: str

### `country()`

Gets the country of this Address.  # noqa: E501

        Country 2 digit ISO code  # noqa: E501

        :return: The country of this Address.  # noqa: E501
        :rtype: str

### `country()`

Sets the country of this Address.

        Country 2 digit ISO code  # noqa: E501

        :param country: The country of this Address.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `error_response_version()`

Gets the error_response_version of this ApiErrorResponse.  # noqa: E501


        :return: The error_response_version of this ApiErrorResponse.  # noqa: E501
        :rtype: str

### `error_response_version()`

Sets the error_response_version of this ApiErrorResponse.


        :param error_response_version: The error_response_version of this ApiErrorResponse.  # noqa: E501
        :type: str

### `status_code()`

Gets the status_code of this ApiErrorResponse.  # noqa: E501


        :return: The status_code of this ApiErrorResponse.  # noqa: E501
        :rtype: int

### `status_code()`

Sets the status_code of this ApiErrorResponse.


        :param status_code: The status_code of this ApiErrorResponse.  # noqa: E501
        :type: int

### `error_message()`

Gets the error_message of this ApiErrorResponse.  # noqa: E501


        :return: The error_message of this ApiErrorResponse.  # noqa: E501
        :rtype: str

### `error_message()`

Sets the error_message of this ApiErrorResponse.


        :param error_message: The error_message of this ApiErrorResponse.  # noqa: E501
        :type: str

### `error_details()`

Gets the error_details of this ApiErrorResponse.  # noqa: E501


        :return: The error_details of this ApiErrorResponse.  # noqa: E501
        :rtype: str

### `error_details()`

Sets the error_details of this ApiErrorResponse.


        :param error_details: The error_details of this ApiErrorResponse.  # noqa: E501
        :type: str

### `request_id()`

Gets the request_id of this ApiErrorResponse.  # noqa: E501


        :return: The request_id of this ApiErrorResponse.  # noqa: E501
        :rtype: str

### `request_id()`

Sets the request_id of this ApiErrorResponse.


        :param request_id: The request_id of this ApiErrorResponse.  # noqa: E501
        :type: str

### `validation_errors()`

Gets the validation_errors of this ApiErrorResponse.  # noqa: E501


        :return: The validation_errors of this ApiErrorResponse.  # noqa: E501
        :rtype: list[ApiValidationError]

### `validation_errors()`

Sets the validation_errors of this ApiErrorResponse.


        :param validation_errors: The validation_errors of this ApiErrorResponse.  # noqa: E501
        :type: list[ApiValidationError]

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `salesorder_id()`

Gets the salesorder_id of this OrderStatusResponse.  # noqa: E501

        Id for this order  # noqa: E501

        :return: The salesorder_id of this OrderStatusResponse.  # noqa: E501
        :rtype: int

### `salesorder_id()`

Sets the salesorder_id of this OrderStatusResponse.

        Id for this order  # noqa: E501

        :param salesorder_id: The salesorder_id of this OrderStatusResponse.  # noqa: E501
        :type: int

### `customer_id()`

Gets the customer_id of this OrderStatusResponse.  # noqa: E501

        Your Digi-Key customer Id  # noqa: E501

        :return: The customer_id of this OrderStatusResponse.  # noqa: E501
        :rtype: int

### `customer_id()`

Sets the customer_id of this OrderStatusResponse.

        Your Digi-Key customer Id  # noqa: E501

        :param customer_id: The customer_id of this OrderStatusResponse.  # noqa: E501
        :type: int

### `billing_account()`

Gets the billing_account of this OrderStatusResponse.  # noqa: E501

        Net Terms billing account number used for the order.  # noqa: E501

        :return: The billing_account of this OrderStatusResponse.  # noqa: E501
        :rtype: int

### `billing_account()`

Sets the billing_account of this OrderStatusResponse.

        Net Terms billing account number used for the order.  # noqa: E501

        :param billing_account: The billing_account of this OrderStatusResponse.  # noqa: E501
        :type: int

### `email()`

Gets the email of this OrderStatusResponse.  # noqa: E501

        Email Address  # noqa: E501

        :return: The email of this OrderStatusResponse.  # noqa: E501
        :rtype: str

### `email()`

Sets the email of this OrderStatusResponse.

        Email Address  # noqa: E501

        :param email: The email of this OrderStatusResponse.  # noqa: E501
        :type: str

### `purchase_order()`

Gets the purchase_order of this OrderStatusResponse.  # noqa: E501

        Freeform purchase order  # noqa: E501

        :return: The purchase_order of this OrderStatusResponse.  # noqa: E501
        :rtype: str

### `purchase_order()`

Sets the purchase_order of this OrderStatusResponse.

        Freeform purchase order  # noqa: E501

        :param purchase_order: The purchase_order of this OrderStatusResponse.  # noqa: E501
        :type: str

### `payment_method()`

Gets the payment_method of this OrderStatusResponse.  # noqa: E501

        Payment method for the order  # noqa: E501

        :return: The payment_method of this OrderStatusResponse.  # noqa: E501
        :rtype: str

### `payment_method()`

Sets the payment_method of this OrderStatusResponse.

        Payment method for the order  # noqa: E501

        :param payment_method: The payment_method of this OrderStatusResponse.  # noqa: E501
        :type: str

### `supplier()`

Gets the supplier of this OrderStatusResponse.  # noqa: E501

        Shipped by  # noqa: E501

        :return: The supplier of this OrderStatusResponse.  # noqa: E501
        :rtype: str

### `supplier()`

Sets the supplier of this OrderStatusResponse.

        Shipped by  # noqa: E501

        :param supplier: The supplier of this OrderStatusResponse.  # noqa: E501
        :type: str

### `shipping_method()`

Gets the shipping_method of this OrderStatusResponse.  # noqa: E501

        Shipping method requested  # noqa: E501

        :return: The shipping_method of this OrderStatusResponse.  # noqa: E501
        :rtype: str

### `shipping_method()`

Sets the shipping_method of this OrderStatusResponse.

        Shipping method requested  # noqa: E501

        :param shipping_method: The shipping_method of this OrderStatusResponse.  # noqa: E501
        :type: str

### `backorder_shipping_method()`

Gets the backorder_shipping_method of this OrderStatusResponse.  # noqa: E501

        Backorder shipping method requested  # noqa: E501

        :return: The backorder_shipping_method of this OrderStatusResponse.  # noqa: E501
        :rtype: str

### `backorder_shipping_method()`

Sets the backorder_shipping_method of this OrderStatusResponse.

        Backorder shipping method requested  # noqa: E501

        :param backorder_shipping_method: The backorder_shipping_method of this OrderStatusResponse.  # noqa: E501
        :type: str

### `shipper_account_number()`

Gets the shipper_account_number of this OrderStatusResponse.  # noqa: E501

        Account number with the shipper  # noqa: E501

        :return: The shipper_account_number of this OrderStatusResponse.  # noqa: E501
        :rtype: str

### `shipper_account_number()`

Sets the shipper_account_number of this OrderStatusResponse.

        Account number with the shipper  # noqa: E501

        :param shipper_account_number: The shipper_account_number of this OrderStatusResponse.  # noqa: E501
        :type: str

### `backorder_shipper_account_number()`

Gets the backorder_shipper_account_number of this OrderStatusResponse.  # noqa: E501

        Account number with the backorder shipper  # noqa: E501

        :return: The backorder_shipper_account_number of this OrderStatusResponse.  # noqa: E501
        :rtype: str

### `backorder_shipper_account_number()`

Sets the backorder_shipper_account_number of this OrderStatusResponse.

        Account number with the backorder shipper  # noqa: E501

        :param backorder_shipper_account_number: The backorder_shipper_account_number of this OrderStatusResponse.  # noqa: E501
        :type: str

### `shipment_type()`

Gets the shipment_type of this OrderStatusResponse.  # noqa: E501

        Can be Immediate, Double or Single. If Immediate, all items will ship as available. If Double, all items immediately available will ship, and other items will be held untill all are available. If Single, entire order is held untill all items are available.  # noqa: E501

        :return: The shipment_type of this OrderStatusResponse.  # noqa: E501
        :rtype: str

### `shipment_type()`

Sets the shipment_type of this OrderStatusResponse.

        Can be Immediate, Double or Single. If Immediate, all items will ship as available. If Double, all items immediately available will ship, and other items will be held untill all are available. If Single, entire order is held untill all items are available.  # noqa: E501

        :param shipment_type: The shipment_type of this OrderStatusResponse.  # noqa: E501
        :type: str

### `currency()`

Gets the currency of this OrderStatusResponse.  # noqa: E501

        ISO code for currency used in the order.  # noqa: E501

        :return: The currency of this OrderStatusResponse.  # noqa: E501
        :rtype: str

### `currency()`

Sets the currency of this OrderStatusResponse.

        ISO code for currency used in the order.  # noqa: E501

        :param currency: The currency of this OrderStatusResponse.  # noqa: E501
        :type: str

### `shipping_address()`

Gets the shipping_address of this OrderStatusResponse.  # noqa: E501


        :return: The shipping_address of this OrderStatusResponse.  # noqa: E501
        :rtype: Address

### `shipping_address()`

Sets the shipping_address of this OrderStatusResponse.


        :param shipping_address: The shipping_address of this OrderStatusResponse.  # noqa: E501
        :type: Address

### `billing_address()`

Gets the billing_address of this OrderStatusResponse.  # noqa: E501


        :return: The billing_address of this OrderStatusResponse.  # noqa: E501
        :rtype: Address

### `billing_address()`

Sets the billing_address of this OrderStatusResponse.


        :param billing_address: The billing_address of this OrderStatusResponse.  # noqa: E501
        :type: Address

### `shipping_details()`

Gets the shipping_details of this OrderStatusResponse.  # noqa: E501

        List of shipping details  # noqa: E501

        :return: The shipping_details of this OrderStatusResponse.  # noqa: E501
        :rtype: list[ShippingDetail]

### `shipping_details()`

Sets the shipping_details of this OrderStatusResponse.

        List of shipping details  # noqa: E501

        :param shipping_details: The shipping_details of this OrderStatusResponse.  # noqa: E501
        :type: list[ShippingDetail]

### `line_items()`

Gets the line_items of this OrderStatusResponse.  # noqa: E501

        List of line items  # noqa: E501

        :return: The line_items of this OrderStatusResponse.  # noqa: E501
        :rtype: list[LineItem]

### `line_items()`

Sets the line_items of this OrderStatusResponse.

        List of line items  # noqa: E501

        :param line_items: The line_items of this OrderStatusResponse.  # noqa: E501
        :type: list[LineItem]

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `carrier()`

Gets the carrier of this ShippingDetail.  # noqa: E501

        Name of the carrier  # noqa: E501

        :return: The carrier of this ShippingDetail.  # noqa: E501
        :rtype: str

### `carrier()`

Sets the carrier of this ShippingDetail.

        Name of the carrier  # noqa: E501

        :param carrier: The carrier of this ShippingDetail.  # noqa: E501
        :type: str

### `carrier_package_id()`

Gets the carrier_package_id of this ShippingDetail.  # noqa: E501

        Id assigned by the carrier  # noqa: E501

        :return: The carrier_package_id of this ShippingDetail.  # noqa: E501
        :rtype: str

### `carrier_package_id()`

Sets the carrier_package_id of this ShippingDetail.

        Id assigned by the carrier  # noqa: E501

        :param carrier_package_id: The carrier_package_id of this ShippingDetail.  # noqa: E501
        :type: str

### `date_transaction()`

Gets the date_transaction of this ShippingDetail.  # noqa: E501

        Date that tracking number was generated in ISO 8601 format  # noqa: E501

        :return: The date_transaction of this ShippingDetail.  # noqa: E501
        :rtype: str

### `date_transaction()`

Sets the date_transaction of this ShippingDetail.

        Date that tracking number was generated in ISO 8601 format  # noqa: E501

        :param date_transaction: The date_transaction of this ShippingDetail.  # noqa: E501
        :type: str

### `shipping_method()`

Gets the shipping_method of this ShippingDetail.  # noqa: E501

        Shipping method used by this shipment  # noqa: E501

        :return: The shipping_method of this ShippingDetail.  # noqa: E501
        :rtype: str

### `shipping_method()`

Sets the shipping_method of this ShippingDetail.

        Shipping method used by this shipment  # noqa: E501

        :param shipping_method: The shipping_method of this ShippingDetail.  # noqa: E501
        :type: str

### `tracking_url()`

Gets the tracking_url of this ShippingDetail.  # noqa: E501


        :return: The tracking_url of this ShippingDetail.  # noqa: E501
        :rtype: str

### `tracking_url()`

Sets the tracking_url of this ShippingDetail.


        :param tracking_url: The tracking_url of this ShippingDetail.  # noqa: E501
        :type: str

### `invoice_id()`

Gets the invoice_id of this ShippingDetail.  # noqa: E501

        The Invoice Id for this shipment  # noqa: E501

        :return: The invoice_id of this ShippingDetail.  # noqa: E501
        :rtype: int

### `invoice_id()`

Sets the invoice_id of this ShippingDetail.

        The Invoice Id for this shipment  # noqa: E501

        :param invoice_id: The invoice_id of this ShippingDetail.  # noqa: E501
        :type: int

### `canceled_or_voided()`

Gets the canceled_or_voided of this ShippingDetail.  # noqa: E501

        Whether this individual detail has been canceled or voided.  # noqa: E501

        :return: The canceled_or_voided of this ShippingDetail.  # noqa: E501
        :rtype: bool

### `canceled_or_voided()`

Sets the canceled_or_voided of this ShippingDetail.

        Whether this individual detail has been canceled or voided.  # noqa: E501

        :param canceled_or_voided: The canceled_or_voided of this ShippingDetail.  # noqa: E501
        :type: bool

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `digi_key_release_date()`

Gets the digi_key_release_date of this DefaultShipping.  # noqa: E501

        Default shipping date  # noqa: E501

        :return: The digi_key_release_date of this DefaultShipping.  # noqa: E501
        :rtype: str

### `digi_key_release_date()`

Sets the digi_key_release_date of this DefaultShipping.

        Default shipping date  # noqa: E501

        :param digi_key_release_date: The digi_key_release_date of this DefaultShipping.  # noqa: E501
        :type: str

### `estimated_in_house_date()`

Gets the estimated_in_house_date of this DefaultShipping.  # noqa: E501

        The estimated date the product will  # noqa: E501

        :return: The estimated_in_house_date of this DefaultShipping.  # noqa: E501
        :rtype: str

### `estimated_in_house_date()`

Sets the estimated_in_house_date of this DefaultShipping.

        The estimated date the product will  # noqa: E501

        :param estimated_in_house_date: The estimated_in_house_date of this DefaultShipping.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `salesorder_id()`

Gets the salesorder_id of this SalesOrderHistoryItem.  # noqa: E501

        The SalesOrder Id. You can use this Id to look up details on the order.  # noqa: E501

        :return: The salesorder_id of this SalesOrderHistoryItem.  # noqa: E501
        :rtype: int

### `salesorder_id()`

Sets the salesorder_id of this SalesOrderHistoryItem.

        The SalesOrder Id. You can use this Id to look up details on the order.  # noqa: E501

        :param salesorder_id: The salesorder_id of this SalesOrderHistoryItem.  # noqa: E501
        :type: int

### `customer_id()`

Gets the customer_id of this SalesOrderHistoryItem.  # noqa: E501

        The CustomerId associated with the SalesOrder  # noqa: E501

        :return: The customer_id of this SalesOrderHistoryItem.  # noqa: E501
        :rtype: int

### `customer_id()`

Sets the customer_id of this SalesOrderHistoryItem.

        The CustomerId associated with the SalesOrder  # noqa: E501

        :param customer_id: The customer_id of this SalesOrderHistoryItem.  # noqa: E501
        :type: int

### `date_entered()`

Gets the date_entered of this SalesOrderHistoryItem.  # noqa: E501

        Date in which the order was entered in ISO 8601 format.  # noqa: E501

        :return: The date_entered of this SalesOrderHistoryItem.  # noqa: E501
        :rtype: str

### `date_entered()`

Sets the date_entered of this SalesOrderHistoryItem.

        Date in which the order was entered in ISO 8601 format.  # noqa: E501

        :param date_entered: The date_entered of this SalesOrderHistoryItem.  # noqa: E501
        :type: str

### `purchase_order()`

Gets the purchase_order of this SalesOrderHistoryItem.  # noqa: E501

        Purchase order if available  # noqa: E501

        :return: The purchase_order of this SalesOrderHistoryItem.  # noqa: E501
        :rtype: str

### `purchase_order()`

Sets the purchase_order of this SalesOrderHistoryItem.

        Purchase order if available  # noqa: E501

        :param purchase_order: The purchase_order of this SalesOrderHistoryItem.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `salesorder_id()`

Gets the salesorder_id of this SalesorderHistoryItem.  # noqa: E501

        The Salesorder Id. You can use this Id to look up details on the order.  # noqa: E501

        :return: The salesorder_id of this SalesorderHistoryItem.  # noqa: E501
        :rtype: int

### `salesorder_id()`

Sets the salesorder_id of this SalesorderHistoryItem.

        The Salesorder Id. You can use this Id to look up details on the order.  # noqa: E501

        :param salesorder_id: The salesorder_id of this SalesorderHistoryItem.  # noqa: E501
        :type: int

### `customer_id()`

Gets the customer_id of this SalesorderHistoryItem.  # noqa: E501

        The CustomerId associated with the Salesorder  # noqa: E501

        :return: The customer_id of this SalesorderHistoryItem.  # noqa: E501
        :rtype: int

### `customer_id()`

Sets the customer_id of this SalesorderHistoryItem.

        The CustomerId associated with the Salesorder  # noqa: E501

        :param customer_id: The customer_id of this SalesorderHistoryItem.  # noqa: E501
        :type: int

### `date_entered()`

Gets the date_entered of this SalesorderHistoryItem.  # noqa: E501

        Date in which the order was entered in ISO 8601 format.  # noqa: E501

        :return: The date_entered of this SalesorderHistoryItem.  # noqa: E501
        :rtype: str

### `date_entered()`

Sets the date_entered of this SalesorderHistoryItem.

        Date in which the order was entered in ISO 8601 format.  # noqa: E501

        :param date_entered: The date_entered of this SalesorderHistoryItem.  # noqa: E501
        :type: str

### `purchase_order()`

Gets the purchase_order of this SalesorderHistoryItem.  # noqa: E501

        Purchase order if available  # noqa: E501

        :return: The purchase_order of this SalesorderHistoryItem.  # noqa: E501
        :rtype: str

### `purchase_order()`

Sets the purchase_order of this SalesorderHistoryItem.

        Purchase order if available  # noqa: E501

        :param purchase_order: The purchase_order of this SalesorderHistoryItem.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `scheduled_quantity()`

Gets the scheduled_quantity of this Schedule.  # noqa: E501

        The total quantity for the schedule.  # noqa: E501

        :return: The scheduled_quantity of this Schedule.  # noqa: E501
        :rtype: int

### `scheduled_quantity()`

Sets the scheduled_quantity of this Schedule.

        The total quantity for the schedule.  # noqa: E501

        :param scheduled_quantity: The scheduled_quantity of this Schedule.  # noqa: E501
        :type: int

### `scheduled_date()`

Gets the scheduled_date of this Schedule.  # noqa: E501

        The Date of the Schedule ISO 8601 format  # noqa: E501

        :return: The scheduled_date of this Schedule.  # noqa: E501
        :rtype: str

### `scheduled_date()`

Sets the scheduled_date of this Schedule.

        The Date of the Schedule ISO 8601 format  # noqa: E501

        :param scheduled_date: The scheduled_date of this Schedule.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `quantity()`

Gets the quantity of this BackOrderDetails.  # noqa: E501

        The total quantity that is backorder. This quantity is the same as LinteItem.QuantityBackorder  # noqa: E501

        :return: The quantity of this BackOrderDetails.  # noqa: E501
        :rtype: int

### `quantity()`

Sets the quantity of this BackOrderDetails.

        The total quantity that is backorder. This quantity is the same as LinteItem.QuantityBackorder  # noqa: E501

        :param quantity: The quantity of this BackOrderDetails.  # noqa: E501
        :type: int

### `back_order_estimates()`

Gets the back_order_estimates of this BackOrderDetails.  # noqa: E501

        The Manufacturer's estimated date and quantity that Digi-Key will receive the product.  # noqa: E501

        :return: The back_order_estimates of this BackOrderDetails.  # noqa: E501
        :rtype: list[Schedule]

### `back_order_estimates()`

Sets the back_order_estimates of this BackOrderDetails.

        The Manufacturer's estimated date and quantity that Digi-Key will receive the product.  # noqa: E501

        :param back_order_estimates: The back_order_estimates of this BackOrderDetails.  # noqa: E501
        :type: list[Schedule]

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `field()`

Gets the field of this ApiValidationError.  # noqa: E501


        :return: The field of this ApiValidationError.  # noqa: E501
        :rtype: str

### `field()`

Sets the field of this ApiValidationError.


        :param field: The field of this ApiValidationError.  # noqa: E501
        :type: str

### `message()`

Gets the message of this ApiValidationError.  # noqa: E501


        :return: The message of this ApiValidationError.  # noqa: E501
        :rtype: str

### `message()`

Sets the message of this ApiValidationError.


        :param message: The message of this ApiValidationError.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `children()`

Gets the children of this LimitedTaxonomy.  # noqa: E501

        List of taxonomies contained within this taxonomy.  # noqa: E501

        :return: The children of this LimitedTaxonomy.  # noqa: E501
        :rtype: list[LimitedTaxonomy]

### `children()`

Sets the children of this LimitedTaxonomy.

        List of taxonomies contained within this taxonomy.  # noqa: E501

        :param children: The children of this LimitedTaxonomy.  # noqa: E501
        :type: list[LimitedTaxonomy]

### `product_count()`

Gets the product_count of this LimitedTaxonomy.  # noqa: E501

        The number of products contained within this taxonomy.  # noqa: E501

        :return: The product_count of this LimitedTaxonomy.  # noqa: E501
        :rtype: int

### `product_count()`

Sets the product_count of this LimitedTaxonomy.

        The number of products contained within this taxonomy.  # noqa: E501

        :param product_count: The product_count of this LimitedTaxonomy.  # noqa: E501
        :type: int

### `new_product_count()`

Gets the new_product_count of this LimitedTaxonomy.  # noqa: E501

        The number of new products contained within this taxonomy.  # noqa: E501

        :return: The new_product_count of this LimitedTaxonomy.  # noqa: E501
        :rtype: int

### `new_product_count()`

Sets the new_product_count of this LimitedTaxonomy.

        The number of new products contained within this taxonomy.  # noqa: E501

        :param new_product_count: The new_product_count of this LimitedTaxonomy.  # noqa: E501
        :type: int

### `parameter_id()`

Gets the parameter_id of this LimitedTaxonomy.  # noqa: E501

        The Id of the parameter.  # noqa: E501

        :return: The parameter_id of this LimitedTaxonomy.  # noqa: E501
        :rtype: int

### `parameter_id()`

Sets the parameter_id of this LimitedTaxonomy.

        The Id of the parameter.  # noqa: E501

        :param parameter_id: The parameter_id of this LimitedTaxonomy.  # noqa: E501
        :type: int

### `value_id()`

Gets the value_id of this LimitedTaxonomy.  # noqa: E501

        The Id of the value.  # noqa: E501

        :return: The value_id of this LimitedTaxonomy.  # noqa: E501
        :rtype: str

### `value_id()`

Sets the value_id of this LimitedTaxonomy.

        The Id of the value.  # noqa: E501

        :param value_id: The value_id of this LimitedTaxonomy.  # noqa: E501
        :type: str

### `parameter()`

Gets the parameter of this LimitedTaxonomy.  # noqa: E501

        The name of the parameter.  # noqa: E501

        :return: The parameter of this LimitedTaxonomy.  # noqa: E501
        :rtype: str

### `parameter()`

Sets the parameter of this LimitedTaxonomy.

        The name of the parameter.  # noqa: E501

        :param parameter: The parameter of this LimitedTaxonomy.  # noqa: E501
        :type: str

### `value()`

Gets the value of this LimitedTaxonomy.  # noqa: E501

        The name of the value.  # noqa: E501

        :return: The value of this LimitedTaxonomy.  # noqa: E501
        :rtype: str

### `value()`

Sets the value of this LimitedTaxonomy.

        The name of the value.  # noqa: E501

        :param value: The value of this LimitedTaxonomy.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `error_response_version()`

Gets the error_response_version of this ApiErrorResponse.  # noqa: E501


        :return: The error_response_version of this ApiErrorResponse.  # noqa: E501
        :rtype: str

### `error_response_version()`

Sets the error_response_version of this ApiErrorResponse.


        :param error_response_version: The error_response_version of this ApiErrorResponse.  # noqa: E501
        :type: str

### `status_code()`

Gets the status_code of this ApiErrorResponse.  # noqa: E501


        :return: The status_code of this ApiErrorResponse.  # noqa: E501
        :rtype: int

### `status_code()`

Sets the status_code of this ApiErrorResponse.


        :param status_code: The status_code of this ApiErrorResponse.  # noqa: E501
        :type: int

### `error_message()`

Gets the error_message of this ApiErrorResponse.  # noqa: E501


        :return: The error_message of this ApiErrorResponse.  # noqa: E501
        :rtype: str

### `error_message()`

Sets the error_message of this ApiErrorResponse.


        :param error_message: The error_message of this ApiErrorResponse.  # noqa: E501
        :type: str

### `error_details()`

Gets the error_details of this ApiErrorResponse.  # noqa: E501


        :return: The error_details of this ApiErrorResponse.  # noqa: E501
        :rtype: str

### `error_details()`

Sets the error_details of this ApiErrorResponse.


        :param error_details: The error_details of this ApiErrorResponse.  # noqa: E501
        :type: str

### `request_id()`

Gets the request_id of this ApiErrorResponse.  # noqa: E501


        :return: The request_id of this ApiErrorResponse.  # noqa: E501
        :rtype: str

### `request_id()`

Sets the request_id of this ApiErrorResponse.


        :param request_id: The request_id of this ApiErrorResponse.  # noqa: E501
        :type: str

### `validation_errors()`

Gets the validation_errors of this ApiErrorResponse.  # noqa: E501


        :return: The validation_errors of this ApiErrorResponse.  # noqa: E501
        :rtype: list[ApiValidationError]

### `validation_errors()`

Sets the validation_errors of this ApiErrorResponse.


        :param validation_errors: The validation_errors of this ApiErrorResponse.  # noqa: E501
        :type: list[ApiValidationError]

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `products()`

Gets the products of this BatchProductDetailsRequest.  # noqa: E501

          # noqa: E501

        :return: The products of this BatchProductDetailsRequest.  # noqa: E501
        :rtype: list[str]

### `products()`

Sets the products of this BatchProductDetailsRequest.

          # noqa: E501

        :param products: The products of this BatchProductDetailsRequest.  # noqa: E501
        :type: list[str]

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `site()`

Gets the site of this IsoSearchLocale.  # noqa: E501

        The site used for the API call.  # noqa: E501

        :return: The site of this IsoSearchLocale.  # noqa: E501
        :rtype: str

### `site()`

Sets the site of this IsoSearchLocale.

        The site used for the API call.  # noqa: E501

        :param site: The site of this IsoSearchLocale.  # noqa: E501
        :type: str

### `language()`

Gets the language of this IsoSearchLocale.  # noqa: E501

        The language used for the API call. If the provided language is not valid for the site, it will be set to the site default.  # noqa: E501

        :return: The language of this IsoSearchLocale.  # noqa: E501
        :rtype: str

### `language()`

Sets the language of this IsoSearchLocale.

        The language used for the API call. If the provided language is not valid for the site, it will be set to the site default.  # noqa: E501

        :param language: The language of this IsoSearchLocale.  # noqa: E501
        :type: str

### `currency()`

Gets the currency of this IsoSearchLocale.  # noqa: E501

        The currency used for the API call. If the provided currency is not valid for the site, it will be set to the site default.  # noqa: E501

        :return: The currency of this IsoSearchLocale.  # noqa: E501
        :rtype: str

### `currency()`

Sets the currency of this IsoSearchLocale.

        The currency used for the API call. If the provided currency is not valid for the site, it will be set to the site default.  # noqa: E501

        :param currency: The currency of this IsoSearchLocale.  # noqa: E501
        :type: str

### `ship_to_country()`

Gets the ship_to_country of this IsoSearchLocale.  # noqa: E501

        The destination for shipping the product. This is used for tariffs and regional pricing.  # noqa: E501

        :return: The ship_to_country of this IsoSearchLocale.  # noqa: E501
        :rtype: str

### `ship_to_country()`

Sets the ship_to_country of this IsoSearchLocale.

        The destination for shipping the product. This is used for tariffs and regional pricing.  # noqa: E501

        :param ship_to_country: The ship_to_country of this IsoSearchLocale.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `parameter_id()`

Gets the parameter_id of this PidVid.  # noqa: E501

        The Id of the parameter.  # noqa: E501

        :return: The parameter_id of this PidVid.  # noqa: E501
        :rtype: int

### `parameter_id()`

Sets the parameter_id of this PidVid.

        The Id of the parameter.  # noqa: E501

        :param parameter_id: The parameter_id of this PidVid.  # noqa: E501
        :type: int

### `value_id()`

Gets the value_id of this PidVid.  # noqa: E501

        The Id of the value.  # noqa: E501

        :return: The value_id of this PidVid.  # noqa: E501
        :rtype: str

### `value_id()`

Sets the value_id of this PidVid.

        The Id of the value.  # noqa: E501

        :param value_id: The value_id of this PidVid.  # noqa: E501
        :type: str

### `parameter()`

Gets the parameter of this PidVid.  # noqa: E501

        The name of the parameter.  # noqa: E501

        :return: The parameter of this PidVid.  # noqa: E501
        :rtype: str

### `parameter()`

Sets the parameter of this PidVid.

        The name of the parameter.  # noqa: E501

        :param parameter: The parameter of this PidVid.  # noqa: E501
        :type: str

### `value()`

Gets the value of this PidVid.  # noqa: E501

        The name of the value.  # noqa: E501

        :return: The value of this PidVid.  # noqa: E501
        :rtype: str

### `value()`

Sets the value of this PidVid.

        The name of the value.  # noqa: E501

        :param value: The value of this PidVid.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `my_pricing()`

Gets the my_pricing of this ProductDetails.  # noqa: E501

        Your pricing for the account with which you authenticated. Also dependent on locale information.  # noqa: E501

        :return: The my_pricing of this ProductDetails.  # noqa: E501
        :rtype: list[PriceBreak]

### `my_pricing()`

Sets the my_pricing of this ProductDetails.

        Your pricing for the account with which you authenticated. Also dependent on locale information.  # noqa: E501

        :param my_pricing: The my_pricing of this ProductDetails.  # noqa: E501
        :type: list[PriceBreak]

### `obsolete()`

Gets the obsolete of this ProductDetails.  # noqa: E501

        Indicates whether this Part is obsolete.  # noqa: E501

        :return: The obsolete of this ProductDetails.  # noqa: E501
        :rtype: bool

### `obsolete()`

Sets the obsolete of this ProductDetails.

        Indicates whether this Part is obsolete.  # noqa: E501

        :param obsolete: The obsolete of this ProductDetails.  # noqa: E501
        :type: bool

### `media_links()`

Gets the media_links of this ProductDetails.  # noqa: E501

        Collection of MediaLinks objects. These can contain links to datasheets, photos or manuals.  # noqa: E501

        :return: The media_links of this ProductDetails.  # noqa: E501
        :rtype: list[MediaLinks]

### `media_links()`

Sets the media_links of this ProductDetails.

        Collection of MediaLinks objects. These can contain links to datasheets, photos or manuals.  # noqa: E501

        :param media_links: The media_links of this ProductDetails.  # noqa: E501
        :type: list[MediaLinks]

### `standard_package()`

Gets the standard_package of this ProductDetails.  # noqa: E501

        The number of products in the manufacturer's standard package.  # noqa: E501

        :return: The standard_package of this ProductDetails.  # noqa: E501
        :rtype: int

### `standard_package()`

Sets the standard_package of this ProductDetails.

        The number of products in the manufacturer's standard package.  # noqa: E501

        :param standard_package: The standard_package of this ProductDetails.  # noqa: E501
        :type: int

### `limited_taxonomy()`

Gets the limited_taxonomy of this ProductDetails.  # noqa: E501


        :return: The limited_taxonomy of this ProductDetails.  # noqa: E501
        :rtype: LimitedTaxonomy

### `limited_taxonomy()`

Sets the limited_taxonomy of this ProductDetails.


        :param limited_taxonomy: The limited_taxonomy of this ProductDetails.  # noqa: E501
        :type: LimitedTaxonomy

### `kits()`

Gets the kits of this ProductDetails.  # noqa: E501

        Kits that this product is contained in.  # noqa: E501

        :return: The kits of this ProductDetails.  # noqa: E501
        :rtype: list[AssociatedProduct]

### `kits()`

Sets the kits of this ProductDetails.

        Kits that this product is contained in.  # noqa: E501

        :param kits: The kits of this ProductDetails.  # noqa: E501
        :type: list[AssociatedProduct]

### `kit_contents()`

Gets the kit_contents of this ProductDetails.  # noqa: E501

        Products contained within this product. Only applicable if this product is a kit.  # noqa: E501

        :return: The kit_contents of this ProductDetails.  # noqa: E501
        :rtype: list[KitPart]

### `kit_contents()`

Sets the kit_contents of this ProductDetails.

        Products contained within this product. Only applicable if this product is a kit.  # noqa: E501

        :param kit_contents: The kit_contents of this ProductDetails.  # noqa: E501
        :type: list[KitPart]

### `mating_products()`

Gets the mating_products of this ProductDetails.  # noqa: E501

        An association of same manufacturer products that mate with each other.  # noqa: E501

        :return: The mating_products of this ProductDetails.  # noqa: E501
        :rtype: list[AssociatedProduct]

### `mating_products()`

Sets the mating_products of this ProductDetails.

        An association of same manufacturer products that mate with each other.  # noqa: E501

        :param mating_products: The mating_products of this ProductDetails.  # noqa: E501
        :type: list[AssociatedProduct]

### `search_locale_used()`

Gets the search_locale_used of this ProductDetails.  # noqa: E501


        :return: The search_locale_used of this ProductDetails.  # noqa: E501
        :rtype: IsoSearchLocale

### `search_locale_used()`

Sets the search_locale_used of this ProductDetails.


        :param search_locale_used: The search_locale_used of this ProductDetails.  # noqa: E501
        :type: IsoSearchLocale

### `associated_products()`

Gets the associated_products of this ProductDetails.  # noqa: E501

        Products that are directly correlated to complete the intended function of the product. These products may be  either same manufacturer or differ.  # noqa: E501

        :return: The associated_products of this ProductDetails.  # noqa: E501
        :rtype: list[AssociatedProduct]

### `associated_products()`

Sets the associated_products of this ProductDetails.

        Products that are directly correlated to complete the intended function of the product. These products may be  either same manufacturer or differ.  # noqa: E501

        :param associated_products: The associated_products of this ProductDetails.  # noqa: E501
        :type: list[AssociatedProduct]

### `for_use_with_products()`

Gets the for_use_with_products of this ProductDetails.  # noqa: E501

        Products that are directly correlated to complete the intended function of the product. These products may be  either same manufacturer or differ.  # noqa: E501

        :return: The for_use_with_products of this ProductDetails.  # noqa: E501
        :rtype: list[AssociatedProduct]

### `for_use_with_products()`

Sets the for_use_with_products of this ProductDetails.

        Products that are directly correlated to complete the intended function of the product. These products may be  either same manufacturer or differ.  # noqa: E501

        :param for_use_with_products: The for_use_with_products of this ProductDetails.  # noqa: E501
        :type: list[AssociatedProduct]

### `rohs_subs()`

Gets the rohs_subs of this ProductDetails.  # noqa: E501

        Rohs substitutions  # noqa: E501

        :return: The rohs_subs of this ProductDetails.  # noqa: E501
        :rtype: list[AssociatedProduct]

### `rohs_subs()`

Sets the rohs_subs of this ProductDetails.

        Rohs substitutions  # noqa: E501

        :param rohs_subs: The rohs_subs of this ProductDetails.  # noqa: E501
        :type: list[AssociatedProduct]

### `suggested_subs()`

Gets the suggested_subs of this ProductDetails.  # noqa: E501

        Suggested substitutions for when the product is obsolete.  # noqa: E501

        :return: The suggested_subs of this ProductDetails.  # noqa: E501
        :rtype: list[AssociatedProduct]

### `suggested_subs()`

Sets the suggested_subs of this ProductDetails.

        Suggested substitutions for when the product is obsolete.  # noqa: E501

        :param suggested_subs: The suggested_subs of this ProductDetails.  # noqa: E501
        :type: list[AssociatedProduct]

### `additional_value_fee()`

Gets the additional_value_fee of this ProductDetails.  # noqa: E501

        Any additional value fee. Most commonly the Digi-Reel fee. May be used for programmable parts as well.  # noqa: E501

        :return: The additional_value_fee of this ProductDetails.  # noqa: E501
        :rtype: float

### `additional_value_fee()`

Sets the additional_value_fee of this ProductDetails.

        Any additional value fee. Most commonly the Digi-Reel fee. May be used for programmable parts as well.  # noqa: E501

        :param additional_value_fee: The additional_value_fee of this ProductDetails.  # noqa: E501
        :type: float

### `standard_pricing()`

Gets the standard_pricing of this ProductDetails.  # noqa: E501

        Standard pricing for the validated locale.  # noqa: E501

        :return: The standard_pricing of this ProductDetails.  # noqa: E501
        :rtype: list[PriceBreak]

### `standard_pricing()`

Sets the standard_pricing of this ProductDetails.

        Standard pricing for the validated locale.  # noqa: E501

        :param standard_pricing: The standard_pricing of this ProductDetails.  # noqa: E501
        :type: list[PriceBreak]

### `ro_hs_status()`

Gets the ro_hs_status of this ProductDetails.  # noqa: E501

        RoHS status. Can be: RoHS Compliant, RoHS non-compliant, RoHS Compliant By Exemption, Not Applicable, Vendor  undefined, Request Inventory Verification, ROHS3 Compliant.  # noqa: E501

        :return: The ro_hs_status of this ProductDetails.  # noqa: E501
        :rtype: str

### `ro_hs_status()`

Sets the ro_hs_status of this ProductDetails.

        RoHS status. Can be: RoHS Compliant, RoHS non-compliant, RoHS Compliant By Exemption, Not Applicable, Vendor  undefined, Request Inventory Verification, ROHS3 Compliant.  # noqa: E501

        :param ro_hs_status: The ro_hs_status of this ProductDetails.  # noqa: E501
        :type: str

### `lead_status()`

Gets the lead_status of this ProductDetails.  # noqa: E501

        Lead status. Can be: Lead Free, Contains lead, Lead Free By Exemption, Not Applicable, Vendor undefined, unknown,  or Request Inventory Verification.  # noqa: E501

        :return: The lead_status of this ProductDetails.  # noqa: E501
        :rtype: str

### `lead_status()`

Sets the lead_status of this ProductDetails.

        Lead status. Can be: Lead Free, Contains lead, Lead Free By Exemption, Not Applicable, Vendor undefined, unknown,  or Request Inventory Verification.  # noqa: E501

        :param lead_status: The lead_status of this ProductDetails.  # noqa: E501
        :type: str

### `parameters()`

Gets the parameters of this ProductDetails.  # noqa: E501

        Parameters for the part. Can be used for filtering keyword searches.  # noqa: E501

        :return: The parameters of this ProductDetails.  # noqa: E501
        :rtype: list[PidVid]

### `parameters()`

Sets the parameters of this ProductDetails.

        Parameters for the part. Can be used for filtering keyword searches.  # noqa: E501

        :param parameters: The parameters of this ProductDetails.  # noqa: E501
        :type: list[PidVid]

### `product_url()`

Gets the product_url of this ProductDetails.  # noqa: E501

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :return: The product_url of this ProductDetails.  # noqa: E501
        :rtype: str

### `product_url()`

Sets the product_url of this ProductDetails.

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :param product_url: The product_url of this ProductDetails.  # noqa: E501
        :type: str

### `primary_datasheet()`

Gets the primary_datasheet of this ProductDetails.  # noqa: E501

        The URL to the product's datasheet.  # noqa: E501

        :return: The primary_datasheet of this ProductDetails.  # noqa: E501
        :rtype: str

### `primary_datasheet()`

Sets the primary_datasheet of this ProductDetails.

        The URL to the product's datasheet.  # noqa: E501

        :param primary_datasheet: The primary_datasheet of this ProductDetails.  # noqa: E501
        :type: str

### `primary_photo()`

Gets the primary_photo of this ProductDetails.  # noqa: E501

        The URL to the product's image.  # noqa: E501

        :return: The primary_photo of this ProductDetails.  # noqa: E501
        :rtype: str

### `primary_photo()`

Sets the primary_photo of this ProductDetails.

        The URL to the product's image.  # noqa: E501

        :param primary_photo: The primary_photo of this ProductDetails.  # noqa: E501
        :type: str

### `primary_video()`

Gets the primary_video of this ProductDetails.  # noqa: E501

        The URL to the product's video.  # noqa: E501

        :return: The primary_video of this ProductDetails.  # noqa: E501
        :rtype: str

### `primary_video()`

Sets the primary_video of this ProductDetails.

        The URL to the product's video.  # noqa: E501

        :param primary_video: The primary_video of this ProductDetails.  # noqa: E501
        :type: str

### `series()`

Gets the series of this ProductDetails.  # noqa: E501


        :return: The series of this ProductDetails.  # noqa: E501
        :rtype: PidVid

### `series()`

Sets the series of this ProductDetails.


        :param series: The series of this ProductDetails.  # noqa: E501
        :type: PidVid

### `manufacturer_lead_weeks()`

Gets the manufacturer_lead_weeks of this ProductDetails.  # noqa: E501

        The number of weeks expected to receive stock from manufacturer.  # noqa: E501

        :return: The manufacturer_lead_weeks of this ProductDetails.  # noqa: E501
        :rtype: str

### `manufacturer_lead_weeks()`

Sets the manufacturer_lead_weeks of this ProductDetails.

        The number of weeks expected to receive stock from manufacturer.  # noqa: E501

        :param manufacturer_lead_weeks: The manufacturer_lead_weeks of this ProductDetails.  # noqa: E501
        :type: str

### `manufacturer_page_url()`

Gets the manufacturer_page_url of this ProductDetails.  # noqa: E501

        The URL to Digi-Key's page on the manufacturer.  # noqa: E501

        :return: The manufacturer_page_url of this ProductDetails.  # noqa: E501
        :rtype: str

### `manufacturer_page_url()`

Sets the manufacturer_page_url of this ProductDetails.

        The URL to Digi-Key's page on the manufacturer.  # noqa: E501

        :param manufacturer_page_url: The manufacturer_page_url of this ProductDetails.  # noqa: E501
        :type: str

### `product_status()`

Gets the product_status of this ProductDetails.  # noqa: E501

        Status of the product. Options include: Active, Obsolete, Discontinued at Digi-Key, Last Time Buy, Not For New  Designs, Preliminary. For obsolete parts the part will become a non-stocking item when stock is depleted; minimums  will apply. Order the quantity available or the quantity available plus a multiple of the minimum order quantity.  # noqa: E501

        :return: The product_status of this ProductDetails.  # noqa: E501
        :rtype: str

### `product_status()`

Sets the product_status of this ProductDetails.

        Status of the product. Options include: Active, Obsolete, Discontinued at Digi-Key, Last Time Buy, Not For New  Designs, Preliminary. For obsolete parts the part will become a non-stocking item when stock is depleted; minimums  will apply. Order the quantity available or the quantity available plus a multiple of the minimum order quantity.  # noqa: E501

        :param product_status: The product_status of this ProductDetails.  # noqa: E501
        :type: str

### `date_last_buy_chance()`

Gets the date_last_buy_chance of this ProductDetails.  # noqa: E501

        Last date that the product will be available for purchase. Date is in ISO 8601.  # noqa: E501

        :return: The date_last_buy_chance of this ProductDetails.  # noqa: E501
        :rtype: datetime

### `date_last_buy_chance()`

Sets the date_last_buy_chance of this ProductDetails.

        Last date that the product will be available for purchase. Date is in ISO 8601.  # noqa: E501

        :param date_last_buy_chance: The date_last_buy_chance of this ProductDetails.  # noqa: E501
        :type: datetime

### `alternate_packaging()`

Gets the alternate_packaging of this ProductDetails.  # noqa: E501

        Other packaging types available for this product.  # noqa: E501

        :return: The alternate_packaging of this ProductDetails.  # noqa: E501
        :rtype: list[BasicProduct]

### `alternate_packaging()`

Sets the alternate_packaging of this ProductDetails.

        Other packaging types available for this product.  # noqa: E501

        :param alternate_packaging: The alternate_packaging of this ProductDetails.  # noqa: E501
        :type: list[BasicProduct]

### `detailed_description()`

Gets the detailed_description of this ProductDetails.  # noqa: E501

        Extended catalog description of the product.  # noqa: E501

        :return: The detailed_description of this ProductDetails.  # noqa: E501
        :rtype: str

### `detailed_description()`

Sets the detailed_description of this ProductDetails.

        Extended catalog description of the product.  # noqa: E501

        :param detailed_description: The detailed_description of this ProductDetails.  # noqa: E501
        :type: str

### `reach_status()`

Gets the reach_status of this ProductDetails.  # noqa: E501

        REACH is a regulation of the European Union. See documentation from the European Chemicals Agency.  # noqa: E501

        :return: The reach_status of this ProductDetails.  # noqa: E501
        :rtype: str

### `reach_status()`

Sets the reach_status of this ProductDetails.

        REACH is a regulation of the European Union. See documentation from the European Chemicals Agency.  # noqa: E501

        :param reach_status: The reach_status of this ProductDetails.  # noqa: E501
        :type: str

### `export_control_class_number()`

Gets the export_control_class_number of this ProductDetails.  # noqa: E501

        Export control class number. See documentation from the U.S. Department of Commerce.  # noqa: E501

        :return: The export_control_class_number of this ProductDetails.  # noqa: E501
        :rtype: str

### `export_control_class_number()`

Sets the export_control_class_number of this ProductDetails.

        Export control class number. See documentation from the U.S. Department of Commerce.  # noqa: E501

        :param export_control_class_number: The export_control_class_number of this ProductDetails.  # noqa: E501
        :type: str

### `htsus_code()`

Gets the htsus_code of this ProductDetails.  # noqa: E501

        Harmonized Tariff Schedule of the United States. See documentation from the U.S. International Trade Commission.  # noqa: E501

        :return: The htsus_code of this ProductDetails.  # noqa: E501
        :rtype: str

### `htsus_code()`

Sets the htsus_code of this ProductDetails.

        Harmonized Tariff Schedule of the United States. See documentation from the U.S. International Trade Commission.  # noqa: E501

        :param htsus_code: The htsus_code of this ProductDetails.  # noqa: E501
        :type: str

### `tariff_description()`

Gets the tariff_description of this ProductDetails.  # noqa: E501

        Description of the tariff status. Only applies if purchasing in USD and shipping to the US. Valid options are No  Tariff and Tariff Applied.  # noqa: E501

        :return: The tariff_description of this ProductDetails.  # noqa: E501
        :rtype: str

### `tariff_description()`

Sets the tariff_description of this ProductDetails.

        Description of the tariff status. Only applies if purchasing in USD and shipping to the US. Valid options are No  Tariff and Tariff Applied.  # noqa: E501

        :param tariff_description: The tariff_description of this ProductDetails.  # noqa: E501
        :type: str

### `moisture_sensitivity_level()`

Gets the moisture_sensitivity_level of this ProductDetails.  # noqa: E501

        Code for Moisture Sensitivity Level of the product  # noqa: E501

        :return: The moisture_sensitivity_level of this ProductDetails.  # noqa: E501
        :rtype: str

### `moisture_sensitivity_level()`

Sets the moisture_sensitivity_level of this ProductDetails.

        Code for Moisture Sensitivity Level of the product  # noqa: E501

        :param moisture_sensitivity_level: The moisture_sensitivity_level of this ProductDetails.  # noqa: E501
        :type: str

### `manufacturer_part_number()`

Gets the manufacturer_part_number of this ProductDetails.  # noqa: E501

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :return: The manufacturer_part_number of this ProductDetails.  # noqa: E501
        :rtype: str

### `manufacturer_part_number()`

Sets the manufacturer_part_number of this ProductDetails.

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :param manufacturer_part_number: The manufacturer_part_number of this ProductDetails.  # noqa: E501
        :type: str

### `minimum_order_quantity()`

Gets the minimum_order_quantity of this ProductDetails.  # noqa: E501

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :return: The minimum_order_quantity of this ProductDetails.  # noqa: E501
        :rtype: int

### `minimum_order_quantity()`

Sets the minimum_order_quantity of this ProductDetails.

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :param minimum_order_quantity: The minimum_order_quantity of this ProductDetails.  # noqa: E501
        :type: int

### `non_stock()`

Gets the non_stock of this ProductDetails.  # noqa: E501

        Indicates this product is a non stock product.  # noqa: E501

        :return: The non_stock of this ProductDetails.  # noqa: E501
        :rtype: bool

### `non_stock()`

Sets the non_stock of this ProductDetails.

        Indicates this product is a non stock product.  # noqa: E501

        :param non_stock: The non_stock of this ProductDetails.  # noqa: E501
        :type: bool

### `packaging()`

Gets the packaging of this ProductDetails.  # noqa: E501


        :return: The packaging of this ProductDetails.  # noqa: E501
        :rtype: PidVid

### `packaging()`

Sets the packaging of this ProductDetails.


        :param packaging: The packaging of this ProductDetails.  # noqa: E501
        :type: PidVid

### `quantity_available()`

Gets the quantity_available of this ProductDetails.  # noqa: E501

        Quantity of the product available for immediate sale.  # noqa: E501

        :return: The quantity_available of this ProductDetails.  # noqa: E501
        :rtype: int

### `quantity_available()`

Sets the quantity_available of this ProductDetails.

        Quantity of the product available for immediate sale.  # noqa: E501

        :param quantity_available: The quantity_available of this ProductDetails.  # noqa: E501
        :type: int

### `digi_key_part_number()`

Gets the digi_key_part_number of this ProductDetails.  # noqa: E501

        The Digi-Key part number.  # noqa: E501

        :return: The digi_key_part_number of this ProductDetails.  # noqa: E501
        :rtype: str

### `digi_key_part_number()`

Sets the digi_key_part_number of this ProductDetails.

        The Digi-Key part number.  # noqa: E501

        :param digi_key_part_number: The digi_key_part_number of this ProductDetails.  # noqa: E501
        :type: str

### `product_description()`

Gets the product_description of this ProductDetails.  # noqa: E501

        Catalog description of the product.  # noqa: E501

        :return: The product_description of this ProductDetails.  # noqa: E501
        :rtype: str

### `product_description()`

Sets the product_description of this ProductDetails.

        Catalog description of the product.  # noqa: E501

        :param product_description: The product_description of this ProductDetails.  # noqa: E501
        :type: str

### `unit_price()`

Gets the unit_price of this ProductDetails.  # noqa: E501

        The price for a single unit of this product.  # noqa: E501

        :return: The unit_price of this ProductDetails.  # noqa: E501
        :rtype: float

### `unit_price()`

Sets the unit_price of this ProductDetails.

        The price for a single unit of this product.  # noqa: E501

        :param unit_price: The unit_price of this ProductDetails.  # noqa: E501
        :type: float

### `manufacturer()`

Gets the manufacturer of this ProductDetails.  # noqa: E501


        :return: The manufacturer of this ProductDetails.  # noqa: E501
        :rtype: PidVid

### `manufacturer()`

Sets the manufacturer of this ProductDetails.


        :param manufacturer: The manufacturer of this ProductDetails.  # noqa: E501
        :type: PidVid

### `manufacturer_public_quantity()`

Gets the manufacturer_public_quantity of this ProductDetails.  # noqa: E501

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :return: The manufacturer_public_quantity of this ProductDetails.  # noqa: E501
        :rtype: int

### `manufacturer_public_quantity()`

Sets the manufacturer_public_quantity of this ProductDetails.

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :param manufacturer_public_quantity: The manufacturer_public_quantity of this ProductDetails.  # noqa: E501
        :type: int

### `quantity_on_order()`

Gets the quantity_on_order of this ProductDetails.  # noqa: E501

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :return: The quantity_on_order of this ProductDetails.  # noqa: E501
        :rtype: int

### `quantity_on_order()`

Sets the quantity_on_order of this ProductDetails.

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :param quantity_on_order: The quantity_on_order of this ProductDetails.  # noqa: E501
        :type: int

### `dk_plus_restriction()`

Gets the dk_plus_restriction of this ProductDetails.  # noqa: E501

        If true- this product is not available for purchase through the Ordering API - it must be purchased through the  Digi-Key web site  # noqa: E501

        :return: The dk_plus_restriction of this ProductDetails.  # noqa: E501
        :rtype: bool

### `dk_plus_restriction()`

Sets the dk_plus_restriction of this ProductDetails.

        If true- this product is not available for purchase through the Ordering API - it must be purchased through the  Digi-Key web site  # noqa: E501

        :param dk_plus_restriction: The dk_plus_restriction of this ProductDetails.  # noqa: E501
        :type: bool

### `supplier_direct_ship()`

Gets the supplier_direct_ship of this ProductDetails.  # noqa: E501

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :return: The supplier_direct_ship of this ProductDetails.  # noqa: E501
        :rtype: bool

### `supplier_direct_ship()`

Sets the supplier_direct_ship of this ProductDetails.

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :param supplier_direct_ship: The supplier_direct_ship of this ProductDetails.  # noqa: E501
        :type: bool

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `product_details()`

Gets the product_details of this BatchProductDetailsResponse.  # noqa: E501

        List of ProductDetails  # noqa: E501

        :return: The product_details of this BatchProductDetailsResponse.  # noqa: E501
        :rtype: list[ProductDetails]

### `product_details()`

Sets the product_details of this BatchProductDetailsResponse.

        List of ProductDetails  # noqa: E501

        :param product_details: The product_details of this BatchProductDetailsResponse.  # noqa: E501
        :type: list[ProductDetails]

### `errors()`

Gets the errors of this BatchProductDetailsResponse.  # noqa: E501

        List of Errors  # noqa: E501

        :return: The errors of this BatchProductDetailsResponse.  # noqa: E501
        :rtype: list[str]

### `errors()`

Sets the errors of this BatchProductDetailsResponse.

        List of Errors  # noqa: E501

        :param errors: The errors of this BatchProductDetailsResponse.  # noqa: E501
        :type: list[str]

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `associated_product()`

Gets the associated_product of this KitPart.  # noqa: E501


        :return: The associated_product of this KitPart.  # noqa: E501
        :rtype: AssociatedProduct

### `associated_product()`

Sets the associated_product of this KitPart.


        :param associated_product: The associated_product of this KitPart.  # noqa: E501
        :type: AssociatedProduct

### `kit_part_quantity()`

Gets the kit_part_quantity of this KitPart.  # noqa: E501

        Number of the product in the Kit.  # noqa: E501

        :return: The kit_part_quantity of this KitPart.  # noqa: E501
        :rtype: int

### `kit_part_quantity()`

Sets the kit_part_quantity of this KitPart.

        Number of the product in the Kit.  # noqa: E501

        :param kit_part_quantity: The kit_part_quantity of this KitPart.  # noqa: E501
        :type: int

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `product_url()`

Gets the product_url of this AssociatedProduct.  # noqa: E501

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :return: The product_url of this AssociatedProduct.  # noqa: E501
        :rtype: str

### `product_url()`

Sets the product_url of this AssociatedProduct.

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :param product_url: The product_url of this AssociatedProduct.  # noqa: E501
        :type: str

### `manufacturer_part_number()`

Gets the manufacturer_part_number of this AssociatedProduct.  # noqa: E501

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :return: The manufacturer_part_number of this AssociatedProduct.  # noqa: E501
        :rtype: str

### `manufacturer_part_number()`

Sets the manufacturer_part_number of this AssociatedProduct.

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :param manufacturer_part_number: The manufacturer_part_number of this AssociatedProduct.  # noqa: E501
        :type: str

### `minimum_order_quantity()`

Gets the minimum_order_quantity of this AssociatedProduct.  # noqa: E501

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :return: The minimum_order_quantity of this AssociatedProduct.  # noqa: E501
        :rtype: int

### `minimum_order_quantity()`

Sets the minimum_order_quantity of this AssociatedProduct.

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :param minimum_order_quantity: The minimum_order_quantity of this AssociatedProduct.  # noqa: E501
        :type: int

### `non_stock()`

Gets the non_stock of this AssociatedProduct.  # noqa: E501

        Indicates this product is a non stock product.  # noqa: E501

        :return: The non_stock of this AssociatedProduct.  # noqa: E501
        :rtype: bool

### `non_stock()`

Sets the non_stock of this AssociatedProduct.

        Indicates this product is a non stock product.  # noqa: E501

        :param non_stock: The non_stock of this AssociatedProduct.  # noqa: E501
        :type: bool

### `packaging()`

Gets the packaging of this AssociatedProduct.  # noqa: E501


        :return: The packaging of this AssociatedProduct.  # noqa: E501
        :rtype: PidVid

### `packaging()`

Sets the packaging of this AssociatedProduct.


        :param packaging: The packaging of this AssociatedProduct.  # noqa: E501
        :type: PidVid

### `quantity_available()`

Gets the quantity_available of this AssociatedProduct.  # noqa: E501

        Quantity of the product available for immediate sale.  # noqa: E501

        :return: The quantity_available of this AssociatedProduct.  # noqa: E501
        :rtype: int

### `quantity_available()`

Sets the quantity_available of this AssociatedProduct.

        Quantity of the product available for immediate sale.  # noqa: E501

        :param quantity_available: The quantity_available of this AssociatedProduct.  # noqa: E501
        :type: int

### `digi_key_part_number()`

Gets the digi_key_part_number of this AssociatedProduct.  # noqa: E501

        The Digi-Key part number.  # noqa: E501

        :return: The digi_key_part_number of this AssociatedProduct.  # noqa: E501
        :rtype: str

### `digi_key_part_number()`

Sets the digi_key_part_number of this AssociatedProduct.

        The Digi-Key part number.  # noqa: E501

        :param digi_key_part_number: The digi_key_part_number of this AssociatedProduct.  # noqa: E501
        :type: str

### `product_description()`

Gets the product_description of this AssociatedProduct.  # noqa: E501

        Catalog description of the product.  # noqa: E501

        :return: The product_description of this AssociatedProduct.  # noqa: E501
        :rtype: str

### `product_description()`

Sets the product_description of this AssociatedProduct.

        Catalog description of the product.  # noqa: E501

        :param product_description: The product_description of this AssociatedProduct.  # noqa: E501
        :type: str

### `unit_price()`

Gets the unit_price of this AssociatedProduct.  # noqa: E501

        The price for a single unit of this product.  # noqa: E501

        :return: The unit_price of this AssociatedProduct.  # noqa: E501
        :rtype: float

### `unit_price()`

Sets the unit_price of this AssociatedProduct.

        The price for a single unit of this product.  # noqa: E501

        :param unit_price: The unit_price of this AssociatedProduct.  # noqa: E501
        :type: float

### `manufacturer()`

Gets the manufacturer of this AssociatedProduct.  # noqa: E501


        :return: The manufacturer of this AssociatedProduct.  # noqa: E501
        :rtype: PidVid

### `manufacturer()`

Sets the manufacturer of this AssociatedProduct.


        :param manufacturer: The manufacturer of this AssociatedProduct.  # noqa: E501
        :type: PidVid

### `manufacturer_public_quantity()`

Gets the manufacturer_public_quantity of this AssociatedProduct.  # noqa: E501

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :return: The manufacturer_public_quantity of this AssociatedProduct.  # noqa: E501
        :rtype: int

### `manufacturer_public_quantity()`

Sets the manufacturer_public_quantity of this AssociatedProduct.

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :param manufacturer_public_quantity: The manufacturer_public_quantity of this AssociatedProduct.  # noqa: E501
        :type: int

### `quantity_on_order()`

Gets the quantity_on_order of this AssociatedProduct.  # noqa: E501

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :return: The quantity_on_order of this AssociatedProduct.  # noqa: E501
        :rtype: int

### `quantity_on_order()`

Sets the quantity_on_order of this AssociatedProduct.

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :param quantity_on_order: The quantity_on_order of this AssociatedProduct.  # noqa: E501
        :type: int

### `dk_plus_restriction()`

Gets the dk_plus_restriction of this AssociatedProduct.  # noqa: E501

        If true- this product is not available for purchase through the Ordering API - it must be purchased through the  Digi-Key web site  # noqa: E501

        :return: The dk_plus_restriction of this AssociatedProduct.  # noqa: E501
        :rtype: bool

### `dk_plus_restriction()`

Sets the dk_plus_restriction of this AssociatedProduct.

        If true- this product is not available for purchase through the Ordering API - it must be purchased through the  Digi-Key web site  # noqa: E501

        :param dk_plus_restriction: The dk_plus_restriction of this AssociatedProduct.  # noqa: E501
        :type: bool

### `supplier_direct_ship()`

Gets the supplier_direct_ship of this AssociatedProduct.  # noqa: E501

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :return: The supplier_direct_ship of this AssociatedProduct.  # noqa: E501
        :rtype: bool

### `supplier_direct_ship()`

Sets the supplier_direct_ship of this AssociatedProduct.

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :param supplier_direct_ship: The supplier_direct_ship of this AssociatedProduct.  # noqa: E501
        :type: bool

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `manufacturer_part_number()`

Gets the manufacturer_part_number of this BasicProduct.  # noqa: E501

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :return: The manufacturer_part_number of this BasicProduct.  # noqa: E501
        :rtype: str

### `manufacturer_part_number()`

Sets the manufacturer_part_number of this BasicProduct.

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :param manufacturer_part_number: The manufacturer_part_number of this BasicProduct.  # noqa: E501
        :type: str

### `minimum_order_quantity()`

Gets the minimum_order_quantity of this BasicProduct.  # noqa: E501

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :return: The minimum_order_quantity of this BasicProduct.  # noqa: E501
        :rtype: int

### `minimum_order_quantity()`

Sets the minimum_order_quantity of this BasicProduct.

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :param minimum_order_quantity: The minimum_order_quantity of this BasicProduct.  # noqa: E501
        :type: int

### `non_stock()`

Gets the non_stock of this BasicProduct.  # noqa: E501

        Indicates this product is a non stock product.  # noqa: E501

        :return: The non_stock of this BasicProduct.  # noqa: E501
        :rtype: bool

### `non_stock()`

Sets the non_stock of this BasicProduct.

        Indicates this product is a non stock product.  # noqa: E501

        :param non_stock: The non_stock of this BasicProduct.  # noqa: E501
        :type: bool

### `packaging()`

Gets the packaging of this BasicProduct.  # noqa: E501


        :return: The packaging of this BasicProduct.  # noqa: E501
        :rtype: PidVid

### `packaging()`

Sets the packaging of this BasicProduct.


        :param packaging: The packaging of this BasicProduct.  # noqa: E501
        :type: PidVid

### `quantity_available()`

Gets the quantity_available of this BasicProduct.  # noqa: E501

        Quantity of the product available for immediate sale.  # noqa: E501

        :return: The quantity_available of this BasicProduct.  # noqa: E501
        :rtype: int

### `quantity_available()`

Sets the quantity_available of this BasicProduct.

        Quantity of the product available for immediate sale.  # noqa: E501

        :param quantity_available: The quantity_available of this BasicProduct.  # noqa: E501
        :type: int

### `digi_key_part_number()`

Gets the digi_key_part_number of this BasicProduct.  # noqa: E501

        The Digi-Key part number.  # noqa: E501

        :return: The digi_key_part_number of this BasicProduct.  # noqa: E501
        :rtype: str

### `digi_key_part_number()`

Sets the digi_key_part_number of this BasicProduct.

        The Digi-Key part number.  # noqa: E501

        :param digi_key_part_number: The digi_key_part_number of this BasicProduct.  # noqa: E501
        :type: str

### `product_description()`

Gets the product_description of this BasicProduct.  # noqa: E501

        Catalog description of the product.  # noqa: E501

        :return: The product_description of this BasicProduct.  # noqa: E501
        :rtype: str

### `product_description()`

Sets the product_description of this BasicProduct.

        Catalog description of the product.  # noqa: E501

        :param product_description: The product_description of this BasicProduct.  # noqa: E501
        :type: str

### `unit_price()`

Gets the unit_price of this BasicProduct.  # noqa: E501

        The price for a single unit of this product.  # noqa: E501

        :return: The unit_price of this BasicProduct.  # noqa: E501
        :rtype: float

### `unit_price()`

Sets the unit_price of this BasicProduct.

        The price for a single unit of this product.  # noqa: E501

        :param unit_price: The unit_price of this BasicProduct.  # noqa: E501
        :type: float

### `manufacturer()`

Gets the manufacturer of this BasicProduct.  # noqa: E501


        :return: The manufacturer of this BasicProduct.  # noqa: E501
        :rtype: PidVid

### `manufacturer()`

Sets the manufacturer of this BasicProduct.


        :param manufacturer: The manufacturer of this BasicProduct.  # noqa: E501
        :type: PidVid

### `manufacturer_public_quantity()`

Gets the manufacturer_public_quantity of this BasicProduct.  # noqa: E501

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :return: The manufacturer_public_quantity of this BasicProduct.  # noqa: E501
        :rtype: int

### `manufacturer_public_quantity()`

Sets the manufacturer_public_quantity of this BasicProduct.

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :param manufacturer_public_quantity: The manufacturer_public_quantity of this BasicProduct.  # noqa: E501
        :type: int

### `quantity_on_order()`

Gets the quantity_on_order of this BasicProduct.  # noqa: E501

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :return: The quantity_on_order of this BasicProduct.  # noqa: E501
        :rtype: int

### `quantity_on_order()`

Sets the quantity_on_order of this BasicProduct.

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :param quantity_on_order: The quantity_on_order of this BasicProduct.  # noqa: E501
        :type: int

### `dk_plus_restriction()`

Gets the dk_plus_restriction of this BasicProduct.  # noqa: E501

        If true- this product is not available for purchase through the Ordering API - it must be purchased through the  Digi-Key web site  # noqa: E501

        :return: The dk_plus_restriction of this BasicProduct.  # noqa: E501
        :rtype: bool

### `dk_plus_restriction()`

Sets the dk_plus_restriction of this BasicProduct.

        If true- this product is not available for purchase through the Ordering API - it must be purchased through the  Digi-Key web site  # noqa: E501

        :param dk_plus_restriction: The dk_plus_restriction of this BasicProduct.  # noqa: E501
        :type: bool

### `supplier_direct_ship()`

Gets the supplier_direct_ship of this BasicProduct.  # noqa: E501

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :return: The supplier_direct_ship of this BasicProduct.  # noqa: E501
        :rtype: bool

### `supplier_direct_ship()`

Sets the supplier_direct_ship of this BasicProduct.

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :param supplier_direct_ship: The supplier_direct_ship of this BasicProduct.  # noqa: E501
        :type: bool

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `media_type()`

Gets the media_type of this MediaLinks.  # noqa: E501

        The type of media.  # noqa: E501

        :return: The media_type of this MediaLinks.  # noqa: E501
        :rtype: str

### `media_type()`

Sets the media_type of this MediaLinks.

        The type of media.  # noqa: E501

        :param media_type: The media_type of this MediaLinks.  # noqa: E501
        :type: str

### `title()`

Gets the title of this MediaLinks.  # noqa: E501

        The title of the media.  # noqa: E501

        :return: The title of this MediaLinks.  # noqa: E501
        :rtype: str

### `title()`

Sets the title of this MediaLinks.

        The title of the media.  # noqa: E501

        :param title: The title of this MediaLinks.  # noqa: E501
        :type: str

### `small_photo()`

Gets the small_photo of this MediaLinks.  # noqa: E501

        URL to a small photo.  # noqa: E501

        :return: The small_photo of this MediaLinks.  # noqa: E501
        :rtype: str

### `small_photo()`

Sets the small_photo of this MediaLinks.

        URL to a small photo.  # noqa: E501

        :param small_photo: The small_photo of this MediaLinks.  # noqa: E501
        :type: str

### `thumbnail()`

Gets the thumbnail of this MediaLinks.  # noqa: E501

        URL to the thumbnail image of the media.  # noqa: E501

        :return: The thumbnail of this MediaLinks.  # noqa: E501
        :rtype: str

### `thumbnail()`

Sets the thumbnail of this MediaLinks.

        URL to the thumbnail image of the media.  # noqa: E501

        :param thumbnail: The thumbnail of this MediaLinks.  # noqa: E501
        :type: str

### `url()`

Gets the url of this MediaLinks.  # noqa: E501

        URL of the media.  # noqa: E501

        :return: The url of this MediaLinks.  # noqa: E501
        :rtype: str

### `url()`

Sets the url of this MediaLinks.

        URL of the media.  # noqa: E501

        :param url: The url of this MediaLinks.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `break_quantity()`

Gets the break_quantity of this PriceBreak.  # noqa: E501

        Price tiers based on the available quantities of the product.  # noqa: E501

        :return: The break_quantity of this PriceBreak.  # noqa: E501
        :rtype: int

### `break_quantity()`

Sets the break_quantity of this PriceBreak.

        Price tiers based on the available quantities of the product.  # noqa: E501

        :param break_quantity: The break_quantity of this PriceBreak.  # noqa: E501
        :type: int

### `unit_price()`

Gets the unit_price of this PriceBreak.  # noqa: E501

        Price of a single unit of the product at this break.  # noqa: E501

        :return: The unit_price of this PriceBreak.  # noqa: E501
        :rtype: float

### `unit_price()`

Sets the unit_price of this PriceBreak.

        Price of a single unit of the product at this break.  # noqa: E501

        :param unit_price: The unit_price of this PriceBreak.  # noqa: E501
        :type: float

### `total_price()`

Gets the total_price of this PriceBreak.  # noqa: E501

        Price of BreakQuantity units of the product.  # noqa: E501

        :return: The total_price of this PriceBreak.  # noqa: E501
        :rtype: float

### `total_price()`

Sets the total_price of this PriceBreak.

        Price of BreakQuantity units of the product.  # noqa: E501

        :param total_price: The total_price of this PriceBreak.  # noqa: E501
        :type: float

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `manufacturer_product()`

Gets the manufacturer_product of this ManufacturerProductDetailsRequest.  # noqa: E501

        Manufacturer product name to search on.  # noqa: E501

        :return: The manufacturer_product of this ManufacturerProductDetailsRequest.  # noqa: E501
        :rtype: str

### `manufacturer_product()`

Sets the manufacturer_product of this ManufacturerProductDetailsRequest.

        Manufacturer product name to search on.  # noqa: E501

        :param manufacturer_product: The manufacturer_product of this ManufacturerProductDetailsRequest.  # noqa: E501
        :type: str

### `record_count()`

Gets the record_count of this ManufacturerProductDetailsRequest.  # noqa: E501

        Number of products to return between 1 and 50.  # noqa: E501

        :return: The record_count of this ManufacturerProductDetailsRequest.  # noqa: E501
        :rtype: int

### `record_count()`

Sets the record_count of this ManufacturerProductDetailsRequest.

        Number of products to return between 1 and 50.  # noqa: E501

        :param record_count: The record_count of this ManufacturerProductDetailsRequest.  # noqa: E501
        :type: int

### `record_start_position()`

Gets the record_start_position of this ManufacturerProductDetailsRequest.  # noqa: E501

        The starting index of the records returned. This is used to paginate beyond 50 results.  # noqa: E501

        :return: The record_start_position of this ManufacturerProductDetailsRequest.  # noqa: E501
        :rtype: int

### `record_start_position()`

Sets the record_start_position of this ManufacturerProductDetailsRequest.

        The starting index of the records returned. This is used to paginate beyond 50 results.  # noqa: E501

        :param record_start_position: The record_start_position of this ManufacturerProductDetailsRequest.  # noqa: E501
        :type: int

### `filters()`

Gets the filters of this ManufacturerProductDetailsRequest.  # noqa: E501


        :return: The filters of this ManufacturerProductDetailsRequest.  # noqa: E501
        :rtype: Filters

### `filters()`

Sets the filters of this ManufacturerProductDetailsRequest.


        :param filters: The filters of this ManufacturerProductDetailsRequest.  # noqa: E501
        :type: Filters

### `sort()`

Gets the sort of this ManufacturerProductDetailsRequest.  # noqa: E501


        :return: The sort of this ManufacturerProductDetailsRequest.  # noqa: E501
        :rtype: SortParameters

### `sort()`

Sets the sort of this ManufacturerProductDetailsRequest.


        :param sort: The sort of this ManufacturerProductDetailsRequest.  # noqa: E501
        :type: SortParameters

### `requested_quantity()`

Gets the requested_quantity of this ManufacturerProductDetailsRequest.  # noqa: E501

        The quantity of the product you are looking to purchase. This is used with the SortByUnitPrice SortOption as price varies at differing quantities.  # noqa: E501

        :return: The requested_quantity of this ManufacturerProductDetailsRequest.  # noqa: E501
        :rtype: int

### `requested_quantity()`

Sets the requested_quantity of this ManufacturerProductDetailsRequest.

        The quantity of the product you are looking to purchase. This is used with the SortByUnitPrice SortOption as price varies at differing quantities.  # noqa: E501

        :param requested_quantity: The requested_quantity of this ManufacturerProductDetailsRequest.  # noqa: E501
        :type: int

### `search_options()`

Gets the search_options of this ManufacturerProductDetailsRequest.  # noqa: E501

        Filters the search results by the included SearchOption.  # noqa: E501

        :return: The search_options of this ManufacturerProductDetailsRequest.  # noqa: E501
        :rtype: list[SearchOption]

### `search_options()`

Sets the search_options of this ManufacturerProductDetailsRequest.

        Filters the search results by the included SearchOption.  # noqa: E501

        :param search_options: The search_options of this ManufacturerProductDetailsRequest.  # noqa: E501
        :type: list[SearchOption]

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `field()`

Gets the field of this ApiValidationError.  # noqa: E501


        :return: The field of this ApiValidationError.  # noqa: E501
        :rtype: str

### `field()`

Sets the field of this ApiValidationError.


        :param field: The field of this ApiValidationError.  # noqa: E501
        :type: str

### `message()`

Gets the message of this ApiValidationError.  # noqa: E501


        :return: The message of this ApiValidationError.  # noqa: E501
        :rtype: str

### `message()`

Sets the message of this ApiValidationError.


        :param message: The message of this ApiValidationError.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `children()`

Gets the children of this LimitedTaxonomy.  # noqa: E501

        List of taxonomies contained within this taxonomy.  # noqa: E501

        :return: The children of this LimitedTaxonomy.  # noqa: E501
        :rtype: list[LimitedTaxonomy]

### `children()`

Sets the children of this LimitedTaxonomy.

        List of taxonomies contained within this taxonomy.  # noqa: E501

        :param children: The children of this LimitedTaxonomy.  # noqa: E501
        :type: list[LimitedTaxonomy]

### `product_count()`

Gets the product_count of this LimitedTaxonomy.  # noqa: E501

        The number of products contained within this taxonomy.  # noqa: E501

        :return: The product_count of this LimitedTaxonomy.  # noqa: E501
        :rtype: int

### `product_count()`

Sets the product_count of this LimitedTaxonomy.

        The number of products contained within this taxonomy.  # noqa: E501

        :param product_count: The product_count of this LimitedTaxonomy.  # noqa: E501
        :type: int

### `new_product_count()`

Gets the new_product_count of this LimitedTaxonomy.  # noqa: E501

        The number of new products contained within this taxonomy.  # noqa: E501

        :return: The new_product_count of this LimitedTaxonomy.  # noqa: E501
        :rtype: int

### `new_product_count()`

Sets the new_product_count of this LimitedTaxonomy.

        The number of new products contained within this taxonomy.  # noqa: E501

        :param new_product_count: The new_product_count of this LimitedTaxonomy.  # noqa: E501
        :type: int

### `parameter_id()`

Gets the parameter_id of this LimitedTaxonomy.  # noqa: E501

        The Id of the parameter.  # noqa: E501

        :return: The parameter_id of this LimitedTaxonomy.  # noqa: E501
        :rtype: int

### `parameter_id()`

Sets the parameter_id of this LimitedTaxonomy.

        The Id of the parameter.  # noqa: E501

        :param parameter_id: The parameter_id of this LimitedTaxonomy.  # noqa: E501
        :type: int

### `value_id()`

Gets the value_id of this LimitedTaxonomy.  # noqa: E501

        The Id of the value.  # noqa: E501

        :return: The value_id of this LimitedTaxonomy.  # noqa: E501
        :rtype: str

### `value_id()`

Sets the value_id of this LimitedTaxonomy.

        The Id of the value.  # noqa: E501

        :param value_id: The value_id of this LimitedTaxonomy.  # noqa: E501
        :type: str

### `parameter()`

Gets the parameter of this LimitedTaxonomy.  # noqa: E501

        The name of the parameter.  # noqa: E501

        :return: The parameter of this LimitedTaxonomy.  # noqa: E501
        :rtype: str

### `parameter()`

Sets the parameter of this LimitedTaxonomy.

        The name of the parameter.  # noqa: E501

        :param parameter: The parameter of this LimitedTaxonomy.  # noqa: E501
        :type: str

### `value()`

Gets the value of this LimitedTaxonomy.  # noqa: E501

        The name of the value.  # noqa: E501

        :return: The value of this LimitedTaxonomy.  # noqa: E501
        :rtype: str

### `value()`

Sets the value of this LimitedTaxonomy.

        The name of the value.  # noqa: E501

        :param value: The value of this LimitedTaxonomy.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `reeling_fee()`

Gets the reeling_fee of this DigiReelPricing.  # noqa: E501

        Fee per reel ordered.  # noqa: E501

        :return: The reeling_fee of this DigiReelPricing.  # noqa: E501
        :rtype: float

### `reeling_fee()`

Sets the reeling_fee of this DigiReelPricing.

        Fee per reel ordered.  # noqa: E501

        :param reeling_fee: The reeling_fee of this DigiReelPricing.  # noqa: E501
        :type: float

### `unit_price()`

Gets the unit_price of this DigiReelPricing.  # noqa: E501

        Price of a single unit of the product.  # noqa: E501

        :return: The unit_price of this DigiReelPricing.  # noqa: E501
        :rtype: float

### `unit_price()`

Sets the unit_price of this DigiReelPricing.

        Price of a single unit of the product.  # noqa: E501

        :param unit_price: The unit_price of this DigiReelPricing.  # noqa: E501
        :type: float

### `extended_price()`

Gets the extended_price of this DigiReelPricing.  # noqa: E501

        The total price of the requested reels and the reeling fee.  # noqa: E501

        :return: The extended_price of this DigiReelPricing.  # noqa: E501
        :rtype: float

### `extended_price()`

Sets the extended_price of this DigiReelPricing.

        The total price of the requested reels and the reeling fee.  # noqa: E501

        :param extended_price: The extended_price of this DigiReelPricing.  # noqa: E501
        :type: float

### `requested_quantity()`

Gets the requested_quantity of this DigiReelPricing.  # noqa: E501

        The passed in quantity of the product you are looking to create a Digi-Reel with.  # noqa: E501

        :return: The requested_quantity of this DigiReelPricing.  # noqa: E501
        :rtype: int

### `requested_quantity()`

Sets the requested_quantity of this DigiReelPricing.

        The passed in quantity of the product you are looking to create a Digi-Reel with.  # noqa: E501

        :param requested_quantity: The requested_quantity of this DigiReelPricing.  # noqa: E501
        :type: int

### `search_locale_used()`

Gets the search_locale_used of this DigiReelPricing.  # noqa: E501


        :return: The search_locale_used of this DigiReelPricing.  # noqa: E501
        :rtype: IsoSearchLocale

### `search_locale_used()`

Sets the search_locale_used of this DigiReelPricing.


        :param search_locale_used: The search_locale_used of this DigiReelPricing.  # noqa: E501
        :type: IsoSearchLocale

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `error_response_version()`

Gets the error_response_version of this ApiErrorResponse.  # noqa: E501


        :return: The error_response_version of this ApiErrorResponse.  # noqa: E501
        :rtype: str

### `error_response_version()`

Sets the error_response_version of this ApiErrorResponse.


        :param error_response_version: The error_response_version of this ApiErrorResponse.  # noqa: E501
        :type: str

### `status_code()`

Gets the status_code of this ApiErrorResponse.  # noqa: E501


        :return: The status_code of this ApiErrorResponse.  # noqa: E501
        :rtype: int

### `status_code()`

Sets the status_code of this ApiErrorResponse.


        :param status_code: The status_code of this ApiErrorResponse.  # noqa: E501
        :type: int

### `error_message()`

Gets the error_message of this ApiErrorResponse.  # noqa: E501


        :return: The error_message of this ApiErrorResponse.  # noqa: E501
        :rtype: str

### `error_message()`

Sets the error_message of this ApiErrorResponse.


        :param error_message: The error_message of this ApiErrorResponse.  # noqa: E501
        :type: str

### `error_details()`

Gets the error_details of this ApiErrorResponse.  # noqa: E501


        :return: The error_details of this ApiErrorResponse.  # noqa: E501
        :rtype: str

### `error_details()`

Sets the error_details of this ApiErrorResponse.


        :param error_details: The error_details of this ApiErrorResponse.  # noqa: E501
        :type: str

### `request_id()`

Gets the request_id of this ApiErrorResponse.  # noqa: E501


        :return: The request_id of this ApiErrorResponse.  # noqa: E501
        :rtype: str

### `request_id()`

Sets the request_id of this ApiErrorResponse.


        :param request_id: The request_id of this ApiErrorResponse.  # noqa: E501
        :type: str

### `validation_errors()`

Gets the validation_errors of this ApiErrorResponse.  # noqa: E501


        :return: The validation_errors of this ApiErrorResponse.  # noqa: E501
        :rtype: list[ApiValidationError]

### `validation_errors()`

Sets the validation_errors of this ApiErrorResponse.


        :param validation_errors: The validation_errors of this ApiErrorResponse.  # noqa: E501
        :type: list[ApiValidationError]

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `site()`

Gets the site of this IsoSearchLocale.  # noqa: E501

        The site used for the API call.  # noqa: E501

        :return: The site of this IsoSearchLocale.  # noqa: E501
        :rtype: str

### `site()`

Sets the site of this IsoSearchLocale.

        The site used for the API call.  # noqa: E501

        :param site: The site of this IsoSearchLocale.  # noqa: E501
        :type: str

### `language()`

Gets the language of this IsoSearchLocale.  # noqa: E501

        The language used for the API call. If the provided language is not valid for the site, it will be set to the site default.  # noqa: E501

        :return: The language of this IsoSearchLocale.  # noqa: E501
        :rtype: str

### `language()`

Sets the language of this IsoSearchLocale.

        The language used for the API call. If the provided language is not valid for the site, it will be set to the site default.  # noqa: E501

        :param language: The language of this IsoSearchLocale.  # noqa: E501
        :type: str

### `currency()`

Gets the currency of this IsoSearchLocale.  # noqa: E501

        The currency used for the API call. If the provided currency is not valid for the site, it will be set to the site default.  # noqa: E501

        :return: The currency of this IsoSearchLocale.  # noqa: E501
        :rtype: str

### `currency()`

Sets the currency of this IsoSearchLocale.

        The currency used for the API call. If the provided currency is not valid for the site, it will be set to the site default.  # noqa: E501

        :param currency: The currency of this IsoSearchLocale.  # noqa: E501
        :type: str

### `ship_to_country()`

Gets the ship_to_country of this IsoSearchLocale.  # noqa: E501

        The destination for shipping the product. This is used for tariffs and regional pricing.  # noqa: E501

        :return: The ship_to_country of this IsoSearchLocale.  # noqa: E501
        :rtype: str

### `ship_to_country()`

Sets the ship_to_country of this IsoSearchLocale.

        The destination for shipping the product. This is used for tariffs and regional pricing.  # noqa: E501

        :param ship_to_country: The ship_to_country of this IsoSearchLocale.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `parameter_id()`

Gets the parameter_id of this PidVid.  # noqa: E501

        The Id of the parameter.  # noqa: E501

        :return: The parameter_id of this PidVid.  # noqa: E501
        :rtype: int

### `parameter_id()`

Sets the parameter_id of this PidVid.

        The Id of the parameter.  # noqa: E501

        :param parameter_id: The parameter_id of this PidVid.  # noqa: E501
        :type: int

### `value_id()`

Gets the value_id of this PidVid.  # noqa: E501

        The Id of the value.  # noqa: E501

        :return: The value_id of this PidVid.  # noqa: E501
        :rtype: str

### `value_id()`

Sets the value_id of this PidVid.

        The Id of the value.  # noqa: E501

        :param value_id: The value_id of this PidVid.  # noqa: E501
        :type: str

### `parameter()`

Gets the parameter of this PidVid.  # noqa: E501

        The name of the parameter.  # noqa: E501

        :return: The parameter of this PidVid.  # noqa: E501
        :rtype: str

### `parameter()`

Sets the parameter of this PidVid.

        The name of the parameter.  # noqa: E501

        :param parameter: The parameter of this PidVid.  # noqa: E501
        :type: str

### `value()`

Gets the value of this PidVid.  # noqa: E501

        The name of the value.  # noqa: E501

        :return: The value of this PidVid.  # noqa: E501
        :rtype: str

### `value()`

Sets the value of this PidVid.

        The name of the value.  # noqa: E501

        :param value: The value of this PidVid.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `sort_option()`

Gets the sort_option of this SortParameters.  # noqa: E501


        :return: The sort_option of this SortParameters.  # noqa: E501
        :rtype: SortOption

### `sort_option()`

Sets the sort_option of this SortParameters.


        :param sort_option: The sort_option of this SortParameters.  # noqa: E501
        :type: SortOption

### `direction()`

Gets the direction of this SortParameters.  # noqa: E501


        :return: The direction of this SortParameters.  # noqa: E501
        :rtype: SortDirection

### `direction()`

Sets the direction of this SortParameters.


        :param direction: The direction of this SortParameters.  # noqa: E501
        :type: SortDirection

### `sort_parameter_id()`

Gets the sort_parameter_id of this SortParameters.  # noqa: E501

        The ParameterId of the parameter to sort on. The ParameterId can be found in the Search response. This is only used with SortByParameter.  # noqa: E501

        :return: The sort_parameter_id of this SortParameters.  # noqa: E501
        :rtype: int

### `sort_parameter_id()`

Sets the sort_parameter_id of this SortParameters.

        The ParameterId of the parameter to sort on. The ParameterId can be found in the Search response. This is only used with SortByParameter.  # noqa: E501

        :param sort_parameter_id: The sort_parameter_id of this SortParameters.  # noqa: E501
        :type: int

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `my_pricing()`

Gets the my_pricing of this ProductDetails.  # noqa: E501

        Your pricing for the account with which you authenticated. Also dependent on locale information.  # noqa: E501

        :return: The my_pricing of this ProductDetails.  # noqa: E501
        :rtype: list[PriceBreak]

### `my_pricing()`

Sets the my_pricing of this ProductDetails.

        Your pricing for the account with which you authenticated. Also dependent on locale information.  # noqa: E501

        :param my_pricing: The my_pricing of this ProductDetails.  # noqa: E501
        :type: list[PriceBreak]

### `obsolete()`

Gets the obsolete of this ProductDetails.  # noqa: E501

        Indicates whether this Part is obsolete.  # noqa: E501

        :return: The obsolete of this ProductDetails.  # noqa: E501
        :rtype: bool

### `obsolete()`

Sets the obsolete of this ProductDetails.

        Indicates whether this Part is obsolete.  # noqa: E501

        :param obsolete: The obsolete of this ProductDetails.  # noqa: E501
        :type: bool

### `media_links()`

Gets the media_links of this ProductDetails.  # noqa: E501

        Collection of MediaLinks objects. These can contain links to datasheets, photos or manuals.  # noqa: E501

        :return: The media_links of this ProductDetails.  # noqa: E501
        :rtype: list[MediaLinks]

### `media_links()`

Sets the media_links of this ProductDetails.

        Collection of MediaLinks objects. These can contain links to datasheets, photos or manuals.  # noqa: E501

        :param media_links: The media_links of this ProductDetails.  # noqa: E501
        :type: list[MediaLinks]

### `standard_package()`

Gets the standard_package of this ProductDetails.  # noqa: E501

        The number of products in the manufacturer's standard package.  # noqa: E501

        :return: The standard_package of this ProductDetails.  # noqa: E501
        :rtype: int

### `standard_package()`

Sets the standard_package of this ProductDetails.

        The number of products in the manufacturer's standard package.  # noqa: E501

        :param standard_package: The standard_package of this ProductDetails.  # noqa: E501
        :type: int

### `limited_taxonomy()`

Gets the limited_taxonomy of this ProductDetails.  # noqa: E501


        :return: The limited_taxonomy of this ProductDetails.  # noqa: E501
        :rtype: LimitedTaxonomy

### `limited_taxonomy()`

Sets the limited_taxonomy of this ProductDetails.


        :param limited_taxonomy: The limited_taxonomy of this ProductDetails.  # noqa: E501
        :type: LimitedTaxonomy

### `kits()`

Gets the kits of this ProductDetails.  # noqa: E501

        Kits that this product is contained in.  # noqa: E501

        :return: The kits of this ProductDetails.  # noqa: E501
        :rtype: list[AssociatedProduct]

### `kits()`

Sets the kits of this ProductDetails.

        Kits that this product is contained in.  # noqa: E501

        :param kits: The kits of this ProductDetails.  # noqa: E501
        :type: list[AssociatedProduct]

### `kit_contents()`

Gets the kit_contents of this ProductDetails.  # noqa: E501

        Products contained within this product. Only applicable if this product is a kit.  # noqa: E501

        :return: The kit_contents of this ProductDetails.  # noqa: E501
        :rtype: list[KitPart]

### `kit_contents()`

Sets the kit_contents of this ProductDetails.

        Products contained within this product. Only applicable if this product is a kit.  # noqa: E501

        :param kit_contents: The kit_contents of this ProductDetails.  # noqa: E501
        :type: list[KitPart]

### `mating_products()`

Gets the mating_products of this ProductDetails.  # noqa: E501

        An association of same manufacturer products that mate with each other.  # noqa: E501

        :return: The mating_products of this ProductDetails.  # noqa: E501
        :rtype: list[AssociatedProduct]

### `mating_products()`

Sets the mating_products of this ProductDetails.

        An association of same manufacturer products that mate with each other.  # noqa: E501

        :param mating_products: The mating_products of this ProductDetails.  # noqa: E501
        :type: list[AssociatedProduct]

### `search_locale_used()`

Gets the search_locale_used of this ProductDetails.  # noqa: E501


        :return: The search_locale_used of this ProductDetails.  # noqa: E501
        :rtype: IsoSearchLocale

### `search_locale_used()`

Sets the search_locale_used of this ProductDetails.


        :param search_locale_used: The search_locale_used of this ProductDetails.  # noqa: E501
        :type: IsoSearchLocale

### `associated_products()`

Gets the associated_products of this ProductDetails.  # noqa: E501

        Products that are directly correlated to complete the intended function of the product. These products may be  either same manufacturer or differ.  # noqa: E501

        :return: The associated_products of this ProductDetails.  # noqa: E501
        :rtype: list[AssociatedProduct]

### `associated_products()`

Sets the associated_products of this ProductDetails.

        Products that are directly correlated to complete the intended function of the product. These products may be  either same manufacturer or differ.  # noqa: E501

        :param associated_products: The associated_products of this ProductDetails.  # noqa: E501
        :type: list[AssociatedProduct]

### `for_use_with_products()`

Gets the for_use_with_products of this ProductDetails.  # noqa: E501

        Products that are directly correlated to complete the intended function of the product. These products may be  either same manufacturer or differ.  # noqa: E501

        :return: The for_use_with_products of this ProductDetails.  # noqa: E501
        :rtype: list[AssociatedProduct]

### `for_use_with_products()`

Sets the for_use_with_products of this ProductDetails.

        Products that are directly correlated to complete the intended function of the product. These products may be  either same manufacturer or differ.  # noqa: E501

        :param for_use_with_products: The for_use_with_products of this ProductDetails.  # noqa: E501
        :type: list[AssociatedProduct]

### `rohs_subs()`

Gets the rohs_subs of this ProductDetails.  # noqa: E501

        Rohs substitutions  # noqa: E501

        :return: The rohs_subs of this ProductDetails.  # noqa: E501
        :rtype: list[AssociatedProduct]

### `rohs_subs()`

Sets the rohs_subs of this ProductDetails.

        Rohs substitutions  # noqa: E501

        :param rohs_subs: The rohs_subs of this ProductDetails.  # noqa: E501
        :type: list[AssociatedProduct]

### `suggested_subs()`

Gets the suggested_subs of this ProductDetails.  # noqa: E501

        Suggested substitutions for when the product is obsolete.  # noqa: E501

        :return: The suggested_subs of this ProductDetails.  # noqa: E501
        :rtype: list[AssociatedProduct]

### `suggested_subs()`

Sets the suggested_subs of this ProductDetails.

        Suggested substitutions for when the product is obsolete.  # noqa: E501

        :param suggested_subs: The suggested_subs of this ProductDetails.  # noqa: E501
        :type: list[AssociatedProduct]

### `additional_value_fee()`

Gets the additional_value_fee of this ProductDetails.  # noqa: E501

        Any additional value fee. Most commonly the Digi-Reel fee. May be used for programmable parts as well.  # noqa: E501

        :return: The additional_value_fee of this ProductDetails.  # noqa: E501
        :rtype: float

### `additional_value_fee()`

Sets the additional_value_fee of this ProductDetails.

        Any additional value fee. Most commonly the Digi-Reel fee. May be used for programmable parts as well.  # noqa: E501

        :param additional_value_fee: The additional_value_fee of this ProductDetails.  # noqa: E501
        :type: float

### `standard_pricing()`

Gets the standard_pricing of this ProductDetails.  # noqa: E501

        Standard pricing for the validated locale.  # noqa: E501

        :return: The standard_pricing of this ProductDetails.  # noqa: E501
        :rtype: list[PriceBreak]

### `standard_pricing()`

Sets the standard_pricing of this ProductDetails.

        Standard pricing for the validated locale.  # noqa: E501

        :param standard_pricing: The standard_pricing of this ProductDetails.  # noqa: E501
        :type: list[PriceBreak]

### `ro_hs_status()`

Gets the ro_hs_status of this ProductDetails.  # noqa: E501

        RoHS status. Can be: RoHS Compliant, RoHS non-compliant, RoHS Compliant By Exemption, Not Applicable, Vendor  undefined, Request Inventory Verification, ROHS3 Compliant.  # noqa: E501

        :return: The ro_hs_status of this ProductDetails.  # noqa: E501
        :rtype: str

### `ro_hs_status()`

Sets the ro_hs_status of this ProductDetails.

        RoHS status. Can be: RoHS Compliant, RoHS non-compliant, RoHS Compliant By Exemption, Not Applicable, Vendor  undefined, Request Inventory Verification, ROHS3 Compliant.  # noqa: E501

        :param ro_hs_status: The ro_hs_status of this ProductDetails.  # noqa: E501
        :type: str

### `lead_status()`

Gets the lead_status of this ProductDetails.  # noqa: E501

        Lead status. Can be: Lead Free, Contains lead, Lead Free By Exemption, Not Applicable, Vendor undefined, unknown,  or Request Inventory Verification.  # noqa: E501

        :return: The lead_status of this ProductDetails.  # noqa: E501
        :rtype: str

### `lead_status()`

Sets the lead_status of this ProductDetails.

        Lead status. Can be: Lead Free, Contains lead, Lead Free By Exemption, Not Applicable, Vendor undefined, unknown,  or Request Inventory Verification.  # noqa: E501

        :param lead_status: The lead_status of this ProductDetails.  # noqa: E501
        :type: str

### `parameters()`

Gets the parameters of this ProductDetails.  # noqa: E501

        Parameters for the part. Can be used for filtering keyword searches.  # noqa: E501

        :return: The parameters of this ProductDetails.  # noqa: E501
        :rtype: list[PidVid]

### `parameters()`

Sets the parameters of this ProductDetails.

        Parameters for the part. Can be used for filtering keyword searches.  # noqa: E501

        :param parameters: The parameters of this ProductDetails.  # noqa: E501
        :type: list[PidVid]

### `product_url()`

Gets the product_url of this ProductDetails.  # noqa: E501

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :return: The product_url of this ProductDetails.  # noqa: E501
        :rtype: str

### `product_url()`

Sets the product_url of this ProductDetails.

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :param product_url: The product_url of this ProductDetails.  # noqa: E501
        :type: str

### `primary_datasheet()`

Gets the primary_datasheet of this ProductDetails.  # noqa: E501

        The URL to the product's datasheet.  # noqa: E501

        :return: The primary_datasheet of this ProductDetails.  # noqa: E501
        :rtype: str

### `primary_datasheet()`

Sets the primary_datasheet of this ProductDetails.

        The URL to the product's datasheet.  # noqa: E501

        :param primary_datasheet: The primary_datasheet of this ProductDetails.  # noqa: E501
        :type: str

### `primary_photo()`

Gets the primary_photo of this ProductDetails.  # noqa: E501

        The URL to the product's image.  # noqa: E501

        :return: The primary_photo of this ProductDetails.  # noqa: E501
        :rtype: str

### `primary_photo()`

Sets the primary_photo of this ProductDetails.

        The URL to the product's image.  # noqa: E501

        :param primary_photo: The primary_photo of this ProductDetails.  # noqa: E501
        :type: str

### `primary_video()`

Gets the primary_video of this ProductDetails.  # noqa: E501

        The URL to the product's video.  # noqa: E501

        :return: The primary_video of this ProductDetails.  # noqa: E501
        :rtype: str

### `primary_video()`

Sets the primary_video of this ProductDetails.

        The URL to the product's video.  # noqa: E501

        :param primary_video: The primary_video of this ProductDetails.  # noqa: E501
        :type: str

### `series()`

Gets the series of this ProductDetails.  # noqa: E501


        :return: The series of this ProductDetails.  # noqa: E501
        :rtype: PidVid

### `series()`

Sets the series of this ProductDetails.


        :param series: The series of this ProductDetails.  # noqa: E501
        :type: PidVid

### `manufacturer_lead_weeks()`

Gets the manufacturer_lead_weeks of this ProductDetails.  # noqa: E501

        The number of weeks expected to receive stock from manufacturer.  # noqa: E501

        :return: The manufacturer_lead_weeks of this ProductDetails.  # noqa: E501
        :rtype: str

### `manufacturer_lead_weeks()`

Sets the manufacturer_lead_weeks of this ProductDetails.

        The number of weeks expected to receive stock from manufacturer.  # noqa: E501

        :param manufacturer_lead_weeks: The manufacturer_lead_weeks of this ProductDetails.  # noqa: E501
        :type: str

### `manufacturer_page_url()`

Gets the manufacturer_page_url of this ProductDetails.  # noqa: E501

        The URL to Digi-Key's page on the manufacturer.  # noqa: E501

        :return: The manufacturer_page_url of this ProductDetails.  # noqa: E501
        :rtype: str

### `manufacturer_page_url()`

Sets the manufacturer_page_url of this ProductDetails.

        The URL to Digi-Key's page on the manufacturer.  # noqa: E501

        :param manufacturer_page_url: The manufacturer_page_url of this ProductDetails.  # noqa: E501
        :type: str

### `product_status()`

Gets the product_status of this ProductDetails.  # noqa: E501

        Status of the product. Options include: Active, Obsolete, Discontinued at Digi-Key, Last Time Buy, Not For New  Designs, Preliminary. For obsolete parts the part will become a non-stocking item when stock is depleted; minimums  will apply. Order the quantity available or the quantity available plus a multiple of the minimum order quantity.  # noqa: E501

        :return: The product_status of this ProductDetails.  # noqa: E501
        :rtype: str

### `product_status()`

Sets the product_status of this ProductDetails.

        Status of the product. Options include: Active, Obsolete, Discontinued at Digi-Key, Last Time Buy, Not For New  Designs, Preliminary. For obsolete parts the part will become a non-stocking item when stock is depleted; minimums  will apply. Order the quantity available or the quantity available plus a multiple of the minimum order quantity.  # noqa: E501

        :param product_status: The product_status of this ProductDetails.  # noqa: E501
        :type: str

### `date_last_buy_chance()`

Gets the date_last_buy_chance of this ProductDetails.  # noqa: E501

        Last date that the product will be available for purchase. Date is in ISO 8601.  # noqa: E501

        :return: The date_last_buy_chance of this ProductDetails.  # noqa: E501
        :rtype: datetime

### `date_last_buy_chance()`

Sets the date_last_buy_chance of this ProductDetails.

        Last date that the product will be available for purchase. Date is in ISO 8601.  # noqa: E501

        :param date_last_buy_chance: The date_last_buy_chance of this ProductDetails.  # noqa: E501
        :type: datetime

### `alternate_packaging()`

Gets the alternate_packaging of this ProductDetails.  # noqa: E501

        Other packaging types available for this product.  # noqa: E501

        :return: The alternate_packaging of this ProductDetails.  # noqa: E501
        :rtype: list[BasicProduct]

### `alternate_packaging()`

Sets the alternate_packaging of this ProductDetails.

        Other packaging types available for this product.  # noqa: E501

        :param alternate_packaging: The alternate_packaging of this ProductDetails.  # noqa: E501
        :type: list[BasicProduct]

### `detailed_description()`

Gets the detailed_description of this ProductDetails.  # noqa: E501

        Extended catalog description of the product.  # noqa: E501

        :return: The detailed_description of this ProductDetails.  # noqa: E501
        :rtype: str

### `detailed_description()`

Sets the detailed_description of this ProductDetails.

        Extended catalog description of the product.  # noqa: E501

        :param detailed_description: The detailed_description of this ProductDetails.  # noqa: E501
        :type: str

### `reach_status()`

Gets the reach_status of this ProductDetails.  # noqa: E501

        REACH is a regulation of the European Union. See documentation from the European Chemicals Agency.  # noqa: E501

        :return: The reach_status of this ProductDetails.  # noqa: E501
        :rtype: str

### `reach_status()`

Sets the reach_status of this ProductDetails.

        REACH is a regulation of the European Union. See documentation from the European Chemicals Agency.  # noqa: E501

        :param reach_status: The reach_status of this ProductDetails.  # noqa: E501
        :type: str

### `export_control_class_number()`

Gets the export_control_class_number of this ProductDetails.  # noqa: E501

        Export control class number. See documentation from the U.S. Department of Commerce.  # noqa: E501

        :return: The export_control_class_number of this ProductDetails.  # noqa: E501
        :rtype: str

### `export_control_class_number()`

Sets the export_control_class_number of this ProductDetails.

        Export control class number. See documentation from the U.S. Department of Commerce.  # noqa: E501

        :param export_control_class_number: The export_control_class_number of this ProductDetails.  # noqa: E501
        :type: str

### `htsus_code()`

Gets the htsus_code of this ProductDetails.  # noqa: E501

        Harmonized Tariff Schedule of the United States. See documentation from the U.S. International Trade Commission.  # noqa: E501

        :return: The htsus_code of this ProductDetails.  # noqa: E501
        :rtype: str

### `htsus_code()`

Sets the htsus_code of this ProductDetails.

        Harmonized Tariff Schedule of the United States. See documentation from the U.S. International Trade Commission.  # noqa: E501

        :param htsus_code: The htsus_code of this ProductDetails.  # noqa: E501
        :type: str

### `tariff_description()`

Gets the tariff_description of this ProductDetails.  # noqa: E501

        Description of the tariff status. Only applies if purchasing in USD and shipping to the US. Valid options are No  Tariff and Tariff Applied.  # noqa: E501

        :return: The tariff_description of this ProductDetails.  # noqa: E501
        :rtype: str

### `tariff_description()`

Sets the tariff_description of this ProductDetails.

        Description of the tariff status. Only applies if purchasing in USD and shipping to the US. Valid options are No  Tariff and Tariff Applied.  # noqa: E501

        :param tariff_description: The tariff_description of this ProductDetails.  # noqa: E501
        :type: str

### `moisture_sensitivity_level()`

Gets the moisture_sensitivity_level of this ProductDetails.  # noqa: E501

        Code for Moisture Sensitivity Level of the product  # noqa: E501

        :return: The moisture_sensitivity_level of this ProductDetails.  # noqa: E501
        :rtype: str

### `moisture_sensitivity_level()`

Sets the moisture_sensitivity_level of this ProductDetails.

        Code for Moisture Sensitivity Level of the product  # noqa: E501

        :param moisture_sensitivity_level: The moisture_sensitivity_level of this ProductDetails.  # noqa: E501
        :type: str

### `family()`

Gets the family of this ProductDetails.  # noqa: E501


        :return: The family of this ProductDetails.  # noqa: E501
        :rtype: PidVid

### `family()`

Sets the family of this ProductDetails.


        :param family: The family of this ProductDetails.  # noqa: E501
        :type: PidVid

### `category()`

Gets the category of this ProductDetails.  # noqa: E501


        :return: The category of this ProductDetails.  # noqa: E501
        :rtype: PidVid

### `category()`

Sets the category of this ProductDetails.


        :param category: The category of this ProductDetails.  # noqa: E501
        :type: PidVid

### `manufacturer_part_number()`

Gets the manufacturer_part_number of this ProductDetails.  # noqa: E501

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :return: The manufacturer_part_number of this ProductDetails.  # noqa: E501
        :rtype: str

### `manufacturer_part_number()`

Sets the manufacturer_part_number of this ProductDetails.

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :param manufacturer_part_number: The manufacturer_part_number of this ProductDetails.  # noqa: E501
        :type: str

### `minimum_order_quantity()`

Gets the minimum_order_quantity of this ProductDetails.  # noqa: E501

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :return: The minimum_order_quantity of this ProductDetails.  # noqa: E501
        :rtype: int

### `minimum_order_quantity()`

Sets the minimum_order_quantity of this ProductDetails.

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :param minimum_order_quantity: The minimum_order_quantity of this ProductDetails.  # noqa: E501
        :type: int

### `non_stock()`

Gets the non_stock of this ProductDetails.  # noqa: E501

        Indicates this product is a non stock product.  # noqa: E501

        :return: The non_stock of this ProductDetails.  # noqa: E501
        :rtype: bool

### `non_stock()`

Sets the non_stock of this ProductDetails.

        Indicates this product is a non stock product.  # noqa: E501

        :param non_stock: The non_stock of this ProductDetails.  # noqa: E501
        :type: bool

### `packaging()`

Gets the packaging of this ProductDetails.  # noqa: E501


        :return: The packaging of this ProductDetails.  # noqa: E501
        :rtype: PidVid

### `packaging()`

Sets the packaging of this ProductDetails.


        :param packaging: The packaging of this ProductDetails.  # noqa: E501
        :type: PidVid

### `quantity_available()`

Gets the quantity_available of this ProductDetails.  # noqa: E501

        Quantity of the product available for immediate sale.  # noqa: E501

        :return: The quantity_available of this ProductDetails.  # noqa: E501
        :rtype: int

### `quantity_available()`

Sets the quantity_available of this ProductDetails.

        Quantity of the product available for immediate sale.  # noqa: E501

        :param quantity_available: The quantity_available of this ProductDetails.  # noqa: E501
        :type: int

### `digi_key_part_number()`

Gets the digi_key_part_number of this ProductDetails.  # noqa: E501

        The Digi-Key part number.  # noqa: E501

        :return: The digi_key_part_number of this ProductDetails.  # noqa: E501
        :rtype: str

### `digi_key_part_number()`

Sets the digi_key_part_number of this ProductDetails.

        The Digi-Key part number.  # noqa: E501

        :param digi_key_part_number: The digi_key_part_number of this ProductDetails.  # noqa: E501
        :type: str

### `product_description()`

Gets the product_description of this ProductDetails.  # noqa: E501

        Catalog description of the product.  # noqa: E501

        :return: The product_description of this ProductDetails.  # noqa: E501
        :rtype: str

### `product_description()`

Sets the product_description of this ProductDetails.

        Catalog description of the product.  # noqa: E501

        :param product_description: The product_description of this ProductDetails.  # noqa: E501
        :type: str

### `unit_price()`

Gets the unit_price of this ProductDetails.  # noqa: E501

        The price for a single unit of this product.  # noqa: E501

        :return: The unit_price of this ProductDetails.  # noqa: E501
        :rtype: float

### `unit_price()`

Sets the unit_price of this ProductDetails.

        The price for a single unit of this product.  # noqa: E501

        :param unit_price: The unit_price of this ProductDetails.  # noqa: E501
        :type: float

### `manufacturer()`

Gets the manufacturer of this ProductDetails.  # noqa: E501


        :return: The manufacturer of this ProductDetails.  # noqa: E501
        :rtype: PidVid

### `manufacturer()`

Sets the manufacturer of this ProductDetails.


        :param manufacturer: The manufacturer of this ProductDetails.  # noqa: E501
        :type: PidVid

### `manufacturer_public_quantity()`

Gets the manufacturer_public_quantity of this ProductDetails.  # noqa: E501

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :return: The manufacturer_public_quantity of this ProductDetails.  # noqa: E501
        :rtype: int

### `manufacturer_public_quantity()`

Sets the manufacturer_public_quantity of this ProductDetails.

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :param manufacturer_public_quantity: The manufacturer_public_quantity of this ProductDetails.  # noqa: E501
        :type: int

### `quantity_on_order()`

Gets the quantity_on_order of this ProductDetails.  # noqa: E501

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :return: The quantity_on_order of this ProductDetails.  # noqa: E501
        :rtype: int

### `quantity_on_order()`

Sets the quantity_on_order of this ProductDetails.

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :param quantity_on_order: The quantity_on_order of this ProductDetails.  # noqa: E501
        :type: int

### `dk_plus_restriction()`

Gets the dk_plus_restriction of this ProductDetails.  # noqa: E501

        Deprecated property - see Marketplace  # noqa: E501

        :return: The dk_plus_restriction of this ProductDetails.  # noqa: E501
        :rtype: bool

### `dk_plus_restriction()`

Sets the dk_plus_restriction of this ProductDetails.

        Deprecated property - see Marketplace  # noqa: E501

        :param dk_plus_restriction: The dk_plus_restriction of this ProductDetails.  # noqa: E501
        :type: bool

### `marketplace()`

Gets the marketplace of this ProductDetails.  # noqa: E501

        Product is a Marketplace product that ships direct from the supplier.  A separate shipping fee may apply  # noqa: E501

        :return: The marketplace of this ProductDetails.  # noqa: E501
        :rtype: bool

### `marketplace()`

Sets the marketplace of this ProductDetails.

        Product is a Marketplace product that ships direct from the supplier.  A separate shipping fee may apply  # noqa: E501

        :param marketplace: The marketplace of this ProductDetails.  # noqa: E501
        :type: bool

### `supplier_direct_ship()`

Gets the supplier_direct_ship of this ProductDetails.  # noqa: E501

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :return: The supplier_direct_ship of this ProductDetails.  # noqa: E501
        :rtype: bool

### `supplier_direct_ship()`

Sets the supplier_direct_ship of this ProductDetails.

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :param supplier_direct_ship: The supplier_direct_ship of this ProductDetails.  # noqa: E501
        :type: bool

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `parameter_id()`

Gets the parameter_id of this ParametricFilter.  # noqa: E501

        The parameter identifier.  # noqa: E501

        :return: The parameter_id of this ParametricFilter.  # noqa: E501
        :rtype: int

### `parameter_id()`

Sets the parameter_id of this ParametricFilter.

        The parameter identifier.  # noqa: E501

        :param parameter_id: The parameter_id of this ParametricFilter.  # noqa: E501
        :type: int

### `value_id()`

Gets the value_id of this ParametricFilter.  # noqa: E501

        The value identifier.  # noqa: E501

        :return: The value_id of this ParametricFilter.  # noqa: E501
        :rtype: str

### `value_id()`

Sets the value_id of this ParametricFilter.

        The value identifier.  # noqa: E501

        :param value_id: The value_id of this ParametricFilter.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `associated_product()`

Gets the associated_product of this KitPart.  # noqa: E501


        :return: The associated_product of this KitPart.  # noqa: E501
        :rtype: AssociatedProduct

### `associated_product()`

Sets the associated_product of this KitPart.


        :param associated_product: The associated_product of this KitPart.  # noqa: E501
        :type: AssociatedProduct

### `kit_part_quantity()`

Gets the kit_part_quantity of this KitPart.  # noqa: E501

        Number of the product in the Kit.  # noqa: E501

        :return: The kit_part_quantity of this KitPart.  # noqa: E501
        :rtype: int

### `kit_part_quantity()`

Sets the kit_part_quantity of this KitPart.

        Number of the product in the Kit.  # noqa: E501

        :param kit_part_quantity: The kit_part_quantity of this KitPart.  # noqa: E501
        :type: int

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `product_url()`

Gets the product_url of this AssociatedProduct.  # noqa: E501

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :return: The product_url of this AssociatedProduct.  # noqa: E501
        :rtype: str

### `product_url()`

Sets the product_url of this AssociatedProduct.

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :param product_url: The product_url of this AssociatedProduct.  # noqa: E501
        :type: str

### `manufacturer_part_number()`

Gets the manufacturer_part_number of this AssociatedProduct.  # noqa: E501

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :return: The manufacturer_part_number of this AssociatedProduct.  # noqa: E501
        :rtype: str

### `manufacturer_part_number()`

Sets the manufacturer_part_number of this AssociatedProduct.

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :param manufacturer_part_number: The manufacturer_part_number of this AssociatedProduct.  # noqa: E501
        :type: str

### `minimum_order_quantity()`

Gets the minimum_order_quantity of this AssociatedProduct.  # noqa: E501

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :return: The minimum_order_quantity of this AssociatedProduct.  # noqa: E501
        :rtype: int

### `minimum_order_quantity()`

Sets the minimum_order_quantity of this AssociatedProduct.

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :param minimum_order_quantity: The minimum_order_quantity of this AssociatedProduct.  # noqa: E501
        :type: int

### `non_stock()`

Gets the non_stock of this AssociatedProduct.  # noqa: E501

        Indicates this product is a non stock product.  # noqa: E501

        :return: The non_stock of this AssociatedProduct.  # noqa: E501
        :rtype: bool

### `non_stock()`

Sets the non_stock of this AssociatedProduct.

        Indicates this product is a non stock product.  # noqa: E501

        :param non_stock: The non_stock of this AssociatedProduct.  # noqa: E501
        :type: bool

### `packaging()`

Gets the packaging of this AssociatedProduct.  # noqa: E501


        :return: The packaging of this AssociatedProduct.  # noqa: E501
        :rtype: PidVid

### `packaging()`

Sets the packaging of this AssociatedProduct.


        :param packaging: The packaging of this AssociatedProduct.  # noqa: E501
        :type: PidVid

### `quantity_available()`

Gets the quantity_available of this AssociatedProduct.  # noqa: E501

        Quantity of the product available for immediate sale.  # noqa: E501

        :return: The quantity_available of this AssociatedProduct.  # noqa: E501
        :rtype: int

### `quantity_available()`

Sets the quantity_available of this AssociatedProduct.

        Quantity of the product available for immediate sale.  # noqa: E501

        :param quantity_available: The quantity_available of this AssociatedProduct.  # noqa: E501
        :type: int

### `digi_key_part_number()`

Gets the digi_key_part_number of this AssociatedProduct.  # noqa: E501

        The Digi-Key part number.  # noqa: E501

        :return: The digi_key_part_number of this AssociatedProduct.  # noqa: E501
        :rtype: str

### `digi_key_part_number()`

Sets the digi_key_part_number of this AssociatedProduct.

        The Digi-Key part number.  # noqa: E501

        :param digi_key_part_number: The digi_key_part_number of this AssociatedProduct.  # noqa: E501
        :type: str

### `product_description()`

Gets the product_description of this AssociatedProduct.  # noqa: E501

        Catalog description of the product.  # noqa: E501

        :return: The product_description of this AssociatedProduct.  # noqa: E501
        :rtype: str

### `product_description()`

Sets the product_description of this AssociatedProduct.

        Catalog description of the product.  # noqa: E501

        :param product_description: The product_description of this AssociatedProduct.  # noqa: E501
        :type: str

### `unit_price()`

Gets the unit_price of this AssociatedProduct.  # noqa: E501

        The price for a single unit of this product.  # noqa: E501

        :return: The unit_price of this AssociatedProduct.  # noqa: E501
        :rtype: float

### `unit_price()`

Sets the unit_price of this AssociatedProduct.

        The price for a single unit of this product.  # noqa: E501

        :param unit_price: The unit_price of this AssociatedProduct.  # noqa: E501
        :type: float

### `manufacturer()`

Gets the manufacturer of this AssociatedProduct.  # noqa: E501


        :return: The manufacturer of this AssociatedProduct.  # noqa: E501
        :rtype: PidVid

### `manufacturer()`

Sets the manufacturer of this AssociatedProduct.


        :param manufacturer: The manufacturer of this AssociatedProduct.  # noqa: E501
        :type: PidVid

### `manufacturer_public_quantity()`

Gets the manufacturer_public_quantity of this AssociatedProduct.  # noqa: E501

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :return: The manufacturer_public_quantity of this AssociatedProduct.  # noqa: E501
        :rtype: int

### `manufacturer_public_quantity()`

Sets the manufacturer_public_quantity of this AssociatedProduct.

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :param manufacturer_public_quantity: The manufacturer_public_quantity of this AssociatedProduct.  # noqa: E501
        :type: int

### `quantity_on_order()`

Gets the quantity_on_order of this AssociatedProduct.  # noqa: E501

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :return: The quantity_on_order of this AssociatedProduct.  # noqa: E501
        :rtype: int

### `quantity_on_order()`

Sets the quantity_on_order of this AssociatedProduct.

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :param quantity_on_order: The quantity_on_order of this AssociatedProduct.  # noqa: E501
        :type: int

### `dk_plus_restriction()`

Gets the dk_plus_restriction of this AssociatedProduct.  # noqa: E501

        Deprecated property - see Marketplace  # noqa: E501

        :return: The dk_plus_restriction of this AssociatedProduct.  # noqa: E501
        :rtype: bool

### `dk_plus_restriction()`

Sets the dk_plus_restriction of this AssociatedProduct.

        Deprecated property - see Marketplace  # noqa: E501

        :param dk_plus_restriction: The dk_plus_restriction of this AssociatedProduct.  # noqa: E501
        :type: bool

### `marketplace()`

Gets the marketplace of this AssociatedProduct.  # noqa: E501

        Product is a Marketplace product that ships direct from the supplier.  A separate shipping fee may apply  # noqa: E501

        :return: The marketplace of this AssociatedProduct.  # noqa: E501
        :rtype: bool

### `marketplace()`

Sets the marketplace of this AssociatedProduct.

        Product is a Marketplace product that ships direct from the supplier.  A separate shipping fee may apply  # noqa: E501

        :param marketplace: The marketplace of this AssociatedProduct.  # noqa: E501
        :type: bool

### `supplier_direct_ship()`

Gets the supplier_direct_ship of this AssociatedProduct.  # noqa: E501

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :return: The supplier_direct_ship of this AssociatedProduct.  # noqa: E501
        :rtype: bool

### `supplier_direct_ship()`

Sets the supplier_direct_ship of this AssociatedProduct.

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :param supplier_direct_ship: The supplier_direct_ship of this AssociatedProduct.  # noqa: E501
        :type: bool

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `values()`

Gets the values of this LimitedParameter.  # noqa: E501

        List of values for the parameter that are contained in the products.  # noqa: E501

        :return: The values of this LimitedParameter.  # noqa: E501
        :rtype: list[ValuePair]

### `values()`

Sets the values of this LimitedParameter.

        List of values for the parameter that are contained in the products.  # noqa: E501

        :param values: The values of this LimitedParameter.  # noqa: E501
        :type: list[ValuePair]

### `parameter_id()`

Gets the parameter_id of this LimitedParameter.  # noqa: E501

        The Id of the parameter.  # noqa: E501

        :return: The parameter_id of this LimitedParameter.  # noqa: E501
        :rtype: int

### `parameter_id()`

Sets the parameter_id of this LimitedParameter.

        The Id of the parameter.  # noqa: E501

        :param parameter_id: The parameter_id of this LimitedParameter.  # noqa: E501
        :type: int

### `parameter()`

Gets the parameter of this LimitedParameter.  # noqa: E501

        The name of the parameter.  # noqa: E501

        :return: The parameter of this LimitedParameter.  # noqa: E501
        :rtype: str

### `parameter()`

Sets the parameter of this LimitedParameter.

        The name of the parameter.  # noqa: E501

        :param parameter: The parameter of this LimitedParameter.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `keywords()`

Gets the keywords of this KeywordSearchRequest.  # noqa: E501

        Keywords to search on. Can be a description, partial part number, manufacturer part number, or a Digi-Key part number.  # noqa: E501

        :return: The keywords of this KeywordSearchRequest.  # noqa: E501
        :rtype: str

### `keywords()`

Sets the keywords of this KeywordSearchRequest.

        Keywords to search on. Can be a description, partial part number, manufacturer part number, or a Digi-Key part number.  # noqa: E501

        :param keywords: The keywords of this KeywordSearchRequest.  # noqa: E501
        :type: str

### `record_count()`

Gets the record_count of this KeywordSearchRequest.  # noqa: E501

        Number of products to return between 1 and 50.  # noqa: E501

        :return: The record_count of this KeywordSearchRequest.  # noqa: E501
        :rtype: int

### `record_count()`

Sets the record_count of this KeywordSearchRequest.

        Number of products to return between 1 and 50.  # noqa: E501

        :param record_count: The record_count of this KeywordSearchRequest.  # noqa: E501
        :type: int

### `record_start_position()`

Gets the record_start_position of this KeywordSearchRequest.  # noqa: E501

        The starting index of the records returned. This is used to paginate beyond 50 results.  # noqa: E501

        :return: The record_start_position of this KeywordSearchRequest.  # noqa: E501
        :rtype: int

### `record_start_position()`

Sets the record_start_position of this KeywordSearchRequest.

        The starting index of the records returned. This is used to paginate beyond 50 results.  # noqa: E501

        :param record_start_position: The record_start_position of this KeywordSearchRequest.  # noqa: E501
        :type: int

### `filters()`

Gets the filters of this KeywordSearchRequest.  # noqa: E501


        :return: The filters of this KeywordSearchRequest.  # noqa: E501
        :rtype: Filters

### `filters()`

Sets the filters of this KeywordSearchRequest.


        :param filters: The filters of this KeywordSearchRequest.  # noqa: E501
        :type: Filters

### `sort()`

Gets the sort of this KeywordSearchRequest.  # noqa: E501


        :return: The sort of this KeywordSearchRequest.  # noqa: E501
        :rtype: SortParameters

### `sort()`

Sets the sort of this KeywordSearchRequest.


        :param sort: The sort of this KeywordSearchRequest.  # noqa: E501
        :type: SortParameters

### `requested_quantity()`

Gets the requested_quantity of this KeywordSearchRequest.  # noqa: E501

        The quantity of the product you are looking to purchase. This is used with the SortByUnitPrice SortOption as price varies at differing quantities.  # noqa: E501

        :return: The requested_quantity of this KeywordSearchRequest.  # noqa: E501
        :rtype: int

### `requested_quantity()`

Sets the requested_quantity of this KeywordSearchRequest.

        The quantity of the product you are looking to purchase. This is used with the SortByUnitPrice SortOption as price varies at differing quantities.  # noqa: E501

        :param requested_quantity: The requested_quantity of this KeywordSearchRequest.  # noqa: E501
        :type: int

### `search_options()`

Gets the search_options of this KeywordSearchRequest.  # noqa: E501

        Filters the search results by the included SearchOption.  # noqa: E501

        :return: The search_options of this KeywordSearchRequest.  # noqa: E501
        :rtype: list[SearchOption]

### `search_options()`

Sets the search_options of this KeywordSearchRequest.

        Filters the search results by the included SearchOption.  # noqa: E501

        :param search_options: The search_options of this KeywordSearchRequest.  # noqa: E501
        :type: list[SearchOption]

### `exclude_market_place_products()`

Gets the exclude_market_place_products of this KeywordSearchRequest.  # noqa: E501

        Used to exclude MarkPlace products from search results. Default is false  # noqa: E501

        :return: The exclude_market_place_products of this KeywordSearchRequest.  # noqa: E501
        :rtype: bool

### `exclude_market_place_products()`

Sets the exclude_market_place_products of this KeywordSearchRequest.

        Used to exclude MarkPlace products from search results. Default is false  # noqa: E501

        :param exclude_market_place_products: The exclude_market_place_products of this KeywordSearchRequest.  # noqa: E501
        :type: bool

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `manufacturer_part_number()`

Gets the manufacturer_part_number of this BasicProduct.  # noqa: E501

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :return: The manufacturer_part_number of this BasicProduct.  # noqa: E501
        :rtype: str

### `manufacturer_part_number()`

Sets the manufacturer_part_number of this BasicProduct.

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :param manufacturer_part_number: The manufacturer_part_number of this BasicProduct.  # noqa: E501
        :type: str

### `minimum_order_quantity()`

Gets the minimum_order_quantity of this BasicProduct.  # noqa: E501

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :return: The minimum_order_quantity of this BasicProduct.  # noqa: E501
        :rtype: int

### `minimum_order_quantity()`

Sets the minimum_order_quantity of this BasicProduct.

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :param minimum_order_quantity: The minimum_order_quantity of this BasicProduct.  # noqa: E501
        :type: int

### `non_stock()`

Gets the non_stock of this BasicProduct.  # noqa: E501

        Indicates this product is a non stock product.  # noqa: E501

        :return: The non_stock of this BasicProduct.  # noqa: E501
        :rtype: bool

### `non_stock()`

Sets the non_stock of this BasicProduct.

        Indicates this product is a non stock product.  # noqa: E501

        :param non_stock: The non_stock of this BasicProduct.  # noqa: E501
        :type: bool

### `packaging()`

Gets the packaging of this BasicProduct.  # noqa: E501


        :return: The packaging of this BasicProduct.  # noqa: E501
        :rtype: PidVid

### `packaging()`

Sets the packaging of this BasicProduct.


        :param packaging: The packaging of this BasicProduct.  # noqa: E501
        :type: PidVid

### `quantity_available()`

Gets the quantity_available of this BasicProduct.  # noqa: E501

        Quantity of the product available for immediate sale.  # noqa: E501

        :return: The quantity_available of this BasicProduct.  # noqa: E501
        :rtype: int

### `quantity_available()`

Sets the quantity_available of this BasicProduct.

        Quantity of the product available for immediate sale.  # noqa: E501

        :param quantity_available: The quantity_available of this BasicProduct.  # noqa: E501
        :type: int

### `digi_key_part_number()`

Gets the digi_key_part_number of this BasicProduct.  # noqa: E501

        The Digi-Key part number.  # noqa: E501

        :return: The digi_key_part_number of this BasicProduct.  # noqa: E501
        :rtype: str

### `digi_key_part_number()`

Sets the digi_key_part_number of this BasicProduct.

        The Digi-Key part number.  # noqa: E501

        :param digi_key_part_number: The digi_key_part_number of this BasicProduct.  # noqa: E501
        :type: str

### `product_description()`

Gets the product_description of this BasicProduct.  # noqa: E501

        Catalog description of the product.  # noqa: E501

        :return: The product_description of this BasicProduct.  # noqa: E501
        :rtype: str

### `product_description()`

Sets the product_description of this BasicProduct.

        Catalog description of the product.  # noqa: E501

        :param product_description: The product_description of this BasicProduct.  # noqa: E501
        :type: str

### `unit_price()`

Gets the unit_price of this BasicProduct.  # noqa: E501

        The price for a single unit of this product.  # noqa: E501

        :return: The unit_price of this BasicProduct.  # noqa: E501
        :rtype: float

### `unit_price()`

Sets the unit_price of this BasicProduct.

        The price for a single unit of this product.  # noqa: E501

        :param unit_price: The unit_price of this BasicProduct.  # noqa: E501
        :type: float

### `manufacturer()`

Gets the manufacturer of this BasicProduct.  # noqa: E501


        :return: The manufacturer of this BasicProduct.  # noqa: E501
        :rtype: PidVid

### `manufacturer()`

Sets the manufacturer of this BasicProduct.


        :param manufacturer: The manufacturer of this BasicProduct.  # noqa: E501
        :type: PidVid

### `manufacturer_public_quantity()`

Gets the manufacturer_public_quantity of this BasicProduct.  # noqa: E501

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :return: The manufacturer_public_quantity of this BasicProduct.  # noqa: E501
        :rtype: int

### `manufacturer_public_quantity()`

Sets the manufacturer_public_quantity of this BasicProduct.

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :param manufacturer_public_quantity: The manufacturer_public_quantity of this BasicProduct.  # noqa: E501
        :type: int

### `quantity_on_order()`

Gets the quantity_on_order of this BasicProduct.  # noqa: E501

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :return: The quantity_on_order of this BasicProduct.  # noqa: E501
        :rtype: int

### `quantity_on_order()`

Sets the quantity_on_order of this BasicProduct.

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :param quantity_on_order: The quantity_on_order of this BasicProduct.  # noqa: E501
        :type: int

### `dk_plus_restriction()`

Gets the dk_plus_restriction of this BasicProduct.  # noqa: E501

        Deprecated property - see Marketplace  # noqa: E501

        :return: The dk_plus_restriction of this BasicProduct.  # noqa: E501
        :rtype: bool

### `dk_plus_restriction()`

Sets the dk_plus_restriction of this BasicProduct.

        Deprecated property - see Marketplace  # noqa: E501

        :param dk_plus_restriction: The dk_plus_restriction of this BasicProduct.  # noqa: E501
        :type: bool

### `marketplace()`

Gets the marketplace of this BasicProduct.  # noqa: E501

        Product is a Marketplace product that ships direct from the supplier.  A separate shipping fee may apply  # noqa: E501

        :return: The marketplace of this BasicProduct.  # noqa: E501
        :rtype: bool

### `marketplace()`

Sets the marketplace of this BasicProduct.

        Product is a Marketplace product that ships direct from the supplier.  A separate shipping fee may apply  # noqa: E501

        :param marketplace: The marketplace of this BasicProduct.  # noqa: E501
        :type: bool

### `supplier_direct_ship()`

Gets the supplier_direct_ship of this BasicProduct.  # noqa: E501

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :return: The supplier_direct_ship of this BasicProduct.  # noqa: E501
        :rtype: bool

### `supplier_direct_ship()`

Sets the supplier_direct_ship of this BasicProduct.

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :param supplier_direct_ship: The supplier_direct_ship of this BasicProduct.  # noqa: E501
        :type: bool

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `media_type()`

Gets the media_type of this MediaLinks.  # noqa: E501

        The type of media.  # noqa: E501

        :return: The media_type of this MediaLinks.  # noqa: E501
        :rtype: str

### `media_type()`

Sets the media_type of this MediaLinks.

        The type of media.  # noqa: E501

        :param media_type: The media_type of this MediaLinks.  # noqa: E501
        :type: str

### `title()`

Gets the title of this MediaLinks.  # noqa: E501

        The title of the media.  # noqa: E501

        :return: The title of this MediaLinks.  # noqa: E501
        :rtype: str

### `title()`

Sets the title of this MediaLinks.

        The title of the media.  # noqa: E501

        :param title: The title of this MediaLinks.  # noqa: E501
        :type: str

### `small_photo()`

Gets the small_photo of this MediaLinks.  # noqa: E501

        URL to a small photo.  # noqa: E501

        :return: The small_photo of this MediaLinks.  # noqa: E501
        :rtype: str

### `small_photo()`

Sets the small_photo of this MediaLinks.

        URL to a small photo.  # noqa: E501

        :param small_photo: The small_photo of this MediaLinks.  # noqa: E501
        :type: str

### `thumbnail()`

Gets the thumbnail of this MediaLinks.  # noqa: E501

        URL to the thumbnail image of the media.  # noqa: E501

        :return: The thumbnail of this MediaLinks.  # noqa: E501
        :rtype: str

### `thumbnail()`

Sets the thumbnail of this MediaLinks.

        URL to the thumbnail image of the media.  # noqa: E501

        :param thumbnail: The thumbnail of this MediaLinks.  # noqa: E501
        :type: str

### `url()`

Gets the url of this MediaLinks.  # noqa: E501

        URL of the media.  # noqa: E501

        :return: The url of this MediaLinks.  # noqa: E501
        :rtype: str

### `url()`

Sets the url of this MediaLinks.

        URL of the media.  # noqa: E501

        :param url: The url of this MediaLinks.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `standard_pricing()`

Gets the standard_pricing of this Product.  # noqa: E501

        Standard pricing for the validated locale.  # noqa: E501

        :return: The standard_pricing of this Product.  # noqa: E501
        :rtype: list[PriceBreak]

### `standard_pricing()`

Sets the standard_pricing of this Product.

        Standard pricing for the validated locale.  # noqa: E501

        :param standard_pricing: The standard_pricing of this Product.  # noqa: E501
        :type: list[PriceBreak]

### `ro_hs_status()`

Gets the ro_hs_status of this Product.  # noqa: E501

        RoHS status. Can be: RoHS Compliant, RoHS non-compliant, RoHS Compliant By Exemption, Not Applicable, Vendor  undefined, Request Inventory Verification, ROHS3 Compliant.  # noqa: E501

        :return: The ro_hs_status of this Product.  # noqa: E501
        :rtype: str

### `ro_hs_status()`

Sets the ro_hs_status of this Product.

        RoHS status. Can be: RoHS Compliant, RoHS non-compliant, RoHS Compliant By Exemption, Not Applicable, Vendor  undefined, Request Inventory Verification, ROHS3 Compliant.  # noqa: E501

        :param ro_hs_status: The ro_hs_status of this Product.  # noqa: E501
        :type: str

### `lead_status()`

Gets the lead_status of this Product.  # noqa: E501

        Lead status. Can be: Lead Free, Contains lead, Lead Free By Exemption, Not Applicable, Vendor undefined, unknown,  or Request Inventory Verification.  # noqa: E501

        :return: The lead_status of this Product.  # noqa: E501
        :rtype: str

### `lead_status()`

Sets the lead_status of this Product.

        Lead status. Can be: Lead Free, Contains lead, Lead Free By Exemption, Not Applicable, Vendor undefined, unknown,  or Request Inventory Verification.  # noqa: E501

        :param lead_status: The lead_status of this Product.  # noqa: E501
        :type: str

### `parameters()`

Gets the parameters of this Product.  # noqa: E501

        Parameters for the part. Can be used for filtering keyword searches.  # noqa: E501

        :return: The parameters of this Product.  # noqa: E501
        :rtype: list[PidVid]

### `parameters()`

Sets the parameters of this Product.

        Parameters for the part. Can be used for filtering keyword searches.  # noqa: E501

        :param parameters: The parameters of this Product.  # noqa: E501
        :type: list[PidVid]

### `product_url()`

Gets the product_url of this Product.  # noqa: E501

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :return: The product_url of this Product.  # noqa: E501
        :rtype: str

### `product_url()`

Sets the product_url of this Product.

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :param product_url: The product_url of this Product.  # noqa: E501
        :type: str

### `primary_datasheet()`

Gets the primary_datasheet of this Product.  # noqa: E501

        The URL to the product's datasheet.  # noqa: E501

        :return: The primary_datasheet of this Product.  # noqa: E501
        :rtype: str

### `primary_datasheet()`

Sets the primary_datasheet of this Product.

        The URL to the product's datasheet.  # noqa: E501

        :param primary_datasheet: The primary_datasheet of this Product.  # noqa: E501
        :type: str

### `primary_photo()`

Gets the primary_photo of this Product.  # noqa: E501

        The URL to the product's image.  # noqa: E501

        :return: The primary_photo of this Product.  # noqa: E501
        :rtype: str

### `primary_photo()`

Sets the primary_photo of this Product.

        The URL to the product's image.  # noqa: E501

        :param primary_photo: The primary_photo of this Product.  # noqa: E501
        :type: str

### `primary_video()`

Gets the primary_video of this Product.  # noqa: E501

        The URL to the product's video.  # noqa: E501

        :return: The primary_video of this Product.  # noqa: E501
        :rtype: str

### `primary_video()`

Sets the primary_video of this Product.

        The URL to the product's video.  # noqa: E501

        :param primary_video: The primary_video of this Product.  # noqa: E501
        :type: str

### `series()`

Gets the series of this Product.  # noqa: E501


        :return: The series of this Product.  # noqa: E501
        :rtype: PidVid

### `series()`

Sets the series of this Product.


        :param series: The series of this Product.  # noqa: E501
        :type: PidVid

### `manufacturer_lead_weeks()`

Gets the manufacturer_lead_weeks of this Product.  # noqa: E501

        The number of weeks expected to receive stock from manufacturer.  # noqa: E501

        :return: The manufacturer_lead_weeks of this Product.  # noqa: E501
        :rtype: str

### `manufacturer_lead_weeks()`

Sets the manufacturer_lead_weeks of this Product.

        The number of weeks expected to receive stock from manufacturer.  # noqa: E501

        :param manufacturer_lead_weeks: The manufacturer_lead_weeks of this Product.  # noqa: E501
        :type: str

### `manufacturer_page_url()`

Gets the manufacturer_page_url of this Product.  # noqa: E501

        The URL to Digi-Key's page on the manufacturer.  # noqa: E501

        :return: The manufacturer_page_url of this Product.  # noqa: E501
        :rtype: str

### `manufacturer_page_url()`

Sets the manufacturer_page_url of this Product.

        The URL to Digi-Key's page on the manufacturer.  # noqa: E501

        :param manufacturer_page_url: The manufacturer_page_url of this Product.  # noqa: E501
        :type: str

### `product_status()`

Gets the product_status of this Product.  # noqa: E501

        Status of the product. Options include: Active, Obsolete, Discontinued at Digi-Key, Last Time Buy, Not For New  Designs, Preliminary. For obsolete parts the part will become a non-stocking item when stock is depleted; minimums  will apply. Order the quantity available or the quantity available plus a multiple of the minimum order quantity.  # noqa: E501

        :return: The product_status of this Product.  # noqa: E501
        :rtype: str

### `product_status()`

Sets the product_status of this Product.

        Status of the product. Options include: Active, Obsolete, Discontinued at Digi-Key, Last Time Buy, Not For New  Designs, Preliminary. For obsolete parts the part will become a non-stocking item when stock is depleted; minimums  will apply. Order the quantity available or the quantity available plus a multiple of the minimum order quantity.  # noqa: E501

        :param product_status: The product_status of this Product.  # noqa: E501
        :type: str

### `date_last_buy_chance()`

Gets the date_last_buy_chance of this Product.  # noqa: E501

        Last date that the product will be available for purchase. Date is in ISO 8601.  # noqa: E501

        :return: The date_last_buy_chance of this Product.  # noqa: E501
        :rtype: datetime

### `date_last_buy_chance()`

Sets the date_last_buy_chance of this Product.

        Last date that the product will be available for purchase. Date is in ISO 8601.  # noqa: E501

        :param date_last_buy_chance: The date_last_buy_chance of this Product.  # noqa: E501
        :type: datetime

### `alternate_packaging()`

Gets the alternate_packaging of this Product.  # noqa: E501

        Other packaging types available for this product.  # noqa: E501

        :return: The alternate_packaging of this Product.  # noqa: E501
        :rtype: list[BasicProduct]

### `alternate_packaging()`

Sets the alternate_packaging of this Product.

        Other packaging types available for this product.  # noqa: E501

        :param alternate_packaging: The alternate_packaging of this Product.  # noqa: E501
        :type: list[BasicProduct]

### `detailed_description()`

Gets the detailed_description of this Product.  # noqa: E501

        Extended catalog description of the product.  # noqa: E501

        :return: The detailed_description of this Product.  # noqa: E501
        :rtype: str

### `detailed_description()`

Sets the detailed_description of this Product.

        Extended catalog description of the product.  # noqa: E501

        :param detailed_description: The detailed_description of this Product.  # noqa: E501
        :type: str

### `reach_status()`

Gets the reach_status of this Product.  # noqa: E501

        REACH is a regulation of the European Union. See documentation from the European Chemicals Agency.  # noqa: E501

        :return: The reach_status of this Product.  # noqa: E501
        :rtype: str

### `reach_status()`

Sets the reach_status of this Product.

        REACH is a regulation of the European Union. See documentation from the European Chemicals Agency.  # noqa: E501

        :param reach_status: The reach_status of this Product.  # noqa: E501
        :type: str

### `export_control_class_number()`

Gets the export_control_class_number of this Product.  # noqa: E501

        Export control class number. See documentation from the U.S. Department of Commerce.  # noqa: E501

        :return: The export_control_class_number of this Product.  # noqa: E501
        :rtype: str

### `export_control_class_number()`

Sets the export_control_class_number of this Product.

        Export control class number. See documentation from the U.S. Department of Commerce.  # noqa: E501

        :param export_control_class_number: The export_control_class_number of this Product.  # noqa: E501
        :type: str

### `htsus_code()`

Gets the htsus_code of this Product.  # noqa: E501

        Harmonized Tariff Schedule of the United States. See documentation from the U.S. International Trade Commission.  # noqa: E501

        :return: The htsus_code of this Product.  # noqa: E501
        :rtype: str

### `htsus_code()`

Sets the htsus_code of this Product.

        Harmonized Tariff Schedule of the United States. See documentation from the U.S. International Trade Commission.  # noqa: E501

        :param htsus_code: The htsus_code of this Product.  # noqa: E501
        :type: str

### `tariff_description()`

Gets the tariff_description of this Product.  # noqa: E501

        Description of the tariff status. Only applies if purchasing in USD and shipping to the US. Valid options are No  Tariff and Tariff Applied.  # noqa: E501

        :return: The tariff_description of this Product.  # noqa: E501
        :rtype: str

### `tariff_description()`

Sets the tariff_description of this Product.

        Description of the tariff status. Only applies if purchasing in USD and shipping to the US. Valid options are No  Tariff and Tariff Applied.  # noqa: E501

        :param tariff_description: The tariff_description of this Product.  # noqa: E501
        :type: str

### `moisture_sensitivity_level()`

Gets the moisture_sensitivity_level of this Product.  # noqa: E501

        Code for Moisture Sensitivity Level of the product  # noqa: E501

        :return: The moisture_sensitivity_level of this Product.  # noqa: E501
        :rtype: str

### `moisture_sensitivity_level()`

Sets the moisture_sensitivity_level of this Product.

        Code for Moisture Sensitivity Level of the product  # noqa: E501

        :param moisture_sensitivity_level: The moisture_sensitivity_level of this Product.  # noqa: E501
        :type: str

### `family()`

Gets the family of this Product.  # noqa: E501


        :return: The family of this Product.  # noqa: E501
        :rtype: PidVid

### `family()`

Sets the family of this Product.


        :param family: The family of this Product.  # noqa: E501
        :type: PidVid

### `category()`

Gets the category of this Product.  # noqa: E501


        :return: The category of this Product.  # noqa: E501
        :rtype: PidVid

### `category()`

Sets the category of this Product.


        :param category: The category of this Product.  # noqa: E501
        :type: PidVid

### `manufacturer_part_number()`

Gets the manufacturer_part_number of this Product.  # noqa: E501

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :return: The manufacturer_part_number of this Product.  # noqa: E501
        :rtype: str

### `manufacturer_part_number()`

Sets the manufacturer_part_number of this Product.

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :param manufacturer_part_number: The manufacturer_part_number of this Product.  # noqa: E501
        :type: str

### `minimum_order_quantity()`

Gets the minimum_order_quantity of this Product.  # noqa: E501

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :return: The minimum_order_quantity of this Product.  # noqa: E501
        :rtype: int

### `minimum_order_quantity()`

Sets the minimum_order_quantity of this Product.

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :param minimum_order_quantity: The minimum_order_quantity of this Product.  # noqa: E501
        :type: int

### `non_stock()`

Gets the non_stock of this Product.  # noqa: E501

        Indicates this product is a non stock product.  # noqa: E501

        :return: The non_stock of this Product.  # noqa: E501
        :rtype: bool

### `non_stock()`

Sets the non_stock of this Product.

        Indicates this product is a non stock product.  # noqa: E501

        :param non_stock: The non_stock of this Product.  # noqa: E501
        :type: bool

### `packaging()`

Gets the packaging of this Product.  # noqa: E501


        :return: The packaging of this Product.  # noqa: E501
        :rtype: PidVid

### `packaging()`

Sets the packaging of this Product.


        :param packaging: The packaging of this Product.  # noqa: E501
        :type: PidVid

### `quantity_available()`

Gets the quantity_available of this Product.  # noqa: E501

        Quantity of the product available for immediate sale.  # noqa: E501

        :return: The quantity_available of this Product.  # noqa: E501
        :rtype: int

### `quantity_available()`

Sets the quantity_available of this Product.

        Quantity of the product available for immediate sale.  # noqa: E501

        :param quantity_available: The quantity_available of this Product.  # noqa: E501
        :type: int

### `digi_key_part_number()`

Gets the digi_key_part_number of this Product.  # noqa: E501

        The Digi-Key part number.  # noqa: E501

        :return: The digi_key_part_number of this Product.  # noqa: E501
        :rtype: str

### `digi_key_part_number()`

Sets the digi_key_part_number of this Product.

        The Digi-Key part number.  # noqa: E501

        :param digi_key_part_number: The digi_key_part_number of this Product.  # noqa: E501
        :type: str

### `product_description()`

Gets the product_description of this Product.  # noqa: E501

        Catalog description of the product.  # noqa: E501

        :return: The product_description of this Product.  # noqa: E501
        :rtype: str

### `product_description()`

Sets the product_description of this Product.

        Catalog description of the product.  # noqa: E501

        :param product_description: The product_description of this Product.  # noqa: E501
        :type: str

### `unit_price()`

Gets the unit_price of this Product.  # noqa: E501

        The price for a single unit of this product.  # noqa: E501

        :return: The unit_price of this Product.  # noqa: E501
        :rtype: float

### `unit_price()`

Sets the unit_price of this Product.

        The price for a single unit of this product.  # noqa: E501

        :param unit_price: The unit_price of this Product.  # noqa: E501
        :type: float

### `manufacturer()`

Gets the manufacturer of this Product.  # noqa: E501


        :return: The manufacturer of this Product.  # noqa: E501
        :rtype: PidVid

### `manufacturer()`

Sets the manufacturer of this Product.


        :param manufacturer: The manufacturer of this Product.  # noqa: E501
        :type: PidVid

### `manufacturer_public_quantity()`

Gets the manufacturer_public_quantity of this Product.  # noqa: E501

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :return: The manufacturer_public_quantity of this Product.  # noqa: E501
        :rtype: int

### `manufacturer_public_quantity()`

Sets the manufacturer_public_quantity of this Product.

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :param manufacturer_public_quantity: The manufacturer_public_quantity of this Product.  # noqa: E501
        :type: int

### `quantity_on_order()`

Gets the quantity_on_order of this Product.  # noqa: E501

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :return: The quantity_on_order of this Product.  # noqa: E501
        :rtype: int

### `quantity_on_order()`

Sets the quantity_on_order of this Product.

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :param quantity_on_order: The quantity_on_order of this Product.  # noqa: E501
        :type: int

### `dk_plus_restriction()`

Gets the dk_plus_restriction of this Product.  # noqa: E501

        Deprecated property - see Marketplace  # noqa: E501

        :return: The dk_plus_restriction of this Product.  # noqa: E501
        :rtype: bool

### `dk_plus_restriction()`

Sets the dk_plus_restriction of this Product.

        Deprecated property - see Marketplace  # noqa: E501

        :param dk_plus_restriction: The dk_plus_restriction of this Product.  # noqa: E501
        :type: bool

### `marketplace()`

Gets the marketplace of this Product.  # noqa: E501

        Product is a Marketplace product that ships direct from the supplier.  A separate shipping fee may apply  # noqa: E501

        :return: The marketplace of this Product.  # noqa: E501
        :rtype: bool

### `marketplace()`

Sets the marketplace of this Product.

        Product is a Marketplace product that ships direct from the supplier.  A separate shipping fee may apply  # noqa: E501

        :param marketplace: The marketplace of this Product.  # noqa: E501
        :type: bool

### `supplier_direct_ship()`

Gets the supplier_direct_ship of this Product.  # noqa: E501

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :return: The supplier_direct_ship of this Product.  # noqa: E501
        :rtype: bool

### `supplier_direct_ship()`

Sets the supplier_direct_ship of this Product.

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :param supplier_direct_ship: The supplier_direct_ship of this Product.  # noqa: E501
        :type: bool

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `break_quantity()`

Gets the break_quantity of this PriceBreak.  # noqa: E501

        Price tiers based on the available quantities of the product.  # noqa: E501

        :return: The break_quantity of this PriceBreak.  # noqa: E501
        :rtype: int

### `break_quantity()`

Sets the break_quantity of this PriceBreak.

        Price tiers based on the available quantities of the product.  # noqa: E501

        :param break_quantity: The break_quantity of this PriceBreak.  # noqa: E501
        :type: int

### `unit_price()`

Gets the unit_price of this PriceBreak.  # noqa: E501

        Price of a single unit of the product at this break.  # noqa: E501

        :return: The unit_price of this PriceBreak.  # noqa: E501
        :rtype: float

### `unit_price()`

Sets the unit_price of this PriceBreak.

        Price of a single unit of the product at this break.  # noqa: E501

        :param unit_price: The unit_price of this PriceBreak.  # noqa: E501
        :type: float

### `total_price()`

Gets the total_price of this PriceBreak.  # noqa: E501

        Price of BreakQuantity units of the product.  # noqa: E501

        :return: The total_price of this PriceBreak.  # noqa: E501
        :rtype: float

### `total_price()`

Sets the total_price of this PriceBreak.

        Price of BreakQuantity units of the product.  # noqa: E501

        :param total_price: The total_price of this PriceBreak.  # noqa: E501
        :type: float

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `product_details()`

Gets the product_details of this ProductDetailsResponse.  # noqa: E501

        List of ProductDetails  # noqa: E501

        :return: The product_details of this ProductDetailsResponse.  # noqa: E501
        :rtype: list[ProductDetails]

### `product_details()`

Sets the product_details of this ProductDetailsResponse.

        List of ProductDetails  # noqa: E501

        :param product_details: The product_details of this ProductDetailsResponse.  # noqa: E501
        :type: list[ProductDetails]

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `value_id()`

Gets the value_id of this ValuePair.  # noqa: E501

        The Id of the value.  # noqa: E501

        :return: The value_id of this ValuePair.  # noqa: E501
        :rtype: str

### `value_id()`

Sets the value_id of this ValuePair.

        The Id of the value.  # noqa: E501

        :param value_id: The value_id of this ValuePair.  # noqa: E501
        :type: str

### `value()`

Gets the value of this ValuePair.  # noqa: E501

        The name of the value.  # noqa: E501

        :return: The value of this ValuePair.  # noqa: E501
        :rtype: str

### `value()`

Sets the value of this ValuePair.

        The name of the value.  # noqa: E501

        :param value: The value of this ValuePair.  # noqa: E501
        :type: str

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `taxonomy_ids()`

Gets the taxonomy_ids of this Filters.  # noqa: E501

        A collection of Taxonomy Ids to filter on. Ids can be found in the initial search response.  # noqa: E501

        :return: The taxonomy_ids of this Filters.  # noqa: E501
        :rtype: list[int]

### `taxonomy_ids()`

Sets the taxonomy_ids of this Filters.

        A collection of Taxonomy Ids to filter on. Ids can be found in the initial search response.  # noqa: E501

        :param taxonomy_ids: The taxonomy_ids of this Filters.  # noqa: E501
        :type: list[int]

### `manufacturer_ids()`

Gets the manufacturer_ids of this Filters.  # noqa: E501

        A collection of Manufacturer Ids to filter on. Ids can be found in the initial search response.  # noqa: E501

        :return: The manufacturer_ids of this Filters.  # noqa: E501
        :rtype: list[int]

### `manufacturer_ids()`

Sets the manufacturer_ids of this Filters.

        A collection of Manufacturer Ids to filter on. Ids can be found in the initial search response.  # noqa: E501

        :param manufacturer_ids: The manufacturer_ids of this Filters.  # noqa: E501
        :type: list[int]

### `parametric_filters()`

Gets the parametric_filters of this Filters.  # noqa: E501

        A collection of ParametricFilters. A ParametricFilter consists of a ParameterId and a ValueId. Those Ids can also be found in the Search response.  # noqa: E501

        :return: The parametric_filters of this Filters.  # noqa: E501
        :rtype: list[ParametricFilter]

### `parametric_filters()`

Sets the parametric_filters of this Filters.

        A collection of ParametricFilters. A ParametricFilter consists of a ParameterId and a ValueId. Those Ids can also be found in the Search response.  # noqa: E501

        :param parametric_filters: The parametric_filters of this Filters.  # noqa: E501
        :type: list[ParametricFilter]

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model

### `limited_taxonomy()`

Gets the limited_taxonomy of this KeywordSearchResponse.  # noqa: E501


        :return: The limited_taxonomy of this KeywordSearchResponse.  # noqa: E501
        :rtype: LimitedTaxonomy

### `limited_taxonomy()`

Sets the limited_taxonomy of this KeywordSearchResponse.


        :param limited_taxonomy: The limited_taxonomy of this KeywordSearchResponse.  # noqa: E501
        :type: LimitedTaxonomy

### `filter_options()`

Gets the filter_options of this KeywordSearchResponse.  # noqa: E501

        Available filters for narrowing down results.  # noqa: E501

        :return: The filter_options of this KeywordSearchResponse.  # noqa: E501
        :rtype: list[LimitedParameter]

### `filter_options()`

Sets the filter_options of this KeywordSearchResponse.

        Available filters for narrowing down results.  # noqa: E501

        :param filter_options: The filter_options of this KeywordSearchResponse.  # noqa: E501
        :type: list[LimitedParameter]

### `products()`

Gets the products of this KeywordSearchResponse.  # noqa: E501

        List of products returned by KeywordSearch  # noqa: E501

        :return: The products of this KeywordSearchResponse.  # noqa: E501
        :rtype: list[Product]

### `products()`

Sets the products of this KeywordSearchResponse.

        List of products returned by KeywordSearch  # noqa: E501

        :param products: The products of this KeywordSearchResponse.  # noqa: E501
        :type: list[Product]

### `products_count()`

Gets the products_count of this KeywordSearchResponse.  # noqa: E501

        Total number of matching products found.  # noqa: E501

        :return: The products_count of this KeywordSearchResponse.  # noqa: E501
        :rtype: int

### `products_count()`

Sets the products_count of this KeywordSearchResponse.

        Total number of matching products found.  # noqa: E501

        :param products_count: The products_count of this KeywordSearchResponse.  # noqa: E501
        :type: int

### `exact_manufacturer_products_count()`

Gets the exact_manufacturer_products_count of this KeywordSearchResponse.  # noqa: E501

        Number of exact ManufacturerPartNumber matches.  # noqa: E501

        :return: The exact_manufacturer_products_count of this KeywordSearchResponse.  # noqa: E501
        :rtype: int

### `exact_manufacturer_products_count()`

Sets the exact_manufacturer_products_count of this KeywordSearchResponse.

        Number of exact ManufacturerPartNumber matches.  # noqa: E501

        :param exact_manufacturer_products_count: The exact_manufacturer_products_count of this KeywordSearchResponse.  # noqa: E501
        :type: int

### `exact_manufacturer_products()`

Gets the exact_manufacturer_products of this KeywordSearchResponse.  # noqa: E501

        List of products that are exact ManufacturerPartNumber matches.  # noqa: E501

        :return: The exact_manufacturer_products of this KeywordSearchResponse.  # noqa: E501
        :rtype: list[Product]

### `exact_manufacturer_products()`

Sets the exact_manufacturer_products of this KeywordSearchResponse.

        List of products that are exact ManufacturerPartNumber matches.  # noqa: E501

        :param exact_manufacturer_products: The exact_manufacturer_products of this KeywordSearchResponse.  # noqa: E501
        :type: list[Product]

### `exact_digi_key_product()`

Gets the exact_digi_key_product of this KeywordSearchResponse.  # noqa: E501


        :return: The exact_digi_key_product of this KeywordSearchResponse.  # noqa: E501
        :rtype: Product

### `exact_digi_key_product()`

Sets the exact_digi_key_product of this KeywordSearchResponse.


        :param exact_digi_key_product: The exact_digi_key_product of this KeywordSearchResponse.  # noqa: E501
        :type: Product

### `search_locale_used()`

Gets the search_locale_used of this KeywordSearchResponse.  # noqa: E501


        :return: The search_locale_used of this KeywordSearchResponse.  # noqa: E501
        :rtype: IsoSearchLocale

### `search_locale_used()`

Sets the search_locale_used of this KeywordSearchResponse.


        :param search_locale_used: The search_locale_used of this KeywordSearchResponse.  # noqa: E501
        :type: IsoSearchLocale

### `to_dict()`

Returns the model properties as a dict

### `to_str()`

Returns the string representation of the model
