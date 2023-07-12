# Blood Assit
#### Video Demo:  <https://youtu.be/5elPDl3QQmk>
#### Finally Hosted it check it out : http://fusion123.pythonanywhere.com/login
#### Description:
Hello World,This is BloodAssit, My final Project for CS50x.During my first year of college I joined a blood donation NGO that helps people connect with blood donors.So by drawing some inspiration from that I decided to create my own e blood bank ,BloodAssit.

The Webapp starts with a Login page where user has to log in to the website.I have added backend checks to login to make sure that user logs in correctly.
It also has a Signup tab on the navigation bar uptop where new user can SignUp.


![Screenshot 2023-07-12 192220](https://github.com/suraj-fusion/BloodAssit/assets/79706268/5b4afee4-14cd-43f1-bcd6-fe7b2d8d1767)

The homepage of this web app is all about encouraging people to donate blood and to register to this noble cause,by presenting some unfortunate statistics and facts related to blood donations in India.


I created a navigation bar uptop that have tabs to go to the Homepage, to Register oneself to donate blood,to Locate a donor,to know some general myths related to blood donation and to know some information on blood.I have decided to make it responsive by bootstrap by adding a toggler button so that the website is usable for mobile users.

![Screenshot 2023-07-12 192255](https://github.com/suraj-fusion/BloodAssit/assets/79706268/81577835-d3d1-4832-a60f-7d8ab6b3a03c)

In the register webpage,first i encourage the user to read the conditions to make sure that the user is fit to donate blood.
It leads to a condition webpage which presents those conditions in a neat way by using an unordered list.


Next i have created a form to ask the user for their Name,Age,City,State or Union territory,their blood type and their Phone number.I make sure that the user has provided a name, their age(also that their age fall into the prescribed age for blood donation),City,State,Blood type and Phone number through back end checks.I did not implement front end checks to prevent users to change the conditions themselves by altering the html that the users browser receives.
I have also made sure that no single user can register multiple times.
If the user fails to fill the form correctly it leads to a error webpage which tells the user exactly where they  went wrong.
If the user succeeds to fill the form correctly a registered webpage is rendered which tells the user that they are registered.


![Screenshot 2023-07-12 192313](https://github.com/suraj-fusion/BloodAssit/assets/79706268/661c5fb0-df7d-45e2-b8ea-1a417ae11e60)


The Locate Webpage does what its name conveys ,it helps people in need of blood ,find the donors who have previously registered to donate.The user can search for the donors according to the state that they reside in and the blood group that they need.Upon clicking the search button a search webpage is rendered which presents the user with the information they need in a tabular way.I have decided to include a similar table that displays information about all the donors in the locate webpage itself where user can decide to directly look through all our donors.


![Screenshot 2023-07-12 192332](https://github.com/suraj-fusion/BloodAssit/assets/79706268/00eb43c4-8ec6-42b7-8d16-ea423fe9e8ad)


The Myths tab leads to Myths webpage that lets the user know about general myths related to blood donations that people have and also the associated fact of the myth.

![Screenshot 2023-07-12 193314](https://github.com/suraj-fusion/BloodAssit/assets/79706268/b4e60d39-0d1e-457d-b917-fa8a2253e797)


The info webpage presents some information related to blood that donors may know.

![Screenshot 2023-07-12 193330](https://github.com/suraj-fusion/BloodAssit/assets/79706268/403161d8-9798-4a88-85bf-c4e89f47278a)
The Deregister tab on the right as the name suggests deregisters the user from the donors database.

Logout tab as the name suggests logs the user out.


Finally,I have also created a layout.html file that extends all these webpages using jinja.I have tried to style this webpage in a very minimalist way using  bootstrap framework.I have created a separate layoutlogsign.html file that extends the layout of signup and login webpages.

A huge thank you to all CS50 staff and Harvard for this awesome course.

This was BloodAssit.
