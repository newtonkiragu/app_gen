
import os
import sys
import enum
import inspect
import datetime
import shutils
from datetime import timedelta, datetime, date

from sqlalchemy.orm import relationship, query, defer, deferred, column_property, mapper
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy import (Column, Integer, String, ForeignKey,
    Sequence, Float, Text, BigInteger, Date, SmallInteger, BigInteger, 
    DateTime, Time, Boolean, Index, CheckConstraint, Interval, # MatchType  
    UniqueConstraint, ForeignKeyConstraint, Numeric, LargeBinary , Table, func, Enum,
    text)

# IMPORT Postgresql Specific Types
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.dialects.postgresql import (
    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE,
    DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER,
    INTERVAL, JSON, JSONB, MACADDR, NUMERIC, OID, REAL, SMALLINT, TEXT,
    TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE,
    DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR, aggregate_order_by )

from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn, UserExtensionMixin
from flask_appbuilder.filemanager import ImageManager

from flask_appbuilder.models.decorators import renders
from sqlalchemy_utils import aggregated, force_auto_coercion, observes
from sqlalchemy_utils.types import TSVectorType   #Searchability look at DocMixin
from sqlalchemy.ext.associationproxy import association_proxy

from flask_appbuilder.security.sqla.models import User
from geoalchemy2 import Geometry

# To create GraphSQL API
# import graphene
# from graphene_sqlalchemy import SQLAlchemyObjectType

# Versioning Mixin
# from sqlalchemy_continuum import make_versioned
#Add __versioned__ = {}


# from sqlalchemy_searchable import make_searchable
# from flask_graphql import GraphQLView

# ActiveRecord Model Features
# from sqlalchemy_mixins import AllFeaturesMixin, ActiveRecordMixin


# from .model_mixins import *

# Here is how to extend the User model
#class UserExtended(Model, UserExtensionMixin):
#    contact_group_id = Column(Integer, ForeignKey('contact_group.id'), nullable=True)
#    contact_group = relationship('ContactGroup')

# UTILITY CLASSES
# import arrow,


# Initialize sqlalchemy_utils
#force_auto_coercion()
# Keep versions of all data
# make_versioned()
# make_searchable()



class Doc_category(enum.Enum):
   IDENTIFICATION = 'Identification'
   CERTIFICATION = 'Certification'
   FINANCIAL = 'Financial'
   EDUCATIONAL = 'Educational'
   LEGAL_DOCUMENT = 'Legal_Document'
   UTILITY_BILL = 'Utility_Bill'
   MEDICAL_REPORT = 'Medical_Report'
   CONTRACT = 'Contract'
   INSURANCE_POLICY = 'Insurance_Policy'
   TAX_DOCUMENT = 'Tax_Document'



class Registration_status(enum.Enum):
   PENDING = 'pending'
   KYC_SUBMITTED = 'kyc_submitted'
   KYC_APPROVED = 'kyc_approved'
   KYC_REJECTED = 'kyc_rejected'
   ESCALATED = 'escalated'
   CONTRACTED = 'contracted'
   ACTIVE = 'active'
   SUSPENDED = 'suspended'
   INACTIVE = 'inactive'
   CONTRACT_TERMINATED = 'contract_terminated'
   DOCS_EXPIRED = 'docs_expired'
   UNDER_REVIEW = 'under_review'
   LOCKED = 'locked'
   AWAITING_RENEWAL = 'awaiting_renewal'
   RENEWAL_REJECTED = 'renewal_rejected'
   VERIFICATION_FAILED = 'verification_failed'



class Agent_type(enum.Enum):
   INDIVIDUAL = 'Individual'
   BUSINESS_NAME = 'Business_Name'
   SOLE_PROPRIETORSHIP = 'Sole_Proprietorship'
   PRIVATE_LIMITED_COMPANY = 'Private_Limited_Company'
   PUBLIC_LIMITED_COMPANY = 'Public_Limited_Company'
   PUBLIC_COMPANY_LIMITED_BY_GUARANTEE = 'Public_Company_Limited_by_Guarantee'
   PRIVATE_UNLIMITED_COMPANY = 'Private_Unlimited_Company'
   PUBLIC_UNLIMITED_COMPANY = 'Public_Unlimited_Company'



class Agent_role(enum.Enum):
   AGENT = 'agent'
   SUB_AGENT = 'sub_agent'
   SUPER_AGENT = 'super_agent'
   AGGREGATOR = 'aggregator'



class Kyc_verification_status(enum.Enum):
   PENDING = 'pending'
   KYC_SUBMITTED = 'kyc_submitted'
   KYC_APPROVED = 'kyc_approved'
   KYC_REJECTED = 'kyc_rejected'
   ESCALATED = 'escalated'
   CONTRACTED = 'contracted'
   ACTIVE = 'active'
   SUSPENDED = 'suspended'
   INACTIVE = 'inactive'
   CONTRACT_TERMINATED = 'contract_terminated'
   DOCS_EXPIRED = 'docs_expired'
   UNDER_REVIEW = 'under_review'
   LOCKED = 'locked'
   AWAITING_RENEWAL = 'awaiting_renewal'
   RENEWAL_REJECTED = 'renewal_rejected'
   VERIFICATION_FAILED = 'verification_failed'






class Person_role(enum.Enum):
   NEXT_OF_KIN = 'next_of_kin'
   COMPANY_DIRECTOR = 'company_director'
   POS_OPERATOR = 'pos_operator'
   FIELD_SUPPORT = 'field_support'
   CUSTOMER = 'customer'
   REFEREE = 'referee'
   SUPERVISOR = 'supervisor'



class Gender(enum.Enum):
   MALE = 'Male'
   FEMALE = 'Female'
   NON_BINARY = 'Non_Binary'
   PREFER_NOT_TO_SAY = 'Prefer_Not_to_Say'
   OTHER = 'Other'






class Transaction_type(enum.Enum):
   CASH = 'cash'
   CREDIT_CARD = 'credit_card'
   DEBIT_CARD = 'debit_card'
   PREPAID_CARD = 'prepaid_card'
   COMMERCIAL_CARD = 'commercial_card'
   DEBT = 'debt'
   BANK = 'bank'
   MOBILE = 'mobile'
   COUPON = 'coupon'
   ORDER = 'order'
   WITHDRAWAL = 'withdrawal'
   FUND_WALLET = 'fund_wallet'
   CHEQUE = 'cheque'
   BANK_TRANSFER = 'bank_transfer'
   CRYPTO = 'crypto'
   BARTER = 'barter'
   WIRE_TRANSFER = 'wire_transfer'
   CONTACTLESS = 'contactless'
   GIFT_CARD = 'gift_card'
   LOYALTY_POINTS = 'loyalty_points'
   MONEY_ORDER = 'money_order'
   ESCROW = 'escrow'
   INSTALLMENT = 'installment'
   INVOICE = 'invoice'
   PREPAID = 'prepaid'
   QR_CODE = 'qr_code'
   DIGITAL_WALLET = 'digital_wallet'
   AUTOMATIC_DEBIT = 'automatic_debit'
   CASH_ON_DELIVERY = 'cash_on_delivery'
   POSTPAID = 'postpaid'
   THIRD_PARTY = 'third_party'
   TRADE_CREDIT = 'trade_credit'



class Card_trans_type(enum.Enum):
   PURCHASE = 'purchase'
   BALANCE = 'balance'
   REFUND = 'refund'
   CASH_ADVANCE = 'cash_advance'
   CASH_BACK = 'cash_back'
   PRE_AUTHORIZATION = 'pre_authorization'
   PRE_AUTHORIZATION_COMPLETION = 'pre_authorization_completion'
   CARD_VERIFICATION = 'card_verification'
   TRANSACTION = 'transaction'
   SETTLEMENT = 'settlement'



