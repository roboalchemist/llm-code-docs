# Source: https://smartcar.com/docs/getting-started/tutorials/ios.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# iOS Tutorial

> In this tutorial, we will use the iOS SDK to integrate Connect into your application.

<Warning>
  Our frontend SDKs handle getting an authorization code representing a vehicle owner's consent for your application to interact with their vehicle
  for the requested permissions. In order to make requests to a vehicle, please use one of our [backend SDKs](/api-reference/api-sdks).

  For security, token exchanges and requests to vehicles **should not** be made client side.
</Warning>

<br />

# Overview

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/overview.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=45bac644e60e25a9e5a92a550e398f37" data-og-width="850" width="850" data-og-height="510" height="510" data-path="images/ios/overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/overview.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=a61885111dee58865db17980113e5035 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/overview.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=b8651a42e98db8d2eab1c451f37f6995 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/overview.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=bdc2acc2ab6a04e66c4717359d4aa74b 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/overview.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=ac8a17905c843637daf985634c01cf76 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/overview.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=cf6a43d011422f21f72e89fc7422fcef 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/overview.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=2e1b4272ed0a314b03128f615747b033 2500w" />
</Frame>

<br />

1. The Mobile Application launches a `SafariView` with Smartcar Connect to request access to a user’s vehicle.
   On Connect, the user logs in with their vehicle credentials and grants the Application access to their vehicle.
2. The `SafariView` is redirected to a specified `REDIRECT_URI` along with an authorization `code`.
   This will be the custom scheme set on the application. The Smartcar iOS SDK receives the authorization `code` in a view listening
   for the specified custom scheme URI, and passes it to the Mobile Application.
3. The Mobile Application sends the received authorization `code` to the Application’s back-end service.
4. The Application sends a request to the Smartcar API. This request contains the authorization code along with the Application’s
   `CLIENT_ID` and `CLIENT_SECRET`.
5. In response, Smartcar returns an `ACCESS_TOKEN` and a `REFRESH_TOKEN`.
6. Using the `ACCESS_TOKEN`, the Application can now send requests to the Smartcar API. It can access protected resources and send commands
   to and from the user’s vehicle via the backend service.

# Prerequisites

