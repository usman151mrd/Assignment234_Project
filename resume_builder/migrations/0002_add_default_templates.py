from django.db import migrations

def add_default_templates(apps, schema_editor):
    ResumeTemplate = apps.get_model('resume_builder', 'ResumeTemplate')
    templates = [
        {'name': 'Classic', 'format_type': 'CLASSIC', 'description': 'A classic professional template.'},
        {'name': 'Modern', 'format_type': 'MODERN', 'description': 'A modern, clean template.'},
        {'name': 'Creative', 'format_type': 'CREATIVE', 'description': 'A creative, stylish template.'},
        {'name': 'Technical', 'format_type': 'TECHNICAL', 'description': 'A technical, detail-oriented template.'},
        {'name': 'Elegant', 'format_type': 'CLASSIC', 'description': 'An elegant, refined template.'},
    ]
    for tpl in templates:
        ResumeTemplate.objects.get_or_create(name=tpl['name'], defaults=tpl)

class Migration(migrations.Migration):
    dependencies = [
        ('resume_builder', '0002_personalinformation'),
    ]
    operations = [
        migrations.RunPython(add_default_templates),
    ] 