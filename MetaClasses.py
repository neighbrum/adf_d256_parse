
class AccessMethods (metaclass=ADFMeta):
    DATA = (('ASYNC', 'AL', 'A'), ('Dial-Toll-Free Async', 'DW', 'B'), ('Reserved', 'DL', 'C'), ('Direct Connect', 'DF', 'D'), ('Reserved', 'DI', 'E'), ('SARATOGA', 'RM', 'F'), ('Dial - Europe', 'EP', 'G'), ('VirtualNet IP', 'PG', 'H'), ('Reserved', 'LC', 'I'), ('Dial - Toll - Free Caribbean', 'JD', 'J'), ('Internet - VirtualNet SSL', 'MX', 'L'), ('Reserved', 'MD', 'M'), ('Dial - 950 (Feature Group B) Sync', 'FS', 'N'), ('Dial - Toll Free Sync', '8S', 'O'), ('Dial - Toll Free Canada', 'DV', 'P'), ('Wireless', 'MW', 'Q'), ('BAS Re-authorization (TSYS Internal\nUse Only)', 'CW', 'R'), ('Petro Gateway', 'DC', 'S'), ('Reserved', 'EC', 'T'), ('Batch - CNP Authorization', 'DG', 'U'), ('Direct Connect (IP Gateway PPM\nBilling)', 'XL', 'V'), ('Reserved', 'TN', 'W'), ('Reserved', 'n_a', 'X'), ('Dynamic Currency Conversion (DCC)', 'FT', 'Y'), ('Dialpay Transaction', '__', '_'), ('Reserved', 'SC', 'N_A'), ('Reserved', 'n_a', 'Z'))
    LUT = {'A': DATA[0], 'B': DATA[1], 'C': DATA[2], 'D': DATA[3], 'E': DATA[4], 'F': DATA[5], 'G': DATA[6], 'H': DATA[7], 'I': DATA[8], 'J': DATA[9], 'L': DATA[10], 'M': DATA[11], 'N': DATA[12], 'O': DATA[13], 'P': DATA[14], 'Q': DATA[15], 'R': DATA[16], 'S': DATA[17], 'T': DATA[18], 'U': DATA[19], 'V': DATA[20], 'W': DATA[21], 'X': DATA[22], 'Y': DATA[23], '_': DATA[24], 'N_A': DATA[25], 'Z': DATA[26]}

    ROW = lambda row, DATA=DATA: DATA[row]
    COLUMN = lambda column, DATA=DATA: [data[column] for data in DATA]
    AT = lambda row,column, DATA=DATA: DATA[row][column]

    def __init__(self,paramTuple):
        self.description, self.accessMethod, self.aSCIIBillCode = paramTuple

class AMEXCardholderVerificationResults (metaclass=ADFMeta):
    DATA = (('Byte 1', 'Billing ZIP Code', 'Y=Data Matches \nU=Data Unchecked\nN=No Match\nS=Service not Allowed\nR=Retry\nSpace=Data not sent'), ('Byte 2', 'Billing Street Match Code', ''), ('Byte 3', 'Billing Name Match Code', ''), ('Byte 4', 'Telephone Number Match Code', ''), ('Byte 5', 'E-mail Address Match Code', ''), ('Byte 6-9', 'Reserved', ''))
    LUT = {'Byte 1': DATA[0], 'Byte 2': DATA[1], 'Byte 3': DATA[2], 'Byte 4': DATA[3], 'Byte 5': DATA[4], 'Byte 6-9': DATA[5]}

    ROW = lambda row, DATA=DATA: DATA[row]
    COLUMN = lambda column, DATA=DATA: [data[column] for data in DATA]
    AT = lambda row,column, DATA=DATA: DATA[row][column]

    def __init__(self,paramTuple):
        self.byte, self.description, self.possibleValuesForEachByte = paramTuple

class AuthorizationCharacteristicsIndicators (metaclass=ADFMeta):
    DATA = (('Y (Transaction\nrequests\nparticipation)', 'A', 'N', 'T', 'Card present; magnetic stripe read and\nsent; for Retail 2 (key entered) or\nCommercial Card submissions, the\nmagnetic stripe is not included, but other\nsubmission requirements are met;\nsignature obtained; CVV requested if\nmagnetic stripe is present: All CPS market\nsegments'), ('Y (Transaction\nrequests\nparticipation)', 'B', 'N', 'T', 'Tokenized e-commerce with mobile device'), ('Y (Transaction\nrequests\nparticipation)', 'E', 'N', 'T', 'Meets requirements for A, plus merchant\nname and location (enriched name and\nlocation data) present; also valid for Retail\n2 (key-entered), Commercial Card and\nVisa Cashback submissions'), ('Y (Transaction\nrequests\nparticipation)', 'V', 'N', 'T', 'Meets address verification requirements;\nverification requested for card not present\ntransactions (Direct Marketing, Transport\nmarket segments)'), ('Y (Transaction\nrequests\nparticipation)', 'C', 'N', 'T', 'Meets requirements for A, plus merchant\nname, location present, and cardholder-\nactivated terminal indicator (AFD); but no\nsignature required'), ('Y (Transaction\nrequests\nparticipation)', 'M', 'N', 'T', 'Meets national payment service\nrequirements with no address verification:\nDirect Marketing'), ('Y (Transaction\nrequests\nparticipation)', 'F', 'N', 'T', 'Meets qualifications for Visa Account\nFunding Transactions'), ('Y (Transaction\nrequests\nparticipation)', 'J', 'N', 'T', 'Card not present, recurring bill payment'), ('Y (Transaction\nrequests\nparticipation)', 'K', 'N', 'T', 'Card present, unable to read Magnetic\nStripe and included an address verification\nrequest in the authorization request'), ('Y (Transaction\nrequests\nparticipation)', 'U', 'N', 'T', 'Meets basic CPS/E-Commerce\nrequirements and VSEC 3-D Secure data\nis present'), ('Y (Transaction\nrequests\nparticipation)', 'W', 'N', 'T', 'Meets basic CPS/E-Commerce\nrequirements but transmission was not a\nverified VSEC 3-D Secure transmission'), ('R (Recurring\npayment)', 'R', 'N', 'T', 'Meets Direct Marketing recurring payment\nqualification without address verification\nrequest'), ('I (Increment to\npreviously approved\ntransaction)', 'I', 'N', 'T', 'Incremental authorization qualified for\nCPS, card may or may not be present:\nHotel/Auto Rental'), ('P (Preferred\nCustomer)', 'P', 'N', 'T', 'Meets requirements for Preferred\nCustomer, card not present: Hotel/Auto\nRental and Transport'))
    LUT = {'A': DATA[0], 'B': DATA[1], 'E': DATA[2], 'V': DATA[3], 'C': DATA[4], 'M': DATA[5], 'F': DATA[6], 'J': DATA[7], 'K': DATA[8], 'U': DATA[9], 'W': DATA[10], 'R': DATA[11], 'I': DATA[12], 'P': DATA[13]}

    ROW = lambda row, DATA=DATA: DATA[row]
    COLUMN = lambda column, DATA=DATA: [data[column] for data in DATA]
    AT = lambda row,column, DATA=DATA: DATA[row][column]

    def __init__(self,paramTuple):
        self.endpointSendsACI, self.qualified, self.notQualified, self.approvedandMCCnoteligible, self.because = paramTuple

