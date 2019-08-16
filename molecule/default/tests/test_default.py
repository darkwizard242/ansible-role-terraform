import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

TERRAFORM_BINARY_PATH = '/usr/local/bin/terraform'


def test_terraform_binary_exists(host):
    host.file('TERRAFORM_BINARY_PATH').exists


def test_terraform_binary_file(host):
    host.file('TERRAFORM_BINARY_PATH').is_file


def test_terraform_binary_run(host):
    host.check_output('whereis terraform') == TERRAFORM_BINARY_PATH
