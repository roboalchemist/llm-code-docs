# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/cloud-functions/otp-authentication-react-native.md

---
title: OTP Auth
slug: docs/react-native/parse-sdk/cloud-functions/otp-authentication-react-native
description: In this guide, you'll learn how to use Parse Cloud Code function build a OTP feature to your React Native App
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T17:59:05.497Z
updatedAt: 2025-01-16T19:29:08.295Z
---

# OTP Authentication for React Native using Cloud Functions

## Introduction

In this guide, you will learn how to use a Parse Cloud Code function to integrate Twilio Verify API in a React Native App to enable an OTP login feature. Cloud Code functions are the perfect place for this type of operations since it allows you to handle sensitive data and use other APIs outside of your application.

In this guide you will also check how to implement a React Native component using the OTP integration, improving our previous guide User Email Verification example.

:::hint{type="success"}
At any time, you can access the complete Android Project built with this tutorial at our Github repositories

- [**Kotlin Example Repository**](https://github.com/templates-back4app/Android-Parse-Sdk-Kotlin)
- [**Java Example Repository**](https://github.com/templates-back4app/Android-Parse-Sdk-Java)
:::

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- A React Native App created and [**connected to Back4App**](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk).
- Understand how to [**deploy a cloud function**](https://www.back4app.com/docs/get-started/cloud-functions) on Back4App.
- An active account at Twilio, you can create a free trial one [**here**](https://login.twilio.com/u/signup?state=hKFo2SBWNGZlcUY5cjJ3WGFZaHQwcnIzME5KQTVpVG51YjBZU6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIHg1LVRWTXpRaUphT3d4MGhZWUNXQm5WQi0xdDM1WDhLo2NpZNkgTW05M1lTTDVSclpmNzdobUlKZFI3QktZYjZPOXV1cks).
- An active account at SendGrid, you can create a free trial one [**here**](https://login.twilio.com/u/signup?state=hKFo2SBFZTlfRWNTc2tFLWRDQUMtQUJJc3pGNUFnZFRGdlNtdqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIHM3ek1JeWJoUGVBN3dNdlJSc0dlYTYwLWtVbWpPQ0NNo2NpZNkgR244UWMyZ1FOa2trZ0llT2s4QlJqRWZ5eWNoMTU2VUk).
:::

## Goal

Integrate Twilio Verify API using Parse Cloud Code functions on Back4App and use it in a React Native App.

## 1 - Setting up Twilio Verify

Twilio is a well-known 2FA token and OTP service provider, used by a wide range of companies nowadays. The Verify API is a simplified API set to help developers to verify phones, emails and to perform passwordless logins with no hassle. In this guide, you will be using the SMS and email verification methods to enable your application to have an OTP feature. We will be following the official Verify [**docs**](https://www.twilio.com/docs/verify/api), so reference it if any step becomes confused to you.

After creating your Twilio and SendGrid accounts (SendGrid is needed for sending automated emails containing your user tokens), write down the following identifiers, that can be retrieved from each services dashboard:

- Twilio’s account SID and auth token;
- SendGrid ID and a simple email template ID.

Now, create a new Verify service in Twilio Verify [**dashboard**](https://www.twilio.com/console/verify/dashboard), which is a set of configurations that will manage our OTP requests and verifications. Make sure to write down your service SID here. If you want, you can also enable email code sending by adding your SendGrid keys by creating a new email integration within the Verify service [**dashboard**](https://www.twilio.com/docs/verify/email).

That’s it, all setup is done and we may now proceed to create our Cloud Code functions.

## 2 - Integrating via Cloud Code Functions

As discussed before, using Cloud Code functions in your application enables great flexibility in your code, making it possible to detach reusable methods from your app and to better control their behavior. You can check or review how to use them in [**our Cloud functions starter guide**](https://www.back4app.com/docs/get-started/cloud-functions).

Let´s create our first cloud function called requestOTP, in which an OTP will be created and sent to the user through the chosen method. The function needs to receive two parameters, userData containing an email or phone number and verificationType, specifying which verification method to be used, email or sms.

Here is the function code:

```javascript
1	// Define Twilio keys and require the library helper
2	const accountSid = 'YOUR_TWILIO_ACCOUNT_SID_HERE';
3	const authToken = 'YOUR_TWILIO_AUTH_TOKEN_HERE';
4	const client = require('twilio')(accountSid, authToken);
5	
6	// Request OTP
7	Parse.Cloud.define('requestOTP', async (request) => {
8	  const userData = request.params.userData;
9	  const verificationType = request.params.verificationType;
10	  let verification_request = await client.verify
11	    .services('YOUR_TWILIO_VERIFY_SERVICE_ID_HERE')
12	    .verifications.create({ to: userData, channel: verificationType });
13	  return { status: verification_request.status, error: '' };
14	});
```

Note that at the top we defined our Twilio API keys and also imported the helper library. Back4App’s Parse Server implementation provides us access to the Twilio library from default, so you don’t need to install it on your server.

The second and last cloud function is called verifyOTP, it verifies your user token in Twilio’s Verify and logs him in automatically, creating a session and passing its ID back to your application, so you can log in with no password from there. There are four required parameters, being the first two the same ones from the previous function, with the addition of userToken, containing the informed verifying token, and also userInstallationId, which will be explained later on.

```javascript
1	// Since we need in UUID v4 id for creating a new session, this function
2	// mocks the creation of one without the need to import the `uuidv4` module
3	// For a more robust solution, consider using the uuid module, which uses
4	// higher quality RNG APIs.
5	// Adapted from https://stackoverflow.com/a/2117523
6	function uuidv4() {
7	  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
8	    var r = (Math.random() * 16) | 0,
9	      v = c == 'x' ? r : (r & 0x3) | 0x8;
10	    return v.toString(16);
11	  });
12	}
13	
14	// Verify OTP
15	Parse.Cloud.define('verifyOTP', async (request) => {
16	  const { userData, verificationType, userToken, userInstallationId } =
17	    request.params;
18	  let verification_check = await client.verify
19	    .services('YOUR_TWILIO_VERIFY_SERVICE_ID_HERE')
20	    .verificationChecks.create({ to: userData, code: userToken });
21	  // Status can be 'approved' if correct or 'pending' if incorrect
22	  if (verification_check.status === 'approved') {
23	    try {
24	      // Get user to login
25	      let user = null;
26	      if (verificationType === 'sms') {
27	        user = await new Parse.Query(Parse.User)
28	          .equalTo('phoneNumber', userData)
29	          .first({ useMasterKey: true });
30	      } else {
31	        user = await new Parse.Query(Parse.User)
32	          .equalTo('email', userData)
33	          .first({ useMasterKey: true });
34	      }
35	      // Create new session for login use in
36	      // Manually create session (without using Parse.Session because of it's update restrictions)
37	      // Adapted from https://stackoverflow.com/a/67432715
38	      let session = new Parse.Object('_Session', {
39	        user: user,
40	        installationId: userInstallationId,
41	        sessionToken: `r:${uuidv4()}`,
42	      });
43	      session = await session.save(undefined, { useMasterKey: true });
44	      return { sessionId: session.get('sessionToken') };
45	    } catch (error) {
46	      console.log(error);
47	      return { error: `${error}` };
48	    }
49	  }
50	  return { error: 'Could not validate your token or account! Try again!' };
51	});
```

Make sure to deploy these functions in your Parse Server before moving to the next step.

## 3 - Creating an OTP feature in React Native

Let’s now use the same project example from the User Email Verification [**guide**](https://www.back4app.com/docs/react-native/parse-sdk/working-with-users/react-native-email-verification) as a base and add some changes to it enabling the new OTP feature. We recommend downloading the project example and setting it up before continuing with the guide.

First, to allow users to log in using their phone number, add a new input field and add the value to the user registration saving method in the UserRegistration.js (or UserRegistration.tsx) file:

:::CodeblockTabs
JavaScript

```javascript
1	import React, {useState} from 'react';
2	import {
3	  Alert,
4	  Image,
5	  Text,
6	  TextInput,
7	  TouchableOpacity,
8	  View,
9	} from 'react-native';
10	import Parse from 'parse/react-native';
11	import {useNavigation} from '@react-navigation/native';
12	import {StackActions} from '@react-navigation/native';
13	import Styles from './Styles';
14	
15	export const UserRegistration = () => {
16	  const navigation = useNavigation();
17	
18	  const [username, setUsername] = useState('');
19	  const [password, setPassword] = useState('');
20	  const [email, setEmail] = useState('');
21	  const [phoneNumber, setPhoneNumber] = useState('');
22	
23	  const doUserSignUp = async function () {
24	    // Note that this values come from state variables that we've declared before
25	    const usernameValue = username;
26	    const passwordValue = password;
27	    const emailValue = email;
28	    const phoneNumberValue = phoneNumber;
29	    try {
30	      // Since the signUp method returns a Promise, we need to call it using await
31	      // Note that now you are setting the user email value as well
32	      let createdUser = await Parse.User.signUp(usernameValue, passwordValue, {
33	        email: emailValue,
34	        phoneNumber: phoneNumberValue,
35	      });
36	
37	      // Parse.User.signUp returns the already created ParseUser object if successful
38	      Alert.alert(
39	        'Success!',
40	        `User ${createdUser.get(
41	          'username',
42	        )} was successfully created! Verify your email to login`,
43	      );
44	      // Since email verification is now required, make sure to log out
45	      // the new user, so any Session created is cleared and the user can
46	      // safely log in again after verifying
47	      await Parse.User.logOut();
48	      // Go back to the login page
49	      navigation.dispatch(StackActions.popToTop());
50	      return true;
51	    } catch (error) {
52	      // signUp can fail if any parameter is blank or failed an uniqueness check on the server
53	      Alert.alert('Error!', error.message);
54	      return false;
55	    }
56	  };
57	
58	  return (
59	    <View style={Styles.login_wrapper}>
60	      <View style={Styles.form}>
61	        <TextInput
62	          style={Styles.form_input}
63	          value={username}
64	          placeholder={'Username'}
65	          onChangeText={(text) => setUsername(text)}
66	          autoCapitalize={'none'}
67	          keyboardType={'email-address'}
68	        />
69	        <TextInput
70	          style={Styles.form_input}
71	          value={email}
72	          placeholder={'Email'}
73	          onChangeText={(text) => setEmail(text)}
74	          autoCapitalize={'none'}
75	          keyboardType={'email-address'}
76	        />
77	        <TextInput
78	          style={Styles.form_input}
79	          value={phoneNumber}
80	          placeholder={'Phone (international format +15017122661)'}
81	          onChangeText={(text) => setPhoneNumber(text)}
82	          autoCapitalize={'none'}
83	          keyboardType={'phone-pad'}
84	        />
85	        <TextInput
86	          style={Styles.form_input}
87	          value={password}
88	          placeholder={'Password'}
89	          secureTextEntry
90	          onChangeText={(text) => setPassword(text)}
91	        />
92	        <TouchableOpacity onPress={() => doUserSignUp()}>
93	          <View style={Styles.button}>
94	            <Text style={Styles.button_label}>{'Sign Up'}</Text>
95	          </View>
96	        </TouchableOpacity>
97	      </View>
98	      <View style={Styles.login_social}>
99	        <View style={Styles.login_social_separator}>
100	          <View style={Styles.login_social_separator_line} />
101	          <Text style={Styles.login_social_separator_text}>{'or'}</Text>
102	          <View style={Styles.login_social_separator_line} />
103	        </View>
104	        <View style={Styles.login_social_buttons}>
105	          <TouchableOpacity>
106	            <View
107	              style={[
108	                Styles.login_social_button,
109	                Styles.login_social_facebook,
110	              ]}>
111	              <Image
112	                style={Styles.login_social_icon}
113	                source={require('./assets/icon-facebook.png')}
114	              />
115	            </View>
116	          </TouchableOpacity>
117	          <TouchableOpacity>
118	            <View style={Styles.login_social_button}>
119	              <Image
120	                style={Styles.login_social_icon}
121	                source={require('./assets/icon-google.png')}
122	              />
123	            </View>
124	          </TouchableOpacity>
125	          <TouchableOpacity>
126	            <View style={Styles.login_social_button}>
127	              <Image
128	                style={Styles.login_social_icon}
129	                source={require('./assets/icon-apple.png')}
130	              />
131	            </View>
132	          </TouchableOpacity>
133	        </View>
134	      </View>
135	      <>
136	        <TouchableOpacity onPress={() => navigation.navigate('Login')}>
137	          <Text style={Styles.login_footer_text}>
138	            {'Already have an account? '}
139	            <Text style={Styles.login_footer_link}>{'Log In'}</Text>
140	          </Text>
141	        </TouchableOpacity>
142	      </>
143	    </View>
144	  );
145	};
```

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
11	import {useNavigation} from '@react-navigation/native';
12	import {StackActions} from '@react-navigation/native';
13	import Styles from './Styles';
14	
15	export const UserRegistration: FC<{}> = ({}): ReactElement => {
16	  const navigation = useNavigation();
17	
18	  const [username, setUsername] = useState('');
19	  const [password, setPassword] = useState('');
20	  const [email, setEmail] = useState('');
21	  const [phoneNumber, setPhoneNumber] = useState('');
22	
23	  const doUserSignUp = async function (): Promise<boolean> {
24	    // Note that this values come from state variables that we've declared before
25	    const usernameValue: string = username;
26	    const passwordValue: string = password;
27	    const emailValue: string = email;
28	    const phoneNumberValue: string = phoneNumber;
29	    try {
30	      // Since the signUp method returns a Promise, we need to call it using await
31	      // Note that now you are setting the user email value as well
32	      let createdUser = await Parse.User.signUp(usernameValue, passwordValue, {
33	        email: emailValue,
34	        phoneNumber: phoneNumberValue,
35	      });
36	
37	      // Parse.User.signUp returns the already created ParseUser object if successful
38	      Alert.alert(
39	        'Success!',
40	        `User ${createdUser.get(
41	          'username',
42	        )} was successfully created! Verify your email to login`,
43	      );
44	      // Since email verification is now required, make sure to log out
45	      // the new user, so any Session created is cleared and the user can
46	      // safely log in again after verifying
47	      await Parse.User.logOut();
48	      // Go back to the login page
49	      navigation.dispatch(StackActions.popToTop());
50	      return true;
51	    } catch (error: object) {
52	      // signUp can fail if any parameter is blank or failed an uniqueness check on the server
53	      Alert.alert('Error!', error.message);
54	      return false;
55	    }
56	  };
57	
58	  return (
59	    <View style={Styles.login_wrapper}>
60	      <View style={Styles.form}>
61	        <TextInput
62	          style={Styles.form_input}
63	          value={username}
64	          placeholder={'Username'}
65	          onChangeText={(text) => setUsername(text)}
66	          autoCapitalize={'none'}
67	          keyboardType={'email-address'}
68	        />
69	        <TextInput
70	          style={Styles.form_input}
71	          value={email}
72	          placeholder={'Email'}
73	          onChangeText={(text) => setEmail(text)}
74	          autoCapitalize={'none'}
75	          keyboardType={'email-address'}
76	        />
77	        <TextInput
78	          style={Styles.form_input}
79	          value={phoneNumber}
80	          placeholder={'Phone (international format +15017122661)'}
81	          onChangeText={(text) => setPhoneNumber(text)}
82	          autoCapitalize={'none'}
83	          keyboardType={'phone-pad'}
84	        />
85	        <TextInput
86	          style={Styles.form_input}
87	          value={password}
88	          placeholder={'Password'}
89	          secureTextEntry
90	          onChangeText={(text) => setPassword(text)}
91	        />
92	        <TouchableOpacity onPress={() => doUserSignUp()}>
93	          <View style={Styles.button}>
94	            <Text style={Styles.button_label}>{'Sign Up'}</Text>
95	          </View>
96	        </TouchableOpacity>
97	      </View>
98	      <View style={Styles.login_social}>
99	        <View style={Styles.login_social_separator}>
100	          <View style={Styles.login_social_separator_line} />
101	          <Text style={Styles.login_social_separator_text}>{'or'}</Text>
102	          <View style={Styles.login_social_separator_line} />
103	        </View>
104	        <View style={Styles.login_social_buttons}>
105	          <TouchableOpacity>
106	            <View
107	              style={[
108	                Styles.login_social_button,
109	                Styles.login_social_facebook,
110	              ]}>
111	              <Image
112	                style={Styles.login_social_icon}
113	                source={require('./assets/icon-facebook.png')}
114	              />
115	            </View>
116	          </TouchableOpacity>
117	          <TouchableOpacity>
118	            <View style={Styles.login_social_button}>
119	              <Image
120	                style={Styles.login_social_icon}
121	                source={require('./assets/icon-google.png')}
122	              />
123	            </View>
124	          </TouchableOpacity>
125	          <TouchableOpacity>
126	            <View style={Styles.login_social_button}>
127	              <Image
128	                style={Styles.login_social_icon}
129	                source={require('./assets/icon-apple.png')}
130	              />
131	            </View>
132	          </TouchableOpacity>
133	        </View>
134	      </View>
135	      <>
136	        <TouchableOpacity onPress={() => navigation.navigate('Login')}>
137	          <Text style={Styles.login_footer_text}>
138	            {'Already have an account? '}
139	            <Text style={Styles.login_footer_link}>{'Log In'}</Text>
140	          </Text>
141	        </TouchableOpacity>
142	      </>
143	    </View>
144	  );
145	};
```
:::

Let’s now create a new file containing the new UserOTP screen, which will handle all the OTP processes. The screen will have two input fields, being the first one for your user to provide the means to get the OTP (email address or phone number). The other input field, hidden before submitting the OTP request, will contain the user received token. Here is the full UserOTP.js (or UserOTP.tsx) code:

:::CodeblockTabs
JavaScript

```javascript
1	import React, {useState} from 'react';
2	import {Alert, Text, TextInput, TouchableOpacity, View} from 'react-native';
3	import Parse from 'parse/react-native';
4	import {useNavigation} from '@react-navigation/native';
5	import Styles from './Styles';
6	
7	export const UserOTP = () => {
8	  const navigation = useNavigation();
9	
10	  const [userData, setUserData] = useState('');
11	  const [userToken, setUserToken] = useState('');
12	  const [tokenRequested, setTokenRequested] = useState(false);
13	
14	  const requestOTP = async function () {
15	    // Note that this values come from state variables that we've declared before
16	    const userDataValue = userData;
17	    // Check if value is an email if it contains @. Note that in a real
18	    // app you need a much better validator for this field
19	    const verificationType =
20	      userDataValue.includes('@') === true ? 'email' : 'sms';
21	    // We need to call it using await
22	    try {
23	      await Parse.Cloud.run('requestOTP', {
24	        userData: userDataValue,
25	        verificationType: verificationType,
26	      });
27	      // Show token input field
28	      setTokenRequested(true);
29	      Alert.alert('Success!', `Token requested via ${verificationType}!`);
30	      return true;
31	    } catch (error) {
32	      Alert.alert('Error!', error.message);
33	      return false;
34	    }
35	  };
36	
37	  const verifyOTP = async function () {
38	    // Note that this values come from state variables that we've declared before
39	    const userDataValue = userData;
40	    const userTokenValue = userToken;
41	    // Check if value is an email if it contains @. Note that in a real
42	    // app you need a much better validator for this field
43	    const verificationType =
44	      userDataValue.includes('@') === true ? 'email' : 'sms';
45	    // We need the installation id to allow cloud code to create
46	    // a new session and login user without password
47	    const parseInstallationId = await Parse._getInstallationId();
48	    // We need to call it using await
49	    try {
50	      // Verify OTP, if successful, returns a sessionId
51	      let response = await Parse.Cloud.run('verifyOTP', {
52	        userData: userDataValue,
53	        verificationType: verificationType,
54	        userToken: userTokenValue,
55	        parseInstallationId: parseInstallationId,
56	      });
57	      if (response.sessionId !== undefined) {
58	        // Use generated sessionId to become a user,
59	        // logging in without needing to inform password and username
60	        await Parse.User.become(response.sessionId);
61	        const loggedInUser= await Parse.User.currentAsync();
62	        Alert.alert(
63	          'Success!',
64	          `User ${loggedInUser.get('username')} has successfully signed in!`,
65	        );
66	        // Navigation.navigate takes the user to the home screen
67	        navigation.navigate('Home');
68	        return true;
69	      } else {
70	        throw response;
71	      }
72	    } catch (error) {
73	      Alert.alert('Error!', error.message);
74	      return false;
75	    }
76	  };
77	
78	  return (
79	    <View style={Styles.login_wrapper}>
80	      {tokenRequested === false ? (
81	        <View style={Styles.form}>
82	          <TextInput
83	            style={Styles.form_input}
84	            value={userData}
85	            placeholder={'Email or mobile phone number'}
86	            onChangeText={(text) => setUserData(text)}
87	            autoCapitalize={'none'}
88	            keyboardType={'email-address'}
89	          />
90	          <TouchableOpacity onPress={() => requestOTP()}>
91	            <View style={Styles.button}>
92	              <Text style={Styles.button_label}>{'Request OTP'}</Text>
93	            </View>
94	          </TouchableOpacity>
95	        </View>
96	      ) : (
97	        <View style={Styles.form}>
98	          <Text>{'Inform the received token to proceed'}</Text>
99	          <TextInput
100	            style={Styles.form_input}
101	            value={userToken}
102	            placeholder={'Token (6 digits)'}
103	            onChangeText={(text) => setUserToken(text)}
104	            autoCapitalize={'none'}
105	            keyboardType={'default'}
106	          />
107	          <TouchableOpacity onPress={() => verifyOTP()}>
108	            <View style={Styles.button}>
109	              <Text style={Styles.button_label}>{'Verify'}</Text>
110	            </View>
111	          </TouchableOpacity>
112	          <TouchableOpacity onPress={() => requestOTP()}>
113	            <View style={Styles.button}>
114	              <Text style={Styles.button_label}>{'Resend token'}</Text>
115	            </View>
116	          </TouchableOpacity>
117	        </View>
118	      )}
119	    </View>
120	  );
121	};
```

```typescript
1	import React, {FC, ReactElement, useState} from 'react';
2	import {Alert, Text, TextInput, TouchableOpacity, View} from 'react-native';
3	import Parse from 'parse/react-native';
4	import {useNavigation} from '@react-navigation/native';
5	import Styles from './Styles';
6	
7	export const UserOTP: FC<{}> = ({}): ReactElement => {
8	  const navigation = useNavigation();
9	
10	  const [userData, setUserData] = useState('');
11	  const [userToken, setUserToken] = useState('');
12	  const [tokenRequested, setTokenRequested] = useState(false);
13	
14	  const requestOTP = async function (): Promise<boolean> {
15	    // Note that this values come from state variables that we've declared before
16	    const userDataValue: string = userData;
17	    // Check if value is an email if it contains @. Note that in a real
18	    // app you need a much better validator for this field
19	    const verificationType: string =
20	      userDataValue.includes('@') === true ? 'email' : 'sms';
21	    // We need to call it using await
22	    try {
23	      await Parse.Cloud.run('requestOTP', {
24	        userData: userDataValue,
25	        verificationType: verificationType,
26	      });
27	      // Show token input field
28	      setTokenRequested(true);
29	      Alert.alert('Success!', `Token requested via ${verificationType}!`);
30	      return true;
31	    } catch (error) {
32	      Alert.alert('Error!', error.message);
33	      return false;
34	    }
35	  };
36	
37	  const verifyOTP = async function (): Promise<Boolean> {
38	    // Note that this values come from state variables that we've declared before
39	    const userDataValue: string = userData;
40	    const userTokenValue: string = userToken;
41	    // Check if value is an email if it contains @. Note that in a real
42	    // app you need a much better validator for this field
43	    const verificationType: string =
44	      userDataValue.includes('@') === true ? 'email' : 'sms';
45	    // We need the installation id to allow cloud code to create
46	    // a new session and login user without password; this is obtained
47	    // using a static method from Parse
48	    const parseInstallationId: string = await Parse._getInstallationId();
49	    // We need to call it using await
50	    try {
51	      // Verify OTP, if successful, returns a sessionId
52	      let response: object = await Parse.Cloud.run('verifyOTP', {
53	        userData: userDataValue,
54	        verificationType: verificationType,
55	        userToken: userTokenValue,
56	        parseInstallationId: parseInstallationId,
57	      });
58	      if (response.sessionId !== undefined) {
59	        // Use generated sessionId to become a user,
60	        // logging in without needing to inform password and username
61	        await Parse.User.become(response.sessionId);
62	        const loggedInUser: Parse.User = await Parse.User.currentAsync();
63	        Alert.alert(
64	          'Success!',
65	          `User ${loggedInUser.get('username')} has successfully signed in!`,
66	        );
67	        // Navigation.navigate takes the user to the home screen
68	        navigation.navigate('Home');
69	        return true;
70	      } else {
71	        throw response;
72	      }
73	    } catch (error) {
74	      Alert.alert('Error!', error.message);
75	      return false;
76	    }
77	  };
78	
79	  return (
80	    <View style={Styles.login_wrapper}>
81	      {tokenRequested === false ? (
82	        <View style={Styles.form}>
83	          <TextInput
84	            style={Styles.form_input}
85	            value={userData}
86	            placeholder={'Email or mobile phone number'}
87	            onChangeText={(text) => setUserData(text)}
88	            autoCapitalize={'none'}
89	            keyboardType={'email-address'}
90	          />
91	          <TouchableOpacity onPress={() => requestOTP()}>
92	            <View style={Styles.button}>
93	              <Text style={Styles.button_label}>{'Request OTP'}</Text>
94	            </View>
95	          </TouchableOpacity>
96	        </View>
97	      ) : (
98	        <View style={Styles.form}>
99	          <Text>{'Inform the received token to proceed'}</Text>
100	          <TextInput
101	            style={Styles.form_input}
102	            value={userToken}
103	            placeholder={'Token (6 digits)'}
104	            onChangeText={(text) => setUserToken(text)}
105	            autoCapitalize={'none'}
106	            keyboardType={'default'}
107	          />
108	          <TouchableOpacity onPress={() => verifyOTP()}>
109	            <View style={Styles.button}>
110	              <Text style={Styles.button_label}>{'Verify'}</Text>
111	            </View>
112	          </TouchableOpacity>
113	          <TouchableOpacity onPress={() => requestOTP()}>
114	            <View style={Styles.button}>
115	              <Text style={Styles.button_label}>{'Resend token'}</Text>
116	            </View>
117	          </TouchableOpacity>
118	        </View>
119	      )}
120	    </View>
121	  );
122	};
```
:::

Take a closer look at the requestOTP and verifyOTP functions, which are responsible for calling the respective Cloud Code functions and validating their response. More detail on how they work can be inspected in the code comments.

After creating the new screen, import and declare it in your App.js (or App.tsx). After that, add a new button in your UserLogin.js (or UserLogin.tsx) file, enabling your user to navigate to the OTP screen.

## 4 - Testing the New OTP Feature

Let’s now test our changes to the app. First, register a new user containing a valid email and phone number. Make sure to use the international notation (E.164) format in the phone number (e.g.: +14155552671).

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ItGPJroL7lUbXlVHS22O-_image.png" signedSrc size="50" width="355" height="751" position="center" caption}

Now, navigate to the OTP screen from the login screen and inform the same email or phone number as before. Click on the request button and you should get a message like this, changing the active input on your screen.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/-Y28GHDGf3Y_1BcFLh1mX_image.png" signedSrc size="50" width="355" height="748" position="center" caption}

If you informed an email address, you should receive an email containing the OTP token; if a phone number was passed, you will get an SMS text message on your mobile phone. The email should contain a message like this, depending on how you set up the SendGrid template.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ymagmPxoqZJLwmTFpjSlJ_image.png)



Inform the OTP token and click on verify. If everything went well, you should now be at the home screen with the following message:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/7TtHoyH3jZRy0cqVAfFF3_image.png" signedSrc size="50" width="360" height="751" position="center" caption}

## Conclusion

At the end of this guide, you learned how to use Parse Cloud Code functions to integrate third-party services in your React Native application. In the next guide, you will learn how to work with Users in Parse.
