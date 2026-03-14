# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/crud/encoder/JsonEncoder.md

# [JsonEncoder](https://bryntum.com/docs/gantt/api/Scheduler/crud/encoder/JsonEncoder)

Implements data encoding functional that should be mixed to a [AbstractCrudManager](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManager) sub-class. Uses _JSON_ as an encoding system.

```
// create a new CrudManager using AJAX as a transport system and JSON for encoding
class MyCrudManager extends JsonEncode(AjaxTransport(AbstractCrudManager)) {}
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[encoder](https://bryntum.com/docs/gantt/api/Scheduler/crud/encoder/JsonEncoder#config-encoder)
Configuration of the JSON encoder used by the _Crud Manager_.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isJsonEncoder](https://bryntum.com/docs/gantt/api/Scheduler/crud/encoder/JsonEncoder#property-isJsonEncoder)
Identifies an object as an instance of [JsonEncoder](https://bryntum.com/docs/gantt/api/#Scheduler/crud/encoder/JsonEncoder) class, or subclass thereof.

[isJsonEncoder](https://bryntum.com/docs/gantt/api/Scheduler/crud/encoder/JsonEncoder#property-isJsonEncoder-static)
Identifies an object as an instance of [JsonEncoder](https://bryntum.com/docs/gantt/api/#Scheduler/crud/encoder/JsonEncoder) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[encode](https://bryntum.com/docs/gantt/api/Scheduler/crud/encoder/JsonEncoder#function-encode)
Encodes a request object to _JSON_ encoded string. If encoding fails (due to circular structure), it returns null. Supposed to be overridden in case data provided by the _Crud Manager_ has to be transformed into format requested by server.

[decode](https://bryntum.com/docs/gantt/api/Scheduler/crud/encoder/JsonEncoder#function-decode)
Decodes (parses) a _JSON_ response string to an object. If parsing fails, it returns null. Supposed to be overridden in case data provided by server has to be transformed into format requested by the _Crud Manager_.
