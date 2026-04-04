# Source: https://docs.pentaho.com/rest-api/carte-apis-carte-server.md

# Carte APIs   Carte Server

Provides web service calls related to servers, such as allocating sockets and ports, getting the list of slaves and registering them, and displaying the initial Carte page.

## Allocate server socket

> Allocates port to use by client.\
> Allows any client to ask for a port number to use. This is necessary several slaves can be run on the same host.\
> The method ensures the port number is unique for host name provided and makes sure the slaves are using\
> valid port numbers. Data communication across a cluster of Carte servers happens through TCP/IP sockets.\
> Slave transformations sometimes open (or listen to) tens to hundreds of sockets. When you want to allocate\
> the port numbers for data communication between slave transformation in a kettle clustering run, you need\
> unique combinations of all the parameters below.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET /kettle/allocateSocket/?xml=Y\&rangeStart=100\&host=locahost\&id=clust\&trans=my\_trans\&sourceSlave=slave\_1\&sourceStep=200\&sourceCopy=1\&targetSlave=slave\_2\&targetStep=50\&targetCopy=1\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Carte APIs - Carte Server","description":"Provides web service calls related to servers, such as allocating sockets and ports, getting the list of slaves and registering them, and displaying the initial Carte page."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"ErrorResponse":{"type":"object","description":"Error response format","properties":{"result":{"type":"string","enum":["ERROR"],"description":"Always ERROR for error responses"},"message":{"type":"string","description":"Error message describing what went wrong"},"exception":{"type":"string","description":"Exception details if available"}},"xml":{"name":"webresult"}}}},"paths":{"/kettle/allocateSocket":{"get":{"tags":["Carte APIs - Carte Server"],"summary":"Allocate server socket","description":"Allocates port to use by client.\nAllows any client to ask for a port number to use. This is necessary several slaves can be run on the same host.\nThe method ensures the port number is unique for host name provided and makes sure the slaves are using\nvalid port numbers. Data communication across a cluster of Carte servers happens through TCP/IP sockets.\nSlave transformations sometimes open (or listen to) tens to hundreds of sockets. When you want to allocate\nthe port numbers for data communication between slave transformation in a kettle clustering run, you need\nunique combinations of all the parameters below.\n\n**Example Request:**\n```\nGET /kettle/allocateSocket/?xml=Y&rangeStart=100&host=locahost&id=clust&trans=my_trans&sourceSlave=slave_1&sourceStep=200&sourceCopy=1&targetSlave=slave_2&targetStep=50&targetCopy=1\n```\n","parameters":[{"name":"xml","in":"query","description":"Return XML format when Y, HTML otherwise","required":false,"schema":{"type":"string","enum":["Y","N"],"default":"N"}},{"name":"rangeStart","in":"query","description":"Port number to start looking from","required":false,"schema":{"type":"integer"}},{"name":"host","in":"query","description":"Port's host","required":false,"schema":{"type":"string"}},{"name":"id","in":"query","description":"Carte container id","required":false,"schema":{"type":"string"}},{"name":"trans","in":"query","description":"Running transformation id","required":false,"schema":{"type":"string"}},{"name":"sourceSlave","in":"query","description":"Name of the source slave server","required":false,"schema":{"type":"string"}},{"name":"sourceStep","in":"query","description":"Port number step used on source slave server","required":false,"schema":{"type":"integer"}},{"name":"sourceCopy","in":"query","description":"Number of copies of the step on source server","required":false,"schema":{"type":"integer"}},{"name":"targetSlave","in":"query","description":"Name of the target slave server","required":false,"schema":{"type":"string"}},{"name":"targetStep","in":"query","description":"Port number step used on target slave server","required":false,"schema":{"type":"integer"}},{"name":"targetCopy","in":"query","description":"Number of copies of the step on target server","required":false,"schema":{"type":"integer"}}],"responses":{"200":{"description":"Socket allocated successfully","content":{"text/xml":{"schema":{"type":"string","description":"Socket allocation result"}}}},"500":{"description":"Internal server error","content":{"text/xml":{"schema":{"$ref":"#/components/schemas/ErrorResponse"}}}}}}}}}
````

## List allocated server sockets

