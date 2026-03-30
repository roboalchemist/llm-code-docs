# Source: https://www.nutrient.io/api/table-extraction-api/

---
description: Extract tables from PDFs with Nutrient’s cloud API. Convert PDF tables into Excel, CSV, JSON, or XML for analytics, reporting, ETL, and document-processing workflows.
title: Table extraction API from PDF to Excel, CSV, JSON, and XML | Nutrient
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

# Table extraction API from PDF to Excel, CSV, JSON, and XML workflows

Use Nutrient DWS as a table extraction API from PDF to Excel, CSV, JSON, and XML. Extract tables from PDF documents when your workflow needs line items, statements, reports, and other tabular content as structured output instead of page images or manual rekeying.

[ START FREE ](https://www.nutrient.io/try/) [ PROCESSOR PRICING ](https://www.nutrient.io/api/pricing/processor-api/) 

EXTRACT FROM 

PDF 

 PDF 

EXTRACT TO 

Select output file type 

## Try it out

This example will convert your uploaded PDF file to an XLSX.

---

Try it out in three steps

1. Add a PDF file named `document.pdf` to your project folder.
2. Run the code from the same folder.
3. Open `result.xlsx` in your project folder to view the results.

* [ SHELL ](#panel-0002bi)
* [ SHELL (WINDOWS) ](#panel-0002bj)
* [ JAVA ](#panel-0002bk)
* [ C# ](#panel-0002bl)
* [ JAVASCRIPT ](#panel-0002bm)
* [ PYTHON ](#panel-0002bn)
* [ PHP ](#panel-0002bo)
* [ HTTP ](#panel-0002bp)

SHELL 

 SHELL  SHELL (WINDOWS)  JAVA  C#  JAVASCRIPT  PYTHON  PHP  HTTP 

```

curl -X POST https://api.nutrient.io/build \

  -H "Authorization: Bearer your_api_key_here" \

  -o result.xlsx \

  --fail \

  -F document=@document.pdf \

  -F instructions='{

      "parts": [

        {

          "file": "document"

        }

      ],

      "output": {

        "type": "xlsx"

      }

    }'


```

```

curl -X POST https://api.nutrient.io/build ^

  -H "Authorization: Bearer your_api_key_here" ^

  -o result.xlsx ^

  --fail ^

  -F document=@document.pdf ^

  -F instructions="{\"parts\": [{\"file\": \"document\"}], \"output\": {\"type\": \"xlsx\"}}"


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

            .put("type", "xlsx")

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

        FileSystems.getDefault().getPath("result.xlsx"),

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

            ["type"] = "xlsx"

          }

        }.ToString());


      request.AdvancedResponseWriter = (responseStream, response) =>

      {

        if (response.StatusCode == HttpStatusCode.OK)

        {

          using (responseStream)

          {

            using var outputFileWriter = File.OpenWrite("result.xlsx");

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

    type: "xlsx"

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


    response.data.pipe(fs.createWriteStream("result.xlsx"))

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

        'type': 'xlsx'

      }

    })

  },

  stream = True

)


if response.ok:

  with open('result.xlsx', 'wb') as fd:

    for chunk in response.iter_content(chunk_size=8096):

      fd.write(chunk)

else:

  print(response.text)

  exit()


```

```

<?php


$FileHandle = fopen('result.xlsx', 'w+');


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

        "type": "xlsx"

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

    "type": "xlsx"

  }

}

--customboundary

Content-Disposition: form-data; name="document"; filename="document.pdf"

Content-Type: application/pdf


(document data)

--customboundary--


```

See all lines 

Using Postman? [Check out our Postman collection](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/overview) and start using the API with a single click. [](/guides/dws-processor/getting-started/postman-collection)Read more → 

Your API key has automatically been inserted into the API example code. Run the sample code in your terminal to execute the API call. [See my API keys](https://dashboard.nutrient.io/processor-api/api%5Fkeys/). 

 Submit inquiry 

# PDF-to-XML API

A PDF-to-XML API is currently in development. To get an email when we launch this feature, or to learn more, please get in touch. Nutrient’s document understanding engine will analyze input PDF documents and output structured data as XML files. The API will be usable by PHP, Java, Python, Node, and more.

## Get in touch

To get an email when we launch this feature, or to learn more, please tell us about your project and we’ll be happy to get back to you.

FIRST NAME

Please enter your first name

LAST NAME

Please enter your last name

COMPANY

Please enter your company name

EMAIL

Please enter your email address

ABOUT YOUR PROJECT

By submitting this form, you agree to Nutrient’s[Privacy Policy](https://www.nutrient.io/legal/privacy/)and[Terms of Service](https://www.nutrient.io/legal/terms/).

GET IN TOUCH 

## Thank you!

Thanks for filling out the form and letting us know about your interest in our PDF-to-XML API.

## Try it out

This example will extract tables from a PDF and return them as a JSON file.

---

Try it out in three steps

1. Add a PDF named `document.pdf` to your project folder.
2. Run the code from the same folder.
3. Open `result.json` to see the output.

* [ SHELL ](#panel-0002bq)
* [ SHELL (WINDOWS) ](#panel-0002br)
* [ JAVA ](#panel-0002bs)
* [ C# ](#panel-0002bt)
* [ JAVASCRIPT ](#panel-0002bu)
* [ PYTHON ](#panel-0002bv)
* [ PHP ](#panel-0002bw)
* [ HTTP ](#panel-0002bx)

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

        "plainText": false,

        "structuredText": false,

        "keyValuePairs": false,

        "tables": true

      }

    }'


```

```

curl -X POST https://api.nutrient.io/build ^

  -H "Authorization: Bearer your_api_key_here" ^

  -o result.json ^

  --fail ^

  -F document=@document.pdf ^

  -F instructions="{\"parts\": [{\"file\": \"document\"}], \"output\": {\"type\": \"json-content\", \"plainText\": false, \"structuredText\": false, \"keyValuePairs\": false, \"tables\": true}}"


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

            .put("plainText", false)

            .put("structuredText", false)

            .put("keyValuePairs", false)

            .put("tables", true)

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

            ["plainText"] = false,

            ["structuredText"] = false,

            ["keyValuePairs"] = false,

            ["tables"] = true

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

    plainText: false,

    structuredText: false,

    keyValuePairs: false,

    tables: true

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

        'plainText': False,

        'structuredText': False,

        'keyValuePairs': False,

        'tables': True

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

        "plainText": false,

        "structuredText": false,

        "keyValuePairs": false,

        "tables": true

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

    "plainText": false,

    "structuredText": false,

    "keyValuePairs": false,

    "tables": true

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

Your API key has automatically been inserted into the API example code. Run the sample code in your terminal to execute the API call. [See my API keys](https://dashboard.nutrient.io/processor-api/api%5Fkeys/). 

 Submit inquiry 

# PDF-to-CSV API

A PDF-to-CSV API is currently in development. To get an email when we launch this feature, or to learn more, please get in touch. Nutrient’s document understanding engine will analyze input PDF documents and output structured data as CSV files. The API will be usable by PHP, Java, Python, Node, and more.

## Get in touch

To get an email when we launch this feature, or to learn more, please tell us about your project and we’ll be happy to get back to you.

FIRST NAME

Please enter your first name

LAST NAME

Please enter your last name

COMPANY

Please enter your company name

EMAIL

Please enter your email address

ABOUT YOUR PROJECT

By submitting this form, you agree to Nutrient’s[Privacy Policy](https://www.nutrient.io/legal/privacy/)and[Terms of Service](https://www.nutrient.io/legal/terms/).

GET IN TOUCH 

## Thank you!

Thanks for filling out the form and letting us know about your interest in our PDF to CSV API.

---

[ PDF-to-Excel Convert PDF documents to Microsoft Excel files containing structured data. TRY NOW ](https://www.nutrient.io/api/pdf-to-excel-api/) [  Request PDF-to-XML API Convert PDF documents to XML files with our table extraction API. SEND INQUIRY ](https://www.nutrient.io/api/pdf-to-xml-api/) [ PDF-to-JSON API Use our PDF-to-JSON conversion API to generate structured JSON files from PDF documents. TRY NOW ](https://www.nutrient.io/api/pdf-to-json-api/) [  Request PDF-to-CSV API Use our PDF-to-CSV conversion API to output table data as comma-separated values. SEND INQUIRY ](https://www.nutrient.io/api/pdf-to-csv-api/) 

---

Most common next paths

## Use exact output pages when the request is more specific than table extraction

[ OPEN PDF-TO-EXCEL API ](https://www.nutrient.io/api/pdf-to-excel-api/) 

 Use the following: 

[ PDF-to-Excel When the query already implies Excel as the preferred structured output ](https://www.nutrient.io/api/pdf-to-excel-api/) [ PDF-to-JSON When the query already implies JSON as the preferred structured output or downstream system ](https://www.nutrient.io/api/pdf-to-json-api/) [ Key-value pair extraction If the workflow needs invoice fields or labeled data rather than tabular rows ](https://www.nutrient.io/api/key-value-pair-extraction-api/) 

 For broader evaluation, continue to: 

[ Data extraction API To connect table extraction to structured output workflows ](https://www.nutrient.io/api/data-extraction-api/) [ Getting started For API key setup ](https://www.nutrient.io/guides/dws-processor/getting-started/) [ Processor API pricing For credits ](https://www.nutrient.io/api/pricing/processor-api/) [ Processor API overview For broader DWS evaluation ](https://www.nutrient.io/api/processor-api/) 

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