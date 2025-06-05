# 📰 Neutralizing Headlines

A Natural Language Processing (NLP) project that transforms **sensationalized** news headlines into a **neutral and factual tone** using a fine-tuned text generation model. This promotes responsible journalism and reduces emotional manipulation in news media.

## 🔍 Problem Statement

Many media headlines are written in an emotionally charged manner to attract attention, often at the cost of factual accuracy. This project aims to **neutralize such headlines**, preserving meaning while removing sensational language.

## 🎯 Project Goals

- Detect and transform sensational headlines to a neutral tone.
- Use NLP models to rewrite text while preserving key information.
- Provide a user-friendly interface or API for input-output interaction.

## 🛠️ Tech Stack

- **Language Model**: BART (fine-tuned)
- **Framework**: Hugging Face Transformers
- **Dataset**: Custom-labeled Kaggle dataset (sensational vs. neutral)
- **Deployment**: Hugging Face Spaces 
- **Others**: Python, PyTorch, scikit-learn, Pandas

## 🧠 Model Overview

The model was fine-tuned on pairs of:
