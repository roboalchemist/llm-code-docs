# Source: https://plivo.com/docs/voice/use-cases/screen-incoming-calls.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Screen Incoming Calls

> Block calls from specific phone numbers or country codes

<Tabs>
  <Tab title="Node">
    ## Overview

    When you don’t want to receive calls from a specific phone number or even a whole country, follow the instructions in this guide to create an application to block phone numbers or country codes associated with incoming calls.

    You can screen incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to screen inbound calls with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screencalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=e8468d10ae62f554bea8a7918ca86682" alt="Screen Incoming Calls Call Flow" width="1448" height="774" data-path="images/screencalls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create a PHLO to block a specific number

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        You can create a PHLO to block a specific number or a whole country. This first example shows how to block a specific number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screen-number.gif?s=c5faa9f0b07fc720df358b750699fa7a" alt="Create the PHLO to Block calls from a specific number" width="1024" height="562" data-path="images/screen-number.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Branch** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Branch** node.

          The branch component splits a workflow by comparing a variable with a value. Based on the conditions, the execution branches into different workflows. In this case, we compare the “from” number to a specific phone number to block.

          In the Configuration panel, enter the caller ID variable `{{ "{{Start.call.from" }}}}` in **Variable to compare** field.

          In **Operation**, select “Is equal to” from the drop-down list.

          In the final field, enter a value to compare: in this case a phone number — for example, 1-202-555-1234.

        * The branch component has two output nodes:

          * **No Match**: When the values do not match
          * **Condition1**: When the condition matches

          <Note>
            <strong>Note:</strong> Condition field names are editable. You can change the name if you have multiple values to compare. This makes a PHLO easier to understand.
          </Note>

        * Drag and drop the **Call forwarding** component onto the canvas and connect **No Match** to it.

        * You can leave the **Condition1** node empty or attach it to the **Hangup** component. The calls will be blocked in either case.

        * Click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Create a PHLO to block a country

        This example shows how to block calls from a whole country.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screen-country.gif?s=3f9e0d797aa73782b3eb11df70703076" alt="Create the PHLO to Block calls from a specific number" width="1024" height="562" data-path="images/screen-country.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Branch** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Branch** node.

          The branch component splits a workflow by comparing a variable with a value. Based on the conditions, the execution branches into different workflows. In this case, we compare the [two-character ISO country code](https://en.wikipedia.org/wiki/ISO_3166-2) to block calls from a specific country.

          In the Configuration panel, enter the ISO code variable `{{ "{{Start.call.from_iso2" }}}}` in **Variable to compare** field.

          In **Operation**, select “Is equal to” from the drop-down list.

          In the final field, enter a value to compare: in this case the ISO code for the country you want to block.

        * The branch component has two output nodes:

          * **No Match**: When the values do not match
          * **Condition1**: When the condition matches

          <Note>
            <strong>Note:</strong> Condition field names are editable. You can change the name if you have multiple values to compare. This makes a PHLO easier to understand.
          </Note>

        * Drag and drop the **Call forwarding** component onto the canvas and connect **No Match** to it.

        * You can choose to leave the **Condition1** node empty or attach it to the **Hangup** component. The calls will be blocked in either case.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_screen.gif?s=c9f05e5c5a0513a04de336edc46935c7" alt="Configure the PHLO to your Plivo Number" width="1024" height="562" data-path="images/assign_screen.gif" />
        </Frame>

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        ## Test

        You can now make a call to your Plivo phone number from a blocked phone number or country and see that the call is rejected. If you make a call from any other number, the call should be forwarded as specified in the PHLO.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that screens incoming calls on a Plivo number.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screencalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=e8468d10ae62f554bea8a7918ca86682" alt="Inbound Call Flow" width="1448" height="774" data-path="images/screencalls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, we check whether the number has been blacklisted. If it has, we reject the call using the [Hangup](/voice/xml/hangup/) XML element. If the phone number hasn't been blacklisted, we return a [Speak](/voice/xml/speak/) XML element that says, “Hello, how are you today.”

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an Express server to screen incoming calls

        Create a file called `screen_call.js` and paste into it this code.

        ```js  theme={null}
        var plivo = require('plivo');
        var express = require('express');
        var bodyParser = require('body-parser');
        var app = express();

        app.use(bodyParser.urlencoded({extended: true}));
        app.set('port', (process.env.PORT || 5000));

        app.all('/screen_call/', function(request, response) {
            var blacklist = [ '<phone_number1>', '<phone_number2>', '<phone_number3>'];
            // Get the caller's phone number from the 'From' parameter
            var from_number = request.query.From || request.body.From;
            var r = plivo.Response();
            if (blacklist.indexOf(from_number) === -1){
                var body = "Hello, how are you today";
                r.addSpeak(body);
            } else {
                //Specify the reason for hangup

                var params = {'reason': "rejected"};
                r.addHangup(params);
            }
            console.log (r.toXML());
            response.set({'Content-Type': 'text/xml'});
            response.send(r.toXML());
        });

        app.listen(app.get('port'), function() {
            console.log('Node app is running on port', app.get('port'));
        });
        ```

        Replace the phone number placeholders with actual phone numbers (for example, 12025551234).

        ## Create a Plivo application to screen calls

        Associate the Express server you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Screen Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/screen_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_screencall.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=d1a63cef317b163ec438f9723a63fc4c" alt="Create Screencall Application" width="1440" height="805" data-path="images/create_screencall.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Screen Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_screencall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=4f1b628fda49934c679d4615bd5a9886" alt="Assign Screen call Application" width="1440" height="704" data-path="images/assign_screencall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides. If your phone number is not blacklisted, the call will go through and you should hear, “Hello, how are you today.”
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Ruby">
    ## Overview

    When you don’t want to receive calls from a specific phone number or even a whole country, follow the instructions in this guide to create an application to block phone numbers or country codes associated with incoming calls.

    You can screen incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to screen inbound calls with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screencalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=e8468d10ae62f554bea8a7918ca86682" alt="Screen Incoming Calls Call Flow" width="1448" height="774" data-path="images/screencalls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create a PHLO to block a specific number

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        You can create a PHLO to block a specific number or a whole country. This first example shows how to block a specific number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screen-number.gif?s=c5faa9f0b07fc720df358b750699fa7a" alt="Create the PHLO to Block calls from a specific number" width="1024" height="562" data-path="images/screen-number.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Branch** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Branch** node.

          The branch component splits a workflow by comparing a variable with a value. Based on the conditions, the execution branches into different workflows. In this case, we compare the “from” number to a specific phone number to block.

          In the Configuration panel, enter the caller ID variable `{{ "{{Start.call.from" }}}}` in **Variable to compare** field.

          In **Operation**, select “Is equal to” from the drop-down list.

          In the final field, enter a value to compare: in this case a phone number — for example, 1-202-555-1234.

        * The branch component has two output nodes:

          * **No Match**: When the values do not match
          * **Condition1**: When the condition matches

          <Note>
            <strong>Note:</strong> Condition field names are editable. You can change the name if you have multiple values to compare. This makes a PHLO easier to understand.
          </Note>

        * Drag and drop the **Call forwarding** component onto the canvas and connect **No Match** to it.

        * You can leave the **Condition1** node empty or attach it to the **Hangup** component. The calls will be blocked in either case.

        * Click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Create a PHLO to block a country

        This example shows how to block calls from a whole country.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screen-country.gif?s=3f9e0d797aa73782b3eb11df70703076" alt="Create the PHLO to Block calls from a specific number" width="1024" height="562" data-path="images/screen-country.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Branch** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Branch** node.

          The branch component splits a workflow by comparing a variable with a value. Based on the conditions, the execution branches into different workflows. In this case, we compare the [two-character ISO country code](https://en.wikipedia.org/wiki/ISO_3166-2) to block calls from a specific country.

          In the Configuration panel, enter the ISO code variable `{{ "{{Start.call.from_iso2" }}}}` in **Variable to compare** field.

          In **Operation**, select “Is equal to” from the drop-down list.

          In the final field, enter a value to compare: in this case the ISO code for the country you want to block.

        * The branch component has two output nodes:

          * **No Match**: When the values do not match
          * **Condition1**: When the condition matches

          <Note>
            <strong>Note:</strong> Condition field names are editable. You can change the name if you have multiple values to compare. This makes a PHLO easier to understand.
          </Note>

        * Drag and drop the **Call forwarding** component onto the canvas and connect **No Match** to it.

        * You can choose to leave the **Condition1** node empty or attach it to the **Hangup** component. The calls will be blocked in either case.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_screen.gif?s=c9f05e5c5a0513a04de336edc46935c7" alt="Configure the PHLO to your Plivo Number" width="1024" height="562" data-path="images/assign_screen.gif" />
        </Frame>

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        ## Test

        You can now make a call to your Plivo phone number from a blocked phone number or country and see that the call is rejected. If you make a call from any other number, the call should be forwarded as specified in the PHLO.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that screens incoming calls on a Plivo number.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screencalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=e8468d10ae62f554bea8a7918ca86682" alt="Inbound Call Flow" width="1448" height="774" data-path="images/screencalls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, we check whether the number has been blacklisted. If it has, we reject the call using the [Hangup](/voice/xml/hangup/) XML element. If the phone number hasn't been blacklisted, we return a [Speak](/voice/xml/speak/) XML element that says, “Hello, how are you today.”

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Rails controller to screen incoming calls

        Change to the project directory and run this command to create a Rails controller to screen incoming calls.

        ```shell  theme={null}
        $ rails generate controller Plivo voice
        ```

        This command generates a controller named plivo\_controller in the app/controllers/ directory, and a view will be generated in app/views/plivo directory. We can delete the view as we don’t need it.

        ```shell  theme={null}
        $ rm app/views/plivo/voice.html.erb
        ```

        Open the file app/controllers/plivo\_controller.rb and paste this code in the PlivoController class:

        ```rb  theme={null}
        include Plivo
        include Plivo::XML
        include Plivo::Exceptions

        class PlivoController < ApplicationController
         def screen
            blacklist = ['<phone_number1>', '<phone_number2>', '<phone_number3>']

            from_number = params[:From]
            r = Response.new()

            if blacklist.include? from_number
                # Specify the reason for hangup
                params = {
                    reason: 'rejected'
                }
                r.addHangup(params)
            else
                r.addSpeak('Hello, how are you today')
            end
            xml = Plivo::PlivoXML.new(r)
            render xml: xml.to_xml
         end
        end
        ```

        Replace the phone number placeholders with actual phone numbers (for example, 12025551234).

        ## Create a Plivo application to screen calls

        Associate the Rails server you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Screen Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/screen_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_screencall.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=d1a63cef317b163ec438f9723a63fc4c" alt="Create Screencall Application" width="1440" height="805" data-path="images/create_screencall.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Screen Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_screencall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=4f1b628fda49934c679d4615bd5a9886" alt="Assign Screen call Application" width="1440" height="704" data-path="images/assign_screencall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides. If your phone number is not blacklisted, the call will go through and you should hear, “Hello, how are you today.”
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Python">
    ## Overview

    When you don’t want to receive calls from a specific phone number or even a whole country, follow the instructions in this guide to create an application to block phone numbers or country codes associated with incoming calls.

    You can screen incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to screen inbound calls with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screencalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=e8468d10ae62f554bea8a7918ca86682" alt="Screen Incoming Calls Call Flow" width="1448" height="774" data-path="images/screencalls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create a PHLO to block a specific number

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        You can create a PHLO to block a specific number or a whole country. This first example shows how to block a specific number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screen-number.gif?s=c5faa9f0b07fc720df358b750699fa7a" alt="Create the PHLO to Block calls from a specific number" width="1024" height="562" data-path="images/screen-number.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Branch** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Branch** node.

          The branch component splits a workflow by comparing a variable with a value. Based on the conditions, the execution branches into different workflows. In this case, we compare the “from” number to a specific phone number to block.

          In the Configuration panel, enter the caller ID variable `{{ "{{Start.call.from" }}}}` in **Variable to compare** field.

          In **Operation**, select “Is equal to” from the drop-down list.

          In the final field, enter a value to compare: in this case a phone number — for example, 1-202-555-1234.

        * The branch component has two output nodes:

          * **No Match**: When the values do not match
          * **Condition1**: When the condition matches

          <Note>
            <strong>Note:</strong> Condition field names are editable. You can change the name if you have multiple values to compare. This makes a PHLO easier to understand.
          </Note>

        * Drag and drop the **Call forwarding** component onto the canvas and connect **No Match** to it.

        * You can leave the **Condition1** node empty or attach it to the **Hangup** component. The calls will be blocked in either case.

        * Click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Create a PHLO to block a country

        This example shows how to block calls from a whole country.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screen-country.gif?s=3f9e0d797aa73782b3eb11df70703076" alt="Create the PHLO to Block calls from a specific number" width="1024" height="562" data-path="images/screen-country.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Branch** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Branch** node.

          The branch component splits a workflow by comparing a variable with a value. Based on the conditions, the execution branches into different workflows. In this case, we compare the [two-character ISO country code](https://en.wikipedia.org/wiki/ISO_3166-2) to block calls from a specific country.

          In the Configuration panel, enter the ISO code variable `{{ "{{Start.call.from_iso2" }}}}` in **Variable to compare** field.

          In **Operation**, select “Is equal to” from the drop-down list.

          In the final field, enter a value to compare: in this case the ISO code for the country you want to block.

        * The branch component has two output nodes:

          * **No Match**: When the values do not match
          * **Condition1**: When the condition matches

          <Note>
            <strong>Note:</strong> Condition field names are editable. You can change the name if you have multiple values to compare. This makes a PHLO easier to understand.
          </Note>

        * Drag and drop the **Call forwarding** component onto the canvas and connect **No Match** to it.

        * You can choose to leave the **Condition1** node empty or attach it to the **Hangup** component. The calls will be blocked in either case.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_screen.gif?s=c9f05e5c5a0513a04de336edc46935c7" alt="Configure the PHLO to your Plivo Number" width="1024" height="562" data-path="images/assign_screen.gif" />
        </Frame>

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        ## Test

        You can now make a call to your Plivo phone number from a blocked phone number or country and see that the call is rejected. If you make a call from any other number, the call should be forwarded as specified in the PHLO.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that screens incoming calls on a Plivo number.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screencalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=e8468d10ae62f554bea8a7918ca86682" alt="Inbound Call Flow" width="1448" height="774" data-path="images/screencalls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, we check whether the number has been blacklisted. If it has, we reject the call using the [Hangup](/voice/xml/hangup/) XML element. If the phone number hasn't been blacklisted, we return a [Speak](/voice/xml/speak/) XML element that says, “Hello, how are you today.”

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Flask application to screen incoming calls

        Create a file called `screen_call.py` and paste into it this code.

        ```py  theme={null}
        from flask import Flask, Response
        from flask import request
        from plivo import plivoxml

        app = Flask(__name__)

        @app.route('/screen_call/', methods=['GET', 'POST'])
        def screen_call():

            blacklist = ['<phone_number1>','<phone_number2>','<phone_number3>']
            from_number = request.values.get('From')
            response = plivoxml.ResponseElement()

            if from_number in blacklist:
                params = {'reason': 'rejected'}
                response.add(plivoxml.HangupElement(**params))
            else:
                response.add(plivoxml.SpeakElement('Hello, how are you today'))
            return Response(response.to_string(), mimetype='application/xml')

        if __name__ == "__main__":
            app.run(host='0.0.0.0', debug=True)
        ```

        Replace the phone number placeholders with actual phone numbers (for example, 12025551234).

        ## Create a Plivo application to screen calls

        Associate the Flask application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Screen Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/screen_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_screencall.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=d1a63cef317b163ec438f9723a63fc4c" alt="Create Screencall Application" width="1440" height="805" data-path="images/create_screencall.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Screen Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_screencall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=4f1b628fda49934c679d4615bd5a9886" alt="Assign Screen call Application" width="1440" height="704" data-path="images/assign_screencall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides. If your phone number is not blacklisted, the call will go through and you should hear, “Hello, how are you today.”
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="PHP">
    ## Overview

    When you don’t want to receive calls from a specific phone number or even a whole country, follow the instructions in this guide to create an application to block phone numbers or country codes associated with incoming calls.

    You can screen incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to screen inbound calls with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screencalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=e8468d10ae62f554bea8a7918ca86682" alt="Screen Incoming Calls Call Flow" width="1448" height="774" data-path="images/screencalls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create a PHLO to block a specific number

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        You can create a PHLO to block a specific number or a whole country. This first example shows how to block a specific number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screen-number.gif?s=c5faa9f0b07fc720df358b750699fa7a" alt="Create the PHLO to Block calls from a specific number" width="1024" height="562" data-path="images/screen-number.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Branch** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Branch** node.

          The branch component splits a workflow by comparing a variable with a value. Based on the conditions, the execution branches into different workflows. In this case, we compare the “from” number to a specific phone number to block.

          In the Configuration panel, enter the caller ID variable `{{ "{{Start.call.from" }}}}` in **Variable to compare** field.

          In **Operation**, select “Is equal to” from the drop-down list.

          In the final field, enter a value to compare: in this case a phone number — for example, 1-202-555-1234.

        * The branch component has two output nodes:

          * **No Match**: When the values do not match
          * **Condition1**: When the condition matches

          <Note>
            <strong>Note:</strong> Condition field names are editable. You can change the name if you have multiple values to compare. This makes a PHLO easier to understand.
          </Note>

        * Drag and drop the **Call forwarding** component onto the canvas and connect **No Match** to it.

        * You can leave the **Condition1** node empty or attach it to the **Hangup** component. The calls will be blocked in either case.

        * Click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Create a PHLO to block a country

        This example shows how to block calls from a whole country.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screen-country.gif?s=3f9e0d797aa73782b3eb11df70703076" alt="Create the PHLO to Block calls from a specific number" width="1024" height="562" data-path="images/screen-country.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Branch** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Branch** node.

          The branch component splits a workflow by comparing a variable with a value. Based on the conditions, the execution branches into different workflows. In this case, we compare the [two-character ISO country code](https://en.wikipedia.org/wiki/ISO_3166-2) to block calls from a specific country.

          In the Configuration panel, enter the ISO code variable `{{ "{{Start.call.from_iso2" }}}}` in **Variable to compare** field.

          In **Operation**, select “Is equal to” from the drop-down list.

          In the final field, enter a value to compare: in this case the ISO code for the country you want to block.

        * The branch component has two output nodes:

          * **No Match**: When the values do not match
          * **Condition1**: When the condition matches

          <Note>
            <strong>Note:</strong> Condition field names are editable. You can change the name if you have multiple values to compare. This makes a PHLO easier to understand.
          </Note>

        * Drag and drop the **Call forwarding** component onto the canvas and connect **No Match** to it.

        * You can choose to leave the **Condition1** node empty or attach it to the **Hangup** component. The calls will be blocked in either case.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_screen.gif?s=c9f05e5c5a0513a04de336edc46935c7" alt="Configure the PHLO to your Plivo Number" width="1024" height="562" data-path="images/assign_screen.gif" />
        </Frame>

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        ## Test

        You can now make a call to your Plivo phone number from a blocked phone number or country and see that the call is rejected. If you make a call from any other number, the call should be forwarded as specified in the PHLO.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that screens incoming calls on a Plivo number.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screencalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=e8468d10ae62f554bea8a7918ca86682" alt="Inbound Call Flow" width="1448" height="774" data-path="images/screencalls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, we check whether the number has been blacklisted. If it has, we reject the call using the [Hangup](/voice/xml/hangup/) XML element. If the phone number hasn't been blacklisted, we return a [Speak](/voice/xml/speak/) XML element that says, “Hello, how are you today.”

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Laravel controller to screen incoming calls

        Change to the project directory and run this command to create a Laravel controller to screen inbound calls.

        ```shell  theme={null}
        $ php artisan make:controller VoiceController
        ```

        The command generates a controller named VoiceController in the app/http/controllers/ directory. Edit the app/http/controllers/voiceController.php file and paste into it this code.

        ```php  theme={null}
        <?php

        namespace App\Http\Controllers;
        require '../../vendor/autoload.php';
        use Plivo\RestClient;
        use Plivo\XML\Response;
        use Illuminate\Http\Request;

        class VoiceController extends Controller
        {
            // Speak XML to handle your first incoming call
            public function screenCall()
            {
              $from_number = $_REQUEST['From'];
              $blacklist = array('<phone_number1>', '<phone_number2>', '<phone_number3>');
              $r = new Response();
              if (in_array($from_number, $blacklist)) {
                 $params = array('reason' => 'rejected');
                 $r->addHangup($params);
              } else {
                 $body = "Hello, how are you today";
                 $r->addSpeak($body);
              }
              Header('Content-type: text/xml');
              echo $r->toXML();
            }
        }
        ```

        Replace the phone number placeholders with actual phone numbers (for example, 12025551234).

        ## Create a Plivo application to screen calls

        Associate the Laravel controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Screen Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/screen_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_screencall.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=d1a63cef317b163ec438f9723a63fc4c" alt="Create Screencall Application" width="1440" height="805" data-path="images/create_screencall.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Screen Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_screencall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=4f1b628fda49934c679d4615bd5a9886" alt="Assign Screen call Application" width="1440" height="704" data-path="images/assign_screencall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides. If your phone number is not blacklisted, the call will go through and you should hear, “Hello, how are you today.”
      </Tab>
    </Tabs>
  </Tab>

  <Tab title=".NET">
    ## Overview

    When you don’t want to receive calls from a specific phone number or even a whole country, follow the instructions in this guide to create an application to block phone numbers or country codes associated with incoming calls.

    You can screen incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to screen inbound calls with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screencalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=e8468d10ae62f554bea8a7918ca86682" alt="Screen Incoming Calls Call Flow" width="1448" height="774" data-path="images/screencalls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create a PHLO to block a specific number

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        You can create a PHLO to block a specific number or a whole country. This first example shows how to block a specific number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screen-number.gif?s=c5faa9f0b07fc720df358b750699fa7a" alt="Create the PHLO to Block calls from a specific number" width="1024" height="562" data-path="images/screen-number.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Branch** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Branch** node.

          The branch component splits a workflow by comparing a variable with a value. Based on the conditions, the execution branches into different workflows. In this case, we compare the “from” number to a specific phone number to block.

          In the Configuration panel, enter the caller ID variable `{{ "{{Start.call.from" }}}}` in **Variable to compare** field.

          In **Operation**, select “Is equal to” from the drop-down list.

          In the final field, enter a value to compare: in this case a phone number — for example, 1-202-555-1234.

        * The branch component has two output nodes:

          * **No Match**: When the values do not match
          * **Condition1**: When the condition matches

          <Note>
            <strong>Note:</strong> Condition field names are editable. You can change the name if you have multiple values to compare. This makes a PHLO easier to understand.
          </Note>

        * Drag and drop the **Call forwarding** component onto the canvas and connect **No Match** to it.

        * You can leave the **Condition1** node empty or attach it to the **Hangup** component. The calls will be blocked in either case.

        * Click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Create a PHLO to block a country

        This example shows how to block calls from a whole country.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screen-country.gif?s=3f9e0d797aa73782b3eb11df70703076" alt="Create the PHLO to Block calls from a specific number" width="1024" height="562" data-path="images/screen-country.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Branch** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Branch** node.

          The branch component splits a workflow by comparing a variable with a value. Based on the conditions, the execution branches into different workflows. In this case, we compare the [two-character ISO country code](https://en.wikipedia.org/wiki/ISO_3166-2) to block calls from a specific country.

          In the Configuration panel, enter the ISO code variable `{{ "{{Start.call.from_iso2" }}}}` in **Variable to compare** field.

          In **Operation**, select “Is equal to” from the drop-down list.

          In the final field, enter a value to compare: in this case the ISO code for the country you want to block.

        * The branch component has two output nodes:

          * **No Match**: When the values do not match
          * **Condition1**: When the condition matches

          <Note>
            <strong>Note:</strong> Condition field names are editable. You can change the name if you have multiple values to compare. This makes a PHLO easier to understand.
          </Note>

        * Drag and drop the **Call forwarding** component onto the canvas and connect **No Match** to it.

        * You can choose to leave the **Condition1** node empty or attach it to the **Hangup** component. The calls will be blocked in either case.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_screen.gif?s=c9f05e5c5a0513a04de336edc46935c7" alt="Configure the PHLO to your Plivo Number" width="1024" height="562" data-path="images/assign_screen.gif" />
        </Frame>

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        ## Test

        You can now make a call to your Plivo phone number from a blocked phone number or country and see that the call is rejected. If you make a call from any other number, the call should be forwarded as specified in the PHLO.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that screens incoming calls on a Plivo number.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screencalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=e8468d10ae62f554bea8a7918ca86682" alt="Inbound Call Flow" width="1448" height="774" data-path="images/screencalls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, we check whether the number has been blacklisted. If it has, we reject the call using the [Hangup](/voice/xml/hangup/) XML element. If the phone number hasn't been blacklisted, we return a [Speak](/voice/xml/speak/) XML element that says, “Hello, how are you today.”

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an MVC controller to screen incoming calls

        In Visual Studio, create a new project. Use the template for Web Application (Model-View-Controller).

        <Frame>
                    <img src="https://mintlify.s3.us-west-1.amazonaws.com/plivo/images/create_mvcapp.jpg" alt="Create an MVC app" />
        </Frame>

        Give the project a name — we used `Screencall`.

        Navigate to Controllers directory in the Screencall project. Create a controller named ScreencallController.cs and paste into it this code.

        ```cs  theme={null}
        using System;
        using System.Collections.Generic;
        using Plivo.XML;
        using Microsoft.AspNetCore.Mvc;

        namespace Screencall.Controllers
        {
            public class ScreencallController : Controller
            {
                // GET: /<controller>/
                public IActionResult Index()
                {
                    string[] blacklist = { "<phone_number1>", "<phone_number2>", "<phone_number3>" };
                    string fromNumber = Request.Query["From"];
                    Plivo.XML.Response resp = new Plivo.XML.Response();

                    if (blacklist.Equals(fromNumber))
                    {
                        resp.AddHangup(new Dictionary<string, string>()
                    {
                        {"reason","rejected"}, // Specify the reason for hangup
                    });
                    }
                    else
                    {
                        resp.AddSpeak("Hello, how are you today", new Dictionary<string, string>() { });
                    }
                    var output = resp.ToString();
                    return this.Content(output, "text/xml");
                }
            }
        }
        ```

        Replace the phone number placeholders with actual phone numbers (for example, 12025551234).

        ## Create a Plivo application to screen calls

        Associate the controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Screen Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/screen_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_screencall.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=d1a63cef317b163ec438f9723a63fc4c" alt="Create Screencall Application" width="1440" height="805" data-path="images/create_screencall.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Screen Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_screencall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=4f1b628fda49934c679d4615bd5a9886" alt="Assign Screen call Application" width="1440" height="704" data-path="images/assign_screencall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides. If your phone number is not blacklisted, the call will go through and you should hear, “Hello, how are you today.”
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Java">
    ## Overview

    When you don’t want to receive calls from a specific phone number or even a whole country, follow the instructions in this guide to create an application to block phone numbers or country codes associated with incoming calls.

    You can screen incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to screen inbound calls with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screencalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=e8468d10ae62f554bea8a7918ca86682" alt="Screen Incoming Calls Call Flow" width="1448" height="774" data-path="images/screencalls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create a PHLO to block a specific number

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        You can create a PHLO to block a specific number or a whole country. This first example shows how to block a specific number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screen-number.gif?s=c5faa9f0b07fc720df358b750699fa7a" alt="Create the PHLO to Block calls from a specific number" width="1024" height="562" data-path="images/screen-number.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Branch** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Branch** node.

          The branch component splits a workflow by comparing a variable with a value. Based on the conditions, the execution branches into different workflows. In this case, we compare the “from” number to a specific phone number to block.

          In the Configuration panel, enter the caller ID variable `{{ "{{Start.call.from" }}}}` in **Variable to compare** field.

          In **Operation**, select “Is equal to” from the drop-down list.

          In the final field, enter a value to compare: in this case a phone number — for example, 1-202-555-1234.

        * The branch component has two output nodes:

          * **No Match**: When the values do not match
          * **Condition1**: When the condition matches

          <Note>
            <strong>Note:</strong> Condition field names are editable. You can change the name if you have multiple values to compare. This makes a PHLO easier to understand.
          </Note>

        * Drag and drop the **Call forwarding** component onto the canvas and connect **No Match** to it.

        * You can leave the **Condition1** node empty or attach it to the **Hangup** component. The calls will be blocked in either case.

        * Click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Create a PHLO to block a country

        This example shows how to block calls from a whole country.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screen-country.gif?s=3f9e0d797aa73782b3eb11df70703076" alt="Create the PHLO to Block calls from a specific number" width="1024" height="562" data-path="images/screen-country.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Branch** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Branch** node.

          The branch component splits a workflow by comparing a variable with a value. Based on the conditions, the execution branches into different workflows. In this case, we compare the [two-character ISO country code](https://en.wikipedia.org/wiki/ISO_3166-2) to block calls from a specific country.

          In the Configuration panel, enter the ISO code variable `{{ "{{Start.call.from_iso2" }}}}` in **Variable to compare** field.

          In **Operation**, select “Is equal to” from the drop-down list.

          In the final field, enter a value to compare: in this case the ISO code for the country you want to block.

        * The branch component has two output nodes:

          * **No Match**: When the values do not match
          * **Condition1**: When the condition matches

          <Note>
            <strong>Note:</strong> Condition field names are editable. You can change the name if you have multiple values to compare. This makes a PHLO easier to understand.
          </Note>

        * Drag and drop the **Call forwarding** component onto the canvas and connect **No Match** to it.

        * You can choose to leave the **Condition1** node empty or attach it to the **Hangup** component. The calls will be blocked in either case.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_screen.gif?s=c9f05e5c5a0513a04de336edc46935c7" alt="Configure the PHLO to your Plivo Number" width="1024" height="562" data-path="images/assign_screen.gif" />
        </Frame>

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        ## Test

        You can now make a call to your Plivo phone number from a blocked phone number or country and see that the call is rejected. If you make a call from any other number, the call should be forwarded as specified in the PHLO.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that screens incoming calls on a Plivo number.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screencalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=e8468d10ae62f554bea8a7918ca86682" alt="Inbound Call Flow" width="1448" height="774" data-path="images/screencalls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, we check whether the number has been blacklisted. If it has, we reject the call using the [Hangup](/voice/xml/hangup/) XML element. If the phone number hasn't been blacklisted, we return a [Speak](/voice/xml/speak/) XML element that says, “Hello, how are you today.”

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Spark application to screen incoming calls

        Create a Java class named `ScreenCall` and paste into it this code.

        ```java  theme={null}
        import java.util.Arrays;
        import com.plivo.api.xml.Hangup;
        import com.plivo.api.xml.Response;
        import com.plivo.api.xml.Speak;
        import static spark.Spark.*;

        public class screencalls {
            public static void main(String[] args) {
                post("/screen_call/", (request, response) -> {
                    response.type("application/xml");
                    String fromNumber = request.queryParams("From");
                    String[] blacklist = { "<phone_number1>","<phone_number2>", "<phone_number3>"};
                if (Arrays.asList(blacklist).contains(fromNumber)) {
                    return new Response()
                            .children(
                                    new Hangup()
                                            .reason("rejected")
                            ).toXmlString();
                } else {
                    return new Response()
                            .children(
                                    new Speak("Hello, how are you today")
                            ).toXmlString();
                }
                });
            }
        }
        ```

        Replace the phone number placeholders with actual phone numbers (for example, 12025551234).

        ## Create a Plivo application to screen calls

        Associate the Spark application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Screen Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/screen_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_screencall.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=d1a63cef317b163ec438f9723a63fc4c" alt="Create Screencall Application" width="1440" height="805" data-path="images/create_screencall.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Screen Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_screencall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=4f1b628fda49934c679d4615bd5a9886" alt="Assign Screen call Application" width="1440" height="704" data-path="images/assign_screencall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides. If your phone number is not blacklisted, the call will go through and you should hear, “Hello, how are you today.”
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Go">
    ## Overview

    When you don’t want to receive calls from a specific phone number or even a whole country, follow the instructions in this guide to create an application to block phone numbers or country codes associated with incoming calls.

    You can screen incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to screen inbound calls with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screencalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=e8468d10ae62f554bea8a7918ca86682" alt="Screen Incoming Calls Call Flow" width="1448" height="774" data-path="images/screencalls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create a PHLO to block a specific number

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        You can create a PHLO to block a specific number or a whole country. This first example shows how to block a specific number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screen-number.gif?s=c5faa9f0b07fc720df358b750699fa7a" alt="Create the PHLO to Block calls from a specific number" width="1024" height="562" data-path="images/screen-number.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Branch** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Branch** node.

          The branch component splits a workflow by comparing a variable with a value. Based on the conditions, the execution branches into different workflows. In this case, we compare the “from” number to a specific phone number to block.

          In the Configuration panel, enter the caller ID variable `{{ "{{Start.call.from" }}}}` in **Variable to compare** field.

          In **Operation**, select “Is equal to” from the drop-down list.

          In the final field, enter a value to compare: in this case a phone number — for example, 1-202-555-1234.

        * The branch component has two output nodes:

          * **No Match**: When the values do not match
          * **Condition1**: When the condition matches

          <Note>
            <strong>Note:</strong> Condition field names are editable. You can change the name if you have multiple values to compare. This makes a PHLO easier to understand.
          </Note>

        * Drag and drop the **Call forwarding** component onto the canvas and connect **No Match** to it.

        * You can leave the **Condition1** node empty or attach it to the **Hangup** component. The calls will be blocked in either case.

        * Click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Create a PHLO to block a country

        This example shows how to block calls from a whole country.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screen-country.gif?s=3f9e0d797aa73782b3eb11df70703076" alt="Create the PHLO to Block calls from a specific number" width="1024" height="562" data-path="images/screen-country.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Branch** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Branch** node.

          The branch component splits a workflow by comparing a variable with a value. Based on the conditions, the execution branches into different workflows. In this case, we compare the [two-character ISO country code](https://en.wikipedia.org/wiki/ISO_3166-2) to block calls from a specific country.

          In the Configuration panel, enter the ISO code variable `{{ "{{Start.call.from_iso2" }}}}` in **Variable to compare** field.

          In **Operation**, select “Is equal to” from the drop-down list.

          In the final field, enter a value to compare: in this case the ISO code for the country you want to block.

        * The branch component has two output nodes:

          * **No Match**: When the values do not match
          * **Condition1**: When the condition matches

          <Note>
            <strong>Note:</strong> Condition field names are editable. You can change the name if you have multiple values to compare. This makes a PHLO easier to understand.
          </Note>

        * Drag and drop the **Call forwarding** component onto the canvas and connect **No Match** to it.

        * You can choose to leave the **Condition1** node empty or attach it to the **Hangup** component. The calls will be blocked in either case.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_screen.gif?s=c9f05e5c5a0513a04de336edc46935c7" alt="Configure the PHLO to your Plivo Number" width="1024" height="562" data-path="images/assign_screen.gif" />
        </Frame>

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        ## Test

        You can now make a call to your Plivo phone number from a blocked phone number or country and see that the call is rejected. If you make a call from any other number, the call should be forwarded as specified in the PHLO.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that screens incoming calls on a Plivo number.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screencalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=e8468d10ae62f554bea8a7918ca86682" alt="Inbound Call Flow" width="1448" height="774" data-path="images/screencalls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, we check whether the number has been blacklisted. If it has, we reject the call using the [Hangup](/voice/xml/hangup/) XML element. If the phone number hasn't been blacklisted, we return a [Speak](/voice/xml/speak/) XML element that says, “Hello, how are you today.”

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Go server to screen incoming calls

        Create a file called `screen_call.go` and paste into it this code.

        ```go  theme={null}
        package main

        import (
        	"github.com/go-martini/martini"
        	"github.com/plivo/plivo-go/v7/xml"
        	"net/http"
        )

        func main() {
        	m := martini.Classic()
        	m.Get("/screen_call", func(w http.ResponseWriter, r *http.Request) string {
        		w.Header().Set("Content-Type", "application/xml")
        		fromNumber := r.FormValue("From")
        		blacklist := []string{"<phone_number1>", "<phone_number2>", "<phone_number3>"}

        ​		for _, num := range blacklist {
        ​			if num == fromNumber {
        ​				return xml.ResponseElement{
        ​					Contents: []interface{}{
        ​						new(xml.HangupElement).
        ​							SetReason("rejected"),
        ​					},
        ​				}.String()
        ​			}
        ​		}
        ​		return xml.ResponseElement{Contents: []interface{}{
        ​			new(xml.SpeakElement).
        ​				SetLoop(0).
        ​				AddSpeak("Hello, how are you today"),
        ​		}}.String()
        ​	})
        ​	m.Run()
        }
        ```

        Replace the phone number placeholders with actual phone numbers (for example, 12025551234).

        ## Create a Plivo application to screen calls

        Associate the Go application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Screen Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/screen_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_screencall.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=d1a63cef317b163ec438f9723a63fc4c" alt="Create Screencall Application" width="1440" height="805" data-path="images/create_screencall.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Screen Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_screencall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=4f1b628fda49934c679d4615bd5a9886" alt="Assign Screen call Application" width="1440" height="704" data-path="images/assign_screencall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides. If your phone number is not blacklisted, the call will go through and you should hear, “Hello, how are you today.”
      </Tab>
    </Tabs>
  </Tab>
</Tabs>
