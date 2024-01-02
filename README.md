#  SERVICE MANAGEMENT
![developer](https://img.shields.io/badge/Developed%20By%20%3A-Sumit%20Kumar-red)
---
## SCREENSHOTS
### Home Page
![dashboard snap](https://github.com/sumitkumar1503/servicemanagement/blob/master/static/screenshots/home.png?raw=true)
### Admin Dashboard Dark theme
![dashboard snap](https://github.com/sumitkumar1503/servicemanagement/blob/master/static/screenshots/admin_dark.png?raw=true)
### Admin Dashboard Light theme
![dashboard snap](https://github.com/sumitkumar1503/servicemanagement/blob/master/static/screenshots/admin_light.png?raw=true)
### offer Dashboard
![dashboard snap](https://github.com/sumitkumar1503/servicemanagement/blob/master/static/screenshots/offer_dashboard.png?raw=true)
### Customer Dashboard
![dashboard snap](https://github.com/sumitkumar1503/servicemanagement/blob/master/static/screenshots/customer_dashboard.png?raw=true)
---
## FUNCTIONS
## Customer
- customer will signup and login into system
- customer can make request for service of their  by providing details ( number, model, problem description etc.)
- After Request approved by admin, customer can check cost, status of service
- customer can delete request (Enquiry) if customer change their mind or not approved by admin (ONLY PENDING REQUEST CAN BE DELETED )
- customer can check status of Request(Enquiry) that is Pending, Approved, Repairing, Repairing Done, Released
- customer can check invoice details or repaired s
- customer can send feedback to admin
- customer can see/edit their profile
---
## offer
- offer will apply for job by providing details like (skills, address, mobile etc.)
- Admin will hire(approve) offer account based on skill
- After account approval, offer can login into system
- offer can see how many work (s to repair) is assigned to me
- offer can change status of service ('Repairing', 'Repairing Done') according to work progress
- offer can see salary and how many s he/she have repaired so far
- offer can send feedback to admin
- offer can see/edit their profile
---
### Admin
- First admin will login ( for username/password run following command in cmd )
```
py manage.py createsuperuser
```
- Give username, email, password and your admin account will be created.
- After login , admin can see how many customer, offer, recent service orders on dashboard
- Admin can see/add/update/delete customers
- Admin can see each customer invoice (if two request made by same customer it will show total sum of both request)
- Admin can see/add/update/delete offers
- Admin can approve(hire) offers (requested by offer) based on their skills
- Admin can see/update offer salary
- Admin can see/update/delete request/enquiry for service sent by customer
- Admin can also make request for service (suppose customer directly reached to service center/office)
- Admin can approve request for service made by customer and assign to offer for repairing and will provide cost according to problem description
- Admin can see all service cost of request (both approved and pending)
- Admin can see feedbacks sent by customer/offer
---
### Other Features
- we can change theme of website day(white) and night(black)
- if customer is deleted by admin then their request(Enquiry) will be deleted automatically

## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :
```
pip install django==3.0.5
pip install django-widget-tweaks

```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```

## CHANGES REQUIRED FOR CONTACT US PAGE
- In settins.py file, You have to give your email and password
```
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'your email password'
EMAIL_RECEIVING_USER = 'youremail@gmail.com'
```
- Login to gmail through host email id in your browser and open following link and turn it ON
```
https://myaccount.google.com/lesssecureapps
```
## Drawbacks/LoopHoles
- When customer/offer edit their profile then he/she must login again because their username/password is updated in db.
## Credits
- Tran Anh Tuat ( Admin Dashboard UI )
## Disclaimer
This project is developed for demo purpose and it's not supposed to be used in real application.

## Feedback
Any suggestion and feedback is welcome. You can message me on facebook
- [Contact on Facebook](https://fb.com/sumit.luv)
- [Subscribe my Channel LazyCoder On Youtube](https://youtube.com/lazycoders)
