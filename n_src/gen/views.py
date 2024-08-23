from flask_appbuilder import ModelView, MasterDetailView, MultipleView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.actions import action
from flask_appbuilder.security.decorators import has_access
from . import appbuilder, db
from .models import *


class AbPermissionView(ModelView):
    datamodel = SQLAInterface(AbPermission)
    list_title = 'Ab Permission List'
    show_title = 'Ab Permission Details'
    add_title = 'Add Ab Permission'
    edit_title = 'Edit Ab Permission'
    list_columns = ['id', 'name']
    label_columns = {'id': 'Id', 'name': 'Name'}
    search_columns = ['name']
    show_columns = ['id', 'name']
    add_columns = ['name']
    edit_columns = ['name']

    def __repr__(self):
        return self.name
    

class AbRegisterUserView(ModelView):
    datamodel = SQLAInterface(AbRegisterUser)
    list_title = 'Ab Register User List'
    show_title = 'Ab Register User Details'
    add_title = 'Add Ab Register User'
    edit_title = 'Edit Ab Register User'
    list_columns = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'registration_date', 'registration_hash']
    label_columns = {'id': 'Id', 'first_name': 'First Name', 'last_name': 'Last Name', 'username': 'Username', 'password': 'Password', 'email': 'Email', 'registration_date': 'Registration Date', 'registration_hash': 'Registration Hash'}
    search_columns = ['first_name', 'last_name', 'username', 'password', 'email', 'registration_hash']
    show_columns = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'registration_date', 'registration_hash']
    add_columns = ['first_name', 'last_name', 'username', 'password', 'email', 'registration_date', 'registration_hash']
    edit_columns = ['first_name', 'last_name', 'username', 'password', 'email', 'registration_date', 'registration_hash']

    def __repr__(self):
        return self.id
    

class AbRoleView(ModelView):
    datamodel = SQLAInterface(AbRole)
    list_title = 'Ab Role List'
    show_title = 'Ab Role Details'
    add_title = 'Add Ab Role'
    edit_title = 'Edit Ab Role'
    list_columns = ['id', 'name']
    label_columns = {'id': 'Id', 'name': 'Name'}
    search_columns = ['name']
    show_columns = ['id', 'name']
    add_columns = ['name']
    edit_columns = ['name']

    def __repr__(self):
        return self.name
    

class AbUserView(ModelView):
    datamodel = SQLAInterface(AbUser)
    list_title = 'Ab User List'
    show_title = 'Ab User Details'
    add_title = 'Add Ab User'
    edit_title = 'Edit Ab User'
    list_columns = ['id', 'first_name', 'last_name', 'username', 'password', 'active', 'email', 'last_login', 'login_count', 'fail_login_count', 'created_on', 'changed_on', 'created_by_fk', 'changed_by_fk']
    label_columns = {'id': 'Id', 'first_name': 'First Name', 'last_name': 'Last Name', 'username': 'Username', 'password': 'Password', 'active': 'Active', 'email': 'Email', 'last_login': 'Last Login', 'login_count': 'Login Count', 'fail_login_count': 'Fail Login Count', 'created_on': 'Created On', 'changed_on': 'Changed On', 'created_by_fk': 'Created By Fk', 'changed_by_fk': 'Changed By Fk'}
    search_columns = ['first_name', 'last_name', 'username', 'password', 'email']
    show_columns = ['id', 'first_name', 'last_name', 'username', 'password', 'active', 'email', 'last_login', 'login_count', 'fail_login_count', 'created_on', 'changed_on', 'created_by_fk', 'changed_by_fk']
    add_columns = ['first_name', 'last_name', 'username', 'password', 'active', 'email', 'last_login', 'login_count', 'fail_login_count', 'created_on', 'changed_on', 'created_by_fk', 'changed_by_fk']
    edit_columns = ['first_name', 'last_name', 'username', 'password', 'active', 'email', 'last_login', 'login_count', 'fail_login_count', 'created_on', 'changed_on', 'created_by_fk', 'changed_by_fk']

    def __repr__(self):
        return self.id
    

class AbViewMenuView(ModelView):
    datamodel = SQLAInterface(AbViewMenu)
    list_title = 'Ab View Menu List'
    show_title = 'Ab View Menu Details'
    add_title = 'Add Ab View Menu'
    edit_title = 'Edit Ab View Menu'
    list_columns = ['id', 'name']
    label_columns = {'id': 'Id', 'name': 'Name'}
    search_columns = ['name']
    show_columns = ['id', 'name']
    add_columns = ['name']
    edit_columns = ['name']

    def __repr__(self):
        return self.name
    

class AlternatenameView(ModelView):
    datamodel = SQLAInterface(Alternatename)
    list_title = 'Alternatename List'
    show_title = 'Alternatename Details'
    add_title = 'Add Alternatename'
    edit_title = 'Edit Alternatename'
    list_columns = ['id', 'isolanguage', 'alternatename', 'ispreferredname', 'isshortname', 'iscolloquial', 'ishistoric', 'name_from', 'name_to']
    label_columns = {'id': 'Id', 'isolanguage': 'Isolanguage', 'alternatename': 'Alternatename', 'ispreferredname': 'Ispreferredname', 'isshortname': 'Isshortname', 'iscolloquial': 'Iscolloquial', 'ishistoric': 'Ishistoric', 'name_from': 'Name From', 'name_to': 'Name To'}
    search_columns = ['isolanguage', 'alternatename', 'name_from', 'name_to']
    show_columns = ['id', 'isolanguage', 'alternatename', 'ispreferredname', 'isshortname', 'iscolloquial', 'ishistoric', 'name_from', 'name_to']
    add_columns = ['isolanguage', 'alternatename', 'ispreferredname', 'isshortname', 'iscolloquial', 'ishistoric', 'name_from', 'name_to']
    edit_columns = ['isolanguage', 'alternatename', 'ispreferredname', 'isshortname', 'iscolloquial', 'ishistoric', 'name_from', 'name_to']

    def __repr__(self):
        return self.id
    

class BadgeView(ModelView):
    datamodel = SQLAInterface(Badge)
    list_title = 'Badge List'
    show_title = 'Badge Details'
    add_title = 'Add Badge'
    edit_title = 'Edit Badge'
    list_columns = ['id', 'name', 'description', 'criteria', 'icon']
    label_columns = {'id': 'Id', 'name': 'Name', 'description': 'Description', 'criteria': 'Criteria', 'icon': 'Icon'}
    search_columns = ['name', 'description', 'criteria', 'icon']
    show_columns = ['id', 'name', 'description', 'criteria', 'icon']
    add_columns = ['name', 'description', 'criteria', 'icon']
    edit_columns = ['name', 'description', 'criteria', 'icon']

    def __repr__(self):
        return self.name
    

class ContactTypeView(ModelView):
    datamodel = SQLAInterface(ContactType)
    list_title = 'Contact Type List'
    show_title = 'Contact Type Details'
    add_title = 'Add Contact Type'
    edit_title = 'Edit Contact Type'
    list_columns = ['id', 'name', 'description', 'is_digital', 'requires_verification', 'max_length', 'icon_url', 'created_at', 'updated_at']
    label_columns = {'id': 'Id', 'name': 'Name', 'description': 'Description', 'is_digital': 'Is Digital', 'requires_verification': 'Requires Verification', 'max_length': 'Max Length', 'icon_url': 'Icon Url', 'created_at': 'Created At', 'updated_at': 'Updated At'}
    search_columns = ['name', 'description', 'icon_url']
    show_columns = ['id', 'name', 'description', 'is_digital', 'requires_verification', 'max_length', 'icon_url', 'created_at', 'updated_at']
    add_columns = ['name', 'description', 'is_digital', 'requires_verification', 'max_length', 'icon_url', 'created_at', 'updated_at']
    edit_columns = ['name', 'description', 'is_digital', 'requires_verification', 'max_length', 'icon_url', 'created_at', 'updated_at']

    def __repr__(self):
        return self.name
    

class CountryView(ModelView):
    datamodel = SQLAInterface(Country)
    list_title = 'Country List'
    show_title = 'Country Details'
    add_title = 'Add Country'
    edit_title = 'Edit Country'
    list_columns = ['id', 'iso_alpha2', 'iso_alpha3', 'iso_numeric', 'fips_code', 'name', 'capital', 'areainsqkm', 'population', 'continent', 'tld', 'currencycode', 'currencyname', 'phone', 'postalcode', 'postalcoderegex', 'languages', 'geo_id_fk', 'neighbors', 'equivfipscode', 'flag']
    label_columns = {'id': 'Id', 'iso_alpha2': 'Iso Alpha2', 'iso_alpha3': 'Iso Alpha3', 'iso_numeric': 'Iso Numeric', 'fips_code': 'Fips Code', 'name': 'Name', 'capital': 'Capital', 'areainsqkm': 'Areainsqkm', 'population': 'Population', 'continent': 'Continent', 'tld': 'Tld', 'currencycode': 'Currencycode', 'currencyname': 'Currencyname', 'phone': 'Phone', 'postalcode': 'Postalcode', 'postalcoderegex': 'Postalcoderegex', 'languages': 'Languages', 'geo_id_fk': 'Geo Id Fk', 'neighbors': 'Neighbors', 'equivfipscode': 'Equivfipscode', 'flag': 'Flag'}
    search_columns = ['iso_alpha2', 'iso_alpha3', 'fips_code', 'name', 'capital', 'continent', 'tld', 'currencycode', 'currencyname', 'phone', 'postalcode', 'postalcoderegex', 'languages', 'neighbors', 'equivfipscode', 'flag']
    show_columns = ['id', 'iso_alpha2', 'iso_alpha3', 'iso_numeric', 'fips_code', 'name', 'capital', 'areainsqkm', 'population', 'continent', 'tld', 'currencycode', 'currencyname', 'phone', 'postalcode', 'postalcoderegex', 'languages', 'geo_id_fk', 'neighbors', 'equivfipscode', 'flag']
    add_columns = ['iso_alpha2', 'iso_alpha3', 'iso_numeric', 'fips_code', 'name', 'capital', 'areainsqkm', 'population', 'continent', 'tld', 'currencycode', 'currencyname', 'phone', 'postalcode', 'postalcoderegex', 'languages', 'geo_id_fk', 'neighbors', 'equivfipscode', 'flag']
    edit_columns = ['iso_alpha2', 'iso_alpha3', 'iso_numeric', 'fips_code', 'name', 'capital', 'areainsqkm', 'population', 'continent', 'tld', 'currencycode', 'currencyname', 'phone', 'postalcode', 'postalcoderegex', 'languages', 'geo_id_fk', 'neighbors', 'equivfipscode', 'flag']

    def __repr__(self):
        return self.name
    

class CurrencyView(ModelView):
    datamodel = SQLAInterface(Currency)
    list_title = 'Currency List'
    show_title = 'Currency Details'
    add_title = 'Add Currency'
    edit_title = 'Edit Currency'
    list_columns = ['id', 'name', 'symbol', 'numeric_code', 'full_name']
    label_columns = {'id': 'Id', 'name': 'Name', 'symbol': 'Symbol', 'numeric_code': 'Numeric Code', 'full_name': 'Full Name'}
    search_columns = ['name', 'symbol', 'numeric_code', 'full_name']
    show_columns = ['id', 'name', 'symbol', 'numeric_code', 'full_name']
    add_columns = ['name', 'symbol', 'numeric_code', 'full_name']
    edit_columns = ['name', 'symbol', 'numeric_code', 'full_name']

    def __repr__(self):
        return self.name
    

class FeaturecodesView(ModelView):
    datamodel = SQLAInterface(Featurecodes)
    list_title = 'Featurecodes List'
    show_title = 'Featurecodes Details'
    add_title = 'Add Featurecodes'
    edit_title = 'Edit Featurecodes'
    list_columns = ['id', 'code', 'fclass', 'fcode', 'label', 'description']
    label_columns = {'id': 'Id', 'code': 'Code', 'fclass': 'Fclass', 'fcode': 'Fcode', 'label': 'Label', 'description': 'Description'}
    search_columns = ['code', 'fclass', 'fcode', 'label', 'description']
    show_columns = ['id', 'code', 'fclass', 'fcode', 'label', 'description']
    add_columns = ['code', 'fclass', 'fcode', 'label', 'description']
    edit_columns = ['code', 'fclass', 'fcode', 'label', 'description']

    def __repr__(self):
        return self.label
    

class GeonameView(ModelView):
    datamodel = SQLAInterface(Geoname)
    list_title = 'Geoname List'
    show_title = 'Geoname Details'
    add_title = 'Add Geoname'
    edit_title = 'Edit Geoname'
    list_columns = ['id', 'name', 'asciiname', 'alt_names', 'alternatenames_id_fk', 'latitude', 'longitude', 'fclass', 'fcode', 'countrycode', 'country_id_fk', 'cc2', 'admin1', 'admin2', 'admin3', 'admin4', 'population', 'elevation', 'gtopo30', 'timezone', 'moddate']
    label_columns = {'id': 'Id', 'name': 'Name', 'asciiname': 'Asciiname', 'alt_names': 'Alt Names', 'alternatenames_id_fk': 'Alternatenames Id Fk', 'latitude': 'Latitude', 'longitude': 'Longitude', 'fclass': 'Fclass', 'fcode': 'Fcode', 'countrycode': 'Countrycode', 'country_id_fk': 'Country Id Fk', 'cc2': 'Cc2', 'admin1': 'Admin1', 'admin2': 'Admin2', 'admin3': 'Admin3', 'admin4': 'Admin4', 'population': 'Population', 'elevation': 'Elevation', 'gtopo30': 'Gtopo30', 'timezone': 'Timezone', 'moddate': 'Moddate'}
    search_columns = ['name', 'asciiname', 'alt_names', 'fclass', 'fcode', 'countrycode', 'cc2', 'admin1', 'admin2', 'admin3', 'admin4', 'timezone']
    show_columns = ['id', 'name', 'asciiname', 'alt_names', 'alternatenames_id_fk', 'latitude', 'longitude', 'fclass', 'fcode', 'countrycode', 'country_id_fk', 'cc2', 'admin1', 'admin2', 'admin3', 'admin4', 'population', 'elevation', 'gtopo30', 'timezone', 'moddate']
    add_columns = ['name', 'asciiname', 'alt_names', 'alternatenames_id_fk', 'latitude', 'longitude', 'fclass', 'fcode', 'countrycode', 'country_id_fk', 'cc2', 'admin1', 'admin2', 'admin3', 'admin4', 'population', 'elevation', 'gtopo30', 'timezone', 'moddate']
    edit_columns = ['name', 'asciiname', 'alt_names', 'alternatenames_id_fk', 'latitude', 'longitude', 'fclass', 'fcode', 'countrycode', 'country_id_fk', 'cc2', 'admin1', 'admin2', 'admin3', 'admin4', 'population', 'elevation', 'gtopo30', 'timezone', 'moddate']

    def __repr__(self):
        return self.name
    

class LanguagecodesView(ModelView):
    datamodel = SQLAInterface(Languagecodes)
    list_title = 'Languagecodes List'
    show_title = 'Languagecodes Details'
    add_title = 'Add Languagecodes'
    edit_title = 'Edit Languagecodes'
    list_columns = ['id', 'iso_639_3', 'iso_639_2', 'iso_639_1', 'name']
    label_columns = {'id': 'Id', 'iso_639_3': 'Iso 639 3', 'iso_639_2': 'Iso 639 2', 'iso_639_1': 'Iso 639 1', 'name': 'Name'}
    search_columns = ['iso_639_3', 'iso_639_2', 'iso_639_1', 'name']
    show_columns = ['id', 'iso_639_3', 'iso_639_2', 'iso_639_1', 'name']
    add_columns = ['iso_639_3', 'iso_639_2', 'iso_639_1', 'name']
    edit_columns = ['iso_639_3', 'iso_639_2', 'iso_639_1', 'name']

    def __repr__(self):
        return self.name
    

