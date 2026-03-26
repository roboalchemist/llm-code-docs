# Source: https://www.nutrient.io/api/url-to-pdf-api/

---
description: Save development time with an accurate and reliable URL-to-PDF API. High-quality conversions keep colors, images, text, fonts, and metadata from original documents.
title: URL-to-PDF API | Nutrient DWS Processor API
image: https://cdn.prod.website-files.com/65fdb7696055f07a05048833/6717c1324bc009b855df63a7_Nutrient.jpg
---

Search

ASK AI SEARCH CODE EXAMPLES 

RESULTS

ASK AI ASSISTANT

SUGGESTED FILTERS

OTHER WAYS TO CONNECT

[ Schedule a call ](#) [ Email Sales ](mailto:sales@nutrient.io) [ Technical support ](https://support.nutrient.io/hc/en-us/requests/new) 

Loading content... 

# URL-to-PDF API

Convert URL to PDF files with our URL-to-PDF API.

[ Try for free ](https://dashboard.nutrient.io/sign%5Fup/?product=processor) 

##### Accurate web-to-PDF rendering

Capture the full content, layout, and styling of any webpage — including HTML, CSS, images, and fonts — just like it appears in the browser.

##### Automate with Zapier

Automatically convert webpage URLs in Google Drive to PDF using our Zapier integration. A fast, no-code way to generate PDFs from URLs.

[ CONNECT WITH ZAPIER ](https://zapier.com/apps/google-drive/integrations/google-drive/255621765/convert-new-web-page-urls-in-google-drive-to-pdf-with-nutrient-api-and-save-to-them-to-google-drive) 

##### Perfect for automation and archiving

Create PDFs from URLs for invoices, blog posts, dashboards, terms of service, and more without opening a browser.

---

## Try it out

This example will download a file from a URL and convert it to a PDF.

---

Try it out in two steps

1. Copy the code and run it.
2. Open `result.pdf` to see the output.

* [ SHELL ](#panel-0002da)
* [ SHELL (WINDOWS) ](#panel-0002db)
* [ JAVA ](#panel-0002dc)
* [ C# ](#panel-0002dd)
* [ JAVASCRIPT ](#panel-0002de)
* [ PYTHON ](#panel-0002df)
* [ PHP ](#panel-0002dg)
* [ HTTP ](#panel-0002dh)

SHELL 

 SHELL  SHELL (WINDOWS)  JAVA  C#  JAVASCRIPT  PYTHON  PHP  HTTP 

```

curl -X POST https://api.nutrient.io/build \

  -H "Content-Type: application/json" \

  -H "Authorization: Bearer your_api_key_here" \

  -o result.pdf \

  --fail \

  -d '{

      "parts": [

        {

          "file": {

            "url": "https://www.nutrient.io/api/assets/downloads/samples/docx/document.docx"

          }

        }

      ]

    }'


```

```

curl -X POST https://api.nutrient.io/build ^

  -H "Content-Type: application/json" ^

  -H "Authorization: Bearer your_api_key_here" ^

  -o result.pdf ^

  --fail ^

  -d "{\"parts\": [{\"file\": {\"url\": \"https://www.nutrient.io/api/assets/downloads/samples/docx/document.docx\"}}]}"


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

    final MediaType mediaType = MediaType.parse("application/json");

    final RequestBody body = RequestBody.create(

      mediaType,

      new JSONObject()

        .put("parts", new JSONArray()

          .put(new JSONObject()

            .put("file", new JSONObject()

              .put("url", "https://www.nutrient.io/api/assets/downloads/samples/docx/document.docx")

            )

          )

        ).toString()

    );


    final Request request = new Request.Builder()

      .url("https://api.nutrient.io/build")

      .method("POST", body)

      .addHeader("Content-Type", "application/json")

      .addHeader("Authorization", "Bearer your_api_key_here")

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

      var client = new RestClient("https://api.nutrient.io/build");


      var request = new RestRequest(Method.POST)

        .AddHeader("Authorization", "Bearer your_api_key_here")

        .AddJsonBody(new JsonObject

          {

            ["parts"] = new JsonArray

            {

              new JsonObject

              {

                ["file"] = new JsonObject

                {

                  ["url"] = "https://www.nutrient.io/api/assets/downloads/samples/docx/document.docx"

                }

              }

            }

          });


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

// This code requires Node.js. Do not run this code directly in a web browser.


const axios = require('axios')

const FormData = require('form-data')

const fs = require('fs')


const body = JSON.stringify({

  parts: [

    {

      file: {

        url: "https://www.nutrient.io/api/assets/downloads/samples/docx/document.docx"

      }

    }

  ]

})


;(async () => {

  try {

    const response = await axios.post('https://api.nutrient.io/build', body, {

      headers: {

        'Content-Type': 'application/json',

        'Authorization': 'Bearer your_api_key_here'

      },

      responseType: "stream"

    })


    response.data.pipe(fs.createWriteStream("result.pdf"))

  } catch (e) {

    const errorString = await streamToString(e.response.data)

    console.log(errorString)

  }

})()


function streamToString(stream) {

  const chunks = []

  return new Promise((resolve, reject) => {

    stream.on("data", (chunk) => chunks.push(Buffer.from(chunk)))

    stream.on("error", (err) => reject(err))

    stream.on("end", () => resolve(Buffer.concat(chunks).toString("utf8")))

  })

}


```

```

import requests

import json


body = json.dumps({

  'parts': [

    {

      'file': {

        'url': 'https://www.nutrient.io/api/assets/downloads/samples/docx/document.docx'

      }

    }

  ]

})


response = requests.request(

  'POST',

  'https://api.nutrient.io/build',

  headers = {

    'Content-Type': 'application/json',

    'Authorization': 'Bearer your_api_key_here'

  },

  data = body,

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

<?php


$FileHandle = fopen('result.pdf', 'w+');


$curl = curl_init();


$body = '{

  "parts": [

    {

      "file": {

        "url": "https://www.nutrient.io/api/assets/downloads/samples/docx/document.docx"

      }

    }

  ]

}';


curl_setopt_array($curl, array(

  CURLOPT_URL => 'https://api.nutrient.io/build',

  CURLOPT_CUSTOMREQUEST => 'POST',

  CURLOPT_RETURNTRANSFER => true,

  CURLOPT_ENCODING => '',

  CURLOPT_POSTFIELDS => $body,

  CURLOPT_HTTPHEADER => array(

    'Content-Type: application/json',

    'Authorization: Bearer your_api_key_here'

  ),

  CURLOPT_FILE => $FileHandle,

));


$response = curl_exec($curl);


curl_close($curl);


fclose($FileHandle);


```

```

POST https://api.nutrient.io/build HTTP/1.1

Content-Type: application/json

Authorization: Bearer your_api_key_here


{

  "parts": [

    {

      "file": {

        "url": "https://www.nutrient.io/api/assets/downloads/samples/docx/document.docx"

      }

    }

  ]

}


```

See all lines 

Using Postman? [Check out our Postman collection](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/overview) and start using the API with a single click. [](/guides/dws-processor/getting-started/postman-collection)Read more → 

Your API key has automatically been inserted into the API example code. Run the sample code in your terminal to execute the API call. [See my API keys](https://dashboard.nutrient.io/processor-api/api%5Fkeys/). 

Start now

## Create an account to access your API key and start with 50 free credits per month

Start building with DWS Processor API in minutes — no payment information required.

[ SIGN UP ](https://dashboard.nutrient.io/sign%5Fup/) 

 Already have an account? [ Sign in → ](https://dashboard.nutrient.io/sign%5Fin/) 

---

Most common next steps

## Connect URL-to-PDF evaluation to getting started, pricing, and broader web-to-document workflows

[ OPEN GETTING STARTED ](https://www.nutrient.io/guides/dws-processor/getting-started/) 

 After validating URL-to-PDF output, continue to: 

[ HTML-to-PDF If the source is raw HTML with CSS templates rather than a live URL ](https://www.nutrient.io/api/html-to-pdf-api/) [ Getting started For API key setup ](https://www.nutrient.io/guides/dws-processor/getting-started/) [ Postman collection For the fastest first request ](https://www.nutrient.io/guides/dws-processor/getting-started/postman-collection/) [ Processor API pricing For credits ](https://www.nutrient.io/api/pricing/processor-api/) [ Processor API overview For broader DWS evaluation of web page, HTML, and URL-based PDF generation workflows ](https://www.nutrient.io/api/processor-api/) 

---

## Security is our top priority

##### No document storage

No input or resulting documents are stored on our infrastructure. All files are deleted as soon as a request finishes. Alternatively, [check out](https://www.nutrient.io/sdk/document-engine/) our self-hosted product.

##### HTTPS encryption

All communication between your application and Nutrient is done via HTTPS to ensure your data is encrypted when it’s sent to us.

##### Safe payment processing

All payments are handled by Paddle. Nutrient DWS Processor API never has direct access to any of your payment data.

---

## Ready to try it?

Create an account to get your DWS Processor API key and start making API calls.

[ START FOR FREE ](https://dashboard.nutrient.io/sign%5Fup/) 

---

ASK AI 