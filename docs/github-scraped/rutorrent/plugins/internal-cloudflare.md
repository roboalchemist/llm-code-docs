# Plugin _cloudflare

## Description

This plugin allows to scrape the DDOS protection from Cloudflare.
It requires python and the module [cloudscraper](https://github.com/VeNoMouS/cloudscraper). The plugin is loaded only if python is present and can import the module cloudscraper. I.e.

1. Python must be installed and ruTorrent config variable ```$pathToExternals['python']``` must contain path to it. You may to define this variable in the global config.php or in the plugin's conf.php.
2. Python module ```cloudscraper``` must be installed (see link above for details).
3. You must set environment variable ```PYTHONPATH``` for your web-server to the correct value.

Technically the module will pass the challenge of the cloudflare protection and output 2 cookies. The cookies are added to the session to reach the page correctly.

The challenge might ask for a recaptcha challenge. If you have subscription in any of the supported 3rd party, you can activate the scraping by filling the details in the plugin's conf.php. This recaptcha requires another python module: python_anticaptcha
