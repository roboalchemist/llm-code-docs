# Source: https://www.activepieces.com/docs/install/architecture/performance.md

# Performance & Benchmarking

## Performance

On average, Activepieces (self-hosted) can handle 95 flow executions per second on a single instance (including PostgreSQL and Redis) with under 300ms latency.\
It can scale up much more with increasing instance resources and/or adding more instances.\
\
The result of **5000** requests with concurrency of **25**

```
This is ApacheBench, Version 2.3 <$Revision: 1913912 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 500 requests
Completed 1000 requests
Completed 1500 requests
Completed 2000 requests
Completed 2500 requests
Completed 3000 requests
Completed 3500 requests
Completed 4000 requests
Completed 4500 requests
Completed 5000 requests
Finished 5000 requests


Server Software:        
Server Hostname:        localhost
Server Port:            4200

Document Path:          /api/v1/webhooks/GMtpNwDsy4mbJe3369yzy/sync
Document Length:        16 bytes

Concurrency Level:      25
Time taken for tests:   52.087 seconds
Complete requests:      5000
Failed requests:        0
Total transferred:      1375000 bytes
HTML transferred:       80000 bytes
Requests per second:    95.99 [#/sec] (mean)
Time per request:       260.436 [ms] (mean)
Time per request:       10.417 [ms] (mean, across all concurrent requests)
Transfer rate:          25.78 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       1
Processing:    32  260  23.8    254     756
Waiting:       31  260  23.8    254     756
Total:         32  260  23.8    254     756

Percentage of the requests served within a certain time (ms)
  50%    254
  66%    261
  75%    267
  80%    272
  90%    289
  95%    306
  98%    327
  99%    337
 100%    756 (longest request)
```

#### Benchmarking

Here is how to reproduce the benchmark:

1. Run Activepieces with PostgreSQL and Redis with the following environment variables:

```env  theme={null}
AP_EXECUTION_MODE=SANDBOX_CODE_ONLY
AP_FLOW_WORKER_CONCURRENCY=25
```

2. Create a flow with a Catch Webhook trigger and a webhook Return Response action.

   <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/simple-webhook-flow.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3932ff8bbe1bc53cb4968458b5d617b0" alt="Simple Webhook Flow" data-og-width="719" width="719" data-og-height="847" height="847" data-path="resources/screenshots/simple-webhook-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/simple-webhook-flow.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=f7f3771d8d0ddf3ea65aceaf8989177f 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/simple-webhook-flow.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=5f63616909a658a7c36ccf60e376af4f 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/simple-webhook-flow.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=76c7ada115f8b4a9cc2e5ee37d5ec064 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/simple-webhook-flow.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=38ead94383a663547736a50dcd43e372 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/simple-webhook-flow.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=6609bba1e3550712e3bf97019d8b33eb 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/simple-webhook-flow.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0b43adade90df31e0c038cec274282a9 2500w" />
3. Get the webhook URL from the webhook trigger and append `/sync` to it.
4. Install a benchmark tool like [ab](https://httpd.apache.org/docs/2.4/programs/ab.html):

```bash  theme={null}
sudo apt-get install apache2-utils
```

5. Run the benchmark:

```bash  theme={null}
ab -c 25 -n 5000 http://localhost:4200/api/v1/webhooks/GMtpNwDsy4mbJe3369yzy/sync
```

6. Check the results:

Instance specs used to get the above results:

* 16GB RAM
* AMD Ryzen 7 8845HS (8 cores, 16 threads)
* Ubuntu 24.04 LTS

<Tip>
  These benchmarks are based on running Activepieces in `SANDBOX_CODE_ONLY` mode. This does **not** represent the performance of Activepieces Cloud, which uses a different sandboxing mechanism to support multi-tenancy. For more information, see [Sandboxing](/install/architecture/workers#sandboxing).
</Tip>
