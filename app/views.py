from django.shortcuts import render, redirect


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
