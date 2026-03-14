# Source: https://plivo.com/docs/voice/use-cases/number-masking.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Number Masking

> Hide caller and recipient phone numbers using proxy number masking

<Tabs>
  <Tab title="Node">
    ## Overview

    Phone number masking hides the phone numbers of parties in a call from each other. Many businesses find it advantageous to anonymize communication between two parties — for example, between a customer and a delivery agent on a food delivery service platform or a driver and a rider using a ride-hailing application. Businesses can implement phone number masking by sending calls through an intermediate phone number that acts as a proxy between the two parties. A Plivo number can serve as the intermediate number to connect the two parties while keeping their contact information private.

    ## How it works

    <Tabs>
      <Tab title="Customer calls agent">
        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/customer-calls-agent.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=90ed32982a971c334a1241cb00056274" alt="" width="1446" height="774" data-path="images/customer-calls-agent.png" />
        </Frame>
      </Tab>

      <Tab title="Agent calls customer">
        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/agent-calls-customer.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=08b157996f03f2c61b2e920017ad594f" alt="" width="1446" height="774" data-path="images/agent-calls-customer.png" />
        </Frame>
      </Tab>
    </Tabs>

    As an example, we’ll build a number-masking application for a food delivery service that lets the company connect customers with delivery agents and vice versa without revealing any actual phone numbers. To do this, you

    1. Create a customer-to-agent phone number mapping in your application’s back end.
    2. Create the number masking application using Plivo.
    3. Assign the number masking application to a Plivo number.

    ## Prerequisites

    To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

    ## Create a 1:1 map with actual numbers

    Create customer-to-agent phone number mapping for the application. Whenever a customer places an order, their phone number should be stored in a database for your application to access. A delivery agent will be assigned for the order, and the agent’s number will also be stored in your database, and will be mapped to the customer's number:

    ```
    Customer’s Number		<->		Agent’s Number
    1-415-666-7777					1-415-666-7778
    ```

    We created sample mapping data in a config.js file:

    ```javascript  theme={null}
        const config = {app: {port: 5000}}
    	config.customerAgentMap = {
    		'14156667777':'14156667778', 
    		'14156667779':'14156667780', 
    		'14156667781':'14156667782'
    	};
    	module.exports = config;
    ```

    ## Create an Express application for number masking

    Create a file called `number_masking.js` and paste into it this code.

    ```js  theme={null}
    const config = require('./config');
    const plivo = require('plivo');
    const express = require('express');
    const app = express();
    app.set('port', (process.env.PORT || 5000));

    // Handle incoming calls to a Plivo number, connect agent with customer and vice versa without revealing their actual phone numbers. 
    app.all('/handleincoming/', function(req, res) {
        const fromNumber = (req.query.From);
        const toNumber = (req.query.To);
        const response = plivo.Response();
        const customerPhoneMapping = config.customerAgentMap;
        const agentCustomerMapping = Object.fromEntries(Object.entries(customerPhoneMapping).map(v => v.reverse()));
        if(fromNumber in customerPhoneMapping){ // Check whether the customer's number is in the customer-agent mapping
            const number = customerPhoneMapping[fromNumber]; // Assign the value from the customer-agent array to number variable
            const params = {
                'callerId': toNumber, // Plivo number is used as the caller ID for the call toward the agent
            };
            const dial = response.addDial(params);
            const destNumber = number;
            dial.addNumber(destNumber);
            res.send(response.toXML());
        }
        else if(fromNumber in agentCustomerMapping){ // Check whether the agent's number is in the customer-agent mapping
            const number = agentCustomerMapping[fromNumber]; // Assign the key from the customer-agent array to number variable
            const params = {
                'callerId': toNumber, // Plivo number is used as the caller ID for the call toward the customer
            };
            const dial = response.addDial(params);
            const destNumber = number;
            dial.addNumber(destNumber);
            res.send(response.toXML());
        }
    });

    app.listen(app.get('port'), function () {
    	console.log('Node app is running on port', app.get('port'));
    });
    ```

    Save the file and run it.

    ```shell  theme={null}
    $ node number_masking.js
    ```

    You should see your basic server application in action at [http://localhost:5000/handleincoming/](http://localhost:5000/handleincoming/).

    [Set up ngrok](/sdk/server/set-up-node-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

    Now people can call your Plivo number. If an incoming call to your Plivo number is from one of the customer phone numbers in the customer-agent map — for example, if the caller number is `14156667777` — then Plivo will send the XML response to process the incoming call as below, and you can check the XML document in your browser.

    <Frame>
            <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ngrok_c2a.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=311a77ec6bada079d064bbf183a81ff5" alt="" width="1538" height="418" data-path="images/ngrok_c2a.png" />
    </Frame>

    If the incoming call to your Plivo number is from one of the agent phone numbers in the customer-agent map — for example, if the caller number is `14156667778` — then Plivo will send the XML response to process the incoming call as below, and you can check the XML document in your browser.

    <Frame>
            <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ngrok_a2c.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=9dc67f44fa072efd286b8f9da8d3882f" alt="" width="1562" height="378" data-path="images/ngrok_a2c.png" />
    </Frame>

    ## Create a Plivo application

    Associate the Express application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

    Give your application a name — we called ours `Number Masking`. Enter the server URL you want to use (for example, https\://\<ngrok\_identifier>.ngrok.io/handleincoming/) in the `Answer URL` field and set the method as `GET`.  Click **Create Application** to save your application.

    <Frame>
            <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_masking.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=cf592df075798ef478707538f45c4075" alt="" width="1439" height="821" data-path="images/create_masking.png" />
    </Frame>

    ## Assign a Plivo number to your application

    Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

    From the Application Type drop-down, select `XML Application`.

    From the Plivo Application drop-down, select `Number Masking` (the name we gave the application).

    Click **Update Number** to save.

    <Frame>
            <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_masking.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=427b5db48eb7204267e6a9cda90bbf53" alt="" width="2762" height="1578" data-path="images/assign_masking.png" />
    </Frame>

    ## Test

    To test the application, you need two Plivo numbers. Set up one of your numbers as a customer and another as an agent in the customer-to-agent mapping data in the config file. Make a call from each of your mobile numbers to the Plivo number you mapped to the application. You should see that the call is forwarded to the other number, and that the incoming call has the Plivo number as the caller ID.
  </Tab>

  <Tab title="Ruby">
    ## Overview

    Phone number masking hides the phone numbers of parties in a call from each other. Many businesses find it advantageous to anonymize communication between two parties — for example, between a customer and a delivery agent on a food delivery service platform or a driver and a rider using a ride-hailing application. Businesses can implement phone number masking by sending calls through an intermediate phone number that acts as a proxy between the two parties. A Plivo number can serve as the intermediate number to connect the two parties while keeping their contact information private.

    ## Outline

    <Tabs>
      <Tab title="Customer calls agent">
        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/customer-calls-agent.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=90ed32982a971c334a1241cb00056274" alt="" width="1446" height="774" data-path="images/customer-calls-agent.png" />
        </Frame>
      </Tab>

      <Tab title="Agent calls customer">
        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/agent-calls-customer.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=08b157996f03f2c61b2e920017ad594f" alt="" width="1446" height="774" data-path="images/agent-calls-customer.png" />
        </Frame>
      </Tab>
    </Tabs>

    As an example, we’ll build a number-masking application for a food delivery service that lets the company connect customers with delivery agents and vice versa without revealing any actual phone numbers. To do this, you

    1. Create a customer-to-agent phone number mapping in your application’s back end.
    2. Create the number masking application using Plivo.
    3. Assign the number masking application to a Plivo number.

    ## Prerequisites

    To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

    ## Create a 1:1 map with actual numbers

    Create customer-to-agent phone number mapping for the application. Whenever a customer places an order, their phone number should be stored in a database for your application to access. A delivery agent will be assigned for the order, and the agent’s number will also be stored in your database, and will be mapped to the customer's number:

    ```
    Customer’s Number		<->		Agent’s Number
    1-415-666-7777					1-415-666-7778
    ```

    We created sample mapping data in a config/application.rb file:

    ```
    # customer <> agent map
    config.base_map = {"14156667777" => "14156667778", "14156667779" => "14156667780", "14156667781" => "14156667782"}
    ```

    ## Create a Rails controller for number masking

    Change to the project directory and run the command `rails generate controller Numbermasking` to create a Rails controller named numbermasking\_controller in the app/controllers/ directory. Edit the app/controllers/numbermasking\_controller.rb file and paste into it this code:

    ```ruby  theme={null}
    include Plivo

    include Plivo::XML
    include Plivo::Exceptions

    \# Handle incoming calls to a Plivo number, connect agent with customer and vice versa without revealing their actual phone numbers. 
    class NumbermaskingController < ApplicationController
        def handle_incoming
            customer_agent_map = Rails.application.config.base_map
            agent_customer_map = customer_agent_map.invert
            from_number = params[:From]
            to_number = params[:To]
            response = Response.new()
            customer_to_agent = customer_agent_map.include?(from_number) # Check whether the customer's number is in the customer-agent mapping
            agent_to_customer = agent_customer_map.include?(from_number) # Check whether the agent's number is in the customer-agent mapping
            if(customer_to_agent == true)
                dest_number = customer_agent_map[from_number] # Assign the value from the customer-agent array to dest_number variable
                params = {
                'callerId' => to_number # Plivo number is used as the caller ID for the call toward the agent
                }
                dial = response.addDial(params)
                dial.addNumber(dest_number)
            elsif(agent_to_customer == true)
                dest_number = agent_customer_map[from_number] # Assign the key from the customer-agent array to dest_number variable
                params = {
                'callerId' => to_number # Plivo number is used as the caller ID for the call toward the customer
                }
                dial = response.addDial(params)
                dial.addNumber(dest_number)
            end
            xml = PlivoXML.new(response)
            puts xml.to_xml()
            render xml: xml.to_xml
        end
    end
    ```

    ### Add a route

    Add a route for the handle\_incoming function in NumbermaskingController class. Edit the config/routes.rb file and add this line after the outbound route:

    ```shell  theme={null}
    get 'numbermasking/handle_incoming'
    ```

    Start the Rails server to forward incoming calls.

    ```shell  theme={null}
    $ rails server
    ```

    You should see your basic server application in action at [http://localhost:3000/numbermasking/handle\_incoming/](http://localhost:3000/numbermasking/handle_incoming/).

    [Set up ngrok](/sdk/server/set-up-ruby-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

    <div class="notice-box">
      <strong>Note:</strong> Before you start the ngrok service, add ngrok in the config.hosts list in the config/environments/development.rb file and include the line below. You’ll start to see <i>Blocked host</i> errors if you fail to add this.
    </div>

    ```shell  theme={null}
    # Whitelist ngrok domain
    config.hosts << /[a-z0-9]+\.ngrok\.io/
    ```

    Now people can call your Plivo number. If an incoming call to your Plivo number is from one of the customer phone numbers in the customer-agent map — for example, if the caller number is `14156667777` — then Plivo will send the XML response to process the incoming call as below, and you can check the XML document in your browser.

    <Frame>
            <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ngrok_c2a-rails.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=1a5a758925026ec1f9b3681d6cd63898" alt="" width="1662" height="396" data-path="images/ngrok_c2a-rails.png" />
    </Frame>

    If the incoming call to your Plivo number is from one of the agent phone numbers in the customer-agent map — for example, if the caller number is `14156667778` — then Plivo will send the XML response to process the incoming call as below, and you can check the XML document in your browser.

    <Frame>
            <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ngrok_a2c-rails.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=e43e5a38c498be1cb4dd32715d097977" alt="" width="1658" height="364" data-path="images/ngrok_a2c-rails.png" />
    </Frame>

    ## Create a Plivo application

    Associate the Rails controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

    Give your application a name — we called ours `Number Masking`. Enter the server URL you want to use (for example, https\://\<ngrok\_identifier>.ngrok.io/handleincoming/) in the `Answer URL` field and set the method as `GET`.  Click **Create Application** to save your application.

    <Frame>
            <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_masking.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=cf592df075798ef478707538f45c4075" alt="" width="1439" height="821" data-path="images/create_masking.png" />
    </Frame>

    ## Assign a Plivo number to your application

    Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

    From the Application Type drop-down, select `XML Application`.

    From the Plivo Application drop-down, select `Number Masking` (the name we gave the application).

    Click **Update Number** to save.

    <Frame>
            <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_masking.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=427b5db48eb7204267e6a9cda90bbf53" alt="" width="2762" height="1578" data-path="images/assign_masking.png" />
    </Frame>

    ## Test

    To test the application, you need two Plivo numbers. Set up one of your numbers as a customer and another as an agent in the customer-to-agent mapping data in the config file. Make a call from each of your mobile numbers to the Plivo number you mapped to the application. You should see that the call is forwarded to the other number, and that the incoming call has the Plivo number as the caller ID.
  </Tab>

  <Tab title="Python">
    ## Overview

    Phone number masking hides the phone numbers of parties in a call from each other. Many businesses find it advantageous to anonymize communication between two parties — for example, between a customer and a delivery agent on a food delivery service platform or a driver and a rider using a ride-hailing application. Businesses can implement phone number masking by sending calls through an intermediate phone number that acts as a proxy between the two parties. A Plivo number can serve as the intermediate number to connect the two parties while keeping their contact information private.

    ## How it works

    <Tabs>
      <Tab title="Customer calls agent">
        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/customer-calls-agent.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=90ed32982a971c334a1241cb00056274" alt="" width="1446" height="774" data-path="images/customer-calls-agent.png" />
        </Frame>
      </Tab>

      <Tab title="Agent calls customer">
        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/agent-calls-customer.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=08b157996f03f2c61b2e920017ad594f" alt="" width="1446" height="774" data-path="images/agent-calls-customer.png" />
        </Frame>
      </Tab>
    </Tabs>

    As an example, we’ll build a number-masking application for a food delivery service that lets the company connect customers with delivery agents and vice versa without revealing any actual phone numbers. To do this, you

    1. Create a customer-to-agent phone number mapping in your application’s back end.
    2. Create the number masking application using Plivo.
    3. Assign the number masking application to a Plivo number.

    ## Prerequisites

    To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

    ## Create a 1:1 map with actual numbers

    Create customer-to-agent phone number mapping for the application. Whenever a customer places an order, their phone number should be stored in a database for your application to access. A delivery agent will be assigned for the order, and the agent’s number will also be stored in your database, and will be mapped to the customer's number:

    ```
    Customer’s Number		<->		Agent’s Number
    1-415-666-7777					1-415-666-7778
    ```

    We created sample mapping data in a config.ini file:

    ```
    [c2amap]
    customer_agent = {"14156667777":"14156667778", "14156667779":"14156667780", "14156667781":"14156667782"}
    ```

    ## Create a Flask application for number masking

    Create a file called `number_masking.py` and paste into it this code.

    ```py  theme={null}
    import json
    from flask import Flask, Response, request
    from configparser import ConfigParser
    from plivo import plivoxml

    config = ConfigParser()
    config.read('config.ini')
    app = Flask(__name__)

    \# Handle incoming calls to a Plivo number, connect agent with customer and vice versa without revealing their actual phone numbers. 
    @app.route("/handleincoming/", methods=["GET", "POST"])
    def number_masking():
        base_map = config.get("c2amap","customer_agent")
        customer_agent_map = json.loads(base_map) # Customer-agent mapping data
        agent_customer_map = {v: k for k, v in customer_agent_map.items()} # Agent-customer mapping data
        from_number = request.form.get("From") or request.args.get("From") 
        to_number = request.form.get("To") or request.args.get("To")
        response = plivoxml.ResponseElement()
        if from_number in customer_agent_map: # Check whether the customer's number is in the customer-agent mapping
            number = customer_agent_map[from_number] # Assign the value from the customer-agent array to number variable
            response.add(
                plivoxml.DialElement(
                    caller_id=to_number, # Plivo number is used as the caller ID for the call toward the agent
                ).add(plivoxml.NumberElement(number))
            )
        elif from_number in agent_customer_map: # Check whether the agent's number is in the customer-agent mapping
            number = agent_customer_map[from_number] # Assign the key from the customer-agent array to number variable
            response.add(
                plivoxml.DialElement(
                    caller_id=to_number, # Plivo number is used as the caller ID for the call toward the customer
                ).add(plivoxml.NumberElement(number))
            )
        print(response)
        return Response(response.to_string(), mimetype='application/xml')

    if __name__ == "__main__":
        app.run(host="0.0.0.0", debug=True)
    ```

    Save the file and run it.

    ```shell  theme={null}
    $ python number_masking.py
    ```

    You should see your basic server application in action at [http://localhost:5000/handleincoming/](http://localhost:5000/handleincoming/).

    [Set up ngrok](/sdk/server/set-up-python-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

    Now people can call your Plivo number. If an incoming call to your Plivo number is from one of the customer phone numbers in the customer-agent map — for example, if the caller number is `14156667777` — then Plivo will send the XML response to process the incoming call as below, and you can check the XML document in your browser.

    <Frame>
            <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ngrok_c2a.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=311a77ec6bada079d064bbf183a81ff5" alt="" width="1538" height="418" data-path="images/ngrok_c2a.png" />
    </Frame>

    If the incoming call to your Plivo number is from one of the agent phone numbers in the customer-agent map — for example, if the caller number is `14156667778` — then Plivo will send the XML response to process the incoming call as below, and you can check the XML document in your browser.

    <Frame>
            <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ngrok_a2c.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=9dc67f44fa072efd286b8f9da8d3882f" alt="" width="1562" height="378" data-path="images/ngrok_a2c.png" />
    </Frame>

    ## Create a Plivo application

    Associate the Flask application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

    Give your application a name — we called ours `Number Masking`. Enter the server URL you want to use (for example, https\://\<ngrok\_identifier>.ngrok.io/handleincoming/) in the `Answer URL` field and set the method as `GET`.  Click **Create Application** to save your application.

    <Frame>
            <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_masking.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=cf592df075798ef478707538f45c4075" alt="" width="1439" height="821" data-path="images/create_masking.png" />
    </Frame>

    ## Assign a Plivo number to your application

    Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

    From the Application Type drop-down, select `XML Application`.

    From the Plivo Application drop-down, select `Number Masking` (the name we gave the application).

    Click **Update Number** to save.

    <Frame>
            <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_masking.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=427b5db48eb7204267e6a9cda90bbf53" alt="" width="2762" height="1578" data-path="images/assign_masking.png" />
    </Frame>

    ## Test

    To test the application, you need two Plivo numbers. Set up one of your numbers as a customer and another as an agent in the customer-to-agent mapping data in the config file. Make a call from each of your mobile numbers to the Plivo number you mapped to the application. You should see that the call is forwarded to the other number, and that the incoming call has the Plivo number as the caller ID.
  </Tab>

  <Tab title="PHP">
    ## Overview

    Phone number masking hides the phone numbers of parties in a call from each other. Many businesses find it advantageous to anonymize communication between two parties — for example, between a customer and a delivery agent on a food delivery service platform or a driver and a rider using a ride-hailing application. Businesses can implement phone number masking by sending calls through an intermediate phone number that acts as a proxy between the two parties. A Plivo number can serve as the intermediate number to connect the two parties while keeping their contact information private.

    ## How it works

    <Tabs>
      <Tab title="Customer calls agent">
        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/customer-calls-agent.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=90ed32982a971c334a1241cb00056274" alt="" width="1446" height="774" data-path="images/customer-calls-agent.png" />
        </Frame>
      </Tab>

      <Tab title="Agent calls customer">
        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/agent-calls-customer.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=08b157996f03f2c61b2e920017ad594f" alt="" width="1446" height="774" data-path="images/agent-calls-customer.png" />
        </Frame>
      </Tab>
    </Tabs>

    As an example, we’ll build a number-masking application for a food delivery service that lets the company connect customers with delivery agents and vice versa without revealing any actual phone numbers. To do this, you

    1. Create a customer-to-agent phone number mapping in your application’s back end.
    2. Create the number masking application using Plivo.
    3. Assign the number masking application to a Plivo number.

    ## Prerequisites

    To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

    ## Create a 1:1 map with actual numbers

    Create customer-to-agent phone number mapping for the application. Whenever a customer places an order, their phone number should be stored in a database for your application to access. A delivery agent will be assigned for the order, and the agent’s number will also be stored in your database, and will be mapped to the customer's number:

    ```
    Customer’s Number		<->		Agent’s Number
    1-415-666-7777					1-415-666-7778
    ```

    We created sample mapping data in a config/app.php file:

    ```php  theme={null}
        'customer_agent_map' => [
            '14156667777' => '14156667778',
            '14156667779' => '14156667780',
            '14156667781' => '14156667782',
        ],
    ```

    ## Create a Laravel controller for number masking

    Change to the project directory and run this command to create a Laravel controller for inbound calls.

    ```shell  theme={null}
    $ php artisan make:controller MaskingController
    ```

    This command generates a controller named MaskingController in the app/http/controllers/ directory. Edit the app/http/controllers/MaskingController.php file and paste into it this code:

    ```php  theme={null}
    <?php

    namespace App\Http\Controllers;
    require '../../vendor/autoload.php';
    use Plivo\RestClient;
    use Plivo\XML\Response;
    use Illuminate\Http\Request;
    use Illuminate\Support\Facades\Log;
    use Config;

    class MaskingController extends Controller
    {
        // Handle incoming calls to a Plivo number, connect agent with customer and vice versa without revealing their actual phone numbers. 
        public function numberMasking(Request $request)
        {
            $from_number = $_REQUEST['From'];
            $to_number = $_REQUEST['To'];
            $response = new Response();
            $customerPhoneMaping = Config::get('app.customer_agent_map');
            $customer_to_agent = array_key_exists($from_number, $customerPhoneMaping); // Check whether the customer's number is in the customer-agent mapping
            $agent_to_customer = array_key_exists($from_number, array_flip($customerPhoneMaping)); // Check whether the agent's number is in the customer-agent mapping
            if ($customer_to_agent == true){
                $number = $customerPhoneMaping[$from_number]; // Assign the value from the customer-agent array to $number variable
                $params = array(
                    'callerId' => $to_number, // Plivo number is used as the caller ID for the call toward the agent
                );
                $dial = $response->addDial($params);
                $dial->addNumber($number);
            } elseif ($agent_to_customer == true){
                $number = array_search($from_number, $customerPhoneMaping); // Assign the key from the customer-agent array to $number variable
                $params = array(
                    'callerId' => $to_number, // Plivo number is used as the caller ID for the call toward the customer
                );
                $dial = $response->addDial($params);
                $dial->addNumber($number);
            }
            $xml_response = $response->toXML(); 
            return response($xml_response, 200)->header('Content-Type', 'application/xml');
        }
    }
    ```

    ### Add a route

    To add a route for the functions in the MaskingController class, edit the routes/web.php file and add this line at the end of the file:

    ```shell  theme={null}
    Route::match(['get', 'post'], '/numbermasking', 'App\Http\Controllers\MaskingController@numberMasking');
    ```

    <Note>
      <strong>Note:</strong> You can edit the app/Http/Middleware/VerifyCsrfToken.php file and add the route of the app numbermasking to the “except” array to disable CSRF verification.
    </Note>

    Run this command to start the Laravel server to forward incoming calls.

    ```shell  theme={null}
    $ php artisan serve
    ```

    You should see the Laravel controller in action on [http://localhost:8000/numbermasking/](http://localhost:8000/numbermasking/).

    [Set up ngrok](/sdk/server/set-up-php-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

    Now people can call your Plivo number. If an incoming call to your Plivo number is from one of the customer phone numbers in the customer-agent map — for example, if the caller number is `14156667777` — then Plivo will send the XML response to process the incoming call as below, and you can check the XML document in your browser.

    <Frame>
            <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ngrok_c2a-php.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=3b3a736581b904c867d8e55900ad7743" alt="" width="1558" height="470" data-path="images/ngrok_c2a-php.png" />
    </Frame>

    If the incoming call to your Plivo number is from one of the agent phone numbers in the customer-agent map — for example, if the caller number is `14156667778` — then Plivo will send the XML response to process the incoming call as below, and you can check the XML document in your browser.

    <Frame>
            <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ngrok_a2c-php.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=16996c8cf97aa206061d63c7c6f601bc" alt="" width="1584" height="410" data-path="images/ngrok_a2c-php.png" />
    </Frame>

    ## Create a Plivo application

    Associate the Laravel controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

    Give your application a name — we called ours `Number Masking`. Enter the server URL you want to use (for example, https\://\<ngrok\_identifier>.ngrok.io/handleincoming/) in the `Answer URL` field and set the method as `GET`.  Click **Create Application** to save your application.

    <Frame>
            <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_masking.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=cf592df075798ef478707538f45c4075" alt="" width="1439" height="821" data-path="images/create_masking.png" />
    </Frame>

    ## Assign a Plivo number to your application

    Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

    From the Application Type drop-down, select `XML Application`.

    From the Plivo Application drop-down, select `Number Masking` (the name we gave the application).

    Click **Update Number** to save.

    <Frame>
            <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_masking.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=427b5db48eb7204267e6a9cda90bbf53" alt="" width="2762" height="1578" data-path="images/assign_masking.png" />
    </Frame>

    ## Test

    To test the application, you need two Plivo numbers. Set up one of your numbers as a customer and another as an agent in the customer-to-agent mapping data in the config file. Make a call from each of your mobile numbers to the Plivo number you mapped to the application. You should see that the call is forwarded to the other number, and that the incoming call has the Plivo number as the caller ID.
  </Tab>

  <Tab title=".NET">
    ## Overview

    Phone number masking hides the phone numbers of parties in a call from each other. Many businesses find it advantageous to anonymize communication between two parties — for example, between a customer and a delivery agent on a food delivery service platform or a driver and a rider using a ride-hailing application. Businesses can implement phone number masking by sending calls through an intermediate phone number that acts as a proxy between the two parties. A Plivo number can serve as the intermediate number to connect the two parties while keeping their contact information private.

    ## How it works

    <Tabs>
      <Tab title="Customer calls agent">
        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/customer-calls-agent.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=90ed32982a971c334a1241cb00056274" alt="" width="1446" height="774" data-path="images/customer-calls-agent.png" />
        </Frame>
      </Tab>

      <Tab title="Agent calls customer">
        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/agent-calls-customer.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=08b157996f03f2c61b2e920017ad594f" alt="" width="1446" height="774" data-path="images/agent-calls-customer.png" />
        </Frame>
      </Tab>
    </Tabs>

    As an example, we’ll build a number-masking application for a food delivery service that lets the company connect customers with delivery agents and vice versa without revealing any actual phone numbers. To do this, you

    1. Create a customer-to-agent phone number mapping in your application’s back end.
    2. Create the number masking application using Plivo.
    3. Assign the number masking application to a Plivo number.

    ## Prerequisites

    To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

    ## Create a 1:1 map with actual numbers

    Create customer-to-agent phone number mapping for the application. Whenever a customer places an order, their phone number should be stored in a database for your application to access. A delivery agent will be assigned for the order, and the agent’s number will also be stored in your database, and will be mapped to the customer's number:

    ```
    Customer’s Number		<->		Agent’s Number
    1-415-666-7777					1-415-666-7778
    ```

    We created an App.config file with sample mapping data for this project:

    ```xml  theme={null}
    <?xml version="1.0" encoding="UTF-8" ?>
    <configuration>
        <configSections>
            <section
                    name="CustomerAgent"
                    type="System.Configuration.DictionarySectionHandler" />
        </configSections>
        <CustomerAgent>
            <add key="14156667777" value="14156667778" />
            <add key="14156667779" value="14156667780" />
            <add key="14156667781" value="14156667782" />
        </CustomerAgent>
    </configuration>
    ```

    ## Create an MVC controller for number masking

    In Visual Studio, navigate to the Controllers directory in the NumberMasking application. Create a controller named `HandleIncomingController.cs` and paste into it this code:

    <Frame>
            <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_controller-mask.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=7d727ad55a80252b8b40591cfc3d0af3" alt="" width="2760" height="1746" data-path="images/create_controller-mask.png" />
    </Frame>

    ```cs  theme={null}
    using System.Configuration;
    using Plivo.XML;
    using System.Collections.Generic;
    using System.Linq;
    using Microsoft.AspNetCore.Mvc;
    using System.Diagnostics;
    using System.Collections;

    // Handle incoming calls to a Plivo number, connect agent with customer and vice versa without revealing their actual phone numbers. 

    namespace NumberMasking.Controllers
    {
        public class HandleIncomingController : Controller
        {

            // GET: /<controller>/
            public IActionResult Index()
            {
                string FromNumber = Request.Query["From"];
                string ToNumber = Request.Query["To"];
                var resp = new Response();
        
                // Customer-agent mapping
                var CustomerAgentMap = (ConfigurationManager.GetSection("CustomerAgent") as Hashtable)
                     .Cast<DictionaryEntry>()
                     .ToDictionary(n => n.Key.ToString(), n => n.Value.ToString());
        
                // Agent-customer mapping
                var AgentCustomerMap = CustomerAgentMap.ToDictionary(kp => kp.Value, kp => kp.Key);
        
                if (CustomerAgentMap.ContainsKey(FromNumber)) // Check whether the customer's number is in the customer-agent mapping
                {
                    var DestNumber = CustomerAgentMap[FromNumber]; // Assign the value from the customer-agent array to number variable
        
                    Dial dial = new Dial(new
                        Dictionary<string, string>() {
                        {"callerId", ToNumber} // Plivo number is used as the caller ID for the call toward the agent
                    });
                    dial.AddNumber(DestNumber,
                        new Dictionary<string, string>() { });
                    resp.Add(dial);
                }
                else if (AgentCustomerMap.ContainsKey(FromNumber)) // Check whether the agent's number is in the customer-agent mapping
                {
                    var DestNumber = AgentCustomerMap[FromNumber]; // Assign the key from the customer-agent array to number variable
                    Dial dial = new Dial(new
                        Dictionary<string, string>() {
                        {"callerId", ToNumber} // Plivo number is used as the caller ID for the call toward the customer
                    });
                    dial.AddNumber(DestNumber,
                        new Dictionary<string, string>() { });
                    resp.Add(dial);
                }
                Debug.WriteLine(resp.ToString());
                var output = resp.ToString();
                return this.Content(output, "text/xml");
            }
        
        }
    }
    ```

    Before you start the application, edit the Properties/launchSettings.json file and set the `applicationUrl`:

    ```json  theme={null}
    "applicationUrl": "http://localhost:5000/"
    ```

    Run the project and you should see your basic server application in action at [http://localhost:5000/handleincoming/](http://localhost:5000/handleincoming/).

    [Set up ngrok](/sdk/server/set-up-dotnet-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

    Now people can call your Plivo number. If an incoming call to your Plivo number is from one of the customer phone numbers in the customer-agent map — for example, if the caller number is `14156667777` — then Plivo will send the XML response to process the incoming call as below, and you can check the XML document in your browser.

    <Frame>
            <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ngrok_c2a.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=311a77ec6bada079d064bbf183a81ff5" alt="" width="1538" height="418" data-path="images/ngrok_c2a.png" />
    </Frame>

    If the incoming call to your Plivo number is from one of the agent phone numbers in the customer-agent map — for example, if the caller number is `14156667778` — then Plivo will send the XML response to process the incoming call as below, and you can check the XML document in your browser.

    <Frame>
            <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ngrok_a2c.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=9dc67f44fa072efd286b8f9da8d3882f" alt="" width="1562" height="378" data-path="images/ngrok_a2c.png" />
    </Frame>

    ## Create a Plivo application

    Associate the MVC controller you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

    Give your application a name — we called ours `Number Masking`. Enter the server URL you want to use (for example, https\://\<ngrok\_identifier>.ngrok.io/handleincoming/) in the `Answer URL` field and set the method as `GET`.  Click **Create Application** to save your application.

    <Frame>
            <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_masking.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=cf592df075798ef478707538f45c4075" alt="" width="1439" height="821" data-path="images/create_masking.png" />
    </Frame>

    ## Assign a Plivo number to your application

    Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

    From the Application Type drop-down, select `XML Application`.

    From the Plivo Application drop-down, select `Number Masking` (the name we gave the application).

    Click **Update Number** to save.

    <Frame>
            <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_masking.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=427b5db48eb7204267e6a9cda90bbf53" alt="" width="2762" height="1578" data-path="images/assign_masking.png" />
    </Frame>

    ## Test

    To test the application, you need two Plivo numbers. Set up one of your numbers as a customer and another as an agent in the customer-to-agent mapping data in the config file. Make a call from each of your mobile numbers to the Plivo number you mapped to the application. You should see that the call is forwarded to the other number, and that the incoming call has the Plivo number as the caller ID.
  </Tab>

  <Tab title="Java">
    ## Overview

    Phone number masking hides the phone numbers of parties in a call from each other. Many businesses find it advantageous to anonymize communication between two parties — for example, between a customer and a delivery agent on a food delivery service platform or a driver and a rider using a ride-hailing application. Businesses can implement phone number masking by sending calls through an intermediate phone number that acts as a proxy between the two parties. A Plivo number can serve as the intermediate number to connect the two parties while keeping their contact information private.

    ## How it works

    <Tabs>
      <Tab title="Customer calls agent">
        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/customer-calls-agent.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=90ed32982a971c334a1241cb00056274" alt="" width="1446" height="774" data-path="images/customer-calls-agent.png" />
        </Frame>
      </Tab>

      <Tab title="Agent calls customer">
        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/agent-calls-customer.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=08b157996f03f2c61b2e920017ad594f" alt="" width="1446" height="774" data-path="images/agent-calls-customer.png" />
        </Frame>
      </Tab>
    </Tabs>

    As an example, we’ll build a number-masking application for a food delivery service that lets the company connect customers with delivery agents and vice versa without revealing any actual phone numbers. To do this, you

    1. Create a customer-to-agent phone number mapping in your application’s back end.
    2. Create the number masking application using Plivo.
    3. Assign the number masking application to a Plivo number.

    ## Prerequisites

    To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

    ## Create a 1:1 map with actual numbers

    Create customer-to-agent phone number mapping for the application. Whenever a customer places an order, their phone number should be stored in a database for your application to access. A delivery agent will be assigned for the order, and the agent’s number will also be stored in your database, and will be mapped to the customer's number:

    ```
    Customer's Number		<->		Agent's Number
    1-415-666-7777					1-415-666-7778
    ```

    We created sample mapping data in the src/main/resources/application.properties file:

    ```json  theme={null}
    spring.main.banner-mode=off
    spring.output.ansi.enabled=ALWAYS
    logging.pattern.console=%clr(%d{yy-MM-dd E HH:mm:ss.SSS}){blue} %clr(%-5p) %clr(%logger{0}){blue} %clr(%m){faint}%n

    number.map={"14156667777":"14156667778", "14156667779":"14156667780", "14156667781":"14156667782"}
    ```

    ## Create a Spring application for number masking

    Open the NumberMaskingApplication.java file in the src/main/java/com.example.NumberMasking/ folder and paste into it this code.

    <Note>
      <strong>Note:</strong> Here, the demo application name is NumberMaskingApplication.java because the friendly name we provided in Spring Initializr was `NumberMasking`.
    </Note>

    ```java  theme={null}
    package com.example.NumberMasking;

    import com.plivo.api.exceptions.PlivoXmlException;
    import com.plivo.api.xml.Dial;
    import com.plivo.api.xml.Response;
    import com.plivo.api.xml.Number;
    import org.springframework.beans.factory.annotation.Value;
    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.web.bind.annotation.*;
    import com.google.common.collect.HashBiMap;
    import java.util.Map;

    @SpringBootApplication
    @RestController
    public class NumberMaskingApplication {

    	@Value("#{${number.map}}")
    	Map<String, String> CustomerAgentMap;
    	
    	public static void main(String[] args) {
    		SpringApplication.run(NumberMaskingApplication.class, args);
    	}
    	
    	// Handle incoming calls to a Plivo number, connect agent with customer and vice versa without revealing their actual phone numbers.
    	@RequestMapping(value = "/number_masking/", produces = { "application/xml" }, method = { RequestMethod.GET, RequestMethod.POST })
    	public Response HandleIncoming(@RequestParam("From") String FromNumber, @RequestParam("To") String ToNumber)
    			throws PlivoXmlException {
    		Map<String, String> AgentCustomerMap = HashBiMap.create(CustomerAgentMap).inverse();
    		Response response = new Response();
    		if(CustomerAgentMap.containsKey(FromNumber)) { // Check whether the customer's number is in the customer-agent mapping
    			var DestNumber =  CustomerAgentMap.get(FromNumber); // Assign the value from the customer-agent map to DestNumber variable
    			response.children(new Dial()
    					.callerId(ToNumber) // Plivo number is used as the caller ID for the call toward the agent
    					.children(new Number(DestNumber)));
    		}
    		else if (AgentCustomerMap.containsKey(FromNumber)) { // Check whether the agent's number is in the customer-agent mapping
    			var DestNumber =  AgentCustomerMap.get(FromNumber); // Assign the Kky from the customer-agent map to DestNumber variable
    			response.children(new Dial()
    					.callerId(ToNumber) // Plivo number is used as the caller ID for the call toward the customer
    					.children(new Number(DestNumber)));
    		}
    		System.out.println(response.toXmlString());
    		return response;
    	}
    }
    ```

    Save the file and run it.

    <Frame>
            <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/run-mask.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=6eece6ac0bbf8564a68de00446466f40" alt="" width="2756" height="1740" data-path="images/run-mask.png" />
    </Frame>

    You should see your basic server application in action at [http://localhost:8080/number\_masking/](http://localhost:8080/number_masking/).

    [Set up ngrok](/sdk/server/set-up-java-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

    Now people can call your Plivo number. If an incoming call to your Plivo number is from one of the customer phone numbers in the customer-agent map — for example, if the caller number is `14156667777` — then Plivo will send the XML response to process the incoming call as below, and you can check the XML document in your browser.

    <Frame>
            <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ngrok_c2a-go.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=6a1ff52a88a35f915eb0da542b110948" alt="" width="1590" height="410" data-path="images/ngrok_c2a-go.png" />
    </Frame>

    If the incoming call to your Plivo number is from one of the agent phone numbers in the customer-agent map — for example, if the caller number is `14156667778` — then Plivo will send the XML response to process the incoming call as below, and you can check the XML document in your browser.

    <Frame>
            <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ngrok_a2c-go.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=28f10568606c9dab307c75865b3f63fd" alt="" width="1606" height="374" data-path="images/ngrok_a2c-go.png" />
    </Frame>

    ## Create a Plivo application

    Associate the Spring application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

    Give your application a name — we called ours `Number Masking`. Enter the server URL you want to use (for example, https\://\<ngrok\_identifier>.ngrok.io/handleincoming/) in the `Answer URL` field and set the method as `GET`.  Click **Create Application** to save your application.

    <Frame>
            <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_masking.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=cf592df075798ef478707538f45c4075" alt="" width="1439" height="821" data-path="images/create_masking.png" />
    </Frame>

    ## Assign a Plivo number to your application

    Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

    From the Application Type drop-down, select `XML Application`.

    From the Plivo Application drop-down, select `Number Masking` (the name we gave the application).

    Click **Update Number** to save.

    <Frame>
            <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_masking.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=427b5db48eb7204267e6a9cda90bbf53" alt="" width="2762" height="1578" data-path="images/assign_masking.png" />
    </Frame>

    ## Test

    To test the application, you need two Plivo numbers. Set up one of your numbers as a customer and another as an agent in the customer-to-agent mapping data in the config file. Make a call from each of your mobile numbers to the Plivo number you mapped to the application. You should see that the call is forwarded to the other number, and that the incoming call has the Plivo number as the caller ID.
  </Tab>

  <Tab title="Go">
    ## Overview

    Phone number masking hides the phone numbers of parties in a call from each other. Many businesses find it advantageous to anonymize communication between two parties — for example, between a customer and a delivery agent on a food delivery service platform or a driver and a rider using a ride-hailing application. Businesses can implement phone number masking by sending calls through an intermediate phone number that acts as a proxy between the two parties. A Plivo number can serve as the intermediate number to connect the two parties while keeping their contact information private.

    ## How it works

    <Tabs>
      <Tab title="Customer calls agent">
        <Frame>
                    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/customer-calls-agent.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=90ed32982a971c334a1241cb00056274" alt="" width="1446" height="774" data-path="images/customer-calls-agent.png" />
        </Frame>
      </Tab>

      <Tab title="Agent calls customer">
        <Frame>
                    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/agent-calls-customer.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=08b157996f03f2c61b2e920017ad594f" alt="" width="1446" height="774" data-path="images/agent-calls-customer.png" />
        </Frame>
      </Tab>
    </Tabs>

    As an example, we’ll build a number-masking application for a food delivery service that lets the company connect customers with delivery agents and vice versa without revealing any actual phone numbers. To do this, you

    1. Create a customer-to-agent phone number mapping in your application’s back end.
    2. Create the number masking application using Plivo.
    3. Assign the number masking application to a Plivo number.

    ## Prerequisites

    To get started, you need a Plivo account —  [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the [Numbers API](/numbers/). If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-xml-voice/) and a web server and safely expose that server to the internet.

    ## Create a 1:1 map with actual numbers

    Create customer-to-agent phone number mapping for the application. Whenever a customer places an order, their phone number should be stored in a database for your application to access. A delivery agent will be assigned for the order, and the agent’s number will also be stored in your database, and will be mapped to the customer's number:

    ```
    Customer’s Number		<->		Agent’s Number
    1-415-666-7777					1-415-666-7778
    ```

    We created sample mapping data in a .env file:

    ```sh  theme={null}
    json
    BASEMAP = {"14156667777":"14156667778","14156667779":"14156667780","14156667781":"14156667782"}
    ```

    ## Create a Go server for number masking

    Create a file called `masking.go` and paste into it this code.

    ```go  theme={null}
    package main

    import (
    	"encoding/json"
    	"log"
    	"os"

    	"github.com/gin-gonic/gin"
    	"github.com/joho/godotenv"
    	"github.com/plivo/plivo-go/v7/xml"
    )

    // init gets called before the main function
    func init() {
    	// Log error if .env file does not exist
    	err := godotenv.Load(".env")
    	if err != nil {
    		log.Fatal("Error loading .env file")
    	}
    }

    // Handle incoming calls to a Plivo number, connect agent with customer and vice versa without revealing their actual phone numbers.
    func main() {
    	r := gin.Default()
    	r.GET("/number_masking", func(c *gin.Context) {
    		customerAgentmap := os.Getenv("BASEMAP")
    		// Declares an empty map interface
    		var result map[string]string
    		fromNumber := c.Query("From")
    		toNumber := c.Query("To")
    		// Unmarshal or Decode the JSON to the interface.
    		json.Unmarshal([]byte(customerAgentmap), &result)
    		agentCustomermap := reverseMap(result)
    		_, custToagent := result[fromNumber]
    		_, agenTocust := agentCustomermap[fromNumber]
    		if custToagent { // Check whether the customer's number is in the customer-agent mapping
    			destNumber := result[fromNumber] // Assign the value from the customer-agent array to number variable
    			c.XML(200, xml.ResponseElement{
    				Contents: []interface{}{
    					new(xml.DialElement).
    						SetCallerID(toNumber). // Plivo number is used as the caller ID for the call toward the agent
    						SetContents([]interface{}{
    							new(xml.NumberElement).
    								SetContents(destNumber),
    						}),
    				},
    			})
    		} else if agenTocust { // Check whether the agent's number is in the customer-agent mapping
    			destNumber := agentCustomermap[fromNumber] // Assign the key from the customer-agent array to number variable
    			c.XML(200, xml.ResponseElement{
    				Contents: []interface{}{
    					new(xml.DialElement).
    						SetCallerID(toNumber). // Plivo number is used as the caller ID for the call toward the customer
    						SetContents([]interface{}{
    							new(xml.NumberElement).
    								SetContents(destNumber),
    						}),
    				},
    			})
    		}
    		c.Header("Content-Type", "application/xml")
    	})
    	r.Run() // listen and serve on 0.0.0.0:8080 (for Windows "localhost:8080")
    }

    // Reverse the Basemap from env file to get customer-agent mapping data
    func reverseMap(m map[string]string) map[string]string {
    	n := make(map[string]string)
    	for k, v := range m {
    		n[v] = k
    	}
    	return n
    }
    ```

    Save the file and run it.

    ```shell  theme={null}
    $ go run masking.go
    ```

    You should see your basic server application in action on [http://localhost:8080/number\_masking/](http://localhost:8080/number_masking/).

    [Set up ngrok](/sdk/server/set-up-go-dev-environment-api-xml-voice/#ngrok-setup) to expose your local server to the internet.

    Now people can call your Plivo number. If an incoming call to your Plivo number is from one of the customer phone numbers in the customer-agent map — for example, if the caller number is `14156667777` — then Plivo will send the XML response to process the incoming call as below, and you can check the XML document in your browser.

    <Frame>
            <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ngrok_c2a-go.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=6a1ff52a88a35f915eb0da542b110948" alt="" width="1590" height="410" data-path="images/ngrok_c2a-go.png" />
    </Frame>

    If the incoming call to your Plivo number is from one of the agent phone numbers in the customer-agent map — for example, if the caller number is `14156667778` — then Plivo will send the XML response to process the incoming call as below, and you can check the XML document in your browser.

    <Frame>
            <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/ngrok_a2c-go.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=28f10568606c9dab307c75865b3f63fd" alt="" width="1606" height="374" data-path="images/ngrok_a2c-go.png" />
    </Frame>

    ## Create a Plivo application

    Associate the Go application you created with Plivo by creating a Plivo application. Visit Voice > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click on **Add New Application**, or use Plivo’s [Application API](/account/api/application/#create-an-application).

    Give your application a name — we called ours `Number Masking`. Enter the server URL you want to use (for example, https\://\<ngrok\_identifier>.ngrok.io/handleincoming/) in the `Answer URL` field and set the method as `GET`.  Click **Create Application** to save your application.

    <Frame>
            <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_masking.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=cf592df075798ef478707538f45c4075" alt="" width="1439" height="821" data-path="images/create_masking.png" />
    </Frame>

    ## Assign a Plivo number to your application

    Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use for this application.

    From the Application Type drop-down, select `XML Application`.

    From the Plivo Application drop-down, select `Number Masking` (the name we gave the application).

    Click **Update Number** to save.

    <Frame>
            <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_masking.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=427b5db48eb7204267e6a9cda90bbf53" alt="" width="2762" height="1578" data-path="images/assign_masking.png" />
    </Frame>

    ## Test

    To test the application, you need two Plivo numbers. Set up one of your numbers as a customer and another as an agent in the customer-to-agent mapping data in the config file. Make a call from each of your mobile numbers to the Plivo number you mapped to the application. You should see that the call is forwarded to the other number, and that the incoming call has the Plivo number as the caller ID.
  </Tab>
</Tabs>
