# Source: https://docs.xano.com/xanoscript/key-concepts.md

# Source: https://docs.xano.com/before-you-begin/key-concepts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Key Concepts

> Get a quick primer on the key concepts and terminology that we use throughout the product and documentation to get you started quickly.

***

### 🖥️ Instance

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/nBW9XuzKBAE" title="What is an Instance" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

Your Xano instance is the heart of everything you do in Xano. An **instance** is a dedicated server that we manage for you and it contains all of your Xano data, including APIs, databases, user data, and more.

On all of our paid plans, each instance has its own dedicated resources, is always available, and completely isolated from other Xano users. This means that even if, in the rare occurrence that one user experiences an issue with their own Xano backend, it won't impact anybody else.

On our free plan, you are on a shared instance with other Xano users.

***

### 📂 Workspace

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/lCIjFBVJ8HM" title="What is a Workspace" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

In your Xano instance, you can have multiple **workspaces**. Think of a workspace as a separate container for each project you're building in Xano. Your workspaces are completely isolated from each other, but all share the same compute resources provided by your instance.

***

### 🧠 Backend

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/igzPKoqYpR0" title="What is a Backend?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

Think of the backend as the brains of a website or app. It's all the behind-the-scenes action that users don't see. When you're browsing an online store, the backend is figuring out what products to show you, keeping track of your shopping cart, and making sure your payment goes through. It's like the engine room of a ship - not glamorous, but absolutely crucial.

***

### 📱 Frontend

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/ddwSQ2d5rng" title="What is a Frontend" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

The frontend is everything you see and interact with on a website or app. It's the pretty face that greets you when you land on a page. This includes the layout, colors, buttons, and forms you fill out. A good frontend makes using a website feel smooth and intuitive, like a well-designed cockpit in an airplane. It's all about creating a great user experience.

***

### 🗄️ Database

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/oTsGKqo_py4" title="What is a Database" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

A database is essentially a digital warehouse for information. It's where websites and apps store all their data in an organized way. Need to look up a customer's order history? That's stored in a database. Want to see all products under \$50? The database has that info too. It's like a super-efficient librarian who can find any piece of information in milliseconds.

***

### 🔌 API

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/ROCHqKMwtBM" title="What is an API" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

APIs allow different applications to communicate and share data with each other. When you use Google Maps inside another app, that's an API at work. When you click a Buy Now button on Amazon, APIs are firing at all cylinders behind the scenes.

APIs don't have to only be based on user action, either. For example, most websites implement some sort of tracking to ensure that the user experience is as smooth as possible. When you visit these websites, there are API calls being made as you navigate through their frontend.

APIs set the rules for how different pieces of software can talk to each other, making it possible for developers to integrate various services without starting from scratch.

An API has a few main components.

<Steps>
  <Step title="Headers">
    Headers are the configuration that rides along with an API request. They contain information like where the request is coming from and what type of data it contains.
  </Step>

  <Step title="Method">
    The method, also known as the verb, is assigned to an API to typically dictate the type of operation the API is designed to complete.

    * **GET**
      * Retrieve data
    * **POST**
      * Send data
    * **PUT / PATCH**
      * Update data
    * **DELETE**
      * Delete data

    <Info>
      Please note that when you build APIs in Xano, you can choose the method to apply, giving you full flexibility in exactly what function that API serves. While it isn't always best practice, a DELETE endpoint could technically do nothing but add new data, if it makes sense for your use case.
    </Info>
  </Step>

  <Step title="Query parameters / Request body">
    Query parameters and the request body are kind of the same thing, but sent in an API request in different ways.

    * **Query parameters** live as part of the request URL. If the API URL is `https://myapi.com/getThings` and expects you to send a thingId with your request, you would append it to the URL with `?thingId=99`, so your full request URL would be `https://myapi.com/getThings?thingId=99.` You would typically use query parameters for GET and DELETE endpoints.

    * **Request Body** is like a set of query parameters, but sent as a JSON object. It's more flexible when sending complex data types, such as lists, nested objects, or files.

    In the Xano visual builder, these are known as **inputs**. You can add inputs manually, or add a **Database Link** input to automatically populate and sync all fields from a database table.
  </Step>

  <Step title="Response">
    The response is whatever the API sends back once it has completed the logic it is meant to perform. An API doesn't necessarily need to deliver a response, but it is typical.

    Think of your frontend sending an API request when a user logs in. That API request would probably return information about the user logging in, such as their name, location, or other relevant user data.

    A response has a few different pieces, similar to what's included in the request, including **response headers** and a **response body**.
  </Step>
</Steps>

***

## 🏷️ Variables

Variables are like containers or labels that store information you want to use later in a workflow. Think of them as named boxes where you can keep different types of items, such as numbers, words, or lists. You give each box a name so you can easily find and use the information it holds whenever you need it in your project. This makes it simple to update or change the data without needing to rewrite everything.

