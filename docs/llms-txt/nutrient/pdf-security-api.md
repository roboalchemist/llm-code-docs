# Source: https://www.nutrient.io/api/pdf-security-api/

---
description: Protect PDFs with passwords, permissions, and document security controls using Nutrient’s cloud API. Use this secure PDF API for enterprise document delivery, regulated workflows, and protected content.
title: Secure PDF API for enterprise passwords, permissions, and document protection
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

# PDF security API

Protect sensitive PDF documents with a secure PDF API for enterprise workflows. Add password protection, disable printing, restrict copying, and apply access controls for secure document delivery, regulated workflows, and enterprise document handling.

[ Try for free ](https://dashboard.nutrient.io/sign%5Fup/?product=processor) 

##### Custom document protection

Add passwords, disable printing, and restrict copying so only authorized users can access or interact with protected PDFs.

##### Enterprise-ready security workflows

Use PDF permissions and password protection as part of a broader DWS platform with security, privacy, and SOC 2 Type 2 trust context for commercial evaluations.

##### Simple and transparent pricing

Select a package that suits your needs according to the number of credits you wish to spend. Each API tool and action has a specific credit cost.

---

## Try it out

This example protects a document with a password.

---

Try it out in three steps

1. Add a PDF named `document.pdf` to your project folder.
2. Run the code from the same folder.
3. Open `result.pdf` to see the output.

* [ SHELL ](#panel-0001yg)
* [ SHELL (WINDOWS) ](#panel-0001yh)
* [ JAVA ](#panel-0001yi)
* [ C# ](#panel-0001yj)
* [ JAVASCRIPT ](#panel-0001yk)
* [ PYTHON ](#panel-0001yl)
* [ PHP ](#panel-0001ym)
* [ HTTP ](#panel-0001yn)

SHELL 

 SHELL  SHELL (WINDOWS)  JAVA  C#  JAVASCRIPT  PYTHON  PHP  HTTP 

```

curl -X POST https://api.nutrient.io/build \

  -H "Authorization: Bearer your_api_key_here" \

  -o result.pdf \

  --fail \

  -F document=@document.pdf \

  -F instructions='{

      "parts": [

        {

          "file": "document"

        }

      ],

      "output": {

        "type": "pdf",

        "owner_password": "owner-password",

        "user_password": "user-password",

        "user_permissions": [

          "printing",

          "modification",

          "extract",

          "annotations_and_forms",

          "fill_forms",

          "extract_accessibility",

          "assemble",

          "print_high_quality"

        ]

      }

    }'


```

```

curl -X POST https://api.nutrient.io/build ^

  -H "Authorization: Bearer your_api_key_here" ^

  -o result.pdf ^

  --fail ^

  -F document=@document.pdf ^

  -F instructions="{\"parts\": [{\"file\": \"document\"}], \"output\": {\"type\": \"pdf\", \"owner_password\": \"owner-password\", \"user_password\": \"user-password\", \"user_permissions\": [\"printing\", \"modification\", \"extract\", \"annotations_and_forms\", \"fill_forms\", \"extract_accessibility\", \"assemble\", \"print_high_quality\"]}}"


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

            .put("type", "pdf")

            .put("owner_password", "owner-password")

            .put("user_password", "user-password")

            .put("user_permissions", new JSONArray()

              .put("printing")

              .put("modification")

              .put("extract")

              .put("annotations_and_forms")

              .put("fill_forms")

              .put("extract_accessibility")

              .put("assemble")

              .put("print_high_quality")

            )

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

            ["type"] = "pdf",

            ["owner_password"] = "owner-password",

            ["user_password"] = "user-password",

            ["user_permissions"] = new JsonArray

            {

              "printing",

              "modification",

              "extract",

              "annotations_and_forms",

              "fill_forms",

              "extract_accessibility",

              "assemble",

              "print_high_quality"

            }

          }

        }.ToString());


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


const formData = new FormData()

formData.append('instructions', JSON.stringify({

  parts: [

    {

      file: "document"

    }

  ],

  output: {

    type: "pdf",

    owner_password: "owner-password",

    user_password: "user-password",

    user_permissions: [

      "printing",

      "modification",

      "extract",

      "annotations_and_forms",

      "fill_forms",

      "extract_accessibility",

      "assemble",

      "print_high_quality"

    ]

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

        'type': 'pdf',

        'owner_password': 'owner-password',

        'user_password': 'user-password',

        'user_permissions': [

          'printing',

          'modification',

          'extract',

          'annotations_and_forms',

          'fill_forms',

          'extract_accessibility',

          'assemble',

          'print_high_quality'

        ]

      }

    })

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

<?php


$FileHandle = fopen('result.pdf', 'w+');


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

        "type": "pdf",

        "owner_password": "owner-password",

        "user_password": "user-password",

        "user_permissions": [

          "printing",

          "modification",

          "extract",

          "annotations_and_forms",

          "fill_forms",

          "extract_accessibility",

          "assemble",

          "print_high_quality"

        ]

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

    "type": "pdf",

    "owner_password": "owner-password",

    "user_password": "user-password",

    "user_permissions": [

      "printing",

      "modification",

      "extract",

      "annotations_and_forms",

      "fill_forms",

      "extract_accessibility",

      "assemble",

      "print_high_quality"

    ]

  }

}

--customboundary

Content-Disposition: form-data; name="document"; filename="document.pdf"

Content-Type: application/pdf


(document data)

--customboundary--


```

See all lines 

Using Postman? [Try this](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/evgkkkf/pdf-security?tab=body) in our Postman collection to start using the API with a single click. [](/guides/dws-processor/getting-started/postman-collection)Read more → 

Your API key has automatically been inserted into the API example code. Run the sample code in your terminal to execute the API call. [See my API keys](https://dashboard.nutrient.io/processor-api/api%5Fkeys/). 

Start now

## Create an account to access your API key and start with 50 free credits per month

Start building with DWS Processor API in minutes — no payment information required.

[ SIGN UP ](https://dashboard.nutrient.io/sign%5Fup/) 

 Already have an account? [ Sign in → ](https://dashboard.nutrient.io/sign%5Fin/) 

---

## Getting started

Use the PDF security guide for passwords and permissions, then continue to Processor pricing and DWS security documentation for broader enterprise evaluation.

[ GUIDES ](https://www.nutrient.io/guides/dws-processor/tools-and-api/pdf-security-api/) 

[ ![](https://www.nutrient.io/_astro/gs-password.BuRnXjcY_31FEL.png)  PDF passwords Owner and user passwords ](https://www.nutrient.io/guides/dws-processor/tools-and-api/pdf-security-api/#pdf-passwords)[ ![](https://www.nutrient.io/_astro/gs-permissions.CpM_I_8F_1XTyNd.png)  PDF permissions PDF permissions ](https://www.nutrient.io/guides/dws-processor/tools-and-api/pdf-security-api/#pdf-permissions) 

---

Most common next steps

## Connect PDF security evaluation to getting started, pricing, security, privacy, and the broader Processor platform

This page exists for secure PDF workflows where password protection and permissions must be explicit.

[ OPEN GETTING STARTED ](https://www.nutrient.io/guides/dws-processor/getting-started/) 

 After validating password and permissions workflows, continue to: 

[ Digital signatures If the workflow also needs certificate-based PDF signing ](https://www.nutrient.io/api/digital-signatures-api/) [ Getting started For API key setup ](https://www.nutrient.io/guides/dws-processor/getting-started/) [ Processor API pricing For credits and commercial review ](https://www.nutrient.io/api/pricing/processor-api/) [ Processor API overview For platform context ](https://www.nutrient.io/api/processor-api/) [ Security documentation When enterprise evaluation needs trust signals alongside implementation detail ](https://www.nutrient.io/guides/dws-processor/security/) [ Privacy documentation When enterprise evaluation needs trust signals alongside implementation detail ](https://www.nutrient.io/guides/dws-processor/privacy/) 

## Security is our top priority

##### No document storage

No input or resulting documents are stored on our infrastructure. All files are deleted as soon as a request finishes. Alternatively, [check out](https://www.nutrient.io/sdk/document-engine/) our self-hosted product.

##### HTTPS encryption

All communication between your application and Nutrient is done via HTTPS to ensure your data is encrypted when it’s sent to us.

##### Safe payment processing

All payments are handled by Paddle. Nutrient DWS Processor API never has direct access to any of your payment data.

## Ready to try it?

Create an account to get your DWS Processor API key and start making API calls.

[ START FOR FREE ](https://dashboard.nutrient.io/sign%5Fup/) 

---

ASK AI 