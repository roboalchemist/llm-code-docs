# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/debug-logs.md

# Debug logs

You can use the **console.log** statement in the Javascript node to log messages at specific steps in the script. This helps to verify if the script is executing as expected and to identify points of failure. You can then use the **Debug logs** options in **Dialog skill** to display all the logs generated using console.log.

Consider that in the **Order Status skill** of the **Pizza agent**,  you have logged **context** for an intent:

```markup
console.log(context);
```

* In the **Agent** page, click the **Debug  -> Debug logs** option in the left navigation menu.&#x20;
* Click the agent icon in the bottom-right corner.
* Enter the order number. Context details are displayed in the **Debug logs** window. Similarly, you can use **console.log** to log messages at specific steps in the script, as required.

{% hint style="info" %}
**Note**: In the `Debug logs` pop-up window, a maximum of 50 consecutive `Console.log` statements can be printed.
{% endhint %}