class PersonView(ModelView):
    datamodel = SQLAInterface(Person)
    list_title = 'Person List'
    show_title = 'Person Details'
    add_title = 'Add Person'
    edit_title = 'Edit Person'
    list_columns = ['id', 'first_name', 'middle_name', 'last_name', 'full_name', 'nick_name', 'headline', 'location', 'summary', 'email', 'phone', 'date_of_birth', 'city', 'state_province', 'postal_code', 'country', 'bio', 'skills_description', 'interests', 'is_volunteer', 'is_staff', 'onboarding_step', 'profile_completion', 'last_profile_update', 'points', 'level', 'social_media_imported']
    label_columns = {'id': 'Id', 'first_name': 'First Name', 'middle_name': 'Middle Name', 'last_name': 'Last Name', 'full_name': 'Full Name', 'nick_name': 'Nick Name', 'headline': 'Headline', 'location': 'Location', 'summary': 'Summary', 'email': 'Email', 'phone': 'Phone', 'date_of_birth': 'Date Of Birth', 'city': 'City', 'state_province': 'State Province', 'postal_code': 'Postal Code', 'country': 'Country', 'bio': 'Bio', 'skills_description': 'Skills Description', 'interests': 'Interests', 'is_volunteer': 'Is Volunteer', 'is_staff': 'Is Staff', 'onboarding_step': 'Onboarding Step', 'profile_completion': 'Profile Completion', 'last_profile_update': 'Last Profile Update', 'points': 'Points', 'level': 'Level', 'social_media_imported': 'Social Media Imported'}
    search_columns = ['first_name', 'middle_name', 'last_name', 'full_name', 'nick_name', 'headline', 'location', 'summary', 'email', 'phone', 'city', 'state_province', 'postal_code', 'country', 'bio', 'skills_description', 'interests']
    show_columns = ['id', 'first_name', 'middle_name', 'last_name', 'full_name', 'nick_name', 'headline', 'location', 'summary', 'email', 'phone', 'date_of_birth', 'city', 'state_province', 'postal_code', 'country', 'bio', 'skills_description', 'interests', 'is_volunteer', 'is_staff', 'onboarding_step', 'profile_completion', 'last_profile_update', 'points', 'level', 'social_media_imported']
    add_columns = ['first_name', 'middle_name', 'last_name', 'full_name', 'nick_name', 'headline', 'location', 'summary', 'email', 'phone', 'date_of_birth', 'city', 'state_province', 'postal_code', 'country', 'bio', 'skills_description', 'interests', 'is_volunteer', 'is_staff', 'onboarding_step', 'profile_completion', 'last_profile_update', 'points', 'level', 'social_media_imported']
    edit_columns = ['first_name', 'middle_name', 'last_name', 'full_name', 'nick_name', 'headline', 'location', 'summary', 'email', 'phone', 'date_of_birth', 'city', 'state_province', 'postal_code', 'country', 'bio', 'skills_description', 'interests', 'is_volunteer', 'is_staff', 'onboarding_step', 'profile_completion', 'last_profile_update', 'points', 'level', 'social_media_imported']

    def __repr__(self):
        return self.id
    

class ScrapingTargetsView(ModelView):
    datamodel = SQLAInterface(ScrapingTargets)
    list_title = 'Scraping Targets List'
    show_title = 'Scraping Targets Details'
    add_title = 'Add Scraping Targets'
    edit_title = 'Edit Scraping Targets'
    list_columns = ['id', 'url', 'name', 'category', 'frequency', 'priority', 'requires_auth', 'auth_username', '_auth_password', 'is_active', 'created_at', 'updated_at', 'scraping_rule_version']
    label_columns = {'id': 'Id', 'url': 'Url', 'name': 'Name', 'category': 'Category', 'frequency': 'Frequency', 'priority': 'Priority', 'requires_auth': 'Requires Auth', 'auth_username': 'Auth Username', '_auth_password': ' Auth Password', 'is_active': 'Is Active', 'created_at': 'Created At', 'updated_at': 'Updated At', 'scraping_rule_version': 'Scraping Rule Version'}
    search_columns = ['url', 'name', 'category', 'frequency', 'auth_username', '_auth_password', 'scraping_rule_version']
    show_columns = ['id', 'url', 'name', 'category', 'frequency', 'priority', 'requires_auth', 'auth_username', '_auth_password', 'is_active', 'created_at', 'updated_at', 'scraping_rule_version']
    add_columns = ['url', 'name', 'category', 'frequency', 'priority', 'requires_auth', 'auth_username', '_auth_password', 'is_active', 'created_at', 'updated_at', 'scraping_rule_version']
    edit_columns = ['url', 'name', 'category', 'frequency', 'priority', 'requires_auth', 'auth_username', '_auth_password', 'is_active', 'created_at', 'updated_at', 'scraping_rule_version']

    def __repr__(self):
        return self.name
    

class SkillCategoryView(ModelView):
    datamodel = SQLAInterface(SkillCategory)
    list_title = 'Skill Category List'
    show_title = 'Skill Category Details'
    add_title = 'Add Skill Category'
    edit_title = 'Edit Skill Category'
    list_columns = ['id', 'name', 'description']
    label_columns = {'id': 'Id', 'name': 'Name', 'description': 'Description'}
    search_columns = ['name', 'description']
    show_columns = ['id', 'name', 'description']
    add_columns = ['name', 'description']
    edit_columns = ['name', 'description']

    def __repr__(self):
        return self.name
    

class TagView(ModelView):
    datamodel = SQLAInterface(Tag)
    list_title = 'Tag List'
    show_title = 'Tag Details'
    add_title = 'Add Tag'
    edit_title = 'Edit Tag'
    list_columns = ['id', 'name']
    label_columns = {'id': 'Id', 'name': 'Name'}
    search_columns = ['name']
    show_columns = ['id', 'name']
    add_columns = ['name']
    edit_columns = ['name']

    def __repr__(self):
        return self.name
    

class AbPermissionViewView(ModelView):
    datamodel = SQLAInterface(AbPermissionView)
    list_title = 'Ab Permission View List'
    show_title = 'Ab Permission View Details'
    add_title = 'Add Ab Permission View'
    edit_title = 'Edit Ab Permission View'
    list_columns = ['id']
    label_columns = {'id': 'Id', 'permission_id': 'Permission Id', 'view_menu_id': 'View Menu Id'}
    search_columns = []
    show_columns = ['id', 'permission_id', 'view_menu_id']
    add_columns = []
    edit_columns = ['permission_id', 'view_menu_id']

    def __repr__(self):
        return self.id
    

class AbUserRoleView(ModelView):
    datamodel = SQLAInterface(AbUserRole)
    list_title = 'Ab User Role List'
    show_title = 'Ab User Role Details'
    add_title = 'Add Ab User Role'
    edit_title = 'Edit Ab User Role'
    list_columns = ['id']
    label_columns = {'id': 'Id', 'user_id': 'User Id', 'role_id': 'Role Id'}
    search_columns = []
    show_columns = ['id', 'user_id', 'role_id']
    add_columns = []
    edit_columns = ['user_id', 'role_id']

    def __repr__(self):
        return self.id
    

class Admin1codesView(ModelView):
    datamodel = SQLAInterface(Admin1codes)
    list_title = 'Admin1codes List'
    show_title = 'Admin1codes Details'
    add_title = 'Add Admin1codes'
    edit_title = 'Edit Admin1codes'
    list_columns = ['id', 'code', 'country_id_fk', 'admin1_code', 'name', 'alt_name_english', 'geo_id_fk']
    label_columns = {'id': 'Id', 'code': 'Code', 'country_id_fk': 'Country Id Fk', 'admin1_code': 'Admin1 Code', 'name': 'Name', 'alt_name_english': 'Alt Name English', 'geo_id_fk': 'Geo Id Fk'}
    search_columns = ['code', 'admin1_code', 'name', 'alt_name_english']
    show_columns = ['id', 'code', 'country_id_fk', 'admin1_code', 'name', 'alt_name_english', 'geo_id_fk']
    add_columns = ['code', 'country_id_fk', 'admin1_code', 'name', 'alt_name_english', 'geo_id_fk']
    edit_columns = ['code', 'country_id_fk', 'admin1_code', 'name', 'alt_name_english', 'geo_id_fk']

    def __repr__(self):
        return self.name
    

class Admin2codesView(ModelView):
    datamodel = SQLAInterface(Admin2codes)
    list_title = 'Admin2codes List'
    show_title = 'Admin2codes Details'
    add_title = 'Add Admin2codes'
    edit_title = 'Edit Admin2codes'
    list_columns = ['id', 'code', 'country_id_fk', 'admin1_code', 'name', 'alt_name_english', 'geo_id_fk']
    label_columns = {'id': 'Id', 'code': 'Code', 'country_id_fk': 'Country Id Fk', 'admin1_code': 'Admin1 Code', 'name': 'Name', 'alt_name_english': 'Alt Name English', 'geo_id_fk': 'Geo Id Fk'}
    search_columns = ['code', 'admin1_code', 'name', 'alt_name_english']
    show_columns = ['id', 'code', 'country_id_fk', 'admin1_code', 'name', 'alt_name_english', 'geo_id_fk']
    add_columns = ['code', 'country_id_fk', 'admin1_code', 'name', 'alt_name_english', 'geo_id_fk']
    edit_columns = ['code', 'country_id_fk', 'admin1_code', 'name', 'alt_name_english', 'geo_id_fk']

    def __repr__(self):
        return self.name
    

class ContactView(ModelView):
    datamodel = SQLAInterface(Contact)
    list_title = 'Contact List'
    show_title = 'Contact Details'
    add_title = 'Add Contact'
    edit_title = 'Edit Contact'
    list_columns = ['id', 'person_id_fk', 'contact_type_id_fk', 'contact_value', 'priority', 'best_time_to_contact_start', 'best_time_to_contact_end', 'active_from_date', 'active_to_date', 'for_business_use', 'for_personal_use', 'do_not_use', 'is_active', 'is_blocked', 'is_verified', 'notes']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'contact_type_id_fk': 'Contact Type Id Fk', 'contact_value': 'Contact Value', 'priority': 'Priority', 'best_time_to_contact_start': 'Best Time To Contact Start', 'best_time_to_contact_end': 'Best Time To Contact End', 'active_from_date': 'Active From Date', 'active_to_date': 'Active To Date', 'for_business_use': 'For Business Use', 'for_personal_use': 'For Personal Use', 'do_not_use': 'Do Not Use', 'is_active': 'Is Active', 'is_blocked': 'Is Blocked', 'is_verified': 'Is Verified', 'notes': 'Notes'}
    search_columns = ['contact_value', 'notes']
    show_columns = ['id', 'person_id_fk', 'contact_type_id_fk', 'contact_value', 'priority', 'best_time_to_contact_start', 'best_time_to_contact_end', 'active_from_date', 'active_to_date', 'for_business_use', 'for_personal_use', 'do_not_use', 'is_active', 'is_blocked', 'is_verified', 'notes']
    add_columns = ['person_id_fk', 'contact_type_id_fk', 'contact_value', 'priority', 'best_time_to_contact_start', 'best_time_to_contact_end', 'active_from_date', 'active_to_date', 'for_business_use', 'for_personal_use', 'do_not_use', 'is_active', 'is_blocked', 'is_verified', 'notes']
    edit_columns = ['person_id_fk', 'contact_type_id_fk', 'contact_value', 'priority', 'best_time_to_contact_start', 'best_time_to_contact_end', 'active_from_date', 'active_to_date', 'for_business_use', 'for_personal_use', 'do_not_use', 'is_active', 'is_blocked', 'is_verified', 'notes']

    def __repr__(self):
        return self.id
    

class GamificationChallengeView(ModelView):
    datamodel = SQLAInterface(GamificationChallenge)
    list_title = 'Gamification Challenge List'
    show_title = 'Gamification Challenge Details'
    add_title = 'Add Gamification Challenge'
    edit_title = 'Edit Gamification Challenge'
    list_columns = ['id', 'name', 'description', 'points_reward', 'badge_reward_id_fk', 'start_date', 'end_date']
    label_columns = {'id': 'Id', 'name': 'Name', 'description': 'Description', 'points_reward': 'Points Reward', 'badge_reward_id_fk': 'Badge Reward Id Fk', 'start_date': 'Start Date', 'end_date': 'End Date'}
    search_columns = ['name', 'description']
    show_columns = ['id', 'name', 'description', 'points_reward', 'badge_reward_id_fk', 'start_date', 'end_date']
    add_columns = ['name', 'description', 'points_reward', 'badge_reward_id_fk', 'start_date', 'end_date']
    edit_columns = ['name', 'description', 'points_reward', 'badge_reward_id_fk', 'start_date', 'end_date']

    def __repr__(self):
        return self.name
    

class LeaderboardView(ModelView):
    datamodel = SQLAInterface(Leaderboard)
    list_title = 'Leaderboard List'
    show_title = 'Leaderboard Details'
    add_title = 'Add Leaderboard'
    edit_title = 'Edit Leaderboard'
    list_columns = ['id', 'person_id_fk', 'score', 'last_updated']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'score': 'Score', 'last_updated': 'Last Updated'}
    search_columns = []
    show_columns = ['id', 'person_id_fk', 'score', 'last_updated']
    add_columns = ['person_id_fk', 'score', 'last_updated']
    edit_columns = ['person_id_fk', 'score', 'last_updated']

    def __repr__(self):
        return self.id
    

class MessageView(ModelView):
    datamodel = SQLAInterface(Message)
    list_title = 'Message List'
    show_title = 'Message Details'
    add_title = 'Add Message'
    edit_title = 'Edit Message'
    list_columns = ['id', 'sender_id_fk', 'recipient_id_fk', 'subject', 'body', 'sent_date', 'read_date']
    label_columns = {'id': 'Id', 'sender_id_fk': 'Sender Id Fk', 'recipient_id_fk': 'Recipient Id Fk', 'subject': 'Subject', 'body': 'Body', 'sent_date': 'Sent Date', 'read_date': 'Read Date'}
    search_columns = ['subject', 'body']
    show_columns = ['id', 'sender_id_fk', 'recipient_id_fk', 'subject', 'body', 'sent_date', 'read_date']
    add_columns = ['sender_id_fk', 'recipient_id_fk', 'subject', 'body', 'sent_date', 'read_date']
    edit_columns = ['sender_id_fk', 'recipient_id_fk', 'subject', 'body', 'sent_date', 'read_date']

    def __repr__(self):
        return self.id
    

class NotificationView(ModelView):
    datamodel = SQLAInterface(Notification)
    list_title = 'Notification List'
    show_title = 'Notification Details'
    add_title = 'Add Notification'
    edit_title = 'Edit Notification'
    list_columns = ['id', 'person_id_fk', 'message', 'notification_type', 'created_date', 'read_date']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'message': 'Message', 'notification_type': 'Notification Type', 'created_date': 'Created Date', 'read_date': 'Read Date'}
    search_columns = ['message', 'notification_type']
    show_columns = ['id', 'person_id_fk', 'message', 'notification_type', 'created_date', 'read_date']
    add_columns = ['person_id_fk', 'message', 'notification_type', 'created_date', 'read_date']
    edit_columns = ['person_id_fk', 'message', 'notification_type', 'created_date', 'read_date']

    def __repr__(self):
        return self.id
    

