# ShulaTech_Solutions_Iris_Flower_Classification

## Overview
This project implements a machine learning model to classify iris flowers into three species: *Iris-setosa*, *Iris-versicolor*, and *Iris-virginica*. The classification is performed using the **K-Nearest Neighbors (KNN)** algorithm.

## Dataset
- **Name:** `iris.csv`
- **Description:** The Iris dataset contains 150 samples with the following features:
  - *Sepal Length* (cm)
  - *Sepal Width* (cm)
  - *Petal Length* (cm)
  - *Petal Width* (cm)
  - *Species* (Target variable)

## Project Structure
- `Iris_Flower_Classification_using_KNN.ipynb`: The Jupyter notebook containing code for data loading, exploration, visualization, preprocessing, and model training.
- `iris.csv`: The dataset file used for model training and evaluation.

## Steps Performed
1. **Data Loading:** The dataset is imported using pandas.
2. **Exploratory Data Analysis (EDA):**
   - Viewing dataset shape and basic statistics.
   - Displaying the first few rows of the data.
   - Checking the distribution of flower species.
3. **Data Visualization:**
   - Generating histograms to understand feature distributions.
   - Creating scatter plots to visualize relationships between features.
4. **Data Preprocessing:**
   - Encoding categorical species names into numerical values.
   - Splitting the dataset into features (*X*) and target (*y*).
5. **Model Training:**
   - Implementing the KNN algorithm using scikit-learn.
   - Training the model on the dataset.
   - Evaluating model performance.

## Requirements
- **Python Libraries:**
  - pandas
  - numpy
  - matplotlib
  - scikit-learn

Install required libraries using:
```bash
pip install pandas numpy matplotlib scikit-learn
```

## Usage
1. Open the `Iris_Flower_Classification_using_KNN.ipynb` notebook in Jupyter or Google Colab.
2. Run the notebook cells sequentially.
3. Observe data exploration, visualization outputs, and model performance metrics.

## Model Evaluation
The notebook evaluates the KNN model's performance using appropriate metrics such as accuracy. Additional evaluation metrics can be added as needed.

## License
This project is for educational purposes.

---
*Developed as part of a machine learning classification task using the Iris dataset.*

