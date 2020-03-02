from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import URLForm
from .models import CuttedUrl


def index(request):
    form = URLForm()
    urls = CuttedUrl.objects.all()
    if request.method == 'GET':
        return render(request, 'index.html', context={'form': form, 'urls': urls})
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            real_url = form.cleaned_data.get('url')
            if form.cleaned_data.get('code'):
                new_cut = CuttedUrl.objects.create(real_url=real_url, code=form.cleaned_data.get('code'))
                return redirect(reverse('index_url'))
            else:
                new_cut = CuttedUrl.objects.create(real_url=real_url)

            return redirect(reverse('index_url'))
        else:
            return render(request, 'index.html', context={'form': form, 'urls': urls})


def redirect_view(request, code):
    if request.method == 'GET':
        current_url = CuttedUrl.objects.get(code=code)
        current_url.clicks += 1
        current_url.save()
        redirect_url = current_url.real_url
        return redirect(redirect_url)
