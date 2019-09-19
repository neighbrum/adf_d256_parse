
from TSYS import DataTypes
import re
from io import StringIO

class ADFMeta(type):
    def __getitem__(cls,val):
        return cls.DATA[val]
    def __len__(cls):
        return len(cls.DATA)

class Record:
    regexpr = {key:re.compile(expr) for key,expr in DataTypes.items()}

    @staticmethod
    def isAlphaNumeric(value):
        return True if regexpr["AN"].fullmatch(value) else False
    @staticmethod
    def isAlpha(value):
        return True if regexpr["A"].fullmatch(value) else False
    @staticmethod
    def isSpace(value):
        return True if regexpr["S"].fullmatch(value) else False
    @staticmethod
    def isNumeric(value):
        return True if regexpr["N"].fullmatch(value) else False
    @staticmethod
    def isPackedDecimal(value):
        return True if regexpr["PN"].fullmatch(value) else False

    def __init__(self):
        data = StringIO(self.data)
        for i in range(len(self.RECORD)):
            self.__dict__[list(self.__dict__.keys())[i]] = data.read(int(self.RECORD[i][2]))




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

#moved records so class type refernces would not complain

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


class BINHeaderRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field identifies that this record is the\nBIN Header.\nValue = BH01'),('2','Acquirer BIN','6','5-10','A/N',"This field identifies the financial institution acting as the Acquirer of this customer transaction."),('3','Reserved (for future use)','890','11-900','A/N','Reserved'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
        "acquirerBIN":None,
        "reserved1":None
                }

    LENGTH = 900

    def __init__(self,f):
        self.recordType, self.acquirerBIN, self.reserved1 = (None,None,None)
        self.data = f.read(BINHeaderRecord.LENGTH)
        super(BINHeaderRecord, self).__init__()
        
class BINTrailerRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates that this record is\nthe BIN Trailer.\nValue = BT01'), ('2', 'Acquirer BIN', '6', '5-10', 'A/N', 'This field identifies the financial\ninstitution acting as the Acquirer of\nthis customer transaction.'), ('3', 'BIN Total Report Count', '8', '11-18', 'N', 'This field identifies the total number of\nReport(s) that are included for a\nparticular BIN.'), ('4', 'BIN Total Transaction\nCount', '12', '19-30', 'N', 'This field identifies the total number of\ntransactions that are included for a\nparticular BIN.'))

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
        self.recordType, self.acquirerBIN, self.bINTotalReportCount, self.bINTotalTransactionCount = (None, None, None, None)
        self.data = f.read(BINTrailerRecord.LENGTH)
        super(BINTrailerRecord, self).__init__()
        
class DiscoverPayPalExtensionRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates this record\nis the Discover/PayPal\nExtension Record.\nValue = EX01'), ('2', 'Discover/PayPal\nAcquirer ID', '11', '5-15', 'N', 'This field identifies a unique\nidentification number\nassigned by Discover /PayPal\nNetworks to the Acquirer.'), ('3', 'Discover/PayPal\nMerchant ID', '15', '16-30', 'AN', 'This field identifies a unique\nnumber assigned to the\nmerchant by Discover/PayPal\nNetworks.'), ('4', 'Discover/PayPal\nProcessing Code', '6', '31-36', 'N', 'This value identifies the\ncardholder transaction type\nand cardholder account type\n(if any) that are affected by\nthe transaction.\nTransaction Type -\nPositions 1-2\n00 - Purchase of\nGoods / Services\n01 - Withdrawal/Cash\nAdvance\n09 - Purchase of\nGoods or Services with\nCash Over\n13 - Address\nVerification with a\nGoods or Service\nAuthorization for\nRecurring Billing\n14 - Recurring Billing\n(Automatic Payment)-\nGoods or Service\n15 - Installment\nPayment - Goods or\nService\n18 - Address\nVerification Only\n20 - Merchandise\nReturn\n28 - Recharge/Reload\n31 - Balance Inquiry\n90 - Activation\nAccount Type From -\nPositions 3-4\n00 - Not\nApplicable/Not\nSpecified\n10 - Savings Accounts\n20 - Checking Account\n30 - Credit Card\nAccount\nAccount Type To -\nPositions 5-6\n00 - Not\nApplicable/Not\nSpecified'), ('5', 'Discover/PayPal\nPOS Entry Mode', '4', '37-40', 'N', 'This field consists of two\nnumbers to indicate the\nmethod used to enter the\nPrimary Account Number\n(PAN) into the system and\none number to indicate the\nPIN entry capabilities.\nPAN and Date Entry Mode -\nPositions 1-2\n00 - Unknown\n01 - Manual (Key\nEntered)\n02 - Magnetic Stripe\n03 - Bar\nCode/Payment Code\n04 - Optical Character\nReader (OCR)\n05 - Integrated Circuit\nCard Reader\n07 - Electronic\nCommerce\n81 - Radio Frequency\nID Indicator - Magnetic\nStripe\n82 - Mobile Commerce\n(mCommerce)\n83 - Radio Frequency\nID Indicator - Chip\n85 - Chip Fallback\n90 - Voice\nAuthorizations\n91 - Voice Response\nUnit\n92 - Batch\nAuthorizations\n93 - Batch\nAuthorizations Cash\nAccess\nPIN Entry Capability -\nPositions 3\n0 - Unspecified or\nUnknown\n1 - PIN entry capability\n2 - POS device does\nnot have PIN entry\ncapability\n8 - POS device has\nPIN entry capability,\nbut PIN pad is not\ncurrently operative\n9 - PIN verified by POS\ndevice\nTSYS Reserved - Position 4\nSpace - Reserved for\nfuture use'), ('6', 'Discover/PayPal\nResponse Code', '3', '41-43', 'A/N', 'This field identifies the\nauthorization response code\nfrom the authorizer.\nPositions 1-2\nPOS Response Code value\n(Discover ISO field 39)\nPosition 3\nSpace - TSYS Reserved'), ('7', 'Discover/PayPal\nPOS Data Code', '13', '44-56', 'A/N', 'This value defines specific\ncard information capture\nconditions present at the time\na card transaction took place\nat the point of service.\nDiscover/PayPal POS Data\nCode for valid values'), ('8', 'Discover Cash Over\nAmount', '12', '57-68', 'N', 'This field identifies the\namount of cash over\ndisbursed.'), ('9', 'Discover/PayPal\nAVS Response Code', '1', '69', 'AN', 'This value contains the\nAddress Verification Service\nResponse Code (AVS)\nResponse Code received from\nDiscover/PayPal.'), ('10', 'Cardholder Full\nName Result Code', '1', '70', 'AN', 'Possible values:\nB - Unknown response\ndue to blank input\nF - First Name\nMatches, Last Name\ndoes not match\nK - Unknown\nL - First Name does\nnot match, Last Name\nmatches\nM - First Name and\nLast Name match\nN - Nothing matches\nP - Not processed\nU - Retry, system\nunable to process\nW - No data from\nIssuer/ Authorization\nsystem'), ('11', 'Registered User\nIndicator', '1', '71', 'A/N', "This field indicates if the\ncardholder is a registered\nuser on a merchant's website\n(Discover transactions only).\nY - The cardholder is a\nregistered user with an online\nprofile and login credentials\nN - The cardholder is not a\nregistered user, and may\nshop only as a guest"), ('12', 'Last Registered User\nProfile Date Change', '8', '72-79', 'N', 'This field contains the date\nwhen the cardholder last\nvoluntarily changed their\nregistered profile (Discover\ntransactions only).\nFormat: MMDDYYYY'), ('13', 'PAN Reference\nIdentifier (PRI)', '35', '80-114', 'A/N', 'This field indicates the value\nassigned by Discover at the\ntime of token provisioning and\nis associated with a specific\nmobile wallet.'), ('14', 'Reserved', '38', '115-152', 'A/N', 'Reserved'))

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
        self.recordType, self.discoverPayPalAcquirerID, self.discoverPayPalMerchantID, self.discoverPayPalProcessingCode, self.discoverPayPalPOSEntryMode, self.discoverPayPalResponseCode, self.discoverPayPalPOSDataCode, self.discoverCashOverAmount, self.discoverPayPalAVSResponseCode, self.cardholderFullNameResultCode, self.registeredUserIndicator, self.lastRegisteredUserProfileDateChange, self.pANReferenceIdentifier, self.reserved13 = (None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        self.data = f.read(DiscoverPayPalExtensionRecord.LENGTH)
        super(DiscoverPayPalExtensionRecord, self).__init__()
        
class MastercardExtensionRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates that the\nrecord is the Mastercard\nExtension Record.\nValue = EX02'), ('2', 'Association Timestamp', '10', '5-14', 'A/N', 'Date and time in MMDDhhmmss\nformat'), ('3', 'EMS Risk Score', '3', '15-17', 'N', 'Expert Monitoring Solutions Risk\nScore\nThis field is included in the\nresponse, and indicates the\ntransaction risk score.\nValid value:\n001-998'), ('4', 'EMS Score Reason\nCode', '2', '18-19', 'A/N', 'This Reason Code for the EMS\nscore indicates the key factors\nthat influenced the fraud score.'), ('5', 'Domain Server', '1', '20', 'N', 'Valid values:\n1=Issuer Domain\n2=Acquirer Domain'), ('6', 'Mobile Device Type', '2', '21-22', 'N', 'This field identifies the type of\nPayPass device used by the\ncardholder to initiate the\ntransaction. This field is required\nfor all Mastercard PayPass\n(contactless) transactions.\nValid values'), ('7', 'Transit Transaction\nType Indicator', '2', '23-24', 'N', 'This field identifies the type of\ntransit transactions.'), ('8', 'Transportation Mode\nIndicator', '2', '25-26', 'N', 'This field identifies the mode of\ntransportation used.'), ('9', 'Mastercard Wallet\nIdentifier', '3', '27-29', 'A/N', 'This Mastercard value is\ngenerated by the Masterpass\nonline platform. This value is\npassed to the merchant at the\ntime of consumer checkout for\necommerce transactions, and is\nincluded in the authorization\nrequest.'), ('10', 'Authorization Indicator', '1', '30', 'A/N', 'This field defines the type of\nauthorization request and is\nrequired to be included on all\nMastercard authorization request\ntransactions.\nValid values:\nF - Final Authorization - A\nrequest for a final amount\nthat may not be canceled\nonce it is approved\nP - Pre-Authorization - A\nrequest for an estimated\namount\nU - Undefined\nAuthorization - Used when\nthe intent is unknown, and\nthe transaction is neither\na preauthorization nor a\nfinal authorization'), ('11', 'Lane ID', '8', '31-38', 'N', 'This data uniquely identifies a\nterminal at the card acceptor\nlocation of acquiring institutions\nor merchant POS systems.'), ('12', 'Transaction Integrity\nClass', '2', '39-40', 'A/N', 'This value shows the safety and\nsecurity of the transaction and\nincludes the final assessment of\nthe validity of the card and the\ncardholder. Some transactions\nare inherently more secure than\nothers are. For example, EMV\nchip cards are more secure than\nmagnetic stripe cards. There are\nnuances across both the\ntechnology (card) and the\nCardholder Verification Method\n(cardholder), but the combination\nwas assessed across the\nspectrum to determine the overall\nintegrity of the transaction.\nNote: This field is required when\nincluded by Mastercard. Effective\nin April 2019, Mastercard\nincorporates the Transaction\nIntegrity Class in the interchange\nprocess.\nValid Values:\nCard and Cardholder Present:\nA1 - EMV/Token in a Secure,\nTrusted Environment\nB1 - EMV/Chip Equivalent\nC1 - Mag Stripe\nE1 - Key Entered\nU0 � Unclassified\nCard and/or Cardholder Not\nPresent:\nA2 - Digital Transactions\nB2 - Authenticated Checkout\nC2 - Transaction Validation\nD2 - Enhanced Data\nE2 - Generic Messaging\nU0 - Unclassified'), ('13', 'Reserved', '112', '41-152', 'A/N', 'Reserved'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"associationTimestamp": None,
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
        self.recordType, self.associationTimestamp, self.eMSRiskScore, self.eMSScoreReasonCode, self.domainServer, self.mobileDeviceType, self.transitTransactionTypeIndicator, self.transportationModeIndicator, self.mastercardWalletIdentifier, self.authorizationIndicator, self.laneID, self.transactionIntegrityClass, self.reserved12 = (None, None, None, None, None, None, None, None, None, None, None, None, None)
        self.data = f.read(MastercardExtensionRecord.LENGTH)
        super(MastercardExtensionRecord, self).__init__()
        
class AdditionalDetailDataExtensionRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates this\nrecord is the Additional\nDetail Data Extension\nRecord.\nValue = EX03'), ('2', 'Terminal Verification\nResults', '10', '5-14', 'A/N', 'This field identifies the status\nof the different functions as\nseen from the terminal.'), ('3', 'Cardholder\nVerification Method', '6', '15-20', 'A/N', 'This field identifies a method\nof verification of the\ncardholder supported by the\napplication.'), ('4', 'Form Factor\nIndicator', '8', '21-28', 'A/N', 'This field defines the type of\nconsumer device used to\nconduct a\ncontact/contactless\ntransaction.'))

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
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates this record\nis the Additional Detail Data\nExtension Record.\nValue = EX04'), ('2', 'PSP Name', '20', '5-24', 'A/N', 'Payment Service Provider or\nAggregator'), ('3', 'Seller Street\nAddress', '25', '25-49', 'A/N', 'Street Address of the Seller'), ('4', 'Seller City', '13', '50-62', 'A/N', 'Seller�s City'), ('5', 'Seller Postal Code', '10', '63-72', 'A/N', 'Seller�s Postal Code'), ('6', 'Seller Region Code', '3', '73-75', 'A/N', 'Seller�s State/Region Code'), ('7', 'Seller Email', '40', '76-115', 'A/N', 'This field identifies the email\naddress for the Seller of the\nPayment Service\nProvider/Aggregator or OptBlue\nparticipant.'), ('8', 'Seller Telephone', '10', '116-125', 'A/N', 'This field identifies the\ntelephone number for the Seller\nof the Payment Service\nProvider/Aggregator or OptBlue\nparticipant.'), ('9', 'Reserved', '27', '126-152', 'A/N', 'Reserved'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"pSPName": None,
		"sellerStreetAddress": None,
		"sellerCity": None,
		"sellerPostalCode": None,
		"sellerRegionCode": None,
		"sellerEmail": None,
		"sellerTelephone": None,
		"reserved8": None
                }

    LENGTH = 160

    def __init__(self,f):
        self.recordType, self.pSPName, self.sellerStreetAddress, self.sellerCity, self.sellerPostalCode, self.sellerRegionCode3, self.sellerEmail, self.sellerTelephone, self.reserved8 = (None, None, None, None, None, None, None, None, None)
        self.data = f.read(MerchantDataExtensionRecord.LENGTH)
        super(MerchantDataExtensionRecord, self).__init__()
        
class ReportHeader(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field identifies that this record is the\nReport Header.\nValue = RH01'), ('2', 'Acquirer BIN', '6', '5-10', 'A/N', 'This field identifies the financial institution\nacting as the Acquirer of this customer\ntransaction.'), ('3', 'Agent', '6', '11-16', 'A/N', 'This value identifies the agent filter, if\ndefined, from the report registration. The\nagent is a six character value assigned\nby the merchant�s bank or processor.\nThe field is issued by the merchant�s\nmember bank or processor for purposes\nof identifying a specific agent entity of the\nmember bank or processor.\nPossible values:\n6 character agent value\nNA - then left justified, space filled\nSpace filled'), ('4', 'Chain', '6', '17-22', 'A/N', 'This value identifies the chain filter, if\ndefined, from the report registration. The\nChain is a six character value assigned\nby the merchant�s bank or processor.\nThe field is issued by the merchant�s\nmember bank or processor for purposes\nof identifying a specific chain of the agent\norganization.\nPossible values:\n6 character chain value\nNA - then left justified, space filled\nSpace filled'), ('5', 'Effective Start Date &\nT\nime', '19', '23-41', 'A/N', 'This field identifies the start date and\ntime (GMT) from the report registration.\nExample:\nYYYY-MM-DD HH:MM:SS (using a 24-\nhour clock)'), ('6', 'Effective End Date &\nT\nime', '19', '42-60', 'A/N', 'This field identifies the end date and time\nGreenwich Mean Time (GMT) from the\nreport registration.\nExample:\nYYYY-MM-DD HH:MM:SS (using a 24-\nhour clock)'))

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
        self.recordType, self.acquirerBIN, self.agent, self.chain, self.effectiveStartDateTime, self.effectiveEndDateTime = (None, None, None, None, None, None)
        self.data = f.read(ReportHeader.LENGTH)
        super(ReportHeader, self).__init__()
        
class ReportHeaderRecord(Record):
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates that this record is\nthe Report Header.\nValue = RH02'), ('2', 'Acquirer BIN', '6', '5-10', 'A/N', 'This field identifies the financial\ninstitution acting as the Acquirer of\nthis customer transaction.'), ('3', 'Agent', '6', '11-16', 'A/N', 'This field identifies the agent filter, if\ndefined, from the report registration.\nThe agent is a six character value\nassigned by the merchant�s bank or\nprocessor.\nPossible values:\n6 character agent value\nNA - then left justified space\nfilled\nSpace filled'), ('4', 'Chain', '6', '17-22', 'A/N', 'This field identifies the chain filter, if\ndefined, from the report registration.\nThe Chain is a six character value\nassigned by the merchant�s bank or\nprocessor.\nPossible values:\n6 character chain value\nNA - then left justified, space\nfilled\nSpace filled'), ('5', 'Effective Start Date &\nT\nime', '19', '23-41', 'A/N', 'This field identifies the start date and\ntime (GMT) from the report\nregistration.\nExample:\nYYYY-MM-DD HH:MM:SS (using a\n24-hour clock)'), ('6', 'Effective End Date &\nT\nime', '19', '42-60', 'A/N', 'This field identifies the end date and\ntime (GMT) from the report generation.\nExample:\nYYYY-MM-DD HH:MM:SS (using a\n24-hour clock)'), ('7', 'Include Host Capture\nTransactions', '1', '61', 'A/N', 'This field indicates if host capture\nadjustment and inquiry transactions\nare present in the report.\nPossible values:\n1 - Includes adjustment\ntransaction (TD02) and inquiry\ntransaction (TD03) records\n2 - Includes batch inquiry\ntransactions only\n3 - Includes adjustment\ntransactions only'))

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
        self.recordType, self.acquirerBIN, self.agent, self.chain, self.effectiveStartDateTime, self.effectiveEndDateTime, self.includeHostCaptureTransactions = (None, None, None, None, None, None, None)
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
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates that this record\nis the Transaction Detail Header.\nValue = TD01'), ('2', 'Acquirer BIN', '6', '5-10', 'A/N', 'This field identifies the financial\ninstitution acting as the Acquirer of\nthis customer transaction.'), ('3', 'Exit BIN', '5', '11-15', 'A/N', 'This field identifies the extra data\nthat is received from the ISO\nmessage for the BIN.'), ('4', 'Agent', '6', '16-21', 'A/N', 'The field is assigned by the\nmerchant�s member bank or\nprocessor for purposes of\nidentifying a specific agent entity\nof the member bank or processor.\nPossible values:\n6 character Agent value\nNA - then left justified,\nspace filled\nSpace filled'), ('5', 'Chain', '6', '22-27', 'A/N', 'The field is assigned by the\nmerchant�s member bank or\nprocessor for purposes of\nidentifying a specific chain of the\nagent organization.\nPossible values:\n6 character Chain value\nNA - then left justified,\nspace filled\nSpace filled'), ('6', 'e-Connections\nMerchant\nNumber', '15', '28-42', 'A/N', 'This field identifies the merchant\nnumber that is displayed in the e-\nConnections Authorization and\nCapture module.'), ('7', 'Store Number', '4', '43-46', 'A/N', 'This field identifies the store\nnumber.'), ('8', 'Terminal Number', '4', '47-50', 'A/N', 'This field identifies the terminal\nnumber.'), ('9', 'Card Acceptor\nID', '15', '51-65', 'A/N', 'This field identifies the merchant\nnumber plus the first three of the\nstore.'), ('10', 'Merchant Name', '25', '66-90', 'A/N', 'This field identifies the name of the\nmerchant.\nThis field identifies the name of the\nSub-Merchant if the transaction is\nsubmitted by a Payment\nFacilitator.'), ('11', 'Card Acceptor\nCity', '18', '91-108', 'A/N', "This field identifies the merchant's\nlocation where the cardholder�s\ntransaction occurs.\nExample: Chandler\nThis field identifies the City of the\nSub-Merchant if the transaction is\nsubmitted by a Payment\nFacilitator."), ('12', 'Card Acceptor\nState', '2', '109-110', 'A/N', "This field identifies the merchant's\nlocation where the cardholder�s\ntransaction occurs. \nExample: AZ\nThis field identifies the State of the\nSub- Merchant if the transaction is\nsubmitted by a Payment\nFacilitator."), ('13', 'Card Acceptor\nCountry Code', '2', '111-112', 'A/N', "Includes the merchant's location\nwhere the cardholder�s transaction\noccurs.\nThis field identifies the Country\nCode of the Sub-Merchant if the\ntransaction is submitted by a\nPayment Facilitator."), ('14', 'Country Code\nPAN Extended', '3', '113-115', 'A/N', 'This field identifies a code in the\ncard�s magnetic stripe that\nidentifies the country of the card\nissuer institution.'), ('15', 'National POS\nGeographic Data', '14', '116-129', 'A/N', 'This field identifies the location of\nthe cardholder transaction.\nThis field identifies the location of\nthe Sub- Merchant if the\ntransaction is submitted by a\nPayment Facilitator\nState code (positions 1-2)\nCounty code (positions 3-5)\nPostal code (positions 6-\n14)\nSee U.S. state codes for a list of\nstate codes.'), ('16', 'MCC Code', '4', '130-133', 'N', 'This field identifies a merchant\ncategory code that describes a\nmerchant�s type of business,\nproduct, or service.'), ('17', 'Merchant ABA\nNumber', '9', '134-142', 'A/N', 'This field identifies the Merchant\nABA Number. It consists of 0 to 9\ncharacters and identifies the\nmerchant to a direct debit switch.\nThis number is provided by the\nsigning member or processor.'), ('18', 'Card Acceptor\nSettlement\nAgent', '4', '143-146', 'A/N', 'This field identifies the financial\ninstitution.'), ('19', 'ISO Source\nStation ID', '6', '147-152', 'N', 'This field identifies the originator of\nthe ISO request message.'), ('20', 'Acquirer\nBusiness ID', '8', '153-160', 'A/N', 'This field identifies the VISA\nassigned Acquirer Business ID.'), ('21', 'Acquirer Country\nCode', '3', '161-163', 'A/N', 'This field identifies the country of\nthe acquiring institution for the\nmerchant.'), ('22', 'Card Type', '1', '164', 'A/N', 'This field identifies the card plan\ntype.\nA <space> or "?" value in this field\nindicates the card type was\nunknown.\nCREDIT\nThe transaction is identified\nas credit if ADF Field 84\nNID=�NULL� or �0002�\n3\nAmerican Express\n4\nVisa\n5\nMastercard\n7\nJCB\n8\nDiscover\n9\nOther\nP\nPayPal\nDEBIT\nThe transaction is identified as\ndebit if Field 84 NID is not =\n�NULL� and NID is not=�0002�\nSee Network ID and Sharing\nGroup Codes for a list of codes.'), ('23', 'Primary Account\nNumber', '22', '165-186', 'A/N', 'This field identifies the primary\naccount number.\nThis field may be masked based\non configuration.'), ('24', 'EXT PAN', '28', '187-214', 'A/N', 'This field is used for the numeric\naccount numbers or numbers\nencoded on track 3. It may also\ncontain a cardholder identification\nnumber that points to one or more\ncardholder accounts.\nThis field may be masked based\non configuration.'), ('25', 'Account ID 1', '28', '215-242', 'A/N', 'For Mastercard transactions, this\nvalue is used for the Paypass\nPrimary Account Number.\nFormatting is left justified and\nspace filled.\nThis field may be masked based\non configuration.'), ('26', 'Card expiration\nDate', '4', '243-246', 'N', 'This field identifies the card\nexpiration date in YYMM format.'), ('27', 'Issuing\nInstitution\nStation ID', '6', '247-252', 'A/N', 'This field identifies the endpoint\nthat introduced the message into\nthe network.'), ('28', 'Issuing\nInstitution ID\nCode', '11', '253-263', 'A/N', 'This field identifies the Issuer ID of\nthe cardholder�s account.'), ('29', 'Julian Day', '3', '264-266', 'N', 'This field identifies the Julian day\nof the year, which is a number\nrepresenting the ordinal position of\nthe transaction date.\nFormat = DDD\nExample: December 30 in a non-\nleap year = 364'), ('30', 'Transaction Date\n& Time', '19', '267-285', 'A/N', 'This field identifies the date and\ntime stamp of a transaction based\non GMT.\nExample:\nYYYY-MM-DD HH:MM:SS (using\na 24-hour clock)'), ('31', 'Settlement Date', '4', '286-289', 'N', "This field identifies the month and\nthe day when the message\nbecame part of SMS' settlement\nbetween the acquirer and issuer.\nExample: 0501"), ('32', 'Load Date &\nT\nime', '19', '290-308', 'A/N', 'This field identifies the date and\ntime (GMT) the transaction was\nloaded into the report by a third\nparty.\nExample:\nYYYY-MM-DD HH:MM:SS (using\na 24-hour clock)'), ('33', 'Message Type', '4', '309-312', 'A/N', 'This value identifies the ISO\nrequest type.\nMessage types 0100/0200/0400/\n0420 are messages from an\nendpoint to a card issuer. TSYS\nAcquiring Solutions uses these for\nauthorization and verification\nrequests to be routed from the\nendpoint to the card issuer.\n0120 message types are for\nAutomated Fuel Dispenser (AFD)\nadvice messages indicating the\nfinal amount dispensed.'), ('34', 'Processing\nCode', '6', '313-318', 'A/N', 'This value identifies the cardholder\ntransaction type and cardholder\naccount types (if any) that are\naffected by the transaction:\nPositions 1 - 2: Transaction Type\nPositions 3 - 4: Account Type\n(from)\nPositions 5 - 6: Account Type (to)'), ('35', 'Access Method', '2', '319-320', 'A/N', 'This value identifies the\nconnectivity method utilized to\ntransmit the transaction and maps\ndirectly to the ASCII Line Type.\nRefer to Access Method Definition\nof Values for possible values.'), ('36', 'ASCII Bill Code', '1', '321', 'A/N', 'This value identifies the billing\ndescriptor. It may contain\nadditional billing or reporting\ninformation.\nRefer to Access Method Definition\nof Values for possible values.'), ('37', 'Transaction\nIdentifier', '15', '322-336', 'A/N', 'This value identifies a key element\nthat links original authorization and\nfinancial requests to subsequent\nmessages.'), ('38', 'Retrieval\nReference\nNumber', '12', '337-348', 'N', 'This value identifies a number that\nis used with other key data\nelements to identify and track all\nmessages related to a given\ncardholder transaction.'), ('39', 'Systems Trace\nAudit Number', '6', '349-354', 'A/N', 'This value uniquely identifies a\ncardholder transaction and all the\nmessage types it comprises per\nindividual program rules.'), ('40', 'Authorized\nAmount', '12', '355-366', 'N', 'This value identifies the\ntransaction amount. The decimal\nplace is implied based on\ncurrency.\nFor AFD message types, this\nvalue represents the final amount\nto be settled.'), ('41', 'Cardholder\nBilling Amount', '12', '367-378', 'N', 'This value identifies a transaction\namount converted to the currency\nused to bill the cardholder�s\naccount.'), ('42', 'Approval Code', '6', '379-384', 'A/N', 'This value identifies the approval\ncode from the authorizer.'), ('43', 'Authorization\nResponse', '2', '385-386', 'A/N', 'This value identifies the\nauthorization response code from\nthe authorizer.\nRefer to Response Codes for valid\nresponse codes.'), ('44', 'Internal Error\nCode', '1', '387', 'A/N', 'Possible values:\nT = Timeout\nG = Standard GEN2\nparsing/edit error\nS = SARATOGA\nparsing/edit error\nV = VIP ISO reject (This\nISO reject condition can\nonly occur for VIP\ntransactions.)\nC = Citi GEN2 parsing/edit\nerror\nBlank = not timeout or new\nreject type'), ('45', 'ISO Reject Code', '4', '388-391', 'A/N', 'This field identifies the specific\ntype of reject if an internal error\ncode exists.\nRefer to Reject Codes and\nNumeric Sequence for a list of\nreject codes.'), ('46', 'CVV2 / CVC2 /\nCID Response\nType', '1', '392', 'A/N', 'This field identifies the presence of\nthe Card Verification Values.\nValid values:\n0 = Only the normal\nresponse code in ISO field\n39 should be returned\n1 = The normal response\ncode in ISO field 39 and the\nCVV2 result in ISO field\n44.10 should be returned'), ('47', 'CVV2 / CVC2 /\nCID Presence\nIndicator', '1', '393', 'A/N', 'This field identifies the presence of\ncard verification values.\nValid values:\n0 = CVV2 value is\ndeliberately bypassed or is\nnot provided by the\nmerchant\n1 = CVV2 value is present\n2 = CVV2 is on the card\nbut is illegible\n9 = Cardholder states that\nthe card does not have a\nCVV2 imprint'), ('48', 'Message\nReason Code', '4', '394-397', 'A/N', 'This field supports multiple\nusages.\nReversal Messages\nIf there is no reversal, data will not\nbe present.\nPossible values for Reversal\nMessages:\n2501 - Transaction voided\nby customer\n2502 - Transaction has not\ncompleted (Request timed\nout or terminal\nmalfunctioned)\n2503 - No confirmation from\nthe point of sale\n2504 - POS partial reversal\n2516 - Premature chip card\nremoval (after online\nrequest sent, before\nresponse received)\n2517 - Chip declined\ntransaction after online\nissuer approved\nVisa Merchant Initiated\nTransactions\nThe Message Reason Code field\nwill be used to identify Merchant\nInitiated Transactions (MIT) for\nVisa. A MIT is any transaction that\nrelates to a previous consumer-\ninitiated transaction, but is\nconducted without the consumer\nbeing present and without any\ncardholder validation performed.\nPossible values for Visa\nMerchant Initiated\nTransactions:\n3900 - Incremental\nAuthorization\n3901 - Resubmission\n3902 - Delayed Charges\n3903 - Reauthorization\n3904 - No Show'), ('49', 'Additional\nResponse Data', '25', '398-422', 'A/N/S', 'This field contains miscellaneous\nresponse message data. TSYS\nAcquiring Solutions uses this field\nand its subfields for the following\nspecial codes:\nRefer to Additional Response Data\nCodes for a list of codes to include\nthe length, position, and\ndescription.'), ('50', 'Request ACI', '1', '423', 'A/S', 'This field identifies if a transaction\nrequested CPS qualification when\nit was sent by the merchant.\nRefer to Authorization\nCharacteristics Indicators for\npossible values.'), ('51', 'Return ACI', '1', '424', 'A/S', 'This field identifies the response to\nthe ACI Request.\nRefer to Authorization\nCharacteristics Indicators for\npossible values.'), ('52', 'Validation Code', '4', '425-428', 'A/N', 'This field identifies a Visa\ncalculated code in the\nauthorization message to ensure\nthat key fields match their\nrespective fields in the Visa BASE\nII clearing message.\nFor Discover and PayPal\ntransactions, the field contains the\nTransaction Data Condition Code\nutilizing the first 2 bytes of the\nfield.'), ('53', 'Product Type\nIdentification', '2', '429-430', 'N', 'Refer to Card Product Codes for a\nlist of values.'), ('54', 'Transaction\nSource Flag', '3', '431-433', 'A/N', 'This field identifies the Telecom\nprovider for authorizations handled\nthrough TSYS Acquiring Solutions.'), ('55', 'VAR Track ID', '10', '434-443', 'A/N', 'This field identifies the Developer\nID for the transaction.'), ('56', 'Vendor ID', '5', '444-448', 'N', 'This field identifies the Vendor ID\nfor the transaction.'), ('57', 'POS Entry\nMode', '4', '449-452', 'A/N', "This value identifies the method\nused to capture the account\nnumber and expiration from the\ncard and the terminal's PIN\ncapture capability.\nRefer to\n POS Entry Mode Codes\nfor values."), ('58', 'ISA Charge\nIndicator', '1', '453', 'A/N', 'This field indicates whether the\nVisa ISA charge was assessed.'), ('59', 'AMEX\nCardholder\nVerification\nResults', '9', '454-462', 'ANS', 'Bytes 1-5 contain verification\ncodes received from AMEX in the\nauthorization response.\nRefer to Amex Cardholder\nVerification Results for a list of\npossible values.\nBytes 6-9 are reserved and space\nfilled.'), ('60', 'POS Condition\nCode', '2', '463-464', 'A/N', 'This value identifies transaction\nconditions at the point of sale or\npoint of service.\nRefer to POS Condition Codes for\na list of codes.'), ('61', 'Additional Data\nPrivate Request', '20', '465-484', 'A/N', 'Refer to Additional Data Private\nRequest for a list that defines the\nusage code key for all private\nrequests for additional data.'), ('62', 'Additional Data\nPrivate\nResponse', '20', '485-504', 'A/N', 'Values are identical to those in\nAdditional Data Private Request'), ('63', 'Supporting\nInformation', '60', '505-564', 'A/N/S', 'Private use field with the following\nusages:\nUsage\nNotes\n1\nReserved for future\nuse\n2\nReserved for future\nuse\n3\nReserved for future\nuse\n4\nReserved for future\nuse\n5\nReserved for future\nuse\n7\nReserved for future\nuse'), ('64', 'Duration', '2', '565-566', 'A/N', 'This field identifies the number of\ndays (from 01 through 99)\nanticipated for the auto rental or\nhotel stay.'), ('65', 'Market Specific\nData Indicator', '1', '567', 'A/N', 'This field identifies the industry for\nwhich market specific data has\nbeen provided.\nPossible values:\nCode\nDefinition\nA\nAuto Rental\nB\nBill Payment\nE\ncCommerce\nTransaction\nAggregation\nH\nHotel\nJ\nB2B Invoice\nPayments\nM\nHealthcare\nN\nFailed CPS Market\nData Edit\nT\nTransit'), ('66', 'Cash Back\nAmount', '12', '568-579', 'N', 'This field identifies the cash back\namount.'), ('67', 'Cardholder\nBilling\nConversion Rate', '9', '580-588', 'N', 'This field identifies a calculated\nvalue that represents a factor that\nmay be applied to the transaction\namount to obtain the cardholder\nbilling amount.'), ('68', 'Cardholder\nBilling Currency\nCode', '3', '589-591', 'A/N', 'This field contains a three-digit\ncode identifying the currency used\nby the Issuer to bill the\ncardholder�s account.\nRefer to \nCurrency Codes for a\nlist of currency codes.'), ('69', 'Request\nAdditional\nAmount', '20', '592-611', 'A/N', 'This field identifies account\nbalance information for ATM\nbalance inquiries, cash\ndisbursements, or available credit\nbalance inquiries.\nThe following is the field layout:\nPosition\nByte\nData\nValue\n \n1\nLength\n1-2\n23\nAccount\nType\n3-4\n4-5\nAmount\nType\n5-7\n6-8\nCurrency\nCode\n8\n9\nAmount\nSign\n9-20\n10-20\nAmount'), ('70', 'Mastercard\nAssigned ID', '6', '612-617', 'A/N', 'This value in this field is assigned\nby Mastercard to identify\nmerchants participating in various\nprograms or for data integrity\npurposes.'), ('71', 'Mastercard IIAS\nIndicator', '1', '618', 'N', 'Inventory Information Approval\nSystem Indicator\n0 - Merchant terminal did\nnot verify the purchased\nitems against an IIAS\n1 - Merchant terminal\nverified the purchase items\nagainst an IIAS\n2 - Merchant claims\nexemption from IIAS based\non the 90 percent rule'), ('72', 'Response\nAdditional\nAmount', '20', '619-638', 'A/N', 'This value identifies the response\ninformation on ATM balance\ninquiries, cash disbursements, or\navailable credit balance inquiries.\nRefer to Field 69 Description\n(above) for field layout.'), ('73', 'Replacement\nAmounts', '12', '639-650', 'A/N', 'This value identifies the corrected\namount of a transaction if a partial\nreversal was completed.'), ('74', 'X\nID', '40', '651-690', 'A/N', 'This field identifies the unique\nVSEC transaction ID generated by\nthe merchant server to identify the\ntransaction.'), ('75', 'UCAF Collection\nIndicator', '1', '691', 'A/N', 'This field indicates whether\nMastercard Universal Cardholder\nAuthentication Data was included\nin the transaction message.\nValid values:\nValue\nDescription\n0\nUCAF data\ncollection is not\nsupported by the\nmerchant or a\nSecureCode\nmerchant chose not\nto undertake\nSecureCode on this\ntransaction\n1\nUCAF data\ncollection is\nsupported by the\nmerchant and UCAF\ndata was present\nand contained an\nattempted AAV for\nMastercard\nSecureCode\n2\nUCAF data\ncollection is\nsupported by the\nmerchant and UCAF\ndata was present\nand contained a\nfully authenticated\nAAV\n5\nIssuer Risk-Based\nDecisioning\n6\nMerchant Risk-\nBased Decisioning\n7\nPartial shipment,\nincremental, or\nrecurring payment'), ('76', 'Transaction\nCurrency Code', '3', '692-694', 'A/N', 'This field identifies a three-\ncharacter code used to define the\ncurrency of the transaction. It is\nalso used to determine the number\nof decimal places for ISO fields 4,\n61.1 and 95.1.\nRefer to \nCurrency Codes for a\nlist of currency codes.'), ('77', 'Gateway\nCurrency Code', '3', '695-697', 'A/N', 'This field identifies a three-\ncharacter code used to define the\ncurrency code of the gateway.\nRefer to \nCurrency Codes for a\nlist of currency codes.'), ('78', 'Gateway\nCountry Code', '3', '698-700', 'A/N', 'This field identifies the country\ncode of the gateway that\nprocessed the transaction.'), ('79', 'Receiving\nInstitution\nCountry Code', '3', '701-733', 'A/N', 'This field identifies the country\nwhere the Receiving Institution is\nlocated.'), ('80', 'Sharing Group', '30', '704-733', 'A/N', 'This field specifies the PIN Debit\nnetwork access priority.\nRefer to Network ID and Sharing\nGroup Codes list of codes.'), ('81', 'GIV', '1', '734', 'A/N', 'This field identifies the Gross\nInterchange Value and is set by\nVISA.\nIf the flag is @, the transaction\nhas financial impact and is\nincluded in the appropriate\nsettlement accumulation during\nprocessing of the request/\nresponse or advice/advice-\nresponse message pair.\nIf flag is blank, the transaction is\nineligible for settlement\nprocessing.'), ('82', 'Reimbursement\nAttribute', '1', '735', 'A/N/S', 'This field identifies a code that\nrepresents the applicable\ninterchange reimbursement fee for\na purchase transaction.'), ('83', 'Receiving\nInstitution ID\nCode', '11', '736-746', 'A/N', 'This field identifies a message\nrouting code that identifies the\ninstitution that should receive a\nrequest or advice.'), ('84', 'Network ID', '4', '747-750', 'N', 'For PIN Debit, this identifies the\ndebit network that processed the\ntransaction. This field may be\npopulated for other transaction\ntypes, such as Visa non-PIN debit\nauthorizations.\nNote: See Network ID and Sharing\nGroup Codes for a list of valid\nvalues.'), ('85', 'Transaction data', '12', '751-762', 'A/N', 'G\nThis field contains values\nextracted from the second\ngeneration request messages. The\nlayout varies depending on the\nFormat Identifier in the first\nposition of the field.\nen2 Position\nSGMF Position\nAPEX XML Position'), ('86', 'Transaction Fee\nAmount', '9', '763-771', 'A/N', 'This field identifies a destination\nassessed PIN POS and credit\ntransaction surcharge fee in the\ntransaction amount currency for\ninformation only.'), ('87', 'Prestigious\nProperty\nIndicator', '1', '772', 'A', 'This field identifies an indicator\nused by CPS Acquirers in the\nVISA USA Prestigious Lodging\nProgram to identify a property floor\nlimit.\nValid values:\nCode\nDefinition\nD\nPrestigious property\nwith US $500 limit\nB\nPrestigious property\nwith US $1000 limit\nS\nPrestigious property\nwith US $1500 limit'), ('88', 'Pre Auth Time\nLimit', '4', '773-776', 'A/N', 'This value indicates the period that\nfunds will be held for a pre-\nauthorization transaction before\nthe completion transaction is\nfinished. This field only applies to\npre-authorization and completion\ntransactions; otherwise, it will be\nomitted.'), ('89', 'Forwarding\nInstitution\nCountry Code', '3', '777-779', 'A/N', 'This field identifies the country of\nthe forwarding institution.'), ('90', 'Dial Pay\nAuthorization\nCall Type', '2', '780-781', 'A/N', 'This field specifies the type of Dial-\nPay authorization that was\nprocessed.\nTSYS Acquiring Solutions uses\nthis value to segregate and\naccumulate Dial-Pay\nauthorizations for merchant billing\npurposes.\nValid values:\nCode\nDescription\nBH\nBatch History\nBlank\nNot a Dial-Pay\nAuthorization\nBR\nBatch Review\nBT\nBatch Totals\nCR\nCredit\nDC\nDropped Call\nLT\nBatch Find\nIV\nIVR\nOF\nOffline\nOT\nOther\nRF\nReferral\nVC\nVoice\nVD\nVoid'), ('91', 'Digital Entity\nIdentifier', '5', '782-786', 'A/N', 'This value is a unique identifier\nassigned by Visa at the time of\nauthorization to identify a\ntransaction that originates from\nVisa Checkout.'), ('92', 'Reserved', '12', '787-798', 'HEX', 'Internal use only'), ('93', 'Reversal\nRequest Code', '2', '799-800', 'A/N', 'This value is a code that may be\npresent in the reversal request for\na Mastercard transaction to signify\nthe reason for a reversal.'), ('94', 'Additional POS\nInformation Text', '12', '801-812', 'A/N', "R\nThis value identifies the terminal's\ncapability to read account\nnumbers and expiration dates\nelectronically.\nefer to \nAdditional POS\nInformation Position Values for\nmore details."), ('95', 'Endpoint Code', '1', '813', 'A/N', 'The value of this field is privately\nused by TSYS Acquiring\nSolutions.\nValid values:\nEndpoint\nCode\nAmerican Express A\nDiscover\nD\nCiti Bank\nC\nMastercard\nM\nNot Routed\nNull\nStored Value\nS\nSystems\nFifth Third Bank\nF\nTSYS Issuing TS2\nT\nValueLink\nY\nVisa\nV'), ('96', 'Mapped Account\nExpiration Date', '4', '814-817', 'A/N', 'This value represents the\nexpiration date of the Mapped\nPaypass card.'), ('97', 'POS Data Code', '12', '818-829', 'A/N', 'S\n D\nThis field consists of 12 subfields\nthat indicate the condition or state\nof the terminal at the time of the\ntransaction. The fields come in two\ntypes, static or dynamic.\ntatic Fields:\nStatic fields have the same value\nfor every transaction. They do not\ntypically change once the software\nand hardware are considered\ntogether in the environment in\nwhich they are deployed.\nynamic Values:\nDynamic fields can change based\non the transaction scenario.\nRefer to Mastercard POS Data\nCode for a list of codes.\nRefer to Amex POS Data Code for\na list of codes.'), ('98', 'POS\nEnvironment\nIndicator', '1', '830', 'A/N', 'This Visa only field contains an\nindicator for the following types of\ntransactions:\nC - Credential on File\nI - Installment Payment\nR - Recurring Payment'), ('99', 'Reserved', '42', '831-872', 'A/N', 'Reserved'), ('100', 'Local\nTransaction Date', '4', '873-876', 'N', 'MMDD\nThis is the month and day the\ncardholder originated the\ntransaction. For recurring\npayments, the date is the\ncardholder requested payment\ndate.'), ('101', 'Local\nTransaction\nT\nime', '6', '877-882', 'N', 'This field identifies six-digits in the\nHHMMSS format indicating the\nexact time a transaction is\nperformed.'), ('102', 'Fee Program\nIndicator', '3', '883-885', 'A/N', 'This field identifies the fee program\nindicator; it is used in assessing\nthe fee amount applied to the\ntransaction.'), ('103', 'Visa DCC\nIndicator', '1', '886', 'A/N', 'Visa Dynamic Currency\nConversion Indicator\nPossible values:\n1 - DCC was performed\nSpace - DCC was not\nperformed'), ('104', 'Encryption\nIndicator', '1', '887', 'A/N', 'Encryption Indicator\nPossible values:\nV - Voltage encrypted\nP - P2PE encrypted\nN - NESA encrypted\nSpace - Not an encrypted\ntransaction'), ('105', 'TSYS Token\nIndicator', '1', '888', 'A/N', 'TSYS Token Indicator\nPossible values:\nY - Transaction used\nTokens\nN - Transaction did not use\nTokens'), ('106', 'Account Funding\nSource', '1', '889', 'A/N', 'Account Funding Source\nPossible values:\nC - Credit\nD - Debit\nH - Charge\nP - Prepaid\nR - Deferred Debit\nSpace - N/A'), ('107', 'Issuing BIN\nLook-Up', '1', '890', 'A/N', 'This field indicates an Issuing BIN\nlook up was performed to\ndetermine whether the transaction\nwas credit or debit.\nPossible values:\nY - Look-Up Performed\nN - No Look-Up'), ('108', 'Fallback\nIndicator', '1', '891', 'A/N', 'This field identifies that a\ntransaction initiated with a chip\ncard at a chip card capable\nterminal failed, resulting in a\nfallback to a mag-stripe entry\nmode.\nPossible values:\nT - Technical Fallback\nE - Empty Candidate List\nFallback\nSpace - No Fallback'))

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
		"terminalNumber": None,
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
		"iSORejectCode": None,
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
		"transactiondata": None,
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
        self.recordType, self.acquirerBIN, self.exitBIN, self.agent, self.chain, self.eConnectionsMerchantNumber, self.storeNumber, self.terminalNumber, self.cardAcceptorID, self.merchantName, self.cardAcceptorCity, self.cardAcceptorState, self.cardAcceptorCountryCode, self.countryCodePANExtended, self.nationalPOSGeographicData, self.mCCCode, self.merchantABANumber, self.cardAcceptorSettlementAgent, self.iSOSourceStationID, self.acquirerBusinessID, self.acquirerCountryCode, self.cardType, self.primaryAccountNumber, self.eXTPAN, self.accountID1, self.cardexpirationDate, self.issuingInstitutionStationID, self.issuingInstitutionIDCode, self.julianDay, self.transactionDateTime, self.settlementDate, self.loadDateTime, self.messageType, self.processingCode, self.accessMethod, self.aSCIIBillCode, self.transactionIdentifier, self.retrievalReferenceNumber, self.systemsTraceAuditNumber, self.authorizedAmount, self.cardholderBillingAmount, self.approvalCode, self.authorizationResponse, self.internalErrorCode, self.iSORejectCode, self.cVV2CVC2CIDResponseType, self.cVV2CVC2CIDPresenceIndicator, self.messageReasonCode, self.additionalResponseData, self.requestACI, self.returnACI, self.validationCode, self.productTypeIdentification, self.transactionSourceFlag, self.vARTrackID, self.vendorID, self.pOSEntryMode, self.iSAChargeIndicator, self.aMEXCardholderVerificationResults, self.pOSConditionCode, self.additionalDataPrivateRequest, self.additionalDataPrivateResponse, self.supportingInformation, self.duration, self.marketSpecificDataIndicator, self.cashBackAmount, self.cardholderBillingConversionRate, self.cardholderBillingCurrencyCode, self.requestAdditionalAmount, self.mastercardAssignedID, self.mastercardIIASIndicator, self.responseAdditionalAmount, self.replacementAmounts, self.xID, self.uCAFCollectionIndicator, self.transactionCurrencyCode, self.gatewayCurrencyCode, self.gatewayCountryCode, self.receivingInstitutionCountryCode, self.sharingGroup, self.gIV, self.reimbursementAttribute, self.receivingInstitutionIDCode, self.networkID, self.transactiondata, self.transactionFeeAmount, self.prestigiousPropertyIndicator, self.preAuthTimeLimit, self.forwardingInstitutionCountryCode, self.dialPayAuthorizationCallType, self.digitalEntityIdentifier, self.reserved91, self.reversalRequestCode, self.additionalPOSInformationText, self.endpointCode, self.mappedAccountExpirationDate, self.pOSDataCode, self.pOSEnvironmentIndicator, self.reserved98, self.localTransactionDate, self.localTransactionTime, self.feeProgramIndicator, self.visaDCCIndicator, self.encryptionIndicator, self.tSYSTokenIndicator, self.accountFundingSource, self.issuingBINLookUp, self.fallbackIndicator = (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
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
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates that this record\nis the Transaction Detail\nExtension Record.\nValue = TD11'), ('2', 'Extension Record', '8', '5-12', 'A/N', 'This field indicates the record that\nfollows the TD11 Record.\nPossible values:\nSpace - no record follows\nEX01 - Discover/PayPal\nextension record follows\nEX02 - Mastercard\nextension record follows\nEX03 - Additional detail\ndata extension record\nfollows\nEX04 - Merchant Data\nextension record follows'), ('3', 'Merchant\nConsent Indicator', '1', '13', 'A/N', 'This field indicates the value of the\nmerchant consent indicator at the\ntime a transaction is processed.It\nis specific to merchants\nprocessing transactions in\nCanada, and indicates if the\nmerchant has or has not\nconsented to the Canadian Code\nof Conduct. Merchants must\ndeclare a value for both card\npresent and card not present\ntransactions.\nPossible values:\nCard Present\n1 - Merchant consented\n2 - Merchant did not\nconsent\nCard Not Present\n3 - Merchant consented\n4 - Merchant did not\nconsent'), ('4', 'Goods Sold\nProduct Code', '4', '14-17', 'A/N', 'This field is used by Card Present\nmerchants to provide an Amex\ndefined Goods Sold value.\nValid values:\n1000 - Gift Card\nSpace fill'), ('5', 'Card Brand\nToken Assurance\nLevel', '2', '18-19', 'A/N', 'Defined by the token service\nprovider, this Visa, Mastercard or\nDiscover value indicates the\nassigned confidence level of the\ntoken-to-PAN/cardholder binding.'), ('6', 'Account Range\nStatus', '1', '20', 'A/N', 'This Visa value is used by the\nacquirer or processor; it indicates\nthe status of the account.\nValid values:\nSpace\nR - Regulated\nN - Non-Regulated'), ('7', 'Seller ID', '20', '21-40', 'A/N', 'This American Express value is\nthe identifier assigned by the\nPayment Service\nProvider/Aggregator or OptBlue\nparticipant.'), ('8', 'Card Brand\nToken Requestor\nID', '11', '41-51', 'A/N', 'This field contains eleven digits\nthat uniquely identify the pairing of\nthe token requestor with the token\ndomain. It is assigned by the\ntoken service provider and is\nunique within the token vault.'), ('9', 'Industry SE\nNumber', '10', '52-61', 'A/N', 'This American Express value\nrepresents the identifier of the\nService Establishment/Merchant.'), ('10', 'Seller DBA', '30', '62-91', 'A/N', 'This is the merchant�s �Doing\nBusiness As� name. It is the\ncommon name of the business.'), ('11', 'Payment\nFacilitator\nIdentifier', '11', '92-102', 'A/N', 'Mastercard assigns this value\nduring registration via Mastercard\nConnect for the Service Provider\ndesignated as a �Payment\nFacilitator�.'), ('12', 'ISO Identifier', '11', '103-113', 'A/N', 'Mastercard assigns this value\nduring registration via Mastercard\nConnect for the Service Provider\ndesignated as an �Independent\nSales Organization�.'), ('13', 'Sub-Merchant\nIdentifier', '15', '114-128', 'A/N', 'The Payment Facilitator or the\nAcquirer assigns this Mastercard\nvalue.'), ('14', 'Expanded Billing\nClass', '2', '129-130', 'A/N', 'This field indicates the ingress\nconnectivity method between a\nclient and its respective\ntransaction processing gateway.\nThis field is used for\nmerchant/service specific billing.\nPossible value:\nV1-V9 [Port Options 1-9]'), ('15', 'Issuer Country\nCode', '3', '131-133', 'A/N', 'This field is populated for Visa and\nMastercard.'), ('16', 'Service Code', '3', '134-136', 'N', 'This field is a service code from\ntrack data.'), ('17', 'Payment\nAccount\nReference (PAR)', '35', '137-171', 'AN', "PAR is a value assigned by the\nBIN Controller, which is defined as\neither an issuer or card brand.\nThis field is directly associated\nwith the cardholder's account."), ('18', 'Business\nApplication\nIdentifier', '2', '172-173', 'A/N', 'Business Application Identifier\nThis field identifies industry-\nspecific business practices\npertaining to Account Funding\nTransactions (AFT).\nValid Value:\nWT � Wallet Transfer'), ('19', 'Endpoint POS\nData Code', '13', '174-186', 'A/N', 'This field contains data indicating\nthe condition or state of the\nterminal at the time the\nauthorization request is sent to\nthe various endpoints. Each\nendpoint has different subfields.\nThe fields come in two types,\nstatic or dynamic.\nStatic Fields:\nStatic fields have the same value\nfor every transaction. They do not\ntypically change once the\nsoftware and hardware are\nconsidered together in the\nenvironment in which they are\ndeployed.\nDynamic Values:\nDynamic fields can change based\non the transaction scenario.\nRefer to Amex POS Data Code for\na list of codes.\nRefer to Discover/PayPal POS\nData Code for a list of codes.\nRefer to Mastercard POS Data\nCode for a list of codes.'), ('20', 'Reserved', '134', '187-320', 'A/N', 'Reserved'), ('21', 'TSYS', '6', '321-326', 'A/N', 'TSYS Internal Use Only'))

    ROW = lambda row, RECORD=RECORD: RECORD[row]
    COLUMN = lambda column, RECORD=RECORD: [data[column] for data in RECORD]
    AT = lambda row,column, RECORD=RECORD: RECORD[row][column]

    restrictions = {
		"recordType": None,
		"extensionRecord": None,
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

    LENGTH = 400

    def __init__(self,f):
        self.recordType, self.extensionRecord, self.merchantConsentIndicator, self.goodsSoldProductCode, self.cardBrandTokenAssuranceLevel, self.accountRangeStatus, self.sellerID, self.cardBrandTokenRequestorID, self.industrySENumber, self.sellerDBA, self.paymentFacilitatorIdentifier, self.iSOIdentifier, self.subMerchantIdentifier, self.expandedBillingClass, self.issuerCountryCode, self.serviceCode, self.paymentAccountReference, self.businessApplicationIdentifier, self.endpointPOSDataCode, self.reserved19, self.tSYS = (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
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
    RECORD = (('1', 'Record Type', '4', '1-4', 'A/N', 'This field indicates that this record is the\nTransmission Trailer.\nValue = TT01'), ('2', 'Version Number', '5', '5-9', 'A/N', 'This field identifies the Report Version\nNumber. Example: 01.00'), ('3', 'Destination ID', '30', '10-39', 'A/N', 'This field identifies the destination client ID\nfrom the report registration.'), ('4', 'File type', '10', '40-49', 'A/N', 'This field identifies the file type being sent.\nValue = ADF'), ('5', 'File Frequency', '1', '50', 'A/N', 'This field identifies the frequency in which the\nfile is sent.\nExample:\nB = Bi-hourly\nD = Daily\nW = Weekly'), ('6', 'Processing Year', '4', '51-54', 'N', 'This field identifies the year the file was\ncreated.\nExample: YYYY'), ('7', 'Processing Month', '2', '55-56', 'N', 'This field identifies the month the file was\ncreated.\nExample: MM - month number, from 01 to 12'), ('8', 'Processing Week', '1', '57', 'N', 'This field identifies the week the file was\ncreated. The valid value for a week\ncorresponds to the specific week within a\nmonth, and can be a 1, 2, 3, or 4. This field\nwill only be used if it is a weekly file.\nValue\nDefinition\n1\nWeek 1 (day 1 - 7)\n2\nWeek 2 (day 8 - 15)\n3\nWeek 3 (day 16 - 22)\n4\nWeek 4 (day 23 - end of month)\nIf it is not a weekly file, then this field will be\nblank.'), ('9', 'Processing Day', '2', '58-59', 'N', 'Reserved for TSYS Acquiring Solutions use\nonly'), ('10', 'Processing End\nHour', '2', '60-61', 'N', 'This field identifies the hour the file was\ncreated if the file is bi-hourly. If it is not a bi-\nhourly file, then this field will be blank.\nExample:\nHH, (using a 24-hour clock). Based on\nGreenwich Mean Time (GMT).'), ('11', 'File Reference ID', '20', '62-81', 'A/N', 'Reserved for TSYS Acquiring Solutions use\nonly'), ('12', 'File Total BIN Count', '8', '82-89', 'N', 'This field identifies the total number of unique\nBIN(s) located within the file.'), ('13', 'File Total Report\nCount', '8', '90-97', 'N', 'This field identifies the total number of unique\nReport(s) located within the file.'), ('14', 'File Total\nTransaction Count', '12', '98-109', 'N', 'This field identifies the total number of\ntransactions located within the transmission.'))

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
		"fileTotalBINCount": None,
		"fileTotalReportCount": None,
		"fileTotalTransactionCount": None
                }

    LENGTH = 900

    def __init__(self,f):
        self.recordType, self.versionNumber, self.destinationID, self.filetype, self.fileFrequency, self.processingYear, self.processingMonth, self.processingWeek, self.processingDay, self.processingEndHour, self.fileReferenceID, self.fileTotalBINCount, self.fileTotalReportCount, self.fileTotalTransactionCount = (None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        self.data = f.read(TransmissionTrailerRecord.LENGTH)
        super(TransmissionTrailerRecord, self).__init__()
        

class Records (metaclass=ADFMeta):
    DATA = (('Transmission Header Record', '900', 'TH01', TransmissionHeaderRecord), ('BIN Header Record', '900', 'BH01', BINHeaderRecord), ('Report Header Record', '900', 'RH01', ReportHeader), ('Transaction Detail Record', '900', 'TD01', TransactionDetailRecord), ('Transaction Detail Extension Record', '200', 'TD11', TransactionDetailExtensionRecord), ('Discover/ PayPal Extension Record', '160', 'EX01', DiscoverPayPalExtensionRecord), ('Mastercard Extension Record', '160', 'EX02', MastercardExtensionRecord), ('Merchant Data Extension Record', '160', 'EX04', MerchantDataExtensionRecord), ('Additional Detail Data Extension Record', '320', 'EX03', AdditionalDetailDataExtensionRecord), ('Report Header Record', '81', 'RH02', ReportHeaderRecord), ('Host Capture Adjustment Transaction Detail Record', '120', 'TD02', HostCaptureAdjustmentTransactionDetailRecord), ('Host Capture Batch Inquiry Transaction Detail Record', '100', 'TD03', HostCaptureBatchInquiryTransactionDetailRecord), ('Report Trailer Record', '93', 'RT02', ReportTrailerRecord), ('Report Trailer Record', '900', 'RT01', ReportTrailer), ('BIN Trailer Record', '900', 'BT01', BINTrailerRecord), ('Transmission Trailer Record', '900', 'TT01', TransmissionTrailerRecord))
    LUT = {'TH01': DATA[0], 'BH01': DATA[1], 'RH01': DATA[2], 'TD01': DATA[3], 'TD11': DATA[4], 'EX01': DATA[5], 'EX02': DATA[6], 'EX04': DATA[7], 'EX03': DATA[8], 'RH02': DATA[9], 'TD02': DATA[10], 'TD03': DATA[11], 'RT02': DATA[12], 'RT01': DATA[13], 'BT01': DATA[14], 'TT01': DATA[15]}

    ROW = lambda row, DATA=DATA: DATA[row]
    COLUMN = lambda column, DATA=DATA: [data[column] for data in DATA]
    AT = lambda row,column, DATA=DATA: DATA[row][column]

    def __init__(self,paramTuple):
        self.transmissionTrailerRecord, self.totalBytes, self.recordCode = paramTuple