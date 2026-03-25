# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/working-with-users/react-native-password-reset.md

---
title: Password Reset
slug: docs/react-native/parse-sdk/working-with-users/react-native-password-reset
description: In this guide you'll learn how to allow users to reset their password in Parse on React Native
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T15:50:13.670Z
updatedAt: 2024-03-29T01:24:21.713Z
---

# User Password Reset for React Native

## Introduction

It’s a fact that as soon as you introduce passwords into a system, users will forget them. In such cases, Parse library provides a way to let them securely reset their password.
As with email verification, Parse already has an implementation ready for this, Parse.User.requestPasswordEmail. By using this method, Parse will handle all aspects of password resetting for you seamlessly.

::embed[]{url="https://www.youtube.com/embed/dmlPFO1zo80"}

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- A React Native App created and [**connected to Back4App**](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk).
- Complete the previous guides so you can have a better understanding of [**the Parse User class**](https://www.back4app.com/docs/react-native/parse-sdk/working-with-users/react-native-login).
:::

## Goal

To add a user password reset feature to a React Native App using Parse.

## 1 - Customizing password reset emails

Before calling the Parse.User.requestPasswordEmail method, you can customize the message that your user will get after requesting a password reset. Log in to your App dashboard, go to Settings->Verification Emails and change your password reset email subject or message. Ensure that your user will receive an email containing clear instructions and indicating that it is indeed from your application.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/vWUUq02YQjyLFsQRtm5aN_image.png)

## 2 - Using requestPasswordEmail

Calling the Parse.User.requestPasswordEmail method only requires your user account email as a parameter, so go ahead and add the following function to your password reset screen. Remember to add a text input for your user email to your screen.

:::CodeblockTabs
JavaScript

```javascript
1	const doUserPasswordReset = async function () {
2	  // Note that this value come from state variables linked to your text input
3	  const emailValue = email;
4	  return await Parse.User.requestPasswordReset(emailValue)
5	    .then(() => {
6	      // logIn returns the corresponding ParseUser object
7	      Alert.alert(
8	        'Success!',
9	        `Please check ${email} to proceed with password reset.`,
10	      );
11	      return true;
12	    })
13	    .catch((error) => {
14	      // Error can be caused by lack of Internet connection
15	      Alert.alert('Error!', error.message);
16	      return false;
17	    });
18	};
```

```typescript
1	const doUserPasswordReset = async function (): Promise<boolean> {
2	  // Note that this value come from state variables linked to your text input
3	  const emailValue: string = email;
4	  return await Parse.User.requestPasswordReset(emailValue)
5	    .then(() => {
6	      // logIn returns the corresponding ParseUser object
7	      Alert.alert(
8	        'Success!',
9	        `Please check ${email} to proceed with password reset.`,
10	      );
11	      return true;
12	    })
13	    .catch((error: object) => {
14	      // Error can be caused by lack of Internet connection
15	      Alert.alert('Error!', error.message);
16	      return false;
17	    });
18	};
```
:::

Go ahead and test your screen and component. You will see a message like this after requesting a password reset email:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/XfbIUhm89_x4I7CJI23-H_image.png" signedSrc size="50" width="355" height="740" position="center" caption}

You should have received the email, so go ahead and check your inbox. Note that the message will contain any changes you had set up before in your Parse dashboard.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/28ePpcP3tau-T1R_1Lj77_image.png)

The password reset form will look like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/7xjVKTUDVHZkKmgZxTUVL_image.png)

That’s it, after changing the password in this form, your user will be able to log in again to your application.

## 3 - Creating a password request component

As said before, you should create a component containing the function shown on Step 2 and also a text input field for your user account email to enable password reset in your app. Here is a complete example of this component. You can plug it in in our previous guides user login project if you like.

:::CodeblockTabs
UserResetPassword.js

