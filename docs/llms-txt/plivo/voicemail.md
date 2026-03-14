# Source: https://plivo.com/docs/voice/use-cases/voicemail.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Voicemail

> Set up voicemail to capture caller messages when recipients are unavailable

<Tabs>
  <Tab title="Node">
    ## Overview

    You can use voicemail to capture a caller’s message if a call recipient is unavailable. This guide shows how to set up voicemail, either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement voicemail with a few clicks on the PHLO canvas.

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=ae83dbedd71dfbdda471ba054f8b3eb7" alt="" width="1446" height="774" data-path="images/voicemail.png" />
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

        * Click the **Start** node to open the Configuration tab, then enter **from** and **to** as keys in the API Request section. To keep the PHLO dynamic, don‘t enter values for the  variables.

        * Once you’ve configured the node, save the configuration by clicking **Validate**. Do the same for each node as you go along.

        * From the list of components on the left side, drag and drop the **Record Audio** component onto the canvas. When a component is placed on the canvas it becomes a node. In its Configuration tab, give the node a descriptive name, such as Voicemail\_Message, and enter text for a message you want to play to callers.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Record Audio** node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail_message.mp4?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=950cbf540558e96e0335d48dbbd179c9" data-path="images/voicemail_message.mp4" />
          </Frame>

        * Once a message is recorded, send the URL of the recording to a responsible party. To do that, drag and drop the **Send Message** component into the canvas, and rename it **Send\_Recording\_URL**.

        * In its Configuration tab, enter variables for the From and To fields. Enter two curly brackets to view all available variables, and choose the appropriate ones. PHLO will get the number from the key/value pairs set in the Start node. In the Message field, enter a message that provides context for the voicemail recipient. The message can be static or dynamic or a combination of the two.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.jfif?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=1c802d3ab2ec2d21eacb477c9c4f7107" alt="" width="1440" height="785" data-path="images/voicemail.jfif" />
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

        You can now call your Plivo phone number and see how the voicemail PHLO works.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to implement voicemail using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=ae83dbedd71dfbdda471ba054f8b3eb7" alt="" width="1446" height="774" data-path="images/voicemail.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an Express server to implement voicemail

        Create a file called `voicemail.js` and paste into it this code.

        ```js  theme={null}
        var plivo = require('plivo');
        var express = require('express');
        var bodyParser = require('body-parser');
        var app = express();

        app.use(bodyParser.urlencoded({extended: true}));
        app.set('port', (process.env.PORT || 5000));

        app.post('/voicemail/', function(request, response) {
          var r = plivo.Response();
          var params;
          params = {
            'action': "https://<yourdomain>.com/get_recording/",
            'finishOnKey': "*",
            'maxLength': "20"
          };
          r.addRecord(params);
          var second_speak_body = "Recording not received";
          r.addSpeak(second_speak_body);

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
        $ node voicemail.js
        ```

        You should see your basic server application in action at [http://localhost:3000/voicemail/](http://localhost:3000/voicemail/).

        ## Create a Plivo application for voicemail

        Associate the Express server you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Voicemail`. Enter the server URL you want to use (for example `https://<yourdomain>.com/voicemail/`) in the `Answer URL` field and set the method to `GET`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create-voicemail.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=7aa089545ca416c50e69c0ff6e16c204" alt="" width="1436" height="764" data-path="images/create-voicemail.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Voicemail` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-voicemail.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=814d0f45847d590d3aaeccc5f846d91e" alt="" width="1437" height="767" data-path="images/assign-voicemail.png" />
        </Frame>

        ## Test

        Make a call to your Plivo number and leave yourself a voicemail message.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Ruby">
    ## Overview

    You can use voicemail to capture a caller’s message if a call recipient is unavailable. This guide shows how to set up voicemail, either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement voicemail with a few clicks on the PHLO canvas.

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=ae83dbedd71dfbdda471ba054f8b3eb7" alt="" width="1446" height="774" data-path="images/voicemail.png" />
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

        * Click the **Start** node to open the Configuration tab, then enter **from** and **to** as keys in the API Request section. To keep the PHLO dynamic, don‘t enter values for the  variables.

        * Once you’ve configured the node, save the configuration by clicking **Validate**. Do the same for each node as you go along.

        * From the list of components on the left side, drag and drop the **Record Audio** component onto the canvas. When a component is placed on the canvas it becomes a node. In its Configuration tab, give the node a descriptive name, such as Voicemail\_Message, and enter text for a message you want to play to callers.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Record Audio** node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail_message.mp4?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=950cbf540558e96e0335d48dbbd179c9" data-path="images/voicemail_message.mp4" />
          </Frame>

        * Once a message is recorded, send the URL of the recording to a responsible party. To do that, drag and drop the **Send Message** component into the canvas, and rename it **Send\_Recording\_URL**.

        * In its Configuration tab, enter variables for the From and To fields. Enter two curly brackets to view all available variables, and choose the appropriate ones. PHLO will get the number from the key/value pairs set in the Start node. In the Message field, enter a message that provides context for the voicemail recipient. The message can be static or dynamic or a combination of the two.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.jfif?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=1c802d3ab2ec2d21eacb477c9c4f7107" alt="" width="1440" height="785" data-path="images/voicemail.jfif" />
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

        You can now call your Plivo phone number and see how the voicemail PHLO works.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to implement voicemail using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=ae83dbedd71dfbdda471ba054f8b3eb7" alt="" width="1446" height="774" data-path="images/voicemail.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Rails controller to implement voicemail

        Change to the project directory and run this command to create a Rails controller for inbound calls.

        ```shell  theme={null}
        $ rails generate controller Plivo voice
        ```

        This command generates a controller named plivo\_controller in the app/controllers/ directory and a respective view in app/views/plivo. We can delete the view as we do not need it.

        ```shell  theme={null}
        $ rm app/views/plivo/voice.html.erb
        ```

        Edit app/controllers/plivo\_controller.rb and paste this code into the PlivoController class.

        ```ruby  theme={null}
        include Plivo
        include Plivo::XML
        include Plivo::Exceptions

        class PlivoController < ApplicationController
        	def voicemail
        		response = Response.new

        		first_speak_body = 'Please leave a message after the beep. Press the star key when done.'
        		response.addSpeak(first_speak_body)

        		params = {
        			action: 'https://www.foo.com/get_recording/',
        			maxLength: '30',
        			finishOnKey: '*'
        		}
        		response.addRecord(params)

        		second_speak_body = 'Recording not received.'
        		response.addSpeak(second_speak_body)
        				xml = PlivoXML.new(response)
        		render xml: xml.to_xml
        	end
        end
        ```

        ### Add a route

        To add a route for the inbound function in the PlivoController class, edit config/routes.rb and add this line after the inbound route.

        ```shell  theme={null}
        get 'plivo/voicemail'
        ```

        Start the Rails server

        ```shell  theme={null}
        $ rails server
        ```

        You should see your basic server application in action at [http://localhost:3000/plivo/voicemail/](http://localhost:3000/plivo/voicemail/).

        ## Create a Plivo application for voicemail

        Associate the Rails controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Voicemail`. Enter the server URL you want to use (for example `https://<yourdomain>.com/voicemail/`) in the `Answer URL` field and set the method to `GET`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create-voicemail.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=7aa089545ca416c50e69c0ff6e16c204" alt="" width="1436" height="764" data-path="images/create-voicemail.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Voicemail` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-voicemail.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=814d0f45847d590d3aaeccc5f846d91e" alt="" width="1437" height="767" data-path="images/assign-voicemail.png" />
        </Frame>

        ## Test

        Make a call to your Plivo number and leave yourself a voicemail message.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Python">
    ## Overview

    You can use voicemail to capture a caller’s message if a call recipient is unavailable. This guide shows how to set up voicemail, either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement voicemail with a few clicks on the PHLO canvas.

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=ae83dbedd71dfbdda471ba054f8b3eb7" alt="" width="1446" height="774" data-path="images/voicemail.png" />
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

        * Click the **Start** node to open the Configuration tab, then enter **from** and **to** as keys in the API Request section. To keep the PHLO dynamic, don‘t enter values for the  variables.

        * Once you’ve configured the node, save the configuration by clicking **Validate**. Do the same for each node as you go along.

        * From the list of components on the left side, drag and drop the **Record Audio** component onto the canvas. When a component is placed on the canvas it becomes a node. In its Configuration tab, give the node a descriptive name, such as Voicemail\_Message, and enter text for a message you want to play to callers.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Record Audio** node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail_message.mp4?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=950cbf540558e96e0335d48dbbd179c9" data-path="images/voicemail_message.mp4" />
          </Frame>

        * Once a message is recorded, send the URL of the recording to a responsible party. To do that, drag and drop the **Send Message** component into the canvas, and rename it **Send\_Recording\_URL**.

        * In its Configuration tab, enter variables for the From and To fields. Enter two curly brackets to view all available variables, and choose the appropriate ones. PHLO will get the number from the key/value pairs set in the Start node. In the Message field, enter a message that provides context for the voicemail recipient. The message can be static or dynamic or a combination of the two.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.jfif?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=1c802d3ab2ec2d21eacb477c9c4f7107" alt="" width="1440" height="785" data-path="images/voicemail.jfif" />
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

        You can now call your Plivo phone number and see how the voicemail PHLO works.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to implement voicemail using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=ae83dbedd71dfbdda471ba054f8b3eb7" alt="" width="1446" height="774" data-path="images/voicemail.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Flask server to implement voicemail

        Create a file called `voicemail.py` and paste into it this code.

        ```py  theme={null}
        # -*- coding: utf-8 -*-
        from flask import Flask, Response, request, url_for
        from plivo import plivoxml

        app = Flask(__name__)

        @app.route('/voicemail/', methods=['GET','POST'])
        def voicemail():
            response = plivoxml.ResponseElement()
            response.add(
                plivoxml.SpeakElement(
                    'Please leave a message. Press the star key when you\'re done'))
            response.add(
                plivoxml.RecordElement(
                    action='https://<yourdomain>.com/get_recording/',
                    max_length=30,
                    finish_on_key='*'))
            response.add(plivoxml.SpeakElement('Recording not received'))
            return Response(response.to_string(), mimetype='application/xml')

        if __name__ == '__main__':
            app.run(host='0.0.0.0', debug=True)
        ```

        Save the file and run it.

        ```shell  theme={null}
        $ python voicemail.py
        ```

        You should see your basic server application in action at [http://localhost:5000/voicemail/](http://localhost:5000/voicemail/).

        ## Create a Plivo application for voicemail

        Associate the Flask server you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application#create-an-application).

        Give your application a name — we called ours `Voicemail`. Enter the server URL you want to use (for example `https://<yourdomain>.com/voicemail/`) in the `Answer URL` field and set the method to `GET`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create-voicemail.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=7aa089545ca416c50e69c0ff6e16c204" alt="" width="1436" height="764" data-path="images/create-voicemail.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Voicemail` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-voicemail.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=814d0f45847d590d3aaeccc5f846d91e" alt="" width="1437" height="767" data-path="images/assign-voicemail.png" />
        </Frame>

        ## Test

        Make a call to your Plivo number and leave yourself a voicemail message.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="PHP">
    ## Overview

    You can use voicemail to capture a caller’s message if a call recipient is unavailable. This guide shows how to set up voicemail, either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement voicemail with a few clicks on the PHLO canvas.

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=ae83dbedd71dfbdda471ba054f8b3eb7" alt="" width="1446" height="774" data-path="images/voicemail.png" />
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

        * Click the **Start** node to open the Configuration tab, then enter **from** and **to** as keys in the API Request section. To keep the PHLO dynamic, don‘t enter values for the  variables.

        * Once you’ve configured the node, save the configuration by clicking **Validate**. Do the same for each node as you go along.

        * From the list of components on the left side, drag and drop the **Record Audio** component onto the canvas. When a component is placed on the canvas it becomes a node. In its Configuration tab, give the node a descriptive name, such as Voicemail\_Message, and enter text for a message you want to play to callers.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Record Audio** node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail_message.mp4?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=950cbf540558e96e0335d48dbbd179c9" data-path="images/voicemail_message.mp4" />
          </Frame>

        * Once a message is recorded, send the URL of the recording to a responsible party. To do that, drag and drop the **Send Message** component into the canvas, and rename it **Send\_Recording\_URL**.

        * In its Configuration tab, enter variables for the From and To fields. Enter two curly brackets to view all available variables, and choose the appropriate ones. PHLO will get the number from the key/value pairs set in the Start node. In the Message field, enter a message that provides context for the voicemail recipient. The message can be static or dynamic or a combination of the two.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.jfif?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=1c802d3ab2ec2d21eacb477c9c4f7107" alt="" width="1440" height="785" data-path="images/voicemail.jfif" />
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

        You can now call your Plivo phone number and see how the voicemail PHLO works.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to implement voicemail using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=ae83dbedd71dfbdda471ba054f8b3eb7" alt="" width="1446" height="774" data-path="images/voicemail.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Laravel controller to implement voicemail

        Change to the project directory run this command to create a Laravel controller for inbound calls.

        ```shell  theme={null}
        $ php artisan make:controller VoicemailController
        ```

        This generate a controller named VoicemailController in the app/http/controllers/ directory. Edit app/http/controllers/VoicemailController.php and paste into it this code.

        ```php  theme={null}
        <?php

        namespace App\Http\Controllers;
        require '../../vendor/autoload.php';
        use Plivo\RestClient;
        use Plivo\XML\Response;
        use Illuminate\Http\Request;

        class VoicemailController extends Controller
        {
            // Record XML to handle the incoming call
            public function voicemailMain()
            {
              $response = new Response();

              $first_speak_body = "Please leave a message . Press the star key when you're done";

              $response->addSpeak($first_speak_body);

              $params = array(
                 'action' => "https://<yourdomain>.com/get_recording/",
                 'finishOnKey' => "*",
                 'maxLength' => "20"
              );

              $response->addRecord($params);

              $second_speak_body = "Recording not received";
              $response->addSpeak($second_speak_body);
              Header('Content-type: text/xml');
              echo $r->toXML();
            }
        }
        ```

        ### Add a route

        To add a route for the inbound function in the VoicemailController class, edit routes/web.php file and add this line.

        ```shell  theme={null}
        Route::match(['get', 'post'], '/voicemail', 'VoicemailController@voicemailMain');
        ```

        Start the Laravel server.

        ```shell  theme={null}
        $ php artisan serve
        ```

        You should see your basic server application in action at  [http://localhost:8000/voicemail](http://localhost:8000/voicemail).

        ## Create a Plivo application for voicemail

        Associate the Laravel controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Voicemail`. Enter the server URL you want to use (for example `https://<yourdomain>.com/voicemail/`) in the `Answer URL` field and set the method to `GET`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create-voicemail.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=7aa089545ca416c50e69c0ff6e16c204" alt="" width="1436" height="764" data-path="images/create-voicemail.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Voicemail` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-voicemail.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=814d0f45847d590d3aaeccc5f846d91e" alt="" width="1437" height="767" data-path="images/assign-voicemail.png" />
        </Frame>

        ## Test

        Make a call to your Plivo number and leave yourself a voicemail message.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title=".NET">
    ## Overview

    You can use voicemail to capture a caller’s message if a call recipient is unavailable. This guide shows how to set up voicemail, either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement voicemail with a few clicks on the PHLO canvas.

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=ae83dbedd71dfbdda471ba054f8b3eb7" alt="" width="1446" height="774" data-path="images/voicemail.png" />
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

        * Click the **Start** node to open the Configuration tab, then enter **from** and **to** as keys in the API Request section. To keep the PHLO dynamic, don‘t enter values for the  variables.

        * Once you’ve configured the node, save the configuration by clicking **Validate**. Do the same for each node as you go along.

        * From the list of components on the left side, drag and drop the **Record Audio** component onto the canvas. When a component is placed on the canvas it becomes a node. In its Configuration tab, give the node a descriptive name, such as Voicemail\_Message, and enter text for a message you want to play to callers.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Record Audio** node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail_message.mp4?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=950cbf540558e96e0335d48dbbd179c9" data-path="images/voicemail_message.mp4" />
          </Frame>

        * Once a message is recorded, send the URL of the recording to a responsible party. To do that, drag and drop the **Send Message** component into the canvas, and rename it **Send\_Recording\_URL**.

        * In its Configuration tab, enter variables for the From and To fields. Enter two curly brackets to view all available variables, and choose the appropriate ones. PHLO will get the number from the key/value pairs set in the Start node. In the Message field, enter a message that provides context for the voicemail recipient. The message can be static or dynamic or a combination of the two.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.jfif?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=1c802d3ab2ec2d21eacb477c9c4f7107" alt="" width="1440" height="785" data-path="images/voicemail.jfif" />
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

        You can now call your Plivo phone number and see how the voicemail PHLO works.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to implement voicemail using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=ae83dbedd71dfbdda471ba054f8b3eb7" alt="" width="1446" height="774" data-path="images/voicemail.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an MVC controller to implement voicemail

        In Visual Studio, create a controller called `VoicemailController.cs` and paste into it this code.

        ```cs  theme={null}
        using System.Collections.Generic;
        using Microsoft.AspNetCore.Mvc;

        namespace Receivecall.Controllers
        {
            public class VoicemailController : Controller
            {
                // GET: /<controller>/
                public IActionResult Index()
                {
                    Plivo.XML.Response resp = new Plivo.XML.Response();
                    resp.AddSpeak("Please leave a message. Press the star key when you're done",
                        new Dictionary<string, string>() { });
                    resp.AddRecord(new Dictionary<string, string>() {
                        {"action", "https://<yourdomain>.com/get_recording/"},
                        {"finishOnKey", "*"},
                        {"maxLength", "20"},
                        {"playBeep", "true"},
                        {"timeout", "15"}
                    });
                    resp.AddSpeak("Recording not received",
                        new Dictionary<string, string>() { });

                    var output = resp.ToString();
                    return this.Content(output, "text/xml");
                }
            }
        }
        ```

        Save the file. Edit Properties/launchSettings.json and set the applicationUrl.

        "applicationUrl": "[http://localhost:5000/](http://localhost:5000/)"

        Run the project and you should see your basic server application in action at [http://localhost:5000/voicemail/](http://localhost:5000/voicemail/).

        ## Create a Plivo application for voicemail

        Associate the MVC controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Voicemail`. Enter the server URL you want to use (for example `https://<yourdomain>.com/voicemail/`) in the `Answer URL` field and set the method to `GET`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create-voicemail.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=7aa089545ca416c50e69c0ff6e16c204" alt="" width="1436" height="764" data-path="images/create-voicemail.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Voicemail` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-voicemail.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=814d0f45847d590d3aaeccc5f846d91e" alt="" width="1437" height="767" data-path="images/assign-voicemail.png" />
        </Frame>

        ## Test

        Make a call to your Plivo number and leave yourself a voicemail message.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Java">
    ## Overview

    You can use voicemail to capture a caller’s message if a call recipient is unavailable. This guide shows how to set up voicemail, either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement voicemail with a few clicks on the PHLO canvas.

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=ae83dbedd71dfbdda471ba054f8b3eb7" alt="" width="1446" height="774" data-path="images/voicemail.png" />
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

        * Click the **Start** node to open the Configuration tab, then enter **from** and **to** as keys in the API Request section. To keep the PHLO dynamic, don‘t enter values for the  variables.

        * Once you’ve configured the node, save the configuration by clicking **Validate**. Do the same for each node as you go along.

        * From the list of components on the left side, drag and drop the **Record Audio** component onto the canvas. When a component is placed on the canvas it becomes a node. In its Configuration tab, give the node a descriptive name, such as Voicemail\_Message, and enter text for a message you want to play to callers.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Record Audio** node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail_message.mp4?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=950cbf540558e96e0335d48dbbd179c9" data-path="images/voicemail_message.mp4" />
          </Frame>

        * Once a message is recorded, send the URL of the recording to a responsible party. To do that, drag and drop the **Send Message** component into the canvas, and rename it **Send\_Recording\_URL**.

        * In its Configuration tab, enter variables for the From and To fields. Enter two curly brackets to view all available variables, and choose the appropriate ones. PHLO will get the number from the key/value pairs set in the Start node. In the Message field, enter a message that provides context for the voicemail recipient. The message can be static or dynamic or a combination of the two.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.jfif?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=1c802d3ab2ec2d21eacb477c9c4f7107" alt="" width="1440" height="785" data-path="images/voicemail.jfif" />
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

        You can now call your Plivo phone number and see how the voicemail PHLO works.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to implement voicemail using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=ae83dbedd71dfbdda471ba054f8b3eb7" alt="" width="1446" height="774" data-path="images/voicemail.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Spark application to implement voicemail

        Create a Java class called `Voicemail` and paste into it this code.

        ```java  theme={null}
        import static spark.Spark.*;

        import com.plivo.api.xml.GetInput;
        import com.plivo.api.xml.Play;
        import com.plivo.api.xml.Response;
        import com.plivo.api.xml.Speak;

        public class Voicemail {
            public static void main(String[] args) {
                post("/voicemail/", (request, response) -> {
                    response.type("application/xml");
                    Response response = new Response()
                        .children(
                                new Speak("Please leave a message. Press the star key when you're done"),
                                new Record("https://<yourdomain>.com/get_recording/")
                                        .finishOnKey("*")
                                        .maxLength(20),
                                new Speak("Recording not received")
                        );
                    resp.children(new Speak(NoinputMessage));
                    return resp.toXmlString();
                });
            }
        }
        ```

        Save the project and run it. You should see your basic server application in action at [http://localhost:4567/voicemail/](http://localhost:4567/voicemail/).

        ## Create a Plivo application for voicemail

        Associate the Spark application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Voicemail`. Enter the server URL you want to use (for example `https://<yourdomain>.com/voicemail/`) in the `Answer URL` field and set the method to `GET`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create-voicemail.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=7aa089545ca416c50e69c0ff6e16c204" alt="" width="1436" height="764" data-path="images/create-voicemail.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Voicemail` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-voicemail.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=814d0f45847d590d3aaeccc5f846d91e" alt="" width="1437" height="767" data-path="images/assign-voicemail.png" />
        </Frame>

        ## Test

        Make a call to your Plivo number and leave yourself a voicemail message.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Go">
    ## Overview

    You can use voicemail to capture a caller’s message if a call recipient is unavailable. This guide shows how to set up voicemail, either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a workflow to implement voicemail with a few clicks on the PHLO canvas.

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=ae83dbedd71dfbdda471ba054f8b3eb7" alt="" width="1446" height="774" data-path="images/voicemail.png" />
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

        * Click the **Start** node to open the Configuration tab, then enter **from** and **to** as keys in the API Request section. To keep the PHLO dynamic, don‘t enter values for the  variables.

        * Once you’ve configured the node, save the configuration by clicking **Validate**. Do the same for each node as you go along.

        * From the list of components on the left side, drag and drop the **Record Audio** component onto the canvas. When a component is placed on the canvas it becomes a node. In its Configuration tab, give the node a descriptive name, such as Voicemail\_Message, and enter text for a message you want to play to callers.

        * Draw a line to connect the **Start** node‘s **Incoming Call** trigger state to the **Record Audio** node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail_message.mp4?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=950cbf540558e96e0335d48dbbd179c9" data-path="images/voicemail_message.mp4" />
          </Frame>

        * Once a message is recorded, send the URL of the recording to a responsible party. To do that, drag and drop the **Send Message** component into the canvas, and rename it **Send\_Recording\_URL**.

        * In its Configuration tab, enter variables for the From and To fields. Enter two curly brackets to view all available variables, and choose the appropriate ones. PHLO will get the number from the key/value pairs set in the Start node. In the Message field, enter a message that provides context for the voicemail recipient. The message can be static or dynamic or a combination of the two.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your complete PHLO should look like this.

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.jfif?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=1c802d3ab2ec2d21eacb477c9c4f7107" alt="" width="1440" height="785" data-path="images/voicemail.jfif" />
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

        You can now call your Plivo phone number and see how the voicemail PHLO works.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to implement voicemail using XML.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/voicemail.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=ae83dbedd71dfbdda471ba054f8b3eb7" alt="" width="1446" height="774" data-path="images/voicemail.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Go server to implement voicemail

        Create a file called `voicemail.go` and paste into it this code.

        ```go  theme={null}
        package main

        import (
        	"github.com/go-martini/martini"
        	"github.com/plivo/plivo-go/v7/xml"
        	"net/http"
        )

        func main() {
        	m := martini.Classic()

        	m.Post("/voicemail/", func(w http.ResponseWriter, r *http.Request) string {
        		w.Header().Set("Content-Type", "application/xml")
        		response := xml.ResponseElement{
        		Contents: []interface{}{
        				new(xml.SpeakElement).
        					AddSpeak("Please leave a message. Press the star key when you're done"),
        				new(xml.RecordElement).
        					SetAction("https://<yourdomain>.com/get_recording/").
        					SetFinishOnKey("*").
        					SetMaxLength(20),

        				new(xml.SpeakElement).
        					AddSpeak("Recording not received"),
        			},
        		}
        		return response.String()
        	})

        	m.Run()
        }
        ```

        Save the file and run it.

        ```shell  theme={null}
        $ go run voicemail.go
        ```

        You should see your basic server application in action at [http://localhost:8080/voicemail/](http://localhost:8080/voicemail/).

        ## Create a Plivo application for voicemail

        Associate the Go application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Voicemail`. Enter the server URL you want to use (for example `https://<yourdomain>.com/voicemail/`) in the `Answer URL` field and set the method to `GET`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create-voicemail.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=7aa089545ca416c50e69c0ff6e16c204" alt="" width="1436" height="764" data-path="images/create-voicemail.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Voicemail` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-voicemail.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=814d0f45847d590d3aaeccc5f846d91e" alt="" width="1437" height="767" data-path="images/assign-voicemail.png" />
        </Frame>

        ## Test

        Make a call to your Plivo number and leave yourself a voicemail message.
      </Tab>
    </Tabs>
  </Tab>
</Tabs>
