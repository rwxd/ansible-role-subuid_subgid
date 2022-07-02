# Ansible Role for Generating Subuids & Subgids

Creates subuid & subgid mappings for users.

Inspired from this blog article <https://eengstrom.github.io/musings/generate-non-contiguous-subuid-subgid-maps-for-rootless-podman>

## Install

`roles/requirements.yml`

```bash
---
roles:
  - name: subuid_subgid
    version: v1.0.2
    src: git@github.com:rwxd/ansible-role-subuid_subgid.git
    scm: git
```

`ansible.cfg`

```bash
[defaults]
roles_path=./roles
```

Get requirements with `ansible-galaxy role install -r roles/requirements.yml`

## Usage

A `subid_users` variable is required e.g.:

```yaml
- name: Set users
  set_fact:
    subid_users:
      - peter
      - james

- name: Generate subuids & subgids
  include_role:
    name: subuid_subgid
```

`/etc/subuid` will contain

```bash
peter:65929216:65536
james:65470464:65536
```

`/etc/subgid` will contain

```bash
peter:65929216:65536
james:65470464:65536
```
