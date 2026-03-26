# Source: https://www.nutrient.io/api/merge-pdf-api/

---
description: Reduce development time with a merge PDF API that lets you combine and merge multiple PDFs in your iOS, Android, web, or desktop applications. Try it free.
title: Merge PDF API: Easily combine multiple PDFs | Nutrient DWS Processor API
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

Merge 

* Merge
* [Split](https://www.nutrient.io/api/split-pdf-api/)
* [Duplicate](https://www.nutrient.io/api/duplicate-pdf-page-api/)
* [Delete](https://www.nutrient.io/api/delete-pdf-page-api/)
* [Flatten](https://www.nutrient.io/api/flatten-pdf-api/)
* [Rotate](https://www.nutrient.io/api/pdf-rotate-api/)
* [Add pages](https://www.nutrient.io/api/add-page-api/)
* [Set page label](https://www.nutrient.io/api/set-page-label-api/)
* [JSON import](https://www.nutrient.io/api/instant-json-import-api/)
* [XFDF import](https://www.nutrient.io/api/xfdf-import-api/)

# Merge PDF API

Combine multiple PDF files into a single, organized document using a fast, secure, and reliable PDF merging API. Perfect for reports, archives, or batch processing.

[ Try for free ](https://dashboard.nutrient.io/sign%5Fup/?product=processor) 

##### Seamless document merging

Merge PDFs in any order with full control over page sequence. Ideal for assembling invoices, contracts, scanned forms, or multipart reports.

##### Automate with Zapier

Automatically merge new PDF files in Google Drive using our Zapier integration. Simply drop your PDFs into a folder, and let the Nutrient API handle the rest.

[ CONNECT WITH ZAPIER ](https://zapier.com/apps/google-drive/integrations/google-drive/255622171/merge-new-pdf-files-in-google-drive-using-nutrient-api-and-upload-to-google-drive) 

##### Simple and transparent pricing

Select a package that suits your needs according to the number of credits you wish to spend. Each API tool and action has a specific credit cost.

---

## Try it out

This example will merge the two supplied documents into one PDF. The order of the documents in the final PDF is controlled by the order of the `parts` array.

---

Try it out in three steps

1. Add two scanned PDFs named `first-half.pdf` and `second-half.pdf` to your project folder.
2. Run the code from the same folder.
3. Open `result.pdf` to see the output.

* [ SHELL ](#panel-0001c0)
* [ SHELL (WINDOWS) ](#panel-0001c1)
* [ JAVA ](#panel-0001c2)
* [ C# ](#panel-0001c3)
* [ JAVASCRIPT ](#panel-0001c4)
* [ PYTHON ](#panel-0001c5)
* [ PHP ](#panel-0001c6)
* [ HTTP ](#panel-0001c7)

SHELL 

 SHELL  SHELL (WINDOWS)  JAVA  C#  JAVASCRIPT  PYTHON  PHP  HTTP 

```

curl -X POST https://api.nutrient.io/build \

  -H "Authorization: Bearer your_api_key_here" \

  -o result.pdf \

  --fail \

  -F first_half=@first_half.pdf \

  -F second_half=@second_half.pdf \

  -F instructions='{

      "parts": [

        {

          "file": "first_half"

        },

        {

          "file": "second_half"

        }

      ]

    }'


```

```

curl -X POST https://api.nutrient.io/build ^

  -H "Authorization: Bearer your_api_key_here" ^

  -o result.pdf ^

  --fail ^

  -F first_half=@first_half.pdf ^

  -F second_half=@second_half.pdf ^

  -F instructions="{\"parts\": [{\"file\": \"first_half\"}, {\"file\": \"second_half\"}]}"


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

        "first_half",

        "first_half.pdf",

        RequestBody.create(

          MediaType.parse("application/pdf"),

          new File("first_half.pdf")

        )

      )

      .addFormDataPart(

        "second_half",

        "second_half.pdf",

        RequestBody.create(

          MediaType.parse("application/pdf"),

          new File("second_half.pdf")

        )

      )

      .addFormDataPart(

        "instructions",

        new JSONObject()

          .put("parts", new JSONArray()

            .put(new JSONObject()

              .put("file", "first_half")

            )

            .put(new JSONObject()

              .put("file", "second_half")

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

        .AddFile("first_half", "first_half.pdf")

        .AddFile("second_half", "second_half.pdf")

        .AddParameter("instructions", new JsonObject

        {

          ["parts"] = new JsonArray

          {

            new JsonObject

            {

              ["file"] = "first_half"

            },

            new JsonObject

            {

              ["file"] = "second_half"

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

      file: "first_half"

    },

    {

      file: "second_half"

    }

  ]

}))

formData.append('first_half', fs.createReadStream('first_half.pdf'))

formData.append('second_half', fs.createReadStream('second_half.pdf'))


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

    'first_half': open('first_half.pdf', 'rb'),

    'second_half': open('second_half.pdf', 'rb')

  },

  data = {

    'instructions': json.dumps({

      'parts': [

        {

          'file': 'first_half'

        },

        {

          'file': 'second_half'

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

          "file": "first_half"

        },

        {

          "file": "second_half"

        }

      ]

    }',

    'first_half' => new CURLFILE('first_half.pdf'),

    'second_half' => new CURLFILE('second_half.pdf')

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

      "file": "first_half"

    },

    {

      "file": "second_half"

    }

  ]

}

--customboundary

Content-Disposition: form-data; name="first_half"; filename="first_half.pdf"

Content-Type: application/pdf


(first_half data)

--customboundary

Content-Disposition: form-data; name="second_half"; filename="second_half.pdf"

Content-Type: application/pdf


(second_half data)

--customboundary--


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

## Connect PDF merge evaluation to getting started, pricing, and broader document combination workflows

[ OPEN GETTING STARTED ](https://www.nutrient.io/guides/dws-processor/getting-started/) 

 After validating PDF merge behavior, continue to: 

[ Split PDF If the workflow also needs to separate documents ](https://www.nutrient.io/api/split-pdf-api/) [ Getting started For API key setup ](https://www.nutrient.io/guides/dws-processor/getting-started/) [ Postman collection For the fastest first request ](https://www.nutrient.io/guides/dws-processor/getting-started/postman-collection/) [ Processor API pricing For credits ](https://www.nutrient.io/api/pricing/processor-api/) [ Processor API overview For broader DWS evaluation of combine, batch, and document assembly workflows ](https://www.nutrient.io/api/processor-api/) 

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