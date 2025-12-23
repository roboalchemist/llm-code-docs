# Source: https://fastapi.tiangolo.com/reference/openapi/models/

# OpenAPI `models`[&para;](#openapi-models)

OpenAPI Pydantic models used to generate and validate the generated OpenAPI.

## 
``            fastapi.openapi.models

[&para;](#fastapi.openapi.models)

### 
``            SchemaType

      `module-attribute`

[&para;](#fastapi.openapi.models.SchemaType)

`SchemaType = Literal[
    "array",
    "boolean",
    "integer",
    "null",
    "number",
    "object",
    "string",
]
`

### 
``            SchemaOrBool

      `module-attribute`

[&para;](#fastapi.openapi.models.SchemaOrBool)

`SchemaOrBool = Union[[Schema](#fastapi.openapi.models.Schema), bool]
`

### 
``            SecurityScheme

      `module-attribute`

[&para;](#fastapi.openapi.models.SecurityScheme)

`SecurityScheme = Union[
    [APIKey](#fastapi.openapi.models.APIKey), [HTTPBase](#fastapi.openapi.models.HTTPBase), [OAuth2](#fastapi.openapi.models.OAuth2), [OpenIdConnect](#fastapi.openapi.models.OpenIdConnect), [HTTPBearer](#fastapi.openapi.models.HTTPBearer)
]
`

### 
``            BaseModelWithConfig

[&para;](#fastapi.openapi.models.BaseModelWithConfig)

              Bases: `BaseModel`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.BaseModelWithConfig.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            Contact

[&para;](#fastapi.openapi.models.Contact)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            name

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Contact.name)

`name = None
`

#### 
``            url

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Contact.url)

`url = None
`

#### 
``            email

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Contact.email)

`email = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Contact.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            License

[&para;](#fastapi.openapi.models.License)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            name

      `instance-attribute`

[&para;](#fastapi.openapi.models.License.name)

`name
`

#### 
``            identifier

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.License.identifier)

`identifier = None
`

#### 
``            url

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.License.url)

`url = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.License.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            Info

[&para;](#fastapi.openapi.models.Info)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            title

      `instance-attribute`

[&para;](#fastapi.openapi.models.Info.title)

`title
`

#### 
``            summary

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Info.summary)

`summary = None
`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Info.description)

`description = None
`

#### 
``            termsOfService

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Info.termsOfService)

`termsOfService = None
`

#### 
``            contact

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Info.contact)

`contact = None
`

#### 
``            license

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Info.license)

`license = None
`

#### 
``            version

      `instance-attribute`