```javascript
1	import React, {FC, ReactElement, useState} from 'react';
2	import {Alert, Text, TextInput, TouchableOpacity, View} from 'react-native';
3	import Parse from 'parse/react-native';
4	import {useNavigation} from '@react-navigation/native';
5	import Styles from './Styles';
6	
7	export const UserResetPassword = () => {
8	  const navigation = useNavigation();
9	
10	  // Your state variable
11	  const [email, setEmail] = useState('');
12	
13	  const doUserPasswordReset = async function (): Promise<boolean> {
14	    // Note that this value come from state variables linked to your text input
15	    const emailValue = email;
16	    return await Parse.User.requestPasswordReset(emailValue)
17	      .then(() => {
18	        // logIn returns the corresponding ParseUser object
19	        Alert.alert(
20	          'Success!',
21	          `Please check ${email} to proceed with password reset.`,
22	        );
23	        // Redirect user to your login screen
24	        navigation.navigate('Login');
25	        return true;
26	      })
27	      .catch((error) => {
28	        // Error can be caused by lack of Internet connection
29	        Alert.alert('Error!', error.message);
30	        return false;
31	      });
32	  };
33	
34	  return (
35	    <View style={Styles.login_wrapper}>
36	      <View style={Styles.form}>
37	        <Text>{'Please enter your account email to reset your password:'}</Text>
38	        <TextInput
39	          style={Styles.form_input}
40	          value={email}
41	          placeholder={'Your account email'}
42	          onChangeText={(text) => setEmail(text)}
43	          autoCapitalize={'none'}
44	          keyboardType={'email-address'}
45	        />
46	        <TouchableOpacity onPress={() => doUserPasswordReset()}>
47	          <View style={Styles.button}>
48	            <Text style={Styles.button_label}>{'Request password reset'}</Text>
49	          </View>
50	        </TouchableOpacity>
51	      </View>
52	    </View>
53	  );
54	};
```

UserResetPassword.tsx

```typescript
1	import React, {FC, ReactElement, useState} from 'react';
2	import {Alert, Text, TextInput, TouchableOpacity, View} from 'react-native';
3	import Parse from 'parse/react-native';
4	import {useNavigation} from '@react-navigation/native';
5	import Styles from './Styles';
6	
7	export const UserResetPassword: FC<{}> = ({}): ReactElement => {
8	  const navigation = useNavigation();
9	
10	  // Your state variable
11	  const [email, setEmail] = useState('');
12	
13	  const doUserPasswordReset = async function (): Promise<boolean> {
14	    // Note that this value come from state variables linked to your text input
15	    const emailValue: string = email;
16	    return await Parse.User.requestPasswordReset(emailValue)
17	      .then(() => {
18	        // logIn returns the corresponding ParseUser object
19	        Alert.alert(
20	          'Success!',
21	          `Please check ${email} to proceed with password reset.`,
22	        );
23	        // Redirect user to your login screen
24	        navigation.navigate('Login');
25	        return true;
26	      })
27	      .catch((error: object) => {
28	        // Error can be caused by lack of Internet connection
29	        Alert.alert('Error!', error.message);
30	        return false;
31	      });
32	  };
33	
34	  return (
35	    <View style={Styles.login_wrapper}>
36	      <View style={Styles.form}>
37	        <Text>{'Please enter your account email to reset your password:'}</Text>
38	        <TextInput
39	          style={Styles.form_input}
40	          value={email}
41	          placeholder={'Your account email'}
42	          onChangeText={(text) => setEmail(text)}
43	          autoCapitalize={'none'}
44	          keyboardType={'email-address'}
45	        />
46	        <TouchableOpacity onPress={() => doUserPasswordReset()}>
47	          <View style={Styles.button}>
48	            <Text style={Styles.button_label}>{'Request password reset'}</Text>
49	          </View>
50	        </TouchableOpacity>
51	      </View>
52	    </View>
53	  );
54	};
```
:::

This component should render in a screen like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/NzfeuOTZiQ8jQ_0jivdJ6_image.png" signedSrc size="50" width="347" height="741" position="center" caption}

### Conclusion

At the end of this guide, you learned how to allow your Parse users to reset their password on React Native. In the next guide, we will show you how to perform useful user queries.
