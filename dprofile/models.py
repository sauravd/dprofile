
from django.db import models


class AccessToRoadnetwork(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    road_infrastructure = models.CharField(max_length=255, blank=True, null=True)
    road_infrastructure_unit = models.CharField(max_length=255, blank=True, null=True)
    road_infrastructure_baseyear = models.IntegerField(blank=True, null=True)
    road_infrastructure_condition = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'access_to_roadnetwork'


class AgriLivstkCooperatives(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    updated_date = models.DateField(blank=True, null=True)
    org_name = models.CharField(max_length=255, blank=True, null=True)
    registered_data = models.DateField(blank=True, null=True)
    org_address = models.CharField(max_length=255, blank=True, null=True)
    contact_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agri_livstk_cooperatives'


class AnimalHusbandryFirms(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    name_of_animal_husbandry_firm = models.CharField(max_length=255, blank=True, null=True)
    address_of_firm = models.CharField(max_length=255, blank=True, null=True)
    products = models.CharField(max_length=255, blank=True, null=True)
    units_produced = models.CharField(max_length=25, blank=True, null=True)
    amount_produced = models.IntegerField(blank=True, null=True)
    name_of_proprietor = models.CharField(max_length=255, blank=True, null=True)
    employed_female = models.IntegerField(blank=True, null=True)
    employed_male = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animal_husbandry_firms'


class AnimalProducts(models.Model):
    parent_index = models.IntegerField(blank=True, null=True)
    animal_name = models.CharField(max_length=255, blank=True, null=True)
    animal_count = models.IntegerField(blank=True, null=True)
    milk_production = models.IntegerField(blank=True, null=True)
    meat_production = models.IntegerField(blank=True, null=True)
    egg_production = models.IntegerField(blank=True, null=True)
    wool_production = models.IntegerField(blank=True, null=True)
    bone_production = models.IntegerField(blank=True, null=True)
    leather_production = models.IntegerField(blank=True, null=True)
    financial_gain = models.IntegerField(blank=True, null=True)
    key_column = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'animal_products'



class AvailabilityOfIrrigationFacilities(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    project_name = models.CharField(max_length=255, blank=True, null=True)
    irrigation_type = models.CharField(max_length=255, blank=True, null=True)
    irrigation_means = models.CharField(max_length=255, blank=True, null=True)
    units = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    irrigation_availability = models.CharField(max_length=255, blank=True, null=True)
    irrigated_area = models.IntegerField(blank=True, null=True)
    benefitting_household = models.IntegerField(blank=True, null=True)
    total_population = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'availability_of_irrigation_facilities'


class BuildingSlumHousingForUnderprivileged(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    housing_type = models.CharField(max_length=255, blank=True, null=True)
    housing_wardno = models.IntegerField(blank=True, null=True)
    housing_number = models.IntegerField(blank=True, null=True)
    housing_condition = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'building_slum_housing_for_underprivileged'


class CitizenAwarenessVillageDevelpmtOrg(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    name_of_org = models.CharField(max_length=255, blank=True, null=True)
    member_female = models.IntegerField(blank=True, null=True)
    member_male = models.IntegerField(blank=True, null=True)
    member_total = models.IntegerField(blank=True, null=True)
    covered_family_dalit = models.IntegerField(blank=True, null=True)
    covered_family_janajati = models.IntegerField(blank=True, null=True)
    covered_family_others = models.IntegerField(blank=True, null=True)
    covered_family_total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizen_awareness_village_develpmt_org'


class CommunityInstitutionDetails(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    community_org_saving_grp = models.IntegerField(blank=True, null=True)
    farmers_grp = models.IntegerField(blank=True, null=True)
    forest_grp = models.IntegerField(blank=True, null=True)
    cooperatives = models.IntegerField(blank=True, null=True)
    ngo_club_group_foundation = models.CharField(max_length=255, blank=True, null=True)
    traditional_grp = models.IntegerField(blank=True, null=True)
    mothers_grp = models.IntegerField(blank=True, null=True)
    civi_awareness_center = models.IntegerField(blank=True, null=True)
    locality_development_committee = models.IntegerField(blank=True, null=True)
    entrepreneurial_grp = models.IntegerField(blank=True, null=True)
    others = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'community_institution_details'


class DeadFamilyMembers(models.Model):
    parent_index = models.IntegerField(blank=True, null=True)
    death_within_year = models.BooleanField(blank=True, null=True)
    name_of_dead = models.CharField(max_length=255, blank=True, null=True)
    relationship_with_hh = models.CharField(max_length=255, blank=True, null=True)
    gender_of_dead = models.CharField(max_length=10, blank=True, null=True)
    age_at_death = models.IntegerField(blank=True, null=True)
    reason_of_death = models.CharField(max_length=255, blank=True, null=True)
    disease_of_dead = models.CharField(max_length=255, blank=True, null=True)
    pregnantwomen = models.BooleanField(blank=True, null=True)
    infant = models.BooleanField(blank=True, null=True)
    key_column = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dead_family_members'


class DescriptionOfBridges(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    bridge_name = models.CharField(max_length=255, blank=True, null=True)
    bridged_river_name = models.CharField(max_length=255, blank=True, null=True)
    bridge_link_starting_place = models.CharField(max_length=255, blank=True, null=True)
    bridge_link_ending_place = models.CharField(max_length=255, blank=True, null=True)
    bridge_type = models.CharField(max_length=255, blank=True, null=True)
    bridge_length = models.IntegerField(blank=True, null=True)
    bridge_condition = models.CharField(max_length=255, blank=True, null=True)
    bridge_constructed_year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'description_of_bridges'


class DescriptionOfCommunityForests(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    registration_no = models.IntegerField(blank=True, null=True)
    comun_forest_consumer_grp_name = models.CharField(max_length=255, blank=True, null=True)
    address_at_handover = models.CharField(max_length=255, blank=True, null=True)
    present_address = models.CharField(max_length=255, blank=True, null=True)
    household = models.IntegerField(blank=True, null=True)
    handover_date = models.DateField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'description_of_community_forests'


class DescriptionOfDiseaseTreatment(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    disease_name = models.CharField(max_length=255, blank=True, null=True)
    diseased_number = models.IntegerField(blank=True, null=True)
    treated_number = models.IntegerField(blank=True, null=True)
    followup_number = models.IntegerField(blank=True, null=True)
    referred_number = models.IntegerField(blank=True, null=True)
    dead_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'description_of_disease_treatment'


class DescriptionOfGovernmentBuilding(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    building_name = models.CharField(max_length=255, blank=True, null=True)
    building_tole_name = models.CharField(max_length=255, blank=True, null=True)
    office_name = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.IntegerField(blank=True, null=True)
    building_type = models.CharField(max_length=255, blank=True, null=True)
    building_condition = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'description_of_government_building'


class DetailsOfNgo(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    org_name = models.CharField(max_length=255, blank=True, null=True)
    yearly_budget = models.BigIntegerField(blank=True, null=True)
    subject_area = models.CharField(max_length=255, blank=True, null=True)
    human_resources = models.IntegerField(blank=True, null=True)
    development_partner = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'details_of_ngo'


class DisasterManagement(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    disaster_name = models.CharField(max_length=255, blank=True, null=True)
    units = models.CharField(max_length=25, blank=True, null=True)
    wardno = models.CharField(max_length=100, blank=True, null=True)
    disaster_percentage = models.IntegerField(blank=True, null=True)
    disaster_condition = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disaster_management'


class EnvironmentAndHygiene(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    indicator = models.CharField(max_length=255, blank=True, null=True)
    indicator_numbers = models.IntegerField(blank=True, null=True)
    units = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'environment_and_hygiene'


class FarmersEntrepreneursAndSavingsGroups(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    name_of_org = models.CharField(max_length=255, blank=True, null=True)
    member_female = models.IntegerField(blank=True, null=True)
    member_male = models.IntegerField(blank=True, null=True)
    member_total = models.IntegerField(blank=True, null=True)
    covered_family_dalit = models.IntegerField(blank=True, null=True)
    covered_family_janajati = models.IntegerField(blank=True, null=True)
    covered_family_others = models.IntegerField(blank=True, null=True)
    covered_family_total = models.IntegerField(blank=True, null=True)
    saving_amount = models.IntegerField(blank=True, null=True)
    investment_amount = models.IntegerField(blank=True, null=True)
    investment_field = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmers_entrepreneurs_and_savings_groups'


class FinancialInstutionsDetails(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    org_name = models.CharField(max_length=255, blank=True, null=True)
    org_type = models.CharField(max_length=255, blank=True, null=True)
    yearly_transaction = models.BigIntegerField(blank=True, null=True)
    investment_amount = models.BigIntegerField(blank=True, null=True)
    investment_fields = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financial_instutions_details'


class ForestDescription(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    forest_type = models.CharField(max_length=255, blank=True, null=True)
    covered_hh = models.IntegerField(blank=True, null=True)
    forest_name = models.CharField(max_length=255, blank=True, null=True)
    forest_area = models.FloatField(blank=True, null=True)
    accumulation_rate = models.FloatField(blank=True, null=True)
    wood_production = models.FloatField(blank=True, null=True)
    firewood_production = models.FloatField(blank=True, null=True)
    medicinal_herbs = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forest_description'


class ForestInLocalLevel(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    forest_type = models.CharField(max_length=255, blank=True, null=True)
    forest_area = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forest_in_local_level'


class ForestryAndEnvironment(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    fne_areas = models.CharField(max_length=255, blank=True, null=True)
    fne_unit = models.CharField(max_length=255, blank=True, null=True)
    fne_amount = models.FloatField(blank=True, null=True)
    fne_number = models.IntegerField(blank=True, null=True)
    fne_wardno = models.CharField(max_length=255, blank=True, null=True)
    fne_condition = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forestry_and_environment'


class GenderEqualtiyNSocialInclusion(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    service_delivery = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    baseline_year = models.IntegerField(blank=True, null=True)
    condition = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gender_equaltiy_n_social_inclusion'


class GhattaMillsAndCollectionProcessingCenters(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    watermill_traditional = models.IntegerField(blank=True, null=True)
    watermill_improved = models.IntegerField(blank=True, null=True)
    coldstorage = models.IntegerField(blank=True, null=True)
    grinding_watermill = models.IntegerField(blank=True, null=True)
    grinding_diselmill = models.IntegerField(blank=True, null=True)
    grinding_electricitymill = models.IntegerField(blank=True, null=True)
    collection_processing_center_agri = models.IntegerField(blank=True, null=True)
    collection_processing_center_herbs = models.IntegerField(blank=True, null=True)
    collection_processing_center_industry = models.IntegerField(blank=True, null=True)
    salescenter_koselihouse = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ghatta_mills_and_collection_processing_centers'


class GovernmentOfficesAndAgencies(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    gov_org_type = models.CharField(max_length=255, blank=True, null=True)
    gov_org_name = models.CharField(max_length=255, blank=True, null=True)
    gov_org_address = models.CharField(max_length=255, blank=True, null=True)
    gov_org_area = models.FloatField(blank=True, null=True)
    gov_human_resources = models.IntegerField(blank=True, null=True)
    gov_org_are_of_work = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'government_offices_and_agencies'


class HealthNNutritionInformation(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    health_n_nutrition = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    baseline_year = models.IntegerField(blank=True, null=True)
    condition = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'health_n_nutrition_information'


class HhFamilydetails(models.Model):
    parent_index = models.IntegerField(blank=True, null=True)
    fristname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    englishname = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    realationship_with_hh = models.CharField(max_length=255, blank=True, null=True)
    other_relationship = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    bloodgrp = models.CharField(max_length=25, blank=True, null=True)
    citizenship = models.CharField(max_length=15, blank=True, null=True)
    citizenship_no = models.CharField(max_length=50, blank=True, null=True)
    citizenship_issuedate = models.DateField(blank=True, null=True)
    citizenship_issuedist = models.CharField(max_length=255, blank=True, null=True)
    no_citizenship_reason = models.CharField(max_length=255, blank=True, null=True)
    nationalid = models.CharField(max_length=25, blank=True, null=True)
    nationalid_no = models.CharField(max_length=255, blank=True, null=True)
    nationalid_issue_date = models.DateField(blank=True, null=True)
    passport = models.CharField(max_length=20, blank=True, null=True)
    passport_no = models.CharField(max_length=255, blank=True, null=True)
    passport_issuedate = models.DateField(blank=True, null=True)
    passport_issue_place = models.CharField(max_length=255, blank=True, null=True)
    passport_expire_date = models.DateField(blank=True, null=True)
    pan = models.CharField(max_length=25, blank=True, null=True)
    pan_no = models.IntegerField(blank=True, null=True)
    ssid = models.CharField(max_length=25, blank=True, null=True)
    ssid_no = models.IntegerField(blank=True, null=True)
    driving_license = models.CharField(max_length=25, blank=True, null=True)
    driving_license_no = models.IntegerField(blank=True, null=True)
    driving_license_issuedate = models.DateField(blank=True, null=True)
    driving_license_expdate = models.DateField(blank=True, null=True)
    driving_license_category = models.CharField(max_length=10, blank=True, null=True)
    mobilenumber = models.CharField(max_length=100, blank=True, null=True)
    voteridno = models.IntegerField(blank=True, null=True)
    voting_place = models.CharField(max_length=100, blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    caste_caste = models.CharField(max_length=255, blank=True, null=True)
    religion = models.CharField(max_length=255, blank=True, null=True)
    mother_tongue = models.CharField(max_length=255, blank=True, null=True)
    edulevel = models.CharField(max_length=255, blank=True, null=True)
    edufaculty = models.CharField(max_length=255, blank=True, null=True)
    gradyear = models.IntegerField(blank=True, null=True)
    edu_gradingsys = models.CharField(max_length=255, blank=True, null=True)
    gradeobtained = models.CharField(max_length=255, blank=True, null=True)
    eduinstitutename = models.CharField(max_length=255, blank=True, null=True)
    schooldropout = models.BooleanField(blank=True, null=True)
    schooldropout_reason = models.CharField(max_length=255, blank=True, null=True)
    residence_status = models.CharField(max_length=255, blank=True, null=True)
    residence_country = models.CharField(max_length=255, blank=True, null=True)
    residence_locallevel = models.CharField(max_length=255, blank=True, null=True)
    residence_locallevel_wardno = models.IntegerField(blank=True, null=True)
    migration_reason = models.CharField(max_length=255, blank=True, null=True)
    migration_reason_salaryjob = models.IntegerField(blank=True, null=True)
    migration_reason_business = models.IntegerField(blank=True, null=True)
    migration_reason_sudytraining = models.IntegerField(blank=True, null=True)
    migration_reason_jobsearch = models.IntegerField(blank=True, null=True)
    migration_reason_dependent = models.IntegerField(blank=True, null=True)
    profession_business = models.CharField(max_length=255, blank=True, null=True)
    maritalstatus = models.CharField(max_length=255, blank=True, null=True)
    foreignmigrationreturnee = models.BooleanField(blank=True, null=True)
    countryreturnedfrom = models.CharField(max_length=255, blank=True, null=True)
    professionabroad = models.CharField(max_length=255, blank=True, null=True)
    workdurationabroad = models.IntegerField(blank=True, null=True)
    skilltraining = models.CharField(max_length=255, blank=True, null=True)
    trainingduration = models.IntegerField(blank=True, null=True)
    trainingyear = models.IntegerField(blank=True, null=True)
    professioninnepal = models.CharField(max_length=255, blank=True, null=True)
    disabilitystatus = models.CharField(max_length=255, blank=True, null=True)
    disabilitytype = models.CharField(max_length=255, blank=True, null=True)
    healthstatus = models.CharField(max_length=255, blank=True, null=True)
    infecteddisease = models.CharField(max_length=255, blank=True, null=True)
    infecteddisease_heartdisease = models.IntegerField(blank=True, null=True)
    infecteddisease_asthama_respiratory = models.IntegerField(blank=True, null=True)
    infecteddisease_tumor_cancer = models.IntegerField(blank=True, null=True)
    infecteddisease_diabetes = models.IntegerField(blank=True, null=True)
    infecteddisease_kidney_live = models.IntegerField(blank=True, null=True)
    infecteddisease_gynecology = models.IntegerField(blank=True, null=True)
    infecteddisease_ulcer_intestinal = models.IntegerField(blank=True, null=True)
    infecteddisease_hypertension = models.IntegerField(blank=True, null=True)
    infecteddisease_lowbloodpressure = models.IntegerField(blank=True, null=True)
    infecteddisease_arthritis = models.IntegerField(blank=True, null=True)
    infecteddisease_epilepsy = models.IntegerField(blank=True, null=True)
    infecteddisease_parkinsons = models.IntegerField(blank=True, null=True)
    infecteddisease_alzheimers = models.IntegerField(blank=True, null=True)
    infecteddisease_otherdisease = models.IntegerField(blank=True, null=True)
    contactless_abroad = models.BooleanField(blank=True, null=True)
    associated_tole_dvlp_org = models.CharField(max_length=255, blank=True, null=True)
    interestedprofession = models.CharField(max_length=255, blank=True, null=True)
    interestedprofession_others = models.CharField(max_length=255, blank=True, null=True)
    officename = models.CharField(max_length=255, blank=True, null=True)
    office_designation = models.CharField(max_length=255, blank=True, null=True)
    exprienceyears = models.IntegerField(blank=True, null=True)
    affectedbypandemic = models.BooleanField(blank=True, null=True)
    nameofpandemic = models.CharField(max_length=255, blank=True, null=True)
    otherpandemic = models.CharField(max_length=255, blank=True, null=True)
    pandeimcinfecteddate = models.IntegerField(blank=True, null=True)
    symptomofpandemic = models.CharField(max_length=255, blank=True, null=True)
    sympt_pandmi_diarrhoea = models.IntegerField(blank=True, null=True)
    sympt_pandmi_fever = models.IntegerField(blank=True, null=True)
    sympt_pandmi_cough = models.IntegerField(blank=True, null=True)
    sympt_pandmi_lung_infection = models.IntegerField(blank=True, null=True)
    sympt_pandmi_othersymptoms = models.IntegerField(blank=True, null=True)
    sympt_pandmi_othersymptoms_name = models.CharField(max_length=255, blank=True, null=True)
    stayedafterinfection = models.CharField(max_length=255, blank=True, null=True)
    styed_at_homeisolation = models.IntegerField(blank=True, null=True)
    styed_at_locallevel_isolation = models.IntegerField(blank=True, null=True)
    styed_at_hospital = models.IntegerField(blank=True, null=True)
    typeofroominhospital = models.CharField(max_length=255, blank=True, null=True)
    neededoxygentreatment = models.BooleanField(blank=True, null=True)
    daysinhospital = models.IntegerField(blank=True, null=True)
    vaccinatedwithcovid19 = models.BooleanField(blank=True, null=True)
    doseofvaccine = models.CharField(max_length=255, blank=True, null=True)
    nameofvaccine = models.CharField(max_length=255, blank=True, null=True)
    healthinsurance = models.BooleanField(blank=True, null=True)
    accinbank = models.BooleanField(blank=True, null=True)
    nameofbank = models.CharField(max_length=255, blank=True, null=True)
    key_column = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'hh_familydetails'


class HhSurvey(models.Model):
    indexno = models.IntegerField(primary_key=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    nepaliname = models.CharField(max_length=255, blank=True, null=True)
    englishname = models.CharField(max_length=255, blank=True, null=True)
    fathersname = models.CharField(max_length=255, blank=True, null=True)
    mothersname = models.CharField(max_length=255, blank=True, null=True)
    grandfathersname = models.CharField(max_length=255, blank=True, null=True)
    grandmothersname = models.CharField(max_length=255, blank=True, null=True)
    nooffamilymember = models.IntegerField(blank=True, null=True)
    photo_name = models.CharField(max_length=255, blank=True, null=True)
    photoofhhh = models.BinaryField(blank=True, null=True)
    houseno = models.FloatField(blank=True, null=True)
    tole = models.CharField(max_length=255, blank=True, null=True)
    wardno = models.FloatField(blank=True, null=True)
    phonenumber = models.CharField(max_length=255, blank=True, null=True)
    medicaltreatment_choice_one = models.CharField(max_length=255, blank=True, null=True)
    medicaltreatment_choice_two = models.CharField(max_length=255, blank=True, null=True)
    medicaltreatment_choice_three = models.CharField(max_length=255, blank=True, null=True)
    pregnantmember_regular_medics_consultation = models.CharField(max_length=255, blank=True, null=True)
    childbirthplace_within_one_year = models.CharField(max_length=255, blank=True, null=True)
    childbirth_death_afterdelivery_or_within_six_weeks = models.CharField(max_length=10, blank=True, null=True)
    child_death_within_four_weeks = models.CharField(max_length=10, blank=True, null=True)
    no_of_dead_children_within_four_weeks = models.IntegerField(blank=True, null=True)
    child_death_from_four_weeks_to_a_year = models.CharField(max_length=10, blank=True, null=True)
    no_of_dead_children_four_to_a_year_time = models.IntegerField(blank=True, null=True)
    below_five_yrs_vaccinated_with_bcg_dpt_measles = models.CharField(max_length=10, blank=True, null=True)
    landuse_for_agri_livestock = models.CharField(max_length=10, blank=True, null=True)
    land_area_owned = models.IntegerField(blank=True, null=True)
    family_land_area = models.IntegerField(blank=True, null=True)
    land_area_for_food_crop = models.CharField(max_length=255, blank=True, null=True)
    enoughirrigation_in_cultivationarea = models.CharField(max_length=10, blank=True, null=True)
    land_area_irrigated_throughout_year = models.IntegerField(blank=True, null=True)
    source_of_irrigation = models.CharField(max_length=255, blank=True, null=True)
    src_of_irri_canal = models.IntegerField(blank=True, null=True)
    src_of_irri_tubewell = models.IntegerField(blank=True, null=True)
    src_of_irri_deepboring = models.IntegerField(blank=True, null=True)
    src_of_irri_dripirrigation = models.IntegerField(blank=True, null=True)
    src_of_irri_springcall = models.IntegerField(blank=True, null=True)
    src_of_irri_rainwater = models.IntegerField(blank=True, null=True)
    src_of_irri_plasticpond = models.IntegerField(blank=True, null=True)
    src_of_irri_sluice = models.IntegerField(blank=True, null=True)
    src_of_irri_drainage = models.IntegerField(blank=True, null=True)
    ownership_of_house_residing = models.CharField(max_length=255, blank=True, null=True)
    house_construction_type = models.CharField(max_length=255, blank=True, null=True)
    house_storey = models.IntegerField(blank=True, null=True)
    area_covered_by_house = models.IntegerField(blank=True, null=True)
    year_constructed = models.CharField(max_length=255, blank=True, null=True)
    house_design_approved = models.CharField(max_length=10, blank=True, null=True)
    source_of_drinkingwater = models.CharField(max_length=255, blank=True, null=True)
    src_of_dw_pipedwater_insidehouse = models.IntegerField(blank=True, null=True)
    src_of_dw_pipedwater_outsidehouse = models.IntegerField(blank=True, null=True)
    src_of_dw_deepboring = models.IntegerField(blank=True, null=True)
    src_of_dw_tubewell = models.IntegerField(blank=True, null=True)
    src_of_dw_handpump = models.IntegerField(blank=True, null=True)
    src_of_dw_well = models.IntegerField(blank=True, null=True)
    src_of_dw_openwell = models.IntegerField(blank=True, null=True)
    src_of_dw_watersource = models.IntegerField(blank=True, null=True)
    src_of_dw_river = models.IntegerField(blank=True, null=True)
    src_of_dw_jarbottled = models.IntegerField(blank=True, null=True)
    purify_water_before_drinking = models.CharField(max_length=10, blank=True, null=True)
    techniques_for_water_purification = models.CharField(max_length=255, blank=True, null=True)
    boiling = models.IntegerField(blank=True, null=True)
    chlorine_or_pius = models.IntegerField(blank=True, null=True)
    water_filter = models.IntegerField(blank=True, null=True)
    sodis_filter = models.IntegerField(blank=True, null=True)
    cooking_fule = models.CharField(max_length=255, blank=True, null=True)
    cooking_wood = models.IntegerField(blank=True, null=True)
    cooking_kerosene = models.IntegerField(blank=True, null=True)
    cooking_lpgas = models.IntegerField(blank=True, null=True)
    cooking_electricity = models.IntegerField(blank=True, null=True)
    cooking_biogas = models.IntegerField(blank=True, null=True)
    cooking_guitha = models.IntegerField(blank=True, null=True)
    stove_used_at_home = models.CharField(max_length=255, blank=True, null=True)
    stove_mud = models.IntegerField(blank=True, null=True)
    stove_improved_smokeless = models.IntegerField(blank=True, null=True)
    stove_vushe = models.IntegerField(blank=True, null=True)
    stove_kerosene = models.IntegerField(blank=True, null=True)
    stove_gastove = models.IntegerField(blank=True, null=True)
    stove_induction = models.IntegerField(blank=True, null=True)
    source_of_light = models.CharField(max_length=255, blank=True, null=True)
    electricity_source = models.CharField(max_length=255, blank=True, null=True)
    metered_connection = models.CharField(max_length=10, blank=True, null=True)
    toilet_type = models.CharField(max_length=255, blank=True, null=True)
    toilet_connected_to_publicdrainage = models.IntegerField(blank=True, null=True)
    toilet_flush_with_septictank = models.IntegerField(blank=True, null=True)
    toilet_simple = models.IntegerField(blank=True, null=True)
    toilet_temporary = models.IntegerField(blank=True, null=True)
    toilet_public = models.IntegerField(blank=True, null=True)
    toilet_notoilet = models.IntegerField(blank=True, null=True)
    income_from_agriculture = models.IntegerField(blank=True, null=True)
    income_from_business = models.IntegerField(blank=True, null=True)
    income_from_industry = models.IntegerField(blank=True, null=True)
    income_from_job = models.IntegerField(blank=True, null=True)
    income_from_remittence = models.IntegerField(blank=True, null=True)
    income_from_rent = models.IntegerField(blank=True, null=True)
    income_from_enterprenureship = models.IntegerField(blank=True, null=True)
    income_from_othersource = models.IntegerField(blank=True, null=True)
    expense_from_food = models.IntegerField(blank=True, null=True)
    expense_from_education = models.IntegerField(blank=True, null=True)
    expense_from_health = models.IntegerField(blank=True, null=True)
    expense_from_taxandservices = models.IntegerField(blank=True, null=True)
    expense_from_enterandtravel = models.IntegerField(blank=True, null=True)
    expense_from_socialwork = models.IntegerField(blank=True, null=True)
    expense_from_loanpayment = models.IntegerField(blank=True, null=True)
    expense_from_donation = models.IntegerField(blank=True, null=True)
    expense_from_othersexpense = models.IntegerField(blank=True, null=True)
    serviceconsumed_radio = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_televison = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_landlinetelephone = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_mobile = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_smartphone = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_tablet = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_computer = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_laptop = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_internet = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_motorcycle = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_car = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_refrigerator = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_washingmachine = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_airconditioner = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_transportvehicle = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_tracktor = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_waterfilter = models.CharField(max_length=10, blank=True, null=True)
    serviceconsumed_electricfan = models.CharField(max_length=10, blank=True, null=True)
    cattle_rearing = models.CharField(max_length=10, blank=True, null=True)
    number_of_ponds = models.IntegerField(blank=True, null=True)
    area_of_pond = models.IntegerField(blank=True, null=True)
    yearly_fish_production = models.IntegerField(blank=True, null=True)
    number_of_beehive = models.IntegerField(blank=True, null=True)
    beehive_type = models.CharField(max_length=255, blank=True, null=True)
    yearly_honey_production = models.IntegerField(blank=True, null=True)
    silkworm_cocoons_number = models.IntegerField(blank=True, null=True)
    silk_production = models.IntegerField(blank=True, null=True)
    type_of_healthfacility = models.CharField(max_length=255, blank=True, null=True)
    nearest_healthfacility = models.CharField(max_length=255, blank=True, null=True)
    time_to_reach_nearest_healthfacility = models.IntegerField(blank=True, null=True)
    medium_to_reach_nearest_healthfacility = models.CharField(max_length=255, blank=True, null=True)
    nearest_education_institute = models.CharField(max_length=255, blank=True, null=True)
    time_to_reach_nearest_educationfacility = models.IntegerField(blank=True, null=True)
    medium_to_reach_nearest_educationfacility = models.CharField(max_length=255, blank=True, null=True)
    solid_waste_management_site = models.CharField(max_length=255, blank=True, null=True)
    solid_waste_river = models.IntegerField(blank=True, null=True)
    solid_waste_stream = models.IntegerField(blank=True, null=True)
    solid_waste_roadside = models.IntegerField(blank=True, null=True)
    solid_waste_dumpingsite = models.IntegerField(blank=True, null=True)
    solid_waste_housecompund = models.IntegerField(blank=True, null=True)
    solid_waste_compostebin = models.IntegerField(blank=True, null=True)
    solid_waste_publicplace = models.IntegerField(blank=True, null=True)
    solid_waste_anywhere = models.IntegerField(blank=True, null=True)
    drainage_facility_at_home = models.CharField(max_length=255, blank=True, null=True)
    nodrainage_water_waste_mgmt_place = models.CharField(max_length=255, blank=True, null=True)
    nodrainage_river = models.IntegerField(blank=True, null=True)
    nodrainage_stream = models.IntegerField(blank=True, null=True)
    nodrainage_road = models.IntegerField(blank=True, null=True)
    nodrainage_inside_housecompund = models.IntegerField(blank=True, null=True)
    nodrainage_kitchengarden = models.IntegerField(blank=True, null=True)
    social_financial_participation = models.CharField(max_length=255, blank=True, null=True)
    female_in_social_org = models.CharField(max_length=10, blank=True, null=True)
    female_in_social_org_name = models.CharField(max_length=255, blank=True, null=True)
    female_in_tole_devlpmnt_inst = models.IntegerField(blank=True, null=True)
    female_in_agri_grp = models.IntegerField(blank=True, null=True)
    female_in_yuth_grp = models.IntegerField(blank=True, null=True)
    female_in_club = models.IntegerField(blank=True, null=True)
    female_in_consumer_committee = models.IntegerField(blank=True, null=True)
    female_in_schl_mgmt_committee = models.IntegerField(blank=True, null=True)
    female_in_drnk_water_consum_grp = models.IntegerField(blank=True, null=True)
    female_in_forest_consum_grp = models.IntegerField(blank=True, null=True)
    female_in_mother_grp = models.IntegerField(blank=True, null=True)
    female_in_cooperative = models.IntegerField(blank=True, null=True)
    natural_calamity_risk = models.CharField(max_length=255, blank=True, null=True)
    natural_calamity_risk_flood = models.IntegerField(blank=True, null=True)
    natural_calamity_risk_landslide = models.IntegerField(blank=True, null=True)
    natural_calamity_risk_fire = models.IntegerField(blank=True, null=True)
    natural_calamity_risk_epidemic = models.IntegerField(blank=True, null=True)
    natural_calamity_risk_wind = models.IntegerField(blank=True, null=True)
    natural_calamity_risk_lightning = models.IntegerField(blank=True, null=True)
    natural_calamity_risk_rivererosion = models.IntegerField(blank=True, null=True)
    natural_calamity_risk_drought = models.IntegerField(blank=True, null=True)
    natural_calamity_risk_winterwave = models.IntegerField(blank=True, null=True)
    natural_calamity_risk_earthquake = models.IntegerField(blank=True, null=True)
    natural_calamity_risk_hail = models.IntegerField(blank=True, null=True)
    natural_calamity_risk_none = models.IntegerField(blank=True, null=True)
    affected_by_natural_calamity_this_year = models.CharField(max_length=40, blank=True, null=True)
    decision_abt_household_subjects_takenby = models.CharField(max_length=255, blank=True, null=True)
    household_work_involvement = models.CharField(max_length=255, blank=True, null=True)
    bank_acc_operation = models.CharField(max_length=255, blank=True, null=True)
    consumer_committee_participation = models.CharField(max_length=255, blank=True, null=True)
    school_mgmt_committee_participation = models.CharField(max_length=255, blank=True, null=True)
    industry_business_involvement = models.CharField(max_length=255, blank=True, null=True)
    registered_as_taxpayer = models.CharField(max_length=255, blank=True, null=True)
    pan_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hh_survey'


class HotelsLodgesResturantsHomestay(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    serial_no = models.IntegerField(blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)
    firms_name = models.CharField(max_length=255, blank=True, null=True)
    proprietor_name = models.CharField(max_length=255, blank=True, null=True)
    firm_type = models.CharField(max_length=255, blank=True, null=True)
    firm_address = models.CharField(max_length=255, blank=True, null=True)
    registration_no = models.IntegerField(blank=True, null=True)
    firm_renewed = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotels_lodges_resturants_homestay'


class HrRelatedToAgricultureAndAnimalHusbandry(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    lead_farmer = models.CharField(max_length=255, blank=True, null=True)
    active_rural_jta = models.CharField(max_length=255, blank=True, null=True)
    active_rural_animal_health_activist = models.CharField(max_length=255, blank=True, null=True)
    commercial_nursery_operator = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_related_to_agriculture_and_animal_husbandry'


class InvestmentInformation(models.Model):
    parent_index = models.IntegerField(blank=True, null=True)
    investment_area = models.CharField(max_length=255, blank=True, null=True)
    investment_area_agriculture_forestry = models.IntegerField(blank=True, null=True)
    investment_area_fisheries = models.IntegerField(blank=True, null=True)
    investment_area_mining_quarrying = models.IntegerField(blank=True, null=True)
    investment_area_industry = models.IntegerField(blank=True, null=True)
    investment_area_electricity_gas_water = models.IntegerField(blank=True, null=True)
    investment_area_construction = models.IntegerField(blank=True, null=True)
    investment_area_wholesale_retail = models.IntegerField(blank=True, null=True)
    investment_area_transport_communication_storage = models.IntegerField(blank=True, null=True)
    investment_area_hotel_resturant = models.IntegerField(blank=True, null=True)
    investment_area_financial_intermediation = models.IntegerField(blank=True, null=True)
    investment_area_realestate_rental_businessservices = models.IntegerField(blank=True, null=True)
    investment_area_publicadmin_defence = models.IntegerField(blank=True, null=True)
    investment_area_education = models.IntegerField(blank=True, null=True)
    investment_amount = models.IntegerField(blank=True, null=True)
    key_column = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'investment_information'


class LandUseCondition(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    land_use_description = models.CharField(max_length=255, blank=True, null=True)
    wardno = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.FloatField(blank=True, null=True)
    land_condition = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'land_use_condition'


class LoanInformation(models.Model):
    parent_index = models.IntegerField(blank=True, null=True)
    loan_area = models.CharField(max_length=255, blank=True, null=True)
    loan_area_business_indutry = models.IntegerField(blank=True, null=True)
    loan_area_agri_anihusb_beekeeping_vegcultivation = models.IntegerField(blank=True, null=True)
    loan_area_house_land = models.IntegerField(blank=True, null=True)
    loan_area_birth_death_marriage_engagement = models.IntegerField(blank=True, null=True)
    loan_area_business_festival = models.IntegerField(blank=True, null=True)
    loan_area_business_medicine_treatment = models.IntegerField(blank=True, null=True)
    loan_area_business_education = models.IntegerField(blank=True, null=True)
    loan_area_business_householdconsumption = models.IntegerField(blank=True, null=True)
    loan_area_business_send_familymember_abroad = models.IntegerField(blank=True, null=True)
    loan_area_business_other_purpose = models.IntegerField(blank=True, null=True)
    loan_source = models.CharField(max_length=255, blank=True, null=True)
    loan_source_bank_finance = models.IntegerField(blank=True, null=True)
    loan_source_cooperative = models.IntegerField(blank=True, null=True)
    loan_source_personal = models.IntegerField(blank=True, null=True)
    loan_source_other_source = models.IntegerField(blank=True, null=True)
    loan_amt = models.IntegerField(blank=True, null=True)
    key_column = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'loan_information'


class MajorFestivalsAndFairs(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    festivals = models.CharField(max_length=255, blank=True, null=True)
    festival_place = models.CharField(max_length=255, blank=True, null=True)
    celebration_month = models.CharField(max_length=255, blank=True, null=True)
    festival_main_feature = models.CharField(max_length=255, blank=True, null=True)
    festival_main_community = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'major_festivals_and_fairs'


class MappingOfNaturalResources(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    resource_name = models.CharField(max_length=255, blank=True, null=True)
    resource_wardno = models.CharField(max_length=255, blank=True, null=True)
    firm_name = models.CharField(max_length=255, blank=True, null=True)
    firm_condition = models.CharField(max_length=255, blank=True, null=True)
    firm_number = models.IntegerField(blank=True, null=True)
    firm_area = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapping_of_natural_resources'


class MotherWomenGroupAndTraditionalGroup(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    name_of_org = models.CharField(max_length=255, blank=True, null=True)
    member_female = models.IntegerField(blank=True, null=True)
    member_male = models.IntegerField(blank=True, null=True)
    member_total = models.IntegerField(blank=True, null=True)
    covered_family_dalit = models.IntegerField(blank=True, null=True)
    covered_family_janajati = models.IntegerField(blank=True, null=True)
    covered_family_others = models.IntegerField(blank=True, null=True)
    covered_family_total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mother_women_group_and_traditional_group'


class NaturalCalamity(models.Model):
    parent_index = models.IntegerField(blank=True, null=True)
    calamity_name = models.CharField(max_length=255, blank=True, null=True)
    calamity_flood = models.IntegerField(blank=True, null=True)
    calamity_landslide = models.IntegerField(blank=True, null=True)
    calamity_fire = models.IntegerField(blank=True, null=True)
    calamity_epidemic = models.IntegerField(blank=True, null=True)
    calamity_wind = models.IntegerField(blank=True, null=True)
    calamity_lightning = models.IntegerField(blank=True, null=True)
    calamity_river_erosion = models.IntegerField(blank=True, null=True)
    calamity_drought = models.IntegerField(blank=True, null=True)
    calamity_winter_wave = models.IntegerField(blank=True, null=True)
    calamity_earthquake = models.IntegerField(blank=True, null=True)
    calamity_hail = models.IntegerField(blank=True, null=True)
    calamity_norisk = models.IntegerField(blank=True, null=True)
    cost_of_damage = models.IntegerField(blank=True, null=True)
    key_column = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'natural_calamity'


class PersonalEventDetails(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    birth = models.IntegerField(blank=True, null=True)
    death = models.IntegerField(blank=True, null=True)
    marriage = models.IntegerField(blank=True, null=True)
    divorce = models.IntegerField(blank=True, null=True)
    migration_incoming = models.IntegerField(blank=True, null=True)
    migration_outgoing = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_event_details'


class ProjectsOfPride(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    project_name = models.CharField(max_length=255, blank=True, null=True)
    project_address = models.CharField(max_length=255, blank=True, null=True)
    project_ward_no = models.IntegerField(blank=True, null=True)
    project_chief_name = models.CharField(max_length=255, blank=True, null=True)
    project_type = models.CharField(max_length=255, blank=True, null=True)
    project_total_budget = models.BigIntegerField(blank=True, null=True)
    project_physical_target = models.CharField(max_length=255, blank=True, null=True)
    project_progress_financial = models.BigIntegerField(blank=True, null=True)
    project_progress_physical = models.CharField(max_length=255, blank=True, null=True)
    project_other_information = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects_of_pride'


class PublicAndCommunityBuildings(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    building_name = models.CharField(max_length=255, blank=True, null=True)
    building_tole_name = models.CharField(max_length=255, blank=True, null=True)
    building_used_for = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.FloatField(blank=True, null=True)
    building_area = models.FloatField(blank=True, null=True)
    building_condition = models.CharField(max_length=255, blank=True, null=True)
    benefitting_household = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'public_and_community_buildings'


class PublicPondsAndFisheries(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    address_of_pond = models.CharField(max_length=255, blank=True, null=True)
    area_of_pond = models.IntegerField(blank=True, null=True)
    fish_production_yearly = models.IntegerField(blank=True, null=True)
    pond_ownership = models.CharField(max_length=255, blank=True, null=True)
    income_yearly = models.IntegerField(blank=True, null=True)
    rm_yearly_fees = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'public_ponds_and_fisheries'


class PublicServiceDelivery(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    service_delivery = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    ward_no = models.CharField(max_length=255, blank=True, null=True)
    satisfication_percentage = models.IntegerField(blank=True, null=True)
    satisfication_condition = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'public_service_delivery'


class Roadways(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    road_name = models.CharField(max_length=255, blank=True, null=True)
    road_begining_place = models.CharField(max_length=255, blank=True, null=True)
    road_ending_place = models.CharField(max_length=255, blank=True, null=True)
    road_length = models.IntegerField(blank=True, null=True)
    road_type = models.CharField(max_length=255, blank=True, null=True)
    road_rights_area = models.CharField(max_length=255, blank=True, null=True)
    road_benefited_population = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roadways'


class SavingsInformation(models.Model):
    parent_index = models.IntegerField(blank=True, null=True)
    saving_area = models.CharField(max_length=255, blank=True, null=True)
    saving_amount = models.IntegerField(blank=True, null=True)
    key_column = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'savings_information'


class SocialSecurityProgramDetails(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    sr_female = models.IntegerField(blank=True, null=True)
    sr_male = models.IntegerField(blank=True, null=True)
    sr_amount = models.BigIntegerField(blank=True, null=True)
    single_women = models.IntegerField(blank=True, null=True)
    single_women_amount = models.BigIntegerField(blank=True, null=True)
    complete_disabled_female = models.IntegerField(blank=True, null=True)
    complete_disabled_male = models.IntegerField(blank=True, null=True)
    complete_disabled_amount = models.BigIntegerField(blank=True, null=True)
    partial_disabled_female = models.IntegerField(blank=True, null=True)
    partial_disabled_male = models.IntegerField(blank=True, null=True)
    partial_disabled_amount = models.BigIntegerField(blank=True, null=True)
    child_protection_grant_female = models.IntegerField(blank=True, null=True)
    child_protection_grant_male = models.IntegerField(blank=True, null=True)
    child_protection_grant_amount = models.BigIntegerField(blank=True, null=True)
    dipressed_class_female = models.IntegerField(blank=True, null=True)
    dipressed_class_male = models.IntegerField(blank=True, null=True)
    dipressed_class_amount = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_security_program_details'


class SolidWasteManagement(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    solid_waste_type = models.CharField(max_length=255, blank=True, null=True)
    daily_production = models.IntegerField(blank=True, null=True)
    waste_collection_system = models.CharField(max_length=255, blank=True, null=True)
    management_system = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solid_waste_management'


class SourceOfAirPollution(models.Model):
    sn = models.SmallIntegerField(primary_key=True)
    air_pollution_source = models.CharField(max_length=255, blank=True, null=True)
    numbers = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=255, blank=True, null=True)
    fule_consumption_volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'source_of_air_pollution'


class YearlyCultivation(models.Model):
    parent_index = models.IntegerField(blank=True, null=True)
    cropname = models.CharField(max_length=255, blank=True, null=True)
    other_cropname = models.CharField(max_length=255, blank=True, null=True)
    production_volume = models.IntegerField(blank=True, null=True)
    cultivated_area = models.IntegerField(blank=True, null=True)
    sales_volume = models.IntegerField(blank=True, null=True)
    key_column = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'yearly_cultivation'
