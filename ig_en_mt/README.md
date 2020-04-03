

# Igbo-English Machine Translation: An Evaluation Benchmark

This repository contains a collection of human corrected and validated Igbo monolingual data and human-translated Igbo-English sentence pairs for training machine translation systems as presented in this paper:
[Igbo-English Machine Translation: An Evaluation Benchmark](https://arxiv.org/abs/2004.00648)).

## Repo Content:
This repo contains:
### Monolingual data:
The content summary is presented below while the source details can be found [here]():
| Filename | Sentences | Tokens | UniqTkns|
| --- |  ---: | ---: | ---: |
|eze_goes_to_school.txt | 1,272 | 25,413 | 2,616 |
|mmadu_ka_a_na_aria.txt | 2,023 | 39,731 | 3,292 |
|bbc-igbo.txt | 34,056 | 566,804 | 28,459|
|igbo-radio.txt | 5,131 | 191,450 | 13,391|
|jw-ot-igbo.txt | 32,251 | 712,349 | 13,417 |
|jw-nt-igbo.txt | 10,334 | 253,806 | 6,731|
|jw-books.txt | 142,753 | 1,879,755 | 25,617|
|jw-teta.txt | 14,097 | 196,818 | 7,689|
|jw-ulo_nche.txt | 277,60 | 392,412 | 10,868|
|jw-ulo_nche_naamu.txt | 113,772 | 1,465,663 | 17,870|
|**Total** | **383449** | **5724201** | **69091**|

Work on the baseslines is on-going following the approach used [Facebook Research FloRes Project](https://github.com/facebookresearch/flores) and wil be released in this repo when ready.

<!-- Code to reproduce the baselines is available at: https://github.com/facebookresearch/flores -->
<!--
V1 - Submitted: 1 Apr 2020

+ Languages included: Sinhalese<>English, Nepali <> English.
+ Initial Sinhalese to English and Nepali to English sets that pass quality thresholds.
Fluency rating > 3.0/5.0 , Translation rating > 70.0/100.0
+ Translations with multiple references have been merged as additional training examples.
+ Direct and reverse translations are mixed at approx. 50%.
+ Merging several references as test examples.
+ The sets are as follows:
-->

|language pair| devset | testset|testset (hidden)|
|---|---|---|---|
|Igbo-English| 10000| 1000| 584|

## Citation
```bibtex
@inproceedings{ezeani_ig_en_evalset_2020,
author={Ezeani, Ignatius and Rayson, Paul and Onyenwe, Ikechukwu and Uchechukwu, Chinedu, Hepple, Mark},
title={Igbo-English Machine Translation: An Evaluation Benchmark},
journal={arXiv preprint arXiv:2004.00648},
year={2020}
}
```