class CardProducts (metaclass=ADFMeta):
    DATA = (('A^', 'Visa Traditional'), ('AX', 'American Express Card'), ('B^', 'Visa Traditional Rewards'), ('C^', 'Visa Signature'), ('D^', 'Visa Signature Preferred'), ('DI', 'Discover Card'), ('DN', 'Diners Card'), ('E^', 'Proprietary ATM'), ('F^', 'Visa Classic'), ('G^', 'Visa Business'), ('G1', 'Visa Signature Business'), ('G2', 'Reserved'), ('G3', 'Visa Business Enhanced\nVisa Platinum Business'), ('G4', 'Visa Infinite Business\nVisa Infinite Privilege Business (Canada)'), ('H^', 'Reserved'), ('I^', 'Visa Infinite\n[New Consumer Credit Product]'), ('I1', 'Visa Infinite Privilege'), ('I2', '[Ultra High Net Worth]'), ('J^', 'Reserved'), ('J1', 'Reserved'), ('J2', 'Reserved'), ('J3', 'Visa Healthcare'), ('J4', 'Reserved'), ('JC', 'JCB Card'), ('K^', 'Visa Corporate T & E'), ('K1', 'Visa GSC Corporate T & E'), ('L^', 'Electron'), ('M^', 'Mastercard'), ('N^', 'Visa Platinum'), ('N1', 'Visa Rewards'), ('N2', 'Visa Select'), ('P^', 'Visa Gold'), ('Q^', 'Private Label'), ('Q1', 'Reserved'), ('Q2', 'Private Label Basic'), ('Q3', 'Private Label Standard'), ('Q4', 'Private Label Enhanced'), ('Q5', 'Private Label Specialized'), ('Q6', 'Private Label Premium'), ('R^', 'Proprietary'), ('S^', 'Visa Purchasing'), ('S1', 'Visa Purchasing with Fleet (outside of Canada)\nVisa Fleet (cards issued in Canada)'), ('S2', 'Visa GSA Purchasing'), ('S3', 'Visa GSA Purchasing with Fleet'), ('S4', 'Commercial Loan'), ('S5', 'Commercial Transport EBT'), ('S6', 'Business Loan'), ('S7', 'Reserved'), ('T^', 'Reserved'), ('U^', 'Visa Travel Money'), ('V^', 'V Pay'), ('V1', 'Reserved'), ('W^', 'Reserved'), ('X^', 'Visa B2B Virtual Payments'), ('Y^', 'Reserved'), ('Z^', 'Reserved'))
    LUT = {'A^': DATA[0], 'AX': DATA[1], 'B^': DATA[2], 'C^': DATA[3], 'D^': DATA[4], 'DI': DATA[5], 'DN': DATA[6], 'E^': DATA[7], 'F^': DATA[8], 'G^': DATA[9], 'G1': DATA[10], 'G2': DATA[11], 'G3': DATA[12], 'G4': DATA[13], 'H^': DATA[14], 'I^': DATA[15], 'I1': DATA[16], 'I2': DATA[17], 'J^': DATA[18], 'J1': DATA[19], 'J2': DATA[20], 'J3': DATA[21], 'J4': DATA[22], 'JC': DATA[23], 'K^': DATA[24], 'K1': DATA[25], 'L^': DATA[26], 'M^': DATA[27], 'N^': DATA[28], 'N1': DATA[29], 'N2': DATA[30], 'P^': DATA[31], 'Q^': DATA[32], 'Q1': DATA[33], 'Q2': DATA[34], 'Q3': DATA[35], 'Q4': DATA[36], 'Q5': DATA[37], 'Q6': DATA[38], 'R^': DATA[39], 'S^': DATA[40], 'S1': DATA[41], 'S2': DATA[42], 'S3': DATA[43], 'S4': DATA[44], 'S5': DATA[45], 'S6': DATA[46], 'S7': DATA[47], 'T^': DATA[48], 'U^': DATA[49], 'V^': DATA[50], 'V1': DATA[51], 'W^': DATA[52], 'X^': DATA[53], 'Y^': DATA[54], 'Z^': DATA[55]}

    ROW = lambda row, DATA=DATA: DATA[row]
    COLUMN = lambda column, DATA=DATA: [data[column] for data in DATA]
    AT = lambda row,column, DATA=DATA: DATA[row][column]

    def __init__(self,paramTuple):
        self.value, self.productDescription = paramTuple

