# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/working-with-users/react-native-facebook-login.md

---
title: SignIn with Facebook
slug: docs/react-native/parse-sdk/working-with-users/react-native-facebook-login
description: In this guide you'll learn how to login a user in Parse on React Native using Facebook FBSDK Login
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T16:07:59.386Z
updatedAt: 2024-03-29T01:26:44.717Z
---

# React Native Facebook login

## Introduction

In the last tutorials, you built a User login/logout feature to your App using the Parse.User class. Now you will learn how to use Facebook FBSDK Login to retrieve user data from Facebook and log in, sign up or link existent users with it. You will also install and configure the react-native-fbsdk lib to achieve that.

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

To build a User LogIn feature using Facebook FBSDK Login on Parse for a React Native App.

## 1 - Installing dependencies

The most popular way to add Facebook login on React Native is using react-native-fbsdk to handle it. Since this library configuration depends on your development environment, target platform, and preferences, set it up following the [**official docs**](https://github.com/facebook/react-native-fbsdk).

:::hint{type="info"}
**Note:** If you are developing for iOS, make sure that your project has support for Swift files, containing a Bridging Header. Also, pay close attention to where you add the Facebook App IDs inside yourinfo.plist file and if your Pods files are correctly generated.
:::

## 2 - Using FBSDK Login with Parse

Let’s now create a new method inside the UserLogIn component calling Facebook FBSDK authentication modal with LoginManager.logInWithPermissions, requesting permission only to access the user email. If the user successfully signs in with Facebook, you can then call AccessToken.getCurrentAccessToken to retrieve the user access token from Facebook. After that, you still need to get the user id and email using a GraphRequest through FBSDK GraphRequestManager.

:::CodeblockTabs
JavaScript

```javascript
1	const doUserLogInFacebook = async function () {
2	  try {
3	    // Login using the Facebook login dialog asking form email permission
4	    return await LoginManager.logInWithPermissions(['email']).then(
5	      (loginResult) => {
6	        if (loginResult.isCancelled) {
7	          console.log('Login cancelled');
8	          return false;
9	        } else {
10	          // Retrieve access token from FBSDK to be able to linkWith Parse
11	          AccessToken.getCurrentAccessToken().then((data) => {
12	            const facebookAccessToken = data.accessToken;
13	            // Callback that will be called after FBSDK successfuly retrieves user email and id from FB
14	            const responseEmailCallback = async (
15	              error,
16	              emailResult,
17	            ) => {
18	              if (error) {
19	                console.log('Error fetching data: ' + error.toString());
20	              } else {
21	                // Format authData to provide correctly for Facebook linkWith on Parse
22	                const facebookId = emailResult.id;
23	                const facebookEmail = emailResult.email;
24	                const authData = {
25	                  id: facebookId,
26	                  access_token: facebookAccessToken,
27	                };
28	                // Log in or sign up on Parse using this Facebook credentials
29	                let userToLogin = new Parse.User();
30	                // Set username and email to match provider email
31	                userToLogin.set('username', facebookEmail);
32	                userToLogin.set('email', facebookEmail);
33	                return await userToLogin
34	                  .linkWith('facebook', {
35	                    authData: authData,
36	                  })
37	                  .then(async (loggedInUser) => {
38	                    // logIn returns the corresponding ParseUser object
39	                    Alert.alert(
40	                      'Success!',
41	                      `User ${loggedInUser.get(
42	                        'username',
43	                      )} has successfully signed in!`,
44	                    );
45	                    // To verify that this is in fact the current user, currentAsync can be used
46	                    const currentUser = await Parse.User.currentAsync();
47	                    console.log(loggedInUser === currentUser);
48	                    // Navigation.navigate takes the user to the screen named after the one
49	                    // passed as parameter
50	                    navigation.navigate('Home');
51	                    return true;
52	                  })
53	                  .catch(async (error) => {
54	                    // Error can be caused by wrong parameters or lack of Internet connection
55	                    Alert.alert('Error!', error.message);
56	                    return false;
57	                  });
58	              }
59	            };
60	
61	            // Formats a FBSDK GraphRequest to retrieve user email and id
62	            const emailRequest = new GraphRequest(
63	              '/me',
64	              {
65	                accessToken: facebookAccessToken,
66	                parameters: {
67	                  fields: {
68	                    string: 'email',
69	                  },
70	                },
71	              },
72	              responseEmailCallback,
73	            );
74	
75	            // Start the graph request, which will call the callback after finished
76	            new GraphRequestManager().addRequest(emailRequest).start();
77	
78	            return true;
79	          });
80	        }
81	      },
82	      (error) => {
83	        console.log('Login fail with error: ' + error);
84	        return false;
85	      },
86	    );
87	  } catch (error) {
88	    Alert.alert('Error!', error.code);
89	    return false;
90	  }
91	};
```

```typescript
1	const doUserLogInFacebook = async function (): Promise<boolean> {
2	  try {
3	    // Login using the Facebook login dialog asking form email permission
4	    return await LoginManager.logInWithPermissions(['email']).then(
5	      (loginResult: object) => {
6	        if (loginResult.isCancelled) {
7	          console.log('Login cancelled');
8	          return false;
9	        } else {
10	          // Retrieve access token from FBSDK to be able to linkWith Parse
11	          AccessToken.getCurrentAccessToken().then((data: object) => {
12	            const facebookAccessToken = data.accessToken;
13	            // Callback that will be called after FBSDK successfuly retrieves user email and id from FB
14	            const responseEmailCallback = async (
15	              error: string,
16	              emailResult: object,
17	            ) => {
18	              if (error) {
19	                console.log('Error fetching data: ' + error.toString());
20	              } else {
21	                // Format authData to provide correctly for Facebook linkWith on Parse
22	                const facebookId: string = emailResult.id;
23	                const facebookEmail: string = emailResult.email;
24	                const authData: object = {
25	                  id: facebookId,
26	                  access_token: facebookAccessToken,
27	                };
28	                // Log in or sign up on Parse using this Facebook credentials
29	                let userToLogin: Parse.User = new Parse.User();
30	                // Set username and email to match provider email
31	                userToLogin.set('username', facebookEmail);
32	                userToLogin.set('email', facebookEmail);
33	                return await userToLogin
34	                  .linkWith('facebook', {
35	                    authData: authData,
36	                  })
37	                  .then(async (loggedInUser: Parse.User) => {
38	                    // logIn returns the corresponding ParseUser object
39	                    Alert.alert(
40	                      'Success!',
41	                      `User ${loggedInUser.get(
42	                        'username',
43	                      )} has successfully signed in!`,
44	                    );
45	                    // To verify that this is in fact the current user, currentAsync can be used
46	                    const currentUser: Parse.User = await Parse.User.currentAsync();
47	                    console.log(loggedInUser === currentUser);
48	                    // Navigation.navigate takes the user to the screen named after the one
49	                    // passed as parameter
50	                    navigation.navigate('Home');
51	                    return true;
52	                  })
53	                  .catch(async (error: object) => {
54	                    // Error can be caused by wrong parameters or lack of Internet connection
55	                    Alert.alert('Error!', error.message);
56	                    return false;
57	                  });
58	              }
59	            };
60	
61	            // Formats a FBSDK GraphRequest to retrieve user email and id
62	            const emailRequest = new GraphRequest(
63	              '/me',
64	              {
65	                accessToken: facebookAccessToken,
66	                parameters: {
67	                  fields: {
68	                    string: 'email',
69	                  },
70	                },
71	              },
72	              responseEmailCallback,
73	            );
74	
75	            // Start the graph request, which will call the callback after finished
76	            new GraphRequestManager().addRequest(emailRequest).start();
77	
78	            return true;
79	          });
80	        }
81	      },
82	      (error: string) => {
83	        console.log('Login fail with error: ' + error);
84	        return false;
85	      },
86	    );
87	  } catch (error: object) {
88	    Alert.alert('Error!', error.code);
89	    return false;
90	  }
91	};
```
:::

Note that after the GraphRequest succeeds, this function uses Parse.User.linkWith on a new Parse.User object to register a new user or log in a previous one with these credentials, passing his Facebook authentication data accordingly.

Add this function to your UserSignIn component and assign it to your Facebook button onPress parameter. Go ahead and test your new function, you will see that the user will be redirected to your home screen after successfully signing in.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Iro2fj5ZeoN7wXoBDLaHC_image.png" signedSrc size="50" width="347" height="729" position="center" caption}

## 3 - Verifying user sign in and session creation

To make sure that the Facebook sign-in worked, you can look at your Parse dashboard and see your new User (if your Facebook authentication data didn’t belong to another user), containing the Facebook authData parameters.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/fRO9633LiJUBYLwmYigzD_image.png)

