import json

from django.shortcuts import render
from django.http.response import HttpResponse
from web.models import Subscribe,Customer,Feature,VideoBlog,Testimonial,MarketingFeature,Product,Blog


def home(request):
    customers = Customer.objects.all()
    features = Feature.objects.all()
    videoBlog = VideoBlog.objects.all()
    testimonial = Testimonial.objects.filter(is_featured=True)  
    marketing_features = MarketingFeature.objects.all() 
    product = Product.objects.all()
    blog = Blog.objects.all() 
    context = {
        "customers": customers,
        "features": features,
        "videoBlog": videoBlog,
        "testimonial": testimonial,
        "marketing_features": marketing_features,
        "product": product,
        "blog": blog
    }
    
    
    return render(request,'index.html',context=context)


def subscribe(request):
    email = request.POST.get("email")
    if not Subscribe.objects.filter(email=email).exists():
        Subscribe.objects.create(
        email = email
        )
        response_data={
            "status": "success",
            "title": "Successfully Registered",
            "message":"you subscribed to our newsletter successfully."
        }
    else:
         response_data={
            "status": "error",
            "title": "you are already subscribed",
            "message":"you are already a member. No need to register again."
        }


    return HttpResponse(json.dumps(response_data),content_type ="application/javascript")



