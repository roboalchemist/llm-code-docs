# Source: https://firebase.google.com/docs/remote-config/server-side-rendering-web-apps.md.txt

To provide maximum flexibility, FirebaseRemote Configsupports both client-side and server-side SDK integrations for web applications. This means your app can:

- **Fetch and evaluateRemote Configtemplates on your server:** Your server can download theRemote Configtemplate and evaluate targeting conditions directly.
- **Optimize initial page load performance:**For server-side rendering scenarios, the server can provide the evaluated configuration to the client during the initial page load. This improves performance by delivering the necessary configuration data upfront.

| **Important:** The focus of this capability is on the server-side evaluation. Client-side evaluation is not supported.

This approach empowers you to manage your app's behavior and configuration dynamically, particularly in server-side rendering setups.

## Set up server-side rendering for your apps

To configure server-side rendering withRemote Configin your web app, update your client and server apps using the steps that follow.

### Step 1: Update your server-side application

In your server app, where you implemented the Firebase Admin Node.js SDK, include a`RemoteConfigFetchResponse`class that accepts the existing[`ServerConfig`](https://github.com/firebase/firebase-admin-node/blob/a6a930c0cec994f61ca1f4d2f75a5c74144e19e4/src/remote-config/remote-config-api.ts#L685). You can use this to serialize config values that can be passed to your client.  


    export default async function MyServerComponent() {
      const serverApp = initializeApp();
      const serverSideConfig = getRemoteConfig(serverApp);
      const template = await serverSideConfig.getServerTemplate();
      const config = template.evaluate({randomizationId: 'some-uuid'});
      const fetchResponse = new RemoteConfigFetchResponse(serverApp, config);

      return (
        <div>
          <MyClientComponent initialFetchResponse={fetchResponse}></MyClientComponent>
        </div>
      );
    }

### Step 2: Update your client app

On your client app, which implements the Firebase Javascript SDK, include an`initialFetchResponse`configuration option to accept the serialized values passed from your server app. This manually hydrates the config state without making an async fetch request.

Additionally, you must include an initialization option that lets you set the`firebase-server`as the`templateId`on the client SDK. This configures the SDK to use the initial server-side template for subsequent fetches, ensuring consistent parameters and conditional values between client and server.  


    export default function MyClientComponent({initialFetchResponse= ''} = {}) {
      const app = initializeApp(firebaseConfig);
      const config = getRemoteConfig(app, {
            templateId: 'firebase-server',
            initialFetchResponse
      });
      const paramValue = getString(config, 'my_rc_parameter_key');

      return (
        <div>{paramValue}</div>
      );
    }