class Trans_status(enum.Enum):
   PENDING = 'pending'
   AUTHORIZED = 'authorized'
   COMPLETED = 'completed'
   FAILED = 'failed'
   CANCELLED = 'cancelled'
   REFUNDED = 'refunded'
   REVERSED = 'reversed'
   HOLD = 'hold'
   SUSPENDED = 'suspended'
   DISPUTED = 'disputed'
   DELIVERED = 'delivered'
   SETTLEMENT_PENDING = 'settlement_pending'
   SETTLED = 'settled'
   REJECTED = 'rejected'
   EXPIRED = 'expired'
   PENDING_VERIFICATION = 'pending_verification'
   HOLD_FOR_REVIEW = 'hold_for_review'
   PARTIALLY_COMPLETED = 'partially_completed'
   PARTIALLY_REFUNDED = 'partially_refunded'
   PARTIALLY_REVERSED = 'partially_reversed'
   COMPLETED_WITH_ERRORS = 'completed_with_errors'
   BATCH_PROCESSING = 'batch_processing'
   DEFERRED = 'deferred'
   WAITING_FOR_AUTHORIZATION = 'waiting_for_authorization'
   PROCESSING = 'processing'
   PENDING_FUNDS_AVAILABILITY = 'pending_funds_availability'
   PENDING_REVIEW = 'pending_review'
   PENDING_CONFIRMATION = 'pending_confirmation'
   WAITING_FOR_SETTLEMENT = 'waiting_for_settlement'
   PENDING_RECONCILIATION = 'pending_reconciliation'
   PENDING_DISBURSEMENT = 'pending_disbursement'
   CHARGEBACK_INITIATED = 'chargeback_initiated'
   CHARGEBACK_RESOLVED = 'chargeback_resolved'
   PENDING_CAPTURE = 'pending_capture'
   CAPTURED = 'captured'
   VOIDED = 'voided'
   IN_QUEUE = 'in_queue'
   MANUAL_INTERVENTION_REQUIRED = 'manual_intervention_required'
   GATEWAY_TIMEOUT = 'gateway_timeout'
   FRAUD_ALERT = 'fraud_alert'
   UNDER_AUDIT = 'under_audit'
   AUDIT_COMPLETED = 'audit_completed'
   CURRENCY_CONVERSION = 'currency_conversion'
   CURRENCY_CONVERSION_COMPLETED = 'currency_conversion_completed'
   ESCALATED = 'escalated'
   DE_ESCALATED = 'de_escalated'
   PENDING_APPROVAL = 'pending_approval'
   APPROVED = 'approved'
   DECLINED = 'declined'
   RE_ATTEMPTED = 're_attempted'
   RE_SCHEDULED = 're_scheduled'
   INSUFFICIENT_FUNDS = 'insufficient_funds'
   VERIFICATION_FAILED = 'verification_failed'
   VERIFICATION_SUCCESSFUL = 'verification_successful'
   PENDING_CLEARANCE = 'pending_clearance'
   CLEARED = 'cleared'
   RE_INITIATED = 're_initiated'
   SPLIT_TRANSACTION = 'split_transaction'
   CONSOLIDATED = 'consolidated'



class Origin_source(enum.Enum):
   CASH = 'cash'
   CREDIT_CARD = 'credit_card'
   DEBIT_CARD = 'debit_card'
   PREPAID_CARD = 'prepaid_card'
   COMMERCIAL_CARD = 'commercial_card'
   DEBT = 'debt'
   BANK = 'bank'
   MOBILE = 'mobile'
   COUPON = 'coupon'
   ORDER = 'order'
   WITHDRAWAL = 'withdrawal'
   FUND_WALLET = 'fund_wallet'
   CHEQUE = 'cheque'
   BANK_TRANSFER = 'bank_transfer'
   CRYPTO = 'crypto'
   BARTER = 'barter'
   WIRE_TRANSFER = 'wire_transfer'
   CONTACTLESS = 'contactless'
   GIFT_CARD = 'gift_card'
   LOYALTY_POINTS = 'loyalty_points'
   MONEY_ORDER = 'money_order'
   ESCROW = 'escrow'
   INSTALLMENT = 'installment'
   INVOICE = 'invoice'
   PREPAID = 'prepaid'
   QR_CODE = 'qr_code'
   DIGITAL_WALLET = 'digital_wallet'
   AUTOMATIC_DEBIT = 'automatic_debit'
   CASH_ON_DELIVERY = 'cash_on_delivery'
   POSTPAID = 'postpaid'
   THIRD_PARTY = 'third_party'
   TRADE_CREDIT = 'trade_credit'



class Trans_dest(enum.Enum):
   CASH = 'cash'
   CREDIT_CARD = 'credit_card'
   DEBIT_CARD = 'debit_card'
   PREPAID_CARD = 'prepaid_card'
   COMMERCIAL_CARD = 'commercial_card'
   DEBT = 'debt'
   BANK = 'bank'
   MOBILE = 'mobile'
   COUPON = 'coupon'
   ORDER = 'order'
   WITHDRAWAL = 'withdrawal'
   FUND_WALLET = 'fund_wallet'
   CHEQUE = 'cheque'
   BANK_TRANSFER = 'bank_transfer'
   CRYPTO = 'crypto'
   BARTER = 'barter'
   WIRE_TRANSFER = 'wire_transfer'
   CONTACTLESS = 'contactless'
   GIFT_CARD = 'gift_card'
   LOYALTY_POINTS = 'loyalty_points'
   MONEY_ORDER = 'money_order'
   ESCROW = 'escrow'
   INSTALLMENT = 'installment'
   INVOICE = 'invoice'
   PREPAID = 'prepaid'
   QR_CODE = 'qr_code'
   DIGITAL_WALLET = 'digital_wallet'
   AUTOMATIC_DEBIT = 'automatic_debit'
   CASH_ON_DELIVERY = 'cash_on_delivery'
   POSTPAID = 'postpaid'
   THIRD_PARTY = 'third_party'
   TRADE_CREDIT = 'trade_credit'



class Verification_status(enum.Enum):
   PENDING = 'pending'
   KYC_SUBMITTED = 'kyc_submitted'
   KYC_APPROVED = 'kyc_approved'
   KYC_REJECTED = 'kyc_rejected'
   ESCALATED = 'escalated'
   CONTRACTED = 'contracted'
   ACTIVE = 'active'
   SUSPENDED = 'suspended'
   INACTIVE = 'inactive'
   CONTRACT_TERMINATED = 'contract_terminated'
   DOCS_EXPIRED = 'docs_expired'
   UNDER_REVIEW = 'under_review'
   LOCKED = 'locked'
   AWAITING_RENEWAL = 'awaiting_renewal'
   RENEWAL_REJECTED = 'renewal_rejected'
   VERIFICATION_FAILED = 'verification_failed'






class AgentTier(Model):
    __tablename__ = "agent_tier"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    notes = Column(Text, nullable=True)

    def __repr__(self):

       return self.name

 ### 


class Bank(Model):
    __tablename__ = "bank"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String
		, comment="NIBSS institutionCode")
    name = Column(String)
    category = Column(Integer, nullable=True
		, comment="category")
    swift_code = Column(String, nullable=True)
    sort_code = Column(String, nullable=True)
    iban = Column(String, nullable=True)
    cust_care_phone = Column(String, nullable=True)
    cust_care_email = Column(String, nullable=True)
    escalation_contact = Column(Text, nullable=True)
    created_on = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    updated_on = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)

    def __repr__(self):

       return self.name

 ### 


class BillerCategory(Model):
    __tablename__ = "biller_category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    notes = Column(Text, nullable=True)

    def __repr__(self):

       return self.name

 ### 


class ContactType(Model):
    __tablename__ = "contact_type"
    __doc__ = " phone, mobile, email, messaging, whatsapp, viber, instagram, website, etc"
    id = Column(Integer, primary_key=True, autoincrement=True
		, comment="Unique identifier for the address type.")
    name = Column(String
		, comment="Name or type of contact method, e.g., Mobile, Email, WhatsApp.")
    description = Column(Text, nullable=True
		, comment="Brief description about the address type, providing context or usage scenarios.")
    is_digital = Column(Boolean, default=True, nullable=True
		, comment="Indicates if the contact method is digital or physical.")
    requires_verification = Column(Boolean, default=False, nullable=True
		, comment="Indicates if the address type typically requires a verification process, e.g., email confirmation.")
    max_length = Column(Integer, nullable=True
		, comment="If applicable, the maximum character length of a value of this address type. Useful for validation.")
    icon_url = Column(String, nullable=True
		, comment="URL or link to an icon or image representing this address type. Useful for UI/UX purposes.")
    created_at = Column(DateTime, server_default=text('NOW()'), nullable=True
		, comment="Timestamp when the address type was added to the system.")
    updated_at = Column(DateTime, server_default=text('NOW()'), nullable=True
		, comment="Timestamp when the address type was last updated.")

    def __repr__(self):

       return self.name

 ### 


