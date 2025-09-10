# 📰 Neutralizing Headlines

A collaborative Natural Language Processing (NLP) project that transforms sensationalized news headlines into a neutral and factual tone using a fine-tuned text generation model. This promotes responsible journalism and reduces emotional manipulation in news media.

[![Open in Spaces](https://img.shields.io/badge/🤗-Open%20in%20Spaces-blue.svg)](https://huggingface.co/spaces/your-username/your-space-name)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🔍 Problem Statement

Modern media often relies on emotionally charged headlines to attract clicks, a practice that can distort facts and manipulate readers. This project addresses the issue by leveraging AI to automatically rephrase sensationalist language into neutral, factual statements without losing the core meaning of the headline.

## 🎯 Project Goals

*   **Detection & Transformation:** Identify emotionally charged language in headlines and transform them into a neutral tone.
*   **Faithful Rewriting:** Utilize advanced NLP models to ensure key information (who, what, where, when) is preserved during the rewriting process.
*   **Accessibility:** Provide a simple, user-friendly interface (web demo & API) for public use and experimentation.

## 🛠️ Tech Stack

*   **Language Model:** [BART](https://huggingface.co/docs/transformers/model_doc/bart) (Bidirectional and Auto-Regressive Transformers), fine-tuned on a custom dataset.
*   **Frameworks:** Hugging Face Transformers, PyTorch
*   **Dataset:** Curated from [Kaggle](https://www.kaggle.com/datasets/) (pairs of sensational and neutral headlines)
*   **Deployment:** [Hugging Face Spaces](https://huggingface.co/spaces) for a live demo
*   **Development:** Python, Pandas, scikit-learn, Jupyter Notebook

## 🧠 Model Overview

The core of this project is a BART model fine-tuned in a text-to-text format. The training data consisted of pairs of sensational and neutral headlines, teaching the model the mapping between biased and objective language.

**Input (Sensational):** `"SHOCKING: Politician Unveils RADICAL New Plan That Will DESTROY The Economy!"`

**Output (Neutral):** `"Politician Proposes New Economic Plan."`