class OrganizationView(ModelView):
    datamodel = SQLAInterface(Organization)
    list_title = 'Organization List'
    show_title = 'Organization Details'
    add_title = 'Add Organization'
    edit_title = 'Edit Organization'
    list_columns = ['id', 'name', 'legal_name', 'org_type', 'org_cat', 'status', 'industry', 'website', 'is_verified', 'description', 'mission_statement', 'size', 'revenue', 'founded_date', 'country_of_operation_id_fk', 'logo', 'social_media_links', 'registration_number', 'seeking_funding', 'providing_funding', 'authorized_representative', 'legal_structure', 'compliance_status', 'financial_year_end', 'last_audit_date', 'auditor_name', 'phone_number', 'email', 'address', 'city', 'state', 'country', 'postal_code', 'board_members', 'governance_structure', 'risk_assessment', 'insurance_coverage', 'compliance_certifications', 'ethics_policy', 'sustainability_policy', 'primary_funding_source', 'secondary_funding_source', 'main_areas_of_operation', 'key_programs', 'beneficiary_info', 'major_donors', 'partnerships_affiliations', 'onboarding_step', 'profile_completion', 'last_profile_update', 'associated_people_id_fk']
    label_columns = {'id': 'Id', 'name': 'Name', 'legal_name': 'Legal Name', 'org_type': 'Org Type', 'org_cat': 'Org Cat', 'status': 'Status', 'industry': 'Industry', 'website': 'Website', 'is_verified': 'Is Verified', 'description': 'Description', 'mission_statement': 'Mission Statement', 'size': 'Size', 'revenue': 'Revenue', 'founded_date': 'Founded Date', 'country_of_operation_id_fk': 'Country Of Operation Id Fk', 'logo': 'Logo', 'social_media_links': 'Social Media Links', 'tax_id': 'Tax Id', 'registration_number': 'Registration Number', 'seeking_funding': 'Seeking Funding', 'providing_funding': 'Providing Funding', 'authorized_representative': 'Authorized Representative', 'legal_structure': 'Legal Structure', 'compliance_status': 'Compliance Status', 'financial_year_end': 'Financial Year End', 'last_audit_date': 'Last Audit Date', 'auditor_name': 'Auditor Name', 'phone_number': 'Phone Number', 'email': 'Email', 'address': 'Address', 'city': 'City', 'state': 'State', 'country': 'Country', 'postal_code': 'Postal Code', 'board_members': 'Board Members', 'governance_structure': 'Governance Structure', 'risk_assessment': 'Risk Assessment', 'insurance_coverage': 'Insurance Coverage', 'compliance_certifications': 'Compliance Certifications', 'ethics_policy': 'Ethics Policy', 'sustainability_policy': 'Sustainability Policy', 'primary_funding_source': 'Primary Funding Source', 'secondary_funding_source': 'Secondary Funding Source', 'main_areas_of_operation': 'Main Areas Of Operation', 'key_programs': 'Key Programs', 'beneficiary_info': 'Beneficiary Info', 'major_donors': 'Major Donors', 'partnerships_affiliations': 'Partnerships Affiliations', 'onboarding_step': 'Onboarding Step', 'profile_completion': 'Profile Completion', 'last_profile_update': 'Last Profile Update', 'associated_people_id_fk': 'Associated People Id Fk'}
    search_columns = ['name', 'legal_name', 'org_type', 'org_cat', 'status', 'industry', 'website', 'description', 'mission_statement', 'logo', 'social_media_links', 'tax_id', 'registration_number', 'legal_structure', 'compliance_status', 'auditor_name', 'phone_number', 'email', 'address', 'city', 'state', 'country', 'postal_code', 'board_members', 'governance_structure', 'risk_assessment', 'compliance_certifications', 'ethics_policy', 'sustainability_policy', 'primary_funding_source', 'secondary_funding_source', 'main_areas_of_operation', 'key_programs', 'beneficiary_info', 'major_donors', 'partnerships_affiliations']
    show_columns = ['id', 'name', 'legal_name', 'org_type', 'org_cat', 'status', 'industry', 'website', 'is_verified', 'description', 'mission_statement', 'size', 'revenue', 'founded_date', 'country_of_operation_id_fk', 'logo', 'social_media_links', 'tax_id', 'registration_number', 'seeking_funding', 'providing_funding', 'authorized_representative', 'legal_structure', 'compliance_status', 'financial_year_end', 'last_audit_date', 'auditor_name', 'phone_number', 'email', 'address', 'city', 'state', 'country', 'postal_code', 'board_members', 'governance_structure', 'risk_assessment', 'insurance_coverage', 'compliance_certifications', 'ethics_policy', 'sustainability_policy', 'primary_funding_source', 'secondary_funding_source', 'main_areas_of_operation', 'key_programs', 'beneficiary_info', 'major_donors', 'partnerships_affiliations', 'onboarding_step', 'profile_completion', 'last_profile_update', 'associated_people_id_fk']
    add_columns = ['name', 'legal_name', 'org_type', 'org_cat', 'status', 'industry', 'website', 'is_verified', 'description', 'mission_statement', 'size', 'revenue', 'founded_date', 'country_of_operation_id_fk', 'logo', 'social_media_links', 'registration_number', 'seeking_funding', 'providing_funding', 'authorized_representative', 'legal_structure', 'compliance_status', 'financial_year_end', 'last_audit_date', 'auditor_name', 'phone_number', 'email', 'address', 'city', 'state', 'country', 'postal_code', 'board_members', 'governance_structure', 'risk_assessment', 'insurance_coverage', 'compliance_certifications', 'ethics_policy', 'sustainability_policy', 'primary_funding_source', 'secondary_funding_source', 'main_areas_of_operation', 'key_programs', 'beneficiary_info', 'major_donors', 'partnerships_affiliations', 'onboarding_step', 'profile_completion', 'last_profile_update', 'associated_people_id_fk']
    edit_columns = ['name', 'legal_name', 'org_type', 'org_cat', 'status', 'industry', 'website', 'is_verified', 'description', 'mission_statement', 'size', 'revenue', 'founded_date', 'country_of_operation_id_fk', 'logo', 'social_media_links', 'tax_id', 'registration_number', 'seeking_funding', 'providing_funding', 'authorized_representative', 'legal_structure', 'compliance_status', 'financial_year_end', 'last_audit_date', 'auditor_name', 'phone_number', 'email', 'address', 'city', 'state', 'country', 'postal_code', 'board_members', 'governance_structure', 'risk_assessment', 'insurance_coverage', 'compliance_certifications', 'ethics_policy', 'sustainability_policy', 'primary_funding_source', 'secondary_funding_source', 'main_areas_of_operation', 'key_programs', 'beneficiary_info', 'major_donors', 'partnerships_affiliations', 'onboarding_step', 'profile_completion', 'last_profile_update', 'associated_people_id_fk']

    def __repr__(self):
        return self.name
    

class PersonBadgeView(ModelView):
    datamodel = SQLAInterface(PersonBadge)
    list_title = 'Person Badge List'
    show_title = 'Person Badge Details'
    add_title = 'Add Person Badge'
    edit_title = 'Edit Person Badge'
    list_columns = ['person_id_fk', 'badge_id_fk', 'date_earned']
    label_columns = {'person_id_fk': 'Person Id Fk', 'badge_id_fk': 'Badge Id Fk', 'date_earned': 'Date Earned'}
    search_columns = []
    show_columns = ['person_id_fk', 'badge_id_fk', 'date_earned']
    add_columns = ['person_id_fk', 'badge_id_fk', 'date_earned']
    edit_columns = ['person_id_fk', 'badge_id_fk', 'date_earned']

    def __repr__(self):
        return self.person_id_fk
    

class PersonCertificationView(ModelView):
    datamodel = SQLAInterface(PersonCertification)
    list_title = 'Person Certification List'
    show_title = 'Person Certification Details'
    add_title = 'Add Person Certification'
    edit_title = 'Edit Person Certification'
    list_columns = ['id', 'person_id_fk', 'name', 'issuing_organization', 'issue_date', 'expiration_date', 'credential_url']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'name': 'Name', 'issuing_organization': 'Issuing Organization', 'issue_date': 'Issue Date', 'expiration_date': 'Expiration Date', 'credential_id': 'Credential Id', 'credential_url': 'Credential Url'}
    search_columns = ['name', 'issuing_organization', 'credential_id', 'credential_url']
    show_columns = ['id', 'person_id_fk', 'name', 'issuing_organization', 'issue_date', 'expiration_date', 'credential_id', 'credential_url']
    add_columns = ['person_id_fk', 'name', 'issuing_organization', 'issue_date', 'expiration_date', 'credential_url']
    edit_columns = ['person_id_fk', 'name', 'issuing_organization', 'issue_date', 'expiration_date', 'credential_id', 'credential_url']

    def __repr__(self):
        return self.name
    

class PersonCourseView(ModelView):
    datamodel = SQLAInterface(PersonCourse)
    list_title = 'Person Course List'
    show_title = 'Person Course Details'
    add_title = 'Add Person Course'
    edit_title = 'Edit Person Course'
    list_columns = ['id', 'person_id_fk', 'name', 'institution', 'completion_date', 'description']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'name': 'Name', 'institution': 'Institution', 'completion_date': 'Completion Date', 'description': 'Description'}
    search_columns = ['name', 'institution', 'description']
    show_columns = ['id', 'person_id_fk', 'name', 'institution', 'completion_date', 'description']
    add_columns = ['person_id_fk', 'name', 'institution', 'completion_date', 'description']
    edit_columns = ['person_id_fk', 'name', 'institution', 'completion_date', 'description']

    def __repr__(self):
        return self.name
    

class PersonEducationView(ModelView):
    datamodel = SQLAInterface(PersonEducation)
    list_title = 'Person Education List'
    show_title = 'Person Education Details'
    add_title = 'Add Person Education'
    edit_title = 'Edit Person Education'
    list_columns = ['id', 'person_id_fk', 'school_name', 'degree', 'field_of_study', 'start_date', 'end_date', 'description']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'school_name': 'School Name', 'degree': 'Degree', 'field_of_study': 'Field Of Study', 'start_date': 'Start Date', 'end_date': 'End Date', 'description': 'Description'}
    search_columns = ['school_name', 'degree', 'field_of_study', 'description']
    show_columns = ['id', 'person_id_fk', 'school_name', 'degree', 'field_of_study', 'start_date', 'end_date', 'description']
    add_columns = ['person_id_fk', 'school_name', 'degree', 'field_of_study', 'start_date', 'end_date', 'description']
    edit_columns = ['person_id_fk', 'school_name', 'degree', 'field_of_study', 'start_date', 'end_date', 'description']

    def __repr__(self):
        return self.id
    

class PersonExperienceView(ModelView):
    datamodel = SQLAInterface(PersonExperience)
    list_title = 'Person Experience List'
    show_title = 'Person Experience Details'
    add_title = 'Add Person Experience'
    edit_title = 'Edit Person Experience'
    list_columns = ['id', 'person_id_fk', 'job_title', 'company_name', 'location', 'start_date', 'end_date', 'description', 'awards']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'job_title': 'Job Title', 'company_name': 'Company Name', 'location': 'Location', 'start_date': 'Start Date', 'end_date': 'End Date', 'description': 'Description', 'awards': 'Awards'}
    search_columns = ['job_title', 'company_name', 'location', 'description', 'awards']
    show_columns = ['id', 'person_id_fk', 'job_title', 'company_name', 'location', 'start_date', 'end_date', 'description', 'awards']
    add_columns = ['person_id_fk', 'job_title', 'company_name', 'location', 'start_date', 'end_date', 'description', 'awards']
    edit_columns = ['person_id_fk', 'job_title', 'company_name', 'location', 'start_date', 'end_date', 'description', 'awards']

    def __repr__(self):
        return self.id
    

class PersonHonorAwardView(ModelView):
    datamodel = SQLAInterface(PersonHonorAward)
    list_title = 'Person Honor Award List'
    show_title = 'Person Honor Award Details'
    add_title = 'Add Person Honor Award'
    edit_title = 'Edit Person Honor Award'
    list_columns = ['id', 'person_id_fk', 'title', 'issuer', 'date_received', 'description']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'title': 'Title', 'issuer': 'Issuer', 'date_received': 'Date Received', 'description': 'Description'}
    search_columns = ['title', 'issuer', 'description']
    show_columns = ['id', 'person_id_fk', 'title', 'issuer', 'date_received', 'description']
    add_columns = ['person_id_fk', 'title', 'issuer', 'date_received', 'description']
    edit_columns = ['person_id_fk', 'title', 'issuer', 'date_received', 'description']

    def __repr__(self):
        return self.title
    

class PersonLanguageView(ModelView):
    datamodel = SQLAInterface(PersonLanguage)
    list_title = 'Person Language List'
    show_title = 'Person Language Details'
    add_title = 'Add Person Language'
    edit_title = 'Edit Person Language'
    list_columns = ['id', 'person_id_fk', 'name', 'proficiency']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'name': 'Name', 'proficiency': 'Proficiency'}
    search_columns = ['name', 'proficiency']
    show_columns = ['id', 'person_id_fk', 'name', 'proficiency']
    add_columns = ['person_id_fk', 'name', 'proficiency']
    edit_columns = ['person_id_fk', 'name', 'proficiency']

    def __repr__(self):
        return self.name
    

class PersonOrganizationMembershipView(ModelView):
    datamodel = SQLAInterface(PersonOrganizationMembership)
    list_title = 'Person Organization Membership List'
    show_title = 'Person Organization Membership Details'
    add_title = 'Add Person Organization Membership'
    edit_title = 'Edit Person Organization Membership'
    list_columns = ['id', 'person_id_fk', 'organization_name', 'role', 'start_date', 'end_date', 'description']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'organization_name': 'Organization Name', 'role': 'Role', 'start_date': 'Start Date', 'end_date': 'End Date', 'description': 'Description'}
    search_columns = ['organization_name', 'role', 'description']
    show_columns = ['id', 'person_id_fk', 'organization_name', 'role', 'start_date', 'end_date', 'description']
    add_columns = ['person_id_fk', 'organization_name', 'role', 'start_date', 'end_date', 'description']
    edit_columns = ['person_id_fk', 'organization_name', 'role', 'start_date', 'end_date', 'description']

    def __repr__(self):
        return self.id
    

class PersonPatentView(ModelView):
    datamodel = SQLAInterface(PersonPatent)
    list_title = 'Person Patent List'
    show_title = 'Person Patent Details'
    add_title = 'Add Person Patent'
    edit_title = 'Edit Person Patent'
    list_columns = ['id', 'person_id_fk', 'title', 'patent_office', 'patent_number', 'issue_date', 'description']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'title': 'Title', 'patent_office': 'Patent Office', 'patent_number': 'Patent Number', 'issue_date': 'Issue Date', 'description': 'Description'}
    search_columns = ['title', 'patent_office', 'patent_number', 'description']
    show_columns = ['id', 'person_id_fk', 'title', 'patent_office', 'patent_number', 'issue_date', 'description']
    add_columns = ['person_id_fk', 'title', 'patent_office', 'patent_number', 'issue_date', 'description']
    edit_columns = ['person_id_fk', 'title', 'patent_office', 'patent_number', 'issue_date', 'description']

    def __repr__(self):
        return self.title
    

class PersonProjectView(ModelView):
    datamodel = SQLAInterface(PersonProject)
    list_title = 'Person Project List'
    show_title = 'Person Project Details'
    add_title = 'Add Person Project'
    edit_title = 'Edit Person Project'
    list_columns = ['id', 'person_id_fk', 'name', 'description', 'start_date', 'end_date', 'project_url']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'name': 'Name', 'description': 'Description', 'start_date': 'Start Date', 'end_date': 'End Date', 'project_url': 'Project Url'}
    search_columns = ['name', 'description', 'project_url']
    show_columns = ['id', 'person_id_fk', 'name', 'description', 'start_date', 'end_date', 'project_url']
    add_columns = ['person_id_fk', 'name', 'description', 'start_date', 'end_date', 'project_url']
    edit_columns = ['person_id_fk', 'name', 'description', 'start_date', 'end_date', 'project_url']

    def __repr__(self):
        return self.name
    

class PersonPublicationView(ModelView):
    datamodel = SQLAInterface(PersonPublication)
    list_title = 'Person Publication List'
    show_title = 'Person Publication Details'
    add_title = 'Add Person Publication'
    edit_title = 'Edit Person Publication'
    list_columns = ['id', 'person_id_fk', 'title', 'publisher', 'date', 'url', 'description']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'title': 'Title', 'publisher': 'Publisher', 'date': 'Date', 'url': 'Url', 'description': 'Description'}
    search_columns = ['title', 'publisher', 'url', 'description']
    show_columns = ['id', 'person_id_fk', 'title', 'publisher', 'date', 'url', 'description']
    add_columns = ['person_id_fk', 'title', 'publisher', 'date', 'url', 'description']
    edit_columns = ['person_id_fk', 'title', 'publisher', 'date', 'url', 'description']

    def __repr__(self):
        return self.title
    

class PersonVolunteerExperienceView(ModelView):
    datamodel = SQLAInterface(PersonVolunteerExperience)
    list_title = 'Person Volunteer Experience List'
    show_title = 'Person Volunteer Experience Details'
    add_title = 'Add Person Volunteer Experience'
    edit_title = 'Edit Person Volunteer Experience'
    list_columns = ['id', 'person_id_fk', 'role', 'organization', 'cause', 'start_date', 'end_date', 'description']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'role': 'Role', 'organization': 'Organization', 'cause': 'Cause', 'start_date': 'Start Date', 'end_date': 'End Date', 'description': 'Description'}
    search_columns = ['role', 'organization', 'cause', 'description']
    show_columns = ['id', 'person_id_fk', 'role', 'organization', 'cause', 'start_date', 'end_date', 'description']
    add_columns = ['person_id_fk', 'role', 'organization', 'cause', 'start_date', 'end_date', 'description']
    edit_columns = ['person_id_fk', 'role', 'organization', 'cause', 'start_date', 'end_date', 'description']

    def __repr__(self):
        return self.id
    

class PointEarningActivityView(ModelView):
    datamodel = SQLAInterface(PointEarningActivity)
    list_title = 'Point Earning Activity List'
    show_title = 'Point Earning Activity Details'
    add_title = 'Add Point Earning Activity'
    edit_title = 'Edit Point Earning Activity'
    list_columns = ['id', 'person_id_fk', 'activity_type', 'points_earned', 'timestamp']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'activity_type': 'Activity Type', 'points_earned': 'Points Earned', 'timestamp': 'Timestamp'}
    search_columns = ['activity_type']
    show_columns = ['id', 'person_id_fk', 'activity_type', 'points_earned', 'timestamp']
    add_columns = ['person_id_fk', 'activity_type', 'points_earned', 'timestamp']
    edit_columns = ['person_id_fk', 'activity_type', 'points_earned', 'timestamp']

    def __repr__(self):
        return self.id
    

class ProfileUpdateReminderView(ModelView):
    datamodel = SQLAInterface(ProfileUpdateReminder)
    list_title = 'Profile Update Reminder List'
    show_title = 'Profile Update Reminder Details'
    add_title = 'Add Profile Update Reminder'
    edit_title = 'Edit Profile Update Reminder'
    list_columns = ['id', 'person_id_fk', 'last_reminder_date', 'reminder_count', 'next_reminder_date']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'last_reminder_date': 'Last Reminder Date', 'reminder_count': 'Reminder Count', 'next_reminder_date': 'Next Reminder Date'}
    search_columns = []
    show_columns = ['id', 'person_id_fk', 'last_reminder_date', 'reminder_count', 'next_reminder_date']
    add_columns = ['person_id_fk', 'last_reminder_date', 'reminder_count', 'next_reminder_date']
    edit_columns = ['person_id_fk', 'last_reminder_date', 'reminder_count', 'next_reminder_date']

    def __repr__(self):
        return self.id
    

class ScrapingRulesView(ModelView):
    datamodel = SQLAInterface(ScrapingRules)
    list_title = 'Scraping Rules List'
    show_title = 'Scraping Rules Details'
    add_title = 'Add Scraping Rules'
    edit_title = 'Edit Scraping Rules'
    list_columns = ['id', 'version', 'rule_data', 'created_at', 'is_active', 'created_by', 'updated_at']
    label_columns = {'id': 'Id', 'target_id': 'Target Id', 'version': 'Version', 'rule_data': 'Rule Data', 'created_at': 'Created At', 'is_active': 'Is Active', 'created_by': 'Created By', 'updated_at': 'Updated At'}
    search_columns = ['version', 'rule_data']
    show_columns = ['id', 'target_id', 'version', 'rule_data', 'created_at', 'is_active', 'created_by', 'updated_at']
    add_columns = ['version', 'rule_data', 'created_at', 'is_active', 'created_by', 'updated_at']
    edit_columns = ['target_id', 'version', 'rule_data', 'created_at', 'is_active', 'created_by', 'updated_at']

    def __repr__(self):
        return self.id
    

