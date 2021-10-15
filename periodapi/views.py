from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timedelta
from .models import FertilityWindow, PeriodData, ProcessedData


# Create your views here.

def create_cycles(request):
    if request.method == "GET":
        data = PeriodData.objects.all()
        return render(request, "form.html", {"data": data})
    else:
        last_period = request.POST.get("last_period")
        cycle_average = int(request.POST.get("cycle_average"))
        period_average = int(request.POST.get("period_average"))
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        PeriodData.objects.all().delete()
        ProcessedData.objects.all().delete()
        FertilityWindow.objects.all().delete()

        period_data = PeriodData(
            last_period = last_period,
            cycle_average = cycle_average,
            period_average = period_average,
            start_date= start_date,
            end_date= end_date
        )
        period_data.save()

        #convert strings to date objects
        last_period1 = datetime.strptime(last_period, "%Y-%m-%d").date()
        start_date1 = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date1 = datetime.strptime(end_date, "%Y-%m-%d").date()


        calculation_date = start_date1
        while not calculation_date >= end_date1: 
            period_start_date = last_period1 + timedelta(days=cycle_average)
            period_end_date = period_start_date + timedelta(days=period_average)
            ovulation_date = period_start_date + timedelta(days=cycle_average//2)
            fertility_window = []
            fertility_window.append(ovulation_date - timedelta(days=4))
            fertility_window.append(ovulation_date + timedelta(days=4))
            pre_ovulation_window = "todo"
            post_ovulation_window = "todo"

            last_period1 = period_start_date


            processed_data = ProcessedData(
                period_start_date = period_start_date,
                period_end_date = period_end_date,
                ovulation_date = ovulation_date,
                pre_ovulation_window = pre_ovulation_window,
                post_ovulation_window = post_ovulation_window,
            )
            processed_data.save()

            processed_data_object = ProcessedData.objects.get(period_start_date= period_start_date)

            for value in fertility_window:
                data_input = FertilityWindow(fertility_window=value, processed_data=processed_data_object)
                data_input.save()

            calculation_date = period_end_date

        return JsonResponse({"total_created_cycles": ProcessedData.objects.all().count()})


def cycle_event(request):
    if request.method == "GET":
        cycle_variable = str(request.GET.get("date", None))
        if not cycle_variable == None:
            events = []
            cycle_variable = datetime.strptime(cycle_variable, "%Y-%m-%d").date()
            data = ProcessedData.objects.all().prefetch_related("fertility_window")
            
            first_set = data.values(
            "ovulation_date",
            "period_start_date",
            "period_end_date",
            "pre_ovulation_window",
            "post_ovulation_window")

            second_set = data.values_list("fertility_window", flat=True)

            for main_set in first_set:
                for key, value in main_set.items():
                    if value == cycle_variable:
                        events_dict = {
                            "events": key,
                            "date": value
                        }

                        events.append(events_dict)
                        print(events)


            windows = FertilityWindow.objects.filter(id__in=second_set).values("fertility_window")

            for subset in windows:
                for name, date in subset.items():
                    if date == cycle_variable:
                        events_dict = {
                            "events": name,
                            "date": date
                        }

                        events.append(events_dict)

            print(events)
            return JsonResponse({"events_to_happen": events})