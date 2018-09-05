from django.shortcuts import render
from modelapp.models import  User
# Create your views here.

#Functunal Views

#view for index html page
def index(request):
    return render(request,'apptwo/index.html')


#class based view
def user(request):

        user_list=User.objects.order_by('first_name')
        user_dict={'users':user_list}
        return render(request,'apptwo/users.html',context=user_dict)

    

