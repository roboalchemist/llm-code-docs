# Source: https://pymagento2.readthedocs.io/en/latest/api_reference.html

Title: API Reference — PyMagento 1.9.2 documentation

URL Source: https://pymagento2.readthedocs.io/en/latest/api_reference.html

Markdown Content:
Client[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#module-magento "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------

magento.format_datetime(_dt:datetime.datetime_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento.html#format_datetime)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.format_datetime "Permalink to this definition")
Format a datetime for Magento.

magento.parse_datetime(_s:str_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento.html#parse_datetime)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.parse_datetime "Permalink to this definition")
Parse a datetime string from Magento.

### magento.client[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#module-magento.client "Permalink to this headline")

_class_ magento.client.Magento(_token:Optional[str]=None_, _base\_url:Optional[str]=None_, _scope:Optional[str]=None_, _logger:Optional[logging.Logger]=None_, _read\_only=False_, _user\_agent=None_, _*_, _batch\_page\_size:Optional[int]=None_, _**kwargs_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento "Permalink to this definition")
Client for the Magento API.

PAGE_SIZE _=1000_[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.PAGE_SIZE "Permalink to this definition")add_product_to_category(_category\_id:Union[int,str]_, _product\_link:Dict[str,Any]_, _**kwargs_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.add_product_to_category)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.add_product_to_category "Permalink to this definition")
Assign a product to a category.

[https://adobe-commerce.redoc.ly/2.4.6-admin/tag/categoriescategoryIdproducts/#operation/PostV1CategoriesCategoryIdProducts](https://adobe-commerce.redoc.ly/2.4.6-admin/tag/categoriescategoryIdproducts/#operation/PostV1CategoriesCategoryIdProducts)

Parameters
*   **category_id** – ID of the category

*   **product_link** – product link. See the Adobe Commerce documentation for the format.

add_products_attribute_option(_attribute\_code:str_, _option:Dict[str,str]_)→str[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.add_products_attribute_option)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.add_products_attribute_option "Permalink to this definition")
Add an option to a products attribute.

[https://magento.redoc.ly/2.3.6-admin/#operation/catalogProductAttributeOptionManagementV1AddPost](https://magento.redoc.ly/2.3.6-admin/#operation/catalogProductAttributeOptionManagementV1AddPost)

Parameters
*   **attribute_code** –

*   **option** – dict with label/value keys (mandatory)

Returns
new id

assign_attribute_set_attribute(_attribute\_set\_id:int_, _attribute\_group\_id:int_, _attribute\_code:str_, _sort\_order:int=0_, _**kwargs_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.assign_attribute_set_attribute)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.assign_attribute_set_attribute "Permalink to this definition")
Assign an attribute to an attribute set.

Parameters
*   **attribute_set_id** – ID of the attribute set.

*   **attribute_group_id** – ID of the attribute group. It must be in the attribute set.

*   **attribute_code** – code of the attribute to add in that attribute group and so in that attribute set.

*   **sort_order** –

*   **kwargs** –

Returns async_update_products(_product\_updates:Iterable[Dict[str,Any]]_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.async_update_products)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.async_update_products "Permalink to this definition")
Update multiple products using the async bulk API.

Example:

>>> Magento().async_update_products([{"sku": "SK123", "name": "Abc"}), {"sku": "SK4", "name": "Def"}])

See [https://devdocs.magento.com/guides/v2.4/rest/bulk-endpoints.html](https://devdocs.magento.com/guides/v2.4/rest/bulk-endpoints.html)

Parameters
**product_updates** – sequence of product data dicts. They MUST contain an sku key.

Returns create_category(_category:Dict[str,Any]_, _**kwargs_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.create_category)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.create_category "Permalink to this definition")
Create a new category.

create_order_invoice(_order\_id:Union[int,str]_, _payload:Optional[dict]=None_, _notify=True_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.create_order_invoice)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.create_order_invoice "Permalink to this definition")
Create an invoice for an order.

