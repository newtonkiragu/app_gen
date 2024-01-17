
from flask_appbuilder import ModelRestApi
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.api import BaseApi, expose
from flask_appbuilder.models.filters import BaseFilter
from sqlalchemy import or_
from sqlalchemy.sql import text

from . import appbuilder, db
from .models import *


class AgentTierApi(ModelRestApi):
    resource = "agent_tier"
    datamodel = SQLAInterface(AgentTier)
    allow_browser_login = True
 
appbuilder.add_api(AgentTierApi)



class BankApi(ModelRestApi):
    resource = "bank"
    datamodel = SQLAInterface(Bank)
    allow_browser_login = True
 
appbuilder.add_api(BankApi)



class BillerCategoryApi(ModelRestApi):
    resource = "biller_category"
    datamodel = SQLAInterface(BillerCategory)
    allow_browser_login = True
 
appbuilder.add_api(BillerCategoryApi)



class ContactTypeApi(ModelRestApi):
    resource = "contact_type"
    datamodel = SQLAInterface(ContactType)
    allow_browser_login = True
 
appbuilder.add_api(ContactTypeApi)



class CountryApi(ModelRestApi):
    resource = "country"
    datamodel = SQLAInterface(Country)
    allow_browser_login = True
 
appbuilder.add_api(CountryApi)



class CouponApi(ModelRestApi):
    resource = "coupon"
    datamodel = SQLAInterface(Coupon)
    allow_browser_login = True
 
appbuilder.add_api(CouponApi)



class CurrencyApi(ModelRestApi):
    resource = "currency"
    datamodel = SQLAInterface(Currency)
    allow_browser_login = True
 
appbuilder.add_api(CurrencyApi)



class CustomerSegmentApi(ModelRestApi):
    resource = "customer_segment"
    datamodel = SQLAInterface(CustomerSegment)
    allow_browser_login = True
 
appbuilder.add_api(CustomerSegmentApi)



class DocTypeApi(ModelRestApi):
    resource = "doc_type"
    datamodel = SQLAInterface(DocType)
    allow_browser_login = True
 
appbuilder.add_api(DocTypeApi)



class MimeTypeApi(ModelRestApi):
    resource = "mime_type"
    datamodel = SQLAInterface(MimeType)
    allow_browser_login = True
 
appbuilder.add_api(MimeTypeApi)



class MimeTypeMapApi(ModelRestApi):
    resource = "mime_type_map"
    datamodel = SQLAInterface(MimeTypeMap)
    allow_browser_login = True
 
appbuilder.add_api(MimeTypeMapApi)



class PaymentCardApi(ModelRestApi):
    resource = "payment_card"
    datamodel = SQLAInterface(PaymentCard)
    allow_browser_login = True
 
appbuilder.add_api(PaymentCardApi)



class PromotionApi(ModelRestApi):
    resource = "promotion"
    datamodel = SQLAInterface(Promotion)
    allow_browser_login = True
 
appbuilder.add_api(PromotionApi)



class TechparamsApi(ModelRestApi):
    resource = "techparams"
    datamodel = SQLAInterface(Techparams)
    allow_browser_login = True
 
appbuilder.add_api(TechparamsApi)



class TokenProviderApi(ModelRestApi):
    resource = "token_provider"
    datamodel = SQLAInterface(TokenProvider)
    allow_browser_login = True
 
appbuilder.add_api(TokenProviderApi)



class TransRoutingThresholdsApi(ModelRestApi):
    resource = "trans_routing_thresholds"
    datamodel = SQLAInterface(TransRoutingThresholds)
    allow_browser_login = True
 
appbuilder.add_api(TransRoutingThresholdsApi)



class TransTypeApi(ModelRestApi):
    resource = "trans_type"
    datamodel = SQLAInterface(TransType)
    allow_browser_login = True
 
appbuilder.add_api(TransTypeApi)



class UserExtApi(ModelRestApi):
    resource = "user_ext"
    datamodel = SQLAInterface(UserExt)
    allow_browser_login = True
 
