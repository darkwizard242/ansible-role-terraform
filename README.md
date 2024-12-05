[![build-test](https://github.com/darkwizard242/ansible-role-terraform/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-terraform/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-terraform/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-terraform/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/terraform) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-terraform&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-terraform) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-terraform&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-terraform) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-terraform&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-terraform) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-terraform?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-terraform?color=orange&style=flat-square)

# Ansible Role: Terraform

Role to install (_by default_) [terraform](https://www.terraform.io/) package on **Debian/Ubuntu** and **EL** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
terraform_app: terraform
terraform_version: 1.10.1
terraform_os: "{{ ansible_system | lower }}"
terraform_architecture_map:
  amd64: amd64
  arm: arm64
  x86_64: amd64
  armv6l: armv6
  armv7l: armv7
  aarch64: arm64
  32-bit: "386"
  64-bit: amd64
terraform_dl_url: https://releases.hashicorp.com
terraform_dl_loc: /tmp
terraform_bin_path: /usr/local/bin
terraform_file_owner: root
terraform_file_group: root
terraform_file_mode: '0755'
```

### Variables table:

Variable                   | Description
-------------------------- | -----------------------------------------------------------------------------------------------------------------------------------------------------------
terraform_app              | Defines the app to install i.e. **terraform**
terraform_version          | Defined to dynamically fetch the desired version to install. Defaults to: **1.10.1**
terraform_os               | Defines os type. Used for obtaining the correct type of binaries based on OS type.
terraform_architecture_map | Defines os architecture. Used to set the correct type of binaries based on OS System Architecture.
terraform_dl_url           | Defines URL to download the terraform binary from.
terraform_dl_loc           | Defined to dynamically set where to place the binary archive for `terraform` temporarily. Defaults to: **/tmp**
terraform_bin_path         | Defined to dynamically set the appropriate path to store terraform binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**
terraform_file_owner       | Owner for the binary file of terraform.
terraform_file_group       | Group for the binary file of terraform.
terraform_file_mode        | Mode for the binary file of terraform.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **terraform**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.terraform
```

For customizing behavior of role (i.e. specifying the desired **terraform** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.terraform
  vars:
    terraform_version: 0.12.27
```

For customizing behavior of role (i.e. placing binary of **terraform** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.terraform
  vars:
    terraform_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-terraform/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
