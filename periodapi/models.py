from django.db import models

# Create your models here.
class PeriodData(models.Model):
    last_period = models.DateField()
    cycle_average = models.IntegerField(null=False)
    period_average = models.IntegerField(null=False)
    start_date = models.DateField()
    end_date =  models.DateField()

    def __str__(self):
        return {
        "last_period": self.last_period,
        "cycle_average": self.cycle_average,
        "period_average": self.period_average,
        "start_date": self.start_date,
        "end_date": self.end_date
        }
       


class ProcessedData(models.Model):
    period_start_date = models.DateField()
    period_end_date = models.DateField()
    ovulation_date = models.DateField()
    pre_ovulation_window = models.CharField(max_length=20)
    post_ovulation_window = models.CharField(max_length=20)


class FertilityWindow(models.Model):
    fertility_window = models.DateField()
    processed_data = models.ForeignKey(ProcessedData, on_delete=models.CASCADE, related_name="fertility_window") 
    