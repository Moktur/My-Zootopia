import json

def load_data(file_path):
  """Loads a JSON file"""
  with open(file_path, "r") as handle:
    return json.load(handle)


def iterate_through_animals(animals_json_load):
  a_info_to_print = ""
  for animal in animals_json_load:
    a_name = animal.get("name")
    a_diet = animal.get("characteristics", {}).get("diet")
    a_locations = animal.get("locations", [])
    a_location = a_locations[0] if a_locations else None
    a_type = animal.get("characteristics", {}).get("type")
    if a_name and a_diet and a_location and a_type:
      print("Name: " + a_name)
      print("Diet: " + a_diet)
      print("Location: " + a_location)
      print("Type: " + a_type + "\n")


def main():

  animals_data = load_data('animals_data.json')  
  # print(animals_data)
  iterate_through_animals(animals_data)


if __name__ == '__main__':
  main()