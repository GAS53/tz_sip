from django.urls import path, include

from callapp.views import RunCallingAPI, GetAllProjects, UploadFileView, CreateProjectAPI, AddPhonesAPI, CheckProjectAPI


app_name = 'callapp'


urlpatterns = [
    path("v1/new_project/", CreateProjectAPI.as_view()),
    path("v1/all_projects/", GetAllProjects.as_view()),
    path("v1/check_project/<int:pk>", CheckProjectAPI.as_view()),
    path("v1/upload_file/", UploadFileView.as_view()),
    path("v1/add_phones/", AddPhonesAPI.as_view()),
    
    path("v1/run_project/<int:pk>", RunCallingAPI.as_view()),
]