class Country(Model):
    __tablename__ = "country"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    code = Column(String, nullable=True)
    phone_code = Column(Integer, nullable=True)

    def __repr__(self):

       return self.name

 ### 


class Coupon(Model):
    __tablename__ = "coupon"
    __doc__ = " A coupon can be shared electronically and redeemed at any agent"
    coupon_id = Column(Integer, primary_key=True, autoincrement=True)
    coupon_value = Column(Numeric, nullable=True)
    active = Column(Boolean, nullable=True)
    used = Column(Boolean, default=False, nullable=True)
    used_date = Column(DateTime, server_default=text('NOW()'), nullable=True)
    primary_scan_code_label = Column(String, nullable=True)
    is_return_coupon = Column(Boolean, nullable=True)
    expiration_date = Column(Date, nullable=True)
    generation_date = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    activation_date = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    secondary_scan_code_label = Column(String, nullable=True)
    scan_code_img = Column(String, nullable=True)
    coupon_code = Column(String, nullable=True)
    return_coupon_reason = Column(String, nullable=True)
    is_valid = Column(Boolean, default=True, nullable=True)
    coupon_status = Column(String, nullable=True)
    discount_percentage = Column(Integer, nullable=True)
    coupon_count = Column(Integer, nullable=True)
    payment_method_status = Column(String)

    def __repr__(self):

       return self.coupon_id

 ### 


class Currency(Model):
    __tablename__ = "currency"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    symbol = Column(String, nullable=True)
    numeric_code = Column(String, nullable=True)
    full_name = Column(String, nullable=True)
    decimal_places = Column(SmallInteger, nullable=True)
    internationalized_name_code = Column(String, nullable=True)

    def __repr__(self):

       return self.name

 ### 


class CustomerSegment(Model):
    __tablename__ = "customer_segment"
    cs_id = Column(Integer, primary_key=True, autoincrement=True)
    cs_name = Column(String, nullable=True)
    cs_notes = Column(Text, nullable=True)

    def __repr__(self):

       return self.cs_name

 ### 


class DocType(Model):
    __tablename__ = "doc_type"
    id = Column(Integer, primary_key=True, autoincrement=True
		, comment="Unique identifier for the document type.")
    name = Column(String, nullable=True
		, comment="Name or title of the document type e.g. Passport, Drivers License.")
    doc_category = Column(Enum(Doc_category), name='t_doc_category', nullable=False)
    notes = Column(Text, nullable=True
		, comment="Any additional remarks or details about the document type.")
    required_information = Column(Text, nullable=True
		, comment="List or description of required fields/information for this document type.")
    is_serialized = Column(Boolean, default=False, nullable=True)
    serial_length = Column(Integer, nullable=True)
    expires = Column(Boolean, default=False, nullable=True)
    validity_period = Column(Integer, nullable=True
		, comment="Standard validity duration of this type of document in days.")
    renewal_frequency = Column(Integer, nullable=True
		, comment="Frequency at which this document typically needs renewal, in days. Useful for setting reminders.")
    is_government_issued = Column(Boolean, default=False, nullable=True
		, comment="Indicates if this document is typically issued by a government authority.")
    is_digital = Column(Boolean, default=False, nullable=True
		, comment="Indicates if the document is typically in digital format.")
    template_url = Column(String, nullable=True
		, comment="URL or link to a template or sample of this document type, if available.")
    example_image_url = Column(String, nullable=True
		, comment="URL or link to an example image of this document type.")
    created_at = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True
		, comment="Timestamp when the document type was added to the system.")
    updated_at = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True
		, comment="Timestamp when the document type was last updated.")

    def __repr__(self):

       return self.name

 ### 


class MimeType(Model):
    __tablename__ = "mime_type"
    __doc__ = "Standard MIME types recognized by the content management system."
    id = Column(Integer, primary_key=True, autoincrement=True)
    label = Column(String, nullable=True)
    mime_type = Column(String, nullable=True)
    file_extension = Column(String, nullable=True)

    def __repr__(self):

       return self.label

 ### 


class MimeTypeMap(Model):
    __tablename__ = "mime_type_map"
    __doc__ = "Maps extesions to mime types"
    id = Column(Integer, primary_key=True, autoincrement=True)
    extension = Column(String, nullable=True)
    mime_type = Column(String, nullable=True)

    def __repr__(self):

       return self.id

 ### 


class PaymentCard(Model):
    __tablename__ = "payment_card"
    __doc__ = "We want to store as little data as possible about peoples cards"
    id = Column(Integer, primary_key=True, autoincrement=True)
    bin = Column(String, nullable=True)
    pan = Column(String, nullable=True)
    credit_card_expired = Column(Boolean, default=False)
    card_token = Column(String)
    issue_number = Column(String)
    bill_to_city = Column(String, nullable=True)
    masked_number = Column(String)
    name = Column(String)
    company_name = Column(String, nullable=True)
    card_holder_name = Column(String)
    number_last_digits = Column(String)
    payment_card_type = Column(String)
    derived_card_type_code = Column(String, nullable=True)
    expiration_year = Column(Integer, nullable=True)
    expiration_month = Column(Integer, nullable=True)
    bill_to_street = Column(String, nullable=True)
    bill_to_street2 = Column(String, nullable=True)
    bill_to_first_name = Column(String, nullable=True)
    bill_to_last_name = Column(String, nullable=True)
    payment_method_status = Column(String, nullable=True)
    card_number = Column(String, nullable=True
		, comment="Mask this number")
    cardholder_name = Column(String, nullable=True)
    card_expiration = Column(String, nullable=True)
    service_code = Column(String, nullable=True)
    cvv = Column(String, nullable=True
		, comment="mask or hash the cvv")

    def __repr__(self):

       return self.name

 ### 


class Promotion(Model):
    __tablename__ = "promotion"
    promo_id = Column(Integer, primary_key=True, autoincrement=True)
    promo_name = Column(String, nullable=True)
    promo_notes = Column(Text, nullable=True)
    promo_start_date = Column(DateTime, server_default=text('NOW()'), nullable=True)
    promo_end_date = Column(DateTime, server_default=text('NOW()'), nullable=True)

    def __repr__(self):

       return self.promo_name

 ### 


class Techparams(Model):
    __tablename__ = "techparams"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tp_key = Column(String, nullable=True)
    tp_value = Column(Text, nullable=True)
    enabled = Column(Boolean, default=True, nullable=True)
    notes = Column(Text, nullable=True)

    def __repr__(self):

       return self.id

 ### 


class TokenProvider(Model):
    __tablename__ = "token_provider"
    token_provider_id = Column(Integer, primary_key=True, autoincrement=True)
    token_provider_name = Column(String)
    token_provioder_notes = Column(Text, nullable=True)
    token_provider_priv_key = Column(Text, nullable=True)
    token_provider_pub_key = Column(Text, nullable=True)
    token_provider_endpoint = Column(Text, nullable=True)
    token_provider_protocol = Column(Text, nullable=True)
    token_provider_auth = Column(Text, nullable=True)
    token_provider_ssl = Column(Text, nullable=True)
    token_provider_ip_whitelist = Column(Text, nullable=True)
    token_provider_password = Column(String, nullable=True)
    enabled = Column(Boolean, default=False, nullable=True)

    def __repr__(self):

       return self.token_provider_name

 ### 


class TransRoutingThresholds(Model):
    __tablename__ = "trans_routing_thresholds"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    min_amount = Column(Numeric, nullable=True)
    max_amount = Column(Numeric, nullable=True)
    priority = Column(Integer, nullable=True)

    def __repr__(self):

       return self.name

 ### 


class TransType(Model):
    __tablename__ = "trans_type"
    tt_id = Column(Integer, primary_key=True, autoincrement=True)
    tt_name = Column(String, nullable=True
		, comment="Deposit, Withdrawal, Transfer, Bill Payment, etc")
    tt_notes = Column(Text, nullable=True)

    def __repr__(self):

       return self.tt_name

 ### 


