# Source: https://plivo.com/docs/voice/concepts/signature-validation.md

# Source: https://plivo.com/docs/messaging/concepts/signature-validation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Validating Requests and Responses

> Verify webhook requests from Plivo using signature validation

All requests made by Plivo to your server URLs contain `X-Plivo-Signature-V2`, `X-Plivo-Signature-Ma-V2`, and `X-Plivo-Signature-V2-Nonce` HTTP headers. To validate a request and to verify that the request to your server originated from Plivo, you must generate a signature at your end and check that it matches with the `X-Plivo-Signature-V2` or `X-Plivo-Signature-Ma-V2` parameter in the HTTP header.

You can use either `X-Plivo-Signature-V2` or `X-Plivo-Signature-Ma-V2` to validate a signature.

<Note>
  * **X-Plivo-Signature-V2** is generated using the Auth Token of the associated account or subaccount. To validate using the **X-Plivo-Signature-V2** request header, you must generate a signature at your end using the same account or subaccount.
  * **X-Plivo-Signature-Ma-V2** is always generated using the Auth Token of the main account. To validate using the **X-Plivo-Signature-Ma-V2** request header, you must generate the signature using the main account.
</Note>

## Generating and validating the signature

You can generate the signature by calculating the keyed hash message authentication code (HMAC) with these parameters:

* Key — Your Plivo Auth Token
* Message — Base URI appended with X-Plivo-Signature-V2-Nonce. For example, if the base URI is https\://\<yourdomain>.com/answer/ and X-Plivo-Signature-V2-Nonce is 05429567804466091622, the message will be https\://\<yourdomain>.com/answer/05429567804466091622.
* Hashing Function — SHA256

## Validating signatures using the latest server SDKs

To validate and verify that the request to your server has originated from Plivo, you must compare the generated signature with X-Plivo-Signature-V2 parameter in the HTTP header and check whether they’re identical. You’ll need your Auth Token, `X-Plivo-Signature-V2-Nonce`, and the original URL of the server to which callback was sent.

## Code

