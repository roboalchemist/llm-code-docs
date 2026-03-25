# Source: https://docs-containers.back4app.com/docs/react-native/graphql/users/user-sign-up-relay.md

---
title: User Sign Up
slug: docs/react-native/graphql/users/user-sign-up-relay
description: In this guide you will learn how to implement a user sign up into a React Native application using GraphQL and Relay Modern
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-20T13:13:12.866Z
updatedAt: 2025-01-16T19:39:02.992Z
---

# User Sign up with Relay

## Introduction

The first thing your app will do is probably ask the user to sign up. Back4App/Parse already provides by default a class User, which already has a ready-to-use GraphQL Mutation to sign up new users when it is necessary for your app.

In this guide, you will create a Sign-Up feature for a React Native app using Relay to persist our data on Back4App.

The flow is very similar to create a Query Renderer. After implementation, the Relay Compiler will check Frontend(fragments) and Backend(data model) and return if everything matches. If so, the types and the application is already to communicate with the backend.

:::hint{type="success"}
**At any time, you can access this project via our GitHub repositories to checkout the styles and complete code.**

- [**JavaScript Example Repository**](https://github.com/templates-back4app/react-native-graphql-relay-js-users)
:::

## Goal

At the end of this guide, you will have a React Native application with the user sign up feature implemented as show below.

## Prerequisites

- **An app created at Back4App using the&#x20;**[**Parse Server Version 3.10**](https://www.back4app.com/docs/platform/parse-server-version)**&#x20;or above.**
- **You have to conclude the&#x20;**[**Relay Environment setup tutorial**](https://www.back4app.com/docs/react-native/graphql/relay-setup)**:**
- **For this tutorial we are going to use the Expo as a React Native framework;**
- **For this tutorial we are going to use Javascript as our default implementation language;**
- **For this tutorial we are going to use our Style css sample;**

## 1 - Creating Sign Up Form

If the application already has a Form component, go to step 2. Otherwise, feel free to follow our boilerplate.

We will use an Expo app having with which has a Form with the username and password. To make our life easier, we are going to use some third-party libraries to help build the SignUp feature. Our form component will use the formik library. It is important to note that it doesn’t infer the final result.

- Install formik

:::BlockQuote
yarn add formik
:::

- Create a new component and name it FormSignUp.js
- Paste the following code inside it:

```javascript
1	import React, { useState } from 'react';
2	import { Button, Text, TextInput, View, TouchableOpacity } from "react-native";
3	import { useFormik, FormikProvider } from 'formik';
4	import Styles from "../../Style"
5	import environment from '../../relay/environment';
6	
7	const SignUp = () => {
8	  const [userCreated, setUserCreated] = useState();
9	
10	  const onSubmit = (values) => {
11	    // @todo the mutation will be implemented here
12	  };
13	
14	  const formikbag = useFormik({
15	    initialValues: {
16	      username: '',
17	      password: '',
18	    },
19	    onSubmit,
20	  });
21	
22	  const { handleSubmit, setFieldValue } = formikbag;
23	  if (userCreated?.id) {
24	    return (
25	      <View style={ {marginTop: 15, alignItems: 'center'} }>
26	        <Text>User {userCreated.name} created</Text>
27	      </View>
28	    );
29	  }
30	
31	  return (
32	    <FormikProvider value={formikbag}>
33	      <View style={Styles.login_wrapper}>
34	        <View style={Styles.form}>
35	          <Text>Username</Text>
36	          <TextInput
37	            name={"username"}
38	            style={Styles.form_input}
39	            autoCapitalize="none"
40	            onChangeText={(text) => setFieldValue("username", text)}
41	          />
42	          <Text>Password</Text>
43	          <TextInput
44	            style={Styles.form_input}
45	            name={"password"}
46	            autoCapitalize="none"
47	            secureTextEntry
48	            onChangeText={(text) => setFieldValue("password", text)}
49	          />
50	          <TouchableOpacity onPress={() => handleSubmit()}>
51	            <View style={Styles.button}>
52	              <Text style={Styles.button_label}>{"Sign in"}</Text>
53	            </View>
54	          </TouchableOpacity>
55	        </View>
56	      </View>
57	    </FormikProvider>
58	  );
59	};
60	
61	export default SignUp;
```

The application should run ok until here. The form should look like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/p7wZa2TV6QilONY0iUHTN_image.png" signedSrc size="70" width="828" height="1792" position="center" caption}

Let’s situate our component explaining some points:

- **We are using formik to control our form values. You can also use a form with HTML, CSS, and JS.**
- **styled-components will be used to give simple CSS styles for the component**
- **There is a use state to control if our user was registered or not.**

Please, look at the onSubmit function. Note that the Relay Mutation will be inside of this function. Again, it is not a problem if the application is not using Formik. Once we are implementing a Form Component, the Relay Mutation only needs to be called inside the submit function.

## 2 - Creating the Mutation

Using the Colocation principle, let’s create a new folder the most closely to the Form Component. Name it as mutations. To remember about colocation you can go to our doc [**Getting Started**](https://www.back4app.com/docs/react-native/graphql/get-started-relay-graphql), where we give a brief about it.

Exemplifying how handles the colocation, in the image below the component SignUp is wrapped by a folder. Inside of this folder is where we will create the folder mutations. And, inside of mutations folder, we will create the Relay Mutation. This works perfectly on big projects. Everything related to the component will be placed close to it and will be more easily work, find, etc.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/OLpnCu7Lsfj0TdMoCgF44_image.png" signedSrc size="80" width="291" height="105" position="center" caption}

:::hint{type="success"}
use this approach for every new mutation of the application. Every time put it close to the component that will use it.
:::

Inside this folder, you will create a new file called SignUpMutation.js. According to our last guide where we explained the Relay Mutations, you will create a function inside and call it commit. You can use the code below:

```javascript
1	function commit({ environment, input, onCompleted, onError }) {
2	  const variables = { input };
3	
4	  commitMutation(environment, {
5	    mutation,
6	    variables,
7	    onCompleted,
8	    onError,
9	  });
10	}
11	
12	export default {
13	  commit,
14	};
```

Before going back to the form component, let’s create our variable that will receive the GraphQL Fragment, representing the Mutation. The GraphQL Fragment is what the Relay Compiler will read and match with schema.graphql.

Before the commitMutation, copy and paste the following code:

```javascript
1	const mutation = graphql`
2	  mutation SignUpMutation($input: SignUpInput!) {
3	    signUp(input: $input) {
4	      viewer {
5	        user {
6	          id
7	          username
8	          createdAt
9	        }
10	        sessionToken
11	      }
12	    }
13	  }
14	`;
```

Final file:

```javascript
1	import {commitMutation, graphql} from 'react-relay';
2	
3	const mutation = graphql`
4	  mutation SignUpMutation($input: SignUpInput!) {
5	    signUp(input: $input) {
6	      viewer {
7	        user {
8	          id
9	          username
10	          createdAt
11	        }
12	        sessionToken
13	      }
14	    }
15	  }
16	`;
17	
18	function commit({environment, input, onCompleted, onError}) {
19	  const variables = {input};
20	
21	  commitMutation(environment, {
22	    mutation,
23	    variables,
24	    onCompleted,
25	    onError,
26	  });
27	}
28	
29	export default {
30	  commit,
31	};
```

:::hint{type="success"}
Since the GraphQL Fragment represents the backend, to get the code of Relay Mutation, you can go to the [**Back4App GraphQL Cookbook**](https://www.back4app.com/docs/react-native/graphql/users/back4app.com/docs/parse-graphql/graphql-sign-up) and find the Fragment.
:::

Run yarn relay to generate the new mutation and update the files. If everything is okay the types of mutation it will be generated and you can go forward.

## 3 - Implement On Submit Function

The submit step is the most important. Here is where the Relay Mutation magic happens.

:::hint{type="success"}
this step gets the values of the form from the formik. If the application is not using formik, the values need to be available here independent of the way they get it.
:::

Back to Form Component, let’s start the implementation of the Relay Mutation.

- **Import the mutation**

```javascript
1	import SignUpMutation from './mutations/SignUpMutation';
```

- **Inside of OnSubmit function, stars creating the input variables:**

```javascript
1	const onSubmit = (values) => {
2	    const {username, password} = values;
3	    
4	    const input = {
5	      userFields: {
6	        username,
7	        password,
8	      },
9	    };
10	}
```

:::hint{type="info"}
The values are injected by Formik. Here, if you are not using formik, the values will likely come via the form’s native oSubmit or as you prefer.
:::

- **At last, call the Mutation passing all props (remember to import them).**

```javascript
1	    SignUpMutation.commit({
2	      environment,
3	      input,
4	      onCompleted: ({signUp}) => {
5	        const { viewer } = signUp;
6	        const { sessionToken, user } = viewer;
7	
8	        if (sessionToken !== null) {
9	          alert(`user ${user.username} successfully created`);
10	          setUserCreated(user);
11	          return;
12	        }
13	      },
14	      onError: (errors) => {
15	        alert(errors[0].message);
16	      },
17	    });
```

- **Final result of onSubmit**

```javascript
1	const onSubmit = (values) => {
2	    const { username, password } = values;
3	    
4	    const input = {
5	      userFields: {
6	        username,
7	        password,
8	      },
9	    };
10	
11	    SignUpMutation.commit({
12	      environment,
13	      input,
14	      onCompleted: ({signUp}) => {
15	        const { viewer } = signUp;
16	        const { sessionToken, user } = viewer;
17	    
18	        if (sessionToken !== null) {
19	          alert(`user ${user.username} successfully created`);
20	          setUserCreated(user);
21	          return;
22	        }
23	      },
24	      onError: (errors) => {
25	        alert(errors[0].message);
26	      },
27	    });
28	};
```

Run your project, register your User and then check it on Back4App Dashboard. The Mutation will return the values from the server. Once the session token is returned, the application can start to manage it.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/D3FfkncQ0Xg1nFqMylUgI_image.png" signedSrc size="50" width="828" height="1792" position="center" caption}

## Handling Errors

On commit mutation, the application can handle errors on onError. Always will receive an array of errors. The most common is this array has only one object containing the error message. See the example below:

:::BlockQuote
1	\{
2	  "errors": \[
3	    \{
4	      "message": "Account already exists for this username.",
5	      "locations": \[
6	        \{
7	          "line": 2,
8	          "column": 3
9	        }
10	      ],
11	      "path": \[
12	        "signUp"
13	      ],
14	      "extensions": \{
15	        "code": 202
16	      }
17	    }
18	  ],
19	  "data": \{
20	    "signUp": null
21	  }
22	}
:::

Based on this example feel free to create your our error handle. By now, if some error is returned we just show it by an alert:

```javascript
1   onError: (errors) => {
2     alert(errors[0].message);
3   },
```

## Conclusion

You now have an application with a sign-up feature fully working. In the next guide, you will understand how to authenticate a user(login) and log out him using the same approach. You will also use Relay Mutations to call our backend.
