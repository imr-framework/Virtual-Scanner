# Copyright of the Board of Trustees of Columbia University in the City of New York

import virtualscanner.server.ana.T1_mapping as dicom2mapT1
import virtualscanner.server.ana.T2_mapping as dicom2mapT2
from virtualscanner.utils import constants

SERVER_T1_INPUT_PATH = constants.SERVER_ANALYZE_PATH / 'inputs' / 'T1_orig_data'
SERVER_T2_INPUT_PATH = constants.SERVER_ANALYZE_PATH / 'inputs' / 'T2_orig_data'

'''
TI = [0.021, 0.1, 0.2, 0.4, 0.8, 1.6, 3.2]
TR = [10, 10, 10, 10, 10, 10, 10]
TE = [0.012, 0.022, 0.042, 0.062, 0.102, 0.152, 0.202]
'''
if __name__ == '__main__':
    T1_map = dicom2mapT1.main(
        dicom_file_path=SERVER_T1_INPUT_PATH,
        TR='10, 10, 10, 10, 10, 10, 10',
        TI='0.021, 0.1, 0.2, 0.4, 0.8, 1.6, 3.2',
        TE='0.012, 0.012, 0.012, 0.012, 0.012, 0.012, 0.012',
        pat_id='9306'
    )

if __name__ == '__main__':
    T2_map = dicom2mapT2.main(
        dicom_file_path=SERVER_T2_INPUT_PATH,
        TR='10, 10, 10, 10, 10, 10, 10',
        TE='0.012, 0.022, 0.042, 0.062, 0.102, 0.152, 0.202',
        pat_id='9306'
    )
