# Source: https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions.md.txt

# Data API Code Snippets

## Instructions

The interactive code snippets tool lets you easily test API requests and generate code samples specific to those requests. For any given method, the tool shows code snippets for one or more use cases, and each use case describes a common way of calling that method. For example, you can call the `channels.list` method to retrieve data about a specific channel or about the current user's channel.

### Execute API requests

You can execute requests by clicking the **Execute** button next to the list of request parameters. If you have not previously authorized the application to submit API requests on your behalf, you will be prompted to do so. As an extra precaution, if your request performs a write operation -- inserting, updating, or deleting resources associated with your channel -- you will be asked to confirm that you want to execute the request before it actually executes.

![](https://developers.google.com/static/youtube/images/confirm-interactive-snippet-request.png)

### Toggle code snippets and full samples

For each use case, the tool shows a code snippet that identifies code specific to the particular method being called. Each snippet identifies the method being called as well as parameter and property values used in the API request.

In addition, the tool also shows a full code sample that puts that code snippet into a template that defines boilerplate functions for authorizing API requests and constructing API requests. You can use the slider above the samples to switch between the snippet and the full sample:

![](https://developers.google.com/static/youtube/images/interactive-snippet-slider.png)

#### Run full code samples locally

The full code samples are designed to be copied and run locally. Please note the following prerequisites and set up steps for running the full code samples:
Java

**Prerequisites**

- Java 1.7 or greater
- Gradle 2.3 or greater

**Set up your project and run code samples**

1. Create a project in the [API Console](https://console.cloud.google.com/) and set up credentials for a web application. Set the authorized redirect URIs as appropriate.

2. Follow the instructions in the [API Java Quickstart Guide](https://developers.google.com/youtube/v3/quickstart/java) for preparing your project, but replace the contents of the default `build.gradle` file with the following code:

   ```
   apply plugin: 'java'
   apply plugin: 'application'

   mainClassName = 'ApiExample'
   sourceCompatibility = 1.7
   targetCompatibility = 1.7
   version = '1.0'

   repositories {
       mavenCentral()
   }

   dependencies {
       compile 'com.google.api-client:google-api-client:1.22.0'
       compile 'com.google.oauth-client:google-oauth-client-jetty:1.22.0'
       compile 'com.google.apis:google-api-services-youtube:v3-rev182-1.22.0'
       compile group: 'com.google.code.gson', name: 'gson', version: '1.7.2'
       compile group: 'com.fasterxml.jackson.core', name: 'jackson-databind', version: '2.4.4'
   }

   compileJava {
       options.compilerArgs << "-Xlint:unchecked" << "-Xlint:deprecation"
   }
   ```
3. From your working directory, save the `client_secrets.json` file associated with your credentials to `src/main/resources/client_secret.json`.

4. From your working directory, copy the full code sample to `src/main/java/ApiExample.java`. (The class name in each sample is `ApiExample` so that you do not need to modify the `build.gradle` file to run different samples.)

5. Run the sample from the command line:

   ```
   gradle -q run
   ```
6. Most samples print something to `STDOUT`. You can also check the YouTube website to see the effects of requests that write data, such as requests that create playlists or channel sections.

JavaScript

1. Create a project in the [API Console](https://console.cloud.google.com/) and set up credentials for a web application. Set the authorized JavaScript origins to identify the URL from which you'll be sending requests (e.g. `http://localhost`).

2. Copy the full code sample to a local file accessible to your web server (e.g. `/var/www/html/example.html`).

3. Find the line in the code sample that sets the client ID to be used for the request, and replace the value with the client ID for your credentials:

   ```
   gapi.client.init({
       'clientId': 'REPLACE_ME',
   ```
4. Open the file in your browser (e.g. `http://localhost/example.html`). It is recommended to use a browser with a debugging console, such as Google Chrome.

5. Authorize the request if necessary. If the request is authorized, the debugging console should display the API response to the request as a JSON object.

Node.js

**Prerequisites**

- Node.js must be installed.
- The [npm](https://www.npmjs.com/) package management tool (comes with Node.js).
- The Google APIs Client Library for Node.js:  

  ```
  npm install googleapis --save
  ```
- Access to the internet and a web browser.
- A Google account.

**Set up your project and run code samples**

1. Create a project in the [API Console](https://console.cloud.google.com/) and set up OAuth 2.0 credentials in the [Google API Console](https://console.cloud.google.com/). When setting up your credentials, set the application type to **Other**.

2. Save the `client_secret.json` file associated with your credentials to a local file.

3. Copy the full code sample to a local file in the same directory as the `client_secret.json` file (or modify the sample to correctly identify that file's location.

4. Run the sample from the command line:

   ```
   node sample.js
   ```
5. Most samples print something to `STDOUT` or, for web application examples, to the web page you're viewing. You can also check the YouTube website to see the effects of requests that write data, such as requests that create playlists or channel sections.

Python

**Prerequisites**

- Python 2.6 or greater
- The pip package management tool
- The Google APIs Client Library for Python:  

  ```
  pip install --upgrade google-api-python-client
  ```
- The google-auth, google-auth-oauthlib, and google-auth-httplib2 for user authorization.  

  ```
  pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
  ```
- The Flask Python web application framework (if you are running the Python samples for web server applications).  

  ```
  pip install --upgrade flask
  ```
- The requests HTTP library.  

  ```
  pip install --upgrade requests
  ```

**Set up your project and run code samples**

1. Create a project in the [API Console](https://console.cloud.google.com/) and set up OAuth 2.0 credentials in the [Google API Console](https://console.cloud.google.com/). When setting up your credentials, set the application type to **Web application** for samples that use the Flask Python web application framework and also set authorized redirect URIs for those credentials. Otherwise, set the application type to **Other**.

2. Save the `client_secret.json` file associated with your credentials to a local file.

3. Copy the full code sample to a local file in the same directory as the `client_secret.json` file (or modify the sample to correctly identify that file's location.

4. Run the sample from the command line:

   ```
   python sample.py
   ```  
   **Note for web server application examples:**   

   If you are running the Python samples for web server applications, then running the script starts a local web server. To actually execute the API request, you need to go to the served web page in a browser. For example, the Python samples that use the Flask web application framework contain a line like this:  

   `app.run('localhost', 8080, debug=True)`  

   This code starts a local web server at `http://localhost:8080`. However, the script doesn't try to execute an API request until you actually navigate to `http://localhost:8080` in a browser. (The URL for your local server must also be set as an authorized redirect URI for your authorization credentials.)
5. Most samples print something to `STDOUT` or, for web application examples, to the web page you're viewing. You can also check the YouTube website to see the effects of requests that write data, such as requests that create playlists or channel sections.

PHP

**Prerequisites**

- PHP 5.4 or greater with the command-line interface (CLI) and JSON extension installed.
- The [Composer](https://getcomposer.org/) dependency management tool.
- The Google APIs Client Library for PHP:  

  ```
  php composer.phar require google/apiclient:^2.0
  ```

**Set up your project and run code samples**

1. Create a project in the [API Console](https://console.cloud.google.com/) and set up OAuth 2.0 credentials in the [Google API Console](https://console.cloud.google.com/). When setting up your credentials, set the application type to **Other**.

2. Save the `client_secret.json` file associated with your credentials to a local file.

3. Copy the full code sample to a local file in the same directory as the `client_secret.json` file (or modify the sample to correctly identify that file's location.

4. Run the sample from the command line:

   ```
   php sample.php
   ```
5. Most samples print something to `STDOUT` or, for web application examples, to the web page you're viewing. You can also check the YouTube website to see the effects of requests that write data, such as requests that create playlists or channel sections.

Ruby

**Prerequisites**

- Ruby 2.0 or greater
- The Google APIs Client Library for Ruby:  

  ```
  gem install google-api-client
  ```

**Set up your project and run code samples**

1. Create a project in the [API Console](https://console.cloud.google.com/) and set up OAuth 2.0 credentials in the [Google API Console](https://console.cloud.google.com/). When setting up your credentials, set the application type to **Other**.

2. Save the `client_secret.json` file associated with your credentials to a local file.

3. Copy the full code sample to a local file in the same directory as the `client_secret.json` file (or modify the sample to correctly identify that file's location.

4. Run the sample from the command line:

   ```
   ruby sample.rb
   ```
5. Most samples print something to `STDOUT` or, for web application examples, to the web page you're viewing. You can also check the YouTube website to see the effects of requests that write data, such as requests that create playlists or channel sections.

Apps Script Follow the instructions for enabling [advanced Google services](https://developers.google.com/apps-script/guides/services/advanced) to enable YouTube features. Go

1. Create a project in the [API Console](https://console.cloud.google.com/) and set up OAuth 2.0 credentials in the [Google API Console](https://console.cloud.google.com/). When setting up your credentials, set the application type to **Other**.

2. Save the `client_secret.json` file associated with your credentials to a local file.

3. Copy the full code sample to a local file in the same directory as the `client_secret.json` file (or modify the sample to correctly identify that file's location.

4. Run the sample from the command line:

   ```
   go run sample.go
   ```
5. Most samples print something to `STDOUT` or, for web application examples, to the web page you're viewing. You can also check the YouTube website to see the effects of requests that write data, such as requests that create playlists or channel sections.

### Use boilerplate functions

As noted above, full code samples use boilerplate code for authorizing and constructing API requests. For example, the `build_resource` function in Python samples uses a dictionary that maps resource properties to their values to construct a resource that can be inserted or updated. Similar functions are provided for JavaScript, PHP, Ruby, Go, and Apps Script.

For example, the tabs below show how the boilerplate functions for building resources would be called to construct a `playlist` resource. Note that the boilerplate functions do not need to know what type of resource is being created.
JavaScript  

```
function createResource(properties) {
  var resource = {};
  var normalizedProps = properties;
  for (var p in properties) {
    var value = properties[p];
    if (p && p.substr(-2, 2) == '[]') {
      var adjustedName = p.replace('[]', '');
      if (value) {
        normalizedProps[adjustedName] = value.split(',');
      }
      delete normalizedProps[p];
    }
  }
  for (var p in normalizedProps) {
    // Leave properties that don't have values out of inserted resource.
    if (normalizedProps.hasOwnProperty(p) && normalizedProps[p]) {
      var propArray = p.split('.');
      var ref = resource;
      for (var pa = 0; pa < propArray.length; pa++) {
        var key = propArray[pa];
        if (pa == propArray.length - 1) {
          ref[key] = normalizedProps[p];
        } else {
          ref = ref[key] = ref[key] || {};
        }
      }
    };
  }
  return resource;
}
var resource = createResource({
    'snippet.title': 'Sample playlist ',
    'snippet.description': 'This is a sample playlist description.',
    'snippet.tags[]': 'JavaScript code, interactive',
    'snippet.defaultLanguage': '',
    'status.privacyStatus': 'private'
}
```
Python  

```
# Build a resource based on a list of properties given as key-value pairs.
# Leave properties with empty values out of the inserted resource.
def build_resource(properties):
  resource = {}
  for p in properties:
    # Given a key like "snippet.title", split into "snippet" and "title", where
    # "snippet" will be an object and "title" will be a property in that object.
    prop_array = p.split('.')
    ref = resource
    for pa in range(0, len(prop_array)):
      is_array = False
      key = prop_array[pa]
      # Convert a name like "snippet.tags[]" to snippet.tags, but handle
      # the value as an array.
      if key[-2:] == '[]':
        key = key[0:len(key)-2:]
        is_array = True
      if pa == (len(prop_array) - 1):
        # Leave properties without values out of inserted resource.
        if properties[p]:
          if is_array:
            ref[key] = properties[p].split(',')
          else:
            ref[key] = properties[p]
      elif key not in ref:
        # For example, the property is "snippet.title", but the resource does
        # not yet have a "snippet" object. Create the snippet object here.
        # Setting "ref = ref[key]" means that in the next time through the
        # "for pa in range ..." loop, we will be setting a property in the
        # resource's "snippet" object.
        ref[key] = {}
        ref = ref[key]
      else:
        # For example, the property is "snippet.description", and the resource
        # already has a "snippet" object.
        ref = ref[key]
  return resource

resource = build_resource({
    'snippet.title': 'Sample playlist ',
    'snippet.description': 'This is a sample playlist description.',
    'snippet.tags[]': 'Python code, interactive',
    'snippet.defaultLanguage': '',
    'status.privacyStatus': 'private'}
  
```
PHP

```
// Add a property to the resource.
function addPropertyToResource(&$ref, $property, $value) {
    $keys = explode(".", $property);
    $is_array = false;
    foreach ($keys as $key) {
        // Convert a name like "snippet.tags[]" to "snippet.tags" and
        // set a boolean variable to handle the value like an array.
        if (substr($key, -2) == "[]") {
            $key = substr($key, 0, -2);
            $is_array = true;
        }
        $ref = &$ref[$key];
    }

    // Set the property value. Make sure array values are handled properly.
    if ($is_array && $value) {
        $ref = $value;
        $ref = explode(",", $value);
    } elseif ($is_array) {
        $ref = array();
    } else {
        $ref = $value;
    }
}

// Build a resource based on a list of properties given as key-value pairs.
function createResource($properties) {
    $resource = array();
    foreach ($properties as $prop => $value) {
        if ($value) {
            addPropertyToResource($resource, $prop, $value);
        }
    }
    return $resource;
}

$propertyObject = createResource(array(
    'snippet.title' => 'Sample playlist ',
    'snippet.description' => 'This is a sample playlist description.',
    'snippet.tags[]' => 'Python code, interactive',
    'snippet.defaultLanguage' => '',
    'status.privacyStatus' => 'private'));
```
Ruby  

```
# Build a resource based on a list of properties given as key-value pairs.
def create_resource(properties)
  resource = {}
  properties.each do |prop, value|
    ref = resource
    prop_array = prop.to_s.split(".")
    for p in 0..(prop_array.size - 1)
      is_array = false
      key = prop_array[p]
      if key[-2,2] == "[]"
        key = key[0...-2]
        is_array = true
      end
      if p == (prop_array.size - 1)
        if is_array
          if value == ""
            ref[key.to_sym] = []
          else
            ref[key.to_sym] = value.split(",")
          end
        elsif value != ""
          ref[key.to_sym] = value
        end
      elsif ref.include?(key.to_sym)
        ref = ref[key.to_sym]
      else
        ref[key.to_sym] = {}
        ref = ref[key.to_sym]
      end
    end
  end
  return resource
end

resource = create_resource({
    'snippet.title': 'Sample playlist ',
    'snippet.description': 'This is a sample playlist description.',
    'snippet.tags[]': 'Ruby code, interactive',
    'snippet.default_language': '',
    'status.privacy_status': 'private'})
```
Apps Script  

```
// Build an object from an object containing properties as key-value pairs
function createResource(properties) {
  var res = {};
  var normalizedProps = {};
  for (var p in properties) {
    var value = properties[p];
    if (p.substr(-2, 2) == '[]' && value) {
      var adjustedName = p.replace('[]', '');
      normalizedProps[adjustedName] = value.split(',');
    } else {
      normalizedProps[p] = value;
    }
  }
  for (var p in normalizedProps) {
    if (normalizedProps.hasOwnProperty(p) && normalizedProps[p]) {
      var propArray = p.split('.');
      var ref = res;
      for (var pa = 0; pa < propArray.length; pa++) {
        var key = propArray[pa];
        if (pa == propArray.length - 1) {
          ref[key] = normalizedProps[p];
        } else {
          ref = ref[key] = ref[key] || {};
        }
      }
    };
  }
  return res;
}

var resource = createResource({
    'snippet.title': 'Sample playlist ',
    'snippet.description': 'This is a sample playlist description.',
    'snippet.tags[]': 'Apps Script code, interactive',
    'snippet.defaultLanguage': '',
    'status.privacyStatus': 'private'
});
```
Go  

```
func addPropertyToResource(ref map[string]interface{}, keys []string, value string, count int) map[string]interface{} {
        for k := count; k < (len(keys) - 1); k++ {
                switch val := ref[keys[k]].(type) {
                case map[string]interface{}:
                        ref[keys[k]] = addPropertyToResource(val, keys, value, (k + 1))
                case nil:
                        next := make(map[string]interface{})
                        ref[keys[k]] = addPropertyToResource(next, keys, value, (k + 1))
                }
        }
        // Only include properties that have values.
        if (count == len(keys) - 1 && value != "") {
                valueKey := keys[len(keys)-1]
                if valueKey[len(valueKey)-2:] == "[]" {
                        ref[valueKey[0:len(valueKey)-2]] = strings.Split(value, ",")
                } else if len(valueKey) > 4 && valueKey[len(valueKey)-4:] == "|int" {
                        ref[valueKey[0:len(valueKey)-4]], _ = strconv.Atoi(value)
                } else if value == "true" {
                        ref[valueKey] = true
                } else if value == "false" {
                        ref[valueKey] = false
                } else {
                        ref[valueKey] = value
                }
        }
        return ref
}

func createResource(properties map[string]string) string {
        resource := make(map[string]interface{})
        for key, value := range properties {
                keys := strings.Split(key, ".")
                ref := addPropertyToResource(resource, keys, value, 0)
                resource = ref
        }
        propJson, err := json.Marshal(resource)
        if err != nil {
               log.Fatal("cannot encode to JSON ", err)
        }
        return string(propJson)
}

func main() {
        properties := (map[string]string{
                 "snippet.title": "Sample playlist ",
                 "snippet.description": "This is a sample playlist description.",
                 "snippet.tags[]": "Go code, interactive",
                 "snippet.defaultLanguage": "",
                 "status.privacyStatus": "private",
        })
        res := createResource(properties)
```

### Load existing resources

To test a request to update an existing resource, you can load the current property values for that resource into the update form. For example, to update metadata about a video, enter the video ID in the `id` property field and click the **Load resource** button. The current property values load into the form and you can update just the values that you want to change.
![](https://developers.google.com/static/youtube/images/interactive-snippet-load-resource.png)