class Currencies (metaclass=ADFMeta):
    DATA = (('004', 'Afghanistan'), ('008', 'Albania'), ('010', 'Antarctica'), ('012', 'Algeria'), ('031', 'Azerbaijin'), ('032', 'Argentina'), ('036', 'Australia'), ('036', 'Christmas Is.'), ('036', 'Cocos (Keeling) Is.'), ('036', 'Heard and McDonald Is.'), ('036', 'Kiribati'), ('036', 'Nauru'), ('036', 'Norfolk Is.'), ('036', 'Tuvalu'), ('040', 'Austria'), ('044', 'Bahamas'), ('048', 'Bahrain'), ('050', 'Bangladesh'), ('051', 'Armenia'), ('052', 'Barbados'), ('064', 'Bhutan'), ('068', 'Bolivia'), ('072', 'Botswana'), ('084', 'Belize'), ('090', 'Solomon Is.'), ('096', 'Brunei Darussalam'), ('100', 'Bulgaria'), ('104', 'Myanmar'), ('108', 'Burundi'), ('116', 'Cambodia'), ('124', 'Canada'), ('132', 'Cape Verde Is.'), ('136', 'Cayman Is.'), ('144', 'Sri Lanka'), ('152', 'Chile'), ('156', 'China'), ('170', 'Columbia'), ('174', 'Comoros'), ('188', 'Costa Rica'), ('191', 'Croatia'), ('192', 'Cuba'), ('196', 'Cyprus'), ('203', 'Czech Republic'), ('208', 'Denmark'), ('208', 'Faeroe Is.'), ('208', 'Greenland'), ('214', 'Dominican Rep.'), ('218', 'Ecuador'), ('222', 'El Salvador'), ('230', 'Ethiopia'), ('232', 'Eritrea'), ('233', 'Estonia'), ('238', 'Falkland Is. (Malvinas)'), ('242', 'Fiji'), ('262', 'Dijibouto'), ('270', 'Gambia'), ('288', 'Ghana'), ('292', 'Gibraltar'), ('320', 'Guatemala'), ('324', 'Guinea'), ('328', 'Guyana'), ('332', 'Haiti'), ('340', 'Honduras'), ('344', 'Hong Kong, China'), ('348', 'Hungary'), ('352', 'Iceland'), ('356', 'India'), ('360', 'East Timor'), ('360', 'Indonesia'), ('364', 'Iran, Islamic Republic of'), ('365', 'Iran Airlines'), ('368', 'Iraq'), ('376', 'Israel'), ('380', 'Italy'), ('388', 'Jamaica'), ('392', 'Japan'), ('398', 'Kazakhstan'), ('400', 'Jordan'), ('404', 'Kenya'), ('408', "Korea, Democratic People's Republic of (North Korea)"), ('410', 'Korea, Republic of'), ('414', 'Kuwait'), ('417', 'Kyrgyzstan'), ('418', "Lao People's Democratic Republic"), ('422', 'Lebanon'), ('428', 'Latvia'), ('430', 'Liberia'), ('434', 'Libyan Arab Jamahiriya'), ('440', 'Lithuania'), ('446', 'Macau, China'), ('450', 'Madagascar'), ('454', 'Malawi'), ('458', 'Malaysia'), ('462', 'Maldives'), ('470', 'Malta'), ('478', 'Mauritania'), ('480', 'Mauritius'), ('484', 'Mexico'), ('496', 'Mongolia'), ('498', 'Moldova, Republic of'), ('504', 'Morocco'), ('504', 'Western Sahara'), ('508', 'Mozambique'), ('512', 'Oman'), ('516', 'Nambia'), ('524', 'Nepal'), ('532', 'Netherlands Antilles'), ('533', 'Aruba'), ('548', 'Vanuatu'), ('554', 'Cook Is.'), ('554', 'New Zealand'), ('554', 'Niue'), ('554', 'Pitcairin'), ('554', 'Tokelau'), ('558', 'Nicaragua'), ('566', 'Nigeria'), ('578', 'Antarctica'), ('578', 'Bouvet Is.'), ('578', 'Norway'), ('578', 'Svalbard and Jan Mayen Is.'), ('586', 'Pakistan'), ('590', 'Panama'), ('598', 'Papua New Guinea'), ('600', 'Paraguay'), ('604', 'Peru'), ('606', 'Bermuda'), ('608', 'Philippines'), ('624', 'Guinea-Bissau'), ('626', 'East Timor'), ('634', 'Qatar'), ('642', 'Romania'), ('643', 'Russian Federation in the Central and Eastern Europe, Middle East and Africa (CEMEA)'), ('646', 'Rwanda'), ('654', 'St. Helena'), ('678', 'Sao Tome and Principe'), ('682', 'Saudi Arabia'), ('690', 'Seychelles'), ('694', 'Sierra Leone'), ('702', 'Singapore'), ('703', 'Slovakia'), ('704', 'Vietnam'), ('705', 'Slovenia'), ('706', 'Somalia'), ('710', 'Lesotho'), ('710', 'South Africa'), ('716', 'Z\nimbabwe'), ('736', 'Sudan'), ('737', 'Sudan Airlines'), ('740', 'Suriname (Guilder)'), ('748', 'Swaziland'), ('752', 'Sweden'), ('756', 'Liechtenstein'), ('756', 'Switzerland'), ('760', 'Syrian Arab Rep.'), ('764', 'Thailand'), ('776', 'Tonga'), ('780', 'Trinidad and Tobago'), ('784', 'United Arab Emirates'), ('788', 'Tunisia'), ('792', 'Turkey'), ('795', 'Turkmenistan'), ('800', 'Uganda'), ('804', 'Ukraine'), ('807', 'Macedonia, The Former Yugoslav Republic of'), ('810', 'Russian Federation'), ('818', 'Egypt'), ('826', 'United Kingdom'), ('826', 'So. Georgia and So. Sandwich Is.'), ('834', 'Tanzania, United Republic of'), ('840', 'American Samoa'), ('840', 'British Indian Ocean Territory'), ('840', 'British Virgin Is.'), ('840', 'Guam'), ('840', 'Marshall Islands'), ('840', 'Micronesia'), ('840', 'Northern Mariana Is.'), ('840', 'Palestinian Territory, Occupied'), ('840', 'Palau'), ('840', 'Panama'), ('840', 'Puerto Rico'), ('840', 'Turks and Caicos Is.'), ('840', 'United States'), ('840', 'U.S. Minor Outlying Islands'), ('840', 'U.S. Virgin Islands'), ('858', 'Uruguay'), ('860', 'Uzbekistan'), ('862', 'Venezuela'), ('876', 'Wallis and Futuna Is.'), ('882', 'Samoa'), ('886', 'Yemen'), ('891', 'Republic of Montenegro'), ('891', 'Yugoslavia'), ('894', 'Zambia'), ('901', 'Taiwan'), ('920', 'St. Pierre and Miquelon'), ('941', 'Republic of Serbia'), ('950', 'Cameroon, United Republic of'), ('950', 'Central African Republic'), ('950', 'Chad'), ('950', 'Congo'), ('950', 'Equatorial Guinea'), ('950', 'Gabon'), ('951', 'Antigua and Barbuda'), ('951', 'Anguilla'), ('951', 'Dominica'), ('951', 'Grenada'), ('951', 'Montserrat'), ('951', 'St. Kitts-Nevis'), ('951', 'St. Lucia'), ('952', 'Benin'), ('952', 'Burkina Faso'), ('952', "Cote D' Ivorie (Ivory Coast)"), ('952', 'Mali'), ('952', 'Niger'), ('952', 'Senegal'), ('953', 'French Polynesia'), ('953', 'New Caledonia'), ('953', 'Wallis and Futuna Is.'), ('968', 'Suriname in the Latin America and Caribbean (LAC)'), ('972', 'Tajikistan'), ('973', 'Angola'), ('974', 'Belarus'), ('976', 'Democratic Republic of the Congo (Zaire)'), ('977', 'Bosnia and Herzegovina'), ('978', 'Andorra'), ('978', 'Belguim'), ('978', 'European Union'), ('978', 'Finland'), ('978', 'France'), ('978', 'France, Metropolitan'), ('978', 'French Guiana'), ('978', 'French Southern Territory'), ('978', 'Germany'), ('978', 'Greece'), ('978', 'Guadeloupe'), ('978', 'Ireland, Republic of'), ('978', 'Kosovo, United Nations Interim Administration Mission'), ('978', 'Luxembourg'), ('978', 'Martinique'), ('978', 'Mayotte'), ('978', 'Monaco'), ('978', 'Netherlands'), ('978', 'Portugal'), ('978', 'San Marino'), ('978', 'Spain'), ('978', 'St. Vincent and the Grenadines'), ('978', 'Vatican City (Holly See)'), ('981', 'Georgia'), ('985', 'Poland'), ('986', 'Brazil'))
    LUT = {'004': DATA[0], '008': DATA[1], '010': DATA[2], '012': DATA[3], '031': DATA[4], '032': DATA[5], '036': DATA[13], '040': DATA[14], '044': DATA[15], '048': DATA[16], '050': DATA[17], '051': DATA[18], '052': DATA[19], '064': DATA[20], '068': DATA[21], '072': DATA[22], '084': DATA[23], '090': DATA[24], '096': DATA[25], '100': DATA[26], '104': DATA[27], '108': DATA[28], '116': DATA[29], '124': DATA[30], '132': DATA[31], '136': DATA[32], '144': DATA[33], '152': DATA[34], '156': DATA[35], '170': DATA[36], '174': DATA[37], '188': DATA[38], '191': DATA[39], '192': DATA[40], '196': DATA[41], '203': DATA[42], '208': DATA[45], '214': DATA[46], '218': DATA[47], '222': DATA[48], '230': DATA[49], '232': DATA[50], '233': DATA[51], '238': DATA[52], '242': DATA[53], '262': DATA[54], '270': DATA[55], '288': DATA[56], '292': DATA[57], '320': DATA[58], '324': DATA[59], '328': DATA[60], '332': DATA[61], '340': DATA[62], '344': DATA[63], '348': DATA[64], '352': DATA[65], '356': DATA[66], '360': DATA[68], '364': DATA[69], '365': DATA[70], '368': DATA[71], '376': DATA[72], '380': DATA[73], '388': DATA[74], '392': DATA[75], '398': DATA[76], '400': DATA[77], '404': DATA[78], '408': DATA[79], '410': DATA[80], '414': DATA[81], '417': DATA[82], '418': DATA[83], '422': DATA[84], '428': DATA[85], '430': DATA[86], '434': DATA[87], '440': DATA[88], '446': DATA[89], '450': DATA[90], '454': DATA[91], '458': DATA[92], '462': DATA[93], '470': DATA[94], '478': DATA[95], '480': DATA[96], '484': DATA[97], '496': DATA[98], '498': DATA[99], '504': DATA[101], '508': DATA[102], '512': DATA[103], '516': DATA[104], '524': DATA[105], '532': DATA[106], '533': DATA[107], '548': DATA[108], '554': DATA[113], '558': DATA[114], '566': DATA[115], '578': DATA[119], '586': DATA[120], '590': DATA[121], '598': DATA[122], '600': DATA[123], '604': DATA[124], '606': DATA[125], '608': DATA[126], '624': DATA[127], '626': DATA[128], '634': DATA[129], '642': DATA[130], '643': DATA[131], '646': DATA[132], '654': DATA[133], '678': DATA[134], '682': DATA[135], '690': DATA[136], '694': DATA[137], '702': DATA[138], '703': DATA[139], '704': DATA[140], '705': DATA[141], '706': DATA[142], '710': DATA[144], '716': DATA[145], '736': DATA[146], '737': DATA[147], '740': DATA[148], '748': DATA[149], '752': DATA[150], '756': DATA[152], '760': DATA[153], '764': DATA[154], '776': DATA[155], '780': DATA[156], '784': DATA[157], '788': DATA[158], '792': DATA[159], '795': DATA[160], '800': DATA[161], '804': DATA[162], '807': DATA[163], '810': DATA[164], '818': DATA[165], '826': DATA[167], '834': DATA[168], '840': DATA[183], '858': DATA[184], '860': DATA[185], '862': DATA[186], '876': DATA[187], '882': DATA[188], '886': DATA[189], '891': DATA[191], '894': DATA[192], '901': DATA[193], '920': DATA[194], '941': DATA[195], '950': DATA[201], '951': DATA[208], '952': DATA[214], '953': DATA[217], '968': DATA[218], '972': DATA[219], '973': DATA[220], '974': DATA[221], '976': DATA[222], '977': DATA[223], '978': DATA[246], '981': DATA[247], '985': DATA[248], '986': DATA[249]}

    ROW = lambda row, DATA=DATA: DATA[row]
    COLUMN = lambda column, DATA=DATA: [data[column] for data in DATA]
    AT = lambda row,column, DATA=DATA: DATA[row][column]

    def __init__(self,paramTuple):
        self.currencyCode, self.countryName = paramTuple

