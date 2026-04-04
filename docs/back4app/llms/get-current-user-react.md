# Source: https://docs-containers.back4app.com/docs/react/working-with-users/get-current-user-react.md

---
title: Current User
slug: docs/react/working-with-users/get-current-user-react
description: In this guide you will learn how to fetch the current user in Parse on React
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T17:19:37.911Z
updatedAt: 2025-01-16T20:27:04.148Z
---

# Get current User for React

## Introduction

After implementing user registration and login to your, you need to retrieve the currently logged user data to perform different actions and requests. This data can be promptly retrieved by using Parse.User.current inside your app components.

## Prerequisites

:::hint{type="info"}
To complete this tutorial, you will need:

-
  A React App created and [**connected to Back4App**](https://www.back4app.com/docs/react/quickstart).
- Complete the previous guide so you can have a better understanding of [**the Parse.User class and the Parse.User.logIn method**](https://www.back4app.com/docs/react/working-with-users/react-user-login)
- If you want to test/use the screen layout provided by this guide, you should set up the [**&#x20;library.**](https://ant.design/docs/react/introduce)
:::

## Goal

Get the current user data fetching using Parse for a React app.

## 1 - Retrieving Current User

The method Parse.User.current can be used anywhere on your code, after properly configuring your app to use Parse. Its response will be your current user’s object (Parse.User) or null if there is no logged-in user currently.

:::CodeblockTabs
JavaScript

```javascript
1	const getCurrentUser = async function () {
2	  const currentUser = await Parse.User.current();
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
1	const getCurrentUser = async function (): Promise<Parse.User | null> {
2	  const currentUser: Parse.User = await Parse.User.current();
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

## 2 - Using Current User in a React component

In our previous guides, the Parse.User.current method was already used for testing showing the current username on the User Login guide. Here is the UserLogin component code, take a closer look at the getCurrentUser function:

:::CodeblockTabs
UserLogin.js

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
106	            >
107	              Log In
108	            </Button>
109	          </div>
110	        </div>
111	      )}
112	      {currentUser !== null && (
113	        <div className="container">
114	          <h2 className="heading">{'User Screen'}</h2>
115	          <Divider />
116	          <h2 className="heading">{`Hello ${currentUser.get('username')}!`}</h2>
117	          <div className="form_buttons">
118	            <Button
119	              onClick={() => doUserLogOut()}
120	              type="primary"
121	              className="form_button"
122	              color={'#208AEC'}
123	              size="large"
124	            >
125	              Log Out
126	            </Button>
127	          </div>
128	        </div>
129	      )}
130	    </div>
131	  );
132	};
```

HelloUser.tsx

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
76	      {currentUser === null &&
77	        (<div className="container">
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
104	            >
105	              Log In
106	            </Button>
107	          </div>
108	        </div>)
109	      }
110	      {currentUser !== null &&
111	        (<div className="container">
112	          <h2 className="heading">{'User Screen'}</h2>
113	          <Divider />
114	          <h2 className="heading">{`Hello ${currentUser.get('username')}!`}</h2>
115	          <div className="form_buttons">
116	            <Button
117	              onClick={() => doUserLogOut()}
118	              type="primary"
119	              className="form_button"
120	              color={'#208AEC'}
121	              size="large"
122	            >
123	              Log Out
124	            </Button>
125	          </div>
126	        </div>)
127	      }
128	    </div>
129	  );
130	};
```
:::

In this component, the Parse.User.current method retrieves the username and updates the state variable that is rendered inside the component JSX.

Add these classes to your App.css file to fully render the layout styles:

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
96	  border-bottom: 1px solid rgba(0,0,0,0.06);
97	  text-align: left;
98	}
99	
100	.list_item_title {
101	  color: rgba(0,0,0,0.87);
102	  font-size: 17px;
103	}
104	
105	.list_item_description {
106	  color: rgba(0,0,0,0.5);
107	  font-size: 15px;
108	}
```
:::

## Conclusion

At the end of this guide, you learned how to retrieve the current Parse user data from local storage on React. In the next guide, we will show you how to enable your user to reset his password.
