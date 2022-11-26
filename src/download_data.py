# Author: DSCI_522_Group_5
# Date: 2022-11-18
# Original code source: download_data.py used in DSCI 522 Lecture 2 (with modifications)

"""Downloads data (html table) from the web, convert and save it as a csv to a local filepath.

Usage: download_data.py --url=<url> --out_file=<out_file> 
 
Options:
--url=<url>             URL from where to download the data (must be in html table)
--out_file=<out_file>   Path (including filename) of where to locally write the file

Note:
1. Command to install the required package lxml: conda install -c conda-forge lxml
2. A sample HTML website that would work: http://flavorsofcacao.com/database_w_REF.html
"""

import os
import pandas as pd
from docopt import docopt

opt = docopt(__doc__)

def main(url, out_file):
    '''
    Get the data through the url, read it and output a csv file 
    
    Parameters
    ----------
    url : str
        URL from where to download the data
    out_file : path
        The output file path
    '''
    data = pd.read_html(url)[0]
    try:
        data.to_csv(out_file, index=False)
    except:
        os.makedirs(os.path.dirname(out_file))
        data.to_csv(out_file, index=False)


if __name__ == "__main__":
    main(opt["--url"], opt["--out_file"])
