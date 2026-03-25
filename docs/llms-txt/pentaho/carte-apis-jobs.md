# Source: https://docs.pentaho.com/rest-api/carte-apis-jobs.md

# Carte APIs   Jobs

Provides information on web service calls to create, run, and delete jobs. Calls for getting images, statuses and for starting and stopping jobs are also included.

## Upload and execute job

> \*\*DEPRECATED\*\*: This endpoint is deprecated and may be removed in future versions.\
> \
> Uploads and executes job configuration XML file.\
> Uploads xml file containing job and job\_execution\_configuration\
> (wrapped in job\_configuration tag) to be executed and executes it. Method relies\
> on the input parameter to determine if xml or html reply should be produced. The job\_configuration xml is\
> transferred within request body. Job name of the executed job will be returned in the Response object\
> or message describing error occurred. To determine if the call successful or not you should rely\
> on result parameter in response.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST /kettle/addJob/?xml=Y\
> \`\`\`\
> Request body should contain xml containing job\_configuration (job and\
> job\_execution\_configuration wrapped in job\_configuration tag).<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Carte APIs - Jobs","description":"Provides information on web service calls to create, run, and delete jobs. Calls for getting images, statuses and for starting and stopping jobs are also included."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"WebResult":{"type":"object","description":"Standard response format for most Carte operations","properties":{"result":{"type":"string","enum":["OK","ERROR"],"description":"Result status of the operation"},"message":{"type":"string","description":"Human readable message describing the result"},"id":{"type":"string","description":"Unique identifier for the created/modified resource"}},"xml":{"name":"webresult"}},"ErrorResponse":{"type":"object","description":"Error response format","properties":{"result":{"type":"string","enum":["ERROR"],"description":"Always ERROR for error responses"},"message":{"type":"string","description":"Error message describing what went wrong"},"exception":{"type":"string","description":"Exception details if available"}},"xml":{"name":"webresult"}}}},"paths":{"/kettle/addJob":{"post":{"tags":["Carte APIs - Jobs"],"summary":"Upload and execute job","deprecated":true,"description":"**DEPRECATED**: This endpoint is deprecated and may be removed in future versions.\n\nUploads and executes job configuration XML file.\nUploads xml file containing job and job_execution_configuration\n(wrapped in job_configuration tag) to be executed and executes it. Method relies\non the input parameter to determine if xml or html reply should be produced. The job_configuration xml is\ntransferred within request body. Job name of the executed job will be returned in the Response object\nor message describing error occurred. To determine if the call successful or not you should rely\non result parameter in response.\n\n**Example Request:**\n```\nPOST /kettle/addJob/?xml=Y\n```\nRequest body should contain xml containing job_configuration (job and\njob_execution_configuration wrapped in job_configuration tag).\n","parameters":[{"name":"xml","in":"query","description":"Boolean flag set to either Y or N describing if xml or html reply should be produced.","required":false,"schema":{"type":"string","enum":["Y","N"],"default":"N"}}],"requestBody":{"required":true,"description":"XML containing job_configuration (job and job_execution_configuration wrapped in job_configuration tag)","content":{"application/xml":{"schema":{"type":"string","description":"Job configuration XML"}}}},"responses":{"200":{"description":"Request was processed and XML response is returned","content":{"text/xml":{"schema":{"$ref":"#/components/schemas/WebResult"}}}},"500":{"description":"Internal server error occurs during request processing","content":{"text/xml":{"schema":{"$ref":"#/components/schemas/ErrorResponse"}}}}}}}}}
````

## Generate job image

> Generates PNG image of the specified job currently present on Carte server.\
> Job name and Carte job ID (optional) are used for specifying which\
> job to get information for. Response is a binary of the PNG image.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET /kettle/jobImage?name=dummy-job\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Carte APIs - Jobs","description":"Provides information on web service calls to create, run, and delete jobs. Calls for getting images, statuses and for starting and stopping jobs are also included."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"ErrorResponse":{"type":"object","description":"Error response format","properties":{"result":{"type":"string","enum":["ERROR"],"description":"Always ERROR for error responses"},"message":{"type":"string","description":"Error message describing what went wrong"},"exception":{"type":"string","description":"Exception details if available"}},"xml":{"name":"webresult"}}}},"paths":{"/kettle/jobImage":{"get":{"tags":["Carte APIs - Jobs"],"summary":"Generate job image","description":"Generates PNG image of the specified job currently present on Carte server.\nJob name and Carte job ID (optional) are used for specifying which\njob to get information for. Response is a binary of the PNG image.\n\n**Example Request:**\n```\nGET /kettle/jobImage?name=dummy-job\n```\n","parameters":[{"name":"name","in":"query","description":"Name of the job to be used for image generation.","required":true,"schema":{"type":"string"}},{"name":"id","in":"query","description":"Carte id of the job to be used for image generation.","required":false,"schema":{"type":"string"}}],"responses":{"200":{"description":"Request was processed","content":{"image/png":{"schema":{"type":"string","format":"binary","description":"Binary PNG image"}}}},"500":{"description":"Internal server error occurs during request processing","content":{"text/xml":{"schema":{"$ref":"#/components/schemas/ErrorResponse"}}}}}}}}}
````

## Get job status

> Retrieves status of the specified job. Status is returned as HTML or XML output\
> depending on the input parameters. Status contains information about last execution of the job.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET /kettle/jobStatus/?name=dummy-job\&xml=Y\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Carte APIs - Jobs","description":"Provides information on web service calls to create, run, and delete jobs. Calls for getting images, statuses and for starting and stopping jobs are also included."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"ErrorResponse":{"type":"object","description":"Error response format","properties":{"result":{"type":"string","enum":["ERROR"],"description":"Always ERROR for error responses"},"message":{"type":"string","description":"Error message describing what went wrong"},"exception":{"type":"string","description":"Exception details if available"}},"xml":{"name":"webresult"}}}},"paths":{"/kettle/jobStatus":{"get":{"tags":["Carte APIs - Jobs"],"summary":"Get job status","description":"Retrieves status of the specified job. Status is returned as HTML or XML output\ndepending on the input parameters. Status contains information about last execution of the job.\n\n**Example Request:**\n```\nGET /kettle/jobStatus/?name=dummy-job&xml=Y\n```\n","parameters":[{"name":"name","in":"query","description":"Name of the job to be used for status generation.","required":true,"schema":{"type":"string"}},{"name":"xml","in":"query","description":"Boolean flag which defines output format Y forces XML output to be generated. HTML is returned otherwise.","required":false,"schema":{"type":"string","enum":["Y","N"],"default":"N"}},{"name":"id","in":"query","description":"Carte id of the job to be used for status generation.","required":false,"schema":{"type":"string"}},{"name":"from","in":"query","description":"Start line number of the execution log to be included into response.","required":false,"schema":{"type":"integer"}}],"responses":{"200":{"description":"Request was processed","content":{"text/xml":{"schema":{"type":"string","description":"XML response containing job status details"}},"text/html":{"schema":{"type":"string","description":"HTML response containing job status details"}}}},"500":{"description":"Internal server error occurs during request processing","content":{"text/xml":{"schema":{"$ref":"#/components/schemas/ErrorResponse"}}}}}}}}}
````

## Execute job from repository

> Execute job from enterprise repository. Repository should be configured in Carte xml file.\
> Response contains ERROR result if error happened during job execution.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET /kettle/runJob?job=home%2Fadmin%2Fdummy-job\&level=Debug\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Carte APIs - Jobs","description":"Provides information on web service calls to create, run, and delete jobs. Calls for getting images, statuses and for starting and stopping jobs are also included."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"WebResult":{"type":"object","description":"Standard response format for most Carte operations","properties":{"result":{"type":"string","enum":["OK","ERROR"],"description":"Result status of the operation"},"message":{"type":"string","description":"Human readable message describing the result"},"id":{"type":"string","description":"Unique identifier for the created/modified resource"}},"xml":{"name":"webresult"}},"ErrorResponse":{"type":"object","description":"Error response format","properties":{"result":{"type":"string","enum":["ERROR"],"description":"Always ERROR for error responses"},"message":{"type":"string","description":"Error message describing what went wrong"},"exception":{"type":"string","description":"Exception details if available"}},"xml":{"name":"webresult"}}}},"paths":{"/kettle/runJob":{"get":{"tags":["Carte APIs - Jobs"],"summary":"Execute job from repository","description":"Execute job from enterprise repository. Repository should be configured in Carte xml file.\nResponse contains ERROR result if error happened during job execution.\n\n**Example Request:**\n```\nGET /kettle/runJob?job=home%2Fadmin%2Fdummy-job&level=Debug\n```\n","parameters":[{"name":"job","in":"query","description":"Full path to the job in repository.","required":true,"schema":{"type":"string"}},{"name":"level","in":"query","description":"Logging level to be used for job execution (i.e. Debug).","required":true,"schema":{"type":"string"}}],"responses":{"200":{"description":"Request was processed","content":{"text/xml":{"schema":{"$ref":"#/components/schemas/WebResult"}},"text/html":{"schema":{"type":"string","description":"HTML response containing operation result"}}}},"500":{"description":"Internal server error occurs during request processing","content":{"text/xml":{"schema":{"$ref":"#/components/schemas/ErrorResponse"}}}}}}}}}
````
