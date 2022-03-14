from django.contrib import admin
from django.urls import path
from interview.views import createInterview, showInterviews, uploadResume

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', createInterview),
    path('create', createInterview),
    path('interviews', showInterviews),
    path('interviews/<slug:edit_id>', showInterviews),
    path('upload', uploadResume),
    path('upload/<slug:upload_id>', uploadResume),
]

