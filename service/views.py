from django.shortcuts import render,redirect,reverse
from service import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.db.models import Q

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'service/index.html')


#for showing signup/login button for customer
def customerclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'service/customerclick.html')

#for showing signup/login button for offers
def offersclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'service/offersclick.html')


#for showing signup/login button for ADMIN(by sumit)
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')


def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('customerlogin')
    return render(request,'service/customersignup.html',context=mydict)


def offer_signup_view(request):
    userForm=forms.offerUserForm()
    offerForm=forms.offerForm()
    mydict={'userForm':userForm,'offerForm':offerForm}
    if request.method=='POST':
        userForm=forms.offerUserForm(request.POST)
        offerForm=forms.offerForm(request.POST,request.FILES)
        if userForm.is_valid() and offerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            offer=offerForm.save(commit=False)
            offer.user=user
            offer.save()
            my_offer_group = Group.objects.get_or_create(name='offer')
            my_offer_group[0].user_set.add(user)
        return HttpResponseRedirect('offerlogin')
    return render(request,'service/offersignup.html',context=mydict)


#for checking user customer, offer or admin(by sumit)
def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()


def afterlogin_view(request):
    if is_customer(request.user):
        print("User is identified as a customer")
        return redirect('customer-dashboard')
    else:
        print("User is NOT identified as a customer")
        return redirect('admin-dashboard')




#============================================================================================
# ADMIN RELATED views start
#============================================================================================

@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    enquiry=models.Request.objects.all().order_by('-id')
    customers=[]
    for enq in enquiry:
        customer=models.Customer.objects.get(id=enq.customer_id)
        customers.append(customer)
    dict={
    'total_customer':models.Customer.objects.all().count(),
    'total_offer':models.offer.objects.all().count(),
    'total_request':models.Request.objects.all().count(),
    'total_feedback':models.Feedback.objects.all().count(),
    'data':zip(customers,enquiry),
    }
    return render(request,'service/admin_dashboard.html',context=dict)


@login_required(login_url='adminlogin')
def admin_customer_view(request):
    return render(request,'service/admin_customer.html')

@login_required(login_url='adminlogin')
def admin_view_customer_view(request):
    customers=models.Customer.objects.all()
    return render(request,'service/admin_view_customer.html',{'customers':customers})


@login_required(login_url='adminlogin')
def delete_customer_view(request,pk):
    customer=models.Customer.objects.get(id=pk)
    user=models.User.objects.get(id=customer.user_id)
    user.delete()
    customer.delete()
    return redirect('admin-view-customer')


