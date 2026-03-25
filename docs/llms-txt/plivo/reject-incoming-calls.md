# Source: https://plivo.com/docs/voice/use-cases/reject-incoming-calls.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Reject Incoming Calls

> Reject unwanted incoming calls on your Plivo phone numbers

<Tabs>
  <Tab title="Node">
    ## Overview

    When you don’t want to receive incoming calls on your Plivo numbers, follow the instructions in this guide to create an application to reject them.

    You can reject incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to reject incoming calls with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/rejectcalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=7171dd672d138f9c43d835a03248ccf7" alt="Inbound Call Flow" width="1446" height="774" data-path="images/rejectcalls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reject_calls_phlo.gif?s=74827b34691b9abb695c33aca812f8a8" alt="Create a PHLO to reject incoming calls" width="1024" height="585" data-path="images/reject_calls_phlo.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components, on the left hand side, drag and drop the **Hangup** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Hangup** node.

        * Click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you have created and configured your PHLO, assign your PHLO to a Plivo number.

        1. On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        2. In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        3. From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reject_calls_number.gif?s=4928adb6cc2996091fed04c3c8abb071" alt="Assign PHLO to a Plivo number" width="1024" height="585" data-path="images/reject_calls_number.gif" />
        </Frame>

        ## Test

        You can now make a call to your Plivo phone number and see that calls are rejected.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that rejects incoming calls on a Plivo number.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/rejectcalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=7171dd672d138f9c43d835a03248ccf7" alt="Inbound Call Flow" width="1446" height="774" data-path="images/rejectcalls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo rejects the call using the [Hangup](/voice/xml/hangup/) XML element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an application to reject incoming calls

        Create a file called `reject_call.js` and paste into it this code.

        ```js  theme={null}
        var express = require('express');
        var plivo = require('plivo');
        var app = express();

        app.set('port', (process.env.PORT || 5000));

        app.all('/reject_calls/', function(request, response) {
            var response = plivo.Response();
            var params = {
                'reason': 'rejected'
            };
            response.addHangup(params);
            res.writeHead(200, {'Content-Type': 'text/xml'});
            res.end(response.toXML());
        });

        app.listen(app.get('port'), function() {
            console.log('Node app is running on port', app.get('port'));
        });
        ```

        ## Create a Plivo application to reject calls

        Associate the code you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Reject Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/reject_caller/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_reject_calls.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=854bc59a424f5174888f0dde781dab8c" alt="Create Application" width="1440" height="805" data-path="images/create_reject_calls.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Reject Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_rejectcall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=a8e95e075a18d2675fb0c05520aa36e9" alt="Assign Phone Number to Reject Call App" width="1440" height="704" data-path="images/assign_rejectcall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides — in this case, rejecting it.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Ruby">
    ## Overview

    When you don’t want to receive incoming calls on your Plivo numbers, follow the instructions in this guide to create an application to reject them.

    You can reject incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to reject incoming calls with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/rejectcalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=7171dd672d138f9c43d835a03248ccf7" alt="Inbound Call Flow" width="1446" height="774" data-path="images/rejectcalls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reject_calls_phlo.gif?s=74827b34691b9abb695c33aca812f8a8" alt="Create a PHLO to reject incoming calls" width="1024" height="585" data-path="images/reject_calls_phlo.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components, on the left hand side, drag and drop the **Hangup** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Hangup** node.

        * Click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you have created and configured your PHLO, assign your PHLO to a Plivo number.

        1. On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        2. In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        3. From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reject_calls_number.gif?s=4928adb6cc2996091fed04c3c8abb071" alt="Assign PHLO to a Plivo number" width="1024" height="585" data-path="images/reject_calls_number.gif" />
        </Frame>

        ## Test

        You can now make a call to your Plivo phone number and see that calls are rejected.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that rejects incoming calls on a Plivo number.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/rejectcalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=7171dd672d138f9c43d835a03248ccf7" alt="Inbound Call Flow" width="1446" height="774" data-path="images/rejectcalls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo rejects the call using the [Hangup](/voice/xml/hangup/) XML element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-go-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Rails controller to reject incoming calls

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
         def reject
            r = Response.new()
            params = {
                'reason' => 'rejected', # Specify the reason for hangup
            }
            r.addHangup(params)
            xml = Plivo::PlivoXML.new(r)
            render xml: xml.to_xml
         end
        end
        ```

        ## Create a Plivo application to reject calls

        Associate the Rails controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Reject Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/reject_caller/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_reject_calls.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=854bc59a424f5174888f0dde781dab8c" alt="Create Application" width="1440" height="805" data-path="images/create_reject_calls.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Reject Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_rejectcall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=a8e95e075a18d2675fb0c05520aa36e9" alt="Assign Phone Number to Reject Call App" width="1440" height="704" data-path="images/assign_rejectcall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides — in this case, rejecting it.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Python">
    ## Overview

    When you don’t want to receive incoming calls on your Plivo numbers, follow the instructions in this guide to create an application to reject them.

    You can reject incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to reject incoming calls with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/rejectcalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=7171dd672d138f9c43d835a03248ccf7" alt="Inbound Call Flow" width="1446" height="774" data-path="images/rejectcalls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reject_calls_phlo.gif?s=74827b34691b9abb695c33aca812f8a8" alt="Create a PHLO to reject incoming calls" width="1024" height="585" data-path="images/reject_calls_phlo.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components, on the left hand side, drag and drop the **Hangup** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Hangup** node.

        * Click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you have created and configured your PHLO, assign your PHLO to a Plivo number.

        1. On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        2. In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        3. From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reject_calls_number.gif?s=4928adb6cc2996091fed04c3c8abb071" alt="Assign PHLO to a Plivo number" width="1024" height="585" data-path="images/reject_calls_number.gif" />
        </Frame>

        ## Test

        You can now make a call to your Plivo phone number and see that calls are rejected.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that rejects incoming calls on a Plivo number.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/rejectcalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=7171dd672d138f9c43d835a03248ccf7" alt="Inbound Call Flow" width="1446" height="774" data-path="images/rejectcalls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo rejects the call using the [Hangup](/voice/xml/hangup/) XML element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Flask server to reject incoming calls

        Create a file called `reject_call.py` and paste into it this code.

        ```py  theme={null}
        from flask import Flask, Response
        from plivo import plivoxml

        app = Flask(__name__)

        @app.route("/reject_call/", methods=['GET','POST'])
        def hangup():
            # Generate Hangup XML to reject an incoming call.
            response = plivoxml.ResponseElement()
            params = {'reason': 'rejected'}
            response.add(plivoxml.HangupElement(**params))

            return Response(response.to_string(), mimetype='application/xml')

        if __name__ == "__main__":
            app.run(host='0.0.0.0', debug=True)
        ```

        ## Create a Plivo application to reject calls

        Associate the Flask server you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Reject Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/reject_caller/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_reject_calls.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=854bc59a424f5174888f0dde781dab8c" alt="Create Application" width="1440" height="805" data-path="images/create_reject_calls.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Reject Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_rejectcall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=a8e95e075a18d2675fb0c05520aa36e9" alt="Assign Phone Number to Reject Call App" width="1440" height="704" data-path="images/assign_rejectcall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides — in this case, rejecting it.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="PHP">
    ## Overview

    When you don’t want to receive incoming calls on your Plivo numbers, follow the instructions in this guide to create an application to reject them.

    You can reject incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to reject incoming calls with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/rejectcalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=7171dd672d138f9c43d835a03248ccf7" alt="Inbound Call Flow" width="1446" height="774" data-path="images/rejectcalls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reject_calls_phlo.gif?s=74827b34691b9abb695c33aca812f8a8" alt="Create a PHLO to reject incoming calls" width="1024" height="585" data-path="images/reject_calls_phlo.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components, on the left hand side, drag and drop the **Hangup** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Hangup** node.

        * Click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you have created and configured your PHLO, assign your PHLO to a Plivo number.

        1. On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        2. In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        3. From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reject_calls_number.gif?s=4928adb6cc2996091fed04c3c8abb071" alt="Assign PHLO to a Plivo number" width="1024" height="585" data-path="images/reject_calls_number.gif" />
        </Frame>

        ## Test

        You can now make a call to your Plivo phone number and see that calls are rejected.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that rejects incoming calls on a Plivo number.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/rejectcalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=7171dd672d138f9c43d835a03248ccf7" alt="Inbound Call Flow" width="1446" height="774" data-path="images/rejectcalls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo rejects the call using the [Hangup](/voice/xml/hangup/) XML element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Laravel controller to reject incoming calls

        Change to the project directory and run this command to create a Laravel controller to reject inbound calls.

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
            public function rejectCall()
            {
              $r = new Response();
              // Generate Hangup XML
              $params = array(
                    'reason' => 'rejected', # Specify the reason for hangup
              );

              $r->addHangup($params);
              Header('Content-type: text/xml');
              echo $r->toXML();
            }
        }
        ```

        ## Create a Plivo application to reject calls

        Associate the controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Reject Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/reject_caller/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_reject_calls.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=854bc59a424f5174888f0dde781dab8c" alt="Create Application" width="1440" height="805" data-path="images/create_reject_calls.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Reject Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_rejectcall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=a8e95e075a18d2675fb0c05520aa36e9" alt="Assign Phone Number to Reject Call App" width="1440" height="704" data-path="images/assign_rejectcall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides — in this case, rejecting it.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title=".NET">
    ## Overview

    When you don’t want to receive incoming calls on your Plivo numbers, follow the instructions in this guide to create an application to reject them.

    You can reject incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to reject incoming calls with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/rejectcalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=7171dd672d138f9c43d835a03248ccf7" alt="Inbound Call Flow" width="1446" height="774" data-path="images/rejectcalls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reject_calls_phlo.gif?s=74827b34691b9abb695c33aca812f8a8" alt="Create a PHLO to reject incoming calls" width="1024" height="585" data-path="images/reject_calls_phlo.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components, on the left hand side, drag and drop the **Hangup** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Hangup** node.

        * Click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you have created and configured your PHLO, assign your PHLO to a Plivo number.

        1. On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        2. In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        3. From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reject_calls_number.gif?s=4928adb6cc2996091fed04c3c8abb071" alt="Assign PHLO to a Plivo number" width="1024" height="585" data-path="images/reject_calls_number.gif" />
        </Frame>

        ## Test

        You can now make a call to your Plivo phone number and see that calls are rejected.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that rejects incoming calls on a Plivo number.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/rejectcalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=7171dd672d138f9c43d835a03248ccf7" alt="Inbound Call Flow" width="1446" height="774" data-path="images/rejectcalls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo rejects the call using the [Hangup](/voice/xml/hangup/) XML element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an MVC controller to reject incoming calls

        In Visual Studio, create a new project. Use the template for Web Application (Model-View-Controller).

        <Frame>
                    <img src="https://mintlify.s3.us-west-1.amazonaws.com/plivo/images/create_mvcapp.jpg" alt="Create an MVC app" />
        </Frame>

        Give the project a name — we used `Rejectcall`.

        Navigate to the Controllers directory in the Rejectcall project. Create  a controller named RejectcallController.cs and paste into it this code.

        ```cs  theme={null}
        using System;
        using Plivo.XML;
        using System.Collections.Generic;
        using Microsoft.AspNetCore.Mvc;

        namespace Rejectcall
        {
            public class RejectcallController : Controller
            {
                public IActionResult Index()
                {
                    Plivo.XML.Response resp = new Plivo.XML.Response();
                    // Add Hangup XML Tag
                    resp.AddHangup(new Dictionary<string, string>()
                    {
                        {"reason","rejected"}, // Specify the reason for hangup
                    });
                    var output = resp.ToString();
                    return this.Content(output, "text/xml");
                }
            }
        }
        ```

        ## Create a Plivo application to reject calls

        Associate the controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Reject Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/reject_caller/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_reject_calls.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=854bc59a424f5174888f0dde781dab8c" alt="Create Application" width="1440" height="805" data-path="images/create_reject_calls.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Reject Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_rejectcall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=a8e95e075a18d2675fb0c05520aa36e9" alt="Assign Phone Number to Reject Call App" width="1440" height="704" data-path="images/assign_rejectcall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides — in this case, rejecting it.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Java">
    ## Overview

    When you don’t want to receive incoming calls on your Plivo numbers, follow the instructions in this guide to create an application to reject them.

    You can reject incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to reject incoming calls with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/rejectcalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=7171dd672d138f9c43d835a03248ccf7" alt="Inbound Call Flow" width="1446" height="774" data-path="images/rejectcalls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reject_calls_phlo.gif?s=74827b34691b9abb695c33aca812f8a8" alt="Create a PHLO to reject incoming calls" width="1024" height="585" data-path="images/reject_calls_phlo.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components, on the left hand side, drag and drop the **Hangup** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Hangup** node.

        * Click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you have created and configured your PHLO, assign your PHLO to a Plivo number.

        1. On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        2. In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        3. From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reject_calls_number.gif?s=4928adb6cc2996091fed04c3c8abb071" alt="Assign PHLO to a Plivo number" width="1024" height="585" data-path="images/reject_calls_number.gif" />
        </Frame>

        ## Test

        You can now make a call to your Plivo phone number and see that calls are rejected.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that rejects incoming calls on a Plivo number.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/rejectcalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=7171dd672d138f9c43d835a03248ccf7" alt="Inbound Call Flow" width="1446" height="774" data-path="images/rejectcalls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo rejects the call using the [Hangup](/voice/xml/hangup/) XML element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Spark application to reject incoming calls

        Create a Java class named `RejectCall` and paste into it this code.

        ```java  theme={null}
        import static spark.Spark.*;
        import com.plivo.api.xml.Response;
        import com.plivo.api.xml.Speak;

        public class rejectcall {
            public static void main(String[] args) {
                post("/reject_calls", (request, response) - > {
                    response.type("application/xml");
                    Response resp = new Response()
                    .children(
                        new Hangup()
                        .reason("rejected")
                    );
                    // Returns the XML
                    return resp.toXmlString();
                });
            }
        }
        ```

        ## Create a Plivo application to reject calls

        Associate the Spark application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Reject Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/reject_caller/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_reject_calls.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=854bc59a424f5174888f0dde781dab8c" alt="Create Application" width="1440" height="805" data-path="images/create_reject_calls.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Reject Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_rejectcall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=a8e95e075a18d2675fb0c05520aa36e9" alt="Assign Phone Number to Reject Call App" width="1440" height="704" data-path="images/assign_rejectcall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides — in this case, rejecting it.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Go">
    ## Overview

    When you don’t want to receive incoming calls on your Plivo numbers, follow the instructions in this guide to create an application to reject them.

    You can reject incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to reject incoming calls with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/rejectcalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=7171dd672d138f9c43d835a03248ccf7" alt="Inbound Call Flow" width="1446" height="774" data-path="images/rejectcalls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reject_calls_phlo.gif?s=74827b34691b9abb695c33aca812f8a8" alt="Create a PHLO to reject incoming calls" width="1024" height="585" data-path="images/reject_calls_phlo.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components, on the left hand side, drag and drop the **Hangup** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Hangup** node.

        * Click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you have created and configured your PHLO, assign your PHLO to a Plivo number.

        1. On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        2. In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        3. From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/reject_calls_number.gif?s=4928adb6cc2996091fed04c3c8abb071" alt="Assign PHLO to a Plivo number" width="1024" height="585" data-path="images/reject_calls_number.gif" />
        </Frame>

        ## Test

        You can now make a call to your Plivo phone number and see that calls are rejected.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that rejects incoming calls on a Plivo number.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/rejectcalls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=7171dd672d138f9c43d835a03248ccf7" alt="Inbound Call Flow" width="1446" height="774" data-path="images/rejectcalls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo rejects the call using the [Hangup](/voice/xml/hangup/) XML element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Go server to reject incoming calls

        Create a file called `reject_call.go` and paste into it this code.

        ```go  theme={null}
        package main

        import (
        	"net/http"
        	"github.com/go-martini/martini"
        	"github.com/plivo/plivo-go/v7/xml"
        )

        func main() {
        	m := martini.Classic()
        	m.Get("/reject_call", func(w http.ResponseWriter, r *http.Request) string {
        		w.Header().Set("Content-Type", "application/xml")

        		response := xml.ResponseElement{
        			Contents: []interface{}{
        				new(xml.HangupElement).
        					SetReason("rejected"),
        			},
        		}
        		print(response.String())
        		return response.String()
        	})
        	m.Run()
        }
        ```

        ## Create a Plivo application to reject calls

        Associate the Go application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Reject Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/reject_caller/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_reject_calls.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=854bc59a424f5174888f0dde781dab8c" alt="Create Application" width="1440" height="805" data-path="images/create_reject_calls.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Reject Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_rejectcall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=a8e95e075a18d2675fb0c05520aa36e9" alt="Assign Phone Number to Reject Call App" width="1440" height="704" data-path="images/assign_rejectcall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides — in this case, rejecting it.
      </Tab>
    </Tabs>
  </Tab>
</Tabs>
