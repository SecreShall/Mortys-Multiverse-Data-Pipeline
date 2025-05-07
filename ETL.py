import requests
import pandas as pd
from dotenv import load_dotenv
import os
import mysql.connector

def extract():
    # Extract all location data
    print(f"Extracting Location Data")
    df_location = pd.DataFrame(columns=['location_id', 'name', 'type', 'dimension', 'residents'])
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
                            'location_id': location['id'],
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
    df_character = pd.DataFrame(columns=['character_id', 'name', 'status', 'species', 'type', 'gender', 'origin', 'location', 'episode_count'])

    for index in range(1, 827):

        url = f"https://rickandmortyapi.com/api/character/?page={index}"
        raw_data = requests.get(url)
        data = raw_data.json()

        if 'results' in data:
            for character in data['results']:
                df_character = pd.concat(
                    [
                        df_character, pd.DataFrame([{
                        'character_id': character['id'],
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
    df_location = pd.read_csv('Data/extracted_location_data.csv', index_col=0)

    # Fill null values of columns 
    df_location['type'] = df_location['type'].fillna('unknown')
    df_location['dimension'] = df_location['dimension'].fillna('unknown')

    # Character ---------------------------------------------------
    # Read character data
    df_character = pd.read_csv('Data/extracted_character_data.csv', index_col=0)

    # Fill null values of columns
    df_character['type'] = df_character['type'].fillna('unknown')
    df_character['origin'] = df_character['origin'].str.split('/').str[5].fillna(0).astype(int)
    df_character['location'] = df_character['location'].str.split('/').str[5].fillna(0).astype(int)

    # remove duplicates of character data
    df_character = df_character.drop_duplicates(subset=['name','status','species','type','gender', 'origin', 'location','episode_count'], keep='first')

    # Reset the id to remove unique id gap
    df_character = df_character.reset_index(drop=True) 
    df_character['character_id'] = range(1, len(df_character) + 1)

    # Output cleaned data as csv
    df_location.to_csv('Data/transformed_location_data.csv')
    df_character.to_csv('Data/transformed_character_data.csv')

def load():

    load_dotenv
    db_pass = os.getenv('db_pass')
    
    db_connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            database = "rick_morty",
            password = db_pass,
        )

    cursor = db_connection.cursor()
   
    # Insert location data into database
    try:
        location = pd.read_csv('Data/transformed_location_data.csv')

        # Add a lcoation for unknown
        cursor.execute("INSERT INTO locations (location_id, name, type, dimension, residents) VALUES (0, 'unknown', 'unknown', 'unknown', 0)")
        db_connection.commit()

        insert_query = "INSERT INTO locations (location_id, name, type, dimension, residents) VALUES (%s, %s, %s, %s, %s)"

        values = [tuple(row[1:]) for row in location.itertuples(index=False, name=None)]


        cursor.executemany(insert_query, values)
        db_connection.commit()

    except mysql.connector.Error as e:
        print(f"Error occured in locations insertion: {e}")

   
    # Insert character data into database
    try:
        character = pd.read_csv('Data/transformed_character_data.csv')

        insert_query = "INSERT INTO characters (character_id, name, status, species, type, gender, origin_id, location_id, episode_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        values = [tuple(row[1:]) for row in character.itertuples(index=False, name=None)]

        cursor.executemany(insert_query, values)
        db_connection.commit()

    except mysql.connector.Error as e:
        print(f"Error occurred in character insertion: {e}")
       
    # Close the connection
    cursor.close()
    db_connection.close()

def main():
    extract()
    transform()
    load()

if __name__ == "__main__":
    main()