# Source: https://smartcar.com/docs/getting-started/tutorials/react.md

# React Tutorial

> In this tutorial, we will use the JavaScript SDK to integrate Connect into your application.

<Warning>
  Our frontend SDKs handle getting an authorization code representing a vehicle owner's consent for your application to interact with their vehicle
  for the requested permissions. In order to make requests to a vehicle, please use one of our [backend SDKs](/api-reference/api-sdks).

  For security, token exchanges and requests to vehicles **should not** be made client side.
</Warning>

<br />

# Overview

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/react/overview.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=a030ac9d073b3f69e52e9831b0e41bea" data-og-width="850" width="850" data-og-height="510" height="510" data-path="images/react/overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/react/overview.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=c46752e77889db204b1930062db34936 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/react/overview.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=c1d3d7adcbc35bc127407083157060bc 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/react/overview.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=6d9ee3d46aee7f0663736122763c1dba 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/react/overview.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=60875fcb463a344e1015b1ec771ae261 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/react/overview.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=f2e679d7bbf21c310786a5897d70504f 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/react/overview.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=ed5d7cecf987432ab8992b387ab6d6eb 2500w" />
</Frame>

<br />

1. The Single-Page Application launches a pop-up window with Smartcar Connect to request access to a user’s vehicle.
   It does so by using the Smartcar JavaScript SDK. On Connect, the user logs in with the username and password for
   their vehicle’s connected services account and grants the Application access to their vehicle.
2. The user’s browser is redirected to a specified Smartcar-hosted `REDIRECT_URI` - the Smartcar JavaScript SDK redirect page.
3. The Smartcar JavaScript SDK redirect page will receive an authorization `code` as a query parameter. The redirect page will then
   send the code to the Single-Page Application’s `onComplete` callback using the `postMessage` web API. **This step is handled entirely
   by the JavaScript SDK.**
4. The Single-Page Application sends the received authorization `code` to the Application’s backend service.
5. The Application sends a request to the Smartcar API. This request contains the authorization code along with the Application’s
   `CLIENT_ID` and `CLIENT_SECRET`.
6. In response, Smartcar returns an `ACCESS_TOKEN` and a `REFRESH_TOKEN`.
7. Using the `ACCESS_TOKEN`, the Application can now send requests to the Smartcar API. It can access protected resources and send commands
   to and from the user’s vehicle via the backend service.

# Prerequisites

