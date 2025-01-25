import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

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

def regenerate_html(html_path, data):
    content = load_template(html_path)
    animals_display = serialize_animals(data)
    new_content = content.replace("__REPLACE_ANIMALS_INFO__", animals_display)
    with open(html_path,"w") as handle:
        handle.write(new_content)

if __name__ == "__main__":
    data = load_data('animals_data.json')
    html_path = "animals_template.html"
    regenerate_html(html_path, data)