# Source: https://docs.pentaho.com/rest-api/scheduling-apis-scheduler-resource.md

# Scheduling APIs   Scheduler Resource

The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler.

## Add blockout for scheduled jobs

> Creates a new blockout for scheduled jobs.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST pentaho/api/scheduler/blockout/add\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/blockout/add>" \\\
> &#x20; -H "Content-Type: application/xml" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -d '\<jobScheduleRequest>\
> &#x20;   \<jobName>DAILY-1820438815:admin:7740000\</jobName>\
> &#x20;   \<complexJobTrigger>\
> &#x20;     \<uiPassParam>DAILY\</uiPassParam>\
> &#x20;     \<daysOfWeek>1\</daysOfWeek>\
> &#x20;     \<daysOfWeek>2\</daysOfWeek>\
> &#x20;     \<daysOfWeek>3\</daysOfWeek>\
> &#x20;     \<daysOfWeek>4\</daysOfWeek>\
> &#x20;     \<daysOfWeek>5\</daysOfWeek>\
> &#x20;     \<startTime>2014-08-19T10:51:00.000-04:00\</startTime>\
> &#x20;     \<endTime />\
> &#x20;   \</complexJobTrigger>\
> &#x20;   \<inputFile>\</inputFile>\
> &#x20;   \<outputFile>\</outputFile>\
> &#x20;   \<duration>7740000\</duration>\
> &#x20;   \<timeZone>America/New\_York\</timeZone>\
> &#x20; \</jobScheduleRequest>'\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"JobScheduleRequest":{"type":"object","description":"Request object for scheduling jobs and blockouts","properties":{"jobName":{"type":"string","description":"Name of the job"},"jobId":{"type":"string","description":"ID of the job (for updates)"},"simpleJobTrigger":{"type":"object","description":"Simple job trigger configuration","properties":{"uiPassParam":{"type":"string","description":"UI parameter for trigger type"},"repeatInterval":{"type":"integer","description":"Repeat interval in seconds"},"repeatCount":{"type":"integer","description":"Number of times to repeat (-1 for infinite)"},"startTime":{"type":"string","description":"Start time in ISO format"},"endTime":{"type":"string","description":"End time in ISO format"}}},"complexJobTrigger":{"type":"object","description":"Complex job trigger configuration","properties":{"uiPassParam":{"type":"string","description":"UI parameter for trigger type"},"daysOfWeek":{"type":"array","description":"Days of week when job should run","items":{"type":"integer"}},"startTime":{"type":"string","description":"Start time in ISO format"},"endTime":{"type":"string","description":"End time in ISO format"}}},"inputFile":{"type":"string","description":"Input file path"},"outputFile":{"type":"string","description":"Output file path"},"duration":{"type":"integer","description":"Duration in milliseconds for blockouts"},"timeZone":{"type":"string","description":"Time zone for the schedule"},"jobParameters":{"type":"object","description":"Job parameters","properties":{"name":{"type":"string","description":"Parameter name"},"type":{"type":"string","description":"Parameter type"},"stringValue":{"type":"string","description":"Parameter value"}}}}}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/blockout/add":{"post":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Add blockout for scheduled jobs","consumes":["application/json","application/xml"],"description":"Creates a new blockout for scheduled jobs.\n\n**Example Request:**\n```\nPOST pentaho/api/scheduler/blockout/add\n```\n\n**cURL Example:**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/scheduler/blockout/add\" \\\n  -H \"Content-Type: application/xml\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -d '<jobScheduleRequest>\n    <jobName>DAILY-1820438815:admin:7740000</jobName>\n    <complexJobTrigger>\n      <uiPassParam>DAILY</uiPassParam>\n      <daysOfWeek>1</daysOfWeek>\n      <daysOfWeek>2</daysOfWeek>\n      <daysOfWeek>3</daysOfWeek>\n      <daysOfWeek>4</daysOfWeek>\n      <daysOfWeek>5</daysOfWeek>\n      <startTime>2014-08-19T10:51:00.000-04:00</startTime>\n      <endTime />\n    </complexJobTrigger>\n    <inputFile></inputFile>\n    <outputFile></outputFile>\n    <duration>7740000</duration>\n    <timeZone>America/New_York</timeZone>\n  </jobScheduleRequest>'\n```\n","requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/JobScheduleRequest"}},"application/xml":{"schema":{"$ref":"#/components/schemas/JobScheduleRequest"}}}},"responses":{"200":{"description":"Successfully created blockout schedule","content":{"text/plain":{"schema":{"type":"string","description":"ID of the blockout which was created"}}}},"401":{"description":"User is not authorized to create blockout"}}}}}}
````

## Get all blockout jobs

> Get all the blockout jobs in the system.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/scheduler/blockout/blockoutjobs\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/blockout/blockoutjobs>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`xml\
> \<jobs>\
> &#x20; \<job>\
> &#x20;   \<groupName>admin\</groupName>\
> &#x20;   \<jobId>admin  BlockoutAction  1408457558636\</jobId>\
> &#x20;   \<jobName>BlockoutAction\</jobName>\
> &#x20;   \<jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>TIME\_ZONE\_PARAM\</name>\
> &#x20;       \<value>America/New\_York\</value>\
> &#x20;     \</jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>DURATION\_PARAM\</name>\
> &#x20;       \<value>10080000\</value>\
> &#x20;     \</jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>uiPassParam\</name>\
> &#x20;       \<value>DAILY\</value>\
> &#x20;     \</jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>user\_locale\</name>\
> &#x20;       \<value>en\_US\</value>\
> &#x20;     \</jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>ActionAdapterQuartzJob-ActionUser\</name>\
> &#x20;       \<value>admin\</value>\
> &#x20;     \</jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>ActionAdapterQuartzJob-ActionClass\</name>\
> &#x20;       \<value>org.pentaho.platform.scheduler2.blockout.BlockoutAction\</value>\
> &#x20;     \</jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>lineage-id\</name>\
> &#x20;       \<value>0989726c-3247-4864-bc79-8e2a1dc60c58\</value>\
> &#x20;     \</jobParams>\
> &#x20;   \</jobParams>\
> &#x20;   \<jobTrigger xsi:type="complexJobTrigger">\
> &#x20;     \<cronString>0 12 10 ? \* 2,3,4,5,6 \*\</cronString>\
> &#x20;     \<duration>10080000\</duration>\
> &#x20;     \<startTime>2014-08-19T10:12:00-04:00\</startTime>\
> &#x20;     \<uiPassParam>DAILY\</uiPassParam>\
> &#x20;     \<dayOfMonthRecurrences />\
> &#x20;     \<dayOfWeekRecurrences>\
> &#x20;       \<recurrenceList>\
> &#x20;         \<values>2\</values>\
> &#x20;         \<values>3\</values>\
> &#x20;         \<values>4\</values>\
> &#x20;         \<values>5\</values>\
> &#x20;         \<values>6\</values>\
> &#x20;       \</recurrenceList>\
> &#x20;     \</dayOfWeekRecurrences>\
> &#x20;     \<hourlyRecurrences>\
> &#x20;       \<recurrenceList>\
> &#x20;         \<values>10\</values>\
> &#x20;       \</recurrenceList>\
> &#x20;     \</hourlyRecurrences>\
> &#x20;     \<minuteRecurrences>\
> &#x20;       \<recurrenceList>\
> &#x20;         \<values>12\</values>\
> &#x20;       \</recurrenceList>\
> &#x20;     \</minuteRecurrences>\
> &#x20;     \<monthlyRecurrences />\
> &#x20;     \<secondRecurrences>\
> &#x20;       \<recurrenceList>\
> &#x20;         \<values>0\</values>\
> &#x20;       \</recurrenceList>\
> &#x20;     \</secondRecurrences>\
> &#x20;     \<yearlyRecurrences />\
> &#x20;   \</jobTrigger>\
> &#x20;   \<nextRun>2014-08-20T10:12:00-04:00\</nextRun>\
> &#x20;   \<state>NORMAL\</state>\
> &#x20;   \<userName>admin\</userName>\
> &#x20; \</job>\
> \</jobs>\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A Response object that contains a list of blockout jobs.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"JobWrapper":{"type":"object","description":"Wrapper for job collections","properties":{"job":{"type":"array","description":"Array of jobs","items":{"$ref":"#/components/schemas/Job"}}}},"Job":{"type":"object","description":"Job information","properties":{"groupName":{"type":"string","description":"Group name of the job"},"jobId":{"type":"string","description":"Unique identifier for the job"},"jobName":{"type":"string","description":"Name of the job"},"jobParams":{"type":"array","description":"Job parameters","items":{"type":"object","properties":{"name":{"type":"string","description":"Parameter name"},"value":{"type":"string","description":"Parameter value"}}}},"jobTrigger":{"type":"object","description":"Job trigger configuration","properties":{"duration":{"type":"integer","description":"Duration of the trigger"},"startTime":{"type":"string","description":"Start time in ISO format"},"uiPassParam":{"type":"string","description":"UI parameter for trigger type"},"repeatCount":{"type":"integer","description":"Number of times to repeat"},"repeatInterval":{"type":"integer","description":"Repeat interval in seconds"}}},"lastRun":{"type":"string","description":"Last run time in ISO format"},"nextRun":{"type":"string","description":"Next run time in ISO format"},"state":{"type":"string","description":"Current state of the job"},"userName":{"type":"string","description":"User who owns the job"}}}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/blockout/blockoutjobs":{"get":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Get all blockout jobs","produces":["application/json","application/xml"],"description":"Get all the blockout jobs in the system.\n\n**Example Request:**\n```\nGET pentaho/api/scheduler/blockout/blockoutjobs\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/scheduler/blockout/blockoutjobs\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Example Response:**\n```xml\n<jobs>\n  <job>\n    <groupName>admin</groupName>\n    <jobId>admin  BlockoutAction  1408457558636</jobId>\n    <jobName>BlockoutAction</jobName>\n    <jobParams>\n      <jobParams>\n        <name>TIME_ZONE_PARAM</name>\n        <value>America/New_York</value>\n      </jobParams>\n      <jobParams>\n        <name>DURATION_PARAM</name>\n        <value>10080000</value>\n      </jobParams>\n      <jobParams>\n        <name>uiPassParam</name>\n        <value>DAILY</value>\n      </jobParams>\n      <jobParams>\n        <name>user_locale</name>\n        <value>en_US</value>\n      </jobParams>\n      <jobParams>\n        <name>ActionAdapterQuartzJob-ActionUser</name>\n        <value>admin</value>\n      </jobParams>\n      <jobParams>\n        <name>ActionAdapterQuartzJob-ActionClass</name>\n        <value>org.pentaho.platform.scheduler2.blockout.BlockoutAction</value>\n      </jobParams>\n      <jobParams>\n        <name>lineage-id</name>\n        <value>0989726c-3247-4864-bc79-8e2a1dc60c58</value>\n      </jobParams>\n    </jobParams>\n    <jobTrigger xsi:type=\"complexJobTrigger\">\n      <cronString>0 12 10 ? * 2,3,4,5,6 *</cronString>\n      <duration>10080000</duration>\n      <startTime>2014-08-19T10:12:00-04:00</startTime>\n      <uiPassParam>DAILY</uiPassParam>\n      <dayOfMonthRecurrences />\n      <dayOfWeekRecurrences>\n        <recurrenceList>\n          <values>2</values>\n          <values>3</values>\n          <values>4</values>\n          <values>5</values>\n          <values>6</values>\n        </recurrenceList>\n      </dayOfWeekRecurrences>\n      <hourlyRecurrences>\n        <recurrenceList>\n          <values>10</values>\n        </recurrenceList>\n      </hourlyRecurrences>\n      <minuteRecurrences>\n        <recurrenceList>\n          <values>12</values>\n        </recurrenceList>\n      </minuteRecurrences>\n      <monthlyRecurrences />\n      <secondRecurrences>\n        <recurrenceList>\n          <values>0</values>\n        </recurrenceList>\n      </secondRecurrences>\n      <yearlyRecurrences />\n    </jobTrigger>\n    <nextRun>2014-08-20T10:12:00-04:00</nextRun>\n    <state>NORMAL</state>\n    <userName>admin</userName>\n  </job>\n</jobs>\n```\n\n**Returns:**\nA Response object that contains a list of blockout jobs.\n","responses":{"200":{"description":"Successfully retrieved blockout jobs","content":{"application/json":{"schema":{"$ref":"#/components/schemas/JobWrapper"}},"application/xml":{"schema":{"$ref":"#/components/schemas/JobWrapper"}}}},"500":{"description":"Error while retrieving blockout jobs"}}}}}}
````

