from pyexpat import model
from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import (
    LoginView, LogoutView,
)
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .mixins import OnlyYouMixin
from .forms import (
    LoginForm, UserCreateForm, UserUpdateForm,UserPostForm
)
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView,
)
from django.views.generic import ListView, CreateView, FormView
from .models import PostModel,UserPostModel
from model.score import ScoreGenerator

UserModel = get_user_model()
class UserCreate(CreateView):
    form_class = UserCreateForm
    template_name = 'cms/signup.html'
    success_url = reverse_lazy('cms:top')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

class TopView(TemplateView):
    template_name = 'cms/top.html'

class Logout(LogoutView):
    pass

class Login(LoginView):
    form_class = LoginForm
    template_name = 'cms/login.html'

class UserUpdate(OnlyYouMixin, UpdateView):
    model = UserModel
    form_class = UserUpdateForm
    template_name = 'cms/user_update.html'

    def get_success_url(self):
        return resolve_url('cms:user_detail', pk=self.kwargs['pk'])

class UserDetail(DetailView):
    model = UserModel
    template_name = 'cms/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

class UserList(ListView):
    model = UserModel
    template_name = 'cms/user_list.html'

class UserDelete(OnlyYouMixin, DeleteView):
    model = UserModel
    template_name = 'cms/user_delete.html'
    success_url = reverse_lazy('cms:top')

class Post(CreateView):
    model = PostModel
    template_name = 'cms/post.html'
    fields = ('no_one', 'no_two')
    success_url = reverse_lazy('cms:top')

    def post(self, request, *args, **kwargs):
        #スコアパラメータの計算
        score_one = ScoreGenerator(request.POST['no_one']).calculate_score()
        score_two = ScoreGenerator(request.POST['no_two']).calculate_score()
        score_values = []

        #2つの文章のスコアを計算し，平均をとる
        for one, two in zip(score_one.values(), score_two.values()):
            score = (one + two) / 2
            score_values.append(score)

        params = {}
        labels = ['negative', 'mount', 'ill']
        for label, value in zip(labels, score_values):
            params[label] = value

        return render(request, 'cms/result.html', params)

class UserPost(OnlyYouMixin, UpdateView):
    model = UserModel
    form_class = UserPostForm
    template_name = 'cms/user_post.html'

    def get_success_url(self):
        return resolve_url('cms:user_detail', pk=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        #スコアパラメータの計算
        score_one = ScoreGenerator(request.POST['no_one']).calculate_score()
        score_two = ScoreGenerator(request.POST['no_two']).calculate_score()
        score_values = []

        #2つの文章のスコアを計算し，平均をとる
        for one, two in zip(score_one.values(), score_two.values()):
            score = (one + two) / 2
            score_values.append(score)

        params = {}
        labels = ['negative', 'mount', 'ill']
        for label, value in zip(labels, score_values):
            params[label] = value

        return render(request, 'cms/result.html', params)


class UserPostView(OnlyYouMixin,CreateView):
    model = UserPostModel
    template_name = 'cms/user_post.html'
    fields = ('no_one', 'no_two')
    success_url = reverse_lazy('cms:top')

    def post(self, request, *args, **kwargs):
        #スコアパラメータの計算
        score_one = ScoreGenerator(request.POST['no_one']).calculate_score()
        score_two = ScoreGenerator(request.POST['no_two']).calculate_score()
        score_values = []

        #2つの文章のスコアを計算し，平均をとる
        for one, two in zip(score_one.values(), score_two.values()):
            score = (one + two) / 2
            score_values.append(score)

        params = {}
        labels = ['negative', 'mount', 'ill']
        for label, value in zip(labels, score_values):
            params[label] = value

        return render(request, 'cms/result.html', params)