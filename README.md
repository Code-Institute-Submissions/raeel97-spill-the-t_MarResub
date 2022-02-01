# Spill The T
## **Code Institute - Portfolio Project 4: _FullStack Toolkit Portfolio Project** 
Spill The T is an django blog app inspired focusing on transgender and gender diverse news. 

This web app will allow users to explore the fond memories of their childhood and purchase the products they have always dreamed of!
## Demo

[View the Live Website Here](https://raeel97-spill-the-t.herokuapp.com/)

<img src="https://raeel97-spill-the-t.s3.eu-west-1.amazonaws.com/media/am-i-responsive.PNG">


## Table of contents
+ [User Experience](#User-Experience)
     + [Project Goals](#Project-Goals)
     + [User Stories](#User-Stories)
     + [Strategy](#Strategy)
     + [Scope](#Scope)
     + [Structure](#Structure)
          + [Front end Pages](Front-end-Pages)
     + [Skeleton](#Skeleton)
          + [Wireframes](#Wireframes)
     + [Surface](#Surface)
+ [Features](#Features) 
     + [Existing Features](#Existing-Features)
     + [Features to Implement in the future](#Features-to-Implement-in-the-future)
+ [Database](#Database)
+ [Testing](#Tests)
+ [Bugs](#Bugs)
+ [Technologies Used](#Technologies-Used)
     + [Resources](#Resources)
     + [Tools](#Tools)
+ [Deployment](#Deployment)
     + [Heroku Deployment](#Heroku-Deployment)
+ [Credits](#Credits)

***
# User Experience
## Project Goals
The primary goal of Spill The T is to enable users to peruse a number of transgender and gender diverse new stories in a handy blog format. The goal for the design was to make it as easy as possible to access information, while striving for a trans-friendly user experience!

## User Stories

- View post list: As a Site User I can view a list of posts so that I can select one to read
- Open a post: As a Site User I can click on a post so that I can read the full text
- View likes: As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral
- View comments: As a Site User / Admin I can view comments on an individual post so that I can read the conversation
- Account registration: As a Site User I can register an account so that I can comment and like
- Comment on a post: As a Site User I can leave comments on a post so that I can be involved in the conversation
- Like / Unlike: As a Site User I can like or unlike a post so that I can interact with the content
- Manage posts: As a Site Admin I can create, read, update and delete posts so that I can manage my blog content
- Create drafts: As a Site Admin I can create draft posts so that I can finish writing the content later
- Approve comments: As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments


[^ back to top ^](#Table-of-contents)
<br>

## Strategy
### — Project Planning —

Agile Development was used to plan the project. This was implemented using a kanban board in github issues and projects. 

<br>

[back to top](#Table-of-contents)
<br>


## Scope

To achieve user and owner’s goals, below are the minimum features to be included in this project. Also, **CRUD** Create, Read, Update, and Delete functions are required for this project so these are implemented as a part of the essential features.


- Simple homepage that explains the purpose of the website
- Register page 
- Logout Page
- Sign in and sign out page where users can sign into and out of their accounts.
- Login page  
- Contact form  
- 404 page that appears for invalid URL and takes users back to *Home* page of the website safely
- Ability to sign up for newsletter

[back to top](#Table-of-contents)
<br>
> 

## Structure

The entire web app has the same menu and footer. 

The menu has the following navigation links:
- Title leads to home page
- Home leads to home page
- Contact leads to contact page
- blog leads to blog view page
- Each blog post leads to blog page



The footer has the following navigation links:
- Basic newsletter sign up form powered by mailchimp
- Contact us button takes user to contact form
- Git hub icon and name takes user to developers github profile. 


The main pages of the website are:

- Homepage(index.html) - Which takes users to blog page through the view blog button
- Blog page(post_view.html) - Which renders all published posts in blog which leads to blog post page
- Blog post page(post_detail.html) - Which renders a view of a specific blog post. 
- Contact page(contact.html) - Which renders the contact form. 
<br>

[back to top](#Table-of-contents)
<br>


## Skeleton

### Wireframes

Home Page
<img src="">
<br>
Blog Page
<br>
<img src="">
<br>
Blog post Page
<br>
<img src="">
<br>
Contact Page
<br>
<img src="">
<br>
Future Feature Page
<br>
<img src="">
<br>
404 error Page
<br>
<img src="">
<br>
Register Page
<br>
<img src="">
<br>
Log in Page
<br>
<img src="">
<br>
Log out Page
<br>
<img src="">


## Surface

— **Colour** —

The colors for the blog were taken from the transgender flag whilst keeping accesibility and contrast rules in mind. 
<br>
_Color Palette_
<br>
<br>
<img src="https://raeel97-spill-the-t.s3.eu-west-1.amazonaws.com/media/color-palette.PNG">
<br>
[back to top](#Table-of-contents)
<br>



# FEATURES

## Existing Features 
#### **Navigation menu displayed across all pages**

- Navigation menu
- Website Title that redirects to home page
- Contact Form
- Ability to create, read, update and delete comments
- Ability for admin to approve comments in admin panel
- Ability to sign in, sign out and register
- Ability to view individual blog posts and like/unlike posts. 
    

## Features to Implement in the future 
- Blog management tool for site admin to implement CRUD functionality on blog posts
- Blog management tool for site admin to implement comment approval outside of admin panel
- - Blog management tool for site admin to read and respond to contact queries

[back to top](#Table-of-contents)
<br>


# Database

One relational database was used to create this site - during production and deployment, Postgres was used. 
Amazon Web Services is used for the hosting of all media and static files. 
<br>
The database contains three models - Post, Comment and Contact. 

![database]()<br>

Sitemap screenshot 

![sitemap]()<br>

###

# Technologies Used

- [Django3](https://www.djangoproject.com/) framework
- [HTML5](https://en.wikipedia.org/wiki/HTML) for markup
- [CSS3](https://en.wikipedia.org/wiki/CSS) for style
- [Postgressql](https://www.postgresql.org/) for the database
- [Bootstrap 4 ](https://mdbootstrap.com/) for bulk of CSS
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for interaction
- [JQUERY](https://jquery.com/) for interaction
- [Python3](https://www.python.org/) as a backend 
- [Google Fonts](https://fonts.google.com/) for fonts
- [Font Awesome](https://fontawesome.com/) for icons
- [Amazon AWS](https://aws.amazon.com/) for image and static files hosting
- [Summernote](https://summernote.org/) editor for adding and editing updates
- [Gitpod](https://www.gitpod.io/) for cloud IDE
- [Git](https://git-scm.com/) for source control
- [GitHub](https://github.com/) for file and documents hosting
- [Heroku](https://www.heroku.com/) for website deployment


## Resources 

- Code Institute Course Materials
- [Stack Overflow](https://stackoverflow.com/)
- [YouTube](https://www.youtube.com/)
- [W3schools](https://www.w3schools.com/)
- [Google](https://www.google.com/)


## Tools

- [Balsamiq](https://balsamiq.com/) for wireframes
- [Pixlr](https://pixlr.com/e/) for resizing images
- [W3C Markup Validation Service](https://validator.w3.org/) for testing HTML code
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) for testing CSS code
- [jshint](https://jshint.com/) for testing JavaScript code
- [PEP8 Online](http://pep8online.com/) for checking Python code compliance
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) for testing, style checking and debugging

***

<br>

[back to top](#Table-of-contents)
<br>

# Testing
The entirety of the testing was done manually. 

PEP8 Flake tests, HTML and CSS Validators were also done! 
html and CSS validator

HTML Validation was done using W3C Nu HTML Validator:
<img src="">
<br>
<br>
CSS Validation was done using W3C Jigsaw Validator:
<img src="">
<br>
<br>
Lighthouse testing was done using Chrome Developer Tools:
<img src="">

# Bugs
When removing a blog post image and leaving it as blank, it breaks the image link instead of rendering default image. 
<img src="">

# Deployment
## Heroku Deployment
This project was deployed through Heroku in the following steps:

1) A repository was created in github using the student template
2) The repo was pushed to the cloud based IDE called GITPOD
3) In the GITPOD terminal, django and its supporting libraries were installed using pip3
4) The project is then created using using python3 manage.py startproject projectname
5) The first app is then created using python3 manage.py createapp appname
6) The app is then registered in the setting file in the project level settings.py. 
7) An app is the created in heroku and the installation of postgres is done under resources making sure to add postgres url to config vars
8) Back in the GITPOD terminal, install Django Database and psycopg2
9) Import dj database url in your settings file and replace default database with dj database passing it postgres url
10) Migrate database and load data in gitpod terminal 
11) Create another super user
12) Create an if else statement that checks the database url and runs the correct database accordingly. 
13) Install gunicorn, create a procfile and log into heroku in the terminal. 
14) Disable the static files using heroku config:set, DISABLE_COLLECTSTATIC=1 --app appname
15) Add heroku app and localhost to allowed hosts in settings.py
16) Generate a secret key using Django secret key generator and add to config vars whilst linking it to settings.py
16) Add, commit and push changes to Github
17) Set heroku to automatically deploy but setting it to Github and searching/connecting to correct repo. 


[back to top](#Table-of-contents)
<br>


# Credits
### Code
* [Code Institute](https://codeinstitute.net/ie/) supplied the bulk of the tutorials, resources and support for this project!
* [Bootstrap](https://getbootstrap.com/) for creating a responsive site.
* [Twilio](https://getbootstrap.com/) for their contact form tutorial which was adapted to create mine
* [Bootstrap](https://getbootstrap.com/) for creating a responsive site.
* [w3schools](https://www.w3schools.com/) was used as a general source of knowledge 
* [youtube](https://www.youtube.com/) 
* [Stack Overflow](https://stackoverflow.com/) 
* [MDN Web Docs](https://developer.mozilla.org/) for various tutorials and walkthroughs!
* [Django Docs](https://docs.djangoproject.com/en/3.2/) for django documentation.



### Media
[Image credits]()



### Acknowledgements
* I would like to thank the Slack Community and Tutor support for their help, especially the women in my cohort, who went above and beyond to help me! 
* I would like to thank Kasia Bogucka my class cohort facilitator for her tireless assistance and support! Your weekly standup meetings and one-on-one huddles saved my hide! 
* I would like to thank my mentor Chris for his support, guidance and feedback, without him I would have given into my imposter syndrome long ago! Thanks for going the extra mile for me!
* I would like to also thank all my family, friends and associates who have supported me during the making of this project!
 
***
[back to top](#Table-of-contents)