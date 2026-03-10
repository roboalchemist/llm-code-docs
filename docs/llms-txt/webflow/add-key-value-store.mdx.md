# Source: https://developers.webflow.com/webflow-cloud/add-key-value-store.mdx

***

title: Add a Key Value Store to your app
slug: add-key-value-store
description: Add a Key Value Store to your app
hidden: null
subtitle: Add a caching layer to your Webflow Cloud app using a Key Value Store
-------------------------------------------------------------------------------

**What you’ll learn:**

* How to add a Key Value Store to your Webflow Cloud project
* How to use a Key Value Store as a caching layer for third-party API data
* How to improve performance and reduce external requests

## Prerequisites

Before you begin, make sure you have:

* A Webflow Cloud project linked to a GitHub repository
* A Webflow Cloud environment set up
* Node.js 20+ and npm 10+
* Basic familiarity with JavaScript/TypeScript

<Note title="New to Webflow Cloud?">
  If you haven’t already, follow the [Quick Start guide](/webflow-cloud/getting-started) to set up your project and environment.
</Note>

## Add a Key Value Store binding

Before you can use a Key Value Store in your Webflow Cloud app, you need to declare a binding in your project’s configuration. This binding tells your app how to connect to the storage resource.

Once the binding is declared, your app can use simple methods like `.get()`, `.put()`, and `.delete()` to read from and write to the Key Value Store directly in your code.

