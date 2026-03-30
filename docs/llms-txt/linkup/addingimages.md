# Source: https://docs.linkup.so/pages/changelog/addingimages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding Images

> _Released: January 07, 2025_

We're excited to introduce the ability to include images in your search results. This new feature allows you to retrieve relevant images alongside your regular search data.

### How to Enable

To include images in your search results, simply add `includeImages=true` to your API request.

**Example Request**

```shell curl theme={null}
curl --request POST \
  --url https://api.linkup.so/v1/search \
  --header 'Authorization: Bearer {{LINKUP_API_KEY}}' \
  --header 'Content-Type: application/json' \
  --data '{
  "q": "Who is Barack Obama?",
  "depth": "standard",
  "outputType": "searchResults",
  "includeImages": "true"
}'
```

**Example Response**

```json json theme={null}
{
  "results": [
    {
      "type": "image",
      "name": "Barack Obama | Biography, Presidency, & Facts | Britannica.com",
      "url": "https://cdn.britannica.com/43/172743-138-545C299D/overview-Barack-Obama.jpg"
    },
    {
      "type": "text",
      "name": "Barack Obama Biography",
      "url": "https://www.biography.com/political-figures/barack-obama",
      "content": "Barack Obama was the 44th president of the United States and the first Black commander-in-chief. He served two terms, from 2009 until 2017."
    }
  ]
}
```


Built with [Mintlify](https://mintlify.com).