# Source: https://docs-containers.back4app.com/docs/react/working-with-users/react-login.md

---
title: User LogIn
slug: docs/react/working-with-users/react-login
description: In this guide you will learn how to login and logout a user in Parse on React
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T17:20:13.079Z
updatedAt: 2025-01-17T01:29:37.768Z
---

# User LogIn and LogOut for React

## Introduction

After implementing a component that handles user registration in Parse in the last guide, you will now learn how to log in and log out users using the same Parse.User class.

The Parse.User.logIn method stores in your local storage a valid user session, so future calls to methods like current will successfully retrieve your User data. On the other hand, logOut will clear this session from the disk and log out of any linked services in your Parse server.

## Prerequisites

:::hint{type="info"}
To complete this tutorial, you will need:

-
  A React App created and [**connected to Back4App**](https://www.back4app.com/docs/react/quickstart).
- Complete the previous guide so you can have a better understanding of [**the Parse.User class**](https://www.back4app.com/docs/react/working-with-users/sign-up-page-react).
- If you want to test/use the screen layout provided by this guide, you should set up the [**&#x20;library.**](https://ant.design/docs/react/introduce)
:::

## Goal

To build a User LogIn and LogOut feature using Parse for a React App.

## 1 - Understanding the logIn and logOut methods

Parse User management uses the Parse.User object type, which extends the default ParseObject type while containing unique helper methods, such as current and getUsername, that will help you retrieve user data throughout your app. You can read more about the Parse.User object [**here at the official documentation**](https://parseplatform.org/Parse-SDK-JS/api/master/Parse.User.html).

In this guide, you will learn how to use the logIn and logOut methods that will handle the user login process, saving the user data locally.

## 2 - Creating a login component

Let’s now build the UserLogIn component in your App. Create a new file in your src directory called UserLogIn.js (UserLogIn.tsx if you are using TypeScript) and add the input elements using state hooks to manage their data. Note that there is also a function responsible for updating a state variable with the current logged in user, that you will use later:

:::CodeblockTabs
UserLogIn.js

```javascript
1	import React, { useState } from 'react';
2	import Parse from 'parse/dist/parse.min.js';
3	import './App.css';
4	import { Button, Divider, Input } from 'antd';
5	
6	export const UserLogin = () => {
7	  // State variables
8	  const [username, setUsername] = useState('');
9	  const [password, setPassword] = useState('');
10	  const [currentUser, setCurrentUser] = useState(null);
11	
12	  // Function that will return current user and also update current username
13	  const getCurrentUser = async function () {
14	    const currentUser = await Parse.User.current();
15	    // Update state variable holding current user
16	    setCurrentUser(currentUser);
17	    return currentUser;
18	  };
19	
20	  return (
21	    <div>
22	      <div className="header">
23	        <img
24	          className="header_logo"
25	          alt="Back4App Logo"
26	          src={
27	            'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png'
28	          }
29	        />
30	        <p className="header_text_bold">{'React on Back4App'}</p>
31	        <p className="header_text">{'User Login'}</p>
32	      </div>
33	      <div className="container">
34	        <h2 className="heading">{'User Login'}</h2>
35	        <Divider />
36	        <div className="form_wrapper">
37	          <Input
38	            value={username}
39	            onChange={(event) => setUsername(event.target.value)}
40	            placeholder="Username"
41	            size="large"
42	            className="form_input"
43	          />
44	          <Input
45	            value={password}
46	            onChange={(event) => setPassword(event.target.value)}
47	            placeholder="Password"
48	            size="large"
49	            type="password"
50	            className="form_input"
51	          />
52	        </div>
53	        <div className="form_buttons">
54	          <Button
55	            onClick={() => doUserLogIn()}
56	            type="primary"
57	            className="form_button"
58	            color={'#208AEC'}
59	            size="large"
60	            block
61	          >
62	            Log In
63	          </Button>
64	        </div>
65	        <Divider />
66	        <div className="login-social">
67	          <div className="login-social-item login-social-item--facebook">
68	            <img className="login-social-item__image" src={'https://findicons.com/files/icons/2830/clean_social_icons/250/facebook.png'} alt=""/>
69	          </div>
70	          <div className="login-social-item">
71	            <img className="login-social-item__image" src={'data:image/png;base64,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'} alt=""/>
72	          </div>
73	          <div className="login-social-item">
74	            <img className="login-social-item__image" src={'data:image/png;base64,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'} alt=""/>
75	          </div>
76	        </div>
77	        <p className="form__hint">Don't have an account? <a className="form__link" href="#">Sign up</a></p>
78	      </div>
79	    </div>
80	  );
81	};
```

UserLogIn.tsx

```typescript
1	import React, { useState, FC, ReactElement } from 'react';
2	import './App.css';
3	import { Button, Divider, Input } from 'antd';
4	const Parse = require('parse/dist/parse.min.js');
5	
6	export const UserLogin: FC<{}> = (): ReactElement => {
7	  // State variables
8	  const [username, setUsername] = useState('');
9	  const [password, setPassword] = useState('');
10	  const [currentUser, setCurrentUser] = useState<Parse.Object | null>(null);
11	
12	  // Function that will return current user and also update current username
13	  const getCurrentUser = async function (): Promise<Parse.User | null> {
14	    const currentUser: (Parse.User | null) = await Parse.User.current();
15	    // Update state variable holding current user
16	    setCurrentUser(currentUser);
17	    return currentUser;
18	  }
19	
20	  return (
21	    <div>
22	      <div className="header">
23	        <img
24	          className="header_logo"
25	          alt="Back4App Logo"
26	          src={
27	            'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png'
28	          }
29	        />
30	        <p className="header_text_bold">{'React on Back4App'}</p>
31	        <p className="header_text">{'User Login'}</p>
32	      </div>
33	      <div className="container">
34	        <h2 className="heading">{'User Login'}</h2>
35	        <Divider />
36	        <div className="form_wrapper">
37	          <Input
38	            value={username}
39	            onChange={(event) => setUsername(event.target.value)}
40	            placeholder="Username"
41	            size="large"
42	            className="form_input"
43	          />
44	          <Input
45	            value={password}
46	            onChange={(event) => setPassword(event.target.value)}
47	            placeholder="Password"
48	            size="large"
49	            type="password"
50	            className="form_input"
51	          />
52	        </div>
53	        <div className="form_buttons">
54	          <Button
55	            onClick={() => doUserLogIn()}
56	            type="primary"
57	            className="form_button"
58	            color={'#208AEC'}
59	            size="large"
60	            block
61	          >
62	            Log In
63	          </Button>
64	        </div>
65	        <Divider />
66	        <div className="login-social">
67	          <div className="login-social-item login-social-item--facebook">
68	            <img className="login-social-item__image" src={'https://findicons.com/files/icons/2830/clean_social_icons/250/facebook.png'} alt=""/>
69	          </div>
70	          <div className="login-social-item">
71	            <img className="login-social-item__image" src={'data:image/png;base64,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'} alt=""/>
72	          </div>
73	          <div className="login-social-item">
74	            <img className="login-social-item__image" src={'data:image/png;base64,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'} alt=""/>
75	          </div>
76	        </div>
77	        <p className="form__hint">Don't have an account? <a className="form__link" href="#">Sign up</a></p>
78	      </div>
79	    </div>
80	  );
81	};
```
:::

You can now implement the function that will call the Parse.User.logIn method, using state variables:

:::CodeblockTabs
JavaScript

```javascript
1	const doUserLogIn = async function () {
2	  // Note that these values come from state variables that we've declared before
3	  const usernameValue = username;
4	  const passwordValue = password;
5	  try {
6	    const loggedInUser = await Parse.User.logIn(usernameValue, passwordValue);
7	    // logIn returns the corresponding ParseUser object
8	    alert(
9	      `Success! User ${loggedInUser.get(
10	        'username'
11	      )} has successfully signed in!`
12	    );
13	    // To verify that this is in fact the current user, `current` can be used
14	    const currentUser = await Parse.User.current();
15	    console.log(loggedInUser === currentUser);
16	    // Clear input fields
17	    setUsername('');
18	    setPassword('');
19	    // Update state variable holding current user
20	    getCurrentUser();
21	    return true;
22	  } catch (error) {
23	    // Error can be caused by wrong parameters or lack of Internet connection
24	    alert(`Error! ${error.message}`);
25	    return false;
26	  }
27	};
```

```typescript
1	const doUserLogIn = async function (): Promise<boolean> {
2	  // Note that these values come from state variables that we've declared before
3	  const usernameValue: string = username;
4	  const passwordValue: string = password;
5	  try {
6	    const loggedInUser: Parse.User = await Parse.User.logIn(usernameValue, passwordValue);
7	    // logIn returns the corresponding ParseUser object
8	    alert(
9	      `Success! User ${loggedInUser.get('username')} has successfully signed in!`,
10	    );
11	    // To verify that this is in fact the current user, `current` can be used
12	    const currentUser: Parse.User = await Parse.User.current();
13	    console.log(loggedInUser === currentUser);
14	    // Clear input fields
15	    setUsername('');
16	    setPassword('');
17	    // Update state variable holding current user
18	    getCurrentUser();
19	    return true;
20	  } catch (error: any) {
21	    // Error can be caused by wrong parameters or lack of Internet connection
22	    alert(`Error! ${error.message}`);
23	    return false;
24	  }
25	};
```
:::

Insert this function inside the UserLogIn component, just before the return call, to be called and tested. Remember to update the form’s login button onClick action to () => doUserLogIn(). If you want to fully render this screen layout, add these classes to your App.css file:

:::CodeblockTabs
App.css

```css
1	@import '~antd/dist/antd.css';
2	
3	.App {
4	  text-align: center;
5	}
6	
7	html {
8	  box-sizing: border-box;
9	  outline: none;
10	  overflow: auto;
11	}
12	
13	*,
14	*:before,
15	*:after {
16	  margin: 0;
17	  padding: 0;
18	  box-sizing: inherit;
19	}
20	
21	h1,
22	h2,
23	h3,
24	h4,
25	h5,
26	h6 {
27	  margin: 0;
28	  font-weight: bold;
29	}
30	
31	p {
32	  margin: 0;
33	}
34	
35	body {
36	  margin: 0;
37	  background-color: #fff;
38	}
39	
40	.container {
41	  width: 100%;
42	  max-width: 900px;
43	  margin: auto;
44	  padding: 20px 0;
45	  text-align: left;
46	}
47	
48	.header {
49	  align-items: center;
50	  padding: 25px 0;
51	  background-color: #208AEC;
52	}
53	
54	.header_logo {
55	  height: 55px;
56	  margin-bottom: 20px;
57	  object-fit: contain;
58	}
59	
60	.header_text_bold {
61	  margin-bottom: 3px;
62	  color: rgba(255, 255, 255, 0.9);
63	  font-size: 16px;
64	  font-weight: bold;
65	}
66	
67	.header_text {
68	  color: rgba(255, 255, 255, 0.9);
69	  font-size: 15px;
70	}
71	
72	.heading {
73	  font-size: 22px;
74	}
75	
76	.flex {
77	  display: flex;
78	}
79	
80	.flex_between {
81	  display: flex;
82	  justify-content: space-between;
83	}
84	
85	.flex_child {
86	  flex: 0 0 45%;
87	}
88	
89	.heading_button {
90	  margin-left: 12px;
91	}
92	
93	.list_item {
94	  padding-bottom: 15px;
95	  margin-bottom: 15px;
96	  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
97	  text-align: left;
98	}
99	
100	.list_item_title {
101	  color: rgba(0, 0, 0, 0.87);
102	  font-size: 17px;
103	}
104	
105	.list_item_description {
106	  color: rgba(0, 0, 0, 0.5);
107	  font-size: 15px;
108	}
109	
110	.form_input {
111	  margin-bottom: 20px;
112	}
113	
114	.login-social {
115	  display: flex;
116	  justify-content: center;
117	  margin-bottom: 30px;
118	}
119	
120	.login-social-item {
121	  width: 54px;
122	  height: 54px;
123	  border-radius: 54px;
124	  padding: 12px;
125	  margin: 0 12px;
126	  border: 1px solid #e6e6e6;
127	  box-shadow: 0 2px 4px #d6d6d6;
128	}
129	
130	.login-social-item--facebook {
131	  padding: 4px;
132	  background-color: #3C5B9B;
133	}
134	
135	.login-social-item__image {
136	  width: 100%;
137	}
138	
139	.form__hint {
140	  color: rgba(0, 0, 0, 0.5);
141	  font-size: 16px;
142	  text-align: center;
143	}
```
:::

Go ahead and run your application, importing this login component into your main application file. You should see a screen just like this and also a success message after logging in with the right credentials:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/SsOX_fEH0uUbp0_3VRB-l_image.png)

## 3 - Checking logged-in user

After your user successfully logs in to the application, he should be able to know about that and also be able to log out of the application. First, let’s hide the login form and render a welcome message containing the username. Note the usage of the conditional operator in conjunction with the state variable holding the current username.

:::CodeblockTabs
UserLogIn.js

```javascript
1	// Your imports ...
2	export const UserLogin = () => {
3	  // State variables and functions ...
4	
5	  return (
6	    <div>
7	      <div className="header">
8	        <img
9	          className="header_logo"
10	          alt="Back4App Logo"
11	          src={
12	            'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png'
13	          }
14	        />
15	        <p className="header_text_bold">{'React on Back4App'}</p>
16	        <p className="header_text">{'User Login'}</p>
17	      </div>
18	      {currentUser === null && (
19	        <div className="container">
20	          <h2 className="heading">{'User Login'}</h2>
21	          <Divider />
22	          <div className="form_wrapper">
23	            <Input
24	              value={username}
25	              onChange={(event) => setUsername(event.target.value)}
26	              placeholder="Username"
27	              size="large"
28	              className="form_input"
29	            />
30	            <Input
31	              value={password}
32	              onChange={(event) => setPassword(event.target.value)}
33	              placeholder="Password"
34	              size="large"
35	              type="password"
36	              className="form_input"
37	            />
38	          </div>
39	          <div className="form_buttons">
40	            <Button
41	              onClick={() => doUserLogIn()}
42	              type="primary"
43	              className="form_button"
44	              color={'#208AEC'}
45	              size="large"
46	              block
47	            >
48	              Log In
49	            </Button>
50	          </div>
51	          <Divider />
52	          <div className="login-social">
53	            <div className="login-social-item login-social-item--facebook">
54	              <img className="login-social-item__image" src={'https://findicons.com/files/icons/2830/clean_social_icons/250/facebook.png'} alt=""/>
55	            </div>
56	            <div className="login-social-item">
57	              <img className="login-social-item__image" src={'data:image/png;base64,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'} alt=""/>
58	            </div>
59	            <div className="login-social-item">
60	              <img className="login-social-item__image" src={'data:image/png;base64,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'} alt=""/>
61	            </div>
62	          </div>
63	          <p className="form__hint">Don't have an account? <a className="form__link" href="#">Sign up</a></p>
64	        </div>
65	      )}
66	      {currentUser !== null &&
67	        (<div className="container">
68	          <h2 className="heading">{'User Screen'}</h2>
69	          <Divider />
70	          <h2 className="heading">{`Hello ${currentUser.get('username')}!`}</h2>
71	          <div className="form_buttons">
72	            <Button
73	              onClick={() => {}}
74	              type="primary"
75	              className="form_button"
76	              color={'#208AEC'}
77	              size="large"
78	            >
79	              Log Out
80	            </Button>
81	          </div>
82	        </div>)
83	      }
84	    </div>
85	  );
86	};
```

UserLogIn.tsx

```typescript
1	// Your imports ...
2	export const UserLogin: FC<{}> = (): ReactElement => {
3	  // State variables and functions ...
4	  
5	  return (
6	    <div>
7	      <div className="header">
8	        <img
9	          className="header_logo"
10	          alt="Back4App Logo"
11	          src={
12	            'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png'
13	          }
14	        />
15	        <p className="header_text_bold">{'React on Back4App'}</p>
16	        <p className="header_text">{'User Login'}</p>
17	      </div>
18	      {currentUser === null && (
19	        <div className="container">
20	          <h2 className="heading">{'User Login'}</h2>
21	          <Divider />
22	          <div className="form_wrapper">
23	            <Input
24	              value={username}
25	              onChange={(event) => setUsername(event.target.value)}
26	              placeholder="Username"
27	              size="large"
28	              className="form_input"
29	            />
30	            <Input
31	              value={password}
32	              onChange={(event) => setPassword(event.target.value)}
33	              placeholder="Password"
34	              size="large"
35	              type="password"
36	              className="form_input"
37	            />
38	          </div>
39	          <div className="form_buttons">
40	            <Button
41	              onClick={() => doUserLogIn()}
42	              type="primary"
43	              className="form_button"
44	              color={'#208AEC'}
45	              size="large"
46	              block
47	            >
48	              Log In
49	            </Button>
50	          </div>
51	          <Divider />
52	          <div className="login-social">
53	            <div className="login-social-item login-social-item--facebook">
54	              <img className="login-social-item__image" src={'https://findicons.com/files/icons/2830/clean_social_icons/250/facebook.png'} alt=""/>
55	            </div>
56	            <div className="login-social-item">
57	              <img className="login-social-item__image" src={'data:image/png;base64,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'} alt=""/>
58	            </div>
59	            <div className="login-social-item">
60	              <img className="login-social-item__image" src={'data:image/png;base64,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'} alt=""/>
61	            </div>
62	          </div>
63	          <p className="form__hint">Don't have an account? <a className="form__link" href="#">Sign up</a></p>
64	        </div>
65	      )}
66	      {currentUser !== null &&
67	        (<div className="container">
68	          <h2 className="heading">{'User Screen'}</h2>
69	          <Divider />
70	          <h2 className="heading">{`Hello ${currentUser.get('username')}!`}</h2>
71	          <div className="form_buttons">
72	            <Button
73	              onClick={() => {}}
74	              type="primary"
75	              className="form_button"
76	              color={'#208AEC'}
77	              size="large"
78	            >
79	              Log Out
80	            </Button>
81	          </div>
82	        </div>)
83	      }
84	    </div>
85	  );
86	};
```
:::

Go ahead and run your app again. Notice that your app will now show the user screen and welcome message just like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/iphqrWbJfIa34MW3ei4aL_image.png" signedSrc size="70" width="702" height="503" position="center" caption}

## 4 - Creating a log out function

The logOut method is simpler than the login since the Parse.User.logOut method takes no arguments and clears the currentUser data stored locally automatically. Create this function in the UserLogin component and call it in the onClick attribute of the logout button:

:::CodeblockTabs
UserLogOut.js

```javascript
1	const doUserLogOut = async function () {
2	  try {
3	    await Parse.User.logOut();
4	    // To verify that current user is now empty, currentAsync can be used
5	    const currentUser = await Parse.User.current();
6	    if (currentUser === null) {
7	      alert('Success! No user is logged in anymore!');
8	    }
9	    // Update state variable holding current user
10	    getCurrentUser();
11	    return true;
12	  } catch (error) {
13	    alert(`Error! ${error.message}`);
14	    return false;
15	  }
16	};
```

UserLogOut.tsx

```typescript
1	const doUserLogOut = async function (): Promise<boolean> {
2	  try {
3	    await Parse.User.logOut();
4	    // To verify that current user is now empty, currentAsync can be used
5	    const currentUser: Parse.User = await Parse.User.current();
6	    if (currentUser === null) {
7	      alert('Success! No user is logged in anymore!');
8	    }
9	    // Update state variable holding current user
10	    getCurrentUser();
11	    return true;
12	  } catch (error: any) {
13	    alert(`Error! ${error.message}`);
14	    return false;
15	  }
16	};
```
:::

If you perform a successful log out, you will see a message like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/JmAG22pgR2Pr-TQj0SuB__image.png" signedSrc size="80" width="732" height="494" position="center" caption}

Here is the full component code containing all the functions shown before:

:::CodeblockTabs
UserLogIn.js

```javascript
1	import React, { useState } from 'react';
2	import Parse from 'parse/dist/parse.min.js';
3	import './App.css';
4	import { Button, Divider, Input } from 'antd';
5	
6	export const UserLogin = () => {
7	  // State variables
8	  const [username, setUsername] = useState('');
9	  const [password, setPassword] = useState('');
10	  const [currentUser, setCurrentUser] = useState(null);
11	
12	  const doUserLogIn = async function () {
13	    // Note that these values come from state variables that we've declared before
14	    const usernameValue = username;
15	    const passwordValue = password;
16	    try {
17	      const loggedInUser = await Parse.User.logIn(usernameValue, passwordValue);
18	      // logIn returns the corresponding ParseUser object
19	      alert(
20	        `Success! User ${loggedInUser.get(
21	          'username'
22	        )} has successfully signed in!`
23	      );
24	      // To verify that this is in fact the current user, `current` can be used
25	      const currentUser = await Parse.User.current();
26	      console.log(loggedInUser === currentUser);
27	      // Clear input fields
28	      setUsername('');
29	      setPassword('');
30	      // Update state variable holding current user
31	      getCurrentUser();
32	      return true;
33	    } catch (error) {
34	      // Error can be caused by wrong parameters or lack of Internet connection
35	      alert(`Error! ${error.message}`);
36	      return false;
37	    }
38	  };
39	
40	  const doUserLogOut = async function () {
41	    try {
42	      await Parse.User.logOut();
43	      // To verify that current user is now empty, currentAsync can be used
44	      const currentUser = await Parse.User.current();
45	      if (currentUser === null) {
46	        alert('Success! No user is logged in anymore!');
47	      }
48	      // Update state variable holding current user
49	      getCurrentUser();
50	      return true;
51	    } catch (error) {
52	      alert(`Error! ${error.message}`);
53	      return false;
54	    }
55	  };
56	
57	  // Function that will return current user and also update current username
58	  const getCurrentUser = async function () {
59	    const currentUser = await Parse.User.current();
60	    // Update state variable holding current user
61	    setCurrentUser(currentUser);
62	    return currentUser;
63	  };
64	
65	  return (
66	    <div>
67	      <div className="header">
68	        <img
69	          className="header_logo"
70	          alt="Back4App Logo"
71	          src={
72	            'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png'
73	          }
74	        />
75	        <p className="header_text_bold">{'React on Back4App'}</p>
76	        <p className="header_text">{'User Login'}</p>
77	      </div>
78	      {currentUser === null && (
79	        <div className="container">
80	          <h2 className="heading">{'User Login'}</h2>
81	          <Divider />
82	          <div className="form_wrapper">
83	            <Input
84	              value={username}
85	              onChange={(event) => setUsername(event.target.value)}
86	              placeholder="Username"
87	              size="large"
88	              className="form_input"
89	            />
90	            <Input
91	              value={password}
92	              onChange={(event) => setPassword(event.target.value)}
93	              placeholder="Password"
94	              size="large"
95	              type="password"
96	              className="form_input"
97	            />
98	          </div>
99	          <div className="form_buttons">
100	            <Button
101	              onClick={() => doUserLogIn()}
102	              type="primary"
103	              className="form_button"
104	              color={'#208AEC'}
105	              size="large"
106	              block
107	            >
108	              Log In
109	            </Button>
110	          </div>
111	          <Divider />
112	          <div className="login-social">
113	            <div className="login-social-item login-social-item--facebook">
114	              <img className="login-social-item__image" src={'https://findicons.com/files/icons/2830/clean_social_icons/250/facebook.png'} alt=""/>
115	            </div>
116	            <div className="login-social-item">
117	              <img className="login-social-item__image" src={'data:image/png;base64,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'} alt=""/>
118	            </div>
119	            <div className="login-social-item">
120	              <img className="login-social-item__image" src={'data:image/png;base64,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'} alt=""/>
121	            </div>
122	          </div>
123	          <p className="form__hint">Don't have an account? <a className="form__link" href="#">Sign up</a></p>
124	        </div>
125	      )}
126	      {currentUser !== null && (
127	        <div className="container">
128	          <h2 className="heading">{'User Screen'}</h2>
129	          <Divider />
130	          <h2 className="heading">{`Hello ${currentUser.get('username')}!`}</h2>
131	          <div className="form_buttons">
132	            <Button
133	              onClick={() => doUserLogOut()}
134	              type="primary"
135	              className="form_button"
136	              color={'#208AEC'}
137	              size="large"
138	            >
139	              Log Out
140	            </Button>
141	          </div>
142	        </div>
143	      )}
144	    </div>
145	  );
146	};
```

UserLogIn.tsx

```typescript
1	import React, { useState, FC, ReactElement } from 'react';
2	import './App.css';
3	import { Button, Divider, Input } from 'antd';
4	const Parse = require('parse/dist/parse.min.js');
5	
6	export const UserLogin: FC<{}> = (): ReactElement => {
7	  // State variables
8	  const [username, setUsername] = useState('');
9	  const [password, setPassword] = useState('');
10	  const [currentUser, setCurrentUser] = useState<Parse.Object | null>(null);
11	
12	  const doUserLogIn = async function (): Promise<boolean> {
13	    // Note that these values come from state variables that we've declared before
14	    const usernameValue: string = username;
15	    const passwordValue: string = password;
16	    try {
17	      const loggedInUser: Parse.User = await Parse.User.logIn(usernameValue, passwordValue);
18	      // logIn returns the corresponding ParseUser object
19	      alert(
20	        `Success! User ${loggedInUser.get('username')} has successfully signed in!`,
21	      );
22	      // To verify that this is in fact the current user, `current` can be used
23	      const currentUser: Parse.User = await Parse.User.current();
24	      console.log(loggedInUser === currentUser);
25	      // Clear input fields
26	      setUsername('');
27	      setPassword('');
28	      // Update state variable holding current user
29	      getCurrentUser();
30	      return true;
31	    } catch (error: any) {
32	      // Error can be caused by wrong parameters or lack of Internet connection
33	      alert(`Error! ${error.message}`);
34	      return false;
35	    }
36	  };
37	
38	  const doUserLogOut = async function (): Promise<boolean> {
39	    try {
40	      await Parse.User.logOut();
41	      // To verify that current user is now empty, currentAsync can be used
42	      const currentUser: Parse.User = await Parse.User.current();
43	      if (currentUser === null) {
44	        alert('Success! No user is logged in anymore!');
45	      }
46	      // Update state variable holding current user
47	      getCurrentUser();
48	      return true;
49	    } catch (error: any) {
50	      alert(`Error! ${error.message}`);
51	      return false;
52	    }
53	  };
54	
55	  // Function that will return current user and also update current username
56	  const getCurrentUser = async function (): Promise<Parse.User | null> {
57	    const currentUser: (Parse.User | null) = await Parse.User.current();
58	    // Update state variable holding current user
59	    setCurrentUser(currentUser);
60	    return currentUser;
61	  }
62	
63	  return (
64	    <div>
65	      <div className="header">
66	        <img
67	          className="header_logo"
68	          alt="Back4App Logo"
69	          src={
70	            'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png'
71	          }
72	        />
73	        <p className="header_text_bold">{'React on Back4App'}</p>
74	        <p className="header_text">{'User Login'}</p>
75	      </div>
76	      {currentUser === null && (
77	        <div className="container">
78	          <h2 className="heading">{'User Login'}</h2>
79	          <Divider />
80	          <div className="form_wrapper">
81	            <Input
82	              value={username}
83	              onChange={(event) => setUsername(event.target.value)}
84	              placeholder="Username"
85	              size="large"
86	              className="form_input"
87	            />
88	            <Input
89	              value={password}
90	              onChange={(event) => setPassword(event.target.value)}
91	              placeholder="Password"
92	              size="large"
93	              type="password"
94	              className="form_input"
95	            />
96	          </div>
97	          <div className="form_buttons">
98	            <Button
99	              onClick={() => doUserLogIn()}
100	              type="primary"
101	              className="form_button"
102	              color={'#208AEC'}
103	              size="large"
104	              block
105	            >
106	              Log In
107	            </Button>
108	          </div>
109	          <Divider />
110	          <div className="login-social">
111	            <div className="login-social-item login-social-item--facebook">
112	              <img className="login-social-item__image" src={'https://findicons.com/files/icons/2830/clean_social_icons/250/facebook.png'} alt=""/>
113	            </div>
114	            <div className="login-social-item">
115	              <img className="login-social-item__image" src={'data:image/png;base64,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'} alt=""/>
116	            </div>
117	            <div className="login-social-item">
118	              <img className="login-social-item__image" src={'data:image/png;base64,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'} alt=""/>
119	            </div>
120	          </div>
121	          <p className="form__hint">Don't have an account? <a className="form__link" href="#">Sign up</a></p>
122	        </div>
123	      )}
124	      {currentUser !== null &&
125	        (<div className="container">
126	          <h2 className="heading">{'User Screen'}</h2>
127	          <Divider />
128	          <h2 className="heading">{`Hello ${currentUser.get('username')}!`}</h2>
129	          <div className="form_buttons">
130	            <Button
131	              onClick={() => doUserLogOut()}
132	              type="primary"
133	              className="form_button"
134	              color={'#208AEC'}
135	              size="large"
136	            >
137	              Log Out
138	            </Button>
139	          </div>
140	        </div>)
141	      }
142	    </div>
143	  );
144	};
```
:::

## Conclusion

At the end of this guide, you learned how to log in and log out Parse users on React. In the next guide, we will show you how to perform useful user queries.
