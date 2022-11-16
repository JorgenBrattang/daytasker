from django.shortcuts import render, redirect
from .models import Category
from .forms import AddCategories


def get_category_list(request):
    # categories = AddCategories.objects.all()
    # context = {
    #     'categories': categories
    # }
    # return render(request, 'category/category_list.html', context)
    return render(request, 'category/category_list.html')


# def add_task_form(request, id=0):
#     if request.method == 'POST':
#         if id == 0:
#             form = AddTask(request.POST)
#         else:
#             task = Task.objects.get(pk=id)
#             form = AddTask(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#         return redirect('/tasks/')
#     else:
#         if id == 0:
#             form = AddTask()
#         else:
#             task = Task.objects.get(pk=id)
#             form = AddTask(instance=task)
#         context = {
#             'form': form
#         }
#         return render(request, 'tasks/add_task_form.html', context)


# def delete_task(request, id):
#     task = Task.objects.get(pk=id)
#     task.delete()
#     return redirect('/tasks/')