## Check blockout status

> Check the status of the selected blockout schedule.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST pentaho/api/scheduler/blockout/blockstatus\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/blockout/blockstatus>" \\\
> &#x20; -H "Content-Type: application/xml" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -d '\<jobScheduleRequest>\
> &#x20;   \<jobName>DAILY-1820438815:admin:7740000\</jobName>\
> &#x20;   \<complexJobTrigger>\
> &#x20;     \<uiPassParam>DAILY\</uiPassParam>\
> &#x20;     \<daysOfWeek>1\</daysOfWeek>\
> &#x20;     \<daysOfWeek>2\</daysOfWeek>\
> &#x20;     \<daysOfWeek>3\</daysOfWeek>\
> &#x20;     \<daysOfWeek>4\</daysOfWeek>\
> &#x20;     \<daysOfWeek>5\</daysOfWeek>\
> &#x20;     \<startTime>2014-08-19T10:51:00.000-04:00\</startTime>\
> &#x20;     \<endTime />\
> &#x20;   \</complexJobTrigger>\
> &#x20;   \<inputFile>\</inputFile>\
> &#x20;   \<outputFile>\</outputFile>\
> &#x20;   \<duration>7740000\</duration>\
> &#x20;   \<timeZone>America/New\_York\</timeZone>\
> &#x20; \</jobScheduleRequest>'\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`xml\
> \<blockStatusProxy>\
> &#x20; \<partiallyBlocked>false\</partiallyBlocked>\
> &#x20; \<totallyBlocked>true\</totallyBlocked>\
> \</blockStatusProxy>\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> &#x20;A Response object which contains a BlockStatusProxy which contains totallyBlocked and partiallyBlocked flags<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"JobScheduleRequest":{"type":"object","description":"Request object for scheduling jobs and blockouts","properties":{"jobName":{"type":"string","description":"Name of the job"},"jobId":{"type":"string","description":"ID of the job (for updates)"},"simpleJobTrigger":{"type":"object","description":"Simple job trigger configuration","properties":{"uiPassParam":{"type":"string","description":"UI parameter for trigger type"},"repeatInterval":{"type":"integer","description":"Repeat interval in seconds"},"repeatCount":{"type":"integer","description":"Number of times to repeat (-1 for infinite)"},"startTime":{"type":"string","description":"Start time in ISO format"},"endTime":{"type":"string","description":"End time in ISO format"}}},"complexJobTrigger":{"type":"object","description":"Complex job trigger configuration","properties":{"uiPassParam":{"type":"string","description":"UI parameter for trigger type"},"daysOfWeek":{"type":"array","description":"Days of week when job should run","items":{"type":"integer"}},"startTime":{"type":"string","description":"Start time in ISO format"},"endTime":{"type":"string","description":"End time in ISO format"}}},"inputFile":{"type":"string","description":"Input file path"},"outputFile":{"type":"string","description":"Output file path"},"duration":{"type":"integer","description":"Duration in milliseconds for blockouts"},"timeZone":{"type":"string","description":"Time zone for the schedule"},"jobParameters":{"type":"object","description":"Job parameters","properties":{"name":{"type":"string","description":"Parameter name"},"type":{"type":"string","description":"Parameter type"},"stringValue":{"type":"string","description":"Parameter value"}}}}},"BlockStatusProxy":{"type":"object","description":"Blockout status information","properties":{"partiallyBlocked":{"type":"boolean","description":"Whether the schedule is partially blocked"},"totallyBlocked":{"type":"boolean","description":"Whether the schedule is totally blocked"}}}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/blockout/blockstatus":{"post":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Check blockout status","consumes":["application/json","application/xml"],"produces":["application/json","application/xml"],"description":"Check the status of the selected blockout schedule.\n\n**Example Request:**\n```\nPOST pentaho/api/scheduler/blockout/blockstatus\n```\n\n**cURL Example:**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/scheduler/blockout/blockstatus\" \\\n  -H \"Content-Type: application/xml\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -d '<jobScheduleRequest>\n    <jobName>DAILY-1820438815:admin:7740000</jobName>\n    <complexJobTrigger>\n      <uiPassParam>DAILY</uiPassParam>\n      <daysOfWeek>1</daysOfWeek>\n      <daysOfWeek>2</daysOfWeek>\n      <daysOfWeek>3</daysOfWeek>\n      <daysOfWeek>4</daysOfWeek>\n      <daysOfWeek>5</daysOfWeek>\n      <startTime>2014-08-19T10:51:00.000-04:00</startTime>\n      <endTime />\n    </complexJobTrigger>\n    <inputFile></inputFile>\n    <outputFile></outputFile>\n    <duration>7740000</duration>\n    <timeZone>America/New_York</timeZone>\n  </jobScheduleRequest>'\n```\n\n**Example Response:**\n```xml\n<blockStatusProxy>\n  <partiallyBlocked>false</partiallyBlocked>\n  <totallyBlocked>true</totallyBlocked>\n</blockStatusProxy>\n```\n\n**Returns:**\n A Response object which contains a BlockStatusProxy which contains totallyBlocked and partiallyBlocked flags\n","requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/JobScheduleRequest"}},"application/xml":{"schema":{"$ref":"#/components/schemas/JobScheduleRequest"}}}},"responses":{"200":{"description":"Successfully got the blockout status","content":{"application/json":{"schema":{"$ref":"#/components/schemas/BlockStatusProxy"}},"application/xml":{"schema":{"$ref":"#/components/schemas/BlockStatusProxy"}}}},"401":{"description":"User is not authorized to get the blockout status"}}}}}}
````

## Check if blockouts exist

> Checks if there are blockouts in the system.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/scheduler/blockout/hasblockouts\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/blockout/hasblockouts>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> true\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> true or false whether there are blackouts or not.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/blockout/hasblockouts":{"get":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Check if blockouts exist","produces":["text/plain"],"description":"Checks if there are blockouts in the system.\n\n**Example Request:**\n```\nGET pentaho/api/scheduler/blockout/hasblockouts\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/scheduler/blockout/hasblockouts\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Example Response:**\n```\ntrue\n```\n\n**Returns:**\ntrue or false whether there are blackouts or not.\n","responses":{"200":{"description":"Successfully determined whether or not the system contains blockouts","content":{"text/plain":{"schema":{"type":"string","description":"true or false whether there are blackouts or not"}}}}}}}}}
````

## Check if blockout should fire now

> Checks if the selected blockout schedule should be fired now.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/scheduler/blockout/shouldFireNow\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/blockout/shouldFireNow>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> true\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> true or false whether the blockout should fire now.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/blockout/shouldFireNow":{"get":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Check if blockout should fire now","produces":["text/plain"],"description":"Checks if the selected blockout schedule should be fired now.\n\n**Example Request:**\n```\nGET pentaho/api/scheduler/blockout/shouldFireNow\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/scheduler/blockout/shouldFireNow\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Example Response:**\n```\ntrue\n```\n\n**Returns:**\ntrue or false whether the blockout should fire now.\n","responses":{"200":{"description":"Successful operation","content":{"text/plain":{"schema":{"type":"string","description":"true or false whether the blockout should fire now"}}}}}}}}}
````

## Update existing blockout

