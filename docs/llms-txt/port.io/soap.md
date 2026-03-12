# Source: https://docs.port.io/build-your-software-catalog/custom-integration/webhook/examples/packages/soap.md

# SOAP API

In this example you are going to create a `soapApi` blueprint that ingests all paths in your SOAP API definition files using a combination of Port's [API](/build-your-software-catalog/custom-integration/api/.md) and [webhook functionality](/build-your-software-catalog/custom-integration/webhook/.md).

To ingest the API paths to Port, a script that sends information about the API definition according to the webhook configuration is used.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

Create the following blueprint definition and webhook configuration:

SOAP blueprint

Create in Port

```
{
  "identifier": "soapApi",
  "description": "This blueprint represents a SOAP API in our software catalog",
  "title": "SOAP API",
  "icon": "ApiDoc",
  "schema": {
    "properties": {
      "url": {
        "type": "string",
        "title": "API URL",
        "format": "url"
      },
      "attributes": {
        "type": "object",
        "title": "Attributes"
      },
      "parameters": {
        "type": "object",
        "title": "Parameters"
      },
      "response": {
        "type": "object",
        "title": "Response"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```

Package webhook configuration

```
{
  "identifier": "soapApiMapper",
  "title": "SOAP API Mapper",
  "description": "A webhook configuration to ingest SOAP API paths from a file",
  "icon": "ApiDoc",
  "mappings": [
    {
      "blueprint": "soapApi",
      "itemsToParse": ".body.paths",
      "entity": {
        "identifier": ".item.path_name",
        "title": ".item.path_name",
        "properties": {
          "url": ".item.url",
          "attributes": ".item.attributes",
          "parameters": ".item.parameters",
          "response": ".item.response"
        }
      }
    }
  ],
  "enabled": true,
  "security": {}
}
```

## Working with Port's API and Python script[â](#working-with-ports-api-and-python-script "Direct link to Working with Port's API and Python script")

Here is an example snippet showing how to integrate Port's API and webhook with your existing pipelines using Python:

Python script example

```
## Import the needed libraries
import requests
import os
import xml.dom.minidom

# The URL for the webhook endpoint provided by Port
WEBHOOK_URL = os.environ["WEBHOOK_URL"]

def add_entity_to_port(entity_object):
    """A function to create the passed entity in Port using the webhook URL

    Params
    --------------
    entity_object: dict
        The entity to add in your Port catalog

    Returns
    --------------
    response: dict
        The response object after calling the webhook
    """
    headers = {"Content-Type": "application/json"}
    response = requests.post(WEBHOOK_URL, json=entity_object, headers=headers)
    return response.json()


def ingest_soap_request_data(soap_file):
    """This function takes a soap request XML file and extracts the path information into a
    JSON array object

    Params
    --------------
    soap_file: str
        The path to the xml file relative to the project's root folder

    Returns
    --------------
    response: dict
        The JSON data extracted from the xml file
    """

    dom = xml.dom.minidom.parse(soap_file)

    # Get the root object
    root_element = dom.documentElement
    root_namespace = root_element.tagName.split(":")[0]

    # Extract data from the SOAP request body
    body_element = root_element.getElementsByTagName(root_namespace + ':Body')[0]
    api_url = body_element.getAttribute('xmlns')

    # Extract paths, attributes and parameters for each child element
    child_elements = [child for child in body_element.childNodes if child.nodeType == child.ELEMENT_NODE]
    soap_request_object = []
    for child_element in child_elements:
        path_name = child_element.localName
        self_url = child_element.getAttribute("xmlns")
        parameters = {}
        for parameter_element in child_element.getElementsByTagName('*'):
            parameter_name = parameter_element.localName
            parameter_value = parameter_element.firstChild.data if parameter_element.firstChild else None
            parameters[parameter_name] = parameter_value

        soap_request_object.append({"path_name": path_name, "attributes": {"self_url": self_url}, "parameters": parameters, "api_url": api_url})
    return soap_request_object


def ingest_soap_respone_data(soap_file):
    """This function takes a soap response XML file path and extracts the path information into a
    JSON object

    Params
    --------------
    soap_file: str
        The path to the xml file relative to the project's root folder

    Returns
    --------------
    response: dict
        The JSON data extracted from the xml file
    """

    dom = xml.dom.minidom.parse(soap_file)

    # Get the root object
    root_element = dom.documentElement
    root_namespace = root_element.tagName.split(":")[0]

    # Extract data from the SOAP response body
    body_element = root_element.getElementsByTagName(root_namespace + ':Body')[0]
    child_elements = [child for child in body_element.childNodes if child.nodeType == child.ELEMENT_NODE]
    soap_response_object = {}
    for child_element in child_elements:
        path_name = child_element.localName
        data = {}
        for data_element in child_element.getElementsByTagName('*'):
            data_name = data_element.localName
            if not data_name.endswith("Result"):

                data_value = data_element.firstChild.data if data_element.firstChild else None
                data[data_name] = data_value

        soap_response_object[path_name] = data

    return soap_response_object

# Replace the values in these variables with the paths leading to your SOAP API definition XML files
soap_request_file = "your_soap_request.xml"
soap_response_file = "your_soap_response.xml"

request_object = ingest_soap_request_data(soap_request_file)
response_object = ingest_soap_respone_data(soap_response_file)

## Map each SOAP Request to its response data
for index, element in enumerate(request_object):
    element["response"] = response_object.get(element["path_name"]+"Response", {})
    request_object[index].update(element)

port_entity_object = {
    "paths": request_object
}
webhook_response = add_entity_to_port(port_entity_object)
print(webhook_response)
```
