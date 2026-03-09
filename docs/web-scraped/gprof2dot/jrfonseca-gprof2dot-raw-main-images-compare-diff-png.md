# Source: https://github.com/jrfonseca/gprof2dot/raw/main/images/compare_diff.png

Title: compare_diff.png

URL Source: https://github.com/jrfonseca/gprof2dot/raw/main/images/compare_diff.png

Markdown Content:
compare_diff.png
===============

Pgfplots: easier use of foreach with conditional checking I'd like to have this block #28 in my figure: \NewDocumentCommand{\mycov}{{c} #1 % <#1=row, <#2=coll, <#3=data, if<#3>แกน x else แกน y} { \node[draw, circle, inner sep=0pt, label={above:#1<#2}, text=black, fill, font=\tiny] at (#3) (x\pgfplotspointmeta){#3}; \node[labels=#3 label={left:($x\pgfplotspointmeta$) }];
