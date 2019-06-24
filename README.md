sys_fs.varnish
==============

This role installs and configures Varnish from the official repository on
Debian and Ubuntu.

Requirements
------------

This role requires at least Ansible 2.6.

Role Variables
--------------

    varnish_version: 6.2

The version of Varnish to install.

    varnish_listen_address: ':80'

The address that Varnish will listen on for frontend connections.

    varnish_admin_listen_address: 'localhost:6082'

The address that Varnish's admin console will listen on.

    varnish_storage_backend: 'malloc,256m'

The storage backend to use.

	# varnish_vcl_template: example.vcl.j2

Custom VCL template to use. If left unset the default VCL will be deployed. The
template should be located in a subdirectory called `templates`, located within
your playbook root.

Example Playbook
----------------

    - hosts: varnish
	  roles:
        - sys_fs.varnish

License
-------

MIT