class NetworkIDs (metaclass=ADFMeta):
    DATA = (('0003', 'G', 'Interlink'), ('0004', 'B', 'Plus ATM'), ('0006', 'O', 'Cirrus ATM'), ('0007', 'J', 'Mastercard ATM'), ('0008', 'N', 'STAR'), ('0009', 'S', 'PULSE'), ('0010', 'W', 'STAR Southeast'), ('0011', 'Z', 'STAR Northeast'), ('0012', 'Q', 'STAR West'), ('0013', 'U', 'AFFN�'), ('0015', 'M', 'STAR'), ('0016', '8', 'Maestro�'), ('0017', 'L', 'Pulse�'), ('0018', 'Y', 'NYCE'), ('0019', 'H', 'PULSE'), ('0020', 'E', 'Accel�'), ('0024', 'C', 'CU24'), ('0027', 'F', 'NYCE'), ('0028', '7', 'Shazamsm (ITS)'), ('0029', 'K', 'EBT'), ('0030', 'T', 'EBT ATM'), ('0040', 'A', 'Amex ATM'), ('0041', 'D', 'Discover ATM'), ('0042', '1', 'AFFN ATM'), ('0053', '2', 'Fifth Third (TSYS assigned value)'), ('0777', '5', 'Visa Check Card II (TSYS assigned value)'), ('1001', '!', 'Evertech (TSYS assigned value)'))
    LUT = {'0003': DATA[0], '0004': DATA[1], '0006': DATA[2], '0007': DATA[3], '0008': DATA[4], '0009': DATA[5], '0010': DATA[6], '0011': DATA[7], '0012': DATA[8], '0013': DATA[9], '0015': DATA[10], '0016': DATA[11], '0017': DATA[12], '0018': DATA[13], '0019': DATA[14], '0020': DATA[15], '0024': DATA[16], '0027': DATA[17], '0028': DATA[18], '0029': DATA[19], '0030': DATA[20], '0040': DATA[21], '0041': DATA[22], '0042': DATA[23], '0053': DATA[24], '0777': DATA[25], '1001': DATA[26]}

    ROW = lambda row, DATA=DATA: DATA[row]
    COLUMN = lambda column, DATA=DATA: [data[column] for data in DATA]
    AT = lambda row,column, DATA=DATA: DATA[row][column]

    def __init__(self,paramTuple):
        self.networkID, self.sharedGroupCode, self.network = paramTuple

