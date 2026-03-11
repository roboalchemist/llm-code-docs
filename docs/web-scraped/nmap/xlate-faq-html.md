# Source: https://nmap.org/xlate-faq.html

Title: Nmap Man Page Translation FAQ

URL Source: https://nmap.org/xlate-faq.html

Markdown Content:
[Download](https://nmap.org/download.html)[Reference Guide](https://nmap.org/book/man.html)[Book](https://nmap.org/book/)[Docs](https://nmap.org/docs.html)[Zenmap GUI](https://nmap.org/zenmap/)[In the Movies](https://nmap.org/movies/)
So you want to translate the [Nmap Reference Guide](https://nmap.org/book/man.html) (man page) to another language? We appreciate that, and potential Nmap users who read that language likely appreciate it even more! The most popular translations are viewed on the web thousands of times per month, and also made part of regional Linux (and other OS) distributions. This FAQ gives instructions on how to get started, how to credit yourself in the translation, etc.

1.   **How do I start?**
First, check the [Nmap Documentation Page](https://nmap.org/docs.html) to insure that a translation in your desired language isn't already available. If the language is already done, but you want to improve it, see the later question about [correcting mistakes or updating a translation](https://nmap.org/xlate-faq.html#xlate-correct).

If you find that your language isn't available, we'd love to have a translation. The man pages are written using the [DocBook XML](http://www.docbook.org/) format. This makes it easy to convert them to HTML, man page (nroff) format, PDF guides, etc. You _must_ translate the XML source, rather than starting with HTML or Nroff, or doing it in Word. The source to translate can be found at [https://nmap.org/data/nmap-man.xml](https://nmap.org/data/nmap-man.xml).

Now you are ready to begin translating text. Using an XML editor or just a normal text editor, translate nmap-man.xml to your chosen language. The formatting is in XML tags such as <refsect1 id="man-options">, <title>, etc. Don't replace those tags -- leave them just as they are. Only replace the text around and enclosed by the tags. There are a few additions (such as your names and a disclaimer) that should be added to your translation. See the question on [XML additions](https://nmap.org/xlate-faq.html#xml-additions). The file name of your translation should be nmap-man-[langprefix].xml. Langprefix is the standard ISO abbreviations for the language. For example, the Portuguese (Brazil) version would be nmap-man-pt-br.xml . The Italian version is nmap-man-it.xml .

Send me the translated XML file. An email attachment or linking to a web page or CVS repository is OK. I'll use my scripts to convert it to a web page to post to Insecure.Org and an Nroff man page. Yay! If I don't acknowledge receipt within 2 days, mail me again. I'm worried that my spam filter might catch some of them due to receiving messages in unusual (for my mailbox) languages. But this hasn't been a problem with the dozen translations we have so far.

2.   **The language I'm doing needs special character encoding for Unicode or what not. How do I handle that?**
Most languages are using UTF-8 or ISO-8859-1. Alternatively, you could use UTF-16. The team needs to agree on a common encoding for their contributions. The encoding is then specified at the top of the file, as in these three examples:

<?xml version="1.0" encoding="ISO-8859-1"?>
<?xml version="1.0" encoding="UTF-8"?>
<?xml version="1.0" encoding="UTF-16"?>
3.   **What if an existing translation contains errors or is out of date?**
If there is just a mis-spelled word or small grammar error, I wouldn't worry about it. It shouldn't hinder readers much. But if there are a lot of little errors (like you find 10 or more), those add up and are probably worth fixing. To do this, downloaded the translated XML file which will have the name nmap-man-[ISO-LANGUAGE-CODE].xml and reside in the browseable [https://nmap.org/data/man-xlate/](https://nmap.org/data/man-xlate/) directory. Just make your changes and send the new version to [Fyodor](mailto:fyodor@nmap.org). He will then update the XML on the web site and also reconvert to HTML and Nroff.

Nmap is always changing, so these reference guides will eventually become dated. If you find this has happened for a language you care about, you are welcome and encouraged to update it. First, check if there is an XML version number that the translated was based on. It should be in a "Translation Notes" (see [this question](https://nmap.org/xlate-faq.html#xml-additions) type of section. If not, it isn't a big deal. Mail Fyodor that version number (if available) and indicate which language you want to update. Fyodor will send a list of changes made in the English version since the translation was done. This is usually a lot easier to handle than trying to compare the documents alone and determine what has changed.

4.   **What if I find a problem in the English nmap-man.xml file?**
If there is a typoe, spelling error, or other problem in the English version, please [mail me](mailto:fyodor@nmap.org) describing the problem. Content suggestions are appreciated too.

5.   **Where should we add our names and other translation information? What else should be added to the file?**
There is some extra information that will definitely be useful to add to your translation. This includes:

    *   Name(s) of the Translator(s) 
    *   Version number of the English XML file that you translated 
    *   Copyright license for your translation (I recommend the [Creative Commons Attribution License](http://creativecommons.org/licenses/by/2.5/)), which is what the English version is under. 
    *   Disclaimer that this is an unofficial translation 

To do this, I suggest adding two new sections. The first is a new "translation" section. You may want to put it near the beginning, such as between "Description" and "Options Summary". This section should be in your target language. Here is the suggested text:

> <refsect1 id="man-translation">
>   <title>Translation Notes</title>
> 
>   <para>This [Finnish] edition of the Nmap Reference Guide has
>   been translated from version [2940] of the <ulink
>   url="https://nmap.org/book/man.html">original English
>   version</ulink> by [Linus Torvalds
>   <email>torvalds@osdl.org</email> and CmdrTaco
>   <email>malda@slashdot.org</email>].  While [we/I] hope
>   this will make Nmap more accessible to [Finnish] speakers worldwide,
>   [we/I] cannot guarantee that this translation is as complete or
>   up-to-date as the official English version.  This work may be
>   modified and redistributed under the terms of the <ulink
>   url="http://creativecommons.org/licenses/by/2.5/">Creative
>   Commons Attribution License</ulink>.</para>
> </refsect1>

Of course, the stuff in brackets ([]) should be changed to the relevant values for your translation. You may or may not want to include email addresses. They are sure to be picked up by spammers if you do. It is your decision whether to include, omit, or obfuscate your email address in the translation you are working on. The license link above includes links to versions in many languages. You can link directly to your language if you wish. The version number in the section is taken from the top of the English nmap-man.xml you translated, where you will find a comment like this:

<!-- $Id: manhtml.xml 2991 2005-12-12 10:21:33Z fyodor $ -->

In this case (above), the version number is 2991.

The second new section (actually a subsection) is a translation disclaimer that should be added to the legal issues section. This is mostly taken from [wording the FSF uses for GPL translations](http://www.gnu.org/licenses/translations.html). This should be added _in both English and the target language_ right after the "Legal Notices" heading:

> <refsect2 id="translation-disclaimer">
>   <title>Unofficial Translation Disclaimer / [Title in target
>   language]</title>
> 
>   <para>This is an unnofficial translation of the <ulink
>   url="https://nmap.org/book/man-legal.html">Nmap
>   license details</ulink> into [Finnish].  It was not written by
>   Nmap Software LLC, and does not legally state the distribution terms
>   for Nmap -- only the original English text does that.  However, we
>   hope that this translation helps [Finish] speakers understand the
>   Nmap license better.</para>
> 
>   <para>[text above in target language]</para>
> </refsect2>

6.   **What if I have other questions?**
If you have any other questions, [mail fyodor](mailto:fyodor@nmap.org).