[&para;](#fastapi.openapi.models.Info.version)

`version
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Info.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            ServerVariable

[&para;](#fastapi.openapi.models.ServerVariable)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            enum

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ServerVariable.enum)

`enum = None
`

#### 
``            default

      `instance-attribute`

[&para;](#fastapi.openapi.models.ServerVariable.default)

`default
`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ServerVariable.description)

`description = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ServerVariable.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            Server

[&para;](#fastapi.openapi.models.Server)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            url

      `instance-attribute`

[&para;](#fastapi.openapi.models.Server.url)

`url
`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Server.description)

`description = None
`

#### 
``            variables

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Server.variables)

`variables = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Server.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            Reference

[&para;](#fastapi.openapi.models.Reference)

              Bases: `BaseModel`

#### 
``            ref

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Reference.ref)

`ref = Field(alias='$ref')
`

### 
``            Discriminator

[&para;](#fastapi.openapi.models.Discriminator)

              Bases: `BaseModel`

#### 
``            propertyName

      `instance-attribute`

[&para;](#fastapi.openapi.models.Discriminator.propertyName)

`propertyName
`

#### 
``            mapping

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Discriminator.mapping)

`mapping = None
`

### 
``            XML

[&para;](#fastapi.openapi.models.XML)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            name

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.XML.name)

`name = None
`

#### 
``            namespace

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.XML.namespace)

`namespace = None
`

#### 
``            prefix

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.XML.prefix)

`prefix = None
`

#### 
``            attribute

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.XML.attribute)

`attribute = None
`

#### 
``            wrapped

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.XML.wrapped)

`wrapped = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.XML.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            ExternalDocumentation

[&para;](#fastapi.openapi.models.ExternalDocumentation)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ExternalDocumentation.description)

`description = None
`

#### 
``            url

      `instance-attribute`

[&para;](#fastapi.openapi.models.ExternalDocumentation.url)

`url
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ExternalDocumentation.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            Schema

[&para;](#fastapi.openapi.models.Schema)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            schema_

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.schema_)

`schema_ = Field(default=None, alias='$schema')
`

#### 
``            vocabulary

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.vocabulary)

`vocabulary = Field(default=None, alias='$vocabulary')
`

#### 
``            id

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.id)

`id = Field(default=None, alias='$id')
`

#### 
``            anchor

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.anchor)

`anchor = Field(default=None, alias='$anchor')
`

#### 
``            dynamicAnchor

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.dynamicAnchor)

`dynamicAnchor = Field(default=None, alias='$dynamicAnchor')
`

#### 
``            ref

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.ref)

`ref = Field(default=None, alias='$ref')
`

#### 
``            dynamicRef

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.dynamicRef)

`dynamicRef = Field(default=None, alias='$dynamicRef')
`

#### 
``            defs

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.defs)

`defs = Field(default=None, alias='$defs')
`

#### 
``            comment

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.comment)

`comment = Field(default=None, alias='$comment')
`

#### 
``            allOf

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.allOf)

`allOf = None
`

#### 
``            anyOf

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.anyOf)

`anyOf = None
`

#### 
``            oneOf

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.oneOf)

`oneOf = None
`

#### 
``            not_

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.not_)

`not_ = Field(default=None, alias='not')
`

#### 
``            if_

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.if_)

`if_ = Field(default=None, alias='if')
`

#### 
``            then

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.then)

`then = None
`

#### 
``            else_

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.else_)

`else_ = Field(default=None, alias='else')
`

#### 
``            dependentSchemas

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.dependentSchemas)

`dependentSchemas = None
`

#### 
``            prefixItems

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.prefixItems)

`prefixItems = None
`

#### 
``            items

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.items)

`items = None
`

#### 
``            contains

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.contains)

`contains = None
`

#### 
``            properties

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.properties)

`properties = None
`

#### 
``            patternProperties

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.patternProperties)

`patternProperties = None
`

#### 
``            additionalProperties

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.additionalProperties)

`additionalProperties = None
`

#### 
``            propertyNames

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.propertyNames)

`propertyNames = None
`

#### 
``            unevaluatedItems

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.unevaluatedItems)

`unevaluatedItems = None
`

#### 
``            unevaluatedProperties

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.unevaluatedProperties)

`unevaluatedProperties = None
`

#### 
``            type

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.type)

`type = None
`

#### 
``            enum

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.enum)

`enum = None
`

#### 
``            const

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.const)

`const = None
`

#### 
``            multipleOf

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.multipleOf)

`multipleOf = Field(default=None, gt=0)
`

#### 
``            maximum

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.maximum)

`maximum = None
`

#### 
``            exclusiveMaximum

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.exclusiveMaximum)

`exclusiveMaximum = None
`

#### 
``            minimum

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.minimum)

`minimum = None
`

#### 
``            exclusiveMinimum

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.exclusiveMinimum)

`exclusiveMinimum = None
`

#### 
``            maxLength

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.maxLength)

`maxLength = Field(default=None, ge=0)
`

#### 
``            minLength

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.minLength)

`minLength = Field(default=None, ge=0)
`

#### 
``            pattern

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.pattern)

`pattern = None
`

#### 
``            maxItems

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.maxItems)

`maxItems = Field(default=None, ge=0)
`

#### 
``            minItems

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.minItems)

`minItems = Field(default=None, ge=0)
`

#### 
``            uniqueItems

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.uniqueItems)

`uniqueItems = None
`

#### 
``            maxContains

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.maxContains)

`maxContains = Field(default=None, ge=0)
`

#### 
``            minContains

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.minContains)

`minContains = Field(default=None, ge=0)
`

#### 
``            maxProperties

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.maxProperties)

`maxProperties = Field(default=None, ge=0)
`

#### 
``            minProperties

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.minProperties)

`minProperties = Field(default=None, ge=0)
`

#### 
``            required

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.required)

`required = None
`

#### 
``            dependentRequired

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.dependentRequired)

`dependentRequired = None
`

#### 
``            format

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.format)

`format = None
`

#### 
``            contentEncoding

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.contentEncoding)

`contentEncoding = None
`

#### 
``            contentMediaType

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.contentMediaType)

`contentMediaType = None
`

#### 
``            contentSchema

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.contentSchema)

`contentSchema = None
`

#### 
``            title

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.title)

`title = None
`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.description)

`description = None
`

#### 
``            default

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.default)

`default = None
`

#### 
``            deprecated

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.deprecated)

`deprecated = None
`

#### 
``            readOnly

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.readOnly)

`readOnly = None
`

#### 
``            writeOnly

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.writeOnly)

`writeOnly = None
`

#### 
``            examples

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.examples)

`examples = None
`

#### 
``            discriminator

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.discriminator)

`discriminator = None
`

#### 
``            xml

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.xml)

`xml = None
`

#### 
``            externalDocs

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.externalDocs)

`externalDocs = None
`

#### 
``            example

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.example)

`example = None
`

  Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Schema.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            Example

[&para;](#fastapi.openapi.models.Example)

              Bases: `TypedDict`

#### 
``            summary

      `instance-attribute`

[&para;](#fastapi.openapi.models.Example.summary)

`summary
`

#### 
``            description

      `instance-attribute`

[&para;](#fastapi.openapi.models.Example.description)

`description
`

#### 
``            value

      `instance-attribute`

[&para;](#fastapi.openapi.models.Example.value)

`value
`

#### 
``            externalValue

      `instance-attribute`

[&para;](#fastapi.openapi.models.Example.externalValue)

`externalValue
`

### 
``            ParameterInType

[&para;](#fastapi.openapi.models.ParameterInType)

              Bases: `Enum`

#### 
``            query

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ParameterInType.query)

`query = 'query'
`

#### 
``            header

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ParameterInType.header)

`header = 'header'
`

#### 
``            path

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ParameterInType.path)

`path = 'path'
`

#### 
``            cookie

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ParameterInType.cookie)

`cookie = 'cookie'
`

### 
``            Encoding

[&para;](#fastapi.openapi.models.Encoding)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            contentType

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Encoding.contentType)

`contentType = None
`

#### 
``            headers

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Encoding.headers)

`headers = None
`

#### 
``            style

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Encoding.style)

`style = None
`

#### 
``            explode

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Encoding.explode)

`explode = None
`

#### 
``            allowReserved

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Encoding.allowReserved)

`allowReserved = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Encoding.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            MediaType

[&para;](#fastapi.openapi.models.MediaType)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            schema_

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.MediaType.schema_)

`schema_ = Field(default=None, alias='schema')
`

#### 
``            example

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.MediaType.example)

`example = None
`

#### 
``            examples

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.MediaType.examples)

`examples = None
`

#### 
``            encoding

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.MediaType.encoding)

