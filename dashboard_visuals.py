# Sample data visualization for food tracking
import matplotlib.pyplot as plt

def plot_nutrition_data():
    categories = ['Carbs', 'Protein', 'Vitamins']
    values = [60, 25, 15]

    plt.bar(categories, values, color=['orange', 'green', 'blue'])
    plt.title('Average Daily Intake')
    plt.ylabel('Percentage (%)')
    plt.show()

if __name__ == "__main__":
    plot_nutrition_data()
