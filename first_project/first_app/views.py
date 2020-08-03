from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from . import forms
# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' : webpages_list}
    my_dict = {'insert_me':"Hello I am from view.py!!!"}
    return render(request, "first_app/index.html", context=date_dict)

def form_name_view(request):
    form = forms.NewWebpageForm()
    if request.method == 'POST':
        form = forms.NewWebpageForm(request.POST)

        if form.is_valid():
            # Do something code
            form.save(commit=True)
            return index(request)
        else:
            print('Error form invalid')
    return render(request, 'first_app/index.html', {'form' : form})
