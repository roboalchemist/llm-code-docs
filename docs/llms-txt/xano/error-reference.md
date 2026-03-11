# Source: https://docs.xano.com/troubleshooting-and-support/error-reference.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Error Reference

You can use this page to quickly search for and discover solutions to some common Xano errors.

<Accordion title="Not Supported. Please upgrade your Xano instance.">
  This message indicates that you are trying to access a feature that is not currently enabled on your Xano account and requires an upgrade.

  To add most features to your plan, you can head to your Billing screen and upgrade to the appropriate package.

  If you have already upgraded and still do not have access to the feature in question, please reach out to support directly.
</Accordion>

<Accordion title="Invalid name">
  This error usually arises when you have a step in a function stack or otherwise attempt to access a table that does not / no longer exists.

  The solution is to recreate any offending steps so that only existing tables are referenced.

  This can also happen if the authentication settings for an endpoint do not have a table selected.
</Accordion>

<Accordion title="Variable is not an array.">
  This message indicates that you are trying to apply array functions or filters to a variable that is not an array. An array is a list of values or objects separated by commas and enclosed inside \[brackets]

  ```
  ["Ford", "BMW", "Fiat"]
  ```

  Make sure the variable you are referencing is an array.
</Accordion>

<Accordion title="Invalid token">
  You might see this error message if you are trying to run an endpoint that requires authentication, but are not providing a valid authentication token.

  When testing your endpoints, you can choose an auth token using the option shown below to make sure you are always providing a valid token.

    <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/16cd786b-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=3bb1b0295bb8f39cfd1896fd4297e22c" alt="" width="652" height="495" data-path="images/16cd786b-image.jpeg" />
</Accordion>

