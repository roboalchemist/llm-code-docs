# Source: https://doc.qt.io/qtforpython-6/developer/index.html

Title: Developer Notes - Qt for Python

URL Source: https://doc.qt.io/qtforpython-6/developer/index.html

Markdown Content:
Developer Notes - Qt for Python
===============
- [x] - [x] [Skip to content](https://doc.qt.io/qtforpython-6/developer/index.html#furo-main-content)

[Qt for Python](https://doc.qt.io/qtforpython-6/index.html)

[![Image 1: Logo](https://doc.qt.io/qtforpython-6/_static/qtforpython.png) Qt for Python](https://doc.qt.io/qtforpython-6/index.html)

*   [Getting Started](https://doc.qt.io/qtforpython-6/gettingstarted.html)
*   [Commercial Use](https://doc.qt.io/qtforpython-6/commercial/index.html)
*   [Building from Source](https://doc.qt.io/qtforpython-6/building_from_source/index.html)
*   [Package Details](https://doc.qt.io/qtforpython-6/package_details.html)
*   [Modules API](https://doc.qt.io/qtforpython-6/api.html)
*   [Tools](https://doc.qt.io/qtforpython-6/tools/index.html)
*   [Tutorials](https://doc.qt.io/qtforpython-6/tutorials/index.html)
*   [Examples](https://doc.qt.io/qtforpython-6/examples/index.html)
*   [Videos](https://doc.qt.io/qtforpython-6/videos.html)
*   [Deployment](https://doc.qt.io/qtforpython-6/deployment/index.html)
*   [Considerations](https://doc.qt.io/qtforpython-6/considerations.html)
*   [Developer Notes](https://doc.qt.io/qtforpython-6/developer/index.html#)- [x] 
    *   [Add a new module](https://doc.qt.io/qtforpython-6/developer/add_module.html)
    *   [Add a new example or port one](https://doc.qt.io/qtforpython-6/developer/add_port_example.html)
    *   [Add a new tool or a Qt tool wrapper](https://doc.qt.io/qtforpython-6/developer/add_tool.html)
    *   [Adapting to changes in supported Python versions](https://doc.qt.io/qtforpython-6/developer/pythonversions.html)
    *   [Fixing Documentation issues](https://doc.qt.io/qtforpython-6/developer/documentation.html)
    *   [Adapt to new Qt versions](https://doc.qt.io/qtforpython-6/developer/adapt_qt.html)
    *   [Test a wheel](https://doc.qt.io/qtforpython-6/developer/extras.html)
    *   [Build on the command line](https://doc.qt.io/qtforpython-6/developer/extras.html#build-on-the-command-line)
    *   [Build with address sanitizer (Linux)](https://doc.qt.io/qtforpython-6/developer/extras.html#build-with-address-sanitizer-linux)
    *   [Build with thread sanitizer](https://doc.qt.io/qtforpython-6/developer/extras.html#build-with-thread-sanitizer)
    *   [De-Virtualize the Python Files](https://doc.qt.io/qtforpython-6/developer/extras.html#de-virtualize-the-python-files)
    *   [QtAsyncio developer notes](https://doc.qt.io/qtforpython-6/developer/qtasyncio.html)
    *   [Signalmanager](https://doc.qt.io/qtforpython-6/developer/signalmanager.html)
    *   [Description](https://doc.qt.io/qtforpython-6/developer/signalmanager.html#description)
    *   [The Set of Enum Features](https://doc.qt.io/qtforpython-6/developer/enumfeatures_doc.html)
    *   [The Transition To The Limited Python API (PEP384)](https://doc.qt.io/qtforpython-6/developer/limited_api.html)
    *   [The signature C extension](https://doc.qt.io/qtforpython-6/developer/signature_doc.html)
    *   [Improving the Quality of Signatures with mypy](https://doc.qt.io/qtforpython-6/developer/mypy-correctness.html)
    *   [Why do we have a __feature__?](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html)
    *   [The snake_case feature](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#the-snake-case-feature)
    *   [The true_property feature](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#the-true-property-feature)
    *   [The __feature__ import](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#the-feature-import)
    *   [Qt Remote Objects Overview](https://doc.qt.io/qtforpython-6/developer/remoteobjects.html)
    *   [Fixing Type Hints](https://doc.qt.io/qtforpython-6/developer/fix_type_hints.html)

*   [Release Notes](https://doc.qt.io/qtforpython-6/release_notes/index.html)
*   [Module Index](https://doc.qt.io/qtforpython-6/contents.html)

[Back to top](https://doc.qt.io/qtforpython-6/developer/index.html#)
Developer Notes[¶](https://doc.qt.io/qtforpython-6/developer/index.html#developer-notes "Link to this heading")
===============================================================================================================

Developing Qt for Python requires people to understand different processes and steps that need to be taken into account when dealing with topics related to modules, bindings, examples, and more.

Development Topics[¶](https://doc.qt.io/qtforpython-6/developer/index.html#development-topics "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

*   [Add a new module](https://doc.qt.io/qtforpython-6/developer/add_module.html)
    *   [Add bindings](https://doc.qt.io/qtforpython-6/developer/add_module.html#add-bindings)
    *   [Distribution](https://doc.qt.io/qtforpython-6/developer/add_module.html#distribution)
    *   [Add documentation](https://doc.qt.io/qtforpython-6/developer/add_module.html#add-documentation)

*   [Add a new example or port one](https://doc.qt.io/qtforpython-6/developer/add_port_example.html)
    *   [Add a new example](https://doc.qt.io/qtforpython-6/developer/add_port_example.html#add-a-new-example)
    *   [Port a Qt example](https://doc.qt.io/qtforpython-6/developer/add_port_example.html#port-a-qt-example)

*   [Add a new tool or a Qt tool wrapper](https://doc.qt.io/qtforpython-6/developer/add_tool.html)
    *   [Add a new tool](https://doc.qt.io/qtforpython-6/developer/add_tool.html#add-a-new-tool)
    *   [Add a Qt tool wrapper](https://doc.qt.io/qtforpython-6/developer/add_tool.html#add-a-qt-tool-wrapper)

*   [Adapting to changes in supported Python versions](https://doc.qt.io/qtforpython-6/developer/pythonversions.html)
    *   [Relevant preprocessor defines](https://doc.qt.io/qtforpython-6/developer/pythonversions.html#relevant-preprocessor-defines)
    *   [Removing outdated Python versions](https://doc.qt.io/qtforpython-6/developer/pythonversions.html#removing-outdated-python-versions)
    *   [Adapting to new Python versions](https://doc.qt.io/qtforpython-6/developer/pythonversions.html#adapting-to-new-python-versions)

*   [Fixing Documentation issues](https://doc.qt.io/qtforpython-6/developer/documentation.html)
    *   [Fixing texts](https://doc.qt.io/qtforpython-6/developer/documentation.html#fixing-texts)
    *   [Fixing snippets](https://doc.qt.io/qtforpython-6/developer/documentation.html#fixing-snippets)
    *   [Maintaining additionaldocs.lst](https://doc.qt.io/qtforpython-6/developer/documentation.html#maintaining-additionaldocs-lst)
    *   [Inheritance graphs](https://doc.qt.io/qtforpython-6/developer/documentation.html#inheritance-graphs)

*   [Adapt to new Qt versions](https://doc.qt.io/qtforpython-6/developer/adapt_qt.html)
    *   [Adapting to source changes](https://doc.qt.io/qtforpython-6/developer/adapt_qt.html#adapting-to-source-changes)
    *   [Bumping the version](https://doc.qt.io/qtforpython-6/developer/adapt_qt.html#bumping-the-version)

*   [Test a wheel](https://doc.qt.io/qtforpython-6/developer/extras.html)
*   [Build on the command line](https://doc.qt.io/qtforpython-6/developer/extras.html#build-on-the-command-line)
*   [Build with address sanitizer (Linux)](https://doc.qt.io/qtforpython-6/developer/extras.html#build-with-address-sanitizer-linux)
*   [Build with thread sanitizer](https://doc.qt.io/qtforpython-6/developer/extras.html#build-with-thread-sanitizer)
*   [De-Virtualize the Python Files](https://doc.qt.io/qtforpython-6/developer/extras.html#de-virtualize-the-python-files)
*   [QtAsyncio developer notes](https://doc.qt.io/qtforpython-6/developer/qtasyncio.html)
    *   [QtAsyncio vs asyncio](https://doc.qt.io/qtforpython-6/developer/qtasyncio.html#qtasyncio-vs-asyncio)
    *   [The step function](https://doc.qt.io/qtforpython-6/developer/qtasyncio.html#the-step-function)
    *   [Keeping QtAsyncio in sync with asyncio](https://doc.qt.io/qtforpython-6/developer/qtasyncio.html#keeping-qtasyncio-in-sync-with-asyncio)
    *   [asyncio developer guidance](https://doc.qt.io/qtforpython-6/developer/qtasyncio.html#asyncio-developer-guidance)

*   [Signalmanager](https://doc.qt.io/qtforpython-6/developer/signalmanager.html)
*   [Description](https://doc.qt.io/qtforpython-6/developer/signalmanager.html#description)
    *   [Issues](https://doc.qt.io/qtforpython-6/developer/signalmanager.html#issues)
    *   [Plans](https://doc.qt.io/qtforpython-6/developer/signalmanager.html#plans)

Implementation details[¶](https://doc.qt.io/qtforpython-6/developer/index.html#implementation-details "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

Complementary, here you can find the reasoning and motivation for the many features and implementation details that the project has:

*   [The Set of Enum Features](https://doc.qt.io/qtforpython-6/developer/enumfeatures_doc.html)
    *   [The Possible Enum Flags](https://doc.qt.io/qtforpython-6/developer/enumfeatures_doc.html#the-possible-enum-flags)
    *   [The most likely flags needed](https://doc.qt.io/qtforpython-6/developer/enumfeatures_doc.html#the-most-likely-flags-needed)
    *   [Flags for completeness](https://doc.qt.io/qtforpython-6/developer/enumfeatures_doc.html#flags-for-completeness)

*   [The Transition To The Limited Python API (PEP384)](https://doc.qt.io/qtforpython-6/developer/limited_api.html)
    *   [Foreword](https://doc.qt.io/qtforpython-6/developer/limited_api.html#foreword)
    *   [Changed Modules](https://doc.qt.io/qtforpython-6/developer/limited_api.html#changed-modules)
    *   [Using The New Type API](https://doc.qt.io/qtforpython-6/developer/limited_api.html#using-the-new-type-api)
    *   [Future Versions Of The Limited API](https://doc.qt.io/qtforpython-6/developer/limited_api.html#future-versions-of-the-limited-api)
    *   [Appendix A: The Transition To Simpler Types](https://doc.qt.io/qtforpython-6/developer/limited_api.html#appendix-a-the-transition-to-simpler-types)
    *   [Appendix B: Verification Of PyTypeObject](https://doc.qt.io/qtforpython-6/developer/limited_api.html#appendix-b-verification-of-pytypeobject)

*   [The signature C extension](https://doc.qt.io/qtforpython-6/developer/signature_doc.html)
    *   [Short Introduction to the Topic](https://doc.qt.io/qtforpython-6/developer/signature_doc.html#short-introduction-to-the-topic)
    *   [The Idea to Support Signatures](https://doc.qt.io/qtforpython-6/developer/signature_doc.html#the-idea-to-support-signatures)
    *   [Impacts of The Signature Module](https://doc.qt.io/qtforpython-6/developer/signature_doc.html#impacts-of-the-signature-module)
    *   [Update and Future of the Signature Module](https://doc.qt.io/qtforpython-6/developer/signature_doc.html#update-and-future-of-the-signature-module)
    *   [Literature](https://doc.qt.io/qtforpython-6/developer/signature_doc.html#literature)

*   [Improving the Quality of Signatures with mypy](https://doc.qt.io/qtforpython-6/developer/mypy-correctness.html)
    *   [Preliminary](https://doc.qt.io/qtforpython-6/developer/mypy-correctness.html#preliminary)
    *   [Running the mypy Tests](https://doc.qt.io/qtforpython-6/developer/mypy-correctness.html#running-the-mypy-tests)
    *   [Types of mypy Errors](https://doc.qt.io/qtforpython-6/developer/mypy-correctness.html#types-of-mypy-errors)
    *   [Unsolvable Errors](https://doc.qt.io/qtforpython-6/developer/mypy-correctness.html#unsolvable-errors)
    *   [Conclusion and Future](https://doc.qt.io/qtforpython-6/developer/mypy-correctness.html#conclusion-and-future)
    *   [Literature](https://doc.qt.io/qtforpython-6/developer/mypy-correctness.html#literature)

*   [Why do we have a __feature__?](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html)
    *   [History](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#history)
    *   [Why are features selectable per-module?](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#why-are-features-selectable-per-module)
    *   [Why dunder, and why not __future__?](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#why-dunder-and-why-not-future)

*   [The snake_case feature](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#the-snake-case-feature)
*   [The true_property feature](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#the-true-property-feature)
    *   [Normal Properties](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#normal-properties)
    *   [Special Properties](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#special-properties)
    *   [Class properties](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#class-properties)
    *   [About Property Completeness](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#about-property-completeness)
    *   [Name Clashes and Solution](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#name-clashes-and-solution)

*   [The __feature__ import](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#the-feature-import)
    *   [Overriding __import__](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#overriding-import)
    *   [IDEs and Modifying Python stub files](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#ides-and-modifying-python-stub-files)
    *   [Using __feature__ with UIC files](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#using-feature-with-uic-files)

*   [Qt Remote Objects Overview](https://doc.qt.io/qtforpython-6/developer/remoteobjects.html)
    *   [Replicas are _latent copies_](https://doc.qt.io/qtforpython-6/developer/remoteobjects.html#replicas-are-latent-copies)
    *   [How does this affect PySide?](https://doc.qt.io/qtforpython-6/developer/remoteobjects.html#how-does-this-affect-pyside)
    *   [RepFile PySide type](https://doc.qt.io/qtforpython-6/developer/remoteobjects.html#repfile-pyside-type)
    *   [Replica type](https://doc.qt.io/qtforpython-6/developer/remoteobjects.html#replica-type)
    *   [Source type](https://doc.qt.io/qtforpython-6/developer/remoteobjects.html#source-type)
    *   [Realizing Source/Replica types in python](https://doc.qt.io/qtforpython-6/developer/remoteobjects.html#realizing-source-replica-types-in-python)

*   [Fixing Type Hints](https://doc.qt.io/qtforpython-6/developer/fix_type_hints.html)
    *   [Overview](https://doc.qt.io/qtforpython-6/developer/fix_type_hints.html#overview)
    *   [Tools and Setup](https://doc.qt.io/qtforpython-6/developer/fix_type_hints.html#tools-and-setup)
    *   [Finding Type Hints Issues](https://doc.qt.io/qtforpython-6/developer/fix_type_hints.html#finding-type-hints-issues)
    *   [How to Fix](https://doc.qt.io/qtforpython-6/developer/fix_type_hints.html#how-to-fix)
    *   [Rebuild and Verify](https://doc.qt.io/qtforpython-6/developer/fix_type_hints.html#rebuild-and-verify)
    *   [Special Cases and Workarounds](https://doc.qt.io/qtforpython-6/developer/fix_type_hints.html#special-cases-and-workarounds)

[Next Add a new module](https://doc.qt.io/qtforpython-6/developer/add_module.html)[Previous Considerations](https://doc.qt.io/qtforpython-6/considerations.html)

 Copyright © 2026 The Qt Company Ltd. Documentation contributions included herein are the copyrights of their respective owners. The documentation provided herein is licensed under the terms of the GNU Free Documentation License version 1.3 (https://www.gnu.org/licenses/fdl.html) as published by the Free Software Foundation. Qt and respective logos are trademarks of The Qt Company Ltd. in Finland and/or other countries worldwide. All other trademarks are property of their respective owners. 

 Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me/)'s [Furo](https://github.com/pradyunsg/furo)

 On this page 

*   [Developer Notes](https://doc.qt.io/qtforpython-6/developer/index.html#)
    *   [Development Topics](https://doc.qt.io/qtforpython-6/developer/index.html#development-topics)
    *   [Implementation details](https://doc.qt.io/qtforpython-6/developer/index.html#implementation-details)
