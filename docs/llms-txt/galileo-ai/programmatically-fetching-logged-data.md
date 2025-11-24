# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/how-to/programmatically-fetching-logged-data.md

# Programmatically Fetching Logged Data

> Fetch logged data programmatically in Galileo Observe with step-by-step instructions for seamless integration into automated workflows and analysis tools.

If you want to fetch your logged data and metrics programmatically, you can do so via our Typescript and Python clients or via our REST APIs:

<Tabs>
  <Tab title="Typescript">
    First, npm install `@rungalileo/observe`

    Then add the following to your project:

    ```ts
        import { ApiClient } from "@rungalileo/observe";
        const apiClient = new ApiClient();
        await apiClient.init("YOUR_PROJECT_NAME");
    ```

    You can use this with `getLoggedData` to retrieve the raw data.

    ```ts
        // Optional
        const filters = [{ col_name: "model", operator: "eq", value: "gpt-3.5-turbo" }];

        // Optional
        const sort_spec = [{ col_name: "created_at", sort_dir: "asc" }];

        const rows = await apiClient.getLoggedData(
        "2024-03-11T16:15:28.294Z", // ISO start_time string with timezone
        "2024-03-12T16:15:28.294Z", // ISO end_time string with timezone
        filters, // (optional) See above for an example.
        sort_spec, // (optional) See above for an example
        limit // a number of items to return
        );
        console.log(rows);
    ```
  </Tab>

  <Tab title="Python">
    First, see the [Quickstart guide](/galileo/gen-ai-studio-products/galileo-observe/getting-started) for installing galileo\_observe and using it in your project.

    ```py
        ...
        observe = GalileoObserve(project_name=MY_PROJECT_NAME)
        ...
    ```

    ```py
        filters = [{"col_name": "model", "operator": "eq", "value": "gpt-3.5-turbo"}]
        sort_spec = [{"col_name": "created_at", "sort_dir": "asc"}]

        # ISO start and end time strings with timezone
        start = "2024-03-11T16:15:28.294Z"
        end = "2024-03-12T16:15:28.294Z"

        rows = observe.get_logged_data(filters=filters, sort_spec=sort_spec)
        print(rows)

        metrics = observe.get_metrics(
            start_time=end,
            end_time=end,
            filters=[
                {
                    "col_name": "metrics",
                    "json_field": "cost",
                    "json_field_type": "float",
                    "operator": "gte",
                    "value": 0,
                }
            ],
        )
        print(metrics)
    ```
  </Tab>

  <Tab title="REST endpoints">
    Fetching data via our RESTful APIs is a two-step process:
    1 Authentication
    2 Fetching

    ### Authentication

    To fetch an authentication token, send a `POST` request to `/login` with your `username` and `password`:

    ```py
        import requests

        base_url = YOUR_BASE_URL #see below for instructions to get your base_url

        headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
        'username': '{YOUR_USERNAME}',
        'password': '{YOUR_PASSWORD}',
        }

        response = requests.post(f'{base_url}/login', headers=headers, data=data)

        access_token = response.json()["access_token"]
    ```

    Note: `access_token` will need to be refreshed every 48 hours for security reasons.

    Reach out to us if you don't know your 'base\_url'. For most users, this is the same as their console URL except with the word 'console' replaced by 'api' (e.g. [http://www.\*\*console\*\*.galileo.myenterprise.com](http://www.**console**.galileo.myenterprise.com) -> [http://www.\*\*api\*\*.galileo.myenterprise.com](http://www.**api**.galileo.myenterprise.com))

    ### Fetching

    Once you have your auth token, you can start making ingestion calls to Galileo Observe.

    #### Project ID

    To log data, you'll need your project ID. Get your project ID by making a GET request to the `/projects` endpoint, or simply copy it from the URL in your browser window. This project ID is static and will never change. You only have to do this once.

    ```py
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {access_token}"}

    response = requests.get(f"{base_url}/projects", headers=headers,
                            params={"project_name": "{YOUR_PROJECT_NAME}"}
                            )
    project_id = response.json()[0]["id"]
    ```

    #### Fetching all records

    To fetch a list of your records, make a `POST` the `/observe/rows` endpoint:

    ```py
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {access_token}"}

    records = requests.post(f"{base_url}/projects/{project_id}/observe/rows",
                            headers=headers)
    ```

    Additional query params:

    * `include_chains`: False by default.

    * `start_time` / `end_time`: Use to limit your request to a specific time window (e.g. "2018-11-12T09:15:32Z")

    * `chain_id`: Fetch a specific chain.˝

    * `limit`: Integer. Limit your the search to the n most recent records.

    #### Fetching aggregate metrics

    To fetch a list of aggregate metrics bucketed over time, make a `POST` request to the `/observe/metrics/` endpoint:

    ```py
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {access_token}"}

    records = requests.post(f"{base_url}/projects/{project_id}/observe/metrics",
                            headers=headers)
    ```

    Additional query params:

    * `include_chains`: False by default.

    * `start_time` / `end_time`: Use to limit your request to a specific time window (e.g. "2018-11-12 09:15:32")
  </Tab>
</Tabs>