> Update an existing blockout.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST pentaho/api/scheduler/blockout/update?jobid=admin%09BlockoutAction%091410786491209\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/blockout/update?jobid=admin%09BlockoutAction%091410786491209>" \\\
> &#x20; -H "Content-Type: application/xml" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -d '\<jobScheduleRequest>\
> &#x20;   \<jobName>DAILY-1820438815:admin:7740000\</jobName>\
> &#x20;   \<complexJobTrigger>\
> &#x20;     \<uiPassParam>DAILY\</uiPassParam>\
> &#x20;     \<daysOfWeek>1\</daysOfWeek>\
> &#x20;     \<daysOfWeek>2\</daysOfWeek>\
> &#x20;     \<daysOfWeek>3\</daysOfWeek>\
> &#x20;     \<daysOfWeek>4\</daysOfWeek>\
> &#x20;     \<daysOfWeek>5\</daysOfWeek>\
> &#x20;     \<startTime>2012-01-12T10:51:00.000-04:00\</startTime>\
> &#x20;     \<endTime />\
> &#x20;   \</complexJobTrigger>\
> &#x20;   \<inputFile>\</inputFile>\
> &#x20;   \<outputFile>\</outputFile>\
> &#x20;   \<duration>7740000\</duration>\
> &#x20;   \<timeZone>America/New\_York\</timeZone>\
> &#x20; \</jobScheduleRequest>'\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A Response object which contains the ID of the blockout which was created.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"JobScheduleRequest":{"type":"object","description":"Request object for scheduling jobs and blockouts","properties":{"jobName":{"type":"string","description":"Name of the job"},"jobId":{"type":"string","description":"ID of the job (for updates)"},"simpleJobTrigger":{"type":"object","description":"Simple job trigger configuration","properties":{"uiPassParam":{"type":"string","description":"UI parameter for trigger type"},"repeatInterval":{"type":"integer","description":"Repeat interval in seconds"},"repeatCount":{"type":"integer","description":"Number of times to repeat (-1 for infinite)"},"startTime":{"type":"string","description":"Start time in ISO format"},"endTime":{"type":"string","description":"End time in ISO format"}}},"complexJobTrigger":{"type":"object","description":"Complex job trigger configuration","properties":{"uiPassParam":{"type":"string","description":"UI parameter for trigger type"},"daysOfWeek":{"type":"array","description":"Days of week when job should run","items":{"type":"integer"}},"startTime":{"type":"string","description":"Start time in ISO format"},"endTime":{"type":"string","description":"End time in ISO format"}}},"inputFile":{"type":"string","description":"Input file path"},"outputFile":{"type":"string","description":"Output file path"},"duration":{"type":"integer","description":"Duration in milliseconds for blockouts"},"timeZone":{"type":"string","description":"Time zone for the schedule"},"jobParameters":{"type":"object","description":"Job parameters","properties":{"name":{"type":"string","description":"Parameter name"},"type":{"type":"string","description":"Parameter type"},"stringValue":{"type":"string","description":"Parameter value"}}}}}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/blockout/update":{"post":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Update existing blockout","consumes":["application/json","application/xml"],"description":"Update an existing blockout.\n\n**Example Request:**\n```\nPOST pentaho/api/scheduler/blockout/update?jobid=admin%09BlockoutAction%091410786491209\n```\n\n**cURL Example:**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/scheduler/blockout/update?jobid=admin%09BlockoutAction%091410786491209\" \\\n  -H \"Content-Type: application/xml\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -d '<jobScheduleRequest>\n    <jobName>DAILY-1820438815:admin:7740000</jobName>\n    <complexJobTrigger>\n      <uiPassParam>DAILY</uiPassParam>\n      <daysOfWeek>1</daysOfWeek>\n      <daysOfWeek>2</daysOfWeek>\n      <daysOfWeek>3</daysOfWeek>\n      <daysOfWeek>4</daysOfWeek>\n      <daysOfWeek>5</daysOfWeek>\n      <startTime>2012-01-12T10:51:00.000-04:00</startTime>\n      <endTime />\n    </complexJobTrigger>\n    <inputFile></inputFile>\n    <outputFile></outputFile>\n    <duration>7740000</duration>\n    <timeZone>America/New_York</timeZone>\n  </jobScheduleRequest>'\n```\n\n**Returns:**\nA Response object which contains the ID of the blockout which was created.\n","parameters":[{"name":"jobid","in":"query","required":true,"description":"The jobId of the blockout we are editing","schema":{"type":"string"}}],"requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/JobScheduleRequest"}},"application/xml":{"schema":{"$ref":"#/components/schemas/JobScheduleRequest"}}}},"responses":{"200":{"description":"Successful operation","content":{"text/plain":{"schema":{"type":"string","description":"ID of the blockout which was updated"}}}},"401":{"description":"User is not authorized to update blockout"}}}}}}
````

## Check if blockout will fire

> Checks if the selected blockout schedule will be fired.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST pentaho/api/scheduler/blockout/willFire\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/blockout/willFire>" \\\
> &#x20; -H "Content-Type: application/xml" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -d '\<jobScheduleRequest>\
> &#x20;   \<jobName>DAILY-1820438815:admin:7740000\</jobName>\
> &#x20;   \<complexJobTrigger>\
> &#x20;     \<uiPassParam>DAILY\</uiPassParam>\
> &#x20;     \<daysOfWeek>1\</daysOfWeek>\
> &#x20;     \<daysOfWeek>2\</daysOfWeek>\
> &#x20;     \<daysOfWeek>3\</daysOfWeek>\
> &#x20;     \<daysOfWeek>4\</daysOfWeek>\
> &#x20;     \<daysOfWeek>5\</daysOfWeek>\
> &#x20;     \<startTime>2014-08-19T10:51:00.000-04:00\</startTime>\
> &#x20;     \<endTime />\
> &#x20;   \</complexJobTrigger>\
> &#x20;   \<inputFile>\</inputFile>\
> &#x20;   \<outputFile>\</outputFile>\
> &#x20;   \<duration>7740000\</duration>\
> &#x20;   \<timeZone>America/New\_York\</timeZone>\
> &#x20; \</jobScheduleRequest>'\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> false\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> true or false indicating whether the blockout will fire.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"JobScheduleRequest":{"type":"object","description":"Request object for scheduling jobs and blockouts","properties":{"jobName":{"type":"string","description":"Name of the job"},"jobId":{"type":"string","description":"ID of the job (for updates)"},"simpleJobTrigger":{"type":"object","description":"Simple job trigger configuration","properties":{"uiPassParam":{"type":"string","description":"UI parameter for trigger type"},"repeatInterval":{"type":"integer","description":"Repeat interval in seconds"},"repeatCount":{"type":"integer","description":"Number of times to repeat (-1 for infinite)"},"startTime":{"type":"string","description":"Start time in ISO format"},"endTime":{"type":"string","description":"End time in ISO format"}}},"complexJobTrigger":{"type":"object","description":"Complex job trigger configuration","properties":{"uiPassParam":{"type":"string","description":"UI parameter for trigger type"},"daysOfWeek":{"type":"array","description":"Days of week when job should run","items":{"type":"integer"}},"startTime":{"type":"string","description":"Start time in ISO format"},"endTime":{"type":"string","description":"End time in ISO format"}}},"inputFile":{"type":"string","description":"Input file path"},"outputFile":{"type":"string","description":"Output file path"},"duration":{"type":"integer","description":"Duration in milliseconds for blockouts"},"timeZone":{"type":"string","description":"Time zone for the schedule"},"jobParameters":{"type":"object","description":"Job parameters","properties":{"name":{"type":"string","description":"Parameter name"},"type":{"type":"string","description":"Parameter type"},"stringValue":{"type":"string","description":"Parameter value"}}}}}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/blockout/willFire":{"post":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Check if blockout will fire","consumes":["application/json","application/xml"],"produces":["text/plain"],"description":"Checks if the selected blockout schedule will be fired.\n\n**Example Request:**\n```\nPOST pentaho/api/scheduler/blockout/willFire\n```\n\n**cURL Example:**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/scheduler/blockout/willFire\" \\\n  -H \"Content-Type: application/xml\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -d '<jobScheduleRequest>\n    <jobName>DAILY-1820438815:admin:7740000</jobName>\n    <complexJobTrigger>\n      <uiPassParam>DAILY</uiPassParam>\n      <daysOfWeek>1</daysOfWeek>\n      <daysOfWeek>2</daysOfWeek>\n      <daysOfWeek>3</daysOfWeek>\n      <daysOfWeek>4</daysOfWeek>\n      <daysOfWeek>5</daysOfWeek>\n      <startTime>2014-08-19T10:51:00.000-04:00</startTime>\n      <endTime />\n    </complexJobTrigger>\n    <inputFile></inputFile>\n    <outputFile></outputFile>\n    <duration>7740000</duration>\n    <timeZone>America/New_York</timeZone>\n  </jobScheduleRequest>'\n```\n\n**Example Response:**\n```\nfalse\n```\n\n**Returns:**\ntrue or false indicating whether the blockout will fire.\n","requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/JobScheduleRequest"}},"application/xml":{"schema":{"$ref":"#/components/schemas/JobScheduleRequest"}}}},"responses":{"200":{"description":"Successful operation","content":{"text/plain":{"schema":{"type":"string","description":"true or false indicating whether the blockout will fire"}}}},"500":{"description":"An error occurred while determining blockouts being fired"}}}}}}
````

## Check user scheduling authority

> Checks whether the current user has authority to schedule any content in the platform.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/scheduler/canSchedule\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/canSchedule>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> true\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> true or false. true indicates scheduling is allowed and false indicates scheduling is not allowed for the user.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/canSchedule":{"get":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Check user scheduling authority","produces":["application/json"],"description":"Checks whether the current user has authority to schedule any content in the platform.\n\n**Example Request:**\n```\nGET pentaho/api/scheduler/canSchedule\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/scheduler/canSchedule\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Example Response:**\n```\ntrue\n```\n\n**Returns:**\ntrue or false. true indicates scheduling is allowed and false indicates scheduling is not allowed for the user.\n","responses":{"200":{"description":"Successfully retrieved the scheduling permission","content":{"application/json":{"schema":{"type":"string","description":"true or false indicating scheduling is allowed for the user"}}}},"500":{"description":"Unable to retrieve the scheduling permission"}}}}}}
````

## Get generated content for schedule

