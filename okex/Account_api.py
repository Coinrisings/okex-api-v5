from .client import Client
from .consts import *


class AccountAPI(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, flag='0'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag)

    # Get Positions
    def get_position_risk(self, instType=None):
        params = {}
        if instType:
            params['instType'] = instType
        return self._request_with_params(GET, POSITION_RISK, params)

    # Get Balance
    def get_account(self, ccy=None):
        params = {}
        if ccy:
            params['ccy'] = ccy
        return self._request_with_params(GET, ACCOUNT_INFO, params)

    # Get Positions
    def get_positions(self, instType=None, instId=None):
        params = {}
        if instType:
            params['instType'] = instType
        if instId:
            params['instId'] = instId
        return self._request_with_params(GET, POSITION_INFO, params)

    # Get Bills Details (recent 7 days)
    def get_bills_detail(self, instType=None, ccy=None, mgnMode=None, ctType=None, type=None, subType=None, after=None, before=None,
                         limit=None):
        params = {k:v  for k, v in locals().items() if k != 'self' and v is not None}
        return self._request_with_params(GET, BILLS_DETAIL, params)

    # Get Bills Details (recent 3 months)
    def get_bills_details(self, instType=None, ccy=None, mgnMode=None, ctType=None, type=None, subType=None, after=None, before=None,
                          limit=None):
        params = {k:v  for k, v in locals().items() if k != 'self' and v is not None}
        return self._request_with_params(GET, BILLS_ARCHIVE, params)

    # Get Account Configuration
    def get_account_config(self):
        return self._request_without_params(GET, ACCOUNT_CONFIG)

    # Get Account Configuration
    def get_position_mode(self, posMode):
        params = {'posMode': posMode}
        return self._request_with_params(POST, POSITION_MODE, params)

    # Get Account Configuration
    def set_leverage(self, lever, mgnMode, instId=None, ccy=None, posSide=None):
        params = {k:v  for k, v in locals().items() if k != 'self' and v is not None}
        return self._request_with_params(POST, SET_LEVERAGE, params)

    # Get Maximum Tradable Size For Instrument
    def get_maximum_trade_size(self, instId, tdMode, ccy=None, px=None):
        params = {'instId': instId, 'tdMode': tdMode, 'ccy': ccy, 'px': px}
        return self._request_with_params(GET, MAX_TRADE_SIZE, params)

    # Get Maximum Available Tradable Amount
    def get_max_avail_size(self, instId, tdMode, ccy=None, reduceOnly=None):
        params = {'instId': instId, 'tdMode': tdMode, 'ccy': ccy, 'reduceOnly': reduceOnly}
        return self._request_with_params(GET, MAX_AVAIL_SIZE, params)

    # Increase / Decrease margin
    def Adjustment_margin(self, instId, posSide, type, amt):
        params = {'instId': instId, 'posSide': posSide, 'type': type, 'amt': amt}
        return self._request_with_params(POST, ADJUSTMENT_MARGIN, params)

    # Get Leverage
    def get_leverage(self, instId, mgnMode):
        params = {'instId': instId, 'mgnMode': mgnMode}
        return self._request_with_params(GET, GET_LEVERAGE, params)

    # Get the maximum loan of isolated MARGIN
    def get_max_load(self, instId, mgnMode, mgnCcy):
        params = {'instId': instId, 'mgnMode': mgnMode, 'mgnCcy': mgnCcy}
        # params = {k:v  for k, v in locals().items() if k != 'self' and v is not None}
        return self._request_with_params(GET, MAX_LOAN, params)

    # Get Fee Rates
    def get_fee_rates(self, instType, instId=None, uly=None, category=None):
        params = {'instType': instType,}
        if instId is not None:
            params['instId'] = instId
        if uly is not None:
            params['uly'] = uly,
        if category is not None:
            params['category'] = category
        return self._request_with_params(GET, FEE_RATES, params)

    # Get interest-accrued
    def get_interest_accrued(self, instId=None, ccy=None, mgnMode=None, after=None, before=None, limit=None):
        params = {k:v  for k, v in locals().items() if k != 'self' and v is not None}
        return self._request_with_params(GET, INTEREST_ACCRUED, params)

    # Get interest-accrued
    def get_interest_rate(self, ccy=None):
        params = {'ccy': ccy}
        return self._request_with_params(GET, INTEREST_RATE, params)

    # Set Greeks (PA/BS)
    def set_greeks(self, greeksType):
        params = {'greeksType': greeksType}
        return self._request_with_params(POST, SET_GREEKS, params)

    # Get Maximum Withdrawals
    def get_max_withdrawal(self, ccy=None):
        params = {}
        if ccy:
            params['ccy'] = ccy
        return self._request_with_params(GET, MAX_WITHDRAWAL, params)
