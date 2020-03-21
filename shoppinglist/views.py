# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.conf import settings

from .forms import ShoppingForm, SortForm
from .models import Shopping

import datetime

# Create your views here.

@login_required
def index(request):
    return redirect('shoppinglist:list',sort='buy_or_not')

@login_required
def sort(request):
    if request.method == "POST":
        s = request.POST.get('key')
        return redirect('shoppinglist:list', sort=s)
    else:
        return redirect('shoppinglist:list', sort='buy_or_not')

def buy(request,pk):
    shopping = Shopping.objects.get(id=pk)
    shopping.buy_or_not = True
    shopping.date = datetime.date.today()
    shopping.save()
    return redirect('shoppinglist:index')

def must_buy(request,pk):
    shopping = Shopping.objects.get(id=pk)
    shopping.buy_or_not = False
    shopping.save()
    return redirect('shoppinglist:index')

@method_decorator(login_required, name='dispatch')
class ShoppingListView(ListView):
    model = Shopping

    def get_queryset(self):
        key = self.kwargs['sort']
        shoppings = Shopping.objects.filter(user=self.request.user).order_by(key)
        for shopping in shoppings:
            if shopping.date:
                shopping.days = (datetime.date.today() - shopping.date).days
                shopping.save()
        return shoppings

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)  #テンプレートに渡すコンテキストに 「user_count」 という変数を追加
            context['form'] = SortForm
            return context

@method_decorator(login_required, name='dispatch')
class ShoppingCreateView(CreateView):
    form_class = ShoppingForm
    template_name = 'shoppinglist/shopping_create.html'
    success_url = reverse_lazy('shoppinglist:index')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(ShoppingCreateView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class ShoppingUpdateView(UpdateView):
    model = Shopping
    form_class = ShoppingForm
    success_url = reverse_lazy('shoppinglist:index')

@method_decorator(login_required, name='dispatch')
class ShoppingDeleteView(DeleteView):
    model = Shopping
    success_url = reverse_lazy('shoppinglist:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meta_fields = Shopping._meta.get_fields()
        dic = {}
        for field in meta_fields:
            if field.name != 'id' and field.name != 'user':
                exec('dic[field.verbose_name]=context["object"].{}'.format(field.name))
        context['info'] = dic
        return context