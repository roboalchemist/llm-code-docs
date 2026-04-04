# Source: https://www.nutrient.io/api/pdf-to-md-api/

---
description: Plug &#38; play PDF to Markdown Conversion API. Easily integrate our API to get fast &#38; accurate PDF to Markdown conversions in your iOS, Android, Web app.
title: PDF to Markdown API: Convert PDF to Markdown | Nutrient
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

[Markup converter API](https://www.nutrient.io/api/pdf-to-markup-api/) 

PDF-to-Markdown API 

* [PDF-to-markup API](https://www.nutrient.io/api/pdf-to-markup-api/)
* [PDF-to-HTML API](https://www.nutrient.io/api/pdf-to-html-api/)
* PDF-to-Markdown API

# PDF-to-Markdown API

Convert PDF files to Markdown using our PDF to Markdown API.

[ Try for free ](https://dashboard.nutrient.io/sign%5Fin/) 

##### Preserve layout and formatting

Accurately convert text, headings, tables, and styles into Markdown format while maintaining the structure of the original PDF.

##### Automate with Zapier

Automatically convert PDF files in Google Drive to Markdown using our Zapier integration. It's the fastest way to turn web content into documents without writing code.

[ CONNECT WITH ZAPIER ](https://zapier.com/apps/google-drive/integrations/google-drive/255620380/convert-new-html-files-in-google-drive-to-pdfs-with-nutrient-document-web-services-api) 

##### Simple and transparent pricing

Select a package that suits your needs according to the number of credits you wish to spend. Each API tool and action has a specific credit cost.

---

## Try it out

This example will convert your uploaded PDF file to an MD.

---

Try it out in three steps

1. Add a PDF file named `document.pdf` to your project folder.
2. Run the code from the same folder.
3. Open `result.md` in your project folder to view the results.

* [ SHELL ](#panel-000214)
* [ SHELL (WINDOWS) ](#panel-000215)
* [ JAVA ](#panel-000216)
* [ C# ](#panel-000217)
* [ JAVASCRIPT ](#panel-000218)
* [ PYTHON ](#panel-000219)
* [ PHP ](#panel-00021a)
* [ HTTP ](#panel-00021b)

SHELL 

 SHELL  SHELL (WINDOWS)  JAVA  C#  JAVASCRIPT  PYTHON  PHP  HTTP 

```

curl -X POST https://api.nutrient.io/build \

  -H "Authorization: Bearer your_api_key_here" \

  -o result.md \

  --fail \

  -F file=@document.pdf \

  -F instructions='{

      "parts": [

        {

          "file": "file"

        }

      ],

      "output": {

        "type": "markdown"

      }

    }'


```

```

curl -X POST https://api.nutrient.io/build ^

  -H "Authorization: Bearer your_api_key_here" ^

  -o result.md ^

  --fail ^

  -F file=@document.pdf ^

  -F instructions="{\"parts\": [{\"file\": \"file\"}], \"output\": {\"type\": \"markdown\"}}"


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

        "file",

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

              .put("file", "file")

            )

          )

          .put("output", new JSONObject()

            .put("type", "markdown")

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

        FileSystems.getDefault().getPath("result.md"),

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

        .AddFile("file", "document.pdf")

        .AddParameter("instructions", new JsonObject

        {

          ["parts"] = new JsonArray

          {

            new JsonObject

            {

              ["file"] = "file"

            }

          },

          ["output"] = new JsonObject

          {

            ["type"] = "markdown"

          }

        }.ToString());


      request.AdvancedResponseWriter = (responseStream, response) =>

      {

        if (response.StatusCode == HttpStatusCode.OK)

        {

          using (responseStream)

          {

            using var outputFileWriter = File.OpenWrite("result.md");

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

      file: "file"

    }

  ],

  output: {

    type: "markdown"

  }

}))

formData.append('file', fs.createReadStream('document.pdf'))


;(async () => {

  try {

    const response = await axios.post('https://api.nutrient.io/build', formData, {

      headers: formData.getHeaders({

        'Authorization': 'Bearer your_api_key_here'

      }),

      responseType: "stream"

    })


    response.data.pipe(fs.createWriteStream("result.md"))

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

    'file': open('document.pdf', 'rb')

  },

  data = {

    'instructions': json.dumps({

      'parts': [

        {

          'file': 'file'

        }

      ],

      'output': {

        'type': 'markdown'

      }

    })

  },

  stream = True

)


if response.ok:

  with open('result.md', 'wb') as fd:

    for chunk in response.iter_content(chunk_size=8096):

      fd.write(chunk)

else:

  print(response.text)

  exit()


```

```

<?php


$FileHandle = fopen('result.md', 'w+');


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

          "file": "file"

        }

      ],

      "output": {

        "type": "markdown"

      }

    }',

    'file' => new CURLFILE('document.pdf')

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

      "file": "file"

    }

  ],

  "output": {

    "type": "markdown"

  }

}

--customboundary

Content-Disposition: form-data; name="file"; filename="document.pdf"

Content-Type: application/pdf


(file data)

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