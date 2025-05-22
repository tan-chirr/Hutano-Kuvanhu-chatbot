# Simple chatbot response based on age-specific nutrition guidance

def get_nutrition_advice(age, food_item):
    responses = {
        "maize": "Maize porridge is good for toddlers but should be enriched with protein sources.",
        "beans": "Beans are an excellent source of protein and iron."
    }
    return responses.get(food_item.lower(), "Food not recognized. Please consult local nutrition guide.")

if __name__ == "__main__":
    print(get_nutrition_advice(2, "maize"))
