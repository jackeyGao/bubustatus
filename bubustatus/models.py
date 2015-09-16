from django.db import models

# Create your models here.

class Label(models.Model):
    name = models.CharField(max_length=45, primary_key=True)
    step_count = models.IntegerField()
    desc = models.TextField()

    def __unicode__(self):
        return unicode(self.name)

    def __str__(self):
        return self.name



class Step(models.Model):
    label = models.ForeignKey(Label)
    name = models.CharField(max_length=45)
    desc = models.CharField(max_length=200)
    status = models.CharField(max_length=45)
    insert = models.DateTimeField(auto_now_add=True)
    confirm_time = models.DateTimeField(auto_now=True)
    is_confirm = models.BooleanField()

#    class Meta:
#        unique_together = ("label", "name", "status")

    def order(self):
        queryset = Step.objects.filter(label=self.label, 
                name=self.name, status=self.status).order_by('insert')
        steps = [ step for step in queryset ]
        return steps.index(self) + 1

    def complete_number(self):
        queryset = Step.objects.filter(label=self.label,
                name=self.name)

        order = (len(queryset) + self.label.step_count - 1) / self.label.step_count
        return order * self.label.step_count

    def label_name(self):
        return self.label.name

    def __unicode__(self):
        return unicode(self.name)

    def __str__(self):
        return self.name


