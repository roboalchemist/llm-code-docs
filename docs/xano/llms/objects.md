# Source: https://docs.xano.com/xanoscript/function-reference/data-manipulation/objects.md

# Source: https://docs.xano.com/the-function-stack/functions/data-manipulation/objects.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Objects

These functions are used when you need to get the properties of an objection in the function stack.

#### Examples

For each of these examples, we will create a variable called `object` with the value

```json  theme={null}
{
   "a":"3",
   "b":"2",
   "c":"1"
}
```

## **Get Keys**

Get the property names of an object as an array.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c6932090-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=ff4b7c4954b0295fa181f5dd29cda5f8" width="1072" height="718" data-path="images/c6932090-image.jpeg" />
</Frame>

In the above example, the object is changed to an array

```javascript  theme={null}
{
   "a",
   "b",
   "c"
}
```

## **Get Values**

Get the property values of an object as an array.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/1d40cca4-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=bec70686bdece7889c40c5d6910f7047" width="1060" height="714" data-path="images/1d40cca4-image.jpeg" />
</Frame>

In the above example, the object is changed to an array

```javascript  theme={null}
{
   "3",
   "2",
   "1"
}
```

## **Get Entries**

Get the property entries of an object as an array

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/caf7d453-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=a0fbb50489e25c9d61e8a60369efcd94" width="1062" height="740" data-path="images/caf7d453-image.jpeg" />
</Frame>

In the above example, the object is changed to an array

```json  theme={null}
[
   {
      "key":"a",
      "value":"3"
   },
   {
      "key":"b",
      "value":"2"
   },
   {
      "key":"c",
      "value":"1"
   }
]
```


Built with [Mintlify](https://mintlify.com).