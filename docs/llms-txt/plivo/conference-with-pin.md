# Source: https://plivo.com/docs/voice/use-cases/conference-with-pin.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Conference Calling with a PIN

> Create secure conference calls with PIN-based access control

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to create and configure conference calls with a PIN to let multiple people securely connect to a single call. Only participants who have a specified passcode can enter the conference call.

    You can make conference calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement conference calling with a PIN with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/p4JrSz8P_8w" title="How to Set Up a Secured Voice Conference with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.
          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Conference Bridge** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Conference Bridge** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_component.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=282f5d8fbe965dcd6e7a57443aa6ab32" data-path="images/conf_component.mp4" />
          </Frame>

        * In the Configuration tab at the right of the canvas, under Conference Type, tick Protected, then enter a participant PIN and a moderator PIN for the conference. All participants must enter the participant PIN to connect to the conference. The moderator must use the moderator PIN to start the conference.

        * You can also add an announcement message to greet callers, and configure the hold music.

        * Once you’ve configured the node, click **Validate** to save the configuration.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_protected.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=0361d833e617e9a83ebb958a86b9f561" data-path="images/conf_protected.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conferencewithpin.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=3f5af89f5d3d0e2978b7f0326d08cf3c" alt="" width="1440" height="785" data-path="images/conferencewithpin.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now call to your Plivo phone number and see how callers are added to a conference call that requires PIN validation.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to receive a call on a Plivo number and add the caller to a conference call named “demo” after the caller enters a valid PIN.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/pin.png?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=718b09c4e658170b679d68a1561b0cec" alt="" width="1446" height="774" data-path="images/pin.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an Express server to implement a conference call with PIN

        Create a file called `conference_call.js` and paste into it this code.

        ```js  theme={null}
        var plivo = require('plivo');
        var express = require('express');
        var bodyParser = require('body-parser');
        var app = express();

        app.use(bodyParser.urlencoded({extended: true}));
        app.set('port', (process.env.PORT || 5000));

        // Message that Plivo reads when the caller dials in
        var WelcomeMessage = "Welcome to the demo. Press 1234 to join the conference";
        // Message that Plivo reads when the caller does nothing
        var NoinputMessage = "Sorry, I didn't catch that. Please hang up and try again";
        // Message that Plivo reads when the caller enters an invalid number.
        var WronginputMessage = "Sorry, that's an invalid PIN";

        app.post('/conference/', function(request, response) {
          var r = plivo.Response();
          var getinput_action_url, params, get_input;
          getinput_action_url = request.protocol + '://' + request.headers.host + '/conference/firstbranch/';
          params = {
                'action': getinput_action_url,
                'method': 'POST',
                'inputType': 'dtmf',
                'digitEndTimeout': '5',
                'numDigits': '5',
                'redirect': 'true',
          };
          get_input = r.addGetInput(params);
          get_input.addSpeak(WelcomeMessage);
          r.addSpeak(NoinputMessage);

          console.log(r.toXML());
          response.set({'Content-Type': 'text/xml'});
          response.send(r.toXML());
        });

        app.post('/conference/firstbranch/', function(request, response) {
          var r = plivo.Response();
          var getinput_action_url, params, get_input;
          var digit = request.query.Digits;
          console.log(digit);
          if (digit === '1234') {
            var params = {
                'startConferenceOnEnter': "true",
                'endConferenceOnExit': "true"
            };
            var conference_name = "demo";
            r.addConference(conference_name, params);
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
        $ node conference_call.js
        ```

        You should see your basic server application in action at [http://localhost:3000/conference/](http://localhost:3000/conference/).

        ## Create a Plivo application for the conference call

        Associate the Express application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Conference Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/conference/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_conferenceapp.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=e67a9a1f45d8bb48ad05d5818ed18718" alt="" width="1440" height="805" data-path="images/create_conferenceapp.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Conference Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_conferencecall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=58fa03a1130e7f3aa267ee54e3ef099e" alt="" width="1440" height="700" data-path="images/assign_conferencecall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number. You should be prompted for a PIN, then placed into a conference after PIN validation.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to create and configure conference calls with a PIN to let multiple people securely connect to a single call. Only participants who have a specified passcode can enter the conference call.

    You can make conference calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement conference calling with a PIN with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/p4JrSz8P_8w" title="How to Set Up a Secured Voice Conference with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.
          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Conference Bridge** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Conference Bridge** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_component.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=282f5d8fbe965dcd6e7a57443aa6ab32" data-path="images/conf_component.mp4" />
          </Frame>

        * In the Configuration tab at the right of the canvas, under Conference Type, tick Protected, then enter a participant PIN and a moderator PIN for the conference. All participants must enter the participant PIN to connect to the conference. The moderator must use the moderator PIN to start the conference.

        * You can also add an announcement message to greet callers, and configure the hold music.

        * Once you’ve configured the node, click **Validate** to save the configuration.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_protected.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=0361d833e617e9a83ebb958a86b9f561" data-path="images/conf_protected.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conferencewithpin.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=3f5af89f5d3d0e2978b7f0326d08cf3c" alt="" width="1440" height="785" data-path="images/conferencewithpin.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now call to your Plivo phone number and see how callers are added to a conference call that requires PIN validation.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to receive a call on a Plivo number and add the caller to a conference call named “demo” after the caller enters a valid PIN.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/pin.png?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=718b09c4e658170b679d68a1561b0cec" alt="" width="1446" height="774" data-path="images/pin.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Rails controller to implement a conference call with PIN

        Change to the project directory and run this command to create a Rails controller for inbound calls.

        ```shell  theme={null}
        $ rails generate controller Plivo voice
        ```

        This will generate a controller named plivo\_controller in the app/controllers/ directory and a view in app/views/plivo. We can delete the view as we don’t need it.

        ```shell  theme={null}
        $ rm app/views/plivo/voice.html.erb
        ```

        Edit app/controllers/plivo\_controller.rb and paste this code into the PlivoController class:

        ```ruby  theme={null}
        include Plivo
        include Plivo::XML
        include Plivo::Exceptions

        class PlivoController < ApplicationController
          # Message that Plivo reads when the caller dials in
          $welcome_message = "Welcome to the demo. Press 1234 to join the conference"
          # Message that Plivo reads when the caller does nothing
          $noinput_message = "Sorry, I didn't catch that. Please hang up and try again"
          # Message that Plivo reads when the caller enters an invalid number
          $wronginput_message = "Sorry, that's and invalid PIN"
          def conference
            r = Response.new()

            getinput_action_url = "https://<yourdomain>.com/firstbranch/"
            params = {
                action: getinput_action_url,
                method: 'POST',
                digitEndTimeout: '5',
                inputType:'dtmf',
                numDigits:'4',
                redirect:'true'
            }
            getinput = r.addGetInput(params)
            getinput.addSpeak($welcome_message)
            r.addSpeak($noinput_message)

            xml = PlivoXML.new(r)
            render xml: xml.to_xml
          end
          def firstbranch
            digit = params[:Digits]
            r = Response.new()

            if (digit == "1234")
                params = {
                  'startConferenceOnEnter' => "false",
                  'waitSound' => "https://<yourdomain>.com/waitmusic/"
                }

                conference_name = "demo"
                r.addConference(conference_name, params)
            else
                r.addSpeak($wronginput_message)
            end

            xml = PlivoXML.new(r)
            render xml: xml.to_xml
          end
        end
        ```

        ### Add a route

        Add a route for the inbound function in the PlivoController class. Edit config/routes.rb and add these lines after the inbound route.

        ```shell  theme={null}
        get 'plivo/conference'
        get 'plivo/firstbranch'
        ```

        Now plivo\_controller is ready for your first inbound call. To start the Rails server, run

        ```shell  theme={null}
        $ rails server
        ```

        You should see your basic server application in action at [http://localhost:3000/plivo/conference/](http://localhost:3000/plivo/conference/).

        ## Create a Plivo application for the conference call

        Associate the Rails application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Conference Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/conference_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_conferenceapp.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=e67a9a1f45d8bb48ad05d5818ed18718" alt="" width="1440" height="805" data-path="images/create_conferenceapp.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Conference Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_conferencecall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=58fa03a1130e7f3aa267ee54e3ef099e" alt="" width="1440" height="700" data-path="images/assign_conferencecall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number. You should be prompted for a PIN, then placed into a conference after PIN validation.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to create and configure conference calls with a PIN to let multiple people securely connect to a single call. Only participants who have a specified passcode can enter the conference call.

    You can make conference calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement conference calling with a PIN with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/p4JrSz8P_8w" title="How to Set Up a Secured Voice Conference with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.
          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Conference Bridge** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Conference Bridge** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_component.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=282f5d8fbe965dcd6e7a57443aa6ab32" data-path="images/conf_component.mp4" />
          </Frame>

        * In the Configuration tab at the right of the canvas, under Conference Type, tick Protected, then enter a participant PIN and a moderator PIN for the conference. All participants must enter the participant PIN to connect to the conference. The moderator must use the moderator PIN to start the conference.

        * You can also add an announcement message to greet callers, and configure the hold music.

        * Once you’ve configured the node, click **Validate** to save the configuration.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_protected.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=0361d833e617e9a83ebb958a86b9f561" data-path="images/conf_protected.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conferencewithpin.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=3f5af89f5d3d0e2978b7f0326d08cf3c" alt="" width="1440" height="785" data-path="images/conferencewithpin.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now call to your Plivo phone number and see how callers are added to a conference call that requires PIN validation.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to receive a call on a Plivo number and add the caller to a conference call named “demo” after the caller enters a valid PIN.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/pin.png?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=718b09c4e658170b679d68a1561b0cec" alt="" width="1446" height="774" data-path="images/pin.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Flask application to implement a conference call with PIN

        Create a file called `conference_call.py` and paste into it this code.

        ```py  theme={null}
        # -*- coding: utf-8 -*-
        from flask import Flask, Response, request, url_for
        from plivo import plivoxml

        # Message that Plivo reads when the caller dials in
        welcome_message = "Welcome to the demo. Press 1234 to join the conference"
        # Message that Plivo reads when the caller does nothing
        noinput_message = "Sorry, I didn't catch that. Please hang up and try again"
        # Message that Plivo reads when the caller enters an invalid number
        wronginput_message = "Sorry, that's an invalid PIN"

        app = Flask(__name__)

        @app.route('/conference/', methods=['GET','POST'])
        def conference():
            response = plivoxml.ResponseElement()
            getinput_action_url = "https://<yourdomain>.com/conference/firstbranch/"
            response.add(plivoxml.GetInputElement().
                set_action(getinput_action_url).
                set_method('POST').
                set_input_type('dtmf').
                set_digit_end_timeout(5).
                set_num_digits(4).
                set_redirect(True).add(
                    plivoxml.SpeakElement(welcome_message)))
            response.add(plivoxml.SpeakElement(noinput_message))
            return Response(response.to_string(), mimetype='application/xml')

        @app.route('/conference/firstbranch/', methods=['GET','POST'])
        def firstbranch():
            response = plivoxml.ResponseElement()
            digit = request.values.get('Digits')
            if digit == "1234":
                getinput_action_url = "https://<yourdomain>.com/secondbranch/"
                response.add(
                plivoxml.ConferenceElement(
                    'demo',
                    start_conference_on_enter=False,
                    wait_sound='https://<yourdomain>.com/waitmusic/'))
            else:
                response.add_speak(wronginput_message)
            return Response(response.to_string(), mimetype='application/xml')

        if __name__ == '__main__':
            app.run(host='0.0.0.0', debug=True)
        ```

        Save the file and run it.

        ```shell  theme={null}
        $ python conference_call.py
        ```

        You should see your basic server application in action at [http://localhost:5000/conference/](http://localhost:5000/conference/).

        ## Create a Plivo application for the conference call

        Associate the Flask application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Conference Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/conference/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_conferenceapp.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=e67a9a1f45d8bb48ad05d5818ed18718" alt="" width="1440" height="805" data-path="images/create_conferenceapp.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Conference Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_conferencecall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=58fa03a1130e7f3aa267ee54e3ef099e" alt="" width="1440" height="700" data-path="images/assign_conferencecall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number. You should be prompted for a PIN, then placed into a conference after PIN validation.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to create and configure conference calls with a PIN to let multiple people securely connect to a single call. Only participants who have a specified passcode can enter the conference call.

    You can make conference calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement conference calling with a PIN with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/p4JrSz8P_8w" title="How to Set Up a Secured Voice Conference with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.
          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Conference Bridge** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Conference Bridge** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_component.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=282f5d8fbe965dcd6e7a57443aa6ab32" data-path="images/conf_component.mp4" />
          </Frame>

        * In the Configuration tab at the right of the canvas, under Conference Type, tick Protected, then enter a participant PIN and a moderator PIN for the conference. All participants must enter the participant PIN to connect to the conference. The moderator must use the moderator PIN to start the conference.

        * You can also add an announcement message to greet callers, and configure the hold music.

        * Once you’ve configured the node, click **Validate** to save the configuration.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_protected.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=0361d833e617e9a83ebb958a86b9f561" data-path="images/conf_protected.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conferencewithpin.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=3f5af89f5d3d0e2978b7f0326d08cf3c" alt="" width="1440" height="785" data-path="images/conferencewithpin.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now call to your Plivo phone number and see how callers are added to a conference call that requires PIN validation.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to receive a call on a Plivo number and add the caller to a conference call named “demo” after the caller enters a valid PIN.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/pin.png?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=718b09c4e658170b679d68a1561b0cec" alt="" width="1446" height="774" data-path="images/pin.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Laravel controller to implement a conference call with PIN

        Change to the project directory and run this command to create a Laravel controller for inbound calls.

        ```shell  theme={null}
        $ php artisan make:controller ConferencecallController
        ```

        This generates a controller named ConferencecallController in the app/http/controllers/ directory. Edit app/http/controllers/ConferencecallController.php and add into it this code.

        ```php  theme={null}
        <?php

        namespace App\Http\Controllers;
        require '../../vendor/autoload.php';
        use Plivo\RestClient;
        use Plivo\XML\Response;
        use Illuminate\Http\Request;

        class ConferencecallController extends Controller
        {
            // GetInput XML to handle the incoming call
            public function conferenceCall()
            {
                $welcome_message = "Welcome to the demo. Press 1234 to join the conference"; //  Message that Plivo reads when the caller dials in
                $no_input = "Sorry, I didn't catch that. Please hang up and try again"; // Message that Plivo reads when the caller does nothing
                $response = new Response();
                $get_input = $response->addGetInput(
                            [
                                'action' => "https://<yourdomain>.com/conference/confbranch",
                                'method' => "POST",
                                'digitEndTimeout' => "5",
                                'numDigits' => "4",
                                'inputType' => "dtmf",
                                'redirect' => "true",
                            ]);
                $get_input->addSpeak($welcome_message, ['language'=>"en-US", 'voice'=>"Polly.Salli"]);
                $response->addSpeak($no_input);
                Header('Content-type: text/xml');
                echo $response->toXML();
            }

            public function confBranch(Request $request)
            {
                $wrong_input = "Sorry, that's an invalid PIN"; // Message that Plivo reads when the caller enters an invalid number
                $digit = $request->query('Digits');
                $response = new Response();
                if ($digit=="1234") {
                    $params = array(
                        'startConferenceOnEnter' => "true",
                        'endConferenceOnExit' => "true"
                    );

                    $conference_name = "demo";
                    $response->addConference($conference_name, $params);
                } else {
                    $response->addSpeak($wrong_input);
                }
                Header('Content-type: text/xml');
                echo $response->toXML();
            }
        }
        ```

        ### Add a route

        Add a route for the forward function in the ConferencecallController class. Edit routes/web.php and add these lines.

        ```shell  theme={null}
        Route::match(['get', 'post'], '/conference', 'ConferenceCallController@conferenceCall');
        Route::match(['get', 'post'], '/conference/confbranch', 'ConferenceCallController@confBranch');
        ```

        Now ConferencecallController is ready to forward incoming calls to your Plivo number. Start the Laravel server.

        ```shell  theme={null}
        $ php artisan serve
        ```

        You should see your basic server application in action at [http://localhost:8000/conference/](http://localhost:8000/conference/).

        ## Create a Plivo application for the conference call

        Associate the Laravel application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Conference Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/conference_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_conferenceapp.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=e67a9a1f45d8bb48ad05d5818ed18718" alt="" width="1440" height="805" data-path="images/create_conferenceapp.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Conference Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_conferencecall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=58fa03a1130e7f3aa267ee54e3ef099e" alt="" width="1440" height="700" data-path="images/assign_conferencecall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number. You should be prompted for a PIN, then placed into a conference after PIN validation.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to create and configure conference calls with a PIN to let multiple people securely connect to a single call. Only participants who have a specified passcode can enter the conference call.

    You can make conference calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement conference calling with a PIN with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/p4JrSz8P_8w" title="How to Set Up a Secured Voice Conference with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.
          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Conference Bridge** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Conference Bridge** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_component.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=282f5d8fbe965dcd6e7a57443aa6ab32" data-path="images/conf_component.mp4" />
          </Frame>

        * In the Configuration tab at the right of the canvas, under Conference Type, tick Protected, then enter a participant PIN and a moderator PIN for the conference. All participants must enter the participant PIN to connect to the conference. The moderator must use the moderator PIN to start the conference.

        * You can also add an announcement message to greet callers, and configure the hold music.

        * Once you’ve configured the node, click **Validate** to save the configuration.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_protected.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=0361d833e617e9a83ebb958a86b9f561" data-path="images/conf_protected.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conferencewithpin.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=3f5af89f5d3d0e2978b7f0326d08cf3c" alt="" width="1440" height="785" data-path="images/conferencewithpin.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now call to your Plivo phone number and see how callers are added to a conference call that requires PIN validation.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to receive a call on a Plivo number and add the caller to a conference call named “demo” after the caller enters a valid PIN.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/pin.png?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=718b09c4e658170b679d68a1561b0cec" alt="" width="1446" height="774" data-path="images/pin.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an MVC controller to implement a conference call with PIN

        In Visual Studio, create a controller called `ConferencecallController.cs` and paste into it this code.

        ```cs  theme={null}
        using System;
        using System.Collections.Generic;
        using System.Diagnostics;
        using Microsoft.AspNetCore.Mvc;
        using Plivo.XML;

        namespace Receivecall
        {
            public class ConferencecallController : Controller
            {
                // Message that Plivo reads when the caller dials in
                String WelcomeMessage = "Welcome to the demo. Press 1234 to join the conference";
                // Message that Plivo reads when the caller does nothing
                String NoinputMessage = "Sorry, I didn't catch that. Please hang up and try again";
                // Message that Plivo reads when the caller enters an invalid number
                String WronginputMessage = "Sorry, that's an invalid PIN";

                // GET: /<controller>/
                public IActionResult Index()
                {
                    var resp = new Response();
                    Plivo.XML.GetInput get_input = new
                        Plivo.XML.GetInput("",
                            new Dictionary<string, string>()
                            {
                                {"action", "https://<yourdomain>.com/conference/firstbranch/"},
                                {"method", "POST"},
                                {"digitEndTimeout", "5"},
                                {"numDigits", "4"},
                                {"inputType", "dtmf"},
                                {"redirect", "true"},
                            });
                    resp.Add(get_input);
                    get_input.AddSpeak(WelcomeMessage,
                        new Dictionary<string, string>() { });
                    resp.AddSpeak(NoinputMessage,
                        new Dictionary<string, string>() { });

                    var output = resp.ToString();
                    return this.Content(output, "text/xml");
                }
                // Conference Branch
                public IActionResult FirstBranch()
                {
                    String digit = Request.Query["Digits"];
                    Debug.WriteLine("Digit pressed : {0}", digit);

                    var resp = new Response();

                    if (digit == "1234")
                    {
                        // Add Conference XML Tag
                        resp.AddConference("demo",
                        new Dictionary<string, string>()
                        {
                            {"startConferenceOnEnter", "true"},
                            {"endConferenceOnExit", "true"},
                            {"waitSound", "https://<yourdomain>.com/waitmusic/"}
                        });
                    }
                    else
                    {
                        // Add Speak XML Tag
                        resp.AddSpeak(WronginputMessage,
                            new Dictionary<string, string>() { });
                    }

                    Debug.WriteLine(resp.ToString());

                    var output = resp.ToString();
                    return this.Content(output, "text/xml");
                }
            }
        }
        ```

        Before you start the application, update Properties/launchSettings.json:

        "applicationUrl": "[http://localhost:5000/](http://localhost:5000/)"

        Run the project and you should see your basic server application in action at [http://localhost:5000/conference/](http://localhost:5000/conference/).

        ## Create a Plivo application for the conference call

        Associate the .NET application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Conference Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/conference/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_conferenceapp.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=e67a9a1f45d8bb48ad05d5818ed18718" alt="" width="1440" height="805" data-path="images/create_conferenceapp.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Conference Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_conferencecall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=58fa03a1130e7f3aa267ee54e3ef099e" alt="" width="1440" height="700" data-path="images/assign_conferencecall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number. You should be prompted for a PIN, then placed into a conference after PIN validation.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to create and configure conference calls with a PIN to let multiple people securely connect to a single call. Only participants who have a specified passcode can enter the conference call.

    You can make conference calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement conference calling with a PIN with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/p4JrSz8P_8w" title="How to Set Up a Secured Voice Conference with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.
          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Conference Bridge** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Conference Bridge** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_component.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=282f5d8fbe965dcd6e7a57443aa6ab32" data-path="images/conf_component.mp4" />
          </Frame>

        * In the Configuration tab at the right of the canvas, under Conference Type, tick Protected, then enter a participant PIN and a moderator PIN for the conference. All participants must enter the participant PIN to connect to the conference. The moderator must use the moderator PIN to start the conference.

        * You can also add an announcement message to greet callers, and configure the hold music.

        * Once you’ve configured the node, click **Validate** to save the configuration.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_protected.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=0361d833e617e9a83ebb958a86b9f561" data-path="images/conf_protected.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conferencewithpin.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=3f5af89f5d3d0e2978b7f0326d08cf3c" alt="" width="1440" height="785" data-path="images/conferencewithpin.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now call to your Plivo phone number and see how callers are added to a conference call that requires PIN validation.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to receive a call on a Plivo number and add the caller to a conference call named “demo” after the caller enters a valid PIN.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/pin.png?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=718b09c4e658170b679d68a1561b0cec" alt="" width="1446" height="774" data-path="images/pin.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Spark application to implement a conference call with PIN

        Create a Java class called `ConferenceCall` and paste into it this code.

        ```java  theme={null}
        import com.plivo.api.xml.*;

        import static spark.Spark.post;

        public class ConferenceCall {
            public static void main(String[] args) {
                // Message that Plivo reads when the caller dials in
                String WelcomeMessage = "Welcome to the demo. Press 1234 to join the conference";
                // Message that Plivo reads when the caller does nothing
                String NoinputMessage = "Sorry, I didn't catch that. Please hang up and try again";
                // Message that Plivo reads when the caller enters an invalid number
                String WronginputMessage = "Sorry, that's an invalid PIN";
                post("/conference/", (request, response) -> {
                    response.type("application/xml");
                    Response resp = new Response();
                    resp.children(
                            new GetInput()
                                    .action("https://<yourdomain>.com/ivr/firstbranch/")
                                    .method("POST")
                                    .inputType("dtmf")
                                    .digitEndTimeout(5)
                                    .numDigits(4)
                                    .redirect(true)
                                    .children(
                                            new Speak(WelcomeMessage)
                                    )
                    );
                    resp.children(new Speak(NoinputMessage));
                    return resp.toXmlString();
                });
                post("/conference/firstbranch/", (request, response) -> {
                    response.type("application/xml");
                    String digit = request.queryParams("Digits");
                    Response resp = new Response();
                    if (digit.equals("1234")){
                        resp.children(
                                new Speak("You will now be placed into the demo conference"),
                                new Conference("demo")
                                        .endConferenceOnExit(true)
                                        .startConferenceOnEnter(false)
                                        .waitSound("https://<yourdomain>.com/waitmusic/")

                        );
                        resp.children(new Speak(NoinputMessage));
                    }
                    else {
                        resp.children(
                                new Speak(WronginputMessage)
                        );
                    }
                    return resp.toXmlString();
                });
            }
        }
        ```

        Save the file and run it. You should see your basic server application in action at [http://localhost:4567/conference/](http://localhost:4567/conference/).

        ## Create a Plivo application for the conference call

        Associate the Spark application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Conference Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/conference/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_conferenceapp.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=e67a9a1f45d8bb48ad05d5818ed18718" alt="" width="1440" height="805" data-path="images/create_conferenceapp.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Conference Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_conferencecall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=58fa03a1130e7f3aa267ee54e3ef099e" alt="" width="1440" height="700" data-path="images/assign_conferencecall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number. You should be prompted for a PIN, then placed into a conference after PIN validation.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to create and configure conference calls with a PIN to let multiple people securely connect to a single call. Only participants who have a specified passcode can enter the conference call.

    You can make conference calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement conference calling with a PIN with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/p4JrSz8P_8w" title="How to Set Up a Secured Voice Conference with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **CREATE NEW PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.
          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Conference Bridge** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Conference Bridge** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_component.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=282f5d8fbe965dcd6e7a57443aa6ab32" data-path="images/conf_component.mp4" />
          </Frame>

        * In the Configuration tab at the right of the canvas, under Conference Type, tick Protected, then enter a participant PIN and a moderator PIN for the conference. All participants must enter the participant PIN to connect to the conference. The moderator must use the moderator PIN to start the conference.

        * You can also add an announcement message to greet callers, and configure the hold music.

        * Once you’ve configured the node, click **Validate** to save the configuration.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_protected.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=0361d833e617e9a83ebb958a86b9f561" data-path="images/conf_protected.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conferencewithpin.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=3f5af89f5d3d0e2978b7f0326d08cf3c" alt="" width="1440" height="785" data-path="images/conferencewithpin.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now call to your Plivo phone number and see how callers are added to a conference call that requires PIN validation.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to receive a call on a Plivo number and add the caller to a conference call named “demo” after the caller enters a valid PIN.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/pin.png?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=718b09c4e658170b679d68a1561b0cec" alt="" width="1446" height="774" data-path="images/pin.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Go server to implement a conference call with PIN

        Create a file called `conference_call.go` and paste into it this code.

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
        	WelcomeMessage = "Welcome to the demo. Press 1234 to join the conference"
        	// Message that Plivo reads when the caller does nothing
        	NoInputMessage = "Sorry, I didn't catch that. Please hang up and try again"
        	// Message that Plivo reads when the caller enters an invalid number
        	WrongInputMessage = "Sorry, that's an invalid PIN"
        	)

        	m.Post("/conference/", func(w http.ResponseWriter, r *http.Request) string {
        		w.Header().Set("Content-Type", "application/xml")
        		response := xml.ResponseElement{
        			Contents: []interface{}{
        				new(xml.GetInputElement).
        				SetAction("https://<yourdomain>.com/ivr/firstbranch/").
        				SetMethod("POST").
        				SetDigitEndTimeout(5).
        				SetInputType("dtmf").
        				SetNumDigits(4).
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

        	m.Post("/conference/firstbranch/", func(w http.ResponseWriter, r *http.Request) string {
        	w.Header().Set("Content-Type", "application/xml")
        	digit := r.FormValue("Digits")
        	if digit == "1234" {
        		return xml.ResponseElement{
        			Contents: []interface{} {
        				new(xml.SpeakElement).
        				AddSpeak("You will now be placed into the demo conference"),
        				new(xml.ConferenceElement).
        				SetEndConferenceOnExit(true).
        				SetStartConferenceOnEnter(false).
        				SetWaitSound("https://<yourdomain>.com/waitmusic/").
        				SetContents("demo"),

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
        $ go run conference_call.go
        ```

        You should see your basic server application in action at [http://localhost:8080/conference/](http://localhost:8080/conference/).

        ## Create a Plivo application for the conference call

        Associate the Go application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Conference Call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/conference/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_conferenceapp.jpg?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=e67a9a1f45d8bb48ad05d5818ed18718" alt="" width="1440" height="805" data-path="images/create_conferenceapp.jpg" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Conference Call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_conferencecall.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=58fa03a1130e7f3aa267ee54e3ef099e" alt="" width="1440" height="700" data-path="images/assign_conferencecall.jpg" />
        </Frame>

        ## Test

        Make a call to your Plivo number. You should be prompted for a PIN, then placed into a conference after PIN validation.
      </Tab>
    </Tabs>
  </Tab>
</Tabs>
