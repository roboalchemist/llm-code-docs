# Source: https://docs.anchorbrowser.io/advanced/proxy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Proxy

Anchor provides proxy configurations to access websites from different geographic locations, configurable down to the **city level.** Use custom proxies or Anchor's built-in proxy for localization.

<Warning>
  Anchor Browser infrastructure is fully hosted in the US. For GDPR compliance, upgrade to the [Growth tier](https://app.anchorbrowser.io/billing) or [contact support](https://mail.google.com/mail/?view=cm\&fs=1\&to=support@anchorbrowser.io\&su=Full%20GDPR%20Compatibility%20Request).
</Warning>

#### Quick Start Example

Here's a simple example of how to use Anchor's built-in proxy:

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  const anchor_client = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});

  const session = await anchor_client.sessions.create({
      session: {
        proxy: {
          active: true,
          country_code: 'gb',
        }
      }
  });

  console.log("Session created:", session.data);
  ```

  ```python python theme={null}
  import os
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  session = anchor_client.sessions.create(
    session={
      'proxy': {
          'active': True,
          'country_code': 'gb',
      }
    }
  )
  print("Session created:", session.data)
  ```
</CodeGroup>

This creates a browser session using Anchor's US proxy. You can change `country_code` to any supported country (e.g., 'gb', 'de', 'jp').

To experiment with different proxy configurations, visit our [Interactive API Reference](/api-reference/browser-sessions/start-browser-session)

## Custom Proxy

Anchor Browser allows you to use your own proxy servers, giving you complete control over your proxy infrastructure. This is particularly useful when you have existing proxy solutions or need to comply with specific network policies.

### Custom Proxy Configuration

To use a custom proxy, you need to provide the following information:

* **`active`**: Set to `true` to enable the proxy
* **`type`**: Set to `"custom"` to indicate you're using your own proxy
* **`server`**: The hostname or IP address of your proxy server, appended by the port (SERVER:PORT)
* **`username`**: Your proxy authentication username (if required)
* **`password`**: Your proxy authentication password (if required)

### Supported Proxy Protocols

Anchor Browser supports the following proxy protocols:

* **HTTP Proxy**: Standard HTTP proxy with optional authentication
* **HTTPS Proxy**: Secure HTTPS proxy connections
* **SOCKS5 Proxy**: SOCKS5 proxy for enhanced privacy and flexibility

### Example Configurations

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});

  const response = await anchorClient.sessions.create({
    session: {
      proxy: {
        active: true
        type: 'custom',
        server: 'proxy.example.com:port',
        username: 'myUser',
        password: 'myPassword',
      }
    }
  });
    
  console.log('Session created:', response.data);
  ```

  ```python python theme={null}
  import os
  import json
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv('ANCHOR_API_KEY'))

  response = anchor_client.sessions.create(
    session={
      'proxy': {
          'active': True
          'type': 'custom',
          'server': 'proxy.example.com:port',
          'username': 'myUser',
          'password': 'myPassword',
      }
    }
  )

  print('Session created:')
  print(response.data)
  ```
</CodeGroup>

## Localization

You can specify a country code for your proxy to route traffic through a specific geographic location. This is useful for accessing region-specific content or testing localized experiences.

