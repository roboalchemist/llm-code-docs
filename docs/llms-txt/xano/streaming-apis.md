# Source: https://docs.xano.com/xano-ai/streaming-apis.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Streaming APIs

### Streaming API Request

<Frame>
  <iframe width="768" height="432" src="https://www.youtube.com/embed/SXIzhmcI1vo" title="Connecting to Streaming APIs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

You can use the Streaming External API Request endpoint to call an API that returns a stream in almost exactly the same way as you call normal APIs from your function stacks. The only difference is the structure of data returned, which would typically be an array of items that you would leverage a For Each loop to work with.

### Streaming API Response

When delivering certain types of API responses, you may want to 'stream' this response (similar to your favorite AI-powered chatbots). In Xano, this is possible with a simple combination of a For Each loop and a Streaming API Response function.

<Frame>
  <iframe width="768" height="432" src="https://www.youtube.com/embed/ldkcggSHuOA" title="Streaming API Responses with Xano" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

We'll be using a poem in the public domain to demonstrate the streaming response. You can copy the sample below and use it in your own function stacks to test.

```javascript  theme={null}
["Two roads diverged in a yellow wood,","And sorry I could not travel both","And be one traveler, long I stood","And looked down one as far as I could","To where it bent in the undergrowth;","","Then took the other, as just as fair,","And having perhaps the better claim,","Because it was grassy and wanted wear;","Though as for that the passing there","Had worn them really about the same,","","And both that morning equally lay","In leaves no step had trodden black.","Oh, I kept the first for another day!","Yet knowing how way leads on to way,","I doubted if I should ever come back.","","I shall be telling this with a sigh","Somewhere ages and ages hence:","Two roads diverged in a wood, and I—","I took the one less traveled by,","And that has made all the difference."]
```

Data that you use for a streaming response needs to be separated into logical pieces. In this example, each item in the array is a new line in the poem. It would typically make the most sense to build a streaming response against an array just for ease of implementation.

### Setting up a streaming response

* Set the API response type to 'streaming' from the API settings, or choose the streaming option when creating a new API endpoint.
  <Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/7a26500a-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=2bcd16876df9ad0389c6ab89f795124d" width="849" height="1351" data-path="images/7a26500a-image.jpeg" />
  </Frame>

* In your function stack, once you have the data you want to stream ready to go, use a For Each loop to start looping against each item in your array.
  <Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/89ed6f08-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=56dbebf1478d51c44483493e143b89da" width="900" height="405" data-path="images/89ed6f08-image.jpeg" />
  </Frame>

* Inside of the loop, use a **Streaming API Response** function to deliver each item inside of the array as the loop iterates through it.
  <Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/952b6c16-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=1f9e7b8d15f953f838654af194387494" width="900" height="430" data-path="images/952b6c16-image.jpeg" />
  </Frame>

* You can now test your streaming API, and should see each item in the array streamed as part of the response.

<Info>
  Please note that your front-end must support streaming responses. If it does not, the response can still be delivered traditionally.

  Using Run & Debug will not display a stream, and only the entire response once the stream has completed.
</Info>

### Testing your Streaming Response

#### Testing in Postman

* Create a new request with type HTTP

* Paste your API endpoint URL in the URL input, and click Send.

* You will see your API response delivered in the result panel.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/6022fd52-image.gif?s=6bb50554999beecd52abaf8cd38fb501" width="800" height="493" data-path="images/6022fd52-image.gif" />
</Frame>

#### Testing in Insomnia

* Create a new request with type Event Stream

* Paste your API endpoint URL in the URL input, and click Connect

* You will see your API response delivered in the result panel.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/dbeafd11-image.gif?s=5d30ad2a81011d1aa11edaf7fcdfa35d" width="800" height="456" data-path="images/dbeafd11-image.gif" />
</Frame>


Built with [Mintlify](https://mintlify.com).