<h1 style="color: orange">&nbsp; Airborne <span style="color: #bafc03;">https://airborne.kk1729.repl.co</span></h1>

> Came in top 5 and won 3rd place 🥳!

<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="aeroplane.png" alt="Logo" width="200" height="200">
  </a>

  <h1 align="center">Airborne</h3>

  <h3 align="center">
     &raquo; Discover The Best Holiday Spots In The World, Adventure Awaits.
    <br />
    <a href="https://airborne.kk1729.repl.co/" style="color: orange"><strong>Visit the website</strong></a>
    
</p>
<br >

<h2 align="center" style="color: orange">How to use</h1>

<h3 align="center" style="color: orange"> Dicover the best hand-picked holiday spots from a database of over 45 locations from around the world at the <a href="https://airborne.kk1729.repl.co/">Website</a></h3>

## 1. [Locations Page/ Home Page](https://airborne.kk1729.repl.co/all)

    - You can see all the locations in the database and search/filter for particular
    cities using keywords, factors of the location and name of the country etc using the search bar.

    - For each location that appears u can see its related tags which when clicked will take you to a page containing all the locations with the respective #tag-name

    - You can click on the learn more button at the bottom of the card and it redirect you to a page containing detailed information about the particular locations and all the factors you need to consider for a vacation.

## 2. The location page

    - Here you can see the description of the location.

    - On clicking the map-marker icon beside the name of the location, you can view the location on google maps

    - You can also see the current weather conditions and the forecast for 7 days with the min-max temperature.

    - You can review a location and rate it and also read others reviews and ratings

## 3. Features

    - You can favourite any location by clciking the star icon on a location

    - You can mark a pl ace as visited by click on the visited icon on the bottom of the location card

## 4. [Profile Page](https://airborne.kk1729.repl.co/users/profile)

    - Here you can see the places that you have marked favourite

    - Here you can see the places you have marked as visited

    ~ You can see the search history of all the things you have searched in the search bar

    ~ You can see all the reviews and delete them if u want to

<h1 style="color: orange" align="center">
    Setting Up the project on your machine  
</h1>


### Images
<img src="images/Screenshot (93).png" >
<img src="images/Screenshot (95).png" >
<img src="images/Screenshot (97).png" >
<img src="images/Screenshot (100).png" >
<img src="images/Screenshot (101).png" >
<img src="images/Screenshot (94).png" >
### Install this repo or clone it and unzip it into a single folder.

<br >

### Activate a virtual env an run the following commands. Make sure you are in the same directory as manage.py, core, holiday_planner, static, static_cdn and users.

### download the database with all the cities from https://github.com/KrishnaKanth1729/sqliteForAirborne/blob/main/db.sqlite3 and place it in the same directory as manage.py and make sure the it is saved as db.sqlite3

<br >

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Now navigate your browser to 127.0.0.1:8000 and make sure to disable the CORS error settings in browser. You can now use the website with the full functionality
