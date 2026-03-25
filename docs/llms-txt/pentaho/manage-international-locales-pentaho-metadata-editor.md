# Source: https://docs.pentaho.com/pba-metadata-editor/manage-international-locales-pentaho-metadata-editor.md

# Source: https://docs.pentaho.com/pba-metadata-editor/pdia-9.3-metadata-editor/manage-international-locales-pentaho-metadata-editor.md

# Source: https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/manage-international-locales-pentaho-metadata-editor.md

# Manage international locales

Pentaho Metadata Editor supports multiple locale entries for any text or string-based metadata property. You must first specify the locales you want to include in your model by using the **Locales Editor**.

Perform the following steps to set up locales:

1. In the Pentaho Metadata Editor, go to **Tools** > **Locales Editor**.
2. Place your cursor in the first column of the first empty row in the **Locales Editor** main table, as shown in the following example:

   ![Locales tab, Pentaho Metadata Editor](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-cfe6739c782dfd24d1e005012aff4bd0a0174669%2F43_pme_locale.png?alt=media)
3. Type the [Java Locale code](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html) of the language you want to add in the next column.
4. Specify the order in which you want this locale to be used.

   In the example above, `English (American)` is designated as the first language (**Order** = `1`).
5. Type a **Y** in the last column to activate the locale, or an **N** to de-activate it.
6. Click **Apply Changes** when you are done.
