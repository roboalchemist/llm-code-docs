# Package org.hibernate.validator.spi.scripting

---

package org.hibernate.validator.spi.scripting

This package provides support for customization of the script evaluation for `ScriptAssert`
and `ParameterScriptAssert` constraints.

This package is part of the public Hibernate Validator SPI.

Author:
Marko Bekhta

- 

Class
Description
AbstractCachingScriptEvaluatorFactory

Basic cacheable factory responsible for the creation of `ScriptEvaluator`s.

ScriptEngineScriptEvaluator

A wrapper around JSR 223 `ScriptEngine`s.

ScriptEvaluationException

Exception raised when an error occurs during the evaluation of a script.

ScriptEvaluator

Used to evaluate script expressions for `ScriptAssert`
and `ParameterScriptAssert` constraints.

ScriptEvaluatorFactory

Factory used to initialize the `ScriptEvaluator`s required to evaluate script expressions defined in
`ScriptAssert` and `ParameterScriptAssert` constraints.

ScriptEvaluatorNotFoundException

Exception raised when a script evaluator cannot be found for a given language.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved