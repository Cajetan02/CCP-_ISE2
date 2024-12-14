
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Bar Chart of Sales Data
class BarChart:
    @staticmethod
    def plot_sales(file_path):
        data = pd.read_csv(file_path)
        plt.bar(data['Region'], data['Sales'], color='skyblue')
        plt.title('Sales by Region')
        plt.xlabel('Region')
        plt.ylabel('Sales')
        plt.show()

# Line Chart of Temperature Changes
class LineChart:
    @staticmethod
    def plot_temperature(file_path):
        data = pd.read_csv(file_path)
        plt.plot(data['Day'], data['Temperature'], color='blue', marker='o')
        plt.title('Temperature Trend')
        plt.xlabel('Days')
        plt.ylabel('Temperature')
        plt.show()

# Scatter Plot of Student Scores
class ScatterPlot:
    @staticmethod
    def plot_scores(file_path):
        data = pd.read_csv(file_path)
        plt.scatter(data['Hours Studied'], data['Scores Obtained'], color='red')
        plt.title('Study Hours vs Scores')
        plt.xlabel('Hours Studied')
        plt.ylabel('Scores Obtained')
        plt.show()

# Histogram of Exam Scores
class Histogram:
    @staticmethod
    def plot_scores_distribution(file_path):
        data = pd.read_csv(file_path)
        plt.hist(data['Exam Scores'], bins=10, color='green', edgecolor='black')
        plt.title('Exam Scores Distribution')
        plt.xlabel('Scores')
        plt.ylabel('Frequency')
        plt.show()

# Heatmap of Correlation
class Heatmap:
    @staticmethod
    def plot_correlation(file_path):
        data = pd.read_csv(file_path)
        sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.show()

# Wave Plot of Sine and Cosine
class WavePlot:
    @staticmethod
    def plot_sine_and_cosine():
        x = np.linspace(0, 2 * np.pi, 100)
        plt.plot(x, np.sin(x), label='Sine')
        plt.plot(x, np.cos(x), label='Cosine')
        plt.title('Sine and Cosine Waves')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()

# Box Plot of House Prices
class BoxPlot:
    @staticmethod
    def plot_price_distribution(file_path):
        data = pd.read_csv(file_path)
        sns.boxplot(x='House Type', y='Price', data=data)
        plt.title('Price Distribution by House Type')
        plt.xlabel('House Type')
        plt.ylabel('Price')
        plt.show()

# Additional visualizations can be added similarly...
