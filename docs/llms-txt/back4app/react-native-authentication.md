# Source: https://docs-containers.back4app.com/docs/react-native/graphql/users/react-native-authentication.md

---
title: User Authentication
slug: docs/react-native/graphql/users/react-native-authentication
description: In this guide you will learn how to authenticate your React Native requests on Back4App using Relay.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-20T13:33:48.482Z
updatedAt: 2025-01-16T19:39:55.385Z
---

# React Native authentication using Relay

## Introduction

Using the GraphQL API, after signing up or logging a user in, you will receive a session token that you can use to retrieve the logged user at any time. The session token comes from a Relay Mutation. You will find those Relay Mutation examples on the previous guides of [**Sign Up**](https://www.back4app.com/docs/parse-graphql/graphql-sign-up) or [**Log In**](https://www.back4app.com/docs/parse-graphql/graphql-login).

The session token value represents the current session and controls if the user is authenticated or not. At the moment of authentication, this value needs to start to be on header params. On Relay, we use the Environment to handle the header params, so you should insert the session token inside this file.

After adding the session to the headers, each request will be authenticated by Back4App and, the user will access the private resources.

:::hint{type="success"}
**At any time, you can access this project via our GitHub repositories to checkout the styles and complete code.**

- [**JavaScript Example Repository**](https://github.com/templates-back4app/react-native-graphql-relay-js-users)
:::

## Goal

Authenticate the user requests on Back4App using the session token on header params.

## Prerequisites

- **An app created at Back4App using the Parse Server Version 3.10 or above.**
- **You have to conclude the&#x20;**[**Relay Environment setup tutorial**](https://www.back4app.com/docs/react-native/graphql/relay-setup)**:**
- **You have to conclude the&#x20;**[**React Native Login sample using Relay**](https://www.back4app.com/docs/react-native/graphql/users/react-native-login-sample)**:**
- **For this tutorial we are going to use the Expo as a React Native framework;**
- **For this tutorial we are going to use Javascript as our default implementation language;**
- **For this tutorial we are going to use Async Storage;**

## 1 - Install Async Storage

After conclude the tutorials [**Sign Up**](https://www.back4app.com/docs/parse-graphql/graphql-sign-up) or [**Log In**](https://www.back4app.com/docs/parse-graphql/graphql-login), your app will receive a session token. Let’s store the token using the Async Storage. Follow the official docs to install the Async Storage Lib on your App.

:::hint{type="success"}
You can use async storage, redux, or your preferred local storage solution. You only make sure that this value will be available in the Environment.
:::

## 2 - Retrieve the token

Let’s go ahead using the [**last guide code**](https://www.back4app.com/docs/parse-graphql/graphql-login). You’ll need to get the session token and persist this value in your application using Async Storage.

Start by changing the session token state management from useState hook to Async Storage. The first step is to create a function inside of the environment file to retrieve the session token from Async Storage.

Import the Async Storage:

```javascript
1    import AsyncStorage from '@react-native-async-storage/async-storage';
```

Now, create the function:

```javascript
1    export const getSessionToken = async () => {
2      const sessionToken = await AsyncStorage.getItem('sessionToken');
3      return sessionToken;
4    };
```

## 3 - Save the token on the Client-side

Let’s now improve the Sign In component to persist the session token instead of managing it using the useState hook. The component will now keep the logged-in state even when reloading the App because it has the session token persisted.

Open the Sign In component. Inside of the onCompleted from onSubmit, saving the session token on Async Storage getting the following result:

Then improve the onCompleted:

```javascript
1	onCompleted: async (response) => {
2	    if(!response?.logIn || response?.logIn === null) {
3	      alert('Error while logging');
4	      return;
5	    }
6	
7	    const { viewer } = response?.logIn;
8	    const { sessionToken, user } = viewer;
9	
10	    if (sessionToken !== null) {
11	      setUserLogged(user);
12	      alert(`user ${user.username} successfully logged`);
13	      await AsyncStorage.setItem('sessionToken', sessionToken);
14	      return;
15	    }
16	},
```

After, inside of the SignIn component declaration, create a new useState for the session token:

```javascript
1	const [sessionToken, setSessionToken] = useState(null);
```

Add a useEffect to be called every time that the component is mounted and check if has a session token (import thegetSessionTokenfrom environment file:

```javascript
1	useEffect(() => {
2	  (async () => {
3	    const sT = await getSessionToken();
4	    setSessionToken(sT);
5	  })();
6	}, []);
```

&#x20;By last, let’s change again the onCompleted for now handle the new useState, getting the new lines of code:

```javascript
1	onCompleted: async (response) => {
2	    if (!response?.logIn || response?.logIn === null) {
3	    alert('Error while logging');
4	    return;
5	    }
6	    
7	    const { viewer } = response?.logIn;
8	    const { sessionToken, user } = viewer;
9	    
10	    if (sessionToken !== null) {
11	       setSessionToken(sessionToken);
12	       await AsyncStorage.setItem('sessionToken', sessionToken);
13	       return;
14	  
15	    }
16	},
```

Remove the useState for user logged, the both lines below from respective places:

```javascript
1	const [userLogged, setUserLogged] = useState(null);
```

and

```javascript
1	setUserLogged(user);
```

We avoid the alert and start to set the info of the user and the token in a useState followed by the Async Storage saving the token.

Changes the if to handle now the session token.

```javascript
1	if (sessionToken) {
2	  return (
3	    <View>
4	      <Text>User logged</Text>
5	    </View>
6	  );
7	}
```

## 4 - Final result of SignIn component

After all changes, the SignIn component will be similar to the below.

```javascript
1	import React, {useEffect, useState} from 'react';
2	import LogInMutation from './mutations/LogInMutation';
3	import environment, { getSessionToken } from '../../relay/environment';
4	import {FormikProvider, useFormik} from 'formik';
5	import { Button, Text, TextInput, View, TouchableOpacity } from 'react-native';
6	import AsyncStorage from '@react-native-async-storage/async-storage';
7	
8	const SignIn = () => {
9	  const [sessionToken, setSessionToken] = useState(null);
10	
11	  useEffect(() => {
12	    (async () => {
13	      const sT = await getSessionToken();
14	      setSessionToken(sT);
15	    })();
16	  }, []);
17	
18	  const onSubmit = async (values) = {
19	    const { username, password } = values;
20	    const input = {
21	      username,
22	      password,
23	    };
24	
25	    LogInMutation.commit({
26	      environment,
27	      input,
28	      onCompleted: async (response) => {
29	        if (!response?.logIn || response?.logIn === null) {
30	          alert('Error while logging');
31	          return;
32	        }
33	
34	        const { viewer } = response?.logIn;
35	        const { sessionToken, user } = viewer;
36	
37	        if (sessionToken !== null) {
38	          setSessionToken(sessionToken);
39	          setUserLogged(user);
40	
41	          await AsyncStorage.setItem('sessionToken', sessionToken);
42	          return;
43	        }
44	      },
45	      onError: (errors) => {
46	        alert(errors[0].message);
47	      },
48	    });
49	  };
50	
51	  const formikbag = useFormik({
52	    initialValues: {
53	      username: '',
54	      password: '',
55	    },
56	    onSubmit,
57	  });
58	
59	 const { handleSubmit, setFieldValue } = formikbag;
60	
61	  if (sessionToken) {
62	    return (
63	      <View style={ {marginTop: 15, alignItems: 'center'} }>
64	        <Text>User logged</Text>
65	      </View>
66	    );
67	  }
68	
69	  return (
70	      <FormikProvider value={formikbag}>
71	          <View style={Styles.login_wrapper}>
72	              <View style={Styles.form}>
73	                  <Text>Username</Text>
74	                  <TextInput
75	                      name={"username"}
76	                      style={Styles.form_input}
77	                      autoCapitalize="none"
78	                      onChangeText={(text) => setFieldValue("username", text)}
79	                  />
80	                  <Text>Password</Text>
81	                  <TextInput
82	                      style={Styles.form_input}
83	                      name={"password"}
84	                      autoCapitalize="none"
85	                      secureTextEntry
86	                      onChangeText={(text) => setFieldValue("password", text)}
87	                  />
88	                  <TouchableOpacity onPress={() => handleSubmit()}>
89	                      <View style={Styles.button}>
90	                          <Text style={Styles.button_label}>{"Sign in"}</Text>
91	                      </View>
92	                  </TouchableOpacity>
93	              </View>
94	          </View>
95	      </FormikProvider>
96	  );
97	};
98	
99	export default SignIn;
```

## 5 - Testing

It’s time to test the new changes of Sign In component. To make sure there is no one user logged in, kill your application and open again.

:::hint{type="success"}
Remember also to clear the Async Storage. You can do it calling the AsyncStorage.clear() method and clear the actual state.
:::

Log in again and you will see the following message.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/FVeoyIrC2dFPWlcJEFgU0_image.png" signedSrc size="60" width="828" height="1792" position="center" caption}

## 6 - Set the Session token on Relay Environment

Now, let’s insert the session token on the application’s requests to Back4App GraphQL API. Inside of the Environment file, retrieve the sessionToken and add it to the headers object. You should pass the sessionToken on the variable X-Parse-Session-Token on the headers.
Here, we will reuse the getSessionToken function we already created.

Create a function before the fetchQuery function and paste the following code:

```javascript
1	export const getToken = async () => {
2	  const sessionToken = await getSessionToken();
3	
4	  if (sessionToken) {
5	    return {
6	      'X-Parse-Session-Token': sessionToken,
7	    };
8	  }
9	
10	  return {};
11	};
```

The function above retrieve the session token only if it exists. Now, add it to the headers object deconstructing it.

```javascript
1	const headers = {
2	  Accept: 'application/json',
3	  'Content-type': 'application/json',
4	  'X-Parse-Application-Id': 'YOUR_APP_ID_HERE',
5	  'X-Parse-Client-Key': 'YOUR_CLIENT_KEY_HERE',
6	  ...await getToken(),
7	};
```

Right below of headers, there is the try catch for make the request. Let’s set an if after the request that will handle when the http status of the request will be 401. This will mean that the actually token is not valid anymore. So, we will clear the storage and kill the current user:

```javascript
1	try {
2	    const response = await fetch(`https://parseapi.back4app.com/graphql`, {
3	        method: "POST",
4	        headers,
5	        body,
6	    });
7	
8	    const data = await response.json();
9	
10	    
11	    // this if will retrive the response when status code 401 and clear the session token
12	    if (response.status === 401) {
13	        await AsyncStorage.getItem("sessionToken");
14	        return;
15	    }
16	
17	    if (data.errors) {
18	        throw data.errors;
19	    }
20	
21	    return data;
22	} catch (err) {
23	    console.log("err on fetch graphql", err);
24	
25	    throw err;
26	}
```

Now, your application can start to retrieve private resources from the Back4App backend. And, if the session token does not exist, won’t break because we won’t pass it.

:::hint{type="success"}
Do not forget to configure the security mechanisms to guarantee the desired level of access for users. To better understand access the link [**security docs**](https://docs.parseplatform.org/js/guide/#security) from Parse.
:::

## Conclusion

In this guide, you have saved the session token using async storage and, now can start to retrieve resources that need a user logged.

In the next doc, let’s prepare a component that will retrieve the info about the user logged and stop using a useState to show it.

:::hint{type="success"}
For user SignUp you can follow the same approach of this tutorial to handle the session token
:::

