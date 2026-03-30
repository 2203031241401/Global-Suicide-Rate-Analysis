import matplotlib.pyplot as plt

def plot_top_countries(data):
    data.head(10).plot(kind='bar')
    plt.title("Top 10 Countries by Suicide Count")
    plt.show()