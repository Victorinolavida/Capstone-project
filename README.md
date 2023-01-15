# Capstone-project

Capstone project from Meta backend developer

## urls available

- **GET:** `restaurant/menu`: return all menu items

- `restaurant/menu/<int:pk>`

  - GET: return item by id
  - PUT: update a item by id
  - DELETE: delete the item with that id

- **GET:** `restaurant/booking/tables/`:return booking items (you must be have a token)

- **POST:** `auth/users/`: create new user

- **POST:**`auth/token/login`: generate a token for a user
