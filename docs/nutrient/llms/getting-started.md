# Source: https://www.nutrient.io/guides/dws-processor/getting-started/

---
description: Step-by-step guide to get started with DWS Processor API using the dashboard, a live API key, and first-request examples.
title: Getting started with DWS Processor API
image: https://cdn.prod.website-files.com/65fdb7696055f07a05048833/6717c1324bc009b855df63a7_Nutrient.jpg
---

# Getting started with DWS Processor API

Copy page 

[ Copy pageCopy page as Markdown for LLMs ](#) [ View as MarkdownView this page as plain text ](#) [ Open with ChatGPTExplain the page with ChatGPT ](#) [ Open with ClaudeExplain the page with Claude ](#) [ Open with GrokExplain the page with Grok ](#) 

Nutrient Document Web Services (DWS) Processor API is a service that enables fast and easy integration to instantly generate, convert, and modify PDF documents in your workflows.

Use this guide when you want a DWS Processor get started path via the dashboard, need to create a free trial account, get a live API key, and make your first request.

If you need broader evaluation context before making that first call, continue to the [Processor API overview](https://www.nutrient.io/api/processor-api/), [Processor API pricing](https://www.nutrient.io/api/pricing/processor-api/), or the [Postman collection](https://www.nutrient.io/guides/dws-processor/getting-started/postman-collection/).

## [ ](#try-it-in-30-seconds) Try it in 30 seconds 

Want to see it in action right away? Copy and paste these commands into your terminal:

Terminal window

```

# Create sample HTML.

echo '<html><body><h1>Hello from Nutrient!</h1></body></html>' > index.html


# Convert to PDF (replace YOUR_API_KEY).

curl -X POST 'https://api.nutrient.io/build' \

  -H 'Authorization: Bearer YOUR_API_KEY' \

  -F 'index.html=@index.html' \

  -F 'instructions={"parts":[{"html":"index.html"}]}' \

  -o hello.pdf


```

Get your API key by [signing up(opens in a new tab)](https://dashboard.nutrient.io/sign%5Fup/?product=processor) for free. Then replace `YOUR_API_KEY` in the command above with your key.

## [ ](#getting-started) Getting started 

1. [Sign up(opens in a new tab)](https://dashboard.nutrient.io/sign%5Fup/?product=processor) for a free account in the DWS dashboard. The signup link preselects DWS Processor API for you.
2. If you’re prompted to choose a product, click **Get Started** on the Processor API card.  
    
![DWS Processor API card](https://www.nutrient.io/_astro/dws-processor-api-highlighted-on-dashboard.BHaqBF6S_20V8fo.png)
3. Copy your live API key and select an [API tool(opens in a new tab)](https://dashboard.nutrient.io/processor-api/playground/) to get started. Below you’ll see a demonstration of the PDF generation API.  
> To make requests using your account, pass the API key to every call you make.
4. Add an HTML file named `index.html` to your project folder. You can also use our [sample file](https://www.nutrient.io/api/assets/downloads/samples/html/index.html).
5. Copy the code below and run it from the same folder you added the files to. For a list of all programming languages that support HTTP requests, refer to our [supported languages](https://www.nutrient.io/guides/dws-processor/supported-languages/) guide.

* [ HTTP ](#panel-0003gg)
* [ PHP ](#panel-0003gh)
* [ Python ](#panel-0003gi)
* [ JavaScript ](#panel-0003gj)
* [ C# ](#panel-0003gk)
* [ Java ](#panel-0003gl)
* [ Shell ](#panel-0003gm)
* [ Shell (Windows) ](#panel-0003gn)

HTTP 

 HTTP  PHP  Python  JavaScript  C#  Java  Shell  Shell (Windows) 

```

POST https://api.nutrient.io/processor/generate_pdf HTTP/1.1

Content-Type: multipart/form-data; boundary=--customboundary

Authorization: Bearer <add-your-live-API-key-here>


--customboundary

Content-Disposition: form-data; name="html"; filename="index.html"

Content-Type: text/html


(html data)

--customboundary--


```

```

<?php


$FileHandle = fopen('result.pdf', 'w+');


$curl = curl_init();


curl_setopt_array($curl, array(

  CURLOPT_URL => 'https://api.nutrient.io/processor/generate_pdf',

  CURLOPT_CUSTOMREQUEST => 'POST',

  CURLOPT_RETURNTRANSFER => true,

  CURLOPT_ENCODING => '',

  CURLOPT_POSTFIELDS => array(

    'html' => new CURLFILE('index.html')

  ),

  CURLOPT_HTTPHEADER => array(

    'Authorization: Bearer <add-your-live-API-key-here>'

  ),

  CURLOPT_FILE => $FileHandle,

));


$response = curl_exec($curl);


curl_close($curl);


fclose($FileHandle);


```

```

import requests

import json


response = requests.request(

  'POST',

  'https://api.nutrient.io/processor/generate_pdf',

  headers = {

    'Authorization': 'Bearer <add-your-live-API-key-here>'

  },

  files = {

    'html': open('index.html', 'rb')

  },

  stream = True

)


if response.ok:

  with open('result.pdf', 'wb') as fd:

    for chunk in response.iter_content(chunk_size=8096):

      fd.write(chunk)

else:

  print(response.text)

  exit()


```

```

// This code requires Node.js. Do not run this code directly in a web browser.


const axios = require("axios");

const FormData = require("form-data");

const fs = require("fs");


const formData = new FormData();

formData.append("html", fs.createReadStream("index.html"));

(async () => {

  try {

    const response = await axios.post(

      "https://api.nutrient.io/processor/generate_pdf",

      formData,

      {

        headers: formData.getHeaders({

          Authorization: "Bearer <add-your-live-API-key-here>",

        }),

        responseType: "stream",

      },

    );


    response.data.pipe(fs.createWriteStream("result.pdf"));

  } catch (e) {

    const errorString = await streamToString(e.response.data);

    console.log(errorString);

  }

})();


function streamToString(stream) {

  const chunks = [];

  return new Promise((resolve, reject) => {

    stream.on("data", (chunk) => chunks.push(Buffer.from(chunk)));

    stream.on("error", (err) => reject(err));

    stream.on("end", () => resolve(Buffer.concat(chunks).toString("utf8")));

  });

}


```

```

using System;

using System.IO;

using System.Net;

using RestSharp;


namespace PspdfkitApiDemo

{

  class Program

  {

    static void Main(string[] args)

    {

      var client = new RestClient("https://api.nutrient.io/processor/generate_pdf");


      var request = new RestRequest(Method.POST)

        .AddHeader("Authorization", "Bearer <add-your-live-API-key-here>")

        .AddFile("html", "index.html");


      request.AdvancedResponseWriter = (responseStream, response) =>

      {

        if (response.StatusCode == HttpStatusCode.OK)

        {

          using (responseStream)

          {

            using var outputFileWriter = File.OpenWrite("result.pdf");

            responseStream.CopyTo(outputFileWriter);

          }

        }

        else

        {

          var responseStreamReader = new StreamReader(responseStream);

          Console.Write(responseStreamReader.ReadToEnd());

        }

      };


      client.Execute(request);

    }

  }

}


```

```

package com.example.pspdfkit;


import java.io.File;

import java.io.IOException;

import java.nio.file.FileSystems;

import java.nio.file.Files;

import java.nio.file.StandardCopyOption;


import org.json.JSONArray;

import org.json.JSONObject;


import okhttp3.MediaType;

import okhttp3.MultipartBody;

import okhttp3.OkHttpClient;

import okhttp3.Request;

import okhttp3.RequestBody;

import okhttp3.Response;


public final class PspdfkitApiExample {

  public static void main(final String[] args) throws IOException {

    final RequestBody body = new MultipartBody.Builder()

      .setType(MultipartBody.FORM)

      .addFormDataPart(

        "html",

        "index.html",

        RequestBody.create(

          MediaType.parse("text/html"),

          new File("index.html")

        )

      )

      .build();


    final Request request = new Request.Builder()

      .url("https://api.nutrient.io/processor/generate_pdf")

      .method("POST", body)

      .addHeader("Authorization", "Bearer <add-your-live-API-key-here>")

      .build();


    final OkHttpClient client = new OkHttpClient()

      .newBuilder()

      .build();


    final Response response = client.newCall(request).execute();


    if (response.isSuccessful()) {

      Files.copy(

        response.body().byteStream(),

        FileSystems.getDefault().getPath("result.pdf"),

        StandardCopyOption.REPLACE_EXISTING

      );

    } else {

      // Handle the error

      throw new IOException(response.body().string());

    }

  }

}


```

Terminal window

```

curl -X POST https://api.nutrient.io/processor/generate_pdf \

  -H "Authorization: Bearer <add-your-live-API-key-here>" \

  -o result.pdf \

  --fail \

  -F html=@index.html


```

Terminal window

```

curl -X POST https://api.nutrient.io/processor/generate_pdf ^

  -H "Authorization: Bearer <add-your-live-API-key-here>" ^

  -o result.pdf ^

  --fail ^

  -F html=@index.html


```

Similarly, you can use other DWS Processor API endpoints to convert, modify, and manipulate documents. To explore more endpoints, [try other DWS Processor API endpoints(opens in a new tab)](https://dashboard.nutrient.io/processor-api/playground/) in our API playground, browse the full set of available task pages on the [Processor API overview](https://www.nutrient.io/api/processor-api/) and [tools overview](https://www.nutrient.io/api/tools-overview/), or consult the [REST API reference](https://www.nutrient.io/api/reference/public/) for detailed endpoint documentation.

---

### Was this helpful?

YES 

NO 

### Help us improve

0 / 2000 characters

Cancel Send 

### Thank you for your feedback!

### Something went wrong. Please try again or let us know.

Try Again [Contact Us](https://www.nutrient.io/company/contact/) 

---

 On this page 

## On this page

ASK AI 

```json
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.nutrient.io/guides/dws-processor/getting-started/"
  },
  "headline": "Getting started with DWS Processor API",
  "description": "Step-by-step guide to get started with DWS Processor API using the dashboard, a live API key, and first-request examples.",
  "inLanguage": "en-US",
  "articleSection": "Getting Started",
  "wordCount": 338,
  "publisher": {
    "@type": "Organization",
    "name": "Nutrient",
    "logo": {
      "@type": "ImageObject",
      "url": "https://www.nutrient.io/_astro/nutrient-logo.CJxiofUP_19DKCs.svg"
    },
    "sameAs": [
      "https://www.nutrient.io/company/about",
      "https://www.linkedin.com/company/nutrientdocs",
      "https://www.facebook.com/nutrientdocs/",
      "https://x.com/nutrientdocs"
    ]
  },
  "author": {
    "@type": "Organization",
    "name": "Nutrient Documentation Team"
  }
}
```
