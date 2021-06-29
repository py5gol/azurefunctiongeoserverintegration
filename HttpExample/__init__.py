import json
import logging
import sys
import requests
import json
from urllib.parse import urljoin
from geoserver.catalog import Catalog

import azure.functions as func


def main(myblob: func.InputStream):
    logging.info('Python Blob trigger function processed %s', myblob.name)

    api_entry = 'http://20.90.96.9:8080/geoserver/rest/'
    credential = ('admin', 'geoserver')

    cat = Catalog('http://20.90.96.9:8080/geoserver/rest/', 'admin', 'geoserver')
    # resource = 'workspaces'
    # payload = {'workspace': {'name':'acme2'}}
    # headers = {'content-type': 'application/json'}

    # request_url = urljoin(api_entry, resource)

    # r = requests.post(
    #     request_url,
    #     data=json.dumps(payload),
    #     headers=headers,
    #     auth=credential
    # )

    # r.raise_for_status()

    # coveragestore_name = myblob.name.split("/")[1].split(".")[0]
    # resource = 'workspaces/cite/coveragestores'
    # headers = {'content-type': 'application/xml'}
    # request_url = urljoin(api_entry, resource)
    # body = "<coverageStore><name>{}</name><workspace>cite</workspace><enabled>true</enabled></coverageStore>".format(coveragestore_name)

    # r = requests.post(
    #     request_url,
    #     data=body,
    #     headers=headers,
    #     auth=credential
    # )

    # curl -v -u admin:geoserver -XPUT -H "Content-type: text/plain"
    #    -d "file:///path_to_directory/int_dec.tif"
    #    http://localhost:8080/geoserver/rest/workspaces/restProba/coveragestores/int_dec/external.geotiff

    # coveragestore_name = myblob.name.split("/")[1].split(".")[0]
    # body = myblob.read()
    # resource = 'workspaces/cite/coveragestores/{}/external.geotiff'.format(coveragestore_name)
    # headers = {'content-type': 'application/octet-stream'}
    # request_url = urljoin(api_entry, resource)
    # body = myblob.read()

    # r = requests.put(
    #     request_url,
    #     data=body,
    #     headers=headers,
    #     auth=credential
    # )

    logging.info("name: {}".format(myblob.name))
    logging.info("length: {}".format(myblob.length))
    logging.info("--")
    logging.info(myblob.read())
    logging.info("--")
    # logging.info("length: {}".format(myblob.length))

    ft = cat.create_coveragestore(myblob.name, workspace='cite', type='GeoTIFF', create_layer=True, upload_data=True, overwrite=True, path=myblob.read())

    # r = requests.put(
    #     request_url,
    #     data=myblob,
    #     headers=headers,
    #     auth=credential
    # )

    # logging.info(r)

    # with open(file_name, 'rb') as f:
    #     r = requests.put(
    #         request_url,
    #         data=f,
    #         headers=headers,
    #         auth=credential
    #     )

    # try:
    #         geo = Geoserver('http://20.90.96.9:8080/geoserver', username='admin', password='geoserver')
    #         logging.info('Conectado com o geoserver')
    # except Exception as err:
    #         logging.info('Erro na conexao com o geoserver')
    #         logging.error("{}".format(err))

