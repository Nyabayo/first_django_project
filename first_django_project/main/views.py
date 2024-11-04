from django.shortcuts import render, get_object_or_404, redirect
from .models import Detail

def detail_list(request):
    details = Detail.objects.all()
    return render(request, 'main/detail_list.html', {'details': details})

def detail_view(request, pk):
    detail = get_object_or_404(Detail, pk=pk)
    return render(request, 'main/detail_view.html', {'detail': detail})

def detail_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Detail.objects.create(title=title, description=description)
        return redirect('detail_list')
    return render(request, 'main/detail_form.html')

def detail_update(request, pk):
    detail = get_object_or_404(Detail, pk=pk)
    if request.method == 'POST':
        detail.title = request.POST.get('title')
        detail.description = request.POST.get('description')
        detail.save()
        return redirect('detail_list')
    return render(request, 'main/detail_form.html', {'detail': detail})

def detail_delete(request, pk):
    detail = get_object_or_404(Detail, pk=pk)
    detail.delete()
    return redirect('detail_list')
