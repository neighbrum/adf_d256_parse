NegativeAmounts = {'}': 0, 'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9}
DataTypes = {'A': r'[a-zA-Z]+', 'AN': r'[a-zA-Z0-9 ]+', 'S': r' +', 'N': '\d+', 'PN': r'.{2}'} #NOTE: TSYS may use more than 2 bytes for PN...
UserAbbreviations = {'All': 'All associations and TSYS Acquiring Solutions', 'X': 'American Express®', 'CAPN': 'American Express Card Acceptance Processing Network®', 'D': 'Diners Club®', 'S': 'Discover®', 'E': 'Europay®', 'JCB': 'Japanese Credit Bureau®', 'M': 'MasterCard®', 'P': 'Private label', 'V': 'Visa®', 'V-UK': 'Visa United Kingdom®', 'V-EU': 'Visa European Union®', 'TSYS Acquiring Solutions': 'TSYS Acquiring Solutions'}
NetworkIDs = {'XL': 'Accel®', 'AF': 'Armed Forces Financial Network (AFFN)', 'AL': 'Alert®', 'AV': 'Avail®', 'BM': 'Bankmate®', 'CA': 'Cactus®', 'CS': 'Cash Station®', 'CU': 'Credit Union 24 (CU24)', 'EB': 'EBT® (Electronic Benefits Transfer)', 'EV': 'Evertec', 'EH': 'The Exchange®', 'DB': 'Generic debit', 'GF': 'Gulfnet®', 'HO': 'Honor®', 'IT': 'Instant Teller®', 'IL': 'Interlink®', 'JE': 'Jeanie®', 'MA': 'Mac®', 'ME': 'Maestro®', 'ML': 'Magicline®', 'MS': 'Money Station®', 'MO': 'Most®', 'IM': 'Mpact®', 'NY': 'NYCE®', 'PL': 'Pulse®', 'QU': 'Quest®', 'S': 'Shaam®', 'ST': 'Star (Explore)®', 'TY': 'Tyme®', 'VI': 'Visa®', 'C2': 'Visa Checkcard II®', 'YN': 'Yankee 24®'}

class Record:
    def __init__(self):
        pass

class BINHeaderRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N',
								'This field identifies that this record is the\n'
								+'BIN Header.\nValue = BH01'),)

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
			"recordType": None
    }

    LENGTH = 900

    def __init__(self,f):
        self.recordType = (None,)
        self.data = f.read(BINHeaderRecord.LENGTH)
        super(BINHeaderRecord, self).__init__()
        
class BINTrailerRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 
									'This field indicates that this record is\n'
									+'the BIN Trailer.\nValue = BT01'), 
							('2', 'Acquirer BIN', '6', '5-10', 'A/N', 
								'This field identifies the financial\n'
							  +'institution acting as the Acquirer of\n'
								+'this customer transaction.'), 
							('3', 'BIN Total Report Count', '8', '11-18', 'N', 
								 'This field identifies the total number of\n'
									+'Report(s) that are included for a\nparticular BIN.'), 
							('4', 'BIN Total Transaction\nCount', '12', '19-30', 'N', 
									'This field identifies the total number of\n'
									+'transactions that are included for a\nparticular BIN.'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
			"recordType": None,
			"acquirerBIN": None,
			"bINTotalReportCount": None,
			"bINTotalTransactionCount": None
    }

    LENGTH = 900

    def __init__(self,f):
        (self.recordType, 
					self.acquirerBIN, 
					self.bINTotalReportCount, 
					self.bINTotalTransactionCount) = (None)*4

        self.data = f.read(BINTrailerRecord.LENGTH)
        super(BINTrailerRecord, self).__init__()
        
class DiscoverPayPalExtensionRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 
							 'This field indicates this record\nis the Discover/PayPal\n'
							 +'Extension Record.\nValue = EX01'), 
							('2', 'Discover/PayPal\nAcquirer ID', '11', '5-15', 'N',
								'This field identifies a unique\nidentification number\n'
								+'assigned by Discover /PayPal\nNetworks to the Acquirer.'),
							('3', 'Discover/PayPal\nMerchant ID', '15', '16-30', 'AN',
							  'This field identifies a unique\nnumber assigned to the\n'
								+'merchant by Discover/PayPal\nNetworks.'), 
							('4', 'Discover/PayPal\nProcessing Code', '6', '31-36', 'N',
								"""This value identifies the\ncardholder transaction type\n
								and cardholder account type\n(if any) that are affected by\n
								the transaction.\nTransaction Type -\nPositions 1-2\n
								00 - Purchase of\nGoods / Services\n01 - Withdrawal/Cash\n
								Advance\n09 - Purchase of\nGoods or Services with\n
								Cash Over\n13 - Address\nVerification with a\n
								Goods or Service\nAuthorization for\nRecurring Billing\n
								14 - Recurring Billing\n(Automatic Payment)-\n
								Goods or Service\n15 - Installment\nPayment - Goods or\n
								Service\n18 - Address\nVerification Only\n20 - Merchandise\n
								Return\n28 - Recharge/Reload\n31 - Balance Inquiry\n
								90 - Activation\nAccount Type From -\nPositions 3-4\n
								00 - Not\nApplicable/Not\nSpecified\n10 - Savings Accounts\n
								20 - Checking Account\n30 - Credit Card\nAccount\n
								Account Type To -\nPositions 5-6\n00 - Not\nApplicable/Not\n
								Specified"""), 
							('5', 'Discover/PayPal\nPOS Entry Mode', '4', '37-40', 'N', 
								"""This field consists of two\nnumbers to indicate the\n
									method used to enter the\nPrimary Account Number\n
									(PAN) into the system and\none number to indicate the\n
									PIN entry capabilities.\nPAN and Date Entry Mode -\n
									Positions 1-2\n00 - Unknown\n01 - Manual (Key\nEntered)\n
									02 - Magnetic Stripe\n03 - Bar\nCode/Payment Code\n
									04 - Optical Character\nReader (OCR)\n
									05 - Integrated Circuit\nCard Reader\n07 - Electronic\n
									Commerce\n81 - Radio Frequency\nID Indicator - Magnetic\n
									Stripe\n82 - Mobile Commerce\n(mCommerce)\n
									83 - Radio Frequency\nID Indicator - Chip\n
									85 - Chip Fallback\n90 - Voice\nAuthorizations\n
									91 - Voice Response\nUnit\n92 - Batch\nAuthorizations\n
									93 - Batch\nAuthorizations Cash\nAccess\n
									PIN Entry Capability -\nPositions 3\n0 - Unspecified or\n
									Unknown\n1 - PIN entry capability\n2 - POS device does\n
									not have PIN entry\ncapability\n8 - POS device has\n
									PIN entry capability,\nbut PIN pad is not\n
									currently operative\n9 - PIN verified by POS\n
									device\nTSYS Reserved - Position 4\nSpace - Reserved for\n
									future use"""), 
							('6', 'Discover/PayPal\nResponse Code', '3', '41-43', 'A/N',
								"""This field identifies the\nauthorization response code\n
									from the authorizer.\nPositions 1-2\n
									POS Response Code value\n(Discover ISO field 39)\n
									Position 3\n
									Space - TSYS Reserved"""), 
							('7', 'Discover/PayPal\nPOS Data Code', '13', '44-56', 'A/N', 
								"""This value defines specific\ncard information capture\n
									conditions present at the time\n
									a card transaction took place\n
									at the point of service.\nDiscover/PayPal POS Data\n
									Code for valid values"""), 
							('8', 'Discover Cash Over\nAmount', '12', '57-68', 'N',
								'This field identifies the\namount of cash over\ndisbursed.'),
							('9', 'Discover/PayPal\nAVS Response Code', '1', '69', 'AN',
								"""This value contains the\nAddress Verification Service\n
									Response Code (AVS)\nResponse Code received from\n
									Discover/PayPal."""),
							('10', 'Cardholder Full\nName Result Code', '1', '70', 'AN',
								"""Possible values:\nB - Unknown response\n
									due to blank input\nF - First Name\nMatches, Last Name\n
									does not match\nK - Unknown\nL - First Name does\n
									not match, Last Name\nmatches\nM - First Name and\n
									Last Name match\nN - Nothing matches\nP - Not processed\n
									U - Retry, system\nunable to process\nW - No data from\n
									Issuer/ Authorization\nsystem"""), 
							('11', 'Registered User\nIndicator', '1', '71', 'A/N', 
								"""This field indicates if the\n
									cardholder is a registered\n
									user on a merchant's website\n
									(Discover transactions only).\n
									Y - The cardholder is a\n
									registered user with an online\n
									profile and login credentials\n
									N - The cardholder is not a\n
									registered user, and may\n
										shop only as a guest"""), 
							('12', 'Last Registered User\nProfile Date Change', '8',
								"""72-79', 'N', 'This field contains the date\n
									when the cardholder last\nvoluntarily changed their\n
									registered profile (Discover\n
									transactions only).\nFormat: MMDDYYYY"""),
							('13', 'PAN Reference\nIdentifier (PRI)', '35', '80-114',
								'A/N', """This field indicates the value\n
								assigned by Discover at the\n
								time of token provisioning and\n
								is associated with a specific\nmobile wallet."""), 
							('14', 'Reserved', '38', '115-152', 'A/N', 'Reserved'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"discoverPayPalAcquirerID": None,
		"discoverPayPalMerchantID": None,
		"discoverPayPalProcessingCode": None,
		"discoverPayPalPOSEntryMode": None,
		"discoverPayPalResponseCode": None,
		"discoverPayPalPOSDataCode": None,
		"discoverCashOverAmount": None,
		"discoverPayPalAVSResponseCode": None,
		"cardholderFullNameResultCode": None,
		"registeredUserIndicator": None,
		"lastRegisteredUserProfileDateChange": None,
		"pANReferenceIdentifier": None,
		"reserved13": None
                }

    LENGTH = 160

    def __init__(self,f):
        (self.recordType,
					self.discoverPayPalAcquirerID,
					self.discoverPayPalMerchantID,
					self.discoverPayPalProcessingCode,
					self.discoverPayPalPOSEntryMode,
					self.discoverPayPalResponseCode,
					self.discoverPayPalPOSDataCode,
					self.discoverCashOverAmount,
					self.discoverPayPalAVSResponseCode,
					self.cardholderFullNameResultCode,
					self.registeredUserIndicator,
					self.lastRegisteredUserProfileDateChange,
					self.pANReferenceIdentifier,
					self.reserved13) = (None)*14

        self.data = f.read(DiscoverPayPalExtensionRecord.LENGTH)
        super(DiscoverPayPalExtensionRecord, self).__init__()
        
class MastercardExtensionRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 
								"""This field indicates that the\nrecord is the Mastercard\n
									Extension Record.\nValue = EX02"""), 
							('2', 'Association Timestamp 10', '', '5-14', 'A/N', 
								'Date and time in MMDDhhmmss\nformat'),
							('3', 'EMS Risk Score', '3', '15-17', 'N', 
								"""Expert Monitoring Solutions Risk\nScore\n
									This field is included in the\nresponse, and indicates the\n
										transaction risk score.\nValid value:\n001-998"""), 
							('4', 'EMS Score Reason\nCode', '2', '18-19', 'A/N', 
								"""This Reason Code for the EMS\n
									score indicates the key factors\n
										that influenced the fraud score."""), 
							('5', 'Domain Server', '1', '20', 'N', 
								'Valid values:\n1=Issuer Domain\n2=Acquirer Domain'),
							('6', 'Mobile Device Type', '2', '21-22', 'N', 
								"""This field identifies the type of\n
									PayPass device used by the\ncardholder to initiate the\n
									transaction. This field is required\n
									for all Mastercard PayPass\n(contactless) transactions.\n
									Valid values"""),
							('7', 'Transit Transaction\nType Indicator', '2', '23-24', 'N',
								"""This field identifies the type of\ntransit transactions."""),
							('8', 'Transportation Mode\nIndicator', '2', '25-26', 'N',
								'This field identifies the mode of\ntransportation used.'),
							('9', 'Mastercard Wallet\nIdentifier', '3', '27-29', 'A/N', 
								"""This Mastercard value is\ngenerated by the Masterpass\n
									online platform. This value is\n
									passed to the merchant at the\n
									time of consumer checkout for\n
									ecommerce transactions, and is\n
									included in the authorization\nrequest."""),
							('10', 'Authorization Indicator', '1', '30', 'A/N',
								"""This field defines the type of\n
									authorization request and is\n
									required to be included on all\n
									Mastercard authorization request\n
									transactions.\nValid values:\nF - Final Authorization - A\n
									request for a final amount\nthat may not be canceled\n
									once it is approved\nP - Pre-Authorization - A\n
									request for an estimated\namount\nU - Undefined\n
									Authorization - Used when\nthe intent is unknown, and\n
									the transaction is neither\na preauthorization nor a\n
									final authorization"""), 
							('11', 'Lane ID', '8', '31-38', 'N', 
								"""This data uniquely identifies a\n
									terminal at the card acceptor\n
									location of acquiring institutions\n
									or merchant POS systems."""),
							('12', 'Transaction Integrity\nClass', '2', '39-40', 'A/N', 
								"""This value shows the safety and\n
									security of the transaction and\n
									includes the final assessment of\n
									the validity of the card and the\n
									cardholder. Some transactions\n
									are inherently more secure than\n
									others are. For example, EMV\n
									chip cards are more secure than\n
									magnetic stripe cards. There are\n
									nuances across both the\ntechnology (card) and the\n
									Cardholder Verification Method\n
									(cardholder), but the combination\n
									was assessed across the\nspectrum to determine the overall\n
									integrity of the transaction.\n
									Note: This field is required when\n
									included by Mastercard. Effective\n
									in April 2019, Mastercard\nincorporates the Transaction\n
									Integrity Class in the interchange\nprocess.\nValid Values:\n
									Card and Cardholder Present:\nA1 - EMV/Token in a Secure,\n
									Trusted Environment\nB1 - EMV/Chip Equivalent\n
									C1 - Mag Stripe\nE1 - Key Entered\nU0 � Unclassified\n
									Card and/or Cardholder Not\nPresent:\n
									A2 - Digital Transactions\nB2 - Authenticated Checkout\n
									C2 - Transaction Validation\nD2 - Enhanced Data\n
									E2 - Generic Messaging\nU0 - Unclassified"""), 
							('13', 'Reserved', '112', '41-152', 'A/N', 'Reserved'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"associationTimestamp10": None,
		"eMSRiskScore": None,
		"eMSScoreReasonCode": None,
		"domainServer": None,
		"mobileDeviceType": None,
		"transitTransactionTypeIndicator": None,
		"transportationModeIndicator": None,
		"mastercardWalletIdentifier": None,
		"authorizationIndicator": None,
		"laneID": None,
		"transactionIntegrityClass": None,
		"reserved12": None
    }

    LENGTH = 160

    def __init__(self,f):
        (self.recordType, 
					self.associationTimestamp10, 
					self.eMSRiskScore, 
					self.eMSScoreReasonCode, 
					self.domainServer, 
					self.mobileDeviceType, 
					self.transitTransactionTypeIndicator, 
					self.transportationModeIndicator, 
					self.mastercardWalletIdentifier, 
					self.authorizationIndicator, 
					self.laneID, 
					self.transactionIntegrityClass, 
					self.reserved12) = (None)*13
        self.data = f.read(MastercardExtensionRecord.LENGTH)
        super(MastercardExtensionRecord, self).__init__()
        
class AdditionalDetailDataExtensionRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 
								"""This field indicates this\nrecord is the Additional\n
									Detail Data Extension\nRecord.\nValue = EX03"""),
							('2', 'Terminal Verification\nResults', '10', '5-14', 'A/N',
								"""This field identifies the status\n
									of the different functions as\nseen from the terminal."""), 
							('3', 'Cardholder\nVerification Method', '6', '15-20', 'A/N', 
								"""This field identifies a method\nof verification of the\
									cardholder supported by the\napplication."""),
							('4', 'Form Factor\nIndicator', '8', '21-28', 'A/N',
								"""This field defines the type of\nconsumer device used to\n
									conduct a\ncontact/contactless\ntransaction."""))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"terminalVerificationResults": None,
		"cardholderVerificationMethod": None,
		"formFactorIndicator": None
    }

    LENGTH = 320

    def __init__(self,f):
        self.recordType, self.terminalVerificationResults, self.cardholderVerificationMethod, self.formFactorIndicator = (None, None, None, None)
        self.data = f.read(AdditionalDetailDataExtensionRecord.LENGTH)
        super(AdditionalDetailDataExtensionRecord, self).__init__()
        
class MerchantDataExtensionRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N',
								"""This field indicates this record\n
									is the Additional Detail Data\nExtension Record.\n
									Value = EX04"""), 
							('2', 'PSP Name', '20', '5-24', 'A/N',
								'Payment Service Provider or\nAggregator'),
							('3', 'Seller Street\nAddress', '25', '25-49', 'A/N',
								'Street Address of the Seller'), 
							('4', 'Seller City', '13', '50-62', 'A/N', "Seller's City"),
							('5', 'Seller Postal Code', '10', '63-72', 'A/N',
								"Seller's Postal Code"), 
							('6', 'Seller Region Code 3', '', '73-75', 'A/N', 
								"Seller's State/Region Code"), 
							('7', 'Seller Email', '40', '76-115', 'A/N', 
								"""This field identifies the email\n
									address for the Seller of the\n
									Payment Service\n
									Provider/Aggregator or OptBlue\n
									participant."""), 
							('8', 'Seller Telephone', '10', '116-125', 'A/N',
								"""This field identifies the\ntelephone number for the Seller\n
									of the Payment Service\nProvider/Aggregator or OptBlue\n
									participant."""), 
							('9', 'Reserved', '27', '126-152', 'A/N', 'Reserved'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"pSPName": None,
		"sellerStreetAddress": None,
		"sellerCity": None,
		"sellerPostalCode": None,
		"sellerRegionCode3": None,
		"sellerEmail": None,
		"sellerTelephone": None,
		"reserved8": None
    }

    LENGTH = 160

    def __init__(self,f):
        (self.recordType,
					self.pSPName,
					self.sellerStreetAddress,
					self.sellerCity,
					self.sellerPostalCode,
					self.sellerRegionCode3,
					self.sellerEmail,
					self.sellerTelephone,
					self.reserved8) = (None)*9

        self.data = f.read(MerchantDataExtensionRecord.LENGTH)
        super(MerchantDataExtensionRecord, self).__init__()
        
class ReportHeaderRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 
								"""This field identifies that this record is the\n
								Report Header.\nValue = RH01"""), 
							('2', 'Acquirer BIN', '6', '5-10', 'A/N',
								"""This field identifies the financial institution\n
									acting as the Acquirer of this customer\ntransaction."""), 
							('3', 'Agent', '6', '11-16', 'A/N', 
								"""This value identifies the agent filter, if\n
									defined, from the report registration. The\n
									agent is a six character value assigned\n
									by the merchant's bank or processor.\n
									The field is issued by the merchant's\n
									member bank or processor for purposes\n
									of identifying a specific agent entity of the\n
									member bank or processor.\nPossible values:\n
									6 character agent value\n
									NA - then left justified, space filled\n
									Space filled"""), 
							('4', 'Chain', '6', '17-22', 'A/N', 
								"""This value identifies the chain filter, if\n
									defined, from the report registration. The\n
									Chain is a six character value assigned\n
									by the merchant�s bank or processor.\n
									The field is issued by the merchant's\n
									member bank or processor for purposes\n
									of identifying a specific chain of the agent\n
									organization.\nPossible values:\n
									6 character chain value\n
									NA - then left justified, space filled\n
									Space filled"""), 
							('5', 'Effective Start Date &\nT\nime', '19', '23-41', 'A/N', 
								"""This field identifies the start date and\n
									time (GMT) from the report registration.\n
									Example:\nYYYY-MM-DD HH:MM:SS (using a 24-\n
									hour clock)"""), 
							('6', 'Effective End Date &\nT\nime', '19', '42-60', 'A/N',
								"""This field identifies the end date and time\n
									Greenwich Mean Time (GMT) from the\n
									report registration.\n
									Example:\nYYYY-MM-DD HH:MM:SS (using a 24-\nhour clock)"""))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"acquirerBIN": None,
		"agent": None,
		"chain": None,
		"effectiveStartDateTime": None,
		"effectiveEndDateTime": None
    }

    LENGTH = 900

    def __init__(self,f):
        (self.recordType,
					self.acquirerBIN,
					self.agent,
					self.chain,
					self.effectiveStartDateTime,
					self.effectiveEndDateTime) = (None)*6

        self.data = f.read(ReportHeaderRecord.LENGTH)
        super(ReportHeaderRecord, self).__init__()
        
class ReportHeaderRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 
								"""This field indicates that this record is\n
									the Report Header.\nValue = RH02"""),
							('2', 'Acquirer BIN', '6', '5-10', 'A/N',
								"""This field identifies the financial\n
									institution acting as the Acquirer of\n
									this customer transaction."""),
							('3', 'Agent', '6', '11-16', 'A/N',
								"""This field identifies the agent filter, if\n
									defined, from the report registration.\n
									The agent is a six character value\n
									assigned by the merchant's bank or\n
									processor.\nPossible values:\n6 character agent value\n
									NA - then left justified space\nfilled\nSpace filled"""),
							('4', 'Chain', '6', '17-22', 'A/N', 
								"""This field identifies the chain filter, if\n
									defined, from the report registration.\n
									The Chain is a six character value\n
									assigned by the merchant�s bank or\nprocessor.\n
									Possible values:\n6 character chain value\n
									NA - then left justified, space\nfilled\nSpace filled"""),
							('5', 'Effective Start Date &\nT\nime', '19', '23-41', 'A/N', 
									"""This field identifies the start date and\n
										time (GMT) from the report\nregistration.\nExample:\n
										YYYY-MM-DD HH:MM:SS (using a\n24-hour clock)"""),
							('6', 'Effective End Date &\nT\nime', '19', '42-60', 'A/N', 
								"""This field identifies the end date and\n
									time (GMT) from the report generation.\nExample:\n
										YYYY-MM-DD HH:MM:SS (using a\n24-hour clock)"""),
							('7', 'Include Host Capture\nTransactions', '1', '61', 'A/N', 
									"""This field indicates if host capture\n
										adjustment and inquiry transactions\n
										are present in the report.\nPossible values:\n
										1 - Includes adjustment\ntransaction (TD02) and inquiry\n
										transaction (TD03) records\n2 - Includes batch inquiry\n
										transactions only\n3 - Includes adjustment\n
										transactions only"""))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"acquirerBIN": None,
		"agent": None,
		"chain": None,
		"effectiveStartDateTime": None,
		"effectiveEndDateTime": None,
		"includeHostCaptureTransactions": None
    }

    LENGTH = 81

    def __init__(self,f):
        (self.recordType,
					self.acquirerBIN,
					self.agent,
					self.chain,
					self.effectiveStartDateTime,
					self.effectiveEndDateTime,
					self.includeHostCaptureTransactions) = (None)*7
        self.data = f.read(ReportHeaderRecord.LENGTH)
        super(ReportHeaderRecord, self).__init__()
        
class ReportTrailer(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates that this record is the\nReport Trailer.\nValue = RT01'), ('2', 'Acquirer BIN', '6', '5-10', 'A/N', 'This field identifies the financial institution\nacting as the Acquirer of this customer\ntransaction.'), ('3', 'Agent', '6', '11-16', 'A/N', 'This field identifies the agent filter, if\ndefined, from the report registration. The\nagent is a six character value assigned\nby the merchant�s bank or processor.\nPossible values:\n6 character agent value\nNA - then left justified, space filled\nSpace filled'), ('4', 'Chain', '6', '17-22', 'A/N', 'This field identifies the chain filter, if\ndefined, from the report registration. The\nchain is a six character value assigned\nby the merchant�s bank or processor.\nPossible values:\n6 character chain value\nNA - then left justified, space filled\nSpace filled'), ('5', 'Effective Start Date', '19', '23-41', 'A/N', 'This field identifies the start date and time\n(GMT) from the report registration.\nExample:\nYYYY-MM-DD HH:MM:SS (using a 24-\nhour clock)'), ('6', 'Effective End Date', '19', '42-60', 'A/N', 'This field identifies the end date and time\n(GMT) from the report registration.\nExample:\nYYYY-MM-DD HH:MM:SS (using a 24-\nhour clock)'), ('7', 'Include Error\nTransaction', '1', '61', 'A/N', 'This field indicates if error transactions\nare present in the report.\n1 = Includes all transactions\n4 = Includes all transactions\nexcept Hierarchy Validation errors'), ('8', 'Reserved (internal)', '20', '62-81', 'A/N', 'Reserved for TSYS Acquiring Solutions\nuse only'), ('9', 'Report Total\nTransaction Count', '12', '82-93', 'N', 'This field identifies the total number of\ntransactions included in the report.'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"acquirerBIN": None,
		"agent": None,
		"chain": None,
		"effectiveStartDate": None,
		"effectiveEndDate": None,
		"includeErrorTransaction": None,
		"reserved7": None,
		"reportTotalTransactionCount": None
                }

    LENGTH = 900

    def __init__(self,f):
        self.recordType, self.acquirerBIN, self.agent, self.chain, self.effectiveStartDate, self.effectiveEndDate, self.includeErrorTransaction, self.reserved7, self.reportTotalTransactionCount = (None, None, None, None, None, None, None, None, None)
        self.data = f.read(ReportTrailer.LENGTH)
        super(ReportTrailer, self).__init__()
        
class ReportTrailerRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates that this record is the\nReport Header.\nValue = RT02'), ('2', 'Acquirer BIN', '6', '5-10', 'A/N', 'This field identifies the financial institution\nacting as the Acquirer of this customer\ntransaction.'), ('3', 'Agent', '6', '11-16', 'A/N', 'This field identifies the agent filter, if\ndefined, from the report registration. The\nagent is a six character value assigned\nby the merchant�s bank or processor.\nPossible values:\n6 character agent value\nNA - then left justified, space filled\nSpace filled'), ('4', 'Chain', '6', '17-22', 'A/N', 'This field identifies the chain filter, if\ndefined, from the report registration. The\nchain is a six character value assigned\nby the merchant�s bank or processor.\nPossible values:\n6 character chain value\nNA - then left justified, space filled\nSpace filled'), ('5', 'Effective Start Date &\nT\nime', '19', '23-41', 'A/N', 'This field identifies the start date and\ntime (GMT) from the report registration.\nExample:\nYYYY-MM-DD HH:MM:SS (using a 24-\nhour clock)'), ('6', 'Effective End Date &\nT\nime', '19', '42-60', 'A/N', 'This field identifies the end date and time\n(GMT) from the report generation.\nExample:\nYYYY-MM-DD HH:MM:SS (using a 24-\nhour clock)'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"acquirerBIN": None,
		"agent": None,
		"chain": None,
		"effectiveStartDateTime": None,
		"effectiveEndDateTime": None
                }

    LENGTH = 93

    def __init__(self,f):
        self.recordType, self.acquirerBIN, self.agent, self.chain, self.effectiveStartDateTime, self.effectiveEndDateTime = (None, None, None, None, None, None)
        self.data = f.read(ReportTrailerRecord.LENGTH)
        super(ReportTrailerRecord, self).__init__()
        
class TransactionDetailRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates that this record\nis the Transaction Detail Header.\nValue = TD01'), ('2', 'Acquirer BIN', '6', '5-10', 'A/N', 'This field identifies the financial\ninstitution acting as the Acquirer of\nthis customer transaction.'), ('3', 'Exit BIN', '5', '11-15', 'A/N', 'This field identifies the extra data\nthat is received from the ISO\nmessage for the BIN.'), ('4', 'Agent', '6', '16-21', 'A/N', 'The field is assigned by the\nmerchant�s member bank or\nprocessor for purposes of\nidentifying a specific agent entity\nof the member bank or processor.\nPossible values:\n6 character Agent value\nNA - then left justified,\nspace filled\nSpace filled'), ('5', 'Chain', '6', '22-27', 'A/N', 'The field is assigned by the\nmerchant�s member bank or\nprocessor for purposes of\nidentifying a specific chain of the\nagent organization.\nPossible values:\n6 character Chain value\nNA - then left justified,\nspace filled\nSpace filled'), ('6', 'e-Connections\nMerchant\nNumber', '15', '28-42', 'A/N', 'This field identifies the merchant\nnumber that is displayed in the e-\nConnections Authorization and\nCapture module.'), ('7', 'Store Number', '4', '43-46', 'A/N', 'This field identifies the store\nnumber.'), ('8', 'Terminal Number 4', '', '47-50', 'A/N', 'This field identifies the terminal\nnumber.'), ('9', 'Card Acceptor\nID', '15', '51-65', 'A/N', 'This field identifies the merchant\nnumber plus the first three of the\nstore.'), ('10', 'Merchant Name', '25', '66-90', 'A/N', 'This field identifies the name of the\nmerchant.\nThis field identifies the name of the\nSub-Merchant if the transaction is\nsubmitted by a Payment\nFacilitator.'), ('11', 'Card Acceptor\nCity', '18', '91-108', 'A/N', "This field identifies the merchant's\nlocation where the cardholder�s\ntransaction occurs.\nExample: Chandler\nThis field identifies the City of the\nSub-Merchant if the transaction is\nsubmitted by a Payment\nFacilitator."), ('12', 'Card Acceptor\nState', '2', '109-110', 'A/N', "This field identifies the merchant's\nlocation where the cardholder�s\ntransaction occurs. \nExample: AZ\nThis field identifies the State of the\nSub- Merchant if the transaction is\nsubmitted by a Payment\nFacilitator."), ('13', 'Card Acceptor\nCountry Code', '2', '111-112', 'A/N', "Includes the merchant's location\nwhere the cardholder�s transaction\noccurs.\nThis field identifies the Country\nCode of the Sub-Merchant if the\ntransaction is submitted by a\nPayment Facilitator."), ('14', 'Country Code\nPAN Extended', '3', '113-115', 'A/N', 'This field identifies a code in the\ncard�s magnetic stripe that\nidentifies the country of the card\nissuer institution.'), ('15', 'National POS\nGeographic Data', '14', '116-129', 'A/N', 'This field identifies the location of\nthe cardholder transaction.\nThis field identifies the location of\nthe Sub- Merchant if the\ntransaction is submitted by a\nPayment Facilitator\nState code (positions 1-2)\nCounty code (positions 3-5)\nPostal code (positions 6-\n14)\nSee U.S. state codes for a list of\nstate codes.'), ('16', 'MCC Code', '4', '130-133', 'N', 'This field identifies a merchant\ncategory code that describes a\nmerchant�s type of business,\nproduct, or service.'), ('17', 'Merchant ABA\nNumber', '9', '134-142', 'A/N', 'This field identifies the Merchant\nABA Number. It consists of 0 to 9\ncharacters and identifies the\nmerchant to a direct debit switch.\nThis number is provided by the\nsigning member or processor.'), ('18', 'Card Acceptor\nSettlement\nAgent', '4', '143-146', 'A/N', 'This field identifies the financial\ninstitution.'), ('19', 'ISO Source\nStation ID', '6', '147-152', 'N', 'This field identifies the originator of\nthe ISO request message.'), ('20', 'Acquirer\nBusiness ID', '8', '153-160', 'A/N', 'This field identifies the VISA\nassigned Acquirer Business ID.'), ('21', 'Acquirer Country\nCode', '3', '161-163', 'A/N', 'This field identifies the country of\nthe acquiring institution for the\nmerchant.'), ('22', 'Card Type', '1', '164', 'A/N', 'This field identifies the card plan\ntype.\nA <space> or "?" value in this field\nindicates the card type was\nunknown.\nCREDIT\nThe transaction is identified\nas credit if ADF Field 84\nNID=�NULL� or �0002�\n3\nAmerican Express\n4\nVisa\n5\nMastercard\n7\nJCB\n8\nDiscover\n9\nOther\nP\nPayPal\nDEBIT\nThe transaction is identified as\ndebit if Field 84 NID is not =\n�NULL� and NID is not=�0002�\nSee Network ID and Sharing\nGroup Codes for a list of codes.'), ('23', 'Primary Account\nNumber', '22', '165-186', 'A/N', 'This field identifies the primary\naccount number.\nThis field may be masked based\non configuration.'), ('24', 'EXT PAN', '28', '187-214', 'A/N', 'This field is used for the numeric\naccount numbers or numbers\nencoded on track 3. It may also\ncontain a cardholder identification\nnumber that points to one or more\ncardholder accounts.\nThis field may be masked based\non configuration.'), ('25', 'Account ID 1', '28', '215-242', 'A/N', 'For Mastercard transactions, this\nvalue is used for the Paypass\nPrimary Account Number.\nFormatting is left justified and\nspace filled.\nThis field may be masked based\non configuration.'), ('26', 'Card expiration\nDate', '4', '243-246', 'N', 'This field identifies the card\nexpiration date in YYMM format.'), ('27', 'Issuing\nInstitution\nStation ID', '6', '247-252', 'A/N', 'This field identifies the endpoint\nthat introduced the message into\nthe network.'), ('28', 'Issuing\nInstitution ID\nCode', '11', '253-263', 'A/N', 'This field identifies the Issuer ID of\nthe cardholder�s account.'), ('29', 'Julian Day', '3', '264-266', 'N', 'This field identifies the Julian day\nof the year, which is a number\nrepresenting the ordinal position of\nthe transaction date.\nFormat = DDD\nExample: December 30 in a non-\nleap year = 364'), ('30', 'Transaction Date\n& Time', '19', '267-285', 'A/N', 'This field identifies the date and\ntime stamp of a transaction based\non GMT.\nExample:\nYYYY-MM-DD HH:MM:SS (using\na 24-hour clock)'), ('31', 'Settlement Date', '4', '286-289', 'N', "This field identifies the month and\nthe day when the message\nbecame part of SMS' settlement\nbetween the acquirer and issuer.\nExample: 0501"), ('32', 'Load Date &\nT\nime', '19', '290-308', 'A/N', 'This field identifies the date and\ntime (GMT) the transaction was\nloaded into the report by a third\nparty.\nExample:\nYYYY-MM-DD HH:MM:SS (using\na 24-hour clock)'), ('33', 'Message Type', '4', '309-312', 'A/N', 'This value identifies the ISO\nrequest type.\nMessage types 0100/0200/0400/\n0420 are messages from an\nendpoint to a card issuer. TSYS\nAcquiring Solutions uses these for\nauthorization and verification\nrequests to be routed from the\nendpoint to the card issuer.\n0120 message types are for\nAutomated Fuel Dispenser (AFD)\nadvice messages indicating the\nfinal amount dispensed.'), ('34', 'Processing\nCode', '6', '313-318', 'A/N', 'This value identifies the cardholder\ntransaction type and cardholder\naccount types (if any) that are\naffected by the transaction:\nPositions 1 - 2: Transaction Type\nPositions 3 - 4: Account Type\n(from)\nPositions 5 - 6: Account Type (to)'), ('35', 'Access Method', '2', '319-320', 'A/N', 'This value identifies the\nconnectivity method utilized to\ntransmit the transaction and maps\ndirectly to the ASCII Line Type.\nRefer to Access Method Definition\nof Values for possible values.'), ('36', 'ASCII Bill Code', '1', '321', 'A/N', 'This value identifies the billing\ndescriptor. It may contain\nadditional billing or reporting\ninformation.\nRefer to Access Method Definition\nof Values for possible values.'), ('37', 'Transaction\nIdentifier', '15', '322-336', 'A/N', 'This value identifies a key element\nthat links original authorization and\nfinancial requests to subsequent\nmessages.'), ('38', 'Retrieval\nReference\nNumber', '12', '337-348', 'N', 'This value identifies a number that\nis used with other key data\nelements to identify and track all\nmessages related to a given\ncardholder transaction.'), ('39', 'Systems Trace\nAudit Number', '6', '349-354', 'A/N', 'This value uniquely identifies a\ncardholder transaction and all the\nmessage types it comprises per\nindividual program rules.'), ('40', 'Authorized\nAmount', '12', '355-366', 'N', 'This value identifies the\ntransaction amount. The decimal\nplace is implied based on\ncurrency.\nFor AFD message types, this\nvalue represents the final amount\nto be settled.'), ('41', 'Cardholder\nBilling Amount', '12', '367-378', 'N', 'This value identifies a transaction\namount converted to the currency\nused to bill the cardholder�s\naccount.'), ('42', 'Approval Code', '6', '379-384', 'A/N', 'This value identifies the approval\ncode from the authorizer.'), ('43', 'Authorization\nResponse', '2', '385-386', 'A/N', 'This value identifies the\nauthorization response code from\nthe authorizer.\nRefer to Response Codes for valid\nresponse codes.'), ('44', 'Internal Error\nCode', '1', '387', 'A/N', 'Possible values:\nT = Timeout\nG = Standard GEN2\nparsing/edit error\nS = SARATOGA\nparsing/edit error\nV = VIP ISO reject (This\nISO reject condition can\nonly occur for VIP\ntransactions.)\nC = Citi GEN2 parsing/edit\nerror\nBlank = not timeout or new\nreject type'), ('45', 'ISO Reject Code 4', '', '388-391', 'A/N', 'This field identifies the specific\ntype of reject if an internal error\ncode exists.\nRefer to Reject Codes and\nNumeric Sequence for a list of\nreject codes.'), ('46', 'CVV2 / CVC2 /\nCID Response\nType', '1', '392', 'A/N', 'This field identifies the presence of\nthe Card Verification Values.\nValid values:\n0 = Only the normal\nresponse code in ISO field\n39 should be returned\n1 = The normal response\ncode in ISO field 39 and the\nCVV2 result in ISO field\n44.10 should be returned'), ('47', 'CVV2 / CVC2 /\nCID Presence\nIndicator', '1', '393', 'A/N', 'This field identifies the presence of\ncard verification values.\nValid values:\n0 = CVV2 value is\ndeliberately bypassed or is\nnot provided by the\nmerchant\n1 = CVV2 value is present\n2 = CVV2 is on the card\nbut is illegible\n9 = Cardholder states that\nthe card does not have a\nCVV2 imprint'), ('48', 'Message\nReason Code', '4', '394-397', 'A/N', 'This field supports multiple\nusages.\nReversal Messages\nIf there is no reversal, data will not\nbe present.\nPossible values for Reversal\nMessages:\n2501 - Transaction voided\nby customer\n2502 - Transaction has not\ncompleted (Request timed\nout or terminal\nmalfunctioned)\n2503 - No confirmation from\nthe point of sale\n2504 - POS partial reversal\n2516 - Premature chip card\nremoval (after online\nrequest sent, before\nresponse received)\n2517 - Chip declined\ntransaction after online\nissuer approved\nVisa Merchant Initiated\nTransactions\nThe Message Reason Code field\nwill be used to identify Merchant\nInitiated Transactions (MIT) for\nVisa. A MIT is any transaction that\nrelates to a previous consumer-\ninitiated transaction, but is\nconducted without the consumer\nbeing present and without any\ncardholder validation performed.\nPossible values for Visa\nMerchant Initiated\nTransactions:\n3900 - Incremental\nAuthorization\n3901 - Resubmission\n3902 - Delayed Charges\n3903 - Reauthorization\n3904 - No Show'), ('49', 'Additional\nResponse Data', '25', '398-422', 'A/N/S', 'This field contains miscellaneous\nresponse message data. TSYS\nAcquiring Solutions uses this field\nand its subfields for the following\nspecial codes:\nRefer to Additional Response Data\nCodes for a list of codes to include\nthe length, position, and\ndescription.'), ('50', 'Request ACI', '1', '423', 'A/S', 'This field identifies if a transaction\nrequested CPS qualification when\nit was sent by the merchant.\nRefer to Authorization\nCharacteristics Indicators for\npossible values.'), ('51', 'Return ACI', '1', '424', 'A/S', 'This field identifies the response to\nthe ACI Request.\nRefer to Authorization\nCharacteristics Indicators for\npossible values.'), ('52', 'Validation Code', '4', '425-428', 'A/N', 'This field identifies a Visa\ncalculated code in the\nauthorization message to ensure\nthat key fields match their\nrespective fields in the Visa BASE\nII clearing message.\nFor Discover and PayPal\ntransactions, the field contains the\nTransaction Data Condition Code\nutilizing the first 2 bytes of the\nfield.'), ('53', 'Product Type\nIdentification', '2', '429-430', 'N', 'Refer to Card Product Codes for a\nlist of values.'), ('54', 'Transaction\nSource Flag', '3', '431-433', 'A/N', 'This field identifies the Telecom\nprovider for authorizations handled\nthrough TSYS Acquiring Solutions.'), ('55', 'VAR Track ID', '10', '434-443', 'A/N', 'This field identifies the Developer\nID for the transaction.'), ('56', 'Vendor ID', '5', '444-448', 'N', 'This field identifies the Vendor ID\nfor the transaction.'), ('57', 'POS Entry\nMode', '4', '449-452', 'A/N', "This value identifies the method\nused to capture the account\nnumber and expiration from the\ncard and the terminal's PIN\ncapture capability.\nRefer to\n POS Entry Mode Codes\nfor values."), ('58', 'ISA Charge\nIndicator', '1', '453', 'A/N', 'This field indicates whether the\nVisa ISA charge was assessed.'), ('59', 'AMEX\nCardholder\nVerification\nResults', '9', '454-462', 'ANS', 'Bytes 1-5 contain verification\ncodes received from AMEX in the\nauthorization response.\nRefer to Amex Cardholder\nVerification Results for a list of\npossible values.\nBytes 6-9 are reserved and space\nfilled.'), ('60', 'POS Condition\nCode', '2', '463-464', 'A/N', 'This value identifies transaction\nconditions at the point of sale or\npoint of service.\nRefer to POS Condition Codes for\na list of codes.'), ('61', 'Additional Data\nPrivate Request', '20', '465-484', 'A/N', 'Refer to Additional Data Private\nRequest for a list that defines the\nusage code key for all private\nrequests for additional data.'), ('62', 'Additional Data\nPrivate\nResponse', '20', '485-504', 'A/N', 'Values are identical to those in\nAdditional Data Private Request'), ('63', 'Supporting\nInformation', '60', '505-564', 'A/N/S', 'Private use field with the following\nusages:\nUsage\nNotes\n1\nReserved for future\nuse\n2\nReserved for future\nuse\n3\nReserved for future\nuse\n4\nReserved for future\nuse\n5\nReserved for future\nuse\n7\nReserved for future\nuse'), ('64', 'Duration', '2', '565-566', 'A/N', 'This field identifies the number of\ndays (from 01 through 99)\nanticipated for the auto rental or\nhotel stay.'), ('65', 'Market Specific\nData Indicator', '1', '567', 'A/N', 'This field identifies the industry for\nwhich market specific data has\nbeen provided.\nPossible values:\nCode\nDefinition\nA\nAuto Rental\nB\nBill Payment\nE\ncCommerce\nTransaction\nAggregation\nH\nHotel\nJ\nB2B Invoice\nPayments\nM\nHealthcare\nN\nFailed CPS Market\nData Edit\nT\nTransit'), ('66', 'Cash Back\nAmount', '12', '568-579', 'N', 'This field identifies the cash back\namount.'), ('67', 'Cardholder\nBilling\nConversion Rate', '9', '580-588', 'N', 'This field identifies a calculated\nvalue that represents a factor that\nmay be applied to the transaction\namount to obtain the cardholder\nbilling amount.'), ('68', 'Cardholder\nBilling Currency\nCode', '3', '589-591', 'A/N', 'This field contains a three-digit\ncode identifying the currency used\nby the Issuer to bill the\ncardholder�s account.\nRefer to \nCurrency Codes for a\nlist of currency codes.'), ('69', 'Request\nAdditional\nAmount', '20', '592-611', 'A/N', 'This field identifies account\nbalance information for ATM\nbalance inquiries, cash\ndisbursements, or available credit\nbalance inquiries.\nThe following is the field layout:\nPosition\nByte\nData\nValue\n \n1\nLength\n1-2\n23\nAccount\nType\n3-4\n4-5\nAmount\nType\n5-7\n6-8\nCurrency\nCode\n8\n9\nAmount\nSign\n9-20\n10-20\nAmount'), ('70', 'Mastercard\nAssigned ID', '6', '612-617', 'A/N', 'This value in this field is assigned\nby Mastercard to identify\nmerchants participating in various\nprograms or for data integrity\npurposes.'), ('71', 'Mastercard IIAS\nIndicator', '1', '618', 'N', 'Inventory Information Approval\nSystem Indicator\n0 - Merchant terminal did\nnot verify the purchased\nitems against an IIAS\n1 - Merchant terminal\nverified the purchase items\nagainst an IIAS\n2 - Merchant claims\nexemption from IIAS based\non the 90 percent rule'), ('72', 'Response\nAdditional\nAmount', '20', '619-638', 'A/N', 'This value identifies the response\ninformation on ATM balance\ninquiries, cash disbursements, or\navailable credit balance inquiries.\nRefer to Field 69 Description\n(above) for field layout.'), ('73', 'Replacement\nAmounts', '12', '639-650', 'A/N', 'This value identifies the corrected\namount of a transaction if a partial\nreversal was completed.'), ('74', 'X\nID', '40', '651-690', 'A/N', 'This field identifies the unique\nVSEC transaction ID generated by\nthe merchant server to identify the\ntransaction.'), ('75', 'UCAF Collection\nIndicator', '1', '691', 'A/N', 'This field indicates whether\nMastercard Universal Cardholder\nAuthentication Data was included\nin the transaction message.\nValid values:\nValue\nDescription\n0\nUCAF data\ncollection is not\nsupported by the\nmerchant or a\nSecureCode\nmerchant chose not\nto undertake\nSecureCode on this\ntransaction\n1\nUCAF data\ncollection is\nsupported by the\nmerchant and UCAF\ndata was present\nand contained an\nattempted AAV for\nMastercard\nSecureCode\n2\nUCAF data\ncollection is\nsupported by the\nmerchant and UCAF\ndata was present\nand contained a\nfully authenticated\nAAV\n5\nIssuer Risk-Based\nDecisioning\n6\nMerchant Risk-\nBased Decisioning\n7\nPartial shipment,\nincremental, or\nrecurring payment'), ('76', 'Transaction\nCurrency Code', '3', '692-694', 'A/N', 'This field identifies a three-\ncharacter code used to define the\ncurrency of the transaction. It is\nalso used to determine the number\nof decimal places for ISO fields 4,\n61.1 and 95.1.\nRefer to \nCurrency Codes for a\nlist of currency codes.'), ('77', 'Gateway\nCurrency Code', '3', '695-697', 'A/N', 'This field identifies a three-\ncharacter code used to define the\ncurrency code of the gateway.\nRefer to \nCurrency Codes for a\nlist of currency codes.'), ('78', 'Gateway\nCountry Code', '3', '698-700', 'A/N', 'This field identifies the country\ncode of the gateway that\nprocessed the transaction.'), ('79', 'Receiving\nInstitution\nCountry Code', '3', '701-733', 'A/N', 'This field identifies the country\nwhere the Receiving Institution is\nlocated.'), ('80', 'Sharing Group', '30', '704-733', 'A/N', 'This field specifies the PIN Debit\nnetwork access priority.\nRefer to Network ID and Sharing\nGroup Codes list of codes.'), ('81', 'GIV', '1', '734', 'A/N', 'This field identifies the Gross\nInterchange Value and is set by\nVISA.\nIf the flag is @, the transaction\nhas financial impact and is\nincluded in the appropriate\nsettlement accumulation during\nprocessing of the request/\nresponse or advice/advice-\nresponse message pair.\nIf flag is blank, the transaction is\nineligible for settlement\nprocessing.'), ('82', 'Reimbursement\nAttribute', '1', '735', 'A/N/S', 'This field identifies a code that\nrepresents the applicable\ninterchange reimbursement fee for\na purchase transaction.'), ('83', 'Receiving\nInstitution ID\nCode', '11', '736-746', 'A/N', 'This field identifies a message\nrouting code that identifies the\ninstitution that should receive a\nrequest or advice.'), ('84', 'Network ID', '4', '747-750', 'N', 'For PIN Debit, this identifies the\ndebit network that processed the\ntransaction. This field may be\npopulated for other transaction\ntypes, such as Visa non-PIN debit\nauthorizations.\nNote: See Network ID and Sharing\nGroup Codes for a list of valid\nvalues.'), ('85', 'Transaction data 12', '', '751-762', 'A/N', 'G\nThis field contains values\nextracted from the second\ngeneration request messages. The\nlayout varies depending on the\nFormat Identifier in the first\nposition of the field.\nen2 Position\nSGMF Position\nAPEX XML Position'), ('86', 'Transaction Fee\nAmount', '9', '763-771', 'A/N', 'This field identifies a destination\nassessed PIN POS and credit\ntransaction surcharge fee in the\ntransaction amount currency for\ninformation only.'), ('87', 'Prestigious\nProperty\nIndicator', '1', '772', 'A', 'This field identifies an indicator\nused by CPS Acquirers in the\nVISA USA Prestigious Lodging\nProgram to identify a property floor\nlimit.\nValid values:\nCode\nDefinition\nD\nPrestigious property\nwith US $500 limit\nB\nPrestigious property\nwith US $1000 limit\nS\nPrestigious property\nwith US $1500 limit'), ('88', 'Pre Auth Time\nLimit', '4', '773-776', 'A/N', 'This value indicates the period that\nfunds will be held for a pre-\nauthorization transaction before\nthe completion transaction is\nfinished. This field only applies to\npre-authorization and completion\ntransactions; otherwise, it will be\nomitted.'), ('89', 'Forwarding\nInstitution\nCountry Code', '3', '777-779', 'A/N', 'This field identifies the country of\nthe forwarding institution.'), ('90', 'Dial Pay\nAuthorization\nCall Type', '2', '780-781', 'A/N', 'This field specifies the type of Dial-\nPay authorization that was\nprocessed.\nTSYS Acquiring Solutions uses\nthis value to segregate and\naccumulate Dial-Pay\nauthorizations for merchant billing\npurposes.\nValid values:\nCode\nDescription\nBH\nBatch History\nBlank\nNot a Dial-Pay\nAuthorization\nBR\nBatch Review\nBT\nBatch Totals\nCR\nCredit\nDC\nDropped Call\nLT\nBatch Find\nIV\nIVR\nOF\nOffline\nOT\nOther\nRF\nReferral\nVC\nVoice\nVD\nVoid'), ('91', 'Digital Entity\nIdentifier', '5', '782-786', 'A/N', 'This value is a unique identifier\nassigned by Visa at the time of\nauthorization to identify a\ntransaction that originates from\nVisa Checkout.'), ('92', 'Reserved', '12', '787-798', 'HEX', 'Internal use only'), ('93', 'Reversal\nRequest Code', '2', '799-800', 'A/N', 'This value is a code that may be\npresent in the reversal request for\na Mastercard transaction to signify\nthe reason for a reversal.'), ('94', 'Additional POS\nInformation Text', '12', '801-812', 'A/N', "R\nThis value identifies the terminal's\ncapability to read account\nnumbers and expiration dates\nelectronically.\nefer to \nAdditional POS\nInformation Position Values for\nmore details."), ('95', 'Endpoint Code', '1', '813', 'A/N', 'The value of this field is privately\nused by TSYS Acquiring\nSolutions.\nValid values:\nEndpoint\nCode\nAmerican Express A\nDiscover\nD\nCiti Bank\nC\nMastercard\nM\nNot Routed\nNull\nStored Value\nS\nSystems\nFifth Third Bank\nF\nTSYS Issuing TS2\nT\nValueLink\nY\nVisa\nV'), ('96', 'Mapped Account\nExpiration Date', '4', '814-817', 'A/N', 'This value represents the\nexpiration date of the Mapped\nPaypass card.'), ('97', 'POS Data Code', '12', '818-829', 'A/N', 'S\n D\nThis field consists of 12 subfields\nthat indicate the condition or state\nof the terminal at the time of the\ntransaction. The fields come in two\ntypes, static or dynamic.\ntatic Fields:\nStatic fields have the same value\nfor every transaction. They do not\ntypically change once the software\nand hardware are considered\ntogether in the environment in\nwhich they are deployed.\nynamic Values:\nDynamic fields can change based\non the transaction scenario.\nRefer to Mastercard POS Data\nCode for a list of codes.\nRefer to Amex POS Data Code for\na list of codes.'), ('98', 'POS\nEnvironment\nIndicator', '1', '830', 'A/N', 'This Visa only field contains an\nindicator for the following types of\ntransactions:\nC - Credential on File\nI - Installment Payment\nR - Recurring Payment'), ('99', 'Reserved', '42', '831-872', 'A/N', 'Reserved'), ('100', 'Local\nTransaction Date', '4', '873-876', 'N', 'MMDD\nThis is the month and day the\ncardholder originated the\ntransaction. For recurring\npayments, the date is the\ncardholder requested payment\ndate.'), ('101', 'Local\nTransaction\nT\nime', '6', '877-882', 'N', 'This field identifies six-digits in the\nHHMMSS format indicating the\nexact time a transaction is\nperformed.'), ('102', 'Fee Program\nIndicator', '3', '883-885', 'A/N', 'This field identifies the fee program\nindicator; it is used in assessing\nthe fee amount applied to the\ntransaction.'), ('103', 'Visa DCC\nIndicator', '1', '886', 'A/N', 'Visa Dynamic Currency\nConversion Indicator\nPossible values:\n1 - DCC was performed\nSpace - DCC was not\nperformed'), ('104', 'Encryption\nIndicator', '1', '887', 'A/N', 'Encryption Indicator\nPossible values:\nV - Voltage encrypted\nP - P2PE encrypted\nN - NESA encrypted\nSpace - Not an encrypted\ntransaction'), ('105', 'TSYS Token\nIndicator', '1', '888', 'A/N', 'TSYS Token Indicator\nPossible values:\nY - Transaction used\nTokens\nN - Transaction did not use\nTokens'), ('106', 'Account Funding\nSource', '1', '889', 'A/N', 'Account Funding Source\nPossible values:\nC - Credit\nD - Debit\nH - Charge\nP - Prepaid\nR - Deferred Debit\nSpace - N/A'), ('107', 'Issuing BIN\nLook-Up', '1', '890', 'A/N', 'This field indicates an Issuing BIN\nlook up was performed to\ndetermine whether the transaction\nwas credit or debit.\nPossible values:\nY - Look-Up Performed\nN - No Look-Up'), ('108', 'Fallback\nIndicator', '1', '891', 'A/N', 'This field identifies that a\ntransaction initiated with a chip\ncard at a chip card capable\nterminal failed, resulting in a\nfallback to a mag-stripe entry\nmode.\nPossible values:\nT - Technical Fallback\nE - Empty Candidate List\nFallback\nSpace - No Fallback'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"acquirerBIN": None,
		"exitBIN": None,
		"agent": None,
		"chain": None,
		"eConnectionsMerchantNumber": None,
		"storeNumber": None,
		"terminalNumber4": None,
		"cardAcceptorID": None,
		"merchantName": None,
		"cardAcceptorCity": None,
		"cardAcceptorState": None,
		"cardAcceptorCountryCode": None,
		"countryCodePANExtended": None,
		"nationalPOSGeographicData": None,
		"mCCCode": None,
		"merchantABANumber": None,
		"cardAcceptorSettlementAgent": None,
		"iSOSourceStationID": None,
		"acquirerBusinessID": None,
		"acquirerCountryCode": None,
		"cardType": None,
		"primaryAccountNumber": None,
		"eXTPAN": None,
		"accountID1": None,
		"cardexpirationDate": None,
		"issuingInstitutionStationID": None,
		"issuingInstitutionIDCode": None,
		"julianDay": None,
		"transactionDateTime": None,
		"settlementDate": None,
		"loadDateTime": None,
		"messageType": None,
		"processingCode": None,
		"accessMethod": None,
		"aSCIIBillCode": None,
		"transactionIdentifier": None,
		"retrievalReferenceNumber": None,
		"systemsTraceAuditNumber": None,
		"authorizedAmount": None,
		"cardholderBillingAmount": None,
		"approvalCode": None,
		"authorizationResponse": None,
		"internalErrorCode": None,
		"iSORejectCode4": None,
		"cVV2CVC2CIDResponseType": None,
		"cVV2CVC2CIDPresenceIndicator": None,
		"messageReasonCode": None,
		"additionalResponseData": None,
		"requestACI": None,
		"returnACI": None,
		"validationCode": None,
		"productTypeIdentification": None,
		"transactionSourceFlag": None,
		"vARTrackID": None,
		"vendorID": None,
		"pOSEntryMode": None,
		"iSAChargeIndicator": None,
		"aMEXCardholderVerificationResults": None,
		"pOSConditionCode": None,
		"additionalDataPrivateRequest": None,
		"additionalDataPrivateResponse": None,
		"supportingInformation": None,
		"duration": None,
		"marketSpecificDataIndicator": None,
		"cashBackAmount": None,
		"cardholderBillingConversionRate": None,
		"cardholderBillingCurrencyCode": None,
		"requestAdditionalAmount": None,
		"mastercardAssignedID": None,
		"mastercardIIASIndicator": None,
		"responseAdditionalAmount": None,
		"replacementAmounts": None,
		"xID": None,
		"uCAFCollectionIndicator": None,
		"transactionCurrencyCode": None,
		"gatewayCurrencyCode": None,
		"gatewayCountryCode": None,
		"receivingInstitutionCountryCode": None,
		"sharingGroup": None,
		"gIV": None,
		"reimbursementAttribute": None,
		"receivingInstitutionIDCode": None,
		"networkID": None,
		"transactiondata12": None,
		"transactionFeeAmount": None,
		"prestigiousPropertyIndicator": None,
		"preAuthTimeLimit": None,
		"forwardingInstitutionCountryCode": None,
		"dialPayAuthorizationCallType": None,
		"digitalEntityIdentifier": None,
		"reserved91": None,
		"reversalRequestCode": None,
		"additionalPOSInformationText": None,
		"endpointCode": None,
		"mappedAccountExpirationDate": None,
		"pOSDataCode": None,
		"pOSEnvironmentIndicator": None,
		"reserved98": None,
		"localTransactionDate": None,
		"localTransactionTime": None,
		"feeProgramIndicator": None,
		"visaDCCIndicator": None,
		"encryptionIndicator": None,
		"tSYSTokenIndicator": None,
		"accountFundingSource": None,
		"issuingBINLookUp": None,
		"fallbackIndicator": None
                }

    LENGTH = 900

    def __init__(self,f):
        self.recordType, self.acquirerBIN, self.exitBIN, self.agent, self.chain, self.eConnectionsMerchantNumber, self.storeNumber, self.terminalNumber4, self.cardAcceptorID, self.merchantName, self.cardAcceptorCity, self.cardAcceptorState, self.cardAcceptorCountryCode, self.countryCodePANExtended, self.nationalPOSGeographicData, self.mCCCode, self.merchantABANumber, self.cardAcceptorSettlementAgent, self.iSOSourceStationID, self.acquirerBusinessID, self.acquirerCountryCode, self.cardType, self.primaryAccountNumber, self.eXTPAN, self.accountID1, self.cardexpirationDate, self.issuingInstitutionStationID, self.issuingInstitutionIDCode, self.julianDay, self.transactionDateTime, self.settlementDate, self.loadDateTime, self.messageType, self.processingCode, self.accessMethod, self.aSCIIBillCode, self.transactionIdentifier, self.retrievalReferenceNumber, self.systemsTraceAuditNumber, self.authorizedAmount, self.cardholderBillingAmount, self.approvalCode, self.authorizationResponse, self.internalErrorCode, self.iSORejectCode4, self.cVV2CVC2CIDResponseType, self.cVV2CVC2CIDPresenceIndicator, self.messageReasonCode, self.additionalResponseData, self.requestACI, self.returnACI, self.validationCode, self.productTypeIdentification, self.transactionSourceFlag, self.vARTrackID, self.vendorID, self.pOSEntryMode, self.iSAChargeIndicator, self.aMEXCardholderVerificationResults, self.pOSConditionCode, self.additionalDataPrivateRequest, self.additionalDataPrivateResponse, self.supportingInformation, self.duration, self.marketSpecificDataIndicator, self.cashBackAmount, self.cardholderBillingConversionRate, self.cardholderBillingCurrencyCode, self.requestAdditionalAmount, self.mastercardAssignedID, self.mastercardIIASIndicator, self.responseAdditionalAmount, self.replacementAmounts, self.xID, self.uCAFCollectionIndicator, self.transactionCurrencyCode, self.gatewayCurrencyCode, self.gatewayCountryCode, self.receivingInstitutionCountryCode, self.sharingGroup, self.gIV, self.reimbursementAttribute, self.receivingInstitutionIDCode, self.networkID, self.transactiondata12, self.transactionFeeAmount, self.prestigiousPropertyIndicator, self.preAuthTimeLimit, self.forwardingInstitutionCountryCode, self.dialPayAuthorizationCallType, self.digitalEntityIdentifier, self.reserved91, self.reversalRequestCode, self.additionalPOSInformationText, self.endpointCode, self.mappedAccountExpirationDate, self.pOSDataCode, self.pOSEnvironmentIndicator, self.reserved98, self.localTransactionDate, self.localTransactionTime, self.feeProgramIndicator, self.visaDCCIndicator, self.encryptionIndicator, self.tSYSTokenIndicator, self.accountFundingSource, self.issuingBINLookUp, self.fallbackIndicator = (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        self.data = f.read(TransactionDetailRecord.LENGTH)
        super(TransactionDetailRecord, self).__init__()
        
class HostCaptureAdjustmentTransactionDetailRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates that this\nrecord is the Transaction Detail\nHeader-TD02.'), ('2', 'Acquirer BIN', '6', '5-10', 'A/N', 'This field identifies the financial\ninstitution acting as the Acquirer\nof this customer transaction.'), ('3', 'EXT BIN', '5', '11-15', 'A/N', 'This field identifies the extra data\nthat is received from the ISO\nmessage for the BIN.'), ('4', 'Agent', '6', '16-21', 'A/N', 'This field identifies the agent\nfilter, if defined, from the report\nregistration. The agent is a six\ncharacter value assigned by the\nmerchant�s bank or processor.\nPossible values:\n6 character agent value\nNA � then left justified,\nspace filled\nSpace filled'), ('5', 'Chain', '6', '22-27', 'A/N', 'This field identifies the chain\nfilter, if defined, from the report\nregistration. The chain is a six-\ncharacter value assigned by the\nmerchant�s bank or processor.\nPossible values:\n6 character agent value\nNA � then left justified,\nspace filled\nSpace filled'), ('6', 'Merchant\nNumber', '15', '28-42', 'A/N', 'This field identifies the merchant\nnumber that is displayed in the e-\nConnections Authorization and\nCapture module.'), ('7', 'Store Number', '4', '43-46', 'A/N', 'This field identifies the store\nnumber.'), ('8', 'Terminal\nNumber', '4', '47-50', 'A/N', 'This field identifies the terminal\nnumber.'), ('9', 'Retrieval\nReference\nNumber', '12', '51-62', 'N', 'This field contains a number that\nis used with other key data\nelements to identify and track all\nmessages related to a given\ncardholder transaction. This is\nthe RRN of the original\nauthorization.'), ('10', 'Transaction\nType', '3', '63-65', 'N', 'This field identifies the type of\nadjustment transaction.\nPossible values:\n101 adjustment\n102 tip adjustment\n103 void'), ('11', 'Transaction\nDate & Time', '12', '66-77', 'N', 'This field identifies the Local\nTransaction Date and Local\nTransaction Time fields.\nMMDDYYHHMMSS'), ('12', 'Access Method', '2', '78-79', 'A/N', 'This field identifies the\nconnectivity method utilized to\ntransmit the transaction. This\nfield maps directly to the ASCII\nLine Type.'), ('13', 'ASCII Bill Code', '1', '80', 'A/N', 'This field identifies the billing\ndescriptor. It may contain\nadditional billing or reporting\ninformation.'), ('14', 'Application Type 1', '', '81', 'A/N', 'This field describes whether the\ntransaction was transmitted via\n�0� Single Transaction, �2� multi-\ntransaction, or �4� interleaved\ntransaction.'), ('15', 'Card Type', '1', '82', 'A/N', 'This field identifies the card plan\ntype of the original authorization.\nSee field 22 in TD01 -\nTransaction Detail Record for\ndefinitions.'), ('16', 'Network ID', '4', '83-86', 'N', 'For PIN Debit, this identifies the\ndebit network that processed the\ntransaction. This field may be\npopulated for other transaction\ntypes as well. For example, Visa\nnon-PIN debit authorizations.'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"acquirerBIN": None,
		"eXTBIN": None,
		"agent": None,
		"chain": None,
		"merchantNumber": None,
		"storeNumber": None,
		"terminalNumber": None,
		"retrievalReferenceNumber": None,
		"transactionType": None,
		"transactionDateTime": None,
		"accessMethod": None,
		"aSCIIBillCode": None,
		"applicationType1": None,
		"cardType": None,
		"networkID": None
                }

    LENGTH = 120

    def __init__(self,f):
        self.recordType, self.acquirerBIN, self.eXTBIN, self.agent, self.chain, self.merchantNumber, self.storeNumber, self.terminalNumber, self.retrievalReferenceNumber, self.transactionType, self.transactionDateTime, self.accessMethod, self.aSCIIBillCode, self.applicationType1, self.cardType, self.networkID = (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        self.data = f.read(HostCaptureAdjustmentTransactionDetailRecord.LENGTH)
        super(HostCaptureAdjustmentTransactionDetailRecord, self).__init__()
        
class HostCaptureBatchInquiryTransactionDetailRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates that this\nrecord is the Transaction\nDetail Header-TD03.'), ('2', 'Acquirer BIN', '6', '5-10', 'A/N', 'This field identifies the\nfinancial institution acting as\nthe Acquirer of this customer\ntransaction.'), ('3', 'EXT BIN', '5', '11-15', 'A/N', 'This field identifies the extra\ndata that is received from the\nISO message for the BIN.'), ('4', 'Agent', '6', '16-21', 'A/N', 'This field identifies the agent\nfilter, if defined, from the report\nregistration. The agent is a six\ncharacter value assigned by\nthe merchant�s bank or\nprocessor.\nPossible values:\n6 character agent value\nNA � then left justified,\nspace filled\nSpace filled'), ('5', 'Chain', '6', '22-27', 'A/N', 'This field identifies the chain\nfilter, if defined, from the report\nregistration. The chain is a six\ncharacter value assigned by\nthe merchant�s bank or\nprocessor.\nPossible values:\n6 character agent value\nNA � then left justified,\nspace filled\nSpace filled'), ('6', 'Merchant\nNumber', '15', '28-42', 'A/N', 'This field identifies the\nmerchant number that is\ndisplayed in the e-\nConnections Authorization\nand Capture module.'), ('7', 'Store Number', '4', '43-46', 'A/N', 'This field identifies the store\nnumber.'), ('8', 'Terminal\nNumber', '4', '47-50', 'A/N', 'This field identifies the\nterminal number.'), ('9', 'Transaction\nType', '3', '51-53', 'N', 'This field identifies the type of\nadjustment transaction:\nPossible values:\n201 Manual Batch\nClose\n202 Batch Summary\nInquiry\n203 Batch Detail\nInquiry\n204 Transaction Detail\nInquiry\n205 Low-Buffer Batch\nSummary Inquiry'), ('10', 'Transaction\nDate & Time', '12', '54-65', 'N', 'This field identifies the Local\nTransaction Date and Local\nTransaction Time fields.\nMMDDYYHHMMSS'), ('11', 'Access Method 2', '', '66-67', 'A/N', 'This field identifies the\nconnectivity method utilized to\ntransmit the transaction. This\nfield maps directly to the\nASCII Line Type.'), ('12', 'ASCII Bill Code 1', '', '68', 'A/N', 'This field identifies the billing\ndescriptor. It may contain\nadditional billing or reporting\ninformation.'), ('13', 'Application\nType', '1', '69', 'A/N', 'This field describes whether\nthe transaction was\ntransmitted via �0� Single\nTransaction, �2� multi-\ntransaction, or �4� interleaved\ntransaction.'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"acquirerBIN": None,
		"eXTBIN": None,
		"agent": None,
		"chain": None,
		"merchantNumber": None,
		"storeNumber": None,
		"terminalNumber": None,
		"transactionType": None,
		"transactionDateTime": None,
		"accessMethod2": None,
		"aSCIIBillCode1": None,
		"applicationType": None
                }

    LENGTH = 100

    def __init__(self,f):
        self.recordType, self.acquirerBIN, self.eXTBIN, self.agent, self.chain, self.merchantNumber, self.storeNumber, self.terminalNumber, self.transactionType, self.transactionDateTime, self.accessMethod2, self.aSCIIBillCode1, self.applicationType = (None, None, None, None, None, None, None, None, None, None, None, None, None)
        self.data = f.read(HostCaptureBatchInquiryTransactionDetailRecord.LENGTH)
        super(HostCaptureBatchInquiryTransactionDetailRecord, self).__init__()
        
class TransactionDetailExtensionRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates that this record\nis the Transaction Detail\nExtension Record.\nValue = TD11'), ('2', 'Extension Record 8', '', '5-12', 'A/N', 'This field indicates the record that\nfollows the TD11 Record.\nPossible values:\nSpace - no record follows\nEX01 - Discover/PayPal\nextension record follows\nEX02 - Mastercard\nextension record follows\nEX03 - Additional detail\ndata extension record\nfollows\nEX04 - Merchant Data\nextension record follows'), ('3', 'Merchant\nConsent Indicator', '1', '13', 'A/N', 'This field indicates the value of the\nmerchant consent indicator at the\ntime a transaction is processed.It\nis specific to merchants\nprocessing transactions in\nCanada, and indicates if the\nmerchant has or has not\nconsented to the Canadian Code\nof Conduct. Merchants must\ndeclare a value for both card\npresent and card not present\ntransactions.\nPossible values:\nCard Present\n1 - Merchant consented\n2 - Merchant did not\nconsent\nCard Not Present\n3 - Merchant consented\n4 - Merchant did not\nconsent'), ('4', 'Goods Sold\nProduct Code', '4', '14-17', 'A/N', 'This field is used by Card Present\nmerchants to provide an Amex\ndefined Goods Sold value.\nValid values:\n1000 - Gift Card\nSpace fill'), ('5', 'Card Brand\nToken Assurance\nLevel', '2', '18-19', 'A/N', 'Defined by the token service\nprovider, this Visa, Mastercard or\nDiscover value indicates the\nassigned confidence level of the\ntoken-to-PAN/cardholder binding.'), ('6', 'Account Range\nStatus', '1', '20', 'A/N', 'This Visa value is used by the\nacquirer or processor; it indicates\nthe status of the account.\nValid values:\nSpace\nR - Regulated\nN - Non-Regulated'), ('7', 'Seller ID', '20', '21-40', 'A/N', 'This American Express value is\nthe identifier assigned by the\nPayment Service\nProvider/Aggregator or OptBlue\nparticipant.'), ('8', 'Card Brand\nToken Requestor\nID', '11', '41-51', 'A/N', 'This field contains eleven digits\nthat uniquely identify the pairing of\nthe token requestor with the token\ndomain. It is assigned by the\ntoken service provider and is\nunique within the token vault.'), ('9', 'Industry SE\nNumber', '10', '52-61', 'A/N', 'This American Express value\nrepresents the identifier of the\nService Establishment/Merchant.'), ('10', 'Seller DBA', '30', '62-91', 'A/N', 'This is the merchant�s �Doing\nBusiness As� name. It is the\ncommon name of the business.'), ('11', 'Payment\nFacilitator\nIdentifier', '11', '92-102', 'A/N', 'Mastercard assigns this value\nduring registration via Mastercard\nConnect for the Service Provider\ndesignated as a �Payment\nFacilitator�.'), ('12', 'ISO Identifier', '11', '103-113', 'A/N', 'Mastercard assigns this value\nduring registration via Mastercard\nConnect for the Service Provider\ndesignated as an �Independent\nSales Organization�.'), ('13', 'Sub-Merchant\nIdentifier', '15', '114-128', 'A/N', 'The Payment Facilitator or the\nAcquirer assigns this Mastercard\nvalue.'), ('14', 'Expanded Billing\nClass', '2', '129-130', 'A/N', 'This field indicates the ingress\nconnectivity method between a\nclient and its respective\ntransaction processing gateway.\nThis field is used for\nmerchant/service specific billing.\nPossible value:\nV1-V9 [Port Options 1-9]'), ('15', 'Issuer Country\nCode', '3', '131-133', 'A/N', 'This field is populated for Visa and\nMastercard.'), ('16', 'Service Code', '3', '134-136', 'N', 'This field is a service code from\ntrack data.'), ('17', 'Payment\nAccount\nReference (PAR)', '35', '137-171', 'AN', "PAR is a value assigned by the\nBIN Controller, which is defined as\neither an issuer or card brand.\nThis field is directly associated\nwith the cardholder's account."), ('18', 'Business\nApplication\nIdentifier', '2', '172-173', 'A/N', 'Business Application Identifier\nThis field identifies industry-\nspecific business practices\npertaining to Account Funding\nTransactions (AFT).\nValid Value:\nWT � Wallet Transfer'), ('19', 'Endpoint POS\nData Code', '13', '174-186', 'A/N', 'This field contains data indicating\nthe condition or state of the\nterminal at the time the\nauthorization request is sent to\nthe various endpoints. Each\nendpoint has different subfields.\nThe fields come in two types,\nstatic or dynamic.\nStatic Fields:\nStatic fields have the same value\nfor every transaction. They do not\ntypically change once the\nsoftware and hardware are\nconsidered together in the\nenvironment in which they are\ndeployed.\nDynamic Values:\nDynamic fields can change based\non the transaction scenario.\nRefer to Amex POS Data Code for\na list of codes.\nRefer to Discover/PayPal POS\nData Code for a list of codes.\nRefer to Mastercard POS Data\nCode for a list of codes.'), ('20', 'Reserved', '134', '187-320', 'A/N', 'Reserved'), ('21', 'TSYS', '6', '321-326', 'A/N', 'TSYS Internal Use Only'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"extensionRecord8": None,
		"merchantConsentIndicator": None,
		"goodsSoldProductCode": None,
		"cardBrandTokenAssuranceLevel": None,
		"accountRangeStatus": None,
		"sellerID": None,
		"cardBrandTokenRequestorID": None,
		"industrySENumber": None,
		"sellerDBA": None,
		"paymentFacilitatorIdentifier": None,
		"iSOIdentifier": None,
		"subMerchantIdentifier": None,
		"expandedBillingClass": None,
		"issuerCountryCode": None,
		"serviceCode": None,
		"paymentAccountReference": None,
		"businessApplicationIdentifier": None,
		"endpointPOSDataCode": None,
		"reserved19": None,
		"tSYS": None
                }

    LENGTH = 200

    def __init__(self,f):
        self.recordType, self.extensionRecord8, self.merchantConsentIndicator, self.goodsSoldProductCode, self.cardBrandTokenAssuranceLevel, self.accountRangeStatus, self.sellerID, self.cardBrandTokenRequestorID, self.industrySENumber, self.sellerDBA, self.paymentFacilitatorIdentifier, self.iSOIdentifier, self.subMerchantIdentifier, self.expandedBillingClass, self.issuerCountryCode, self.serviceCode, self.paymentAccountReference, self.businessApplicationIdentifier, self.endpointPOSDataCode, self.reserved19, self.tSYS = (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        self.data = f.read(TransactionDetailExtensionRecord.LENGTH)
        super(TransactionDetailExtensionRecord, self).__init__()
        
class TransmissionHeaderRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates that this record is the\nTransmission Header.\nValue = TH01'), ('2', 'Version Number', '5', '5-9', 'A/N', 'This field identifies the Report Version\nNumber.\nExample: 01.00'), ('3', 'Destination ID', '30', '10-39', 'A/N', 'This field identifies the destination client ID\nfrom the report registration.'), ('4', 'File Type', '10', '40-49', 'A/N', 'This field identifies the file type being sent.\nValue = ADF'), ('5', 'File Frequency', '1', '50', 'A/N', 'This field identifies the frequency in which\nthe file is sent.\nExample:\nB = Bi-hourly\nD = Daily\nW = Weekly'), ('6', 'Processing Year', '4', '51-54', 'N', 'This field identifies the year in which the file\nwas created.\nExample: YYYY'), ('7', 'Processing Month', '2', '55-56', 'N', 'This field identifies the month in which the\nfile was created.\nExample: MM - month number, from 01 to\n12'), ('8', 'Processing Week', '1', '57', 'N', 'This field identifies the week in which the file\nwas created. The valid value for a week\ncorresponds to the specific week within a\nmonth, and can be a 1, 2, 3, or 4. This field\nwill only be used if it is a weekly file.\nValue\nDefinition\n1\nWeek 1 (day 1 - 7)\n2\nWeek 2 (day 8 - 15)\n3\nWeek 3 (day 16 - 22)\n4\nWeek 4 (day 23 - end of month)\nIf it is not a weekly file, then this field will be\nleft blank.'), ('9', 'Processing Day', '2', '58-59', 'N', 'Reserved for TSYS Acquiring Solutions use\nonly'), ('10', 'Processing End\nHour', '2', '60-61', 'N', 'This value, formatted as HH, identifies the\nhour in which the file was created if the file\nis bi-hourly. If it is not a bi-hourly file, then\nthis field will be left blank.\nExample:\nThis uses a 24-hour clock based on\nGreenwich Mean Time (GMT)'), ('11', 'File Reference ID', '20', '62-81', 'A/N', 'Reserved for TSYS Acquiring Solutions use\nonly'), ('12', 'File Creation Date &\nT\nime', '19', '82-100', 'A/N', 'This field identifies the date and time (GMT)\nthe file was created.\nExample:\nYYYY-MM-DD HH:MM:SS (using a 24-hour\nclock)'), ('13', 'Reserved (internal)', '19', '101-119', 'A/N', 'TSYS Acquiring Solutions use only'), ('14', 'Reserved (internal)', '19', '120-138', 'A/N', 'TSYS Acquiring Solutions use only'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"versionNumber": None,
		"destinationID": None,
		"fileType": None,
		"fileFrequency": None,
		"processingYear": None,
		"processingMonth": None,
		"processingWeek": None,
		"processingDay": None,
		"processingEndHour": None,
		"fileReferenceID": None,
		"fileCreationDateTime": None,
		"reserved12": None,
		"reserved13": None
                }

    LENGTH = 900

    def __init__(self,f):
        self.recordType, self.versionNumber, self.destinationID, self.fileType, self.fileFrequency, self.processingYear, self.processingMonth, self.processingWeek, self.processingDay, self.processingEndHour, self.fileReferenceID, self.fileCreationDateTime, self.reserved12, self.reserved13 = (None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        self.data = f.read(TransmissionHeaderRecord.LENGTH)
        super(TransmissionHeaderRecord, self).__init__()
        
class TransmissionTrailerRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates that this record is the\nTransmission Trailer.\nValue = TT01'), ('2', 'Version Number', '5', '5-9', 'A/N', 'This field identifies the Report Version\nNumber. Example: 01.00'), ('3', 'Destination ID', '30', '10-39', 'A/N', 'This field identifies the destination client ID\nfrom the report registration.'), ('4', 'File type', '10', '40-49', 'A/N', 'This field identifies the file type being sent.\nValue = ADF'), ('5', 'File Frequency', '1', '50', 'A/N', 'This field identifies the frequency in which the\nfile is sent.\nExample:\nB = Bi-hourly\nD = Daily\nW = Weekly'), ('6', 'Processing Year', '4', '51-54', 'N', 'This field identifies the year the file was\ncreated.\nExample: YYYY'), ('7', 'Processing Month', '2', '55-56', 'N', 'This field identifies the month the file was\ncreated.\nExample: MM - month number, from 01 to 12'), ('8', 'Processing Week', '1', '57', 'N', 'This field identifies the week the file was\ncreated. The valid value for a week\ncorresponds to the specific week within a\nmonth, and can be a 1, 2, 3, or 4. This field\nwill only be used if it is a weekly file.\nValue\nDefinition\n1\nWeek 1 (day 1 - 7)\n2\nWeek 2 (day 8 - 15)\n3\nWeek 3 (day 16 - 22)\n4\nWeek 4 (day 23 - end of month)\nIf it is not a weekly file, then this field will be\nblank.'), ('9', 'Processing Day', '2', '58-59', 'N', 'Reserved for TSYS Acquiring Solutions use\nonly'), ('10', 'Processing End\nHour', '2', '60-61', 'N', 'This field identifies the hour the file was\ncreated if the file is bi-hourly. If it is not a bi-\nhourly file, then this field will be blank.\nExample:\nHH, (using a 24-hour clock). Based on\nGreenwich Mean Time (GMT).'), ('11', 'File Reference ID', '20', '62-81', 'A/N', 'Reserved for TSYS Acquiring Solutions use\nonly'), ('12', 'File Total BIN Count 8', '', '82-89', 'N', 'This field identifies the total number of unique\nBIN(s) located within the file.'), ('13', 'File Total Report\nCount', '8', '90-97', 'N', 'This field identifies the total number of unique\nReport(s) located within the file.'), ('14', 'File Total\nTransaction Count', '12', '98-109', 'N', 'This field identifies the total number of\ntransactions located within the transmission.'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"versionNumber": None,
		"destinationID": None,
		"filetype": None,
		"fileFrequency": None,
		"processingYear": None,
		"processingMonth": None,
		"processingWeek": None,
		"processingDay": None,
		"processingEndHour": None,
		"fileReferenceID": None,
		"fileTotalBINCount8": None,
		"fileTotalReportCount": None,
		"fileTotalTransactionCount": None
                }

    LENGTH = 900

    def __init__(self,f):
        self.recordType, self.versionNumber, self.destinationID, self.filetype, self.fileFrequency, self.processingYear, self.processingMonth, self.processingWeek, self.processingDay, self.processingEndHour, self.fileReferenceID, self.fileTotalBINCount8, self.fileTotalReportCount, self.fileTotalTransactionCount = (None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        self.data = f.read(TransmissionTrailerRecord.LENGTH)
        super(TransmissionTrailerRecord, self).__init__()
        
