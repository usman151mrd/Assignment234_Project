# Python
from django.urls import path
from .views import (
    # Work Experience Views
    WorkExperienceListView, WorkExperienceCreateView, WorkExperienceUpdateView,
    WorkExperienceDeleteView, WorkExperienceDetailView,
    # Education Views
    EducationListView, EducationCreateView, EducationUpdateView,
    EducationDeleteView, EducationDetailView,
    # Project Views
    ProjectListView, ProjectCreateView, ProjectUpdateView,
    ProjectDeleteView, ProjectDetailView,
    # Certification Views
    CertificationListView, CertificationCreateView, CertificationUpdateView,
    CertificationDeleteView, CertificationDetailView,
    # Award Views
    AwardListView, AwardCreateView, AwardUpdateView,
    AwardDeleteView, AwardDetailView,
    # Language Views
    LanguageListView, LanguageCreateView, LanguageUpdateView,
    LanguageDeleteView, LanguageDetailView,
    # Technical Skill Views
    TechnicalSkillListView, TechnicalSkillCreateView, TechnicalSkillUpdateView,
    TechnicalSkillDeleteView, TechnicalSkillDetailView,
    # Personal Information Views
    PersonalInformationListView, PersonalInformationCreateView, PersonalInformationUpdateView,
    PersonalInformationDeleteView, PersonalInformationDetailView,
)

app_name = 'resume_builder'

urlpatterns = [
    # Work Experience URLs
    path('work-experience/', WorkExperienceListView.as_view(), name='work_experience_list'),
    path('work-experience/add/', WorkExperienceCreateView.as_view(), name='work_experience_create'),
    path('work-experience/<int:pk>/edit/', WorkExperienceUpdateView.as_view(), name='work_experience_update'),
    path('work-experience/<int:pk>/delete/', WorkExperienceDeleteView.as_view(), name='work_experience_delete'),
    path('work-experience/<int:pk>/', WorkExperienceDetailView.as_view(), name='work_experience_detail'),
    
    # Education URLs
    path('education/', EducationListView.as_view(), name='education_list'),
    path('education/add/', EducationCreateView.as_view(), name='education_create'),
    path('education/<int:pk>/edit/', EducationUpdateView.as_view(), name='education_update'),
    path('education/<int:pk>/delete/', EducationDeleteView.as_view(), name='education_delete'),
    path('education/<int:pk>/', EducationDetailView.as_view(), name='education_detail'),
    
    # Project URLs
    path('project/', ProjectListView.as_view(), name='project_list'),
    path('project/add/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    
    # Certification URLs
    path('certification/', CertificationListView.as_view(), name='certification_list'),
    path('certification/add/', CertificationCreateView.as_view(), name='certification_create'),
    path('certification/<int:pk>/edit/', CertificationUpdateView.as_view(), name='certification_update'),
    path('certification/<int:pk>/delete/', CertificationDeleteView.as_view(), name='certification_delete'),
    path('certification/<int:pk>/', CertificationDetailView.as_view(), name='certification_detail'),
    
    # Award URLs
    path('award/', AwardListView.as_view(), name='award_list'),
    path('award/add/', AwardCreateView.as_view(), name='award_create'),
    path('award/<int:pk>/edit/', AwardUpdateView.as_view(), name='award_update'),
    path('award/<int:pk>/delete/', AwardDeleteView.as_view(), name='award_delete'),
    path('award/<int:pk>/', AwardDetailView.as_view(), name='award_detail'),
    
    # Language URLs
    path('language/', LanguageListView.as_view(), name='language_list'),
    path('language/add/', LanguageCreateView.as_view(), name='language_create'),
    path('language/<int:pk>/edit/', LanguageUpdateView.as_view(), name='language_update'),
    path('language/<int:pk>/delete/', LanguageDeleteView.as_view(), name='language_delete'),
    path('language/<int:pk>/', LanguageDetailView.as_view(), name='language_detail'),
    
    # Technical Skill URLs
    path('technical-skill/', TechnicalSkillListView.as_view(), name='technical_skill_list'),
    path('technical-skill/add/', TechnicalSkillCreateView.as_view(), name='technical_skill_create'),
    path('technical-skill/<int:pk>/edit/', TechnicalSkillUpdateView.as_view(), name='technical_skill_update'),
    path('technical-skill/<int:pk>/delete/', TechnicalSkillDeleteView.as_view(), name='technical_skill_delete'),
    path('technical-skill/<int:pk>/', TechnicalSkillDetailView.as_view(), name='technical_skill_detail'),
    # Personal Information URLs
    path('personal-information/', PersonalInformationListView.as_view(), name='personal_information_list'),
    path('personal-information/add/', PersonalInformationCreateView.as_view(), name='personal_information_create'),
    path('personal-information/<int:pk>/edit/', PersonalInformationUpdateView.as_view(), name='personal_information_update'),
    path('personal-information/<int:pk>/delete/', PersonalInformationDeleteView.as_view(), name='personal_information_delete'),
    path('personal-information/<int:pk>/', PersonalInformationDetailView.as_view(), name='personal_information_detail'),
]