appbuilder.add_api(UserExtApi)



class BillerApi(ModelRestApi):
    resource = "biller"
    datamodel = SQLAInterface(Biller)
    allow_browser_login = True
 
appbuilder.add_api(BillerApi)



class StateApi(ModelRestApi):
    resource = "state"
    datamodel = SQLAInterface(State)
    allow_browser_login = True
 
appbuilder.add_api(StateApi)



class TokenApi(ModelRestApi):
    resource = "token"
    datamodel = SQLAInterface(Token)
    allow_browser_login = True
 
appbuilder.add_api(TokenApi)



class BillerOfferingApi(ModelRestApi):
    resource = "biller_offering"
    datamodel = SQLAInterface(BillerOffering)
    allow_browser_login = True
 
appbuilder.add_api(BillerOfferingApi)



class LgaApi(ModelRestApi):
    resource = "lga"
    datamodel = SQLAInterface(Lga)
    allow_browser_login = True
 
appbuilder.add_api(LgaApi)



class AgentApi(ModelRestApi):
    resource = "agent"
    datamodel = SQLAInterface(Agent)
    allow_browser_login = True
 
appbuilder.add_api(AgentApi)



class PosApi(ModelRestApi):
    resource = "pos"
    datamodel = SQLAInterface(Pos)
    allow_browser_login = True
 
appbuilder.add_api(PosApi)



class AgentPosLinkApi(ModelRestApi):
    resource = "agent_pos_link"
    datamodel = SQLAInterface(AgentPosLink)
    allow_browser_login = True
 
appbuilder.add_api(AgentPosLinkApi)



class CommRefApi(ModelRestApi):
    resource = "comm_ref"
    datamodel = SQLAInterface(CommRef)
    allow_browser_login = True
 
appbuilder.add_api(CommRefApi)



class PersonApi(ModelRestApi):
    resource = "person"
    datamodel = SQLAInterface(Person)
    allow_browser_login = True
 
appbuilder.add_api(PersonApi)



class WalletApi(ModelRestApi):
    resource = "wallet"
    datamodel = SQLAInterface(Wallet)
    allow_browser_login = True
 
appbuilder.add_api(WalletApi)



class AgentPersonLinkApi(ModelRestApi):
    resource = "agent_person_link"
    datamodel = SQLAInterface(AgentPersonLink)
    allow_browser_login = True
 
appbuilder.add_api(AgentPersonLinkApi)



class ContactApi(ModelRestApi):
    resource = "contact"
    datamodel = SQLAInterface(Contact)
    allow_browser_login = True
 
appbuilder.add_api(ContactApi)



class DocApi(ModelRestApi):
    resource = "doc"
    datamodel = SQLAInterface(Doc)
    allow_browser_login = True
 
appbuilder.add_api(DocApi)



class PersonAdditionalDataApi(ModelRestApi):
    resource = "person_additional_data"
    datamodel = SQLAInterface(PersonAdditionalData)
    allow_browser_login = True
 
appbuilder.add_api(PersonAdditionalDataApi)



class PersonAdminDataApi(ModelRestApi):
    resource = "person_admin_data"
    datamodel = SQLAInterface(PersonAdminData)
    allow_browser_login = True
 
appbuilder.add_api(PersonAdminDataApi)



class TransApi(ModelRestApi):
    resource = "trans"
    datamodel = SQLAInterface(Trans)
    allow_browser_login = True
 
appbuilder.add_api(TransApi)



class AgentDocLinkApi(ModelRestApi):
    resource = "agent_doc_link"
    datamodel = SQLAInterface(AgentDocLink)
    allow_browser_login = True
 
appbuilder.add_api(AgentDocLinkApi)



class PersonDocLinkApi(ModelRestApi):
    resource = "person_doc_link"
    datamodel = SQLAInterface(PersonDocLink)
    allow_browser_login = True
 
appbuilder.add_api(PersonDocLinkApi)

