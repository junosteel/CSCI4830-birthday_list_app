from django.shortcuts import render, get_object_or_404, redirect
from .models import Birthday
from .forms import BirthdayForm

def birthday_list(request):
    birthdays = Birthday.objects.order_by('birth_date')
    priority_filter = request.GET.get('priority')
    if priority_filter:
        birthdays = birthdays.filter(priority=priority_filter)
    return render(request, 'birthdays/birthday_list.html', {'birthdays': birthdays})

def add_birthday(request):
    if request.method == "POST":
        form = BirthdayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('birthday_list')
    else:
        form = BirthdayForm()
    return render(request, 'birthdays/birthday_form.html', {'form': form})

def edit_birthday(request, pk):
    birthday = get_object_or_404(Birthday, pk=pk)
    if request.method == "POST":
        form = BirthdayForm(request.POST, instance=birthday)
        if form.is_valid():
            form.save()
            return redirect('birthday_list')
    else:
        form = BirthdayForm(instance=birthday)
    return render(request, 'birthdays/birthday_form.html', {'form': form})