> Gets list of ports for specified host.\
> Method is used for listing all or just open ports for specified host. Response contains port number,\
> which transformation it is (was) used for, current status of the port and last date time used.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET /kettle/listSocket/?host=127.0.0.1\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Carte APIs - Carte Server","description":"Provides web service calls related to servers, such as allocating sockets and ports, getting the list of slaves and registering them, and displaying the initial Carte page."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"ErrorResponse":{"type":"object","description":"Error response format","properties":{"result":{"type":"string","enum":["ERROR"],"description":"Always ERROR for error responses"},"message":{"type":"string","description":"Error message describing what went wrong"},"exception":{"type":"string","description":"Exception details if available"}},"xml":{"name":"webresult"}}}},"paths":{"/kettle/listSocket":{"get":{"tags":["Carte APIs - Carte Server"],"summary":"List allocated server sockets","description":"Gets list of ports for specified host.\nMethod is used for listing all or just open ports for specified host. Response contains port number,\nwhich transformation it is (was) used for, current status of the port and last date time used.\n\n**Example Request:**\n```\nGET /kettle/listSocket/?host=127.0.0.1\n```\n","parameters":[{"name":"host","in":"query","description":"Host to get ports for","required":true,"schema":{"type":"string"}},{"name":"onlyOpen","in":"query","description":"Boolean flag that indicates whether all or only open ports should be returned. Set it to Y to get the list of only currently open ports.","required":false,"schema":{"type":"string","enum":["Y","N"]}}],"responses":{"200":{"description":"Socket list retrieved successfully","content":{"text/html":{"schema":{"type":"string","description":"HTML document listing the ports requested"}}}},"500":{"description":"Internal server error","content":{"text/xml":{"schema":{"$ref":"#/components/schemas/ErrorResponse"}}}}}}}}}
````

## Get next sequence value

> Increments specified pre-configured sequence.\
> Method is used for reserving a number of IDs and incrementing a sequence pre-configured in Carte server configuration\
> by specified amount. If no increment value provided 10000 is used by default.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET /kettle/nextSequence?name=test\_seq\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Carte APIs - Carte Server","description":"Provides web service calls related to servers, such as allocating sockets and ports, getting the list of slaves and registering them, and displaying the initial Carte page."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"ErrorResponse":{"type":"object","description":"Error response format","properties":{"result":{"type":"string","enum":["ERROR"],"description":"Always ERROR for error responses"},"message":{"type":"string","description":"Error message describing what went wrong"},"exception":{"type":"string","description":"Exception details if available"}},"xml":{"name":"webresult"}}}},"paths":{"/kettle/nextSequence":{"get":{"tags":["Carte APIs - Carte Server"],"summary":"Get next sequence value","description":"Increments specified pre-configured sequence.\nMethod is used for reserving a number of IDs and incrementing a sequence pre-configured in Carte server configuration\nby specified amount. If no increment value provided 10000 is used by default.\n\n**Example Request:**\n```\nGET /kettle/nextSequence?name=test_seq\n```\n","parameters":[{"name":"name","in":"query","description":"Name of the sequence specified in Carte configuration file","required":true,"schema":{"type":"string"}},{"name":"increment","in":"query","description":"Parameter used for incrementing sequence. If no parameter specified 10000 is used by default.","required":false,"schema":{"type":"integer","default":10000}}],"responses":{"200":{"description":"Next sequence value retrieved","content":{"text/xml":{"schema":{"type":"string","description":"XML containing sequence value and the increment value used"}}}},"500":{"description":"Internal server error","content":{"text/xml":{"schema":{"$ref":"#/components/schemas/ErrorResponse"}}}}}}}}}
````

## Register slave server