See: * [https://devdocs.magento.com/guides/v2.4/rest/tutorials/orders/order-create-invoice.html](https://devdocs.magento.com/guides/v2.4/rest/tutorials/orders/order-create-invoice.html) * [https://www.rakeshjesadiya.com/create-invoice-using-rest-api-magento-2/](https://www.rakeshjesadiya.com/create-invoice-using-rest-api-magento-2/)

Parameters
*   **order_id** – Order id.

*   **payload** – payload to send to the API.

*   **notify** – if True (default), notify the client. This is overridden by `payload`.

Returns delete_attribute(_attribute\_code:str_, _**kwargs_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.delete_attribute)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.delete_attribute "Permalink to this definition")delete_default_source_items()[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.delete_default_source_items)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.delete_default_source_items "Permalink to this definition")
Delete all source items that have a source_code=default.

Returns
requests.Response object if there are default source items, None otherwise.

delete_product(_sku:str_, _skip\_missing=False_, _throw=True_, _**kwargs_)→bool[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.delete_product)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.delete_product "Permalink to this definition")
Delete a product given its SKU.

Parameters
*   **sku** –

*   **skip_missing** – if true, don’t raise if the product is missing, and return False.

*   **throw** – throw on error response

*   **kwargs** – keyword arguments passed to all underlying methods.

Returns
a boolean indicating success.

delete_product_media(_sku:str_, _media\_id:Union[int,str]_, _throw=False_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.delete_product_media)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.delete_product_media "Permalink to this definition")
Delete a media associated with a product.

Parameters
*   **sku** – SKU of the product

*   **media_id** –

*   **throw** –

Returns delete_products_attribute_option(_attribute\_code:str_, _option\_id:Union[int,str]_)→bool[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.delete_products_attribute_option)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.delete_products_attribute_option "Permalink to this definition")
Remove an option to a products attribute.

Parameters
*   **attribute_code** –

*   **option_id** –

Returns
boolean

delete_source_items(_source\_items:Iterable[Dict[str,Any]]_, _throw=True_, _**kwargs_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.delete_source_items)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.delete_source_items "Permalink to this definition")
Delete a sequence of source-items. Only the SKU and the source_code are used. Note: Magento returns an error if this is called with empty source_items.

Parameters
*   **source_items** –

*   **throw** –

*   **kwargs** – keyword arguments passed to the underlying POST call.

Returns
requests.Response object

delete_special_prices(_special\_prices:Sequence[Dict[str,Any]]_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.delete_special_prices)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.delete_special_prices "Permalink to this definition")
Delete a sequence of special prices.

delete_special_prices_by_sku(_skus:Sequence[str]_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.delete_special_prices_by_sku)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.delete_special_prices_by_sku "Permalink to this definition")
Equivalent of `delete_special_prices(get_special_prices(skus))`.

get_attribute_set_attributes(_attribute\_set\_id:int_, _**kwargs_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_attribute_set_attributes)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_attribute_set_attributes "Permalink to this definition")
Get all attributes for the given attribute set id.

get_attribute_sets(_query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_attribute_sets)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_attribute_sets "Permalink to this definition")
Get all attribute sets (generator).

get_base_prices(_skus:Sequence[str]_)→List[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_base_prices)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_base_prices "Permalink to this definition")
Get base prices for a sequence of SKUs.

get_bulk_status(_bulk\_uuid:str_)→Dict[str,Any][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_bulk_status)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_bulk_status "Permalink to this definition")
Get the status of an async/bulk operation.

get_carts(_*_, _query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_carts)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_carts "Permalink to this definition")
Get all carts (generator).

get_categories(_query:Optional[Dict[str,Any]]=None_, _path\_prefix:Optional[str]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_categories)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_categories "Permalink to this definition")
Yield all categories.

Parameters
*   **path_prefix** – optional path prefix for the categories. Example: `"1/2"` for all categories whose path is `"1/2/..."`, including `"1/2"` itself. Use `"1/2/"` to exclude `"1/2"` from the returned categories.

*   **query** – optional query. This overrides `path_prefix`.

*   **limit** – optional limit

get_category(_category\_id:Union[int,str]_)→Optional[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_category)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_category "Permalink to this definition")
Return a category given its id.

