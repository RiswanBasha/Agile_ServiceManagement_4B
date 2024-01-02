from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
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


class Request(models.Model):
    # cat=(('two wheeler with gear','two wheeler with gear'),('two wheeler without gear','two wheeler without gear'),('three wheeler','three wheeler'),('four wheeler','four wheeler'))
    # category=models.CharField(max_length=50,choices=cat)

    # _no=models.PositiveIntegerField(null=False)
    # _name = models.CharField(max_length=40,null=False)
    # _model = models.CharField(max_length=40,null=False)
    # _brand = models.CharField(max_length=40,null=False)

    # problem_description = models.CharField(max_length=500,null=False)
    # date=models.DateField(auto_now=True)
    # cost=models.PositiveIntegerField(null=True)

    # customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    # offer=models.ForeignKey('offer',on_delete=models.CASCADE,null=True)

    # stat=(('Pending','Pending'),('Approved','Approved'),('Repairing','Repairing'),('Repairing Done','Repairing Done'),('Released','Released'))
    # status=models.CharField(max_length=50,choices=stat,default='Pending',null=True)

    # def __str__(self):
    #     return self.problem_description
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
    stat=(('Pending','Pending'),('Approved','Approved'),('In-Progress','In-Progress'),('Repairing Done','Repairing Done'),('Released','Released'))
    status=models.CharField(max_length=50,choices=stat,default='Pending',null=True)

    def __str__(self):
        return self.project_information

class Feedback(models.Model):
    date = models.DateField(auto_now=True)
    by = models.CharField(max_length=40)
    message = models.CharField(max_length=500)