<Steps>
  <Step title="Update your project in Webflow Cloud (Optional)">
    If you created a Webflow Cloud prior to 7/16/2025, you'll need to update your project in the Webflow Cloud dashboard to use Webflow Cloud's new storage system.

    1. Go to your project in the Webflow Cloud dashboard.
    2. Select the "..." icon in the "Actions" section of the menu.
    3. Select "Edit" (you don't actually need to edit anything).
    4. Press "Save Changes" to update your project.

       <Frame>
         <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/97a23431a8bc1c17dfca0fe41f64dc3417e79faf969fd07d89b3b1fc809a86bc/products/webflow-cloud/pages/concepts/assets/update-project.png" />
       </Frame>
  </Step>

  <Step title="Open your project.">
    Launch your project in your preferred code editor.
  </Step>

  <Step title="Declare the Key Value Store binding.">
    In your project’s `wrangler.json` file, add a `kv_namespaces` array to define your Key Value Store binding:

    ```json title="wrangler.json"
    "kv_namespaces": [
        {
            "binding": "WEATHER_CACHE",
            "id": "1234567890", // Webflow Cloud will generate this for you once you deploy your app
        }
    ]
    ```

    * `binding`: The variable name you’ll use to access the database in your code. This must be a valid JavaScript variable name.
    * `id`: A unique identifier for your database (Webflow Cloud will generate this for you once you deploy your app).
  </Step>

  <Step title="Generate type definitions for your binding.">
    Update your project’s type definitions to enable autocomplete and type safety:

    <Tabs>
      <Tab title="Astro">
        ```bash title="Terminal"
        wrangler types
        ```
      </Tab>

      <Tab title="Next.js">
        ```bash
        npm run cf-typegen
        ```
      </Tab>
    </Tabs>

    This ensures your code editor recognizes the Key Value Store binding.
  </Step>
</Steps>

## Get weather data

Now that your Key Value Store binding is set up, you can use it to cache data in your app. In this section, you’ll build an API route that fetches weather information based on the user’s location. Each response will be stored in your Key Value Store for 10 minutes, so repeated requests are fast and reduce calls to the external weather API.

<Steps>
  <Step title="Create a new API route">
    Set up an API endpoint that will fetch weather data for your users.

    <Tabs>
      <Tab title="Astro">
        1. In your Astro project, go to the `src/pages/api` directory. If this directory doesn’t exist, create it.

        2. Inside this directory, create a new file called `weather.ts`.

        3. Add the following code into your new file:

        ```ts title="src/pages/api/weather.ts"
        import { APIRoute } from "astro";

        // Get api/weather
        export const GET: APIRoute = async ({ request, locals }) => {

        //... Implementation will be added in the next steps
        }
        ```
      </Tab>

      <Tab title="Next.js">
        1. In your Next.js project, go to the `src/app/api` directory. If this directory doesn’t exist, create it.

        2. Inside this directory, create a new file called `weather/route.ts`.

        3. Add the following code into your new file:

        ```ts title="src/app/api/weather/route.ts"
        import type { NextRequest } from "next/server";
        import { getCloudflareContext } from "@opennextjs/cloudflare";

        // Get api/weather
        export async function GET(request: NextRequest) {

            //... Implementation will be added in the next steps
        }
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Get the Key Value Store binding">
    Access your Key Value Store binding in your API route so you can read from and write to the store.

    <Tabs>
      <Tab title="Astro">
        In your `weather.ts` file, access the binding from the runtime environment:

        ```ts title="src/pages/api/weather.ts" {5-7}
        import { APIRoute } from "astro";

        export const GET: APIRoute = async ({ request, locals }) => {

            // Access the environment bindings
            { env } = locals.runtime;
            const weatherCache = env.WEATHER_CACHE;

            //... continue with the next steps
        }
        ```

        * `env.WEATHER_CACHE` gives you access to the Key Value Store you declared in `wrangler.json`.
      </Tab>

      <Tab title="Next.js">
        In your `weather/route.ts` file, access the binding using the Cloudflare context:

        ```ts title="src/app/api/weather/route.ts" {6-8}
        import type { NextRequest } from "next/server";
        import { getCloudflareContext } from "@opennextjs/cloudflare";

        export async function GET(request: NextRequest) {

            // Access the environment bindings and cloudflare request context
            const { env, cf } = getCloudflareContext();
            const weatherCache = env.WEATHER_CACHE;

            //... continue with the next steps
        }
        ```

        * `env.WEATHER_CACHE` gives you access to the Key Value Store you declared in `wrangler.json`.
        * `cf` contains the user's location information, we'll use this in the next step.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Get user's location">
    Extract the user's location from the request headers. This information will be used to fetch location-specific weather data.

    <Tabs>
      <Tab title="Astro">
        In your `weather.ts` file, add the following code to get the user's latitude and longitude from the Cloudflare request headers:

        ```ts title="src/pages/api/weather.ts" {9-12}
        import { APIRoute } from "astro";

        export const GET: APIRoute = async ({ request, locals }) => {

            { env } = locals.runtime;
            const weatherCache = env.WEATHER_CACHE;

            // Get User's location from Cloudflare headers
            if (!request.cf) {
                return new Response("No Cloudflare headers found", { status: 400 });
            }
            const { latitude, longitude } = request.cf;


            //... continue with the next steps
        }
        ```

        * `request.cf` contains the user's location information.
        * If the headers are missing, return a 400 error.
      </Tab>

      <Tab title="Next.js">
        In your `weather/route.ts` file, add the following code to get the user's latitude and longitude from Cloudflare's request headers:

        ```ts title="src/app/api/weather/route.ts" {13-17}
        import type { NextRequest } from "next/server";
        import { getCloudflareContext } from "@opennextjs/cloudflare";

        type WeatherCache = { data: any; timestamp: number };

        // Get Request
        export async function GET(request: NextRequest) {

            // Get binding and cloudflare request context
            const { env, cf } = getCloudflareContext();
            const weatherCache = env.WEATHER_CACHE;

            // Get User's location from Cloudflare headers
            if (!cf) {
                return new Response("No Cloudflare headers found", { status: 400 });
            }
            const { latitude, longitude } = cf;


            //... continue with the next steps
        }
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Check for cached data">
    Before making an external API call, check if the weather data for the user’s location is already stored in your Key Value Store. If cached data exists, return it immediately to improve performance and reduce external requests.

    Use the `.get()` method on the binding to check for cached data.

    <Tabs>
      <Tab title="Astro">
        In your `weather.ts` file, add the following logic after retrieving the user's location:

        ```ts title="src/pages/api/weather.ts" {8}
        // ...previous code

            // Create a cache key from latitude and longitude
            const cacheKey = `${latitude}-${longitude}`;

            try {
                // Try to get the weather data from the cache
                const cachedWeather = await weatherCache.get(cacheKey);

                // If the cached data exists, return it
                if (cachedWeather) {
                    return new Response(cachedWeather, {
                    status: 200,
                    headers: {
                        "Content-Type": "application/json",
                        "X-Cache-Status": "HIT"
                    },
                    });
                }

                //... continue with fetching weather data from the API if not cached

        ```

        * This creates a unique cache key for each location.
        * If data is found, return it with a `X-Cache-Status: HIT` header.
        * If not, continue to the next step to fetch and cache new data.
      </Tab>

      <Tab title="Next.js">
        In your `weather/route.ts` file, add the following logic after retrieving the user's location:

        ```ts title="src/app/api/weather/route.ts" {8}
        // ...previous code

            // Create a cache key from latitude and longitude
            const cacheKey = `${latitude}-${longitude}`;

            try {
                // Try to get the weather data from the cache
                const cachedWeather = await weatherCache.get(cacheKey);

                // If the cached data exists, return it
                if (cachedWeather) {
                    return new Response(cachedWeather, {
                    status: 200,
                    headers: {
                        "Content-Type": "application/json",
                        "X-Cache-Status": "HIT"
                    },
                    });
                }

                //... continue with fetching weather data from the API if not cached

        ```

        * This creates a unique cache key for each location.
        * If data is found, return it with a `X-Cache-Status: HIT` header.
        * If not, continue to the next step to fetch and cache new data.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Fetch and cache fresh weather data">
    If no cached weather data is found, fetch fresh data from the Open-Meteo API, store it in your Key Value Store, and return it to the user.

    Store the fresh data in your Key Value Store using the `.put()` method.

    <Tabs>
      <Tab title="Astro">
        In your `weather.ts` file, add the following logic after checking for cached data:

        ```ts title="src/pages/api/weather.ts"
        // ...previous code

        // If NOT cached, fetch weather data from Open-Meteo API
        const weatherUrl = `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true&temperature_unit=fahrenheit`;
        const weatherData = await fetch(weatherUrl);

        // If error, return error message
        if (!weatherData.ok) {
            throw new Error(`Weather API error: ${weatherData.status}`);
        }

        // Parse the weather data
        const weatherDataJson = await weatherData.json();

        // Cache the weather data for 10 minutes (600 seconds)
        await weatherCache.put(cacheKey, JSON.stringify(weatherDataJson), {
            expirationTtl: 600,
        });

        // Return the weather data with a cache status header
        return new Response(JSON.stringify(weatherDataJson), {
            status: 200,
            headers: {
                "Content-Type": "application/json",
                "X-Cache-Status": "MISS"
                    },
        });

        // Add error handling
        } catch (error) {
            console.error("Error fetching or caching weather data:", error);
            return new Response(
                JSON.stringify({ error: "Failed to fetch weather data" }),
                {
                    status: 502,
                    headers: { "Content-Type": "application/json" },
                }
            );
        }
        };
        ```

        * Fetches weather data for the user’s location.
        * Stores the result in your Key Value Store for 10 minutes.
        * Returns the data with a `X-Cache-Status: MISS` header.
        * If error, return error message.
      </Tab>

      <Tab title="Next.js">
        ```ts title="src/app/api/weather/route.ts"
        // ...previous code

        // If NOT cached, fetch weather data from Open-Meteo API
        const weatherUrl = `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true&temperature_unit=fahrenheit`;
        const weatherData = await fetch(weatherUrl);

        // If error, return error message
        if (!weatherData.ok) {
            throw new Error(`Weather API error: ${weatherData.status}`);
        }

        // Parse the weather data
        const weatherDataJson = await weatherData.json();

        // Cache the weather data for 10 minutes (600 seconds)
        await weatherCache.put(cacheKey, JSON.stringify(weatherDataJson), {
            expirationTtl: 600,
        });

        // Return the weather data with a cache status header
        return new Response(JSON.stringify(weatherDataJson), {
            status: 200,
            headers: { "Content-Type": "application/json" },
        });

        // Add error handling
        } catch (error) {
        console.error("Error fetching or caching weather data:", error);
        return new Response(
            JSON.stringify({ error: "Failed to fetch weather data" }),
            {
                status: 502,
                headers: { "Content-Type": "application/json" },
            }
        );
        }
        };
        ```

        * Fetches weather data for the user’s location.
        * Stores the result in your Key Value Store for 10 minutes.
        * Returns the data with a `X-Cache-Status: MISS` header.
        * If error, return error message.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Test your weather API endpoint">
    Make sure your API route works as expected by sending a request from your terminal.

    1. In your terminal, start your dev server using Cloudflare's context.

       ```bash
       npm run preview
       ```

    2. In a new terminal, run:

       ```bash
       curl http://localhost:<YOUR_PORT_NUMBER>/<YOUR_BASE_PATH>/api/weather
       ```

       * `<YOUR_PORT_NUMBER>` is the port number of your dev server.
       * `<YOUR_BASE_PATH>` is the base path of your project.

    3. Check the response headers:

       * The first request should include `X-Cache-Status: MISS` (data fetched from the API and cached).
       * Subsequent requests should include `X-Cache-Status: HIT` (data returned from the cache).

       If you see the expected headers and weather data in the response, your endpoint and caching are working!
  </Step>
</Steps>

## Update your home page

Now that your API is returning weather data, let’s display it directly on your home page. In this section, you’ll add a weather widget that shows the current temperature and a matching weather icon for your user’s location. This gives users instant, dynamic feedback and demonstrates how to connect your frontend to your new API.

<Steps>
  <Step title="Add weather icons to your project">
    Add weather icons to your project so you can visually represent the current weather.

    ```bash
    npm install weather-icons
    ```

    * Run this command in your project's root directory.
    * The `weather-icons` package provides a set of CSS classes for common weather conditions
  </Step>

  <Step title="Map weather codes to icon classes">
    Create a utility to translate weather codes from your API into icon classes for display.

    1. In your project’s `src` directory, create a `utils` folder if it doesn’t already exist.
    2. Inside `utils`, create a file named `iconMap.ts`.
    3. Copy and paste the following code into `iconMap.ts`:

    ```ts title="src/utils/iconMap.ts" maxLines=10
        const ICON_MAP: { [key: number]: string } = {
            0: "wi-day-sunny", // Clear
            1: "wi-day-sunny-overcast", // Mostly Clear
            2: "wi-day-cloudy", // Partly Cloudy
            3: "wi-cloudy", // Overcast

            45: "wi-fog", // Fog
            48: "wi-fog", // Icy Fog

            51: "wi-sprinkle", // Light Drizzle
            53: "wi-showers", // Drizzle
            55: "wi-rain", // Heavy Drizzle

            56: "wi-rain-mix", // Light Freezing Drizzle
            57: "wi-rain-mix", // Freezing Drizzle

            61: "wi-raindrops", // Light Rain
            63: "wi-rain", // Rain
            65: "wi-rain-wind", // Heavy Rain

            66: "wi-rain-mix", // Light Freezing Rain
            67: "wi-rain-mix", // Freezing Rain

            71: "wi-snow", // Light Snow
            73: "wi-snow", // Snow
            75: "wi-snow-wind", // Heavy Snow

            77: "wi-snowflake-cold", // Snow Grains

            80: "wi-raindrops", // Light Showers
            81: "wi-rain", // Showers
            82: "wi-rain-wind", // Heavy Showers

            85: "wi-snow", // Light Snow Showers
            86: "wi-snow-wind", // Snow Showers

            95: "wi-thunderstorm", // Thunderstorm
            96: "wi-storm-showers", // Light T-storm w/ Hail
            99: "wi-storm-showers", // T-storm w/ Hail
        };

        export default ICON_MAP;

    ```
  </Step>

  <Step title="Call the weather API from your home page">
    Fetch the latest weather data from your API and display it on your home page, along with the appropriate weather icon.

    <Tabs>
      <Tab title="Astro">
        1. Open your home page file. (for example, `src/pages/index.astro`)

        2. Import the weather icons CSS and your icon map utility at the top of the file.

           ```ts title="src/pages/index.astro"
           import 'weather-icons/css/weather-icons.css';
           import ICON_MAP from '../utils/iconMap.js';
           ```

        3. Fetch the weather data from your API and extract the temperature and weather code. Then, use the weather code to get the appropriate icon class from your icon map utility.

           ```ts title="src/pages/index.astro"
           // Get the base URL for your API
           const url = Astro.url.origin + import.meta.env.BASE_URL;

           // Fetch weather data
           const weather = await fetch(`${url}/api/weather`);
           const weatherData = await weather.json();
           const { temperature, weathercode } = weatherData?.current_weather;

           // Map the weather code to an icon class
           const iconClass = ICON_MAP[weathercode];
           ---
           ```

        4. Display the weather data and icon in your page’s markup, below the welcome message:

           ```tsx title="src/pages/index.astro" {3}
           <h1 class="margin-bottom-24px">Welcome to Webflow Cloud</h1>
           <p class="margin-bottom-24px">This is a simple test using Basic components with enhanced styling.</p>
           <h2>{temperature}°F <i class={`wi ${iconClass}`}></i></h2>
           <div>
           ```

        See the full code example below:

        ```ts title="src/pages/index.astro" maxLines=10
        ---
        import Layout from '../layouts/Layout.astro';
        import { Navbar } from '../../devlink/Navbar.jsx';
        import { Section, Container, Block, Link } from '../../devlink/_Builtin/Basic';
        import 'weather-icons/css/weather-icons.css';
        import ICON_MAP from '../utils/iconMap.js';

        // Get base url for API calls
        const url = Astro.url.origin + import.meta.env.BASE_URL;

        //  Get weather data
        const weather = await fetch(`${url}/api/weather`);
        console.log(weather);
        const weatherData = await weather.json();
        const { temperature, weathercode }: { temperature: number; weathercode: number } = weatherData?.current_weather;

        const iconClass = ICON_MAP[weathercode];

        ---

        <Layout>
        <Navbar
        />
        <Section
            client:load
            tag="section"
            className="margin-bottom-24px"
            style={{
            minHeight: '100vh',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center'
            }}
        >
            <Container>
            <Block
                tag="div"
                className="hero-split"
                style={{
                textAlign: 'center',
                maxWidth: '600px',
                margin: '0 auto'
                }}
            >
                <h1 class="margin-bottom-24px">Welcome to Webflow Cloud</h1>
                <p class="margin-bottom-24px">This is a simple test using Basic components with enhanced styling.</p>
                <h2>{temperature}°F <i class={`wi ${iconClass}`}></i></h2>
                <div>
                <Link
                    button={true}
                    options={{
                    href: "#"
                    }}
                    className="button-primary"
                >
                    Get Started
                </Link>
                </div>
            </Block>
            </Container>
        </Section>
        </Layout>

        <style>
        h1 {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(83.21deg, #3245ff 0%, #bc52ee 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        </style>

        ```
      </Tab>

      <Tab title="Next.js">
        1. Open your home page file (e.g., src/pages/page.tsx).

        2. Import the weather icons CSS and your icon map utility at the top of the file.

           ```ts title="src/pages/page.tsx"
           import "weather-icons/css/weather-icons.css";
           import ICON_MAP from "./utils/iconMap";
           ```

        3. Use a React effect to fetch weather data from your API and store it in state:

           ```ts title="src/pages/page.tsx"
           const [weather, setWeather] = useState<{ temperature: number; weathercode: number } | null>(null);

           useEffect(() => {
           fetch(`${process.env.NEXT_PUBLIC_BASE_URL}/api/weather`)
               .then((res) => res.json())
               .then((data) => {
               setWeather((data as any).current_weather);
               })
               .catch((err) => {
               console.error("Weather API error:", err);
               });
           }, []);
           ```

        4. Display the weather data and icon in your component’s TSX:

           ```tsx title="src/pages/page.tsx"
           {weather ? (
           <h2>
           {weather.temperature}°F <i className={`wi ${ICON_MAP[weather.weathercode] || "wi-na"}`}></i>
           </h2>
           ) : (
               <div>Loading...</div>
           )}
           ```

        See the full code example below:

        ```ts title="src/pages/page.tsx"
            "use client";

            import { useEffect, useState } from "react";
            import { Section, Block, Link } from "@/devlink/_Builtin";
            import ICON_MAP from "./utils/iconMap";
            import "weather-icons/css/weather-icons.css";

            export default function Home() {

                // State for weather data
                const [weather, setWeather] = useState<{ temperature: number; weathercode: number } | null>(null);

                // Call the weather API and get the weather data for the user's location
                useEffect(() => {
                // Fetch weather data from your API
                fetch(`${process.env.NEXT_PUBLIC_BASE_URL}/api/weather`)
                .then((res) => res.json())
                .then((data) => {
                    // Set weather state from API response
                    setWeather((data as any).current_weather);
                })
                .catch((err) => {
                    console.error("Weather API error:", err);
                    });
                }, []);


                return (
                <main style={{ minHeight: "100vh", display: "flex", alignItems: "center", justifyContent: "center" }}>
                <div style={{ textAlign: "center", maxWidth: 600, margin: "0 auto" }}>
                    <h1 className="margin-bottom-24px" style={{
                    fontSize: "2.5rem",
                    fontWeight: 700,
                    background: "linear-gradient(83.21deg, #3245ff 0%, #bc52ee 100%)",
                    WebkitBackgroundClip: "text",
                    WebkitTextFillColor: "transparent",
                    backgroundClip: "text"
                    }}>
                    Welcome to Webflow Cloud
                    </h1>
                    <p className="margin-bottom-24px">
                    This is a simple test using Basic components with enhanced styling.
                    </p>
                    <h2>
                    {weather.temperature}°F <i className={`wi ${ICON_MAP[weather.weathercode] || "wi-na"}`}></i>
                    </h2>
                    <div>
                    <a href="#" className="button-primary">
                        Get Started
                    </a>
                    </div>
                </div>
                </main>
            );
            }
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>

## Test and deploy your app

Make sure your app is working as expected by running it locally and verifying the weather widget displays correctly.

<Steps>
  <Step title="Start your development server">
    Start your app in development mode with the Cloudflare context.

    ```bash
    npm run preview

    ```
  </Step>

  <Step title="Open your app in the browser">
    Visit your app in a web browser.

    * Go to `http://<YOUR_PORT_NUMBER>/<YOUR_BASE_PATH>` to see your app running locally.

      * `<YOUR_PORT_NUMBER>` is the port number of your dev server.
      * `<YOUR_BASE_PATH>` is the base path of your project.

      You should see your app running locally with the weather widget displaying the current temperature and weather icon.

      <Frame>
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/1251fbeb41ff27040e411120967ebd2d410c813add0801ac24a2a3f7013a1c13/products/webflow-cloud/pages/concepts/assets/weather.png" />
      </Frame>
  </Step>

  <Step title="Deploy your app">
    Deploy your app to Webflow Cloud. You can deploy your app in two ways:

    1. Use the Webflow CLI
       ```bash
       webflow cloud deploy
       ```

    2. Commit and push your changes to your GitHub repository.

       ```bash
       git add .
       git commit -m "Deploying app to Webflow Cloud"
       git push
       ```

    Go to your environment in Webflow Cloud to see your app deployed. Once deployed, you can access your app at `https://<YOUR_DOMAIN>/<YOUR_BASE_PATH>`.
  </Step>
</Steps>

## Next steps

Congratulations! You’ve successfully added a Key Value Store to your Webflow Cloud app, built a weather API with caching, and displayed live weather data on your home page.

<CardGroup>
  <Card
    title="Explore more Key Value Store features"
    href="/webflow-cloud/storing-data/key-value-store"
    iconPosition="left"
    iconSize="12"
    icon={
                <>
                    <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/DeveloperToolsSDK.svg" alt="" className="dark-icon" />
                    <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/DeveloperToolsSDK.svg" alt="" className="light-icon" />
                </>
            }
  >
    Learn how to manage data, set advanced expiration rules, and handle larger datasets in the Key Value Store documentation.
  </Card>

  <Card
    title="Compare storage options"
    href="/webflow-cloud/storing-data/overview"
    iconPosition="left"
    iconSize="12"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/CMS.svg" alt="" className="dark-icon" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/CMS.svg" alt="" className="light-icon" />
            </>
        }
  >
    See how Key Value Store fits alongside other storage solutions in Webflow Cloud.
  </Card>
</CardGroup>