`encoding = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.MediaType.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            ParameterBase

[&para;](#fastapi.openapi.models.ParameterBase)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ParameterBase.description)

`description = None
`

#### 
``            required

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ParameterBase.required)

`required = None
`

#### 
``            deprecated

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ParameterBase.deprecated)

`deprecated = None
`

#### 
``            style

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ParameterBase.style)

`style = None
`

#### 
``            explode

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ParameterBase.explode)

`explode = None
`

#### 
``            allowReserved

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ParameterBase.allowReserved)

`allowReserved = None
`

#### 
``            schema_

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ParameterBase.schema_)

`schema_ = Field(default=None, alias='schema')
`

#### 
``            example

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ParameterBase.example)

`example = None
`

#### 
``            examples

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ParameterBase.examples)

`examples = None
`

#### 
``            content

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ParameterBase.content)

`content = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.ParameterBase.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            Parameter

[&para;](#fastapi.openapi.models.Parameter)

              Bases: `[ParameterBase](#fastapi.openapi.models.ParameterBase)`

#### 
``            name

      `instance-attribute`

[&para;](#fastapi.openapi.models.Parameter.name)

`name
`

#### 
``            in_

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Parameter.in_)

`in_ = Field(alias='in')
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Parameter.model_config)

`model_config = {'extra': 'allow'}
`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Parameter.description)

`description = None
`

#### 
``            required

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Parameter.required)

`required = None
`

#### 
``            deprecated

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Parameter.deprecated)

`deprecated = None
`

#### 
``            style

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Parameter.style)

`style = None
`

#### 
``            explode

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Parameter.explode)

`explode = None
`

#### 
``            allowReserved

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Parameter.allowReserved)

`allowReserved = None
`

#### 
``            schema_

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Parameter.schema_)

`schema_ = Field(default=None, alias='schema')
`

#### 
``            example

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Parameter.example)

`example = None
`

#### 
``            examples

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Parameter.examples)

`examples = None
`

#### 
``            content

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Parameter.content)

`content = None
`

### 
``            Header

[&para;](#fastapi.openapi.models.Header)

              Bases: `[ParameterBase](#fastapi.openapi.models.ParameterBase)`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Header.model_config)

`model_config = {'extra': 'allow'}
`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Header.description)

`description = None
`

#### 
``            required

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Header.required)

