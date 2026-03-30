# Source: https://www.nutrient.io/api/split-pdf-api/

---
description: Split PDFs into multiple files with Nutrient’s cloud API. Use DWS Processor for page-range extraction, packet separation, and automated PDF splitting workflows.
title: Split PDF API: Split PDFs into multiple files | Nutrient DWS Processor API
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

[PDF Editor](https://www.nutrient.io/api/pdf-editor-api/) 

Split 

* [Merge](https://www.nutrient.io/api/merge-pdf-api/)
* Split
* [Duplicate](https://www.nutrient.io/api/duplicate-pdf-page-api/)
* [Delete](https://www.nutrient.io/api/delete-pdf-page-api/)
* [Flatten](https://www.nutrient.io/api/flatten-pdf-api/)
* [Rotate](https://www.nutrient.io/api/pdf-rotate-api/)
* [Add pages](https://www.nutrient.io/api/add-page-api/)
* [Set page label](https://www.nutrient.io/api/set-page-label-api/)
* [JSON import](https://www.nutrient.io/api/instant-json-import-api/)
* [XFDF import](https://www.nutrient.io/api/xfdf-import-api/)

# Split PDF API

Split PDF documents into smaller, organized files using a PDF splitting API built for extracting specific sections, separating batches, packet routing, and automated document workflows.

[ Try for free ](https://dashboard.nutrient.io/sign%5Fup/?product=processor) 

##### Precise PDF splitting

Split PDFs by page ranges or document sections so downstream systems receive the exact file boundaries they need for routing, review, storage, or delivery.

##### Built for automated document routing

Use REST, Postman, JavaScript, Python, Java, C#, PHP, or HTTP to break large PDFs into smaller outputs for packet separation, export jobs, intake workflows, and archive-ready processing pipelines.

##### Simple and transparent pricing

Select a package that suits your needs according to the number of credits you wish to spend. Each API tool and action has a specific credit cost.

---

## Try it out

This example will split your document into two documents. The first PDF will contain all pages except the last five, and the second PDF will contain the remaining five pages.

---

Try it out in three steps

1. Add a PDF named `document.pdf` to your project folder.
2. Run the code from the same folder.
3. Open `first_half.pdf` in your project folder to view the results.

* [ SHELL ](#panel-0002au)
* [ SHELL (WINDOWS) ](#panel-0002av)
* [ JAVA ](#panel-0002aw)
* [ C# ](#panel-0002ax)
* [ JAVASCRIPT ](#panel-0002ay)
* [ PYTHON ](#panel-0002az)
* [ PHP ](#panel-0002b0)
* [ HTTP ](#panel-0002b1)

SHELL 

 SHELL  SHELL (WINDOWS)  JAVA  C#  JAVASCRIPT  PYTHON  PHP  HTTP 

```

curl -X POST https://api.nutrient.io/build \

  -H "Authorization: Bearer your_api_key_here" \

  -o first_half.pdf \

  --fail \

  -F document=@document.pdf \

  -F instructions='{

      "parts": [

        {

          "file": "document",

          "pages": {

            "end": -6

          }

        }

      ]

    }'


curl -X POST https://api.nutrient.io/build \

  -H "Authorization: Bearer your_api_key_here" \

  -o second_half.pdf \

  --fail \

  -F document=@document.pdf \

  -F instructions='{

      "parts": [

        {

          "file": "document",

          "pages": {

            "start": -5

          }

        }

      ]

    }'


```

```

curl -X POST https://api.nutrient.io/build ^

  -H "Authorization: Bearer your_api_key_here" ^

  -o first_half.pdf ^

  --fail ^

  -F document=@document.pdf ^

  -F instructions="{\"parts\": [{\"file\": \"document\", \"pages\": {\"end\": -6}}]}"


curl -X POST https://api.nutrient.io/build ^

  -H "Authorization: Bearer your_api_key_here" ^

  -o second_half.pdf ^

  --fail ^

  -F document=@document.pdf ^

  -F instructions="{\"parts\": [{\"file\": \"document\", \"pages\": {\"start\": -5}}]}"


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

    final RequestBody firstHalfBody = new MultipartBody.Builder()

      .setType(MultipartBody.FORM)

      .addFormDataPart(

        "document",

        "document.pdf",

        RequestBody.create(

          MediaType.parse("application/pdf"),

          new File("document.pdf")

        )

      )

      .addFormDataPart(

        "instructions",

        new JSONObject()

          .put("parts", new JSONArray()

            .put(new JSONObject()

              .put("file", "document")

              .put("pages", new JSONObject()

                .put("end", -6)

              )

            )

          ).toString()

      )

      .build();


    final Request firstHalfRequest = new Request.Builder()

      .url("https://api.nutrient.io/build")

      .method("POST", firstHalfBody)

      .addHeader("Authorization", "Bearer your_api_key_here")

      .build();


    final RequestBody secondHalfBody = new MultipartBody.Builder()

      .setType(MultipartBody.FORM)

      .addFormDataPart(

        "document",

        "document.pdf",

        RequestBody.create(

          MediaType.parse("application/pdf"),

          new File("document.pdf")

        )

      )

      .addFormDataPart(

        "instructions",

        new JSONObject()

          .put("parts", new JSONArray()

            .put(new JSONObject()

              .put("file", "document")

              .put("pages", new JSONObject()

                .put("start", -5)

              )

            )

          ).toString()

      )

      .build();


    final Request secondHalfRequest = new Request.Builder()

      .url("https://api.nutrient.io/build")

      .method("POST", secondHalfBody)

      .addHeader("Authorization", "Bearer your_api_key_here")

      .build();


    executeRequest(firstHalfRequest, "first_half.pdf");

    executeRequest(secondHalfRequest, "second_half.pdf");

  }


  private static void executeRequest(final Request request, final String outputFileName) throws IOException {

    final OkHttpClient client = new OkHttpClient()

      .newBuilder()

      .build();


    final Response response = client.newCall(request).execute();


    if (response.isSuccessful()) {

      Files.copy(

        response.body().byteStream(),

        FileSystems.getDefault().getPath(outputFileName),

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


      var firstHalfRequest = new RestRequest(Method.POST)

        .AddHeader("Authorization", "Bearer your_api_key_here")

        .AddFile("document", "document.pdf")

        .AddParameter("instructions", new JsonObject

        {

          ["parts"] = new JsonArray

          {

            new JsonObject

            {

              ["file"] = "document",

              ["pages"] = new JsonObject

              {

                ["end"] = -6

              }

            }

          }

        }.ToString());


      firstHalfRequest.AdvancedResponseWriter = OutputFileResponseWriter("first_half.pdf");


      var secondHalfRequest = new RestRequest(Method.POST)

        .AddHeader("Authorization", "Bearer your_api_key_here")

        .AddFile("document", "document.pdf")

        .AddParameter("instructions", new JsonObject

        {

          ["parts"] = new JsonArray

          {

            new JsonObject

            {

              ["file"] = "document",

              ["pages"] = new JsonObject

              {

                ["start"] = -5

              }

            }

          }

        }.ToString());


      secondHalfRequest.AdvancedResponseWriter = OutputFileResponseWriter("second_half.pdf");


      client.Execute(firstHalfRequest);

      client.Execute(secondHalfRequest);

    }


    static Action<Stream, IHttpResponse> OutputFileResponseWriter(string outputFileName)

    {

      return (responseStream, response) =>

      {

        if (response.StatusCode == HttpStatusCode.OK)

        {

          using (responseStream)

          {

            using var outputFileWriter = File.OpenWrite(outputFileName);

            responseStream.CopyTo(outputFileWriter);

          }

        }

        else

        {

          var responseStreamReader = new StreamReader(responseStream);

          Console.Write(responseStreamReader.ReadToEnd());

        }

      };

    }

  }

}


```

```

// This code requires Node.js. Do not run this code directly in a web browser.


const axios = require('axios')

const FormData = require('form-data')

const fs = require('fs')


;(async () => {

  const firstHalf = new FormData()

  firstHalf.append('instructions', JSON.stringify({

    parts: [

      {

        file: "document",

        pages: {

          end: -6

        }

      }

    ]

  }))

  firstHalf.append('document', fs.createReadStream('document.pdf'))


  const secondHalf = new FormData()

  secondHalf.append('instructions', JSON.stringify({

    parts: [

      {

        file: "document",

        pages: {

          start: -5

        }

      }

    ]

  }))

  secondHalf.append('document', fs.createReadStream('document.pdf'))


  await executeRequest(firstHalf, "first_half.pdf")

  await executeRequest(secondHalf, "second_half.pdf")

})()


async function executeRequest(formData, outputFile) {

  try {

    const response = await axios.post('https://api.nutrient.io/build', formData, {

      headers: formData.getHeaders({

        'Authorization': 'Bearer your_api_key_here'

      }),

      responseType: "stream"

    })


    response.data.pipe(fs.createWriteStream(outputFile))

  } catch (e) {

    const errorString = await streamToString(e.response.data)

    console.log(errorString)

  }

}


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


def process_first_half():

  response = requests.request(

    'POST',

    'https://api.nutrient.io/build',

    headers = {

      'Authorization': 'Bearer your_api_key_here'

    },

    files = {

      'document': open('document.pdf', 'rb')

    },

    data = {

      'instructions': json.dumps({

        'parts': [

          {

            'file': 'document',

            'pages': {

              'end': -6

            }

          }

        ]

      })

    },

    stream = True

  )


  if response.ok:

    with open('first_half.pdf', 'wb') as fd:

      for chunk in response.iter_content(chunk_size=8096):

        fd.write(chunk)

  else:

    print(response.text)

    exit()


def process_second_half():

  response = requests.request(

    'POST',

    'https://api.nutrient.io/build',

    headers = {

      'Authorization': 'Bearer your_api_key_here'

    },

    files = {

      'document': open('document.pdf', 'rb')

    },

    data = {

      'instructions': json.dumps({

        'parts': [

          {

            'file': 'document',

            'pages': {

              'start': -5

            }

          }

        ]

      })

    },

    stream = True

  )


  if response.ok:

    with open('second_half.pdf', 'wb') as fd:

      for chunk in response.iter_content(chunk_size=8096):

        fd.write(chunk)

  else:

    print(response.text)

    exit()


process_first_half()

process_second_half()


```

```

<?php


function process_first_half() {

  $FileHandle = fopen('first_half.pdf', 'w+');


  $curl = curl_init();


  curl_setopt_array($curl, array(

    CURLOPT_URL => 'https://api.nutrient.io/build',

    CURLOPT_CUSTOMREQUEST => 'POST',

    CURLOPT_RETURNTRANSFER => true,

    CURLOPT_ENCODING => '',

    CURLOPT_POSTFIELDS => array(

      'instructions' => '{

        "parts": [

          {

            "file": "document",

            "pages": {

              "end": -6

            }

          }

        ]

      }',

      'document' => new CURLFILE('document.pdf')

    ),

    CURLOPT_HTTPHEADER => array(

      'Authorization: Bearer your_api_key_here'

    ),

    CURLOPT_FILE => $FileHandle,

  ));


  $response = curl_exec($curl);


  curl_close($curl);


  fclose($FileHandle);

}


function process_second_half() {

  $FileHandle = fopen('second_half.pdf', 'w+');


  $curl = curl_init();


  curl_setopt_array($curl, array(

    CURLOPT_URL => 'https://api.nutrient.io/build',

    CURLOPT_CUSTOMREQUEST => 'POST',

    CURLOPT_RETURNTRANSFER => true,

    CURLOPT_ENCODING => '',

    CURLOPT_POSTFIELDS => array(

      'instructions' => '{

        "parts": [

          {

            "file": "document",

            "pages": {

              "start": -5

            }

          }

        ]

      }',

      'document' => new CURLFILE('document.pdf')

    ),

    CURLOPT_HTTPHEADER => array(

      'Authorization: Bearer your_api_key_here'

    ),

    CURLOPT_FILE => $FileHandle,

  ));


  $response = curl_exec($curl);


  curl_close($curl);


  fclose($FileHandle);

}


process_first_half();

process_second_half();


```

```

POST https://api.nutrient.io/build HTTP/1.1

Content-Type: multipart/form-data; boundary=--customboundary

Authorization: Bearer your_api_key_here


--customboundary

Content-Disposition: form-data; name="instructions"

Content-Type: application/json


{

  "parts": [

    {

      "file": "document",

      "pages": {

        "end": -6

      }

    }

  ]

}

--customboundary

Content-Disposition: form-data; name="document"; filename="document.pdf"

Content-Type: application/pdf


(document data)

--customboundary--


POST https://api.nutrient.io/build HTTP/1.1

Content-Type: multipart/form-data; boundary=--customboundary

Authorization: Bearer your_api_key_here


--customboundary

Content-Disposition: form-data; name="instructions"

Content-Type: application/json


{

  "parts": [

    {

      "file": "document",

      "pages": {

        "start": -5

      }

    }

  ]

}

--customboundary

Content-Disposition: form-data; name="document"; filename="document.pdf"

Content-Type: application/pdf


(document data)

--customboundary--


```

See all lines 

Using Postman? [Try this tool](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/iduiys4/split?tab=body) in our Postman collection and start using the API with a single click. [](/guides/dws-processor/getting-started/postman-collection)Read more → 

Your API key has automatically been inserted into the API example code. Run the sample code in your terminal to execute the API call. [See my API keys](https://dashboard.nutrient.io/processor-api/api%5Fkeys/). 

Start now

## Create an account to access your API key and start with 50 free credits per month

Start building with DWS Processor API in minutes — no payment information required.

[ SIGN UP ](https://dashboard.nutrient.io/sign%5Fup/) 

 Already have an account? [ Sign in → ](https://dashboard.nutrient.io/sign%5Fin/) 

---

Implementation options

## Validate split workflows before wiring them into packet-routing or document-delivery systems

Teams evaluating split PDF workflows usually need to confirm both the page-range behavior and the easiest integration path. Nutrient supports REST, Postman, JavaScript, Python, Java, C#, PHP, and raw HTTP so developers can test PDF splitting — separate documents by page range, chapter, or content boundary — with real files before connecting it to intake, export, routing, or archive workflows.

[ OPEN PROCESSOR API ](https://www.nutrient.io/api/processor-api/) 

 Continue to: 

[ Merge PDF If the workflow also needs to combine documents ](https://www.nutrient.io/api/merge-pdf-api/) [ Getting started For API key setup ](https://www.nutrient.io/guides/dws-processor/getting-started/) [ Postman collection For the fastest first request ](https://www.nutrient.io/guides/dws-processor/getting-started/postman-collection/) [ Processor API pricing For credits ](https://www.nutrient.io/api/pricing/processor-api/) [ Processor API overview For broader DWS evaluation of page, packet, and document splitting workflows ](https://www.nutrient.io/api/processor-api/) 

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