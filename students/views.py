

# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Student
import csv
import openpyxl
from io import BytesIO

def upload_students(request):
    if request.method == 'POST' and request.FILES.get('file'):
        csv_file = request.FILES['file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            Student.objects.create(
                name=row['name'],
                usn=row['usn'],
                subject=row['subject'],
                booklet_no=row['booklet_no']
            )
        return JsonResponse({'message': 'Students imported successfully'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def generate_bform(request):
    students = Student.objects.all().order_by('subject', 'id')
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "B-Form"

    # Headers
    sheet.append(["Si No", "Name", "USN", "Booklet No", "Signature", "Room"])

    # Grouping students into classrooms
    room_number = 1
    for index, student in enumerate(students, start=1):
        if (index - 1) % 40 == 0:
            room_number += 1
        sheet.append([
            index,
            student.name,
            student.usn,
            student.booklet_no,
            "",
            f"Room {room_number}"
        ])

    # Response
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=B-Form.xlsx'
    workbook.save(response)
    return response
