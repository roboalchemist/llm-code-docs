# Source: https://novita.ai/docs/api-reference/model-apis-image-to-prompt.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Image to Prompt

**This API extracts prompts from images.**

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="image_file" type="string" required={true}>
  The base64-encoded original image, with a maximum resolution of 2048 x 2048 pixels and a maximum file size of 30 MB.
</ParamField>

## Response

<ResponseField name="prompt" type="string" required={false}>
  The prompt generated from the input image.
</ResponseField>

## Example

This API retrieves prompts from images.

Please set the **`Content-Type`** header to **`application/json`** in your HTTP request to indicate that you are sending JSON data. Currently, **only JSON format is supported**.

`Request:`

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/img2prompt' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data '{
    "image_file": "{{Base64 encoded image}}"
}'
```

HTTP status codes in the 2xx range indicate that the request has been successfully accepted. A status code of 400 means there is an error with the request parameters, while status codes in the 5xx range indicate internal server errors.

You can find the generated prompt in the `prompt` field of the response.

`Image`:

<Frame>
  <img src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/img2prompt.png" />
</Frame>

`Response:`

```js  theme={"system"}
{
    "prompt": "a man standing on a rock near the ocean, Alejandro Iñárritu, Nadav Kander, Ignacio Fernández Ríos, Ignacio Fernández Ríos, Ignacio Ríos, Navid Negahban, Reza Afshar, Steven Klein, Ignacio Fernández Ríos, Lorenzo Lanfranconi, Peter Palombi, Alberto Mielgo"
}
```


Built with [Mintlify](https://mintlify.com).