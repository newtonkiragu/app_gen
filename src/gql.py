
# coding: utf-8
# AUTOGENERATED BY appgen 
# Copyright (C) Nyimbi Odero, 2024 


 
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphene import relay
from flask_graphql import GraphQLView

from flask_appbuilder.security.sqla.models import User, Role, Permission, PermissionView, RegisterUser
from .models import *
from . import app

t_doc_category_gql = graphene.Enum.from_enum(t_doc_category)
t_verification_status_gql = graphene.Enum.from_enum(t_verification_status)
t_org_type_gql = graphene.Enum.from_enum(t_org_type)
t_agent_role_gql = graphene.Enum.from_enum(t_agent_role)
t_verification_status_gql = graphene.Enum.from_enum(t_verification_status)
t_org_type_gql = graphene.Enum.from_enum(t_org_type)
t_person_role_gql = graphene.Enum.from_enum(t_person_role)
t_gender_gql = graphene.Enum.from_enum(t_gender)
t_gender_gql = graphene.Enum.from_enum(t_gender)
t_payment_method_gql = graphene.Enum.from_enum(t_payment_method)
t_card_trans_type_gql = graphene.Enum.from_enum(t_card_trans_type)
t_transaction_status_gql = graphene.Enum.from_enum(t_transaction_status)
t_payment_method_gql = graphene.Enum.from_enum(t_payment_method)
t_payment_method_gql = graphene.Enum.from_enum(t_payment_method)
t_verification_status_gql = graphene.Enum.from_enum(t_verification_status)
t_verification_status_gql = graphene.Enum.from_enum(t_verification_status)

class AgentTierGql(SQLAlchemyObjectType):
    class Meta:
        model = AgentTier
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class BankGql(SQLAlchemyObjectType):
    class Meta:
        model = Bank
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class BillerCategoryGql(SQLAlchemyObjectType):
    class Meta:
        model = BillerCategory
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class ContactTypeGql(SQLAlchemyObjectType):
    class Meta:
        model = ContactType
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class CountryGql(SQLAlchemyObjectType):
    class Meta:
        model = Country
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class CouponGql(SQLAlchemyObjectType):
    class Meta:
        model = Coupon
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class CurrencyGql(SQLAlchemyObjectType):
    class Meta:
        model = Currency
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class CustomerSegmentGql(SQLAlchemyObjectType):
    class Meta:
        model = CustomerSegment
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class DocTypeGql(SQLAlchemyObjectType):
    class Meta:
        model = DocType
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        

    doc_category = graphene.Field(t_doc_category_gql)

class MimeTypeGql(SQLAlchemyObjectType):
    class Meta:
        model = MimeType
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class MimeTypeMapGql(SQLAlchemyObjectType):
    class Meta:
        model = MimeTypeMap
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class PaymentCardGql(SQLAlchemyObjectType):
    class Meta:
        model = PaymentCard
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class PromotionGql(SQLAlchemyObjectType):
    class Meta:
        model = Promotion
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class TechparamsGql(SQLAlchemyObjectType):
    class Meta:
        model = Techparams
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class TokenProviderGql(SQLAlchemyObjectType):
    class Meta:
        model = TokenProvider
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class TransRoutingThresholdsGql(SQLAlchemyObjectType):
    class Meta:
        model = TransRoutingThresholds
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class TransTypeGql(SQLAlchemyObjectType):
    class Meta:
        model = TransType
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class UserExtGql(SQLAlchemyObjectType):
    class Meta:
        model = UserExt
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class BillerGql(SQLAlchemyObjectType):
    class Meta:
        model = Biller
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class StateGql(SQLAlchemyObjectType):
    class Meta:
        model = State
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class TokenGql(SQLAlchemyObjectType):
    class Meta:
        model = Token
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class BillerOfferingGql(SQLAlchemyObjectType):
    class Meta:
        model = BillerOffering
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class LgaGql(SQLAlchemyObjectType):
    class Meta:
        model = Lga
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class AgentGql(SQLAlchemyObjectType):
    class Meta:
        model = Agent
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        

    verification_status = graphene.Field(t_verification_status_gql)
    agent_type = graphene.Field(t_org_type_gql)
    agent_role = graphene.Field(t_agent_role_gql)
    kyc_verification_status = graphene.Field(t_verification_status_gql)

class PosGql(SQLAlchemyObjectType):
    class Meta:
        model = Pos
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class AgentPosLinkGql(SQLAlchemyObjectType):
    class Meta:
        model = AgentPosLink
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class CommRefGql(SQLAlchemyObjectType):
    class Meta:
        model = CommRef
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        

    agent_type = graphene.Field(t_org_type_gql)