class ScrapingTasksView(ModelView):
    datamodel = SQLAInterface(ScrapingTasks)
    list_title = 'Scraping Tasks List'
    show_title = 'Scraping Tasks Details'
    add_title = 'Add Scraping Tasks'
    edit_title = 'Edit Scraping Tasks'
    list_columns = ['id', 'status', 'scheduled_at', 'executed_at', 'completed_at', 'error_message', 'performance_metrics']
    label_columns = {'id': 'Id', 'target_id': 'Target Id', 'status': 'Status', 'scheduled_at': 'Scheduled At', 'executed_at': 'Executed At', 'completed_at': 'Completed At', 'error_message': 'Error Message', 'performance_metrics': 'Performance Metrics'}
    search_columns = ['status', 'error_message', 'performance_metrics']
    show_columns = ['id', 'target_id', 'status', 'scheduled_at', 'executed_at', 'completed_at', 'error_message', 'performance_metrics']
    add_columns = ['status', 'scheduled_at', 'executed_at', 'completed_at', 'error_message', 'performance_metrics']
    edit_columns = ['target_id', 'status', 'scheduled_at', 'executed_at', 'completed_at', 'error_message', 'performance_metrics']

    def __repr__(self):
        return self.id
    

class SkillView(ModelView):
    datamodel = SQLAInterface(Skill)
    list_title = 'Skill List'
    show_title = 'Skill Details'
    add_title = 'Add Skill'
    edit_title = 'Edit Skill'
    list_columns = ['id', 'name', 'skill_category_id_fk', 'description']
    label_columns = {'id': 'Id', 'name': 'Name', 'skill_category_id_fk': 'Skill Category Id Fk', 'description': 'Description'}
    search_columns = ['name', 'description']
    show_columns = ['id', 'name', 'skill_category_id_fk', 'description']
    add_columns = ['name', 'skill_category_id_fk', 'description']
    edit_columns = ['name', 'skill_category_id_fk', 'description']

    def __repr__(self):
        return self.name
    

class TimezoneView(ModelView):
    datamodel = SQLAInterface(Timezone)
    list_title = 'Timezone List'
    show_title = 'Timezone Details'
    add_title = 'Add Timezone'
    edit_title = 'Edit Timezone'
    list_columns = ['id', 'country_id_fk', 'timezonename', 'comments']
    label_columns = {'id': 'Id', 'country_id_fk': 'Country Id Fk', 'timezonename': 'Timezonename', 'comments': 'Comments'}
    search_columns = ['timezonename', 'comments']
    show_columns = ['id', 'country_id_fk', 'timezonename', 'comments']
    add_columns = ['country_id_fk', 'timezonename', 'comments']
    edit_columns = ['country_id_fk', 'timezonename', 'comments']

    def __repr__(self):
        return self.id
    

class UserActivityView(ModelView):
    datamodel = SQLAInterface(UserActivity)
    list_title = 'User Activity List'
    show_title = 'User Activity Details'
    add_title = 'Add User Activity'
    edit_title = 'Edit User Activity'
    list_columns = ['id', 'person_id_fk', 'activity_type', 'timestamp', 'details']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'activity_type': 'Activity Type', 'timestamp': 'Timestamp', 'details': 'Details'}
    search_columns = ['activity_type', 'details']
    show_columns = ['id', 'person_id_fk', 'activity_type', 'timestamp', 'details']
    add_columns = ['person_id_fk', 'activity_type', 'timestamp', 'details']
    edit_columns = ['person_id_fk', 'activity_type', 'timestamp', 'details']

    def __repr__(self):
        return self.id
    

class UserGamificationView(ModelView):
    datamodel = SQLAInterface(UserGamification)
    list_title = 'User Gamification List'
    show_title = 'User Gamification Details'
    add_title = 'Add User Gamification'
    edit_title = 'Edit User Gamification'
    list_columns = ['id', 'user_id_fk', 'points', 'level', 'last_point_earned', 'points_to_next_level']
    label_columns = {'id': 'Id', 'user_id_fk': 'User Id Fk', 'points': 'Points', 'level': 'Level', 'last_point_earned': 'Last Point Earned', 'points_to_next_level': 'Points To Next Level'}
    search_columns = []
    show_columns = ['id', 'user_id_fk', 'points', 'level', 'last_point_earned', 'points_to_next_level']
    add_columns = ['user_id_fk', 'points', 'level', 'last_point_earned', 'points_to_next_level']
    edit_columns = ['user_id_fk', 'points', 'level', 'last_point_earned', 'points_to_next_level']

    def __repr__(self):
        return self.id
    

class AbPermissionViewRoleView(ModelView):
    datamodel = SQLAInterface(AbPermissionViewRole)
    list_title = 'Ab Permission View Role List'
    show_title = 'Ab Permission View Role Details'
    add_title = 'Add Ab Permission View Role'
    edit_title = 'Edit Ab Permission View Role'
    list_columns = ['id']
    label_columns = {'id': 'Id', 'permission_view_id': 'Permission View Id', 'role_id': 'Role Id'}
    search_columns = []
    show_columns = ['id', 'permission_view_id', 'role_id']
    add_columns = []
    edit_columns = ['permission_view_id', 'role_id']

    def __repr__(self):
        return self.id
    

class BoardMemberView(ModelView):
    datamodel = SQLAInterface(BoardMember)
    list_title = 'Board Member List'
    show_title = 'Board Member Details'
    add_title = 'Add Board Member'
    edit_title = 'Edit Board Member'
    list_columns = ['id', 'organization_id_fk', 'person_id_fk', 'position', 'start_date', 'end_date']
    label_columns = {'id': 'Id', 'organization_id_fk': 'Organization Id Fk', 'person_id_fk': 'Person Id Fk', 'position': 'Position', 'start_date': 'Start Date', 'end_date': 'End Date'}
    search_columns = ['position']
    show_columns = ['id', 'organization_id_fk', 'person_id_fk', 'position', 'start_date', 'end_date']
    add_columns = ['organization_id_fk', 'person_id_fk', 'position', 'start_date', 'end_date']
    edit_columns = ['organization_id_fk', 'person_id_fk', 'position', 'start_date', 'end_date']

    def __repr__(self):
        return self.id
    

class ContactApplicationView(ModelView):
    datamodel = SQLAInterface(ContactApplication)
    list_title = 'Contact Application List'
    show_title = 'Contact Application Details'
    add_title = 'Add Contact Application'
    edit_title = 'Edit Contact Application'
    list_columns = ['id', 'person_id_fk', 'organization_id_fk', 'position', 'message', 'application_date', 'status', 'review_date', 'review_notes']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'organization_id_fk': 'Organization Id Fk', 'position': 'Position', 'message': 'Message', 'application_date': 'Application Date', 'status': 'Status', 'review_date': 'Review Date', 'review_notes': 'Review Notes'}
    search_columns = ['position', 'message', 'status', 'review_notes']
    show_columns = ['id', 'person_id_fk', 'organization_id_fk', 'position', 'message', 'application_date', 'status', 'review_date', 'review_notes']
    add_columns = ['person_id_fk', 'organization_id_fk', 'position', 'message', 'application_date', 'status', 'review_date', 'review_notes']
    edit_columns = ['person_id_fk', 'organization_id_fk', 'position', 'message', 'application_date', 'status', 'review_date', 'review_notes']

    def __repr__(self):
        return self.id
    

class DocumentSubmissionView(ModelView):
    datamodel = SQLAInterface(DocumentSubmission)
    list_title = 'Document Submission List'
    show_title = 'Document Submission Details'
    add_title = 'Add Document Submission'
    edit_title = 'Edit Document Submission'
    list_columns = ['id', 'organization_id_fk', 'document_type', 'document_name', 'file_path', 'upload_date', 'status', 'next_status', 'review_notes', 'review_date']
    label_columns = {'id': 'Id', 'organization_id_fk': 'Organization Id Fk', 'document_type': 'Document Type', 'document_name': 'Document Name', 'file_path': 'File Path', 'upload_date': 'Upload Date', 'status': 'Status', 'next_status': 'Next Status', 'review_notes': 'Review Notes', 'review_date': 'Review Date'}
    search_columns = ['document_type', 'document_name', 'file_path', 'status', 'next_status', 'review_notes']
    show_columns = ['id', 'organization_id_fk', 'document_type', 'document_name', 'file_path', 'upload_date', 'status', 'next_status', 'review_notes', 'review_date']
    add_columns = ['organization_id_fk', 'document_type', 'document_name', 'file_path', 'upload_date', 'status', 'next_status', 'review_notes', 'review_date']
    edit_columns = ['organization_id_fk', 'document_type', 'document_name', 'file_path', 'upload_date', 'status', 'next_status', 'review_notes', 'review_date']

    def __repr__(self):
        return self.id
    

class EventView(ModelView):
    datamodel = SQLAInterface(Event)
    list_title = 'Event List'
    show_title = 'Event Details'
    add_title = 'Add Event'
    edit_title = 'Edit Event'
    list_columns = ['id', 'organization_id_fk', 'name', 'description', 'start_datetime', 'end_datetime', 'location', 'is_virtual', 'max_participants']
    label_columns = {'id': 'Id', 'organization_id_fk': 'Organization Id Fk', 'name': 'Name', 'description': 'Description', 'start_datetime': 'Start Datetime', 'end_datetime': 'End Datetime', 'location': 'Location', 'is_virtual': 'Is Virtual', 'max_participants': 'Max Participants'}
    search_columns = ['name', 'description', 'location']
    show_columns = ['id', 'organization_id_fk', 'name', 'description', 'start_datetime', 'end_datetime', 'location', 'is_virtual', 'max_participants']
    add_columns = ['organization_id_fk', 'name', 'description', 'start_datetime', 'end_datetime', 'location', 'is_virtual', 'max_participants']
    edit_columns = ['organization_id_fk', 'name', 'description', 'start_datetime', 'end_datetime', 'location', 'is_virtual', 'max_participants']

    def __repr__(self):
        return self.name
    

class ExecutivePositionView(ModelView):
    datamodel = SQLAInterface(ExecutivePosition)
    list_title = 'Executive Position List'
    show_title = 'Executive Position Details'
    add_title = 'Add Executive Position'
    edit_title = 'Edit Executive Position'
    list_columns = ['id', 'organization_id_fk', 'person_id_fk', 'title', 'start_date', 'end_date']
    label_columns = {'id': 'Id', 'organization_id_fk': 'Organization Id Fk', 'person_id_fk': 'Person Id Fk', 'title': 'Title', 'start_date': 'Start Date', 'end_date': 'End Date'}
    search_columns = ['title']
    show_columns = ['id', 'organization_id_fk', 'person_id_fk', 'title', 'start_date', 'end_date']
    add_columns = ['organization_id_fk', 'person_id_fk', 'title', 'start_date', 'end_date']
    edit_columns = ['organization_id_fk', 'person_id_fk', 'title', 'start_date', 'end_date']

    def __repr__(self):
        return self.title
    

class GrantView(ModelView):
    datamodel = SQLAInterface(Grant)
    list_title = 'Grant List'
    show_title = 'Grant Details'
    add_title = 'Add Grant'
    edit_title = 'Edit Grant'
    list_columns = ['id', 'donor_id_fk', 'recipient_id_fk', 'amount', 'start_date', 'end_date', 'status', 'description']
    label_columns = {'id': 'Id', 'donor_id_fk': 'Donor Id Fk', 'recipient_id_fk': 'Recipient Id Fk', 'amount': 'Amount', 'start_date': 'Start Date', 'end_date': 'End Date', 'status': 'Status', 'description': 'Description'}
    search_columns = ['status', 'description']
    show_columns = ['id', 'donor_id_fk', 'recipient_id_fk', 'amount', 'start_date', 'end_date', 'status', 'description']
    add_columns = ['donor_id_fk', 'recipient_id_fk', 'amount', 'start_date', 'end_date', 'status', 'description']
    edit_columns = ['donor_id_fk', 'recipient_id_fk', 'amount', 'start_date', 'end_date', 'status', 'description']

    def __repr__(self):
        return self.id
    

class OnboardingProgressView(ModelView):
    datamodel = SQLAInterface(OnboardingProgress)
    list_title = 'Onboarding Progress List'
    show_title = 'Onboarding Progress Details'
    add_title = 'Add Onboarding Progress'
    edit_title = 'Edit Onboarding Progress'
    list_columns = ['id', 'user_id_fk', 'organization_id_fk', 'step', 'completed_at']
    label_columns = {'id': 'Id', 'user_id_fk': 'User Id Fk', 'organization_id_fk': 'Organization Id Fk', 'step': 'Step', 'completed_at': 'Completed At'}
    search_columns = []
    show_columns = ['id', 'user_id_fk', 'organization_id_fk', 'step', 'completed_at']
    add_columns = ['user_id_fk', 'organization_id_fk', 'step', 'completed_at']
    edit_columns = ['user_id_fk', 'organization_id_fk', 'step', 'completed_at']

    def __repr__(self):
        return self.id
    

class OrganizationAwardView(ModelView):
    datamodel = SQLAInterface(OrganizationAward)
    list_title = 'Organization Award List'
    show_title = 'Organization Award Details'
    add_title = 'Add Organization Award'
    edit_title = 'Edit Organization Award'
    list_columns = ['id', 'organization_id_fk', 'name', 'awarding_body', 'date_received', 'description']
    label_columns = {'id': 'Id', 'organization_id_fk': 'Organization Id Fk', 'name': 'Name', 'awarding_body': 'Awarding Body', 'date_received': 'Date Received', 'description': 'Description'}
    search_columns = ['name', 'awarding_body', 'description']
    show_columns = ['id', 'organization_id_fk', 'name', 'awarding_body', 'date_received', 'description']
    add_columns = ['organization_id_fk', 'name', 'awarding_body', 'date_received', 'description']
    edit_columns = ['organization_id_fk', 'name', 'awarding_body', 'date_received', 'description']

    def __repr__(self):
        return self.name
    

class OrganizationBadgeView(ModelView):
    datamodel = SQLAInterface(OrganizationBadge)
    list_title = 'Organization Badge List'
    show_title = 'Organization Badge Details'
    add_title = 'Add Organization Badge'
    edit_title = 'Edit Organization Badge'
    list_columns = ['id', 'organization_id_fk', 'badge_id_fk', 'date_earned']
    label_columns = {'id': 'Id', 'organization_id_fk': 'Organization Id Fk', 'badge_id_fk': 'Badge Id Fk', 'date_earned': 'Date Earned'}
    search_columns = []
    show_columns = ['id', 'organization_id_fk', 'badge_id_fk', 'date_earned']
    add_columns = ['organization_id_fk', 'badge_id_fk', 'date_earned']
    edit_columns = ['organization_id_fk', 'badge_id_fk', 'date_earned']

    def __repr__(self):
        return self.id
    

class OrganizationClimateCategoriesView(ModelView):
    datamodel = SQLAInterface(OrganizationClimateCategories)
    list_title = 'Organization Climate Categories List'
    show_title = 'Organization Climate Categories Details'
    add_title = 'Add Organization Climate Categories'
    edit_title = 'Edit Organization Climate Categories'
    list_columns = ['organization_id_fk', 'climate_category']
    label_columns = {'organization_id_fk': 'Organization Id Fk', 'climate_category': 'Climate Category'}
    search_columns = ['climate_category']
    show_columns = ['organization_id_fk', 'climate_category']
    add_columns = ['organization_id_fk', 'climate_category']
    edit_columns = ['organization_id_fk', 'climate_category']

    def __repr__(self):
        return self.organization_id_fk
    

class OrganizationContactView(ModelView):
    datamodel = SQLAInterface(OrganizationContact)
    list_title = 'Organization Contact List'
    show_title = 'Organization Contact Details'
    add_title = 'Add Organization Contact'
    edit_title = 'Edit Organization Contact'
    list_columns = ['id', 'organization_id_fk', 'person_id_fk', 'org_email', 'org_phone', 'position', 'department', 'start_date', 'end_date', 'is_primary', 'status', 'notes']
    label_columns = {'id': 'Id', 'organization_id_fk': 'Organization Id Fk', 'person_id_fk': 'Person Id Fk', 'org_email': 'Org Email', 'org_phone': 'Org Phone', 'position': 'Position', 'department': 'Department', 'start_date': 'Start Date', 'end_date': 'End Date', 'is_primary': 'Is Primary', 'status': 'Status', 'notes': 'Notes'}
    search_columns = ['org_email', 'org_phone', 'position', 'department', 'status', 'notes']
    show_columns = ['id', 'organization_id_fk', 'person_id_fk', 'org_email', 'org_phone', 'position', 'department', 'start_date', 'end_date', 'is_primary', 'status', 'notes']
    add_columns = ['organization_id_fk', 'person_id_fk', 'org_email', 'org_phone', 'position', 'department', 'start_date', 'end_date', 'is_primary', 'status', 'notes']
    edit_columns = ['organization_id_fk', 'person_id_fk', 'org_email', 'org_phone', 'position', 'department', 'start_date', 'end_date', 'is_primary', 'status', 'notes']

    def __repr__(self):
        return self.id
    