@login_required(login_url='adminlogin')
def update_customer_view(request,pk):
    customer=models.Customer.objects.get(id=pk)
    user=models.User.objects.get(id=customer.user_id)
    userForm=forms.CustomerUserForm(instance=user)
    customerForm=forms.CustomerForm(request.FILES,instance=customer)
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST,instance=user)
        customerForm=forms.CustomerForm(request.POST,request.FILES,instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return redirect('admin-view-customer')
    return render(request,'service/update_customer.html',context=mydict)


@login_required(login_url='adminlogin')
def admin_add_customer_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('/admin-view-customer')
    return render(request,'service/admin_add_customer.html',context=mydict)


@login_required(login_url='adminlogin')
def admin_view_customer_enquiry_view(request):
    enquiry=models.Request.objects.all().order_by('-id')
    customers=[]
    for enq in enquiry:
        customer=models.Customer.objects.get(id=enq.customer_id)
        customers.append(customer)
    return render(request,'service/admin_view_customer_enquiry.html',{'data':zip(customers,enquiry)})


@login_required(login_url='adminlogin')
def admin_view_customer_invoice_view(request):
    enquiry=models.Request.objects.values('customer_id').annotate(Sum('cost'))
    print(enquiry)
    customers=[]
    for enq in enquiry:
        print(enq)
        customer=models.Customer.objects.get(id=enq['customer_id'])
        customers.append(customer)
    return render(request,'service/admin_view_customer_invoice.html',{'data':zip(customers,enquiry)})

@login_required(login_url='adminlogin')
def admin_offer_view(request):
    return render(request,'service/admin_offer.html')


@login_required(login_url='adminlogin')
def admin_approve_offer_view(request):
    offers=models.offer.objects.all().filter(status=False)
    return render(request,'service/admin_approve_offer.html',{'offers':offers})

@login_required(login_url='adminlogin')
def approve_offer_view(request,pk):
    offerSalary=forms.offerSalaryForm()
    if request.method=='POST':
        offerSalary=forms.offerSalaryForm(request.POST)
        if offerSalary.is_valid():
            offer=models.offer.objects.get(id=pk)
            offer.salary=offerSalary.cleaned_data['salary']
            offer.status=True
            offer.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-approve-offer')
    return render(request,'service/admin_approve_offer_details.html',{'offerSalary':offerSalary})


@login_required(login_url='adminlogin')
def delete_offer_view(request,pk):
    offer=models.offer.objects.get(id=pk)
    user=models.User.objects.get(id=offer.user_id)
    user.delete()
    offer.delete()
    return redirect('admin-approve-offer')


# @login_required(login_url='adminlogin')
# def admin_add_offer_view(request):
#     userForm=forms.offerUserForm()
#     offerForm=forms.offerForm()
#     offerSalary=forms.offerSalaryForm()
#     mydict={'userForm':userForm,'offerForm':offerForm,'offerSalary':offerSalary}
#     if request.method=='POST':
#         userForm=forms.offerUserForm(request.POST)
#         offerForm=forms.offerForm(request.POST,request.FILES)
#         offerSalary=forms.offerSalaryForm(request.POST)
#         if userForm.is_valid() and offerForm.is_valid() and offerSalary.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()
#             offer=offerForm.save(commit=False)
#             offer.user=user
#             offer.status=True
#             offer.salary=offerSalary.cleaned_data['salary']
#             offer.save()
#             my_offer_group = Group.objects.get_or_create(name='offer')
#             my_offer_group[0].user_set.add(user)
#             return HttpResponseRedirect('admin-view-offer')
#         else:
#             print('problem in form')
#     return render(request,'/admin_add_offer.html',context=mydict)

@login_required(login_url='adminlogin')
def admin_add_offer_view(request):
    if request.method == 'POST':
        offer_form = forms.offerForm(request.POST, request.FILES)
        if offer_form.is_valid():
            offer = offer_form.save(commit=False)
            offer.status = True  # Set default value or logic for status
            offer.save()
            return HttpResponseRedirect('admin-view-offer')
    else:
        offer_form = forms.offerForm()
    
    context = {'offer_form': offer_form}
    return render(request, 'service/admin_add_offer.html', context)

@login_required(login_url='adminlogin')
def admin_view_offer_view(request):
    offers=models.offer.objects.all()
    return render(request,'service/admin_view_offer.html',{'offers':offers})


@login_required(login_url='adminlogin')
def delete_offer_view(request,pk):
    offer=models.offer.objects.get(id=pk)
    offer.delete()
    return redirect('admin-view-offer')


# views.py
@login_required(login_url='adminlogin')
def update_offer_view(request, pk):
    offer = models.offer.objects.get(id=pk)
    offerForm = forms.offerForm(request.POST or None, request.FILES or None, instance=offer)
    mydict = {'offerForm': offerForm}
    
    if request.method == 'POST':
        offerForm = forms.offerForm(request.POST, request.FILES, instance=offer)
        if offerForm.is_valid():
            offerForm.save()
            return redirect('admin-view-offer')
    
    return render(request, 'service/update_offer.html', context=mydict)



@login_required(login_url='adminlogin')
def admin_request_view(request):
    return render(request,'service/admin_request.html')

@login_required(login_url='adminlogin')
def admin_view_request_view(request):
    enquiry=models.Request.objects.all().order_by('-id')
    customers=[]
    for enq in enquiry:
        customer=models.Customer.objects.get(id=enq.customer_id)
        customers.append(customer)
    return render(request,'service/admin_view_request.html',{'data':zip(customers,enquiry)})


@login_required(login_url='adminlogin')
def change_status_view(request,pk):
    adminenquiry=forms.AdminApproveRequestForm()
    if request.method=='POST':
        adminenquiry=forms.AdminApproveRequestForm(request.POST)
        if adminenquiry.is_valid():
            enquiry_x=models.Request.objects.get(id=pk)
            enquiry_x.offer=adminenquiry.cleaned_data['offer']
            enquiry_x.cost=adminenquiry.cleaned_data['cost']
            enquiry_x.status=adminenquiry.cleaned_data['status']
            enquiry_x.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-view-request')
    return render(request,'service/admin_approve_request_details.html',{'adminenquiry':adminenquiry})


@login_required(login_url='adminlogin')
def admin_delete_request_view(request,pk):
    requests=models.Request.objects.get(id=pk)
    requests.delete()
    return redirect('admin-view-request')



@login_required(login_url='adminlogin')
def admin_add_request_view(request):
    enquiry=forms.RequestForm()
    adminenquiry=forms.AdminRequestForm()
    mydict={'enquiry':enquiry,'adminenquiry':adminenquiry}
    if request.method=='POST':
        enquiry=forms.RequestForm(request.POST)
        adminenquiry=forms.AdminRequestForm(request.POST)
        if enquiry.is_valid() and adminenquiry.is_valid():
            enquiry_x=enquiry.save(commit=False)
            enquiry_x.customer=adminenquiry.cleaned_data['customer']
            enquiry_x.offer=adminenquiry.cleaned_data['offer']
            enquiry_x.cost=adminenquiry.cleaned_data['cost']
            enquiry_x.status='Approved'
            enquiry_x.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('admin-view-request')
    return render(request,'service/admin_add_request.html',context=mydict)

@login_required(login_url='adminlogin')
def admin_approve_request_view(request):
    enquiry=models.Request.objects.all().filter(status='Pending')
    return render(request,'service/admin_approve_request.html',{'enquiry':enquiry})

@login_required(login_url='adminlogin')
def approve_request_view(request,pk):
    adminenquiry=forms.AdminApproveRequestForm()
    if request.method=='POST':
        adminenquiry=forms.AdminApproveRequestForm(request.POST)
        if adminenquiry.is_valid():
            enquiry_x=models.Request.objects.get(id=pk)
            enquiry_x.offer=adminenquiry.cleaned_data['offer']
            enquiry_x.cost=adminenquiry.cleaned_data['cost']
            enquiry_x.status=adminenquiry.cleaned_data['status']
            enquiry_x.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-approve-request')
    return render(request,'service/admin_approve_request_details.html',{'adminenquiry':adminenquiry})




@login_required(login_url='adminlogin')
def admin_view_service_cost_view(request):
    enquiry=models.Request.objects.all().order_by('-id')
    customers=[]
    for enq in enquiry:
        customer=models.Customer.objects.get(id=enq.customer_id)
        customers.append(customer)
    print(customers)
    return render(request,'service/admin_view_service_cost.html',{'data':zip(customers,enquiry)})


@login_required(login_url='adminlogin')
def update_cost_view(request,pk):
    updateCostForm=forms.UpdateCostForm()
    if request.method=='POST':
        updateCostForm=forms.UpdateCostForm(request.POST)
        if updateCostForm.is_valid():
            enquiry_x=models.Request.objects.get(id=pk)
            enquiry_x.cost=updateCostForm.cleaned_data['cost']
            enquiry_x.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-view-service-cost')
    return render(request,'service/update_cost.html',{'updateCostForm':updateCostForm})


@login_required(login_url='adminlogin')
def admin_feedback_view(request):
    feedback=models.Feedback.objects.all().order_by('-id')
    return render(request,'service/admin_feedback.html',{'feedback':feedback})

#============================================================================================
# ADMIN RELATED views END
#============================================================================================


#============================================================================================
# CUSTOMER RELATED views start
#============================================================================================

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_dashboard_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    work_in_progress=models.Request.objects.all().filter(customer_id=customer.id,status='In-Progress').count()
    work_completed=models.Request.objects.all().filter(customer_id=customer.id).filter(Q(status="Repairing Done") | Q(status="Released")).count()
    new_request_made=models.Request.objects.all().filter(customer_id=customer.id).filter(Q(status="Pending") | Q(status="Approved")).count()
    #bill=models.Request.objects.all().filter(customer_id=customer.id).filter(Q(status="Repairing Done") | Q(status="Released")).aggregate(Sum('cost'))
    #print(bill)
    dict={
    'work_in_progress':work_in_progress,
    'work_completed':work_completed,
    'new_request_made':new_request_made,
    #'bill':bill['cost__sum'],
    'customer':customer,
    }
    return render(request,'service/customer_dashboard.html',context=dict)


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_request_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    return render(request,'service/customer_request.html',{'customer':customer})


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_view_request_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    enquiries=models.Request.objects.all().filter(customer_id=customer.id , status="Pending")
    return render(request,'service/customer_view_request.html',{'customer':customer,'enquiries':enquiries})


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_delete_request_view(request,pk):
    customer=models.Customer.objects.get(user_id=request.user.id)
    enquiry=models.Request.objects.get(id=pk)
    enquiry.delete()
    return redirect('customer-view-request')

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_view_approved_request_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    enquiries=models.Request.objects.all().filter(customer_id=customer.id).exclude(status='Pending')
    return render(request,'service/customer_view_approved_request.html',{'customer':customer,'enquiries':enquiries})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_view_approved_request_invoice_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    enquiries=models.Request.objects.all().filter(customer_id=customer.id).exclude(status='Pending')
    offer_names = []
    for enquiry in enquiries:
            if enquiry.offer:
                offer_name = enquiry.offer.employee_name  # Accessing the get_name property from offer model
                offer_names.append(offer_name)
    return render(request,'service/customer_view_approved_request_invoice.html',{'customer':customer,'enquiries':enquiries,'offer_names': offer_names,})



@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_add_request_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    enquiry=forms.RequestForm()
    if request.method=='POST':
        enquiry=forms.RequestForm(request.POST)
        if enquiry.is_valid():
            customer=models.Customer.objects.get(user_id=request.user.id)
            enquiry_x=enquiry.save(commit=False)
            enquiry_x.customer=customer
            enquiry_x.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('customer-dashboard')
    return render(request,'service/customer_add_request.html',{'enquiry':enquiry,'customer':customer})


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_profile_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    return render(request,'service/customer_profile.html',{'customer':customer})


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def edit_customer_profile_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    user=models.User.objects.get(id=customer.user_id)
    userForm=forms.CustomerUserForm(instance=user)
    customerForm=forms.CustomerForm(request.FILES,instance=customer)
    mydict={'userForm':userForm,'customerForm':customerForm,'customer':customer}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST,instance=user)
        customerForm=forms.CustomerForm(request.POST,instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return HttpResponseRedirect('customer-profile')
    return render(request,'service/edit_customer_profile.html',context=mydict)


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_invoice_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    enquiries=models.Request.objects.all().filter(customer_id=customer.id).exclude(status='Pending')
    return render(request,'service/customer_invoice.html',{'customer':customer,'enquiries':enquiries})


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_feedback_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    feedback=forms.FeedbackForm()
    if request.method=='POST':
        feedback=forms.FeedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()
        else:
            print("form is invalid")
        return render(request,'service/feedback_sent_by_customer.html',{'customer':customer})
    return render(request,'service/customer_feedback.html',{'feedback':feedback,'customer':customer})
#============================================================================================
# CUSTOMER RELATED views END
#============================================================================================



# for aboutus and contact
def aboutus_view(request):
    return render(request,'service/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, '/contactussuccess.html')
    return render(request, 'service/contactus.html', {'form':sub})