get_category_by_name(_name:str_)→Optional[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_category_by_name)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_category_by_name "Permalink to this definition")
Return the first category with the given name.

Parameters
**name** – exact name of the category

Returns get_category_products(_category\_id:Union[int,str]_, _**kwargs_)→List[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_category_products)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_category_products "Permalink to this definition")
Get products assigned to a category.

[https://adobe-commerce.redoc.ly/2.4.6-admin/tag/categoriescategoryIdproducts#operation/GetV1CategoriesCategoryIdProducts](https://adobe-commerce.redoc.ly/2.4.6-admin/tag/categoriescategoryIdproducts#operation/GetV1CategoriesCategoryIdProducts)

Example:

> {‘sku’: ‘MYSKU123’, ‘position’: 2, ‘category_id’: ‘17’}

get_cms_blocks(_*_, _query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_cms_blocks)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_cms_blocks "Permalink to this definition")
Get all CMS blocks (generator).

get_cms_pages(_*_, _query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_cms_pages)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_cms_pages "Permalink to this definition")
Get all CMS pages (generator).

get_coupons(_*_, _query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_coupons)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_coupons "Permalink to this definition")
Get all coupons (generator).

get_credit_memos(_query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_credit_memos)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_credit_memos "Permalink to this definition")
Get all credit memos (generator).

get_current_store_group_id(_*_, _skip\_store\_groups=False_)→int[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_current_store_group_id)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_current_store_group_id "Permalink to this definition")
Get the current store group id for the current scope. This is not part of Magento API.

Parameters
**skip_store_groups** – if True, assume the current scope is not already a store group.

get_customer(_customer\_id:int_)→dict[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_customer)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_customer "Permalink to this definition")
Return a single customer.

get_customer_groups(_*_, _query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_customer_groups)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_customer_groups "Permalink to this definition")
Get all customer groups (generator).

get_customers(_*_, _query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_customers)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_customers "Permalink to this definition")
Get all customers (generator).

get_invoice(_invoice\_id:int_)→Dict[str,Any][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_invoice)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_invoice "Permalink to this definition")get_invoice_by_increment_id(_increment\_id:str_)→Optional[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_invoice_by_increment_id)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_invoice_by_increment_id "Permalink to this definition")get_invoices(_query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_invoices)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_invoices "Permalink to this definition")
Get all invoices (generator).

get_last_orders(_limit=10_)→List[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_last_orders)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_last_orders "Permalink to this definition")
Return a list of the last orders (default: 10).

get_manufacturers()[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_manufacturers)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_manufacturers "Permalink to this definition")
Shortcut for .get_products_attribute_options(“manufacturer”).

get_modules(_query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_modules)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_modules "Permalink to this definition")
Get all enabled modules (generator).

get_order(_order\_id:str_, _throw=True_)→Optional[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_order)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_order "Permalink to this definition")
Get an order given its (entity) id.

get_order_by_increment_id(_increment\_id:str_)→Optional[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_order_by_increment_id)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_order_by_increment_id "Permalink to this definition")
Get an order given its increment id. Return `None` if the order doesn’t exist.

get_order_invoices(_order\_id:Union[int,str]_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_order_invoices)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_order_invoices "Permalink to this definition")
Get invoices for the given order id.

get_order_shipments(_order\_id:Union[int,str]_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_order_shipments)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_order_shipments "Permalink to this definition")
Get shipments for the given order id.

get_orders(_*_, _status:Optional[str]=None_, _status\_condition\_type:Optional[str]=None_, _limit=-1_, _query:Optional[Dict[str,Any]]=None_, _retry=0_)→Iterator[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_orders)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_orders "Permalink to this definition")
Return a generator of all orders with this status up to the limit.

Parameters
*   **status** – order status, e.g. “awaiting_shipping”. This overrides `query`.

*   **status_condition_type** – condition type to use for the status. Default is “eq”. This has no effect if `status` is not given.

*   **limit** – maximum number of orders to yield (default: no limit).

*   **query** – optional query.

*   **retry** – max retries count

Returns
generator of orders

get_orders_items(_*_, _sku:Optional[str]=None_, _query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_orders_items)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_orders_items "Permalink to this definition")
Return orders items.

