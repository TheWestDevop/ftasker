from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
     
    path('all/user/',listUser,name="list-user"),
    path('create/user/',createUser,name="create-user"),
    path('edit/user/<int:id>/',editUser,name="edit-user"),
    path('delete/user/<int:id>/',deleteUser,name="delete-user"),
    
    path('all/profile/',listProfile,name="list-profile"),
    path('create/profile/',createProfile,name="create-profile"),
    path('edit/profile/<int:id>/',editProfile,name="edit-profile"),
    path('delete/profile/<int:id>/',deleteProfile,name="delete-profile"),
    
    path('all/usertype/',listUserType,name="list-usertype"),
    path('create/usertype/',createUserType,name="create-usertype"),
    path('edit/usertype/<int:id>/',editUserType,name="edit-usertype"),
    path('delete/usertype/<int:id>/',deleteUserType,name="delete-usertype"),
    
    path('all/category/',listCategory,name="list-category"),
    path('create/category/',createCategory,name="create-category"),
    path('edit/category/<int:id>/',editCategory,name="edit-category"),
    path('delete/category/<int:id>/',deleteCategory,name="delete-category"),
    
    path('all/sub/category/',listSubcategory,name="list-sub-category"),
    path('create/sub/category/',createSubcategory,name="create-sub-category"),
    path('edit/sub/category/<int:id>/',editSubcategory,name="edit-sub-category"),
    path('delete/sub/category/<int:id>/',deleteSubcategory,name="delete-sub-category"),
    
    path('all/country/',listCountry,name="list-country"),
    path('create/country/',createCountry,name="create-country"),
    path('edit/country/<int:id>/',editCountry,name="edit-country"),
    path('delete/country/<int:id>/',deleteCountry,name="delete-country"),
    
    path('all/state/',listState,name="list-state"),
    path('create/state/',createState,name="create-state"),
    path('edit/state/<int:id>/',editState,name="edit-state"),
    path('delete/state/<int:id>/',deleteState,name="delete-state"),
    
    path('all/city/',listCity,name="list-city"),
    path('create/city/',createCity,name="create-city"),
    path('edit/city/<int:id>/',editCity,name="edit-city"),
    path('delete/city/<int:id>/',deleteCity,name="delete-city"),
    
    path('all/job/type/',listJobType,name="list-job-type"),
    path('create/job/type/',createJobType,name="create-job-type"),
    path('edit/job/type/<int:id>/',editJobType,name="edit-job-type"),
    path('delete/job/type/<int:id>/',deleteJobType,name="delete-job-type"),
    
    path('all/job/category/',listJobCategory,name="list-job-category"),
    path('create/job/category/',createJobCategory,name="create-job-category"),
    path('edit/job/category/<int:id>/',editJobCategory,name="edit-job-category"),
    path('delete/job/category/<int:id>/',deleteJobCategory,name="delete-job-category"),
    
    path('all/job/',listJob,name="list-job"),
    path('create/job/',createJob,name="create-job"),
    path('edit/job/<int:id>/',editJob,name="edit-job"),
    path('delete/job/<int:id>/',deleteJob,name="delete-job"),
    
    path('all/job/application/',listJobApplication,name="list-job-application"),
    path('create/job/application/',createJobApplication,name="create-job-application"),
    path('edit/job/application/<int:id>/',editJobApplication,name="edit-job-application"),
    path('delete/job/application/<int:id>/',deleteJobApplication,name="delete-job-application"),
    
    path('all/notification/',listNotification,name="list-notification"),
    path('create/notification/',createNotification,name="create-notification"),
    path('edit/notification/<int:id>/',editNotification,name="edit-notification"),
    path('delete/notification/<int:id>/',deleteNotification,name="delete-notification"),
    
    path('auth/',Auth,name="auth"),
    path('login/',login,name="login"),
    path('logout/',logout,name="logout"),
    path('gen/',gen),
	
]