> Retrieve the list of execute content by lineage id.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/scheduler/generatedContentForSchedule?lineageId=:public:Steel%20Wheels:Inventory%20List%20(report).prpt\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/generatedContentForSchedule?lineageId=:public:Steel%20Wheels:Inventory%20List%20(report).prpt>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A list of RepositoryFileDto objects.\
> \
> \*\*Example Response:\*\*\
> \`\`\`xml\
> \<List>\
> &#x20; \<repositoryFileDto>\
> &#x20;   \<createdDate>1402911997019\</createdDate>\
> &#x20;   \<fileSize>3461\</fileSize>\
> &#x20;   \<folder>false\</folder>\
> &#x20;   \<hidden>false\</hidden>\
> &#x20;   \<id>ff11ac89-7eda-4c03-aab1-e27f9048fd38\</id>\
> &#x20;   \<lastModifiedDate>1406647160536\</lastModifiedDate>\
> &#x20;   \<locale>en\</locale>\
> &#x20;   \<localePropertiesMapEntries>\
> &#x20;     \<localeMapDto>\
> &#x20;       \<locale>default\</locale>\
> &#x20;       \<properties>\
> &#x20;         \<stringKeyStringValueDto>\
> &#x20;           \<key>file.title\</key>\
> &#x20;           \<value>myFile\</value>\
> &#x20;         \</stringKeyStringValueDto>\
> &#x20;         \<stringKeyStringValueDto>\
> &#x20;           \<key>jcr:primaryType\</key>\
> &#x20;           \<value>nt:unstructured\</value>\
> &#x20;         \</stringKeyStringValueDto>\
> &#x20;         \<stringKeyStringValueDto>\
> &#x20;           \<key>title\</key>\
> &#x20;           \<value>myFile\</value>\
> &#x20;         \</stringKeyStringValueDto>\
> &#x20;         \<stringKeyStringValueDto>\
> &#x20;           \<key>file.description\</key>\
> &#x20;           \<value>myFile Description\</value>\
> &#x20;         \</stringKeyStringValueDto>\
> &#x20;       \</properties>\
> &#x20;     \</localeMapDto>\
> &#x20;   \</localePropertiesMapEntries>\
> &#x20;   \<locked>false\</locked>\
> &#x20;   \<name>myFile.prpt\</name>\
> &#x20;   \<originalParentFolderPath>/public/admin\</originalParentFolderPath>\
> &#x20;   \<ownerType>-1\</ownerType>\
> &#x20;   \<path>/public/admin/ff11ac89-7eda-4c03-aab1-e27f9048fd38\</path>\
> &#x20;   \<title>myFile\</title>\
> &#x20;   \<versionId>1.9\</versionId>\
> &#x20;   \<versioned>true\</versioned>\
> &#x20; \</repositoryFileDto>\
> \</List>\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"RepositoryFileDto":{"type":"object","description":"Repository file data transfer object","properties":{"id":{"type":"string","description":"Unique identifier for the file"},"name":{"type":"string","description":"Name of the file"},"path":{"type":"string","description":"Full path to the file"},"folder":{"type":"boolean","description":"Whether this is a folder"},"hidden":{"type":"boolean","description":"Whether this file is hidden"},"versioned":{"type":"boolean","description":"Whether this file is versioned"},"locked":{"type":"boolean","description":"Whether this file is locked"},"fileSize":{"type":"integer","format":"int64","description":"Size of the file in bytes"},"createdDate":{"type":"string","format":"date-time","description":"When the file was created"},"lastModifiedDate":{"type":"string","format":"date-time","description":"When the file was last modified"},"ownerType":{"type":"integer","description":"Type of owner (USER, ROLE)"},"title":{"type":"string","description":"Title of the file"},"description":{"type":"string","description":"Description of the file"},"deletedDate":{"type":"string","format":"date-time","description":"When the file was deleted (if applicable)"},"locale":{"type":"string","description":"Locale of the file"},"originalParentFolderPath":{"type":"string","description":"Original parent folder path before deletion"},"versionId":{"type":"string","description":"Version identifier of the file"},"localePropertiesMapEntries":{"type":"array","description":"Locale-specific properties","items":{"type":"object","properties":{"locale":{"type":"string","description":"Locale identifier"},"properties":{"type":"array","description":"Key-value properties for this locale","items":{"type":"object","properties":{"key":{"type":"string","description":"Property key"},"value":{"type":"string","description":"Property value"}}}}}}}}}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/generatedContentForSchedule":{"get":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Get generated content for schedule","produces":["application/json","application/xml"],"description":"Retrieve the list of execute content by lineage id.\n\n**Example Request:**\n```\nGET pentaho/api/scheduler/generatedContentForSchedule?lineageId=:public:Steel%20Wheels:Inventory%20List%20(report).prpt\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/scheduler/generatedContentForSchedule?lineageId=:public:Steel%20Wheels:Inventory%20List%20(report).prpt\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Returns:**\nA list of RepositoryFileDto objects.\n\n**Example Response:**\n```xml\n<List>\n  <repositoryFileDto>\n    <createdDate>1402911997019</createdDate>\n    <fileSize>3461</fileSize>\n    <folder>false</folder>\n    <hidden>false</hidden>\n    <id>ff11ac89-7eda-4c03-aab1-e27f9048fd38</id>\n    <lastModifiedDate>1406647160536</lastModifiedDate>\n    <locale>en</locale>\n    <localePropertiesMapEntries>\n      <localeMapDto>\n        <locale>default</locale>\n        <properties>\n          <stringKeyStringValueDto>\n            <key>file.title</key>\n            <value>myFile</value>\n          </stringKeyStringValueDto>\n          <stringKeyStringValueDto>\n            <key>jcr:primaryType</key>\n            <value>nt:unstructured</value>\n          </stringKeyStringValueDto>\n          <stringKeyStringValueDto>\n            <key>title</key>\n            <value>myFile</value>\n          </stringKeyStringValueDto>\n          <stringKeyStringValueDto>\n            <key>file.description</key>\n            <value>myFile Description</value>\n          </stringKeyStringValueDto>\n        </properties>\n      </localeMapDto>\n    </localePropertiesMapEntries>\n    <locked>false</locked>\n    <name>myFile.prpt</name>\n    <originalParentFolderPath>/public/admin</originalParentFolderPath>\n    <ownerType>-1</ownerType>\n    <path>/public/admin/ff11ac89-7eda-4c03-aab1-e27f9048fd38</path>\n    <title>myFile</title>\n    <versionId>1.9</versionId>\n    <versioned>true</versioned>\n  </repositoryFileDto>\n</List>\n```\n","parameters":[{"name":"lineageId","in":"query","required":true,"description":"The path for the file","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully got the generated content for schedule","content":{"application/json":{"schema":{"type":"array","items":{"$ref":"#/components/schemas/RepositoryFileDto"}}},"application/xml":{"schema":{"type":"array","items":{"$ref":"#/components/schemas/RepositoryFileDto"}}}}}}}}}}
````

## Get content cleaner job

> Get the scheduled job created by the system for deleting generated files.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/scheduler/getContentCleanerJob\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/getContentCleanerJob>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A Job object containing the definition of the content cleaner job.\
> \
> \*\*Example Response:\*\*\
> \`\`\`xml\
> \<job>\
> &#x20; \<groupName>admin\</groupName>\
> &#x20; \<jobId>admin  GeneratedContentCleaner 1408377444383\</jobId>\
> &#x20; \<jobName>GeneratedContentCleaner\</jobName>\
> &#x20; \<jobParams>\
> &#x20;   \<jobParams>\
> &#x20;     \<name>uiPassParam\</name>\
> &#x20;     \<value>DAILY\</value>\
> &#x20;   \</jobParams>\
> &#x20;   \<jobParams>\
> &#x20;     \<name>age\</name>\
> &#x20;     \<value>15552000\</value>\
> &#x20;   \</jobParams>\
> &#x20;   \<jobParams>\
> &#x20;     \<name>user\_locale\</name>\
> &#x20;     \<value>en\_US\</value>\
> &#x20;   \</jobParams>\
> &#x20;   \<jobParams>\
> &#x20;     \<name>ActionAdapterQuartzJob-ActionUser\</name>\
> &#x20;     \<value>admin\</value>\
> &#x20;   \</jobParams>\
> &#x20;   \<jobParams>\
> &#x20;     \<name>ActionAdapterQuartzJob-ActionClass\</name>\
> &#x20;     \<value>org.pentaho.platform.admin.GeneratedContentCleaner\</value>\
> &#x20;   \</jobParams>\
> &#x20;   \<jobParams>\
> &#x20;     \<name>lineage-id\</name>\
> &#x20;     \<value>c3cfbad4-2e34-4dbd-8071-a2f3c7e8fab9\</value>\
> &#x20;   \</jobParams>\
> &#x20; \</jobParams>\
> &#x20; \<jobTrigger xsi:type="simpleJobTrigger">\
> &#x20;   \<duration>-1\</duration>\
> &#x20;   \<startTime>2014-08-18T11:57:00-04:00\</startTime>\
> &#x20;   \<uiPassParam>DAILY\</uiPassParam>\
> &#x20;   \<repeatCount>-1\</repeatCount>\
> &#x20;   \<repeatInterval>86400\</repeatInterval>\
> &#x20; \</jobTrigger>\
> &#x20; \<lastRun>2014-08-18T11:57:00-04:00\</lastRun>\
> &#x20; \<nextRun>2014-08-19T11:57:00-04:00\</nextRun>\
> &#x20; \<state>NORMAL\</state>\
> &#x20; \<userName>admin\</userName>\
> \</job>\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"Job":{"type":"object","description":"Job information","properties":{"groupName":{"type":"string","description":"Group name of the job"},"jobId":{"type":"string","description":"Unique identifier for the job"},"jobName":{"type":"string","description":"Name of the job"},"jobParams":{"type":"array","description":"Job parameters","items":{"type":"object","properties":{"name":{"type":"string","description":"Parameter name"},"value":{"type":"string","description":"Parameter value"}}}},"jobTrigger":{"type":"object","description":"Job trigger configuration","properties":{"duration":{"type":"integer","description":"Duration of the trigger"},"startTime":{"type":"string","description":"Start time in ISO format"},"uiPassParam":{"type":"string","description":"UI parameter for trigger type"},"repeatCount":{"type":"integer","description":"Number of times to repeat"},"repeatInterval":{"type":"integer","description":"Repeat interval in seconds"}}},"lastRun":{"type":"string","description":"Last run time in ISO format"},"nextRun":{"type":"string","description":"Next run time in ISO format"},"state":{"type":"string","description":"Current state of the job"},"userName":{"type":"string","description":"User who owns the job"}}}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/getContentCleanerJob":{"get":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Get content cleaner job","produces":["application/json","application/xml"],"description":"Get the scheduled job created by the system for deleting generated files.\n\n**Example Request:**\n```\nGET pentaho/api/scheduler/getContentCleanerJob\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/scheduler/getContentCleanerJob\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Returns:**\nA Job object containing the definition of the content cleaner job.\n\n**Example Response:**\n```xml\n<job>\n  <groupName>admin</groupName>\n  <jobId>admin  GeneratedContentCleaner 1408377444383</jobId>\n  <jobName>GeneratedContentCleaner</jobName>\n  <jobParams>\n    <jobParams>\n      <name>uiPassParam</name>\n      <value>DAILY</value>\n    </jobParams>\n    <jobParams>\n      <name>age</name>\n      <value>15552000</value>\n    </jobParams>\n    <jobParams>\n      <name>user_locale</name>\n      <value>en_US</value>\n    </jobParams>\n    <jobParams>\n      <name>ActionAdapterQuartzJob-ActionUser</name>\n      <value>admin</value>\n    </jobParams>\n    <jobParams>\n      <name>ActionAdapterQuartzJob-ActionClass</name>\n      <value>org.pentaho.platform.admin.GeneratedContentCleaner</value>\n    </jobParams>\n    <jobParams>\n      <name>lineage-id</name>\n      <value>c3cfbad4-2e34-4dbd-8071-a2f3c7e8fab9</value>\n    </jobParams>\n  </jobParams>\n  <jobTrigger xsi:type=\"simpleJobTrigger\">\n    <duration>-1</duration>\n    <startTime>2014-08-18T11:57:00-04:00</startTime>\n    <uiPassParam>DAILY</uiPassParam>\n    <repeatCount>-1</repeatCount>\n    <repeatInterval>86400</repeatInterval>\n  </jobTrigger>\n  <lastRun>2014-08-18T11:57:00-04:00</lastRun>\n  <nextRun>2014-08-19T11:57:00-04:00</nextRun>\n  <state>NORMAL</state>\n  <userName>admin</userName>\n</job>\n```\n","responses":{"200":{"description":"Content cleaner job successfully retrieved","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Job"}},"application/xml":{"schema":{"$ref":"#/components/schemas/Job"}}}},"204":{"description":"No content cleaner job exists"}}}}}}
````