class PersonGql(SQLAlchemyObjectType):
    class Meta:
        model = Person
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        

    person_role = graphene.Field(t_person_role_gql)
    gender = graphene.Field(t_gender_gql)

class WalletGql(SQLAlchemyObjectType):
    class Meta:
        model = Wallet
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class AgentPersonLinkGql(SQLAlchemyObjectType):
    class Meta:
        model = AgentPersonLink
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class ContactGql(SQLAlchemyObjectType):
    class Meta:
        model = Contact
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class DocGql(SQLAlchemyObjectType):
    class Meta:
        model = Doc
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class PersonAdditionalDataGql(SQLAlchemyObjectType):
    class Meta:
        model = PersonAdditionalData
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        

    gender = graphene.Field(t_gender_gql)

class PersonAdminDataGql(SQLAlchemyObjectType):
    class Meta:
        model = PersonAdminData
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        


class TransGql(SQLAlchemyObjectType):
    class Meta:
        model = Trans
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        

    transaction_type = graphene.Field(t_payment_method_gql)
    card_trans_type = graphene.Field(t_card_trans_type_gql)
    trans_status = graphene.Field(t_transaction_status_gql)
    origin_source = graphene.Field(t_payment_method_gql)
    trans_dest = graphene.Field(t_payment_method_gql)

class AgentDocLinkGql(SQLAlchemyObjectType):
    class Meta:
        model = AgentDocLink
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        

    verification_status = graphene.Field(t_verification_status_gql)

