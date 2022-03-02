import sqlite3

# В первом варианте сделал новую базу данных как в условиях ДЗ,
# но в разборе ДЗ этим условием пренебрегли и решение
# в таком варианте стало чрезмерно сложным в условиях недостатка знаний.
with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()

create_animals_type_query = ("""CREATE TABLE animal_types
  (id INTEGER PRIMARY KEY AUTOINCREMENT,
  animal_type VARCHAR (100) NOT NULL
  )
  """)

cursor.execute(create_animals_type_query)

create_breed_type_query = ("""CREATE TABLE animal_breeds
  (id INTEGER PRIMARY KEY AUTOINCREMENT,
  animal_breed VARCHAR (100) NOT NULL
  )
  """)

cursor.execute(create_breed_type_query)

create_color_query = ("""CREATE TABLE colors
  (id INTEGER PRIMARY KEY AUTOINCREMENT,
  color VARCHAR (100) NOT NULL
  )
  """)

cursor.execute(create_color_query)

create_outcome_subtype_query = ("""CREATE TABLE outcome_subtypes
  (id INTEGER PRIMARY KEY AUTOINCREMENT,
  subtype VARCHAR (100) NOT NULL
  )
  """)

cursor.execute(create_outcome_subtype_query)

create_outcome_type_query = ("""CREATE TABLE outcome_types
  (id INTEGER PRIMARY KEY AUTOINCREMENT,
  type VARCHAR (100) NOT NULL
  )
  """)

cursor.execute(create_outcome_type_query)

create_animals_table_query = ("""CREATE TABLE animals_by_id
  (id INTEGER PRIMARY KEY AUTOINCREMENT,
  animal_id VARCHAR (10) NOT NULL,
  animal_type_id INTEGER,
  name VARCHAR (255),
  breed_id INTEGER,
  color_1_id INTEGER,
  color_2_id INTEGER,
  date_of_birth DATE, 


  FOREIGN KEY (animal_type_id) REFERENCES animal_types(id) ON DELETE CASCADE,
  FOREIGN KEY (breed_id) REFERENCES animal_breeds(id) ON DELETE CASCADE,
  FOREIGN KEY (color_1_id) REFERENCES colors(id) ON DELETE CASCADE,
  FOREIGN KEY (color_2_id) REFERENCES colors(id) ON DELETE CASCADE
  )
  """)

cursor.execute(create_animals_table_query)

create_outcome_table_query = ("""CREATE TABLE outcome_by_id
  (outcome_id INTEGER PRIMARY KEY AUTOINCREMENT,
  outcome_subtype_id INTEGER,
  outcome_type_id INTEGER ,
  outcome_month INTEGER, 
  outcome_year INTEGER,

  FOREIGN KEY (outcome_subtype_id) REFERENCES outcome_subtypes(id) ON DELETE CASCADE,
  FOREIGN KEY (outcome_type_id) REFERENCES outcome_types(id) ON DELETE CASCADE
  )
  """)

cursor.execute(create_outcome_table_query)

create_main_table_query = ("""CREATE TABLE animals_main
  (id INTEGER PRIMARY KEY AUTOINCREMENT,
  animal_main_id INTEGER NOT NULL, 
  outcome_main_id INTEGER NOT NULL,

  FOREIGN KEY (animal_main_id) REFERENCES animals_by_id(id) ON DELETE CASCADE,
  FOREIGN KEY (outcome_main_id) REFERENCES outcome_by_id(outcome_id) ON DELETE CASCADE 
  )
  """)

cursor.execute(create_main_table_query)


cursor.close()