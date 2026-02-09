# Source: https://docs.zapier.com/platform/build/search.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a search action

## 1. Add the action settings

* Open the *Actions* tab in Zapier's Platform UI from the sidebar on the left, and select **Add Action**, selecting your action type. New actions are *create* type by default, and add new data or update existing data to your app.
  <Frame>
    <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3e47ad8a26c30fb761fdd60390d8705e.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=4461ae46885268b178266a66593cd5be" alt="Zapier Search action settings" data-og-width="809" width="809" data-og-height="723" height="723" data-path="images/3e47ad8a26c30fb761fdd60390d8705e.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3e47ad8a26c30fb761fdd60390d8705e.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=86b47d082e0b46bbcbc1d35119285bbf 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3e47ad8a26c30fb761fdd60390d8705e.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=44313664d713e8e65cdc09864125325a 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3e47ad8a26c30fb761fdd60390d8705e.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=04463d389b32e49c33c62a2a7a1bd803 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3e47ad8a26c30fb761fdd60390d8705e.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=9fb9e66a8c975f2e4d0d1f91b37545ee 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3e47ad8a26c30fb761fdd60390d8705e.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=ce403f78dc6a2ef8de887ed3dd2c33ba 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3e47ad8a26c30fb761fdd60390d8705e.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=b3a9aa7292e5ee609ce2e6ce87903e03 2500w" />
  </Frame>

<Info>
  **Note**: You cannot change an action type once you click *Save and Continue*
  on a new action. If you need to change the action type, delete the action and
  recreate it.
</Info>

* On the Settings page, specify the following:

– **Key**: A unique identifier for this action, used to reference the action inside Zapier. Does not need to be the same identifier as used in your API. Not shown to users.

– **Name**: A human friendly plain text name for this action, typically with a verb such as *Find* or *Search* followed by the name of the item this action will find in your app. The title-case name is shown in Zapier products and on Zapier's app directory marketing pages.

– **Noun**: A single noun that describes what this action searches, used by Zapier products to auto-generate text about your action.

– **Description**: A plain text sentence that describes what the action does and when it should be used. Shown inside Zapier products and on Zapier's app directory marketing pages. Start with the word “Find”.

– **Visibility Options**: An option to select when this action will be shown. *Shown* is chosen by default.

* At the bottom of the settings page, you'll see an option to pair your *search* with a *create* action. That lets your [action also create an item](/platform/build/search-or-create) if the search does not return any results.

* Click on the *Save and Continue* button.

## 2. Complete the Input Designer

On the *Input Designer* page, add user [input fields](/platform/build/add-fields) for this action. All action steps *must* include an input form for Zapier to gather the data needed to create or find items in your app. Add at least one input field to your action.

Before building your action's input form, list each piece of data your app needs to find an item. Most search actions only include a single input field, sometimes along with a drop-down menu to select filter data.

## 3. Set up the API Configuration

In the final *API Configuration* page, add the API endpoint where Zapier will send the search request to.

A `GET` call is used for search actions by default, and sends the data from the input form to your API endpoint.

Zapier expects an array response with 0 or more items.

If multiple matches are found, return a reasonable number of items. Pagination is not supported, and returning too many results will produce errors. Although by default Zaps only use the first result, users [*can* decide](https://help.zapier.com/hc/en-us/articles/8496241402253-Search-for-existing-data-in-Zaps) to group all results as [line items](https://help.zapier.com/hc/en-us/articles/8496277737997). Other products like Agents will always use all results. Do not group multiple results as line items yourself, as this will conflict with allowing products and users to control this.

If no matches are found, an empty array must be returned - even if the API responds with a `404` status. A *search* that returns no results is still considered a successful action step and [should not return an error](/platform/build/response-types).

If you need to parse the response from the endpoint into the expected response type, switch to [Code Mode](/platform/build/code-mode) to write custom JavaScript code for your action.

## 4. Test your API request

Configure test data to [test the *search* action](/platform/build/test-triggers-actions). Testing a GET request would be expected to return the item from the endpoint.

## 5. Define your output

Define sample data and output fields following [the guide](/platform/build/sample-data).

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
