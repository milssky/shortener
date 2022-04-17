from django.shortcuts import get_object_or_404, HttpResponsePermanentRedirect ,render

from .forms import UrlsForm
from .logic import get_short_urlcode, make_short_url
from .models import Urls


def index(request):
    if not request.method == 'POST':
        form = UrlsForm()
        return render(request, 'shortener/index.html', {
            'form': form
        })

    form = UrlsForm(request.POST)
    if not form.is_valid():
        return render(request, 'shortener/index.html', {
            'form': form
        })
    
    short_url = form.save(commit=False)
    short_url.short_id = get_short_urlcode()
    short_url.save()
    return render(request, 'shortener/index.html', {
        'form':form,
        'short_url': make_short_url(short_url.short_id)
    })

def redirect_to_http_url(request, slug):
    url = get_object_or_404(Urls, short_id=slug)
    url.nums_of_visits += 1
    url.save()
    return HttpResponsePermanentRedirect(url.http_url)