Parameters
*   **sku** – filter orders items on SKU. This is a shortcut for `query=make_field_value_query("sku", sku)`.

*   **query** – optional query. This take precedence over `sku`.

*   **limit** –

Returns get_paginated(_path:str_, _*_, _query:Optional[Dict[str,Any]]=None_, _limit=-1_, _retry=0_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_paginated)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_paginated "Permalink to this definition")
Get a paginated API path.

Parameters
*   **path** –

*   **query** –

*   **limit** – -1 for no limit

*   **retry** –

Returns get_product(_sku:str_)→Optional[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_product)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_product "Permalink to this definition")
Get a single product. Return `None` if it doesn’t exist.

Parameters
**sku** – SKU of the product

Returns get_product_by_id(_product\_id:int_)→Optional[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_product_by_id)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_product_by_id "Permalink to this definition")
Get a product given its id. Return `None` if the product doesn’t exist.

Parameters
**product_id** – ID of the product

Returns get_product_by_query(_query:Optional[Dict[str,Any]]_, _*_, _expect\_one=True_)→Optional[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_product_by_query)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_product_by_query "Permalink to this definition")
Get a product with a custom query. Return `None` if the query doesn’t return match any product, and raise an exception if it returns more than one, unless `expect_one` is set to `False`.

Parameters
*   **query** –

*   **expect_one** – if True (the default), raise an exception if the query returns more than one result.

Returns get_product_media(_sku:str_, _media\_id:Union[int,str]_)→Dict[str,Any][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_product_media)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_product_media "Permalink to this definition")
Return a gallery entry.

Parameters
*   **sku** – SKU of the product.

*   **media_id** –

Returns get_product_medias(_sku:str_)→Sequence[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_product_medias)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_product_medias "Permalink to this definition")
Get the list of gallery entries associated with the given product.

Parameters
**sku** – SKU of the product.

Returns get_product_stock_item(_sku:str_)→Dict[str,Any][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_product_stock_item)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_product_stock_item "Permalink to this definition")
Get the stock item for an SKU.

get_product_stock_status(_sku:str_)→Dict[str,Any][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_product_stock_status)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_product_stock_status "Permalink to this definition")
Get stock status for an SKU.

get_products(_limit=-1_, _query:Optional[Dict[str,Any]]=None_, _retry=0_)→Iterator[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_products)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_products "Permalink to this definition")
Return a generator of all products.

Parameters
*   **limit** – -1 for unlimited.

*   **query** –

*   **retry** –

Returns get_products_attribute_options(_attribute\_code:str_)→Sequence[Dict[str,str]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_products_attribute_options)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_products_attribute_options "Permalink to this definition")
Get all options for a products attribute.

Parameters
**attribute_code** –

Returns
sequence of option dicts.

get_products_types()→Sequence[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_products_types)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_products_types "Permalink to this definition")
Get available product types.

get_root_category_id()→int[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_root_category_id)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_root_category_id "Permalink to this definition")
Get the root category id of the current scope. This is not part of Magento API.

get_sales_rules(_*_, _query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_sales_rules)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_sales_rules "Permalink to this definition")
Get all sales rules (generator).

get_shipments(_*_, _query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_shipments)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_shipments "Permalink to this definition")
Return shipments (generator).

get_source(_source\_code:str_)→Optional[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_source)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_source "Permalink to this definition")
Get a single source, or None if it doesn’t exist.

[https://adobe-commerce.redoc.ly/2.4.6-admin/tag/inventorysourcessourceCode#operation/GetV1InventorySourcesSourceCode](https://adobe-commerce.redoc.ly/2.4.6-admin/tag/inventorysourcessourceCode#operation/GetV1InventorySourcesSourceCode)

get_source_items(_source\_code:Optional[str]=None_, _sku:Optional[str]=None_, _*_, _skus:Optional[Iterable[str]]=None_, _query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_source_items)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_source_items "Permalink to this definition")
Return a generator of all source items.

Parameters
*   **source_code** – optional source_code to filter on. This takes precedence over the query parameter.

*   **sku** – optional SKU to filter on. This takes precedence over the query and the skus parameter.

