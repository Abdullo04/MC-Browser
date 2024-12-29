from django.shortcuts import render, redirect, HttpResponse
from .models import SearchHistory

def save_search(request):
    if request.method == 'POST':
        query = request.POST.get('q')

        # Save the query to the database
        if query:
            SearchHistory.objects.create(query=query)

        # Redirect to Google search
        return redirect(f'https://www.google.com/search?q={query}')

    return HttpResponse("Invalid request", status=400)


def main(request):
    """
    Main page
    :param request: HttpRequest
    :return: HttpResponse
    """
    return render(request, "main.html")


def search(request):
    """
    Search file
    :param request:
    :return:
    """
    return render(request, "search.html")


def history(request):
    """
    History page
    :param request:
    :return:
    """
    histories = SearchHistory.objects.all()
    print(histories)
    return render(request, "history.html", {"histories": histories})
