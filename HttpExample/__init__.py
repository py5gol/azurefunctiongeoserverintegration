import logging
from geoserver.catalog import Catalog

import azure.functions as func


def main(myblob: func.InputStream):
    logging.info('Python Blob trigger function processed %s', myblob.name)

    cat = Catalog('http://20.90.96.9:8080/geoserver/rest/', 'admin', 'geoserver')

    logging.info("name: {}".format(myblob.name))
    logging.info("length: {}".format(myblob.length))

    cat.create_coveragestore(myblob.name, workspace='cite', type='GeoTIFF', create_layer=True, upload_data=True, overwrite=True, path=myblob.read())