class UserExt(Model):
    __tablename__ = "user_ext"
    id = Column(Integer, primary_key=True, autoincrement=True)
    manager_id_fk = Column(Integer, ForeignKey('user_ext.id'), nullable=True)
    first_name = Column(String, nullable=True)
    middle_name = Column(String, nullable=True)
    surname = Column(String, nullable=True)
    employee_number = Column(String, nullable=True)
    job_title = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    email = Column(String, nullable=True)
    user_data = Column(Text, nullable=True)
    user_ext_manager = relationship('UserExt', backref='user_exts_user_ext_manager', primaryjoin='UserExt.manager_id_fk == UserExt.id', remote_side=[id])

    def __repr__(self):

       return self.first_name

 ### 


class Biller(Model):
    __tablename__ = "biller"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cat_id_fk = Column(Integer, ForeignKey('biller_category.id'), nullable=True)
    code = Column(String)
    name = Column(String, nullable=True)
    url = Column(String, nullable=True)
    note = Column(Text, nullable=True)
    biller_cat = relationship(BillerCategory, backref='billers_biller_cat', primaryjoin='Biller.cat_id_fk == BillerCategory.id')

    def __repr__(self):

       return self.name

 ### 


class State(Model):
    __tablename__ = "state"
    country_id_fk = Column(Integer, ForeignKey('country.id'), nullable=True)
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, nullable=True)
    name = Column(String, nullable=True)
    desc = Column(Text, nullable=True)
    state_country = relationship(Country, backref='states_state_country', primaryjoin='State.country_id_fk == Country.id')

    def __repr__(self):

       return self.name

 ### 


class Token(Model):
    __tablename__ = "token"
    token_id = Column(Integer, primary_key=True, autoincrement=True)
    token_provider_id_fk = Column(Integer, ForeignKey('token_provider.token_provider_id'), nullable=True)
    token_name = Column(String, nullable=True)
    token_issue_date = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    token_expiry_date = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    token_validity = Column(Integer, nullable=True)
    token_expired = Column(Boolean, default=False, nullable=True)
    token_value = Column(String, nullable=True)
    token_username = Column(String, nullable=True)
    token_password = Column(String, nullable=True)
    token_notes = Column(Text, nullable=True)
    token_client_secret = Column(Text, nullable=True)
    enabled = Column(Boolean, default=False, nullable=True)
    token_token_provider = relationship(TokenProvider, backref='tokens_token_token_provider', primaryjoin='Token.token_provider_id_fk == TokenProvider.token_provider_id')

    def __repr__(self):

       return self.token_name

 ### 


class BillerOffering(Model):
    __tablename__ = "biller_offering"
    biller_id_fk = Column(Integer, ForeignKey('biller.id'), nullable=True)
    offering_id = Column(Integer, primary_key=True, autoincrement=True)
    offering_name = Column(String, nullable=True)
    offering_description = Column(Text, nullable=True)
    offering_price = Column(Numeric, nullable=True)
    biller_offering_biller = relationship(Biller, backref='biller_offerings_biller_offering_biller', primaryjoin='BillerOffering.biller_id_fk == Biller.id')

    def __repr__(self):

       return self.offering_name

 ### 


class Lga(Model):
    __tablename__ = "lga"
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_id_fk = Column(Integer, ForeignKey('state.id'), nullable=True)
    code = Column(String, nullable=True)
    lga_name = Column(String, nullable=True)
    lga_state = relationship(State, backref='lgas_lga_state', primaryjoin='Lga.state_id_fk == State.id')

    def __repr__(self):

       return self.code

 ### 


class Agent(Model):
    __tablename__ = "agent"
    id = Column(Integer, primary_key=True, autoincrement=True)
    aggregator_id_fk = Column(Integer, ForeignKey('agent.id'), nullable=True)
    is_aggregator = Column(Boolean, default=False, nullable=True)
    became_aggregator_date = Column(DateTime, server_default=text('NOW()'), nullable=True)
    assigned_pos_count = Column(Integer)
    aggregator_pos_threshold = Column(Integer, nullable=True)
    registration_status = Column(Enum(Registration_status), name='t_registration_status', nullable=False)
    registration_status_notes = Column(Text, nullable=True)
    agent_type = Column(Enum(Agent_type), name='t_agent_type', nullable=False)
    agent_role = Column(Enum(Agent_role), name='t_agent_role', nullable=False)
    agent_tier_id_fk = Column(Integer, ForeignKey('agent_tier.id'), nullable=True)
    account_manager_id_fk = Column(Integer, ForeignKey('user_ext.id'), nullable=True)
    agent_name = Column(String, nullable=True)
    alias = Column(String, nullable=True
		, comment="Use this for reports if available")
    phone_country_id_fk = Column(Integer, ForeignKey('country.id'), nullable=True)
    phone = Column(String)
    phone_ext = Column(String, nullable=True)
    alt_phone_country_id_fk = Column(Integer, ForeignKey('country.id'), nullable=True)
    alt_phone = Column(String, nullable=True)
    alt_phone_ext = Column(String, nullable=True)
    email = Column(String, nullable=True)
    alt_email = Column(String, nullable=True)
    bvn = Column(String, nullable=True)
    bvn_verified = Column(Boolean, default=False, nullable=True)
    bvn_verification_date = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    bvn_verification_code = Column(Text, nullable=True)
    tax_id = Column(String, nullable=True)
    bank_id_fk = Column(Integer, ForeignKey('bank.id'), nullable=True)
    bank_acc_no = Column(String, nullable=True
		, comment="Transactions to this bank are free?")
    biz_name = Column(String, nullable=True)
    biz_state_id_fk = Column(Integer, ForeignKey('state.id'), nullable=True)
    biz_lga_id_fk = Column(Integer, ForeignKey('lga.id'), nullable=True)
    biz_city = Column(String, nullable=True)
    biz_city_area = Column(String, nullable=True)
    biz_street = Column(String, nullable=True)
    biz_building = Column(String, nullable=True)
    biz_address = Column(Text, nullable=True)
    biz_poa_img = Column(String, nullable=True)
    biz_poa_desc = Column(String, nullable=True)
    biz_poa_valid = Column(Boolean, default=False, nullable=True)
    biz_lat = Column(Float, nullable=True)
    biz_lon = Column(Float, nullable=True)
    biz_loc = Column(Text, nullable=True)
    biz_ggl_code = Column(String, nullable=True)
    company_name = Column(String, nullable=True)
    cac_number = Column(String, nullable=True)
    cac_reg_date = Column(Date, nullable=True)
    cac_cert_img = Column(String, nullable=True)
    cac_cert_no = Column(String, nullable=True)
    ref_code = Column(String, nullable=True)
    access_pin = Column(String, nullable=True)
    registered_by_fk = Column(Integer, ForeignKey('user_ext.id'), nullable=True)
    registration_date = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    reviewed_by_fk = Column(Integer, ForeignKey('user_ext.id'), nullable=True)
    review_date = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    approved_by_fk = Column(Integer, ForeignKey('user_ext.id'), nullable=True)
    approval_date = Column(DateTime, server_default=text('NOW()'), nullable=True)
    approval_narrative = Column(Text, nullable=True)
    kyc_submit_date = Column(DateTime, server_default=text('NOW()'), nullable=True)
    kyc_verification_status = Column(Enum(Kyc_verification_status), name='t_kyc_verification_status', nullable=False)
    kyc_approval_date = Column(DateTime, server_default=text('NOW()'), nullable=True)
    kyc_ref_code = Column(String, nullable=True)
    kyc_rejection_narrative = Column(Text, nullable=True)
    kyc_rejection_by_fk = Column(Integer, ForeignKey('user_ext.id'), nullable=True)
    rejection_date = Column(DateTime, server_default=text('NOW()'), nullable=True)
    rejection_narrative = Column(Text, nullable=True)
    rejected_by_fk = Column(Integer, ForeignKey('user_ext.id'), nullable=True)
    face_matrix = Column(Text, nullable=True)
    finger_print_img = Column(Text, nullable=True)
    agent_public_key = Column(Text, nullable=True)
    agent_pj_expiry = Column(DateTime, server_default=text('NOW()'), nullable=True)
    agent_history = Column(Text, nullable=True)
    agent_account_manager = relationship(UserExt, backref='agents_agent_account_manager', primaryjoin='Agent.account_manager_id_fk == UserExt.id')
    agent_agent_tier = relationship(AgentTier, backref='agents_agent_agent_tier', primaryjoin='Agent.agent_tier_id_fk == AgentTier.id')
    agent_aggregator = relationship('Agent', backref='agents_agent_aggregator', primaryjoin='Agent.aggregator_id_fk == Agent.id', remote_side=[id])
    agent_alt_phone_country = relationship(Country, backref='agents_agent_alt_phone_country', primaryjoin='Agent.alt_phone_country_id_fk == Country.id')
    agent_approved_by_fk_fkey = relationship(UserExt, backref='agents_agent_approved_by_fk_fkey', primaryjoin='Agent.approved_by_fk == UserExt.id')
    agent_bank = relationship(Bank, backref='agents_agent_bank', primaryjoin='Agent.bank_id_fk == Bank.id')
    agent_biz_lga = relationship(Lga, backref='agents_agent_biz_lga', primaryjoin='Agent.biz_lga_id_fk == Lga.id')
    agent_biz_state = relationship(State, backref='agents_agent_biz_state', primaryjoin='Agent.biz_state_id_fk == State.id')
    agent_kyc_rejection_by_fk_fkey = relationship(UserExt, backref='agents_agent_kyc_rejection_by_fk_fkey', primaryjoin='Agent.kyc_rejection_by_fk == UserExt.id')
    agent_phone_country = relationship(Country, backref='agents_agent_phone_country', primaryjoin='Agent.phone_country_id_fk == Country.id')
    agent_registered_by_fk_fkey = relationship(UserExt, backref='agents_agent_registered_by_fk_fkey', primaryjoin='Agent.registered_by_fk == UserExt.id')
    agent_rejected_by_fk_fkey = relationship(UserExt, backref='agents_agent_rejected_by_fk_fkey', primaryjoin='Agent.rejected_by_fk == UserExt.id')
    agent_reviewed_by_fk_fkey = relationship(UserExt, backref='agents_agent_reviewed_by_fk_fkey', primaryjoin='Agent.reviewed_by_fk == UserExt.id')

    def __repr__(self):

       return self.alias

 ### 


