# Ansible Role for Generating Subuids & Subgids

Creates subuid & subgid mappings for users.

Inspired from this blog article <https://eengstrom.github.io/musings/generate-non-contiguous-subuid-subgid-maps-for-rootless-podman>

## Usage

A `users` variable is required e.g.:

```yaml
users:
  - peter
  - james
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
