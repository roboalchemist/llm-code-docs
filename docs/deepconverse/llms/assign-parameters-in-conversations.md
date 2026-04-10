# Source: https://docs.deepconverse.com/product-docs/conversational-flow-builder/assign-parameters-in-conversations.md

# Assign Parameters in Conversations

The chatbot conversation can remember certain parameters that are set in the conversation. These can be set at various points to help make decisions at future points in the conversation. A classic example is setting parameter based on users selection.

For ex. if a user is asked a question "Please select the reason for contacting us today" and presented with options "Sales" and "Support", we can store their selection in a parameter for use in the rest of the conversation.

### How to set a parameter?

* Open the conversation flow and navigate to the node where you would like to set a parameter.&#x20;
* Click on the node and open the right panel
* In the right panel scroll down to **Additional Settings** and click **Edit** next to **Assign Parameters**
* In the popup you will be able to add parameters and save them at this node.
* If a captured or declared parameter holds sensitive data such as an API Key, email etc. you should declare it under **Sensitive Parameters** to ensure it is scrubbed from the transcript.
* Optionally the parameter can be declared as Encrypted&#x20;

***Note**: Parameters are assigned after the node has been evaluated and are available for use from the subsequent steps*

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FFAt9CrcRN05bm7Fywyqc%2FScreenshot%202023-12-22%20at%2011.29.39%20AM.png?alt=media&#x26;token=e84afdf2-da94-44e4-89fb-aead2ae09f1f" alt=""><figcaption></figcaption></figure>

### Types of Parameter Values

#### Fixed Values

Fixed parameter values can be used to set parameters for routing the conversation or using some conversation state available from the platform.

| **Parameter**              | **Description**                                                                                                                                  |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| $sys\_transcript           | Allows you to store the transcript of the conversation till this point into the parameter                                                        |
| $sys\_outgoing\_transition | Allows you to capture the user selection in case of a Question node into a parameter                                                             |
| $a.b.c                     | Allows copying the nested parameter value from the conversation context. This is useful for api calls where the response might be a nested JSON. |
| \<Any Text Value>          | Saves the text value in the parameter and is available in the conversation till unset                                                            |

&#x20;

#### Expression

Expressions allow to transform data and store the result in a parameter. The expressions are useful if you are looking to do operations such as math operations, string manipulation and certain built in functions that are provided through the platform.

**Operators**

Here is a list of operators that you use with the conversation parameters

| `+`  | <p>add two things. <code>x + y</code> <code>1 + 1</code> -> <code>2</code><br>string concatenation <code>firstName</code> + ' ' + <code>lastName</code> -> <code>dhruv arya</code></p> |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-`  | subtract two things `x - y` `100 - 1` -> `99`                                                                                                                                          |
| `/`  | divide one thing by another `x / y` `100/10` -> `10`                                                                                                                                   |
| `*`  | multiple one thing by another `x * y` `10 * 10` -> `100`                                                                                                                               |
| `**` | 'to the power of' `x**y` `2 ** 10` -> `1024`                                                                                                                                           |
| `%`  | modulus. (remainder) `x % y` `15 % 4` -> `3`                                                                                                                                           |
| `==` | equals `x == y` `15 == 4` -> `False`                                                                                                                                                   |
| `<`  | Less than. `x < y` `1 < 4` -> `True`                                                                                                                                                   |
| `>`  | Greater than. `x > y` `1 > 4` -> `False`                                                                                                                                               |
| `<=` | Less than or Equal to. `x <= y` `1 < 4` -> `True`                                                                                                                                      |
| `>=` | Greater or Equal to `x >= 21` `1 >= 4` -> `False`                                                                                                                                      |
| `in` | is something contained within something else. `"spam" in "my breakfast"` -> `False`                                                                                                    |

\
**Utility Functions**

In addition to the operators you can also use certain prebuilt utility functions.

| DOUBLE                 | Convert parameter to a floating point type                                                                                                                 |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MD5                    | Generate the md5 hash of the parameter                                                                                                                     |
| INT                    | Convert parameter to a integer type                                                                                                                        |
| STR                    | Convert parameter to string type                                                                                                                           |
| SORT\_LIST             | Sort the list of values in ascending order                                                                                                                 |
| REVERSE\_LIST          | Reverse the list of values                                                                                                                                 |
| APPEND\_LIST           | Sort the list of values                                                                                                                                    |
| SUBSTITUTE             | Substitute part of a string ex. *SUBSTITUTE(param1, '-', '\_')*                                                                                            |
| FORMAT\_DATE           | <p>FORMAT\_DATE(param1, \<date\_format>)<br><br>For referencing date format please visit <a href="https://www.strfti.me/"><https://www.strfti.me/></a></p> |
| REGEX\_EXTRACT         | REGEX\_EXTRACT(param1, \<pattern>)                                                                                                                         |
| SPLIT\_PART            | <p>SPLIT\_PART(param1, ' ', 1)<br><br>example:<br>SPLIT\_PART('Dhruv Arya', ' ', 1)<br>will be equal to "Arya"</p>                                         |
| CURRENT\_DATE\_BETWEEN | CURRENT\_DATE\_BETWEEN(start\_date\_or\_timestamp, end\_date\_or\_timestamp)                                                                               |

&#x20;

### How to unset a parameter value?&#x20;

You can unset a parameter by choosing the **Unset** option and giving the parameter name or path you would like to unset.

You can use path notation as well ex. `a.b.c`

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FI0XLEL42RXWSSrqsrTyX%2Fimage.png?alt=media&#x26;token=302797e9-7b35-4d70-bf02-b7c3be4c57f0" alt=""><figcaption></figcaption></figure>

### How to use parameters in messages?

Parameters can be used in our templating language by referring to them as follows:

```
Hello {{ firstName }}
```

### Action Parameters

Action parameters are special purpose parameters that allow you to define actions to take during the flow execution. These are fixed value parameters with value serving as a property of the parameter.

You can set this like the image below:

![mceclip2.png](https://help.deepconverse.com/hc/article_attachments/4410304233876/mceclip2.png)

| **Parameter**     | **Value Type**                                                     | **Description**                            |
| ----------------- | ------------------------------------------------------------------ | ------------------------------------------ |
| \_\_action\_delay | Number of Seconds to delay, maximum delay of 15 seconds is allowed | Allows you to delay going to the next node |

&#x20;
