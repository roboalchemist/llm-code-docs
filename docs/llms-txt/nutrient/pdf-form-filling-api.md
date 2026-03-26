# Source: https://www.nutrient.io/api/pdf-form-filling-api/

---
description: Integrate a PDF form filler API to import and fill PDF forms in your app. Supports XFDF and JSON.
title: PDF form filler API: Fill form fields in PDFs
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

# PDF form filling API

Integrate our PDF form filler API to import and fill PDF forms in your application or workflow.

[ Try for free ](https://dashboard.nutrient.io/sign%5Fup/?product=processor) 

##### Dynamic, data-driven filling

Import data into fillable fields across any PDF form using a simple JSON structure.

##### Automate with Zapier

Automatically fill new PDF forms in Google Drive using our Zapier integration. Just upload a form and your data, and Nutrient will handle the rest.

[ CONNECT WITH ZAPIER ](https://zapier.com/apps/google-drive/integrations/google-drive/255622201/fill-new-pdf-forms-in-google-drive-with-nutrient-api-and-upload-to-google-drive) 

##### Seamless integration

Easily connect to your apps or workflows to generate prefilled forms for contracts, registration, compliance, and more.

---

## Try it out

This example will import Instant JSON to fill forms in a PDF.

---

Try it out in three steps

1. Add `forms.pdf` and `form-filling.json` to your project folder.
2. Run the code from the same folder.
3. Open `result.pdf` to see the output.

* [ SHELL ](#panel-0001wo)
* [ SHELL (WINDOWS) ](#panel-0001wp)
* [ JAVA ](#panel-0001wq)
* [ C# ](#panel-0001wr)
* [ JAVASCRIPT ](#panel-0001ws)
* [ PYTHON ](#panel-0001wt)
* [ PHP ](#panel-0001wu)
* [ HTTP ](#panel-0001wv)

SHELL 

 SHELL  SHELL (WINDOWS)  JAVA  C#  JAVASCRIPT  PYTHON  PHP  HTTP 

```

curl -X POST https://api.nutrient.io/build \

  -H "Authorization: Bearer your_api_key_here" \

  -o result.pdf \

  --fail \

  -F document=@form.pdf \

  -F form_filling.json=@form_filling.json \

  -F instructions='{

      "parts": [

        {

          "file": "document"

        }

      ],

      "actions": [

        {

          "type": "applyInstantJson",

          "file": "form_filling.json"

        }

      ]

    }'


```

```

curl -X POST https://api.nutrient.io/build ^

  -H "Authorization: Bearer your_api_key_here" ^

  -o result.pdf ^

  --fail ^

  -F document=@form.pdf ^

  -F form_filling.json=@form_filling.json ^

  -F instructions="{\"parts\": [{\"file\": \"document\"}], \"actions\": [{\"type\": \"applyInstantJson\", \"file\": \"form_filling.json\"}]}"


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

        "form.pdf",

        RequestBody.create(

          MediaType.parse("application/pdf"),

          new File("form.pdf")

        )

      )

      .addFormDataPart(

        "form_filling.json",

        "form_filling.json",

        RequestBody.create(

          MediaType.parse("application/json"),

          new File("form_filling.json")

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

          .put("actions", new JSONArray()

            .put(new JSONObject()

              .put("type", "applyInstantJson")

              .put("file", "form_filling.json")

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

        .AddFile("document", "form.pdf")

        .AddFile("form_filling.json", "form_filling.json")

        .AddParameter("instructions", new JsonObject

        {

          ["parts"] = new JsonArray

          {

            new JsonObject

            {

              ["file"] = "document"

            }

          },

          ["actions"] = new JsonArray

          {

            new JsonObject

            {

              ["type"] = "applyInstantJson",

              ["file"] = "form_filling.json"

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

  actions: [

    {

      type: "applyInstantJson",

      file: "form_filling.json"

    }

  ]

}))

formData.append('document', fs.createReadStream('form.pdf'))

formData.append('form_filling.json', fs.createReadStream('form_filling.json'))


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

    'document': open('form.pdf', 'rb'),

    'form_filling.json': open('form_filling.json', 'rb')

  },

  data = {

    'instructions': json.dumps({

      'parts': [

        {

          'file': 'document'

        }

      ],

      'actions': [

        {

          'type': 'applyInstantJson',

          'file': 'form_filling.json'

        }

      ]

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

      "actions": [

        {

          "type": "applyInstantJson",

          "file": "form_filling.json"

        }

      ]

    }',

    'document' => new CURLFILE('form.pdf'),

    'form_filling.json' => new CURLFILE('form_filling.json')

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

  "actions": [

    {

      "type": "applyInstantJson",

      "file": "form_filling.json"

    }

  ]

}

--customboundary

Content-Disposition: form-data; name="document"; filename="form.pdf"

Content-Type: application/pdf


(document data)

--customboundary

Content-Disposition: form-data; name="form_filling.json"; filename="form_filling.json"

Content-Type: application/json


(form_filling.json data)

--customboundary--


```

See all lines 

Using Postman? [Download our official collection](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/overview) and start using the API with a single click. [](/guides/dws-processor/getting-started/postman-collection)Read more → 

Your API key has automatically been inserted into the API example code. Run the sample code in your terminal to execute the API call. [See my API keys](https://dashboard.nutrient.io/processor-api/api%5Fkeys/). 

Start now

## Create an account to access your API key and start with 50 free credits per month

Start building with DWS Processor API in minutes — no payment information required.

[ SIGN UP ](https://dashboard.nutrient.io/sign%5Fup/) 

 Already have an account? [ Sign in → ](https://dashboard.nutrient.io/sign%5Fin/) 

---

## Instant JSON

The Instant JSON format is the native annotation format of the Nutrient API, and it defines an extensive number of annotation types and properties for your documents. Use this format to programmatically generate robust, feature-rich annotations for your documents.

[ INSTANT JSON REFERENCE ](https://www.nutrient.io/api/reference/document-engine/instant-json/) 

![Instant JSON annotation format](https://www.nutrient.io/_astro/instant-json.CtVXg0L__Z2h5wIs.png) 

---

Most common next steps

## Connect form-filling workflows to getting started, pricing, and broader form import automation

[ OPEN GETTING STARTED ](https://www.nutrient.io/guides/dws-processor/getting-started/) 

 After validating PDF form filling, continue to: 

[ PDF form creator If the workflow also needs to add new form fields ](https://www.nutrient.io/api/pdf-form-creator-api/) [ Getting started For API key setup ](https://www.nutrient.io/guides/dws-processor/getting-started/) [ Postman collection For the fastest first request ](https://www.nutrient.io/guides/dws-processor/getting-started/postman-collection/) [ Processor API pricing For credits ](https://www.nutrient.io/api/pricing/processor-api/) [ Processor API overview For broader DWS evaluation ](https://www.nutrient.io/api/processor-api/) [ Instant JSON import API When form filling depends on JSON payloads ](https://www.nutrient.io/api/instant-json-import-api/) [ XFDF import API When form filling depends on XFDF payloads ](https://www.nutrient.io/api/xfdf-import-api/) 

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