`required = None
`

#### 
``            deprecated

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Header.deprecated)

`deprecated = None
`

#### 
``            style

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Header.style)

`style = None
`

#### 
``            explode

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Header.explode)

`explode = None
`

#### 
``            allowReserved

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Header.allowReserved)

`allowReserved = None
`

#### 
``            schema_

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Header.schema_)

`schema_ = Field(default=None, alias='schema')
`

#### 
``            example

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Header.example)

`example = None
`

#### 
``            examples

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Header.examples)

`examples = None
`

#### 
``            content

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Header.content)

`content = None
`

### 
``            RequestBody

[&para;](#fastapi.openapi.models.RequestBody)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.RequestBody.description)

`description = None
`

#### 
``            content

      `instance-attribute`

[&para;](#fastapi.openapi.models.RequestBody.content)

`content
`

#### 
``            required

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.RequestBody.required)

`required = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.RequestBody.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            Link

[&para;](#fastapi.openapi.models.Link)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            operationRef

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Link.operationRef)

`operationRef = None
`

#### 
``            operationId

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Link.operationId)

`operationId = None
`

#### 
``            parameters

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Link.parameters)

`parameters = None
`

#### 
``            requestBody

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Link.requestBody)

`requestBody = None
`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Link.description)

`description = None
`

#### 
``            server

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Link.server)

`server = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Link.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            Response

[&para;](#fastapi.openapi.models.Response)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            description

      `instance-attribute`

[&para;](#fastapi.openapi.models.Response.description)

`description
`

#### 
``            headers

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Response.headers)

`headers = None
`

#### 
``            content

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Response.content)

`content = None
`

#### 
``            links

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Response.links)

