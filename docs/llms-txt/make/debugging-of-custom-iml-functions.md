# Source: https://developers.make.com/custom-apps-documentation/debug-your-app/debugging-of-custom-iml-functions.md

# Custom IML functions

To debug your IML functions, output the code and use a tool of your choosing.

## Output a message to the dev console

You can use `debug` inside your IML functions to print a message or mid-results of your code.\
During the function execution, debug messages are visible inside the console of your browser.

{% hint style="info" %}
To open the developer console in Google Chrome, open the Chrome Menu in the upper-right-hand corner of the browser window and select **More Tools > Developer Tools**. You can also use **Option + ⌘ + J** (on macOS), or **Shift + CTRL + J** (on Windows/Linux).
{% endhint %}

{% tabs %}
{% tab title="IML function" %}

```javascript
function add(a, b) {
    	let sum = a + b;
    
        //instead of usual console.log(), use debug().
        debug("a = " + a) 
	debug('b = ' + b)
	debug(`a+b = ${sum}`)
	
	return sum;
}
```

{% hint style="info" %}
By using `debug()` you can understand what data you are manipulating inside a function.
{% endhint %}
{% endtab %}

{% tab title="Console messages" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-26f6fd333265588d0e2d8fc8e184e7a9a0c2ae96%2Foutput_debug_customIML.png?alt=media" alt="" width="419"><figcaption></figcaption></figure></div>

{% hint style="info" %}
During the run of a module, IML functions called inside this module will also run.

All debug messages that you specified in the IML function are available inside the developer console of your browser.
{% endhint %}
{% endtab %}
{% endtabs %}

## Debug the JavaScript snippet

To debug the output, you can use a variety of tools. Search online to find a JavaScript debugging tool that you prefer.

Here are some to choose from:

* [JS Playground](https://www.jsplayground.dev/)
* [Mozilla developer playground](https://developer.mozilla.org/fr/play)
* [RunJS](https://runjs.app/)

{% tabs %}
{% tab title="Sample code to test" %}

```javascript
function myFunction(x) {
    x = x + 1;
    //do something
    console.log(x); // outputs the value of x at this point
    return x;
}

myFunction(1);
```

{% hint style="info" %}
You can use this code to test the functionality of the JavaScript debugger to see how it works.
{% endhint %}
{% endtab %}
{% endtabs %}
