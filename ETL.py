import requests
import pandas as pd



def exctract():

    # Extract all location data
    print(f"Extracting Location Data")
    df_location = pd.DataFrame()
    for index in range(1,127):

    
        url = f"https://rickandmortyapi.com/api/location/?page={index}"

        raw_data = requests.get(url)

        data = raw_data.json()

        if 'results' in data:
            for location in data['results']:

                df_location = pd.concat(
                    [
                        df_location,
                        pd.DataFrame([{
                            'id': location['id'],
                            'name': location['name'],
                            'type': location['type'],
                            'dimension': location['dimension'],
                            'residents': len(location['residents']),
                        }])
                    ],
                    ignore_index=True
                )
            print(f"Location ID {index} added to data frame")
    # Save location data to csv
    df_location.to_csv("extracted_location_data.csv")
    print(f"Saved Location Data to CSV")


    # Extract all character data
    print(f"Extracting Character Data")
    df_character = pd.DataFrame()

    for index in range(1, 827):

        url = f"https://rickandmortyapi.com/api/character/?page={index}"

        raw_data = requests.get(url)

        data = raw_data.json()

        if 'results' in data:
            for character in data['results']:
                df_character = pd.concat(
                    [
                        df_character, pd.DataFrame([{
                        'id': character['id'],
                        'name': character['name'],
                        'status': character['status'],
                        'species': character['species'],
                        'type': character['type'],
                        'gender': character['gender'],
                        'origin': character['origin']['url'],
                        'location': character['location']['url'],
                        'episode': len(character['episode']),
                        }])
                    ], 
                    ignore_index=True
                )
            print(f"Character ID {index} added to data frame")
    # Save character data to csv
    df_character.to_csv("extracted_character_data.csv")
    print(f"Saved Character Data to CSV")

    
    

exctract()