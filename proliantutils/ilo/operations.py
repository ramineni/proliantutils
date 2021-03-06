# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from proliantutils import exception

ERRMSG = "The specified operation is not supported on current platform."


class IloOperations:
    """iLO class for performing iLO Operations.

    This class provides an OO interface for retrieving information
    and managing iLO. It implements the same interface in
    python as described in HP iLO 4 Scripting and Command Line Guide.

    """
    def get_all_licenses(self):
        """Retrieve license type, key, installation date, etc."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def get_product_name(self):
        """Get the model name of the queried server."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def get_host_power_status(self):
        """Request the power state of the server."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def get_one_time_boot(self):
        """Retrieves the current setting for the one time boot."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def get_vm_status(self, device='FLOPPY'):
        """Returns the virtual media drive status like url, is connected, etc.

        """
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def reset_server(self):
        """Resets the server."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def press_pwr_btn(self):
        """Simulates a physical press of the server power button."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def hold_pwr_btn(self):
        """Simulate a physical press and hold of the server power button."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def set_host_power(self, power):
        """Toggle the power button of server.

        :param power: 'ON' or 'OFF'
        """
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def set_one_time_boot(self, value):
        """Configures a single boot from a specific device."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def insert_virtual_media(self, url, device='FLOPPY'):
        """Notifies iLO of the location of a virtual media diskette image."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def eject_virtual_media(self, device='FLOPPY'):
        """Ejects the Virtual Media image if one is inserted."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def set_vm_status(self, device='FLOPPY',
                      boot_option='BOOT_ONCE', write_protect='YES'):
        """Sets the Virtual Media drive status and allows the

        boot options for booting from the virtual media.
        """
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def get_current_boot_mode(self):
        """Retrieves the current boot mode settings."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def get_pending_boot_mode(self):
        """Retrieves the pending boot mode settings."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def get_supported_boot_mode(self):
        """Retrieves the supported boot mode."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def set_pending_boot_mode(self, value):
        """Sets the boot mode of the system for next boot."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def get_persistent_boot(self):
        """Retrieves the boot order of the host."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def get_persistent_boot_device(self):
        """Get the current persistent boot device set for the host."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def set_persistent_boot(self, values=[]):
        """Configures to boot from a specific device."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def update_persistent_boot(self, device_type=[]):
        """Updates persistent boot based on the boot mode."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def get_secure_boot_state(self):
        """Get the status if secure boot is enabled or not."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def set_secure_boot_state(self, secure_boot_enable):
        """Enable/Disable secure boot on the server."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def reset_secure_boot_keys(self):
        """Reset secure boot keys to manufacturing defaults."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def clear_secure_boot_keys(self):
        """Reset all keys."""
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def reset_ilo_credential(self, password):
        """Resets the iLO password.

        :param password: The password to be set.
        :raises: IloError, if account not found or on an error from iLO.
        :raises: IloCommandNotSupportedError, if the command is not supported
             on the server.
        """
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def reset_ilo(self):
        """Resets the iLO.

        :raises: IloError, on an error from iLO.
        :raises: IloCommandNotSupportedError, if the command is not supported
                 on the server.
        """
        raise exception.IloCommandNotSupportedError(ERRMSG)

    def reset_bios_to_default(self):
        """Resets the BIOS settings to default values.

        :raises: IloError, on an error from iLO.
        :raises: IloCommandNotSupportedError, if the command is not supported
                 on the server.
        """
        raise exception.IloCommandNotSupportedError(ERRMSG)
