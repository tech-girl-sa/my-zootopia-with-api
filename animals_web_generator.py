from data_fetcher import get_animals


def serialize_animal(animal_obj):
    to_display = {
        "Name": animal_obj.get("name"),
        "Diet": animal_obj['characteristics'].get('diet'),
        "Location": animal_obj.get("locations")[0],
        "Type": animal_obj['characteristics'].get('type'),
        "Skin Type": animal_obj['characteristics'].get('skin_type'),
    }
    animal_card = '<li class="cards__item">\n'
    for key, value in to_display.items():
        if key == "Name":
            animal_card += f'<div class="card__title">{value}</div>\n <p class="card__text">\n<ul class="animal_info">'
        elif value:
            animal_card += f"<li><strong>{key}</strong>: {value}</li>\n"
    animal_card += '</ul>\n</p>\n</li>\n'
    return animal_card

def serialize_animals(data):
    animals =""
    for animal in data:
        animal_card = serialize_animal(animal)
        animals += animal_card
    return animals

def load_template(html_path):
    with open(html_path, "r") as handle:
        return handle.read()

def regenerate_html(html_path, data, animal):
    content = load_template("animals_blue_print.html")
    if data:
        animals_display = serialize_animals(data)
    else:
        animals_display = (f'<li class="cards__item"> <h2>The animal {animal} doesn\'t exist. <h2><li>')
    new_content = content.replace("__REPLACE_ANIMALS_INFO__", animals_display)
    with open(html_path,"w") as handle:
        handle.write(new_content)

if __name__ == "__main__":
    animal = input("Enter a name of an animal: ")
    data = get_animals(animal)
    html_path = "animals_template.html"
    regenerate_html(html_path, data, animal)
    print("Website was successfully generated to the file animals_template.html")