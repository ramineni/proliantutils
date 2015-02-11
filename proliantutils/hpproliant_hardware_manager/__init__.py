import os
import re

from ironic_python_agent.common import metrics
from ironic_python_agent import errors
from ironic_python_agent import hardware
from ironic_python_agent import netutils
from ironic_python_agent.openstack.common import log
from ironic_python_agent import utils

LOG = log.getLogger()
FW_DIR = '/tmp/fw-ilo/'

class HPProliantHardwareManager(hardware.GenericHardwareManager):
    HARDWARE_MANAGER_VERSION = "3"

    def evaluate_hardware_support(cls):
        return hardware.HardwareSupport.SERVICE_PROVIDER
    
    def erase_block_device(self, block_device):
        npass = 2  
        cmd = ['shred', '--force', '--zero', '--verbose',
               '--iterations', npass, block_device.name]

        utils.execute(*cmd, check_exit_code=[0])

    def erase_devices(self):
        block_devices = self.list_block_devices()
        for block_device in block_devices:
            self.erase_block_device(block_device)

#     def _request_url(image_info, url):
#         resp = requests.get(url, stream=True)
#         if resp.status_code != 200:
#             raise errors.ImageDownloadError(image_info['id'])
#         return resp
# 
#     def upgrade_firmware(self, node):
#         LOG.info('Update BIOS called with %s' % driver_info)
#         driver_info = node.get('driver_info', {})
#         # Assuming temp url is received from ironic to download the
#         # firmware images.
#         url = driver_info['swift_temp_url']
#         try:
#             LOG.info("Attempting to download image from {0}".format(url))
#             
#         except errors.ImageDownloadError:
#             failtime = time.time() - starttime
#             log_msg = "Image download failed. URL: {0}; time: {1} seconds"
#             LOG.warning(log_msg.format(url, failtime))
#             continue
#         
#         hpsum_cmd = ['hpsum', '--s', '--romonly', '--use_location', FW_DIR]
# 
#         utils.execute(cmd, check_exit_code=[0])
#         return True
#     
#     def _download_firmware_images(self, urls):
#         resp = None
#         for url in image_info['urls']:
#             try:
#                 LOG.info("Attempting to download image from {0}".format(url))
#                 resp = requests.get(url, stream=True)
#                 if resp.status_code != 200:
#                     raise errors.ImageDownloadError(image_info['id'])
#             except errors.ImageDownloadError:
#                 log_msg = "Image download failed. URL: {0}; time: {1} seconds"
#                 continue
#        
#             if resp is None:
#                 raise errors.ImageDownloadError(image_info['id'])
#     
#             image_location = FW_DIR + filename
#             with open(image_location, 'wb') as f:
#                 try:
#                     for chunk in resp.iter_content(IMAGE_CHUNK_SIZE):
#                         f.write(chunk)
#                 except Exception:
#                     raise errors.ImageDownloadError(image_info['id'])