You can also verify that a valid session was created in the dashboard, containing a pointer to that User object.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/uyh9t2l7jBOcicRezlAuc_image.png)

## 4 - Linking an existing User to FBSDK Login

Another linkWith possible use is to link an existing user with another auth provider, in this case, Facebook. Add this function that calls linkWith the same way you did in UserLogIn to your HelloUser component or directly to your home screen. The only difference here is that instead of calling the method from an empty Parse.User, you will use it from the logged-in user object.

:::CodeblockTabs
JavaScript

```javascript
1	const doUserLinkFacebook = async function () {
2	  try {
3	    // Login using the Facebook login dialog asking form email permission
4	    return await LoginManager.logInWithPermissions(['email']).then(
5	      (loginResult) => {
6	        if (loginResult.isCancelled) {
7	          console.log('Login cancelled');
8	          return false;
9	        } else {
10	          // Retrieve access token from FBSDK to be able to linkWith Parse
11	          AccessToken.getCurrentAccessToken().then((data) => {
12	            const facebookAccessToken = data.accessToken;
13	            // Callback that will be called after FBSDK successfuly retrieves user email and id from FB
14	            const responseEmailCallback = async (
15	              error,
16	              emailResult,
17	            ) => {
18	              if (error) {
19	                console.log('Error fetching data: ' + error.toString());
20	              } else {
21	                // Format authData to provide correctly for Facebook linkWith on Parse
22	                const facebookId = emailResult.id;
23	                const authData = {
24	                  id: facebookId,
25	                  access_token: facebookAccessToken,
26	                };
27	                let currentUser = await Parse.User.currentAsync();
28	                return await currentUser
29	                  .linkWith('facebook', {
30	                    authData: authData,
31	                  })
32	                  .then(async (loggedInUser) => {
33	                    // logIn returns the corresponding ParseUser object
34	                    Alert.alert(
35	                      'Success!',
36	                      `User ${loggedInUser.get(
37	                        'username',
38	                      )} has successfully linked his Facebook account!`,
39	                    );
40	                    // To verify that this is in fact the current user, currentAsync can be used
41	                    currentUser = await Parse.User.currentAsync();
42	                    console.log(loggedInUser === currentUser);
43	                    return true;
44	                  })
45	                  .catch(async (linkWithError) => {
46	                    // Error can be caused by wrong parameters or lack of Internet connection
47	                    Alert.alert('Error!', linkWithError.message);
48	                    return false;
49	                  });
50	              }
51	            };
52	
53	            // Formats a FBSDK GraphRequest to retrieve user email and id
54	            const emailRequest = new GraphRequest(
55	              '/me',
56	              {
57	                accessToken: facebookAccessToken,
58	                parameters: {
59	                  fields: {
60	                    string: 'email',
61	                  },
62	                },
63	              },
64	              responseEmailCallback,
65	            );
66	
67	            // Start the graph request, which will call the callback after finished
68	            new GraphRequestManager().addRequest(emailRequest).start();
69	
70	            return true;
71	          });
72	        }
73	      },
74	      (error) => {
75	        console.log('Login fail with error: ' + error);
76	        return false;
77	      },
78	    );
79	  } catch (error) {
80	    Alert.alert('Error!', error.code);
81	    return false;
82	  }
83	};
```

