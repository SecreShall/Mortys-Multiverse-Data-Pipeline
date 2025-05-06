import requests
import pandas as pd

def exctract():
    # Extract all location data
    print(f"Extracting Location Data")
    df_location = pd.DataFrame(columns=['id', 'name', 'dimension', 'residents'])
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
    df_location.to_csv("Data/extracted_location_data.csv")
    print(f"Saved Location Data to CSV")

    # Extract all character data
    print(f"Extracting Character Data")
    df_character = pd.DataFrame(columns=['id', 'name', 'status', 'species', 'type', 'gender', 'origin', 'location', 'episode_count'])

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
                        'episode_count': len(character['episode']),
                        }])
                    ], 
                    ignore_index=True
                )
            print(f"Character ID {index} added to data frame")
    # Save character data to csv
    df_character.to_csv("Data/extracted_character_data.csv")
    print(f"Saved Character Data to CSV")

def transform():
    # Location -----------------------------------------------------
    # Read location data
    df_location = pd.read_csv('Data/extracted_location_data.csv')

    # Fill null values of columns 
    df_location['type'] = df_location['type'].fillna('unknown')
    df_location['dimension'] = df_location['dimension'].fillna('unknown')

    # Character ---------------------------------------------------
    # Read character data
    df_character = pd.read_csv('Data/extracted_character_data.csv')

    # Fill null values of columns
    df_character['type'] = df_character['type'].fillna('unknown')
    df_character['origin'] = df_character['origin'].str.split('/').str[5].fillna(0).astype(int)
    df_character['location'] = df_character['location'].str.split('/').str[5].fillna(0).astype(int)

    # remove duplicates of character data
    clean_character = df_character.drop_duplicates(subset=['name','status','species','type','gender', 'origin', 'location','episode_count'], keep='first')

    # Reset the id to remove unique id gap
    clean_character = clean_character.reset_index(drop=True) 
    clean_character['id'] = range(1, len(clean_character) + 1)

    # Output cleaned data as csv
    df_location.to_csv('Data/transformed_location_data.csv')
    clean_character.to_csv('Data/transformed_character_data.csv')

def load():
    pass

def main():
    exctract()
    transform()
    load()

if __name__ == "__main__":
    main()