from django.contrib import admin
from .models.model_medical_record import MedicalRecord
from .models.model_static_data import StaticData
from .models.model_medicines import Medicine
from .models.model_specific_exams import SpecificExam
from .models.model_complaint import Complaint
from .models.model_exams import Exam

admin.site.register(MedicalRecord)
admin.site.register(StaticData)
admin.site.register(Medicine)
admin.site.register(SpecificExam)
admin.site.register(Complaint)
admin.site.register(Exam)
