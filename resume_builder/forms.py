from django import forms
from .models import (
    ResumeTemplate, Resume, ResumeSection, WorkExperience, TechnicalSkill,
    Education, Technology, Project, Certification, Award, Language
)
from django.forms import DateInput, SelectMultiple


class ResumeTemplateForm(forms.ModelForm):
    class Meta:
        model = ResumeTemplate
        fields = [
            'name', 'description', 'format_type', 'thumbnail',
            'config', 'version', 'is_active'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'format_type': forms.Select(attrs={'class': 'form-control'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'config': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'version': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ResumeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.resume_instance = kwargs.pop('resume_instance', None)
        super().__init__(*args, **kwargs)

        if self.user and 'resume' in self.fields:
            if self.user and hasattr(self.user, 'is_authenticated') and self.user.is_authenticated:
                self.fields['resume'].queryset = Resume.objects.filter(user=self.user)

        if self.resume_instance:
            self.fields['resume'].initial = self.resume_instance
            self.fields['resume'].widget = forms.HiddenInput()


    class Meta:
        model = Resume
        fields = [
            'title', 'slug', 'summary', 'tags', 'template',
            'language', 'visibility'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comma-separated tags'}),
            'template': forms.Select(attrs={'class': 'form-control'}),
            'language': forms.TextInput(attrs={'class': 'form-control'}),
            'visibility': forms.Select(attrs={'class': 'form-control'}),
        }


class ResumeSectionForm(forms.ModelForm):
    class Meta:
        model = ResumeSection
        fields = [
            'section_type', 'title', 'content', 'order', 'is_visible'
        ]
        widgets = {
            'section_type': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class WorkExperienceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.resume_instance = kwargs.pop('resume_instance', None)
        super().__init__(*args, **kwargs)

        if self.user and 'resume' in self.fields:
            if self.user and hasattr(self.user, 'is_authenticated') and self.user.is_authenticated:
                self.fields['resume'].queryset = Resume.objects.filter(user=self.user)

        if self.resume_instance:
            self.fields['resume'].initial = self.resume_instance
            self.fields['resume'].widget = forms.HiddenInput()


    class Meta:
        model = WorkExperience
        fields = [
            'resume',
            'job_title', 'company', 'location', 'start_date',
            'end_date', 'is_current', 'description',
            'achievements', 'technologies'
        ]
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_current': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'achievements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter achievements as a Text Format'}),
            'technologies': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TechnicalSkillForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.resume_instance = kwargs.pop('resume_instance', None)
        super().__init__(*args, **kwargs)

        if self.user and 'resume' in self.fields:
            if self.user.is_authenticated:
                self.fields['resume'].queryset = Resume.objects.filter(user=self.user)

        if self.resume_instance and 'resume' in self.fields:
            self.fields['resume'].initial = self.resume_instance
            self.fields['resume'].widget = forms.HiddenInput()


    class Meta:
        model = TechnicalSkill
        fields = [
            'resume',
            'technology', 'proficiency', 'years_experience',
            'last_used', 'project_count', 'is_visible'
        ]
        widgets = {
            'technology': forms.TextInput(attrs={'class': 'form-control'}),
            'proficiency': forms.Select(attrs={'class': 'form-control'}),
            'years_experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'last_used': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'project_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class EducationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.resume_instance = kwargs.pop('resume_instance', None)
        super().__init__(*args, **kwargs)

        if self.user and 'resume' in self.fields:
            if self.user and hasattr(self.user, 'is_authenticated') and self.user.is_authenticated:
                self.fields['resume'].queryset = Resume.objects.filter(user=self.user)


        if self.resume_instance:
            self.fields['resume'].initial = self.resume_instance
            self.fields['resume'].widget = forms.HiddenInput()


    class Meta:
        model = Education
        fields = [
            'resume',
            'degree', 'institution', 'location', 'start_date',
            'end_date', 'gpa', 'description', 'is_visible'
        ]
        widgets = {
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '4'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class TechnologyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.resume_instance = kwargs.pop('resume_instance', None)
        super().__init__(*args, **kwargs)

        if self.user and 'resume' in self.fields:
            if self.user.is_authenticated:
                self.fields['resume'].queryset = Resume.objects.filter(user=self.user)

        if self.resume_instance and 'resume' in self.fields:
            self.fields['resume'].initial = self.resume_instance
            self.fields['resume'].widget = forms.HiddenInput()

    class Meta:
        model = Technology
        fields = [
            'resume',
            'name', 'category', 'icon'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., fa-python'}),
        }


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.resume_instance = kwargs.pop('resume_instance', None)
        super().__init__(*args, **kwargs)

        if self.user and 'resume' in self.fields:
            if self.user and hasattr(self.user, 'is_authenticated') and self.user.is_authenticated:
                self.fields['resume'].queryset = Resume.objects.filter(user=self.user)

        if self.resume_instance:
            self.fields['resume'].initial = self.resume_instance
            self.fields['resume'].widget = forms.HiddenInput()

    class Meta:
        model = Project
        fields = [
            'resume',
            'title', 'role', 'start_date', 'end_date',
            'description', 'technologies', 'outcomes', 'url', 'is_active'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'technologies': forms.TextInput(attrs={'class': 'form-control'}),
            'outcomes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter outcomes as a Text Format'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CertificationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.resume_instance = kwargs.pop('resume_instance', None)
        super().__init__(*args, **kwargs)

        if self.user and 'resume' in self.fields:
            if self.user.is_authenticated:
                self.fields['resume'].queryset = Resume.objects.filter(user=self.user)

        if self.resume_instance and 'resume' in self.fields:
            self.fields['resume'].initial = self.resume_instance
            self.fields['resume'].widget = forms.HiddenInput()

    class Meta:
        model = Certification
        fields = [
            'resume',
            'name', 'issuer', 'issue_date', 'expiration_date',
            'credential_id', 'verification_url', 'skills'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'issuer': forms.TextInput(attrs={'class': 'form-control'}),
            'issue_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expiration_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'credential_id': forms.TextInput(attrs={'class': 'form-control'}),
            'verification_url': forms.URLInput(attrs={'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AwardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.resume_instance = kwargs.pop('resume_instance', None)
        super().__init__(*args, **kwargs)

        if self.user and 'resume' in self.fields:
            if self.user.is_authenticated:
                self.fields['resume'].queryset = Resume.objects.filter(user=self.user)

        if self.resume_instance and 'resume' in self.fields:
            self.fields['resume'].initial = self.resume_instance
            self.fields['resume'].widget = forms.HiddenInput()

    class Meta:
        model = Award
        fields = [
            'resume',
            'title', 'issuer', 'issue_date', 'category',
            'description', 'impact_metrics', 'is_visible'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'issuer': forms.TextInput(attrs={'class': 'form-control'}),
            'issue_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'impact_metrics': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter metrics as a Text Format'}),
            'is_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class LanguageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.resume_instance = kwargs.pop('resume_instance', None)
        super().__init__(*args, **kwargs)

        if self.user and 'resume' in self.fields:
            if self.user.is_authenticated:
                self.fields['resume'].queryset = Resume.objects.filter(user=self.user)

        if self.resume_instance and 'resume' in self.fields:
            self.fields['resume'].initial = self.resume_instance
            self.fields['resume'].widget = forms.HiddenInput()

    class Meta:
        model = Language
        fields = [
            'resume',
            'name', 'proficiency', 'certification', 'is_visible'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'proficiency': forms.Select(attrs={'class': 'form-control'}),
            'certification': forms.TextInput(attrs={'class': 'form-control'}),
            'is_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class EmptyForm(forms.Form):
    pass