> Registers slave server in the master.\
> The method is used to add or update information of slave server.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST /kettle/registerSlave/\
> \`\`\`\
> Request body should contain xml containing slave server description.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Carte APIs - Carte Server","description":"Provides web service calls related to servers, such as allocating sockets and ports, getting the list of slaves and registering them, and displaying the initial Carte page."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"WebResult":{"type":"object","description":"Standard response format for most Carte operations","properties":{"result":{"type":"string","enum":["OK","ERROR"],"description":"Result status of the operation"},"message":{"type":"string","description":"Human readable message describing the result"},"id":{"type":"string","description":"Unique identifier for the created/modified resource"}},"xml":{"name":"webresult"}},"ErrorResponse":{"type":"object","description":"Error response format","properties":{"result":{"type":"string","enum":["ERROR"],"description":"Always ERROR for error responses"},"message":{"type":"string","description":"Error message describing what went wrong"},"exception":{"type":"string","description":"Exception details if available"}},"xml":{"name":"webresult"}}}},"paths":{"/kettle/registerSlave":{"post":{"tags":["Carte APIs - Carte Server"],"summary":"Register slave server","description":"Registers slave server in the master.\nThe method is used to add or update information of slave server.\n\n**Example Request:**\n```\nPOST /kettle/registerSlave/\n```\nRequest body should contain xml containing slave server description.\n","requestBody":{"required":true,"description":"XML containing slave server description","content":{"application/xml":{"schema":{"type":"string","description":"SlaveServerDetection XML"}}}},"responses":{"200":{"description":"Slave server registered successfully","content":{"text/xml":{"schema":{"$ref":"#/components/schemas/WebResult"}}}},"500":{"description":"Internal server error","content":{"text/xml":{"schema":{"$ref":"#/components/schemas/ErrorResponse"}}}}}}}}}
````

## Get registered slave servers

> Gets list of slave servers.\
> Retrieves list of slave servers which are known to specific server.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET /kettle/getSlaves\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Carte APIs - Carte Server","description":"Provides web service calls related to servers, such as allocating sockets and ports, getting the list of slaves and registering them, and displaying the initial Carte page."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"ErrorResponse":{"type":"object","description":"Error response format","properties":{"result":{"type":"string","enum":["ERROR"],"description":"Always ERROR for error responses"},"message":{"type":"string","description":"Error message describing what went wrong"},"exception":{"type":"string","description":"Exception details if available"}},"xml":{"name":"webresult"}}}},"paths":{"/kettle/getSlaves":{"get":{"tags":["Carte APIs - Carte Server"],"summary":"Get registered slave servers","description":"Gets list of slave servers.\nRetrieves list of slave servers which are known to specific server.\n\n**Example Request:**\n```\nGET /kettle/getSlaves\n```\n","parameters":[{"name":"xml","in":"query","description":"Return XML format when Y, HTML otherwise","required":false,"schema":{"type":"string","enum":["Y","N"],"default":"N"}}],"responses":{"200":{"description":"Slave servers list retrieved successfully","content":{"text/xml":{"schema":{"type":"string","description":"List of registered slave servers"}}}},"500":{"description":"Internal server error","content":{"text/xml":{"schema":{"$ref":"#/components/schemas/ErrorResponse"}}}}}}}}}
````

## Get server status

> Retrieve server status. The status contains information about the server itself (OS, memory, etc)\
> and information about jobs and transformations present on the server.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET /kettle/status/?xml=Y\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Carte APIs - Carte Server","description":"Provides web service calls related to servers, such as allocating sockets and ports, getting the list of slaves and registering them, and displaying the initial Carte page."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"ErrorResponse":{"type":"object","description":"Error response format","properties":{"result":{"type":"string","enum":["ERROR"],"description":"Always ERROR for error responses"},"message":{"type":"string","description":"Error message describing what went wrong"},"exception":{"type":"string","description":"Exception details if available"}},"xml":{"name":"webresult"}}}},"paths":{"/kettle/status":{"get":{"tags":["Carte APIs - Carte Server"],"summary":"Get server status","description":"Retrieve server status. The status contains information about the server itself (OS, memory, etc)\nand information about jobs and transformations present on the server.\n\n**Example Request:**\n```\nGET /kettle/status/?xml=Y\n```\n","parameters":[{"name":"xml","in":"query","description":"Return XML format when Y, HTML otherwise","required":false,"schema":{"type":"string","enum":["Y","N"],"default":"N"}}],"responses":{"200":{"description":"Server status retrieved successfully","content":{"text/xml":{"schema":{"type":"string","description":"Server status in XML format including memory, CPU, OS info and running transformations/jobs"}}}},"500":{"description":"Internal server error","content":{"text/xml":{"schema":{"$ref":"#/components/schemas/ErrorResponse"}}}}}}}}}
````

## Shutdown Carte server

> Stops the Carte server. This method must be set up initially through the CLI and is used for stopping the Carte server.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET <http://localhost:8080/pentaho/kettle/stopCarte\\>
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Carte APIs - Carte Server","description":"Provides web service calls related to servers, such as allocating sockets and ports, getting the list of slaves and registering them, and displaying the initial Carte page."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"ErrorResponse":{"type":"object","description":"Error response format","properties":{"result":{"type":"string","enum":["ERROR"],"description":"Always ERROR for error responses"},"message":{"type":"string","description":"Error message describing what went wrong"},"exception":{"type":"string","description":"Exception details if available"}},"xml":{"name":"webresult"}}}},"paths":{"/kettle/stopCarte":{"get":{"tags":["Carte APIs - Carte Server"],"summary":"Shutdown Carte server","description":"Stops the Carte server. This method must be set up initially through the CLI and is used for stopping the Carte server.\n\n**Example Request:**\n```\nGET http://localhost:8080/pentaho/kettle/stopCarte\n```\n","parameters":[{"name":"xml","in":"query","description":"Return XML format when Y, HTML otherwise","required":false,"schema":{"type":"string","enum":["Y","N"],"default":"N"}}],"responses":{"200":{"description":"Request was processed","content":{"text/xml":{"schema":{"type":"object","properties":{"request_accepted":{"type":"boolean","description":"Whether the shutdown request was accepted"}},"xml":{"name":"request_accepted"}}},"text/html":{"schema":{"type":"string","description":"HTML page confirming shutdown request"}}}},"500":{"description":"Internal server error occurs during request processing","content":{"text/xml":{"schema":{"$ref":"#/components/schemas/ErrorResponse"}}}}}}}}}
````
