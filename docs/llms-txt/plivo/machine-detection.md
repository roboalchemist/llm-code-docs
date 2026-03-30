# Source: https://plivo.com/docs/voice/concepts/machine-detection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Answering machine/voicemail detection

> Detect answering machines and voicemail on outbound calls to optimize agent time

You can enable answering machine or voicemail detection by including the `machine_detection` parameter when you make an outbound call using the Call API. Plivo runs machine detection in the background. When it finds a machine, Plivo makes an HTTP request, sending a `Machine` parameter with the value `true` to the `machine_detection_url` you specify. Your application can then make a decision based on this parameter. Chances are you'll use the [Transfer API](/voice/api/calls#transfer-a-call) to change the flow of the call. See the [Asynchronous machine detection](/voice/api/calls#asynchronous-machine-detection) page of our API reference documentation for details on the parameters sent.

## Getting started

1. Sign up for a free [Plivo trial account](https://cx.plivo.com/signup).
2. Check out our [server SDKs](/sdk/server/) page and install the SDK for the programming language you want to use.
3. [Buy a Plivo phone number](https://cx.plivo.com/phone-numbers) (optional). You need a Plivo phone number to receive calls. You can buy a Plivo phone number in more than 20 countries by visiting Phone Numbers > [Buy Numbers](https://cx.plivo.com/phone-numbers) in the Plivo console. Check the [Voice API coverage](https://www.plivo.com/voice/coverage/) page to see the supported countries.
4. Use a web hosting service to host your web application. Many inexpensive cloud hosting providers cost just a few dollars a month. Follow the instructions of your hosting provider to host your web application.

## Implementation

1. Copy the code below into a text file and save it.
2. Replace the placeholders `<auth_id>` and `<auth_token>` with your account’s Auth ID and Auth Token, which you can find on the overview page of the [Plivo console](https://cx.plivo.com/home).
3. Add your `from` (source) phone number, which will show up as your caller ID. All phone numbers should include country code, area code, and phone number without spaces or dashes (e.g., 14153336666).
4. Add your `to` (destination) phone number. To place bulk calls to more than one number, separate the destination phone numbers with the `<` character (e.g., 14156667777\<14157778888\<14158889999).

<Note>
  <strong>Note:</strong> If you’re using a trial account, your destination number needs to be verified with Plivo. Phone numbers can be verified at the Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page of the console.
</Note>

5. Edit the `answer_url` field and supply a URL for Plivo to request when the call is answered. This URL supplies XML code that Plivo what to do with the call.
6. Give the `answer_method` field a value of either `GET` or `POST`.
7. Edit the `machine_detection_url` field and supply a URL for Plivo to request if an answering machine or voicemail is detected on the call.
8. Give the `machine_detection_method` field a value of either `GET` or `POST`.

## Code

<CodeGroup>
  ```py Python theme={null}
  import plivo, plivoxml
  from flask import Flask

  auth_id = "<auth_id>"
  auth_token = "<auth_token>"
  p = plivo.RestAPI(auth_id, auth_token)

  # Machine detection using Call API

  params = {
      'to': '<destination_number>', # The phone numer to which the call will be placed
      'from': '<caller_id>', # The phone number to use as the caller id
      # The URL invoked by Plivo when the outbound call is answered
  ​    'answer_url': "https://<yourdomain>.com/detect/",
  ​    'answer_method': "GET", # Method to request the answer_url
  ​    'machine_detection': "true", # Used to detect if the call has been answered by a machine. Valid values are "true" and "hangup".
  ​    'machine_detection_time': "10000", # Time allotted to analyze if the call has been answered by a machine. The default value is 5000 ms.
  ​    'machine_detection_url': "https://<yourdomain>.com/machine_detection/", # A URL where machine detection parameters will be sent by Plivo.
  ​    'machine_detection_method': "GET" # Method used to invoke machine_detection_url
  }

  # Make an outbound call
  response = p.make_call(params)
  print str(response)


  # As soon as the voicemail finishes and there is a silence for minSilence
  # milliseconds, the next element in the XML is processed, without waiting for
  # the whole period of length seconds to pass

  @app.route('/detect/', methods=['GET','POST'])
  def detect():
      try:
          r = plivoxml.Response()
          params = {
              'length': "1000", # Time to wait in seconds
              'silence' : "true", # When silence is set to true, if no sound is detected for minSilence milliseconds, end the wait and continue to the next element in the XML immediately
              'minSilence' : "3000" # Only used when silence is set to true. The minimum length in milliseconds of silence that needs to be present to qualify as silence
          }
          r.addWait(**params)
          r.addSpeak("Hello Voicemail")
          print r.to_xml()
          return Response(str(r), mimetype='text/xml')
      except Exception as e:
          print '\n'.join(traceback.format_exc().splitlines())

  # Machine Detection URL example

  @app.route('/machine_detection/',methods=['POST', 'GET'])
  def machine_detection():
      from_number = request.args.get('From') # The number calling
      to_number = request.args.get('To') # The number being called
      machine = request.args.get('Machine') # This parameter will be true if a machine has been detected on the call.
      call_uuid = request.args.get('CallUUID') # The ID of the call.
      event = request.args.get('Event') # The event of the notification. When requesting the machine_detection_url, this parameter will always have the value 'MachineDetection'
      call_status = request.args.get('CallStatus') # The status of the call. This will hold the value of in-progress.

      print "From: %s " % (from_number)
      print "To: %s " % (to_number)
      print "Machine: %s " % (machine)
      print "Call UUID: %s " % (call_uuid)
      print "Event: %s " % (event)
      print "Call Status: %s " % (call_status)
      return "OK"
  ```

  ```rb Ruby theme={null}
  require 'rubygems'
  require 'sinatra'
  require 'plivo'
  include Plivo

  AUTH_ID = "<auth_id>"
  AUTH_TOKEN = "<auth_token>"
  p = RestAPI.new(AUTH_ID, AUTH_TOKEN)

  # Machine detection using Call API

  params = {
      'to' => '<caller_id>', # The phone number to which the call will be placed
      'from' => '<destination_number>', # The phone number to use as the caller id
      'answer_url' => 'https://<yourdomain>.com/detect/', # The URL requested by Plivo when the outbound call is answered
      'answer_method' => 'GET', # The method used to request the answer_url
      'machine_detection' => "true", # Used to detect if the call has been answered by a machine. The valid values are true and hangup.
      'machine_detection_time' => "10000", # Time allotted to analyze if the call has been answered by a machine. The default value is 5000 ms.
      'machine_detection_url' => "https://<yourdomain>.com/machine_detection/", # A URL where machine detection parameters will be sent by Plivo.
      'machine_detection_method' => "GET" # Method used to request machine_detection_url
  }

  # Make an outbound call
  response = p.make_call(params)
  print response

  # As soon as the voicemail finishes speaking, and there is a silence for minSilence milliseconds,
  # the next element in the XML is processed, without waiting for the whole period of length seconds to pass

  get '/detect/' do
      r = Response.new()
      params = {
          'length' => "1000", # Time to wait in seconds
          'silence' => "true", # When silence is set to true, if no sound is detected for minSilence milliseconds, end the wait and continue to the next element in the XML immediately
          'minSilence' => "3000" # Only used when silence is set to true. The minimum length in milliseconds of silence that needs to be present to qualify as silence
      }
      r.addWait(params)
      r.addSpeak("Hello Voicemail")

      puts r.to_xml()
      content_type 'text/xml'
      return r.to_s()
  end

  # Machine Detection URL example

  get '/machine_detection/' do
      r = Response.new()
      from_number = params[:From]
      to_number = params[:To]
      machine = params[:Machine]
      call_uuid = params[:CallUUID]
      event = params[:Event]
      status = params[:CallStatus]

      puts "From: #{from_number}, To: #{to_number}, Machine: #{machine}, Call UUID: #{call_uuid}, Event: #{event}, Status: #{status}"
      return "OK"
  end
  ```

  ```js Node.js theme={null}
  var express = require('express');
  var app = express();

  var plivo = require('plivo');
  var p = plivo.RestAPI({
    authId: '<auth_id>',
    authToken: '<auth_token>'
  });

  app.set('port', (process.env.PORT || 5000));

  var params = {
      'to': '<caller_id>',    // The phone numer to which the call will be placed
      'from': '<destination_number>', // The phone number to be used as the caller id
      'answer_url': 'https://<yourdomain>.com/detect/', // The URL invoked by Plivo when the outbound call is answered
      'answer_method': 'GET', // The method used to call the answer_url
      'machine_detection': "true", // Used to detect if the call has been answered by a machine. The valid values are true and hangup.
      'machine_detection_time': "5000", // Time allotted to analyze if the call has been answered by a machine. The default value is 5000 ms.
      'machine_detection_url': "https://<yourdomain>.com/machine_detection/", // A URL where machine detection parameters will be sent by Plivo.
      'machine_detection_method': "GET" // Method used to request machine_detection_url
  };

  // Make an outbound call and print the response
  p.make_call(params, function (status, response) {
      console.log('Status: ', status);
      console.log('API Response:\n', response);
  });

  app.post('/detect/', function(request, response) {
      var r = plivo.Response();
      var params = {
          'length': "1000", // Time to wait in seconds
          'silence': "true", // When silence is set to true, if no sound is detected for minSilence milliseconds, end the wait and continue to the next element in the XML immediately
          'minSilence': "3000" // Only used when silence is set to true. The minimum length in milliseconds of silence that needs to be present to qualify as silence
      };
      r.addWait(params);
      r.addSpeak("Hello Voicemail");

      console.log(r.toXML());
      response.set({'Content-Type': 'text/xml'});
      response.send(r.toXML());
  });

  app.post('/machine_detection/', function(request, response){
      var from_number = request.body.From;
      var to_number = request.body.To;
      var machine = request.body.Machine;
      var call_uuid = request.body.CallUUID;
      var event = request.body.Event;
      var status = request.body.CallStatus;

      console.log("From: ", from_number,
                  "To: ", to_number,
                  "Machine: ", machine,
                  "Call UUID: ", call_uuid,
                  "Event: ", event,
                  "Status: ", status);
      
      response.send("OK");
  });

  app.listen(app.get('port'), function() {
      console.log('Node app is running on port', app.get('port'));
  });
  ```

  ```php PHP theme={null}
  <!-- machine_detection_call.php -->

  <?php
      require 'vendor/autoload.php';
      use Plivo\RestAPI;

      $auth_id = "<auth_id>";
      $auth_token = "<auth_token>";
      $p = new RestAPI($auth_id, $auth_token);
      
      $params = array(
          'to' => '14155069431', # The phone numer to which the call will be placed
          'from' => '18583650866', # The phone number to use as the caller id
          'answer_url' => "https://<yourdomain>.com/detect.php", # The URL requested by Plivo when the outbound call is answered
          'answer_method' => "GET", # The method used to request the answer_url
          'machine_detection' => "true", # Used to detect if the call has been answered by a machine. The valid values are true and hangup.
          'machine_detection_time' => "10000", # Time allotted to analyze if the call has been answered by a machine. The default value is 5000 ms.
          'machine_detection_url' => "https://<yourdomain>.com/machine_detect.php", # A URL where machine detection parameters will be sent by Plivo.
          'machine_detection_method' => "GET" # Method used to request machine_detection_url
      );
      
      $response = $p->make_call($params);
      print_r ($response);
  ?>

  <!-- detect.php-->

  <?php
      require 'vendor/autoload.php';
      use Plivo\Response;

      $r = new Response();
      // Add Wait tag
      $params = array(
          'length' => "1000", # Time to wait in seconds
          'silence' => "true", # When silence is set to true, if no sound is detected for minSilence milliseconds, end the wait and continue to the next element in the XML immediately
          'minSilence' => "3000" # Only used when silence is set to true. The minimum length in milliseconds of silence that needs to be present to qualify as silence
      );
      $r->addWait($params);
      $r->addSpeak("Hello Voicemail");
      Header('Content-type: text/xml');
      echo($r->toXML());
  ?>

  <!-- machine_detect.php-->

  <?php
      $from_number = $_REQUEST['From'];
      $to_number = $_REQUEST['To'];
      $machine = $_REQUEST['Machine'];
      $call_uuid = $_REQUEST['CallUUID'];
      $event = $_REQUEST['Event'];
      $call_status = $_REQUEST['CallStatus'];
      error_log("From: $from_number , To: $to_number , Machine: $machine , Call UUID: $call_uuid , Event: $event , Call Status: $call_status");
      echo "OK";
  ?>
  ```

  ```java Java theme={null}
  // machineDetectionCall.java
  package plivoexample;

  import java.lang.reflect.Field;
  import java.lang.reflect.Modifier;
  import java.util.LinkedHashMap;
  import com.plivo.helper.api.client.*;
  import com.plivo.helper.api.response.call.Call;
  import com.plivo.helper.exception.PlivoException;

  public class machineDetectionCall {
      public static void main(String[] args) throws IllegalAccessException {

          String auth_id = "<auth_id>";
          String auth_token = "<auth_token>";
      
          RestAPI api = new RestAPI(auth_Id, auth_Token, "v1");
      
          LinkedHashMap<String, String> parameters = new LinkedHashMap<String, String>();
          parameters.put("to","<caller_id>"); // The phone number to which the call will be placed
          parameters.put("from","<destination_number>"); // The phone number to be used as the caller id
          parameters.put("answer_url","https://<yourdomain>.com/detect/"); // The URL requested by Plivo when the outbound call is answered
          parameters.put("answer_method","GET"); // method to request the answer_url
          parameters.put("machine_detection","true"); // Used to detect if the call has been answered by a machine. The valid values are true and hangup.
          parameters.put("machine_detection_time", "10000"); // Time allotted to analyze if the call has been answered by a machine. The default value is 5000 ms.
          parameters.put("machine_detection_url", "https://<yourdomain>.com/machine_detection/"); // A URL where machine detection parameters will be sent by Plivo.
          parameters.put("machine_detection_method", "GET"); // Method used to request machine_detection_url
      
          try {
             Call resp = api.makeCall(parameters);
             System.out.println(resp);
          } catch (PlivoException e) {
             System.out.println(e.getLocalizedMessage());
          }
      }
  }

  // detect.java
  package plivoexample;

  import java.io.IOException;
  import com.plivo.helper.exception.PlivoException;
  import com.plivo.helper.xml.elements.PlivoResponse;
  import com.plivo.helper.xml.elements.Speak;
  import com.plivo.helper.xml.elements.Wait;
  import javax.servlet.ServletException;
  import javax.servlet.http.HttpServlet;
  import javax.servlet.http.HttpServletRequest;
  import javax.servlet.http.HttpServletResponse;
  import org.eclipse.jetty.server.Server;
  import org.eclipse.jetty.servlet.ServletContextHandler;
  import org.eclipse.jetty.servlet.ServletHolder;

  public class detect extends HttpServlet {
      private static final long serialVersionUID = 1L;
      @Override
      protected void doGet(HttpServletRequest req, HttpServletResponse resp)
              throws ServletException, IOException {

          PlivoResponse response = new PlivoResponse();
          Wait wait = new Wait();
          wait.setLength(10); // Time to wait in seconds
          wait.setMinSilence(3000); // When silence is set to true, if no sound is detected for minSilence milliseconds, end the wait and continue to the next element in the XML immediately
          wait.setSilence(true); // Only used when silence is set to true. The minimum length in milliseconds of silence that needs to be present to qualify as silence
      
          Speak spk = new Speak("Hello Voicemail");
      
          try {
              response.append(wait);
              response.append(spk);
              System.out.println(response.toXML());
              resp.addHeader("Content-Type", "text/xml");
              resp.getWriter().print(response.toXML());
          } catch (PlivoException e) {
              e.printStackTrace();
          }
      }
      
      public static void main(String[] args) throws Exception {
          String port = System.getenv("PORT");
          if(port == null)
              port = "8000";
          Server server = new Server(Integer.valueOf(port));
          ServletContextHandler context = new ServletContextHandler(ServletContextHandler.SESSIONS);
          context.setContextPath("/");
          server.setHandler(context);
          context.addServlet(new ServletHolder(new detect()),"/detect/");
          context.addServlet(new ServletHolder(new machineDetection()),"/machine_detection/");
          server.start();
          server.join();
      }
  }

  // machineDetection.java
  package plivoexample;

  import java.io.IOException;
  import javax.servlet.ServletException;
  import javax.servlet.http.HttpServlet;
  import javax.servlet.http.HttpServletRequest;
  import javax.servlet.http.HttpServletResponse;

  public class machineDetection extends HttpServlet {
      private static final long serialVersionUID = 1L;

      @Override
      protected void doGet(HttpServletRequest req, HttpServletResponse resp)
              throws ServletException, IOException {
          String from_number = req.getParameter("From");
          String machine = req.getParameter("Machine");
          String to_number = req.getParameter("To");
          String call_uuid = req.getParameter("CallUUID");
          String event = req.getParameter("Event");
          String status = req.getParameter("CallStatus");
          System.out.println("From: " + from_number + " Machine: " + machine + " To: " + to_number +
                              " Call UUID: " + call_uuid + " Event: " + event + " Call Status: " + status);
          resp.getWriter().print("OK");
      }
  }
  ```

  ```cs .NET theme={null}
  // make outbound call with machine detection enabled
  using System;
  using System.Collections.Generic;
  using RestSharp;
  using Plivo.API;

  namespace send_sms
  {
      class bulk_sms
      {
          static void Main(string[] args)
          {
              RestAPI plivo = new RestAPI("<auth_id>", "Your AUTH_TOKEN");

              // Make an outbound call
              IRestResponse<Call> resp = plivo.make_call(new Dictionary<string,string>()
              {
                  {"to", "<caller_id>" }, // The phone number to which the call has to be placed
                  {"from", "<destination_number>"}, // The phone number to be used as the caller id
                  {"answer_url","https://<yourdomain>.com/detect/"}, // The URL requested by Plivo when the outbound call is answered
                  {"answer_method","GET"}, // Method to request the answer_url
                  {"machine_detection","true"}, // Used to detect if the call has been answered by a machine. The valid values are true and hangup.
                  {"machine_detection_time","10000"}, // Time allotted to analyze if the call has been answered by a machine. The default value is 5000 ms.
                  {"machine_detection_url","https://<yourdomain>.com/machine_detection/"}, // A URL where machine detection parameters will be sent by Plivo.
                  {"machine_detection_method","GET"} // Method used to request machine_detection_url
              });
      
              //Prints the message details
              Console.Write(resp.Content);
      
              Console.ReadLine();
          }
      }
  }

  // Example for answer_url and machine_detection_url
  using System;
  using System.Collections.Generic;
  using System.Diagnostics;
  using RestSharp;
  using Plivo.XML;
  using Nancy;

  namespace machine_detection
  {
      public class Program : NancyModule
      {
          public Program()
          {

              // As soon as the voicemail finishes speaking, and there is a silence for minSilence milliseconds,
              // the next element in the XML is processed, without waiting for the whole period of length seconds to pass
      
              Get["/detect/"] = x =>
              {
                  Plivo.XML.Response resp = new Plivo.XML.Response();
                  resp.AddWait(new Dictionary&lt;string, string&gt;()
                  {
                      {"length","1000"},
                      {"silence","true"},
                      {"minSilence","3000"}
                  });
      
                  resp.AddSpeak("Hello Voicemail", new Dictionary&lt;string, string&gt;() { });
      
                  Debug.WriteLine(resp.ToString());
      
                  var output = resp.ToString();
                  var res = (Nancy.Response)output;
                  res.ContentType = "text/xml";
                  return res;
              };
      
              //Machine Detection URL example
              Get["/machine_detection/"] = x =>
              {
                  String from_number = Request.Query["From"];
                  String machine = Request.Query["Machine"];
                  String to_number = Request.Query["To"];
                  String call_uuid = Request.Query["CallUUID"];
                  String event_ = Request.Query["Event"];
                  String status = Request.Query["CallStatus"];
      
                  Debug.WriteLine("From: {0}, Machine: {1}, To: {2}, Call UUID: {3}, Event: {4}, Call Status: {5}", from_number, machine, to_number, call_uuid, event_, status);
                  return "OK";
              };
          }
      }
  }
  ```
</CodeGroup>

## Sample Response

### Make Outbound call

```json  theme={null}
(201, {
        u'message': u'call fired',
        u'request_uuid': u'a52a7ae0-0551-462c-9cf0-1f79f79737c8',
        u'api_id': u'45305402-959f-11e4-b932-22000ac50fac'
    }
)
```

### XML returned by the answer\_url

```xml  theme={null}
<Response>
    <Wait minSilence="3000" silence="true" length="10"/>
    <Speak>Hello Voicemail</Speak>
</Response>
```

### Machine Detection URL output

```json  theme={null}
From : <caller_id>
To : <destination_number>
Machine : true
Call UUID : 45704ba2-959f-11e4-802f-e9b058eeb9e5
Event : MachineDetection
Call Status : in-progress
```
