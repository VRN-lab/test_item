from django.shortcuts import render


def menu_pages(request, page):
    return render(request, 'menu_item.html')
