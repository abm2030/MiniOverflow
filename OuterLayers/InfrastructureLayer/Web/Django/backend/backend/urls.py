"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import sys

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

sys.path.append('../../../../..')
import index
def prepare(req, questionID=None, answerID=None, commentID=None):
    return index.djangoInputs(req, questionID, answerID, commentID)


from django.urls import path

urlpatterns = [
    path('api/', prepare),
    path('api/questions', prepare),
    path('api/questions/<str:questionID>', prepare),
    path('api/questions/<str:questionID>/comments', prepare),
    path('api/questions/<str:questionID>/comments/<str:commentID>', prepare),
    path('api/questions/<str:questionID>/answers', prepare),
    path('api/questions/<str:questionID>/answers/<str:answerID>', prepare),
    path('api/questions/<str:questionID>/answers/<str:answerID>/comments', prepare),
    path('api/questions/<str:questionID>/answers/<str:answerID>/comments/<str:commentID>', prepare),
]