class OrganizationDocumentsView(ModelView):
    datamodel = SQLAInterface(OrganizationDocuments)
    list_title = 'Organization Documents List'
    show_title = 'Organization Documents Details'
    add_title = 'Add Organization Documents'
    edit_title = 'Edit Organization Documents'
    list_columns = ['id', 'document_type', 'document_name', 'document_path', 'upload_date', 'document_summary']
    label_columns = {'id': 'Id', 'organization_id': 'Organization Id', 'document_type': 'Document Type', 'document_name': 'Document Name', 'document_path': 'Document Path', 'upload_date': 'Upload Date', 'document_summary': 'Document Summary'}
    search_columns = ['document_type', 'document_name', 'document_path', 'document_summary']
    show_columns = ['id', 'organization_id', 'document_type', 'document_name', 'document_path', 'upload_date', 'document_summary']
    add_columns = ['document_type', 'document_name', 'document_path', 'upload_date', 'document_summary']
    edit_columns = ['organization_id', 'document_type', 'document_name', 'document_path', 'upload_date', 'document_summary']

    def __repr__(self):
        return self.id
    

class OrganizationHierarchyView(ModelView):
    datamodel = SQLAInterface(OrganizationHierarchy)
    list_title = 'Organization Hierarchy List'
    show_title = 'Organization Hierarchy Details'
    add_title = 'Add Organization Hierarchy'
    edit_title = 'Edit Organization Hierarchy'
    list_columns = ['id', 'parent_org_id_fk', 'child_org_id_fk', 'relationship_type']
    label_columns = {'id': 'Id', 'parent_org_id_fk': 'Parent Org Id Fk', 'child_org_id_fk': 'Child Org Id Fk', 'relationship_type': 'Relationship Type'}
    search_columns = ['relationship_type']
    show_columns = ['id', 'parent_org_id_fk', 'child_org_id_fk', 'relationship_type']
    add_columns = ['parent_org_id_fk', 'child_org_id_fk', 'relationship_type']
    edit_columns = ['parent_org_id_fk', 'child_org_id_fk', 'relationship_type']

    def __repr__(self):
        return self.id
    

class OrganizationProfileView(ModelView):
    datamodel = SQLAInterface(OrganizationProfile)
    list_title = 'Organization Profile List'
    show_title = 'Organization Profile Details'
    add_title = 'Add Organization Profile'
    edit_title = 'Edit Organization Profile'
    list_columns = ['id', 'organization_id_fk', 'funding_focus_areas', 'average_grant_size', 'grant_making_process', 'funding_restrictions', 'focus_areas', 'target_beneficiaries', 'geographic_reach', 'years_of_operation', 'total_beneficiaries_last_year', 'annual_budget', 'num_employees', 'num_volunteers', 'last_year_revenue', 'last_year_expenditure']
    label_columns = {'id': 'Id', 'organization_id_fk': 'Organization Id Fk', 'funding_focus_areas': 'Funding Focus Areas', 'average_grant_size': 'Average Grant Size', 'grant_making_process': 'Grant Making Process', 'funding_restrictions': 'Funding Restrictions', 'focus_areas': 'Focus Areas', 'target_beneficiaries': 'Target Beneficiaries', 'geographic_reach': 'Geographic Reach', 'years_of_operation': 'Years Of Operation', 'total_beneficiaries_last_year': 'Total Beneficiaries Last Year', 'annual_budget': 'Annual Budget', 'num_employees': 'Num Employees', 'num_volunteers': 'Num Volunteers', 'last_year_revenue': 'Last Year Revenue', 'last_year_expenditure': 'Last Year Expenditure'}
    search_columns = ['funding_focus_areas', 'grant_making_process', 'funding_restrictions', 'focus_areas', 'target_beneficiaries', 'geographic_reach']
    show_columns = ['id', 'organization_id_fk', 'funding_focus_areas', 'average_grant_size', 'grant_making_process', 'funding_restrictions', 'focus_areas', 'target_beneficiaries', 'geographic_reach', 'years_of_operation', 'total_beneficiaries_last_year', 'annual_budget', 'num_employees', 'num_volunteers', 'last_year_revenue', 'last_year_expenditure']
    add_columns = ['organization_id_fk', 'funding_focus_areas', 'average_grant_size', 'grant_making_process', 'funding_restrictions', 'focus_areas', 'target_beneficiaries', 'geographic_reach', 'years_of_operation', 'total_beneficiaries_last_year', 'annual_budget', 'num_employees', 'num_volunteers', 'last_year_revenue', 'last_year_expenditure']
    edit_columns = ['organization_id_fk', 'funding_focus_areas', 'average_grant_size', 'grant_making_process', 'funding_restrictions', 'focus_areas', 'target_beneficiaries', 'geographic_reach', 'years_of_operation', 'total_beneficiaries_last_year', 'annual_budget', 'num_employees', 'num_volunteers', 'last_year_revenue', 'last_year_expenditure']

    def __repr__(self):
        return self.id
    

class OrganizationProgramsView(ModelView):
    datamodel = SQLAInterface(OrganizationPrograms)
    list_title = 'Organization Programs List'
    show_title = 'Organization Programs Details'
    add_title = 'Add Organization Programs'
    edit_title = 'Edit Organization Programs'
    list_columns = ['id', 'program_name', 'program_description', 'start_date', 'end_date', 'budget', 'impact_assessment']
    label_columns = {'id': 'Id', 'organization_id': 'Organization Id', 'program_name': 'Program Name', 'program_description': 'Program Description', 'start_date': 'Start Date', 'end_date': 'End Date', 'budget': 'Budget', 'impact_assessment': 'Impact Assessment'}
    search_columns = ['program_name', 'program_description', 'impact_assessment']
    show_columns = ['id', 'organization_id', 'program_name', 'program_description', 'start_date', 'end_date', 'budget', 'impact_assessment']
    add_columns = ['program_name', 'program_description', 'start_date', 'end_date', 'budget', 'impact_assessment']
    edit_columns = ['organization_id', 'program_name', 'program_description', 'start_date', 'end_date', 'budget', 'impact_assessment']

    def __repr__(self):
        return self.id
    

class OrganizationSdgsView(ModelView):
    datamodel = SQLAInterface(OrganizationSdgs)
    list_title = 'Organization Sdgs List'
    show_title = 'Organization Sdgs Details'
    add_title = 'Add Organization Sdgs'
    edit_title = 'Edit Organization Sdgs'
    list_columns = ['organization_id_fk', 'sdg']
    label_columns = {'organization_id_fk': 'Organization Id Fk', 'sdg': 'Sdg'}
    search_columns = ['sdg']
    show_columns = ['organization_id_fk', 'sdg']
    add_columns = ['organization_id_fk', 'sdg']
    edit_columns = ['organization_id_fk', 'sdg']

    def __repr__(self):
        return self.organization_id_fk
    

class OrganizationTagView(ModelView):
    datamodel = SQLAInterface(OrganizationTag)
    list_title = 'Organization Tag List'
    show_title = 'Organization Tag Details'
    add_title = 'Add Organization Tag'
    edit_title = 'Edit Organization Tag'
    list_columns = ['id', 'organization_id_fk', 'tag_id_fk']
    label_columns = {'id': 'Id', 'organization_id_fk': 'Organization Id Fk', 'tag_id_fk': 'Tag Id Fk'}
    search_columns = []
    show_columns = ['id', 'organization_id_fk', 'tag_id_fk']
    add_columns = ['organization_id_fk', 'tag_id_fk']
    edit_columns = ['organization_id_fk', 'tag_id_fk']

    def __repr__(self):
        return self.id
    

class OrganizationVerificationView(ModelView):
    datamodel = SQLAInterface(OrganizationVerification)
    list_title = 'Organization Verification List'
    show_title = 'Organization Verification Details'
    add_title = 'Add Organization Verification'
    edit_title = 'Edit Organization Verification'
    list_columns = ['id', 'organization_id_fk', 'registration_number', 'registration_date', 'registering_authority', 'registration_expiry', 'last_verification_date', 'verification_status', 'verification_notes']
    label_columns = {'id': 'Id', 'organization_id_fk': 'Organization Id Fk', 'registration_number': 'Registration Number', 'registration_date': 'Registration Date', 'registering_authority': 'Registering Authority', 'registration_expiry': 'Registration Expiry', 'last_verification_date': 'Last Verification Date', 'verification_status': 'Verification Status', 'verification_notes': 'Verification Notes'}
    search_columns = ['registration_number', 'registering_authority', 'verification_status', 'verification_notes']
    show_columns = ['id', 'organization_id_fk', 'registration_number', 'registration_date', 'registering_authority', 'registration_expiry', 'last_verification_date', 'verification_status', 'verification_notes']
    add_columns = ['organization_id_fk', 'registration_number', 'registration_date', 'registering_authority', 'registration_expiry', 'last_verification_date', 'verification_status', 'verification_notes']
    edit_columns = ['organization_id_fk', 'registration_number', 'registration_date', 'registering_authority', 'registration_expiry', 'last_verification_date', 'verification_status', 'verification_notes']

    def __repr__(self):
        return self.id
    

class PersonOrganizationClaimView(ModelView):
    datamodel = SQLAInterface(PersonOrganizationClaim)
    list_title = 'Person Organization Claim List'
    show_title = 'Person Organization Claim Details'
    add_title = 'Add Person Organization Claim'
    edit_title = 'Edit Person Organization Claim'
    list_columns = ['id', 'claim_type', 'status', 'claim_date', 'review_date']
    label_columns = {'id': 'Id', 'person_id': 'Person Id', 'organization_id': 'Organization Id', 'claim_type': 'Claim Type', 'status': 'Status', 'claim_date': 'Claim Date', 'review_date': 'Review Date'}
    search_columns = ['claim_type', 'status']
    show_columns = ['id', 'person_id', 'organization_id', 'claim_type', 'status', 'claim_date', 'review_date']
    add_columns = ['claim_type', 'status', 'claim_date', 'review_date']
    edit_columns = ['person_id', 'organization_id', 'claim_type', 'status', 'claim_date', 'review_date']

    def __repr__(self):
        return self.id
    

class PersonSkillView(ModelView):
    datamodel = SQLAInterface(PersonSkill)
    list_title = 'Person Skill List'
    show_title = 'Person Skill Details'
    add_title = 'Add Person Skill'
    edit_title = 'Edit Person Skill'
    list_columns = ['id', 'person_id_fk', 'skill_id_fk', 'proficiency_level', 'endorsements']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'skill_id_fk': 'Skill Id Fk', 'proficiency_level': 'Proficiency Level', 'endorsements': 'Endorsements'}
    search_columns = []
    show_columns = ['id', 'person_id_fk', 'skill_id_fk', 'proficiency_level', 'endorsements']
    add_columns = ['person_id_fk', 'skill_id_fk', 'proficiency_level', 'endorsements']
    edit_columns = ['person_id_fk', 'skill_id_fk', 'proficiency_level', 'endorsements']

    def __repr__(self):
        return self.id
    

class ProjectView(ModelView):
    datamodel = SQLAInterface(Project)
    list_title = 'Project List'
    show_title = 'Project Details'
    add_title = 'Add Project'
    edit_title = 'Edit Project'
    list_columns = ['id', 'organization_id_fk', 'name', 'description', 'start_date', 'end_date', 'budget', 'status', 'beneficiaries', 'outcomes']
    label_columns = {'id': 'Id', 'organization_id_fk': 'Organization Id Fk', 'name': 'Name', 'description': 'Description', 'start_date': 'Start Date', 'end_date': 'End Date', 'budget': 'Budget', 'status': 'Status', 'beneficiaries': 'Beneficiaries', 'outcomes': 'Outcomes'}
    search_columns = ['name', 'description', 'status', 'outcomes']
    show_columns = ['id', 'organization_id_fk', 'name', 'description', 'start_date', 'end_date', 'budget', 'status', 'beneficiaries', 'outcomes']
    add_columns = ['organization_id_fk', 'name', 'description', 'start_date', 'end_date', 'budget', 'status', 'beneficiaries', 'outcomes']
    edit_columns = ['organization_id_fk', 'name', 'description', 'start_date', 'end_date', 'budget', 'status', 'beneficiaries', 'outcomes']

    def __repr__(self):
        return self.name
    

class RawScrapedDataView(ModelView):
    datamodel = SQLAInterface(RawScrapedData)
    list_title = 'Raw Scraped Data List'
    show_title = 'Raw Scraped Data Details'
    add_title = 'Add Raw Scraped Data'
    edit_title = 'Edit Raw Scraped Data'
    list_columns = ['id', 'content', 'created_at', 'is_archived']
    label_columns = {'id': 'Id', 'task_id': 'Task Id', 'content': 'Content', 'created_at': 'Created At', 'is_archived': 'Is Archived'}
    search_columns = ['content']
    show_columns = ['id', 'task_id', 'content', 'created_at', 'is_archived']
    add_columns = ['content', 'created_at', 'is_archived']
    edit_columns = ['task_id', 'content', 'created_at', 'is_archived']

    def __repr__(self):
        return self.id
    

class ReportView(ModelView):
    datamodel = SQLAInterface(Report)
    list_title = 'Report List'
    show_title = 'Report Details'
    add_title = 'Add Report'
    edit_title = 'Edit Report'
    list_columns = ['id', 'organization_id_fk', 'title', 'description', 'file_path', 'created_date', 'report_type']
    label_columns = {'id': 'Id', 'organization_id_fk': 'Organization Id Fk', 'title': 'Title', 'description': 'Description', 'file_path': 'File Path', 'created_date': 'Created Date', 'report_type': 'Report Type'}
    search_columns = ['title', 'description', 'file_path', 'report_type']
    show_columns = ['id', 'organization_id_fk', 'title', 'description', 'file_path', 'created_date', 'report_type']
    add_columns = ['organization_id_fk', 'title', 'description', 'file_path', 'created_date', 'report_type']
    edit_columns = ['organization_id_fk', 'title', 'description', 'file_path', 'created_date', 'report_type']

    def __repr__(self):
        return self.title
    

class SocialMediaProfileView(ModelView):
    datamodel = SQLAInterface(SocialMediaProfile)
    list_title = 'Social Media Profile List'
    show_title = 'Social Media Profile Details'
    add_title = 'Add Social Media Profile'
    edit_title = 'Edit Social Media Profile'
    list_columns = ['id', 'person_id_fk', 'org_id_fk', 'platform', 'access_token', 'refresh_token', 'token_expiry']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'org_id_fk': 'Org Id Fk', 'platform': 'Platform', 'profile_id': 'Profile Id', 'access_token': 'Access Token', 'refresh_token': 'Refresh Token', 'token_expiry': 'Token Expiry'}
    search_columns = ['platform', 'profile_id', 'access_token', 'refresh_token']
    show_columns = ['id', 'person_id_fk', 'org_id_fk', 'platform', 'profile_id', 'access_token', 'refresh_token', 'token_expiry']
    add_columns = ['person_id_fk', 'org_id_fk', 'platform', 'access_token', 'refresh_token', 'token_expiry']
    edit_columns = ['person_id_fk', 'org_id_fk', 'platform', 'profile_id', 'access_token', 'refresh_token', 'token_expiry']

    def __repr__(self):
        return self.id
    

class TrainingView(ModelView):
    datamodel = SQLAInterface(Training)
    list_title = 'Training List'
    show_title = 'Training Details'
    add_title = 'Add Training'
    edit_title = 'Edit Training'
    list_columns = ['id', 'offering_org_id_fk', 'name', 'description', 'start_date', 'end_date', 'is_certified']
    label_columns = {'id': 'Id', 'offering_org_id_fk': 'Offering Org Id Fk', 'name': 'Name', 'description': 'Description', 'start_date': 'Start Date', 'end_date': 'End Date', 'is_certified': 'Is Certified'}
    search_columns = ['name', 'description']
    show_columns = ['id', 'offering_org_id_fk', 'name', 'description', 'start_date', 'end_date', 'is_certified']
    add_columns = ['offering_org_id_fk', 'name', 'description', 'start_date', 'end_date', 'is_certified']
    edit_columns = ['offering_org_id_fk', 'name', 'description', 'start_date', 'end_date', 'is_certified']

    def __repr__(self):
        return self.name
    

class UserChallengeView(ModelView):
    datamodel = SQLAInterface(UserChallenge)
    list_title = 'User Challenge List'
    show_title = 'User Challenge Details'
    add_title = 'Add User Challenge'
    edit_title = 'Edit User Challenge'
    list_columns = ['id', 'person_id_fk', 'challenge_id_fk', 'completed', 'completion_date']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'challenge_id_fk': 'Challenge Id Fk', 'completed': 'Completed', 'completion_date': 'Completion Date'}
    search_columns = []
    show_columns = ['id', 'person_id_fk', 'challenge_id_fk', 'completed', 'completion_date']
    add_columns = ['person_id_fk', 'challenge_id_fk', 'completed', 'completion_date']
    edit_columns = ['person_id_fk', 'challenge_id_fk', 'completed', 'completion_date']

    def __repr__(self):
        return self.id
    

