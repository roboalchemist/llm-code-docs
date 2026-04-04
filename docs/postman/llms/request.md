# request

The **Request** block is a special block that’s present by default in [Flows actions](/docs/postman-flows/build-flows/structure/actions/). The **Request** block takes request data sent to a deployed action’s URL and routes the data through its **Headers**, **Params**, and **Body** output ports. The **Request** block can’t be added or deleted.

> You can change a **Request** block to a **Schedule** block to run the action at regular intervals or at specific times. To learn how, see [Schedule an action to run automatically](/docs/postman-flows/build-flows/structure/actions/#schedule-an-action-to-run-automatically).

Prior to an action being deployed, the **Request** block takes the values for headers, parameters, and the request body that you store in [scenarios](/docs/postman-flows/build-flows/configure/scenarios/). By running different scenarios, you can test how your action will behave once it’s deployed. Testing with scenarios is necessary because the action won’t have a URL until you deploy it.

> The **Request** block can ingest input data of up to 5 megabytes if you’ve [purchased the Flows add-on](https://www.postman.com/pricing/), or 1 megabyte if you’re using Flows for free.

## Outputs

* **Headers** - Sends the request headers to the deployed action’s URL.
* **Params** - Sends the request’s query parameters to the deployed action’s URL.
* **Body** - Sends the request body to the deployed action’s URL. Actions support JSON, `form-data`, and `x-www-form-urlencoded` formats.

## Setup

The **Request** block itself requires no setup, but it does require you to create at least one scenario with data that the **Request** block can take as input. This is a prerequisite for testing your action locally. By testing, you verify that the blocks you add make your action perform the desired work.

The procedure for creating a scenario depends on the type and structure of the data you plan to send in the request body.

> This procedure assumes you already know the JSON structure of the action you’re creating will require, or that you have a correct example request body available to copy and paste. If that’s not the case, see [Send URL-encoded or form data to actions in Postman Flows](/docs/postman-flows/build-flows/structure/actions-form-data/).

1. Create a scenario and type or paste a correctly structured example request body into the **Body** field. For an empty request body, use the empty JSON object `{}`.
2. (Optional) Add content for the **Headers** and **Query Params** fields as needed.
3. Save and run the scenario.
4. Click the **Body** output of the **Request** block to open the block footer, and verify that the block emitted the correct request body, headers, and parameters.

## Related blocks

The **Request** block is one of the three blocks that every action has upon creation. The others are the [**Template**](/docs/postman-flows/reference/blocks/template/) and the [**Response**](/docs/postman-flows/reference/blocks/response/) block.