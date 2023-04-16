from django.shortcuts import render
from django.http import HttpResponse, Http404
import pandas as pd
import numpy as np


# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

df=pd.read_csv('static/prediction_result_voting_classifier.csv')
df2 = df.assign(ColumnA = df.HomeTeam.astype(str) + '- ' + df.AwayTeam.astype(str) + ' :  ' + df.label.astype(str) + ' with  ' + df.probablity.astype(str) + ' probablitiy')

texts = []
for i in range(len(df2)):
    texts.append(df2.ColumnA[i])

def section(request, num):
    if 1 <= num <= 10:
        return HttpResponse(texts[num-1])
    else:
        raise Http404("No such section")