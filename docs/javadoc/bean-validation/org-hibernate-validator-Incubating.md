# Annotation Interface Incubating

---

@Documented
@Retention(CLASS)
public @interface Incubating
Marks the annotated element as incubating. The contract of incubating elements (e.g. packages, types, methods,
constants etc.) is under active development and may be incompatibly altered - or removed - in subsequent releases.

Usage of incubating API/SPI members is encouraged (so the development team can get feedback on these new features)
but you should be prepared for updating code which is using them as needed.

Author:
Gunnar Morling

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved