NegativeAmounts = {'}': 0, 'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9}
DataTypes = {'A': r'[a-zA-Z]+', 'AN': r'[a-zA-Z0-9 ]+', 'S': r' +', 'N': '\d+', 'PN': r'.{2}'} #NOTE: TSYS may use more than 2 bytes for PN...
UserAbbreviations = {'All': 'All associations and TSYS Acquiring Solutions', 'X': 'American Express®', 'CAPN': 'American Express Card Acceptance Processing Network®', 'D': 'Diners Club®', 'S': 'Discover®', 'E': 'Europay®', 'JCB': 'Japanese Credit Bureau®', 'M': 'MasterCard®', 'P': 'Private label', 'V': 'Visa®', 'V-UK': 'Visa United Kingdom®', 'V-EU': 'Visa European Union®', 'TSYS Acquiring Solutions': 'TSYS Acquiring Solutions'}
NetworkIDs = {'XL': 'Accel®', 'AF': 'Armed Forces Financial Network (AFFN)', 'AL': 'Alert®', 'AV': 'Avail®', 'BM': 'Bankmate®', 'CA': 'Cactus®', 'CS': 'Cash Station®', 'CU': 'Credit Union 24 (CU24)', 'EB': 'EBT® (Electronic Benefits Transfer)', 'EV': 'Evertec', 'EH': 'The Exchange®', 'DB': 'Generic debit', 'GF': 'Gulfnet®', 'HO': 'Honor®', 'IT': 'Instant Teller®', 'IL': 'Interlink®', 'JE': 'Jeanie®', 'MA': 'Mac®', 'ME': 'Maestro®', 'ML': 'Magicline®', 'MS': 'Money Station®', 'MO': 'Most®', 'IM': 'Mpact®', 'NY': 'NYCE®', 'PL': 'Pulse®', 'QU': 'Quest®', 'S': 'Shaam®', 'ST': 'Star (Explore)®', 'TY': 'Tyme®', 'VI': 'Visa®', 'C2': 'Visa Checkcard II®', 'YN': 'Yankee 24®'}
ExtensionRecordIndicator = {'AIRL1': 'Airline/Passenger Transport 1',
							'AMEXR': 'Restaurant',
							'CARNT': 'Car Rental',
							'CHECK': 'Electronic Check',
							'DIRCT': 'Direct Marketing',
							'EINTR': 'Electronic Invoice Transaction Data',
							'EINPR': 'Electronic Invoice Party Information',
							'ENT1*': 'Entertainment/Ticketing',
							'EXT**': 'General',
							'FLEET': 'Fleet Service 1',
							'INS1*': 'Insurance',
							'LODGE': 'Lodging',
							'MERCH': 'Merchant Description',
							'PURC1': 'Purchasing Card1',
							'RETAL': 'Retail',
							'SHIP1': 'Shipping Service 1',
							'TEMP1': 'Temporary Help Services 1',
							'TBSUM': 'Telephon Billing Summary',
							'TBDET': 'Telephone Billing Detail'}

__all__ = [NegativeAmounts, DataTypes, UserAbbreviations, NetworkIDs, ExtensionRecordIndicator]