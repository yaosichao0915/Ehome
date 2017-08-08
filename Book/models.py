from django.db import models

# Create your models here.
class Statement(models.Model):
    category=models.CharField(max_length=200)
    summary=models.CharField(max_length=200)
    issued_date = models.DateField()
    balance_type = models.CharField(max_length=200)
    balance = models.DecimalField(max_digits=10,decimal_places=2)   
    def __str__(self):
        return '%s,%s,%.2f'%(self.summary,self.balance_type,self.balance)
        