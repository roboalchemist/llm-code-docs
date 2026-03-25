# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/working-with-users/react-native-user-registration.md

---
title: User Registration
slug: docs/react-native/parse-sdk/working-with-users/react-native-user-registration
description: In this guide you'll learn how to register user in Parse on React Native
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T14:40:01.941Z
updatedAt: 2024-03-29T01:20:06.542Z
---

# User Registration for React Native

## Introduction

At the core of many apps, user accounts have a notion that lets users securely access their information. Parse provides a specialized user class called Parse.User that automatically handles much of the functionality required for user account management.

In this guide, you’ll learn how Parse.User class works by creating a user registration feature for your React Native App using Parse JS SDK.

::embed[]{url="https://www.youtube.com/embed/5cGCJGnRtVk"}

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- A React Native App created and [**connected to Back4App**](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk).
:::

## Goal

To build a User Registration feature using Parse for a React Native App.

## 1 - Understanding the SignUp method

Parse User management uses the Parse.User object type, which extends the default ParseObject type while containing unique helper methods, such as current and getUsername, that will help you retrieve user data throughout your app. You can read more about the Parse.User object [**here at the official documentation**](https://parseplatform.org/Parse-SDK-JS/api/2.18.0/Parse.User.html).

In this guide, you will learn how to use the signUp method that creates a new valid and unique Parse.User object both locally and on the server, taking as arguments valid username and password values.

## 2 - Create the user registration component

Let’s now build the functional component, which will call the signUp method in our App. First, create a new file in your root directory called UserRegistration.js (UserRegistration.tsx if you are using TypeScript) and also add the needed input elements (username and password inputs), using state hooks via useState to manage their data:

:::CodeblockTabs
UserRegistration.js

```javascript
1	import React, { FC, ReactElement, useState } from "react";
2	import { Button, StyleSheet, TextInput } from "react-native";
3	import Parse from "parse/react-native";
4	
5	export const UserRegistration = () => {
6	  const [username, setUsername] = useState("");
7	  const [password, setPassword] = useState("");
8	
9	  return (
10	    <>
11	      <TextInput
12	        style={styles.input}
13	        value={username}
14	        placeholder={"Username"}
15	        onChangeText={(text) => setUsername(text)}
16	        autoCapitalize={"none"}
17	      />
18	      <TextInput
19	        style={styles.input}
20	        value={password}
21	        placeholder={"Password"}
22	        secureTextEntry
23	        onChangeText={(text) => setPassword(text)}
24	      />
25	      <Button title={"Sign Up"} onPress={() => {}} />
26	    </>
27	  );
28	};
29	
30	const styles = StyleSheet.create({
31	  input: {
32	    height: 40,
33	    marginBottom: 10,
34	    backgroundColor: '#fff',
35	  },
36	});
```

UserRegistration.tsx

```typescript
1	import React, { FC, ReactElement, useState } from "react";
2	import { Button, StyleSheet, TextInput } from "react-native";
3	import Parse from "parse/react-native";
4	
5	export const UserRegistration: FC<{}> = ({}): ReactElement => {
6	  const [username, setUsername] = useState("");
7	  const [password, setPassword] = useState("");
8	
9	  return (
10	    <>
11	      <TextInput
12	        style={styles.input}
13	        value={username}
14	        placeholder={"Username"}
15	        onChangeText={(text) => setUsername(text)}
16	        autoCapitalize={"none"}
17	      />
18	      <TextInput
19	        style={styles.input}
20	        value={password}
21	        placeholder={"Password"}
22	        secureTextEntry
23	        onChangeText={(text) => setPassword(text)}
24	      />
25	      <Button title={"Sign Up"} onPress={() => {}} />
26	    </>
27	  );
28	};
29	
30	const styles = StyleSheet.create({
31	  input: {
32	    height: 40,
33	    marginBottom: 10,
34	    backgroundColor: '#fff',
35	  },
36	});
```
:::

## 3 - Create a Sign Up function

You can now create the sign-up function that will call the signUp method:

:::CodeblockTabs
JavaScript

```javascript
1	const doUserRegistration = async function () {
2	  // Note that these values come from state variables that we've declared before
3	  const usernameValue = username;
4	  const passwordValue = password;
5	  // Since the signUp method returns a Promise, we need to call it using await
6	  return await Parse.User.signUp(usernameValue, passwordValue)
7	    .then((createdUser) => {
8	      // Parse.User.signUp returns the already created ParseUser object if successful
9	      Alert.alert(
10	        'Success!',
11	        `User ${createdUser.getUsername()} was successfully created!`,
12	      );
13	      return true;
14	    })
15	    .catch((error) => {
16	      // signUp can fail if any parameter is blank or failed an uniqueness check on the server
17	      Alert.alert('Error!', error.message);
18	      return false;
19	    });
20	};
```

```typescript
1	const doUserRegistration = async function (): Promise<boolean> {
2	  // Note that these values come from state variables that we've declared before
3	  const usernameValue: string = username;
4	  const passwordValue: string = password;
5	  // Since the signUp method returns a Promise, we need to call it using await
6	  return await Parse.User.signUp(usernameValue, passwordValue)
7	    .then((createdUser: Parse.User) => {
8	      // Parse.User.signUp returns the already created ParseUser object if successful
9	      Alert.alert(
10	        'Success!',
11	        `User ${createdUser.getUsername()} was successfully created!`,
12	      );
13	      return true;
14	    })
15	    .catch((error: object) => {
16	      // signUp can fail if any parameter is blank or failed an uniqueness check on the server
17	      Alert.alert('Error!', error.message);
18	      return false;
19	    });
20	};
```
:::

:::hint{type="info"}
**Note:** Creating a new user using signUp also makes it the currently logged-in user, so there is no need for your user to log in again to continue using your App.
:::

Insert this function inside the UserRegistration component, just before the return call, to be called and tested. Remember to update the form’s sign up button onPress action to () => doUserRegistration() and to import Alert from react-native. Your component should now look like this:

:::CodeblockTabs
UserRegistration.js

```javascript
1	import React, { FC, ReactElement, useState } from "react";
2	import { Alert, Button, StyleSheet, TextInput } from "react-native";
3	import Parse from "parse/react-native";
4	
5	export const UserRegistration = () => {
6	  const [username, setUsername] = useState("");
7	  const [password, setPassword] = useState("");
8	
9	  const doUserRegistration = async function () {
10	    // Note that these values come from state variables that we've declared before
11	    const usernameValue = username;
12	    const passwordValue = password;
13	    // Since the signUp method returns a Promise, we need to call it using await
14	    return await Parse.User.signUp(usernameValue, passwordValue)
15	      .then((createdUser) => {
16	        // Parse.User.signUp returns the already created ParseUser object if successful
17	        Alert.alert(
18	          "Success!",
19	          `User ${createdUser.get("username")} was successfully created!`
20	        );
21	        return true;
22	      })
23	      .catch((error) => {
24	        // signUp can fail if any parameter is blank or failed an uniqueness check on the server
25	        Alert.alert("Error!", error.message);
26	        return false;
27	      });
28	  };
29	
30	  return (
31	    <>
32	      <TextInput
33	        style={styles.input}
34	        value={username}
35	        placeholder={"Username"}
36	        onChangeText={(text) => setUsername(text)}
37	        autoCapitalize={"none"}
38	      />
39	      <TextInput
40	        style={styles.input}
41	        value={password}
42	        placeholder={"Password"}
43	        secureTextEntry
44	        onChangeText={(text) => setPassword(text)}
45	      />
46	      <Button title={"Sign Up"} onPress={() => doUserRegistration()} />
47	    </>
48	  );
49	};
50	
51	const styles = StyleSheet.create({
52	  input: {
53	    height: 40,
54	    marginBottom: 10,
55	    backgroundColor: "#fff",
56	  },
57	});
```

UserRegistration.tsx

```typescript
1	import React, { FC, ReactElement, useState } from "react";
2	import { Alert, Button, StyleSheet, TextInput } from "react-native";
3	import Parse from "parse/react-native";
4	
5	export const UserRegistration: FC<{}> = ({}): ReactElement => {
6	  const [username, setUsername] = useState("");
7	  const [password, setPassword] = useState("");
8	
9	  const doUserRegistration = async function (): Promise<boolean> {
10	    // Note that these values come from state variables that we've declared before
11	    const usernameValue: string = username;
12	    const passwordValue: string = password;
13	    // Since the signUp method returns a Promise, we need to call it using await
14	    return await Parse.User.signUp(usernameValue, passwordValue)
15	      .then((createdUser: Parse.User) => {
16	        // Parse.User.signUp returns the already created ParseUser object if successful
17	        Alert.alert(
18	          "Success!",
19	          `User ${createdUser.get("username")} was successfully created!`
20	        );
21	        return true;
22	      })
23	      .catch((error: object) => {
24	        // signUp can fail if any parameter is blank or failed an uniqueness check on the server
25	        Alert.alert("Error!", error.message);
26	        return false;
27	      });
28	  };
29	
30	  return (
31	    <>
32	      <TextInput
33	        style={styles.input}
34	        value={username}
35	        placeholder={"Username"}
36	        onChangeText={(text) => setUsername(text)}
37	        autoCapitalize={"none"}
38	      />
39	      <TextInput
40	        style={styles.input}
41	        value={password}
42	        placeholder={"Password"}
43	        secureTextEntry
44	        onChangeText={(text) => setPassword(text)}
45	      />
46	      <Button title={"Sign Up"} onPress={() => doUserRegistration()} />
47	    </>
48	  );
49	};
50	
51	const styles = StyleSheet.create({
52	  input: {
53	    height: 40,
54	    marginBottom: 10,
55	    backgroundColor: "#fff",
56	  },
57	});
```
:::

## 4 - Testing the component

The final step is to use our new component inside your React Native Application App.js file (or App.tsx if using TypeScript):

:::CodeblockTabs
App.js

```javascript
1	import { UserRegistration } from "./UserRegistration";
2	/*
3	Your functions here
4	*/
5	return (
6	  <>
7	    <StatusBar />
8	    <SafeAreaView style={styles.container}>
9	      <>
10	        <Text style={styles.title}>React Native on Back4App</Text>
11	        <Text>User registration tutorial</Text>
12	        <UserRegistration />
13	      </>
14	    </SafeAreaView>
15	  </>
16	);
17	
18	// Remember to add some styles at the end of your file
19	const styles = StyleSheet.create({
20	  container: {
21	    flex: 1,
22	    backgroundColor: "#fff",
23	    alignItems: "center",
24	    justifyContent: "center",
25	  },
26	  title: {
27	    fontSize: 20,
28	    fontWeight: "bold",
29	  },
30	});
```

App.tsx

```typescript
1	import { UserRegistration } from "./UserRegistration";
2	/*
3	Your functions here
4	*/
5	return (
6	  <>
7	    <StatusBar />
8	    <SafeAreaView style={styles.container}>
9	      <>
10	        <Text style={styles.title}>React Native on Back4App</Text>
11	        <Text>User registration tutorial</Text>
12	        <UserRegistration />
13	      </>
14	    </SafeAreaView>
15	  </>
16	);
17	
18	// Remember to add some styles at the end of your file
19	const styles = StyleSheet.create({
20	  container: {
21	    flex: 1,
22	    backgroundColor: "#fff",
23	    alignItems: "center",
24	    justifyContent: "center",
25	  },
26	  title: {
27	    fontSize: 20,
28	    fontWeight: "bold",
29	  },
30	});
```
:::

Your app now should look like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/iPbehNRY59rROxZSszBfD_image.png" signedSrc size="50" width="358" height="750" position="center" caption}

After providing the desired user credentials, you will see this message after pressing on Sign Up if everything was successful:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/_xSJ2aMIPg4gOxCkazhNF_image.png" signedSrc size="50" width="363" height="751" position="center" caption}

Error handling can be tested if you try to register a user with the same username as before:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/EpTs9m2bvVYMFgJ0PZ9Zw_image.png" signedSrc size="50" width="368" height="751" position="center" caption}

You will get another error if you try to sign up with no password:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ZIv5M1Rf7GFMUZYPfVvKA_image.png" signedSrc size="50" width="370" height="750" position="center" caption}

## Conclusion

At the end of this guide, you learned how to register new Parse users on React Native. In the next guide, we will show you how to log in and out users.
