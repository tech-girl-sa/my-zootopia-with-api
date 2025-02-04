from data_fetcher import get_animals


def serialize_animal(animal_obj):
    """generates one card to display animal info"""
    to_display = {
        "Name": animal_obj.get("name"),
        "Diet": animal_obj['characteristics'].get('diet'),
        "Location": animal_obj.get("locations")[0],
        "Type": animal_obj['characteristics'].get('type'),
        "Skin Type": animal_obj['characteristics'].get('skin_type'),
    }
    animal_card = '<li class="cards__item">'
    for key, value in to_display.items():
        if key == "Name":
            animal_card += f'''
            <div class="card__title">{value}</div>
                <p class="card__text">
                    <ul class="animal_info">
'''
        elif value:
            animal_card += f"""
                            <li>
                                <strong>{key}</strong>: {value}
                            </li>
"""
    animal_card += '''
                    </ul>
                </p>
            </li>
            '''
    return animal_card

def serialize_animals(data):
    """generates list of animal cards in webpage"""
    animals =""
    for animal in data:
        animal_card = serialize_animal(animal)
        animals += animal_card
    return animals

def load_template(html_path):
    """loads the template to use in generating the webpage"""
    with open(html_path, "r", encoding="utf-8") as handle:
        return handle.read()

def regenerate_html(html_path, data, animal):
    """generates the whole animals webpage"""
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