The `country_code` parameter accepts country codes in lowercase. See the [complete list of supported countries](#supported-countries-with-their-country-codes) below for all available options.

### Region and City-Based Targeting

For even more precise geographic targeting, you can specify both `region` and `city` parameters. This is only supported for the default proxy type (`anchor_proxy`).

**Important Notes:**

* The `city` parameter can only be used when `region` is also provided
* If you specify a city without a region, the city parameter will be ignored
* City names: use English, case-insensitive. Both "Los Angeles" and "los-angeles" work.

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});

  const response = await anchorClient.sessions.create({
    session: {
      proxy: {
        active: true,
        country_code: 'us',
        region: 'ca',
        city: 'los-angeles'
      }
    }
  });
    
  console.log('Session created:', response.data);
  ```

  ```python python theme={null}
  import os
  import json
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv('ANCHOR_API_KEY'))

  response = anchor_client.sessions.create(
      session={
          'proxy': {
              'active': True,
              'country_code': 'us',
              'region': 'ca',
              'city': 'los-angeles'
          }
      }
  )

  print('Session created:')
  print(response.data)
  ```
</CodeGroup>

### Supported Countries with their Country Codes

<Tabs>
  <Tab title="Anchor Proxy">
    |                        |    |                  |    |                          |    |
    | ---------------------- | -- | ---------------- | -- | ------------------------ | -- |
    | Afghanistan            | af | France           | fr | Netherlands              | nl |
    | Albania                | al | French Guiana    | gf | New Zealand              | nz |
    | Algeria                | dz | French Polynesia | pf | Nicaragua                | ni |
    | Andorra                | ad | Gabon            | ga | Nigeria                  | ng |
    | Angola                 | ao | Gambia           | gm | Norway                   | no |
    | American Samoa         | as | Georgia          | ge | Pakistan                 | pk |
    | Antigua and Barbuda    | ag | Germany          | de | Panama                   | pa |
    | Argentina              | ar | Ghana            | gh | Paraguay                 | py |
    | Armenia                | am | Gibraltar        | gi | Peru                     | pe |
    | Aruba                  | aw | Greece           | gr | Philippines              | ph |
    | Australia              | au | Grenada          | gd | Poland                   | pl |
    | Austria                | at | Guadeloupe       | gp | Portugal                 | pt |
    | Azerbaijan             | az | Guatemala        | gt | Puerto Rico              | pr |
    | Bahamas                | bs | Guernsey         | gg | Qatar                    | qa |
    | Bahrain                | bh | Guinea           | gn | Romania                  | ro |
    | Barbados               | bb | Guinea-Bissau    | gw | Saint Lucia              | lc |
    | Belarus                | by | Guyana           | gy | San Marino               | sm |
    | Belgium                | be | Haiti            | ht | Saudi Arabia             | sa |
    | Belize                 | bz | Honduras         | hn | Senegal                  | sn |
    | Benin                  | bj | Hungary          | hu | Serbia                   | rs |
    | Bermuda                | bm | Iceland          | is | Seychelles               | sc |
    | Bolivia                | bo | India            | in | Sierra Leone             | sl |
    | Bosnia and Herzegovina | ba | Iran             | ir | Slovakia                 | sk |
    | Brazil                 | br | Iraq             | iq | Slovenia                 | si |
    | Bulgaria               | bg | Ireland          | ie | Somalia                  | so |
    | Burkina Faso           | bf | Israel           | il | South Africa             | za |
    | Cameroon               | cm | Italy            | it | South Korea              | kr |
    | Canada                 | ca | Jamaica          | jm | Spain                    | es |
    | Cape Verde             | cv | Japan            | jp | Suriname                 | sr |
    | Chad                   | td | Jordan           | jo | Sweden                   | se |
    | Chile                  | cl | Kazakhstan       | kz | Switzerland              | ch |
    | Colombia               | co | Kuwait           | kw | Syria                    | sy |
    | Congo                  | cg | Kyrgyzstan       | kg | São Tomé and Príncipe    | st |
    | Costa Rica             | cr | Latvia           | lv | Taiwan                   | tw |
    | Côte d’Ivoire          | ci | Lebanon          | lb | Tajikistan               | tj |
    | Croatia                | hr | Libya            | ly | Togo                     | tg |
    | Cuba                   | cu | Liechtenstein    | li | Trinidad and Tobago      | tt |
    | Cyprus                 | cy | Lithuania        | lt | Tunisia                  | tn |
    | Czech Republic         | cz | Luxembourg       | lu | Turkey                   | tr |
    | Denmark                | dk | Macedonia        | mk | Turks and Caicos Islands | tc |
    | Dominica               | dm | Mali             | ml | Ukraine                  | ua |
    | Dominican Republic     | do | Malta            | mt | United Arab Emirates     | ae |
    | Ecuador                | ec | Martinique       | mq | United Kingdom           | gb |
    | Egypt                  | eg | Mauritania       | mr | United States            | us |
    | El Salvador            | sv | Mexico           | mx | Uruguay                  | uy |
    | Estonia                | ee | Moldova          | md | Uzbekistan               | uz |
    | Ethiopia               | et | Monaco           | mc | Venezuela                | ve |
    | Faroe Islands          | fo | Montenegro       | me | Yemen                    | ye |
    | Finland                | fi | Morocco          | ma |                          |    |
  </Tab>
</Tabs>

{/* # Gov Proxy
  |Afghanistan|af|
  |Albania|al|
  |Algeria|dz|
  |Andorra|ad|
  |Angola|ao|
  |American Samoa|as|
  |Antigua and Barbuda|ag|
  |Argentina|ar|
  |Armenia|am|
  |Aruba|aw|
  |Australia|au|
  |Austria|at|
  |Azerbaijan|az|
  |Bahamas|bs|
  |Bahrain|bh|
  |Barbados|bb|
  |Belarus|by|
  |Belgium|be|
  |Belize|bz|
  |Benin|bj|
  |Bermuda|bm|
  |Bolivia|bo|
  |Bosnia and Herzegovina|ba|
  |Brazil|br|
  |Bulgaria|bg|
  |Burkina Faso|bf|
  |Cameroon|cm|
  |Canada|ca|
  |Cape Verde|cv|
  |Chad|td|
  |Chile|cl|
  |Colombia|co|
  |Congo|cg|
  |Costa Rica|cr|
  |Côte d’Ivoire|ci|
  |Croatia|hr|
  |Cuba|cu|
  |Cyprus|cy|
  |Czech Republic|cz|
  |Denmark|dk|
  |Dominica|dm|
  |Dominican Republic|do|
  |Ecuador|ec|
  |Egypt|eg|
  |El Salvador|sv|
  |Estonia|ee|
  |Ethiopia|et|
  |Faroe Islands|fo|
  |Finland|fi|
  |France|fr|
  |French Guiana|gf|
  |French Polynesia|pf|
  |Gabon|ga|
  |Gambia|gm|
  |Georgia|ge|
  |Germany|de|
  |Ghana|gh|
  |Gibraltar|gi|
  |Greece|gr|
  |Grenada|gd|
  |Guadeloupe|gp|
  |Guatemala|gt|
  |Guernsey|gg|
  |Guinea|gn|
  |Guinea-Bissau|gw|
  |Guyana|gy|
  |Haiti|ht|
  |Honduras|hn|
  |Hungary|hu|
  |Iceland|is|
  |India|in|
  |Iran|ir|
  |Iraq|iq|
  |Ireland|ie|
  |Israel|il|
  |Italy|it|
  |Jamaica|jm|
  |Japan|jp|
  |Jordan|jo|
  |Kazakhstan|kz|
  |Kuwait|kw|
  |Kyrgyzstan|kg|
  |Latvia|lv|
  |Lebanon|lb|
  |Libya|ly|
  |Liechtenstein|li|
  |Lithuania|lt|
  |Luxembourg|lu|
  |Macedonia|mk|
  |Mali|ml|
  |Malta|mt|
  |Martinique|mq|
  |Mauritania|mr|
  |Mexico|mx|
  |Moldova|md|
  |Monaco|mc|
  |Montenegro|me|
  |Morocco|ma|
  |Netherlands|nl|
  |New Zealand|nz|
  |Nicaragua|ni|
  |Nigeria|ng|
  |Norway|no|
  |Pakistan|pk|
  |Panama|pa|
  |Paraguay|py|
  |Peru|pe|
  |Philippines|ph|
  |Poland|pl|
  |Portugal|pt|
  |Puerto Rico|pr|
  |Qatar|qa|
  |Romania|ro|
  |Saint Lucia|lc|
  |San Marino|sm|
  |Saudi Arabia|sa|
  |Senegal|sn|
  |Serbia|rs|
  |Seychelles|sc|
  |Sierra Leone|sl|
  |Slovakia|sk|
  |Slovenia|si|
  |Somalia|so|
  |South Africa|za|
  |South Korea|kr|
  |Spain|es|
  |Suriname|sr|
  |Sweden|se|
  |Switzerland|ch|
  |Syria|sy|
  |São Tomé and Príncipe|st|
  |Taiwan|tw|
  |Tajikistan|tj|
  |Togo|tg|
  |Trinidad and Tobago|tt|
  |Tunisia|tn|
  |Turkey|tr|
  |Turks and Caicos Islands|tc|
  |Ukraine|ua|
  |United Arab Emirates|ae|
  |United States|us|
  |Uruguay|uy|
  |Uzbekistan|uz|
  |Venezuela|ve|
  |Yemen|ye| */}
