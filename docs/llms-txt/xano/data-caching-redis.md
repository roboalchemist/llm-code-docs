# Source: https://docs.xano.com/xanoscript/function-reference/data-caching-redis.md

# Source: https://docs.xano.com/the-function-stack/functions/data-caching-redis.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Caching (Redis)

## What is Data Caching?

Xano provides a data caching service, powered by Redis, that allows you to temporarily store data in memory for high-performance data retrieval and storage purposes. This is great for storing temporary data that needs to be quickly generated and accessed for a period of time.

If you are retrieving data from a database or an external API, for example, that you know never, or very infrequently, changes, using data caching can be incredibly valuable.

### **How long can I store data in the Data Cache?**

Through the cache functions you use, you can manually set how long data gets stored, or you can expect it to naturally get overwritten once it reaches the 100MB limit.

<Warning>
  **Note**

  As mentioned above, **Data Caching is temporary storage** - so never store something that can't be recovered - if permanent storage is required, then the database can and should be used.
</Warning>

## Caching Functions

### Set a Cache Value

Redis Cache Values work in key-value pairs. Set a Cache Value function allows you to define a key to reference the cache value in other cache functions. The data input is where you define the data you wish to be cached (the value of the pair). Ttl stands for time to live. Set this, in seconds, to determine how long to cache the data for.

**Key:** define a key name to reference the cache value by.

**Data:** select the value that you wish to cache. This will often be a variable containing data.

**TTL:** define how long, in seconds, for the cache to last. After this time expires, the query will run normally again and reset the data cache value for the specified time. Set this equal to 0 never reset the cache value.

Redis is extremely sensitive to data variation, so you may find it useful to store JSON objects as text strings for easier use of additional caching functions, such as 'removing from list'.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/fdc43f6c-image.jpeg?fit=max&auto=format&n=WBQXG-4Ngk82eYAW&q=85&s=c4c1973ca4346d3093f6717a9facf3cc" width="2304" height="1272" data-path="images/fdc43f6c-image.jpeg" />
</Frame>

### Get a Cache Value

Get a Cache Value allows you to retrieve a cache value based on the defined key of a set cache value. Get a Cache Value function also outputs a variable so that you can use the data from the cache value in other functions or in the response.

**Key**: enter in the key of a set cache value that you wish to retrieve.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/e10f7803-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=d75bc8d0c2e1d8ee25207e65b54e81a4" width="2304" height="1272" data-path="images/e10f7803-image.jpeg" />
</Frame>

### Has a Cache Value

Has a Cache Value allows you to determine whether or not a cache value exists based on the key. This function will return a boolean of true or false as a variable depending on if the cache value exists.

**Key**: enter a key to find if a cache value exists.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f8f10c7b-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=50654b557ebab82563980d93ef53f0b2" width="2304" height="1274" data-path="images/f8f10c7b-image.jpeg" />
</Frame>

The return variable result will look like this:

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/581ff126-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=9aecba528a94cdb8056a5a147039e32d" width="960" height="540" data-path="images/581ff126-image.jpeg" />
</Frame>

Because the key "user\_info" has a cache value, the return variable is true.

### Delete Cache Value

Delete cache value will delete a cache value based on the key of the cache value.

**Key**: enter in the key of a set cache value in order to delete it.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/77691c5c-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=0039738675c9e66576ab735151e8f52c" width="2304" height="1270" data-path="images/77691c5c-image.jpeg" />
</Frame>

If we try to Get Cache Value for the same key after it is deleted, the response will come back as false.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/7d6bcd9e-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=0521612a43ba290d6cc9da48792bec48" width="2258" height="1360" data-path="images/7d6bcd9e-image.jpeg" />
</Frame>

In this example, we are doing a Get Cache Value for the same key that is being deleted in the prior step. We will try to return the return variable of the Get Cache Value.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/227d55a0-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=776cf5721645d033d7e063b0d7249dd5" width="960" height="540" data-path="images/227d55a0-image.jpeg" />
</Frame>

The Get Cache Value returned a result of false because the cache value was already deleted.

### Increment Cache Value

Increment Cache Value allows you create an Incremental Cache Value by choosing a key and choosing the value to increment by. The incremented value is returned in a variable so you can perform logic based on what the count is.

**Key**: set a key name.

**By**: choose the value to increment by.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/3aba13a7-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=11dd8695ab208b6e5b58b8fdd3ebac05" width="958" height="746" data-path="images/3aba13a7-image.jpeg" />
</Frame>

Increment Cache Value can act as a lightweight counter. The incremental values are stored on temporary memory, so keep in mind, if the server were to ever restart then the count would be reset.

Use case examples include a promotion where something is available or accessible for the first 100 users. Or perhaps, the 100th user wins the promotion.

### Decrement Cache Value