*   **skus** – optional SKUs list to filter on. This takes precedence of the query parameter.

*   **query** – optional query.

*   **limit** – -1 for unlimited.

Returns get_sources(_query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_sources)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_sources "Permalink to this definition")
Get all sources.

[https://adobe-commerce.redoc.ly/2.4.6-admin/tag/inventorysources#operation/GetV1InventorySources](https://adobe-commerce.redoc.ly/2.4.6-admin/tag/inventorysources#operation/GetV1InventorySources)

get_special_prices(_skus:Sequence[str]_)→List[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_special_prices)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_special_prices "Permalink to this definition")
Get special prices for a sequence of SKUs.

get_stock_source_links(_query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_stock_source_links)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_stock_source_links "Permalink to this definition")get_store_configs(_store\_codes:Optional[List[str]]=None_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_store_configs)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_store_configs "Permalink to this definition")get_store_groups()→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_store_groups)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_store_groups "Permalink to this definition")get_store_views()→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_store_views)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_store_views "Permalink to this definition")get_tax_classes(_*_, _query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_tax_classes)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_tax_classes "Permalink to this definition")
Get all tax classes (generator).

get_tax_rates(_*_, _query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_tax_rates)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_tax_rates "Permalink to this definition")
Get all tax rates (generator).

get_tax_rules(_*_, _query:Optional[Dict[str,Any]]=None_, _limit=-1_, _**kwargs_)→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_tax_rules)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_tax_rules "Permalink to this definition")
Get all tax rules (generator).

get_websites()→Iterable[Dict[str,Any]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.get_websites)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.get_websites "Permalink to this definition")hold_order(_order\_id:str_, _**kwargs_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.hold_order)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.hold_order "Permalink to this definition")
Hold an order. This is the opposite of `unhold_order`.

Parameters
**order_id** – order id (not increment id)

link_child_product(_parent\_sku:str_, _child\_sku:str_, _**kwargs_)→requests.models.Response[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.link_child_product)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.link_child_product "Permalink to this definition")
Link two products, one as the parent of the other.

Parameters
*   **parent_sku** – SKU of the parent product

*   **child_sku** – SKU of the child product

Returns
requests.Response object

remove_attribute_set_attribute(_attribute\_set\_id:int_, _attribute\_code:str_, _**kwargs_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.remove_attribute_set_attribute)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.remove_attribute_set_attribute "Permalink to this definition")remove_category(_category\_id:Union[int,str]_, _**kwargs_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.remove_category)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.remove_category "Permalink to this definition")
Remove a category.

[https://adobe-commerce.redoc.ly/2.4.6-admin/tag/categoriescategoryId/#operation/DeleteV1CategoriesCategoryId](https://adobe-commerce.redoc.ly/2.4.6-admin/tag/categoriescategoryId/#operation/DeleteV1CategoriesCategoryId)

remove_product_from_category(_category\_id:Union[int,str]_, _sku:str_, _**kwargs_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.remove_product_from_category)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.remove_product_from_category "Permalink to this definition")
Remove a product from a category.

[https://adobe-commerce.redoc.ly/2.4.6-admin/tag/categoriescategoryIdproductssku/#operation/DeleteV1CategoriesCategoryIdProductsSku](https://adobe-commerce.redoc.ly/2.4.6-admin/tag/categoriescategoryIdproductssku/#operation/DeleteV1CategoriesCategoryIdProductsSku)

Parameters
*   **category_id** – ID of the category

*   **sku** – SKU of the product

request_api(_method:str_, _path:str_, _*args_, _async\_bulk=False_, _throw=False_, _retry=0_, _**kwargs_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.request_api)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.request_api "Permalink to this definition")
Equivalent of .request() that prefixes the path with the base API URL.

Parameters
*   **method** – HTTP method

*   **path** – API path. This must start with “/V1/”

*   **args** – arguments passed to `.request()`