class Pos(Model):
    __tablename__ = "pos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    serial_no = Column(String, nullable=True)
    imei = Column(String, nullable=True)
    mac_addr = Column(String, nullable=True)
    device_model = Column(String, nullable=True)
    device_make = Column(String, nullable=True)
    device_mfg = Column(String, nullable=True)
    os_version = Column(String, nullable=True)
    device_color = Column(String, nullable=True)
    device_condition = Column(String, nullable=True
		, comment="working, irreparrable, repaired")
    status = Column(String, nullable=True)
    owner_type = Column(String, nullable=True)
    registration_date = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    assigned = Column(Boolean, default=False, nullable=True)
    assigned_date = Column(DateTime, server_default=text('NOW()'), nullable=True)
    assigned_narrative = Column(Text, nullable=True)
    active = Column(Boolean, default=False, nullable=True)
    activation_date = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    last_active = Column(DateTime, server_default=text('NOW()'), nullable=True)
    deployed = Column(Boolean, default=False, nullable=True)
    deploy_date = Column(DateTime, server_default=text('NOW()'), nullable=True)
    deploy_narrative = Column(Text, nullable=True)
    returned = Column(Boolean, default=False, nullable=True)
    return_date = Column(DateTime, server_default=text('NOW()'), nullable=True)
    return_narrative = Column(Text, nullable=True)
    return_received_date = Column(DateTime, server_default=text('NOW()'), nullable=True)
    return_received_by = Column(Integer, ForeignKey('user_ext.id'), nullable=True)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=True)
    lga_id = Column(Integer, ForeignKey('lga.id'), nullable=True)
    street_address = Column(String, nullable=True)
    building_name = Column(String, nullable=True)
    contact_phone_num = Column(String, nullable=True)
    pos_user = Column(String, nullable=True)
    crypt_priv_key = Column(Text, nullable=True)
    crypt_pub_key = Column(Text, nullable=True)
    crypt_password = Column(Text, nullable=True)
    override_key = Column(Text, nullable=True)
    pos_lga = relationship(Lga, backref='poss_pos_lga', primaryjoin='Pos.lga_id == Lga.id')
    pos_return_received_by_fkey = relationship(UserExt, backref='poss_pos_return_received_by_fkey', primaryjoin='Pos.return_received_by == UserExt.id')
    pos_state = relationship(State, backref='poss_pos_state', primaryjoin='Pos.state_id == State.id')

    def __repr__(self):

       return self.device_model

 ### 


class AgentPosLink(Model):
    __tablename__ = "agent_pos_link"
    agent_id_fk = Column(Integer, ForeignKey('agent.id'), primary_key=True)
    pos_id_fk = Column(Integer, ForeignKey('pos.id'), primary_key=True)
    assigned_date = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    assigned_by = Column(String, nullable=True
		, comment="user")
    received_by = Column(String, nullable=True)
    received_date = Column(DateTime, server_default=text('NOW()'), nullable=True)
    received_location = Column(String, nullable=True)
    delivery_note = Column(Text, nullable=True)
    delivery_note_printed = Column(Boolean, default=False, nullable=True)
    activated = Column(Boolean, default=False, nullable=True)
    activation_date = Column(DateTime, server_default=text('NOW()'), nullable=True)
    activation_otp = Column(String, nullable=True)
    otp_sent = Column(Boolean, default=False, nullable=True)
    otp_sent_time = Column(DateTime, server_default=text('NOW()'), nullable=True)
    otp_used = Column(Boolean, default=False, nullable=True)
    history = Column(Text, nullable=True)
    agent_pos_link_agent = relationship(Agent, backref='agent_pos_links_agent_pos_link_agent', primaryjoin='AgentPosLink.agent_id_fk == Agent.id')
    agent_pos_link_pos = relationship(Pos, backref='agent_pos_links_agent_pos_link_pos', primaryjoin='AgentPosLink.pos_id_fk == Pos.id')

    def __repr__(self):

       return self.agent_id_fk

 ### 


class CommRef(Model):
    __tablename__ = "comm_ref"
    cr_id = Column(Integer, primary_key=True, autoincrement=True)
    agent_type = Column(Enum(Agent_type), name='t_agent_type', nullable=False)
    agent_tier_level = Column(Integer, ForeignKey('agent_tier.id'), nullable=True)
    agent_id_fk = Column(Integer, ForeignKey('agent.id'), nullable=True)
    state_id_fk = Column(Integer, ForeignKey('state.id'), nullable=True)
    lga_id_fk = Column(Integer, ForeignKey('lga.id'), nullable=True)
    biller_id_fk = Column(Integer, ForeignKey('biller.id'), nullable=True)
    biller_offering_id_fk = Column(Integer, ForeignKey('biller_offering.offering_id'), nullable=True)
    transaction_type_id_fk = Column(Integer, ForeignKey('trans_type.tt_id'), nullable=True)
    customer_segment_id_fk = Column(Integer, ForeignKey('customer_segment.cs_id'), nullable=True
		, comment="Customer Segment")
    special_promotion_id_fk = Column(Integer, ForeignKey('promotion.promo_id'), nullable=True)
    min_trans_amount = Column(Numeric, nullable=True)
    max_trans_amount = Column(Numeric, nullable=True)
    min_max_step = Column(Integer, nullable=True)
    min_comm_amount = Column(Numeric, nullable=True)
    max_comm_amount = Column(Numeric, nullable=True)
    commission_rate = Column(Numeric, nullable=True)
    start_time = Column(Time, nullable=True
		, comment="Start Time of Commission Rate Validity")
    end_time = Column(Time, nullable=True
		, comment="End Time of Commission Rate Validity")
    start_date = Column(Date, nullable=True
		, comment="In case this commission rate is only valid for a period")
    end_date = Column(Date, nullable=True)
    comm_ref_agent = relationship(Agent, backref='comm_refs_comm_ref_agent', primaryjoin='CommRef.agent_id_fk == Agent.id')
    comm_ref_agent_tier_level_fkey = relationship(AgentTier, backref='comm_refs_comm_ref_agent_tier_level_fkey', primaryjoin='CommRef.agent_tier_level == AgentTier.id')
    comm_ref_biller = relationship(Biller, backref='comm_refs_comm_ref_biller', primaryjoin='CommRef.biller_id_fk == Biller.id')
    comm_ref_biller_offering = relationship(BillerOffering, backref='comm_refs_comm_ref_biller_offering', primaryjoin='CommRef.biller_offering_id_fk == BillerOffering.offering_id')
    comm_ref_customer_segment = relationship(CustomerSegment, backref='comm_refs_comm_ref_customer_segment', primaryjoin='CommRef.customer_segment_id_fk == CustomerSegment.cs_id')
    comm_ref_lga = relationship(Lga, backref='comm_refs_comm_ref_lga', primaryjoin='CommRef.lga_id_fk == Lga.id')
    comm_ref_special_promotion = relationship(Promotion, backref='comm_refs_comm_ref_special_promotion', primaryjoin='CommRef.special_promotion_id_fk == Promotion.promo_id')
    comm_ref_state = relationship(State, backref='comm_refs_comm_ref_state', primaryjoin='CommRef.state_id_fk == State.id')
    comm_ref_transaction_type = relationship(TransType, backref='comm_refs_comm_ref_transaction_type', primaryjoin='CommRef.transaction_type_id_fk == TransType.tt_id')

    def __repr__(self):

       return self.cr_id

 ### 


