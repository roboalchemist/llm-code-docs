# Package org.jbake.template

---

package org.jbake.template

- 

Related Packages

Package
Description
org.jbake.template.model
 

- 

Class
Description
AbstractTemplateEngine

A template is responsible for converting a model into a rendered document.

DelegatingTemplateEngine

A template which is responsible for delegating to a supported template engine,
 based on the file extension.

FreemarkerTemplateEngine

Renders pages using the Freemarker template engine.

FreemarkerTemplateEngine.LazyLoadingModel

A custom Freemarker model that avoids loading the whole documents into memory if not necessary.

GroovyMarkupTemplateEngine

Renders documents using the GroovyMarkupTemplateEngine.

GroovyTemplateEngine

Renders documents using a Groovy template engine.

JadeTemplateEngine

Renders pages using the Jade template language.

JadeTemplateEngine.FormatHelper
 
ModelExtractor<T>
 
ModelExtractors

A singleton class giving access to model extractors.

ModelExtractorsDocumentTypeListener
 
NoModelExtractorException
 
PebbleTemplateEngine

Renders pages using the Pebble template engine.

RenderingException

Thrown if rendering of a document failed.

TemplateEngineAdapter<Type>

Adapts model extractor output to used template engine.

TemplateEngineAdapter.NoopAdapter
 
TemplateEngines

 A singleton class giving access to rendering engines.

ThymeleafTemplateEngine

A template engine which renders pages using Thymeleaf.