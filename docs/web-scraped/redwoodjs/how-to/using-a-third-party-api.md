# Source: https://docs.redwoodjs.com/docs/how-to/using-a-third-party-api

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [Using a Third Party API]

[Version: 8.8]

On this page

<div>

# Using a Third Party API

</div>

The time will come when you\'ll need data from a source you don\'t own. This how to will present the scenario of accessing a third party\'s API from a Redwood app. We\'ll show an example of accessing an API from both the client side and the server side.

We\'re going to build a simple weather app that will display the current weather in the user\'s zip code (we\'ll assume only zip codes in the United States of America to keep the example code as simple as possible). To do this we\'ll get the current weather from the [OpenWeather API](https://openweathermap.org/) and display it on the only page of our app, the homepage. The final app could look something like this (if you apply a little more styling on top of the basic version we\'ll build):

![image](https://user-images.githubusercontent.com/300/79395970-af551280-7f2f-11ea-9b8c-870fc2bfdd36.png)

> If you just want to skip to the code, you can get the repo for both the client and server implementation here: [https://github.com/redwoodjs/cookbook-third-party-apis](https://github.com/redwoodjs/cookbook-third-party-apis) You will still need a valid API key from OpenWeather, so don\'t skip the **Setup** steps below!

## Setup[​](#setup "Direct link to Setup") 

You\'ll need to [create a free account](https://home.openweathermap.org/users/sign_up) on OpenWeather to get an API key. You\'ll be able to make 1,000 calls per day, which is more than enough for our sample app (with enough left over that you can release this as a private weather station for your family and friends).

Once you\'ve created your account and verified your email address, go to the API keys tab and copy your default key:

![image](https://user-images.githubusercontent.com/300/79375024-d0f0d280-7f0c-11ea-81a8-364659755efa.png)

(That\'s not a real key so don\'t even think about trying to steal it!)

For some reason it can take up to 30 minutes for OpenWeather to enable your API key, so while we\'re waiting for them let\'s see what a sample API call will return: [https://samples.openweathermap.org/data/2.5/weather?zip=94040,us&appid=439d4b804bc8187953eb36d2a8c26a02](https://samples.openweathermap.org/data/2.5/weather?zip=94040,us&appid=439d4b804bc8187953eb36d2a8c26a02)

``` 
,
  "weather": [
    
  ],
  "base": "stations",
  "main": ,
  "visibility": 12874,
  "wind": ,
  "clouds": ,
  "dt": 1519061700,
  "sys": ,
  "id": 0,
  "name": "Mountain View",
  "cod": 200
}
```

Good ol\' faithful JSON. Let\'s see, what can we use here to display on our site? How about the `name` of the city that the zip is in, the `main.temp` (listed here in Kelvin, so we\'ll need to [convert](https://www.google.com/search?q=297+kelvin+to+fahrenheit&oq=297+kelvin+to+fahrenheit)) and then under the `weather` key we have an array with a `main` that lists the current conditions in english. How about that `icon`? Turns out OpenWeather has some we can use! Just take the icon code and use it in a URL like [http://openweathermap.org/img/wn/10d@2x.png](http://openweathermap.org/img/wn/10d@2x.png)

![rain icon](https://user-images.githubusercontent.com/300/79376259-c33c4c80-7f0e-11ea-8285-701375665451.png)

If enough time has passed your real API key may be activated. You can try seeing the weather in the geographic center of the US (make sure to append your API key to the end of this URL): [https://api.openweathermap.org/data/2.5/weather?zip=66952,us&appid=](https://api.openweathermap.org/data/2.5/weather?zip=66952,us&appid=)

If it\'s still not ready let\'s start working on the app and hopefully it will be by the time we\'re done. You can always use the sample URL and forever see the unchanging weather in Mountain View, California.

## Create the App[​](#create-the-app "Direct link to Create the App") 

We\'ll start our app the way we start all Redwood apps:

``` 
yarn create redwood-app weatherstation
cd weatherstation
yarn rw dev
```

That will open a browser to [http://localhost:8910](http://localhost:8910). Let\'s create a landing page:

``` 
yarn rw generate page home /
```

> If you like typing you can use the full command `yarn redwood generate page home /`

The browser should have refreshed with a message about where to find our new homepage, `web/src/pages/HomePage/HomePage.js`. Let\'s open that up and create a form so the user can actually enter their zip code:

web/src/pages/HomePage/HomePage.js

``` 
import  from '@redwoodjs/forms'

const HomePage = () => 

  return (
    <Form onSubmit= style=}>
      <TextField
        name="zip"
        placeholder="Zip code"
        maxLength="5"
        validation=$/ }}
      />
      <Submit>Go</Submit>
    </Form>
  )
}

export default HomePage
```

This gives us a very simple form and some validation that the user is entering a 5 digit zip code. If you open your Web Inspector and click **Go** you should see the zip code appear in the console:

![console output](https://user-images.githubusercontent.com/300/79378210-c8e76180-7f11-11ea-949d-2bacae483559.png)

Now let\'s talk to the API and get some data for real. We can do that in one of two ways:

1.  Have the client (React app running in the browser) talk to the API directly
2.  Have our own server (or serverless function, in the case of Redwood) talk to the API, and have the client talk to *our* server.

We\'ll build out an example of both types of integration below.

## Client-side API Integration[​](#client-side-api-integration "Direct link to Client-side API Integration") 

For the first version of our client-side integration let\'s access the API directly on the client. What are the pros on cons?

**Pros**

-   Simplest design: no server design/build needed
-   Fewest network calls: one!
-   Fast: calling directly to the API

**Cons**

-   Insecure: users could inspect the page source and get our API key
-   No throttling: someone could write a bot to hit the page thousands of times a second

You\'ll need to balance these risks in a real-world app so choose carefully!

### Fetching the weather data[​](#fetching-the-weather-data "Direct link to Fetching the weather data") 

We\'ve got the zip code in our `onSubmit` handler so it makes sense to simply make the API call from there and then do something with the result. We\'ll use the browser\'s built in [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) since it does exactly what we need. For now let\'s just dump the result to the console (be sure to use your actual API key):

web/src/pages/HomePage/HomePage.js

``` 
const onSubmit = (data) => 
```

![image](https://user-images.githubusercontent.com/300/79379271-858df280-7f13-11ea-97f0-5020f875170d.png)

> If it turns out your API key still isn\'t ready, you\'d think you could just replace the URL in the fetch with the sample response endpoint instead, but this causes a CORS error. At this point you\'ll just need to wait for your API key to start working!

Well that was easy! We have the zip code hardcoded into that URL so let\'s replace that with the actual value from our text box:

web/src/pages/HomePage/HomePage.js

``` 
const onSubmit = (data) => ,us&appid=YOUR_API_KEY`
  )
    .then((response) => response.json())
    .then((json) => console.info(json))
}
```

### Showing the weather on the page[​](#showing-the-weather-on-the-page "Direct link to Showing the weather on the page") 

We\'re getting our data just fine but now we need to update the page with the weather. Let\'s use state to keep track of the result and trigger a refresh in the UI (don\'t forget the new fragment `<> </>` around the form and weather output):

web/src/pages/HomePage/HomePage.js

``` 
import  from 'react'
import  from '@redwoodjs/forms'

const HomePage = () => ,us&appid=YOUR_API_KEY`
    )
      .then((response) => response.json())
      .then((json) => setWeather(json))
  }

  return (
    <>
      <Form onSubmit=>
        <TextField
          name="zip"
          placeholder="Zip code"
          maxLength="5"
          validation=$/ }}
        />
        <Submit>Go</Submit>
      </Form>
      
    </>
  )
}

export default HomePage
```

That should give us a simple text dump of the JSON:

![image](https://user-images.githubusercontent.com/300/79381373-bae80f80-7f16-11ea-9159-dd08e6ac7ade.png)

Finally, let\'s output the actual weather data along with a couple of helper functions to format the output:

web/src/pages/HomePage/HomePage.js

``` 
import  from 'react'
import  from '@redwoodjs/forms'

const HomePage = () => ,us&appid=YOUR_API_KEY`
    )
      .then((response) => response.json())
      .then((json) => setWeather(json))
  }

  const temp = () => Math.round(((weather.main.temp - 273.15) * 9) / 5 + 32)

  const condition = () => weather.weather[0].main

  const icon = () => @2x.png`
  }

  return (
    <>
      <Form onSubmit=>
        <TextField
          name="zip"
          placeholder="Zip code"
          maxLength="5"
          validation=$/ }}
        />
        <Submit>Go</Submit>
      </Form>
      </h1>
          <h2>
            <img src= style=} />
            <span>
              °F and 
            </span>
          </h2>
        </section>
      )}
    </>
  )
}

export default HomePage
```

![image](https://user-images.githubusercontent.com/300/79381535-fbe02400-7f16-11ea-87f8-119bdb121765.png)

It\'s not pretty, but it works! We\'ll leave the styling to you!

> You can see the final code, with styling, here: [https://github.com/redwoodjs/cookbook-third-party-apis/blob/main/web/src/pages/ClientPage/ClientPage.js](https://github.com/redwoodjs/cookbook-third-party-apis/blob/main/web/src/pages/ClientPage/ClientPage.js)

## Server-side API Integration[​](#server-side-api-integration "Direct link to Server-side API Integration") 

If you weighed the pros and cons presented earlier and found too many cons on the client-side implementation, then it looks like we\'re making our call on the server. To do that we\'ll need to do two things

1.  Provide a way for the client to talk to our server(less function)
2.  A way for our server(less function) to talk to the third party API

Redwood comes with GraphQL integration built in so that seems like a logical way to get our client talking to our serverless function. Let\'s create a GraphQL SDL (to define the API interface for the client) and a service (to actually implement the logic of talking to the third-party API).

> **Doesn\'t Redwood have a generator for this?**
>
> Redwood does have an SDL generator, but it assumes you have a model defined in `api/db/schema.prisma` and so creates the SDL you need to access that data structure. If you\'re creating a custom one you\'re on your own!

### The GraphQL API[​](#the-graphql-api "Direct link to The GraphQL API") 

We can create whatever data structure we want so let\'s take this opportunity to strip out the data we don\'t care about coming from OpenWeather and just return the good stuff:

api/src/graphql/weather.sdl.js

``` 
export const schema = gql`
  type Weather 

  type Query 
`
```

This data structure returns just the data we care about, and we can even pre-format it on the server (convert Kelvin to Fahrenheit and get the icon URL). We have a Query type `getWeather` that accepts the zip code (note that it\'s a `String` because it could start with a `0`) and returns our `Weather` type defined above.

### The Service[​](#the-service "Direct link to The Service") 

That\'s it for our client-to-server API interface! Now let\'s define the GraphQL resolver that will actually get the data from OpenWeather. We\'ll take it one step at a time and first make sure we can access our new GraphQL endpoint. We\'ll define the `getWeather` function to just return some dummy data in the format we require.

In Redwood GraphQL Query types are automatically mapped to functions exported from a service with the same name, so we\'ll create a `weather.js` service and name the function `getWeather`:

api/src/services/weather/weather.js

``` 
export const getWeather = () => 
}
```

How can we test this out? Redwood ships with a GraphQL playground that you can use to access your API! Open a browser tab to [http://localhost:8911/graphql](http://localhost:8911/graphql)

![image](https://user-images.githubusercontent.com/300/79391348-3dc49680-7f26-11ea-8d94-8567ae287fa6.png)

We\'ll enter our query at the top left and the variables (zip) at the lower left. Click the huge \"Play\" button in the middle of the screen and you should see the result of our query:

![image](https://user-images.githubusercontent.com/300/79395014-9cd9d980-7f2d-11ea-83b1-45aaa8506706.png)

Okay lets pull the real data from OpenWeather now. We\'ll use a package `@whatwg-node/fetch` that mimics the Fetch API in the browser:

``` 
yarn workspace api add @whatwg-node/fetch
```

And import that into the service and make the fetch. Note that `fetch` returns a Promise so we\'re going to convert our service to `async`/`await` to simplify things:

api/src/services/weather/weather.js

``` 
import  from '@whatwg-node/fetch'

export const getWeather = async () => ,US&appid=YOUR_API_KEY`
  )
  const json = await response.json()

  return @2x.png`,
  }
}
```

If you click \"Play\" in the GraphQL playground we should see the real data from the API:

![image](https://user-images.githubusercontent.com/300/79607107-8ce60500-80a7-11ea-8b1d-fe1cd3e1d3dd.png)

### Displaying the weather[​](#displaying-the-weather "Direct link to Displaying the weather") 

All that\'s left now is to display it in the client! Since we\'re getting data from our GraphQL API we can use a Redwood Cell to simplify all the work that goes around writing API access, displaying a loading state, etc. We can use a generator to get the shell of our Cell:

``` 
yarn rw generate cell weather
```

This will create `web/src/components/WeatherCell/WeatherCell.js`:

web/src/components/WeatherCell/WeatherCell.js

``` 
export const QUERY = gql`
  query FindWeatherQuery($id: Int!) 
  }
`

export const Loading = () => <div>Loading...</div>

export const Empty = () => <div>Empty</div>

export const Failure = () => (
  <div style=}>Error: </div>
)

export const Success = () => </div>
}
```

Let\'s update the QUERY to match the signature of our API:

``` 
export const QUERY = gql`
  query GetWeatherQuery($zip: String!) 
  }
`
```

Note the `weather: getWeather` part. This will actually call the API endpoint `getWeather` but the response will be renamed to `weather` and then given to the `Success` component.

Let\'s leave the display as-is for now to make sure this is working. We\'ll use the `WeatherCell` in our `HomePage` and introduce some state to keep track of when the zip is submitted:

web/src/pages/HomePage/HomePage.js

``` 
import  from '@redwoodjs/forms'
import  from 'react'
import WeatherCell from 'src/components/WeatherCell'

const HomePage = () => 

  return (
    <>
      <Form onSubmit= style=}>
        <TextField
          name="zip"
          placeholder="Zip code"
          maxLength="5"
          validation=$/ }}
        />
        <Submit>Go</Submit>
      </Form>
       />}
    </>
  )
}

export default HomePage
```

If your copy/paste-fu is strong you should get a dump of the JSON from the GraphQL call:

![image](https://user-images.githubusercontent.com/300/79393218-bb3dd600-7f29-11ea-9b3a-3f2bbd854ed8.png)

Now all that\'s left is to format everything a little nicer. How about a little something like this in `WeatherCell`:

web/src/components/WeatherCell/WeatherCell.js

``` 
export const Success = () => </h1>
      <h2>
        <img src= style=} />
        <span>
          °F and 
        </span>
      </h2>
    </section>
  )
}
```

![image](https://user-images.githubusercontent.com/300/79393411-2091c700-7f2a-11ea-8760-8938d55b1ef5.png)

### Extra Credit! Invalid zip codes?[​](#extra-credit-invalid-zip-codes "Direct link to Extra Credit! Invalid zip codes?") 

What if the user inputs an invalid zip code, like **11111**?

![image](https://user-images.githubusercontent.com/2321110/137649805-5a9f6f4d-4f66-4758-9e47-f1a8a985bdda.png)

Gross. This happens when our service tries to parse the response from OpenWeather and can\'t find one of the data points we\'re looking for (the array under the `weather` key). We should put together a nicer error message than that. Let\'s look at the response from OpenWeather when you enter a zip code that doesn\'t exist: [https://api.openweathermap.org/data/2.5/weather?zip=11111,us&appid=YOUR_API_KEY](https://api.openweathermap.org/data/2.5/weather?zip=11111,us&appid=YOUR_API_KEY)

``` 

```

Okay, let\'s look for that `cod` and if it\'s `404` then we know the zip isn\'t found and can return a more helpful error from our service. Open up the service and let\'s add a check:

api/src/services/weather/weather.js

``` 
import  from '@whatwg-node/fetch'
import  from '@redwoodjs/graphql-server'

export const getWeather = async () => ,US&appid=YOUR_API_KEY`
  )
  const json = await response.json()

  if (json.cod === '404')  isn't a valid US zip code, please try again`
    )
  }

  return @2x.png`,
  }
}
```

And now if we submit **11111**:

![image](https://user-images.githubusercontent.com/2321110/137649849-49d3aa66-e08b-44f8-93b9-c8a61f1e5ce9.png)

That\'s much better! Let\'s strip out that \"Error: \" part, and maybe make it look a little more error-like. This is a job for the `Failure` component in our `WeatherCell`:

web/src/components/WeatherCell/WeatherCell.js

``` 
export const Failure = () => (
  <span
    style=}
  >
    
  </span>
)
```

![image](https://user-images.githubusercontent.com/2321110/137649934-35c7b0e1-9b10-409e-8dbb-6a133aeb14bd.png)

Much better!

## Conclusion[​](#conclusion "Direct link to Conclusion") 

We hope this has given you enough confidence to go out and capture data from some of the amazing APIs of the Information Superhighway and get it (them?) into your Redwood app!

Picking up any new framework from scratch is a daunting task and even those of us that wrote this one made more than a few trips to Google! If you think we can improve on this recipe, or any other, open an [issue](https://github.com/redwoodjs/redwoodjs.com/issues) or a [pull request](https://github.com/redwoodjs/redwoodjs.com/pulls).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/using-a-third-party-api.md)