## Get all jobs

> Retrieve the all the job(s) visible to the current users.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/scheduler/getJobs\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/getJobs>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A list of jobs that are visible to the current users.\
> \
> \*\*Example Response:\*\*\
> \`\`\`xml\
> \<jobs>\
> &#x20; \<job>\
> &#x20;   \<groupName>admin\</groupName>\
> &#x20;   \<jobId>admin  PentahoSystemVersionCheck 1408369303507\</jobId>\
> &#x20;   \<jobName>PentahoSystemVersionCheck\</jobName>\
> &#x20;   \<jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>ActionAdapterQuartzJob-ActionUser\</name>\
> &#x20;       \<value>admin\</value>\
> &#x20;     \</jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>ActionAdapterQuartzJob-ActionClass\</name>\
> &#x20;       \<value>org.pentaho.platform.scheduler2.versionchecker.VersionCheckerAction\</value>\
> &#x20;     \</jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>lineage-id\</name>\
> &#x20;       \<value>1986cc90-cf87-43f6-8924-9d6e443e7d5d\</value>\
> &#x20;     \</jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>versionRequestFlags\</name>\
> &#x20;       \<value>0\</value>\
> &#x20;     \</jobParams>\
> &#x20;   \</jobParams>\
> &#x20;   \<jobTrigger xsi:type="simpleJobTrigger">\
> &#x20;     \<duration>-1\</duration>\
> &#x20;     \<startTime>2014-08-18T09:41:43.506-04:00\</startTime>\
> &#x20;     \<repeatCount>-1\</repeatCount>\
> &#x20;     \<repeatInterval>86400\</repeatInterval>\
> &#x20;   \</jobTrigger>\
> &#x20;   \<lastRun>2014-08-18T11:37:31.412-04:00\</lastRun>\
> &#x20;   \<nextRun>2014-08-19T09:41:43.506-04:00\</nextRun>\
> &#x20;   \<state>NORMAL\</state>\
> &#x20;   \<userName>admin\</userName>\
> &#x20; \</job>\
> &#x20; \<job>\
> &#x20;   \<groupName>admin\</groupName>\
> &#x20;   \<jobId>admin UpdateAuditData 1408373019115\</jobId>\
> &#x20;   \<jobName>UpdateAuditData\</jobName>\
> &#x20;   \<jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>autoCreateUniqueFilename\</name>\
> &#x20;       \<value>false\</value>\
> &#x20;     \</jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>uiPassParam\</name>\
> &#x20;       \<value>MINUTES\</value>\
> &#x20;     \</jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>ActionAdapterQuartzJob-StreamProvider\</name>\
> &#x20;       \<value>input file = /public/pentaho-operations-mart/update\_audit\_mart\_data/UpdateAuditData.xaction:outputFile = /public/pentaho-operations-mart/generated\_logs/UpdateAuditData.\*\</value>\
> &#x20;     \</jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>user\_locale\</name>\
> &#x20;       \<value>en\_US\</value>\
> &#x20;     \</jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>ActionAdapterQuartzJob-ActionUser\</name>\
> &#x20;       \<value>admin\</value>\
> &#x20;     \</jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>ActionAdapterQuartzJob-ActionId\</name>\
> &#x20;       \<value>xaction.backgroundExecution\</value>\
> &#x20;     \</jobParams>\
> &#x20;     \<jobParams>\
> &#x20;       \<name>lineage-id\</name>\
> &#x20;       \<value>1f2402c4-0a70-40e4-b428-0d328f504cb3\</value>\
> &#x20;     \</jobParams>\
> &#x20;   \</jobParams>\
> &#x20;   \<jobTrigger xsi:type="simpleJobTrigger">\
> &#x20;     \<duration>-1\</duration>\
> &#x20;     \<startTime>2014-07-14T12:47:00-04:00\</startTime>\
> &#x20;     \<uiPassParam>MINUTES\</uiPassParam>\
> &#x20;     \<repeatCount>-1\</repeatCount>\
> &#x20;     \<repeatInterval>1800\</repeatInterval>\
> &#x20;   \</jobTrigger>\
> &#x20;   \<lastRun>2014-08-18T12:47:00-04:00\</lastRun>\
> &#x20;   \<nextRun>2014-08-18T13:17:00-04:00\</nextRun>\
> &#x20;   \<state>NORMAL\</state>\
> &#x20;   \<userName>admin\</userName>\
> &#x20; \</job>\
> \</jobs>\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"JobWrapper":{"type":"object","description":"Wrapper for job collections","properties":{"job":{"type":"array","description":"Array of jobs","items":{"$ref":"#/components/schemas/Job"}}}},"Job":{"type":"object","description":"Job information","properties":{"groupName":{"type":"string","description":"Group name of the job"},"jobId":{"type":"string","description":"Unique identifier for the job"},"jobName":{"type":"string","description":"Name of the job"},"jobParams":{"type":"array","description":"Job parameters","items":{"type":"object","properties":{"name":{"type":"string","description":"Parameter name"},"value":{"type":"string","description":"Parameter value"}}}},"jobTrigger":{"type":"object","description":"Job trigger configuration","properties":{"duration":{"type":"integer","description":"Duration of the trigger"},"startTime":{"type":"string","description":"Start time in ISO format"},"uiPassParam":{"type":"string","description":"UI parameter for trigger type"},"repeatCount":{"type":"integer","description":"Number of times to repeat"},"repeatInterval":{"type":"integer","description":"Repeat interval in seconds"}}},"lastRun":{"type":"string","description":"Last run time in ISO format"},"nextRun":{"type":"string","description":"Next run time in ISO format"},"state":{"type":"string","description":"Current state of the job"},"userName":{"type":"string","description":"User who owns the job"}}}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/getJobs":{"get":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Get all jobs","produces":["application/json","application/xml"],"description":"Retrieve the all the job(s) visible to the current users.\n\n**Example Request:**\n```\nGET pentaho/api/scheduler/getJobs\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/scheduler/getJobs\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Returns:**\nA list of jobs that are visible to the current users.\n\n**Example Response:**\n```xml\n<jobs>\n  <job>\n    <groupName>admin</groupName>\n    <jobId>admin  PentahoSystemVersionCheck 1408369303507</jobId>\n    <jobName>PentahoSystemVersionCheck</jobName>\n    <jobParams>\n      <jobParams>\n        <name>ActionAdapterQuartzJob-ActionUser</name>\n        <value>admin</value>\n      </jobParams>\n      <jobParams>\n        <name>ActionAdapterQuartzJob-ActionClass</name>\n        <value>org.pentaho.platform.scheduler2.versionchecker.VersionCheckerAction</value>\n      </jobParams>\n      <jobParams>\n        <name>lineage-id</name>\n        <value>1986cc90-cf87-43f6-8924-9d6e443e7d5d</value>\n      </jobParams>\n      <jobParams>\n        <name>versionRequestFlags</name>\n        <value>0</value>\n      </jobParams>\n    </jobParams>\n    <jobTrigger xsi:type=\"simpleJobTrigger\">\n      <duration>-1</duration>\n      <startTime>2014-08-18T09:41:43.506-04:00</startTime>\n      <repeatCount>-1</repeatCount>\n      <repeatInterval>86400</repeatInterval>\n    </jobTrigger>\n    <lastRun>2014-08-18T11:37:31.412-04:00</lastRun>\n    <nextRun>2014-08-19T09:41:43.506-04:00</nextRun>\n    <state>NORMAL</state>\n    <userName>admin</userName>\n  </job>\n  <job>\n    <groupName>admin</groupName>\n    <jobId>admin UpdateAuditData 1408373019115</jobId>\n    <jobName>UpdateAuditData</jobName>\n    <jobParams>\n      <jobParams>\n        <name>autoCreateUniqueFilename</name>\n        <value>false</value>\n      </jobParams>\n      <jobParams>\n        <name>uiPassParam</name>\n        <value>MINUTES</value>\n      </jobParams>\n      <jobParams>\n        <name>ActionAdapterQuartzJob-StreamProvider</name>\n        <value>input file = /public/pentaho-operations-mart/update_audit_mart_data/UpdateAuditData.xaction:outputFile = /public/pentaho-operations-mart/generated_logs/UpdateAuditData.*</value>\n      </jobParams>\n      <jobParams>\n        <name>user_locale</name>\n        <value>en_US</value>\n      </jobParams>\n      <jobParams>\n        <name>ActionAdapterQuartzJob-ActionUser</name>\n        <value>admin</value>\n      </jobParams>\n      <jobParams>\n        <name>ActionAdapterQuartzJob-ActionId</name>\n        <value>xaction.backgroundExecution</value>\n      </jobParams>\n      <jobParams>\n        <name>lineage-id</name>\n        <value>1f2402c4-0a70-40e4-b428-0d328f504cb3</value>\n      </jobParams>\n    </jobParams>\n    <jobTrigger xsi:type=\"simpleJobTrigger\">\n      <duration>-1</duration>\n      <startTime>2014-07-14T12:47:00-04:00</startTime>\n      <uiPassParam>MINUTES</uiPassParam>\n      <repeatCount>-1</repeatCount>\n      <repeatInterval>1800</repeatInterval>\n    </jobTrigger>\n    <lastRun>2014-08-18T12:47:00-04:00</lastRun>\n    <nextRun>2014-08-18T13:17:00-04:00</nextRun>\n    <state>NORMAL</state>\n    <userName>admin</userName>\n  </job>\n</jobs>\n```\n","responses":{"200":{"description":"Jobs retrieved successfully","content":{"application/json":{"schema":{"$ref":"#/components/schemas/JobWrapper"}},"application/xml":{"schema":{"$ref":"#/components/schemas/JobWrapper"}}}},"500":{"description":"Error while retrieving jobs"}}}}}}
````

