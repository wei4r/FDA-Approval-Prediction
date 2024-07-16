# FDA Drug Approval Prediction
## 2022 AI Project - Introduction to AI, National Yang Ming Chiao Tung University

### Overview
This project utilizes machine learning to predict whether compounds will be approved by the FDA as drugs. The goal is to streamline the drug development process by leveraging predictive models to estimate approval likelihood, significantly reducing time and financial costs associated with drug development.

## Datasets
The primary dataset used is **[DrugBank](https://go.drugbank.com)**, a comprehensive and freely accessible online database containing information about drugs and drug targets. It includes:
- 2037 FDA-approved small molecule drugs
- 241 FDA-approved biotech (protein/peptide) drugs
- 96 nutraceuticals
- Over 6000 experimental drugs

## Features
Features are derived using molecular fingerprints, focusing on different substructures or moieties represented in one-hot encoding. Several systems are used to increase feature diversity, including:
- **Checkmol**
- **PubChem**
- **Rings in drugs**
- **MACCS**
- Total of 1744 features.

## Models
We use tree-based machine learning models for this classification problem:
- **Support Vector Machine (SVM)**
- **Random Forest**
- **XGBoost**

## Main Approach
1. **Data Preprocessing**: Data is cleaned and prepared using `Preprocess.py`.
2. **Feature Engineering**: Chemical features are generated with `exec_checkmol` and `exec_Matchmol`.
3. **Model Training**: Models are trained using the engineered features to predict FDA approval.

## Evaluation Metrics
Models are evaluated using:
- **Accuracy**
- **Area Under the ROC Curve (AUC)**

## Related Work
The methodological framework is inspired by existing research and tools:
- **Checkmol** for molecule checking
- **PubChem** for chemical information
- **Molecular Graph Neural Networks with SMILES**

## Acknowledgements
This project is part of the coursework for the Introduction to AI class at National Yang Ming Chiao Tung University. We thank all contributors and data providers for their support.
