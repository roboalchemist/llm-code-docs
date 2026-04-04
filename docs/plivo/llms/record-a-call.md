# Source: https://plivo.com/docs/voice/use-cases/record-a-call.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Record Calls

> Record voice calls and store recordings using the Plivo Voice API

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to initiating call recordings for outbound API calls, Dial XML-connected calls, and conference calls. You can record inbound calls to a Plivo number too when the application associated with the number returns an XML document with a Dial and a Record element.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the Numbers API. If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-phlo/) and a web server and safely expose that server to the internet.

    ## Record a complete outbound call using XML

    You can record a complete call session using the [Record XML](/voice/xml/record/) element in conjunction with a [Dial](/voice/xml/dial/) element response that’s returned by an answer URL. Recording a complete call is useful in applications such as virtual voicemail boxes and automated speech surveys.

    The XML might look like this:

    ```xml  theme={null}
    <Response>
     <Record action="https://<yourdomain>.com/get_recording/" startOnDialAnswer="true" redirect="false" maxLength="3600" />
     <Dial>
      <Number>12025551234</Number>
     </Dial>
    </Response>
    ```

    When the number specified in the Dial XML element answers the call, Plivo records the complete call session. Recording details are sent to the action URL as soon as the recording starts. You can use the attributes available in the Record XML element to control the recording behavior.

    Create a file called `record_call.js` and paste into it this code.

    ```js  theme={null}
    var plivo = require('plivo');

    var response = plivo.Response();

    var params = {
    	'action': "https://<yourdomain>.com/get_recording/",
    	'startOnDialAnswer': "true",
    	'redirect': "false"
    };
    response.addRecord(params);

    var dial = response.addDial();
    var number = "<phone_number>";
    dial.addNumber(number);

    console.log(response.toXML());
    ```

    Replace the phone number placeholder with an actual phone number (for example, 12025551234).

    ## Record a complete conference call using XML

    You can record a complete conference call initiated using a [Conference XML](/voice/xml/conference/) element by using an XML response like this:

    ```xml  theme={null}
    <Response>
      <Conference callbackUrl="https://<yourdomain>.com/confevents/" callbackMethod="POST" record="true" recordFileFormat="wav">My Room</Conference>
    </Response>
    ```

    Plivo will record the complete audio of a conference call connected via this XML document. Recording details are sent to the action URL and callback URL as soon as the recording starts. The parameter `ConferenceAction=record` is also sent to the callback URL when the recording starts.

    Create a file called `record_call.js` and paste into it this code.

    ```js  theme={null}
    var plivo = require('plivo');

    var response = plivo.Response();

    var params = {
    	'record': "true",
    	'callbackUrl': "<yourdomain>.com/confevents/",
        'callbackMethod': "POST",
    	'waitSound': "<yourdomain>.com/waitmusic/"
    };
    var conference_name = "<conference_room_name>";
    response.addConference(conference_name, params);

    console.log(response.toXML());
    ```

    ## Start and stop call recording using APIs

    You can start and stop voice recordings for outbound API calls, Dial XML-connected calls, and conference calls using the Record API and Record Conference API.

    ### Record API

    To start recording using the Record API, you must use the CallUUID of the particular call that you want to record.

    ### Retrieve a CallUUID

    You can get the CallUUID of a call connected via the Outbound API and Dial XML from any of these arguments:

    * ring\_url: Plivo sends a webhook callback to the ring URL used in the call API request as soon as the destination number starts ringing.
    * answer\_url: Plivo sends a webhook callback to the answer URL when the destination number answers the call.
    * fallback\_url: If you define the fallback URL argument in the API request or the application attached to the Plivo number, and if the application server defined in the answer URL is unavailable, then Plivo will try to retrieve the XML document from the fallback URL to process the call. At that time Plivo will send a webhook callback to the fallback URL.
    * callback\_url: If you use the callbackUrl parameter in the Dial XML, Plivo will send a callback to the web server configured in callback URL when the number specified in the Dial XML element answers the call.

    ### Start recording

    Once you have the CallUUID of the call you want to record, you can call the record API and specify the CallUUID in the payload.

    For example, if you want to record an outbound API call, you can use the code below to record the call once the destination number answers the call. The recording will stop automatically once the call is completed.

    Create a file called `record_call.js` and paste into it this code.

    ```js  theme={null}
    var util = require('util');
    var express = require('express');
    var app = express();
    var plivo = require('plivo');

    app.set('port', (process.env.PORT || 5000));

    app.all('/record/', function (req, res) {
    	var r = plivo.Response();
    	var getinput_action_url, params, getDigits;
    	getinput_action_url = req.protocol + '://' + req.headers.host + '/record/action/';
    	params = {
    		'action': getinput_action_url,
    		'method': 'POST',
    		'inputType': 'dtmf',
    		'digitEndTimeout': '5',
    		'redirect': 'true',
    	};
    	get_input = r.addGetInput(params);
    	get_input.addSpeak("Press 1 to record this call");

    	console.log(r.toXML());
    	res.set({ 'Content-Type': 'text/xml' });
    	res.send(r.toXML());
    });

    app.all('/record/action/', function (req, res) {
    	var digit = req.param('Digits');
    	var call_uuid = req.param('CallUUID');
    	console.log("call_uuid is:",call_uuid + "and digit is:",digit)

    	var client = new plivo.Client("<auth_id>", "<auth_token>");
    	
    	if (digit === "1") {
    		var response = client.calls.record(
    			call_uuid, 
    		)
    		console.log(response);
    	} else
    		console.log("Wrong Input");
    });

    app.listen(app.get('port'), function () {
    	console.log('Node app is running on port', app.get('port'));
    });
    ```

    Replace the auth placeholders with your authentication credentials from the Plivo console.

    ### Stop recording

    You can stop recording a call by using the CallUUID — see our [API reference documentation](/voice/api/call/record-calls/#stop-recording-a-call).

    ## Start and stop conference call recording using APIs

    ### Record Conference API

    To start recording conference calls using the Record Conference API, use the name of the conference you want to record. If you want to start recording a conference call once a participant has entered the conference room, you can use this code.

    Create a file called `record_call.js` and paste into it this code.

    ```js  theme={null}

    var plivo = require('plivo');

    (function main() {
    	'use strict';

    	var client = new plivo.Client("<auth_id>","<auth_token>");
    	client.conferences.record(
    		"<conference_room_name>",
    	).then(function (response) {
    		console.log(response);
    	}, function (err) {
    		console.error(err);
    	});
    })();
    ```

    Replace the auth placeholders with your authentication credentials from the Plivo console.

    ### Stop recording

    You can stop recording a conference call by using the conference name — see our [API reference documentation](/voice/api/conference/record-conference/#stop-recording-a-conference).

    ## Recording features

    * **File formats**: You can choose the recording file format (WAV or MP3) by using the `file_format` attribute for the Record API and Record Conference API, `recordFileFormat` for the Conference XML element, and `fileFormat` for the Record XML element.
    * **Channels**: Plivo makes mono recordings of conference calls and stereo recordings of regular calls.
    * **Recording length**: You can set the maximum duration of a recording by using arguments and attributes such as `time_limit` for the Record API and `maxLength` for the Record XML element.

    ## Managing recordings

    * **Fetching recording details**: You can store and retrieve the recording details of the voice calls and conference calls using the HTTP callbacks received on the action and callback URLs. You can also fetch recording details from the Voice >[ Recordings](https://cx.plivo.com/logs) page of the Plivo console.
    * **Deleting recordings**: You can delete a recording by using the [Delete a Recording API](/voice/api/recording/#list-all-recordings) and specifying a recording ID, which you can retrieve from the HTTP callback details stored in your database. You can also delete recordings from the Voice >[ Recordings](https://cx.plivo.com/logs) page of the Plivo console.

    ## Authentication for recordings

    Recordings hosted on Plivo servers are accessible only via unique, hard to guess, long URLs that Plivo shares in recording callbacks and API responses. By default, we do not enforce authentication on GET recording media requests to allow for easy implementation of use cases that involve playing recordings on a web or mobile front end.

    For enhanced security, we recommend enabling basic authentication for retrieving recording media assets in your Plivo account. You can enable Basic Auth for Recording URLs from the Voice >[ Other Settings](https://cx.plivo.com/home) page of the Plivo console.

    <Note>
      <strong>Note:</strong> Only account admins (users with the role Admin) have the required privileges to update the recording authentication preference setting.
    </Note>
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to initiating call recordings for outbound API calls, Dial XML-connected calls, and conference calls. You can record inbound calls to a Plivo number too when the application associated with the number returns an XML document with a Dial and a Record element.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the Numbers API. If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-phlo/) and a web server and safely expose that server to the internet.

    ## Record a complete outbound call using XML

    You can record a complete call session using the [Record XML](/voice/xml/record/) element in conjunction with a [Dial](/voice/xml/dial/) element response that’s returned by an answer URL. Recording a complete call is useful in applications such as virtual voicemail boxes and automated speech surveys.

    The XML might look like this:

    ```xml  theme={null}
    <Response>
     <Record action="https://<yourdomain>.com/get_recording/" startOnDialAnswer="true" redirect="false" maxLength="3600" />
     <Dial>
      <Number>12025551234</Number>
     </Dial>
    </Response>
    ```

    When the number specified in the Dial XML element answers the call, Plivo records the complete call session. Recording details are sent to the action URL as soon as the recording starts. You can use the attributes available in the Record XML element to control the recording behavior.

    Create a file called `record_call.rb` and paste into it this code.

    ```rb  theme={null}
    require 'rubygems'
    require 'plivo'

    include Plivo::XML
    include Plivo::Exceptions

    begin
    	response = Response.new

    	params = {
    		action: 'https://<yourdomain>.com/get_recording/',
    		startOnDialAnswer: 'true',
    		redirect: 'false'
    	}
    	
    	response.addRecord(params)
    	
    	dial = response.addDial()
    	number = '<phone_number>'
    	dial.addNumber(number)
    	
    	xml = PlivoXML.new(response)
    	puts xml.to_xml
    rescue PlivoXMLError => e
    	puts 'Exception: ' + e.message
    ```

    Replace the phone number placeholder with an actual phone number (for example, 12025551234).

    ## Record a complete conference call using XML

    You can record a complete conference call initiated using a [Conference XML](/voice/xml/conference/) element by using an XML response like this:

    ```xml  theme={null}
    <Response>
      <Conference callbackUrl="https://<yourdomain>.com/confevents/" callbackMethod="POST" record="true" recordFileFormat="wav">My Room</Conference>
    </Response>
    ```

    Plivo will record the complete audio of a conference call connected via this XML document. Recording details are sent to the action URL and callback URL as soon as the recording starts. The parameter `ConferenceAction=record` is also sent to the callback URL when the recording starts.

    Create a file called `record_call.rb` and paste into it this code.

    ```rb  theme={null}
    require 'rubygems'
    require 'plivo'

    include Plivo::XML
    include Plivo::Exceptions

    begin
    	response = Response.new

    	params = {
    		'record' => "true",
    		'callbackUrl' => "https://<yourdomain>.com/confevents/",
    		'callbackMethod' => "POST",
    		'waitSound' => "https:/<yourdomain>.com/waitmusic/"
    	}
    	
    	conference_name = "<conference_room_name>"
    	response.addConference(conference_name, params)
    	
    	xml = PlivoXML.new(response)
    	puts xml.to_xml
    rescue PlivoXMLError => e
    	puts 'Exception: ' + e.message
    end
    ```

    ## Start and stop call recording using APIs

    You can start and stop voice recordings for outbound API calls, Dial XML-connected calls, and conference calls using the Record API and Record Conference API.

    ### Record API

    To start recording using the Record API, you must use the CallUUID of the particular call that you want to record.

    ### Retrieve a CallUUID

    You can get the CallUUID of a call connected via the Outbound API and Dial XML from any of these arguments:

    * ring\_url: Plivo sends a webhook callback to the ring URL used in the call API request as soon as the destination number starts ringing.
    * answer\_url: Plivo sends a webhook callback to the answer URL when the destination number answers the call.
    * fallback\_url: If you define the fallback URL argument in the API request or the application attached to the Plivo number, and if the application server defined in the answer URL is unavailable, then Plivo will try to retrieve the XML document from the fallback URL to process the call. At that time Plivo will send a webhook callback to the fallback URL.
    * callback\_url: If you use the callbackUrl parameter in the Dial XML, Plivo will send a callback to the web server configured in callback URL when the number specified in the Dial XML element answers the call.

    ### Start recording

    Once you have the CallUUID of the call you want to record, you can call the record API and specify the CallUUID in the payload.

    For example, if you want to record an outbound API call, you can use the code below to record the call once the destination number answers the call. The recording will stop automatically once the call is completed.

    Create a file called `record_call.go` and paste into it this code.

    ```rb  theme={null}
    require 'rubygems'
    require 'sinatra'
    require 'plivo'

    include Plivo
    include Plivo::XML

    get '/record_api/' do
    	r = Response.new()

    	getinput_action_url = "https://<yourdomain>.com/record_action/"
    	params = {
    		action: getinput_action_url, 
    		method: 'POST', 
    		digitEndTimeout: '5',
    		inputType:'dtmf',
    		redirect:'true'
    	}
    	getinput = r.addGetInput(params)
    	getinput.addSpeak("Press 1 to record this call")
    	
    	xml = PlivoXML.new(r)
    	content_type "application/xml"
    	return xml.to_s()
    end

    get '/record_api_action/' do
    	digit = params[:Digits]
    	call_uuid = params[:CallUUID]

    	puts "call_uuid is %s and digit is %s" % [call_uuid,digit]

    	api = RestClient.new("<auth_id>","<auth_token>")
    	
    	if (digit == "1")
    		response = api.calls.record(call_uuid)
    		print response
    	else
    		print "Invalid input"
    	end
    ```

    Replace the auth placeholders with your authentication credentials from the Plivo console.

    ### Stop recording

    You can stop recording a call by using the CallUUID — see our [API reference documentation](/voice/api/call/record-calls/#stop-recording-a-call).

    ## Start and stop conference call recording using APIs

    ### Record Conference API

    To start recording conference calls using the Record Conference API, use the name of the conference you want to record. If you want to start recording a conference call once a participant has entered the conference room, you can use this code.

    Create a file called `record_call.go` and paste into it this code.

    ```rb  theme={null}
    require 'rubygems'
    require 'plivo'

    include Plivo
    include Plivo::Exceptions

    api = RestClient.new("<auth_id>","<auth_token>")

    begin
    	response = api.conferences.record(
    		'<conference_room_name>'
    	)
    	puts response
    rescue PlivoRESTError => e
    	puts 'Exception: ' + e.message
    ```

    Replace the auth placeholders with your authentication credentials from the Plivo console.

    ### Stop recording

    You can stop recording a conference call by using the conference name — see our [API reference documentation](/voice/api/conference/record-conference/#stop-recording-a-conference).

    ## Recording features

    * **File formats**: You can choose the recording file format (WAV or MP3) by using the `file_format` attribute for the Record API and Record Conference API, `recordFileFormat` for the Conference XML element, and `fileFormat` for the Record XML element.
    * **Channels**: Plivo makes mono recordings of conference calls and stereo recordings of regular calls.
    * **Recording length**: You can set the maximum duration of a recording by using arguments and attributes such as `time_limit` for the Record API and `maxLength` for the Record XML element.

    ## Managing recordings

    * **Fetching recording details**: You can store and retrieve the recording details of the voice calls and conference calls using the HTTP callbacks received on the action and callback URLs. You can also fetch recording details from the Voice >[ Recordings](https://cx.plivo.com/logs) page of the Plivo console.
    * **Deleting recordings**: You can delete a recording by using the [Delete a Recording API](/voice/api/recording/#list-all-recordings) and specifying a recording ID, which you can retrieve from the HTTP callback details stored in your database. You can also delete recordings from the Voice >[ Recordings](https://cx.plivo.com/logs) page of the Plivo console.

    ## Authentication for recordings

    Recordings hosted on Plivo servers are accessible only via unique, hard to guess, long URLs that Plivo shares in recording callbacks and API responses. By default, we do not enforce authentication on GET recording media requests to allow for easy implementation of use cases that involve playing recordings on a web or mobile front end.

    For enhanced security, we recommend enabling basic authentication for retrieving recording media assets in your Plivo account. You can enable Basic Auth for Recording URLs from the Voice >[ Other Settings](https://cx.plivo.com/home) page of the Plivo console.

    <Note>
      <strong>Note:</strong> Only account admins (users with the role Admin) have the required privileges to update the recording authentication preference setting.
    </Note>
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to initiating call recordings for outbound API calls, Dial XML-connected calls, and conference calls. You can record inbound calls to a Plivo number too when the application associated with the number returns an XML document with a Dial and a Record element.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the Numbers API. If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-phlo/) and a web server and safely expose that server to the internet.

    ## Record a complete outbound call using XML

    You can record a complete call session using the [Record XML](/voice/xml/record/) element in conjunction with a [Dial](/voice/xml/dial/) element response that’s returned by an answer URL. Recording a complete call is useful in applications such as virtual voicemail boxes and automated speech surveys.

    The XML might look like this:

    ```xml  theme={null}
    <Response>
     <Record action="https://<yourdomain>.com/get_recording/" startOnDialAnswer="true" redirect="false" maxLength="3600" />
     <Dial>
      <Number>12025551234</Number>
     </Dial>
    </Response>
    ```

    When the number specified in the Dial XML element answers the call, Plivo records the complete call session. Recording details are sent to the action URL as soon as the recording starts. You can use the attributes available in the Record XML element to control the recording behavior.

    Create a file called `record_call.py` and paste into it this code.

    ```py  theme={null}
    from plivo import plivoxml

    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.RecordElement(
            action='https://<yourdomain>.com/get_recording/',
            start_on_dial_answer=True,
            redirect=False))
    response.add(plivoxml.DialElement().add(plivoxml.NumberElement('<phone_number>')))
    print(response.to_string())
    ```

    Replace the phone number placeholder with an actual phone number (for example, 12025551234).

    ## Record a complete conference call using XML

    You can record a complete conference call initiated using a [Conference XML](/voice/xml/conference/) element by using an XML response like this:

    ```xml  theme={null}
    <Response>
      <Conference callbackUrl="https://<yourdomain>.com/confevents/" callbackMethod="POST" record="true" recordFileFormat="wav">My Room</Conference>
    </Response>
    ```

    Plivo will record the complete audio of a conference call connected via this XML document. Recording details are sent to the action URL and callback URL as soon as the recording starts. The parameter `ConferenceAction=record` is also sent to the callback URL when the recording starts.

    Create a file called `record_call.py` and paste into it this code.

    ```py  theme={null}
    from plivo import plivoxml

    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.ConferenceElement(
            '<conference_room_name>',
            record=True,
            callback_url='https://<yourdomain>.com/confevents/',
            callback_method='POST',
            wait_sound='https://<yourdomain>.com/waitmusic/'))

    print(response.to_string())
    ```

    ## Start and stop call recording using APIs

    You can start and stop voice recordings for outbound API calls, Dial XML-connected calls, and conference calls using the Record API and Record Conference API.

    ### Record API

    To start recording using the Record API, you must use the CallUUID of the particular call that you want to record.

    ### Retrieve a CallUUID

    You can get the CallUUID of a call connected via the Outbound API and Dial XML from any of these arguments:

    * ring\_url: Plivo sends a webhook callback to the ring URL used in the call API request as soon as the destination number starts ringing.
    * answer\_url: Plivo sends a webhook callback to the answer URL when the destination number answers the call.
    * fallback\_url: If you define the fallback URL argument in the API request or the application attached to the Plivo number, and if the application server defined in the answer URL is unavailable, then Plivo will try to retrieve the XML document from the fallback URL to process the call. At that time Plivo will send a webhook callback to the fallback URL.
    * callback\_url: If you use the callbackUrl parameter in the Dial XML, Plivo will send a callback to the web server configured in callback URL when the number specified in the Dial XML element answers the call.

    ### Start recording

    Once you have the CallUUID of the call you want to record, you can call the record API and specify the CallUUID in the payload.

    For example, if you want to record an outbound API call, you can use the code below to record the call once the destination number answers the call. The recording will stop automatically once the call is completed.

    Create a file called `record_call.py` and paste into it this code.

    ```py  theme={null}
    from flask import Flask, Response, request, url_for
    from plivo import plivoxml
    import plivo

    app = Flask(__name__)

    @app.route('/record_api/', methods=['POST', 'GET'])
    def record_api():

        response = plivoxml.ResponseElement()
        response.add(plivoxml.GetInputElement().
                     set_action(url_for('record_action', _external=True)).
                     set_method('POST').
                     set_input_type('dtmf').
                     set_digit_end_timeout(5).
                     set_redirect(True).add(
            plivoxml.SpeakElement('Press 1 to record this call')))
        return Response(response.to_string(), mimetype='application/xml')

    @app.route('/record_api_action/', methods=['POST', 'GET'])
    def record_action():
        digit = request.args.get('Digits')
        call_uuid = request.args.get('CallUUID')
        print("call_uuid is {}, and digit pressed {}".format(call_uuid,digit))

        client = plivo.RestClient("<auth_id>", "<auth_token>")
        if digit == "1":
            response = client.calls.record(
                call_uuid=call_uuid, )
        else:
            print "Invalid input"
            response = "Error"
        return Response(response.to_string(), mimetype='text/plain')


    if __name__ == '__main__':
        app.run(host='0.0.0.0', debug='True')
    ```

    Replace the auth placeholders with your authentication credentials from the Plivo console.

    ### Stop recording

    You can stop recording a call by using the CallUUID — see our [API reference documentation](/voice/api/call/record-calls/#stop-recording-a-call).

    ## Start and stop conference call recording using APIs

    ### Record Conference API

    To start recording conference calls using the Record Conference API, use the name of the conference you want to record. If you want to start recording a conference call once a participant has entered the conference room, you can use this code.

    Create a file called `record_call.py` and paste into it this code.

    **Code**

    ```py  theme={null}
    import plivo

    client = plivo.RestClient('<auth_id>','<auth_token>')
    response = client.conferences.record(
        conference_name='<conference_room_name>', )
    print(response)
    ```

    Replace the auth placeholders with your authentication credentials from the Plivo console.

    ### Stop recording

    You can stop recording a conference call by using the conference name — see our [API reference documentation](/voice/api/conference/record-conference/#stop-recording-a-conference).

    ## Recording features

    * **File formats**: You can choose the recording file format (WAV or MP3) by using the `file_format` attribute for the Record API and Record Conference API, `recordFileFormat` for the Conference XML element, and `fileFormat` for the Record XML element.
    * **Channels**: Plivo makes mono recordings of conference calls and stereo recordings of regular calls.
    * **Recording length**: You can set the maximum duration of a recording by using arguments and attributes such as `time_limit` for the Record API and `maxLength` for the Record XML element.

    ## Managing recordings

    * **Fetching recording details**: You can store and retrieve the recording details of the voice calls and conference calls using the HTTP callbacks received on the action and callback URLs. You can also fetch recording details from the Voice >[ Recordings](https://cx.plivo.com/logs) page of the Plivo console.
    * **Deleting recordings**: You can delete a recording by using the [Delete a Recording API](/voice/api/recording/#list-all-recordings) and specifying a recording ID, which you can retrieve from the HTTP callback details stored in your database. You can also delete recordings from the Voice >[ Recordings](https://cx.plivo.com/logs) page of the Plivo console.

    ## Authentication for recordings

    Recordings hosted on Plivo servers are accessible only via unique, hard to guess, long URLs that Plivo shares in recording callbacks and API responses. By default, we do not enforce authentication on GET recording media requests to allow for easy implementation of use cases that involve playing recordings on a web or mobile front end.

    For enhanced security, we recommend enabling basic authentication for retrieving recording media assets in your Plivo account. You can enable Basic Auth for Recording URLs from the Voice >[ Other Settings](https://cx.plivo.com/home) page of the Plivo console.

    <Note>
      <strong>Note:</strong> Only account admins (users with the role Admin) have the required privileges to update the recording authentication preference setting.
    </Note>
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to initiating call recordings for outbound API calls, Dial XML-connected calls, and conference calls. You can record inbound calls to a Plivo number too when the application associated with the number returns an XML document with a Dial and a Record element.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the Numbers API. If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-phlo/) and a web server and safely expose that server to the internet.

    ## Record a complete outbound call using XML

    You can record a complete call session using the [Record XML](/voice/xml/record/) element in conjunction with a [Dial](/voice/xml/dial/) element response that’s returned by an answer URL. Recording a complete call is useful in applications such as virtual voicemail boxes and automated speech surveys.

    The XML might look like this:

    ```xml  theme={null}
    <Response>
     <Record action="https://<yourdomain>.com/get_recording/" startOnDialAnswer="true" redirect="false" maxLength="3600" />
     <Dial>
      <Number>12025551234</Number>
     </Dial>
    </Response>
    ```

    When the number specified in the Dial XML element answers the call, Plivo records the complete call session. Recording details are sent to the action URL as soon as the recording starts. You can use the attributes available in the Record XML element to control the recording behavior.

    Create a file called `record_call.php` and paste into it this code.

    ```php  theme={null}
    <?php
    require '../vendor/autoload.php';
    use Plivo\XML\Response;

    $response = new Response();

    $params = array(
        'action' => "https://<yourdomain>.com/get_recording/",
        'startOnDialAnswer' => "true",
        'redirect' => "false"
    );

    $response->addRecord($params);

    $dial = $response->addDial();
    $number = "<phone_number>";
    $dial->addNumber($number);

    Header('Content-type: text/xml');
    echo ($response->toXML());
    ```

    Replace the phone number placeholder with an actual phone number (for example, 12025551234).

    ## Record a complete conference call using XML

    You can record a complete conference call initiated using a [Conference XML](/voice/xml/conference/) element by using an XML response like this:

    ```xml  theme={null}
    <Response>
      <Conference callbackUrl="https://<yourdomain>.com/confevents/" callbackMethod="POST" record="true" recordFileFormat="wav">My Room</Conference>
    </Response>
    ```

    Plivo will record the complete audio of a conference call connected via this XML document. Recording details are sent to the action URL and callback URL as soon as the recording starts. The parameter `ConferenceAction=record` is also sent to the callback URL when the recording starts.

    Create a file called `record_call.php` and paste into it this code.

    ```php  theme={null}
    <?php
     require 'vendor/autoload.php';
     use Plivo\RestClient;
     use Plivo\Exceptions\PlivoRestException;
     $client = new RestClient("<auth_id>","<auth_token>");
     try
     {
        $response = $client
            ->conferences
            ->startRecording('<conference_room_name>');
        print_r($response);
     }
     catch(PlivoRestException $ex)
     {
        print_r($ex);
     }
    ```

    ## Start and stop call recording using APIs

    You can start and stop voice recordings for outbound API calls, Dial XML-connected calls, and conference calls using the Record API and Record Conference API.

    ### Record API

    To start recording using the Record API, you must use the CallUUID of the particular call that you want to record.

    ### Retrieve a CallUUID

    You can get the CallUUID of a call connected via the Outbound API and Dial XML from any of these arguments:

    * ring\_url: Plivo sends a webhook callback to the ring URL used in the call API request as soon as the destination number starts ringing.
    * answer\_url: Plivo sends a webhook callback to the answer URL when the destination number answers the call.
    * fallback\_url: If you define the fallback URL argument in the API request or the application attached to the Plivo number, and if the application server defined in the answer URL is unavailable, then Plivo will try to retrieve the XML document from the fallback URL to process the call. At that time Plivo will send a webhook callback to the fallback URL.
    * callback\_url: If you use the callbackUrl parameter in the Dial XML, Plivo will send a callback to the web server configured in callback URL when the number specified in the Dial XML element answers the call.

    ### Start recording

    Once you have the CallUUID of the call you want to record, you can call the record API and specify the CallUUID in the payload.

    For example, if you want to record an outbound API call, you can use the code below to record the call once the destination number answers the call. The recording will stop automatically once the call is completed.

    Change to the project directory and run this command to create a Laravel controller.

    ```shell  theme={null}
    $ php artisan make:controller RecordcallController
    ```

    Edit the `RecordcallController.php` file and paste into it this code:

    ```php  theme={null}
    <?php
    namespace App\Http\Controllers;
    require '../../vendor/autoload.php';
    use Plivo\RestClient;
    use Plivo\XML\Response;
    use Illuminate\Http\Request;

    class RecordcallController extends Controller
    {
        public function recordCall()
        {
            $r = new Response();

            $getinput_action_url = "https://<yourdomain>.com/recordAction/";
            $get_input = $r->addGetInput(['action' => $getinput_action_url, 'method' => "POST", 'digitEndTimeout' => "5", 'inputType' => "dtmf", 'redirect' => "true", ]);
            $get_input->addSpeak("Press 1 to record this call");
            Header('Content-type: text/xml');
            echo $response->toXML();
        }
        
        public function recordAction(Request $request)
        {
            $digit = $request->query('Digits');
            $uuid = $request->query('CallUUID');
            print_r("digits is: {$digit} and call_uuid is: {$uuid}");
            $response = new Response();
            $client = new RestClient("<auth_id>","<auth_token>");
            if ($digit == "1")
            {
                $response = $client
                    ->calls
                    ->startRecording($uuid);
                print_r($response);
            }
            else
            {
                print ("Invalid input");
            }
        }
    }
    ```

    Replace the auth placeholders with your authentication credentials from the Plivo console.

    ### Stop recording

    You can stop recording a call by using the CallUUID — see our [API reference documentation](/voice/api/call/record-calls/#stop-recording-a-call).

    ## Start and stop conference call recording using APIs

    ### Record Conference API

    To start recording conference calls using the Record Conference API, use the name of the conference you want to record. If you want to start recording a conference call once a participant has entered the conference room, you can use this code.

    ```php  theme={null}
    <?php
    require '../vendor/autoload.php';
    use Plivo\XML\Response;

    $response = new Response();

    $params = array(
        'record' => "true",
        'callbackUrl' => "https://<yourdomain>.com/confevents/",
        'callbackMethod' => "POST",
        'waitSound' => "https://<yourdomain>.com/waitmusic/"
    );

    $conference_name = "<conference_room_name>";
    $response->addConference($conference_name, $params);

    Header('Content-type: text/xml');
    echo ($response->toXML());
    ?>
    ```

    Replace the auth placeholders with your authentication credentials from the Plivo console.

    ### Stop recording

    You can stop recording a conference call by using the conference name — see our [API reference documentation](/voice/api/conference/record-conference/#stop-recording-a-conference).

    ## Recording features

    * **File formats**: You can choose the recording file format (WAV or MP3) by using the `file_format` attribute for the Record API and Record Conference API, `recordFileFormat` for the Conference XML element, and `fileFormat` for the Record XML element.
    * **Channels**: Plivo makes mono recordings of conference calls and stereo recordings of regular calls.
    * **Recording length**: You can set the maximum duration of a recording by using arguments and attributes such as `time_limit` for the Record API and `maxLength` for the Record XML element.

    ## Managing recordings

    * **Fetching recording details**: You can store and retrieve the recording details of the voice calls and conference calls using the HTTP callbacks received on the action and callback URLs. You can also fetch recording details from the Voice >[ Recordings](https://cx.plivo.com/logs) page of the Plivo console.
    * **Deleting recordings**: You can delete a recording by using the [Delete a Recording API](/voice/api/recording/#list-all-recordings) and specifying a recording ID, which you can retrieve from the HTTP callback details stored in your database. You can also delete recordings from the Voice >[ Recordings](https://cx.plivo.com/logs) page of the Plivo console.

    ## Authentication for recordings

    Recordings hosted on Plivo servers are accessible only via unique, hard to guess, long URLs that Plivo shares in recording callbacks and API responses. By default, we do not enforce authentication on GET recording media requests to allow for easy implementation of use cases that involve playing recordings on a web or mobile front end.

    For enhanced security, we recommend enabling basic authentication for retrieving recording media assets in your Plivo account. You can enable Basic Auth for Recording URLs from the Voice >[ Other Settings](https://cx.plivo.com/home) page of the Plivo console.

    <Note>
      <strong>Note:</strong> Only account admins (users with the role Admin) have the required privileges to update the recording authentication preference setting.
    </Note>
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to initiating call recordings for outbound API calls, Dial XML-connected calls, and conference calls. You can record inbound calls to a Plivo number too when the application associated with the number returns an XML document with a Dial and a Record element.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the Numbers API. If this is your first time using Plivo APIs, follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-phlo/) and a web server and safely expose that server to the internet.

    ## Record a complete outbound call using XML

    You can record a complete call session using the [Record XML](/voice/xml/record/) element in conjunction with a [Dial](/voice/xml/dial/) element response that’s returned by an answer URL. Recording a complete call is useful in applications such as virtual voicemail boxes and automated speech surveys.

    The XML might look like this:

    ```xml  theme={null}
    <Response>
     <Record action="https://<yourdomain>.com/get_recording/" startOnDialAnswer="true" redirect="false" maxLength="3600" />
     <Dial>
      <Number>12025551234</Number>
     </Dial>
    </Response>
    ```

    When the number specified in the Dial XML element answers the call, Plivo records the complete call session. Recording details are sent to the action URL as soon as the recording starts. You can use the attributes available in the Record XML element to control the recording behavior.

    Create an MVC controller and paste into it this code.

    ```cs  theme={null}
    using System;
    using System.Collections.Generic;
    using Plivo.XML;

    namespace Plivo {
      class MainClass {
        public static void Main(string[] args) {
          Plivo.XML.Response resp = new Plivo.XML.Response();
          resp.AddRecord(new Dictionary < string, string > () {
            {
              "action",
              "Https://<yourdomain>.com/get_recording/"
            },
            {
              "startOnDialAnswer",
              "true"
            },
            {
              "redirect",
              "false"
            }
          });

          Plivo.XML.Dial dial = new Plivo.XML.Dial(new
          Dictionary < string, string > () {});
        
          dial.AddNumber("<phone_number>", new Dictionary < string, string > () {});
          resp.Add(dial);
        
          var output = resp.ToString();
          Console.WriteLine(output);
        
        }
      }
    }
    ```

    Replace the phone number placeholder with an actual phone number (for example, 12025551234).

    ## Record a complete conference call using XML

    You can record a complete conference call initiated using a [Conference XML](/voice/xml/conference/) element by using an XML response like this:

    ```xml  theme={null}
    <Response>
      <Conference callbackUrl="https://<yourdomain>.com/confevents/" callbackMethod="POST" record="true" recordFileFormat="wav">My Room</Conference>
    </Response>
    ```

    Plivo will record the complete audio of a conference call connected via this XML document. Recording details are sent to the action URL and callback URL as soon as the recording starts. The parameter `ConferenceAction=record` is also sent to the callback URL when the recording starts.

    Create an MVC controller and paste into it this code.

    ```cs  theme={null}
    using System;
    using System.Collections.Generic;
    using Plivo.XML;

    namespace Plivo {
      class MainClass {
        public static void Main(string[] args) {
          Plivo.XML.Response resp = new Plivo.XML.Response();
          resp.AddConference("<conference_room_name>", new Dictionary < string, string > () {
            {
              "record",
              "true"
            },
            {
              "recordFileFormat",
              "mp3"
            },
            {
              "callbackUrl",
              "https://<yourdomain>.com/confevents/"
            },
            {
              "callbackMethod",
              "POST"
            },
            {
              "waitSound",
              "https://<yourdomain>.com/waitmusic/"
            }
          });
          var output = resp.ToString();
          Console.WriteLine(output);

        }
      }
    }
    ```

    ## Start and stop call recording using APIs

    You can start and stop voice recordings for outbound API calls, Dial XML-connected calls, and conference calls using the Record API and Record Conference API.

    ### Record API

    To start recording using the Record API, you must use the CallUUID of the particular call that you want to record.

    ### Retrieve a CallUUID

    You can get the CallUUID of a call connected via the Outbound API and Dial XML from any of these arguments:

    * ring\_url: Plivo sends a webhook callback to the ring URL used in the call API request as soon as the destination number starts ringing.
    * answer\_url: Plivo sends a webhook callback to the answer URL when the destination number answers the call.
    * fallback\_url: If you define the fallback URL argument in the API request or the application attached to the Plivo number, and if the application server defined in the answer URL is unavailable, then Plivo will try to retrieve the XML document from the fallback URL to process the call. At that time Plivo will send a webhook callback to the fallback URL.
    * callback\_url: If you use the callbackUrl parameter in the Dial XML, Plivo will send a callback to the web server configured in callback URL when the number specified in the Dial XML element answers the call.

    ### Start recording

    Once you have the CallUUID of the call you want to record, you can call the record API and specify the CallUUID in the payload.

    For example, if you want to record an outbound API call, you can use the code below to record the call once the destination number answers the call. The recording will stop automatically once the call is completed.

    Create an MVC controller and paste into it this code.

    ```cs  theme={null}
    using System;
    using System.Collections.Generic;
    using System.Diagnostics;
    using Microsoft.AspNetCore.Mvc;
    using Plivo;
    using Plivo.XML;

    // For more information on enabling MVC for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860
    namespace Recordcall.Controllers {
      public class RecordController: Controller {
        // GET: /<controller>/
        public IActionResult Index() {
          var resp = new Response();
          Plivo.XML.GetInput get_input = new
          Plivo.XML.GetInput("", new Dictionary < string, string > () {
            {
              "action",
              "https://<yourdomain>.com/record/action/"
            },
            {
              "method",
              "POST"
            },
            {
              "digitEndTimeout",
              "5"
            },
            {
              "finishOnKey",
              "#"
            },
            {
              "inputType",
              "dtmf"
            },
            {
              "redirect",
              "false"
            },
          });
          resp.Add(get_input);
          get_input.AddSpeak("Press 1 to record this call", new Dictionary < string, string > () {});
          var output = resp.ToString();
          return this.Content(output, "text/xml");
        }
        // Action URL
        public String Action() {
          String digits = Request.Query["Digits"];
          String uuid = Request.Query["CallUUID"];
          Debug.WriteLine("Digit pressed : {0}, Call UUID : {1}", digits, uuid);

          if (digits == "1") {
            string auth_id = "<auth_id>";
            string auth_token = "<auth_token>";
            var api = new PlivoApi(auth_id, auth_token);
            var resp = api.Call.StartRecording(
            callUuid: uuid);
            Debug.WriteLine(resp);
          }
          else {
            Debug.WriteLine("Invalid input");
          }
          return "OK";
        }
      }
    }
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home).

    ### Stop recording

    You can stop recording a call by using the CallUUID — see our [API reference documentation](/voice/api/call/record-calls/#stop-recording-a-call).

    ## Start and stop conference call recording using APIs

    ### Record Conference API

    To start recording conference calls using the Record Conference API, use the name of the conference you want to record. If you want to start recording a conference call once a participant has entered the conference room, you can use this code.

    ```cs  theme={null}
      using System;
      using System.Collections.Generic;
      using Plivo;
      using Plivo.Exception;

    namespace PlivoExamples {
      internal class Program {
        public static void Main(string[] args) {
          var api = new PlivoApi("<auth_id>","<auth_token>");
          try {
            var response = api.Conference.StartRecording("<conference_room_name>");
            Console.WriteLine(response);
          }
          catch(PlivoRestException e) {
            Console.WriteLine("Exception: " + e.Message);
          }
        }
      }
    }
    ```

    Replace the auth placeholders with your authentication credentials from the Plivo console.

    ### Stop recording

    You can stop recording a conference call by using the conference name — see our [API reference documentation](/voice/api/conference/record-conference/#stop-recording-a-conference).

    ## Recording features

    * **File formats**: You can choose the recording file format (WAV or MP3) by using the `file_format` attribute for the Record API and Record Conference API, `recordFileFormat` for the Conference XML element, and `fileFormat` for the Record XML element.
    * **Channels**: Plivo makes mono recordings of conference calls and stereo recordings of regular calls.
    * **Recording length**: You can set the maximum duration of a recording by using arguments and attributes such as `time_limit` for the Record API and `maxLength` for the Record XML element.

    ## Managing recordings

    * **Fetching recording details**: You can store and retrieve the recording details of the voice calls and conference calls using the HTTP callbacks received on the action and callback URLs. You can also fetch recording details from the Voice >[ Recordings](https://cx.plivo.com/logs) page of the Plivo console.
    * **Deleting recordings**: You can delete a recording by using the [Delete a Recording API](/voice/api/recording/#list-all-recordings) and specifying a recording ID, which you can retrieve from the HTTP callback details stored in your database. You can also delete recordings from the Voice >[ Recordings](https://cx.plivo.com/logs) page of the Plivo console.

    ## Authentication for recordings

    Recordings hosted on Plivo servers are accessible only via unique, hard to guess, long URLs that Plivo shares in recording callbacks and API responses. By default, we do not enforce authentication on GET recording media requests to allow for easy implementation of use cases that involve playing recordings on a web or mobile front end.

    For enhanced security, we recommend enabling basic authentication for retrieving recording media assets in your Plivo account. You can enable Basic Auth for Recording URLs from the Voice >[ Other Settings](https://cx.plivo.com/home) page of the Plivo console.

    <Note>
      <strong>Note:</strong> Only account admins (users with the role Admin) have the required privileges to update the recording authentication preference setting.
    </Note>
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to initiating call recordings for outbound API calls, Dial XML-connected calls, and conference calls. You can record inbound calls to a Plivo number too when the application associated with the number returns an XML document with a Dial and a Record element.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the Numbers API. If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-phlo/) and a web server and safely expose that server to the internet.

    ## Record a complete outbound call using XML

    You can record a complete call session using the [Record XML](/voice/xml/record/) element in conjunction with a [Dial](/voice/xml/dial/) element response that’s returned by an answer URL. Recording a complete call is useful in applications such as virtual voicemail boxes and automated speech surveys.

    The XML might look like this:

    ```xml  theme={null}
    <Response>
     <Record action="https://<yourdomain>.com/get_recording/" startOnDialAnswer="true" redirect="false" maxLength="3600" />
     <Dial>
      <Number>12025551234</Number>
     </Dial>
    </Response>
    ```

    When the number specified in the Dial XML element answers the call, Plivo records the complete call session. Recording details are sent to the action URL as soon as the recording starts. You can use the attributes available in the Record XML element to control the recording behavior.

    ```java  theme={null}
    package com.plivo.api.xml.samples.record;

    import com.plivo.api.exceptions.PlivoXmlException;
    import com.plivo.api.xml.Dial;
    import com.plivo.api.xml.Number;
    import com.plivo.api.xml.Record;
    import com.plivo.api.xml.Response;

    class RecordACompleteCallSession {
        public static void main(String[] args) throws PlivoXmlException {
            Response response = new Response()
                .children(
                    new Record("https://<yourdomain>.com/get_recording/")
                    .redirect(false)
                    .startOnDialAnswer(true),
                    new Dial()
                    .children(
                        new Number("<phone_number>")
                    )
                );
            System.out.println(response.toXmlString());
        }
    }
    ```

    Replace the phone number placeholder with an actual phone number (for example, 12025551234).

    ## Record a complete conference call using XML

    You can record a complete conference call initiated using a [Conference XML](/voice/xml/conference/) element by using an XML response like this:

    ```xml  theme={null}
    <Response>
      <Conference callbackUrl="https://<yourdomain>.com/confevents/" callbackMethod="POST" record="true" recordFileFormat="wav">My Room</Conference>
    </Response>
    ```

    Plivo will record the complete audio of a conference call connected via this XML document. Recording details are sent to the action URL and callback URL as soon as the recording starts. The parameter `ConferenceAction=record` is also sent to the callback URL when the recording starts.

    ```java  theme={null}
    // Example for conference
    package com.plivo.api.xml.samples.conference;

    import com.plivo.api.exceptions.PlivoXmlException;
    import com.plivo.api.xml.Conference;
    import com.plivo.api.xml.Response;
    import com.plivo.api.xml.Speak;

    class RecordConference {
        public static void main(String[] args) throws PlivoXmlException {
            Response response = new Response()
                .children(
                    new Speak("You will now be placed into the conference"),
                    new Conference("<conference_room_name>")
                    .record(true)
                    .callbackMethod("POST")
                    .callbackUrl("https://<yourdomain>.com/confevents/")
                    .waitSound("https://<yourdomain>.com/waitmusic/")
                );
            System.out.println(response.toXmlString());
        }
    }
    ```

    ## Start and stop call recording using APIs

    You can start and stop voice recordings for outbound API calls, Dial XML-connected calls, and conference calls using the Record API and Record Conference API.

    ### Record API

    To start recording using the Record API, you must use the CallUUID of the particular call that you want to record.

    ### Retrieve a CallUUID

    You can get the CallUUID of a call connected via the Outbound API and Dial XML from any of these arguments:

    * ring\_url: Plivo sends a webhook callback to the ring URL used in the call API request as soon as the destination number starts ringing.
    * answer\_url: Plivo sends a webhook callback to the answer URL when the destination number answers the call.
    * fallback\_url: If you define the fallback URL argument in the API request or the application attached to the Plivo number, and if the application server defined in the answer URL is unavailable, then Plivo will try to retrieve the XML document from the fallback URL to process the call. At that time Plivo will send a webhook callback to the fallback URL.
    * callback\_url: If you use the callbackUrl parameter in the Dial XML, Plivo will send a callback to the web server configured in callback URL when the number specified in the Dial XML element answers the call.

    ### Start recording

    Once you have the CallUUID of the call you want to record, you can call the record API and specify the CallUUID in the payload.

    For example, if you want to record an outbound API call, you can use the code below to record the call once the destination number answers the call. The recording will stop automatically once the call is completed.

    Locate the file PlivoVoiceApplication.java in the src/main/java/com.example.demo/ folder and paste into it this code.

    <Note>
      <strong>Note:</strong> Here, the demo application name is PlivoVoiceApplication.java because the friendly name provided in the <a href="https://start.spring.io/" rel="nofollow">Spring Initializr</a> was “Plivo Voice.”
    </Note>

    ```java  theme={null}
    package com.example.demo;
    import com.plivo.api.Plivo;
    import com.plivo.api.exceptions.PlivoRestException;
    import com.plivo.api.models.call.Call;
    import com.plivo.api.models.call.actions.CallRecordCreateResponse;
    import com.plivo.api.xml.*;
    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RequestParam;
    import org.springframework.web.bind.annotation.RestController;
    import com.plivo.api.exceptions.PlivoXmlException;

    import java.io.IOException;

    @SpringBootApplication
    @RestController
    public class PlivoVoiceApplication {

        public static void main(String[] args) {
            SpringApplication.run(PlivoVoiceApplication.class, args);
        }
        
        @GetMapping(value = "/record", produces = {
            "application/xml"
        })
        public Response recordCall() throws PlivoXmlException, IOException, PlivoRestException {
            Response resp = new Response();
            resp.children(
                new GetInput()
                .action("https://<yourdomain>.com/record_action/")
                .method("POST")
                .inputType("dtmf")
                .digitEndTimeout(5)
                .redirect(true)
                .children(
                    new Speak("Press 1 to record this call")
                ));
            return resp;
        }
        
        @GetMapping(value = "/record_action", produces = {
            "application/xml"
        })
        public String forwardCall(@RequestParam("Digits") String digits, @RequestParam("CallUUID") String callUuid) throws PlivoXmlException, IOException, PlivoRestException {
            System.out.println("Digit : " + digits + " Call UUID : " + callUuid);
            Response resp = new Response();
            Plivo.init("<auth_id>", "<auth_token>");
            if (digits.equals("1")) {
                CallRecordCreateResponse r = Call.recorder(callUuid)
                    .record();
                System.out.println(r);
            } else {
                System.out.println("Invalid input");
            }
            return "ok";
        }
    }
    ```

    Replace the auth placeholders with your authentication credentials from the Plivo console.

    ### Stop recording

    You can stop recording a call by using the CallUUID — see our [API reference documentation](/voice/api/call/record-calls/#stop-recording-a-call).

    ## Start and stop conference call recording using APIs

    ### Record Conference API

    To start recording conference calls using the Record Conference API, use the name of the conference you want to record. If you want to start recording a conference call once a participant has entered the conference room, you can use this code.

    ```java  theme={null}
    package com.plivo.api.samples.conference.record;

    import java.io.IOException;

    import com.plivo.api.Plivo;
    import com.plivo.api.exceptions.PlivoRestException;
    import com.plivo.api.models.conference.Conference;
    import com.plivo.api.models.conference.ConferenceRecordCreateResponse;

        class RecordCreate {
        public static void main(String[] args) {
            Plivo.init("<auth_id>","<auth_token>");
            try {
                ConferenceRecordCreateResponse response = Conference.recorder("<conference_room_name>")
                    .record();
        
                System.out.println(response);
            } catch (PlivoRestException | IOException e) {
                e.printStackTrace();
            }
        }
        }
    ```

    Replace the auth placeholders with your authentication credentials from the Plivo console.

    ### Stop recording

    You can stop recording a conference call by using the conference name — see our [API reference documentation](/voice/api/conference/record-conference/#stop-recording-a-conference).

    ## Recording features

    * **File formats**: You can choose the recording file format (WAV or MP3) by using the `file_format` attribute for the Record API and Record Conference API, `recordFileFormat` for the Conference XML element, and `fileFormat` for the Record XML element.
    * **Channels**: Plivo makes mono recordings of conference calls and stereo recordings of regular calls.
    * **Recording length**: You can set the maximum duration of a recording by using arguments and attributes such as `time_limit` for the Record API and `maxLength` for the Record XML element.

    ## Managing recordings

    * **Fetching recording details**: You can store and retrieve the recording details of the voice calls and conference calls using the HTTP callbacks received on the action and callback URLs. You can also fetch recording details from the Voice >[ Recordings](https://cx.plivo.com/logs) page of the Plivo console.
    * **Deleting recordings**: You can delete a recording by using the [Delete a Recording API](/voice/api/recording/#list-all-recordings) and specifying a recording ID, which you can retrieve from the HTTP callback details stored in your database. You can also delete recordings from the Voice >[ Recordings](https://cx.plivo.com/logs) page of the Plivo console.

    ## Authentication for recordings

    Recordings hosted on Plivo servers are accessible only via unique, hard to guess, long URLs that Plivo shares in recording callbacks and API responses. By default, we do not enforce authentication on GET recording media requests to allow for easy implementation of use cases that involve playing recordings on a web or mobile front end.

    For enhanced security, we recommend enabling basic authentication for retrieving recording media assets in your Plivo account. You can enable Basic Auth for Recording URLs from the Voice >[ Other Settings](https://cx.plivo.com/home) page of the Plivo console.

    <Note>
      <strong>Note:</strong> Only account admins (users with the role Admin) have the required privileges to update the recording authentication preference setting.
    </Note>
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to initiating call recordings for outbound API calls, Dial XML-connected calls, and conference calls. You can record inbound calls to a Plivo number too when the application associated with the number returns an XML document with a Dial and a Record element.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. You must have a voice-enabled Plivo phone number to receive incoming calls; you can rent numbers from the [Numbers](https://cx.plivo.com/phone-numbers) page of the Plivo console, or by using the Numbers API. If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-phlo/) and a web server and safely expose that server to the internet.

    ## Record a complete outbound call using XML

    You can record a complete call session using the [Record XML](/voice/xml/record/) element in conjunction with a [Dial](/voice/xml/dial/) element response that’s returned by an answer URL. Recording a complete call is useful in applications such as virtual voicemail boxes and automated speech surveys.

    The XML might look like this:

    ```xml  theme={null}
    <Response>
     <Record action="https://<yourdomain>.com/get_recording/" startOnDialAnswer="true" redirect="false" maxLength="3600" />
     <Dial>
      <Number>12025551234</Number>
     </Dial>
    </Response>
    ```

    When the number specified in the Dial XML element answers the call, Plivo records the complete call session. Recording details are sent to the action URL as soon as the recording starts. You can use the attributes available in the Record XML element to control the recording behavior.

    Create a file called `record_call.go` and paste into it this code.

    ```go  theme={null}
    package main
    import "github.com/plivo/plivo-go/v7/xml"
    func main() {
      response: = xml.ResponseElement {
    ​    Contents: [] interface {} {
       new(xml.RecordElement).
       SetAction("https://<yourdomain>.com/get_recording/").
       SetRedirect(false).
       SetStartOnDialAnswer(true),

    ​     new(xml.DialElement).
       SetContents([] interface {} {
    ​     new(xml.NumberElement).
    ​     SetContents("<phone_number>"),
       }),
     },
    }
    print(response.String())
    }
    ```

    Replace the phone number placeholder with an actual phone number (for example, 12025551234).

    ## Record a complete conference call using XML

    You can record a complete conference call initiated using a [Conference XML](/voice/xml/conference/) element by using an XML response like this:

    ```xml  theme={null}
    <Response>
      <Conference callbackUrl="https://<yourdomain>.com/confevents/" callbackMethod="POST" record="true" recordFileFormat="wav">My Room</Conference>
    </Response>
    ```

    Plivo will record the complete audio of a conference call connected via this XML document. Recording details are sent to the action URL and callback URL as soon as the recording starts. The parameter `ConferenceAction=record` is also sent to the callback URL when the recording starts.

    Create a file called `record_call.go` and paste into it this code.

    ```go  theme={null}
    package main
    import "github.com/plivo/plivo-go/v7/xml"
    func main() {
      response: = xml.ResponseElement {
    ​    Contents: [] interface {} {
    ​      new(xml.SpeakElement).
    ​      AddSpeak("You will now be placed into the conference"), 
    ​        new(xml.ConferenceElement).
    ​      SetRecord(true).
    ​      SetCallbackMethod("POST").
    ​      SetCallbackUrl("https://<yourdomain>.com/confevents/").
    ​      SetWaitSound("https://<yourdomain>.com/waitmusic/").
    ​      SetContents("<conference_room_name> "),
    ​    },
      }
      print(response.String())
    }
    ```

    ## Start and stop call recording using APIs

    You can start and stop voice recordings for outbound API calls, Dial XML-connected calls, and conference calls using the Record API and Record Conference API.

    ### Record API

    To start recording using the Record API, you must use the CallUUID of the particular call that you want to record.

    ### Retrieve a CallUUID

    You can get the CallUUID of a call connected via the Outbound API and Dial XML from any of these arguments:

    * ring\_url: Plivo sends a webhook callback to the ring URL used in the call API request as soon as the destination number starts ringing.
    * answer\_url: Plivo sends a webhook callback to the answer URL when the destination number answers the call.
    * fallback\_url: If you define the fallback URL argument in the API request or the application attached to the Plivo number, and if the application server defined in the answer URL is unavailable, then Plivo will try to retrieve the XML document from the fallback URL to process the call. At that time Plivo will send a webhook callback to the fallback URL.
    * callback\_url: If you use the callbackUrl parameter in the Dial XML, Plivo will send a callback to the web server configured in callback URL when the number specified in the Dial XML element answers the call.

    ### Start recording

    Once you have the CallUUID of the call you want to record, you can call the record API and specify the CallUUID in the payload.

    For example, if you want to record an outbound API call, you can use the code below to record the call once the destination number answers the call. The recording will stop automatically once the call is completed.

    Create a file called `record_call.go` and paste into it this code.

    ```go  theme={null}
    package main
    import (
      "fmt"
      "github.com/go-martini/martini"
      "github.com/plivo/plivo-go/v7/xml"
      "github.com/plivo/plivo-go/v7"
      "net/http"
    )
    func main() {
      m: = martini.Classic()
      m.Post("/record/", func(w http.ResponseWriter, r * http.Request) string {
        w.Header().Set("Content-Type", "application/xml")
        response: = xml.ResponseElement {
          Contents: [] interface {} {
            new(xml.GetInputElement).
            SetAction("https://<yourdomain>.com/record/action/").
            SetMethod("POST").
            SetDigitEndTimeout(5).
            SetInputType("dtmf").
            SetRedirect(true).
            SetContents([] interface {} {
              new(xml.SpeakElement).
              AddSpeak("Press 1 to record this call"),
            }),
          },
        }
        return response.String()
      })
      m.Post("/record/action/", func(w http.ResponseWriter, r * http.Request) string {
        digits: = r.FormValue("Digits")
        uuid: = r.FormValue("CallUUID")
        fmt.Printf("Digit received: %#v\n", digits)
        client,
        err: = plivo.NewClient("<auth_id>", "<auth_token>", & plivo.ClientOptions {})
        if err != nil {
          panic(err)
        }
        response,
        err: = client.Calls.Record(
          uuid,
          plivo.CallRecordParams {},
        )
        fmt.Printf("Response: %#v\n", response)
        return "ok"
      })
      m.Run()
    }
    ```

    Replace the auth placeholders with your authentication credentials from the Plivo console.

    ### Stop recording

    You can stop recording a call by using the CallUUID — see our [API reference documentation](/voice/api/call/record-calls/#stop-recording-a-call).

    ## Start and stop conference call recording using APIs

    ### Record Conference API

    To start recording conference calls using the Record Conference API, use the name of the conference you want to record. If you want to start recording a conference call once a participant has entered the conference room, you can use this code.

    Create a file called `record_call.go` and paste into it this code.

    ```go  theme={null}
    package main
    import "fmt"
    import "github.com/plivo/plivo-go/v7"
    func main() {
      err: = plivo.NewClient("<auth_id>", "<auth_token>", & plivo.ClientOptions {})
      if err != nil {
        panic(err)
      }
      response, err: = client.Conferences.Record(
        "<conference_room_name>",
        plivo.ConferenceRecordParams {},
      )
      if err != nil {
        panic(err)
      }
      fmt.Printf("Response: %#v\n", response)
    }
    ```

    Replace the auth placeholders with your authentication credentials from the Plivo console.

    ### Stop recording

    You can stop recording a conference call by using the conference name — see our [API reference documentation](/voice/api/conference/record-conference/#stop-recording-a-conference).

    ## Recording features

    * **File formats**: You can choose the recording file format (WAV or MP3) by using the `file_format` attribute for the Record API and Record Conference API, `recordFileFormat` for the Conference XML element, and `fileFormat` for the Record XML element.
    * **Channels**: Plivo makes mono recordings of conference calls and stereo recordings of regular calls.
    * **Recording length**: You can set the maximum duration of a recording by using arguments and attributes such as `time_limit` for the Record API and `maxLength` for the Record XML element.

    ## Managing recordings

    * **Fetching recording details**: You can store and retrieve the recording details of the voice calls and conference calls using the HTTP callbacks received on the action and callback URLs. You can also fetch recording details from the Voice >[ Recordings](https://cx.plivo.com/logs) page of the Plivo console.
    * **Deleting recordings**: You can delete a recording by using the [Delete a Recording API](/voice/api/recording/#list-all-recordings) and specifying a recording ID, which you can retrieve from the HTTP callback details stored in your database. You can also delete recordings from the Voice >[ Recordings](https://cx.plivo.com/logs) page of the Plivo console.

    ## Authentication for recordings

    Recordings hosted on Plivo servers are accessible only via unique, hard to guess, long URLs that Plivo shares in recording callbacks and API responses. By default, we do not enforce authentication on GET recording media requests to allow for easy implementation of use cases that involve playing recordings on a web or mobile front end.

    For enhanced security, we recommend enabling basic authentication for retrieving recording media assets in your Plivo account. You can enable Basic Auth for Recording URLs from the Voice >[ Other Settings](https://cx.plivo.com/home) page of the Plivo console.

    <Note>
      <strong>Note:</strong> Only account admins (users with the role Admin) have the required privileges to update the recording authentication preference setting.
    </Note>
  </Tab>
</Tabs>
