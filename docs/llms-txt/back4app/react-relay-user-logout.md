# Source: https://docs-containers.back4app.com/docs/react-native/graphql/users/react-relay-user-logout.md

---
title: User Logout
slug: docs/react-native/graphql/users/react-relay-user-logout
description: In this guide you will learn how to logout the user closing the actual session
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-20T13:50:47.868Z
updatedAt: 2025-01-16T19:41:24.636Z
---

# React Native User Logout

## Introduction

In this step you will create the user Logout for React Native using Relay, the last implementation for this User’s section. This step is simple and we will follow our [**GraphQL Logout Guide**](https://www.back4app.com/docs/parse-graphql/graphql-logout-mutation) from our GraphQL Cookbook. You will implement the Logout mutation and call it using a button into the React Native Application.

:::hint{type="success"}
**At any time, you can access this project via our GitHub repositories to checkout the styles and complete code.**

- [**JavaScript Example Repository**](https://github.com/templates-back4app/react-native-graphql-relay-js-users)
:::

## Goal

To implement the Logout feature to our React Native App using Relay and the Back4App GraphQL API.

## Prerequisites

- For this tutorial we will use the Parse Server in the 4.4 version. If you want to use other versions you can check the corresponding mutation code at [**GraphQL Logout Guide**](https://www.back4app.com/docs/parse-graphql/graphql-logout-mutation) example for your respective version.
- You have to conclude the [**Relay Environment setup tutorial**](https://www.back4app.com/docs/react-native/graphql/relay-setup):
- You have to conclude the [**React Native Login sample using Relay**](https://www.back4app.com/docs/react-native/graphql/users/react-native-login-sample):
- You have to conclude the [**React Native User Logged**](https://app.archbee.com/docs/_roxIyUMXoBue9I7uv49e/6qyoyUmFLdRtjjy7dcgnr):
- For this tutorial, we are going to use the Expo as a React Native framework;
- For this tutorial, we are going to use Javascript as our default implementation language;

## 1 - Creating the Logout Mutation

Back again to the SignIn folder, into mutations folder create a new file and call it LogOutMutation.js.

Copy and paste the following code inside:

```javascript
1	import { commitMutation, graphql } from 'react-relay';
2	
3	const mutation = graphql`
4	  mutation LogOutMutation($input: LogOutInput!) {
5	    logOut(input: $input) {
6	      clientMutationId
7	    }
8	  }
9	`;
10	
11	function commit({ environment, input, onCompleted, onError }) {
12	    const variables = { input };
13	
14	    commitMutation(environment, {
15	        mutation,
16	        variables,
17	        onCompleted,
18	        onError,
19	    });
20	}
21	
22	export default {
23	    commit,
24	};
```

Run yarn relay into your terminal to update the relay types:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/SAkFpoBSkoDk028w_ShEl_image.png" signedSrc size="70" width="632" height="252" position="center" caption}

## 2 - Creating logout button

Now, open the FormSignIn.js component. Let’s add the Logout Button and call the Relay Mutation.

Import the new Relay Mutation on begin of file:

```javascript
1	import LogOutMutation from "./mutations/LogOutMutation";
```

Then, create the function responsible to call the LogOut Mutation:

```javascript
1	const handleLogout = async () => {
2	  LogOutMutation.commit({
3	    environment: environment,
4	    input: {},
5	    onCompleted: async () => {
6	      await AsyncStorage.removeItem('sessionToken');
7	      setSessionToken(null);
8	      alert('User successfully logged out');
9	    },
10	    onError: (errors) => {
11	      alert(errors[0].message);
12	    },
13	  });
14	};
```

What is happening into onCompleted:

- **it is removing the session token from Async Storage because it is not valid anymore.**
- **is cleaning the local useState that retrieves the session token for the same reason above.**
- **an alert saying the user it was logged out with success.**

After, right below the UserLoggedRenderer, let’s implement the button responsible to call the logout:

From:

```javascript
1   if (sessionToken) {
2     return <UserLoggedRenderer />;
3   }
```

To

```javascript
1	if (sessionToken) {
2	  return (
3	    <>
4	      <UserLoggedRenderer />
5	      <Button title={'logout'} onPress={() => handleLogout()} />
6	    </>
7	  )
8	}
```

:::hint{type="success"}
Import the Button from react-native lib import \{ Button, Text, TextInput, View, TouchableOpacity } from "react-native";
:::

The application screen should look like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/vb1yq78Wc2fDQjeNNThKX_image.png" signedSrc size="60" width="828" height="1792" position="center" caption}

## 3 - Testing

Testing the button, when click should be made the logout and appears an alert:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/5wX6DxsRc_vJF2_WfNbDL_image.png" signedSrc size="60" width="828" height="1792" position="center" caption}

And, after should return to Login page:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/UIlqzlmwpXlZpTXyEWXfQ_image.png" signedSrc size="60" width="828" height="1792" position="center" caption}

## Conclusion

Now you’ve implemented the main user authentication features necessary to any App. Your users can now SignUp, Login, navigate on authenticated area and LogOut from your React Native App using Relay and Back4App GraphQL API.
