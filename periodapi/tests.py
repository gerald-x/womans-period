from django.test import TestCase
from .models import PeriodData

# Create your tests here.
class ModelTest(TestCase):

    def test_create_cycle(self):
        period_data = PeriodData.objects.create(
            last_period = "2020-06-20",
            cycle_average = 25,
            period_average = 5,
            start_date = "2020-07-25",
            end_date = "2021-07-25"
        )
        period_data.save()

        self.assertEqual(str(period_data.last_period), "2020-06-20")


