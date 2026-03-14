# Source: https://plivo.com/docs/voice/use-cases/voice-broadcasting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Voice Alerts/Notifications Broadcasting

> Broadcast voice messages to multiple recipients at once

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to broadcast voice messages to multiple recipients at once. You can play recorded audio when the call recipient answers or use text-to-speech, as we show here.

    You can use voice broadcasting for use cases such as:

    * Bulk voice calling campaigns
    * Emergency notifications
    * Survey campaigns
    * User feedback
    * Announcements
    * Promotions and special deals
    * Reminder campaigns

    You can broadcast voice alerts either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to broadcast voice alerts and notifications with a few clicks on the PHLO canvas and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Node.js, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/).

        ## Create the PHLO

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/broadcasting.gif?s=47fe14c58bb267101db704bb789854f7" alt="" width="1024" height="545" data-path="images/broadcasting.gif" />
        </Frame>

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * Click the **Start** node to open the Configuration tab to the right of the canvas, then enter the information to retrieve from the HTTP Request payload — in this case, from and to numbers.

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. This adds an **Initiate Call** node onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.

        * In the Configuration tab of the **Initiate Call** node, give the node a meaningful name. You can rename nodes as you like to improve your PHLO's readability. Enter a phone number in the From field that will serve as the caller ID, and enter as many numbers as you‘d like to call in the To field.

        * Validate the configuration by clicking **Validate**. Every time you finish configuring a node, click **Validate** to check the syntax and save your changes.

        * Drag and drop the **Play Audio** component onto the canvas. Draw a line to connect the **Answered** trigger state of the **Initiate Call** node to the Play Audio node.

        * In the Configuration tab of the **Play Audio** node, in the Speak Text box, enter a message to play to call recipients using text-to-speech.

        * Draw a line to connect the **Answered** trigger state of the **Initiate Call** node to the **Play Audio** node.

        * After you complete and validate all the node configurations, give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        ### With static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

        Create a file called `TriggerPhlo.js` and paste into it this code.

        ```js  theme={null}
        var plivo = require('plivo');
        var PhloClient = plivo.PhloClient;

        var authId = '<auth_id>';
        var authToken = '<auth_token>';
        var phloId = '<phlo_id>';
        var phloClient = phlo = null;

        phloClient = new PhloClient(authId, authToken);
        phloClient.phlo(phloId).run().then(function (result) {
            console.log('Phlo run result', result);
        }).catch(function (err) {
            console.error('Phlo run failed', err);
        });
        ```

        ### With dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code to the PHLO when you trigger it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        #### Code

        Create a file called `TriggerPhlo.js` and paste into it this code.

        ```js  theme={null}
        var plivo = require('plivo');
        var PhloClient = plivo.PhloClient;

        var authId = '<auth_id>';
        var authToken = '<auth_token>';
        var phloId = '<phlo_id>';
        var phloClient = phlo = null;

        var payload = {
            from: '<caller_id>',
        		dest1:   '<destination_number1>',
        		dest2:   '<destination_number2>',
        		dest3:   '<destination_number3>',
        		dest4:   '<destination_number4>',
        		dest5:   '<destination_number5>'
        }
        phloClient = new PhloClient(authId, authToken);
        phloClient.phlo(phloId).run(payload).then(function (result) {
            console.log('Phlo run result', result);
        }).catch(function (err) {
            console.error('Phlo run failed', err);
        });
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        node TriggerPhlo.js
        ```
      </Tab>

      <Tab title="Using XML">
        Here’s how to broadcast voice alerts and notifications using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. To see how this works, you can use [https://s3.amazonaws.com/static.plivo.com/broadcast.xml](https://s3.amazonaws.com/static.plivo.com/broadcast.xml) as an answer URL to test your first outgoing call. The file contains this XML code:

        ```xml  theme={null}
        <Response>
        <Speak>Congratulations! You have made your first bulk call.</Speak>
        </Response>
        ```

        This code instructs Plivo to say, “Congratulations! You have made your first bulk call” to the call recipients. You can find the entire list of valid Plivo XML verbs in our [XML Reference](/voice/xml/overview/) documentation.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create voice alert broadcast application

        Create a file called `Broadcast.js` and paste into it this code.

        ```js  theme={null}
        var plivo = require('plivo');

        (function main() {
            'use strict';

            var client = new plivo.Client("<auth_id>","<auth_token>");
            client.calls.create(
                "<caller_id>", // from
                "destination_number1<destination_number2", // to
                "https://s3.amazonaws.com/static.plivo.com/broadcast.xml", // answer url
                {
                    answerMethod: "GET",
                },
            ).then(function (response) {
                console.log(response);
            }, function (err) {
                console.error(err);
            });
        })();
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). Destination numbers may also be SIP endpoints, in which case each destination\_number placeholder must be a valid SIP URI — for example, sip:[john1234@phone.plivo.com](mailto:john1234@phone.plivo.com).

        <Note>
          <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables, so as to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and it will automatically fetch them from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
        </Note>

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        node Broadcast.js
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to broadcast voice messages to multiple recipients at once. You can play recorded audio when the call recipient answers or use text-to-speech, as we show here.

    You can use voice broadcasting for use cases such as:

    * Bulk voice calling campaigns
    * Emergency notifications
    * Survey campaigns
    * User feedback
    * Announcements
    * Promotions and special deals
    * Reminder campaigns

    You can broadcast voice alerts either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to broadcast voice alerts and notifications with a few clicks on the PHLO canvas and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Node.js, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/).

        ## Create the PHLO

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/broadcasting.gif?s=47fe14c58bb267101db704bb789854f7" alt="" width="1024" height="545" data-path="images/broadcasting.gif" />
        </Frame>

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * Click the **Start** node to open the Configuration tab to the right of the canvas, then enter the information to retrieve from the HTTP Request payload — in this case, from and to numbers.

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. This adds an **Initiate Call** node onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.

        * In the Configuration tab of the **Initiate Call** node, give the node a meaningful name. You can rename nodes as you like to improve your PHLO's readability. Enter a phone number in the From field that will serve as the caller ID, and enter as many numbers as you‘d like to call in the To field.

        * Validate the configuration by clicking **Validate**. Every time you finish configuring a node, click **Validate** to check the syntax and save your changes.

        * Drag and drop the **Play Audio** component onto the canvas. Draw a line to connect the **Answered** trigger state of the **Initiate Call** node to the Play Audio node.

        * In the Configuration tab of the **Play Audio** node, in the Speak Text box, enter a message to play to call recipients using text-to-speech.

        * Draw a line to connect the **Answered** trigger state of the **Initiate Call** node to the **Play Audio** node.

        * After you complete and validate all the node configurations, give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        ### With static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

        Create a file called `trigger_phlo.rb` and paste into it this code.

        ```ruby  theme={null}
        require 'rubygems'
        require 'plivo'

        include Plivo

        AUTH_ID = '<auth_id>'
        AUTH_TOKEN = '<auth_token>'

        client = Phlo.new(AUTH_ID, AUTH_TOKEN)

        # if credentials are stored in the PLIVO_AUTH_ID and the PLIVO_AUTH_TOKEN environment variables
        # then initialize client as:
        # client = Phlo.new

        begin
          phlo = client.phlo.get('<phlo_id>')
          response = phlo.run()
          puts response
        rescue PlivoRESTError => e
          puts 'Exception: ' + e.message
        end
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents).

        ### With dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code to the PHLO when you trigger it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        #### Code

        Create a file called `trigger_phlo.rb` and paste into it this code.

        ```ruby  theme={null}
        require 'rubygems'
        require 'plivo'

        include Plivo

        AUTH_ID = '<auth_id>'
        AUTH_TOKEN = '<auth_token>'

        client = Phlo.new(AUTH_ID, AUTH_TOKEN)

        # if credentials are stored in the PLIVO_AUTH_ID and the PLIVO_AUTH_TOKEN environment variables
        # then initialize client as:
        # client = Phlo.new

        begin
          phlo = client.phlo.get('<phlo_id>')
          #parameters set in PHLO - params
          params = {
             from: '<caller_id>',
             dest1:   '<destination_number1>',
             dest2:   '<destination_number2>',
             dest3:   '<destination_number3>',
             dest4:   '<destination_number4>',
             dest5:   '<destination_number5>'
          }
          response = phlo.run(params)
          puts response
        rescue PlivoRESTError => e
          puts 'Exception: ' + e.message
        end
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        ruby trigger_phlo.rb
        ```
      </Tab>

      <Tab title="Using XML">
        Here’s how to broadcast voice alerts and notifications using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. To see how this works, you can use [https://s3.amazonaws.com/static.plivo.com/broadcast.xml](https://s3.amazonaws.com/static.plivo.com/broadcast.xml) as an answer URL to test your first outgoing call. The file contains this XML code:

        ```xml  theme={null}
        <Response>
        <Speak>Congratulations! You have made your first bulk call.</Speak>
        </Response>
        ```

        This code instructs Plivo to say, “Congratulations!  You have made your first bulk call” to the call recipients. You can find the entire list of valid Plivo XML verbs in our [XML Reference](/voice/xml/overview/) documentation.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create voice alert broadcast application

        Create a file called `broadcast.rb` and paste into it this code.

        ```ruby  theme={null}
        require 'rubygems'
        require 'plivo'

        include Plivo
        include Plivo::Exceptions

        api = RestClient.new("<auth_id>","<auth_token>")

        begin
          response = api.calls.create(
            '<caller_id>',
            ['<destination_number1>', '<destination_number2>'],
            'https://s3.amazonaws.com/static.plivo.com/broadcast.xml'
          )
          puts response
        rescue PlivoRESTError => e
          puts 'Exception: ' + e.message
        end
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). Destination numbers may also be SIP endpoints, in which case each destination\_number placeholder must be a valid SIP URI — for example, sip:[john1234@phone.plivo.com](mailto:john1234@phone.plivo.com).

        <Note>
          <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables, so as to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and it will automatically fetch them from the environment variables. You can use `ENV` to store environment variables and fetch them when initializing the client.
        </Note>

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        ruby broadcast.rb
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to broadcast voice messages to multiple recipients at once. You can play recorded audio when the call recipient answers or use text-to-speech, as we show here.

    You can use voice broadcasting for use cases such as:

    * Bulk voice calling campaigns
    * Emergency notifications
    * Survey campaigns
    * User feedback
    * Announcements
    * Promotions and special deals
    * Reminder campaigns

    You can broadcast voice alerts either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to broadcast voice alerts and notifications with a few clicks on the PHLO canvas and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Node.js, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/).

        ## Create the PHLO

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/broadcasting.gif?s=47fe14c58bb267101db704bb789854f7" alt="" width="1024" height="545" data-path="images/broadcasting.gif" />
        </Frame>

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * Click the **Start** node to open the Configuration tab to the right of the canvas, then enter the information to retrieve from the HTTP Request payload — in this case, from and to numbers.

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. This adds an **Initiate Call** node onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.

        * In the Configuration tab of the **Initiate Call** node, give the node a meaningful name. You can rename nodes as you like to improve your PHLO's readability. Enter a phone number in the From field that will serve as the caller ID, and enter as many numbers as you‘d like to call in the To field.

        * Validate the configuration by clicking **Validate**. Every time you finish configuring a node, click **Validate** to check the syntax and save your changes.

        * Drag and drop the **Play Audio** component onto the canvas. Draw a line to connect the **Answered** trigger state of the **Initiate Call** node to the Play Audio node.

        * In the Configuration tab of the **Play Audio** node, in the Speak Text box, enter a message to play to call recipients using text-to-speech.

        * Draw a line to connect the **Answered** trigger state of the **Initiate Call** node to the **Play Audio** node.

        * After you complete and validate all the node configurations, give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        ### With static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

        Create a file called `trigger_phlo.py` and paste into it this code.

        ```py  theme={null}
        import plivo

        auth_id = '<auth_id>'
        auth_token = '<auth_token>'
        phlo_id = '<phlo_id>'
        payload = {"from": "<caller_id>", "dest1":   "<destination_number1>", "dest2":   "<destination_number2>", "dest3":   "<destination_number3>", "dest4":   "<destination_number4>", "dest5":   "<destination_number5>"}
        phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
        phlo = phlo_client.phlo.get(phlo_id)
        response = phlo.run(**payload)
        print str(response)
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents).

        ### With dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code to the PHLO when you trigger it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        #### Code

        Create a file called `trigger_phlo.py` and paste into it this code.

        ```py  theme={null}
        import plivo

        auth_id = '<auth_id>'
        auth_token = '<auth_token>'
        phlo_id = '<phlo_id>'
        payload = {"from": "<caller_id>", "dest1":   "<destination_number1>", "dest2":   "<destination_number2>", "dest3":   "<destination_number3>", "dest4":   "<destination_number4>", "dest5":   "<destination_number5>"}
        phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
        phlo = phlo_client.phlo.get(phlo_id)
        response = phlo.run(**payload)
        print str(response)
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        python trigger_phlo.py
        ```
      </Tab>

      <Tab title="Using XML">
        Here’s how to broadcast voice alerts and notifications using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. To see how this works, you can use [https://s3.amazonaws.com/static.plivo.com/broadcast.xml](https://s3.amazonaws.com/static.plivo.com/broadcast.xml) as an answer URL to test your first outgoing call. The file contains this XML code:

        ```xml  theme={null}
        <Response>
        <Speak>Congratulations! You have made your first bulk call.</Speak>
        </Response>
        ```

        This code instructs Plivo to say, “Congratulations!  You have made your first bulk call” to the call recipients. You can find the entire list of valid Plivo XML verbs in our [XML Reference](/voice/xml/overview/) documentation.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create voice alert broadcast application

        Create a file called `broadcast.py` and paste into it this code.

        ```py  theme={null}
        import plivo

        client = plivo.RestClient('<auth_id>','<auth_token>')
        response = client.calls.create(
            from='<caller_id>',
            to='destination_number1<destination_number2',
            answer_url='https://s3.amazonaws.com/static.plivo.com/broadcast.xml',
            answer_method='GET', )
        print(response)
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). Destination numbers may also be SIP endpoints, in which case each destination\_number placeholder must be a valid SIP URI — for example, sip:[john1234@phone.plivo.com](mailto:john1234@phone.plivo.com).

        <Note>
          <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables, so as to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and it will automatically fetch them from the environment variables. You can use `os module(os.environ)` to store environment variables and fetch them when initializing the client.
        </Note>

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        python broadcast.py
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to broadcast voice messages to multiple recipients at once. You can play recorded audio when the call recipient answers or use text-to-speech, as we show here.

    You can use voice broadcasting for use cases such as:

    * Bulk voice calling campaigns
    * Emergency notifications
    * Survey campaigns
    * User feedback
    * Announcements
    * Promotions and special deals
    * Reminder campaigns

    You can broadcast voice alerts either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to broadcast voice alerts and notifications with a few clicks on the PHLO canvas and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Node.js, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/).

        ## Create the PHLO

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/broadcasting.gif?s=47fe14c58bb267101db704bb789854f7" alt="" width="1024" height="545" data-path="images/broadcasting.gif" />
        </Frame>

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * Click the **Start** node to open the Configuration tab to the right of the canvas, then enter the information to retrieve from the HTTP Request payload — in this case, from and to numbers.

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. This adds an **Initiate Call** node onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.

        * In the Configuration tab of the **Initiate Call** node, give the node a meaningful name. You can rename nodes as you like to improve your PHLO's readability. Enter a phone number in the From field that will serve as the caller ID, and enter as many numbers as you‘d like to call in the To field.

        * Validate the configuration by clicking **Validate**. Every time you finish configuring a node, click **Validate** to check the syntax and save your changes.

        * Drag and drop the **Play Audio** component onto the canvas. Draw a line to connect the **Answered** trigger state of the **Initiate Call** node to the Play Audio node.

        * In the Configuration tab of the **Play Audio** node, in the Speak Text box, enter a message to play to call recipients using text-to-speech.

        * Draw a line to connect the **Answered** trigger state of the **Initiate Call** node to the **Play Audio** node.

        * After you complete and validate all the node configurations, give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        ### With static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

        Create a file called `trigger_phlo.php` and paste into it this code.

        ```php  theme={null}
        <?php
        require 'vendor/autoload.php';
        use Plivo\Resources\PHLO\PhloRestClient;
        use Plivo\Exceptions\PlivoRestException;
        $client = new PhloRestClient("<auth_id>", "<auth_token>");

        $phlo = $client->phlo->get("<phlo_id>");
        try {
            $response = $phlo->run();
            print_r($response);
        } catch (PlivoRestException $ex) {
            print_r($ex);
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents).

        ### With dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code to the PHLO when you trigger it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        #### Code

        Create a file called `trigger_phlo.php` and paste into it this code.

        ```php  theme={null}
        import plivo

        auth_id = '<auth_id>'
        auth_token = '<auth_token>'
        phlo_id = '<phlo_id>'
        payload = {"from": "<caller_id>", "dest1":   "<destination_number1>", "dest2":   "<destination_number2>", "dest3":   "<destination_number3>", "dest4":   "<destination_number4>", "dest5":   "<destination_number5>"}
        phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
        phlo = phlo_client.phlo.get(phlo_id)
        response = phlo.run(**payload)
        print str(response)
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        php TriggerPhlo.php
        ```
      </Tab>

      <Tab title="Using XML">
        Here’s how to broadcast voice alerts and notifications using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. To see how this works, you can use [https://s3.amazonaws.com/static.plivo.com/broadcast.xml](https://s3.amazonaws.com/static.plivo.com/broadcast.xml) as an answer URL to test your first outgoing call. The file contains this XML code:

        ```xml  theme={null}
        <Response>
        <Speak>Congratulations! You have made your first bulk call.</Speak>
        </Response>
        ```

        This code instructs Plivo to say, “Congratulations!  You have made your first bulk call” to the call recipients. You can find the entire list of valid Plivo XML verbs in our [XML Reference](/voice/xml/overview/) documentation.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create voice alert broadcast application

        Create a file called `broadcast.py` and paste into it this code.

        ```php  theme={null}
        import plivo

        client = plivo.RestClient('<auth_id>','<auth_token>')
        response = client.calls.create(
            from='<caller_id>',
            to='destination_number1<destination_number2',
            answer_url='https://s3.amazonaws.com/static.plivo.com/broadcast.xml',
            answer_method='GET', )
        print(response)
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). Destination numbers may also be SIP endpoints, in which case each destination\_number placeholder must be a valid SIP URI — for example, sip:[john1234@phone.plivo.com](mailto:john1234@phone.plivo.com).

        <Note>
          <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables, so as to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and it will automatically fetch them from the environment variables. You can use `$_ENV` or `putenv/getenv` to store environment variables and fetch them when initializing the client.
        </Note>

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        php Broadcast.php
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to broadcast voice messages to multiple recipients at once. You can play recorded audio when the call recipient answers or use text-to-speech, as we show here.

    You can use voice broadcasting for use cases such as:

    * Bulk voice calling campaigns
    * Emergency notifications
    * Survey campaigns
    * User feedback
    * Announcements
    * Promotions and special deals
    * Reminder campaigns

    You can broadcast voice alerts either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to broadcast voice alerts and notifications with a few clicks on the PHLO canvas and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Node.js, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/).

        ## Create the PHLO

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/broadcasting.gif?s=47fe14c58bb267101db704bb789854f7" alt="" width="1024" height="545" data-path="images/broadcasting.gif" />
        </Frame>

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * Click the **Start** node to open the Configuration tab to the right of the canvas, then enter the information to retrieve from the HTTP Request payload — in this case, from and to numbers.

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. This adds an **Initiate Call** node onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.

        * In the Configuration tab of the **Initiate Call** node, give the node a meaningful name. You can rename nodes as you like to improve your PHLO's readability. Enter a phone number in the From field that will serve as the caller ID, and enter as many numbers as you‘d like to call in the To field.

        * Validate the configuration by clicking **Validate**. Every time you finish configuring a node, click **Validate** to check the syntax and save your changes.

        * Drag and drop the **Play Audio** component onto the canvas. Draw a line to connect the **Answered** trigger state of the **Initiate Call** node to the Play Audio node.

        * In the Configuration tab of the **Play Audio** node, in the Speak Text box, enter a message to play to call recipients using text-to-speech.

        * Draw a line to connect the **Answered** trigger state of the **Initiate Call** node to the **Play Audio** node.

        * After you complete and validate all the node configurations, give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        ### With static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

        Open the file in the CS project called `Program.cs` and paste into it this code.

        ```cs  theme={null}
        using System;
        using Plivo;

        namespace test_PHLO
        {
            class Program
            {
                public static void Main(string[] args)
                {
                    var phloClient = new PhloApi("<auth_id>", "<auth_token>");
                    var phloID = "<phlo_id>";
                    var phlo = phloClient.Phlo.Get(phloID);
                    Console.WriteLine(phlo.Run());
                }
            }
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents).

        ### With dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code to the PHLO when you trigger it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        #### Code

        Open the file in the CS project called `Program.cs` and paste into it this code.

        ```cs  theme={null}
        using System;
        using System.Collections.Generic;
        using Plivo;

        namespace test_PHLO
        {
            class Program
            {
                public static void Main(string[] args)
                {
                    var phloClient = new PhloApi("<auth_id>", "<auth_token>");
                    var phloID = "<phlo_id>";
                    var phlo = phloClient.Phlo.Get(phloID);
                    var data = new Dictionary<string, object>
                    {
                        { "from", "<caller_id>" },
                        { "dest1", "<destination_number1>" },
                        { "dest2", "<destination_number2>" }
                        { "dest3", "<destination_number3>" },
                        { "dest4", "<destination_number4>" },
                        { "dest5", "<destination_number5>" },
                    };
                    Console.WriteLine(phlo.Run(data));
                }
            }
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.
      </Tab>

      <Tab title="Using XML">
        Here’s how to broadcast voice alerts and notifications using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. To see how this works, you can use [https://s3.amazonaws.com/static.plivo.com/broadcast.xml](https://s3.amazonaws.com/static.plivo.com/broadcast.xml) as an answer URL to test your first outgoing call. The file contains this XML code:

        ```xml  theme={null}
        <Response>
        <Speak>Congratulations! You have made your first bulk call.</Speak>
        </Response>
        ```

        This code instructs Plivo to say, “Congratulations!  You have made your first bulk call” to the call recipients. You can find the entire list of valid Plivo XML verbs in our [XML Reference](/voice/xml/overview/) documentation.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create voice alert broadcast application

        In Visual Studio, open the file in the CS project called `Program.cs` and paste into it this code.

        ```cs  theme={null}
        using System;
        using System.Collections.Generic;
        using Plivo;

        namespace testplivo
        {
            class Program
            {
                static void Main(string[] args)
                {
                    var api = new PlivoApi("<auth_id>","<auth_token>");
                    var response = api.Call.Create(
                        to: new List<String> { "<destination_number1>", "<destination_number2>" },
                        from: "<caller_id>",
                        answerMethod: "GET",
                        answerUrl: "https://s3.amazonaws.com/static.plivo.com/broadcast.xml"
                    );
                    Console.WriteLine(response);
                }
            }
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). Destination numbers may also be SIP endpoints, in which case each destination\_number placeholder must be a valid SIP URI — for example, sip:[john1234@phone.plivo.com](mailto:john1234@phone.plivo.com).

        <Note>
          <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables, so as to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and it will automatically fetch them from the environment variables. You can use [Environment.SetEnvironmentVariable Method](https://docs.microsoft.com/en-us/dotnet/api/system.environment.setenvironmentvariable?view=netcore-3.1) to store environment variables and [Environment.GetEnvironmentVariable Method](https://docs.microsoft.com/en-us/dotnet/api/system.environment.getenvironmentvariable?view=netcore-3.1) to fetch them when initializing the client.
        </Note>

        ## Test

        Save the file and run it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/build_app.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=57ed7d2310aa904fb31a34ad205f863c" alt="" width="1116" height="444" data-path="images/build_app.jpg" />
        </Frame>
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to broadcast voice messages to multiple recipients at once. You can play recorded audio when the call recipient answers or use text-to-speech, as we show here.

    You can use voice broadcasting for use cases such as:

    * Bulk voice calling campaigns
    * Emergency notifications
    * Survey campaigns
    * User feedback
    * Announcements
    * Promotions and special deals
    * Reminder campaigns

    You can broadcast voice alerts either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to broadcast voice alerts and notifications with a few clicks on the PHLO canvas and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Node.js, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/).

        ## Create the PHLO

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/broadcasting.gif?s=47fe14c58bb267101db704bb789854f7" alt="" width="1024" height="545" data-path="images/broadcasting.gif" />
        </Frame>

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * Click the **Start** node to open the Configuration tab to the right of the canvas, then enter the information to retrieve from the HTTP Request payload — in this case, from and to numbers.

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. This adds an **Initiate Call** node onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.

        * In the Configuration tab of the **Initiate Call** node, give the node a meaningful name. You can rename nodes as you like to improve your PHLO's readability. Enter a phone number in the From field that will serve as the caller ID, and enter as many numbers as you‘d like to call in the To field.

        * Validate the configuration by clicking **Validate**. Every time you finish configuring a node, click **Validate** to check the syntax and save your changes.

        * Drag and drop the **Play Audio** component onto the canvas. Draw a line to connect the **Answered** trigger state of the **Initiate Call** node to the Play Audio node.

        * In the Configuration tab of the **Play Audio** node, in the Speak Text box, enter a message to play to call recipients using text-to-speech.

        * Draw a line to connect the **Answered** trigger state of the **Initiate Call** node to the **Play Audio** node.

        * After you complete and validate all the node configurations, give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        ### With static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

        Create a Java class in the project called `TriggerPhlo` and paste into it this code.

        ```java  theme={null}
        <?php
        import com.plivo.api.Plivo;
        import com.plivo.api.PlivoClient;
        import com.plivo.api.exceptions.PlivoRestException;
        import com.plivo.api.models.phlo.Phlo;
        import java.io.IOException;

        public class Example
        {
            private static final String authId = "<auth_id>";
            private static final String authToken = "<auth_token>";
            private static PlivoClient client = new PlivoClient(authId, authToken);
            public static void main(String[] args) throws IOException, PlivoRestException
            {
                String phloId = "<phlo_id>";
                Plivo.init(authId, authToken);
                Phlo phlo = Phlo.getter(phloId).client(client).get();
                PhloUpdateResponse response = Phlo.updater(phloId).payload().run();
            }
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents).

        ### With dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code to the PHLO when you trigger it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        #### Code

        Create a Java class in the project called `TriggerPhlo` and paste into it this code.

        ```java  theme={null}
        import plivo

        auth_id = '<auth_id>'
        auth_token = '<auth_token>'
        phlo_id = '<phlo_id>'
        payload = {"from": "<caller_id>", "dest1":   "<destination_number1>", "dest2":   "<destination_number2>", "dest3":   "<destination_number3>", "dest4":   "<destination_number4>", "dest5":   "<destination_number5>"}
        phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
        phlo = phlo_client.phlo.get(phlo_id)
        response = phlo.run(**payload)
        print str(response)
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.
      </Tab>

      <Tab title="Using XML">
        Here’s how to broadcast voice alerts and notifications using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. To see how this works, you can use [https://s3.amazonaws.com/static.plivo.com/broadcast.xml](https://s3.amazonaws.com/static.plivo.com/broadcast.xml) as an answer URL to test your first outgoing call. The file contains this XML code:

        ```xml  theme={null}
        <Response>
        <Speak>Congratulations! You have made your first bulk call.</Speak>
        </Response>
        ```

        This code instructs Plivo to say, “Congratulations!  You have made your first bulk call” to the call recipients. You can find the entire list of valid Plivo XML verbs in our [XML Reference](/voice/xml/overview/) documentation.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create voice alert broadcast application

        Create a Java class in the project called `Broadcast` and paste into it this code.

        ```java  theme={null}
        import java.io.IOException;
        import java.util.Collections;
        import com.plivo.api.Plivo;
        import com.plivo.api.exceptions.PlivoRestException;
        import com.plivo.api.models.call.Call;
        import com.plivo.api.models.call.CallCreateResponse;

        class MakeCall {
            public static void main(String [] args) throws IOException, PlivoRestException {
                Plivo.init("<auth_id>","<auth_token>");
                CallCreateResponse response = Call.creator("<caller_id>",
                        Collections.singletonList("<destination_number1>", "<destination_number2>"),
                        "https://s3.amazonaws.com/static.plivo.com/broadcast.xml")
                        .answerMethod("GET")
                        .create();
                System.out.println(response);
            }
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). Destination numbers may also be SIP endpoints, in which case each destination\_number placeholder must be a valid SIP URI — for example, sip:[john1234@phone.plivo.com](mailto:john1234@phone.plivo.com).

        <Note>
          <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables, so as to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and it will automatically fetch them from the environment variables. You can use [System.getenv()](https://docs.oracle.com/javase/tutorial/essential/environment/env.html) to store environment variables and retrieve them when initializing the client.
        </Note>

        ## Test

        Save the file and run it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/makecall.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=91fc98e74b30fc4708b5f608889a18f2" alt="" width="1440" height="900" data-path="images/makecall.png" />
        </Frame>
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to broadcast voice messages to multiple recipients at once. You can play recorded audio when the call recipient answers or use text-to-speech, as we show here.

    You can use voice broadcasting for use cases such as:

    * Bulk voice calling campaigns
    * Emergency notifications
    * Survey campaigns
    * User feedback
    * Announcements
    * Promotions and special deals
    * Reminder campaigns

    You can broadcast voice alerts either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to broadcast voice alerts and notifications with a few clicks on the PHLO canvas and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Node.js, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/).

        ## Create the PHLO

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/broadcasting.gif?s=47fe14c58bb267101db704bb789854f7" alt="" width="1024" height="545" data-path="images/broadcasting.gif" />
        </Frame>

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * Click the **Start** node to open the Configuration tab to the right of the canvas, then enter the information to retrieve from the HTTP Request payload — in this case, from and to numbers.

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. This adds an **Initiate Call** node onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.

        * In the Configuration tab of the **Initiate Call** node, give the node a meaningful name. You can rename nodes as you like to improve your PHLO's readability. Enter a phone number in the From field that will serve as the caller ID, and enter as many numbers as you‘d like to call in the To field.

        * Validate the configuration by clicking **Validate**. Every time you finish configuring a node, click **Validate** to check the syntax and save your changes.

        * Drag and drop the **Play Audio** component onto the canvas. Draw a line to connect the **Answered** trigger state of the **Initiate Call** node to the Play Audio node.

        * In the Configuration tab of the **Play Audio** node, in the Speak Text box, enter a message to play to call recipients using text-to-speech.

        * Draw a line to connect the **Answered** trigger state of the **Initiate Call** node to the **Play Audio** node.

        * After you complete and validate all the node configurations, give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        ### With static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

        Create a file called `TriggerPhlo.go` and paste into it this code:

        ```go  theme={null}
        package main

        import (
        	"fmt"
        	"plivo-go"
        )
        // Initialize the following params with corresponding values to trigger resources
        const authId = "<auth_id>"
        const authToken = "<auth_token>"
        const phloId = "<phlo_id>"

        func main() {
        	testPhloRunWithoutParams()
        }

        func testPhloRunWithoutParams() {
        	phloClient, err := plivo.NewPhloClient(authId, authToken, &plivo.ClientOptions{})
        	if err != nil {
        			fmt.Print("Error", err.Error())
        			return
        		}
        	phloGet, err := phloClient.Phlos.Get(phloId)
        	if err != nil {
        			fmt.Print("Error", err.Error())
        			return
        		}
        	response, err := phloGet.Run(nil)
        	if err != nil {
        			fmt.Print("Error", err.Error())
        			return
        		}
        	fmt.Printf("Response: %#v\n", response)
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents).

        ### With dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code to the PHLO when you trigger it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        #### Code

        Create a file called `TriggerPhlo.go` and paste into it this code:

        ```go  theme={null}
        package main

        import (
        	"fmt"
        	"plivo-go"
        )
        // Initialize the following params with corresponding values to trigger resources
        const authId = "<auth_id>"
        const authToken = "<auth_token>"
        const phloId = "<phlo_id>"

        func main() {
        	testPhloRunWithParams()
        }

        func testPhloRunWithParams() {
        	phloClient, err := plivo.NewPhloClient(authId, authToken, &plivo.ClientOptions{})
        	if err != nil {
        			fmt.Print("Error", err.Error())
        			return
        		}
        	phloGet, err := phloClient.Phlos.Get(phloId)
        	if err != nil {
        			fmt.Print("Error", err.Error())
        			return
        		}
        	//pass corresponding from and to values
        	type params map[string]interface{}
        	response, err := phloGet.Run(params{
        		"from": "<caller_id>",
        		"dest1":   "<destination_number1>",
        		"dest2":   "<destination_number2>",
        		"dest3":   "<destination_number3>",
        		"dest4":   "<destination_number4>",
        		"dest5":   "<destination_number5>"
        	})

        	if err != nil {
        		println(err)
        	}
        	fmt.Printf("Response: %#v\n", response)
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        go run TriggerPhlo.go
        ```
      </Tab>

      <Tab title="Using XML">
        Here’s how to broadcast voice alerts and notifications using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. To see how this works, you can use [https://s3.amazonaws.com/static.plivo.com/broadcast.xml](https://s3.amazonaws.com/static.plivo.com/broadcast.xml) as an answer URL to test your first outgoing call. The file contains this XML code:

        ```xml  theme={null}
        <Response>
        <Speak>Congratulations! You have made your first bulk call.</Speak>
        </Response>
        ```

        This code instructs Plivo to say, “Congratulations!  You have made your first bulk call” to the call recipients. You can find the entire list of valid Plivo XML verbs in our [XML Reference](/voice/xml/overview/) documentation.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create voice alert broadcast application

        Create a file called `Broadcast.go` and paste into it this code:

        ```go  theme={null}
        package main

        import "fmt"
        import "github.com/plivo/plivo-go/v7"

        func main() {
        	client, err := plivo.NewClient("<auth_id>","<auth_token>", &plivo.ClientOptions{})
        	if err != nil {
        			fmt.Print("Error", err.Error())
        			return
        		}
        	response, err := client.Calls.Create(
        		plivo.CallCreateParams{
        			From: "<caller_id>",
        			To: "destination_number1<destination_number2",
        			AnswerURL: "https://s3.amazonaws.com/static.plivo.com/broadcast.xml",
        			AnswerMethod: "GET",
        		},
        	)
        	if err != nil {
        			fmt.Print("Error", err.Error())
        			return
        		}
        	fmt.Printf("Response: %#v\n", response)
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). Destination numbers may also be SIP endpoints, in which case each destination\_number placeholder must be a valid SIP URI — for example, sip:[john1234@phone.plivo.com](mailto:john1234@phone.plivo.com).

        <Note>
          <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables, so as to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and it will automatically fetch them from the environment variables. You can use `os.Setenv` and `os.Getenv` to store environment variables and fetch them when initializing the client.
        </Note>

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        go run Broadcast.go
        ```
      </Tab>
    </Tabs>
  </Tab>
</Tabs>
