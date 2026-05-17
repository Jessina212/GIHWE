# GIMHE: Green Integration Of Mankind With Environment
#### Video Demo:  <https://youtu.be/hxeyt2TIE0o>
#### Description:

This project is crafted keeping in mind the love for the environment and the existing crisis of protecting it.\
What it's supposed to do is provide the user with a (randomly generated) task which users can do within whatever amount of time they have in minutes, **allowing to incorporate managing the environment with daily activities** and show people it's not hard to integrate nature and love for it with their daily routines.\
This is required since nowadays, people do not have much time at hand and thus are not able to give much time to the environment. Therefore, *time-based tasks actually help with doing small tasks within a limited time*- which would be beneficial for the nature in the long run.
The current version focuses on core functionality. That said, this project is not incomplete in any way, just a scope for further improvement in the future.\
An additional functionality for this is it also provides a **positive quote** to (*try and) brighten* the user's day.


#### Functionality
Allow me to introduce how the project was made -
1. Firstly the login/register/logout page- this was taken from the Finance problem set. I do understand how they are actually implemented(I created the register function in finance), and thus not just copy-pasted. Same for the logout page.


2. The Content Page: This consists of
a. The **greeting for the user**- this greets the user with the username that they logged in with. A simple and warm welcome to the web page.
b. Provides a **positive quote**-  from the database itself. Randomly generated everytime the website reloads.
c. Takes input from the user and provides a task that can be done within that time. Many different tasks have been input in the database, so different tasks come up when same time is input twice.


3. **Flashcard for task** : this was implemented using Java, CSS and HTML.
   Most of the tasks are those which the user can ***perform anywhere, without any physical constraint and within the given time.***
   Some tasks, however, require certain physical resources- such as tasks like "Plant a Seed", which would obviously require a pot, seeds and some sand.
   So the user, according to the materials available to them, can input the time again and get another task or continue with the one given to them.


#### Technologies Used
* **Python, Flask** - Backend Logic and Routing
* **SQL** - Database Management for Quotes, Tasks and Users
* **HTML, CSS, JavaScript** - Frontend design and Interactivity


#### Citing use of ai
ChatGPT helped with debugging.\
Adding hundred of tasks, quotes within the database.\
Help with CSS.


#### What I did on my Own
Came up with the idea of the project\
Designed app.py in such a way that it fits the idea for the project\
Made layout.html and all other HTML files\
Decided the name for the project\
The CSS decisions for the project\
Made the flashcard come to reality from thought using JavaScript\
Used SQL in a way which helps the project


#### Design decisions
The double card design for the quotes and input was selected after checking how the single card looked- the page seemed empty.\
Then the shadow double card design came on accidentally as a code error, but seemed better and so decided to keep it.

The flashcard design was curated after a lot of debate among myself- since the tasks are the main content in the web page and needed to be presented effectively, on the other hand- it seemed like a lot at once.\
After much debate, went on with the idea of creating them and they turned out better than expected.

The page background `#eef7f2` was decided such because it provides a good feel of nature.

#### Limitation and Future Improvements
1. It only gives tasks for input between 1- 120 minutes.
   > Improvement- To be expanded in the future.

2. Only gives a short description of the task.
   > Improvement-  Video links, tutorials, detailed desription along with images, etc to be added so as to support and help the user performing the task.

3. Login and Registering only allowed with unique usernames. People with same names cannot use the site.
   > Improvement- Registering to be based on another parameter (id).

4. Everything - quotes, tasks, greetings- compiled on one page.
   > Improvement- Different HTML pages with additional content to be created.

5. Greeting with the username as it is, without capitalising or specifying any case.
   > Improvement- With some constraints on the username(such as alphabets only, no numbers allowed), this could be improved.

6. No constraint on password, username.
   > Improvement- Adding constrains such as passwords to be minimum 8 characters long, etc.

7. Daily Streak Count could be added to make the user more interested and consistent in performing tasks, which would in turn be more beneficial to the environment as well.

### Closing note

The main motive for this project is that if everyone completes these tasks, performing one each day, irrespective of the time they have - the world would ultimately become a better place.