class PersonDocLinkGql(SQLAlchemyObjectType):
    class Meta:
        model = PersonDocLink
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        

    verification_status = graphene.Field(t_verification_status_gql)

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple AgentTiercolumns, by default over the primary key
    all_agent_tier = SQLAlchemyConnectionField(AgentTierGql.connection) #sort=AgentTierGql.sort_argument())
    # Allows sorting over multiple Bankcolumns, by default over the primary key
    all_bank = SQLAlchemyConnectionField(BankGql.connection) #sort=BankGql.sort_argument())
    # Allows sorting over multiple BillerCategorycolumns, by default over the primary key
    all_biller_category = SQLAlchemyConnectionField(BillerCategoryGql.connection) #sort=BillerCategoryGql.sort_argument())
    # Allows sorting over multiple ContactTypecolumns, by default over the primary key
    all_contact_type = SQLAlchemyConnectionField(ContactTypeGql.connection) #sort=ContactTypeGql.sort_argument())
    # Allows sorting over multiple Countrycolumns, by default over the primary key
    all_country = SQLAlchemyConnectionField(CountryGql.connection) #sort=CountryGql.sort_argument())
    # Allows sorting over multiple Couponcolumns, by default over the primary key
    all_coupon = SQLAlchemyConnectionField(CouponGql.connection) #sort=CouponGql.sort_argument())
    # Allows sorting over multiple Currencycolumns, by default over the primary key
    all_currency = SQLAlchemyConnectionField(CurrencyGql.connection) #sort=CurrencyGql.sort_argument())
    # Allows sorting over multiple CustomerSegmentcolumns, by default over the primary key
    all_customer_segment = SQLAlchemyConnectionField(CustomerSegmentGql.connection) #sort=CustomerSegmentGql.sort_argument())
    # Allows sorting over multiple DocTypecolumns, by default over the primary key
    all_doc_type = SQLAlchemyConnectionField(DocTypeGql.connection) #sort=DocTypeGql.sort_argument())
    # Allows sorting over multiple MimeTypecolumns, by default over the primary key
    all_mime_type = SQLAlchemyConnectionField(MimeTypeGql.connection) #sort=MimeTypeGql.sort_argument())
    # Allows sorting over multiple MimeTypeMapcolumns, by default over the primary key
    all_mime_type_map = SQLAlchemyConnectionField(MimeTypeMapGql.connection) #sort=MimeTypeMapGql.sort_argument())
    # Allows sorting over multiple PaymentCardcolumns, by default over the primary key
    all_payment_card = SQLAlchemyConnectionField(PaymentCardGql.connection) #sort=PaymentCardGql.sort_argument())
    # Allows sorting over multiple Promotioncolumns, by default over the primary key
    all_promotion = SQLAlchemyConnectionField(PromotionGql.connection) #sort=PromotionGql.sort_argument())
    # Allows sorting over multiple Techparamscolumns, by default over the primary key
    all_techparams = SQLAlchemyConnectionField(TechparamsGql.connection) #sort=TechparamsGql.sort_argument())
    # Allows sorting over multiple TokenProvidercolumns, by default over the primary key
    all_token_provider = SQLAlchemyConnectionField(TokenProviderGql.connection) #sort=TokenProviderGql.sort_argument())
    # Allows sorting over multiple TransRoutingThresholdscolumns, by default over the primary key
    all_trans_routing_thresholds = SQLAlchemyConnectionField(TransRoutingThresholdsGql.connection) #sort=TransRoutingThresholdsGql.sort_argument())
    # Allows sorting over multiple TransTypecolumns, by default over the primary key
    all_trans_type = SQLAlchemyConnectionField(TransTypeGql.connection) #sort=TransTypeGql.sort_argument())
    # Allows sorting over multiple UserExtcolumns, by default over the primary key
    all_user_ext = SQLAlchemyConnectionField(UserExtGql.connection) #sort=UserExtGql.sort_argument())
    # Allows sorting over multiple Billercolumns, by default over the primary key
    all_biller = SQLAlchemyConnectionField(BillerGql.connection) #sort=BillerGql.sort_argument())
    # Allows sorting over multiple Statecolumns, by default over the primary key
    all_state = SQLAlchemyConnectionField(StateGql.connection) #sort=StateGql.sort_argument())
    # Allows sorting over multiple Tokencolumns, by default over the primary key
    all_token = SQLAlchemyConnectionField(TokenGql.connection) #sort=TokenGql.sort_argument())
    # Allows sorting over multiple BillerOfferingcolumns, by default over the primary key
    all_biller_offering = SQLAlchemyConnectionField(BillerOfferingGql.connection) #sort=BillerOfferingGql.sort_argument())
    # Allows sorting over multiple Lgacolumns, by default over the primary key
    all_lga = SQLAlchemyConnectionField(LgaGql.connection) #sort=LgaGql.sort_argument())
    # Allows sorting over multiple Agentcolumns, by default over the primary key
    all_agent = SQLAlchemyConnectionField(AgentGql.connection) #sort=AgentGql.sort_argument())
    # Allows sorting over multiple Poscolumns, by default over the primary key
    all_pos = SQLAlchemyConnectionField(PosGql.connection) #sort=PosGql.sort_argument())
    # Allows sorting over multiple AgentPosLinkcolumns, by default over the primary key
    all_agent_pos_link = SQLAlchemyConnectionField(AgentPosLinkGql.connection) #sort=AgentPosLinkGql.sort_argument())
    # Allows sorting over multiple CommRefcolumns, by default over the primary key
    all_comm_ref = SQLAlchemyConnectionField(CommRefGql.connection) #sort=CommRefGql.sort_argument())
    # Allows sorting over multiple Personcolumns, by default over the primary key
    all_person = SQLAlchemyConnectionField(PersonGql.connection) #sort=PersonGql.sort_argument())
    # Allows sorting over multiple Walletcolumns, by default over the primary key
    all_wallet = SQLAlchemyConnectionField(WalletGql.connection) #sort=WalletGql.sort_argument())
    # Allows sorting over multiple AgentPersonLinkcolumns, by default over the primary key
    all_agent_person_link = SQLAlchemyConnectionField(AgentPersonLinkGql.connection) #sort=AgentPersonLinkGql.sort_argument())
    # Allows sorting over multiple Contactcolumns, by default over the primary key
    all_contact = SQLAlchemyConnectionField(ContactGql.connection) #sort=ContactGql.sort_argument())
    # Allows sorting over multiple Doccolumns, by default over the primary key
    all_doc = SQLAlchemyConnectionField(DocGql.connection) #sort=DocGql.sort_argument())
    # Allows sorting over multiple PersonAdditionalDatacolumns, by default over the primary key
    all_person_additional_data = SQLAlchemyConnectionField(PersonAdditionalDataGql.connection) #sort=PersonAdditionalDataGql.sort_argument())
    # Allows sorting over multiple PersonAdminDatacolumns, by default over the primary key
    all_person_admin_data = SQLAlchemyConnectionField(PersonAdminDataGql.connection) #sort=PersonAdminDataGql.sort_argument())
    # Allows sorting over multiple Transcolumns, by default over the primary key
    all_trans = SQLAlchemyConnectionField(TransGql.connection) #sort=TransGql.sort_argument())
    # Allows sorting over multiple AgentDocLinkcolumns, by default over the primary key
    all_agent_doc_link = SQLAlchemyConnectionField(AgentDocLinkGql.connection) #sort=AgentDocLinkGql.sort_argument())
    # Allows sorting over multiple PersonDocLinkcolumns, by default over the primary key
    all_person_doc_link = SQLAlchemyConnectionField(PersonDocLinkGql.connection) #sort=PersonDocLinkGql.sort_argument())

schema = graphene.Schema(query=Query)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
))
