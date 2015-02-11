import os
import re
import urlparse
import tempfile
import requests
import gzip
import shutil
import six
import tarfile

from ironic_python_agent import errors
from ironic_python_agent import hardware
from ironic_python_agent import netutils
from ironic_python_agent.openstack.common import log
from ironic_python_agent import utils
from django.core.files.locks import fd

LOG = log.getLogger()
FW_DIR = '/tmp/fw-ilo/'
IMAGE_CHUNK_SIZE = 1024 * 1024

class HPProliantHardwareManager(hardware.GenericHardwareManager):
    HARDWARE_MANAGER_VERSION = "3"

    def evaluate_hardware_support(cls):
        return hardware.HardwareSupport.SERVICE_PROVIDER
    
    def erase_block_device(self, block_device):
        npass = 3
        cmd = ['shred', '--force', '--zero', '--verbose',
               '--iterations', npass, block_device.name]

        utils.execute(*cmd, check_exit_code=[0])

    def erase_devices(self):
        block_devices = self.list_block_devices()
        for block_device in block_devices:
            self.erase_block_device(block_device)
    
    def upgrade_firmware(self, node):
        driver_info = node.get('driver_info', {})
        location = driver_info.get('ilo_firmware_location_url')
        abs_path = None
        
        # Code should be moved to ironic to generate temp url
        url = urlparse.urlparse(location)
        if url.scheme not in ('http', 'https'):
            # Raise Error here
            pass
        file = self._download_url(location)
        if tarfile.is_tarfile(file):
            fwfiles = self._unpack(file)
        
        else:
            # Raise exception here
            raise 
        
        for fd in fwfiles:
            # TODO:Check permissions
            # Check the extension
            print fd.name
            extension = os.path.splitext(filename)[1][1:]
            print extension
            
            if extension == 'scexe':
                # execute and get the return value
                abs_path = os.path.join(FW_DIR, fd.name)
                print abs_path
                cmd = [fd.name, '-s']
                utils.execute(*cmd, check_exit_code=[0])
                print " right"
            else:
                msg = "Unsupported extension"
                continue            
            
            
            
        
        
        # Assuming location is http url of .tar/.gz file
        #self._download_file(FW_DIR)

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
    def _unpack(self, file):
        print file
        tar_file = tarfile.open(file, 'r')
        tar_objects = []
        
        for item in tar_file:
            tar_file.extract(item, FW_DIR)
            if item.isfile():
                tar_objects.append(item)
            
        print tar_objects
        return tar_objects
            
    def _download_url(self, url):
        resp = None
        err_msg = ("Failed to download image from %s", url)
        data = None
#         LOG.info("Attempting to download image from {0}".format(url))
        try:
            data = requests.get(url).content
        except Exception as e:
            print e
            raise errors.ImageDownloadError(err_msg)
        
        if data is not None:
            print "data not NOne"
        
        data = six.StringIO(data)
        fw_file = tempfile.NamedTemporaryFile(delete=False,dir=FW_DIR,
                                              prefix='firmware')
        
        with gzip.GzipFile('firmware', 'rb', fileobj=data) as gunzipped:
            try:
                shutil.copyfileobj(gunzipped, fw_file)
            except Exception as e:
                print e
                # Delete the created file
                # utils.unlink_without_raise(configdrive_file.name)
                pass
        
            finally:
                fw_file.close()
        
        print fw_file.name
        return fw_file.name