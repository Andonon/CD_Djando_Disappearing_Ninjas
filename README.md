# CD_Djando_Disappearing_Ninjas
Troy Center troycenter1@gmail.com June 2017 
Coding Dojo Django "Disappearing Ninjas" assignment. 

Disappearing Ninjas
Rebuild the Disappearing Ninjas assignment from flask, this time using Django.

This exercise will help you practice using URLs to render templates and static content.

<img src="http://s3.amazonaws.com/General_V88/boomyeah/company_209/chapter_3832/handouts/chapter3832_6610_tmnt.png" alt="Coding Dojo Assignment Image">

Here is your product backlog:

<ul> 
    <li>Default page (‘localhost:8000’) should display a view that displays “No ninjas here.”</li>
    <li>Visiting /ninjas should display all four Ninja Turtles (Leonardo, Michelangelo, Raphael, and Donatello)</li>
    <li>Visiting /ninjas/[ninja_color] should display the corresponding Ninja Turtle</li>
        <li>Use named groups to grab the color parameter out of the requested URL</li>
        <li>I.e. visiting /ninjas/blue should only display Leonardo</li>
        <li>/ninjas/orange => Michelangelo.</li>
        <li>/ninjas/red => Raphael</li>
        <li>/ninjas/purple => Donatello</li>
    <li>If a user tries to hack into your web app by specifying a color or string combination other than the colors (blue, orange, red, and purple) that you’re anticipating, then display a picture of April O'Neil.</li> 
    <li>All of the ninjas/[ninja_color] paths should just be one route (not 5 separate routes…)</li>
</ul>