`links = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Response.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            Operation

[&para;](#fastapi.openapi.models.Operation)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            tags

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Operation.tags)

`tags = None
`

#### 
``            summary

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Operation.summary)

`summary = None
`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Operation.description)

`description = None
`

#### 
``            externalDocs

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Operation.externalDocs)

`externalDocs = None
`

#### 
``            operationId

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Operation.operationId)

`operationId = None
`

#### 
``            parameters

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Operation.parameters)

`parameters = None
`

#### 
``            requestBody

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Operation.requestBody)

`requestBody = None
`

#### 
``            responses

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Operation.responses)

`responses = None
`

#### 
``            callbacks

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Operation.callbacks)

`callbacks = None
`

#### 
``            deprecated

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Operation.deprecated)

`deprecated = None
`

#### 
``            security

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Operation.security)

`security = None
`

#### 
``            servers

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Operation.servers)

`servers = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Operation.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            PathItem

[&para;](#fastapi.openapi.models.PathItem)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            ref

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.PathItem.ref)

`ref = Field(default=None, alias='$ref')
`

#### 
``            summary

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.PathItem.summary)

`summary = None
`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.PathItem.description)

`description = None
`

#### 
``            get

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.PathItem.get)

`get = None
`

#### 
``            put

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.PathItem.put)

`put = None
`

#### 
``            post

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.PathItem.post)

`post = None
`

#### 
``            delete

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.PathItem.delete)

`delete = None
`

#### 
``            options

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.PathItem.options)

`options = None
`

#### 
``            head

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.PathItem.head)

`head = None
`

#### 
``            patch

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.PathItem.patch)

`patch = None
`

#### 
``            trace

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.PathItem.trace)

`trace = None
`

#### 
``            servers

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.PathItem.servers)

`servers = None
`

#### 
``            parameters

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.PathItem.parameters)

`parameters = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.PathItem.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            SecuritySchemeType

[&para;](#fastapi.openapi.models.SecuritySchemeType)

              Bases: `Enum`

#### 
``            apiKey

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.SecuritySchemeType.apiKey)

`apiKey = 'apiKey'
`

#### 
``            http

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.SecuritySchemeType.http)

`http = 'http'
`

#### 
``            oauth2

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.SecuritySchemeType.oauth2)

`oauth2 = 'oauth2'
`

#### 
``            openIdConnect

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.SecuritySchemeType.openIdConnect)

`openIdConnect = 'openIdConnect'
`

### 
``            SecurityBase

[&para;](#fastapi.openapi.models.SecurityBase)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            type_

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.SecurityBase.type_)

`type_ = Field(alias='type')
`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.SecurityBase.description)

`description = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.SecurityBase.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            APIKeyIn

[&para;](#fastapi.openapi.models.APIKeyIn)

              Bases: `Enum`

#### 
``            query

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.APIKeyIn.query)

`query = 'query'
`

#### 
``            header

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.APIKeyIn.header)

`header = 'header'
`

#### 
``            cookie

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.APIKeyIn.cookie)

`cookie = 'cookie'
`

### 
``            APIKey

[&para;](#fastapi.openapi.models.APIKey)

              Bases: `[SecurityBase](#fastapi.openapi.models.SecurityBase)`

#### 
``            type_

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.APIKey.type_)

`type_ = Field(default=[apiKey](#fastapi.openapi.models.SecuritySchemeType.apiKey), alias='type')
`

#### 
``            in_

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.APIKey.in_)

`in_ = Field(alias='in')
`

#### 
``            name

      `instance-attribute`