class VolunteerLogView(ModelView):
    datamodel = SQLAInterface(VolunteerLog)
    list_title = 'Volunteer Log List'
    show_title = 'Volunteer Log Details'
    add_title = 'Add Volunteer Log'
    edit_title = 'Edit Volunteer Log'
    list_columns = ['id', 'person_id_fk', 'organization_id_fk', 'start_date', 'end_date', 'hours_contributed', 'role', 'skills_used']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'organization_id_fk': 'Organization Id Fk', 'start_date': 'Start Date', 'end_date': 'End Date', 'hours_contributed': 'Hours Contributed', 'role': 'Role', 'skills_used': 'Skills Used'}
    search_columns = ['role', 'skills_used']
    show_columns = ['id', 'person_id_fk', 'organization_id_fk', 'start_date', 'end_date', 'hours_contributed', 'role', 'skills_used']
    add_columns = ['person_id_fk', 'organization_id_fk', 'start_date', 'end_date', 'hours_contributed', 'role', 'skills_used']
    edit_columns = ['person_id_fk', 'organization_id_fk', 'start_date', 'end_date', 'hours_contributed', 'role', 'skills_used']

    def __repr__(self):
        return self.id
    

class EventRegistrationView(ModelView):
    datamodel = SQLAInterface(EventRegistration)
    list_title = 'Event Registration List'
    show_title = 'Event Registration Details'
    add_title = 'Add Event Registration'
    edit_title = 'Edit Event Registration'
    list_columns = ['id', 'event_id_fk', 'person_id_fk', 'registration_date', 'attended']
    label_columns = {'id': 'Id', 'event_id_fk': 'Event Id Fk', 'person_id_fk': 'Person Id Fk', 'registration_date': 'Registration Date', 'attended': 'Attended'}
    search_columns = []
    show_columns = ['id', 'event_id_fk', 'person_id_fk', 'registration_date', 'attended']
    add_columns = ['event_id_fk', 'person_id_fk', 'registration_date', 'attended']
    edit_columns = ['event_id_fk', 'person_id_fk', 'registration_date', 'attended']

    def __repr__(self):
        return self.id
    

class ImpactView(ModelView):
    datamodel = SQLAInterface(Impact)
    list_title = 'Impact List'
    show_title = 'Impact Details'
    add_title = 'Add Impact'
    edit_title = 'Edit Impact'
    list_columns = ['id', 'organization_id_fk', 'project_id_fk', 'metric_name', 'value', 'unit', 'date_measured', 'description']
    label_columns = {'id': 'Id', 'organization_id_fk': 'Organization Id Fk', 'project_id_fk': 'Project Id Fk', 'metric_name': 'Metric Name', 'value': 'Value', 'unit': 'Unit', 'date_measured': 'Date Measured', 'description': 'Description'}
    search_columns = ['metric_name', 'unit', 'description']
    show_columns = ['id', 'organization_id_fk', 'project_id_fk', 'metric_name', 'value', 'unit', 'date_measured', 'description']
    add_columns = ['organization_id_fk', 'project_id_fk', 'metric_name', 'value', 'unit', 'date_measured', 'description']
    edit_columns = ['organization_id_fk', 'project_id_fk', 'metric_name', 'value', 'unit', 'date_measured', 'description']

    def __repr__(self):
        return self.id
    

class PersonTrainingView(ModelView):
    datamodel = SQLAInterface(PersonTraining)
    list_title = 'Person Training List'
    show_title = 'Person Training Details'
    add_title = 'Add Person Training'
    edit_title = 'Edit Person Training'
    list_columns = ['id', 'training_id_fk', 'person_id_fk', 'start_date', 'completion_date', 'completed']
    label_columns = {'id': 'Id', 'training_id_fk': 'Training Id Fk', 'person_id_fk': 'Person Id Fk', 'start_date': 'Start Date', 'completion_date': 'Completion Date', 'completed': 'Completed', 'certificate_id': 'Certificate Id'}
    search_columns = ['certificate_id']
    show_columns = ['id', 'training_id_fk', 'person_id_fk', 'start_date', 'completion_date', 'completed', 'certificate_id']
    add_columns = ['training_id_fk', 'person_id_fk', 'start_date', 'completion_date', 'completed']
    edit_columns = ['training_id_fk', 'person_id_fk', 'start_date', 'completion_date', 'completed', 'certificate_id']

    def __repr__(self):
        return self.id
    

class PjFeedbackView(ModelView):
    datamodel = SQLAInterface(PjFeedback)
    list_title = 'Pj Feedback List'
    show_title = 'Pj Feedback Details'
    add_title = 'Add Pj Feedback'
    edit_title = 'Edit Pj Feedback'
    list_columns = ['id', 'person_id_fk', 'organization_id_fk', 'project_id_fk', 'rating', 'comments', 'notes', 'date']
    label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'organization_id_fk': 'Organization Id Fk', 'project_id_fk': 'Project Id Fk', 'rating': 'Rating', 'comments': 'Comments', 'notes': 'Notes', 'date': 'Date'}
    search_columns = ['comments', 'notes']
    show_columns = ['id', 'person_id_fk', 'organization_id_fk', 'project_id_fk', 'rating', 'comments', 'notes', 'date']
    add_columns = ['person_id_fk', 'organization_id_fk', 'project_id_fk', 'rating', 'comments', 'notes', 'date']
    edit_columns = ['person_id_fk', 'organization_id_fk', 'project_id_fk', 'rating', 'comments', 'notes', 'date']

    def __repr__(self):
        return self.id
    

class ProjectLocationsView(ModelView):
    datamodel = SQLAInterface(ProjectLocations)
    list_title = 'Project Locations List'
    show_title = 'Project Locations Details'
    add_title = 'Add Project Locations'
    edit_title = 'Edit Project Locations'
    list_columns = ['id', 'project_id_fk', 'location_name', 'location_coordinates_id_fk']
    label_columns = {'id': 'Id', 'project_id_fk': 'Project Id Fk', 'location_name': 'Location Name', 'location_coordinates_id_fk': 'Location Coordinates Id Fk'}
    search_columns = ['location_name']
    show_columns = ['id', 'project_id_fk', 'location_name', 'location_coordinates_id_fk']
    add_columns = ['project_id_fk', 'location_name', 'location_coordinates_id_fk']
    edit_columns = ['project_id_fk', 'location_name', 'location_coordinates_id_fk']

    def __repr__(self):
        return self.id
    

class ProjectTagView(ModelView):
    datamodel = SQLAInterface(ProjectTag)
    list_title = 'Project Tag List'
    show_title = 'Project Tag Details'
    add_title = 'Add Project Tag'
    edit_title = 'Edit Project Tag'
    list_columns = ['id', 'project_id_fk', 'tag_id_fk']
    label_columns = {'id': 'Id', 'project_id_fk': 'Project Id Fk', 'tag_id_fk': 'Tag Id Fk'}
    search_columns = []
    show_columns = ['id', 'project_id_fk', 'tag_id_fk']
    add_columns = ['project_id_fk', 'tag_id_fk']
    edit_columns = ['project_id_fk', 'tag_id_fk']

    def __repr__(self):
        return self.id
    

class ScrapedRfpsView(ModelView):
    datamodel = SQLAInterface(ScrapedRfps)
    list_title = 'Scraped Rfps List'
    show_title = 'Scraped Rfps Details'
    add_title = 'Add Scraped Rfps'
    edit_title = 'Edit Scraped Rfps'
    list_columns = ['id', 'title', 'description', 'source_url', 'published_date', 'deadline', 'organization', 'industry', 'is_duplicate', 'relevance_score', 'sentiment_score', 'created_at', 'content_hash']
    label_columns = {'id': 'Id', 'task_id': 'Task Id', 'raw_data_id': 'Raw Data Id', 'title': 'Title', 'description': 'Description', 'source_url': 'Source Url', 'published_date': 'Published Date', 'deadline': 'Deadline', 'organization': 'Organization', 'industry': 'Industry', 'is_duplicate': 'Is Duplicate', 'relevance_score': 'Relevance Score', 'sentiment_score': 'Sentiment Score', 'created_at': 'Created At', 'content_hash': 'Content Hash'}
    search_columns = ['title', 'description', 'source_url', 'organization', 'industry', 'content_hash']
    show_columns = ['id', 'task_id', 'raw_data_id', 'title', 'description', 'source_url', 'published_date', 'deadline', 'organization', 'industry', 'is_duplicate', 'relevance_score', 'sentiment_score', 'created_at', 'content_hash']
    add_columns = ['title', 'description', 'source_url', 'published_date', 'deadline', 'organization', 'industry', 'is_duplicate', 'relevance_score', 'sentiment_score', 'created_at', 'content_hash']
    edit_columns = ['task_id', 'raw_data_id', 'title', 'description', 'source_url', 'published_date', 'deadline', 'organization', 'industry', 'is_duplicate', 'relevance_score', 'sentiment_score', 'created_at', 'content_hash']

    def __repr__(self):
        return self.title
    

class AbUserAbUserMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(AbUser)
    related_views = [AbUserView]
    list_title = 'Ab User with Ab User'
    show_template = 'appbuilder/general/model/show_cascade.html'

class AbUserAbUserMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(AbUser)
    related_views = [AbUserView]
    list_title = 'Ab User with Ab User'
    show_template = 'appbuilder/general/model/show_cascade.html'

class GeonameCountryMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Geoname)
    related_views = [CountryView]
    list_title = 'Geoname with Country'
    show_template = 'appbuilder/general/model/show_cascade.html'

class CountryGeonameMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Country)
    related_views = [GeonameView]
    list_title = 'Country with Geoname'
    show_template = 'appbuilder/general/model/show_cascade.html'

class AlternatenameGeonameMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Alternatename)
    related_views = [GeonameView]
    list_title = 'Alternatename with Geoname'
    show_template = 'appbuilder/general/model/show_cascade.html'

class AbPermissionAbPermissionViewMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(AbPermission)
    related_views = [AbPermissionViewView]
    list_title = 'Ab Permission with Ab Permission View'
    show_template = 'appbuilder/general/model/show_cascade.html'

class AbViewMenuAbPermissionViewMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(AbViewMenu)
    related_views = [AbPermissionViewView]
    list_title = 'Ab View Menu with Ab Permission View'
    show_template = 'appbuilder/general/model/show_cascade.html'

class AbUserAbUserRoleMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(AbUser)
    related_views = [AbUserRoleView]
    list_title = 'Ab User with Ab User Role'
    show_template = 'appbuilder/general/model/show_cascade.html'

class AbRoleAbUserRoleMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(AbRole)
    related_views = [AbUserRoleView]
    list_title = 'Ab Role with Ab User Role'
    show_template = 'appbuilder/general/model/show_cascade.html'

class CountryAdmin1codesMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Country)
    related_views = [Admin1codesView]
    list_title = 'Country with Admin1codes'
    show_template = 'appbuilder/general/model/show_cascade.html'

class GeonameAdmin1codesMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Geoname)
    related_views = [Admin1codesView]
    list_title = 'Geoname with Admin1codes'
    show_template = 'appbuilder/general/model/show_cascade.html'

class CountryAdmin2codesMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Country)
    related_views = [Admin2codesView]
    list_title = 'Country with Admin2codes'
    show_template = 'appbuilder/general/model/show_cascade.html'

class GeonameAdmin2codesMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Geoname)
    related_views = [Admin2codesView]
    list_title = 'Geoname with Admin2codes'
    show_template = 'appbuilder/general/model/show_cascade.html'

class ContactTypeContactMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(ContactType)
    related_views = [ContactView]
    list_title = 'Contact Type with Contact'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonContactMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [ContactView]
    list_title = 'Person with Contact'
    show_template = 'appbuilder/general/model/show_cascade.html'

class BadgeGamificationChallengeMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Badge)
    related_views = [GamificationChallengeView]
    list_title = 'Badge with Gamification Challenge'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonLeaderboardMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [LeaderboardView]
    list_title = 'Person with Leaderboard'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonMessageMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [MessageView]
    list_title = 'Person with Message'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonMessageMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [MessageView]
    list_title = 'Person with Message'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonNotificationMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [NotificationView]
    list_title = 'Person with Notification'
    show_template = 'appbuilder/general/model/show_cascade.html'

class CountryOrganizationMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Country)
    related_views = [OrganizationView]
    list_title = 'Country with Organization'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonOrganizationMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [OrganizationView]
    list_title = 'Person with Organization'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPersonBadgeMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonBadgeView]
    list_title = 'Person with Person Badge'
    show_template = 'appbuilder/general/model/show_cascade.html'

class BadgePersonBadgeMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Badge)
    related_views = [PersonBadgeView]
    list_title = 'Badge with Person Badge'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPersonCertificationMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonCertificationView]
    list_title = 'Person with Person Certification'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPersonCourseMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonCourseView]
    list_title = 'Person with Person Course'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPersonEducationMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonEducationView]
    list_title = 'Person with Person Education'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPersonExperienceMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonExperienceView]
    list_title = 'Person with Person Experience'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPersonHonorAwardMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonHonorAwardView]
    list_title = 'Person with Person Honor Award'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPersonLanguageMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonLanguageView]
    list_title = 'Person with Person Language'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPersonOrganizationMembershipMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonOrganizationMembershipView]
    list_title = 'Person with Person Organization Membership'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPersonPatentMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonPatentView]
    list_title = 'Person with Person Patent'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPersonProjectMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonProjectView]
    list_title = 'Person with Person Project'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPersonPublicationMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonPublicationView]
    list_title = 'Person with Person Publication'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPersonVolunteerExperienceMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonVolunteerExperienceView]
    list_title = 'Person with Person Volunteer Experience'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPointEarningActivityMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PointEarningActivityView]
    list_title = 'Person with Point Earning Activity'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonProfileUpdateReminderMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [ProfileUpdateReminderView]
    list_title = 'Person with Profile Update Reminder'
    show_template = 'appbuilder/general/model/show_cascade.html'

class ScrapingTargetsScrapingRulesMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(ScrapingTargets)
    related_views = [ScrapingRulesView]
    list_title = 'Scraping Targets with Scraping Rules'
    show_template = 'appbuilder/general/model/show_cascade.html'

class AbUserScrapingRulesMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(AbUser)
    related_views = [ScrapingRulesView]
    list_title = 'Ab User with Scraping Rules'
    show_template = 'appbuilder/general/model/show_cascade.html'

class ScrapingTargetsScrapingTasksMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(ScrapingTargets)
    related_views = [ScrapingTasksView]
    list_title = 'Scraping Targets with Scraping Tasks'
    show_template = 'appbuilder/general/model/show_cascade.html'

class SkillCategorySkillMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(SkillCategory)
    related_views = [SkillView]
    list_title = 'Skill Category with Skill'
    show_template = 'appbuilder/general/model/show_cascade.html'

class CountryTimezoneMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Country)
    related_views = [TimezoneView]
    list_title = 'Country with Timezone'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonUserActivityMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [UserActivityView]
    list_title = 'Person with User Activity'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonUserGamificationMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [UserGamificationView]
    list_title = 'Person with User Gamification'
    show_template = 'appbuilder/general/model/show_cascade.html'

class AbPermissionViewAbPermissionViewRoleMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(AbPermissionView)
    related_views = [AbPermissionViewRoleView]
    list_title = 'Ab Permission View with Ab Permission View Role'
    show_template = 'appbuilder/general/model/show_cascade.html'

class AbRoleAbPermissionViewRoleMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(AbRole)
    related_views = [AbPermissionViewRoleView]
    list_title = 'Ab Role with Ab Permission View Role'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonBoardMemberMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [BoardMemberView]
    list_title = 'Person with Board Member'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationBoardMemberMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [BoardMemberView]
    list_title = 'Organization with Board Member'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonContactApplicationMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [ContactApplicationView]
    list_title = 'Person with Contact Application'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationContactApplicationMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [ContactApplicationView]
    list_title = 'Organization with Contact Application'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationDocumentSubmissionMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [DocumentSubmissionView]
    list_title = 'Organization with Document Submission'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationEventMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [EventView]
    list_title = 'Organization with Event'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationExecutivePositionMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [ExecutivePositionView]
    list_title = 'Organization with Executive Position'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonExecutivePositionMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [ExecutivePositionView]
    list_title = 'Person with Executive Position'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationGrantMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [GrantView]
    list_title = 'Organization with Grant'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationGrantMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [GrantView]
    list_title = 'Organization with Grant'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonOnboardingProgressMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [OnboardingProgressView]
    list_title = 'Person with Onboarding Progress'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationOnboardingProgressMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [OnboardingProgressView]
    list_title = 'Organization with Onboarding Progress'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationOrganizationAwardMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [OrganizationAwardView]
    list_title = 'Organization with Organization Award'
    show_template = 'appbuilder/general/model/show_cascade.html'

class BadgeOrganizationBadgeMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Badge)
    related_views = [OrganizationBadgeView]
    list_title = 'Badge with Organization Badge'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationOrganizationBadgeMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [OrganizationBadgeView]
    list_title = 'Organization with Organization Badge'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationOrganizationClimateCategoriesMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [OrganizationClimateCategoriesView]
    list_title = 'Organization with Organization Climate Categories'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationOrganizationContactMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [OrganizationContactView]
    list_title = 'Organization with Organization Contact'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonOrganizationContactMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [OrganizationContactView]
    list_title = 'Person with Organization Contact'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationOrganizationDocumentsMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [OrganizationDocumentsView]
    list_title = 'Organization with Organization Documents'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationOrganizationHierarchyMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [OrganizationHierarchyView]
    list_title = 'Organization with Organization Hierarchy'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationOrganizationHierarchyMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [OrganizationHierarchyView]
    list_title = 'Organization with Organization Hierarchy'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationOrganizationProfileMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [OrganizationProfileView]
    list_title = 'Organization with Organization Profile'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationOrganizationProgramsMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [OrganizationProgramsView]
    list_title = 'Organization with Organization Programs'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationOrganizationSdgsMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [OrganizationSdgsView]
    list_title = 'Organization with Organization Sdgs'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationOrganizationTagMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [OrganizationTagView]
    list_title = 'Organization with Organization Tag'
    show_template = 'appbuilder/general/model/show_cascade.html'

class TagOrganizationTagMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Tag)
    related_views = [OrganizationTagView]
    list_title = 'Tag with Organization Tag'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationOrganizationVerificationMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [OrganizationVerificationView]
    list_title = 'Organization with Organization Verification'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationPersonOrganizationClaimMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [PersonOrganizationClaimView]
    list_title = 'Organization with Person Organization Claim'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPersonOrganizationClaimMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonOrganizationClaimView]
    list_title = 'Person with Person Organization Claim'
    show_template = 'appbuilder/general/model/show_cascade.html'

class SkillPersonSkillMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Skill)
    related_views = [PersonSkillView]
    list_title = 'Skill with Person Skill'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPersonSkillMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonSkillView]
    list_title = 'Person with Person Skill'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationProjectMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [ProjectView]
    list_title = 'Organization with Project'
    show_template = 'appbuilder/general/model/show_cascade.html'

class ScrapingTasksRawScrapedDataMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(ScrapingTasks)
    related_views = [RawScrapedDataView]
    list_title = 'Scraping Tasks with Raw Scraped Data'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationReportMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [ReportView]
    list_title = 'Organization with Report'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonSocialMediaProfileMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [SocialMediaProfileView]
    list_title = 'Person with Social Media Profile'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationSocialMediaProfileMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [SocialMediaProfileView]
    list_title = 'Organization with Social Media Profile'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationTrainingMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [TrainingView]
    list_title = 'Organization with Training'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonUserChallengeMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [UserChallengeView]
    list_title = 'Person with User Challenge'
    show_template = 'appbuilder/general/model/show_cascade.html'

class GamificationChallengeUserChallengeMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(GamificationChallenge)
    related_views = [UserChallengeView]
    list_title = 'Gamification Challenge with User Challenge'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationVolunteerLogMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [VolunteerLogView]
    list_title = 'Organization with Volunteer Log'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonVolunteerLogMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [VolunteerLogView]
    list_title = 'Person with Volunteer Log'
    show_template = 'appbuilder/general/model/show_cascade.html'

class EventEventRegistrationMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Event)
    related_views = [EventRegistrationView]
    list_title = 'Event with Event Registration'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonEventRegistrationMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [EventRegistrationView]
    list_title = 'Person with Event Registration'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationImpactMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [ImpactView]
    list_title = 'Organization with Impact'
    show_template = 'appbuilder/general/model/show_cascade.html'

class ProjectImpactMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Project)
    related_views = [ImpactView]
    list_title = 'Project with Impact'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPersonTrainingMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonTrainingView]
    list_title = 'Person with Person Training'
    show_template = 'appbuilder/general/model/show_cascade.html'

class TrainingPersonTrainingMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Training)
    related_views = [PersonTrainingView]
    list_title = 'Training with Person Training'
    show_template = 'appbuilder/general/model/show_cascade.html'

class OrganizationPjFeedbackMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Organization)
    related_views = [PjFeedbackView]
    list_title = 'Organization with Pj Feedback'
    show_template = 'appbuilder/general/model/show_cascade.html'

class ProjectPjFeedbackMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Project)
    related_views = [PjFeedbackView]
    list_title = 'Project with Pj Feedback'
    show_template = 'appbuilder/general/model/show_cascade.html'

class PersonPjFeedbackMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PjFeedbackView]
    list_title = 'Person with Pj Feedback'
    show_template = 'appbuilder/general/model/show_cascade.html'

class GeonameProjectLocationsMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Geoname)
    related_views = [ProjectLocationsView]
    list_title = 'Geoname with Project Locations'
    show_template = 'appbuilder/general/model/show_cascade.html'

class ProjectProjectLocationsMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Project)
    related_views = [ProjectLocationsView]
    list_title = 'Project with Project Locations'
    show_template = 'appbuilder/general/model/show_cascade.html'

class ProjectProjectTagMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Project)
    related_views = [ProjectTagView]
    list_title = 'Project with Project Tag'
    show_template = 'appbuilder/general/model/show_cascade.html'

class TagProjectTagMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Tag)
    related_views = [ProjectTagView]
    list_title = 'Tag with Project Tag'
    show_template = 'appbuilder/general/model/show_cascade.html'

class RawScrapedDataScrapedRfpsMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(RawScrapedData)
    related_views = [ScrapedRfpsView]
    list_title = 'Raw Scraped Data with Scraped Rfps'
    show_template = 'appbuilder/general/model/show_cascade.html'

class ScrapingTasksScrapedRfpsMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(ScrapingTasks)
    related_views = [ScrapedRfpsView]
    list_title = 'Scraping Tasks with Scraped Rfps'
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(AbUserAbUserMasterDetailView, 'Ab User - Ab User', icon='fa-link', category='Master-Detail')
appbuilder.add_view(AbUserAbUserMasterDetailView, 'Ab User - Ab User', icon='fa-link', category='Master-Detail')
appbuilder.add_view(GeonameCountryMasterDetailView, 'Geoname - Country', icon='fa-link', category='Master-Detail')
appbuilder.add_view(CountryGeonameMasterDetailView, 'Country - Geoname', icon='fa-link', category='Master-Detail')
appbuilder.add_view(AlternatenameGeonameMasterDetailView, 'Alternatename - Geoname', icon='fa-link', category='Master-Detail')
appbuilder.add_view(AbPermissionAbPermissionViewMasterDetailView, 'Ab Permission - Ab Permission View', icon='fa-link', category='Master-Detail')
appbuilder.add_view(AbViewMenuAbPermissionViewMasterDetailView, 'Ab View Menu - Ab Permission View', icon='fa-link', category='Master-Detail')
appbuilder.add_view(AbUserAbUserRoleMasterDetailView, 'Ab User - Ab User Role', icon='fa-link', category='Master-Detail')
appbuilder.add_view(AbRoleAbUserRoleMasterDetailView, 'Ab Role - Ab User Role', icon='fa-link', category='Master-Detail')
appbuilder.add_view(CountryAdmin1codesMasterDetailView, 'Country - Admin1codes', icon='fa-link', category='Master-Detail')
appbuilder.add_view(GeonameAdmin1codesMasterDetailView, 'Geoname - Admin1codes', icon='fa-link', category='Master-Detail')
appbuilder.add_view(CountryAdmin2codesMasterDetailView, 'Country - Admin2codes', icon='fa-link', category='Master-Detail')
appbuilder.add_view(GeonameAdmin2codesMasterDetailView, 'Geoname - Admin2codes', icon='fa-link', category='Master-Detail')
appbuilder.add_view(ContactTypeContactMasterDetailView, 'Contact Type - Contact', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonContactMasterDetailView, 'Person - Contact', icon='fa-link', category='Master-Detail')
appbuilder.add_view(BadgeGamificationChallengeMasterDetailView, 'Badge - Gamification Challenge', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonLeaderboardMasterDetailView, 'Person - Leaderboard', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonMessageMasterDetailView, 'Person - Message', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonMessageMasterDetailView, 'Person - Message', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonNotificationMasterDetailView, 'Person - Notification', icon='fa-link', category='Master-Detail')
appbuilder.add_view(CountryOrganizationMasterDetailView, 'Country - Organization', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonOrganizationMasterDetailView, 'Person - Organization', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPersonBadgeMasterDetailView, 'Person - Person Badge', icon='fa-link', category='Master-Detail')
appbuilder.add_view(BadgePersonBadgeMasterDetailView, 'Badge - Person Badge', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPersonCertificationMasterDetailView, 'Person - Person Certification', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPersonCourseMasterDetailView, 'Person - Person Course', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPersonEducationMasterDetailView, 'Person - Person Education', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPersonExperienceMasterDetailView, 'Person - Person Experience', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPersonHonorAwardMasterDetailView, 'Person - Person Honor Award', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPersonLanguageMasterDetailView, 'Person - Person Language', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPersonOrganizationMembershipMasterDetailView, 'Person - Person Organization Membership', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPersonPatentMasterDetailView, 'Person - Person Patent', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPersonProjectMasterDetailView, 'Person - Person Project', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPersonPublicationMasterDetailView, 'Person - Person Publication', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPersonVolunteerExperienceMasterDetailView, 'Person - Person Volunteer Experience', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPointEarningActivityMasterDetailView, 'Person - Point Earning Activity', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonProfileUpdateReminderMasterDetailView, 'Person - Profile Update Reminder', icon='fa-link', category='Master-Detail')
appbuilder.add_view(ScrapingTargetsScrapingRulesMasterDetailView, 'Scraping Targets - Scraping Rules', icon='fa-link', category='Master-Detail')
appbuilder.add_view(AbUserScrapingRulesMasterDetailView, 'Ab User - Scraping Rules', icon='fa-link', category='Master-Detail')
appbuilder.add_view(ScrapingTargetsScrapingTasksMasterDetailView, 'Scraping Targets - Scraping Tasks', icon='fa-link', category='Master-Detail')
appbuilder.add_view(SkillCategorySkillMasterDetailView, 'Skill Category - Skill', icon='fa-link', category='Master-Detail')
appbuilder.add_view(CountryTimezoneMasterDetailView, 'Country - Timezone', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonUserActivityMasterDetailView, 'Person - User Activity', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonUserGamificationMasterDetailView, 'Person - User Gamification', icon='fa-link', category='Master-Detail')
appbuilder.add_view(AbPermissionViewAbPermissionViewRoleMasterDetailView, 'Ab Permission View - Ab Permission View Role', icon='fa-link', category='Master-Detail')
appbuilder.add_view(AbRoleAbPermissionViewRoleMasterDetailView, 'Ab Role - Ab Permission View Role', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonBoardMemberMasterDetailView, 'Person - Board Member', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationBoardMemberMasterDetailView, 'Organization - Board Member', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonContactApplicationMasterDetailView, 'Person - Contact Application', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationContactApplicationMasterDetailView, 'Organization - Contact Application', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationDocumentSubmissionMasterDetailView, 'Organization - Document Submission', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationEventMasterDetailView, 'Organization - Event', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationExecutivePositionMasterDetailView, 'Organization - Executive Position', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonExecutivePositionMasterDetailView, 'Person - Executive Position', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationGrantMasterDetailView, 'Organization - Grant', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationGrantMasterDetailView, 'Organization - Grant', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonOnboardingProgressMasterDetailView, 'Person - Onboarding Progress', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationOnboardingProgressMasterDetailView, 'Organization - Onboarding Progress', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationOrganizationAwardMasterDetailView, 'Organization - Organization Award', icon='fa-link', category='Master-Detail')
appbuilder.add_view(BadgeOrganizationBadgeMasterDetailView, 'Badge - Organization Badge', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationOrganizationBadgeMasterDetailView, 'Organization - Organization Badge', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationOrganizationClimateCategoriesMasterDetailView, 'Organization - Organization Climate Categories', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationOrganizationContactMasterDetailView, 'Organization - Organization Contact', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonOrganizationContactMasterDetailView, 'Person - Organization Contact', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationOrganizationDocumentsMasterDetailView, 'Organization - Organization Documents', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationOrganizationHierarchyMasterDetailView, 'Organization - Organization Hierarchy', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationOrganizationHierarchyMasterDetailView, 'Organization - Organization Hierarchy', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationOrganizationProfileMasterDetailView, 'Organization - Organization Profile', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationOrganizationProgramsMasterDetailView, 'Organization - Organization Programs', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationOrganizationSdgsMasterDetailView, 'Organization - Organization Sdgs', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationOrganizationTagMasterDetailView, 'Organization - Organization Tag', icon='fa-link', category='Master-Detail')
appbuilder.add_view(TagOrganizationTagMasterDetailView, 'Tag - Organization Tag', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationOrganizationVerificationMasterDetailView, 'Organization - Organization Verification', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationPersonOrganizationClaimMasterDetailView, 'Organization - Person Organization Claim', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPersonOrganizationClaimMasterDetailView, 'Person - Person Organization Claim', icon='fa-link', category='Master-Detail')
appbuilder.add_view(SkillPersonSkillMasterDetailView, 'Skill - Person Skill', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPersonSkillMasterDetailView, 'Person - Person Skill', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationProjectMasterDetailView, 'Organization - Project', icon='fa-link', category='Master-Detail')
appbuilder.add_view(ScrapingTasksRawScrapedDataMasterDetailView, 'Scraping Tasks - Raw Scraped Data', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationReportMasterDetailView, 'Organization - Report', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonSocialMediaProfileMasterDetailView, 'Person - Social Media Profile', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationSocialMediaProfileMasterDetailView, 'Organization - Social Media Profile', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationTrainingMasterDetailView, 'Organization - Training', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonUserChallengeMasterDetailView, 'Person - User Challenge', icon='fa-link', category='Master-Detail')
appbuilder.add_view(GamificationChallengeUserChallengeMasterDetailView, 'Gamification Challenge - User Challenge', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationVolunteerLogMasterDetailView, 'Organization - Volunteer Log', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonVolunteerLogMasterDetailView, 'Person - Volunteer Log', icon='fa-link', category='Master-Detail')
appbuilder.add_view(EventEventRegistrationMasterDetailView, 'Event - Event Registration', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonEventRegistrationMasterDetailView, 'Person - Event Registration', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationImpactMasterDetailView, 'Organization - Impact', icon='fa-link', category='Master-Detail')
appbuilder.add_view(ProjectImpactMasterDetailView, 'Project - Impact', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPersonTrainingMasterDetailView, 'Person - Person Training', icon='fa-link', category='Master-Detail')
appbuilder.add_view(TrainingPersonTrainingMasterDetailView, 'Training - Person Training', icon='fa-link', category='Master-Detail')
appbuilder.add_view(OrganizationPjFeedbackMasterDetailView, 'Organization - Pj Feedback', icon='fa-link', category='Master-Detail')
appbuilder.add_view(ProjectPjFeedbackMasterDetailView, 'Project - Pj Feedback', icon='fa-link', category='Master-Detail')
appbuilder.add_view(PersonPjFeedbackMasterDetailView, 'Person - Pj Feedback', icon='fa-link', category='Master-Detail')
appbuilder.add_view(GeonameProjectLocationsMasterDetailView, 'Geoname - Project Locations', icon='fa-link', category='Master-Detail')
appbuilder.add_view(ProjectProjectLocationsMasterDetailView, 'Project - Project Locations', icon='fa-link', category='Master-Detail')
appbuilder.add_view(ProjectProjectTagMasterDetailView, 'Project - Project Tag', icon='fa-link', category='Master-Detail')
appbuilder.add_view(TagProjectTagMasterDetailView, 'Tag - Project Tag', icon='fa-link', category='Master-Detail')
appbuilder.add_view(RawScrapedDataScrapedRfpsMasterDetailView, 'Raw Scraped Data - Scraped Rfps', icon='fa-link', category='Master-Detail')
appbuilder.add_view(ScrapingTasksScrapedRfpsMasterDetailView, 'Scraping Tasks - Scraped Rfps', icon='fa-link', category='Master-Detail')
class AbRoleMultipleView(MultipleView):
    datamodel = SQLAInterface(AbRole)
    views = [AbPermissionViewRoleView, AbUserRoleView]

class AbUserMultipleView(MultipleView):
    datamodel = SQLAInterface(AbUser)
    views = [AbUserView, ScrapingRulesView, AbUserRoleView]

class BadgeMultipleView(MultipleView):
    datamodel = SQLAInterface(Badge)
    views = [PersonBadgeView, GamificationChallengeView, OrganizationBadgeView]

class CountryMultipleView(MultipleView):
    datamodel = SQLAInterface(Country)
    views = [TimezoneView, OrganizationView, GeonameView, Admin2codesView, Admin1codesView]

class GeonameMultipleView(MultipleView):
    datamodel = SQLAInterface(Geoname)
    views = [ProjectLocationsView, CountryView, Admin2codesView, AlternatenameView, Admin1codesView]

class PersonMultipleView(MultipleView):
    datamodel = SQLAInterface(Person)
    views = [PersonVolunteerExperienceView, PersonExperienceView, VolunteerLogView, PersonLanguageView, ExecutivePositionView, PersonPublicationView, UserChallengeView, ContactView, ProfileUpdateReminderView, PersonOrganizationClaimView, PersonCourseView, UserActivityView, PersonOrganizationMembershipView, NotificationView, PersonSkillView, PointEarningActivityView, OrganizationContactView, BoardMemberView, PjFeedbackView, PersonBadgeView, EventRegistrationView, MessageView, OrganizationView, SocialMediaProfileView, PersonTrainingView, UserGamificationView, PersonEducationView, PersonPatentView, PersonHonorAwardView, PersonProjectView, PersonCertificationView, OnboardingProgressView, LeaderboardView, ContactApplicationView]

