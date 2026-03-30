# Package org.h2.bnf

---

package org.h2.bnf

The implementation of the BNF (Backus-Naur form) parser and tool.

- 

Related Packages

Package
Description
org.h2

Implementation of the JDBC driver.

org.h2.bnf.context

Classes that provide context for the BNF tool, in order to provide BNF-based
 auto-complete.

- 

Class
Description
Bnf

This class can read a file that is similar to BNF (Backus-Naur form).

BnfVisitor

The visitor interface for BNF rules.

Rule

Represents a BNF rule.

RuleElement

A single terminal rule in a BNF object.

RuleExtension

Represents a non-standard syntax.

RuleFixed

Represents a hard coded terminal rule in a BNF object.

RuleHead

Represents the head of a BNF rule.

RuleList

Represents a sequence of BNF rules, or a list of alternative rules.

RuleOptional

Represents an optional BNF rule.

RuleRepeat

Represents a loop in a BNF object.

Sentence

A query context object.