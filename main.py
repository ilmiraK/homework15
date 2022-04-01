import sqlite3

with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()

    query = """

    
    CREATE TABLE if not exists animal_type
(
    id integer PRIMARY KEY AUTOINCREMENT,
    animal_type varchar(50)

);
        CREATE TABLE if not exists  breed (
                id integer PRIMARY KEY AUTOINCREMENT, 
                breed varchar(50) 

);


        CREATE TABLE if not exists  outcome_type (
                id integer PRIMARY KEY AUTOINCREMENT, 
                outcome_type varchar(50) 

);

        CREATE TABLE if not exists  outcome_subtype (
                id integer PRIMARY KEY AUTOINCREMENT, 
                outcome_subtype varchar(50) 

);

        CREATE TABLE if not exists  outcome_month (
                id integer PRIMARY KEY AUTOINCREMENT, 
                outcome_month integer 

);

        CREATE TABLE if not exists  outcome_year (
                id integer PRIMARY KEY AUTOINCREMENT, 
                outcome_year integer 

);

          CREATE TABLE if not exists  color (
                  id integer PRIMARY KEY AUTOINCREMENT, 
                  color varchar(50) 

);
CREATE TABLE if not exists  animal (
                index_animal integer PRIMARY KEY AUTOINCREMENT, 
                animal_id integer,
                age_upon_outcome varchar(50),   
                date_of_birth date,
                animal_type_id integer,
                breed_id integer,
                outcome_type_id integer,
                outcome_subtype_id integer,
                outcome_month_id integer,
                outcome_year_id integer,
                FOREIGN KEY (animal_type_id) REFERENCES animal_type(id),
                FOREIGN KEY (breed_id) REFERENCES breed(id), 
                FOREIGN KEY (outcome_type_id) REFERENCES outcome_type(id),              
                FOREIGN KEY (outcome_subtype_id) REFERENCES outcome_subtype(id),                
                FOREIGN KEY (outcome_month_id) REFERENCES outcome_month(id),                
                FOREIGN KEY (outcome_year_id) REFERENCES outcome_year(id)
);

CREATE TABLE if not exists  animal_color (
                id integer PRIMARY KEY AUTOINCREMENT,    
                animal_id integer,
                color_id varchar(50),
                FOREIGN KEY (animal_id) REFERENCES animals(animal_id), 
                FOREIGN KEY (color_id) REFERENCES color(id)

);

        
    """

    cursor.executescript(query)
    cursor.fetchall()
    connection.commit()

with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()
    query = """
    INSERT INTO animal_type(animal_type)
    SELECT distinct (animal_type) FROM main.animals
    

  """
    cursor.executescript(query)
    cursor.fetchall()
    connection.commit()

with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()
    query = """
    INSERT INTO breed(breed)
    SELECT distinct (breed) FROM main.animals


  """
    cursor.executescript(query)
    cursor.fetchall()
    connection.commit()

with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()
    query = """
    INSERT INTO outcome_type(outcome_type)
    SELECT distinct (outcome_type) FROM main.animals



    
  """
    cursor.executescript(query)
    cursor.fetchall()
    connection.commit()

with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()
    query = """
    INSERT INTO outcome_subtype(outcome_subtype)
    SELECT distinct (outcome_subtype) FROM main.animals




  """
    cursor.executescript(query)
    cursor.fetchall()
    connection.commit()

with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()
    query = """
    INSERT INTO outcome_month(outcome_month)
    SELECT distinct (outcome_month) FROM main.animals




  """
    cursor.executescript(query)
    cursor.fetchall()
    connection.commit()

with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()
    query = """
    INSERT INTO outcome_year(outcome_year)
    SELECT distinct (outcome_year) FROM main.animals




  """
    cursor.executescript(query)
    cursor.fetchall()
    connection.commit()

with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()
    query = """
insert into color(color)
select color
from (
         select DISTINCT(rtrim(color1)) as color
         from animals
         union
         select DISTINCT(rtrim(color2)) as color
         from animals)
where color is not null
;


  """
    cursor.executescript(query)
    cursor.fetchall()
    connection.commit()

with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()
    query = """
    INSERT INTO animal(    
                animal_id,           
                age_upon_outcome,   
                date_of_birth,
                animal_type_id,
                breed_id,
                outcome_type_id,
                outcome_subtype_id,
                outcome_month_id,
                outcome_year_id)
                
    select
    a.animal_id,
    a.age_upon_outcome,
    a.date_of_birth,
    at.id,
    b.id,
    a.outcome_type,
    a.outcome_subtype,
    a.outcome_month,
    a.outcome_year
    from main.animals as a
    left join main.breed b on a.breed = b.breed 
    left join main.animal_type at on a.animal_type = at.animal_type;
    
    
    """
    cursor.executescript(query)
    cursor.fetchall()
    connection.commit()

with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()
    query = """
    INSERT INTO animal_color(
                animal_id,           
                color_id  
               )

    select 
    a.animal_id,
    b.id
    from main.animals as a
    left join main.color b on a.color1 = b.color;
    


    """
    cursor.executescript(query)
    cursor.fetchall()
    connection.commit()

with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()
    query = """
       INSERT INTO animal_color(
                   animal_id,           
                   color_id  
                  )

       select 
       a.animal_id,
       b.id
       from main.animals as a
       left join main.color b on rtrim(a.color2) = b.color ;



       """
    cursor.executescript(query)
    cursor.fetchall()
    connection.commit()
