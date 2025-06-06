# Movie Recommendation System

---

## Project Structure

| File/Folder               | Description                                        |
|--------------------------|--------------------------------------------------|
| `.idea/`                 | IDE configuration files (PyCharm or similar)      |
| `.ipynb_checkpoints/`    | Jupyter notebook autosaves                         |
| `.gitattributes`         | Git LFS tracking configuration for large files    |
| `app.py`                 | Main Python script to run the recommendation app  |
| `model.ipynb`            | Jupyter notebook with data exploration and model development |
| `movies.pkl`             | Serialized movie metadata for fast loading         |
| `similarity.pkl`         | Large precomputed similarity matrix (tracked with Git LFS) |
| `tmdb_5000_credits.csv`  | TMDB dataset file containing movie credits         |
| `tmdb_5000_movies.csv`   | TMDB dataset file containing movie metadata        |
| `requirement.txt`        | Python dependencies required for the project       |

---

## Overview

This is a **Content-Based Movie Recommendation System** that recommends movies by analyzing content features from the TMDB dataset and computing similarity scores between movies. It uses a precomputed similarity matrix to quickly fetch recommendations.

## Note

The similarity matrix file `similarity.pkl` is large (~180MB) and managed via Git Large File Storage (LFS). If cloning the repo, ensure Git LFS is set up to download this file correctly.

## Getting Started

### Prerequisites

- Python(I used 3.12 )
- Git LFS installed and configured (for handling `similarity.pkl`)



### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourrepo.git
    cd yourrepo
    ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the similarity matrix (handled via Git LFS).

---


Feel free to customize this content with your own repo URL, file names, or additional features!


