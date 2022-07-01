# Ansible Role for Generating Subuids & Subgids

Creates subuid & subgid mappings for users.

Inspired from this blog article <https://eengstrom.github.io/musings/generate-non-contiguous-subuid-subgid-maps-for-rootless-podman>

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
