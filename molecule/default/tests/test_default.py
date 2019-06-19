import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    pkg = host.package('varnish')
    assert pkg.is_installed


def test_service(host):
    service = host.service('varnish')

    assert service.is_running
    assert service.is_enabled


def test_secret(host):
    secret = host.file('/etc/varnish/secret')

    assert secret.exists
    assert secret.mode == 0o400
    assert secret.user == 'root'
    assert secret.group == 'root'
