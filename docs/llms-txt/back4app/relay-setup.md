# Source: https://docs-containers.back4app.com/docs/react-native/graphql/relay-setup.md

---
title: Prepare Environment
slug: docs/react-native/graphql/relay-setup
description: In this guide you will learn how to prepare the environment for relay
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T18:35:45.058Z
updatedAt: 2024-03-29T01:41:21.748Z
---

# Relay Setup

## Introduction

In our previous guide, we’ve learned how to get the schema file, save it, and paste it on our React Native application. In this guide, we are going to install Relay and prepare our environment to start developing a React Native Application.

## Goal

In order to set up Relay we will need first to install Relay on our React Native application and then prepare the Relay environment.

## Prerequisites

:::hint{type="info"}
- We recommend a basic understanding of the following topics: [**Relay Modern**](https://relay.dev/), [**Babel JS**](https://babeljs.io/), JavaScript (ECS5 and ECS6), [**GraphQL.js**](https://github.com/graphql/graphql-js) README
- A React Native basic project running on your local environment.
- A schema.graphql file download on your React Native project.
:::

In the following steps you’ll find a basic Relay installation focused on a React Native Application. If you want to deep dive into this topic please visit the [**official documentation**](https://relay.dev/docs/en/installation-and-setup#docsNav).

## 1 - Installing React Relay Official API

Let’s start installing the official library *react-relay*. This library is the Relay Core Team official API and has everything to build the data fragments.

:::BlockQuote
1   yarn add react-relay\@10.0.0
:::

:::hint{type="success"}
Important installing Relay Modern for this tutorial with 10.0.0 as version. From verion 11.0.0 the approach to use the react-relay is different because of the new hooks.
:::

## 2 - Relay Config

The Relay Config has the info necessary for the Relay Compiler. Inside it, we will specify where Relay Compiler can find the schema.file, which folders should be looked up, and other configs. Let’s first install the relay-config package:

:::BlockQuote
1   yarn add --dev relay-config
:::

:::hint{type="success"}
NOTE: This tutorial uses yarn as a package client, but you can use npm anyway.
:::

Now let’s create the Relay Config file where Relay will find the schema path.

- **Create a new file inside the root of the application.**
- **Name it as relay.config.js.**

Open the file and save it with the information below:

:::BlockQuote
1   module.exports = \{
2     schema: './data/schema.graphql',
3     src: './',
4   };
:::

## 3 - Relay Babel Plugin

To convert the GraphQL artifacts at runtime, we need to install a babel plugin.

:::BlockQuote
1   yarn add --dev babel-plugin-relay graphql
:::

Now, inside your babel config file, you must add on plugins array the Relay Babel Plugin. The final babel.config.js will look like this:

:::BlockQuote
1    \{
2     "plugins": \[
3       "relay"
4     ]
5    }
:::

In expo projects follow the same approach adding the plugins array inside of the babel.config.js right after the presets array. The final result should look:

```javascript
1	module.exports = function (api) {
2	  api.cache(true);
3	  return {
4	    presets: [
5	      "babel-preset-expo",
6	    ],
7	    plugins: [
8	      'relay'
9	    ]
10	  };
11	};
```

:::hint{type="success"}
The relay plugin must run before other plugins for a correct transformation of GraphQL artifacts. Check the plugin babel docs to know more.
:::

## 4 - Relay Compiler

Since our first documentation, we have been explaining about the Relay Compiler. For our application to compile our data fragments, we will install it now.

:::BlockQuote
1   yarn add **--**&#x64;ev rela&#x79;**-**&#x63;ompiler
:::

Let’s open our package.json and configure a new script command to run the relay compiler.

:::BlockQuote
1    "relay": "relay-compiler --watchman false"
:::

Watchman is responsible for configuring whether the Relay Compiler must be looking for any changes on relay fragments. If true it will rerun at each change. If false it will run after you run the yarn relay by itself.

The package.json file should look like this:

```json
1	  "scripts": {
2	    "android": "react-native run-android",
3	    "ios": "react-native run-ios",
4	    "start": "react-native start",
5	    "test": "jest",
6	    "lint": "eslint .",
7	    "relay": "relay-compiler --watchman false"
8	  },
```

## 5 - Run yarn relay

Finally, with installation steps done, we can run the yarn relay command on the root of the application:

:::BlockQuote
1   yarn relay
:::

Since we don’t build any data fragment, the Relay Compiler returns any file changed:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/TsgibxDpL2xrdQWVEDSuq_image.png" signedSrc size="80" width="385" height="101" position="center" caption}

Nice, your application has the Relay already installed and configured. Now, let’s implement our Environment to start making requests to the Back4App server.

## 6 - Preparing the fetch environment

The Relay Environment defines how the Network Layer will handle the requests and how the *Relay Store* must work. The Store controls our data on the frontend by updating it only when changed and caching it. A simple Environment will need at least the Network Layer and the Store.

**Network Layer**

The [**Network Layer**](https://relay.dev/docs/en/network-layer) is easy to build. It will handle each request of our application, making queries, mutations, and subscriptions (if your application supports). Consuming it, the Relay will know-how to prepare the calls to access the application server.

**Relay Store**

The [**Store**](https://relay.dev/docs/en/relay-store.html) is responsible for update the data of our application on the client-side. Each request can have an updater function. Inside the updater function, you can use a list of helper functions to update your data with the Store Interface.

In order to prepare the Relay environment we need to create an environment config file. The file will be read by the Query Renderer every time a query is performed. Let’s prepare this file.

### **6.1 - Create the Environment File**

We will follow the principle of design from Relay Library, the collocation concept. To start, let’s create a folder on the root of the application and name it relay. Inside it, create a file and name it environment.js.

### **6.2 - Configure the Environment**

After that, import from relay-runtime all we need:

```javascript
1	import {
2	    Environment,
3	    Network,
4	    RecordSource,
5	    Store,
6	} from 'relay-runtime';
```

### **6.3 - Configure the Network Layer**

The network layer needs a function to fetch the data from the server. First of all, let’s create a fetch function responsible to perform a POST request:

```javascript
1	const fetchQuery = async (request, variables) => {
2	  const body = JSON.stringify({
3	    query: request.text,
4	    variables,
5	  });
6	
7	  const headers = {
8	    Accept: 'application/json',
9	    'Content-type': 'application/json',
10	    'X-Parse-Application-Id': 'X-Parse-Application-Id',
11	    'X-Parse-Client-Key': 'X-Parse-Client-Key',
12	  };
13	
14	  try {
15	      const response = await fetch(`https://parseapi.back4app.com/graphql`, {
16	        method: 'POST',
17	        headers,
18	        body,
19	      });
20	  
21	      const data = await response.json();
22	  
23	      if (data.errors) {
24	        throw data.errors;
25	      }
26	  
27	      return data;
28	    } catch (err) {
29	      console.log('err on fetch graphql', err);
30	  
31	      throw err;
32	    }
33	};
```

:::hint{type="success"}
We wrapper the request for the backend by a try-catch. Having an error will be thrown and the application will handle it. Otherwise will follow the normal behavior and return the data.
:::

On Network Layer it’s also where you configure your application-server connection. At Back4App we use two main keys: Application Id and Client Key. The keys must be informed on the headers as long as the server URL. To get this information go to your App, and click on API Console -> GraphQL menu.

With the GraphQL console open, you will see the URL on the top, and on the bottom the application keys necessary. Replace with your info the fetch function.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/jqLTXI5I-dNrDTnR6eJ0v_image.png)

:::hint{type="success"}
Remember to do not expose the master key
:::

### **6.4 - Export the Environment**

The relay-runtime provides the functions necessary to consume the Network Layer and creates the Store. Finally, let’s combine them into a new Environment and export to our application. Use the code below on your Environment file.

```javascript
1	const environment = new Environment({
2	  network: Network.create(fetchQuery),
3	  store: new Store(new RecordSource()),
4	});
5	
6	export default environment;
```

Environment final file will look like this:

```javascript
1	import {
2	  Environment,
3	  Network,
4	  RecordSource,
5	  Store,
6	} from 'relay-runtime';
7	
8	const fetchQuery = async (request, variables) => {
9	  const body = JSON.stringify({
10	    query: request.text,
11	    variables,
12	  });
13	
14	  const headers = {
15	    Accept: 'application/json',
16	    'Content-type': 'application/json',
17	    'X-Parse-Application-Id': 'X-Parse-Application-Id',
18	    'X-Parse-Client-Key': 'X-Parse-Client-Key',
19	  };
20	
21	  try {
22	        const response = await fetch(`https://parseapi.back4app.com/graphql`, {
23	          method: 'POST',
24	          headers,
25	          body,
26	        });
27	    
28	        const data = await response.json();
29	    
30	        if (data.errors) {
31	          throw data.errors;
32	        }
33	    
34	        return data;
35	      } catch (err) {
36	        console.log('err on fetch graphql', err);
37	    
38	        throw err;
39	      }
40	};
41	
42	const environment = new Environment({
43	  network: Network.create(fetchQuery),
44	  store: new Store(new RecordSource()),
45	});
46	
47	export default environment;
```

## Conclusion

Awesome. Now with the Relay and Relay environment installed and configured it’s time to start to consume the Back4App GraphQL API. So, the next step is to create our first Query Renderer and communicate it to our server.
