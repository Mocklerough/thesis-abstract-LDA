# thesis-abstract-LDA

As part of the literature review on my master's thesis, perform LDA on the set of 328 article abstracts related to LLM usage in social research.

This represents an important step in the thesis writign process. Having discovered relevant research, the LDA is intendd to provode initial groupigns and topic discovery to help sort through the large number of documents. The LDA-discovered categories will assist in assessing areas of research that LLMs are currently being applied to in social research, while also sorting and organizing them. This minimizes a tedious and difficult start, where otherwise I would have a pile of 291 research articles and facced with the challenge of pouring through each individualy while at the same time attempting to identify macro-level trends in research.

## Project Steps

### Prereq: Gather Relevant Research

This has been done by 1) Identifying relevant computational social science journals and high-quality methods journals across the social sciences, then either manually reviewing journal titles/abstracts from the past few years (2020-2024) or using keyword search to identify articles related to LLMs or generative AI. This is merely an initial search, prioritizing quik reviews to achieve a large startig corpus and being only loosely-guided by earlier work outline the thesis' argument, 

These articles were collected using Zotero. A manual cleaning step ensured each article had an abstract, proper citation, and were not duplicated.

### Prepare corpus of Article Abstracts

Zotero does not natively allow the direct download of just isolated abstracts, but the `Generate Report` option is useful here to produce an HTML file of the `Info` data of all articles in a collection. From here, there are a few tools available online to pull abstracts, but I found none that were maintained and unbroken, or that gave the exact data I need to feed into an LDA. Since this HTML file is well-formatted, a simple HTML-parser can be easily build in Python.
