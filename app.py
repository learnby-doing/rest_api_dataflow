try:
    import argparse

    parser = argparse.ArgumentParser()
    # Runtime arguments for Datflow API
    parser.add_argument('--input',
                        dest='input',
                        required=True,
                        help="Inputs files to be processed!")

    print(parser.parse_known_args())

except:
    import os
    os.system("""
              
              """)