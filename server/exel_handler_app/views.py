import pandas, pdfkit
import datetime

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from .models import FileUploadModel, Group, Subject, DataTable
from .serializers import DataSerializer

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)


# Create your views here.
# class FileUploadView(APIView):
#     parser_classes = (FileUploadParser,)

#     def put(self, request, filename=None, format=None):
#         file_obj = request.FILES['file']
#         print('hello there')
#         # do some stuff with uploaded file
#         return Response(status=204)


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def put(self, request, format=None):
        now = datetime.datetime.now().strftime('%d%m%y%H%M%S')
        file_obj = request.data['file']

        df = pandas.read_excel(file_obj, encoding='UTF-8', sheet_name='учет')
        cols = ['Дата', 'Курс', 'Группа', 'Название учебной дисциплины', 'Лекции',
                'Практические (сем.) занятия', 'Лабораторные занятия',
                'Модульный контроль', 'Семестр (консультации)',
                'Экзамен (консультации)', 'Зачеты', 'Экзамены', 'Курсовые работы',
                'ВКР бакалавров', 'ВКР специалистов', 'ВКР магистров',
                'Руководство практикой', 'Госэкзамены', 'Рецензирование ВКР',
                'Защита ВКР', 'Руководство аспирантами', 'Другие виды учеб. нагрузки',
                'Количество часов всего', 'Подпись']
        if not df.columns.isin(cols).all():
            filename = now + ''.join(['_error.' if f == '.' else f for f in file_obj.name])
            instance = FileUploadModel(owner=request.user)
            instance.datafile.save(filename, file_obj)
            instance.save()
        else:
            term = 1
            base = None
            for index, row in df.iterrows():
                if pandas.isnull(row['Дата']):
                    continue
                data_instance = DataTable()
                data_instance.added_by = request.user
                data_instance.term = term
                if 'ВТОРОЙ СЕМЕСТР' in str(row['Дата']):
                    term = 2
                    continue
                if '(БЮДЖЕТ)' in str(row['Дата']):
                    base = 'B'
                    continue
                if '(ДОГОВОР)' in str(row['Дата']):
                    base = 'C'
                    continue
                if 'итог' in str(row['Дата']).lower():
                    data_instance.subject, _ = \
                        Subject.objects.get_or_create(
                            subject_name=row['Дата'].upper())  # хранить поля итого в названии предмета
                else:
                    data_instance.date = row['Дата']
                    data_instance.course = row['Курс']
                    data_instance.group, _ = Group.objects.get_or_create(group_name=row['Группа'])
                    data_instance.base = base
                    data_instance.subject, _ = \
                        Subject.objects.get_or_create(subject_name=row['Название учебной дисциплины'])
                if not pandas.isnull(row['Лекции']):
                    data_instance.lectures = row['Лекции']
                if not pandas.isnull(row['Практические (сем.) занятия']):
                    data_instance.practise_less = row['Практические (сем.) занятия']
                if not pandas.isnull(row['Лабораторные занятия']):
                    data_instance.lab_works = row['Лабораторные занятия']
                if not pandas.isnull(row['Модульный контроль']):
                    data_instance.modular_control = row['Модульный контроль']
                if not pandas.isnull(row['Семестр (консультации)']):
                    data_instance.term_consultation = row['Семестр (консультации)']
                if not pandas.isnull(row['Экзамен (консультации)']):
                    data_instance.exam_consultation = row['Экзамен (консультации)']
                if not pandas.isnull(row['Зачеты']):
                    data_instance.credit = row['Зачеты']
                if not pandas.isnull(row['Экзамены']):
                    data_instance.exam = row['Экзамены']
                if not pandas.isnull(row['Курсовые работы']):
                    data_instance.course_work = row['Курсовые работы']
                if not pandas.isnull(row['ВКР бакалавров']):
                    data_instance.vkr_bac = row['ВКР бакалавров']
                if not pandas.isnull(row['ВКР специалистов']):
                    data_instance.vkr_spec = row['ВКР специалистов']
                if not pandas.isnull(row['ВКР магистров']):
                    data_instance.vkr_mag = row['ВКР магистров']
                if not pandas.isnull(row['Руководство практикой']):
                    data_instance.practise_ruk = row['Руководство практикой']
                if not pandas.isnull(row['Госэкзамены']):
                    data_instance.gos_exam = row['Госэкзамены']
                if not pandas.isnull(row['Рецензирование ВКР']):
                    data_instance.rez_vkr = row['Рецензирование ВКР']
                if not pandas.isnull(row['Защита ВКР']):
                    data_instance.zach_vkr = row['Защита ВКР']
                if not pandas.isnull(row['Руководство аспирантами']):
                    data_instance.asp_ruk = row['Руководство аспирантами']
                if not pandas.isnull(row['Другие виды учеб. нагрузки']):
                    data_instance.other = row['Другие виды учеб. нагрузки']
                data_instance.all = row['Количество часов всего']
                data_instance.save()
            instance = FileUploadModel(owner=request.user)
            instance.datafile.save(now + file_obj.name, file_obj)
            instance.save()

            df.to_html('test.html')
            # path_wkthmltopdf = r'D:\Progs/wkhtmltopdf/bin/wkhtmltopdf.exe'
            config = pdfkit.configuration(wkhtmltopdf='D:\\Progs\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
            fl = pdfkit.from_file('test.html', file_obj.name + '.pdf', configuration=config)

            gauth = GoogleAuth()
            # Try to load saved client credentials
            gauth.LoadCredentialsFile("mycreds.txt")
            if gauth.credentials is None:
                # Authenticate if they're not there
                gauth.LocalWebserverAuth()
            elif gauth.access_token_expired:
                # Refresh them if expired
                gauth.Refresh()
            else:
                # Initialize the saved creds
                gauth.Authorize()
            # Save the current credentials to a file
            gauth.SaveCredentialsFile("mycreds.txt")
            drive = GoogleDrive(gauth)
            textfile = drive.CreateFile({'title': file_obj.name})
            textfile.SetContentFile(file_obj.name + '.pdf')
            textfile.Upload()

        return Response(status=204)


class DataPagination(PageNumberPagination):
    page_size = 10


class Data(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    # pagination_class = DataPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        usr = self.request.user
        return DataTable.objects.filter(added_by=usr).all()


class Send(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        sender_email = "" #Your email
        receiver_email = request.data['email']
        password = '' #Email password   

        message = MIMEMultipart("alternative")
        message["Subject"] = "Data from Lab1"
        message["From"] = sender_email
        message["To"] = receiver_email
        html = '''\
        <html>
        <body>
    <table>
        <thead>
            <tr>
                <th>Название учебной дисциплины</th>
                <th>Дата</th>
                <th>Курс</th>
                <th>Группа</th>
                <th>База обучения</th>
                <th>Семестр</th>
                <th>Лекции</th>
                <th>Практические (сем.) занятия</th>
                <th>Лабораторные занятия</th>
                <th>Модульный контроль</th>
                <th>Семестр (консультации)</th>
                <th>Экзамен (консультации)</th>
                <th>Зачеты</th>
                <th>Экзамены</th>
                <th>Курсовые работы</th>
                <th>ВКР бакалавров</th>
                <th>ВКР специалистов</th>
                <th>ВКР магистров</th>
                <th>Руководство практикой</th>
                <th>Госэкзамены</th>
                <th>Рецензирование ВКР</th>
                <th>Защита ВКР</th>
                <th>Руководство аспирантами</th>
                <th>Другие виды учеб. нагрузки</th>
                <th>Количество часов всего</th>
            </tr>
        </thead>
        <tbody>
        '''

        for item in request.data['items']:
            html += '''\
            <tr>
                <td>{subject}</td>
                <td>{date}</td>
                <td>{course}</td>
                <td>{group_name}</td>
                <td>{base}</td>
                <td>{term}</td>
                <td>{lectures}</td>
                <td>{practise_less}</td>
                <td>{lab_works}</td>
                <td>{modular_control}</td>
                <td>{term_consultation}</td>
                <td>{exam_consultation}</td>
                <td>{credit}</td>
                <td>{exam}</td>
                <td>{course_work}</td>
                <td>{vkr_bac}</td>
                <td>{vkr_spec}</td>
                <td>{vkr_mag}</td>
                <td>{practise_ruk}</td>
                <td>{gos_exam}</td>
                <td>{rez_vkr}</td>
                <td>{zach_vkr}</td>
                <td>{asp_ruk}</td>
                <td>{other}</td>
                <td>{all}</td>
            </tr>
            '''.format(**item)
        html+='''\
                </tbody>
            </table>
        </body>
        </html>
        '''
        part = MIMEText(html, "html")
        message.attach(part)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        return Response({}, status=HTTP_200_OK)
