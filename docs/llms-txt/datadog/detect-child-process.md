# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-node-security/detect-child-process.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/detect-child-process.md

---
title: Avoid instances of 'child_process' and non-literal 'exec()'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid instances of 'child_process' and non-literal 'exec()'
---

# Avoid instances of 'child_process' and non-literal 'exec()'

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-node-security/detect-child-process`

**Language:** JavaScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

In Node.js, the "child_process" module provides capabilities to execute shell commands directly. While this might seem beneficial, it comes with significant security risks. If the input to this module isn't properly sanitized, it can pave the way for command injection attacks. In such attacks, malicious actors could introduce harmful commands, which, when executed, could compromise system integrity or lead to data breaches.

Additionally, using non-literal arguments with "exec()" presents another challenge. When arguments to "exec()" are dynamic or derived from untrusted sources, there's a risk that attackers could manipulate this input. This makes the system vulnerable to unauthorized actions, potentially causing significant damage. Therefore, for a more secure Node.js application, it's advised to tread cautiously with these features, employing rigorous input validation and considering safer alternatives.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
require('child_process')
require('node:child_process')
var child = require('child_process'); child.exec(com)
var nodeChild = require('node:child_process'); nodeChild.exec(com)
import childImport from 'child_process'; childImport.exec(com)
import nodeChildImport from 'node:child_process'; nodeChildImport.exec(com)

// not supported
// var child = sinon.stub(require('child_process')); child.exec.returns({});
// var child = sinon.stub(require('node:child_process')); child.exec.returns({});

function fn () {
    var result = child.exec(str);
}

function fn () {
    var result = childImport.exec(str);
}

function fn () {
    var result = nodeChildImport.exec(str);
}

require('child_process').exec(str)

function fn () {
    require('child_process').exec(str)
}

const {exec} = require('child_process');
exec(str)

const {exec: nodeExec} = require('node:child_process');
nodeExec(str)

import {exec as foo} from 'child_process'; 
foo(com);
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
child_process.exec('ls')

var {} = require('child_process');
var result = /hello/.exec(str);

var {} = require('node:child_process');
var result = /hello/.exec(str);

import {} from 'child_process';
var result = /hello/.exec(str);

import {} from 'node:child_process';
var result = /hello/.exec(str);

var { spawn } = require('child_process'); spawn(str);
var { spawn } = require('node:child_process'); spawn(str);
import { spawn } from 'child_process'; spawn(str);
import { spawn } from 'node:child_process'; spawn(str);

// import redeclare not covered
// var foo = require('child_process');
// function fn () {
//   var foo = /hello/;
//   var result = foo.exec(str);
// }

var child = require('child_process'); child.spawn(str)
var child = require('node:child_process'); child.spawn(str)
import child from 'child_process'; child.spawn(str)
import child from 'node:child_process'; child.spawn(str)

var foo = require('child_process');
function fn () {
  var result = foo.spawn(str);
}

require('child_process').spawn(str)

function fn () {
  require('child_process').spawn(str)
}

// constant assigment static analysis not covered
// var child_process = require('child_process');
// var FOO = 'ls';
// child_process.exec(FOO);

// import child_process from 'child_process';
// const FOO = 'ls';
// child_process.exec(FOO);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 