# Source: https://docs.hypermode.com/dgraph/guides/to-do-app/auth0-jwt.md

# Using Auth0

> Get an app running with Auth0. This step in the GraphQL tutorial walks you through using Auth0 in an example to-do app tutorial.

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

<Note>This is part 4 of [Building a To-Do List App](./introduction).</Note>

Let's start by going to our Auth0 dashboard where we can see the app which we
have already created and used in our frontend-app.

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/dashboard.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=8dc16d74e480f1d62245af52ceba8eae" alt="Dashboard" width="3584" height="1790" data-path="images/dgraph/guides/to-do-app/dashboard.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/dashboard.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=13540cbe3917629df38b7a7e46774a89 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/dashboard.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=ff9bda1d96b4e8f470b0589eb243e90c 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/dashboard.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=09e28ef926437037a6fe86a8d5aa5234 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/dashboard.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=c8fbb839318dfdd80ff1b428683e3582 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/dashboard.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=65f61fbb8ab0a78c48d9c14467286f44 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/dashboard.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=b6afe163e0e9a5bfd837f36f7e325856 2500w" data-optimize="true" data-opv="2" />

Now we want to use the JWT that Auth0 generates, but we also need to add custom
claims to that token which will be used by our auth rules. So we can use
something known as "Rules" (left sidebar on dashboard page under "Auth
Pipeline") to add custom claims to a token. Let's create a new empty rule.

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/rule.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=f3bb054e4a006da7c9623856644dd825" alt="Rule" width="3584" height="1790" data-path="images/dgraph/guides/to-do-app/rule.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/rule.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=ddc91d107cf29ab91276c7177892343c 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/rule.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=8c3d652d8d95b6a5a92a5343a090c93e 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/rule.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=8dec7da88f687c31139540d196074ebb 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/rule.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=891b325bf2632807723165a271d6c3d0 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/rule.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=3e4e7498214697306fb4f7a8ddfadb1e 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/rule.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=09973271fba063ab0a3f4fa5325429eb 2500w" data-optimize="true" data-opv="2" />

Replace the content with the following -

```javascript
function (user, context, callback) {
  const namespace = "https://dgraph.io/jwt/claims";
  context.idToken[namespace] =
    {
      'USER': user.email,
    };

  return callback(null, user, context);
}
```

In the above function, we are only just adding the custom claim to the token
with a field as `USER` which if you recall from the last step is used in our
auth rules, so it needs to match exactly with that name.

Now let's go to `Settings` of our Auth0 app and then go down to view the
`Advanced Settings` to check the JWT signature algorithm (OAuth tab) and then
get the certificate (Certificates tab). We will be using `RS256` in this example
so let's make sure it's set to that and then copy the certificate which we will
use to get the public key. Use the download certificate button there to get the
certificate in `PEM`.

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/certificate.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=10c318d59a61243a2524eae2e82ee802" alt="Certificate" width="3584" height="1792" data-path="images/dgraph/guides/to-do-app/certificate.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/certificate.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=b1dbf820bf5323e684a70ef6a2ead8f1 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/certificate.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=16c9f62da89fd2ecbadc2f043c5376c9 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/certificate.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=4cc39b38751a61b403c6dd0794db8c80 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/certificate.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=480292c96c12831bdbb5f359b69d843e 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/certificate.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=9cb6a6fd8ea65e8c3ec772d9033523f7 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/certificate.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=19f47b2ad98f8bbb809d7493271a68ee 2500w" data-optimize="true" data-opv="2" />

Now let's run a command to get the public key from it, which we will add to our
schema. Just change the `file_name` and run the command.

```
openssl x509 -pubkey -noout -in file_name.pem
```

Copy the public key and now let's add it to our schema. For doing that we will
add something like this, to the bottom of our schema file -

```
# Dgraph.Authorization {"VerificationKey":"<AUTH0-APP-PUBLIC-KEY>","Header":"X-Auth-Token","Namespace":"https://dgraph.io/jwt/claims","Algo":"RS256","Audience":["<AUTH0-APP-CLIENT-ID>"]}
```

Let me just quickly explain what each thing means in that, so firstly we start
the line with a `#  Dgraph.Authorization`. Next is the `VerificationKey`, so
update `<AUTH0-APP-PUBLIC-KEY>` with your public key within the quotes and make
sure to have it in a single line and add `\n` where ever needed. Then set
`Header` to the name of the header `X-Auth-Token` (can be anything) which will
be used to send the value of the JWT. Next is the `Namespace` name
`https://dgraph.io/jwt/claims` (again can be anything, just needs to match with
the name specified in Auth0). Then next is the `Algo` which is `RS256`, the JWT
signature algorithm (another option is `HS256` but remember to use the same
algorithm in Auth0). Then for the `Audience`, add your app's Auth0 client ID.

The updated schema will look something like this (update the public key with
your key) -

```graphql
type Task
  @auth(
    query: {
      rule: """
      query($USER: String!) {
          queryTask {
              user(filter: { username: { eq: $USER } }) {
                  __typename
              }
          }
      }
      """
    }
  ) {
  id: ID!
  title: String! @search(by: [fulltext])
  completed: Boolean! @search
  user: User!
}
type User {
  username: String! @id @search(by: [hash])
  name: String
  tasks: [Task] @hasInverse(field: user)
}
# Dgraph.Authorization {"VerificationKey":"<AUTH0-APP-PUBLIC-KEY>","Header":"X-Auth-Token","Namespace":"https://dgraph.io/jwt/claims","Algo":"RS256","Audience":["<AUTH0-APP-CLIENT-ID>"]}
```

Resubmit the updated schema -

```
curl -X POST localhost:8080/admin/schema --data-binary '@schema.graphql'
```

Let's get that token and see what all it contains, then update the frontend
accordingly. For doing this, let's start our app again.

```
npm start
```

Now open a browser window, navigate to
[http://localhost:3000](http://localhost:3000) and open the developer tools, go
to the `network` tab and find a call called `token` to get your JWT from its
response JSON (field `id_token`).

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/token.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=e2cbb27bdd2ba2e2f27e72c82fe4d754" alt="Token" width="854" height="355" data-path="images/dgraph/guides/to-do-app/token.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/token.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=51791331e30aad00e325a4d80944efbf 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/token.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=f66a3531854d459eea2bc95fd6335e54 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/token.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=14f11f01200c3b06da156595c68fbe1a 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/token.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=7b900783364e682a2b219e28ecb00372 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/token.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=a285b516d824d5d2120c87d25c4b07e3 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/token.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=f81b7adb3e8af28c983f8a90451a83a5 2500w" data-optimize="true" data-opv="2" />

Now go to [jwt.io](https://jwt.io) and paste your token there.

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/jwt.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=0264e1df1d23ea38da0ddf43bd369db5" alt="jwt" width="854" height="439" data-path="images/dgraph/guides/to-do-app/jwt.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/jwt.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=a36fb7ae1ba3c897fbb2923f4752bcc0 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/jwt.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=ab98f8066e1c757fe87207b8bfede452 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/jwt.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=20d8c0b646fcf61696aafec599c8b737 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/jwt.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=085ca389b674f47fa37a904a2a4e1d1d 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/jwt.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=264c39043c27f4af7a1600ca8fffe3c0 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/jwt.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=82784e5377c0bc86c93fa8681b95a518 2500w" data-optimize="true" data-opv="2" />

The token also includes our custom claim like below.

```json
{
"https://dgraph.io/jwt/claims": {
    "USER": "vardhanapoorv"
  },
  ...
}
```

Now, you can check if the auth rule that we added is working as expected or not.
Open the GraphQL tool (Insomnia, GraphQL Playground) add the URL along with the
header `X-Auth0-Token` and its value as the JWT. Let's try the query to see the
todos and only the todos the logged-in user created should be visible.

```graphql
query {
  queryTask {
    title
    completed
    user {
      username
    }
  }
}
```

The above should give you only your todos and verifies that our auth rule
worked!

Now let's update our frontend app to include the `X-Auth0-Token` header with
value as JWT from Auth0 when sending a request.

To do this, we need to update the Apollo client setup to include the header
while sending the request, and we need to get the JWT from Auth0.

The value we want is in the field `idToken` from Auth0. We get that by quickly
updating `react-auth0-spa.js` to get `idToken` and pass it as a prop to our
`App`.

```javascript
...

const [popupOpen, setPopupOpen] = useState(false);
const [idToken, setIdToken] = useState("");

...

if (isAuthenticated) {
        const user = await auth0FromHook.getUser();
        setUser(user);
        const idTokenClaims = await auth0FromHook.getIdTokenClaims();
        setIdToken(idTokenClaims.__raw);
}

...

const user = await auth0Client.getUser();
const idTokenClaims = await auth0Client.getIdTokenClaims();

setIdToken(idTokenClaims.__raw);

...

{children}
      <App idToken={idToken} />
    </Auth0Context.Provider>

...

```

Check the updated file
[here](https://github.com/dgraph-io/graphql-sample-apps/blob/c94b6eb1cec051238b81482a049100b1cd15bbf7/todo-app-react/src/react-auth0-spa.js)

Now let's use that token while creating an Apollo client instance and give it to
a header `X-Auth0-Token` in our case. Let's update our `src/App.js` file.

```javascript
...

import { useAuth0 } from "./react-auth0-spa";
import { setContext } from "apollo-link-context";

// Updated to take token
const createApolloClient = token => {
  const httpLink = createHttpLink({
    uri: config.graphqlUrl,
    options: {
      reconnect: true,
    },
});

// Add header
const authLink = setContext((_, { headers }) => {
    // return the headers to the context so httpLink can read them
    return {
      headers: {
        ...headers,
        "X-Auth-Token": token,
      },
    };
});

// Include header
return new ApolloClient({
    link: httpLink,
    link: authLink.concat(httpLink),
    cache: new InMemoryCache()
});

// Get token from props and pass to function
const App = ({idToken}) => {
  const { loading } = useAuth0();
  if (loading) {
    return <div>Loading...</div>;
  }
const client = createApolloClient(idToken);

...
```

Check the updated file
[here](https://github.com/dgraph-io/graphql-sample-apps/blob/c94b6eb1cec051238b81482a049100b1cd15bbf7/todo-app-react/src/App.js).

Refer this step in
[GitHub](https://github.com/dgraph-io/graphql-sample-apps/commit/c94b6eb1cec051238b81482a049100b1cd15bbf7).

Let's now start the app.

```
npm start
```

Now you should have an app running with Auth0!