class Person(Model):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, autoincrement=True)
    agent_id_fk = Column(Integer, ForeignKey('agent.id'), nullable=True)
    next_of_kin_id_fk = Column(Integer, ForeignKey('person.id'), nullable=True)
    person_role = Column(Enum(Person_role), name='t_person_role', nullable=False)
    first_name = Column(String, nullable=True)
    middle_name = Column(String, nullable=True)
    surname = Column(String, nullable=True)
    nick_name = Column(String, nullable=True)
    gender = Column(Enum(Gender), name='t_gender', nullable=False)
    photo_img = Column(String, nullable=True)
    signature_img = Column(String, nullable=True)
    bvn_no = Column(String, nullable=True)
    bvn_verified = Column(Boolean, default=False, nullable=True)
    bvn_verification_date = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    bvn_verification_code = Column(Text, nullable=True)
    tax_id = Column(String, nullable=True)
    home_poa_img = Column(String, nullable=True)
    home_poa_desc = Column(String, nullable=True)
    home_poa_valid = Column(Boolean, default=False, nullable=True)
    home_lat = Column(Float, nullable=True)
    home_lon = Column(Float, nullable=True)
    home_loc = Column(Text, nullable=True)
    home_ggl_code = Column(String, nullable=True)
    person_agent = relationship(Agent, backref='persons_person_agent', primaryjoin='Person.agent_id_fk == Agent.id')
    person_next_of_kin = relationship('Person', backref='persons_person_next_of_kin', primaryjoin='Person.next_of_kin_id_fk == Person.id', remote_side=[id])

    def __repr__(self):

       return self.first_name

 ### 


class Wallet(Model):
    __tablename__ = "wallet"
    __doc__ = " Each Pos has an individual wallet"
    id = Column(Integer, primary_key=True, autoincrement=True)
    agent_id_fk = Column(Integer, ForeignKey('agent.id'), nullable=True)
    pos_id_fk = Column(Integer, ForeignKey('pos.id'), nullable=True)
    wallet_name = Column(String, nullable=True)
    wallet_balance = Column(Numeric, nullable=True)
    wallet_locked = Column(Boolean, default=False, nullable=True)
    wallet_active = Column(Boolean, default=True, nullable=True)
    wallet_code = Column(String, nullable=True)
    wallet_crypt = Column(Text, nullable=True)
    wallet_narrative = Column(Text, nullable=True)
    wallet_agent = relationship(Agent, backref='wallets_wallet_agent', primaryjoin='Wallet.agent_id_fk == Agent.id')
    wallet_pos = relationship(Pos, backref='wallets_wallet_pos', primaryjoin='Wallet.pos_id_fk == Pos.id')

    def __repr__(self):

       return self.wallet_name

 ### 


class AgentPersonLink(Model):
    __tablename__ = "agent_person_link"
    person_id_fk = Column(Integer, ForeignKey('person.id'), primary_key=True)
    agent_id_fk = Column(Integer, ForeignKey('agent.id'), primary_key=True)
    agent_person_link_agent = relationship(Agent, backref='agent_person_links_agent_person_link_agent', primaryjoin='AgentPersonLink.agent_id_fk == Agent.id')
    agent_person_link_person = relationship(Person, backref='agent_person_links_agent_person_link_person', primaryjoin='AgentPersonLink.person_id_fk == Person.id')

    def __repr__(self):

       return self.person_id_fk

 ### 


class Contact(Model):
    __tablename__ = "contact"
    id = Column(Integer, primary_key=True, autoincrement=True
		, comment="Unique identifier for the contact.")
    person_id_fk = Column(Integer, ForeignKey('person.id'), nullable=True
		, comment="Reference to the individual associated with this contact.")
    agent_id_fk = Column(Integer, ForeignKey('agent.id'), nullable=True
		, comment="Reference to the organization associated with this contact.")
    contact_type_id_fk = Column(Integer, ForeignKey('contact_type.id')
		, comment="Reference to the type of contact.")
    contact = Column(String
		, comment="Actual contact value, e.g., phone number or email address.")
    priority = Column(Integer
		, comment="Ordering priority for displaying or using the contact. Lower value indicates higher priority.")
    best_time_to_contact_start = Column(Time, nullable=True
		, comment="Preferred start time when the individual/organization is available for contact.")
    best_time_to_contact_end = Column(Time, nullable=True
		, comment="Preferred end time for availability.")
    active_from_date = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True
		, comment="Date when this contact became active or relevant.")
    active_to_date = Column(Date, nullable=True
		, comment="Date when this contact ceases to be active or relevant.")
    for_business_use = Column(Boolean, default=False, nullable=True
		, comment="Indicates if the contact is primarily for business purposes.")
    for_personal_use = Column(Boolean, default=True, nullable=True
		, comment="Indicates if the contact is primarily for personal use.")
    do_not_use = Column(Boolean, default=False, nullable=True
		, comment="Indicates if there are any restrictions or requests not to use this contact.")
    is_active = Column(Boolean, default=True, nullable=True
		, comment="Indicates if this contact is currently active and usable.")
    is_blocked = Column(Boolean, default=False, nullable=True
		, comment="Indicates if this contact is blocked, maybe due to spam or other reasons.")
    is_verified = Column(Boolean, default=False, nullable=True
		, comment="Indicates if this contact has been verified, e.g., via OTP or email confirmation.")
    notes = Column(Text, nullable=True
		, comment="Additional notes or context about the contact.")
    contact_agent = relationship(Agent, backref='contacts_contact_agent', primaryjoin='Contact.agent_id_fk == Agent.id')
    contact_contact_type = relationship(ContactType, backref='contacts_contact_contact_type', primaryjoin='Contact.contact_type_id_fk == ContactType.id')
    contact_person = relationship(Person, backref='contacts_contact_person', primaryjoin='Contact.person_id_fk == Person.id')

    def __repr__(self):

       return self.id

 ### 


