from django.db import models

class Student(models.Model):
    # invoice = models.ForeignKey(Invoice, related_name = 'files', on_delete = models.CASCADE)
    # file = models.FileField(upload_to = 'img/')
    
    # def delete(self, *args, **kwargs):
    #     self.file.delete()
    #     return super(File, self).delete(*args, **kwargs)
    
    diploma = models.FileField(upload_to='img/', blank=True, null=True)

    # def delete(self):
    #         images = ProductImage.objects.filter(product=self)
    #         for image in images:
    #             image.delete()
    #         self.thumbnail.delete()
    #         super(Product, self).delete()

# class MyModel(models.Model):
#     ''' for example this is your model '''
#     name = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='/img/')

# # this is your view
# mm = MyModel.objects.get(pk=111)
# # print(mm.image)
# mm.image.close() # add this line
# mm.image.delete()