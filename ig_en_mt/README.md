# Igbo-English Machine Translation: An Evaluation Benchmark

So far, this repository contains a collection of human corrected and validated Igbo monolingual data and human-translated Igbo-English sentence pairs for training machine translation systems as presented in this paper:
[Igbo-English Machine Translation: An Evaluation Benchmark](https://arxiv.org/abs/2004.00648). Work on the comparative experiments for the Ig-En MT baselines are still on-going and will be included soon. 

---
## Citation
```bibtex
@misc{ezeani2020igboenglish,
    title={Igbo-English Machine Translation: An Evaluation Benchmark},
    author={Ignatius Ezeani and Paul Rayson and Ikechukwu Onyenwe and Chinedu Uchechukwu and Mark Hepple},
    year={2020},
    eprint={2004.00648},
    archivePrefix={arXiv},
    primaryClass={cs.CL},
    url={https://arxiv.org/abs/2004.00648}
}
```
---
## Repo Content:
This repo contains both the **monolingual** and **parallell (Ig-En)** data:
### Monolingual data:
The content summary is presented below while the source details can be found [here](https://github.com/IgnatiusEzeani/IGBONLP/tree/master/ig_monoling):
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

### Parallel (IG-EN) data:


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

|Type| Sent pairs | Source |
|---|---:|---|
*Igbo-English* | 5,836 | News from [BBC Igbo](https://www.bbc.com/igbo) website
*English-Igbo* | 5,748 | News from Nigerian newspapers (e.g. [Punch](https://punchng.com/))
**Total** | 11,584 |

The data splits into *Dev set*, *Test set* and *hidden set* are shown below. The *hidden set* is held out for further evaluations on trained and tested MT models. 

|Evaluation Splits | IG-EN | EN-IG |
|---|---:|---:|
*Devset* | 5000 | 5000 |
*Testset* | 500 | 500 |
*Hidden* | 336 | 248 |

## Usage
Running the `read_data.py` creates the ParallelData class which builds the *Devset* and the *testset* with its `get_evalsets()` method. The following example produces the results below:

```python
par_data = ParallelData(datapath)
par_data.get_evalsets()

#Igbo sents
print("\n".join(par_data.devset[0][:5]))
print('-'*10)

#English sents
print("\n".join(par_data.devset[1][:5]))
```
Output:
```
---Igbo sentences:
Akụkọ ndị ga-amasị gị:
Joseph Achuzie, Dike Biafra alala
Dapchi: Gọọmenti emeribeghị Boko Haram - Massob
Tottenham na-ele anya iburu iko FA na mmeri Rochadale
Son Heung-min, Fernando Llorente na Kyle Walter-Peters nke Tottenham bụ ndị mmechiri ọnụ Rochadale n'asọmpị ụnyaahụ.

---English sentences:
The news that will interest you:
Joseph Achuzie, the Biafran brave man is gone.
Dapchi: Government  has not defeated Boko Haram and Massob
Tottenham look forward to lifting the FA cup in defeating Rochadale.
Son Heung-min, Fernando Llorente and Kyle Walter-Peters of Tottenham beat Rochadale mercilessly in their yesterday's FA cup competition.
```
