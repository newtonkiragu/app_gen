
# coding: utf-8
# AUTOGENERATED BY appgen
# Copyright (C) Nyimbi Odero, 2024
 


from flask_appbuilder import ModelRestApi
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.api import BaseApi, expose
from flask_appbuilder.models.filters import BaseFilter
from sqlalchemy import or_
from sqlalchemy.sql import text

from . import appbuilder, db
from .models import *


class BadgeApi(ModelRestApi):
    resource = "badge"
    datamodel = SQLAInterface(Badge)
    allow_browser_login = True
 
appbuilder.add_api(BadgeApi)



class ContactTypeApi(ModelRestApi):
    resource = "contact_type"
    datamodel = SQLAInterface(ContactType)
    allow_browser_login = True
 
appbuilder.add_api(ContactTypeApi)



class CurrencyApi(ModelRestApi):
    resource = "currency"
    datamodel = SQLAInterface(Currency)
    allow_browser_login = True
 
appbuilder.add_api(CurrencyApi)



class FeaturecodesApi(ModelRestApi):
    resource = "featurecodes"
    datamodel = SQLAInterface(Featurecodes)
    allow_browser_login = True
 
appbuilder.add_api(FeaturecodesApi)



class GeonameApi(ModelRestApi):
    resource = "geoname"
    datamodel = SQLAInterface(Geoname)
    allow_browser_login = True
 
appbuilder.add_api(GeonameApi)



class LanguagecodesApi(ModelRestApi):
    resource = "languagecodes"
    datamodel = SQLAInterface(Languagecodes)
    allow_browser_login = True
 
appbuilder.add_api(LanguagecodesApi)



class PersonApi(ModelRestApi):
    resource = "person"
    datamodel = SQLAInterface(Person)
    allow_browser_login = True
 
appbuilder.add_api(PersonApi)



class SkillCategoryApi(ModelRestApi):
    resource = "skill_category"
    datamodel = SQLAInterface(SkillCategory)
    allow_browser_login = True
 
appbuilder.add_api(SkillCategoryApi)



class TagApi(ModelRestApi):
    resource = "tag"
    datamodel = SQLAInterface(Tag)
    allow_browser_login = True
 
appbuilder.add_api(TagApi)



class AlternatenameApi(ModelRestApi):
    resource = "alternatename"
    datamodel = SQLAInterface(Alternatename)
    allow_browser_login = True
 
appbuilder.add_api(AlternatenameApi)



class ContactApi(ModelRestApi):
    resource = "contact"
    datamodel = SQLAInterface(Contact)
    allow_browser_login = True
 
appbuilder.add_api(ContactApi)



class CountryApi(ModelRestApi):
    resource = "country"
    datamodel = SQLAInterface(Country)
    allow_browser_login = True
 
appbuilder.add_api(CountryApi)



class GamificationChallengeApi(ModelRestApi):
    resource = "gamification_challenge"
    datamodel = SQLAInterface(GamificationChallenge)
    allow_browser_login = True
 
appbuilder.add_api(GamificationChallengeApi)



class LeaderboardApi(ModelRestApi):
    resource = "leaderboard"
    datamodel = SQLAInterface(Leaderboard)
    allow_browser_login = True
 
appbuilder.add_api(LeaderboardApi)



class MessageApi(ModelRestApi):
    resource = "message"
    datamodel = SQLAInterface(Message)
    allow_browser_login = True
 
appbuilder.add_api(MessageApi)



class NotificationApi(ModelRestApi):
    resource = "notification"
    datamodel = SQLAInterface(Notification)
    allow_browser_login = True
 
appbuilder.add_api(NotificationApi)



class PersonBadgeApi(ModelRestApi):
    resource = "person_badge"
    datamodel = SQLAInterface(PersonBadge)
    allow_browser_login = True
 
appbuilder.add_api(PersonBadgeApi)



class PersonCertificationApi(ModelRestApi):
    resource = "person_certification"
    datamodel = SQLAInterface(PersonCertification)
    allow_browser_login = True
 
appbuilder.add_api(PersonCertificationApi)



class PersonCourseApi(ModelRestApi):
    resource = "person_course"
    datamodel = SQLAInterface(PersonCourse)
    allow_browser_login = True
 
appbuilder.add_api(PersonCourseApi)



class PersonEducationApi(ModelRestApi):
    resource = "person_education"
    datamodel = SQLAInterface(PersonEducation)
    allow_browser_login = True
 
appbuilder.add_api(PersonEducationApi)



class PersonExperienceApi(ModelRestApi):
    resource = "person_experience"
    datamodel = SQLAInterface(PersonExperience)
    allow_browser_login = True
 
appbuilder.add_api(PersonExperienceApi)



class PersonHonorAwardApi(ModelRestApi):
    resource = "person_honor_award"
    datamodel = SQLAInterface(PersonHonorAward)
    allow_browser_login = True
 
appbuilder.add_api(PersonHonorAwardApi)



class PersonLanguageApi(ModelRestApi):
    resource = "person_language"
    datamodel = SQLAInterface(PersonLanguage)
    allow_browser_login = True
 
