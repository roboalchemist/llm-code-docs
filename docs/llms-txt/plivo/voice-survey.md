# Source: https://plivo.com/docs/voice/use-cases/voice-survey.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Voice Surveys

> Automate voice surveys to collect feedback and poll responses via phone

<Tabs>
  <Tab title="Node">
    ## Overview

    Plivo lets you automate voice surveys for use cases such as collecting feedback from customers and conducting polling on political issues. You can set up multiple levels of questions and walk users through different paths depending on the keys they press in response to your questions, and save the responses for analysis.

    You can implement voice surveys either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to automate voice surveys with a few clicks on the PHLO canvas, and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Node.js, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * Click the **Start** node to open the Configuration tab to the right of the canvas, then enter the information to retrieve from the HTTP Request payload. For this example, enter From and To phone numbers and your business name.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/start_config.mp4?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=9262dc36cff409df19fb62ed6deebab7" data-path="images/start_config.mp4" />
          </Frame>

        * Validate the configuration by clicking **Validate**. Every time you finish configuring a node, click **Validate** to check the syntax and save your changes.

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. This adds an **Initiate Call** node onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call_customer.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=03b96867037cb2e2e3920f55c3a05bfc" data-path="images/call_customer.mp4" />
          </Frame>

        * In the Configuration tab of the **Initiate Call** node, rename the node to **Call\_Customer**. You can rename nodes as you like to improve your PHLO's readability. To enter values for the From and To fields, start typing two curly brackets. PHLO will display a list of all available variables; choose the appropriate ones. When you use variables in a PHLO, the values are retrieved from the HTTP Request payload you defined in the Start node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call_customer_config.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=2078b426506e6c7787053203de00d06c" data-path="images/call_customer_config.mp4" />
          </Frame>

        * Next, drag and drop the **IVR Menu** component onto the canvas. Draw a line to connect the **Initiate Call** node‘s **Answered** trigger state to the IVR Menu node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_1.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=0e5e5dec3ac0e1c8c007c04045daee30" data-path="images/question_1.mp4" />
          </Frame>

        * Click the **IVR Menu** node to open its Configuration tab. Rename the **IVR Menu** node **Question\_1**. For this example, select **1** and **2** as allowed choices. In the Speak Text box, enter a message to play to the user that introduces the survey and states the choices they can respond with. If you like, you can also configure the Language and Voice fields for the message.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_1_config.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=65c71c8e745edb6b2faa1a05c469068c" data-path="images/question_1_config.mp4" />
          </Frame>

        * Repeat the process with another **IVR Menu** node. Rename it **Question\_2**.

        * To daisy-chain to the second question after the user gives a valid response to question 1, connect the **Question\_1** node‘s **1** and **2** trigger states to the **Question\_2** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_2.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=c463df1f9c685a9fd35974ea183c1b5f" data-path="images/question_2.mp4" />
          </Frame>

        * Configure the choices for **Question\_2** on its **Configuration** tab. Again, select **1** and **2** as allowed choices and enter a message to play to the user.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/question_2_config.mp4?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=3062979820e40e30eb382925f563be2b" data-path="images/question_2_config.mp4" />
          </Frame>

        * Drag and drop the **Play Audio** component onto the canvas. Draw a line to connect the **Question\_2** node‘s **1** and **2** trigger states to the **Play Audio** node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/acknowledge_participation.mp4?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=bd159c8c416868549fa8be707a613fa6" data-path="images/acknowledge_participation.mp4" />
          </Frame>

        * In its Configuration tab, rename the node to **Acknowledge\_Participation**. Enter a message of thanks to play to the user in the node‘s Speak Text box.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/acknowledge_participation_config.mp4?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=220bf7ac1b7faa27844c69a0e075c403" data-path="images/acknowledge_participation_config.mp4" />
          </Frame>

        * Drag and drop the **HTTP Request** component onto the canvas. Draw a line to connect the **Acknowledge\_Participation** node‘s **Prompt Completed** trigger state to the HTTP Request node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/handle_callback_voice_survey.mp4?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=918061ee1f2a6b9e8d3d89ca04776c14" data-path="images/handle_callback_voice_survey.mp4" />
          </Frame>

        * Rename the **HTTP Request** node **Handle\_Callback**. Configure the node to post the survey results to a website. On its Configuration tab, enter key names `answer1` and `answer2`. For their values, begin typing two curly brackets to view all available variables, then select **Question\_1.digits** and **Question\_2.digits**.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/handle_callback_config.mp4?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=45ab508b76b09714acead46d6e65f176" data-path="images/handle_callback_config.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        ### With static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="" width="1398" height="765" data-path="images/static_payload.png" />
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

        ### With dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code to the PHLO when you trigger it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        ### Code

        Create a file called `TriggerPhlo.php` and paste into it this code.

        ```php  theme={null}
        <?php
        require 'vendor/autoload.php';
        use Plivo\Resources\PHLO\PhloRestClient;
        use Plivo\Exceptions\PlivoRestException;
        $client = new PhloRestClient("<auth_id>", "<auth_token>");

        $phlo = $client->phlo->get("<phlo_id>");
        try {
            $response = $phlo->run(["from" => "<caller_id>", "to" => "<destination_number>"]);
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

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to implement voice surveys.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a voice survey application in PHP

        Change to the project directory and run this command to create a Laravel controller.

        ```shell  theme={null}
        $ php artisan make:controller SurveyController
        ```

        This generates a controller named SurveyController in the app/http/controllers/ directory. Edit app/http/controllers/SurveyController.php and add this code.

        ```php  theme={null}
        <?php

        namespace App\Http\Controllers;
        require '../../vendor/autoload.php';
        use Plivo\RestClient;
        use Plivo\XML\Response;
        use Illuminate\Http\Request;

        class SurveyController extends Controller
        {
            // GetInput XML to handle the incoming call
            public function ivrMain()
            {
                // Message that Plivo reads when the call recipient answers
                $Question1 = "Hi, this is a call from Plivo. How would you rate your overall satisfaction with our services? Press 1 if you're satisfied or 2 to suggest improvements";
                // Message that Plivo reads when the recipient provides negative feedback
                $NegativeFeedback = "We're sorry about your bad experience, One of our representatives will get in touch with you";
                // Message that Plivo reads when the caller does nothing
                $NoinputMessage = "Sorry, I didn't catch that. Please hang up and try again";
                // Message that Plivo reads when the caller enters an invalid number
                $WronginputMessage = "Sorry, that's not a valid entry";

                $r = new Response();

                $getinput_action_url = "https://<yourdomain>.com/firstbranch.php";
                $get_input = $r->addGetInput([
                            'action' => $getinput_action_url,
                            'method' => "POST",
                            'digitEndTimeout' => "5",
                            'inputType' => "dtmf",
                            'redirect' => "true",
                        ]);
                $get_input->addSpeak($Question1);
                $r->addSpeak($NoinputMessage);
                Header('Content-type: text/xml');
                echo $r->toXML();
            }

            // Action URL block for DTMF
            public function firstBranch(Request $request)
            {
                $Question2 = "How would you rate your satisfaction with our customer service? Press 1 if you're satisfied or 2 to suggest improvements";
                // Message that Plivo reads when the recipient provides negative feedback
                $NegativeFeedback = "We're sorry about your bad experience, One of our representatives will get in touch with you";
                // Message that Plivo reads when the caller does nothing
                $NoinputMessage = "Sorry, I didn't catch that. Please hang up and try again";
                // Message that Plivo reads when the caller enters an invalid number
                $WronginputMessage = "Sorry, that's not a valid entry";

                $r = new Response();

                $digit = $_REQUEST['Digits'];
                if ($digit == '1'){
                    $getinput_action_url = "https://<yourdomain>.com/secondbranch.php";
                    $get_input = $r->addGetInput([
                            'action' => $getinput_action_url,
                            'method' => "POST",
                            'digitEndTimeout' => "5",
                            'inputType' => "dtmf",
                            'redirect' => "true",
                        ]);
                    $get_input->addSpeak($Question2);
                    $r->addSpeak($NoinputMessage);
                }
                else if ($digit == '2'){
                    $r->addSpeak($NegativeFeedback);
                }
                else {
                    $r->addSpeak($WronginputMessage);
                }
                Header('Content-type: text/xml');
                echo $r->toXML();
            }

            // Action URL block for Sales and Support branch
            public function secondBranch(Request $request)
            {
                // Message that Plivo reads when the recipient provides negative feedback
                $NegativeFeedback = "We're sorry about your bad experience, One of our representatives will get in touch with you";
                // Message that Plivo reads when the caller enters a wrong number
                $WronginputMessage = "Sorry, that's not a valid entry";

                $r = new Response();
                $digit = $_REQUEST['Digits'];
                if ($digit == '1'){
                    $body = "Thank you for participating in the survey";
                    $params = array(
                        'language' => "en-GB"
                    );
                    $r->addSpeak($body,$params);
                }
                else if ($digit == '2'){
                    $r->addSpeak($NegativeFeedback);
                }
                else {
                    $r->addSpeak($WronginputMessage);
                }
                Header('Content-type: text/xml');
                echo $r->toXML();
            }
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        <div class="notice-box">
          <strong>Note:</strong>
          We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables, to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch them from the environment variables. You can use `$_ENV` or `putenv/getenv` functions to store environment variables and fetch them when initializing the client.
        </div>

        ### Add a route

        Add a route for the forward function in the SurveyController class. Edit routes/web.php and add these lines.

        ```shell  theme={null}
        Route::match(['get', 'post'], '/survey', 'SurveyController@ivrMain');
        Route::match(['get', 'post'], '/firstbranch', 'SurveyController@firstBranch');
        Route::match(['get', 'post'], '/secondbranch', 'SurveyController@secondBranch');
        ```

        Start the Laravel server.

        ```shell  theme={null}
        $ php artisan serve
        ```

        You should see your basic server application in acation at [http://localhost:8000/survey](http://localhost:8000/survey).

        [Set up ngrok](/sdk/server/set-up-php-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

        ## Test

        Make a call to a Plivo phone number and see how the survey application works.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Ruby">
    ## Overview

    Plivo lets you automate voice surveys for use cases such as collecting feedback from customers and conducting polling on political issues. You can set up multiple levels of questions and walk users through different paths depending on the keys they press in response to your questions, and save the responses for analysis.

    You can implement voice surveys either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to automate voice surveys with a few clicks on the PHLO canvas, and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Node.js, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * Click the **Start** node to open the Configuration tab to the right of the canvas, then enter the information to retrieve from the HTTP Request payload. For this example, enter From and To phone numbers and your business name.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/start_config.mp4?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=9262dc36cff409df19fb62ed6deebab7" data-path="images/start_config.mp4" />
          </Frame>

        * Validate the configuration by clicking **Validate**. Every time you finish configuring a node, click **Validate** to check the syntax and save your changes.

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. This adds an **Initiate Call** node onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call_customer.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=03b96867037cb2e2e3920f55c3a05bfc" data-path="images/call_customer.mp4" />
          </Frame>

        * In the Configuration tab of the **Initiate Call** node, rename the node to **Call\_Customer**. You can rename nodes as you like to improve your PHLO's readability. To enter values for the From and To fields, start typing two curly brackets. PHLO will display a list of all available variables; choose the appropriate ones. When you use variables in a PHLO, the values are retrieved from the HTTP Request payload you defined in the Start node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call_customer_config.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=2078b426506e6c7787053203de00d06c" data-path="images/call_customer_config.mp4" />
          </Frame>

        * Next, drag and drop the **IVR Menu** component onto the canvas. Draw a line to connect the **Initiate Call** node‘s **Answered** trigger state to the IVR Menu node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_1.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=0e5e5dec3ac0e1c8c007c04045daee30" data-path="images/question_1.mp4" />
          </Frame>

        * Click the **IVR Menu** node to open its Configuration tab. Rename the **IVR Menu** node **Question\_1**. For this example, select **1** and **2** as allowed choices. In the Speak Text box, enter a message to play to the user that introduces the survey and states the choices they can respond with. If you like, you can also configure the Language and Voice fields for the message.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_1_config.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=65c71c8e745edb6b2faa1a05c469068c" data-path="images/question_1_config.mp4" />
          </Frame>

        * Repeat the process with another **IVR Menu** node. Rename it **Question\_2**.

        * To daisy-chain to the second question after the user gives a valid response to question 1, connect the **Question\_1** node‘s **1** and **2** trigger states to the **Question\_2** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_2.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=c463df1f9c685a9fd35974ea183c1b5f" data-path="images/question_2.mp4" />
          </Frame>

        * Configure the choices for **Question\_2** on its **Configuration** tab. Again, select **1** and **2** as allowed choices and enter a message to play to the user.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/question_2_config.mp4?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=3062979820e40e30eb382925f563be2b" data-path="images/question_2_config.mp4" />
          </Frame>

        * Drag and drop the **Play Audio** component onto the canvas. Draw a line to connect the **Question\_2** node‘s **1** and **2** trigger states to the **Play Audio** node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/acknowledge_participation.mp4?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=bd159c8c416868549fa8be707a613fa6" data-path="images/acknowledge_participation.mp4" />
          </Frame>

        * In its Configuration tab, rename the node to **Acknowledge\_Participation**. Enter a message of thanks to play to the user in the node‘s Speak Text box.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/acknowledge_participation_config.mp4?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=220bf7ac1b7faa27844c69a0e075c403" data-path="images/acknowledge_participation_config.mp4" />
          </Frame>

        * Drag and drop the **HTTP Request** component onto the canvas. Draw a line to connect the **Acknowledge\_Participation** node‘s **Prompt Completed** trigger state to the HTTP Request node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/handle_callback_voice_survey.mp4?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=918061ee1f2a6b9e8d3d89ca04776c14" data-path="images/handle_callback_voice_survey.mp4" />
          </Frame>

        * Rename the **HTTP Request** node **Handle\_Callback**. Configure the node to post the survey results to a website. On its Configuration tab, enter key names `answer1` and `answer2`. For their values, begin typing two curly brackets to view all available variables, then select **Question\_1.digits** and **Question\_2.digits**.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/handle_callback_config.mp4?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=45ab508b76b09714acead46d6e65f176" data-path="images/handle_callback_config.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        ### With static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

        Create a file called `trigger_phlo.rb` and paste into it this code.

        ```ruby  theme={null}
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

        ### With dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code to the PHLO when you trigger it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        #### Code

        Create a file called `trigger_phlo.rb` and paste into it this code.

        ```ruby  theme={null}
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
             from: '<caller_id>',
             to: '<destination_number>'
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

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to implement voice surveys.

        ## Create a voice survey application in Ruby

        Change to the project directory and run this command to create a Rails controller.

        ```shell  theme={null}
        $ rails generate controller Plivo voice
        ```

        This generates a controller named plivo\_controller in the app/controllers/ directory and a respective view  in app/views/plivo. We can delete the view as we will not need it.

        ```shell  theme={null}
        $ rm app/views/plivo/voice.html.erb
        ```

        Edit app/controllers/plivo\_controller.rb and add this code in the PlivoController class.

        ```ruby  theme={null}
        include Plivo
        include Plivo::XML
        include Plivo::Exceptions

        class PlivoController < ApplicationController
          # Message that Plivo reads when the call recipient answers
          $question1 = "Hi, this is a call from Plivo. How would you rate your overall satisfaction with our services? Press 1 if you're satisfied or 2 to suggest improvements"
          $question2 = "How would you rate your satisfaction with our customer service? Press 1 if you're satisfied or 2 to suggest improvements"
          # Message that Plivo reads when the recipient provides negative feedback
          $negative_feedback = "We're sorry about your bad experience. One of our representatives will get in touch with you"
          # Message that Plivo reads when the caller does nothing
          $noinput_message = "Sorry, I didn't catch that. Please hang up and try again"
          # This is the message that Plivo reads when the caller inputs a wrong number.
          $wronginput_message = "Sorry, that's not a valid entry"
          def survey
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
            getinput.addSpeak($question1)
            r.addSpeak($noinput_message)

            xml = PlivoXML.new(r)
            render xml: xml.to_xml
          end
          def firstbranch
            digit = params[:Digits]
            r = Response.new()

            if (digit == "1")
                getinput_action_url = "https://<yourdomain>.com/ivr/secondbranch/"
                params = {
                    action: getinput_action_url,
                    method: 'POST',
                    digitEndTimeout: '5',
                    inputType:'dtmf',
                    redirect:'true'
                }
                getinput = r.addGetInput(params)
                getinput.addSpeak($question2)
                r.addSpeak($noinput_message)

            elsif (digit == "2")
                r.addSpeak($negative_feedback)
            else
                r.addSpeak($wronginput_message)
            end

            xml = PlivoXML.new(r)
            render xml: xml.to_xml
          end
          def secondbranch
            digit = params[:Digits]

            r = Response.new()

            if (digit == "1")
                body = "Thank you for participating in the survey"
                params = {
                    'language'=> "en-GB"
                }

                r.addSpeak(body,params)
            elsif (digit == "2")
                r.addSpeak($negative_feedback)
            else
                r.addSpeak($wronginput_message)
            end

            xml = PlivoXML.new(r)
            render xml: xml.to_xml
          end
        end
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        <Note>
          <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables, to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `ENV` to store environment variables and fetch them when initializing the client.
        </Note>

        ### Add a route

        Add a route for the inbound function in the PlivoController class. Edit config/routes.rb and add these lines after the inbound route.

        ```shell  theme={null}
        get 'plivo/survey'
        get 'plivo/firstbranch'
        get 'plivo/secondbranch'
        ```

        Start the Rails server.

        ```shell  theme={null}
        $ rails server
        ```

        You should see your basic server application in action at  [http://localhost:3000/plivo/survey/](http://localhost:3000/plivo/survey/).

        [Set up ngrok](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

        ## Test

        Make a call to a Plivo phone number and see how the survey application works.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Python">
    ## Overview

    Plivo lets you automate voice surveys for use cases such as collecting feedback from customers and conducting polling on political issues. You can set up multiple levels of questions and walk users through different paths depending on the keys they press in response to your questions, and save the responses for analysis.

    You can implement voice surveys either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to automate voice surveys with a few clicks on the PHLO canvas, and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Node.js, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * Click the **Start** node to open the Configuration tab to the right of the canvas, then enter the information to retrieve from the HTTP Request payload. For this example, enter From and To phone numbers and your business name.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/start_config.mp4?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=9262dc36cff409df19fb62ed6deebab7" data-path="images/start_config.mp4" />
          </Frame>

        * Validate the configuration by clicking **Validate**. Every time you finish configuring a node, click **Validate** to check the syntax and save your changes.

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. This adds an **Initiate Call** node onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call_customer.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=03b96867037cb2e2e3920f55c3a05bfc" data-path="images/call_customer.mp4" />
          </Frame>

        * In the Configuration tab of the **Initiate Call** node, rename the node to **Call\_Customer**. You can rename nodes as you like to improve your PHLO's readability. To enter values for the From and To fields, start typing two curly brackets. PHLO will display a list of all available variables; choose the appropriate ones. When you use variables in a PHLO, the values are retrieved from the HTTP Request payload you defined in the Start node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call_customer_config.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=2078b426506e6c7787053203de00d06c" data-path="images/call_customer_config.mp4" />
          </Frame>

        * Next, drag and drop the **IVR Menu** component onto the canvas. Draw a line to connect the **Initiate Call** node‘s **Answered** trigger state to the IVR Menu node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_1.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=0e5e5dec3ac0e1c8c007c04045daee30" data-path="images/question_1.mp4" />
          </Frame>

        * Click the **IVR Menu** node to open its Configuration tab. Rename the **IVR Menu** node **Question\_1**. For this example, select **1** and **2** as allowed choices. In the Speak Text box, enter a message to play to the user that introduces the survey and states the choices they can respond with. If you like, you can also configure the Language and Voice fields for the message.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_1_config.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=65c71c8e745edb6b2faa1a05c469068c" data-path="images/question_1_config.mp4" />
          </Frame>

        * Repeat the process with another **IVR Menu** node. Rename it **Question\_2**.

        * To daisy-chain to the second question after the user gives a valid response to question 1, connect the **Question\_1** node‘s **1** and **2** trigger states to the **Question\_2** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_2.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=c463df1f9c685a9fd35974ea183c1b5f" data-path="images/question_2.mp4" />
          </Frame>

        * Configure the choices for **Question\_2** on its **Configuration** tab. Again, select **1** and **2** as allowed choices and enter a message to play to the user.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/question_2_config.mp4?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=3062979820e40e30eb382925f563be2b" data-path="images/question_2_config.mp4" />
          </Frame>

        * Drag and drop the **Play Audio** component onto the canvas. Draw a line to connect the **Question\_2** node‘s **1** and **2** trigger states to the **Play Audio** node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/acknowledge_participation.mp4?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=bd159c8c416868549fa8be707a613fa6" data-path="images/acknowledge_participation.mp4" />
          </Frame>

        * In its Configuration tab, rename the node to **Acknowledge\_Participation**. Enter a message of thanks to play to the user in the node‘s Speak Text box.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/acknowledge_participation_config.mp4?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=220bf7ac1b7faa27844c69a0e075c403" data-path="images/acknowledge_participation_config.mp4" />
          </Frame>

        * Drag and drop the **HTTP Request** component onto the canvas. Draw a line to connect the **Acknowledge\_Participation** node‘s **Prompt Completed** trigger state to the HTTP Request node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/handle_callback_voice_survey.mp4?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=918061ee1f2a6b9e8d3d89ca04776c14" data-path="images/handle_callback_voice_survey.mp4" />
          </Frame>

        * Rename the **HTTP Request** node **Handle\_Callback**. Configure the node to post the survey results to a website. On its Configuration tab, enter key names `answer1` and `answer2`. For their values, begin typing two curly brackets to view all available variables, then select **Question\_1.digits** and **Question\_2.digits**.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/handle_callback_config.mp4?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=45ab508b76b09714acead46d6e65f176" data-path="images/handle_callback_config.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        ### With static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="" width="1398" height="765" data-path="images/static_payload.png" />
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

        ### With dynamic payload

        To use dynamic values for the parameters, you can use the liquid templating params while creating the PHLO and pass the values while triggering the PHLO.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        #### Code

        Create a file called `trigger_phlo.py` and paste into it this code.

        ```py  theme={null}
        import plivo

        auth_id = '<auth_id>'
        auth_token = '<auth_token>'
        phlo_id = '<phlo_id>'
        payload = {"from" : "<caller_id>","to" : "<destination_number>"}
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

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to implement voice surveys.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a voice survey application in PHP

        Create a file called `survey.py` and paste into it this code.

        ```py  theme={null}
        # -*- coding: utf-8 -*-
        from flask import Flask, Response, request, url_for
        from plivo import plivoxml

        # Message that Plivo reads when the call recipient answers
        question1 = "Hi, this is a call from Plivo. How would you rate your overall satisfaction with our services? Press 1 if you're satisfied or 2 to suggest improvements"
        question2 = "How would you rate your satisfaction with our customer service? Press 1 if you're satisfied or 2 to suggest improvements"
        # Message that Plivo reads when the recipient provides negative feedback
        negative_feedback = "We're sorry about your bad experience, One of our representatives will get in touch with you"
        # Message that Plivo reads when the caller does nothing
        noinput_message = "Sorry, I didn't catch that. Please hang up and try again"
        # Message that Plivo reads when the caller enters an invalid number
        wronginput_message = "Sorry, that's not a valid entry"

        app = Flask(__name__)

        @app.route('/survey/', methods=['GET','POST'])
        def ivr():
            response = plivoxml.ResponseElement()
            getinput_action_url = "https://<yourdomain>.com/firstbranch/"
            response.add(plivoxml.GetInputElement().
                set_action(getinput_action_url).
                set_method('POST').
                set_input_type('dtmf').
                set_digit_end_timeout(5).
                set_redirect(True).add(
                    plivoxml.SpeakElement(question1)))
            response.add(plivoxml.SpeakElement(noinput_message))
            return Response(response.to_string(), mimetype='application/xml')

        @app.route('/survey/firstbranch/', methods=['GET','POST'])
        def firstbranch():
            response = plivoxml.ResponseElement()
            digit = request.values.get('Digits')
            if digit == "1":
                # Read out a text.
                getinput_action_url = "https://<yourdomain>.com/secondbranch/"
                response.add(plivoxml.GetInputElement().
                    set_action(getinput_action_url).
                    set_method('POST').
                    set_input_type('dtmf').
                    set_digit_end_timeout(5).
                    set_redirect(True).add(
                        plivoxml.SpeakElement(question2)))
                response.add(plivoxml.SpeakElement(noinput_message))

            elif digit == "2":
                response.add_speak(negative_feedback)

            else:
                response.add_speak(wronginput_message)
            return Response(response.to_string(), mimetype='application/xml')

        @app.route('/ivr/secondbranch/', methods=['GET','POST'])
        def secondbranch():
            response = plivoxml.ResponseElement()
            digit = request.values.get('Digits')

            if digit == "1":
                text = u"Thank you for participating in the survey"
                params = {
                    'language': "en-GB",
                }
                response.add_speak(text,**params)

            elif digit == "2":
                response.add_speak(negative_feedback)

            else:
                response.add_speak(wronginput_message)
            return Response(response.to_string(), mimetype='application/xml')

        if __name__ == '__main__':
            app.run(host='0.0.0.0', debug=True)
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        <Note>
          <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables, to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `os module(os.environ)` to store environment variables and fetch them when initializing the client.
        </Note>

        Save the file and run it.

        ```shell  theme={null}
        python survey.py
        ```

        You should see your basic server application in action at [http://localhost:5000/survey/](http://localhost:5000/survey/).

        [Set up ngrok](/sdk/server/set-up-python-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

        ## Test

        Make a call to a Plivo phone number and see how the survey application works.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="PHP">
    ## Overview

    Plivo lets you automate voice surveys for use cases such as collecting feedback from customers and conducting polling on political issues. You can set up multiple levels of questions and walk users through different paths depending on the keys they press in response to your questions, and save the responses for analysis.

    You can implement voice surveys either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to automate voice surveys with a few clicks on the PHLO canvas, and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Node.js, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * Click the **Start** node to open the Configuration tab to the right of the canvas, then enter the information to retrieve from the HTTP Request payload. For this example, enter From and To phone numbers and your business name.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/start_config.mp4?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=9262dc36cff409df19fb62ed6deebab7" data-path="images/start_config.mp4" />
          </Frame>

        * Validate the configuration by clicking **Validate**. Every time you finish configuring a node, click **Validate** to check the syntax and save your changes.

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. This adds an **Initiate Call** node onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call_customer.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=03b96867037cb2e2e3920f55c3a05bfc" data-path="images/call_customer.mp4" />
          </Frame>

        * In the Configuration tab of the **Initiate Call** node, rename the node to **Call\_Customer**. You can rename nodes as you like to improve your PHLO's readability. To enter values for the From and To fields, start typing two curly brackets. PHLO will display a list of all available variables; choose the appropriate ones. When you use variables in a PHLO, the values are retrieved from the HTTP Request payload you defined in the Start node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call_customer_config.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=2078b426506e6c7787053203de00d06c" data-path="images/call_customer_config.mp4" />
          </Frame>

        * Next, drag and drop the **IVR Menu** component onto the canvas. Draw a line to connect the **Initiate Call** node‘s **Answered** trigger state to the IVR Menu node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_1.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=0e5e5dec3ac0e1c8c007c04045daee30" data-path="images/question_1.mp4" />
          </Frame>

        * Click the **IVR Menu** node to open its Configuration tab. Rename the **IVR Menu** node **Question\_1**. For this example, select **1** and **2** as allowed choices. In the Speak Text box, enter a message to play to the user that introduces the survey and states the choices they can respond with. If you like, you can also configure the Language and Voice fields for the message.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_1_config.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=65c71c8e745edb6b2faa1a05c469068c" data-path="images/question_1_config.mp4" />
          </Frame>

        * Repeat the process with another **IVR Menu** node. Rename it **Question\_2**.

        * To daisy-chain to the second question after the user gives a valid response to question 1, connect the **Question\_1** node‘s **1** and **2** trigger states to the **Question\_2** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_2.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=c463df1f9c685a9fd35974ea183c1b5f" data-path="images/question_2.mp4" />
          </Frame>

        * Configure the choices for **Question\_2** on its **Configuration** tab. Again, select **1** and **2** as allowed choices and enter a message to play to the user.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/question_2_config.mp4?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=3062979820e40e30eb382925f563be2b" data-path="images/question_2_config.mp4" />
          </Frame>

        * Drag and drop the **Play Audio** component onto the canvas. Draw a line to connect the **Question\_2** node‘s **1** and **2** trigger states to the **Play Audio** node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/acknowledge_participation.mp4?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=bd159c8c416868549fa8be707a613fa6" data-path="images/acknowledge_participation.mp4" />
          </Frame>

        * In its Configuration tab, rename the node to **Acknowledge\_Participation**. Enter a message of thanks to play to the user in the node‘s Speak Text box.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/acknowledge_participation_config.mp4?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=220bf7ac1b7faa27844c69a0e075c403" data-path="images/acknowledge_participation_config.mp4" />
          </Frame>

        * Drag and drop the **HTTP Request** component onto the canvas. Draw a line to connect the **Acknowledge\_Participation** node‘s **Prompt Completed** trigger state to the HTTP Request node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/handle_callback_voice_survey.mp4?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=918061ee1f2a6b9e8d3d89ca04776c14" data-path="images/handle_callback_voice_survey.mp4" />
          </Frame>

        * Rename the **HTTP Request** node **Handle\_Callback**. Configure the node to post the survey results to a website. On its Configuration tab, enter key names `answer1` and `answer2`. For their values, begin typing two curly brackets to view all available variables, then select **Question\_1.digits** and **Question\_2.digits**.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/handle_callback_config.mp4?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=45ab508b76b09714acead46d6e65f176" data-path="images/handle_callback_config.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        ### With static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="" width="1398" height="765" data-path="images/static_payload.png" />
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

        ### With dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code to the PHLO when you trigger it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        ### Code

        Create a file called `TriggerPhlo.php` and paste into it this code.

        ```php  theme={null}
        <?php
        require 'vendor/autoload.php';
        use Plivo\Resources\PHLO\PhloRestClient;
        use Plivo\Exceptions\PlivoRestException;
        $client = new PhloRestClient("<auth_id>", "<auth_token>");

        $phlo = $client->phlo->get("<phlo_id>");
        try {
            $response = $phlo->run(["from" => "<caller_id>", "to" => "<destination_number>"]);
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

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to implement voice surveys.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a voice survey application in PHP

        Change to the project directory and run this command to create a Laravel controller.

        ```shell  theme={null}
        $ php artisan make:controller SurveyController
        ```

        This generates a controller named SurveyController in the app/http/controllers/ directory. Edit app/http/controllers/SurveyController.php and add this code.

        ```php  theme={null}
        <?php

        namespace App\Http\Controllers;
        require '../../vendor/autoload.php';
        use Plivo\RestClient;
        use Plivo\XML\Response;
        use Illuminate\Http\Request;

        class SurveyController extends Controller
        {
            // GetInput XML to handle the incoming call
            public function ivrMain()
            {
                // Message that Plivo reads when the call recipient answers
                $Question1 = "Hi, this is a call from Plivo. How would you rate your overall satisfaction with our services? Press 1 if you're satisfied or 2 to suggest improvements";
                // Message that Plivo reads when the recipient provides negative feedback
                $NegativeFeedback = "We're sorry about your bad experience, One of our representatives will get in touch with you";
                // Message that Plivo reads when the caller does nothing
                $NoinputMessage = "Sorry, I didn't catch that. Please hang up and try again";
                // Message that Plivo reads when the caller enters an invalid number
                $WronginputMessage = "Sorry, that's not a valid entry";

                $r = new Response();

                $getinput_action_url = "https://<yourdomain>.com/firstbranch.php";
                $get_input = $r->addGetInput([
                            'action' => $getinput_action_url,
                            'method' => "POST",
                            'digitEndTimeout' => "5",
                            'inputType' => "dtmf",
                            'redirect' => "true",
                        ]);
                $get_input->addSpeak($Question1);
                $r->addSpeak($NoinputMessage);
                Header('Content-type: text/xml');
                echo $r->toXML();
            }

            // Action URL block for DTMF
            public function firstBranch(Request $request)
            {
                $Question2 = "How would you rate your satisfaction with our customer service? Press 1 if you're satisfied or 2 to suggest improvements";
                // Message that Plivo reads when the recipient provides negative feedback
                $NegativeFeedback = "We're sorry about your bad experience, One of our representatives will get in touch with you";
                // Message that Plivo reads when the caller does nothing
                $NoinputMessage = "Sorry, I didn't catch that. Please hang up and try again";
                // Message that Plivo reads when the caller enters an invalid number
                $WronginputMessage = "Sorry, that's not a valid entry";

                $r = new Response();

                $digit = $_REQUEST['Digits'];
                if ($digit == '1'){
                    $getinput_action_url = "https://<yourdomain>.com/secondbranch.php";
                    $get_input = $r->addGetInput([
                            'action' => $getinput_action_url,
                            'method' => "POST",
                            'digitEndTimeout' => "5",
                            'inputType' => "dtmf",
                            'redirect' => "true",
                        ]);
                    $get_input->addSpeak($Question2);
                    $r->addSpeak($NoinputMessage);
                }
                else if ($digit == '2'){
                    $r->addSpeak($NegativeFeedback);
                }
                else {
                    $r->addSpeak($WronginputMessage);
                }
                Header('Content-type: text/xml');
                echo $r->toXML();
            }

            // Action URL block for Sales and Support branch
            public function secondBranch(Request $request)
            {
                // Message that Plivo reads when the recipient provides negative feedback
                $NegativeFeedback = "We're sorry about your bad experience, One of our representatives will get in touch with you";
                // Message that Plivo reads when the caller enters a wrong number
                $WronginputMessage = "Sorry, that's not a valid entry";

                $r = new Response();
                $digit = $_REQUEST['Digits'];
                if ($digit == '1'){
                    $body = "Thank you for participating in the survey";
                    $params = array(
                        'language' => "en-GB"
                    );
                    $r->addSpeak($body,$params);
                }
                else if ($digit == '2'){
                    $r->addSpeak($NegativeFeedback);
                }
                else {
                    $r->addSpeak($WronginputMessage);
                }
                Header('Content-type: text/xml');
                echo $r->toXML();
            }
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        <div class="notice-box">
          <strong>Note:</strong>
          We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables, to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch them from the environment variables. You can use `$_ENV` or `putenv/getenv` functions to store environment variables and fetch them when initializing the client.
        </div>

        ### Add a route

        Add a route for the forward function in the SurveyController class. Edit routes/web.php and add these lines.

        ```shell  theme={null}
        Route::match(['get', 'post'], '/survey', 'SurveyController@ivrMain');
        Route::match(['get', 'post'], '/firstbranch', 'SurveyController@firstBranch');
        Route::match(['get', 'post'], '/secondbranch', 'SurveyController@secondBranch');
        ```

        Start the Laravel server.

        ```shell  theme={null}
        $ php artisan serve
        ```

        You should see your basic server application in acation at [http://localhost:8000/survey](http://localhost:8000/survey).

        [Set up ngrok](/sdk/server/set-up-php-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

        ## Test

        Make a call to a Plivo phone number and see how the survey application works.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title=".NET">
    ## Overview

    Plivo lets you automate voice surveys for use cases such as collecting feedback from customers and conducting polling on political issues. You can set up multiple levels of questions and walk users through different paths depending on the keys they press in response to your questions, and save the responses for analysis.

    You can implement voice surveys either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to automate voice surveys with a few clicks on the PHLO canvas, and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Node.js, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * Click the **Start** node to open the Configuration tab to the right of the canvas, then enter the information to retrieve from the HTTP Request payload. For this example, enter From and To phone numbers and your business name.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/start_config.mp4?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=9262dc36cff409df19fb62ed6deebab7" data-path="images/start_config.mp4" />
          </Frame>

        * Validate the configuration by clicking **Validate**. Every time you finish configuring a node, click **Validate** to check the syntax and save your changes.

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. This adds an **Initiate Call** node onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call_customer.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=03b96867037cb2e2e3920f55c3a05bfc" data-path="images/call_customer.mp4" />
          </Frame>

        * In the Configuration tab of the **Initiate Call** node, rename the node to **Call\_Customer**. You can rename nodes as you like to improve your PHLO's readability. To enter values for the From and To fields, start typing two curly brackets. PHLO will display a list of all available variables; choose the appropriate ones. When you use variables in a PHLO, the values are retrieved from the HTTP Request payload you defined in the Start node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call_customer_config.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=2078b426506e6c7787053203de00d06c" data-path="images/call_customer_config.mp4" />
          </Frame>

        * Next, drag and drop the **IVR Menu** component onto the canvas. Draw a line to connect the **Initiate Call** node‘s **Answered** trigger state to the IVR Menu node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_1.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=0e5e5dec3ac0e1c8c007c04045daee30" data-path="images/question_1.mp4" />
          </Frame>

        * Click the **IVR Menu** node to open its Configuration tab. Rename the **IVR Menu** node **Question\_1**. For this example, select **1** and **2** as allowed choices. In the Speak Text box, enter a message to play to the user that introduces the survey and states the choices they can respond with. If you like, you can also configure the Language and Voice fields for the message.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_1_config.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=65c71c8e745edb6b2faa1a05c469068c" data-path="images/question_1_config.mp4" />
          </Frame>

        * Repeat the process with another **IVR Menu** node. Rename it **Question\_2**.

        * To daisy-chain to the second question after the user gives a valid response to question 1, connect the **Question\_1** node‘s **1** and **2** trigger states to the **Question\_2** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_2.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=c463df1f9c685a9fd35974ea183c1b5f" data-path="images/question_2.mp4" />
          </Frame>

        * Configure the choices for **Question\_2** on its **Configuration** tab. Again, select **1** and **2** as allowed choices and enter a message to play to the user.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/question_2_config.mp4?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=3062979820e40e30eb382925f563be2b" data-path="images/question_2_config.mp4" />
          </Frame>

        * Drag and drop the **Play Audio** component onto the canvas. Draw a line to connect the **Question\_2** node‘s **1** and **2** trigger states to the **Play Audio** node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/acknowledge_participation.mp4?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=bd159c8c416868549fa8be707a613fa6" data-path="images/acknowledge_participation.mp4" />
          </Frame>

        * In its Configuration tab, rename the node to **Acknowledge\_Participation**. Enter a message of thanks to play to the user in the node‘s Speak Text box.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/acknowledge_participation_config.mp4?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=220bf7ac1b7faa27844c69a0e075c403" data-path="images/acknowledge_participation_config.mp4" />
          </Frame>

        * Drag and drop the **HTTP Request** component onto the canvas. Draw a line to connect the **Acknowledge\_Participation** node‘s **Prompt Completed** trigger state to the HTTP Request node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/handle_callback_voice_survey.mp4?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=918061ee1f2a6b9e8d3d89ca04776c14" data-path="images/handle_callback_voice_survey.mp4" />
          </Frame>

        * Rename the **HTTP Request** node **Handle\_Callback**. Configure the node to post the survey results to a website. On its Configuration tab, enter key names `answer1` and `answer2`. For their values, begin typing two curly brackets to view all available variables, then select **Question\_1.digits** and **Question\_2.digits**.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/handle_callback_config.mp4?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=45ab508b76b09714acead46d6e65f176" data-path="images/handle_callback_config.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        ### With static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

        In Visual Studio, open the file in the CS project called `Program.cs` and paste into it this code.

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

        ### With dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code to the PHLO when you trigger it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        #### Code

        In Visual Studio, open the file in the CS project called `Program.cs` and paste into it this code.

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
                        { "from", "<caller_id>" },
                        { "to", "<destination_number>" }

                    };
                    Console.WriteLine(phlo.Run(data));
                }
            }
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.
      </Tab>

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to implement voice surveys.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a voice survey application in C\#

        In Visual Studio, create a controller called `SurveyController.cs` and paste into it this code.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_controller.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=a7ec7769fad39d920defa0ec18f44dcd" alt="" width="1440" height="680" data-path="images/create_controller.png" />
        </Frame>

        ```cs  theme={null}
        using System;
        using System.Collections.Generic;
        using System.Diagnostics;
        using System.Linq;
        using System.Threading.Tasks;
        using Microsoft.AspNetCore.Mvc;
        using Plivo.XML;

        namespace Receivecall.Controllers
        {
            public class SurveyController : Controller
            {
                // Message that Plivo reads when the call recipient answers
                String Question1 = "Hi, this is a call from Plivo. How would you rate your overall satisfaction with our services? Press 1 if you're satisfied. Press 2 to suggest improvements";
                String Question2 = "How would you rate your satisfaction with our customer service? Press 1 if you're satisfied. Press 2 to suggest improvements";
                // Message that Plivo reads when the recipient provides negative feedback
                String NegativeFeedback = "We're sorry about your bad experience. One of our representatives will get in touch with you";
                // Message that Plivo reads when the caller does nothing
                String NoinputMessage = "Sorry, I didn't catch that. Please hang up and try again";
                // Message that Plivo reads when the caller enters an invalid number
                String WronginputMessage = "Sorry, that's not a valid entry";

                // GET: /<controller>/ -12/
                public IActionResult Index()
                {
                    var resp = new Response();
                    Plivo.XML.GetInput get_input = new
                        Plivo.XML.GetInput("",
                            new Dictionary<string, string>()
                            {
                                {"action", "https://<yourdomain>.com/survey/firstbranch/"},
                                {"method", "POST"},
                                {"digitEndTimeout", "5"},
                                {"inputType", "dtmf"},
                                {"redirect", "true"},
                            });
                    resp.Add(get_input);
                    get_input.AddSpeak(Question1,
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
                        String getinput_action_url = "https://<yourdomain>.com/survey/secondbranch/";

                        // Add GetInput XML Tag
                        Plivo.XML.GetInput get_input = new
                        Plivo.XML.GetInput("",
                            new Dictionary<string, string>()
                            {
                                {"action", getinput_action_url},
                                {"method", "POST"},
                                {"digitEndTimeout", "5"},
                                {"finishOnKey", "#"},
                                {"inputType", "dtmf"},
                                {"redirect", "true"},
                            });
                        resp.Add(get_input);
                        get_input.AddSpeak(Question2,
                            new Dictionary<string, string>() { });
                        resp.AddSpeak(NoinputMessage,
                            new Dictionary<string, string>() { });
                    }
                    else if (digit == "2")
                    {
                        // Add Speak XML Tag
                        resp.AddSpeak(NegativeFeedback,
                            new Dictionary<string, string>() { });
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
                // Second branch of IVR phone tree
                public IActionResult SecondBranch()
                {
                    var resp = new Response();
                    String digit = Request.Query["Digits"];
                    Debug.WriteLine("Digit pressed : {0}", digit);

                    // Add Speak XMLTag
                    if (digit == "1")
                    {
                        resp.AddSpeak("Thank you for participating in the survey",
                           new Dictionary<string, string>()
                           {
                            { "language","en-GB"}
                        });
                    }
                    else if (digit == "2")
                    {
                        // Add Speak XML Tag
                        resp.AddSpeak(NegativeFeedback,
                            new Dictionary<string, string>() { });
                    }
                    else
                    {
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

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        <Note>
          <strong>Note:</strong>We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables, to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use the `<a href="https://docs.microsoft.com/en-us/dotnet/api/system.environment.setenvironmentvariable?view=netcore-3.1" rel="nofollow">Environment.SetEnvironmentVariable</a>` method to store environment variables and `<a href="https://docs.microsoft.com/en-us/dotnet/api/system.environment.getenvironmentvariable?view=netcore-3.1" rel="nofollow">Environment.GetEnvironmentVariable</a>` to fetch them when initializing the client.
        </Note>

        Before starting the application, edit Properties/launchSettings.json and set the applicationUrl as

        ```json  theme={null}
        "applicationUrl": "http://localhost:5000/"
        ```

        Run the project and you should see your basic server application in action at [http://localhost:5000/survey/](http://localhost:5000/survey/).

        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/build_app.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=57ed7d2310aa904fb31a34ad205f863c" alt="" width="1116" height="444" data-path="images/build_app.jpg" />
        </Frame>

        [Set up ngrok](/sdk/server/set-up-dotnet-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

        ## Test

        Make a call to a Plivo phone number and see how the survey application works.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Java">
    ## Overview

    Plivo lets you automate voice surveys for use cases such as collecting feedback from customers and conducting polling on political issues. You can set up multiple levels of questions and walk users through different paths depending on the keys they press in response to your questions, and save the responses for analysis.

    You can implement voice surveys either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to automate voice surveys with a few clicks on the PHLO canvas, and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Node.js, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * Click the **Start** node to open the Configuration tab to the right of the canvas, then enter the information to retrieve from the HTTP Request payload. For this example, enter From and To phone numbers and your business name.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/start_config.mp4?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=9262dc36cff409df19fb62ed6deebab7" data-path="images/start_config.mp4" />
          </Frame>

        * Validate the configuration by clicking **Validate**. Every time you finish configuring a node, click **Validate** to check the syntax and save your changes.

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. This adds an **Initiate Call** node onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call_customer.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=03b96867037cb2e2e3920f55c3a05bfc" data-path="images/call_customer.mp4" />
          </Frame>

        * In the Configuration tab of the **Initiate Call** node, rename the node to **Call\_Customer**. You can rename nodes as you like to improve your PHLO's readability. To enter values for the From and To fields, start typing two curly brackets. PHLO will display a list of all available variables; choose the appropriate ones. When you use variables in a PHLO, the values are retrieved from the HTTP Request payload you defined in the Start node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call_customer_config.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=2078b426506e6c7787053203de00d06c" data-path="images/call_customer_config.mp4" />
          </Frame>

        * Next, drag and drop the **IVR Menu** component onto the canvas. Draw a line to connect the **Initiate Call** node‘s **Answered** trigger state to the IVR Menu node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_1.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=0e5e5dec3ac0e1c8c007c04045daee30" data-path="images/question_1.mp4" />
          </Frame>

        * Click the **IVR Menu** node to open its Configuration tab. Rename the **IVR Menu** node **Question\_1**. For this example, select **1** and **2** as allowed choices. In the Speak Text box, enter a message to play to the user that introduces the survey and states the choices they can respond with. If you like, you can also configure the Language and Voice fields for the message.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_1_config.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=65c71c8e745edb6b2faa1a05c469068c" data-path="images/question_1_config.mp4" />
          </Frame>

        * Repeat the process with another **IVR Menu** node. Rename it **Question\_2**.

        * To daisy-chain to the second question after the user gives a valid response to question 1, connect the **Question\_1** node‘s **1** and **2** trigger states to the **Question\_2** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_2.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=c463df1f9c685a9fd35974ea183c1b5f" data-path="images/question_2.mp4" />
          </Frame>

        * Configure the choices for **Question\_2** on its **Configuration** tab. Again, select **1** and **2** as allowed choices and enter a message to play to the user.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/question_2_config.mp4?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=3062979820e40e30eb382925f563be2b" data-path="images/question_2_config.mp4" />
          </Frame>

        * Drag and drop the **Play Audio** component onto the canvas. Draw a line to connect the **Question\_2** node‘s **1** and **2** trigger states to the **Play Audio** node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/acknowledge_participation.mp4?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=bd159c8c416868549fa8be707a613fa6" data-path="images/acknowledge_participation.mp4" />
          </Frame>

        * In its Configuration tab, rename the node to **Acknowledge\_Participation**. Enter a message of thanks to play to the user in the node‘s Speak Text box.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/acknowledge_participation_config.mp4?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=220bf7ac1b7faa27844c69a0e075c403" data-path="images/acknowledge_participation_config.mp4" />
          </Frame>

        * Drag and drop the **HTTP Request** component onto the canvas. Draw a line to connect the **Acknowledge\_Participation** node‘s **Prompt Completed** trigger state to the HTTP Request node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/handle_callback_voice_survey.mp4?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=918061ee1f2a6b9e8d3d89ca04776c14" data-path="images/handle_callback_voice_survey.mp4" />
          </Frame>

        * Rename the **HTTP Request** node **Handle\_Callback**. Configure the node to post the survey results to a website. On its Configuration tab, enter key names `answer1` and `answer2`. For their values, begin typing two curly brackets to view all available variables, then select **Question\_1.digits** and **Question\_2.digits**.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/handle_callback_config.mp4?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=45ab508b76b09714acead46d6e65f176" data-path="images/handle_callback_config.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        ### With static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

        Create a Java class in the project called `TriggerPhlo` and paste into it this code.

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

        ### With dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code to the PHLO when you trigger it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        #### Code

        Create a Java class in the project called `TriggerPhlo` and paste into it this code.

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
                payload.put("from", "<caller_id>");
                payload.put("to", "<destination_number>");
                PhloUpdateResponse response = Phlo.updater(phloId).payload(payload).run();
            }
        }
        ```

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phlo\_id placeholder with your PHLO ID from the [Plivo console](https://cx.plivo.com/agents). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        ## Test

        Save the file and run it.
      </Tab>

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to implement voice surveys.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a voice survey application in Java

        Create a Java class called `Survey` and paste into it this code.

        ```java  theme={null}
        import static spark.Spark.*;

        import com.plivo.api.xml.GetInput;
        import com.plivo.api.xml.Play;
        import com.plivo.api.xml.Response;
        import com.plivo.api.xml.Speak;

        public class IVR {
            public static void main(String[] args) {
                // Message that Plivo reads when the call recipient answers
                String Question1 = "Hi, this is a call from Plivo. How would you rate your overall satisfaction with our services? Press 1 if you're satisfied or 2 to suggest improvements";
                String Question2 = "How would you rate your satisfaction with our customer service? Press 1 if you're satisfied or 2 to suggest improvements";
                // Message that Plivo reads when the recipient provides negative feedback
                String NegativeFeedback = "We're sorry about your bad experience. One of our representatives will get in touch with you";
                // Message that Plivo reads when the caller does nothing
                String NoinputMessage = "Sorry, I didn't catch that. Please hang up and try again";
                // Message that Plivo reads when the caller enters an invalid number
                String WronginputMessage = "Sorry, that's not a valid entry";
                post("/survey/", (request, response) -> {
                    response.type("application/xml");
                    Response resp = new Response();
                    resp.children(
                        new GetInput()
                                .action("https://<yourdomain>.com/ivr/firstbranch/")
                                .method("POST")
                                .inputType("dtmf")
                                .digitEndTimeout(5)
                                .redirect(true)
                                .children(
                                        new Speak(Question1)
                                )
                    );
                    resp.children(new Speak(NoinputMessage));
                    return resp.toXmlString();
                });
                post("/survey/firstbranch/", (request, response) -> {
                    response.type("application/xml");
                    String digit = request.queryParams("Digits");
                    Response resp = new Response();
                    if (digit.equals("1")){
                        resp.children(
                                new GetInput()
                                        .action("https://<yourdomain>.com/ivr/secondbranch/")
                                        .method("POST")
                                        .inputType("dtmf")
                                        .digitEndTimeout(5)
                                        .redirect(true)
                                        .children(
                                                new Speak(Question2)
                                        )
                        );
                        resp.children(new Speak(NoinputMessage));
                    }
                    else if (digit.equals("2")){
                        resp.children(
                                new Speak(NegativeFeedback)
                        );
                    }
                    else {
                        resp.children(
                                new Speak(WronginputMessage)
                        );
                    }
                    return resp.toXmlString();
                });
                post("/survey/secondbranch/", (request, response) -> {
                    response.type("application/xml");
                    String digit = request.queryParams("Digits");
                    Response resp = new Response();
                    if (digit.equals("1")){
                        resp.children(
                                new Speak("Thank you for participating in the survey", "MAN","en-GB",1)
                        );
                    }
                    else if (digit.equals("2")){
                        resp.children(
                                new Speak(NegativeFeedback)
                        );
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

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        <Note>
          <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables, to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `<a rel="nofollow" href="https://docs.oracle.com/javase/tutorial/essential/environment/env.html">System.getenv()</a>` to store environment variables and retrieve them when initializing the client.
        </Note>

        Save the file and run it. You should see your basic server application in action at [http://localhost:4567/survey/](http://localhost:4567/survey/).

        [Set up ngrok](/sdk/server/set-up-java-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

        ## Test

        Make a call to a Plivo phone number and see how the survey application works.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Go">
    ## Overview

    Plivo lets you automate voice surveys for use cases such as collecting feedback from customers and conducting polling on political issues. You can set up multiple levels of questions and walk users through different paths depending on the keys they press in response to your questions, and save the responses for analysis.

    You can implement voice surveys either by using our PHLO visual workflow builder or our APIs and XML documents. Follow the instructions in one of the tabs below.

    <Tabs>
      <Tab title="Using PHLO">
        You can create and deploy a PHLO to automate voice surveys with a few clicks on the PHLO canvas, and trigger it with a few lines of code.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time triggering a PHLO with Node.js, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/).

        ## Create the PHLO

        To create a PHLO, visit the [PHLO](https://cx.plivo.com/agents) page of the Plivo console. If this is your first PHLO, the PHLO page will be empty.

        * Click **Create New PHLO**.

        * In the **Choose your use case** pop-up, click **Build my own**. The PHLO canvas will appear with the **Start** node.

          <Note>
            <strong>Note:</strong> The Start node is the starting point of any PHLO. It lets you trigger a PHLO to start upon one of three actions: incoming SMS message, incoming call, or API request.
          </Note>

        * Click the **Start** node to open the Configuration tab to the right of the canvas, then enter the information to retrieve from the HTTP Request payload. For this example, enter From and To phone numbers and your business name.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/start_config.mp4?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=9262dc36cff409df19fb62ed6deebab7" data-path="images/start_config.mp4" />
          </Frame>

        * Validate the configuration by clicking **Validate**. Every time you finish configuring a node, click **Validate** to check the syntax and save your changes.

        * From the list of components on the left side, drag and drop the **Initiate Call** component onto the canvas. This adds an **Initiate Call** node onto the canvas. When a component is placed on the canvas it becomes a node.

        * Draw a line to connect the **Start** node’s **API Request** trigger state to the **Initiate Call** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call_customer.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=03b96867037cb2e2e3920f55c3a05bfc" data-path="images/call_customer.mp4" />
          </Frame>

        * In the Configuration tab of the **Initiate Call** node, rename the node to **Call\_Customer**. You can rename nodes as you like to improve your PHLO's readability. To enter values for the From and To fields, start typing two curly brackets. PHLO will display a list of all available variables; choose the appropriate ones. When you use variables in a PHLO, the values are retrieved from the HTTP Request payload you defined in the Start node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/call_customer_config.mp4?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=2078b426506e6c7787053203de00d06c" data-path="images/call_customer_config.mp4" />
          </Frame>

        * Next, drag and drop the **IVR Menu** component onto the canvas. Draw a line to connect the **Initiate Call** node‘s **Answered** trigger state to the IVR Menu node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_1.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=0e5e5dec3ac0e1c8c007c04045daee30" data-path="images/question_1.mp4" />
          </Frame>

        * Click the **IVR Menu** node to open its Configuration tab. Rename the **IVR Menu** node **Question\_1**. For this example, select **1** and **2** as allowed choices. In the Speak Text box, enter a message to play to the user that introduces the survey and states the choices they can respond with. If you like, you can also configure the Language and Voice fields for the message.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_1_config.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=65c71c8e745edb6b2faa1a05c469068c" data-path="images/question_1_config.mp4" />
          </Frame>

        * Repeat the process with another **IVR Menu** node. Rename it **Question\_2**.

        * To daisy-chain to the second question after the user gives a valid response to question 1, connect the **Question\_1** node‘s **1** and **2** trigger states to the **Question\_2** node.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/question_2.mp4?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=c463df1f9c685a9fd35974ea183c1b5f" data-path="images/question_2.mp4" />
          </Frame>

        * Configure the choices for **Question\_2** on its **Configuration** tab. Again, select **1** and **2** as allowed choices and enter a message to play to the user.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/question_2_config.mp4?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=3062979820e40e30eb382925f563be2b" data-path="images/question_2_config.mp4" />
          </Frame>

        * Drag and drop the **Play Audio** component onto the canvas. Draw a line to connect the **Question\_2** node‘s **1** and **2** trigger states to the **Play Audio** node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/acknowledge_participation.mp4?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=bd159c8c416868549fa8be707a613fa6" data-path="images/acknowledge_participation.mp4" />
          </Frame>

        * In its Configuration tab, rename the node to **Acknowledge\_Participation**. Enter a message of thanks to play to the user in the node‘s Speak Text box.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/acknowledge_participation_config.mp4?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=220bf7ac1b7faa27844c69a0e075c403" data-path="images/acknowledge_participation_config.mp4" />
          </Frame>

        * Drag and drop the **HTTP Request** component onto the canvas. Draw a line to connect the **Acknowledge\_Participation** node‘s **Prompt Completed** trigger state to the HTTP Request node.

          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/handle_callback_voice_survey.mp4?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=918061ee1f2a6b9e8d3d89ca04776c14" data-path="images/handle_callback_voice_survey.mp4" />
          </Frame>

        * Rename the **HTTP Request** node **Handle\_Callback**. Configure the node to post the survey results to a website. On its Configuration tab, enter key names `answer1` and `answer2`. For their values, begin typing two curly brackets to view all available variables, then select **Question\_1.digits** and **Question\_2.digits**.
          <Frame>
            <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/handle_callback_config.mp4?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=45ab508b76b09714acead46d6e65f176" data-path="images/handle_callback_config.mp4" />
          </Frame>

        * Give the PHLO a name by clicking in the upper left, then click **Save**.

        Your PHLO is now ready to test.

        ## Trigger the PHLO

        You integrate a PHLO into your application workflow by making an API request to trigger the PHLO with the required payload — the set of parameters you pass to the PHLO. You can define a static payload by specifying values when you create the PHLO, or define a dynamic payload by passing values through parameters when you trigger the PHLO from your application.

        ### With static payload

        When you configure values when creating the PHLO, they act as a static payload.

        <Frame>
                    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/static_payload.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e34e3011bffc239aa02054403be0e79a" alt="" width="1398" height="765" data-path="images/static_payload.png" />
        </Frame>

        #### Code

        Create a file called `TriggerPhlo.go` and paste into it this code.

        ```go  theme={null}
        package main

        import (
        	"fmt"
        	"plivo-go"
        )
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

        ### With dynamic payload

        To use dynamic values for the parameters, use Liquid templating parameters when you create the PHLO and pass the values from your code to the PHLO when you trigger it.

        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/dynamic_payload.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=9af2698b7d971dfa9ad451e66d038256" alt="" width="1398" height="765" data-path="images/dynamic_payload.png" />
        </Frame>

        #### Code

        Create a file called `TriggerPhlo.go` and paste into it this code.

        ```go  theme={null}
        package main

        import (
        	"fmt"
        	"plivo-go"
        )
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
        		"from": "<caller_id>",
        		"to":   "<destination_number>",
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

      <Tab title="Using XML">
        Here’s how to use Plivo APIs and XML to implement voice surveys.

        ## How it works

        <Frame>
                    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/make-bulk-calls.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=fea79ace9feb45bfb5ee7bbb98831781" alt="" width="1446" height="774" data-path="images/make-bulk-calls.png" />
        </Frame>

        Plivo requests an answer URL when the call is answered (step 4) and expects the file at that address to hold a valid XML response from the application with instructions on how to handle the call.

        ## Prerequisites

        To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

        ## Create a voice survey application in Go

        Create a file called `survey.go` and paste into it this code.

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
        	// Message that Plivo reads when the call recipient answers
          Question1 = "Hi, this is a call from Plivo. How would you rate your overall satisfaction with our services? Press 1 if you're satisfied or 2 to suggest improvements"
          Question2 = "How would you rate your satisfaction with our customer service? Press 1 if you're satisfied or 2 to suggest improvements"
          // Message that Plivo reads when the recipient provides negative feedback
          NegativeFeedback = "We're sorry about your bad experience. One of our representatives will get in touch with you"
          // Message that Plivo reads when the caller does nothing
          NoinputMessage = "Sorry, I didn't catch that. Please hang up and try again"
          // Message that Plivo reads when the caller enters an invalid number
          WronginputMessage = "Sorry, that's not a valid entry"
        	)

        	m.Post("/survey/", func(w http.ResponseWriter, r *http.Request) string {
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
        					AddSpeak(Question1),
        					}),
        				new(xml.SpeakElement).
        					AddSpeak(NoInputMessage),
        			},
        		}
        		return response.String()
        	})

        	m.Post("/survey/firstbranch/", func(w http.ResponseWriter, r *http.Request) string {
        	w.Header().Set("Content-Type", "application/xml")
        	digit := r.FormValue("Digits")
        	if digit == "1" {
        		return xml.ResponseElement{
        			Contents: []interface{}{
        				new(xml.GetInputElement).
        				SetAction("https://<yourdomain>.com/ivr/firstbranch/").
        				SetMethod("POST").
        				SetDigitEndTimeout(5).
        				SetInputType("dtmf").
        				SetRedirect(true).
        				SetContents([]interface{}{new(xml.SpeakElement).
        					AddSpeak(Question2),
        					}),
        				new(xml.SpeakElement).
        					AddSpeak(NoInputMessage),
        			},
        		}.String()
        	} else if digit == "2" {
        		return xml.ResponseElement{
        			Contents: []interface{}{
        				new(xml.SpeakElement).
        					AddSpeak(NegativeFeedback),
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

        	m.Post("/survey/secondbranch/", func(w http.ResponseWriter, r *http.Request) string {
        		w.Header().Set("Content-Type", "application/xml")
        		digit := r.FormValue("Digits")
        		if digit == "1" {
        			return xml.ResponseElement{
        				Contents: []interface{}{
        					new(xml.SpeakElement).
        						SetLanguage("en-GB").
        						AddSpeak("Thank you for participating in the survey"),
        					},
        				}.String()
        		} else if digit == "2" {
        		return xml.ResponseElement{
        			Contents: []interface{}{
        				new(xml.SpeakElement).
        					AddSpeak(NegativeFeedback),
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

        Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

        <Note>
          <strong>Note:</strong>We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables, to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `os.Setenv` and `os.Getenv` functions to store environment variables and fetch them when initializing the client.
        </Note>

        Save the file and run it.

        ```shell  theme={null}
        go run survey.go
        ```

        You should see your basic server application in action at [http://localhost:8080/survey/](http://localhost:8080/survey/).

        [Set up ngrok](/sdk/server/set-up-go-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

        ## Test

        Make a call to a Plivo phone number and see how the survey application works.
      </Tab>
    </Tabs>
  </Tab>
</Tabs>
