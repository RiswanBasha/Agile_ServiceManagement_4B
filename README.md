**<h2>Agile Project - Service Management Portal - 4B</h2>**

**<h3>Members:</h3>**

**1. Riswan Basha Saleem Basha**

**2. Amith Nair**

**3. Jishnu Shivaraman**

**4. Shivakumar Veerapur**



**<h3>Steps to run the project:</h3>**

1. Clone the project: `git clone https://github.com/RiswanBasha/Agile_ServiceManagement_4B.git`
2. Install the depedencies: `pip install -r requirements.txt`
3. Do make migrations for the model: `python manage.py makemigrations`
4. Migrate it: `python manage.py migrate`

**If you like to be an admin:**
1. For creating superuser: `python manage.py createsuperuser`

**For Run:** : `python manage.py runserver`

**Service Management Platform Architecture: A Comprehensive Overview**

**1. User Interface (UI) Layer:**

Home page: Entry point with login/sign-up options, admin access, and a welcoming design.

Customer Signup/Login page: Allows users to register and log in, with integrated social media options.

Dashboard: Centralized display of job requests, status updates, and provider messages.

Make Request: Interface for users to submit detailed job requests, which are then posted to external groups.

View Pending Request: Where users track and manage their pending job requests.

Offers: Section where users explore and respond to job offers fetched from external provider APIs.

Feedback: Enables users to provide feedback on services and offers.

Admin Login Page: Secure access point for administrators to manage the platform.

**2. Backend Layer:**

User Management: Handles registration, authentication, and user profile management.

Request Management: Processes and stores job requests, and manages their lifecycle.

Offer Management: Integrates with external APIs to fetch and display offers to users.

Feedback System: Collects and processes user feedback on services and providers.

**3. Database Layer:**

Stores user profiles, job requests, offers, and feedback.

Manages the authentication information for users and administrators.

**3. Integration Layer:**

API Endpoints: Communicate with external groups to fetch offers and post requests.

Admin Functions: Provide admins with the ability to manage user profiles, requests, and system settings.

**Important Link:**
  (1. http://13.48.42.106:8000/  --> Service Management Portal)
  (2. http://codexauthv2.onrender.com/api/register/  --> Register component from team 1)
  (3. http://codexauthv2.onrender.com/api/login/ --> login component from team 1)
  (4. https://dg4gi3uw0m2xs.cloudfront.net/agreement/ --> Master Agreement API from 2B)
  (5. http://ec2-52-90-1-48.compute-1.amazonaws.com:4000/users/offers?provider=A --> Offers API  from 3B of provider A)
  (6. http://ec2-52-90-1-48.compute-1.amazonaws.com:4000/users/offers?provider=B --> Offers API  from 3B of provider B)
  (7. http://ec2-52-90-1-48.compute-1.amazonaws.com:4000/users/offers?provider=C --> Offers API  from 3B of provider C)
  (8. http://ec2-52-90-1-48.compute-1.amazonaws.com:4000/users/offers?provider=D --> Offers API  from 3B of provider D)

