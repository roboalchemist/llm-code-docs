# Source: https://docs.redwoodjs.com/docs/how-to/disable-api-database

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [Disable API/Database]

[Version: 8.8]

On this page

<div>

# Disable API/Database

</div>

Did you know you could deploy your Redwood app without an API layer or database? Maybe you have a simple static site that doesn\'t need any external data, or you only need to digest a simple JSON data structure that changes infrequently. So infrequently that changing the data can mean just editing a plain text file and deploying your site again.

Let\'s take a look at these scenarios and how you can get them working with Redwood.

## Assumptions[​](#assumptions "Direct link to Assumptions") 

We assume you\'re deploying to Netlify in this recipe. Your mileage may vary for other providers or a custom build process.

## Remove the /api directory[​](#remove-the-api-directory "Direct link to Remove the /api directory") 

Just delete the `/api` directory altogether and your app will still work in dev mode:

``` 
rm -rf api
```

You can also run `yarn install` to cleanup those packages that aren\'t used any more.

## Disable Prisma functionality[​](#disable-prisma-functionality "Direct link to Disable Prisma functionality") 

The `--prisma` and `--dm` flags are set to `true` by default and need to be set to `false` in the build command.

``` 
[build]
  command = "yarn rw deploy netlify --prisma=false --dm=false"
```

While omitting these flags won\'t prevent you from developing the site in a local environment, not setting them to `false` will lead to a `'No Prisma Schema found'` error when you attempt to deploy your site to a production environment, at least when Netlify is the deployment target.

## Turn off the API build process[​](#turn-off-the-api-build-process "Direct link to Turn off the API build process") 

When it comes time to deploy, we need to let Netlify know that it shouldn\'t bother trying to look for any code to turn into AWS Lambda functions.

Open up `netlify.toml`. We\'re going to comment out one line:

``` 
[build]
  command = "yarn rw deploy netlify --prisma=false --dm=false"
  publish = "web/dist"
  # functions = "api/dist/functions"

[dev]
  command = "yarn rw dev"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

If you just have a static site that doesn\'t need any data access at all (even our simple JSON file discussed above) then you\'re done! Keep reading to see how you can access a local data store that we\'ll deploy along with the web side of our app.

## Local JSON Fetch[​](#local-json-fetch "Direct link to Local JSON Fetch") 

Let\'s display a graph of the weather forecast for the week of Jan 30, 2017 in Moscow, Russia. If this seems like a strangely specific scenario it\'s because that\'s the example data we can quickly get from the [OpenWeather API](https://openweathermap.org/forecast16). Get the JSON data [here](https://samples.openweathermap.org/data/2.5/forecast/daily?id=524901&appid=b1b15e88fa797225412429c1c50c122a1) or copy the following and save it to a file at `web/public/forecast.json`:

``` 
,
  "cnt": 7,
  "list": [
    ,
      "pressure": 1024.53,
      "humidity": 76,
      "weather": [
        
      ],
      "speed": 4.57,
      "deg": 225,
      "clouds": 0,
      "snow": 0.01
    },
    ,
      "pressure": 1018.1,
      "humidity": 91,
      "weather": [
        
      ],
      "speed": 4.1,
      "deg": 249,
      "clouds": 88,
      "snow": 1.44
    },
    ,
      "pressure": 1010.85,
      "humidity": 92,
      "weather": [
        
      ],
      "speed": 4.53,
      "deg": 298,
      "clouds": 64,
      "snow": 0.92
    },
    ,
      "pressure": 1019.32,
      "humidity": 84,
      "weather": [
        
      ],
      "speed": 3.06,
      "deg": 344,
      "clouds": 0
    },
    ,
      "pressure": 1012.2,
      "humidity": 0,
      "weather": [
        
      ],
      "speed": 7.35,
      "deg": 24,
      "clouds": 45,
      "snow": 0.21
    },
    ,
      "pressure": 1029.5,
      "humidity": 0,
      "weather": [
        
      ],
      "speed": 2.6,
      "deg": 331,
      "clouds": 29
    },
    ,
      "pressure": 1023.21,
      "humidity": 0,
      "weather": [
        
      ],
      "speed": 5.33,
      "deg": 234,
      "clouds": 46,
      "snow": 0.04
    }
  ]
}
```

Any files that you put in `web/public` will be served by Netlify, skipping any build process.

Next let\'s have a React component get that data remotely and then display it on a page. For this example we\'ll generate a homepage:

``` 
yarn rw generate page home /
```

Next we\'ll use the browser\'s builtin `fetch()` function to get the data and then we\'ll just dump it to the screen to make sure it works:

``` 
import  from 'react'

const HomePage = () => )

  useEffect(() => , [])

  return <div></div>
}

export default HomePage
```

We use `useState` to keep track of the forecast data and `useEffect` to actually trigger the loading of the data when the component mounts. Now we just need a graph! Let\'s add [chart.js](https://www.chartjs.org/) for some simple graphing:

``` 
yarn workspace web add chart.js
```

Let\'s generate a sample graph:

``` 
import  from 'react'
import Chart from 'chart.js'

const HomePage = () => )

  useEffect(() => , [])

  useEffect(() => ,
          ,
        ],
      },
    })
  }, [forecast])

  return <canvas ref= />
}

export default HomePage
```

![image](https://user-images.githubusercontent.com/300/80657460-7beaab80-8a38-11ea-886d-17040ef8573c.png)

If that looks good then all that\'s left is to transform the weather data JSON into the format that Chart.js wants. Here\'s the final `HomePage` including a couple of functions to transform our data and display the dates properly:

``` 
import  from 'react'
import Chart from 'chart.js'

const MONTHS = [
  'Jan',
  'Feb',
  'Mar',
  'Apr',
  'May',
  'Jun',
  'Jul',
  'Aug',
  'Sep',
  'Oct',
  'Nov',
  'Dec',
]

const getDates = (forecast) =>  $`
  })
}

const getTemps = (forecast) => ,
    ,
  ]
}

const kelvinToFahrenheit = (temp) => 

const HomePage = () => , [])

  useEffect(() => ,
      })
    }
  }, [forecast])

  return <canvas ref= />
}

export default HomePage
```

If you got all of that right then you should see:

![Chart screenshot](https://user-images.githubusercontent.com/300/80656934-32e62780-8a37-11ea-963e-0b227d7fe1df.png)

All that\'s left is to deploy it to the world!

## Wrapping Up[​](#wrapping-up "Direct link to Wrapping Up") 

Although we think Redwood will make app developers\' lives easier when they need to talk to a database or third party API, it can be used with static sites and even hybrid sites like this when you want to digest and display data, but from a static file at your own URL.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/disable-api-database.md)