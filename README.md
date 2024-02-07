# Movie Recommendation System 🎬

## Table of Contents 📚

- [Project Details](#project-details)
- [Data Extraction](#data-extraction)
- [Data Preprocessing](#data-preprocessing)
- [Machine Learning Algorithms](#machine-learning-algorithms)
- [Webpage](#webpage) (streamlit)
- [Presentation](#presentation)
- [Usage](#usage)

## Project Details 🌐

This project focuses on building a movie recommendation system using machine learning algorithms. It involves data extraction from TMDB (The Movie Database), data preprocessing, application of machine learning algorithms, and creating a user-friendly webpage using Streamlit.

## Data Extraction 📊

The dataset used in this project is obtained from TMDB and consists of two main files: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`. These datasets provide information about movies, including details like genres, keywords, cast, and crew.

## Data Preprocessing 🧹

Data preprocessing involves handling missing values, removing duplicates, and converting string representations of lists to actual lists using the ast library. The final preprocessed data is used to create feature vectors for movie recommendations.

## Machine Learning Algorithms 🤖

The project utilizes machine learning algorithms, specifically cosine similarity, to determine the similarity between movies based on their tags (overview, genres, keywords, cast, and crew). The similarity matrix is then used to recommend movies similar to a user's selection.

## Webpage (Streamlit) 🌐

The user interface for the movie recommendation system is implemented using Streamlit. The webpage allows users to select a movie and receive recommendations based on the selected movie.

## 📷 Screenshots

* <h3>Home Page</h3>
![Home page / search bar](https://github.com/mayurpaunikar7/Movie-Recommender-System/blob/main/Images/WhatsApp%20Image%202024-02-07%20at%204.31.07%20PM.jpeg)

* <h3>Top Statistics</h3>
![Home page / search bar](https://github.com/mayurpaunikar7/Movie-Recommender-System/blob/main/Images/WhatsApp%20Image%202024-02-07%20at%204.35.42%20PM.jpeg)

* <h3>Message distribution over time</h3>
![Home page / search bar](https://github.com/mayurpaunikar7/Movie-Recommender-System/blob/main/Images/WhatsApp%20Image%202024-02-07%20at%204.35.59%20PM.jpeg)

* <h3>Message distribution over time</h3>
![Home page / search bar](https://github.com/mayurpaunikar7/Movie-Recommender-System/blob/main/Images/WhatsApp%20Image%202024-02-07%20at%204.33.11%20PM.jpeg)

## Presentation 📊

The presentation includes visualizations and insights derived from the analysis. It provides a clear overview of how the recommendation system works and its potential applications.

## Usage 🚀

To use the movie recommendation system:

1. Clone the repository.
2. Ensure that the required libraries are installed (`numpy`, `pandas`, `matplotlib`, `seaborn`, `nltk`, `scikit-learn`, `streamlit`).
3. Run the Streamlit app using the command `streamlit run app.py`.
4. Follow the instructions on the webpage to select and receive movie recommendations.

Feel free to explore the Jupyter Notebook files and the Python scripts for more details on each step of the project.
