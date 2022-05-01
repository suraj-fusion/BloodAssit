# Blood Assit
#### Video Demo:  <https://youtu.be/5elPDl3QQmk>
#### Description:
Hello World,This is BloodAssit, My final Project for CS50x.During my first year of college I joined a blood donation NGO that helps people connect with blood donors.So by drawing some inspiration from that I decided to create my own e blood bank ,BloodAssit.

The Webapp starts with a Login page where user has to log in to the website.I have added backend checks to login to make sure that user logs in correctly.
It also has a Signup tab on the navigation bar uptop where new user can SignUp.



The homepage of this web app is all about encouraging people to donate blood and to register to this noble cause,by presenting some unfortunate statistics and facts related to blood donations in India.


I created a navigation bar uptop that have tabs to go to the Homepage, to Register oneself to donate blood,to Locate a donor,to know some general myths related to blood donation and to know some information on blood.I have decided to make it responsive by bootstrap by adding a toggler button so that the website is usable for mobile users.


In the register webpage,first i encourage the user to read the conditions to make sure that the user is fit to donate blood.
It leads to a condition webpage which presents those conditions in a neat way by using an unordered list.


Next i have created a form to ask the user for their Name,Age,City,State or Union territory,their blood type and their Phone number.I make sure that the user has provided a name, their age(also that their age fall into the prescribed age for blood donation),City,State,Blood type and Phone number through back end checks.I did not implement front end checks to prevent users to change the conditions themselves by altering the html that the users browser receives.
I have also made sure that no single user can register multiple times.
If the user fails to fill the form correctly it leads to a error webpage which tells the user exactly where they  went wrong.
If the user succeeds to fill the form correctly a registered webpage is rendered which tells the user that they are registered.



The Locate Webpage does what its name conveys ,it helps people in need of blood ,find the donors who have previously registered to donate.The user can search for the donors according to the state that they reside in and the blood group that they need.Upon clicking the search button a search webpage is rendered which presents the user with the information they need in a tabular way.I have decided to include a similar table that displays information about all the donors in the locate webpage itself where user can decide to directly look through all our donors.


The Myths tab leads to Myths webpage that lets the user know about general myths related to blood donations that people have and also the associated fact of the myth.


The info webpage presents some information related to blood that donors may know.

The Deregister tab on the right as the name suggests deregisters the user from the donors database.

Logout tab as the name suggests logs the user out.


Finally,I have also created a layout.html file that extends all these webpages using jinja.I have tried to style this webpage in a very minimalist way using  bootstrap framework.I have created a separate layoutlogsign.html file that extends the layout of signup and login webpages.

A huge thank you to all CS50 staff and Harvard for this awesome course.

This was BloodAssit.