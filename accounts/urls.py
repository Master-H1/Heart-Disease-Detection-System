from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    # User role dashboard
    path('dashboard/', views.DashboardView, name='dashboard'),
    # Consultant dashboard
    path('add-patient/', views.AddPatientView, name='addpatient'),
    path('patient-list-view/', views.PatientsView, name='viewpatients'),
    path('edit-patient/<int:id>/', views.EditPatientView, name='editpatient'),
    path('consult-to-doctor/<int:id>/',
         views.ConsultToDoctorView, name='consdoctor'),
    path('view-consult-to-doctor/',
         views.viewConsultToDoctorView, name='viewconsdoctor'),
    path('delete-consult-record/<int:id>/',
         views.DeleteConsultRecord, name='delrecord'),

    # Laboratory Dashboard
    path('heart-lab-medical-hist/',
         views.HeartLabMedicalHistView, name='heartlabresult'),
    path('patient-record-from-doctor/',
         views.RecordsFromDoctorView, name='fromdoctor'),
    path('add-patient-heart-lab-exam-results/<int:id>',
         views.AddHeartLabResults, name='addheartexam'),
    path('edit-patient-heart-lab-exam-results/<int:id>',
         views.EditHeartLabResults, name='editheartexam'),

    # Heart Deapartment
    path('final-results-record/', views.FinalTestResultsView, name='finalresults'),
    path('records-from-consult/', views.RecordsFromConsultView, name='fromconsult'),
    path('heart-records-sent-to-lab/<int:id>/',
         views.HeartSendToLabTest, name='heartlab'),
    path('heart-delete-from-consult-record/<int:id>/',
         views.HeartDeleteConsultRecord, name='heartdelrecord'),
    path('view-heart-records-sent-to-lab/',
         views.ViewHeartSendToLabTest, name='viewheartlab'),
    path('predict-heart-disease/<int:id>/',
         views.HeartPredictView, name='heartpredict'),
    # Turn html patient result to pfd
    path('print_patient_result_pdf/<int:id>/',
         views.PrintPatientResult, name='print_result'),



]
