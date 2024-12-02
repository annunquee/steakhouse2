GRANT ALL PRIVILEGES ON DATABASE steakhouse_kyzx TO steakhouse_kyzx_user;


CREATE SEQUENCE category_seq;
CREATE SEQUENCE recipe_seq;

CREATE TABLE category (
    id INT PRIMARY KEY DEFAULT nextval('category_seq'),
    name VARCHAR(50) NOT NULL,
    image VARCHAR(100)
);

CREATE TABLE recipe (
    id INT PRIMARY KEY DEFAULT nextval('recipe_seq'),
    title VARCHAR(100) NOT NULL,
    description TEXT,
	ingredients TEXT,
    category_id INT,        
    image VARCHAR(100),
    FOREIGN KEY (category_id) REFERENCES category(id)
);

INSERT INTO category (name, image) VALUES 
('Vegetarian', 'vegetarian.jpg'),
('Desserts', 'desserts.jpg'),
('Main Courses', 'main_courses.jpg'),
('Snacks', 'snacks.jpg'),
('breakfast', 'breakfast.jpg');