<Accordion title="Variable is not text. Are you referencing a full object?">
  You might see this error if you are trying to apply a text filter to a value that is not text (or interchangeable with text, such as an integer).

  For example, if you have a JSON object called "api\_1" and you are trying to apply a text transformation to a value inside of that object, it is likely that you are not using proper [dot notation](/the-function-stack/building-with-visual-development#dot-notation) to target that text value directly.
</Accordion>

<Accordion title="Removal of entry with a stream is not supported">
  When using the Stream return type, certain functions are not supported; specifically anything that has to do with modifying the dataset that the For Each loop is iterating through, such as For Each Loop: Remove Entry
</Accordion>

<Accordion title="Please use a numerically indexed array">
  This error message is triggered when referencing something that is not an array, or an improperly formatted array, in a [For Each loop](/the-function-stack/functions/data-manipulation/loops#for-each-loop).

  The solution would be to make sure you're targeting a proper array when building For Each loops.
</Accordion>

<Accordion title="Unable to decode input">
  This error occurs when malformed input is sent to an API endpoint and you are using Get All Input to gather any data sent to the endpoint. Make sure that any data being sent to your Xano APIs are in valid JSON format.
</Accordion>

<Accordion title="Potential infinite loop. Please limit your loop operations to under x.">
  In Xano, we have some protections around loops to prevent infinite looping. Make sure that you are limiting your loops in a way so that they do not surpass the number of iterations allowed as defined in the error message.
</Accordion>

<Accordion title="Invalid parameter count based on format">
  When using [Direct Database Query](/the-function-stack/functions/database-requests/direct-database-query) and dynamically specifying values, make sure that the number of arguments you define in your query statement match the number of substitutions defined in the Statement Arguments section.
</Accordion>

<Accordion title="Text filter requires a scalar value">
  A scalar value just means a single value, not a list or a JSON object. You'll see this error if you attempt to apply a text-based transformation filter to something that is not a scalar value.

  This can happen if you are trying to target a value inside of an array or object and you are using incorrect [dot notation](/the-function-stack/building-with-visual-development#dot-notation).
</Accordion>

<Accordion title="Unable to locate input">
  This error can happen if you are trying to reference an input that is either not provided when making a request to the API, or an input that no longer exists.
</Accordion>

<Accordion title="SQLSTATE errors">
  There are several variations of these errors. Further into the message will usually give you a clue as to what the exact error means, but here are some common things to look out for.

  * **Disk Full** - This typically means that your instance is out of database storage. You will need to head to your Billing screen to add additional database storage.

  * **Index building errors** - These can occur if you are trying to add a normal index to an extremely large column (such as text descriptions) or adding too many columns to a single index. Please review our documentation on indexing to make sure you are building indexes properly, and for long text fields, consider using Fuzzy Search instead.
</Accordion>

<Accordion title="(value) is not one of the allowable values">
  This error occurs when you are using an Enum field but trying to supply a value to that field that is not one of the allowable options you've specified in the database or input settings.

  To remedy this, you can update the allowable values on the enum field, or switch to a text field if you need more freedom to specify new values.
</Accordion>

<Accordion title="Unable to locate (variable name).(path)">
  This error indicates that you are trying to reference a path inside of a variable that does not exist.

  For example, sometimes an external API request will not return certain values in every response, or if there is pagination involved, it has run out of items to return, causing this message to appear when you try to work with the data expected inside of that response.

  There can be a number of ways to resolve this error, including:

  * Adding [conditional logic](/the-function-stack/functions/data-manipulation/conditional)to determine the steps to take based on the existence of a value

  * Using the GET filter or [Conditional Set Filters](/the-function-stack/filters/manipulation#set_conditional)to change the behavior based on if the value is provided
</Accordion>

<Accordion title="Unknown Error">
  This error message indicates that Xano has run into an unhandled exception, and we don't have a specific error message defined for the issue you're experiencing.

  If this is happening when working in a database table, or somewhere else in Xano **outside of a function stack**, it's best to reach out to support to determine the cause.

  If this is happening when calling an API or using Run & Debug, it typically indicates one of the following:

  * Memory-related issues. Your instance is not equipped to fully complete the request and is hitting resource limits.

  * Applying a filter incorrectly. Somewhere in your function stack, you have a filter applied to an incorrect data type, such as trying to use an Array-based filter on a single value.

  Due to the ambiguous nature of this error, if further assistance is required to diagnose the source of the problem, please don't hesitate to reach out to support for clarification.
</Accordion>

<Accordion title="Numbers are required for mathematical operations">
  This error indicates that you are trying to apply a mathematical filter or function to a value that is not a number.

  To resolve this, please check the following:

  * Are you targeting a number directly, and is it actually a number?

    * It is possible to store numbers as text strings, and while these are typically interchangeable, in some cases you may find that retaining an integer or decimal data type is necessary. You can apply filters such as **to\_int** or **to\_dec** to change the data type based on your needs

  * Are you using proper [dot notation](/the-function-stack/building-with-visual-development#dot-notation)?

    * You might be trying to target a value inside of an object, but are not using proper dot notation to reference that value, or perhaps the value does not exist.
</Accordion>

<Accordion title="Failed to Execute">
  This is a rare error that can occur when using Create File Resource / a File Resource input with certain files, or when using a Lambda function.

  * **Create File Resource / File Resource Input**

    * When this error appears using Create File Resource, or with a File Resource input, this indicates that there is a problem with the file itself preventing proper upload to Xano. Make sure that you are able to otherwise read / access the file as expected, and if you are, please reach out to Xano support so we can troubleshoot this further. You will need to provide the file to us so we can determine the cause.

  * **Lambda Functions**

    * This error usually just indicates an error in your Lambda function's code.
</Accordion>

<Accordion title="This name conflicts with another API endpoint.">
  This error indicates that the name you are trying to use for another API endpoint conflicts with an existing API. It's important to remember that URL parameters need to be considered as well.

  For example, assuming these endpoints have the same verb (such as POST), an endpoint named **/auth/me** would conflict with an endpoint named **/auth/\{user\_id}**, because Xano has no way of knowing if "me" should actually be a value for user\_id.
</Accordion>

<Accordion title="Authentication Required">
  This message indicates that you are trying to call an API endpoint or function that requires authentication to execute, but an authentication token was not provided.

  To resolve, make sure you are providing an authentication token when calling the API endpoint in question.
</Accordion>


Built with [Mintlify](https://mintlify.com).