<CodeGroup>
  ```py Python theme={null}
  from flask import Flask, request, make_response, url_for
  import plivo

  app = Flask(__name__)

  @app.route('/receive_sms/', methods =['GET','POST'])
  def signature():
      signature = request.headers.get('X-Plivo-Signature-V2')
      nonce = request.headers.get('X-Plivo-Signature-V2-Nonce')
      uri = url_for('signature', _external=True)
      auth_token = "<auth_token>"
      
      output = plivo.utils.validate_signature(uri,nonce,signature,auth_token)
      print(output)

      from_number = request.values.get('From') # Sender's phone numer
      to_number = request.values.get('To') # Receiver's phone number - Plivo number
      text = request.values.get('Text') # The text which was received

      print('Message received - From: %s, To: %s, Text: %s' %(from_number, to_number, text))
      return "Text received"

  if __name__ == "__main__":
      app.run(host='0.0.0.0', debug=True)
  ```

  ```rb Ruby theme={null}
  require 'sinatra'
  require 'rubygems'
  require 'plivo'
  include Plivo
  require 'uri'

  get '/receive_sms/' do
      auth_token = "<auth_token>"
      signature = request.env["HTTP_X_PLIVO_SIGNATURE_V2"]
      nonce = request.env["HTTP_X_PLIVO_SIGNATURE_V2_NONCE"]
      url = request.url
      uri = (url.split("?"))[0]
      
      output = Plivo::Utils.valid_signature?(uri,nonce,signature,auth_token)
      puts output

      from_number = params[:From]# The phone number of the person who sent the SMS
      to_number = params[:To]# Your Plivo number that will receive the SMS
      text = params[:Text]# The text which was received on your Plivo number

      puts "Message received from #{from_number} : #{ text }"
  end
  ```

  ```js Node.js theme={null}
  var plivo = require('plivo');
  var express = require('express');
  var app = express();

  app.set('port', (process.env.PORT || 5000));
  app.use(express.static(__dirname + '/public'));
  app.use(express.urlencoded({ extended: true }))

  app.all('/receive_sms/', function(req, res) {
      
      var auth_token = ('<auth_token>');
      var signature = req.get('X-Plivo-Signature-V2');
      var nonce = req.get('X-Plivo-Signature-V2-Nonce');
      var fullUrl = req.protocol + '://' + req.get('host') + req.originalUrl;

      var from_number = req.body.From;// Sender's phone number
      var to_number = req.body.To;// Receiver's phone number - Plivo number
      var text = req.body.Text;// The text which was received

      var output = plivo.validateSignature(fullUrl, nonce, signature, auth_token)
      console.log(output);
      
      console.log ('From : ' + from_number + ' To : ' + to_number + ' Text : ' + text);

  });

  app.listen(app.get('port'), function() {
      console.log('Node app is running on port', app.get('port'));
  });
  ```

  ```php PHP theme={null}
  <?php
      require 'vendor/autoload.php';
      use Plivo\Util\signatureValidation;

      $auth_token = "<auth_token>";
      $signature = $_SERVER["HTTP_X_PLIVO_SIGNATURE_V2"];
      $nonce = $_SERVER["HTTP_X_PLIVO_SIGNATURE_V2_NONCE"];
      
      $url = 'http' . (isset($_SERVER['HTTPS']) ? 's' : '') . '://' . "{$_SERVER['HTTP_HOST']}{$_SERVER['REQUEST_URI']}";
      $uri = explode('?',$url);   
      $uri1 = $uri[0];    

      $SVUtil = new signatureValidation();
      $output = $SVUtil->validateSignature($uri1,$nonce,$signature,$auth_token);
      var_export($output);
      
      $from_number = $_REQUEST["From"];// Sender's phone numer
      $to_number = $_REQUEST["To"];// Receiver's phone number - Plivo number
      $text = $_REQUEST["Text"];// The SMS text message which was received
      
      echo("Message received from $from_number : $text");
  ?>
  ```

  ```java Java theme={null}
  import java.io.IOException;
  import java.net.URLDecoder;
  import java.util.Iterator;
  import java.util.LinkedHashMap;
  import java.util.List;
  import java.util.Map;

  import com.plivo.api.util.Utils;
  import java.io.IOException;
  import java.security.InvalidKeyException;
  import java.security.NoSuchAlgorithmException;

  import javax.servlet.ServletException;
  import javax.servlet.http.HttpServlet;
  import javax.servlet.http.HttpServletRequest;
  import javax.servlet.http.HttpServletResponse;

  import org.eclipse.jetty.server.Server;
  import org.eclipse.jetty.servlet.ServletContextHandler;
  import org.eclipse.jetty.servlet.ServletHolder;

  import com.plivo.api.util.*;
  import com.plivo.api.exceptions.*;

  public class validateSignature extends HttpServlet {
      private static final long serialVersionUID = 1L;
      @Override
      protected void doPost(HttpServletRequest req, HttpServletResponse resp)
              throws ServletException, IOException {
          String auth_token = "<auth_token>";
          String signature = req.getHeader("X-Plivo-Signature-V2");
          String nonce = req.getHeader("X-Plivo-Signature-V2-Nonce");
          String url = req.getRequestURL().toString();

          try {
              Boolean isValid = Utils.validateSignature(url, nonce, signature, auth_token);
              System.out.println("Valid : " + isValid);
          } catch (Exception  e) {
              e.printStackTrace();
          }

          String from_number = req.getParameter("From");
          String to_number = req.getParameter("To");
          String text = req.getParameter("Text");
          System.out.println("From : " + from_number + " To : " + to_number + " Text : " + text);
      }

      public static void main(String[] args) throws Exception {
          String port = System.getenv("PORT");
          if(port==null)
              port ="8080";
          Server server = new Server(Integer.valueOf(port));
          ServletContextHandler context = new ServletContextHandler(ServletContextHandler.SESSIONS);
          context.setContextPath("/");
          server.setHandler(context);
          context.addServlet(new ServletHolder(new validateSignature()),"/receive_sms");
          server.start();
          server.join();
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
  	"fmt"
  	"net/http"

  	"github.com/plivo/plivo-go/v7"
  )

  func handler(w http.ResponseWriter, r *http.Request) {

  	originalurl := "https://" + r.Host + r.URL.Path
  	authToken := "<auth_token>"
  	signature := r.Header.Get("X-Plivo-Signature-V2")
  	nonce := r.Header.Get("X-Plivo-Signature-V2-Nonce")
  	fromnumber := r.FormValue("From")
  	tonumber := r.FormValue("To")
  	text := r.FormValue("Text")

  	response := plivo.ValidateSignatureV2(
  		originalurl,
  		nonce,
  		signature,
  		authToken,
  	)
  	fmt.Printf("Response: %#v\n", response)

  	print("Message Received - ", fromnumber, " ", tonumber, " ", text)
  }

  func main() {
  	http.HandleFunc("/receive_sms/", handler)
  	http.ListenAndServe(":8080", nil)
  }
  ```

  ```cs .NET theme={null}
  using System;
  using System.Collections.Generic;
  using System.Diagnostics;
  using RestSharp;
  using Plivo.Utilities;
  using Nancy;

  namespace validateSignature
  {
      public class Program : NancyModule
      {
          public Program()
          {
              Get["/receive_sms/"] = x =>
              {
                  IEnumerable<string> signature = Request.Headers["X-Plivo-Signature-V2"];
                  String[] sign = (String[])signature;
                  String actualsignature = sign[0];

                  IEnumerable<string> nonce = Request.Headers["X-Plivo-Signature-V2-Nonce"];
                  String[] key = (String[])nonce;
                  String actualnonce = key[0];

                  String auth_token = "<auth_token>";
                  String url = Request.Url.SiteBase + Request.Url.Path;

                  bool valid = Plivo.Utilities.XPlivoSignatureV2.VerifySignature(url, actualnonce, actualsignature, auth_token);
                  Debug.WriteLine("Valid : " + valid);
                  
                  String from_number = Request.Query["From"];
                  String to_number = Request.Query["To"];
                  String text = Request.Query["Text"];

                  Debug.WriteLine("From : {0}, To : {1}, Text : {2}", from_number, to_number, text);
                  Console.ReadLine(); 
                  return "OK";
              };
          }
      }
  }
  ```
</CodeGroup>
