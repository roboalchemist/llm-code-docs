# Source: https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/managing-index-size.md

# Managing Index Size

## What is Indexable Size?&#x20;

Indexable size is size of all code files, excluding following from the folder:&#x20;

* **Directory/File based filtering**
  * logs, node\_modules, dist, target, bin, package-lock.json, data.json, build, .gradle, .idea, gradle, extension.js, vendor.js, ngsw\.json, polyfills.js, ngsw-worker.js, runtime.js, runtime-main.js, service-worker.js, bundle.js, bundle.css
* **Extension based filtering**
  * bin, exe, dll, log, aac, avif, bmp, cda, gif ,mp3, mp4, mpeg, weba, webm, webp, oga, ogv, png, jpeg, jpg, bmp, wpa, tif, tiff, svg, ico, wav, mov, avi, doc, docx, ppt, pptx, xls, xlsx, ods, odp, odt, pdf, epub, rar, tar, zip, vsix, 7z, bz, bz2, gzip, jar, war, gz, tgz, woff, woff2, eot, ttf, map, apk, app, ipa, lock, tmp, logs, gmo, pt
* **Hidden files are filtered** i.e., files starting with "."&#x20;
* **All Empty files are filtered.**&#x20;
* **All Binary files are also filtered.**

## Is there any limit on repository size?&#x20;

For workspaces that have upgraded to Bito's **Team Plan**, we have set the indexable size limit to 120MB per repo. However, once we launch the "AI that Understands Your Code" feature for our **Free Plan** users, they will be restricted to repositories with an indexable size limit of 10MB.

