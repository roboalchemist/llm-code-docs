# Source: https://plivo.com/docs/voice/use-cases/supervisor-coaching.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send SMS Alerts

> Implement supervisor coaching for call center agents using multiparty calls

<Tabs>
  <Tab title="Node">
    ## Overview

    Supervisors in call centers need to coach agents to cultivate an effective team. Coaching involves supervisors listening in on live calls and advising agents without customers’ knowledge. A supervisor can also take over a call and talk to a customer directly. This guide shows how to implement supervisor coaching using Plivo‘s multiparty call (MPC) feature. We’ll look at four tasks:

    * Connecting a customer and an agent
    * Agent adding supervisor to a call
    * Supervisor joining call
    * Supervisor taking over call

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the Numbers API. If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

    ## Connect customer and agent

    Consider the case of a call center where customers call a hotline number to connect with a customer support representative using a web app powered by [Plivo Browser SDK](/voice/client-sdk/). The call flow goes like this:

    1. Customer dials in from the browser app to talk to an agent.
    2. The customer is added to a multiparty call.
    3. The agent is added to the same multiparty call.

    <Frame>
            <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/connect-customer-agent.png?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=f2861d4a19f82fb06d34b9b35f72a6b7" alt="" width="1446" height="774" data-path="images/connect-customer-agent.png" />
    </Frame>

    Here’s what that process looks in Node.js.

    ```js  theme={null}
    var plivo = require('../plivo-node/');
    var express = require('express');
    var bodyParser = require('body-parser');
    var app = express();
    app.set('port', (process.env.PORT || 5000));
    app.use(express.static(__dirname + '/public'));
    app.use(bodyParser.json()); // support json encoded bodies
    app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies

    var musicUrl = "https://s3.amazonaws.com/plivocloud/music.mp3"
    var client = new plivo.Client("<auth_id>","<auth_token>");

    // Add customer to the MPC
    app.all('/add/customer/', function (request, response) {
        var r = new plivo.Response();
        var mpcName = 'test';
        var params = {
            "role": "Customer",
            "statusCallbackUrl": "https://<ngrok_identifier>.ngrok.io/add/agent/",
            "statusCallbackMethod": "POST",
            "waitMusicUrl": musicUrl,
            "waitMusicMethod": "GET",
        };
        r.addMultiPartyCall(mpcName, params);
        console.log(r.toXML());
        response.set({ 'Content-Type': 'text/xml' });
        response.end(r.toXML());
    });

    //Add agent to the MPC to talk to the customer
    app.all('/add/agent/', function (request, response) {
        var mpcEventName = request.query.EventName || request.body.EventName; 
        var mpcMPCUUID = request.query.MPCUUID || request.body.MPCUUID;
        var mpcParticipantCallFrom = request.query.ParticipantCallFrom || request.body.ParticipantCallFrom;
        console.log(mpcEventName);
        if (mpcEventName == 'MPCInitialized') {
            client.multiPartyCalls.addParticipant('Agent', { 'uuid': mpcMPCUUID, 'from': mpcParticipantCallFrom, 'to': 'sip:Testendpoint181116105835@phone.plivo.com', 'status_callback_url': 'https://<ngrok_identifier>.ngrok.io/agent/callback/' })
            console.log(response);
        }
    });

    // Collect status callback events after agent joins the MPC
    app.all('/agent/callback/', function (request, response) {
        var mpcMPCUUID = request.query.MPCUUID;
        console.log(mpcMPCUUID)
    });

    app.listen(app.get('port'), function () {
        console.log('Node app is running on port', app.get('port'));
    });
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home).

    ## Agent adds supervisor to a call

    The previous example was a simple case that involved just a customer and an agent. If the call center wants to provide supervisor coaching, agents can add a supervisor to an ongoing multiparty call like this:

    1. The agent clicks an Add Supervisor button on the dialer web app on which they’re  talking to the customer.
    2. The supervisor is added to the multiparty call using Plivo’s [Add Participant API](/voice/api/multiparty-call/participants/add-a-participant/).
    3. By default, only the agent will be able to hear the supervisor. You can override this by changing the coachMode parameter to `false`.

    <Frame>
            <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/agent-adds-supervisor.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=20920516240f6a10fbc69f2d17aa7cf9" alt="" width="1446" height="774" data-path="images/agent-adds-supervisor.png" />
    </Frame>

    Here’s what that process looks like in Node.js.

    ```js  theme={null}
    var plivo = require('../plivo-node/');
    var express = require('express');
    var bodyParser = require('body-parser');
    var app = express();
    app.set('port', (process.env.PORT || 5000));
    app.use(express.static(__dirname + '/public'));
    app.use(bodyParser.json()); // support json encoded bodies
    app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies

    var musicUrl = "https://s3.amazonaws.com/plivocloud/music.mp3"
    var client = new plivo.Client("<auth_id>","<auth_token>");

    // Add customer to the MPC
    app.all('/add/customer/', function (request, response) {
        ...
        ...
    });

    //Add agent to the MPC to talk to the customer
    app.all('/add/agent/', function (request, response) {
        ...
        ...
    });

    // Collect status callback events after agent joins the MPC
    app.all('/agent/callback/', function (request, response) {
        ...
        ...
    });

    // Agent clicks "Add supervisor to the call" option to add them to the ongoing MPC
    app.all('/add_supervisor/:mpcMPCUUID', function (request, response) {
        var mpcUUID = request.params("mpcMPCUUID");
        client.multiPartyCalls.addParticipant('Supervisor', { 'uuid': mpcUUID, 'from': mpcParticipantCallFrom, 'to': 'sip:Testendpoint181116105835@phone.plivo.com', 'status_callback_url': 'https://<ngrok_identifier>.ngrok.io/supervisor/callback/' })
        console.log(response);
    });

    app.listen(app.get('port'), function () {
        console.log('Node app is running on port', app.get('port'));
    });
    ```

    ## Supervisor joins an ongoing call

    Not all supervisor calls are initiated by agents — supervisors can jump in themselves. Here’s how this process — often called call barging — works:

    1. An agent is talking to a customer on an ongoing multiparty call.
    2. A supervisor, who is monitoring all the live calls on the call center web dashboard, clicks on a Join the Call button next to the longest call in the queue.
    3. The supervisor can then listen to the call and coach the agent.

    <Frame>
            <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/supervisor-joins-call.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=22065bb2c0074ac4851a029240319f35" alt="" width="1446" height="774" data-path="images/supervisor-joins-call.png" />
    </Frame>

    Here’s what that process looks like in Node.js.

    ```js  theme={null}
    var plivo = require('../plivo-node/');
    var express = require('express');
    var bodyParser = require('body-parser');
    var app = express();
    app.set('port', (process.env.PORT || 5000));
    app.use(express.static(__dirname + '/public'));
    app.use(bodyParser.json()); // support json encoded bodies
    app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies

    var musicUrl = "https://s3.amazonaws.com/plivocloud/music.mp3"
    var client = new plivo.Client("<auth_id>","<auth_token>");

    // Add customer to the MPC
    app.all('/add/customer/', function (request, response) {
        ...
        ...
    });

    //Add agent to the MPC to talk to the customer
    app.all('/add/agent/', function (request, response) {
        ...
        ...
    });

    // Collect status callback events after agent joins the MPC
    app.all('/agent/callback/', function (request, response) {
        ...
        ...
    });

    // Agent clicks "Add supervisor to the call" option to add them to the ongoing MPC
    app.all('/add_supervisor/:mpcMPCUUID', function (request, response) {
        ...
        ...
    });

    // Supervisor clicks "Join the call" option to be added to the ongoing MPC
    app.all('/coach_the_agent/', function (request, response) {
        var r = new plivo.Response();
        var mpcName = 'test'; // MPC name of the call to which the supervisor wishes to join; you can get this from status_callback_url
        var params = {
            "role": "Supervisor",
            "coach_mode": True, // The supervisor can talk to only the agent. 
            "status_callback_url": "https://<ngrok_identifier>.ngrok.io/supervisor/callback/",
            "status_callback_method": "POST",
            "enter_sound": "none",
        };
        r.addMultiPartyCall(mpcName, params);
        console.log(r.toXML());
        response.set({ 'Content-Type': 'text/xml' });
        response.end(r.toXML());
    });

    app.listen(app.get('port'), function () {
        console.log('Node app is running on port', app.get('port'));
    });
    ```

    ## Supervisor takes over a call

    Depending on what they hear, sometimes supervisors want to talk to both the customer and the agent. Here’s how that process might go.

    1. An agent is talking to a customer on an ongoing multiparty call.
    2. The supervisor is monitoring all live calls on the call center web dashboard.
    3. The supervisor clicks on the Take Over the Call button of a specific call, and can then take over the call and talk to both the customer and the agent.

    <Frame>
            <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/supervisor-takes-over.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=217fc00263fc5eaa970e3f13aad1e0a3" alt="" width="1446" height="774" data-path="images/supervisor-takes-over.png" />
    </Frame>

    Here’s what that process looks like in Node.js.

    ```js  theme={null}
    var plivo = require('../plivo-node/');
    var express = require('express');
    var bodyParser = require('body-parser');
    var app = express();
    app.set('port', (process.env.PORT || 5000));
    app.use(express.static(__dirname + '/public'));
    app.use(bodyParser.json()); // support json encoded bodies
    app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies

    var musicUrl = "https://s3.amazonaws.com/plivocloud/music.mp3"
    var client = new plivo.Client("<auth_id>","<auth_token>");

    // Add customer to the MPC
    app.all('/add/customer/', function (request, response) {
        ...
        ...
    });

    //Add agent to the MPC to talk to the customer
    app.all('/add/agent/', function (request, response) {
        ...
        ...
    });

    // Collect status callback events after agent joins the MPC
    app.all('/agent/callback/', function (request, response) {
        ...
        ...
    });

    // Agent clicks "Add supervisor to the call" option to add him to the ongoing MPC
    app.all('/add_supervisor/:mpcMPCUUID', function (request, response) {
        ...
        ...
    });

    // Supervisor clicks "Join the call" option to add him to the ongoing MPC
    app.all('/coach_the_agent/', function (request, response) {
        ...
        ...
    });

    // Supervisor clicks "Join the call" option to be added to the ongoing MPC
    app.all('/talk_to_customer/', function (request, response) {
        var r = new plivo.Response();
        var mpcName = 'test'; // MPC name of the call to which the supervisor wishes to join; you can get this from status_callback_url
        var params = {
            "role": "Supervisor",
            "coach_mode": false, // The supervisor can talk to only the agent 
            "status_callback_url": "https://<ngrok_identifier>.ngrok.io/supervisor/callback/",
            "status_callback_method": "POST",
            "enter_sound": "none",
        };
        r.addMultiPartyCall(mpcName, params);
        console.log(r.toXML());
        response.set({ 'Content-Type': 'text/xml' });
        response.end(r.toXML());
    });

    app.listen(app.get('port'), function () {
        console.log('Node app is running on port', app.get('port'));
    });
    ```

    As you can see, Plivo makes it easy to set up and manage multiparty calls. With these capabilities, you can run your own call center, manage call transfers, coach agents, and much more. For more details, see our [Multiparty Call API reference](/voice/api/multiparty-call/) page.
  </Tab>

  <Tab title="Python">
    ## Overview

    Supervisors in call centers need to coach agents to cultivate an effective team. Coaching involves supervisors listening in on live calls and advising agents without customers’ knowledge. A supervisor can also take over a call and talk to a customer directly. This guide shows how to implement supervisor coaching using Plivo‘s multiparty call (MPC) feature. We’ll look at four tasks:

    * Connecting a customer and an agent
    * Agent adding supervisor to a call
    * Supervisor joining call
    * Supervisor taking over call

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the Numbers API. If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

    ## Connect customer and agent

    Consider the case of a call center where customers call a hotline number to connect with a customer support representative using a web app powered by [Plivo Browser SDK](/voice/client-sdk/). The call flow goes like this:

    1. Customer dials in from the browser app to talk to an agent.
    2. The customer is added to a multiparty call.
    3. The agent is added to the same multiparty call.

    <Frame>
            <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/connect-customer-agent.png?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=f2861d4a19f82fb06d34b9b35f72a6b7" alt="" width="1446" height="774" data-path="images/connect-customer-agent.png" />
    </Frame>

    Here’s what that process looks like in Python.

    ```py  theme={null}
    from flask import Flask, Response, request, make_response
    import plivo
    from plivo import plivoxml

    app=Flask(__name__)

    music_url = "https://s3.amazonaws.com/plivocloud/music.mp3"
    client = plivo.RestClient(auth_id="<auth_id>", auth_token="<auth_token>")

    # Add customer to the MPC. You can assign this to the Plivo app of the endpoint mapped to the customer in the browser app
    @app.route("/add/customer/", methods=["GET", "POST"])
    def multipartycall_add_customer():
       mpc_name = "test"
       mpc_params = {
           "content": mpc_name,
           "role": "Customer",
           "status_callback_url": "https://<ngrok_identifier>.ngrok.io/add/agent/",
           "status_callback_method": "POST",
           "wait_music_url": music_url,
           "wait_music_method": "GET",
       }
       mpc_element = plivoxml.MultiPartyCallElement(**mpc_params)
       res = plivoxml.ResponseElement()
       res.add(mpc_element)
       return Response(res.to_string(), mimetype="application/xml")

    # Add agent to the MPC to talk to the customer
    @app.route("/customer/callback/", methods=["GET", "POST"])
    def multipartycall_add_agent():
       mpc_EventName = request.form.get("EventName")
       mpc_MPCUUID = request.form.get("MPCUUID")
       mpc_ParticipantCallFrom = request.form.get("ParticipantCallFrom")
       if mpc_EventName == "MPCInitialized":
           call_params = {
               'role': "Agent",
               'uuid': mpc_MPCUUID,
               'start_mpc_on_enter': True,
               'from_': mpc_ParticipantCallFrom, # Customer number as caller ID
               'to_': "sip:websdk171107061912@phone.plivo.com", #Agent's endpoint username or phone number
               'call_status_callback_url': "https://<ngrok_identifier>.ngrok.io/agent/callback/",
               'call_status_callback_method': 'POST',
               "enter_sound": "none"
           }
           try:
               response = client.multi_party_calls.add_participant(**call_params)
           except Exception as e:
               response = client.multi_party_calls.stop(uuid=mpc_MPCUUID)
       return 'ok'

    if __name__ == "__main__":
        app.run(host="0.0.0.0", debug=True)
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home).

    ## Agent adds supervisor to a call

    1. The previous example was a simple case that involved just a customer and an agent. If the call center wants to provide supervisor coaching, agents can add a supervisor to an ongoing multiparty call like this:

       1. The agent clicks an Add Supervisor button on the dialer web app on which they’re  talking to the customer.
       2. The supervisor is added to the multiparty call using Plivo’s [Add Participant API](/voice/api/multiparty-call/participants/add-a-participant/).
       3. By default, only the agent will be able to hear the supervisor. You can override this by changing the coachMode parameter to `false`.

    <Frame>
            <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/agent-adds-supervisor.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=20920516240f6a10fbc69f2d17aa7cf9" alt="" width="1446" height="774" data-path="images/agent-adds-supervisor.png" />
    </Frame>

    Here’s what that process looks like in Python.

    ```py  theme={null}
    from flask import Flask, Response, request, make_response
    import plivo
    from plivo import plivoxml

    app=Flask(__name__)

    music_url = "https://s3.amazonaws.com/plivocloud/music.mp3"
    client = plivo.RestClient(auth_id="<auth_id>", auth_token="<auth_token>")

    @app.route("/mpc/customer/", methods=["GET", "POST"])
    def multipartycall_customer():
      ....
      ....

    # Add agent to the MPC to talk to the customer
    @app.route("/customer/callback/", methods=["GET", "POST"])
    def multipartycall_agent():
       ....
       ....

    # Agent clicks "Add supervisor to the call" option to add them to the ongoing MPC
    @app.route("/add_supervisor/<mpc_MPCUUID>", methods=["GET", "POST"])
    def add_supervisor(mpc_MPCUUID):   
       call_params = {
           'role': "Supervisor",
           'uuid': mpc_MPCUUID, # you can get this from status_callback_url
           'dial_music': 'None',
           'from_': "<caller_id>", # Agent number as caller ID; you can get this from status_callback_url
           'to_': "sip:browsersdkdemo438313651789286059@phone.plivo.com", #Supervisor Phone number goes here
           'call_status_callback_url': "https://<ngrok_identifier>.ngrok.io/supervisor/callback/",
           'call_status_callback_method': 'POST',
       }
       response = client.multi_party_calls.add_participant(**call_params)
       return str(response)

    if __name__ == "__main__":
        app.run(host="0.0.0.0", debug=True)
    ```

    ## Supervisor joins an ongoing call

    Not all supervisor calls are initiated by agents — supervisors can jump in themselves. Here’s how this process — often called call barging — works:

    1. An agent is talking to a customer on an ongoing multiparty call.
    2. A supervisor, who is monitoring all the live calls on the call center web dashboard, clicks on a Join the Call button next to the longest call in the queue.
    3. The supervisor can then listen to the call and coach the agent.

    <Frame>
            <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/supervisor-joins-call.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=22065bb2c0074ac4851a029240319f35" alt="" width="1446" height="774" data-path="images/supervisor-joins-call.png" />
    </Frame>

    Here’s what that process looks like in Python.

    ```py  theme={null}
    from flask import Flask, Response, request, make_response
    import plivo
    from plivo import plivoxml

    app=Flask(__name__)

    music_url = "https://s3.amazonaws.com/plivocloud/music.mp3"
    client = plivo.RestClient(auth_id="<auth_id>", auth_token="<auth_token>")

    @app.route("/mpc/customer/", methods=["GET", "POST"])
    def multipartycall_customer():
        ....
        ....

    # Add agent to the MPC to talk to the customer
    @app.route("/customer/callback/", methods=["GET", "POST"])
    def multipartycall_agent():
        ....
        ....

    # Agent clicks "Add supervisor to the call" option to add them to the ongoing MPC
    @app.route("/add_supervisor/", methods=["GET", "POST"])
    def add_supervisor():    
        ....
        ....

    # Supervisor clicks "Join the call" option to be added to the ongoing MPC
    @app.route("/coach_the_agent/<mpc_MPCUUID>", methods=["GET", "POST"])
    def join_specific_mpc(mpc_MPCUUID):   
       mpc_name = "test" # MPC name of the call to which the supervisor wishes to join; you can get this from status_callback_url
       mpc_params = {
           "content": mpc_name,
           "role": "Supervisor",
           "coach_mode": True, # The supervisor can talk to only the agent.
           "status_callback_url": "https://<ngrok_identifier>.ngrok.io/supervisor/callback/",
           "status_callback_method": "POST",
           "enter_sound": "none",
       }
       mpc_element = plivoxml.MultiPartyCallElement(**mpc_params)
       res = plivoxml.ResponseElement()
       res.add(mpc_element)
       return Response(res.to_string(), mimetype="application/xml")

    if __name__ == "__main__":
        app.run(host="0.0.0.0", debug=True)
    ```

    ## Supervisor takes over a call

    Depending on what they hear, sometimes supervisors want to talk to both the customer and the agent. Here’s how that process might go.

    1. An agent is talking to a customer on an ongoing multiparty call.
    2. The supervisor is monitoring all live calls on the call center web dashboard.
    3. The supervisor clicks on the Take Over the Call button of a specific call, and can then take over the call and talk to both the customer and the agent.

    <Frame>
            <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/supervisor-takes-over.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=217fc00263fc5eaa970e3f13aad1e0a3" alt="" width="1446" height="774" data-path="images/supervisor-takes-over.png" />
    </Frame>

    Here’s what that process looks like in Python.

    ```py  theme={null}
    from flask import Flask, Response, request, make_response
    import plivo
    from plivo import plivoxml

    app=Flask(__name__)

    music_url = "https://s3.amazonaws.com/plivocloud/music.mp3"
    client = plivo.RestClient(auth_id="<auth_id>", auth_token="<auth_token>")

    @app.route("/mpc/customer/", methods=["GET", "POST"])
    def multipartycall_customer():
        ....
        ....

    # Add agent to the MPC to talk to the customer
    @app.route("/customer/callback/", methods=["GET", "POST"])
    def multipartycall_agent():
        ....
        ....

    # Agent clicks "Add supervisor to the call" option to add them to the ongoing MPC
    @app.route("/add_supervisor/", methods=["GET", "POST"])
    def add_supervisor():    
        ....
        ....

    # Supervisor clicks "Join the call" option to be added to the ongoing MPC
    @app.route("/coach_the_agent/", methods=["GET", "POST"])
    def join_specific_mpc():    
        ....
        ....

    # Supervisor clicks "Take over the call" option to be added to the ongoing MPC
    @app.route("/talk_to_customer/", methods=["GET", "POST"])
    def talk_to_customer():   
       mpc_name = "test" # MPC name of the call to which the supervisor wishes to join; you can get this from status_callback_url
       mpc_params = {
           "content": mpc_name,
           "role": "Supervisor",
           "coach_mode": false, # The supervisor can talk to only the agent
           "status_callback_url": "https://<ngrok_identifier>.ngrok.io/supervisor/callback/",
           "status_callback_method": "POST",
           "enter_sound": "none",
       }
       mpc_element = plivoxml.MultiPartyCallElement(**mpc_params)
       res = plivoxml.ResponseElement()
       res.add(mpc_element)
       return Response(res.to_string(), mimetype="application/xml")

    if __name__ == "__main__":
       app.run(host="0.0.0.0", debug=True)
    ```

    As you can see, Plivo makes it easy to set up and manage multiparty calls. With these capabilities, you can run your own call center, manage call transfers, coach agents, and much more. For more details, see our [Multiparty Call API reference](/voice/api/multiparty-call/) page.
  </Tab>
</Tabs>
