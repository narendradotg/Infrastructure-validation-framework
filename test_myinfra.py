#! /usr/bin/python
import pytest
import testinfra


@pytest.mark.infra
def test_os_release(host):
    """
    Usage: Validate hosts file exist
    """
    hosts_info_file = "/etc/hosts"
    assert host.file(hosts_info_file)


@pytest.mark.infra
@pytest.mark.parametrize("service", [("nginx")])
def test_servicestate(host, service):
    """
    Usage: Validate service status.
    """
    assert host.service(service).is_running
    assert host.service(service).is_enabled