*   **async_bulk** – if True, use the “/async/bulk” prefix. [https://devdocs.magento.com/guides/v2.3/rest/bulk-endpoints.html](https://devdocs.magento.com/guides/v2.3/rest/bulk-endpoints.html)

*   **throw** – if True, raise an exception if the response is an error

*   **retry** – if non-zero, retry the request that many times if there is an error, sleeping 10s between each request.

*   **kwargs** – keyword arguments passed to `.request()`

Returns save_attribute(_attribute:Dict[str,Any]_, _*_, _with\_defaults=True_, _throw=True_, _**kwargs_)→Dict[str,Any][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.save_attribute)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.save_attribute "Permalink to this definition")save_base_prices(_prices:Sequence[Dict[str,Any]]_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.save_base_prices)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.save_base_prices "Permalink to this definition")
Save base prices.

Example:

>>> self.save_base_prices([{"price": 3.14, "sku": "W1033", "store_id": 0}])

Parameters
**prices** – base prices to save.

Returns
requests.Response object

save_configurable_product_option(_sku:str_, _option:Dict[str,Any]_, _throw=False_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.save_configurable_product_option)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.save_configurable_product_option "Permalink to this definition")
Save a configurable product option.

Parameters
*   **sku** – SKU of the product

*   **option** – option to save

*   **throw** –

Returns
requests.Response object

save_order(_order:Dict[str,Any]_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.save_order)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.save_order "Permalink to this definition")
Save an order.

save_product(_product_, _*_, _save\_options:Optional[bool]=None_)→Dict[str,Any][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.save_product)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.save_product "Permalink to this definition")
Save a product.

Parameters
*   **product** – product to save (can be partial).

*   **save_options** – set the saveOptions attribute.

Returns save_product_media(_sku:str_, _media\_entry:Dict[str,Any]_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.save_product_media)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.save_product_media "Permalink to this definition")
Save a product media.

save_source(_source:Dict[str,Any]_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.save_source)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.save_source "Permalink to this definition")
Save a source.

[https://adobe-commerce.redoc.ly/2.4.6-admin/tag/inventorysources/#operation/PostV1InventorySources](https://adobe-commerce.redoc.ly/2.4.6-admin/tag/inventorysources/#operation/PostV1InventorySources)

save_source_items(_source\_items:Sequence[Dict[str,Any]]_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.save_source_items)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.save_source_items "Permalink to this definition")
Save a sequence of source-items. Return None if the sequence is empty.

Parameters
**source_items** –

Returns save_special_prices(_special\_prices:Sequence[Dict[str,Any]]_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.save_special_prices)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.save_special_prices "Permalink to this definition")
Save a sequence of special prices.

Example:

>>> price_from = "2022-01-01 00:00:00"
>>> price_to = "2022-01-31 23:59:59"
>>> special_price = {"store_id": 0, "sku": "W1033", "price": 2.99,                                  "price_from": price_from, "price_to": price_to}
>>> self.save_special_prices([special_price])

Parameters
**special_prices** – Special prices to save.

Returns set_order_status(_order:Dict[str,Any]_, _status:str_, _*_, _external\_order\_id:Optional[str]=None_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.set_order_status)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.set_order_status "Permalink to this definition")
Change the status of an order, and optionally set its `ext_order_id`. This is a convenient wrapper around `save_order`.

Parameters
*   **order** – order payload

*   **status** – new status

*   **external_order_id** – optional external order id

Returns set_product_stock_item(_sku:str_, _quantity:int_, _is\_in\_stock=1_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.set_product_stock_item)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.set_product_stock_item "Permalink to this definition")Parameters
*   **sku** –

*   **quantity** –

*   **is_in_stock** –

Returns
requests.Response

ship_order(_order\_id:Union[int,str]_, _payload:Dict[str,Any]_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.ship_order)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.ship_order "Permalink to this definition")
Ship an order.

unhold_order(_order\_id:str_, _**kwargs_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.unhold_order)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.unhold_order "Permalink to this definition")
Un-hold an order. This is the opposite of `hold_order`.

Parameters
**order_id** – order id (not increment id)

unlink_child_product(_parent\_sku:str_, _child\_sku:str_, _**kwargs_)→requests.models.Response[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.unlink_child_product)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.unlink_child_product "Permalink to this definition")
Opposite of link_child_product().

