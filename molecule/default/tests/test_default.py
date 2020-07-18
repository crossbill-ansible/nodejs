import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_node_is_installed(host):
    node = host.file("/opt/software/nodejs/current")
    assert node.is_symlink
