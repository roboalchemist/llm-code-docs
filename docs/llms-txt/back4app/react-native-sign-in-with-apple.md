# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/working-with-users/react-native-sign-in-with-apple.md

---
title: SignIn with Apple
slug: docs/react-native/parse-sdk/working-with-users/react-native-sign-in-with-apple
description: In this guide you'll learn how to login a user in Parse on React Native using Apple SignIn
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T16:17:31.267Z
updatedAt: 2024-03-29T01:27:53.077Z
---

# SignIn with Apple for React Native

## Introduction

In the last tutorial, you built a User login/logout feature to your App using the Parse.User class. Now you will learn how to use Apple Sign-in to retrieve user data from Apple and log in, sign up or link existent users with it. You will also install and configure react-native-apple-authentication lib to achieve that.

The Parse.User.linkWith method is responsible for signing up and logging in users using any third-party authentication method, as long as you pass the right parameters requested by each different provider. After linking the user data to a new or existent Parse.User, Parse will store a valid user session in your device. Future calls to methods like currentAsync will successfully retrieve your User data, just like with regular logins.

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

To build a User LogIn feature using Apple Sign-in on Parse for a React Native App.

## 1 - Installing dependencies

The most popular way to enable Apple Sign-in on React Native is using react-native-apple-authentication to handle it. Since this library configuration depends on your development environment, target platform, and preferences, set it up following the [**official docs**](https://github.com/invertase/react-native-apple-authentication).

If you are developing for Android, you also need to install the [****](https://github.com/auth0/jwt-decode) library for decoding Apple JWT tokens.

:::hint{type="info"}
**Note:** Make sure to thoroughly follow the instructions for initial setup of Xcode environment, creating your app ID, keys and service ID on Apple Developer portal.
:::

## 2 - Using Apple Sign-in with Parse

Let’s now create a new method inside the UserLogIn component calling Apple Sign-in authentication modal. The react-native-apple-authentication lib has two separate modules to handle this call based on your user platform, so you need to use appleAuth.performRequest on iOS and appleAuthAndroid.signIn on Android. If the user signs in with Apple, this call will retrieve the user data from Apple and you need to store the id, token, and Apple email for later.

:::CodeblockTabs
JavaScript

```javascript
1	const doUserLogInApple = async function (): Promise<boolean> {
2	  try {
3	    let response = {};
4	    let appleId = '';
5	    let appleToken = '';
6	    let appleEmail = '';
7	    if (Platform.OS === 'ios') {
8	      // Performs login request requesting user email
9	      response = await appleAuth.performRequest({
10	        requestedOperation: appleAuth.Operation.LOGIN,
11	        requestedScopes: [appleAuth.Scope.EMAIL],
12	      });
13	      // On iOS, user ID and email are easily retrieved from request
14	      appleId = response.user;
15	      appleToken = response.identityToken;
16	      appleEmail = response.email;
17	    } else if (Platform.OS === 'android') {
18	      // Configure the request
19	      appleAuthAndroid.configure({
20	        // The Service ID you registered with Apple
21	        clientId: 'YOUR_SERVICE_ID',
22	        // Return URL added to your Apple dev console
23	        redirectUri: 'YOUR_REDIRECT_URL',
24	        responseType: appleAuthAndroid.ResponseType.ALL,
25	        scope: appleAuthAndroid.Scope.ALL,
26	      });
27	      response = await appleAuthAndroid.signIn();
28	      // Decode user ID and email from token returned from Apple,
29	      // this is a common workaround for Apple sign-in via web API
30	      const decodedIdToken = jwt_decode(response.id_token);
31	      appleId = decodedIdToken.sub;
32	      appleToken = response.id_token;
33	      appleEmail = decodedIdToken.email;
34	    }
35	    // Format authData to provide correctly for Apple linkWith on Parse
36	    const authData = {
37	      id: appleId,
38	      token: appleToken,
39	    };
40	  } catch (error) {
41	    // Error can be caused by wrong parameters or lack of Internet connection
42	    Alert.alert('Error!', error);
43	    return false;
44	  }
45	};
```

```typescript
1	const doUserLogInApple = async function (): Promise<boolean> {
2	  try {
3	    let response: object = {};
4	    let appleId: string = '';
5	    let appleToken: string = '';
6	    let appleEmail: string = '';
7	    if (Platform.OS === 'ios') {
8	      // Performs login request requesting user email
9	      response = await appleAuth.performRequest({
10	        requestedOperation: appleAuth.Operation.LOGIN,
11	        requestedScopes: [appleAuth.Scope.EMAIL],
12	      });
13	      // On iOS, user ID and email are easily retrieved from request
14	      appleId = response.user;
15	      appleToken = response.identityToken;
16	      appleEmail = response.email;
17	    } else if (Platform.OS === 'android') {
18	      // Configure the request
19	      appleAuthAndroid.configure({
20	        // The Service ID you registered with Apple
21	        clientId: 'YOUR_SERVICE_ID',
22	        // Return URL added to your Apple dev console
23	        redirectUri: 'YOUR_SERVICE_URL',
24	        responseType: appleAuthAndroid.ResponseType.ALL,
25	        scope: appleAuthAndroid.Scope.ALL,
26	      });
27	      response = await appleAuthAndroid.signIn();
28	      // Decode user ID and email from token returned from Apple,
29	      // this is a common workaround for Apple sign-in via web API
30	      const decodedIdToken: object = jwt_decode(response.id_token);
31	      appleId = decodedIdToken.sub;
32	      appleToken = response.id_token;
33	      appleEmail = decodedIdToken.email;
34	    }
35	    // Format authData to provide correctly for Apple linkWith on Parse
36	    const authData: object = {
37	      id: appleId,
38	      token: appleToken,
39	    };
40	  } catch (error: any) {
41	    // Error can be caused by wrong parameters or lack of Internet connection
42	    Alert.alert('Error!', error);
43	    return false;
44	  }
45	};
```
:::

Note that for Android you need to decode the returning token from Apple because the lib react-native-apple-authentication uses Apple Sign-in web API for authentication. There are restrictions for data access when using this method, so a common workaround for retrieving your user ID and email is through this decoding process, as stated [**here**](https://docs.parseplatform.org/parse-server/guide/#apple-authdata) in the official Parse guides.

After that, you can use Parse.User.linkWith on a new Parse.User object to register a new user and log in. Note that if your user had already signed up using this Apple authentication, linkWith will log him in using the existent account.

:::CodeblockTabs
JavaScript

```javascript
1	const doUserLogInApple = async function (): Promise<boolean> {
2	  try {
3	    let response = {};
4	    let appleId = '';
5	    let appleToken = '';
6	    let appleEmail = '';
7	    if (Platform.OS === 'ios') {
8	      // Performs login request requesting user email
9	      response = await appleAuth.performRequest({
10	        requestedOperation: appleAuth.Operation.LOGIN,
11	        requestedScopes: [appleAuth.Scope.EMAIL],
12	      });
13	      // On iOS, user ID and email are easily retrieved from request
14	      appleId = response.user;
15	      appleToken = response.identityToken;
16	      appleEmail = response.email;
17	    } else if (Platform.OS === 'android') {
18	      // Configure the request
19	      appleAuthAndroid.configure({
20	        // The Service ID you registered with Apple
21	        clientId: 'YOUR_SERVICE_IO',
22	        // Return URL added to your Apple dev console
23	        redirectUri: 'YOUR_SERVICE_URL',
24	        responseType: appleAuthAndroid.ResponseType.ALL,
25	        scope: appleAuthAndroid.Scope.ALL,
26	      });
27	      response = await appleAuthAndroid.signIn();
28	      // Decode user ID and email from token returned from Apple,
29	      // this is a common workaround for Apple sign-in via web API
30	      const decodedIdToken = jwt_decode(response.id_token);
31	      appleId = decodedIdToken.sub;
32	      appleToken = response.id_token;
33	      appleEmail = decodedIdToken.email;
34	    }
35	    // Format authData to provide correctly for Apple linkWith on Parse
36	    const authData = {
37	      id: appleId,
38	      token: appleToken,
39	    };
40	    // Log in or sign up on Parse using this Apple credentials
41	    let userToLogin = new Parse.User();
42	    // Set username and email to match provider email
43	    userToLogin.set('username', appleEmail);
44	    userToLogin.set('email', appleEmail);
45	    return await userToLogin
46	      .linkWith('apple', {
47	        authData: authData,
48	      })
49	      .then(async (loggedInUser) => {
50	        // logIn returns the corresponding ParseUser object
51	        Alert.alert(
52	          'Success!',
53	          `User ${loggedInUser.get('username')} has successfully signed in!`,
54	        );
55	        // To verify that this is in fact the current user, currentAsync can be used
56	        const currentUser = await Parse.User.currentAsync();
57	        console.log(loggedInUser === currentUser);
58	        // Navigation.navigate takes the user to the screen named after the one
59	        // passed as parameter
60	        navigation.navigate('Home');
61	        return true;
62	      })
63	      .catch(async (error) => {
64	        // Error can be caused by wrong parameters or lack of Internet connection
65	        Alert.alert('Error!', error.message);
66	        return false;
67	      });
68	  } catch (error) {
69	    // Error can be caused by wrong parameters or lack of Internet connection
70	    Alert.alert('Error!', error);
71	    return false;
72	  }
73	};
```

```typescript
1	const doUserLogInApple = async function (): Promise<boolean> {
2	  try {
3	    let response: object = {};
4	    let appleId: string = '';
5	    let appleToken: string = '';
6	    let appleEmail: string = '';
7	    if (Platform.OS === 'ios') {
8	      // Performs login request requesting user email
9	      response = await appleAuth.performRequest({
10	        requestedOperation: appleAuth.Operation.LOGIN,
11	        requestedScopes: [appleAuth.Scope.EMAIL],
12	      });
13	      // On iOS, user ID and email are easily retrieved from request
14	      appleId = response.user;
15	      appleToken = response.identityToken;
16	      appleEmail = response.email;
17	    } else if (Platform.OS === 'android') {
18	      // Configure the request
19	      appleAuthAndroid.configure({
20	        // The Service ID you registered with Apple
21	        clientId: 'com.back4app.userguide',
22	        // Return URL added to your Apple dev console
23	        redirectUri: 'https://tuhl.software/back4appuserguide/',
24	        responseType: appleAuthAndroid.ResponseType.ALL,
25	        scope: appleAuthAndroid.Scope.ALL,
26	      });
27	      response = await appleAuthAndroid.signIn();
28	      // Decode user ID and email from token returned from Apple,
29	      // this is a common workaround for Apple sign-in via web API
30	      const decodedIdToken: object = jwt_decode(response.id_token);
31	      appleId = decodedIdToken.sub;
32	      appleToken = response.id_token;
33	      appleEmail = decodedIdToken.email;
34	    }
35	    // Format authData to provide correctly for Apple linkWith on Parse
36	    const authData: object = {
37	      id: appleId,
38	      token: appleToken,
39	    };
40	    // Log in or sign up on Parse using this Apple credentials
41	    let userToLogin: Parse.User = new Parse.User();
42	    // Set username and email to match provider email
43	    userToLogin.set('username', appleEmail);
44	    userToLogin.set('email', appleEmail);
45	    return await userToLogin
46	      .linkWith('apple', {
47	        authData: authData,
48	      })
49	      .then(async (loggedInUser: Parse.User) => {
50	        // logIn returns the corresponding ParseUser object
51	        Alert.alert(
52	          'Success!',
53	          `User ${loggedInUser.get('username')} has successfully signed in!`,
54	        );
55	        // To verify that this is in fact the current user, currentAsync can be used
56	        const currentUser: Parse.User = await Parse.User.currentAsync();
57	        console.log(loggedInUser === currentUser);
58	        // Navigation.navigate takes the user to the screen named after the one
59	        // passed as parameter
60	        navigation.navigate('Home');
61	        return true;
62	      })
63	      .catch(async (error: object) => {
64	        // Error can be caused by wrong parameters or lack of Internet connection
65	        Alert.alert('Error!', error.message);
66	        return false;
67	      });
68	  } catch (error: any) {
69	    // Error can be caused by wrong parameters or lack of Internet connection
70	    Alert.alert('Error!', error);
71	    return false;
72	  }
73	};
```
:::

Add this function to your UserSignIn component and assign it to your Apple button onPress parameter. Go ahead and test your new function. Note that the user will be redirected to your home screen after successfully registering and/or signing in.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/wRB6RPTTfGtLJPm1Kfyj4_image.png" signedSrc size="50" width="368" height="738" position="center" caption}

## 3 - Verifying user sign in and session creation

To make sure that the Apple sign-in worked, you can look at your Parse dashboard and see your new User (if your Apple authentication data didn’t belong to another user), containing the Apple authData parameters.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/2kFrsjiGKtI8OR236o9Fh_image.png)

You can also verify that a valid session was created in the dashboard, containing a pointer to that User object.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/7cDKv-fc1S1IWbhlH3s0u_image.png)

## 4 - Linking an existing User to Apple Sign-in

Another linkWith possible use is to link an existing user with another auth provider, in this case, Apple. Add this function that calls linkWith the same way you did in UserLogIn to your HelloUser component or directly to your home screen. The only difference here is that instead of calling the method from an empty Parse.User, you will use it from the logged-in user object.

:::CodeblockTabs
JavaScript

```javascript
1	const doUserLinkApple = async function (){
2	  try {
3	    let response = {};
4	    let appleId = '';
5	    let appleToken = '';
6	    if (Platform.OS === 'ios') {
7	      // Performs login request requesting user email
8	      response = await appleAuth.performRequest({
9	        requestedOperation: appleAuth.Operation.LOGIN,
10	        requestedScopes: [appleAuth.Scope.EMAIL],
11	      });
12	      // On iOS, user ID and email are easily retrieved from request
13	      appleId = response.user;
14	      appleToken = response.identityToken;
15	    } else if (Platform.OS === 'android') {
16	      // Configure the request
17	      appleAuthAndroid.configure({
18	        // The Service ID you registered with Apple
19	        clientId: 'YOUR_SERVICE_ID',
20	        // Return URL added to your Apple dev console
21	        redirectUri: 'YOUR_REDIRECT_URL',
22	        responseType: appleAuthAndroid.ResponseType.ALL,
23	        scope: appleAuthAndroid.Scope.ALL,
24	      });
25	      response = await appleAuthAndroid.signIn();
26	      // Decode user ID and email from token returned from Apple,
27	      // this is a common workaround for Apple sign-in via web API
28	      const decodedIdToken = jwt_decode(response.id_token);
29	      appleId = decodedIdToken.sub;
30	      appleToken = response.id_token;
31	    }
32	    // Format authData to provide correctly for Apple linkWith on Parse
33	    const authData = {
34	      id: appleId,
35	      token: appleToken,
36	    };
37	    let currentUser = await Parse.User.currentAsync();
38	    // Link user with his Apple Credentials
39	    return await currentUser
40	      .linkWith('apple', {
41	        authData: authData,
42	      })
43	      .then(async (loggedInUser) => {
44	        // logIn returns the corresponding ParseUser object
45	        Alert.alert(
46	          'Success!',
47	          `User ${loggedInUser.get(
48	            'username',
49	          )} has successfully linked his Apple account!`,
50	        );
51	        // To verify that this is in fact the current user, currentAsync can be used
52	        currentUser = await Parse.User.currentAsync();
53	        console.log(loggedInUser === currentUser);
54	        return true;
55	      })
56	      .catch(async (error) => {
57	        // Error can be caused by wrong parameters or lack of Internet connection
58	        Alert.alert('Error!', error.message);
59	        return false;
60	      });
61	  } catch (error) {
62	    // Error can be caused by wrong parameters or lack of Internet connection
63	    Alert.alert('Error!', error);
64	    return false;
65	  }
66	};
```

```typescript
1	const doUserLinkApple = async function (): Promise<boolean> {
2	  try {
3	    let response: object = {};
4	    let appleId: string = '';
5	    let appleToken: string = '';
6	    if (Platform.OS === 'ios') {
7	      // Performs login request requesting user email
8	      response = await appleAuth.performRequest({
9	        requestedOperation: appleAuth.Operation.LOGIN,
10	        requestedScopes: [appleAuth.Scope.EMAIL],
11	      });
12	      // On iOS, user ID and email are easily retrieved from request
13	      appleId = response.user;
14	      appleToken = response.identityToken;
15	    } else if (Platform.OS === 'android') {
16	      // Configure the request
17	      appleAuthAndroid.configure({
18	        // The Service ID you registered with Apple
19	        clientId: 'YOUR_SERVICE_ID',
20	        // Return URL added to your Apple dev console
21	        redirectUri: 'YOUR_SERVICE_URL',
22	        responseType: appleAuthAndroid.ResponseType.ALL,
23	        scope: appleAuthAndroid.Scope.ALL,
24	      });
25	      response = await appleAuthAndroid.signIn();
26	      // Decode user ID and email from token returned from Apple,
27	      // this is a common workaround for Apple sign-in via web API
28	      const decodedIdToken: object = jwt_decode(response.id_token);
29	      appleId = decodedIdToken.sub;
30	      appleToken = response.id_token;
31	    }
32	    // Format authData to provide correctly for Apple linkWith on Parse
33	    const authData: object = {
34	      id: appleId,
35	      token: appleToken,
36	    };
37	    let currentUser: Parse.User = await Parse.User.currentAsync();
38	    // Link user with his Apple Credentials
39	    return await currentUser
40	      .linkWith('apple', {
41	        authData: authData,
42	      })
43	      .then(async (loggedInUser: Parse.User) => {
44	        // logIn returns the corresponding ParseUser object
45	        Alert.alert(
46	          'Success!',
47	          `User ${loggedInUser.get(
48	            'username',
49	          )} has successfully linked his Apple account!`,
50	        );
51	        // To verify that this is in fact the current user, currentAsync can be used
52	        currentUser = await Parse.User.currentAsync();
53	        console.log(loggedInUser === currentUser);
54	        return true;
55	      })
56	      .catch(async (error: object) => {
57	        // Error can be caused by wrong parameters or lack of Internet connection
58	        Alert.alert('Error!', error.message);
59	        return false;
60	      });
61	  } catch (error: any) {
62	    // Error can be caused by wrong parameters or lack of Internet connection
63	    Alert.alert('Error!', error);
64	    return false;
65	  }
66	};
```
:::

Assign this function to a Apple button onPress parameter on your home screen. Test your new function, noting that the Parse.User object authData value will be updated with the new auth provider data. Verify if the user has indeed updated in your Parse server dashboard.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/MNr0-o_nrQgaLIDQfa8sw_image.png)

## Conclusion

At the end of this guide, you learned how to log in, sign up or link existing Parse users on React Native using Apple Sign-in with react-native-apple-authentication. In the next guide, we will show you how to perform useful user queries.
