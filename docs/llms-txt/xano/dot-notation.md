# Source: https://docs.xano.com/building/logic/working-with-data/dot-notation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dot Notation

> Dot notation is used to target specific pieces of data inside of objects and arrays

## What is dot notation?

Dot notation is a way to access specific properties of an object or array using a period (.) to separate the property name from the object or array.

## Using dot notation with objects

Let's say we have the following object:

```json  theme={null}
{
    "name": "John",
    "age": 30,
    "created_at": 1736364473744
}
```

If we want to use an Update Variable function to update that `created_at` property to be human readable, we would use dot notation to target that property directly, like this:

<Frame><img src="https://mintcdn.com/xano-997cb9ee/wrzs-BFWgaRt_XRt/images/dot-notation-20251013-093904.png?fit=max&auto=format&n=wrzs-BFWgaRt_XRt&q=85&s=770cbb59bf4f8297c2c723911f705d0c" alt="dot-notation-20251013-093904" width="543" height="527" data-path="images/dot-notation-20251013-093904.png" /></Frame>

This will target `created_at` inside of the object and update it to `Wed, 08 Jan 2025 19:27:53 +0000`.

You can also use dot notation to create new properties inside of an object. Our user object doesn't have a `location` property yet, so we can add it like this:

<Frame><img src="https://mintcdn.com/xano-997cb9ee/wrzs-BFWgaRt_XRt/images/dot-notation-20251013-094029.png?fit=max&auto=format&n=wrzs-BFWgaRt_XRt&q=85&s=7550bbc445f76e6cdf1df26e590ca93b" alt="dot-notation-20251013-094029" width="546" height="408" data-path="images/dot-notation-20251013-094029.png" /></Frame>

So, even though the email property doesn't exist, using dot notation to target it will create it for us.

## Using dot notation with arrays

Arrays are a little different than objects in that they are indexed, starting at 0. So, the first item in the array is at index 0, the second item is at index 1, and so on. The `index` just refers to the position of the item in the array.

Let's say we have the following array:

```json  theme={null}
[
    "apple", // index 0
    "banana", // index 1
    "cherry" // index 2
]
```

If we want to use an Update Variable function to update the second item in the array to be "orange", we would use dot notation to target that item directly, like this:

<Frame><img src="https://mintcdn.com/xano-997cb9ee/wrzs-BFWgaRt_XRt/images/dot-notation-20251013-094238.png?fit=max&auto=format&n=wrzs-BFWgaRt_XRt&q=85&s=4e0413b8c95ba3cb4dc77367a16bed34" alt="dot-notation-20251013-094238" width="537" height="407" data-path="images/dot-notation-20251013-094238.png" /></Frame>

This will target the second item in the array and update it to `orange`.

## Using dot notation with complex nested data

You can use dot notation with any combination of nested arrays and objects.

Let's say we have the following array:

```json  theme={null}
[
    {
        "name": "apple",
        "details": {
            "color": "red",
            "price": 1.00
        }
    },
    {
        "name": "banana",
        "details": {
            "color": "yellow",
            "price": 0.50
        }
    }
]
```

If we want to use an Update Variable function to update the price of the second item in the array to be \$0.75, we would use dot notation to target that item directly, like this:

<Frame><img src="https://mintcdn.com/xano-997cb9ee/wrzs-BFWgaRt_XRt/images/dot-notation-20251013-094542.png?fit=max&auto=format&n=wrzs-BFWgaRt_XRt&q=85&s=f377b82b5524e563270007a14571b3bd" alt="dot-notation-20251013-094542" width="545" height="403" data-path="images/dot-notation-20251013-094542.png" /></Frame>

This will target the second item in the array and update the price to \$0.75.

<Tip>When you need to utilize dots inside of keys (for example, if an external API is returning a key with a dot in it), use double dots to 'escape' the dot and it will remain, instead of being interpreted as dot notation. For example, to access a key named `user.name`, you would use `user..name` in your dot notation. Without the double dots, it would try to access the `name` property of the `user` object.</Tip>

## Try it out

You can create a new API or custom function and paste the following XanoScript into the editor to see it in action. Feel free to experiment and modify the logic to get a feel for how it works.

```javascript lines icon="code" Dot notation example theme={null}
query dot_notation_example verb=GET {
  input {
  }

  stack {
    var $user {
      value = {}
        |set:"name":"John"
        |set:"age":30
        |set:"created_at":1736364473744
    }
  
    var.update $user.created_at {
      value = $user.created_at|format_timestamp:"r":"UTC"
    }
  
    var.update $user.email {
      value = "john@email.com"
    }
  
    var $fruits {
      value = []
        |push:"apple"
        |push:"banana"
        |push:"cherry"
    }
  
    var.update $fruits.1 {
      value = "orange"
    }
  
    var $fruits_complex {
      value = """
        [
          {
            "name": "apple",
            "details": {
              "color": "red",
              "price": 1
            }
          },
          {
            "name": "banana",
            "details": {
              "color": "yellow",
              "price": 0.5
            }
          }
        ]
        """|json_decode
    }
  
    var.update $fruits_complex.1.details.price {
      value = 0.75
    }
  }

  response {
    value = {
      user          : $user
      fruits        : $fruits
      fruits_complex: $fruits_complex
    }
  }

  history = {inherit: true}
}
```


Built with [Mintlify](https://mintlify.com).