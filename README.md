# Cake SHOP!
#### Contributors: Chen Jiang, Sarah Baughman

## Description
Utilizing a Flask API backend with a React frontend, Cake SHOP! is a business app intended to give users access to the many offerings of a cake shop, as well as provide an easy way for the business to take in orders. 

## User Story
A user interacting the site may do the following:
 -  Visit the Home and About page to learn more about the Cake SHOP business
 - Move through various pages with just a click using a navigation bar
 - View the cake offerings and cake information, includes a "Read More" button to expand and reveal more text
 - Click "Reviews" button to view reviews specific to each cake
 - Create, login and logout of a user account in order to store user information
 - Click "Add to Cart" button to add cakes to cart with login/logout and refresh page persistance
 - Adjust quantity of each cake in the Cart and submit an order
 - Click "Add to Favorites" button to add cakes to a Favorites page with login/logout and refresh page persistance
 - View MyPage to view past orders and write, view and delete reviews for purchased cakes 


# Code Files
Fork and clone:
 - Frontend - https://github.com/LuluLalaJ/cake_shop_frontend
 - Backend - https://github.com/LuluLalaJ/cake_shop_backend 

# Setup
Be sure to run both the backend and frontend for the full app experience.

## Frontend Setup
To download dependencies and get started, in the project directory run: 

```console
$ npm install
$ npm start
```
The React app will run in a separate window on [http://localhost:4000]

## Backend Setup
To download dependencies and get started, in the project directory run: 

```console
$ pipenv install
$ pipenv shell
```

You can run the Flask API on [http://127.0.0.1:5555] in the project directory by running: 

```console
$ python app.py
```



## Frontend Information
#### Project Requirements
- Use forms and validation through Formik on all input
- At least one datatype validation
- At least one string/number format validation
- Have at least three different client-side routes using React Router
- Include navigation bar or other UI element allowing users to navigate between routes
- Connect the client and server using fetch()

#### Component Heirarchy
- App
    - About
    - Cakes
        - CakeCard
    - ShoppingCart
    - CheckOut
    - Favorites
        - FavoriteCard
    - Login
    - Home
    - Signup
    - MyPage
        - PastOrderCard
            - PastCakeCard
                - ReviewForm
        - MyPagePreviewCard
    - Error
    - Nav
    - Review
        - ReviewCard
    - Signup

## Backend Information
#### Project Requirements
- Have at least three models on the backend
- Include at least two one-to-many relationships
- Include at least one reciprocal many-to-many  relationship
- Full CRUD actions for at least one resource
- Minimum of create and read actions for each resource

#### Models
![](2023-06-08-18-57-21.png/)


