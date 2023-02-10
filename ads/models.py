from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    group = models.ForeignKey('Group',on_delete=models.PROTECT, null=True,blank=True)

    def __str__(self):
        return f'{self.name}{self.group}'


    objects = models.Manager


class Disciplines(models.Model):
    disciplines = models.CharField(max_length=50)
    def __str__(self):
        return self.disciplines

    objects = models.Manager

class Group(models.Model):
    group = models.CharField(max_length=50)

    def __str__(self):
        return self.group

    objects = models.Manager

class Mark(models.Model):
    name_student = models.ForeignKey('Student', on_delete=models.PROTECT,null=True,blank=True)
    mark = models.CharField(max_length=50)
    lesson = models.ForeignKey('Lesson', on_delete=models.PROTECT,null=True,blank=True)

    def __str__(self):
        return f'{self.name_student}{self.mark}'



    objects = models.Manager

class Lesson(models.Model):
    date = models.DateField()
    discipline = models.ForeignKey('Disciplines', on_delete=models.PROTECT,null=True,blank=True)
    group = models.ForeignKey('Group',on_delete=models.PROTECT, null = True, blank = True)

    def __str__(self):
        return f'{self.date}{self.discipline}{self.group}'



    objects = models.Manager