* [Sign up](https://dashboard.smartcar.com/signup) for a Smartcar account.
* Make a note of your `CLIENT_ID` and `CLIENT_SECRET` from the **Configuration** section on the Dashboard.
* Add the special JavaScript SDK redirect URI to your application configuration.
* Add the `REACT_APP_SERVER` redirect URI from [Setup step 2.](/getting-started/tutorials/react#setup) to your application configuration.

<Note>
  To use the JavaScript SDK, we require the special redirect URI to provide a simpler flow to retrieve authorization codes.
  For this tutorial you can use the following:

  `https://javascript-sdk.smartcar.com/v2/redirect?app_origin=http://localhost:3000`
</Note>

# Setup

1. Clone our repo and install the required dependencies:
   ```bash  theme={null}
   $git clone https://github.com/smartcar/getting-started-javascript-sdk-react.git
   $cd getting-started-javascript-sdk-react/tutorial
   $npm install
   ```
2. Set the following environment variables. We will be setting up a server later for our React front-end to communicate with.
   For now, let’s assume our server is listening on `http://localhost:8000`.
   ```bash  theme={null}
   $export REACT_APP_CLIENT_ID=<your-client-id>
   $export REACT_APP_REDIRECT_URI= https://javascript-sdk.smartcar.com/v2/redirect?app_origin=http://localhost:3000
   $export REACT_APP_SERVER=http://localhost:8000
   ```

<Note>
  Note: If you are using Windows, ensure you are appropriately setting environment variables for your shell.
  Please refer to this post which details how to set environment variables on Windows.
</Note>

# Build your Connect URL

1. Instantiate a `Smartcar` object in the `constructor` of the App component.
   ```js App.jsx theme={null}
   constructor(props) {
   ...
   // TODO: Authorization Step 1: Initialize the Smartcar object
   this.smartcar = new Smartcar({
       clientId: process.env.REACT_APP_CLIENT_ID,
       redirectUri: process.env.REACT_APP_REDIRECT_URI,
       scope: ['required:read_vehicle_info'],
       mode: 'test',
       onComplete: this.onComplete,
   });
   }
   ```

<Snippet file="tutorials/info-mode-callout.mdx" />

2. A single-page application will launch a pop-up window with Smartcar Connect to request access to a user’s vehicle.
   On Connect, the user logs in with the username and password for their vehicle’s connected services account and grants
   the application access to their vehicle.

   To launch Connect, we can use the `openDialog` function that our `Smartcar` object has access to. We can place this is
   an `onClick` handler of an HTML button.

   ```js App.jsx theme={null}
   authorize() {
       // TODO: Authorization Step 2a: Launch Connect
       this.smartcar.openDialog({forcePrompt: true});
   }

   render() {
       // TODO: Authorization Step 2b: Render the Connect component
       return <Connect onClick={this.authorize} />;
   }
   ```

# Handle the response

1. Once a user has authorized the application to access their vehicle, the user is redirected to the `redirect_uri` with an
   authorization code as a query parameter and the pop-up dialog is closed. Using the JavaScript SDK, the frontend can
   receive this `code` in the `onComplete` callback passed into the `Smartcar` object.
   ```js App.jsx theme={null}
   onComplete(err, code, status) {
       //TODO: Authorization Step 3: Receive the authorization code
       console.log(code);
       //prints out the authorization code
   };
   ```

# Launching Connect

Restart your server, open up your browser and go to `http://localhost:3000/login`. You should be reciderect to Smartcar Connect.

<Info>
  This tutorial configures Connect to launch in `test` mode by default.
  In `test` mode, any `username` and `password` is valid for each brand.
</Info>

Smartcar showcases all the permissions your application is asking for - `read_vehicle_info` in this case.
Once you have logged in and accepted the permissions, you should see your authorization `code` printed to your console.

# Getting your first access token

After receiving the authorization code, the React application must exchange it for an `ACCESS_TOKEN`. To do so, we can send
the code to the backend service which we will implement in a bit. Until then, let’s assume our backend service contains
an endpoint `/exchange` that receives an authorization code as a query parameter and exchanges it for an `ACCESS_TOKEN`.

We can add this logic in our `onComplete` callback

```js App.jsx theme={null}
onComplete(err, code, status) {
  // TODO: Request Step 1: Obtain an access token
  return axios
    .get(`${process.env.REACT_APP_SERVER}/exchange?code=${code}`);
}

```

# Getting data from a vehicle

Once the back-end has the `ACCESS_TOKEN`, it can send requests to a vehicle using the Smartcar API. The React app will
have to send a request to the backend service which in turn sends a request to Smartcar. We have to do this because
our frontend does not have the `ACCESS_TOKEN`.

Assuming our backend has a `/vehicle` endpoint that returns the information of a user’s vehicle, we can make this query in
our `completion callback` and and set the state of the React app with the returned vehicle attributes.

```js App.jsx theme={null}
onComplete(err, code, status) {
  // TODO: Request Step 2a: Get vehicle information
  return axios
    .get(`${process.env.REACT_APP_SERVER}/exchange?code=${code}`)
    .then(_ => {
      return axios.get(`${process.env.REACT_APP_SERVER}/vehicle`);
    })
    .then(res => {
      this.setState({vehicle: res.data});
    });
}

```

Now that we have the vehicle attributes, we can render a simple Vehicle component that shows the vehicle attributes in a table.

```js App.jsx theme={null}
render() {
  // TODO: Request Step 2b: Get vehicle information
  return Object.keys(this.state.vehicle).length !== 0 ? (
    <Vehicle info={this.state.vehicle} />
  ) : (
    <Connect onClick={this.authorize} />
  );
}
```

# Setting up your backend

Now that our frontend is complete, we will need to create a backend service that contains the logic for the `/exchange` and `/vehicle` endpoints.
You can use any of our backend SDKs below to set up the service starting from the **Obtaining an access token** step.

<Note>
  When setting up the environment variables for your  backend SDK, make sure to set `REDIRECT_URI` to the custom scheme
  used for this tutorial i.e. `https://javascript-sdk.smartcar.com/v2/redirect?app_origin=http://localhost:3000`.
</Note>

<CardGroup cols={4}>
  <Card title="Java" icon="java" href="/getting-started/how-to/architecture-design" icontype="duotone" />

  <Card title="Node.js" href="/getting-started/how-to/architecture-design" icon="node-js" icontype="duotone" />

  <Card title="Python" icon="python" href="/getting-started/how-to/architecture-design" icontype="duotone" />

  <Card title="Ruby" href="/getting-started/how-to/architecture-design" icon="gem" icontype="duotone" />
</CardGroup>
