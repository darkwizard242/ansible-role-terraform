[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-terraform.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-terraform) ![Ansible Role](https://img.shields.io/ansible/role/42050?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/42050?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/42050?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-terraform&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-terraform) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-terraform?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-terraform?color=orange&style=flat-square)

# Ansible Role: Terraform

Role to install (_by default_) [terraform](https://www.terraform.io/) package on **Debian/Ubuntu** and **EL** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
terraform_app: terraform
terraform_version: 0.12.28
terraform_osarch: linux_amd64
terraform_dl_url: https://releases.hashicorp.com
terraform_dl_loc: /tmp
terraform_bin_path: /usr/local/bin
```

### Variables table:

Variable           | Value (default)                  | Description
------------------ | -------------------------------- | -----------------------------------------------------------------------------------------------------------------------------------------------------------
terraform_app      | terraform                        | Defines the app to install i.e. **terraform**
terraform_version  | 0.12.28                          | Defined to dynamically fetch the desired version to install. Defaults to: **0.12.28**
terraform_osarch   | linux_amd64                      | Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture. Defaults to: **linux_amd64**
terraform_dl_url   | <https://releases.hashicorp.com> | Defines URL to download the terraform binary from.
terraform_dl_loc   | /tmp                             | Defined to dynamically set where to place the binary archive for `terraform` temporarily. Defaults to: **/tmp**
terraform_bin_path | /usr/local/bin                   | Defined to dynamically set the appropriate path to store terraform binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**

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

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
