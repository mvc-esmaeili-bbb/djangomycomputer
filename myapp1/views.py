from django.shortcuts import render, HttpResponse
from myapp1.models import Product
from django.views.generic.list import ListView


class ListView1(ListView):
    queryset = Product.objects.all()
    template_name = "listview.html"

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ListView1, self).get_context_data(*args, **kwargs)
        return context


def home_page(request):
    
   # return HttpResponse(69)
    return render(request,myapp1\index1.html)
# template=loder.get_template('base1.html')
# return HttpResponse(template.render())

def contact(request):

    return HttpResponse(69)


def products_view(request):
    q = Product.objects.all()
    context = {"r": q}
    return render(request, mypage1.html, context)