```typescript
1	const doUserLinkFacebook = async function (): Promise<boolean> {
2	  try {
3	    // Login using the Facebook login dialog asking form email permission
4	    return await LoginManager.logInWithPermissions(['email']).then(
5	      (loginResult: object) => {
6	        if (loginResult.isCancelled) {
7	          console.log('Login cancelled');
8	          return false;
9	        } else {
10	          // Retrieve access token from FBSDK to be able to linkWith Parse
11	          AccessToken.getCurrentAccessToken().then((data: object) => {
12	            const facebookAccessToken = data.accessToken;
13	            // Callback that will be called after FBSDK successfuly retrieves user email and id from FB
14	            const responseEmailCallback = async (
15	              error: string,
16	              emailResult: object,
17	            ) => {
18	              if (error) {
19	                console.log('Error fetching data: ' + error.toString());
20	              } else {
21	                // Format authData to provide correctly for Facebook linkWith on Parse
22	                const facebookId: string = emailResult.id;
23	                const authData: object = {
24	                  id: facebookId,
25	                  access_token: facebookAccessToken,
26	                };
27	                let currentUser: Parse.User = await Parse.User.currentAsync();
28	                return await currentUser
29	                  .linkWith('facebook', {
30	                    authData: authData,
31	                  })
32	                  .then(async (loggedInUser: Parse.User) => {
33	                    // logIn returns the corresponding ParseUser object
34	                    Alert.alert(
35	                      'Success!',
36	                      `User ${loggedInUser.get(
37	                        'username',
38	                      )} has successfully linked his Facebook account!`,
39	                    );
40	                    // To verify that this is in fact the current user, currentAsync can be used
41	                    currentUser = await Parse.User.currentAsync();
42	                    console.log(loggedInUser === currentUser);
43	                    return true;
44	                  })
45	                  .catch(async (linkWithError: object) => {
46	                    // Error can be caused by wrong parameters or lack of Internet connection
47	                    Alert.alert('Error!', linkWithError.message);
48	                    return false;
49	                  });
50	              }
51	            };
52	
53	            // Formats a FBSDK GraphRequest to retrieve user email and id
54	            const emailRequest = new GraphRequest(
55	              '/me',
56	              {
57	                accessToken: facebookAccessToken,
58	                parameters: {
59	                  fields: {
60	                    string: 'email',
61	                  },
62	                },
63	              },
64	              responseEmailCallback,
65	            );
66	
67	            // Start the graph request, which will call the callback after finished
68	            new GraphRequestManager().addRequest(emailRequest).start();
69	
70	            return true;
71	          });
72	        }
73	      },
74	      (error: string) => {
75	        console.log('Login fail with error: ' + error);
76	        return false;
77	      },
78	    );
79	  } catch (error: object) {
80	    Alert.alert('Error!', error.code);
81	    return false;
82	  }
83	};
```
:::

Assign this function to a Facebook button onPress parameter on your home screen. Test your new function, noting that the Parse.User object authData value will be updated with the new auth provider data. Verify if the user has indeed updated in your Parse server dashboard.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/boZiySaGlvpvsSo0AIOfN_image.png)

## Conclusion

At the end of this guide, you learned how to log in or sign up Parse users on React Native using Facebook FBSDK Login with react-native-fbsdk. In the next guide, we will show you how to perform useful user queries.
