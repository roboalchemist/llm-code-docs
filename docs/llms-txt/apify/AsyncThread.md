# Source: https://docs.apify.com/sdk/python/reference/class/AsyncThread.md

# AsyncThread<!-- -->

Class for running an asyncio event loop in a separate thread.

This allows running asynchronous coroutines from synchronous code by executingthem on an event loop that runs in its own dedicated thread.

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/AsyncThread.md#__init__)
* [**close](https://docs.apify.com/sdk/python/sdk/python/reference/class/AsyncThread.md#close)
* [**run\_coro](https://docs.apify.com/sdk/python/sdk/python/reference/class/AsyncThread.md#run_coro)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/scrapy/_async_thread.py#L23)\_\_init\_\_

* ****\_\_init\_\_**(): None

- #### Returns None

### [**](#close)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/scrapy/_async_thread.py#L70)close

* ****close**(timeout): None

- Close the event loop and its thread gracefully.

  This method cancels all pending tasks, stops the event loop, and waits for the thread to exit. If the thread does not exit within the given timeout, a forced shutdown is attempted.

  ***

  #### Parameters

  * ##### optionaltimeout: timedelta = <!-- -->timedelta(seconds=60)

    The maximum number of seconds to wait for the event loop thread to exit.

  #### Returns None

### [**](#run_coro)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/scrapy/_async_thread.py#L33)run\_coro

* ****run\_coro**(coro, timeout): Any

- Run a coroutine on an event loop running in a separate thread.

  This method schedules the coroutine to run on the event loop and blocks until the coroutine completes or the specified timeout is reached.

  ***

  #### Parameters

  * ##### coro: Coroutine

    The coroutine to run.

  * ##### optionaltimeout: timedelta = <!-- -->timedelta(seconds=60)

    The maximum number of seconds to wait for the coroutine to finish.

  #### Returns Any