## Check if scheduling is allowed for file

> Checks whether the current user may schedule a repository file in the platform.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/scheduler/isScheduleAllowed?id=b5f806b9-9f72-4814-b1e0-aa9e0ece7e1a\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/isScheduleAllowed?id=b5f806b9-9f72-4814-b1e0-aa9e0ece7e1a>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> true or false. true indicates scheduling is allowed and false indicates scheduling is not allowed for the file.\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> true\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/isScheduleAllowed":{"get":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Check if scheduling is allowed for file","produces":["text/plain"],"description":"Checks whether the current user may schedule a repository file in the platform.\n\n**Example Request:**\n```\nGET pentaho/api/scheduler/isScheduleAllowed?id=b5f806b9-9f72-4814-b1e0-aa9e0ece7e1a\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/scheduler/isScheduleAllowed?id=b5f806b9-9f72-4814-b1e0-aa9e0ece7e1a\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Returns:**\ntrue or false. true indicates scheduling is allowed and false indicates scheduling is not allowed for the file.\n\n**Example Response:**\n```\ntrue\n```\n","parameters":[{"name":"id","in":"query","required":true,"description":"The repository file ID of the content to checked","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully retrieved scheduling ability of repository file","content":{"text/plain":{"schema":{"type":"string","description":"true or false indicating scheduling is allowed for the file"}}}},"500":{"description":"Invalid repository file id"}}}}}}
````

## Create new scheduled job

> Creates a new scheduled job.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST pentaho/api/scheduler/job\
> \`\`\`\
> \
> \*\*POST data:\*\*\
> \`\`\`xml\
> \<jobScheduleRequest>\
> &#x20; \<jobName>JobName\</jobName>\
> &#x20; \<simpleJobTrigger>\
> &#x20;   \<uiPassParam>MINUTES\</uiPassParam>\
> &#x20;   \<repeatInterval>1800\</repeatInterval>\
> &#x20;   \<repeatCount>-1\</repeatCount>\
> &#x20;   \<startTime>2014-08-14T11:46:00.000-04:00\</startTime>\
> &#x20;   \<endTime />\
> &#x20; \</simpleJobTrigger>\
> &#x20; \<inputFile>/public/Steel Wheels/Top Customers (report).prpt\</inputFile>\
> &#x20; \<outputFile>/public/output\</outputFile>\
> &#x20; \<jobParameters>\
> &#x20;   \<name>ParameterName\</name>\
> &#x20;   \<type>string\</type>\
> &#x20;   \<stringValue>false\</stringValue>\
> &#x20; \</jobParameters>\
> \</jobScheduleRequest>\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/job>" \\\
> &#x20; -H "Content-Type: application/xml" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -d '\<jobScheduleRequest>\
> &#x20;   \<jobName>JobName\</jobName>\
> &#x20;   \<simpleJobTrigger>\
> &#x20;     \<uiPassParam>MINUTES\</uiPassParam>\
> &#x20;     \<repeatInterval>1800\</repeatInterval>\
> &#x20;     \<repeatCount>-1\</repeatCount>\
> &#x20;     \<startTime>2014-08-14T11:46:00.000-04:00\</startTime>\
> &#x20;     \<endTime />\
> &#x20;   \</simpleJobTrigger>\
> &#x20;   \<inputFile>/public/Steel Wheels/Top Customers (report).prpt\</inputFile>\
> &#x20;   \<outputFile>/public/output\</outputFile>\
> &#x20;   \<jobParameters>\
> &#x20;     \<name>ParameterName\</name>\
> &#x20;     \<type>string\</type>\
> &#x20;     \<stringValue>false\</stringValue>\
> &#x20;   \</jobParameters>\
> &#x20; \</jobScheduleRequest>'\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> admin  JobName  1410786491777\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A jax-rs Response object with the created jobId.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"JobScheduleRequest":{"type":"object","description":"Request object for scheduling jobs and blockouts","properties":{"jobName":{"type":"string","description":"Name of the job"},"jobId":{"type":"string","description":"ID of the job (for updates)"},"simpleJobTrigger":{"type":"object","description":"Simple job trigger configuration","properties":{"uiPassParam":{"type":"string","description":"UI parameter for trigger type"},"repeatInterval":{"type":"integer","description":"Repeat interval in seconds"},"repeatCount":{"type":"integer","description":"Number of times to repeat (-1 for infinite)"},"startTime":{"type":"string","description":"Start time in ISO format"},"endTime":{"type":"string","description":"End time in ISO format"}}},"complexJobTrigger":{"type":"object","description":"Complex job trigger configuration","properties":{"uiPassParam":{"type":"string","description":"UI parameter for trigger type"},"daysOfWeek":{"type":"array","description":"Days of week when job should run","items":{"type":"integer"}},"startTime":{"type":"string","description":"Start time in ISO format"},"endTime":{"type":"string","description":"End time in ISO format"}}},"inputFile":{"type":"string","description":"Input file path"},"outputFile":{"type":"string","description":"Output file path"},"duration":{"type":"integer","description":"Duration in milliseconds for blockouts"},"timeZone":{"type":"string","description":"Time zone for the schedule"},"jobParameters":{"type":"object","description":"Job parameters","properties":{"name":{"type":"string","description":"Parameter name"},"type":{"type":"string","description":"Parameter type"},"stringValue":{"type":"string","description":"Parameter value"}}}}}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/job":{"post":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Create new scheduled job","consumes":["application/json","application/xml"],"produces":["text/plain"],"description":"Creates a new scheduled job.\n\n**Example Request:**\n```\nPOST pentaho/api/scheduler/job\n```\n\n**POST data:**\n```xml\n<jobScheduleRequest>\n  <jobName>JobName</jobName>\n  <simpleJobTrigger>\n    <uiPassParam>MINUTES</uiPassParam>\n    <repeatInterval>1800</repeatInterval>\n    <repeatCount>-1</repeatCount>\n    <startTime>2014-08-14T11:46:00.000-04:00</startTime>\n    <endTime />\n  </simpleJobTrigger>\n  <inputFile>/public/Steel Wheels/Top Customers (report).prpt</inputFile>\n  <outputFile>/public/output</outputFile>\n  <jobParameters>\n    <name>ParameterName</name>\n    <type>string</type>\n    <stringValue>false</stringValue>\n  </jobParameters>\n</jobScheduleRequest>\n```\n\n**cURL Example:**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/scheduler/job\" \\\n  -H \"Content-Type: application/xml\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -d '<jobScheduleRequest>\n    <jobName>JobName</jobName>\n    <simpleJobTrigger>\n      <uiPassParam>MINUTES</uiPassParam>\n      <repeatInterval>1800</repeatInterval>\n      <repeatCount>-1</repeatCount>\n      <startTime>2014-08-14T11:46:00.000-04:00</startTime>\n      <endTime />\n    </simpleJobTrigger>\n    <inputFile>/public/Steel Wheels/Top Customers (report).prpt</inputFile>\n    <outputFile>/public/output</outputFile>\n    <jobParameters>\n      <name>ParameterName</name>\n      <type>string</type>\n      <stringValue>false</stringValue>\n    </jobParameters>\n  </jobScheduleRequest>'\n```\n\n**Example Response:**\n```\nadmin  JobName  1410786491777\n```\n\n**Returns:**\nA jax-rs Response object with the created jobId.\n","requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/JobScheduleRequest"}},"application/xml":{"schema":{"$ref":"#/components/schemas/JobScheduleRequest"}}}},"responses":{"200":{"description":"Schedule created successfully","content":{"text/plain":{"schema":{"type":"string","description":"Created jobId"}}}},"401":{"description":"User is not allowed to create schedules"},"403":{"description":"Cannot create schedules for the specified file"},"500":{"description":"An error occurred while creating a schedule"}}}}}}
````

## Get job information

