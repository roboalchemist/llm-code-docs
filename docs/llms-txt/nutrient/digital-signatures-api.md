# Source: https://www.nutrient.io/api/digital-signatures-api/

---
description: Use this API to sign PDFs digitally with certificate-based, legally binding signatures. Nutrient’s digital signatures API is SOC 2-audited and supports compliance standards like eIDAS and US and Canadian laws.
title: API to sign PDFs digitally with certificates and compliance-ready workflows | Nutrient
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

# Digital signatures API

Use this API to sign PDFs digitally with SOC 2-audited, certificate-based workflows. Sign, manage, and validate legally binding documents in your apps, websites, and platforms using a reliable cloud API.

[ TRY FOR FREE ](https://dashboard.nutrient.io/sign%5Fup/?product=processor) 

##### Legally binding and cryptographically secure

Digitally sign PDF documents with digital certificates that support legal, regulatory, and compliance-oriented workflows such as eIDAS and related enterprise signing requirements.

##### Built for seamless integration

Use REST, Postman, JavaScript, Python, Java, C#, PHP, or HTTP to sign and validate PDF documents in your own platform without dealing with complex certificate workflows or signing infrastructure.

##### Try it instantly on Zapier

No code? No problem. Cryptographically sign new PDF files in Google Drive using our Zapier integration, and automatically save the signed copies back to Google Drive.

[ CONNECT WITH ZAPIER ](https://zapier.com/apps/google-drive/integrations/google-drive/255621909/cryptographically-sign-new-pdf-files-in-google-drive-with-nutrient-api-and-add-them-to-google-drive) 

---

## Try it out

This example will sign your document with a Nutrient certificate.

---

Try it out in three steps

1. Add a PDF named `document.pdf` to your project folder.
2. Run the code from the same folder.
3. Open `result.pdf` to see the output.

* [ SHELL ](#panel-0000lk)
* [ SHELL (WINDOWS) ](#panel-0000ll)
* [ JAVA ](#panel-0000lm)
* [ C# ](#panel-0000ln)
* [ JAVASCRIPT ](#panel-0000lo)
* [ PYTHON ](#panel-0000lp)
* [ PHP ](#panel-0000lq)
* [ HTTP ](#panel-0000lr)

SHELL 

 SHELL  SHELL (WINDOWS)  JAVA  C#  JAVASCRIPT  PYTHON  PHP  HTTP 

```

curl -X POST https://api.nutrient.io/sign \

  -H "Authorization: Bearer your_api_key_here" \

  -o result.pdf \

  --fail \

  -F file=@document.pdf \

  -F data='{

      "signatureType": "cades",

      "cadesLevel": "b-lt"

    }'


```

```

curl -X POST https://api.nutrient.io/sign ^

  -H "Authorization: Bearer your_api_key_here" ^

  -o result.pdf ^

  --fail ^

  -F file=@document.pdf ^

  -F data="{\"signatureType\": \"cades\", \"cadesLevel\": \"b-lt\"}"


```

```

package com.example.pspdfkit;


import java.io.File;

import java.io.IOException;

import java.nio.file.FileSystems;

import java.nio.file.Files;

import java.nio.file.StandardCopyOption;


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

        "data",

        new JSONObject()

          .put("signatureType", "cades")

          .put("cadesLevel", "b-lt").toString()

      )

      .build();


    final Request request = new Request.Builder()

      .url("https://api.nutrient.io/sign")

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

      var client = new RestClient("https://api.nutrient.io/sign");


      var request = new RestRequest(Method.POST)

        .AddHeader("Authorization", "Bearer your_api_key_here")

        .AddFile("file", "document.pdf")

        .AddParameter("data", new JsonObject

        {

          ["signatureType"] = "cades",

          ["cadesLevel"] = "b-lt"

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

formData.append('data', JSON.stringify({

  signatureType: "cades",

  cadesLevel: "b-lt"

}))

formData.append('file', fs.createReadStream('document.pdf'))


;(async () => {

  try {

    const response = await axios.post('https://api.nutrient.io/sign', formData, {

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

  'https://api.nutrient.io/sign',

  headers = {

    'Authorization': 'Bearer your_api_key_here'

  },

  files = {

    'file': open('document.pdf', 'rb')

  },

  data = {

    'data': json.dumps({

      'signatureType': 'cades',

      'cadesLevel': 'b-lt'

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

  CURLOPT_URL => 'https://api.nutrient.io/sign',

  CURLOPT_CUSTOMREQUEST => 'POST',

  CURLOPT_RETURNTRANSFER => true,

  CURLOPT_ENCODING => '',

  CURLOPT_POSTFIELDS => array(

    'data' => '{

      "signatureType": "cades",

      "cadesLevel": "b-lt"

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

POST https://api.nutrient.io/sign HTTP/1.1

Content-Type: multipart/form-data; boundary=--customboundary

Authorization: Bearer your_api_key_here


--customboundary

Content-Disposition: form-data; name="data"

Content-Type: application/json


{

  "signatureType": "cades",

  "cadesLevel": "b-lt"

}

--customboundary

Content-Disposition: form-data; name="file"; filename="document.pdf"

Content-Type: application/pdf


(file data)

--customboundary--


```

See all lines 

Using Postman? [Try this tool](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/overview) in our Postman collection to start using the API with a single click. [](/guides/dws-processor/getting-started/postman-collection)Read more → 

Your API key has automatically been inserted into the API example code. Run the sample code in your terminal to execute the API call. [See my API keys](https://dashboard.nutrient.io/processor-api/api%5Fkeys/). 

Start now

## Create an account to access your API key and start with 50 free credits per month

Start building with DWS Processor API in minutes — no payment information required.

[ SIGN UP ](https://dashboard.nutrient.io/sign%5Fup/) 

 Already have an account? [ Sign in → ](https://dashboard.nutrient.io/sign%5Fin/) 

---

### How does it work?

##### Obtain the document to be signed

---

##### Create signing fields

---

##### Collect signer approval

For example, collect ink signatures from all users who need to approve the document before the final digital signature step.

---

##### Authenticate

Ensure the correct user is signing the document

---

##### Digitally sign

Use Nutrient’s digital seal (certificate), which guarantees that a document wasn’t tampered with after signing. Tampering with the document in any way invalidates the signature.

---

Most common next steps

## Connect digital-signature evaluation to getting started, pricing, compliance, and the broader Processor platform

[ OPEN GETTING STARTED ](https://www.nutrient.io/guides/dws-processor/getting-started/) 

 After validating digital-signature workflows, continue to: 

[ PDF security If the workflow also needs password protection and permissions ](https://www.nutrient.io/api/pdf-security-api/) [ Getting started For API key setup ](https://www.nutrient.io/guides/dws-processor/getting-started/) [ Postman collection For the fastest first request ](https://www.nutrient.io/guides/dws-processor/getting-started/postman-collection/) [ Processor API pricing For credits ](https://www.nutrient.io/api/pricing/processor-api/) [ Processor API overview For broader DWS evaluation of digital signature, certificate-based, compliance-ready PDF signing ](https://www.nutrient.io/api/processor-api/) 

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