NegativeAmounts = {'}': 0, 'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9}
DataTypes = {'A': r'[a-zA-Z]+', 'AN': r'[a-zA-Z0-9 ]+', 'S': r' +', 'N': '\d+', 'PN': r'.{2}'} #NOTE: TSYS may use more than 2 bytes for PN...
UserAbbreviations = {'All': 'All associations and TSYS Acquiring Solutions', 'X': 'American Express®', 'CAPN': 'American Express Card Acceptance Processing Network®', 'D': 'Diners Club®', 'S': 'Discover®', 'E': 'Europay®', 'JCB': 'Japanese Credit Bureau®', 'M': 'MasterCard®', 'P': 'Private label', 'V': 'Visa®', 'V-UK': 'Visa United Kingdom®', 'V-EU': 'Visa European Union®', 'TSYS Acquiring Solutions': 'TSYS Acquiring Solutions'}
NetworkIDs = {'XL': 'Accel®', 'AF': 'Armed Forces Financial Network (AFFN)', 'AL': 'Alert®', 'AV': 'Avail®', 'BM': 'Bankmate®', 'CA': 'Cactus®', 'CS': 'Cash Station®', 'CU': 'Credit Union 24 (CU24)', 'EB': 'EBT® (Electronic Benefits Transfer)', 'EV': 'Evertec', 'EH': 'The Exchange®', 'DB': 'Generic debit', 'GF': 'Gulfnet®', 'HO': 'Honor®', 'IT': 'Instant Teller®', 'IL': 'Interlink®', 'JE': 'Jeanie®', 'MA': 'Mac®', 'ME': 'Maestro®', 'ML': 'Magicline®', 'MS': 'Money Station®', 'MO': 'Most®', 'IM': 'Mpact®', 'NY': 'NYCE®', 'PL': 'Pulse®', 'QU': 'Quest®', 'S': 'Shaam®', 'ST': 'Star (Explore)®', 'TY': 'Tyme®', 'VI': 'Visa®', 'C2': 'Visa Checkcard II®', 'YN': 'Yankee 24®'}

class Record:
    def __init__(self):
        pass


class TransmissionHeader(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe sequence number for the transmission \r\nheader must be 0000001. For more \r\ninformation about sequence numbers, see \r\nSequence numbers on page 55.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nRequired value  9010'),
             ('3', '12-15', '4', 'AN', 'TSYS Acquiring Solutions', 'Transmit Bank Number\r\nThe transmit bank number is assigned by \r\nTSYS Acquiring Solutions.'),
             ('4', '16-19', '4', 'N', 'TSYS Acquiring Solutions', 'User-Assigned Transmission Number\r\nThis number is assigned by the client. It \r\nmust match the value in field 4 of the \r\ntransmission trailer.'),
             ('5', '20-27', '8', 'AN', 'TSYS Acquiring Solutions', 'Transmission Name Identification\r\nAfter the client completes the Transmission \r\nQuestionnaire, TSYS Acquiring Solutions \r\nwill assign the transmission name \r\nidentification for the new transmission. \r\nTSYS Acquiring Solutions will use the value \r\nin this field to verify transmission security.'),
             ('6', '28-39', '12', 'AN', 'TSYS Acquiring Solutions', 'User Security Password\r\nThe User Security Password is assigned by \r\nTSYS Acquiring Solutions and used to \r\nverify transmission security.'),
             ('7', '40-42', '3', 'N', 'TSYS Acquiring Solutions', 'Transmission Date (Julian)\r\nThis field must contain the date the \r\ntransmission is sent to TSYS Acquiring \r\nSolutions. For an explanation of the format, \r\nsee Julian day of the year on page 8.\r\nFormat  DDD'),
             ('8', '43-48', '6', 'N', 'TSYS Acquiring Solutions', 'Transmission Date (Gregorian)\r\nThis field must contain the date the \r\ntransmission is sent to TSYS Acquiring \r\nSolutions.\r\nFormat  MMDDYY'),
             ('9', '49-54', '6', 'AN', 'TSYS Acquiring Solutions', 'Transmission Description Code\r\nThis field must contain spaces or the code \r\nassigned by TSYS Acquiring Solutions when \r\nthe transmission was set up.\r\nThe transmission description identifies the \r\nsource of the transmission on various TSYS \r\nAccounting (TSA) System screens and \r\nreports. If the client did not request a \r\nspecific description when the transmission \r\nwas set up, the default transmission \r\ndescription DAILY TANDEM ENTRY \r\nwill appear.'),
             ('10', '55', '1', 'AN', 'TSYS Acquiring Solutions', 'Pre-Process Flag\r\nThis field is for TSYS Acquiring Solutions \r\nuse only. Clients can use a space in this field.'),
             ('11', '56-59', '4', 'S', 'TSYS Acquiring Solutions', 'Vendor Identifier Expansion\r\nReserved for future use'),
             ('12', '60', '1', 'AN', '', 'Commingled File Processing Flag'),
             ('13', '61-63', '3', '', '', 'Multi-Currency Currency Code\r\nIf the transmission currency type is different \r\nfrom the banks currency type, this field \r\nmust contain the code for the currency type \r\nof the transmission.\r\nNOTEBefore using currency codes not \r\npreviously utilied, please contact your TSYS \r\nAcquiring Solutions Relationship Managers about \r\ntesting the new currency.'),
             ('14', '64-74', '11', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('15', '75-96', '22', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('16', '97', '1', 'S', 'TSYS Acquiring Solutions', 'ECCB Qualification Flag\r\nUse a space in this field.'),
             ('17', '98-100', '3', 'AN', 'TSYS Acquiring Solutions', 'Vendor Identifier\r\nThe vendor identifier is assigned by TSYS \r\nAcquiring Solutions to identify the data \r\ncapture vendor. If there is no vendor, use \r\nspaces in this field.'),
             ('18', '101-108', '8', 'S', 'TSYS Acquiring Solutions', 'Mailbox Transmission Identifier\r\nThis field is for TSYS Acquiring Solutions \r\nuse only. Clients can use a space in this field.'),
             ('19', '109-115', '7', 'S', 'TSYS Acquiring Solutions', 'Mailbox Batch Number\r\nThis field is for TSYS Acquiring Solutions \r\nuse only. Clients can use a space in this field.'),
             ('20', '116-120', '5', 'S', 'TSYS Acquiring Solutions', 'Mailbox Transmission Date\r\nThis field is for TSYS Acquiring Solutions \r\nuse only. Clients can use a space in this field.'),
             ('21', '121-124', '4', 'S', 'TSYS Acquiring Solutions', 'Mailbox Transmission Time\r\nThis field is for TSYS Acquiring Solutions \r\nuse only. Clients can use a space in this field.'),
             ('22', '125-127', '3', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('23', '128', '1', 'AN', 'TSYS Acquiring Solutions', '256-byte Transmission Identifier Flag\r\nThis field indicates whether the \r\ntransmission header and all records \r\nfollowing it are 256 bytes long.\r\nPossible values  \r\nSpace\r\nor N - \r\n128-byte record lengths\r\nY - \r\n256-byte record lengths\r\nNote\r\nEach 256-byte record must be transmitted as \r\ntwo 128-byte records.'),
             ('24', '129', '1', 'AN', 'TSYS Acquiring Solutions', 'Expanded Trailer Amounts Indicator\r\nThis field indicates whether the \r\ntransmission trailer expanded amount fields \r\nwill be used instead of the standard amount \r\nfields. Each expanded amount field is 15 \r\nbytes long, and each standard amount field \r\nis 12 bytes long. Expanded length fields are \r\navailable only if 256-byte records are being \r\ntransmitted.\r\nPossible values  \r\nN - \r\nuse standard amount fields \r\n(transmission trailer fields 5-7)\r\nY - \r\nuse expanded amount fields \r\n(transmission trailer fields 9, 10, 12)'),
             ('25', '130-256', '127', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "transmitBankNumber": None,
        "userAssignedTransmissionNumber": None,
        "transmissionNameIdentification": None,
        "userSecurityPassword": None,
        "transmissionDateJulian": None,
        "transmissionDateGregorian": None,
        "transmissionDescriptionCode": None,
        "preProcessFlag": None,
        "vendorIdentifierExpansion": None,
        "commingledFileProcessingFlag": None,
        "multiCurrencyCurrencyCode": None,
        "reservedForFutureUse14": None,
        "reservedForFutureUse15": None,
        "eccbQualificationFlag": None,
        "vendorIdentifier": None,
        "mailboxTransmissionIdentifier": None,
        "mailboxBatchNumber": None,
        "mailboxTransmissionDate": None,
        "mailboxTransmissionTime": None,
        "reservedForFutureUse22": None,
        "byteTransmissionIdentifierFlag256": None,
        "expandedTrailerAmountsIndicator": None,
        "reservedForFutureUse25": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.transmitBankNumber,
        self.userAssignedTransmissionNumber,
        self.transmissionNameIdentification,
        self.userSecurityPassword,
        self.transmissionDateJulian,
        self.transmissionDateGregorian,
        self.transmissionDescriptionCode,
        self.preProcessFlag,
        self.vendorIdentifierExpansion,
        self.commingledFileProcessingFlag,
        self.multiCurrencyCurrencyCode,
        self.reservedForFutureUse14,
        self.reservedForFutureUse15,
        self.eccbQualificationFlag,
        self.vendorIdentifier,
        self.mailboxTransmissionIdentifier,
        self.mailboxBatchNumber,
        self.mailboxTransmissionDate,
        self.mailboxTransmissionTime,
        self.reservedForFutureUse22,
        self.byteTransmissionIdentifierFlag256,
        self.expandedTrailerAmountsIndicator,
        self.reservedForFutureUse25 = (None)*25
        self.data = f.read(TransmissionHeader.LENGTH)
        super(TransmissionHeader, self).__init__()
        
class MerchantHeader(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nPossible values  \r\n9104 - \r\nThe merchant name and address \r\n(city, state, country, and postal \r\ncode) will be pulled from the TSYS \r\nAcquiring Solutions Merchant \r\nAccounting System (MAS). The \r\nMerchant Category Code (MCC) \r\nwill be pulled from the Merchant \r\nHeader 6 unless that field contains \r\nspaces. For more information, see \r\nthe Merchant Category Code\r\nfield (field 10).\r\n9107 - \r\nThe merchant name and address \r\nand the Merchant Category Code \r\nwill be pulled from the Draft 256 \r\nFinancial record. \r\n9019 - \r\nUsed for Merchant Transmittal \r\nAdustments.\r\nNote\r\nAirline transactions must use a transaction \r\ncode of 9107.'),
             ('3', '12-27', '16', 'N', 'TSYS Acquiring Solutions', 'Merchant Account Number\r\nUse the full merchant account number. This \r\nfield must be left-aligned and space-filled.'),
             ('4', '28-38', '11', 'N', 'TSYS Acquiring Solutions', 'Beginning Transaction Reference Number\r\nThis field must contain a non-ero number. \r\nIt must be right-aligned and ero-filled.'),
             ('5', '39-49', '11', 'N', 'TSYS Acquiring Solutions', 'Net Deposit Amount\r\nThis field must be right-aligned and ero-\r\nfilled. If the net deposit is negative, a \r\nnegative character sign is required. (See \r\nNegative amounts on page 56.)'),
             ('6', '50-58', '9', 'N', 'TSYS Acquiring Solutions', 'Total Amount of Discount\r\nThis field must contain the total amount of \r\ndiscount paid by the merchant. The value in \r\nthis field must be right-aligned and ero-\r\nfilled. The amount can be ero.\r\nIf the value is a discount refund to the \r\nmerchant, a negative character sign is \r\nrequired. (See Negative amounts on page \r\n56.)'),
             ('7', '59-61', '3', 'AN', 'TSYS Acquiring Solutions', 'Batch Item(s) Retention Location'),
             ('8', '62', '1', 'AN', 'TSYS Acquiring Solutions', 'Large Ticket Indicator\r\nPossible values  \r\nL - \r\nlarge ticket item\r\nSpace - \r\nnot a large ticket item'),
             ('9', '63-64', '2', 'AN', 'V, M', 'POS (Point of Sale)/Interaction Terminal \r\nCapabilities\r\nPossible values  \r\n0 - \r\nUnknown\r\n1 - \r\nTerminal not used\r\n2 - \r\nMag Stripe\r\n3 - \r\nBar Code/Payment Code\r\n4 - \r\nOCR\r\n5 - \r\nChip\r\n8 - \r\nContactless-read capability\r\n9 - \r\nTerminal does not read track data\r\nThis field can contain all spaces.'),
             ('10', '65-68', '4', 'N', 'V, M', 'Merchant Category Code (MCC)\r\nFor a 9104 transaction code\r\nIf you want to use the MCC that is stored in \r\nthe TSYS Acquiring Solutions MAS, use \r\nspaces in this field. If you want to use an \r\nMCC that is different from the one stored in \r\nthe MAS, use the preferred MCC in this \r\nfield. \r\nNote\r\nUsing this field with a 9104 transaction code \r\nwill not change the MCC value that is stored in \r\nthe MAS.\r\nFor a 9107 transaction code\r\nSpaces can be used in this field. The MCC \r\nvalue will be pulled from the Draft 256 \r\nFinancial Record.'),
             ('11', '69-71', '3', 'AN', '', 'Source Currency Code\r\nEntering the source currency code overrides \r\nthe merchant currency conversion code that \r\nis pulled from the Accounting Control \r\nRecord. This field can contain all spaces.\r\nNOTEBefore using currency codes not \r\npreviously utilied, please contact your TSYS \r\nAcquiring Solutions Relationship Managers about \r\ntesting the new currency.'),
             ('12', '72-86', '15', 'AN', 'V, M', 'Card Acceptor Identifier'),
             ('13', '87', '1', 'AN', 'TSYS Acquiring Solutions', 'Adusted Transaction Indicator\r\nPossible values  \r\nY - \r\ntransaction has been adusted\r\nSpace\r\nor N - \r\ntransaction has not been adusted\r\nNote\r\nYou must have TSYS Acquiring Solutions \r\napproval to use a Y in this field.'),
             ('14', '88', '1', 'AN', 'V, M', 'Mail/Telephone or Electronic Commerce \r\nIndicator\r\nThis field should contain a space unless the \r\nvalue in this field will apply to all items \r\nincluded in the batch.'),
             ('15', '89-91', '3', 'AN', 'V, M', 'Merchant Country Code\r\nIf the country code is two characters, this \r\nfield must be left-aligned and space-filled.'),
             ('16', '92-99', '8', 'AN', 'V, MCAPN', 'POS (Point of Sale)/Interaction Terminal \r\nIdentifier\r\nTerminal ID'),
             ('17', '100-114', '15', 'AN', 'M', 'Merchant Tax Identifier\r\nThe Merchant Tax Identifier is required for \r\nall Commercial Card transactions.'),
             ('18', '115', '1', 'AN', 'V', 'Additional Information Indicator\r\nPossible values  \r\nY - \r\nadditional information\r\nN or \r\nSpace - \r\nno additional information'),
             ('19', '116-129', '14', 'AN', 'V', 'Merchant Telephone Number\r\nThis field must be left-aligned and space-\r\nfilled. The fourth position must contain a \r\nhyphen.\r\nFormat  -'),
             ('20', '130-133', '4', 'AN', 'TSYS Acquiring Solutions', 'Department Code'),
             ('21', '134', '1', 'AN', 'TSYS Acquiring Solutions', 'Merchant Additional Data Indicator\r\nPossible values  \r\nY - \r\nissuer is authoried to print \r\nmerchants customer service \r\ntelephone number on cardholders \r\nstatement\r\nSpace - \r\ntelephone number not provided'),
             ('22', '135-138', '4', 'AN', 'TSYS Acquiring Solutions', 'Merchant Store Number\r\nThis field can contain spaces.'),
             ('23', '139-144', '6', 'AN', 'TSYS Acquiring Solutions', 'Merchant Deposit Date\r\nThis field must contain all spaces or the date \r\nof the merchant deposit.'),
             ('24', '145-146', '2', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('25', '147-154', '8', 'S', 'TSYS Acquiring Solutions', 'Control Sequence Number'),
             ('26', '155', '1', 'S', 'M', 'Reserved for future use'),
             ('27', '156-170', '15', 'N', 'TSYS Acquiring Solutions', 'Alternate Total Net Deposit Amount\r\nThis field must be right-aligned and ero-\r\nfilled.'),
             ('28', '171', '1', '', '', 'Convert Currency Indicator'),
             ('29', '172-181', '10', 'AN', 'X', 'American Express OptBlue Industry \r\nService Establishment (SE) Number'),
             ('30', '182-191', '10', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('31', '192 - 206', '15', 'N', 'TSYS Acquiring Solutions', 'Merchant Defined Conversion Rate\r\nCurrency conversion rate that will be used \r\nto fund the merchant.'),
             ('32', '207', '1', 'A', 'S', 'Discover MAP Override Flag\r\nIndicates if the transactions in this merchant \r\ndeposit are to be processed as Discover \r\nMAP transactions.\r\nAuthoriation and data capture vendors \r\nsupply the value in this field.\r\nPossible values  \r\nSpace - Default value.  Participation will be \r\ndetermined based on merchant set \r\nup in the TSYS Clearing and \r\nSettlement system.\r\nY - \r\nDiscover transactions in this \r\nmerchant deposit will be processed \r\nas Discover MAP\r\nN - \r\nDiscover transactions in this \r\nmerchant deposit will not be \r\nprocessed as Discover MAP'),
             ('33', '208-213', '6', 'N', 'TSYS Acquiring Solutions', 'Front-End BIN \r\nThis is the Bank Identification Number \r\nassociated with the Merchant in the TSYS \r\nBoarding System.\r\nNOTEThis field is for use only with Merchants \r\nutiliing Tokeniation and who have permission by \r\nTSYS Acquiring Solutions.'),
             ('34', '214-225', '12', 'N', 'TSYS Acquiring Solutions', 'Front-End MID\r\nThis is the Merchant Identifier associated with \r\nthe Merchant in the TSYS Boarding System.\r\nNOTEThis field is for use only with Merchants \r\nutiliing Tokeniation and who have permission by \r\nTSYS Acquiring Solutions.'),
             ('35', '226-242', '17', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('36', '243', '1', 'AN', 'X', 'American Express OptBlue participation \r\nindicator\r\nPossible values  \r\nY - \r\nMerchant is an  American Express \r\nOptBlue participant\r\nN - \r\nMerchant is not a American \r\nExpress OptBlue participant\r\nspace - Default value.  Participation will be \r\ndetermined based on merchant set up in the \r\nTSYS Clearing and Settlement system.'),
             ('37', '244-256', '13', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "merchantAccountNumber": None,
        "beginningTransactionReferenceNumber": None,
        "netDepositAmount": None,
        "totalAmountOfDiscount": None,
        "batchItemSRetentionLocation": None,
        "largeTicketIndicator": None,
        "posPointOfSaleInteractionTerminal9": None,
        "merchantCategoryCodeMcc": None,
        "sourceCurrencyCode": None,
        "cardAcceptorIdentifier": None,
        "adustedTransactionIndicator": None,
        "mailTelephoneOrElectronicCommerce": None,
        "merchantCountryCode": None,
        "posPointOfSaleInteractionTerminal16": None,
        "merchantTaxIdentifier": None,
        "additionalInformationIndicator": None,
        "merchantTelephoneNumber": None,
        "departmentCode": None,
        "merchantAdditionalDataIndicator": None,
        "merchantStoreNumber": None,
        "merchantDepositDate": None,
        "reservedForFutureUse24": None,
        "controlSequenceNumber": None,
        "reservedForFutureUse26": None,
        "alternateTotalNetDepositAmount": None,
        "convertCurrencyIndicator": None,
        "americanExpressOptblueIndustry": None,
        "reservedForFutureUse30": None,
        "merchantDefinedConversionRate": None,
        "discoverMapOverrideFlag": None,
        "frontEndBin": None,
        "frontEndMid": None,
        "reservedForFutureUse35": None,
        "americanExpressOptblueParticipation": None,
        "reservedForFutureUse37": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.merchantAccountNumber,
        self.beginningTransactionReferenceNumber,
        self.netDepositAmount,
        self.totalAmountOfDiscount,
        self.batchItemSRetentionLocation,
        self.largeTicketIndicator,
        self.posPointOfSaleInteractionTerminal9,
        self.merchantCategoryCodeMcc,
        self.sourceCurrencyCode,
        self.cardAcceptorIdentifier,
        self.adustedTransactionIndicator,
        self.mailTelephoneOrElectronicCommerce,
        self.merchantCountryCode,
        self.posPointOfSaleInteractionTerminal16,
        self.merchantTaxIdentifier,
        self.additionalInformationIndicator,
        self.merchantTelephoneNumber,
        self.departmentCode,
        self.merchantAdditionalDataIndicator,
        self.merchantStoreNumber,
        self.merchantDepositDate,
        self.reservedForFutureUse24,
        self.controlSequenceNumber,
        self.reservedForFutureUse26,
        self.alternateTotalNetDepositAmount,
        self.convertCurrencyIndicator,
        self.americanExpressOptblueIndustry,
        self.reservedForFutureUse30,
        self.merchantDefinedConversionRate,
        self.discoverMapOverrideFlag,
        self.frontEndBin,
        self.frontEndMid,
        self.reservedForFutureUse35,
        self.americanExpressOptblueParticipation,
        self.reservedForFutureUse37 = (None)*37
        self.data = f.read(MerchantHeader.LENGTH)
        super(MerchantHeader, self).__init__()
        
class FinancialRecord(Record):
    RECORD = (('3', '12-27', '16', 'AN', 'AllCAPN', 'Cardholder Account Number \r\nIf the Account Number contains fewer than \r\n16 digits, this field must be left-ustified and \r\nspace-filled.\r\nPrimary Account Number\r\nIf the account number contains more than \r\n16 characters, use the existing Cardholder \r\nAccount Number Expansion field to enter \r\nup to three more characters.'),
             ('4', '28-30', '3', 'AN', 'VS', 'Cardholder Account Number Expansion\r\nAccount Number Extension\r\nIf the cardholder account number is 19 \r\ncharacters long, use this field for the last 3 \r\ncharacters of the account number.\r\nIf you are sending a 16-character account \r\nnumber, do not enter any values in this field.'),
             ('5', '31-36', '6', 'N', 'All', 'Transaction Date\r\nDate of the original transaction \r\n(MMDDYY).'),
             ('6', '37', '1', 'AN', 'V', 'Market-Specific Authoriation Data \r\nIndicator \r\nUsed to identify the type of enriched data \r\nthat was present in the authoriation \r\nrequest. \r\nPossible values  \r\nA - \r\nAuto Rental\r\nB - \r\nBill Payment\r\nE - \r\nTransaction Aggregation\r\nJ - \r\nB2B Invoice Payment\r\nH - \r\nHotel/Lodging\r\nM - \r\nHealthcare\r\nN - \r\nInvalid or not applicable market \r\nspecific authoriation data received\r\nT - \r\nTransit\r\nNOTEOther Market-Specific Authoriation \r\nData Indicator values apply to auto rental and hotel \r\ntransactions and may be provided in the Car Rental \r\n(CARNT) or Lodging (LODGE) extension \r\nrecords.'),
             ('7', '38', '1', 'S', 'TSYS Acquiring Solutions', 'Card Type\r\nPossible values  \r\nM - \r\nMasterCard\r\nL - \r\nPrivate Label\r\nR - \r\nDiscover\r\nP - \r\nPaypal\r\nV - \r\nVisa\r\nS - \r\nAmerican Express\r\nO - \r\nOther'),
             ('8', '39', '1', 'AN', 'V', 'Prepaid Card Indicator\r\nPossible values  \r\nSpace - \r\nnot applicable\r\nL - \r\nprepaid load\r\nP - \r\nprepaid card'),
             ('9', '40-51', '12', 'N', 'All', 'Transaction Amount\r\nMonetary amount of the transaction in the \r\ncurrency of the country where the \r\ntransaction took place.\r\nNOTE This field contains a 2-character implied \r\ndecimal (100000000.00).'),
             ('10b-1b', '52-60', '9', 'AN', 'M', 'Abbreviated Airline Name'),
             ('10a', '52-76', '25', 'AN', 'AllSX, CAPN', 'Merchant DBA Name\r\nDoing Business As (DBA) name of the \r\nmerchant where the transaction originated. \r\nYou can also enter information that you \r\nwant to print on the cardholder statement.\r\nThis field must be left-ustified. You can use \r\nblanks as filler.\r\nFor MasterCard Quick Payment Service \r\n(QPS) transactions, positions 71-73 must \r\ncontain the registered QPS indicator.\r\nMerchant Name\r\nMerchant DBA (Doing Business As) name, \r\nwhich is also displayed on the cardholder \r\nstatement. For Discover, the field must \r\ncontain upper case characters and it must be \r\nleft ustified. It can be filled with spaces.\r\nLocation Name'),
             ('10b-2', '64-76', '13', 'AN', 'V', 'Visa Airline Ticket Number'),
             ('10b-3', '61-76', '16', 'S', 'M', 'Reserved for future use when used in \r\nconunction with Field 10b-1b for \r\nMasterCard airline transactions.'),
             ('11', '77-89', '13', 'AN', 'AllCAPN', 'Merchant City\r\nCity where the merchant is located. For \r\nDiscover, the field must contain upper case \r\ncharacters and it must be left ustified.You \r\ncan use spaces as filler.\r\nLocation City\r\nThe city name must be entered in upper case \r\ncharacters. In addition, the field must be left \r\n-ustified. You can use spaces as filler.\r\nAggregators Only - this field must contain \r\nthe city where the seller is located\r\nMOTO/Internet - Merchants in these \r\nindustries may substitute the name of the \r\ncity in which the merchants order \r\nprocessing facility is located.'),
             ('12', '90-92', '3', 'AN', 'AllCAPNS', 'Merchant State or Province Code\r\nCode for the state or province where the \r\nmerchant is located.\r\nThis field must be left-ustified. You can use \r\nblanks as filler since this field is normally \r\ntwo bytes in length.\r\nLocation Region Code\r\nThe code must be entered in upper case \r\ncharacters. In addition, the field must be left \r\n-ustified. You can use spaces as filler since \r\nthis field is normally two bytes in length.\r\nAggregators Only - This field must contain \r\nthe region code that corresponds to the \r\nstate, province or other country subdivision \r\nin which the seller is located.\r\nMerchant State or Province Code\r\nCode for the state or country where the \r\nmerchant is located. For Discover, this field \r\nmust contain upper case characters. '),
             ('13', '93', '1', 'AN', 'All', 'Extended Free-text Flag\r\nThis option allows the full, 41-character \r\nmerchant description (name, city and \r\nstate/province) to be displayed as one field.\r\nPossible values  \r\nY - \r\nuse option\r\nN or \r\nspace - \r\ndo not use option'),
             ('14', '94-96', '3', 'AN', 'V, M, SCAPN', 'Merchant Country Code\r\nCode that identifies the country where the \r\nmerchant is located.\r\nLocation Country Code\r\nAggregators Only - This field must contain \r\nthe country code that corresponds to the \r\nsellers location.'),
             ('15', '97-100', '4', 'N', 'V, MS, X (CAPN)', 'Merchant Category Code (MCC)\r\nFor a 9104 transaction code in Merchant \r\nHeader 6\r\nSpaces can be used in this field.\r\nFor a 9107 transaction code in Merchant \r\nHeader 6\r\nThis field must contain the MCC.\r\nMerchant Category Code (MCC)\r\nThe MCC identifies the type of business of \r\nthe merchant.'),
             ('16', '101-105', '5', 'N', 'V, MS', 'Merchant IP� or Postal Code \r\nIP Code or Postal Code for the merchant \r\naddress 5-character numeric.'),
             ('17', '106-111', '6', 'AN', 'V, M, X, JCBSCAPN', 'Authoriation Code\r\nFor Visa and MasterCard, this field must be \r\nleft-ustified. You can use blanks as filler.\r\nAuthoriation Code\r\nCode or number of the authoriation.\r\nThis field must be left-ustified. You can use \r\nblanks as filler.\r\nApproval Code\r\nApproval code generated by American \r\nExpress and contained in the Authoriation \r\nResponse message for the transaction. In \r\ncases such as credit transactions, when the \r\napproval code is not available or applicable, \r\nthe field must be filled with spaces.'),
             ('18', '112-122', '11', 'AN', 'V, M, X, D, JCB, SCAPN', 'Acquirers Internal Reference Number\r\nIf this field contains all spaces, TSYS \r\nAcquiring Solutions will assign the next \r\nsequential number after the merchant \r\nheaders Beginning Transaction Reference \r\nNumber.\r\nClient specific internal reference number for \r\nthe transaction.\r\nInvoice or Reference Number\r\nReference number used by American \r\nExpress. The number can be either the \r\noriginal invoice number from a receipt \r\ngenerated by a POS        (Point of Service) \r\nterminal, or the reference number \r\nassociated with a transaction in the \r\ncomputeried cash register or order \r\nprocessing system used by the merchant. \r\nThe merchant must be able to use the \r\nreference number to retrieve information \r\nabout the transaction.\r\nIf no reference number is used, the field \r\nmust be filled with eroes.'),
             ('19', '123', '1', 'AN', 'V', 'Authoriation Source Code'),
             ('20', '124', '1', 'AN', 'V', 'Cardholder Identification Method\r\nPossible values  \r\nSpace - \r\nNot specified\r\n1 - \r\nSignature\r\n2 - \r\nPIN\r\n3 - \r\nUnattended\r\n4 - \r\nMOTO'),
             ('21', '125', '1', 'AN', 'VM', 'Acceptance Terminal Indicator\r\nPossible values  \r\nSpace - \r\nNot applicable to this transaction\r\n1 - \r\nUnattended cardholder activated, \r\nno authoriation, below floor limit\r\n2 - \r\nUnattended chip and PIN \r\ntransaction, Europe only\r\n3 - \r\nUnattended cardholder activated, \r\nauthoried transaction\r\n4 - \r\nRemote Indicator\r\n5 - \r\nUnattended consumer device\r\n9 - \r\nMobile acceptance solution\r\nCardholder-Activated Terminal (CAT) \r\nIndicator\r\nPossible values  \r\nSpace - \r\nTerminal type data unknown or not \r\navailable\r\nA - \r\nATM Terminal\r\n1 - \r\nAutomated Dispensing Machine\r\n2 - \r\nSelf Service Terminal (Use with \r\nautomated fueling and unattended \r\nterminal)\r\n3 - \r\nLimited amount terminal\r\n4 - \r\nIn-flight Commerce\r\n5 - \r\nReserved (Do not use)\r\n6 - \r\nMasterCard eCommerce\r\n7 - \r\nTransponder Transaction (RFID, \r\ncontactless)\r\n9 - \r\nMobile acceptance solution\r\nM - \r\nManual, no terminal\r\nP - \r\nPOI terminal'),
             ('22', '126', '1', 'AN', 'V', 'Reimbursement Attribute Code\r\nNOTEThis is only used for Debit/EBT \r\ntransactions.'),
             ('23', '127', '1', 'AN', 'V', 'Chip Condition Code\r\nPossible values  \r\n0 - \r\nService code does not begin with a \r\n2 or 6 or fill for subsequent \r\npositions that are present.\r\n1 - \r\nService code begins with a 2 or 6 \r\nlast read at the chip capable \r\nterminal was successful or was not a \r\nchip transaction or unknown.\r\n2 - \r\nService code begins with a 2 or 6 \r\nlast transaction at the chip capable \r\nterminal was an unsuccessful chip \r\nread.'),
             ('24', '128', '1', 'AN', 'V', 'Mail/Telephone or Electronic Commerce \r\nIndicator\r\nPossible values  \r\nSpace - \r\nNot applicable\r\n1 - \r\nSingle transaction for MOTO\r\n2 - \r\nRecurring transaction\r\n3 - \r\nInstallment payment\r\n4 - \r\nUnknown or classification/other \r\nmail order\r\n5 - \r\nSecure electronic commerce \r\ntransaction\r\n6 - \r\nNon-authenticated security \r\ntransaction at a 3-D secure capable \r\nmerchant\r\n7 - \r\nNon-authenticated electronic \r\ncommerce security transaction\r\n8 - \r\nNon-secure electronic commerce \r\ntransaction\r\n9 - \r\nNon-authenticated secure \r\ntransaction at a secure electronic \r\ncapable merchant located outside \r\nthe U.S. region'),
             ('25', '129-130', '2', 'AN', 'V, M', 'Point of Sale (POS)/Interaction Terminal \r\nEntry Mode\r\nPossible values  \r\n00 - \r\nUnknown or terminal not used\r\n01 - \r\nManual (Key entry) \r\n02 - \r\nFor Visa Magnetic stripe read \r\nCVV checking may not be possible.  \r\nFor MasterCard Magnetic stripe \r\nread - track data is not required or \r\nthe acquirer is not qualified to use a \r\nvalue of 90, so MasterCard replaced \r\nthe 90 or 91 with the value of 2.\r\n03 - \r\nBar code/Payment code read\r\n04 - \r\nOCR coding read (POS Check)\r\n05 - \r\nIntegrated circuit card read CVV \r\ndata reliable\r\n06 - \r\nTrack One read (Visa only)\r\n07 - \r\nAccount number auto-entry via \r\ncontactless chip\r\n79 - \r\nAcquirer generated transaction due \r\nto a chip card failure of a hybrid \r\nterminal (MC only)\r\n80 - \r\nTerminal defaulted to read the \r\nmagnetic stripe after a chip card \r\nfailure (MC Only)\r\n81 - \r\nElectronic Commerce transaction \r\n(MC Only)\r\n82 - \r\nPAN Auto Entry via Server (Issuer, \r\nAcquirer, Third Party Vendor \r\nSystem)\r\n90 - \r\nMagnetic stripe read and exact \r\ncontent of track one or two \r\nincluded\r\n91 - \r\nAccount number auto-entry via \r\ncontactless magnetic stripe\r\n95 - \r\nIntegrated circuit card CVV data \r\nmay be unreliable (Visa only)96 - \r\nStored Value from Pre-Registered \r\nCheckout service'),
             ('26', '131', '1', 'AN', 'VM', 'Visa Authoriation Characteristics \r\nIndicator   (ACI)\r\nMasterCard ACI must be R for \r\ntransactions submitted for the MC Service \r\nIndustries interchange program, and a "P" \r\nfor the MC Travel Industries Premier \r\nService interchange program.PS2000 Transaction Identifier \r\nTransaction Identifier\r\nNumber assigned to a sales transaction by \r\nAmerican Express. The transaction \r\nidentifier is derived from the Authoriation \r\nResponse message, and is used to track the \r\ntransaction.\r\nNetwork Reference ID \r\nUnique ID assigned by Discover at the time \r\nof the Authoriation Response.'),
             ('27b-1', '132-140', '9', 'AN', 'M', 'BankNet Reference Number'),
             ('27c-1', '132-141', '10', '', 'X', 'Record of Charge Number\r\nThis field must be left-ustified and space-\r\nfilled.'),
             ('27b-2', '141-146', '6', 'S', 'M', 'Reserved for future use'),
             ('27c-2', '142-146', '5', 'S', 'X', 'Reserved for future use'),
             ('28', '147-149', '3', 'AN', 'VCAPN', 'Authoriation Currency Code\r\nCode that identifies the currency used in the \r\noriginal authoried transaction.\r\nNOTEBefore using currency codes not \r\npreviously utilied, please contact your TSYS \r\nAcquiring Solutions Relationship Managers about \r\ntesting the new currency.\r\nTransaction Currency Code\r\nCode that identifies the currency used in the \r\noriginal authoried transaction. Since \r\nAmerican Express currently accepts only \r\ntransactions made in the United States in \r\nUSD, the valid values for this field are USD \r\nand 840.\r\nIf the alpha identifier is used, the characters \r\nmust be upper case.'),
             ('29', '150-161', '12', 'N', 'All', 'Authoriation Amount\r\nThis field should contain the original \r\ntransaction amount that was authoried.'),
             ('30b-1', '162-164', '3', 'N', 'M ', 'Electronic Commerce Security Level \r\nIndicator \r\nConsists of three subfields that provide \r\ninformation about the Universal Cardholder \r\nAuthentication Field (UCAF) security \r\nprotocol for internet transactions.\r\nSubfield 1 - Security Protocol\r\nPossible values  \r\n0 - \r\nReserved for existing MasterCard \r\nEurope/Visa� definitions\r\n1 - \r\nReserved for future use\r\n2 - \r\nChannel\r\n3-8 - \r\nReserved for future use\r\n9 - \r\nNone (no security protocol)\r\nSubfield 2 - Cardholder Authentication \r\nIndicator\r\nPossible values  \r\n0 - \r\nReserved for future use\r\n1 - \r\nCardholder certificate not used\r\n2 - \r\nProcessed through MasterPass\r\n3 - \r\nReserved for future use\r\n4 - \r\nDigital Secure Remote Payment \r\ntransaction\r\n9 - \r\nReserved for future use\r\nSubfield 3 - UCAF Collection Indicator\r\nPossible values  \r\n0 - \r\nUCAF data collection is not \r\nsupported by the merchant\r\n1 - \r\nUCAF data collection is supported \r\nby the merchant, and UCAF data \r\nmay be present in the authoriation \r\nmessage2 - \r\nUCAF data collection is supported \r\nby the merchant, and UCAF data \r\nwas present in the authoriation \r\nmessage\r\n3 - \r\nUCAF data collection is supported \r\nby the merchant, and UCAF \r\nMasterCard assigned Static Account \r\nholder Authentication Value data \r\nmust be present\r\n4 - \r\nReserved for future use\r\n5 - \r\nIssuer risk based decisioning  \r\n6 - \r\nMerchant risk based decisioning \r\n7 - \r\nPartial shipment or recurring \r\npayment'),
             ('30a', '162-165', '4', 'AN', 'V', 'Validation Code'),
             ('30b-2', '165', '1', 'S', 'TSYS Acquiring Solutions', 'Reserved for future useVisa   Authoriation Response Code\r\nDiscover   Response Code\r\nAmex Approval Code'),
             ('32b-1', '168-171', '4', 'N', 'M', 'BankNet Date\r\nFormat  MMDD'),
             ('32a', '168-173', '6', 'N', 'VS', 'Authoriation Date\r\nFormat MMDDYY\r\nAuthoriation Transmission Date\r\nDate that the authoriation was captured by \r\nthe association or scheme (MMDDYY).\r\nDiscover Local Transaction Date \r\nDate the transaction took place \r\n(MMDDYY). This date is the merchants \r\nlocal date. '),
             ('32b-2', '172-173', '2', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('33', '174-175', '2', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('34', '176-178', '3', 'AN', 'TSYS Acquiring Solutions', 'Debit Network Identifier\r\nFor a list of possible values, see Debit card \r\nnetwork IDs on page 57.'),
             ('35', '179', '1', 'AN', 'M', 'Switch-Settled Indicator'),
             ('36', '180-184', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nIndicates if an extension record follows and, \r\nif so, the type of extension record.\r\nSpace - \r\nNo extension record follows\r\nAIRL1 - \r\nAirline/Passenger Transport 1\r\nAMEXR - Restaurant\r\nCARNT - Car Rental\r\nCHECK - Electronic Check\r\nDIRCT - Direct Marketing\r\nEINTR - Electronic Invoice Transaction \r\nData\r\nEINPR - Electronic Invoice Party \r\nInformation\r\nENT1 - Entertainment/Ticketing\r\nEXT - General\r\nFLEET - Fleet Service 1\r\nINS1 - \r\nInsurance\r\nLODGE - Lodging\r\nMERCH - Merchant Description\r\nPURC1 - \r\nPurchasing Card 1\r\nRETAL - Retail\r\nSHIP1 - \r\nShipping Services 1\r\nTEMP1 - Temporary Help Services 1\r\nTBSUM - Telephone Billing Summary\r\nTBDET - Telephone Billing Detail'),
             ('37', '185', '1', 'AN', 'V', 'Requested Payment Service Indicator'),
             ('38b-1', '186-187', '2', 'AN', 'V', 'Electronic Commerce Goods Indicator\r\nThis field must be left-ustified and space \r\nfilled. The field must contain one of the \r\nvalid values listed below. The second \r\nposition must be a blank.\r\nValid values for the first position\r\nDDigital Goods\r\nPPhysical Goods\r\nSpaceNot applicable'),
             ('38b-2', '188', '1', 'AN', 'V', 'Transaction Code Qualifier (TCQ)\r\nValid Values\r\n0Any Non-Account Funding or Non CFT\r\n    transaction (default)\r\n1Account funding sales draft or \r\n    credit voucher\r\n2Card holder funds Transfer (CFT)'),
             ('38b-3', '189', '1', 'AN', 'V', 'Number of Payment Forms \r\nThis field must contain a value from 1 \r\nthrough 9, or  (plus character if greater \r\nthan 9) '),
             ('38c', '186-191', '6', 'N', 'S, X', 'Discover Sales Tax Amount\r\nAmerican Express Sales Tax.\r\nTotal monetary amount of the sales tax \r\ncharged at the point of the sale.\r\nThis field must be right-ustified. It can be \r\nfilled with eros.'),
             ('38d', '186-191', '6', 'AN', 'M', 'MasterCard Partner ID Code'),
             ('38b-4', '190-191', '2', 'AN', 'TSYS Acquiring Solutions', 'Reserved for Future Use'),
             ('39a-1', '192', '1', 'AN', 'V', 'Special Condition indicator, Risk \r\nIdentification'),
             ('39a-2', '193', '1', 'AN', 'V', 'Special Condition indicator, Merchant \r\nTransaction'),
             ('39b', '192-193', '2', 'AN', 'M', 'Transaction Category Indicator\r\nPossible values  \r\nSpaces - \r\nNot applicable\r\n02 - \r\nMerchant claims exemption from \r\nIIAS based on the 90 percent rule\r\n03 - \r\nQualified healthcare expenses were \r\nverified against an Inventory \r\nInformation Approval System \r\n(IIAS) during the authoriation \r\nprocess.'),
             ('40', '194-208', '15', 'AN', 'V', 'Card Acceptor Identifier'),
             ('41', '209-216', '8', 'AN', 'V, M', 'Point of Sale/Interaction Terminal \r\nIdentifier\r\nThis field should be populated with the \r\nterminal V from a TSYS Front End system \r\n(MMS or Express Merchant Boarding and \r\nMaintenance)'),
             ('42', '217', '1', 'S', 'S, X', 'Discover/AMEX Flag'),
             ('43', '218', '1', 'S', 'TSYS Acquiring Solutions', 'Electronic Commerce Transaction \r\nIndicator'),
             ('44', '219-227', '9', 'AN', 'V, M, S', 'Cash back amount'),
             ('45', '228', '1', 'AN', 'P', 'Store Type\r\nPossible values  \r\nG - \r\ngas advantage\r\nP - \r\npit stop store\r\nR - \r\nretail store\r\nO - \r\nother\r\nS - \r\npart source'),
             ('46', '229-236', '8', 'AN', 'P', 'Invoice Number'),
             ('47', '237', '1', 'AN', 'TSYS Acquiring Solutions', 'Refund Risk Type Indicator\r\nThis field will identify the status of the \r\ncredit/refund to offsetting sales totals.\r\nPossible values  \r\nN - \r\nNo offsetting sale found\r\nE - \r\nAn individual credit/refund equal \r\nto total sales but total \r\ncredits/refunds exceeds total sales\r\nG - \r\nAn individual credit/refund greater \r\nthan total sales\r\nP - \r\nAn individual credit/refund less \r\nthan total sales but total \r\ncredits/refunds exceeds total sales'),
             ('48', '238-240', '3', 'AN', 'M', 'MasterCard Wallet Identifier \r\nThis is a MasterCard value that is generated \r\nby the MasterPass online platform. This \r\nvalue is passed to the merchant at the time \r\nof consumer checkout, and is included in \r\nthe authoriation request transaction. '),
             ('49', '241-245', '5', 'AN', 'TSYS Acquiring Solutions', 'Reserved for Future Use'),
             ('50', '246-248', '3', 'AN', 'P', 'Insurance Code'),
             ('51', '249', '1', 'AN', 'VP', 'Visa  Service Development Indicator\r\nPrivate label  MSR Flag'),
             ('52', '250-254', '5', 'AN', '', 'Register Number\r\nIf the transaction is ACH, then set to\r\n 9001, left ustified and space filled.\r\nIf the transaction is not ACH, then space \r\nfill.'),
             ('53', '255', '1', 'AN', '', 'Original ESID Code'),
             ('54', '256', '1', 'AN', 'MPV', 'MasterCard  Recurring Payment Indicator\r\nPrivate label Insurance Payment Choices\r\nPOS Environment\r\nR Recurring payment\r\nSpaceDefault'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "cardholderAccountNumber": None,
        "cardholderAccountNumberExpansion": None,
        "transactionDate": None,
        "marketSpecificAuthoriationData": None,
        "cardType": None,
        "prepaidCardIndicator": None,
        "transactionAmount": None,
        "abbreviatedAirlineName": None,
        "merchantDbaName": None,
        "visaAirlineTicketNumber": None,
        "reservedForFutureUseWhenUsedIn": None,
        "merchantCity": None,
        "merchantStateOrProvinceCode": None,
        "extendedFreeTextFlag": None,
        "merchantCountryCode": None,
        "merchantCategoryCodeMcc": None,
        "merchantIpOrPostalCode": None,
        "authoriationCode": None,
        "acquirersInternalReferenceNumber": None,
        "authoriationSourceCode": None,
        "cardholderIdentificationMethod": None,
        "acceptanceTerminalIndicator": None,
        "reimbursementAttributeCode": None,
        "chipConditionCode": None,
        "mailTelephoneOrElectronicCommerce": None,
        "pointOfSalePosInteractionTerminal": None,
        "visaAuthoriationCharacteristics": None,
        "banknetReferenceNumber": None,
        "recordOfChargeNumber": None,
        "reservedForFutureUse27b-2": None,
        "reservedForFutureUse27c-2": None,
        "authoriationCurrencyCode": None,
        "authoriationAmount": None,
        "electronicCommerceSecurityLevel": None,
        "validationCode": None,
        "reservedForFutureUsevisaAuthoriationResponseCode": None,
        "banknetDate": None,
        "authoriationDate": None,
        "reservedForFutureUse32b-2": None,
        "reservedForFutureUse33": None,
        "debitNetworkIdentifier": None,
        "switchSettledIndicator": None,
        "extensionRecordIndicator": None,
        "requestedPaymentServiceIndicator": None,
        "electronicCommerceGoodsIndicator": None,
        "transactionCodeQualifierTcq": None,
        "numberOfPaymentForms": None,
        "discoverSalesTaxAmount": None,
        "mastercardPartnerIdCode": None,
        "reservedForFutureUse38b-4": None,
        "specialConditionIndicatorRisk": None,
        "specialConditionIndicatorMerchant": None,
        "transactionCategoryIndicator": None,
        "cardAcceptorIdentifier": None,
        "pointOfSaleInteractionTerminal": None,
        "discoverAmexFlag": None,
        "electronicCommerceTransaction": None,
        "cashBackAmount": None,
        "storeType": None,
        "invoiceNumber": None,
        "refundRiskTypeIndicator": None,
        "mastercardWalletIdentifier": None,
        "reservedForFutureUse49": None,
        "insuranceCode": None,
        "visaServiceDevelopmentIndicator": None,
        "registerNumber": None,
        "originalEsidCode": None,
        "mastercardRecurringPaymentIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.cardholderAccountNumber,
        self.cardholderAccountNumberExpansion,
        self.transactionDate,
        self.marketSpecificAuthoriationData,
        self.cardType,
        self.prepaidCardIndicator,
        self.transactionAmount,
        self.abbreviatedAirlineName,
        self.merchantDbaName,
        self.visaAirlineTicketNumber,
        self.reservedForFutureUseWhenUsedIn,
        self.merchantCity,
        self.merchantStateOrProvinceCode,
        self.extendedFreeTextFlag,
        self.merchantCountryCode,
        self.merchantCategoryCodeMcc,
        self.merchantIpOrPostalCode,
        self.authoriationCode,
        self.acquirersInternalReferenceNumber,
        self.authoriationSourceCode,
        self.cardholderIdentificationMethod,
        self.acceptanceTerminalIndicator,
        self.reimbursementAttributeCode,
        self.chipConditionCode,
        self.mailTelephoneOrElectronicCommerce,
        self.pointOfSalePosInteractionTerminal,
        self.visaAuthoriationCharacteristics,
        self.banknetReferenceNumber,
        self.recordOfChargeNumber,
        self.reservedForFutureUse27b-2,
        self.reservedForFutureUse27c-2,
        self.authoriationCurrencyCode,
        self.authoriationAmount,
        self.electronicCommerceSecurityLevel,
        self.validationCode,
        self.reservedForFutureUsevisaAuthoriationResponseCode,
        self.banknetDate,
        self.authoriationDate,
        self.reservedForFutureUse32b-2,
        self.reservedForFutureUse33,
        self.debitNetworkIdentifier,
        self.switchSettledIndicator,
        self.extensionRecordIndicator,
        self.requestedPaymentServiceIndicator,
        self.electronicCommerceGoodsIndicator,
        self.transactionCodeQualifierTcq,
        self.numberOfPaymentForms,
        self.discoverSalesTaxAmount,
        self.mastercardPartnerIdCode,
        self.reservedForFutureUse38b-4,
        self.specialConditionIndicatorRisk,
        self.specialConditionIndicatorMerchant,
        self.transactionCategoryIndicator,
        self.cardAcceptorIdentifier,
        self.pointOfSaleInteractionTerminal,
        self.discoverAmexFlag,
        self.electronicCommerceTransaction,
        self.cashBackAmount,
        self.storeType,
        self.invoiceNumber,
        self.refundRiskTypeIndicator,
        self.mastercardWalletIdentifier,
        self.reservedForFutureUse49,
        self.insuranceCode,
        self.visaServiceDevelopmentIndicator,
        self.registerNumber,
        self.originalEsidCode,
        self.mastercardRecurringPaymentIndicator = (None)*68
        self.data = f.read(FinancialRecord.LENGTH)
        super(FinancialRecord, self).__init__()
        
class AirlinePassengerTransport1ExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nA list of transaction codes can be found on \r\nthe Inquire Status Record (ISR) screen of \r\nthe TSYS Accounting (TSA) System.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator identifies this record \r\nas an Airline/Passenger Transport 1 \r\nExtension Record.\r\nRequired value  AIRL1'),
             ('4b-1', '17-36', '20', 'AN', 'V', 'Passenger Name'),
             ('4a-1', '17-41', '25', 'AN', 'M, S', 'Passenger Name'),
             ('4a-2', '42-46', '5', 'S', 'M', 'Reserved for future use'),
             ('4b-2', '37-46', '10', 'S', 'V', 'Reserved for future use'),
             ('5', '47-63', '17', 'AN', 'M, S', 'Customer Code'),
             ('6', '64-75', '12', 'N', 'V, MS', 'Total Fare Amount\r\nTotal Fare'),
             ('7', '76-87', '12', 'N', 'V, MS', 'Total Tax Amount\r\nTotal Taxes'),
             ('8', '88-99', '12', 'N', 'V', 'National Tax Amount'),
             ('9', '100-111', '12', 'N', 'V, MS', 'Total Fee Amount\r\nTotal Fee'),
             ('10', '112-114', '3', 'AN', 'V, S', 'Currency Code\r\nNOTEBefore using currency codes not \r\npreviously utilied, please contact your TSYS \r\nAcquiring Solutions Relationship Managers about \r\ntesting the new currency.'),
             ('11', '115-127', '13', 'AN', 'V', 'Exchange Ticket Number'),
             ('12', '128-139', '12', 'N', 'VS', 'Exchange Ticket Amount\r\nExchange Amount'),
             ('13', '140-147', '8', 'AN', 'V, M, S', 'Travel Agency Code'),
             ('14', '148-172', '25', 'AN', 'V, M, S', 'Travel Agency Name'),
             ('15', '173-186', '14', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('16', '187', '1', 'AN', 'V', 'Internet Indicator'),
             ('17', '188-193', '6', 'AN', 'M, S', 'Issue Date\r\nFormat  MMDDYY'),
             ('18', '194-197', '4', 'AN', 'MS', 'Issuing Carrier\r\nCarrier Code'),
             ('19', '198', '1', 'AN', 'V', 'Restricted Ticket Number Indicator'),
             ('20', '199-202', '4', 'AN', 'V', 'Computeried Reservation System \r\nIndicator'),
             ('21', '203-217', '15', 'N', 'M, S', 'Ticket Number\r\nThis field must be left-ustified and space-\r\nfilled.'),
             ('22', '218-219', '2', '', '', 'Multi-Sequence Number'),
             ('23', '220-221', '2', '', '', 'Multi-Sequence Count'),
             ('24', '222-239', '18', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('25', '240', '1', '', '', 'Electronic Ticket Number'),
             ('26', '241-251', '11', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('27', '252-256', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nPossible values  \r\nSpace - \r\nno extension record follows\r\nAIRL2 - \r\nan Airline/Passenger Transport 2 \r\nExtension Record follows'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "passengerName4b-1": None,
        "passengerName4a-1": None,
        "reservedForFutureUse4a-2": None,
        "reservedForFutureUse4b-2": None,
        "customerCode": None,
        "totalFareAmount": None,
        "totalTaxAmount": None,
        "nationalTaxAmount": None,
        "totalFeeAmount": None,
        "currencyCode": None,
        "exchangeTicketNumber": None,
        "exchangeTicketAmount": None,
        "travelAgencyCode": None,
        "travelAgencyName": None,
        "reservedForFutureUse15": None,
        "internetIndicator": None,
        "issueDate": None,
        "issuingCarrier": None,
        "restrictedTicketNumberIndicator": None,
        "computeriedReservationSystem": None,
        "ticketNumber": None,
        "multiSequenceNumber": None,
        "multiSequenceCount": None,
        "reservedForFutureUse24": None,
        "electronicTicketNumber": None,
        "reservedForFutureUse26": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.passengerName4b-1,
        self.passengerName4a-1,
        self.reservedForFutureUse4a-2,
        self.reservedForFutureUse4b-2,
        self.customerCode,
        self.totalFareAmount,
        self.totalTaxAmount,
        self.nationalTaxAmount,
        self.totalFeeAmount,
        self.currencyCode,
        self.exchangeTicketNumber,
        self.exchangeTicketAmount,
        self.travelAgencyCode,
        self.travelAgencyName,
        self.reservedForFutureUse15,
        self.internetIndicator,
        self.issueDate,
        self.issuingCarrier,
        self.restrictedTicketNumberIndicator,
        self.computeriedReservationSystem,
        self.ticketNumber,
        self.multiSequenceNumber,
        self.multiSequenceCount,
        self.reservedForFutureUse24,
        self.electronicTicketNumber,
        self.reservedForFutureUse26,
        self.extensionRecordIndicator = (None)*30
        self.data = f.read(AirlinePassengerTransport1ExtensionRecord.LENGTH)
        super(AirlinePassengerTransport1ExtensionRecord, self).__init__()
        
class AirlinePassengerTransport2ExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nA list of transaction codes can be found on \r\nthe Inquire Status Record (ISR) screen of \r\nthe TSYS Accounting (TSA) System.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator identifies this record \r\nas an Airline/Passenger Transport 2 \r\nExtension Record.\r\nRequired value  AIRL2'),
             ('4', '17-30', '14', 'AN', 'V, MS', 'Conunction Ticket Number\r\nFor Visa, this field must be left-ustified and \r\nspace-filled. Visa uses only 13 characters for \r\nthe conunction ticket number.\r\nFor MasterCard, the ticket number is 14 \r\ncharacters.\r\nLeg Conunction Ticket Number\r\nTicket number for this leg of the flight'),
             ('5', '31', '1', 'AN', 'V, MS', 'Coupon Number\r\nLeg Coupon '),
             ('6', '32-33', '2', 'AN', 'V, MS', 'Carrier Code\r\nLeg Carrier Code'),
             ('7', '34-38', '5', 'AN', 'V, MS', 'Flight Number\r\nLeg Flight Number'),
             ('8', '39-40', '2', 'AN', 'V, MS', 'Service Class\r\nLeg Class'),
             ('9', '41-45', '5', 'AN', 'VMS', 'Visa  Origination City/Airport Code\r\nMasterCard City of Origin/Airport Code\r\nDiscover Leg Departure Airport'),
             ('10', '46', '1', 'AN', 'V, MS', 'Stopover Code\r\nLeg Stopover Code'),
             ('11', '47-51', '5', 'AN', 'VMS', 'Visa Destination City/Airport Code\r\nMasterCard City of Destination/Airport \r\nCode\r\nDiscover Leg Destination Code'),
             ('12', '52-59', '8', '', '', 'Fare Basis Code'),
             ('13', '60-65', '6', 'N', 'VM, S', 'Visa Departure Date\r\nFormat  MMDDYY\r\nMasterCard Travel Date\r\nDiscover Leg Date\r\nFor the first leg, this field is used to house \r\nthe travel date for that leg (departure date). \r\nFor each subsequent leg, this field can \r\ncontain the travel date of the particular leg \r\n(preferred) or the travel date for the first leg.\r\nFormat MMDDYY'),
             ('14', '66-69', '4', 'N', 'V, MS', 'Departure Time\r\nLeg Departure Time\r\nFormat HHMM'),
             ('15', '70-73', '4', 'N', 'V, MS', 'Arrival Time\r\nLeg Arrival Time\r\nFormat HHMM'),
             ('16', '74', '1', 'AN', 'M', 'Departure Time Segment'),
             ('17', '75', '1', 'AN', 'M', 'Arrival Time Segment'),
             ('18b', '76-90', '15', 'AN', 'MS', 'MasterCard Fare Basis Code\r\nDiscover Leg Fare Basis Code'),
             ('18a-2', '84-90', '7', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('19', '91-105', '15', 'AN', 'MS', 'Exchange Ticket Number\r\nExchange Ticket'),
             ('20', '106-116', '11', 'N', 'MS', 'Fare Amount\r\nLeg Amount'),
             ('21', '117-125', '9', 'N', 'MS', 'Fee Amount\r\nLeg Fees'),
             ('22', '126-134', '9', 'N', 'MS', 'Tax Amount\r\nLeg Taxes'),
             ('23', '135-154', '20', 'AN', 'MS', 'Endorsements/Restrictions\r\nRestriction Indicator or Leg Restrictions\r\nEndorsements are notations, such as value \r\nadded tax, which can be added by the agency \r\nor required by the government. Restrictions \r\nare limitations set on a ticket based on a type \r\nof fare, such as non-refundable or 3-day \r\nminimum stay.\r\nRestriction Indicator is a part of Sequence II \r\nof the Discover Network Airline \r\nSupplemental Data record.\r\nLeg Restrictions is a part of Sequence IV of \r\nthe Discover Network Airline Supplemental \r\nData Record.'),
             ('24', '155-172', '18', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('25', '173-176', '4', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('26', '177-178', '2', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('27', '179-191', '13', '', '', 'Control ID/Travel Obligation Number'),
             ('28', '192-251', '60', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('25', '252-256', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nPossible values  \r\nSpace - \r\nno extension record follows\r\nAIRL2 - \r\nanother Airline/Passenger \r\nTransport 2 Extension Record \r\nfollows'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "conunctionTicketNumber": None,
        "couponNumber": None,
        "carrierCode": None,
        "flightNumber": None,
        "serviceClass": None,
        "visaOriginationCityAirportCode": None,
        "stopoverCode": None,
        "visaDestinationCityAirportCode": None,
        "fareBasisCode": None,
        "visaDepartureDate": None,
        "departureTime": None,
        "arrivalTime": None,
        "departureTimeSegment": None,
        "arrivalTimeSegment": None,
        "mastercardFareBasisCode": None,
        "reservedForFutureUse18a-2": None,
        "exchangeTicketNumber": None,
        "fareAmount": None,
        "feeAmount": None,
        "taxAmount": None,
        "endorsementsRestrictions": None,
        "reservedForFutureUse24": None,
        "reservedForFutureUse25": None,
        "reservedForFutureUse26": None,
        "controlIdTravelObligationNumber": None,
        "reservedForFutureUse28": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.conunctionTicketNumber,
        self.couponNumber,
        self.carrierCode,
        self.flightNumber,
        self.serviceClass,
        self.visaOriginationCityAirportCode,
        self.stopoverCode,
        self.visaDestinationCityAirportCode,
        self.fareBasisCode,
        self.visaDepartureDate,
        self.departureTime,
        self.arrivalTime,
        self.departureTimeSegment,
        self.arrivalTimeSegment,
        self.mastercardFareBasisCode,
        self.reservedForFutureUse18a-2,
        self.exchangeTicketNumber,
        self.fareAmount,
        self.feeAmount,
        self.taxAmount,
        self.endorsementsRestrictions,
        self.reservedForFutureUse24,
        self.reservedForFutureUse25,
        self.reservedForFutureUse26,
        self.controlIdTravelObligationNumber,
        self.reservedForFutureUse28,
        self.extensionRecordIndicator = (None)*30
        self.data = f.read(AirlinePassengerTransport2ExtensionRecord.LENGTH)
        super(AirlinePassengerTransport2ExtensionRecord, self).__init__()
        
class CarRentalExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nA list of transaction codes can be found on \r\nthe Inquire Status Record (ISR) screen of \r\nthe TSYS Accounting (TSA) System.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator identifies this record \r\nas a Car Rental Extension Record.\r\nRequired value  CARNT'),
             ('4b-1', '17-25', '9', '', 'MSCAPN', 'MasterCard Rental Agreement Number\r\nAgreement Reference\r\nAmerican Express Auto Rental Agreement \r\nNumber\r\nNumber of the invoice associated with the \r\nrental agreement that is signed by the \r\ncardmember.'),
             ('4b-2', '26-35', '10', '', 'MS', 'MasterCard Customer Service Telephone \r\nNumber \r\nToll Free Number'),
             ('4a', '17-41', '25', 'AN', 'V', 'Visa Car Rental Agreement Number'),
             ('4b-3', '36-41', '6', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('5', '42', '1', 'AN', 'V', 'No Show Indicator'),
             ('6', '43-48', '6', 'AN', 'V', 'Extra Charges'),
             ('7', '49-54', '6', 'N', 'V, MSCAPN', 'Checkout Date (MMDDYY)\r\nThis is the date the customer picked up the \r\ncar or was scheduled to do so.\r\nRental Date (MMDDYY)\r\nThis is the date the customer picked up the \r\ncar or was scheduled to do so.\r\nAmerican Express Auto Rental Pickup \r\nDate\r\nDate the rental vehicle was picked up by the \r\ncardmember (MMDDYY).'),
             ('8', '55', '1', 'N', 'V', 'Market-specific Authoriation Data \r\nIndicator'),
             ('9', '56-67', '12', 'N', 'V', 'Total Authoried Amount'),
             ('10b-1', '68-87', '20', 'AN', 'MSCAPN', 'Renter Name \r\nName\r\nAmerican Express Auto Rental Renter \r\nName\r\nFor MasterCard, Discover and American \r\nExpress, this is the name of the person who \r\nrented the vehicle.'),
             ('10b-2', '88-105', '18', 'AN', 'MSCAPN', 'Rental Return City \r\nReturn City\r\nAmerican Express Auto Rental Return City \r\nName\r\nFor MasterCard, Discover and American \r\nExpress, this is the name of the city to which \r\nthe vehicle will be returned.'),
             ('10a-1', '68-107', '40', 'AN', 'V', 'Visa Renter Name '),
             ('10b-3', '106-108', '3', 'AN', 'MSCAPN', 'Rental Return State/Country\r\nReturn State\r\nAmerican Express Auto Rental Return \r\nRegion Code\r\nCode used to identify the state, province, or \r\nregion to which the vehicle was returned.'),
             ('10a-2', '108', '1', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('11', '109-118', '10', 'AN', 'M, S', 'Return Location Identifier'),
             ('12', '119-120', '2', 'AN', 'MS', 'Program Code\r\nVehicle Program Code/Special Program \r\nCode\r\nCode used to identify characteristics of a \r\nrental program.\r\n\r\nVehicle Program Code is part of Sequence \r\nII of the Discover Network Vehicle Rental \r\nSupplemental Data Record.\r\n\r\nSpecial Program Code is part of Sequence \r\nIII of the Discover Network Vehicle Return \r\nSupplemental Data Record.'),
             ('13', '121-126', '6', 'N', 'M, SCAPN', 'Rental Return Date\r\nFormat MMDDYY\r\nAmerican Express Auto Rental Return \r\nDate\r\nDate the rented vehicle was returned \r\n(MMDDYY).'),
             ('14', '127-135', '9', 'N', 'VM, S', 'Daily Rental Rate\r\nRental Rate'),
             ('15', '136-144', '9', 'N', 'V, SM', 'Visa and Discover Weekly Rental Rate\r\nMasterCard  Rate per Mile\r\nFor Visa, MasterCard and Discover, this \r\nfield must be right-ustified.'),
             ('16', '145', '1', 'AN', 'M, SCAPN', 'Adusted Amount Indicator\r\nAmerican Express Auto Rental Audit \r\nAdustment Indicator\r\nCode used to indicate that an adustment \r\nwas made to a vehicle rental charge.\r\nPossible values  \r\nSpace - No additional charges or unknown\r\nA - \r\nDrop off charges\r\nB - \r\nDelivery charges\r\nC - \r\nParking expenses\r\nD - \r\nExtra hours\r\nE - \r\nViolations\r\nF-S - \r\nReserved for ISO use\r\nT-W - \r\nReserved for national use\r\nX - \r\nMultiple charges of the above types\r\nY - \r\nAdustment made, cardmember \r\nnotified\r\n - \r\nAdustment made, cardmember not \r\nnotified'),
             ('17', '146-154', '9', 'N', 'VM, SCAPN', 'Visa   Fuel Charges\r\nMasterCard and Discover Adusted \r\nAmount\r\nAmerican Express Auto Rental Audit \r\nAdustment Amount\r\nMonetary amount of any adustments made \r\nto a vehicle rental contract after the vehicle \r\nwas checked in. This monetary amount is \r\ngiven in the currency and decimaliation of \r\nthe First Presentment.'),
             ('18', '155', '1', 'AN', 'M, S', 'Insurance Indicator\r\nPossible values  \r\nY - \r\nInsurance was purchased by the \r\nrenter\r\nN - \r\nInsurance was not purchased by the \r\nrenter\r\nSpace - Value not provided'),
             ('19', '156-164', '9', 'N', 'V, MS', 'Insurance Charges\r\nInsurance Amount'),
             ('20', '165-166', '2', 'AN', 'VMCAPN', 'Visa  Car Class Code\r\nMasterCard Rental Class ID\r\nAmerican Express Auto Rental Vehicle \r\nClass Identifier\r\nCode used by CAPN to indicate the class of \r\nvehicle rented.\r\nPossible values  \r\n01 - \r\nMini\r\n02  - \r\nSubcompact\r\n03 - \r\nEconomy\r\n04 - \r\nCompact\r\n05 - \r\nMidsie\r\n06 - \r\nIntermediate\r\n07 - \r\nStandard\r\n08 - \r\nFull sie\r\n09 - \r\nLuxury\r\n10 - \r\nPremium\r\n11 - \r\nMinivan\r\n12 - \r\n12-passenger van\r\n13 - \r\nMoving van\r\n14 - \r\n15-passenger van\r\n15 - \r\nCargo van\r\n16 - \r\n12-foot truck\r\n17  - \r\n20-foot truck\r\n18 - \r\n24-foot truck\r\n19 - \r\n26-foot truck\r\n20 - \r\nMoped\r\n21 - \r\nStretch22  - \r\nRegular\r\n23 - \r\nUnique\r\n24 - \r\nExotic\r\n25 - \r\nSmall/medium truck\r\n26 - \r\nLarge truck\r\n27 - \r\nSmall SUV\r\n28  - \r\nMedium SUV\r\n29  - \r\nLarge SUV\r\n30  - \r\nExotic SUV\r\n31 - \r\nFour Wheel Drive\r\n32 - \r\nSpecial\r\n99 - \r\nMiscellaneous'),
             ('21', '167-175', '9', 'N', 'V', 'One-Way Drop-off Charges'),
             ('22', '176-179', '4', 'N', 'MSCAPN', 'Total Miles\r\nRental Distance\r\nAmerican Express Auto Rental Distance\r\nDistance traveled in the vehicle during the \r\nrental.'),
             ('23', '180-183', '4', 'N', 'M, S', 'Maximum Free Miles'),
             ('24', '184-188', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nPossible values  \r\nSpace - \r\nno extension record follows\r\nCARNT - another Car Rental Extension \r\nRecord follows - Visa only\r\nOPTIN - \r\na Car Rental Optional Extension \r\nRecord follows'),
             ('25', '189-190', '2', 'N', 'V, M', 'Days Rented'),
             ('26', '191', '1', 'AN', 'MS', 'Rental Rate Indicator\r\nTime Period\r\nMasterCard and Discover Indicates \r\nwhether the rental rate is for a daily, weekly, \r\nor monthly rental.\r\nPossible values  \r\nD - \r\nDaily\r\nW - \r\nWeekly\r\nM - \r\nMonthly\r\nSpace - \r\nNot known'),
             ('27', '192-209', '18', 'AN', 'M, SCAPN', 'Rental Location City\r\nCity from which the rental transaction \r\noriginated.\r\nAmerican Express Auto Rental Pickup City \r\nName\r\nCity from which the rental vehicle was \r\npicked up.'),
             ('28', '210-212', '3', 'AN', 'M,SCAPN', 'Rental Location State or Province\r\nCode for the state or province where the \r\nrental transaction originated.\r\nThis field cannot contain all spaces. It must \r\ncontain a valid state or province code.\r\nAmerican Express Auto Rental Pickup \r\nRegion Code\r\nCode used to identify the state, province, or \r\nregion from which the rental vehicle was \r\npicked up. '),
             ('29', '213-215', '3', 'AN', 'M,SCAPN', 'Rental Location Country\r\nCode for the country where the rental \r\ntransaction originated.\r\nThis field cannot contain all spaces. It must \r\ncontain a valid alphabetic ISO country code.\r\nAmerican Express Auto Rental Pickup \r\nCountry Code\r\nCode for the country in which the rental \r\nvehicle was picked up. '),
             ('30', '216', '1', 'AN', 'M', 'Tax Exempt Indicator\r\nCode that indicates if the goods or services \r\nare not subect to taxes.\r\nPossible values  \r\n0 - \r\nNot applicable\r\n1 - \r\nGoods or services are tax exempt'),
             ('31', '217-228', '12', 'N', 'S', 'Tax Amount'),
             ('32', '229-256', '28', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "mastercardRentalAgreementNumber": None,
        "mastercardCustomerServiceTelephone": None,
        "visaCarRentalAgreementNumber": None,
        "reservedForFutureUse4b-3": None,
        "noShowIndicator": None,
        "extraCharges": None,
        "checkoutDateMmddyy": None,
        "marketSpecificAuthoriationData": None,
        "totalAuthoriedAmount": None,
        "renterName": None,
        "rentalReturnCity": None,
        "visaRenterName": None,
        "rentalReturnStateCountry": None,
        "reservedForFutureUse10a-2": None,
        "returnLocationIdentifier": None,
        "programCode": None,
        "rentalReturnDate": None,
        "dailyRentalRate": None,
        "visaAndDiscoverWeeklyRentalRate": None,
        "adustedAmountIndicator": None,
        "visaFuelCharges": None,
        "insuranceIndicator": None,
        "insuranceCharges": None,
        "visaCarClassCode": None,
        "oneWayDropOffCharges": None,
        "totalMiles": None,
        "maximumFreeMiles": None,
        "extensionRecordIndicator": None,
        "daysRented": None,
        "rentalRateIndicator": None,
        "rentalLocationCity": None,
        "rentalLocationStateOrProvince": None,
        "rentalLocationCountry": None,
        "taxExemptIndicator": None,
        "taxAmount": None,
        "reservedForFutureUse32": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.mastercardRentalAgreementNumber,
        self.mastercardCustomerServiceTelephone,
        self.visaCarRentalAgreementNumber,
        self.reservedForFutureUse4b-3,
        self.noShowIndicator,
        self.extraCharges,
        self.checkoutDateMmddyy,
        self.marketSpecificAuthoriationData,
        self.totalAuthoriedAmount,
        self.renterName,
        self.rentalReturnCity,
        self.visaRenterName,
        self.rentalReturnStateCountry,
        self.reservedForFutureUse10a-2,
        self.returnLocationIdentifier,
        self.programCode,
        self.rentalReturnDate,
        self.dailyRentalRate,
        self.visaAndDiscoverWeeklyRentalRate,
        self.adustedAmountIndicator,
        self.visaFuelCharges,
        self.insuranceIndicator,
        self.insuranceCharges,
        self.visaCarClassCode,
        self.oneWayDropOffCharges,
        self.totalMiles,
        self.maximumFreeMiles,
        self.extensionRecordIndicator,
        self.daysRented,
        self.rentalRateIndicator,
        self.rentalLocationCity,
        self.rentalLocationStateOrProvince,
        self.rentalLocationCountry,
        self.taxExemptIndicator,
        self.taxAmount,
        self.reservedForFutureUse32 = (None)*39
        self.data = f.read(CarRentalExtensionRecord.LENGTH)
        super(CarRentalExtensionRecord, self).__init__()
        
class LodgingOptionalExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nA list of transaction codes can be found on \r\nthe Inquire Status Record (ISR) screen of \r\nthe TSYS Accounting (TSA) System.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator identifies this record \r\nas an Optional Extension Record.\r\nRequired value  OPTIN'),
             ('4', '17-41', '25', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('5', '42-53', '12', 'N', 'V', 'Parking Charges'),
             ('6', '54-65', '12', 'N', 'V', 'Movie Charges'),
             ('7', '66-77', '12', 'N', 'V', 'Business Center Charges'),
             ('8', '78-89', '12', 'N', 'V', 'Health Club Charges'),
             ('9', '90-101', '12', 'N', 'V', 'Mini Bar Charges'),
             ('10', '102-113', '12', 'N', 'V', 'Telephone Charges'),
             ('11', '114-125', '12', 'N', 'V', 'Other Charges'),
             ('12', '126-137', '12', 'N', 'V', 'Gift Shop Charges'),
             ('13', '138-142', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nPossible values  \r\nSpace - \r\nno extension record follows\r\nOPTIN - \r\nanother Lodging Optional \r\nExtension Record follows'),
             ('14', '143-154', '12', 'N', 'V', 'Laundry Charges'),
             ('15', '155-166', '12', 'N', 'V', 'Total Non-Room Charges'),
             ('16', '167-192', '26', 'AN', 'CAPN', 'Lodging Renter Name\r\nName of the person charged for the \r\nreservation and stay. This field can also \r\ncontain the name of the business entity \r\ncharged for the reservation and stay.\r\nThis field must be left-ustified. You can use \r\nspaces as filler.'),
             ('17', '193-256', '64', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "reservedForFutureUse4": None,
        "parkingCharges": None,
        "movieCharges": None,
        "businessCenterCharges": None,
        "healthClubCharges": None,
        "miniBarCharges": None,
        "telephoneCharges": None,
        "otherCharges": None,
        "giftShopCharges": None,
        "extensionRecordIndicator": None,
        "laundryCharges": None,
        "totalNonRoomCharges": None,
        "lodgingRenterName": None,
        "reservedForFutureUse17": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.reservedForFutureUse4,
        self.parkingCharges,
        self.movieCharges,
        self.businessCenterCharges,
        self.healthClubCharges,
        self.miniBarCharges,
        self.telephoneCharges,
        self.otherCharges,
        self.giftShopCharges,
        self.extensionRecordIndicator,
        self.laundryCharges,
        self.totalNonRoomCharges,
        self.lodgingRenterName,
        self.reservedForFutureUse17 = (None)*17
        self.data = f.read(LodgingOptionalExtensionRecord.LENGTH)
        super(LodgingOptionalExtensionRecord, self).__init__()
        
class POSCheckServiceExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nEach record must contain a sequence \r\nnumber to identify its position within the \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nThe Transaction code identifies the type of \r\nrecord being transmitted.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator shows that this is a \r\nCheck extension record.\r\nRequired value  CHECK'),
             ('4', '17-35', '19', 'N', 'V', 'Checking Account Number'),
             ('5', '36-44', '9', 'A/N', 'V', 'ABA/RTN'),
             ('6', '45-59', '15', 'N', 'V', 'Check Number'),
             ('7', '60-61', '2', 'N', 'V', 'Check Service Option\r\nCO- Conversion Only\r\nCV- Conversion w/ Verification\r\nCG- Conversion w/Guarantee'),
             ('8', '62-66', '5', 'A/N', 'V', 'Check Service Program\r\nSMS-Online SMS\r\n3PACH- 3rd Party ACH'),
             ('9', '67-72', '6', 'A/N', 'V', 'Receiving Institution ID (RIID)'),
             ('10', '73-85', '13', 'A/N', 'V', 'Internal Merchant Batch Key'),
             ('11', '86-100', '15', 'A/N', 'TSYS Acquiring Solutions', 'Individual Merchant ID'),
             ('12', '101-103', '3', 'A/N', 'TSYS Acquiring Solutions', 'Sec Code'),
             ('13', '104-113', '10', 'N', 'TSYS Acquiring Solutions', 'Phone Number'),
             ('14', '114', '1', 'A/N', 'TSYS Acquiring Solutions', 'Account Type Indicator'),
             ('15', '115-136', '22', 'A/N', 'TSYS Acquiring Solutions', 'Individual Name'),
             ('16', '137', '1', 'A/N', 'TSYS Acquiring Solutions', 'Payment Type'),
             ('17', '138-150', '13', 'A/N', 'TSYS Acquiring Solutions', 'Terminal City'),
             ('18', '151-152', '2', 'A/N', 'TSYS Acquiring Solutions', 'Terminal State'),
             ('19', '153-154', '2', 'A/N', 'TSYS Acquiring Solutions', 'Discretionary Data'),
             ('20', '155-251', '97', 'A/N', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('21', '252-256', '5', 'A/N', 'TSYS Acquiring Solutions', 'Reserved for future use'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "checkingAccountNumber": None,
        "abaRtn": None,
        "checkNumber": None,
        "checkServiceOption": None,
        "checkServiceProgram": None,
        "receivingInstitutionIdRiid": None,
        "internalMerchantBatchKey": None,
        "individualMerchantId": None,
        "secCode": None,
        "phoneNumber": None,
        "accountTypeIndicator": None,
        "individualName": None,
        "paymentType": None,
        "terminalCity": None,
        "terminalState": None,
        "discretionaryData": None,
        "reservedForFutureUse20": None,
        "reservedForFutureUse21": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.checkingAccountNumber,
        self.abaRtn,
        self.checkNumber,
        self.checkServiceOption,
        self.checkServiceProgram,
        self.receivingInstitutionIdRiid,
        self.internalMerchantBatchKey,
        self.individualMerchantId,
        self.secCode,
        self.phoneNumber,
        self.accountTypeIndicator,
        self.individualName,
        self.paymentType,
        self.terminalCity,
        self.terminalState,
        self.discretionaryData,
        self.reservedForFutureUse20,
        self.reservedForFutureUse21 = (None)*21
        self.data = f.read(POSCheckServiceExtensionRecord.LENGTH)
        super(POSCheckServiceExtensionRecord, self).__init__()
        
class DirectMarketingExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nA list of transaction codes can be found on \r\nthe Inquire Status Record (ISR) screen of \r\nthe TSYS Accounting (TSA) System.\r\nNOTEThis field should contain the same \r\ninformation as the Transaction Code field in the \r\nFinancial record.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator identifies this record \r\nas a Direct Marketing Extension Record.\r\nRequired value  DIRCT'),
             ('4', '17-41', '25', 'AN', 'V', 'Direct Marketing Order Number (Purchase \r\nIdentifier)'),
             ('5', '42', '1', 'N', 'V', 'Address Verification Service (AVS) \r\nResponse Code'),
             ('6', '43-54', '12', 'N', 'V', 'Total Authoried Amount'),
             ('7', '55-67', '13', 'AN', 'V', 'Merchants Customer Service Telephone \r\nNumber\r\nIf provided, this customer service telephone \r\nnumber will only be used to overlay the \r\nmerchant city field on the PV report and \r\nin the outgoing Association file. It will not \r\nsatisfy MasterCards customer service phone \r\nnumber requirement for MO/TO and \r\nRecurring Payment transactions (use \r\nEXT or the MAS Inquire Merchant \r\nAccount screen).  \r\nThe format for this field is xxx-xxxxxxx'),
             ('8', '68-69', '2', 'AN', 'V', 'Multiple Clearing Sequence Number\r\nIf a merchant is billing a cardholder in \r\ninstallments, this field contains the number \r\nof the current installment.'),
             ('9', '70-71', '2', 'AN', 'V', 'Multiple Clearing Sequence Count\r\nIf a merchant is billing a cardholder in \r\ninstallments, this field contains the total \r\nnumber of installments.\r\nIf used, the Installment Billing Number and \r\nCount fields will appear at the end of the \r\nMerchant DBA name field. For example, 2 \r\nof 5 would indicate the current charge is \r\nthe second installment out of a total of five.'),
             ('10', '72-76', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nPossible values  \r\nSpace - \r\nno extension record follows\r\nPURC1 - \r\na Purchasing Card 1 Extension \r\nRecord follows'),
             ('11', '77-256', '180', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "directMarketingOrderNumberPurchase": None,
        "addressVerificationServiceAvs": None,
        "totalAuthoriedAmount": None,
        "merchantsCustomerServiceTelephone": None,
        "multipleClearingSequenceNumber": None,
        "multipleClearingSequenceCount": None,
        "extensionRecordIndicator": None,
        "reservedForFutureUse": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.directMarketingOrderNumberPurchase,
        self.addressVerificationServiceAvs,
        self.totalAuthoriedAmount,
        self.merchantsCustomerServiceTelephone,
        self.multipleClearingSequenceNumber,
        self.multipleClearingSequenceCount,
        self.extensionRecordIndicator,
        self.reservedForFutureUse = (None)*11
        self.data = f.read(DirectMarketingExtensionRecord.LENGTH)
        super(DirectMarketingExtensionRecord, self).__init__()
        
class ElectronicInvoiceTransactionData(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nNumber that identifies the position of the \r\nrecord within the file.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nCode that identifies the type of record being \r\ntransmitted.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nIndicates an Electronic Invoice Transaction \r\nData extension record EINTR.'),
             ('4', '17-41', '25', 'N', 'M', 'Invoice Number\r\nIndicates the number of the electronic \r\ninvoice.'),
             ('5', '42-47', '6', 'N', 'M', 'Invoice Date\r\nIndicates the date of the electronic invoice \r\n(YYMMDD).'),
             ('6', '48-53', '6', 'N', 'M', 'Invoice Creation Date\r\nIndicates the date the electronic invoice was \r\ncreated (YYMMDD).'),
             ('7', '54-59', '6', 'N', 'M', 'Invoice Creation Time\r\nIndicates the time the electronic invoice was \r\ncreated (HHMMSS).'),
             ('8', '60-251', '192', 'AN', 'M', 'Reserved for future use.'),
             ('9', '252-256', '5', 'A', 'M', 'Extension Record Indicator\r\nIndicates an electronic invoice party \r\ninformation record is to follow.\r\nPossible value  EINPR'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "invoiceNumber": None,
        "invoiceDate": None,
        "invoiceCreationDate": None,
        "invoiceCreationTime": None,
        "reservedForFutureUse": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.invoiceNumber,
        self.invoiceDate,
        self.invoiceCreationDate,
        self.invoiceCreationTime,
        self.reservedForFutureUse,
        self.extensionRecordIndicator = (None)*9
        self.data = f.read(ElectronicInvoiceTransactionData.LENGTH)
        super(ElectronicInvoiceTransactionData, self).__init__()
        
class ElectronicInvoicePartyInformation(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nNumber that identifies the position of the \r\nrecord within the file.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nCode that identifies the type of record being \r\ntransmitted.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nIndicates an Electronic Invoice Party \r\nInformation extension record EINPR.'),
             ('4', '17-18', '2', 'AN', 'M', 'Party ID\r\nCode that identifies the various parties on an \r\ninvoice.'),
             ('5', '19-58', '40', 'AN', 'M', 'Party Name\r\nIndicates the name of the party identified on \r\nthe invoice.'),
             ('6', '59-98', '40', 'AN', 'M', 'Party Address\r\nIndicates the address of the party identified \r\non the invoice.'),
             ('7', '99-138', '40', 'AN', 'M', 'Party Supplemental Data Description 1\r\nContains information about the party \r\nidentified on the invoice.'),
             ('8', '139-178', '40', 'AN', 'M', 'Party Supplemental Data Description 2\r\nContains information about the party \r\nidentified on the invoice.'),
             ('9', '179-251', '73', 'AN', 'M', 'Reserved for future use.'),
             ('10', '252-256', '5', 'A', 'M', 'Extension Record Indicator\r\nIndicates an electronic invoice party \r\ninformation record is to follow.\r\nPossible value  EINPR'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "partyId": None,
        "partyName": None,
        "partyAddress": None,
        "partySupplementalDataDescription1": None,
        "partySupplementalDataDescription2": None,
        "reservedForFutureUse": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.partyId,
        self.partyName,
        self.partyAddress,
        self.partySupplementalDataDescription1,
        self.partySupplementalDataDescription2,
        self.reservedForFutureUse,
        self.extensionRecordIndicator = (None)*10
        self.data = f.read(ElectronicInvoicePartyInformation.LENGTH)
        super(ElectronicInvoicePartyInformation, self).__init__()
        
class EntertainmentTicketingExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nNumber that identifies the position of this \r\nrecord within the file.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nCode that identifies the type of transaction \r\nbeing transmitted.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nCode that indicates the record type.\r\nPossible value  ENT1'),
             ('4', '17-46', '30', 'AN', 'CAPN', 'Event Name\r\nName of the event.\r\nIf a value is entered in this field, the value \r\nmust be left-ustified. The field can be filled \r\nwith spaces.'),
             ('5', '47-52', '6', 'N', 'CAPN', 'Event Date\r\nDate of the event (MMDDYY).'),
             ('6', '53-64', '12', 'N', 'CAPN', 'Event Individual Ticket Price Amount\r\nPrice of one ticket to the event.\r\nThis field must be right-ustified. It can be \r\nfilled with eroes.'),
             ('7', '65-68', '4', 'N', 'CAPN', 'Event Ticket Quantity\r\nNumber of tickets purchased.\r\nThis field must be right-ustified. It can be \r\nfilled with eroes.'),
             ('8', '69-108', '40', 'AN', 'CAPN', 'Event Location\r\nLocation of the event.\r\nThis field must be left-ustified. It can be \r\nfilled with spaces.'),
             ('9', '109-111', '3', 'AN', 'CAPN', 'Event Region Code\r\nThe region code that corresponds to the \r\nstate, province, or other country subdivision \r\nwhere the even took place.\r\nNOTEIf the Event Region Code field is \r\npopulated, the Event Country Code field must also \r\nbe populated, and vice versa. If this field is not \r\nused, it must be filled with spaces.  \r\nThis field must be left-ustified and be in \r\nupper case.'),
             ('10', '112-114', '3', 'AN', 'CAPN', 'Event Country Code\r\nCountry code of the location where the \r\nevent took place.\r\nNOTE If the Event Country Code field is \r\npopulated, the Event Region Code field must also \r\nbe populated, and vice versa. If this field is not \r\nused, it must be filled with spaces.\r\nThis field must be in upper case.'),
             ('11', '115-251', '138', 'B', 'TSYS Acquiring Solutions', 'Reserved for future use.'),
             ('12', '252-256', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nCode that indicates if another extension \r\nrecord follows this record. \r\nPossible value  Blank (No extension record \r\nfollows).'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "eventName": None,
        "eventDate": None,
        "eventIndividualTicketPriceAmount": None,
        "eventTicketQuantity": None,
        "eventLocation": None,
        "eventRegionCode": None,
        "eventCountryCode": None,
        "reservedForFutureUse": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.eventName,
        self.eventDate,
        self.eventIndividualTicketPriceAmount,
        self.eventTicketQuantity,
        self.eventLocation,
        self.eventRegionCode,
        self.eventCountryCode,
        self.reservedForFutureUse,
        self.extensionRecordIndicator = (None)*12
        self.data = f.read(EntertainmentTicketingExtensionRecord.LENGTH)
        super(EntertainmentTicketingExtensionRecord, self).__init__()
        
class FleetService1ExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nA list of transaction codes can be found on \r\nthe Inquire Status Record (ISR) screen of \r\nthe TSYS Accounting (TSA) System.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator identifies this record \r\nas a Fleet Service 1 Extension Record.\r\nRequired value  FLEET'),
             ('4', '17-20', '4', 'N', 'MS', 'Oil Company Brand Name\r\nMotor Oil Company Brand Name Code'),
             ('5', '21-50', '30', 'AN', 'M', 'Merchant Street Address'),
             ('6', '51-59', '9', 'AN', 'M', 'Merchant Postal/IP code  Extension'),
             ('7', '60-63', '4', 'N', 'M', 'Purchase Time\r\nFormat  HHMM (using 24-hour clock)'),
             ('8', '64', '1', 'AN', 'VMS', 'Visa Service Type\r\nMasterCard Motor Fuel Service Type\r\nDiscover Fleet Motor Fuel Service Type\r\nCode that indicates if full or self service was \r\nassociated with the transaction.\r\nPossible values  \r\nBlank - Not reported (This is the default \r\nvalue)\r\n1 - \r\nSelf service\r\n2 - \r\nFull service\r\n3 - \r\nOnly non-fuel products purchased'),
             ('9', '65-67', '3', 'AN', 'V M', 'Visa Fuel Type\r\nFor Visa, this field must be left-ustified and \r\nspace-filled. Visa uses only 2 characters for \r\nthe Fuel Type\r\nMasterCard Motor Fuel Product Code\r\nValid value ranges\r\n001-009\r\n011-029\r\n100-102\r\n150-150\r\n200-203'),
             ('10', '68-79', '12', 'N', 'V, M', 'Motor Fuel Unit Price\r\nFor Visa transactions, this field must be \r\nright-ustified with four positions to the \r\nright of the implied decimal.\r\nFor MasterCard transactions, this field must \r\nbe right-ustified with three positions to the \r\nright of the implied decimal.'),
             ('11', '80', '1', 'AN', 'V, M,S', 'Visa and Discover Unit of Measure\r\nMasterCard Motor Fuel Unit of Measure\r\nCode that indicates the unit of measure for \r\nthe fuel purchased. \r\nPossible values  for Visa\r\nL - \r\nLiter\r\nG - \r\nU.S. Gallon\r\nI - \r\nImperial gallon\r\nK - \r\nKilo\r\nP - \r\nPound\r\nPossible values  for MasterCard and Discover\r\nSpace - \r\nNot applicable\r\n1 - \r\nGallon\r\n2 - \r\nLiter\r\n3 - \r\nPound\r\n4 - \r\nKilo\r\n5 - \r\nImperial gallon'),
             ('12', '81-92', '12', 'N', 'V, M, S', 'Motor Fuel Quantity\r\nFor MasterCard transactions, this field must \r\nbe right-ustified with two positions to the \r\nright of the implied decimal.'),
             ('13', '93-104', '12', 'N', 'V, M', 'Gross Fuel Sale Amount'),
             ('14', '105-116', '12', 'N', 'V', 'Net Fuel Price'),
             ('15', '117-128', '12', 'N', 'V', 'Net Non-Fuel Price'),
             ('16', '129-135', '7', 'N', 'V, M, S', 'Visa and MasterCard Odometer Reading\r\nDiscover Odometer\r\nThis field must be right-ustified and ero-\r\nfilled.'),
             ('17', '136-152', '17', 'AN', 'MS', 'Vehicle Number\r\nVIN Registration Number'),
             ('18', '153-169', '17', 'AN', 'VMS', 'Visa  Customer Code/Customer Reference \r\nIdentifier (CRI)\r\nMasterCard  Driver Number/ID \r\nFor MasterCard, this field is used to house \r\nthe identification number assigned to the \r\ndriver.\r\nFleet Driver/Other ID Numbers\r\nIdentification number assigned to the driver \r\nand used at the point of interaction.'),
             ('19', '170', '1', 'N', 'VM', 'Visa Type of Purchase\r\nMasterCard  Product Type Code'),
             ('20', '171-175', '5', 'N', 'MS', 'Coupon/Discount Amount\r\nFleet Amount Bottom Line Discount'),
             ('21', '176-187', '12', 'N', 'VMS', 'Visa  State Fuel Tax Amount\r\nMasterCard Tax Amount 1\r\nDiscover Fleet Amount Total Tax'),
             ('22', '188-199', '12', 'N', 'M', 'MasterCard Tax Amount 2'),
             ('23', '200-211', '12', 'N', 'V', 'Local Fuel Tax Amount'),
             ('24', '212-215', '4', 'N', 'V', 'Value-added tax (VAT) Rate'),
             ('25', '216-217', '2', 'AN', 'V', 'Product Code 1'),
             ('26', '218-219', '2', 'AN', 'V', 'Product Code 2'),
             ('27', '220-221', '2', 'AN', 'V', 'Product Code 3'),
             ('28', '222-223', '2', 'AN', 'V', 'Product Code 4'),
             ('29', '224-225', '2', 'AN', 'V', 'Product Code 5'),
             ('30', '226-227', '2', 'AN', 'V', 'Product Code 6'),
             ('31', '228-229', '2', 'AN', 'V', 'Product Code 7'),
             ('32', '230-231', '2', 'AN', 'V', 'Product Code 8'),
             ('33', '232-243', '12', 'N', 'VM', 'Visa  Local Sales Tax\r\nMasterCard  Tax Amount 3'),
             ('34', '244', '1', 'AN', 'V', 'Local Tax Included'),
             ('35', '245-253', '9', 'N', 'V', 'Gross Non-fuel Price'),
             ('36', '254', '1', 'AN', 'V', 'Miscellaneous Fuel Tax Exemption Status'),
             ('37', '255', '1', 'AN', 'V', 'Miscellaneous Non-fuel Tax Exemption \r\nStatus'),
             ('38', '256', '1', 'AN', 'V, M', 'Extension Record Indicator\r\nPossible values  \r\nSpace - \r\nno extension record follows\r\n2 - \r\nA Fleet Service 2 Extension Record \r\nfollows\r\nP - \r\nPurchasing Card Format 1 \r\nExtension record follows '))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "oilCompanyBrandName": None,
        "merchantStreetAddress": None,
        "merchantPostalIpCodeExtension": None,
        "purchaseTime": None,
        "visaServiceType": None,
        "visaFuelType": None,
        "motorFuelUnitPrice": None,
        "visaAndDiscoverUnitOfMeasure": None,
        "motorFuelQuantity": None,
        "grossFuelSaleAmount": None,
        "netFuelPrice": None,
        "netNonFuelPrice": None,
        "visaAndMastercardOdometerReading": None,
        "vehicleNumber": None,
        "visaCustomerCodeCustomerReference": None,
        "visaTypeOfPurchase": None,
        "couponDiscountAmount": None,
        "visaStateFuelTaxAmount": None,
        "mastercardTaxAmount2": None,
        "localFuelTaxAmount": None,
        "valueAddedTaxVatRate": None,
        "productCode1": None,
        "productCode2": None,
        "productCode3": None,
        "productCode4": None,
        "productCode5": None,
        "productCode6": None,
        "productCode7": None,
        "productCode8": None,
        "visaLocalSalesTax": None,
        "localTaxIncluded": None,
        "grossNonFuelPrice": None,
        "miscellaneousFuelTaxExemptionStatus": None,
        "miscellaneousNonFuelTaxExemption": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.oilCompanyBrandName,
        self.merchantStreetAddress,
        self.merchantPostalIpCodeExtension,
        self.purchaseTime,
        self.visaServiceType,
        self.visaFuelType,
        self.motorFuelUnitPrice,
        self.visaAndDiscoverUnitOfMeasure,
        self.motorFuelQuantity,
        self.grossFuelSaleAmount,
        self.netFuelPrice,
        self.netNonFuelPrice,
        self.visaAndMastercardOdometerReading,
        self.vehicleNumber,
        self.visaCustomerCodeCustomerReference,
        self.visaTypeOfPurchase,
        self.couponDiscountAmount,
        self.visaStateFuelTaxAmount,
        self.mastercardTaxAmount2,
        self.localFuelTaxAmount,
        self.valueAddedTaxVatRate,
        self.productCode1,
        self.productCode2,
        self.productCode3,
        self.productCode4,
        self.productCode5,
        self.productCode6,
        self.productCode7,
        self.productCode8,
        self.visaLocalSalesTax,
        self.localTaxIncluded,
        self.grossNonFuelPrice,
        self.miscellaneousFuelTaxExemptionStatus,
        self.miscellaneousNonFuelTaxExemption,
        self.extensionRecordIndicator = (None)*38
        self.data = f.read(FleetService1ExtensionRecord.LENGTH)
        super(FleetService1ExtensionRecord, self).__init__()
        
class FleetService2ExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nA list of transaction codes can be found on \r\nthe Inquire Status Record (ISR) screen of \r\nthe TSYS Accounting (TSA) System.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator identifies this record \r\nas a Fleet Service 2 Extension Record.\r\nRequired value  FLEE2'),
             ('4', '17-19', '3', 'N', 'M', 'Product Code'),
             ('5a', '20-23', '4', 'AN', 'V', 'Fuel Brand'),
             ('5b', '24-28', '5', 'AN', 'V', 'Fuel Transaction Validation Results'),
             ('5c', '29', '1', 'AN', 'V', 'Fuel Acceptance Mode'),
             ('5d', '30-49', '20', 'AN', 'V', 'Driver Identification'),
             ('5', '20-54', '35', 'AN', 'M', 'Item Description'),
             ('5e', '50-59', '10', 'AN', 'V', 'Job Number'),
             ('6', '55-59', '5', 'AN', 'M', 'Item Quantity'),
             ('7', '60-62', '3', 'AN', 'VM', 'Visa  Item Sequence Number\r\nMasterCard  Item Unit of Measure'),
             ('8', '63-71', '9', 'N', 'M', 'Extended Item Amount\r\nThis field cannot contain all eroes or all \r\nspaces.'),
             ('9', '72', '1', 'AN', 'M', 'Discount Indicator'),
             ('10', '73-81', '9', 'AN', 'M', 'Discount Amount'),
             ('11', '82', '1', 'AN', 'M', 'Net/Gross Indicator for Extended Item \r\nAmount\r\nThis field indicates whether tax was \r\nincluded in the Extended Item Amount \r\n(field 8).\r\nPossible values  \r\nY - \r\ntax included\r\nN - \r\ntax not included'),
             ('12', '83-87', '5', 'AN', 'M', 'Tax Rate Applied'),
             ('13', '88-91', '4', 'AN', 'M', 'Tax Type Applied'),
             ('14', '92-100', '9', 'AN', 'M', 'Tax Amount'),
             ('13a', '88-101', '14', 'AN', 'V', 'Vehicle Registration Number'),
             ('15', '101', '1', 'AN', 'M', 'Debit/Credit Indicator'),
             ('16', '102-116', '15', 'AN', 'VM', 'Visa  Message Identifier\r\nMasterCard  Alternate Tax Identifier'),
             ('17', '117', '1', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nPossible values  \r\nSpace - \r\nno extension record follows\r\n2 - \r\nanother Fleet Service 2 Extension \r\nRecord follows\r\nP - \r\nPurchasing Card Format 1 \r\nExtension record follows '),
             ('18', '118', '1', 'AN', 'V', 'Federal Excise Tax Exemption Status (Non-\r\nFuel)\r\nPossible values  \r\n0 - \r\nnot exempt\r\n1 - \r\nexempt'),
             ('19', '119-130', '12', 'N', 'V', 'Federal Non-Fuel Excise Tax'),
             ('20', '131', '1', 'AN', 'V', 'Federal Fuel Tax Exemption Status\r\nPossible values  \r\n0 - \r\nnot exempt\r\n1 - \r\nexempt'),
             ('21', '132-143', '12', 'N', 'V', 'Federal Fuel Excise Tax'),
             ('22', '144', '1', 'AN', 'V', 'State Motor Fuel Tax Exemption Status\r\nPossible values  \r\n0 - \r\nnot exempt\r\n1 - \r\nexempt'),
             ('23', '145-156', '12', 'N', 'V', 'State Motor Fuel Tax'),
             ('24', '157', '1', 'AN', 'V', 'County Fuel Sales Tax Exemption Status\r\nPossible values  \r\n0 - \r\nnot exempt\r\n1 - \r\nexempt'),
             ('25', '158-169', '12', 'N', 'V', 'County Fuel Sales Tax'),
             ('26', '170', '1', 'AN', 'V', 'State and Local Sales Tax Exemption Status \r\n(Non-Fuel)\r\nPossible values  \r\n0 - \r\nnot exempt\r\n1 - \r\nexempt'),
             ('27', '171-182', '12', 'N', 'V', 'State and Local Sales Tax (Non-Fuel)'),
             ('28', '183', '1', 'AN', 'V', 'County Motor Fuel Tax Exemption Status\r\nPossible values  \r\n0 - \r\nnot exempt\r\n1 - \r\nexempt'),
             ('29', '184-195', '12', 'N', 'V', 'County Motor Fuel Tax'),
             ('30', '196', '1', 'AN', 'V', 'City Sales Fuel Tax Exemption Status\r\nPossible values  \r\n0 - \r\nnot exempt\r\n1 - \r\nexempt'),
             ('31', '197-208', '12', 'N', 'V', 'City Sales Fuel Tax'),
             ('32', '209', '1', 'AN', 'V', 'City Motor Fuel Tax Exemption Status\r\nPossible values  \r\n0 - \r\nnot exempt\r\n1 - \r\nexempt'),
             ('33', '210-221', '12', 'N', 'V', 'City Motor Fuel Tax'),
             ('34', '222', '1', 'AN', 'V', 'Secondary State Fuel Tax Exemption Status\r\nPossible values  \r\n0 - \r\nnot exempt\r\n1 - \r\nexempt'),
             ('35', '223-234', '12', 'N', 'V', 'Secondary State Fuel Tax'),
             ('36', '235', '1', 'AN', 'V', 'Reimbursement Attribute Code'),
             ('37', '236', '1', 'AN', 'V', 'Federal Sales Tax Exemption Status\r\nPossible values  \r\n0 - \r\nnot exempt\r\n1 - \r\nexempt'),
             ('38', '237-248', '12', 'N', 'V', 'Federal Sales Tax'),
             ('39', '249-256', '8', 'AN', 'V', 'Fleet Number'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "productCode": None,
        "fuelBrand": None,
        "fuelTransactionValidationResults": None,
        "fuelAcceptanceMode": None,
        "driverIdentification": None,
        "itemDescription": None,
        "jobNumber": None,
        "itemQuantity": None,
        "visaItemSequenceNumber": None,
        "extendedItemAmount": None,
        "discountIndicator": None,
        "discountAmount": None,
        "netGrossIndicatorForExtendedItem": None,
        "taxRateApplied": None,
        "taxTypeApplied": None,
        "taxAmount": None,
        "vehicleRegistrationNumber": None,
        "debitCreditIndicator": None,
        "visaMessageIdentifier": None,
        "extensionRecordIndicator": None,
        "federalExciseTaxExemptionStatusNon": None,
        "federalNonFuelExciseTax": None,
        "federalFuelTaxExemptionStatus": None,
        "federalFuelExciseTax": None,
        "stateMotorFuelTaxExemptionStatus": None,
        "stateMotorFuelTax": None,
        "countyFuelSalesTaxExemptionStatus": None,
        "countyFuelSalesTax": None,
        "stateAndLocalSalesTaxExemptionStatus": None,
        "stateAndLocalSalesTaxNonFuel": None,
        "countyMotorFuelTaxExemptionStatus": None,
        "countyMotorFuelTax": None,
        "citySalesFuelTaxExemptionStatus": None,
        "citySalesFuelTax": None,
        "cityMotorFuelTaxExemptionStatus": None,
        "cityMotorFuelTax": None,
        "secondaryStateFuelTaxExemptionStatus": None,
        "secondaryStateFuelTax": None,
        "reimbursementAttributeCode": None,
        "federalSalesTaxExemptionStatus": None,
        "federalSalesTax": None,
        "fleetNumber": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.productCode,
        self.fuelBrand,
        self.fuelTransactionValidationResults,
        self.fuelAcceptanceMode,
        self.driverIdentification,
        self.itemDescription,
        self.jobNumber,
        self.itemQuantity,
        self.visaItemSequenceNumber,
        self.extendedItemAmount,
        self.discountIndicator,
        self.discountAmount,
        self.netGrossIndicatorForExtendedItem,
        self.taxRateApplied,
        self.taxTypeApplied,
        self.taxAmount,
        self.vehicleRegistrationNumber,
        self.debitCreditIndicator,
        self.visaMessageIdentifier,
        self.extensionRecordIndicator,
        self.federalExciseTaxExemptionStatusNon,
        self.federalNonFuelExciseTax,
        self.federalFuelTaxExemptionStatus,
        self.federalFuelExciseTax,
        self.stateMotorFuelTaxExemptionStatus,
        self.stateMotorFuelTax,
        self.countyFuelSalesTaxExemptionStatus,
        self.countyFuelSalesTax,
        self.stateAndLocalSalesTaxExemptionStatus,
        self.stateAndLocalSalesTaxNonFuel,
        self.countyMotorFuelTaxExemptionStatus,
        self.countyMotorFuelTax,
        self.citySalesFuelTaxExemptionStatus,
        self.citySalesFuelTax,
        self.cityMotorFuelTaxExemptionStatus,
        self.cityMotorFuelTax,
        self.secondaryStateFuelTaxExemptionStatus,
        self.secondaryStateFuelTax,
        self.reimbursementAttributeCode,
        self.federalSalesTaxExemptionStatus,
        self.federalSalesTax,
        self.fleetNumber = (None)*45
        self.data = f.read(FleetService2ExtensionRecord.LENGTH)
        super(FleetService2ExtensionRecord, self).__init__()
        
class GeneralExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nIdentifies the records position within the \r\ntransmission file.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nA list of transaction codes can be found on \r\nthe Inquire Status Record (ISR) screen of \r\nthe TSYS Accounting (TSA) System.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nIdentifies this record as a General Extension \r\nRecord.\r\nRequired value  EXT'),
             ('4', '17-28', '12', 'AN', 'M', 'Point of Service (POS) Data Code\r\nConsists of 12 subfields that identify point-\r\nof-interaction environment conditions.\r\nSubfield 1 - Card Data Input Capability\r\nPossible values  \r\n0 - \r\nUnknown, data not available\r\n1 - \r\nManual, no terminal\r\n2 - \r\nMagnetic stripe reader\r\n4 - \r\nOptical character reader\r\n5 - \r\nIntegrated circuit card (ICC) reader\r\n6 - \r\nKey entry\r\nA - \r\nContactless mag stripe reader\r\nB - \r\nMagnetic stripe reader and key \r\nentry\r\nC - \r\nMag stripe reader, ICC reader and \r\nkey entry\r\nD - \r\nMag stripe reader and ICC reader\r\nE - \r\nICC reader and key entry\r\nM - \r\nContactless chip reader\r\nV - \r\nOther\r\nSubfield 2 - Cardholder Authentication \r\nCapability\r\nPossible values  \r\n0 - \r\nNo electronic authentication \r\ncapability\r\n1 - \r\nPIN entry capability\r\n2 - \r\nElectronic signature analysis \r\ncapability\r\n5 - \r\nElectronic authentication capability \r\nis inoperative\r\n6 - \r\nOther\r\n9 - \r\nUnknown, data not available\r\nSubfield 3 - Card Capture Capability\r\nPossible values  \r\n0 - \r\nNo capture capability\r\n1 - \r\nCard capture capability\r\n9 - \r\nUnknown, data not availableSubfield 4 - Terminal Operating \r\nEnvironment\r\nPossible values  \r\n0 - \r\nNo terminal used\r\n1 - \r\nOn card acceptor premises, \r\nattended terminal\r\n2 - \r\nOn card acceptor premises, \r\nunattended terminal\r\n3 - \r\nOff card acceptor premises, \r\nattended\r\n4 - \r\nOff card acceptor premises, \r\nunattended\r\n5 - \r\nOn cardholder premises, \r\nunattended\r\n6 - \r\nOff cardholder premises, \r\nunattended\r\n9 - \r\nUnknown, data not available\r\nSubfield 5 - Cardholder Present Data\r\nPossible values  \r\n0 - \r\nCardholder present\r\n1 - \r\nCardholder not present, unspecified\r\n2 - \r\nCardholder not present, \r\nmail/facsimile transaction\r\n3 - \r\nCardholder not present, phone \r\norder\r\n4 - \r\nCardholder not present, standing \r\norder/recurring transaction\r\n5 - \r\nCardholder not present, electronic \r\norder\r\n9 - \r\nUnknown, data not available\r\nSubfield 6 - Card Present Data\r\nPossible values  \r\n0 - \r\nCard not present\r\n1 - \r\nCard present\r\n9 - \r\nUnknown, data not available\r\nX - \r\nAMEX contactless transactions, \r\nincluding ExpressPaySubfield 7 - Card Data Input Mode\r\nPossible values  \r\n0 - \r\nUnknown, data not available\r\n1 - \r\nManual, no terminal\r\n2 - \r\nMagnetic stripe reader\r\n6 - \r\nKey entered\r\n9 - \r\nTechnical fallback - transaction \r\ninitiated as chip card but was \r\nprocessed using an alternative \r\ntechnology (such as magnetic \r\nstripe)\r\nA - \r\nPAN auto-entry via contactless \r\nmagnetic stripe\r\nB - \r\nMagnetic stripe reader, track data \r\ncaptured and passed unaltered\r\nC - \r\nOnline Chip\r\nF - \r\nOffline Chip\r\nM - \r\nPAN auto-entry via contactless \r\nM/Chip\r\nR - \r\nPAN entry via electronic \r\ncommerce, including remote chip\r\nS - \r\nElectronic commerce\r\nT - \r\nPAN auto entry via server (issuer, \r\naquirer, or third party vendor \r\nsystem)\r\nSubfield 8 - Cardholder Authentication \r\nMethod\r\nPossible values  \r\n0 - \r\nNot authenticated\r\n1 - \r\nPIN\r\n2 - \r\nElectronic signature analysis\r\n5 - \r\nManual signature verification\r\n6 - \r\nOther manual verification\r\n9 - \r\nUnknown, data not available\r\nS - \r\nOther systematic verification\r\nSubfield 9 - Cardholder Authentication \r\nEntity\r\nPossible values  \r\n0 - \r\nNot authenticated\r\n1 - \r\nICC - offline PIN\r\n2 - \r\nCard Acceptance Device\r\n3 - \r\nAuthoriing Agent - Online PIN4 - \r\nMerchant/card acceptor - signature\r\n5 - \r\nOther\r\n9 - \r\nUnknown, data not available\r\nSubfield 10 - Card Data Output Capability\r\nPossible values  \r\n0 - \r\nUnknown, data not available\r\n1 - \r\nNone\r\n2 - \r\nMagnetic stripe write\r\n3 - \r\nICC\r\nS - \r\nOther\r\nSubfield 11 - Terminal Data Output \r\nCapability\r\nPossible values  \r\n0 - \r\nUnknown, data not available\r\n1 - \r\nNone\r\n2 - \r\nPrinting capability only\r\n3 - \r\nDisplay capability only\r\n4 - \r\nPrinting and display capability\r\nSubfield 12 - PIN Capture Capability\r\nPossible values  \r\n0 - \r\nNo PIN capture capability\r\n1 - \r\nUnknown, data not available\r\n2 - \r\nReserved\r\n3 - \r\nReserved\r\n4 - \r\nPIN capture capability, 4 chars max\r\n5 - \r\nPIN capture capability, 5 chars max\r\n6 - \r\nPIN capture capability, 6 chars max\r\n7 - \r\nPIN capture capability, 7 chars max\r\n8 - \r\nPIN capture capability, 8 chars max\r\n9 - \r\nPIN capture capability, 9 chars max\r\nA - \r\nPIN capture capability, 10 chars \r\nmax\r\nB - \r\nPIN capture capability, 11 chars \r\nmax\r\nC - \r\nPIN capture capability, 12 chars \r\nmax\r\nNOTEThe following information shows the \r\nmapping between the values in TSYS ISO Field 82 \r\nand the values to be used for Amex ISO Field 22. \r\nIf you utilie the TSYS ISO 8583 specifications for \r\nauthoriation processing, you will need to map to \r\nthe values from TSYS ISO Field 82 to the values \r\nspecified for each subfield.  '),
             ('5', '29-31', '3', 'AN', 'M', 'Program Registration Identifier\r\nUsed to monitor and track a participants \r\nactivity in special promotion interchange \r\nrate programs.\r\nPossible values  \r\nC01 - \r\nPerson-to-person payment \r\n(Payment transaction)\r\nC02 - \r\nMasterCard Rebate (Payment \r\ntransaction)\r\nC03 - \r\nrePower Load value (Payment \r\ntransaction)\r\nC04 - \r\nGaming Re-pay (Payment \r\ntransaction)\r\nC05 - \r\nOther Payment transaction\r\nC06 - \r\nPayment of a credit card balance via \r\ncash or check\r\nPxx - \r\nPremier Service transaction\r\nRxx - \r\nService Industries transaction\r\nSxx - \r\nSupermarket transaction\r\nUxx - \r\nUtilities transaction\r\nWxx - \r\nWarehouse Club transaction'),
             ('6', '32-33', '2', 'AN', 'V', 'Card Product Code\r\nRefer to Appendix  for values.'),
             ('7', '34-35', '2', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('8', '36-37', '2', 'AN', 'CAPN', 'Media Code\r\nCode that identifies the type of media used \r\nin the transaction.\r\nPossible values  \r\n01 - \r\nCardmember signature on file\r\n02 - \r\nPhone order\r\n03 - \r\nMail order\r\n04 - \r\nInternet order\r\n05 - \r\nRecurring billing\r\nThis field can be filled with spaces.'),
             ('9', '38-39', '2', 'AN', 'CAPN', 'Submission Method\r\nCode that identifies the method used to \r\ninitiate the transaction.\r\nPossible values  \r\n01 - \r\nPOS Terminal-American Express\r\n02 - \r\nPOS Terminal-Non-American \r\nExpress\r\n03 - \r\nIntegrated POS System-Non-\r\nAmerican Express\r\nPaper-External vendor, paper \r\n05 - \r\nprocessor\r\n06 - \r\nPurchase Express\r\n07 - \r\nPayflow\r\n10 - \r\nDial Payment System\r\n13 - \r\nAutomated Bill Payment Platform\r\nThis field can be filled with spaces.'),
             ('10', '40-43', '4', 'N', 'CAPN', 'Card Expiry Date\r\nMonth and year after which the card is no \r\nlonger valid (YYMM).\r\nThis field can be filled with eroes.'),
             ('11', '44-49', '6', 'N', 'CAPN, VS', 'Transaction Time\r\nTime that the transaction took place. In the \r\ncase of mail or telephone orders, the time \r\nwhen the goods were shipped (HHMMSS).\r\nThe field can be filled with eroes.\r\nTime the transaction occurred (HHMMSS). '),
             ('12', '50-52', '3', 'N', 'M', 'Service Code\r\nValues from the magnetic stripe or the chip \r\nof a card which instructed the terminal \r\nabout conditions under which the card may \r\nbe used. '),
             ('13', '53-66', '14', 'AN', 'M, S', 'MasterCard Merchants Customer Service \r\nTelephone Number \r\nDiscover Customer Service Phone Number\r\nA 10-position, left-ustified value with \r\ntrailing spaces is required for all MO/TO \r\nand Recurring Payment transactions \r\nacquired in the U.S. and Canadian regions.'),
             ('14', '67', '1', 'AN', 'S', 'Partial Shipment Indicator\r\nCode that indicates whether part of a \r\nshipment was sent, instead of the whole \r\nshipment. \r\nPossible values  \r\nY - \r\nPart of a shipment was sent\r\nN - \r\nAll or none of the shipment was \r\nsent\r\nNOTEIf a value for this field is not provided, N \r\nwill be used.'),
             ('15', '68-73', '6', 'N', 'S', 'Local Transaction Time\r\nTime the first presentment was initiated \r\n(HHMMSS). '),
             ('16b-1', '74-79', '6', 'N', 'S', 'System Trace Audit Number\r\nNumber assigned by the acquiring member \r\nor the merchant to help identify the \r\ntransaction. The field must be right ustified. \r\nIt can contain leading eroes. '),
             ('16b-2', '80-82', '3', 'N', 'S', 'POS Entry Mode\r\nCode that identifies the method used to \r\nenter the transaction in the terminal. '),
             ('16a', '74-84', '11', 'N', 'M', 'Payment Facilitator ID \r\nValue assigned by MasterCard that \r\nrepresents the Company ID that will be \r\nassigned during the time of registration of a \r\nservice provider as Payment Facilitator.\r\nNOTEValue is the same in authoriation and \r\nclearing and settlement '),
             ('16b-3', '83-84', '2', 'N', 'S', 'Track Condition Code\r\nTwo-part field that indicates the condition \r\nof the card track information in the \r\nauthoriation request. The first part of the \r\nfield indicates the condition of the Track 1 \r\ninformation. The second part of the field \r\nindicates the condition of the Track 2 \r\ninformation. \r\nPossible values  for the Track 1 condition are\r\n0 - \r\nTrack 1 data is not present or is \r\ninvalid\r\n1 - \r\nTrack 1 data is present but \r\nCVV/DCVV/iCVV is not \r\nprovided\r\n2 - \r\nTrack 1 data is present using \r\nCVV/DCVV/iCVV\r\n3 - \r\nTrack 1 data is present with \r\nCVV/DCVV/iCVV set to all eros \r\n4 - \r\n Track 1 data is present with \r\nCVV/DCVV/iCVV containing \r\nsome or all blanks \r\n5 - \r\nTrack 1 data is present but \r\nCVV/DCVV/iCVV location was \r\nnot provided \r\n6 - \r\nTrack 1 data not present with \r\nCAVV provided\r\n7 - \r\nTrack 1 data not present with D-\r\nPAS Cryptogram provided \r\nPossible values  for the Track 2 condition are\r\n0 - \r\n Track 2 data is not present\r\n1 - \r\nTrack 2 data is present but  \r\nCVV/DCVV/iCVV is not \r\nprovided\r\n2 - \r\nTrack 2 data is present using \r\nCVV/DCVV/iCVV\r\n3 - \r\nTrack 2 data is present with \r\nCVV/DCVV/iCVV set to all eros 4 - \r\n Track 2 data is present with \r\nCVV/DCVV/iCVV containing \r\nsome or all blanks \r\n5 - \r\nTrack 2 data is present but \r\nCVV/DCVV/iCVV location was \r\nnot provided'),
             ('17a', '85-95', '11', 'N', 'M', 'Independent Sales Organiation (ISO) ID\r\nCompany ID  assigned by MasterCard \r\nduring registration of a service provider as \r\nIndependent Sales Organiation. \r\nNOTEValue is the same in authoriation and \r\nclearing and settlement '),
             ('17b', '85-97', '13', 'AN', 'S', 'POS Data Code\r\nCode that indicates specific conditions that \r\nexisted at the time of the transaction. The \r\nfield has 13 subfields. \r\nSubfield 1(POS Device Attendance \r\nIndicator) indicates if the merchant is \r\npresent at the POS device. The following \r\nvalues are valid for subfield 1. \r\n0 - \r\nAttended POS Device\r\n1 - \r\nUnattended POS Device \r\n2 - \r\nNo POS Device Used\r\n9 - \r\nUnknown \r\nSubfield 2 (Partial Approval Indicator) \r\nindicates if the merchant supports approvals \r\nof partial monetary amounts. The following \r\nvalues are valid for subfield 2. \r\n0 - \r\nPartial Approval Not Supported \r\n1 - \r\nPartial Approval Supported   \r\nMerchandise can be partially \r\napproved  Cash Over can be \r\npartially approved \r\n2 - \r\nPartial Approval Supported   \r\nMerchandise can be partially \r\napproved   Cash Over must be \r\nfully approved or declined \r\n3 - \r\nPartial Approval Supported   \r\nMerchandise must be fully \r\napproved or declined   Cash Over \r\ncan be partially approved\r\n4 - \r\nPartial Approval Supported   \r\nMerchandise must be fully \r\napproved or declined   Cash Over \r\nmust be fully approved or declined Subfield 3 (POS Device Location Indicator) \r\nindicates the location of the POS device. \r\nThe following values are valid for subfield 3.   \r\n0 - \r\nOn premises of Merchant facility\r\n1 - \r\nOff premises of Merchant facility \r\n(Merchant POS Device-remote \r\nlocation) \r\n2 - \r\nOn premises of Cardholder (home \r\nPC) \r\n3 - \r\nNo POS Device used (voice/ARU \r\nAudio Response Unit \r\nAuthoriations)\r\n9 - \r\nUnknown \r\nSubfield 4 (POS Cardholder Presence \r\nIndicator) indicates if the cardholder was \r\npresent at the POS. The following values are \r\nvalid for subfield 4. \r\n0 - \r\nCardholder present\r\n1 - \r\nCardholder not present, unspecified\r\n2 - \r\nCardholder not present, \r\nmail/facsimile order \r\n3 - \r\nCardholder not present, \r\ntelephone/ARU order \r\n4 - \r\nCardholder not present, standing \r\norder/recurring transactions \r\n(Automatic Payments)\r\n5 - \r\nElectronic Order (Internet)\r\n9 - \r\nUnknown \r\nSubfield 5 (POS Card Presence Indicator) \r\nindicates if the card was present at the POS. \r\nThe following values are valid for subfield 5.\r\n0  - \r\nCard present \r\n1  - \r\nCard not present\r\n9  - \r\nUnknown Subfield 6 (POS Card Capture Capabilities \r\nIndicator) indicates if the POS device can be \r\nused to capture card information. The \r\nfollowing values are valid for subfield 6.\r\n0 - \r\nPOS Device/operator has no Card \r\ncapture capability\r\n1 - \r\n POS Device/operator has Card \r\ncapture capability \r\n9 - \r\nUnknown \r\nSubfield 7 (POS Transaction Status \r\nIndicator) indicates the purpose or the \r\nstatus of the authoriation request. The \r\nfollowing values are valid for subfield 7. \r\n0 - \r\n Normal Request (original \r\npresentment) \r\n4  - \r\nPreauthoried Request\r\nSubfield 8 (POS Transaction Security \r\nIndicator) indicates the card acceptors \r\nassessment of the card presenter. The \r\nfollowing values are valid for subfield 8. \r\n0 - \r\nNo security concern \r\n1 - \r\nSuspected fraud (Merchant \r\nsuspicious) \r\n2 - \r\n ID verified \r\n3 - \r\n Cardholder verified by Biometrics \r\n9 - \r\nUnknown Subfield 9 POS e-Commerce transaction \r\nindicator\r\n0 - \r\nUnknown\r\n1 - \r\nCard transaction is not e-\r\nCommerce transaction\r\n4 - \r\nIn-app authentication\r\n5 - \r\nCard transaction is a secure e-\r\nCommerce transaction\r\n6 - \r\nMerchant attempted to authenticate \r\ncardholder information but issuer \r\ndoes not participate in ProtectBuy\r\n7 - \r\ne-Commerce card transaction with \r\ndata protection but not using \r\nProtectBuy for cardholder \r\nauthentication\r\n8 - \r\ne-Commerce card transaction \r\nwithout data protection\r\n9 - \r\nReserved\r\nSubfield 10 POS Type of terminal device\r\n0 - \r\nUnspecified\r\n9 - \r\nUnknown \r\nM - \r\nmPOS\r\nSubfield 11 (POS Device Card Data Input \r\nCapability Indicator) indicates if the POS \r\ndevice used by the merchant can capture \r\ncard information. The following values are \r\nvalid for subfield 11. \r\n0  - \r\nUnspecified \r\n1  - \r\n No POS Device used (voice/ARU \r\nAuthoriation) \r\n2  - \r\nMagnetic stripe reader \r\n3  - \r\nBar Code/Payment Code Read\r\n4 - \r\nOptical Character Recognition \r\n5 - \r\n Integrated Circuit Card Reader\r\n 6 - \r\nKey Entry Only (manual)  7  - \r\nMagnetic stripe reader and key \r\nentry \r\nC - \r\nRadio Frequency Identification \r\n(RFID) - Chip\r\nH - \r\nHybrid - Integrated Circuit Card \r\nReader  Contactless Capabilities\r\nR - \r\nRadio Frequency Identification \r\n(RFID) - Magnetic Stripe \r\nS - \r\nSecure Electronic Transaction \r\n(SET) with certification\r\nT  - \r\nSET without certificate \r\nU  - \r\nChannel-encrypted Electronic \r\nCommerce Transaction (SSL\r\nV - \r\nNon-secure Electronic Commerce \r\nTranaction\r\nSubfield 12 is reserved for future use. It \r\nshould be filled with a ero. \r\nSubfield 13 is reserved for future use. It \r\nshould be filled with a ero.'),
             ('18', '98-103', '6', 'N', 'S', 'Processing Code\r\nCode used to indicate the effect of a \r\ntransaction on the account or on the \r\nreceiving institution. \r\nPossible values  \r\nFor position 1-2 indicate the Process \r\nDescription\r\n00 - \r\nPurchase (of Goods or Services)\r\n01 - \r\nWithdrawal / Cash Advance\r\n09 - \r\nPurchase of Goods or Services with \r\nCash Over - Discover Only\r\n10 - \r\n Payment Transaction MasterCard\r\n13 - \r\nAddress Verification with a Goods \r\nor Services Authoriation for \r\nRecurring Billing (Automatic \r\nPayment)\r\n14 - \r\nRecurring Billing (Automatic \r\nPayment) - Goods or Services\r\n15 - \r\nInstallment Payment - Goods or \r\nServices\r\n16 - \r\nSubscription\r\n18 - \r\nAddress Verification Only\r\n20 - \r\nMerchandise Return\r\n28 - \r\nRecharge / Reload\r\n30 - \r\nAvailable Funds Inquiry\r\n31 - \r\nBalance Inquiry\r\n40 - \r\nAccounts Transfer / Cash OutFor positions 3-4 indicate the "From" \r\naccount for the card transaction\r\n00 - \r\n Not Applicable\r\n10 - \r\nSavings Account \r\n20 - \r\nChecking Account\r\n30 - \r\nCredit Card Account\r\n38 - \r\nCredit Line Account\r\n39 - \r\nCorporate \r\n40 - \r\nUniversal Account (Customer ID \r\nnumber)\r\n50 - \r\nMoney Market Investment Account\r\n60  - \r\nStored Value Account\r\n90 - \r\nRevolving Load Account \r\nFor positions 5-6 indicate the "To" account \r\nfor transfers\r\n00 - \r\nNot applicable\r\n10 - \r\nSavings Account\r\n20 - \r\nChecking Account\r\n30 - \r\nCredit Card Account\r\n38 - \r\nCredit Line Account\r\n40 - \r\nUniversal Account\r\n50 - \r\nMoney Market Investment Account\r\n58 - \r\nIRA Investment Account\r\n90 - \r\nRevolving Loan Account\r\n91 - \r\nInstallment Loan Account\r\n92  - \r\nReal Estate Loan Account'),
             ('19', '104', '1', 'S', 'TSYS', 'Reserved for TSYS use'),
             ('20', '105-116', '12', 'N', 'M', 'Point of Interaction (POI) Amount \r\nThe original transaction amount in the \r\nmerchants local currency prior to currency \r\nconversion services being performed.'),
             ('21', '117-119', '3', 'N', 'M', 'Point of Interaction (POI) Currency Code    \r\nThe numeric currency code that is \r\nassociated with the Point of Interaction \r\n(POI) Amount.   \r\nNOTEBefore using currency codes not \r\npreviously utilied, please contact your TSYS \r\nAcquiring Solutions Relationship Managers about \r\ntesting the new currency.'),
             ('22', '120', '1', 'AN', 'S', 'Address Verification Service (AVS) \r\nResponse Code'),
             ('23', '121-123', '3', 'AN', 'V', 'Visa Fee Program Indicator\r\nPossible value  3-character alphanumeric.\r\nValue assigned by Visa to each of its \r\ninterchange fee programs. This value \r\nindicates the interchange fee program for \r\nwhich a transaction was qualified or was \r\nsubmitted.'),
             ('24b-1', '124-127', '4', 'AN', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('24a', '124-128', '5', 'AN', 'V', 'Agent Unique Identifier\r\nPossible value  VCIND\r\nA unique identifier that is assigned by Visa at \r\nthe time of authoriation that identifies \r\ntransactions that originate from Visa \r\nCheckout.'),
             ('24b-2', '128', '1', 'A', 'TSYS Acquiring Solutions', 'Capture Endpoint Code\r\nPossible values  \r\nJ - \r\nJCB Capture Endpoint Code\r\nD - \r\nDiscover Capture Endpoint Code\r\nNOTEThis field applies to JCB transactions only \r\nand denotes whether TSYS should settle the \r\ntransaction through the Discover or JCB network.  \r\nThe field should contain a space for all other card \r\ntypes.'),
             ('26b-1', '129-140', '12', 'N', 'V, M, S', 'Transaction Fee Amount'),
             ('26b-2', '141', '1', 'A', 'V, M, S', 'Transaction Fee Indicator\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('26b-3', '142-144', '3', 'N', 'V, M', 'Cardholder Billing Currency Code\r\nNOTEBefore using currency codes not \r\npreviously utilied, please contact your TSYS \r\nAcquiring Solutions Relationship Managers about \r\ntesting the new currency.'),
             ('26a', '129-148', '20', 'AN', 'CAPN', 'Seller ID\r\nA unique code defined by the aggregator or \r\nOptBlue participant to identify a \r\nseller/vendor. '),
             ('26b-4', '145-148', '4', 'S', 'VM', 'Reserved for future use.'),
             ('27', '149-155', '7', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use.'),
             ('28', '156-157', '2', 'N', 'M', 'Device Type\r\nPossible values  \r\n00 - \r\nCard (default)\r\n01 - \r\nMobile Phone or Smartphone with  \r\nMobile Network Operator (MNO) \r\ncontrolled removable secure \r\nelement (SIM or UICC) \r\n02 - \r\nKeyFob\r\n03 - \r\nWatch using a contactless chip or a \r\nfixed (non-removable) secure \r\nelement not controlled by the \r\nMNO\r\n04 - \r\nMobile tag\r\n05 - \r\nWristband\r\n06 - \r\nMobile Phone Case or Sleeve\r\n07 - \r\nMobile Phone or Smartphone with \r\na fixed (non-removable) secure \r\nelement controlled by the MNO \r\n(such as CDMA)\r\n08 - \r\nMobile Phone or Smartphone with \r\nremovable secure element not         \r\ncontrolled by the MNO (such as a \r\npersonalied SD Card)\r\n09 - \r\nMobile Phone or Smartphone with \r\na fixed (non-removable) secure \r\nelement not controlled by the \r\nMNO\r\n10 - \r\nTablet or E-Book with an MNO \r\ncontrolled removable secure \r\nelement (SIM or UICC) \r\n11 - \r\nTablet or E-Book with a fixed \r\n(non-removable) secure element \r\ncontrolled by the MNO12 - \r\nTablet or E-Book with a removable \r\nsecure element not controlled by \r\nthe MNO (such as an SD Card) \r\n13 - \r\nTablet or E-Book with fixed (non-\r\nremovable) secure element not            \r\ncontrolled by the MNO \r\n14 - \r\nMobile Phone or Smartphone with \r\na payment application running in a \r\nhost processor\r\n15 - \r\nTablet or E-Book with a payment \r\napplication running in a host \r\nprocessor\r\n16 - \r\nMobile Phone or Smartphone with \r\na payment application running in \r\nthe TEE of a host processor\r\n17 - \r\nTablet or E-Book with a payment \r\napplication running in the TEE of a \r\nhost processor\r\n18 - \r\nWatch with a payment application \r\nrunning in the TEE of a host \r\nprocessor\r\n19 - \r\nWatch with a payment application \r\nrunning in a host processor\r\n20-99 - \r\nReserved for future device types. \r\nAny value in this range may occur \r\nwithin devices and transaction data \r\nwithout prior notice'),
             ('29', '158', '1', 'A', 'V', 'Spend Qualified Indicator\r\nThis value is optionally sent by Visa in an \r\nauthoriation response message. The \r\nmerchants interchange rate may be \r\ndetermined by the value of the Spend \r\nQualified Indicator. \r\nPossible values  \r\nB - \r\nBase send assessement threshold \r\nhas been met\r\nN - \r\nSpend Assessment not met\r\nQ - \r\nSpend Assessment has been met\r\nSpace - \r\nSpend Assessment does not apply'),
             ('30', '159', '1', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use.'),
             ('31', '160', '1', 'AN', 'V', 'Dynamic Currency Conversion (DCC) \r\nIndicator\r\nPossible values  \r\n1 - \r\nDCC performed for this \r\ntransaction\r\nSpace - \r\nNot a DCC transaction'),
             ('32', '161-193', '33', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use.'),
             ('33', '194-197', '4', 'N', 'M', 'Message Reason Code \r\nUsed in situations where multiple clearing \r\nrecords will be sent with a single \r\nauthoriation \r\nPossible values  \r\n1403 - \r\nPreviously approved \r\nauthoriation-partial amount, \r\nmulti-clearing\r\n1404 - \r\nPreviously approved \r\nauthoriation-partial amount, \r\nfinal clearing'),
             ('34', '198-212', '15', 'AN', 'M', 'Sub Merchant ID \r\nThis field is assigned by the Payment \r\nFacilitator or the Acquirer, and is applicable \r\nto all MasterCard transactions that originate \r\nfrom a Payment Facilitator. '),
             ('35', '213-247', '35', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('36', '248-249', '2', 'N', 'M', 'Transit Transaction Type Indicator\r\nPossible values  \r\n01 - \r\nPrefunded\r\n02 - \r\nReal time authoried\r\n03 - \r\nPost-authoried aggregated\r\n04 - \r\nAuthoried aggregated split clearing\r\n05 - \r\nOther\r\n07 - \r\nDebt Recovery\r\n06, 08-99 - Reserved for future use'),
             ('37', '250-251', '2', 'N', 'M', 'Transportation Mode Indicator\r\nPossible values  \r\n00 - \r\nUnknown\r\n01 - \r\nUrban bus\r\n02 - \r\nInterurban bus\r\n03 - \r\nLight train mass transit\r\n04 - \r\nTrain\r\n05 - \r\nCommuter train\r\n06 - \r\nWaterborne vehicle\r\n07 - \r\nToll\r\n08 - \r\nParking\r\n09 - \r\nTaxi\r\n10 - \r\nHigh speed train\r\n11 - \r\nRural bus\r\n12 - \r\nExpress commuter train\r\n13 - \r\nPara transit\r\n14 - \r\nSelf drive vehicle\r\n15 - \r\nCoach\r\n16 - \r\nLocomotive\r\n17 - \r\nPowered motor vehicle\r\n18 - \r\nTrailer\r\n19 - \r\nRegional train\r\n20 - \r\nInter city\r\n21 - \r\nFunicular train\r\n22 - \r\nCable car\r\n23-99 - \r\nReserved for future use'),
             ('38', '252-256', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nIndicates if an extension record follows, and \r\nif so, the type of extension record.\r\nPossible values  \r\nSpace - No extension record follows\r\nAIRL1 - \r\nAirline/Passenger Transport 1\r\nCARNT - Car Rental\r\nDIRCT - Direct Marketing\r\nEINTR - Electronic Invoice Transaction \r\nData\r\nENT1 - American Express Insurance \r\nIndustry\r\nEINPR - Electronic Invoice Party\r\nInformation\r\nFLEET - Fleet Service 1\r\nINS1 - \r\nAmerican Express Entertainment \r\nor Ticketing\r\nLODGE - Lodging\r\nMERCH - Merchant Description\r\nPURC1 - \r\nPurchasing Card 1\r\nRETAL - Retail\r\nSHIP1 - \r\nShipping Services 1\r\nTEMP1 - Temporary Help Services 1\r\nTBSUM - Telephone Billing Summary\r\nTBDET - Telephone Billing Detail'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "pointOfServicePosDataCode": None,
        "programRegistrationIdentifier": None,
        "cardProductCode": None,
        "reservedForFutureUse7": None,
        "mediaCode": None,
        "submissionMethod": None,
        "cardExpiryDate": None,
        "transactionTime": None,
        "serviceCode": None,
        "mastercardMerchantsCustomerService": None,
        "partialShipmentIndicator": None,
        "localTransactionTime": None,
        "systemTraceAuditNumber": None,
        "posEntryMode": None,
        "paymentFacilitatorId": None,
        "trackConditionCode": None,
        "independentSalesOrganiationIsoId": None,
        "posDataCode": None,
        "processingCode": None,
        "reservedForTsysUse": None,
        "pointOfInteractionPoiAmount": None,
        "pointOfInteractionPoiCurrencyCode": None,
        "addressVerificationServiceAvs": None,
        "visaFeeProgramIndicator": None,
        "reservedForFutureUse24b-1": None,
        "agentUniqueIdentifier": None,
        "captureEndpointCode": None,
        "transactionFeeAmount": None,
        "transactionFeeIndicator": None,
        "cardholderBillingCurrencyCode": None,
        "sellerId": None,
        "reservedForFutureUse26b-4": None,
        "reservedForFutureUse27": None,
        "deviceType": None,
        "spendQualifiedIndicator": None,
        "reservedForFutureUse30": None,
        "dynamicCurrencyConversionDcc": None,
        "reservedForFutureUse32": None,
        "messageReasonCode": None,
        "subMerchantId": None,
        "reservedForFutureUse35": None,
        "transitTransactionTypeIndicator": None,
        "transportationModeIndicator": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.pointOfServicePosDataCode,
        self.programRegistrationIdentifier,
        self.cardProductCode,
        self.reservedForFutureUse7,
        self.mediaCode,
        self.submissionMethod,
        self.cardExpiryDate,
        self.transactionTime,
        self.serviceCode,
        self.mastercardMerchantsCustomerService,
        self.partialShipmentIndicator,
        self.localTransactionTime,
        self.systemTraceAuditNumber,
        self.posEntryMode,
        self.paymentFacilitatorId,
        self.trackConditionCode,
        self.independentSalesOrganiationIsoId,
        self.posDataCode,
        self.processingCode,
        self.reservedForTsysUse,
        self.pointOfInteractionPoiAmount,
        self.pointOfInteractionPoiCurrencyCode,
        self.addressVerificationServiceAvs,
        self.visaFeeProgramIndicator,
        self.reservedForFutureUse24b-1,
        self.agentUniqueIdentifier,
        self.captureEndpointCode,
        self.transactionFeeAmount,
        self.transactionFeeIndicator,
        self.cardholderBillingCurrencyCode,
        self.sellerId,
        self.reservedForFutureUse26b-4,
        self.reservedForFutureUse27,
        self.deviceType,
        self.spendQualifiedIndicator,
        self.reservedForFutureUse30,
        self.dynamicCurrencyConversionDcc,
        self.reservedForFutureUse32,
        self.messageReasonCode,
        self.subMerchantId,
        self.reservedForFutureUse35,
        self.transitTransactionTypeIndicator,
        self.transportationModeIndicator,
        self.extensionRecordIndicator = (None)*47
        self.data = f.read(GeneralExtensionRecord.LENGTH)
        super(GeneralExtensionRecord, self).__init__()
        
class TokenExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the records \r\nposition within the transmission file.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions ', 'Transaction Code\r\nThe Transaction code identifies the type of \r\nrecord being transmitted.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions ', 'Extension Record Indicator\r\nThe Extension Record Indicator identifies this \r\nrecord as a Token Extension Record.\r\nRequired value TOKEN'),
             ('4', '17-18', '2', 'AN', 'V, M', 'Token Assurance Level\r\nDefined by the token service provider, this Visa \r\nor MasterCard value indicates the assigned \r\nconfidence level of the token-to-\r\nPAN/cardholder binding. '),
             ('5', '19-27', '9', 'AN', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('6', '28', '1', 'AN', 'V, M', 'Account Range Status\r\nThis value is used by the acquirer or processor \r\nand indicates the status of the account.\r\nPossible values  \r\nSpace\r\nR - Regulated\r\nN - Non-Regulated'),
             ('7', '29', '1', 'AN', 'TSYS Acquiring Solutions', 'BAS Token Indicator\r\nTSYS internal use only'),
             ('8', '30-40', '11', 'AN', 'V, M', 'Requestor ID\r\nThis value uniquely identifies the pairing of \r\ntoken requestor with the token domain. '),
             ('9', '41-251', '211', 'AN', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('10', '252-256', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "extensionRecordIndicator3": None,
        "tokenAssuranceLevel": None,
        "reservedForFutureUse5": None,
        "accountRangeStatus": None,
        "basTokenIndicator": None,
        "requestorId": None,
        "reservedForFutureUse9": None,
        "extensionRecordIndicator10": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.extensionRecordIndicator3,
        self.tokenAssuranceLevel,
        self.reservedForFutureUse5,
        self.accountRangeStatus,
        self.basTokenIndicator,
        self.requestorId,
        self.reservedForFutureUse9,
        self.extensionRecordIndicator10 = (None)*10
        self.data = f.read(TokenExtensionRecord.LENGTH)
        super(TokenExtensionRecord, self).__init__()
        
class InsuranceIndustryExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nNumber that identifies the position of this \r\nrecord within the file.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nCode that identifies the type of transaction \r\nbeing transmitted.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nCode that indicates the record type.\r\nPossible value  INS1'),
             ('4', '17-39', '23', 'AN', 'CAPN', 'Insurance Policy Number\r\nNumber assigned to the insurance policy.'),
             ('5', '40-45', '6', 'N', 'CAPN', 'Insurance Coverage Start Date\r\nDate the insurance coverage began \r\n(MMDDYY).'),
             ('6', '46-51', '6', 'N', 'CAPN', 'Insurance Coverage End Date\r\nDate the insurance coverage is scheduled to \r\nend (MMDDYY).'),
             ('7', '52-58', '7', 'AN', 'CAPN', 'Insurance Policy Premium Frequency\r\nUsed to identify how often the policy \r\npremium is due. This is a text field.'),
             ('8', '59-81', '23', 'AN', 'CAPN', 'Additional Insurance Policy Number\r\nNumber of any additional insurance policy \r\nassociated with the insurance policy \r\nidentified in the Insurance Policy Number \r\nfield.'),
             ('9', '82-106', '25', 'AN', 'CAPN', 'Type of Policy\r\nText field used to indicate the type of \r\ncoverage offered by the policy.'),
             ('10', '107-136', '30', 'AN', 'CAPN', 'Name of Insured\r\nText field used to indicate the name of the \r\nperson insured. This name can be different \r\nfrom the cardmembers name.'),
             ('11', '137-251', '116', 'B', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('12', '252-256', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nCode that indicates if another extension \r\nrecord follows this record. \r\nPossible value  Blank (No extension record \r\nfollows).'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "insurancePolicyNumber": None,
        "insuranceCoverageStartDate": None,
        "insuranceCoverageEndDate": None,
        "insurancePolicyPremiumFrequency": None,
        "additionalInsurancePolicyNumber": None,
        "typeOfPolicy": None,
        "nameOfInsured": None,
        "reservedForFutureUse": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.insurancePolicyNumber,
        self.insuranceCoverageStartDate,
        self.insuranceCoverageEndDate,
        self.insurancePolicyPremiumFrequency,
        self.additionalInsurancePolicyNumber,
        self.typeOfPolicy,
        self.nameOfInsured,
        self.reservedForFutureUse,
        self.extensionRecordIndicator = (None)*12
        self.data = f.read(InsuranceIndustryExtensionRecord.LENGTH)
        super(InsuranceIndustryExtensionRecord, self).__init__()
        
class LodgingExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nA list of transaction codes can be found on \r\nthe Inquire Status Record (ISR) screen of \r\nthe TSYS Accounting (TSA) System.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator identifies this record \r\nas a Lodging Extension Record.\r\nRequired value  LODGE'),
             ('4b-1', '17-26', '10', 'AN', 'M', 'Hotel Folio Number'),
             ('4c-1', '17-26', '10', 'AN', 'X', 'Record of Charge'),
             ('4b-2', '27-36', '10', 'AN', 'M', 'Customer Service Telephone Number'),
             ('4a', '17-41', '25', 'AN', 'SCVXAPN', 'Purchase Identifier\r\nPositions 17-41 Hotel Folio Number.\r\nRecord of Charge Number\r\nPositions 17-26 Record of Charge Number\r\nPositions 27-41 Blanks\r\nFolio Number\r\nLodging Folio Number\r\nNumber used to identify the statement \r\ncontaining the charges and credits for this \r\nstay. The number is assigned by either the \r\nmerchant or an authoried processor for the \r\nmerchant.\r\nThis field must be left-ustified. You can use \r\nspaces as filler.'),
             ('4b-3', '37-41', '5', 'S', 'M', 'Reserved for future use'),
             ('4c-2', '27-41', '15', 'S', 'X', 'Reserved for future use'),
             ('5', '42', '1', 'AN', 'VCAPN', 'No Show Indicator \r\nCode that indicates if the cardholder did not \r\nuse the lodging reservation.\r\nPossible values  \r\n0 - \r\nNot applicable\r\n1 - \r\nNo show\r\nLodging Special Program Code\r\nCode that identifies an additional service \r\nassociated with a lodging charge. For more \r\ninformation, refer to your American \r\nExpress documentation.\r\nPossible values  \r\n1 - \r\nLodging\r\n2 - \r\nNo Show Reservation\r\n3  - \r\nAdvance Deposit'),
             ('6', '43-48', '6', 'AN', 'VX', 'Extra Charges\r\nRoom Rate'),
             ('7', '49-54', '6', 'N', 'VMSCAPN', 'Check-in Date (MMDDYY)\r\nArrival Date (MMDDYY)\r\nArrival Date (MMDDYY)\r\nDate the cardholder checked into the \r\nlodging facility.\r\nLodging Check-In Date (MMDDYY)\r\nEither the date that the guest is scheduled to \r\ncheck in at the lodging facility, or the actual \r\ndate that the guest checked in.'),
             ('8', '55', '1', 'N', 'VX', ' Market Specific Authoriation Data \r\nIndicator\r\nCharge Descriptor'),
             ('9', '56-67', '12', 'N', 'VX', 'Total Authoried Amount\r\nTax Amount'),
             ('10', '68-77', '10', 'AN', 'MS', 'Property Telephone Number\r\nFacility Telephone Number\r\nTelephone number at the lodging location'),
             ('11', '78-83', '6', 'N', 'MSCAPN', 'Checkout Date\r\nDeparture Date (MMDDYY)\r\nDate the customer checked out of the \r\nlodging facility.\r\nLodging Checkout Date (MMDDYY)\r\nEither the date that the guest was scheduled \r\nto check out of the lodging facility, or the \r\nactual date that the guest checked out.'),
             ('12', '84-85', '2', 'AN', 'MSX', 'Program Code\r\nProgram Code\r\nCode used to identify special circumstances, \r\nsuch as a no-show customer\r\nApproval Code'),
             ('13', '86-97', '12', 'N', 'VMSCAPN', 'Daily Room Rate\r\nRate charged for each day the room is \r\nrented. Multiple LODGE extension records \r\nan be used to handle additional fields.\r\nRoom Rate\r\nRate charged for renting the room. Multiple \r\nLODGE extension records can be used to \r\nhandle additional fields.\r\nRoom Rate\r\nRate charged for renting the room.\r\nLodging Room Rate 1\r\nRate charged for one night at the lodging \r\nfacility. The monetary amount in this field \r\nmust be in the currency identified in the \r\nAuthoriation Currency Code field in the \r\nDF256 record. \r\nFor all associations, the field must be right-\r\nustified. You can use eroes as filler.\r\nUp to three Lodging Room Rates are \r\npossible. They need to be sent to \r\nsubsequent Lodge records.'),
             ('14', '98-109', '12', 'N', 'VM,S, CAPN', 'Total Tax\r\nRoom Tax\r\nThis field must be right-ustified and ero-\r\nfilled.'),
             ('15', '110-121', '12', 'N', 'MSCAPN', 'Total Charges for All Calls\r\nThis field is used to house the dollar amount \r\nof all calls. It must be right-ustified and \r\nero-filled.\r\nPhone Charges\r\nTotal monetary amount of all calls made \r\nfrom the room. It must be right-ustified and \r\nero-filled.\r\nPhone'),
             ('16', '122-133', '12', 'N', 'VM, SCAPN', 'Food/Beverage Charges\r\nRestaurant/Room Service Charges\r\nFor Visa, MasterCard and Discover this \r\nfield must be right-ustified and ero-filled.\r\nRestaurant/Room Service'),
             ('17', '134-145', '12', 'N', 'M, SCAPN', 'Bar/Mini-Bar Charges\r\nThis field must be right-ustified and ero-\r\nfilled.\r\nBar/Mini-Bar'),
             ('18', '146-157', '12', 'N', 'M, SCAPN', 'Gift Shop Charges\r\nThis field must be right-ustified and ero-\r\nfilled.\r\nGift Shop'),
             ('19', '158-169', '12', 'N', 'M, SCAPN', 'Laundry/Dry Cleaning Amount\r\nThis field must be right-ustified and ero-\r\nfilled.\r\nLaundry/Dry-Cleaning'),
             ('20', '170-172', '3', 'AN', 'MS', 'Other Services Code\r\nOther Indicator\r\nCode that identifies any additional services \r\nfor which the cardholder was billed.'),
             ('21', '173-184', '12', 'N', 'MSCAPN', 'Other Services Charges\r\nThis field must be right-ustified and ero-\r\nfilled.\r\nOther Charges\r\nMonetary amount charged for the additional \r\nservices identified in the Other Services \r\nCode field.\r\nThis field must be right-ustified and ero-\r\nfilled.\r\nMisc. Charges/Fees'),
             ('22', '185', '1', 'AN', 'M', 'Billing Adustment Indicator'),
             ('23', '186-197', '12', 'N', 'VMSCAPN', 'Folio Cash Advances\r\nBilling Adustment Amount\r\nAdustment Amount\r\nTotal monetary amount of adustments or \r\ncash advances charged to the customers \r\naccount\r\nCharges Added After Check-\r\nOut/Departure'),
             ('24', '198-209', '12', 'N', 'V', 'Prepaid Expense'),
             ('25', '210-214', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nPossible values  \r\nSpace - \r\nno extension record follows\r\nLODGE - another Lodging Extension Record \r\nfollows (Visa only)\r\nOPTIN - \r\na Lodging Optional Extension \r\nRecord follows\r\nPURC1 - \r\na Purchasing Card 1 Extension \r\nRecord follows'),
             ('26', '215-216', '2', 'N', 'V, MCAPN', 'Room Nights\r\nNumber of nights the hotel room was used.\r\nNumber of Nights at Room Rate 1\r\nNumber of nights the guest stayed in the \r\nroom. These nights were charged at the rate \r\ncontained in the Lodging Room Rate 1 field.\r\nThis field must be right-ustified. You can \r\nuse eroes as filler.\r\nUp to three Number of Nights at Room \r\nRate fields are possible. They need to be \r\nsent to subsequent Lodge records.'),
             ('27', '217-228', '12', 'N', 'V', 'Total Room Tax'),
             ('28', '229', '1', 'AN', 'M', 'Fire Safety Act Indicator\r\nCode that identifies if the facility is in \r\ncompliance with the Hotel and Motel Fire \r\nSafety Act.\r\nPossible values  \r\nY - \r\nIn compliance\r\nN - \r\nNot in compliance'),
             ('29', '230', '1', 'A', 'M', 'Billing Adustment Sign\r\nSub-field 3 of the Billing Adustment field \r\nindicates whether the billing adustment is a \r\ndebit or credit. A billing adustment is used \r\nwhen additional charges were incurred after \r\nthe cardholders departure.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('30', '231', '1', 'A', 'M', 'Room Tax Amount Sign\r\nSub-field 3 of the Total Room Tax field \r\nindicates whether the total room tax amount \r\nis a debit or credit. The total room tax \r\ncontains tax information including room \r\ntax, occupancy tax, energy tax and tourist \r\ntax.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('31', '232', '1', 'A', 'M', 'Phone Charge Sign\r\nSub-field 3 of the Phone Charge field \r\nindicates whether the phone charge amount \r\nis a debit or credit. The amount of the phone \r\ncharge is the total amount of charges for all \r\nphone calls.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('32', '233', '1', 'A', 'M', 'Room Service Sign\r\nSub-field 3 of the Room Service Charges \r\nfield indicates whether the room service \r\namount is a debit or credit. The room \r\nservice amount is the total amount of room \r\nservice charges.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('33', '234', '1', 'A', 'M', 'Bar Sign\r\nSub-field 3 of the Lounge/Bar Charges \r\nfield indicates whether the lounge and bar \r\ncharges amount is a debit or credit. The \r\namount of this charge is the total amount of \r\nlounge and bar charges.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('34', '235', '1', 'A', 'M', 'Gift Shop Sign\r\nSub-field 3 of the Gift Shop Charges field \r\nindicates whether the gift shop charge \r\namount is a debit or credit. The amount of \r\nthe gift shop charge is the total amount of all \r\ngift shop and specialty shop charges.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('35', '236', '1', 'A', 'M', 'Laundry Sign\r\nSub-field 3 of the Laundry and Dry Cleaning \r\nCharge field indicates whether the amount \r\nof laundry and dry cleaning charges is a debit \r\nor credit. The amount of laundry and dry \r\ncleaning charges is the total amount of \r\ncleaning charges.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('36', '237', '1', 'A', 'M', 'Other Services Sign\r\nSubfield 3 of the Other Services field \r\nindicates whether the other services amount \r\nis a debit or credit. The other services \r\namount is the total amount of other services \r\nnot classified elsewhere.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('37', '238-256', '19', 'AN', 'M', 'Reserved for future use.'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "hotelFolioNumber": None,
        "recordOfCharge": None,
        "customerServiceTelephoneNumber": None,
        "purchaseIdentifier": None,
        "reservedForFutureUse4b-3": None,
        "reservedForFutureUse4c-2": None,
        "noShowIndicator": None,
        "extraCharges": None,
        "checkInDateMmddyy": None,
        "marketSpecificAuthoriationData": None,
        "totalAuthoriedAmount": None,
        "propertyTelephoneNumber": None,
        "checkoutDate": None,
        "programCode": None,
        "dailyRoomRate": None,
        "totalTax": None,
        "totalChargesForAllCalls": None,
        "foodBeverageCharges": None,
        "barMiniBarCharges": None,
        "giftShopCharges": None,
        "laundryDryCleaningAmount": None,
        "otherServicesCode": None,
        "otherServicesCharges": None,
        "billingAdustmentIndicator": None,
        "folioCashAdvances": None,
        "prepaidExpense": None,
        "extensionRecordIndicator": None,
        "roomNights": None,
        "totalRoomTax": None,
        "fireSafetyActIndicator": None,
        "billingAdustmentSign": None,
        "roomTaxAmountSign": None,
        "phoneChargeSign": None,
        "roomServiceSign": None,
        "barSign": None,
        "giftShopSign": None,
        "laundrySign": None,
        "otherServicesSign": None,
        "reservedForFutureUse37": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.hotelFolioNumber,
        self.recordOfCharge,
        self.customerServiceTelephoneNumber,
        self.purchaseIdentifier,
        self.reservedForFutureUse4b-3,
        self.reservedForFutureUse4c-2,
        self.noShowIndicator,
        self.extraCharges,
        self.checkInDateMmddyy,
        self.marketSpecificAuthoriationData,
        self.totalAuthoriedAmount,
        self.propertyTelephoneNumber,
        self.checkoutDate,
        self.programCode,
        self.dailyRoomRate,
        self.totalTax,
        self.totalChargesForAllCalls,
        self.foodBeverageCharges,
        self.barMiniBarCharges,
        self.giftShopCharges,
        self.laundryDryCleaningAmount,
        self.otherServicesCode,
        self.otherServicesCharges,
        self.billingAdustmentIndicator,
        self.folioCashAdvances,
        self.prepaidExpense,
        self.extensionRecordIndicator,
        self.roomNights,
        self.totalRoomTax,
        self.fireSafetyActIndicator,
        self.billingAdustmentSign,
        self.roomTaxAmountSign,
        self.phoneChargeSign,
        self.roomServiceSign,
        self.barSign,
        self.giftShopSign,
        self.laundrySign,
        self.otherServicesSign,
        self.reservedForFutureUse37 = (None)*42
        self.data = f.read(LodgingExtensionRecord.LENGTH)
        super(LodgingExtensionRecord, self).__init__()
        
class MerchantDescriptionExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nA list of transaction codes can be found on \r\nthe Inquire Status Record (ISR) screen of \r\nthe TSYS Accounting (TSA) System.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator identifies this record \r\nas a Merchant Description Extension \r\nRecord.\r\nRequired value  MERCH'),
             ('4', '17-41', '25', 'AN', 'MX, CAPN', 'Merchant Street Address\r\nStreet address used by the merchant.\r\nThis field must be left-ustified and space-\r\nfilled.\r\nLocation Address\r\nThis field is designed to accept upper-case \r\nalpha characters. In addition, the field must \r\nbe left-ustified.\r\nYou can use spaces as filler.\r\nAggregators Only- this field must contain \r\nthe sellers street address.\r\nMOTO/Internet - Merchants in these \r\nindustries may substitute the street address \r\nwhere the merchants order processing \r\nfacility is located.'),
             ('5', '42-57', '16', 'AN', 'M, X', 'Merchant Telephone Number\r\nThis field must be left-ustified and space-\r\nfilled.'),
             ('6', '58-82', '25', 'AN', 'M', 'Sole Proprietor Name\r\nThis field must be left-ustified and space-\r\nfilled.'),
             ('7', '83-107', '25', 'AN', 'M', 'Legal Corporate Name\r\nThis field must be left-ustified and space-\r\nfilled.'),
             ('8', '108-117', '10', 'AN', 'MX, CAPN', 'Merchant Location Postal Code\r\nPostal code used with the merchant address.\r\nThis field must be left-ustified and space-\r\nfilled.\r\nLocation Postal Code\r\nThis field is designed to accept upper-case \r\nalpha characters. In addition, the field must \r\nbe left-ustified.\r\nYou can use spaces as filler.\r\nAggregators Only - This field must contain \r\nthe postal code that corresponds to the \r\nsellers location. In cases where a postal \r\ncode is unavailable, this field must be \r\ncharacter space filled.'),
             ('9', '118-132', '15', 'N', 'M', 'Dun  Bradstreet Number\r\nIf the Dun  Bradstreet number is not \r\navailable, use eros in this field.'),
             ('10b-1', '133-138', '6', 'AN', 'M', 'Customer Identifier Type\r\nPossible values  \r\nCUSORD - Customer Order\r\nCUSTPO - Customer Purchase Order\r\nFOLNUM - Folio Number\r\nINVACT - Invoice or Account Number for \r\nBill Payments\r\nOTHER1 - Other\r\nPRCHID - Purchase Identification\r\nRECLOC - Record Locator\r\nRESNUM - Reservation Number\r\nRNTAGR - Rental Agreement\r\nSUPINV - Supplier Invoice\r\nSUPORD - Supplier Order\r\nTKTNUM - Ticket Number\r\nTRANID - Transaction Identification\r\nTRKNUM - Tracking Number\r\nPMTRF - Payment Reference Number'),
             ('10a-1', '133-172', '40', 'AN', 'X, CAPN', 'Merchant Contact Information\r\nTelephone number or worldwide web \r\naddress, or e-mail address of the merchant. \r\nThe contact information can display on the \r\ncardmember statement. It can also be used \r\nto resolve disputes and billing inquiries. \r\nThe field is designed to accept upper-case \r\nletters however, you can use lower-case \r\nletters for worldwide web and e-mail \r\naddresses.\r\nThis field must be left-ustified and space-\r\nfilled.'),
             ('10a-2', '173-210', '38', 'AN', 'X, CAPN', 'Merchant DBA\r\nDoing Business As (DBA) name of the \r\nmerchant where the transaction originated. \r\nThis field is left ustified and space-filled.\r\nExample (Note  designates a space)\r\nKATYS BEACH \r\nUMBRELLAS\r\nFor transactions that arrive via a Payment \r\nService Provider (PSP) / Aggregator, the \r\nfield will also contain the PSP Name, left \r\nustified. There will be no spaces in the PSP \r\nName itself, yet it will be space-filled on the \r\nend, to 12 characters in length. The format \r\ncontains an equal sign delimiter following \r\nthe PSP Name.\r\nPSP NameDBA Name\r\nExample (Note  designates a space)\r\nMONSTERPSPKATYS BEACH \r\nUMBRELLAS'),
             ('10b-2', '139-214', '76', 'AN', 'M', 'Custom Identifier Detail'),
             ('10a-3', '211-214', '4', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use.'),
             ('11', '215-222', '8', 'NUM', 'TSYS Acquiring Solutions', 'Lane ID\r\nThis data uniquely identifies a terminal at \r\nthe card acceptor location of acquiring \r\ninstitutions or merchant POS systems.'),
             ('12', '223-251', '29', 'AN', 'TSYS Acquiring Solutions', 'Reserved for future use.'),
             ('13', '252-256', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nThe value in this field indicates whether an \r\nextension record follows and, if so, the type \r\nof extension.\r\nPossible values  \r\nAIRL1 - \r\nAirline/Passenger Transport 1\r\nCARNT - Car Rental\r\nDIRCT - Direct Marketing\r\nFLEET - Fleet Service 1\r\nGENER - Generic\r\nLODGE - Lodging\r\nPURC1 - \r\nPurchasing Card 1\r\nAMEXR - Restaurant'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "merchantStreetAddress": None,
        "merchantTelephoneNumber": None,
        "soleProprietorName": None,
        "legalCorporateName": None,
        "merchantLocationPostalCode": None,
        "dunBradstreetNumber": None,
        "customerIdentifierType": None,
        "merchantContactInformation": None,
        "merchantDba": None,
        "customIdentifierDetail": None,
        "reservedForFutureUse10a-3": None,
        "laneId": None,
        "reservedForFutureUse12": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.merchantStreetAddress,
        self.merchantTelephoneNumber,
        self.soleProprietorName,
        self.legalCorporateName,
        self.merchantLocationPostalCode,
        self.dunBradstreetNumber,
        self.customerIdentifierType,
        self.merchantContactInformation,
        self.merchantDba,
        self.customIdentifierDetail,
        self.reservedForFutureUse10a-3,
        self.laneId,
        self.reservedForFutureUse12,
        self.extensionRecordIndicator = (None)*17
        self.data = f.read(MerchantDescriptionExtensionRecord.LENGTH)
        super(MerchantDescriptionExtensionRecord, self).__init__()
        
class TaxExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the records \r\nposition within the transmission file.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nFor a list of possible values, see the Inquire \r\nStatus Record (ISR) screen of the TSYS \r\nAccounting (TSA) System.\r\nCommon values (not inclusive)\r\n0101 -Regular Sales Draft \r\n0102 -Regular Cash Advance\r\n0106 -Credit to Purchase Balance\r\n0108 -Payment\r\n0109 -Sales Draft Reversal\r\n0110 -Cash Advance Reversal\r\n0114 -Credit Reversal Purchase Balance\r\n0116 -Payment Reversal'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator identifies this record as a \r\nDetailed Tax Extension Record.\r\nRequired value   TAX'),
             ('4', '17', '1', 'AN', 'M', 'Tax Amount Indicator 1\r\nCode that indicates how additional tax \r\ninformation is captured and reported.\r\nPossible values  \r\nY - \r\nTax included in the total purchase \r\namount\r\nN - \r\nTax not included in total purchase \r\namount\r\nSpace -   Not applicable'),
             ('5', '18-29', '12', 'N', 'M', 'Tax Amount 1\r\nMonetary amount of the additional tax\r\nThe value must be right-ustified.'),
             ('6', '30-34', '5', 'N', 'M', 'Tax Rate 1\r\nTax rate applied to the purchase\r\nThe value must be right-ustified.\r\nThe Tax Rate 1 and Tax Rate Exponent 1 fields \r\nare used together to express the tax rate. For \r\nexample, if the value in the Tax Rate 1 field is \r\n12345 and the value in the Tax Rate Exponent 1 \r\nfield is 3, then the amount in the Tax Rate 1 \r\nfield is read as 12.345.'),
             ('7', '35', '1', 'N', 'M', 'Tax Rate Exponent 1\r\nDecimal location of  Tax Rate 1 possible values \r\nare 0 to 5\r\nThe  Tax Rate 1 and Tax Rate Exponent 1 fields \r\nare used together to express the tax rate. For \r\nexample, if the value in the  Tax Rate 1 field is \r\n12345 and the value in the Tax Rate Exponent 1 \r\nfield is 3, then the amount in the Tax Rate 1 \r\nfield is read as 12.345.'),
             ('8', '36-39', '4', 'AN', 'M', ' Tax Type Applied 1\r\nCode that defines a tax category that may apply \r\nto specific domestic processing arrangements.\r\nNOTEThis may be space-filled, unless \r\ndirected otherwise by MasterCard.'),
             ('9', '40-41', '2', 'AN', 'M', 'Tax Type ID 1\r\nCode that identifies the type of tax that Tax \r\nAmount 1 represents.\r\nPossible values  \r\n00 - \r\nUnknown\r\n01 - \r\nFederal or national sales tax\r\n02 - \r\nState sales tax\r\n03 - \r\nCity sales tax\r\n04 - \r\nLocal sales tax\r\n05 - \r\nMunicipal sales tax\r\n06 - \r\nOther tax\r\n10 - \r\nValue Added Tax (VAT)\r\n11 - \r\nGoods and Services Tax (GST)\r\n12 - \r\nProvincial Sales Tax (PST)\r\n13  - \r\nHarmonied Sales Tax (HST)\r\n14 - \r\nQuebec Sales Tax (QST)\r\n20 - \r\nRoom tax\r\n21 - \r\nOccupancy tax\r\n22 - \r\nEnergy Tax\r\nSpace - Not applicable'),
             ('10', '42', '1', 'AN', 'M', 'Tax Amount Indicator 2\r\nCode that indicates how additional tax \r\ninformation is captured and reported.\r\nPossible values  \r\nY - \r\nTax included in the total purchase \r\namount\r\nN - \r\nTax not included in total purchase \r\namount\r\nSpace - Not applicable'),
             ('11', '43-54', '12', 'N', 'M', 'Tax Amount 2\r\nMonetary amount of the additional tax\r\nThe value must be right-ustified.'),
             ('12', '55-59', '5', 'N', 'M', 'Tax Rate 2\r\nTax rate applied to the purchase.\r\nThe value must be right-ustified.\r\nThe Tax Rate 2 and Tax Rate Exponent 2 fields \r\nare used together to express the tax rate. For \r\nexample, if the value in the Tax Rate 2 field is \r\n12345 and the value in the Tax Rate Exponent 2 \r\nfield is 3, then the amount in the Tax Rate 2 \r\nfield is read as 12.345.'),
             ('13', '60', '1', 'N', 'M', 'Tax Rate Exponent 2\r\nDecimal location of  Tax Rate 2 possible values \r\nare 0 to 5\r\nThe Tax Rate 2 and Tax Rate Exponent 2 fields \r\nare used together to express the tax rate. For \r\nexample, if the value in the Tax Rate 2 field is \r\n12345 and the value in the Tax Rate Exponent 2 \r\nfield is 3, then the amount in the Tax Rate 2 \r\nfield is read as 12.345.'),
             ('14', '61-64', '4', 'AN', 'M', 'Tax Type Applied 2\r\nCode that defines a tax category that may apply \r\nto specific domestic processing arrangements.\r\nNOTEThis field may be space-filled, unless \r\ndirected otherwise by MasterCard.'),
             ('15', '65-66', '2', 'AN', 'M', 'Tax Type ID 2\r\nCode that identifies the type of tax that Tax \r\nAmount 2 represents.\r\nPossible values  \r\n00 - \r\nUnknown\r\n01 - \r\nFederal or national sales tax\r\n02 - \r\nState sales tax\r\n03 - \r\nCity sales tax\r\n04 - \r\nLocal sales tax\r\n05 - \r\nMunicipal sales tax\r\n06 - \r\nOther tax\r\n10 - \r\nValue Added Tax (VAT)\r\n11 - \r\nGoods and Services Tax (GST)\r\n12 - \r\nProvincial Sales Tax (PST)\r\n13  - \r\nHarmonied Sales Tax (HST)\r\n14 - \r\nQuebec Sales Tax (QST)\r\n20 - \r\nRoom tax\r\n21 - \r\nOccupancy tax\r\n22 - \r\nEnergy Tax\r\nSpace - Not applicable'),
             ('16', '67', '1', 'AN', 'M', 'Tax Amount Indicator 3\r\nCode that indicates how additional tax \r\ninformation is captured and reported.\r\nPossible values  \r\nY - \r\nTax included in the total purchase \r\namount\r\nN - \r\nTax not included in total purchase \r\namount\r\nSpace - Not applicable'),
             ('17', '68-79', '12', 'N', 'M', 'Tax Amount 3\r\nMonetary amount of the additional tax\r\nThe value must be right-ustified.'),
             ('18', '80-84', '5', 'N', 'M', 'Tax Rate 3\r\nTax rate applied to the purchase\r\nThe value must be right-ustified.\r\nThe Tax Rate 3 and Tax Rate Exponent 3 fields \r\nare used together to express the tax rate. For \r\nexample, if the value in the Tax Rate 3 field is \r\n12345 and the value in the Tax Rate Exponent 3 \r\nfield is 3, then the amount in the Tax Rate 3 \r\nfield is read as 12.345.'),
             ('19', '85', '1', 'N', 'M', 'Tax Rate Exponent 3\r\nDecimal location of Tax Rate 3 possible values \r\nare 0 to 5\r\nThe Tax Rate 3 and Tax Rate Exponent 3 fields \r\nare used together to express the tax rate. For \r\nexample, if the value in the Tax Rate 3 field is \r\n12345 and the value in the Tax Rate Exponent 3 \r\nfield is 3, then the amount in the  Tax Rate 3 \r\nfield is read as 12.345.'),
             ('20', '86-89', '4', 'AN', 'M', 'Tax Type Applied 3\r\nCode that defines a tax category that may apply \r\nto specific domestic processing arrangements.\r\nNOTEThis field may be space-filled, unless \r\ndirected otherwise by MasterCard.'),
             ('21', '90-91', '2', 'AN', 'M', 'Tax Type ID 3\r\nCode that identifies the type of tax that Tax \r\nAmount 3 represents.\r\nPossible values  \r\n00 - \r\nUnknown\r\n01 - \r\nFederal or national sales tax\r\n02 - \r\nState sales tax\r\n03 - \r\nCity sales tax\r\n04 - \r\nLocal sales tax\r\n05 - \r\nMunicipal sales tax\r\n06 - \r\nOther tax\r\n10 - \r\nValue Added Tax (VAT)\r\n11 - \r\nGoods and Services Tax (GST)\r\n12 - \r\nProvincial Sales Tax (PST)\r\n13  - \r\nHarmonied Sales Tax (HST)\r\n14 - \r\nQuebec Sales Tax (QST)\r\n20 - \r\nRoom tax\r\n21 - \r\nOccupancy tax\r\n22 - \r\nEnergy Tax\r\nSpace - Not applicable'),
             ('22', '92', '1', 'AN', 'M', 'Tax Amount Indicator 4\r\nCode that indicates how additional tax \r\ninformation is captured and reported.\r\nY - \r\nTax included in the total purchase \r\namount\r\nN - \r\nTax not included in total purchase \r\namount\r\nSpace - Not applicable'),
             ('23', '93-104', '12', 'N', 'M', 'Tax Amount 4\r\nMonetary amount of the additional tax\r\nThe value must be right-ustified.'),
             ('24', '105-109', '5', 'N', 'M', 'Tax Rate 4\r\nTax rate applied to the purchase\r\nThe value must be right-ustified.\r\nThe Tax Rate 4 and Tax Rate Exponent 4 fields \r\nare used together to express the tax rate. For \r\nexample, if the value in the Tax Rate 4 field is \r\n12345 and the value in the Tax Rate Exponent 4 \r\nfield is 3, then the amount in the Tax Rate 4 \r\nfield is read as 12.345.'),
             ('25', '110', '1', 'N', 'M', 'Tax Rate Exponent 4\r\nDecimal location of  Tax Rate 4 possible values \r\nare 0 to 5\r\nThe Tax Rate 4 and Tax Rate Exponent 4 fields \r\nare used together to express the tax rate. For \r\nexample, if the value in the Tax Rate 4 field is \r\n12345 and the value in the Tax Rate Exponent 4 \r\nfield is 3, then the amount in the Tax Rate 4 \r\nfield is read as 12.345.'),
             ('26', '111-114', '4', 'AN', 'M', 'Tax Type Applied 4\r\nCode that defines a tax category that may apply \r\nto specific domestic processing arrangements.\r\nNOTEThis field may be space-filled, unless \r\ndirected otherwise by MasterCard.'),
             ('27', '115-116', '2', 'AN', 'M', 'Tax Type ID 4\r\nCode that identifies the type of tax that Tax \r\nAmount 4 represents.\r\nPossible values  \r\n00 - \r\nUnknown\r\n01 - \r\nFederal or national sales tax\r\n02 - \r\nState sales tax\r\n03 - \r\nCity sales tax\r\n04 - \r\nLocal sales tax\r\n05 - \r\nMunicipal sales tax\r\n06 - \r\nOther tax\r\n10 - \r\nValue Added Tax (VAT)\r\n11 - \r\nGoods and Services Tax (GST)\r\n12 - \r\nProvincial Sales Tax (PST)\r\n13  - \r\nHarmonied Sales Tax (HST)\r\n14 - \r\nQuebec Sales Tax (QST)\r\n20 - \r\nRoom tax\r\n21 - \r\nOccupancy tax\r\n22 - \r\nEnergy Tax\r\nSpace - Not applicable'),
             ('28', '117', '1', 'AN', 'M', 'Tax Amount Indicator 5\r\nCode that indicates how additional tax \r\ninformation is captured and reported.\r\nPossible values  \r\nY - \r\nTax included in the total purchase \r\namount\r\nN - \r\nTax not included in total purchase \r\namount\r\nSpace - Not applicable'),
             ('29', '118-129', '12', 'N', 'M', 'Tax Amount 5\r\nMonetary amount of the additional tax\r\nThe value must be right-ustified.'),
             ('30', '130-134', '5', 'N', 'M', 'Tax Rate 5\r\nTax rate applied to the purchase\r\nThe value must be right-ustified.\r\nThe Tax Rate 5 and Tax Rate Exponent 5 fields \r\nare used together to express the tax rate. For \r\nexample, if the value in the  Tax Rate 5 field is \r\n12345 and the value in the Tax Rate Exponent 5 \r\nfield is 3, then the amount in the Tax Rate 5 \r\nfield is read as 12.345.'),
             ('31', '135', '1', 'N', 'M', 'Tax Rate Exponent 5\r\nDecimal location of  Tax Rate 5 possible values \r\nare 0 to 5\r\nThe Tax Rate 5 and Tax Rate Exponent 5 fields \r\nare used together to express the tax rate. For \r\nexample, if the value in the  Tax Rate 5 field is \r\n12345 and the value in the  Tax Rate Exponent \r\n5 field is 3, then the amount in the Tax Rate 5 \r\nfield is read as 12.345.'),
             ('32', '136-139', '4', 'AN', 'M', 'Tax Type Applied 5\r\nCode that defines a tax category that may apply \r\nto specific domestic processing arrangements.\r\nNOTEThis field may be space-filled, unless \r\ndirected otherwise by MasterCard.'),
             ('33', '140-141', '2', 'AN', 'M', 'Tax Type ID 5\r\nCode that identifies the type of tax that Tax \r\nAmount 5 represents.\r\nPossible values  \r\n00 - \r\nUnknown\r\n01 - \r\nFederal or national sales tax\r\n02 - \r\nState sales tax\r\n03 - \r\nCity sales tax\r\n04 - \r\nLocal sales tax\r\n05 - \r\nMunicipal sales tax\r\n06 - \r\nOther tax\r\n10 - \r\nValue Added Tax (VAT)\r\n11 - \r\nGoods and Services Tax (GST)\r\n12 - \r\nProvincial Sales Tax (PST)\r\n13  - \r\nHarmonied Sales Tax (HST)\r\n14 - \r\nQuebec Sales Tax (QST)\r\n20 - \r\nRoom tax\r\n21 - \r\nOccupancy tax\r\n22 - \r\nEnergy Tax\r\nSpace - Not applicable'),
             ('34', '142', '1', 'AN', 'M', 'Tax Amount Indicator 6\r\nCode that indicates how additional tax \r\ninformation is captured and reported.\r\nPossible values  \r\nY - \r\nTax included in the total purchase \r\namount\r\nN - \r\nTax not included in total purchase \r\namount\r\nSpace - Not applicable'),
             ('35', '143-154', '12', 'N', 'M', 'Tax Amount 6\r\nMonetary amount of the additional tax\r\nThe value must be right-ustified.'),
             ('36', '155-159', '5', 'N', 'M', 'Tax Rate 6\r\nTax rate applied to the purchase\r\nThe value must be right-ustified.\r\nThe Tax Rate 6 and Tax Rate Exponent 6 fields \r\nare used together to express the tax rate. For \r\nexample, if the value in the Tax Rate 6 field is \r\n12345 and the value in the Tax Rate Exponent 6 \r\nfield is 3, then the amount in the Tax Rate 6 \r\nfield is read as 12.345.'),
             ('37', '160', '1', 'N', 'M', 'Tax Rate Exponent 6\r\nDecimal location of  Tax Rate 6 possible values \r\nare 0 to 5\r\nThe Tax Rate 6 and Tax Rate Exponent 6 fields \r\nare used together to express the tax rate. For \r\nexample, if the value in the Tax Rate 6 field is \r\n12345 and the value in the Tax Rate Exponent 6 \r\nfield is 3, then the amount in the Tax Rate 6 \r\nfield is read as 12.345.'),
             ('38', '161-164', '4', 'AN', 'M', 'Tax Type Applied 6\r\nCode that defines a tax category that may apply \r\nto specific domestic processing arrangements.\r\nThis field may be space-filled, unless directed \r\notherwise by MasterCard.'),
             ('39', '165-166', '2', 'AN', 'M', 'Tax Type ID 6\r\nCode that identifies the type of tax that Tax \r\nAmount 6 represents.\r\nPossible values  \r\n00 - \r\nUnknown\r\n01 - \r\nFederal or national sales tax\r\n02 - \r\nState sales tax\r\n03 - \r\nCity sales tax\r\n04 - \r\nLocal sales tax\r\n05 - \r\nMunicipal sales tax\r\n06 - \r\nOther tax\r\n10 - \r\nValue Added Tax (VAT)\r\n11 - \r\nGoods and Services Tax (GST)\r\n12 - \r\nProvincial Sales Tax (PST)\r\n13  - \r\nHarmonied Sales Tax (HST)\r\n14 - \r\nQuebec Sales Tax (QST)\r\n20 - \r\nRoom tax\r\n21 - \r\nOccupancy tax\r\n22 - \r\nEnergy Tax\r\nSpace - Not applicable'),
             ('40', '167-196', '30', 'AN', 'V', 'Buyer/Recipient Name\r\nThis  value is required on transactions greater \r\nthan 150.00'),
             ('41', '197-251', '55', 'AN', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('42', '252-256', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nThe value in this field indicates the type of \r\nextension record that follows.'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "taxAmountIndicator1": None,
        "taxAmount1": None,
        "taxRate1": None,
        "taxRateExponent1": None,
        "taxTypeApplied1": None,
        "taxTypeId1": None,
        "taxAmountIndicator2": None,
        "taxAmount2": None,
        "taxRate2": None,
        "taxRateExponent2": None,
        "taxTypeApplied2": None,
        "taxTypeId2": None,
        "taxAmountIndicator3": None,
        "taxAmount3": None,
        "taxRate3": None,
        "taxRateExponent3": None,
        "taxTypeApplied3": None,
        "taxTypeId3": None,
        "taxAmountIndicator4": None,
        "taxAmount4": None,
        "taxRate4": None,
        "taxRateExponent4": None,
        "taxTypeApplied4": None,
        "taxTypeId4": None,
        "taxAmountIndicator5": None,
        "taxAmount5": None,
        "taxRate5": None,
        "taxRateExponent5": None,
        "taxTypeApplied5": None,
        "taxTypeId5": None,
        "taxAmountIndicator6": None,
        "taxAmount6": None,
        "taxRate6": None,
        "taxRateExponent6": None,
        "taxTypeApplied6": None,
        "taxTypeId6": None,
        "buyerRecipientName": None,
        "reservedForFutureUse": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.taxAmountIndicator1,
        self.taxAmount1,
        self.taxRate1,
        self.taxRateExponent1,
        self.taxTypeApplied1,
        self.taxTypeId1,
        self.taxAmountIndicator2,
        self.taxAmount2,
        self.taxRate2,
        self.taxRateExponent2,
        self.taxTypeApplied2,
        self.taxTypeId2,
        self.taxAmountIndicator3,
        self.taxAmount3,
        self.taxRate3,
        self.taxRateExponent3,
        self.taxTypeApplied3,
        self.taxTypeId3,
        self.taxAmountIndicator4,
        self.taxAmount4,
        self.taxRate4,
        self.taxRateExponent4,
        self.taxTypeApplied4,
        self.taxTypeId4,
        self.taxAmountIndicator5,
        self.taxAmount5,
        self.taxRate5,
        self.taxRateExponent5,
        self.taxTypeApplied5,
        self.taxTypeId5,
        self.taxAmountIndicator6,
        self.taxAmount6,
        self.taxRate6,
        self.taxRateExponent6,
        self.taxTypeApplied6,
        self.taxTypeId6,
        self.buyerRecipientName,
        self.reservedForFutureUse,
        self.extensionRecordIndicator = (None)*42
        self.data = f.read(TaxExtensionRecord.LENGTH)
        super(TaxExtensionRecord, self).__init__()
        
class PurchasingCard1ExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nA list of transaction codes can be found on \r\nthe Inquire Status Record (ISR) screen of \r\nthe TSYS Accounting (TSA) System.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator identifies this record \r\nas a Purchasing Card 1 Extension Record.\r\nRequired value  PURC1'),
             ('4a', '17-28', '12', 'N', 'V', 'Visa Value-Added Tax (VAT) Amount, or \r\nShipping and Freight Amount\r\nMonetary amount of VAT assessed on the \r\ntransaction, or the monetary amount of \r\nshipping and freight charges assessed on the \r\ntransaction.'),
             ('4b', '29-32', '4', 'N', 'V', 'Visa VAT Rate, or Shipping and Freight \r\nRate\r\nVAT rate used to assess taxes on the \r\ntransaction, or shipping and freight rate \r\nused to assess charges on the transaction.'),
             ('5', '17-33', '17', 'AN', 'M', 'MasterCard Unique Invoice Number\r\nThe unique invoice number is assigned by \r\nthe card acceptor to help identify the \r\ntransaction. \r\nWhen provided, this information should be \r\nleft-ustified.'),
             ('4c', '33', '1', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('6', '34-36', '3', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('7a-1', '37-53', '17', 'AN', 'VX', 'Visa  Customer Code/Customer Reference \r\nIdentifier (CRI)\r\nAmerican Express Cardmember Reference \r\nNumber\r\nThis number is defined by the cardmember. \r\nIt is entered by the merchant at the point of \r\nsale. The number displays during the \r\nStatement/Reporting process and may \r\ninclude accounting information specific to \r\nthe client.\r\nFor American Express, this number is left-\r\nustified and can be filled with spaces.'),
             ('7a-2', '54-56', '3', 'AN', 'V, X', 'Reserved for future use'),
             ('7a-3', '57-61', '5', 'N', 'V', 'Local Tax Rate (three decimals implied)'),
             ('7b', '37-61', '25', 'AN', 'M', 'MasterCard Customer Code\r\nWhen provided, this field should contain a \r\nvalue that a commercial cardholder supplied \r\nto the merchant. It must be left-ustified and \r\nmay contain up to 25 positions. '),
             ('8a', '62', '1', 'AN', 'V', 'Visa Local Tax Included Indicator\r\nPossible values  \r\n0 - \r\nno tax included\r\n1 - \r\nstate or provincial tax included\r\n2 - \r\nnon-taxable transaction'),
             ('8b', '62', '1', 'AN', 'M', 'MasterCard Tax Exempt Indicator\r\nIdentifies whether the goods or services \r\nwere tax-exempt.\r\nPossible values  \r\nSpace - \r\nUnknown or not applicable\r\n0 - \r\nNo tax collected\r\n1 - \r\nTax exempt'),
             ('9', '63-74', '12', 'N', 'MSCVAPN', 'Visa Local Tax Amount\r\nFor Visa, this field has two implied decimal \r\npositions and can contain all eros. It is used \r\nto house the amount of state or provincial \r\ntax included in the transaction amount (see \r\nthe Transaction Amount field in the \r\nFinancial Record).\r\nNote\r\nThe currency type must be the same for this field \r\nand the Transaction Amount field.\r\nMasterCard Tax Amount\r\nDiscover Tax Amount\r\nSales Tax'),
             ('10', '75-86', '12', 'N', 'V, MCAPN', 'Freight/Shipping Amount\r\nFor Visa, this field has two implied decimal \r\npositions and can contain all eros.\r\nFreight/Shipping/Handling '),
             ('11', '87-96', '10', 'AN', 'V, MSCAPN', 'Visa and MasterCard Destination Postal \r\nCode/IP code\r\nDiscover Destination IP code to which \r\nthe merchandise was shipped.\r\nAmerican Express IP code to which the \r\nmerchandise was shipped.\r\nFor American Express, this field must be \r\nleft-ustified.'),
             ('12', '97-100', '4', 'AN', 'M', 'Merchant Type Code'),
             ('13', '101-112', '12', 'N', 'V, MCAPN', 'Duty Amount\r\nFor Visa, this field has two implied decimal \r\npositions and can contain all eros.\r\nSurcharge'),
             ('14', '113-122', '10', 'AN', 'M', 'Merchant Tax Identifier'),
             ('15', '123-132', '10', 'AN', 'V, MS', 'Ship from Postal Code/IP code\r\nOriginating IP\r\nPostal code or IP code used by the \r\nlocation from which the merchandise was \r\nshipped.'),
             ('16', '133', '1', 'AN', 'VM', 'Visa  National Tax Included Indicator\r\nPossible values  \r\n0 - \r\nnon-taxable\r\n1 - \r\nsubect to tax\r\nMasterCard  Alternate Tax Amount \r\nIndicator'),
             ('17', '134-145', '12', 'AN', 'VM', 'Visa National Tax Amount\r\nFor Visa, this field must contain the amount \r\nof national tax included in the transaction \r\namount. The field has two implied decimal \r\npositions and can contain all eros. The \r\ncurrency must be the same as the source \r\namount.\r\nMasterCard Alternate Tax Amount'),
             ('18', '146-157', '12', 'N', 'V', 'Other Tax'),
             ('19', '158-160', '3', 'AN', 'V, M, S', 'Destination Country Code\r\nFor Visa, this field may contain a valid \r\nnumeric ISO country code. For MasterCard \r\nand Discover, this field may contain a valid \r\nalphabetic ISO country code.'),
             ('20', '161-177', '17', 'AN', 'M', 'Merchant Reference Number'),
             ('21', '178-189', '12', 'AN', 'VCAPN', 'Discount Amount\r\nReward Program Transaction'),
             ('22a-1', '190-202', '13', 'AN', 'V', 'Merchant VAT Registration or Single \r\nBusiness Reference Number (SBRN)'),
             ('22a-2', '203-215', '13', 'AN', 'V', 'Customer VAT Registration Number'),
             ('22a-3', '216-219', '4', 'AN', 'V', 'Commodity Summary'),
             ('22b', '190-219', '30', 'AN', 'CAPN', 'Retail Department Name\r\nName of the department within the store \r\nwhere the transaction occurred. \r\nThis field must be left-ustified. You can use \r\nspaces as filler.'),
             ('23', '220-235', '16', 'AN', 'V', 'VAT Invoice Reference Number'),
             ('24', '236-241', '6', 'AN', 'V', 'Order Date'),
             ('25', '242', '1', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nPossible values  \r\nSpace - \r\nno extension record follows\r\nD  - \r\na PURC2 record follows\r\nT - \r\na TEMP1 record follows\r\nS  - \r\na SHIP1 record follows'),
             ('26', '243', '1', 'A', 'M', 'Total Tax Amount Sign\r\nSubfield 3 of Total Tax Amount field \r\nindicates whether the total tax amount is a \r\ndebit or credit. The total tax amount is the \r\ntotal amount of sales tax or VAT (Value \r\nAdded Tax) on the total purchase amount.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('27', '244', '1', 'A', 'VM', 'Freight/Shipping Amount Signage\r\nPossible values  \r\nD - \r\nFreight/Shipping amount is \r\nconsidered positive and represents \r\na cost on the invoice\r\nC - \r\nFreight/Shipping amount is \r\nconsidered negative and represents \r\na refund on the invoice\r\nFreight Amount Sign\r\nSubfield 3 of Freight Amount field \r\nindicates whether the freight amount is a \r\ndebit or credit. The freight amount contains \r\nthe freight charges on total purchases.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('28', '245', '1', 'A', 'VM', 'Duty Amount Signage\r\nPossible values  \r\nD - \r\nDuty amount is considered positive \r\nand represents a cost on the invoice\r\nC - \r\nDuty amount is considered negative \r\nand represents a refund on the \r\ninvoice\r\nDuty Amount Sign\r\nSubfield 3 of Duty Amount field indicates \r\nwhether the duty amount is a debit or credit. \r\nThe duty amount is the duty on the total \r\npurchase amount.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('29', '246', '1', 'N', 'V', 'Invoice Level Discount Treatment Code\r\nPossible values  \r\n0 - \r\nNo invoice level discount provided\r\n1 - \r\nTax was calculated on the post-\r\ndiscount invoice total\r\n2 - \r\nTax was calculated on the pre-\r\ndiscount invoice total\r\nSpace - \r\nField not in use'),
             ('30', '247', '1', 'N', 'V', 'Tax Treatment\r\nPossible values  \r\n0 - \r\nNet prices with tax calculated at \r\nline item level\r\n1 - \r\nNet prices with tax calculated at \r\ninvoice level\r\n2 - \r\nGross prices given with tax \r\ninformation at line item level\r\n3 - \r\nGross prices given with tax \r\ninformation provided at invoice \r\nlevel\r\n4 - \r\nNo tax applies (small supplier) \r\non the invoice for the \r\ntransaction\r\nSpace - \r\nField not in use'),
             ('31', '248', '1', 'AN', 'V', 'VAT/Tax Amount (Freight/Shipping) \r\nSignage\r\nPossible values  \r\nD - \r\nVAT/tax amount is considered \r\npositive   for   the   invoice                                                                                 \r\nC - \r\nVAT/tax amount is considered \r\nnegative for the invoice'),
             ('32', '249', '1', 'AN', 'V', 'Discount Amount Signage \r\nPossible values  \r\nD  - \r\nDiscount amount is considered a \r\ndiscount for the invoice\r\nC - \r\nDiscount amount is considered a \r\ndiscount refund for the invoice '),
             ('33', '250-256', '7', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use.'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "visaValueAddedTaxVatAmountOr": None,
        "visaVatRateOrShippingAndFreight": None,
        "mastercardUniqueInvoiceNumber": None,
        "reservedForFutureUse4c": None,
        "reservedForFutureUse6": None,
        "visaCustomerCodeCustomerReference": None,
        "reservedForFutureUse7a-2": None,
        "localTaxRateThreeDecimalsImplied": None,
        "mastercardCustomerCode": None,
        "visaLocalTaxIncludedIndicator": None,
        "mastercardTaxExemptIndicator": None,
        "visaLocalTaxAmount": None,
        "freightShippingAmount": None,
        "visaAndMastercardDestinationPostal": None,
        "merchantTypeCode": None,
        "dutyAmount": None,
        "merchantTaxIdentifier": None,
        "shipFromPostalCodeIpCode": None,
        "visaNationalTaxIncludedIndicator": None,
        "visaNationalTaxAmount": None,
        "otherTax": None,
        "destinationCountryCode": None,
        "merchantReferenceNumber": None,
        "discountAmount": None,
        "merchantVatRegistrationOrSingle": None,
        "customerVatRegistrationNumber": None,
        "commoditySummary": None,
        "retailDepartmentName": None,
        "vatInvoiceReferenceNumber": None,
        "orderDate": None,
        "extensionRecordIndicator": None,
        "totalTaxAmountSign": None,
        "freightShippingAmountSignage": None,
        "dutyAmountSignage": None,
        "invoiceLevelDiscountTreatmentCode": None,
        "taxTreatment": None,
        "vatTaxAmountFreightShipping": None,
        "discountAmountSignage": None,
        "reservedForFutureUse33": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.visaValueAddedTaxVatAmountOr,
        self.visaVatRateOrShippingAndFreight,
        self.mastercardUniqueInvoiceNumber,
        self.reservedForFutureUse4c,
        self.reservedForFutureUse6,
        self.visaCustomerCodeCustomerReference,
        self.reservedForFutureUse7a-2,
        self.localTaxRateThreeDecimalsImplied,
        self.mastercardCustomerCode,
        self.visaLocalTaxIncludedIndicator,
        self.mastercardTaxExemptIndicator,
        self.visaLocalTaxAmount,
        self.freightShippingAmount,
        self.visaAndMastercardDestinationPostal,
        self.merchantTypeCode,
        self.dutyAmount,
        self.merchantTaxIdentifier,
        self.shipFromPostalCodeIpCode,
        self.visaNationalTaxIncludedIndicator,
        self.visaNationalTaxAmount,
        self.otherTax,
        self.destinationCountryCode,
        self.merchantReferenceNumber,
        self.discountAmount,
        self.merchantVatRegistrationOrSingle,
        self.customerVatRegistrationNumber,
        self.commoditySummary,
        self.retailDepartmentName,
        self.vatInvoiceReferenceNumber,
        self.orderDate,
        self.extensionRecordIndicator,
        self.totalTaxAmountSign,
        self.freightShippingAmountSignage,
        self.dutyAmountSignage,
        self.invoiceLevelDiscountTreatmentCode,
        self.taxTreatment,
        self.vatTaxAmountFreightShipping,
        self.discountAmountSignage,
        self.reservedForFutureUse33 = (None)*42
        self.data = f.read(PurchasingCard1ExtensionRecord.LENGTH)
        super(PurchasingCard1ExtensionRecord, self).__init__()
        
class PurchasingCard2ExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nA list of transaction codes can be found on \r\nthe Inquire Status Record (ISR) screen of \r\nthe TSYS Accounting (TSA) System.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator identifies this record \r\nas a Purchasing Card 2 Extension Record.\r\nRequired value  PURC2'),
             ('4', '17-35', '19', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('5', '36', '1', 'AN', 'MS', 'Discount Indicator\r\nLine Item Discount Indicator\r\nCode that indicates if a discount amount \r\nwas applied to the transaction.\r\nPossible values  \r\nY - \r\ndiscount applied\r\nN - \r\nno discount applied\r\nSpace - \r\nInformation is not available'),
             ('6', '37-45', '9', 'AN', 'V, MS', 'Discount Amount\r\nLine Item Discount Amount'),
             ('7', '46-60', '15', 'AN', 'M', 'Alternate Tax Identifier'),
             ('8', '61-72', '12', 'AN', 'V, MS', 'Product Code\r\nLine Item Product Code'),
             ('9', '73-75', '3', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('10b-1', '76-110', '35', 'AN', 'MS', 'Item Description \r\nLine Item Description'),
             ('10a-2', '102-110', '9', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use.'),
             ('10c-1', '76-115', '40', 'AN', 'CAPN', 'Charge Description\r\nDescription of the purchase. American \r\nExpress allows you to enter up to four \r\ncharge descriptions. You should enter each \r\ndescription on a separate PURC2 extension \r\nrecord.\r\nThis field must be left-ustified.'),
             ('10c-2', '116-122', '7', 'N', 'CAPN', 'Charge Item Quantity 1\r\nQuantity of the item described in the Charge \r\nDescription field that was purchased. \r\nThis field must be right-ustified. You can \r\nuse eroes as filler.\r\nUp to four Charge l Item Quantities are \r\npossible. They need to be sent in subsequent \r\nPURC2 records.'),
             ('10a-3', '111-122', '12', 'AN', 'V', 'Item Quantity'),
             ('10b-2', '111-122', '12', 'AN', 'MS', 'Item Quantity\r\nLine Item Quantity'),
             ('11', '123-134', '12', 'AN', 'VMS', 'Unit of Measure/Code\r\nItem Unit of Measure\r\nLine Item Unit of Measure'),
             ('12', '135-146', '12', 'N', 'VMCAPN', 'Unit Cost\r\nExtended Item Amount\r\nCannot be all eroes or spaces.\r\nCharge Item Amount 1\r\nCost for each unit of the item described in \r\nthe Charge Description field. \r\nThis field must be right-ustified. You can \r\nuse eroes as filler.\r\nUp to four Charge Item Amounts are \r\npossible. They need to be sent in subsequent \r\nPURC2 records.'),
             ('13', '147', '1', 'AN', 'M', 'Detail Tax Amount Indicator 1\r\nPossible values  \r\nN - \r\nTax not included in total purchase \r\namount\r\nY - \r\nTax included in total purchase \r\namount \r\nSpace - \r\nNot supported'),
             ('14', '148-152', '5', 'N', 'V', 'Visa  Value-added tax (VAT)/Tax Rate'),
             ('15', '153-156', '4', 'AN', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('16', '157-168', '12', 'AN', 'VM', 'Visa  VAT/Tax Amount\r\nMasterCard  Tax Amount'),
             ('17', '169', '1', 'AN', 'MSV', 'Debit/Credit Indicator\r\nLine Item Debit/Credit Indicator\r\nCode that indicates if the transaction \r\namount is a debit or a credit.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit\r\nSpace - \r\nInformation not available'),
             ('18', '170-171', '2', 'AN', 'V', 'Type of Supply'),
             ('19', '172', '1', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nPossible values  \r\nSpace - \r\nno extension record follows\r\nD - \r\nanother Purchasing Card 2 \r\nExtension Record follows'),
             ('20', '173-184', '12', 'AN', 'V', 'Commodity Code'),
             ('21', '185-196', '12', 'N', 'V, M, S', 'Visa Line Item Total\r\nMasterCard Line Item Total Amount\r\nDiscover Total Amount\r\nTotal amount of all line items from each \r\nPURC2 record.'),
             ('22', '197', '1', 'AN', 'M', 'MasterCard Item Quantity Exponent\r\nIndicates the decimal location for the Item \r\nQuantity field.'),
             ('23', '198-202', '5', 'AN', 'M, S', 'MasterCard Item Discount Rate\r\nDiscover Line Item Discount Rate\r\nThe discount rate applied to the individual \r\nitem purchased.\r\nFor MasterCard, this field must contain a \r\nfive -digit numeric value.'),
             ('24', '203', '1', 'AN', 'M', 'Item Discount Rate Exponent\r\nIndicates the decimal location for the item \r\ndiscount rate.'),
             ('25', '204-215', '12', 'N', 'M', 'Unit Price\r\nPrice for one unit of the product\r\nNOTEThe implied decimal for the Unit Price \r\nmust be the same as the implied decimal for the \r\nTransaction Amount in the Draft 256 Financial \r\nRecord (DF256).'),
             ('26', '216', '1', 'N', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('27', '217-218', '2', 'AN', 'S', 'Line Item Tax Type\r\nThis field indicates the type of tax collected \r\nin relationship to a specific tax amount and \r\nmay contain spaces.'),
             ('28', '219-224', '6', 'N', 'M', 'Line Item Date\r\nThe purchase date of the item referenced in \r\nthe associated Corporate Card Line Item \r\nDetail (YYMMDD).'),
             ('29', '225', '1', 'A', 'M', 'Total Tax Amount Sign\r\nSubfield 3 of the Total Tax Amount field \r\nindicates whether the total tax amount is a \r\ndebit or credit. The total tax amount of the \r\ntotal amount of sales tax or VAT on the \r\ntotal purchase amount.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('30', '226', '1', 'A', 'M', 'Extended Amount Sign\r\nSubfield 3 of the Extended Item Amount \r\nfield indicates whether the extended item \r\namount is a debit or credit. The extended \r\nitem amount is the individual item amount \r\nthat is normally calculated as price \r\nmultiplied by quantity.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('31', '227', '1', 'A', 'M', 'Item Discount Amount Sign\r\nSubfield 5 of the Item Discount field \r\nindicates whether the item discount is a \r\ndebit or credit. The item discount contains \r\nthe item discount indicator and amount.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('32', '228', '1', 'A', 'M', 'Line Item Amount Sign \r\nSubfield 3 of the Line Item Total Amount \r\nfield indicates whether the line item total \r\namount is a debit or credit. The line item \r\ntotal amount is the total amount of the line \r\nitem.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('33', '229', '1', 'AN', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('34', '230-233', '4', 'A', 'M', 'Reserved for future use.'),
             ('35', '234', '1', 'N', 'V', 'Line Item Level Discount Treatment Code\r\nPossible values  \r\n0 - \r\nNo line level discount provided\r\n1 - \r\nTax was calculated on the post-\r\ndiscount line item total\r\n2 - \r\nTax was calculated on the pre-\r\ndiscount line item total\r\nSpace - \r\nField not in use'),
             ('36', '235-256', '22', 'A', 'M', 'Reserved for future use.'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "reservedForFutureUse4": None,
        "discountIndicator": None,
        "discountAmount": None,
        "alternateTaxIdentifier": None,
        "productCode": None,
        "reservedForFutureUse9": None,
        "itemDescription": None,
        "reservedForFutureUse10a-2": None,
        "chargeDescription": None,
        "chargeItemQuantity1": None,
        "itemQuantity10a-3": None,
        "itemQuantity10b-2": None,
        "unitOfMeasureCode": None,
        "unitCost": None,
        "detailTaxAmountIndicator1": None,
        "visaValueAddedTaxVatTaxRate": None,
        "reservedForFutureUse15": None,
        "visaVatTaxAmount": None,
        "debitCreditIndicator": None,
        "typeOfSupply": None,
        "extensionRecordIndicator": None,
        "commodityCode": None,
        "visaLineItemTotal": None,
        "mastercardItemQuantityExponent": None,
        "mastercardItemDiscountRate": None,
        "itemDiscountRateExponent": None,
        "unitPrice": None,
        "reservedForFutureUse26": None,
        "lineItemTaxType": None,
        "lineItemDate": None,
        "totalTaxAmountSign": None,
        "extendedAmountSign": None,
        "itemDiscountAmountSign": None,
        "lineItemAmountSign": None,
        "reservedForFutureUse33": None,
        "reservedForFutureUse34": None,
        "lineItemLevelDiscountTreatmentCode": None,
        "reservedForFutureUse36": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.reservedForFutureUse4,
        self.discountIndicator,
        self.discountAmount,
        self.alternateTaxIdentifier,
        self.productCode,
        self.reservedForFutureUse9,
        self.itemDescription,
        self.reservedForFutureUse10a-2,
        self.chargeDescription,
        self.chargeItemQuantity1,
        self.itemQuantity10a-3,
        self.itemQuantity10b-2,
        self.unitOfMeasureCode,
        self.unitCost,
        self.detailTaxAmountIndicator1,
        self.visaValueAddedTaxVatTaxRate,
        self.reservedForFutureUse15,
        self.visaVatTaxAmount,
        self.debitCreditIndicator,
        self.typeOfSupply,
        self.extensionRecordIndicator,
        self.commodityCode,
        self.visaLineItemTotal,
        self.mastercardItemQuantityExponent,
        self.mastercardItemDiscountRate,
        self.itemDiscountRateExponent,
        self.unitPrice,
        self.reservedForFutureUse26,
        self.lineItemTaxType,
        self.lineItemDate,
        self.totalTaxAmountSign,
        self.extendedAmountSign,
        self.itemDiscountAmountSign,
        self.lineItemAmountSign,
        self.reservedForFutureUse33,
        self.reservedForFutureUse34,
        self.lineItemLevelDiscountTreatmentCode,
        self.reservedForFutureUse36 = (None)*41
        self.data = f.read(PurchasingCard2ExtensionRecord.LENGTH)
        super(PurchasingCard2ExtensionRecord, self).__init__()
        
class RestaurantExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nA list of transaction codes can be found on \r\nthe Inquire Status Record (ISR) screen of \r\nthe TSYS Accounting (TSA) System.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator identifies this record \r\nas a Restaurant Extension Record.\r\nRequired value  AMEXR'),
             ('4', '17', '1', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('5', '18-32', '15', 'AN', 'X', 'Record of Charge'),
             ('6', '33-38', '6', 'N', 'X', 'Tax Amount'),
             ('7', '39-46', '8', 'AN', 'X', 'Food Description\r\nPossible values  \r\nFOOD\r\nBEVERAGE\r\nFOOD-BEV'),
             ('8', '47-54', '8', 'N', 'X', 'Food Amount'),
             ('9', '55-62', '8', 'N', 'X', 'Beverage Amount'),
             ('10', '63-70', '8', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('11', '71-78', '8', 'N', 'X', 'Tip Amount'),
             ('12', '79-94', '16', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('13', '95-96', '2', 'AN', 'X', 'Approval Code'),
             ('14', '97-256', '160', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "reservedForFutureUse4": None,
        "recordOfCharge": None,
        "taxAmount": None,
        "foodDescription": None,
        "foodAmount": None,
        "beverageAmount": None,
        "reservedForFutureUse10": None,
        "tipAmount": None,
        "reservedForFutureUse12": None,
        "approvalCode": None,
        "reservedForFutureUse14": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.reservedForFutureUse4,
        self.recordOfCharge,
        self.taxAmount,
        self.foodDescription,
        self.foodAmount,
        self.beverageAmount,
        self.reservedForFutureUse10,
        self.tipAmount,
        self.reservedForFutureUse12,
        self.approvalCode,
        self.reservedForFutureUse14 = (None)*14
        self.data = f.read(RestaurantExtensionRecord.LENGTH)
        super(RestaurantExtensionRecord, self).__init__()
        
class RetailExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nA list of transaction codes can be found on \r\nthe Inquire Status Record (ISR) screen of \r\nthe TSYS Accounting (TSA) System.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator identifies this record \r\nas a Retail Extension Record.\r\nRequired value  RETAL'),
             ('4', '17', '1', 'AN', '', 'Transaction Indicator\r\nPossible values  \r\nSpace - \r\nnot applicable\r\nC - \r\nsame as cash, based on a fixed date\r\nD - \r\ndeferred, based on number of days\r\nF - \r\ndeferred, based on a fixed date\r\nI - \r\ninstallment\r\nS - \r\nsame as cash, based on number of \r\ndays'),
             ('5b-1', '18-21', '4', 'AN', '', 'Number of Days\r\nIf the Transaction Indicator is based on the \r\nnumber of days, this field must contain that \r\nnumber.'),
             ('5c-1', '18-21', '4', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('5a', '18-23', '6', 'AN', '', 'Expiration Date for Transaction Indicator\r\nIf the Transaction Indicator is based on a \r\nfixed date, this field must contain that date.\r\nFormat  MMDDYY'),
             ('5c-2', '22-23', '2', 'AN', '', 'Number of Installments\r\nIf the Transaction Indicator is an I, this \r\nfield must contain the number of \r\ninstallments for the transaction.'),
             ('5b-2', '22-23', '2', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('6', '24', '1', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('7', '25-28', '4', 'AN', '', 'Deferred Plan Type'),
             ('8', '29-33', '5', 'AN', '', 'Transaction/Receipt Number'),
             ('9', '34-35', '2', 'AN', '', 'Deferred Month'),
             ('10', '36-44', '9', 'N', 'P', 'Base Points\r\nThis field has two implied decimal positions.'),
             ('11', '45-53', '9', 'N', 'P', 'Store Points\r\nThis field has two implied decimal positions.'),
             ('12', '54-62', '9', 'N', 'P', 'Product Points\r\nThis field has two implied decimal positions.'),
             ('13', '63-71', '9', 'N', 'P', 'Redemption Points'),
             ('14', '72-80', '9', 'N', 'P', 'Promotion Points\r\nThis field has two implied decimal positions.'),
             ('15', '81-85', '5', 'AN', '', 'Register Number'),
             ('16', '86', '1', 'AN', '', 'Redemption Type\r\nPossible values  \r\nF - \r\nfixed amount\r\nP - \r\npercentage of transaction'),
             ('17', '87-93', '7', 'N', '', 'Redemption Dollar Amount\r\nThis field has two implied decimal positions.'),
             ('18', '94', '1', 'AN', 'P', 'Flag for Negative Base Points'),
             ('19', '95', '1', 'AN', 'P', 'Flag for Negative Store Points'),
             ('20', '96', '1', 'AN', 'P', 'Flag for Negative Product Points'),
             ('21', '97', '1', 'AN', 'P', 'Flag for Negative Redemption Points'),
             ('22', '98', '1', 'AN', 'P', 'Flag for Negative Promotion Points'),
             ('23', '99-100', '2', 'AN', '', 'Number of Months for Transaction \r\nIndicator'),
             ('24', '101-120', '20', 'AN', '', 'Purchase Order Number'),
             ('25', '121-122', '2', 'AN', '', 'Frequency of Installments'),
             ('26', '123-145', '23', 'AN', 'P', '23-Digit Reference Number'),
             ('27', '146-155', '10', 'AN', 'P', 'Postal Code'),
             ('28', '156-251', '96', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('29', '252-256', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nPossible values  \r\nSpace - \r\nno extension record follows\r\nGENER - a Generic Extension Record \r\nfollows'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "transactionIndicator": None,
        "numberOfDays": None,
        "reservedForFutureUse5c-1": None,
        "expirationDateForTransactionIndicator": None,
        "numberOfInstallments": None,
        "reservedForFutureUse5b-2": None,
        "reservedForFutureUse6": None,
        "deferredPlanType": None,
        "transactionReceiptNumber": None,
        "deferredMonth": None,
        "basePoints": None,
        "storePoints": None,
        "productPoints": None,
        "redemptionPoints": None,
        "promotionPoints": None,
        "registerNumber": None,
        "redemptionType": None,
        "redemptionDollarAmount": None,
        "flagForNegativeBasePoints": None,
        "flagForNegativeStorePoints": None,
        "flagForNegativeProductPoints": None,
        "flagForNegativeRedemptionPoints": None,
        "flagForNegativePromotionPoints": None,
        "numberOfMonthsForTransaction": None,
        "purchaseOrderNumber": None,
        "frequencyOfInstallments": None,
        "digitReferenceNumber23": None,
        "postalCode": None,
        "reservedForFutureUse28": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.transactionIndicator,
        self.numberOfDays,
        self.reservedForFutureUse5c-1,
        self.expirationDateForTransactionIndicator,
        self.numberOfInstallments,
        self.reservedForFutureUse5b-2,
        self.reservedForFutureUse6,
        self.deferredPlanType,
        self.transactionReceiptNumber,
        self.deferredMonth,
        self.basePoints,
        self.storePoints,
        self.productPoints,
        self.redemptionPoints,
        self.promotionPoints,
        self.registerNumber,
        self.redemptionType,
        self.redemptionDollarAmount,
        self.flagForNegativeBasePoints,
        self.flagForNegativeStorePoints,
        self.flagForNegativeProductPoints,
        self.flagForNegativeRedemptionPoints,
        self.flagForNegativePromotionPoints,
        self.numberOfMonthsForTransaction,
        self.purchaseOrderNumber,
        self.frequencyOfInstallments,
        self.digitReferenceNumber23,
        self.postalCode,
        self.reservedForFutureUse28,
        self.extensionRecordIndicator = (None)*33
        self.data = f.read(RetailExtensionRecord.LENGTH)
        super(RetailExtensionRecord, self).__init__()
        
class MasterCardShippingServicesExtensionRecordFormat1(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nEach record must contain a sequence \r\nnumber to identify its position within the \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nThe transaction code identifies the type of \r\nrecord being transmitted.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator indicates that this \r\nrecord is a Shipping Services Format 1 \r\nExtension Record.\r\nRequired value  SHIP1'),
             ('4', '17-40', '24', 'AN', 'M', 'Service Description Code'),
             ('5', '41-62', '22', 'AN', 'M', 'Tracking Number\r\nPackage tracking number.'),
             ('6', '63-68', '6', 'N', 'M', 'Pick Up Date\r\nMasterCard required format YYMMDD, \r\nleft-ustified and space filled.'),
             ('7', '69-85', '17', 'AN', 'M', 'Customer Code'),
             ('8', '86-94', '9', 'N', 'M', 'Shipping Net Amount\r\nThis field contains two implied decimal \r\nplaces.\r\nExample 9999999.99'),
             ('9', '95-103', '9', 'N', 'M', 'Incentive Amount'),
             ('10', '104-112', '9', 'N', 'M', 'Tax Amount\r\nThis field contains two implied decimal \r\nplaces.\r\nExample 9999999.99'),
             ('11', '113-122', '10', 'AN', 'M', 'Shipping Party Postal Code'),
             ('12', '123-132', '10', 'AN', 'M', 'Delivery Party Postal Code'),
             ('13', '133-134', '2', 'AN', 'M', 'Delivery Party Country Code'),
             ('14', '135-137', '3', 'N', 'M', 'Unit of Measure'),
             ('15', '138-142', '5', 'AN', 'M', 'Package Weight'),
             ('16', '143-147', '5', 'N', 'M', 'Number of Packages'),
             ('17', '148-153', '4', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use.'),
             ('18', '154-178', '25', 'AN', 'M', 'Shipping Party City'),
             ('19', '179-181', '3', 'AN', 'M', 'Shipping Party State'),
             ('20', '182-184', '3', 'AN', 'M', 'Shipping Party Country'),
             ('21', '185-209', '25', 'AN', 'M', 'Delivery Party City'),
             ('22', '210-212', '3', 'AN', 'M', 'Delivery Party State'),
             ('23', '213-215', '3', 'AN', 'M', 'Delivery Party Country'),
             ('24', '216-251', '36', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use.'),
             ('25', '252-256', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nRequired value  SHIP2\r\nA SHIP2 extension record must follow the \r\nSHIP1 record.'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "serviceDescriptionCode": None,
        "trackingNumber": None,
        "pickUpDate": None,
        "customerCode": None,
        "shippingNetAmount": None,
        "incentiveAmount": None,
        "taxAmount": None,
        "shippingPartyPostalCode": None,
        "deliveryPartyPostalCode": None,
        "deliveryPartyCountryCode": None,
        "unitOfMeasure": None,
        "packageWeight": None,
        "numberOfPackages": None,
        "reservedForFutureUse17": None,
        "shippingPartyCity": None,
        "shippingPartyState": None,
        "shippingPartyCountry": None,
        "deliveryPartyCity": None,
        "deliveryPartyState": None,
        "deliveryPartyCountry": None,
        "reservedForFutureUse24": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.serviceDescriptionCode,
        self.trackingNumber,
        self.pickUpDate,
        self.customerCode,
        self.shippingNetAmount,
        self.incentiveAmount,
        self.taxAmount,
        self.shippingPartyPostalCode,
        self.deliveryPartyPostalCode,
        self.deliveryPartyCountryCode,
        self.unitOfMeasure,
        self.packageWeight,
        self.numberOfPackages,
        self.reservedForFutureUse17,
        self.shippingPartyCity,
        self.shippingPartyState,
        self.shippingPartyCountry,
        self.deliveryPartyCity,
        self.deliveryPartyState,
        self.deliveryPartyCountry,
        self.reservedForFutureUse24,
        self.extensionRecordIndicator = (None)*25
        self.data = f.read(MasterCardShippingServicesExtensionRecordFormat1.LENGTH)
        super(MasterCardShippingServicesExtensionRecordFormat1, self).__init__()
        
class MasterCardShippingServicesExtensionRecordFormat2(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nEach record must contain a sequence \r\nnumber to identify its position within the \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nThe transaction code identifies the type of \r\nrecord being transmitted.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator indicates that this is a \r\nShipping Services Format 2 Extension \r\nRecord.\r\nRequired value  SHIP2'),
             ('4', '17-41', '25', 'AN', 'M', 'Shipping Party Name'),
             ('5', '42-66', '25', 'AN', 'M', 'Shipping Party Address'),
             ('6', '67-91', '25', 'AN', 'M', 'Delivery Party Name'),
             ('7', '92-116', '25', 'AN', 'M', 'Delivery Party Address'),
             ('8', '117-177', '61', 'AN', 'M', 'Shipping Party Contact\r\nThis field contains the following two sub-\r\nfields\r\n\r\nSub-field 1 - Party contact information \r\ndescriptor, 1 byte\r\nPossible values  \r\n1 - \r\nName\r\n2 - \r\nTitle\r\n3 - \r\nTelephone\r\n4 - \r\nEmail address\r\n5 - \r\nFunction\r\n\r\nSub-field 2 - Party contact information, 60 \r\nbytes\r\nThis field must be left-ustified and cannot \r\ncontain all eroes.'),
             ('9', '178-238', '61', 'AN', 'M', 'Delivery Party Contact\r\nThis field contains the following two sub-\r\nfields\r\n\r\nSub-field 1 - Party contact information \r\ndescriptor, 1 byte\r\nPossible values  \r\n1 - \r\nName\r\n2 - \r\nTitle\r\n3 - \r\nTelephone\r\n4 - \r\nEmail address\r\n5 - \r\nFunction\r\n\r\nSub-field 2 - Party contact information, 60 \r\nbytes\r\nThis field must be left-ustified and cannot \r\ncontain all eroes.'),
             ('10', '239-251', '3', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use.'),
             ('11', '252-256', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nPossible values  \r\nBlank - \r\nno extension record follows\r\nGENER - a Generic Extension Record \r\nfollows'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "shippingPartyName": None,
        "shippingPartyAddress": None,
        "deliveryPartyName": None,
        "deliveryPartyAddress": None,
        "shippingPartyContact": None,
        "deliveryPartyContact": None,
        "reservedForFutureUse": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.shippingPartyName,
        self.shippingPartyAddress,
        self.deliveryPartyName,
        self.deliveryPartyAddress,
        self.shippingPartyContact,
        self.deliveryPartyContact,
        self.reservedForFutureUse,
        self.extensionRecordIndicator = (None)*11
        self.data = f.read(MasterCardShippingServicesExtensionRecordFormat2.LENGTH)
        super(MasterCardShippingServicesExtensionRecordFormat2, self).__init__()
        
class TelephonyBillingSummary(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nNumber that identifies the position of the \r\nrecord within the file.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nCode that identifies the type of record being \r\ntransmitted.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nIndicates a Telephony Billing Summary \r\nextension record.\r\nRequired value  TBSUM'),
             ('4', '17-56', '40', 'AN', 'M', 'User Name\r\nIndicates the user name related to the \r\nTelephony Billing information.'),
             ('5', '57-96', '40', 'AN', 'M', 'User Account Number\r\nIndicates the users account number related \r\nto Telephony Billing information.'),
             ('6', '97-121', '25', 'AN', 'M', 'User Telephone Number\r\nIndicates the users telephone number \r\nrelated to the Telephony Billing \r\ninformation.'),
             ('7', '122-127', '6', 'N', 'M', 'Statement Start Date\r\nIndicates the start date of the Billing \r\nStatement Period (YYMMDD).'),
             ('8', '128-133', '6', 'N', 'M', 'Statement End Date\r\nIndicates the end date of the Billing \r\nStatement Period (YYMMDD).'),
             ('9', '134-145', '12', 'N', 'M', 'Billing Event 1 Amount First Occurrence\r\nIndicates the amount information \r\npertaining to the first occurrence for the \r\nTelephony Billing Event.'),
             ('10', '146', '1', 'A', 'M', 'Billing Event 1 Sign First Occurrence\r\nSubfield 3 of the Billing Event 1 field \r\nindicates whether the Billing Event 1 first \r\noccurrence amount is a debit or credit. This \r\namount contains information pertaining to \r\nthe Telephony Billing event.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('11', '147-158', '12', 'N', 'M', 'Billing Event 1 Amount Second Occurrence\r\nContains information pertaining to the \r\nsecond occurrence for the Telephony \r\nBilling Event.'),
             ('12', '159', '1', 'A', 'M', 'Billing Event 1 Sign Second Occurrence\r\nSubfield 3 of the Billing Event 1 field \r\nindicates whether the Billing Event 1 second \r\noccurrence amount is a debit or credit. This \r\namount contains information pertaining to \r\nthe Telephony Billing Event.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('13', '160-171', '12', 'N', 'M', 'Billing Event 1 Amount Third Occurrence\r\nContains information pertaining to the third \r\noccurrence for the Telephony Billing Event.'),
             ('14', '172', '1', 'A', 'M', 'Billing Event 1 Sign Third Occurrence\r\nSubfield 3 of the Billing Event 1 field \r\nindicates whether the Billing Event 1 third \r\noccurrence amount is a debit or credit. This \r\namount contains information pertaining to \r\nthe Telephony Billing Event.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('15', '173-184', '12', 'N', 'M', 'Billing Event 1 Amount Fourth Occurrence\r\nContains information pertaining to the \r\nfourth occurrence for the Telephony Billing \r\nEvent.'),
             ('16', '185', '1', 'A', 'M', 'Billing Event 1 Sign Fourth Occurrence\r\nSubfield 3 of the Billing Event 1 field \r\nindicates whether the Billing Event 1 fourth \r\noccurrence amount is a debit or credit. This \r\namount contains information pertaining to \r\nthe Telephony Billing Event.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('17', '186-197', '12', 'N', 'M', 'Detail Tax Amount 1\r\nProvides additional tax information such as \r\ntax rate, tax amounts and tax type.'),
             ('18', '198', '1', 'A', 'M', 'Detail Tax Sign D/C 1\r\nSubfield 3 of the Detailed Tax Amount 1 \r\nfield indicates whether the detailed tax \r\namount is a debit or credit. The Detailed \r\nTax Amount 1 field contains additional \r\ninformation such as tax rate, tax amounts \r\nand tax type.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('19', '199-251', '53', 'AN', 'M', 'Reserved for future use.'),
             ('20', '252-256', '5', 'A', 'M', 'Extension Record Indicator\r\nIndicates that a Telephony Billing Detail \r\nrecord is to follow.\r\nPossible value  TBDET'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "userName": None,
        "userAccountNumber": None,
        "userTelephoneNumber": None,
        "statementStartDate": None,
        "statementEndDate": None,
        "billingEvent1AmountFirstOccurrence": None,
        "billingEvent1SignFirstOccurrence": None,
        "billingEvent1AmountSecondOccurrence": None,
        "billingEvent1SignSecondOccurrence": None,
        "billingEvent1AmountThirdOccurrence": None,
        "billingEvent1SignThirdOccurrence": None,
        "billingEvent1AmountFourthOccurrence": None,
        "billingEvent1SignFourthOccurrence": None,
        "detailTaxAmount1": None,
        "detailTaxSignDC1": None,
        "reservedForFutureUse": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.userName,
        self.userAccountNumber,
        self.userTelephoneNumber,
        self.statementStartDate,
        self.statementEndDate,
        self.billingEvent1AmountFirstOccurrence,
        self.billingEvent1SignFirstOccurrence,
        self.billingEvent1AmountSecondOccurrence,
        self.billingEvent1SignSecondOccurrence,
        self.billingEvent1AmountThirdOccurrence,
        self.billingEvent1SignThirdOccurrence,
        self.billingEvent1AmountFourthOccurrence,
        self.billingEvent1SignFourthOccurrence,
        self.detailTaxAmount1,
        self.detailTaxSignDC1,
        self.reservedForFutureUse,
        self.extensionRecordIndicator = (None)*20
        self.data = f.read(TelephonyBillingSummary.LENGTH)
        super(TelephonyBillingSummary, self).__init__()
        
class TelephonyBillingDetail(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nNumber that identifies the position of the \r\nrecord within the file.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nCode that identifies the type of record being \r\ntransmitted.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nIndicates a Telephony Billing Detail \r\nextension record.\r\nRequired value  TBDET'),
             ('4', '17-28', '12', 'N', 'M', 'Total Tax Amount\r\nIndicates the total amount of sales tax or \r\nVAT on the total purchase amount.'),
             ('5', '29', '1', 'A', 'M', 'Total Tax Amount Sign\r\nSubfield 3 of Total Tax Amount field \r\nindicates whether the total tax amount is a \r\ndebit or credit. The total tax amount is the \r\ntotal amount of sales tax or VAT on the \r\ntotal purchase amount.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('6', '30-35', '6', 'N', 'M', 'Call Date\r\nIndicates the date of the call related to the \r\nTelephony Billing Detail (YYMMDD).'),
             ('7', '36-41', '6', 'N', 'M', 'Call Time\r\nIndicates the time of the call related to the \r\nTelephony Billing Detail (HHMMSS).'),
             ('8', '42-61', '20', 'AN', 'M', 'Call To State/Province\r\nIndicates the state or province called for the \r\nTelephony Billing Event.'),
             ('9', '62-81', '20', 'AN', 'M', 'Call To Country\r\nIndicates the country called for the \r\nTelephony Billing Event.'),
             ('10', '82-106', '25', 'AN', 'M', 'Call To Number\r\nIndicates the phone number called for the \r\nTelephony Billing Event.'),
             ('11', '107-126', '20', 'AN', 'M', 'Call From State/Province\r\nIndicates the state or province for the \r\noriginator of the telephone call.'),
             ('12', '127-146', '20', 'AN', 'M', 'Call From Country\r\nIndicates the country for the originator of \r\nthe telephone call.'),
             ('13', '147-171', '25', 'AN', 'M', 'Call From Number\r\nIndicates the number from which the call \r\nwas made.'),
             ('14', '172-183', '12', 'N', 'M', 'Call Usage Amount\r\nIndicates the monetary amount of the call \r\nusage pertaining to the Telephony Billing \r\nEvent.'),
             ('15', '184', '1', 'A', 'M', 'Call Usage Amount Sign\r\nSubfield 3 of Call Usage Amount field \r\nindicates whether the call usage amount is a \r\ndebit or credit. The amount is the monetary \r\namount of the call usage pertaining to the \r\nTelephony Billing Detail.\r\nPossible values  \r\nD - \r\nDebit\r\nC - \r\nCredit'),
             ('16', '185-251', '67', 'AN', 'M', 'Reserved for future use.'),
             ('17', '252-256', '5', 'A', 'M', 'Extension Record Indicator\r\nIndicates that a Telephony Billing Detail \r\nrecord is to follow.\r\nPossible value  TBDET'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "totalTaxAmount": None,
        "totalTaxAmountSign": None,
        "callDate": None,
        "callTime": None,
        "callToStateProvince": None,
        "callToCountry": None,
        "callToNumber": None,
        "callFromStateProvince": None,
        "callFromCountry": None,
        "callFromNumber": None,
        "callUsageAmount": None,
        "callUsageAmountSign": None,
        "reservedForFutureUse": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.totalTaxAmount,
        self.totalTaxAmountSign,
        self.callDate,
        self.callTime,
        self.callToStateProvince,
        self.callToCountry,
        self.callToNumber,
        self.callFromStateProvince,
        self.callFromCountry,
        self.callFromNumber,
        self.callUsageAmount,
        self.callUsageAmountSign,
        self.reservedForFutureUse,
        self.extensionRecordIndicator = (None)*17
        self.data = f.read(TelephonyBillingDetail.LENGTH)
        super(TelephonyBillingDetail, self).__init__()
        
class MasterCardTemporaryHelpServicesExtensionRecordFormat1(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nEach record must contain a sequence \r\nnumber to identify its position within the \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nThe transaction code identifies the type of \r\nrecord being transmitted.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator indicates that this \r\nrecord is a Temporary Help Services Format \r\n1 Extension Record.\r\nRequired value  TEMP1'),
             ('4', '17-41', '25', 'AN', 'M', 'Employee/Temp Name'),
             ('5', '42-50', '9', 'N', 'M', 'Social Security Number'),
             ('6', '51-60', '10', 'AN', 'M', 'Job Code'),
             ('7', '61-66', '6', 'N', 'M', 'Temp Start Date\r\nMasterCard required date format \r\nYYMMDD, left-ustified and space filled.'),
             ('8', '67-72', '6', 'N', 'M', 'Week Ending Date (Sunday)\r\nMasterCard required date format \r\nYYMMDD, left-ustified and space filled.'),
             ('9', '73-77', '5', 'N', 'M', 'Regular Hours Worked'),
             ('10', '78-84', '7', 'N', 'M', 'Regular Hours Rate'),
             ('11', '85-89', '5', 'N', 'M', 'Overtime Hours Worked'),
             ('12', '90-96', '7', 'N', 'M', 'Overtime Hours Rate'),
             ('13', '97', '1', 'N', 'M', 'Flat Rate Indicator'),
             ('14', '98-100', '3', 'AN', 'M', 'Miscellaneous Expense Indicator'),
             ('15', '101-107', '7', 'N', 'M', 'Miscellaneous Expense Amount'),
             ('16', '108-132', '25', 'AN', 'M', 'Requestor Name or ID'),
             ('17', '133-157', '25', 'AN', 'M', 'Supervisor Name or ID'),
             ('18', '158-197', '40', 'AN', 'M', 'Job Description'),
             ('19', '198-209', '12', 'N', 'M', 'Discount Amount'),
             ('20', '210-221', '12', 'N', 'M', 'Subtotal Amount'),
             ('21', '222-251', '30', 'B', 'TSYS Acquiring Solutions', 'Reserved for future use.'),
             ('22', '252-256', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nRequired value  TEMP2\r\nA TEMP2 extension record must follow the \r\nTEMP1 record.'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "employeeTempName": None,
        "socialSecurityNumber": None,
        "jobCode": None,
        "tempStartDate": None,
        "weekEndingDateSunday": None,
        "regularHoursWorked": None,
        "regularHoursRate": None,
        "overtimeHoursWorked": None,
        "overtimeHoursRate": None,
        "flatRateIndicator": None,
        "miscellaneousExpenseIndicator": None,
        "miscellaneousExpenseAmount": None,
        "requestorNameOrId": None,
        "supervisorNameOrId": None,
        "jobDescription": None,
        "discountAmount": None,
        "subtotalAmount": None,
        "reservedForFutureUse": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.employeeTempName,
        self.socialSecurityNumber,
        self.jobCode,
        self.tempStartDate,
        self.weekEndingDateSunday,
        self.regularHoursWorked,
        self.regularHoursRate,
        self.overtimeHoursWorked,
        self.overtimeHoursRate,
        self.flatRateIndicator,
        self.miscellaneousExpenseIndicator,
        self.miscellaneousExpenseAmount,
        self.requestorNameOrId,
        self.supervisorNameOrId,
        self.jobDescription,
        self.discountAmount,
        self.subtotalAmount,
        self.reservedForFutureUse,
        self.extensionRecordIndicator = (None)*22
        self.data = f.read(MasterCardTemporaryHelpServicesExtensionRecordFormat1.LENGTH)
        super(MasterCardTemporaryHelpServicesExtensionRecordFormat1, self).__init__()
        
class MasterCardTemporaryHelpServicesExtensionRecordFormat2(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nEach record must contain a sequence \r\nnumber to identify its position within the \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nThe transaction code identifies the type of \r\nrecord being transmitted.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator indicates that this is a \r\nTemporary Help Services Extension \r\nRecord.\r\nRequired value  TEMP2'),
             ('4', '17-66', '50', 'AN', 'M', 'Miscellaneous Expense Description 1'),
             ('5', '67-78', '12', 'N', 'M', 'Miscellaneous Expense Amount 1'),
             ('6', '79-128', '50', 'AN', 'M', 'Miscellaneous Expense Description 2'),
             ('7', '129-140', '12', 'N', 'M', 'Miscellaneous Expense Amount 2'),
             ('8', '141-251', '111', 'B', 'TSYS Acquiring Solutions', 'Reserved for future use.'),
             ('9', '252-256', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nPossible values  \r\nBlank - \r\nno extension record follows\r\nGENER - a Generic Extension Record \r\nfollows'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "miscellaneousExpenseDescription1": None,
        "miscellaneousExpenseAmount1": None,
        "miscellaneousExpenseDescription2": None,
        "miscellaneousExpenseAmount2": None,
        "reservedForFutureUse": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.miscellaneousExpenseDescription1,
        self.miscellaneousExpenseAmount1,
        self.miscellaneousExpenseDescription2,
        self.miscellaneousExpenseAmount2,
        self.reservedForFutureUse,
        self.extensionRecordIndicator = (None)*9
        self.data = f.read(MasterCardTemporaryHelpServicesExtensionRecordFormat2.LENGTH)
        super(MasterCardTemporaryHelpServicesExtensionRecordFormat2, self).__init__()
        
class ChipDetailExtensionRecord1(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nNumber that identifies the position of the \r\nrecord within the file.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nThe transaction code from the Financial \r\nrecord, field 2.'),
             ('3', '12-16', '5', 'N', 'TSYS Acquiring Solutions', 'Format Indicator\r\nCode that identifies this record. Must be \r\nEMVC1.'),
             ('4', '17-32', '16', 'AN', 'VMCAPNS', 'Application Cryptogram\r\nValue sent by the chip card in response to a \r\nGenerate Application Cryptogram \r\ncommand. The value is either the \r\nAuthoriation Request Crypto-gram \r\n(ARQC) or the Transaction Certificate \r\n(TC).\r\nThe value must be sent in display \r\nhexadecimal format. (0-9, A-F)'),
             ('5', '33-96', '64', 'AN', 'VMCAPNS', 'Issuer Application Information\r\nProprietary application information for \r\ntransmission to the issuer in an online \r\ntransaction.\r\nThe value must be sent in display \r\nhexadecimal format. (0-9, A-F)'),
             ('6', '97-104', '8', 'AN', 'VMCAPNS', 'Unpredictable Number\r\nVariable number that makes the Application \r\nCryptogram field unique.\r\nThe value must be sent in display \r\nhexadecimal format. (0-9, A-F)'),
             ('7', '105-108', '4', 'AN', 'VMCAPNS', 'Application Transaction Counter\r\nNumber of times the card has been used \r\nwith a specific application. This count \r\nincludes failed transactions.\r\nThe value must be sent in display \r\nhexadecimal format. (0-9, A-F)'),
             ('8', '109-118', '10', 'AN', 'VMCAPNS', 'Terminal Verification Results\r\nCode that indicates the status of various \r\nfunctions of the terminal, as indicated by the \r\nterminal.\r\nThe value must be sent in display \r\nhexadecimal format. (0-9, A-F)'),
             ('9', '119-124', '6', 'N', 'VMCAPNS', 'Transaction Date\r\nDate of the transaction as determined by the \r\nterminal. Format is YYMMDD.'),
             ('10', '125-126', '2', 'N', 'VMCAPNS', 'Transaction Type Code\r\nA code identifying the type of transaction. \r\nPossible values  \r\n00 - \r\nDebit\r\n01 - \r\nCash\r\n02 - \r\nCredit'),
             ('11', '127-138', '12', 'N', 'VMCAPNS', 'Amount Authoried\r\nTransaction amount authoried. This \r\namount is sent to the chip to generate the \r\napplication cryptogram.'),
             ('12', '139-142', '4', 'N', 'VMCAPNS', 'Terminal Transaction Currency Code\r\nNumeric code identifying the currency used \r\nin the transaction. This is a three digit \r\ncurrency code preceded by a ero (0).\r\nFor example, U.S. dollars is expressed as \r\n0840.\r\nNOTEBefore using currency codes not \r\npreviously utilied, please contact your TSYS \r\nAcquiring Solutions Relationship Managers about \r\ntesting the new currency.'),
             ('13', '143-146', '4', 'N', 'VMCAPNS', 'Terminal Country Code\r\nNumeric code identifying the country where \r\nthe terminal is located. This is a three digit \r\ncountry codes preceded by a ero (0).\r\nFor example, a terminal located in Canada \r\nwould be expressed as 0124.'),
             ('14', '147-150', '4', 'AN', 'VMCAPNS', 'Application Interchange Profile\r\nA code that identifies which interchange \r\nfunctions are supported by the chip.\r\nThe value must be sent in display \r\nhexadecimal format. (0-9, A-F)'),
             ('15', '151-162', '12', 'N', 'VMCAPNS', 'Amount, Other\r\nThe cash back amount given to the \r\ncardholder as part of the transaction.\r\nIf the transaction does not include cash \r\nback, this field is ero filled.'),
             ('16', '163-166', '4', 'N', 'VMCAPNS', 'PAN (Primary Account Number) Sequence \r\nNumber\r\nA number identifying separate cards using \r\nthe same PAN. ero (0) is used to left fill the \r\nfield.\r\nFor example, a card with sequence number \r\n8 is expressed as 0008.'),
             ('17', '167-168', '2', 'AN', 'VMCAPNS', 'Cryptogram Information Code\r\nIndicates the type of cryptogram returned \r\nby the card and the actions taken by the \r\nterminal.\r\nThe value must be sent in display \r\nhexadecimal format. (0-9, A-F)'),
             ('18', '169-251', '83', 'AN', 'TSYS Acquiring Solutions', 'Reserved for Future Use\r\nThis field is space filled.'),
             ('19', '252-256', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nIndicates the extension record that follows \r\nthis record.\r\nIf Chip Extension Record 2 follows, this \r\nvalue must be EMVC2.'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "applicationCryptogram": None,
        "issuerApplicationInformation": None,
        "unpredictableNumber": None,
        "applicationTransactionCounter": None,
        "terminalVerificationResults": None,
        "transactionDate": None,
        "transactionTypeCode": None,
        "amountAuthoried": None,
        "terminalTransactionCurrencyCode": None,
        "terminalCountryCode": None,
        "applicationInterchangeProfile": None,
        "amountOther": None,
        "panPrimaryAccountNumberSequence": None,
        "cryptogramInformationCode": None,
        "reservedForFutureUse": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.applicationCryptogram,
        self.issuerApplicationInformation,
        self.unpredictableNumber,
        self.applicationTransactionCounter,
        self.terminalVerificationResults,
        self.transactionDate,
        self.transactionTypeCode,
        self.amountAuthoried,
        self.terminalTransactionCurrencyCode,
        self.terminalCountryCode,
        self.applicationInterchangeProfile,
        self.amountOther,
        self.panPrimaryAccountNumberSequence,
        self.cryptogramInformationCode,
        self.reservedForFutureUse,
        self.extensionRecordIndicator = (None)*19
        self.data = f.read(ChipDetailExtensionRecord1.LENGTH)
        super(ChipDetailExtensionRecord1, self).__init__()
        
class TransactionExtensionRecord(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nThe Transaction code identifies the type of \r\nrecord being transmitted.'),
             ('3', '12-16', '5', 'AN', 'TSYS Acquiring Solutions', 'Format Indicator\r\nThe Format Indicator identifies this record \r\nas a Transaction Extension Record.\r\nRequired value  TADD'),
             ('4', '17-37', '21', 'AN', 'TSYS Acquiring Solutions', 'Detail Merchant Name\r\nSpace Filled'),
             ('5', '38-62', '25', 'AN', 'TSYS Acquiring Solutions', 'Merchant Soft Descriptor'),
             ('6', '63-251', '189', 'AN', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('7', '252-256', '5', 'AN', 'TSYS Acquiring Solutions', 'Extension Record Indicator\r\nIndicates if another extension record \r\nfollows this record.\r\nPossible values  \r\nSpace - \r\nNo extension record follows.\r\nxxxxx - \r\nAny allowed extension record.'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "formatIndicator": None,
        "detailMerchantName": None,
        "merchantSoftDescriptor": None,
        "reservedForFutureUse": None,
        "extensionRecordIndicator": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.formatIndicator,
        self.detailMerchantName,
        self.merchantSoftDescriptor,
        self.reservedForFutureUse,
        self.extensionRecordIndicator = (None)*7
        self.data = f.read(TransactionExtensionRecord.LENGTH)
        super(TransactionExtensionRecord, self).__init__()
        
class BatchTrailer(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nRequired value  9013'),
             ('3', '12-15', '4', 'AN', 'TSYS Acquiring Solutions', 'Transmit Bank Number\r\nThe transmit bank number is assigned by \r\nTSYS Acquiring Solutions.'),
             ('4', '16-20', '5', 'AN', 'TSYS Acquiring Solutions', 'Batch Format Indicator\r\nThe value in this field indicates the type of \r\ntransaction records included in this batch. \r\nFor a batch of Draft 256 records, use DF256 \r\nin this field.\r\nNote\r\nAll records in a batch must be the same format \r\ntype (for example, Draft 256).'),
             ('5', '21-23', '3', 'N', 'TSYS Acquiring Solutions', 'Julian Day of the Year\r\nFormat  DDD\r\nFor an explanation of the format, see Julian \r\nday of the year on page 8.'),
             ('6', '24-27', '4', 'N', 'TSYS Acquiring Solutions', 'Batch Number\r\nThis field must contain the batch number \r\nassigned by the client or the clients data \r\ncapture vendor.'),
             ('7', '28-30', '3', 'AN', 'TSYS Acquiring Solutions', 'Batch Operator Initials\r\nThis field must contain the initials of the \r\noperator who generated the batch or \r\nanother unique batch ID.'),
             ('8', '31-42', '12', 'N', 'TSYS Acquiring Solutions', 'Net Amount of Batch\r\nIf you are using the expanded amount fields \r\n(fields 17-20), use all spaces in this field and \r\nuse a Y in the Expanded Trailer Amounts \r\nIndicator field (batch header position 51).'),
             ('9', '43-48', '6', 'N', 'TSYS Acquiring Solutions', 'Number of Debits'),
             ('10', '49-58', '10', 'N', 'TSYS Acquiring Solutions', 'Amount of Debits\r\nIf you are using the expanded amount fields \r\n(fields 17-20), use all spaces in this field and \r\nuse a Y in the Expanded Trailer Amounts \r\nIndicator field (batch header position 51).'),
             ('11', '59-64', '6', 'N', 'TSYS Acquiring Solutions', 'Number of Credits'),
             ('12', '65-74', '10', 'N', 'TSYS Acquiring Solutions', 'Amount of Credits\r\nIf you are using the expanded amount fields \r\n(fields 17-20), use all spaces in this field and \r\nuse a Y in the Expanded Trailer Amounts \r\nIndicator field (batch header position 51).'),
             ('13', '75-80', '6', 'N', 'TSYS Acquiring Solutions', 'Number of Payments'),
             ('14', '81-90', '10', 'N', 'TSYS Acquiring Solutions', 'Amount of Payments\r\nIf you are using the expanded amount fields \r\n(fields 17-20), use all spaces in this field and \r\nuse a Y in the batch header Expanded \r\nTrailer Amounts Indicator field (batch \r\nheader field 11).'),
             ('15', '91-126', '36', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('16', '127-128', '2', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('17', '129-143', '15', 'N', 'TSYS Acquiring Solutions', 'Expanded Net Amount of Batch'),
             ('18', '144-158', '15', 'N', 'TSYS Acquiring Solutions', 'Expanded Amount of Debits'),
             ('19', '159-173', '15', 'N', 'TSYS Acquiring Solutions', 'Expanded Amount of Credits'),
             ('20', '174-188', '15', 'N', 'TSYS Acquiring Solutions', 'Expanded Amount of Payments'),
             ('21', '189-256', '68', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "transmitBankNumber": None,
        "batchFormatIndicator": None,
        "julianDayOfTheYear": None,
        "batchNumber": None,
        "batchOperatorInitials": None,
        "netAmountOfBatch": None,
        "numberOfDebits": None,
        "amountOfDebits": None,
        "numberOfCredits": None,
        "amountOfCredits": None,
        "numberOfPayments": None,
        "amountOfPayments": None,
        "reservedForFutureUse15": None,
        "reservedForFutureUse16": None,
        "expandedNetAmountOfBatch": None,
        "expandedAmountOfDebits": None,
        "expandedAmountOfCredits": None,
        "expandedAmountOfPayments": None,
        "reservedForFutureUse21": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.transmitBankNumber,
        self.batchFormatIndicator,
        self.julianDayOfTheYear,
        self.batchNumber,
        self.batchOperatorInitials,
        self.netAmountOfBatch,
        self.numberOfDebits,
        self.amountOfDebits,
        self.numberOfCredits,
        self.amountOfCredits,
        self.numberOfPayments,
        self.amountOfPayments,
        self.reservedForFutureUse15,
        self.reservedForFutureUse16,
        self.expandedNetAmountOfBatch,
        self.expandedAmountOfDebits,
        self.expandedAmountOfCredits,
        self.expandedAmountOfPayments,
        self.reservedForFutureUse21 = (None)*21
        self.data = f.read(BatchTrailer.LENGTH)
        super(BatchTrailer, self).__init__()
        
class TransmissionTrailer(Record):
    RECORD = (('1', '1-7', '7', 'N', 'TSYS Acquiring Solutions', 'Sequence Number\r\nThe Sequence Number identifies the \r\nrecords position within the transmission \r\nfile.'),
             ('2', '8-11', '4', 'N', 'TSYS Acquiring Solutions', 'Transaction Code\r\nRequired value  9011'),
             ('3', '12-15', '4', 'AN', 'TSYS Acquiring Solutions', 'Transmit Bank Number\r\nThe transmit bank number is assigned by \r\nTSYS Acquiring Solutions.'),
             ('4', '16-19', '4', 'N', 'TSYS Acquiring Solutions', 'User-Assigned Transmission Number\r\nThis number is assigned by the client. It \r\nmust match the value in field 4 of the \r\ntransmission header.'),
             ('5', '20-31', '12', 'N', 'TSYS Acquiring Solutions', 'Amount of Debits'),
             ('6', '32-43', '12', 'N', 'TSYS Acquiring Solutions', 'Amount of Credits'),
             ('7', '44-55', '12', 'N', 'TSYS Acquiring Solutions', 'Amount of Payments'),
             ('8', '56-95', '40', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('9', '96-110', '15', 'N', 'TSYS Acquiring Solutions', 'Expanded Amount of Debits'),
             ('10', '111-125', '15', 'N', 'TSYS Acquiring Solutions', 'Expanded Amount of Credits'),
             ('11', '126-128', '3', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'),
             ('12', '129-143', '15', 'N', 'TSYS Acquiring Solutions', 'Expanded Amount of Payments'),
             ('13', '144-256', '113', 'S', 'TSYS Acquiring Solutions', 'Reserved for future use'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
        "sequenceNumber": None,
        "transactionCode": None,
        "transmitBankNumber": None,
        "userAssignedTransmissionNumber": None,
        "amountOfDebits": None,
        "amountOfCredits": None,
        "amountOfPayments": None,
        "reservedForFutureUse8": None,
        "expandedAmountOfDebits": None,
        "expandedAmountOfCredits": None,
        "reservedForFutureUse11": None,
        "expandedAmountOfPayments": None,
        "reservedForFutureUse13": None
                }

    LENGTH = 256

    def __init__(self,f):
        self.sequenceNumber,
        self.transactionCode,
        self.transmitBankNumber,
        self.userAssignedTransmissionNumber,
        self.amountOfDebits,
        self.amountOfCredits,
        self.amountOfPayments,
        self.reservedForFutureUse8,
        self.expandedAmountOfDebits,
        self.expandedAmountOfCredits,
        self.reservedForFutureUse11,
        self.expandedAmountOfPayments,
        self.reservedForFutureUse13 = (None)*13
        self.data = f.read(TransmissionTrailer.LENGTH)
        super(TransmissionTrailer, self).__init__()
        