# Source: https://firebase.google.com/docs/functions/networking.md.txt

<br />

The simplicity ofCloud Functionslets you quickly develop code and run it in a serverless environment. At moderate scale, the cost of running functions is low, and optimizing your code might not seem like a high priority. As your deployment scales up, however, optimizing your code becomes increasingly important.

This document describes how to optimize networking for your functions. Some of the benefits of optimizing networking are as follows:

- Reduce CPU time spent in establishing new outbound connections at each function call.
- Reduce the likelihood of running out of connection or DNS[quotas](https://cloud.google.com/functions/quotas).

## Maintaining Persistent Connections

This section gives examples of how to maintain persistent connections in a function. Failure to do so can result in quickly exhausting connection quotas.

The following scenarios are covered in this section:

- HTTP/S
- Google APIs

### HTTP/S Requests

The optimized code snippet below shows how to maintain persistent connections instead of creating a new connection upon every function invocation:  

### Node.js

```javascript
const http = require('http');
const functions = require('firebase-functions');

// Setting the `keepAlive` option to `true` keeps
// connections open between function invocations
const agent = new http.Agent({keepAlive: true});

exports.function = functions.https.onRequest((request, response) => {
    req = http.request({
        host: '',
        port: 80,
        path: '',
        method: 'GET',
        agent: agent, // Holds the connection open after the first invocation
    }, res => {
        let rawData = '';
        res.setEncoding('utf8');
        res.on('data', chunk => { rawData += chunk; });
        res.on('end', () => {
            response.status(200).send(`Data: ${rawData}`);
        });
    });
    req.on('error', e => {
        response.status(500).send(`Error: ${e.message}`);
    });
    req.end();
});
```

### Python

```python
from firebase_functions import https_fn
import requests

# Create a global HTTP session (which provides connection pooling)
session = requests.Session()

@https_fn.on_request()
def connection_pooling(request):

    # The URL to send the request to
    url = "http://example.com"

    # Process the request
    response = session.get(url)
    response.raise_for_status()
    return https_fn.Response("Success!")
    
```

This HTTP function uses a connection pool to make HTTP requests. It takes a request object (`flask.Request`) and returns the response text, or any set of values that can be turned into a`Response`object using[`make_response`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.make_response).

### Accessing Google APIs

The example below uses[Cloud Pub/Sub](https://cloud.google.com/pubsub/docs/reference/libraries), but this approach also works for other client libraries---for example,[Cloud Natural Language](https://cloud.google.com/natural-language/docs/reference/libraries)or[Cloud Spanner](https://cloud.google.com/spanner/docs/reference/libraries). Note that performance improvements may depend on the current implementation of particular client libraries.

Creating a Pub/Sub client object results in one connection and two DNS queries per invocation. To avoid unnecessary connections and DNS queries, create the Pub/Sub client object in global scope as shown in the sample below:  

### node.js

```javascript
const PubSub = require('@google-cloud/pubsub');
const functions = require('firebase-functions');
const pubsub = PubSub();

exports.function = functions.https.onRequest((req, res) => {
    const topic = pubsub.topic('');

    topic.publish('Test message', err => {
        if (err) {
            res.status(500).send(`Error publishing the message: ${err}`);
        } else {
            res.status(200).send('1 message published');
        }
    });
});
```

### Python

```python
import os

from firebase_functions import https_fn
from google.cloud import pubsub_v1

# from firebase_functions import https_fn
# Create a global Pub/Sub client to avoid unneeded network activity
pubsub = pubsub_v1.PublisherClient()

@https_fn.on_request()
def gcp_api_call(request):

    project = os.getenv("GCP_PROJECT")
    request_json = request.get_json()

    topic_name = request_json["topic"]
    topic_path = pubsub.topic_path(project, topic_name)

    # Process the request
    data = b"Test message"
    pubsub.publish(topic_path, data=data)

    return https_fn.Response("1 message published")
    
```

This HTTP function uses a cached client library instance to reduce the number of connections required per function invocation. It takes a request object (`flask.Request`) and returns the response text, or any set of values that can be turned into a`Response`object using[`make_response`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.make_response).

The`GCP_PROJECT`environment variable is set automatically in the Python 3.7 runtime. In later runtimes, make sure to specify it on function deployment. See[Configure environment variables](https://cloud.google.com/run/docs/configuring/services/environment-variables).

### Outbound connections

#### Outbound request timeouts

There is a timeout after 10 minutes of idle time for requests from your function to the VPC network. For requests from your function to the internet, there is a timeout after 20 minutes of idle time.

#### Outbound connection resets

Connection streams from your function to both the[VPC network](https://cloud.google.com/run/docs/configuring/connecting-vpc)and internet can be occasionally terminated and replaced when underlying infrastructure is restarted or updated. If your application reuses long-lived connections, we recommend that you configure your application to re-establish connections to avoid the reuse of a dead connection.

## Load-testing Your Function

To measure how many connections your function performs on average, deploy it as a HTTP function and use a performance-testing framework to invoke it at certain QPS. One possible choice is[Artillery](https://artillery.io/), which you can invoke with a single line:  

```
$ artillery quick -d 300 -r 30 URL
```

This command fetches the given URL at 30 QPS for 300 seconds.

After performing the test, check the usage of your connection quota on the[Cloud FunctionsAPI quota page](https://console.cloud.google.com/apis/api/cloudfunctions.googleapis.com/quotas)in Cloud Console. If the usage is consistently around 30 (or its multiple), you are establishing one (or several) connections in every invocation. After you optimize your code, you should see a few (10-30) connections occur only at the beginning of the test.

You can also compare the CPU cost before and after the optimization on the CPU quota plot on the same page.