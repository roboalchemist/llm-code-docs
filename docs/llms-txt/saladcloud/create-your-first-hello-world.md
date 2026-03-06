# Source: https://docs.salad.com/container-engine/tutorials/nodejs/create-your-first-hello-world.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Your first "hello world"

*Last Updated: September 24, 2024*

## **Creating a *"hello world"* Node.js Application**

First, we will start by creating a directory for our project and then install some dependencies for our simple “Hello
world” app using the command line.

```shell  theme={null}
mkdir nodejs-server

cd nodejs-server
```

\*\*Install npm And Express Framework: \*\* Install npm and Express, which is a Node.js framework.

**Then, initialize npm** in our directory. Copy or use the command below in your command line or terminal.

```shell  theme={null}
npm init
```

Above, **`npm`** creates a **`package.json`** that holds the dependencies of the app.

\*\*Next, \*\*install the Express framework dependency.

```shell  theme={null}
npm install express --save
```

Codebase should look like this below:

**Create a package.json file with the following content:**

```json  theme={null}
{
  "name": "node-app",
  "version": "1.0.0",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  },
  "license": "MIT",
  "dependencies": {
    "express": "^4.18.2"
  }
}
```

**Create an app.js file with an HTTP server that will return Hello world.**

Here is the code below :

```javascript  theme={null}
const express = require('express')
const app = express()

// This tells the app which port to listen to
app.listen(process.env.PORT || 5000, () => {
  console.log(`Server is running on port`)
})

//This shows the response that will sent to the user
app.get('/', (req, res) => {
  res.send('Hello World')
})
```

**Now, Save this file above, open your terminal, CLI (Command Line) to run the application**

```shell  theme={null}
node app.js
```

The app is now ready to launch:

It will show you on your terminal ***`Server is running on port 5000`***

![](https://files.readme.io/e15a288-node.PNG "node.PNG")

Go to your browser, copy and paste \*\* `http://localhost:8080/` \*\* in your browser to view it.

Here is a ***“Hello world”*** output on my browser :

![](https://files.readme.io/77b4901-hello_world.PNG "hello world.PNG")
