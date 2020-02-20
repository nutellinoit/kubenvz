[![Actions Status](https://github.com/nutellinoit/kubenvz/workflows/Test/badge.svg)](https://github.com/nutellinoit/kubenvz/actions)

[![Actions Status](https://github.com/nutellinoit/kubenvz/workflows/Build%20&%20Release/badge.svg)](https://github.com/nutellinoit/kubenvz/actions)

# Kubenvz

kubectl & kustomize & helm & helmfile version manager

Inspired by terraenv https://github.com/aaratn/terraenv

## Installation

### Automatic

Install via Homebrew on OSx

```console
$ brew tap nutellinoit/kubenvz
$ brew install kubenvz
```
### Upgrade

via Homebrew on OSx

```console
$ brew upgrade kubenvz
```


## Usage

### kubenvz <kubectl / kustomize / helm / helmfile> install [remote_version]

Install a specific version of kubectl/kustomize/helm/helmfile , list available remote versions with `kubenvz kustomize list remote`  :

- `kustomize/v.X.X.X` use exact version to install

> kustomize has lot of release, kubenvz filter all releases that are not cli executable


```console
$ kubenvz kubectl install v1.16.0
$ kubenvz kustomize install 1.0.10
$ kubenvz helm install v3.1.0
$ kubenvz helmfile install v0.100.1
```

## kubenvz <kubectl / kustomize / helm / helmfile> list <remote / local>

To list local installed version use:

```bash
kubenvz kustomize list local
```

## kubenvz <kubectl / kustomize / helm / helmfile> use [local_version]

To use a local installed version:

```bash
kubenvz kustomize use 1.0.10
```


## LICENSE

- [kubenvz](https://github.com/aaratn/kubenvz/blob/master/LICENSE)
- [terraenv](https://github.com/aaratn/terraenv/blob/master/LICENSE)
- [rbenv](https://github.com/rbenv/rbenv/blob/master/LICENSE)

## Inspiration

- [terraenv](https://github.com/aaratn/terraenv/blob/master/LICENSE)
- [tfenv](https://github.com/tfutils/tfenv)
- [tgenv](https://github.com/cunymatthieu/tgenv)
- [rbenv](https://github.com/rbenv/rbenv)
