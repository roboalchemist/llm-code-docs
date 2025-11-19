# Source: https://docs.hypermode.com/dgraph/guides/to-do-app/firebase-jwt.md

# Using Firebase Authentication

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

<Note>This is part 5 of [Building a To-Do List App](./introduction).</Note>

In this step, we will add Firebase authentication per the sample
[Todo app with Firebase Authentication](https://github.com/dgraph-io/graphql-sample-apps/tree/master/todo-react-firebase).

### Create Project

Let's start by going to the
[Firebase console](https://console.firebase.google.com/u/0/project/_/authentication/users?pli=1)
and create a new project (Todo-app).

In the **Authentication** section, enable `Email/Password` login. You can add a
custom domain to `Authorized domains` below according to where you want to
deploy your app. By default localhost is added to the list.

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-domains.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=6746c1dd7d3392549619d1c402d6dcec" alt="Authentication Section" width="842" height="480" data-path="images/dgraph/guides/to-do-app/firebase-domains.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-domains.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=8613866ee74704d7b39f1cb1333b3f7f 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-domains.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=05e781877122a8712b2048c40d43e119 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-domains.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=e9dbefeded9882cb156ced9a0f560994 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-domains.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=e5198d775ef186a340f8e61a6a5ae6f3 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-domains.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=05f1112518cfcce2721ad5c72ffba6a9 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-domains.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=f35d81cefb1a29cca5839b47264c289e 2500w" data-optimize="true" data-opv="2" />

Now we want to use the JWT that Firebase generates, but we also need to add
custom claims to that token which will be used by our authorization rules.

To add custom claims to the JWT we need to host a cloud function which will
insert claims into the JWT on user creation. This is our cloud function which
inserts `USER`: `email` claim under the Namespace
`https://dgraph.io/jwt/claims`.

```javascript
const functions = require("firebase-functions")
const admin = require("firebase-admin")
admin.initializeApp()

exports.addUserClaim = functions.https.onCall((data, context) => {
  return admin
    .auth()
    .getUserByEmail(data.email)
    .then((user) => {
      return admin.auth().setCustomUserClaims(user.uid, {
        "https://dgraph.io/jwt/claims": {
          USER: data.email,
        },
      })
    })
    .then(() => {
      return {
        message: `Success!`,
      }
    })
    .catch((err) => {
      return err
    })
})
```

### Using the Firebase CLI

Clone the Todo Firebase app repo and try to deploy the function to the Firebase
project created above.

```
git clone https://github.com/dgraph-io/graphql-sample-apps.git
cd graphql-sample-apps/todo-react-firebase
npm i
```

* Install the Firebase CLI tool `npm install -g firebase-tools`.
* Login into Firebase from the CLI `firebase login`.
* Run `firebase init functions` then select an existing project (that you
  created above).
* Select language as `JavaScript` for this example.
* Replace `index.js` with the snippet above.
* Deploy the function \`firebase deploy --only functions.

Please refer to the
[deployment guide](https://firebase.google.com/docs/functions/get-started) for
more info.

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-cli.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=7deac772abf354bd5b1af1ded9120c93" alt="Firebase CLI" width="744" height="480" data-path="images/dgraph/guides/to-do-app/firebase-cli.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-cli.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=a695c26684b13d0adb81e6660e4a0ff2 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-cli.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=be52d2a2ae9e5388a2dfd9485b0da136 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-cli.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=e402d3c1d21e3a0f63e5fa4c2f3b8269 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-cli.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=0c575e46f97d48f5413a3ef6f52a6eb1 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-cli.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=f960e2bbcd96d30ff0fb60a0106b8778 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-cli.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=aaacd9a08e12332c21ae71c329e8deb0 2500w" data-optimize="true" data-opv="2" />

### Create Webapp

Create a web app from your Firebase project settings page.

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-create-webapp.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=0e3042ebf1c6ab47621ef397e82cda70" alt="Firebase Create Webapp" width="846" height="480" data-path="images/dgraph/guides/to-do-app/firebase-create-webapp.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-create-webapp.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=d261bf422d6cbccad0698e66f47a08d2 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-create-webapp.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=673c7b5db14cab828e8405354a60a74e 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-create-webapp.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=13b9e8fe86c91f798f5b840277fac014 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-create-webapp.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=92f7308e59d1d4d6e2bba9db7c24a5a1 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-create-webapp.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=8e7c1e6b4dcda8cc4d282d4a128d442c 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-create-webapp.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=cd01970e008eda2a9c67d3fd759bdd2a 2500w" data-optimize="true" data-opv="2" />

After creating that, copy the config from there.

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-config.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=25dbbf967b1d3a398e1f7eac4f74c42e" alt="Firebase Config" width="845" height="480" data-path="images/dgraph/guides/to-do-app/firebase-config.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-config.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=b764f07e087b964ed14971cfa878aaad 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-config.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=15ac140cdeed8dd5c6b8baa247f6f69d 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-config.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=a254d3e82eb666250ea75ff7eabcb639 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-config.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=8ad86924c0301463518665bb89065733 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-config.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=181af6bd8362197264aa1def3aa924c7 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-config.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=41106acb76d69a691664658e6ec097ca 2500w" data-optimize="true" data-opv="2" />

Setup your Firebase configuration and `Dgraph Cloud` endpoint in the
[config.json](https://github.com/dgraph-io/graphql-sample-apps/blob/master/todo-react-firebase/src/config.json).
It looks like this:

```json
{
  "apiKey": "your-firebase-apiKey",
  "authDomain": "your-firebase-authDomain",
  "projectId": "your-firebase-projectId",
  "storageBucket": "your-firebase-storageBucket",
  "messagingSenderId": "your-firebase-messagingSenderId",
  "appId": "your-firebase-appId",
  "graphqlUrl": "your-graphql-endpoint"
}
```

Authentication with Firebase is done through the `JWKURL`, where the JSON Web
Key sets are hosted by Firebase. Since Firebase shares the JWKs among multiple
tenants, you must provide your Firebase `project-Id` to the `Audience` field. So
the `Dgraph.Authorization` header will look like this:

```
{"Header":"your-header", "Namespace":"namespace-of-custom-claims","JWKURL": "https://www.googleapis.com/service_accounts/v1/jwk/securetoken@system.gserviceaccount.com", "Audience":[your-projectID]}
```

You don't need to set the `VerificationKey` and `Algo` in the `Authorization`
header. Doing so will cause an error.

Update the
[schema](https://github.com/dgraph-io/graphql-sample-apps/blob/master/todo-react-firebase/schema.graphql),
add the Authorization header (update the project-Id) -

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
    add: {
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

# Dgraph.Authorization {"JWKUrl":"https://www.googleapis.com/service_accounts/v1/jwk/securetoken@system.gserviceaccount.com", "Namespace": "https://dgraph.io/jwt/claims", "Audience": ["your-project-id"], "Header": "X-Auth-Token"}
```

Resubmit the updated schema to Dgraph or Dgraph Cloud.

### React App

For an example of how to initialize the Firebase app with the updated
configuration (`config`) settings, see
[base.js](https://github.com/dgraph-io/graphql-sample-apps/blob/master/todo-react-firebase/src/base.js).

```javascript
import firebase from "firebase/app"
import "firebase/auth"
import config from "./config.json"

const app = firebase.initializeApp({
  apiKey: config.apiKey,
  authDomain: config.authDomain,
  projectId: config.projectId,
  storageBucket: config.storageBucket,
  messagingSenderId: config.messagingSenderId,
  appId: config.appId,
})

export default app
```

To understand how the client gets the token and sends it along with each GraphQL
request, see
[Auth.js](https://github.com/dgraph-io/graphql-sample-apps/blob/master/todo-react-firebase/src/Auth.js).
We can see from the code that whenever there will be `state` change,
`currentUser` will be set to the `new user` and context will return `App` with
the new `idToken`. `App` will initialize the Apollo Client which will send this
`idToken` in header along with every GraphQL request.

```javascript
import React, { useEffect, useState } from "react"
import app from "./base.js"
import firebase from "firebase/app"
import "firebase/functions"

import App from "./App"
export const AuthContext = React.createContext()

export const AuthProvider = ({ children }) => {
  const [currentUser, setCurrentUser] = useState(null)
  const [loading, setLoading] = useState(true)
  const [idToken, setIdToken] = useState("")
  const addUserClaim = firebase.functions().httpsCallable("addUserClaim")

  useEffect(() => {
    app.auth().onAuthStateChanged(async (user) => {
      setLoading(false)
      setCurrentUser(user)
      if (user) {
        addUserClaim({ email: user.email })
        const token = await user.getIdToken()
        setIdToken(token)
      }
    })
  }, [])

  if (loading) {
    return <>Loading...</>
  }
  return (
    <AuthContext.Provider
      value={{
        loading,
        currentUser,
      }}
    >
      {children}
      <App idToken={idToken} />
    </AuthContext.Provider>
  )
}
```

To review the Apollo Client setup, see
[App.js](https://github.com/dgraph-io/graphql-sample-apps/blob/master/todo-react-firebase/src/App.js).

```javascript
...

const createApolloClient = token => {
  const httpLink = createHttpLink({
    uri: config.graphqlUrl,
    options: {
      reconnect: true,
    },
  });

  const authLink = setContext((_, { headers }) => {
    // return the headers to the context so httpLink can read them
    return {
      headers: {
        ...headers,
        "X-Auth-Token": token,
      },
    };
  });

  return new ApolloClient({
    link: authLink.concat(httpLink),
    cache: new InMemoryCache()
  });
}

const App = ({idToken}) => {
  const { loading } = useContext(AuthContext);
  if (loading) {
    return <div>Loading...</div>;
  }
  console.log(idToken)
  const client = createApolloClient(idToken);
  return (
    <ApolloProvider client={client}>
      <div>
        <Router history={history}>
        <header className="navheader">
          <NavBar/>
        </header>
        <Switch>
        <PrivateRoute path="/" component= {TodoApp} exact />
        <PrivateRoute path="/profile" component={Profile} exact/>
        <Route exact path="/login" component = {Login} />
        <Route exact path="/signup" component={SignUp} />
      </Switch>
      </Router>
    </div>
    </ApolloProvider>
  );
}

export default App
```

Now that we have a basic understanding of how to integrate Firebase
authentication in our app, let's see it in action!

```
npm start
```

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-webapp.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=3acbd730d2f02347e7ab5ecf0af6c69f" alt="SignUp Screen" width="854" height="442" data-path="images/dgraph/guides/to-do-app/firebase-webapp.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-webapp.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=9a5b4dbdaec0a55cbe1c9000d82a3818 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-webapp.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=0934192ca1a75a20260319311ffcc373 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-webapp.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=be19907440c4a49a9beb22bb0d30b432 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-webapp.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=816d42352cef24a2adeaf6316fca91b7 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-webapp.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=537eb13729ca49541674b247e945665f 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-webapp.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=2849d871f323a5bb01ab67b801ace9e9 2500w" data-optimize="true" data-opv="2" />

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-todo.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=5767d99f7308f7a5e8686bf4590449b9" alt="Todos Screen" width="627" height="480" data-path="images/dgraph/guides/to-do-app/firebase-todo.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-todo.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=c7b91ce3538b28eb3729e3d212dfc3b1 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-todo.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=a3d6e57c07ee801ba8df3c2710b0ddc6 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-todo.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=397914d6584bb456e81eff93f7d88f4f 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-todo.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=12285502f1caa4e2755368fc2531ea55 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-todo.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=d55ea85808d98a4b5a54876df6b4cc6d 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/firebase-todo.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=5a754fa498f0475dcf626a95d9571cbb 2500w" data-optimize="true" data-opv="2" />
