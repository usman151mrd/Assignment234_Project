from django.contrib import admin
from .models import (
    ResumeTemplate, Resume, ResumeSection, WorkExperience,
    TechnicalSkill, Education, Technology, Project,
    Certification, Award, Language, PersonalInformation
)

# Register your models here.
@admin.register(ResumeTemplate)
class ResumeTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'format_type', 'version', 'is_active']
    list_filter = ['format_type', 'is_active']
    search_fields = ['name', 'description']

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'template', 'visibility', 'created_at']
    list_filter = ['visibility', 'template', 'created_at']
    search_fields = ['title', 'user__email']

@admin.register(PersonalInformation)
class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'resume', 'is_visible']
    list_filter = ['is_visible', 'country']
    search_fields = ['first_name', 'last_name', 'email', 'resume__title']

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'company', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current', 'start_date']
    search_fields = ['job_title', 'company']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date']
    search_fields = ['degree', 'institution']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'role', 'start_date', 'end_date', 'is_active']
    list_filter = ['is_active', 'start_date']
    search_fields = ['title', 'role']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuer', 'issue_date', 'expiration_date']
    list_filter = ['issue_date', 'expiration_date']
    search_fields = ['name', 'issuer']

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuer', 'category', 'issue_date']
    list_filter = ['category', 'issue_date']
    search_fields = ['title', 'issuer']

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency', 'is_visible']
    list_filter = ['proficiency', 'is_visible']
    search_fields = ['name']

@admin.register(TechnicalSkill)
class TechnicalSkillAdmin(admin.ModelAdmin):
    list_display = ['technology', 'proficiency', 'years_experience', 'is_visible']
    list_filter = ['proficiency', 'is_visible']
    search_fields = ['technology__name']

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
    search_fields = ['name']

@admin.register(ResumeSection)
class ResumeSectionAdmin(admin.ModelAdmin):
    list_display = ['resume', 'section_type', 'title', 'order', 'is_visible']
    list_filter = ['section_type', 'is_visible']
    search_fields = ['title', 'resume__title']