class Records (metaclass=ADFMeta):
    DATA = (('Transmission Header Record', '900', 'TH01', 'TransmissionHeaderRecord'), ('BIN Header Record', '900', 'BH01', 'BINHeaderRecord'), ('Report Header Record', '900', 'RH01', 'ReportHeaderRecord'), ('Transaction Detail Record', '900', 'TD01', 'TransactionDetailRecord'), ('Transaction Detail Extension Record', '200', 'TD11', 'TransactionDetailExtensionRecord'), ('Discover/ PayPal Extension Record', '160', 'EX01', 'DiscoverPayPalExtensionRecord'), ('Mastercard Extension Record', '160', 'EX02', 'MastercardExtensionRecord'), ('Merchant Data Extension Record', '160', 'EX04', 'MerchantDataExtensionRecord'), ('Additional Detail Data Extension Record', '320', 'EX03', 'AdditionalDetailDataExtensionRecord'), ('Report Header Record', '81', 'RH02', 'ReportHeaderRecord'), ('Host Capture Adjustment Transaction Detail Record', '120', 'TD02', 'HostCaptureAdjustmentTransactionDetailRecord'), ('Host Capture Batch Inquiry Transaction Detail Record', '100', 'TD03', 'HostCaptureBatchInquiryTransactionDetailRecord'), ('Report Trailer Record', '93', 'RT02', 'ReportTrailerRecord'), ('Report Trailer Record', '900', 'RT01', 'ReportTrailerRecord'), ('BIN Trailer Record', '900', 'BT01', 'BINTrailerRecord'), ('Transmission Trailer Record', '900', 'TT01', 'TransmissionTrailerRecord'))
    LUT = {'TH01': DATA[0], 'BH01': DATA[1], 'RH01': DATA[2], 'TD01': DATA[3], 'TD11': DATA[4], 'EX01': DATA[5], 'EX02': DATA[6], 'EX04': DATA[7], 'EX03': DATA[8], 'RH02': DATA[9], 'TD02': DATA[10], 'TD03': DATA[11], 'RT02': DATA[12], 'RT01': DATA[13], 'BT01': DATA[14], 'TT01': DATA[15]}

    ROW = lambda row, DATA=DATA: DATA[row]
    COLUMN = lambda column, DATA=DATA: [data[column] for data in DATA]
    AT = lambda row,column, DATA=DATA: DATA[row][column]

    def __init__(self,paramTuple):
        self.transmissionTrailerRecord, self.totalBytes, self.recordCode, self.className = paramTuple

