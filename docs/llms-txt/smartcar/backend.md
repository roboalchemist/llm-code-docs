# Source: https://smartcar.com/docs/getting-started/tutorials/backend.md

# Backend SDK Tutorials

> In this tutorial, we will go over how to integrate Connect into your application and make requests to a vehicle using our backend SDKs.

# Overview

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/backend-sdks/overview.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c14eeafc1d4ff0ae02482d59c66d451e" data-og-width="850" width="850" data-og-height="491" height="491" data-path="images/backend-sdks/overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/backend-sdks/overview.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a750458073489eac8055cdb934501cff 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/backend-sdks/overview.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=07bb6214d5299d1307fac596f1f9ed62 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/backend-sdks/overview.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=92e3e33f2a10f43968b4b54283aaf562 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/backend-sdks/overview.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=d6e7165c1893d87298c28e6c66fef71d 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/backend-sdks/overview.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=6804f3ac4768b14e517fb07c3448ca6a 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/backend-sdks/overview.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=bacb0ca36a1b1a5f5c91a6ef0bfb06cc 2500w" />
</Frame>

<br />

1. The Application redirects the user to Smartcar Connect to request access to the user’s vehicle. In Connect,
   the user logs in with their vehicle credentials and grants the Application access to their vehicle.
2. The user’s browser is redirected to a specified `REDIRECT_URI`. The Application Server, which is listening
   at the `REDIRECT_URI`, will retrieve the authorization code from query parameters sent to the `REDIRECT_URI`.
3. The Application sends a request to the Smartcar API. This request contains the authorization `code` along with
   the Application’s `CLIENT_ID` and `CLIENT_SECRET`.
4. In response, Smartcar returns an `ACCESS_TOKEN` and a `REFRESH_TOKEN`.
5. Using the `ACCESS_TOKEN`, the Application can now send requests to the Smartcar API. It can access protected resources and send commands
   to and from the user’s vehicle via the backend service.

# Prerequisites

