# Source: https://docs.instabug.com/references/report-data/logging/network-logging-react-native.md

# Network Logging - React Native

Network logs are automatically collected by Luciq when possible. There are many way to configure and manipulate these logs from the code.

### Disable and Enable Request Logging

By default, request logging is enabled. It can be disabled using the API to the right.

```javascript
NetworkLogger.setEnabled(false);
```

### Importing the Network Logger

You'll first need to import the Network Logger in order to be able start logging network requests. You can use this statement to import it.

```javascript
import { NetworkLogger } from '@luciq/react-native';
```

### Omitting Requests from Logs

You can omit requests from being logged based on either their request or response details.

`setRequestFilterExpression` allows you to specify an expression to be evaluated against every request and response to determine if the request should be included in logs or not.

The code in the example below excludes all requests made to URLs that have the request header `accept` set to `application/json`.

```javascript
NetworkLogger.setRequestFilterExpression('network.requestHeaders[\'accept\'] === \'application/json\'')
```

### Obfuscating Data

Both requests and responses can be obfuscated if required. You can obfuscate user sensitive data in requests, like authentication tokens for example, without filtering out the whole request. As with requests, the response object, as well as the response data, could be modified for obfuscation purposes before they are logged.

{% tabs %}
{% tab title="Obfuscate Request" %}

```javascript
NetworkLogger.setNetworkDataObfuscationHandler(async (networkData) => {
      networkData.requestHeaders = {'Content-Type': 'application/json', 'TestHeader': 'some-header2'}
      return networkData;
    });
```

{% endtab %}

{% tab title="Obfuscate Response" %}

```python
NetworkLogger.setNetworkDataObfuscationHandler(async (networkData) => {
      networkData.response = {};
      return networkData;
    });
```

{% endtab %}
{% endtabs %}

### Progress Event Handler

If you'd like to execute a block of code whenever a network request is made, you can use this event handler. This handler returns the total bytes, as well as, the loaded bytes so far.

```javascript
NetworkLogger.setProgressHandlerForRequest((total, loaded) => {
});
```
