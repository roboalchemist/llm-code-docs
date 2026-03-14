# Source: https://plivo.com/docs/messaging/migrate/sdk/legacy-to-active-sdk/from-legacy-to-latest.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# From Legacy to 4.x

> Migrate from legacy Plivo SDKs to the latest active versions

<Tabs>
  <Tab title="Node">
    # Upgrade from Node.js Legacy to v4.8.0 or Latest Version

    ## Introduction

    This is a major application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      <strong>Deprecation notice:</strong> We’re deprecating Plivo Node.js SDK legacy versions lower than v4.8.0 on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and messaging may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.
    </Warning>

    ## Migrate your applications

    ### Node.js version support

    The 4.x version of the Plivo SDK is compatible with Node.js versions 5.5 and higher.

    Use the command `npm install plivo@4.8.0` to upgrade to the active version of the SDK, or `npm install plivo@latest` to upgrade to the latest version.

    After you upgrade to the latest version of the SDK, you should check every program that depends on it and make changes to the syntax for several kinds of operations. Here are examples of how coding differs between the deprecated legacy version of the SDK and the latest active versions.

    ### Import the SDK

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```js  theme={null}
            var plivo = require('plivo');
            ```
          </div>
        </td>

        <td>
          <div>
            ```js  theme={null}
            var plivo = require('plivo');
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Initialize

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```js  theme={null}
            var p = plivo.RestAPI({
              authId: '<auth_id>',
              authToken: '<auth_token>'
            });
            ```
          </div>
        </td>

        <td>
          <div>
            ```js  theme={null}
            var client = new plivo.Client('<auth_id>', '<auth_token>');
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Access resources

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```js  theme={null}
            p.send_message(params, function(status, response) {
            console.log('Status: ', status);
            console.log('API Response:\n', response);
            });
            });
            ```
          </div>
        </td>

        <td>
          <div>
            ```js  theme={null}
            client.messages.create(params).then(function(response) {
                console.log(response);
            }, function(err) {
                console.error(err);
            });
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Send a message

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```js  theme={null}
            var plivo = require('plivo');
            var p = plivo.RestAPI({
                authId: '<auth_id>',
                authToken: '<auth_token>'
            });

            var params = {
                'src': '+12025551212',
                'dst': '+12025552323 ',
                'text': 'Hello, this is a sample text',
                'url': 'https://<yourdomain>.com/report/',
                'method': 'GET'
            };

            p.send_message(params, function(status, response) {
                console.log('API Response:\n', response);
            });
            ```
          </div>
        </td>

        <td>
          <div>
            ```js  theme={null}
            var plivo = require('plivo');
            (function main() {
                'use strict';
                var client = new plivo.Client('<auth_id>', '<auth_token>');
                client.messages.create({
                    src: "+12025551212",
                    dst: "+12025552323",
                    text: "Hello, this is a sample text",
                    url: "https://<yourdomain>.com/sms_status/"
                }).then(function(response) {
                    console.log(response);
                });
            })();
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Retrieve a message

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```js  theme={null}
            var plivo = require('plivo');
            var p = plivo.RestAPI({
                authId: '<auth_id>',
                authToken: '<auth_token>'
            });

            var params = {
                'record_id': '<your_message_uuid>'
            };

            p.get_message(params, function(status, response) {
                console.log('Status: ', status);
                console.log('API Response:\n', response);
                console.log('Units:', response['units']);
                console.log('Status:', response['message_state']);
            });
            ```
          </div>
        </td>

        <td>
          <div>
            ```js  theme={null}
            var plivo = require('plivo');

            (function main() {
                'use strict';
                var client = new plivo.Client('<auth_id>', '<auth_token>');
                client.messages.get('<your_message_uuid>', ).then(function(response) {
                    console.log(response);
                }, );
            })();
            ```
          </div>
        </td>
      </tr>
    </table>

    ### List all messages

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```js  theme={null}
            var plivo = require('plivo');
            var p = plivo.RestAPI({
                authId: '<auth_id>',
                authToken: '<auth_token>'
            });

            var params = {};
            p.get_messages(params, function(status, response) {
                console.log('Status: ', status);
                console.log('API Response:\n', response);
            });

            var params1 = {
                'limit': '5',
                'offset': '0'
            };
            p.get_messages(params1, function(status, response) {
                console.log('Status: ', status);
            });
            ```
          </div>
        </td>

        <td>
          <div>
            ```js  theme={null}
            var plivo = require('plivo');

            (function main() {
                'use strict';
                var client = new plivo.Client('<auth_id>', '<auth_token>');
                client.messages.list({
                    limit: 5,
                    offset: 0,
                }).then(function(response) {
                    console.log(response);
                }, );
            })();
            ```
          </div>
        </td>
      </tr>
    </table>
  </Tab>

  <Tab title="Ruby">
    # Upgrade from Ruby Legacy to v4.9.0 or Latest Version

    ## Introduction

    This is a major application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      <p><strong>Deprecation notice:</strong> We’re deprecating Plivo Ruby SDK legacy versions lower than v4.9.0 on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and messaging may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.</p>
    </Warning>

    ## Migrate your applications

    ### Ruby version support

    The Plivo Ruby SDK supports Ruby 2.0 and higher.

    Use the command `gem install plivo -v 4.9.0` to upgrade to the active version of the SDK, or `gem update plivo` to upgrade to the latest version.

    After you upgrade to the latest version of the SDK, you should check every program that depends on it and make changes to the syntax for several kinds of operations. Here are examples of how coding differs between the deprecated legacy version of the SDK and the latest active versions.

    ### Import the SDK

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```rb  theme={null}
            require 'plivo'
            ```
          </div>
        </td>

        <td>
          <div>
            ```rb  theme={null}
            require 'plivo'
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Initialize

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```rb  theme={null}
            p = RestAPI.new("<auth_id>","<auth_token>")
            ```
          </div>
        </td>

        <td>
          <div>
            ```rb  theme={null}
            api = RestClient.new("<auth_id>","<auth_token>")
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Access resources

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```rb  theme={null}
            response = p.send_message(params)
            ```
          </div>
        </td>

        <td>
          <div>
            ```rb  theme={null}
            response = api.messages.create(params)
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Send a message

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```rb  theme={null}
            require 'rubygems'
            require 'plivo'
            include Plivo

            AUTH_ID = "<auth_id>"
            AUTH_TOKEN = "<auth_token>"

            p = RestAPI.new(AUTH_ID, AUTH_TOKEN)
            params = {
                'src' => '+12025551212',
                'dst' => '+12025552323',
                'text' => 'Hello, this is a sample text',
                'url' => 'https://<yourdomain>.com/sms status/',
            }
            response = p.send_message(params)
            puts response
            ```
          </div>
        </td>

        <td>
          <div>
            ```rb  theme={null}
            require 'plivo'
            include Plivo

            api = RestClient.new('<auth_id>','<auth_token>')
            response = api.messages.create(
            	src:"+12025551212",
            	dst:"+12025552323",
            	text:"Hello, this is a sample text",
            	url:"https://<yourdomain>.com/sms status/",
            )
            puts response
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Retrieve a message

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```rb  theme={null}
            require 'rubygems'
            require 'plivo'
            include Plivo

            AUTH_ID = '<auth_id>'
            AUTH_TOKEN = '<auth_token>'
            p = RestAPI.new(AUTH_ID, AUTH_TOKEN)

            params = {'record_id' => '<your_message_uuid>'}
            response = p.get_message(params)
            ```
          </div>
        </td>

        <td>
          <div>
            ```rb  theme={null}
            require 'rubygems'
            require 'plivo'

            include Plivo

            api = RestClient.new('<auth_id>','<auth_token>')
            response = api.messages.get('<your_message_uuid>')
            puts response
            ```
          </div>
        </td>
      </tr>
    </table>

    ### List all messages

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```rb  theme={null}
            require 'rubygems'
            require 'plivo'
            include Plivo

            AUTH_ID = "<auth_id>"
            AUTH_TOKEN = "<auth_token>"
            p = RestAPI.new(AUTH_ID, AUTH_TOKEN)

            response = p.get_messages()
            puts response

            params = {
                'limit' => '5',
                'offset' => '0',
            }

            response = p.get_messages(params)

            puts response
            ```
          </div>
        </td>

        <td>
          <div>
            ```rb  theme={null}
            require 'plivo'
            include Plivo

            api = RestClient.new('<auth_id>','<auth_token>')
              response = api.messages.list(
                limit: 5,
                offset: 0,
              )
              puts response
            ```
          </div>
        </td>
      </tr>
    </table>
  </Tab>

  <Tab title="Python">
    # Upgrade from Python SDK Legacy to v4.9.0 or Latest Version

    ## Introduction

    This is a major application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      <p><strong>Deprecation notice:</strong> We’re deprecating Plivo Python SDK legacy versions lower than v4.9.0 on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and messaging may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.</p>
    </Warning>

    ## Migrate your applications

    ### Python version support

    Version 4.x of the Python SDK requires at least Python version 2.7. It will work with later versions, including Python 3.x versions.

    Use the command `pip install --upgrade plivo==4.9.0` to upgrade to the active version of the SDK, or `pip install --upgrade plivo` to upgrade to the latest version.

    After you upgrade to the latest version of the SDK, you should check every program that depends on it and make changes to the syntax for several kinds of operations. Here are examples of how coding differs between the deprecated legacy version of the SDK and the latest active versions.

    ### Import the SDK

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```py  theme={null}
            import plivo, plivoxml
            ```
          </div>
        </td>

        <td>
          <div>
            ```py  theme={null}
            import plivo
            from plivo import plivoxml
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Initialize

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```py  theme={null}
            p = plivo.RestAPI('<auth_id>','<auth_token>')
            ```
          </div>
        </td>

        <td>
          <div>
            ```py  theme={null}
            client = plivo.RestClient('<auth_id>','<auth_token>')
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Access resources

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```py  theme={null}
            response = p.send_message(params)
            ```
          </div>
        </td>

        <td>
          <div>
            ```py  theme={null}
            response = client.messages.create(params)
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Send a message

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```py  theme={null}
            import plivo

            auth_id = "<auth_id>"
            auth_token = "<auth_token>"

            p = plivo.RestAPI(auth_id, auth_token)

            params = {
                "src": "+12025551212",
                "dst": "+12025552323",
                "text": "Hello, this is a sample text",
                "url": "https://<yourdomain>.com/sms_status/",
            }

            response = p.send_message(params)

            print str(response)
            ```
          </div>
        </td>

        <td>
          <div>
            ```py  theme={null}
            import plivo

            client = plivo.RestClient("<auth_id>", "<auth_token>")
            response = client.messages.create(
                src="+12025551212",
                dst="+12025552323",
                text="Hello, this is a sample text",
                url="https://<yourdomain>.com/sms_status/",
            )
            print(response)
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Retrieve a message

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```py  theme={null}
            import plivo

            auth_id = "<auth_id>"
            auth_token = "<auth_token>"
            p = plivo.RestAPI(auth_id, auth_token)
            params = {"message_uuid": "<your_message_uuid>"}

            response = p.get_message(params)

            print str(response)
            ```
          </div>
        </td>

        <td>
          <div>
            ```py  theme={null}
            import plivo

            client = plivo.RestClient("<auth_id>", "<auth_token>")
            response = client.messages.get(message_uuid="<your_message_uuid>")
            print(response)
            ```
          </div>
        </td>
      </tr>
    </table>

    ### List all messages

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```py  theme={null}
            import plivo

            auth_id = "<auth_id>"
            auth_token = "<auth_token>"
            p = plivo.RestAPI(auth_id, auth_token)

            response = p.get_messages()

            print str(response)

            params = {
                "limit": "5",
                "offset": "0",
            }

            response = p.get_messages(params)
            print str(response)
            ```
          </div>
        </td>

        <td>
          <div>
            ```py  theme={null}
            import plivo

            client = plivo.RestClient("<auth_id>", "<auth_token>")
            response = client.messages.list(
                limit=5,
                offset=0,
            )
            print(response)
            ```
          </div>
        </td>
      </tr>
    </table>
  </Tab>

  <Tab title="PHP">
    # Upgrade from PHP SDK Legacy to v4.25.0 or Latest Version

    ## Introduction

    This is a major application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      <p><strong>Deprecation notice:</strong> We’re deprecating Plivo PHP SDK legacy versions lower than 4.25.0 on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and messaging may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.</p>
    </Warning>

    ## Migrate your applications

    ### PHP version support

    The 4.x version of the Plivo SDK is compatible with PHP versions 7.3 and higher.

    Use the command `composer require plivo/plivo-php:4.25.0` to upgrade to the active version of the SDK, or `composer require plivo/plivo-php` to upgrade to the latest version.

    After you upgrade to the latest version of the SDK, you should check every program that depends on it and make changes to the syntax for several kinds of operations. Here are examples of how coding differs between the deprecated legacy version of the SDK and the latest active versions.

    ### Import the SDK

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```php  theme={null}
            <?php
            require 'vendor/autoload.php';
            use Plivo\RestAPI;
            ```
          </div>
        </td>

        <td>
          <div>
            ```php  theme={null}
            <?php
            require 'vendor/autoload.php';
            use Plivo\RestClient;
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Initialize

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```php  theme={null}
            $p = new RestAPI($auth_id, $auth_token);
            ```
          </div>
        </td>

        <td>
          <div>
            ```php  theme={null}
            $client = new RestClient("<auth_id>","<auth_token>");
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Access resources

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```php  theme={null}
            $response = $p->send_message($params);
            ```
          </div>
        </td>

        <td>
          <div>
            ```php  theme={null}
            $response = $client->messages->create($params);
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Send a message

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```php  theme={null}
            <?php
                require 'vendor/autoload.php';
                use Plivo\RestAPI;
                $auth_id = '<auth_id>';
                $auth_token = '<auth_token>';

                $p = new RestAPI($auth_id, $auth_token);
                $params = array(
                    'src' => '+12025551212', 
                    'dst' => '+12025552323',
                    'text' => 'Hello, this is a sample text',
                    'url' => 'https://<yourdomain>.com/sms_status/'
                );
                $response = $p->send_message($params);
                
                echo "Response : ";
                print_r ($response['response']);
            ?>

            ```
          </div>
        </td>

        <td>
          <div>
            ```php  theme={null}
            <?php
            require 'vendor/autoload.php';
            use Plivo\RestClient;

            $client = new RestClient('<auth_id>','<auth_token>');
            $response = $client->messages->create(
              [  
                "src" => "+12025551212",
                "dst" => "+12025552323",
                "text"  =>"Hello, this is a sample text",
                "url"=>"https://<yourdomain>.com/sms_status/"
             ]
            );
            print_r($response);
            ?>
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Retrieve a message

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```php  theme={null}
            <?php
                require 'vendor/autoload.php';
                use Plivo\RestAPI;
                $auth_id = '<auth_id>';
                $auth_token = '<auth_token>';
                $p = new RestAPI($auth_id, $auth_token);

                $params = array('record_id' => '<your_message_uuid>');
                $response = $p->get_message($params);
                
                print_r ($response['response']);
            ?>
            ```
          </div>
        </td>

        <td>
          <div>
            ```php  theme={null}
            <?php
            require 'vendor/autoload.php';
            use Plivo\RestClient;

            $client = new RestClient('<auth_id>','<auth_token>');
            $response = $client->messages->get('<your_message_uuid>');
            print_r($response);
            ?>
            ```
          </div>
        </td>
      </tr>
    </table>

    ### List all messages

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```php  theme={null}
            <?php
                require 'vendor/autoload.php';
                use Plivo\RestAPI;
                $auth_id = '<auth_id>';
                $auth_token = '<auth_token>';
                $p = new RestAPI($auth_id, $auth_token);

                $response = $p->get_messages();


                print_r ($response['response']);
                
                $params = array(
                    'limit' => '5', 
                    'offset' => '0',
                );
                
                $response = $p->get_messages($params);
                print_r ($response['response']);
            ?>
            ```
          </div>
        </td>

        <td>
          <div>
            ```php  theme={null}
            <?php
            require 'vendor/autoload.php';
            use Plivo\RestClient;

            $client = new RestClient('<auth_id>','<auth_token>');
            $response = $client->messages->list(
              [
                'limit' => 5,
                'offset' => 0
              ]
            );
            print_r($response);
            ?>
            ```
          </div>
        </td>
      </tr>
    </table>
  </Tab>

  <Tab title=".NET">
    # Upgrade from .NET SDK Legacy to v4.10.0 or Latest Version

    ## Introduction

    This is a major application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      <p><strong>Deprecation notice:</strong> We’re deprecating Plivo .NET SDK legacy versions lower than v4.10.0 on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and messaging may fail intermittently.  Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.</p>
    </Warning>

    ## Migrate your applications

    ### .NET version support

    The Plivo .NET SDK supports .NET applications written in C# and Visual Basic that utilize the .NET Framework version 3.5 or higher or any .NET runtime supporting [.NET Standard](https://docs.microsoft.com/en-us/dotnet/articles/standard/library) v1.4.

    Use the command `Update-Package Plivo -Version 4.10.0` to upgrade to the active version of the SDK, or `Update-Package Plivo` to upgrade to the latest version.

    After you upgrade, you should check every program that depends on the SDK and make changes to the syntax for several kinds of operations. Here are examples of how coding differs between the deprecated legacy versions of the SDK and the latest active versions.

    ### Import the SDK

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```cs  theme={null}
            using System;
            using System.Collections.Generic;
            using RestSharp;
            using Plivo.API;
            ```
          </div>
        </td>

        <td>
          <div>
            ```cs  theme={null}
            using System;
            using System.Collections.Generic;
            using Plivo;
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Initialize

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```cs  theme={null}
            RestAPI plivo = new RestAPI("<auth_id>","<auth_token>");
            ```
          </div>
        </td>

        <td>
          <div>
            ```cs  theme={null}
            var api = new PlivoApi("<auth_id>","<auth_token>");
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Access resources

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```cs  theme={null}
            IRestResponse < MessageResponse > resp =
              plivo.send_message(new Dictionary < string, string > () {params});
            ```
          </div>
        </td>

        <td>
          <div>
            ```cs  theme={null}
            var response = api.Message.Create(params);
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Send a message

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```cs  theme={null}
            using System;
            using System.Collections.Generic;
            using System.Reflection;
            using RestSharp;
            using Plivo.API;
            namespace Send_Sms
            {
                class Program
                {
                    static void Main(string[] args)
                    {
                        RestAPI plivo = new RestAPI("<auth_id>", "<auth_token>");
                        IRestResponse<MessageResponse> resp = plivo.send_message(new Dictionary<string, string>()
                        {
                            { "src", "+12025551212" },
                            { "dst", "+12025552323" },
                            { "text", "Hello, this is a sample text" }, 
                            { "url", "https://<yourdomain>.com/sms_status/"}
                             });
                        Console.Write(resp.Content);
                       Console.ReadLine();
                    }
                }
            }
            ```
          </div>
        </td>

        <td>
          <div>
            ```cs  theme={null}
            using System;
            using System.Collections.Generic;
            using Plivo;

            namespace PlivoExamples
            {
                internal class Program
                {
                    public static void Main(string[] args)
                    {
                        var api = new PlivoApi("<auth_id>","<auth_token>");
                        var response = api.Message.Create(
                            src: "+12025551212",
                            dst: "+12025552323",
                            text: "Hello, this is a sample text",
                            url: "https://<yourdomain>.com/sms_status/"
                            );
                        Console.WriteLine(response);
                    }
                }
            }
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Retrieve a message

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```cs  theme={null}
            using System;
            using System.Collections.Generic;
            using System.Reflection;
            using RestSharp;
            using Plivo.API;

            namespace Get_Details
            {
                class Program
                {
                    static void Main(string[] args)
                    {
                        RestAPI plivo = new RestAPI("<auth_id>", "<auth_token>");
                        IRestResponse<Message> resp = plivo.get_message(new Dictionary<string, string>()
                        {
                            { "record_id", "<your_message_uuid>" }
                        });

                        Console.Write(resp.Content);
                
                        Console.ReadLine();
                    }
                }
            }
            ```
          </div>
        </td>

        <td>
          <div>
            ```cs  theme={null}
            using System;
            using Plivo;
            using Plivo.Exception;

            namespace PlivoExamples
            {
                internal class Program
                {
                    public static void Main(string[] args)
                    {
                        var api = new PlivoApi("<auth_id>","<auth_token>");
                            var response = api.Message.Get(
                                messageUuid: "<your_message_uuid>"
                            );
                            Console.WriteLine(response);
                    }
                }
            }
            ```
          </div>
        </td>
      </tr>
    </table>

    ### List all messages

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```cs  theme={null}
            using System;
            using System.Collections.Generic;
            using System.Reflection;
            using RestSharp;
            using Plivo.API;

            namespace GetAllDetails
            {
                class Program
                {
                    static void Main(string[] args)
                    {
                        RestAPI plivo = new RestAPI("<auth_id>","<auth_token>");
                        IRestResponse<MessageList> resp = plivo.get_messages();

                        Console.Write(resp.Content);
                 
                        IRestResponse<MessageList> response = plivo.get_messages(new Dictionary<string, string>()
                        {
                            { "limit", "10" },
                            { "offset", "0" }
                        });
                
                        Console.WriteLine(response.Content);
                
                        Console.ReadLine();
                    }
                }
            }
            ```
          </div>
        </td>

        <td>
          <div>
            ```cs  theme={null}
            using System;
            using System.Collections.Generic;
            using Plivo;

            namespace PlivoExamples
            {
                internal class Program
                {
                    public static void Main(string[] args)
                    {
                        var api = new PlivoApi("<auth_id>","<auth_token>");

                            var response = api.Message.List(
                                limit:10,
                                offset:0
                            );
                            Console.WriteLine(response);
                    }
                }
            }
            ```
          </div>
        </td>
      </tr>
    </table>
  </Tab>

  <Tab title="Java">
    # Upgrade from Java Legacy to v4.8.0 or Latest Version

    ## Introduction

    This is a major application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      <p><strong>Deprecation notice:</strong> We’re deprecating Plivo Java SDK legacy versions lower than v4.8.0 on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and messaging may fail intermittently.  Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.</p>
    </Warning>

    ## Migrate your applications

    ### Java version support

    The Plivo Java SDK supports OpenJDK 8 and 11 and OracleJDK 8 and 11.

    Use the command `Update-Package Plivo -Version 4.10.0` to upgrade to the active version of the SDK, or upgrade to the latest version.

    After you upgrade to the latest version of the SDK, you should check every program that depends on it and make changes to the syntax for several kinds of operations. Here are examples of how coding differs between the deprecated legacy version of the SDK and the latest active versions.

    ### Import the SDK

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```java  theme={null}
            import com.plivo.helper.api.client.*;
            import com.plivo.helper.xml.elements.Dial;
            ```
          </div>
        </td>

        <td>
          <div>
            ```java  theme={null}
            import com.plivo.api.Plivo;
            import com.plivo.api.xml.Dial;
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Initialize

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```java  theme={null}
            RestAPI api = new RestAPI("<auth_id>","<auth_token>", "v1");
            ```
          </div>
        </td>

        <td>
          <div>
            ```java  theme={null}
            Plivo.init("<auth_id>","<auth_token>");
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Access resources

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```java  theme={null}
            Message resp = api.makeCall(parameters);
            ```
          </div>
        </td>

        <td>
          <div>
            ```java  theme={null}
            MessageCreateResponse response = Message.creator(parameters)
                .create();
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Send a message

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```java  theme={null}
            package com.plivo.test;

            import java.util.LinkedHashMap;
            import com.plivo.helper.api.client.*;
            import com.plivo.helper.api.response.message.MessageResponse;
            import com.plivo.helper.exception.PlivoException;

            public class SendMessage {
                public static void main(String[] args) {
                    String authId = "<auth_id>";
                    String authToken = "<auth_token>";
                    RestAPI api = new RestAPI(authId, authToken, "v1");

                    LinkedHashMap<String, String> parameters = new LinkedHashMap<String, String>();
                    parameters.put("src", "12025551212"); 
                    parameters.put("dst", "12025552323"); 
                    parameters.put("text", "Hello, this is a test message"); 
                    parameters.put("url", "https://<yourdomain>.com/sms_status/");
                    try {
                        MessageResponse msgResponse = api.sendMessage(parameters);
                        System.out.println(msgResponse);
                    } catch (PlivoException e) {
                        System.out.println(e.getLocalizedMessage());
                    }
                }
            }
            ```
          </div>
        </td>

        <td>
          <div>
            ```java  theme={null}
            import java.io.IOException;
            import java.net.URL;
            import java.util.Collections;

            import com.plivo.api.Plivo;
            import com.plivo.api.exceptions.PlivoRestException;
            import com.plivo.api.models.message.Message;
            import com.plivo.api.models.message.MessageCreateResponse;

            class MessageCreate
            {
                public static void main(String [] args)
                {
                    Plivo.init("<auth_id>","<auth_token>");
                    try
                    {
                        MessageCreateResponse response = Message.creator("+12025551212","+12025552323",
                                "Hello, this is a test message")
                                .url(new URL("https://<yourdomain>.com/sms_status/") )
                                .create();
                        System.out.println(response);
                    }
                    catch (PlivoRestException | IOException e)
                    {
                        e.printStackTrace();
                    }
                }
            }
            ```
          </div>
        </td>
      </tr>
    </table>

    ### Retrieve a message

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```java  theme={null}
            package com.plivo.test;

            import java.util.LinkedHashMap;
            import com.plivo.helper.api.client.*;
            import com.plivo.helper.api.response.message.MessageResponse;
            import com.plivo.helper.exception.PlivoException;

            public class GetDetails {
                public static void main(String[] args) {
                    String authId = "<auth_id>";
                    String authToken = "<auth_token>";
                    RestAPI api = new RestAPI(authId, authToken, "v1");

                    LinkedHashMap<String, String> parameters = new LinkedHashMap<String, String>();
                    parameters.put("record_id", "<your_message_uuid>");
                    try {
                        Message msg = api.getMessage(parameters);
                        System.out.println(msg);
                    } catch (PlivoException e) {
                        System.out.println(e.getLocalizedMessage());
                    }
                }
            }
            ```
          </div>
        </td>

        <td>
          <div>
            ```java  theme={null}
            import java.io.IOException;
            import com.plivo.api.Plivo;
            import com.plivo.api.exceptions.PlivoRestException;
            import com.plivo.api.models.message.Message;

            class MessageGet
            {
                public static void main(String [] args)
                {
                    Plivo.init("<auth_id>", "<auth_token>");
                    try
                    {
                        Message response = Message.getter("<your_message_uuid>")
                                .get();

                        System.out.println(response);
                
                    }
                    catch (PlivoRestException | IOException e)
                    {
                        e.printStackTrace();
                    }
                }
            }
            ```
          </div>
        </td>
      </tr>
    </table>

    ### List all messages

    <table>
      <tr>
        <td>
          **Legacy**
        </td>

        <td>
          **Latest**
        </td>
      </tr>

      <tr>
        <td>
          <div>
            ```java  theme={null}
            package com.plivo.test;

            import java.util.LinkedHashMap;
            import com.plivo.helper.api.client.*;
            import com.plivo.helper.api.response.message.MessageResponse;
            import com.plivo.helper.exception.PlivoException;

            public class GetAllDetails {
                public static void main(String[] args) {
                    String authId = "<auth_id>";
                    String authToken = "<auth_token>";
                    RestAPI api = new RestAPI(authId, authToken, "v1");
                    try {
                        MessageFactory msg = api.getMessages();

                        System.out.println(msg);
                    } catch (PlivoException e) {
                        System.out.println(e.getLocalizedMessage());
                    }
                
                    LinkedHashMap<String, String> parameters = new LinkedHashMap<String, String>();
                    parameters.put("limit", "5"); 
                    parameters.put("offset", "0"); 
                    try {
                        MessageFactory msg = api.getMessages(parameters);
                        System.out.println(msg);
                    } catch (PlivoException e) {
                        System.out.println(e.getLocalizedMessage());
                    }
                }
            }
            ```
          </div>
        </td>

        <td>
          <div>
            ```java  theme={null}
            import java.io.IOException;

            import com.plivo.api.Plivo;
            import com.plivo.api.exceptions.PlivoRestException;
            import com.plivo.api.models.message.Message;
            import com.plivo.api.models.base.ListResponse;


            class GetAllMessageList
            {
                public static void main(String [] args)
                {
                    Plivo.init("<auth_id>","<auth_token>");
                    try
                    {
                        ListResponse<Message> response = Message.lister()
                                .limit(5)
                                .offset(0)
                                .list();
                        System.out.println(response);
                    }
                    catch (PlivoRestException | IOException e)
                    {
                        e.printStackTrace();
                    }
                }
            }
            ```
          </div>
        </td>
      </tr>
    </table>
  </Tab>
</Tabs>
