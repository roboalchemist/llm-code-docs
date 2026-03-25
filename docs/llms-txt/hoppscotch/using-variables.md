# Source: https://docs.hoppscotch.io/documentation/getting-started/graphql/using-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.hoppscotch.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Using variables in a GraphQL query

> Learn how to use variables in a GraphQL query.

Hoppscotch allows you to pass variables in the query to fetch data dynamically.

To demonstrate the use of variables, let's write a query to get countries by their `name` and `continent`. For example, we will fetch the details of **"Bahrain"** from the **"Asia"** continent.

## Variables

Go to the variables section and define the variable.

```json  theme={null}
{
  "countryName": "Bahrain",
  "continentCode": "AS"
}
```

## Using the variable in the query

Now create a query `getCountries` with variables as shown below:

```graphql  theme={null}
  query getCountries($countryName: String!, $continentCode: String!) {
    countries(filter: {name: {eq: $countryName}, continent: {eq: $continentCode}}) {
      name
      continent {
        name
      }
      code
      emoji
      currencies
    }
  }
```

Hoppscotch will retrieve the value of the variable and execute the query to get the below response.

```json  theme={null}
  {
    "data": {
      "countries": [
        {
          "name": "Bahrain",
          "continent": {
            "name": "Asia"
          },
          "code": "BH",
          "emoji": "🇧🇭",
          "currencies": [
            "BHD"
          ]
        }
      ]
    }
  }
```


Built with [Mintlify](https://mintlify.com).