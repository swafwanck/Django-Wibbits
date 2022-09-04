from django.db import models

content_type = (
    ("blog post","Blog post"),
    ("webinar","Webinar"),
    ("report","Report"),
)


class Subscribe(models.Model):
    email = models.EmailField(unique=True, primary_key =True)

    def __str__(self):
        return self.email



class Customer(models.Model):
    image = models.FileField(upload_to="customer/")


class Feature(models.Model):
    image = models.ImageField(upload_to="feature/")
    icon = models.FileField(upload_to="feature/")
    icon_background = models.CharField(max_length=128)
    title = models.CharField(max_length=255)
    description = models.TextField()
    testimonial_description = models.TextField()
    testimonial_author = models.CharField(max_length=128)
    designation = models.CharField(max_length=255)
    testimonial_logo = models.FileField(upload_to="feature/")


    def __str__(self):
        return self.title


class VideoBlog(models.Model):
    image = models.ImageField(upload_to="videoBlog/")
    title = models.CharField(max_length=255)
    logo = models.FileField(upload_to="videoBlog/logo/")


    def __str__(self):
        return self.title



class Testimonial(models.Model):
    image = models.ImageField(upload_to="testimonial/")
    logo = models.FileField(upload_to="testimonial/logo", blank=True,null=True)
    description = models.TextField()
    name = models.CharField(max_length=128)
    designation = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    is_featured = models.BooleanField()

    
    def __str__(self):
        return self.name


class MarketingFeature(models.Model):
    image = models.FileField(upload_to="makerting/")
    title = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.FileField(upload_to="product/images/")
    title = models.CharField(max_length = 255)
    description = models.TextField()
    logo = models.FileField(upload_to="product/logo/")
    background = models.CharField(max_length = 128)
    def __str__(self):
        return self.title


class Blog(models.Model):
    image = models.ImageField(upload_to="Blog/images/")
    title = models.CharField(max_length = 255)
    content_type = models.TextField(choices=content_type) 
    text = models.CharField(max_length = 255)

    
    def __str__(self):
        return self.title  




