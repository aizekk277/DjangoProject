from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from apps.gifts.forms import ProposalForm
from apps.gifts.models import Author


def home(request):
    return render(request, 'index.html')