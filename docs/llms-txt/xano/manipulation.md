# Source: https://docs.xano.com/xanoscript/filter-reference/manipulation.md

# Source: https://docs.xano.com/the-function-stack/filters/manipulation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manipulation

<Tip>
  **NOTE**

  When a filter below refers to the **parent value**, we're talking about the value box that lives immediately above the filter.

  <Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/465e2547-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=b224df8de804bea26c1c4f7994db2d87" width="633" height="199" data-path="images/465e2547-image.jpeg" />
  </Frame>
</Tip>

## fill

Create an array of a certain size with a default value.

| Parameter    | Purpose                          | Example         |
| ------------ | -------------------------------- | --------------- |
| parent value | The default value to fill        | "default value" |
| start        | The starting index of the array  | 0               |
| length       | The number of items in the array | 10              |

### Examples

<Tabs>
  <Tab title="Example">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/d2ede07b-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=080942dd34e3a4e868be5a5ba5fc62ed" width="647" height="478" data-path="images/d2ede07b-image.jpeg" />
    </Frame>
  </Tab>

  <Tab title="Result">
    ```json  theme={null}
    [
        "Default Value",
        "Default Value",
        "Default Value",
        "Default Value",
        "Default Value",
        "Default Value",
        "Default Value",
        "Default Value",
        "Default Value",
        "Default Value"
    ]
    ```
  </Tab>
</Tabs>

***

## fill\_keys

Creates an object of a certain size with a default value and a list of keys.

| Parameter    | Purpose                   | Example                     |
| ------------ | ------------------------- | --------------------------- |
| parent value | The default value to fill | "default value"             |
| keys         | The array of keys to use  | `[	"key1",	"key2",	"key3"]` |

### Examples

<Tabs>
  <Tab title="Example">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/353a9339-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=052b0ea292abf06387ad59b57ebda5c2" width="646" height="464" data-path="images/353a9339-image.jpeg" />
    </Frame>
  </Tab>

  <Tab title="Output">
    ```json  theme={null}
    {
      "key1": "Default Value",
      "key2": "Default Value",
      "key3": "Default Value"
    }
    ```
  </Tab>
</Tabs>

***

## first\_notempty

Applies the first value that is not **empty** (0, null, "", empty string)

Useful if you need to determine a value to apply based on what is provided, such as editing a database record and being uncertain if an input will be provided to replace a value.

| Parameter    | Purpose                                       | Example                             |
| ------------ | --------------------------------------------- | ----------------------------------- |
| parent value | The value to check if empty                   | Can contain any value, or no value. |
| value        | The value to use if the parent value is empty | "default"                           |

### Examples

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/374ee0e8-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=9ce5b79108c7bcccfefe465c35dfd2f8" width="1305" height="777" data-path="images/374ee0e8-image.jpeg" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b7e4321f-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=7c461464b78b323374d2bd29fb489f4a" width="1305" height="827" data-path="images/b7e4321f-image.jpeg" />
</Frame>

***

## first\_notnull

Applies the first value that is not `null`

Useful if you need to determine a value to apply based on what is provided, such as editing a database record and being uncertain if an input will be provided to replace a value.

<Info>
  **Hint**

  Remember, `null` is its own value entirely. It is not the same as "null", an empty string, or any other similar empty state.
</Info>

| Parameter    | Purpose                                        | Example          |
| ------------ | ---------------------------------------------- | ---------------- |
| parent value | The value to check if `null`                   | Can be any value |
| value        | The value to use if the parent value is `null` | "default"        |

### Examples

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/5e2bba62-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=00fe753b796323be12d4e7ee39b85343" width="1301" height="912" data-path="images/5e2bba62-image.jpeg" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/98f5281c-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=6feb530908dbc34fc0ed97333bf0ffe8" width="1310" height="912" data-path="images/98f5281c-image.jpeg" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/08fcda59-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=9b9aa34a8670c386dfa998c0664bf361" width="1306" height="771" data-path="images/08fcda59-image.jpeg" />
</Frame>

***

## get

Gets a value at the specified path inside of an array or object.

For arrays, the path can be an index, such as `0`, `1,` or `2`, which will get the specific item at that index in the array.

For arrays of objects, you can specify the index + a path, such as `2.name`

For single objects, you can just specify the path, such as `name`.

This filter is useful if you aren't sure if the value you need will exist, and need to provide a default value in place of it.

<Tip>
  **Hint**

  Are you getting errors in your function stacks because certain values don't exist all the time? The **GET** filter can be a great fix for this.
</Tip>

