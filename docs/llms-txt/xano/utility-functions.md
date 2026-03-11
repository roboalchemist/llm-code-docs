# Source: https://docs.xano.com/xanoscript/function-reference/utility-functions.md

# Source: https://docs.xano.com/the-function-stack/functions/utility-functions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Utility Functions

## Send Email

Sends an email using a third-party mail service. Currently only supports [Resend](https://resend.com/).

### Configure

API Key Options:

* **Use Xano API Key** - Uses free credits provided by Xano for testing only. Will only allow for sends to the instance administrator's email address.
* **Use your own Resend API Key** - When you're ready to move to production, select this option to provide your own API key from Resend.

### Compose Email

| Parameter    | Purpose                             | Example                                                | Availability     |
| ------------ | ----------------------------------- | ------------------------------------------------------ | ---------------- |
| Subject      | Email subject                       | `"Welcome to our service!"`                            | Free             |
| Message      | Email body                          | `"<h1>Hello, User!</h1><p>Thanks for joining us.</p>"` | Free             |
| To           | Recipient email address             | `"<user@example.com>"`                                 | Free             |
| BCC          | Blind carbon copy email addresses   | `["<bcc@example.com>"]`                                | Requires API key |
| CC           | Carbon copy email addresses         | `["<cc@example.com>"]`                                 | Requires API key |
| From         | Sender email address                | `"<noreply@example.com>"`                              | Requires API key |
| Reply-To     | Reply-to email address              | `"<replyto@example.com>"`                              | Requires API key |
| Scheduled At | Schedule email send time (ISO 8601) | `"2023-10-01T10:00:00Z"` or `"in one minute"`          | Requires API key |

## Return

Halts execution and returns the defined result immediately. Return is useful when used in combination with [conditional statements](/the-function-stack/functions/data-manipulation/conditional) where you want to change the return based on the result of the condition.

## Try/Catch

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/GpZkdTho20E" title="Try/Catch" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

Try/catch enables you to catch any errors that may occur in a specific stack of functions and execute additional logic based on that result. This function essentially enables fully custom error handling in Xano.

**Try** - Try these functions first

**Catch** - Execute these functions if the Try statements return an error

**Finally** - Execute these functions regardless of the result

In the below example, we are starting with a Delete File function, and trying to delete a file that does not exist.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/7c70784c-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=40fcb766b6b460a4414ea7d46d68b963" width="2186" height="1074" data-path="images/7c70784c-image.jpeg" />
</Frame>

Deleting a file that does not exist returns ERROR\_CODE\_NOT\_FOUND and halts execution.

Normally, when an error occurs in the function stack, execution is halted entirely. If we wanted to deploy some customized error handling to change this behavior, we can do so by placing this function inside of a Try/Catch statement.

In the below iteration, we've moved Delete File into the Try portion of a Try/Catch statement. Now, when we run the endpoint again, the function itself is still failing, but the API itself still returns a success response.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/7c72d1e2-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=6571bf5eadad15996e1316d603319722" width="2185" height="1351" data-path="images/7c72d1e2-image.jpeg" />
</Frame>

We can then use the Catch portion to read the error, using three variables only available via Try/Catch.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/22594c85-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=7bbb01dcd00d38613945eb6ec27b44ba" width="489" height="386" data-path="images/22594c85-image.jpeg" />
</Frame>

* **code** is the error code
* **message** is the error message
* **result** will be any accompanying data. Most functions will not output a result, and only return data in **code** and **message**

When we run this again and output those variables as part of our response, you'll see that the API still returns a 'Success' result, but we can view the error message returned by our function in our Try statement.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/32984492-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=7a431c94f5bc823eb5f7534de02f3014" width="2035" height="1347" data-path="images/32984492-image.jpeg" />
</Frame>

You can then use the Finally section to determine the behavior based on the result of your Try/Catch. In the below example, we're using a conditional statement to check if the try/catch **code** variable is empty. If it is empty, we return a success message. If it is not empty (which means there was an error in our Try statements), we return an error message.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/3e649d07-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=fcba5b09ffb0b3c5e8251197121396c0" width="1546" height="600" data-path="images/3e649d07-image.jpeg" />
</Frame>

**Practical Example of using Try/Catch**

<Frame>
  <iframe src="https://www.loom.com/embed/7bcb6034e1314eeaacdf9bbc386ca8d6" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen width="640" height="360" />
</Frame>

## Throw Error

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/8f278a5e-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=e3cad52164ef85064900daec4d191cdc" width="1205" height="313" data-path="images/8f278a5e-image.jpeg" />
</Frame>

Throw Error allows you to halt execution with a custom error message. This is different from a Precondition step because it does not restrict you to specific error codes. It can be used in combination with Try/Catch or on its own.

## Post Process

Post process allows you to execute additional logic after your API has provided a response. This can be useful if you want to see a response on your front-end without waiting for any additional processing to occur, but a background task does not meet your needs.

**Example**

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f062f5c9-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=2b6e88df40af1ce0f03958715fd790e8" width="1142" height="875" data-path="images/f062f5c9-image.jpeg" />
</Frame>

In this function stack, we are setting **var\_1** with a value of "Hello" and calling an external API to send the contents of this variable.

Afterwards, we have added Post Process to update **var\_1** and send a new request to the same external API.

The function stack is set to respond with the contents of **var\_1.**

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/fe0b8cd3-image.jpeg?fit=max&auto=format&n=WBQXG-4Ngk82eYAW&q=85&s=755032d93d1c8b0c48e5ad1abc581788" width="1170" height="512" data-path="images/fe0b8cd3-image.jpeg" />
</Frame>

This means that the following will happen in sequence:

1. Set **var\_1** to "Hello!"
2. Send **var\_1** to external API
3. The Xano API responds with "Hello!"
4. Set \*\*var\_1 \*\*to "Goodbye!"
5. Send **var\_1** to external API

Below is a video of this example in action. Note how the external API recieves both 'Hello' and 'Goodbye', but the Xano API just responds with 'Hello'. *Note: the video does not contain any audio.*

Post Process will use the state of variables where it is defined. This means that while Post Process executes at the end of the function stack, the placement is still important to ensure that any variables it uses retain the appropriate content.

Post Process also enables the use of some special variables: **body, headers,** and **status\_code**. These are only available during post process, and can be used to transmit any of the corresponding data back to a database table, or to an external API, to record the results of post process.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a4d151a8-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=4703ed261a2524c691a95b0029da278a" width="1140" height="684" data-path="images/a4d151a8-image.jpeg" />
</Frame>

## Debug Log

Debug Log allows you to output specific information in a new debug logging section of the Debugger. This is similar to how a console log statement in Javascript would behave. These steps will not run outside of Run & Debug.

<Frame>
  <iframe width="768" height="432" src="https://www.youtube.com/embed/rQiO-QkcdTM" title="Debugging your Function Stacks with Debug Log" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

This can be especially helpful for debugging data errors with loops or otherwise just giving you a quick view of a variable's contents during execution. You can insert whatever data you'd like into Debug Logs; they will accept any data type, and can also have filters applied.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/34437bb6-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=0d0203ef87f5b6a51e25f538a3c7b888" width="660" height="379" data-path="images/34437bb6-image.jpeg" />
</Frame>

In the below example, we're looping through results from a Query All Records statement, and outputting a specific value from each item to the new Debug Log.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/85818cf3-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=1609e53f26559983f84771071fcab0bc" width="1231" height="554" data-path="images/85818cf3-image.jpeg" />
</Frame>

And the result is available in the new Debug Log section of the debugger

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/5f7c83ac-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=3b3ac0ad5cab1a7f40ff4e1bcd1d8dba" width="578" height="858" data-path="images/5f7c83ac-image.jpeg" />
</Frame>

## Precondition

A precondition is a statement that says "this condition must evaluate as true, or we halt execution and return an error message."

<Steps>
  <Step title="Preconditions use the expression builder to define the conditions it checks. Click button below to define your conditions.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/5ff0dd45-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=0d7de2c37a02f6fcbd60653406b8e8eb" width="20" height="22" data-path="images/5ff0dd45-image.jpeg" />
    </Frame>

    ### Using the Expression Builder

    Each conditional has four different components.

    **Conditional Type**

    The conditional type determines how this condition is weighted in the final return. You can choose between **AND** and **OR. AND** conditionals require the present conditional and any others before it to be satisfied, such as "where the date is before today **AND** the user is an admin". **OR** conditionals do not require any other conditionals to be satisfied, such as "if the user is an admin **OR** if the user is a manager".

    **Left Value**

    This is the first value you're using in the conditional. In a database query, this is usually going to be a column that you want to check against.

    **Operators**

    <Info>
      Please note that operators may differ based on where you are building the expression. Database queries will have different operators available than regular conditional statements. Learn More
    </Info>

    * **Equals (==)** - an exact match

    * **Not Equals (!=)** - does not equal

    * **Equals with type matching (===)** - an exact value match and an exact type match

      * Ex. Variable **var\_1** has a value of 123, with a type of text. You set up a conditional statement to check if **var\_1 === 123**, but your value in the conditional statement is of type integer. This would return false, because the types do not match.

    * **Not equals with type matching (!==)** - does not equal value or type, similar to ===

    * **Greater than (>)** - the value on the left is greater than the value on the right

    * **Greater than or equals (≥)** - the value on the left is greater than or equals to the value on the right.

    * **Less than (\<)** - the value on the left is less than the value on the right.

    * **Less than or equals (≤)** - the value on the left is less than or equals to the value on the right.

    * **LIKE** - Used for comparing text. Like is case-insensitive and compares if a text string is like another text string. It can be thought of as equals for text but upper case and lower case does not matter.

    * **NOT LIKE** - Used for comparing text. Not Like is case-insensitive and compares if a text string is not like another. It is like not equals for text but upper case and lower case does not matter.

    * **INCLUDES** - Used for comparing text. Includes is a flexible operator and is case-insensitive. It is able to determine if there is a partial match in a text string.

    * **DOES NOT INCLUDE** - Used for comparing text. Does not include determines if a text string is not included in another text string.

    * **IN** - If a single value is found in an array (list). Start with the single value on the left side and the right side should contain the array.

    * **NOT IN** - If a single value is not found in an array (list). The single value should be on the left side and the array on the right side.

    * **REGEX MATCHES** - [Regular Expression](https://regex101.com/) used for finding patterns in text.

    * **REGEX DOES NOT MATCH** - [Regular Expression](https://regex101.com/) used for finding a pattern that does not match in text.

    * **OVERLAPS** - Used for comparing two arrays. Overlaps determines if any values in one array are present in the second array.

    * **DOES NOT OVERLAP** - Used for comparing two arrays. Does not overlaps determines if no values in the first array are present in the second array.

    * **CONTAINS** - Contains is an advanced filter used for JSON and arrays. It looks for an exact schema match.

    * **DOES NOT CONTAIN** - Does not contain is the opposite of contains. It determines if there is not an exact schema match.

    #### Right Value

    The right value is whatever you are checking against the left value. This could be a hardcoded value, a variable, or even a database field from the same record.
  </Step>

  <Step title="Define what happens if the conditions do not evaluate as true.">
    You can provide a custom error message, choose an error type, and supply a payload to return, such as the values being checked in your conditions.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/afa8ba59-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=9f37856052fec4bc3e46f56e1c88ebb1" width="584" height="478" data-path="images/afa8ba59-image.jpeg" />
    </Frame>
  </Step>
</Steps>

## Stop & Debug

Halts execution and returns a value. Useful to ensure that specific pieces of your function stack are running as expected while building.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/37eb490a-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=49ced4871bf957d06ea6a418db3f9549" width="587" height="184" data-path="images/37eb490a-image.jpeg" />
</Frame>

## Group

Groups functions together. This is an organizational tool for you as you build your function stacks and does not impact any part of the actual execution.

## Sleep

Waits for a defined number of seconds before proceeding to the next step.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/3b42e96e-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=0b96a29e57898f7d2ac77b6d4df6dad0" width="591" height="190" data-path="images/3b42e96e-image.jpeg" />
</Frame>

## CSV Stream

CSV Stream is a powerful function allowing you to 'stream' chunks of a CSV file in sequence to your function stack, allowing for processing of large CSV files.

<Frame>
  <iframe width="768" height="432" src="https://www.youtube.com/embed/SNE0mQDGCxo" title="CSV Stream | Process Large CSVs in your Function Stack" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

A successful CSV stream function stack includes three essential parts.

* a **file resource** to ingest the CSV file This can come from either a File Resource input, or a file delivered by an external API, with a Create File Resource step applied
* a **CSV stream** function to stream the CSV data This function initiates the streaming of CSV data, and provides an output variable. This output variable is meant for use with a [For Each](/working-with-data/functions/data-manipulation/loops/for-each-loop) loop
* a **For Each** loop to run through the individual CSV rows The loop is responsible for performing any functions you'd like on your CSV, such as adding each row to one of your database tables.

In the below example, we've added these three key components, and can now process the incoming CSV data.

CSV Stream is a much simpler alternative to the previously established method of array functions and object manipulation to process incoming CSV data.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/377d4789-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=b49ad5bbe04e8ed004ff84939ff82e20" width="1152" height="888" data-path="images/377d4789-image.jpeg" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/0c2635e7-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=dcfca8013104dfc3a3bc02cb27ab2c11" width="740" height="1068" data-path="images/0c2635e7-image.jpeg" />
</Frame>

## JSONL Stream

JSONL Stream is a powerful function allowing you to 'stream' chunks of JSON in sequence to your function stack, allowing for processing of large data sets, similar to the CSV Stream function above.

## HTTP Header

Set a custom HTTP header. This function is useful if you need your responses to deliver specific, custom headers. You can also use this to specify custom API response codes outside of the ones our Precondition function offers.

The **duplicates** parameter lets you decide to either replace headers that already exist with your new header, or allow for duplicate headers to exist.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e6f56390-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=dc15b7990b0134c7b046f08f5d132550" width="742" height="395" data-path="images/e6f56390-image.jpeg" />
</Frame>

<Accordion title="Examples of Custom HTTP Headers">
  <Info>
    Please note that each individual header should use its own Set Header function.
  </Info>

  **Rate Limiting**

  These will not enforce rate limits themselves, but it's good information to have in your headers if you are rate limiting your APIs.

  ```
  X-Rate-Limit-Limit: 100
  X-Rate-Limit-Remaining: 95
  X-Rate-Limit-Reset: 1615560000
  ```

  #### Serving Content Downloads

  If you want your API to directly serve file downloads, use this header:

  ```
  Content-Disposition: attachment; filename="report.pdf"
  ```

  You may also need:

  ```
  Content-Type: text/html
  ```

  #### Custom HTTP Status

  Sometimes, you might need to send an HTTP status that Xano doesn't natively offer using preconditions.

  ```
  HTTP/1.1 201 Created
  Content-Type: application/json
  ```
</Accordion>

## Get All Variables

Returns all of the variables present up to that point in the function stack.

## Get All Input

Returns all of the inputs sent to the API in a single object.

## Get All Raw Input

Returns all data sent to the API, even if they are not defined inputs. You'd use this function when building a \*\*Webhook, \*\*or you otherwise aren't sure what data will be sent to this endpoint.

<Info>
  Exclude Middleware Modification should be set to `false` if you intend on using the raw data in your function stack \*\*before \*\*it's modified by Middleware.
</Info>

## Get Environment Variables

Returns all of your [environment variables](/the-function-stack/environment-variables) in a single object.

## Calculate Distance

Calculate the distance between two longitude/Latitude points

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/e0fc633d-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=bbbff4768c0b168c53e1113668837ff1" width="1194" height="1418" data-path="images/e0fc633d-image.jpeg" />
</Frame>

## IP Address Lookup

Takes in an IP address and returns geographical information based on that IP. This product includes GeoLite2 data created by MaxMind, available from [https://www.maxmind.com](https://www.maxmind.com/).

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c6ff07d9-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=e018b7993b4cf36a19ddd5d4f93f5aa1" width="1077" height="538" data-path="images/c6ff07d9-image.jpeg" />
</Frame>

## Set Data Source

This function allows you to specify which data source that database operations following it target. Remember that the order of operations in a function stack matters, so any database operations that come before your Set Data Source statement will use whatever is used normally.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/594182f3-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=0b6907fc24a970018d5d3204a43828b3" width="1312" height="580" data-path="images/594182f3-image.jpeg" />
</Frame>

## Async Function Await

[Learn about Async functions here](/the-function-stack/functions/custom-functions#async-function-await)


Built with [Mintlify](https://mintlify.com).