# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.detail import DetailView
from records.models import Post
from django.views.generic.list import ListView

class PostListView(ListView):	
	
	model = Post
# Create your views here.

class PostDetailView(DetailView):

	model = Post