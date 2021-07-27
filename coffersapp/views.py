from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import BlogModel

# Create your views here.
class IndexView(TemplateView):
    template_name ="index.html"

class BeansView(TemplateView):
    template_name ="beans.html"

class EquipmentView(TemplateView):
    template_name ="equipment.html"

class WaterView(TemplateView):
    template_name ="water.html"

class ArrangeView(TemplateView):
    template_name ="arrange.html"

class BlogList(ListView):
    template_name = "list.html"
    model = BlogModel

class BlogDetail(DetailView):
    template_name = "detail.html"
    model = BlogModel

class SignupView(TemplateView):
    template_name ="signup.html"

#未開設ショッピングページ関係
# class Beans_BuyView(TemplateView):
#     template_name ="beans_buy.html"

#     def get_context_data(self, **kwargs):
#         # ゲットパラメーター
#         context = super().get_context_data(**kwargs)
#         q = self.request.GET.get('q')
#         context['q'] = q
#         beanid = self.request.GET.get('beanid')
#         context['beanid'] = beanid
#         # 自動フォーム入力
#         return context

# class Equipment_BuyView(TemplateView):
#     template_name ="equipment_buy.html"

# class Water_BuyView(TemplateView):
#     template_name ="water_buy.html"