Learn more about [**indexable size**](#what-is-indexable-size) above and see which files and folders are excluded by default.

You can reduce your repo's indexable size by excluding certain files and folders from indexing using [**.bitoignore**](#what-is-.bitoignore-and-how-to-use-it) file and remain within the limit.

## What if a repo hits 120MB limit?

If a repo hits 120MB limit, then the below error message will be displayed in the "Manage repos" tab and the repo's index status will be changed to "Not Indexed".

{% hint style="danger" %}
Sorry, we don’t currently support repos of this size. Please use .bitoignore to reduce the size of the repo you want Bito to index.
{% endhint %}

To fix this issue, follow our instructions regarding [**how to use .bitoignore file**](#what-is-.bitoignore-and-how-to-use-it) and reduce your repo's size and bring it under the max limit of 120MB.

After that, you must [**delete the index**](https://docs.bito.ai/ai-code-reviews-in-ide/faqs#how-to-delete-project-index-from-ide) and then restart the indexing by clicking on the "Start Indexing" button shown for the repo folder. You can also follow our step-by-step guides to [**Start Indexing in Visual Studio Code**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/using-in-visual-studio-code) and [**Start Indexing in JetBrains**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/using-in-jetbrains-ides) IDEs.

## What is .bitoignore and how to use it?

A `.bitoignore` file is a plain text file where each line contains a pattern or rules that tells Bito which files or directories to ignore and not index. In other words, it's a way to reduce your repo's indexable size. You can also see [**which files/folders are excluded by default**](#what-is-indexable-size).

**There are two ways to use `.bitoignore` file:**

1. Create a `.bitoignore` file inside the folder where indexes created by Bito are stored. e.g. `<user-home-directory>/.bito/localcodesearch/.bitoignore`
   * On Windows, this path will be something like: `C:\Users\<your username>\.bito\localcodesearch\.bitoignore`
   * **Note:** The custom ignore rules you set in this `.bitoignore` file will be applied to all the repositories where you have **enabled indexing**.
2. Create a `.bitoignore` file inside your repository's root folder.

{% hint style="info" %}
If a **.gitignore** file is available in your repo then Bito will also use that to ignore files & folders from indexing process. Both **.bitoignore** and **.gitignore** files can work together without any issues.
{% endhint %}

{% hint style="info" %}
At present, Bito considers only those **.gitignore** files that are placed in the project root directory and **.bitoignore** files that are placed either in `<user-home-directory\.bito\localcodesearch>` or `<project-root-directory>`
{% endhint %}

Changes to the `.bitoignore` file are taken into account at the beginning of the indexing process, not during or after the indexing itself.

Therefore, to implement changes made to the `.bitoignore` file, you'll need to [**delete the index**](https://docs.bito.ai/ai-code-reviews-in-ide/faqs#how-to-delete-project-index-from-ide) and then restart the indexing by clicking on the "Start Indexing" button shown for the repo folder. You can also follow our step-by-step guides to [**Start Indexing in Visual Studio Code**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/using-in-visual-studio-code) and [**Start Indexing in JetBrains**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/using-in-jetbrains-ides) IDEs.

{% hint style="info" %}
Please note that any changes to the **.bitoignore** or **.gitignore** file will take a minimum of 3 to 5 minutes to trigger new indexing.
{% endhint %}

## Common .bitoignore Patterns <a href="#common-.bitoignore-patterns" id="common-.bitoignore-patterns"></a>

Understanding these patterns/rules is crucial for effectively managing the files and directories that Bito indexes and excludes in your projects.

<table><thead><tr><th width="330">Sample Rule</th><th>Description</th></tr></thead><tbody><tr><td><code># this is a comment.</code></td><td>Any line that starts with a <code>#</code> symbol is considered as a comment and will not be processed.</td></tr><tr><td><code>*</code></td><td>(Wildcard character) Ignores all files</td></tr><tr><td><code>**</code></td><td>(Wildcard character) Match any number of directories.</td></tr><tr><td><code>todo.txt</code></td><td>Ignores a specific file named <code>todo.txt</code></td></tr><tr><td><code>*.txt</code></td><td>Ignores all files ending with <code>.txt</code></td></tr><tr><td><code>*.*</code></td><td>Ignores all files with any extension.</td></tr><tr><td><code>Engine/</code> or <code>Engine/**</code></td><td>Ignores all files in the <code>Engine</code> directory and their subdirectories (contents).</td></tr><tr><td><code>subdirectory1/example.html</code></td><td>Ignore the file named <code>example.html</code>, specifically located in the directory named <code>subdirectory1</code>.</td></tr><tr><td><code>!contacts.txt</code></td><td>(Negation Rule) Explicitly tracks <code>contacts.txt</code>, even if all <code>.txt</code> files are ignored.</td></tr><tr><td><code>!Engine/Batch/Builds</code></td><td>(Negation Rule) Tracks the <code>Builds</code> directory inside <code>Engine/Batch</code>, overriding a broader exclusion.</td></tr><tr><td><code>!Engine/Batch/Builds/**</code></td><td>(Negation Rule) Tracks the <code>Builds</code> directory and all of its subdirectories inside <code>Engine/Batch</code>, overriding a broader exclusion.</td></tr><tr><td><code>!.java</code></td><td>(Negation Rule) Ensures that all <code>.java</code> files are included, overriding any previous ignore rules that might apply to them.</td></tr><tr><td><code>!subdirectory1/*.txt</code></td><td>(Negation Rule) Track files with the <code>.txt</code> extension located specifically in the <code>subdirectory1</code> directory, even if other rules might otherwise ignore <code>.txt</code> files.</td></tr><tr><td><code>BitoUtil?.java</code></td><td>The <code>?</code> (question mark) matches any single character in a filename or directory name.</td></tr></tbody></table>

## Negation `!` (exclamation mark)

When a pattern starts with `!` it negates the pattern, meaning it explicitly includes files or directories that would otherwise be ignored. For example, have a look at this sample **.bitoignore** file:

{% tabs %}
{% tab title=".bitoignore" %}

```
Engine/**
!Engine/Build/BatchFiles/**
```

{% endtab %}
{% endtabs %}

&#x20;Here `!Engine/Build/BatchFiles/**` pattern includes all files in the `Engine/Build/BatchFiles` directory and its subdirectories, even though `Engine/**` pattern would ignore them.

{% hint style="info" %}
**Avoid Ambiguous Patterns:** Negation patterns can become confusing when they potentially match multiple files. Target specific files or folders rather than using wildcards in negation patterns.

For example, it is better to use patterns like **`!Engine/Build/BatchFiles/script.bat`** instead of **`!Engine/Build/BatchFiles/**`**
{% endhint %}

## .bitoignore Examples

### Exclude Files/Folders

```
# Ignore specific file named "config.ini"
config.ini

# Ignore all files with a '.bak' extension
*.bak

# Ignore all files with a '.kunal' extension
*.kunal

# Exclude directories
backup
temp/
dist/vendor
```

### Exclude Everything Except Specific Files

To exempt a file, ensure that the negation pattern `!` appears afterward, thereby overriding any broader exclusions.

```
# Ignore all files except C++, header and python files
*
!*.cpp
!*.h
!*.py
```