Variables are temporary and exist only while a workflow is running, used for storing information you need to access quickly, whereas values in a database are like records in a filing cabinet, stored permanently until you decide to update or delete them, accessible across various workflows and sessions. This makes databases ideal for managing large sets of data over time, and variables more appropriate for temporary data handling.

***

### 🗃️ JSON

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/ouVQFne9IpI" title="What is JSON" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

JSON is a handy way of formatting data that's easy for both humans and computers to understand. JSON organizes information into simple key-value pairs, kind of like a really well-structured grocery list. It's lightweight and flexible, which is why developers love using it to pass data between servers and web applications.

For an example of how JSON can supercharge your data structure, take this example of a hand-written grocery list compared to a JSON equivalent.

<Tabs>
  <Tab title="Handwritten List">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/707ef008-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=505075517eb655653881176f5eb42471" width="680" height="876" data-path="images/707ef008-image.jpeg" />
    </Frame>
  </Tab>

  <Tab title="JSON">
    ```json  theme={null}
    [
      {
        "category": "Dairy",
        "items": [
          "Eggs",
          "Milk",
          "Cheddar cheese"
        ]
      },
      {
        "category": "Bakery",
        "items": [
          "Bread"
        ]
      },
      {
        "category": "Meat",
        "items": [
          "Chicken breast",
          "Ground beef"
        ]
      },
      {
        "category": "Household",
        "items": [
          "Candles",
          "Laundry detergent"
        ]
      },
      {
        "category": "Grains",
        "items": [
          "Rice"
        ]
      },
      {
        "category": "Supplements",
        "items": [
          "Protein powder"
        ]
      },
      {
        "category": "Produce",
        "items": [
          "Grapes"
        ]
      }
    ]
    ```
  </Tab>
</Tabs>

JSON follows a structure of `key: value` pairs. The key typically defines what the value represents, and the value is the actual value itself.

While it may seem similar, **JSON is not code**. It is just a standard way to structure data. For a real-world comparison, maybe you have a favorite news site or blog that you visit daily. You are used to the format they provide so the information is easily digestible. Now, imagine if every day, they decided to follow a different, unorganized structure instead. This is why data standardization is important, and JSON is a very effective way of achieving this.

#### 📄 Objects

An object represents the whole of a thing, such as a person, place, vehicle, form submission -- the possibilities are endless and fully dependent on what you are building. A JSON object can have multiple keys and values inside.

Here is an example of a JSON object that represents user data.

```json  theme={null}
{
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "isStudent": false
}
```

As you can see, we have our **keys**, such as `name`, `age`, and `city`, as well as our values, which are the actual data that belongs to this user.

#### 📑 Arrays

JSON can also represent lists of items, like the example below. It looks almost exactly the same, but now we have multiple people inside of an **array**, or list, denoted by square brackets.

```json  theme={null}
[
  {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "isStudent": false
  },
  {
    "name": "Jane Smith",
    "age": 25,
    "city": "San Francisco",
    "isStudent": true
  },
  {
    "name": "Bob Johnson",
    "age": 35,
    "city": "Chicago",
    "isStudent": false
  }
]
```

#### Nested Data

Values don't just have to be single items, such as a person's name or email. You can also supply other objects or arrays for your values. In the below example, we've added an interests key and supplied an array of text strings for the value.

```json  theme={null}
{
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "isStudent": false,
  "interests": ["tennis",
                "visual development",
                "pizza"]
}
```

### ℹ️ JSON Data Types

You may have noticed a few mentions of things like integers or strings when learning about JSON. It is important to know what types of data are valid representations inside of a JSON object. One of the most important things to remember when working with JSON is that quotation marks are incredibly important and can be the difference between something working or falling apart.

🔤 **Strings** are surrounded by "quotation marks" and are just plain text.

```json  theme={null}
  {
    "name": "John Doe"
  }
```

🔢 **Integers** are numbers that are not decimals. Notice how we do not have quotation marks around `1994` in the example below. If we used `"1994"` instead, this would become a string.

```json  theme={null}
  {
    "year": 1994
  }
```

🔢 **Decimals&#x20;**&#x61;re numbers that contain a decimal point.

```json  theme={null}
  {
    "price": 9.99
  }
```

✅ **Booleans** are true or false values.

```json  theme={null}
    "exists": true
```

⛔ **Null&#x20;**&#x69;s a special data type that represents nothing in situations where you need to specify that nothing is provided.

```json  theme={null}
    "phone": null
```

📑 **Arrays** are lists of things. These could be any other valid JSON data type. You could even have an array of arrays if you wanted.

```json  theme={null}
[
    "red",
    "blue",
    "green"
    ]
```

📄 **Objects** are collections of key-value pairs enclosed in curly braces. Keys are always strings, but values can be any valid JSON data type.

```json  theme={null}
{
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "isStudent": false
  }
```


Built with [Mintlify](https://mintlify.com).