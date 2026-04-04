# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/security-engine-custom-configuration.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/security-engine-custom-configuration.md

# Security engine custom configuration

*Security Engine Custom Configuration is available as part of the* [*Enterprise edition*](https://www.sonarsource.com/plans-and-pricing/enterprise/) *and* [*above*](https://www.sonarsource.com/plans-and-pricing/)*.*

The security engine tracks the path that data follows through your code. It detects when data that’s potentially manipulated by a malicious user reaches a sensitive piece of code where an attack can occur.

Those potentially malicious data are also called tainted data because they are tainted by user inputs.

SonarQube Server’s security engine already knows a lot of APIs that are potential sources or targets of attack. While we do our best to identify publicly available APIs, we can’t know everything about your homemade frameworks particularly when it comes to sanitizing your data. Because of this, SonarQube Server allows you to customize the security engine to add your own sources, sanitizers, passthroughs, and sinks (see the **Elements** section below for more on these elements).

For example, you may want to:

* Add a source to add support for a framework that SonarQube Server doesn’t cover out of the box.
* Use a custom sanitizer to tell the security engine that all data going through sanitizers should be considered safe. This allows you to remove false positives and tailor the security engine to your company.

### Rules <a href="#rules" id="rules"></a>

You can customize elements for Java, PHP, C#, and Python rules in the security engine. Click the languages below to expand a list of customizable rules for that language:

<details>

<summary>Java</summary>

* [S2076](https://rules.sonarsource.com/java/RSPEC-2076): OS commands should not be vulnerable to command injection attacks
* [S2078](https://rules.sonarsource.com/java/RSPEC-2078): LDAP queries should not be vulnerable to injection attacks
* [S2083](https://rules.sonarsource.com/java/RSPEC-2083): I/O function calls should not be vulnerable to path injection attacks
* [S2091](https://rules.sonarsource.com/java/RSPEC-2091): XPath expressions should not be vulnerable to injection attacks
* [S2631](https://rules.sonarsource.com/java/RSPEC-2631): Regular expressions should not be vulnerable to Denial of Service attacks
* [S3649](https://rules.sonarsource.com/java/RSPEC-3649): Database queries should not be vulnerable to injection attacks
* [S5131](https://rules.sonarsource.com/java/RSPEC-5131): Endpoints should not be vulnerable to reflected cross-site scripting (XSS) attacks
* [S5135](https://rules.sonarsource.com/java/RSPEC-5135): Deserialization should not be vulnerable to injection attacks
* [S5144](https://rules.sonarsource.com/java/RSPEC-5144): Server-side requests should not be vulnerable to forging attacks
* [S5145](https://rules.sonarsource.com/java/RSPEC-5145): Logging should not be vulnerable to injection attacks
* [S5146](https://rules.sonarsource.com/java/RSPEC-5146): HTTP request redirections should not be open to forging attacks
* [S5147](https://rules.sonarsource.com/java/RSPEC-5147): NoSQL operations should not be vulnerable to injection attacks
* [S5883](https://rules.sonarsource.com/java/RSPEC-5883): OS commands should not be vulnerable to argument injection attacks
* [S5334](https://rules.sonarsource.com/java/RSPEC-5334): Dynamic code execution should not be vulnerable to injection attacks
* [S6096](https://rules.sonarsource.com/java/RSPEC-6096): Extracting archives should not lead to zip slip vulnerabilities
* [S6173](https://rules.sonarsource.com/java/RSPEC-6173): Reflection should not be vulnerable to injection attacks
* [S6287](https://rules.sonarsource.com/java/RSPEC-6287): Applications should not create session cookies from untrusted input
* [S6350](https://rules.sonarsource.com/java/RSPEC-6350/): Constructing arguments of system commands from user input is security-sensitive
* [S6384](https://rules.sonarsource.com/java/RSPEC-6384): Components should not be vulnerable to intent redirection
* [S6390](https://rules.sonarsource.com/java/RSPEC-6390): Thread suspensions should not be vulnerable to Denial of Service attacks
* [S6398](https://rules.sonarsource.com/java/RSPEC-6398): JSON operations should not be vulnerable to injection attacks
* [S6399](https://rules.sonarsource.com/java/RSPEC-6399): XML operations should not be vulnerable to injection attacks
* [S6547](https://rules.sonarsource.com/java/RSPEC-6547): Environment variables should not be defined from untrusted input
* [S6549](https://rules.sonarsource.com/java/RSPEC-6549/): Accessing files should not lead to filesystem oracle attacks

</details>

<details>

<summary>PHP</summary>

* [S2076](https://rules.sonarsource.com/php/RSPEC-2076): OS commands should not be vulnerable to command injection attacks
* [S2078](https://rules.sonarsource.com/php/RSPEC-2078): LDAP queries should not be vulnerable to injection attacks
* [S2083](https://rules.sonarsource.com/php/RSPEC-2083): I/O function calls should not be vulnerable to path injection attacks
* [S2091](https://rules.sonarsource.com/php/RSPEC-2091): XPath expressions should not be vulnerable to injection attacks
* [S2631](https://rules.sonarsource.com/php/RSPEC-2631): Regular expressions should not be vulnerable to Denial of Service attacks
* [S3649](https://rules.sonarsource.com/php/RSPEC-3649): Database queries should not be vulnerable to injection attacks
* [S5131](https://rules.sonarsource.com/php/RSPEC-5131): Endpoints should not be vulnerable to reflected cross-site scripting (XSS) attacks
* [S5135](https://rules.sonarsource.com/php/RSPEC-5135): Deserialization should not be vulnerable to injection attacks
* [S5144](https://rules.sonarsource.com/php/RSPEC-5144): Server-side requests should not be vulnerable to forging attacks
* [S5145](https://rules.sonarsource.com/php/RSPEC-5145): Logging should not be vulnerable to injection attacks
* [S5146](https://rules.sonarsource.com/php/RSPEC-5146): HTTP request redirections should not be open to forging attacks
* [S5334](https://rules.sonarsource.com/php/RSPEC-5334): Dynamic code execution should not be vulnerable to injection attacks
* [S5335](https://rules.sonarsource.com/php/RSPEC-5335): Include expressions should not be vulnerable to injection attacks
* [S5883](https://rules.sonarsource.com/php/RSPEC-5883): OS commands should not be vulnerable to argument injection attacks
* [S6173](https://rules.sonarsource.com/php/RSPEC-6173): Reflection should not be vulnerable to injection attacks
* [S6287](https://rules.sonarsource.com/php/RSPEC-6287): Applications should not create session cookies from untrusted input
* [S6350](https://rules.sonarsource.com/php/RSPEC-6350): Constructing arguments of system commands from user input is security-sensitive

</details>

<details>

<summary>C#</summary>

* [S2076](https://rules.sonarsource.com/csharp/RSPEC-2076): OS commands should not be vulnerable to command injection attacks
* [S2078](https://rules.sonarsource.com/csharp/RSPEC-2078): LDAP queries should not be vulnerable to injection attacks
* [S2083](https://rules.sonarsource.com/csharp/RSPEC-2083): I/O function calls should not be vulnerable to path injection attacks
* [S2091](https://rules.sonarsource.com/csharp/RSPEC-2091): XPath expressions should not be vulnerable to injection attacks
* [S2631](https://rules.sonarsource.com/csharp/RSPEC-2631): Regular expressions should not be vulnerable to Denial of Service attacks
* [S3649](https://rules.sonarsource.com/csharp/RSPEC-3649): Database queries should not be vulnerable to injection attacks
* [S5131](https://rules.sonarsource.com/csharp/RSPEC-5131): Endpoints should not be vulnerable to reflected cross-site scripting (XSS) attacks
* [S5135](https://rules.sonarsource.com/csharp/RSPEC-5135): Deserialization should not be vulnerable to injection attacks
* [S5144](https://rules.sonarsource.com/csharp/RSPEC-5144): Server-side requests should not be vulnerable to forging attacks
* [S5145](https://rules.sonarsource.com/csharp/RSPEC-5145): Logging should not be vulnerable to injection attacks
* [S5146](https://rules.sonarsource.com/csharp/RSPEC-5146): HTTP request redirections should not be open to forging attacks
* [S5334](https://rules.sonarsource.com/csharp/RSPEC-5334): Dynamic code execution should not be vulnerable to injection attacks
* [S5883](https://rules.sonarsource.com/csharp/RSPEC-5883): OS commands should not be vulnerable to argument injection attacks
* [S6096](https://rules.sonarsource.com/csharp/RSPEC-6096): Extracting archives should not lead to zip slip vulnerabilities
* [S6173](https://rules.sonarsource.com/csharp/RSPEC-6173): Reflection should not be vulnerable to injection attacks
* [S6287](https://rules.sonarsource.com/csharp/RSPEC-6287): Applications should not create session cookies from untrusted input
* [S6350](https://rules.sonarsource.com/csharp/RSPEC-6350): Constructing arguments of system commands from user input is security-sensitive
* [S6399](https://rules.sonarsource.com/csharp/RSPEC-6399): XML operations should not be vulnerable to injection attacks
* [S6639](https://rules.sonarsource.com/csharp/RSPEC-6639): Memory allocations should not be vulnerable to Denial of Service attacks
* [S6641](https://rules.sonarsource.com/csharp/RSPEC-6641): Connection strings should not be vulnerable to injections attacks

</details>

<details>

<summary>Python</summary>

* [S2076](https://rules.sonarsource.com/python/RSPEC-2076): OS commands should not be vulnerable to command injection attacks
* [S2078](https://rules.sonarsource.com/python/RSPEC-2078): LDAP queries should not be vulnerable to injection attacks
* [S2083](https://rules.sonarsource.com/python/RSPEC-2083): I/O function calls should not be vulnerable to path injection attacks
* [S2091](https://rules.sonarsource.com/python/RSPEC-2091): XPath expressions should not be vulnerable to injection attacks
* [S2631](https://rules.sonarsource.com/python/RSPEC-2631): Regular expressions should not be vulnerable to Denial of Service attacks
* [S3649](https://rules.sonarsource.com/python/RSPEC-3649): Database queries should not be vulnerable to injection attacks
* [S5131](https://rules.sonarsource.com/python/RSPEC-5131): Endpoints should not be vulnerable to reflected cross-site scripting (XSS) attacks
* [S5135](https://rules.sonarsource.com/python/RSPEC-5135): Deserialization should not be vulnerable to injection attacks
* [S5144](https://rules.sonarsource.com/python/RSPEC-5144): Server-side requests should not be vulnerable to forging attacks
* [S5145](https://rules.sonarsource.com/python/RSPEC-5145): Logging should not be vulnerable to injection attacks
* [S5146](https://rules.sonarsource.com/python/RSPEC-5146): HTTP request redirections should not be open to forging attacks
* [S5147](https://rules.sonarsource.com/python/RSPEC-5147): NoSQL operations should not be vulnerable to injection attacks
* [S5334](https://rules.sonarsource.com/python/RSPEC-5334): Dynamic code execution should not be vulnerable to injection attacks
* [S5496](https://rules.sonarsource.com/python/RSPEC-5496): Server-side templates should not be vulnerable to injection attacks
* [S6287](https://rules.sonarsource.com/python/RSPEC-6287): Applications should not create session cookies from untrusted input
* [S6350](https://rules.sonarsource.com/csharp/RSPEC-6350): Constructing arguments of system commands from user input is security-sensitive

</details>

### Elements <a href="#elements" id="elements"></a>

You can add the following elements to your custom configuration:

* **Source** – Where you get user data. You should always consider user data tainted and vulnerable to injection attacks. Example: Calling `HttpServletRequest#getParam("foo")` will return tainted content.
* **Sanitizer** – Finds and removes malicious content from one or more potentially tainted arguments. Example: `DatabaseUtils#sqlEscapeString(String str)` returns a modified version of `str` where characters used in an SQL injection attack are removed.
* **Validator** - Marks one or more arguments as safe from malicious content. Example: `String#matches(String str)` can be used to verify that `str` does not contain any content which may be used in an injection attack.
* **Passthrough** – Allows you to keep track of tainted data sent to a library outside the current function. When you pass a tainted value to a library function outside the current function, SonarQube Server automatically assumes it’s being passed to a sanitizer. If the tainted data isn’t being passed to a sanitizer, you can set up a passthrough to keep track of the data.
* **Sink** – A piece of code that can perform a security-sensitive task. Data should not contain any malicious content once it reaches a sink. Example: Running an SQL query with `java.sql.Statement#execute`.

### MethodId <a href="#method-id" id="method-id"></a>

All custom configurations rely on the accuracy of the provided `methodId`. The `methodId` format differs for each language. Click the language you’re using below for more information on the format for that language.

### Creating your custom configuration JSON file <a href="#custom-configuration" id="custom-configuration"></a>

You need to add your custom configurations to SonarQube Server using a JSON file. You can apply your custom configuration to a specific project or to all of your projects at the global level in SonarQube Server:

* **Project level** – go to **Project Settings** > **General Settings** > **SAST Engine** and add your JSON file to the **JAVA/PHP/C#/Python custom configuration** field.
* **Global level** – go to **Administration** > **General Settings** > **SAST Engine** and add your JSON file to the **JAVA/PHP/C#/Python custom configuration** field.

See the following section for more information on formatting your JSON file.

#### Configuration file format <a href="#configuration-file-format" id="configuration-file-format"></a>

Your JSON file should include the rule you’re adding a custom element to, the element you are customizing, and the `methodId` for each element. Each language needs a separate JSON file but can contain multiple rules. You may use the special rule key `common` to apply the given configuration to all the rules. Click your language below to expand an example of a JSON file to help you understand the expected format.

<details>

<summary>Java JSON file example</summary>

```json
{
  "S3649": {
    "sources": [
      {
        "methodId": "my.package.ServerRequest#getQuery()Ljava/lang/String;"
      }
    ],
    "sanitizers": [
      {
        "methodId": "my.package.StringUtils#stringReplace(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;",
        "args": [
          2 
        ]
      }
    ],
    "validators": [
      {
        "methodId": "my.package.StringUtils#equals(Ljava/lang/String;)Z",
        "args": [
          1
        ]
      }
    ],
    "passthroughs": [
      {
        "methodId": "my.package.RawUrl#<init>(Ljava/lang/String;)V",
        "isWhitelist": true,
        "args": [
          1
        ]
      }
    ],
    "sinks": [
      {
        "methodId": "my.package.MySql#query(Ljava/lang/String;)V",
        "args": [
          1
        ]
      },
      {
        "methodId": "my.package.SqlStatement#execute",
        "isMethodPrefix": true,
        "args": [
          0,
          1
        ]
      },
      {
        "methodId": "my.package.SqlStatement#run(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V",
        "interval": {
          "fromIndex": 1
        }
      }
    ]
  },
  "S5131": {
    "sources": [
      {
        "methodId": "my.package.ServerRequest#getQueryString()Ljava/lang/String;"
      }
    ],
    "sinks": [
      {
        "methodId": "my.package.Server#write(",
        "isMethodPrefix": true,
        "interval": {
          "fromIndex": 1
        }
      }
    ]
  },
  "common": {
    "sources": [
      {
        "methodId": "my.package.Input#getUserInput()Ljava/lang/String;"
      }
    ]
  }
}
```

The `args` is the index of the parameter that can receive a tainted variable. Index starts:

* `1` for a function call.
* `0` for a method call, index `0` being the current instance (`this`). The `args` field must be a non-empty array of non-negative integers, and it is a mandatory field for sanitizers and validators.

</details>

<details>

<summary>PHP JSON file example</summary>

```json
{
  "S3649": {
    "sources": [
      {
        "methodId": "My\\Namespace\\ClassName\\ServerRequest::getQuery"
      }
    ],
    "sanitizers": [
      {
        "methodId": "str_replace",
        "args": [
          3
        ]
      }
    ],
    "validators": [
      {
        "methodId": "My\\Namespace\\Validator\\inArray::isValid",
        "args": [
          1
        ]
      }
    ],
    "passthroughs": [
      {
        "methodId": "My\\Namespace\\RawUrl::RawUrl",
        "isWhitelist": true,
        "args": [
          1
        ]
      }
    ],
    "sinks": [
      {
        "methodId": "mysql_query",
        "args": [
          1
        ]
      },
     {
        "methodId": "My\\Namespace\\SqlStatement::execute",
        "isMethodPrefix": true,
        "args": [
          0,
          1
        ]
      },
      {
        "methodId": "My\\Namespace\\SqlStatement::run",
        "interval": {
          "fromIndex": 1
        }
      }
    ]
  },
  "S5131": {
    "sources": [
      {
        "methodId": "My\\Namespace\\ClassName\\ServerRequest::getQueryString"
      }
    ],
    "sinks": [
      {
        "methodId": "My\\Namespace\\ClassName\\Server::write",
        "isMethodPrefix": true,
        "interval": {
          "fromIndex": 1
        }
      }
    ]
  },
  "common": {
    "sources": [
      {
        "methodId": "My\\Namespace\\ClassName\\Input::getUserInput"
      }
    ]
  }
}
```

The `args` is the index of the parameter that can receive a tainted variable. Index starts:

* `1` for a function call.
* `0` for a method call, index `0` being the current instance (`this`). The `args` field must be a non-empty array of non-negative integers, and it is a mandatory field for sanitizers and validators.

</details>

<details>

<summary>C# JSON file example</summary>

```json
{
  "S3649": {
    "sources": [
      {
        "methodId": "My.Namespace.ServerRequest.GetQuery()"
      }
    ],
    "sanitizers": [
      {
        "methodId": "My.Namespace.StringUtils.StringReplace(string, string)",
        "args": [
          0
        ]
      }
    ],
    "validators": [
      {
        "methodId": "My.Namespace.StringUtils.Regex.Matches(string)",
        "args": [
          0
        ]
      }
    ],
    "passthroughs": [
      {
        "methodId": "My.Namespace.RawUrl.RawUrl(string)",
        "isWhitelist": true,
        "args": [
          1
        ]
      }
    ],
    "sinks": [
      {
        "methodId": "My.Namespace.MySql.Query(string)",
        "args": [
          1
        ]
      },
      {
        "methodId": "My.Namespace.SqlStatement.Execute",
        "isMethodPrefix": true,
        "args": [
          0,
          1
        ]
      },
      {
        "methodId": "My.Namespace.SqlStatement.Run(string, string, string)",
        "interval": {
          "fromIndex": 1
        }
      }
    ]
  },
  "S5131": {
    "sources": [
      {
        "$comment": "The following method id is a getter on the 'QueryString' property",
        "methodId": "My.Namespace.ServerRequest.QueryString.get"
      }
    ],
    "sinks": [
      {
        "methodId": "My.Namespace.Server.Write(",
        "isMethodPrefix": true,
        "interval": {
          "fromIndex": 1
        }
      }
    ]
  },
  "common": {
    "sources": [
      {
        "methodId": "My.Namespace.Input.GetUserInput()"
      }
    ]
  }
}
```

The `args` is the index of the parameter that can receive a tainted variable. Index starts:

* `1` for a function call.
* `0` for a method call, index `0` being the current instance (`this`). The `args` field must be a non-empty array of non-negative integers, and it is a mandatory field for sanitizers and validators.

</details>

<details>

<summary>Python JSON file example</summary>

```json
{
  "S3649": {
    "sources": [
      {
        "methodId": "my.namespace.ServerRequest.get_query"
      }
    ],
    "sanitizers": [
      {
        "methodId": "str_replace",
        "args": [
          1
        ]
      }
    ],
    "validators": [
      {
        "methodId": "my.namespace.regex.matches",
        "args": [
          1
        ]
      }
    ],
    "passthroughs": [
      {
        "methodId": "my.namespace.RawUrl",
        "isWhitelist": true,
        "args": [
          1
        ]
      }
    ],
    "sinks": [
      {
        "methodId": "mysql_query",
        "args": [
          1
        ]
      },
      {
        "methodId": "my.namespace.SqlStatement.execute",
        "isMethodPrefix": true,
        "args": [
          0,
          1
        ]
      },
      {
        "methodId": "my.namespace.SqlStatement.run",
        "interval": {
          "fromIndex": 1
        }
      }
    ]
  },
  "S5131": {
    "sources": [
      {
        "methodId": "my.namespace.ServerRequest.get_query_string"
      }
    ],
    "sinks": [
      {
        "methodId": "my.namespace.Server.write(",
        "isMethodPrefix": true,
        "interval": {
          "fromIndex": 1
        }
      }
    ]
  },
  "common": {
    "sources": [
      {
        "methodId": "my.namespace.Input.get_input"
      }
    ]
  }
}
```

The `args` is the index of the parameter that can receive a tainted variable. Index starts:

* `1` for a function call.
* `0` for a method call, index `0` being the current instance (`this`). The `args` field must be a non-empty array of non-negative integers, and it is a mandatory field for sanitizers and validators.

</details>

#### (Deprecated) Customizing through analysis parameters <a href="#deprecated-customizing-through-analysis-parameters" id="deprecated-customizing-through-analysis-parameters"></a>

{% hint style="warning" %}
Customizing the security engine through analysis parameters is deprecated. We recommend adding your custom configuration in SonarQube Server as shown above. This allows you to create a single configuration file for each language and to easily apply it to multiple projects or globally.
{% endhint %}

To customize the SonarQube Server security engine, you can feed security configuration data through parameters given to the SonarScanners. To do this, you should provide JSON files with the value of the new analysis parameters.

{% hint style="info" %}
The configuration works per rule. You can’t share a configuration between rules.
{% endhint %}

The parameters should use the following syntax:

```css-79elbk
sonar.security.[ConfigType].[RuleRepository].[RuleKey]=[FileName]
```

The `ConfigType` value can be one of the following:

* `sources`
* `sanitizers`
* `passthroughs`
* `sinks`

The `RuleRepository` value can be one of the following:

* `javasecurity`: if you want to customize the Java Security Engine
* `phpsecurity`: if you want to customize the PHP Security Engine
* `roslyn.sonaranalyzer.security.cs`: if you want to customize the C# Security Engine
* `pythonsecurity`: if you want to customize the Python Security Engine

The `RuleKey` value should be one of the values shown in the **Rules** section above.

**JSON formatting example**

Configuration is provided using JSON files. Click the heading below to expand an example PHP JSON file to help you understand the expected format.

<details>

<summary>JSON File Format Example for PHP</summary>

{% hint style="info" %}
You need to create a configuration for each rule. There is no way to share a configuration between rules.
{% endhint %}

```json
{
  "sources": [
    {
      "methodId": "My\\Namespace\\ClassName\\ServerRequest::getQuery"
    }
  ],
  "sanitizers": [
    {
      "methodId": "str_replace",
      "args": [
        3
      ]
    }
  ],
  "validators": [
    {
     "methodId": "My\\Namespace\\Validator\\inArray::isValid",
     "args": [
        1
      ]
    }
  ],
 "passthroughs": [
    {
      "methodId": "rawurldecode",
      "args": [
        1
      ]
    }
  ],
  "sinks": [
    {
      "methodId": "mysql_query",
      "args": [
        1
      ]
    },
    {
      "methodId": "My\\Namespace\\SqlStatement::execute",
      "isMethodPrefix": true, // this is to say that all the methods starting with execute on the SqlStatement object will be considered
      "args": [
        0,
        1
      ]
    },
    {
      "methodId": "My\\Namespace\\SqlStatement::run",
      "interval": {
        "fromIndex": 1 // every parameter from the number 1 will be considered
      }
    }
  ]  
}
```

The `args` is the index of the parameter that can receive a tainted variable. Index starts:

* `1` for a function call.
* `0` for a method call, index `0` being the current instance (`this`) . The `args` field must be a non-empty array of non-negative integers, and it is a mandatory field for sanitizers and validators.

</details>
