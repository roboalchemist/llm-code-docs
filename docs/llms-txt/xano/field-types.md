# Source: https://docs.xano.com/the-database/database-basics/field-types.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Field Types

### 📄 Text

A text field can contain anything that you'd want to provide, such as names, addresses, location names, and descriptions.

```
Hello
John Smith
Chicago
```

### 🔢 Integer

An integer is just a whole number, such as 3, 42, 100, etc...

```
1
100
1000
```

### ㊙️ UUID

UUID stands for **universally unique identifier**, and is a random string of letters and numbers, typically used to enforce uniqueness amongst other records in the table.

```
105c8b80-fd24-4cf3-bbed-a43e8134c8b0
984x0t12-rt12-5ey6-poqw-b12y1923e6l0
```

### 🍱 Object

Imagine a folder that can hold different types of information together - like how a contact card holds someone's name, phone, and address. Or, recording certain data about vehicles, such as year, make, and model.

```json  theme={null}
{
  "make": "Toyota",
  "model": "Corolla",
  "year": 2020
    }
```

### ❓ Table Reference

This field type is like a quick link to a record in another table (or even the same table, if your use case requires it). Table references are useful when separating data between tables and maintaining relationships between them.

For example, you might have a table of users, and a table of user roles. In your users table, you could add a table reference to your roles table to link each user to a specific role. This is advantageous because it is easier to maintain consistency and make changes to role types.

### 🤖 Vector

Vectors are used for AI/LLM applications to store data that helps the model find the most relevant information based on the query being made. Think of it like a DNA sequence - it's just a string of values that might not mean much to us when we look at them directly, but they encode important information that the AI system knows how to interpret.

```
[-0.235, 0.458, -0.891, 0.023, 0.444, -0.657, ...]
```

* It's a fixed-length array of numbers (often hundreds or thousands of elements)
* The numbers are usually floating-point values (often between -1 and 1)
* Each vector has the same dimensionality (length) within a given field
* The individual numbers themselves don't have inherent meaning - they're abstract representations that are provided by an AI model and stored for later use.

### 🛑 Enum

An enum is like a text field, but only allows for specific values. It's like a multiple choice question instead of a freeform input. For example, an enum field would be appropriate to use if you wanted to store a color from a specific list.

```
Red
Blue
Green
Orange
```

### 🕕 Timestamp

Xano stores timestamps in <Tooltip tip="The UNIX Epoch format is &#x22;the number of seconds since Jan 1, 1970 00:00&#x22;. Xano takes this a step further and stores this value as milliseconds, giving you further flexibility to store time values.">UNIX Epoch format</Tooltip>. They are stored in the database as an integer, but appear to you as human readable timestamps in your local timezone. While it may seem unintuitive, this format is ideal for ensuring that you can always store and return accurate time-based data in a user's local time zone, and have the most flexibility when down-to-the-millisecond accuracy is required.

```
1733762528000 // This Epoch timestamp in MS represents Mon, 09 Dec 2024 16:42:08 GMT
```

### 📅 Date

This is just a calendar date. It offers less flexibility than the recommended Timestamp field, but can be useful when exact times are not important, such as birthdays or anniversaries.

### ✅ Boolean

A boolean is just a true or false value. It's a bit different than storing true or false in a text string and the recommended option if you need to store true and false values.

* Booleans take up less storage space, as they are one-bit values (0/1) instead of the full text.
* They enforce data validation and ensure that only true / false values are stored in the database instead of different variations with potential errors (such as TRUE, true, ture, Y, 1)

### 🔢 Decimal

This is similar to the integer field, but allows for decimal points. Use this field type for things like money (\$12.34) or measurments (3.14 inches).

### 📨 Email

Xano's Email field is really just a text field, but enforces proper formatting to ensure that emails are entered properly into the database.

### 🔑 Password

Xano's Password field is really just a text field, but includes extra security around storing and showing the value to you.

* Xano's passwords are stored encrypted. Password fields will never store passwords in plain text.
* They are not viewable from the database view.
* If you return the password field in a database query, only the encrypted version is shown. It is not possible to retrieve raw user passwords from a password field.

### 💻 JSON

Think of this as a flexible container that can hold different types of information in an organized way - like a recipe that lists ingredients and steps.

```json  theme={null}
{
  "name": "Classic Chocolate Chip Cookies",
  "prepTime": 15,
  "ingredients": [
    {
      "item": "flour",
      "amount": 2.25,
      "unit": "cups"
    },
    {
      "item": "chocolate chips",
      "amount": 2,
      "unit": "cups"
    }
  ],
  "steps": [
    "Cream butter and sugars",
    "Add eggs and vanilla",
    "Mix in dry ingredients",
    "Stir in chocolate chips"
  ],
  "isGlutenFree": false,
  "servings": 24
}
```

### 🖼️ Storage

Xano includes support for file storage, and utilizes your database to record files you have stored in Xano. The database tables themselves do not include the actual files; only metadata for the files themselves, such as name, size, and location.

```json  theme={null}
{
  "promoImage": {
    "access": "public",
    "path": "/vault/ABC123xyz/D3F4G5hij/K7L8M9.../sample-image.png",
    "name": "sample-image.png",
    "type": "image",
    "size": 123456,
    "mime": "image/png",
    "meta": {
      "width": 1080,
      "height": 400
    },
    "url": "https://example-domain.io/vault/ABC123xyz/sample-image.png"
  }
}
```

### 🗺️ Geography

Geography fields in Xano can contain different types of information, all based around latitude and longitude.

* Points on a map
* A route of connected points
* A polygon of points, such as a specific geographical area

#### Geo Point

```json  theme={null}
{
    "type": "point",
    "data": {
        "lng": 128.233455,
        "lat": 39.391205
    }
}
```

#### Path

```json  theme={null}
{
    "type": "path",
    "data": [
            {
                "lng": -115.697829,
                "lat": 38.512029
            },
            {
                "lng": 15.719451,
                "lat": 32.816569
            }
        ]
}
```

#### Polygon

```json  theme={null}
{
 "type": "poly",
 "data": [
   {
     "lng": -169.592325,
     "lat": 79.284391
   },
   {
     "lng": -70.737922,
     "lat": 77.866587
   },
   {
     "lng": 56.995958,
     "lat": 12.476723
   },
   {
     "lng": -156.669723,
     "lat": -29.580055
   },
   {
     "lng": -169.592325,
     "lat": 79.284391
   }
 ]
}
```


Built with [Mintlify](https://mintlify.com).