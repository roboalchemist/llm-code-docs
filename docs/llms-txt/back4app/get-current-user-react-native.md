# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/working-with-users/get-current-user-react-native.md

---
title: Current User
slug: docs/react-native/parse-sdk/working-with-users/get-current-user-react-native
description: In this guide you'll learn how to fetch the current user in Parse on React Native
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T15:41:52.736Z
updatedAt: 2024-03-21T19:06:30.702Z
---

# Get current User for React Native

## Introduction

After implementing user registration and login to your, you need to retrieve the currently logged user data to perform different actions and requests. Since React Native uses AsyncStorage as the local storage, this data can be retrieved using Parse.currentAsync inside your app’s component.

::embed[]{url="https://www.youtube.com/embed/Iy_6bCh_ecg"}

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- A React Native App created and [**connected to Back4App**](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk).
- Complete the previous guides so you can have a better understanding of [**the Parse User class**](https://www.back4app.com/docs/react-native/parse-sdk/working-with-users/react-native-login).
:::

## Goal

Get the current user data fetching using Parse for a React Native App.

## 1 - Retrieving Current User

The method Parse.currentAsync can be used anywhere on your code, after properly configuring your app to use Parse and AsyncStorage. Its response will be your current user’s object (Parse.User) or null if there is no logged-in user currently.

:::CodeblockTabs
JavaScript

```javascript
1	const getCurrentUser = async function () {
2	  const currentUser = await Parse.User.currentAsync();
3	  if (currentUser !== null) {
4	    Alert.alert(
5	      'Success!',
6	      `${currentUser.get('username')} is the current user!`,
7	    );
8	  }
9	  return currentUser;
10	};
```

```typescript
1	const getCurrentUser = async function (): Promise<Parse.User> {
2	  const currentUser: Parse.User = await Parse.User.currentAsync();
3	  if (currentUser !== null) {
4	    Alert.alert(
5	      'Success!',
6	      `${currentUser.get('username')} is the current user!`,
7	    );
8	  }
9	  return currentUser;
10	};
```
:::

This method is essential in situations where you don’t have access to your application state or your user data, making it possible to perform relevant Parse requests in any component of your app.

## 2 - Using Current User in a React Native component

In our previous guides, Parse.currentAsync was already used for testing and inside the HelloUser component. Here is the complete component again:

:::CodeblockTabs
HelloUser.js

```javascript
1	import React, {FC, ReactElement, useEffect, useState} from 'react';
2	import {Text, View} from 'react-native';
3	import Parse from 'parse/react-native';
4	import Styles from './Styles';
5	
6	export const HelloUser = () => {
7	  // State variable that will hold username value
8	  const [username, setUsername] = useState('');
9	
10	  // useEffect is called after the component is initially rendered and
11	  // after every other render
12	  useEffect(() => {
13	    // Since the async method Parse.User.currentAsync is needed to
14	    // retrieve the current user data, you need to declare an async
15	    // function here and call it afterwards
16	    async function getCurrentUser() {
17	      // This condition ensures that username is updated only if needed
18	      if (username === '') {
19	        const currentUser = await Parse.User.currentAsync();
20	        if (currentUser !== null) {
21	          setUsername(currentUser.getUsername());
22	        }
23	      }
24	    }
25	    getCurrentUser();
26	  }, [username]);
27	
28	  // Note the conditional operator here, so the "Hello" text is only
29	  // rendered if there is an username value
30	  return (
31	    <View style={Styles.login_wrapper}>
32	      <View style={Styles.form}>
33	        {username !== '' && <Text>{`Hello ${username}!`}</Text>}
34	      </View>
35	    </View>
36	  );
37	};
```

HelloUser.tsx

```typescript
1	import React, {FC, ReactElement, useEffect, useState} from 'react';
2	import {Text, View} from 'react-native';
3	import Parse from 'parse/react-native';
4	import Styles from './Styles';
5	
6	export const HelloUser: FC<{}> = ({}): ReactElement => {
7	  // State variable that will hold username value
8	  const [username, setUsername] = useState('');
9	
10	  // useEffect is called after the component is initially rendered and
11	  // after every other render
12	  useEffect(() => {
13	    // Since the async method Parse.User.currentAsync is needed to
14	    // retrieve the current user data, you need to declare an async
15	    // function here and call it afterwards
16	    async function getCurrentUser() {
17	      // This condition ensures that username is updated only if needed
18	      if (username === '') {
19	        const currentUser = await Parse.User.currentAsync();
20	        if (currentUser !== null) {
21	          setUsername(currentUser.getUsername());
22	        }
23	      }
24	    }
25	    getCurrentUser();
26	  }, [username]);
27	
28	  // Note the conditional operator here, so the "Hello" text is only
29	  // rendered if there is an username value
30	  return (
31	    <View style={Styles.login_wrapper}>
32	      <View style={Styles.form}>
33	        {username !== '' && <Text>{`Hello ${username}!`}</Text>}
34	      </View>
35	    </View>
36	  );
37	};
```
:::

In this case, the Parse.currentAsync method retrieves the username and updates the state variable that is rendered inside the component JSX.

## Conclusion

At the end of this guide, you learned how to retrieve the current Parse user data from local storage on React Native. In the next guide, we will show you how to allow your user to reset his password.