| Parameter     | Purpose                                                     | Example                                                                                                                                                                                                                                         |
| ------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| parent value  | The object or array to search for the value                 | This can be an object, array, a variable, or the result of one of the Get All Input functions [\[1\]](/the-function-stack/functions/utility-functions#get-all-input) [\[2\]](/the-function-stack/functions/utility-functions#get-all-raw-input) |
| path          | The path to look for inside of the parent value             | For getting a specific array item: `0` For getting a specific path inside of an object: `pathName` For getting a specific path inside of an array of objects: `0.pathName`                                                                      |
| default value | The value to provide in place of the value that isn't found | This value can be whatever you'd like.                                                                                                                                                                                                          |

### Examples

<Frame caption="An age is provided in the input, so it is provided by the GET filter.">
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/4e030afe-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=d558bcc9c6c9d81777a9d06a02c2a2c7" width="1307" height="777" data-path="images/4e030afe-image.jpeg" />
</Frame>

<Frame caption="No age is provided in the input, so the default value is used instead.">
  <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/ae3dc485-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=1724b9c6d1fe5e0175ee537c206883d0" width="1313" height="768" data-path="images/ae3dc485-image.jpeg" />
</Frame>

***

## has

Checks if a value is present (similar to get), but only returns a true or false.

| Parameter    | Purpose                                         | Example                                                                                                                                                                                                                                         |
| ------------ | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| parent value | The object or array to search for the value     | This can be an object, array, a variable, or the result of one of the Get All Input functions [\[1\]](/the-function-stack/functions/utility-functions#get-all-input) [\[2\]](/the-function-stack/functions/utility-functions#get-all-raw-input) |
| path         | The path to look for inside of the parent value | For getting a specific array item: `0`<br /><br />For getting a specific path inside of an object: `pathName`<br /><br />For getting a specific path inside of an array of objects: `0.pathName`                                                |

### Examples

<Frame caption="An age is provided, so the filter returns true">
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/3228a04d-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=aac7d4f3ce11367a6f252eb616a3b419" width="1306" height="777" data-path="images/3228a04d-image.jpeg" />
</Frame>

<Frame caption="An age is not provided, so the filter returns false">
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/13a795cf-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=8c6756f4f1b3198936d5d82c90215128" width="1307" height="776" data-path="images/13a795cf-image.jpeg" />
</Frame>

***

## set

Replaces or inserts new data at a specified path.

| Parameter    | Purpose                                           |
| ------------ | ------------------------------------------------- |
| parent value | The object or array to target with the set filter |
| path         | The path at which to insert the supplied value    |
| value        | The supplied value to use                         |

### Examples

<Frame caption="Replace a value with another">
  <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/f9de76c4-image.jpeg?fit=max&auto=format&n=WBQXG-4Ngk82eYAW&q=85&s=f98a449b7f8499ac449a387eefc36bb4" width="1304" height="855" data-path="images/f9de76c4-image.jpeg" />
</Frame>

<Frame caption="Set a new key inside of an object">
  <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/3e28ae11-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=6f965b01505fbfdb4cb5f3fe65662f36" width="1310" height="554" data-path="images/3e28ae11-image.jpeg" />
</Frame>

***

## set\_conditional

Use set\_conditional to set a new value in an object based on whether a condition evaluates as true.

<Frame>
  <iframe src="https://demo.arcade.software/CxgMoWBBckff0sO4P3ik?embed" title="https://demo.arcade.software/CxgMoWBBckff0sO4P3ik?embed" allowFullScreen allow="clipboard-write" class="contentkit-webframe" width="1000" height="500" />
</Frame>

| Parameter    | Purpose                                                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------------------------------------ |
| parent value | The data to insert the result, such as an object                                                                         |
| path         | The path to insert the result                                                                                            |
| value        | The value to insert at the specified path                                                                                |
| conditional  | The condition to check. This can either come from an earlier function,or another filter that returns a `true` or `false` |

### Examples

<Frame caption="The age provided is greater than 20, so we return the value set in our set_conditional filter">
  <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/cfe9fbff-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=0a8b5c3b772db80e2cbb3c6c1e62f2df" width="1311" height="882" data-path="images/cfe9fbff-image.jpeg" />
</Frame>

***

## set\_ifnotempty

## set\_ifnotnull

Sets a new value in an object if the value provided is not empty. An empty value can be 0, `null`, or an empty string.

set\_ifnotnull works the same, but only checks for `null`

| Parameter    | Purpose                                                      | Example                                 |
| ------------ | ------------------------------------------------------------ | --------------------------------------- |
| parent value | Where to set the value                                       | This will usually be an existing object |
| path         | The path to set the value if the checked value exists        | "name"<br />"age"<br />"location"       |
| value        | The value to set if the checked value is not empty (or null) | Any value                               |

### Examples

<Steps>
  <Step title="First, we're getting an existing record from the database.">
    In this function stack, we're simulating a user submitting changes to their user profile.
  </Step>

  <Step title="Then, we use an Update Variable with set_ifnotempty (or set_ifnotnull) to determine whether or not the returned record needs to be updated." />

  <Step title="Finally, we edit the record using the result of step 2 for all of our values." />
</Steps>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/bd1a1448-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=497a2296b0dcb7ad7bac4acd3bb68c17" width="2198" height="1173" data-path="images/bd1a1448-image.jpeg" />
</Frame>

***

## transform

The `transform` filter is universal way to transform data. It works with arrays, objects, and scalar values. It uses the [expression data type](/the-function-stack/data-types/expression) to specify the transformation.

## Hint

This filter is similar to the [map filter](/the-function-stack/filters/transform#map), except it can bind to all data - not just an array.

You can use the context variable \$\$ to target the parent value.

| Parameter    | Purpose                                  | Example                      |
| ------------ | ---------------------------------------- | ---------------------------- |
| parent value | The value to apply the transformation to | Can be any value or variable |
| expression   | The expression to run                    | Any expression               |

Read more about expressions and Xano Transform below.

<Card href="/the-function-stack/data-types/expression">
  Expression
</Card>

<Card icon="arrow-down-up-across-line" href="/xano-transform/using-xano-transform">
  Xano Transform
</Card>

### Examples

```powershell  theme={null}
[1,2,3]|transform:($$|count)                              // returns 3
[1,2,3]|transform:($$|count)+($$|sum)                     // returns 9
{first:Alpha,last:Beta}|transform:$$.first~" "~$$.last    // returns Alpha Beta
```

***

## unset

Removes a key from an object

| Parameter    | Purpose                                       |
| ------------ | --------------------------------------------- |
| parent value | The object to target                          |
| path         | The name of the key to remove from the object |

### Examples

<Frame caption="The user record normally returns a &#x22;name&#x22;, but using unset has removed it.">
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e58f521c-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=fe5614920557b9b602eb9a94dc50d0ff" width="1305" height="589" data-path="images/e58f521c-image.jpeg" />
</Frame>

***


Built with [Mintlify](https://mintlify.com).