class Doc(Model):
    __tablename__ = "doc"
    id = Column(Integer, primary_key=True, autoincrement=True
		, comment="Unique identifier for the document.")
    doc_type_id_fk = Column(Integer, ForeignKey('doc_type.id'), nullable=True
		, comment="References the type of document e.g. passport, license.")
    person_id_fk = Column(Integer, ForeignKey('person.id'), nullable=True
		, comment="The person to whom the document belongs.")
    agent_id_fk = Column(Integer, ForeignKey('agent.id'), nullable=True
		, comment="The organization associated with the document.")
    doc_name = Column(String, nullable=True
		, comment="Name or title of the document.")
    doc_content_type = Column(Integer, ForeignKey('mime_type.id'), nullable=True
		, comment="MIME type of the document content e.g. application/pdf, image/jpeg.")
    doc_binaary = Column(Text, nullable=True)
    doc_url = Column(Text, nullable=True
		, comment="Actual doc in pdf or other format")
    doc_length = Column(Integer, nullable=True
		, comment="Size of the document in bytes or another measure.")
    doc_text = Column(Text, nullable=True
		, comment="Text content extracted from the document. Useful for search and analytics. May be stored in another database for scalability.")
    identification_number = Column(String, nullable=True
		, comment="Unique identification number, e.g., passport number.")
    serial_number = Column(String, nullable=True
		, comment="Serial number of the document if applicable.")
    description = Column(Text, nullable=True
		, comment="Detailed description or remarks about the document.")
    file_name = Column(String, nullable=True
		, comment="Name of the file if stored digitally.")
    page_count = Column(Integer, nullable=True
		, comment="Number of pages in the document, if applicable.")
    issued_on = Column(Date, nullable=True
		, comment="The date when the document was issued.")
    issued_by_authority = Column(String, nullable=True
		, comment="Authority or organization that issued the document.")
    issued_at = Column(String, nullable=True
		, comment="Place or location where the document was issued.")
    expires_on = Column(Date, nullable=True
		, comment="Expiration date of the document.")
    expired = Column(Boolean, default=False, nullable=True
		, comment="Flag to indicate if the document has expired.")
    verified = Column(Boolean, default=False, nullable=True)
    verification_date = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True
		, comment="The date when the document was verified.")
    verification_code = Column(Text, nullable=True)
    uploaded_on = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True
		, comment="Timestamp when the document was uploaded into the system.")
    updated_on = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True
		, comment="Timestamp when the document record was last updated.")
    doc_agent = relationship(Agent, backref='docs_doc_agent', primaryjoin='Doc.agent_id_fk == Agent.id')
    doc_doc_content_type_fkey = relationship(MimeType, backref='docs_doc_doc_content_type_fkey', primaryjoin='Doc.doc_content_type == MimeType.id')
    doc_doc_type = relationship(DocType, backref='docs_doc_doc_type', primaryjoin='Doc.doc_type_id_fk == DocType.id')
    doc_person = relationship(Person, backref='docs_doc_person', primaryjoin='Doc.person_id_fk == Person.id')

    def __repr__(self):

       return self.doc_name

 ### 


class PersonAdditionalData(Model):
    __tablename__ = "person_additional_data"
    person_id_fk = Column(Integer, ForeignKey('person.id'), primary_key=True)
    gender = Column(Enum(Gender), name='t_gender', nullable=False)
    religion = Column(String, nullable=True)
    ethnicity = Column(String, nullable=True)
    consumer_credit_score = Column(Integer, nullable=True)
    is_home_owner = Column(Boolean, nullable=True)
    person_height = Column(Integer, nullable=True)
    person_weight = Column(Integer, nullable=True)
    person_height_unit_of_measure = Column(String, nullable=True)
    person_weight_unit_of_measure = Column(String, nullable=True)
    highest_education_level = Column(String, nullable=True)
    person_life_stage = Column(String, nullable=True)
    mothers_maiden_name = Column(String, nullable=True)
    Marital_Status_cd = Column(Integer, nullable=True)
    citizenship_fk = Column(Integer, ForeignKey('country.id'), nullable=True)
    From_whom = Column(String, nullable=True)
    Amount = Column(Numeric, nullable=True)
    Interest_rate_pa = Column(Numeric, nullable=True)
    Number_of_people_depending_on_overal_income = Column(Integer, nullable=True)
    YesNo_cd_Bank_account = Column(Integer, nullable=True)
    YesNo_cd_Business_plan_provided = Column(Integer, nullable=True)
    YesNo_cd_Access_to_internet = Column(Integer, nullable=True)
    Introduced_by = Column(String, nullable=True)
    Known_to_introducer_since = Column(String, nullable=True)
    Last_visited_by = Column(String, nullable=True)
    Last_visited_on = Column(Date)
    person_additional_data_citizenship_fk_fkey = relationship(Country, backref='person_additional_datas_person_additional_data_citizenship_fk_fkey', primaryjoin='PersonAdditionalData.citizenship_fk == Country.id')
    person_additional_data_person = relationship(Person, backref='person_additional_datas_person_additional_data_person', primaryjoin='PersonAdditionalData.person_id_fk == Person.id')

    def __repr__(self):

       return self.mothers_maiden_name

 ### 


class PersonAdminData(Model):
    __tablename__ = "person_admin_data"
    person_id_fk = Column(Integer, ForeignKey('person.id'), primary_key=True)
    creation_time = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    failed_login_count = Column(Integer, nullable=True)
    failed_login_timestamp = Column(DateTime, server_default=text('NOW()'), nullable=True)
    password_last_set_time = Column(DateTime, server_default=text('NOW()'), nullable=True)
    profile_picture = Column(String, nullable=True)
    awatar = Column(String, nullable=True)
    screen_name = Column(String, nullable=True)
    user_priv_cert = Column(Text, nullable=True)
    user_pub_cert = Column(Text, nullable=True)
    alt_security_identities = Column(Text, nullable=True)
    generated_UID = Column(UUID, nullable=True)
    do_not_email = Column(Boolean, default=False, nullable=True)
    do_not_phone = Column(Boolean, default=False, nullable=True)
    do_not_mail = Column(Boolean, default=False, nullable=True)
    do_not_sms = Column(Boolean, default=False, nullable=True)
    do_not_trade = Column(Boolean, default=False, nullable=True)
    opted_out = Column(Boolean, default=False, nullable=True)
    do_not_track_update_date = Column(Date, nullable=True)
    do_not_process_from_update_date = Column(Date, nullable=True)
    do_not_market_from_update_date = Column(Date, nullable=True)
    do_not_track_location_update_date = Column(Date, nullable=True)
    do_not_profile_from_update_date = Column(Date, nullable=True)
    do_forget_me_from_update_date = Column(Date, nullable=True)
    do_not_process_reason = Column(String, nullable=True)
    no_merge_reason = Column(String, nullable=True)
    do_extract_my_data_update_date = Column(Date, nullable=True)
    should_forget = Column(Boolean, nullable=True)
    consumer_credit_score_provider_name = Column(String, nullable=True)
    web_site_url = Column(String, nullable=True)
    ordering_name = Column(String, nullable=True)
    hospitalizations_last5_years_count = Column(Integer, nullable=True)
    surgeries_last5_years_count = Column(Integer, nullable=True)
    dependent_count = Column(Integer, nullable=True)
    account_locked = Column(Boolean, default=False, nullable=True)
    send_individual_data = Column(Boolean, nullable=True)
    influencer_rating = Column(Integer, nullable=True)
    person_admin_data_person = relationship(Person, backref='person_admin_datas_person_admin_data_person', primaryjoin='PersonAdminData.person_id_fk == Person.id')

    def __repr__(self):

       return self.screen_name

 ### 


