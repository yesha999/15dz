import sqlite3

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<animal_id>')
def get_animal_by_id(animal_id):
    with sqlite3.connect("animal.db") as connection:
        cursor = connection.cursor()

    view_query = """
        SELECT 
            animals_main.id as main_id,
            animals_by_id.animal_id,
            animal_types.animal_type,
            animals_by_id.name,
            animal_breeds.animal_breed,
            animal_color1.color,
            animal_color2.color,
            animals_by_id.date_of_birth

        FROM animals_main
        LEFT JOIN animals_by_id
        ON animals_by_id.id = main_id
        LEFT JOIN animal_types
        ON animal_types.id = animals_by_id.animal_type_id
        LEFT JOIN animal_breeds
        ON animal_breeds.id = animals_by_id.breed_id
        LEFT JOIN colors as animal_color1
        ON animal_color1.id = animals_by_id.color_1_id
        LEFT JOIN colors as animal_color2
        ON animal_color2.id = animals_by_id.color_2_id
        
        WHERE animals_main.id = ?;
    """


    cursor.execute(view_query, (animal_id,))
    row = cursor.fetchone()

    cursor.close()

    return render_template('animal_id.html', row=row)


@app.route('/<animal_id>/outcome')
def get_animal_by_id_w_outcome(animal_id):
    with sqlite3.connect("animal.db") as connection:
        cursor = connection.cursor()

    view_query_w_outcome = """
        SELECT 
            animals_main.id as main_id,
            animals_by_id.animal_id,
            animal_types.animal_type,
            animals_by_id.name,
            animal_breeds.animal_breed,
            animal_color1.color,
            animal_color2.color,
            animals_by_id.date_of_birth,
            outcome_subtypes.subtype,
            outcome_types.type,
            outcome_by_id.outcome_month,
            outcome_by_id.outcome_year

        FROM animals_main, outcome_by_id
        LEFT JOIN animals_by_id
        ON animals_by_id.id = main_id
        LEFT JOIN animal_types
        ON animal_types.id = animals_by_id.animal_type_id
        LEFT JOIN animal_breeds
        ON animal_breeds.id = animals_by_id.breed_id
        LEFT JOIN colors as animal_color1
        ON animal_color1.id = animals_by_id.color_1_id
        LEFT JOIN colors as animal_color2
        ON animal_color2.id = animals_by_id.color_2_id
        LEFT JOIN outcome_subtypes
        ON outcome_subtypes.id = outcome_by_id.outcome_subtype_id
        LEFT JOIN outcome_types
        ON outcome_types.id = outcome_by_id.outcome_type_id


        WHERE animals_main.id = ?;
    """

    cursor.execute(view_query_w_outcome, (animal_id,))
    row = cursor.fetchone()

    cursor.close()

    return render_template('animal_id_w_outcome.html', row=row)



if __name__ == '__main__':
    app.run(debug=True)
#
# #


# animal_breeds.animal_breed,
# animal_color1.color as 'color1',
# animal_color2.color as 'color2',
# animals_by_id.date_of_birth
