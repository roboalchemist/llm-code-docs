# Source: https://docs.avaamo.com/user-guide/tutorials-and-exercises/part-1-creating-my-agent/chapter-5-building-a-dialog-skill/exercise-5.4-adding-a-javascript.md

# Exercise 5.4: Adding a JavaScript

Let us add the javascript that will create the incident

You can add the following code to your code block:

```javascript
var SERVICE_NOW_INSTANCE_ID = "66374";
var SERVICE_NOW_URL = "https://dev"+SERVICE_NOW_INSTANCE_ID+".service-now.com/api/now/";
var SERVICE_NOW_USERID = "admin";
var SERVICE_NOW_PWD = "qPoOh5VfCsV5";
let SERVICE_NOW_CALLER = "2def7d7edb3d330082fb6a49489619c0";

function createNewIncident(description,urgency,sht_desc) {
  let caller = SERVICE_NOW_CALLER;  
  let url = SERVICE_NOW_URL+'table/incident'
  return await(fetch(url, {
    method: 'POST',
    headers: {
      "Content-Type": "application/json",
      'Authorization': 'Basic '+Buffer.from(SERVICE_NOW_USERID+':'+SERVICE_NOW_PWD).toString('base64')
    },
    body: JSON.stringify({
      "short_description": sht_desc,
   "caller_id": caller,
   "description": description,
      "severity": 8,
      "impact": 9,
      "urgency":urgency
    })
  }).then(function(response) {
    return response.json();
  })
  .then(function(apiJson) {
    console.log(apiJson.result);
    return apiJson.result.number;
  }));
}


let shortDescription = context.variables.short_description
let description = context.variables.description
let urgency = context.variables.urgency

var incidentNumber = createNewIncident(shortDescription, description, urgency);
if(incidentNumber){ 
 return ("Ticket "+incidentNumber+" has been created on your behalf.");
}
else{
 return "Unable to create a ticket at the moment. Please try again later.";
}
```

Once the code has been written, save your changes to the skill and build the agent. Let us test the skill to see how it responds.<br>