class Rejects (metaclass=ADFMeta):
    DATA = (('0001', '2', 'Primary Account Number', 'Invalid Length (length subfield)'), ('0002', '2', 'Primary Account Number', 'Invalid Value'), ('0003', 'H5', 'Destination Station ID', 'Invalid Value'), ('0004', 'H6', 'TSYS Acquiring Solutions Endpoint ID', 'Invalid Value'), ('0005', 'MTI', 'Message Type Identifier', 'Invalid Value'), ('0008', '3', 'Processing Code', 'Invalid Value'), ('0009', '4', 'Transaction Amount', 'Invalid Value'), ('0010', '7', 'Transmission Date and Time', 'Invalid Value'), ('0011', '11', 'Systems Trace Audit Number', 'Invalid Value'), ('0012', 'H1', 'Header Length', 'Invalid Value'), ('0013', 'H2', 'Header Flag and Format', 'Invalid Value'), ('0014', '14', 'Expiration Date', 'Invalid Value'), ('0015', 'H3', 'Text Format', 'Invalid Value'), ('0016', 'H4', 'Total Message Length', 'Invalid Value'), ('0017', '18', 'Merchant�s Type', 'Invalid Value'), ('0018', '25', 'POS Condition Code', 'Invalid Value'), ('0019', '22', 'POS Entry Mode Code', 'Invalid Value: First 2 digits\ninvalid (Field 22=90 but acquirer\nnot certified)'), ('0020', '32', 'Acquiring Institution ID Code', 'Invalid Value'), ('0021', '32', 'Acquiring Institution ID Code', 'Invalid Value'), ('', 'H6', 'Source Station ID', 'The message contains a PIN,\nbut the Source Station ID is not\ncertified for PIN processing'), ('0022', 'H7', 'Round-Trip Control Information', 'Invalid Value'), ('0023', 'H8', 'Base I Flags', 'Invalid Value'), ('0024', '35', 'Length subfield of Track 2 Data', 'Invalid Length (track data too\nlong)'), ('0025', 'H9', 'Message Status Flags', 'Invalid Value'), ('0026', '61', 'Length subfield of Other Amounts', 'Invalid Length'), ('0027', '35', 'Track 2 Data', 'Invalid Value (Service Code)'), ('', '40', 'Service Restriction Code', 'Invalid Value'), ('', '45', 'Track 1 Data', 'Invalid Value (Service Code)'), ('028', '59', 'National POS Geographic Data', 'Invalid length (length subfield)'), ('0030', 'H10', 'Batch Number', 'Invalid Value'), ('0033', '19', 'Acquiring Institution Country Code', 'Invalid Value'), ('', '33', 'Forwarding Institution ID Code', 'Field Missing'), ('0034', '38', 'Authorization Identification Response', 'Invalid Value'), ('0035', '20', 'PAN Extended, Country Code', 'Invalid Value'), ('0037', '49', 'Currency Code, Transaction', 'Invalid Value'), ('0042', '70', 'Network Management Information Code', 'Invalid Value'), ('0055', '90', 'Original Data Elements', 'Invalid Value'), ('0056', '33', 'Forwarding Institution Identification Code', 'Invalid Length (length subfield)'), ('0057', '33', 'Forwarding Institution Identification Code', 'Invalid Value'), ('0061', '48', 'Additional Data - Private, position 1', 'Invalid Value'), ('063', '48', 'Additional Data - Private', 'Invalid Length (length subfield)'), ('0070', '26', 'Point-of-Service PIN Capture Code', 'Invalid Value'), ('0071', '44', 'Additional Response Data', 'Invalid Length (length subfield)'), ('0072', '60', 'POS Entry Capability and Merchant Group\nCode', 'Invalid Length (length subfield)'), ('0082', '100', 'Receiving Institution Identification Code', 'Invalid Length (length subfield)'), ('0087', '39', 'Response Code', 'Invalid Value'), ('0088', '53', 'Security Related Control Information', 'Invalid Value'), ('0090', '12', 'Local Transaction Time', 'Invalid Value'), ('0091', '13', 'Local Transaction Date', 'Invalid Value'), ('0094', '37', 'First four digits of Retrieval Reference\nNumber', 'Invalid Value'), ('0095', '37', 'Retrieval Reference Number', 'Invalid Value'), ('0096', '42', 'Card Acceptor Identification Code', 'Invalid Value'), ('0100', '100', 'Receiving Institution Identification Code', 'Invalid Length (length subfield)'), ('0102', '45', 'Track 1 Data', 'Invalid Length'), ('0103', '102', 'Account Identification 1', 'Invalid Value'), ('0104', '102', 'Account Identification 1', 'Invalid Length (length subfield)'), ('0105', '60', 'POS Entry Capability and Merchant Group\nCode', 'Invalid Value'), ('0106', '61', 'Other Amounts', 'Invalid Value'), ('0111', '103', 'Account Identification 2', 'Invalid Length (length subfield)'), ('0112', '103', 'Account Identification 2', 'Invalid Value'), ('0118', '21', 'Forwarding Institution Country Code', 'Invalid Value'), ('0119', '68', 'Receiving Institution Country Code', 'Invalid Value'), ('0127', '44.2', 'Additional Response Data', 'Invalid Value'), ('0129', '121', 'Issuing Institution Identification Code', 'Invalid length (length subfield)'), ('0142', '22', 'POS Entry Mode Code', 'Field value = 90, but track data\nnot present'), ('', '35', 'Track 2 Data', 'Magnetic stripe data missing'), ('', '45', 'Track 1 Data', 'Magnetic stripe data missing'), ('0148', '126.10', 'CVV2 Authorization Request', 'Invalid Value'), ('0152', '62.1', 'Authorization Characteristics Indicator', 'Invalid Value'), ('0180', '126.0', 'Bit Map', 'Invalid bit map'), ('0185', '60', 'Additional POS Information', 'Invalid values in position 9 and\n10 (e- Commerce)'), ('0189', '4', 'Transaction Amount', 'Invalid conversion overflow'), ('0251', '2', 'Primary Account Number', 'Field Missing'), ('0259', 'H8', 'Host Flags', 'Field Missing'), ('0260', 'H9', 'Message Status Flags', 'Field Missing'), ('0270', 'MTI', 'Message Type Identifier', 'Field Missing (located between\nthe header bit map fields and\nthe message data fields)'), ('0274', '3', 'Processing Code', 'Field Missing'), ('0275', '4', 'Transaction Amount', 'Field Missing'), ('0276', '7', 'Transmission date and time', 'Field Missing'), ('0277', '11', 'Systems Trace Audit Number', 'Field Missing'), ('0279', '13', 'Local Transaction Date', 'Field Missing'), ('0280', '14', 'Expiration Date', 'Field Missing'), ('0283', '18', 'Merchant Type', 'Field Missing'), ('0284', '25', 'POS Condition Code', 'Field Missing'), ('0285', '22', 'POS Entry Mode Code', 'Field Missing'), ('0287', '32', 'Acquiring Institution Identification Code', 'Field Missing'), ('0289', '41', 'Card Acceptor Terminal ID', 'Field Missing'), ('0291', '35', 'Track 2 Data', 'Field Missing'), ('0293', '38', 'Authorization Identification Response', 'Field Missing'), ('0294', '39', 'Response Code', 'Field Missing'), ('0295', '52', 'Personal Identification Number (PIN)', 'Field Missing'), ('0306', '19', 'Acquiring Institution Identification Code', 'Field Missing'), ('0310', '37', 'Retrieval Reference Number', 'Field Missing'), ('0311', '42', 'Card Acceptor Identification Number', 'Field Missing'), ('0312', '43', 'Card Acceptor Name/ Location', 'Field Missing'), ('0313', '48', 'Additional Data, Private', 'Field Missing'), ('0315', '49', 'Transaction Currency Code', 'Field Missing'), ('0321', '70', 'Network Management Information Code', 'Field Missing'), ('334', '100', 'Receiving Institution Identification Code', 'Field Missing'), ('336', '90', 'Original Data Elements', 'Field Missing'), ('0359', '126', 'Bit Map', 'Field Missing'), ('0360', '60', 'Additional POS Information', 'Field Missing'), ('0384', '53', 'Security Related Control Information', 'Field Missing'), ('0394', '102', 'Account Identification 1', 'Field Missing'), ('0397', '103', 'Account Identification 2', 'Field Missing, or the message\ncontains no account number.'), ('0401', '121', 'Issuing Institution Identification Code', 'Field Missing'), ('0452', '21', 'Forwarding Institution Identification Code', 'Field Missing'), ('0483', '62.2', 'Authorization Characteristics Indicator', 'Field Missing'), ('0488', '60.8', 'Additional POS Information', 'E-Commerce Indicator\n(positions 9-10) is missing'), ('0518', '54', 'Additional Amounts', 'Incorrect usage of field 54'), ('0519', 'H2', 'Header Format', 'Invalid Value'), ('0592', '52', 'Personal Identification Number (PIN)', 'PIN data present when not\nallowed. Field 22 or field 25\nindicate manual entry or card-\nnot- present transaction.'), ('0643', '59', 'National Point-of Service Geographic Data', 'Invalid national POS geographic\ncode'), ('0644', '59', 'National Point-of-Service Geographic Data', 'Invalid national POS ZIP code'), ('0801', '47', 'AMEX ITD/APD', 'Invalid Length'), ('0802', '81', 'Extended AVS Data', 'Invalid Length'), ('0803', '82', 'POS Data Group', 'Invalid Length'), ('0804', '83', 'AMEX Merchant Name/Location', 'Invalid Length'))
    LUT = {'0001': DATA[0], '0002': DATA[1], '0003': DATA[2], '0004': DATA[3], '0005': DATA[4], '0008': DATA[5], '0009': DATA[6], '0010': DATA[7], '0011': DATA[8], '0012': DATA[9], '0013': DATA[10], '0014': DATA[11], '0015': DATA[12], '0016': DATA[13], '0017': DATA[14], '0018': DATA[15], '0019': DATA[16], '0020': DATA[17], '0021': DATA[18], '': DATA[66], '0022': DATA[20], '0023': DATA[21], '0024': DATA[22], '0025': DATA[23], '0026': DATA[24], '0027': DATA[25], '028': DATA[28], '0030': DATA[29], '0033': DATA[30], '0034': DATA[32], '0035': DATA[33], '0037': DATA[34], '0042': DATA[35], '0055': DATA[36], '0056': DATA[37], '0057': DATA[38], '0061': DATA[39], '063': DATA[40], '0070': DATA[41], '0071': DATA[42], '0072': DATA[43], '0082': DATA[44], '0087': DATA[45], '0088': DATA[46], '0090': DATA[47], '0091': DATA[48], '0094': DATA[49], '0095': DATA[50], '0096': DATA[51], '0100': DATA[52], '0102': DATA[53], '0103': DATA[54], '0104': DATA[55], '0105': DATA[56], '0106': DATA[57], '0111': DATA[58], '0112': DATA[59], '0118': DATA[60], '0119': DATA[61], '0127': DATA[62], '0129': DATA[63], '0142': DATA[64], '0148': DATA[67], '0152': DATA[68], '0180': DATA[69], '0185': DATA[70], '0189': DATA[71], '0251': DATA[72], '0259': DATA[73], '0260': DATA[74], '0270': DATA[75], '0274': DATA[76], '0275': DATA[77], '0276': DATA[78], '0277': DATA[79], '0279': DATA[80], '0280': DATA[81], '0283': DATA[82], '0284': DATA[83], '0285': DATA[84], '0287': DATA[85], '0289': DATA[86], '0291': DATA[87], '0293': DATA[88], '0294': DATA[89], '0295': DATA[90], '0306': DATA[91], '0310': DATA[92], '0311': DATA[93], '0312': DATA[94], '0313': DATA[95], '0315': DATA[96], '0321': DATA[97], '334': DATA[98], '336': DATA[99], '0359': DATA[100], '0360': DATA[101], '0384': DATA[102], '0394': DATA[103], '0397': DATA[104], '0401': DATA[105], '0452': DATA[106], '0483': DATA[107], '0488': DATA[108], '0518': DATA[109], '0519': DATA[110], '0592': DATA[111], '0643': DATA[112], '0644': DATA[113], '0801': DATA[114], '0802': DATA[115], '0803': DATA[116], '0804': DATA[117]}

    ROW = lambda row, DATA=DATA: DATA[row]
    COLUMN = lambda column, DATA=DATA: [data[column] for data in DATA]
    AT = lambda row,column, DATA=DATA: DATA[row][column]

    def __init__(self,paramTuple):
        self.code, self.fieldinError, self.fieldName, self.rejectReason = paramTuple

