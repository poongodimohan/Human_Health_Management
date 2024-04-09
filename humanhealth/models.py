from django.db import models

# Create your models here.
class Food(models.Model):
    Date=models.DateField()
    Breakfasttime=models.TimeField()
    BreakfastLocation=models.CharField(max_length=30)
    LunchTime= models.TimeField()
    LunchLocation=models.CharField(max_length=30)
    DinnerTime=models.TimeField()
    DinnerLocation=models.CharField(max_length=30)


class Meta:
    db_table = "Food"

def __str__ (self):
    return f"{self.Date}-{self.Breakfasttime}-{self.BreakfastLocation}-{self.LunchTime}-{self.LunchLocation}-{self.DinnerTime}-{self.DinnerLocation}"


class Sleep(models.Model):
    Date=models.DateField()
    Starttime=models.TimeField()
    Endtime=models.TimeField()

class Meta:
    db_table = "Sleep"

def __str__(self):
    return f"{self.Date}-{self.Starttime}-{self.Endtime}"

class Water(models.Model):
    Date=models.DateField()
    Quantity=models.BigIntegerField


class Meta:
    db_table = "Water"
def __str__(self):
    return f"{self.Date}={self.Quantity}"

class Walk(models.Model):
    Date = models.DateField()
    Distance = models.BigIntegerField()

    class Meta:
        db_table = "Walk"

    def __str__(self):
        return f"{self.Date}-{self.Distance}"
    

class Mobile(models.Model):
    Date = models.DateField()
    Hours = models.BigIntegerField()
    Minitue =models.BigIntegerField()

    class Meta:
        db_table = "Mobile"

    def __str__(self):
        return f"{self.Date}-{self.Hours}-{self.Minitue}"
    

class Location(models.Model):
    Create_food_location = models.BigIntegerField()

    class Meta:
        db_table = "Location"

    def __str__(self):
        return f"{self.Create_food_location}"