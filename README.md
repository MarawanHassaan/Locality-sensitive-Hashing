# Locality-Sensitive Hashing (LSH) Implementation

This repository contains a Python implementation of Locality-Sensitive Hashing (LSH), a technique used for approximate nearest neighbor searches in high-dimensional data. The project includes implementations of MinHashing, shingling, and hashing functions, making it a powerful tool for tasks such as duplicate detection, clustering, and similarity search.

---

## Features

- **MinHashing**: Generate compact signatures for sets or documents to estimate Jaccard similarity.
- **Shingling**: Create shingles (subsets) from input data for text similarity analysis.
- **LSH Buckets**: Group similar data points into the same bucket for efficient lookup.
- **Sample Dataset**: Includes a `apartments.tsv` file for testing the implementation.

---

## Project Structure

- **`HashGenerator.py`**: Contains functions to generate hash values for input data.
- **`LSH.py`**: Implements the Locality-Sensitive Hashing algorithm.
- **`Main.py`**: Entry point for running the LSH workflow.
- **`Minhash.py`**: Provides the MinHash algorithm for approximate Jaccard similarity computation.
- **`Shingles.py`**: Functions for creating shingles from input data.
- **`apartments.tsv`**: Example dataset for testing purposes.

---

## Installation and Usage

### Prerequisites
- Python 3.x installed on your system
- Dependencies listed in `requirements.txt`

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MarawanHassaan/Locality-sensitive-Hashing.git
2. **Navigate to the Directory**:
   ```bash
    cd Locality-sensitive-Hashing
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Run the application***
   ```bash
   python.main
## How It Works
1. Shingling: Converts input documents into sets of shingles (fixed-size substrings).
2. MinHashing: Creates a signature matrix for the shingled data to reduce dimensionality.
3. LSH: Maps the MinHash signatures into buckets such that similar documents land in the same bucket, enabling fast lookups.
