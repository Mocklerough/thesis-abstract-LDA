# thesis-abstract-LDA

As part of the literature review on my master's thesis, perform LDA on the set of 328 article abstracts related to LLM usage in social research.

This represents an important step in the thesis writign process. Having discovered relevant research, the LDA is intendd to provode initial groupigns and topic discovery to help sort through the large number of documents. The LDA-discovered categories will assist in assessing areas of research that LLMs are currently being applied to in social research, while also sorting and organizing them. This minimizes a tedious and difficult start, where otherwise I would have a pile of 291 research articles and facced with the challenge of pouring through each individualy while at the same time attempting to identify macro-level trends in research.

## Project Steps

### Prereq: Gather Relevant Research

This has been done by 1) Identifying relevant computational social science journals and high-quality methods journals across the social sciences, then either manually reviewing journal titles/abstracts from the past few years (2020-2024) or using keyword search to identify articles related to LLMs or generative AI. This is merely an initial search, prioritizing quik reviews to achieve a large startig corpus and being only loosely-guided by earlier work outline the thesis' argument, 

These articles were collected using Zotero. A manual cleaning step ensured each article had an abstract, proper citation, and were not duplicated.

### Prepare corpus of Article Abstracts

Zotero does not natively allow the direct download of just isolated abstracts, but the `Generate Report` option is useful here to produce an HTML file of the `Info` data of all articles in a collection. From here, there are a few tools available online to pull abstracts, but I found none that were maintained and unbroken, or that gave the exact data I need to feed into an LDA. Since this HTML file is well-formatted, a simple HTML-parser can be easily build in Python.

### Run and fine-tune LDA

LDAs ran with limited success, due to the very high overlap in topic among documents (ia, llm, appearing in almost every abstract). Added tf-idf, which improved results a bit. Playing around just with the number of topics, 4-6 topics appear to give ok groupings. 

## Project Retrospective

The groupings unfortunately didn't prove very fruitful for the downstream work of my thesis in reviewing the literature. This is because of two reasons:
- Limited data: Only using the abstracts likely didn't capture enough of the research for the topic models to make use of. Zotero made getting abstracts easy, but scraping each research article .pdf for the full text would be a meaningful amount of work.
- Limited fine-tuning: adding tf-idf significantly improved results, but I did little in the way of tuning parameters, exploring other ways to tokenize, create dictionaries, etc. Massaging the model parameters might give some small gains, but I believe the resutls are far enough from beign useful that this would not be profitable.
- Results did not align with later work: Having seen these topics, they do not appear to be helpful in my task of reviewing and digesting the literature. FOr my purposes, mere groups of related research isn't enough, and I'm looking for som deeper insight. LDA's process of tokenization reduces analysis to word-level existence, whcih drops their context and relationships that make their source research articles relevant, thus losing the context I meant to gain insight in.

Maybe moving to something more advanced would help, ironically using a language model (treatign this data as a fine-tuning dataset) might work pretty well. However, a constraint here is time: I spent all of an 8-hour work day figuring this out, which was worth finding otu that it doesn't work. Extending this to a week-long project is then too much work to apply here, when I still need to do the meat-and-potatoes work of reading and thinking about the literature. 
