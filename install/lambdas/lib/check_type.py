from enum import Enum

class CheckType(Enum):
    MISSING_TAGS = 'MISSING_TAGS'
    NO_MFA_ON_ROOT = 'NO_MFA_ON_ROOT'
    NO_PASSWORD_POLICY = 'NO_PASSWORD_POLICY'
    PUBLIC_BUCKETS = 'PUBLIC_BUCKETS'
    NO_BUSINESS_SUPPORT = 'NO_BUSINESS_SUPPORT'
    NO_BUDGET = 'NO_BUDGET'
    UNUSED_EIP = 'UNUSED_EIP'
    UNATTACHED_EBS_VOLUMES = 'UNATTACHED_EBS_VOLUMES'
    USING_DEFAULT_VPC = 'USING_DEFAULT_VPC'
    EC2_IN_PUBLIC_SUBNET = 'EC2_IN_PUBLIC_SUBNET'