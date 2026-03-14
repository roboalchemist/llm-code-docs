# Source: https://plivo.com/docs/voice/use-cases/receive-incoming-calls.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Receive Incoming Calls

> Handle incoming calls on a Plivo number with text-to-speech greetings

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to receiving incoming calls on a Plivo number and greet callers with a text-to-speech message. Managing incoming calls is a key part of the call flow in many common use cases, such as interactive voice response (IVR), call forwarding, and conference calling.

    You can handle incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to receive an inbound call with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/receive-incoming.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=356ffd22965f7f9ccf8f969617603ee1" alt="" width="1446" height="774" data-path="images/receive-incoming.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/receive_call-phlo.gif?s=722ef75c0f7d1e9f1578237363ce2c03" alt="Create a PHLO to receive incoming call" width="1024" height="560" data-path="images/receive_call-phlo.gif" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Play Audio** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Play Audio** node.

        * In the Configuration pane at the right of the canvas, configure the **Play Audio** node to play a message to the caller.

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="Assign PHLO to a Plivo number" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now make a call to your Plivo phone number and see how the inbound call is handled.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that handles incoming calls on a Plivo number by playing a text-to-speech message to the caller.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/receive-incoming-calls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=fc3a488003b5b2eaa3ebe2302793cf9e" alt="Inbound Call Flow" width="1448" height="774" data-path="images/receive-incoming-calls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo’s text-to-speech engine plays a message using the [Speak](/voice/xml/speak/) XML element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an MVC controller to handle incoming calls

        In Visual Studio, create a new project. Use the template for Web Application (Model-View-Controller).

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_mvcapp.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=342cab800d30d99fb9cdb362a91ccab8" alt="Create an MVC app" width="1198" height="706" data-path="images/create_mvcapp.png" />
        </Frame>

        Give the project a name — we used `Receivecall`.

        <Frame>
                    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/configure_mvcapp.png?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=9c42a016caf26a1d44fc1edbafa2ae14" alt="Configure the MVC app" width="1142" height="701" data-path="images/configure_mvcapp.png" />
        </Frame>

        Navigate to the Controllers directory in the Receivecall project. Create a controller named ReceivecallController.cs and paste into it this code.

        ```cs  theme={null}
        using System;
        using Plivo.XML;
        using System.Collections.Generic;
        using Microsoft.AspNetCore.Mvc;

        namespace Receivecall
        {
            public class ReceivecallController : Controller
            {
                public IActionResult Index()
                {
                    Plivo.XML.Response resp = new Plivo.XML.Response();
                    resp.AddSpeak("Hello, you just received your first call",
                        new Dictionary<string, string>() {
                {
                "loop",
                "3"
                }
                        });
                    var output = resp.ToString();
                    Console.WriteLine(output);

                    return this.Content(output, "text/xml");
                }
            }
        }
        ```

        ## Create a Plivo application to receive calls

        Associate the controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Receive_call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/receive_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_receivecall_app.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=fa56f60792c23523b7597ec4f1f07401" alt="Create Application" width="1440" height="788" data-path="images/create_receivecall_app.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Receive_call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_receivecall_app.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=489823f8c06deb4fa2f087c71ce50b70" alt="Assign Phone Number to Receive Call App" width="1440" height="792" data-path="images/assign_receivecall_app.png" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides. You should hear the text-to-speech message, “Hello, you just received your first call.”
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to receiving incoming calls on a Plivo number and greet callers with a text-to-speech message. Managing incoming calls is a key part of the call flow in many common use cases, such as interactive voice response (IVR), call forwarding, and conference calling.

    You can handle incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to receive an inbound call with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/receive-incoming.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=356ffd22965f7f9ccf8f969617603ee1" alt="" width="1446" height="774" data-path="images/receive-incoming.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintlify.s3.us-west-1.amazonaws.com/plivo/imagesreceive_call-phlo.gif" alt="Create a PHLO to receive incoming call" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Play Audio** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Play Audio** node.

        * In the Configuration pane at the right of the canvas, configure the **Play Audio** node to play a message to the caller.

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="Assign PHLO to a Plivo number" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now make a call to your Plivo phone number and see how the inbound call is handled.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that handles incoming calls on a Plivo number by playing a text-to-speech message to the caller.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/receive-incoming-calls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=fc3a488003b5b2eaa3ebe2302793cf9e" alt="Inbound Call Flow" width="1448" height="774" data-path="images/receive-incoming-calls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo’s text-to-speech engine plays a message using the [Speak](/voice/xml/speak/) XML element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Ruby application to handle incoming calls

        Create a file called `receive_call.rb` and paste into it this code.

        ```rb  theme={null}
        include Plivo
        include Plivo::XML
        include Plivo::Exceptions

        class PlivoController < ApplicationController
         def inbound
            response = Response.new
            speak_body = 'Hello, you just received your first call'
            response.addSpeak(speak_body)

            xml = Plivo::PlivoXML.new(response)
            render xml: xml.to_xml
         end
        end
        ```

        ## Create a Plivo application to receive calls

        Associate the Ruby application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Receive_call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/receive_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_receivecall_app.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=fa56f60792c23523b7597ec4f1f07401" alt="Create Application" width="1440" height="788" data-path="images/create_receivecall_app.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Receive_call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintlify.s3.us-west-1.amazonaws.com/plivo/assign_receivecall_app.png" alt="Assign Phone Number to Receive Call App" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides. You should hear the text-to-speech message, “Hello, you just received your first call.”
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to receiving incoming calls on a Plivo number and greet callers with a text-to-speech message. Managing incoming calls is a key part of the call flow in many common use cases, such as interactive voice response (IVR), call forwarding, and conference calling.

    You can handle incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to receive an inbound call with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/receive-incoming.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=356ffd22965f7f9ccf8f969617603ee1" alt="" width="1446" height="774" data-path="images/receive-incoming.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintlify.s3.us-west-1.amazonaws.com/plivo/imagesreceive_call-phlo.gif" alt="Create a PHLO to receive incoming call" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Play Audio** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Play Audio** node.

        * In the Configuration pane at the right of the canvas, configure the **Play Audio** node to play a message to the caller.

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="Assign PHLO to a Plivo number" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now make a call to your Plivo phone number and see how the inbound call is handled.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that handles incoming calls on a Plivo number by playing a text-to-speech message to the caller.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/receive-incoming-calls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=fc3a488003b5b2eaa3ebe2302793cf9e" alt="Inbound Call Flow" width="1448" height="774" data-path="images/receive-incoming-calls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo’s text-to-speech engine plays a message using the [Speak](/voice/xml/speak/) XML element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Flask server to handle incoming calls

        Create a file called `receive_call.py` and paste into it this code.

        ```py  theme={null}
        from flask import Flask, request, make_response
        from plivo import plivoxml

        app = Flask(__name__)

        @app.route('/receive_call/', methods=['GET','POST'])
        def speak_xml():

        response = (plivoxml.ResponseElement()
                    .add(plivoxml.SpeakElement('Hello, you just received your first call')))
            return(response.to_string())

        if __name__ == "__main__":
            app.run(host='0.0.0.0', debug=True)
        ```

        ## Create a Plivo application to receive calls

        Associate the Flask server you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Receive_call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/receive_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_receivecall_app.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=fa56f60792c23523b7597ec4f1f07401" alt="Create Application" width="1440" height="788" data-path="images/create_receivecall_app.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Receive_call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_receivecall_app.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=489823f8c06deb4fa2f087c71ce50b70" alt="Assign Phone Number to Receive Call App" width="1440" height="792" data-path="images/assign_receivecall_app.png" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides. You should hear the text-to-speech message, “Hello, you just received your first call.”
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to receiving incoming calls on a Plivo number and greet callers with a text-to-speech message. Managing incoming calls is a key part of the call flow in many common use cases, such as interactive voice response (IVR), call forwarding, and conference calling.

    You can handle incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to receive an inbound call with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/receive-incoming.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=356ffd22965f7f9ccf8f969617603ee1" alt="" width="1446" height="774" data-path="images/receive-incoming.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintlify.s3.us-west-1.amazonaws.com/plivo/imagesreceive_call-phlo.gif" alt="Create a PHLO to receive incoming call" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Play Audio** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Play Audio** node.

        * In the Configuration pane at the right of the canvas, configure the **Play Audio** node to play a message to the caller.

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="Assign PHLO to a Plivo number" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now make a call to your Plivo phone number and see how the inbound call is handled.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that handles incoming calls on a Plivo number by playing a text-to-speech message to the caller.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/receive-incoming-calls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=fc3a488003b5b2eaa3ebe2302793cf9e" alt="Inbound Call Flow" width="1448" height="774" data-path="images/receive-incoming-calls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo’s text-to-speech engine plays a message using the [Speak](/voice/xml/speak/) XML element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Laravel controller for incoming calls

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
            // Speak XML to handle your first incoming call
            public function receiveCall()
            {
                $response = new Response();
                $speak_body = "Hello, you just received your first call";
                $response->addSpeak($speak_body);
                Header('Content-type: text/xml');
                echo $response->toXML();
            }
        }
        ```

        ## Create a Plivo application to receive calls

        Associate the controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Receive_call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/receive_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_receivecall_app.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=fa56f60792c23523b7597ec4f1f07401" alt="Create Application" width="1440" height="788" data-path="images/create_receivecall_app.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Receive_call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_receivecall_app.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=489823f8c06deb4fa2f087c71ce50b70" alt="Assign Phone Number to Receive Call App" width="1440" height="792" data-path="images/assign_receivecall_app.png" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides. You should hear the text-to-speech message, “Hello, you just received your first call.”
      </Tab>
    </Tabs>
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to receiving incoming calls on a Plivo number and greet callers with a text-to-speech message. Managing incoming calls is a key part of the call flow in many common use cases, such as interactive voice response (IVR), call forwarding, and conference calling.

    You can handle incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to receive an inbound call with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/receive-incoming.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=356ffd22965f7f9ccf8f969617603ee1" alt="" width="1446" height="774" data-path="images/receive-incoming.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintlify.s3.us-west-1.amazonaws.com/plivo/imagesreceive_call-phlo.gif" alt="Create a PHLO to receive incoming call" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Play Audio** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Play Audio** node.

        * In the Configuration pane at the right of the canvas, configure the **Play Audio** node to play a message to the caller.

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="Assign PHLO to a Plivo number" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now make a call to your Plivo phone number and see how the inbound call is handled.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that handles incoming calls on a Plivo number by playing a text-to-speech message to the caller.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/receive-incoming-calls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=fc3a488003b5b2eaa3ebe2302793cf9e" alt="Inbound Call Flow" width="1448" height="774" data-path="images/receive-incoming-calls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo’s text-to-speech engine plays a message using the [Speak](/voice/xml/speak/) XML element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create an MVC controller to handle incoming calls

        In Visual Studio, create a new project. Use the template for Web Application (Model-View-Controller).

        <Frame>
                    <img src="https://mintlify.s3.us-west-1.amazonaws.com/plivo/images/create_mvcapp.jpg" alt="Create an MVC app" />
        </Frame>

        Give the project a name — we used `Receivecall`.

        <Frame>
                    <img src="https://mintlify.s3.us-west-1.amazonaws.com/plivo/images/configure_mvcapp.jpg" alt="Configure the MVC app" />
        </Frame>

        Navigate to the Controllers directory in the Receivecall project. Create a controller named ReceivecallController.cs and paste into it this code.

        ```cs  theme={null}
        using System;
        using Plivo.XML;
        using System.Collections.Generic;
        using Microsoft.AspNetCore.Mvc;

        namespace Receivecall
        {
            public class ReceivecallController : Controller
            {
                public IActionResult Index()
                {
                    Plivo.XML.Response resp = new Plivo.XML.Response();
                    resp.AddSpeak("Hello, you just received your first call",
                        new Dictionary<string, string>() {
                {
                "loop",
                "3"
                }
                        });
                    var output = resp.ToString();
                    Console.WriteLine(output);

                    return this.Content(output, "text/xml");
                }
            }
        }
        ```

        ## Create a Plivo application to receive calls

        Associate the controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Receive_call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/receive_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_receivecall_app.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=fa56f60792c23523b7597ec4f1f07401" alt="Create Application" width="1440" height="788" data-path="images/create_receivecall_app.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Receive_call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_receivecall_app.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=489823f8c06deb4fa2f087c71ce50b70" alt="Assign Phone Number to Receive Call App" width="1440" height="792" data-path="images/assign_receivecall_app.png" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides. You should hear the text-to-speech message, “Hello, you just received your first call.”
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to receiving incoming calls on a Plivo number and greet callers with a text-to-speech message. Managing incoming calls is a key part of the call flow in many common use cases, such as interactive voice response (IVR), call forwarding, and conference calling.

    You can handle incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to receive an inbound call with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/receive-incoming.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=356ffd22965f7f9ccf8f969617603ee1" alt="" width="1446" height="774" data-path="images/receive-incoming.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintlify.s3.us-west-1.amazonaws.com/plivo/imagesreceive_call-phlo.gif" alt="Create a PHLO to receive incoming call" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Play Audio** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Play Audio** node.

        * In the Configuration pane at the right of the canvas, configure the **Play Audio** node to play a message to the caller.

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="Assign PHLO to a Plivo number" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now make a call to your Plivo phone number and see how the inbound call is handled.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that handles incoming calls on a Plivo number by playing a text-to-speech message to the caller.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/receive-incoming-calls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=fc3a488003b5b2eaa3ebe2302793cf9e" alt="Inbound Call Flow" width="1448" height="774" data-path="images/receive-incoming-calls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo’s text-to-speech engine plays a message using the [Speak](/voice/xml/speak/) XML element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Spark application to handle incoming calls

        Create a Java class called `ReceiveCall` and paste into it this code.

        ```java  theme={null}
        import static spark.Spark.*;
        import com.plivo.api.xml.Speak;
        import com.plivo.api.xml.Response;

        public class ReceiveCall {
            public static void main(String[] args) {
                post("/receive_call/", (request, response) -> {
                    response.type("application/xml");
                    return new Response()
                            .children(new Speak("Hello, you just received your first call")).toXmlString();
                });
            }
        }
        ```

        ## Create a Plivo application to receive calls

        Associate the Spark application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

        Give your application a name — we called ours `Receive_call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/receive_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_receivecall_app.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=fa56f60792c23523b7597ec4f1f07401" alt="Create Application" width="1440" height="788" data-path="images/create_receivecall_app.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Receive_call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_receivecall_app.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=489823f8c06deb4fa2f087c71ce50b70" alt="Assign Phone Number to Receive Call App" width="1440" height="792" data-path="images/assign_receivecall_app.png" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides. You should hear the text-to-speech message, “Hello, you just received your first call.”÷÷
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to receiving incoming calls on a Plivo number and greet callers with a text-to-speech message. Managing incoming calls is a key part of the call flow in many common use cases, such as interactive voice response (IVR), call forwarding, and conference calling.

    You can handle incoming calls either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to receive an inbound call with a few clicks on the PHLO canvas, without writing a single line of code.

        ## How it works

        When you receive a call on a voice-enabled Plivo number, you can control the call flow by associating a PHLO application to that Plivo number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call.

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/receive-incoming.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=356ffd22965f7f9ccf8f969617603ee1" alt="" width="1446" height="774" data-path="images/receive-incoming.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. To receive incoming calls, you must have a voice-enabled Plivo phone number. You can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        <Frame>
                    <img src="https://mintlify.s3.us-west-1.amazonaws.com/plivo/imagesreceive_call-phlo.gif" alt="Create a PHLO to receive incoming call" />
        </Frame>

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * From the list of components on the left side, drag and drop the **Play Audio** component onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **Incoming Call** trigger state to the **Play Audio** node.

        * In the Configuration pane at the right of the canvas, configure the **Play Audio** node to play a message to the caller.

        * Once you’ve configured the node, click **Validate** to save the configuration.

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        ## Assign the PHLO to a Plivo number

        Once you’ve created and configured your PHLO, assign it to a Plivo number.

        * On the [Numbers](https://cx.plivo.com/phone-numbers) page of the console, under **Your Numbers**, click the phone number you want to use for the PHLO.
        * In the **Number Configuration** box, select **PHLO** from the **Application Type** drop-down.
        * From the **PHLO Name** drop-down, select the PHLO you want to use with the number, then click **Update Number**.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=2a03349e5087a0e5f873a3119658300f" alt="Assign PHLO to a Plivo number" width="1440" height="785" data-path="images/assign-phlo.png" />
        </Frame>

        ## Test

        You can now make a call to your Plivo phone number and see how the inbound call is handled.

        For more information about creating a PHLO application, see the [PHLO Getting Started guide](/phlo/). For information on components and their variables, see the [PHLO Components Library](/phlo/components-library/overview/).
      </Tab>

      <Tab title="Using XML">
        Here’s how to use a Plivo XML document that handles incoming calls on a Plivo number by playing a text-to-speech message to the caller.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/receive-incoming-calls.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=fc3a488003b5b2eaa3ebe2302793cf9e" alt="Inbound Call Flow" width="1448" height="774" data-path="images/receive-incoming-calls.png" />
        </Frame>

        Plivo requests an answer URL when it answers the call (step 2) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call. In this example, when an incoming call is received, Plivo’s text-to-speech engine plays a message using the [Speak](/voice/xml/speak/) XML element.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a Go application to handle incoming calls

        Create a file called `receive_call.go` and paste into it this code.

        ```go  theme={null}
        package main

        import (
        	"fmt"
        	"net/http"
        	"github.com/plivo/plivo-go/v7"
        )

        func handler(w http.ResponseWriter, r *http.Request) {

        	response := xml.ResponseElement{
        		Contents: []interface{} {
        			new(xml.SpeakElement).
        			AddSpeak("Hello, you just received your first call"),
        		},
        	}
        	fmt.Printf(response.String())
        }

        func main() {
        	http.HandleFunc("/receive_call/", handler)
        	http.ListenAndServe(":8080", nil)
        }

        ```

        ## Create a Plivo application to receive calls

        Associate the Go application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application#create-an-application).

        Give your application a name — we called ours `Receive_call`. Enter the server URL you want to use (for example `https://<yourdomain>.com/receive_call/`) in the `Answer URL` field and set the method to `POST`.  Click **Create Application** to save your application.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_receivecall_app.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=fa56f60792c23523b7597ec4f1f07401" alt="Create Application" width="1440" height="788" data-path="images/create_receivecall_app.png" />
        </Frame>

        ## Assign a Plivo number to your application

        Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

        From the Application Type drop-down, select `XML Application`.

        From the Plivo Application drop-down, select `Receive_call` (the name we gave the application).

        Click **Update Number** to save.

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_receivecall_app.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=489823f8c06deb4fa2f087c71ce50b70" alt="Assign Phone Number to Receive Call App" width="1440" height="792" data-path="images/assign_receivecall_app.png" />
        </Frame>

        ## Test

        Make a call to your Plivo number using any phone. Plivo will send a request to the answer URL you provided requesting an XML response and then process the call according to the instructions in the XML document the server provides. You should hear the text-to-speech message, “Hello, you just received your first call.”
      </Tab>
    </Tabs>
  </Tab>
</Tabs>
