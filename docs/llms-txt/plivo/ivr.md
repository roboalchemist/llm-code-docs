# Source: https://plivo.com/docs/voice/use-cases/ivr.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Phone system IVR

> Build an interactive voice response phone system with menu navigation

<Tabs>
  <Tab title="Node">
    ## Overview

    Interactive voice response (IVR) systems let incoming callers access information and find contacts via a menu of prerecorded messages, without having to speak to an agent, and let you automate polling via outgoing calls. Callers and call recipients can respond to prompts via Touch-Tone keypad presses or speech recognition. IVR systems can handle larger call volumes than operators and reduce costs associated with customer service.

    Common IVR use cases include:

    * **Auto-attendant**: You can replace a receptionist with an IVR system that routes calls to agents during business hours and accepts voicemail when no one is available.
    * **Call center**: You can route calls coming in to call centers to the appropriate representatives based on user input.
    * **Surveys, polling, and voting**: You can implement IVR in outbound calls to collect customer satisfaction scores or conduct political polling.
    * **Appointment reminders**: You can send automated reminders to customers before their scheduled visits to help avoid missed appointments and facilitate rescheduling.
    * **Lead assignment and lead routing**: For inbound sales calls, you can set up an IVR menu with a set of qualifying questions to discover a customer’s interests, then redirect their call to a representative based on their responses.

    This guide shows how to build an IVR menu system on the Plivo platform, either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement an IVR system with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/au8SCJEHrNU" title="How to Set Up a Professional IVR System with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.
        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong>
            The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>
        * Click the **Start** node to open the Configuration tab, then enter information that other nodes can retrieve in the API Request section — in this case, the From and optionally To numbers for the IVR system.
        * From the list of components on the left side, drag and drop the **IVR Menu** component onto the canvas. When a component is placed on the canvas it becomes a node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr_component.mp4?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=2e441bc6a99e39e3b7f38747aee4715c" data-path="images/ivr_component.mp4" />
          </Frame>
        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **IVR Menu** node.
        * In the Configuration tab at the right of the canvas, configure the choices for the IVR menu. For this example, select **1** and **2** as allowed choices. Enter a message to play to the user in the Speak Text box.
        * Once you’ve configured the node, save the configuration by clicking **Validate**. Do the same for each node as you go along.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr_connect.mp4?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=ac61267ec6c575a607186712b72afa43" data-path="images/ivr_connect.mp4" />
          </Frame>
        * Drag and drop two instances of the **Call Forward** component onto the canvas.  Rename them **Connect\_to\_Support** and **Connect\_to\_Sales**. Draw lines to connect the **IVR Menu** node‘s **1** and **2** trigger states to the new nodes.
        * Configure each **Call Forward** node to select the From number using a variable. PHLO will get the number from the key/value pairs set in the Start node. Enter two curly brackets to view all available variables, and choose the appropriate one. For the To number, either enter a fixed number directly into the To field, or use a variable that you configured in the Start node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/connect_to_ivr.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=f2e86bac6245b8f250ef42a8faf85b89" data-path="images/connect_to_ivr.mp4" />
          </Frame>
        * Drag and drop two instances of the **Play Audio** component onto the canvas. Rename the two nodes **No\_Input\_Prompt** and **Invalid\_Input\_Prompt** and configure each to speak a fixed message for callers to hear when they enter no input or invalid input. Draw lines from the **IVR Menu** node‘s No Input and Wrong Input trigger states to the respective nodes, then draw lines from the **Prompt Completed** trigger states of the new nodes back to the IVR Menu node, to give callers another chance to enter a menu choice.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/connect_ivr_invalid.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=36b7a65a75c998c80e2f4c53d425b624" data-path="images/connect_ivr_invalid.mp4" />
          </Frame>
        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/phonesystem-ivr.jpg?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=4fe6398a8b0ba7b21eec99ebfc8128f2" alt="" width="1440" height="785" data-path="images/phonesystem-ivr.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you‘ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now call your Plivo phone number and see how the IVR system works.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here‘s how to implement an IVR system using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=b6746be9ca27e825ced6ea5a60146f21" alt="" width="1446" height="774" data-path="images/ivr.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an Express server to implement IVR

        Create a file called `ivr.js` and paste into it this code.

        ```js  theme={null}
        var plivo = require('plivo');
        var express = require('express');
        var bodyParser = require('body-parser');
        var app = express();

        app.use(bodyParser.urlencoded({extended: true}));
        app.set('port', (process.env.PORT || 5000));

        // Message that Plivo reads when the caller dials in
        var IvrMessage1 = "Welcome to the demo. Press 1 to contact sales. Press 2 to contact support";
        // Message that Plivo reads when the caller does nothing
        var NoinputMessage = "Sorry, I didn't catch that. Please hang up and try again";
        // Message that Plivo reads when the caller enters an invalid number
        var WronginputMessage = "Sorry, that's not a valid entry";
        // Sales Phone number
        var salesPhoneNumber = "+15671234567"
        // Support Phone number
         var supportPhoneNumber = "+15671234578"

        app.post('/ivr/', function(request, response) {
          var r = plivo.Response();
          var getinput_action_url, params, get_input;
          getinput_action_url = request.protocol + '://' + request.headers.host + '/ivr/firstbranch/';
          params = {
                'action': getinput_action_url,
                'method': 'POST',
                'inputType': 'dtmf',
                'digitEndTimeout': '5',
                'redirect': 'true',
          };
          get_input = r.addGetInput(params);
          get_input.addSpeak(IvrMessage1);
          r.addSpeak(NoinputMessage);

          console.log(r.toXML());
          response.set({'Content-Type': 'text/xml'});
          response.send(r.toXML());
        });

        app.post('/ivr/firstbranch/', function(request, response) {
          var r = plivo.Response();
          var digit = request.body.Digits;
          console.log(digit);
          if (digit === '1') {
            var dial = r.addDial();
            dial.addNumber(salesPhoneNumber);

          } else if (digit === '2') {
            var dial = r.addDial();
            dial.addNumber(supportPhoneNumber);
          } else {
            r.addSpeak(WronginputMessage);
          }
          console.log(r.toXML());
          response.set({'Content-Type': 'text/xml'});
          response.send(r.toXML());
        });

        app.listen(app.get('port'), function() {
            console.log('Node app is running on port', app.get('port'));
        });
        ```

        Save the file and run it.

        ```shell  theme={null}
        node ivr.js
        ```

        You should see your basic server application in action at [http://localhost:3000/ivr/](http://localhost:3000/ivr/).

        [Set up ngrok](/sdk/server/set-up-node-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

        ## Create a Plivo application

        Associate the Express server you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Phone IVR`. Enter the server URL you want to use (for example `https://<yourdomain>.com/ivr/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_phoneIVR.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=97c9a8eb44f1ad4d35448ff18093677b" alt="" width="1440" height="805" data-path="images/create_phoneIVR.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Phone IVR` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_phoneIVR.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=3d1d4946b0eccb2bb844fc674dbb7ea2" alt="" width="1440" height="785" data-path="images/assign_phoneIVR.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo phone number and see how the IVR application works.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Ruby">
    ## Overview

    Interactive voice response (IVR) systems let incoming callers access information and find contacts via a menu of prerecorded messages, without having to speak to an agent, and let you automate polling via outgoing calls. Callers and call recipients can respond to prompts via Touch-Tone keypad presses or speech recognition. IVR systems can handle larger call volumes than operators and reduce costs associated with customer service.

    Common IVR use cases include:

    * **Auto-attendant**: You can replace a receptionist with an IVR system that routes calls to agents during business hours and accepts voicemail when no one is available.
    * **Call center**: You can route calls coming in to call centers to the appropriate representatives based on user input.
    * **Surveys, polling, and voting**: You can implement IVR in outbound calls to collect customer satisfaction scores or conduct political polling.
    * **Appointment reminders**: You can send automated reminders to customers before their scheduled visits to help avoid missed appointments and facilitate rescheduling.
    * **Lead assignment and lead routing**: For inbound sales calls, you can set up an IVR menu with a set of qualifying questions to discover a customer’s interests, then redirect their call to a representative based on their responses.

    This guide shows how to build an IVR menu system on the Plivo platform, either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement an IVR system with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/au8SCJEHrNU" title="How to Set Up a Professional IVR System with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.
        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong>
            The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>
        * Click the **Start** node to open the Configuration tab, then enter information that other nodes can retrieve in the API Request section — in this case, the From and optionally To numbers for the IVR system.
        * From the list of components on the left side, drag and drop the **IVR Menu** component onto the canvas. When a component is placed on the canvas it becomes a node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr_component.mp4?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=2e441bc6a99e39e3b7f38747aee4715c" data-path="images/ivr_component.mp4" />
          </Frame>
        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **IVR Menu** node.
        * In the Configuration tab at the right of the canvas, configure the choices for the IVR menu. For this example, select **1** and **2** as allowed choices. Enter a message to play to the user in the Speak Text box.
        * Once you’ve configured the node, save the configuration by clicking **Validate**. Do the same for each node as you go along.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr_connect.mp4?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=ac61267ec6c575a607186712b72afa43" data-path="images/ivr_connect.mp4" />
          </Frame>
        * Drag and drop two instances of the **Call Forward** component onto the canvas.  Rename them **Connect\_to\_Support** and **Connect\_to\_Sales**. Draw lines to connect the **IVR Menu** node‘s **1** and **2** trigger states to the new nodes.
        * Configure each **Call Forward** node to select the From number using a variable. PHLO will get the number from the key/value pairs set in the Start node. Enter two curly brackets to view all available variables, and choose the appropriate one. For the To number, either enter a fixed number directly into the To field, or use a variable that you configured in the Start node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/connect_to_ivr.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=f2e86bac6245b8f250ef42a8faf85b89" data-path="images/connect_to_ivr.mp4" />
          </Frame>
        * Drag and drop two instances of the **Play Audio** component onto the canvas. Rename the two nodes **No\_Input\_Prompt** and **Invalid\_Input\_Prompt** and configure each to speak a fixed message for callers to hear when they enter no input or invalid input. Draw lines from the **IVR Menu** node‘s No Input and Wrong Input trigger states to the respective nodes, then draw lines from the **Prompt Completed** trigger states of the new nodes back to the IVR Menu node, to give callers another chance to enter a menu choice.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/connect_ivr_invalid.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=36b7a65a75c998c80e2f4c53d425b624" data-path="images/connect_ivr_invalid.mp4" />
          </Frame>
        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/phonesystem-ivr.jpg?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=4fe6398a8b0ba7b21eec99ebfc8128f2" alt="" width="1440" height="785" data-path="images/phonesystem-ivr.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you‘ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now call your Plivo phone number and see how the IVR system works.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here‘s how to implement an IVR system using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=b6746be9ca27e825ced6ea5a60146f21" alt="" width="1446" height="774" data-path="images/ivr.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Rails controller to implement IVR

        Change to the project directory and run this command to create a Rails controller for inbound calls.

        ```shell  theme={null}
        rails generate controller Plivo voice
        ```

        This generates a controller named plivo\_controller in the app/controllers/ directory and a respective view in app/views/plivo. We can delete the view as we don‘t need it.

        ```shell  theme={null}
        rm app/views/plivo/voice.html.erb
        ```

        Edit app/controllers/plivo\_controller.rb and paste into the PlivoController class this code.

        ```ruby  theme={null}
        include Plivo
        include Plivo::XML
        include Plivo::Exceptions

        class PlivoController < ApplicationController
          $ivr_message1 = "Welcome to the demo. Press 1 to contact sales. Press 2 to contact support"
          # Message that Plivo reads when the caller does nothing
          $noinput_message = "Sorry, I did not catch that. Please hang up and try again"
          # Message that Plivo reads when the caller enters an invalid number
          $wronginput_message = "Sorry, that's not a valid entry"
          # Sales Phone number
          $salesphone_number = "+15671234567"
          # Support Phone number
          $supportphone_number = "+15671234578"

          def ivr
            r = Response.new()

            getinput_action_url = "https://<yourdomain>.com/ivr/firstbranch/"
            params = {
                action: getinput_action_url,
                method: 'POST',
                digitEndTimeout: '5',
                inputType:'dtmf',
                redirect:'true'
            }
            getinput = r.addGetInput(params)
            getinput.addSpeak($ivr_message1)
            r.addSpeak($noinput_message)

            xml = PlivoXML.new(r)
            render xml: xml.to_xml
          end

          def firstbranch
            digit = params[:Digits]
            r = Response.new()

            if (digit == "1")
              r = response.addDial()
              r.addNumber(salesphone_number)

            elsif (digit == "2")
              r = response.addDial()
              r.addNumber(supportphone_number)
            else
                r.addSpeak($wronginput_message)
            end

            xml = PlivoXML.new(r)
            render xml: xml.to_xml
          end
        end
        ```

        ### Add a route

        Add a route for the inbound function in PlivoController class. Edit config/routes.rb and add these lines after the inbound route:

        ```shell  theme={null}
        get 'plivo/ivr'
        get 'plivo/firstbranch'
        ```

        Start the Rails server.

        ```shell  theme={null}
        rails server
        ```

        You should see your basic server application in action at [http://localhost:3000/plivo/ivr/](http://localhost:3000/plivo/ivr/).

        [Set up ngrok](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

        ## Create a Plivo application

        Associate the Rails controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Phone IVR`. Enter the server URL you want to use (for example `https://<yourdomain>.com/ivr/`) in the `Answer URL` field and set the method to `GET`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/createPhoneIVR-ruby.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=ede7995f02e455a2fa506f22db9bc6c1" alt="" width="1440" height="823" data-path="images/createPhoneIVR-ruby.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Phone IVR` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_phoneIVR.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=3d1d4946b0eccb2bb844fc674dbb7ea2" alt="" width="1440" height="785" data-path="images/assign_phoneIVR.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo phone number and see how the IVR application works.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Python">
    ## Overview

    Interactive voice response (IVR) systems let incoming callers access information and find contacts via a menu of prerecorded messages, without having to speak to an agent, and let you automate polling via outgoing calls. Callers and call recipients can respond to prompts via Touch-Tone keypad presses or speech recognition. IVR systems can handle larger call volumes than operators and reduce costs associated with customer service.

    Common IVR use cases include:

    * **Auto-attendant**: You can replace a receptionist with an IVR system that routes calls to agents during business hours and accepts voicemail when no one is available.
    * **Call center**: You can route calls coming in to call centers to the appropriate representatives based on user input.
    * **Surveys, polling, and voting**: You can implement IVR in outbound calls to collect customer satisfaction scores or conduct political polling.
    * **Appointment reminders**: You can send automated reminders to customers before their scheduled visits to help avoid missed appointments and facilitate rescheduling.
    * **Lead assignment and lead routing**: For inbound sales calls, you can set up an IVR menu with a set of qualifying questions to discover a customer’s interests, then redirect their call to a representative based on their responses.

    This guide shows how to build an IVR menu system on the Plivo platform, either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement an IVR system with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/au8SCJEHrNU" title="How to Set Up a Professional IVR System with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.
        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong>
            The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>
        * Click the **Start** node to open the Configuration tab, then enter information that other nodes can retrieve in the API Request section — in this case, the From and optionally To numbers for the IVR system.
        * From the list of components on the left side, drag and drop the **IVR Menu** component onto the canvas. When a component is placed on the canvas it becomes a node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr_component.mp4?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=2e441bc6a99e39e3b7f38747aee4715c" data-path="images/ivr_component.mp4" />
          </Frame>
        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **IVR Menu** node.
        * In the Configuration tab at the right of the canvas, configure the choices for the IVR menu. For this example, select **1** and **2** as allowed choices. Enter a message to play to the user in the Speak Text box.
        * Once you’ve configured the node, save the configuration by clicking **Validate**. Do the same for each node as you go along.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr_connect.mp4?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=ac61267ec6c575a607186712b72afa43" data-path="images/ivr_connect.mp4" />
          </Frame>
        * Drag and drop two instances of the **Call Forward** component onto the canvas.  Rename them **Connect\_to\_Support** and **Connect\_to\_Sales**. Draw lines to connect the **IVR Menu** node‘s **1** and **2** trigger states to the new nodes.
        * Configure each **Call Forward** node to select the From number using a variable. PHLO will get the number from the key/value pairs set in the Start node. Enter two curly brackets to view all available variables, and choose the appropriate one. For the To number, either enter a fixed number directly into the To field, or use a variable that you configured in the Start node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/connect_to_ivr.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=f2e86bac6245b8f250ef42a8faf85b89" data-path="images/connect_to_ivr.mp4" />
          </Frame>
        * Drag and drop two instances of the **Play Audio** component onto the canvas. Rename the two nodes **No\_Input\_Prompt** and **Invalid\_Input\_Prompt** and configure each to speak a fixed message for callers to hear when they enter no input or invalid input. Draw lines from the **IVR Menu** node‘s No Input and Wrong Input trigger states to the respective nodes, then draw lines from the **Prompt Completed** trigger states of the new nodes back to the IVR Menu node, to give callers another chance to enter a menu choice.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/connect_ivr_invalid.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=36b7a65a75c998c80e2f4c53d425b624" data-path="images/connect_ivr_invalid.mp4" />
          </Frame>
        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/phonesystem-ivr.jpg?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=4fe6398a8b0ba7b21eec99ebfc8128f2" alt="" width="1440" height="785" data-path="images/phonesystem-ivr.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you‘ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now call your Plivo phone number and see how the IVR system works.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here‘s how to implement an IVR system using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=b6746be9ca27e825ced6ea5a60146f21" alt="" width="1446" height="774" data-path="images/ivr.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Flask server to implement IVR

        Create a file called `ivr.py` and paste into it this code.

        ```py  theme={null}
        # -*- coding: utf-8 -*-
        from flask import Flask, Response, request, url_for
        from plivo import plivoxml

        # Message that Plivo reads when the caller dials in
        ivr_message1 = "Welcome to the demo. Press 1 to contact sales. Press 2 to contact support"
        # Message that Plivo reads when the caller does nothing
        noinput_message = "Sorry, I didn't catch that. Please hang up and try again"
        # Message that Plivo reads when the caller enters an invalid number
        wronginput_message = "Sorry, that's not a valid entry"
        # Sales Phone number
        salesphone_number = "+15671234567"
        # Support Phone number
        supportphone_number = "+15671234578"

        app = Flask(__name__)

        @app.route('/ivr/', methods=['GET','POST'])
        def ivr():
            response = plivoxml.ResponseElement()
            response.add(plivoxml.GetInputElement().
                set_action(url_for('firstbranch', _external=True)).
                set_method('POST').
                set_input_type('dtmf').
                set_digit_end_timeout(5).
                set_redirect(True).add(
                    plivoxml.SpeakElement(ivr_message1)))
            response.add(plivoxml.SpeakElement(noinput_message))
            return Response(response.to_string(), mimetype='application/xml')

        @app.route('/ivr/firstbranch/', methods=['GET','POST'])
        def firstbranch():
            response = plivoxml.ResponseElement()
            digit = request.values.get('Digits')
            if digit == "1":
                response.add(plivoxml.DialElement().add(
                plivoxml.NumberElement(salesphone_number)))
            elif digit == "2":
                response.add(plivoxml.DialElement().add(
                plivoxml.NumberElement(supportphone_number)))
            else:
                response.add_speak(wronginput_message)
            return Response(response.to_string(), mimetype='application/xml')

        if __name__ == '__main__':
            app.run(host='0.0.0.0', debug=True)
        ```

        Save the file and run it.

        ```shell  theme={null}
        python ivr.py
        ```

        You should see your basic server application in action at [http://localhost:5000/ivr/](http://localhost:5000/ivr/).

        [Set up ngrok](/sdk/server/set-up-python-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

        ## Create a Plivo application

        Associate the Flask application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Phone IVR`. Enter the server URL you want to use (for example `https://<yourdomain>.com/ivr/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_phoneIVR.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=97c9a8eb44f1ad4d35448ff18093677b" alt="" width="1440" height="805" data-path="images/create_phoneIVR.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Phone IVR` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_phoneIVR.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=3d1d4946b0eccb2bb844fc674dbb7ea2" alt="" width="1440" height="785" data-path="images/assign_phoneIVR.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo phone number and see how the IVR application works.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="PHP">
    ## Overview

    Interactive voice response (IVR) systems let incoming callers access information and find contacts via a menu of prerecorded messages, without having to speak to an agent, and let you automate polling via outgoing calls. Callers and call recipients can respond to prompts via Touch-Tone keypad presses or speech recognition. IVR systems can handle larger call volumes than operators and reduce costs associated with customer service.

    Common IVR use cases include:

    * **Auto-attendant**: You can replace a receptionist with an IVR system that routes calls to agents during business hours and accepts voicemail when no one is available.
    * **Call center**: You can route calls coming in to call centers to the appropriate representatives based on user input.
    * **Surveys, polling, and voting**: You can implement IVR in outbound calls to collect customer satisfaction scores or conduct political polling.
    * **Appointment reminders**: You can send automated reminders to customers before their scheduled visits to help avoid missed appointments and facilitate rescheduling.
    * **Lead assignment and lead routing**: For inbound sales calls, you can set up an IVR menu with a set of qualifying questions to discover a customer’s interests, then redirect their call to a representative based on their responses.

    This guide shows how to build an IVR menu system on the Plivo platform, either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement an IVR system with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/au8SCJEHrNU" title="How to Set Up a Professional IVR System with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.
        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong>
            The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>
        * Click the **Start** node to open the Configuration tab, then enter information that other nodes can retrieve in the API Request section — in this case, the From and optionally To numbers for the IVR system.
        * From the list of components on the left side, drag and drop the **IVR Menu** component onto the canvas. When a component is placed on the canvas it becomes a node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr_component.mp4?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=2e441bc6a99e39e3b7f38747aee4715c" data-path="images/ivr_component.mp4" />
          </Frame>
        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **IVR Menu** node.
        * In the Configuration tab at the right of the canvas, configure the choices for the IVR menu. For this example, select **1** and **2** as allowed choices. Enter a message to play to the user in the Speak Text box.
        * Once you’ve configured the node, save the configuration by clicking **Validate**. Do the same for each node as you go along.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr_connect.mp4?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=ac61267ec6c575a607186712b72afa43" data-path="images/ivr_connect.mp4" />
          </Frame>
        * Drag and drop two instances of the **Call Forward** component onto the canvas.  Rename them **Connect\_to\_Support** and **Connect\_to\_Sales**. Draw lines to connect the **IVR Menu** node‘s **1** and **2** trigger states to the new nodes.
        * Configure each **Call Forward** node to select the From number using a variable. PHLO will get the number from the key/value pairs set in the Start node. Enter two curly brackets to view all available variables, and choose the appropriate one. For the To number, either enter a fixed number directly into the To field, or use a variable that you configured in the Start node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/connect_to_ivr.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=f2e86bac6245b8f250ef42a8faf85b89" data-path="images/connect_to_ivr.mp4" />
          </Frame>
        * Drag and drop two instances of the **Play Audio** component onto the canvas. Rename the two nodes **No\_Input\_Prompt** and **Invalid\_Input\_Prompt** and configure each to speak a fixed message for callers to hear when they enter no input or invalid input. Draw lines from the **IVR Menu** node‘s No Input and Wrong Input trigger states to the respective nodes, then draw lines from the **Prompt Completed** trigger states of the new nodes back to the IVR Menu node, to give callers another chance to enter a menu choice.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/connect_ivr_invalid.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=36b7a65a75c998c80e2f4c53d425b624" data-path="images/connect_ivr_invalid.mp4" />
          </Frame>
        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/phonesystem-ivr.jpg?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=4fe6398a8b0ba7b21eec99ebfc8128f2" alt="" width="1440" height="785" data-path="images/phonesystem-ivr.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you‘ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now call your Plivo phone number and see how the IVR system works.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here‘s how to implement an IVR system using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=b6746be9ca27e825ced6ea5a60146f21" alt="" width="1446" height="774" data-path="images/ivr.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Laravel server to implement IVR

        Change the project directory and run this command to create a Laravel controller for inbound calls.

        ```shell  theme={null}
        php artisan make:controller IvrController
        ```

        This generates a controller named IvrController in the app/http/controllers/ directory. Edit app/http/controllers/IvrController.php and paste into it this code.

        ```php  theme={null}
        <?php

        namespace App\Http\Controllers;
        require '../../vendor/autoload.php';
        use Plivo\RestClient;
        use Plivo\XML\Response;
        use Illuminate\Http\Request;

        class IvrController extends Controller
        {
            // GetInput XML to handle the incoming call
            public function ivrMain()
            {
                # Message that Plivo reads when the caller dials in
                $IvrMessage = "Welcome to the demo. Press 1 to contact sales. Press 2 to contact support";
                # Message that Plivo reads when the caller does nothing
                $NoinputMessage = "Sorry, I didn't catch that. Please hang up and try again";
                # Message that Plivo reads when the caller enters an invalid number.
                $WronginputMessage = "Sorry, that's not a valid entry";

                // Sales Phone Number
                $salesPhoneNumber = "+15671234567";

                // support Phone Number
                $supportPhoneNumber = "+15671234578";

                $r = new Response();
                $getinput_action_url = "https://<yourdomain>.com/firstbranch.php";
                $get_input = $r->addGetInput([
                            'action' => $getinput_action_url,
                            'method' => "POST",
                            'digitEndTimeout' => "5",
                            'inputType' => "dtmf",
                            'redirect' => "true",
                        ]);
                $get_input->addSpeak($IvrMessage);
                $r->addSpeak($NoinputMessage);
                Header('Content-type: text/xml');
                echo $r->toXML();
            }

            // Action URL block for DTMF
            public function firstBranch(Request $request)
            {
                # File to be played when a caller presses 2
                $PlivoSong = "https://s3.amazonaws.com/plivocloud/music.mp3";
                $IvrMessage = "Press 1 for English. Press 2 for French. Press 3 for Russian";
                # Message that Plivo reads when the caller does nothing
                $NoinputMessage = "Sorry, I didn't catch that. Please hang up and try again";
                # Message that Plivo reads when the caller enters an invalid number
                $WronginputMessage = "Sorry, that's not a valid entry";

                $r = new Response();

                $digit = $_REQUEST['Digits'];
                if ($digit == '1'){
                $dial = $response->addDial();
                $dial->addNumber($salesPhoneNumber);
                }
                else if ($digit == '2'){
                    $dial = $response->addDial();
                    $dial->addNumber($supportPhoneNumber);
                }
                else {
                    $r->addSpeak($WronginputMessage);
                }
                Header('Content-type: text/xml');
                echo $r->toXML();
            }
        }
        ```

        ### Add a route

        Add a route for the forward function in the IvrController class. Edit routes/web.php and add these lines:

        ```shell  theme={null}
        Route::match(['get', 'post'], '/ivr', 'IvrController@ivrMain');
        Route::match(['get', 'post'], '/firstbranch', 'IvrController@firstBranch');
        ```

        Start the Laravel server.

        ```shell  theme={null}
        php artisan serve
        ```

        You should see your basic server application in action at [http://localhost:8000/ivr](http://localhost:8000/ivr).

        [Set up ngrok](/sdk/server/set-up-php-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

        ## Create a Plivo application

        Associate the Laravel server you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Phone IVR`. Enter the server URL you want to use (for example `https://<yourdomain>.com/ivr/`) in the `Answer URL` field and set the method to `GET`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_phoneivr-dotnet.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=8ec9f78fd432aed5f08c04931d7fd3b2" alt="" width="1440" height="822" data-path="images/create_phoneivr-dotnet.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Phone IVR` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_phoneIVR.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=3d1d4946b0eccb2bb844fc674dbb7ea2" alt="" width="1440" height="785" data-path="images/assign_phoneIVR.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo phone number and see how the IVR application works.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title=".NET">
    ## Overview

    Interactive voice response (IVR) systems let incoming callers access information and find contacts via a menu of prerecorded messages, without having to speak to an agent, and let you automate polling via outgoing calls. Callers and call recipients can respond to prompts via Touch-Tone keypad presses or speech recognition. IVR systems can handle larger call volumes than operators and reduce costs associated with customer service.

    Common IVR use cases include:

    * **Auto-attendant**: You can replace a receptionist with an IVR system that routes calls to agents during business hours and accepts voicemail when no one is available.
    * **Call center**: You can route calls coming in to call centers to the appropriate representatives based on user input.
    * **Surveys, polling, and voting**: You can implement IVR in outbound calls to collect customer satisfaction scores or conduct political polling.
    * **Appointment reminders**: You can send automated reminders to customers before their scheduled visits to help avoid missed appointments and facilitate rescheduling.
    * **Lead assignment and lead routing**: For inbound sales calls, you can set up an IVR menu with a set of qualifying questions to discover a customer’s interests, then redirect their call to a representative based on their responses.

    This guide shows how to build an IVR menu system on the Plivo platform, either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement an IVR system with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/au8SCJEHrNU" title="How to Set Up a Professional IVR System with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.
        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong>
            The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>
        * Click the **Start** node to open the Configuration tab, then enter information that other nodes can retrieve in the API Request section — in this case, the From and optionally To numbers for the IVR system.
        * From the list of components on the left side, drag and drop the **IVR Menu** component onto the canvas. When a component is placed on the canvas it becomes a node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr_component.mp4?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=2e441bc6a99e39e3b7f38747aee4715c" data-path="images/ivr_component.mp4" />
          </Frame>
        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **IVR Menu** node.
        * In the Configuration tab at the right of the canvas, configure the choices for the IVR menu. For this example, select **1** and **2** as allowed choices. Enter a message to play to the user in the Speak Text box.
        * Once you’ve configured the node, save the configuration by clicking **Validate**. Do the same for each node as you go along.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr_connect.mp4?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=ac61267ec6c575a607186712b72afa43" data-path="images/ivr_connect.mp4" />
          </Frame>
        * Drag and drop two instances of the **Call Forward** component onto the canvas.  Rename them **Connect\_to\_Support** and **Connect\_to\_Sales**. Draw lines to connect the **IVR Menu** node‘s **1** and **2** trigger states to the new nodes.
        * Configure each **Call Forward** node to select the From number using a variable. PHLO will get the number from the key/value pairs set in the Start node. Enter two curly brackets to view all available variables, and choose the appropriate one. For the To number, either enter a fixed number directly into the To field, or use a variable that you configured in the Start node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/connect_to_ivr.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=f2e86bac6245b8f250ef42a8faf85b89" data-path="images/connect_to_ivr.mp4" />
          </Frame>
        * Drag and drop two instances of the **Play Audio** component onto the canvas. Rename the two nodes **No\_Input\_Prompt** and **Invalid\_Input\_Prompt** and configure each to speak a fixed message for callers to hear when they enter no input or invalid input. Draw lines from the **IVR Menu** node‘s No Input and Wrong Input trigger states to the respective nodes, then draw lines from the **Prompt Completed** trigger states of the new nodes back to the IVR Menu node, to give callers another chance to enter a menu choice.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/connect_ivr_invalid.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=36b7a65a75c998c80e2f4c53d425b624" data-path="images/connect_ivr_invalid.mp4" />
          </Frame>
        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/phonesystem-ivr.jpg?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=4fe6398a8b0ba7b21eec99ebfc8128f2" alt="" width="1440" height="785" data-path="images/phonesystem-ivr.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you‘ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now call your Plivo phone number and see how the IVR system works.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here‘s how to implement an IVR system using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=b6746be9ca27e825ced6ea5a60146f21" alt="" width="1446" height="774" data-path="images/ivr.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an MVC controller to implement IVR

        In Visual Studio, create a controller called `IvrController.cs` and paste into it this code.

        ```cs  theme={null}
        using System;
        using Plivo.XML;
        using Microsoft.AspNetCore.Mvc;
        using System.Collections.Generic;
        using System.Diagnostics;

        namespace Ivrphonetree.Controllers
        {
            public class IvrController : Controller
            {
                // Message that Plivo reads when the caller dials in
                String IvrMessage = "Welcome to the demo. Press 1 to contact sales. Press 2 to contact support";
                // Message that Plivo reads when the caller does nothing
                String NoinputMessage = "Sorry, I didn't catch that. Please hang up and try again";
                // Message that Plivo reads when the caller enters an invalid number
                String WronginputMessage = "Sorry, that's not a valid entry";
                // Sales Phone Number
                String salesPhoneNumber = "+15671234567";

                // Support Phone number
                String supprtPhoneNumber = "+15671234578";

                // GET: /<controller>/
                public IActionResult Index()
                {
                    var resp = new Response();
                    Plivo.XML.GetInput get_input = new
                        Plivo.XML.GetInput("",
                            new Dictionary<string, string>()
                            {
                                {"action", "https://<yourdomain>.com/ivr/firstbranch/"},
                                {"method", "POST"},
                                {"digitEndTimeout", "5"},
                                {"inputType", "dtmf"},
                                {"redirect", "true"},
                            });
                    resp.Add(get_input);
                    get_input.AddSpeak(IvrMessage,
                        new Dictionary<string, string>() { });
                    resp.AddSpeak(NoinputMessage,
                        new Dictionary<string, string>() { });

                    var output = resp.ToString();
                    return this.Content(output, "text/xml");
                }
                // First branch of IVR phone tree
                public IActionResult FirstBranch()
                {
                    String digit = Request.Query["Digits"];
                    Debug.WriteLine("Digit pressed : {0}", digit);

                    var resp = new Response();

                    if (digit == "1")
                    {
                        String getinput_action_url = "https://<yourdomain>.com/ivr/secondbranch/";

                        Plivo.XML.Dial dial = new Plivo.XML.Dial(new
        				Dictionary<string, string>() {{}});

        			    dial.AddNumber(salesPhoneNumber,
        				new Dictionary<string, string>() { });
        			    resp.Add(dial);
                    }
                    else if (digit == "2")
                    {
                        Plivo.XML.Dial dial = new Plivo.XML.Dial(new
        				Dictionary<string, string>() {{}});
                        dial.AddNumber(supprtPhoneNumber,
        				new Dictionary<string, string>() { });
        			    resp.Add(dial);
                    }
                    else
                    {
                        // Add Speak XML tag
                        resp.AddSpeak(WronginputMessage,new Dictionary<string, string>() { });
                    }

                    Debug.WriteLine(resp.ToString());

                    var output = resp.ToString();
                    return this.Content(output, "text/xml");
                }
            }
        }
        ```

        Before starting the application, edit Properties/launchSettings.json and set the applicationUrl as

        "applicationUrl": "[http://localhost:5000/](http://localhost:5000/)"

        Run the project and you should see your basic server application in action at [http://localhost:5000/ivr/](http://localhost:5000/ivr/).

        [Set up ngrok](/sdk/server/set-up-dotnet-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

        ## Create a Plivo application

        Associate the MVC controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Phone IVR`. Enter the server URL you want to use (for example `https://<yourdomain>.com/ivr/`) in the `Answer URL` field and set the method to `GET`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_phoneivr-dotnet.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=8ec9f78fd432aed5f08c04931d7fd3b2" alt="" width="1440" height="822" data-path="images/create_phoneivr-dotnet.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Phone IVR` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_phoneIVR.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=3d1d4946b0eccb2bb844fc674dbb7ea2" alt="" width="1440" height="785" data-path="images/assign_phoneIVR.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo phone number and see how the IVR application works.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Java">
    ## Overview

    Interactive voice response (IVR) systems let incoming callers access information and find contacts via a menu of prerecorded messages, without having to speak to an agent, and let you automate polling via outgoing calls. Callers and call recipients can respond to prompts via Touch-Tone keypad presses or speech recognition. IVR systems can handle larger call volumes than operators and reduce costs associated with customer service.

    Common IVR use cases include:

    * **Auto-attendant**: You can replace a receptionist with an IVR system that routes calls to agents during business hours and accepts voicemail when no one is available.
    * **Call center**: You can route calls coming in to call centers to the appropriate representatives based on user input.
    * **Surveys, polling, and voting**: You can implement IVR in outbound calls to collect customer satisfaction scores or conduct political polling.
    * **Appointment reminders**: You can send automated reminders to customers before their scheduled visits to help avoid missed appointments and facilitate rescheduling.
    * **Lead assignment and lead routing**: For inbound sales calls, you can set up an IVR menu with a set of qualifying questions to discover a customer’s interests, then redirect their call to a representative based on their responses.

    This guide shows how to build an IVR menu system on the Plivo platform, either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement an IVR system with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/au8SCJEHrNU" title="How to Set Up a Professional IVR System with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.
        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong>
            The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>
        * Click the **Start** node to open the Configuration tab, then enter information that other nodes can retrieve in the API Request section — in this case, the From and optionally To numbers for the IVR system.
        * From the list of components on the left side, drag and drop the **IVR Menu** component onto the canvas. When a component is placed on the canvas it becomes a node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr_component.mp4?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=2e441bc6a99e39e3b7f38747aee4715c" data-path="images/ivr_component.mp4" />
          </Frame>
        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **IVR Menu** node.
        * In the Configuration tab at the right of the canvas, configure the choices for the IVR menu. For this example, select **1** and **2** as allowed choices. Enter a message to play to the user in the Speak Text box.
        * Once you’ve configured the node, save the configuration by clicking **Validate**. Do the same for each node as you go along.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr_connect.mp4?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=ac61267ec6c575a607186712b72afa43" data-path="images/ivr_connect.mp4" />
          </Frame>
        * Drag and drop two instances of the **Call Forward** component onto the canvas.  Rename them **Connect\_to\_Support** and **Connect\_to\_Sales**. Draw lines to connect the **IVR Menu** node‘s **1** and **2** trigger states to the new nodes.
        * Configure each **Call Forward** node to select the From number using a variable. PHLO will get the number from the key/value pairs set in the Start node. Enter two curly brackets to view all available variables, and choose the appropriate one. For the To number, either enter a fixed number directly into the To field, or use a variable that you configured in the Start node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/connect_to_ivr.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=f2e86bac6245b8f250ef42a8faf85b89" data-path="images/connect_to_ivr.mp4" />
          </Frame>
        * Drag and drop two instances of the **Play Audio** component onto the canvas. Rename the two nodes **No\_Input\_Prompt** and **Invalid\_Input\_Prompt** and configure each to speak a fixed message for callers to hear when they enter no input or invalid input. Draw lines from the **IVR Menu** node‘s No Input and Wrong Input trigger states to the respective nodes, then draw lines from the **Prompt Completed** trigger states of the new nodes back to the IVR Menu node, to give callers another chance to enter a menu choice.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/connect_ivr_invalid.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=36b7a65a75c998c80e2f4c53d425b624" data-path="images/connect_ivr_invalid.mp4" />
          </Frame>
        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/phonesystem-ivr.jpg?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=4fe6398a8b0ba7b21eec99ebfc8128f2" alt="" width="1440" height="785" data-path="images/phonesystem-ivr.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you‘ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now call your Plivo phone number and see how the IVR system works.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here‘s how to implement an IVR system using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=b6746be9ca27e825ced6ea5a60146f21" alt="" width="1446" height="774" data-path="images/ivr.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Spark web application to implement IVR

        Create a Java class called `IVR` and paste into it this code.

        ```java  theme={null}
        import com.plivo.api.exceptions.PlivoValidationException;
        import com.plivo.api.exceptions.PlivoXmlException;
        import com.plivo.api.xml.Dial;
        import com.plivo.api.xml.GetInput;
        import com.plivo.api.xml.Response;
        import com.plivo.api.xml.Speak;
        import com.plivo.api.xml.Number;
        import static spark.Spark.*;

        public class ivr {
            public static void main(String[] args) throws PlivoValidationException, PlivoXmlException {
                // Message that Plivo reads when the caller dials in
                String ivrMessage = "Welcome to the demo. Press 1 to contact sales. Press 2 to contact support";
                // Message that Plivo reads when the caller does nothing
                String noInputMessage = "Sorry, I didn't catch that. Please hang up and try again";
                // Message that Plivo reads when the caller enters an invalid number
                String wrongInputMessage = "Sorry, that's not a valid entry";
                // Sales Phone number
                final String salesPhoneNumber = "+15671234567";
                // Support Phone number
                final String supportPhoneNumber = "+15671234578";

                post("/ivr/", (req, res) -> {
                    res.type("application/xml");
                    Response resp = new Response();
                    resp.children(
                            new GetInput()
                                    .action("https://<yourdomain>.com/ivr/firstbranch/")
                                    .method("POST")
                                    .inputType("dtmf")
                                    .digitEndTimeout(5)
                                    .redirect(true)
                                    .children(
                                            new Speak(ivrMessage)
                                    )
                    );
                    resp.children(new Speak(noInputMessage));
                    return resp.toXmlString();
                });
                post("/ivr/firstbranch/", (req, res) -> {
                    res.type("application/xml");
                    String digit = req.queryParams("Digits");
                    Response resp = new Response();
                    if (digit.equals("1")) {
                        resp.children(
                                new Dial()
                                        .children(
                                                new Number(salesPhoneNumber)
                                        )
                        );
                        resp.children(new Speak(noInputMessage));
                    } else if (digit.equals("2")) {
                        resp.children(
                                new Dial()
                                        .children(
                                                new Number(supportPhoneNumber)
                                        )
                        );
                    } else {
                        resp.children(
                                new Speak(wrongInputMessage)
                        );
                    }
                    return resp.toXmlString();
                });
            }
        }
        ```

        Run the project and you should see your basic server application in action at [http://localhost:4567/ivr/](http://localhost:4567/ivr/).

        [Set up ngrok](/sdk/server/set-up-java-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

        ## Create a Plivo application

        Associate the Spark web application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Phone IVR`. Enter the server URL you want to use (for example `https://<yourdomain>.com/ivr/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_phoneIVR.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=97c9a8eb44f1ad4d35448ff18093677b" alt="" width="1440" height="805" data-path="images/create_phoneIVR.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Phone IVR` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_phoneIVR.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=3d1d4946b0eccb2bb844fc674dbb7ea2" alt="" width="1440" height="785" data-path="images/assign_phoneIVR.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo phone number and see how the IVR application works.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Go">
    ## Overview

    Interactive voice response (IVR) systems let incoming callers access information and find contacts via a menu of prerecorded messages, without having to speak to an agent, and let you automate polling via outgoing calls. Callers and call recipients can respond to prompts via Touch-Tone keypad presses or speech recognition. IVR systems can handle larger call volumes than operators and reduce costs associated with customer service.

    Common IVR use cases include:

    * **Auto-attendant**: You can replace a receptionist with an IVR system that routes calls to agents during business hours and accepts voicemail when no one is available.
    * **Call center**: You can route calls coming in to call centers to the appropriate representatives based on user input.
    * **Surveys, polling, and voting**: You can implement IVR in outbound calls to collect customer satisfaction scores or conduct political polling.
    * **Appointment reminders**: You can send automated reminders to customers before their scheduled visits to help avoid missed appointments and facilitate rescheduling.
    * **Lead assignment and lead routing**: For inbound sales calls, you can set up an IVR menu with a set of qualifying questions to discover a customer’s interests, then redirect their call to a representative based on their responses.

    This guide shows how to build an IVR menu system on the Plivo platform, either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement an IVR system with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/au8SCJEHrNU" title="How to Set Up a Professional IVR System with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.
        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong>
            The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>
        * Click the **Start** node to open the Configuration tab, then enter information that other nodes can retrieve in the API Request section — in this case, the From and optionally To numbers for the IVR system.
        * From the list of components on the left side, drag and drop the **IVR Menu** component onto the canvas. When a component is placed on the canvas it becomes a node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr_component.mp4?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=2e441bc6a99e39e3b7f38747aee4715c" data-path="images/ivr_component.mp4" />
          </Frame>
        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **IVR Menu** node.
        * In the Configuration tab at the right of the canvas, configure the choices for the IVR menu. For this example, select **1** and **2** as allowed choices. Enter a message to play to the user in the Speak Text box.
        * Once you’ve configured the node, save the configuration by clicking **Validate**. Do the same for each node as you go along.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr_connect.mp4?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=ac61267ec6c575a607186712b72afa43" data-path="images/ivr_connect.mp4" />
          </Frame>
        * Drag and drop two instances of the **Call Forward** component onto the canvas.  Rename them **Connect\_to\_Support** and **Connect\_to\_Sales**. Draw lines to connect the **IVR Menu** node‘s **1** and **2** trigger states to the new nodes.
        * Configure each **Call Forward** node to select the From number using a variable. PHLO will get the number from the key/value pairs set in the Start node. Enter two curly brackets to view all available variables, and choose the appropriate one. For the To number, either enter a fixed number directly into the To field, or use a variable that you configured in the Start node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/connect_to_ivr.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=f2e86bac6245b8f250ef42a8faf85b89" data-path="images/connect_to_ivr.mp4" />
          </Frame>
        * Drag and drop two instances of the **Play Audio** component onto the canvas. Rename the two nodes **No\_Input\_Prompt** and **Invalid\_Input\_Prompt** and configure each to speak a fixed message for callers to hear when they enter no input or invalid input. Draw lines from the **IVR Menu** node‘s No Input and Wrong Input trigger states to the respective nodes, then draw lines from the **Prompt Completed** trigger states of the new nodes back to the IVR Menu node, to give callers another chance to enter a menu choice.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/connect_ivr_invalid.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=36b7a65a75c998c80e2f4c53d425b624" data-path="images/connect_ivr_invalid.mp4" />
          </Frame>
        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/phonesystem-ivr.jpg?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=4fe6398a8b0ba7b21eec99ebfc8128f2" alt="" width="1440" height="785" data-path="images/phonesystem-ivr.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you‘ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now call your Plivo phone number and see how the IVR system works.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here‘s how to implement an IVR system using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ivr.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=b6746be9ca27e825ced6ea5a60146f21" alt="" width="1446" height="774" data-path="images/ivr.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Go server to implement IVR

        Create a file called `ivr.go` and paste into it this code.

        ```go  theme={null}
        package main

        import (
        	"github.com/go-martini/martini"
        	"github.com/plivo/plivo-go/v7/xml"
        	"net/http"
        )

        func main() {
        	m := martini.Classic()
        	const
        	(
        	// Message that Plivo reads when the caller dials in
        	WelcomeMessage = "Welcome to the demo. Press 1 to contact sales. Press 2 to contact support"
        	// Message that Plivo reads when the caller does nothing
        	NoInputMessage = "Sorry, I didn't catch that. Please hang up and try again"
        	// Message that Plivo reads when the caller enters an invalid number
        	WrongInputMessage = "Sorry, that's not a valid entry"
        	// Sales phone number
        	SalesPhoneNumber = "+15671234567"
        	// Support phone number
        	SupportPhoneNumber = "+15671234578"
        	)

        	m.Post("/ivr/", func(w http.ResponseWriter, r *http.Request) string {
        		w.Header().Set("Content-Type", "application/xml")
        		response := xml.ResponseElement{
        			Contents: []interface{}{
        				new(xml.GetInputElement).
        				SetAction("https://<yourdomain>.com/ivr/firstbranch/").
        				SetMethod("POST").
        				SetDigitEndTimeout(5).
        				SetInputType("dtmf").
        				SetRedirect(true).
        				SetContents([]interface{}{new(xml.SpeakElement).
        					AddSpeak(WelcomeMessage),
        					}),
        				new(xml.SpeakElement).
        					AddSpeak(NoInputMessage),
        			},
        		}
        		return response.String()
        	})

        	m.Post("/ivr/firstbranch/", func(w http.ResponseWriter, r *http.Request) string {
        	w.Header().Set("Content-Type", "application/xml")
        	digit := r.FormValue("Digits")
        	if digit == "1" {
        		return xml.ResponseElement{
        		Contents: []interface{}{
        			new(xml.DialElement).

        				SetContents(
        					[]interface{}{
        						new(xml.NumberElement).
        							SetContents(SalesPhoneNumber),
        					},
        				),
        		},
        	}.String()
        	} else if digit == "2" {
        		return xml.ResponseElement{
        		Contents: []interface{}{

        			new(xml.DialElement).
        				SetContents(
        					[]interface{}{
        						new(xml.NumberElement).
        							SetContents(SupportPhoneNumber),
        					},
        				),
        		},
        	}.String()
        	} else {
        		return xml.ResponseElement{
        			Contents: []interface{}{
        				new(xml.SpeakElement).
        					AddSpeak(WrongInputMessage),
        				},
        			}.String()
        		}
        	})
        	m.Run()
        }
        ```

        Save the file and run it.

        ```shell  theme={null}
        $ go run ivr.go
        ```

        You should see your basic server application in action at [http://localhost:8080/ivr/](http://localhost:8080/ivr/).

        [Set up ngrok](/sdk/server/set-up-go-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

        ## Create a Plivo application

        Associate the Go server you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application#create-an-application).

        Give your application a name — we called ours `Phone IVR`. Enter the server URL you want to use (for example `https://<yourdomain>.com/ivr/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_phoneIVR.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=97c9a8eb44f1ad4d35448ff18093677b" alt="" width="1440" height="805" data-path="images/create_phoneIVR.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Phone IVR` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_phoneIVR.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=3d1d4946b0eccb2bb844fc674dbb7ea2" alt="" width="1440" height="785" data-path="images/assign_phoneIVR.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo phone number and see how the IVR application works.
      </Tab>
    </Tabs>
  </Tab>
</Tabs>
