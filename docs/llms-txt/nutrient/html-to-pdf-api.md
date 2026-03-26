# Source: https://www.nutrient.io/api/html-to-pdf-api/

---
description: Accurate, reliable HTML to PDF API. Create PDFs from a template, invoice, or report. Plug &#38; play integration to easily deploy HTML to PDF generation in your app.
title: HTML to PDF API: Create PDFs from HTML Template | Nutrient
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

# HTML to PDF API

Convert HTML files into pixel-perfect PDF documents with ease. Ideal for invoices, reports, dynamic content, and web-to-document workflows.

[ TRY FOR FREE ](https://dashboard.nutrient.io/sign%5Fin/) 

##### Accurate, pixel-perfect rendering

Preserve layout, styles, fonts, and responsive design to ensure your HTML content looks exactly as intended in PDF format.

##### Automate with Zapier

Automatically convert HTML files in Google Drive to PDFs using our Zapier integration. It’s the fastest way to turn web content into documents without writing code.

[ CONNECT WITH ZAPIER ](https://zapier.com/apps/google-drive/integrations/google-drive/255620380/convert-new-html-files-in-google-drive-to-pdfs-with-nutrient-document-web-services-api) 

##### Simple and transparent pricing

Select a package that suits your needs according to the number of credits you wish to spend. Each API tool and action has a specific credit cost.

---

## Try it out

This example will create a PDF from the supplied `index.html` file and render it on an A4-sized page. For detailed information on how to structure your HTML files, along with all the available customization options, visit our guides.

[ Guides ](https://www.nutrient.io/guides/dws-processor/developer-guides/pdf-generation/) 

---

Try it out in three steps

1. Add an HTML file named `index.html` to your project folder.
2. Run the code from the same folder.
3. Open `result.pdf` to see the output.

 Advanced API 

* [ SHELL ](#panel-0000vk)
* [ SHELL (WINDOWS) ](#panel-0000vl)
* [ JAVA ](#panel-0000vm)
* [ C# ](#panel-0000vn)
* [ JAVASCRIPT ](#panel-0000vo)
* [ PYTHON ](#panel-0000vp)
* [ PHP ](#panel-0000vq)
* [ HTTP ](#panel-0000vr)

SHELL 

 SHELL  SHELL (WINDOWS)  JAVA  C#  JAVASCRIPT  PYTHON  PHP  HTTP 

```

curl -X POST https://api.nutrient.io/processor/generate_pdf \

  -H "Authorization: Bearer your_api_key_here" \

  -o result.pdf \

  --fail \

  -F html=@index.html


```

```

curl -X POST https://api.nutrient.io/processor/generate_pdf ^

  -H "Authorization: Bearer your_api_key_here" ^

  -o result.pdf ^

  --fail ^

  -F html=@index.html


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

      var client = new RestClient("https://api.nutrient.io/processor/generate_pdf");


      var request = new RestRequest(Method.POST)

        .AddHeader("Authorization", "Bearer your_api_key_here")

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

// This code requires Node.js. Do not run this code directly in a web browser.


const axios = require('axios')

const FormData = require('form-data')

const fs = require('fs')


const formData = new FormData()

formData.append('html', fs.createReadStream('index.html'))


;(async () => {

  try {

    const response = await axios.post('https://api.nutrient.io/processor/generate_pdf', formData, {

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

  'https://api.nutrient.io/processor/generate_pdf',

  headers = {

    'Authorization': 'Bearer your_api_key_here'

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

    'Authorization: Bearer your_api_key_here'

  ),

  CURLOPT_FILE => $FileHandle,

));


$response = curl_exec($curl);


curl_close($curl);


fclose($FileHandle);


```

```

POST https://api.nutrient.io/processor/generate_pdf HTTP/1.1

Content-Type: multipart/form-data; boundary=--customboundary

Authorization: Bearer your_api_key_here


--customboundary

Content-Disposition: form-data; name="html"; filename="index.html"

Content-Type: text/html


(html data)

--customboundary--


```

See all lines 

Using Postman? [Check out our other Postman collection](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/overview) and start using the API with a single click. [](/guides/dws-processor/getting-started/postman-collection)Read more → 

* [ SHELL ](#panel-0000vs)
* [ SHELL (WINDOWS) ](#panel-0000vt)
* [ JAVA ](#panel-0000vu)
* [ C# ](#panel-0000vv)
* [ JAVASCRIPT ](#panel-0000vw)
* [ PYTHON ](#panel-0000vx)
* [ PHP ](#panel-0000vy)
* [ HTTP ](#panel-0000vz)

SHELL 

 SHELL  SHELL (WINDOWS)  JAVA  C#  JAVASCRIPT  PYTHON  PHP  HTTP 

```

curl -X POST https://api.nutrient.io/build \

  -H "Authorization: Bearer your_api_key_here" \

  -o result.pdf \

  --fail \

  -F index.html=@index.html \

  -F instructions='{

      "parts": [

        {

          "html": "index.html"

        }

      ]

    }'


```

```

curl -X POST https://api.nutrient.io/build ^

  -H "Authorization: Bearer your_api_key_here" ^

  -o result.pdf ^

  --fail ^

  -F index.html=@index.html ^

  -F instructions="{\"parts\": [{\"html\": \"index.html\"}]}"


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

        "index.html",

        "index.html",

        RequestBody.create(

          MediaType.parse("text/html"),

          new File("index.html")

        )

      )

      .addFormDataPart(

        "instructions",

        new JSONObject()

          .put("parts", new JSONArray()

            .put(new JSONObject()

              .put("html", "index.html")

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

        .AddFile("index.html", "index.html")

        .AddParameter("instructions", new JsonObject

        {

          ["parts"] = new JsonArray

          {

            new JsonObject

            {

              ["html"] = "index.html"

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

      html: "index.html"

    }

  ]

}))

formData.append('index.html', fs.createReadStream('index.html'))


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

    'index.html': open('index.html', 'rb')

  },

  data = {

    'instructions': json.dumps({

      'parts': [

        {

          'html': 'index.html'

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

          "html": "index.html"

        }

      ]

    }',

    'index.html' => new CURLFILE('index.html')

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

      "html": "index.html"

    }

  ]

}

--customboundary

Content-Disposition: form-data; name="index.html"; filename="index.html"

Content-Type: text/html


(index.html data)

--customboundary--


```

See all lines 

Using Postman? [Check out our other Postman collection](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/overview) and start using the API with a single click. [](/guides/dws-processor/getting-started/postman-collection)Read more → 

Your API key has automatically been inserted into the API example code. Run the sample code in your terminal to execute the API call. [See my API keys](https://dashboard.nutrient.io/processor-api/api%5Fkeys/). 

Start now

## Create an account to access your API key and start with 50 free credits per month

Start building with DWS Processor API in minutes — no payment information required.

[ SIGN UP ](https://dashboard.nutrient.io/sign%5Fup/) 

 Already have an account? [ Sign in → ](https://dashboard.nutrient.io/sign%5Fin/) 

---

## API comparison

 BASIC 

### Convert to PDF API

Straightforward API for converting to PDF. Perfect for most use cases.

---

FEATURES

* Simple request format
* Minimal configuration required
* Purpose-built for specific tasks

 ADVANCED 

### Build API

Maximum flexibility and advanced features for complex workflows.

---

FEATURES

* Multipart document support
* Advanced actions and transformations
* Workflow orchestration

---

## Getting started

The following section will walk you through how to go from a simple HTML file to a fully featured invoice, making use of all the functionality the PDF Generator API provides.

[ GUIDES ](https://www.nutrient.io/guides/dws-processor/tools-and-api/pdf-generator-api/) 

[ ![](https://www.nutrient.io/_astro/gs-basic.3lJ-a5Te_1dFyhJ.png)  1 — Basics The basics of PDF Generation ](https://www.nutrient.io/guides/dws-processor/tools-and-api/pdf-generator-api/#basics-of-pdf-generation)[ ![](https://www.nutrient.io/_astro/gs-generate-style.BI3SZ8Hp_1ENSEM.png)  2 — Styling Applying Basic Styling ](https://www.nutrient.io/guides/dws-processor/tools-and-api/pdf-generator-api/#applying-basic-styling)[ ![](https://www.nutrient.io/_astro/gs-generate-assets.CU66plZP_1gzyLs.png)  3 — Assets Introducing Assets ](https://www.nutrient.io/guides/dws-processor/tools-and-api/pdf-generator-api/#introducing-assets)[ ![](https://www.nutrient.io/_astro/gs-generate-invoice.q_G34eN8_Z1PWxJg.png)  4 — creation Creating an Invoice ](https://www.nutrient.io/guides/dws-processor/tools-and-api/pdf-generator-api/#creating-an-invoice) 

---

## Download sample documents

Try generating PDFs with different HTML templates. Download our various sample documents and customize them to your needs.

![Invoice template](https://www.nutrient.io/_astro/cine-co-invoice.DNz4Xtp3_Z1FkfMp.png) 

[ INVOICE ](https://www.nutrient.io/downloads/cloud-expamples/cine-co-invoice.zip) 

![Form template](https://www.nutrient.io/_astro/air-co-application-form.nikK3GIM_QT29l.png) 

[ FORM ](https://www.nutrient.io/downloads/cloud-expamples/air-co-form.zip) 

![Purchase order template](https://www.nutrient.io/_astro/capital-co-purchase-requisition.BeXtkWJ5_ZianXl.png) 

[ PURCHASE REQUISITION ](https://www.nutrient.io/downloads/cloud-expamples/capital-co-purchase-requisition.zip) 

![Contract template](https://www.nutrient.io/_astro/capital-co-business-contract.CBodln8i_9BWdA.png) 

[ CONTRACT ](https://www.nutrient.io/downloads/cloud-expamples/capital-co-contract.zip) 

![Report template](https://www.nutrient.io/_astro/capital-co-annual-report.DxXuPrS5_2kRtSa.png) 

[ REPORT ](https://www.nutrient.io/downloads/cloud-expamples/capital-co-annual-report.zip) 

![Business letter template](https://www.nutrient.io/_astro/capital-co-business-letter.DeLDeMvl_tfezE.png) 

[ BUSINESS LETTER ](https://www.nutrient.io/downloads/cloud-expamples/capital-co-letter.zip) 

![Expense sheet template](https://www.nutrient.io/_astro/capital-co-expense-sheet.D19SdpDt_VHeLV.png) 

[ EXPENSE SHEET ](https://www.nutrient.io/downloads/cloud-expamples/capital-co-expense-sheet.zip) 

![Presentation template](https://www.nutrient.io/_astro/books-co-the-secretl-life-of-rocks.CHq5uOa__Z2egcuc.jpg) 

[ PRESENTATION ](https://www.nutrient.io/downloads/cloud-expamples/presentation-books-co.zip) 

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