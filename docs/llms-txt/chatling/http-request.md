# Source: https://docs.chatling.ai/chatbot/builder/blocks/action/http-request.md

# Source: https://docs.chatling.ai/ai-agent/actions/http-request.md

# Source: https://docs.chatling.ai/chatbot/builder/blocks/action/http-request.md

# Source: https://docs.chatling.ai/ai-agent/actions/http-request.md

# Source: https://docs.chatling.ai/chatbot/builder/blocks/action/http-request.md

# Source: https://docs.chatling.ai/ai-agent/actions/http-request.md

# Source: https://docs.chatling.ai/chatbot/builder/blocks/action/http-request.md

# HTTP Request Block

> Learn about the HTTP Request block and how to set it up in the Builder.

The HTTP Request block is used to send HTTP requests to external APIs and services. You can use it to fetch data, send data, or perform other actions by interacting with APIs.

The block consists of the following components:

* **Request method**: The HTTP method to use for the request, such as GET, POST, PUT, PATCH, and DELETE.
* **URL**: The URL of the API endpoint to send the request to.
* **Request options**: You can configure additional options for the request, such as headers, query parameters, and request body.
* **Capture Response**: You can capture the responses from the API and store them a variable. The response must be in JSON format.

## Method and URL

In order to send a request, you must provide the endpoint URL and select the appropriate request method. The following request methods are supported:

* **GET**: Retrieve data from the server.
* **POST**: Send data to the server.
* **PUT**: Update data on the server.
* **PATCH**: Partially update data on the server.
* **DELETE**: Delete data from the server.

As an example, an endpoint URL might look like this:

`https://openlibrary.org/works/OL45804W.json`

## Request Options

When sending requests to external APIs, you may need to provide additional options such as headers, query parameters, and request body. Here are the available options:

* **Headers**: You can set headers for the request, such as Content-Type, Authorization, and Accept.
* **Query Params**: The URL query parameters to include for the request.
* **Request Body**: The request payload which can be passed as form data, form URL encoded, or raw JSON.

### How to use variables in JSON payload

To use variables in the request payload, you must enclose the variable's name in double curly braces within quotes. Here's an example:

```json  theme={null}
{
    "name": "{{contact_name}}",
    "age": 21,
    "email": "{{contact_email}}"
}
```

Some points to note:

* Make sure that the variables exist and that their name is correct. Otherwise, they will not be replaced with the actual value.
* If you change a variable's name, you must also update the JSON payload to reflect the change.
* Variables must be enclosed in double curly braces as shown in the example above.

## Capture Response

Responses from the API can be captured and stored in one or more variables. In order for this to work, the response from the endpoint must be in JSON format.

Click the `Add` button to add a new row for capturing a value. You must specify the key and the variable where the value will be stored.

The naming convention for the key is as follows:

* **Top level data**: use the key, such as name or age.
* **Nested data**: use dot notation, such as user.name or profile.address.city.
* **Array data**: use the index, such as users\[0].name or countries\[1].cities\[0].population.

Let's take a look at an example. Below is a sample JSON response from an API endpoint:

```json  theme={null}
{
    "title": "Fantastic Mr Fox",
    "permalink": "/works/OL45804W",
    "authors": [
    {
        "author": {
            "name": "Roald Dahl"
        },
    }
    ],
    "description": "The main character of Fantastic Mr. Fox is an extremely clever anthropomorphized fox named Mr. Fox. He lives with his wife and four little foxes. In order to feed his family, he steals food from the cruel, brutish farmers named Boggis, Bunce, and Bean every night.\r\n\r\nFinally tired of being constantly outwitted by Mr. Fox, the farmers attempt to capture and kill him. The foxes escape in time by burrowing deep into the ground. The farmers decide to wait outside the hole for the foxes to emerge. Unable to leave the hole and steal food, Mr. Fox and his family begin to starve. Mr. Fox devises a plan to steal food from the farmers by tunneling into the ground and borrowing into the farmer's houses.\r\n\r\nAided by a friendly Badger, the animals bring the stolen food back and Mrs. Fox prepares a great celebratory banquet attended by the other starving animals and their families. Mr. Fox invites all the animals to live with him underground and says that he will provide food for them daily thanks to his underground passages. All the animals live happily and safely, while the farmers remain waiting outside in vain for Mr. Fox to show up.",
    "meta": {
        "published_at": "1970-06-01"
    },
}
```

To capture the title, date of publication, and author name from the response, you would use the following keys:

* **Title**: `title`
* **Published date**: `meta.published_at`
* **Author Name**: `authors[0].author.name`

<img src="https://chatling-assets.b-cdn.net/http-request-capture-response-example.png" alt="HTTP Request capture response example" width="300" />