Decrement Cache Value allows you to decrement a cache value by choosing a key and a value to decrement it by. The decremented cache value is returned in a variable so you can perform additional logic based on its value.

**Key**: create a key name for the decrement cache value.

**By**: choose the value to decrement by.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/17006079-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=d389667d774213ab9a0af3fa13206c35" width="948" height="764" data-path="images/17006079-image.jpeg" />
</Frame>

Decrement cache value is similar to increment cache value but it decreases the value. You can also use this as a counter stored on temporary memory.

### Get Cache Keys

Get Cache Keys allows you to retrieve cache keys that match a searched value. You can use "\*" as a wildcard to search. Only putting in "\*" will grab all keys but you can combine it with with text string to narrow your search.

**Search**: enter in they name of the keys you are searching for. Use "\*" as a wildcard.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/3435fb05-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=b0a51130e3603b475c59d10ed62c0698" width="2304" height="1273" data-path="images/3435fb05-image.jpeg" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/1b533931-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=fd54b6954e3d8cdf4d1619ad088434ae" width="2304" height="1223" data-path="images/1b533931-image.jpeg" />
</Frame>

Here's an example of combining the wildcard "\*" with text to retrieve cache key.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c1d94744-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=a9835a4479ac747a3636977dfa5ed33d" width="2304" height="1214" data-path="images/c1d94744-image.jpeg" />
</Frame>

### Add to Beginning of List

Add to Beginning of List allows you to insert a value at the start of the list stored at a key you specify.

**Key**: set a key name.

**Value**: the value to add to the beginning of the list.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/40930774-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=1c6773689abc94f3d7f42c51d5290eca" width="596" height="514" data-path="images/40930774-image.jpeg" />
</Frame>

### Add to End of List

Add to End of List allows you to insert a specified value at the tail end of the list, stored at the key you specify.

**Key**: set a key name.

**Value**: the value to add to the end of the list

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/28e9c1a6-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=98645fd966cbad45de30c5f94d63a492" width="599" height="518" data-path="images/28e9c1a6-image.jpeg" />
</Frame>

### Remove from Beginning of List

Allows you to remove the first element from a list stored at a key you specify.

**Key**: the key that you'd like to remove the value from

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/0a7f6a47-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=ed39fca66d22589cab1feb90d9c3fb89" width="596" height="439" data-path="images/0a7f6a47-image.jpeg" />
</Frame>

### Remove from End of List

Allows you to remove the last element from a list stored at a key you specify.

**Key**: the key that you'd like to remove the value from

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/0a7f6a47-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=ed39fca66d22589cab1feb90d9c3fb89" width="596" height="439" data-path="images/0a7f6a47-image.jpeg" />
</Frame>

### Remove from List

Allows you to remove a specified item from a list. You can choose to remove all specified values, or a maximum amount.

**Key**: the key that you'd like to remove the value from

**Value**: the value you would like to remove

**Count**: the amount of values you want to remove. The default (0) will remove all, or you can specify a maximum.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/56689723-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=5083454ad4e48604491d050efd2e7bb1" width="597" height="455" data-path="images/56689723-image.jpeg" />
</Frame>

### Get Length of List

Allows you to return the current length of a list as a variable.

**Key**: specifies the key you would like to reference

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/76028141-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=5901838b177ed3c163cd80b59ea27a0b" width="597" height="428" data-path="images/76028141-image.jpeg" />
</Frame>

### Get Elements from List

Allows you to retrieve a range of values from a list.

**Key**: specify which key you would like to reference.

**Start**: identifies the start of the elements you would like to retrieve.

**Stop**: identifies the end of the elements you would like to retrieve.

You can use negative values to represent the end of the list (ex. -1 is the last element, -2 is the second to last, and so on). The start and stop parameters are also inclusive. This means that the results you are given will include the elements at the positions you start and end with.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f701200d-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=7ccf1f1954c6628ef30c4256131bafc0" width="595" height="470" data-path="images/f701200d-image.jpeg" />
</Frame>

### Rate Limit

Xano allows you to set rate limits on your queries so that you can limit the requests per given time period that an API endpoint can be called.

The Rate Limit function comes with a few settings for configuration.

**Key**: define a key for the rate limit.

**Max**: set the max amount of requests allowed in the given time or TTL.

**TTL**: set the time to live, in seconds, of each cycle.

**Error**: optionally include an error message. If you include an error message, when the Rate Limit is reached it will automatically throw an error and display this message. If you do not, the Rate Limit will output a boolean of false when the Rate Limit is reached. This can be used if you wish to create custom logic for what happens when the Rate Limit is reached.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/aceac9fb-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=5bac56a0e71d1b674853adca9919aea4" width="2304" height="1269" data-path="images/aceac9fb-image.jpeg" />
</Frame>


Built with [Mintlify](https://mintlify.com).