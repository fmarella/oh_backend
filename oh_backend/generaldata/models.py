from django.db import models


class Deliveryresulttype(models.Model):
    drt_id_a = models.CharField(db_column='DRT_ID_A', primary_key=True, max_length=1, verbose_name="Codice")
    drt_desc = models.CharField(db_column='DRT_DESC', max_length=50, verbose_name="Descrizione")
    
    def __str__(self):
        return self.drt_desc

    class Meta:
        db_table = 'DELIVERYRESULTTYPE'

class Deliverytype(models.Model):
    dlt_id_a = models.CharField(db_column='DLT_ID_A', primary_key=True, max_length=1, verbose_name="Codice")
    dlt_desc = models.CharField(db_column='DLT_DESC', max_length=50, verbose_name="Descrizione")
    class Meta:
        db_table = 'DELIVERYTYPE'

class Dischargetype(models.Model):
    dist_id_a = models.CharField(db_column='DIST_ID_A', primary_key=True, max_length=10, verbose_name="Codice")
    dist_desc = models.CharField(db_column='DIST_DESC', max_length=50, verbose_name="Descrizione")
    class Meta:
        db_table = 'DISCHARGETYPE'
        
class Diseasetype(models.Model):
    dcl_id_a = models.CharField(db_column='DCL_ID_A', primary_key=True, max_length=2, verbose_name="Codice")
    dcl_desc = models.CharField(db_column='DCL_DESC', max_length=50, verbose_name="Descrizione")
    class Meta:
        db_table = 'DISEASETYPE'
        
class Medicaldsrstockmovtype(models.Model):
    mmvt_id_a = models.CharField(db_column='MMVT_ID_A', primary_key=True, max_length=10, verbose_name="Codice")
    mmvt_desc = models.CharField(db_column='MMVT_DESC', max_length=50, verbose_name="Descrizione")
    mmvt_type = models.CharField(db_column='MMVT_TYPE', max_length=2)
    class Meta:
        db_table = 'MEDICALDSRSTOCKMOVTYPE'

class Medicaldsrtype(models.Model):
    mdsrt_id_a = models.CharField(db_column='MDSRT_ID_A', primary_key=True, max_length=1, verbose_name="Codice")
    mdsrt_desc = models.CharField(db_column='MDSRT_DESC', max_length=30, blank=True, verbose_name="Descrizione")
    class Meta:
        db_table = 'MEDICALDSRTYPE'
        
class Operationtype(models.Model):
    ocl_id_a = models.CharField(db_column='OCL_ID_A', primary_key=True, max_length=2, verbose_name="Codice")
    ocl_desc = models.CharField(db_column='OCL_DESC', max_length=50, verbose_name="Descrizione")
    ocl_type = models.CharField(db_column='OCL_TYPE', max_length=20)
    class Meta:
        db_table = 'OPERATIONTYPE'
        
class Pregnanttreatmenttype(models.Model):
    ptt_id_a = models.CharField(db_column='PTT_ID_A', primary_key=True, max_length=10, verbose_name="Codice")
    ptt_desc = models.CharField(db_column='PTT_DESC', max_length=50, verbose_name="Descrizione")
    class Meta:
        db_table = 'PREGNANTTREATMENTTYPE'
        
class Vaccinetype(models.Model):
    vact_id_a = models.CharField(db_column='VACT_ID_A', primary_key=True, max_length=1, verbose_name="Codice")
    vact_desc = models.CharField(db_column='VACT_DESC', max_length=50, verbose_name="Descrizione")
    class Meta:
        db_table = 'VACCINETYPE'
        
class Admissiontype(models.Model):
    admt_id_a = models.CharField(db_column='ADMT_ID_A', primary_key=True, max_length=10, verbose_name="Codice")
    admt_desc = models.CharField(db_column='ADMT_DESC', max_length=50, verbose_name="Descrizione")
    class Meta:
        db_table = 'ADMISSIONTYPE'

class Agetype(models.Model):
    at_code = models.CharField(db_column='AT_CODE', primary_key=True, max_length=4, verbose_name="Codice")
    at_from = models.IntegerField(db_column='AT_FROM')
    at_to = models.IntegerField(db_column='AT_TO')
    at_desc = models.CharField(db_column='AT_DESC', max_length=100, verbose_name="Descrizione")
    class Meta:
        db_table = 'AGETYPE'
        
class Examtype(models.Model):
    exc_id_a = models.CharField(db_column='EXC_ID_A', primary_key=True, max_length=2, verbose_name="Codice")
    exc_desc = models.CharField(db_column='EXC_DESC', max_length=50, verbose_name="Descrizione")
    class Meta:
        db_table = 'EXAMTYPE'
        
class Pricesothers(models.Model):
    oth_id = models.IntegerField(db_column='OTH_ID', primary_key=True, verbose_name="Codice")
    oth_code = models.CharField(db_column='OTH_CODE', max_length=10)
    oth_desc = models.CharField(db_column='OTH_DESC', max_length=100)
    oth_opd_include = models.IntegerField(db_column='OTH_OPD_INCLUDE')
    oth_ipd_include = models.IntegerField(db_column='OTH_IPD_INCLUDE')
    oth_daily = models.IntegerField(db_column='OTH_DAILY')
    oth_discharge = models.IntegerField(db_column='OTH_DISCHARGE', blank=True, null=True)
    oth_undefined = models.IntegerField(db_column='OTH_UNDEFINED', blank=True, null=True)
    class Meta:
        db_table = 'PRICESOTHERS'