appbuilder.add_api(PersonLanguageApi)



class PersonOrganizationMembershipApi(ModelRestApi):
    resource = "person_organization_membership"
    datamodel = SQLAInterface(PersonOrganizationMembership)
    allow_browser_login = True
 
appbuilder.add_api(PersonOrganizationMembershipApi)



class PersonPatentApi(ModelRestApi):
    resource = "person_patent"
    datamodel = SQLAInterface(PersonPatent)
    allow_browser_login = True
 
appbuilder.add_api(PersonPatentApi)



class PersonProjectApi(ModelRestApi):
    resource = "person_project"
    datamodel = SQLAInterface(PersonProject)
    allow_browser_login = True
 
appbuilder.add_api(PersonProjectApi)



class PersonPublicationApi(ModelRestApi):
    resource = "person_publication"
    datamodel = SQLAInterface(PersonPublication)
    allow_browser_login = True
 
appbuilder.add_api(PersonPublicationApi)



class PersonVolunteerExperienceApi(ModelRestApi):
    resource = "person_volunteer_experience"
    datamodel = SQLAInterface(PersonVolunteerExperience)
    allow_browser_login = True
 
appbuilder.add_api(PersonVolunteerExperienceApi)



class PointEarningActivityApi(ModelRestApi):
    resource = "point_earning_activity"
    datamodel = SQLAInterface(PointEarningActivity)
    allow_browser_login = True
 
appbuilder.add_api(PointEarningActivityApi)



class ProfileUpdateReminderApi(ModelRestApi):
    resource = "profile_update_reminder"
    datamodel = SQLAInterface(ProfileUpdateReminder)
    allow_browser_login = True
 
appbuilder.add_api(ProfileUpdateReminderApi)



class SkillApi(ModelRestApi):
    resource = "skill"
    datamodel = SQLAInterface(Skill)
    allow_browser_login = True
 
appbuilder.add_api(SkillApi)



class UserActivityApi(ModelRestApi):
    resource = "user_activity"
    datamodel = SQLAInterface(UserActivity)
    allow_browser_login = True
 
appbuilder.add_api(UserActivityApi)



class UserGamificationApi(ModelRestApi):
    resource = "user_gamification"
    datamodel = SQLAInterface(UserGamification)
    allow_browser_login = True
 
appbuilder.add_api(UserGamificationApi)



class Admin1codesApi(ModelRestApi):
    resource = "admin1codes"
    datamodel = SQLAInterface(Admin1codes)
    allow_browser_login = True
 
appbuilder.add_api(Admin1codesApi)



class Admin2codesApi(ModelRestApi):
    resource = "admin2codes"
    datamodel = SQLAInterface(Admin2codes)
    allow_browser_login = True
 
appbuilder.add_api(Admin2codesApi)



class OrganizationApi(ModelRestApi):
    resource = "organization"
    datamodel = SQLAInterface(Organization)
    allow_browser_login = True
 
appbuilder.add_api(OrganizationApi)



class PersonSkillApi(ModelRestApi):
    resource = "person_skill"
    datamodel = SQLAInterface(PersonSkill)
    allow_browser_login = True
 
appbuilder.add_api(PersonSkillApi)



class TimezoneApi(ModelRestApi):
    resource = "timezone"
    datamodel = SQLAInterface(Timezone)
    allow_browser_login = True
 
appbuilder.add_api(TimezoneApi)



class UserChallengeApi(ModelRestApi):
    resource = "user_challenge"
    datamodel = SQLAInterface(UserChallenge)
    allow_browser_login = True
 
appbuilder.add_api(UserChallengeApi)



class BoardMemberApi(ModelRestApi):
    resource = "board_member"
    datamodel = SQLAInterface(BoardMember)
    allow_browser_login = True
 
appbuilder.add_api(BoardMemberApi)



class ContactApplicationApi(ModelRestApi):
    resource = "contact_application"
    datamodel = SQLAInterface(ContactApplication)
    allow_browser_login = True
 
appbuilder.add_api(ContactApplicationApi)



class DocumentSubmissionApi(ModelRestApi):
    resource = "document_submission"
    datamodel = SQLAInterface(DocumentSubmission)
    allow_browser_login = True
 
appbuilder.add_api(DocumentSubmissionApi)



class EventApi(ModelRestApi):
    resource = "event"
    datamodel = SQLAInterface(Event)
    allow_browser_login = True
 
appbuilder.add_api(EventApi)



class ExecutivePositionApi(ModelRestApi):
    resource = "executive_position"
    datamodel = SQLAInterface(ExecutivePosition)
    allow_browser_login = True
 
appbuilder.add_api(ExecutivePositionApi)



class GrantApi(ModelRestApi):
    resource = "grant"
    datamodel = SQLAInterface(Grant)
    allow_browser_login = True
 
appbuilder.add_api(GrantApi)



class OnboardingProgressApi(ModelRestApi):
    resource = "onboarding_progress"
    datamodel = SQLAInterface(OnboardingProgress)
    allow_browser_login = True
 
appbuilder.add_api(OnboardingProgressApi)



