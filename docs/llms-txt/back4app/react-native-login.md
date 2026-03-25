# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/working-with-users/react-native-login.md

---
title: User LogIn
slug: docs/react-native/parse-sdk/working-with-users/react-native-login
description: In this guide you'll learn how to login and logout a user in Parse on React Native
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T14:57:26.605Z
updatedAt: 2024-03-29T01:22:50.239Z
---

# User LogIn and LogOut for React Native

## Introduction

After implementing a component that handles User Registration in Parse in the last guide, you will now learn how to log in and log out users using the same Parse.User class. You will also learn to install and configure react-navigation so you can navigate the user through your new screens and components.
The Parse.User.logIn method stores in your local storage a valid user session, so future calls to methods like currentAsync will successfully retrieve your User data. On the other hand, logOut will clear this session from disk and log out of any linked services in your Parse server.

::embed[]{url="https://www.youtube.com/embed/NKhzloPrIQw"}

:::hint{type="success"}
At any time, you can access the complete Android Project built with this tutorial at our Github repositories

- [**Kotlin Example Repository**](https://github.com/templates-back4app/Android-Parse-Sdk-Kotlin)
- [**Java Example Repository**](https://github.com/templates-back4app/Android-Parse-Sdk-Java)
:::

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- A React Native App created and [**connected to Back4App**](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk).
- Complete the previous guides so you can have a better understanding of [**the Parse User class**](https://www.back4app.com/docs/react-native/parse-sdk/working-with-users/react-native-login).
:::

## Goal

To build a User LogIn and LogOut feature using Parse for a React Native App.

## 1 - Installing dependencies

At some point, every application in React Native will need screen navigation. You will now learn how to install and configure the most used library in React Native for this, react-navigation.

Go to your project root directory and install the following dependencies:

:::BlockQuote
cd yourApp

yarn add @react-navigation/native react-native-reanimated react-native-gesture-handler react-native-screens react-native-safe-area-context @react-native-community/masked-view
:::

If you are developing for iOS, you need to install the pods to complete your app auto-linking:

:::BlockQuote
cd ios

npx pod-install
:::

:::hint{type="info"}
**Note:** Linking is automatic for React native 0.60+ to all platforms, so if you are still using an older version of RN, take a look at React Native docs [**here**](https://reactnative.dev/docs/linking-libraries-ios).&#x20;
:::

In your app entry file (App.tsx or App.js), add this import line at the very top of the file. Now you need to move your components inside the react-navigation container, which will encapsulate your app inside a NavigationContainer:

:::CodeblockTabs
App.tsx/App.js

```typescript
1	import "react-native-gesture-handler";
2	// Your other imports go here
3	import { NavigationContainer } from "@react-navigation/native";
4	
5	const App = () => {
6	  return <NavigationContainer>{/* Your app code */}</NavigationContainer>;
7	}
8	
9	export default App;
```
:::

The core navigation library has different additional navigation modules like a stack, tabs, drawer, others. Stack navigator is the most straightforward one and the one that you will use in this guide. Proceed with the installation:

:::BlockQuote
\# This is the navigator that you will use
yarn add @react-navigation/stack
:::

## 2 - Creating a StackNavigator

Let’s now create and set up a StackNavigator. This module will manage and handle screen navigation on your app. Since it’s not a goal here to give you a react-navigation deep understanding, please go to the [**official docs**](https://reactnavigation.org/docs/hello-react-navigation/) to know more.

In your App.js (App.tsx if you are using TypeScript) file, import and create a StackNavigator, create a function containing your user registration screen and insert the navigator inside your app NavigationContainer. Your main file should look like this:

:::CodeblockTabs
App.tsx/App.js

```typescript
1	import 'react-native-gesture-handler';
2	import React from 'react';
3	import {Image, SafeAreaView, StatusBar, Text, View} from 'react-native';
4	
5	import AsyncStorage from '@react-native-async-storage/async-storage';
6	import Parse from 'parse/react-native';
7	import {NavigationContainer} from '@react-navigation/native';
8	import {createStackNavigator} from '@react-navigation/stack';
9	import {UserRegistration} from './UserRegistration';
10	import Styles from './Styles';
11	
12	// Your Parse initialization configuration goes here
13	Parse.setAsyncStorage(AsyncStorage);
14	const PARSE_APPLICATION_ID: string = 'APPLICATION_ID';
15	const PARSE_HOST_URL: string = 'HOST_URL';
16	const PARSE_JAVASCRIPT_ID: string = 'JAVASCRIPT_ID';
17	Parse.initialize(PARSE_APPLICATION_ID, PARSE_JAVASCRIPT_ID);
18	Parse.serverURL = PARSE_HOST_URL;
19	
20	// Wrap your old app screen in a separate function, so you can create a screen
21	// inside the navigator; you can also declare your screens in a separate file, 
22	// export and import here to reduce some clutter
23	function UserRegistrationScreen() {
24	  return (
25	    <>
26	      <StatusBar />
27	      <SafeAreaView style={Styles.login_container}>
28	        <View style={Styles.login_header}>
29	          <Image
30	            style={Styles.login_header_logo}
31	            source={require('./assets/logo-back4app.png')}
32	          />
33	          <Text style={Styles.login_header_text}>
34	            <Text style={Styles.login_header_text_bold}>
35	              {'React Native on Back4App - '}
36	            </Text>
37	            {' User registration'}
38	          </Text>
39	        </View>
40	        <UserRegistration />
41	      </SafeAreaView>
42	    </>
43	  );
44	}
45	
46	// Create your main navigator here
47	const Stack = createStackNavigator();
48	
49	// Add the stack navigator to your NavigationContainer
50	// and in it you can add all your app screens in the order you need
51	// them on your stack
52	const App = () => {
53	  return (
54	    <NavigationContainer>
55	      <Stack.Navigator>
56	        <Stack.Screen name="Sign Up" component={UserRegistrationScreen} />
57	      </Stack.Navigator>
58	    </NavigationContainer>
59	  );
60	};
61	
62	export default App;
```
:::

If you run your app now, you will notice the inclusion of a header at the top of the screen containing your screen name:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Axy6jQGtw5aTsMPqRiOAG_image.png" signedSrc size="50" width="358" height="732" position="center" caption}

## 3 - Creating a login component

Let’s now build the UserLogIn functional component in your App. Create a new file in your root directory called UserLogIn.js (UserLogIn.tsx if you are using TypeScript) and add the input elements using state hooks to manage their data:

:::CodeblockTabs
UserLogIn.js

```javascript
1	import React, {FC, ReactElement, useState} from 'react';
2	import {
3	  Image,
4	  Text,
5	  TextInput,
6	  TouchableOpacity,
7	  View,
8	} from 'react-native';
9	import Parse from 'parse/react-native';
10	import Styles from './Styles';
11	
12	export const UserLogIn = () => {
13	  const [username, setUsername] = useState("");
14	  const [password, setPassword] = useState("");
15	
16	  return (
17	    <View style={Styles.login_wrapper}>
18	      <View style={Styles.form}>
19	        <TextInput
20	          style={Styles.form_input}
21	          value={username}
22	          placeholder={'Username'}
23	          onChangeText={(text) => setUsername(text)}
24	          autoCapitalize={'none'}
25	          keyboardType={'email-address'}
26	        />
27	        <TextInput
28	          style={Styles.form_input}
29	          value={password}
30	          placeholder={'Password'}
31	          secureTextEntry
32	          onChangeText={(text) => setPassword(text)}
33	        />
34	        <TouchableOpacity onPress={() => {}}>
35	          <View style={Styles.button}>
36	            <Text style={Styles.button_label}>{'Sign in'}</Text>
37	          </View>
38	        </TouchableOpacity>
39	      </View>
40	      <View style={Styles.login_social}>
41	        <View style={Styles.login_social_separator}>
42	          <View style={Styles.login_social_separator_line} />
43	          <Text style={Styles.login_social_separator_text}>{'or'}</Text>
44	          <View style={Styles.login_social_separator_line} />
45	        </View>
46	        <View style={Styles.login_social_buttons}>
47	          <TouchableOpacity>
48	            <View
49	              style={[
50	                Styles.login_social_button,
51	                Styles.login_social_facebook,
52	              ]}>
53	              <Image
54	                style={Styles.login_social_icon}
55	                source={require('./assets/icon-facebook.png')}
56	              />
57	            </View>
58	          </TouchableOpacity>
59	          <TouchableOpacity>
60	            <View style={Styles.login_social_button}>
61	              <Image
62	                style={Styles.login_social_icon}
63	                source={require('./assets/icon-google.png')}
64	              />
65	            </View>
66	          </TouchableOpacity>
67	          <TouchableOpacity>
68	            <View style={Styles.login_social_button}>
69	              <Image
70	                style={Styles.login_social_icon}
71	                source={require('./assets/icon-apple.png')}
72	              />
73	            </View>
74	          </TouchableOpacity>
75	        </View>
76	      </View>
77	    </View>
78	  );
79	};
```

UserLogIn.tsx

```typescript
1	import React, {FC, ReactElement, useState} from 'react';
2	import {
3	  Image,
4	  Text,
5	  TextInput,
6	  TouchableOpacity,
7	  View,
8	} from 'react-native';
9	import Parse from 'parse/react-native';
10	import Styles from './Styles';
11	
12	export const UserLogIn: FC<{}> = ({}): ReactElement => {
13	  const [username, setUsername] = useState("");
14	  const [password, setPassword] = useState("");
15	
16	  return (
17	    <View style={Styles.login_wrapper}>
18	      <View style={Styles.form}>
19	        <TextInput
20	          style={Styles.form_input}
21	          value={username}
22	          placeholder={'Username'}
23	          onChangeText={(text) => setUsername(text)}
24	          autoCapitalize={'none'}
25	          keyboardType={'email-address'}
26	        />
27	        <TextInput
28	          style={Styles.form_input}
29	          value={password}
30	          placeholder={'Password'}
31	          secureTextEntry
32	          onChangeText={(text) => setPassword(text)}
33	        />
34	        <TouchableOpacity onPress={() => {}}>
35	          <View style={Styles.button}>
36	            <Text style={Styles.button_label}>{'Sign in'}</Text>
37	          </View>
38	        </TouchableOpacity>
39	      </View>
40	      <View style={Styles.login_social}>
41	        <View style={Styles.login_social_separator}>
42	          <View style={Styles.login_social_separator_line} />
43	          <Text style={Styles.login_social_separator_text}>{'or'}</Text>
44	          <View style={Styles.login_social_separator_line} />
45	        </View>
46	        <View style={Styles.login_social_buttons}>
47	          <TouchableOpacity>
48	            <View
49	              style={[
50	                Styles.login_social_button,
51	                Styles.login_social_facebook,
52	              ]}>
53	              <Image
54	                style={Styles.login_social_icon}
55	                source={require('./assets/icon-facebook.png')}
56	              />
57	            </View>
58	          </TouchableOpacity>
59	          <TouchableOpacity>
60	            <View style={Styles.login_social_button}>
61	              <Image
62	                style={Styles.login_social_icon}
63	                source={require('./assets/icon-google.png')}
64	              />
65	            </View>
66	          </TouchableOpacity>
67	          <TouchableOpacity>
68	            <View style={Styles.login_social_button}>
69	              <Image
70	                style={Styles.login_social_icon}
71	                source={require('./assets/icon-apple.png')}
72	              />
73	            </View>
74	          </TouchableOpacity>
75	        </View>
76	      </View>
77	    </View>
78	  );
79	};
```
:::

You can now implement the function that will call theParse.User.logInmethod, using state variables:

:::CodeblockTabs
JavaScript

```javascript
1	const doUserLogIn = async function () {
2	  // Note that these values come from state variables that we've declared before
3	  const usernameValue = username;
4	  const passwordValue = password;
5	  return await Parse.User.logIn(usernameValue, passwordValue)
6	    .then(async (loggedInUser) => {
7	      // logIn returns the corresponding ParseUser object
8	      Alert.alert(
9	        'Success!',
10	        `User ${loggedInUser.get('username')} has successfully signed in!`,
11	      );
12	      // To verify that this is in fact the current user, currentAsync can be used
13	      const currentUser = await Parse.User.currentAsync();
14	      console.log(loggedInUser === currentUser);
15	      return true;
16	    })
17	    .catch((error) => {
18	      // Error can be caused by wrong parameters or lack of Internet connection
19	      Alert.alert('Error!', error.message);
20	      return false;
21	    });
22	};
```

```typescript
1	const doUserLogIn = async function (): Promise<boolean> {
2	  // Note that these values come from state variables that we've declared before
3	  const usernameValue: string = username;
4	  const passwordValue: string = password;
5	  return await Parse.User.logIn(usernameValue, passwordValue)
6	    .then(async (loggedInUser: Parse.User) => {
7	      // logIn returns the corresponding ParseUser object
8	      Alert.alert(
9	        'Success!',
10	        `User ${loggedInUser.get('username')} has successfully signed in!`,
11	      );
12	      // To verify that this is in fact the current user, currentAsync can be used
13	      const currentUser: Parse.User = await Parse.User.currentAsync();
14	      console.log(loggedInUser === currentUser);
15	      return true;
16	    })
17	    .catch((error: object) => {
18	      // Error can be caused by wrong parameters or lack of Internet connection
19	      Alert.alert('Error!', error.message);
20	      return false;
21	    });
22	};
```
:::

Insert this function inside the UserLogIn component, just before the return call, to be called and tested. Remember to update the form’s login button onPress action to () => doUserLogIn() and to import Alert from react-native. Your component should now look like this:

:::CodeblockTabs
UserLogIn.js

```javascript
1	import React, {FC, ReactElement, useState} from 'react';
2	import {
3	  Alert,
4	  Image,
5	  Text,
6	  TextInput,
7	  TouchableOpacity,
8	  View,
9	} from 'react-native';
10	import Parse from 'parse/react-native';
11	import Styles from './Styles';
12	
13	export const UserLogIn = () => {
14	  const [username, setUsername] = useState('');
15	  const [password, setPassword] = useState('');
16	
17	  const doUserLogIn = async function () {
18	    // Note that these values come from state variables that we've declared before
19	    const usernameValue = username;
20	    const passwordValue = password;
21	    return await Parse.User.logIn(usernameValue, passwordValue)
22	      .then(async (loggedInUser) => {
23	        // logIn returns the corresponding ParseUser object
24	        Alert.alert(
25	          'Success!',
26	          `User ${loggedInUser.get('username')} has successfully signed in!`,
27	        );
28	        // To verify that this is in fact the current user, currentAsync can be used
29	        const currentUser = await Parse.User.currentAsync();
30	        console.log(loggedInUser === currentUser);
31	        return true;
32	      })
33	      .catch((error) => {
34	        // Error can be caused by wrong parameters or lack of Internet connection
35	        Alert.alert('Error!', error.message);
36	        return false;
37	      });
38	  };
39	
40	  return (
41	    <View style={Styles.login_wrapper}>
42	      <View style={Styles.form}>
43	        <TextInput
44	          style={Styles.form_input}
45	          value={username}
46	          placeholder={'Username'}
47	          onChangeText={(text) => setUsername(text)}
48	          autoCapitalize={'none'}
49	          keyboardType={'email-address'}
50	        />
51	        <TextInput
52	          style={Styles.form_input}
53	          value={password}
54	          placeholder={'Password'}
55	          secureTextEntry
56	          onChangeText={(text) => setPassword(text)}
57	        />
58	        <TouchableOpacity onPress={() => doUserLogIn()}>
59	          <View style={Styles.button}>
60	            <Text style={Styles.button_label}>{'Sign in'}</Text>
61	          </View>
62	        </TouchableOpacity>
63	      </View>
64	      <View style={Styles.login_social}>
65	        <View style={Styles.login_social_separator}>
66	          <View style={Styles.login_social_separator_line} />
67	          <Text style={Styles.login_social_separator_text}>{'or'}</Text>
68	          <View style={Styles.login_social_separator_line} />
69	        </View>
70	        <View style={Styles.login_social_buttons}>
71	          <TouchableOpacity>
72	            <View
73	              style={[
74	                Styles.login_social_button,
75	                Styles.login_social_facebook,
76	              ]}>
77	              <Image
78	                style={Styles.login_social_icon}
79	                source={require('./assets/icon-facebook.png')}
80	              />
81	            </View>
82	          </TouchableOpacity>
83	          <TouchableOpacity>
84	            <View style={Styles.login_social_button}>
85	              <Image
86	                style={Styles.login_social_icon}
87	                source={require('./assets/icon-google.png')}
88	              />
89	            </View>
90	          </TouchableOpacity>
91	          <TouchableOpacity>
92	            <View style={Styles.login_social_button}>
93	              <Image
94	                style={Styles.login_social_icon}
95	                source={require('./assets/icon-apple.png')}
96	              />
97	            </View>
98	          </TouchableOpacity>
99	        </View>
100	      </View>
101	    </View>
102	  );
103	};
```

UserLogIn.tsx

```typescript
1	import React, {FC, ReactElement, useState} from 'react';
2	import {
3	  Alert,
4	  Image,
5	  Text,
6	  TextInput,
7	  TouchableOpacity,
8	  View,
9	} from 'react-native';
10	import Parse from 'parse/react-native';
11	import Styles from './Styles';
12	
13	export const UserLogIn: FC<{}> = ({}): ReactElement => {
14	  const [username, setUsername] = useState('');
15	  const [password, setPassword] = useState('');
16	
17	  const doUserLogIn = async function (): Promise<boolean> {
18	    // Note that these values come from state variables that we've declared before
19	    const usernameValue: string = username;
20	    const passwordValue: string = password;
21	    return await Parse.User.logIn(usernameValue, passwordValue)
22	      .then(async (loggedInUser: Parse.User) => {
23	        // logIn returns the corresponding ParseUser object
24	        Alert.alert(
25	          'Success!',
26	          `User ${loggedInUser.get('username')} has successfully signed in!`,
27	        );
28	        // To verify that this is in fact the current user, currentAsync can be used
29	        const currentUser: Parse.User = await Parse.User.currentAsync();
30	        console.log(loggedInUser === currentUser);
31	        return true;
32	      })
33	      .catch((error: object) => {
34	        // Error can be caused by wrong parameters or lack of Internet connection
35	        Alert.alert('Error!', error.message);
36	        return false;
37	      });
38	  };
39	
40	  return (
41	    <View style={Styles.login_wrapper}>
42	      <View style={Styles.form}>
43	        <TextInput
44	          style={Styles.form_input}
45	          value={username}
46	          placeholder={'Username'}
47	          onChangeText={(text) => setUsername(text)}
48	          autoCapitalize={'none'}
49	          keyboardType={'email-address'}
50	        />
51	        <TextInput
52	          style={Styles.form_input}
53	          value={password}
54	          placeholder={'Password'}
55	          secureTextEntry
56	          onChangeText={(text) => setPassword(text)}
57	        />
58	        <TouchableOpacity onPress={() => doUserLogIn()}>
59	          <View style={Styles.button}>
60	            <Text style={Styles.button_label}>{'Sign in'}</Text>
61	          </View>
62	        </TouchableOpacity>
63	      </View>
64	      <View style={Styles.login_social}>
65	        <View style={Styles.login_social_separator}>
66	          <View style={Styles.login_social_separator_line} />
67	          <Text style={Styles.login_social_separator_text}>{'or'}</Text>
68	          <View style={Styles.login_social_separator_line} />
69	        </View>
70	        <View style={Styles.login_social_buttons}>
71	          <TouchableOpacity>
72	            <View
73	              style={[
74	                Styles.login_social_button,
75	                Styles.login_social_facebook,
76	              ]}>
77	              <Image
78	                style={Styles.login_social_icon}
79	                source={require('./assets/icon-facebook.png')}
80	              />
81	            </View>
82	          </TouchableOpacity>
83	          <TouchableOpacity>
84	            <View style={Styles.login_social_button}>
85	              <Image
86	                style={Styles.login_social_icon}
87	                source={require('./assets/icon-google.png')}
88	              />
89	            </View>
90	          </TouchableOpacity>
91	          <TouchableOpacity>
92	            <View style={Styles.login_social_button}>
93	              <Image
94	                style={Styles.login_social_icon}
95	                source={require('./assets/icon-apple.png')}
96	              />
97	            </View>
98	          </TouchableOpacity>
99	        </View>
100	      </View>
101	    </View>
102	  );
103	};
```
:::

## 4 - Creating a login screen

Let’s now create a new screen for your app that will use your UserLogIn component. Add the new screen as the first (or top) screen of your StackNavigator as well:

:::CodeblockTabs
App.tsx/App.js

```typescript
1	// ...
2	
3	// Add this new screen function below the UserRegistrationScreen
4	function UserLogInScreen() {
5	  return (
6	    <>
7	      <StatusBar />
8	      <SafeAreaView style={Styles.login_container}>
9	        <View style={Styles.login_header}>
10	          <Image
11	            style={Styles.login_header_logo}
12	            source={require('./assets/logo-back4app.png')}
13	          />
14	          <Text style={Styles.login_header_text}>
15	            <Text style={Styles.login_header_text_bold}>
16	              {'React Native on Back4App - '}
17	            </Text>
18	            {' User login'}
19	          </Text>
20	        </View>
21	        <UserLogIn />
22	      </SafeAreaView>
23	    </>
24	  );
25	}
26	
27	// ...
28	
29	// Add the screen as the top one at your StackNavigator
30	const App = () => {
31	  return (
32	    <NavigationContainer>
33	      <Stack.Navigator>
34	        <Stack.Screen name="Login" component={UserLogInScreen} />
35	        <Stack.Screen name="Sign Up" component={UserRegistrationScreen} />
36	      </Stack.Navigator>
37	    </NavigationContainer>
38	  );
39	};
40	
41	// ...
```
:::

Go ahead and test your screen and component. Notice that your app will now show the user login screen instead of the user registration one, due to their placement on the StackNavigator screen list. You will see a message like this after signing in:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/cXG_2oVHycVlL5VmR3BjT_image.png" signedSrc size="50" width="355" height="730" position="center" caption}

## 5 - Creating a Home Screen and handling navigation

After logging in, you will generally want to take the user to your app home screen. Create this screen in your app’s main file:

:::CodeblockTabs
App.tsx/App.js

```typescript
1	// ...
2	
3	// Add this new screen function below the UserRegistrationScreen
4	function UserLogInScreen() {
5	  return (
6	    <>
7	      <StatusBar />
8	      <SafeAreaView style={Styles.login_container}>
9	        <View style={Styles.login_header}>
10	          <Image
11	            style={Styles.login_header_logo}
12	            source={require('./assets/logo-back4app.png')}
13	          />
14	          <Text style={Styles.login_header_text}>
15	            <Text style={Styles.login_header_text_bold}>
16	              {'React Native on Back4App - '}
17	            </Text>
18	            {' User login'}
19	          </Text>
20	        </View>
21	        <UserLogIn />
22	      </SafeAreaView>
23	    </>
24	  );
25	}
26	
27	// ...
28	
29	// Add the screen as the top one at your StackNavigator
30	const App = () => {
31	  return (
32	    <NavigationContainer>
33	      <Stack.Navigator>
34	        <Stack.Screen name="Login" component={UserLogInScreen} />
35	        <Stack.Screen name="Sign Up" component={UserRegistrationScreen} />
36	      </Stack.Navigator>
37	    </NavigationContainer>
38	  );
39	};
40	
41	// ...
```
:::

Now you need to use ‘react-navigation’ to navigate the user after he logs in, adding this new code inside theUserLogIncomponent:

:::CodeblockTabs
UserLogIn.js

```javascript
1	// ...
2	// Add this import
3	import {useNavigation} from '@react-navigation/native';
4	
5	export const UserLogIn = () => {
6	  // Add this to use useNavigation hook
7	  const navigation = useNavigation();
8	  
9	  //...
10	
11	  const doUserLogIn = async function () {
12	    const usernameValue = username;
13	    const passwordValue = password;
14	    return await Parse.User.logIn(usernameValue, passwordValue)
15	      .then(async (loggedInUser) => {
16	        Alert.alert(
17	          'Success!',
18	          `User ${loggedInUser.get('username')} has successfully signed in!`,
19	        );
20	        const currentUser = await Parse.User.currentAsync();
21	        console.log(loggedInUser === currentUser);
22	        // Add this to navigate your home screen; Navigation.navigate takes
23	        // the user to the screen named after the one passed as parameter
24	        navigation.navigate('Home');
25	        return true;
26	      })
27	      .catch((error) => {
28	        Alert.alert('Error!', error.message);
29	        return false;
30	      });
31	  };
32	// ...
```

UserLogIn.tsx

```typescript
1	// ...
2	// Add this import
3	import {useNavigation} from '@react-navigation/native';
4	
5	export const UserLogIn: FC<{}> = ({}): ReactElement => {
6	  // Add this to use useNavigation hook
7	  const navigation = useNavigation();
8	
9	  // ...
10	  
11	  const doUserLogIn = async function (): Promise<boolean> {
12	    const usernameValue: string = username;
13	    const passwordValue: string = password;
14	    return await Parse.User.logIn(usernameValue, passwordValue)
15	      .then(async (loggedInUser: Parse.User) => {
16	        Alert.alert(
17	          'Success!',
18	          `User ${loggedInUser.get('username')} has successfully signed in!`,
19	        );
20	        const currentUser: Parse.User = await Parse.User.currentAsync();
21	        console.log(loggedInUser === currentUser);
22	        // Add this to navigate your home screen; Navigation.navigate takes
23	        // the user to the screen named after the one passed as parameter
24	        navigation.navigate('Home');
25	        return true;
26	      })
27	      .catch((error: object) => {
28	        Alert.alert('Error!', error.message);
29	        return false;
30	      });
31	  };
32	
33	// ...
```
:::

You will be redirected to your new HomeScreen after logging in. You can upgrade this screen by adding this HelloUser component that shows the current user username:

:::CodeblockTabs
HelloUser.js

```javascript
1	import React, {FC, ReactElement, useEffect, useState} from 'react';
2	import {Text} from 'react-native';
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
28	  // Note the condition operator here, so the "Hello" text is only
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
2	import {Text} from 'react-native';
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
28	  // Note the condition operator here, so the "Hello" text is only
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

:::hint{type="info"}
**Note:** You can take a better look at React’s useEffect hooks [**here**](https://reactjs.org/docs/hooks-effect.html).
:::

After calling this component inside your HomeScreen, your app should look like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/F1JR7J-5HVh7MjAAdPtgt_image.png" signedSrc size="50" width="361" height="731" position="center" caption}

## 6 - Creating a logout component

The UserLogOut component is simpler than the login since the Parse.User.logOut method takes no arguments and clears the currentUser data stored locally automatically. Create this component in your app root directory:

:::CodeblockTabs
UserLogOut.js

```javascript
1	import React, {FC, ReactElement} from 'react';
2	import {Alert, Text, TouchableOpacity, View} from 'react-native';
3	import Parse from 'parse/react-native';
4	import {useNavigation} from '@react-navigation/native';
5	import {StackActions} from '@react-navigation/native';
6	import Styles from './Styles';
7	
8	export const UserLogOut = () => {
9	  const navigation = useNavigation();
10	
11	  const doUserLogOut = async function () {
12	    return await Parse.User.logOut()
13	      .then(async () => {
14	        // To verify that current user is now empty, currentAsync can be used
15	        const currentUser = await Parse.User.currentAsync();
16	        if (currentUser === null) {
17	          Alert.alert('Success!', 'No user is logged in anymore!');
18	        }
19	        // Navigation dispatch calls a navigation action, and popToTop will take
20	        // the user back to the very first screen of the stack
21	        navigation.dispatch(StackActions.popToTop());
22	        return true;
23	      })
24	      .catch((error) => {
25	        Alert.alert('Error!', error.message);
26	        return false;
27	      });
28	  };
29	
30	  return (
31	    <View style={Styles.login_wrapper}>
32	      <View style={Styles.form}>
33	        <TouchableOpacity onPress={() => doUserLogOut()}>
34	          <View style={Styles.button}>
35	            <Text style={Styles.button_label}>{'Logout'}</Text>
36	          </View>
37	        </TouchableOpacity>
38	      </View>
39	    </View>
40	  );
41	};
```

UserLogOut.tsx

```typescript
1	import React, {FC, ReactElement} from 'react';
2	import {Alert, Text, TouchableOpacity, View} from 'react-native';
3	import Parse from 'parse/react-native';
4	import {useNavigation} from '@react-navigation/native';
5	import {StackActions} from '@react-navigation/native';
6	import Styles from './Styles';
7	
8	export const UserLogOut: FC<{}> = ({}): ReactElement => {
9	  const navigation = useNavigation();
10	
11	  const doUserLogOut = async function (): Promise<boolean> {
12	    return await Parse.User.logOut()
13	      .then(async () => {
14	        // To verify that current user is now empty, currentAsync can be used
15	        const currentUser: Parse.User = await Parse.User.currentAsync();
16	        if (currentUser === null) {
17	          Alert.alert('Success!', 'No user is logged in anymore!');
18	        }
19	        // Navigation dispatch calls a navigation action, and popToTop will take
20	        // the user back to the very first screen of the stack
21	        navigation.dispatch(StackActions.popToTop());
22	        return true;
23	      })
24	      .catch((error: object) => {
25	        Alert.alert('Error!', error.message);
26	        return false;
27	      });
28	  };
29	
30	  return (
31	    <View style={Styles.login_wrapper}>
32	      <View style={Styles.form}>
33	        <TouchableOpacity onPress={() => doUserLogOut()}>
34	          <View style={Styles.button}>
35	            <Text style={Styles.button_label}>{'Logout'}</Text>
36	          </View>
37	        </TouchableOpacity>
38	      </View>
39	    </View>
40	  );
41	};
```
:::

Append this new component to HomeScreen so you can test it after signing in. Your app home screen will look like this now:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/onWiS-UCALVmfhSazjE7L_image.png" signedSrc size="50" width="351" height="728" position="center" caption}

If you perform a successful logout, you will see a message like this while being redirected to the UserLogIn screen, which is the first one in the navigation stack:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/4ncdQ-pdCOArfxivJ-IZF_image.png" signedSrc size="50" width="374" height="736" position="center" caption}

Connect your UserRegistration to a registration button inside the UserLogIn screen and repeat the same redirection pattern to your app HomeScreen. Remember to read through react-navigation’s docs to discover several customization options and control every aspect of your app navigation.

:::CodeblockTabs
UserLogIn.js

```javascript
1	// ...
2	
3	export const UserLogIn = () => {
4	  const navigation = useNavigation();
5	
6	  const [username, setUsername] = useState('');
7	  const [password, setPassword] = useState('');
8	
9	  const doUserLogIn = async function () {
10	    // Note that these values come from state variables that we've declared before
11	    const usernameValue = username;
12	    const passwordValue = password;
13	    return await Parse.User.logIn(usernameValue, passwordValue)
14	      .then(async (loggedInUser) => {
15	        // logIn returns the corresponding ParseUser object
16	        Alert.alert(
17	          'Success!',
18	          `User ${loggedInUser.get('username')} has successfully signed in!`,
19	        );
20	        // To verify that this is in fact the current user, currentAsync can be used
21	        const currentUser: Parse.User = await Parse.User.currentAsync();
22	        console.log(loggedInUser === currentUser);
23	        // Navigation.navigate takes the user to the screen named after the one
24	        // passed as parameter
25	        navigation.navigate('Home');
26	        return true;
27	      })
28	      .catch((error) => {
29	        // Error can be caused by wrong parameters or lack of Internet connection
30	        Alert.alert('Error!', error.message);
31	        return false;
32	      });
33	  };
34	
35	  return (
36	    <View style={Styles.login_wrapper}>
37	      <View style={Styles.form}>
38	        <TextInput
39	          style={Styles.form_input}
40	          value={username}
41	          placeholder={'Username'}
42	          onChangeText={(text) => setUsername(text)}
43	          autoCapitalize={'none'}
44	          keyboardType={'email-address'}
45	        />
46	        <TextInput
47	          style={Styles.form_input}
48	          value={password}
49	          placeholder={'Password'}
50	          secureTextEntry
51	          onChangeText={(text) => setPassword(text)}
52	        />
53	        <TouchableOpacity onPress={() => doUserLogIn()}>
54	          <View style={Styles.button}>
55	            <Text style={Styles.button_label}>{'Sign in'}</Text>
56	          </View>
57	        </TouchableOpacity>
58	      </View>
59	      <View style={Styles.login_social}>
60	        <View style={Styles.login_social_separator}>
61	          <View style={Styles.login_social_separator_line} />
62	          <Text style={Styles.login_social_separator_text}>{'or'}</Text>
63	          <View style={Styles.login_social_separator_line} />
64	        </View>
65	        <View style={Styles.login_social_buttons}>
66	          <TouchableOpacity>
67	            <View
68	              style={[
69	                Styles.login_social_button,
70	                Styles.login_social_facebook,
71	              ]}>
72	              <Image
73	                style={Styles.login_social_icon}
74	                source={require('./assets/icon-facebook.png')}
75	              />
76	            </View>
77	          </TouchableOpacity>
78	          <TouchableOpacity>
79	            <View style={Styles.login_social_button}>
80	              <Image
81	                style={Styles.login_social_icon}
82	                source={require('./assets/icon-google.png')}
83	              />
84	            </View>
85	          </TouchableOpacity>
86	          <TouchableOpacity>
87	            <View style={Styles.login_social_button}>
88	              <Image
89	                style={Styles.login_social_icon}
90	                source={require('./assets/icon-apple.png')}
91	              />
92	            </View>
93	          </TouchableOpacity>
94	        </View>
95	      </View>
96	      <>
97	        <TouchableOpacity onPress={() => navigation.navigate('Sign Up')}>
98	          <Text style={Styles.login_footer_text}>
99	            {"Don't have an account? "}
100	            <Text style={Styles.login_footer_link}>{'Sign up'}</Text>
101	          </Text>
102	        </TouchableOpacity>
103	      </>
104	    </View>
105	  );
106	};
107	
108	// ...
```

UserLogIn.tsx

```typescript
1	// ...
2	
3	export const UserLogIn: FC<{}> = ({}): ReactElement => {
4	  const navigation = useNavigation();
5	
6	  const [username, setUsername] = useState('');
7	  const [password, setPassword] = useState('');
8	
9	  const doUserLogIn = async function (): Promise<boolean> {
10	    // Note that these values come from state variables that we've declared before
11	    const usernameValue: string = username;
12	    const passwordValue: string = password;
13	    return await Parse.User.logIn(usernameValue, passwordValue)
14	      .then(async (loggedInUser: Parse.User) => {
15	        // logIn returns the corresponding ParseUser object
16	        Alert.alert(
17	          'Success!',
18	          `User ${loggedInUser.get('username')} has successfully signed in!`,
19	        );
20	        // To verify that this is in fact the current user, currentAsync can be used
21	        const currentUser: Parse.User = await Parse.User.currentAsync();
22	        console.log(loggedInUser === currentUser);
23	        // Navigation.navigate takes the user to the screen named after the one
24	        // passed as parameter
25	        navigation.navigate('Home');
26	        return true;
27	      })
28	      .catch((error: object) => {
29	        // Error can be caused by wrong parameters or lack of Internet connection
30	        Alert.alert('Error!', error.message);
31	        return false;
32	      });
33	  };
34	
35	  return (
36	    <View style={Styles.login_wrapper}>
37	      <View style={Styles.form}>
38	        <TextInput
39	          style={Styles.form_input}
40	          value={username}
41	          placeholder={'Username'}
42	          onChangeText={(text) => setUsername(text)}
43	          autoCapitalize={'none'}
44	          keyboardType={'email-address'}
45	        />
46	        <TextInput
47	          style={Styles.form_input}
48	          value={password}
49	          placeholder={'Password'}
50	          secureTextEntry
51	          onChangeText={(text) => setPassword(text)}
52	        />
53	        <TouchableOpacity onPress={() => doUserLogIn()}>
54	          <View style={Styles.button}>
55	            <Text style={Styles.button_label}>{'Sign in'}</Text>
56	          </View>
57	        </TouchableOpacity>
58	      </View>
59	      <View style={Styles.login_social}>
60	        <View style={Styles.login_social_separator}>
61	          <View style={Styles.login_social_separator_line} />
62	          <Text style={Styles.login_social_separator_text}>{'or'}</Text>
63	          <View style={Styles.login_social_separator_line} />
64	        </View>
65	        <View style={Styles.login_social_buttons}>
66	          <TouchableOpacity>
67	            <View
68	              style={[
69	                Styles.login_social_button,
70	                Styles.login_social_facebook,
71	              ]}>
72	              <Image
73	                style={Styles.login_social_icon}
74	                source={require('./assets/icon-facebook.png')}
75	              />
76	            </View>
77	          </TouchableOpacity>
78	          <TouchableOpacity>
79	            <View style={Styles.login_social_button}>
80	              <Image
81	                style={Styles.login_social_icon}
82	                source={require('./assets/icon-google.png')}
83	              />
84	            </View>
85	          </TouchableOpacity>
86	          <TouchableOpacity>
87	            <View style={Styles.login_social_button}>
88	              <Image
89	                style={Styles.login_social_icon}
90	                source={require('./assets/icon-apple.png')}
91	              />
92	            </View>
93	          </TouchableOpacity>
94	        </View>
95	      </View>
96	      <>
97	        <TouchableOpacity onPress={() => navigation.navigate('Sign Up')}>
98	          <Text style={Styles.login_footer_text}>
99	            {"Don't have an account? "}
100	            <Text style={Styles.login_footer_link}>{'Sign up'}</Text>
101	          </Text>
102	        </TouchableOpacity>
103	      </>
104	    </View>
105	  );
106	};
107	
108	// ...
```
:::

:::CodeblockTabs
UserRegistration.js

```javascript
1	export const UserRegistration = () => {
2	  const navigation = useNavigation();
3	
4	  const [username, setUsername] = useState('');
5	  const [password, setPassword] = useState('');
6	
7	  const doUserSignUp = async function () {
8	    // Note that these values come from state variables that we've declared before
9	    const usernameValue = username;
10	    const passwordValue = password;
11	    // Since the signUp method returns a Promise, we need to call it using await
12	    return await Parse.User.signUp(usernameValue, passwordValue)
13	      .then((createdUser) => {
14	        // Parse.User.signUp returns the already created ParseUser object if successful
15	        Alert.alert(
16	          'Success!',
17	          `User ${createdUser.get('username')} was successfully created!`,
18	        );
19	        // Navigation.navigate takes the user to the screen named after the one
20	        // passed as parameter
21	        navigation.navigate('Home');
22	        return true;
23	      })
24	      .catch((error) => {
25	        // signUp can fail if any parameter is blank or failed an uniqueness check on the server
26	        Alert.alert('Error!', error.message);
27	        return false;
28	      });
29	  };
30	
31	  return (
32	    <View style={Styles.login_wrapper}>
33	      <View style={Styles.form}>
34	        <TextInput
35	          style={Styles.form_input}
36	          value={username}
37	          placeholder={'Username'}
38	          onChangeText={(text) => setUsername(text)}
39	          autoCapitalize={'none'}
40	          keyboardType={'email-address'}
41	        />
42	        <TextInput
43	          style={Styles.form_input}
44	          value={password}
45	          placeholder={'Password'}
46	          secureTextEntry
47	          onChangeText={(text) => setPassword(text)}
48	        />
49	        <TouchableOpacity onPress={() => doUserSignUp()}>
50	          <View style={Styles.button}>
51	            <Text style={Styles.button_label}>{'Sign Up'}</Text>
52	          </View>
53	        </TouchableOpacity>
54	      </View>
55	      <View style={Styles.login_social}>
56	        <View style={Styles.login_social_separator}>
57	          <View style={Styles.login_social_separator_line} />
58	          <Text style={Styles.login_social_separator_text}>{'or'}</Text>
59	          <View style={Styles.login_social_separator_line} />
60	        </View>
61	        <View style={Styles.login_social_buttons}>
62	          <TouchableOpacity>
63	            <View
64	              style={[
65	                Styles.login_social_button,
66	                Styles.login_social_facebook,
67	              ]}>
68	              <Image
69	                style={Styles.login_social_icon}
70	                source={require('./assets/icon-facebook.png')}
71	              />
72	            </View>
73	          </TouchableOpacity>
74	          <TouchableOpacity>
75	            <View style={Styles.login_social_button}>
76	              <Image
77	                style={Styles.login_social_icon}
78	                source={require('./assets/icon-google.png')}
79	              />
80	            </View>
81	          </TouchableOpacity>
82	          <TouchableOpacity>
83	            <View style={Styles.login_social_button}>
84	              <Image
85	                style={Styles.login_social_icon}
86	                source={require('./assets/icon-apple.png')}
87	              />
88	            </View>
89	          </TouchableOpacity>
90	        </View>
91	      </View>
92	      <>
93	        <TouchableOpacity onPress={() => navigation.navigate('Login')}>
94	          <Text style={Styles.login_footer_text}>
95	            {'Already have an account? '}
96	            <Text style={Styles.login_footer_link}>{'Log In'}</Text>
97	          </Text>
98	        </TouchableOpacity>
99	      </>
100	    </View>
101	  );
102	};
103	
104	// ...
```

UserRegistration.tsx

```typescript
1	// ...
2	
3	export const UserRegistration: FC<{}> = ({}): ReactElement => {
4	  const navigation = useNavigation();
5	
6	  const [username, setUsername] = useState('');
7	  const [password, setPassword] = useState('');
8	
9	  const doUserSignUp = async function (): Promise<boolean> {
10	    // Note that these values come from state variables that we've declared before
11	    const usernameValue: string = username;
12	    const passwordValue: string = password;
13	    // Since the signUp method returns a Promise, we need to call it using await
14	    return await Parse.User.signUp(usernameValue, passwordValue)
15	      .then((createdUser: Parse.User) => {
16	        // Parse.User.signUp returns the already created ParseUser object if successful
17	        Alert.alert(
18	          'Success!',
19	          `User ${createdUser.get('username')} was successfully created!`,
20	        );
21	        // Navigation.navigate takes the user to the screen named after the one
22	        // passed as parameter
23	        navigation.navigate('Home');
24	        return true;
25	      })
26	      .catch((error: object) => {
27	        // signUp can fail if any parameter is blank or failed an uniqueness check on the server
28	        Alert.alert('Error!', error.message);
29	        return false;
30	      });
31	  };
32	
33	  return (
34	    <View style={Styles.login_wrapper}>
35	      <View style={Styles.form}>
36	        <TextInput
37	          style={Styles.form_input}
38	          value={username}
39	          placeholder={'Username'}
40	          onChangeText={(text) => setUsername(text)}
41	          autoCapitalize={'none'}
42	          keyboardType={'email-address'}
43	        />
44	        <TextInput
45	          style={Styles.form_input}
46	          value={password}
47	          placeholder={'Password'}
48	          secureTextEntry
49	          onChangeText={(text) => setPassword(text)}
50	        />
51	        <TouchableOpacity onPress={() => doUserSignUp()}>
52	          <View style={Styles.button}>
53	            <Text style={Styles.button_label}>{'Sign Up'}</Text>
54	          </View>
55	        </TouchableOpacity>
56	      </View>
57	      <View style={Styles.login_social}>
58	        <View style={Styles.login_social_separator}>
59	          <View style={Styles.login_social_separator_line} />
60	          <Text style={Styles.login_social_separator_text}>{'or'}</Text>
61	          <View style={Styles.login_social_separator_line} />
62	        </View>
63	        <View style={Styles.login_social_buttons}>
64	          <TouchableOpacity>
65	            <View
66	              style={[
67	                Styles.login_social_button,
68	                Styles.login_social_facebook,
69	              ]}>
70	              <Image
71	                style={Styles.login_social_icon}
72	                source={require('./assets/icon-facebook.png')}
73	              />
74	            </View>
75	          </TouchableOpacity>
76	          <TouchableOpacity>
77	            <View style={Styles.login_social_button}>
78	              <Image
79	                style={Styles.login_social_icon}
80	                source={require('./assets/icon-google.png')}
81	              />
82	            </View>
83	          </TouchableOpacity>
84	          <TouchableOpacity>
85	            <View style={Styles.login_social_button}>
86	              <Image
87	                style={Styles.login_social_icon}
88	                source={require('./assets/icon-apple.png')}
89	              />
90	            </View>
91	          </TouchableOpacity>
92	        </View>
93	      </View>
94	      <>
95	        <TouchableOpacity onPress={() => navigation.navigate('Login')}>
96	          <Text style={Styles.login_footer_text}>
97	            {'Already have an account? '}
98	            <Text style={Styles.login_footer_link}>{'Log In'}</Text>
99	          </Text>
100	        </TouchableOpacity>
101	      </>
102	    </View>
103	  );
104	};
105	
106	// ...
```
:::

Your login and registration screens now should look like these:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/EGxclVQlaT1CgqtgpSYoH_image.png" signedSrc size="50" width="362" height="732" position="center" caption}

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/E_IJmJBmL96wTGsmwh5aa_image.png" signedSrc size="50" width="364" height="730" position="center" caption}

## Conclusion

At the end of this guide, you learned how to log in and log out Parse users on React Native and to navigate users through your application using react-navigation. In the next guide, we will show you how to perform useful user queries.
