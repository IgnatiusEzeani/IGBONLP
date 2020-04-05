

# Igbo-English Machine Translation: An Evaluation Benchmark

So far, this repository contains a collection of human corrected and validated Igbo monolingual data and human-translated Igbo-English sentence pairs for training machine translation systems as presented in this paper:
[Igbo-English Machine Translation: An Evaluation Benchmark](https://arxiv.org/abs/2004.00648)). Work on the comparative experiments for the Ig-En MT baselines are still on-going and will be included soon. 

## Repo Content:
This repo contains both the **monolingual** and **parallell (Ig-En)** data:
### Monolingual data:
The content summary is presented below while the source details can be found [here](https://github.com/IgnatiusEzeani/IGBONLP/blob/master/ig_en_mt/ig_data/summary.txt):
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

|language pair| devset | testset|testset (hidden)|
|---|---|---|---|
|Igbo-English| 10000| 1000| 584|

```latex
\begin{table}[!ht]
\caption{Breakdown of the Benchmark Evaluation Parallel Data}
\label{breakdown}
\centering
\begin{tabular}{lrl}
\hline
\multicolumn{1}{l}{\textbf{Type}}&\multicolumn{1}{c}{\textbf{Sent pairs}}&\multicolumn{1}{l}{\textbf{Sources}}\\
\hline
\textit{Igbo-English} & 5,836 & \url{https://www.bbc.com/igbo}\\
\textit{English-Igbo} & 5,748 & Mostly from local newspapers (e.g. Punch)\\
\hline
\textit{Total} & $11,584$ &\\
\hline
\end{tabular}
\caption{Splits of the Benchmark Evaluation Parallel Data}
\label{splits}
\begin{tabular}{lrl}
\hline
\textbf{Evaluation Splits} & \textbf{IG-EN} & \textbf{EN-IG}\\
\hline
\textit{Development Set} & 5000 & \multicolumn{1}{r}{5000}\\
\textit{Test set} & 500 & \multicolumn{1}{r}{500}\\
\textit{Hidden Test} & 336 & \multicolumn{1}{r}{248}\\
\hline
\end{tabular}
\end{table}
```

## Citation
```bibtex
@misc{ezeani2020igboenglish,
    title={Igbo-English Machine Translation: An Evaluation Benchmark},
    author={Ignatius Ezeani and Paul Rayson and Ikechukwu Onyenwe and Chinedu Uchechukwu and Mark Hepple},
    year={2020},
    eprint={2004.00648},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