* [Sign up](https://dashboard.smartcar.com/signup) for a Smartcar account.
* Make a note of your `CLIENT_ID` and `CLIENT_SECRET` from the **Configuration** section on the Dashboard.
* Add a custom scheme redirect URI to your application configuration.
* Add the `appServer` redirect URI from [step 2](/getting-started/tutorials/ios/#setup) below to your application configuration.

<Note>
  For iOS, we require the custom URI scheme to be in the format of `sc` + `clientId` + `://` + `hostname`.
  For now, you can just set it to `sc` + `clientId` + `://exchange`.

  Please see our [Connect Docs](/connect/dashboard-config#redirect-uris) for more information.
</Note>

# Setup

1. Clone our repo and install the required dependencies:
   ```bash  theme={null}
   $git clone https://github.com/smartcar/getting-started-ios-sdk.git
   $cd getting-started-ios-sdk/tutorial
   $pod install
   $open getting-started-ios-sdk.xcworkspace
   ```
2. Set the following constants in `Constants.swift`. We're setting `appServer` to `http://localhost:8000` to pass the authorization `code` from
   the [Handle the Response](/getting-started/tutorials/ios#handle-the-response) step later on in the tutorial to our backend.
   ```swift Constants.swift theme={null}
   struct Constants {
       static let clientId = "<your-client-id>";
       static let appServer = "http://localhost:8000";
   }
   ```

# Build your Connect URL

Instantiate a `SmartcarAuth` object in the `viewdidLoad` function of the `ViewController`.
The iOS application will launch a `WebView` with Connect to request access to a user’s vehicle.
On Connect, the user logs in with the username and password for their vehicle’s connected services account
and grants the application access to their vehicle.

To launch Connect, we can use the `launchAuthFlow` function that our `SmartcarAuth` object has access to. We can place
this within the `connectPressed` action function.

```swift ViewController.swift theme={null}
let appDelegate = UIApplication.shared.delegate as! AppDelegate

func completionHandler(code: String?, state: String?, virtualKeyUrl: String?, err: AuthorizationError?,) -> Void {
// Receive authorization code
}

appDelegate.smartcar = SmartcarAuth(
  clientId: "afb0b7d3-807f-4c61-9b04-352e91fe3134",
  redirectUri: "scafb0b7d3-807f-4c61-9b04-352e91fe3134://exchange",
  scope: ["read_vin", "read_vehicle_info", "read_odometer"],
  mode: SCMode.simulated, //use SCMode.live to connect to a real vehicles
  completionHandler: completionHandler
)
let smartcar = appDelegate.smartcar

// Generate a Connect URL
let authUrl = smartcar.authUrlBuilder().build()

// Pass in the generated Connect URL and a UIViewController
smartcar.launchAuthFlow(url: authUrl, viewController: viewController)
```

<br />

# Registering your Custom Scheme

Once a user has authorized the application to access their vehicle, the user is redirected to the `REDIRECT_URI` with an authorization code as a query parameter.

iOS applications use custom URI schemes to intercept calls and launch the relevant application. This is defined within the `Info.plist`.

1. Open up `Info.plist` and click on the grey arrow next to **URL types**.
2. Next, click on the grey arrow next to the `Item 0` dictionary and `URL Schemes` array.
3. Finally, set your `Item 0` string to the redirect URI you set up in the [Prerequisites](/getting-started/tutorials/ios#prerequisites) section (i.e. 'sc' + clientId).

<Frame>
  <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/info-plist.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=f44c4b8181efc5f04fd5032a3b22829d" data-og-width="866" width="866" data-og-height="464" height="464" data-path="images/ios/info-plist.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/info-plist.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=811be6c402b564aff3ee32bd8ed317b7 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/info-plist.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=77760fa09f368baac7206da5867b6275 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/info-plist.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=92e4e79d535d84f17f8b7c324bfac253 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/info-plist.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=b33b563596db365cddb46d19c2e87494 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/info-plist.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=09fc68c33c02682e8f352e03b658e193 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/info-plist.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=71e3a80d7430a15c99788daf2ed85b53 2500w" />
</Frame>

<br />

# Handle the response

1. The iOS application will now receive the request in the `application:(_:open:options:)` function within the AppDelegate.
   ```swift AppDelegate.swift theme={null}
   func application(_ application: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
       {/* TODO: Authorization Step 3a: Receive the authorization code */}
       window!.rootViewController?.presentedViewController?.dismiss(animated: true , completion: nil)
       smartcar!.handleCallback(with: url)
       
       return true
   }
   ```
2. Using the iOS SDK, the application can receive the code in the `completion callback` passed into the `SmartcarAuth` object.
   ```swift AppDelegate.swift theme={null}
   func completion(err: Error?, code: String?, state: String?) -> Any {
       {/* TODO: Authorization Step 3b: Receive the authorization code */}
       print(code!);
       {/* prints out the authorization code */}
   }
   ```

# Launching Connect

Build your application in XCode and click on the **Connect your vehicle** button.

<Info>
  This tutorial configures Connect to launch in `test` mode by default.
  In `test` mode, any `username` and `password` is valid for each brand.
</Info>

Smartcar showcases all the permissions your application is asking for - `read_vehicle_info` in this case.
Once you have logged in and accepted the permissions, you should see your authorization `code` printed to your console.

# Getting your first Access Token

After receiving the authorization `code`, your iOS application must exchange it for an `ACCESS_TOKEN`. To do so, we can send
the code to a backend service. Let’s assume our backend service contains an endpoint `/exchange` that receives an authorization `code` as a query parameter and exchanges it for an `ACCESS_TOKEN`.

```swift ViewController.swift theme={null}
// TODO: Obtain an access token
Alamofire.request("\(Constants.appServer)/exchange?code=\(code!)", method: .get)
    .responseJSON {_ in}
```

<Warning>
  Notice that our backend service **does not** return the `ACCESS_TOKEN`.
  This is by design. For security, our frontend should never have access
  to the `ACCESS_TOKEN` and should always be stored in the backend.
</Warning>

# Getting data from a vehicle

Once the backend has the `ACCESS_TOKEN`, it can send requests to a vehicle using the Smartcar API. The iOS app will
have to send a request to the backend service which in turn sends a request to Smartcar. We have to do this because
our frontend **does not** have the `ACCESS_TOKEN`.

Assuming our backend has a `/vehicle` endpoint that returns the information of a user’s vehicle, we can make this query in
our `completion callback` and segue into another `view` to show the returned  vehicle attributes

```swift ViewController.swift theme={null}
func completion(err: Error?, code: String?, state: String?) -> Any {

    // send request to exchange auth code for access token
    Alamofire.request("\(Constants.appServer)/exchange?code=\(code!)", method: .get).responseJSON {_ in

        // TODO: Request Step 2: Get vehicle information
        // send request to retrieve the vehicle info
        Alamofire.request("\(Constants.appServer)/vehicle", method: .get).responseJSON { response in
            print(response.result.value!)
            
            if let result = response.result.value {
                let JSON = result as! NSDictionary
                
                let make = JSON.object(forKey: "make")!  as! String
                let model = JSON.object(forKey: "model")!  as! String
                let year = String(JSON.object(forKey: "year")!  as! Int)
                
                let vehicle = "\(year) \(make) \(model)"
                self.vehicleText = vehicle
                
                self.performSegue(withIdentifier: "displayVehicleInfo", sender: self)
            }
        }
    }
    
    return ""
}
```

# Setting up your backend

Now that our frontend is complete, we will need to create a backend service that contains the logic for the `/exchange` and `/vehicle` endpoints.
You can use any of our backend SDKs below to set up the service starting from the **Obtaining an Access Token** step.

<Note>
  When setting up the environment variables for your  backend SDK, make sure to set `REDIRECT_URI` to the custom scheme
  used for this tutorial i.e. `sc + "clientId" + ://exchange`.
</Note>

<CardGroup cols={4}>
  <Card title="Java" icon="java" href="/getting-started/tutorials/backend#getting-your-first-access-token" icontype="duotone" />

  <Card title="Node.js" href="/getting-started/tutorials/backend#getting-your-first-access-token" icon="node-js" icontype="duotone" />

  <Card title="Python" icon="python" href="/getting-started/tutorials/backend#getting-your-first-access-token" icontype="duotone" />

  <Card title="Ruby" href="/getting-started/tutorials/backend#getting-your-first-access-token" icon="gem" icontype="duotone" />
</CardGroup>