class Trans(Model):
    __tablename__ = "trans"
    id = Column(Integer, primary_key=True, autoincrement=True)
    coupon_id_fk = Column(Integer, ForeignKey('coupon.coupon_id'), nullable=True)
    customer_name = Column(String, nullable=True)
    trans_purpose = Column(Text, nullable=True)
    customer_id = Column(String, nullable=True)
    transaction_type = Column(Enum(Transaction_type), name='t_transaction_type', nullable=False)
    card_trans_type = Column(Enum(Card_trans_type), name='t_card_trans_type', nullable=False)
    agent_id_fk = Column(Integer, ForeignKey('agent.id'))
    payment_card_id_fk = Column(Integer, ForeignKey('payment_card.id'), nullable=True)
    pos_id_fk = Column(Integer, ForeignKey('pos.id'), nullable=True)
    wallet_id_fk = Column(Integer, ForeignKey('wallet.id'), nullable=True)
    biller_id_fk = Column(Integer, ForeignKey('biller.id'), nullable=True)
    biller_offering_id_fk = Column(Integer, ForeignKey('biller_offering.offering_id'), nullable=True)
    trans_time = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    currency_id_fk = Column(Integer, ForeignKey('currency.id'), nullable=True)
    trans_status = Column(Enum(Trans_status), name='t_trans_status', nullable=False)
    trans_route_id_fk = Column(Integer, ForeignKey('trans_routing_thresholds.id'), nullable=True)
    origin_source = Column(Enum(Origin_source), name='t_origin_source', nullable=False)
    origin_ref_code = Column(String, nullable=True)
    origin_trans_notes = Column(Text, nullable=True)
    origin_bank_id_fk = Column(Integer, ForeignKey('bank.id'), nullable=True)
    origin_institution_code = Column(String, nullable=True)
    origin_account_num = Column(String, nullable=True)
    origin_account_name = Column(String, nullable=True)
    origin_KYC_Level = Column(Integer, nullable=True)
    origin_Bank_Verification_Number = Column(String, nullable=True)
    origin_bvn = Column(String, nullable=True
		, comment="used for check balance")
    session_ref = Column(String, nullable=True)
    transaction_ref = Column(String, nullable=True)
    channelCode = Column(Integer, nullable=True)
    name_enquiry_ref = Column(String, nullable=True)
    api_transactionid = Column(String, nullable=True)
    receipt_no = Column(String, nullable=True)
    pin_based = Column(Boolean, default=False, nullable=True)
    pin_code = Column(String, nullable=True)
    pin_option = Column(String, nullable=True)
    authorization_code = Column(String, nullable=True)
    acquirer_name = Column(String, nullable=True)
    currency = Column(String, nullable=True)
    transaction_location = Column(String, nullable=True)
    payment_reference = Column(String, nullable=True)
    response_code = Column(String, nullable=True)
    trans_dest = Column(Enum(Trans_dest), name='t_trans_dest', nullable=False)
    bene_ref_code = Column(String, nullable=True)
    bene_trans_notes = Column(Text, nullable=True)
    bene_bank_id_fk = Column(Integer, ForeignKey('bank.id'), nullable=True)
    bene_account_num = Column(String, nullable=True)
    bene_institution_code = Column(String, nullable=True)
    bene_bank_verification_number = Column(String, nullable=True)
    bene_KYC_Level = Column(Integer, nullable=True)
    bene_account_name = Column(String, nullable=True)
    bene_phone_number = Column(String, nullable=True)
    bene_phone_denom = Column(String, nullable=True)
    bene_phone_product = Column(String, nullable=True)
    transaction_amount = Column(Numeric, nullable=True
		, comment="topup_amount or bank transfer amount")
    available_balance = Column(Numeric, nullable=True)
    svc_fees = Column(Numeric, nullable=True
		, comment="service fees")
    comm_total = Column(Numeric, nullable=True)
    comm_agent = Column(Numeric, nullable=True)
    comm_aggr = Column(Numeric, nullable=True)
    comm_ours = Column(Numeric, nullable=True)
    comm_other = Column(Numeric, nullable=True
		, comment="payments to others")
    comm_net_pct = Column(Float, nullable=True)
    tax = Column(Numeric, nullable=True)
    excise_duty = Column(Numeric, nullable=True)
    vat = Column(Numeric, nullable=True)
    transmit_amount = Column(Numeric, nullable=True)
    comm_narration = Column(Text, nullable=True
		, comment="how the commision was calculated")
    trans_currency = Column(String, nullable=True)
    trans_convert_currency = Column(String, nullable=True)
    trans_currency_exchange_rate = Column(Numeric, nullable=True)
    trans_date = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    customer_segment_id_fk = Column(Integer, ForeignKey('customer_segment.cs_id'), nullable=True)
    agent_tier_level_id_fk = Column(Integer, ForeignKey('agent_tier.id'), nullable=True)
    special_promotions_id_fk = Column(Integer, ForeignKey('promotion.promo_id'), nullable=True)
    fraud_marker = Column(Boolean, default=False, nullable=True
		, comment="fraudulent transaction")
    fraud_eval_outcome = Column(String, nullable=True
		, comment="returned by as Fraud, Not Fraud, Unknown")
    fraud_risk_score = Column(Float, nullable=True
		, comment="values 1-1000")
    fraud_prediction_explanations = Column(Text, nullable=True
		, comment=" list of explanations for how each event variable impacted the fraud prediction score.")
    fraud_rule_evaluations = Column(Text, nullable=True
		, comment="evaluations of the rules that were included in the detector version")
    fraud_event_num = Column(String, nullable=True
		, comment=" returned by AWS Fraud Detector")
    trans_narration = Column(Text, nullable=True
		, comment="we track and store very event that happens")
    trans_agent = relationship(Agent, backref='transs_trans_agent', primaryjoin='Trans.agent_id_fk == Agent.id')
    trans_agent_tier_level = relationship(AgentTier, backref='transs_trans_agent_tier_level', primaryjoin='Trans.agent_tier_level_id_fk == AgentTier.id')
    trans_bene_bank = relationship(Bank, backref='transs_trans_bene_bank', primaryjoin='Trans.bene_bank_id_fk == Bank.id')
    trans_biller = relationship(Biller, backref='transs_trans_biller', primaryjoin='Trans.biller_id_fk == Biller.id')
    trans_biller_offering = relationship(BillerOffering, backref='transs_trans_biller_offering', primaryjoin='Trans.biller_offering_id_fk == BillerOffering.offering_id')
    trans_coupon = relationship(Coupon, backref='transs_trans_coupon', primaryjoin='Trans.coupon_id_fk == Coupon.coupon_id')
    trans_currency = relationship(Currency, backref='transs_trans_currency', primaryjoin='Trans.currency_id_fk == Currency.id')
    trans_customer_segment = relationship(CustomerSegment, backref='transs_trans_customer_segment', primaryjoin='Trans.customer_segment_id_fk == CustomerSegment.cs_id')
    trans_origin_bank = relationship(Bank, backref='transs_trans_origin_bank', primaryjoin='Trans.origin_bank_id_fk == Bank.id')
    trans_payment_card = relationship(PaymentCard, backref='transs_trans_payment_card', primaryjoin='Trans.payment_card_id_fk == PaymentCard.id')
    trans_pos = relationship(Pos, backref='transs_trans_pos', primaryjoin='Trans.pos_id_fk == Pos.id')
    trans_special_promotions = relationship(Promotion, backref='transs_trans_special_promotions', primaryjoin='Trans.special_promotions_id_fk == Promotion.promo_id')
    trans_trans_route = relationship(TransRoutingThresholds, backref='transs_trans_trans_route', primaryjoin='Trans.trans_route_id_fk == TransRoutingThresholds.id')
    trans_wallet = relationship(Wallet, backref='transs_trans_wallet', primaryjoin='Trans.wallet_id_fk == Wallet.id')

    def __repr__(self):

       return self.customer_name

 ### 


class AgentDocLink(Model):
    __tablename__ = "agent_doc_link"
    agent_id_fk = Column(Integer, ForeignKey('agent.id'), primary_key=True)
    doc_id_fk = Column(Integer, ForeignKey('doc.id'), primary_key=True)
    verification_status = Column(Enum(Verification_status), name='t_verification_status', nullable=False)
    submit_date = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    notes = Column(Text, nullable=True)
    agent_doc_link_agent = relationship(Agent, backref='agent_doc_links_agent_doc_link_agent', primaryjoin='AgentDocLink.agent_id_fk == Agent.id')
    agent_doc_link_doc = relationship(Doc, backref='agent_doc_links_agent_doc_link_doc', primaryjoin='AgentDocLink.doc_id_fk == Doc.id')

    def __repr__(self):

       return self.agent_id_fk

 ### 


class PersonDocLink(Model):
    __tablename__ = "person_doc_link"
    person_id_fk = Column(Integer, ForeignKey('person.id'), primary_key=True)
    doc_id_fk = Column(Integer, ForeignKey('doc.id'), primary_key=True)
    verification_status = Column(Enum(Verification_status), name='t_verification_status', nullable=False)
    submit_date = Column(DateTime, server_default=text('NOW()'), default=func.now(), nullable=True)
    person_doc_link_doc = relationship(Doc, backref='person_doc_links_person_doc_link_doc', primaryjoin='PersonDocLink.doc_id_fk == Doc.id')
    person_doc_link_person = relationship(Person, backref='person_doc_links_person_doc_link_person', primaryjoin='PersonDocLink.person_id_fk == Person.id')

    def __repr__(self):

       return self.person_id_fk

 ### 

