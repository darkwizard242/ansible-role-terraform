import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE_BINARY = '/usr/local/bin/terraform'


def test_terraform_binary_exists(host):
    """
    Tests if terraform binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_terraform_binary_file(host):
    """
    Tests if terraform binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_terraform_binary_which(host):
    """
    Tests the output to confirm terraform's binary location.
    """
    assert host.check_output('which terraform') == PACKAGE_BINARY
