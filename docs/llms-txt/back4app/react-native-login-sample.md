# Source: https://docs-containers.back4app.com/docs/react-native/graphql/users/react-native-login-sample.md

---
title: User Login
slug: docs/react-native/graphql/users/react-native-login-sample
description: In this guide you will learn how to implement a user sign in into a React Native application using GraphQL and Relay Modern
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-20T13:25:16.408Z
updatedAt: 2025-01-16T19:39:22.053Z
---

# React Native Login sample using Relay

## Introduction

In the last tutorial, you’ve implemented the User Sign Up to your React Native App using Back4App and Relay. In this guide, you’ll build the login mechanism complementing your App auth feature.

As you may know, Parse already provides by default a User class User, which already has a ready-to-use GraphQL Mutation to login in users when it is necessary for your app.

The flow here will be very similar to the User Sign Up tutorial. You’‘ll build a Login screen using formik, then this form will call the Relay Mutation. The Relay Mutation will communicate with the Back4App Server handling the whole process of authentication.

:::hint{type="success"}
**At any time, you can access this project via our GitHub repositories to checkout the styles and complete code.**

- [**JavaScript Example Repository**](https://github.com/templates-back4app/react-native-graphql-relay-js-users)
:::

## Goal

At the end of this guide, you will have a React Native application with the user login feature implemented, as shown below.

### Prerequisites

:::hint{type="info"}
- An app created at Back4App using the Parse Server Version 3.10 or above.
- You have to conclude the [**Relay Environment setup tutorial**](https://www.back4app.com/docs/react-native/graphql/relay-setup):
- Expect an app with a simple sign in form. Here we are using an Expo app having a Form with the username and password.
- For this tutorial, we are going to use the Expo as a React Native framework;
- For this tutorial, we are going to use Javascript as our default implementation language;
- For this tutorial we are going to use our Style css sample;
:::

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/HLS0YNmG6UzTVGL_mVB82_image.png" signedSrc size="60" width="828" height="1792" position="center" caption}

## 1 - Creating Sign In Form

If the application already has a Form component, go to step 2. Otherwise, feel free to follow our boilerplate. The form is similar to the form used in the Sign-Up doc. You can also use it as a basis for login. Please go to User [**User Sign Up**](https://www.back4app.com/docs/react-native/graphql/user-sign-up-relay) if you want to learn how to implement it. The Login form code should look like this:

```javascript
1	import React, {useState} from 'react';
2	import environment from '../../relay/environment';
3	import {FormikProvider, useFormik} from 'formik';
4	import { Button, Text, TextInput, View, TouchableOpacity } from 'react-native';
5	import Styles from "../../Style"
6	
7	const SignIn = () => {
8	  const [userLogged, setUserLogged] = useState(null);
9	
10	  const onSubmit = async (values) => {
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
22	  const {handleSubmit, setFieldValue} = formikbag;
23	
24	  if (userLogged?.id) {
25	    return (
26	      <View style={ {marginTop: 15, alignItems: 'center'} }>
27	        <Text>User {userLogged.name} logged</Text>
28	      </View>
29	    );
30	  }
31	
32	  return (
33	    <FormikProvider value={formikbag}>
34	        <View style={Styles.login_wrapper}>
35	            <View style={Styles.form}>
36	                <Text>Username</Text>
37	                <TextInput
38	                    name={"username"}
39	                    style={Styles.form_input}
40	                    autoCapitalize="none"
41	                    onChangeText={(text) => setFieldValue("username", text)}
42	                />
43	                <Text>Password</Text>
44	                <TextInput
45	                    style={Styles.form_input}
46	                    name={"password"}
47	                    autoCapitalize="none"
48	                    secureTextEntry
49	                    onChangeText={(text) => setFieldValue("password", text)}
50	                />
51	                <TouchableOpacity onPress={() => handleSubmit()}>
52	                    <View style={Styles.button}>
53	                        <Text style={Styles.button_label}>{"Sign in"}</Text>
54	                    </View>
55	                </TouchableOpacity>
56	            </View>
57	        </View>
58	    </FormikProvider>
59	  );
60	};
61	
62	export default SignIn;
```

Run your application, and you’ll see a screen as shown below.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/xp1JZ8tdTWLrt9vgHL6TX_image.png" signedSrc size="60" width="828" height="1792" position="center" caption}

Please, look at the onSubmit function. Note that the Relay Mutation will be inside of this function. Again, it is not a problem if the application is not using Formik. Once you’re implementing a Form Component, the Relay Mutation only needs to be called inside the submit function.

## 2 - Creating the Mutation

Using the Colocation principle, let’s create a new folder called mutations the most closely to the Form Component. If you want to learn more about colocation please go to [**Getting Started**](https://www.back4app.com/docs/react-native/graphql/get-started-relay-graphql) guide.

In the image below, you can see the colocation principle in practice. Everything related to the component is close to it. A folder wraps the LogIn component, and inside of it, you’ll create another folder called mutations. In the mutations’ folder, you will create the Relay Mutation.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Lm6WApFKYgSa8kzB7Wqaj_image.png" signedSrc size="80" width="290" height="100" position="center" caption}

:::hint{type="success"}
This pattern works perfectly on big projects. Every time you have a new mutation, put it close to the component that will use it.
:::

Inside this folder, you will create a new file called LogInMutation.js. According to our Working with users guide, where we explained the Relay Mutations, you will create a commit function, as shown below.

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
2	  mutation LogInMutation($input: LogInInput!) {
3	    logIn(input: $input) {
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
1	import { commitMutation, graphql } from 'react-relay';
2	
3	const mutation = graphql`
4	  mutation LogInMutation($input: LogInInput!) {
5	    logIn(input: $input) {
6	      viewer {
7	        user {
8	          id
9	          createdAt
10	          updatedAt
11	          username
12	        }
13	        sessionToken
14	      }
15	    }
16	  }
17	`;
18	
19	function commit({ environment, input, onCompleted, onError }) {
20	  const variables = { input };
21	
22	  commitMutation(environment, {
23	    mutation,
24	    variables,
25	    onCompleted,
26	    onError,
27	  });
28	}
29	
30	export default {
31	  commit,
32	};
```

:::hint{type="success"}
Since the GraphQL Fragment represents the backend, to get the code of Relay Mutation, you can go to the [**Back4App GraphQL Cookbook**](https://www.back4app.com/docs/react-native/graphql/users/back4app.com/docs/parse-graphql/graphql-sign-in) and find the Fragment.
:::

Run yarn relay to generate the new mutation and update the files. If everything is okay the types of mutation it will be generated and you can go forward.

## 3 - Implement On Submit Function

The submit step is the most important. Here is where the Relay Mutation magic happens.

:::hint{type="info"}
this step gets the values of the form from the formik. If the application is not using formik, the values need to be available here independent of the way they get it.
:::

Back to Form Component, let’s start the implementation of the Relay Mutation.

Import the mutation

```javascript
1	import LogInMutation from './mutations/LogInMutation';
```

Inside of OnSubmit function, stars creating the input variables:

```javascript
1	const onSubmit = (values) => {
2	    const {username, password} = values;
3	    const input = {
4	        username,
5	        password,
6	    };
7	}
```

:::hint{type="info"}
The values are injected by Formik. Here, if you are not using formik, the values will likely come via the form’s native oSubmit or as you prefer.
:::

At last, call the Mutation passing all props (remember to import them).

```javascript
1	    LogInMutation.commit({
2	      environment,
3	      input,
4	      onCompleted: (response) => {
5	        if(!response?.logIn || response?.logIn === null) {
6	          alert('Error while logging');
7	          return;
8	        }
9	
10	        const { viewer } = response?.logIn;
11	        const { sessionToken, user } = viewer;
12	
13	        if (sessionToken !== null) {
14	          setUserLogged(user);
15	          alert(`user ${user.username} successfully logged`);
16	          return;
17	        }
18	      },
19	      onError: (errors) => {
20	        alert(errors[0].message);
21	      },
22	    });
```

Final result of onSubmit

```javascript
1	const onSubmit = (values) => {
2	    const { username, password } = values;
3	    
4	    const input = {
5	      username,
6	      password,
7	    };
8	
9	    LogInMutation.commit({
10	      environment,
11	      input,
12	      onCompleted: (response) => {
13	        if(!response?.logIn || response?.logIn === null) {
14	          alert('Error while logging');
15	          return;
16	        }
17	
18	        const { viewer } = response?.logIn;
19	        const { sessionToken, user } = viewer;
20	
21	        if (sessionToken !== null) {
22	          setUserLogged(user);
23	          alert(`user ${user.username} successfully logged`);
24	          return;
25	        }
26	      },
27	      onError: (errors) => {
28	        alert(errors[0].message);
29	      },
30	    });
31	};
```

Run your project, register your User and then check it on Back4App Dashboard. The Mutation will return the values from the server. Once the session token is returned, the application can start to manage it.

Testing using the user created on the last tutorial. If everything works ok, it will be showed an alert like below:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/0_SLXED_VK1LnAADDzUuy_image.png" signedSrc size="70" width="828" height="1792" position="center" caption}

## Handling Errors

On commit mutation, the application can handle errors on onError. Always will receive an array of errors. The most common is this array has only one object containing the error message. See the example below:

:::BlockQuote
1	\{
2	  "errors": \[
3	    \{
4	      "message": "Invalid username/password.",
5	      "locations": \[
6	        \{
7	          "line": 2,
8	          "column": 3
9	        }
10	      ],
11	      "path": \[
12	        "logIn"
13	      ],
14	      "extensions": \{
15	        "code": 202
16	      }
17	    }
18	  ],
19	  "data": \{
20	    "logIn": null
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

You now have an application with a sign-in feature fully working. In the next guide, you will understand how to log out him using the same approach. You will also use Relay Mutations to call our backend.
