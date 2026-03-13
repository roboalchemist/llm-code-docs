# Source: https://plivo.com/docs/voice/use-cases/dial-status-reporting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Dial Status Reporting

> Track call status at each stage using webhook-based dial status reporting

<Tabs>
  <Tab title="Node">
    ## Overview

    Plivo passes the call status of an ongoing call so you can decide how to process it. For all the calls made using Plivo’s [Make a Call API](/voice/api/call/#make-a-call) or [Dial XML](/voice/xml/dial/), Plivo sends the call status to the application server at different stages of a call. We send call status as an HTTP webhook request to URLs such as `ring_url`, `answer_url`, `fallback_url`, `action_url`, `callback_url`, and `hangup_url`.

    In each callback, the `CallStatus` parameter takes one of these values:

    <table>
      <tbody>
        <tr>
          <td><strong>in-progress</strong></td>

          <td>
            <p>The call was answered and is in progress. Calls with this status can be terminated using the <a href="/voice/api/call/hangup-a-call/">Hangup API</a>.</p>
          </td>
        </tr>

        <tr>
          <td><strong>completed</strong></td>

          <td>
            <p>The call was completed, terminated either by the Hangup API or by one of the parties in the call.</p>
          </td>
        </tr>

        <tr>
          <td><strong>ringing</strong></td>

          <td>
            <p>The call is ringing. This status is sent to the Ring URL.</p>
          </td>
        </tr>

        <tr>
          <td><strong>no-answer</strong></td>

          <td>
            <p>The call was not answered.</p>
          </td>
        </tr>

        <tr>
          <td><strong>busy</strong></td>

          <td>
            <p>The called line is busy.</p>
          </td>
        </tr>

        <tr>
          <td><strong>cancel</strong></td>

          <td>
            <p>The call was canceled by the caller.</p>
          </td>
        </tr>

        <tr>
          <td><strong>timeout</strong></td>

          <td>
            <p>There was a timeout while connecting your call, caused by either an issue with one of the terminating carriers or network lag in our system.</p>
          </td>
        </tr>
      </tbody>
    </table>

    Plivo sends these parameters to the application server in the webhook:

    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Description</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>`DialRingStatus`</td>
          <td>Indicates whether the dial attempt rang or not. Values: `true`, `false`</td>
        </tr>

        <tr>
          <td>`DialHangupCause`</td>
          <td>The <a href="/voice/troubleshooting/hangup-causes/#list-of-hangup-causes">standard telephony hangup cause</a>.</td>
        </tr>

        <tr>
          <td>`DialStatus`</td>
          <td>Status of the dial. Values: `completed`, `busy`, `failed`, `timeout`, `no-answer`</td>
        </tr>

        <tr>
          <td>`DialALegUUID`</td>
          <td>CallUUID of the A leg.</td>
        </tr>

        <tr>
          <td>`DialBLegUUID`</td>
          <td>CallUUID of the B leg. Empty if nobody answers.</td>
        </tr>
      </tbody>
    </table>

    You can implement dial status reporting either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to handle dial status reporting with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status-reporting.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=128df4ffcabef5e92220b9616eff9f21" alt="Screen Incoming Calls Call Flow" width="1446" height="774" data-path="images/dial-status-reporting.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status.gif?s=3075e34fce686a7f9646d51a76e550d0" alt="Create the PHLO to Block calls from a specific number" width="1024" height="545" data-path="images/dial-status.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Call Forward** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Call Forward** node.

        * In the configuration panel for the **Call Forward** node, enter the caller ID variable `{{ "{{Start.call.from" }}}}` in the **From** field. Enter any numbers you want to call in the **To** field, separated by commas.

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Next, from the list of components, drag and drop the **HTTP Request** component onto the canvas.

        * Draw lines to connect all of the dial status states of the **Call Forward** node (Completed, No Answer, Busy/Rejected, Failed) with the **HTTP Request** node.

        * Configure the **HTTP Request** node. Enter your application server URL in the box next to the HTTP Method (GET/POST) field.

        * Provide key:value pairs of the callback attributes you’re interested in, such as `DialRingStatus`, `DialHangupCause`, `DialStatus`, `DialALegUUID`, and `DialBLegUUID`.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_dialstatus.gif?s=057b7f6972e2a56dbd895d8f08006111" alt="Configure the PHLO to your Plivo Number" width="1024" height="545" data-path="images/assign_dialstatus.gif" />
        </Frame>

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        ## Test

        You can now make a call to your Plivo phone number. After the call ends, Plivo reports back the status via the key:value pairs you specified to the URL you specified.

        For more information about creating a PHLO app, see the [PHLO User Guide](/phlo/).For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to send callback events for dial status reporting.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status-reporting.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=128df4ffcabef5e92220b9616eff9f21" alt="Outbound Call Flow" width="1446" height="774" data-path="images/dial-status-reporting.png" />
        </Frame>

        Plivo requests an answer URL when a Plivo number receives a call (step 2) and expects the file at that URL to be configured in the application assigned to the number to hold a valid XML response with instructions on how to handle the call. For [outbound calls](/voice/use-cases/make-outbound-calls/node/) you specify an answer URL along with the make call API request, and for [incoming calls](/voice/use-cases/receive-incoming-calls/node/) the answer URL is specified in the Plivo application associated with the phone number.

        In addition to requests to the answer URL, Plivo initiates HTTP requests to your application server throughout the course of a call based on specific XML elements and attributes in your answer XML document (step 5). Such requests are broadly classified into two categories:

        **Action URL requests:** These requests are typically  invoked at the end of an XML element’s execution, and the server expects XML instructions to carry forward the call in response to these  requests. This happens, for example, when a caller provides Touch-Tone input during GetInput XML execution.

        **Callback URL requests:** These requests serve as webhooks to pass the application server  information about events through the course of an XML element’s  execution, such as when a conference participant is muted or unmuted. These callback URL requests can be used for dial status reporting. No XML instructions are expected in response to these requests.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an Express server for dial status reporting

        Create a file called `dial_status.js` and paste into it this code.

        ```js  theme={null}
        var plivo = require('plivo');
        var express = require('express');
        var app = express();

        app.set('port', (process.env.PORT || 5000));
        app.use(express.static(__dirname + '/public'));

        app.all('/dialstatus/', function(request, response) {
            var r = plivo.Response();
            var params = {
                'action': "https://<yourdomain>.com/dialstatus/action/",
                'method': "POST",
                'redirect': "true"
            };
            var dial = r.addDial(params);
            var first_number = "<phone_number>";
            dial.addNumber(first_number);
            console.log (r.toXML());
            response.set({
                'Content-Type': 'text/xml'
            });
            response.end(r.toXML());
        });

        app.all('/dialstatus/action/', function(request, response) {
            var status = request.param('Status');
            var aleg = request.param('DialALegUUID');
            var bleg = request.param('DialBLegUUID');

            console.log ('Status : ' + status + ' Aleg UUID  : ' + aleg + ' Bleg UUID : ' + bleg);
        });

        app.listen(app.get('port'), function() {
            console.log('Node app is running on port', app.get('port'));
        });
        ```

        Replace the phone number placeholder with an actual phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        In this code, we tell Plivo to POST the call status to https\://\<yourdomain>.com/dialstatus/.  We set the [redirect attribute](/voice/xml/redirect/), which determines whether to change the call flow of an ongoing call based on the actions performed, to `true`, which tells Plivo to expect a valid XML document to be posted to https\://\<yourdomain>.com/dialstatus/action. The code creates an XML document with a Dial XML element.

        ## Create a Plivo application for dial status reporting

        Associate the Express server you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Dial Status Report`. Enter the server URL you want to use (for example `https://<yourdomain>.com/dialstatus/`) in the `Answer URL` field and set the method to `POST`.  Click on `Create Application` to save your application.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dialstatusreporting.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=a8af3b7e6c4eb5b552a6904de0a6477f" alt="Create dial status application" width="1440" height="805" data-path="images/dialstatusreporting.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Dial Status Report` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_dialstatusreport.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=79cc79bf9d43547163544e04d6062b97" alt="assign dial status application" width="1440" height="785" data-path="images/assign_dialstatusreport.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides, and call details will be posted to your application server via the action and callback URLs you configured throughout the course of the call.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Ruby">
    ## Overview

    Plivo passes the call status of an ongoing call so you can decide how to process it. For all the calls made using Plivo’s [Make a Call API](/voice/api/call/#make-a-call) or [Dial XML](/voice/xml/dial/), Plivo sends the call status to the application server at different stages of a call. We send call status as an HTTP webhook request to URLs such as `ring_url`, `answer_url`, `fallback_url`, `action_url`, `callback_url`, and `hangup_url`.

    In each callback, the `CallStatus` parameter takes one of these values:

    <table>
      <tbody>
        <tr>
          <td><strong>in-progress</strong></td>

          <td>
            <p>The call was answered and is in progress. Calls with this status can be terminated using the <a href="/voice/api/call/hangup-a-call/">Hangup API</a>.</p>
          </td>
        </tr>

        <tr>
          <td><strong>completed</strong></td>

          <td>
            <p>The call was completed, terminated either by the Hangup API or by one of the parties in the call.</p>
          </td>
        </tr>

        <tr>
          <td><strong>ringing</strong></td>

          <td>
            <p>The call is ringing. This status is sent to the Ring URL.</p>
          </td>
        </tr>

        <tr>
          <td><strong>no-answer</strong></td>

          <td>
            <p>The call was not answered.</p>
          </td>
        </tr>

        <tr>
          <td><strong>busy</strong></td>

          <td>
            <p>The called line is busy.</p>
          </td>
        </tr>

        <tr>
          <td><strong>cancel</strong></td>

          <td>
            <p>The call was canceled by the caller.</p>
          </td>
        </tr>

        <tr>
          <td><strong>timeout</strong></td>

          <td>
            <p>There was a timeout while connecting your call, caused by either an issue with one of the terminating carriers or network lag in our system.</p>
          </td>
        </tr>
      </tbody>
    </table>

    Plivo sends these parameters to the application server in the webhook:

    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Description</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>`DialRingStatus`</td>
          <td>Indicates whether the dial attempt rang or not. Values: `true`, `false`</td>
        </tr>

        <tr>
          <td>`DialHangupCause`</td>
          <td>The <a href="/voice/troubleshooting/hangup-causes/#list-of-hangup-causes">standard telephony hangup cause</a>.</td>
        </tr>

        <tr>
          <td>`DialStatus`</td>
          <td>Status of the dial. Values: `completed`, `busy`, `failed`, `timeout`, `no-answer`</td>
        </tr>

        <tr>
          <td>`DialALegUUID`</td>
          <td>CallUUID of the A leg.</td>
        </tr>

        <tr>
          <td>`DialBLegUUID`</td>
          <td>CallUUID of the B leg. Empty if nobody answers.</td>
        </tr>
      </tbody>
    </table>

    You can implement dial status reporting either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to handle dial status reporting with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status-reporting.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=128df4ffcabef5e92220b9616eff9f21" alt="Screen Incoming Calls Call Flow" width="1446" height="774" data-path="images/dial-status-reporting.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status.gif?s=3075e34fce686a7f9646d51a76e550d0" alt="Create the PHLO to Block calls from a specific number" width="1024" height="545" data-path="images/dial-status.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Call Forward** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Call Forward** node.

        * In the configuration panel for the **Call Forward** node, enter the caller ID variable `{{ "{{Start.call.from" }}}}` in the **From** field. Enter any numbers you want to call in the **To** field, separated by commas.

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Next, from the list of components, drag and drop the **HTTP Request** component onto the canvas.

        * Draw lines to connect all of the dial status states of the **Call Forward** node (Completed, No Answer, Busy/Rejected, Failed) with the **HTTP Request** node.

        * Configure the **HTTP Request** node. Enter your application server URL in the box next to the HTTP Method (GET/POST) field.

        * Provide key:value pairs of the callback attributes you’re interested in, such as `DialRingStatus`, `DialHangupCause`, `DialStatus`, `DialALegUUID`, and `DialBLegUUID`.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_dialstatus.gif?s=057b7f6972e2a56dbd895d8f08006111" alt="Configure the PHLO to your Plivo Number" width="1024" height="545" data-path="images/assign_dialstatus.gif" />
        </Frame>

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        ## Test

        You can now make a call to your Plivo phone number. After the call ends, Plivo reports back the status via the key:value pairs you specified to the URL you specified.

        For more information about creating a PHLO app, see the [PHLO User Guide](/phlo/).For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to send callback events for dial status reporting.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status-reporting.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=128df4ffcabef5e92220b9616eff9f21" alt="Outbound Call Flow" width="1446" height="774" data-path="images/dial-status-reporting.png" />
        </Frame>

        Plivo requests an answer URL when a Plivo number receives a call (step 2) and expects the file at that URL to be configured in the application assigned to the number to hold a valid XML response with instructions on how to handle the call. For [outbound calls](/voice/use-cases/make-outbound-calls/node/) you specify an answer URL along with the make call API request, and for [incoming calls](/voice/use-cases/receive-incoming-calls/node/) the answer URL is specified in the Plivo application associated with the phone number.

        In addition to requests to the answer URL, Plivo initiates HTTP requests to your application server throughout the course of a call based on specific XML elements and attributes in your answer XML document (step 5). Such requests are broadly classified into two categories:

        **Action URL requests:** These requests are typically  invoked at the end of an XML element’s execution, and the server expects XML instructions to carry forward the call in response to these  requests. This happens, for example, when a caller provides Touch-Tone input during GetInput XML execution.

        **Callback URL requests:** These requests serve as webhooks to pass the application server  information about events through the course of an XML element’s  execution, such as when a conference participant is muted or unmuted. These callback URL requests can be used for dial status reporting. No XML instructions are expected in response to these requests.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Rails controller for dial status reporting

        Change to the project directory and run this command to create a Rails controller to reject incoming calls.

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
         def dialstatus
            r = Response.new()
            params = {
                'action' => "https://<yourdomain>.com/dialstatus/action/", # Redirect to this URL after leaving Dial.
                'method' => 'GET' # Submit to action URL using GET or POST.
            }

            r.addSpeak("Connecting your call..")
            d = r.addDial(params)
            d.addNumber("<phone_number>")
            xml = Plivo::PlivoXML.new(r)
            render xml: xml.to_xml
         end
         def dialstatusaction
            status = params[:DialStatus]
            aleg = params[:DialALegUUID]
            bleg = params[:DialBLegUUID]
            puts "Status : #{status}, ALeg UUID : #{aleg}, BLeg UUID : #{bleg}"
         end
        end
        ```

        Replace the phone number placeholder with an actual phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        In this code, we tell Plivo to POST the call status to https\://\<yourdomain>.com/dialstatus/. We set the [redirect attribute](/voice/xml/redirect/), which determines whether to change the call flow of an ongoing call based on the actions performed, to `true`, which tells Plivo to expect a valid XML document to be posted to https\://\<yourdomain>.com/dialstatus/action. The code creates an XML document with a Dial XML element.

        ## Create a Plivo application for dial status reporting

        Associate the Rails controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Dial Status Report`. Enter the server URL you want to use (for example `https://<yourdomain>.com/dialstatus/`) in the `Answer URL` field and set the method to `POST`.  Click on `Create Application` to save your application.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dialstatusreporting.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=a8af3b7e6c4eb5b552a6904de0a6477f" alt="Create dial status application" width="1440" height="805" data-path="images/dialstatusreporting.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Dial Status Report` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_dialstatusreport.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=79cc79bf9d43547163544e04d6062b97" alt="assign dial status application" width="1440" height="785" data-path="images/assign_dialstatusreport.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides, and call details will be posted to your application server via the action and callback URLs you configured throughout the course of the call.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Python">
    ## Overview

    Plivo passes the call status of an ongoing call so you can decide how to process it. For all the calls made using Plivo’s [Make a Call API](/voice/api/call#make-a-call) or [Dial XML](/voice/xml/dial/), Plivo sends the call status to the application server at different stages of a call. We send call status as an HTTP webhook request to URLs such as `ring_url`, `answer_url`, `fallback_url`, `action_url`, `callback_url`, and `hangup_url`.

    In each callback, the `CallStatus` parameter takes one of these values:

    <table>
      <tbody>
        <tr>
          <td><strong>in-progress</strong></td>

          <td>
            <p>The call was answered and is in progress. Calls with this status can be terminated using the <a href="/voice/api/call/hangup-a-call/">Hangup API</a>.</p>
          </td>
        </tr>

        <tr>
          <td><strong>completed</strong></td>

          <td>
            <p>The call was completed, terminated either by the Hangup API or by one of the parties in the call.</p>
          </td>
        </tr>

        <tr>
          <td><strong>ringing</strong></td>

          <td>
            <p>The call is ringing. This status is sent to the Ring URL.</p>
          </td>
        </tr>

        <tr>
          <td><strong>no-answer</strong></td>

          <td>
            <p>The call was not answered.</p>
          </td>
        </tr>

        <tr>
          <td><strong>busy</strong></td>

          <td>
            <p>The called line is busy.</p>
          </td>
        </tr>

        <tr>
          <td><strong>cancel</strong></td>

          <td>
            <p>The call was canceled by the caller.</p>
          </td>
        </tr>

        <tr>
          <td><strong>timeout</strong></td>

          <td>
            <p>There was a timeout while connecting your call, caused by either an issue with one of the terminating carriers or network lag in our system.</p>
          </td>
        </tr>
      </tbody>
    </table>

    Plivo sends these parameters to the application server in the webhook:

    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Description</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>`DialRingStatus`</td>
          <td>Indicates whether the dial attempt rang or not. Values: `true`, `false`</td>
        </tr>

        <tr>
          <td>`DialHangupCause`</td>
          <td>The <a href="/voice/troubleshooting/hangup-causes/#list-of-hangup-causes">standard telephony hangup cause</a>.</td>
        </tr>

        <tr>
          <td>`DialStatus`</td>
          <td>Status of the dial. Values: `completed`, `busy`, `failed`, `timeout`, `no-answer`</td>
        </tr>

        <tr>
          <td>`DialALegUUID`</td>
          <td>CallUUID of the A leg.</td>
        </tr>

        <tr>
          <td>`DialBLegUUID`</td>
          <td>CallUUID of the B leg. Empty if nobody answers.</td>
        </tr>
      </tbody>
    </table>

    You can implement dial status reporting either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to handle dial status reporting with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status-reporting.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=128df4ffcabef5e92220b9616eff9f21" alt="Screen Incoming Calls Call Flow" width="1446" height="774" data-path="images/dial-status-reporting.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status.gif?s=3075e34fce686a7f9646d51a76e550d0" alt="Create the PHLO to Block calls from a specific number" width="1024" height="545" data-path="images/dial-status.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Call Forward** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Call Forward** node.

        * In the configuration panel for the **Call Forward** node, enter the caller ID variable `{{ "{{Start.call.from" }}}}` in the **From** field. Enter any numbers you want to call in the **To** field, separated by commas.

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Next, from the list of components, drag and drop the **HTTP Request** component onto the canvas.

        * Draw lines to connect all of the dial status states of the **Call Forward** node (Completed, No Answer, Busy/Rejected, Failed) with the **HTTP Request** node.

        * Configure the **HTTP Request** node. Enter your application server URL in the box next to the HTTP Method (GET/POST) field.

        * Provide key:value pairs of the callback attributes you’re interested in, such as `DialRingStatus`, `DialHangupCause`, `DialStatus`, `DialALegUUID`, and `DialBLegUUID`.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_dialstatus.gif?s=057b7f6972e2a56dbd895d8f08006111" alt="Configure the PHLO to your Plivo Number" width="1024" height="545" data-path="images/assign_dialstatus.gif" />
        </Frame>

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        ## Test

        You can now make a call to your Plivo phone number. After the call ends, Plivo reports back the status via the key:value pairs you specified to the URL you specified.

        For more information about creating a PHLO app, see the [PHLO User Guide](/phlo/).For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to send callback events for dial status reporting.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status-reporting.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=128df4ffcabef5e92220b9616eff9f21" alt="Screen Incoming Calls Call Flow" width="1446" height="774" data-path="images/dial-status-reporting.png" />
        </Frame>

        Plivo requests an answer URL when a Plivo number receives a call (step 2) and expects the file at that URL to be configured in the application assigned to the number to hold a valid XML response with instructions on how to handle the call. For [outbound calls](/voice/use-cases/make-outbound-calls/node/) you specify an answer URL along with the make call API request, and for [incoming calls](/voice/use-cases/receive-incoming-calls/node/) the answer URL is specified in the Plivo application associated with the phone number.

        In addition to requests to the answer URL, Plivo initiates HTTP requests to your application server throughout the course of a call based on specific XML elements and attributes in your answer XML document (step 5). Such requests are broadly classified into two categories:

        **Action URL requests:** These requests are typically  invoked at the end of an XML element’s execution, and the server expects XML instructions to carry forward the call in response to these  requests. This happens, for example, when a caller provides Touch-Tone input during GetInput XML execution.

        **Callback URL requests:** These requests serve as webhooks to pass the application server  information about events through the course of an XML element’s  execution, such as when a conference participant is muted or unmuted. These callback URL requests can be used for dial status reporting. No XML instructions are expected in response to these requests.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Flask application for dial status reporting

        Create a file called `dial_status.py` and paste into it this code.

        ```py  theme={null}
        from flask import Flask, request, Response
        from plivo import plivoxml

        app=Flask(__name__)

        @app.route('/dialstatus/', methods=['GET','POST'])
        def dial_xml():

            # Generate Dial XML
            response = plivoxml.ResponseElement()
            response.add(plivoxml.SpeakElement('Connecting your call..'))
            response.add(plivoxml.DialElement(action='https://<yourdomain>.com/dialstatus/action/', method='POST', redirect=True)
            .add(plivoxml.NumberElement("<phone_number>")))
            return Response(response.to_string(), mimetype='application/xml')

        @app.route('/dialstatus/action/', methods=['GET','POST'])
        def dial_status():

            # After completion of the call, Plivo will report back the status to the action URL in the Dial XML.

            status = request.args.get('DialStatus')
            aleg = request.args.get('DialALegUUID')
            bleg = request.args.get('DialBLegUUID')
            print "Status : %s, ALeg Uuid : %s, BLeg Uuid : %s" % (status,aleg,bleg)
            return "Dial status reported"

        if __name__ == '__main__':
            app.run(host='0.0.0.0', debug=True)
        ```

        Replace the phone number placeholder with an actual phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        In this code, we tell Plivo to POST the call status to https\://\<yourdomain>.com/dialstatus/. We set the [redirect attribute](/voice/xml/redirect/), which determines whether to change the call flow of an ongoing call based on the actions performed, to `true`, which tells Plivo to expect a valid XML document to be posted to https\://\<yourdomain>.com/dialstatus/action. The code creates an XML document with a Dial XML element.

        ## Create a Plivo application for dial status reporting

        Associate the Flask application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Dial Status Report`. Enter the server URL you want to use (for example `https://<yourdomain>.com/dialstatus/`) in the `Answer URL` field and set the method to `POST`.  Click on `Create Application` to save your application.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dialstatusreporting.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=a8af3b7e6c4eb5b552a6904de0a6477f" alt="Create dial status application" width="1440" height="805" data-path="images/dialstatusreporting.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Dial Status Report` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_dialstatusreport.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=79cc79bf9d43547163544e04d6062b97" alt="assign dial status application" width="1440" height="785" data-path="images/assign_dialstatusreport.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides, and call details will be posted to your application server via the action and callback URLs you configured throughout the course of the call.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="PHP">
    ## Overview

    Plivo passes the call status of an ongoing call so you can decide how to process it. For all the calls made using Plivo’s [Make a Call API](/voice/api/call/#make-a-call) or [Dial XML](/voice/xml/dial/), Plivo sends the call status to the application server at different stages of a call. We send call status as an HTTP webhook request to URLs such as `ring_url`, `answer_url`, `fallback_url`, `action_url`, `callback_url`, and `hangup_url`.

    In each callback, the `CallStatus` parameter takes one of these values:

    <table>
      <tbody>
        <tr>
          <td><strong>in-progress</strong></td>

          <td>
            <p>The call was answered and is in progress. Calls with this status can be terminated using the <a href="/voice/api/call/hangup-a-call/">Hangup API</a>.</p>
          </td>
        </tr>

        <tr>
          <td><strong>completed</strong></td>

          <td>
            <p>The call was completed, terminated either by the Hangup API or by one of the parties in the call.</p>
          </td>
        </tr>

        <tr>
          <td><strong>ringing</strong></td>

          <td>
            <p>The call is ringing. This status is sent to the Ring URL.</p>
          </td>
        </tr>

        <tr>
          <td><strong>no-answer</strong></td>

          <td>
            <p>The call was not answered.</p>
          </td>
        </tr>

        <tr>
          <td><strong>busy</strong></td>

          <td>
            <p>The called line is busy.</p>
          </td>
        </tr>

        <tr>
          <td><strong>cancel</strong></td>

          <td>
            <p>The call was canceled by the caller.</p>
          </td>
        </tr>

        <tr>
          <td><strong>timeout</strong></td>

          <td>
            <p>There was a timeout while connecting your call, caused by either an issue with one of the terminating carriers or network lag in our system.</p>
          </td>
        </tr>
      </tbody>
    </table>

    Plivo sends these parameters to the application server in the webhook:

    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Description</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>`DialRingStatus`</td>
          <td>Indicates whether the dial attempt rang or not. Values: `true`, `false`</td>
        </tr>

        <tr>
          <td>`DialHangupCause`</td>
          <td>The <a href="/voice/troubleshooting/hangup-causes/#list-of-hangup-causes">standard telephony hangup cause</a>.</td>
        </tr>

        <tr>
          <td>`DialStatus`</td>
          <td>Status of the dial. Values: `completed`, `busy`, `failed`, `timeout`, `no-answer`</td>
        </tr>

        <tr>
          <td>`DialALegUUID`</td>
          <td>CallUUID of the A leg.</td>
        </tr>

        <tr>
          <td>`DialBLegUUID`</td>
          <td>CallUUID of the B leg. Empty if nobody answers.</td>
        </tr>
      </tbody>
    </table>

    You can implement dial status reporting either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to handle dial status reporting with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status-reporting.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=128df4ffcabef5e92220b9616eff9f21" alt="Screen Incoming Calls Call Flow" width="1446" height="774" data-path="images/dial-status-reporting.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status.gif?s=3075e34fce686a7f9646d51a76e550d0" alt="Create the PHLO to Block calls from a specific number" width="1024" height="545" data-path="images/dial-status.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Call Forward** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Call Forward** node.

        * In the configuration panel for the **Call Forward** node, enter the caller ID variable `{{ "{{Start.call.from" }}}}` in the **From** field. Enter any numbers you want to call in the **To** field, separated by commas.

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Next, from the list of components, drag and drop the **HTTP Request** component onto the canvas.

        * Draw lines to connect all of the dial status states of the **Call Forward** node (Completed, No Answer, Busy/Rejected, Failed) with the **HTTP Request** node.

        * Configure the **HTTP Request** node. Enter your application server URL in the box next to the HTTP Method (GET/POST) field.

        * Provide key:value pairs of the callback attributes you’re interested in, such as `DialRingStatus`, `DialHangupCause`, `DialStatus`, `DialALegUUID`, and `DialBLegUUID`.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_dialstatus.gif?s=057b7f6972e2a56dbd895d8f08006111" alt="Configure the PHLO to your Plivo Number" width="1024" height="545" data-path="images/assign_dialstatus.gif" />
        </Frame>

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        ## Test

        You can now make a call to your Plivo phone number. After the call ends, Plivo reports back the status via the key:value pairs you specified to the URL you specified.

        For more information about creating a PHLO app, see the [PHLO User Guide](/phlo/).For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to send callback events for dial status reporting.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status-reporting.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=128df4ffcabef5e92220b9616eff9f21" alt="Outbound Call Flow" width="1446" height="774" data-path="images/dial-status-reporting.png" />
        </Frame>

        Plivo requests an answer URL when a Plivo number receives a call (step 2) and expects the file at that URL to be configured in the application assigned to the number to hold a valid XML response with instructions on how to handle the call. For [outbound calls](/voice/use-cases/make-outbound-calls/node/) you specify an answer URL along with the make call API request, and for [incoming calls](/voice/use-cases/receive-incoming-calls/node/) the answer URL is specified in the Plivo application associated with the phone number.

        In addition to requests to the answer URL, Plivo initiates HTTP requests to your application server throughout the course of a call based on specific XML elements and attributes in your answer XML document (step 5). Such requests are broadly classified into two categories:

        **Action URL requests:** These requests are typically  invoked at the end of an XML element’s execution, and the server expects XML instructions to carry forward the call in response to these  requests. This happens, for example, when a caller provides Touch-Tone input during GetInput XML execution.

        **Callback URL requests:** These requests serve as webhooks to pass the application server  information about events through the course of an XML element’s  execution, such as when a conference participant is muted or unmuted. These callback URL requests can be used for dial status reporting. No XML instructions are expected in response to these requests.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Laravel controller for dial status reporting

        Create a file called `dial_status.php` and paste into it this code.

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
            public function dialStatus()
            {
              $r = new Response();
              // Add Speak tag
              $body = "Connecting your call..";
              $r->addSpeak($body);
              $params = array(
                 'action' => 'https://<yourdomain>.com/dial_action/', # Redirect to this URL after leaving Dial.
                 'method' => 'GET' # Submit to action URL using GET or POST.
              );
              // Add Dial tag
              $d = $r->addDial($params);
              $number = "<phone_number>";
              $d->addNumber($number);
              Header('Content-type: text/xml');
              echo($r->toXML());
            }
            // Action URL Block
            public function dialstatusAction()
            {
              // Print the Dial Details
              $status = $_REQUEST['DialStatus'];
              $aleg = $_REQUEST['DialALegUUID'];
              $bleg = $_REQUEST['DialBLegUUID'];
              echo "Status = $status , Aleg UUID = $aleg , Bleg UUID = $bleg";
            }
        }
        ```

        Replace the phone number placeholder with an actual phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        In this code, we tell Plivo to POST the call status to https\://\<yourdomain>.com/dialstatus/.  We set the [redirect attribute](/voice/xml/redirect/), which determines whether to change the call flow of an ongoing call based on the actions performed, to `true`, which tells Plivo to expect a valid XML document to be posted to https\://\<yourdomain>.com/dialstatus/action. The code creates an XML document with a Dial XML element.

        ## Create a Plivo application for dial status reporting

        Associate the Laravel controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Dial Status Report`. Enter the server URL you want to use (for example `https://<yourdomain>.com/dialstatus/`) in the `Answer URL` field and set the method to `POST`.  Click on `Create Application` to save your application.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dialstatusreporting.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=a8af3b7e6c4eb5b552a6904de0a6477f" alt="Create dial status application" width="1440" height="805" data-path="images/dialstatusreporting.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Dial Status Report` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_dialstatusreport.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=79cc79bf9d43547163544e04d6062b97" alt="assign dial status application" width="1440" height="785" data-path="images/assign_dialstatusreport.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides, and call details will be posted to your application server via the action and callback URLs you configured throughout the course of the call.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title=".NET">
    ## Overview

    Plivo passes the call status of an ongoing call so you can decide how to process it. For all the calls made using Plivo’s [Make a Call API](/voice/api/call/#make-a-call) or [Dial XML](/voice/xml/dial/), Plivo sends the call status to the application server at different stages of a call. We send call status as an HTTP webhook request to URLs such as `ring_url`, `answer_url`, `fallback_url`, `action_url`, `callback_url`, and `hangup_url`.

    In each callback, the `CallStatus` parameter takes one of these values:

    <table>
      <tbody>
        <tr>
          <td><strong>in-progress</strong></td>

          <td>
            <p>The call was answered and is in progress. Calls with this status can be terminated using the <a href="/voice/api/call/hangup-a-call/">Hangup API</a>.</p>
          </td>
        </tr>

        <tr>
          <td><strong>completed</strong></td>

          <td>
            <p>The call was completed, terminated either by the Hangup API or by one of the parties in the call.</p>
          </td>
        </tr>

        <tr>
          <td><strong>ringing</strong></td>

          <td>
            <p>The call is ringing. This status is sent to the Ring URL.</p>
          </td>
        </tr>

        <tr>
          <td><strong>no-answer</strong></td>

          <td>
            <p>The call was not answered.</p>
          </td>
        </tr>

        <tr>
          <td><strong>busy</strong></td>

          <td>
            <p>The called line is busy.</p>
          </td>
        </tr>

        <tr>
          <td><strong>cancel</strong></td>

          <td>
            <p>The call was canceled by the caller.</p>
          </td>
        </tr>

        <tr>
          <td><strong>timeout</strong></td>

          <td>
            <p>There was a timeout while connecting your call, caused by either an issue with one of the terminating carriers or network lag in our system.</p>
          </td>
        </tr>
      </tbody>
    </table>

    Plivo sends these parameters to the application server in the webhook:

    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Description</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>`DialRingStatus`</td>
          <td>Indicates whether the dial attempt rang or not. Values: `true`, `false`</td>
        </tr>

        <tr>
          <td>`DialHangupCause`</td>
          <td>The <a href="/voice/troubleshooting/hangup-causes/#list-of-hangup-causes">standard telephony hangup cause</a>.</td>
        </tr>

        <tr>
          <td>`DialStatus`</td>
          <td>Status of the dial. Values: `completed`, `busy`, `failed`, `timeout`, `no-answer`</td>
        </tr>

        <tr>
          <td>`DialALegUUID`</td>
          <td>CallUUID of the A leg.</td>
        </tr>

        <tr>
          <td>`DialBLegUUID`</td>
          <td>CallUUID of the B leg. Empty if nobody answers.</td>
        </tr>
      </tbody>
    </table>

    You can implement dial status reporting either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to handle dial status reporting with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status-reporting.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=128df4ffcabef5e92220b9616eff9f21" alt="Screen Incoming Calls Call Flow" width="1446" height="774" data-path="images/dial-status-reporting.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status.gif?s=3075e34fce686a7f9646d51a76e550d0" alt="Create the PHLO to Block calls from a specific number" width="1024" height="545" data-path="images/dial-status.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Call Forward** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Call Forward** node.

        * In the configuration panel for the **Call Forward** node, enter the caller ID variable `{{ "{{Start.call.from" }}}}` in the **From** field. Enter any numbers you want to call in the **To** field, separated by commas.

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Next, from the list of components, drag and drop the **HTTP Request** component onto the canvas.

        * Draw lines to connect all of the dial status states of the **Call Forward** node (Completed, No Answer, Busy/Rejected, Failed) with the **HTTP Request** node.

        * Configure the **HTTP Request** node. Enter your application server URL in the box next to the HTTP Method (GET/POST) field.

        * Provide key:value pairs of the callback attributes you’re interested in, such as `DialRingStatus`, `DialHangupCause`, `DialStatus`, `DialALegUUID`, and `DialBLegUUID`.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_dialstatus.gif?s=057b7f6972e2a56dbd895d8f08006111" alt="Configure the PHLO to your Plivo Number" width="1024" height="545" data-path="images/assign_dialstatus.gif" />
        </Frame>

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        ## Test

        You can now make a call to your Plivo phone number. After the call ends, Plivo reports back the status via the key:value pairs you specified to the URL you specified.

        For more information about creating a PHLO app, see the [PHLO User Guide](/phlo/).For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to send callback events for dial status reporting.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status-reporting.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=128df4ffcabef5e92220b9616eff9f21" alt="Outbound Call Flow" width="1446" height="774" data-path="images/dial-status-reporting.png" />
        </Frame>

        Plivo requests an answer URL when a Plivo number receives a call (step 2) and expects the file at that URL to be configured in the application assigned to the number to hold a valid XML response with instructions on how to handle the call. For [outbound calls](/voice/use-cases/make-outbound-calls/node/) you specify an answer URL along with the make call API request, and for [incoming calls](/voice/use-cases/receive-incoming-calls/node/) the answer URL is specified in the Plivo application associated with the phone number.

        In addition to requests to the answer URL, Plivo initiates HTTP requests to your application server throughout the course of a call based on specific XML elements and attributes in your answer XML document (step 5). Such requests are broadly classified into two categories:

        **Action URL requests:** These requests are typically  invoked at the end of an XML element’s execution, and the server expects XML instructions to carry forward the call in response to these  requests. This happens, for example, when a caller provides Touch-Tone input during GetInput XML execution.

        **Callback URL requests:** These requests serve as webhooks to pass the application server  information about events through the course of an XML element’s  execution, such as when a conference participant is muted or unmuted. These callback URL requests can be used for dial status reporting. No XML instructions are expected in response to these requests.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an MVC controller for dial status reporting

        Navigate to the Controllers directory in the Dialstatus app. Create a Controller named `DialstatusController.cs` and paste into it this code.

        ```cs  theme={null}
        using System;
        using System.Collections.Generic;
        using Plivo.XML;
        using Microsoft.AspNetCore.Mvc;

        namespace Dialstatus.Controllers
        {
            public class DialstatusController : Controller
            {
                // GET: /<controller>/
                public IActionResult Index()
                {
                    Plivo.XML.Response resp = new Plivo.XML.Response();
                    // Generate Dial XML
                    Plivo.XML.Dial dial = new Plivo.XML.Dial(new Dictionary<string, string>()
                    {
                        {"action","https://<yourdomain>.com/dialstatus/action/"}, // Redirect to this URL after leaving Dial.
                        {"method","GET"} // Submit to action URL using GET or POST.
                    });
                    dial.AddNumber("<phone_number>", new Dictionary<string, string>() { });
                    resp.Add(dial);
                    var output = resp.ToString();
                    return this.Content(output, "text/xml");
                }
                //Action URL
                public String Action()
                {
                    var status = Request.Query["DialStatus"];
                    var aleg = Request.Form["DialALegUUID"];
                    var bleg = Request.Form["DialBLegUUID"];
                    Debug.WriteLine("Status : {0}, ALeg UUID : {1}, BLeg UUID : {2}", status, aleg, bleg);
                    return "OK";
                }
            }
        }
        ```

        Replace the phone number placeholder with an actual phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        In this code, we tell Plivo to POST the call status to https\://\<yourdomain>.com/dialstatus/.  We set the [redirect attribute](/voice/xml/redirect/), which determines whether to change the call flow of an ongoing call based on the actions performed, to `true`, which tells Plivo to expect a valid XML document to be posted to https\://\<yourdomain>.com/dialstatus/action. The code creates an XML document with a Dial XML element.

        ## Create a Plivo application for dial status reporting

        Associate the controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Dial Status Report`. Enter the server URL you want to use (for example `https://<yourdomain>.com/dialstatus/`) in the `Answer URL` field and set the method to `POST`.  Click on `Create Application` to save your application.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dialstatusreporting.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=a8af3b7e6c4eb5b552a6904de0a6477f" alt="Create dial status application" width="1440" height="805" data-path="images/dialstatusreporting.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Dial Status Report` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_dialstatusreport.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=79cc79bf9d43547163544e04d6062b97" alt="assign dial status application" width="1440" height="785" data-path="images/assign_dialstatusreport.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides, and call details will be posted to your application server via the action and callback URLs you configured throughout the course of the call.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Java">
    ## Overview

    Plivo passes the call status of an ongoing call so you can decide how to process it. For all the calls made using Plivo’s [Make a Call API](/voice/api/call/#make-a-call) or [Dial XML](/voice/xml/dial/), Plivo sends the call status to the application server at different stages of a call. We send call status as an HTTP webhook request to URLs such as `ring_url`, `answer_url`, `fallback_url`, `action_url`, `callback_url`, and `hangup_url`.

    In each callback, the `CallStatus` parameter takes one of these values:

    <table>
      <tbody>
        <tr>
          <td><strong>in-progress</strong></td>

          <td>
            <p>The call was answered and is in progress. Calls with this status can be terminated using the <a href="/voice/api/call/hangup-a-call/">Hangup API</a>.</p>
          </td>
        </tr>

        <tr>
          <td><strong>completed</strong></td>

          <td>
            <p>The call was completed, terminated either by the Hangup API or by one of the parties in the call.</p>
          </td>
        </tr>

        <tr>
          <td><strong>ringing</strong></td>

          <td>
            <p>The call is ringing. This status is sent to the Ring URL.</p>
          </td>
        </tr>

        <tr>
          <td><strong>no-answer</strong></td>

          <td>
            <p>The call was not answered.</p>
          </td>
        </tr>

        <tr>
          <td><strong>busy</strong></td>

          <td>
            <p>The called line is busy.</p>
          </td>
        </tr>

        <tr>
          <td><strong>cancel</strong></td>

          <td>
            <p>The call was canceled by the caller.</p>
          </td>
        </tr>

        <tr>
          <td><strong>timeout</strong></td>

          <td>
            <p>There was a timeout while connecting your call, caused by either an issue with one of the terminating carriers or network lag in our system.</p>
          </td>
        </tr>
      </tbody>
    </table>

    Plivo sends these parameters to the application server in the webhook:

    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Description</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>`DialRingStatus`</td>
          <td>Indicates whether the dial attempt rang or not. Values: `true`, `false`</td>
        </tr>

        <tr>
          <td>`DialHangupCause`</td>
          <td>The <a href="/voice/troubleshooting/hangup-causes/#list-of-hangup-causes">standard telephony hangup cause</a>.</td>
        </tr>

        <tr>
          <td>`DialStatus`</td>
          <td>Status of the dial. Values: `completed`, `busy`, `failed`, `timeout`, `no-answer`</td>
        </tr>

        <tr>
          <td>`DialALegUUID`</td>
          <td>CallUUID of the A leg.</td>
        </tr>

        <tr>
          <td>`DialBLegUUID`</td>
          <td>CallUUID of the B leg. Empty if nobody answers.</td>
        </tr>
      </tbody>
    </table>

    You can implement dial status reporting either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to handle dial status reporting with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status-reporting.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=128df4ffcabef5e92220b9616eff9f21" alt="Screen Incoming Calls Call Flow" width="1446" height="774" data-path="images/dial-status-reporting.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status.gif?s=3075e34fce686a7f9646d51a76e550d0" alt="Create the PHLO to Block calls from a specific number" width="1024" height="545" data-path="images/dial-status.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Call Forward** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Call Forward** node.

        * In the configuration panel for the **Call Forward** node, enter the caller ID variable `{{ "{{Start.call.from" }}}}` in the **From** field. Enter any numbers you want to call in the **To** field, separated by commas.

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Next, from the list of components, drag and drop the **HTTP Request** component onto the canvas.

        * Draw lines to connect all of the dial status states of the **Call Forward** node (Completed, No Answer, Busy/Rejected, Failed) with the **HTTP Request** node.

        * Configure the **HTTP Request** node. Enter your application server URL in the box next to the HTTP Method (GET/POST) field.

        * Provide key:value pairs of the callback attributes you’re interested in, such as `DialRingStatus`, `DialHangupCause`, `DialStatus`, `DialALegUUID`, and `DialBLegUUID`.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_dialstatus.gif?s=057b7f6972e2a56dbd895d8f08006111" alt="Configure the PHLO to your Plivo Number" width="1024" height="545" data-path="images/assign_dialstatus.gif" />
        </Frame>

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        ## Test

        You can now make a call to your Plivo phone number. After the call ends, Plivo reports back the status via the key:value pairs you specified to the URL you specified.

        For more information about creating a PHLO app, see the [PHLO User Guide](/phlo/).For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to send callback events for dial status reporting.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status-reporting.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=128df4ffcabef5e92220b9616eff9f21" alt="Outbound Call Flow" width="1446" height="774" data-path="images/dial-status-reporting.png" />
        </Frame>

        Plivo requests an answer URL when a Plivo number receives a call (step 2) and expects the file at that URL to be configured in the application assigned to the number to hold a valid XML response with instructions on how to handle the call. For [outbound calls](/voice/use-cases/make-outbound-calls/node/) you specify an answer URL along with the make call API request, and for [incoming calls](/voice/use-cases/receive-incoming-calls/node/) the answer URL is specified in the Plivo application associated with the phone number.

        In addition to requests to the answer URL, Plivo initiates HTTP requests to your application server throughout the course of a call based on specific XML elements and attributes in your answer XML document (step 5). Such requests are broadly classified into two categories:

        **Action URL requests:** These requests are typically  invoked at the end of an XML element’s execution, and the server expects XML instructions to carry forward the call in response to these  requests. This happens, for example, when a caller provides Touch-Tone input during GetInput XML execution.

        **Callback URL requests:** These requests serve as webhooks to pass the application server  information about events through the course of an XML element’s  execution, such as when a conference participant is muted or unmuted. These callback URL requests can be used for dial status reporting. No XML instructions are expected in response to these requests.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Spark application for dial status reporting

        Create a Java class named `DialStatus` and paste into it this code.

        ```java  theme={null}
        import static spark.Spark.*;
        import com.plivo.api.xml.Dial;
        import com.plivo.api.xml.Number;
        import com.plivo.api.xml.Response;

        public class dialstatus {
            public static void main(String[] args) {
                post("/dialstatus/", (request, response) -> {
                    response.type("application/xml");
                    Response resp = new Response()
                        .children(
                                new Dial()
                                    .action("https://<yourdomain>.com/dialstatus/action/")
                                    .method("POST")
                                    .redirect(true)
                                    .children(
                                            new Number("<phone_number>")
                                    )
                        );
                    return resp.toXmlString();
                });
                post("/dialstatus/action/", (request, response) -> {
                    String status = request.queryParams("Status");
                    String aleg = request.queryParams("DialALegUUID");
                    String bleg = request.queryParams("DialBLegUUID");
                    System.out.println("Status : " + status + " ALeg UUID : " + aleg + " Bleg UUID : " + bleg);
                    response.raw().getWriter().print("Status : " + status + " ALeg UUID : " + aleg + " Bleg UUID : " + bleg);
                    return "done";
                });
            }
        }
        ```

        Replace the phone number placeholder with an actual phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        In this code, we tell Plivo to POST the call status to https\://\<yourdomain>.com/dialstatus/.  We set the [redirect attribute](/voice/xml/redirect/), which determines whether to change the call flow of an ongoing call based on the actions performed, to `true`, which tells Plivo to expect a valid XML document to be posted to https\://\<yourdomain>.com/dialstatus/action. The code creates an XML document with a Dial XML element.

        ## Create a Plivo application for dial status reporting

        Associate the Spark application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Dial Status Report`. Enter the server URL you want to use (for example `https://<yourdomain>.com/dialstatus/`) in the `Answer URL` field and set the method to `POST`.  Click on `Create Application` to save your application.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dialstatusreporting.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=a8af3b7e6c4eb5b552a6904de0a6477f" alt="Create dial status application" width="1440" height="805" data-path="images/dialstatusreporting.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Dial Status Report` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_dialstatusreport.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=79cc79bf9d43547163544e04d6062b97" alt="assign dial status application" width="1440" height="785" data-path="images/assign_dialstatusreport.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides, and call details will be posted to your application server via the action and callback URLs you configured throughout the course of the call.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Go">
    ## Overview

    Plivo passes the call status of an ongoing call so you can decide how to process it. For all the calls made using Plivo’s [Make a Call API](/voice/api/call/#make-a-call) or [Dial XML](/voice/xml/dial/), Plivo sends the call status to the application server at different stages of a call. We send call status as an HTTP webhook request to URLs such as `ring_url`, `answer_url`, `fallback_url`, `action_url`, `callback_url`, and `hangup_url`.

    In each callback, the `CallStatus` parameter takes one of these values:

    <table>
      <tbody>
        <tr>
          <td><strong>in-progress</strong></td>

          <td>
            <p>The call was answered and is in progress. Calls with this status can be terminated using the <a href="/voice/api/call/hangup-a-call/">Hangup API</a>.</p>
          </td>
        </tr>

        <tr>
          <td><strong>completed</strong></td>

          <td>
            <p>The call was completed, terminated either by the Hangup API or by one of the parties in the call.</p>
          </td>
        </tr>

        <tr>
          <td><strong>ringing</strong></td>

          <td>
            <p>The call is ringing. This status is sent to the Ring URL.</p>
          </td>
        </tr>

        <tr>
          <td><strong>no-answer</strong></td>

          <td>
            <p>The call was not answered.</p>
          </td>
        </tr>

        <tr>
          <td><strong>busy</strong></td>

          <td>
            <p>The called line is busy.</p>
          </td>
        </tr>

        <tr>
          <td><strong>cancel</strong></td>

          <td>
            <p>The call was canceled by the caller.</p>
          </td>
        </tr>

        <tr>
          <td><strong>timeout</strong></td>

          <td>
            <p>There was a timeout while connecting your call, caused by either an issue with one of the terminating carriers or network lag in our system.</p>
          </td>
        </tr>
      </tbody>
    </table>

    Plivo sends these parameters to the application server in the webhook:

    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Description</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>`DialRingStatus`</td>
          <td>Indicates whether the dial attempt rang or not. Values: `true`, `false`</td>
        </tr>

        <tr>
          <td>`DialHangupCause`</td>
          <td>The <a href="/voice/troubleshooting/hangup-causes/#list-of-hangup-causes">standard telephony hangup cause</a>.</td>
        </tr>

        <tr>
          <td>`DialStatus`</td>
          <td>Status of the dial. Values: `completed`, `busy`, `failed`, `timeout`, `no-answer`</td>
        </tr>

        <tr>
          <td>`DialALegUUID`</td>
          <td>CallUUID of the A leg.</td>
        </tr>

        <tr>
          <td>`DialBLegUUID`</td>
          <td>CallUUID of the B leg. Empty if nobody answers.</td>
        </tr>
      </tbody>
    </table>

    You can implement dial status reporting either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to handle dial status reporting with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status-reporting.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=128df4ffcabef5e92220b9616eff9f21" alt="Screen Incoming Calls Call Flow" width="1446" height="774" data-path="images/dial-status-reporting.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status.gif?s=3075e34fce686a7f9646d51a76e550d0" alt="Create the PHLO to Block calls from a specific number" width="1024" height="545" data-path="images/dial-status.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Call Forward** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Call Forward** node.

        * In the configuration panel for the **Call Forward** node, enter the caller ID variable `{{ "{{Start.call.from" }}}}` in the **From** field. Enter any numbers you want to call in the **To** field, separated by commas.

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Next, from the list of components, drag and drop the **HTTP Request** component onto the canvas.

        * Draw lines to connect all of the dial status states of the **Call Forward** node (Completed, No Answer, Busy/Rejected, Failed) with the **HTTP Request** node.

        * Configure the **HTTP Request** node. Enter your application server URL in the box next to the HTTP Method (GET/POST) field.

        * Provide key:value pairs of the callback attributes you’re interested in, such as `DialRingStatus`, `DialHangupCause`, `DialStatus`, `DialALegUUID`, and `DialBLegUUID`.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_dialstatus.gif?s=057b7f6972e2a56dbd895d8f08006111" alt="Configure the PHLO to your Plivo Number" width="1024" height="545" data-path="images/assign_dialstatus.gif" />
        </Frame>

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        ## Test

        You can now make a call to your Plivo phone number. After the call ends, Plivo reports back the status via the key:value pairs you specified to the URL you specified.

        For more information about creating a PHLO app, see the [PHLO User Guide](/phlo/).For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to send callback events for dial status reporting.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dial-status-reporting.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=128df4ffcabef5e92220b9616eff9f21" alt="Outbound Call Flow" width="1446" height="774" data-path="images/dial-status-reporting.png" />
        </Frame>

        Plivo requests an answer URL when a Plivo number receives a call (step 2) and expects the file at that URL to be configured in the application assigned to the number to hold a valid XML response with instructions on how to handle the call. For [outbound calls](/voice/use-cases/make-outbound-calls/node/) you specify an answer URL along with the make call API request, and for [incoming calls](/voice/use-cases/receive-incoming-calls/node/) the answer URL is specified in the Plivo application associated with the phone number.

        In addition to requests to the answer URL, Plivo initiates HTTP requests to your application server throughout the course of a call based on specific XML elements and attributes in your answer XML document (step 5). Such requests are broadly classified into two categories:

        **Action URL requests:** These requests are typically  invoked at the end of an XML element’s execution, and the server expects XML instructions to carry forward the call in response to these  requests. This happens, for example, when a caller provides Touch-Tone input during GetInput XML execution.

        **Callback URL requests:** These requests serve as webhooks to pass the application server  information about events through the course of an XML element’s  execution, such as when a conference participant is muted or unmuted. These callback URL requests can be used for dial status reporting. No XML instructions are expected in response to these requests.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Go application for dial status reporting

        Create a file called `dial_status.go` and paste into it this code.

        ```go  theme={null}
        package main

        import (
        	"github.com/go-martini/martini"
        	"github.com/plivo/plivo-go/v7/xml"
        	"net/http"
        )

        func main() {
        	m := martini.Classic()
        	m.Post("/dialstatus/", func(w http.ResponseWriter, r *http.Request) string {
        		w.Header().Set("Content-Type", "application/xml")
        		response := xml.ResponseElement{
        			Contents: []interface{}{
        				new(xml.DialElement).
        					SetAction("https://<yourdomain>.com/dialstatus/action/").
        					SetMethod("POST").
        					SetRedirect(true).
        					SetContents([]interface{}{
        						new(xml.NumberElement).
        							SetContents("<phone_number>"),
        					}),
        			},
        		}
        		return response.String()
        	})
        	m.Post("/dialstatus/action", func(w http.ResponseWriter, r *http.Request) string {
        		status := r.FormValue("DialStatus")
        		aleg := r.FormValue("DialALegUUID")
        		bleg := r.FormValue("DialBLegUUID")
        		result := status + " " + aleg + " " + bleg
        		return result
        	})
        	m.Run()
        }
        ```

        Replace the phone number placeholder with an actual phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        In this code, we tell Plivo to POST the call status to https\://\<yourdomain>.com/dialstatus/. We set the [redirect attribute](/voice/xml/redirect/), which determines whether to change the call flow of an ongoing call based on the actions performed, to `true`, which tells Plivo to expect a valid XML document to be posted to https\://\<yourdomain>.com/dialstatus/action. The code creates an XML document with a Dial XML element.

        ## Create a Plivo application for dial status reporting

        Associate the Go application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Dial Status Report`. Enter the server URL you want to use (for example `https://<yourdomain>.com/dialstatus/`) in the `Answer URL` field and set the method to `POST`.  Click on `Create Application` to save your application.

        <Frame>
          <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dialstatusreporting.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=a8af3b7e6c4eb5b552a6904de0a6477f" alt="Create dial status application" width="1440" height="805" data-path="images/dialstatusreporting.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Dial Status Report` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_dialstatusreport.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=79cc79bf9d43547163544e04d6062b97" alt="assign dial status application" width="1440" height="785" data-path="images/assign_dialstatusreport.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides, and call details will be posted to your application server via the action and callback URLs you configured throughout the course of the call.
      </Tab>
    </Tabs>
  </Tab>
</Tabs>