class Responses (metaclass=ADFMeta):
    DATA = (('00', 'Successful approval/completion'), ('01', 'Refer to card Issuer'), ('02', 'Refer to card Issuer, special condition'), ('03', 'Invalid merchant or service provider'), ('04', 'Pick up card'), ('05', 'Do not honor'), ('06', 'Error'), ('07', 'Pick up card, special condition (other than lost/stolen card)'), ('08', 'Honor with ID (Mastercard specific)'), ('10', 'Partial Authorization'), ('12', 'Invalid transaction'), ('13', 'Invalid amount'), ('14', 'Invalid account number (no such number)'), ('15', 'No such Issuer'), ('19', 'Re-enter transaction'), ('21', 'No action taken (unable to back out prior transaction)'), ('25', 'Unable to locate record in file, or account number is missing from the inquiry'), ('28', 'File is temporarily unavailable'), ('30', 'Format Error - Decline (Mastercard specific)'), ('34', 'Mastercard use only , Suspect Fraud (Used in reversal requests only)'), ('39', 'No credit account (Visa ePay)'), ('41', 'Pick up card (lost card)'), ('43', 'Pick up card (stolen card)'), ('51', 'Insufficient funds'), ('52', 'No checking account'), ('53', 'No savings account'), ('54', 'Expired card'), ('55', 'Incorrect PIN'), ('57', 'Transaction not permitted to cardholder'), ('58', 'Transaction not allowed at terminal'), ('59', 'Transaction not allowed at merchant'), ('61', 'Exceeds withdrawal amount limit (activity amount limit exceeded)'), ('62', 'Restricted card (invalid in region or country)'), ('63', 'Security violation (source is not correct issuer)'), ('65', 'Activity count limit exceeded'), ('75', 'Allowable number of PIN-entry tries exceeded'), ('76', 'Reversal: Unable to locate previous message (no match on Retrieval\nReference number)'), ('77', 'Previous message located for a repeat or reversal, but repeat or reversal data\nare inconsistent with original message'), ('78', 'Invalid/nonexistent account - Decline (Mastercard specific)'), ('79', 'Already reversed (by Switch)'), ('80', 'No financial Impact (Reversal for declined debit).\nInvalid date (for use in private label card transactions)'), ('81', 'PIN cryptographic error found (error found by the Visa security module during\nPIN decryption)'), ('82', 'Incorrect CVV'), ('83', 'Unable to verify PIN'), ('84', 'Invalid Authorization Life Cycle - Decline (Mastercard)\nDuplicate Transaction Detected (Visa)'), ('85', 'No reason to decline a request for account number verification or address\nverification'), ('86', 'Cannot verify PIN'), ('91', 'Issuer unavailable or switch inoperative (STIP not applicable or available for\nthis transaction)'), ('92', 'Destination cannot be found for routing'), ('93', 'Transaction cannot be completed; violation of law'), ('94', 'Duplicate Transmission Detected (Integrated Debit and Mastercard)'), ('96', 'System malfunction'), ('B1', 'Surcharge amount not permitted on Visa cards or EBT Food Stamps'), ('B2', 'Surcharge amount not supported by debit network issuer'), ('CV', 'Card type verification error'), ('EC', 'CID verification error'), ('N0', 'Force STIP'), ('N3', 'Cash service not available'), ('N4', 'Cash request exceeds Issuer limit'), ('N5', 'Ineligible for re-submission'), ('N7', 'Decline for CVV2 failure'), ('N8', 'Transaction amount exceeds preauthorized approval amount'), ('P2', 'Invalid biller Information'), ('R0', 'The transaction was declined or returned because the cardholder requested\nthat payment of a specific recurring or installment payment transaction be\nstopped.'), ('R1', 'The transaction was declined or returned because the cardholder has\nrequested that payment of all recurring or installment payment transactions for\na specific merchant account be stopped.'), ('Q1', 'Card Authentication failed'), ('V1', 'Daily Threshold Exceeded'), ('XA', 'Forward to Issuer'))
    LUT = {'00': DATA[0], '01': DATA[1], '02': DATA[2], '03': DATA[3], '04': DATA[4], '05': DATA[5], '06': DATA[6], '07': DATA[7], '08': DATA[8], '10': DATA[9], '12': DATA[10], '13': DATA[11], '14': DATA[12], '15': DATA[13], '19': DATA[14], '21': DATA[15], '25': DATA[16], '28': DATA[17], '30': DATA[18], '34': DATA[19], '39': DATA[20], '41': DATA[21], '43': DATA[22], '51': DATA[23], '52': DATA[24], '53': DATA[25], '54': DATA[26], '55': DATA[27], '57': DATA[28], '58': DATA[29], '59': DATA[30], '61': DATA[31], '62': DATA[32], '63': DATA[33], '65': DATA[34], '75': DATA[35], '76': DATA[36], '77': DATA[37], '78': DATA[38], '79': DATA[39], '80': DATA[40], '81': DATA[41], '82': DATA[42], '83': DATA[43], '84': DATA[44], '85': DATA[45], '86': DATA[46], '91': DATA[47], '92': DATA[48], '93': DATA[49], '94': DATA[50], '96': DATA[51], 'B1': DATA[52], 'B2': DATA[53], 'CV': DATA[54], 'EC': DATA[55], 'N0': DATA[56], 'N3': DATA[57], 'N4': DATA[58], 'N5': DATA[59], 'N7': DATA[60], 'N8': DATA[61], 'P2': DATA[62], 'R0': DATA[63], 'R1': DATA[64], 'Q1': DATA[65], 'V1': DATA[66], 'XA': DATA[67]}

    ROW = lambda row, DATA=DATA: DATA[row]
    COLUMN = lambda column, DATA=DATA: [data[column] for data in DATA]
    AT = lambda row,column, DATA=DATA: DATA[row][column]

    def __init__(self,paramTuple):
        self.code, self.definition = paramTuple