Parameters
*   **parent_sku** – SKU of the parent product

*   **child_sku** – SKU of the child product

Returns
requests.Response object

update_category(_category\_id:Union[int,str]_, _category\_data:Dict[str,Any]_)→Dict[str,Any][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.update_category)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.update_category "Permalink to this definition")
Update a category.

Parameters
*   **category_id** –

*   **category_data** – (partial) category data to update

Returns
updated category

update_product(_sku:str_, _product:Dict[str,Any]_, _*_, _save\_options:Optional[bool]=None_)→Dict[str,Any][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/client.html#Magento.update_product)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.client.Magento.update_product "Permalink to this definition")
Update a product.

Example:

>>> Magento().update_product("SK1234", {"name": "My New Name"})

To update the SKU of a product, pass its id along the new SKU and set save_options=True:

>>> Magento().update_product("old-sku", {"id": 123, "sku": "new-sku"}, save_options=True)

Parameters
*   **sku** – SKU of the product to update

*   **product** – (partial) product data to update

*   **save_options** – set the saveOptions attribute.

Returns
updated product

Helpers[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#helpers "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------

### magento.attributes[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#module-magento.attributes "Permalink to this headline")

Custom attributes utilities.

magento.attributes.get_boolean_custom_attribute(_item:dict_, _attribute\_code:str_)→Optional[bool][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/attributes.html#get_boolean_custom_attribute)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.attributes.get_boolean_custom_attribute "Permalink to this definition")
Equivalent of `get_custom_attribute(item, attribute_code, coerce_as=bool)` with proper typing.

magento.attributes.get_custom_attribute(_item:dict_, _attribute\_code:str_, _coerce\_as:Callable[[str],magento.attributes.T]_)→Union[None,magento.attributes.T,List[magento.attributes.T]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/attributes.html#get_custom_attribute)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.attributes.get_custom_attribute "Permalink to this definition")magento.attributes.get_custom_attribute(_item:dict_, _attribute\_code:str_)→Union[None,str,List[str]]
Get a custom attribute from an item given its code.

For example:

>>> get_custom_attribute(..., "my_custom_attribute")
"0"

>>> get_custom_attribute(..., "my_custom_attribute", bool)
False

Parameters
*   **item** –

*   **attribute_code** –

*   **coerce_as** – optional callable that is called on the attribute value if it’s set. This is useful to circumvent Magento’s limitation where all attribute values are strings.

Returns
attribute value or None.

magento.attributes.get_custom_attributes_dict(_item:Dict[str,Any]_)→OrderedDict[str,Union[Sequence[str],str]][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/attributes.html#get_custom_attributes_dict)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.attributes.get_custom_attributes_dict "Permalink to this definition")
Get all custom attributes from an item as an ordered dict of code->value.

magento.attributes.serialize_attribute_value(_value:Optional[Union[str,int,float,bool]]_, _force\_none=False_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/attributes.html#serialize_attribute_value)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.attributes.serialize_attribute_value "Permalink to this definition")
Serialize a value to be stored in a Magento attribute.

magento.attributes.set_custom_attribute(_item:dict_, _attribute\_code:str_, _attribute\_value:Optional[Union[str,int,float,bool]]_, _*_, _force\_none=False_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/attributes.html#set_custom_attribute)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.attributes.set_custom_attribute "Permalink to this definition")
Set a custom attribute in an item dict.

For example:

>>> set_custom_attribute({}, "my_custom_attribute", 42)
>>> set_custom_attribute({}, "my_custom_attribute", False)

Parameters
*   **item** – item dict. It’s modified in-place.

*   **attribute_code** –

*   **attribute_value** –

*   **force_none** – by default, the attribute value `None` is serialized as an empty string. Setting this parameter to `True` forces this attribute value to `None` instead. This can be used to delete attributes.

Returns
the modified item dict.

magento.attributes.set_custom_attributes(_item:dict_, _attributes:Iterable[Tuple[str,Optional[Union[str,int,float,bool]]]]_, _*_, _force\_none=False_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/attributes.html#set_custom_attributes)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.attributes.set_custom_attributes "Permalink to this definition")
Set custom attributes in an item dict. Like `set_custom_attribute` but with an iterable of attributes.

Parameters
*   **item** – item dict. It’s modified in-place.

*   **attributes** – iterable of label/value attribute tuples

*   **force_none** – see `set_custom_attribute` for usage.

Returns
the modified item dict.

### magento.batches[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#module-magento.batches "Permalink to this headline")

_class_ magento.batches.BatchGetter(_getter:Callable[[...],Iterable[magento.batches.T]]_, _key\_field:str_, _keys:Iterable_, _batch\_size=50_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/batches.html#BatchGetter)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.batches.BatchGetter "Permalink to this definition")
Base class to create generators of Magento items that can be retrieved from the API using queries. This retrieves items in batches but can be iterated on like any iterator.

_class_ magento.batches.BatchSaver(_client:[magento.client.Magento](https://pymagento2.readthedocs.io/en/latest/api\_reference.html#magento.client.Magento "magento.client.Magento")_, _api\_path:str_, _batch\_size=500_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/batches.html#BatchSaver)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.batches.BatchSaver "Permalink to this definition")
Base class to create context managers for asynchronous batches.

add_item(_item\_data_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/batches.html#BatchSaver.add_item)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.batches.BatchSaver.add_item "Permalink to this definition")
Add an item to the current batch. If it makes the batch large enough, it’s sent to the API and a new empty batch is created.

finalize()[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/batches.html#BatchSaver.finalize)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.batches.BatchSaver.finalize "Permalink to this definition")
Send the last pending batch (if any). This doesn’t need to be called when the object is used as a context manager.

Returns
a dictionary with the total number of batches and items

send_batch()[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/batches.html#BatchSaver.send_batch)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.batches.BatchSaver.send_batch "Permalink to this definition")
Send the current pending batch (if any).

_class_ magento.batches.ProductBatchGetter(_client:[magento.client.Magento](https://pymagento2.readthedocs.io/en/latest/api\_reference.html#magento.client.Magento "magento.client.Magento")_, _skus:Iterable[str]_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/batches.html#ProductBatchGetter)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.batches.ProductBatchGetter "Permalink to this definition")
Get a bunch of products from an iterable of SKUs:

>>> products = ProductBatchGetter(Magento(), ["sku1", "sku2", ...])
>>> for product in products:
...     print(product)

_class_ magento.batches.ProductBatchSaver(_client:[magento.client.Magento](https://pymagento2.readthedocs.io/en/latest/api\_reference.html#magento.client.Magento "magento.client.Magento")_, _batch\_size=500_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/batches.html#ProductBatchSaver)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.batches.ProductBatchSaver "Permalink to this definition")
Context manager to add products to an asynchronous batch job.

>>> with ProductBatchSaver() as p:
...     for product_data in ...:
...         p.save_product(product_data)

save_product(_product\_data:dict_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/batches.html#ProductBatchSaver.save_product)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.batches.ProductBatchSaver.save_product "Permalink to this definition")
### magento.order_helpers[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#module-magento.order_helpers "Permalink to this headline")

magento.order_helpers.get_order_shipping_address(_order:Dict[str,Any]_)→Dict[str,Any][[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/order_helpers.html#get_order_shipping_address)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.order_helpers.get_order_shipping_address "Permalink to this definition")
Return the first shipping address of an order. Note the returned dict is a reference, so if you modify it, it modifies the order. Make a copy if you want to modify the address without affecting the order.

magento.order_helpers.is_order_cash_on_delivery(_order:Dict[str,Any]_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/order_helpers.html#is_order_cash_on_delivery)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.order_helpers.is_order_cash_on_delivery "Permalink to this definition")
Test if an order is paid with ‘cash-on-delivery’.

magento.order_helpers.is_order_on_hold(_order:Dict[str,Any]_)[[source]](https://pymagento2.readthedocs.io/en/latest/_modules/magento/order_helpers.html#is_order_on_hold)[](https://pymagento2.readthedocs.io/en/latest/api_reference.html#magento.order_helpers.is_order_on_hold "Permalink to this definition")
Test if an order is on hold.
