from django.contrib import admin
from reviews.models import Review, ReviewLike

# Register your models here.
admin.site.register(Review)
admin.site.register(ReviewLike)