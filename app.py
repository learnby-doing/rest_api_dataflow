try:
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('--input',
                        dest='input',
                        required=True,
                        help="Inputs files to be processed!")

    print(parser.parse_known_args())

except:
    import os
    os.system("""
              
              """)