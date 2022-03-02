INSERT INTO animal_types (animal_type)
SELECT DISTINCT animal_type
FROM animals;

INSERT INTO animal_breeds (animal_breed)
SELECT DISTINCT breed
FROM animals;

INSERT INTO colors (color)
SELECT DISTINCT TRIM(color1) as color
FROM animals
UNION
SELECT DISTINCT TRIM(color2) as color
FROM animals
WHERE color2 IS NOT NULL;


INSERT INTO outcome_subtypes (subtype)
SELECT DISTINCT outcome_subtype
FROM animals
WHERE outcome_subtype IS NOT NULL;



INSERT INTO outcome_types (type)
SELECT DISTINCT outcome_type
FROM animals
WHERE outcome_type IS NOT NULL;


INSERT INTO animals_by_id (animal_id,
                           animal_type_id,
                           name,
                           breed_id,
                           color_1_id,
                           color_2_id,
                           date_of_birth)

SELECT animal_id,
       animal_types.id  as animal_type_id,
       name,
       animal_breeds.id as breed_id,
       animal_color1.id as color1_id,
       animal_color2.id as color2_id,
       date_of_birth
FROM animals
         LEFT JOIN animal_types
                   ON animal_types.animal_type = animals.animal_type
         LEFT JOIN animal_breeds
                   ON animal_breeds.animal_breed = animals.breed
         LEFT JOIN colors as animal_color1
                   ON animal_color1.color = animals.color1
         LEFT JOIN colors as animal_color2
                   ON animal_color2.color = animals.color2;


INSERT INTO outcome_by_id (outcome_subtype_id,
                           outcome_type_id,
                           outcome_month,
                           outcome_year)

SELECT outcome_subtypes.id as outcome_subtype_id,
       outcome_types.id    as outcome_type_id,
       outcome_month,
       outcome_year
FROM animals
         LEFT JOIN outcome_subtypes
                   ON outcome_subtypes.subtype = animals.outcome_subtype
         LEFT JOIN outcome_types
                   ON outcome_types.type = animals.outcome_type;

INSERT INTO animals_main (animal_main_id, outcome_main_id)

SELECT animals_by_id.id  as animal_main_id,
       outcome_by_id.outcome_id as outcome_main_id
FROM animals_by_id

LEFT JOIN outcome_by_id ON animals_by_id.id = outcome_by_id.outcome_id;