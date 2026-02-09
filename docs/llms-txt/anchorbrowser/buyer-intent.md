# Source: https://docs.anchorbrowser.io/examples/buyer-intent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Buyer Intent Discovery

The following example use-case shows how to find buyer-intent data based on Github stargazers of a Github project named 'Airflow'. A star from a person that works for a significant corporation can be a hint of buying intent in the data pipelines space.

<CodeGroup>
  ```tsx node.js theme={null}
  const result = await anchorClient.agent.task(
    `On the current stargazers list, return the GitHub profile URLs of all users
    that are a part of a well-known company. Then, do this for the first 3 pages
    using the "page" query parameter.
    Return a JSON array result: ["url1", "url2", ...].`,
    {
      taskOptions: {
        url: 'https://github.com/apache/airflow/stargazers?page=1',
      }
    }
  )
  console.log(result);
  ```

  ```python python theme={null}
  result = anchor_client.agent.task(
    '''On the current stargazers list, return the GitHub profile URLs of all users
    that are a part of a well-known company. Then, do this for the first 3 pages
    using the "page" query parameter.
    Return a JSON array result: ["url1", "url2", ...].''',
    task_options={
      'url': 'https://github.com/apache/airflow/stargazers?page=1',
    }
  )
  print(result)
  ```
</CodeGroup>
