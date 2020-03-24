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
$ kubenvz kubectl install 1.16.0
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

## Fast switcher

To have a faster switch between version, install the kbnvz tool:

```bash
wget https://github.com/nutellinoit/kubenvz/releases/download/v0.2.3/kbnvz_v0.2.3 -O /usr/local/bin/kbnvz
chmod +x /usr/local/bin/kbnvz
```

### kbnvz <kubectl / kustomize / helm / helmfile> [local_version]

To use the fast switcher script:

```bash
kbnvz kustomize 1.0.10
```

## Develop

Create a virtualenv:

```bash
python3 -m venv .
```

Start virtualenv:

```bash
source bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```


## LICENSE

- [kubenvz](https://github.com/nutellinoit/kubenvz/blob/master/LICENSE)
- [terraenv](https://github.com/aaratn/terraenv/blob/master/LICENSE)
- [rbenv](https://github.com/rbenv/rbenv/blob/master/LICENSE)

## Inspiration

- [terraenv](https://github.com/aaratn/terraenv/blob/master/LICENSE)
- [tfenv](https://github.com/tfutils/tfenv)
- [tgenv](https://github.com/cunymatthieu/tgenv)
- [rbenv](https://github.com/rbenv/rbenv)
