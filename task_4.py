import json


# search in the recipes source by the preferences of the user, and create a recipe book
# call the function statistics in the end
def search():
    request = input()
    keywords = []
    fav_foods = []
    allergens = []
    request = request.split(" ")
    flag = 0
    for word in request:
        if '+' in word:
            fav_foods.append(word[1:])
            flag = 1
        elif '-' in word:
            allergens.append(word[1:])
            flag = 2
        else:
            if flag == 1:
                fav_foods[-1:] = [str(fav_foods[-1]) + ' ' + word]
            elif flag == 2:
                allergens[-1:] = [str(allergens[-1]) + ' ' + word]
            else:
                keywords.append(word)
    with open("small_database.txt", "r") as f:
        read_json(f)
        for obj in read_json(f):
            if related(keywords, str(obj)) or not keywords:
                if related(fav_foods, obj["ingredients"]) or not fav_foods:
                    if not related(allergens, obj["ingredients"] or not allergens):
                        recipe_book.append(obj)
    statistics()


# generate json objects
def read_json(f):
    for line in f:
        yield json.loads(line)


# return true if one of the keys related to the string s otherwise false
def related(keys, s):
    for key in keys:
        if key in s:
            return True
    return False


# calculate statistics about the recipe_book
def statistics():
    stat = []
    for index, obj in enumerate(recipe_book):
        number_of_ingredients = 1
        for c in obj["ingredients"]:
            if "\n" in c:
                number_of_ingredients += 1
        number_of_instructions = (len(obj["description"].split(" ")))
        stat.append((index, number_of_ingredients, number_of_instructions))
    sum_ingredients = sum(map(lambda x: x[1], stat))
    sum_instructions_words = sum(map(lambda x: x[2], stat))
    min_of_ingredients = min(map(lambda x: x[1], stat))
    min_of_instructions = min(map(lambda x: x[2], stat))
    max_of_ingredients = max(map(lambda x: x[1], stat))
    max_of_instructions = max(map(lambda x: x[2], stat))
    count = len(stat)
    print("average of ingredients: ", sum_ingredients/count)
    print("average of instructions words: ", sum_instructions_words / count)
    print("number of recipes: ", count)
    print("sum of ingredients: ", sum_ingredients)
    print("sum of instructions words: ", sum_instructions_words)
    print("min number of ingredients: ", min_of_ingredients)
    print("min number of instructions words: ", min_of_instructions)
    print("max number of ingredients: ", max_of_ingredients)
    print("max number of instructions words: ", max_of_instructions)


if __name__ == "__main__":
    recipe_book = []
    user_re = input()
    if "search" in user_re:
        search()