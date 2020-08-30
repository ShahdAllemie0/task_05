from django.shortcuts import render
from .models import Restaurant

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        "restaurants":Restaurant.objects.all(),
    }
    return render(request, 'list.html', context)


def restaurant_detail(request, restaurant_id):
    context = {
        "restaurant": Restaurant.objects.get(id=restaurant_id),
    }
    return render(request, 'detail.html', context)
# The list view function has been partially written for you. Provide the dictionary key restaurants with the list of all Restaurant objects.
# Render the list of Restaurant objects to the HTML file provided. In the list view, you'll want to display minimum data (restaurant name and description).
# The detail view function has been partially written for you. Provide the dictionary key restaurant with the specific Restaurant object using the id.
# Render the Restaurant object to the HTML file provided. In the detail view, you'll want to display all data.
# Adjust the URLs so that they'll correctly call the views.
# Using the URL tag, hyperlink the restaurant objects in the list page, so that when a user clicks on a restaurant it takes the user to the detail page.
