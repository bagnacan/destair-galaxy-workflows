<div id="top"></div>

# Workflows

This repository contains a collection of workflows created using the [de.STAIR atoms](https://github.com/destairdenbi/galaxy-atoms). These are incorporated in the [Galaxy workflow generator](https://github.com/destairdenbi/galaxy-workflow-generator)
to provide a baseline of working use-cases, which users can adopt to familiarize with
Galaxy tools for DGEA and RRBS/BS-Seq data analyses.

- [Run workflows](#run-workflows)
- [Contributed workflows](#contributed-workflows)
  - [DGE analysis (single-end reads)](#dge-analysis-single-end-reads)
  - [DGE analysis (paired-end reads)](#dge-analysis-paired-end-reads)
  - [RRBS/BS-Seq analysis (paired-end reads)](#rrbsbs-seq-analysis-paired-end-reads)



## Run workflows

Workflows depend on their tools, which in turn are available depending on the Galaxy
*flavor* in use. For this reason, to make these workflows run it is important to make
sure that you are running the [Galaxy workflow generator](https://github.com/destairdenbi/galaxy-workflow-generator).  

From the Galaxy workflow generator header, click ``Workflow``, and chose which one to
run.
<p align="right"><a href="#top">&#x25B2; back to top</a></p>



## Contributed workflows

The Galaxy workflow generator provides workflows for DGEA and RRBS/BS-Seq data
analyses.  
<p align="right"><a href="#top">&#x25B2; back to top</a></p>



### DGE analysis (single-end reads)
- [FastQC + Trim Galore! --> BWA --> AWK + Infer Experiment + featureCounts + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/se/fastqc__trim_galore__bwa__awk__infer_experiment__featurecounts__deseq2.ga)
- [FastQC + Trim Galore! --> BWA --> AWK + Infer Experiment + HTSeq-count + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/se/fastqc__trim_galore__bwa__awk__infer_experiment__htseq-count__deseq2.ga)
- [FastQC + Trim Galore! --> HISAT2 --> AWK + Infer Experiment + featureCounts + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/se/fastqc__trim_galore__hisat2__awk__infer_experiment__featurecounts__deseq2.ga)
- [FastQC + Trim Galore! --> segemehl --> AWK + Infer Experiment + featureCounts + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/se/fastqc__trim_galore__segemehl__awk__infer_experiment__featurecounts__deseq2.ga)
- [FastQC + Trim Galore! --> segemehl --> AWK + Infer Experiment + HTSeq-count + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/se/fastqc__trim_galore__segemehl__awk__infer_experiment__htseq-count__deseq2.ga)
- [FastQC + Trimmomatic --> BWA --> AWK + Infer Experiment + featureCounts + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/se/fastqc__trimmomatic__bwa__awk__infer_experiment__featurecounts__deseq2.ga)
- [FastQC + Trimmomatic --> BWA --> AWK + Infer Experiment + HTSeq-count + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/se/fastqc__trimmomatic__bwa__awk__infer_experiment__htseq-count__deseq2.ga)
- [FastQC + Trimmomatic --> HISAT2 --> AWK + Infer Experiment + featureCounts + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/se/fastqc__trimmomatic__hisat2__awk__infer_experiment__featurecounts__deseq2.ga)
- [FastQC + Trimmomatic --> HISAT2 --> AWK + Infer Experiment + HTSeq-count + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/se/fastqc__trimmomatic__hisat2__awk__infer_experiment__htseq-count__deseq2.ga)
- [FastQC + Trimmomatic --> segemehl --> AWK + Infer Experiment + featureCounts + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/se/fastqc__trimmomatic__segemehl__awk__infer_experiment__featurecounts__deseq2.ga)
- [FastQC + Trimmomatic --> segemehl --> AWK + Infer Experiment + HTSeq-count + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/se/fastqc__trimmomatic__segemehl__awk__infer_experiment__htseq-count__deseq2.ga)
- [FastQC + Trimmomatic --> STAR --> AWK + Infer Experiment + featureCounts + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/se/fastqc__trimmomatic__star__awk__infer_experiment__featurecounts__deseq2.ga)
- [FastQC + Trimmomatic --> STAR --> AWK + Infer Experiment + HTSeq-count + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/se/fastqc__trimmomatic__star__awk__infer_experiment__htseq-count__deseq2.ga)
<p align="right"><a href="#top">&#x25B2; back to top</a></p>



### DGE analysis (paired-end reads)
- [FastQC + Cutadapt --> BWA --> AWK + Infer Experiment + featureCounts + DESeq2.ga](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/pe/fastqc__cutadapt__bwa__awk__infer_experiment__featurecounts__deseq2.ga)
- [FastQC + Cutadapt --> BWA --> AWK + Infer Experiment + HTSeq-count + DESeq2.ga](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/pe/fastqc__cutadapt__bwa__awk__infer_experiment__htseq-count__deseq2.ga)
- [FastQC + Cutadapt --> HISAT2 --> AWK + Infer Experiment + featureCounts + DESeq2.ga](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/pe/fastqc__cutadapt__hisat2__awk__infer_experiment__featurecounts__deseq2.ga)
- [FastQC + Cutadapt --> HISAT2 --> AWK + Infer Experiment + HTSeq-count + DESeq2.ga](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/pe/fastqc__cutadapt__hisat2__awk__infer_experiment__htseq-count__deseq2.ga)
- [FastQC + Cutadapt --> STAR --> AWK + Infer Experiment + featureCounts + DESeq2.ga](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/pe/fastqc__cutadapt__star__awk__infer_experiment__featurecounts__deseq2.ga)
- [FastQC + Cutadapt --> STAR --> AWK + Infer Experiment + HTSeq-count + DESeq2.ga](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/pe/fastqc__cutadapt__star__awk__infer_experiment__htseq-count__deseq2.ga)
- [FastQC + PRINSEQ --> BWA --> AWK + Infer Experiment + featureCounts + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/pe/fastqc__prinseq__bwa__awk__infer_experiment__featurecounts__deseq2.ga)
- [FastQC + PRINSEQ --> BWA --> AWK + Infer Experiment + HTSeq-count + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/pe/fastqc__prinseq__bwa__awk__infer_experiment__htseq-count__deseq2.ga)
- [FastQC + PRINSEQ --> HISAT2 --> AWK + Infer Experiment + featureCounts + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/pe/fastqc__prinseq__hisat2__awk__infer_experiment__featurecounts__deseq2.ga)
- [FastQC + PRINSEQ --> HISAT2 --> AWK + Infer Experiment + HTSeq-count + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/pe/fastqc__prinseq__hisat2__awk__infer_experiment__htseq-count__deseq2.ga)
- [FastQC + PRINSEQ --> STAR --> AWK + Infer Experiment + featureCounts + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/pe/fastqc__prinseq__star__awk__infer_experiment__featurecounts__deseq2.ga)
- [FastQC + PRINSEQ --> STAR --> AWK + Infer Experiment + HTSeq-count + DESeq2](https://raw.githubusercontent.com/destairdenbi/galaxy-workflows/master/dgea/pe/fastqc__prinseq__star__awk__infer_experiment__htseq-count__deseq2.ga)
<p align="right"><a href="#top">&#x25B2; back to top</a></p>



### RRBS/BS-Seq analysis (paired-end reads)
<p align="right"><a href="#top">&#x25B2; back to top</a></p>