> Retrieves information about a specified job.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/scheduler/jobinfo?jobId=admin%20JobName%201410786491777\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/jobinfo?jobId=admin%20JobName%201410786491777>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`xml\
> \<job>\
> &#x20; \<jobId>admin JobName 1410786491777\</jobId>\
> &#x20; \<jobName>JobName\</jobName>\
> &#x20; \<jobParams>\
> &#x20;   \<jobParams>\
> &#x20;     \<name>uiPassParam\</name>\
> &#x20;     \<value>MINUTES\</value>\
> &#x20;   \</jobParams>\
> &#x20;   \<jobParams>\
> &#x20;     \<name>ActionAdapterQuartzJob-StreamProvider\</name>\
> &#x20;     \<value>input file = /public/Steel Wheels/Top Customers (report).prpt:outputFile = /home/admin/JobName.\*\</value>\
> &#x20;   \</jobParams>\
> &#x20;   \<jobParams>\
> &#x20;     \<name>user\_locale\</name>\
> &#x20;     \<value>en\_US\</value>\
> &#x20;   \</jobParams>\
> &#x20;   \<jobParams>\
> &#x20;     \<name>ActionAdapterQuartzJob-ActionUser\</name>\
> &#x20;     \<value>admin\</value>\
> &#x20;   \</jobParams>\
> &#x20;   \<jobParams>\
> &#x20;     \<name>ActionAdapterQuartzJob-ActionId\</name>\
> &#x20;     \<value>prpt.backgroundExecution\</value>\
> &#x20;   \</jobParams>\
> &#x20;   \<jobParams>\
> &#x20;     \<name>ParameterName\</name>\
> &#x20;     \<value>false\</value>\
> &#x20;   \</jobParams>\
> &#x20;   \<jobParams>\
> &#x20;     \<name>lineage-id\</name>\
> &#x20;     \<value>5212a120-3294-49e8-9c5d-c755b9766c43\</value>\
> &#x20;   \</jobParams>\
> &#x20; \</jobParams>\
> &#x20; \<jobTrigger xsi:type="simpleJobTrigger">\
> &#x20;   \<duration>-1\</duration>\
> &#x20;   \<startTime>2014-08-14T11:46:00-04:00\</startTime>\
> &#x20;   \<uiPassParam>MINUTES\</uiPassParam>\
> &#x20;   \<repeatCount>-1\</repeatCount>\
> &#x20;   \<repeatInterval>1800\</repeatInterval>\
> &#x20; \</jobTrigger>\
> &#x20; \<nextRun>2014-08-14T11:46:00-04:00\</nextRun>\
> &#x20; \<state>NORMAL\</state>\
> &#x20; \<userName>admin\</userName>\
> \</job>\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A Job object containing the info for the specified job.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"Job":{"type":"object","description":"Job information","properties":{"groupName":{"type":"string","description":"Group name of the job"},"jobId":{"type":"string","description":"Unique identifier for the job"},"jobName":{"type":"string","description":"Name of the job"},"jobParams":{"type":"array","description":"Job parameters","items":{"type":"object","properties":{"name":{"type":"string","description":"Parameter name"},"value":{"type":"string","description":"Parameter value"}}}},"jobTrigger":{"type":"object","description":"Job trigger configuration","properties":{"duration":{"type":"integer","description":"Duration of the trigger"},"startTime":{"type":"string","description":"Start time in ISO format"},"uiPassParam":{"type":"string","description":"UI parameter for trigger type"},"repeatCount":{"type":"integer","description":"Number of times to repeat"},"repeatInterval":{"type":"integer","description":"Repeat interval in seconds"}}},"lastRun":{"type":"string","description":"Last run time in ISO format"},"nextRun":{"type":"string","description":"Next run time in ISO format"},"state":{"type":"string","description":"Current state of the job"},"userName":{"type":"string","description":"User who owns the job"}}}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/jobinfo":{"get":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Get job information","produces":["application/json","application/xml"],"description":"Retrieves information about a specified job.\n\n**Example Request:**\n```\nGET pentaho/api/scheduler/jobinfo?jobId=admin%20JobName%201410786491777\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/scheduler/jobinfo?jobId=admin%20JobName%201410786491777\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Example Response:**\n```xml\n<job>\n  <jobId>admin JobName 1410786491777</jobId>\n  <jobName>JobName</jobName>\n  <jobParams>\n    <jobParams>\n      <name>uiPassParam</name>\n      <value>MINUTES</value>\n    </jobParams>\n    <jobParams>\n      <name>ActionAdapterQuartzJob-StreamProvider</name>\n      <value>input file = /public/Steel Wheels/Top Customers (report).prpt:outputFile = /home/admin/JobName.*</value>\n    </jobParams>\n    <jobParams>\n      <name>user_locale</name>\n      <value>en_US</value>\n    </jobParams>\n    <jobParams>\n      <name>ActionAdapterQuartzJob-ActionUser</name>\n      <value>admin</value>\n    </jobParams>\n    <jobParams>\n      <name>ActionAdapterQuartzJob-ActionId</name>\n      <value>prpt.backgroundExecution</value>\n    </jobParams>\n    <jobParams>\n      <name>ParameterName</name>\n      <value>false</value>\n    </jobParams>\n    <jobParams>\n      <name>lineage-id</name>\n      <value>5212a120-3294-49e8-9c5d-c755b9766c43</value>\n    </jobParams>\n  </jobParams>\n  <jobTrigger xsi:type=\"simpleJobTrigger\">\n    <duration>-1</duration>\n    <startTime>2014-08-14T11:46:00-04:00</startTime>\n    <uiPassParam>MINUTES</uiPassParam>\n    <repeatCount>-1</repeatCount>\n    <repeatInterval>1800</repeatInterval>\n  </jobTrigger>\n  <nextRun>2014-08-14T11:46:00-04:00</nextRun>\n  <state>NORMAL</state>\n  <userName>admin</userName>\n</job>\n```\n\n**Returns:**\nA Job object containing the info for the specified job.\n","parameters":[{"name":"jobId","in":"query","required":true,"description":"The jobId of the job for which we are requesting information","schema":{"type":"string"}},{"name":"asCronString","in":"query","required":false,"description":"Cron string (Unused)","schema":{"type":"string","default":"false"}}],"responses":{"200":{"description":"Successfully retrieved the information for the requested job","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Job"}},"application/xml":{"schema":{"$ref":"#/components/schemas/Job"}}}},"204":{"description":"jobId is valid, but the job is either finished or does not exists"},"500":{"description":"Internal error or invalid jobId"}}}}}}
````

## Get job state

> Checks the state of the selected scheduled job.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST pentaho/api/scheduler/jobState\
> \`\`\`\
> \
> \*\*POST data:\*\*\
> \`\`\`xml\
> \<jobRequest>\
> &#x20; \<jobId>admin  JobName 1410786491777\</jobId>\
> \</jobRequest>\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/jobState>" \\\
> &#x20; -H "Content-Type: application/xml" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -d '\<jobRequest>\
> &#x20;   \<jobId>admin  JobName 1410786491777\</jobId>\
> &#x20; \</jobRequest>'\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> NORMAL\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A jax-rs Response object containing the status of the scheduled job.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"JobRequest":{"type":"object","description":"Request object for job operations","properties":{"jobId":{"type":"string","description":"ID of the job"}}}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/jobState":{"post":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Get job state","consumes":["application/json","application/xml"],"produces":["text/plain"],"description":"Checks the state of the selected scheduled job.\n\n**Example Request:**\n```\nPOST pentaho/api/scheduler/jobState\n```\n\n**POST data:**\n```xml\n<jobRequest>\n  <jobId>admin  JobName 1410786491777</jobId>\n</jobRequest>\n```\n\n**cURL Example:**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/scheduler/jobState\" \\\n  -H \"Content-Type: application/xml\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -d '<jobRequest>\n    <jobId>admin  JobName 1410786491777</jobId>\n  </jobRequest>'\n```\n\n**Example Response:**\n```\nNORMAL\n```\n\n**Returns:**\nA jax-rs Response object containing the status of the scheduled job.\n","requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/JobRequest"}},"application/xml":{"schema":{"$ref":"#/components/schemas/JobRequest"}}}},"responses":{"200":{"description":"Successfully retrieved the state of the requested job","content":{"text/plain":{"schema":{"type":"string","description":"State of the scheduled job"}}}},"500":{"description":"Invalid jobId"}}}}}}
````

## Pause scheduler

> Pause the scheduler from a running state.\
> \
> \*\*POST data:\*\*\
> \`\`\`\
> This POST body does not contain data.\
> \`\`\`\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST pentaho/api/scheduler/pause\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/pause>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> PAUSED\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A jax-rs Response object containing the status of the scheduler.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/pause":{"post":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Pause scheduler","produces":["text/plain"],"description":"Pause the scheduler from a running state.\n\n**POST data:**\n```\nThis POST body does not contain data.\n```\n\n**Example Request:**\n```\nPOST pentaho/api/scheduler/pause\n```\n\n**cURL Example:**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/scheduler/pause\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Example Response:**\n```\nPAUSED\n```\n\n**Returns:**\nA jax-rs Response object containing the status of the scheduler.\n","responses":{"200":{"description":"Successfully paused the server","content":{"text/plain":{"schema":{"type":"string","description":"Status of the scheduler"}}}},"500":{"description":"An error occurred when pausing the scheduler"}}}}}}
````

## Pause scheduled job

> Pause the specified scheduled job.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST pentaho/api/scheduler/pauseJob\
> \`\`\`\
> \
> \*\*POST data:\*\*\
> \`\`\`xml\
> \<jobRequest>\
> &#x20; \<jobId>admin  JobName 1410786491777\</jobId>\
> \</jobRequest>\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/pauseJob>" \\\
> &#x20; -H "Content-Type: application/xml" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -d '\<jobRequest>\
> &#x20;   \<jobId>admin  JobName 1410786491777\</jobId>\
> &#x20; \</jobRequest>'\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> PAUSED\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A jax-rs Response object containing the status of the scheduled job.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"JobRequest":{"type":"object","description":"Request object for job operations","properties":{"jobId":{"type":"string","description":"ID of the job"}}}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/pauseJob":{"post":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Pause scheduled job","consumes":["application/json","application/xml"],"produces":["text/plain"],"description":"Pause the specified scheduled job.\n\n**Example Request:**\n```\nPOST pentaho/api/scheduler/pauseJob\n```\n\n**POST data:**\n```xml\n<jobRequest>\n  <jobId>admin  JobName 1410786491777</jobId>\n</jobRequest>\n```\n\n**cURL Example:**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/scheduler/pauseJob\" \\\n  -H \"Content-Type: application/xml\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -d '<jobRequest>\n    <jobId>admin  JobName 1410786491777</jobId>\n  </jobRequest>'\n```\n\n**Example Response:**\n```\nPAUSED\n```\n\n**Returns:**\nA jax-rs Response object containing the status of the scheduled job.\n","requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/JobRequest"}},"application/xml":{"schema":{"$ref":"#/components/schemas/JobRequest"}}}},"responses":{"200":{"description":"Successfully paused the job","content":{"text/plain":{"schema":{"type":"string","description":"Status of the scheduled job"}}}},"500":{"description":"Invalid jobId"}}}}}}
````

## Remove scheduled job

