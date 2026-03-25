# Source: https://plivo.com/docs/messaging/use-cases/send-an-sms/send-an-sms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send SMS Text Messages

> Send outbound SMS text messages to any phone number using Plivo

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to send an SMS text message to any phone number. Businesses send text messages to notify customers about recent information, send alerts, and provide delivery status updates, among other use cases.

    You can start sending SMS messages either by using our PHLO visual workflow builder or our APIs. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to send an SMS text message with a few clicks on the PHLO canvas and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send-sms-phlo.jpg?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=57bb1cf875132c19f7d9a525a124eff6" alt="Send SMS" width="1446" height="774" data-path="images/send-sms-phlo.jpg" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Node.js, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
          <video autoplay loop muted inline width="560" height="315">
            <source width="560" height="315" src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send_sms.mp4?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=a30fc7cf0f8b8fed34d78daf6794da36" type="video/mp4" data-path="images/send_sms.mp4" />
          </video>
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left-hand side, drag and drop the **Send Message** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s  **API Request** trigger state to the **Send Message** node.

        * In the Configuration pane at the right of the canvas, configure the **Send Message** node with a sender ID in the **From** field. Enter the destination number you wish to send a message to in the **To** field. Put your message in the **Text** field.

          <Note>
            <strong>Note:</strong> You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through <a rel="nofollow" href="https://shopify.github.io/liquid/">Liquid</a> templating parameters when you trigger the PHLO from your application.
          </Note>

        * Once you’ve configured the node, click **Validate** to save the configuration.

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
          <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" width="1398" height="765" data-path="images/static_payload.png" />
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

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents).

        ### With a dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code when you trigger it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send_sms_access_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=7af235ce77dc4dea5de829ca38d2e76f" alt="" width="1439" height="818" data-path="images/send_sms_access_payload.png" />
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
            From: '<sender_id>',
            To: '<destination_number>',
        }
        phloClient = new PhloClient(authId, authToken);
        phloClient.phlo(phloId).run(payload).then(function (result) {
            console.log('Phlo run result', result);
        }).catch(function (err) {
            console.error('Phlo run failed', err);
        });
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        Save the file and run it.

        ```shell  theme={null}
        node TriggerPhlo.js
        ```
      </Tab>

      <Tab title="Using API">
        Here’s how to use Plivo APIs to send outbound SMS text messages.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send-sms-api.jpg?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=6695185c1771e4583e7c0a45112c8cbf" alt="Send SMS" width="1446" height="774" data-path="images/send-sms-api.jpg" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-messaging/).

        ## Create the send SMS application

        Create a file called `send_sms.js` and paste into it this code.

        ```js  theme={null}
        var plivo = require('plivo');
        (function main() {
            'use strict';
            var client = new plivo.Client("<auth_id>", "<auth_token>");
            client.messages.create(
              { 
                  src: "<sender_id>", 
                  dst: "<destination_number>",
                  text: "Hello, from Node.js!",
              }
              ).then(function (response) {
                console.log(response);
            });
        })();
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). In countries other than the US and Canada you can use a [sender ID](/messaging/concepts/sender-id-usage/) for the message source. You must have a Plivo phone number to send messages to the US or Canada; you can buy a Plivo number from Phone Numbers > [Buy Numbers](https://cx.plivo.com/phone-numbers) on the Plivo console or via the [Numbers API](/numbers/api/phone-number/#buy-a-phone-number).

        <Note>
          <strong>Note:</strong>
          We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
        </Note>

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        node send_sms.js
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to send an SMS text message to any phone number. Businesses send text messages to notify customers about recent information, send alerts, and provide delivery status updates, among other use cases.

    You can start sending SMS messages either by using our PHLO visual workflow builder or our APIs. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to send an SMS text message with a few clicks on the PHLO canvas and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send-sms-phlo.jpg?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=57bb1cf875132c19f7d9a525a124eff6" alt="Send SMS" width="1446" height="774" data-path="images/send-sms-phlo.jpg" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Ruby, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
          <video autoplay loop muted inline width="560" height="315">
            <source width="560" height="315" src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send_sms.mp4?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=a30fc7cf0f8b8fed34d78daf6794da36" type="video/mp4" data-path="images/send_sms.mp4" />
          </video>
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left-hand side, drag and drop the **Send Message** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s  **API Request** trigger state to the **Send Message** node.

        * In the Configuration pane at the right of the canvas, configure the **Send Message** node with a sender ID in the **From** field. Enter the destination number you wish to send a message to in the **To** field. Put your message in the **Text** field.

          <Note>
            <strong>Note:</strong> You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through <a href="https://shopify.github.io/liquid/">Liquid</a> templating parameters when you trigger the PHLO from your application.
          </Note>

        * Once you’ve configured the node, click **Validate** to save the configuration.

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
          <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

        Create a file called `trigger_phlo.rb` and paste into it this code.

        ```rb  theme={null}
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

        ### With a dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code when you trigger it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send_sms_access_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=7af235ce77dc4dea5de829ca38d2e76f" alt="" width="1439" height="818" data-path="images/send_sms_access_payload.png" />
        </Frame>

        #### Code

        Create a file called `trigger_phlo.rb` and paste into it this code.

        ```rb  theme={null}
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
             From: '<sender_id>',
             To: '<destination_number>',
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

      <Tab title="Using API">
        Here’s how to use Plivo APIs to send outbound SMS text messages.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send-sms-api.jpg?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=6695185c1771e4583e7c0a45112c8cbf" alt="Send SMS" width="1446" height="774" data-path="images/send-sms-api.jpg" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-messaging/).

        ## Create the send SMS application

        Create a file called `send_sms.rb` and paste into it this code.

        ```rb  theme={null}
        require "plivo"
        include Plivo

        api = RestClient.new("<auth_id>","<auth_token>")
        response = api.messages.create(
            src:"<sender_id>",
            dst:"<destination_number>",
            text:"Hello, from Ruby!"
          )
          puts response
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164)] (for example, +12025551234). In countries other than the US and Canada you can use a [sender ID](/messaging/concepts/sender-id-usage/) for the message source. You must have a Plivo phone number to send messages to the US or Canada; you can buy a Plivo number from Phone Numbers > [Buy Numbers](https://cx.plivo.com/phone-numbers) on the Plivo console or via the [Numbers API](/numbers/api/phone-number/#buy-a-phone-number).

        <Note>
          <strong>Note:</strong>
          We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `ENV` to store environment variables and fetch them when initializing the client.
        </Note>

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        ruby send_sms.rb
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to send an SMS text message to any phone number. Businesses send text messages to notify customers about recent information, send alerts, and provide delivery status updates, among other use cases.

    You can start sending SMS messages either by using our PHLO visual workflow builder or our APIs. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to send an SMS text message with a few clicks on the PHLO canvas and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send-sms-phlo.jpg?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=57bb1cf875132c19f7d9a525a124eff6" alt="Send SMS" width="1446" height="774" data-path="images/send-sms-phlo.jpg" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Python, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
          <video autoplay loop muted inline width="560" height="315">
            <source width="560" height="315" src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send_sms.mp4?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=a30fc7cf0f8b8fed34d78daf6794da36" type="video/mp4" data-path="images/send_sms.mp4" />
          </video>
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left-hand side, drag and drop the **Send Message** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s  **API Request** trigger state to the **Send Message** node.

        * In the Configuration pane at the right of the canvas, configure the **Send Message** node with a sender ID in the **From** field. Enter the destination number you wish to send a message to in the **To** field. Put your message in the **Text** field.

          <Note>
            <strong>Note:</strong> You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through <a href="https://shopify.github.io/liquid/">Liquid</a> templating parameters when you trigger the PHLO from your application.
          </Note>

        * Once you’ve configured the node, click **Validate** to save the configuration.

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
          <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

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
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send_sms_access_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=7af235ce77dc4dea5de829ca38d2e76f" alt="" width="1439" height="818" data-path="images/send_sms_access_payload.png" />
        </Frame>

        #### Code

        Create a file called `trigger_phlo.py` and paste into it this code.

        ```py  theme={null}
        import plivo

        auth_id = '<auth_id>'
        auth_token = '<auth_token>'
        phlo_id = '<phlo_id>'
        payload = {"From" : "<sender_id>","To" : "<destination_number>"}
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

      <Tab title="Using API">
        Here’s how to use Plivo APIs to send outbound SMS text messages.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send-sms-api.jpg?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=6695185c1771e4583e7c0a45112c8cbf" alt="Send SMS" width="1446" height="774" data-path="images/send-sms-api.jpg" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-messaging/).

        ## Create the send SMS application

        Create a file called `send_sms.py` and paste into it this code.

        ```py  theme={null}
        import plivo

        client = plivo.RestClient('<auth_id>','<auth_token>')
        response = client.messages.create(
            src='<sender_id>',
            dst='<destination_number>',
            text='Hello, from Python!',)
        print(response)
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). In countries other than the US and Canada you can use a [sender ID](/messaging/concepts/sender-id-usage/) for the message source. You must have a Plivo phone number to send messages to the US or Canada; you can buy a Plivo number from Phone Numbers > [Buy Numbers](https://cx.plivo.com/phone-numbers) on the Plivo console or via the [Numbers API](/numbers/api/phone-number/#buy-a-phone-number).

        <Note>
          <strong>Note:</strong>
          We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `os module(os.environ)` to store environment variables and fetch them when initializing the client.
        </Note>

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        $ python send_sms.py
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to send an SMS text message to any phone number. Businesses send text messages to notify customers about recent information, send alerts, and provide delivery status updates, among other use cases.

    You can start sending SMS messages either by using our PHLO visual workflow builder or our APIs. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to send an SMS text message with a few clicks on the PHLO canvas and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send-sms-phlo.jpg?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=57bb1cf875132c19f7d9a525a124eff6" alt="Send SMS" width="1446" height="774" data-path="images/send-sms-phlo.jpg" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with PHP, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
          <video autoplay loop muted inline width="560" height="315">
            <source width="560" height="315" src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send_sms.mp4?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=a30fc7cf0f8b8fed34d78daf6794da36" type="video/mp4" data-path="images/send_sms.mp4" />
          </video>
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left-hand side, drag and drop the **Send Message** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s  **API Request** trigger state to the **Send Message** node.

        * In the Configuration pane at the right of the canvas, configure the **Send Message** node with a sender ID in the **From** field. Enter the destination number you wish to send a message to in the **To** field. Put your message in the **Text** field.

          <Note>
            <strong>Note:</strong> You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through <a href="https://shopify.github.io/liquid/">Liquid</a> templating parameters when you trigger the PHLO from your application.
          </Note>

        * Once you’ve configured the node, click **Validate** to save the configuration.

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
          <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

        Create a file called `TriggerPhlo.php` and paste into it this code.

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
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send_sms_access_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=7af235ce77dc4dea5de829ca38d2e76f" alt="" width="1439" height="818" data-path="images/send_sms_access_payload.png" />
        </Frame>

        #### Code

        Create a file called `TriggerPhlo.php` and paste into it this code.

        ```php  theme={null}
        <?php
        require 'vendor/autoload.php';
        use Plivo\Resources\PHLO\PhloRestClient;
        use Plivo\Exceptions\PlivoRestException;
        $client = new PhloRestClient("<auth_id>", "<auth_token>");

        $phlo = $client->phlo->get("<phlo_id>");
        try {
            $response = $phlo->run(["From" => "<sender_id>", "To" => "<destination_number>"]);
            print_r($response);
        } catch (PlivoRestException $ex) {
            print_r($ex);
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        php TriggerPhlo.php
        ```
      </Tab>

      <Tab title="Using API">
        Here’s how to use Plivo APIs to send outbound SMS text messages.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send-sms-api.jpg?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=6695185c1771e4583e7c0a45112c8cbf" alt="Send SMS" width="1446" height="774" data-path="images/send-sms-api.jpg" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-api-messaging/).

        ## Create the send SMS application

        Create a file called `SendSMS.php` and paste into it this code.

        ```php  theme={null}
        <?php
        require 'vendor/autoload.php';
        use Plivo\RestClient;
        $client = new RestClient("<auth_id>","<auth_token>");
        $response = $client->messages->create(
             [  
                "src" => "<sender_id>",
                "dst" => "<destination_number>",
                "text"  =>"Hello, from PHP!"
             ]
        );
        print_r($response);
        ?>
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). In countries other than the US and Canada you can use a [sender ID](/messaging/concepts/sender-id-usage/) for the message source. You must have a Plivo phone number to send messages to the US or Canada; you can buy a Plivo number from Phone Numbers > [Buy Numbers](https://cx.plivo.com/phone-numbers) on the Plivo console or via the [Numbers API](/numbers/api/phone-number/#buy-a-phone-number).

        <Note>
          <strong>Note:</strong>
          We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `ENV` to store environment variables and fetch them when initializing the client.
        </Note>

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        php SendSMS.php
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to send an SMS text message to any phone number. Businesses send text messages to notify customers about recent information, send alerts, and provide delivery status updates, among other use cases.

    You can start sending SMS messages either by using our PHLO visual workflow builder or our APIs. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to send an SMS text message with a few clicks on the PHLO canvas and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send-sms-phlo.jpg?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=57bb1cf875132c19f7d9a525a124eff6" alt="Send SMS" width="1446" height="774" data-path="images/send-sms-phlo.jpg" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with .NET, follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
          <video autoplay loop muted inline width="560" height="315">
            <source width="560" height="315" src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send_sms.mp4?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=a30fc7cf0f8b8fed34d78daf6794da36" type="video/mp4" data-path="images/send_sms.mp4" />
          </video>
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left-hand side, drag and drop the **Send Message** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s  **API Request** trigger state to the **Send Message** node.

        * In the Configuration pane at the right of the canvas, configure the **Send Message** node with a sender ID in the **From** field. Enter the destination number you wish to send a message to in the **To** field. Put your message in the **Text** field.

          <Note>
            <strong>Note:</strong> You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through <a href="https://shopify.github.io/liquid/">Liquid</a> templating parameters when you trigger the PHLO from your application.
          </Note>

        * Once you’ve configured the node, click **Validate** to save the configuration.

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
          <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

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
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send_sms_access_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=7af235ce77dc4dea5de829ca38d2e76f" alt="" width="1439" height="818" data-path="images/send_sms_access_payload.png" />
        </Frame>

        #### Code

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
                        { "From", "<sender_id>" },
                        { "To", "<destination_number>" }
                    };  
                    Console.WriteLine(phlo.Run(data));
                }
            }
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164)(for example, +12025551234).

        ## Test

        Save the file and run it.
      </Tab>

      <Tab title="Using API">
        Here’s how to use Plivo APIs to send outbound SMS text messages.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send-sms-api.jpg?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=6695185c1771e4583e7c0a45112c8cbf" alt="Send SMS" width="1446" height="774" data-path="images/send-sms-api.jpg" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-api-messaging/).

        ## Create the send SMS application

        In Visual Studio, in the CS project, open the file `Program.cs` and paste into it this code.

        ```cs  theme={null}
        using System;
        using System.Collections.Generic;
        using Plivo;

        namespace PlivoExamples
        {
            internal class Program
            {
                public static void Main(string[] args)
                {
                    var api = new PlivoApi("<auth_id>","<auth_token>");
                    var response = api.Message.Create(
                        src: "<sender_id>",
                        dst: "<destination_number>",
                        text: "Hello, from .NET!"
                        );
                    Console.WriteLine(response);
                }
            }
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164)(for example, +12025551234). In countries other than the US and Canada you can use a [sender ID](/messaging/concepts/sender-id-usage/) for the message source. You must have a Plivo phone number to send messages to the US or Canada; you can buy a Plivo number from Phone Numbers > [Buy Numbers](https://cx.plivo.com/phone-numbers) on the Plivo console or via the [Numbers API](/numbers/api/phone-number/#buy-a-phone-number).

        <Note>
          <strong>Note:</strong>
          We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use the <a href="https://docs.microsoft.com/en-us/dotnet/api/system.environment.setenvironmentvariable?view=netcore-3.1">Environment.SetEnvironmentVariable</a> method to store environment variables and <a href="https://docs.microsoft.com/en-us/dotnet/api/system.environment.getenvironmentvariable?view=netcore-3.1">Environment.GetEnvironmentVariable</a> to fetch them when initializing the client.
        </Note>

        ## Test

        Save the file and run it.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to send an SMS text message to any phone number. Businesses send text messages to notify customers about recent information, send alerts, and provide delivery status updates, among other use cases.

    You can start sending SMS messages either by using our PHLO visual workflow builder or our APIs. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to send an SMS text message with a few clicks on the PHLO canvas and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send-sms-phlo.jpg?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=57bb1cf875132c19f7d9a525a124eff6" alt="Send SMS" width="1446" height="774" data-path="images/send-sms-phlo.jpg" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Java, follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
          <video autoplay loop muted inline width="560" height="315">
            <source width="560" height="315" src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send_sms.mp4?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=a30fc7cf0f8b8fed34d78daf6794da36" type="video/mp4" data-path="images/send_sms.mp4" />
          </video>
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left-hand side, drag and drop the **Send Message** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s  **API Request** trigger state to the **Send Message** node.

        * In the Configuration pane at the right of the canvas, configure the **Send Message** node with a sender ID in the **From** field. Enter the destination number you wish to send a message to in the **To** field. Put your message in the **Text** field.

          <Note>
            <strong>Note:</strong> You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through <a href="https://shopify.github.io/liquid/">Liquid</a> templating parameters when you trigger the PHLO from your application.
          </Note>

        * Once you’ve configured the node, click **Validate** to save the configuration.

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
          <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

        Create a Java class in the project  `TriggerPhlo` and paste into it this code.

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
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send_sms_access_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=7af235ce77dc4dea5de829ca38d2e76f" alt="" width="1439" height="818" data-path="images/send_sms_access_payload.png" />
        </Frame>

        #### Code

        Create a Java class in the project `TriggerPhlo` and paste into it this code.

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
                payload.put("From", "<sender_id>");
                payload.put("To", "<destination_number>");
                PhloUpdateResponse response = Phlo.updater(phloId).payload(payload).run();
            }
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.
      </Tab>

      <Tab title="Using API">
        Here’s how to use Plivo APIs to send outbound SMS text messages.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send-sms-api.jpg?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=6695185c1771e4583e7c0a45112c8cbf" alt="Send SMS" width="1446" height="774" data-path="images/send-sms-api.jpg" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-api-messaging/).

        ## Create the send SMS application

        Create a Java class called `SendSMS` and paste into it this code.

        ```java  theme={null}
        import java.io.IOException;
        import java.net.URL;
        import java.util.Collections;

        import com.plivo.api.Plivo;
        import com.plivo.api.exceptions.PlivoRestException;
        import com.plivo.api.models.message.Message;
        import com.plivo.api.models.message.MessageCreateResponse;

        class SendSMS
        {
            public static void main(String [] args)
            {
                Plivo.init("<auth_id>","<auth_token>");
                    MessageCreateResponse response = Message.creator("<sender_id>","<destination_number>",
                            "Hello, from Java!")
                            .create();
                    System.out.println(response);
            }
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). In countries other than the US and Canada you can use a [sender ID](/messaging/concepts/sender-id-usage/) for the message source. You must have a Plivo phone number to send messages to the US or Canada; you can buy a Plivo number from Phone Numbers > [Buy Numbers](https://cx.plivo.com/phone-numbers) on the Plivo console or via the [Numbers API](/numbers/api/phone-number/#buy-a-phone-number).

        <Note>
          <strong>Note:</strong>
          We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `<a rel="nofollow" href="https://docs.oracle.com/javase/tutorial/essential/environment/env.html">System.getenv()</a>` to store and retrieve environment variables when initializing the client.
        </Note>

        ## Test
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to send an SMS text message to any phone number. Businesses send text messages to notify customers about recent information, send alerts, and provide delivery status updates, among other use cases.

    You can start sending SMS messages either by using our PHLO visual workflow builder or our APIs. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to send an SMS text message with a few clicks on the PHLO canvas and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send-sms-phlo.jpg?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=57bb1cf875132c19f7d9a525a124eff6" alt="Send SMS" width="1446" height="774" data-path="images/send-sms-phlo.jpg" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Go, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
          <video autoplay loop muted inline width="560" height="315">
            <source width="560" height="315" src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send_sms.mp4?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=a30fc7cf0f8b8fed34d78daf6794da36" type="video/mp4" data-path="images/send_sms.mp4" />
          </video>
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left-hand side, drag and drop the **Send Message** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s  **API Request** trigger state to the **Send Message** node.

        * In the Configuration pane at the right of the canvas, configure the **Send Message** node with a sender ID in the **From** field. Enter the destination number you wish to send a message to in the **To** field. Put your message in the **Text** field.

          <Note>
            <strong>Note:</strong> You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through <a href="https://shopify.github.io/liquid/">Liquid</a> templating parameters when you trigger the PHLO from your application.
          </Note>

        * Once you’ve configured the node, click **Validate** to save the configuration.

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
          <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

        Create a file called `TriggerPhlo.go` and paste into it this code.

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

        ### With a dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code when you trigger it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send_sms_access_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=7af235ce77dc4dea5de829ca38d2e76f" alt="" width="1439" height="818" data-path="images/send_sms_access_payload.png" />
        </Frame>

        #### Code

        Create a file called `TriggerPhlo.go` and paste into it this code.

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
        		"From": "<sender_id>",
        		"To":   "<destination_number>",
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

      <Tab title="Using API">
        Here’s how to use Plivo APIs to send outbound SMS text messages.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send-sms-api.jpg?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=6695185c1771e4583e7c0a45112c8cbf" alt="Send SMS" width="1446" height="774" data-path="images/send-sms-api.jpg" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-messaging/).

        ## Create the send SMS application

        Create a file called `SendSMS.go` and paste into it this code.

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
        	response, err := client.Messages.Create(
        		plivo.MessageCreateParams{
        			Src: "<sender_id>",
        			Dst: "<destination_number>",
        			Text: "Hello, from Go!",
        		},
        	)
        	if err != nil {
        			fmt.Print("Error", err.Error())
        			return
        		}
        	fmt.Printf("Response: %#v\n", response)
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). In countries other than the US and Canada you can use a [sender ID](/messaging/concepts/sender-id-usage/) for the message source. You must have a Plivo phone number to send messages to the US or Canada; you can buy a Plivo number from Phone Numbers > [Buy Numbers](https://cx.plivo.com/phone-numbers) on the Plivo console or via the [Numbers API](/numbers/api/phone-number/#buy-a-phone-number).

        <Note>
          <strong>Note:</strong>
          We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `os.Setenv` and `os.Getenv` functions to store environment variables and fetch them when initializing the client.
        </Note>

        ## Test

        Save the file and run it.

        ```shell  theme={null}
        go run SendSMS.go
        ```
      </Tab>
    </Tabs>
  </Tab>
</Tabs>
