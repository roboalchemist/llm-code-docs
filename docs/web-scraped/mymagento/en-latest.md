# Source: https://my-magento.readthedocs.io/en/latest/

Title: MyMagento - Python Magento 2 REST API Wrapper

URL Source: https://my-magento.readthedocs.io/en/latest/

Markdown Content:
MyMagento - Python Magento 2 REST API Wrapper — MyMagento 2.2.0 documentation
===============

[MyMagento ![Image 6: Logo](https://my-magento.readthedocs.io/en/latest/_static/magento_black.png)](https://my-magento.readthedocs.io/en/latest/#)

 latest 

README

*   [MyMagento - Python Magento 2 REST API Wrapper](https://my-magento.readthedocs.io/en/latest/#)
    *   [About MyMagento](https://my-magento.readthedocs.io/en/latest/#about-mymagento)
        *   [Main Components](https://my-magento.readthedocs.io/en/latest/#main-components)
        *   [Available Endpoints](https://my-magento.readthedocs.io/en/latest/#available-endpoints)

    *   [⚙ Installing MyMagento](https://my-magento.readthedocs.io/en/latest/#installing-mymagento)
    *   [QuickStart: Login with MyMagento](https://my-magento.readthedocs.io/en/latest/#quickstart-login-with-mymagento)
        *   [Setting the Login Credentials](https://my-magento.readthedocs.io/en/latest/#setting-the-login-credentials)
        *   [Getting a `Client`](https://my-magento.readthedocs.io/en/latest/#getting-a-client)
            *   [Option 1: Initialize a `Client` Directly](https://my-magento.readthedocs.io/en/latest/#option-1-initialize-a-client-directly)
            *   [Option 2: Call `get_api()`](https://my-magento.readthedocs.io/en/latest/#option-2-call-get-api)

        *   [Getting an `ACCESS_TOKEN`](https://my-magento.readthedocs.io/en/latest/#getting-an-access-token)

*   [Interacting with the API](https://my-magento.readthedocs.io/en/latest/interact-with-api.html)
    *   [Performing a `search()`](https://my-magento.readthedocs.io/en/latest/interact-with-api.html#performing-a-search)
    *   [Search Results: The `Model` Classes](https://my-magento.readthedocs.io/en/latest/interact-with-api.html#search-results-the-model-classes)
    *   [Building Custom Search Queries](https://my-magento.readthedocs.io/en/latest/interact-with-api.html#building-custom-search-queries)
    *   [Making Authorized Requests](https://my-magento.readthedocs.io/en/latest/interact-with-api.html#making-authorized-requests)
        *   [Example: Making a `get()` Request](https://my-magento.readthedocs.io/en/latest/interact-with-api.html#example-making-a-get-request)
        *   [Example: Making a `post()` Request](https://my-magento.readthedocs.io/en/latest/interact-with-api.html#example-making-a-post-request)

Documentation

*   [The `magento` Package](https://my-magento.readthedocs.io/en/latest/modules.html)
    *   [`get_api()`](https://my-magento.readthedocs.io/en/latest/modules.html#magento.get_api)
    *   [The `clients` module](https://my-magento.readthedocs.io/en/latest/clients.html)
        *   [`Client`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client)
            *   [`Client.__init__()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.__init__)
            *   [`Client.BASE_URL`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.BASE_URL)
            *   [`Client.USER_CREDENTIALS`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.USER_CREDENTIALS)
            *   [`Client.ACCESS_TOKEN`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.ACCESS_TOKEN)
            *   [`Client.domain`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.domain)
            *   [`Client.scope`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.scope)
            *   [`Client.user_agent`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.user_agent)
            *   [`Client.logger`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.logger)
            *   [`Client.store`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.store)
            *   [`Client.new()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.new)
            *   [`Client.load()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.load)
            *   [`Client.from_json()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.from_json)
            *   [`Client.from_dict()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.from_dict)
            *   [`Client.url_for()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.url_for)
            *   [`Client.search()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.search)
            *   [`Client.orders`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.orders)
            *   [`Client.order_items`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.order_items)
            *   [`Client.invoices`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.invoices)
            *   [`Client.categories`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.categories)
            *   [`Client.products`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.products)
            *   [`Client.product_attributes`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.product_attributes)
            *   [`Client.customers`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.customers)
            *   [`Client.get()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.get)
            *   [`Client.post()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.post)
            *   [`Client.put()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.put)
            *   [`Client.delete()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.delete)
            *   [`Client.authenticate()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.authenticate)
            *   [`Client.validate()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.validate)
            *   [`Client.request()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.request)
            *   [`Client.get_logger()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.get_logger)
            *   [`Client.headers`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.headers)
            *   [`Client.token`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.token)
            *   [`Client.to_pickle()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.to_pickle)
            *   [`Client.to_json()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.to_json)
            *   [`Client.to_dict()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.to_dict)
            *   [`Client.view_config()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.view_config)

        *   [`Store`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Store)
            *   [`Store.__init__()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Store.__init__)
            *   [`Store.is_single_store`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Store.is_single_store)
            *   [`Store.active`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Store.active)
            *   [`Store.configs`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Store.configs)
            *   [`Store.views`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Store.views)
            *   [`Store.all_product_attributes`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Store.all_product_attributes)
            *   [`Store.store_view_product_attributes`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Store.store_view_product_attributes)
            *   [`Store.website_product_attributes`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Store.website_product_attributes)
            *   [`Store.global_product_attributes`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Store.global_product_attributes)
            *   [`Store.website_attribute_codes`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Store.website_attribute_codes)
            *   [`Store.filter_website_attrs()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Store.filter_website_attrs)
            *   [`Store.refresh()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Store.refresh)

    *   [The `search` module](https://my-magento.readthedocs.io/en/latest/search_module.html)
        *   [`SearchQuery`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery)
            *   [`SearchQuery.__init__()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.__init__)
            *   [`SearchQuery.client`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.client)
            *   [`SearchQuery.endpoint`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.endpoint)
            *   [`SearchQuery.Model`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.Model)
            *   [`SearchQuery.query`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.query)
            *   [`SearchQuery.fields`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.fields)
            *   [`SearchQuery.add_criteria()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.add_criteria)
            *   [`SearchQuery.restrict_fields()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.restrict_fields)
            *   [`SearchQuery.execute()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.execute)
            *   [`SearchQuery.by_id()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.by_id)
            *   [`SearchQuery.by_list()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.by_list)
            *   [`SearchQuery.get_all()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.get_all)
            *   [`SearchQuery.since()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.since)
            *   [`SearchQuery.until()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.until)
            *   [`SearchQuery.result`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.result)
            *   [`SearchQuery.validate_result()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.validate_result)
            *   [`SearchQuery.parse()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.parse)
            *   [`SearchQuery.reset()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.reset)
            *   [`SearchQuery.result_count`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.result_count)
            *   [`SearchQuery.result_type`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.result_type)
            *   [`SearchQuery.last_group`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.last_group)

        *   [`OrderSearch`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderSearch)
            *   [`OrderSearch.__init__()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderSearch.__init__)
            *   [`OrderSearch.by_number()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderSearch.by_number)
            *   [`OrderSearch.by_product()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderSearch.by_product)
            *   [`OrderSearch.by_sku()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderSearch.by_sku)
            *   [`OrderSearch.by_product_id()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderSearch.by_product_id)
            *   [`OrderSearch.by_category_id()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderSearch.by_category_id)
            *   [`OrderSearch.by_category()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderSearch.by_category)
            *   [`OrderSearch.by_skulist()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderSearch.by_skulist)
            *   [`OrderSearch.by_customer()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderSearch.by_customer)
            *   [`OrderSearch.by_customer_id()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderSearch.by_customer_id)
            *   [`OrderSearch.from_items()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderSearch.from_items)

        *   [`OrderItemSearch`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderItemSearch)
            *   [`OrderItemSearch.__init__()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderItemSearch.__init__)
            *   [`OrderItemSearch.result`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderItemSearch.result)
            *   [`OrderItemSearch.parse()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderItemSearch.parse)
            *   [`OrderItemSearch.by_product()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderItemSearch.by_product)
            *   [`OrderItemSearch.by_sku()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderItemSearch.by_sku)
            *   [`OrderItemSearch.by_product_id()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderItemSearch.by_product_id)
            *   [`OrderItemSearch.by_category_id()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderItemSearch.by_category_id)
            *   [`OrderItemSearch.by_category()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderItemSearch.by_category)
            *   [`OrderItemSearch.by_skulist()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderItemSearch.by_skulist)

        *   [`InvoiceSearch`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.InvoiceSearch)
            *   [`InvoiceSearch.__init__()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.InvoiceSearch.__init__)
            *   [`InvoiceSearch.by_number()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.InvoiceSearch.by_number)
            *   [`InvoiceSearch.by_order_number()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.InvoiceSearch.by_order_number)
            *   [`InvoiceSearch.by_order()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.InvoiceSearch.by_order)
            *   [`InvoiceSearch.by_order_id()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.InvoiceSearch.by_order_id)
            *   [`InvoiceSearch.by_product()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.InvoiceSearch.by_product)
            *   [`InvoiceSearch.by_sku()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.InvoiceSearch.by_sku)
            *   [`InvoiceSearch.by_product_id()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.InvoiceSearch.by_product_id)
            *   [`InvoiceSearch.by_category_id()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.InvoiceSearch.by_category_id)
            *   [`InvoiceSearch.by_category()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.InvoiceSearch.by_category)
            *   [`InvoiceSearch.by_skulist()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.InvoiceSearch.by_skulist)
            *   [`InvoiceSearch.by_customer()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.InvoiceSearch.by_customer)
            *   [`InvoiceSearch.by_customer_id()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.InvoiceSearch.by_customer_id)
            *   [`InvoiceSearch.from_order_items()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.InvoiceSearch.from_order_items)

        *   [`ProductSearch`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductSearch)
            *   [`ProductSearch.__init__()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductSearch.__init__)
            *   [`ProductSearch.attributes`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductSearch.attributes)
            *   [`ProductSearch.by_id()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductSearch.by_id)
            *   [`ProductSearch.by_sku()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductSearch.by_sku)
            *   [`ProductSearch.by_skulist()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductSearch.by_skulist)
            *   [`ProductSearch.by_category()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductSearch.by_category)
            *   [`ProductSearch.by_category_id()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductSearch.by_category_id)
            *   [`ProductSearch.by_customer_id()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductSearch.by_customer_id)
            *   [`ProductSearch.get_stock()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductSearch.get_stock)

        *   [`ProductAttributeSearch`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductAttributeSearch)
            *   [`ProductAttributeSearch.__init__()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductAttributeSearch.__init__)
            *   [`ProductAttributeSearch.get_all()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductAttributeSearch.get_all)
            *   [`ProductAttributeSearch.by_code()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductAttributeSearch.by_code)
            *   [`ProductAttributeSearch.get_types()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductAttributeSearch.get_types)

        *   [`CustomerSearch`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.CustomerSearch)
            *   [`CustomerSearch.__init__()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.CustomerSearch.__init__)
            *   [`CustomerSearch.by_id()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.CustomerSearch.by_id)
            *   [`CustomerSearch.by_first_name()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.CustomerSearch.by_first_name)
            *   [`CustomerSearch.by_last_name()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.CustomerSearch.by_last_name)
            *   [`CustomerSearch.by_invoice()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.CustomerSearch.by_invoice)
            *   [`CustomerSearch.by_order()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.CustomerSearch.by_order)
            *   [`CustomerSearch.by_product()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.CustomerSearch.by_product)

        *   [`CategorySearch`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.CategorySearch)
            *   [`CategorySearch.__init__()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.CategorySearch.__init__)
            *   [`CategorySearch.get_root()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.CategorySearch.get_root)
            *   [`CategorySearch.get_all()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.CategorySearch.get_all)
            *   [`CategorySearch.by_name()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.CategorySearch.by_name)

    *   [The `exceptions` module](https://my-magento.readthedocs.io/en/latest/exceptions.html)
        *   [`MagentoError`](https://my-magento.readthedocs.io/en/latest/exceptions.html#magento.exceptions.MagentoError)
            *   [`MagentoError.DEFAULT_MSG`](https://my-magento.readthedocs.io/en/latest/exceptions.html#magento.exceptions.MagentoError.DEFAULT_MSG)
            *   [`MagentoError.__init__()`](https://my-magento.readthedocs.io/en/latest/exceptions.html#magento.exceptions.MagentoError.__init__)
            *   [`MagentoError.parse()`](https://my-magento.readthedocs.io/en/latest/exceptions.html#magento.exceptions.MagentoError.parse)

        *   [`AuthenticationError`](https://my-magento.readthedocs.io/en/latest/exceptions.html#magento.exceptions.AuthenticationError)
            *   [`AuthenticationError.DEFAULT_MSG`](https://my-magento.readthedocs.io/en/latest/exceptions.html#magento.exceptions.AuthenticationError.DEFAULT_MSG)
            *   [`AuthenticationError.__init__()`](https://my-magento.readthedocs.io/en/latest/exceptions.html#magento.exceptions.AuthenticationError.__init__)

    *   [The `utils` module](https://my-magento.readthedocs.io/en/latest/utils.html)
        *   [`parse_domain()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.parse_domain)
        *   [`get_agents()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.get_agents)
        *   [`get_agent()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.get_agent)
        *   [`LoggerUtils`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.LoggerUtils)
            *   [`LoggerUtils.get_handler_names()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.LoggerUtils.get_handler_names)
            *   [`LoggerUtils.get_stream_handlers()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.LoggerUtils.get_stream_handlers)
            *   [`LoggerUtils.get_file_handlers()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.LoggerUtils.get_file_handlers)
            *   [`LoggerUtils.get_log_files()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.LoggerUtils.get_log_files)
            *   [`LoggerUtils.get_handler_by_log_file()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.LoggerUtils.get_handler_by_log_file)
            *   [`LoggerUtils.clear_handlers()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.LoggerUtils.clear_handlers)
            *   [`LoggerUtils.clear_stream_handlers()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.LoggerUtils.clear_stream_handlers)
            *   [`LoggerUtils.clear_file_handlers()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.LoggerUtils.clear_file_handlers)
            *   [`LoggerUtils.map_handlers_by_name()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.LoggerUtils.map_handlers_by_name)

        *   [`MagentoLogger`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger)
            *   [`MagentoLogger.PREFIX`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.PREFIX)
            *   [`MagentoLogger.PACKAGE_LOG_NAME`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.PACKAGE_LOG_NAME)
            *   [`MagentoLogger.CLIENT_LOG_NAME`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.CLIENT_LOG_NAME)
            *   [`MagentoLogger.HANDLER_NAME`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.HANDLER_NAME)
            *   [`MagentoLogger.LOG_MESSAGE`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.LOG_MESSAGE)
            *   [`MagentoLogger.FORMATTER`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.FORMATTER)
            *   [`MagentoLogger.__init__()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.__init__)
            *   [`MagentoLogger.setup_logger()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.setup_logger)
            *   [`MagentoLogger.format_msg()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.format_msg)
            *   [`MagentoLogger.debug()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.debug)
            *   [`MagentoLogger.info()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.info)
            *   [`MagentoLogger.error()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.error)
            *   [`MagentoLogger.warning()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.warning)
            *   [`MagentoLogger.critical()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.critical)
            *   [`MagentoLogger.handlers`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.handlers)
            *   [`MagentoLogger.handler_names`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.handler_names)
            *   [`MagentoLogger.handler_map`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.handler_map)
            *   [`MagentoLogger.file_handlers`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.file_handlers)
            *   [`MagentoLogger.stream_handlers`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.stream_handlers)
            *   [`MagentoLogger.log_files`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.log_files)
            *   [`MagentoLogger.log_path`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.log_path)
            *   [`MagentoLogger.get_magento_handlers()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.get_magento_handlers)
            *   [`MagentoLogger.clear_magento_handlers()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.clear_magento_handlers)
            *   [`MagentoLogger.clear_magento_file_handlers()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.clear_magento_file_handlers)
            *   [`MagentoLogger.clear_magento_stdout_handlers()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.clear_magento_stdout_handlers)
            *   [`MagentoLogger.owns_handler()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.owns_handler)
            *   [`MagentoLogger.get_package_handler()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.get_package_handler)
            *   [`MagentoLogger.add_request_logging()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.MagentoLogger.add_request_logging)

        *   [`get_package_file_handler()`](https://my-magento.readthedocs.io/en/latest/utils.html#magento.utils.get_package_file_handler)

*   [The `magento.models` subpackage](https://my-magento.readthedocs.io/en/latest/models.html)
    *   [The `model` module](https://my-magento.readthedocs.io/en/latest/model.html)
        *   [`Model`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model)
            *   [`Model.DOCUMENTATION`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model.DOCUMENTATION)
            *   [`Model.IDENTIFIER`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model.IDENTIFIER)
            *   [`Model.__init__()`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model.__init__)
            *   [`Model.set_attrs()`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model.set_attrs)
            *   [`Model.excluded_keys`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model.excluded_keys)
            *   [`Model.uid`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model.uid)
            *   [`Model.data_endpoint()`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model.data_endpoint)
            *   [`Model.query_endpoint()`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model.query_endpoint)
            *   [`Model.parse()`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model.parse)
            *   [`Model.refresh()`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model.refresh)
            *   [`Model.unpack_attributes()`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model.unpack_attributes)
            *   [`Model.pack_attributes()`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model.pack_attributes)
            *   [`Model.encode()`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model.encode)
            *   [`Model.cached`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model.cached)
            *   [`Model.clear()`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model.clear)
            *   [`Model.get_scope_name()`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model.get_scope_name)

        *   [`APIResponse`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.APIResponse)
            *   [`APIResponse.IDENTIFIER`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.APIResponse.IDENTIFIER)
            *   [`APIResponse.__init__()`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.APIResponse.__init__)
            *   [`APIResponse.excluded_keys`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.APIResponse.excluded_keys)
            *   [`APIResponse.uid`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.APIResponse.uid)
            *   [`APIResponse.data_endpoint()`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.APIResponse.data_endpoint)

    *   [The `product` module](https://my-magento.readthedocs.io/en/latest/product.html)
        *   [`Product`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product)
            *   [`Product.STATUS_ENABLED`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.STATUS_ENABLED)
            *   [`Product.STATUS_DISABLED`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.STATUS_DISABLED)
            *   [`Product.VISIBILITY_NOT_VISIBLE`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.VISIBILITY_NOT_VISIBLE)
            *   [`Product.VISIBILITY_CATALOG`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.VISIBILITY_CATALOG)
            *   [`Product.VISIBILITY_SEARCH`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.VISIBILITY_SEARCH)
            *   [`Product.VISIBILITY_BOTH`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.VISIBILITY_BOTH)
            *   [`Product.DOCUMENTATION`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.DOCUMENTATION)
            *   [`Product.IDENTIFIER`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.IDENTIFIER)
            *   [`Product.__init__()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.__init__)
            *   [`Product.excluded_keys`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.excluded_keys)
            *   [`Product.update_stock()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.update_stock)
            *   [`Product.update_status()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.update_status)
            *   [`Product.update_price()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.update_price)
            *   [`Product.update_special_price()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.update_special_price)
            *   [`Product.update_name()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.update_name)
            *   [`Product.update_description()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.update_description)
            *   [`Product.update_metadata()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.update_metadata)
            *   [`Product.add_categories()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.add_categories)
            *   [`Product.remove_categories()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.remove_categories)
            *   [`Product.update_attributes()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.update_attributes)
            *   [`Product.update_custom_attributes()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.update_custom_attributes)
            *   [`Product.add_product_link()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.add_product_link)
            *   [`Product.delete_product_link()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.delete_product_link)
            *   [`Product.get_orders()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.get_orders)
            *   [`Product.get_order_items()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.get_order_items)
            *   [`Product.get_invoices()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.get_invoices)
            *   [`Product.get_customers()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.get_customers)
            *   [`Product.delete()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.delete)
            *   [`Product.get_product_links()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.get_product_links)
            *   [`Product.get_children()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.get_children)
            *   [`Product.children`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.children)
            *   [`Product.link`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.link)
            *   [`Product.categories`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.categories)
            *   [`Product.media_gallery_entries`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.media_gallery_entries)
            *   [`Product.thumbnail`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.thumbnail)
            *   [`Product.thumbnail_link`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.thumbnail_link)
            *   [`Product.get_media_by_id()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.get_media_by_id)
            *   [`Product.encoded_sku`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.encoded_sku)
            *   [`Product.option_skus`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.option_skus)
            *   [`Product.stock`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.stock)
            *   [`Product.stock_item`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.stock_item)
            *   [`Product.stock_item_id`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.stock_item_id)
            *   [`Product.description`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.description)
            *   [`Product.special_price`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product.special_price)

        *   [`MediaEntry`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry)
            *   [`MediaEntry.MEDIA_TYPES`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.MEDIA_TYPES)
            *   [`MediaEntry.DOCUMENTATION`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.DOCUMENTATION)
            *   [`MediaEntry.IDENTIFIER`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.IDENTIFIER)
            *   [`MediaEntry.__init__()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.__init__)
            *   [`MediaEntry.query_endpoint()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.query_endpoint)
            *   [`MediaEntry.excluded_keys`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.excluded_keys)
            *   [`MediaEntry.is_enabled`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.is_enabled)
            *   [`MediaEntry.is_thumbnail`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.is_thumbnail)
            *   [`MediaEntry.link`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.link)
            *   [`MediaEntry.disable()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.disable)
            *   [`MediaEntry.enable()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.enable)
            *   [`MediaEntry.download()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.download)
            *   [`MediaEntry.add_media_type()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.add_media_type)
            *   [`MediaEntry.remove_media_type()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.remove_media_type)
            *   [`MediaEntry.set_media_types()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.set_media_types)
            *   [`MediaEntry.set_position()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.set_position)
            *   [`MediaEntry.set_alt_text()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.set_alt_text)
            *   [`MediaEntry.update()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.MediaEntry.update)

        *   [`ProductAttribute`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.ProductAttribute)
            *   [`ProductAttribute.DOCUMENTATION`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.ProductAttribute.DOCUMENTATION)
            *   [`ProductAttribute.IDENTIFIER`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.ProductAttribute.IDENTIFIER)
            *   [`ProductAttribute.__init__()`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.ProductAttribute.__init__)
            *   [`ProductAttribute.excluded_keys`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.ProductAttribute.excluded_keys)
            *   [`ProductAttribute.options`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.ProductAttribute.options)

    *   [The `category` module](https://my-magento.readthedocs.io/en/latest/category.html)
        *   [`Category`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category)
            *   [`Category.DOCUMENTATION`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.DOCUMENTATION)
            *   [`Category.IDENTIFIER`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.IDENTIFIER)
            *   [`Category.__init__()`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.__init__)
            *   [`Category.excluded_keys`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.excluded_keys)
            *   [`Category.custom_attributes`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.custom_attributes)
            *   [`Category.subcategories`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.subcategories)
            *   [`Category.subcategory_ids`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.subcategory_ids)
            *   [`Category.subcategory_names`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.subcategory_names)
            *   [`Category.all_subcategories`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.all_subcategories)
            *   [`Category.all_subcategory_ids`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.all_subcategory_ids)
            *   [`Category.products`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.products)
            *   [`Category.product_ids`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.product_ids)
            *   [`Category.skus`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.skus)
            *   [`Category.all_products`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.all_products)
            *   [`Category.all_product_ids`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.all_product_ids)
            *   [`Category.all_skus`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.all_skus)
            *   [`Category.get_products()`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.get_products)
            *   [`Category.get_orders()`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.get_orders)
            *   [`Category.get_order_items()`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.get_order_items)
            *   [`Category.get_invoices()`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.get_invoices)
            *   [`Category.add_product()`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.add_product)
            *   [`Category.remove_product()`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category.remove_product)

    *   [The `order` module](https://my-magento.readthedocs.io/en/latest/order.html)
        *   [`Order`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order)
            *   [`Order.DOCUMENTATION`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.DOCUMENTATION)
            *   [`Order.IDENTIFIER`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.IDENTIFIER)
            *   [`Order.__init__()`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.__init__)
            *   [`Order.excluded_keys`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.excluded_keys)
            *   [`Order.id`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.id)
            *   [`Order.number`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.number)
            *   [`Order.items`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.items)
            *   [`Order.item_ids`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.item_ids)
            *   [`Order.products`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.products)
            *   [`Order.get_invoice()`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.get_invoice)
            *   [`Order.customer`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.customer)
            *   [`Order.shipping_address`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.shipping_address)
            *   [`Order.bill_to`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.bill_to)
            *   [`Order.bill_to_address`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.bill_to_address)
            *   [`Order.ship_to`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.ship_to)
            *   [`Order.ship_to_address`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.ship_to_address)
            *   [`Order.payment`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.payment)
            *   [`Order.net_tax`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.net_tax)
            *   [`Order.net_total`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.net_total)
            *   [`Order.item_refunds`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.item_refunds)
            *   [`Order.total_qty_invoiced`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.total_qty_invoiced)
            *   [`Order.total_qty_shipped`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.total_qty_shipped)
            *   [`Order.total_qty_refunded`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.total_qty_refunded)
            *   [`Order.total_qty_canceled`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.total_qty_canceled)
            *   [`Order.total_qty_outstanding`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.total_qty_outstanding)
            *   [`Order.net_qty_ordered`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order.net_qty_ordered)

        *   [`OrderItem`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.OrderItem)
            *   [`OrderItem.DOCUMENTATION`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.OrderItem.DOCUMENTATION)
            *   [`OrderItem.IDENTIFIER`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.OrderItem.IDENTIFIER)
            *   [`OrderItem.__init__()`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.OrderItem.__init__)
            *   [`OrderItem.excluded_keys`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.OrderItem.excluded_keys)
            *   [`OrderItem.order`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.OrderItem.order)
            *   [`OrderItem.product`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.OrderItem.product)
            *   [`OrderItem.product_id`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.OrderItem.product_id)
            *   [`OrderItem.extension_attributes`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.OrderItem.extension_attributes)
            *   [`OrderItem.qty_outstanding`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.OrderItem.qty_outstanding)
            *   [`OrderItem.net_qty_ordered`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.OrderItem.net_qty_ordered)
            *   [`OrderItem.net_tax`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.OrderItem.net_tax)
            *   [`OrderItem.net_total`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.OrderItem.net_total)
            *   [`OrderItem.net_refund`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.OrderItem.net_refund)
            *   [`OrderItem.total_canceled`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.OrderItem.total_canceled)

    *   [The `invoice` module](https://my-magento.readthedocs.io/en/latest/invoice.html)
        *   [`Invoice`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.Invoice)
            *   [`Invoice.DOCUMENTATION`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.Invoice.DOCUMENTATION)
            *   [`Invoice.IDENTIFIER`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.Invoice.IDENTIFIER)
            *   [`Invoice.__init__()`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.Invoice.__init__)
            *   [`Invoice.excluded_keys`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.Invoice.excluded_keys)
            *   [`Invoice.id`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.Invoice.id)
            *   [`Invoice.number`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.Invoice.number)
            *   [`Invoice.order`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.Invoice.order)
            *   [`Invoice.customer`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.Invoice.customer)
            *   [`Invoice.items`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.Invoice.items)

        *   [`InvoiceItem`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.InvoiceItem)
            *   [`InvoiceItem.DOCUMENTATION`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.InvoiceItem.DOCUMENTATION)
            *   [`InvoiceItem.IDENTIFIER`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.InvoiceItem.IDENTIFIER)
            *   [`InvoiceItem.__init__()`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.InvoiceItem.__init__)
            *   [`InvoiceItem.data_endpoint()`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.InvoiceItem.data_endpoint)
            *   [`InvoiceItem.query_endpoint()`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.InvoiceItem.query_endpoint)
            *   [`InvoiceItem.excluded_keys`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.InvoiceItem.excluded_keys)
            *   [`InvoiceItem.order`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.InvoiceItem.order)
            *   [`InvoiceItem.order_item`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.InvoiceItem.order_item)
            *   [`InvoiceItem.product`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.InvoiceItem.product)
            *   [`InvoiceItem.product_id`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.InvoiceItem.product_id)

    *   [The `customer` module](https://my-magento.readthedocs.io/en/latest/customer.html)
        *   [`Customer`](https://my-magento.readthedocs.io/en/latest/customer.html#magento.models.customer.Customer)
            *   [`Customer.DOCUMENTATION`](https://my-magento.readthedocs.io/en/latest/customer.html#magento.models.customer.Customer.DOCUMENTATION)
            *   [`Customer.IDENTIFIER`](https://my-magento.readthedocs.io/en/latest/customer.html#magento.models.customer.Customer.IDENTIFIER)
            *   [`Customer.__init__()`](https://my-magento.readthedocs.io/en/latest/customer.html#magento.models.customer.Customer.__init__)
            *   [`Customer.excluded_keys`](https://my-magento.readthedocs.io/en/latest/customer.html#magento.models.customer.Customer.excluded_keys)
            *   [`Customer.name`](https://my-magento.readthedocs.io/en/latest/customer.html#magento.models.customer.Customer.name)
            *   [`Customer.is_subscribed`](https://my-magento.readthedocs.io/en/latest/customer.html#magento.models.customer.Customer.is_subscribed)
            *   [`Customer.default_billing`](https://my-magento.readthedocs.io/en/latest/customer.html#magento.models.customer.Customer.default_billing)
            *   [`Customer.default_billing_address`](https://my-magento.readthedocs.io/en/latest/customer.html#magento.models.customer.Customer.default_billing_address)
            *   [`Customer.default_shipping`](https://my-magento.readthedocs.io/en/latest/customer.html#magento.models.customer.Customer.default_shipping)
            *   [`Customer.default_shipping_address`](https://my-magento.readthedocs.io/en/latest/customer.html#magento.models.customer.Customer.default_shipping_address)
            *   [`Customer.get_orders()`](https://my-magento.readthedocs.io/en/latest/customer.html#magento.models.customer.Customer.get_orders)
            *   [`Customer.get_invoices()`](https://my-magento.readthedocs.io/en/latest/customer.html#magento.models.customer.Customer.get_invoices)
            *   [`Customer.get_ordered_products()`](https://my-magento.readthedocs.io/en/latest/customer.html#magento.models.customer.Customer.get_ordered_products)

Examples

*   [Get a Magento 2 REST API Token With MyMagento](https://my-magento.readthedocs.io/en/latest/examples/logging-in.html)
    *   [Setting the Login Credentials](https://my-magento.readthedocs.io/en/latest/examples/logging-in.html#setting-the-login-credentials)
    *   [Getting a `Client`](https://my-magento.readthedocs.io/en/latest/examples/logging-in.html#getting-a-client)
    *   [Setting Environment Variables](https://my-magento.readthedocs.io/en/latest/examples/logging-in.html#setting-environment-variables)

*   [Add discount on each product based on product price](https://my-magento.readthedocs.io/en/latest/examples/add-discount-by-product-price.html)
    *   [Solution Using MyMagento](https://my-magento.readthedocs.io/en/latest/examples/add-discount-by-product-price.html#solution-using-mymagento)

Extras

*   [Changelog](https://my-magento.readthedocs.io/en/latest/changelog.html)
    *   [v2.1.0](https://my-magento.readthedocs.io/en/latest/changelog.html#v2-1-0)

*   [Table Of Contents](https://my-magento.readthedocs.io/en/latest/contents.html)

[MyMagento](https://my-magento.readthedocs.io/en/latest/contents.html)

*   [](https://my-magento.readthedocs.io/en/latest/contents.html)
*   MyMagento - Python Magento 2 REST API Wrapper
*   [Edit on GitHub](https://github.com/TDKorn/my-magento/blob/main/docs/source/index.rst)

[Previous](https://my-magento.readthedocs.io/en/latest/contents.html "Table Of Contents")[Next](https://my-magento.readthedocs.io/en/latest/interact-with-api.html "Interacting with the API")

* * *

MyMagento - Python Magento 2 REST API Wrapper[](https://my-magento.readthedocs.io/en/latest/#mymagento-python-magento-2-rest-api-wrapper "Permalink to this heading")
======================================================================================================================================================================

[![Image 7: Logo for MyMagento: Python Magento 2 REST API Wrapper](https://my-magento.readthedocs.io/en/latest/_images/magento_orange.png)](https://my-magento.readthedocs.io/en/latest/_images/magento_orange.png)MyMagento🛒
A Python package that wraps and extends the Magento 2 REST API

[**Explore the docs »**](https://my-magento.readthedocs.io/en/latest/)

[![Image 8: PyPI Version](https://img.shields.io/pypi/v/my-magento?color=eb5202)](https://pypi.org/project/my-magento/)[![Image 9: GitHub Repository](https://img.shields.io/badge/GitHub-my--magento-4f1abc)](https://github.com/tdkorn/my-magento)[![Image 10: https://static.pepy.tech/personalized-badge/my-magento?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads](https://static.pepy.tech/personalized-badge/my-magento?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/my-magento)[![Image 11: Documentation Status](https://readthedocs.org/projects/my-magento/badge/?version=latest)](https://my-magento.readthedocs.io/en/latest/?badge=latest)

About MyMagento[](https://my-magento.readthedocs.io/en/latest/#about-mymagento "Permalink to this heading")
------------------------------------------------------------------------------------------------------------

What’s MyMagento?

`MyMagento` is a highly interconnected package that wraps and extends the Magento 2 REST API, providing a more intuitive and user-friendly interface to access and update your store.

MyMagento simplifies interaction with the Magento 2 REST API

If you’ve worked with the Magento 2 API, you’ll know that not all endpoints are created equally.

`MyMagento` aims to streamline your workflow by simplifying a variety of commonly needed API operations.

### Main Components[](https://my-magento.readthedocs.io/en/latest/#main-components "Permalink to this heading")

The [`Client`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client "magento.clients.Client")

*   Handles all API interactions

*   Supports multiple store views

*   Provides access to all other package components

The [`SearchQuery`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery "magento.search.SearchQuery") and Subclasses

*   [`execute()`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery.execute "magento.search.SearchQuery.execute") a search query on any endpoint

*   Intuitive interface for [Building Custom Search Queries](https://my-magento.readthedocs.io/en/latest/interact-with-api.html#custom-queries)

*   All predefined methods retrieve data using only 1-2 API requests

The [`Model`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model "magento.models.model.Model") Subclasses

*   Wrap all API responses in the package

*   Provide additional endpoint-specific methods to retrieve and update data

### Available Endpoints[](https://my-magento.readthedocs.io/en/latest/#available-endpoints "Permalink to this heading")

`MyMagento` is compatible with every [API endpoint](https://adobe-commerce.redoc.ly/2.3.7-admin/)

Endpoints are wrapped with a [`Model`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model "magento.models.model.Model") and [`SearchQuery`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery "magento.search.SearchQuery") subclass as follows:

| **Endpoint** | **Client Shortcut** | [`SearchQuery`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery "magento.search.SearchQuery")**Subclass** | [`Model`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.Model "magento.models.model.Model")**Subclass** |
| --- | --- | --- | --- |
| `orders` | [`Client.orders`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.orders "magento.clients.Client.orders") | [`OrderSearch`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderSearch "magento.search.OrderSearch") | [`Order`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.Order "magento.models.order.Order") |
| `orders/items` | [`Client.order_items`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.order_items "magento.clients.Client.order_items") | [`OrderItemSearch`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.OrderItemSearch "magento.search.OrderItemSearch") | [`OrderItem`](https://my-magento.readthedocs.io/en/latest/order.html#magento.models.order.OrderItem "magento.models.order.OrderItem") |
| `invoices` | [`Client.invoices`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.invoices "magento.clients.Client.invoices") | [`InvoiceSearch`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.InvoiceSearch "magento.search.InvoiceSearch") | [`Invoice`](https://my-magento.readthedocs.io/en/latest/invoice.html#magento.models.invoice.Invoice "magento.models.invoice.Invoice") |
| `products` | [`Client.products`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.products "magento.clients.Client.products") | [`ProductSearch`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductSearch "magento.search.ProductSearch") | [`Product`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.Product "magento.models.product.Product") |
| `products/attributes` | [`Client.product_attributes`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.product_attributes "magento.clients.Client.product_attributes") | [`ProductAttributeSearch`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.ProductAttributeSearch "magento.search.ProductAttributeSearch") | [`ProductAttribute`](https://my-magento.readthedocs.io/en/latest/product.html#magento.models.product.ProductAttribute "magento.models.product.ProductAttribute") |
| `categories` | [`Client.categories`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.categories "magento.clients.Client.categories") | [`CategorySearch`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.CategorySearch "magento.search.CategorySearch") | [`Category`](https://my-magento.readthedocs.io/en/latest/category.html#magento.models.category.Category "magento.models.category.Category") |
| `customers` | [`Client.customers`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.customers "magento.clients.Client.customers") | [`CustomerSearch`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.CustomerSearch "magento.search.CustomerSearch") | [`Customer`](https://my-magento.readthedocs.io/en/latest/customer.html#magento.models.customer.Customer "magento.models.customer.Customer") |
| `endpoint` | `Client.search('endpoint')` | [`SearchQuery`](https://my-magento.readthedocs.io/en/latest/search_module.html#magento.search.SearchQuery "magento.search.SearchQuery") | [`APIResponse`](https://my-magento.readthedocs.io/en/latest/model.html#magento.models.model.APIResponse "magento.models.model.APIResponse") |

…

⚙ Installing MyMagento[](https://my-magento.readthedocs.io/en/latest/#installing-mymagento "Permalink to this heading")
------------------------------------------------------------------------------------------------------------------------

To install using `pip`:

pip install my-magento

Please note that `MyMagento` requires `Python >= 3.10`

…

QuickStart: Login with MyMagento[](https://my-magento.readthedocs.io/en/latest/#quickstart-login-with-mymagento "Permalink to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

`MyMagento` uses the [`Client`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client "magento.clients.Client") class to handle all interactions with the API.

Tip

See [Get a Magento 2 REST API Token With MyMagento](https://my-magento.readthedocs.io/en/latest/examples/logging-in.html#logging-in) for full details on generating an access token

### Setting the Login Credentials[](https://my-magento.readthedocs.io/en/latest/#setting-the-login-credentials "Permalink to this heading")

To generate an [`ACCESS_TOKEN`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.ACCESS_TOKEN "magento.clients.Client.ACCESS_TOKEN") you’ll need to [`authenticate()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.authenticate "magento.clients.Client.authenticate") your [`USER_CREDENTIALS`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.USER_CREDENTIALS "magento.clients.Client.USER_CREDENTIALS").

Creating a [`Client`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client "magento.clients.Client") requires a `domain`, `username`, and `password` at minimum.

>>> domain = 'website.com'
>>> username ='username'
>>> password = 'password'

If you’re using a local installation of Magento you’ll need to set `local=True`. Your domain should look like this:

>>> domain = '127.0.0.1/path/to/magento'

…

### Getting a [`Client`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client "magento.clients.Client")[](https://my-magento.readthedocs.io/en/latest/#getting-a-client "Permalink to this heading")

#### Option 1: Initialize a [`Client`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client "magento.clients.Client") Directly[](https://my-magento.readthedocs.io/en/latest/#option-1-initialize-a-client-directly "Permalink to this heading")

from magento import Client

>>> api = Client(domain, username, password, **kwargs)

#### Option 2: Call [`get_api()`](https://my-magento.readthedocs.io/en/latest/modules.html#magento.get_api "magento.get_api")[](https://my-magento.readthedocs.io/en/latest/#option-2-call-get-api "Permalink to this heading")

import magento

>>> api = magento.get_api(**kwargs)

[`get_api()`](https://my-magento.readthedocs.io/en/latest/modules.html#magento.get_api "magento.get_api") takes the same keyword arguments as the [`Client`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client "magento.clients.Client")

*   If the `domain`, `username`, or `password` are missing, it will attempt to use the following environment variables:

import os

os.environ['MAGENTO_DOMAIN'] = domain
os.environ['MAGENTO_USERNAME']= username
os.environ['MAGENTO_PASSWORD']= password

…

### Getting an [`ACCESS_TOKEN`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.ACCESS_TOKEN "magento.clients.Client.ACCESS_TOKEN")[](https://my-magento.readthedocs.io/en/latest/#getting-an-access-token "Permalink to this heading")

Unless you specify `login=False`, the [`Client`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client "magento.clients.Client") will automatically call [`authenticate()`](https://my-magento.readthedocs.io/en/latest/clients.html#magento.clients.Client.authenticate "magento.clients.Client.authenticate") once initialized:

>> api.authenticate()

|[ MyMagento | website_username ]|:  Authenticating username on website.com...
|[ MyMagento | website_username ]|:  Logged in to username

[Previous](https://my-magento.readthedocs.io/en/latest/contents.html "Table Of Contents")[Next](https://my-magento.readthedocs.io/en/latest/interact-with-api.html "Interacting with the API")

* * *

© Copyright 2023, Adam Korn. Revision `cae9ef27`.

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/).
