from django.shortcuts import render 


def home(request):

    return render(request,'home.html')

# def about_us(request):

#     return render(request,'about_us.html')

# def show_item(request):
#     return render(request,'show_item.html')