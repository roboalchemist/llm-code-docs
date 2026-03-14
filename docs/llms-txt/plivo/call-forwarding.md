# Source: https://plivo.com/docs/voice/use-cases/call-forwarding.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Call Forwarding

> Route incoming calls dynamically based on availability, time, or location

<Tabs>
  <Tab title="Node">
    ## Overview

    You can use call forwarding to dynamically route incoming calls based on any of several factors.

    * **Agent availability:** You can place calls in a holding queue and route them to an available agent as soon as one is available.
    * **Business hours:** You can route calls to an office number during business hours and to a mobile phone or voicemail during non-business hours.
    * **Time zones:** You can forward calls to agents from different time zones to ensure round-the-clock availability.

    This guide shows how to forward calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement call forwarding with a few clicks on the PHLO canvas.

        <iframe src="https://www.youtube.com/embed/h5JlqpV9R-8" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.
          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Call Forward** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Call Forward** node.

        <iframe src="https://www.youtube.com/embed/iYJv0Y9gY6A" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        * In the Configuration tab at the right of the canvas, configure the **Call Forward** node to select the From number using a variable. Enter two curly brackets to view all available variables, and choose the appropriate one. Enter all the numbers you want to call in the To field, separated with commas.

        <iframe src="https://www.youtube.com/embed/14EyW7An1cs" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        * Once you’ve configured the node, click **Validate** to save the configuration.
        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call-forwarding.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=dd58734038be28d230864f5ae3fb8d6e" alt="" width="1440" height="785" data-path="images/call-forwarding.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo-forward.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=0dd6efea9b4a1d69e8dda54e7cf001e4" alt="" width="1440" height="785" data-path="images/assign-phlo-forward.png" />
        </Frame>

        ## Test

        You can now call your Plivo phone number and see how the inbound call is forwarded.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here‘s how to use Plivo XML to forward calls.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call-forward.png?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=e62ec764aa4537e96c58c4b1522ba77e" alt="" width="1446" height="774" data-path="images/call-forward.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo forwards the call using the [Dial XML](/voice/xml/dial/) element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an Express server to forward incoming calls

        Create a file called `forward_call.js` and paste into it this code.

        ```js  theme={null}
        var express = require('express')
        var app = express()

        app.post('/forward_call/', function(req, res) {
            var plivo = require('plivo');
            var response = plivo.Response();
            var dial = response.addDial();

            dial.addNumber("<destination_number>"); // call wll be forwarded to this number
            res.send(response.toXML());
        })

        app.set('port', (process.env.PORT || 5000));
        app.listen(app.get('port'), function() {
            console.log('Node app is running on port', app.get('port'));
        });
        ```

        Replace the destination number placeholder with an actual phone number (for example, 12025551234).

        Save the file and run it.

        ```shell  theme={null}
        $ node forward_call.js
        ```

        ## Create a Plivo application to forward calls

        Associate the Go application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Forward Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/forward_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Forward Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_forwardcall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=a8be150728d33bc104aede3e6682b635" alt="" width="1440" height="707" data-path="images/assign_forwardcall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then forward the call according to the instructions in the XML document the server provides.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Ruby">
    ## Overview

    You can use call forwarding to dynamically route incoming calls based on any of several factors.

    * **Agent availability:** You can place calls in a holding queue and route them to an available agent as soon as one is available.
    * **Business hours:** You can route calls to an office number during business hours and to a mobile phone or voicemail during non-business hours.
    * **Time zones:** You can forward calls to agents from different time zones to ensure round-the-clock availability.

    This guide shows how to forward calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement call forwarding with a few clicks on the PHLO canvas.

        <iframe src="https://www.youtube.com/embed/h5JlqpV9R-8" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.
          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Call Forward** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Call Forward** node.

        <iframe src="https://www.youtube.com/embed/iYJv0Y9gY6A" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        * In the Configuration tab at the right of the canvas, configure the **Call Forward** node to select the From number using a variable. Enter two curly brackets to view all available variables, and choose the appropriate one. Enter all the numbers you want to call in the To field, separated with commas.

        <iframe src="https://www.youtube.com/embed/14EyW7An1cs" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        * Once you’ve configured the node, click **Validate** to save the configuration.
        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call-forwarding.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=dd58734038be28d230864f5ae3fb8d6e" alt="" width="1440" height="785" data-path="images/call-forwarding.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo-forward.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=0dd6efea9b4a1d69e8dda54e7cf001e4" alt="" width="1440" height="785" data-path="images/assign-phlo-forward.png" />
        </Frame>

        ## Test

        You can now call your Plivo phone number and see how the inbound call is forwarded.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here‘s how to use Plivo XML to forward calls.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call-forward.png?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=e62ec764aa4537e96c58c4b1522ba77e" alt="" width="1446" height="774" data-path="images/call-forward.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo forwards the call using the [Dial XML](/voice/xml/dial/) element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Rails controller to forward incoming calls

        Edit the app/controllers/plivo\_controller.rb file and add this code in the PlivoController class:

        ```ruby  theme={null}
        def forward
           response = Response.new
           dial = response.addDial()
           dest_number = "<destination_number>"
           dial.addNumber(dest_number)

           xml = PlivoXML.new(response)
           puts xml.to_xml
           render xml: xml.to_xml
         end
        ```

        ### Add a route

        Add a route for the inbound function in the **PlivoController** class. Edit config/routes.rb and add this line after the inbound route:

        ```shell  theme={null}
        get 'plivo/forward'
        ```

        Now the controller is ready for inbound calls. Use this command to start the server to handle inbound calls.

        ```shell  theme={null}
        $ rails server
        ```

        ## Create a Plivo application to forward calls

        Associate the Rails server you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Forward Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/forward_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Forward Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_forwardcall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=a8be150728d33bc104aede3e6682b635" alt="" width="1440" height="707" data-path="images/assign_forwardcall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then forward the call according to the instructions in the XML document the server provides.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Python">
    ## Overview

    You can use call forwarding to dynamically route incoming calls based on any of several factors.

    * **Agent availability:** You can place calls in a holding queue and route them to an available agent as soon as one is available.
    * **Business hours:** You can route calls to an office number during business hours and to a mobile phone or voicemail during non-business hours.
    * **Time zones:** You can forward calls to agents from different time zones to ensure round-the-clock availability.

    This guide shows how to forward calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement call forwarding with a few clicks on the PHLO canvas.

        <iframe src="https://www.youtube.com/embed/h5JlqpV9R-8" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.
          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Call Forward** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Call Forward** node.

        <iframe src="https://www.youtube.com/embed/iYJv0Y9gY6A" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        * In the Configuration tab at the right of the canvas, configure the **Call Forward** node to select the From number using a variable. Enter two curly brackets to view all available variables, and choose the appropriate one. Enter all the numbers you want to call in the To field, separated with commas.

        <iframe src="https://www.youtube.com/embed/14EyW7An1cs" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        * Once you’ve configured the node, click **Validate** to save the configuration.
        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call-forwarding.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=dd58734038be28d230864f5ae3fb8d6e" alt="" width="1440" height="785" data-path="images/call-forwarding.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo-forward.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=0dd6efea9b4a1d69e8dda54e7cf001e4" alt="" width="1440" height="785" data-path="images/assign-phlo-forward.png" />
        </Frame>

        ## Test

        You can now call your Plivo phone number and see how the inbound call is forwarded.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here‘s how to use Plivo XML to forward calls.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call-forward.png?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=e62ec764aa4537e96c58c4b1522ba77e" alt="" width="1446" height="774" data-path="images/call-forward.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo forwards the call using the [Dial XML](/voice/xml/dial/) element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Flask server to forward incoming calls

        Create a file called `forward_call.py` and paste into it this code.

        ```py  theme={null}
        from flask import Flask, request, make_response, Response
        from plivo import plivoxml

        app = Flask(__name__)

        @app.route('/forward_call/', methods=['GET', 'POST'])
        def forwardcall():

            response = plivoxml.ResponseElement()
            response.add(
                plivoxml.DialElement().add(
                    plivoxml.NumberElement('<destination_number>'))) // call wll be forwarded to this number
            return(response.to_string())

        if __name__ == '__main__':
            app.run(host='0.0.0.0', debug=True)
        ```

        Replace the destination number placeholder with an actual phone number (for example, 12025551234).

        Save the file and run it.

        ```shell  theme={null}
        $ python forward_call.py
        ```

        ## Create a Plivo application to forward calls

        Associate the Python application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Forward Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/forward_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Forward Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_forwardcall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=a8be150728d33bc104aede3e6682b635" alt="" width="1440" height="707" data-path="images/assign_forwardcall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then forward the call according to the instructions in the XML document the server provides.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="PHP">
    ## Overview

    You can use call forwarding to dynamically route incoming calls based on any of several factors.

    * **Agent availability:** You can place calls in a holding queue and route them to an available agent as soon as one is available.
    * **Business hours:** You can route calls to an office number during business hours and to a mobile phone or voicemail during non-business hours.
    * **Time zones:** You can forward calls to agents from different time zones to ensure round-the-clock availability.

    This guide shows how to forward calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement call forwarding with a few clicks on the PHLO canvas.

        <iframe src="https://www.youtube.com/embed/h5JlqpV9R-8" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.
          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Call Forward** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Call Forward** node.

        <iframe src="https://www.youtube.com/embed/iYJv0Y9gY6A" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        * In the Configuration tab at the right of the canvas, configure the **Call Forward** node to select the From number using a variable. Enter two curly brackets to view all available variables, and choose the appropriate one. Enter all the numbers you want to call in the To field, separated with commas.

        <iframe src="https://www.youtube.com/embed/14EyW7An1cs" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        * Once you’ve configured the node, click **Validate** to save the configuration.
        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call-forwarding.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=dd58734038be28d230864f5ae3fb8d6e" alt="" width="1440" height="785" data-path="images/call-forwarding.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo-forward.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=0dd6efea9b4a1d69e8dda54e7cf001e4" alt="" width="1440" height="785" data-path="images/assign-phlo-forward.png" />
        </Frame>

        ## Test

        You can now call your Plivo phone number and see how the inbound call is forwarded.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here‘s how to use Plivo XML to forward calls.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call-forward.png?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=e62ec764aa4537e96c58c4b1522ba77e" alt="" width="1446" height="774" data-path="images/call-forward.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo forwards the call using the [Dial XML](/voice/xml/dial/) element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Laravel server to forward incoming calls

        Change to the project directory and run this command to create a Laravel controller for inbound calls.

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
            // Dial XML to forward the incoming call
            public function forwardCall()
            {
                $response = new Response();
                $params = array(
                    'action' => "https://<yourdomain>.com/dial_status/",
                    'method' => "POST",
                    'redirect' => "true"
                );
                $dial = $response->addDial($params);
                $number = "<destination_number>";  // call will be forwarded to this number
                $dial->addNumber($number);
                Header('Content-type: text/xml');
                echo $response->toXML();
            }
        }
        ```

        Replace the destination number placeholder with an actual phone number (for example, 12025551234).

        ## Create a Plivo application to forward calls

        Associate the Laravel server you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Forward Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/forward_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Forward Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_forwardcall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=a8be150728d33bc104aede3e6682b635" alt="" width="1440" height="707" data-path="images/assign_forwardcall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then forward the call according to the instructions in the XML document the server provides.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title=".NET">
    ## Overview

    You can use call forwarding to dynamically route incoming calls based on any of several factors.

    * **Agent availability:** You can place calls in a holding queue and route them to an available agent as soon as one is available.
    * **Business hours:** You can route calls to an office number during business hours and to a mobile phone or voicemail during non-business hours.
    * **Time zones:** You can forward calls to agents from different time zones to ensure round-the-clock availability.

    This guide shows how to forward calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement call forwarding with a few clicks on the PHLO canvas.

        <iframe src="https://www.youtube.com/embed/h5JlqpV9R-8" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.
          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Call Forward** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Call Forward** node.

        <iframe src="https://www.youtube.com/embed/iYJv0Y9gY6A" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        * In the Configuration tab at the right of the canvas, configure the **Call Forward** node to select the From number using a variable. Enter two curly brackets to view all available variables, and choose the appropriate one. Enter all the numbers you want to call in the To field, separated with commas.

        <iframe src="https://www.youtube.com/embed/14EyW7An1cs" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        * Once you’ve configured the node, click **Validate** to save the configuration.
        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call-forwarding.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=dd58734038be28d230864f5ae3fb8d6e" alt="" width="1440" height="785" data-path="images/call-forwarding.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo-forward.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=0dd6efea9b4a1d69e8dda54e7cf001e4" alt="" width="1440" height="785" data-path="images/assign-phlo-forward.png" />
        </Frame>

        ## Test

        You can now call your Plivo phone number and see how the inbound call is forwarded.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here‘s how to use Plivo XML to forward calls.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call-forward.png?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=e62ec764aa4537e96c58c4b1522ba77e" alt="" width="1446" height="774" data-path="images/call-forward.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo forwards the call using the [Dial XML](/voice/xml/dial/) element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an MVC controller to forward incoming calls

        In Visual Studio, create a new project. Use the template for Web Application (Model-View-Controller). Navigate to the Controllers directory and create a controller called `ForwardcallController.cs`, and paste into it this code.

        ```cs  theme={null}
        using System;
        using Plivo.XML;
        using System.Collections.Generic;
        using Microsoft.AspNetCore.Mvc;

        namespace Receivecall
        {
        	public class ForwardcallController : Controller
        	{
        		public IActionResult Index()
        		{
        			Plivo.XML.Response resp = new Plivo.XML.Response();
        			Plivo.XML.Dial dial = new Plivo.XML.Dial(new
        				Dictionary<string, string>() {
        			});

        			dial.AddNumber("<destination_number>",
        				new Dictionary<string, string>() { });
        			resp.Add(dial);

        			var output = resp.ToString();
        			Console.WriteLine(output);

        			return this.Content(output, "text/xml");
        		}
        	}
        }
        ```

        Replace the destination number placeholder with an actual phone number (for example, 12025551234).

        ## Create a Plivo application to forward calls

        Associate the .NET application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Forward Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/forward_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Forward Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_forwardcall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=a8be150728d33bc104aede3e6682b635" alt="" width="1440" height="707" data-path="images/assign_forwardcall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then forward the call according to the instructions in the XML document the server provides.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Java">
    ## Overview

    You can use call forwarding to dynamically route incoming calls based on any of several factors.

    * **Agent availability:** You can place calls in a holding queue and route them to an available agent as soon as one is available.
    * **Business hours:** You can route calls to an office number during business hours and to a mobile phone or voicemail during non-business hours.
    * **Time zones:** You can forward calls to agents from different time zones to ensure round-the-clock availability.

    This guide shows how to forward calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement call forwarding with a few clicks on the PHLO canvas.

        <iframe src="https://www.youtube.com/embed/h5JlqpV9R-8" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.
          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Call Forward** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Call Forward** node.

        <iframe src="https://www.youtube.com/embed/iYJv0Y9gY6A" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        * In the Configuration tab at the right of the canvas, configure the **Call Forward** node to select the From number using a variable. Enter two curly brackets to view all available variables, and choose the appropriate one. Enter all the numbers you want to call in the To field, separated with commas.

        <iframe src="https://www.youtube.com/embed/14EyW7An1cs" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        * Once you’ve configured the node, click **Validate** to save the configuration.
        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call-forwarding.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=dd58734038be28d230864f5ae3fb8d6e" alt="" width="1440" height="785" data-path="images/call-forwarding.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo-forward.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=0dd6efea9b4a1d69e8dda54e7cf001e4" alt="" width="1440" height="785" data-path="images/assign-phlo-forward.png" />
        </Frame>

        ## Test

        You can now call your Plivo phone number and see how the inbound call is forwarded.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here‘s how to use Plivo XML to forward calls.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call-forward.png?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=e62ec764aa4537e96c58c4b1522ba77e" alt="" width="1446" height="774" data-path="images/call-forward.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo forwards the call using the [Dial XML](/voice/xml/dial/) element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Java server to forward incoming calls

        Create a Java class called `ForwardCall` and paste into it this code.

        ```java  theme={null}
        import static spark.Spark.*;
        import com.plivo.api.xml.Dial;
        import com.plivo.api.xml.Number;
        import com.plivo.api.xml.Response;

        public class forwardcall {
            public static void main(String[] args) {
                get("/forward_call/", (request, response) -> {
                    String from_number = request.queryParams("From");
                    response.type("application/xml");
                    Response res = new Response()
                            .children(
                            new Dial()
                                    .callerId(from_number)
                                    .children(
                                            new Number("<destination_number>")
                                    )
                            );
                    // Returns the XML
                    return res.toXmlString();
                });
            }
        }
        ```

        Replace the destination number placeholder with an actual phone number (for example, 12025551234).

        ## Create a Plivo application to forward calls

        Associate the Java application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Forward Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/forward_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Forward Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_forwardcall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=a8be150728d33bc104aede3e6682b635" alt="" width="1440" height="707" data-path="images/assign_forwardcall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then forward the call according to the instructions in the XML document the server provides.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Go">
    ## Overview

    You can use call forwarding to dynamically route incoming calls based on any of several factors.

    * **Agent availability:** You can place calls in a holding queue and route them to an available agent as soon as one is available.
    * **Business hours:** You can route calls to an office number during business hours and to a mobile phone or voicemail during non-business hours.
    * **Time zones:** You can forward calls to agents from different time zones to ensure round-the-clock availability.

    This guide shows how to forward calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement call forwarding with a few clicks on the PHLO canvas.

        <iframe src="https://www.youtube.com/embed/h5JlqpV9R-8" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.
          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Call Forward** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Call Forward** node.

        <iframe src="https://www.youtube.com/embed/iYJv0Y9gY6A" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        * In the Configuration tab at the right of the canvas, configure the **Call Forward** node to select the From number using a variable. Enter two curly brackets to view all available variables, and choose the appropriate one. Enter all the numbers you want to call in the To field, separated with commas.

        <iframe src="https://www.youtube.com/embed/14EyW7An1cs" allow="autoplay; encrypted-media" allowfullscreen="" width="700" height="380" frameborder="0" />

        * Once you’ve configured the node, click **Validate** to save the configuration.
        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call-forwarding.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=dd58734038be28d230864f5ae3fb8d6e" alt="" width="1440" height="785" data-path="images/call-forwarding.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo-forward.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=0dd6efea9b4a1d69e8dda54e7cf001e4" alt="" width="1440" height="785" data-path="images/assign-phlo-forward.png" />
        </Frame>

        ## Test

        You can now call your Plivo phone number and see how the inbound call is forwarded.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here‘s how to use Plivo XML to forward calls.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call-forward.png?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=e62ec764aa4537e96c58c4b1522ba77e" alt="" width="1446" height="774" data-path="images/call-forward.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo forwards the call using the [Dial XML](/voice/xml/dial/) element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Go server to forward incoming calls

        Create a file called `forward_call.go` and paste into it this code.

        ```go  theme={null}
        package main

        import (
        	"net/http"
        	"plivo-go/xml"
        )

        func handler(w http.ResponseWriter, r *http.Request) {
        	response := xml.ResponseElement{
        		Contents: []interface{}{
        			new(xml.DialElement).
        				SetContents(
        					[]interface{}{
        						new(xml.NumberElement).
        							SetContents("<destination_number>"),
        					},
        				),
        		},
        	}
        	w.Write([]byte(response.String()))
        }

        func main() {
        	http.HandleFunc("/forward_call/", handler)
        	http.ListenAndServe(":8080", nil)
        }
        ```

        Replace the destination number placeholder with an actual phone number (for example, 12025551234).

        Save the file and run it.

        ```shell  theme={null}
        $ go run forward_call.go
        ```

        ## Create a Plivo application to forward calls

        Associate the Go application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Forward Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/forward_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Forward Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_forwardcall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=a8be150728d33bc104aede3e6682b635" alt="" width="1440" height="707" data-path="images/assign_forwardcall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then forward the call according to the instructions in the XML document the server provides.
      </Tab>
    </Tabs>
  </Tab>
</Tabs>
