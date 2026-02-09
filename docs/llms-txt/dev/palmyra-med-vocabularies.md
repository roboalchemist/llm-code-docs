# Source: https://dev.writer.com/home/palmyra-med-vocabularies.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Palmyra Med vocabularies and entities

Palmyra Med supports the following medical vocabularies:

* Foundational Model of Anatomy
* Gene Ontology
* HUGO Gene Nomenclature Committee
* Human Phenotype Ontology
* ICD-10 Procedure Coding System
* ICD-10-CM (available for US users only)
* ICD-9-CM
* LOINC
* MeSH
* MedlinePlus Health Topics
* Metathesaurus Names
* NCBI Taxonomy
* NCI Thesaurus
* National Drug File
* Online Mendelian Inheritance in Man
* RXNORM
* SNOMED CT (available for US users only)

## Extracting entities, relations, and contextual attributes

Palmyra-Med uses context-aware models to extract medical entities, relations, and contextual attributes. Each text entity is extracted into a medical dictionary entry.

<Info>The maximum size of the medical text is 10,000 Unicode characters.</Info>

Palmyra-Med supports the following medical knowledge categories:

|                   |                                                                                                                                        |
| :---------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| BM\_UNIT          | Body measurement unit                                                                                                                  |
| BM\_VALUE         | Value of a body measurement                                                                                                            |
| BODY\_FUNCTION    | Function carried out by the human body                                                                                                 |
| BODY\_MEASUREMENT | A normal measurement of the human body, such as a vital sign                                                                           |
| LABORATORY\_DATA  | Results of testing a bodily sample                                                                                                     |
| LAB\_RESULT       | Qualitative description of laboratory data, such as increased, decreased, positive, or negative                                        |
| LAB\_UNIT         | Unit of measurement for a laboratory value                                                                                             |
| LAB\_VALUE        | Value of an instance of laboratory data                                                                                                |
| MEDICAL\_DEVICE   | Physical or virtual instrument                                                                                                         |
| MEDICINE          | Drug or other preparation for treatment or prevention of disease                                                                       |
| MED\_DOSE         | Medication dose                                                                                                                        |
| MED\_DURATION     | Medication duration                                                                                                                    |
| MED\_FORM         | Physical characteristics of the specific medication                                                                                    |
| MED\_FREQUENCY    | How often the medication is taken                                                                                                      |
| MED\_ROUTE        | Body location at which the medication is administered                                                                                  |
| MED\_STATUS       | For an existing medication, status can be a modifier such as "continue", "start", "restart", "stop", "switch", "increase", "decrease". |
| MED\_STRENGTH     | Amount of active ingredient in a dose of medication                                                                                    |
| MED\_TOTALDOSE    | Quantity of medication to take at one time                                                                                             |
| MED\_UNIT         | Unit of measurement for the active ingredient in a medication                                                                          |
| PROBLEM           | Medical condition, including findings and diseases                                                                                     |
| PROCEDURE\_RESULT | Results of a procedure                                                                                                                 |
| PROCEDURE         | Diagnostic or treatment procedure                                                                                                      |
| PROC\_METHOD      | Method in which a procedure is conducted                                                                                               |
| SEVERITY          | Severity of the medical condition                                                                                                      |
| SUBSTANCE\_ABUSE  | Abuse of a psychoactive substance                                                                                                      |
