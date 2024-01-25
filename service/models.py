from django.db import IntegrityError, models
from django.contrib.auth.models import User
import requests
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    email = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name

class offer(models.Model):
    id = models.BigAutoField(primary_key=True)
    agreement_name = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    provider_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    external_person = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    required_notes = models.CharField(max_length=255)
    date_until = models.DateField(null=True, blank=True)
    document_data = models.BinaryField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.employee_name

class offer_from_api(models.Model):
    agreement_title_id = models.CharField(max_length=255)
    agreement_title = models.CharField(max_length=255)
    servicerequest_id = models.CharField(max_length=255)
    project_information = models.TextField()
    employee_name = models.CharField(max_length=255)
    provider_name = models.CharField(max_length=255)
    contactperson = models.CharField(max_length=255)
    externalperson = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=10, decimal_places=2, unique=True)
    notes = models.TextField()
    document = models.TextField()
    status = models.CharField(max_length=255)
    v = models.IntegerField()
    
    def __str__(self):
        return self.agreement_title_id

    @classmethod
    def fetch_and_store_offers(cls):
        providers = ['A', 'B', 'C', 'D']
        base_url = "http://ec2-52-90-1-48.compute-1.amazonaws.com:4000/users/offers?provider="

        for provider in providers:
            api_url = f"{base_url}{provider}"
            response = requests.get(api_url)

            if response.status_code == 200:
                offers_data = response.json()

                for offer in offers_data:
                    rate = offer.get('rate')

                    # Check if this rate was marked as deleted
                    if DeletedOffer.objects.filter(rate=rate).exists():
                        print(f"Skipped creating offer with rate {rate} as it was previously deleted.")
                        continue

                    try:
                        # Use get_or_create to avoid recreating an existing offer
                        obj, created = cls.objects.get_or_create(
                            rate=rate,
                            defaults={
                                'agreement_title_id': offer.get('agreement_title_id'),
                                'agreement_title': offer.get('agreement_title'),
                                'servicerequest_id': offer.get('servicerequest_id'),
                                'project_information': offer.get('project_information'),
                                'employee_name': offer.get('employee_name'),
                                'provider_name': offer.get('provider_name'),
                                'contactperson': offer.get('contactperson'),
                                'externalperson': offer.get('externalperson'),
                                'notes': offer.get('notes'),
                                'document': offer.get('document'),
                                'status': offer.get('status'),
                                'v': offer.get('__v'),
                            }
                        )
                        if created:
                            print(f"Offer with rate {rate} created successfully.")
                        else:
                            print(f"Offer with rate {rate} already exists.")
                    except IntegrityError as e:
                        print(f"Could not create offer with rate {rate}: {e}")
            else:
                print(f"Failed to fetch offers for provider {provider}, status code: {response.status_code}")


class DeletedOffer(models.Model):
    rate = models.DecimalField(max_digits=10, decimal_places=2, unique=True)
    reason = models.TextField(default="Not specified") 
    def __str__(self):
        return str(self.rate)


# Define a model for approved offers
class ApprovedOffer(models.Model):
    agreement_title = models.CharField(max_length=100)
    project_information = models.TextField()
    status = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as needed



class Request(models.Model):
    cat=(('0-2','0-2'),('2-5','2-5'),('5-7','5-7'),('7+','7+'))
    project_information = models.CharField(max_length=1000,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    work_location = models.CharField(max_length=50,null=True)
    contract_period = models.PositiveIntegerField(null=True)
    domain = models.CharField(max_length=40,null=False)
    role = models.CharField(max_length=40,null=False)
    experience = models.CharField(max_length=50,choices=cat,default='0-2')
    technology = models.CharField(max_length=40)
    further_skills = models.CharField(max_length=100,null=True)
    upload_resume = models.FileField(upload_to='resumes/',null=True,blank=True)
    onsite_days = models.PositiveIntegerField(null=True)
    remote_days = models.PositiveIntegerField(null=True)
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    offer=models.ForeignKey('offer',on_delete=models.CASCADE,null=True)
    cost=models.PositiveIntegerField(null=True)
    stat=(('Pending','Pending'),('Released','Released'))
    status=models.CharField(max_length=50,choices=stat,default='Pending',null=True)
    agreement_title = models.CharField(max_length=100, null=True)
    agreement_title_id = models.PositiveIntegerField(null=True)
    def __str__(self):
        return self.project_information

class Feedback(models.Model):
    date = models.DateField(auto_now=True)
    by = models.CharField(max_length=40)
    message = models.CharField(max_length=500)

