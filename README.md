[![Build Status](https://travis-ci.com/rasifrana/ecommerce.svg?branch=master)](https://travis-ci.com/rasifrana/ecommerce)

# Health Store. (Online Shop)






![](http://imgur.com/t3teAxi.png)
### :handbag: A simple store for Purchases and Products

 [![GitHub release](https://img.shields.io/github/release/ovflowd/ecommerce.svg)]() 

## Deploy

<a href="http://health-ecommerce.herokuapp.com/"><img src="https://dailysmarty-production.s3.amazonaws.com/uploads/post/img/509/feature_thumb_heroku-logo.jpg" width="60" height="60"></a> 


## Features

<b>Products Features</b>

| Feature  |  Added    | Description  |
|----------|:-------------:|:-------------|
| Add a Product | &#10004; | Ability of Add a Product on the System |
| List Products | &#10004; | Ability of List Products |
| Search a Product | &#10004; | Ability to Filter Products |

<b>Purchase Features</b>

| Feature  |  Added       | Description  |
|----------|:-------------:|:-------------|
| See Cart | &#10004; | Ability to see the Cart and it items |
| Edit a Cart | &#10004; | Ability of Edit Quantity |
| Add Item | &#10004; | Ability of add a new Item on the Cart |
| Remove a Item | &#10004; | Ability of Remove a Item from the Cart |
| Checkout | &#10004; | Ability to Checkout |

# Health eCommerce

**This eCommerce** project is built using Django. The Django project has 7 applications: 

1) media - this app stores and retrieves static files (css,js and media/images) from Amazon AWS. 
2) accounts - this app contains the reference to all the users's information on their accounts and credentials that are used to create, modify and use login and signup information. 
3) products -this app contains and stores all the references to products (id,category,price,quantity) in the 'products' database of the website. 
4) cart - this app contains and stores all the information that connects the products to the cart and to finally the (last) app 'checkout' using Sessions. 
5) checkout - this app contains and stores all the information that related to products, accounts and carts so that products can be ordered and purchased using Stripe's API.
6) home - Main Landing page and to showcase some products
7) search - This app is used to filter products on a page


Project is connected to a PostgresSQL database that can be modified locally or through cloud. Project also takes staticfiles that are served from an online AWS Amazon Bucket. Project implements the STRIPE api configurations that allow purchases to be made for the products stored in the APPs.

The project ignores any senstive commits to github and preserves private keys. Requirements.txt file allow for a quick installation of the requirements for the projects using 'pip -r install requirements.txt'

## Requirements

boto3==1.12.32
botocore==1.15.32
dj-database-url==0.5.0
Django==1.11.24
django-forms-bootstrap==3.1.0
django-storages==1.9.1
docutils==0.15.2
gunicorn==20.0.4
jmespath==0.9.5
olefile==0.46
Pillow==4.3.0
psycopg2==2.8.4
pytz==2019.3
s3transfer==0.3.3
stripe==2.44.0


## Installation

Project can be run locally by cloning/downloading this repository and by cd'ing into the main project directory (where manage.py is contained) that is the main directory for project.From there project can be run locally by using the command python manage.py runserver on the terminal.



## Wireframes

Wireframe for this projects (links are below).

- Landing wireframe: https://github.com/rasifrana/ecommerce/blob/master/wireframes/ecommerce%20landing%20page.pdf

- Checkout wireframe: https://github.com/rasifrana/ecommerce/blob/master/wireframes/ecommerce%20landing%20page.pdf


## Features

- Easy to navigate and user friendly UI 
- All information stored on cloud
- Payment method with Stripe

## Future Developments

 This application can be improved in many ways. Different catagories can be added for products. All links can be provided in the footer.

### Visual representation of portfolio

This project is very simple to use and divided in sections to add assets

- **Landing Page** is Landing Page with easy navigation and main header showcasing the products

- **Products Page** Beautiful cards displayed with multiple types of products

- **Cart Page** All selected items stored in cart

- **Checkout Page** Checkout with payment details



**Forms** Forms are created using django built-in Forms

## Technologies Used

- HTML5

  - Basic html structure / markup.

- CSS3

  - CSS3 for custom styling

- Bootstrap

  - Most of the interface is craeted using bootstrap 

- Google fonts
  - to make website beautifully, Montserrat font-family was used referencing https://fonts.google.com/ CDN

- Font Awsome
  - All icons are refferenced to Font Awsome CDN

- dJango framework
 - For backend

- PostgresSQL 
 - Database

## Testing

 Travis CI for build added

## Responsive

This project is completely responsive with different layout on small and mobile devices. This was done using media queries.

## Deployment

Project is connected to heroku.git (from which it is automatically deployed). This repo is a new copy of the existing heroku.git repo (https://git.heroku.com/health-commerce.git)

Project was also pushed to remote repository on https://github.com/rasifrana/ecommerce on master branch.

## Heroku

Project is deployed at https://health-ecommerce.herokuapp.com/



### Media

- The photo used in this site were obtained from https://unsplash.com

### Acknowledgements

- I received inspiration for this project from code institute team