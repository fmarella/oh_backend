# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admissiontype',
            fields=[
                ('admt_id_a', models.CharField(max_length=10, serialize=False, primary_key=True, db_column=b'ADMT_ID_A')),
                ('admt_desc', models.CharField(max_length=50, db_column=b'ADMT_DESC')),
            ],
            options={
                'db_table': 'ADMISSIONTYPE',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Agetype',
            fields=[
                ('at_code', models.CharField(max_length=4, serialize=False, primary_key=True, db_column=b'AT_CODE')),
                ('at_from', models.IntegerField(db_column=b'AT_FROM')),
                ('at_to', models.IntegerField(db_column=b'AT_TO')),
                ('at_desc', models.CharField(max_length=100, db_column=b'AT_DESC')),
            ],
            options={
                'db_table': 'AGETYPE',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deliveryresulttype',
            fields=[
                ('drt_id_a', models.CharField(max_length=1, serialize=False, primary_key=True, db_column=b'DRT_ID_A')),
                ('drt_desc', models.CharField(max_length=50, db_column=b'DRT_DESC')),
            ],
            options={
                'db_table': 'DELIVERYRESULTTYPE',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deliverytype',
            fields=[
                ('dlt_id_a', models.CharField(max_length=1, serialize=False, primary_key=True, db_column=b'DLT_ID_A')),
                ('dlt_desc', models.CharField(max_length=50, db_column=b'DLT_DESC')),
            ],
            options={
                'db_table': 'DELIVERYTYPE',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dischargetype',
            fields=[
                ('dist_id_a', models.CharField(max_length=10, serialize=False, primary_key=True, db_column=b'DIST_ID_A')),
                ('dist_desc', models.CharField(max_length=50, db_column=b'DIST_DESC')),
            ],
            options={
                'db_table': 'DISCHARGETYPE',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Diseasetype',
            fields=[
                ('dcl_id_a', models.CharField(max_length=2, serialize=False, primary_key=True, db_column=b'DCL_ID_A')),
                ('dcl_desc', models.CharField(max_length=50, db_column=b'DCL_DESC')),
            ],
            options={
                'db_table': 'DISEASETYPE',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Examtype',
            fields=[
                ('exc_id_a', models.CharField(max_length=2, serialize=False, primary_key=True, db_column=b'EXC_ID_A')),
                ('exc_desc', models.CharField(max_length=50, db_column=b'EXC_DESC')),
            ],
            options={
                'db_table': 'EXAMTYPE',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Medicaldsrstockmovtype',
            fields=[
                ('mmvt_id_a', models.CharField(max_length=10, serialize=False, primary_key=True, db_column=b'MMVT_ID_A')),
                ('mmvt_desc', models.CharField(max_length=50, db_column=b'MMVT_DESC')),
                ('mmvt_type', models.CharField(max_length=2, db_column=b'MMVT_TYPE')),
            ],
            options={
                'db_table': 'MEDICALDSRSTOCKMOVTYPE',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Medicaldsrtype',
            fields=[
                ('mdsrt_id_a', models.CharField(max_length=1, serialize=False, primary_key=True, db_column=b'MDSRT_ID_A')),
                ('mdsrt_desc', models.CharField(max_length=30, db_column=b'MDSRT_DESC', blank=True)),
            ],
            options={
                'db_table': 'MEDICALDSRTYPE',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Operationtype',
            fields=[
                ('ocl_id_a', models.CharField(max_length=2, serialize=False, primary_key=True, db_column=b'OCL_ID_A')),
                ('ocl_desc', models.CharField(max_length=50, db_column=b'OCL_DESC')),
                ('ocl_type', models.CharField(max_length=20, db_column=b'OCL_TYPE')),
            ],
            options={
                'db_table': 'OPERATIONTYPE',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pregnanttreatmenttype',
            fields=[
                ('ptt_id_a', models.CharField(max_length=10, serialize=False, primary_key=True, db_column=b'PTT_ID_A')),
                ('ptt_desc', models.CharField(max_length=50, db_column=b'PTT_DESC')),
            ],
            options={
                'db_table': 'PREGNANTTREATMENTTYPE',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pricesothers',
            fields=[
                ('oth_id', models.IntegerField(serialize=False, primary_key=True, db_column=b'OTH_ID')),
                ('oth_code', models.CharField(max_length=10, db_column=b'OTH_CODE')),
                ('oth_desc', models.CharField(max_length=100, db_column=b'OTH_DESC')),
                ('oth_opd_include', models.IntegerField(db_column=b'OTH_OPD_INCLUDE')),
                ('oth_ipd_include', models.IntegerField(db_column=b'OTH_IPD_INCLUDE')),
                ('oth_daily', models.IntegerField(db_column=b'OTH_DAILY')),
                ('oth_discharge', models.IntegerField(null=True, db_column=b'OTH_DISCHARGE', blank=True)),
                ('oth_undefined', models.IntegerField(null=True, db_column=b'OTH_UNDEFINED', blank=True)),
            ],
            options={
                'db_table': 'PRICESOTHERS',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vaccinetype',
            fields=[
                ('vact_id_a', models.CharField(max_length=1, serialize=False, primary_key=True, db_column=b'VACT_ID_A')),
                ('vact_desc', models.CharField(max_length=50, db_column=b'VACT_DESC')),
            ],
            options={
                'db_table': 'VACCINETYPE',
            },
            bases=(models.Model,),
        ),
    ]
