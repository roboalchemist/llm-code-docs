# Source: https://redocly.com/docs/realm/customization/api-functions/create-api-functions.md

# Create API functions

Here are two examples of API functions:

- weather service
- authentication system


To select an example, click either the **Weather API** or **Authentication** filter at the top of the page.

To use this example, generate a free API key from weatherapi.com.

Import the necessary types from the Redocly configuration.
These types provide TypeScript definitions for the request and context objects.

Define the main API function that handles the request.
The function takes two parameters:

- request
- context


Add custom authentication (optional)
Add authentication validation to ensure only authenticated users can access the weather data.
This helper function verifies the session token from cookies.

Add a check to verify the user's authentication status before processing the request.
This code prevents unauthorized access to your API.

Extract query parameters with `context.query` and validate them.
The weather API requires a location parameter (`q`).

Access the API key from environment variables using `process.env`.
Environment variables are a secure way to store sensitive information like API keys.

Make a call to the external weather API using `fetch` API, and validate the response.

Format and return the weather data in a structured JSON response.

Implement error handling for API requests to manage failures and provide useful error messages to clients.

Import the necessary types for authentication.

Define the main API function that handles the request.
The function takes two parameters:

- request
- context


Extract and validate the username and password from the request body.

Generate a session token for authenticated users.
In a production application, you would use a proper JWT library.

Set a secure cookie with the session token to maintain the user's authenticated state.

Return a success response with user information.

Implement error handling to manage authentication failures and provide error responses.

## Reference documentation

To learn more about API functions, see the [API functions reference](/docs/realm/customization/api-functions/api-functions-reference) for available helper methods and properties.