class OrganizationAwardApi(ModelRestApi):
    resource = "organization_award"
    datamodel = SQLAInterface(OrganizationAward)
    allow_browser_login = True
 
appbuilder.add_api(OrganizationAwardApi)



class OrganizationBadgeApi(ModelRestApi):
    resource = "organization_badge"
    datamodel = SQLAInterface(OrganizationBadge)
    allow_browser_login = True
 
appbuilder.add_api(OrganizationBadgeApi)



class OrganizationClimateCategoriesApi(ModelRestApi):
    resource = "organization_climate_categories"
    datamodel = SQLAInterface(OrganizationClimateCategories)
    allow_browser_login = True
 
appbuilder.add_api(OrganizationClimateCategoriesApi)



class OrganizationContactApi(ModelRestApi):
    resource = "organization_contact"
    datamodel = SQLAInterface(OrganizationContact)
    allow_browser_login = True
 
appbuilder.add_api(OrganizationContactApi)



class OrganizationDocumentsApi(ModelRestApi):
    resource = "organization_documents"
    datamodel = SQLAInterface(OrganizationDocuments)
    allow_browser_login = True
 
appbuilder.add_api(OrganizationDocumentsApi)



class OrganizationHierarchyApi(ModelRestApi):
    resource = "organization_hierarchy"
    datamodel = SQLAInterface(OrganizationHierarchy)
    allow_browser_login = True
 
appbuilder.add_api(OrganizationHierarchyApi)



class OrganizationProfileApi(ModelRestApi):
    resource = "organization_profile"
    datamodel = SQLAInterface(OrganizationProfile)
    allow_browser_login = True
 
appbuilder.add_api(OrganizationProfileApi)



class OrganizationProgramsApi(ModelRestApi):
    resource = "organization_programs"
    datamodel = SQLAInterface(OrganizationPrograms)
    allow_browser_login = True
 
appbuilder.add_api(OrganizationProgramsApi)



class OrganizationSdgsApi(ModelRestApi):
    resource = "organization_sdgs"
    datamodel = SQLAInterface(OrganizationSdgs)
    allow_browser_login = True
 
appbuilder.add_api(OrganizationSdgsApi)



class OrganizationTagApi(ModelRestApi):
    resource = "organization_tag"
    datamodel = SQLAInterface(OrganizationTag)
    allow_browser_login = True
 
appbuilder.add_api(OrganizationTagApi)



class OrganizationVerificationApi(ModelRestApi):
    resource = "organization_verification"
    datamodel = SQLAInterface(OrganizationVerification)
    allow_browser_login = True
 
appbuilder.add_api(OrganizationVerificationApi)



class PersonOrganizationClaimApi(ModelRestApi):
    resource = "person_organization_claim"
    datamodel = SQLAInterface(PersonOrganizationClaim)
    allow_browser_login = True
 
appbuilder.add_api(PersonOrganizationClaimApi)



class ProjectApi(ModelRestApi):
    resource = "project"
    datamodel = SQLAInterface(Project)
    allow_browser_login = True
 
appbuilder.add_api(ProjectApi)



class ReportApi(ModelRestApi):
    resource = "report"
    datamodel = SQLAInterface(Report)
    allow_browser_login = True
 
appbuilder.add_api(ReportApi)



class SocialMediaProfileApi(ModelRestApi):
    resource = "social_media_profile"
    datamodel = SQLAInterface(SocialMediaProfile)
    allow_browser_login = True
 
appbuilder.add_api(SocialMediaProfileApi)



class TrainingApi(ModelRestApi):
    resource = "training"
    datamodel = SQLAInterface(Training)
    allow_browser_login = True
 
appbuilder.add_api(TrainingApi)



class VolunteerLogApi(ModelRestApi):
    resource = "volunteer_log"
    datamodel = SQLAInterface(VolunteerLog)
    allow_browser_login = True
 
appbuilder.add_api(VolunteerLogApi)



class EventRegistrationApi(ModelRestApi):
    resource = "event_registration"
    datamodel = SQLAInterface(EventRegistration)
    allow_browser_login = True
 
appbuilder.add_api(EventRegistrationApi)



class ImpactApi(ModelRestApi):
    resource = "impact"
    datamodel = SQLAInterface(Impact)
    allow_browser_login = True
 
appbuilder.add_api(ImpactApi)



class PersonTrainingApi(ModelRestApi):
    resource = "person_training"
    datamodel = SQLAInterface(PersonTraining)
    allow_browser_login = True
 
appbuilder.add_api(PersonTrainingApi)



class PjFeedbackApi(ModelRestApi):
    resource = "pj_feedback"
    datamodel = SQLAInterface(PjFeedback)
    allow_browser_login = True
 
appbuilder.add_api(PjFeedbackApi)



class ProjectLocationsApi(ModelRestApi):
    resource = "project_locations"
    datamodel = SQLAInterface(ProjectLocations)
    allow_browser_login = True
 
appbuilder.add_api(ProjectLocationsApi)



class ProjectTagApi(ModelRestApi):
    resource = "project_tag"
    datamodel = SQLAInterface(ProjectTag)
    allow_browser_login = True
 
appbuilder.add_api(ProjectTagApi)

