# Source: https://docs.curator.interworks.com/curator_api/getting_started/curator_api_overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Curator API Overview

> Complete guide to the Curator API including metadata access, content management and integration command capabilities.

The Integration System gives you many options for interfacing programmatically with the backend. This API
gives you access to the metadata behind your portal content as well as the ability to update content and run
integration commands.
Before you do, though, you'll need an API Key and the endpoint!

## 1. Obtaining an API Key

To access the API, you will need an API key. You can create an API Key in the /backend area of your portal.
API Keys are managed in Settings -> API Keys

## 2. Accessing the API

Once you have an API Key, you can access the API through the "api" folder on your portal's URL.
For example: `https://yourportal.example.com/api/v1/portal/upgrade?apikey=my_api_key_here`

## 3. API Response

All of the Integration System's APIs return JSON. You can convert this easily to an array in most languages.
(json\_decode, for example, in PHP)

## Auto Generate API Links

You can also use Curator's backend to generate links to the various Curator API endpoints

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **API Keys** section from the left-hand menu.
3. Change the dropdowns in the REST API to the respective endpoint you would like to try.
4. Use the preview link generated below the dropdowns to start using the endpoint.  *Note: Some variables may
   be missing from these preview links.*
