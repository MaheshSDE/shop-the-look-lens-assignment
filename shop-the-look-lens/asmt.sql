/*Write the name of tables and their columns that need to be created in the
 DB to store following relationship(DO NOT draw ER diagrams, Only basic 
 columns and relationship need to be shown) There are many hotels,
 each hotel can have multiple menus, each menu can have multiple food items, 
 food items can belong to multiple menus. */

/* creating hotel table*/ 
CREATE TABLE hotel(
    hotel_id INTEGER NOT NULL PRIMARY KEY,
    hotel_name VARCHAR(250),
    rating INTEGER,
    customer_satisfaction VARCHAR(250)
);

/*creating menu_card table*/
CREATE TABLE menu_card(
    menu_id INTEGER NOT NULL PRIMARY KEY,
    menu_name VARCHAR(250),
    food_items VARCHAR(250),
    hotel_id INTEGER.
    FOREIGN KEY(hotel_id) REFERENCES hotel(hote_id) ON DELETE CASCADE
);

/*creating food_items table*/
 CREATE TABLE food_items(
    id INTEGER NOT NULL PRIMARY KEY,
    food_item_name VARCHAR(250),
    food_item_rating INTEGER,
    price INTEGER
 );


/*creating menu_food_item table because menu_card and foodItems tables has many-to-many relationship*/

CREATE TABLE menu_food_item(
  menu_food_id INTEGER NOT NULL PRIMARY KEY,
  id INTEGER,
  menu_id INTEGER,
  quantity INTEGER,
  FOREIGN KEY(id) REFERENCES food_items(id) ON DELETE CASCADE,
  FOREIGN KEY(menu_id) REFERENCES menu_card(menu_id) ON DELETE CASCADE
);