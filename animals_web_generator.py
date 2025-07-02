import json

def load_data(file_path):
  """Loads a JSON file"""
  with open(file_path, "r") as handle:
    return json.load(handle)


def iterate_through_animals(animals_json_load):
  animal_info = ""
  for animal in animals_json_load:
    a_name = animal.get("name")
    a_diet = animal.get("characteristics", {}).get("diet")
    a_locations = animal.get("locations", [])
    a_location = a_locations[0] if a_locations else None
    a_type = animal.get("characteristics", {}).get("type")
    if a_name and a_diet and a_location and a_type:
      # append information to each string
      animal_info += '<li class="cards__item">'
      animal_info += (
          f"<div class=\"card__title\">Name: {a_name}</div>\n"
          f"<p class=\"card__text\">\n"
          f"<strong>Diet:</strong> {a_diet}<br/>\n"
          f"<strong>Location:</strong> {a_location}<br/>\n"
          f"<strong>Type:</strong> {a_type}</br>\n"
          f"</p>"
          f"</li>"
      )
      animal_info += '</li>'
  return animal_info
      

def main():

  animals_data = load_data('animals_data.json')  
  # print(animals_data)
  iterate_through_animals(animals_data)
  htmlfile = ""
  with open("animals_template.html", "r", encoding="utf-8") as at:
    template = at.read()
    htmlfile = template.replace(
      "__REPLACE_ANIMALS_INFO__",
      iterate_through_animals(animals_data)
      )
  with open("animals_template.html", "w", encoding="utf-8") as at:
    at.write(htmlfile)
    



if __name__ == '__main__':
  main()