class ScrapingTargetsMultipleView(MultipleView):
    datamodel = SQLAInterface(ScrapingTargets)
    views = [ScrapingRulesView, ScrapingTasksView]

class TagMultipleView(MultipleView):
    datamodel = SQLAInterface(Tag)
    views = [ProjectTagView, OrganizationTagView]

class AbPermissionViewMultipleView(MultipleView):
    datamodel = SQLAInterface(AbPermissionView)
    views = [AbPermissionViewRoleView, AbPermissionView, AbViewMenuView]

class AbUserRoleMultipleView(MultipleView):
    datamodel = SQLAInterface(AbUserRole)
    views = [AbUserView, AbRoleView]

class Admin1codesMultipleView(MultipleView):
    datamodel = SQLAInterface(Admin1codes)
    views = [GeonameView, CountryView]

class Admin2codesMultipleView(MultipleView):
    datamodel = SQLAInterface(Admin2codes)
    views = [GeonameView, CountryView]

class ContactMultipleView(MultipleView):
    datamodel = SQLAInterface(Contact)
    views = [ContactTypeView, PersonView]

class GamificationChallengeMultipleView(MultipleView):
    datamodel = SQLAInterface(GamificationChallenge)
    views = [BadgeView, UserChallengeView]

class OrganizationMultipleView(MultipleView):
    datamodel = SQLAInterface(Organization)
    views = [OrganizationDocumentsView, VolunteerLogView, OrganizationTagView, OrganizationAwardView, OrganizationHierarchyView, ExecutivePositionView, ImpactView, CountryView, OrganizationClimateCategoriesView, OrganizationVerificationView, TrainingView, PersonOrganizationClaimView, DocumentSubmissionView, GrantView, ProjectView, OrganizationBadgeView, ReportView, OrganizationContactView, BoardMemberView, PjFeedbackView, SocialMediaProfileView, OrganizationProgramsView, OrganizationProfileView, PersonView, EventView, OnboardingProgressView, ContactApplicationView, OrganizationSdgsView]

class PersonBadgeMultipleView(MultipleView):
    datamodel = SQLAInterface(PersonBadge)
    views = [PersonView, BadgeView]

class ScrapingRulesMultipleView(MultipleView):
    datamodel = SQLAInterface(ScrapingRules)
    views = [AbUserView, ScrapingTargetsView]

class ScrapingTasksMultipleView(MultipleView):
    datamodel = SQLAInterface(ScrapingTasks)
    views = [ScrapedRfpsView, RawScrapedDataView, ScrapingTargetsView]

class SkillMultipleView(MultipleView):
    datamodel = SQLAInterface(Skill)
    views = [PersonSkillView, SkillCategoryView]

class AbPermissionViewRoleMultipleView(MultipleView):
    datamodel = SQLAInterface(AbPermissionViewRole)
    views = [AbRoleView, AbPermissionViewView]

class BoardMemberMultipleView(MultipleView):
    datamodel = SQLAInterface(BoardMember)
    views = [OrganizationView, PersonView]

class ContactApplicationMultipleView(MultipleView):
    datamodel = SQLAInterface(ContactApplication)
    views = [OrganizationView, PersonView]

class EventMultipleView(MultipleView):
    datamodel = SQLAInterface(Event)
    views = [EventRegistrationView, OrganizationView]

class ExecutivePositionMultipleView(MultipleView):
    datamodel = SQLAInterface(ExecutivePosition)
    views = [OrganizationView, PersonView]

class OnboardingProgressMultipleView(MultipleView):
    datamodel = SQLAInterface(OnboardingProgress)
    views = [OrganizationView, PersonView]

class OrganizationBadgeMultipleView(MultipleView):
    datamodel = SQLAInterface(OrganizationBadge)
    views = [OrganizationView, BadgeView]

class OrganizationContactMultipleView(MultipleView):
    datamodel = SQLAInterface(OrganizationContact)
    views = [OrganizationView, PersonView]

class OrganizationTagMultipleView(MultipleView):
    datamodel = SQLAInterface(OrganizationTag)
    views = [TagView, OrganizationView]

class PersonOrganizationClaimMultipleView(MultipleView):
    datamodel = SQLAInterface(PersonOrganizationClaim)
    views = [OrganizationView, PersonView]

class PersonSkillMultipleView(MultipleView):
    datamodel = SQLAInterface(PersonSkill)
    views = [SkillView, PersonView]

class ProjectMultipleView(MultipleView):
    datamodel = SQLAInterface(Project)
    views = [ProjectLocationsView, PjFeedbackView, ImpactView, OrganizationView, ProjectTagView]

class RawScrapedDataMultipleView(MultipleView):
    datamodel = SQLAInterface(RawScrapedData)
    views = [ScrapedRfpsView, ScrapingTasksView]

class SocialMediaProfileMultipleView(MultipleView):
    datamodel = SQLAInterface(SocialMediaProfile)
    views = [OrganizationView, PersonView]

class TrainingMultipleView(MultipleView):
    datamodel = SQLAInterface(Training)
    views = [PersonTrainingView, OrganizationView]

class UserChallengeMultipleView(MultipleView):
    datamodel = SQLAInterface(UserChallenge)
    views = [GamificationChallengeView, PersonView]

class VolunteerLogMultipleView(MultipleView):
    datamodel = SQLAInterface(VolunteerLog)
    views = [OrganizationView, PersonView]

class EventRegistrationMultipleView(MultipleView):
    datamodel = SQLAInterface(EventRegistration)
    views = [EventView, PersonView]

class ImpactMultipleView(MultipleView):
    datamodel = SQLAInterface(Impact)
    views = [OrganizationView, ProjectView]

class PersonTrainingMultipleView(MultipleView):
    datamodel = SQLAInterface(PersonTraining)
    views = [TrainingView, PersonView]

class PjFeedbackMultipleView(MultipleView):
    datamodel = SQLAInterface(PjFeedback)
    views = [PersonView, OrganizationView, ProjectView]

class ProjectLocationsMultipleView(MultipleView):
    datamodel = SQLAInterface(ProjectLocations)
    views = [GeonameView, ProjectView]

class ProjectTagMultipleView(MultipleView):
    datamodel = SQLAInterface(ProjectTag)
    views = [TagView, ProjectView]

class ScrapedRfpsMultipleView(MultipleView):
    datamodel = SQLAInterface(ScrapedRfps)
    views = [RawScrapedDataView, ScrapingTasksView]

appbuilder.add_view(AbRoleMultipleView, 'Ab Role Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(AbUserMultipleView, 'Ab User Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(BadgeMultipleView, 'Badge Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(CountryMultipleView, 'Country Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(GeonameMultipleView, 'Geoname Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(PersonMultipleView, 'Person Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(ScrapingTargetsMultipleView, 'Scraping Targets Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(TagMultipleView, 'Tag Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(AbPermissionViewMultipleView, 'Ab Permission View Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(AbUserRoleMultipleView, 'Ab User Role Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(Admin1codesMultipleView, 'Admin1codes Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(Admin2codesMultipleView, 'Admin2codes Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(ContactMultipleView, 'Contact Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(GamificationChallengeMultipleView, 'Gamification Challenge Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(OrganizationMultipleView, 'Organization Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(PersonBadgeMultipleView, 'Person Badge Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(ScrapingRulesMultipleView, 'Scraping Rules Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(ScrapingTasksMultipleView, 'Scraping Tasks Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(SkillMultipleView, 'Skill Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(AbPermissionViewRoleMultipleView, 'Ab Permission View Role Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(BoardMemberMultipleView, 'Board Member Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(ContactApplicationMultipleView, 'Contact Application Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(EventMultipleView, 'Event Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(ExecutivePositionMultipleView, 'Executive Position Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(OnboardingProgressMultipleView, 'Onboarding Progress Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(OrganizationBadgeMultipleView, 'Organization Badge Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(OrganizationContactMultipleView, 'Organization Contact Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(OrganizationTagMultipleView, 'Organization Tag Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(PersonOrganizationClaimMultipleView, 'Person Organization Claim Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(PersonSkillMultipleView, 'Person Skill Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(ProjectMultipleView, 'Project Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(RawScrapedDataMultipleView, 'Raw Scraped Data Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(SocialMediaProfileMultipleView, 'Social Media Profile Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(TrainingMultipleView, 'Training Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(UserChallengeMultipleView, 'User Challenge Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(VolunteerLogMultipleView, 'Volunteer Log Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(EventRegistrationMultipleView, 'Event Registration Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(ImpactMultipleView, 'Impact Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(PersonTrainingMultipleView, 'Person Training Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(PjFeedbackMultipleView, 'Pj Feedback Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(ProjectLocationsMultipleView, 'Project Locations Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(ProjectTagMultipleView, 'Project Tag Multiple', icon='fa-cubes', category='Multiple Views')
appbuilder.add_view(ScrapedRfpsMultipleView, 'Scraped Rfps Multiple', icon='fa-cubes', category='Multiple Views')

# View registrations
appbuilder.add_view(AbPermissionView, 'Ab Permission', icon='fa-table', category='Data')
appbuilder.add_view(AbRegisterUserView, 'Ab Register User', icon='fa-table', category='Data')
appbuilder.add_view(AbRoleView, 'Ab Role', icon='fa-table', category='Data')
appbuilder.add_view(AbUserView, 'Ab User', icon='fa-table', category='Data')
appbuilder.add_view(AbViewMenuView, 'Ab View Menu', icon='fa-table', category='Data')
appbuilder.add_view(AlternatenameView, 'Alternatename', icon='fa-table', category='Data')
appbuilder.add_view(BadgeView, 'Badge', icon='fa-table', category='Data')
appbuilder.add_view(ContactTypeView, 'Contact Type', icon='fa-table', category='Data')
appbuilder.add_view(CountryView, 'Country', icon='fa-table', category='Data')
appbuilder.add_view(CurrencyView, 'Currency', icon='fa-table', category='Data')
appbuilder.add_view(FeaturecodesView, 'Featurecodes', icon='fa-table', category='Data')
appbuilder.add_view(GeonameView, 'Geoname', icon='fa-table', category='Data')
appbuilder.add_view(LanguagecodesView, 'Languagecodes', icon='fa-table', category='Data')
appbuilder.add_view(PersonView, 'Person', icon='fa-table', category='Data')
appbuilder.add_view(ScrapingTargetsView, 'Scraping Targets', icon='fa-table', category='Data')
appbuilder.add_view(SkillCategoryView, 'Skill Category', icon='fa-table', category='Data')
appbuilder.add_view(TagView, 'Tag', icon='fa-table', category='Data')
appbuilder.add_view(AbPermissionViewView, 'Ab Permission View', icon='fa-table', category='Data')
appbuilder.add_view(AbUserRoleView, 'Ab User Role', icon='fa-table', category='Data')
appbuilder.add_view(Admin1codesView, 'Admin1codes', icon='fa-table', category='Data')
appbuilder.add_view(Admin2codesView, 'Admin2codes', icon='fa-table', category='Data')
appbuilder.add_view(ContactView, 'Contact', icon='fa-table', category='Data')
appbuilder.add_view(GamificationChallengeView, 'Gamification Challenge', icon='fa-table', category='Data')
appbuilder.add_view(LeaderboardView, 'Leaderboard', icon='fa-table', category='Data')
appbuilder.add_view(MessageView, 'Message', icon='fa-table', category='Data')
appbuilder.add_view(NotificationView, 'Notification', icon='fa-table', category='Data')
appbuilder.add_view(OrganizationView, 'Organization', icon='fa-table', category='Data')
appbuilder.add_view(PersonBadgeView, 'Person Badge', icon='fa-table', category='Data')
appbuilder.add_view(PersonCertificationView, 'Person Certification', icon='fa-table', category='Data')
appbuilder.add_view(PersonCourseView, 'Person Course', icon='fa-table', category='Data')
appbuilder.add_view(PersonEducationView, 'Person Education', icon='fa-table', category='Data')
appbuilder.add_view(PersonExperienceView, 'Person Experience', icon='fa-table', category='Data')
appbuilder.add_view(PersonHonorAwardView, 'Person Honor Award', icon='fa-table', category='Data')
appbuilder.add_view(PersonLanguageView, 'Person Language', icon='fa-table', category='Data')
appbuilder.add_view(PersonOrganizationMembershipView, 'Person Organization Membership', icon='fa-table', category='Data')
appbuilder.add_view(PersonPatentView, 'Person Patent', icon='fa-table', category='Data')
appbuilder.add_view(PersonProjectView, 'Person Project', icon='fa-table', category='Data')
appbuilder.add_view(PersonPublicationView, 'Person Publication', icon='fa-table', category='Data')
appbuilder.add_view(PersonVolunteerExperienceView, 'Person Volunteer Experience', icon='fa-table', category='Data')
appbuilder.add_view(PointEarningActivityView, 'Point Earning Activity', icon='fa-table', category='Data')
appbuilder.add_view(ProfileUpdateReminderView, 'Profile Update Reminder', icon='fa-table', category='Data')
appbuilder.add_view(ScrapingRulesView, 'Scraping Rules', icon='fa-table', category='Data')
appbuilder.add_view(ScrapingTasksView, 'Scraping Tasks', icon='fa-table', category='Data')
appbuilder.add_view(SkillView, 'Skill', icon='fa-table', category='Data')
appbuilder.add_view(TimezoneView, 'Timezone', icon='fa-table', category='Data')
appbuilder.add_view(UserActivityView, 'User Activity', icon='fa-table', category='Data')
appbuilder.add_view(UserGamificationView, 'User Gamification', icon='fa-table', category='Data')
appbuilder.add_view(AbPermissionViewRoleView, 'Ab Permission View Role', icon='fa-table', category='Data')
appbuilder.add_view(BoardMemberView, 'Board Member', icon='fa-table', category='Data')
appbuilder.add_view(ContactApplicationView, 'Contact Application', icon='fa-table', category='Data')
appbuilder.add_view(DocumentSubmissionView, 'Document Submission', icon='fa-table', category='Data')
appbuilder.add_view(EventView, 'Event', icon='fa-table', category='Data')
appbuilder.add_view(ExecutivePositionView, 'Executive Position', icon='fa-table', category='Data')
appbuilder.add_view(GrantView, 'Grant', icon='fa-table', category='Data')
appbuilder.add_view(OnboardingProgressView, 'Onboarding Progress', icon='fa-table', category='Data')
appbuilder.add_view(OrganizationAwardView, 'Organization Award', icon='fa-table', category='Data')
appbuilder.add_view(OrganizationBadgeView, 'Organization Badge', icon='fa-table', category='Data')
appbuilder.add_view(OrganizationClimateCategoriesView, 'Organization Climate Categories', icon='fa-table', category='Data')
appbuilder.add_view(OrganizationContactView, 'Organization Contact', icon='fa-table', category='Data')
appbuilder.add_view(OrganizationDocumentsView, 'Organization Documents', icon='fa-table', category='Data')
appbuilder.add_view(OrganizationHierarchyView, 'Organization Hierarchy', icon='fa-table', category='Data')
appbuilder.add_view(OrganizationProfileView, 'Organization Profile', icon='fa-table', category='Data')
appbuilder.add_view(OrganizationProgramsView, 'Organization Programs', icon='fa-table', category='Data')
appbuilder.add_view(OrganizationSdgsView, 'Organization Sdgs', icon='fa-table', category='Data')
appbuilder.add_view(OrganizationTagView, 'Organization Tag', icon='fa-table', category='Data')
appbuilder.add_view(OrganizationVerificationView, 'Organization Verification', icon='fa-table', category='Data')
appbuilder.add_view(PersonOrganizationClaimView, 'Person Organization Claim', icon='fa-table', category='Data')
appbuilder.add_view(PersonSkillView, 'Person Skill', icon='fa-table', category='Data')
appbuilder.add_view(ProjectView, 'Project', icon='fa-table', category='Data')
appbuilder.add_view(RawScrapedDataView, 'Raw Scraped Data', icon='fa-table', category='Data')
appbuilder.add_view(ReportView, 'Report', icon='fa-table', category='Data')
appbuilder.add_view(SocialMediaProfileView, 'Social Media Profile', icon='fa-table', category='Data')
appbuilder.add_view(TrainingView, 'Training', icon='fa-table', category='Data')
appbuilder.add_view(UserChallengeView, 'User Challenge', icon='fa-table', category='Data')
appbuilder.add_view(VolunteerLogView, 'Volunteer Log', icon='fa-table', category='Data')
appbuilder.add_view(EventRegistrationView, 'Event Registration', icon='fa-table', category='Data')
appbuilder.add_view(ImpactView, 'Impact', icon='fa-table', category='Data')
appbuilder.add_view(PersonTrainingView, 'Person Training', icon='fa-table', category='Data')
appbuilder.add_view(PjFeedbackView, 'Pj Feedback', icon='fa-table', category='Data')
appbuilder.add_view(ProjectLocationsView, 'Project Locations', icon='fa-table', category='Data')
appbuilder.add_view(ProjectTagView, 'Project Tag', icon='fa-table', category='Data')
appbuilder.add_view(ScrapedRfpsView, 'Scraped Rfps', icon='fa-table', category='Data')