# Source: https://plivo.com/docs/voice/use-cases/make-outbound-calls.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Make Outbound Calls

> Place outbound voice calls programmatically using the Plivo Voice API

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to make an outgoing call and greet the call recipient with a text-to-speech message when they answer. Use cases such as voice notifications and alerts, voice surveys, and, voice one-time passwords involve outbound calls as part of their call flow.

    You can start making and receiving calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to make an outbound call with a few clicks on the PHLO canvas, and trigger it with some simple code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-calls.png?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=f8b62e42991d9fd92d93eab071cb4124" alt="Outbound Call Flow" width="1448" height="774" data-path="images/outbound-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first PHLO, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/).

        ## Create the PHLO

        * To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound_call_phlo.gif?s=5e8307001ea215f316f3eafe6ac18d86" alt="Create a PHLO for outbound calls" width="1024" height="560" data-path="images/outbound_call_phlo.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.

        * In the Configuration pane at the right of the canvas, configure the **Initiate Call** node with a caller ID in the **From** field. Enter the destination number you wish to call in the **To** field.

          <Note>
            <strong>Note:</strong> You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through <a href="https://shopify.github.io/liquid/">Liquid</a> templating parameters when you trigger the PHLO from your application.
          </Note>

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Similarly, create a node from the **Play Audio** component. Connect the **Initiate Call** node to the **Play Audio** node using the **Answered** trigger state.

        * Configure the **Play Audio** node to play a message to the user by entering text in the Speak Text box in the Prompt section of the Configuration pane — for example, “Hello, you just received your first call.”

        * Connect the **Initiate Call** node’s **Answered** trigger state to the **Play Audio** node.

        * After you complete the configuration, give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        In either case, you need your Auth ID and Auth Token, which you can get from the overview page of the Plivo [console](https://cx.plivo.com/home).

        <Frame>
                    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/AuthID.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=8e3e0ebf88faacb95025a7a2854e8f43" alt="AUTHID" width="1440" height="254" data-path="images/AuthID.jpg" />
        </Frame>

        You also need the PHLO ID, which you can copy from the [PHLO list](https://cx.plivo.com/agents) page.

        <Frame>
                    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/Phlo_listing.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=27a26b1ea5747a683d08b688d47b5d88" alt="PHLO List" width="1440" height="348" data-path="images/Phlo_listing.jpg" />
        </Frame>

        ### With a static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
          <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="With Static Payload" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        ### Code

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

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents).

        ### With a dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code when you trigger it.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="With Dynamic Payload" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        ### Code

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
            to: '<destination_number>'
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
        $ node TriggerPhlo.js
        ```
      </Tab>

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to make an outbound call and leave a text-to-speech message when the recipient answers the call.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-calls.png?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=f8b62e42991d9fd92d93eab071cb4124" alt="Outbound Call Flow" width="1448" height="774" data-path="images/outbound-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. To see how this works, you can use [https://s3.amazonaws.com/static.plivo.com/answer.xml](https://s3.amazonaws.com/static.plivo.com/answer.xml) as an answer URL to test your first outgoing call. The file contains this XML code:

        ```xml  theme={null}
        <Response>
        <Speak>Congratulations! You've made your first outbound call!</Speak>
        </Response>
        ```

        This code instructs Plivo to say, “Congratulations! You’ve made your first outbound call!” to the call recipient. You can find the entire list of valid Plivo XML verbs in our [XML Reference](/voice/xml/overview/) documentation.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You can also follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-xml-voice/).

        ## Make an outbound call

        Create a file called `Makecall.js` and paste into it this code.

        ```js  theme={null}
        var plivo = require('plivo');

        (function main() {
            'use strict';

            var client = new plivo.Client("<auth_id>","<auth_token>");
            client.calls.create(
                "<caller_id>", // from
                "<destination_number>", // to
                "https://s3.amazonaws.com/static.plivo.com/answer.xml", // answer url
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

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        $ node Makecall.js
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to make an outgoing call and greet the call recipient with a text-to-speech message when they answer. Use cases such as voice notifications and alerts, voice surveys, and, voice one-time passwords involve outbound calls as part of their call flow.

    You can start making and receiving calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to make an outbound call with a few clicks on the PHLO canvas, and trigger it with some simple code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-calls.png?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=f8b62e42991d9fd92d93eab071cb4124" alt="Outbound Call Flow" width="1448" height="774" data-path="images/outbound-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first PHLO, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-phlo/).

        ## Create the PHLO

        * To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound_call_phlo.gif?s=5e8307001ea215f316f3eafe6ac18d86" alt="Create a PHLO for outbound calls" width="1024" height="560" data-path="images/outbound_call_phlo.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.

        * In the Configuration pane at the right of the canvas, configure the **Initiate Call** node with a caller ID in the **From** field. Enter the destination number you wish to call in the **To** field.

          <Note>
            <strong>Note:</strong> You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through <a href="https://shopify.github.io/liquid/">Liquid</a> templating parameters when you trigger the PHLO from your application.
          </Note>

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Similarly, create a node from the **Play Audio** component. Connect the **Initiate Call** node to the **Play Audio** node using the **Answered** trigger state.

        * Configure the **Play Audio** node to play a message to the user by entering text in the Speak Text box in the Prompt section of the Configuration pane — for example, “Hello, you just received your first call.”

        * Connect the **Initiate Call** node’s **Answered** trigger state to the **Play Audio** node.

        * After you complete the configuration, give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        In either case, you need your Auth ID and Auth Token, which you can get from the overview page of the Plivo [console](https://cx.plivo.com/home).

        <Frame>
                    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/AuthID.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=8e3e0ebf88faacb95025a7a2854e8f43" alt="AUTHID" width="1440" height="254" data-path="images/AuthID.jpg" />
        </Frame>

        You also need the PHLO ID, which you can copy from the [PHLO list](https://cx.plivo.com/agents) page.

        <Frame>
                    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/Phlo_listing.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=27a26b1ea5747a683d08b688d47b5d88" alt="PHLO List" width="1440" height="348" data-path="images/Phlo_listing.jpg" />
        </Frame>

        ### With a static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
          <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="With Static Payload" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        ### Code

        Create a file called `trigger_phlo.rb` and paste into it this code.

        ```rb  theme={null}
        require 'rubygems'
        require 'plivo'

        include Plivo

        AUTH_ID = '<auth_id>'
        AUTH_TOKEN = '<auth_token>'

        \# if credentials are stored in the PLIVO_AUTH_ID and the PLIVO_AUTH_TOKEN environment variables
        \# then initialize client as:
        \# client = Phlo.new

        begin
          phlo = client.phlo.get('<phlo_id>')
          response = phlo.run()
          puts response
        rescue PlivoRESTError => e
          puts 'Exception: ' + e.message
        end
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents).

        ### With a dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code when you trigger it.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="With Dynamic Payload" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        ### Code

        Create a file called `trigger_phlo.rb` and paste into it this code.

        ```rb  theme={null}
        require 'rubygems'
        require 'plivo'

        include Plivo

        AUTH_ID = '<auth_id>'
        AUTH_TOKEN = '<auth_token>'

        client = Phlo.new(AUTH_ID, AUTH_TOKEN)

        \# if credentials are stored in the PLIVO_AUTH_ID and the PLIVO_AUTH_TOKEN environment variables
        \# then initialize client as:
        \# client = Phlo.new

        begin
          phlo = client.phlo.get('<phlo_id>')
          #parameters set in PHLO - params
          params = {
             from: '<caller_id>',
             to: '<destination_number>'
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
        $ ruby trigger_phlo.rb
        ```
      </Tab>

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to make an outbound call and leave a text-to-speech message when the recipient answers the call.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-calls.png?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=f8b62e42991d9fd92d93eab071cb4124" alt="Outbound Call Flow" width="1448" height="774" data-path="images/outbound-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. To see how this works, you can use [https://s3.amazonaws.com/static.plivo.com/answer.xml](https://s3.amazonaws.com/static.plivo.com/answer.xml) as an answer URL to test your first outgoing call. The file contains this XML code:

        ```xml  theme={null}
        <Response>
        <Speak>Congratulations! You've made your first outbound call!</Speak>
        </Response>
        ```

        This code instructs Plivo to say, “Congratulations! You’ve made your first outbound call!” to the call recipient. You can find the entire list of valid Plivo XML verbs in our [XML Reference](/voice/xml/overview/) documentation.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You can also follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/).

        ## Make an outbound call

        Create a file called `make_call.rb` and paste into it this code.

        ```rb  theme={null}
        require 'rubygems'
        require 'plivo'

        include Plivo
        include Plivo::Exceptions

        api = RestClient.new("<auth_id>","<auth_token>")

        begin
          response = api.calls.create(
            '+12025550000',
            ['+12025551111'],
            'https://s3.amazonaws.com/static.plivo.com/answer.xml',
             {
                    answer_method: "GET",
             },
          )
          puts response
        rescue PlivoRESTError => e
          puts 'Exception: ' + e.message
        end
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        $ ruby make_call.rb
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to make an outgoing call and greet the call recipient with a text-to-speech message when they answer. Use cases such as voice notifications and alerts, voice surveys, and, voice one-time passwords involve outbound calls as part of their call flow.

    You can start making and receiving calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to make an outbound call with a few clicks on the PHLO canvas, and trigger it with some simple code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-calls.png?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=f8b62e42991d9fd92d93eab071cb4124" alt="Outbound Call Flow" width="1448" height="774" data-path="images/outbound-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first PHLO, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound_call_phlo.gif?s=5e8307001ea215f316f3eafe6ac18d86" alt="Create a PHLO for outbound calls" width="1024" height="560" data-path="images/outbound_call_phlo.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.

        * In the Configuration pane at the right of the canvas, configure the **Initiate Call** node with a caller ID in the **From** field. Enter the destination number you wish to call in the **To** field.

          <Note>
            <strong>Note:</strong> You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through <a href="https://shopify.github.io/liquid/">Liquid</a> templating parameters when you trigger the PHLO from your application.
          </Note>

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Similarly, create a node from the **Play Audio** component. Connect the **Initiate Call** node to the **Play Audio** node using the **Answered** trigger state.

        * Configure the **Play Audio** node to play a message to the user by entering text in the Speak Text box in the Prompt section of the Configuration pane — for example, “Hello, you just received your first call.”

        * Connect the **Initiate Call** node’s **Answered** trigger state to the **Play Audio** node.

        * After you complete the configuration, give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        In either case, you need your Auth ID and Auth Token, which you can get from the overview page of the Plivo [console](https://cx.plivo.com/home).

        <Frame>
                    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/AuthID.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=8e3e0ebf88faacb95025a7a2854e8f43" alt="AUTHID" width="1440" height="254" data-path="images/AuthID.jpg" />
        </Frame>

        You also need the PHLO ID, which you can copy from the [PHLO list](https://cx.plivo.com/agents) page.

        <Frame>
                    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/Phlo_listing.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=27a26b1ea5747a683d08b688d47b5d88" alt="PHLO List" width="1440" height="348" data-path="images/Phlo_listing.jpg" />
        </Frame>

        ### With a static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
          <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="With Static Payload" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        ### Code

        Create a file called `trigger_phlo.py` and paste into it this code.

        ```py  theme={null}
        import plivo

        auth_id = '<auth_id>'
        auth_token = '<auth_token>'
        phlo_id = '<phlo_id>'
        phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
        phlo = phlo_client.phlo.get(phlo_id)
        response = phlo.run()
        print str(response)
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents).

        ### With a dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code when you trigger it.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="With Dynamic Payload" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        ### Code

        Create a file called `trigger_phlo.py` and paste into it this code.

        ```py  theme={null}
        import plivo

        auth_id = '<auth_id>'
        auth_token = '<auth_token>'
        phlo_id = '<phlo_id>'
        payload = {"from" : "<caller_id>","to" : "<destination_number>"}
        phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
        phlo = phlo_client.phlo.get(phlo_id)
        response = phlo.run(**payload)
        print str(response)
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        $ python trigger_phlo.py
        ```
      </Tab>

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to make an outbound call and leave a text-to-speech message when the recipient answers the call.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-calls.png?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=f8b62e42991d9fd92d93eab071cb4124" alt="Outbound Call Flow" width="1448" height="774" data-path="images/outbound-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. To see how this works, you can use [https://s3.amazonaws.com/static.plivo.com/answer.xml](https://s3.amazonaws.com/static.plivo.com/answer.xml) as an answer URL to test your first outgoing call. The file contains this XML code:

        ```xml  theme={null}
        <Response>
        <Speak>Congratulations! You've made your first outbound call!</Speak>
        </Response>
        ```

        This code instructs Plivo to say, “Congratulations! You’ve made your first outbound call!” to the call recipient. You can find the entire list of valid Plivo XML verbs in our [XML Reference](/voice/xml/overview/) documentation.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You can also follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-xml-voice/).

        ## Make an outbound call

        Create a file called `make_call.py` and paste into it this code.

        ```py  theme={null}
        import plivo

        client = plivo.RestClient('<auth_id>','<auth_token>')
        response = client.calls.create(
            from_='<caller_id>',
            to_='<destination_number>',
            answer_url='https://s3.amazonaws.com/static.plivo.com/answer.xml',
            answer_method='GET', )
        print(response)
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        $ python make_call.py
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to make an outgoing call and greet the call recipient with a text-to-speech message when they answer. Use cases such as voice notifications and alerts, voice surveys, and, voice one-time passwords involve outbound calls as part of their call flow.

    You can start making and receiving calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to make an outbound call with a few clicks on the PHLO canvas, and trigger it with some simple code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-calls.png?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=f8b62e42991d9fd92d93eab071cb4124" alt="Outbound Call Flow" width="1448" height="774" data-path="images/outbound-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first PHLO, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound_call_phlo.gif?s=5e8307001ea215f316f3eafe6ac18d86" alt="Create a PHLO for outbound calls" width="1024" height="560" data-path="images/outbound_call_phlo.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.

        * In the Configuration pane at the right of the canvas, configure the **Initiate Call** node with a caller ID in the **From** field. Enter the destination number you wish to call in the **To** field.

          <Note>
            <strong>Note:</strong> You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through <a href="https://shopify.github.io/liquid/">Liquid</a> templating parameters when you trigger the PHLO from your application.
          </Note>

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Similarly, create a node from the **Play Audio** component. Connect the **Initiate Call** node to the **Play Audio** node using the **Answered** trigger state.

        * Configure the **Play Audio** node to play a message to the user by entering text in the Speak Text box in the Prompt section of the Configuration pane — for example, “Hello, you just received your first call.”

        * Connect the **Initiate Call** node’s **Answered** trigger state to the **Play Audio** node.

        * After you complete the configuration, give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        In either case, you need your Auth ID and Auth Token, which you can get from the overview page of the Plivo [console](https://cx.plivo.com/home).

        <Frame>
                    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/AuthID.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=8e3e0ebf88faacb95025a7a2854e8f43" alt="AUTHID" width="1440" height="254" data-path="images/AuthID.jpg" />
        </Frame>

        You also need the PHLO ID, which you can copy from the [PHLO list](https://cx.plivo.com/agents) page.

        <Frame>
                    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/Phlo_listing.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=27a26b1ea5747a683d08b688d47b5d88" alt="PHLO List" width="1440" height="348" data-path="images/Phlo_listing.jpg" />
        </Frame>

        ### With a static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
          <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="With Static Payload" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        ### Code

        Create a file called TriggerPhlo.php and paste into it this code:

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

        ### With a dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code when you trigger it.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="With Dynamic Payload" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        ### Code

        Create a file called TriggerPhlo.php and paste into it this code:

        ```php  theme={null}
        <?php
        require 'vendor/autoload.php';
        use Plivo\Resources\PHLO\PhloRestClient;
        use Plivo\Exceptions\PlivoRestException;
        $client = new PhloRestClient("<auth_id>", "<auth_token>");

        $phlo = $client->phlo->get("<phlo_id>");
        try {
            $response = $phlo->run(["from" => "<caller_id>", "to" => "<destination_number>"]);
            print_r($response);
        } catch (PlivoRestException $ex) {
            print_r($ex);
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        $ php TriggerPhlo.php
        ```
      </Tab>

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to make an outbound call and leave a text-to-speech message when the recipient answers the call.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-calls.png?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=f8b62e42991d9fd92d93eab071cb4124" alt="Outbound Call Flow" width="1448" height="774" data-path="images/outbound-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. To see how this works, you can use [https://s3.amazonaws.com/static.plivo.com/answer.xml](https://s3.amazonaws.com/static.plivo.com/answer.xml) as an answer URL to test your first outgoing call. The file contains this XML code:

        ```xml  theme={null}
        <Response>
        <Speak>Congratulations! You've made your first outbound call!</Speak>
        </Response>
        ```

        This code instructs Plivo to say, “Congratulations! You’ve made your first outbound call!” to the call recipient. You can find the entire list of valid Plivo XML verbs in our [XML Reference](/voice/xml/overview/) documentation.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You can also follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-api-xml-voice/).

        ## Make an outbound call

        Create a file called `MakeCall.php` and paste into it this code:

        ```php  theme={null}
        <?php
        require 'vendor/autoload.php';
        use Plivo\RestClient;

        $auth_id    = "<auth_id>";
        $auth_token = "<auth_token>";
        $p          = new RestClient($auth_id, $auth_token);

        $response = $client->calls->create('<caller_id>',
                                         ['<destination_number>'],
                                         'https://s3.amazonaws.com/static.plivo.com/answer.xml',);
        print_r($response);
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        $ php MakeCall.php
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to make an outgoing call and greet the call recipient with a text-to-speech message when they answer. Use cases such as voice notifications and alerts, voice surveys, and, voice one-time passwords involve outbound calls as part of their call flow.

    You can start making and receiving calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to make an outbound call with a few clicks on the PHLO canvas, and trigger it with some simple code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-calls.png?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=f8b62e42991d9fd92d93eab071cb4124" alt="Outbound Call Flow" width="1448" height="774" data-path="images/outbound-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first PHLO, follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound_call_phlo.gif?s=5e8307001ea215f316f3eafe6ac18d86" alt="Create a PHLO for outbound calls" width="1024" height="560" data-path="images/outbound_call_phlo.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.

        * In the Configuration pane at the right of the canvas, configure the **Initiate Call** node with a caller ID in the **From** field. Enter the destination number you wish to call in the **To** field.

          <Note>
            <strong>Note:</strong> You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through <a href="https://shopify.github.io/liquid/">Liquid</a> templating parameters when you trigger the PHLO from your application.
          </Note>

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Similarly, create a node from the **Play Audio** component. Connect the **Initiate Call** node to the **Play Audio** node using the **Answered** trigger state.

        * Configure the **Play Audio** node to play a message to the user by entering text in the Speak Text box in the Prompt section of the Configuration pane — for example, “Hello, you just received your first call.”

        * Connect the **Initiate Call** node’s **Answered** trigger state to the **Play Audio** node.

        * After you complete the configuration, give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        In either case, you need your Auth ID and Auth Token, which you can get from the overview page of the Plivo [console](https://cx.plivo.com/home).

        <Frame>
                    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/AuthID.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=8e3e0ebf88faacb95025a7a2854e8f43" alt="AUTHID" width="1440" height="254" data-path="images/AuthID.jpg" />
        </Frame>

        You also need the PHLO ID, which you can copy from the [PHLO list](https://cx.plivo.com/agents) page.

        <Frame>
                    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/Phlo_listing.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=27a26b1ea5747a683d08b688d47b5d88" alt="PHLO List" width="1440" height="348" data-path="images/Phlo_listing.jpg" />
        </Frame>

        ### With a static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
          <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="With Static Payload" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        ### Code

        In Visual Studio, in the CS project, open the file `Program.cs` and paste into it this code.

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

        ### With a dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code when you trigger it.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="With Dynamic Payload" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        ### Code

        In Visual Studio, in the CS project, open the file `Program.cs` and paste into it this code.

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
                        { "to", "<destination_number>" }

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
        Here’s how to use Plivo APIs and XML to make an outbound call and leave a text-to-speech message when the recipient answers the call.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-calls.png?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=f8b62e42991d9fd92d93eab071cb4124" alt="Outbound Call Flow" width="1448" height="774" data-path="images/outbound-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. To see how this works, you can use [https://s3.amazonaws.com/static.plivo.com/answer.xml](https://s3.amazonaws.com/static.plivo.com/answer.xml) as an answer URL to test your first outgoing call. The file contains this XML code:

        ```xml  theme={null}
        <Response>
        <Speak>Congratulations! You've made your first outbound call!</Speak>
        </Response>
        ```

        This code instructs Plivo to say, “Congratulations! You’ve made your first outbound call!” to the call recipient. You can find the entire list of valid Plivo XML verbs in our [XML Reference](/voice/xml/overview/) documentation.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You can also follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-api-xml-voice/).

        ## Make an outbound call

        In Visual Studio, in the CS project, open the file `Program.cs` and paste into it this code.

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
        ÷            var api = new PlivoApi("<auth_id>","<auth_token>");
                    var response = api.Call.Create(
                        to: new List<String> { "<destination_number>" },
                        from: "<caller_id>",
                        answerMethod: "GET",
                        answerUrl: "https://s3.amazonaws.com/static.plivo.com/answer.xml"
                    );
                    Console.WriteLine(response);
                }
            }
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to make an outgoing call and greet the call recipient with a text-to-speech message when they answer. Use cases such as voice notifications and alerts, voice surveys, and, voice one-time passwords involve outbound calls as part of their call flow.

    You can start making and receiving calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to make an outbound call with a few clicks on the PHLO canvas, and trigger it with some simple code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-calls.png?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=f8b62e42991d9fd92d93eab071cb4124" alt="Outbound Call Flow" width="1448" height="774" data-path="images/outbound-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first PHLO, follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound_call_phlo.gif?s=5e8307001ea215f316f3eafe6ac18d86" alt="Create a PHLO for outbound calls" width="1024" height="560" data-path="images/outbound_call_phlo.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.

        * In the Configuration pane at the right of the canvas, configure the **Initiate Call** node with a caller ID in the **From** field. Enter the destination number you wish to call in the **To** field.

          <Note>
            <strong>Note:</strong> You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through <a href="https://shopify.github.io/liquid/">Liquid</a> templating parameters when you trigger the PHLO from your application.
          </Note>

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Similarly, create a node from the **Play Audio** component. Connect the **Initiate Call** node to the **Play Audio** node using the **Answered** trigger state.

        * Configure the **Play Audio** node to play a message to the user by entering text in the Speak Text box in the Prompt section of the Configuration pane — for example, “Hello, you just received your first call.”

        * Connect the **Initiate Call** node’s **Answered** trigger state to the **Play Audio** node.

        * After you complete the configuration, give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        In either case, you need your Auth ID and Auth Token, which you can get from the overview page of the Plivo [console](https://cx.plivo.com/home).

        <Frame>
                    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/AuthID.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=8e3e0ebf88faacb95025a7a2854e8f43" alt="AUTHID" width="1440" height="254" data-path="images/AuthID.jpg" />
        </Frame>

        You also need the PHLO ID, which you can copy from the [PHLO list](https://cx.plivo.com/agents) page.

        <Frame>
                    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/Phlo_listing.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=27a26b1ea5747a683d08b688d47b5d88" alt="PHLO List" width="1440" height="348" data-path="images/Phlo_listing.jpg" />
        </Frame>

        ### With a static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
          <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="With Static Payload" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        ### Code

        Create a Java class in the project called `TriggerPhlo` and paste into it this code.

        ```java  theme={null}
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

        ### With a dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code when you trigger it.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="With Dynamic Payload" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        ### Code

        Create a Java class in the project called `TriggerPhlo` and paste into it this code.

        ```java  theme={null}
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
                Map<String, Object> payload = new HashMap<>();
                payload.put("from", "<caller_id>");
                payload.put("to", "<destination_number>");
                PhloUpdateResponse response = Phlo.updater(phloId).payload(payload).run();
            }
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.
      </Tab>

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to make an outbound call and leave a text-to-speech message when the recipient answers the call.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-calls.png?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=f8b62e42991d9fd92d93eab071cb4124" alt="Outbound Call Flow" width="1448" height="774" data-path="images/outbound-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. To see how this works, you can use [https://s3.amazonaws.com/static.plivo.com/answer.xml](https://s3.amazonaws.com/static.plivo.com/answer.xml) as an answer URL to test your first outgoing call. The file contains this XML code:

        ```xml  theme={null}
        <Response>
        <Speak>Congratulations! You've made your first outbound call!</Speak>
        </Response>
        ```

        This code instructs Plivo to say, “Congratulations! You’ve made your first outbound call!” to the call recipient. You can find the entire list of valid Plivo XML verbs in our [XML Reference](/voice/xml/overview/) documentation.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You can also follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-api-xml-voice/).

        ## Make an outbound call

        Create a Java class in the project `MakeCall` and paste into it this code.

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
                        Collections.singletonList("<destination_number>"),
                        "https://s3.amazonaws.com/static.plivo.com/answer.xml")
                        .answerMethod("GET")
                        .create();
                System.out.println(response);
            }
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to make an outgoing call and greet the call recipient with a text-to-speech message when they answer. Use cases such as voice notifications and alerts, voice surveys, and, voice one-time passwords involve outbound calls as part of their call flow.

    You can start making and receiving calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to make an outbound call with a few clicks on the PHLO canvas, and trigger it with some simple code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-calls.png?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=f8b62e42991d9fd92d93eab071cb4124" alt="Outbound Call Flow" width="1448" height="774" data-path="images/outbound-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first PHLO, follow our instructions to [set up a Go development environment](/voice/quickstart/go-quickstart/#set-up-your-go-gin-gonic-dev-environment).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound_call_phlo.gif?s=5e8307001ea215f316f3eafe6ac18d86" alt="Create a PHLO for outbound calls" width="1024" height="560" data-path="images/outbound_call_phlo.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.

        * In the Configuration pane at the right of the canvas, configure the **Initiate Call** node with a caller ID in the **From** field. Enter the destination number you wish to call in the **To** field.

          <Note>
            <strong>Note:</strong> You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through <a href="https://shopify.github.io/liquid/">Liquid</a> templating parameters when you trigger the PHLO from your application.
          </Note>

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Similarly, create a node from the **Play Audio** component. Connect the **Initiate Call** node to the **Play Audio** node using the **Answered** trigger state.

        * Configure the **Play Audio** node to play a message to the user by entering text in the Speak Text box in the Prompt section of the Configuration pane — for example, “Hello, you just received your first call.”

        * Connect the **Initiate Call** node’s **Answered** trigger state to the **Play Audio** node.

        * After you complete the configuration, give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        In either case, you need your Auth ID and Auth Token, which you can get from the overview page of the Plivo [console](https://cx.plivo.com/home).

        <Frame>
                    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/AuthID.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=8e3e0ebf88faacb95025a7a2854e8f43" alt="AUTHID" width="1440" height="254" data-path="images/AuthID.jpg" />
        </Frame>

        You also need the PHLO ID, which you can copy from the [PHLO list](https://cx.plivo.com/agents) page.

        <Frame>
                    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/Phlo_listing.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=27a26b1ea5747a683d08b688d47b5d88" alt="PHLO List" width="1440" height="348" data-path="images/Phlo_listing.jpg" />
        </Frame>

        ### With a static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
          <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="With Static Payload" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        ### Code

        Create a file called `TriggerPhlo.go` and paste into it this code:

        ```go  theme={null}
        package main

        import (
        	"fmt"
        	"plivo-go"
        )
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

        ### With a dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code when you trigger it.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="With Dynamic Payload" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        ### Code

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
        		"to": "<destination_number>",
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
        Here’s how to use Plivo APIs and XML to make an outbound call and leave a text-to-speech message when the recipient answers the call.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-calls.png?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=f8b62e42991d9fd92d93eab071cb4124" alt="Outbound Call Flow" width="1448" height="774" data-path="images/outbound-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. To see how this works, you can use [https://s3.amazonaws.com/static.plivo.com/answer.xml](https://s3.amazonaws.com/static.plivo.com/answer.xml) as an answer URL to test your first outgoing call. The file contains this XML code:

        ```xml  theme={null}
        <Response>
        <Speak>Congratulations! You've made your first outbound call!</Speak>
        </Response>
        ```

        This code instructs Plivo to say, “Congratulations! You’ve made your first outbound call!” to the call recipient. You can find the entire list of valid Plivo XML verbs in our [XML Reference](/voice/xml/overview/) documentation.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You can also follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-xml-voice/).

        ## Make an outbound call

        Create a file called `MakeCall.go` and paste into it this code:

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
        			To: "<destination_number>",
        			AnswerURL: "https://s3.amazonaws.com/static.plivo.com/answer.xml",
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

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        go run MakeCall.go
        ```
      </Tab>
    </Tabs>
  </Tab>
</Tabs>
