# Source: https://www.exim.org/exim-html-current/doc/html/spec_html/filter.html

Title: Exim's interfaces to mail filtering

URL Source: https://www.exim.org/exim-html-current/doc/html/spec_html/filter.html

Markdown Content:
Exim's interfaces to mail filtering
===============

[Exim Internet Mailer](https://www.exim.org/)
=============================================

*   [Home](https://www.exim.org/index.html)
*   [Download](https://www.exim.org/download.html)
*   [Documentation](https://www.exim.org/docs.html)
*   [Mailing Lists](https://www.exim.org/maillist.html)
*   [Wiki](http://wiki.exim.org/)
*   [Bugs](https://bugs.exim.org/)
*   [Security](https://www.exim.org/static/doc/security)
*   [Credits](https://www.exim.org/credits.html)
*   [Legal](https://www.exim.org/legal.html)

Exim's interfaces to mail filtering
-----------------------------------

Copyright © 2024 The Exim Maintainers

Revision 4.99.1 - 17 Dec 2025

![Image 1](https://www.exim.org/static/doc/plus-12x12.png)![Image 2](https://www.exim.org/static/doc/minus-12x12.png)Expand/Collapse all Chapters

*    1. [Forwarding and filtering in Exim](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-forwarding_and_filtering_in_exim.html)
    *   1. [Introduction](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-forwarding_and_filtering_in_exim.html#SEC00)
    *   2. [Filter operation](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-forwarding_and_filtering_in_exim.html#SEC01)
    *   3. [Testing a new filter file](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-forwarding_and_filtering_in_exim.html#SECTtesting)
    *   4. [Installing a filter file](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-forwarding_and_filtering_in_exim.html#SEC02)
    *   5. [Testing an installed filter file](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-forwarding_and_filtering_in_exim.html#SEC03)
    *   6. [Details of filtering commands](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-forwarding_and_filtering_in_exim.html#SEC04)

*    2. [Sieve filter files](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-sieve_filter_files.html)
    *   1. [Recognition of Sieve filters](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-sieve_filter_files.html#SEC05)
    *   2. [Saving to specified folders](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-sieve_filter_files.html#SEC06)
    *   3. [Strings containing header names](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-sieve_filter_files.html#SEC07)
    *   4. [Exists test with empty list of headers](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-sieve_filter_files.html#SEC08)
    *   5. [Header test with invalid MIME encoding in header](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-sieve_filter_files.html#SEC09)
    *   6. [Address test for multiple addresses per header](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-sieve_filter_files.html#SEC10)
    *   7. [Semantics of keep](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-sieve_filter_files.html#SEC11)
    *   8. [Semantics of fileinto](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-sieve_filter_files.html#SEC12)
    *   9. [Semantics of redirect](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-sieve_filter_files.html#SEC13)
    *   10. [String arguments](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-sieve_filter_files.html#SEC14)
    *   11. [Number units](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-sieve_filter_files.html#SEC15)
    *   12. [RFC compliance](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-sieve_filter_files.html#SEC16)

*    3. [Exim filter files](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html)
    *   1. [Format of Exim filter files](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SEC17)
    *   2. [Data values in filter commands](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SEC18)
    *   3. [String expansion](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTfilterstringexpansion)
    *   4. [Some useful general variables](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SEC19)
    *   5. [Header variables](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTheadervariables)
    *   6. [User variables](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SEC20)
    *   7. [Current directory](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SEC21)
    *   8. [Significant deliveries](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTsigdel)
    *   9. [Filter commands](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SEC222)
    *   10. [The add command](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTadd)
    *   11. [The deliver command](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTdeliver)
    *   12. [The save command](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTsave)
    *   13. [The pipe command](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTpipe)
    *   14. [Mail commands](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTmail)
    *   15. [Logging commands](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTlog)
    *   16. [The finish command](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTfinish)
    *   17. [The testprint command](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTtestprint)
    *   18. [The fail command](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTfail)
    *   19. [The freeze command](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTfreeze)
    *   20. [The headers command](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTheaders)
    *   21. [Obeying commands conditionally](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTif)
    *   22. [String testing conditions](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SEC23)
    *   23. [Numeric testing conditions](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SEC24)
    *   24. [Testing for significant deliveries](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SEC25)
    *   25. [Testing for error messages](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SEC26)
    *   26. [Testing a list of addresses](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SEC27)
    *   27. [Testing for personal mail](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTpersonal)
    *   28. [Alias addresses for the personal condition](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SEC28)
    *   29. [Details of the personal condition](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SEC29)
    *   30. [Testing delivery status](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SEC30)
    *   31. [Multiple personal mailboxes](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTmbox)
    *   32. [Ignoring delivery errors](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SEC43)
    *   33. [Examples of Exim filter commands](https://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html#SECTex)

Website design by [Mike Cardwell](https://www.grepular.com/).

*   [Home](https://www.exim.org/index.html)
*   [Download](https://www.exim.org/download.html)
*   [Documentation](https://www.exim.org/docs.html)
*   [Mailing Lists](https://www.exim.org/maillist.html)
*   [Wiki](http://wiki.exim.org/)
*   [Bugs](https://bugs.exim.org/)
*   [Security](https://www.exim.org/static/doc/security)
*   [Credits](https://www.exim.org/credits.html)
*   [Legal](https://www.exim.org/legal.html)
