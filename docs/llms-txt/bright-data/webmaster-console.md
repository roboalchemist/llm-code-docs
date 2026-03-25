# Source: https://docs.brightdata.com/general/webmaster-console.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Webmaster Console

> Configure BrightBot behavior for your domains using collectors.txt file

## General

<Info>
  To enable BrightBot to function with your domain, please ensure that your firewall allows requests from the range **82.97.199.0/24**
</Info>

| Inputs                   | Description                                                                                                                                                                                                               | Format                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **Personal Information** | Endpoints containing information which are related to an identified or identifiable natural person                                                                                                                        | `URL / Document Object`                            |
| **Disallow**             | List interactive endpoint patterns such as ad links, likes, reviews, and posts. This instruction enables BrightBot to block these endpoints, aligning with our guidelines that prohibit data collection from these areas. | `URL / Document Object`                            |
| **Load**                 | Report your organic traffic load on specific domains or subdomains and on specific time frames. Bright Bot will use this information instead of public load statistics when deciding how it should rate limit itself.     | `URL / Document Object &nbsp;` `Rate` `Time-Frame` |

## Examples

<CodeGroup>
  ```txt collectors.txt theme={null}
  pii: /personal_info_1
  pii: /personal_info_2

  // Endpoints containing information which are related to an identified or identifiable natural person.

  disallow: /disallow_1
  disallow: /disallow_2

  // List interactive endpoint patterns such as ad links, likes, reviews, and posts.

  copyright: /copyright_1
  copyright: /copyright_2

  private: /*secret
  private: /private_2
  private: /private_3/*/private$

  // Wildcards and end-of-string characters can be used.

  load: example.com:100:min
  load: /endpoint_1:4500:day
  load: /endpoint_2:20000:month

  // organic traffic per domain or sub-domain per timeframe as reported by the webmaster, to be considered by Bright Bot
  ```
</CodeGroup>