class States (metaclass=ADFMeta):
    DATA = (('Alabama', '01'), ('Alaska', '02'), ('Arizona', '04'), ('Arkansas', '05'), ('California', '06'), ('Colorado', '08'), ('Connecticut', '09'), ('Delaware', '10'), ('District of Columbia', '11'), ('Florida', '12'), ('Georgia', '13'), ('Hawaii', '15'), ('Idaho', '16'), ('Illinois', '17'), ('Indiana', '18'), ('Iowa', '19'), ('Kansas', '20'), ('Kentucky', '21'), ('Louisiana', '22'), ('Maine', '23'), ('Maryland', '24'), ('Massachusetts', '25'), ('Michigan', '26'), ('Minnesota', '27'), ('Mississippi', '28'), ('Missouri', '29'), ('Montana', '30'), ('Nebraska', '31'), ('Nevada', '32'), ('New Hampshire', '33'), ('New Jersey', '34'), ('New Mexico', '35'), ('New York', '36'), ('North Carolina', '37'), ('North Dakota', '38'), ('Ohio', '39'), ('Oklahoma', '40'), ('Oregon', '41'), ('Pennsylvania', '42'), ('South Carolina', '45'), ('South Dakota', '46'), ('Tennessee', '47'), ('Texas', '48'), ('Utah', '49'), ('Vermont', '50'), ('Virginia', '51'), ('Washington', '53'), ('West Virginia', '54'), ('Wisconsin', '55'), ('Wyoming', '56'), ('U.S. military bases,\nembassies, traveling\nmerchants', '99'))
    LUT = {'01': DATA[0], '02': DATA[1], '04': DATA[2], '05': DATA[3], '06': DATA[4], '08': DATA[5], '09': DATA[6], '10': DATA[7], '11': DATA[8], '12': DATA[9], '13': DATA[10], '15': DATA[11], '16': DATA[12], '17': DATA[13], '18': DATA[14], '19': DATA[15], '20': DATA[16], '21': DATA[17], '22': DATA[18], '23': DATA[19], '24': DATA[20], '25': DATA[21], '26': DATA[22], '27': DATA[23], '28': DATA[24], '29': DATA[25], '30': DATA[26], '31': DATA[27], '32': DATA[28], '33': DATA[29], '34': DATA[30], '35': DATA[31], '36': DATA[32], '37': DATA[33], '38': DATA[34], '39': DATA[35], '40': DATA[36], '41': DATA[37], '42': DATA[38], '45': DATA[39], '46': DATA[40], '47': DATA[41], '48': DATA[42], '49': DATA[43], '50': DATA[44], '51': DATA[45], '53': DATA[46], '54': DATA[47], '55': DATA[48], '56': DATA[49], '99': DATA[50]}

    ROW = lambda row, DATA=DATA: DATA[row]
    COLUMN = lambda column, DATA=DATA: [data[column] for data in DATA]
    AT = lambda row,column, DATA=DATA: DATA[row][column]

    def __init__(self,paramTuple):
        self.stateName, self.code = paramTuple