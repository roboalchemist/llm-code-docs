# Source: https://developers-classic.mailerlite.com/docs/introduction.md

# Introduction

The main information explaining how to install and use Mailerlite PHP SDK is on its GitHub page [here](https://github.com/mailerlite/mailerlite-api-v2-php-sdk).

Here is an example showing how to start using any available API endpoint right away:

[block:code]
{
  "codes": [
    {
      "code": "<?php\nrequire 'vendor/autoload.php';\n\n$mailerliteClient = new \\MailerLiteApi\\MailerLite('your-api-key');\n\n$groupsApi = $mailerliteClient->groups();\n$groups = $groupsApi->get(); // returns array of groups\n\n$fieldsApi = $mailerliteClient->fields();\n$fields = $fieldsApi->get(); // returns array of fields",
      "language": "php"
    }
  ]
}
[/block]

Or access any single available API separately:

[block:code]
{
  "codes": [
    {
      "code": "<?php\nrequire 'vendor/autoload.php';\n\n$groupsApi = (new \\MailerLiteApi\\MailerLite('your-api-key'))->groups();\n\n$allGroups = $groupsApi->get(); // returns array of groups\n\n$groupId = 123;\n$singleGroup = $groupsApi->find($groupId); // returns single item object",
      "language": "php"
    }
  ]
}
[/block]

You will find more examples using PHP SDK in the endpoint reference pages.