[&para;](#fastapi.openapi.models.APIKey.name)

`name
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.APIKey.model_config)

`model_config = {'extra': 'allow'}
`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.APIKey.description)

`description = None
`

### 
``            HTTPBase

[&para;](#fastapi.openapi.models.HTTPBase)

              Bases: `[SecurityBase](#fastapi.openapi.models.SecurityBase)`

#### 
``            type_

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.HTTPBase.type_)

`type_ = Field(default=[http](#fastapi.openapi.models.SecuritySchemeType.http), alias='type')
`

#### 
``            scheme

      `instance-attribute`

[&para;](#fastapi.openapi.models.HTTPBase.scheme)

`scheme
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.HTTPBase.model_config)

`model_config = {'extra': 'allow'}
`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.HTTPBase.description)

`description = None
`

### 
``            HTTPBearer

[&para;](#fastapi.openapi.models.HTTPBearer)

              Bases: `[HTTPBase](#fastapi.openapi.models.HTTPBase)`

#### 
``            scheme

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.HTTPBearer.scheme)

`scheme = 'bearer'
`

#### 
``            bearerFormat

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.HTTPBearer.bearerFormat)

`bearerFormat = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.HTTPBearer.model_config)

`model_config = {'extra': 'allow'}
`

#### 
``            type_

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.HTTPBearer.type_)

`type_ = Field(default=[http](#fastapi.openapi.models.SecuritySchemeType.http), alias='type')
`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.HTTPBearer.description)

`description = None
`

### 
``            OAuthFlow

[&para;](#fastapi.openapi.models.OAuthFlow)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            refreshUrl

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlow.refreshUrl)

`refreshUrl = None
`

#### 
``            scopes

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlow.scopes)

`scopes = {}
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlow.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            OAuthFlowImplicit

[&para;](#fastapi.openapi.models.OAuthFlowImplicit)

              Bases: `[OAuthFlow](#fastapi.openapi.models.OAuthFlow)`

#### 
``            authorizationUrl

      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowImplicit.authorizationUrl)

`authorizationUrl
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowImplicit.model_config)

`model_config = {'extra': 'allow'}
`

#### 
``            refreshUrl

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowImplicit.refreshUrl)

`refreshUrl = None
`

#### 
``            scopes

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowImplicit.scopes)

`scopes = {}
`

### 
``            OAuthFlowPassword

[&para;](#fastapi.openapi.models.OAuthFlowPassword)

              Bases: `[OAuthFlow](#fastapi.openapi.models.OAuthFlow)`

#### 
``            tokenUrl

      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowPassword.tokenUrl)

`tokenUrl
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowPassword.model_config)

`model_config = {'extra': 'allow'}
`

#### 
``            refreshUrl

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowPassword.refreshUrl)

`refreshUrl = None
`

#### 
``            scopes

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowPassword.scopes)

`scopes = {}
`

### 
``            OAuthFlowClientCredentials

[&para;](#fastapi.openapi.models.OAuthFlowClientCredentials)

              Bases: `[OAuthFlow](#fastapi.openapi.models.OAuthFlow)`

#### 
``            tokenUrl

      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowClientCredentials.tokenUrl)

`tokenUrl
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowClientCredentials.model_config)

`model_config = {'extra': 'allow'}
`

#### 
``            refreshUrl

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowClientCredentials.refreshUrl)

`refreshUrl = None
`

#### 
``            scopes

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowClientCredentials.scopes)

`scopes = {}
`

### 
``            OAuthFlowAuthorizationCode

[&para;](#fastapi.openapi.models.OAuthFlowAuthorizationCode)

              Bases: `[OAuthFlow](#fastapi.openapi.models.OAuthFlow)`

#### 
``            authorizationUrl

      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowAuthorizationCode.authorizationUrl)

`authorizationUrl
`

#### 
``            tokenUrl

      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowAuthorizationCode.tokenUrl)

`tokenUrl
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowAuthorizationCode.model_config)

`model_config = {'extra': 'allow'}
`

#### 
``            refreshUrl

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowAuthorizationCode.refreshUrl)

`refreshUrl = None
`

#### 
``            scopes

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlowAuthorizationCode.scopes)

`scopes = {}
`

### 
``            OAuthFlows

[&para;](#fastapi.openapi.models.OAuthFlows)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            implicit

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlows.implicit)

`implicit = None
`

#### 
``            password

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlows.password)

`password = None
`

#### 
``            clientCredentials

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlows.clientCredentials)

`clientCredentials = None
`

#### 
``            authorizationCode

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlows.authorizationCode)

`authorizationCode = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuthFlows.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            OAuth2

[&para;](#fastapi.openapi.models.OAuth2)

              Bases: `[SecurityBase](#fastapi.openapi.models.SecurityBase)`

#### 
``            type_

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuth2.type_)

`type_ = Field(default=[oauth2](#fastapi.openapi.models.SecuritySchemeType.oauth2), alias='type')
`

#### 
``            flows

      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuth2.flows)

`flows
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuth2.model_config)

`model_config = {'extra': 'allow'}
`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OAuth2.description)

`description = None
`

### 
``            OpenIdConnect

[&para;](#fastapi.openapi.models.OpenIdConnect)

              Bases: `[SecurityBase](#fastapi.openapi.models.SecurityBase)`

#### 
``            type_

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OpenIdConnect.type_)

`type_ = Field(default=[openIdConnect](#fastapi.openapi.models.SecuritySchemeType.openIdConnect), alias='type')
`

#### 
``            openIdConnectUrl

      `instance-attribute`

[&para;](#fastapi.openapi.models.OpenIdConnect.openIdConnectUrl)

`openIdConnectUrl
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OpenIdConnect.model_config)

`model_config = {'extra': 'allow'}
`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OpenIdConnect.description)

`description = None
`

### 
``            Components

[&para;](#fastapi.openapi.models.Components)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            schemas

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Components.schemas)

`schemas = None
`

#### 
``            responses

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Components.responses)

`responses = None
`

#### 
``            parameters

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Components.parameters)

`parameters = None
`

#### 
``            examples

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Components.examples)

`examples = None
`

#### 
``            requestBodies

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Components.requestBodies)

`requestBodies = None
`

#### 
``            headers

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Components.headers)

`headers = None
`

#### 
``            securitySchemes

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Components.securitySchemes)

`securitySchemes = None
`

#### 
``            links

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Components.links)

`links = None
`

#### 
``            callbacks

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Components.callbacks)

`callbacks = None
`

#### 
``            pathItems

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Components.pathItems)

`pathItems = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Components.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            Tag

[&para;](#fastapi.openapi.models.Tag)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            name

      `instance-attribute`

[&para;](#fastapi.openapi.models.Tag.name)

`name
`

#### 
``            description

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Tag.description)

`description = None
`

#### 
``            externalDocs

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Tag.externalDocs)

`externalDocs = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.Tag.model_config)

`model_config = {'extra': 'allow'}
`

### 
``            OpenAPI

[&para;](#fastapi.openapi.models.OpenAPI)

              Bases: `[BaseModelWithConfig](#fastapi.openapi.models.BaseModelWithConfig)`

#### 
``            openapi

      `instance-attribute`

[&para;](#fastapi.openapi.models.OpenAPI.openapi)

`openapi
`

#### 
``            info

      `instance-attribute`

[&para;](#fastapi.openapi.models.OpenAPI.info)

`info
`

#### 
``            jsonSchemaDialect

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OpenAPI.jsonSchemaDialect)

`jsonSchemaDialect = None
`

#### 
``            servers

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OpenAPI.servers)

`servers = None
`

#### 
``            paths

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OpenAPI.paths)

`paths = None
`

#### 
``            webhooks

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OpenAPI.webhooks)

`webhooks = None
`

#### 
``            components

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OpenAPI.components)

`components = None
`

#### 
``            security

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OpenAPI.security)

`security = None
`

#### 
``            tags

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OpenAPI.tags)

`tags = None
`

#### 
``            externalDocs

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OpenAPI.externalDocs)

`externalDocs = None
`

#### 
``            model_config

      `class-attribute`
      `instance-attribute`

[&para;](#fastapi.openapi.models.OpenAPI.model_config)

`model_config = {'extra': 'allow'}
`