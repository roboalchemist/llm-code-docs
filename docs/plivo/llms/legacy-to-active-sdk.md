# Source: https://plivo.com/docs/voice/migrate/sdk/legacy-to-active-sdk/legacy-to-active-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Upgrade from Legacy to v4.8.0 or Latest Version

> Migrate from legacy SDK to v4.x — major upgrade steps and changes

<Tabs>
  <Tab title="Node">
    # Upgrade from Node.js Legacy to v4.8.0 or Latest Version

    ## Introduction

    This is a major application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      <strong>Deprecation notice:</strong> We’re deprecating Plivo Node SDK legacy versions lower than v4.8.0 on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and voice calls may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.
    </Warning>

    ## Migrate your applications

    ### Node.js version support

    The 4.x version of the Plivo SDK is compatible with Node.js versions 5.5 and higher.

    Use the command **npm install plivo\@4.8.0** to upgrade to the active version of the SDK, or **npm install plivo\@latest** to upgrade to the latest version.

    After you upgrade to the latest version of the SDK, you should check every program that depends on it and make changes to the syntax for several kinds of operations. Here are examples of how coding differs between the deprecated legacy version of the SDK and the latest active versions.

    ### Import the SDK

    <CodeGroup>
      ```js Legacy theme={null}
      var plivo = require('plivo');
      ```

      ```js Latest theme={null}
      var plivo = require('plivo');
      ```
    </CodeGroup>

    ### Initialize

    <CodeGroup>
      ```js Legacy theme={null}
      var p = plivo.RestAPI({
        authId: '<auth_id>',
        authToken: '<auth_token>'
      });
      ```

      ```js Latest theme={null}
      var client = new plivo.Client("<auth_id>","<auth_token>");
      ```
    </CodeGroup>

    ### Access resources

    <CodeGroup>
      ```js Legacy theme={null}
      p.make_call(params, function (status, response) {
          console.log('Status: ', status);
          console.log('API Response:\n', response);
      });
      ```

      ```js Latest theme={null}
      client.calls.create(params).then(function (response) {
              console.log(response);
          }, function (err) {
              console.error(err);
          });
      ```
    </CodeGroup>

    ### Make a call

    <CodeGroup>
      ```js Legacy theme={null}
      var plivo = require('plivo');
      var p = plivo.RestAPI({
        authId: '<auth_id>',
        authToken: '<auth_token>'
      });

      var params = {
          'to': '2025552323',    
          'from' : '2025551212', 
          'answer_url' : "https://s3.amazonaws.com/static.plivo.com/answer.xml",
          'answer_method' : "GET"
      };
      p.make_call(params, function (status, response) {
          console.log('Status: ', status);
          console.log('API Response:\n', response);
      });
      ```

      ```js Latest theme={null}
      var plivo = require('plivo');
      (function main() {
          'use strict';
          var client = new plivo.Client("<auth_id>","<auth_token>");
          client.calls.create(
              "+12025551212", // from
              "+12025552323", // to
              "https://s3.amazonaws.com/static.plivo.com/answer.xml", 
              {
                  answerMethod: "GET",
              },
          ).then(function (response) {
              console.log(response);
          }, function (err) {
              console.error(err);
          });
      })();
      ```
    </CodeGroup>

    ### Dial XML

    <CodeGroup>
      ```js Legacy theme={null}
      var plivo = require('plivo');

      var response = plivo.Response();

      var params = {
          'dialMusic': "https://<yourdomain>.com/dial_music/"
      };
      var dial = response.addDial(params);

      var first_number = "12025551212";
      dial.addNumber(first_number);

      console.log(response.toXML());
      ```

      ```js Latest theme={null}
      var plivo = require('plivo');

      var response = plivo.Response();

      var params = {
          'dialMusic': "https://<yourdomain>.com/dial_music/"
      };
      var dial = response.addDial(params);

      var first_number = "12025551212";
      dial.addNumber(first_number);

      console.log(response.toXML());
      ```
    </CodeGroup>

    ### Conference XML

    <CodeGroup>
      ```js Legacy theme={null}
      var plivo = require('plivo');
      var response = plivo.Response();
      var params = {
          'startConferenceOnEnter': "false",
          'waitSound': "https://<yourdomain>.com/waitMusic/"
      };
      var conference_name = "My Room";
      response.addConference(conference_name, params);
      console.log(response.toXML());
      ```

      ```js Latest theme={null}
      var plivo = require('plivo');


      var response = plivo.Response();

      var params = {
          'startConferenceOnEnter': "false",
          'waitSound': "https://<yourdomain>.com/waitMusic/"
      };
      var conference_name = "My Room";
      response.addConference(conference_name, params);

      console.log(response.toXML());
      ```
    </CodeGroup>

    ### Record API

    <CodeGroup>
      ```js Legacy theme={null}
      var plivo = require('plivo');
      var p = plivo.RestAPI({
              "authId": "<auth_id>",
              "authToken": "<auth_token>"
          });
       var params = {'call_uuid':call_uuid};   
      var response = p.record(params);
      console.log(response);
      ```

      ```js Latest theme={null}
      var plivo = require('plivo');
      (function main() {
          'use strict';
          var client = new plivo.Client("<auth_id>","<auth_token>");
          client.calls.record(
              "eba53b9e-8fbd-45c1-9444-696d2172fbc8", // call uuid
          ).then(function (response) {
              console.log(response);
          }, function (err) {
              console.error(err);
          });
      })();
      ```
    </CodeGroup>

    ### Record XML

    <CodeGroup>
      ```js Legacy theme={null}
      var plivo = require('plivo');

      var response = plivo.Response();

      var params = {
          'action': "https://<yourdomain>.com/get_recording/",
          'startOnDialAnswer': "true",
          'redirect': "false"
      };
      response.addRecord(params);

      var dial = response.addDial();
      var number = "12025552323";
      dial.addNumber(number);

      console.log(response.toXML());
      ```

      ```js Latest theme={null}
      var plivo = require('plivo');

      var response = plivo.Response();

      var params = {
          'action': "https://<yourdomain>.com/get_recording/",
          'startOnDialAnswer': "true",
          'redirect': "false"
      };
      response.addRecord(params);

      var dial = response.addDial();
      var number = "12025552323";
      dial.addNumber(number);

      console.log(response.toXML());
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Ruby">
    # Upgrade from Ruby Legacy to v4.9.0 or Latest Version

    ## Introduction

    This is a major application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      <strong>Deprecation notice:</strong> We’re deprecating Plivo Ruby SDK legacy versions lower than v4.9.0 on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and voice calls may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.
    </Warning>

    ## Migrate your applications

    ### Ruby version support

    The Plivo Ruby SDK supports Ruby 2.0 and above.

    Use the command **gem install plivo -v 4.9.0** to upgrade to the active version of the SDK, or **gem update plivo** to upgrade to the latest version.

    After you upgrade to the latest version of the SDK, you should check every program that depends on it and make changes to the syntax for several kinds of operations. Here are examples of how coding differs between the deprecated legacy version of the SDK and the latest active versions.

    ### Importing the SDK

    <CodeGroup>
      ```ruby Legacy theme={null}
      require 'plivo'
      ```

      ```ruby Latest theme={null}
      require 'plivo'
      ```
    </CodeGroup>

    ### Initialize

    <CodeGroup>
      ```ruby Legacy theme={null}
      p = RestAPI.new("<auth_id>","<auth_token>")
      ```

      ```ruby Latest theme={null}
      api = RestClient.new("<auth_id>","<auth_token>")
      ```
    </CodeGroup>

    ### Access Resources

    <CodeGroup>
      ```ruby Legacy theme={null}
      response = p.make_call(params)
      ```

      ```ruby Latest theme={null}
      response = api.calls.create(params)
      ```
    </CodeGroup>

    ### Make a call

    <CodeGroup>
      ```ruby Legacy theme={null}
      require 'rubygems'
      require 'plivo'
      include Plivo
      AUTH_ID = "<auth_id>"
      AUTH_TOKEN = "<auth_token>"

      p = RestAPI.new(AUTH_ID, AUTH_TOKEN)

      params = {
          'to' => '12025552323',   
          'from' => '12025551212', 
          'answer_url' => 'https://s3.amazonaws.com/static.plivo.com/answer.xml',
          'answer_method' => 'GET'
      }

      response = p.make_call(params)
      print response
      ```

      ```ruby Latest theme={null}
      require 'rubygems'
      require 'plivo'

      include Plivo
      include Plivo::Exceptions

      api = RestClient.new("<auth_id>","<auth_token>")

      begin
        response = api.calls.create(
          '+12025551212',
          ['+12025552323'],
          'https://s3.amazonaws.com/static.plivo.com/answer.xml'
        )
        puts response
      rescue PlivoRESTError => e
        puts 'Exception: ' + e.message
      end
      ```
    </CodeGroup>

    ### Dial XML

    <CodeGroup>
      ```ruby Legacy theme={null}
      require 'rubygems'
      require 'plivo'
      include Plivo

      response = Response.new()

      params = {
          'dialMusic' => "https://<yourdomain>.com/dial_music/"
      }

      dial = response.addDial(params)
      first_number = "12025552323"
      dial.addNumber(first_number)

      puts response.to_xml()
      ```

      ```ruby Latest theme={null}
      require 'rubygems'
      require 'plivo'

      include Plivo::XML
      include Plivo::Exceptions

      begin
        response = Response.new

        params = {
            'dialMusic' => "https://<yourdomain>.com/dial_music/"
        }

        dial = response.addDial(params)
        first_number = "12025552323"
        dial.addNumber(first_number)

        xml = PlivoXML.new(response)
        puts xml.to_xml
      rescue PlivoXMLError => e
        puts 'Exception: ' + e.message
      end
      ```
    </CodeGroup>

    ### Conference XML

    <CodeGroup>
      ```ruby Legacy theme={null}
      require 'rubygems'
      require 'plivo'
      include Plivo

      response = Response.new()

      params = {
          'startConferenceOnEnter' => "false",
          'waitSound' => "https://<yourdomain>.com/waitmusic/"
      }

      conference_name = "My Room"
      response.addConference(conference_name, params)

      puts response.to_xml()
      ```

      ```ruby Latest theme={null}
      require 'rubygems'
      require 'plivo'

      include Plivo::XML
      include Plivo::Exceptions

      begin
        response = Response.new

        params = {
          'startConferenceOnEnter' => "false",
          'waitSound' => "https://<yourdomain>.com/waitmusic/"
        }

        conference_name = "My Room"
        response.addConference(conference_name, params)

        xml = PlivoXML.new(response)
        puts xml.to_xml
      rescue PlivoXMLError => e
        puts 'Exception: ' + e.message
      end
      ```
    </CodeGroup>

    ### Record API

    <CodeGroup>
      ```ruby Legacy theme={null}
      require 'rubygems'
      require 'plivo'
      AUTH_ID = "<auth_id>"
      AUTH_TOKEN = "<auth_token>"


      p = RestAPI.new(AUTH_ID, AUTH_TOKEN)
      params = {'call_uuid' => call_uuid}
      response = p.record(params)
      print response
      ```

      ```ruby Latest theme={null}
      require 'rubygems'
      require 'plivo'

      include Plivo
      include Plivo::Exceptions

      api = RestClient.new("<auth_id>","<auth_token>")

      begin
        response = api.calls.record(
          'eba53b9e-8fbd-45c1-9444-696d2172fbc8'
        )
        puts response
      rescue PlivoRESTError => e
        puts 'Exception: ' + e.message
      end
      ```
    </CodeGroup>

    ### Record XML

    <CodeGroup>
      ```ruby Legacy theme={null}
      require 'rubygems'
      require 'plivo'
      include Plivo

      response = Response.new()

      params = {
          'action' => "https://<yourdomain>.com/get_recording/",
          'startOnDialAnswer' => "true",
          'redirect' => "false"
      }

      response.addRecord(params)

      dial = response.addDial()
      number = "12025552323"
      dial.addNumber(number)

      puts response.to_xml()
      ```

      ```ruby Latest theme={null}
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
        number = '12025552323'
        dial.addNumber(number)

        xml = PlivoXML.new(response)
        puts xml.to_xml
      rescue PlivoXMLError => e
        puts 'Exception: ' + e.message
      end
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Python">
    # Upgrade from Python SDK Legacy to v4.9.0 or Latest Version

    ## Introduction

    This is a major application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      <strong>Deprecation notice:</strong> We’re deprecating Plivo Python SDK legacy versions lower than v4.9.0 on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and voice calls may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.
    </Warning>

    ## Migrate your applications

    ### Python version support

    Version 4.x of the Python SDK requires at least Python version 2.7. It will work with later versions, including Python 3.x versions.

    Use the command **pip install --upgrade plivo==4.9.0** to upgrade to the active version of the SDK, or **pip install --upgrade plivo** to upgrade to the latest version.

    After you upgrade to the latest version of the SDK, you should check every program that depends on it and make changes to the syntax for several kinds of operations. Here are examples of how coding differs between the deprecated legacy version of the SDK and the latest active versions.

    ### Importing the SDK

    <CodeGroup>
      ```py Legacy theme={null}
      import plivo, plivoxml
      ```

      ```py Latest theme={null}
      import plivo
      from plivo import plivoxml
      ```
    </CodeGroup>

    ### Initializing

    <CodeGroup>
      ```py Legacy theme={null}
      p = plivo.RestAPI('<auth_id>','<auth_token>')
      ```

      ```py Latest theme={null}
      client = plivo.RestClient('<auth_id>','<auth_token>')
      ```
    </CodeGroup>

    ### Accessing resources

    <CodeGroup>
      ```py Legacy theme={null}
      response = p.make_call(params)
      ```

      ```py Latest theme={null}
      response = client.calls.create(params)
      ```
    </CodeGroup>

    ### Making a call

    <CodeGroup>
      ```py Legacy theme={null}
      import plivo, plivoxml

      p = plivo.RestAPI('<auth_id>','<auth_token>')

      params = {
          'to': '<destination_number>',  
          'from' : '<caller_id>',
          'answer_url' : 'https://s3.amazonaws.com/static.plivo.com/answer.xml',
          'answer_method' : "GET", 
          }

      response = p.make_call(params)
      print str(response)
      ```

      ```py Latest theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>','<auth_token>')

      response = client.calls.create(
          from_='<caller_id>',
          to_='<destination_number>',
          answer_url='https://s3.amazonaws.com/static.plivo.com/answer.xml',
          answer_method='GET', )
      print(response)
      ```
    </CodeGroup>

    ### Dial XML

    <CodeGroup>
      ```py Legacy theme={null}
      from flask import Flask, Response, request
      import plivoxml

      app=Flask(__name__)

      @app.route('/dial/caller_tone/', methods=['GET','POST'])
      def caller_tone():
      	response = plivoxml.Response()
      	params = {
      		'dialMusic' : "https://<yourdomain>.com/dial_music/"
      	}
      	Dial = response.addDial(**params)
      	number = "<destination_number>"
      	Dial.addNumber(number)
      	return Response(str(response), mimetype='text/xml')



      if __name__ == "__main__":
      	app.run(host='0.0.0.0', debug=True)
      ```

      ```py Latest theme={null}
      from flask import Flask, Response, request
      from plivo import plivoxml

      app = Flask(__name__)


      @app.route('/dial/caller_tone/', methods=['GET', 'POST'])
      def caller_tone():

         response = plivoxml.ResponseElement()
         response.add(plivoxml.DialElement(dial_music='https://<yourdomain>.com/dial_music/').add(
                 plivoxml.NumberElement('<destination_number>')))
         print(response.to_string())


      if __name__ == "__main__":
         app.run(host='0.0.0.0', debug=True)
      ```
    </CodeGroup>

    ### Conference XML

    <CodeGroup>
      ```py Legacy theme={null}
      from flask import Flask, Response, request
      import plivoxml

      app=Flask(__name__)

      @app.route('/conference/moderated/', methods=['GET','POST'])
      def moderated_conference():
      	response = plivoxml.Response()
      	params = {
      	'startConferenceOnEnter' : "false",
      	'endConferenceOnExit' : "true",
          'waitSound' : "https://<yourdomain>.com/waitmusic/"
      	}
      	conference_name = "My Room"
      	response.addConference(conference_name, **params)
      	return Response(str(response), mimetype='text/xml')



      if __name__ == "__main__":
      	app.run(host='0.0.0.0', debug=True)
      ```

      ```py Latest theme={null}
      from flask import Flask, Response, request
      from plivo import plivoxml

      app = Flask(__name__)


      @app.route('/conference/moderated/', methods=['GET', 'POST'])
      def moderated_conference():

         response = plivoxml.ResponseElement()
         response.add(
             plivoxml.ConferenceElement(
                 'My Room',
                 start_conference_on_enter=False,
                 wait_sound='https://<yourdomain>.com/waitmusic/'))

         return(response.to_string())


      if __name__ == "__main__":
         app.run(host='0.0.0.0', debug=True)
      ```
    </CodeGroup>

    ### Record API

    <CodeGroup>
      ```py Legacy theme={null}
      import plivo

      p = plivo.RestAPI(auth_id, auth_token)
      params = {'call_uuid' : call_uuid} 
              response = p.record(params)
      print str(response)
      ```

      ```py Latest theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>','<auth_token>')
      response = client.calls.record(
          call_uuid='3a2e4c90-dcee-4931-8a59-f123ab507e60', )
      print(response)
      ```
    </CodeGroup>

    ### Record XML

    <CodeGroup>
      ```py Legacy theme={null}
      from flask import Flask, Response, request
      import plivoxml

      app=Flask(__name__)

      @app.route('/record/session/', methods=['GET','POST'])
      def session():
      	response = plivoxml.Response()

      	params = {
      		'startOnDialAnswer' : "true",
      		'action' : "https://<yourdomain>.com/get_recording/",
      		'redirect' : "false"
      	}
      	response.addRecord(**params)
      	dial = response.addDial()
      	dial.addNumber("<destination_number>")
      	
      	return Response(str(response), mimetype='text/xml')

      if __name__ == "__main__":
      	app.run(host='0.0.0.0', debug=True)
      ```

      ```py Latest theme={null}
      from flask import Flask, Response, request
      from plivo import plivoxml

      app = Flask(__name__)


      @app.route('/record/session/', methods=['GET', 'POST'])
      def session():
         response = plivoxml.ResponseElement()
         response.add(
             plivoxml.RecordElement(
                 action='https://<yourdomain>.com/get_recording/',
                 start_on_dial_answer=True,
                 redirect=False))
         response.add(plivoxml.DialElement().add(plivoxml.NumberElement('<destination_number>')))
         return(response.to_string())
      ```
    </CodeGroup>
  </Tab>

  <Tab title="PHP">
    # Upgrade from PHP SDK Legacy to v4.25.0 or Latest Version

    ## Introduction

    This is a major application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      <strong>Deprecation notice:</strong> We’re deprecating Plivo PHP SDK legacy versions lower than 4.25.0 on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and voice calls may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.
    </Warning>

    ## Migrate your applications

    ### PHP version support

    The 4.x version of the Plivo SDK is compatible with PHP versions 7.3 and higher.

    Use the command **composer require plivo/plivo-php:4.25.0** to upgrade to the active version of the SDK, or **composer require plivo/plivo-php** to upgrade to the latest version.

    After you upgrade to the latest version of the SDK, you should check every program that depends on it and make changes to the syntax for several kinds of operations. Here are examples of how coding differs between the deprecated legacy version of the SDK and the latest active versions.

    ### Import the SDK

    <CodeGroup>
      ```php Legacy theme={null}
      <?php
      require 'vendor/autoload.php';
      use Plivo\RestAPI;
      ```

      ```php Latest theme={null}
      <?php
      require 'vendor/autoload.php';
      use Plivo\RestClient;
      ```
    </CodeGroup>

    ### Initialize

    <CodeGroup>
      ```php Legacy theme={null}
      $p = new RestAPI($auth_id, $auth_token);
      ```

      ```php Latest theme={null}
      $client = new RestClient("<auth_id>","<auth_token>");
      ```
    </CodeGroup>

    ### Access resources

    <CodeGroup>
      ```php Legacy theme={null}
      $response = $p->make_call($params);
      ```

      ```php Latest theme={null}
      $response = $client->calls->create($params);
      ```
    </CodeGroup>

    ### Make a call

    <CodeGroup>
      ```php Legacy theme={null}
      <?php
        require 'vendor/autoload.php';
        use Plivo\RestAPI;
        $auth_id = "<auth_id>";
        $auth_token = "<auth_token>";
        $p = new RestAPI($auth_id, $auth_token);
        $params = array(
            'to' => '2025552323',  
            'from' => '2025551212',
                    'answer_url' => "https://s3.amazonaws.com/static.plivo.com/answer.xml",
            'answer_method' => "GET"
        );
        $response = $p->make_call($params);
        print_r ($response);
      ```

      ```php Latest theme={null}
      <?php
        require 'vendor/autoload.php';
        use Plivo\RestClient;
        use Plivo\Exceptions\PlivoRestException;
        $client = new RestClient("<auth_id>","<auth_token>");
        try {
            $response = $client->calls->create(
                '+12025551212',
                ['+12025552323'],
                'https://s3.amazonaws.com/static.plivo.com/answer.xml',
            );
            print_r($response);
        }
        catch (PlivoRestException $ex) {
            print_r($ex);
        }
      ```
    </CodeGroup>

    ### Dial XML

    <CodeGroup>
      ```php Legacy theme={null}
      <?php
          require '../vendor/autoload.php';
          use Plivo\Response;

          $response = new Response();
          
          $params = array(
              'dialMusic' => "https://<yourdomain>.com/dial_music/"
          );
          
          $dial = $response->addDial($params);
          $number = "12025552323";
          $dial->addNumber($number);
          
          Header('Content-type: text/xml');
          echo($response->toXML());
      ```

      ```php Latest theme={null}
      <?php
          require '../vendor/autoload.php';
          use Plivo\Response;

          $response = new Response();
          
          $params = array(
              'dialMusic' => "https://<yourdomain>.com/dial_music/"
          );
          
          $dial = $response->addDial($params);
          $number = "12025552323";
          $dial->addNumber($number);
          
          Header('Content-type: text/xml');
          echo($response->toXML());
      ```
    </CodeGroup>

    ### Conference XML

    <CodeGroup>
      ```php Legacy theme={null}
      <?php
          require '../vendor/autoload.php';
          use Plivo\Response;

          $response = new Response();
          
          $params = array(
              'startConferenceOnEnter' => "false",
              'waitSound' => "https://<yourdomain>.com/waitmusic/"
          );
          
          $conference_name = "My Room";
          $response->addConference($conference_name, $params);
          
          Header('Content-type: text/xml');
          echo($response->toXML());
      ```

      ```php Latest theme={null}
      <?php
          require '../vendor/autoload.php';
          use Plivo\Response;

          $response = new Response();
          
          $params = array(
              'startConferenceOnEnter' => "false",
              'waitSound' => "https://<yourdomain>.com/waitmusic/"
          );
          
          $conference_name = "My Room";
          $response->addConference($conference_name, $params);
          
          Header('Content-type: text/xml');
          echo($response->toXML());
      ```
    </CodeGroup>

    ### Record API

    <CodeGroup>
      ```php Legacy theme={null}
      <?php
          require 'vendor/autoload.php';
          use Plivo\RestAPI;

          $auth_id = "<auth_id>";
          $auth_token = "<auth_token>";
          $p = new RestAPI($auth_id, $auth_token);
          $params = array('call_uuid' => $uuid); 
          $response = $p->record($params);
          print("URL : {$response['response']['url']}");
      ```

      ```php Latest theme={null}
      <?php
          require 'vendor/autoload.php';
          use Plivo\RestClient;
          use Plivo\Exceptions\PlivoRestException;
          $client = new RestClient("<auth_id>","<auth_token>");

          try {
              $response = $client->calls->startRecording(
                  'eba53b9e-8fbd-45c1-9444-696d2172fbc8'
              );
              print_r($response);
          }
          catch (PlivoRestException $ex) {
              print_r($ex);
          }
      ```
    </CodeGroup>

    ### Record XML

    <CodeGroup>
      ```php Legacy theme={null}
      <?php
          require '../vendor/autoload.php';
          use Plivo\Response;

          $response = new Response();
          
          $params = array(
              'action' => "https://<yourdomain>.com/get_recording/",
              'startOnDialAnswer' => "true",
              'redirect' => "false"
          );
          
          $response->addRecord($params);
          
          $dial = $response->addDial();
          $number = "2025552323";
          $dial->addNumber($number);
          
          Header('Content-type: text/xml');
          echo($response->toXML());
      ```

      ```php Latest theme={null}
      <?php
          require '../vendor/autoload.php';
          use Plivo\Response;

          $response = new Response();
          
          $params = array(
              'action' => "https://<yourdomain>.com/get_recording/",
              'startOnDialAnswer' => "true",
              'redirect' => "false"
          );
          
          $response->addRecord($params);
          
          $dial = $response->addDial();
          $number = "2025552323";
          $dial->addNumber($number);
          
          Header('Content-type: text/xml');
          echo($response->toXML());
      ```
    </CodeGroup>
  </Tab>

  <Tab title=".NET">
    # Upgrade from .NET SDK Legacy to v4.10.0 or Latest Version

    ## Introduction

    This is a major application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      <strong>Deprecation notice:</strong> Plivo .NET SDK legacy versions lower than v4.10.0 are being deprecated on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and voice calls may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.
    </Warning>

    ## Migrate your applications

    ### .NET version support

    The Plivo .NET SDK supports .NET applications written in C# and Visual Basic that utilize the .NET Framework version 3.5 or higher or any .NET runtime supporting [.NET Standard](https://docs.microsoft.com/en-us/dotnet/articles/standard/library) v1.4.

    Use the command **Update-Package Plivo -Version 4.10.0** to upgrade to the active version of the SDK, or **Update-Package Plivo** to upgrade to the latest version.

    After you upgrade to the latest version of the SDK, you should check every program that depends on it and make changes to the syntax for several kinds of operations. Here are examples of how coding differs between the deprecated legacy version of the SDK and the latest active versions.

    ### Import the SDK

    <CodeGroup>
      ```csharp Legacy theme={null}
      using System;
      using System.Collections.Generic;
      using RestSharp;
      using Plivo.API;
      ```

      ```csharp Latest theme={null}
      using System;
      using System.Collections.Generic;
      using Plivo;
      ```
    </CodeGroup>

    ### Initialize

    <CodeGroup>
      ```csharp Legacy theme={null}
      RestAPI plivo = new RestAPI("<auth_id>","<auth_token>");
      ```

      ```csharp Latest theme={null}
      var api = new PlivoApi("<auth_id>","<auth_token>");
      ```
    </CodeGroup>

    ### Access resources

    <CodeGroup>
      ```csharp Legacy theme={null}
      IRestResponse<Call> resp = plivo.make_call(new Dictionary<string, string>()
                  {params});
      ```

      ```csharp Latest theme={null}
      var response = api.Call.Create(params);
      ```
    </CodeGroup>

    ### Make a call

    <CodeGroup>
      ```csharp Legacy theme={null}
      using System;
      using System.Collections.Generic;
      using RestSharp;
      using Plivo.API;
      namespace make_calls
      {
         class Program
         {
             static void Main(string[] args)
             {
                 RestAPI plivo = new RestAPI("<auth_id>", "<auth_token>");
                 IRestResponse<Call> resp = plivo.make_call(new Dictionary<string, string>()
                 {
                     { "from", "2025551212" },
                     { "to", "2025552323" },
                     { "answer_url", "https://s3.amazonaws.com/static.plivo.com/answer.xml" },
                     { "answer_method","GET"},
                 });
                 Console.Write(resp.Content);
                 Console.ReadLine();
             }
         }
      }
      ```

      ```csharp Latest theme={null}
      using System;
      using System.Collections.Generic;
      using Plivo;
      using Plivo.Exception;

      namespace PlivoExamples
      {
         internal class Program
         {
             public static void Main(string[] args)
             {
                 var api = new PlivoApi("<auth_id>", "<auth_token>");
                 try
                 {
                     var response = api.Call.Create(
                         to: new List<String> { "+12025552323" },
                         from: "+12025551212",
                         answerMethod: "GET",
                         answerUrl: "https://s3.amazonaws.com/static.plivo.com/answer.xml"
                     );
                     Console.WriteLine(response);
                 }
                 catch (PlivoRestException e)
                 {
                     Console.WriteLine("Exception: " + e.Message);
                 }
             }
         }
      }
      ```
    </CodeGroup>

    ### Dial XML

    <CodeGroup>
      ```csharp Legacy theme={null}
      using System;
      using System.Collections.Generic;
      using Plivo.XML;
      namespace Plivo
      {
      	class MainClass
      	{
      		public static void Main(string[] args)
      		{
      			Plivo.XML.Response resp = new Plivo.XML.Response();
      			Plivo.XML.Dial dial = new Plivo.XML.Dial(new
      				Dictionary<string, string>() {
      				{"dialMusic", "https://<yourdomain>.com/dial_music/"}
      			});

      			dial.AddNumber("12025552323",
      				new Dictionary<string, string>() { });
      			resp.Add(dial);
      	
      			var output = resp.ToString();
      			Console.WriteLine(output);
      	
      		}
      	}
      }
      ```

      ```csharp Latest theme={null}
      using System;
      using System.Collections.Generic;
      using Plivo.XML;

      namespace Plivo
      {
      	class MainClass
      	{
      		public static void Main(string[] args)
      		{
      			Plivo.XML.Response resp = new Plivo.XML.Response();
      			Plivo.XML.Dial dial = new Plivo.XML.Dial(new
      				Dictionary<string, string>() {
      				{"dialMusic", "https://<yourdomain>.com/dial_music/"}
      			});

      			dial.AddNumber("12025552323",
      				new Dictionary<string, string>() { });
      			resp.Add(dial);
      	
      			var output = resp.ToString();
      			Console.WriteLine(output);
      	
      		}
      	}
      }
      ```
    </CodeGroup>

    ### Conference XML

    <CodeGroup>
      ```csharp Legacy theme={null}
      using System;
      using System.Collections.Generic;
      using Plivo.XML;
      namespace Plivo
      {
      	class MainClass
      	{
      		public static void Main(string[] args)
      		{
      			Plivo.XML.Response resp = new Plivo.XML.Response();
      			resp.AddConference("My room", 
                     new Dictionary<string, string>()
      			{
      				{"startConferenceOnEnter", "true"},
      				{"endConferenceOnExit", "true"},
      				{"waitSound", "https://<yourdomain>.com/waitmusic/"}
      			});
      			var output = resp.ToString();
      			Console.WriteLine(output);

      		}
      	}
      }
      ```

      ```csharp Latest theme={null}
      using System;
      using System.Collections.Generic;
      using Plivo.XML;

      namespace Plivo
      {
      	class MainClass
      	{
      		public static void Main(string[] args)
      		{
      			Plivo.XML.Response resp = new Plivo.XML.Response();
      			resp.AddConference("My room", 
                     new Dictionary<string, string>()
      			{
      				{"startConferenceOnEnter", "true"},
      				{"endConferenceOnExit", "true"},
      				{"waitSound", "https://<yourdomain>.com/waitmusic/"}
      			});
      			var output = resp.ToString();
      			Console.WriteLine(output);

      		}
      	}
      }
      ```
    </CodeGroup>

    ### Record API

    <CodeGroup>
      ```csharp Legacy theme={null}
      using System;
      using System.Collections.Generic;
      using System.Diagnostics;
      using RestSharp;
      using Plivo.API;
      namespace PlivoExamples
      {
          internal class Program
          {
              public static void Main(string[] args)
              {
                  string auth_id = "<auth_id>";
                  string auth_token = "<auth_token>";
                  RestAPI plivo = new RestAPI(auth_id, auth_token);


                  IRestResponse<Plivo.API.Record> resp = plivo.record(new Dictionary<string, string>()
                  {
                      { "call_uuid", uuid } // ID of the call
                  });
                  Debug.WriteLine(resp.Content);
               }
          }
      }
      ```

      ```csharp Latest theme={null}
      using System;
      using System.Collections.Generic;
      using Plivo;
      using Plivo.Exception;

      namespace PlivoExamples
      {
          internal class Program
          {
              public static void Main(string[] args)
              {
                  var api = new PlivoApi("<auth_id>","<auth_token>");
                  try
                  {
                      var response = api.Call.StartRecording(
                          callUuid:"10c94053-73b4-46fe-b74a-12159d1d3d60"
                      );
                      Console.WriteLine(response);
                  }
                  catch (PlivoRestException e)
                  {
                      Console.WriteLine("Exception: " + e.Message);
                  }
              }
          }
      }
      ```
    </CodeGroup>

    ### Record XML

    <CodeGroup>
      ```csharp Legacy theme={null}
      using System;
      using System.Collections.Generic;
      using Plivo.XML;
      namespace Plivo
      {
      	class MainClass
      	{
      		public static void Main(string[] args)
      		{
      			Plivo.XML.Response resp = new Plivo.XML.Response();
      			resp.AddRecord(new Dictionary<string, string>() {
      				{"action", "https://<yourdomain>.com/get_recording/"},
      				{"startOnDialAnswer", "true"},
      				{"redirect", "false"}
      			});

      			Plivo.XML.Dial dial = new Plivo.XML.Dial(new
      				Dictionary<string, string>()
      			{ });
      	
      			dial.AddNumber("12025552323",
      				new Dictionary<string, string>() { });
      			resp.Add(dial);
      	
      			var output = resp.ToString();
      			Console.WriteLine(output);
      	
      		}
      	}
      }
      ```

      ```csharp Latest theme={null}
      using System;
      using System.Collections.Generic;
      using Plivo.XML;

      namespace Plivo
      {
      	class MainClass
      	{
      		public static void Main(string[] args)
      		{
      			Plivo.XML.Response resp = new Plivo.XML.Response();
      			resp.AddRecord(new Dictionary<string, string>() {
      				{"action", "https://<yourdomain>.com/get_recording/"},
      				{"startOnDialAnswer", "true"},
      				{"redirect", "false"}
      			});

      			Plivo.XML.Dial dial = new Plivo.XML.Dial(new
      				Dictionary<string, string>()
      			{ });
      	
      			dial.AddNumber("12025552323",
      				new Dictionary<string, string>() { });
      			resp.Add(dial);
      	
      			var output = resp.ToString();
      			Console.WriteLine(output);
      	
      		}
      	}
      }
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Java">
    # Upgrade from Java Legacy to v4.8.0 or Latest Version

    ## Introduction

    This is a major application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      <strong>Deprecation notice:</strong> We’re deprecating Plivo Java SDK legacy versions lower than v4.8.0 on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and voice calls may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.
    </Warning>

    ## Migrate your applications

    ### Java version support

    The Plivo Java SDK supports OpenJDK 8 and 11 and OracleJDK 8 and 11.

    Use the command `Update-Package Plivo -Version 4.10.0` to upgrade to the active version of the SDK, or upgrade to the latest version.

    After you upgrade to the latest version of the SDK, you should check every program that depends on it and make changes to the syntax for several kinds of operations. Here are examples of how coding differs between the deprecated legacy version of the SDK and the latest active versions.

    ### Import the SDK

    <CodeGroup>
      ```java Legacy theme={null}
      import com.plivo.helper.api.client.*;
      import com.plivo.helper.xml.elements.Dial;
      ```

      ```java Latest theme={null}
      import com.plivo.api.Plivo;
      import com.plivo.api.xml.Dial;
      ```
    </CodeGroup>

    ### Initialize

    <CodeGroup>
      ```java Legacy theme={null}
      RestAPI api = new RestAPI("<auth_id>","<auth_token>", "v1");
      ```

      ```java Latest theme={null}
      Plivo.init("<auth_id>","<auth_token>");
      ```
    </CodeGroup>

    ### Accessing resources

    <CodeGroup>
      ```java Legacy theme={null}
      Call resp = api.makeCall(parameters);
      ```

      ```java Latest theme={null}
      CallCreateResponse response = Call.creator(parameters)
                      .create();
      ```
    </CodeGroup>

    ### Make a call

    <CodeGroup>
      ```java Legacy theme={null}
      package com.plivo.test;

      import java.lang.reflect.Field;
      import java.lang.reflect.Modifier;
      import java.util.LinkedHashMap;
      import com.plivo.helper.api.client.*;
      import com.plivo.helper.api.response.call.Call;
      import com.plivo.helper.exception.PlivoException;

      public class App {
          public static void main(String[] args) throws IllegalAccessException {
              String auth_id = "<auth_id>";
              String auth_token = "<auth_token>";
              RestAPI api = new RestAPI(auth_id, auth_token, "v1");

              LinkedHashMap<String, String> parameters = new LinkedHashMap<String, String>();
              parameters.put("to","2025552323"); 
              parameters.put("from","2025551212"); 
              parameters.put("answer_url","https://s3.amazonaws.com/static.plivo.com/answer.xml");
              parameters.put("answer_method","GET"); 
              try {
                  Call resp = api.makeCall(parameters);
                  System.out.println(resp);
              } catch (PlivoException e) {
                  System.out.println(e.getLocalizedMessage());
              }
          }
      }
      ```

      ```java Latest theme={null}
      using System;
      using System.Collections.Generic;
      using Plivo;
      package com.plivo.api.samples.call;

      import java.io.IOException;
      import java.util.Collections;

      import com.plivo.api.Plivo;
      import com.plivo.api.exceptions.PlivoRestException;
      import com.plivo.api.models.call.Call;
      import com.plivo.api.models.call.CallCreateResponse;

      class CallCreate {
          public static void main(String [] args) {
              Plivo.init("<auth_id>","<auth_token>");
              try {
                  CallCreateResponse response = Call.creator("+12025551212", Collections.singletonList("+12025552323"), "https://s3.amazonaws.com/static.plivo.com/answer.xml")
                      .answerMethod("GET")
                      .create();
                  System.out.println(response);
              } catch (PlivoRestException | IOException e) {
                  e.printStackTrace();
              }
          }
      }
      ```
    </CodeGroup>

    ### Dial XML

    <CodeGroup>
      ```java Legacy theme={null}
      import java.io.IOException;

      import com.plivo.helper.exception.PlivoException;
      import com.plivo.helper.xml.elements.Number;
      import com.plivo.helper.xml.elements.Dial;
      import com.plivo.helper.xml.elements.PlivoResponse;

      class CustomCallerTone {
         public static void main(String[] args) throws PlivoXmlException {
             PlivoResponse response = new PlivoResponse();
             Dial dial = new Dial();
             dial.setDialMusic("https://<yourdomain>.com/dial_music/");
             Number number = new Number("12025552323");
            

             response.append(dial);
             dial.append(number);
             System.out.println(response.toXML());
             resp.addHeader("Content-Type", "text/xml");
             resp.getWriter().print(response.toXML());;
         }
      }
      ```

      ```java Latest theme={null}
      package com.plivo.api.xml.samples.dial;

      import com.plivo.api.exceptions.PlivoXmlException;
      import com.plivo.api.xml.Dial;
      import com.plivo.api.xml.Number;
      import com.plivo.api.xml.Response;

      class CustomCallerTone {
          public static void main(String[] args) throws PlivoXmlException {
              Response response = new Response()
                      .children(
                              new Dial()
                                      .dialMusic("https://<yourdomain>.com/dial_music/")
                                      .children(
                                              new Number("12025552323")
                                      )
                      );
              System.out.println(response.toXmlString());
          }
      }
      ```
    </CodeGroup>

    ### Conference XML

    <CodeGroup>
      ```java Legacy theme={null}
      import java.io.IOException;

      import com.plivo.helper.exception.PlivoException;
      import com.plivo.helper.xml.elements.Conference;
      import com.plivo.helper.xml.elements.PlivoResponse;

      class ModeratedConference {
         public static void main(String[] args) throws PlivoException {
             PlivoResponse response = new PlivoResponse();
             Conference conference = new Conference("My Room");
             conference.setEnterSound("");
             conference.setStartConferenceOnEnter(true);
             conference.setEndConferenceOnExit(true);
             conference.setWaitSound("https://<yourdomain>.com/music/");
             response.append(conference);
             System.out.println(response.toXML());
             resp.addHeader("Content-Type", "text/xml");
             resp.getWriter().print(response.toXML());;
         }
      }
      ```

      ```java Latest theme={null}
      package com.plivo.api.xml.samples.conference;

      import com.plivo.api.exceptions.PlivoXmlException;
      import com.plivo.api.xml.Conference;
      import com.plivo.api.xml.Response;
      import com.plivo.api.xml.Speak;

      class ModeratedConference {
          public static void main(String[] args) throws PlivoXmlException {
              Response response = new Response()
                      .children(
                              new Speak("You will now be placed into a demo conference"),
                              new Conference("demo")
                                      .endConferenceOnExit(true)
                                      .startConferenceOnEnter(false)
                                      .waitSound("https://<yourdomain>.com/waitmusic/")
                      );
              System.out.println(response.toXmlString());
          }
      }
      ```
    </CodeGroup>

    ### Record API

    <CodeGroup>
      ```java Legacy theme={null}
      package plivoexample;

      import java.io.IOException;
      import java.util.LinkedHashMap;
      import javax.servlet.ServletException;
      import javax.servlet.http.HttpServlet;
      import javax.servlet.http.HttpServletRequest;
      import javax.servlet.http.HttpServletResponse;
      import com.plivo.helper.api.client.RestAPI;
      import com.plivo.helper.api.response.response.Record;
      import com.plivo.helper.exception.PlivoException;

      class recordApiAction {
         public static void main(String[] args) throws PlivoException {
             String auth_id = "<auth_id>";
             String auth_token = "<auth_token>";
             RestAPI api = new RestAPI(auth_Id, auth_Token, "v1");
             LinkedHashMap<String, String> parameters = new LinkedHashMap<String, String>();
             parameters.put("call_uuid",call_uuid);
             Record record = api.record(parameters);
             System.out.println(record);
            
         }
      }
      ```

      ```java Latest theme={null}
      package com.plivo.api.samples.call.record;

      import java.io.IOException;
      import com.plivo.api.Plivo;
      import com.plivo.api.exceptions.PlivoRestException;
      import com.plivo.api.models.call.Call;
      import com.plivo.api.models.call.actions.CallRecordCreateResponse;

      class RecordCreate {
          public static void main(String [] args) {
              Plivo.init("<auth_id>","<auth_token>");
              try {
                  CallRecordCreateResponse response = Call.recorder("eba53b9e-8fbd-45c1-9444-696d2172fbc8")
                      .record();

                  System.out.println(response);
              } catch (PlivoRestException | IOException e) {
                  e.printStackTrace();
              }
          }
      }
      ```
    </CodeGroup>

    ### Record XML

    <CodeGroup>
      ```java Legacy theme={null}
      import java.io.IOException;

      import com.plivo.helper.exception.PlivoException;
      import com.plivo.helper.xml.elements.Record;
      import com.plivo.helper.xml.elements.Dial;
      import com.plivo.helper.xml.elements.Number;
      import com.plivo.helper.xml.elements.PlivoResponse;

      class recordSession {
         public static void main(String[] args) throws PlivoException {
             response.append(record);
             response.append(dial);
             dial.append(number);
             System.out.println(response.toXML());
             resp.addHeader("Content-Type", "text/xml");
             resp.getWriter().print(response.toXML());;
         }
      }
      ```

      ```java Latest theme={null}
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
                                              new Number("12025552323")
                                      )
                      );
              System.out.println(response.toXmlString());
          }
      }
      ```
    </CodeGroup>
  </Tab>
</Tabs>
