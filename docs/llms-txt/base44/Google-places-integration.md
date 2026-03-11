# Source: https://docs.base44.com/Integrations/Google-places-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Places Integration

> Connect your app to Google Places to easily search, suggest, and display real-world places.

<Info>
  <u>Note</u>: Google Places integration is available on Builder tier and above. If you're on the Free tier, you'll need to upgrade your app to use backend functions and payment features.
</Info>

***

# Step by step setup:

## Part 1: The Google side

If you already have a Google Places API key, feel free to skip ahead to [****Part 2: The Base44 side.****](https://docs.base44.com/Integrations/Google-places-integration#part-2%3A-the-base44-side)

<Steps>
  <Step title="Create (or choose) a project in Google Cloud">
        <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/GoogleCloudConsole.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=d5b443da6da1f62941411efeee7f7d64" alt="Google Cloud Console Pn" width="1550" height="827" data-path="images/GoogleCloudConsole.png" />

    * Head to the Google Cloud Console and either pick an existing project or create a new one.
  </Step>

  <Step title="Enable the places API (New)">
        <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/GoogleAPI.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=a03ab9df6cb3aaa4c29231d45d882b44" alt="Google API Pn" width="1900" height="855" data-path="images/GoogleAPI.png" />

    * In the left sidebar, click **APIs and Services** → **Library**.
    * Use the search bar to find **Places API (New)** and open it.
    * Click **Enable** to activate it for your project.
  </Step>

  <Step title="Generate your API Key">
    * From the API’s credentials page, click **Create Key** and copy it.
    * Save the key somewhere secure. You’ll need to paste it into Base44.
  </Step>
</Steps>

<Tip>
   If you see an error like `REQUEST_DENIED` later on, it usually means billing isn’t enabled or your API key restrictions are too tight. Turning on billing and loosening restrictions during testing often fixes this. If you plan to display a map in the browser, you should also enable the **Maps JavaScript API** and use a browser key restricted to your site.
</Tip>

***

## Part 2: The Base44 side

Once you have your Google Places API key, you can connect it to Base44 in two different ways:

<CardGroup cols={2}>
  <Card icon="sparkle" href="https://docs.base44.com/Integrations/Google-places-integration#option-a%3A-ready-made-integration-create-a-new-app" title="Option A: Ready-made integration (preferred)">
    * Choose this path if you are starting a new app from scratch.
  </Card>

  <Card icon="bolt" href="https://docs.base44.com/Integrations/Google-places-integration#option-b%3A-instant-integration-connecting-to-an-existing-app" title="Option B: Instant integration">
    * Choose this path if you are already in the midst of building and would like to integrate Google Places into an existing app.
  </Card>
</CardGroup>

### Option A: Ready-made integration (create a new app)

<Steps>
  <Step title="Choose the integration">
    * In Base44 click on Integrations

        <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/Integrations.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=16ac71b185167177ef260be7c92b0339" alt="Integrations Pn" width="1570" height="652" data-path="images/Integrations.png" />

    * Find **Google Places**
    * Select **Use this Integration**
  </Step>

  <Step title="Provide your API key">
        <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/GoogleIntegration.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=896eb0dc8f08cd285bcf6c001068d45d" alt="Google Integration Pn" width="1863" height="809" data-path="images/GoogleIntegration.png" />

    * When prompted, paste your Places API key into the field labeled `GOOGLE_PLACES_API_KEY`.
  </Step>

  <Step title="Build your app">
    * In the AI chat, describe your app’s purpose.
    * For example:\
      ` Create an app to plan my next trip. I will tell you the city, you will suggest five places, and you will show them on a Google Places map.`
    * Base44’s AI will build the basic structure for you.
  </Step>

  <Step title="Test with a sample trip">
    * Enter a city, search for up to five places, and save the trip.
    * Check that a map appears with markers for all selected places and that it automatically zooms to fit them.
  </Step>
</Steps>

***

### Option B: Instant integration (connecting to an existing app)

Use this approach when your app is partially built and you want to integrate Places without starting over.

<Steps>
  <Step title="Access your existing app">
    * Here's the prompt that we typed out in the AI chat to build our sample app: \
      ` “Create an app to plan my next trip. I will tell you the city and you will choose five places for me to visit.”`
  </Step>

  <Step stepNumber={2} title="Connect your app to Google Places using the AI chat">
        <img src="https://mintcdn.com/base44/x7uieDiv9xNLARBF/images/TripPlannerApp.png?fit=max&auto=format&n=x7uieDiv9xNLARBF&q=85&s=3eddfdc78ee42b5a7af9fba1e6755bf4" alt="Trip Planner App Pn" width="1889" height="853" data-path="images/TripPlannerApp.png" />

    * Ask the chat to connect your app to Google Places. You can edit this sample prompt:

      `Connect this app to Google Places using the Places API (New). Ask me for GOOGLE_PLACES_API_KEY and save it as a Secret. Create backend functions to:`

      `- search by text and return id, displayName, formattedAddress, location, types`

      `- get details by place_id with the same fields`

      `All calls must run from the backend only.`
  </Step>

  <Step stepNumber={3} title="When prompted by the AI chat, paste your API key">
        <img src="https://mintcdn.com/base44/-Vklow6W-uVvNnvR/images/setsecrets.png?fit=max&auto=format&n=-Vklow6W-uVvNnvR&q=85&s=6f96c4ed12b712cbb8ccee93cb0f761d" alt="Setsecrets Pn" width="802" height="522" data-path="images/setsecrets.png" />

    * When prompted by the AI Chat, click on `Update GOOGLE_PLACES_API_KEY`
    * Then paste your API key into the pop up window
  </Step>

  <Step stepNumber={4} title="Build the interface">
    * Add the Trip Planner UI and map.
    * You can use a prompt similar to this one to build your interface:

      `Add a Trip Planner page with:`

      `- a City field`

      `- 5 auto-suggest place inputs powered by the backend`

      `When a place is selected, save place_id, name, formatted_address, latitude, longitude, types.`

      `Add a Google Map that places a marker for each saved place and automatically fits bounds to show them all. Include a Reset button.`
  </Step>

  <Step stepNumber={5} title="Test your app">
    * Enter a city and let the app suggest five places, then save.
    * Verify that markers appear and the map fits all points.
    * Refresh the app to confirm the saved places render correctly.
  </Step>
</Steps>

***

## **Troubleshooting**

* **403 or REQUEST\_DENIED errors** – Usually the Places API isn’t enabled, the API key is wrong, or key restrictions are too strict. Double‑check that **Places API (New)** is enabled, your billing account is set up, and relax restrictions during testing.
* **Empty suggestions** – Try a different city or search term. Make sure the search is happening on the backend, not in the browser.
* **Map doesn’t fit all points** – Ensure your app calls fitBounds after all markers have been added to the map.
* **Wrong fields saved** – Save exactly the fields listed above (place\_id, name, formatted\_address, latitude, longitude, types) so the map and filters work reliably.

## Common use Cases

Here are some ideas for how you can leverage the Google Places API inside Base44 apps, based on examples from Google’s own documentation and other Places API providers:

* **Trip planners** – Suggest restaurants, attractions, or hotels when someone picks a city.
* **Local business finders** – Let users search for nearby cafés, shops, or services.
* **Route helpers** – Show gas stations, rest stops, or food spots along a journey.
* **Real estate tools** – Highlight schools, parks, or shops near a property.
* **Emergency services locators** – Quickly find hospitals, police stations, or pharmacies.
* **City guides** – Build apps with curated landmarks, events, or lifestyle spots.

These examples illustrate just a few of the many ways you can use the Places API to add location‑aware features, search tools and personalized recommendations to your Base44 apps.


Built with [Mintlify](https://mintlify.com).