> Delete the specified scheduled job from the platform.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> PUT pentaho/api/scheduler/removeJob\
> \`\`\`\
> \
> \*\*PUT data:\*\*\
> \`\`\`xml\
> \<jobRequest>\
> &#x20; \<jobId>admin  BlockoutAction 1410786491503\</jobId>\
> \</jobRequest>\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X PUT \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/removeJob>" \\\
> &#x20; -H "Content-Type: application/xml" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -d '\<jobRequest>\
> &#x20;   \<jobId>admin  BlockoutAction 1410786491503\</jobId>\
> &#x20; \</jobRequest>'\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> REMOVED\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A jax-rs Response object containing the status of the scheduled job.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"JobRequest":{"type":"object","description":"Request object for job operations","properties":{"jobId":{"type":"string","description":"ID of the job"}}}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/removeJob":{"put":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Remove scheduled job","consumes":["application/json","application/xml"],"produces":["text/plain"],"description":"Delete the specified scheduled job from the platform.\n\n**Example Request:**\n```\nPUT pentaho/api/scheduler/removeJob\n```\n\n**PUT data:**\n```xml\n<jobRequest>\n  <jobId>admin  BlockoutAction 1410786491503</jobId>\n</jobRequest>\n```\n\n**cURL Example:**\n```bash\ncurl -X PUT \\\n  \"http://localhost:8080/pentaho/api/scheduler/removeJob\" \\\n  -H \"Content-Type: application/xml\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -d '<jobRequest>\n    <jobId>admin  BlockoutAction 1410786491503</jobId>\n  </jobRequest>'\n```\n\n**Example Response:**\n```\nREMOVED\n```\n\n**Returns:**\nA jax-rs Response object containing the status of the scheduled job.\n","requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/JobRequest"}},"application/xml":{"schema":{"$ref":"#/components/schemas/JobRequest"}}}},"responses":{"200":{"description":"Successfully removed the job","content":{"text/plain":{"schema":{"type":"string","description":"Status of the scheduled job"}}}},"500":{"description":"Invalid jobId"}}}}}}
````

## Remove scheduled job (deprecated)

> Delete the specified scheduled job from the platform.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> DELETE pentaho/api/scheduler/removeJob\
> \`\`\`\
> \
> \*\*DELETE data:\*\*\
> \`\`\`xml\
> \<jobRequest>\
> &#x20; \<jobId>admin  BlockoutAction 1410786491503\</jobId>\
> \</jobRequest>\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X DELETE \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/removeJob>" \\\
> &#x20; -H "Content-Type: application/xml" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -d '\<jobRequest>\
> &#x20;   \<jobId>admin  BlockoutAction 1410786491503\</jobId>\
> &#x20; \</jobRequest>'\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> REMOVED\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A jax-rs Response object containing the status of the scheduled job.\
> \
> \*\*Note:\*\* This method is deprecated. Use "PUT pentaho/api/scheduler/removeJob" instead.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"JobRequest":{"type":"object","description":"Request object for job operations","properties":{"jobId":{"type":"string","description":"ID of the job"}}}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/removeJob":{"delete":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Remove scheduled job (deprecated)","consumes":["application/json","application/xml"],"produces":["text/plain"],"description":"Delete the specified scheduled job from the platform.\n\n**Example Request:**\n```\nDELETE pentaho/api/scheduler/removeJob\n```\n\n**DELETE data:**\n```xml\n<jobRequest>\n  <jobId>admin  BlockoutAction 1410786491503</jobId>\n</jobRequest>\n```\n\n**cURL Example:**\n```bash\ncurl -X DELETE \\\n  \"http://localhost:8080/pentaho/api/scheduler/removeJob\" \\\n  -H \"Content-Type: application/xml\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -d '<jobRequest>\n    <jobId>admin  BlockoutAction 1410786491503</jobId>\n  </jobRequest>'\n```\n\n**Example Response:**\n```\nREMOVED\n```\n\n**Returns:**\nA jax-rs Response object containing the status of the scheduled job.\n\n**Note:** This method is deprecated. Use \"PUT pentaho/api/scheduler/removeJob\" instead.\n","requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/JobRequest"}},"application/xml":{"schema":{"$ref":"#/components/schemas/JobRequest"}}}},"responses":{"200":{"description":"Successfully removed the job","content":{"text/plain":{"schema":{"type":"string","description":"Status of the scheduled job"}}}},"500":{"description":"Invalid jobId"}}}}}}
````

## Resume scheduled job

> Resume the specified scheduled job.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST pentaho/api/scheduler/resumeJob\
> \`\`\`\
> \
> \*\*POST data:\*\*\
> \`\`\`xml\
> \<jobRequest>\
> &#x20; \<jobId>admin  JobName 1410786491777\</jobId>\
> \</jobRequest>\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/resumeJob>" \\\
> &#x20; -H "Content-Type: application/xml" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -d '\<jobRequest>\
> &#x20;   \<jobId>admin  JobName 1410786491777\</jobId>\
> &#x20; \</jobRequest>'\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> NORMAL\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A jax-rs Response object containing the status of the scheduled job.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"JobRequest":{"type":"object","description":"Request object for job operations","properties":{"jobId":{"type":"string","description":"ID of the job"}}}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/resumeJob":{"post":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Resume scheduled job","consumes":["application/json","application/xml"],"produces":["text/plain"],"description":"Resume the specified scheduled job.\n\n**Example Request:**\n```\nPOST pentaho/api/scheduler/resumeJob\n```\n\n**POST data:**\n```xml\n<jobRequest>\n  <jobId>admin  JobName 1410786491777</jobId>\n</jobRequest>\n```\n\n**cURL Example:**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/scheduler/resumeJob\" \\\n  -H \"Content-Type: application/xml\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -d '<jobRequest>\n    <jobId>admin  JobName 1410786491777</jobId>\n  </jobRequest>'\n```\n\n**Example Response:**\n```\nNORMAL\n```\n\n**Returns:**\nA jax-rs Response object containing the status of the scheduled job.\n","requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/JobRequest"}},"application/xml":{"schema":{"$ref":"#/components/schemas/JobRequest"}}}},"responses":{"200":{"description":"Successfully resumed the job","content":{"text/plain":{"schema":{"type":"string","description":"Status of the scheduled job"}}}},"500":{"description":"Invalid jobId"}}}}}}
````

## Shutdown scheduler

> Shuts down the scheduler.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST pentaho/api/scheduler/shutdown\
> \`\`\`\
> \
> \*\*POST data:\*\*\
> \`\`\`\
> This POST body does not contain data.\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/shutdown>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> PAUSED\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A jax-rs Response object containing the status of the scheduler.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/shutdown":{"post":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Shutdown scheduler","produces":["text/plain"],"description":"Shuts down the scheduler.\n\n**Example Request:**\n```\nPOST pentaho/api/scheduler/shutdown\n```\n\n**POST data:**\n```\nThis POST body does not contain data.\n```\n\n**cURL Example:**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/scheduler/shutdown\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Example Response:**\n```\nPAUSED\n```\n\n**Returns:**\nA jax-rs Response object containing the status of the scheduler.\n","responses":{"200":{"description":"Successfully shut down the server","content":{"text/plain":{"schema":{"type":"string","description":"Status of the scheduler"}}}},"500":{"description":"An error occurred when shutting down the scheduler"}}}}}}
````

## Start/resume scheduler

> Resume the scheduler from a paused state.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST pentaho/api/scheduler/start\
> \`\`\`\
> \
> \*\*POST data:\*\*\
> \`\`\`\
> This POST body does not contain data.\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/start>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> RUNNING\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A jax-rs Response object containing the status of the scheduler.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/start":{"post":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Start/resume scheduler","produces":["text/plain"],"description":"Resume the scheduler from a paused state.\n\n**Example Request:**\n```\nPOST pentaho/api/scheduler/start\n```\n\n**POST data:**\n```\nThis POST body does not contain data.\n```\n\n**cURL Example:**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/scheduler/start\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Example Response:**\n```\nRUNNING\n```\n\n**Returns:**\nA jax-rs Response object containing the status of the scheduler.\n","responses":{"200":{"description":"Successfully started the server","content":{"text/plain":{"schema":{"type":"string","description":"Status of the scheduler"}}}},"500":{"description":"An error occurred when resuming the scheduler"}}}}}}
````

## Get scheduler state

> Returns the current state of the scheduler.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/scheduler/state\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/state>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> RUNNING\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> status of the scheduler as RUNNING or PAUSED.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/state":{"get":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Get scheduler state","produces":["text/plain"],"description":"Returns the current state of the scheduler.\n\n**Example Request:**\n```\nGET pentaho/api/scheduler/state\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/scheduler/state\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Example Response:**\n```\nRUNNING\n```\n\n**Returns:**\nstatus of the scheduler as RUNNING or PAUSED.\n","responses":{"200":{"description":"Successfully retrieved the state of the scheduler","content":{"text/plain":{"schema":{"type":"string","description":"Status of the scheduler as RUNNING or PAUSED"}}}},"500":{"description":"An error occurred when getting the state of the scheduler"}}}}}}
````

## Execute job immediately

> Execute a previously scheduled job.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST pentaho/api/scheduler/triggerNow\
> \`\`\`\
> \
> \*\*POST data:\*\*\
> \`\`\`xml\
> \<jobRequest>\
> &#x20; \<jobId>admin  JobName 1410786491777\</jobId>\
> \</jobRequest>\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/scheduler/triggerNow>" \\\
> &#x20; -H "Content-Type: application/xml" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -d '\<jobRequest>\
> &#x20;   \<jobId>admin  JobName 1410786491777\</jobId>\
> &#x20; \</jobRequest>'\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> NORMAL\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A Response object indicating the status of the scheduler.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Scheduling APIs - Scheduler Resource","description":"The SchedulerResource service provides the means to create, read, update, delete and list schedules and blockout periods. Also provides the ability to control the status of schedules and scheduler."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"JobRequest":{"type":"object","description":"Request object for job operations","properties":{"jobId":{"type":"string","description":"ID of the job"}}}}},"paths":{"/plugin/scheduler-plugin/api/scheduler/triggerNow":{"post":{"tags":["Scheduling APIs - Scheduler Resource"],"summary":"Execute job immediately","consumes":["application/json","application/xml"],"produces":["text/plain"],"description":"Execute a previously scheduled job.\n\n**Example Request:**\n```\nPOST pentaho/api/scheduler/triggerNow\n```\n\n**POST data:**\n```xml\n<jobRequest>\n  <jobId>admin  JobName 1410786491777</jobId>\n</jobRequest>\n```\n\n**cURL Example:**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/scheduler/triggerNow\" \\\n  -H \"Content-Type: application/xml\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -d '<jobRequest>\n    <jobId>admin  JobName 1410786491777</jobId>\n  </jobRequest>'\n```\n\n**Example Response:**\n```\nNORMAL\n```\n\n**Returns:**\nA Response object indicating the status of the scheduler.\n","requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/JobRequest"}},"application/xml":{"schema":{"$ref":"#/components/schemas/JobRequest"}}}},"responses":{"200":{"description":"Job triggered successfully","content":{"text/plain":{"schema":{"type":"string","description":"Status of the scheduler"}}}},"400":{"description":"Invalid input"},"500":{"description":"Invalid jobId"}}}}}}
````
