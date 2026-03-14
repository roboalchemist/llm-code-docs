# Source: https://plivo.com/docs/voice/use-cases/call-conference.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PINless Conference Calls

> Set up PINless conference calls to connect multiple participants on one call

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to create and configure conference calling, which lets you connect multiple people to one call at the same time.

    You can implement PINless conference calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement conference calling with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/reJM72ncHFk" title="How to Set Up Voice Conferencing with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
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

        * In the Configuration tab at the right of the canvas, enter a Conference ID for your conference. You can also add an announcement message to greet callers, and configure the hold music.

        * Once you’ve configured the node, click **Validate** to save the configuration.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_component.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=282f5d8fbe965dcd6e7a57443aa6ab32" data-path="images/conf_component.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conferencewithoutpin.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=99ac2b99f74c525c895ed868a2c2bd60" alt="" width="1440" height="785" data-path="images/conferencewithoutpin.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo-pin.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2effd5487030b0ad2802005a59bfdef0" alt="" width="1440" height="785" data-path="images/assign-phlo-pin.png" />
        </Frame>

        ## Test

        You can now call to your Plivo phone number and see how callers are added to a conference call.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to receive a call on a Plivo number and add the caller to a conference call named “demo” using the [Conference XML](/voice/xml/conference/) element.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/pinless-conference.png?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=24bfa7b9d3cc907e8df4bcd8bb2a659b" alt="" width="1446" height="774" data-path="images/pinless-conference.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an Express server to implement a conference call

        Create a file called `conference_call.js` and paste into it this code.

        ```js  theme={null}
        var express = require('express')
        var app = express()

        app.post('/conference_call/', function(req, res) {
            var plivo = require('plivo');
            var response = plivo.Response();

            var speak_body = "You will now be placed into the demo conference";
            response.addSpeak(speak_body);

            var params = {
                'startConferenceOnEnter': "true",
                'endConferenceOnExit': "true"
            };
            var conference_name = "demo";
            response.addConference(conference_name, params);
            res.send(response.toXML());
        })

        app.set('port', (process.env.PORT || 5000));
        app.listen(app.get('port'), function() {
            console.log('Node app is running on port', app.get('port'));
        });
        ```

        Save the file and run it.

        ```shell  theme={null}
        $ node conference_call.js
        ```

        You should see your basic server application in action at [http://localhost:3000/conference\_call/](http://localhost:3000/conference_call/).

        ## Create a Plivo application for the conference call

        Associate the Node.js application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

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

        Make a call to your Plivo number. You should be placed into a conference.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to create and configure conference calling, which lets you connect multiple people to one call at the same time.

    You can implement PINless conference calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement conference calling with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/reJM72ncHFk" title="How to Set Up Voice Conferencing with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
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

        * In the Configuration tab at the right of the canvas, enter a Conference ID for your conference. You can also add an announcement message to greet callers, and configure the hold music.

        * Once you’ve configured the node, click **Validate** to save the configuration.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_component.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=282f5d8fbe965dcd6e7a57443aa6ab32" data-path="images/conf_component.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conferencewithoutpin.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=99ac2b99f74c525c895ed868a2c2bd60" alt="" width="1440" height="785" data-path="images/conferencewithoutpin.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo-pin.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2effd5487030b0ad2802005a59bfdef0" alt="" width="1440" height="785" data-path="images/assign-phlo-pin.png" />
        </Frame>

        ## Test

        You can now call to your Plivo phone number and see how callers are added to a conference call.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to receive a call on a Plivo number and add the caller to a conference call named “demo” using the [Conference XML](/voice/xml/conference/) element.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/pinless-conference.png?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=24bfa7b9d3cc907e8df4bcd8bb2a659b" alt="" width="1446" height="774" data-path="images/pinless-conference.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Rails controller to implement a conference call

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
        def conference
          response = Response.new

          speak_body = 'You will now be placed into the demo conference'
          response.addSpeak(speak_body)

          params = {
            'startConferenceOnEnter' => "false",
            'waitSound' => "https://<yourdomain>.com/waitmusic/"
          }

          conference_name = "demo"
          response.addConference(conference_name, params)

          xml = PlivoXML.new(response)
          puts xml.to_xml
          render xml: xml.to_xml
         end
        ```

        ### Add a route

        Add a route for the inbound function in the PlivoController class. Edit config/routes.rb and add the line below after the inbound route:

        ```shell  theme={null}
        get 'plivo/conference'
        ```

        Now plivo\_controller is ready to forward incoming calls to your Plivo number. To start the Rails server, run

        ```shell  theme={null}
        $ rails server
        ```

        You should see your basic server application in action at [http://localhost:3000/plivo/conference/](http://localhost:3000/plivo/conference/).

        ## Create a Plivo application for the conference call

        Associate the Go application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application#create-an-application).

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

        Make a call to your Plivo number. You should be placed into a conference.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to create and configure conference calling, which lets you connect multiple people to one call at the same time.

    You can implement PINless conference calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement conference calling with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/reJM72ncHFk" title="How to Set Up Voice Conferencing with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
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

        * In the Configuration tab at the right of the canvas, enter a Conference ID for your conference. You can also add an announcement message to greet callers, and configure the hold music.

        * Once you’ve configured the node, click **Validate** to save the configuration.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_component.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=282f5d8fbe965dcd6e7a57443aa6ab32" data-path="images/conf_component.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conferencewithoutpin.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=99ac2b99f74c525c895ed868a2c2bd60" alt="" width="1440" height="785" data-path="images/conferencewithoutpin.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo-pin.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2effd5487030b0ad2802005a59bfdef0" alt="" width="1440" height="785" data-path="images/assign-phlo-pin.png" />
        </Frame>

        ## Test

        You can now call to your Plivo phone number and see how callers are added to a conference call.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to receive a call on a Plivo number and add the caller to a conference call named “demo” using the [Conference XML](/voice/xml/conference/) element.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/pinless-conference.png?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=24bfa7b9d3cc907e8df4bcd8bb2a659b" alt="" width="1446" height="774" data-path="images/pinless-conference.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Flask application to implement a conference call

        Create a file called `conference_call.py` and paste into it this code.

        ```py  theme={null}
        from flask import Flask, Response
        from plivo import plivoxml

        app = Flask(__name__)

        @app.route('/conference_call/', methods=['GET', 'POST'])
        def conference_cal():

            response = plivoxml.ResponseElement()
            response.add(plivoxml.SpeakElement('You will now be placed into the demo conference'))
            response.add(
                plivoxml.ConferenceElement(
                    'demo',
                    start_conference_on_enter=False,
                    wait_sound='https://<yourdomain>.com/waitmusic/'))

            return Response(response.to_string(), mimetype='application/xml')

        if __name__ == '__main__':
            app.run(host='0.0.0.0', debug=True)
        ```

        Save the file and run it.

        ```shell  theme={null}
        $ python conference_call.py
        ```

        You should see your basic server application in action at [http://localhost:5000/conference\_call/](http://localhost:5000/conference_call/).

        ## Create a Plivo application for the conference call

        Associate the Python application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

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

        Make a call to your Plivo number. You should be placed into a conference.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to create and configure conference calling, which lets you connect multiple people to one call at the same time.

    You can implement PINless conference calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement conference calling with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/reJM72ncHFk" title="How to Set Up Voice Conferencing with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
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

        * In the Configuration tab at the right of the canvas, enter a Conference ID for your conference. You can also add an announcement message to greet callers, and configure the hold music.

        * Once you’ve configured the node, click **Validate** to save the configuration.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_component.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=282f5d8fbe965dcd6e7a57443aa6ab32" data-path="images/conf_component.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conferencewithoutpin.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=99ac2b99f74c525c895ed868a2c2bd60" alt="" width="1440" height="785" data-path="images/conferencewithoutpin.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo-pin.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2effd5487030b0ad2802005a59bfdef0" alt="" width="1440" height="785" data-path="images/assign-phlo-pin.png" />
        </Frame>

        ## Test

        You can now call to your Plivo phone number and see how callers are added to a conference call.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to receive a call on a Plivo number and add the caller to a conference call named “demo” using the [Conference XML](/voice/xml/conference/) element.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/pinless-conference.png?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=24bfa7b9d3cc907e8df4bcd8bb2a659b" alt="" width="1446" height="774" data-path="images/pinless-conference.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Laravel controller to implement a conference call

        Change to the project directory and run this command to create a Laravel controller for inbound calls.

        ```shell  theme={null}
        $ php artisan make:controller VoiceController
        ```

        Edit the app/http/controllers/voiceController.php file and paste into it this code.

        ```php  theme={null}
        <?php

        namespace App\Http\Controllers;
        require '../../vendor/autoload.php';
        use Plivo\RestClient;
        use Plivo\XML\Response;
        use Illuminate\Http\Request;

        class VoiceController extends Controller
        {
            public function conferenceCall()
            {
              $response = new Response();

              $speak_body = "You will now be placed into the demo conference";
              $response->addSpeak($speak_body);

              $params = array(
                 'startConferenceOnEnter' => "true",
                 'endConferenceOnExit' => "true"
              );

              $conference_name = "demo";
              $response->addConference($conference_name, $params);

              Header('Content-type: text/xml');
              echo $response->toXML();
            }
        }
        ```

        ### Add a route

        Add a route for the forward function in the VoiceController class. Edit routes/web.php and add this line.

        ```shell  theme={null}
        Route::match(['get', 'post'], '/conferencecall', 'VoiceController@conferenceCall');
        ```

        Now VoiceController is ready to forward incoming calls to your Plivo number. Start the Laravel server.

        ```shell  theme={null}
        $ php artisan serve
        ```

        You should see your basic server application in action at [http://localhost:8000/conferencecall/](http://localhost:8000/conferencecall/).

        ## Create a Plivo application for the conference call

        Associate the Go application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

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

        Make a call to your Plivo number. You should be placed into a conference.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to create and configure conference calling, which lets you connect multiple people to one call at the same time.

    You can implement PINless conference calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement conference calling with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/reJM72ncHFk" title="How to Set Up Voice Conferencing with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
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

        * In the Configuration tab at the right of the canvas, enter a Conference ID for your conference. You can also add an announcement message to greet callers, and configure the hold music.

        * Once you’ve configured the node, click **Validate** to save the configuration.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_component.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=282f5d8fbe965dcd6e7a57443aa6ab32" data-path="images/conf_component.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conferencewithoutpin.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=99ac2b99f74c525c895ed868a2c2bd60" alt="" width="1440" height="785" data-path="images/conferencewithoutpin.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo-pin.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2effd5487030b0ad2802005a59bfdef0" alt="" width="1440" height="785" data-path="images/assign-phlo-pin.png" />
        </Frame>

        ## Test

        You can now call to your Plivo phone number and see how callers are added to a conference call.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to receive a call on a Plivo number and add the caller to a conference call named “demo” using the [Conference XML](/voice/xml/conference/) element.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/pinless-conference.png?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=24bfa7b9d3cc907e8df4bcd8bb2a659b" alt="" width="1446" height="774" data-path="images/pinless-conference.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an MVC controller to implement a conference call

        In Visual Studio, create a controller called `ConferencecallController.cs` and paste into it this code.

        ```cs  theme={null}
        using System;
        using Plivo.XML;
        using System.Collections.Generic;
        using Microsoft.AspNetCore.Mvc;

        namespace Conferencecall
        {
        	public class ConferencecallController : Controller
        	{
        		public IActionResult Index()
        		{
        			Plivo.XML.Response resp = new Plivo.XML.Response();
        			resp.AddSpeak("You will now be placed into the demo conference",
                     new Dictionary<string, string>() { });
        			resp.AddConference("demo",
                       new Dictionary<string, string>()
        			{
        				{"startConferenceOnEnter", "true"},
        				{"endConferenceOnExit", "true"},
        				{"waitSound", "https://<yourdomain>.com/waitmusic/"}
        			});
        			var output = resp.ToString();
        			Console.WriteLine(output);

        			return this.Content(output, "text/xml");
        		}
        	}
        }
        ```

        Run the project and you should see your basic server application in action at [http://localhost:5000/conferencecall/](http://localhost:5000/conferencecall/).

        ## Create a Plivo application for the conference call

        Associate the .NET application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

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

        Make a call to your Plivo number. You should be placed into a conference.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to create and configure conference calling, which lets you connect multiple people to one call at the same time.

    You can implement PINless conference calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement conference calling with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/reJM72ncHFk" title="How to Set Up Voice Conferencing with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
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

        * In the Configuration tab at the right of the canvas, enter a Conference ID for your conference. You can also add an announcement message to greet callers, and configure the hold music.

        * Once you’ve configured the node, click **Validate** to save the configuration.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_component.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=282f5d8fbe965dcd6e7a57443aa6ab32" data-path="images/conf_component.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conferencewithoutpin.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=99ac2b99f74c525c895ed868a2c2bd60" alt="" width="1440" height="785" data-path="images/conferencewithoutpin.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo-pin.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2effd5487030b0ad2802005a59bfdef0" alt="" width="1440" height="785" data-path="images/assign-phlo-pin.png" />
        </Frame>

        ## Test

        You can now call to your Plivo phone number and see how callers are added to a conference call.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to receive a call on a Plivo number and add the caller to a conference call named “demo” using the [Conference XML](/voice/xml/conference/) element.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/pinless-conference.png?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=24bfa7b9d3cc907e8df4bcd8bb2a659b" alt="" width="1446" height="774" data-path="images/pinless-conference.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Spark application to implement a conference call

        Ceate a Java class called `conferencecall` and paste into it this code.

        ```java  theme={null}
        import static spark.Spark.*;
        import com.plivo.api.xml.Dial;
        import com.plivo.api.xml.Number;
        import com.plivo.api.xml.Response;

        public class conferencecall {
            public static void main(String[] args) {
                get("/conference_call/", (request, response) - > {
                    Response response = new Response()
                    .children(
                        new Speak("You will now be placed into the demo conference"),
                        new Conference("demo")
                        .endConferenceOnExit(true)
                        .startConferenceOnEnter(false)
                        .waitSound("https://<yourdomain>.com/waitmusic/")

                    );
                    System.out.println(response.toXmlString());
                    // Returns the XML
                    return response.toXmlString();
                });
            }
        }
        ```

        Save the file and run the project, and you should see your basic server application in action at [http://localhost:4567/conference\_call/](http://localhost:4567/conference_call/).

        ## Create a Plivo application for the conference call

        Associate the Java application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application#create-an-application).

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

        Make a call to your Plivo number. You should be placed into a conference.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to create and configure conference calling, which lets you connect multiple people to one call at the same time.

    You can implement PINless conference calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement conference calling with a few clicks on the PHLO canvas.

        <Frame>
          <iframe width="515" height="380" src="https://www.youtube.com/embed/reJM72ncHFk" title="How to Set Up Voice Conferencing with PHLO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
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

        * In the Configuration tab at the right of the canvas, enter a Conference ID for your conference. You can also add an announcement message to greet callers, and configure the hold music.

        * Once you’ve configured the node, click **Validate** to save the configuration.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conf_component.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=282f5d8fbe965dcd6e7a57443aa6ab32" data-path="images/conf_component.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/conferencewithoutpin.jpg?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=99ac2b99f74c525c895ed868a2c2bd60" alt="" width="1440" height="785" data-path="images/conferencewithoutpin.jpg" />
        </Frame>

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the phone number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo-pin.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2effd5487030b0ad2802005a59bfdef0" alt="" width="1440" height="785" data-path="images/assign-phlo-pin.png" />
        </Frame>

        ## Test

        You can now call to your Plivo phone number and see how callers are added to a conference call.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to receive a call on a Plivo number and add the caller to a conference call named “demo” using the [Conference XML](/voice/xml/conference/) element.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/pinless-conference.png?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=24bfa7b9d3cc907e8df4bcd8bb2a659b" alt="" width="1446" height="774" data-path="images/pinless-conference.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Go server to implement a conference call

        Create a file called `conference_call.go` and paste into it this code.

        ```go  theme={null}
        package main

        import (
            "net/http"
            "github.com/plivo/plivo-go/v7/xml"

        )

        func handler(w http.ResponseWriter, r *http.Request) {
            response := xml.ResponseElement{
                Contents: []interface{} {
                    new(xml.SpeakElement).
                    AddSpeak("You will now be placed into the demo conference"),
                    new(xml.ConferenceElement).
                    SetEndConferenceOnExit(true).
                    SetStartConferenceOnEnter(false).
                    SetWaitSound("https://<yourdomain>.com/waitmusic/").
                    SetContents("demo"),
                },
            }
            w.Write([]byte(response.String()))
            return
        }

        func main() {
            http.HandleFunc("/conference_call/", handler)
            http.ListenAndServe(":8080", nil)
        }
        ```

        Save the file and run it.

        ```shell  theme={null}
        $ go run conference_call.go
        ```

        You should see your basic server application in action at [http://localhost:8080/conference\_call/](http://localhost:8080/conference_call/).

        ## Create a Plivo application for the conference call

        Associate the Go application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

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

        Make a call to your Plivo number. You should be placed into a conference.
      </Tab>
    </Tabs>
  </Tab>
</Tabs>