* [Sign up](https://dashboard.smartcar.com/signup) for a Smartcar account.
* Make a note of your `CLIENT_ID` and `CLIENT_SECRET` from the **Configuration** section on the Dashboard.
* Add the following `REDIRECT_URI` to your application configuration: `http://localhost:8000/exchange`

# Setup

1. Clone the repo for the SDK you want to use and install the required dependencies:
   <CodeGroup>
     ```bash Node theme={null}
     $ git clone https://github.com/smartcar/getting-started-express.git
     $ cd getting-started-express/tutorial
     $ npm install
     ```

     ```bash Python theme={null}
     $ git clone https://github.com/smartcar/getting-started-python-sdk.git
     $ cd getting-started-python-sdk/tutorial
     $ pip install -r requirements.txt
     ```

     ```bash Java theme={null}
     $ git clone https://github.com/smartcar/getting-started-java-sdk.git
     $ cd getting-started-java-sdk/tutorial
     $ gradlew build
     ```

     ```bash Ruby theme={null}
     $ git clone https://github.com/smartcar/getting-started-ruby-sdk.git
     $ cd getting-started-ruby-sdk/tutorial
     $ bundle install
     $ ruby app.rb
     ```
   </CodeGroup>
2. You will also have to set the following environment variables

<Warning>
  If you've used one of our frontend SDKs to integrate connect, you'll want to set the
  `SMARTCAR_REDIRECT_URI` environment variable to the URI you used for that application.
</Warning>

```bash  theme={null}
$export SMARTCAR_CLIENT_ID=<your-client-id>
$export SMARTCAR_CLIENT_SECRET=<your-client-secret>
$export SMARTCAR_REDIRECT_URI=http://localhost:8000/exchange
```

<Note>
  If you are using Windows, ensure you are appropriately setting environment variables for your shell.
  Please refer to [this post](https://stackoverflow.com/questions/9249830/how-can-i-set-node-env-production-on-windows/9250168#9250168) which details how to set environment variables on Windows.
</Note>

<br />

# Build your Connect URL

1. Instantiate a `Smartcar` object in the constructor of the App component.
   <CodeGroup>
     ```js index.js theme={null}
     const client = new smartcar.AuthClient({
         mode: 'simulated',
     });
     ```

     ```python main.py theme={null}
     client = smartcar.AuthClient(mode='simulated')
     ```

     ```java Main.java theme={null}
     String mode = "simulated";

     AuthClient client = new AuthClient.Builder()
     .mode(mode)
     .build();
     ```

     ```ruby index.rb theme={null}
     @@client = Smartcar::AuthClient.new({
         mode: 'simulated',
     })
     ```
   </CodeGroup>

<Info>
  Feel free to set `mode` to `simulated` or `live` where you instantiate your `Smartcar` object to
  connect to a simulated or real vehicle.
</Info>

2. A Server-side rendered application will redirect to Smartcar Connect to request access to a user’s vehicle.
   On Connect, the user logs in with the username and password for their vehicle’s connected services account
   and grants the application access to their vehicle.

   To launch Connect, we need to redirect the user to the appropriate URL. We can make use of the `AUTHORIZATION_URL`
   function in our Smartcar object and redirect the user to the URL to launch the Connect flow.

   <CodeGroup>
     ```js index.js theme={null}
     app.get('/login', function(req, res) {
         const scope = ['read_vehicle_info'];
         const authUrl = client.getAuthUrl(scope);

         res.render('home', {
             url: authUrl,
         });
     });
     ```

     ```python main.py theme={null}
     @app.route('/login', methods=['GET'])
     def login():
         scope = ['read_vehicle_info']
         auth_url = client.get_auth_url(scope)
         return redirect(auth_url)        
     ```

     ```java Main.java theme={null}
     get("/login", (req, res) -> {
         // TODO: Authorization Step 2: Launch Smartcar authentication dialog
         String[] scope = {"read_odometer"};
         String link = client.authUrlBuilder(scope).build();
         res.redirect(link);
         return null;
     });
     ```

     ```ruby index.rb theme={null}
     get "/login" do
         redirect @@client.get_auth_url(['required:read_vehicle_info'])
     end
     ```
   </CodeGroup>

<br />

# Handle the response

Once a user has authorized the application to access their vehicle, the user is redirected to the `REDIRECT_URI`
with an authorization `code` as a query parameter. In the previous section, we had set our `REDIRECT_URI` as `localhost:8000/exchange`.
Now, our server can be set up as follows to receive the authorization `code`.

<CodeGroup>
  ```js index.js theme={null}
  app.get('/exchange', function(req, res) {
  const code = req.query.code;

  console.log(code);

  res.sendStatus(200);
  });
  ```

  ```python main.py theme={null}
  @app.route('/exchange', methods=['GET'])
  def exchange():
      code = request.args.get('code')
      
      print(code)
      
      return '', 200      
  ```

  ```java Main.java theme={null}
  get("/exchange", (req, res) -> {
      String code = req.queryMap("code").value();

      System.out.println(code);

      return "";
  });
  ```

  ```ruby index.rb theme={null}
  get "/exchange" do
      code = params[:code]

      puts code

      "OK"
  end
  ```
</CodeGroup>

<br />

# Launching Connect

Let’s try authenticating a vehicle! Restart your server, open up your browser and go to `http://localhost:8000/login`

<CodeGroup>
  ```bash Node theme={null}
  $node index.js
  ```

  ```bash Python theme={null}
  $python main.py
  ```

  ```bash Java theme={null}
  $./gradlew run
  ```

  ```bash Ruby theme={null}
  $bundle exec ruby app.rb
  ```
</CodeGroup>

<br />

<Info>
  This tutorial configures Connect to launch in `test` mode by default.
  In `test` mode, any `username` and `password` is valid for each brand.
</Info>

Smartcar showcases all the permissions your application is asking for - `read_vehicle_info` in this case.
Once you have logged in and accepted the permissions, you should see your authorization `code` printed to your console.

<br />

# Getting your first access token

<Note>
  If you've used one of our frontend SDKs to integrate Connect, this is where you'll need to fetch your access token.
</Note>

In the previous section, we retrieved an authorization `code`. The application must exchange the code for an `ACCESS_TOKEN` to make a request.
After receiving the ACCESS\_TOKEN, the user can be redirected to the `/vehicle` route.

<CodeGroup>
  ```js index.js theme={null}
  // Global variable to save our access_token
  let access;

  app.get('/exchange', async function(req, res) {
      const code = req.query.code;
      
      // Access our global variable and store our access tokens.
      // In a production app you'll want to store this in some 
      // kind of persistent storage
      access = await client.exchangeCode(code);
      res.redirect('/vehicle');
  });
  ```

  ```python main.py theme={null}
  # Global variable to save our access_token
  access = None

  @app.route('/exchange', methods=['GET'])
  def exchange():
      code = request.args.get('code')

      # Access our global variable and store our access tokens.
      # In a production app you'll want to store this in some
      # kind of persistent storage
      global access

      access = client.exchange_code(code)
      return redirect('/vehicle')      
  ```

  ```java Main.java theme={null}
  // Global variable to save our access_token
  private static String access;

  public static void main(String[] args) {

      get("/exchange", (req, res) -> {
          String code = req.queryMap("code").value();

          Auth auth = client.exchangeCode(code);
          
          // Access our global variable and store our access tokens.
          // In a production app you'll want to store this in some kind of persistent storage
          access = auth.getAccessToken();
          
          res.redirect("/vehicle");
          return null;
      })
  }
  ```

  ```ruby index.rb theme={null}
  # Global variable to store the token
  @@token = ''

  get "/exchange" do
      code = params[:code]
      # Access our global variable and store our access tokens.
      # In a production app you'll want to store this in 
      # some kind of persistent storage
      @@token = @@client.exchange_code(code)[:access_token]
      redirect '/vehicle'
  end
  ```
</CodeGroup>

<br />

# Getting data from a vehicle

1. Once the backend service or server-side application has the `ACCESS_TOKEN`, it can send requests to a vehicle using the Smartcar API.
   First we'll need to fetch the `vehicle_id`s associated with the `ACCESS_TOKEN`, then fetch vehicle attributes for one of them. After
   receiving the `vehicle_attributes` object, we can render it in a simple table on the page.
   <CodeGroup>
     ```js index.js theme={null}
     app.get('/vehicle', async function(req, res) {
         // Get the smartcar vehicleIds associated with the access_token
         const { vehicles } = await smartcar.getVehicles(access.accessToken);
         
         // Instantiate the first vehicle in the vehicle id list
         const vehicle = new smartcar.Vehicle(vehicles[0], access.accessToken);

         // Make a request to Smartcar API
         const attributes = await vehicle.attributes();
         res.render('vehicle', {
             info: attributes, 
         });
     });
     ```

     ```python main.py theme={null}
     @app.route('/vehicle', methods=['GET'])
     def get_vehicle():
         # Access our global variable to retrieve our access tokens
         global access
         
         # Get the smartcar vehicleIds associated with the access_token
         vehicles = smartcar.get_vehicles(access.access_token)
         vehicle_ids = vehicles.vehicles
         
         # Instantiate the first vehicle in the vehicle id list
         vehicle = smartcar.Vehicle(vehicle_ids[0], access.access_token)

         # Make a request to Smartcar API
         attributes = vehicle.attributes()
         return jsonify({
             "make": attributes.make,
             "model": attributes.model,
             "year": attributes.year    
         })
         '''
         {
             "make": "TESLA",
             "model": "Model S",
             "year": 2014
         }
         '''
     ```

     ```java Main.java theme={null}
     get("/vehicle", (req, res) -> {

         // Get the smartcar vehicleIds associated with the access_token
         VehicleIds vehiclesResponse = Smartcar.getVehicles(access);
         String[] vehicleIds = vehiclesResponse.getVehicleIds();
         
         // Instantiate the first vehicle in the vehicle id list
         Vehicle vehicle = new Vehicle(vehicleIds[0], access);

         // Make a request to Smartcar API
         VehicleAttributes attributes = vehicle.attributes();
         System.out.println(gson.toJson(attributes));
         
         // {
         //     "id": "36ab27d0-fd9d-4455-823a-ce30af709ffc",
         //     "make": "TESLA",
         //     "model": "Model S",
         //     "year": 2014
         // }
         
         res.type("application/json");
         return gson.toJson(attributes);
     })
     ```

     ```ruby index.rb theme={null}
     get "/vehicle" do
         code = params[:code]

         # Get the smartcar vehicleIds associated with the access_token
         vehicles =  Smartcar::Vehicle.get_vehicle(token: @@token)
         vehicle_ids = vehicles.vehicles
         
         # Instantiate the first vehicle in the vehicle id list
         vehicle = Smartcar::Vehicle.new(token: @@token, id: vehicle_ids.first)  
         
         # Get the vehicle_attributes object for vehicle
         vehicle_attributes = vehicle.attributes
         vehicle_attributes.slice(*%I(id make model year)).to_json
     end
     ```
   </CodeGroup>

2. Restart your sever and head back to `http://localhost:8000/login` to go through Connect and make your first API request!
   <CodeGroup>
     ```bash Node theme={null}
     $node index.js
     ```

     ```bash Python theme={null}
     $python main.py
     ```

     ```bash Java theme={null}
     $./gradlew run
     ```

     ```bash Ruby theme={null}
     $bundle exec ruby app.rb
     ```
   </CodeGroup>
