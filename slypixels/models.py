from django.db import models
import datetime as dt

class Location(models.Model):
    location = models.CharField(max_length = 30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, id, location, update):
        updated = cls.objects.filter(id = id).update(location = update)
        return updated

    def __str__(self):
        return self.location



class Category(models.Model):
    image_category = models.CharField(max_length = 30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, category, update):
        updated = cls.objects.filter(id = id).update(category = update)
        return updated

    def __str__(self):
        return self.image_category



class Image(models.Model):
    name = models.CharField(max_length = 30, blank = True)
    image = models.ImageField(upload_to = 'pics/', default = 'image')
    image_url = models.TextField(blank = True)
    category = models.ForeignKey(Category)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add = True)
    location = models.ForeignKey(Location)


    