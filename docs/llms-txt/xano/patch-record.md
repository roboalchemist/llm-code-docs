# Source: https://docs.xano.com/the-function-stack/functions/database-requests/patch-record.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Patch Record

**Patch** is most appropriate when you aren't sure what fields will be updated when editing the record.

#### What's the difference between Edit Record and Patch Record?

* **Edit Record** is best used when you have a static expectation for which fields need to be updated when the function is executed. For example, maybe you have an endpoint specifically to allow a user to update their password. Edit Record would make sense here, because you would not be changing any other information.
* **Patch Record** is best used when you have an endpoint that can update multiple fields, but may not always need to do so. Something like a user submitting a collection of edits to their user profile would fall under this example.

**Patch Record** is a little different than **Edit Record** in the way values are provided to it. While Edit Record gives you the option to address each field individually inside of the function, **Patch** only expects a field name and field value (so it knows which record to patch) and a JSON object representing all of the values to be updated.

In the following example, let's say that our record currently looks like this:

```json  theme={null}
{
    "id": 1,
    "name": "Chris",
    "email": "chris@email.com",
    "city": "Chicago"
    }
```

We want to build an endpoint that allows our users to update one or more of these fields in one swing. This means that we need to construct a JSON object that contains **only** the values to be updated and provide that to our Patch Record statement.

If Chris wants to update only his city, the object we provide to Patch would look like this:

```json  theme={null}
{
    "city": "Seattle"
    }
```

And our patch statement might look like this:

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/621ddc14-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=9b219129ef46975056a0dac7b325a934" width="591" height="881" data-path="images/621ddc14-image.jpeg" />
</Frame>

However, using the **set filter** in the scenario where multiple fields **might** be provided is not recommended. This is because if Patch is provided empty or null values, it will write those to the record, and the goal is to only write the fields we want.

<Warning>
  **Please be aware that Patch will write every field provided in the JSON object to the record, even blank and null values. The JSON object used for Patch should only provide the fields you want to update, and nothing more. Providing empty or null values unintentionally can result in data loss.**
</Warning>

<Warning>
  Some frontends will always send empty or null values regardless of what data points are actually defined.

  To make Patch work as it is normally expected, you'll want to leverage filters like:

  * `filter_null` to remove null values

  * `filter_empty_text` to remove empty text strings
</Warning>

Using a **Get All Raw Input** function along with **Patch Record** can be a perfect combination.

* **Get All Raw Input** provides a JSON object of all of the input fields passed to the API.

* We can then provide the output of this function to **Patch Record**, giving us an easy and fast method of building a flexible endpoint for editing records.

Our final endpoint might look something like this:

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/3b530fff-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=0708a9f8f931d6740bbb71589e95bb7e" width="2304" height="740" data-path="images/3b530fff-image.jpeg" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c7ac7be9-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=bc84fab246caedba3854092a59e445ad" width="2304" height="785" data-path="images/c7ac7be9-image.jpeg" />
</Frame>


Built with [Mintlify](https://mintlify.com).