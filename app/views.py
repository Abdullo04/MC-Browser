# views.py
from django.shortcuts import render, redirect, HttpResponse
from .models import SearchHistory

def save_search(request):
    if request.method == 'POST':
        query = request.POST.get('q')

        # Сохранить запрос в базу данных
        if query:
            SearchHistory.objects.create(query=query)

        # Перенаправить на Google
        return redirect(f'https://www.google.com/search?q={query}')

    return HttpResponse("Invalid request", status=400)

def main(request):
    """
    Главная страница
    """
    return render(request, "main.html")

def history(request):
    """
    Страница истории поиска
    """
    # Получаем все закладки
    bookmarks = SearchHistory.objects.filter(is_bookmarked=True)
    # Получаем все остальные запросы
    histories = SearchHistory.objects.filter(is_bookmarked=False)

    return render(request, "history.html", {"bookmarks": bookmarks, "histories": histories})

def toggle_bookmark(request, search_id):
    """
    Изменение состояния закладки для запроса
    """
    try:
        search_history = SearchHistory.objects.get(id=search_id)
        search_history.is_bookmarked = not search_history.is_bookmarked
        search_history.save()
    except SearchHistory.DoesNotExist:
        return HttpResponse("Запись не найдена", status=404)

    return redirect('history')  # Перенаправляем на страницу истории

def delete_search(request, search_id):
    """
    Удаление конкретного запроса из истории
    """
    try:
        search_history = SearchHistory.objects.get(id=search_id)
        search_history.delete()
    except SearchHistory.DoesNotExist:
        return HttpResponse("Запись не найдена", status=404)

    return redirect('history')  # Перенаправляем на страницу истории

def clear_history(request):
    """
    Очистка всей истории
    """
    SearchHistory.objects.all().delete()
    return redirect('history')  # Перенаправляем на страницу истории
def toggle_bookmark(request, search_id):
    """
    Изменение состояния закладки для запроса
    """
    try:
        search_history = SearchHistory.objects.get(id=search_id)
        search_history.is_bookmarked = not search_history.is_bookmarked
        search_history.save()
    except SearchHistory.DoesNotExist:
        return HttpResponse("Запись не найдена", status=404)

    return redirect('history')  # Перенаправляем на страницу истории
