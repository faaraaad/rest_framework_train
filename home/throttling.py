from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class CustomThro(UserRateThrottle):
    scope = 'InamCustom'