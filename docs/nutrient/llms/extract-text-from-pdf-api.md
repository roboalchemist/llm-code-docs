# Source: https://www.nutrient.io/api/extract-text-from-pdf-api/

---
description: Extract text from PDFs with Nutrient’s cloud API. Use DWS Processor for PDF text extraction, searchable content workflows, and structured document-processing pipelines.
title: Extract text from PDF API for document text workflows | Nutrient
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

[Data Extraction](https://www.nutrient.io/api/data-extraction-api/) 

Text extraction 

* Text extraction
* [Key-value pair extraction](https://www.nutrient.io/api/key-value-pair-extraction-api/)
* [Image-to-text API](https://www.nutrient.io/api/image-to-text-api/)

# Extract text from PDF API

Build workflows to automatically extract text from PDF documents with a text extraction API built for document-processing systems. Use Nutrient DWS when you need PDF text output for indexing, search, compliance review, downstream AI pipelines, or structured data workflows.

[ TRY FOR FREE ](https://dashboard.nutrient.io/sign%5Fup/?product=processor) 

##### PDF text extraction built for document workflows

Extract text from PDF files when the next step is search, indexing, review, compliance, analytics, or feeding document text into another processing system.

##### Use REST, Postman, or your preferred language

Use REST, Postman, JavaScript, Python, Java, C#, PHP, or HTTP to automate text extraction from PDFs inside backend workflows and document-processing pipelines.

##### Ideal for downstream text workflows

Use extracted PDF text for knowledge retrieval, search indexes, document QA, AI pipelines, or other systems that need clean text output instead of rendered pages.

---

## Try it out

This example will extract text from an image and return it as a JSON file.

---

Try it out in three steps

1. Add a PDF named `document.pdf` to your project folder.
2. Run the code from the same folder.
3. Open `result.json` to see the output.

* [ SHELL ](#panel-0000s8)
* [ SHELL (WINDOWS) ](#panel-0000s9)
* [ JAVA ](#panel-0000sa)
* [ C# ](#panel-0000sb)
* [ JAVASCRIPT ](#panel-0000sc)
* [ PYTHON ](#panel-0000sd)
* [ PHP ](#panel-0000se)
* [ HTTP ](#panel-0000sf)

SHELL 

 SHELL  SHELL (WINDOWS)  JAVA  C#  JAVASCRIPT  PYTHON  PHP  HTTP 

```

curl -X POST https://api.nutrient.io/build \

  -H "Authorization: Bearer your_api_key_here" \

  -o result.json \

  --fail \

  -F document=@document.pdf \

  -F instructions='{

      "parts": [

        {

          "file": "document"

        }

      ],

      "output": {

        "type": "json-content",

        "plainText": true,

        "structuredText": true

      }

    }'


```

```

curl -X POST https://api.nutrient.io/build ^

  -H "Authorization: Bearer your_api_key_here" ^

  -o result.json ^

  --fail ^

  -F document=@document.pdf ^

  -F instructions="{\"parts\": [{\"file\": \"document\"}], \"output\": {\"type\": \"json-content\", \"plainText\": true, \"structuredText\": true}}"


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

            )

          )

          .put("output", new JSONObject()

            .put("type", "json-content")

            .put("plainText", true)

            .put("structuredText", true)

          ).toString()

      )

      .build();


    final Request request = new Request.Builder()

      .url("https://api.nutrient.io/build")

      .method("POST", body)

      .addHeader("Authorization", "Bearer your_api_key_here")

      .build();


    final OkHttpClient client = new OkHttpClient()

      .newBuilder()

      .build();


    final Response response = client.newCall(request).execute();


    if (response.isSuccessful()) {

      Files.copy(

        response.body().byteStream(),

        FileSystems.getDefault().getPath("result.json"),

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

        .AddFile("document", "document.pdf")

        .AddParameter("instructions", new JsonObject

        {

          ["parts"] = new JsonArray

          {

            new JsonObject

            {

              ["file"] = "document"

            }

          },

          ["output"] = new JsonObject

          {

            ["type"] = "json-content",

            ["plainText"] = true,

            ["structuredText"] = true

          }

        }.ToString());


      request.AdvancedResponseWriter = (responseStream, response) =>

      {

        if (response.StatusCode == HttpStatusCode.OK)

        {

          using (responseStream)

          {

            using var outputFileWriter = File.OpenWrite("result.json");

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


const formData = new FormData()

formData.append('instructions', JSON.stringify({

  parts: [

    {

      file: "document"

    }

  ],

  output: {

    type: "json-content",

    plainText: true,

    structuredText: true

  }

}))

formData.append('document', fs.createReadStream('document.pdf'))


;(async () => {

  try {

    const response = await axios.post('https://api.nutrient.io/build', formData, {

      headers: formData.getHeaders({

        'Authorization': 'Bearer your_api_key_here'

      }),

      responseType: "stream"

    })


    response.data.pipe(fs.createWriteStream("result.json"))

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

          'file': 'document'

        }

      ],

      'output': {

        'type': 'json-content',

        'plainText': True,

        'structuredText': True

      }

    })

  },

  stream = True

)


if response.ok:

  with open('result.json', 'wb') as fd:

    for chunk in response.iter_content(chunk_size=8096):

      fd.write(chunk)

else:

  print(response.text)

  exit()


```

```

<?php


$FileHandle = fopen('result.json', 'w+');


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

          "file": "document"

        }

      ],

      "output": {

        "type": "json-content",

        "plainText": true,

        "structuredText": true

      }

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

      "file": "document"

    }

  ],

  "output": {

    "type": "json-content",

    "plainText": true,

    "structuredText": true

  }

}

--customboundary

Content-Disposition: form-data; name="document"; filename="document.pdf"

Content-Type: application/pdf


(document data)

--customboundary--


```

See all lines 

Using Postman? [Download our official collection](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/overview) and start using the API with a single click. [](/guides/dws-processor/getting-started/postman-collection)Read more → 

Your API key has automatically been inserted into this API example code. Run this sample code in your terminal to execute the API call. [See your API key](https://dashboard.nutrient.io/processor-api/api%5Fkeys/). 

---

Start now

## Create an account to access your API key and start with 50 free credits per month

Start building with DWS Processor API in minutes — no payment information required.

[ SIGN UP ](https://dashboard.nutrient.io/sign%5Fup/) 

 Already have an account? [ Sign in → ](https://dashboard.nutrient.io/sign%5Fin/) 

---

Implementation options

## Validate PDF text extraction before wiring it into a larger search or AI system

Teams exploring extract-text-from-PDF workflows often need to confirm both the text quality and the easiest integration path. Nutrient supports REST, Postman, curl, JavaScript, Python, Java, C#, PHP, and raw HTTP so developers can test PDF text extraction with real files before connecting it to search, compliance review, analytics, or AI ingestion systems.

[ OPEN PROCESSOR API ](https://www.nutrient.io/api/processor-api/) 

 Continue to: 

[ PDF-to-Markdown API If the workflow needs Markdown output instead of plain text for RAG and AI ingestion ](https://www.nutrient.io/api/pdf-to-md-api/) [ Getting started For API key setup ](https://www.nutrient.io/guides/dws-processor/getting-started/) [ Postman collection For the fastest first request ](https://www.nutrient.io/guides/dws-processor/getting-started/postman-collection/) [ Processor API pricing For credits ](https://www.nutrient.io/api/pricing/processor-api/) [ Processor API overview For broader DWS evaluation of text extraction workflows ](https://www.nutrient.io/api/processor-api/) 

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