import matplotlib.pyplot as plt
import seaborn as sns

def bar_chart(data, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    data.plot(kind='bar', color='skyblue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def heatmap(data, title):
    plt.figure(figsize=(10, 6))
    sns.heatmap(data, annot=True, cmap="coolwarm", fmt=".1f")
    plt.title(title)
    plt.tight_layout()
    plt.show()